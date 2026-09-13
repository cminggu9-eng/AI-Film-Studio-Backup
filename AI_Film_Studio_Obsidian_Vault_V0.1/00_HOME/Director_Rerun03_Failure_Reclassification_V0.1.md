---
type: director-rerun03-failure-reclassification
status: complete-awaiting-user-review
version: 0.1
date: 2026-08-28
---

# Director Rerun 03 Failure Reclassification V0.1

## Correction / Reclassification Note

The original immutable Rerun 03 validation record remains unchanged:

```text
category: ROLE SEMANTIC FAILURE
detail: Required role-output heading is missing
```

That classification is superseded for analytical and future-gate purposes by:

```text
MIXED STRUCTURAL + TRANSPORT FAILURE
```

## Evidence

- The raw Director response is complete, JSON-valid, persisted before local validation, and not truncated.
- It contains substantive Directorial Intent, Staging / Blocking, Audience Information, Spatial Geography, Camera / Coverage Intent, Rhythm / Transition Intent, Production Burden, and Handoffs / Unresolved Issues.
- It preserves `DIRECTION_PLAN_PRODUCED`, `ABSENT` flags/handoffs, received Canon locks, and prohibitions.
- It violates the canonical heading order by placing `SPATIAL GEOGRAPHY` before `AUDIENCE INFORMATION`.
- The historical parser also demanded non-canonical title-case variants and lacked two canonical heading requirements.

Therefore the failure was neither an absent Director deliverable nor a missing Director semantic field. It combined a real canonical structural ordering defect with an independent historical parser-contract defect. No original Rerun 03 artifact was deleted, overwritten, or rewritten.
