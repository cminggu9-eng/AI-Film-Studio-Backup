---
type: output-language-contract-test-report
status: passed
classification: NON-NETWORK CONTRACT TEST
---

# Scene Writer Output Language Contract Test Report V0.1

| Test | Result | Evidence |
|---|---|---|
| OL-SW-01 | PASS | explicit `zh-CN` reaches Runtime and validates Chinese creative/control text |
| OL-SW-02 | PASS | explicit `en-US` reaches Runtime and validates English creative/control text |
| OL-SW-03 | PASS | canonical `SCENE_CREATED` and `PRODUCTION_REVIEW_REQUIRED` remain exact English; translated state is rejected |
| OL-SW-04 | PASS | missing `output_language` deterministically inherits explicit `assignment_language` |
| OL-SW-05 | PASS | no explicit language metadata returns `OUTPUT_LANGUAGE_UNRESOLVED` |
| OL-SW-06 | PASS | invalid language value is rejected |
| OL-SW-07 | PASS | English creative/control output fails an explicit `zh-CN` contract |
| OL-SW-08 | PASS | canonical Skill hash/body remain language-agnostic; no Chinese hardcode |

`OL-SW-01–08 = 8 / 8 PASS`.

Regression retained: Scene Writer Runtime `30 / 30 PASS`; Executor Binding `10 / 10 PASS`; Synthetic E2E `PASS`. No provider call occurred in any of these tests.
