# Scene Writer Strict Transport Provider Capability Audit V0.1

## Result

`AVAILABLE FOR THE LIMITED VALIDATION PATH`

Checked on 2026-08-28 against current official DeepSeek documentation.

| Requirement | Result | Verified condition |
| --- | --- | --- |
| `deepseek-v4-pro` Tool Calls | PASS | The current model reference lists Tool Calls support. |
| Strict function mode | PASS | Strict mode is documented for function tools. |
| Endpoint condition | PASS | Strict mode requires `https://api.deepseek.com/beta`. |
| Forced function syntax | PASS | `tool_choice` accepts `{ "type": "function", "function": { "name": "submit_scene_writer_package" } }`. |
| Schema subset | PASS | Object, string, number, integer, boolean, array, enum, and `anyOf` are documented; object properties are required and `additionalProperties` must be `false`. |

## Binding Decision

The Integration layer defines a provider-neutral `StructuredOutputContract`. Only `runtime/shared_qa/deepseek_provider_adapter.py` maps it to DeepSeek `tools`, `function.strict: true`, forced `tool_choice`, and the Beta endpoint. The canonical `scene-writer` Skill contains no DeepSeek syntax.

`BETA_PROVIDER_FEATURE_USED = YES`

This is isolated to the strict-function Scene Writer validation request. It is not a global provider configuration change and does not assert production readiness.

## Supported-subset limitation

DeepSeek strict mode currently rejects `minLength`, `maxLength`, `minItems`, and `maxItems`. The provider schema therefore does not include those keywords. Exact scene count, non-empty text, and the existing compact character limits remain post-parse local contract checks; there is no fallback to `json_object`.

## Sources

- [DeepSeek Tool Calls / Strict Mode](https://api-docs.deepseek.com/guides/tool_calls/)
- [DeepSeek Chat Completions API](https://api-docs.deepseek.com/api/create-chat-completion/)
- [DeepSeek Models and Pricing](https://api-docs.deepseek.com/quick_start/pricing/)
