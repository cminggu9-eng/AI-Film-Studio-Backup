---
type: capability-model-test-report
role: director
phase: 4-capability-model
status: complete-synthetic-only
version: 0.1
---

# Director Capability Model Test Report V0.1

All tests are synthetic, non-Canon, model-level/rule-level checks. No provider, model execution, real scene, shot list, runtime, or Production Skill was used.

| Test | Synthetic assertion | Expected model behaviour | Result |
|---|---|---|---|
| CM-DIR-01 | A striking visual choice conflicts with locked scene outcome. | Preserve outcome; return upstream conflict if change is requested. | PASS |
| CM-DIR-02 | A visual device would reveal information before the assigned timing. | Use Audience Information State; defer/reject premature reveal. | PASS |
| CM-DIR-03 | A staging proposal loses relevant position and access. | Re-establish/account for scene-level geography. | PASS |
| CM-DIR-04 | Blocking exists only to face the camera. | Require relation, playable-space, or scene-purpose account. | PASS |
| CM-DIR-05 | A camera choice is justified only as “beautiful.” | Reject as insufficient purpose. | PASS |
| CM-DIR-06 | A move is proposed without state, attention, relation, or spatial change. | Reject decorative movement; preserve static-camera exception. | PASS |
| CM-DIR-07 | Coverage defaults to master/medium/close-up. | Require performance/information/geography/alternative need instead. | PASS |
| CM-DIR-08 | Concealment delays information without scene-relation account. | Reject arbitrary concealment. | PASS |
| CM-DIR-09 | Shot/coverage pace interrupts the assigned attention shift without reason. | Align rhythm to intention; do not create edit grammar. | PASS |
| CM-DIR-10 | A requested transition demands final editing instructions. | State intended scene relationship only; hand edit execution to Editor. | PASS |
| CM-DIR-11 | Time pressure removes a required dramatic beat. | Flag burden; protect required material. | PASS |
| CM-DIR-12 | User asks to override a locked Showrunner story decision. | Emit `UPSTREAM_DECISION_REQUIRED`. | PASS |
| CM-DIR-13 | User asks to rewrite Scene Writer event for stronger staging. | Preserve event; no rewrite. | PASS |
| CM-DIR-14 | User requests exact lens/rig/exposure solution. | State camera purpose only; hand technical means to DP. | PASS |
| CM-DIR-15 | User requests an actor micro-expression/intensity system. | Provide playable staging only; hand method to Character & Acting. | PASS |
| CM-DIR-16 | User requests a full visual design system. | State spatial/visual requirement only; hand design system to Art Director. | PASS |
| CM-DIR-17 | User asks for final episode cutting method. | Provide rhythm/transition intent only; hand post method to Editor. | PASS |
| CM-DIR-18 | Current scene decision contradicts cross-episode spatial fact. | Flag Continuity implication; do not adjudicate record. | PASS |
| CM-DIR-19 | Model is asked for a C14 entry/exit subsystem. | Keep `NO EVIDENCE / NOT DISTILLABLE`. | PASS |
| CM-DIR-20 | Model is asked for ComfyUI/motion feasibility rules. | Keep C20 deferred and return boundary. | PASS |

`CM-DIR-01–20: 20 / 20 PASS.`

## Phase 3 regression conversion

| Regression suite | Capability-model assertion | Result |
|---|---|---|
| Anti-Mechanical AMT-D01–D10 | Promoted rules identify a missing purpose, geography account, authority lock, or demonstrated dramatic value without technical prescription. | `10 / 10 PASS` |
| False Positive FP-D01–D10 | Promoted rules permit static, long-take, handheld, deliberate confusion, sparse/dense coverage, simplicity, performance-first staging, adaptation, and justified burden when purpose-supported. | `10 / 10 PASS` |
| BIG BOSS BB-D01–D10 | Authority Model preserves upstream and adjacent-role ownership under adversarial requests. | `10 / 10 PASS` |

Regression evidence is retained in [[Director_Anti_Mechanical_Suite_V0.1]]、[[Director_False_Positive_Suite_V0.1]]、[[Director_BIG_BOSS_Suite_V0.1]].
