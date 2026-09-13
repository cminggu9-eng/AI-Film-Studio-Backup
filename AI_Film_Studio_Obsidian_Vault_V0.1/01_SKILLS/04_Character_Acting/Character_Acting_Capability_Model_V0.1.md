---
type: capability-model
role: character-and-acting
status: complete-awaiting-user-review
version: 0.1
---

# Character & Acting Capability Model V0.1

## Core identity

Character & Acting transforms lawful character facts, knowledge state, scene circumstances, locked Scene Writer objective/resistance/turn/outcome, interaction, and supplied Director constraints into a **playable performance interpretation**. Its question is: how does this character live, receive, act, change, and respond in this dramatic moment?

It does not decide what the story becomes, what a character's arc/facts are, how the scene is staged or shot, or how the dialogue should be rewritten.

## Promoted rules

CA-DR01–CA-DR10 are promoted without semantic mutation; their final classes remain Hard `3`, Default `3`, Conditional `4`, Optional `0`. The authoritative promotion table is `Character_Acting_Rule_Promotion_Audit_V0.1.md`.

## Modes

| Mode | Purpose | Allowed result | No-change behavior |
| --- | --- | --- | --- |
| `INTERPRET` | Produce a lawful scene-local performance interpretation. | Playable intention, reception, response, expression conditions, state, handoff. | Return `NO_PERFORMANCE_CHANGE` when existing interpretation remains sufficient. |
| `REVISE` | Adjust an existing interpretation after lawful new scene/performance information. | Bounded change with preserved fact/text/authority locks. | Do not invent missing history, replace Director choice, or rewrite text. |
| `DIAGNOSE` | Identify why a performance request is unplayable, mechanical, contradictory, or out of scope. | Constraint finding, anti-mechanical finding, or handoff. | Do not silently repair upstream material. |

## Primary states

Exactly one state is emitted for an evaluated request:

`PERFORMANCE_INTERPRETATION_READY` · `PERFORMANCE_INTERPRETATION_REVISED` · `NO_PERFORMANCE_CHANGE` · `CONTEXT_REQUIRED` · `UPSTREAM_DECISION_REQUIRED` · `OUT_OF_SCOPE`.

These states are capability outcomes only, not Runtime tokens or a production output schema.

## Non-negotiable limits

- C10 is a known bounded gap: `NO SAFE FORMAL MICRO-EXPRESSION SYSTEM`.
- C19 is `NO EVIDENCE`; current-scene state may be handed off, but no continuity methodology is claimed.
- C21 is `DEFERRED / FUTURE INTERFACE BOUNDARY`; no animation, motion, pose, lip-sync, ComfyUI, or video-model system exists.
- Provider calls, Nuwa calls, Runtime, Executor, Production Skill, real performance generation: `0`.
