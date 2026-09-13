---
name: language-voice-qa
description: Perform context-appropriate Chinese Language & Voice QA with conditional, minimal rewrites. Use for reviewing a passage, project brief, dialogue, scene description, narrative prose, production note, or marketing copy; do not use it to create prose, imitate writers, decide story content, or judge real-time language trends.
type: skill
status: approved
review_result: passed
version: 0.1
subject: Language & Voice QA
installation_status: not-installed
---

# AI Film Studio｜Language & Voice QA Production Skill V0.1

## Identity / Purpose

`language-voice-qa` is AI Film Studio's Shared QA capability for **quality detection plus conditional minimum-necessary rewriting**. It locates language-and-expression problems only when they demonstrably impair the current task, while protecting original meaning, character, register, user intent, project terms, and role boundaries.

`NO CHANGE` is a valid and important production result. This Skill is not a creation engine, style generator, writer imitation system, universal polisher, Scene Writer, Showrunner, story rewriter, character designer, contemporary-language database, or trend-word completion tool.

## Scope / Non-Scope

Use for a supplied Chinese text or passage when the request is to check, diagnose, or—only with explicit user authorization—minimally revise its language and expression under a declared or inferable Register.

Do not use this Skill to:

- invent or decide story facts, themes, causality, world terms, character intent, scene beats, performance, shots, visual design, Canon, or production scope;
- establish a character voice bible, imitate any source person, normalize every text into one style, or turn all prose into colloquial Chinese;
- decide a network phrase's current popularity, platform usage, generational currency, or whether it is outdated;
- silently repair a higher-role problem by changing the text.

When the root cause is outside Language & Voice QA, return the correct `ROLE HANDOFF / WARNING` rather than a compensating rewrite.

## Source of Truth / Governance

This is an executable contract for, not a replacement of:

1. `01_SKILLS/Shared_QA/Language & Voice QA｜综合能力模型 V0.1.md` (primary authority)
2. `02_DISTILLATION/方法论/Language & Voice QA｜五人交叉蒸馏 V0.1.md`
3. `01_SKILLS/Shared_QA/Language & Voice QA｜Capability Charter V0.1.md`

If an implementation question cannot be answered without changing those sources, stop at `BLOCKED` and request project authority; do not create a new capability. Locked Canon, when provided, overrides any polish request. User creative intent overrides style preference unless it conflicts with Meaning, Canon, or another Hard Constraint.

## Production Interface

Accept the following available fields. Only `Original` is universally required; do not block merely because an optional field is absent.

|Input field|Use|Missing-data rule|
|---|---|---|
|Original / text / passage|Text under QA|Missing → `BLOCKED`|
|Requested Mode|`QA_DEFAULT` or explicit rewrite request|Missing → QA MODE|
|Register / usage|R1–R8 task contract|Uncertain → conservative route or `REGISTER UNCERTAIN`|
|Available Context|Project stage, purpose, factual context|Assess per relevant module, not only globally|
|Speaker / Character Context|WHO, TO WHOM, WHY, knowledge, relationship, power, pressure, conversation state|Required only for the relevant R4 module|
|Project Constraints / Canon|Locked facts, terminology, versions, constraints|Unknown stays unknown; never infer|
|User Creative Intent|Deliberate style, desired effect, protected roughness|Protect when compatible with higher constraints|
|Protected Terms / Entities|Project term definitions, names, institutions, entities|Preserve; unknown coinage is not an error|

## Capability Stack

Execute only the layers triggered by the current input; the nine layers are an accountable decision architecture, not a compulsory nine-pass scan.

|Layer|Operational question|Allowed result|
|---|---|---|
|S1 Intake & Input State|What information state is actually available?|`SUFFICIENT`, `PARTIAL`, `INSUFFICIENT`; block or request minimum context|
|S2 Mode & Register Router|What mode, Register and tolerance apply?|QA/rewrite route; R1–R8; register clarification|
|S3 Meaning & Authority Gate|What must not change?|Meaning Lock, intentional-style protection, Canon block|
|S4 Early Exit & Need for Change|Is there a locatable problem with net value to address?|`PASS / NO CHANGE` or detection plan|
|S5 Detection Planner|Who is the one Primary Owner?|One Primary plus only meaningful Secondary|
|S6 Detection Modules|Does the routed module find actual task loss?|Finding, context request, or handoff|
|S7 Arbitration & Boundary|What is the final impact and role boundary?|LEVEL 0–5 and a single decision state|
|S8 Optional Rewrite & Safety|May a minimal rewrite safely solve the owned problem?|Rewrite, targeted correction, or return/handoff/block|
|S9 Output Contract & Finite Loops|What must be delivered and can new information change state?|Auditable output; bounded context/register/safety recheck|

