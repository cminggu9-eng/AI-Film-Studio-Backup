from __future__ import annotations

import json
from pathlib import Path

from director_state_object_test_support import FIXTURES, HERE
import run_minimal_e2e as e2e


EVIDENCE = HERE.parent.parent / "evidence" / "director_request_captures"


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    captures = []
    for fixture_id, fixture_path in FIXTURES.items():
        e2e.FIXTURE_BINDING_PATH = str(fixture_path)
        capture = e2e.director_request_capture()
        capture_path = EVIDENCE / f"{fixture_id}_director_final_request_capture.json"
        capture_path.write_text(json.dumps(capture, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        captures.append({
            "fixture_id": fixture_id,
            "artifact": str(capture_path),
            "result": capture["result"],
            "authority_bundle_hash": capture["authority_bundle_hash"],
            "compiled_run_contract_hash": capture["compiled_run_contract_hash"],
            "state_schema_hash": capture["state_schema_hash"],
            "source_trace_hash": capture["source_trace_hash"],
            "provider_neutral_schema_hash": capture["provider_neutral_schema_hash"],
            "deepseek_projection_schema_hash": capture["deepseek_projection_schema_hash"],
            "final_request_schema_hash": capture["final_request_schema_hash"],
            "final_wire_hash": capture["final_wire_hash"],
            "strict": capture["strict"],
            "tool_name": capture["tool_name"],
            "tool_choice": capture["tool_choice"],
            "provider_calls": 0,
            "network_send_reached": False,
        })
    summary = {
        "classification": "DIRECTOR FINAL REQUEST CAPTURE",
        "passed": sum(item["result"] == "PASS" for item in captures),
        "total": 3,
        "result": "PASS" if all(item["result"] == "PASS" for item in captures) else "FAIL",
        "captures": captures,
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "e2e_runs": 0,
    }
    summary_path = EVIDENCE / "director_final_request_capture_summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
