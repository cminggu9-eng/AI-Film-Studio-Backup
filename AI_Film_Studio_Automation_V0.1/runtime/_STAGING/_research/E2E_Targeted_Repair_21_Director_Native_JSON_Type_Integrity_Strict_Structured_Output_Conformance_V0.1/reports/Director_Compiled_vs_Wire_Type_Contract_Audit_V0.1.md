# Director Compiled vs Wire Type Contract Audit V0.1

The compiled, projected, current request-capture, and R26 final wire schemas are aligned. The exact 15 required fields are retained by the DeepSeek projection; no provider-facing schema branch reduces `unresolved_decisions` to an unrestricted string.

| Contract location | `unresolved_decisions` |
| --- | --- |
| Provider-neutral compiled schema | `const "ABSENT"` or `array` of non-empty strings |
| DeepSeek strict projection | `string enum ["ABSENT"]` or `array` of strings |
| R26 persisted final wire | Same `anyOf` native union |
| Current request capture | Byte-equivalent to the projected schema |
| Local validator | Exact runtime type check: `ABSENT` or Python list of non-empty strings |

The final wire contains `submit_director_package`, `strict:true`, and the exact forced function tool choice. No adapter or request-builder stringifies `unresolved_decisions`.

