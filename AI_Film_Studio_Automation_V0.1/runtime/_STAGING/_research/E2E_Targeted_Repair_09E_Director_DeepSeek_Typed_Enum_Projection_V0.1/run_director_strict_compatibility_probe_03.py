"""One authorized post-09E Director-only live strict compatibility probe."""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Mapping


ROOT = Path(__file__).resolve().parent
AUTOMATION = next(parent for parent in ROOT.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION / "runtime" / "_STAGING" / "_research"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
for directory in (
    HARNESS,
    RESEARCH / "E2E_Targeted_Repair_09D_Director_Strict_Provider_Observability_Conformance_V0.1" / "implementation",
):
    sys.path.insert(0, str(directory))
os.environ["AFS_E2E_FIXTURE_BINDING"] = str(RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1" / "fixtures" / "E2E_FIX_01_Runtime_Binding_V0.1.json")

import run_minimal_e2e as e2e
from deepseek_strict_linter import lint
from director_provider_compatibility import PROJECTION_ID, build_deepseek_compatible_director_contract, deepseek_compatible_schema, equivalence_report
from director_structured_submission import FUNCTION_NAME, director_submission_schema


SOURCE = HARNESS / "evidence" / "E2E-RUN-12"
EVIDENCE = ROOT / "evidence" / "DIRECTOR-STRICT-COMPATIBILITY-PROBE-03"
RUN_ID = "DIRECTOR-STRICT-COMPATIBILITY-PROBE-03"
EXPECTED_POINTERS = (
    "/properties/flags", "/properties/handoffs", "/properties/unresolved_decisions/anyOf/0",
    "/properties/state_evidence/properties/relevant_prior_state/anyOf/0",
    "/properties/state_evidence/properties/current_state/anyOf/0",
    "/properties/state_evidence/properties/proposed_state/anyOf/0",
    "/properties/state_evidence/properties/knowledge_timing/anyOf/0",
    "/properties/state_evidence/properties/relationship_state/anyOf/0",
    "/properties/state_evidence/properties/visual_state/anyOf/0",
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def node_at(schema: Mapping[str, Any], pointer: str) -> Any:
    value: Any = schema
    for part in pointer.strip("/").split("/"):
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def preflight() -> dict[str, Any]:
    schema = deepseek_compatible_schema()
    typed_absence = {"type": "string", "enum": ["ABSENT"]}
    if lint(schema):
        raise RuntimeError("post-09E DeepSeek strict linter must pass before Provider send")
    if not all(node_at(schema, pointer) == typed_absence for pointer in EXPECTED_POINTERS):
        raise RuntimeError("all nine typed-enum nodes must be present before Provider send")
    hashes = {spec.key: e2e.canonical_skill(spec)[1] for spec in e2e.ROLE_SPECS}
    if hashes != e2e.EXPECTED_HASHES:
        raise RuntimeError("canonical Skill hash drift blocks Provider send")
    contract = e2e.compiled_run_contract()
    source_files = {
        "director_input": SOURCE / "artifacts" / "director_input.json",
        "scene_writer_output": SOURCE / "artifacts" / "scene_writer_output.json",
        "showrunner_output": SOURCE / "artifacts" / "showrunner_output.json",
    }
    if not all(path.is_file() for path in source_files.values()):
        raise RuntimeError("frozen Director upstream artifacts are unavailable")
    return {
        "result": "PASS",
        "run_id": RUN_ID,
        "fixture_binding": os.environ["AFS_E2E_FIXTURE_BINDING"],
        "compiled_run_contract": {"fixture_id": contract["fixture"]["fixture_id"], "binding": os.environ["AFS_E2E_FIXTURE_BINDING"]},
        "source_artifacts": {name: {"path": str(path), "sha256": sha256_file(path)} for name, path in source_files.items()},
        "director_structured_contract_version": "Director Full Structured Submission V0.1",
        "compatibility_projection_version": PROJECTION_ID,
        "function_name": FUNCTION_NAME,
        "strict": True,
        "nine_typed_enum_pointers": list(EXPECTED_POINTERS),
        "canonical_skill_hashes": hashes,
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "retries": 0,
        "fallbacks": 0,
    }


def write_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    if EVIDENCE.exists():
        raise RuntimeError(f"immutable probe evidence root already exists: {EVIDENCE}")
    before = preflight()
    EVIDENCE.mkdir(parents=True)
    write_json(EVIDENCE / "preflight_manifest.json", before)
    upstream = json.loads((SOURCE / "artifacts" / "scene_writer_output.json").read_text(encoding="utf-8"))
    director_input = json.loads((SOURCE / "artifacts" / "director_input.json").read_text(encoding="utf-8"))["input"]
    executor = e2e.CanonicalRoleExecutor(evidence_dir=EVIDENCE, run_id=RUN_ID)
    try:
        result, input_path, output_path = executor.invoke(
            spec=e2e.role_spec("director"),
            input_payload=director_input,
            required_locks=upstream["canon_assignment_locks"],
            prohibited_changes=upstream["prohibited_changes"],
            structured_output=build_deepseek_compatible_director_contract(),
            structured_arguments_validator=e2e.make_director_payload_validator(
                selected_mode="PLAN",
                required_locks=upstream["canon_assignment_locks"],
                prohibited_changes=upstream["prohibited_changes"],
            ),
        )
    except Exception as exc:
        record = executor.call_records[0] if executor.call_records else {}
        report = {"classification": "DIRECTOR STRICT COMPATIBILITY PROBE 03", "result": "FAIL", "provider_calls": 1, "retries": 0, "fallbacks": 0, "exception_type": type(exc).__name__, "exception": str(exc), "preflight_manifest": str(EVIDENCE / "preflight_manifest.json"), "call_record": record}
        write_json(EVIDENCE / "probe_manifest.json", report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1
    record = executor.call_records[0]
    report = {"classification": "DIRECTOR STRICT COMPATIBILITY PROBE 03", "result": "PASS", "provider_calls": 1, "retries": 0, "fallbacks": 0, "function_name": FUNCTION_NAME, "equivalence": equivalence_report(), "preflight_manifest": str(EVIDENCE / "preflight_manifest.json"), "call_record": record, "output_artifact": str(output_path), "input_artifact": str(input_path), "primary_state_or_outcome": result["primary_state_or_outcome"]}
    write_json(EVIDENCE / "probe_manifest.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
