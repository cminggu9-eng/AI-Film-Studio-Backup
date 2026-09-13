# Art Director Failure Classification Contract V0.1

Date: 2026-08-31  
Result: ALIGNED

## Ordered classification

1. Provider or transport absence: Provider / transport failure.
2. Parse failure: Executor / parse failure.
3. Exact field, type, lawful-absence, prompt/schema/validator identity, or validator-drift failure: `INTEGRATION OUTPUT-CONTRACT / VALIDATOR ALIGNMENT FAILURE`.
4. Canonical token violation: canonical role semantic failure.
5. Authority takeover or lock mutation: authority / handoff contract failure.

The Art Director integration validator now runs before generic semantic checks. A structurally present provider response that is permitted by the provider-facing schema cannot be relabeled `ROLE SEMANTIC FAILURE` solely because a local validator invented a stricter assertion.

E2E-RUN-15's historical attribution remains immutable. The corrected analysis is additive and does not retroactively mark the run PASS.

