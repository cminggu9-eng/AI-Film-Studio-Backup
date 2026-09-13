"""Static TOKEN-01 through TOKEN-10; no Provider or Executor invocation."""

from __future__ import annotations

import copy
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Mapping


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in ROOT.parents if (parent / "studio.config.json").is_file())
REPAIR_03 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_03_Strict_Structured_Transport_V0.1"
REPAIR_02 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_02_Scene_Writer_Response_Budget_Serialization_V0.1"
REPAIR_01 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1"
HARNESS_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1"
for import_path in (str(REPAIR_03 / "implementation"), str(REPAIR_03 / "tests"), str(REPAIR_02 / "implementation"), str(REPAIR_01 / "implementation"), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

import run_minimal_e2e as e2e
from run_scene_writer_strict_transport_tests import (
    PARAMETERS_SCHEMA,
    SCENE_ID_CONTRACT,
    STATE_FIELD_CONTRACT,
    compact_payload,
)
from scene_writer_strict_transport import (
    CANONICAL_FLAGS_HANDOFFS,
    CANONICAL_PRIMARY_DECISION_STATES,
    FUNCTION_NAME,
    TRANSPORT_ABSENT,
    strict_function_schema,
    validate_required_tool_call_shape,
    validate_strict_scene_writer_arguments,
)


CANONICAL_SKILL = e2e.vault_root() / "01_SKILLS" / "02_Scene_Writer" / "scene-writer" / "SKILL.md"
PROBE_03_RAW = REPAIR_03 / "evidence" / "SW-CONTRACT-PROBE-03" / "artifacts" / "scene_writer_provider_response.json"
RECOVERY_ROOT = HARNESS_STAGE / "evidence" / "E2E-RUN-01-RECOVERY-01"


def canonical_contract_tokens() -> tuple[list[str], list[str], str]:
    text = CANONICAL_SKILL.read_text(encoding="utf-8")
    exact_output = text.split("## Exact Output Contract", 1)[1].split("## Handoff Packet", 1)[0]
    primary_part, flags_part = exact_output.split("Add zero or more **Orthogonal Flags / Handoffs** only when applicable:", 1)
    primary = re.findall(r"- `([A-Z_]+)`", primary_part)
    flags = re.findall(r"- `([A-Z_]+)`", flags_part)
    return primary, flags, exact_output


def recorded_probe03_arguments() -> Mapping[str, Any]:
    raw = json.loads(PROBE_03_RAW.read_text(encoding="utf-8"))
    wire = json.loads(raw["raw_provider_response"])
    message = wire["choices"][0]["message"]
    function = validate_required_tool_call_shape(
        assistant_content=message.get("content") or "",
        tool_calls=message.get("tool_calls"),
        function_name=FUNCTION_NAME,
    )
    return json.loads(function["arguments"])


def e2e_int_12_recorded_transport() -> bool:
    role_results = {
        "showrunner": json.loads((RECOVERY_ROOT / "artifacts" / "showrunner_output.json").read_text(encoding="utf-8")),
        "scene_writer": json.loads((RECOVERY_ROOT / "artifacts" / "scene_writer_output.json").read_text(encoding="utf-8")),
    }
    envelopes = {
        "showrunner": json.loads((RECOVERY_ROOT / "envelopes" / "01_showrunner_to_scene_writer.json").read_text(encoding="utf-8")),
        "scene_writer": json.loads((RECOVERY_ROOT / "envelopes" / "02_scene_writer_to_director.json").read_text(encoding="utf-8")),
    }
    return e2e.e2e_int_12_tokens_preserved(role_results=role_results, envelopes=envelopes)


def rejected_unknown_flag() -> bool:
    payload = compact_payload()
    payload["control"]["flags"] = ["UNKNOWN_FLAG"]
    try:
        validate_strict_scene_writer_arguments(payload, parameters_schema=PARAMETERS_SCHEMA, scene_id_contract=SCENE_ID_CONTRACT, state_field_contract=STATE_FIELD_CONTRACT)
    except Exception:
        return True
    return False


def run() -> int:
    canonical_primary, canonical_flags, exact_output = canonical_contract_tokens()
    schema = strict_function_schema(SCENE_ID_CONTRACT, STATE_FIELD_CONTRACT)
    control = schema["properties"]["control"]
    outcome_enum = control["properties"]["outcome"]["enum"]
    flags_array_enum = control["properties"]["flags"]["anyOf"][1]["items"]["enum"]
    handoffs_array_enum = control["properties"]["handoffs"]["anyOf"][1]["items"]["enum"]
    recorded = recorded_probe03_arguments()
    current_hash = hashlib.sha256(CANONICAL_SKILL.read_bytes()).hexdigest().upper()
    results = [
        {"id": "TOKEN-01", "result": "PASS" if canonical_primary == list(CANONICAL_PRIMARY_DECISION_STATES) == outcome_enum and len(outcome_enum) == 6 else "FAIL", "detail": "six canonical Primary Decision States are fully accounted"},
        {"id": "TOKEN-02", "result": "PASS" if "NEEDS_DECISION" not in canonical_primary and "NEEDS_DECISION" not in outcome_enum else "FAIL", "detail": "NEEDS_DECISION is absent; no canonical alias remains"},
        {"id": "TOKEN-03", "result": "PASS" if "UPSTREAM_DECISION_REQUIRED" in canonical_primary and "UPSTREAM_DECISION_REQUIRED" in outcome_enum else "FAIL", "detail": "UPSTREAM_DECISION_REQUIRED is preserved exactly"},
        {"id": "TOKEN-04", "result": "PASS" if "REQUEST_OUT_OF_SCOPE" in canonical_primary and "REQUEST_OUT_OF_SCOPE" in outcome_enum else "FAIL", "detail": "REQUEST_OUT_OF_SCOPE is preserved exactly"},
        {"id": "TOKEN-05", "result": "PASS" if canonical_flags == list(CANONICAL_FLAGS_HANDOFFS) == flags_array_enum == handoffs_array_enum else "FAIL", "detail": "all canonical flags and handoffs are accounted exactly"},
        {"id": "TOKEN-06", "result": "PASS" if rejected_unknown_flag() else "FAIL", "detail": "unknown flag is rejected by strict schema"},
        {"id": "TOKEN-07", "result": "PASS" if TRANSPORT_ABSENT not in exact_output and control["properties"]["flags"]["anyOf"][0]["enum"] == [TRANSPORT_ABSENT] else "FAIL", "detail": "ABSENT is transport-only and is not added to canonical output semantics"},
        {"id": "TOKEN-08", "result": "PASS" if recorded["control"]["outcome"] == "SCENE_CREATED" else "FAIL", "detail": "recorded CREATE / SCENE_CREATED Probe03 canonical outcome remains preserved; its superseded transport shape is assessed separately"},
        {"id": "TOKEN-09", "result": "PASS" if e2e_int_12_recorded_transport() else "FAIL", "detail": "E2E-INT-12 preserves source mode, primary state, flags, and handoffs exactly"},
        {"id": "TOKEN-10", "result": "PASS" if current_hash == e2e.EXPECTED_HASHES["scene_writer"] else "FAIL", "detail": "canonical Scene Writer Skill hash is unchanged"},
    ]
    output = {
        "classification": "STATIC CANONICAL TOKEN ALIGNMENT TEST",
        "results": results,
        "passed": sum(item["result"] == "PASS" for item in results),
        "total": len(results),
        "provider_calls": 0,
        "executor_calls": 0,
        "canonical_skill_sha256": current_hash,
        "semantic_mutation": 0,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] == output["total"] else 1


if __name__ == "__main__":
    raise SystemExit(run())
