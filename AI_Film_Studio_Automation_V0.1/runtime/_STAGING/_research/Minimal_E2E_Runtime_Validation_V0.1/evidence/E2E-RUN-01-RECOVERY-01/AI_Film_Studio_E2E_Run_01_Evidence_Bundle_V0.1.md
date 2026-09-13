# AI Film Studio E2E Run 01 Evidence Bundle V0.1

| Index | Artifact | Status / path |
| --- | --- | --- |
| 00 | Preflight | `preflight.json` — PASS: State 12/12, Semantic 12/12, Provider-free startup, import counters 0, seven canonical hashes unchanged. |
| 01 | Showrunner artifact | `artifacts/showrunner_input.json`; `artifacts/showrunner_output.json` — executed. |
| 02 | Scene Writer artifact | `artifacts/scene_writer_input.json`; `artifacts/scene_writer_output.json` — executed then BLOCKED by safeguard. |
| 03 | Semantic Safeguard result | `semantic_safeguard.json`; `AI_Film_Studio_E2E_Run_01_Semantic_Safeguard_Report_V0.1.md` — BLOCK. |
| 04 | Direction artifact | `artifacts/director_not_reached.json` — no invocation. |
| 05 | Character & Acting artifact | `artifacts/character_acting_not_reached.json` — no invocation. |
| 06 | Art Director artifact | `artifacts/art_director_not_reached.json` — no invocation. |
| 07 | Continuity result | `artifacts/continuity_not_reached.json` — no invocation. |
| 08 | Shared QA result | `artifacts/shared_qa_not_reached.json` — no invocation. |
| 09 | State Ledger | `AI_Film_Studio_E2E_Run_01_State_Ledger_V0.1.md` — 0 entries, correctly not reached. |
| 10 | Handoff trace | `AI_Film_Studio_E2E_Run_01_Handoff_Trace_V0.1.md`; `envelopes/` — first handoff consumed; second not delivered. |
| 11 | Provider invocation manifest | `provider_manifest.json`; `AI_Film_Studio_E2E_Run_01_Provider_Manifest_V0.1.md`; sibling initial-accounting correction. |
| 12 | E2E-INT report | `acceptance_test_report.json`; `AI_Film_Studio_E2E_Run_01_Acceptance_Test_Report_V0.1.md` — 8 PASS / 4 FAIL / 6 NOT REACHED. |
| 13 | Failure / safe-stop records | `failure_attribution.json`; `AI_Film_Studio_E2E_Run_01_Failure_Attribution_V0.1.md` |

All artifacts reside in this staging-only recovery evidence root. No canonical Skill or Production Lock file is included as a mutation target.
