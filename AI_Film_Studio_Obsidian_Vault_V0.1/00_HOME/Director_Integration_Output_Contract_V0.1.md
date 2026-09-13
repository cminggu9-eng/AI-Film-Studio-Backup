---
type: director-integration-output-contract
status: complete-awaiting-user-review
version: 0.1
date: 2026-08-28
---

# Director Integration Output Contract V0.1

## Transport invariants

| Contract element | Exact rule |
| --- | --- |
| Mode | One of `PLAN`, `REVISE`, `DIAGNOSE`; this frozen path uses `PLAN`. |
| Primary State | One exact canonical Director Primary State; no translation, alias, collapse, or rename. |
| Flags / Handoffs | Director has no defined canonical flag/handoff token list in its Skill; integration requires the transport sentinel `ABSENT`. `ABSENT` is not a canonical creative-state token. |
| State evidence and locks | Existing State & Evidence envelope rules apply unchanged; locks and prohibitions are copied exactly. |
| Scene packages | Must be `ABSENT`; only Scene Writer may emit them. |

## Semantic-field identity and canonical headings

| Stable machine field ID | Canonical output heading token | Required order |
| --- | --- | --- |
| `directorial_intent` | `DIRECTORIAL INTENT` | 1 |
| `staging_blocking` | `STAGING / BLOCKING` | 2 |
| `audience_information` | `AUDIENCE INFORMATION` | 3 |
| `spatial_geography` | `SPATIAL GEOGRAPHY` | 4 |
| `camera_coverage_intent` | `CAMERA / COVERAGE INTENT` | 5 |
| `rhythm_transition_intent` | `RHYTHM / TRANSITION INTENT` | 6 |
| `production_burden` | `PRODUCTION BURDEN` | 7 |
| `handoffs_unresolved_issues` | `HANDOFFS / UNRESOLVED ISSUES` | 8 |

The stable IDs are integration identifiers. The heading tokens remain mandatory in this contract because the canonical Director Skill explicitly requires those exact headings in that exact order. The validator accepts no aliases, case-folding, spacing normalization, regex renaming, hidden tolerance, or LLM rewrite.

## Implementation

`runtime/_STAGING/_research/E2E_Targeted_Repair_05_Director_Output_Contract_Transport_Alignment_V0.1/implementation/director_integration_contract.py`

The Minimal E2E harness calls this deterministic gate only for Director after raw response and usage persistence. It reports structural failure rather than falsely labeling a heading problem as semantic failure.
