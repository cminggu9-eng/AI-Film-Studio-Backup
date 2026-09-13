# Scene Writer Integration State Contract V0.1

## Scope

This is a machine-state handoff contract for the frozen `E2E-FIX-01` Scene Writer fixture. It separates stable canonical tokens from human-readable display prose. It does not change Scene Writer dramatic capability, authority, or canonical identity.

## Exact State Shape

Every `scene_packages[]` item carries a `state_evidence` object with exactly:

`key_identity`, `key_custody`, `knowledge_holders`, `reveal_status`, `relationship_state`, `clothing_visual_state_code`, `clothing_visual_state_display`, `location_presence`, `authorized_transitions`.

## Required Fixture Invariants

- Each of the three scene IDs has `key_identity: A-17`.
- Scene 1 has `clothing_visual_state_code: soaked_uniform`.
- The final scene has `clothing_visual_state_code: changed_clothes`.
- The final scene's `authorized_transitions` includes `change_from_soaked_uniform`.
- At least one reveal uses `REVEALED_WITH_EVENT`; `NOT_YET_REVEALED` remains an exact canonical token where applicable.

## Display Boundary

`clothing_visual_state_display` may express the required output language for human reading. It is never a substitute for `clothing_visual_state_code`; the latter is the machine-checkable token and is never translated.

## Failure Classification

- Missing code: `MISSING_MACHINE_STATE_CODE`
- Wrong/unapproved code: `REQUIRED_STATE_MISMATCH`
- Invalid field shape or extra state keys: `INVALID_STATE_EVIDENCE`

The gate reports these errors; it never synthesizes state or rewrites a scene.

