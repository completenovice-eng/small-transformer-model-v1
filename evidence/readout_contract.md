# 固定paired readoutの公開用説明

同じA/BについてP0でA=oracle、P1でB=oracle。

```text
d0 = logp(A|P0) - logp(B|P0)
d1 = logp(A|P1) - logp(B|P1)
m = (d0-d1)/2
PAIR_CORRECT = (d0>0 and d1<0)
```

Whole-string tokenizationでprefix境界を検証。continuation全tokenのsum-LL、causal position i-1、EOS非採点、length normalizationなし。
Side tie0.5、strict pair tie不正答。Mean marginと両側正答は別。chance25%/sign randomizationを無条件に置かない。
固定candidate priorは差し引けてもprompt-dependent biasは残る。全36cells DESCRIPTIVE_ONLY、Primary0。
公開CSVは保存集計であり、モデルforward/scorer実行/raw loglikelihoodの独立監査はこのsubsetではできない。
正本のruntime scorer/tokenizer/bankは非公開、ここは仕様の説明である。
