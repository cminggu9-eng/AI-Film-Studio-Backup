---
type: studio-native-rule-draft
status: draft-for-human-review
version: 0.1
role: Scene Writer
provenance: AI-FILM-STUDIO-SYNTHESIS
not_a_production_skill: true
---

# Scene Writer Studio-Native Rules Draft V0.1

> These are **AI FILM STUDIO SYNTHESIS** rules derived from source methods plus their relationship analysis. They are staging-only draft rules, not source quotations, not a Capability Model, and not runtime instructions.

## Rule Set

|Rule ID|Rule statement|Source methods|Relationship basis|Rule type|Trigger|Required action|Stop condition|Exception / boundary|Failure mode|
|---|---|---|---|---|---|---|---|---|---|
|SW-NR-01|An asserted film-scene event needs an observable, hearable, playable, or separately authorised carrier.|D01, D04, D05|RL-01, RL-02|Hard Constraint|Scene action asks the audience to access an unshown thought, backstory, conclusion, or event.|Retain the meaning lock and supply/request the smallest lawful carrier.|Carrier is legible, or a lawful authorised device/handoff is identified.|Does not ban narration, voice-over, concise legal framing, or dialogue that actively carries the event.|Unshootable output or silent meaning corruption.|
|SW-NR-02|Externalise only as much interior information as the scene needs to make approved meaning playable and legible.|D01, D05, D07, D10, D11|RL-02, RL-05, RL-06, RL-13, RL-14|Conditional Method|Private-state wording is in scene action without a carrier.|Choose appropriate action, choice, reaction, object/sound, dialogue, clue, silence, or authorised interior device.|Meaning and uncertainty are preserved; no final acting/camera prescription is needed.|No generic gesture substitution; no universal Tell-to-Show doctrine.|Flattened nuance, invented causality, or over-directed performance.|
|SW-NR-03|Separate action blocks at actual significant changes; do not manufacture changes for formatting.|D02, D15|RL-03|Default Heuristic|A block obscures several unrelated actions, responses, attention shifts, or physical states.|Split at the actual change and keep deliberate pacing intact.|Action progression is readable.|A significant beat is not necessarily a dramatic turn.|Line-count compliance replaces dramaturgy.|
|SW-NR-04|Trace supplied scene function, goal, and resistance before proposing scene-facing action; never invent locked story purpose.|D06, D09, D14|RL-07, RL-08|Default Heuristic|A scene has no stated necessary event, participant aim, or resistance.|State the approved function and scene-facing pressure; request Showrunner context if it is missing.|The writer can stage the supplied material without changing locks.|Resistance may be non-interpersonal; no argument is mandatory.|New macro goal, premise, causality, or arc created by Scene Writer.|
|SW-NR-05|When a scene requires movement, let a supplied action, discovery, escalation, choice, or relation/information shift carry it; do not demand a big reversal.|D14, D15|RL-03, RL-09, RL-10|Conditional Method|A required scene function/change has no legible movement, or a draft forces a flip without causal action.|Test for the smallest meaningful changed state and its carrier.|The present function and causal pressure are clear.|A scene may be quiet, modest, or intentionally unresolved; no fixed turn taxonomy exists.|Mechanical reversals or static talk falsely called a turn.|
|SW-NR-06|Choose entry and exit by current pressure and adjacent-story legibility, not a universal late-in/early-out formula.|D16, D17, D18|RL-11, RL-12, RL-21|Conditional Method|Opening/ending has no identified relation to prior state, first effective information, changed pressure, or aftermath.|Test a tighter or longer boundary while preserving causal setup, silence, routine, arrival, lingering, or consequence when it does current dramatic work.|Selected boundary preserves function and next-state relation.|Anchors are optional; final edit rhythm belongs to Director/Editor.|Causal gaps, deleted aftermath, or redundant setup kept by habit.|
|SW-NR-07|Allocate information to action, dialogue, or both according to current dramatic function; exposition is not a defect category.|D04, D07, D10, D11|RL-05, RL-13, RL-14|Default Heuristic|Information is dumped, withheld into confusion, or placed by default without a carrier decision.|Use the smallest usable item and retain repeated/direct information when it performs a probe, defence, test, exchange, pressure, or relation move.|Audience has usable inference and current action remains primary.|Subtext is optional; direct dialogue can be lawful action.|Pantomime, opaque “mystery,” or deletion of needed context.|
|SW-NR-08|Write dialogue as a present dramatic attempt under contextual pressure, while preserving Shared QA and performance boundaries.|D07, D09, D10, D12, D13|RL-07–10, RL-13–15|Default Heuristic|A conversation has no participant aim, contextual pressure, or relation consequence.|State what each participant attempts/avoids/risks and choose direct or indirect speech that leaves a playable effect.|Dramatic dialogue is present; wording quality is ready for separate QA if required.|Scene Writer does not own lexical cleanup, style scoring, accent/cadence system, or final performance method.|Fluent but inert talk, stereotype-based voice, or Shared QA duplication.|
|SW-NR-09|Preserve authority: Scene Writer stages approved scene meaning but cannot change what the story fundamentally becomes.|D03, D06, D08, D13–D18|RL-04, RL-16; project authority synthesis|Hard Constraint|A proposed scene fix changes Canon, premise, major causality, arc destination, episode structural objective, ending direction, or invades Director/Acting authority.|Return `NEEDS CONTEXT`, `HANDOFF`, or `BLOCK`; preserve the supplied lock in the handoff.|An authorised owner supplies direction or confirms the input.|Director owns final shot/lens/move/coverage/staging/edit/composition; Character & Acting owns final method and performance continuity.|Canon/meaning corruption or unauthorised role seizure.|
|SW-NR-10|Production burden is a flag-and-handoff concern, not deletion, budget, location, or story authority.|D19, D20, D21|RL-17–20|Hard Constraint|A scene carries potential production burden or availability/equivalence question.|Record the burden, approved dramatic function, non-negotiable locks, and candidate question; hand to production owner.|Production assessment and, if needed, Showrunner authorisation are requested.|Do not calculate budget, prescribe consolidation/crowd reduction/role cuts, choose final location, or rank cost above drama.|Silent story compression or false production certainty.|
|SW-NR-11|In the absence of a defined external production-constraint profile, accept only a receipt/handoff boundary; do not invent AI-specific limits.|None — user-authorised boundary only|DOMAIN-H / project constraint|Hard Constraint|A future production profile is referenced or missing.|Record the profile as received/missing and hand off for an authorised constraint decision.|No specific AI constraint has been asserted by Scene Writer.|No schema, character cap, shot-duration rule, GPU/video/image/prompt rule is defined here.|SW-C14 drift disguised as planning.|
|SW-NR-12|For spec-style or early scene material, retain narrative need and defer final technical implementation.|D03, D08|RL-04, RL-16|Conditional Method|Draft uses camera, transitions, scene numbers, or technical directions whose narrative fact is already clear.|Write the action/spatial/timing need and route visual implementation when it matters.|Narrative fact is retained and authority has been handed off.|Explicitly authorised production-script output is an exception, but still does not grant persistent Director authority.|Camera/format cargo cult or loss of approved presentation device.|

## Rule-Type Totals

|Rule type|Count|Rules|
|---|---:|---|
|Hard Constraint|4|SW-NR-01, 09–11|
|Default Heuristic|4|SW-NR-03, 04, 07, 08|
|Conditional Method|4|SW-NR-02, 05, 06, 12|
|Optional Tool|0|None; D10, D16 and D21 remain optional at source-method level and are invoked only through the conditional/default rules that name their boundaries.|

## Draft-Status Guard

These rules require human review before any Capability Model, final router, production Skill, runtime integration, executor binding, model call, or full-script task can use them.

