# Art Director Prompt / Schema / Validator Identity Report V0.1

Date: 2026-08-31  
Result: PASS

One shared `ART_DIRECTOR_MACHINE_FIELD_MANIFEST` now drives prompt instructions, provider-facing schema, and local validation.

| Field | Prompt | Provider schema | Validator |
|---|---|---|---|
| `primary_state_or_outcome` | required exact canonical enum | required exact enum | same enum, case-sensitive |
| `flags` | required exact `ABSENT` | required const | exact `ABSENT` |
| `handoffs` | required exact `ABSENT` | required const | exact `ABSENT` |
| `canon_assignment_locks` | required string array | required string array | same |
| `prohibited_changes` | required string array | required string array | same |
| `required_outcome` | required string | required string | same |
| `unresolved_decisions` | required array or `ABSENT`; empty allowed | required `anyOf` | same |
| `state_evidence` | required closed six-field object | required closed object | same |
| `content` | required non-empty string; no heading template | required string | non-empty only |
| `scene_packages` | required exact `ABSENT` | required const | exact `ABSENT` |

Conditional semantics are also identical: Production feasibility, unresolved issues, and current visual state are supplied only when authoritative evidence makes them relevant. No participant imposes an additional prose keyword or display-heading requirement.

