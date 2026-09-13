"""Durable provider-response evidence before Integration role validation.

This module is intentionally transport-only. It does not decide creative
quality, Canon, state semantics, or any role outcome.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Mapping


class ProviderResponsePersistenceError(RuntimeError):
    """Raised when provider evidence cannot be durably verified."""


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _read_json(path: Path) -> Dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ProviderResponsePersistenceError(f"Cannot read persisted evidence: {path.name}") from exc
    if not isinstance(value, dict):
        raise ProviderResponsePersistenceError(f"Persisted evidence is not an object: {path.name}")
    return value


def persist_provider_response(
    *,
    evidence_dir: Path,
    role: str,
    invocation_id: str,
    timestamp: str,
    raw_response: Mapping[str, Any],
    usage_record: Mapping[str, Any] | None,
    input_artifact: str,
) -> Dict[str, Any]:
    """Persist raw content and invocation metadata before any local validation."""

    raw_content = raw_response.get("raw_content")
    if not isinstance(raw_content, str):
        raise ProviderResponsePersistenceError("Raw provider content is unavailable for persistence")
    raw_sha256 = hashlib.sha256(raw_content.encode("utf-8")).hexdigest()
    artifact_prefix = role.lower().replace(" ", "_")
    raw_path = evidence_dir / "artifacts" / f"{artifact_prefix}_provider_response.json"
    metadata_path = evidence_dir / "artifacts" / f"{artifact_prefix}_invocation.json"
    verification_path = evidence_dir / "artifacts" / f"{artifact_prefix}_persistence_verification.json"
    raw_payload = {
        "lifecycle_stage": "RAW_RESPONSE_PERSISTED",
        "invocation_id": invocation_id,
        "role": role,
        "provider": raw_response.get("provider"),
        "model": raw_response.get("model"),
        "provider_invocation_id": raw_response.get("provider_invocation_id"),
        "finish_reason": raw_response.get("finish_reason"),
        "requested_max_tokens": raw_response.get("requested_max_tokens"),
        "http_status": raw_response.get("http_status"),
        "trace_headers": copy.deepcopy(raw_response.get("trace_headers")),
        "raw_content": raw_content,
        "raw_content_sha256": raw_sha256,
        "assistant_content": raw_response.get("assistant_content"),
        "tool_calls": copy.deepcopy(raw_response.get("tool_calls")),
        "raw_provider_response": raw_response.get("raw_provider_response"),
        "structured_output": copy.deepcopy(raw_response.get("structured_output")),
    }
    metadata_payload = {
        "lifecycle_stage": "USAGE_AND_INVOCATION_METADATA_PERSISTED",
        "invocation_id": invocation_id,
        "role": role,
        "timestamp": timestamp,
        "input_artifact": input_artifact,
        "provider": raw_response.get("provider"),
        "model": raw_response.get("model"),
        "provider_invocation_id": raw_response.get("provider_invocation_id"),
        "finish_reason": raw_response.get("finish_reason"),
        "requested_max_tokens": raw_response.get("requested_max_tokens"),
        "http_status": raw_response.get("http_status"),
        "trace_headers": copy.deepcopy(raw_response.get("trace_headers")),
        "usage": copy.deepcopy(dict(usage_record)) if isinstance(usage_record, Mapping) else None,
    }
    _write_json(raw_path, raw_payload)
    _write_json(metadata_path, metadata_payload)
    persisted_raw = _read_json(raw_path)
    persisted_metadata = _read_json(metadata_path)
    verified = (
        persisted_raw.get("invocation_id") == invocation_id
        and persisted_raw.get("role") == role
        and persisted_raw.get("raw_content_sha256") == raw_sha256
        and persisted_metadata.get("invocation_id") == invocation_id
        and persisted_metadata.get("role") == role
        and persisted_metadata.get("input_artifact") == input_artifact
    )
    verification_payload = {
        "lifecycle_stage": "PERSISTENCE_VERIFIED",
        "invocation_id": invocation_id,
        "role": role,
        "verified": verified,
        "raw_response_artifact": str(raw_path),
        "invocation_metadata_artifact": str(metadata_path),
    }
    _write_json(verification_path, verification_payload)
    if not verified:
        raise ProviderResponsePersistenceError("Provider response persistence verification failed")
    return {
        "raw_response_artifact": str(raw_path),
        "invocation_metadata_artifact": str(metadata_path),
        "persistence_verification_artifact": str(verification_path),
        "raw_content_sha256": raw_sha256,
    }


def persist_validation_error(
    *,
    evidence_dir: Path,
    role: str,
    invocation_id: str,
    validation_stage: str,
    category: str,
    detail: str,
) -> str:
    """Persist validation failure separately without changing raw response evidence."""

    artifact_prefix = role.lower().replace(" ", "_")
    path = evidence_dir / "artifacts" / f"{artifact_prefix}_validation_error.json"
    _write_json(
        path,
        {
            "lifecycle_stage": "LOCAL_VALIDATION_FAILURE_RECORDED",
            "invocation_id": invocation_id,
            "role": role,
            "validation_stage": validation_stage,
            "category": category,
            "detail": detail,
        },
    )
    return str(path)
