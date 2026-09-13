---
type: single-source-distillation
status: passed
version: 0.1
source_group: BBC Writersroom
source_evidence: E-BBC-01
scope: methods-not-style
---

# Scene Writer Distillation — BBC Writersroom V0.1

## A. Source Scope

**Actually read:** BBC Writersroom, *Screenplay Format*, viewer PDF p.2 / printed p.1: “Scene action” and its paragraph-beat guidance; viewer PDF p.4: “Transitions”; viewer PDF p.7: “Series of Shots”.

**Not read or transferred:** any writer’s personal style, scene content, character psychology, broad dramatic-structure doctrine, production budgeting, AI-production practice, or an instruction that Scene Writer selects final shots.

**Evidence boundary:** the document is a screenplay-format guide. Its claims establish presentation and screen-action limits, not a complete scene-design theory.

## B. Primary Contributions

- Screen action is constrained to what happens on screen; novelistic interior thought and backstory do not belong there as unconverted description.
- An action paragraph may be treated as one meaningful action beat; the source gives a four-to-five-line rule of thumb, not a universal Studio length rule.
- In a spec-script context, transitions and camera/technical directions are limited rather than default writer authority.

## C. Distilled Methods

### SW-D01 — Screen-Observable Action Filter

- **Capability Name:** Screen-Observable Action Filter
- **Problem It Solves:** A scene description asks the viewer to access a character’s unshown thought, history, or conclusion.
- **Trigger / Detection:** An action line can only be understood by entering a character’s mind or by importing unshown backstory.
- **Decision Principle:** In screen action, keep the description to an event the audience can encounter on screen; retain story meaning only through an observable action, reaction, object, sound, spatial change, or an explicit separately authorized narration device.
- **Action / Transformation:** Flag the inaccessible claim; request or create the smallest visible dramatic carrier without declaring the internal state itself to be false.
- **Stop Condition:** Stop when the scene action is observable but before deciding the final shot, actor’s performance, or exposition policy.
- **Failure Risk:** Mechanical “show, never tell” can erase legitimate narration or project-approved interior devices; those require explicit project authorization rather than automatic deletion.
- **Classification:** `Hard Constraint` within Scene Writer’s screen-action description field.
- **Source Trace:** E-BBC-01, viewer PDF p.2 / printed p.1, “Scene action”: action is limited to what happens on screen and excludes superfluous novelistic thoughts/backstory.

### SW-D02 — One Action Block, One Significant Beat

- **Capability Name:** Significant Beat Segmentation
- **Problem It Solves:** Dense description hides the changes that an actor, reader, or later production role must track.
- **Trigger / Detection:** One block contains several unrelated actions, reactions, or state changes with no clear beat boundary.
- **Decision Principle:** Separate a significant change into a readable action beat. The source’s four-to-five-line paragraph length is contextual guidance, not a Studio maximum.
- **Action / Transformation:** Split only at a change in action, response, attention, information, or physical state; do not split merely for visual neatness.
- **Stop Condition:** Stop when action progression is readable; do not manufacture a scene turn where the source scene has none.
- **Failure Risk:** Treating a formatting heuristic as dramatic law can fragment deliberate pacing or replace dramaturgy with line-count compliance.
- **Classification:** `Default Heuristic`.
- **Source Trace:** E-BBC-01, viewer PDF p.2 / printed p.1, “Scene action”: a paragraph is a significant beat and the stated length is a rule of thumb.

### SW-D03 — Format-Scoped Technical-Direction Boundary

- **Capability Name:** Spec-Script Technical-Direction Boundary
- **Problem It Solves:** Scene material smuggles in director-owned transition, camera, or technical choices as if they were necessary story facts.
- **Trigger / Detection:** A draft uses a specific transition or technical direction when the dramatic meaning is already clear without it.
- **Decision Principle:** In spec-style scene material, presume ordinary continuity unless a transition is genuinely necessary; screenplay transition conventions do not grant Scene Writer final directing authority.
- **Action / Transformation:** Retain the narrative event and route final shot/transition selection to a future Director/Cinematography role when that decision matters.
- **Stop Condition:** Stop after identifying the narrative need; do not resolve its final visual implementation.
- **Failure Risk:** Removing an explicitly approved nonstandard presentation device or treating all scene outputs as spec scripts.
- **Classification:** `Conditional Method` — only when the requested output is spec-style screenplay material.
- **Source Trace:** E-BBC-01, viewer PDF p.4, “Transitions”: transitions are generally for shooting scripts and should be specified only when necessary; viewer PDF p.8 / printed p.7 notes camera/technical directions are avoided in spec scripts.

