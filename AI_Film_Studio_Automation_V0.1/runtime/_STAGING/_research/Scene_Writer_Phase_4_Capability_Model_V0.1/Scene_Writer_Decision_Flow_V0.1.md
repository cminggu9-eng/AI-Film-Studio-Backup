---
type: decision-flow
status: passed-awaiting-human-review
version: 0.1
role: Scene Writer
---

# Scene Writer Decision Flow V0.1

```text
INPUT
  ↓
S0 Route / Mode
  ├─ outside Scene Writer remit → BOUNDARY HANDOFF
  ↓
S1 Authority and Assignment Lock
  ├─ lock conflict → UPSTREAM_DECISION_REQUIRED
  ↓
S2 Context Sufficiency
  ├─ material missing requirement → NEEDS_CONTEXT
  ↓
S3 Function + Before State + Objective + Resistance
  ├─ REVISE and no scoped material defect → NO_MATERIAL_CHANGE
  ↓
S4 Shootability + Action / Dialogue / Information Construction
  ├─ form/Canon/performance/camera/language issue → appropriate HANDOFF
  ↓
S5 State Change / Turn + Entry / Exit
  ↓
S6 Production Burden Gate
  ├─ burden / availability issue → PRODUCTION_REVIEW_REQUIRED flag
  ├─ proposed trade-off touches a lock → UPSTREAM_DECISION_REQUIRED
  ↓
S7 Final Safety / Authority Check
  ↓
OUTPUT + orthogonal flags + downstream package
```

## Decision Guardrails

- `NEEDS_CONTEXT` is allowed only when the missing item materially changes Canon, causality, character intention, required state movement, or required outcome. Missing useful/optional detail continues with disclosed assumptions where appropriate.
- A scene turn passes only if it affects at least one relevant dimension: objective/action direction, relationship/access, information/working inference, pressure/risk, or later dramatic consequence. A mere event is not automatically a turn; a quiet choice can be.
- Production review is a flag/handoff, not a final state that blocks otherwise valid story work unless a real constraint conflicts with a lock.
- A final creative deliverable contains scene material; control data stays concise and need-to-know. The flow never requires private chain-of-thought.

