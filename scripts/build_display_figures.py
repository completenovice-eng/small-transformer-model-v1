# SPDX-License-Identifier: MIT
# Copyright (c) 2026 completenovice-eng
"""Publication-only Japanese layouts from saved aggregate CSV. No model code."""
import argparse
import csv
import hashlib
import json
from pathlib import Path

FONT_SHA='68a3fc98800b2a27b371f2fb79991daf3633bd89309d4ffaa6946fd587f375b5'
FONT_URL='https://raw.githubusercontent.com/notofonts/noto-cjk/main/Sans/OTF/Japanese/NotoSansCJKjp-Regular.otf'
FONT_LICENSE='https://github.com/notofonts/noto-cjk/blob/main/Sans/LICENSE'


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def rows(data,name):
    with (Path(data)/(name+'.csv')).open() as f:
        return list(csv.DictReader(f))


def draw(data,font,output):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
    from matplotlib.patches import FancyBboxPatch
    import numpy as np
    if matplotlib.__version__!='3.10.7' or np.__version__!='2.2.6':
        raise ValueError('PINNED_PLOT_ENV_REQUIRED')
    if sha(font)!=FONT_SHA:
        raise ValueError('FONT_SHA_MISMATCH')
    output=Path(output)
    output.mkdir(parents=True,exist_ok=False)
    font_manager.fontManager.addfont(str(font))
    family=font_manager.FontProperties(fname=str(font)).get_name()
    plt.rcParams.update({'font.family':family,'font.size':12,'axes.titlesize':13,
        'axes.labelsize':12,'xtick.labelsize':12,'ytick.labelsize':12,
        'legend.fontsize':11.5,'axes.spines.top':False,'axes.spines.right':False,
        'svg.fonttype':'none','svg.hashsalt':'model-v1-display-ja-v1','savefig.facecolor':'white'})
    inventory=[]
    def save(fig,name,source_figures,input_names,meaning):
        footer='OBS-5時点の中間報告／記述的資料\n科学的Primary承認0'
        fig.text(.5,.014,footer,ha='center',va='bottom',fontsize=11.5,color='#444444',linespacing=1.5)
        fig.canvas.draw()
        renderer=fig.canvas.get_renderer()
        for text in fig.texts:
            box=text.get_window_extent(renderer)
            if box.x0<0 or box.y0<0 or box.x1>fig.bbox.width or box.y1>fig.bbox.height:
                raise ValueError('FIGURE_TEXT_CLIPPED')
            for ax in fig.axes:
                if ax.get_xlabel() and box.overlaps(ax.xaxis.label.get_window_extent(renderer)):
                    raise ValueError('FOOTER_AXIS_LABEL_OVERLAP')
        # Fixed canvas (no tight crop) keeps minimum text size known at 360 CSS px.
        for ext in ['png','svg']:
            metadata={'Software':'Model v1 publication display'} if ext=='png' else {'Date':None,'Creator':'Model v1 publication display'}
            fig.savefig(output/(name+'.'+ext),dpi=240,metadata=metadata)
            if ext=='svg':
                p=output/(name+'.svg')
                p.write_text('\n'.join(line.rstrip() for line in p.read_text().splitlines())+'\n')
        inventory.append({'name':name,'source_figures':source_figures,'inputs':input_names,'meaning':meaning,
            'canvas_width_inches':3.6,'dpi':240,'minimum_font_points':11.5,
            'minimum_font_css_px_at_360':11.5*360/(3.6*72),
            'outputs':{name+'.'+ext:sha(output/(name+'.'+ext)) for ext in ['png','svg']}})
        plt.close(fig)

    # Same decision history; four Japanese cards combine the original six stages.
    fig,ax=plt.subplots(figsize=(3.6,7.0))
    ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    fig.subplots_adjust(left=.04,right=.96,top=.91,bottom=.11)
    fig.suptitle('図1　研究の経緯',fontsize=15,y=.977)
    stages=[('1　出発点','学習経験と能力形成の関係\n形成時期・一般化・内部変化'),
        ('2　評価方法の監査','通常の問題継続では正答未確立\n対応問題を使う測定を構築'),
        ('3　較正で陽性未成立','原実験：36/1,024問 正答\n限定課題：38/512問 正答'),
        ('4　記述的観察へ変更','能力の認定を保留\n10M／混合条件：1/15本 完了')]
    for i,(title,text) in enumerate(stages):
        top=.985-i*.239
        ax.add_patch(FancyBboxPatch((.01,top-.207),.98,.207,boxstyle='round,pad=.004',
            facecolor='#eef4f7' if i<3 else '#f7eddb',edgecolor='#6a8190'))
        ax.text(.05,top-.031,title,fontsize=13,va='top',color='#17394c')
        ax.text(.05,top-.091,text,fontsize=11.5,va='top',linespacing=1.7)
    save(fig,'note_fig01_history_ja',[1],[],
         'Research history schematic; four cards combine all six original stages; no time scale or new outcome.')

    trajectory=rows(data,'limited_m3_trajectory')
    terminal=rows(data,'limited_m3_terminal')
    counts={r['role']:(int(r['exact_correct']),int(r['N_sides'])) for r in terminal}
    assert counts=={'training_fit':(511,512),'development':(34,256),'world_disjoint_heldout':(38,512)}
    fig,axes=plt.subplots(2,1,figsize=(3.6,8.9))
    fig.subplots_adjust(left=.20,right=.96,top=.83,bottom=.27,hspace=.82)
    fig.suptitle('図2　限定M3の較正\n20M／1初期化・1回の実行',fontsize=15,y=.978,linespacing=1.6)
    fig.text(.5,.883,'学習予測 50,004,416回',ha='center',fontsize=12)
    colors=['#287f8e','#b66a2a','#a63253']
    labels=['既知問題\n511/512','開発用\n34/256','未見世界\n38/512']
    values=[511/512*100,34/256*100,38/512*100]
    axes[0].bar(range(3),values,color=colors,width=.65)
    axes[0].set_xticks(range(3),labels,fontsize=11.5)
    axes[0].set(ylim=(0,110),yticks=[0,50,100],ylabel='正答率（%）')
    axes[0].axhline(90,color='#555555',linestyle=':',linewidth=1.3)
    axes[0].set_title('最終状態の独立正答評価',pad=12)
    axes[0].grid(axis='y',alpha=.16)
    xs=[int(r['predictions'])/1e6 for r in trajectory]
    for key,n,color,label in [('fit_exact',512,colors[0],'既知問題'),('development_exact',256,colors[1],'開発用')]:
        axes[1].plot(xs,[int(r[key])/n*100 for r in trajectory],'o-',color=color,label=label,linewidth=1.6,markersize=4)
    axes[1].scatter([xs[-1]],[38/512*100],marker='D',s=35,color=colors[2],label='未見世界（最終のみ）',zorder=4)
    axes[1].set(xlim=(0,51),ylim=(0,105),xticks=[0,25,50],yticks=[0,50,100],
        xlabel='学習予測回数（百万回）',ylabel='正答率（%）')
    axes[1].set_title('固定時点の推移',pad=10)
    axes[1].legend(loc='center right',framealpha=.95)
    axes[1].grid(alpha=.16)
    fig.text(.5,.16,'90%線だけで陽性成立とはしない\n未見の両側生成正答 0/256組\nStage Cの採点器評価は未実行',ha='center',va='top',fontsize=11.5,linespacing=1.6)
    save(fig,'note_fig02_limited_m3_ja',[7],['limited_m3_trajectory','limited_m3_terminal'],
         'Same five saved observations and terminal counts; 0/256 is independent generation, not paired scorer; no capability or causal attribution.')

    train=rows(data,'training_intervals')
    assert len(train)==24
    fig,axes=plt.subplots(2,1,figsize=(3.6,8.6))
    fig.subplots_adjust(left=.20,right=.96,top=.84,bottom=.27,hspace=.62)
    fig.suptitle('図3　10M／混合条件の学習loss\n61,156更新／約20億回の予測',fontsize=14,y=.978,linespacing=1.6)
    for ax in axes:
        for r in train:
            ax.hlines(float(r['interval_mean_loss']),(int(r['interval_start_update'])-1)*32704/1e9,
                int(r['predictions'])/1e9,color='#267a9b',linewidth=2)
        ax.scatter([int(r['predictions'])/1e9 for r in train],[float(r['endpoint_batch_loss']) for r in train],
            color='#bc6735',marker='x',s=18,zorder=3)
        ax.set(xlim=(0,2.000045824),ylim=(0,10),yticks=[0,5,10],
            xlabel='学習予測回数（十億回）',ylabel='予測誤差（nats／予測）')
        ax.grid(alpha=.16)
    axes[0].set_title('全期間（通常の横軸）',pad=12)
    axes[0].set_xticks([0,1,2])
    axes[1].set_xscale('symlog',linthresh=.001)
    axes[1].set_xticks([0,.001,.01,.1,2],['0','.001','.01','.1','2'])
    axes[1].set_title('同じ値を初期から見る\n横軸はsymlog',pad=12,fontsize=12)
    fig.text(.5,.16,'青線：固定区間の平均\n橙の×：区間終端のbatch loss\n学習前のlossは補っていない',ha='center',va='top',fontsize=11.5,linespacing=1.6)
    save(fig,'note_fig03_training_loss_ja',[3],['training_intervals'],
         'Same 24 nonoverlapping interval means and endpoint batches; unchanged full y0–10, x0–exact2B, symlog linthresh .001; stacked instead of side by side.')
    receipt={'version':'display-ja-v1','model_forward':0,'training':0,'font':{'url':FONT_URL,'sha256':FONT_SHA,
        'license_url':FONT_LICENSE,'license':'SIL-OFL-1.1','bundled':False},
        'data_sha256':{n+'.csv':sha(Path(data)/(n+'.csv')) for n in ['training_intervals','limited_m3_trajectory','limited_m3_terminal']},
        'minimum_font_css_px_at_360':11.5*360/(3.6*72),'figures':inventory,
        'actual_note_UI':'NOT_TESTED;360px raster previews are local layout checks only'}
    (output/'display_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    return receipt


def main():
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True)
    p.add_argument('--font',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();draw(a.data,a.font,a.output)


if __name__=='__main__':main()
