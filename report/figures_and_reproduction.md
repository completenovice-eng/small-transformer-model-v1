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
