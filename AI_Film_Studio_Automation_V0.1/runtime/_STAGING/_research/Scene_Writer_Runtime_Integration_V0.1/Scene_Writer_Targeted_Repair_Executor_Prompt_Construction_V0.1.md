# Executor Prompt Construction Repair V0.1

## Implemented repair surface

- Added `runtime/scene_writer/execution_projection.py` as Runtime-only `MODE / STATE AWARE EXECUTION PROJECTION` data.
- Replaced the executor's universal `scene or revision` instruction with a mode-specific projection in `CanonicalSceneWriterExecutor._request`.
- Added explicit serialization rules: a mode never forces creative output; omit inapplicable fields; never use empty strings or empty creative packets as placeholders.
- Kept the two-key output envelope and all canonical state/flag tokens unchanged.

## State enforcement added in Runtime

- `NO_MATERIAL_CHANGE`: null creative + `material_rewrite_claimed: false`; DIAGNOSE also requires non-empty `diagnosis_summary`.
- `NEEDS_CONTEXT`, `UPSTREAM_DECISION_REQUIRED`, and `REQUEST_OUT_OF_SCOPE`: creative content is forbidden.
- `UPSTREAM_DECISION_REQUIRED`: preserves `UPSTREAM_HANDOFF_REQUIRED`, requires `upstream_decision_needed`, and now requires at least one lawful handoff packet.
- State-specific forbidden non-null boundary fields fail safe. Existing Runtime language validation remains intact.

## Evidence

- Existing Runtime contract regression: `RT-SW-01–30 = 30 / 30 PASS` after the repair.
- TR-SW-01–09 and TR-SW-20 pass in every recorded Targeted Repair attempt.
- No canonical Skill text, capability rule, mode token, primary-state token, flag/handoff token, or authority boundary was changed.

## Current limitation

The output-projection portion is structurally validated, but its real F06/F11/F12/F13 rerun was not authorized to start because the verifier gate did not meet the prerequisite `TR-SW-01–20 = 20 / 20 PASS`.
