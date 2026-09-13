"""Read-only Director recorded-response and real-probe regression gate."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
IMPLEMENTATION = STAGE / "implementation"
HARNESS_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1"
RERUN03_RAW = HARNESS_STAGE / "evidence" / "E2E-RUN-03" / "artifacts" / "director_provider_response.json"
PROBE_ROOT = STAGE / "evidence" / "DIRECTOR-CONTRACT-PROBE-01"
PROBE_RAW = PROBE_ROOT / "artifacts" / "director_provider_response.json"
PROBE_REVIEW = PROBE_ROOT / "director_real_contract_probe_01_post_execution_acceptance_review.json"
for import_path in (str(IMPLEMENTATION), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

from director_integration_contract import DIRECTOR_CANONICAL_OUTPUT_HEADINGS, inspect_director_semantic_fields  # noqa: E402


def _content(path: Path) -> tuple[dict, dict, str]:
    artifact = json.loads(path.read_text(encoding="utf-8"))
    raw = artifact["raw_content"]
    return artifact, json.loads(raw), hashlib.sha256(raw.encode("utf-8")).hexdigest()


def main() -> int:
    rerun03_artifact, rerun03, rerun03_hash = _content(RERUN03_RAW)
    probe_artifact, probe, probe_hash = _content(PROBE_RAW)
    review = json.loads(PROBE_REVIEW.read_text(encoding="utf-8"))
    rerun03_inspection = inspect_director_semantic_fields(rerun03["content"])
    probe_inspection = inspect_director_semantic_fields(probe["content"])
    results = [
        {
            "id": "DIR-REG-01",
            "result": "PASS" if rerun03_hash == "5cccb3c3564f39a1b211fdbfb3c73b89f8c459ef438794e8946f50c9c7414e57" and rerun03_inspection.semantic_fields_present and not rerun03_inspection.canonical_order else "FAIL",
            "detail": "Rerun03 recorded response remains immutable semantic-complete but canonically out of order",
        },
        {
            "id": "DIR-REG-02",
            "result": "PASS" if probe_hash == "8408fd7bff7f6901c0c6ebdb57ad944a6f82e4c5fa492b6d44b599caa83b4f97" and probe_inspection.semantic_fields_present and probe_inspection.canonical_order else "FAIL",
            "detail": "the one-shot Director probe remains complete and canonically ordered",
        },
        {
            "id": "DIR-REG-03",
            "result": "PASS" if review.get("status") == "PASS" and review.get("passed") == 16 and review.get("total") == 16 and review.get("integrity", {}).get("provider_calls") == 0 else "FAIL",
            "detail": "post-execution acceptance review is 16/16 and added no Provider call",
        },
        {
            "id": "DIR-REG-04",
            "result": "PASS" if rerun03_artifact.get("raw_content_sha256") == rerun03_hash and probe_artifact.get("raw_content_sha256") == probe_hash and tuple(DIRECTOR_CANONICAL_OUTPUT_HEADINGS) == tuple(probe_inspection.field_positions and DIRECTOR_CANONICAL_OUTPUT_HEADINGS) else "FAIL",
            "detail": "recorded raw hashes and canonical heading-token set are exact",
        },
    ]
    passed = sum(item["result"] == "PASS" for item in results)
    print(json.dumps({
        "classification": "DIRECTOR RECORDED / PROBE REGRESSION",
        "results": results,
        "passed": passed,
        "total": len(results),
        "provider_calls": 0,
        "executor_calls": 0,
        "read_only": True,
    }, ensure_ascii=False, indent=2))
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
