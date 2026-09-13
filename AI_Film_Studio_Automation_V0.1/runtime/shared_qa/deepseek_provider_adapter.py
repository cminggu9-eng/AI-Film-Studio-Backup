"""Minimal DeepSeek adapter for the provider-neutral model executor.

Only this adapter knows DeepSeek's endpoint, model name, credential variable,
thinking parameter, and pricing basis.  It never writes or logs credentials.
"""

from __future__ import annotations

import json
import os
import time
from typing import Any, Dict, Mapping
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from runtime.shared_qa.model_executor import ModelExecutionError, ModelRequest, ModelResponse, ProviderHTTPError


class DeepSeekProviderAdapter:
    provider = "deepseek"
    model = "deepseek-v4-pro"
    base_url = "https://api.deepseek.com"
    strict_beta_base_url = "https://api.deepseek.com/beta"
    thinking_mode = "disabled"
    retry_policy = "NO_AUTOMATIC_RETRY"
    provider_documented_max_output_tokens = 384000
    trace_header_names = ("x-ds-trace-id", "x-request-id", "request-id", "traceparent", "x-amzn-trace-id")

    # Official DeepSeek V4 Pro pricing, CNY per 1M tokens, read 2026-08-24.
    _INPUT_CACHE_HIT_CNY_PER_M = 0.025
    _INPUT_CACHE_MISS_CNY_PER_M = 3.0
    _OUTPUT_CNY_PER_M = 6.0

    def __init__(self, *, timeout_seconds: int = 90) -> None:
        key = os.environ.get("DEEPSEEK_API_KEY")
        if not isinstance(key, str) or not key.strip():
            raise ModelExecutionError("DEEPSEEK_API_KEY is not available")
        self._api_key = key
        self.timeout_seconds = timeout_seconds

    @staticmethod
    def _integer(value: Any) -> int | None:
        return value if isinstance(value, int) and value >= 0 else None

    @classmethod
    def _trace_headers(cls, headers: Mapping[str, Any]) -> Dict[str, str]:
        normalized = {str(key).casefold(): str(value) for key, value in headers.items() if str(key).casefold() not in {"set-cookie", "authorization", "cookie"}}
        return {name: normalized.get(name, "ABSENT") for name in cls.trace_header_names}

    @classmethod
    def estimate_cost_cny(cls, usage: Mapping[str, Any]) -> float | None:
        prompt_tokens = cls._integer(usage.get("prompt_tokens"))
        completion_tokens = cls._integer(usage.get("completion_tokens"))
        if prompt_tokens is None or completion_tokens is None:
            return None
        cache_hit = cls._integer(usage.get("prompt_cache_hit_tokens")) or 0
        cache_miss = cls._integer(usage.get("prompt_cache_miss_tokens"))
        if cache_miss is None:
            cache_miss = max(prompt_tokens - cache_hit, 0)
        return round(
            (cache_hit * cls._INPUT_CACHE_HIT_CNY_PER_M
             + cache_miss * cls._INPUT_CACHE_MISS_CNY_PER_M
             + completion_tokens * cls._OUTPUT_CNY_PER_M) / 1_000_000,
            8,
        )

    @classmethod
    def pricing_basis(cls) -> Dict[str, Any]:
        return {
            "currency": "CNY",
            "unit": "per_1M_tokens",
            "input_cache_hit": cls._INPUT_CACHE_HIT_CNY_PER_M,
            "input_cache_miss": cls._INPUT_CACHE_MISS_CNY_PER_M,
            "output": cls._OUTPUT_CNY_PER_M,
            "status": "ESTIMATED",
        }

    @classmethod
    def completion_capabilities(cls) -> Dict[str, Any]:
        """Current approved-model output capability recorded for bounded callers."""

        return {
            "provider": cls.provider,
            "model": cls.model,
            "provider_documented_max_output_tokens": cls.provider_documented_max_output_tokens,
            "source": "DeepSeek API Docs / Models & Pricing, checked 2026-08-28",
            "adapter_enforced_ceiling": None,
            "request_parameter": "max_tokens",
        }

    @classmethod
    def build_provider_payload(cls, request: ModelRequest) -> tuple[Dict[str, Any], str]:
        """Provider-neutral request projection, safe to inspect without credentials/network."""
        if request.model != cls.model:
            raise ModelExecutionError("DeepSeek adapter rejected an unapproved model")
        if request.thinking_mode != cls.thinking_mode:
            raise ModelExecutionError("DeepSeek adapter rejected an unapproved thinking mode")
        strict_contract = request.structured_output
        if strict_contract is None and request.response_format != "json_object":
            raise ModelExecutionError("DeepSeek adapter requires JSON output for the standard response path")
        if strict_contract is not None and request.response_format is not None:
            raise ModelExecutionError("Strict structured transport cannot send a parallel response_format route")
        payload: Dict[str, Any] = {"model": cls.model, "messages": [{"role": "system", "content": request.system_prompt}, {"role": "user", "content": request.user_prompt}], "thinking": {"type": cls.thinking_mode}, "max_tokens": request.max_tokens, "stream": False}
        endpoint_base_url = cls.base_url
        if strict_contract is None:
            payload["response_format"] = {"type": "json_object"}
        else:
            if not isinstance(strict_contract.function_name, str) or not strict_contract.function_name.strip() or not isinstance(strict_contract.function_description, str) or not strict_contract.function_description.strip() or not isinstance(strict_contract.parameters_schema, Mapping):
                raise ModelExecutionError("Strict structured transport contract is invalid")
            payload["tools"] = [{"type": "function", "function": {"name": strict_contract.function_name, "description": strict_contract.function_description, "parameters": dict(strict_contract.parameters_schema), "strict": True}}]
            payload["tool_choice"] = {"type": "function", "function": {"name": strict_contract.function_name}}
            endpoint_base_url = cls.strict_beta_base_url
        return payload, endpoint_base_url

    def complete(self, request: ModelRequest) -> ModelResponse:
        if request.model != self.model:
            raise ModelExecutionError("DeepSeek adapter rejected an unapproved model")
        if request.thinking_mode != self.thinking_mode:
            raise ModelExecutionError("DeepSeek adapter rejected an unapproved thinking mode")
        # Response interpretation follows the same explicit contract branch as
        # payload construction; non-structured roles intentionally carry None.
        strict_contract = request.structured_output
        payload, endpoint_base_url = self.build_provider_payload(request)
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        http_request = Request(
            f"{endpoint_base_url}/chat/completions",
            data=body,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._api_key}",
            },
            method="POST",
        )
        started = time.perf_counter()
        try:
            with urlopen(http_request, timeout=self.timeout_seconds) as response:
                raw = response.read()
                http_status = getattr(response, "status", None)
                if not isinstance(http_status, int):
                    http_status = response.getcode()
                trace_headers = self._trace_headers(response.headers)
        except HTTPError as exc:
            try:
                body = exc.read().decode("utf-8", errors="replace")
            except OSError:
                body = ""
            headers = self._trace_headers(exc.headers)
            raise ProviderHTTPError(status=exc.code, body=body, headers=headers, endpoint=f"{endpoint_base_url}/chat/completions") from exc
        except (URLError, TimeoutError, OSError) as exc:
            raise ModelExecutionError(f"DeepSeek API transport failure: {type(exc).__name__}") from exc
        latency_ms = int((time.perf_counter() - started) * 1000)
        try:
            raw_text = raw.decode("utf-8")
            decoded = json.loads(raw_text)
            choice = decoded["choices"][0]
            message = choice["message"]
            content = message.get("content")
        except (UnicodeDecodeError, ValueError, KeyError, IndexError, TypeError) as exc:
            raise ModelExecutionError("DeepSeek API response shape was invalid") from exc
        if content is None:
            content = ""
        if not isinstance(content, str):
            raise ModelExecutionError("DeepSeek API response content was invalid")
        raw_tool_calls = message.get("tool_calls") if isinstance(message, Mapping) else None
        if raw_tool_calls is None:
            raw_tool_calls = []
        if not isinstance(raw_tool_calls, list) or not all(isinstance(item, Mapping) for item in raw_tool_calls):
            raise ModelExecutionError("DeepSeek API response tool calls were invalid")
        if strict_contract is None and not content.strip():
            raise ModelExecutionError("DeepSeek API returned no final structured content")
        if decoded.get("model") != self.model:
            raise ModelExecutionError("DeepSeek API response model did not match deepseek-v4-pro")

        usage_raw = decoded.get("usage", {}) if isinstance(decoded, Mapping) else {}
        usage = {
            "prompt_tokens": self._integer(usage_raw.get("prompt_tokens")) if isinstance(usage_raw, Mapping) else None,
            "completion_tokens": self._integer(usage_raw.get("completion_tokens")) if isinstance(usage_raw, Mapping) else None,
            "total_tokens": self._integer(usage_raw.get("total_tokens")) if isinstance(usage_raw, Mapping) else None,
            "prompt_cache_hit_tokens": self._integer(usage_raw.get("prompt_cache_hit_tokens")) if isinstance(usage_raw, Mapping) else None,
            "prompt_cache_miss_tokens": self._integer(usage_raw.get("prompt_cache_miss_tokens")) if isinstance(usage_raw, Mapping) else None,
        }
        return ModelResponse(
            content=content,
            provider=self.provider,
            model=str(decoded.get("model", self.model)),
            provider_invocation_id=str(decoded.get("id")) if decoded.get("id") is not None else None,
            usage=usage,
            latency_ms=latency_ms,
            thinking_mode=self.thinking_mode,
            finish_reason=str(choice.get("finish_reason")) if choice.get("finish_reason") is not None else None,
            tool_calls=tuple(dict(item) for item in raw_tool_calls),
            raw_provider_response=raw_text,
            http_status=http_status,
            trace_headers=trace_headers,
        )
