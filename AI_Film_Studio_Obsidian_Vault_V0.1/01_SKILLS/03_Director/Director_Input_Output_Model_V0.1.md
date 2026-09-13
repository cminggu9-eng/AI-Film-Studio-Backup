---
type: input-output-model
role: director
phase: 4-capability-model
status: complete-awaiting-user-review
version: 0.1
---

# Director Input / Output Model V0.1

## Input categories

| Category | Inputs | Sufficiency rule |
|---|---|---|
| REQUIRED | Scene identity; Scene Writer deliverable/scene text; Scene Function; locked outcome; Canon/Showrunner locks; participants; any already locked location/spatial facts | Missing information blocks only when it prevents a safe scene-level Director decision or creates a lock conflict. |
| USEFUL | Prior scene state; next-scene relationship; approved character constraints; production notes; authorized visual references; already supplied Art / Acting constraints | Improve precision; absence alone does not block work. |
| OPTIONAL | Downstream requests; a later lawfully supplied external-production constraint | May inform bounded handoff; absence never blocks current Director work. |

## Scene Intent representation

`Scene Intent` records, without rewriting:

- dramatic function;
- audience information change;
- relationship / power change;
- emotional or narrative emphasis;
- required event; and
- locked outcome.

## Context sufficiency

| State | Examples |
|---|---|
| Sufficient | Required assignment and locks are known; useful production/visual detail may be absent. |
| `NEEDS_CONTEXT` | Geography is fundamentally undefined and a decision would alter Canon; locked location facts conflict; required staging depends on an unresolved upstream fact. |
| `UPSTREAM_DECISION_REQUIRED` | Showrunner / Scene Writer outcome conflicts, Canon is ambiguous, or Scene Function is not established. |

The Director must not request context merely because a specific lens, palette, acting detail, technical camera detail, or downstream preference is absent.

## Capability-level output model

| Output component | Required content | Excluded content |
|---|---|---|
| A. Directorial Intent | Scene-purpose account and protected locks | Story rewrite |
| B. Staging / Blocking Plan | Relevant positions, paths, relational distance, playable space | Acting technique / psychology system |
| C. Audience Information Plan | Notice/defer/reveal/conceal timing | Editorial information system |
| D. Spatial Geography | Current-scene relation, access, orientation, purposeful disorientation if justified | Cross-scene continuity database |
| E. Camera / Coverage Intent | Audience reason for position, movement, coverage, and alternatives | Lens, rig, lighting, sensor, or technical sheet |
| F. Rhythm / Transition Intent | Scene-scale, duration/action/attention condition, scene-to-scene relationship intent | Full edit/post methodology |
| G. Production Burden | Required versus desirable burden and risk to required material | Final budget/schedule/logistics decision |
| H. Handoffs / Unresolved Issues | Upstream conflict or bounded downstream specialist need | Silent role takeover |

This output is not a shooting script, final technical camera sheet, Production Skill format, or runtime schema.
