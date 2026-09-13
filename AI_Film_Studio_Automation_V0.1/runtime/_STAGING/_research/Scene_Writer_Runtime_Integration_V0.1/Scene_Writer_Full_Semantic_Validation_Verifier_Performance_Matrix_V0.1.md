# Scene Writer Full Semantic Validation Verifier Performance Matrix V0.1

The verifier was invoked only after Runtime accepted a generated deliverable. It did not produce a `FAIL` result in this pack.

| Fixture | Human fact / knowledge result | Verifier result | Classification |
|---|---|---|---|
| F01 | PASS | PASS | True Negative |
| F02 | PASS | PASS | True Negative |
| F03 | FAIL — unprovided shared prior-work assertion | PASS | **False Negative** |
| F04 | PASS | PASS | True Negative |
| F05 | PASS | PASS | True Negative |
| F07 | PASS | PASS | True Negative |
| F08 | PASS — explicit unknown and broad time preserved | PASS | True Negative |
| F09 | PASS — knowledge scope preserved; separate state-logic failure | PASS | True Negative |
| F10 | FAIL — invented administrative plan / timing / coverage condition | PASS | **False Negative** |
| F14 | FAIL — unsupported wet-ground-to-risk causal assertion | PASS | **False Negative** |
| F06, F11, F12, F13-A, F13-B | Not assessable: Runtime rejected output before verifier | Not run | Not assessable |

## Observed Performance

- Accepted deliverables reviewed for fact / knowledge integrity: `10`.
- Human integrity violations: `3`.
- Verifier positive findings: `0`.
- Observed true negatives: `7`; observed false negatives: `3`; observed false positives: `0`; observed true positives: `0`.
- Observed recall on human-detected integrity violations: `0 / 3 = 0%`.
- Precision is not estimable: the verifier emitted no positive finding in this pack.

This is a bounded empirical result, not a claim of global model performance. It is nevertheless blocking because the known micro-fact risk appeared in multiple real fixtures after the pre-validation verifier matrix had passed.
