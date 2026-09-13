"""Provider-free regression for Probe 02's literal newline failure pattern."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in ROOT.parents if (parent / "studio.config.json").is_file())
HARNESS_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1"
REPAIR_01 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1"
REPAIR_02 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_02_Scene_Writer_Response_Budget_Serialization_V0.1"
for import_path in (str(ROOT / "tests"), str(ROOT / "implementation"), str(REPAIR_02 / "implementation"), str(REPAIR_01 / "implementation"), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

from runtime.shared_qa.model_executor import ModelExecutor, ModelRequest
from run_scene_writer_strict_transport_tests import SyntheticStrictProvider, compact_payload, function_response
from scene_writer_strict_transport import FUNCTION_NAME, build_structured_output_contract, validate_strict_scene_writer_arguments


def run() -> int:
    payload = compact_payload()
    literal_pattern = "许宁换完衣服进入客厅，\n        坐定"
    payload["scenes"][1]["structural"]["入场"] = literal_pattern
    arguments = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    provider = SyntheticStrictProvider(function_response(payload))
    request = ModelRequest(
        system_prompt="synthetic strict transport regression",
        user_prompt="synthetic strict transport regression",
        model="deepseek-v4-pro",
        thinking_mode="disabled",
        max_tokens=1,
        response_format=None,
        structured_output=build_structured_output_contract(),
    )
    executor = ModelExecutor(provider)
    receipt = executor.execute_with_receipt(request, invocation_id="PROBE-02-REGRESSION-01")
    parsed = executor.extract_required_tool_arguments(receipt, function_name=FUNCTION_NAME)
    validated = validate_strict_scene_writer_arguments(parsed)
    results = [
        {"id": "PROBE-02-REG-01", "result": "PASS" if "\\n" in arguments else "FAIL", "detail": "function argument JSON serializes the literal newline as a legal escape"},
        {"id": "PROBE-02-REG-02", "result": "PASS" if parsed["scenes"][1]["structural"]["入场"] == literal_pattern else "FAIL", "detail": "strict argument parsing round-trips the original Chinese multiline value"},
        {"id": "PROBE-02-REG-03", "result": "PASS" if validated == parsed and receipt.raw_provider_response and json.loads(receipt.raw_provider_response)["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"] == arguments else "FAIL", "detail": "raw provider wire response remains parseable and unchanged before validation"},
    ]
    output = {"classification": "PROBE-02 LITERAL-NEWLINE STRICT TRANSPORT REGRESSION", "results": results, "passed": sum(item["result"] == "PASS" for item in results), "total": len(results), "provider_calls": 0, "json_auto_repairs": 0}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] == output["total"] else 1


if __name__ == "__main__":
    raise SystemExit(run())
