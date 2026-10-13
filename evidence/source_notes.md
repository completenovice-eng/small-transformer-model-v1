# 公開用の原本説明と証拠水準

これは非公開H2台帳そのものではなく、P01–P31が使うfactの公開用要約である。raw/manifest/code確認という元statusは当時の内部検証範囲を示し、公開subsetだけで独立確認済みという意味ではない。
SHAや研究commitは原本識別のためのfingerprintであり、非公開内容を復元する手段ではない。

<a id="training-contract"></a>
## Training contract

E1はcontext512/A2/architecture/NaturalR1/exact2Bを固定した。訓練source/weightsと全実行環境はここに同梱していない。技術報告§5の数値とseedは契約からの転記である。

<a id="synthetic-support"></a>
## Synthetic support

family1–3 TRAIN/4heldout、sampling/rejection/renderersはpilot-equivalentで採用。本文は問題のみでoracle completionなし。厳密なgenerator全体やraw inventoryは非公開で、要約だけで分布全体を再現できるとはしない。

<a id="obs5-execution"></a>
## OBS5 execution

10M/MIX/r0の1/15のみ完了。予定/実消費batch照合・checkpoint保存・9Fullの原receiptは非公開。公開CSVは保存集計の派生物であり、元checkpointを第三者が検証した資料ではない。

<a id="observation-freeze"></a>
## Observation freeze

15本のdesignと測定仕様を固定。科学的妥当性承認ではない。旧execution_authorized=false proposalとOBS5明示承認overlayを別に保持。ここへ元freeze manifest全文/履歴はコピーしていない。

<a id="f001"></a>
## F001 — CONFIRMED_FROM_CODE

当初目的はscratch decoder-only Transformerの能力形成時刻、size/domain/transfer差、内部表現・回路との関係であり、実用小型LM最適化ではなかった。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `2209bb1e0c469d26b213c18c9e2e4e4537f66891`。公開URLを意味しない。

<a id="f002"></a>
## F002 — CONFIRMED_FROM_CODE

当初は5 discovery +5 fresh confirmation、暫定4/5方向規則、行動/機構関連/因果のA/B/C区分。replication unitはmodel seedであった。

制限: 当時の概念計画。OBSのr0設計や記述的結果へ確認的規則を自動適用しない。

非公開原記録commit: `2209bb1e0c469d26b213c18c9e2e4e4537f66891`。公開URLを意味しない。

<a id="f003"></a>
## F003 — CONFIRMED_FROM_CODE

architecture、precision、optimizer数値、context、tokenizer、T_max、cadence、統計手続は当初Pilot-resolved。T_signalの99%CI/3点とfinal/plateau変化比landmarksも暫定だった。

制限: 後の仕様を当初から決定済みと書かない。観察研究では旧landmarksは採用していない。

非公開原記録commit: `2209bb1e0c469d26b213c18c9e2e4e4537f66891`。公開URLを意味しない。

<a id="f004"></a>
## F004 — CONFIRMED_FROM_CODE

Phase0.5はlatent/render分離、family1–3 TRAIN/family4 heldout、metadata solver、split/seed namespaceを構想。Natural N0/N2とtransfer P1–P7も提案した。

制限: この構想の全てを実装・測定したわけではない。実MainはTinyStories R1と36cell bank。

非公開原記録commit: `2209bb1e0c469d26b213c18c9e2e4e4537f66891`。公開URLを意味しない。

<a id="f005"></a>
## F005 — REPORTED_ONLY

Logic/Math/Codeのgenerator・独立validator・counterfactual・renderer監査後synthetic-v1をfreeze。L/M/C番号は難易度順ではない。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。 / H2は当時のselection/freeze reportをreadback。元dataset/tokenizer実験を再監査していない。

非公開原記録commit: `c1abf958341044129fdd619ca3be6271f6984108`。公開URLを意味しない。

<a id="f006"></a>
## F006 — REPORTED_ONLY

TinyStories raw→selection v0.2→human decision overlayの来歴を保持。後のNatural freeze/R1がMainのNatural資産となった。

制限: 本研究で成人N0/N2生成比較を実施したとは言わない。human selection記録とfreeze actionを区別。 / H2は当時のselection/freeze reportをreadback。元dataset/tokenizer実験を再監査していない。

非公開原記録commit: `fb70e3681496bfdd30ca0f64cd9bde4fadb92b37`。公開URLを意味しない。

