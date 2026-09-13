---
type: showrunner-integration-field-ownership-map
status: defined-and-offline-validated
version: 0.1
date: 2026-08-28
scope: showrunner-to-integration-only
---

# Showrunner｜Integration Field Ownership Map V0.1

## Sources read

- Canonical `01_SKILLS/01_Showrunner/SKILL.md`: Showrunner owns story, canon, development decisions, and downstream handoff contents; it does not write Scene Writer scene prose.
- Cross-Role Authority Map: Showrunner owns Story / Canon / major outcomes; Scene Writer owns how a scene plays.
- Interface Contract Map: the Showrunner-to-Scene Writer handoff is an assignment containing purpose, objective, conflict, required information, states, canon constraints, prohibitions, and acceptance checks. It is not a Scene Writer package.
- State & Evidence Envelope: adapters preserve source payload and are prohibited from inventing semantic values or changing canonical tokens.
- Immutable `E2E-RUN-02` Showrunner raw response, SHA-256 `c221a9762a3be151c6ab08fa5bdcd00b245a0d32c0f6034f3f641b5022fb5689`.

## Field classification

| Field | Ownership | Rule |
| --- | --- | --- |
| `primary_state_or_outcome` | A. Showrunner role-owned semantic/control field | Must be a supplied exact Showrunner STATUS token: `INFO`, `WARNING`, `BLOCKED`, or `PASS`. Missing or changed values fail. |
| `flags`, `handoffs` | A. Showrunner role-owned control fields | The source supplies literal `ABSENT`; it is preserved exactly. The adapter does not add, translate, or map a token. |
| `canon_assignment_locks`, `prohibited_changes` | A. Showrunner role-owned semantic fields | Must be non-empty supplied lists. A missing list remains a failure. |
| `required_outcome`, `unresolved_decisions` | A. Showrunner role-owned assignment / decision fields | Must be supplied by the role, including an explicit source `ABSENT` where applicable. The adapter does not infer an outcome or decision. |
| `state_evidence.relevant_prior_state`, `current_state`, `proposed_state`, `knowledge_timing`, `relationship_state`, `visual_state` | A. Showrunner role-owned semantic fields | All six exact dimensions must be supplied, non-null, and JSON-safe. No dimension may be created from prose. |
| `content` | A. Showrunner role-owned semantic deliverable | Must be supplied non-empty text and retain the Showrunner assignment / canon semantics. |
| `scene_packages` | B. Integration-owned E2E transport slot | Its semantic content can only be created by Scene Writer. At Showrunner-to-Scene Writer there is lawfully no package, so integration may record the slot as `ABSENT` only under the sentinel rule. |
| `canonical_mode` in State & Evidence Envelope | B. Integration-owned envelope field | Showrunner has no canonical Mode; the envelope carries literal `ABSENT`, without asking Provider to invent a mode. |
| `source_role`, record/version/timestamp, recipient/reason, authority source, evidence locator | B. Integration-owned envelope fields | Deterministic execution provenance only; never creative content. |
| literal `ABSENT` added to missing `scene_packages` | C. Transport absence sentinel | Means only “transport slot not populated at this boundary”; it is not a Showrunner canonical token or semantic decision. |

## Baseline finding

The Rerun 02 raw Showrunner response supplied every A field and parsed successfully. Its only missing field was B field `scene_packages`. The former generic validator incorrectly required the Provider to emit that integration-owned slot before validating the Showrunner role payload. This is an `EXECUTOR / TRANSPORT CONTRACT FAILURE`, not a Showrunner semantic failure.

## Reusable boundary principle

`TRANSPORT MAY REPRESENT ABSENCE; TRANSPORT MAY NOT INVENT ROLE SEMANTICS.`

This map changes no other role contract. A future role may use this principle only after an actual E2E failure establishes an equivalent ownership map.
