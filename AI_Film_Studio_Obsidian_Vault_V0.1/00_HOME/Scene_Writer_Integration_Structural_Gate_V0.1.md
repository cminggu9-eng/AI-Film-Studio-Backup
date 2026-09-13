# Scene Writer Integration Structural Gate V0.1

## Purpose

The structural gate evaluates only deterministic Scene Writer integration obligations after provider JSON parsing. It is not a creative evaluator and it contains no rewrite path.

## Gate Order

1. Provider evidence persistence.
2. Provider JSON parse.
3. Generic role output validation.
4. Scene Writer integration state and structural validation.
5. Existing semantic safeguard as a separate reporting layer.

## Required Checks

- Exactly three fixture scene packages with valid IDs.
- Exact package, state-evidence, and source-attribution field sets.
- Six explicit structural-deliverable keys per scene.
- Exact machine clothing tokens and authorized transition.
- Exact canonical reveal tokens.
- No package-level surplus keys.

## Attributable Outcomes

The gate returns diagnostic codes such as `MISSING_STRUCTURAL_DELIVERABLE`, `MISSING_MACHINE_STATE_CODE`, and `REQUIRED_STATE_MISMATCH`. It cannot correct the response, infer facts, translate canonical tokens, invoke another provider, or dispatch a downstream role.

## Historical Regression

The frozen `E2E-RUN-01-RECOVERY-01` Scene Writer output is expected to fail this gate because it used display prose (`湿透制服`) where `soaked_uniform` was required and did not provide all six structured fields.

