---
type: deepseek-strict-node-anchor-linter-update
status: complete
version: 0.1
---

# DeepSeek Strict Node-Anchor Linter Update V0.1

The recursive strict linter now enforces `NODE_ANCHOR_REQUIRED` on every schema node. A node must contain at least one of `type`, `anyOf`, or `$ref`.

Existing checks remain in force:

- every object property is required;
- every object has `additionalProperties: false`;
- `minLength`, `maxLength`, `minItems`, and `maxItems` are rejected;
- unknown keywords are surfaced as unverified;
- `properties`, `items`, `anyOf`, `$defs`, and `$ref` are traversed recursively.

String-valued enums must declare `type: string`; malformed domains and string-type/value mismatches receive explicit linter codes. A bare `enum: ["ABSENT"]` now fails rather than receiving a false PASS.

