# Director Per-Run State Schema Architecture V0.1

## Pipeline

`Fixture Binding -> Compiled Run Contract -> Validated Source Records/Ledger -> Projection Plan -> Five Strict Schemas + Authority Manifest`

For `relevant_prior_state` and `current_state`, the object branch is generated as:

```json
{
  "type": "object",
  "properties": {
    "<compiled scene id>": {
      "type": "object",
      "properties": {
        "<compiled state dimension>": {"type": "string", "enum": ["<compiled tokens>"]}
      },
      "required": ["<all compiled state dimensions>"],
      "additionalProperties": false
    }
  },
  "required": ["<all compiled scene ids>"],
  "additionalProperties": false
}
```

`relevant_prior_state` retains a typed `ABSENT` union branch under its explicit absence rule. `current_state` uses the object branch for a valid Director handoff. The other three fields currently compile to typed exact `ABSENT`.

Downstream remains object or exact `ABSENT`; no string bridge exists.

