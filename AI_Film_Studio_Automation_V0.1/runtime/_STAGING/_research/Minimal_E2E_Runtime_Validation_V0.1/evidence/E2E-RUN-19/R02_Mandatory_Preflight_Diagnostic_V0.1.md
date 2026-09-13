# R02 Mandatory Preflight Diagnostic V0.1

## Result

BLOCKED before Executor construction.

## Earliest failing suite

- Suite: SW-INT.
- Result: 14/15; first failure `SW-INT-01`.
- Error: `E2EBlocked: Scene package IDs are not exact and ordered`.

The SW-INT fixture builds its recorded case with Fixture01-era `contract.SCENE_IDS`, while the imported live runner reads inherited `AFS_E2E_FIXTURE_BINDING=E2E-FIX-02` and validates against Fixture02 scene IDs. `rerun_preflight()` launches `_run_static_suite()` with the live run environment unchanged; unlike `static_preflight()`, it does not scrub run-local fixture variables for historical/offline suites.

STRICT then raised the same scene-ID mismatch. Repair13 and Repair14 core failures were downstream aggregate regressions from the same contaminated suite environment.

Provider / Executor / Role calls during diagnosis: 0 / 0 / 0.

