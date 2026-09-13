"""Provider-free runtime reliability contracts for the Minimal E2E harness.

These checks own run identity, evidence custody, and lifecycle coherence.  They
do not parse, create, translate, or repair role semantics.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Mapping, Sequence


class RuntimeReliabilityContractError(RuntimeError):
    """Raised when runtime metadata or evidence custody is inconsistent."""


# Lifecycle metadata authorizes only these exact strict transport identities.
# This registry deliberately owns no provider endpoint, schema, or role semantics.
STRICT_TRANSPORT_AUTHORIZATION_REGISTRY: dict[str, str] = {
    "Scene Writer": "submit_scene_writer_package",
    "Director": "submit_director_package",
}


def _inside(root: Path, candidate: Path) -> bool:
    try:
        candidate.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def validate_execution_boundary(*, run_id: str, evidence_root: Path, stage: Path, authorization_label: str) -> dict[str, Any]:
    """Reject ambiguous future-run identity, custody roots, and authorization."""

    if not re.fullmatch(r"E2E-RUN-\d{2}", run_id):
        raise RuntimeReliabilityContractError("I METADATA / EVIDENCE-ROOT HYGIENE: non-canonical Run ID")
    normalized_root = evidence_root.resolve()
    expected_root = (stage / "evidence" / run_id).resolve()
    if normalized_root != expected_root:
        raise RuntimeReliabilityContractError("I METADATA / EVIDENCE-ROOT HYGIENE: evidence root must equal the run-local canonical path")
    if not authorization_label.strip():
        raise RuntimeReliabilityContractError("I METADATA / EVIDENCE-ROOT HYGIENE: execution authorization label is required")
    return {
        "classification": "RUNTIME EXECUTION BOUNDARY",
        "canonical_run_id": run_id,
        "absolute_evidence_root": str(normalized_root),
        "evidence_root_policy": "SINGLE_CANONICAL_PATH_NO_STAGE_RENESTING",
        "authorization_label_present": True,
        "provider_calls": 0,
        "executor_calls": 0,
        "result": "PASS",
    }


def validate_lifecycle_consistency(
    *,
    manifest: Mapping[str, Any],
    provider_manifest: Mapping[str, Any],
    handoffs: Sequence[Mapping[str, Any]],
    ledger: Mapping[str, Any],
    evidence_root: Path,
    require_complete_chain: bool,
) -> dict[str, Any]:
    """Validate only recorded metadata linkage; never infer role content."""

    root = evidence_root.resolve()
    run_id = manifest.get("canonical_run_id") or manifest.get("run_id")
    failures: list[str] = []
    if not isinstance(run_id, str) or not re.fullmatch(r"E2E-RUN-\d{2}", run_id):
        failures.append("run_id is absent or non-canonical")
    if manifest.get("canonical_run_id") != manifest.get("run_id"):
        failures.append("canonical_run_id does not equal run_id")
    if manifest.get("absolute_evidence_root") != str(root):
        failures.append("manifest evidence root is not the normalized runtime root")
    if manifest.get("evidence_root_policy") != "SINGLE_CANONICAL_PATH_NO_STAGE_RENESTING":
        failures.append("evidence root policy is missing or changed")

    calls = provider_manifest.get("calls")
    if not isinstance(calls, list):
        failures.append("provider calls are not a list")
        calls = []
    manifest_count = manifest.get("provider_call_count")
    provider_count = provider_manifest.get("call_count")
    if manifest_count != provider_count or provider_count != len(calls):
        failures.append("provider call counts disagree")
    if manifest.get("retry_count") != 0 or manifest.get("automatic_provider_fallback") != 0:
        failures.append("manifest records retry or provider fallback")
    integrity = manifest.get("integrity")
    if isinstance(integrity, Mapping) and (integrity.get("automatic_retry") != 0 or integrity.get("provider_fallback") != 0):
        failures.append("manifest integrity records retry or provider fallback")
    if provider_manifest.get("retry_count") != 0 or provider_manifest.get("automatic_fallback") != 0:
        failures.append("provider manifest records retry or provider fallback")

    invocation_ids: set[str] = set()
    for call in calls:
        if not isinstance(call, Mapping):
            failures.append("provider call is not an object")
            continue
        invocation_id = call.get("invocation_id")
        if not isinstance(invocation_id, str) or not isinstance(run_id, str) or not invocation_id.startswith(f"{run_id}:"):
            failures.append("invocation ID is absent or belongs to another run")
        elif invocation_id in invocation_ids:
            failures.append("invocation ID is duplicated")
        else:
            invocation_ids.add(invocation_id)
        for field in ("input_artifact", "output_artifact", "raw_response_artifact", "invocation_metadata_artifact", "persistence_verification_artifact"):
            artifact = call.get(field)
            if not isinstance(artifact, str) or not _inside(root, Path(artifact)):
                failures.append(f"{field} is missing or outside evidence root")
        if call.get("persistence_verified") is not True:
            failures.append("raw provider persistence is not verified")
        if call.get("retry_count") != 0 or call.get("transport_auto_repairs") != 0:
            failures.append("silent retry or transport auto-repair detected")

    strict_calls: list[Mapping[str, Any]] = []
    strict_authorizations: list[dict[str, Any]] = []
    for call in calls:
        if not isinstance(call, Mapping):
            continue
        role = call.get("role")
        transport = call.get("structured_transport")
        if not isinstance(transport, Mapping):
            failures.append("structured transport metadata is unavailable")
            continue
        function_name = transport.get("function_name")
        strict_enabled = transport.get("enabled") is True
        expected_function = STRICT_TRANSPORT_AUTHORIZATION_REGISTRY.get(role) if isinstance(role, str) else None
        if strict_enabled:
            strict_calls.append(call)
            tool_choice_function = transport.get("tool_choice_function_name", function_name)
            authorized = expected_function == function_name
            strict_authorizations.append({
                "role": role,
                "function_name": function_name,
                "authorized": authorized,
                "strict": True,
                "tool_choice_function_name": tool_choice_function,
            })
            if not authorized:
                failures.append("strict transport role/function pair is not explicitly authorized")
            if tool_choice_function != function_name:
                failures.append("strict transport tool_choice does not match the declared function")
            if transport.get("beta_provider_feature_used") is not True:
                failures.append("strict transport is not adapter-scoped")
            if transport.get("required_tool_call_verified") is not True:
                failures.append("strict transport did not verify the exact required tool call")
            if transport.get("arguments_parsed") is not True or transport.get("schema_validated") is not True:
                failures.append("strict transport did not complete argument/schema validation")
        elif expected_function is not None and expected_function == function_name:
            failures.append("authorized strict transport pair is missing strict:true")

    if ledger.get("run_id") != run_id or ledger.get("append_only") is not True:
        failures.append("ledger is not run-local append-only evidence")
    entries = ledger.get("entries")
    if not isinstance(entries, list):
        failures.append("ledger entries are not a list")
        entries = []
    if require_complete_chain and len(entries) != 3:
        failures.append("Golden lifecycle requires three ledger entries")

    if require_complete_chain and len(handoffs) != 6:
        failures.append("Golden lifecycle requires six handoffs")
    for handoff in handoffs:
        artifact = handoff.get("envelope_artifact") if isinstance(handoff, Mapping) else None
        if not isinstance(artifact, str) or not _inside(root, Path(artifact)):
            failures.append("handoff envelope is missing or outside evidence root")

    return {
        "classification": "P0 RUNTIME LIFECYCLE / P1 EVIDENCE ROOT CONSISTENCY",
        "run_id": run_id,
        "provider_call_count": len(calls),
        "invocation_id_count": len(invocation_ids),
        "strict_transport_call_count": len(strict_calls),
        "authorized_strict_transport_call_count": sum(1 for item in strict_authorizations if item["authorized"]),
        "strict_transport_authorizations": strict_authorizations,
        "handoff_count": len(handoffs),
        "ledger_entry_count": len(entries),
        "provider_calls": 0,
        "executor_calls": 0,
        "result": "PASS" if not failures else "FAIL",
        "failures": failures,
    }


def load_json(path: Path) -> dict[str, Any] | list[Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_golden_recorded_evidence(*, evidence_root: Path) -> dict[str, Any]:
    """Replay Golden evidence as recorded data, without a provider or executor."""

    root = evidence_root.resolve()
    required = {
        "manifest": root / "execution_manifest.json",
        "provider": root / "provider_manifest.json",
        "handoffs": root / "handoff_trace.json",
        "ledger": root / "state_ledger.json",
        "acceptance": root / "acceptance_test_report.json",
    }
    missing = [name for name, path in required.items() if not path.is_file()]
    if missing:
        return {"classification": "GOLDEN RECORDED REGRESSION", "result": "BLOCKED", "missing": missing, "provider_calls": 0, "executor_calls": 0}
    manifest = load_json(required["manifest"])
    provider = load_json(required["provider"])
    handoffs = load_json(required["handoffs"])
    ledger = load_json(required["ledger"])
    acceptance = load_json(required["acceptance"])
    if not isinstance(manifest, Mapping) or not isinstance(provider, Mapping) or not isinstance(handoffs, list) or not isinstance(ledger, Mapping) or not isinstance(acceptance, Mapping):
        return {"classification": "GOLDEN RECORDED REGRESSION", "result": "FAIL", "failures": ["recorded JSON shapes are invalid"], "provider_calls": 0, "executor_calls": 0}
    lifecycle = validate_lifecycle_consistency(manifest=manifest, provider_manifest=provider, handoffs=handoffs, ledger=ledger, evidence_root=root, require_complete_chain=True)
    expected_outcomes = {
        "showrunner": "PASS",
        "scene_writer": "SCENE_CREATED",
        "director": "DIRECTION_PLAN_PRODUCED",
        "character_acting": "PERFORMANCE_INTERPRETATION_READY",
        "art_director": "DESIGN_RESPONSE_READY",
        "continuity": "CONTINUITY PRESERVED",
        "shared_qa": "PASS / NO CHANGE",
    }
    failures = list(lifecycle["failures"])
    calls = provider.get("calls", [])
    seen_roles: set[str] = set()
    for call in calls if isinstance(calls, list) else []:
        role = call.get("role") if isinstance(call, Mapping) else None
        key = str(role).lower().replace(" & ", "_").replace(" ", "_")
        if key == "character_acting":
            pass
        if key not in expected_outcomes:
            failures.append("unexpected or missing role in provider manifest")
            continue
        seen_roles.add(key)
        output = call.get("output_artifact")
        if not isinstance(output, str) or not Path(output).is_file():
            failures.append(f"{key} parsed output is unavailable")
            continue
        parsed = load_json(Path(output))
        if not isinstance(parsed, Mapping) or parsed.get("primary_state_or_outcome") != expected_outcomes[key]:
            failures.append(f"{key} recorded outcome changed or is unparseable")
        if not isinstance(parsed, Mapping) or parsed.get("flags") != "ABSENT" or parsed.get("handoffs") != "ABSENT":
            failures.append(f"{key} canonical transport tokens changed")
    if seen_roles != set(expected_outcomes):
        failures.append("seven-role chain is incomplete")
    if acceptance.get("passed") != 18 or acceptance.get("total") != 18 or acceptance.get("overall") != "PASS":
        failures.append("E2E-INT 18/18 evidence is not reproducible")
    return {
        "classification": "GOLDEN RECORDED REGRESSION",
        "run_id": manifest.get("run_id"),
        "role_count": len(seen_roles),
        "acceptance": f"{acceptance.get('passed')}/{acceptance.get('total')} {acceptance.get('overall')}",
        "lifecycle": lifecycle,
        "provider_calls": 0,
        "executor_calls": 0,
        "result": "PASS" if not failures else "FAIL",
        "failures": failures,
    }
