# Director State Object Token Domains V0.1

## Established exact values

- `ABSENT` is the only approved absence sentinel for each outer State Evidence dimension. It is not an empty object and is never null.
- Fixture compiler token domains are dynamic: `state_dimensions[].allowed_tokens` and `authorized_transitions` come from the approved binding.
- Director canonical Mode and Primary State tokens are separately established at the outer payload level; they are not nested-state object tokens.

## Authority gap

No contract assigns compiled fixture domains to a particular property in any of the five Director objects. Therefore no nested enum list, alias, translation, or normalization is frozen here. Binding-derived tokens remain valid only at their existing Scene Writer / compiled-contract boundary.

