"""Run only the authorized C02 repair revalidation through the real executor."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.revalidate_shared_qa_with_executor import FIXTURE_ROOT, execute_fixture, parse_fixture


def main() -> int:
    fixture = parse_fixture(FIXTURE_ROOT / "C02_ambiguous_contemporary.md")
    result = execute_fixture(fixture)
    target = ROOT / "runtime" / "_TEST_SANDBOX" / "validation" / "results" / "shared_qa" / "v0.1" / "executor_revalidation" / "C02_repair_run.json"
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    coordinator = result.get("coordinator", {})
    final = result.get("final") or {}
    internal = final.get("runtime_result", {}).get("internal_runtime_result", {})
    passed = coordinator.get("coordinator_status") == "EVIDENCE_RETURNED_TO_QA" and internal.get("runtime_status") == "SUCCESS"
    print(json.dumps({"fixture": "C02", "passed": passed, "coordinator": coordinator.get("coordinator_status"), "final_decision": internal.get("decision"), "failure_code": internal.get("failure_code")}, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

