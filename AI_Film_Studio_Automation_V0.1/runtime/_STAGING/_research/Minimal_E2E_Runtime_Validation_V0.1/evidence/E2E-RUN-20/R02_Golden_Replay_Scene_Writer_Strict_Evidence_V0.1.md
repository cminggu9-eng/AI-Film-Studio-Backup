# R02 Golden Replay Scene Writer Strict Evidence V0.1

Result: FAIL, local strict schema validation.

The provider emitted the forced function `submit_scene_writer_package`, with `finish_reason: tool_calls` and no truncation signal. Its first id was `E2E-FIX-02-S01`; the local enum accepted only Fixture01 ids. The raw third id is also `E2E-FIX-03-S03`, so an aligned Fixture02 validator must retain exact per-scene enforcement and reject that independently if replayed. This is a parser/contract mismatch, not a provider transport or semantic rewrite failure.

Evidence: `artifacts/scene_writer_provider_response.json`, `artifacts/scene_writer_truncation_detection.json`, and `artifacts/scene_writer_validation_error.json`.
