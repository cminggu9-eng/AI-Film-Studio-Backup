# Scene Writer Per-Run Scene-ID Contract V0.1

Result: PASS.

One compiled binding produces one immutable projection with these fields:

- `contract_version`
- `binding_id`
- `scene_count`
- `ordered_scene_ids`
- `source_contract_pointer = compiled_run_contract#/scene_ids`
- `contract_hash`

Construction rejects missing identity, empty IDs, duplicates, and count mismatch. Consumers compare the complete ordered token sequence; no reordering, normalization, suffix matching, repair, or cross-run fallback is permitted.
