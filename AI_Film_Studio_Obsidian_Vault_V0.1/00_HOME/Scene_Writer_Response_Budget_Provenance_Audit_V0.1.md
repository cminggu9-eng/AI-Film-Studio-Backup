# Scene Writer Response Budget Provenance Audit V0.1

## Finding

The failed `SW-CONTRACT-PROBE-01` 3,500 completion-token value was an **explicit integration-runner invocation value**, not a provider-imposed limit, Model Executor default, environment setting, or `studio.config.json` value.

| Layer | Finding |
| --- | --- |
| Caller | `CanonicalRoleExecutor.invoke()` in the Minimal E2E staging runner constructed the Scene Writer `ModelRequest` with `max_tokens=3500`. Probe 01 did not supply an override. |
| Model Executor | `ModelRequest.max_tokens` is required; it has no default budget policy. |
| Provider adapter | `DeepSeekProviderAdapter` forwards `request.max_tokens` unchanged as the Chat Completions `max_tokens` payload field. It had no local output ceiling. |
| Environment/config | No response-budget setting exists in `studio.config.json` or the inspected runtime config paths. |
| Probe-specific config | Probe 01 had no specific response-budget override. |

## Provider Capability Evidence

The current adapter exposes `deepseek-v4-pro` with `max_tokens` as the request parameter and records the provider-documented maximum output as 384,000 tokens. This was verified from the current official [DeepSeek Models & Pricing documentation](https://api-docs.deepseek.com/quick_start/pricing/) on 2026-08-28; it is not inferred from prior memory. The current adapter does not enforce a lower ceiling itself.

The official [Chat Completions documentation](https://api-docs.deepseek.com/api/create-chat-completion/) also states that `finish_reason: length` means the requested output or context boundary was reached, and that partial JSON can result. Repair 02 now captures this field.

## Conclusion

The 3,500 cap was a framework invocation policy error for a large structured deliverable, not a model maximum. Its 5,000-token replacement remains explicitly bounded below both the Repair 02 local ceiling (6,000) and the provider-documented maximum.

