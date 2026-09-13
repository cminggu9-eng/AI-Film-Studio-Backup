from __future__ import annotations

import copy
import inspect
import json
import sys
from pathlib import Path


STAGE = Path(__file__).resolve().parents[1]
IMPLEMENTATION = STAGE / "implementation"
HARNESS = STAGE.parent / "Minimal_E2E_Runtime_Validation_V0.1"
R17 = HARNESS / "evidence" / "E2E-RUN-17"
CANONICAL = Path(r"E:\AI_Film_Studio\AI_Film_Studio_Obsidian_Vault_V0.1\01_SKILLS\06_Continuity\continuity\SKILL.md")
if str(IMPLEMENTATION) not in sys.path:
    sys.path.insert(0, str(IMPLEMENTATION))

from continuity_integration_contract import (  # noqa: E402
    ContinuityIntegrationContractError,
    validate_continuity_integration_output,
)


def fails(payload: object, skill_text: str, classification: str | None = None) -> bool:
    try:
        validate_continuity_integration_output(payload, canonical_skill_text=skill_text)  # type: ignore[arg-type]
    except ContinuityIntegrationContractError as exc:
        return classification is None or exc.classification == classification
    return False


def main() -> int:
    skill_text = CANONICAL.read_text(encoding="utf-8")
    provider_record = json.loads((R17 / "artifacts" / "continuity_provider_response.json").read_text(encoding="utf-8"))
    valid = json.loads(provider_record["raw_content"])
    source = inspect.getsource(sys.modules["continuity_integration_contract"])

    minimal = copy.deepcopy(valid)
    minimal["content"] = "说明。"
    presence_independent = validate_continuity_integration_output(minimal, canonical_skill_text=skill_text)

    prose_override = copy.deepcopy(valid)
    prose_override["primary_state_or_outcome"] = "INVALID OUTCOME"
    prose_override["content"] = "AUTHORIZED OR SUPPORTED CHANGE 受支持的变化"

    translated = copy.deepcopy(valid)
    translated["primary_state_or_outcome"] = "授权或受支持的变化"

    alias = copy.deepcopy(valid)
    alias["primary_state_or_outcome"] = "SUPPORTED CHANGE"

    missing_outcome = copy.deepcopy(valid)
    del missing_outcome["primary_state_or_outcome"]
    missing_outcome["content"] = "AUTHORIZED OR SUPPORTED CHANGE"

    missing_state = copy.deepcopy(valid)
    del missing_state["state_evidence"]["visual_state"]
    missing_state["content"] = "presence authorized supported continuity location knowledge relationship"
    wrong_state = copy.deepcopy(valid)
    wrong_state["state_evidence"]["visual_state"] = ["keyword-rich", "presence"]
    null_state = copy.deepcopy(valid)
    null_state["state_evidence"]["visual_state"] = None

    repair_attempt = copy.deepcopy(valid)
    repair_attempt["handoffs"] = [{"action": "repair", "owner": "Continuity"}]

    valid_direct = validate_continuity_integration_output(valid, canonical_skill_text=skill_text)
    checks = [
        ("CONT-ALIGN-NEG-01", valid_direct.evidence["canonical_outcome"] == valid["primary_state_or_outcome"], "valid canonical outcome cannot be ignored"),
        ("CONT-ALIGN-NEG-02", "semantic_signals" not in source and ".casefold(" not in source, "all-keyword requirement cannot return"),
        ("CONT-ALIGN-NEG-03", presence_independent.evidence["canonical_outcome"] == valid["primary_state_or_outcome"], "presence keyword is not required without machine authority"),
        ("CONT-ALIGN-NEG-04", "受支持的变化" not in source, "Chinese phrase is not required for machine identity"),
        ("CONT-ALIGN-NEG-05", "authorized change" not in source.lower(), "English phrase is not required for machine identity"),
        ("CONT-ALIGN-NEG-06", fails(translated, skill_text, "ROLE SEMANTIC FAILURE"), "display prose cannot override a translated canonical token"),
        ("CONT-ALIGN-NEG-07", fails(prose_override, skill_text, "ROLE SEMANTIC FAILURE"), "valid prose cannot rescue an invalid canonical token"),
        ("CONT-ALIGN-NEG-08", all(fails(item, skill_text, "STATE TRANSPORT FAILURE") for item in (missing_state, wrong_state, null_state)), "keywords cannot rescue missing, wrong-type, or null State Evidence"),
        ("CONT-ALIGN-NEG-09", fails(missing_outcome, skill_text, "TRANSPORT / PARSER CONTRACT FAILURE"), "parser cannot guess a missing machine outcome from prose"),
        ("CONT-ALIGN-NEG-10", fails({key: value for key, value in valid.items() if key != "scene_packages"}, skill_text, "TRANSPORT / PARSER CONTRACT FAILURE"), "integration parser failure is not classified role semantic"),
        ("CONT-ALIGN-NEG-11", fails(repair_attempt, skill_text, "HANDOFF CONTRACT FAILURE"), "Continuity cannot claim repair authority"),
        ("CONT-ALIGN-NEG-12", fails(alias, skill_text, "ROLE SEMANTIC FAILURE"), "canonical outcome alias is rejected"),
    ]
    results = [{"id": item_id, "result": "PASS" if passed else "FAIL", "detail": detail} for item_id, passed, detail in checks]
    output = {
        "classification": "CONTINUITY REPAIR14 ALIGNMENT NEGATIVE TESTS",
        "results": results,
        "passed": sum(item["result"] == "PASS" for item in results),
        "total": len(results),
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "real_e2e_runs": 0,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] == output["total"] == 12 else 1


if __name__ == "__main__":
    raise SystemExit(main())
