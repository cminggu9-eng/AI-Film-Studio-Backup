---
type: showrunner-rerun02-transport-regression-report
status: passed-provider-free
version: 0.1
date: 2026-08-28
source_run: E2E-RUN-02
---

# Showrunner｜Rerun 02 Transport Regression Report V0.1

## Immutable source

Source artifact: `runtime/_STAGING/_research/Minimal_E2E_Runtime_Validation_V0.1/evidence/E2E-RUN-02/artifacts/showrunner_provider_response.json`.

The persisted `raw_content` SHA-256 remains:

`c221a9762a3be151c6ab08fa5bdcd00b245a0d32c0f6034f3f641b5022fb5689`

No Rerun 02 artifact was changed.

## Recorded-response result

| Check | Result |
| --- | --- |
| Same parsed raw Showrunner response retained | PASS |
| Every role-owned field is unchanged after adapter processing | PASS |
| Adapter is the only origin of the formerly missing `scene_packages` field | PASS |
| Hydrated value | `ABSENT` |
| Full E2E role transport schema after hydration | PASS |
| New creative field / inferred semantic content | 0 |
| Canonical STATUS, flags, and handoffs | Exact preservation PASS |
| E2E-INT-12 token-preservation comparison | PASS |

The baseline failure is therefore resolved solely at the Showrunner-to-Integration transport boundary. This report does not constitute an E2E rerun or accept any new creative output.
