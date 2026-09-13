# Semantic Safeguard State Phase Model

`STATE_PHASE_SNAPSHOT_V0.1` defines two distinct snapshots for every validated state dimension:

- `ENTRY` — initial compiled state for S01, or the prior scene's validated EXIT state for later scenes.
- `EXIT` — the current scene's validated `state_evidence` after an actual recorded transition.

The projection is generic: it derives dimensions and allowed tokens from the compiled fixture binding. It contains no fixture-specific business literals.

Each snapshot records scene id, dimension, phase, value, source artifact/version, canonical owner, evidence pointer, source kind, and source binding id. A malformed, missing, or phase-mismatched source is rejected as `REQUIRED_STATE_PHASE_SOURCE_FAILURE` rather than silently substituted.