<a id="f015"></a>
## F015 — REPORTED_ONLY

D3-Aは技術中断とNaturalのみの隔離復旧を記録して1.5Bまで監査。失敗attemptは後続成功で消していない。

制限: H2では重み/実resumeを再実行しない。詳細原因と影響はD3-A/D3-C原本。

非公開原記録commit: `7483299d59dda719fa19af5b3e76d3d66f4dc71b`。公開URLを意味しない。

<a id="f016"></a>
## F016 — CONFIRMED_FROM_MANIFEST

D3-Bで20M MIX/PURE-LOGIC/PURE-NATURALを共通exact2Bまで完走。PURE-MATH/CODEの2B直接検証ではない。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `a36945f0fad851e6b4a9932a47a46686475a2b74`。公開URLを意味しない。

<a id="f017"></a>
## F017 — CONFIRMED_FROM_MANIFEST

D3-Cは3条件各61,156 finite updates、historical SHA監査1,953 files/238,603,088,954 bytesとresumeを照合。能力妥当性を確立した監査ではない。

制限: H2で238GB再SHA監査やモデルloadを実施したとは主張しない。

非公開原記録commit: `a66ef61ee47346e5577ad503ddb151db7d66712e`。公開URLを意味しない。

<a id="f018"></a>
## F018 — CONFIRMED_FROM_MANIFEST

E1は共通context512、A2、Natural R1、exact2,000,045,824 predictionsをfreeze。64×511×61,156。全サイズで同condition/r0 token sequence共有。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `19274e7363ed8ea122334dda10faa6409912aaf1`。公開URLを意味しない。

<a id="f019"></a>
## F019 — CONFIRMED_FROM_MANIFEST

10M/20M/30Mはnonembedding10626816/18887680/29507840、total13772544/23081984/34750720。tied8192×widthを除きLNを含む。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `19274e7363ed8ea122334dda10faa6409912aaf1`。公開URLを意味しない。

<a id="f020"></a>
## F020 — CONFIRMED_FROM_MANIFEST

A2 AdamW LR6e-4、betas(.9,.95)、eps1e-8、wd.1全parameter、clip1、2M warmup後constant、batch64/micro32×2。BF16/FP32、externalEOS、全shifted targets。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `19274e7363ed8ea122334dda10faa6409912aaf1`。公開URLを意味しない。

<a id="f021"></a>
## F021 — CONFIRMED_FROM_MANIFEST

E2-Aは36 proposed cellsと108 answer-adapter review examplesを設計。TRAIN completionの妥当性問題は後続監査で判定。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `5cfcc4895a1ae4f7590a84ae641e31af25bb92a8`。公開URLを意味しない。

<a id="f022"></a>
## F022 — CONFIRMED_FROM_MANIFEST

native-format primary feasible=0/36。TRAIN本文にはoracle answer completionがなく、共通prefix後の双方が有効な問題になり得た。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `15019fab4c324772a0e3151d172cbbffe5f72109`。公開URLを意味しない。

<a id="f024"></a>
## F024 — CONFIRMED_FROM_MANIFEST

保存済み4domain TRAIN token auditで共通positive target exposureはEOSのみ。safe arbitrary label pair未実証、primary candidate0。

制限: 有限bankの実測であり全seedの不可能性定理ではない。EOSはanswer labelに使わない。

非公開原記録commit: `7be83da7217f649a9b27d400a7a980c7b345f232`。公開URLを意味しない。

<a id="f027"></a>
## F027 — CONFIRMED_FROM_MANIFEST

E2-S1はeval coverageと独立にpilot-equivalent TRAIN supportを正式採用。support/sampling lawは同一、seed固有実streamはbounded referenceのみexact検証。material changeなし、long-horizon rerun不要。

制限: same support、same law、same realized streamは別。main seed/matrix/cadenceは当時未確定。

非公開原記録commit: `a24a5d57632c084b69f8335f87d00f4271f37689`。公開URLを意味しない。

<a id="f028"></a>
## F028 — CONFIRMED_FROM_MANIFEST

E2-B1 construction PASS36/36、27,754blocks、1,280controls、3,102negative diagnostics。Primary scientific approval0。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `3d0dd787cb3122e08c6e10ba0c966ea2497c363d`。公開URLを意味しない。

<a id="f029"></a>
## F029 — CONFIRMED_FROM_MANIFEST

