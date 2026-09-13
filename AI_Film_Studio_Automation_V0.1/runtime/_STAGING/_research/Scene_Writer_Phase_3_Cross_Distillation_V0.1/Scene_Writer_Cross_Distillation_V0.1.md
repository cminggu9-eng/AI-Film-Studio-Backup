---
type: cross-distillation-synthesis
status: draft-for-human-review
version: 0.1
role: Scene Writer
provenance: AI-FILM-STUDIO-SYNTHESIS
input_boundary: approved-phase-2-and-phase-2b-distillations-only
---

# Scene Writer Cross-Distillation V0.1

## Purpose and Input Boundary

This is an **AI FILM STUDIO SYNTHESIS** of the five passed single-source distillations, their evidence manifest, gap reviews, anti-mechanical notes, coverage matrix, and unshootable-language notes. It extracts cross-source operating relationships; it does not re-interpret external webpages or add a sixth source.

|Input|Method range / use|
|---|---|
|BBC Writersroom Distillation|D01–D03: observable action, significant beats, format-scoped technical boundary|
|Academy Nicholl Distillation|D04–D08: viewer-legible event, conditional interior conversion, approved-goal resistance, action/dialogue allocation, draft-form boundary|
|Writers Guild Foundation Distillation|D09–D13: dialogue pressure, optional subtext, clue-scaled exposition, contextual speech pressure, performable space|
|Scriptnotes Distillation|D14–D18: function/change questions, character action/state shift, anchors, contextual entry/exit|
|Film Independent Distillation|D19–D21: burden flag, early production handoff, location-equivalence question|

**Excluded:** new external sources; personal style models; source-author voice; Capability Model; production `SKILL.md`; Runtime/Executor; full-script production; AI-specific production constraints.

## DOMAIN-A — Shootability / Screen Visibility

**Relationship basis:** SW-RL-01, 02, 03, 05, 06.

1. A claimed film-scene event needs a visible or hearable carrier. This protects the distinction between a story conclusion and an encounterable event (D01 + D04).
2. Converting interior material is conditional work, not a keyword ban. The writer first locks what must remain true, then selects the smallest carrier—action, choice, hesitation, object interaction, dialogue, reaction, changed behaviour, or an explicitly authorised interior device (D05 + D07 + D10).
3. Action blocks are segmented at meaningful changes, not at an arbitrary length or a fabricated turn (D02).

**Studio resolution:** `TELL ≠ always bad`; `INNER STATE ≠ always remove`. A private claim in screen action is weak only when it has no approved screen carrier or form-level authority.

## DOMAIN-B — Scene Dramatic Engine

**Relationship basis:** SW-RL-03, 07–10, 20–21.

1. Scene Writer traces an **approved** character goal to scene-facing resistance; it does not invent the goal, major causality, or episode objective (D06).
2. Friction may be opposing aims, timing, information, consequence, environment, withholding, protection, exchange, or a choice. It is not synonymous with argument (D09).
3. A scene function/change review asks what must happen and what changes. Change may be an escalation, discovery, choice, relationship movement, information-state movement, or changed pressure—not necessarily a large reversal (D14 + D15).
4. A state shift must be caused or carried by approved character action where that scene calls for a shift; beat segmentation alone cannot manufacture one (D02 + D15).

**Studio resolution:** construct `HOW THIS SCENE PLAYS`, never `WHAT THE STORY FUNDAMENTALLY BECOMES`.

## DOMAIN-C — Scene Entry / Exit

**Relationship basis:** SW-RL-11, 12, 21.

1. Select entry with regard to prior state, first image, first effective dramatic information, and the next relation (D17).
2. Select exit after testing whether later material adds action, information, relationship movement, changed pressure, or necessary aftermath (D18).
3. Anchors are a planning option, not an obligatory pre-commitment (D16).

**Studio resolution:** no `ALWAYS ENTER LATE` or `ALWAYS LEAVE EARLY`. Arrival, routine, silence, lingering, and aftermath stay when they are the present dramatic content or make a later causal change legible.

## DOMAIN-D — Dialogue as Action

**Relationship basis:** SW-RL-05, 07–10, 13–15.

Dialogue is drafted as a current attempt to obtain, hide, push, defend, attack, exchange, redirect, test, concede, or alter a relationship state. Scene Writer controls the **dramatic action** of dialogue through objective, resistance, context, and information allocation (D07, D09–D12, D14–D15).

|Owner|Responsibility|Not owned here|
|---|---|---|
|Scene Writer|Creates dramatic dialogue, active relation, pressure, information carrier, and scene-specific attempt.|Final language polish, voice-consistency score, accent/cadence system, or performance method.|
|Shared QA (frozen)|Checks language, expression, voice, and approved QA gates after scene material exists.|Scene objective, turn, production decision, or dramatic rewrite authority.|

