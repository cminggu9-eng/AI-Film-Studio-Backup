---
type: process-provenance-audit
status: complete-awaiting-user-review
version: 0.1
date: 2026-08-25
---

# AI Film Studio｜Nuwa Distillation Provenance Audit V0.1

## Standard and scope

This audit asks one narrow question: is there retained evidence of an **actual** `huashu-nuwa` invocation for the historical formal source-distillation step? Reading the Skill, naming the Skill in a taskbook, preparing material for a future invocation, or imitating its format is not proof. The only statuses used below are `CONFIRMED_INVOKED`, `CONFIRMED_NOT_INVOKED`, and `INSUFFICIENT_EVIDENCE`.

No historical capability evidence is retroactively invalidated. A process-provenance gap is not an evidence-quality finding.

## Findings

| Role / phase / record | Status | Audit basis | Current role status | Required follow-up |
| --- | --- | --- | --- | --- |
| Showrunner — Craig Mazin single distillation | `INSUFFICIENT_EVIDENCE` | Staging research and Vault output exist, but no invocation receipt, execution reference, or retained invocation output was found. | Published / frozen downstream assets remain unchanged. | Preserve current evidence; re-distill only in the unified hardening program. |
| Showrunner — Vince Gilligan single distillation | `INSUFFICIENT_EVIDENCE` | `01-primary-interviews.md` says it is for a later Nuwa distillation; this is positive evidence of preparation, not execution. No receipt found. | Same. | Same. |
| Showrunner — Shonda Rhimes single distillation | `INSUFFICIENT_EVIDENCE` | No actual invocation receipt or execution reference found. | Same. | Same. |
| Showrunner — Tony Gilroy single distillation | `INSUFFICIENT_EVIDENCE` | No actual invocation receipt or execution reference found. | Same. | Same. |
| Showrunner — David Simon single distillation | `CONFIRMED_NOT_INVOKED` | The evidence audit states that formal distillation still had to pass through a future `huashu-nuwa` first pass; retained record therefore documents that the existing research was pre-invocation. | Published / frozen downstream assets remain unchanged. | Process deviation; preserve source evidence and re-distill in unified hardening. |
| Showrunner — five-person cross-distillation | `INSUFFICIENT_EVIDENCE` | Taskbook and staging README say the work should use the Nuwa process, but no invocation receipt/execution output proves it occurred. | Published cross-distillation and downstream assets remain unchanged. | Record provenance gap; no retrofit. |
| Shared Language & Voice QA — Ye Shengtao | `CONFIRMED_INVOKED` | `00-nuwa-invocation-receipt.md` records readable Skill path, full read, extraction framework, SHA, timestamp, invocation status and method route. | Published / frozen. | No re-distillation required by this audit. |
| Shared Language & Voice QA — Wang Zengqi | `CONFIRMED_INVOKED` | Retained source-specific `00-nuwa-invocation-receipt.md`. | Published / frozen. | None. |
| Shared Language & Voice QA — Lao She | `CONFIRMED_INVOKED` | Retained source-specific `00-nuwa-invocation-receipt.md`. | Published / frozen. | None. |
| Shared Language & Voice QA — Yu Guangzhong | `CONFIRMED_INVOKED` | Retained source-specific `00-nuwa-invocation-receipt.md`. | Published / frozen. | None. |
| Shared Language & Voice QA — Liu Zhenyun | `CONFIRMED_INVOKED` | Retained source-specific `00-nuwa-invocation-receipt.md`. | Published / frozen. | None. |
| Shared Language & Voice QA — five-person cross-distillation | `CONFIRMED_INVOKED` | Retained cross-distillation receipt identifies `huashu-nuwa`, its SHA, input scope, method route, and staging-only control. Historical taskbook claim is therefore verified by actual process evidence. | Published / frozen. | None. |
| Scene Writer — Phase 2: BBC Writersroom / Academy Nicholl / Writers Guild Foundation | `CONFIRMED_NOT_INVOKED` | The completed task record and evidence manifest identify direct source-body distillations and Codex auditing, but contain no Nuwa invocation artifact; the Phase 2 record does not claim a Nuwa run. | Production Skill published / frozen; runtime work remains separately staged. | `PROCESS DEVIATION`; preserve evidence, re-distill only in unified hardening. |
| Scene Writer — Phase 2B: Scriptnotes / Film Independent | `CONFIRMED_NOT_INVOKED` | The completed targeted-gap task record identifies Codex source-distillation work; no Nuwa receipt/execution output exists. | Same. | `PROCESS DEVIATION`; preserve evidence, re-distill only in unified hardening. |
| Director — Phase 2: DGA Nichols/Stone, Vince Gilligan, Lesli Linka Glatter, Clint Eastwood; DR-D01–DR-D16 | `CONFIRMED_NOT_INVOKED` | The Phase 2 task record explicitly describes independent source distillations and `DR-D01–DR-D16`; the evidence manifest has source traces, but no Nuwa receipt or execution reference. | Production Skill published / frozen; no runtime. | `PROCESS DEVIATION`; do not invalidate evidence; re-distill only in unified hardening. |

## Explicit distinction

- “Must follow `huashu-nuwa`” in a taskbook is a requirement, not proof of use.
- “For later Nuwa distillation” is preparation, not use.
- Shared QA is the sole audited historical track with retained, source-specific actual-invocation receipts for both the five singles and the cross-distillation.

## Integrity conclusion

Frozen Skills, Capability Models, runtime artifacts, published archives, and historical source evidence were not edited. Every non-confirmed record is traceable above and is queued only for `AI FILM STUDIO INTEGRATION VALIDATION / HARDENING`.
