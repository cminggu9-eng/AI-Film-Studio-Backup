---
type: deepseek-strict-schema-conformance-linter
status: requires-one-follow-up-rule
version: 0.1
official_source: https://api-docs.deepseek.com/guides/tool_calls/
---

# DeepSeek Strict Schema Conformance Linter V0.1

## Official basis

The linter is limited to DeepSeek's strict-mode documentation. The official guide lists object, string, number, integer, boolean, array, enum, and `anyOf`; requires every object property to appear in `required`; requires `additionalProperties: false`; and documents `minItems` / `maxItems` as unsupported. Its enum example is typed (`type: string` plus `enum`).

## Current checks

`implementation/deepseek_strict_linter.py` recursively checks object requiredness, `additionalProperties: false`, `minLength`, `maxLength`, `minItems`, `maxItems`, unknown keywords, nested `properties`, `items`, `anyOf`, `$defs`, and `$ref` traversal.

## Post-probe correction required

The original pass was incomplete: it accepted an enum-only node. Probe 03's raw DeepSeek error adds an observed server rule: each submitted schema node must contain one of `type`, `anyOf`, or `$ref`. The linter must add this check in the next targeted repair; it must classify the rule as an observed-provider constraint alongside the official source rather than silently treating enum-only nodes as valid.

## Do not use as a pass certificate

Because of that demonstrated coverage gap, the prior `Director projected schema PASS` is superseded. This repair does not claim the 16/16 offline gate.

