---
type: implementation-mapping
status: review
version: 0.1
subject: Language & Voice QA Production Skill
---

# Language & Voice QA Production Skill V0.1｜Capability Mapping

## Mapping Basis

Primary Source of Truth: `Language & Voice QA｜综合能力模型 V0.1.md`. Cross-Distillation and Capability Charter are used only to preserve the Model's approved provenance and clarify source wording. No additional capability, threshold, detector, output state, or future-stage artifact is introduced.

## Capability Stack and Flow

|Capability Model location|Production Skill location|Execution mechanism|Test evidence|
|---|---|---|---|
|Decision Flow, lines 43–72|`Execution Flow`|Ordered flow with primary/secondary restriction and optional rewrite branch|P01–P03, P15, P19|
|S1 Intake & Input State, lines 80–80; Input State, 90–122|`Production Interface`; `S1 — Input and Context Sufficiency`|Original gate plus overall and module-level context states|P03, P12|
|S2 Mode & Register Router, 81; Mode, 124–131; R1–R8, 133–144|`S2 — Mode and Register`|QA default, explicit rewrite, register-specific primary/protected/escalation paths|P04, P10, P16|
|S3 Meaning & Authority Gate, 82; Meaning Lock, 146–168|`Meaning / Authority Gate`|Nine supported-field locks and no-invention gate|P02, P09, P19|
|S4 Early Exit, 83; Stop Condition, 170–181|`Early Exit / Need-for-Change Gate`|No locatable loss or net benefit ends at NO CHANGE|P01, P07, P17|
|S5 Detection Planner, 84; Ownership, 183–214|`Detection Router and Ownership`|Route Gate is distinct from one Primary Owner; Secondary is consequential only|P04, P05|
|S6 Detection Modules, 85; Modules, 216–226|`Seven Core Detection Modules`|Seven conditional modules and their output boundaries|P04, P05, P10–P14|
|S7 Arbitration, 86; Severity, 313–324|`Severity Arbitration`|Impact-based LEVEL 0–5, no hit-count arithmetic|P06|
|S8 Optional Rewrite & Safety, 87; Benefit/Safety, 277–311|`Rewrite Authority, Benefit, Ceiling, and Safety`|Explicit authorization, five-part benefit, minimum scope, nine regression lenses|P02, P07–P09, P19|
|S9 Output Contract & Finite Loops, 88; Outputs/loops, 326–392|`Output Decision States and Contract`; `Finite Recheck`|One decision state plus three state-change limited loops|P15, P16|

## R1–R8 Production Router

|Model Register|Production Skill location|Route mechanism|Test|
|---|---|---|---|
|R1 Creative Discussion|`S2 — Mode and Register` row R1|Meaning + Natural + Creator-Room; exploration protected|P04-R1; P20-BB02/03A|
|R2 Project Brief|S2 row R2|Meaning + Structure + Mapback; precision protected|P04-R2; P17 normal brief|
|R3 Showrunner Diagnosis|S2 row R3|Meaning + Creator-Room + Natural; story root cause handed off|P04-R3|
|R4 Character Dialogue|S2 row R4; `S1`; `Seven Core Detection Modules`|Speaker before Interaction; module context gates|P04-R4; P05; P10; P20-BB03B/08|
|R5 Scene Description|S2 row R5|Meaning + Structure/information order; camera/acting excluded|P04-R5|
|R6 Narrative Prose|S2 row R6|Meaning + Natural; structure only for actual load|P04-R6; P20-BB06|
|R7 Production Note|S2 row R7|Meaning + Structure; conditions/terms protected|P04-R7; P17 professional language|
|R8 Marketing Copy|S2 row R8|Meaning + Style Freedom + Natural; truth/fulfilment handoff|P04-R8; P10; P20-BB04B/10|

## AP-01–18 Ownership

|AP|Model primary (model lines 193–214)|Production Skill primary|Production mechanism|Test|
|---|---|---|---|---|
|AP-01|Meaning Integrity|Meaning Integrity|One finding; Natural only secondary|P05-01|
|AP-02|Meaning Integrity|Meaning Integrity|One finding; no binary blacklist|P05-02, P20-BB03A|
|AP-03|Natural Expression after Register Gate|Natural Expression|R1/R2 vs R8 destination differs|P05-03, P20-BB04|
|AP-04|Term & Contemporary Boundary|Term & Contemporary Boundary|Term state blocks self-naming|P05-04, P12|
|AP-05|Structural Chinese|Structural Chinese|Actual load rather than foreign-form marker|P05-05|
|AP-06|Structural Chinese|Structural Chinese|Mapback/meaning only consequential secondary|P05-06|
|AP-07|Natural Expression|Natural Expression|Meaning secondary only if it changes conclusion|P05-07|
|AP-08|Natural Expression|Natural Expression|Theme direction secondary only if consequential|P05-08|
|AP-09|Natural Expression|Natural Expression|Register/style protection prevents slogan false positive|P05-09|
|AP-10|Natural Expression|Natural Expression|Rhetoric signal is contextual only|P05-10|
|AP-11|Meaning Integrity|Meaning Integrity|Natural/structure are secondary signals|P05-11|
|AP-12|Meaning Integrity|Meaning Integrity|Evidence owner handoff; no invented precision|P05-12|
|AP-13|Speaker Fit|Speaker Fit|R4 and sufficient character context required|P05-13|
|AP-14|Speaker Fit|Speaker Fit|Interaction/meaning secondary, Scene Writer handoff|P05-14|
|AP-15|Speaker Fit|Speaker Fit|Emotion clarity requires Context; no automatic failure|P05-15|
|AP-16|R4 Speaker Fit / non-R4 Structural Chinese|Same route split|Route precedes one primary selection|P05-16|
|AP-17|Structural Chinese|Structural Chinese|Connector load is a signal, no quota|P05-17|
|AP-18|R4 Speaker Fit / non-R4 Natural Expression|Same route split|No forced casualness; contemporary use is handoff|P05-18|

