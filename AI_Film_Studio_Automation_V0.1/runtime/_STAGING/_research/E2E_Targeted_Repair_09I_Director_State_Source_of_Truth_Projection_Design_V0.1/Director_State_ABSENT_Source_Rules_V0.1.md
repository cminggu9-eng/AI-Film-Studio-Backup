# Director State ABSENT Source Rules V0.1

For all five fields, `ABSENT` is lawful only if the selected, approved source contract explicitly establishes that the field has no applicable source value. It is not a substitute for unknown data, unselected competing records, failed projection, malformed source, or missing required evidence. `null` and `{}` are distinct and invalid as absence substitutes.

Current consequence: a missing source-selection rule is a fail-closed authority gap, not permission to emit `ABSENT`.

