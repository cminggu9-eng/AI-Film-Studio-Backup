---
type: showrunner-transport-hydration-contract
status: implemented-and-offline-validated
version: 0.1
date: 2026-08-28
scope: showrunner-to-scene-writer-integration-only
---

# Showrunner｜Transport Hydration Contract V0.1

## Implementation boundary

Staging-only adapter:

`AI_Film_Studio_Automation_V0.1/runtime/_STAGING/_research/E2E_Targeted_Repair_04_Showrunner_Transport_Ownership_Separation_V0.1/implementation/showrunner_transport_hydration.py`

Canonical Showrunner Skill, Production Lock, and all downstream role contracts are untouched.

## Required sequence

1. Persist raw Provider response and usage.
2. Parse the role response.
3. Validate exact Showrunner-owned semantic payload.
4. Hydrate only lawful integration-owned transport fields.
5. Insert `scene_packages: "ABSENT"` only when the four sentinel conditions hold.
6. Validate full E2E transport schema.
7. Run semantic / authority gates.
8. Permit Scene Writer eligibility only after all prior gates pass.

## Adapter contract

Input is a parsed Showrunner response with all nine role-owned fields. `scene_packages` is optional at adapter input only. Output is a deep-copied full E2E transport object plus evidence of any inserted transport field.

| Condition | Result |
| --- | --- |
| Every role-owned field is present and `scene_packages` is absent; no Scene Writer artifact exists | Insert literal `ABSENT`; record `INTEGRATION_TRANSPORT_ABSENCE_SENTINEL`. |
| A role-owned field is missing or invalid | Fail before hydration; do not infer it from content. |
| A Scene Writer artifact exists but `scene_packages` is absent | Fail; adapter may not erase or misrepresent a downstream package. |
| `scene_packages` already exists | Preserve byte-for-value; never replace it. Full E2E validation decides whether its value is lawful for Showrunner. |

## Token and semantic integrity

The adapter makes no mutation to `primary_state_or_outcome`, `flags`, `handoffs`, locks, prohibitions, required outcome, unresolved decisions, state evidence, or content. Its evidence record declares `semantic_mutation: 0` and `canonical_token_mutation: 0`.
