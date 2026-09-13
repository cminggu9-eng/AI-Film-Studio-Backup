"""Provider-neutral transport for canonical Skill model execution.

This module deliberately has no Language & Voice QA decision rules.  It builds
one provider-neutral request, transports it through an adapter, parses JSON,
and retains safe usage metadata for the enclosing audit.
"""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from typing import Any, Dict, Mapping, Protocol


class ModelExecutionError(RuntimeError):
    """A provider or structured-output failure safe for Runtime F3 handling."""


class ProviderHTTPError(ModelExecutionError):
    """HTTP failure with safe-to-persist response observability fields."""
    def __init__(self, *, status: int, body: str, headers: Mapping[str, Any], endpoint: str) -> None:
        super().__init__(f"Provider HTTP failure: {status}")
        self.status, self.body, self.headers, self.endpoint = status, body, dict(headers), endpoint


def assess_response_truncation(
    *,
    raw_content: str,
    finish_reason: str | None,
    completion_tokens: int | None,
    requested_max_tokens: int,
) -> Dict[str, Any]:
    """Classify serialization truncation without repairing or extending content."""

    json_complete = False
    if isinstance(raw_content, str) and raw_content.strip():
        try:
            json.loads(raw_content)
            json_complete = True
        except json.JSONDecodeError:
            json_complete = False
    cap_contact = isinstance(completion_tokens, int) and completion_tokens == requested_max_tokens
    provider_length = finish_reason == "length"
    truncated = provider_length or (not json_complete and cap_contact)
    signals = []
    if provider_length:
        signals.append("PROVIDER_FINISH_REASON_LENGTH")
    if cap_contact:
        signals.append("COMPLETION_TOKEN_CAP_REACHED")
    if not json_complete:
        signals.append("INCOMPLETE_JSON")
    return {
        "classification": "TRUNCATED_RESPONSE" if truncated else "NOT_TRUNCATED",
        "truncated": truncated,
        "finish_reason": finish_reason,
        "completion_tokens": completion_tokens,
        "requested_max_tokens": requested_max_tokens,
        "json_complete": json_complete,
        "signals": signals,
    }


@dataclass(frozen=True)
class StructuredOutputContract:
    """Provider-neutral request for one forced structured response function.

    This is a transport contract only. Provider adapters map it to their own
    function/tool API syntax; it contains no role-specific creative rules.
    """

    function_name: str
    function_description: str
    parameters_schema: Mapping[str, Any]


@dataclass(frozen=True)
class ModelRequest:
    system_prompt: str
    user_prompt: str
    model: str
    thinking_mode: str
    max_tokens: int
    response_format: str | None = "json_object"
    structured_output: StructuredOutputContract | None = None


@dataclass(frozen=True)
class ModelResponse:
    content: str
    provider: str
    model: str
    provider_invocation_id: str | None
    usage: Dict[str, int | None]
    latency_ms: int
    thinking_mode: str
    finish_reason: str | None = None
    tool_calls: tuple[Mapping[str, Any], ...] = ()
    raw_provider_response: str | None = None
    http_status: int | None = None
    trace_headers: Dict[str, str] | None = None


@dataclass(frozen=True)
class ModelExecutionReceipt:
    """Provider response material retained before role-local validation."""

    parsed: Dict[str, Any] | None
    raw_content: str
    assistant_content: str
    tool_calls: tuple[Mapping[str, Any], ...]
    raw_provider_response: str | None
    provider: str
    model: str
    provider_invocation_id: str | None
    usage: Dict[str, int | None]
    latency_ms: int
    thinking_mode: str
    finish_reason: str | None


class ProviderAdapter(Protocol):
    def complete(self, request: ModelRequest) -> ModelResponse:
        """Return the provider response for a neutral model request."""


