# Adapter Strict Contract Wiring Provenance Audit

Repair 10 introduced `build_provider_payload()` and correctly defined `strict_contract` there. `complete()` later interpreted the response using the old unbound name, producing E2E-RUN-11's pre-send NameError. Repair 10A explicitly derives `strict_contract = request.structured_output` in `complete()`.
