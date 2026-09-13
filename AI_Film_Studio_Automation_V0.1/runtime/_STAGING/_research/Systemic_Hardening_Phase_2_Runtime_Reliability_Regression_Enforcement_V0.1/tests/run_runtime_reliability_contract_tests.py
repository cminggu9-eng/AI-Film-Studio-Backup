"""Provider-free P0/P1 reliability checks using only synthetic or recorded data."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Callable


PHASE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in PHASE.parents if (parent / "studio.config.json").is_file())
HARNESS = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1"
GOLDEN = HARNESS / "evidence" / "E2E-RUN-05"
sys.path.insert(0, str(HARNESS))

from runtime_reliability_contract import STRICT_TRANSPORT_AUTHORIZATION_REGISTRY, RuntimeReliabilityContractError, validate_execution_boundary, validate_golden_recorded_evidence, validate_lifecycle_consistency  # noqa: E402


def rejects(action: Callable[[], Any]) -> bool:
    try:
        action()
    except RuntimeReliabilityContractError:
        return True
    return False


def main() -> int:
    manifest = json.loads((GOLDEN / "execution_manifest.json").read_text(encoding="utf-8"))
    provider = json.loads((GOLDEN / "provider_manifest.json").read_text(encoding="utf-8"))
    handoffs = json.loads((GOLDEN / "handoff_trace.json").read_text(encoding="utf-8"))
    ledger = json.loads((GOLDEN / "state_ledger.json").read_text(encoding="utf-8"))
    results: list[dict[str, str]] = []
    good_boundary = validate_execution_boundary(run_id="E2E-RUN-06", evidence_root=HARNESS / "evidence" / "E2E-RUN-06", stage=HARNESS, authorization_label="authorized")
    results.append({"id": "REL-01", "result": "PASS" if good_boundary["result"] == "PASS" else "FAIL", "detail": "canonical Run ID, root, and authorization are explicit before execution"})
    results.append({"id": "REL-02", "result": "PASS" if rejects(lambda: validate_execution_boundary(run_id="E2E-RUN-06", evidence_root=HARNESS / "evidence" / "nested" / "E2E-RUN-06", stage=HARNESS, authorization_label="authorized")) else "FAIL", "detail": "nested or ambiguous evidence root is rejected"})
    results.append({"id": "REL-03", "result": "PASS" if rejects(lambda: validate_execution_boundary(run_id="RUN-06", evidence_root=HARNESS / "evidence" / "RUN-06", stage=HARNESS, authorization_label="authorized")) else "FAIL", "detail": "non-canonical Run ID is rejected"})
    results.append({"id": "REL-04", "result": "PASS" if rejects(lambda: validate_execution_boundary(run_id="E2E-RUN-06", evidence_root=HARNESS / "evidence" / "E2E-RUN-06", stage=HARNESS, authorization_label="")) else "FAIL", "detail": "missing authorization is rejected before evidence creation or provider construction"})
    lifecycle = validate_lifecycle_consistency(manifest=manifest, provider_manifest=provider, handoffs=handoffs, ledger=ledger, evidence_root=GOLDEN, require_complete_chain=True)
    results.append({"id": "REL-05", "result": lifecycle["result"], "detail": "Golden manifest, calls, invocation IDs, handoffs, ledger, and root agree"})
    bad_provider = copy.deepcopy(provider)
    bad_provider["call_count"] = 6
    rejected_counts = validate_lifecycle_consistency(manifest=manifest, provider_manifest=bad_provider, handoffs=handoffs, ledger=ledger, evidence_root=GOLDEN, require_complete_chain=True)
    results.append({"id": "REL-06", "result": "PASS" if rejected_counts["result"] == "FAIL" else "FAIL", "detail": "provider count disagreement is classified as lifecycle failure"})
    outside_provider = copy.deepcopy(provider)
    outside_provider["calls"][0]["raw_response_artifact"] = str(PHASE / "outside.json")
    rejected_root = validate_lifecycle_consistency(manifest=manifest, provider_manifest=outside_provider, handoffs=handoffs, ledger=ledger, evidence_root=GOLDEN, require_complete_chain=True)
    results.append({"id": "REL-07", "result": "PASS" if rejected_root["result"] == "FAIL" else "FAIL", "detail": "raw/parsed/usage linkage cannot escape the declared evidence root"})
    golden = validate_golden_recorded_evidence(evidence_root=GOLDEN)
    results.append({"id": "REL-08", "result": golden["result"], "detail": "Golden recorded evidence replays seven outputs, six handoffs, ledger, outcomes, and E2E-INT without a provider"})
    authorized_isolation = (
        STRICT_TRANSPORT_AUTHORIZATION_REGISTRY == {"Scene Writer": "submit_scene_writer_package", "Director": "submit_director_package"}
        and lifecycle.get("strict_transport_call_count") == 1
        and lifecycle.get("authorized_strict_transport_call_count") == 1
        and lifecycle.get("strict_transport_authorizations") == [{"role": "Scene Writer", "function_name": "submit_scene_writer_package", "authorized": True, "strict": True, "tool_choice_function_name": "submit_scene_writer_package"}]
    )
    results.append({"id": "REL-09", "result": "PASS" if authorized_isolation else "FAIL", "detail": "DeepSeek Beta strict transport remains adapter-scoped and is admitted only through exact authorized role/function pairs"})
    passed = sum(item["result"] == "PASS" for item in results)
    print(json.dumps({"classification": "P0/P1 RUNTIME RELIABILITY CONTRACT", "results": results, "passed": passed, "total": len(results), "provider_calls": 0, "executor_calls": 0, "role_calls": 0}, ensure_ascii=False, indent=2))
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
