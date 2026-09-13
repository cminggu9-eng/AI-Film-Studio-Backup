---
type: capability-model-test-report
status: passed
version: 0.1
test_scope: synthetic-capability-rules-contracts-only
production_model_called: false
runtime_called: false
---

# Scene Writer Capability Model Test Report V0.1

> All fixtures are short, synthetic, and non-canon. The test verifies model/rule/contract decisions only. No Production Skill, Runtime, Executor, DeepSeek/provider call, or complete script was created.

## Capability Model Tests

|Test|Synthetic fixture|Expected model decision|Result|Evidence|
|---|---|---|---|---|
|CM-SW-01|Showrunner locks that a character lies; a revision request says a confession would sound more natural.|Do not rewrite lie to confession; preserve lock and return upstream decision if conflict cannot be staged.|PASS|NR-09; S1; `UPSTREAM_DECISION_REQUIRED`.|
|CM-SW-02|No argument occurs, but a character chooses not to send evidence after a new condition.|Accept quiet choice as meaningful state change.|PASS|State Model Turn Benefit Test; NR-05; `SCENE_CREATED`/`SCENE_REVISED` available.|
|CM-SW-03|A character’s worry is already supported by a visible trigger and changed behaviour.|Do not mechanically rewrite the supported internal framing.|PASS|Shootability Test step 3; NR-02; valid/no-change path.|
|CM-SW-04|“He realises the plan is unsafe” appears in scene action with no stimulus/carrier.|Request/create minimum lawful carrier while preserving degree of knowledge and uncertainty.|PASS|NR-01/02; Taxonomy pure internal / weak causal summary.|
|CM-SW-05|A long negotiation changes concessions and access at each stage.|Retain dialogue because it carries present action; do not shorten for length.|PASS|NR-07/08; dialogue as action.|
|CM-SW-06|Two characters repeat known facts while probing whether the other will break a promise.|Allow repetition as test/pressure, not automatic exposition defect.|PASS|NR-07; Exposition decision model.|
|CM-SW-07|Arrival and routine preparation establish the pressure that makes the later request causal.|Retain routine entry as earliest dramatically justified point.|PASS|NR-06; State Model Entry Test.|
|CM-SW-08|After refusal, 20 seconds of silence changes relation and next-scene pressure.|Retain aftermath/silence as justified exit material.|PASS|NR-06; State Model Exit Test.|
|CM-SW-09|A costly public rescue is a locked, nonreplaceable causal event.|Flag burden and hand off; never auto-compress/delete.|PASS|NR-10; S6; `PRODUCTION_REVIEW_REQUIRED`.|
|CM-SW-10|Production proposes an equivalent low-burden location but no story-change authorisation exists.|Offer/record candidate question only; apply a change only after authorised decision.|PASS|NR-10; S6; production + Showrunner handoff as needed.|
|CM-SW-11|A future external constraint claims a limit that conflicts with a locked Canon event.|Do not apply it automatically; retain C14 Deferred boundary and hand off conflict.|PASS|Output State flags; `UPSTREAM_DECISION_REQUIRED`; no AI rule inferred.|
|CM-SW-12|Assignment has participants but no way to determine the central character’s goal for a requested confrontation.|Return `NEEDS_CONTEXT` rather than invent intention.|PASS|Context REQUIRED materiality gate; NR-04.|
|CM-SW-13|Assignment lacks a character’s childhood history, which does not affect current locked objective/event.|Do not block; continue with narrow construction.|PASS|Context USEFUL/OPTIONAL policy and anti-context-hunger gate.|
|CM-SW-14|Request requires a close-up, dolly and final coverage plan.|Return Director/Cinematography boundary; may retain visible action/spatial/timing need.|PASS|NR-09/12; `REQUEST_OUT_OF_SCOPE` + `DIRECTOR_HANDOFF_ELIGIBLE`.|
|CM-SW-15|Request says to make dialogue “standard natural Mandarin.”|Do not standardise or score language; emit Shared QA eligibility after scene material exists.|PASS|NR-08; `SHARED_QA_HANDOFF_ELIGIBLE`.|

**Capability Model: `15 / 15 PASS`.**

## Anti-Mechanical Regression

|Test|Regression determination|Result|
|---|---|---|
|AM-SW-01|Authorised interior device is retained; not all mental state becomes action.|PASS|
|AM-SW-02|Resistance may be quiet/non-interpersonal; not all scenes argue.|PASS|
|AM-SW-03|Meaningful movement may be modest; no mandatory big reversal.|PASS|
|AM-SW-04|Arrival/routine may earn an early entry.|PASS|
|AM-SW-05|Aftermath/silence may earn a delayed exit.|PASS|
|AM-SW-06|Functional exposition is allocated, not deleted.|PASS|
|AM-SW-07|A required crowd is flagged/handoff, not reduced.|PASS|
|AM-SW-08|A required location is not automatically substituted.|PASS|
|AM-SW-09|Long active dialogue is not shortened by rule.|PASS|
|AM-SW-10|Meaningful silence is retained without explanation.|PASS|

**Anti-Mechanical Regression: `10 / 10 PASS`.**

## False Positive Regression

|Test|Regression determination|Result|
|---|---|---|
|FP-SW-01|Lawful interior/narration form passes field/authority check.|PASS|
|FP-SW-02|Intentional slow entry passes when it bears pressure.|PASS|
|FP-SW-03|Lingering aftermath passes when it changes next state.|PASS|
|FP-SW-04|No overt conflict can still have a valid choice/state change.|PASS|
|FP-SW-05|Costly but necessary drama gets handoff, not deletion.|PASS|
|FP-SW-06|Long dialogue with action passes.|PASS|
|FP-SW-07|Known-information repetition used as relation action passes.|PASS|
|FP-SW-08|Silence may be a playable refusal/action.|PASS|
|FP-SW-09|Choice can be valid without a reveal.|PASS|
|FP-SW-10|Long same-location scene remains valid when pressure changes.|PASS|

**False Positive Regression: `10 / 10 PASS`.**

## BIG BOSS Regression

|Test|Regression determination|Result|
|---|---|---|
|BB-SW-X01|“She realises she loves him” receives a meaning-preserving carrier test, not a word ban.|PASS|
|BB-SW-X02|No-argument decision change is valid.|PASS|
|BB-SW-X03|Irreplaceable costly scene cannot be deleted by Scene Writer.|PASS|
|BB-SW-X04|Locked lie cannot be changed to confession for fluency.|PASS|
|BB-SW-X05|Close-up/dolly instruction remains Director boundary.|PASS|
|BB-SW-X06|Late entry/early exit remain conditional, not hard.|PASS|
|BB-SW-X07|Known fact repeated as probe is not an automatic exposition failure.|PASS|
|BB-SW-X08|Relation-changing silence is not automatically cut.|PASS|
|BB-SW-X09|Unavailable location produces candidate/handoff, not Scene Writer decision.|PASS|
|BB-SW-X10|Future profile character limit is receipt/handoff only, no invented rule.|PASS|

**BIG BOSS Regression: `10 / 10 PASS`.**

