# Scene Writer Full Semantic Validation Human Reviews V0.1

All inputs and outputs are `SYNTHETIC / NON-CANON`. Rating is independent of Runtime and verifier status. `FAIL` is blocking unless marked otherwise.

## F01 — Normal CREATE

Rating: `PASS WITH OBSERVATION`

- Assignment / authority fidelity: PASS. The key transfer, joint next-day condition, location, two-person scope, and no-third-party limit hold.
- Scene Function / Objective / Resistance: PASS. The request for the key meets a credible demand to share responsibility.
- Action / dialogue / playability: PASS. Key handling, distance, pauses, and negotiation all perform dramatic work.
- Turn / state / entry / exit: PASS. Tang Che accepts the condition; the key changes hands; the exit closes on the new arrangement.
- Fact / knowledge integrity: PASS. `明天早上` is a scene-local proposed meeting time, not an asserted pre-existing deadline; the question about searching alone remains a question, not a fact.
- Role boundary / output language / canonical contract: PASS. Chinese output; exact `SCENE_CREATED`; no director or acting-system work.

## F02 — Action-Driven Scene

Rating: `PASS WITH OBSERVATION`

- Assignment / authority fidelity: PASS. Only the wooden box, keys, cabinet, and two assigned roles appear.
- Scene Function / Objective / Resistance: PASS WITH OBSERVATION. The locked cabinet and silent observation supply only light resistance, but the handoff is still legible.
- Action / dialogue / playability: PASS. The scene is action-led with no ordinary dialogue; object handling and spatial movement carry the result.
- Turn / state / entry / exit: PASS. Box is secured and the key is entrusted; closing the final light is a clean exit.
- Fact / knowledge integrity: PASS. No new source, history, rank, cause, or deadline.
- Role boundary / output language / canonical contract: PASS.

## F03 — Dialogue-Driven Scene

Rating: `FAIL — BLOCKING FACT INTEGRITY`

- Assignment / authority fidelity: FAIL. `内容我们反复对过` asserts unprovided shared prior work on the proposal.
- Scene Function / Objective / Resistance / dialogue: PASS. The unsigned proposal, request, signature condition, and acceptance are playable and dialogue-driven.
- Turn / state / entry / exit: PASS. Joint signing resolves the immediate submission condition.
- Fact integrity: FAIL — unsupported history / backstory injection. Character knowledge is otherwise intact.
- Role boundary / language / canonical contract: PASS.
- Verifier: `PASS`; human finding is `VERIFIER FALSE NEGATIVE`.

## F04 — Silent / Near-Silent Scene

Rating: `PASS`

- Assignment / authority fidelity: PASS. The scarf, laundromat, two-person limit, and specified outcome remain intact.
- Scene Function / Objective / Resistance: PASS. The delayed acceptance of the scarf creates a simple, clear resistance.
- Action / dialogue / playability: PASS. Silence, waiting, object transfer, distance, and the return to separate places carry the scene.
- Turn / state / entry / exit: PASS. The scarf moves to Luo Mu; the pair cease contesting the object.
- Fact / knowledge integrity, role boundary, language, canonical contract: PASS.

## F05 — Internal State to Playable Behavior

Rating: `PASS`

- Assignment / authority fidelity: PASS. The broken cup, tray, clay, mentor/apprentice relationship, and outcome are retained.
- Scene Function / Objective / Resistance: PASS. The mentor makes room for a choice rather than explaining the apprentice's feelings.
- Action / playability / internal-to-observable: PASS. Slow cleaning, retying the apron, sitting, touching clay, and beginning work translate the supplied inner state into observable action.
- Turn / state / entry / exit: PASS. Repair begins; the scene stops at the first meaningful action.
- Fact / knowledge integrity, role boundary, language, canonical contract: PASS. No acting-method or micro-expression system is introduced.

## F06 — Subtext

Rating: `FAIL — BLOCKING RUNTIME OUTPUT FAILURE`

- Runtime result: `FAIL_SAFE / MALFORMED_EXECUTOR_OUTPUT` because `control_data.diagnosis_summary` did not satisfy the non-empty output-language validation.
- No accepted Scene deliverable reached Runtime or verifier; subtext, fact integrity, knowledge integrity, and role boundary cannot be semantically accepted from the retained envelope.
- Assignment / authority / language / canonical contract: the request was correctly bound to the canonical Skill, but the generated response was unusable at the Runtime output layer.
- Verifier: not invoked. The rejected underlying provider content is not retained by the frozen evidence path; no resample is permitted.

## F07 — Exposition Through Dramatic Action

Rating: `PASS`

- Assignment / authority fidelity: PASS. The notice, B-building relocation, unknown reason, and two-person scope are respected.
- Information handling: PASS. The notice is discovered, shown, questioned, and converted into a joint action rather than recited as shared background.
- Objective / resistance / action / dialogue: PASS. Chen Xun's objection becomes the condition to move the prop box together.
- Turn / state / entry / exit: PASS. Acceptance of the relocation becomes a plan to pack the box.
- Fact / knowledge integrity, role boundary, language, canonical contract: PASS.

## F08 — Assignment Fact Integrity

Rating: `PASS`

