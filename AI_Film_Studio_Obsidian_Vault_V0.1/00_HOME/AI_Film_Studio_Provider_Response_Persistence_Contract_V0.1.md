# AI Film Studio Provider Response Persistence Contract V0.1

## Scope

This contract applies to a real role invocation after the provider has returned a response and before any local JSON, role, state, structural, or semantic validation is allowed to reject it. It is transport evidence only; it does not alter creative material or repair a provider response.

## Ordering Contract

1. Receive the provider response and usage metadata.
2. Persist the raw provider content and invocation metadata under the run-local `artifacts/` directory.
3. Verify both persisted artifacts are readable and associated with the exact invocation ID.
4. Record the invocation ledger entry.
5. Parse and validate locally.
6. If parsing or validation fails, create a separate validation-error artifact without replacing the provider evidence.

## Required Artifacts

- `<role>_provider_response.json`: verbatim `raw_content`, provider/model, provider invocation ID, and SHA-256.
- `<role>_invocation.json`: request time, usage, latency, fixture/run attribution, and persistence status.
- `<role>_persistence_verification.json`: artifact readability and invocation-ID linkage.
- `<role>_validation_error.json`: local failure category, stage, and detail when applicable.

## Non-Negotiable Rules

- Persistence precedes JSON parsing and every role-specific gate.
- Provider success and local validation success are independently recorded.
- No retry, fallback, prompt rewrite, semantic repair, or raw-response mutation is implied by a local failure.
- Canonical Skills, production locks, Showrunner content, and downstream roles are outside this contract.

## Implementation Boundary

Implemented in `runtime/shared_qa/model_executor.py` and the run-local persistence helper at `runtime/_STAGING/_research/E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1/implementation/provider_response_persistence.py`.

