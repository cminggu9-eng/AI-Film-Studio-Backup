---
type: integration-contract-repair-state-evidence-envelope
status: defined-and-offline-validated
version: 0.1
date: 2026-08-26
scope: minimal-e2e-run-local-transport
---

# AI Film Studio｜State & Evidence Envelope V0.1

## Purpose

This is the minimum lossless transport envelope for a future minimal E2E run. It is role-neutral and provider-free. It carries supplied evidence between roles; it does not create a role, change a role’s authority, translate canonical tokens, derive missing information, or make a continuity decision.

## Exact field contract

Every envelope must contain exactly these fields. The implementation rejects missing and unknown fields rather than filling defaults.

| Group | Exact fields |
| --- | --- |
| Source identity | source_role; source_record_id; version; timestamp |
| Recipient purpose | intended_recipient; handoff_reason |
| Authority constraints | canon_assignment_locks; prohibited_changes |
| Canonical controls | canonical_mode; primary_state_or_outcome; flags; handoffs |
| Decision state | required_outcome; unresolved_decisions |
| State evidence | relevant_prior_state; current_state; proposed_state; knowledge_timing; relationship_state; visual_state |
| Attribution | authority_source; evidence_locator |

The following fields are always supplied, non-empty text: source_role, source_record_id, version, timestamp, intended_recipient, handoff_reason, authority_source, and evidence_locator.

## ABSENT rule

ABSENT is the literal integration sentinel for an upstream value that was not supplied. It is valid only for optional contract fields. An Adapter must preserve it exactly.

- It must not replace ABSENT with null, an empty list, an empty object, an inferred value, or a guessed state.
- A role-local canonical Mode that does not exist is carried as canonical_mode = ABSENT.
- A missing Primary State / Outcome, Flags, Handoffs, state dimension, or optional decision remains ABSENT rather than being normalized.
- An envelope missing one of its exact fields is rejected; the receiver does not add the field.

## Canonical token rule

canonical_mode, primary_state_or_outcome, flags, and handoffs are transported exactly as emitted by the source role. The Envelope provides no aliasing, translation, merging, case normalization, or cross-role token mapping.

## Authority and non-rewrite rule

The Envelope records an authority source and evidence locator. It does not judge their truth, alter the source artifact, decide an unresolved question, or repair a role result. A downstream recipient must either use the supplied evidence or return its own lawful context, handoff, or safe-stop outcome.

## Implementation location

Staging-only implementation:

AI_Film_Studio_Automation_V0.1/runtime/_STAGING/_research/Integration_Contract_Repair_V0.1/implementation/integration_contract/state_evidence.py

No canonical SKILL.md or Production Lock is part of this implementation.
