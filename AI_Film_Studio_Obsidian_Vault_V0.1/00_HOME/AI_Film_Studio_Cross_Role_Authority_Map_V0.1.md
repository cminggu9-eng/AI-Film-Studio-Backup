---
type: integration-phase-1-authority-map
status: frozen-for-phase-1-review
version: 0.1
date: 2026-08-26
scope: authority-mapping-only
---

# AI Film Studio｜Cross-Role Authority Map V0.1

## Authority principle

Each role can decide only in its own declared authority. A downstream role may identify a conflict, insufficiency, or production burden, but must route the decision to the lawful owner. No recipient may silently repair an upstream decision.

| Role | Sole / primary authority | May receive | Must not take over | Lawful escalation |
| --- | --- | --- | --- | --- |
| Showrunner | Story, canon, major outcomes, story-level character and relationship state, and final user-facing story authority. | User concept, approved canon, upstream decision requests, continuity contradiction flags. | Scene prose execution, staging, performance method, visual design, continuity certification, language rewrite. | User for final authority; receives bounded upstream decisions from downstream roles. |
| Scene Writer | How an authorized scene plays: objective, resistance, turn, entry/exit, scene-level dramatic action, and safe scene handoff. | Showrunner assignment/canon locks, current state, required outcome, constraints. | Story/canon alteration, major outcome change, director staging, acting method, visual design, continuity certification. | Showrunner for upstream story/canon; Director, Character & Acting, Shared QA, or production review only through declared flags. |
| Director | Staging, blocking, spatial geography, audience information, visual/auditory execution intent, coverage intent, rhythm, and production burden. | Approved scene content, canon/relationship constraints, known production constraints. | Dialogue/scene story rewrite, character performance ownership, art design ownership, technical department execution, continuity certification. | Showrunner or Scene Writer for dramatic changes; Character & Acting for performance; Art Director for design; production owner for external feasibility. |
| Character & Acting | Playable performance interpretation: character knowledge, objective, partner action/reception, body, voice, timing, and behavioral consequence. | Character facts/knowledge, locked scene content, relationship state, director constraints, physical environment/props. | Story/canon rewrite, dialogue rewrite, staging/camera ownership, art design, continuity certification. | Scene Writer / Showrunner for knowledge or scene meaning; Director for staging; Art Director for physical conditions. |
| Art Director | Visual world, design intent, space/material/prop conditions, visual-state expression, and art-design handoff. | Story/world requirements, scene need, character facts, director visual/spatial intent, physical-performance implications. | Story/canon change, camera/coverage, performance method, continuity certification, production authorization. | Showrunner for world/canon; Director for staging intent; Character & Acting for physical-performance conflict; production owner for feasibility. |
| Continuity | Observe, compare, classify, flag, and route cross-scene state/consistency issues. | Versioned current/prior scene state, authorized changes, supporting evidence, all role outputs that alter state. | Editing or certifying a new canon, choosing a fix, rewriting dialogue/design/performance/staging. | Lawful owner of the contradicted decision; returns for recheck after a new version is supplied. |
| Shared QA | Horizontal language/voice assessment; language-only rewrite only when explicitly requested with protection/lock requirements. | Original textual output; optional context, role, locks, target language, and explicit rewrite instruction. | Story/canon decisions, scene rewrite by default, authority reassignment, silent semantic correction. | Original owning role for revision; user/upstream owner where context is insufficient. |

## Required production chain

USER CONCEPT -> SHOWRUNNER -> SCENE WRITER -> DIRECTOR -> CHARACTER & ACTING -> ART DIRECTOR -> CONTINUITY

Shared QA is horizontal. It may be applied after a textual output at an explicitly selected quality gate; it is not the owner of the production chain and does not replace the originating role.

## Boundary and overlap audit

| Boundary | Finding | Owner rule | Status |
| --- | --- | --- | --- |
| Showrunner / Scene Writer | Story outcome versus how the scene plays is separable when the Showrunner assignment locks purpose, required information, state, and prohibitions. | Showrunner decides what must be true; Scene Writer decides lawful scene execution. | Clear, adapter needed for packaging. |
| Scene Writer / Director | Scene action can be misread as staging instruction. | Scene Writer hands over dramatic function and locks; Director chooses staging. | Clear, adapter needed for bounded director brief. |
| Director / Character & Acting | Blocking can constrain performance but does not define the performance method. | Director supplies spatial/staging constraints; Character & Acting produces playable behavior. | Clear, adapter needed. |
| Director / Art Director | Visual execution intent can overlap world/design execution. | Director owns audience/spatial intent; Art Director owns design response and visual world. | Clear, joint packet needed. |
| All creative roles / Continuity | Every role can change a state, while Continuity only checks it. | Originating owner must declare authorized state change; Continuity compares and routes. | Contract gap: no common state packet. |
| Any textual role / Shared QA | QA output can look like a rewrite of role content. | QA is non-rewriting by default; explicit rewrite is language-only and protected. | Clear, adapter needed for context/locks. |

## Circular-handoff audit

Allowed loops are review loops, not automatic re-execution:

1. A downstream request concerning story/canon returns to Showrunner; a new, versioned assignment is then supplied downstream.
2. A Continuity flag routes to the lawful originator; Continuity only rechecks an explicitly revised version.
3. Shared QA routes a language issue to the original owner, or performs only an explicitly locked language rewrite; an optional QA recheck receives the new version.

No role may invoke an upstream role automatically, retry a provider, or resume a chain merely because a flag exists.

## Missing-owner audit

| Concern | Owner status | Phase 1 conclusion |
| --- | --- | --- |
| Story/canon decision | Showrunner / user final authority | Owned. |
| Scene execution | Scene Writer | Owned. |
| Staging and audience information | Director | Owned. |
| Performance interpretation | Character & Acting | Owned. |
| Visual design intent | Art Director | Owned. |
| Cross-scene comparison and routing | Continuity | Owned, but not a state database owner. |
| Language/voice QA | Shared QA | Owned within QA limits. |
| Technical cinematography, physical production approval, editorial execution, persistent state storage | Explicitly out of the seven-role core | Not silently assigned. A Phase 2 test must safe-stop and label the external owner when these are required. |

No canonical authority boundary was changed by this map.
