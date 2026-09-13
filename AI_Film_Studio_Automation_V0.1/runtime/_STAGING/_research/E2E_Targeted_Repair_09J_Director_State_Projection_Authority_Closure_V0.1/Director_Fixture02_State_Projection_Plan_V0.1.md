# Director Fixture02 State Projection Plan V0.1

- Scenes: `E2E-FIX-02-S01`, `E2E-FIX-02-S02`, `E2E-FIX-02-S03` from the compiled contract.
- Dynamic state property: `signboard_state`.
- Enum domain: `signboard_on`, `signboard_off`.
- `relevant_prior_state` / `current_state`: closed per-scene object plans with that required property.
- `proposed_state`, `knowledge_timing`, `visual_state`: exact `ABSENT` under the same authority rules.

Offline design proof: PASS. All fixture values were read from compiled outputs.

