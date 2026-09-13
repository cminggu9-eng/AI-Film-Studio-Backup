"""Provider-free strict transport preflight using a synthetic function call."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in ROOT.parents if (parent / "studio.config.json").is_file())
HARNESS_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1"
REPAIR_01 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1"
REPAIR_02 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_02_Scene_Writer_Response_Budget_Serialization_V0.1"
for import_path in (str(ROOT / "tests"), str(ROOT / "implementation"), str(REPAIR_02 / "implementation"), str(REPAIR_01 / "implementation"), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

import run_minimal_e2e as e2e
from run_scene_writer_strict_transport_tests import SyntheticStrictProvider, compact_payload, frozen_locks, function_response
from scene_writer_integration_contract import assess_scene_writer_integration_contract
from scene_writer_strict_transport import FUNCTION_NAME, build_structured_output_contract, validate_provider_strict_schema, validate_strict_scene_writer_arguments


def run() -> int:
    provider = SyntheticStrictProvider(function_response(compact_payload()))
    locks, prohibitions = frozen_locks()
    contract = build_structured_output_contract()
    with tempfile.TemporaryDirectory() as directory:
        evidence = Path(directory)
        executor = e2e.CanonicalRoleExecutor(evidence_dir=evidence, provider_adapter=provider, run_id="SW-CONTRACT-PROBE-03-PREFLIGHT")
        result, _, output_path = executor.invoke(
            spec=e2e.role_spec("scene_writer"),
            input_payload={"frozen_showrunner_recovery_artifact": True, "preflight": "synthetic_tool_call_only"},
            required_locks=locks,
            prohibited_changes=prohibitions,
            completion_budget=5000,
            structured_output=contract,
            structured_arguments_validator=validate_strict_scene_writer_arguments,
        )
        raw_path = evidence / "artifacts" / "scene_writer_provider_response.json"
        raw = json.loads(raw_path.read_text(encoding="utf-8")) if raw_path.is_file() else {}
        record = executor.call_records[0] if executor.call_records else {}
        gates = assess_scene_writer_integration_contract(result, run_id="SW-CONTRACT-PROBE-03-PREFLIGHT")
        structured_evidence = raw.get("structured_output") if isinstance(raw.get("structured_output"), dict) else {}
        results = [
            {"id": "PREFLIGHT-01", "result": "PASS" if validate_provider_strict_schema()["passed"] else "FAIL", "detail": "request schema is valid and uses the strict supported subset"},
            {"id": "PREFLIGHT-02", "result": "PASS" if provider.request is not None and provider.request.response_format is None and provider.request.structured_output is not None and provider.request.structured_output.function_name == FUNCTION_NAME else "FAIL", "detail": "forced function contract uses no parallel json_object route"},
            {"id": "PREFLIGHT-03", "result": "PASS" if len(result["scene_packages"]) == 3 and output_path.is_file() else "FAIL", "detail": "function arguments hydrate into the existing integration shape"},
            {"id": "PREFLIGHT-04", "result": "PASS" if gates["passed"] else "FAIL", "detail": "existing structural and state gates are wired after hydration"},
            {"id": "PREFLIGHT-05", "result": "PASS" if raw.get("lifecycle_stage") == "RAW_RESPONSE_PERSISTED" and structured_evidence.get("function_name") == FUNCTION_NAME and record.get("persistence_verified") is True else "FAIL", "detail": "raw response and usage persistence precede transport validation"},
        ]
    output = {"classification": "PROVIDER-FREE STRICT TRANSPORT PREFLIGHT", "results": results, "passed": sum(item["result"] == "PASS" for item in results), "total": len(results), "provider_calls": 0, "synthetic_function_calls": provider.request_count, "showrunner_calls": 0, "downstream_calls": 0, "retries": 0, "fallbacks": 0, "json_auto_repairs": 0, "beta_provider_feature_used": "YES (synthetic adapter path only)"}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] == output["total"] else 1


if __name__ == "__main__":
    raise SystemExit(run())
