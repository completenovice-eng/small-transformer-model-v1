# 図表と再現範囲

公開集計からの図表再生成A、元モデル訓練の再実行B、非公開raw evidenceへの独立検証Cを分離する。
このsubsetで確認したのはAのみ。B/Cの資産・権利・全環境は含まれない。
7図のSVG/PNGは公開表示用の派生版。内部管理用footerだけを変更し、グラフ本体のgeometry・text・値・尺度は保持した。全36cells/9点を保持し、候補長の不一致や小bank、overlap、未成立較正を隠さない。
各画像のSHA、方法、入力は[export manifest](../evidence/export_manifest.json)と[公開CSV](../data/cell_trajectories.csv)へ対応する。

## 再生成

公開rootで、必要なplot packagesを別環境へrequirements.txtどおり導入して実行する。

```sh
python scripts/reproduce_figures.py --output ../reproduced-figures
python scripts/audit_public_export.py --root .
```

Scriptは公開CSVだけを読み、private repository/data/tokenizer/weightsを必要としない。training/model/forwardはない。
Matplotlib3.10.7/NumPy2.2.6および固定plot dependenciesと同一描画環境では14画像SHAを照合する。
異環境のpixel/byte同一性は未保証。数値と描画fingerprintを分けて扱う。
Figure3は24固定区間mean/endpoint、4は25保存probe、5は36x9mean margin、6はstrict選択/lookup/nuisance、7は限定M3。
Figure1/2は研究史と15本design/1本実施の図。時系列線は補助で連続観測ではなく、heatmap列も等時間幅ではない。
Raw source/source_key列やraw responsesは含めず、元CSVの数値文字列は変更していない。
Stage Cは未実行。限定M3の0/256は独立生成pairでありpaired scorerではない。


## note向け日本語表示版

[研究経緯](../figures/note/note_fig01_history_ja.png)、[限定M3](../figures/note/note_fig02_limited_m3_ja.png)、
[10Mの学習loss](../figures/note/note_fig03_training_loss_ja.png)を別の表示用派生物として用意した。
番号1〜3はnote本文の順序で、技術報告のFigure1/7/3に対応する。原図の置換や新しい科学的測定ではない。
日本語の大きい文字と縦配置を使い、較正の全保存時点・lossの全24区間を保持する。
Figure5/6は引き続き全36区分・9時点を掲載する。note記事側で縦長図を省いても、本subsetから行を落とさない。

日本語再生成には、公式Noto Sans CJK JPの指定SHAのfontを別途用意する。font本体は配布しない。
取得元・SHA・SIL OFL1.1原文参照は[display receipt](../evidence/display_receipt.json)。
同じplot環境で次を実行する（fontを指定位置へ用意した場合）。

```sh
python scripts/build_display_figures.py --data data --font ../fonts/NotoSansCJKjp-Regular.otf --output ../note-reproduced
```

360px表示相当で最小文字約16pxを確保し、local縮小previewを確認した。note実画面の圧縮・端末表示は未確認。
原図はprivate原本で保存し、公開版画像SHAと原図SHAを[export manifest](../evidence/export_manifest.json)で区別する。