raw candidate token IDsで15cells/211 nested-answer blocksを同定。短候補が長候補のtoken prefixだとsum-LL長候補が不利となるscorer制約。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `1f734f28e2c9a25a2033285d55085f5101058939`。公開URLを意味しない。

<a id="f030"></a>
## F030 — CONFIRMED_FROM_MANIFEST

自然で構成維持する代替foilを確立せず211 whole blocksを除去。27,543blocks、3,081diagnosticsへ別version修正、E2-B1原本とscorerは不変。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `0dac47829181215744c8817d408bea7e63a1be7e`。公開URLを意味しない。

<a id="f031"></a>
## F031 — CONFIRMED_FROM_MANIFEST

36/36 deterministic measurement VALID、construct LIMITED、claim DESCRIPTIVE_ONLY、scientific Primary approval0。13,319 unequal/14,224 equal answer-token-length blocksを保持。

制限: equal subsetはlatent compositionを変えるためPrimary救済に採用していない。

非公開原記録commit: `5cee366915035580f43b1df9b122b179cfa17e09`。公開URLを意味しない。

<a id="f032"></a>
## F032 — CONFIRMED_FROM_MANIFEST

M=(d0-d1)/2。exp(2m)は2context間candidate likelihood-ratioの比。strict PAIR_CORRECTとmean marginは別、chance .25未正当化、sign randomization未承認。

制限: raw sum-LL、EOS非採点、length normなし、whole-string boundaryとcausal i−1。

非公開原記録commit: `5cee366915035580f43b1df9b122b179cfa17e09`。公開URLを意味しない。

<a id="f034"></a>
## F034 — CONFIRMED_FROM_MANIFEST

12familiesはM3のみ比較的direct predictive pathway、8indirect、family4の3つはown-family TRAINなし。M3 RHS予測と逆問題解答は同じ能力ではない。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `d74aac7705d2a2b55c3113744306b9d4213edaf2`。公開URLを意味しない。

<a id="f035"></a>
## F035 — CONFIRMED_FROM_MANIFEST

oracle/validatorの呼出しだけではlearning pressureと認定せず、acceptance、sampling、rendered predictive dependenciesを追跡した。fとf-primeの識別不能/不明な経路を残した。

制限: pressureの大きさや能力形成確率の定量的証明ではない。Natural/MIX関連知識への接触も否定しない。

非公開原記録commit: `d74aac7705d2a2b55c3113744306b9d4213edaf2`。公開URLを意味しない。

<a id="f036"></a>
## F036 — REPORTED_ONLY

外部AI設計reviewを受けたuser-directed変更という記録があるが、review原文はC1に供給・独立監査されていない。

制限: 会話ではAstra/SuperGrok/Claudeとされる。全文/発言者別提案/正確な時刻を原本から復元できない。

非公開原記録commit: `d74aac7705d2a2b55c3113744306b9d4213edaf2`。公開URLを意味しない。

<a id="f037"></a>
## F037 — UNVERIFIED

外部AI reviewの完全なtranscriptと各提案の採用対応はこのrepository証拠から未検証。

制限: レビュー要約やAI意見は独立実験証拠ではない。原文入手時に追記、推測で補完しない。

非公開原記録commit: `d74aac7705d2a2b55c3113744306b9d4213edaf2`。公開URLを意味しない。

<a id="f038"></a>
## F038 — CONFIRMED_FROM_MANIFEST

model-free local/numeric/editing heuristicsに高成績例。C3/interpolation local direction815/1012両側正答、M3/value_ood antitone826/1014。

制限: static baselinesでありTransformerが採用した証拠でもshortcut ceilingでもない。

非公開原記録commit: `a03cbffa313019ce6c567ed8945b1f85b8342368`。公開URLを意味しない。

<a id="f039"></a>
## F039 — CONFIRMED_FROM_MANIFEST

literal-key lookupは5control banks各256/256。FORMAT/SELECTION/REPRESENTATIONはlookup semanticsを検査できてもlatent rule理解を保証しない。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `a03cbffa313019ce6c567ed8945b1f85b8342368`。公開URLを意味しない。

<a id="f041"></a>
## F041 — CONFIRMED_FROM_MANIFEST

C3 preflightはZERO/INTERFACE_ONLY/RULE_POSITIVE/DEPENDENCY_BROKENを分離、独立competenceとdev/sealed隔離を設計。5,120calibration blocks/768controlsを準備。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `b51c737ba810fda5db1461b964ed979d46fd5a03`。公開URLを意味しない。

