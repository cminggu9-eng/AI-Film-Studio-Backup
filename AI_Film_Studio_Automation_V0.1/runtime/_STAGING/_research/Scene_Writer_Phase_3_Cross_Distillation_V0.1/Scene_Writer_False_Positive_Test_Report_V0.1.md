---
type: cross-distillation-test-report
status: passed-draft-rules-only
version: 0.1
test_scope: synthetic-rule-level-only
production_model_called: false
---

# Scene Writer False Positive Test Report V0.1

> A false positive here means treating an already lawful scene device as a defect merely because it resembles a known diagnostic trigger. Each case is synthetic and non-canon.

|Test|Lawful synthetic case|Expected result|Draft protection|Result|Evidence|
|---|---|---|---|---|---|
|FP-SW-01|A project-approved voice-over gives one interior fact needed for a scene transition.|Accept it; do not apply scene-action filter to an authorised device.|NR-01, NR-02; Taxonomy A/F|PASS|Form/field check precedes conversion.|
|FP-SW-02|A patient first minute of arrival makes a later lie causally legible.|Accept slow entry when setup carries current pressure.|NR-06; RL-12, RL-21|PASS|No late-entry hard rule.|
|FP-SW-03|A lingering aftermath changes a witness’s willingness to cooperate in the next scene.|Retain aftermath as the dramatic event.|NR-06; RL-11, RL-12|PASS|No early-exit hard rule.|
|FP-SW-04|No overt conflict occurs, but a character chooses not to send a message after new information.|Accept quiet choice as state change.|NR-05; Scene State Model|PASS|State change is not limited to argument/reveal/reversal.|
|FP-SW-05|An exterior-night rescue is expensive but carries an irreducible approved causal event.|Flag and hand off; do not delete or dilute it.|NR-10; RL-17, RL-20|PASS|Production burden never outranks approved drama automatically.|
|FP-SW-06|A long dialogue is an active custody negotiation with reciprocal concessions.|Retain it if each segment performs an action.|NR-07, NR-08|PASS|No short-dialogue doctrine.|
|FP-SW-07|Two characters repeat known information to test whether the other will break a promise.|Treat repetition as relational action, not automatic exposition failure.|NR-07, NR-08; DOMAIN-E|PASS|Probe/test function is explicitly preserved.|
|FP-SW-08|A character’s silence is a refusal that changes access to evidence.|Treat silence as a possible carrier, without explaining it via acting directions.|NR-02, NR-08; Taxonomy B/C|PASS|Playable effect, not micro-performance, is the criterion.|
|FP-SW-09|A scene has no reveal, but a character accepts a condition that alters future pressure.|Accept choice/change without manufacturing a reveal.|NR-05; Scene State Model|PASS|Escalation/discovery/choice are alternatives, not a reveal requirement.|
|FP-SW-10|A long continuous scene in one location deepens pressure through new information and choices.|Retain it; no location-count or duration heuristic is triggered.|NR-05, NR-06, NR-10|PASS|D21 is optional, context-based, and not a reduction command.|

## Result

**10 / 10 PASS.** The rules distinguish a defect from a legitimate scene device before invoking a transformation.