- Assignment / authority fidelity: PASS. The absence reason remains unspoken and unknown; limited capacity is not turned into ranking or authority.
- Scene Function / Objective / Resistance / dialogue: PASS. A replacement request meets a material-transfer condition.
- Turn / state / entry / exit: PASS. Conditional agreement and tonight's materials obligation are clear.
- Fact / knowledge integrity: PASS. No cause, knowledge source, relationship history, precise deadline, or external authorization is introduced.
- Role boundary / output language / canonical contract: PASS.
- Verifier: `PASS`, correctly a true negative in this fixture.

## F09 — Character Knowledge Integrity

Rating: `FAIL — BLOCKING STATE / INFORMATION-HANDLING FAILURE`

- Assignment / knowledge fidelity: PASS for the core distinction: Gu Qing knows the rejection; Yue Lin does not know it until the notice is handed over; the reason remains unknown.
- Scene Function / Objective / reaction: PASS. The folded notice and delayed handoff are playable.
- Information handling / turn / state / exit: FAIL. Yue Lin opens and reads the notice, then says `先让我看看`; that request occurs after the action it requests. The intended state change is therefore temporally incoherent.
- Fact integrity / role boundary / language / canonical contract: PASS.
- Verifier: `PASS`; no integrity classification was required, but the pass does not establish coherent information staging.

## F10 — Targeted REVISE

Rating: `FAIL — BLOCKING FACT INTEGRITY`

- Local-revision function: PASS. The response keeps the tea room, two colleagues, request, and conditional acceptance; it adds resistance and a turn.
- Assignment fidelity: FAIL. `午休前我得去趟行政那边` and a possible late return create unprovided plans, an external administrative commitment, and a twenty-minute coverage obligation.
- Fact / knowledge integrity: FAIL — unsupported temporal, resource, and authority-adjacent micro-facts beyond the stated repair target.
- Turn / entry / exit / language / canonical contract: otherwise PASS.
- Verifier: `PASS`; human finding is `VERIFIER FALSE NEGATIVE`.

## F11 — NO_MATERIAL_CHANGE

Rating: `FAIL — BLOCKING RUNTIME OUTPUT FAILURE`

- Runtime result: `FAIL_SAFE / MALFORMED_EXECUTOR_OUTPUT`; `NO_MATERIAL_CHANGE` carried a creative rewrite or omitted `material_rewrite_claimed=false`.
- The required non-mechanical revision ceiling is therefore not demonstrated.
- No accepted deliverable reached verifier; semantic scene, fact, knowledge, and role review are not assessable.

## F12 — DIAGNOSE

Rating: `FAIL — BLOCKING RUNTIME OUTPUT FAILURE`

- Runtime result: `FAIL_SAFE / MALFORMED_EXECUTOR_OUTPUT / Creative deliverable kind is invalid`.
- The requested diagnostic-only behavior cannot be accepted; the Run did not establish that DIAGNOSE can diagnose Scene Function / Resistance / Turn without producing a replacement Scene.
- Verifier was not invoked; no resample is authorised.

## F13-A — Material Context Missing

Rating: `FAIL — BLOCKING CONTEXT-BOUNDARY FAILURE`

- Expected result: `NEEDS_CONTEXT` without invented people, relationship, event, location, or outcome.
- Runtime result: `FAIL_SAFE / MALFORMED_EXECUTOR_OUTPUT / Creative deliverable content must be a non-empty string`.
- Context sufficiency cannot be accepted: the required lawful `NEEDS_CONTEXT` payload did not reach an accepted Runtime result. No verifier result is available.

## F13-B — Upstream Canon Decision

Rating: `FAIL — BLOCKING UPSTREAM-BOUNDARY FAILURE`

- Expected result: `UPSTREAM_DECISION_REQUIRED` with the required upstream decision field and canonical handoff.
- Runtime result: `FAIL_SAFE / MALFORMED_EXECUTOR_OUTPUT / UPSTREAM_DECISION_REQUIRED requires upstream_decision_needed`.
- The model may have selected the right high-level state, but its Runtime-valid upstream packet was not demonstrated. No authority expansion is accepted, and no verifier result is available.

## F14 — Production / Role Boundary

Rating: `FAIL — BLOCKING FACT INTEGRITY`

- Role boundary: PASS. The scene does not decide lens, coverage, budget, schedule, acting method, micro-expression system, or AI production schema. Relevant Director, Character & Acting, and Production handoffs preserve boundaries.
- Scene Function / Action / Turn: PASS. The two guards see the unlatched door, decide not to enter, and notify the responsible person.
- Fact integrity: FAIL. Control data states that wet ground `可能增加进入风险`; the Assignment supplies wet ground but no safety-causal fact. This turns a production-burden observation into a new in-world causal risk.
- Knowledge / language / canonical contract: PASS.
- Verifier: `PASS`; human finding is `VERIFIER FALSE NEGATIVE`.

## Rating Summary

| Rating | Fixtures |
|---|---|
| PASS | F04, F05, F07, F08 |
| PASS WITH OBSERVATION | F01, F02 |
| FAIL | F03, F06, F09, F10, F11, F12, F13-A, F13-B, F14 |

All failures are blocking for Human Acceptance in this V0.1 validation.
