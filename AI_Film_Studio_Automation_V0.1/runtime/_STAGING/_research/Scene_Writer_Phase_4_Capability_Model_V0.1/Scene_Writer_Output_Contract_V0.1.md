---
type: output-contract-draft
status: passed-awaiting-human-review
version: 0.1
role: Scene Writer
runtime_implementation: none
---

# Scene Writer Output Contract V0.1

## Creative Deliverable vs Control Data

|Channel|Contains|Must not contain|
|---|---|---|
|Creative Scene Deliverable|Scene text or a scoped revision; action/dialogue needed by the requested scene form.|Mandatory visible reasoning table, final shot plan, performance blueprint, QA score, budget, or production schedule.|
|Internal Control Data|Assignment/Canon lock summary, scene purpose, participant objectives, resistance, before/after state, turn/entry/exit rationale, rule hits, unresolved questions, handoffs, flags, and decision state.|Private chain-of-thought or speculative project facts.|
|Downstream Package|Only decision-relevant scene facts: approved action/spatial/object/timing needs, state change, unresolved locks, production flags, and eligible handoffs.|Automatic downstream calls or another role’s final decisions.|

## Output Fields by Need

|Field|When emitted|
|---|---|
|scene_text / scoped_revision|For `SCENE_CREATED` or `SCENE_REVISED`; omitted in pure diagnosis/block/no-change unless explicitly requested.|
|scene_purpose, objectives, resistance, before_state, state_change, after_state|Compact control summary when relevant to output/revision/debugging.|
|entry_rationale / exit_rationale|Only when entry/exit was evaluated or changed.|
|production_burden_flags / dramatic-value locks|Only when D19–D21 trigger a production review question.|
|unresolved_questions / upstream_handoff|When required context or authority decision prevents safe completion.|
|shared_qa_handoff_eligible|When a language/voice-level check is requested after scene material is available.|
|downstream_notes|Only facts needed for later roles; never final Director, Acting, Production, or QA decisions.|

## Metadata Overload Safety

Control data serves review, debugging, and later continuity work. It must stay proportional to the task and remain separable from normal readable scene material. A final viewer/writer-facing scene is never converted into “70% metadata, 30% script.”

