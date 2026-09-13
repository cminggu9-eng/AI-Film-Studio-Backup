# REQUIRED_STATE Provenance Audit

## Finding

`E2E-RUN-24` was blocked because `REQUIRED_STATE` read the Scene Writer state ledger snapshot as though it represented the initial state. That snapshot is the scene EXIT/POST state, so the R24 S01 value `battery_removed_and_sealed` was compared with the correctly compiled initial token `battery_installed`.

## Repair19 decision

`REQUIRED_STATE` now carries a `STATE_PHASE_SNAPSHOT_V0.1` selection object in its existing `value` slot. It explicitly selects the `ENTRY` snapshot and includes full provenance. No new top-level transport field was introduced.

## R24 replay result

The required assertion resolves to `ENTRY / battery_installed`, sourced from `compiled_run_contract#/fixture/state_dimensions/0/allowed_tokens/0`, owned by `Fixture Binding / Compiled Run Contract`. The replay decision is `PASS`.

## Boundary

The recorded Scene Writer output and R24 evidence were not edited. This is a parser/assertion phase-selection repair only.
