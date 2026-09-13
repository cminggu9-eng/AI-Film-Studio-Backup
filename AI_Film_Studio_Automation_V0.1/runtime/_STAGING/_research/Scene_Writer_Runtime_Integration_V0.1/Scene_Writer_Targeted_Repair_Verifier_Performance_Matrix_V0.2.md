# Scene Writer Verifier Performance Matrix V0.2

| Evidence cohort | TP | TN | FP | FN | Transport invalid | Interpretation |
|---|---:|---:|---:|---:|---:|---|
| Full Semantic Validation V0.1 accepted outputs | 0 | 7 | 0 | 3 | 0 | Baseline observed recall 0% for three human fact failures. |
| Targeted Repair attempt 1/2 clean replay | — | 8 | 0 | — | 0 | Four clean outputs per attempt remained PASS. |
| Targeted Repair F03 replay before exhaustive coverage | 0 | — | — | 3 observed F03 passes | 0 | Unsupported prior-work claim was repeatedly missed. |
| Final exhaustive-candidate attempt | — | — | — | — | 2 | F03 and first clean replay failed with non-JSON provider response. |

No aggregate precision/recall metric is claimed from these small, interrupted cohorts. The V0.2 conclusion is `NOT A SUFFICIENT SEMANTIC GATE`.