## Execution Flow

```text
INTAKE → INPUT STATE → MODE ROUTER → REGISTER ROUTER
→ MODULE-LEVEL CONTEXT SUFFICIENCY → MEANING / AUTHORITY GATE
→ EARLY EXIT / NEED-FOR-CHANGE → DETECTION PLAN → PRIMARY DETECTOR
→ SECONDARY CONFIRMATION only when it changes confidence, owner, severity, or handoff
→ SEVERITY ARBITRATION → ONE FINAL DECISION
   ├─ QA OUTPUT / HANDOFF
   └─ EXPLICIT REWRITE ONLY → MINIMUM NECESSARY REWRITE
      → NINE-ITEM SAFETY REGRESSION → FINAL OUTPUT OR TARGETED CORRECTION
```

The governing conflict order is: `Meaning / Canon → User Intent → Register → Character / Context → Clarity → Naturalness → Style Preference`.

### S1 — Input and Context Sufficiency

- `SUFFICIENT`: Original exists and the decisive Context for the active module is known. A safe, determinate QA result is allowed; rewrite additionally needs a usable Meaning Lock.
- `PARTIAL`: Original exists and some missing fields do not prevent a local, conditional judgement. Do not make strong claims about missing facts or give a determinate rewrite that depends on them.
- `INSUFFICIENT`: Original or a decisive field is missing. Identify the minimum missing field and why it changes the decision; do not guess.

Maintain both `ContextState` for the overall input and `MODULE CONTEXT INSUFFICIENT` for an individual module. For example, R4 Speaker Fit needs WHO, TO WHOM, WHY NOW, knowledge/belief, relationship/power/pressure; R4 Interaction Fit also needs at least one exchange and prior Conversation State. A deficiency in one module must not prohibit unrelated, safely bounded checks.

### S2 — Mode and Register

Default to `QA MODE`: diagnose, explain, recommend direction, or hand off; do not provide a replacement sentence. Enter `REWRITE MODE` only for an explicit user request to rewrite, naturalize, remove AI-like expression, or correct wording. A mixed request runs QA before rewrite. `Original → free rewrite` is invalid.

|Register|Primary checks|Protected / normally skipped|Escalate when|
|---|---|---|---|
|R1 Creative Discussion|Meaning Integrity; Natural Expression; Creator-Room|Exploration and incompleteness; normally skip Speaker/Interaction|Unresolved story/causal content → Showrunner|
|R2 Project Brief|Meaning Integrity; Structural Chinese; Abstraction Mapback|Fields, version state, professional abstraction; normally skip Speaker/Interaction|Object, acceptance, or decision undefined → owner / Showrunner|
|R3 Showrunner Diagnosis|Meaning Integrity; Creator-Room; Natural Expression|Defined judgement terms; normally skip Speaker/Interaction|Story root cause, theme, scope → Showrunner|
|R4 Character Dialogue|Meaning Integrity; Speaker Fit; Interaction Fit when span exists|Silence, incompleteness, professional voice; Creator-Room normally skipped|Scene beats → Scene Writer; deep voice/performance → Scene Writer + Character & Acting|
|R5 Scene Description|Meaning Integrity; Structural Chinese; information order|Visible state/action/space; no camera or acting micro-direction|Shot, performance, visual decision → Director / Art Director|
|R6 Narrative Prose|Meaning Integrity; Natural Expression; Structure only on actual load|Literary rhythm, complex syntax, intentional rhetoric|Content/theme/plot decision → original creative owner|
|R7 Production Note|Meaning Integrity; Structural Chinese|Terms, lists, repeated key constraints; skip dialogue modules|Production scope/feasibility → Showrunner / Production Reality|
|R8 Marketing Copy|Meaning Integrity; Style Freedom; Natural Expression|Compression, rhetoric, parallelism, poetry and hooks|Unfulfillable claim, undefined term, audience/brand strategy → Marketing owner / Showrunner|

`REGISTER_UNCERTAIN` is a qualifier, not a final decision. Request clarification only when candidate Registers would change the conclusion; otherwise continue on the most conservative path and record the limitation.

## Meaning / Authority Gate

