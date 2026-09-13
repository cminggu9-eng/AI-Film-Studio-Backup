---
type: scene-state-model-draft
status: draft-for-human-review
version: 0.1
role: Scene Writer
provenance: AI-FILM-STUDIO-SYNTHESIS
not_a_capability_model: true
---

# Scene Writer Scene State Model Draft V0.1

> **Draft-only status:** This is a cross-distillation thinking aid. It is not a formal Capability Model, schema, router, executor contract, or instruction to generate a complete scene.

## Working Sequence

```text
Scene Before State
  → Character Action
  → Resistance
  → Escalation / Discovery / Choice
  → State Change
  → Exit Condition
```

|Element|Question it asks|Source-method basis|Permitted output|Must not become|
|---|---|---|---|---|
|Scene Before State|What prior relation, information, pressure, or condition enters this scene?|D14, D17|A bounded scene context and first effective dramatic information.|A replacement for Showrunner premise, Canon, episode objective, or arc destination.|
|Character Action|What does a participant currently attempt, avoid, protect, obtain, hide, test, exchange, or decide?|D06, D09, D12, D15|Playable action and dialogue need at narrative level.|An invented macro goal, final acting tactic, or language/voice score.|
|Resistance|What prevents straightforward achievement—another aim, information, timing, environment, consequence, or condition?|D06, D09|Scene-facing obstacle/pressure.|A mandatory argument, fight, or newly invented conflict.|
|Escalation / Discovery / Choice|What happens that can alter present pressure or the audience’s working inference?|D04, D14, D15|Visible/hearable event, relevant discovery, escalation, or choice.|A required “big reversal” or a universal reveal taxonomy.|
|State Change|What is different at the relevant level—access, information, plan, relation, obligation, pressure, or commitment?|D02, D14, D15|A modest or major changed state tied to action where applicable.|A false positive/negative flip or a story-direction rewrite.|
|Exit Condition|What must remain long enough for function, changed pressure, or aftermath to land?|D16, D18|Contextual end point and any retained aftermath.|An automatic early exit or final edit-rhythm decision.|

## Operating Conditions

1. The sequence is diagnostic, not a mandatory six-beat template. A quiet scene may use a sparse action and a modest state change; a necessary aftermath may legitimately remain after a change.
2. **Resistance is not synonymous with argument.** The resisting force can be social, temporal, environmental, informational, relational, or internal only when it has a playable carrier.
3. **State change is not necessarily a reversal.** It can be a choice, a changed pressure, a new constraint, a relation movement, or an audience inference shift.
4. A supplied Showrunner decision remains supplied. If a required transition would change locked story facts, return `NEEDS CONTEXT`, `HANDOFF`, or `BLOCK`.
5. The model does not decide camera, lens, coverage, staging, edit rhythm, performance micro-detail, production budget, or AI-production constraints.

## Minimum Evidence for a Scene-State Claim

For any model element asserted as part of scene material, provide the smallest suitable carrier:

- an observable/hearable action or event;
- active dialogue/subtext with legible relation;
- a relevant clue or information delivery;
- a choice, consequence, or altered behaviour; or
- a separately approved narration/interior device.

If no carrier exists and no authorised form permits it, the claim is a candidate for the Unshootable Language Taxonomy—not an automatic deletion order.

