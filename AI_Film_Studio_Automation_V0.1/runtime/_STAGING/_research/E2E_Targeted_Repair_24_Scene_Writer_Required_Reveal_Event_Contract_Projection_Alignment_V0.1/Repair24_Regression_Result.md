# Repair24 Regression Result

## Repair24 projection gates

| Gate | Result |
| --- | --- |
| Fixture01/02/03 compile reveal event and eligible scene projection | PASS |
| Provider-facing Scene Writer prompt contains current compiled event, status domain, eligible scenes, and no-early-reveal instruction | PASS |
| Strict transport rejects a foreign reveal status token | PASS |
| Legal reveal in an eligible scene is accepted | PASS |
| Early reveal is rejected with `REVEAL_EVENT_TOO_EARLY` and `REQUIRED_REVEAL_EVENT` | PASS |
| Different-but-rehashed projection authority is rejected | PASS |
| R27 all-`NOT_YET_REVEALED` recorded replay remains fail-closed | PASS |
| Auto-promotion/prose inference/retry path | ABSENT; no such code path was introduced |
| Provider / Executor / Role / Probe / Live E2E calls | `0 / 0 / 0 / 0 / 0` |

## Baseline integrity

- Mandatory Preflight: PASS (15 isolated suites, provider-free).
- Fixture Generality: PASS (18/18).
- Unified Phase2: PASS (25 records).
- Repair16-23 provider-free compatibility chain: PASS.
- Canonical Skill hashes: 7/7 unchanged against E2E-RUN-26.
- Production Lock hashes: 6/6 unchanged against E2E-RUN-26.
- E2E-RUN-06 through E2E-RUN-26 remain immutable; E2E-RUN-27 remains an immutable recorded failure.
