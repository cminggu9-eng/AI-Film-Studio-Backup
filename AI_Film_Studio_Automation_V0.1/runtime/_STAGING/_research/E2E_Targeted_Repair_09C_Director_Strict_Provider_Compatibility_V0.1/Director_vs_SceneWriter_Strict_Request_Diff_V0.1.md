# Director versus Scene Writer Strict Request Diff

Both use the same endpoint/wrapper/strict flag/forced tool choice. Director's original schema uniquely used `minLength` and `const`; successful Scene Writer's documented strict subset excludes `minLength` and does not use `const`. Both use objects, required fields, enums, arrays, `anyOf`, and `additionalProperties:false`.
