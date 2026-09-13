from __future__ import annotations

import copy
import hashlib
import inspect
import json
import subprocess
import sys
from pathlib import Path


STAGE = Path(__file__).resolve().parents[1]
RESEARCH = STAGE.parent
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
IMPLEMENTATION = STAGE / "implementation"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
R17 = HARNESS / "evidence" / "E2E-RUN-17"
CANONICAL = Path(r"E:\AI_Film_Studio\AI_Film_Studio_Obsidian_Vault_V0.1\01_SKILLS\06_Continuity\continuity\SKILL.md")
for path in (IMPLEMENTATION, HARNESS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from continuity_integration_contract import (  # noqa: E402
    canonical_outcomes_from_skill_text,
    validate_continuity_integration_output,
    validate_continuity_non_strict_transport,
)
import run_minimal_e2e as runner  # noqa: E402


def tree_digest(root: Path) -> tuple[int, str]:
    files = sorted((path for path in root.rglob("*") if path.is_file()), key=lambda path: str(path.relative_to(root)).lower())
    manifest = "\n".join(
        f"{path.relative_to(root)}|{hashlib.sha256(path.read_bytes()).hexdigest().upper()}"
        for path in files
    )
    return len(files), hashlib.sha256(manifest.encode("utf-8")).hexdigest().upper()


def run_suite(script: Path, expected: int) -> bool:
    completed = subprocess.run(
        [sys.executable, "-X", "utf8", "-B", str(script)],
        cwd=str(AUTOMATION_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        return False
    return completed.returncode == 0 and payload.get("passed") == expected and payload.get("total") == expected


def main() -> int:
    skill_text = CANONICAL.read_text(encoding="utf-8")
    canonical_outcomes = canonical_outcomes_from_skill_text(skill_text)
    continuity_spec = runner.role_spec("continuity")
    continuity_prompt = runner.build_system_prompt(continuity_spec, skill_text, run_id="REPAIR14-PROMPT-CAPTURE")
    provider_record = json.loads((R17 / "artifacts" / "continuity_provider_response.json").read_text(encoding="utf-8"))
    recorded = json.loads(provider_record["raw_content"])
    raw_hash_before = hashlib.sha256((R17 / "artifacts" / "continuity_provider_response.json").read_bytes()).hexdigest().upper()
    tree_before = tree_digest(R17)
    validation = validate_continuity_integration_output(recorded, canonical_skill_text=skill_text)
    integrated = runner.validate_role_output(
        continuity_spec,
        recorded,
        run_id="E2E-RUN-17-RECORDED-REPLAY",
        canonical_skill_text=skill_text,
    )

    variants = (
        "受支持的变化。",
        "证据显示该差异具有明确来源。",
        "The supplied evidence supports the recorded difference.",
        "已核对。",
    )
    variant_results = []
    for content in variants:
        payload = copy.deepcopy(recorded)
        payload["content"] = content
        variant_results.append(
            validate_continuity_integration_output(payload, canonical_skill_text=skill_text).evidence["canonical_outcome"]
        )

    source = inspect.getsource(sys.modules["continuity_integration_contract"])
    repair13 = run_suite(RESEARCH / "E2E_Targeted_Repair_13_Character_Acting_Reserved_Transport_Slot_Alignment_V0.1" / "tests" / "run_character_acting_transport_core_tests.py", 17)
    repair12 = run_suite(RESEARCH / "E2E_Targeted_Repair_12_Art_Director_Output_Contract_Validator_Alignment_V0.1" / "tests" / "run_art_director_alignment_core_tests.py", 17)
    repair11 = run_suite(RESEARCH / "E2E_Targeted_Repair_11_Strict_Transport_Lifecycle_Authorization_V0.1" / "tests" / "run_strict_transport_lifecycle_tests.py", 30)
    historical_failure = json.loads((R17 / "failure_attribution.json").read_text(encoding="utf-8"))[0]
    validate_continuity_non_strict_transport(strict_enabled=False)
    raw_hash_after = hashlib.sha256((R17 / "artifacts" / "continuity_provider_response.json").read_bytes()).hexdigest().upper()
    tree_after = tree_digest(R17)

    checks = [
        ("CONT-ALIGN-01", all(path.is_file() for path in (CANONICAL, R17 / "artifacts" / "continuity_provider_response.json", R17 / "failure_attribution.json")), "provenance audit sources are complete"),
        ("CONT-ALIGN-02", validation.evidence["machine_identity_source"] == "primary_state_or_outcome" and "exact canonical primary_state_or_outcome as machine identity" in continuity_prompt, "primary_state_or_outcome is aligned across prompt and validator"),
        ("CONT-ALIGN-03", integrated["primary_state_or_outcome"] == recorded["primary_state_or_outcome"], "canonical outcome is recognized through the integrated live validator"),
        ("CONT-ALIGN-04", validation.evidence["canonical_outcome"] == "AUTHORIZED OR SUPPORTED CHANGE", "exact supported-change outcome passes"),
        ("CONT-ALIGN-05", validation.evidence["state_evidence_fields"] == list(runner.validate_state_evidence(recorded["state_evidence"], "Continuity")), "six State Evidence dimensions pass"),
        ("CONT-ALIGN-06", "semantic_signals" not in source and ".casefold(" not in source and validation.evidence["keyword_heuristics"] == [] and "not universal output requirements" in continuity_prompt, "unauthorized universal keyword heuristic is absent from prompt and validator"),
        ("CONT-ALIGN-07", validation.evidence["presence_signal"] == "CONDITIONAL_CANONICAL_REVIEW_DIMENSION_NOT_SEPARATE_MACHINE_FIELD", "presence is conditional evidence, not a prose keyword requirement"),
        ("CONT-ALIGN-08", validation.evidence["authorized_change_signal"] == "CANONICAL_OUTCOME_IDENTITY_NOT_PROSE_DERIVATION", "authorized change identity is not derived from prose"),
        ("CONT-ALIGN-09", len(set(variant_results)) == 1, "display prose variants do not change machine validation"),
        ("CONT-ALIGN-10", variant_results[0] == variant_results[1] == recorded["primary_state_or_outcome"], "Chinese prose wording is machine-independent"),
        ("CONT-ALIGN-11", canonical_outcomes == continuity_spec.allowed_outcomes, "canonical outcome integrity is preserved from the Skill"),
        ("CONT-ALIGN-12", validation.evidence["authority_actions"] == ["OBSERVE", "COMPARE", "CLASSIFY", "FLAG", "ROUTE"], "Continuity authority is preserved and non-strict"),
        ("CONT-ALIGN-13", raw_hash_before == raw_hash_after and tree_before == tree_after, "E2E-RUN-17 recorded response is evaluated read-only"),
        ("CONT-ALIGN-14", historical_failure["layer"] == "TRANSPORT / PARSER CONTRACT FAILURE" and validation.payload == recorded, "historical parser attribution remains exact while corrected validation passes"),
        ("CONT-ALIGN-15", repair13, "Character & Acting Repair13 regression passes 17/17"),
        ("CONT-ALIGN-16", repair12, "Art Director Repair12 regression passes 17/17"),
        ("CONT-ALIGN-17", repair11, "Repair11 lifecycle regression passes 30/30"),
    ]
    results = [{"id": item_id, "result": "PASS" if passed else "FAIL", "detail": detail} for item_id, passed, detail in checks]
    output = {
        "classification": "CONTINUITY REPAIR14 ALIGNMENT CORE TESTS",
        "results": results,
        "passed": sum(item["result"] == "PASS" for item in results),
        "total": len(results),
        "recorded_replay": {
            "decision": "RECORDED CONTINUITY RESPONSE SATISFIES CORRECTED VALIDATOR",
            "historical_status_preserved": True,
            "historical_status": "BLOCKED",
            "raw_response_sha256": raw_hash_after,
            "tree_file_count": tree_after[0],
            "tree_sha256": tree_after[1],
        },
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "real_e2e_runs": 0,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] == output["total"] == 17 else 1


if __name__ == "__main__":
    raise SystemExit(main())
