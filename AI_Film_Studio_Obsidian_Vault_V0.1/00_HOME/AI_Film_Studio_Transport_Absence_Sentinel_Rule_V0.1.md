---
type: transport-absence-sentinel-rule
status: defined-and-offline-validated
version: 0.1
date: 2026-08-28
scope: integration-transport-only
---

# AI Film Studio｜Transport Absence Sentinel Rule V0.1

## Rule

Integration may write literal `ABSENT` only when all four conditions are true:

1. The missing field is classified as integration transport-owned.
2. The current role cannot lawfully own that field’s semantic content.
3. No downstream artifact that could populate the field exists.
4. Absence is determined from the execution boundary, not inferred from prose, tone, or an unstated fact.

The sentinel means `TRANSPORT SLOT NOT POPULATED AT THIS STAGE` only. It is not a canonical Mode, Primary State, Flag, Handoff, role outcome, or creative decision.

## Showrunner application

At the Showrunner-to-Scene Writer boundary, `scene_packages` is a generic E2E transport slot whose content is owned only by Scene Writer. Before a Scene Writer artifact exists, the adapter inserts `scene_packages: "ABSENT"` and records origin `INTEGRATION_TRANSPORT_ABSENCE_SENTINEL`.

## Prohibitions

- Never add a missing Story / Canon / assignment / knowledge / relationship / required-outcome / prohibition field.
- Never derive a field from normal prose.
- Never translate, alias, merge, normalize, or invent canonical tokens.
- Never overwrite an existing downstream package with `ABSENT`.
- Never convert `null`, an empty object, or an empty array into `ABSENT`.
- Never apply this rule to another role merely by analogy.

## Enforcement

The Showrunner adapter first validates all role-owned fields. Only then does it hydrate the integration-owned slot. A downstream-exists guard rejects missing-slot hydration after a Scene Writer artifact exists; a pre-existing `scene_packages` value is preserved untouched and subsequently remains subject to full-schema validation.
