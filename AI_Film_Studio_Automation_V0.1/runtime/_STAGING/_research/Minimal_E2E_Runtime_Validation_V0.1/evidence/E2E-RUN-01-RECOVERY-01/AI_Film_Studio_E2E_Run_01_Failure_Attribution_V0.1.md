# AI Film Studio E2E Run 01 Failure Attribution V0.1

| Failure | Owner | Layer | Evidence | Blocking | Recommended repair scope |
| --- | --- | --- | --- | --- | --- |
| Initial technical post-response persistence/role-contract failure | Integration Harness | RUNTIME / HARNESS FAILURE | `../E2E-RUN-01/Initial_Attempt_Provider_Accounting_Correction_V0.1.md` | Yes; recovery consumed | Preserve parsed Provider response and usage before local validation; this was repaired only to enable the one authorized recovery. |
| `REQUIRED_STATE_MISMATCH` (`SOAKED-UNIFORM`) | Scene Writer output, caught by Integration Semantic Safeguard | SEMANTIC SAFEGUARD FAILURE | `semantic_safeguard.json`; `artifacts/scene_writer_output.json` | Yes | Define/enforce an exact machine enum for `clothing_visual_state` separately from Chinese display prose, and add a real-response contract test. |
| Missing six required scene headings | Scene Writer output | ROLE SEMANTIC FAILURE | `artifacts/scene_writer_output.json`; `acceptance_test_report.json` | Yes for 18/18 PASS | Bind the six headings as validated structured deliverable fields or test them before downstream handoff. |

No repair was executed for either semantic finding. No downstream role was asked to compensate for them.
