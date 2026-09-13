---
type: director-integration-contract-test-report
status: complete-awaiting-user-review
version: 0.1
date: 2026-08-28
---

# Director Integration Contract Test Report V0.1

## Result

`DIR-INT-01` through `DIR-INT-12`: **12 / 12 PASS**. All tests were provider-free and executor-free.

| Test | Result | Verified boundary |
| --- | --- | --- |
| DIR-INT-01 / 02 | PASS | Exact canonical Modes and Primary States preserved. |
| DIR-INT-03 / 04 | PASS | Eight semantic fields accounted; machine IDs separated from heading tokens. |
| DIR-INT-05 | PASS | Rerun 03 classified `MIXED STRUCTURAL + TRANSPORT FAILURE`. |
| DIR-INT-06 / 07 | PASS | Heading-different fixture is structurally rejected without repair; a truly missing field is rejected. |
| DIR-INT-08 / 09 | PASS | Unknown state is rejected; failed validation mutates no raw content. |
| DIR-INT-10 | PASS | Director canonical Skill hash unchanged. |
| DIR-INT-11 / 12 | PASS | State & Evidence Envelope and E2E-INT-12 tokens preserved exactly. |

Source test: `runtime/_STAGING/_research/E2E_Targeted_Repair_05_Director_Output_Contract_Transport_Alignment_V0.1/tests/run_director_integration_contract_tests.py`.

## Existing provider-free regression

All passed after Repair 05: PERSIST `8/8`, SW-INT `15/15`, STRICT `15/15`, TOKEN `10/10`, Probe03 recorded replay `5/5`, SHOWRUNNER-OWN `10/10`, provider-free startup, Minimal E2E harness startup, and canonical Skills `7/7` unchanged. Provider Calls and Executor Calls for these regressions: `0`.
