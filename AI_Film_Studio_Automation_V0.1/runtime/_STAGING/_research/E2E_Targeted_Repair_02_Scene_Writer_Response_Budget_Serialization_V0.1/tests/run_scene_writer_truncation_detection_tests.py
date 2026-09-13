"""Provider-free tests for explicit response-budget failure attribution."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in ROOT.parents if (parent / "studio.config.json").is_file())
if str(AUTOMATION_ROOT) not in sys.path:
    sys.path.insert(0, str(AUTOMATION_ROOT))

from runtime.shared_qa.model_executor import assess_response_truncation


def result(identifier: str, condition: bool, detail: str) -> dict[str, str]:
    return {"id": identifier, "result": "PASS" if condition else "FAIL", "detail": detail}


def run() -> int:
    provider_length = assess_response_truncation(raw_content="{\"x\": 1}", finish_reason="length", completion_tokens=5000, requested_max_tokens=5000)
    cap_and_incomplete = assess_response_truncation(raw_content="{\"x\":", finish_reason=None, completion_tokens=5000, requested_max_tokens=5000)
    malformed_not_cap = assess_response_truncation(raw_content="{\"x\":", finish_reason="stop", completion_tokens=4999, requested_max_tokens=5000)
    complete = assess_response_truncation(raw_content="{\"x\": 1}", finish_reason="stop", completion_tokens=400, requested_max_tokens=5000)
    results = [
        result("TRUNC-01", provider_length["truncated"] and "PROVIDER_FINISH_REASON_LENGTH" in provider_length["signals"], "provider finish reason length is classified TRUNCATED_RESPONSE"),
        result("TRUNC-02", cap_and_incomplete["truncated"] and {"COMPLETION_TOKEN_CAP_REACHED", "INCOMPLETE_JSON"}.issubset(cap_and_incomplete["signals"]), "cap contact plus incomplete JSON is classified TRUNCATED_RESPONSE"),
        result("TRUNC-03", not malformed_not_cap["truncated"], "malformed non-cap response remains executor failure, not semantic failure"),
        result("TRUNC-04", not complete["truncated"] and complete["json_complete"], "complete stopped JSON is not classified truncated"),
    ]
    payload = {"classification": "OFFLINE TRUNCATION DETECTION TEST", "results": results, "passed": sum(item["result"] == "PASS" for item in results), "total": len(results), "provider_calls": 0}
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["passed"] == payload["total"] else 1


if __name__ == "__main__":
    raise SystemExit(run())

