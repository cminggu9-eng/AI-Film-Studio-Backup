# Director relevant_prior_state Selection Contract V0.1

For every `scene_id` supplied by `compiled_run_contract.scene_ids`, Integration selects the validated carry-in snapshot immediately preceding that scene.

Source priority is: run-local Ledger validated pre-scene record; validated upstream handoff state; compiled initial state only for the first scene when no earlier Ledger record exists. Director and Provider never select the source.

The schema is a closed scene-keyed object. Every scene property uses the exact compiled state schema: dimension properties and enum values come from the run's strict scene-package state schema. All compiled scenes and dimensions are required; `additionalProperties:false` applies at both levels.

If an explicit source contract says the whole Director scope has no lawful prior state, exact `ABSENT` is allowed. A missing required per-scene source, ambiguous association, or conflict fails closed and may not become `ABSENT`.

Status: **AUTHORITY CLOSED**.