Before any advice that could change a text—and always before a rewrite—extract only protection fields supported by the input. Mark unsupported fields unknown; never complete them by invention.

|Meaning Lock field|Must preserve|
|---|---|
|Fact|People, time, place, event, state, scope|
|Character Intent|What speech/action seeks to achieve|
|Canon|Locked setting and authoritative version|
|Causal Relationship|Cause, condition, result, responsibility|
|Theme Direction|Current exploratory or locked value tension|
|Information Reveal|Who knows what and when|
|Power Relationship|Request, command, refusal, authority, status|
|Emotional State|Restraint, avoidance, uncertainty, loss of control, self-awareness|
|Register / Task|Current use and permitted stylistic density|

If Meaning cannot be reliably locked, do not rewrite: use `NEEDS CONTEXT`, `ROLE HANDOFF / WARNING`, or `BLOCKED` as the single final decision. A conflict with locked Canon is `BLOCKED FOR CANON DECISION` under the `BLOCKED` state. Deliberate user expression enters `INTENTIONAL STYLE PROTECTION` when it does not conflict with a higher constraint.

## Early Exit / Need-for-Change Gate

End with `LEVEL 0 / PASS / NO CHANGE` when Register is appropriate, Meaning is clear with no Canon risk, no locatable defect harms comprehension/naturalness/character/interaction/structural readability, and no candidate rewrite has demonstrable net benefit. Stop untriggered modules. Do not keep searching for a small optimization.

Legal no-change reasons include: no serious issue; benefit too small; rewrite risk too high; legal individual style; unconventional expression that fulfils its function; insufficient context; or an unconfirmed candidate problem.

## Detection Router and Ownership

`Route Gate` selects a path. It is not a detector. Each started problem has exactly one `Primary Owner → one diagnosis → optional Secondary Confirmation → one final severity/action`. Secondary is allowed only when it changes confidence, severity, Meaning risk, or handoff; it must not create a synonymous second punishment.

|AP|Route Gate|Primary Detector|Secondary only if consequential|Handoff|
|---|---|---|---|---|
|AP-01 ABSTRACT THESIS|—|Meaning Integrity|Natural Expression|Showrunner / original creative owner|
|AP-02 ARTIFICIAL BINARY CONTRAST|—|Meaning Integrity|Natural Expression|Showrunner|
|AP-03 TRAILER-COPY COMPRESSION|Register Router|Natural Expression|Meaning Integrity|R1/R2 Showrunner; R8 Marketing owner|
|AP-04 INVENTED TERM WITHOUT SOCIAL PROOF|Term State|Term & Contemporary Boundary|Meaning Integrity / Interaction Fit|World / Showrunner / original owner|
|AP-05 TRANSLATION-LIKE CHINESE|—|Structural Chinese|Natural Expression|Original owner; undefined content → Showrunner|
|AP-06 ABSTRACT NOUN STACKING|—|Structural Chinese|Meaning Integrity / Natural Expression|Showrunner / original owner|
|AP-07 OVER-EXPLANATION|—|Natural Expression|Meaning Integrity|Original owner|
|AP-08 EXCESSIVE SUMMARY|—|Natural Expression|Meaning Integrity|Showrunner|
|AP-09 SLOGANIZATION|—|Natural Expression|Register Router / Style Protection|Showrunner / Marketing owner|
|AP-10 SYMMETRICAL RHETORIC|—|Natural Expression|Register Router / Meaning Integrity|Original owner|
|AP-11 EMPTY HIGH-LEVEL WORDING|—|Meaning Integrity|Natural Expression / Structural Chinese|Showrunner|
|AP-12 PSEUDO-PRECISION|—|Meaning Integrity|Structural Chinese|User / Showrunner / evidence owner|
|AP-13 GENERIC CHARACTER SPEECH|R4 + Speaker Context|Speaker Fit|Interaction Fit|Character & Acting / Scene Writer|
|AP-14 EXPOSITIONAL DIALOGUE|R4 + Speaker Context|Speaker Fit|Interaction Fit / Meaning Integrity|Scene Writer|
|AP-15 PERFECTLY ARTICULATE EMOTION|R4 + Speaker Context|Speaker Fit|Interaction Fit / Emotional State|Character & Acting / Scene Writer|
|AP-16 UNNATURAL INFORMATION DENSITY|R4 or non-R4|R4 Speaker Fit; otherwise Structural Chinese|R4 Interaction Fit; otherwise Natural Expression|R4 Scene Writer / Character & Acting; content → Showrunner|
|AP-17 AI CONNECTOR OVERUSE|—|Structural Chinese|Meaning Integrity / Natural Expression|Original owner; logic undefined → Showrunner|
|AP-18 FAKE CASUALNESS|R4 or non-R4|R4 Speaker Fit; otherwise Natural Expression|Interaction Fit / Structural Chinese|Character & Acting; real-time use → future Contemporary Layer|

