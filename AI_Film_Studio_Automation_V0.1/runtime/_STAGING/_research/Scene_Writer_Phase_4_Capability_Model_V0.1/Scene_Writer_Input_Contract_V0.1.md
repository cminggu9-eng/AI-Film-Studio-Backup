---
type: input-contract-draft
status: passed-awaiting-human-review
version: 0.1
role: Scene Writer
runtime_implementation: none
---

# Scene Writer Input Contract V0.1

> This is a capability-level contract. Field labels are not an API schema and do not make every field permanently mandatory.

|Field|Purpose|Context class|Requirement rule|
|---|---|---|---|
|project_id / episode_id|Locates relevant Canon and story scope.|Conditional required.|Required where multiple scopes could alter a lock; otherwise an unambiguous project reference suffices.|
|scene_id / scene request|Identifies the scene or requested intervention.|Required.|A create/revise/diagnose request must name or unambiguously describe its scene target.|
|mode|Sets operation: `CREATE`, `REVISE`, or `DIAGNOSE`.|Required or safely inferred.|Infer only where request is unambiguous; otherwise ask once.|
|scene purpose / repair target|Defines why the scene exists or what is being assessed/repaired.|Required.|Missing purpose blocks safe construction or revision.|
|Canon constraints / Showrunner locks|Protects facts, causality, required events/information/outcome, episode function, and ending direction.|Conditional required.|Required when such locks exist or scope makes them relevant; explicit “none supplied” is not permission to invent Canon.|
|participants / character context|Supports intention, resistance, dialogue and action.|Conditional required.|Required when absence changes legal construction; otherwise may be useful.|
|required event / information / outcome|States any locked result the scene must carry.|Conditional required.|Required only if locked or necessary to judge requested scene function; no invented substitute when absent.|
|previous-state context|Makes entry, action, causality and relation legible.|Conditional required.|Required only when it materially affects the present scene.|
|desired post-scene state|Specifies a locked changed condition, if any.|Conditional required.|Required only when locked/necessary to assess target outcome.|
|production constraints|Surfaces confirmed production needs or requests for assessment.|Optional / useful.|May create a flag/handoff, never automatic compression.|
|form / presentation request|Clarifies spec-style versus authorised production-script form.|Useful.|Only blocks if format authority changes what can be written.|
|language / voice QA request|Separates dramatic construction from language-level checking.|Optional.|Produces handoff eligibility only; no Shared QA execution here.|

## Intake Result

The intake emits only a compact assignment-lock summary, required missing items, safe assumptions (if any), mode, and relevant routing flags. It does not require or preserve private chain-of-thought.

