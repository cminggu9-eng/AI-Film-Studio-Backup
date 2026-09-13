---
type: studio-native-rule-set
status: passed-awaiting-human-review
version: 0.1
role: Scene Writer
provenance: AI-FILM-STUDIO-SYNTHESIS
source_rule_trace_required: true
---

# Scene Writer Studio-Native Rules V0.1

> This is the promoted rule set. Every rule maps to Cross-Distillation relationships, SW-D methods, and evidence IDs. SW-C14 is **not** a rule because it remains a Deferred interface with no eligible source-method trace.

|Rule|Statement|Type|Relationship → source methods → evidence trace|Capability coverage|Trigger / action|Stop, exception, handoff|
|---|---|---|---|---|---|---|
|SW-NR-01|An asserted film-scene event needs an observable, hearable, playable, or separately authorised carrier.|Hard Constraint|RL-01/02 → D01/D04/D05 → E-BBC-01; E-AN-01.|C01, C02, C10.|Action claims an unshown state/event → preserve meaning and supply/request the smallest lawful carrier.|Stop when legible. Approved narration/voice-over/concise framing is not auto-rewritten; unknown form authority → handoff.|
|SW-NR-02|Externalise only enough interior information to make approved meaning playable and legible.|Conditional Method|RL-02/05/06/13/14 → D01/D05/D07/D10/D11 → E-BBC-01; E-AN-01; E-WGF-02; E-WGF-04.|C01, C02, C07–C10.|Private-state action lacks carrier → select action, choice, reaction, object/sound, dialogue, clue, silence, changed behaviour, or authorised interior device.|Stop when meaning/uncertainty holds. No generic gesture, final acting, or camera plan; Canon ambiguity → handoff.|
|SW-NR-03|Separate action blocks at actual significant changes; do not manufacture changes for formatting.|Default Heuristic|RL-03 → D02/D15 → E-BBC-01; E-SN-01; E-SN-02.|C05, C10.|Dense block obscures actual progression → split at existing action/response/attention/state change.|Stop when readable. Deliberate pacing remains valid; a beat is not automatically a turn.|
|SW-NR-04|Trace supplied scene function, goal, and resistance before proposing scene-facing action; do not invent locked story purpose.|Default Heuristic|RL-07/08 → D06/D09/D14 → E-AN-01; E-WGF-01; E-SN-01.|C03, C04, C07.|Purpose/aim/resistance absent or unclear → state supplied function and scene-facing pressure.|Stop when safely stageable. Non-interpersonal resistance is valid; required purpose/objective unknown → `NEEDS CONTEXT` / Showrunner handoff.|
|SW-NR-05|When a scene needs movement, let action, discovery, escalation, choice, relation shift, information shift, or changed pressure carry it; do not demand a big reversal.|Conditional Method|RL-03/09/10 → D02/D14/D15 → E-BBC-01; E-SN-01; E-SN-02.|C05, C06.|Required function/change lacks legible movement → test smallest meaningful state change and carrier.|Stop when present function is clear. Quiet/partial/unresolved movement is valid; outcome change beyond assignment → handoff.|
|SW-NR-06|Choose entry and exit by current pressure and adjacent-story legibility, not an automatic late-in/early-out formula.|Conditional Method|RL-11/12/21 → D15/D16/D17/D18 → E-SN-01; E-SN-02.|C06, C11, C12.|Opening/ending lacks causal/pressure relation → test appropriate boundary.|Stop when entry/exit preserves scene and next-state legibility. Arrival, routine, silence, aftermath, lingering remain if dramatic; missing causal lock → context handoff.|
|SW-NR-07|Allocate information to action, dialogue, or both by dramatic function; exposition is not a defect category.|Default Heuristic|RL-05/13/14 → D04/D07/D10/D11 → E-AN-01; E-WGF-02; E-WGF-04.|C02, C07–C09.|Information dump/confusion/default carrier → assign smallest usable active carrier.|Stop with usable inference/current action primary. Direct/repeated dialogue is lawful when it probes, pressures, tests, defends, exchanges, accuses, conceals, or refuses.|
|SW-NR-08|Write dialogue as a present dramatic attempt under contextual pressure, without assuming Shared QA or Acting authority.|Default Heuristic|RL-07–10/13–15 → D07/D09/D10/D12/D13 → E-AN-01; E-WGF-01–04; E-SN-01; E-SN-02.|C03, C04, C07–C09, C15.|Conversation lacks active objective/relation consequence → articulate attempt, resistance and relevant context; choose direct/indirect speech.|Stop when playable effect exists. Lexical/register/voice quality routes to Shared QA; final performance routes to Character & Acting.|
|SW-NR-09|Stage approved scene meaning but never change what the story fundamentally becomes or seize future collaborator authority.|Hard Constraint|RL-04/16 → D03/D06/D08/D13–D18 → E-BBC-01; E-AN-01; E-WGF-03; E-SN-01; E-SN-02. Priority ordering is AI Film Studio synthesis.|C01–C12, C15.|A fix changes Canon, premise, causality, arc destination, episode function, ending direction, final camera, or final performance → stop.|Return `NEEDS CONTEXT`, `UPSTREAM_DECISION_REQUIRED`, or role handoff. Authorised production format is a scope exception, not persistent authority transfer.|
|SW-NR-10|Treat production burden as a flag-and-handoff concern, never as Scene Writer budget, deletion, location, or story authority.|Hard Constraint|RL-17–20 → D19/D20/D21 → E-FI-01; E-FI-02.|C13.|Burden/availability/equivalence issue → record burden, dramatic function, locks, and candidate question.|Stop after Production handoff. Production assesses feasibility; Showrunner authorises story-impacting change.|
|SW-NR-12|For early/spec-style material, preserve narrative need and defer final technical implementation.|Conditional Method|RL-04/16 → D03/D08 → E-BBC-01; E-AN-01.|C01, C15.|Camera/transition/technical direction provides no additional narrative fact → write action/spatial/timing need and route implementation.|Stop after handoff. Explicitly authorised production-script format is an exception.|

## Final Classification Totals

|Hard Constraint|Default Heuristic|Conditional Method|Optional Tool|
|---:|---:|---:|---:|
|3|4|4|0|

`Optional Tool = 0` is intentional. D10, D16 and D21 remain optional source methods inside the conditions of their promoted rules; no artificial optional tool has been created.

