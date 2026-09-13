---
type: integration-contract-repair-state-contract-test-report
status: passed
version: 0.1
date: 2026-08-26
classification: offline-no-provider-no-runtime
---

# AI Film Studio｜State Contract Test Report V0.1

## Result

STATE-01 through STATE-12: 12 / 12 PASS.

The offline test ran the Staging State & Evidence Envelope and run-local Ledger only. Provider calls, executor calls, role executions, E2E execution, and persistence services were not used.

| ID | Result | Evidence |
| --- | --- | --- |
| STATE-01 | PASS | Source record ID and version preserved. |
| STATE-02 | PASS | Locks preserved. |
| STATE-03 | PASS | CREATE and SCENE_CREATED remained exact tokens. |
| STATE-04 | PASS | ABSENT preserved without synthesis. |
| STATE-05 | PASS | Knowledge timing attributable. |
| STATE-06 | PASS | Prior, current, and proposed state distinguishable. |
| STATE-07 | PASS | Visual state attributable. |
| STATE-08 | PASS | Relationship state attributable when present. |
| STATE-09 | PASS | Authority owner preserved. |
| STATE-10 | PASS | Comparison evidence supplied without a Continuity decision. |
| STATE-11 | PASS | Missing current state was not silently repaired. |
| STATE-12 | PASS | Ledger has no database dependency. |

## Executed test

AI_Film_Studio_Automation_V0.1/runtime/_STAGING/_research/Integration_Contract_Repair_V0.1/tests/run_state_contract_tests.py

## Integrity

Provider Calls = 0. Executor Calls = 0. Real Role Executions = 0. Real E2E Executions = 0.
