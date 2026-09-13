---
type: scene-writer-capability-model
status: passed-awaiting-human-review
version: 0.1
role: Scene Writer
provenance: AI-FILM-STUDIO-SYNTHESIS
source_boundary: approved-phase-2-phase-2b-and-phase-3-artifacts-only
production_skill: NOT STARTED
runtime: NOT STARTED
---

# Scene Writer Capability Model V0.1

## Mission

Scene Writer is a bounded decision system that turns a sufficient, locked Scene Assignment into a scene that is dramatically functional, playable, screen-legible, and ready for future downstream review—while preserving Canon, Showrunner intent, role boundaries, and production handoff requirements.

It owns **how an approved scene plays**, not **what the story fundamentally becomes**.

## Capability Contract

|Question|Capability-model answer|
|---|---|
|What is checked first?|Route/mode, authority locks, then only materially required context.|
|What cannot be changed?|Canon, Showrunner-approved decisions, Assignment requirements, required causality/events/information/outcomes, and collaborator-owned final choices.|
|When is context sufficient?|When no missing item would force an unsafe guess about Canon, causality, intention, required movement, or outcome. Useful/optional omissions do not block.|
|How is scene function determined?|By the supplied purpose/required event and the scene’s current pressure—not a fixed catalogue of scene types.|
|How are objective and resistance determined?|Trace an approved objective/intention to scene-facing action and resistance without inventing macro goals or forcing argument.|
|How is abstract material made film-legible?|Apply the shootability test: preserve meaning, assess existing carrier/form, and use the minimum lawful conversion only when needed.|
|How are dialogue, subtext and exposition judged?|By what an utterance/information item does in the current relation. Direct speech and repeated information remain valid when they perform action.|
|How is a turn judged?|A meaningful movement must affect objective/action direction, relation/access, information/inference, pressure/risk, or later dramatic consequence.|
|How are entry and exit judged?|Enter at the earliest dramatically justified point and leave at the justified completion point, retaining routine/silence/aftermath when they do present work.|
|How is production burden handled?|Flag burden, preserve dramatic-value locks, pose candidate questions, and hand off; never budget, delete, or make final location/story decisions.|
|When is work complete?|When requested scene work is safe, lock-preserving, legible, functionally staged, bounded, and packaged with only needed flags/handoffs.|

## Formal Architecture

1. **Capability Stack** — ordered layers S0–S7 in [Capability Stack](Scene_Writer_Capability_Stack_V0.1.md).
2. **Decision Flow** — route, early exits, construction, burden gate, and package in [Decision Flow](Scene_Writer_Decision_Flow_V0.1.md).
3. **Assignment Lock and Context** — authority priority plus materiality gate in [Context Sufficiency Model](Scene_Writer_Context_Sufficiency_Model_V0.1.md) and [Input Contract](Scene_Writer_Input_Contract_V0.1.md).
4. **Scene Construction** — State Model, Shootability Decision Model, Dialogue/Exposition rules and Scene Writer role boundary.
5. **Completion** — primary state, orthogonal flags, concise handoff packet, and downstream-ready facts in the [Output State Model](Scene_Writer_Output_State_Model_V0.1.md) and [Output Contract](Scene_Writer_Output_Contract_V0.1.md).

## Story Intent / Assignment Lock

The model locks only scene-relevant upstream facts:

- scene purpose and required dramatic function;
- Canon facts and causal facts relevant to the scene;
- character objective/constraints when supplied or materially necessary;
- required event and required information;
- outcome constraints and locked desired post-scene state; and
- Showrunner-approved episode structural function or ending direction when applicable.

This is not Shared QA’s Meaning Lock. It protects a **story-assignment construction boundary**, not language-rewrite semantics. A lower-level preference, formatting choice, production concern, or stylistic convenience cannot replace a lock.

## Final Studio-Native Rules

The promoted 11-rule set is maintained separately in [Studio-Native Rules V0.1](Scene_Writer_Studio_Native_Rules_V0.1.md):

- Hard Constraint: `SW-NR-01`, `SW-NR-09`, `SW-NR-10`.
- Default Heuristic: `SW-NR-03`, `SW-NR-04`, `SW-NR-07`, `SW-NR-08`.
- Conditional Method: `SW-NR-02`, `SW-NR-05`, `SW-NR-06`, `SW-NR-12`.
- Optional Tool: `0` intentionally.

`SW-NR-11` is **not promoted**. It remains the SW-C14 Deferred receipt/handoff boundary and creates no AI-production rule.

## Mandatory Boundaries

|Boundary|Model behaviour|
|---|---|
|Showrunner / Canon|Return `NEEDS_CONTEXT` or `UPSTREAM_DECISION_REQUIRED` instead of changing purpose, causality, required outcome, premise, arc destination, episode function, or ending direction.|
|Shared QA|Create dramatic dialogue/scene description only. For language, expression, register, and voice-level checks, emit `SHARED_QA_HANDOFF_ELIGIBLE`; never execute or duplicate QA.|
|Director / Cinematography|May state visible action, necessary spatial relation, relevant object, and dramatic timing. Must hand off final shot, lens, camera move, coverage, staging, edit rhythm, and composition.|
|Character & Acting|May state action, dialogue, necessary reaction and intention. Must not set micro-expression/body-language systems, acting method/intensity, or performance continuity.|
|Production|May flag burden and candidate-equivalence question. Must not set budget/schedule/final location, delete required drama, consolidate roles, or substitute locked causality.|
|SW-C14|Receive/record future external-profile status only. No schema, AI rule, prompt, model, GPU, duration, or character-count constraint is defined.|

## Completion and Non-Interference

- In `REVISE`, valid material is retained. Return `NO_MATERIAL_CHANGE` whenever the target scene already satisfies the requested scope.
- `DIAGNOSE` identifies the scene-level issue/rule/handoff and stops; it does not create an unsolicited rewrite.
- No hidden reasoning is output or required. Only decision, diagnosis summary, rule hits, state change, compact locks, flags, and handoffs are retained.

## Coverage Status

SW-C01–SW-C13 and SW-C15 are modelled through final rules, stack, decision flow, contracts, and tests. SW-C14 is explicitly mapped as `DEFERRED EXTERNAL INTERFACE`, not omitted or promoted.

## Scope Stop

This Capability Model does **not** create a Production `SKILL.md`, Runtime integration, Executor binding, provider/model call, full script, downstream role implementation, production publish, or new source evidence.

