# Scene Writer Integration Contract Test Report V0.1

## Result

**PASS — SW-INT-01 through SW-INT-15: 15/15.** This offline suite made **0 provider calls** and **0 real role executions**.

## Verified Contract Areas

| Area | Result |
| --- | --- |
| Harness wiring | The Scene Writer role validation path invokes the integration contract. |
| Code/display split | Exact machine token is required; display prose is preserved independently. |
| Structural output | All six exact deliverable keys are required per scene. |
| State / attribution shape | Exact field sets, IDs, reveal tokens, and transition are enforced. |
| Failure behavior | Invalid/missing state and structure yield attributable errors; no rewrite occurs. |
| Regression | Frozen recovery failure is detected as `MISSING_MACHINE_STATE_CODE` plus `MISSING_STRUCTURAL_DELIVERABLE`. |
| Integrity | Scene Writer canonical Skill SHA-256 remained `93E1BE12988F8CAA6CDD76ACB5E6C1BF6AD3CA0DFF5806A2EA93511E66052DFB`. |

## Execution

`python -X utf8 runtime/_STAGING/_research/E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1/tests/run_scene_writer_integration_contract_tests.py`

