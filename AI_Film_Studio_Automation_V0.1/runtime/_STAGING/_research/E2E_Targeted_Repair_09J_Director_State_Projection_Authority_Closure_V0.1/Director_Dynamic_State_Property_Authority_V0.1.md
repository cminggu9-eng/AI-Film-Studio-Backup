# Director Dynamic State Property Authority V0.1

Every generated scene property is sourced from `compiled_run_contract.scene_ids`. Every generated state-dimension property and its exact enum comes from the compiled strict scene-package state schema / `state_enums`.

The compiler emits a sidecar authority manifest for each property containing:

- JSON pointer to its compiled source;
- compiled contract/version identity;
- canonical source owner;
- selected source record ID and Ledger sequence for value validation.

Properties lacking all required provenance are excluded only when their governing field contract authorizes exclusion; otherwise compilation fails. Historical model output never supplies a property or enum.

