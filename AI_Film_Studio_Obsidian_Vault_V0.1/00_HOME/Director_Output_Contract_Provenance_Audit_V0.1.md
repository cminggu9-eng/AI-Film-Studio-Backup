---
type: director-output-contract-provenance-audit
status: complete-awaiting-user-review
version: 0.1
date: 2026-08-28
---

# Director Output Contract Provenance Audit V0.1

## Result

The exact Director headings are canonical output-contract tokens, not arbitrary integration display labels. The Rerun 03 rejection additionally used a separate historical runner hardcode which disagreed with the canonical form and omitted two canonical headings.

| Source | Evidence | Authority |
| --- | --- | --- |
| A. Canonical Director contract | `01_SKILLS/03_Director/director/SKILL.md`, Output section | Authoritative. It requires eight exact headings **in this order**: `DIRECTORIAL INTENT`; `STAGING / BLOCKING`; `AUDIENCE INFORMATION`; `SPATIAL GEOGRAPHY`; `CAMERA / COVERAGE INTENT`; `RHYTHM / TRANSITION INTENT`; `PRODUCTION BURDEN`; `HANDOFFS / UNRESOLVED ISSUES`. |
| A. Canonical modes and states | Same Skill | Modes: `PLAN`, `REVISE`, `DIAGNOSE`. Primary States: `DIRECTION_PLAN_PRODUCED`, `DIRECTION_PLAN_REVISED`, `NO_MATERIAL_DIRECTION_CHANGE`, `NEEDS_CONTEXT`, `UPSTREAM_DECISION_REQUIRED`, `OUT_OF_SCOPE_HANDOFF`. |
| Supporting semantic sources | Director Capability Model and published contract | Confirm the eight Director responsibility areas; they do not create an independent runtime heading schema. |
| Interface map | `00_HOME/AI_Film_Studio_Interface_Contract_Map_V0.1.md` | Names Director semantic responsibilities but explicitly does not define a runtime schema. |
| E2E acceptance | E2E acceptance criteria, `E2E-INT-05` | Evaluates Director role behavior; it does not authorize alternate heading aliases. |
| B/D. Historical integration parser | `run_minimal_e2e.py` before Repair 05 | Required title-case labels such as `Directorial Intent` and `Staging/Blocking`; it omitted `CAMERA / COVERAGE INTENT` and `HANDOFFS / UNRESOLVED ISSUES`, did not enforce canonical order, and classified absence as semantic failure. |
| Recorded Rerun 03 response | `.../E2E-RUN-03/artifacts/director_provider_response.json` | Contains all eight canonical heading tokens and substantive content, but emits `SPATIAL GEOGRAPHY` before `AUDIENCE INFORMATION`. |

## Decision

Repair 05 replaces the historical generic heading-membership branch for Director with a source-driven integration validator. It preserves stable machine identities (`directorial_intent`, `staging_blocking`, and the other six IDs) separately from their canonical heading tokens, performs no normalization or auto-repair, and validates exact state tokens, `ABSENT` transport values, heading-line presence, and canonical order.

No strict-function transport was added. The provenance audit found that the canonical Skill itself explicitly owns the exact output headings and order; a second provider schema would not replace that source. The existing provider-neutral JSON object transport, raw-first persistence, and deterministic local contract gate are sufficient for this limited repair.

## Integrity

Canonical Director Skill hash remains `807D5B398A247A69C3F54FB58F256E8E87AE3B245540071A8B3F6832B49A7781`. Canonical Skill Mutation, Capability Model Mutation, and Semantic Mutation are all `0`.
