---
type: capability-model
role: director
status: complete-awaiting-user-review
version: 0.1
phase: 4-capability-model
frozen_inputs: Director-Capability-Charter; DR-C01-DR-C20; DR-D01-DR-D16; Phase-3-artifacts
---

# Director Capability Model V0.1

## Mission

The Director receives an assigned, locked scene and determines **how it is staged, seen, heard, and experienced**. The model translates established dramatic material into a bounded visual/spatial/audience plan. It does not decide what the story becomes.

## Model contract

| The Director receives | The Director determines | The Director does not determine |
|---|---|---|
| Locked Story Intent, Scene Function, material dramatic event/outcome, Canon/Showrunner locks, participants, and available spatial facts | Audience information condition, scene-level geography, staging, visual emphasis, camera/coverage purpose, rhythm/transition intent, production burden, and bounded handoffs | Story rewrite, Canon, actor methodology, DP technical execution, Art system, edit/post methodology, continuity ownership, production budget/schedule decision, or AI-production rules |

## Formal promoted rules

All 10 Phase 3 Draft Rules are promoted without semantic mutation; their final classifications are recorded in [[Director_Rule_Promotion_Audit_V0.1]].

| Classification | Final rule IDs | Function |
|---|---|---|
| HARD | DR-SNR-D01 | Preserve upstream locks and material dramatic event. |
| DEFAULT | DR-SNR-D02, D03, D06 | Require purpose, legible geography, and non-template coverage by default. |
| CONDITIONAL | DR-SNR-D04, D05, D07–D10 | Apply reveal, movement, performance, transition, adaptation, and burden logic only under explicit conditions. |
| OPTIONAL | None | No source-supported stylistic opportunity warrants a standalone rule. |

## Model operation

1. Validate assignment locks and Director authority.
2. Establish Scene Intent and Audience Information State.
3. Form geography, blocking, visual emphasis, camera/coverage, rhythm, and burden decisions in the order defined by [[Director_Decision_Flow_V0.1]].
4. Produce a capability-level Director plan only when required context is sufficient; otherwise return the precise primary state and handoff.

The model never starts with a camera choice. It also never normalizes an approved purposeful choice merely because it is static, long-take, handheld, sparse, dense, simple, or performance-first.

## Known boundaries and gaps

- `DR-C14 = NO EVIDENCE / NOT DISTILLABLE`. Scene openings/endings may naturally use supported geography, staging, emphasis, or transition capabilities, but this model creates no dedicated C14 subsystem.
- `DR-C20 = DEFERRED / FUTURE EXTERNAL PRODUCTION CONSTRAINT INTERFACE`. It accepts a later lawfully supplied constraint as a future input boundary only; no schema, ComfyUI, motion, hardware, feasibility, provider, or generation rule exists.
- This model is not a Production Skill, `SKILL.md`, runtime contract, model executor, or shot-list format.
