"""Non-network shape and freeze checks for the full semantic-validation pack."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


STAGE = Path(__file__).resolve().parents[1]
FIXTURE_PATH = STAGE / "fixtures" / "full_semantic_validation_v0_1.json"
PLAN_PATH = STAGE / "Scene_Writer_Full_Semantic_Validation_Plan_V0.1.md"
CANONICAL_SKILL = Path("E:/AI_Film_Studio/AI_Film_Studio_Obsidian_Vault_V0.1/01_SKILLS/02_Scene_Writer/scene-writer/SKILL.md")
EXPECTED_SKILL_HASH = "93e1be12988f8caa6cdd76acb5e6c1bf6ad3ca0dff5806a2ea93511e66052dfb"


def main() -> int:
    fixtures = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    assert isinstance(fixtures, list) and len(fixtures) == 15, len(fixtures)
    ids = [fixture.get("id") for fixture in fixtures]
    assert ids == ["F01", "F02", "F03", "F04", "F05", "F06", "F07", "F08", "F09", "F10", "F11", "F12", "F13-A", "F13-B", "F14"], ids
    for fixture in fixtures:
        assignment = fixture.get("assignment")
        assert isinstance(assignment, dict), fixture["id"]
        assert assignment.get("output_language") == "zh-CN", fixture["id"]
        assert assignment.get("requested_mode") in {"CREATE", "REVISE", "DIAGNOSE"}, fixture["id"]
        assert isinstance(fixture.get("expected_boundaries", {}).get("must"), list), fixture["id"]
        assert isinstance(fixture.get("expected_boundaries", {}).get("must_not"), list), fixture["id"]
        assert "VALIDATION" not in json.dumps(assignment, ensure_ascii=False).upper() or assignment.get("project_id") == "FSV-SYNTHETIC", fixture["id"]
    assert PLAN_PATH.is_file() and "NO REPAIR DURING VALIDATION" in PLAN_PATH.read_text(encoding="utf-8")
    assert hashlib.sha256(CANONICAL_SKILL.read_bytes()).hexdigest() == EXPECTED_SKILL_HASH
    print(json.dumps({"classification": "NON-NETWORK FULL SEMANTIC VALIDATION FIXTURE PREFLIGHT", "fixtures": len(fixtures), "formal_executions": 15, "resamples": 0, "canonical_skill_hash": EXPECTED_SKILL_HASH, "result": "PASS"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
