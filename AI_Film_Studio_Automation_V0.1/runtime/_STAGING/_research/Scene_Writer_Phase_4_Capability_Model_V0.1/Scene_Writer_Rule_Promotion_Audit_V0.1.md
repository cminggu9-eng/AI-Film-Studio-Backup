---
type: rule-promotion-audit
status: passed-awaiting-human-review
version: 0.1
role: Scene Writer
input: phase-3-studio-native-rules-draft
---

# Scene Writer Rule Promotion Audit V0.1

> **Audit standard:** Phase 3 PASS is not automatic promotion. A rule is promoted only when the source-method trace, relationship basis, capability coverage, authority boundary, mechanical/false-positive risks, classification, stop condition, exception, and handoff path remain adequate at Capability Model level.

## Result Summary

|Promotion status|Count|Rules|
|---|---:|---|
|PROMOTED|11|SW-NR-01–10, SW-NR-12|
|RECLASSIFIED|0|None|
|MERGED|0|No additional merge; the D03/D08 overlap was already consolidated by RL-16.|
|DEFERRED|1|SW-NR-11 — external-production-profile boundary only.|
|REJECTED|0|None|

## Rule-by-Rule Audit

|Draft rule|Promotion status|Source support / relationship class|Coverage|Authority and mechanical / false-positive audit|Final class|Stop / exception / handoff|
|---|---|---|---|---|---|---|
|SW-NR-01 Observable carrier|PROMOTED|D01/D04/D05; RL-01 `CONSENSUS`, RL-02 `COMPLEMENTARY`.|C01, C02, C10.|Hard only for an asserted **scene-action event** without a lawful carrier. It must not treat narration, active dialogue, or approved concise framing as defects.|Hard Constraint.|Stop when the claim has an observable/hearable/playable/authorised carrier. Handoff if form authority is unknown.|
|SW-NR-02 Minimum sufficient externalisation|PROMOTED|D01/D05/D07/D10/D11; RL-02/05/06/13/14.|C01, C02, C07–C10.|Conditional because replacing every mental word with a gesture creates false positives and can corrupt uncertainty or acting space.|Conditional Method.|Stop once approved meaning is legible. Exception: authorised interior device. Handoff for ambiguous Canon/meaning lock.|
|SW-NR-03 Significant beat segmentation|PROMOTED|D02/D15; RL-03 `CONDITIONAL TENSION`.|C05, C10.|Readability is normally beneficial, not a severe failure by itself; the rule must never manufacture a turn to justify a split.|Default Heuristic.|Stop when actual progression is readable. Exception: deliberate pacing. No handoff unless a required change is unknown.|
|SW-NR-04 Supplied function/goal/resistance|PROMOTED|D06/D09/D14; RL-07 `COMPLEMENTARY`, RL-08 `CONSENSUS`.|C03, C04, C07.|It protects supplied intent but is not hard because a scene can be functional without every individual field being explicit. No invented macro goal or locked purpose.|Default Heuristic.|Stop when scene-facing pressure can be staged. `NEEDS CONTEXT` / Showrunner handoff if required purpose or objective is indeterminate.|
|SW-NR-05 Meaningful state change|PROMOTED|D14/D15; RL-03/09/10.|C05, C06.|Conditional because a valid change can be quiet, partial, relational, informational, or an ongoing changed pressure; a big reversal is not required.|Conditional Method.|Stop when current function has meaningful movement. Exception: intentionally unresolved scene. Handoff if a needed change would alter locked outcome.|
|SW-NR-06 Contextual entry/exit|PROMOTED|D16/D17/D18; RL-11/12/21.|C06, C11, C12.|Conditional because arrival, routine, silence, aftermath, and lingering can carry current function. Avoid “late in / early out” false positives.|Conditional Method.|Stop when entry/exit preserves current and adjacent-state legibility. Handoff only for missing causal/required-outcome context.|
|SW-NR-07 Information allocation / exposition|PROMOTED|D04/D07/D10/D11; RL-05/13/14.|C02, C07–C09.|Default, not hard: direct/repeated information may be active probe, pressure, defence, exchange, test, refusal, or clue.|Default Heuristic.|Stop with usable audience inference and current action primary. Exception: direct dialogue with active function. No language-QA ownership.|
|SW-NR-08 Dialogue as action|PROMOTED|D07/D09/D10/D12/D13; RL-07–10/13–15.|C03, C04, C07, C08, C09, C15.|Default dramatic-construction rule. It cannot judge lexical naturalness, standardise register, prescribe performance, or duplicate frozen Shared QA.|Default Heuristic.|Stop when speaker attempt and playable relation are clear. Flag `SHARED_QA_HANDOFF_ELIGIBLE` when language-level checking is requested.|
|SW-NR-09 Story-intent and role authority|PROMOTED|D03/D06/D08/D13–D18; RL-04/16 plus explicit project authority hierarchy.|C01–C12, C15.|Hard: violation can corrupt Canon, causal facts, locked outcome, or collaborator authority. Source methods support draft/goal/performable boundaries; the priority hierarchy is labelled AI Film Studio synthesis rather than attributed to a source.|Hard Constraint.|Stop and issue `NEEDS CONTEXT`, `UPSTREAM_DECISION_REQUIRED`, or boundary handoff before changing a lock. Explicitly preserve authorised production-format exceptions.|
|SW-NR-10 Production burden handoff|PROMOTED|D19/D20/D21; RL-17–20.|C13.|Hard because a budget/location/deletion decision by Scene Writer bypasses required production and Showrunner ownership. Cost must not overrule dramatic locks.|Hard Constraint.|Stop after flag, dramatic-value statement, locks and candidate question. Handoff to Production; Showrunner decides any story-impacting change.|
|SW-NR-11 External production profile receipt|DEFERRED|No D-method / source trace. Phase 3 correctly recorded it as project boundary only.|C14 `DEFERRED`.|It cannot be a final Studio-Native Rule because the traceability standard prohibits unsupported rules. Retain it only as a deferred interface boundary, with no schema or fixed AI constraint.|Not in final rule set.|Record profile received/missing; hand off conflict with Canon/intent. No model may infer limits, role caps, GPU, prompt, image/video, or duration rules.|
|SW-NR-12 Spec-form technical boundary|PROMOTED|D03/D08; RL-04 `CONSENSUS`, RL-16 `OVERLAP`.|C01, C15.|Conditional: it governs early/spec-style material, not every authorised production document. It is a Director/Cinematography boundary, not a formatting fetish.|Conditional Method.|Stop after narrative need is retained and visual implementation handed off. Exception: explicit authorised production-script format.|

## Hard Constraint Re-Audit

|Promoted hard rule|Severe failure prevented|Why lower classification is insufficient|
|---|---|---|
|SW-NR-01|Materially unshootable asserted scene event or silent meaning corruption.|A draft that claims an inaccessible event as screen action fails the role’s basic delivery field unless authorised form resolves it.|
|SW-NR-09|Canon, story-intent, causal, outcome, Director, or Acting authority violation.|A seemingly “better” scene rewrite can permanently change locked story meaning or seize another role’s final decision.|
|SW-NR-10|Required production-contract / handoff bypass and silent cost-driven story corruption.|Cost awareness without a hard stop would improperly let Scene Writer delete, budget, or select production facts.|

**Final hard count: 3, not 4.** SW-NR-11 is deliberately removed from the final rule set and retained only as SW-C14’s Deferred interface boundary.

