"""Authorized F08-only real rerun after Rewrite Output Consistency Gate repair."""

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
    fixture = parse_fixture(FIXTURE_ROOT / "F08_full_passage.md")
    result = execute_fixture(fixture)
    target = ROOT / "runtime" / "_TEST_SANDBOX" / "validation" / "results" / "shared_qa" / "v0.1" / "executor_revalidation" / "F08_rewrite_consistency_repair_run.json"
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    final = result["final"]
    internal = final["runtime_result"]["internal_runtime_result"]
    output = final["canonical_semantic_output"] or {}
    changed = output.get("revised_text") != fixture["text"] if output.get("decision") == "REWRITE DELIVERED" else None
    passed = internal["runtime_status"] == "SUCCESS" and (output.get("decision") != "REWRITE DELIVERED" or changed is True)
    print(json.dumps({"fixture":"F08","passed":passed,"decision":output.get("decision"),"rewrite_changed":changed,"runtime_status":internal.get("runtime_status"),"failure_code":internal.get("failure_code"),"estimated_cost_cny":final.get("estimated_cost_cny")}, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

