# Director Fixture01 State Projection Plan V0.1

- Scenes: `E2E-FIX-01-S01`, `E2E-FIX-01-S02`, `E2E-FIX-01-S03` from the compiled contract.
- Dynamic state property: `clothing_visual_state_code` from compiled `state_enums`.
- Enum domain: `soaked_uniform`, `changed_clothes`, inherited from the binding.
- `relevant_prior_state` / `current_state`: closed per-scene object plans with that required property.
- `proposed_state`: exact `ABSENT`; no Director-writable dimension.
- `knowledge_timing`: exact `ABSENT`; no closed projectable knowledge-record schema.
- `visual_state`: exact `ABSENT`; the state dimension lacks explicit visual/spatial classification metadata.

Offline design proof: PASS. These literals occur only in this per-run plan/output, never in generic compiler design.

