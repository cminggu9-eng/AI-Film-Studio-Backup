---
type: systemic-regression-gate
status: active-staging-gate
version: 0.1
---

# AI Film Studio Systemic Regression Gate V0.1

## Entry point

`python -X utf8 -B E:\AI_Film_Studio\AI_Film_Studio_Automation_V0.1\runtime\_STAGING\_research\Systemic_Hardening_Phase_2_Runtime_Reliability_Regression_Enforcement_V0.1\run_systemic_regression_gate.py`

The Gate runs only Tier 1 provider-free suites and Tier 2 recorded-response suites. Each record reports suite, tier, invariant, failure lineage, test count, evidence script, and `PASS` / `FAIL`. Missing Golden evidence returns `BLOCKED`; no provider, executor, role call, retry, fallback, or E2E run is allowed.

## Stop rule

Any `FAIL` is `HARDENING REGRESSION DETECTED`: stop layering changes, repair the failing boundary only, then rerun the complete Gate. Tier 3 is not invoked by this entry point.

