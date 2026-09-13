# State Phase Negative Test Report

Command:

```text
python -X utf8 -B tests/run_state_phase_negative_tests.py
```

Result: `15 / 15 PASS`.

The matrix rejects ENTRY/EXIT cross-comparisons, authorization-only and planned transitions, all-phase latest-ledger fallback, EXIT substitution for missing ENTRY, implicit persistence, fixture business literals, automatic repair, missing source trace, and invalid/conflicting state sources. It also confirms R24 raw evidence and its complete evidence tree remain immutable.

Call counters: provider `0`, executor `0`, role `0`, probe `0`, live E2E `0`.
