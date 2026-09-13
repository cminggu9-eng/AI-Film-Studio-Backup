---
type: integration-contract-repair-semantic-safeguard
status: defined-and-offline-validated
version: 0.1
date: 2026-08-26
scope: integration-owned-non-rewriting-safeguard
---

# AI Film Studio｜Semantic Safeguard V0.1

## Authority and output boundary

This is an Integration-owned safeguard, not a Scene Writer semantic authority and not a replacement for any canonical role token. It never rewrites creative output. It returns only these Integration-level labels:

PASS; FLAG; BLOCK; HANDOFF.

Those labels do not rename, override, or translate a role’s canonical Mode, Primary State, Flags, or Handoffs.

## Protected objects

The safeguard consumes the State & Evidence Envelope and run-local Ledger to protect:

1. Canon / Assignment Locks.
2. Unsupported new facts.
3. Character knowledge timing.
4. Required prop / state.
5. Authorized state change.

All material findings retain an authority source and evidence locator. Missing authority or evidence is not repaired.

## Two-layer architecture

| Layer | Scope | This repair’s behavior |
| --- | --- | --- |
| Layer A: Deterministic Evidence / Contract Gate | Required fields, exact locks, source version, known state, knowledge holder/timing, explicit required facts, authorized transitions, and evidence attribution. | Implemented and tested offline. It can PASS, FLAG, BLOCK, or prepare a HANDOFF. |
| Layer B: Independent Semantic Review Contract | Unsupported micro-fact, semantic contradiction, early implied knowledge, and meaning-level lock violation that cannot be decided from structure alone. | Implemented as a provider-free review contract. It produces an attributable HANDOFF package only. Any actual model/human semantic review requires separate execution authorization. |

## Legacy verifier rule

Scene Writer’s historical semantic verifier is a SUPPLEMENTAL SIGNAL ONLY. A legacy-verifier PASS by itself produces BLOCK from this safeguard; it cannot be the sole acceptance gate.

## Non-rewrite rule

The safeguard hashes supplied creative output for evidence but omits it from its result. It may flag or block a result, never edit, improve, regenerate, or silently repair it.

## Implementation location

AI_Film_Studio_Automation_V0.1/runtime/_STAGING/_research/Integration_Contract_Repair_V0.1/implementation/integration_contract/semantic_safeguard.py

No Provider call is made by this implementation.
