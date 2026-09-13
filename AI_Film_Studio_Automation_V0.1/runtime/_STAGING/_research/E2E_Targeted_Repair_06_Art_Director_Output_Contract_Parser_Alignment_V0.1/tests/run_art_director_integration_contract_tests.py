"""Provider-free Art Director output-contract tests for Repair 06."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Callable


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
IMPLEMENTATION = STAGE / "implementation"
HARNESS_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1"
RERUN04_RAW = HARNESS_STAGE / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1" / "evidence" / "E2E-RUN-04" / "artifacts" / "art_director_provider_response.json"
for import_path in (str(IMPLEMENTATION), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

from art_director_integration_contract import (  # noqa: E402
    ART_DIRECTOR_CANONICAL_MODES,
    ART_DIRECTOR_PRIMARY_STATES,
    ART_DIRECTOR_REQUIRED_DISPLAY_HEADINGS,
    ArtDirectorIntegrationContractError,
    art_director_machine_field_manifest,
    inspect_art_director_semantic_fields,
    validate_art_director_integration_output,
)
from run_minimal_e2e import (  # noqa: E402
    EXPECTED_HASHES,
    canonical_skill,
    e2e_int_12_tokens_preserved,
    make_envelope,
    role_spec,
    validate_role_output,
)


def _recorded_output() -> tuple[dict[str, Any], str]:
    persisted = json.loads(RERUN04_RAW.read_text(encoding="utf-8"))
    raw_content = persisted["raw_content"]
    return json.loads(raw_content), hashlib.sha256(raw_content.encode("utf-8")).hexdigest()


def _expect_contract_failure(action: Callable[[], Any]) -> bool:
    try:
        action()
    except ArtDirectorIntegrationContractError:
        return True
    return False


def main() -> int:
    recorded, raw_hash = _recorded_output()
    recorded_snapshot = copy.deepcopy(recorded)
    art_director = role_spec("art_director")
    results: list[dict[str, str]] = []

    results.append({
        "id": "AD-INT-01",
        "result": "PASS" if ART_DIRECTOR_CANONICAL_MODES == ("DESIGN", "REVISE", "DIAGNOSE") and art_director.selected_mode == "DESIGN" else "FAIL",
        "detail": "canonical Art Director Modes remain exact",
    })
    results.append({
        "id": "AD-INT-02",
        "result": "PASS" if ART_DIRECTOR_PRIMARY_STATES == art_director.allowed_outcomes else "FAIL",
        "detail": "canonical Art Director capability outcomes remain exact",
    })
    results.append({
        "id": "AD-INT-03",
        "result": "PASS" if ART_DIRECTOR_REQUIRED_DISPLAY_HEADINGS == () and art_director.required_content_headings == () else "FAIL",
        "detail": "minimum-sufficient Art Director output has no forced display-heading template",
    })
    inspection = inspect_art_director_semantic_fields(recorded)
    validation = validate_art_director_integration_output(recorded)
    results.append({
        "id": "AD-INT-04",
        "result": "PASS" if raw_hash == "fa919f8c3c8dfe9d821193a4717a8826a2aac39a31290aa72fa9e7e0257bea44" and inspection.output_is_permitted and validation["output_policy"] == "MINIMUM_SUFFICIENT_UNTEMPLATED_RECORDS" else "FAIL",
        "detail": "Rerun04 record satisfies the minimum-sufficient machine contract",
    })
    legacy_headings = ("Visual World", "A-17 Key", "Costume/Clothing State", "Environment/Prop Continuity", "Unresolved Feasibility")
    results.append({
        "id": "AD-INT-05",
        "result": "PASS" if not any(heading in recorded["content"] for heading in legacy_headings) and validation["required_display_headings"] == [] else "FAIL",
        "detail": "Rerun04 is not rejected for omitting historical English heading aliases",
    })
    compact = copy.deepcopy(recorded)
    compact["content"] = "设计意图：暴雨夜保留 A-17 黄铜钥匙；许宁湿透制服后换为干衣。采购与重复拍摄由 Production 确认。"
    results.append({
        "id": "AD-INT-06",
        "result": "PASS" if validate_art_director_integration_output(compact)["content_nonempty"] and validate_role_output(art_director, compact, required_locks=compact["canon_assignment_locks"], prohibited_changes=compact["prohibited_changes"], run_id="ART-DIRECTOR-CONTRACT-TEST")["content"] == compact["content"] else "FAIL",
        "detail": "a lawful compact record passes without category-heading expansion",
    })
    lawful_absence = copy.deepcopy(recorded)
    lawful_absence["content"] = "设计响应已完成。"
    lawful_absence["state_evidence"] = {field: "ABSENT" for field in lawful_absence["state_evidence"]}
    lawful_absence["unresolved_decisions"] = "ABSENT"
    results.append({
        "id": "AD-INT-07",
        "result": "PASS" if validate_art_director_integration_output(lawful_absence)["visual_state_representation"] == "ABSENT" else "FAIL",
        "detail": "lawful field-level ABSENT remains valid without semantic synthesis",
    })
    unknown_state = copy.deepcopy(recorded)
    unknown_state["primary_state_or_outcome"] = "DESIGN_READY"
    results.append({
        "id": "AD-INT-08",
        "result": "PASS" if _expect_contract_failure(lambda: validate_art_director_integration_output(unknown_state)) else "FAIL",
        "detail": "an unknown Art Director outcome token remains rejected",
    })
    authority_takeover = copy.deepcopy(recorded)
    authority_takeover["camera_execution"] = "unauthorized integration field"
    results.append({
        "id": "AD-INT-09",
        "result": "PASS" if _expect_contract_failure(lambda: validate_art_director_integration_output(authority_takeover)) else "FAIL",
        "detail": "authority-expanding machine fields remain rejected",
    })
    before_hash = hashlib.sha256(json.dumps(recorded, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    validate_art_director_integration_output(recorded)
    after_hash = hashlib.sha256(json.dumps(recorded, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    results.append({
        "id": "AD-INT-10",
        "result": "PASS" if recorded == recorded_snapshot and before_hash == after_hash and art_director_machine_field_manifest()["fields"]["content"]["content_keyword_requirements"] == [] else "FAIL",
        "detail": "validation performs no heading insertion or semantic repair",
    })
    _, canonical_hash = canonical_skill(art_director)
    results.append({
        "id": "AD-INT-11",
        "result": "PASS" if canonical_hash == EXPECTED_HASHES["art_director"] else "FAIL",
        "detail": "canonical Art Director Skill hash is unchanged",
    })
    accepted = validate_role_output(
        art_director,
        recorded,
        required_locks=recorded["canon_assignment_locks"],
        prohibited_changes=recorded["prohibited_changes"],
        run_id="ART-DIRECTOR-CONTRACT-TEST",
    )
    envelope = make_envelope(
        art_director,
        accepted,
        "Continuity",
        "Art Director integration-contract regression",
        RERUN04_RAW,
        run_id="ART-DIRECTOR-CONTRACT-TEST",
    )
    results.append({
        "id": "AD-INT-12",
        "result": "PASS" if envelope["canonical_mode"] == "DESIGN" and envelope["primary_state_or_outcome"] == "DESIGN_RESPONSE_READY" and e2e_int_12_tokens_preserved(role_results={"art_director": accepted}, envelopes={"art_director": envelope}) else "FAIL",
        "detail": "validated Art Director State & Evidence envelope preserves canonical transport tokens",
    })

    passed = sum(item["result"] == "PASS" for item in results)
    print(json.dumps({
        "classification": "ART DIRECTOR INTEGRATION OUTPUT CONTRACT TEST",
        "source_artifact": str(RERUN04_RAW),
        "source_raw_content_sha256": raw_hash,
        "results": results,
        "passed": passed,
        "total": len(results),
        "provider_calls": 0,
        "executor_calls": 0,
        "semantic_mutation": 0,
        "auto_repairs": 0,
    }, ensure_ascii=False, indent=2))
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
