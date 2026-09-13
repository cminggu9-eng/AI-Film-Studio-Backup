---
type: director-provider-projection-equivalence-report
status: pending-minimal-typed-enum-projection
version: 0.1
---

# Director Provider Projection Equivalence Report V0.1

## Preserved by the 09C/09D projection

- All required fields remain present, including the eight Director machine semantic fields.
- Mode and primary-state enum domains are unchanged.
- Locks, prohibitions, handoffs, and absence semantics remain required inputs.
- `minLength` removal remains local-validator responsibility.
- The six state object values use a JSON-string wire representation and are parsed back to mappings by the local Director validator; malformed JSON or a non-object fails closed.

## Required next micro-projection

Transform only enum-only fixed-string nodes from:

```json
{ "enum": ["ABSENT"] }
```

to:

```json
{ "type": "string", "enum": ["ABSENT"] }
```

This is set equality over the accepted values, so it is semantically equivalent. It must be applied centrally in the `const`-to-enum projection, audited recursively, and covered by an updated linter rule before another Provider call.

## Gate status

The existing equivalence checks are valuable but insufficient because they presently assert the old enum-only representation. They must be updated together with the next projection, then rerun with the Repair 09B validator chain and the Unified Phase 2 gate.

