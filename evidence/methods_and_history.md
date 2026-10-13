# 研究史・方法論の公開用要約

当初は学習経験Xから直接解答を教えていない能力Yの形成時刻・規模/domain差・内部変化を問う研究だった。
データ生成/tokenizer/architecture/A2/R1/2B/stream/resumeの技術再現性を検証したが、能力測定の妥当性を確立したわけではない。
Native primary0/36、eval-only interface、label exposure、paired readout、211nested blocks除去を経て27,543blocks/36cellsを保持した。
Controlsのlookup限界、prompt-dependent shortcut、support差、TRAIN内容重複を認め、scientific Primary0とした。
Original C3はRULE_POSITIVE36/1024、限定M3はfit511/512に対しworld-disjoint heldout38/512、独立生成strict0/256。
Positive未成立で限定Stage Cは未実行。scorer感度不足を確定できず、原因も一意に説明できなかった。
OBS0で記述的・探索的比較発達観察へ変更し、元目的と失敗を保存した。旧5+5/4of5/T landmarksは自動適用していない。
OBS1の20M/MIX先行案は研究者のsmall-first判断で10M/MIXへ変更。全stream/index/ledger監査と固定長共有index化を経た。
OBS5で仕様を正式固定し初回のみ実行。2pre-init衝突の記録範囲を保持し10M/MIX/r0を完走。残14は未実行。
外部AI review原文、失敗因果、GPU-active timeは未確認/未測定。AI意見を査読/実験証拠に扱わない。

詳細な当時の判断は[claim説明](source_notes.md)と[14negative records](negative_results.md)に要約した。
原チャット、private RECOVERY、全Git履歴、raw evaluation/weightsは提供していない。
ここにある要約を第三者が原本まで独立検証できるとは主張しない。
