# Director State DeepSeek Strict Schema Report V0.1

Result: **PASS**.

The strict projection recursively preserves every dynamic object, exact properties, exact required lists, nested string enums, and `additionalProperties:false`. It removes unsupported length keywords and projects fixed strings from `const` to `type:string` plus `enum:[value]`.

`proposed_state`, `knowledge_timing`, and `visual_state` are each exactly `{type:"string", enum:["ABSENT"]}`. No bare enum and no object branch exists for these fields. The linter checks every object, anyOf branch, and array item; unsupported `const`/length keywords are absent from final strict schemas.

Final schema identity passed for all three fixtures, and `strict:true`, forced `submit_director_package` tool choice, and adapter-scoped DeepSeek beta endpoint were captured before network send.