## 19/19 Studio-Native Rule Implementation Mapping

|Studio-Native Rule|Capability Model location|Production Skill location|Execution mechanism|Test case|
|---|---|---|---|---|
|LVQ-X01 Context Gate|S1; Model 90–122|`S1 — Input and Context Sufficiency`|Original hard gate; minimum request; module-level insufficiency|P03|
|LVQ-X02 Register Router|S2; 133–144|`S2 — Mode and Register`|R1–R8 routes precede detection|P04|
|LVQ-X03 Meaning Lock Before Change|S3; 146–168|`Meaning / Authority Gate`|Supported protection fields lock before advice/rewrite|P02, P19|
|LVQ-X04 Need-for-Change Gate|S4; 170–181|`Early Exit / Need-for-Change Gate`|No actual loss/net benefit means stop|P01, P07|
|LVQ-X05 Single Primary Detector|S5; 183–214|`Detection Router and Ownership`|One primary, limited consequential secondary|P05|
|LVQ-X06 Pattern Is Not Verdict|Natural/Structural Protocol, 228–239|`Seven Core Detection Modules`|Frequency + Context + Register + Intent + Meaning Impact|P18|
|LVQ-X07 Whole-Task Naturalness|Natural Protocol, 228–233|Natural Expression; Rule Classification|Task/information relay before local aesthetics|P17|
|LVQ-X08 Structure Function Test|Structural Protocol, 234–239|Structural Chinese; Rule Classification|Actual burden only; anti-purism|P05-05, P18|
|LVQ-X09 Abstraction Mapback|Default Heuristics, 415–423|Rule Classification; R2/R3 router|Map back or request/handoff; never invent anchor|P05-06|
|LVQ-X10 Style Freedom Zone|273–275|`Style / User Intent / Unknown`|Intentional Style / Do Not Normalize|P10, P11|
|LVQ-X11 Coinage Suspension|256–264|`Term State`|UNVERIFIED/CONTEXT REQUIRED preserve and request|P12, P13|
|LVQ-X12 Speaker Possibility|240–247; 114–122|S1 R4 gate; Speaker Fit|WHO/receiver/knowledge/power/pressure required|P04-R4, P05-13|
|LVQ-X13 Interaction State|248–252; 114–122|S1 R4 gate; Interaction Fit|Conversation state required, no forced miscommunication|P04-R4, P05-14|
|LVQ-X14 Contemporary Boundary|265–271|`Contemporary Handoff`|No real-time verdict; exact future-layer handoff|P14|
|LVQ-X15 Severity by Impact|313–324|`Severity Arbitration`|Final impact, not count or module arithmetic|P06|
|LVQ-X16 Minimum Necessary Rewrite|291–311|`Rewrite Authority, Benefit, Ceiling, and Safety`|Primary-aligned small scope and nine regressions|P08, P19|
|LVQ-X17 Role Handoff|S7; 283–293|Scope / Non-Scope; Finite Recheck|Upstream cause gets owner, risk, bounded QA scope|P05, P16|
|LVQ-X18 Creator-Room Reality Check|Core Modules, 225; R1/R3 routing|R1/R3; Creator-Room module|Conditional check of decision utility, not chat normalizing|P04-R1/R3, P20-BB02|
|LVQ-X19 AI-Rhetoric Cluster Gate|Natural Protocol, 228–233|Seven Modules; Rule Classification|Conditional contextual gate, no phrase ban|P18, P20-BB02|

## Output State and Rule-Class Completeness

|Formal item|Production Skill location|Test|
|---|---|---|
|Seven mutually exclusive Output Decision States|`Output Decision States and Contract`|P15|
|14 Hard Constraints|`Rule Classification`|P16, Static Audit|
|5 Default Heuristics|`Rule Classification`|P01, P05, P17|
|7 Conditional Methods|`Rule Classification`|P04, P05, P12–P14|
|5 Optional Tools|`Rule Classification`|P16 (must remain optional)|

## Mapping Verdict

S1–S9: `9 / 9` mapped. R1–R8: `8 / 8` mapped. AP-01–18: `18 / 18` mapped. Studio-Native Rules: `19 / 19` mapped. Output Decision States: `7 / 7` mapped. Rule classes: `14 / 5 / 7 / 5` preserved. No added capability or rule-class promotion detected.
