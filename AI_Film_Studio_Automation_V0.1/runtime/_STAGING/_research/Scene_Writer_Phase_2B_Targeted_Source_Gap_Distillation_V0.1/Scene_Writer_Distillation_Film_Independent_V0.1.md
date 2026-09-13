---
type: targeted-single-source-distillation
status: passed
version: 0.1
source_group: Film Independent official production resources
source_evidence: E-FI-01,E-FI-02
method_range: SW-D19-SW-D21
scope: production-cost-awareness-only
---

# Scene Writer Distillation — Film Independent V0.1

## A. Source Scope

**Actually read:** Film Independent’s public articles *Shooting on Location? How To Save Yourself Money and Headaches* and *Making Your Cinematic Dream Come True for $200k*. Read passages cover early script/location review, location-manager value, multiple locations in one, examples of expensive production elements, early budget/schedule work, and travel/lodging trade-offs.

**Not read or transferred:** the *Get Low* case study as a general method, generic low-budget folklore, third-party budget advice, cost estimates, character-combination theory, arbitrary cast/location caps, decision rights to delete scenes, or AI-production guidance.

**Evidence boundary:** the sources are independent-production education pieces, including one low-budget context. They support recognition, early consultation and contextual location trade-offs—not a universal instruction to make every story cheaper.

## B. Primary Contributions

- Certain elements can carry a comparatively high production burden in low-budget contexts: complex action, children/animals, extras, and exterior nights.
- Budget and schedule expertise belongs early in pre-production, alongside early investigation of locations and other production requirements.
- A location manager can find cost-saving locations and sometimes combine multiple location needs; one source explicitly requires weighing lower location fees against travel/lodging expense.
- Script material can be reviewed early for practical location implications, but the sources do not assign final creative deletion authority to Scene Writer.

## C. Distilled Methods

### SW-D19 — Production-Burden Flag

- **Capability Name:** Production-Burden Flag
- **Problem It Solves:** A scene’s production implications remain invisible until scheduling or budgeting, when alternatives are more expensive to evaluate.
- **Trigger / Detection:** The scene includes production-burden signals such as complex action, large extras/crowd demand, children/animals, exterior night, or location requirements that need special preparation.
- **Decision Principle:** Surface the burden as a scene-level flag for production review. Presence of a signal is not a command to remove it, and the source examples are explicitly context-sensitive to low-budget independent work.
- **Action / Transformation:** Record the element, its apparent dramatic function, and the production question it raises; route it to a future Production Constraint Profile / producer or line-producer review.
- **Stop Condition:** Stop after the flag and question are clear; Scene Writer may not make a final budget, schedule, or story-deletion decision.
- **Failure Risk:** Treating “expensive” as “bad,” applying a $200k-project example universally, or stripping a scene’s necessary dramatic action.
- **Classification:** `Conditional Method`.
- **Source Trace:** E-FI-02, “Making Your Cinematic Dream Come True for $200k”, “Choosing the Project” section listing costly/time-consuming elements and related bank breakers.

### SW-D20 — Early Production-Consultation Handoff

- **Capability Name:** Early Production-Consultation Handoff
- **Problem It Solves:** Scene writing assumes a production alternative is cheap/feasible without a budget, schedule, location or legal assessment.
- **Trigger / Detection:** A proposed scene has a material burden flag, unusual location requirement, or needs an equivalence decision beyond narrative action.
- **Decision Principle:** Bring production expertise in early for budget/schedule and location assessment. Scene Writer provides dramatic function and burden flags; qualified production roles assess cost, schedule, permits, legal/technical implications and feasibility.
- **Action / Transformation:** Produce a bounded handoff: `dramatic function`, `non-negotiable story/Canon locks`, `burden flag`, `candidate question`, and `production owner required`. Do not state the solution as a writer decree.
- **Stop Condition:** Stop at the handoff; if a proposed change would alter Showrunner intent, return for authorization.
- **Failure Risk:** Scene Writer pretending to be a line producer, or a production note quietly overwriting story causality.
- **Classification:** `Conditional Method`.
- **Source Trace:** E-FI-02, “Pre-production” section on early budget/schedule expertise and early investigation; E-FI-01, “Get a location manager on board early” on early script review, scouting, legal and technical preparation.

### SW-D21 — Location-Equivalence Trade-off Test

