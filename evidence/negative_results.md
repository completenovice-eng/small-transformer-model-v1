# Negative resultsと未解決事項（公開用要約）

14件を保持。原因未同定を未同定のまま記録する。以下は非公開監査原本に基づく要約で、raw evidenceそのものではない。

## N01 — CONSTRUCT_FAILURE

- 目的: native primary測定
- 事前基準/契約: native problemから一方をunique goldとできること
- 結果: 0/36 primary native
- 確認範囲: oracle completionなし/両continuationが妥当問題
- audit範囲で支持されなかった説明: native問題継続がそのまま解答能力を測るという設計
- 排除できない説明: latent能力の不存在
- 後続判断: eval-only adapterを別constructとして設計
- 参照fact IDs: F021, F022

## N02 — MEASUREMENT_CONFOUND

- 目的: domain-neutral labels
- 事前基準/契約: positive TRAIN exposure/valid token contract
- 結果: 共通positive IDはEOSのみ
- 確認範囲: saved4domain bankにsafe pair未実証
- audit範囲で支持されなかった説明: 0/1が見た目で公平という仮定
- 排除できない説明: 別seedのrare exposure/answer representation transfer
- 後続判断: arbitrary labelsをprimary救済として廃止
- 参照fact IDs: F023, F024

## N03 — MEASUREMENT_CONFOUND

- 目的: item randomization inference
- 事前基準/契約: joint sign-exchangeability
- 結果: 0/36 proven
- 確認範囲: 依存paired生成の交換可能性未証明
- audit範囲で支持されなかった説明: unconditional simple sign-flipの承認
- 排除できない説明: validな別nullが構築可能か
- 後続判断: deterministic measurementとseed inferenceを分離
- 参照fact IDs: F025, F026

## N04 — MEASUREMENT_CONFOUND

- 目的: paired scorerで候補弁別
- 事前基準/契約: token boundary/prefix valid
- 結果: 211/27754 nested blocks removed
- 確認範囲: 15cells affected; final27543
- audit範囲で支持されなかった説明: string-only auditで十分という扱い
- 排除できない説明: 残るlength/context prior
- 後続判断: whole-block deterministic除外、原本保存
- 参照fact IDs: F029, F030

## N05 — MEASUREMENT_CONFOUND

- 目的: rule-readout解釈
- 事前基準/契約: shortcut/control独立性
- 結果: 13319 unequal、literal lookup各256/256
- 確認範囲: 高heuristic成績/controlsがruleを保証しない
- audit範囲で支持されなかった説明: staticPASS=未知shortcut不存在
- 排除できない説明: trained model固有interaction
- 後続判断: 36cells descriptive維持
- 参照fact IDs: F031, F038, F039

## N06 — MEASUREMENT_CONFOUND

- 目的: M3 interpolation両側ID
- 事前基準/契約: TRAIN solution support両側
- 結果: 569/986 CF draw外
- 確認範囲: Main bankはpaired mixed support
- audit範囲で支持されなかった説明: 名前interpolationが両側IDを保証
- 排除できない説明: readout effectへのsupport差寄与
- 後続判断: 較正は別pool、原bankは改変しない
- 参照fact IDs: F049

## N07 — CALIBRATION_NOT_ESTABLISHED

- 目的: known-positiveでscorer感度確認
- 事前基準/契約: 独立competence≥90%とconflict基準/controls/response conjunction
- 結果: C36/1024、strict0/512、readout34/512
- 確認範囲: rational1018と内容36を分離、B/C同initialone replicate
- audit範囲で支持されなかった説明: mean margin上昇だけでpositive
- 排除できない説明: 課題難度/fit/汎化/optimization/interface
- 後続判断: positive-failure停止、D/M1/追加seeds未実行
- 参照fact IDs: F042, F043, F044, F045, F046

## N08 — UNRESOLVED_CAUSAL_EXPLANATION