class ModelExecutor:
    """Parse provider JSON without adding a second QA decision layer."""

    def __init__(self, provider: ProviderAdapter) -> None:
        self.provider = provider
        self._usage_by_invocation: Dict[str, Dict[str, Any]] = {}
        self._response_by_invocation: Dict[str, Dict[str, Any]] = {}

    def execute(self, request: ModelRequest, *, invocation_id: str, fixture_id: str | None = None) -> Dict[str, Any]:
        """Backwards-compatible parsed-output execution path."""

        receipt = self.execute_with_receipt(request, invocation_id=invocation_id, fixture_id=fixture_id)
        if receipt.parsed is None:
            raise ModelExecutionError("Structured function responses require durable transport validation")
        return receipt.parsed

    def execute_with_receipt(
        self,
        request: ModelRequest,
        *,
        invocation_id: str,
        fixture_id: str | None = None,
    ) -> ModelExecutionReceipt:
        """Receive and retain raw/usage material before local role validation.

        The enclosing Integration Harness owns durable evidence persistence. This
        method retains an exact response envelope so that even a later JSON or
        role-contract failure cannot erase provider response/usage evidence.
        """

        response = self.provider.complete(request)
        assistant_content = response.content if isinstance(response.content, str) else ""
        raw_content = (
            response.raw_provider_response
            if request.structured_output is not None and isinstance(response.raw_provider_response, str)
            else assistant_content
        )
        tool_calls = tuple(copy.deepcopy(dict(item)) for item in response.tool_calls if isinstance(item, Mapping))
        usage_record = {
            "provider": response.provider,
            "model": response.model,
            "provider_invocation_id": response.provider_invocation_id,
            "usage": copy.deepcopy(response.usage),
            "latency_ms": response.latency_ms,
            "thinking_mode": response.thinking_mode,
            "fixture_id": fixture_id,
            "request_success": True,
            "requested_max_tokens": request.max_tokens,
            "finish_reason": response.finish_reason,
            "http_status": response.http_status,
            "trace_headers": copy.deepcopy(response.trace_headers),
            "structured_output": {
                "function_name": request.structured_output.function_name,
                "transport": "forced_function",
            } if request.structured_output is not None else None,
        }
        self._usage_by_invocation[invocation_id] = copy.deepcopy(usage_record)
        self._response_by_invocation[invocation_id] = {
            "raw_content": raw_content,
            "assistant_content": assistant_content,
            "tool_calls": copy.deepcopy(list(tool_calls)),
            "raw_provider_response": response.raw_provider_response,
            "provider": response.provider,
            "model": response.model,
            "provider_invocation_id": response.provider_invocation_id,
            "usage": copy.deepcopy(response.usage),
            "latency_ms": response.latency_ms,
            "thinking_mode": response.thinking_mode,
            "fixture_id": fixture_id,
            "request_success": True,
            "requested_max_tokens": request.max_tokens,
            "finish_reason": response.finish_reason,
            "http_status": response.http_status,
            "trace_headers": copy.deepcopy(response.trace_headers),
            "structured_output": {
                "function_name": request.structured_output.function_name,
                "transport": "forced_function",
            } if request.structured_output is not None else None,
        }
        if request.structured_output is not None:
            return ModelExecutionReceipt(
                parsed=None,
                raw_content=raw_content,
                assistant_content=assistant_content,
                tool_calls=tool_calls,
                raw_provider_response=response.raw_provider_response,
                provider=response.provider,
                model=response.model,
                provider_invocation_id=response.provider_invocation_id,
                usage=copy.deepcopy(response.usage),
                latency_ms=response.latency_ms,
                thinking_mode=response.thinking_mode,
                finish_reason=response.finish_reason,
            )
        if not isinstance(response.content, str) or not response.content.strip():
            raise ModelExecutionError("Provider returned empty structured content")
        try:
            parsed = json.loads(response.content)
        except json.JSONDecodeError as exc:
            raise ModelExecutionError("Provider response was not valid JSON") from exc
        if not isinstance(parsed, Mapping):
            raise ModelExecutionError("Provider JSON result must be an object")
        return ModelExecutionReceipt(
            parsed=copy.deepcopy(dict(parsed)),
            raw_content=raw_content,
            assistant_content=assistant_content,
            tool_calls=tool_calls,
            raw_provider_response=response.raw_provider_response,
            provider=response.provider,
            model=response.model,
            provider_invocation_id=response.provider_invocation_id,
            usage=copy.deepcopy(response.usage),
            latency_ms=response.latency_ms,
            thinking_mode=response.thinking_mode,
            finish_reason=response.finish_reason,
        )

    @staticmethod
    def extract_required_tool_arguments(
        receipt: ModelExecutionReceipt,
        *,
        function_name: str,
    ) -> Dict[str, Any]:
        """Parse one forced function argument string without any repair path."""

        if receipt.assistant_content.strip():
            raise ModelExecutionError("Ordinary assistant prose cannot replace the required structured function call")
        if len(receipt.tool_calls) != 1:
            raise ModelExecutionError("Exactly one required structured function call was not received")
        tool_call = receipt.tool_calls[0]
        if tool_call.get("type") != "function":
            raise ModelExecutionError("Required structured call is not a function call")
        function = tool_call.get("function")
        if not isinstance(function, Mapping) or function.get("name") != function_name:
            raise ModelExecutionError("Required structured function name was not received")
        arguments = function.get("arguments")
        if not isinstance(arguments, str) or not arguments.strip():
            raise ModelExecutionError("Required structured function arguments are unavailable")
        try:
            parsed = json.loads(arguments)
        except json.JSONDecodeError as exc:
            raise ModelExecutionError("Required structured function arguments were not valid JSON") from exc
        if not isinstance(parsed, Mapping):
            raise ModelExecutionError("Required structured function arguments must be a JSON object")
        return copy.deepcopy(dict(parsed))

    def usage_for(self, invocation_id: str) -> Dict[str, Any] | None:
        data = self._usage_by_invocation.get(invocation_id)
        return copy.deepcopy(data) if data is not None else None

    def response_for(self, invocation_id: str) -> Dict[str, Any] | None:
        """Return the unmodified provider envelope retained for evidence persistence."""

        data = self._response_by_invocation.get(invocation_id)
        return copy.deepcopy(data) if data is not None else None
