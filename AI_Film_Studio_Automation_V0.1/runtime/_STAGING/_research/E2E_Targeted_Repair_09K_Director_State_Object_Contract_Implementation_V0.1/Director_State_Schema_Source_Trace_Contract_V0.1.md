# Director State Schema Source Trace Contract V0.1

Every generated trace item has this exact field set: `field`, `scene`, `property`, `source_contract_pointer`, `source_version`, `canonical_owner`, `source_record_id`, `ledger_sequence`, `type_source`, `enum_source`, `requiredness_source`, and `projection_rule`.

Dynamic trace coverage is mandatory for every `field × scene × dimension`. Current and previous-scene sources point to `run_local_state_ledger_records`; first-scene initial state points to `compiled_run_contract#/state_enums`; lawful explicit prior absence points to Repair 09J authority. Each of the three exact-ABSENT fields has an explicit Repair 09J authority trace.

The validator checks item shape, non-empty provenance fields, non-negative ledger sequence, coverage, and `source_trace_hash`. Removing a source pointer and recomputing the outer trace hash still fails (`DIR-OBJ-NEG-03`). Full traces are preserved in each final request capture artifact.
