"""SMOKE-EXEC-01: F01 through the formal Runtime and real registered executor."""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.shared_qa.language_voice_qa_binding import create_language_voice_qa_binding


FIXTURE = ROOT / "runtime" / "_TEST_SANDBOX" / "validation" / "fixtures" / "shared_qa" / "v0.1" / "F01_clean_passage.md"
OUTPUT = ROOT / "runtime" / "_TEST_SANDBOX" / "validation" / "results" / "shared_qa" / "v0.1" / "executor_binding_smoke.json"


def main() -> int:
    raw = FIXTURE.read_text(encoding="utf-8")
    text = raw.split("## Text\n", 1)[1].split("\n## Runtime Context\n", 1)[0].strip()
    context = raw.split("\n## Runtime Context\n", 1)[1].strip()
    mode = re.search(r"Requested Mode:\s*`([^`]+)`", context).group(1)
    register_match = re.search(r"Register:\s*([^\n]+)", context)
    register = re.search(r"R[1-8]", register_match.group(1)).group(0) if register_match else None
    bundle = create_language_voice_qa_binding(log_dir=OUTPUT.parent / "runtime_audit_logs" / "SMOKE-EXEC-01")
    result = bundle.runtime.invoke({
        "original": text,
        "requested_mode": mode,
        "register": register,
        "available_context": context,
        "caller": "VALIDATION / SYNTHETIC / NON-CANON / fixture F01",
        "invocation_id": "smoke-exec-01",
    })
    internal = result["internal_runtime_result"]
    usage = bundle.executor.usage_for("smoke-exec-01")
    estimate = bundle.provider.estimate_cost_cny(usage["usage"]) if usage else None
    passed = (
        internal["runtime_status"] == "SUCCESS"
        and internal["failure_code"] is None
        and internal["skill_integrity"]["passed"]
        and isinstance(bundle.executor.output_for("smoke-exec-01"), dict)
        and result["downstream_payload"]["text"] == text
        and usage is not None
    )
    record = {
        "id": "SMOKE-EXEC-01",
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "fixture_id": "F01",
        "provider": usage["provider"] if usage else None,
        "model": usage["model"] if usage else None,
        "thinking_mode": usage["thinking_mode"] if usage else None,
        "runtime_status": internal["runtime_status"],
        "failure_code": internal["failure_code"],
        "canonical_semantic_output": bundle.executor.output_for("smoke-exec-01"),
        "usage": usage,
        "estimated_cost_cny": estimate,
        "cost_status": "ESTIMATED" if estimate is not None else "NOT_AVAILABLE",
        "original_preserved": result["downstream_payload"]["text"] == text,
        "passed": passed,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "id": record["id"], "passed": passed, "provider": record["provider"], "model": record["model"],
        "runtime_status": record["runtime_status"], "failure_code": record["failure_code"],
        "original_preserved": record["original_preserved"], "estimated_cost_cny": estimate,
    }, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
