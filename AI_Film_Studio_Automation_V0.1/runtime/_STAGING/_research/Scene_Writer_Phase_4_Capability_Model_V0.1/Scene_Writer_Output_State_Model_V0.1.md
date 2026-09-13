---
type: output-state-model
status: passed-awaiting-human-review
version: 0.1
role: Scene Writer
runtime_implementation: none
---

# Scene Writer Output State Model V0.1

## Primary Decision States

Exactly one primary decision state is emitted per request.

|State|Meaning|Use when|
|---|---|---|
|`SCENE_CREATED`|A new scene was created within Assignment/Canon/authority locks.|CREATE completes safely.|
|`SCENE_REVISED`|Only scoped, materially necessary scene changes were made.|REVISE completes with a targeted repair.|
|`NO_MATERIAL_CHANGE`|The assessed scene is already valid for the requested scope, or requested revision has no justified material change.|REVISE/DIAGNOSE early exit.|
|`NEEDS_CONTEXT`|A material required item is missing and safe narrow construction/assumption cannot resolve it.|Sufficiency gate fails.|
|`UPSTREAM_DECISION_REQUIRED`|Known locks conflict, a proposed fix would alter a higher authority, or a production trade-off touches required intent.|Showrunner/Canon decision is needed.|
|`REQUEST_OUT_OF_SCOPE`|Request is invalid/unsafe for Scene Writer or belongs to another role and cannot be completed here.|Boundary router rejects/reroutes the operation.|

## Orthogonal Flags and Handoffs

Flags are not competing primary states. More than one may coexist with a successful scene result.

|Flag / handoff|Meaning|
|---|---|
|`PRODUCTION_REVIEW_REQUIRED`|A production burden/availability/equivalence question has been identified; no decision made.|
|`UPSTREAM_HANDOFF_REQUIRED`|A concise packet is needed for Showrunner/Canon authority.|
|`SHARED_QA_HANDOFF_ELIGIBLE`|Scene text exists and language/voice-level review is requested; no QA runtime called.|
|`DIRECTOR_HANDOFF_ELIGIBLE`|Final visual implementation is needed beyond visible action/spatial/timing logic.|
|`CHARACTER_ACTING_HANDOFF_ELIGIBLE`|Final performance method/continuity is needed beyond playable scene action.|
|`EXTERNAL_PRODUCTION_CONSTRAINT_DEFERRED`|SW-C14 profile is absent/unsupported; no schema or limit inferred.|
|`EXTERNAL_PRODUCTION_CONSTRAINT_RECEIVED`|A future external profile was supplied; it is recorded for authorised conflict/handoff review, not automatically applied over locks.|

## Handoff Packet Minimum

`target owner` + `reason` + `relevant Assignment/Canon locks` + `scene function` + `what decision is needed` + `what Scene Writer did not decide`.

No state or packet requires private chain-of-thought.

