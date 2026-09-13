# R03 Golden Replay evidence coverage index

This index distinguishes completed fresh evidence from records that were not reached after the Director safe stop.

| Required evidence | Status | Fresh artifact or reason |
|---|---|---|
| 1 Execution Manifest | PASS | execution_manifest.json |
| 2 Preflight Provenance | PASS | preflight.json |
| 3 F03 Binding Evidence | PASS | authorization.json and showrunner_input.json |
| 4 Compiled Run Contract | PASS | current binding-derived projection in Scene Writer input and wire artifacts |
| 5 Scene-ID Projection | PASS | scene_writer_final_wire_payload.json |
| 6 State-Field Projection | PASS | scene_writer_final_wire_payload.json |
| 7 Scene Writer Wire Strict Schema | PASS | scene_writer_final_wire_payload.json and scene_writer_schema_identity_manifest.json |
| 8 Scene Writer Completeness | PASS | scene_writer_output.json |
| 9 Entity Identity Projection | PASS | semantic_safeguard.json |
| 10 Transition Authority | PASS | semantic_safeguard.json |
| 11 State Phase Projection | PASS | semantic_safeguard.json and state_ledger.json |
| 12 Knowledge Timing | PASS | scene_writer_output.json and semantic_safeguard.json |
| 13 Cross-Fixture Genericity | PASS, offline preflight | preflight.json isolated ENV-ISO evidence |
| 14 Provider Manifest | PASS | provider_manifest.json |
| 15 Handoff Trace | PARTIAL | only successful upstream handoffs; see Handoff Trace |
| 16 State Ledger | PARTIAL | fresh append-only scene records; no downstream decision written |
| 17 Showrunner Evidence | PASS | artifacts/showrunner_* |
| 18 Scene Writer Strict Evidence | PASS | artifacts/scene_writer_* |
| 19 Scene Writer Hydration Evidence | PASS | scene_writer_output.json; no missing-field hydration occurred |
| 20 Safeguard Identity Evidence | PASS | semantic_safeguard.json |
| 21 Safeguard Transition Evidence | PASS | semantic_safeguard.json |
| 22 Safeguard State Phase Evidence | PASS | semantic_safeguard.json |
| 23 Director State Schema Evidence | PASS | director_final_wire_payload.json |
| 24 Director Source Trace Evidence | PASS | director_input.json |
| 25 Director Strict Evidence | FAIL, raw-first preserved | director_provider_response.json and director_validation_error.json |
| 26 Character and Acting Raw9 | NOT REACHED | Director safe stop |
| 27 Character and Acting Reserved Slot | NOT REACHED | Director safe stop |
| 28 Character and Acting Final10 | NOT REACHED | Director safe stop |
| 29 Art Director | NOT REACHED | Director safe stop |
| 30 Continuity Outcome | NOT REACHED | Director safe stop |
| 31 Continuity State | NOT REACHED | Director safe stop |
| 32 Shared QA | NOT REACHED | Director safe stop |
| 33 F03 Semantic Audit | NOT REACHED | requires complete seven-role chain |
| 34 E2E-INT Acceptance | NOT REACHED | acceptance_test_report.json |
| 35 Final Lifecycle Gate | NOT REACHED | requires complete seven-role chain |
| 36 Cost Report | PASS | R03_Golden_Replay_Cost_Report_V0.1.md |
| 37 Final Evidence Bundle | PASS | AI_Film_Studio_E2E_Run_26_Evidence_Bundle_V0.1.md |
| 38 Golden Replay Final Review | PASS, failure review | R03_Golden_Replay_Restart_After_Repair20_Failure_Review_V0.1.md |
| 39 Task Record | PASS | R03_Golden_Replay_Task_Record_V0.1.md |
| 40 Work Log | PASS | R03_Golden_Replay_Work_Log_V0.1.md |