- 目的: C3失敗原因切分
- 事前基準/契約: saved teacher/offset/stream/parser audit
- 結果: answer exposures4756841; answer loss/fit eval missing
- 確認範囲: target loss実在、canonical wrong982
- audit範囲で支持されなかった説明: 全面mask/無教師/normalizationだけ/truncationという観測説明
- 排除できない説明: fit未収束/汎化/難度/packing寄与の因果
- 後続判断: 限定positiveを新事前登録で一度だけ実験
- 参照fact IDs: F047, F048

## N09 — GENERALIZATION_NOT_ESTABLISHED

- 目的: 限定M3 known-positive
- 事前基準/契約: heldout exact≥90%、strict≥80% overall/各conflict、256blocks/64stratum
- 結果: fit511/512 vs heldout38/512、strict0/256
- 確認範囲: 同teacher grammar、world-disjoint、499canonical、newline終了
- audit範囲で支持されなかった説明: fit高正答だけでpositive/formatだけの失敗/打切りだけ
- 排除できない説明: 暗記/shortcut/coverage/optimizationの固有原因
- 後続判断: POSITIVE_NOT_ESTABLISHED; StageC NOT_RUN
- 参照fact IDs: F050, F051, F052, F053, F054, F055

## N10 — CALIBRATION_NOT_ESTABLISHED

- 目的: paired readout感度を確かめる
- 事前基準/契約: StageB positiveを先に成立
- 結果: StageC未実行
- 確認範囲: paired baseline/controls/marginsは測っていない
- audit範囲で支持されなかった説明: StageC未実行をscorer不感性の結果とする解釈
- 排除できない説明: 限定分布でpositive成立時scorerが反応するか
- 後続判断: 新scorer/追加training自動実行なし
- 参照fact IDs: F055

## N11 — SOFTWARE_OR_OPERATIONAL_FAILURE

- 目的: 2B pilotを安全延長
- 事前基準/契約: stream/recovery integrity
- 結果: D3-A技術中断、隔離復旧
- 確認範囲: 成功記録に加え中断記録を維持
- audit範囲で支持されなかった説明: 中断を能力陰性結果とする解釈
- 排除できない説明: 未保存詳細は当時原本の範囲
- 後続判断: D3-C技術closure参照
- 参照fact IDs: F015

## N12 — SOFTWARE_OR_OPERATIONAL_FAILURE

- 目的: Main stream/storage readiness
- 事前基準/契約: 100GB index枠/seed roundtrip/full audit
- 結果: OBS3 blocked→OBS4固定index/全量audit
- 確認範囲: 244GBを単純3分割できない
- audit範囲で支持されなかった説明: 3size共有だけで81GBになるという案
- 排除できない説明: 未準備PUREの実容量
- 後続判断: TRAIN law変えずindex実装改善
- 参照fact IDs: F060, F061, F062, F063

## N13 — SOFTWARE_OR_OPERATIONAL_FAILURE

- 目的: 初回Main起動
- 事前基準/契約: exclusive artifact publication
- 結果: pre-init2衝突→同値性確認shim→完走
- 確認範囲: 失敗記録保持、update/eval前
- audit範囲で支持されなかった説明: 成功runのscientific retry/条件選別という扱い
- 排除できない説明: 第2event独立記録不足
- 後続判断: 元freeze/seed/streamのまま運用修正履歴保持
- 参照fact IDs: F066, F067

## N14 — RESEARCH_GOAL_NOT_ACHIEVED

- 目的: 能力形成・内部機構を比較説明
- 事前基準/契約: valid constructs/known-positive/replication/機構因果別証拠
- 結果: Primary0、positive未成立、観察1/15
- 確認範囲: 技術再現性と記述測定は得た
- audit範囲で支持されなかった説明: 当初から記述目的だった/研究完了という説明
- 排除できない説明: 元能力問い/他14条件/機構/一般化
- 後続判断: OBS scopeへ明示移行、残14は別実行許可
- 参照fact IDs: F057, F072, F073, F074