<a id="f049"></a>
## F049 — CONFIRMED_FROM_MANIFEST

既存M3/interpolation counterfactual569/986の解がTRAIN抽選範囲外と確認。calibrationは両側support済みの別pool、Main bankはそのまま。

制限: 既存名interpolationはpaired全体strictIDを保証しない。C2時点の名から遡って既知だったと書かない。

非公開原記録commit: `b51c737ba810fda5db1461b964ed979d46fd5a03`。公開URLを意味しない。

<a id="f042"></a>
## F042 — CONFIRMED_FROM_CODE

実行前lockはfresh20M、one replicate、B/C共有initial seed17689761006246261369、stream15984386699233955817、各1529updates/50,004,416predictionsを固定。

制限: B/Cを独立2seedsと数えない。実行bindingをpreflightの不足値に対する事前明文化として保存。

非公開原記録commit: `f9072c3010e6e65d8c8d7104f20c4b4b57689300`。公開URLを意味しない。

<a id="f043"></a>
## F043 — CONFIRMED_FROM_RAW

INTERFACE_ONLYは1/1024 exact、44/1024 canonical、strict pairs0/512。RULE_POSITIVEは36/1024 exact、1018/1024 canonical、strict0/512。POSITIVE_NOT_ESTABLISHED。

制限: world-disjoint独立生成評価。canonical formatと内容正答は別。

非公開原記録commit: `0ae379c8d0feda4d72092ed8a2f3a5ffb5961c40`。公開URLを意味しない。

<a id="f044"></a>
## F044 — CONFIRMED_FROM_RAW

sealed512blocks: ZERO mean .006013171/pairs1、INTERFACE_ONLY mean −.007735578/pairs18、RULE_POSITIVE mean .240901128/pairs34。positive mean/gainだけではreadout PASSしない。

制限: 同一実験の既存sealed出力を読むだけ。新たな照会・基準調整なし。

非公開原記録commit: `0ae379c8d0feda4d72092ed8a2f3a5ffb5961c40`。公開URLを意味しない。

<a id="f045"></a>
## F045 — CONFIRMED_FROM_MANIFEST

BはFORMAT124/128、SELECTION8/128、REP124/128。Cは0/128、4/128、1/128。両arm INTERFACE_CONFOUNDED、negativeはINCONCLUSIVE。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `0ae379c8d0feda4d72092ed8a2f3a5ffb5961c40`。公開URLを意味しない。

<a id="f046"></a>
## F046 — CONFIRMED_FROM_MANIFEST

positive failure stopでDEPENDENCY_BROKEN/M1/追加seed/optional direct-interface trainingはNOT_RUN。合計100,008,832predictions。

制限: 未実行negativeの低signalやspecificityを捏造しない。

非公開原記録commit: `0ae379c8d0feda4d72092ed8a2f3a5ffb5961c40`。公開URLを意味しない。

<a id="f047"></a>
## F047 — CONFIRMED_FROM_MANIFEST

全teacher対応・offset/mask監査でanswer content4,756,841 loss targetsを確認。ゼロ教師信号、全面mask、wrong oracle、normalizationだけの説明は支持されなかった。

制限: 全てのsoftware defect不存在の証明でも十分な学習の証明でもない。

非公開原記録commit: `16c995c1b039bf245b85c7454649f772cc16e357`。公開URLを意味しない。

<a id="f048"></a>
## F048 — CONFIRMED_FROM_MANIFEST

原C3はanswer-position loss、fit generation、intermediate competenceを保存していなかった。訓練未収束/汎化/難度を一意に分離できない。

制限: 今回missing valuesを推測・forwardで補わない。scorer不感性やM3不可能性を結論しない。

非公開原記録commit: `16c995c1b039bf245b85c7454649f772cc16e357`。公開URLを意味しない。

<a id="f050"></a>
## F050 — CONFIRMED_FROM_MANIFEST

限定M3はa*x0+b=r、|a|2–9、nonzero|b|1–9、x−9..9、canonical/add+mul/AST depth2。one20M/one seed/one run、Stage B独立90% sides/80%pairs各conflictを事前lock。

制限: 逆問題construct保持する限定条件。元Mainの全sampling lawと同じではない。

非公開原記録commit: `da40ec5d6c3f5505ff5746079650323c321052e3`。公開URLを意味しない。

