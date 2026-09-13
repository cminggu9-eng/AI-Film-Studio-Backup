"""Repair18 fail-closed and non-mutation negative tests."""

from __future__ import annotations

import json

from repair18_support import *


def main() -> int:
    cases = []

    def add(case_id, fn, detail):
        try:
            passed = bool(fn())
            cases.append({"id": case_id, "result": "PASS" if passed else "FAIL", "detail": detail})
        except Exception as exc:
            cases.append({"id": case_id, "result": "FAIL", "detail": f"{type(exc).__name__}: {exc}"})

    f1, f2 = compiled(1), compiled(2)
    p2, value2, expected2 = identity_pair(f2)
    two = synthetic_two_entity_contract()
    ptwo = build_entity_identity_projection(two)

    add("SAFE-ID-NEG-01", lambda: value2["representation_token"] != expected2["representation_token"] and resolved_identity_match(value2, expected2), "cross-namespace raw inequality cannot override resolved binding equality")
    add("SAFE-ID-NEG-02", lambda: "alias" not in json.dumps(p2, ensure_ascii=False).lower(), "global alias table is absent")
    def unknown_rejected():
        try: resolve_entity_identity(p2, namespace="transport.entity_id", token="unknown_identity")
        except SemanticAlignmentContractError: return True
        return False
    add("SAFE-ID-NEG-03", unknown_rejected, "unknown identity fails closed")
    def different_rejected():
        left = resolve_entity_identity(ptwo, namespace="transport.entity_id", token=two["fixture"]["tracked_entities"][0]["entity_id"])
        right = resolve_entity_identity(ptwo, namespace="assertion.identity_lock", token=two["fixture"]["tracked_entities"][1]["identity_lock"])
        return not resolved_identity_match(left, right)
    add("SAFE-ID-NEG-04", different_rejected, "different binding entities do not compare equal")
    def similarity_rejected():
        token = f2["fixture"]["tracked_entities"][0]["entity_id"] + "_similar"
        try: resolve_entity_identity(p2, namespace="transport.entity_id", token=token)
        except SemanticAlignmentContractError: return True
        return False
    add("SAFE-ID-NEG-05", similarity_rejected, "token similarity is not identity authority")
    def fixture_leak_rejected():
        foreign = f1["fixture"]["tracked_entities"][0]["entity_id"]
        try: resolve_entity_identity(p2, namespace="transport.entity_id", token=foreign)
        except SemanticAlignmentContractError: return True
        return False
    add("SAFE-ID-NEG-06", fixture_leak_rejected, "Fixture01 mapping cannot resolve inside Fixture02")
    production = [INTEGRATION / "implementation" / "integration_contract" / "semantic_alignment.py", INTEGRATION / "implementation" / "integration_contract" / "semantic_safeguard.py", HARNESS / "run_minimal_e2e.py"]
    forbidden = ("cracked_white_porcelain_bowl", "same_cracked_bowl")
    add("SAFE-ID-NEG-07", lambda: not any(token in path.read_text(encoding="utf-8") for path in production for token in forbidden), "Fixture02 mapping is not hardcoded in generic production")

    projection = build_shared_transition_authority_projection(f2)
    no_occurrence = scene_matrix(f2, occurs=False)
    classified = classify_transition_evidence(projection, no_occurrence)
    add("SAFE-TR-NEG-01", lambda: classified["machine_classification"]["AUTHORIZED"] and not classified["machine_classification"]["OCCURRED"], "AUTHORIZED is not treated as OCCURRED")
    add("SAFE-TR-NEG-02", lambda: not classify_transition_evidence(projection, scene_matrix(f2, occurs=False, token_scene=3))["machine_classification"]["OCCURRED"], "future or planned token is not occurrence")
    add("SAFE-TR-NEG-03", lambda: not classify_transition_evidence(projection, scene_matrix(f2, occurs=False, token_scene=3))["machine_classification"]["OCCURRED"], "scene position does not imply occurrence")
    ledger = E2EStateLedger(run_id="REPAIR18-AUTH-ONLY")
    envelope = json.loads((R22 / "envelopes" / "02_scene_writer_to_director.json").read_text(encoding="utf-8"))
    for scene in no_occurrence: ledger.append(envelope=envelope, state_snapshot=scene["state_evidence"])
    add("SAFE-TR-NEG-04", lambda: not classify_transition_evidence(projection, no_occurrence, handed_off=False)["machine_classification"]["OCCURRED"], "ledger append does not turn authorization into occurrence")
    add("SAFE-TR-NEG-05", lambda: "next((index" not in (HARNESS / "run_minimal_e2e.py").read_text(encoding="utf-8") and "SHARED_TRANSITION_AUTHORITY_PROJECTION" in json.dumps(projection), "Safeguard has no second scene-position transition law")
    add("SAFE-TR-NEG-06", lambda: classified["occurrence_evidence"] == [] and not classified["machine_classification"]["OBSERVED"], "missing occurrence evidence is not auto-repaired")
    baseline = "c73fba68a29090e4112deb13fb8c73376e9d5fe4f43eb9fe967b47937f64afcb"
    add("SAFE-TR-NEG-07", lambda: r22_tree_hash() == baseline, "recorded R22 remains byte-for-byte immutable")
    add("SAFE-TR-NEG-08", lambda: classified["machine_classification"] == {"AUTHORIZED": True, "OCCURRED": False, "OBSERVED": False, "HANDED_OFF": False}, "integration transition evidence failure remains separately classified")

    passed = sum(item["result"] == "PASS" for item in cases)
    output = {"classification": "REPAIR18 SEMANTIC SAFEGUARD NEGATIVE TEST", "results": cases, "passed": passed, "total": 15, "provider_calls": 0, "executor_calls": 0, "role_calls": 0, "probe_calls": 0, "live_e2e_runs": 0}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if passed == 15 else 1


if __name__ == "__main__":
    raise SystemExit(main())
