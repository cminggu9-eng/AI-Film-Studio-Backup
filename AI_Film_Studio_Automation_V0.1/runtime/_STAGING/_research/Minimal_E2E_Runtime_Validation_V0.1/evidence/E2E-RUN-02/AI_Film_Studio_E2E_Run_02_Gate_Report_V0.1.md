# AI Film Studio｜E2E Run 02 Gate Report V0.1

| Gate | Result | Attributable evidence |
| --- | --- | --- |
| Rerun 02 preflight | PASS | `preflight.json`: PERSIST 8/8, SW-INT 15/15, STRICT 15/15, TOKEN 10/10, Probe03 recorded replay 5/5, provider-free startup PASS, canonical hashes 7/7 unchanged. |
| Showrunner raw-response / usage persistence | PASS | `artifacts/showrunner_provider_response.json`, `artifacts/showrunner_invocation.json`, `artifacts/showrunner_persistence_verification.json`. |
| Showrunner exact E2E transport schema | FAIL | `artifacts/showrunner_validation_error.json`: raw object omitted required top-level `scene_packages` (must be the exact string `ABSENT` for this role). |
| Scene Writer strict tool parse and schema gate | NOT REACHED | Safe stop occurred before Scene Writer invocation. |
| Scene Writer hydrate, structural, state-token, semantic safeguard gates | NOT REACHED | No accepted Scene Writer package exists. |
| Downstream eligibility | BLOCKED | The Showrunner output was not accepted; the required upstream transport gate failed. |

No transport repair, semantic repair, role retry, or fallback was performed.
