# Director Provider Object Schema Contract V0.1

## Status: BLOCKED — exact object shapes are not authoritative

Provider objects are semantically supported by the 09B provider-neutral contract and by the E2E-RUN-14 raw response. However, 09G requires each object schema to have explicit properties, required keys, and `additionalProperties: false` using existing semantic shape constraints.

No canonical source supplies that exact schema. The R14 input has upstream-shaped state objects, while the R14 provider output adds `source` inside `relevant_prior_state`. Deriving an allowlist from that output would make the model response semantic authority; deriving one from the input would classify the observed extra key without an approved rule; inventing a union would be semantic guessing. All are prohibited by 09G.

Accordingly, this repair does not replace the DeepSeek string projection with a strict object schema. It also does not weaken it to an unrestricted generic object.

## Future prerequisite

An approved field-level state schema authority must specify, for each of the five fields, required and optional keys, forbidden keys, value/token domains, `ABSENT` rules, and the relationship to upstream state ownership. Only then can the schema, prompt, and Stage-A validator derive from one contract.

