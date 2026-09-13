"""Provider-free Director output-contract tests for Repair 05.

The recorded Rerun03 response is immutable input.  These tests never invoke a
provider or executor and never alter the recorded response.
"""

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
RERUN03_RAW = HARNESS_STAGE / "evidence" / "E2E-RUN-03" / "artifacts" / "director_provider_response.json"
for import_path in (str(IMPLEMENTATION), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

from director_integration_contract import (  # noqa: E402
    DIRECTOR_CANONICAL_MODES,
    DIRECTOR_CANONICAL_OUTPUT_HEADINGS,
    DIRECTOR_PRIMARY_STATES,
    DIRECTOR_SEMANTIC_FIELDS,
    DirectorIntegrationContractError,
    inspect_director_semantic_fields,
    validate_director_integration_output,
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
    persisted = json.loads(RERUN03_RAW.read_text(encoding="utf-8"))
    raw_content = persisted["raw_content"]
    return json.loads(raw_content), hashlib.sha256(raw_content.encode("utf-8")).hexdigest()


def _canonical_order_content(content: str) -> str:
    sections: dict[str, str] = {}
    positions = sorted(
        ((heading, content.index(heading)) for heading in DIRECTOR_CANONICAL_OUTPUT_HEADINGS),
        key=lambda item: item[1],
    )
    for index, (heading, start) in enumerate(positions):
        end = positions[index + 1][1] if index + 1 < len(positions) else len(content)
        sections[heading] = content[start + len(heading):end].strip()
    return "\n\n".join(f"{heading}\n\n{sections[heading]}" for heading in DIRECTOR_CANONICAL_OUTPUT_HEADINGS)


def _expect_contract_failure(action: Callable[[], Any]) -> bool:
    try:
        action()
    except DirectorIntegrationContractError:
        return True
    return False


def main() -> int:
    recorded, raw_hash = _recorded_output()
    recorded_snapshot = copy.deepcopy(recorded)
    director = role_spec("director")
    ordered = copy.deepcopy(recorded)
    ordered["content"] = _canonical_order_content(recorded["content"])
    results: list[dict[str, str]] = []

    results.append({
        "id": "DIR-INT-01",
        "result": "PASS" if DIRECTOR_CANONICAL_MODES == ("PLAN", "REVISE", "DIAGNOSE") and director.selected_mode == "PLAN" else "FAIL",
        "detail": "canonical Director Modes remain exact",
    })
    results.append({
        "id": "DIR-INT-02",
        "result": "PASS" if DIRECTOR_PRIMARY_STATES == director.allowed_outcomes else "FAIL",
        "detail": "canonical Director Primary States remain exact",
    })
    field_ids = tuple(field_id for field_id, _ in DIRECTOR_SEMANTIC_FIELDS)
    results.append({
        "id": "DIR-INT-03",
        "result": "PASS" if len(field_ids) == 8 and len(set(field_ids)) == 8 and len(DIRECTOR_CANONICAL_OUTPUT_HEADINGS) == 8 else "FAIL",
        "detail": "all canonical Director semantic fields are accounted exactly once",
    })
    results.append({
        "id": "DIR-INT-04",
        "result": "PASS" if all(field_id != heading for field_id, heading in DIRECTOR_SEMANTIC_FIELDS) and tuple(heading for _, heading in DIRECTOR_SEMANTIC_FIELDS) == DIRECTOR_CANONICAL_OUTPUT_HEADINGS else "FAIL",
        "detail": "stable machine field IDs are distinct from canonical display-heading tokens",
    })
    inspection = inspect_director_semantic_fields(recorded["content"])
    legacy_required = ("Directorial Intent", "Staging/Blocking", "Spatial Geography", "Audience Information", "Rhythm/Transition", "Production Burden")
    mixed = inspection.semantic_fields_present and not inspection.canonical_order and any(heading not in recorded["content"] for heading in legacy_required)
    results.append({
        "id": "DIR-INT-05",
        "result": "PASS" if mixed and _expect_contract_failure(lambda: validate_director_integration_output(recorded)) else "FAIL",
        "detail": "Rerun03 is MIXED STRUCTURAL + TRANSPORT, not a semantic-content failure",
    })
    heading_different = copy.deepcopy(ordered)
    heading_different["content"] = heading_different["content"].replace("DIRECTORIAL INTENT", "导演意图", 1)
    heading_different_snapshot = copy.deepcopy(heading_different)
    results.append({
        "id": "DIR-INT-06",
        "result": "PASS" if _expect_contract_failure(lambda: validate_director_integration_output(heading_different)) and heading_different == heading_different_snapshot else "FAIL",
        "detail": "semantic-complete fixture with a different heading is structurally rejected without heading repair",
    })
    missing_field = copy.deepcopy(ordered)
    missing_field["content"] = missing_field["content"].replace("PRODUCTION BURDEN", "", 1)
    results.append({
        "id": "DIR-INT-07",
        "result": "PASS" if _expect_contract_failure(lambda: validate_director_integration_output(missing_field)) else "FAIL",
        "detail": "a genuinely missing required field remains rejected",
    })
    unknown_token = copy.deepcopy(ordered)
    unknown_token["primary_state_or_outcome"] = "NEEDS_DECISION"
    results.append({
        "id": "DIR-INT-08",
        "result": "PASS" if _expect_contract_failure(lambda: validate_director_integration_output(unknown_token)) else "FAIL",
        "detail": "an unknown canonical primary-state token is rejected",
    })
    before_hash = hashlib.sha256(json.dumps(recorded, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    _expect_contract_failure(lambda: validate_director_integration_output(recorded))
    after_hash = hashlib.sha256(json.dumps(recorded, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    results.append({
        "id": "DIR-INT-09",
        "result": "PASS" if recorded == recorded_snapshot and before_hash == after_hash else "FAIL",
        "detail": "failed validation performs no semantic or heading auto-repair",
    })
    _, canonical_hash = canonical_skill(director)
    results.append({
        "id": "DIR-INT-10",
        "result": "PASS" if canonical_hash == EXPECTED_HASHES["director"] else "FAIL",
        "detail": "canonical Director Skill hash is unchanged",
    })
    accepted = validate_role_output(
        director,
        ordered,
        required_locks=ordered["canon_assignment_locks"],
        prohibited_changes=ordered["prohibited_changes"],
        run_id="DIRECTOR-CONTRACT-TEST",
    )
    envelope = make_envelope(
        director,
        accepted,
        "Character & Acting",
        "Director integration-contract regression",
        RERUN03_RAW,
        run_id="DIRECTOR-CONTRACT-TEST",
    )
    results.append({
        "id": "DIR-INT-11",
        "result": "PASS" if envelope["canonical_mode"] == "PLAN" and envelope["primary_state_or_outcome"] == "DIRECTION_PLAN_PRODUCED" else "FAIL",
        "detail": "validated Director State & Evidence Envelope preserves canonical state",
    })
    tokens_preserved = e2e_int_12_tokens_preserved(role_results={"director": accepted}, envelopes={"director": envelope})
    results.append({
        "id": "DIR-INT-12",
        "result": "PASS" if tokens_preserved else "FAIL",
        "detail": "E2E-INT-12 preserves Director mode, state, flags, and handoffs exactly",
    })

    passed = sum(item["result"] == "PASS" for item in results)
    print(json.dumps({
        "classification": "DIRECTOR INTEGRATION OUTPUT CONTRACT TEST",
        "source_artifact": str(RERUN03_RAW),
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
