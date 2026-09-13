"""Provider-free SW-COMP-NEG-01 through SW-COMP-NEG-15 for Repair20."""

from __future__ import annotations

import copy
import json

from repair20_support import (
    R25_RAW,
    R25_VALIDATION,
    complete_f3_arguments,
    current_wire_audit,
    r25_arguments,
    r25_hashes,
    rejects,
)

import run_minimal_e2e as e2e


def main() -> int:
    audit = current_wire_audit()
    schema, scene_ids, state = audit["schema"], audit["scene_ids"], audit["state"]
    raw = r25_arguments()
    before = r25_hashes()
    missing_s02_structural = copy.deepcopy(complete_f3_arguments()); missing_s02_structural["scenes"][1].pop("structural")
    missing_s02_state = copy.deepcopy(complete_f3_arguments()); missing_s02_state["scenes"][1].pop("state")
    missing_s03_structural = copy.deepcopy(complete_f3_arguments()); missing_s03_structural["scenes"][2].pop("structural")
    missing_s03_state = copy.deepcopy(complete_f3_arguments()); missing_s03_state["scenes"][2].pop("state")
    wire = copy.deepcopy(audit["payload"])
    wire["tools"][0]["function"]["parameters"]["properties"]["scenes"]["items"]["required"].remove("structural")
    lost_required_manifest = e2e.scene_writer_schema_identity_manifest(
        compiled_schema=schema,
        final_strict_schema=schema,
        adapter_projected_schema=wire["tools"][0]["function"]["parameters"],
        wire_schema=wire["tools"][0]["function"]["parameters"],
        local_validator_schema=schema,
        function_name=audit["strict"].function_name,
        wire_function_name=wire["tools"][0]["function"]["name"],
        wire_strict=wire["tools"][0]["function"]["strict"],
        wire_tool_choice=wire["tool_choice"],
    )
    strict_lost = copy.deepcopy(audit["payload"]); strict_lost["tools"][0]["function"]["strict"] = False
    strict_lost_manifest = e2e.scene_writer_schema_identity_manifest(
        compiled_schema=schema,
        final_strict_schema=schema,
        adapter_projected_schema=strict_lost["tools"][0]["function"]["parameters"],
        wire_schema=strict_lost["tools"][0]["function"]["parameters"],
        local_validator_schema=schema,
        function_name=audit["strict"].function_name,
        wire_function_name=strict_lost["tools"][0]["function"]["name"],
        wire_strict=strict_lost["tools"][0]["function"]["strict"],
        wire_tool_choice=strict_lost["tool_choice"],
    )
    unforced = copy.deepcopy(audit["payload"]); unforced["tool_choice"] = "auto"
    unforced_manifest = e2e.scene_writer_schema_identity_manifest(
        compiled_schema=schema,
        final_strict_schema=schema,
        adapter_projected_schema=unforced["tools"][0]["function"]["parameters"],
        wire_schema=unforced["tools"][0]["function"]["parameters"],
        local_validator_schema=schema,
        function_name=audit["strict"].function_name,
        wire_function_name=unforced["tools"][0]["function"]["name"],
        wire_strict=unforced["tools"][0]["function"]["strict"],
        wire_tool_choice=unforced["tool_choice"],
    )
    helper_source = e2e.scene_writer_completeness_instruction.__code__.co_consts
    validation = json.loads(R25_VALIDATION.read_text(encoding="utf-8"))
    after = r25_hashes()
    results = []
    def add(case_id, passed, detail):
        results.append({"id": case_id, "result": "PASS" if passed else "FAIL", "detail": detail})

    add("SW-COMP-NEG-01", rejects(missing_s02_structural, schema, scene_ids, state), "S02 without structural is rejected")
    add("SW-COMP-NEG-02", rejects(missing_s02_state, schema, scene_ids, state), "S02 without state is rejected")
    add("SW-COMP-NEG-03", rejects(missing_s03_structural, schema, scene_ids, state), "S03 without structural is rejected")
    add("SW-COMP-NEG-04", rejects(missing_s03_state, schema, scene_ids, state), "S03 without state is rejected")
    add("SW-COMP-NEG-05", "structural" not in raw["scenes"][1] and "state" not in raw["scenes"][1] and rejects(raw, schema, scene_ids, state), "later scenes are not copied from the first scene by any validator path")
    add("SW-COMP-NEG-06", rejects(raw, schema, scene_ids, state) and "content" in raw["scenes"][1], "content cannot synthesize missing structural evidence")
    add("SW-COMP-NEG-07", rejects(raw, schema, scene_ids, state) and "content" in raw["scenes"][2], "content cannot synthesize missing state evidence")
    add("SW-COMP-NEG-08", schema["properties"]["scenes"]["items"]["required"] == ["id", "content", "structural", "state"], "required completeness fields cannot be made optional")
    add("SW-COMP-NEG-09", not lost_required_manifest["schema_byte_equivalence"]["all_five_equal"] and not lost_required_manifest["schema_semantic_equivalence"]["required_sets_equal"], "nested required-set loss is observable before send")
    add("SW-COMP-NEG-10", not strict_lost_manifest["wire_strict_mechanics"]["strict_true"], "adapter cannot silently drop strict:true")
    add("SW-COMP-NEG-11", not unforced_manifest["wire_strict_mechanics"]["tool_choice_exact"], "adapter cannot send unforced tool_choice")
    add("SW-COMP-NEG-12", before == after and "structural" not in r25_arguments()["scenes"][1], "R25 raw provider data was never auto-repaired")
    add("SW-COMP-NEG-13", not any(isinstance(value, str) and any(literal in value for literal in ("C09", "A17", "E2E-FIX-01", "E2E-FIX-02", "E2E-FIX-03", "battery")) for value in helper_source), "generic completeness instruction contains no fixture-specific reminder")
    add("SW-COMP-NEG-14", validation["category"] == "SCHEMA VALIDATION FAILURE" and "Semantic Safeguard" not in validation["validation_stage"], "missing strict fields are not misclassified as Repair19 phase/safeguard failures")
    add("SW-COMP-NEG-15", "NO_AUTOMATIC_RETRY" in (e2e.AUTOMATION_ROOT / "runtime" / "shared_qa" / "deepseek_provider_adapter.py").read_text(encoding="utf-8"), "provider adapter retains an explicit no-automatic-retry policy")

    output = {
        "classification": "SCENE WRITER STRICT COMPLETENESS NEGATIVE TEST",
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
