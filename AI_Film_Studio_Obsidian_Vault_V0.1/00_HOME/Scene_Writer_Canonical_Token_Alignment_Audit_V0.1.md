# Scene Writer Canonical Token Alignment Audit V0.1

## Source of truth

Read-only source: `01_SKILLS/02_Scene_Writer/scene-writer/SKILL.md`, **Exact Output Contract**.

### Primary Decision States

1. `SCENE_CREATED`
2. `SCENE_REVISED`
3. `NO_MATERIAL_CHANGE`
4. `NEEDS_CONTEXT`
5. `UPSTREAM_DECISION_REQUIRED`
6. `REQUEST_OUT_OF_SCOPE`

### Orthogonal Flags / Handoffs

`PRODUCTION_REVIEW_REQUIRED`, `UPSTREAM_HANDOFF_REQUIRED`, `SHARED_QA_HANDOFF_ELIGIBLE`, `DIRECTOR_HANDOFF_ELIGIBLE`, `CHARACTER_ACTING_HANDOFF_ELIGIBLE`, `EXTERNAL_PRODUCTION_CONSTRAINT_DEFERRED`, `EXTERNAL_PRODUCTION_CONSTRAINT_RECEIVED`.

## Repair

| Surface | Before | After |
| --- | --- | --- |
| `control.outcome` enum | included non-canonical `NEEDS_DECISION` | exact six canonical Primary Decision States |
| `control.flags` arrays | arbitrary strings | exact canonical token enum items |
| `control.handoffs` arrays | arbitrary strings | exact canonical token enum items |
| `ABSENT` | transport absence representation | unchanged; not added to canonical output semantics |
| E2E-INT-12 | compared primary state only | compares source mode, primary state, flags, and handoffs exactly |

Provider strict schema supports enum values inside array `items`; therefore the restriction is encoded directly in the strict schema. The existing deterministic integration gate also rejects non-canonical Scene Writer flags/handoffs.

## Integrity

Canonical `scene-writer/SKILL.md` was read but not modified. SHA-256 remains `93E1BE12988F8CAA6CDD76ACB5E6C1BF6AD3CA0DFF5806A2EA93511E66052DFB`.
