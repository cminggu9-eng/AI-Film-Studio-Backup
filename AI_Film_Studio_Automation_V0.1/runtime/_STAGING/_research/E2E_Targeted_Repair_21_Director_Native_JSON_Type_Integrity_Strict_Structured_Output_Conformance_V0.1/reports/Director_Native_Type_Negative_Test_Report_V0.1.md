# Director Native Type Negative Test Report V0.1

Result: **15 / 15 PASS**, provider calls: 0.

| Cases | Verified fail-closed behavior |
| --- | --- |
| NEG-01–04 | Stringified array/object is rejected; no `json.loads` normalization path exists |
| NEG-05–08 | `[]` remains a native array, while `"[]"`, `null`, and scalar wrapping do not become `ABSENT` or an array |
| NEG-09–11 | Native union loss, missing `strict:true`, and unforced tool choice are observable |
| NEG-12 | Legacy JSON-string state representation is unreachable |
| NEG-13 | R26 replay remains `BLOCKED` and immutable |
| NEG-14 | Schema-derived reminder contains no fixture-specific literal |
| NEG-15 | No automatic retry or provider fallback is available |

`[]` is accepted only as the schema-authorized native empty array; it is never treated as `ABSENT`.

