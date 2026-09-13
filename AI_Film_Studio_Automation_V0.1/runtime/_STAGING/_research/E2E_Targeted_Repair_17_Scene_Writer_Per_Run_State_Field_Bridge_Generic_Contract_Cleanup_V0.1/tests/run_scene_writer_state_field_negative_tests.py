"""Provider-free SW-STATE-NEG-01 through SW-STATE-NEG-15 for Repair17."""

from __future__ import annotations

import copy
import hashlib
import json

from repair17_support import (
    GENERIC_SOURCES,
    R21_RAW,
    compile_matrix,
    generic_source_leaks,
    project_recorded_transport_shape,
    r21_arguments,
    replay_r21,
)

from scene_writer_compact_serialization import normalize_compact_scene_writer_output
from scene_writer_scene_id_contract import assess_scene_id_sequence
from scene_writer_state_field_contract import state_field_name
from scene_writer_strict_transport import FUNCTION_DESCRIPTION, FUNCTION_NAME, validate_strict_scene_writer_arguments
import run_minimal_e2e as e2e


def rejected(action) -> bool:
    try:
        action()
    except Exception:
        return True
    return False


def main() -> int:
    compiled, scene_contracts, state_contracts, schemas = compile_matrix()
    fields = [state_field_name(item) for item in state_contracts]
    original = r21_arguments()
    f2 = project_recorded_transport_shape(original, state_contracts[1])
    wrong_field = copy.deepcopy(f2)
    for scene in wrong_field["scenes"]:
        scene["state"][fields[0]] = scene["state"].pop(fields[1])
    illegal_token = copy.deepcopy(f2)
    illegal_token["scenes"][0]["state"][fields[1]] = "FOREIGN_MACHINE_TOKEN"
    unknown_dimension = copy.deepcopy(f2)
    unknown_dimension["scenes"][0]["state"]["unknown_state_dimension"] = "invented"
    renamed_field = copy.deepcopy(f2)
    renamed_field["scenes"][0]["state"]["renamed_state"] = renamed_field["scenes"][0]["state"].pop(fields[1])

    def strict_rejects(value):
        return rejected(lambda: validate_strict_scene_writer_arguments(value, parameters_schema=schemas[1], scene_id_contract=scene_contracts[1], state_field_contract=state_contracts[1]))

    generic_text = "\n".join(path.read_text(encoding="utf-8") for path in GENERIC_SOURCES)
    prompt = e2e.build_system_prompt(
        e2e.role_spec("scene_writer"), "READ ONLY",
        structured_function_name=FUNCTION_NAME,
        structured_parameters_schema=schemas[1],
        scene_id_contract=scene_contracts[1],
        state_field_contract=state_contracts[1],
    )
    raw_hash = hashlib.sha256(R21_RAW.read_bytes()).hexdigest()
    replay = replay_r21()
    source_lower = generic_text.lower()

    results = []
    def add(case_id, passed, detail):
        results.append({"id": case_id, "result": "PASS" if passed else "FAIL", "detail": detail})

    add("SW-STATE-NEG-01", strict_rejects(wrong_field), "Fixture01 state field is rejected in Fixture02")
    add("SW-STATE-NEG-02", fields[1] not in generic_text, "Fixture02 field is not hardcoded in generic production source")
    add("SW-STATE-NEG-03", fields[2] not in generic_text, "Fixture03 field is not hardcoded in generic production source")
    add("SW-STATE-NEG-04", strict_rejects(wrong_field), "legal tokens written to the wrong field fail closed")
    add("SW-STATE-NEG-05", strict_rejects(illegal_token), "illegal token in the correct field fails closed")
    add("SW-STATE-NEG-06", "startswith(" not in source_lower and "token contains" not in source_lower and "token.startswith" not in source_lower, "token-prefix or token-content field inference is absent")
    reverse = [state_field_name(item) for item in reversed(state_contracts)]
    add("SW-STATE-NEG-07", reverse == list(reversed(fields)) and len(set(fields)) == 3, "previous fixture mappings do not leak into the next projection")
    add("SW-STATE-NEG-08", strict_rejects(unknown_dimension), "hydrator input cannot create an unknown state dimension")
    add("SW-STATE-NEG-09", strict_rejects(renamed_field), "serializer cannot rename the current-run state field")
    add("SW-STATE-NEG-10", "clothing_visual_state_code" not in generic_text, "validator has no legacy clothing field constant")
    add("SW-STATE-NEG-11", "A-17" not in prompt, "generic/current Fixture02 prompt contains no Fixture01 business literal")
    add("SW-STATE-NEG-12", "E2E-FIX-01" not in FUNCTION_DESCRIPTION and "probe" not in FUNCTION_DESCRIPTION.lower(), "generic function description contains no Fixture01 probe identity")
    add("SW-STATE-NEG-13", not generic_source_leaks(), "Fixture02 or Fixture03 literals did not replace Fixture01 as a new hardcode")
    add("SW-STATE-NEG-14", replay["raw_machine_tokens"] == replay["hydrated_machine_tokens"] and replay["raw_response_sha256_before"] == raw_hash == replay["raw_response_sha256_after"] and original == r21_arguments(), "R21 raw state tokens and evidence were not auto-repaired")
    add("SW-STATE-NEG-15", assess_scene_id_sequence(scene_contracts[0]["ordered_scene_ids"], scene_contracts[1])["result"] != "PASS" and assess_scene_id_sequence(replay["scene_ids"], scene_contracts[1])["result"] == "PASS", "Repair16 current-run scene-ID contract remains intact")

    output = {
        "classification": "SCENE WRITER PER-RUN STATE-FIELD NEGATIVE TEST",
        "results": results,
        "passed": sum(item["result"] == "PASS" for item in results),
        "total": len(results),
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "live_e2e_runs": 0,
        "historical_replay": "READ_ONLY",
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] == output["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
