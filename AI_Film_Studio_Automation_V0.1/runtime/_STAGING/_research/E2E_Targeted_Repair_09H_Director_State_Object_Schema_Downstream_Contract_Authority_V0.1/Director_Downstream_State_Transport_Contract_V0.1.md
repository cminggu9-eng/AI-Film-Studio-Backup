# Director Downstream State Transport Contract V0.1

## Authoritative decision

For the five fields, canonical State Evidence / Ledger / Handoff carriage is **JSON OBJECT or the exact `ABSENT` sentinel**.

## Basis

The role-neutral State Evidence contract accepts JSON-safe values and preserves them; the minimal E2E envelope copies objects directly; the ledger stores and compares supplied values; and the 09F validator decoded its legacy strings before envelope creation. No higher-authority source requires strings. This implements the 09H default direction and does not mutate runtime.

## Consequence

There is no authorized object-to-string-to-object bridge. 09C's string projection and 09F's decoder are classified as legacy Provider compatibility representation, not semantic or downstream canonical representation. Future Provider repair must emit objects directly only after the five exact schemas exist.

