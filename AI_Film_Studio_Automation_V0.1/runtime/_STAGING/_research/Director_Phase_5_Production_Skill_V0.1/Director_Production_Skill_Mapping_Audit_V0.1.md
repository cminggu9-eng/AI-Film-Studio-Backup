---
type: audit
status: passed-awaiting-user-review
review_result: passed
version: 0.1
subject: Director Production Skill mapping
---

# Director Production Skill Mapping Audit V0.1

## Capability Mapping

| ID | Required capability | Skill destination | Result |
| --- | --- | --- | --- |
| C01 | Scene intent | Scene Intent and Audience Information | PASS |
| C02 | Audience information | Scene Intent and Audience Information | PASS |
| C03 | Spatial geography | Spatial Geography and Blocking | PASS |
| C04 | Blocking | Spatial Geography and Blocking | PASS |
| C05 | Visual emphasis | Visual Emphasis, Camera, and Coverage | PASS |
| C06 | Reveal and conceal | Visual Emphasis, Camera, and Coverage | PASS |
| C07 | Camera purpose | Visual Emphasis, Camera, and Coverage | PASS |
| C08 | Camera movement purpose | Visual Emphasis, Camera, and Coverage | PASS |
| C09 | Coverage purpose | Visual Emphasis, Camera, and Coverage | PASS |
| C10 | Coverage density and variation | Visual Emphasis, Camera, and Coverage | PASS |
| C11 | Composition, partial scope | Visual Emphasis, Camera, and Coverage | PASS — emphasis plus why only |
| C12 | Rhythm | Rhythm, Transition, and Production Burden | PASS |
| C13 | Transition intent | Rhythm, Transition, and Production Burden | PASS |
| C14 | Director Entry/Exit Rules | Known Capability Gaps | PASS — `NO EVIDENCE / NOT DISTILLABLE` |
| C15 | Production burden | Rhythm, Transition, and Production Burden | PASS |
| C16 | Authority lock | Authority Lock | PASS |
| C17 | Role boundary | Role Boundaries and Handoffs | PASS |
| C18 | Context handling | Intake and Context Gate | PASS |
| C19 | Output protocol | Output | PASS |
| C20 | External production constraint input | Known Capability Gaps | PASS — `DEFERRED` |

## Decision Mapping

| ID | Decision capability | Skill destination | Result |
| --- | --- | --- | --- |
| D01 | Authority resolution | Authority Lock | PASS |
| D02 | Intent lock | Scene Intent and Audience Information | PASS |
| D03 | Audience-information choice | Scene Intent and Audience Information | PASS |
| D04 | Geography choice | Spatial Geography and Blocking | PASS |
| D05 | Blocking choice | Spatial Geography and Blocking | PASS |
| D06 | Visual emphasis choice | Visual Emphasis, Camera, and Coverage | PASS |
| D07 | Reveal/conceal choice | Visual Emphasis, Camera, and Coverage | PASS |
| D08 | Camera-purpose choice | Visual Emphasis, Camera, and Coverage | PASS |
| D09 | Movement-purpose choice | Visual Emphasis, Camera, and Coverage | PASS |
| D10 | Coverage choice | Visual Emphasis, Camera, and Coverage | PASS |
| D11 | Rhythm choice | Rhythm, Transition, and Production Burden | PASS |
| D12 | Transition choice | Rhythm, Transition, and Production Burden | PASS |
| D13 | Practicality choice | Rhythm, Transition, and Production Burden | PASS |
| D14 | Context-block decision | Intake and Context Gate | PASS |
| D15 | Handoff decision | Role Boundaries and Handoffs; Primary State | PASS |
| D16 | Completion/state decision | Primary State; Completion Rule | PASS |

## Promoted Rule Mapping

| Rule | Skill destination | Result |
| --- | --- | --- |
| R01 Authority before style | Authority Lock | PASS |
| R02 Do not change locked scene material | Authority Lock | PASS |
| R03 Do not begin camera-first | Decision Sequence | PASS |
| R04 Audience information is explicit | Scene Intent and Audience Information | PASS |
| R05 Geography and blocking serve drama | Spatial Geography and Blocking | PASS |
| R06 Camera and movement need purpose | Visual Emphasis, Camera, and Coverage | PASS |
| R07 Coverage is not a fixed template | Visual Emphasis, Camera, and Coverage | PASS |
| R08 Rhythm and transition are intent, not final edit | Rhythm, Transition, and Production Burden | PASS |
| R09 Practicality cannot remove required material | Rhythm, Transition, and Production Burden | PASS |
| R10 Respect downstream ownership | Role Boundaries and Handoffs | PASS |

## Exact Contract Mapping

- Modes: `PLAN`, `REVISE`, `DIAGNOSE` — 3/3 exact.
- Primary States: `DIRECTION_PLAN_PRODUCED`, `DIRECTION_PLAN_REVISED`, `NO_MATERIAL_DIRECTION_CHANGE`, `NEEDS_CONTEXT`, `UPSTREAM_DECISION_REQUIRED`, `OUT_OF_SCOPE_HANDOFF` — 6/6 exact.
- Handoff architecture: upstream Showrunner, Canon/story, Scene Writer material conflict; downstream DP, Character & Acting, Art Director, Editor/Post, Continuity, Production — preserved.

**PASS — C01–C20, D01–D16, and the ten promoted rules map to a specific executable section without capability loss or expansion.**
