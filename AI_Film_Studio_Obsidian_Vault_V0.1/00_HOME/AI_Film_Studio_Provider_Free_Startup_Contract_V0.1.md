---
type: integration-contract-repair-provider-free-startup-contract
status: implemented-and-tested
version: 0.1
date: 2026-08-26
scope: import-discovery-static-startup-only
---

# AI Film Studio｜Provider-Free Startup Contract V0.1

## Guarantee

During IMPORT, DISCOVERY, and STATIC STARTUP:

- Provider Calls = 0.
- Executor Calls = 0.
- Provider initialization = 0.
- Executor construction = 0.
- No API request, automatic model execution, smoke execution, fallback execution, or retry execution is permitted.

## Explicit execution boundary

Scene Writer provider construction is now local to create_scene_writer_binding. Importing or discovering the binding module cannot construct the DeepSeek adapter or ModelExecutor. Calling that factory is an explicit execution-capable boundary; it still does not itself make a provider completion call.

The factory remains unavailable to this repair’s startup proof and is not called in this phase.

## Legacy runner repair

| Asset | Before | After |
| --- | --- | --- |
| Scene Writer run_smoke_sw_exec_01.py | Import executed the real smoke path. | Assignment remains data-only at import; binding and execution are inside main. |
| Scene Writer run_synthetic_e2e.py | Import constructed a Runtime and executed a synthetic executor. | Runtime construction and execution are inside main. |

The historical runners were not executed as part of this repair.

## Required provider-free startup checks

1. Clean import.
2. Integration harness import.
3. Configuration load.
4. Scene Writer role discovery.
5. Scene Writer adapter discovery.
6. State Envelope contract load.
7. Frozen E2E-FIX-01 document load.
8. Legacy smoke runner import.
9. Legacy synthetic runner import.

## Implementation locations

- Scene Writer staging binding and runner repair: runtime/_STAGING/_research/Scene_Writer_Runtime_Integration_V0.1.
- Provider-free harness: runtime/_STAGING/_research/Integration_Contract_Repair_V0.1/implementation/integration_contract/provider_free_startup.py.

No canonical Skill semantic or Production Lock was changed.
