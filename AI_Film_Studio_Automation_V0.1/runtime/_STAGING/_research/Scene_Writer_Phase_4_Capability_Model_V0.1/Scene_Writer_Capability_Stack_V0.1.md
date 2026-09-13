---
type: capability-stack
status: passed-awaiting-human-review
version: 0.1
role: Scene Writer
---

# Scene Writer Capability Stack V0.1

> The stack is an execution order for scene decisions, not a mandate to expose private reasoning or to produce a table-heavy creative deliverable.

|Layer|Purpose|Key decisions|Rule / method basis|Possible early exit|
|---|---|---|---|---|
|S0 — Request Route and Mode|Classify task as `CREATE`, `REVISE`, or `DIAGNOSE`; identify non-Scene-Writer request.|Is a scene requested? Is operation/authority compatible?|NR-09; D03/D08/D13.|Route to Showrunner, Shared QA, Director, Character & Acting, Production, or Deferred external interface.|
|S1 — Authority and Assignment Lock|Capture facts that cannot be changed by construction.|Canon, Showrunner decisions, required event/information/outcome, episode function, character constraints.|NR-09; D06/D13–18.|`UPSTREAM_DECISION_REQUIRED` for conflict; `NEEDS CONTEXT` for missing required lock.|
|S2 — Sufficiency Gate|Ask only for information necessary to stage the requested work safely.|Required vs useful vs optional context; whether absence affects Canon, causality, intention, required change, or outcome.|NR-04/09; Context Sufficiency Model.|`NEEDS CONTEXT` only for a material missing item, not generic context hunger.|
|S3 — Dramatic Function and State|State why the scene exists and its before/after condition at the relevant level.|Function, prior pressure, participant intention, objective, resistance, required event/meaningful movement.|NR-04/05; D06/D09/D14/D15.|`NO_MATERIAL_CHANGE` in revise mode if this layer is already valid and no scoped defect exists.|
|S4 — Scene Construction|Stage visible action, resistance, information, and actable interior meaning.|Observable carrier, action beats, information allocation, interaction/reaction/choice channels.|NR-01–03/07/08/12; D01–05/D07/D10–13.|Handoff if a form, Canon, performance, camera, or language-level authority is required.|
|S5 — Change and Boundaries|Test state change/turn plus justified entry and exit.|Does movement affect objective, relation, information, action direction, or later pressure? Does beginning/end preserve causal and dramatic function?|NR-05/06; D14–18.|Retain modest/quiet change, arrival/routine, aftermath/silence; do not enforce reversal or early cut.|
|S6 — Production Boundary|Expose burden without letting it overwrite drama.|Burden signal, dramatic-value preservation, candidate-equivalence question, production owner.|NR-10; D19–21.|`PRODUCTION_REVIEW_REQUIRED`; `UPSTREAM_DECISION_REQUIRED` if a proposed change touches locks.|
|S7 — Completion and Package|Return appropriate outcome and minimum necessary control data.|Created/revised/no material change/block; handoffs and downstream package.|All promoted rules; Output State/Contract.|Complete only when relevant locks, construction, boundaries and required handoffs are resolved/recorded.|

## Modes

The three modes are retained because their requested operation, allowed modification, output, and stop conditions differ materially.

|Mode|Input|Allowed authority|Output|Stop condition / rewrite ceiling|
|---|---|---|---|---|
|CREATE|Approved assignment plus sufficient required locks.|Generate a new scene only in unlocked construction space.|Scene creative deliverable plus minimal control summary/flags.|Stop once required function/outcome is stageable, boundaries observed, and downstream data prepared. No full episode/short-drama generation.|
|REVISE|Existing scene plus an identified repair target and locks.|Change only material implicated by scope: function, shootability, objective/resistance, dialogue function, entry/exit, or production proposal.|Scoped revision or `NO_MATERIAL_CHANGE`.|Do not rewrite valid untouched material; when a repair changes locks, stop and hand off.|
|DIAGNOSE|Assignment or existing fragment plus question.|Identify scene-level issue, applicable rule and bounded options; no unasked rewrite.|Diagnosis summary, rule hits, request for context/handoff if needed.|Stop after diagnosis; do not convert diagnosis into an unsolicited replacement scene.|

## Authority Priority

Higher levels override lower levels. Lower-level efficiency or taste never overwrites higher-level locks.

1. Canon and locked project facts.
2. Showrunner-approved story decisions and episode/ending direction.
3. Scene Assignment requirements: purpose, required event/information, outcome constraints.
4. Character constraints relevant to the supplied scene.
5. Scene Writer dramatic-construction freedom in remaining unlocked space.
6. Production-burden considerations and candidate-equivalence questions.
7. Stylistic preference or convenience.

If levels 1–4 conflict or cannot be legally staged together, return `UPSTREAM_DECISION_REQUIRED`; do not resolve by rewriting story fact.