<a id="f051"></a>
## F051 — CONFIRMED_FROM_MANIFEST

model7214329170824346757、stream13286570067985344592、data7062218186872731203。fit1024/dev256/heldout512/paired512 worldsを隔離。最大1529updates/50,004,416pred、30min。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `da40ec5d6c3f5505ff5746079650323c321052e3`。公開URLを意味しない。

<a id="f052"></a>
## F052 — CONFIRMED_FROM_RAW

限定M3 fit exact0,465,511,512,511 /512、dev0,21,27,33,34 /256 at updates0,382,764,1146,1529。

制限: 一時点のfit512/512をterminal heldout competenceに読み替えない。

非公開原記録commit: `da3fcf0a79ce4552a8770ec3dd59ba74d36432de`。公開URLを意味しない。

<a id="f053"></a>
## F053 — CONFIRMED_FROM_RAW

final world-disjoint heldout38/512 exact/rational、499/512 canonical、strict0/256。全newline終了、13malformedはincorrect。

制限: 同じteacher grammar/限定support。規則獲得positive未成立、単純暗記だけが原因とは確定しない。

非公開原記録commit: `da3fcf0a79ce4552a8770ec3dd59ba74d36432de`。公開URLを意味しない。

<a id="f054"></a>
## F054 — CONFIRMED_FROM_MANIFEST

heldout conflict5strataは全てstrict pairs0。last-number25/350、antitone24/256、monotone14/256、positive-sign17/298、recent-copy17/182 side correct。

制限: strataは重複。Nを足して独立sample数にしない。

非公開原記録commit: `da3fcf0a79ce4552a8770ec3dd59ba74d36432de`。公開URLを意味しない。

<a id="f055"></a>
## F055 — CONFIRMED_FROM_MANIFEST

限定M3 answer content4,447,685 targets、last100 answer loss .019708。fit高正答でもheldout未成立。Stage C/pairedbaseline/controlsはNOT_RUN。

制限: heldout0/256は独立生成の両側正答でありpaired scorer結果ではない。

非公開原記録commit: `da3fcf0a79ce4552a8770ec3dd59ba74d36432de`。公開URLを意味しない。

<a id="f056"></a>
## F056 — CONFIRMED_FROM_MANIFEST

限定M3 host GPU-phase wall317.525771sとCUDA-event sum319.013465sを保存。異なるclockで約0.47%差、GPU-active時間とは断定しない。

制限: この数値差を都合よく一方へ統一しない。

非公開原記録commit: `da3fcf0a79ce4552a8770ec3dd59ba74d36432de`。公開URLを意味しない。

<a id="f057"></a>
## F057 — CONFIRMED_FROM_MANIFEST

独立known-positive/readout constructを十分確立できず、OBS0で記述的・探索的比較発達観察へ移行。元研究記録と失敗を保存。

制限: 元から記述研究だったとは書かない。科学的Primary0は能力不存在の判定ではない。

非公開原記録commit: `1925d251fbc749a46300a68faaf44e6373b53836`。公開URLを意味しない。

<a id="f058"></a>
## F058 — CONFIRMED_FROM_MANIFEST

OBS1は5conditions×3sizes/r0の15本、25checkpoint/9Full/Fastなしを具体化。20M/MIX先行とseed/cadence/budgetは当時提案だった。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `710bdd372cc7dfc95ed0addc30b9cf3364b3998f`。公開URLを意味しない。

<a id="f059"></a>
## F059 — CONFIRMED_FROM_MANIFEST

研究者がsmall-first理由で20M/MIX→10M/MIX/r0へ変更。科学的成績による選別でなく、新decision overlayで履歴を保持。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `7ee3e0315b57f18b0f39bdb37bc077aafa90f2df`。公開URLを意味しない。

<a id="f064"></a>
## F064 — CONFIRMED_FROM_MANIFEST

研究者正式承認後428faacのannotated Main Observation freeze。測定仕様固定であり科学的妥当性承認ではない。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `1760d2481c9f09f55d2a99dc7280821a6b3a1c92`。公開URLを意味しない。

<a id="f065"></a>
## F065 — CONFIRMED_FROM_MANIFEST

15本/r0 study design承認、実行許可は初回10M/MIXだけ。init8164703693637831597、stream17323835196105447590、各domain16seq/updateで25%predictions。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `1760d2481c9f09f55d2a99dc7280821a6b3a1c92`。公開URLを意味しない。

