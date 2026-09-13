# R02 Golden Replay Cross-Fixture Genericity Audit V0.1

Result: FAIL.

The active Scene Writer integration contract declares `SCENE_IDS = E2E-FIX-01-S01..S03`; the strict transport imports that constant to construct the `id` enum. This Fixture01 literal directly contaminated the Fixture02 live path. Fixture02 output ids were therefore rejected before parsing.

Repair boundary: parameterize Scene Writer scene-id schema, serialization, and validation from the compiled binding; retain Fixture01 behavior through its own binding, not global constants.

Evidence: `artifacts/scene_writer_validation_error.json`; source locations are `E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1/implementation/scene_writer_integration_contract.py:18` and `E2E_Targeted_Repair_03_Strict_Structured_Transport_V0.1/implementation/scene_writer_strict_transport.py:119`.

