"""Provider-free SW-COMP-01 through SW-COMP-20 for Repair20."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys

from repair20_support import (
    AUTOMATION_ROOT,
    PHASE2,
    R25,
    R25_TRUNCATION,
    R25_VALIDATION,
    REPAIR_07,
    complete_f3_arguments,
    current_wire_audit,
    local_errors,
    r25_arguments,
    r25_hashes,
    r25_wire_payload,
    rejects,
)

import run_minimal_e2e as e2e
from scene_writer_strict_transport import validate_strict_scene_writer_arguments


def run_json(script):
    completed = subprocess.run(
        [sys.executable, "-X", "utf8", "-B", str(script)],
        cwd=str(AUTOMATION_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        payload = {}
    return completed.returncode, payload


def main() -> int:
    audit = current_wire_audit()
    schema, scene_ids, state = audit["schema"], audit["scene_ids"], audit["state"]
    manifest = audit["manifest"]
    complete = complete_f3_arguments()
    before = r25_hashes()
    raw = r25_arguments()
    r25_errors = local_errors(raw, schema)
    r25_wire = r25_wire_payload()
    r25_function = r25_wire["tools"][0]["function"]
    truncation = json.loads(R25_TRUNCATION.read_text(encoding="utf-8"))
    validation = json.loads(R25_VALIDATION.read_text(encoding="utf-8"))
    generic_code, generic = run_json(REPAIR_07 / "tests" / "run_fixture_generality_tests.py")
    gate_path = R25.parents[2] / "E2E_Targeted_Repair_20_Scene_Writer_Strict_Structured_Output_Completeness_Wire_Contract_Conformance_V0.1" / "reports" / "Repair20_Offline_Gates.json"
    gates = json.loads(gate_path.read_text(encoding="utf-8")) if gate_path.is_file() else {}
    after = r25_hashes()

    results = []
    def add(case_id, passed, detail):
        results.append({"id": case_id, "result": "PASS" if passed else "FAIL", "detail": detail})

    required = ["id", "content", "structural", "state"]
    required_sets = manifest["required_field_sets"]["compiled_schema"]
    add("SW-COMP-01", audit["compiled"]["fixture"]["fixture_id"] == "E2E-FIX-03" and audit["schema"]["properties"]["scenes"]["items"]["properties"]["id"]["enum"] == scene_ids["ordered_scene_ids"], "compiled F03 provenance reaches the strict scene schema")
    add("SW-COMP-02", manifest["schema_byte_equivalence"]["wire_equals_local_validator"] and manifest["schema_sha256"]["local_validator_schema"] == manifest["schema_sha256"]["compiled_schema"], "local validator schema is byte-identical to compiled schema")
    add("SW-COMP-03", manifest["schema_byte_equivalence"]["final_strict_equals_adapter_projected"], "adapter projection preserves final strict schema")
    add("SW-COMP-04", r25_function["parameters"] == schema and r25_function["strict"] is True, "R25 actual persisted wire schema retained the complete strict schema")
    add("SW-COMP-05", required_sets["$.scenes[*]"] == required and manifest["schema_semantic_equivalence"]["required_sets_equal"], "all compiled/final/adapter/wire/local nested required sets are identical")
    add("SW-COMP-06", manifest["wire_strict_mechanics"]["strict_true"] and manifest["wire_strict_mechanics"]["function_name_exact"], "strict function mechanics are explicit")
    add("SW-COMP-07", manifest["wire_strict_mechanics"]["tool_choice_exact"], "exact required tool choice is forced")
    add("SW-COMP-08", validate_strict_scene_writer_arguments(complete, parameters_schema=schema, scene_id_contract=scene_ids, state_field_contract=state)["scenes"][0]["id"] == scene_ids["ordered_scene_ids"][0], "complete Scene 1 passes local strict validation")
    add("SW-COMP-09", "structural" in complete["scenes"][1] and "state" in complete["scenes"][1] and not rejects(complete, schema, scene_ids, state), "complete Scene 2 passes independently")
    add("SW-COMP-10", "structural" in complete["scenes"][2] and "state" in complete["scenes"][2] and not rejects(complete, schema, scene_ids, state), "complete Scene 3 passes independently")
    add("SW-COMP-11", rejects(raw, schema, scene_ids, state) and r25_errors[0]["path"] == "scenes/1" and "'structural' is a required property" in r25_errors[0]["message"], "R25 immutable replay fails closed first at S02 structural")
    observed = {(item["path"], item["message"]) for item in r25_errors}
    add("SW-COMP-12", len(r25_errors) == 4 and all((path, message) in observed for path, message in {("scenes/1", "'structural' is a required property"), ("scenes/1", "'state' is a required property"), ("scenes/2", "'structural' is a required property"), ("scenes/2", "'state' is a required property")}), "diagnostic mode enumerates all four R25 missing fields without repair")
    completeness = e2e.scene_writer_completeness_instruction(schema)
    add("SW-COMP-13", all(name in completeness for name in required) and "independently" in completeness and "same-as-above" in completeness and "E2E-FIX-03" not in e2e.scene_writer_completeness_instruction.__code__.co_consts, "provider instruction is generated from final schema and forbids implicit inheritance")
    foreign_ids = complete_f3_arguments()
    foreign_ids["scenes"][0]["id"] = "E2E-FIX-02-S01"
    wrong_state_field = complete_f3_arguments()
    current_state_field = state["transport_field_name"]
    wrong_state_field["scenes"][0]["state"]["foreign_state_field"] = wrong_state_field["scenes"][0]["state"].pop(current_state_field)
    add("SW-COMP-14", rejects(foreign_ids, schema, scene_ids, state) and rejects(wrong_state_field, schema, scene_ids, state), "Repair16 scene-ID and Repair17 state-field paths remain fail-closed")
    add("SW-COMP-15", gates.get("mandatory_preflight", {}).get("passed") is True and gates.get("mandatory_preflight", {}).get("suite_count") == 15, "Mandatory Preflight passes 15/15")
    add("SW-COMP-16", generic_code == 0 and generic.get("passed") == 18 and generic.get("total") == 18, "GEN fixture generality passes 18/18")
    add("SW-COMP-17", gates.get("unified_phase2", {}).get("returncode") == 0 and gates.get("unified_phase2", {}).get("overall") == "PASS" and gates.get("unified_phase2", {}).get("record_count") == 25, "Unified Phase2 passes 25/25")
    add("SW-COMP-18", before == after and (R25 / "artifacts").is_dir(), "R25 evidence was replayed read-only and remains immutable")
    add("SW-COMP-19", truncation["classification"] == "NOT_TRUNCATED" and truncation["finish_reason"] == "tool_calls" and truncation["requested_max_tokens"] == 5000 and validation["category"] == "SCHEMA VALIDATION FAILURE", "R25 is a completeness failure, not a budget, phase, or safeguard failure")
    add("SW-COMP-20", manifest["schema_byte_equivalence"]["all_five_equal"] and audit["endpoint"].endswith("/beta") and audit["payload"]["max_tokens"] == 5000, "strict compiled-to-wire audit completes provider-free with no role call")

    output = {
        "classification": "SCENE WRITER STRICT COMPLETENESS POSITIVE TEST",
        "results": results,
        "passed": sum(item["result"] == "PASS" for item in results),
        "total": len(results),
        "schema_identity_manifest": manifest,
        "r25_replay_errors": r25_errors,
        "mandatory_preflight": gates.get("mandatory_preflight", {}),
        "genericity": {"returncode": generic_code, "passed": generic.get("passed"), "total": generic.get("total")},
        "unified_phase2": gates.get("unified_phase2", {}),
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "live_e2e_runs": 0,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] == output["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