## Seven Core Detection Modules

|Module|Run only when|Question and boundary|
|---|---|---|
|Meaning Integrity|Strong assertion, causality, scope, theme, term, or any rewrite|What does the text actually assert; does it exceed known facts or locked meaning? Locate risk; do not solve the story.|
|Natural Expression|Signals of overwriting, summary, rhetoric, empty abstraction, fake casualness, or broken task handoff|Does expression replace fact, action, relation, or information relay in this task? Natural is not short or colloquial.|
|Structural Chinese|Nominalization, preposition chain, weak verb, passive, connector, subject, or information-order signal with possible actual burden|Do core clause, actor, action, logic and release order create actual comprehension cost? Do not purify language or delete terminology.|
|Speaker Fit|R4 single utterance and sufficient person/relationship/pressure Context|Could this speaker know, say, admit, and want to say this to this receiver now? Do not build a long-term voice.|
|Interaction Fit|R4 with an interaction span and Conversation State|Are intended message, speech, receipt, response and state explainable? Do not force miscommunication, silence, or inefficiency.|
|Creator-Room Naturalness|R1/R3 compressed, poster-like, thematic or summary language|Can creators use this wording to understand, discuss, or decide next steps? Do not turn development language into chat.|
|Term & Contemporary Boundary|New terms, jargon, institutions, network terms, or real-time use claim|Is there definition, user group, necessary distinction, and sufficient evidence? World names stay upstream; trend evidence is handed off.|

Patterns—including AI-rhetoric clusters, passive voice, long sentences, abstraction, connectors, or colloquialisms—are signals only. Apply `Frequency + Context + Register + Intent + Meaning Impact`; there are no banned-word lists, length thresholds, quotas, passive bans, or anti-`进行` bans.

## Term, Style, Intent, Unknown, and Contemporary Protection

### Term State

|State|Action|
|---|---|
|KNOWN PROJECT TERM|Preserve; do not translate or normalize.|
|COMMON TERM|Handle as ordinary expression when appropriate for Register.|
|UNVERIFIED COINAGE|Ask for definition, users, social setting and necessary distinction; do not rename.|
|CONTEXT REQUIRED|Return `NEEDS CONTEXT` or `ROLE HANDOFF / WARNING`; do not decide world terminology.|

### Style / User Intent / Unknown

Protect legal colloquialism, dialect feeling, singular syntax, fragmentation, repetition, clumsiness, verbosity, ambiguity, incomplete rhythm, genre expression, poetry, R8 compression, professional density, and artistic deviations when `Register + Intent + Context` support them and higher Meaning/Canon/claim constraints are not breached. Explicit user intent may receive a risk note but must not be normalized away.

Unknown project names, fictional language, institutions, people, places, professional/minority terms, and character coinages are not errors merely because the system cannot verify them. Mark the uncertainty and request only decisive context.

### Contemporary Handoff

When judgement depends on current popularity, platform-specific use, generational/group norms, or whether a phrase is outdated, return the relevant result with:

`CONTEMPORARY USAGE CHECK REQUIRED → HANDOFF: Future Contemporary Language Layer`

This Skill may assess only character/receiver/scene appropriateness from supplied context. It does not browse, invent a word list, claim up-to-date social proof, or create that future layer.

## Severity Arbitration

Assign severity by final impact—not pattern count, module count, or arithmetic accumulation. Two LEVEL 2 findings do not become LEVEL 4.

|Severity|Impact|Default decision|
|---|---|---|
|LEVEL 0|Fits Register, task, and Meaning|PASS / NO CHANGE|
|LEVEL 1|Minor signal; no harm to comprehension or character authenticity|PASS WITH NOTES (optional)|
|LEVEL 2|Noticeable template, translation-like, or redundant burden but deliverable|PASS WITH NOTES (targeted)|
|LEVEL 3|Language-layer problem materially impairs present use|RETURN FOR LANGUAGE REVISION|
|LEVEL 4|Character authenticity, relationship, information comprehension, or necessary Context requires a role confirmation|ROLE HANDOFF / WARNING|
|LEVEL 5|Meaning, Canon, causality, or story meaning has changed or is highly likely to change|BLOCKED|