- **Capability Name:** Location-Equivalence Trade-off Test
- **Problem It Solves:** A location change is proposed only because it appears cheaper, without checking whether its total burden or dramatic function changes.
- **Trigger / Detection:** Multiple locations, a costly location, or an out-of-area location is being considered for consolidation or substitution.
- **Decision Principle:** Compare the requested dramatic function with the full practical trade-off: a location manager may find a lower-cost or multi-use location, while a seemingly cheaper region can add travel and lodging cost. No option is intrinsically cheaper without assessment.
- **Action / Transformation:** Ask production for alternatives that could carry the same approved scene function; present them as candidates, not instructions. Reject any “saving” claim that lacks production assessment or would change locked story function without authorization.
- **Stop Condition:** Stop when alternatives are identified and ownership is handed off; do not combine characters, reduce crowd scale, or substitute action without direct source support and project authorization.
- **Failure Risk:** Treating fewer locations as universally superior, ignoring travel/lodging, or silently rewriting the scene to fit a location.
- **Classification:** `Optional Tool`.
- **Source Trace:** E-FI-01, “Get a location manager on board early” on finding multiple locations in one and cost-saving locations; E-FI-02, “Location” on weighing lower/free location costs against travel/lodging.

## D. Classification Review

|Method|Hard Constraint|Default Heuristic|Conditional Method|Optional Tool|
|---|---:|---:|---:|---:|
|SW-D19 Production-Burden Flag|No|No|Yes|No|
|SW-D20 Early Production-Consultation Handoff|No|No|Yes|No|
|SW-D21 Location-Equivalence Trade-off Test|No|No|No|Yes|

## E. Studio Translation

Film Independent’s production education becomes a narrowly scoped Scene Writer capability: detect a scene’s likely production burden early, state the approved dramatic function and Canon locks, and hand cost/schedule/location questions to production ownership. The project requirement to preserve story intent and dramatic function is an **AI Film Studio authorization boundary**, not a claim that the sources prescribe a universal compression formula.

## F. Non-Transferable Content

- $200k-specific thresholds, percentages, payroll/insurance/legal detail, sales strategy and staffing advice.
- Rules such as “fewer people is better,” “fewer locations is better,” “exteriors are bad,” or “avoid action.”
- Character consolidation, crowd-scale reduction, transport substitution, or arbitrary compression recipes: no directly verified method source in this set.
- Final producer, line-producer, director, or Showrunner decision authority.
- Any AI-production, model, prompt, GPU, or runtime constraint.

## G. Capability Coverage

|Capability|Coverage|Evidence boundary|
|---|---|---|
|SW-C13 Production Cost Awareness|Strong|Direct support for burden signals, early production review and location trade-off assessment; not budget-setting or deletion authority.|
|SW-C05 Scene Turn|None|Outside authorized Film Independent scope.|
|SW-C06 Scene End Point|None|Outside authorized Film Independent scope.|
|SW-C11 Scene Entry|None|Outside authorized Film Independent scope.|
|SW-C12 Scene Exit|None|Outside authorized Film Independent scope.|
|SW-C14 AI Production Friendliness|Deferred|No source collection or method.|

## Single-Source Distillation Tests

|Test|Result|Evidence|
|---|---|---|
|SD-01 Source Traceability|PASS|SW-D19–21 cite E-FI-01/02.|
|SD-02 No Search-Snippet Distillation|PASS|Only actual Film Independent article bodies used.|
|SD-03 No Style Imitation|PASS|No Film Independent voice, case story or speaker style is modeled.|
|SD-04 No Copyright Overreach|PASS|No extended article quotation retained.|
|SD-05 Rule Classification|PASS|Two conditional methods and one optional tool; no cheapness hard rule.|
|SD-06 No Unsupported Capability|PASS|No character consolidation, crowd reduction or universal compression method invented.|
|SD-07 Scene Writer Boundary|PASS|No Shared QA language/voice function recreated.|
|SD-08 Showrunner Boundary|PASS|Story/Canon changes require authorization.|
|SD-09 Production Gap Honesty|PASS|C14 deferred; cost awareness does not become cost authority.|
|SD-10 Source-Specific Value|PASS|Distinct value is production-burden visibility and location trade-off.|
|SD-11 Personal-Voice Safety|PASS|No organization/person style model exists.|
|SD-12 Production-Authority Safety|PASS|Methods only flag and hand off; no budget or deletion authority granted.|

**Result: `12 / 12 PASS`.**
