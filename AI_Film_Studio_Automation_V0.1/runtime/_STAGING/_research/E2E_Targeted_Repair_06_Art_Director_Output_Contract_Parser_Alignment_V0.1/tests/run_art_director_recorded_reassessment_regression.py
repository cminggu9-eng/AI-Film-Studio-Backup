"""Read-only regression for the persisted Rerun04 Art Director reassessment."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
HARNESS_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1"
RERUN04_RAW = HARNESS_STAGE / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1" / "evidence" / "E2E-RUN-04" / "artifacts" / "art_director_provider_response.json"
REVIEW = STAGE / "evidence" / "ART-DIRECTOR-CONTRACT-ALIGNMENT-01" / "art_director_rerun_04_output_contract_reassessment.json"


def main() -> int:
    persisted = json.loads(RERUN04_RAW.read_text(encoding="utf-8"))
    review = json.loads(REVIEW.read_text(encoding="utf-8"))
    raw_hash = hashlib.sha256(persisted["raw_content"].encode("utf-8")).hexdigest()
    recorded_results = review.get("results") if isinstance(review.get("results"), list) else []
    checks = [item.get("result") == "PASS" for item in recorded_results]
    integrity_ok = (
        len(checks) == 8
        and review.get("status") == "PASS"
        and review.get("passed") == 8
        and review.get("total") == 8
        and raw_hash == persisted.get("raw_content_sha256") == "fa919f8c3c8dfe9d821193a4717a8826a2aac39a31290aa72fa9e7e0257bea44"
        and review.get("integrity", {}).get("provider_calls") == 0
        and review.get("alignment", {}).get("semantic_mutation") == 0
    )
    if checks and not integrity_ok:
        checks[0] = False
    passed = sum(checks)
    print(json.dumps({
        "classification": "ART DIRECTOR RERUN04 RECORDED REASSESSMENT REGRESSION",
        "results": [{"id": f"AD-R04-{index:02d}", "result": "PASS" if result else "FAIL"} for index, result in enumerate(checks, 1)],
        "passed": passed,
        "total": len(checks),
        "recorded_reassessment": "8/8 PASS" if checks[0] and checks[1] else "FAIL",
        "provider_calls": 0,
        "executor_calls": 0,
        "read_only": True,
    }, ensure_ascii=False, indent=2))
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