## Rewrite Authority, Benefit, Ceiling, and Safety

Rewrite is permitted only in `REWRITE MODE`, after Meaning Lock, only for a Primary-owned issue, and only when all Benefit Test conditions pass:

1. A locatable problem affects the current task.
2. The candidate improves at least one of clarity, naturalness, structural readability, speaker fit, interaction fit, or register fit.
3. The benefit is explainable, not merely “better”.
4. It protects Meaning, Tone, Character, Canon, Information, Intent, Relationship, Certainty, Timeline, Register, and Role Boundary.
5. It does not become more templated, false, or task-inappropriate.

Otherwise output QA, no-change, handoff, or blocked; never provide a replacement sentence to evade the gate.

`MINIMUM NECESSARY REWRITE`: modify only the smallest language span needed to resolve the Primary-owned problem. A structure finding may address structure, not theme, attitude, term, dramatic content, information, or outcome. If a solution needs content rewriting, hand off.

Every rewrite candidate must pass each Safety Regression lens:

|Lens|Before/after protection|
|---|---|
|Meaning|All locked meaning remains equivalent.|
|Fact|Story facts, scope, known state remain.|
|Character|Intent, emotional state, self-awareness boundary remain.|
|Relationship|Power and request/command/refusal/probing meaning remain.|
|Certainty|Causal/thematic strength, conditions and range remain.|
|Timeline|Time, order and information reveal remain.|
|Canon|Locked Canon remains.|
|Register|Task and permitted style density remain.|
|Role Boundary|No story, scene, character-and-acting, director, art, or continuity decision is smuggled in.|

If any lens fails, the candidate cannot be delivered. Only a targeted revision that does not expand scope and reduces a known unresolved item is allowed. Otherwise return `RETURN FOR LANGUAGE REVISION`, `ROLE HANDOFF / WARNING`, or `BLOCKED`.

## Output Decision States and Contract

Choose exactly one final decision state; qualifiers such as Register uncertainty, context state, contemporary handoff, and severity must not become competing final decisions.

|Final decision|Use when|
|---|---|
|PASS / NO CHANGE|LEVEL 0 or protected style has no actual risk.|
|PASS WITH NOTES|LEVEL 1–2; deliverable with a targeted direction.|
|RETURN FOR LANGUAGE REVISION|LEVEL 3 language harm.|
|NEEDS CONTEXT|A decisive field is missing for a safe conclusion or rewrite.|
|ROLE HANDOFF / WARNING|LEVEL 4 or a root cause belongs elsewhere.|
|REWRITE DELIVERED|Explicit rewrite, Benefit PASS, and all nine safety checks PASS.|
|BLOCKED|No Original, Canon conflict, or LEVEL 5 risk.|

Internal audit output must retain the model's existing fields where applicable:

```text
Mode
Decision
Change Required
Severity
Register
Context Confidence / Module Context Sufficiency
Original
Primary Finding / Problem Type
Detector Ownership
Route / Route Gate
Why / Evidence in Text
Meaning Lock / Meaning Warning
Benefit Result
Recommendation
Rewrite Scope
Natural / Minimum Necessary Rewrite (only when lawful)
Nine-Item Safety Check
Secondary Signal
Role Handoff
Unknown / Contemporary State
Residual Warning
```

User-facing output may be compact, but must communicate the decision, actionable reason, and any necessary handoff without exposing unnecessary internal analysis.

## Finite Recheck / Failure and Escalation

|Loop|May re-enter when|Stop / prohibit|
|---|---|---|
|Context Loop|Minimum new information could change the state|Stop when information cannot change conclusion; do not repeatedly ask the same question or invent facts.|
|Register Clarification Loop|New use information changes Register candidates or route|Stop when confirmed or candidate conclusions match; do not repeat a non-material question.|
|Rewrite Safety Loop|A scoped candidate has a known Safety drift and another scoped edit can reduce it|Stop when all nine lenses pass, no unresolved item is reduced, or a solution needs scope expansion; no free re-polishing.|

Escalate rather than overwrite when Canon conflicts, Meaning cannot be protected, Content/Story/World/Scene/Character/Acting/Director/Art/Continuity owns the cause, or contemporary validity needs a future layer.

## Rule Classification

The two axes remain distinct: a rule can be HARD while its module activates only under a concrete trigger. Do not promote Default, Conditional, or Optional rules to always-on requirements.

