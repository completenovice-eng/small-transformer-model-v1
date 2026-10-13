# SPDX-License-Identifier: MIT
# Copyright (c) 2026 completenovice-eng
"""Standalone public-subset audit. No model dependencies, network or private data."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import struct
import xml.etree.ElementTree as ET

PATTERNS={
 'local_path':r'/home/[^/\s"<>]+|/mnt/[a-z]/[^\s"<>]+|/Users/[^/\s]+|(?<![A-Za-z])[A-Z]:[\\/][^\s]+',
 'email':r'\b[A-Za-z0-9_.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
 'credential':r'sk-[A-Za-z0-9_-]{24,}|ghp_[A-Za-z0-9]{36}|AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
 'url_credential':r'https?://[^\s/@:]+:[^\s/@]+@',
 'secret_query':r'[?&](?:api_key|apikey|access_token|token|password)=[A-Za-z0-9_%.-]{8,}',
 'assigned_secret':r'''(?:api[_-]?key|access[_-]?token|secret|password)\s*[:=]\s*["'][^"'\s]{8,}''',
 'private_url':r'https?://(?:localhost|127\.0\.0\.1|10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+|[^\s/]+\.internal)(?=[:/\s]|$)',
 'modern_github_token':r'github_pat_[A-Za-z0-9_]{30,}',
 'cloud_or_service_token':r'(?:gh[ousr]_[A-Za-z0-9]{36}|xox[baprs]-[A-Za-z0-9-]{20,})',
 'machine_id':r'GPU-[0-9a-fA-F-]{30,}|(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}',
}
FORBIDDEN={'.git','.gitmodules','.ssh','.aws','.codex','RECOVERY.md','FINAL_RECORD.json','__pycache__'}


def require(ok,message):
 if not ok:raise ValueError(message)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def scan(text):
 return {k:len(re.findall(pattern,text,re.I)) for k,pattern in PATTERNS.items() if re.search(pattern,text,re.I)}


def scan_source(text):
 # Audit detector definitions as code, rather than interpreting regex text as a real path.
 lines=text.splitlines()
 for node in ast.parse(text).body:
  if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PATTERNS' for t in node.targets):
   require(ast.literal_eval(node.value)==PATTERNS,'DETECTOR_DEFINITION_CHANGED')
   lines[node.lineno-1:node.end_lineno]=['']*(node.end_lineno-node.lineno+1)
 return scan('\n'.join(lines))


def png_metadata(p):
 data=Path(p).read_bytes();require(data[:8]==b'\x89PNG\r\n\x1a\n','PNG_SIGNATURE')
 i=8;text={};ended=False
 while i<len(data):
  require(i+12<=len(data),'PNG_CHUNK_BOUNDARY')
  n=struct.unpack('>I',data[i:i+4])[0];kind=data[i+4:i+8];body=data[i+8:i+8+n]
  require(i+n+12<=len(data),'PNG_CHUNK_SIZE');i+=n+12
  if kind==b'tEXt':
   k,v=body.split(b'\0',1);text[k.decode('latin1')]=v.decode('latin1')
  require(kind not in {b'iTXt',b'zTXt',b'eXIf'},'PNG_UNREVIEWED_METADATA')
  require(kind in {b'IHDR',b'IDAT',b'IEND',b'pHYs',b'tEXt'},'PNG_UNREVIEWED_CHUNK')
  if kind==b'IEND':ended=True;break
 require(ended and i==len(data),'PNG_TRAILING_PAYLOAD')
 require(set(text)<= {'Software'} and all(v in {'Model v1 P1 saved-data plotting','Model v1 publication display'} for v in text.values()),'PNG_METADATA_VALUE')
 return text


def check_links(root,p):
 n=0
 for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text()):
  if ref.startswith(('https://','http://')):continue
  name,_,anchor=ref.partition('#');target=(p.parent/name).resolve() if name else p.resolve()
  require(target.is_relative_to(root.resolve()),'LINK_ESCAPES_EXPORT')
  require(target.exists(),'BROKEN_LINK:'+ref)
  if anchor:require('id="'+anchor+'"' in target.read_text(),'BROKEN_ANCHOR:'+anchor)
  n+=1
 return n


def audit(root):
 require(not Path(root).is_symlink(),'EXPORT_ROOT_SYMLINK')
 root=Path(root).resolve();manifest=root/'evidence/export_manifest.json'
 m=json.loads(manifest.read_text());expected=set(m['files'])|{'evidence/export_manifest.json'}
 found=set();links=0;metadata={}
 for p in root.rglob('*'):
  rel=p.relative_to(root)
  require(not p.is_symlink(),'SYMLINK_FORBIDDEN')
  if rel.parts[0]=='.git':
   require((root/'.git').is_dir() and not (root/'.git').is_symlink(),'INVALID_LOCAL_GIT_DIRECTORY')
   continue
  require(not any(s in FORBIDDEN for s in rel.parts),'PRIVATE_CONTROL_FILE_FORBIDDEN')
  require(not any(s.startswith('.') for s in rel.parts),'HIDDEN_FILE_FORBIDDEN')
  if not p.is_file():continue
  found.add(rel.as_posix());require(rel.as_posix() in expected,'NON_WHITELIST_FILE:'+str(rel))
  require(p.suffix not in {'.pt','.pth','.ckpt','.safetensors','.bin','.model','.vocab','.sqlite','.jsonl','.pem','.key'},'UNAPPROVED_ASSET_TYPE')
  if p.suffix=='.png':metadata[rel.as_posix()]=png_metadata(p)
  else:
   text=p.read_text('utf-8');require('\ufffd' not in text,'UTF8_REPLACEMENT_CHARACTER')
   findings=scan_source(text) if p.name=='audit_public_export.py' else scan(text)
   require(not findings,'SAFETY_PATTERN:'+str(rel)+':'+str(list(findings)))
   if p.suffix=='.md':
    links+=check_links(root,p)
    require(text.count('```')%2==0,'UNBALANCED_CODE_FENCE')
   if p.suffix=='.svg':
    tree=ET.fromstring(text)
    for el in tree.iter():
     require(el.tag.split('}')[-1] not in {'script','foreignObject'},'ACTIVE_SVG_CONTENT')
     for key,value in el.attrib.items():
      require(not key.lower().startswith('on'),'SVG_EVENT_HANDLER')
      if key.split('}')[-1]=='href':require(value.startswith(('#','data:image/png;base64,')),'SVG_EXTERNAL_REFERENCE')
 for rel,entry in m['files'].items():require(sha(root/rel)==entry['sha256'],'FILE_SHA:'+rel)
 require(found==expected,'WHITELIST_INCOMPLETE')
 claims=json.loads((root/'evidence/claim_sources.json').read_text())
 require(len(claims['claims'])==31 and claims['scientific_primary_approvals']==0,'CLAIM_SCOPE')
 require(claims['h2_status_counts']=={'CONFIRMED_FROM_RAW':5,'CONFIRMED_FROM_MANIFEST':55,'CONFIRMED_FROM_CODE':5,'REPORTED_ONLY':6,'ESTIMATED':1,'UNVERIFIED':2},'EVIDENCE_LEVELS')
 report=(root/'report/technical_report.md').read_text();readme=(root/'README.md').read_text()
 for text in [report,readme]:
  for token in ['DESCRIPTIVE_ONLY','Primary','1/15','未成立']:
   require(token in text,'PUBLIC_SCIENTIFIC_LIMIT_MISSING:'+token)
 for p in (root/'figures').rglob('*.svg'):
  require('DRAFT_INTERNAL' not in p.read_text() and 'interim draft' not in p.read_text(),'INTERNAL_FIGURE_MARKER')
 for c in claims['claims']:
  require(c['claim_id'] in report,'CLAIM_MISSING:'+c['claim_id'])
 scope=json.loads((root/'licensing/SCOPE.json').read_text())
 require(set(scope['files'])==found,'LICENSE_SCOPE_COVERAGE')
 require(m['author']=='completenovice-eng' and m['publication_authorized'] is True,'AUTHOR_AND_RELEASE_GATE')
 require(m['license_state']=='APPROVED_SCOPE_CC_BY_4_MIT','LICENSE_APPROVAL')
 for rel,e in scope['files'].items():
  expected_license='MIT' if rel.startswith('scripts/') else ('LicenseRef-Standard-License-Text' if rel.startswith('LICENSES/') else 'CC-BY-4.0')
  require(e['license']==expected_license and e['third_party_rights_relicensed'] is False,'PER_FILE_LICENSE:'+rel)
 for rel,h in scope['standard_text_sha256'].items():require(sha(root/rel)==h,'STANDARD_LICENSE_TEXT_SHA')
 require('2026 completenovice-eng' in (root/'LICENSES/MIT.txt').read_text(),'MIT_RIGHTSHOLDER')
 require('licensing/PROPOSALS.md' not in found,'SUPERSEDED_LICENSE_PROPOSAL')
 if (root/'evidence/reproduction_receipt.json').exists():
  receipt=json.loads((root/'evidence/reproduction_receipt.json').read_text())
  require(receipt['status']=='PASS' and receipt['images']==14,'REPRODUCTION_RECEIPT')
  for rel,h in (receipt['data_sha256']|receipt['image_sha256']).items():require(sha(root/rel)==h,'REPRODUCTION_SOURCE_BINDING')
 return {'technical_status':'PASS','publication_status':'PUBLIC_OBS5_INTERIM_REPORT','publication_authorized':True,
         'file_count':len(found),'total_bytes':sum((root/r).stat().st_size for r in found),
         'local_links_checked':links,'PNG_metadata':metadata,'claims':31,'negative_records':14,
         'original_research_Git_history':'NOT_INCLUDED','local_Git_present':(root/'.git').exists(),'commit_identity_check':'SEPARATE_RELEASE_VERIFICATION_REQUIRED',
         'symlinks':0,'submodules':0,'known_pattern_findings':0,
         'limitations':'Automated negative scan is not a safety guarantee. Researcher authorized release; commit history and identity require separate release verification. No model/raw training reproducibility from public aggregates.'}


def main():
 parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);parser.add_argument('--output',type=Path)
 args=parser.parse_args();result=audit(args.root)
 text=json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
 if args.output:args.output.write_text(text)
 else:print(text)


if __name__=='__main__':main()
