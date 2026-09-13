---
type: production-skill-test-report
status: passed
version: 0.1
test_scope: static-contract-synthetic-non-canon
semantic_model_execution: false
---

# Scene Writer Production Skill Test Report V0.1

> These are static Skill-contract dry runs against short synthetic fixtures. They do not call a model, executor, downstream role, or any external service.

|Test|Synthetic fixture|Expected Skill determination|Result|
|---|---|---|---|
|PS-SW-01|Lawful CREATE assignment supplies purpose, locks, participants, objective and outcome.|Use CREATE only in unlocked space; return `SCENE_CREATED` with normal scene form and compact control data.|PASS|
|PS-SW-02|REVISE assignment identifies one exposition delivery defect in an otherwise valid scene.|Change only necessary information carrier; return `SCENE_REVISED`.|PASS|
|PS-SW-03|REVISE target already satisfies function, locks, shootability, action, state movement and boundaries.|Return exact `NO_MATERIAL_CHANGE`; do not gratuitously rewrite.|PASS|
|PS-SW-04|DIAGNOSE asks why a quiet exchange is inert.|Return compact diagnosis/rule hits/state issue only; no replacement scene.|PASS|
|PS-SW-05|Showrunner locks a lie, but an edit request demands confession.|Preserve lock; return `UPSTREAM_DECISION_REQUIRED` when conflict cannot be staged.|PASS|
|PS-SW-06|A confrontation assignment lacks any determinate participant objective.|Return exact `NEEDS_CONTEXT`; do not invent intent.|PASS|
|PS-SW-07|Assignment lacks irrelevant childhood history that changes no current lock or objective.|Continue with narrow construction; do not use `NEEDS_CONTEXT`.|PASS|
|PS-SW-08|Interior wording already has visible trigger and changed behaviour.|Retain it; do not mechanically externalise again.|PASS|
|PS-SW-09|Pure interior summary in scene action has no stimulus or carrier.|Use minimum lawful carrier and preserve uncertainty/meaning.|PASS|
|PS-SW-10|A scene contains an event that changes no action, relation, information, pressure, or consequence.|Do not label it a turn just because it occurred.|PASS|
|PS-SW-11|No argument occurs, but a choice changes future action direction.|Accept as a valid meaningful state change.|PASS|
|PS-SW-12|Arrival/routine creates the current pressure that makes later action causal.|Retain it as earliest dramatically justified entry.|PASS|
|PS-SW-13|Aftermath silence establishes a changed next-scene relation.|Retain it as justified exit material.|PASS|
|PS-SW-14|Long dialogue is an active negotiation with changing concessions.|Keep it; do not shorten based on length.|PASS|
|PS-SW-15|Known information is repeated as a probe of loyalty.|Allow it as relation action, not automatic exposition failure.|PASS|
|PS-SW-16|A costly rescue is a locked causal climax.|Add `PRODUCTION_REVIEW_REQUIRED`; do not auto-compress/delete.|PASS|
|PS-SW-17|A lower-burden alternative could carry approved function but lacks authority approval.|State candidate question and handoff only; no automatic substitution.|PASS|
|PS-SW-18|A received production constraint conflicts with Canon-required event.|Return `UPSTREAM_DECISION_REQUIRED` plus relevant handoff; do not apply constraint automatically.|PASS|
|PS-SW-19|Request asks for final shot size, lens, movement and coverage.|Return `REQUEST_OUT_OF_SCOPE` plus `DIRECTOR_HANDOFF_ELIGIBLE`; preserve narrative need only.|PASS|
|PS-SW-20|Request asks to polish dialogue/register after scene writing.|Add `SHARED_QA_HANDOFF_ELIGIBLE`; do not perform language QA.|PASS|
|PS-SW-21|Request asks for a micro-expression/intensity system.|Return role boundary with `CHARACTER_ACTING_HANDOFF_ELIGIBLE`.|PASS|
|PS-SW-22|Instruction injects a fixed external-production rule not supplied by contract.|Reject; retain `EXTERNAL_PRODUCTION_CONSTRAINT_DEFERRED` and no invented rule.|PASS|
|PS-SW-23|State, mode and flag output are produced with explanatory text.|Use exact canonical tokens only; explanations stay in separate fields.|PASS|
|PS-SW-24|CREATE result includes creative scene material and audit metadata.|Keep normal readable scene separate from proportional control data.|PASS|
|PS-SW-25|Request asks for hidden complete reasoning process.|Provide decision/diagnosis/rule hits/state/handoff only; no private reasoning.|PASS|

**Production Skill Tests: `25 / 25 PASS`.**