## D. Classification Review

|Method|Hard Constraint|Default Heuristic|Conditional Method|Optional Tool|
|---|---:|---:|---:|---:|
|SW-D01 Screen-Observable Action Filter|Yes|No|No|No|
|SW-D02 Significant Beat Segmentation|No|Yes|No|No|
|SW-D03 Technical-Direction Boundary|No|No|Yes|No|

## E. Studio Translation

BBC’s format guidance becomes three bounded Scene Writer checks: whether the information is screen-observable, whether the action changes in readable beats, and whether a request is trying to seize a future director-owned implementation choice. These are scene-material construction checks, not a mandate to format every project in one national industry style.

## F. Non-Transferable Content

- Exact margin, capitalization, spacing, page-break, character-cue, foreign-language and title-page conventions: format-specific; not Studio creative capability.
- The four-to-five-line paragraph count: source rule of thumb, never an absolute Studio length cap.
- Specific transition labels, shot conventions and shooting-script details: Director/Cinematography or production-document territory.
- No source support for scene objective, conflict, turn, end point, production cost, AI production, or character-voice evaluation.

## G. Capability Coverage

|Capability|Coverage|Evidence boundary|
|---|---|---|
|SW-C01 Shootability|Strong|Screen action is limited to what can happen on screen.|
|SW-C02 Tell → Show|Strong|Internal thought/backstory cannot remain unconverted in scene action.|
|SW-C03 Scene Objective|None|No verified treatment.|
|SW-C04 Conflict / Resistance|None|No verified treatment.|
|SW-C05 Scene Turn|Weak|Action beats are not evidence of a dramatic turn.|
|SW-C06 Scene End Point|None|No verified treatment.|
|SW-C07 Dialogue Function|Weak|Only dialogue presentation, not dramatic function.|
|SW-C08 Subtext|None|No verified treatment.|
|SW-C09 Information Delivery|Partial|Screen-observable carrier boundary only.|
|SW-C10 Internal → Actable Behavior|Strong|Requires external screen-action carrier; does not prescribe one.|
|SW-C11 Entry|None|No verified treatment.|
|SW-C12 Exit|None|No verified treatment.|
|SW-C13 Production Cost Awareness|None|NOT SUPPORTED BY CURRENT SOURCE SET.|
|SW-C14 AI Production Friendliness|None|NOT SUPPORTED BY CURRENT SOURCE SET.|
|SW-C15 Character Voice Boundary|None|No verified treatment.|

## Single-Source Distillation Tests

|Test|Result|Evidence|
|---|---|---|
|SD-01 Source Traceability|PASS|SW-D01–03 each cites E-BBC-01 page/section.|
|SD-02 No Search-Snippet Distillation|PASS|Only the actual BBC PDF body is used.|
|SD-03 No Style Imitation|PASS|No author, screenplay character, or prose style is modeled.|
|SD-04 No Copyright Overreach|PASS|No extended quotation or example scene is retained.|
|SD-05 Rule Classification|PASS|One hard, one default, one conditional method.|
|SD-06 No Unsupported Capability|PASS|Unsupported domains are marked None/Weak.|
|SD-07 Scene Writer Boundary|PASS|Language QA is not recreated.|
|SD-08 Showrunner Boundary|PASS|No story or macro-structure authority added.|
|SD-09 Production Gap Honesty|PASS|C13/C14 remain None.|
|SD-10 Source-Specific Value|PASS|Contribution is observability, beat readability, and format boundary.|

**Result: `10 / 10 PASS`.**

