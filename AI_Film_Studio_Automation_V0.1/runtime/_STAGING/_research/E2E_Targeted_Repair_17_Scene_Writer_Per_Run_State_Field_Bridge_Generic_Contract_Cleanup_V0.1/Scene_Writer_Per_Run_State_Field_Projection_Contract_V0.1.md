# Scene Writer Per-Run State-Field Projection Contract V0.1

`build_scene_writer_state_projection(compiled_run_contract)` is the single projection constructor.

It requires exactly one compiled state dimension, exact agreement with `state_enums`, non-empty unique tokens, a binding ID, tracked entities, and transition identity shared with `ledger_tracking`. It emits `state_dimension_id == transport_field_name`; the hash covers every authority-bearing field except itself.

Any missing, conflicting, duplicated, or cross-run value fails closed. No token-to-field heuristic exists.
