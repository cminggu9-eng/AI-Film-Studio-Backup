"""Read-only Repair22 support: canonical Director values and provider wire values stay distinct."""
from __future__ import annotations
import copy, hashlib, json, os, sys
from pathlib import Path
from typing import Any, Dict, Mapping

STAGE = Path(__file__).resolve().parents[1]
ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
RESEARCH = ROOT / "runtime" / "_STAGING" / "_research"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
R07 = RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1"
R05 = RESEARCH / "E2E_Targeted_Repair_05_Director_Output_Contract_Transport_Alignment_V0.1"
R09B = RESEARCH / "E2E_Targeted_Repair_09B_Director_Full_Structured_Submission_Payload_V0.1"
R09C = RESEARCH / "E2E_Targeted_Repair_09C_Director_Strict_Provider_Compatibility_V0.1"
R15 = RESEARCH / "E2E_Targeted_Repair_15_Mandatory_Preflight_Environment_Isolation_V0.1"
R26 = HARNESS / "evidence" / "E2E-RUN-26"
R26_ARTIFACTS = R26 / "artifacts"
PROBE21 = RESEARCH / "E2E_Targeted_Repair_21_Director_Native_JSON_Type_Integrity_Strict_Structured_Output_Conformance_V0.1" / "reports" / "DIRECTOR-NATIVE-TYPE-PROBE-21-F03" / "artifacts" / "director_provider_response.json"
F3 = R07 / "fixtures" / "E2E_FIX_03_Runtime_Binding_V0.1.json"
os.environ["AFS_E2E_FIXTURE_BINDING"] = str(F3)
for p in (R15 / "implementation", R09C / "implementation", R09B / "implementation", R07 / "implementation", R05 / "implementation", HARNESS, ROOT):
    if str(p) not in sys.path: sys.path.insert(0, str(p))
from fixture_contract_compiler import compile_path
from director_state_object_contract import compile_director_state_object_contract
from director_structured_submission import director_submission_schema, make_director_payload_validator
from director_provider_compatibility import (deepseek_compatible_schema, provider_wire_manifest, validate_director_provider_wire_arguments, decode_director_provider_wire_arguments)
import run_minimal_e2e as e2e

def read(path: Path) -> Dict[str, Any]: return json.loads(path.read_text(encoding="utf-8"))
def sha(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()
def outer_arguments(path: Path) -> Dict[str, Any]:
    raw = read(path)["raw_provider_response"]
    return json.loads(json.loads(raw)["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"])
def state_contract() -> tuple[Dict[str, Any], Dict[str, Any]]:
    compiled = compile_path(F3); records = e2e._capture_state_source_records(compiled)
    return compiled, compile_director_state_object_contract(compiled_run_contract=compiled, validated_upstream_state_records=(), run_local_state_ledger_records=records, required_locks=compiled["fixture"]["decision_locks"], transition_authority_records=compiled["fixture"]["authorized_transitions"])
def canonical_validator(contract: Mapping[str, Any]):
    return make_director_payload_validator(selected_mode="PLAN", required_locks=["view_memory_card_decision"], prohibited_changes=["resume_partnership", "permanent_break"], state_contract=contract)
def canonical_fixture() -> Dict[str, Any]:
    p = copy.deepcopy(outer_arguments(R26_ARTIFACTS / "director_provider_response.json")); p["unresolved_decisions"] = ["unresolved-decision"]; return p
def wire_fixture(contract: Mapping[str, Any], status: str = "PRESENT", items: Any = None) -> Dict[str, Any]:
    p = canonical_fixture(); p["unresolved_decisions"] = {"status": status, "items": ["unresolved-decision"] if items is None else items}; return p
def projection_audit(contract: Mapping[str, Any]) -> Dict[str, Any]:
    return {"canonical": director_submission_schema(contract), "wire": deepseek_compatible_schema(contract), "manifest": provider_wire_manifest(contract)}
def production_guards() -> Dict[str, bool]:
    source=(R09C/"implementation"/"director_provider_compatibility.py").read_text(encoding="utf-8")
    adapter=(ROOT/"runtime"/"shared_qa"/"deepseek_provider_adapter.py").read_text(encoding="utf-8")
    return {"no_field_json_loads": "json.loads(" not in source, "adapter_has_no_field_normalizer": "unresolved_decisions" not in adapter, "no_automatic_retry": "NO_AUTOMATIC_RETRY" in adapter}
