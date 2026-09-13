# AI Film Studio｜E2E Run 02 Acceptance Test Report V0.1

The E2E acceptance phase cannot run on a rejected upstream role package. Results below preserve the required three-valued status without treating unaccepted raw content as an accepted role output.

| ID | Result | Attributable evidence |
| --- | --- | --- |
| E2E-INT-01 | PASS | `preflight.json`; frozen fixture ID is `E2E-FIX-01`. |
| E2E-INT-02 | NOT REACHED | Showrunner raw output was not accepted by the exact transport schema. |
| E2E-INT-03 | NOT REACHED | No accepted Scene Writer package reached the Semantic Safeguard. |
| E2E-INT-04 | NOT REACHED | No Scene Writer scenes were invoked or accepted. |
| E2E-INT-05 | NOT REACHED | Director was not invoked. |
| E2E-INT-06 | NOT REACHED | Character & Acting was not invoked. |
| E2E-INT-07 | NOT REACHED | Art Director was not invoked. |
| E2E-INT-08 | NOT REACHED | No accepted Scene Writer transition entered the run-local ledger. |
| E2E-INT-09 | NOT REACHED | No accepted Scene Writer state evidence exists. |
| E2E-INT-10 | NOT REACHED | No accepted Scene Writer knowledge-timing evidence exists. |
| E2E-INT-11 | NOT REACHED | Character & Acting and Art Director were not invoked. |
| E2E-INT-12 | NOT REACHED | No accepted role envelopes were created for token-preservation comparison. |
| E2E-INT-13 | NOT REACHED | Shared QA was not invoked. |
| E2E-INT-14 | PASS | `artifacts/showrunner_input.json`; assignment execution constraint is `output_language: zh-CN`. |
| E2E-INT-15 | NOT REACHED | No Scene Writer Semantic Safeguard result exists. |
| E2E-INT-16 | NOT REACHED | No Scene Writer Semantic Safeguard result exists. |
| E2E-INT-17 | PASS | `preflight.json` exists and passed before executor construction. |
| E2E-INT-18 | FAIL | `provider_manifest.json` records 1/7 role output; complete role-output set is absent due attributable safe stop. |

**Closure:** 3 PASS / 1 FAIL / 14 NOT REACHED. The required 18/18 PASS condition was not met.
