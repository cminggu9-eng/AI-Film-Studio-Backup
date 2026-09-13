"""Minimal real DeepSeek availability check; no fixture or semantic QA is sent."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.shared_qa.deepseek_provider_adapter import DeepSeekProviderAdapter
from runtime.shared_qa.model_executor import ModelRequest


def main() -> int:
    adapter = DeepSeekProviderAdapter()
    response = adapter.complete(ModelRequest(
        system_prompt="Return a valid JSON object. Do not include explanation.",
        user_prompt='Return exactly this JSON object: {"status":"ok"}.',
        model="deepseek-v4-pro",
        thinking_mode="disabled",
        max_tokens=32,
    ))
    usage_present = all(response.usage.get(field) is not None for field in ("prompt_tokens", "completion_tokens", "total_tokens"))
    passed = response.provider == "deepseek" and response.model == "deepseek-v4-pro" and usage_present
    print(json.dumps({
        "provider": response.provider,
        "model": response.model,
        "thinking_mode": response.thinking_mode,
        "usage_metadata_available": usage_present,
        "latency_ms": response.latency_ms,
        "passed": passed,
    }, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

