---
type: integration-contract-repair-provider-free-startup-test-report
status: passed
version: 0.1
date: 2026-08-26
classification: fresh-process-static-startup-proof
---

# AI Film Studio｜Provider-Free Startup Test Report V0.1

## Result

PASS.

The test installed traps for DeepSeekProviderAdapter initialization/completion and ModelExecutor construction/execution, then performed all required imports and static discovery. Every trap counter remained zero.

| Counter | Result |
| --- | --- |
| Provider initializations | 0 |
| Provider completions / calls | 0 |
| Executor initializations | 0 |
| Executor calls | 0 |

| Required check | Result |
| --- | --- |
| Clean import | PASS |
| Harness import | PASS |
| Configuration load | PASS |
| Role discovery | PASS |
| Adapter discovery | PASS |
| State-envelope load | PASS |
| Fixture load | PASS |
| Legacy smoke runner import | PASS |
| Legacy synthetic runner import | PASS |

## Executed test

AI_Film_Studio_Automation_V0.1/runtime/_STAGING/_research/Integration_Contract_Repair_V0.1/tests/run_provider_free_startup_test.py

## Boundary

The proof imports and discovers only. It does not call a provider, instantiate an executor, create a Runtime, run a role, or execute E2E-FIX-01.
