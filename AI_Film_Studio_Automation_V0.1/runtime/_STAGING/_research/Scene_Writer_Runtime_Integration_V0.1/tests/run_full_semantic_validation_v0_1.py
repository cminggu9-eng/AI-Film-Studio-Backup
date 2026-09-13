"""Run the authorised one-pass full semantic-validation fixture pack.

This runner never retries, resamples, repairs, or overwrites prior evidence.
Each fixture is one real canonical Scene Writer execution followed by the
already-bound semantic verifier inside Runtime.
"""

from __future__ import annotations

import copy
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
for path in (str(STAGE), str(AUTOMATION_ROOT)):
    if path not in sys.path:
        sys.path.insert(0, path)

from runtime.scene_writer.scene_writer_executor_binding import create_scene_writer_binding  # noqa: E402


FIXTURE_PATH = STAGE / "fixtures" / "full_semantic_validation_v0_1.json"
RESULT_DIRECTORY = STAGE / "Full_Semantic_Validation_Raw_Results_V0.1"
CLASSIFICATION = "FULL SEMANTIC VALIDATION / SYNTHETIC / NON-CANON / REAL SEMANTIC EXECUTION"


def safe_cost(provider, usage_record: Any) -> float | None:
    usage = usage_record.get("usage") if isinstance(usage_record, dict) else None
    return provider.estimate_cost_cny(usage) if isinstance(usage, dict) else None


def main() -> int:
    if not os.environ.get("DEEPSEEK_API_KEY", "").strip():
        print(json.dumps({"key_status": "NOT AVAILABLE", "result": "NOT EXECUTED"}, ensure_ascii=False, indent=2))
        return 1
    fixtures = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    if RESULT_DIRECTORY.exists():
        raise RuntimeError(f"Validation evidence directory already exists: {RESULT_DIRECTORY}")
    RESULT_DIRECTORY.mkdir(parents=False)
    manifest = {
        "classification": CLASSIFICATION,
        "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "fixture_count": len(fixtures),
        "formal_execution_count_planned": len(fixtures),
        "resample_policy": "PROHIBITED",
        "technical_retry_policy": "NO_AUTOMATIC_RETRY",
        "fixture_ids": [fixture["id"] for fixture in fixtures],
    }
    (RESULT_DIRECTORY / "execution_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    bundle = create_scene_writer_binding(execution_classification=CLASSIFICATION)
    reports: list[Dict[str, Any]] = []
    for sequence, fixture in enumerate(fixtures, start=1):
        fixture_id = fixture["id"]
        request_id = f"FSV-SW-{fixture_id}"
        assignment = copy.deepcopy(fixture["assignment"])
        assignment["request_id"] = request_id
        generation_invocation_id = f"scene-writer:{request_id}"
        verification_invocation_id = f"scene-writer-integrity:{request_id}"
        try:
            runtime_result = bundle.runtime.execute(assignment)
            exception = None
        except Exception as exc:  # Evidence must record any unexpected technical failure without retry.
            runtime_result = None
            exception = f"{type(exc).__name__}: {exc}"
        generation_usage = bundle.executor.usage_for(generation_invocation_id)
        verification_usage = bundle.semantic_verifier.usage_for(verification_invocation_id)
        generation_cost = safe_cost(bundle.provider, generation_usage)
        verification_cost = safe_cost(bundle.provider, verification_usage)
        evidence = {
            "fixture": fixture,
            "sequence": sequence,
            "classification": CLASSIFICATION,
            "formal_execution_count_for_fixture": 1,
            "resamples_for_fixture": 0,
            "provider": bundle.provider.provider,
            "model": bundle.provider.model,
            "assignment": assignment,
            "runtime_result": runtime_result,
            "unexpected_exception": exception,
            "generation_usage": generation_usage,
            "verification_usage": verification_usage,
            "estimated_cost_cny": {
                "generation": generation_cost,
                "verification": verification_cost,
                "total": round(generation_cost + verification_cost, 8) if generation_cost is not None and verification_cost is not None else None,
            },
            "pricing_basis": bundle.provider.pricing_basis(),
        }
        raw_path = RESULT_DIRECTORY / f"{fixture_id}_raw_result.json"
        raw_path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
        reports.append({
            "id": fixture_id,
            "raw_result": raw_path.name,
            "runtime_status": runtime_result.get("runtime_status") if isinstance(runtime_result, dict) else None,
            "primary_state": runtime_result.get("scene_writer", {}).get("control_data", {}).get("primary_state") if isinstance(runtime_result, dict) and isinstance(runtime_result.get("scene_writer"), dict) else None,
            "verifier_result": runtime_result.get("semantic_integrity_validation", {}).get("integrity_result") if isinstance(runtime_result, dict) and isinstance(runtime_result.get("semantic_integrity_validation"), dict) else None,
            "exception": exception,
            "estimated_cost_cny": evidence["estimated_cost_cny"]["total"],
        })
    summary = {
        **manifest,
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "provider": bundle.provider.provider,
        "model": bundle.provider.model,
        "reports": reports,
        "successful_runtime_executions": sum(item["runtime_status"] == "SUCCESS" for item in reports),
        "runtime_non_successes": sum(item["runtime_status"] != "SUCCESS" for item in reports),
        "estimated_total_cost_cny": round(sum(item["estimated_cost_cny"] or 0 for item in reports), 8),
        "pricing_basis": bundle.provider.pricing_basis(),
    }
    (RESULT_DIRECTORY / "execution_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
