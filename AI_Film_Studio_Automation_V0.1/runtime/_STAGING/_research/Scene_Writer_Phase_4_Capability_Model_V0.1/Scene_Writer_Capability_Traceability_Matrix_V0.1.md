---
type: capability-traceability-matrix
status: passed-awaiting-human-review
version: 0.1
role: Scene Writer
orphan_methods: 0
unsupported_final_rules: 0
---

# Scene Writer Capability Traceability Matrix V0.1

## Capability Coverage Trace

|Capability|Final model location|Final rules|Decision flow / contract|Tests|Status|
|---|---|---|---|---|---|
|SW-C01 Shootability|S4; Shootability Model|NR-01, NR-02, NR-12|S4; Input form; Output Director flag|CM-03,04,14; AM-01; FP-01; BB-X01,05|Mapped|
|SW-C02 Tell → Show|S4; Shootability Model|NR-01, NR-02, NR-07|S4; Output control data|CM-03,04; AM-01,06; FP-01; BB-X01|Mapped|
|SW-C03 Scene Objective|S3 State/Function|NR-04, NR-08|S3; Context required-intention gate|CM-01,02,12,13; AM-02; FP-04|Mapped|
|SW-C04 Conflict / Resistance|S3/S4|NR-04, NR-08|S3; Input participants/objective|CM-02; AM-02; FP-04; BB-X02|Mapped|
|SW-C05 Scene Turn|S5 State Model|NR-03, NR-05|S5 Turn Benefit Test|CM-02; AM-03; FP-04,09; BB-X02|Mapped|
|SW-C06 Scene End Point|S5 State Model|NR-05, NR-06|S5; Output exit rationale|CM-08; AM-05; FP-03; BB-X08|Mapped|
|SW-C07 Dialogue Function|S4 Dialogue Construction|NR-02, NR-07, NR-08|S4; Output Shared QA eligibility|CM-05,06,15; AM-09; FP-06,07; BB-X07|Mapped|
|SW-C08 Subtext|S4 Dialogue Construction|NR-02, NR-07, NR-08|S4; Output scene/control separation|CM-06; AM-06; FP-07; BB-X07|Mapped|
|SW-C09 Information Delivery|S4 Information Construction|NR-02, NR-07|S4; Output compact control summary|CM-04,06; AM-06; FP-07; BB-X07|Mapped|
|SW-C10 Internal → Actable Behaviour|S4 Shootability Model|NR-01–03|S4; State Model action carrier|CM-03,04; AM-01,10; FP-01,08; BB-X01,08|Mapped|
|SW-C11 Scene Entry|S5 Entry Test|NR-06|S5; Input prior-state rule|CM-07; AM-04; FP-02|Mapped|
|SW-C12 Scene Exit|S5 Exit Test|NR-06|S5; Output exit rationale|CM-08; AM-05; FP-03; BB-X08|Mapped|
|SW-C13 Production Cost Awareness|S6 Production Boundary|NR-10|S6; input production context; production flag/handoff|CM-09,10,11; AM-07,08; FP-05,10; BB-X03,09|Mapped|
|SW-C14 AI Production Friendliness|S0/S6/S7 Deferred Boundary|None — Deferred interface only|Input/Output external-profile flags|CM-11; WI-06; BB-X10|Mapped as Deferred|
|SW-C15 Character Voice Boundary|S4 / role boundary|NR-08, NR-09, NR-12|Output Shared QA / Director / Acting flags|CM-14,15; WI-04,05; BB-X05|Mapped|

## SW-D Method Trace

