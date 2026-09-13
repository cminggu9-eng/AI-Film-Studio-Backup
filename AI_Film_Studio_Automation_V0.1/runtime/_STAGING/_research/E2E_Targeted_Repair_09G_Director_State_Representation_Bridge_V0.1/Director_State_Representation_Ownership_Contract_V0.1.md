# Director State Representation Ownership Contract V0.1

## Established ownership

| Boundary | Established owner | Established representation |
|---|---|---|
| Director semantic production | Director role | state objects |
| DeepSeek 09C projection | integration compatibility layer | JSON-object strings for five fields |
| 09F validator output | local validation layer | decoded state objects |
| State Evidence Envelope and E2E output | downstream transport | JSON-safe values, observed as objects |

## Missing ownership

No reviewed contract assigns an Integration layer responsibility for deterministic object-to-string serialization before the State Evidence Envelope. No reviewed downstream consumer requires a string-only representation.

The desired invariant, `ROLE OWNS SEMANTIC OBJECT; INTEGRATION OWNS DETERMINISTIC SERIALIZATION; DOWNSTREAM OWNS ONE CANONICAL STRING`, cannot be adopted as fact under this repair authority. Its final clause conflicts with observed current downstream artifacts and has no authoritative contract source.

## Required separate authority

A different targeted repair must establish, before code changes:

1. the canonical representation at the State Evidence / Ledger / Handoff boundary (object or string);
2. the owning integration component and exact handoff boundary; and
3. the approved nested semantic schema for each of the five state objects.

Until then, preserving the current object downstream behavior is the only evidence-backed action.

