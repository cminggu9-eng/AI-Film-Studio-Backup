---
type: integration-phase-1-e2e-acceptance-criteria
status: defined-not-executed
version: 0.1
date: 2026-08-26
scope: future-minimal-e2e-validation
---

# AI Film Studio｜E2E Acceptance Criteria V0.1

## Execution status

All E2E-INT criteria are defined in Phase 1 and executed zero times. They are not a release claim, Human Acceptance, or authorization to begin Runtime.

| ID | Future acceptance criterion | Required evidence / fail condition |
| --- | --- | --- |
| E2E-INT-01 | The only creative input is the frozen one-line E2E-FIX-01 concept plus explicitly versioned, authorized downstream artifacts. | Fail if a pre-authored adaptation, hidden canonical fact, or untracked context is injected. |
| E2E-INT-02 | Showrunner remains sole owner of story/canon/major-outcome decisions. | Fail if a downstream role changes a locked story/canon fact instead of escalating. |
| E2E-INT-03 | Scene Writer keeps the frozen fact and character-knowledge locks, including the A-17 key, custody transfer, and reveal timing. | Fail on unsupported micro-fact addition, early knowledge, missing lock, or untraced state. |
| E2E-INT-04 | Scene Writer’s objective, resistance, dialogue action, turn, entry/exit, and outcome are present as scene-level evidence. | Fail if a scene cannot show how it plays or its state transition. |
| E2E-INT-05 | Director converts dramatic constraints into staging/audience/spatial intent without rewriting story or assuming Character & Acting authority. | Fail on authority takeover or loss of scene locks. |
| E2E-INT-06 | Character & Acting receives locked scene/knowledge and director constraints, then produces a playable interpretation without rewriting scene, canon, or staging. | Fail on a creative ownership breach or absent knowledge/timing evidence. |
| E2E-INT-07 | Art Director receives the correct story/scene/director/performance constraints and produces visual design intent without assuming camera or performance ownership. | Fail if visual work loses the prop, space, visual-state, or authority context. |
| E2E-INT-08 | Continuity receives versioned prior/current/proposed state and authority evidence from creative outputs. | Fail if Continuity must infer state, overwrite a decision, or lacks a usable evidence locator. |
| E2E-INT-09 | Across three to five scenes, the key’s identity, A-17 marking, custody, purpose, knowledge timing, relationship state, and clothing/visual state remain coherent or are explicitly authorized changes. | Fail on unclassified contradiction, loss of carryover, or unauthorized change. |
| E2E-INT-10 | A knowledge reveal remains visible only to characters authorized to know it at each point. | Fail on early disclosure, character-knowledge drift, or untracked transfer of knowledge. |
| E2E-INT-11 | The visual-state change and physical-performance implications reach Continuity in a source-attributed form. | Fail if Continuity receives text without state/evidence or a source version. |
| E2E-INT-12 | Every inter-role handoff preserves source role, source version, intended recipient, locks, canonical Mode/Primary State/Flag/Handoff tokens, unresolved decisions, and the failure route where relevant. | Fail on translated, collapsed, invented, or missing canonical control information. |
| E2E-INT-13 | Shared QA is horizontal and defaults to QA MODE; it cannot perform a creative rewrite. | Fail if QA changes story/canon/role decision or runs REWRITE MODE without explicit instruction and protection. |
| E2E-INT-14 | When target language is supplied, QA control text and deliverable use that language except exact canonical tokens. | Fail on unexplained language mismatch or translated canonical tokens. |
| E2E-INT-15 | A semantic safeguard other than the known unreliable Scene Writer verifier is present for locked facts and character knowledge. | Fail if that verifier is the sole gate or if the gate cannot produce attributable evidence. |
| E2E-INT-16 | Any role failure, ambiguity, external-production need, or missing context is attributed to a lawful owner and ends in a safe stop. | Fail on automatic retry, provider fallback, circular auto-invocation, or silent repair. |
| E2E-INT-17 | The E2E harness has a provider-free import/startup proof before any separate real execution authorization. | Fail if importing the harness can reach an executor/provider. |
| E2E-INT-18 | The integrated evidence bundle is reproducible from frozen input, explicit versions, and recorded handoffs. | Fail if the run cannot identify its inputs, versions, source output, QA result, or safe-stop reason. |

## Minimal pass condition for a later E2E run

A later run may be called a minimal E2E Runtime validation only if E2E-INT-01 through E2E-INT-18 all have attributable evidence and none fails. A blocking prerequisite from the Contract Compatibility Audit must be resolved or separately waived by the user before the run begins.

## Current result

Defined: 18 criteria.
Executed in Phase 1: 0.
Human Acceptance: not started.