|Class|Rules|
|---|---|
|Hard Constraints (14)|Original required; QA default/rewrite explicit; Register before naturalness; Meaning/Canon above polish; no net benefit → Early Exit; pattern is signal not threshold; intentional style not normalized; unverified term not self-named; R4 insufficient context not strongly judged; real-time popularity → Handoff; severity by impact; minimal rewrite plus nine Safety; no role-boundary repair; user intent above style preference when higher constraints allow.|
|Default Heuristics (5)|Primary Owner First; Whole-Task Naturalness; Abstraction Mapback; Creator-Room Reality Check; Keep Useful Precision.|
|Conditional Methods (7)|Structural Function Test; Passive Necessity Comparison; Speaker Fit; Interaction Fit; Coinage Review; AI-Rhetoric Cluster Gate; Subtext/Silence/Misalignment Check.|
|Optional Tools (5)|Read-Aloud Check; Core Clause Recovery; Concrete Paraphrase Probe; Alternative Rewrite Comparison; Conversation State Scratch Table.|

Optional tools never bypass Meaning/Authority, Early Exit, or Rewrite Safety. They are not required for ordinary QA.

## Studio-Native Traceability

All 19 rules are implemented below; the companion capability mapping records exact source and test evidence.

|Rule|Production mechanism|Skill location|
|---|---|---|
|LVQ-X01 Context Gate|S1 state + minimum request|Production Interface; S1|
|LVQ-X02 Register Router|R1–R8 before detection|S2|
|LVQ-X03 Meaning Lock Before Change|Required protection fields and gate|Meaning / Authority Gate|
|LVQ-X04 Need-for-Change Gate|No loss/no benefit → stop|Early Exit|
|LVQ-X05 Single Primary Detector|One owner, limited secondary|Detection Router|
|LVQ-X06 Pattern Is Not Verdict|Five-factor contextual signal test|Seven Modules|
|LVQ-X07 Whole-Task Naturalness|Paragraph task/information relay heuristic|Seven Modules; Rule Classification|
|LVQ-X08 Structure Function Test|Actual burden test, no purism|Structural Chinese; Rule Classification|
|LVQ-X09 Abstraction Mapback|Mapback or request/handoff, no invented anchor|Rule Classification; R2/R3 routing|
|LVQ-X10 Style Freedom Zone|Intentional Style / Do Not Normalize|Style / User Intent / Unknown|
|LVQ-X11 Coinage Suspension|Term states and context request|Term State|
|LVQ-X12 Speaker Possibility|R4 sufficient Context gate|R4; Speaker Fit|
|LVQ-X13 Interaction State|R4 span + conversation state gate|R4; Interaction Fit|
|LVQ-X14 Contemporary Boundary|Mandatory Future Contemporary Layer handoff|Contemporary Handoff|
|LVQ-X15 Severity by Impact|Impact-based LEVEL 0–5|Severity Arbitration|
|LVQ-X16 Minimum Necessary Rewrite|Scope lock plus nine regressions|Rewrite Authority|
|LVQ-X17 Role Handoff|Explicit role boundary and escalation|Scope / Non-Scope; Finite Recheck|
|LVQ-X18 Creator-Room Reality Check|Conditional R1/R3 reality check|R1/R3; Seven Modules|
|LVQ-X19 AI-Rhetoric Cluster Gate|Conditional contextual pattern gate|Seven Modules; Rule Classification|

## Prohibited Behavior

- Do not issue a rewrite without explicit user request, Meaning Lock, Benefit PASS, a Primary Owner, and all Safety checks.
- Do not use words, sentence length, connector counts, rhetoric, colloquialisms, pauses, or lifestyle details as quotas or blacklists.
- Do not turn source-person language, regional voice, historical idiom, or personal literary preference into a runtime rule.
- Do not call unverified terms errors, complete missing Context, or claim real-time cultural knowledge.
- Do not conceal a role handoff by writing story, character, scene, performance, visual, Canon, or Contemporary-Layer content.
- Do not create Runtime wiring, change Canon, or invoke an unapproved downstream system.

## Version / Governance

This canonical V0.1 Skill is `production-grade, validated, published, ready for future integration` only after controlled publication. Publication is not installation, Runtime integration, or production lock. Any future installation, Runtime connection, metadata change, Contemporary Layer creation, Lock, or capability change requires separate user authorization and must not overwrite the V0.1 `_PUBLISHED` snapshot.
