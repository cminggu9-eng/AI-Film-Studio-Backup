---
type: director-deepseek-strict-schema-lint-report
status: targeted-repair-required
version: 0.1
---

# Director DeepSeek Strict Schema Lint Report V0.1

## Initial offline result

The initial linter reported PASS after projection: all object branches had exact `required` sets and `additionalProperties: false`; forbidden length/item keywords were absent; the six state object values were represented as JSON strings and locally parsed fail-closed.

## Authoritative live finding

Probe 03 returned HTTP 400 before generation:

```text
Invalid tool parameters schema : one of `type`, `anyOf`, `$ref` field is required
```

The exact before-send schema contains the following nonconforming enum-only nodes:

| JSON Pointer | Present keywords | Required repair | Semantic impact |
| --- | --- | --- | --- |
| `/properties/flags` | `enum` | add `type: string` | none |
| `/properties/handoffs` | `enum` | add `type: string` | none |
| `/properties/unresolved_decisions/anyOf/0` | `enum` | add `type: string` | none |
| `/properties/state_evidence/properties/relevant_prior_state/anyOf/0` | `enum` | add `type: string` | none |
| `/properties/state_evidence/properties/current_state/anyOf/0` | `enum` | add `type: string` | none |
| `/properties/state_evidence/properties/proposed_state/anyOf/0` | `enum` | add `type: string` | none |
| `/properties/state_evidence/properties/knowledge_timing/anyOf/0` | `enum` | add `type: string` | none |
| `/properties/state_evidence/properties/relationship_state/anyOf/0` | `enum` | add `type: string` | none |
| `/properties/state_evidence/properties/visual_state/anyOf/0` | `enum` | add `type: string` | none |

Every affected enum has exactly the string value `ABSENT`. Adding the string type preserves its legal set exactly; it neither weakens requiredness nor removes a semantic field.

## Classification

`DIRECTOR STRICT PROVIDER TARGETED COMPATIBILITY REPAIR REQUIRED`.

