---
type: systemic-regression-gate-test-report
status: pass
version: 0.1
---

# AI Film Studio Systemic Regression Gate Test Report V0.1

## Result

`PASS` — 14 count-based suites: `144/144`; two provider-free startup suites: `PASS`; Golden recorded regression: `PASS`.

| Tier | Suite results |
| --- | --- |
| Tier 1 | STATE `12/12`; SEM `12/12`; Provider-Free Startup `PASS`; Minimal Harness Startup `PASS`; PERSIST `8/8`; SW-INT `15/15`; SER `12/12`; TRUNC `4/4` |
| Tier 2 | STRICT `15/15`; TOKEN `10/10`; Probe03 Recorded `5/5`; SHOWRUNNER-OWN `10/10`; DIR-INT `12/12`; AD-INT `12/12`; AD-RERUN04 `8/8` |
| Tier 1 + 2 | P0/P1 Runtime Reliability `9/9` |
| Golden recorded | seven role outputs, exact outcomes/tokens, six handoffs, three append-only ledger entries, `E2E-INT 18/18 PASS` |

## Evidence statement

The initial Gate run detected an import-path regression and returned `FAIL`. The direct startup regression was repaired without feature expansion. The final complete rerun above is the authoritative Phase 2 test result.

Counters: `Provider Calls 0`; `Executor Calls 0`; `Role Calls 0`; `Real E2E Runs 0`; `Automatic Retries 0`; `Provider Fallbacks 0`.

