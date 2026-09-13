"""Provider-free negative tests for the compiled current-run Scene Writer ID contract."""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research"
REPAIR_01 = RESEARCH / "E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1"
REPAIR_02 = RESEARCH / "E2E_Targeted_Repair_02_Scene_Writer_Response_Budget_Serialization_V0.1"
REPAIR_03 = RESEARCH / "E2E_Targeted_Repair_03_Strict_Structured_Transport_V0.1"
REPAIR_07 = RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1"
REPAIR_08C = RESEARCH / "E2E_Targeted_Repair_08C_Scene_Writer_Strict_Schema_Composition_V0.1"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
for item in (REPAIR_03 / "implementation", REPAIR_02 / "implementation", REPAIR_01 / "implementation", REPAIR_07 / "implementation", REPAIR_08C / "implementation", HARNESS, AUTOMATION_ROOT):
    sys.path.insert(0, str(item))

from fixture_contract_compiler import compile_path
from scene_writer_scene_id_contract import assess_scene_id_sequence, build_scene_id_contract
from scene_writer_schema_composer import compose
from scene_writer_strict_transport import StrictTransportSchemaError, validate_strict_scene_writer_arguments


def binding(number: int) -> Path:
    return REPAIR_07 / "fixtures" / f"E2E_FIX_0{number}_Runtime_Binding_V0.1.json"


def sample(schema):
    if "enum" in schema:
        return copy.deepcopy(schema["enum"][0])
    kind = schema.get("type")
    if kind == "string":
        return "evidence"
    if kind == "array":
        return [sample(schema["items"])]
    if kind == "object":
        return {name: sample(value) for name, value in schema["properties"].items()}
    if "anyOf" in schema:
        return sample(schema["anyOf"][0])
    raise ValueError(schema)


def valid_payload(compiled, projection):
    schema = compose(compiled, scene_id_contract=projection)
    value = sample(schema)
    scene = schema["properties"]["scenes"]["items"]
    value["scenes"] = []
    for scene_id in projection["ordered_scene_ids"]:
        item = sample(scene)
        item["id"] = scene_id
        value["scenes"].append(item)
    return value, schema


def rejected(payload, schema, projection):
    try:
        validate_strict_scene_writer_arguments(payload, parameters_schema=schema, scene_id_contract=projection)
    except StrictTransportSchemaError:
        return True
    return False


def main() -> int:
    f1, f2, f3 = (compile_path(binding(number)) for number in (1, 2, 3))
    p1, p2, p3 = (build_scene_id_contract(item) for item in (f1, f2, f3))
    payload, schema = valid_payload(f2, p2)
    raw_path = HARNESS / "evidence" / "E2E-RUN-20" / "artifacts" / "scene_writer_provider_response.json"
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    recorded = json.loads(json.loads(raw["raw_provider_response"])["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"])
    recorded_ids = [item["id"] for item in recorded["scenes"]]
    sources = [
        REPAIR_01 / "implementation" / "scene_writer_integration_contract.py",
        REPAIR_01 / "implementation" / "scene_writer_scene_id_contract.py",
        RESEARCH / "E2E_Targeted_Repair_02_Scene_Writer_Response_Budget_Serialization_V0.1" / "implementation" / "scene_writer_compact_serialization.py",
        REPAIR_03 / "implementation" / "scene_writer_strict_transport.py",
        REPAIR_08C / "implementation" / "scene_writer_schema_composer.py",
        HARNESS / "run_minimal_e2e.py",
    ]
    source_text = "\n".join(path.read_text(encoding="utf-8") for path in sources)
    cases = []
    def add(case_id, value, detail): cases.append({"id": case_id, "result": "PASS" if value else "FAIL", "detail": detail})
    f1_id, f3_id = p1["ordered_scene_ids"][0], p3["ordered_scene_ids"][-1]
    wrong_order = copy.deepcopy(payload); wrong_order["scenes"][1]["id"], wrong_order["scenes"][2]["id"] = wrong_order["scenes"][2]["id"], wrong_order["scenes"][1]["id"]
    duplicate = copy.deepcopy(payload); duplicate["scenes"][2]["id"] = duplicate["scenes"][1]["id"]
    missing = copy.deepcopy(payload); missing["scenes"].pop()
    extra = copy.deepcopy(payload); extra["scenes"].append(copy.deepcopy(extra["scenes"][0]))
    fixture1 = copy.deepcopy(payload); fixture1["scenes"][0]["id"] = f1_id
    fixture3 = copy.deepcopy(payload); fixture3["scenes"][2]["id"] = f3_id
    suffix = copy.deepcopy(payload); suffix["scenes"][0]["id"] = "foreign-S01"
    add("SW-ID-NEG-01", rejected(fixture1, schema, p2), "Fixture01 ID is rejected in Fixture02")
    add("SW-ID-NEG-02", rejected(fixture3, schema, p2), "Fixture03 ID is rejected in Fixture02")
    add("SW-ID-NEG-03", rejected(wrong_order, schema, p2), "correct IDs in wrong order are rejected")
    add("SW-ID-NEG-04", rejected(duplicate, schema, p2), "duplicate scene ID is rejected")
    add("SW-ID-NEG-05", rejected(missing, schema, p2), "missing scene ID is rejected")
    add("SW-ID-NEG-06", rejected(extra, schema, p2), "extra scene ID is rejected")
    add("SW-ID-NEG-07", rejected(suffix, schema, p2), "suffix-only identity is rejected")
    add("SW-ID-NEG-08", assess_scene_id_sequence(p1["ordered_scene_ids"], p2)["result"] == "FAIL", "previous-run IDs are not accepted")
    add("SW-ID-NEG-09", p1["ordered_scene_ids"][0] not in json.dumps(p2, ensure_ascii=False), "Fixture02 projection contains no stale Fixture01 ID")
    add("SW-ID-NEG-10", f1_id not in schema["properties"]["scenes"]["items"]["properties"]["id"]["enum"], "provider schema contains no stale Fixture01 enum")
    add("SW-ID-NEG-11", rejected(fixture1, schema, p2), "local validator contains no stale Fixture01 acceptance")
    add("SW-ID-NEG-12", p3["ordered_scene_ids"][-1] in recorded_ids and rejected(recorded, schema, p2), "recorded foreign Fixture03 ID remains fail-closed")
    add("SW-ID-NEG-13", not (HARNESS / "evidence" / "E2E-RUN-20" / "artifacts" / "scene_writer_final_wire_payload.json").exists(), "no historical provider violation is claimed without retained wire schema")
    add("SW-ID-NEG-14", recorded_ids[-1] == p3["ordered_scene_ids"][-1], "recorded response remains unmodified")
    add("SW-ID-NEG-15", "E2E-FIX-01-S01" not in source_text and "E2E-FIX-02-S01" not in source_text and "E2E-FIX-03-S03" not in source_text, "generic runtime, schema compiler, and validator sources contain no fixture scene-id literal")
    output = {"classification": "SCENE WRITER PER-RUN SCENE-ID NEGATIVE TEST", "results": cases, "passed": sum(item["result"] == "PASS" for item in cases), "total": len(cases), "provider_calls": 0, "executor_calls": 0, "role_calls": 0, "replay_only": True}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] == output["total"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
