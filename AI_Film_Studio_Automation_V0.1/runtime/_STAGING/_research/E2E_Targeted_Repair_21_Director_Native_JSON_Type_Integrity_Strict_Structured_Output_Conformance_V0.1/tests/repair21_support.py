"""Read-only provenance and test support for Director native JSON integrity."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, Mapping


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
REPAIR_07 = RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1"
REPAIR_05 = RESEARCH / "E2E_Targeted_Repair_05_Director_Output_Contract_Transport_Alignment_V0.1"
REPAIR_09B = RESEARCH / "E2E_Targeted_Repair_09B_Director_Full_Structured_Submission_Payload_V0.1"
REPAIR_09C = RESEARCH / "E2E_Targeted_Repair_09C_Director_Strict_Provider_Compatibility_V0.1"
REPAIR_09K = RESEARCH / "E2E_Targeted_Repair_09K_Director_State_Object_Contract_Implementation_V0.1"
REPAIR_15 = RESEARCH / "E2E_Targeted_Repair_15_Mandatory_Preflight_Environment_Isolation_V0.1"
REPAIR_20 = RESEARCH / "E2E_Targeted_Repair_20_Scene_Writer_Strict_Structured_Output_Completeness_Wire_Contract_Conformance_V0.1"
PHASE2 = RESEARCH / "Systemic_Hardening_Phase_2_Runtime_Reliability_Regression_Enforcement_V0.1"
F3_BINDING = REPAIR_07 / "fixtures" / "E2E_FIX_03_Runtime_Binding_V0.1.json"
R26 = HARNESS / "evidence" / "E2E-RUN-26"
R26_ARTIFACTS = R26 / "artifacts"

os.environ["AFS_E2E_FIXTURE_BINDING"] = str(F3_BINDING)
for directory in (REPAIR_15 / "implementation", REPAIR_09C / "implementation", REPAIR_09B / "implementation", REPAIR_07 / "implementation", REPAIR_05 / "implementation", HARNESS, AUTOMATION_ROOT):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

from fixture_contract_compiler import compile_path
from director_provider_compatibility import deepseek_compatible_schema, equivalence_report
from director_state_object_contract import compile_director_state_object_contract, stable_hash
from director_structured_submission import (
    build_director_native_json_type_instruction,
    build_director_structured_output_contract,
    director_native_json_type_manifest,
    director_submission_schema,
    make_director_payload_validator,
)
import run_minimal_e2e as e2e


R26_HASHED_ARTIFACTS = {
    "raw": R26_ARTIFACTS / "director_provider_response.json",
    "wire": R26_ARTIFACTS / "director_final_wire_payload.json",
    "invocation": R26_ARTIFACTS / "director_invocation.json",
    "persistence": R26_ARTIFACTS / "director_persistence_verification.json",
    "truncation": R26_ARTIFACTS / "director_truncation_detection.json",
    "validation": R26_ARTIFACTS / "director_validation_error.json",
}


def read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def r26_hashes() -> Dict[str, str]:
    return {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in R26_HASHED_ARTIFACTS.items()}


def r26_wire_payload() -> Dict[str, Any]:
    return read_json(R26_HASHED_ARTIFACTS["wire"])["payload"]


def r26_arguments() -> Dict[str, Any]:
    """Parse only the outer tool-arguments transport; never normalize a field."""
    persisted = read_json(R26_HASHED_ARTIFACTS["raw"])
    response = json.loads(persisted["raw_provider_response"])
    arguments = response["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"]
    return json.loads(arguments)


def r26_diagnostic_inner_array() -> Any:
    """Diagnostic-only inspection of the stringified R26 field, never a repair input."""
    value = r26_arguments()["unresolved_decisions"]
    if not isinstance(value, str):
        return None
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return None


def f3_state_contract() -> tuple[Dict[str, Any], Dict[str, Any]]:
    compiled = compile_path(F3_BINDING)
    records = e2e._capture_state_source_records(compiled)
    state_contract = compile_director_state_object_contract(
        compiled_run_contract=compiled,
        validated_upstream_state_records=(),
        run_local_state_ledger_records=records,
        required_locks=compiled["fixture"]["decision_locks"],
        transition_authority_records=compiled["fixture"]["authorized_transitions"],
    )
    return compiled, state_contract


def current_wire_audit() -> Dict[str, Any]:
    compiled, state_contract = f3_state_contract()
    neutral = director_submission_schema(state_contract)
    strict = build_director_structured_output_contract(state_contract)
    projected = deepseek_compatible_schema(state_contract)
    capture = e2e.director_request_capture()
    wire = capture["final_wire_payload"]
    function = wire["tools"][0]["function"]
    return {
        "compiled": compiled,
        "state_contract": state_contract,
        "neutral": neutral,
        "strict": strict,
        "projected": projected,
        "projection_equivalence": equivalence_report(state_contract),
        "capture": capture,
        "wire": wire,
        "function": function,
        "type_manifest": director_native_json_type_manifest(function["parameters"]),
        "type_instruction": build_director_native_json_type_instruction(function["parameters"]),
    }


def validator_for(state_contract: Mapping[str, Any]):
    return make_director_payload_validator(
        selected_mode="PLAN",
        required_locks=["view_memory_card_decision"],
        prohibited_changes=["resume_partnership", "permanent_break"],
        state_contract=state_contract,
    )


def rejects(payload: Mapping[str, Any], state_contract: Mapping[str, Any]) -> bool:
    try:
        validator_for(state_contract)(payload)
    except Exception:
        return True
    return False


def native_array_payload() -> Dict[str, Any]:
    payload = copy.deepcopy(r26_arguments())
    payload["unresolved_decisions"] = ["unresolved-decision"]
    return payload


def absent_payload() -> Dict[str, Any]:
    payload = copy.deepcopy(r26_arguments())
    payload["unresolved_decisions"] = "ABSENT"
    return payload


def production_source_guards() -> Dict[str, Any]:
    structured_source = (REPAIR_09B / "implementation" / "director_structured_submission.py").read_text(encoding="utf-8")
    adapter_source = (AUTOMATION_ROOT / "runtime" / "shared_qa" / "deepseek_provider_adapter.py").read_text(encoding="utf-8")
    return {
        "field_level_json_loads_absent": "json.loads(" not in structured_source,
        "legacy_alias_has_no_live_reference": structured_source.count("JSON_OBJECT_STRING_STATE_FIELDS") == 1,
        "adapter_has_no_director_field_normalizer": "unresolved_decisions" not in adapter_source,
        "no_automatic_retry_policy": "NO_AUTOMATIC_RETRY" in adapter_source,
    }


def current_integrity() -> Dict[str, Any]:
    manifest = read_json(R26 / "execution_manifest.json")
    return {
        "canonical_hashes_match_r26": e2e.canonical_skill_hashes() == manifest["final_canonical_skill_hashes"],
        "production_lock_hashes_match_r26": e2e.production_lock_hashes() == manifest["production_lock_hashes_after"],
        "canonical_count": len(e2e.canonical_skill_hashes()),
        "production_lock_count": len(e2e.production_lock_hashes()),
        "r26_status": manifest["status"],
    }


def stable(value: Any) -> str:
    return stable_hash(value)
