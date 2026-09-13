# Semantic Safeguard Entity Identity Provenance Audit

Result: PASS.

The current-run authority chain is `fixture binding → compiled_run_contract.fixture.tracked_entities → CURRENT_RUN_ENTITY_IDENTITY_PROJECTION → typed PROP assertion → Semantic Safeguard`.

For E2E-FIX-02, `transport.entity_id = cracked_white_porcelain_bowl` and `assertion.identity_lock = same_cracked_bowl` are legal representations in different namespaces. Both originate from the same `tracked_entities[0]` record. No token wording, LLM inference, historical fixture rule, or manual alias table participates.

Unknown, ambiguous, or foreign representations fail closed.

