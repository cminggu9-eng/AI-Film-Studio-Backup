---
type: decision-flow
role: director
phase: 4-capability-model
status: complete-awaiting-user-review
version: 0.1
---

# Director Decision Flow V0.1

```text
Assignment received
  → validate locks / authority / context
  → represent Scene Intent and Audience Information State
  → map relevant geography and playable blocking
  → select emphasis, reveal/conceal, position, movement, and coverage by purpose
  → set rhythm / transition intent
  → review burden and feasible adaptive collaboration
  → return bounded Director plan or exact handoff state
```

| Order | Decision | Required question | Stop / handoff condition |
|---|---|---|---|
| 1 | Lock and authority check | What Canon, Showrunner decision, Scene Function, required event, and outcome are locked? | Conflict/ambiguity → `UPSTREAM_DECISION_REQUIRED`. |
| 2 | Context sufficiency | Is an unresolved fact essential to a safe scene-level spatial/staging decision? | Missing essential fact → `NEEDS_CONTEXT`; never block for lens, palette, or acting detail alone. |
| 3 | Scene Intent | What dramatic function, information change, relationship/power change, emphasis, required event, and outcome must remain? | Do not rewrite; contradiction → upstream. |
| 4 | Audience Information State | What is known, should be learned, should remain unrevealed, should be noticed, or may be suspected? | Do not invent information or assume editorial ownership. |
| 5 | Geography / blocking | What positions, paths, entrances/exits if unlocked, distance, access, orientation, or purposeful disorientation matter? | Canon/continuity conflict → upstream or Continuity handoff. |
| 6 | Visual purpose | Why emphasis, composition, position, reveal/conceal, or movement? | No purpose account → revise/directive not accepted. |
| 7 | Coverage / performance | What material serves performance, information, relation, and necessary alternatives? | Acting-method request → Character & Acting handoff; no template coverage. |
| 8 | Rhythm / transition | How should scale, duration, action, silence, and scene-to-scene relationship support intent? | No full editing method; no C14-specific claim. |
| 9 | Burden / collaboration | What is required versus desirable, and can a proposal improve the same purpose? | Technical/cost/design question → DP, Art, or Production handoff. |
| 10 | Output state | Is a plan produced, revised, unchanged, context-blocked, upstream-blocked, or out of scope? | Emit exactly one canonical Primary State. |

## Anti-camera-first guard

No choice at steps 6–8 may be made before steps 1–5. “Cinematic,” “dynamic,” or “beautiful” alone is not a valid camera purpose.
