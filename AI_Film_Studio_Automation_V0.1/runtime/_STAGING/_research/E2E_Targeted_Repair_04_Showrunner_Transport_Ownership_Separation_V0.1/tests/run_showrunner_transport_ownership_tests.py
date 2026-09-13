"""Provider-free ownership and recorded-response regressions for Repair 04."""

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
RERUN02_RAW = HARNESS_STAGE / "evidence" / "E2E-RUN-02" / "artifacts" / "showrunner_provider_response.json"
for import_path in (str(IMPLEMENTATION), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

from showrunner_transport_hydration import (  # noqa: E402
    ABSENT,
    SHOWRUNNER_STATUS_TOKENS,
    ShowrunnerRolePayloadError,
    ShowrunnerTransportHydrationError,
    hydrate_showrunner_transport,
    validate_showrunner_role_owned_payload,
)
from run_minimal_e2e import (  # noqa: E402
    EXPECTED_HASHES,
    canonical_skill,
    e2e_int_12_tokens_preserved,
    make_envelope,
    role_spec,
    validate_role_output,
)


def _raw_showrunner_payload() -> tuple[dict[str, Any], str]:
    persisted = json.loads(RERUN02_RAW.read_text(encoding="utf-8"))
    raw_content = persisted["raw_content"]
    return json.loads(raw_content), hashlib.sha256(raw_content.encode("utf-8")).hexdigest()


def _expect_role_owned_failure(action: Callable[[], Any]) -> bool:
    try:
        action()
    except ShowrunnerRolePayloadError:
        return True
    return False


def _expect_transport_failure(action: Callable[[], Any]) -> bool:
    try:
        action()
    except ShowrunnerTransportHydrationError:
        return True
    return False


def main() -> int:
    raw, raw_hash = _raw_showrunner_payload()
    raw_snapshot = copy.deepcopy(raw)
    showrunner = role_spec("showrunner")
    results: list[dict[str, str]] = []

    hydrated = hydrate_showrunner_transport(raw, downstream_scene_writer_artifact_exists=False)
    results.append(
        {
            "id": "OWN-01",
            "result": "PASS" if hydrated.payload["scene_packages"] == ABSENT and hydrated.inserted_transport_fields == ("scene_packages",) else "FAIL",
            "detail": "transport-only missing field becomes the integration ABSENT sentinel",
        }
    )

    missing_canon = copy.deepcopy(raw)
    del missing_canon["canon_assignment_locks"]
    results.append(
        {
            "id": "OWN-02",
            "result": "PASS" if _expect_role_owned_failure(lambda: hydrate_showrunner_transport(missing_canon, downstream_scene_writer_artifact_exists=False)) else "FAIL",
            "detail": "missing role-owned Canon field remains a failure",
        }
    )

    missing_knowledge = copy.deepcopy(raw)
    del missing_knowledge["state_evidence"]["knowledge_timing"]
    results.append(
        {
            "id": "OWN-03",
            "result": "PASS" if _expect_role_owned_failure(lambda: hydrate_showrunner_transport(missing_knowledge, downstream_scene_writer_artifact_exists=False)) else "FAIL",
            "detail": "missing role-owned knowledge lock remains a failure",
        }
    )

    missing_assignment = copy.deepcopy(raw)
    del missing_assignment["required_outcome"]
    results.append(
        {
            "id": "OWN-04",
            "result": "PASS" if _expect_role_owned_failure(lambda: hydrate_showrunner_transport(missing_assignment, downstream_scene_writer_artifact_exists=False)) else "FAIL",
            "detail": "missing role-owned assignment field remains a failure",
        }
    )

    existing_downstream = copy.deepcopy(raw)
    existing_downstream["scene_packages"] = [{"scene_id": "E2E-FIX-01-S01"}]
    preserved = hydrate_showrunner_transport(existing_downstream, downstream_scene_writer_artifact_exists=False)
    downstream_guard = _expect_transport_failure(
        lambda: hydrate_showrunner_transport(raw, downstream_scene_writer_artifact_exists=True)
    )
    results.append(
        {
            "id": "OWN-05",
            "result": "PASS" if downstream_guard and preserved.payload["scene_packages"] == existing_downstream["scene_packages"] and not preserved.inserted_transport_fields else "FAIL",
            "detail": "adapter rejects absence after downstream existence and never overwrites an existing package",
        }
    )

    prose_only = copy.deepcopy(raw)
    del prose_only["canon_assignment_locks"]
    results.append(
        {
            "id": "OWN-06",
            "result": "PASS" if _expect_role_owned_failure(lambda: hydrate_showrunner_transport(prose_only, downstream_scene_writer_artifact_exists=False)) else "FAIL",
            "detail": "adapter cannot infer Canon locks from Showrunner prose",
        }
    )

    origins = hydrated.transport_field_origins
    results.append(
        {
            "id": "OWN-07",
            "result": "PASS" if origins == {"scene_packages": "INTEGRATION_TRANSPORT_ABSENCE_SENTINEL"} and ABSENT not in SHOWRUNNER_STATUS_TOKENS else "FAIL",
            "detail": "ABSENT is recorded as an integration sentinel, not a Showrunner canonical token",
        }
    )

    _, canonical_hash = canonical_skill(showrunner)
    raw_hash_after = hashlib.sha256(json.dumps(raw, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
    raw_snapshot_hash = hashlib.sha256(json.dumps(raw_snapshot, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
    results.append(
        {
            "id": "OWN-08",
            "result": "PASS" if canonical_hash == EXPECTED_HASHES["showrunner"] and raw == raw_snapshot and raw_hash_after == raw_snapshot_hash and raw_hash else "FAIL",
            "detail": "canonical Showrunner Skill and immutable recorded raw response remain unchanged",
        }
    )

    accepted = validate_role_output(showrunner, hydrated.payload, run_id="E2E-RUN-02")
    semantic_fields_preserved = all(accepted[field] == raw[field] for field in raw)
    results.append(
        {
            "id": "OWN-09",
            "result": "PASS" if accepted["scene_packages"] == ABSENT and semantic_fields_preserved else "FAIL",
            "detail": "Rerun02 raw Showrunner response passes full E2E schema after lawful hydration with every source field unchanged",
        }
    )

    envelope = make_envelope(showrunner, accepted, "Scene Writer", "Recorded regression", RERUN02_RAW, run_id="E2E-RUN-02")
    tokens_preserved = e2e_int_12_tokens_preserved(
        role_results={"showrunner": accepted},
        envelopes={"showrunner": envelope},
    )
    results.append(
        {
            "id": "OWN-10",
            "result": "PASS" if tokens_preserved else "FAIL",
            "detail": "E2E-INT-12 preserves canonical mode, primary state, flags, and handoffs exactly",
        }
    )

    passed = sum(item["result"] == "PASS" for item in results)
    print(
        json.dumps(
            {
                "classification": "SHOWRUNNER TRANSPORT OWNERSHIP TEST",
                "source_artifact": str(RERUN02_RAW),
                "source_raw_content_sha256": raw_hash,
                "results": results,
                "passed": passed,
                "total": len(results),
                "provider_calls": 0,
                "executor_calls": 0,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
