# Director Fixture03 State Projection Plan V0.1

- Scenes: `E2E-FIX-03-S01`, `E2E-FIX-03-S02`, `E2E-FIX-03-S03` from the compiled contract.
- Dynamic state property: `camera_battery_state`.
- Enum domain: `battery_installed`, `battery_removed_and_sealed`.
- `relevant_prior_state` / `current_state`: closed per-scene object plans with that required property.
- `proposed_state`, `knowledge_timing`, `visual_state`: exact `ABSENT` under the same authority rules.

Offline design proof: PASS. All fixture values were read from compiled outputs.

