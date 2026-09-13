---
type: integration-phase-1-known-issues-register
status: open-deferred
version: 0.1
date: 2026-08-26
scope: registration-only
---

# AI Film Studio｜Integration Known Issues Register V0.1

## Registration rule

This register consolidates already recorded debts and interface findings. It does not change their original severity, reopen accepted artifacts, or authorize a repair. “Blocking” means blocking a future real minimal E2E Runtime validation, not blocking this static Phase 1 review.

| ID | Source / issue | Owner | Severity | Future impact | Disposition |
| --- | --- | --- | --- | --- | --- |
| INT-ISS-01 | SW-DH01: unsupported micro-fact additions in Scene Writer samples. | Scene Writer | High | Can introduce unassigned facts into the chain. | Blocking for semantic fixture execution until a fact-lock gate is demonstrated. |
| INT-ISS-02 | SW-DH02: character knowledge timing drift. | Scene Writer | High | Can disclose a fact before the authorized reveal point. | Blocking for a fixture that contains a knowledge reveal. |
| INT-ISS-03 | SW-DH03: non-CREATE states are not reliable. | Scene Writer | High | Revision/diagnostic paths cannot be presumed valid. | Revisit before any non-CREATE E2E path; Phase 2 must not use it without a separate gate. |
| INT-ISS-04 | SW-DH04: semantic verifier false negatives/non-JSON behavior. | Scene Writer / Integration owner | Critical | The verifier cannot be the sole integrated semantic acceptance gate. | BLOCKING. Select a controlled semantic-gate design before real E2E execution. |
| INT-ISS-05 | SW-DH05: legacy smoke-runner import can trigger a provider. | Scene Writer / Runtime owner | High | Violates a no-provider dry control and can cause unintended external execution. | BLOCKING before any real integration test; prove a provider-free import path first. |
| INT-ISS-06 | Scene Writer Production Lock and Development Checkpoint disagree on executor binding state. | Scene Writer release owner | High | A planner cannot safely infer real-execution eligibility. | BLOCKING for executor selection; resolve record precedence before Phase 2. |
| INT-ISS-07 | Director, Character & Acting, Art Director, and Continuity SKILL frontmatter remain staging-oriented while checkpoints/locks are PUBLISHED / FROZEN. | Role release owners | Medium | Automated discovery/publish tooling may misclassify lifecycle state. | Non-blocking for static mapping; revisit before automated registration or runtime routing. |
| INT-ISS-08 | No common cross-role state-and-evidence handoff or persistent state retrieval contract. | Integration architecture owner | High | Continuity cannot compare a reliable system state without inference. | BLOCKING for multi-scene E2E validation. |
| INT-ISS-09 | Director DH-DIR-01 / DH-DIR-02: entry/exit evidence and external production constraints remain deferred. | Director | High | Production feasibility and entry/exit expectations must be bounded. | Revisit when the fixture demands those decisions; do not infer a solution. |
| INT-ISS-10 | Character & Acting CA-C10, CA-C19, CA-C21: no safe formal microexpression method, current-scene structural limit, future interface deferred. | Character & Acting | Medium | Performance packet must remain observable/playable and current-scene bounded. | Non-blocking for the fixture if no microexpression claim is required; revisit for broader scope. |
| INT-ISS-11 | Art Director deferred capability limits: material/design evidence, research, and production-feasibility boundaries are partial or deferred. | Art Director | Medium | Art output must declare unresolved research/feasibility instead of inventing it. | Non-blocking for a minimal design-intent fixture; revisit for implementation-facing scope. |
| INT-ISS-12 | Continuity DH-CT01 through DH-CT11: partial checks, retcon boundary, state database/storage/retrieval, Runtime/executor/semantic/cross-role/human validation deferred. | Continuity / Integration architecture owner | High | Comparison can occur only on explicitly supplied evidence; persistence is absent. | BLOCKING for a multi-scene runtime chain until state transport/retrieval is controlled. |
| INT-ISS-13 | Shared QA Hub retains KL-01 and KL-02 as known limitations without a detailed definition in the Hub reviewed here. | Shared QA owner | Not defined in Hub | An integration planner must not invent their scope. | Non-blocking; retain the references and request source detail if they affect a selected QA gate. |
| INT-ISS-14 | Historical Nuwa process-provenance gaps: Showrunner records are INSUFFICIENT_EVIDENCE or CONFIRMED_NOT_INVOKED; Scene Writer and Director formal distillations are CONFIRMED_NOT_INVOKED. | Integration governance / source owners | Historical process debt | Affects successor-distillation governance, not current frozen capability evidence. | Non-blocking for Phase 1. Preserve; address only under authorized unified hardening. |
| INT-ISS-15 | Out-of-core ownership: technical cinematography, physical production approval, editorial execution, and persistent state storage are not owned by the seven-role core. | Integration architecture / future external owner | High when invoked | A role may otherwise silently assume authority. | Safe-stop and label external owner whenever the fixture reaches one of these boundaries. |
| INT-ISS-16 | Canonical tokens are role-specific and there is no implemented token namespace transport. | Integration architecture owner | Medium | A generic orchestrator could translate or collapse source states. | Revisit before automated routing; Phase 2 must preserve exact source tokens. |

## Historical provenance interpretation

The Nuwa provenance entries are governance findings only. The formal audits explicitly preserve frozen Skills, source evidence, capability models, and archives. This register does not retrospectively invalidate their capability claims and does not initiate any new distillation.

## Phase 1 owner boundary

No issue is repaired in this phase. Any action against a blocking item requires a distinct authorization and a new bounded task.
