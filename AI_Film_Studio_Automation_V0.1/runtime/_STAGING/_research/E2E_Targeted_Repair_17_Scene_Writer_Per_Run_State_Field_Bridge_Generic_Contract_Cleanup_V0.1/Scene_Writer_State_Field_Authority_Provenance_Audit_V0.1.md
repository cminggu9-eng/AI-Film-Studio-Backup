# Scene Writer State-Field Authority Provenance Audit V0.1

Result: PASS.

The real compiled artifact was inspected before the projection was defined. The authoritative dimension record is `compiled_run_contract.fixture.state_dimensions[0]`; its identity is independently mirrored by `compiled_run_contract.state_enums`, while transitions are mirrored by `fixture.authorized_transitions` and `ledger_tracking.authorized_transitions`.

The projection records binding ID, contract version, dimension and transport field identity, ordered machine-token domain, initial token as ordered domain index 0, authorized transitions, tracked entities, exact compiled pointers, source owner `compiled_run_contract`, and a deterministic hash. Provider output, prompt examples, previous runs, and Python fixture constants are not authority.

Evidence: `evidence/state_projection_manifest.json`.
