---
type: assignment-fact-knowledge-lock-test-report
status: test-pass-semantic-smoke-failure
classification: NON-NETWORK CONTRACT TEST
---

# Scene Writer Assignment Fact & Character Knowledge Lock Test Report V0.1

| Test | Result | Evidence |
|---|---|---|
| FK-SW-01 | PASS | explicit unknown reason category is rejected |
| FK-SW-02 | PASS | unprovided character knowledge source is rejected |
| FK-SW-03 | PASS | broad `今晚` cannot become Chinese `十二点前` deadline |
| FK-SW-04 | PASS | unsupported capability ranking is rejected for tested wording |
| FK-SW-05 | PASS | unprovided relationship history is rejected |
| FK-SW-06 | PASS | neutral immediate physical action remains lawful |
| FK-SW-07 | PASS | request / conditional negotiation remains lawful dialogue construction |
| FK-SW-08 | PASS | an explicit uncertainty remains uncertainty |
| FK-SW-09 | PASS | world fact is not upgraded into character knowledge |
| FK-SW-10 | PASS | complete Assignment remains executable; no Context Hunger |

`FK-SW-01–10 = 10 / 10 PASS`.

Regression retained: Runtime `30 / 30 PASS`; Executor Binding `10 / 10 PASS`; Output Language `8 / 8 PASS`; Synthetic E2E `PASS`.

## Test adequacy limitation

The real Smoke found a capability-ranking paraphrase not covered by the initial FK-SW-04 lexical case: `最熟悉整体内容的人之一`. Test pass is therefore not treated as semantic proof. No automatic broadening, rerun, or repair was performed after this discovery.
