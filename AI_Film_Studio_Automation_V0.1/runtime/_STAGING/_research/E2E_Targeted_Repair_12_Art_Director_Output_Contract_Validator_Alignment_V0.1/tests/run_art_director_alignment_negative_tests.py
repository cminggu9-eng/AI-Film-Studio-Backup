"""Provider-free Repair12 negative alignment tests (12/12 required)."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Callable


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research"
REPAIR06 = RESEARCH / "E2E_Targeted_Repair_06_Art_Director_Output_Contract_Parser_Alignment_V0.1"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
for path in (REPAIR06 / "implementation", HARNESS, AUTOMATION_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from art_director_integration_contract import (  # noqa: E402
    ART_DIRECTOR_FAILURE_ALIGNMENT,
    ART_DIRECTOR_FAILURE_AUTHORITY,
    ART_DIRECTOR_FAILURE_TOKEN,
    ART_DIRECTOR_REQUIRED_DISPLAY_HEADINGS,
    ArtDirectorIntegrationContractError,
    art_director_machine_field_manifest,
    art_director_prompt_contract_instruction,
    classify_art_director_failure,
    validate_art_director_integration_output,
)
from run_minimal_e2e import build_system_prompt, output_schema, role_spec  # noqa: E402


def rejected(action: Callable[[], object], classification: str | None = None) -> bool:
    try:
        action()
    except ArtDirectorIntegrationContractError as exc:
        return classification is None or exc.classification == classification
    return False


def main() -> int:
    raw_path = HARNESS / "evidence" / "E2E-RUN-15" / "artifacts" / "art_director_provider_response.json"
    base = json.loads(json.loads(raw_path.read_text(encoding="utf-8"))["raw_content"])
    source = (REPAIR06 / "implementation" / "art_director_integration_contract.py").read_text(encoding="utf-8")
    spec = role_spec("art_director")
    skill = (AUTOMATION_ROOT.parent / "AI_Film_Studio_Obsidian_Vault_V0.1" / "01_SKILLS" / "05_Art_Director" / "art-director" / "SKILL.md").read_text(encoding="utf-8")
    prompt = build_system_prompt(spec, skill, run_id="REPAIR12-NEGATIVE-CAPTURE")
    manifest = art_director_machine_field_manifest()

    invalid_visual = copy.deepcopy(base)
    invalid_visual["state_evidence"]["visual_state"] = {"bad": {1, 2}}
    cross_fill = copy.deepcopy(base)
    cross_fill["state_evidence"]["visual_state"] = 42
    cross_fill_before = copy.deepcopy(cross_fill)
    keyword_substitute = copy.deepcopy(base)
    keyword_substitute["unresolved_decisions"] = {"invalid": True}
    keyword_substitute["content"] += " production feasibility budget constraint 制作 可行性 采购 重复拍摄"
    missing_field = copy.deepcopy(base)
    del missing_field["unresolved_decisions"]
    mutated_outcome = copy.deepcopy(base)
    mutated_outcome["primary_state_or_outcome"] = "DESIGN_READY"
    authority_takeover = copy.deepcopy(base)
    authority_takeover["scene_packages"] = {"camera_execution": "takeover"}
    no_conditional = copy.deepcopy(base)
    no_conditional["content"] = "最小充分设计响应。"
    no_conditional["unresolved_decisions"] = []

    identity = set(output_schema(spec)) == set(manifest["required_top_level_fields"])
    no_heuristic = not any(marker in source for marker in ("FORBIDDEN_AI_PRODUCTION_TOKENS", "required_checks", "any(token in", "_json_text", ".casefold()"))
    results = [
        ("AD-ALIGN-NEG-01", validate_art_director_integration_output(base)["visual_state_representation"] == "ABSENT", "lawful ABSENT is not rejected by an object-only assertion"),
        ("AD-ALIGN-NEG-02", rejected(lambda: validate_art_director_integration_output(invalid_visual)), "invalid visual_state object is rejected"),
        ("AD-ALIGN-NEG-03", rejected(lambda: validate_art_director_integration_output(cross_fill)) and cross_fill == cross_fill_before, "other fields do not auto-fill visual_state"),
        ("AD-ALIGN-NEG-04", no_heuristic, "production keyword heuristic is absent"),
        ("AD-ALIGN-NEG-05", rejected(lambda: validate_art_director_integration_output(keyword_substitute)), "keyword-rich prose cannot compensate for an invalid machine field"),
        ("AD-ALIGN-NEG-06", identity and art_director_prompt_contract_instruction() in prompt, "validator requires no field absent from prompt/schema"),
        ("AD-ALIGN-NEG-07", identity and "no mandatory display headings or required keywords" in prompt, "prompt requires no content absent from the contract"),
        ("AD-ALIGN-NEG-08", ART_DIRECTOR_REQUIRED_DISPLAY_HEADINGS == () and spec.required_content_headings == (), "fixed heading requirement has not returned"),
        ("AD-ALIGN-NEG-09", validate_art_director_integration_output(no_conditional)["unresolved_decisions_representation"] == "EMPTY_ARRAY", "conditional content is not treated as mandatory"),
        ("AD-ALIGN-NEG-10", classify_art_director_failure(provider_schema_allows_representation=True, validator_rejected=True, canonical_semantic_violation=False) == ART_DIRECTOR_FAILURE_ALIGNMENT, "integration mismatch is not classified ROLE SEMANTIC FAILURE"),
        ("AD-ALIGN-NEG-11", rejected(lambda: validate_art_director_integration_output(mutated_outcome), ART_DIRECTOR_FAILURE_TOKEN), "canonical outcome mutation is rejected"),
        ("AD-ALIGN-NEG-12", rejected(lambda: validate_art_director_integration_output(authority_takeover), ART_DIRECTOR_FAILURE_AUTHORITY), "Art Director authority takeover through transport is rejected"),
    ]
    records = [{"id": item_id, "result": "PASS" if passed else "FAIL", "detail": detail} for item_id, passed, detail in results]
    passed = sum(item["result"] == "PASS" for item in records)
    print(json.dumps({
        "classification": "ART DIRECTOR REPAIR12 ALIGNMENT NEGATIVE TESTS",
        "results": records,
        "passed": passed,
        "total": len(records),
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "real_e2e_runs": 0,
    }, ensure_ascii=False, indent=2))
    return 0 if passed == len(records) else 1


if __name__ == "__main__":
    raise SystemExit(main())
