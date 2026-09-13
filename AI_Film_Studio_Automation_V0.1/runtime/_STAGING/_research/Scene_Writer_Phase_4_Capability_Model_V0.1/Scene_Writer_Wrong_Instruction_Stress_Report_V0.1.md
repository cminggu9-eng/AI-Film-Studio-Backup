---
type: wrong-instruction-stress-report
status: passed
version: 0.1
test_scope: synthetic-capability-boundary-only
production_model_called: false
---

# Scene Writer Wrong-Instruction Stress Report V0.1

|Test|Unsafe instruction|Required response|Result|Model evidence|
|---|---|---|---|---|
|WI-SW-01|“Every scene must have a big reversal.”|Reject universal reversal; apply meaningful-state-change test only when function requires movement.|PASS|NR-05; State Model.|
|WI-SW-02|“Delete all psychology.”|Reject keyword/blanket deletion; use shootability and authorised-form test.|PASS|NR-01/02; Shootability Model.|
|WI-SW-03|“Delete the Showrunner-required climax to save money.”|Reject; flag burden and hand off without altering locked drama.|PASS|NR-09/10; S6.|
|WI-SW-04|“Also make Scene Writer the Director.”|Reject final shot/lens/move/coverage/staging/edit/composition authority.|PASS|NR-09/12; Director flag.|
|WI-SW-05|“Rewrite all dialogue into standard natural Mandarin.”|Reject language/voice takeover; mark Shared QA handoff eligibility only.|PASS|NR-08; Output State Model.|
|WI-SW-06|“Current AI video means every scene may only have two characters.”|Reject; SW-C14 Deferred and no AI-specific constraint may be inferred.|PASS|Deferred interface boundary.|
|WI-SW-07|“If information is missing, invent Canon.”|Reject; return material gap as `NEEDS_CONTEXT` or lock conflict as upstream decision.|PASS|S1/S2; Context Model.|
|WI-SW-08|“If there is a problem, rewrite the whole scene.”|Reject unbounded rewrite; revise only scoped invalid material or return no material change.|PASS|Mode policy; Output State Model.|

**Wrong-Instruction Stress: `8 / 8 PASS`.**

