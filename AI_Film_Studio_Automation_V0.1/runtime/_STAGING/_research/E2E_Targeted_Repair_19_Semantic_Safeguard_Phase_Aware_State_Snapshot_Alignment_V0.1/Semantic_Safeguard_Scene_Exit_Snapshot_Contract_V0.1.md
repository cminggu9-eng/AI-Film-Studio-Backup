# Scene Exit Snapshot Contract

EXIT is the current scene's validated `state_evidence` and remains the semantic meaning of the Scene Ledger snapshot: `SCENE_LEDGER_STATE_SNAPSHOT_IS_EXIT_POST_STATE`.

An EXIT value can advance from ENTRY only when the shared transition classifier reports actual occurrence. `AUTHORIZED` alone, a future/planned transition, and a merely described transition cannot mutate the projected state.

R24 S01 example: the validated EXIT is `battery_removed_and_sealed`, sourced from the recorded Scene Writer package. That is valid post-scene evidence and is no longer misused as S01's initial required state.
