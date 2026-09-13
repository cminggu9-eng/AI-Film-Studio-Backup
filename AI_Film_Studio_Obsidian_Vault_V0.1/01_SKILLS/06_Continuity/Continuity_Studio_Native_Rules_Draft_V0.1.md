---
type: studio-native-rules-draft
role: continuity
phase: 3-verified-nuwa-cross-distillation
status: draft-not-capability-model
version: 0.1
huashu_nuwa_invocation: CT3-NUWA-CROSS-20260826-01
---

# Continuity Studio-Native Rules Draft V0.1

These are Phase 3 drafts, not a Capability Model, runtime contract, schema, or final token set.

| Rule ID | Class | Draft rule | Originating CT-D / relationship | CT-C mapping | Conditions | Authority boundary | Transferability |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CT-DR-01 | HARD | Treat only locatable supplied evidence as a continuity fact. | D01/D04/D08/D10; RL-01 | C01, C03, C05, C24, C27 | Claim has an input locator or explicit visual/action statement. | No Canon fact creation or inferred backstory. | DIRECT |
| CT-DR-02 | HARD | A detected discrepancy or missing support produces a flag/handoff, never repair, approval, or authorization. | D03/D04; RL-07, RL-12 | C20, C22-23, C29 | Supported concern or relevant evidence gap exists. | Owner decides; Continuity does not rewrite, retcon, or rank authorities. | DIRECT |
| CT-DR-03 | HARD | Do not conflate audience exposure with character knowledge. | D10/D16; RL-10 | C03, C18, C28 | Material distinguishes on-screen access, plot order, or character knowledge. | No belief, subtext, irony, or withheld information becomes fact. | CONDITIONAL |
| CT-DR-04 | HARD | Do not automatically classify marked or source-supported discontinuity, ellipsis, ambiguity, or nonlinearity as error. | D07/D12/D13/D15/D17; RL-08, RL-11 | C05, C07, C25, C27-28 | Specific marker or form evidence supports the exception. | No deviation authorization or interpretive ruling. | CONDITIONAL |
| CT-DR-05 | DEFAULT | Compare declared scene context separately from reconstructed story order. | D01/D08/D12/D13; RL-02 | C05, C07-08, C25 | Input supplies heading/timeframe and/or ordering evidence. | No unseen chronology construction. | CONDITIONAL |
| CT-DR-06 | DEFAULT | Compare physical, action, dialogue, costume, hair/make-up, prop, and emotional-continuity claims as named dimensions, not a single match judgment. | D02/D06; RL-05 | C10-17, C20, C24 | Relevant dimension is evidenced and decision-relevant. | No directing, performance prescription, or design takeover. | DIRECT |
| CT-DR-07 | DEFAULT | Keep designation, presence/source of voice, and condition as separate comparison dimensions. | D09/D11/D02; RL-06 | C02-03, C09, C16 | Input explicitly states at least one dimension. | No identity/alias or Canon decision. | DIRECT |
| CT-DR-08 | DEFAULT | Review spatial continuity as a relation among direction, eyeline, position, distance, movement, action, and presence. | D05/D06/D11; RL-04 | C08-09, C17, C29 | Relevant relation is explicitly available and matters to the assignment. | No camera, coverage, blocking, or sound solution. | CONDITIONAL |
| CT-DR-09 | CONDITIONAL | When a causal link is explicit, compare stated action/decision and resulting state without inventing a bridge event. | D13/D14/D15; RL-09 | C06-07, C20, C28 | Relation is locatable; absent links remain UNKNOWN. | No causal simulation or authorship. | CONDITIONAL |
| CT-DR-10 | CONDITIONAL | When a time-shift, montage, flashback, ellipsis, or subjective form is marked, record its evidentiary effect before comparing surrounding state. | D07/D12/D15/D17; RL-08, RL-11 | C05, C07, C25, C27-28 | Specific marker/form condition is supplied. | No montage construction, edit instruction, or automatic exception. | CONDITIONAL |
| CT-DR-11 | CONDITIONAL | A perceptual spatial concern is reviewable only after checking whether supported formal discontinuity changes its meaning. | D05/D06/D07; RL-13 | C08, C16-17, C20, C25 | Both spatial relation and possible formal exception are evidenced. | No editorial correction or materiality/severity ruling. | CONDITIONAL |
| CT-DR-12 | CONDITIONAL | Where evidence is absent, retain uncertainty and route the question rather than completing the state. | D03/D10/D15/D17; RL-03, RL-07, RL-08 | C01, C03, C19, C20, C27-29 | Decision-relevant unknown remains after supplied-evidence check. | C19 remains WEAK; no state-mutation, retcon, or authorization method is created. | DIRECT |
| CT-DR-13 | OPTIONAL | Use frozen reference material to make a before/after comparison traceable, without requiring a particular record form or system. | D01/D04; RL-01, RL-12 | C05, C07, C24, C27 | Reference material already exists in the assignment/input. | No tracker, schema, database, or Runtime creation. | DIRECT |
| CT-DR-14 | OPTIONAL | Surface owner-relevant change context together with exact evidence locator and exception condition. | D03/D07/D17; RL-07, RL-08 | C20, C22-23, C25, C29 | Concern needs cross-role review and source-supported context exists. | Routing only; no owner precedence or final decision. | CONDITIONAL |

## Classification count

| HARD | DEFAULT | CONDITIONAL | OPTIONAL | Total |
| ---: | ---: | ---: | ---: | ---: |
| 4 | 4 | 5 | 2 | 14 |

## Explicitly rejected candidate rules

- A universal state database or required fields.
- Internal approval of an otherwise consistent change.
- All mismatches are defects unless a producer approves them.
- Inference of unshown bridge events.
- Emotional-continuity-as-belief engine.
- Take/slate/coverage/camera requirements.
- Authority-precedence selection by Continuity.
- Severity tiers.
- Retcon or Canon-change resolution procedure.

