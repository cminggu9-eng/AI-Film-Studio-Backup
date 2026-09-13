# Required State Phase Binding

`build_scene_assertions()` binds an initial-state `REQUIRED_STATE` assertion to `required_phase: ENTRY`. Its selected value is the ENTRY projection token, and its expected value remains the compiled initial allowed token.

The existing assertion transport fields retain their meanings. The phase object is nested in the existing `value` field, avoiding a transport-schema expansion. The Safeguard resolves that object before comparison and preserves historical plain-value assertion behavior for immutable evidence replays.

This separates phase-source faults (`REQUIRED_STATE_PHASE_SOURCE_FAILURE`) from genuine conformance mismatches (`REQUIRED_STATE_MISMATCH`).
