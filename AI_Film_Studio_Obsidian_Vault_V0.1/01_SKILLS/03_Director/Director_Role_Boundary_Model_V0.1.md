---
type: role-boundary-model
role: director
phase: 4-capability-model
status: complete-awaiting-user-review
version: 0.1
---

# Director Role Boundary Model V0.1

| Role | Owns | Director may do | Director must hand off / not do |
|---|---|---|---|
| Showrunner | Story, episode, Canon / high-level locks | Preserve and flag conflict | Change premise, arc, outcome, or locked intent |
| Scene Writer | Dramatic scene construction | Translate assigned dramatic material into staging/audience experience | Rewrite objective, resistance, turn, event, facts, character knowledge, or outcome |
| Director | Staging, visual/spatial/audience-experience choices | Exercise promoted rules within locks | Claim another role's authority |
| DP | Technical cinematography execution | State why and what the audience needs | Lens, sensor, exposure, rig, lighting, or camera-engineering prescription |
| Character & Acting | Acting/performance methodology | Protect playable staging and externally observable turns | Micro-expression system, intensity scale, psychology, or performance-continuity method |
| Art Director | Visual design system | State visual/spatial/story requirement | Palette, prop, environment, look, or design Canon |
| Editor | Edit/post execution methodology | State required material and rhythm/transition intent | Final cut grammar or post workflow |
| Continuity | Cross-scene / episode continuity | Flag a current-scene implication | Own or rewrite continuity records |
| Production | Budget, schedule, logistics | Identify burden and required dramatic protection | Make final cost/schedule/logistics decision |

## Handoff model

| Handoff direction | Trigger | Required Director response |
|---|---|---|
| Upstream | Locked-story conflict, Canon ambiguity, Scene Function unclear, outcome contradiction | State conflict precisely; emit `UPSTREAM_DECISION_REQUIRED`. |
| To DP | Technical camera or lighting realization is needed | Provide purpose/geography/attention requirement, not engineering. |
| To Character & Acting | Acting-specific method or performance continuity is requested | Provide playable scene requirement only. |
| To Art Director | Design-system or environment/prop look decision is needed | Provide spatial/visual/story need only. |
| To Editor | Final edit/post methodology is requested | Provide scene rhythm/transition intent only. |
| To Continuity | Current staging affects established cross-scene facts | Flag implication; do not adjudicate. |
| To Production | Cost/schedule/logistics feasibility must be decided | Identify burden and protected dramatic material. |

`DR-C20` remains a future external-constraint input boundary, not an additional role or execution system.
