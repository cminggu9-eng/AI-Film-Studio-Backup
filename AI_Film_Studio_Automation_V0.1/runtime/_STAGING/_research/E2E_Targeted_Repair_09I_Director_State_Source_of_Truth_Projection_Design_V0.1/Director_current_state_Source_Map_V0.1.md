# Director current_state Source Map V0.1

| Map element | Source-backed finding |
|---|---|
| Primary authority source | validated Scene Writer scene-package state / State Ledger snapshot |
| Secondary carried source | compiled run locks, prohibitions, state enums, authorized transitions |
| Projection owner | Integration |
| Projected keys | compiled scene-package `state` is closed per binding, but Director's winner scene/snapshot is **OPEN** |
| Requiredness / type | selected source `state` is an exact object; selection rule is missing |
| Token source | `compiled_run_contract().state_enums` |
| Forbidden-key source | compiled `additionalProperties:false` state schema plus Director boundary |
| ABSENT rule | only if the upstream contract declares current state unavailable; cannot hide absent source selection |
| Director writable dimensions | none for carried current facts |
| Failure route | multiple/ambiguous snapshots -> fail closed, upstream decision required |

Offline Fixture01–03 compilation confirms the state keys are dynamic (`clothing_visual_state_code`, `signboard_state`, `camera_battery_state`). No existing contract says which one of the ordered multi-scene records becomes the Director field, or whether all are required. Therefore `AUTHORITY OPEN`.