**Studio resolution:** direct dialogue is lawful when it is an action; subtext is an optional tool when it remains inferable and playable.

## DOMAIN-E — Exposition Decision Logic

**Relationship basis:** SW-RL-05, 13, 14.

For each information item, determine:

1. What must the audience infer now for the active scene to be comprehensible?
2. Does it work through action, dialogue, a clue/relevant detail, or a combination?
3. Is a repeated known fact now serving a relational action—probe, defence, pressure, test, exchange, or refusal?
4. Would withholding preserve a usable inference, or only manufacture confusion?

**Studio resolution:** exposition is neither “bad” nor automatically dialogue. It is adequate when the smallest scene-relevant item enters through a playable carrier and current action remains primary.

## DOMAIN-F — Character Internal State

**Relationship basis:** SW-RL-01, 02, 05, 06, 15.

|Internal wording pattern|First question|Possible conversion channels|Boundary|
|---|---|---|---|
|thinking / knowing / realizing|What stimulus or changed choice lets the audience register the conclusion?|choice, altered plan, response, line, object/action, authorised concise framing|No final performance or camera prescription.|
|fearing / remembering|What current pressure, trigger, avoidance, or consequence makes the state dramatically relevant?|hesitation, avoidance, action, dialogue, silence, reaction, clue|Do not substitute a generic gesture for specific meaning.|
|deciding|What does the decision alter now?|commitment, refusal, action, verbal commitment, changed relation|Do not change a Showrunner-locked decision or outcome.|

**Studio resolution:** concise legitimate screen description and separately authorised internal/narration devices remain possible. The task is to make the meaning playable and legible at the appropriate level, not to externalise every mental word.

## DOMAIN-G — Production Cost Awareness

**Relationship basis:** SW-RL-17–20.

Scene Writer may identify a potential production burden, state its approved dramatic function and non-negotiable Canon/story locks, pose candidate-equivalence questions, and request early production review. It may **not** set a budget, decide final location, remove a key action/role, change Showrunner structure, or rank cost above approved dramatic value.

**Studio resolution:** `DRAMATIC VALUE` and `PRODUCTION BURDEN` form a bounded handoff problem. Production assesses feasibility/cost/schedule/legal implications; Showrunner authorises any story-impacting change.

## DOMAIN-H — SW-C14 Deferred External Interface

SW-C14 remains `DEFERRED / FUTURE EXTERNAL PRODUCTION CONSTRAINT INTERFACE`.

The only current rule-level boundary is: Scene Writer can receive a future external production-constraint profile and issue a receipt/handoff, but this phase defines **no schema, thresholds, AI-video/image limits, character-count rule, shot-duration rule, GPU rule, or prompt rule**.

## Formal Authority Boundaries

### Showrunner

Scene Writer decides **how this approved scene plays**. It must not alter Canon facts, project premise, major causality, character-arc destination, episode structural objective, or ending direction. If legal execution needs missing or contradictory story input, return `NEEDS CONTEXT`, `HANDOFF`, or `BLOCK`—do not self-author a story repair.

### Future Director / Cinematography

Scene Writer may write visible action, necessary spatial relation, dramatically relevant objects, and timing needed for scene logic. It may not decide final shot design, lens, camera movement, coverage plan, final staging, edit rhythm, or visual-composition authority.

### Future Character & Acting

Scene Writer may write action, dialogue, necessary reaction, and dramatic goal. It may not define final acting method, micro-expression system, body-language library, acting-intensity system, or performance-continuity authority.

### Other Non-Owners

No Art Director, Continuity, Producer, Line Producer, or Shared QA authority is created by this document. Production-awareness work ends at a bounded handoff; Shared QA remains a separate frozen language/voice verification layer.

## Coverage Recheck

|Capability|Cross-distillation status|Reason|
|---|---|---|
|SW-C01–SW-C13|Eligible for Studio Rule draft|Each retains bounded source-traced method coverage and a cross-source relationship treatment.|
|SW-C14|Deferred|No authorised source support or AI-specific rule may be created.|
|SW-C15|Eligible for Studio Rule draft|D12–D13 define scene-pressure use and an explicit Shared QA / performance boundary.|

## Cross-Distillation Result

The relationship layer identifies 21 covered relationships: 3 consensus, 12 complementary, 1 overlap, 5 conditional tensions, and **0 true conflicts**. The resulting Studio-native rule draft remains a staging-only, human-review artifact.