|Method|Relationship basis|Final model location|Final rule / boundary|Source trace|Status|
|---|---|---|---|---|---|
|D01 Screen-Observable Action Filter|RL-01,02|S4 Shootability|NR-01, NR-02|E-BBC-01|Mapped|
|D02 Significant Beat Segmentation|RL-03|S4/S5|NR-03, NR-05|E-BBC-01|Mapped|
|D03 Format-Scoped Technical Direction|RL-04,16|S0/S4|NR-09, NR-12|E-BBC-01|Mapped|
|D04 Viewer-Legible Event Check|RL-01,05|S4 Shootability/Information|NR-01, NR-07|E-AN-01|Mapped|
|D05 Inner-State Externalisation Prompt|RL-02,06|S4 Shootability|NR-01, NR-02|E-AN-01|Mapped|
|D06 Goal–Obstacle Trace|RL-07,20|S3 Function/Resistance|NR-04, NR-09|E-AN-01|Mapped|
|D07 Action–Dialogue Information Allocation|RL-05,14|S4 Information|NR-02, NR-07, NR-08|E-AN-01|Mapped|
|D08 Draft-Form Authority Boundary|RL-04,16|S0/S4|NR-09, NR-12|E-AN-01|Mapped|
|D09 Dialogue Friction Check|RL-07–10|S3/S4|NR-04, NR-08|E-WGF-01|Mapped|
|D10 Subtext-by-Displacement Option|RL-06,13|S4 Dialogue/Information|NR-02, NR-07, NR-08|E-WGF-02|Mapped, remains optional inside conditions|
|D11 Clue-Scaled Exposition|RL-13,14|S4 Information|NR-02, NR-07|E-WGF-04|Mapped|
|D12 Contextual Speech-Pressure Map|RL-15|S4 Dialogue|NR-08|E-WGF-03|Mapped|
|D13 Leave Performable Space|RL-15|S0/S4 role boundary|NR-08, NR-09|E-WGF-03|Mapped|
|D14 Scene Function-and-Change Questions|RL-08,10|S3/S5|NR-04, NR-05|E-SN-01|Mapped|
|D15 Character-Action State Shift|RL-03,09,10,21|S3/S5|NR-03, NR-05, NR-06|E-SN-01; E-SN-02|Mapped|
|D16 Beginning-and-End Anchor Option|RL-11|S5|NR-06|E-SN-01|Mapped, remains optional inside conditions|
|D17 Entry Context Check|RL-12,21|S5 Entry|NR-06|E-SN-01|Mapped|
|D18 Exit-on-Changed-Pressure Check|RL-11,12|S5 Exit|NR-06|E-SN-01|Mapped|
|D19 Production-Burden Flag|RL-17,18,20|S6|NR-10|E-FI-02|Mapped|
|D20 Early Production-Consultation Handoff|RL-17,19|S6/S7|NR-10|E-FI-01; E-FI-02|Mapped|
|D21 Location-Equivalence Trade-off Test|RL-18,19|S6|NR-10|E-FI-01; E-FI-02|Mapped, remains optional inside conditions|

## Final Rule Trace Check

|Final rule|Relationship traced|Method traced|Evidence present|Result|
|---|---|---|---|---|
|NR-01|RL-01,02|D01,D04,D05|Yes|PASS|
|NR-02|RL-02,05,06,13,14|D01,D05,D07,D10,D11|Yes|PASS|
|NR-03|RL-03|D02,D15|Yes|PASS|
|NR-04|RL-07,08|D06,D09,D14|Yes|PASS|
|NR-05|RL-03,09,10|D02,D14,D15|Yes|PASS|
|NR-06|RL-11,12,21|D15,D16,D17,D18|Yes|PASS|
|NR-07|RL-05,13,14|D04,D07,D10,D11|Yes|PASS|
|NR-08|RL-07–10,13–15|D07,D09,D10,D12,D13|Yes|PASS|
|NR-09|RL-04,16|D03,D06,D08,D13–D18|Yes; hierarchy marked synthesis|PASS|
|NR-10|RL-17–20|D19,D20,D21|Yes|PASS|
|NR-12|RL-04,16|D03,D08|Yes|PASS|

## Orphan Check

- SW-C mappings: `15 / 15`, including SW-C14 as Deferred interface.
- SW-D mappings: `21 / 21`.
- Final Studio Rules with relationship → method → source trace: `11 / 11`.
- Orphan methods: `0`.
- Unsupported final Studio Rules: `0`.

