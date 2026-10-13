# 外部資産・帰属

TinyStoriesはRonen Eldan/Yuanzhi Liの研究・datasetを出典とする。原文、tokenizer、weightsは含まれない。
[固定dataset card](https://huggingface.co/datasets/roneneldan/TinyStories/blob/f54c09fd23315a6f9c86f9dc80f725de7d8f9c64/README.md)にCDLA-Sharing-1.0宣言がある。
[CDLA原文](https://cdla.dev/sharing-1-0/)のData/Enhanced Data/Results区分と再配布条件は対象別reviewが必要で、license所在確認は包括承認ではない。
PlotにはMatplotlib/NumPyと固定dependenciesを使用。softwareやfontの実体をvendorしていない。
Matplotlibのlicense/font notices、NumPy、Python、SentencePiece、PyTorchの原本URLは[参照資料](../references/external_sources.json)へ記録した。
Software利用、生成図、元data、weightsは別の権利である。論文図/本文の転載はしない。
AIは設計/実装/文書支援に関わり研究者が最終判断したが、review全文・担当別貢献の完全な原本は未確認。
著者はcompletenovice-eng。AIレビューを人間のpeer reviewとは呼ばない。第三者の権利は[適用表](SCOPE.json)の独自license対象外。

DejaVu SansはSVG内でfont-familyを参照しPNGで描画する。fontファイルやglyph font packageは同梱しない。
標準license本文はSPDXのlicense-list-data収録版を無改変収録（MITの権利者欄のみ記入）。
外部license本文を本研究のCC BY/MITで再許諾しない。各標準本文の条件と[出典](../references/license_sources.json)を参照。

日本語派生図はNoto Sans CJK JPで描画。font本体を同梱せず、fontへ独自CC BY/MITを適用しない。
[公式SIL OFL1.1](https://github.com/notofonts/noto-cjk/blob/main/Sans/LICENSE)とreceiptのsource SHAを記録した。
