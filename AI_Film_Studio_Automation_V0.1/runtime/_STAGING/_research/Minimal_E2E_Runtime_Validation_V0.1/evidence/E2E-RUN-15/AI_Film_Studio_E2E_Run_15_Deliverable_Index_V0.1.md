# AI Film Studio E2E RUN 15 Deliverable Index V0.1

This index maps the 23 authorized R01 deliverables to the immutable run artifacts that were reached. Downstream items after the Art Director blocker are explicitly `NOT REACHED` rather than synthesized.

| # | Deliverable | Status | Primary evidence |
| --- | --- | --- | --- |
| 1 | R01 Fresh Execution Manifest | COMPLETE | `execution_manifest.json`; `AI_Film_Studio_E2E_Run_15_Execution_Manifest_V0.1.md` |
| 2 | R01 Provider Manifest | COMPLETE | `provider_manifest.json`; `AI_Film_Studio_E2E_Run_15_Provider_Manifest_V0.1.md` |
| 3 | R01 Handoff Trace | COMPLETE TO SAFE STOP | `AI_Film_Studio_E2E_Run_15_Handoff_Trace_V0.1.md`; `envelopes/01` through `04` |
| 4 | R01 State Ledger | COMPLETE TO SAFE STOP | `state_ledger.json`; `AI_Film_Studio_E2E_Run_15_State_Ledger_V0.1.md` |
| 5 | R01 Showrunner Evidence | PASS | `artifacts/showrunner_input.json`; `showrunner_provider_response.json`; `showrunner_invocation.json`; `showrunner_persistence_verification.json`; `showrunner_truncation_detection.json`; `showrunner_output.json` |
| 6 | R01 Scene Writer Strict Evidence | PASS | `artifacts/scene_writer_input.json`; `scene_writer_provider_response.json`; `scene_writer_invocation.json`; `scene_writer_persistence_verification.json`; `scene_writer_truncation_detection.json`; `scene_writer_output.json` |
| 7 | R01 Transition Authority Evidence | PASS | `state_ledger.json`; `semantic_safeguard.json`; `artifacts/scene_writer_output.json` |
| 8 | R01 Semantic Safeguard Evidence | PASS | `semantic_safeguard.json`; `AI_Film_Studio_E2E_Run_15_Semantic_Safeguard_Report_V0.1.md` |
| 9 | R01 Director Compiled State Schema Evidence | PASS | `artifacts/director_final_wire_payload.json` (`state_schema_sha256`) |
| 10 | R01 Director Source Trace Evidence | PASS | `artifacts/director_final_wire_payload.json` (`source_trace_sha256` and `director_state_projection.source_trace`) |
| 11 | R01 Director Strict Submission Evidence | PASS | `artifacts/director_final_wire_payload.json`; `director_provider_response.json`; `director_invocation.json`; `director_persistence_verification.json`; `director_output.json` |
| 12 | R01 Director Downstream Object Carriage Evidence | PASS | `envelopes/03_director_to_character_acting.json`; `artifacts/character_acting_input.json` |
| 13 | R01 Character & Acting Evidence | PASS | `artifacts/character_acting_input.json`; `character_&_acting_provider_response.json`; `character_&_acting_invocation.json`; `character_&_acting_persistence_verification.json`; `character_acting_output.json` |
| 14 | R01 Art Director Evidence | BLOCKED AFTER RAW PERSISTENCE | `artifacts/art_director_input.json`; `art_director_provider_response.json`; `art_director_invocation.json`; `art_director_persistence_verification.json`; `art_director_truncation_detection.json`; `art_director_validation_error.json` |
| 15 | R01 Continuity Evidence | NOT REACHED | Upstream Art Director blocker; no Provider call or synthetic evidence |
| 16 | R01 Shared QA Evidence | NOT REACHED | Upstream Art Director blocker; no Provider call or synthetic evidence |
| 17 | R01 Strict Transport Lifecycle Evidence | PARTIAL / FINAL GATE NOT REACHED | `provider_manifest.json`; Scene Writer and Director are the only reached strict pairs |
| 18 | R01 E2E-INT-01–18 Acceptance Report | COMPLETE: 0/18 NOT REACHED | `acceptance_test_report.json`; `AI_Film_Studio_E2E_Run_15_Acceptance_Test_Report_V0.1.md` |
| 19 | R01 Final Lifecycle Gate Report | NOT REACHED | `execution_manifest.json` (`lifecycle_consistency.result = NOT_REACHED`); `AI_Film_Studio_E2E_Run_15_Gate_Report_V0.1.md` |
| 20 | R01 Final Evidence Bundle | COMPLETE TO SAFE STOP | `AI_Film_Studio_E2E_Run_15_Evidence_Bundle_V0.1.md`; this index |
| 21 | R01 Golden Replay Final Review | COMPLETE | `AI_Film_Studio_Minimal_E2E_Runtime_Validation_Rerun_15_Final_Review_V0.1.md`; `AI_Film_Studio_E2E_Run_15_Independent_Failure_Layer_Audit_V0.1.md` |
| 22 | Task Record update | COMPLETE | `AI_Film_Studio_E2E_Run_15_Task_Record_V0.1.md` |
| 23 | Work Log update | COMPLETE | `AI_Film_Studio_E2E_Run_15_Work_Log_V0.1.md` |

## Final state

`R01 GOLDEN REPLAY FAILED — TARGETED REPAIR REQUIRED`

No R02, R03, Human Acceptance, or Production Readiness activity was started.
