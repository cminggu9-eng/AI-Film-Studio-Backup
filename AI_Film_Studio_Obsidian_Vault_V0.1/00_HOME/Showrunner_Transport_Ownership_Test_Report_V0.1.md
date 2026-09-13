---
type: showrunner-transport-ownership-test-report
status: passed-provider-free
version: 0.1
date: 2026-08-28
---

# Showrunner｜Transport Ownership Test Report V0.1

Test runner:

`runtime/_STAGING/_research/E2E_Targeted_Repair_04_Showrunner_Transport_Ownership_Separation_V0.1/tests/run_showrunner_transport_ownership_tests.py`

Result: **10 / 10 PASS**. Provider Calls = 0; Executor Calls = 0.

| Test | Result | Evidence |
| --- | --- | --- |
| OWN-01 | PASS | Missing transport-only slot hydrates to `ABSENT`. |
| OWN-02 | PASS | Missing Canon field remains failure. |
| OWN-03 | PASS | Missing knowledge-timing field remains failure. |
| OWN-04 | PASS | Missing required assignment field remains failure. |
| OWN-05 | PASS | Existing/downstream package cannot be overwritten; downstream-exists absence is rejected. |
| OWN-06 | PASS | Adapter cannot infer Canon locks from prose. |
| OWN-07 | PASS | `ABSENT` is integration-only, not a Showrunner token. |
| OWN-08 | PASS | Canonical Showrunner hash and recorded raw response unchanged. |
| OWN-09 | PASS | Immutable Rerun 02 raw response passes full schema after lawful hydration only. |
| OWN-10 | PASS | E2E-INT-12 remains exact. |

## Regression matrix

| Suite | Result |
| --- | --- |
| Provider-Free Startup | PASS; Provider and Executor call counters 0. |
| Minimal E2E harness import | PASS; Provider and Executor initialization/call counters 0. |
| PERSIST | 8 / 8 PASS |
| SW-INT | 15 / 15 PASS |
| STRICT | 15 / 15 PASS |
| TOKEN | 10 / 10 PASS |
| Probe03 recorded replay | 5 / 5 PASS |
| Canonical Skill hashes | 7 / 7 unchanged |

The Minimal E2E preflight now includes `SHOWRUNNER-OWN` at 10 / 10 as a provider-free gate.
