# AI Film Studio｜E2E Run 03 Gate Report V0.1

| Gate | Result | Attributable evidence |
| --- | --- | --- |
| Rerun 03 preflight | PASS | `preflight.json`: PERSIST 8/8, SW-INT 15/15, STRICT 15/15, TOKEN 10/10, Probe03 recorded replay 5/5, SHOWRUNNER-OWN 10/10, provider-free startup PASS, hashes 7/7 unchanged. |
| Showrunner persistence and role-owned payload | PASS | Raw response, usage, and output persisted in `artifacts/showrunner_*`; Repair 04 inserted only integration-owned `scene_packages: "ABSENT"`. |
| Showrunner full transport and handoff Envelope | PASS | `artifacts/showrunner_output.json` and `envelopes/01_showrunner_to_scene_writer.json`. |
| Scene Writer strict function / schema / hydration | PASS | `artifacts/scene_writer_provider_response.json` records forced `submit_scene_writer_package`, Beta strict transport, exact function parse and schema validation. |
| Scene Writer structural, state, and Semantic Safeguard gates | PASS | `artifacts/scene_writer_output.json`, `state_ledger.json`, and `semantic_safeguard.json` (`integration_decision: PASS`). |
| Director raw persistence / truncation | PASS | `artifacts/director_provider_response.json`, invocation metadata, and `director_truncation_detection.json` (`NOT_TRUNCATED`). |
| Director local role contract | FAIL | `artifacts/director_validation_error.json`: required exact heading was missing. Raw content uses uppercase/spaced variants such as `DIRECTORIAL INTENT` and `STAGING / BLOCKING`, not the required exact labels. |
| Downstream eligibility after Director | BLOCKED | Character & Acting, Art Director, Continuity, and Shared QA were not invoked. |

No retry, fallback, semantic repair, or provider switching was performed.
