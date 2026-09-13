"""Pure offline corrected replay of immutable Probe22 provider evidence."""
from __future__ import annotations

import json
from repair23_support import *
from repair22_support import canonical_validator as legacy_probe_validator


def main() -> int:
    _, contract = state_contract()
    raw_arguments = probe22_arguments()
    projection = authoritative_projection()

    wire = validate_director_provider_wire_arguments(raw_arguments, contract)
    decoded = decode_director_provider_wire_arguments(wire, contract)
    canonical = canonical_validator(contract, projection)(decoded)
    corrected = e2e.validate_role_output(
        e2e.role_spec("director"),
        canonical,
        projection["canon_assignment_locks"],
        projection["prohibited_changes"],
        run_id="DIRECTOR-TAGGED-WIRE-PROBE-22-F03-CORRECTED-OFFLINE-REPLAY",
    )

    legacy = legacy_probe_validator(contract)(decoded)
    source_scene = read_json(R26_SCENE_WRITER)
    source_input = read_json(R26_DIRECTOR_INPUT)["input"]["upstream_artifacts"]["scene_writer"]
    original = read_json(PROBE22_MANIFEST)
    locks_absent_from_provider_contract = "canon_assignment_locks" not in raw_arguments
    result = {
        "classification": "REPAIR23 PROBE22 CORRECTED OFFLINE REPLAY",
        "overall": "PASS",
        "probe22_historical_result_preserved": original.get("overall") == "FAIL",
        "probe22_historical_failure": original.get("failure"),
        "raw_provider_response_sha256": sha256(PROBE22_RAW),
        "wire_validation": "PASS",
        "tagged_decode": "PASS",
        "canonical_15_field_validation": "PASS",
        "corrected_authoritative_handoff_validation": "PASS",
        "authoritative_source": projection["authority"],
        "projection_rule": projection["projection"],
        "source_scene_writer_equals_director_input_snapshot": source_scene["canon_assignment_locks"] == source_input["canon_assignment_locks"],
        "source_order_preserved": projection["canon_assignment_locks"] == source_scene["canon_assignment_locks"],
        "corrected_received_equals_sent": corrected["canon_assignment_locks"] == projection["canon_assignment_locks"],
        "corrected_prohibitions_equal": corrected["prohibited_changes"] == projection["prohibited_changes"],
        "legacy_probe_received_locks": legacy["canon_assignment_locks"],
        "authoritative_sent_locks": projection["canon_assignment_locks"],
        "real_transit_mutation": False,
        "provider_owned_lock_field": not locks_absent_from_provider_contract,
        "root_cause": "Probe22 independently rebuilt received locks from a one-lock fixture helper while sent/handoff validation used the immutable R26 Scene Writer six-lock authority.",
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "live_e2e_calls": 0,
    }
    required = (
        result["probe22_historical_result_preserved"],
        result["source_scene_writer_equals_director_input_snapshot"],
        result["source_order_preserved"],
        result["corrected_received_equals_sent"],
        result["corrected_prohibitions_equal"],
        locks_absent_from_provider_contract,
    )
    if not all(required):
        result["overall"] = "FAIL"
    e2e.write_json(REPORTS / "Repair23_Probe22_Corrected_Replay.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["overall"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
