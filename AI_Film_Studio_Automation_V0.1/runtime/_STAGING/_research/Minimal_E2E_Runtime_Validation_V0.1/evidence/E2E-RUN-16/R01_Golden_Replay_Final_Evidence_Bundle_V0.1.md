# R01 Golden Replay Final Evidence Bundle V0.1

Run root: `E2E-RUN-16`

Core machine evidence:

- `authorization.json`
- `execution_manifest.json`
- `preflight.json`
- `provider_manifest.json`
- `handoff_trace.json` when complete; partial handoffs are preserved in `envelopes/`
- `state_ledger.json`
- `semantic_safeguard.json`
- `failure_attribution.json`
- `acceptance_test_report.json`

Per-call evidence is under `artifacts/` and contains raw responses, invocation metadata, usage, finish reason, trace evidence, truncation classification, persistence verification, parsed outputs where validation passed, and the Character & Acting validation error.

Additive review evidence consists of the `R01_Golden_Replay_*_V0.1.md` files in this root. Historical E2E-RUN-06 through E2E-RUN-15 files modified after this run started: 0.

