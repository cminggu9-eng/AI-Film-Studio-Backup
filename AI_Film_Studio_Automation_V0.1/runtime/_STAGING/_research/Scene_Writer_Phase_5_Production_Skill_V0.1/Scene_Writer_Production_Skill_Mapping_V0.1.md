---
type: production-skill-mapping-audit
status: passed
version: 0.1
canonical_skill: scene-writer
---

# Scene Writer Production Skill Mapping V0.1

## Package Map

|Package element|Purpose|
|---|---|
|`scene-writer/SKILL.md`|The complete minimal executable protocol; it does not require Phase 1–4 documents at execution time.|
|This mapping audit|Trace verification only; not a runtime dependency.|

## Capability Mapping

|Capability|SKILL.md behaviour anchor|Status|
|---|---|---|
|SW-C01 Shootability|`Scene Construction Protocol > Shootability and Internal State`; exact carrier test.|Mapped|
|SW-C02 Tell → Show|Same section; minimum conversion, no keyword blacklist.|Mapped|
|SW-C03 Scene Objective|`Function, State, Objective, Resistance` and Assignment Intake.|Mapped|
|SW-C04 Conflict / Resistance|Same section; non-argument resistance allowed.|Mapped|
|SW-C05 Scene Turn|Meaningful-turn benefit test.|Mapped|
|SW-C06 Scene End Point|Entry and Exit > justified completion point.|Mapped|
|SW-C07 Dialogue Function|Dialogue as present dramatic action.|Mapped|
|SW-C08 Subtext|Dialogue section; conditional, inferable subtext only.|Mapped|
|SW-C09 Information Delivery|Action/dialogue/both allocation and functional exposition.|Mapped|
|SW-C10 Internal → Actable Behaviour|Approved carrier list with minimum conversion guard.|Mapped|
|SW-C11 Scene Entry|Earliest dramatically justified point.|Mapped|
|SW-C12 Scene Exit|Justified completion point with retained aftermath.|Mapped|
|SW-C13 Production Cost Awareness|Production Burden Gate and Dramatic Value Preservation.|Mapped|
|SW-C14 AI Production Friendliness|External Production Constraint boundary only; receipt/Deferred/handoff, no implementation.|Mapped as Deferred Interface|
|SW-C15 Character Voice Boundary|Shared QA and Character & Acting boundary rows.|Mapped|

## Method and Rule Mapping

|Trace group|SKILL.md section|Result|
|---|---|---|
|D01–D05|Shootability and Internal State.|Mapped|
|D06, D09, D14–D15|Function, State, Objective, Resistance; Meaningful Turn.|Mapped|
|D07, D10–D13|Dialogue, Subtext, and Information; role boundaries.|Mapped|
|D16–D18|Entry and Exit.|Mapped|
|D19–D21|Production Burden Gate.|Mapped|
|D03, D08|Role Boundaries; no final technical implementation.|Mapped|
|Final Rules NR-01–10, NR-12|Authority Lock, Construction Protocol, Role Boundaries, and Exact Output Contract.|`11 / 11 mapped`|

Detailed method trace is preserved in the Phase 4 Capability Traceability Matrix; no source method text is duplicated into the Production Skill.

## Per-Method Behaviour Trace

|Method|Production Skill behaviour|
|---|---|
|D01|Shootability field/meaning/carrier check.|
|D02|Split only at actual significant action change.|
|D03|Retain narrative need; do not claim final technical direction.|
|D04|Require an encounterable scene event/carrier.|
|D05|Use minimum sufficient internal-state externalisation when needed.|
|D06|Trace supplied objective to scene-facing resistance; do not invent goal.|
|D07|Allocate information to action, dialogue, or both.|
|D08|Keep early/spec-style form distinct from final visual authority.|
|D09|Write dialogue as current pressure/competing will, not required argument.|
|D10|Use subtext only when inferable and playable.|
|D11|Deliver relevant clues/information without dump or confusion.|
|D12|Use contextual speech pressure without voice imitation.|
|D13|Leave performable space; defer final acting.|
|D14|State supplied scene function and meaningful effect.|
|D15|Let approved action/choice carry meaningful state movement.|
|D16|Use beginning/end anchors only as optional planning help.|
|D17|Select earliest dramatically justified entry.|
|D18|Select justified exit with retained aftermath when dramatic.|
|D19|Flag production burden; do not delete or budget.|
|D20|Create bounded production handoff packet.|
|D21|Pose location-equivalence question; never select final solution.|

**SW-D traceability result: `21 / 21 mapped`.**

## Modes, States, Flags, and Handoffs

|Contract element|SKILL.md section|Exactness result|
|---|---|---|
|Modes `CREATE`, `REVISE`, `DIAGNOSE`|Modes table|`3 / 3 exact`; no fourth mode.|
|Primary states|Exact Output Contract|`6 / 6 exact`.|
|Orthogonal flags / handoffs|Exact Output Contract and Handoff Packet|`7 / 7 exact`; not encoded as competing primary states.|
|Input / output separation|Assignment Intake and Exact Output Contract|Mapped; creative scene remains readable and control data stays separate.|
