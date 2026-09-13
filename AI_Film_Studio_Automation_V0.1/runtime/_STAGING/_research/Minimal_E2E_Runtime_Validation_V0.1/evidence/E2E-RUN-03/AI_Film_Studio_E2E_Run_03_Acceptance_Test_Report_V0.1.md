# AI Film Studio｜E2E Run 03 Acceptance Test Report V0.1

The complete acceptance aggregator was not reached because Director was rejected by its local contract. This closure records every E2E-INT item only from persisted evidence; accepted partial-chain results are not treated as a seven-role pass.

| ID | Result | Attributable evidence |
| --- | --- | --- |
| E2E-INT-01 | PASS | `preflight.json`; frozen fixture ID is `E2E-FIX-01`. |
| E2E-INT-02 | PASS | Accepted `artifacts/showrunner_output.json` contains the required Canon Locks package. |
| E2E-INT-03 | PASS | `semantic_safeguard.json`: `integration_decision` is `PASS`. |
| E2E-INT-04 | PASS | Accepted Scene Writer output contains three packages and all six structural deliverable fields per scene. |
| E2E-INT-05 | FAIL | Director raw response was rejected because its heading tokens did not exactly match the required role contract. |
| E2E-INT-06 | NOT REACHED | Character & Acting was not invoked after Director failure. |
| E2E-INT-07 | NOT REACHED | Art Director was not invoked after Director failure. |
| E2E-INT-08 | PASS | `state_ledger.json` is append-only with exactly three accepted Scene Writer entries. |
| E2E-INT-09 | PASS | Ledger preserves A-17, scene-one `soaked_uniform`, and final `change_from_soaked_uniform`. |
| E2E-INT-10 | PASS | Ledger contains `REVEALED_WITH_EVENT` evidence. |
| E2E-INT-11 | NOT REACHED | Character & Acting and Art Director outputs do not exist. |
| E2E-INT-12 | PASS | Accepted Showrunner and Scene Writer Envelopes preserve canonical mode/state/flags/handoffs exactly; post-stop provider-free verification passed. |
| E2E-INT-13 | NOT REACHED | Shared QA was not invoked. |
| E2E-INT-14 | PASS | Role inputs use `output_language: zh-CN`. |
| E2E-INT-15 | PASS | `semantic_safeguard.json`: `legacy_verifier_role` is `SUPPLEMENTAL_SIGNAL_ONLY`. |
| E2E-INT-16 | PASS | `semantic_safeguard.json`: `creative_output_rewrite` is `PROHIBITED`. |
| E2E-INT-17 | PASS | `preflight.json` exists and passed before executor construction. |
| E2E-INT-18 | FAIL | `provider_manifest.json` records 3 calls and only 2 accepted role outputs, not the required seven. |

**Closure:** 12 PASS / 2 FAIL / 4 NOT REACHED. The mandatory 18/18 PASS threshold was not met.
