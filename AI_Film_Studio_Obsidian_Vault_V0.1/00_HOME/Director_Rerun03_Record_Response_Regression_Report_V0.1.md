---
type: director-rerun03-recorded-response-regression
status: complete-awaiting-user-review
version: 0.1
date: 2026-08-28
---

# Director Rerun 03 Recorded Response Regression Report V0.1

## Immutable source

`.../Minimal_E2E_Runtime_Validation_V0.1/evidence/E2E-RUN-03/artifacts/director_provider_response.json`

`raw_content_sha256`: `5cccb3c3564f39a1b211fdbfb3c73b89f8c459ef438794e8946f50c9c7414e57`

## Regression finding

| Check | Result |
| --- | --- |
| JSON parsed / raw usage persisted / not truncated | PASS |
| Canonical Primary State | `DIRECTION_PLAN_PRODUCED` exact |
| `flags` and `handoffs` | `ABSENT` exact |
| All eight canonical heading tokens present | PASS |
| Semantic fields present | PASS |
| Canonical heading order | FAIL: `SPATIAL GEOGRAPHY` occurs before `AUDIENCE INFORMATION` |
| Old historical parser title-case requirements | FAIL: it demanded non-canonical variants |
| Raw content altered for regression | No; mutation count `0` |

The new deterministic contract identifies all canonical structure without editing the creative raw response. It correctly rejects the Rerun 03 response as a canonical order failure and does not treat it as semantic absence.