<a id="f066"></a>
## F066 — REPORTED_ONLY

初回起動で2件のpre-initialization排他衝突。空run leafとreceipt overwriteを扱う同値性checked shim後に実行。model update/eval前の失敗として記録。

制限: 第2件はevent hook前の停止で独立HARDSTOP event2件とは書かない。H1 call-path/archiveを根拠に証拠水準を保持。

非公開原記録commit: `1760d2481c9f09f55d2a99dc7280821a6b3a1c92`。公開URLを意味しない。

<a id="f067"></a>
## F067 — CONFIRMED_FROM_MANIFEST

fresh10M/MIX/r0は61156updates/2,000,045,824pred、4domain各500,011,456、25checkpoints/9Fullを完了。

制限: OBS5独立verifierの歴史的receiptを継承。H2はcheckpointを開かず全batch再照合もしない。

非公開原記録commit: `1760d2481c9f09f55d2a99dc7280821a6b3a1c92`。公開URLを意味しない。

<a id="f069"></a>
## F069 — CONFIRMED_FROM_MANIFEST

planned-vs-consumed全61156batch一致の監査によりOBS4 overlap projection適用。target body1944/world7507/diagnostic body192 member matches、source-ID/qualified-ID0。

制限: zero overlapではない。member数であり独立block数ではない。prefix/completion一致0と問題本文一致は別。

非公開原記録commit: `1760d2481c9f09f55d2a99dc7280821a6b3a1c92`。公開URLを意味しない。

<a id="f070"></a>
## F070 — CONFIRMED_FROM_MANIFEST

runtime stage12720.111799525s、launch-to-exit12817.047526295s、9Full合計868.9244039230016s、checkpoint4,225,593,932bytes、run5.2GiB。

制限: snapshot/clockを区別。GPU-active未計測。continuous physical500GB reservation保証とruntime free-floor監視は同一ではない。

非公開原記録commit: `1760d2481c9f09f55d2a99dc7280821a6b3a1c92`。公開URLを意味しない。

<a id="f068"></a>
## F068 — CONFIRMED_FROM_RAW

保存lossはupdate1=9.035449028015137、final1.5014363527297974。25probe/9×36cellとstrata/controls/diagnosticsをH1がrawから再集計した。

制限: H2はhash照合済みH1全表と対応するraw subsetを照合。loss/NLL/accuracy/marginは互換の能力尺度ではない。

非公開原記録commit: `e058413e125bdf770c5a75c8c5e6f64638e409dc`。公開URLを意味しない。

<a id="f071"></a>
## F071 — CONFIRMED_FROM_MANIFEST

H1が全324cell-time/648length/45control/27diag、61156lossの保存証拠を独立再集計。7新softwaretests、過去1842full regressionは再実行せず継承。

制限: H2はH1 receiptとSHAを検証するが、H1の全raw readbackを今回再実行したとは言わない。

非公開原記録commit: `e058413e125bdf770c5a75c8c5e6f64638e409dc`。公開URLを意味しない。

<a id="f072"></a>
## F072 — CONFIRMED_FROM_MANIFEST

完了1/15、pending14はNOT_STARTED/REQUIRES_NEW_EXPLICIT_INSTRUCTION。design承認とexecution許可を分離。Pure4条件全2B streamは未準備。

制限: 当該原本の範囲。software verificationは能力測定の妥当性を承認しない。

非公開原記録commit: `e058413e125bdf770c5a75c8c5e6f64638e409dc`。公開URLを意味しない。

<a id="f073"></a>
## F073 — CONFIRMED_FROM_MANIFEST

全36 DESCRIPTIVE_ONLY/Primary0、calibrationとMain Observation exposureはnonzero、Long-Horizon pilot capabilityと旧Discovery/Confirmation0。H1/H2新規scientific exposure0。

制限: global trained exposure0と言わない。1seedから一般化/因果/能力不存在を結論しない。

非公開原記録commit: `e058413e125bdf770c5a75c8c5e6f64638e409dc`。公開URLを意味しない。

<a id="f074"></a>
## F074 — UNVERIFIED

内部表現のmechanistic association/causal interventionの科学的結果は未確立。元の能力形成研究問いを達成済みとして扱えない。

制限: 未測定/未承認であり負の因果実験結果ではない。

非公開原記録commit: `e058413e125bdf770c5a75c8c5e6f64638e409dc`。公開URLを意味しない。
