# R02 Golden Replay Compiled Run Contract Evidence V0.1

Result: BLOCKED at Scene Writer strict-schema validation.

The live request was built from Fixture02, but the Scene Writer strict transport rejected its first returned id because the validator enum still admitted only `E2E-FIX-01-S01` through `E2E-FIX-01-S03`. The compiled fixture binding and the validator are therefore not aligned.

Evidence: `artifacts/scene_writer_input.json`, `artifacts/scene_writer_provider_response.json`, and `artifacts/scene_writer_validation_error.json`.

