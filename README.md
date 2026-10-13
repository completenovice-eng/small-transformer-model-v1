# Model v1 — OBS-5中間技術報告

**PUBLIC_OBS5_INTERIM_REPORT／記述的・探索的研究の中間報告**

ChatGPT-Sol-6.1を利用しています。
公開repository：[small-transformer-model-v1](https://github.com/completenovice-eng/small-transformer-model-v1)。

当初は学習経験Xから、直接解答を教えていない能力Yの形成を問う研究だった。
評価のconstruct validityとpositive calibrationを十分確立できず、記述的観察へ変更した。
OBS-5時点で、15 trajectories中10M/MIX/r0の **1/15** だけが完了している。残14本の比較結果はない。
全36cellsは **DESCRIPTIVE_ONLY**、科学的Primary承認0、positive calibration未成立、scorer感度未確定。
TRAIN/Core Evalには内容重複がある。loss/margin上昇を能力発現、低値を能力不存在とは解釈しない。

## 読む順序

1. [技術報告](report/technical_report.md)
2. [研究史・方法論](evidence/methods_and_history.md) / [14negative records](evidence/negative_results.md)
3. [P01–P31 claim audit](report/claim_audit.md) / [元証拠の説明](evidence/source_notes.md)
4. [図表再生成](report/figures_and_reproduction.md)
5. [ファイルとSHA](evidence/export_manifest.json)
6. [ライセンス](LICENSE.md) / [ファイル別適用範囲](licensing/SCOPE.json) / [著者・AI支援](AUTHORS.md)


```sh
python -m pip install -r requirements.txt
python scripts/reproduce_figures.py --output ../reproduced-figures
python scripts/audit_public_export.py --root .
```

研究コード全体・weights/checkpoints・training data・tokenizer・全TRAIN stream・raw responses・private recovery/ledgerは含めない。


## ライセンスと科学的制約

独自報告・図表・集計等は、研究者保有の権利の範囲でCC BY 4.0。独自公開スクリプト2本はMIT。
第三者の原作品・software・data・fontには自動適用しない。
公開は測定器の科学的妥当性や能力形成の承認ではない。限定M3のknown/heldout差、Stage C未実行、未解明の失敗原因を保持する。
7技術図は、元の値と科学的制約を保った表示派生物。全36区分の結果を保持する。
このGitHub公開は、残14本の実行やnote投稿を開始する操作ではない。
