---
type: context-sufficiency-model
status: passed-awaiting-human-review
version: 0.1
role: Scene Writer
anti_context_hunger: true
---

# Scene Writer Context Sufficiency Model V0.1

## Principle

Context is sufficient when the Scene Writer can stage the requested work without guessing a Canon fact, required causal fact, character intention, required state movement, or required outcome. It is **not** a demand for encyclopaedic project history.

## Context Classes

|Class|Information|When it belongs here|If absent|
|---|---|---|---|
|REQUIRED|Scene purpose / requested repair target.|Always: Scene Writer cannot safely decide what material is relevant without it.|`NEEDS_CONTEXT`.|
|REQUIRED|Scene identity and project/episode identity or an unambiguous canonical scope.|When multiple scenes/projects or locked canon records could apply.|`NEEDS_CONTEXT` if scope ambiguity could change facts; otherwise record a narrow assumption.|
|REQUIRED|Who is present / materially participates.|When presence changes objective, information delivery, dialogue action, or required event.|`NEEDS_CONTEXT` if it changes legal construction.|
|REQUIRED|Character objective or explicitly approved absence of one.|When objective/resistance is needed to stage the requested scene or diagnose its function.|`NEEDS_CONTEXT` if Scene Writer would have to invent the intention.|
|REQUIRED|Known Canon / Showrunner locks relevant to the scene.|When a fact, causality, required event, information, outcome constraint, or episode function is locked.|`NEEDS_CONTEXT` or `UPSTREAM_DECISION_REQUIRED`; never invent a replacement fact.|
|REQUIRED|Prior-scene state / relationship information.|Only when its absence affects present causality, objective, entry, information meaning, or required change.|`NEEDS_CONTEXT` when material; otherwise continue.|
|REQUIRED|Desired post-scene state.|Only when it is supplied or necessary to evaluate a locked required outcome/change.|`NEEDS_CONTEXT` if locked result cannot be inferred safely.|
|USEFUL|Relationship texture, history, social context, occupation, self-view, or relevant character constraint.|When it improves pressure, dialogue choice, or clue selection but no locked fact depends on it.|Continue; do not block. Keep construction general enough not to invent it.|
|USEFUL|Prior/next scene summaries, first-image preference, production context, format preference.|When it sharpens entry/exit, handoff, or presentation but does not alter locked meaning.|Continue; use conditional check or flag.|
|OPTIONAL|Full season history, world bible beyond relevant locks, actor notes, full visual plan, production budget, future AI profile, stylistic preference.|When it does not determine legal scene construction.|Do not request it as a precondition.|

## Materiality Gate

Before returning `NEEDS_CONTEXT`, answer all four questions:

1. Would the missing information change a Canon fact, causal relationship, character intention, required turn/state movement, or required outcome?
2. Is it needed for the requested mode rather than merely useful for polish?
3. Can the scene be written/diagnosed with a narrower neutral construction that avoids inventing the missing fact?
4. Would a stated assumption remain below the Assignment Lock rather than silently change it?

Return `NEEDS_CONTEXT` only when **1 and 2 are yes, and 3–4 cannot resolve the gap safely**. This is the explicit anti-context-hunger guard derived from the Shared QA KL-01 lesson; it neither changes nor reproduces Shared QA.

## Early-Exit Cases

|Case|Decision|
|---|---|
|Existing scene already fulfils its function, is shootable, respects locks, has valid dialogue movement and justified boundaries.|In `REVISE`, return `NO_MATERIAL_CHANGE`; do not rewrite to prove value.|
|Requested repair is language/register/voice quality only.|Do not duplicate QA; mark `SHARED_QA_HANDOFF_ELIGIBLE`.|
|User requests final lens, dolly, coverage, staging, edit rhythm, or composition.|Return Director/Cinematography boundary handoff.|
|A known production issue has no confirmed constraint yet.|Continue scene work; add `PRODUCTION_REVIEW_REQUIRED` flag rather than block.|
|An external AI production profile is mentioned but not supplied.|Record its Deferred status only; do not ask for a schema or invent a limit.|

