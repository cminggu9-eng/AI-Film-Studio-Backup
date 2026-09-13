"""Character & Acting raw-role and reserved-slot transport separation.

Character & Acting owns playable performance interpretation. Scene Writer owns
``scene_packages`` semantics. The generic ten-field E2E role-result transport
still reserves a ``scene_packages`` slot for every role, so Integration may
represent Character & Acting's lawful non-ownership with the existing literal
sentinel ``ABSENT`` only after a validated upstream Scene Writer source is
present and source-identical.

This module never asks Character & Acting to echo, copy, summarize, reconstruct,
rewrite, or translate Scene Writer packages. It performs no prose extraction or
semantic repair.
"""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Mapping


ABSENT = "ABSENT"
CONTRACT_VERSION = "CHARACTER-ACTING-TRANSPORT-V0.1"
SOURCE_SCHEMA_IDENTITY = "SCENE-WRITER-INTEGRATION-OUTPUT-CONTRACT-V0.1"

CHARACTER_ACTING_CANONICAL_OUTCOMES = (
    "PERFORMANCE_INTERPRETATION_READY",
    "PERFORMANCE_INTERPRETATION_REVISED",
    "NO_PERFORMANCE_CHANGE",
    "CONTEXT_REQUIRED",
    "UPSTREAM_DECISION_REQUIRED",
    "OUT_OF_SCOPE",
)

CHARACTER_ACTING_RAW_ROLE_FIELDS = (
    "primary_state_or_outcome",
    "flags",
    "handoffs",
    "canon_assignment_locks",
    "prohibited_changes",
    "required_outcome",
    "unresolved_decisions",
    "state_evidence",
    "content",
)

CHARACTER_ACTING_FINAL_TRANSPORT_FIELDS = (
    *CHARACTER_ACTING_RAW_ROLE_FIELDS,
    "scene_packages",
)

STATE_EVIDENCE_FIELDS = (
    "relevant_prior_state",
    "current_state",
    "proposed_state",
    "knowledge_timing",
    "relationship_state",
    "visual_state",
)

SCENE_PACKAGE_FIELDS = (
    "scene_id",
    "content",
    "structural_deliverable",
    "state_evidence",
    "source_attribution",
    "evidence_locator",
)

SOURCE_ATTRIBUTION_FIELDS = (
    "source_role",
    "source_record_id",
    "version",
    "evidence_locator",
)

FAILURE_RAW = "CHARACTER & ACTING RAW ROLE-CONTRACT FAILURE"
FAILURE_SLOT = "INTEGRATION MACHINE-CONTRACT / TRANSPORT-SLOT ALIGNMENT FAILURE"
FAILURE_TOKEN = "CHARACTER & ACTING CANONICAL TOKEN FAILURE"
FAILURE_AUTHORITY = "CHARACTER & ACTING AUTHORITY-BOUNDARY FAILURE"


class CharacterActingTransportContractError(ValueError):
    """An attributable raw-role, source, assembly, or final-transport failure."""

    def __init__(self, message: str, *, classification: str = FAILURE_SLOT) -> None:
        super().__init__(message)
        self.classification = classification


@dataclass(frozen=True)
class CharacterActingTransportAssembly:
    """Final ten-field transport plus immutable field-origin evidence."""

    payload: Dict[str, Any]
    evidence: Dict[str, Any]

    def evidence_record(self) -> Dict[str, Any]:
        return copy.deepcopy(self.evidence)


def _stable_json_sha256(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _json_safe(value: Any) -> bool:
    try:
        json.dumps(value, ensure_ascii=False)
    except (TypeError, ValueError):
        return False
    return True


def _string_list(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) and bool(item.strip()) for item in value)


def character_acting_raw_role_schema() -> Dict[str, Any]:
    """Prompt-facing raw role schema; it deliberately has no scene_packages."""

    return {
        "primary_state_or_outcome": f"one exact token from {list(CHARACTER_ACTING_CANONICAL_OUTCOMES)}",
        "flags": "exact ABSENT",
        "handoffs": "exact ABSENT",
        "canon_assignment_locks": ["copy every received lock exactly"],
        "prohibited_changes": ["copy every received prohibition exactly"],
        "required_outcome": "string or exact ABSENT",
        "unresolved_decisions": "array of strings or exact ABSENT",
        "state_evidence": {
            field: "JSON object or exact ABSENT"
            for field in STATE_EVIDENCE_FIELDS
        },
        "content": "non-empty zh-CN playable performance interpretation; no Markdown fence",
    }


def character_acting_contract_manifest() -> Dict[str, Any]:
    """One ownership manifest for prompt, assembly, and both validators."""

    return {
        "contract_version": CONTRACT_VERSION,
        "ownership": {
            "character_acting_role_owned": list(CHARACTER_ACTING_RAW_ROLE_FIELDS),
            "scene_packages_semantic_owner": "Scene Writer",
            "scene_packages_character_stage_owner": "Integration reserved transport slot",
            "scene_packages_character_final_representation": ABSENT,
            "upstream_scene_packages_representation": "independent source artifact and identity reference",
        },
        "raw_role_contract": {
            "required_fields": list(CHARACTER_ACTING_RAW_ROLE_FIELDS),
            "additional_fields": False,
            "scene_packages": "PROHIBITED FROM MODEL RAW ROLE PAYLOAD",
        },
        "final_role_transport_contract": {
            "required_fields": list(CHARACTER_ACTING_FINAL_TRANSPORT_FIELDS),
            "additional_fields": False,
            "scene_packages": {"const": ABSENT, "origin": "INTEGRATION_TRANSPORT_ABSENCE_SENTINEL"},
        },
        "assembly_preconditions": {
            "validated_upstream_scene_writer_output": True,
            "source_artifact_exists": True,
            "source_object_matches_artifact": True,
            "scene_package_source_identity_complete": True,
        },
        "provider_transport": "NON_STRICT",
        "semantic_mutation": 0,
    }


def validate_character_acting_raw_role_payload(payload: Mapping[str, Any]) -> Dict[str, Any]:
    """Validate only Character & Acting-owned raw machine fields."""

    if not isinstance(payload, Mapping):
        raise CharacterActingTransportContractError(
            "Character & Acting raw role payload must be an object",
            classification=FAILURE_RAW,
        )
    actual = set(payload)
    expected = set(CHARACTER_ACTING_RAW_ROLE_FIELDS)
    if "scene_packages" in actual:
        raise CharacterActingTransportContractError(
            "Character & Acting raw role payload must not own or echo scene_packages",
            classification=FAILURE_AUTHORITY,
        )
    if actual != expected:
        raise CharacterActingTransportContractError(
            f"Character & Acting raw role fields are not exact; missing={sorted(expected - actual)}; extra={sorted(actual - expected)}",
            classification=FAILURE_RAW,
        )
    if payload["primary_state_or_outcome"] not in CHARACTER_ACTING_CANONICAL_OUTCOMES:
        raise CharacterActingTransportContractError(
            "Character & Acting outcome is not an exact canonical token",
            classification=FAILURE_TOKEN,
        )
    if payload["flags"] != ABSENT or payload["handoffs"] != ABSENT:
        raise CharacterActingTransportContractError(
            "Character & Acting has no canonical flags or handoffs; both raw values must be ABSENT",
            classification=FAILURE_RAW,
        )
    if not _string_list(payload["canon_assignment_locks"]):
        raise CharacterActingTransportContractError("canon_assignment_locks must be a string array", classification=FAILURE_RAW)
    if not _string_list(payload["prohibited_changes"]):
        raise CharacterActingTransportContractError("prohibited_changes must be a string array", classification=FAILURE_RAW)
    if not isinstance(payload["required_outcome"], str) or not payload["required_outcome"].strip():
        raise CharacterActingTransportContractError("required_outcome must be a non-empty string", classification=FAILURE_RAW)
    unresolved = payload["unresolved_decisions"]
    if unresolved != ABSENT and not _string_list(unresolved):
        raise CharacterActingTransportContractError("unresolved_decisions must be a string array or ABSENT", classification=FAILURE_RAW)
    state = payload["state_evidence"]
    if not isinstance(state, Mapping) or set(state) != set(STATE_EVIDENCE_FIELDS):
        raise CharacterActingTransportContractError("state_evidence must contain the exact six fields", classification=FAILURE_RAW)
    if any(item is None for item in state.values()) or not _json_safe(state):
        raise CharacterActingTransportContractError("state_evidence must be JSON-safe and must not use null", classification=FAILURE_RAW)
    if not isinstance(payload["content"], str) or not payload["content"].strip():
        raise CharacterActingTransportContractError("content must be non-empty", classification=FAILURE_RAW)
    if not _json_safe(payload):
        raise CharacterActingTransportContractError("raw role payload must be JSON-safe", classification=FAILURE_RAW)
    return copy.deepcopy(dict(payload))


def scene_packages_source_identity(
    scene_writer_output: Mapping[str, Any],
    *,
    source_artifact_path: Path,
) -> Dict[str, Any]:
    """Verify the validated Scene Writer source and return transport metadata."""

    if not isinstance(scene_writer_output, Mapping):
        raise CharacterActingTransportContractError("validated upstream Scene Writer output is missing")
    source_path = Path(source_artifact_path).resolve()
    if not source_path.is_file():
        raise CharacterActingTransportContractError("upstream Scene Writer source artifact is missing")
    try:
        persisted_source = json.loads(source_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CharacterActingTransportContractError("upstream Scene Writer source artifact is unreadable") from exc
    packages = scene_writer_output.get("scene_packages")
    persisted_packages = persisted_source.get("scene_packages") if isinstance(persisted_source, Mapping) else None
    if not isinstance(packages, list) or not packages:
        raise CharacterActingTransportContractError("required upstream Scene Writer scene_packages are missing")
    if _stable_json_sha256(packages) != _stable_json_sha256(persisted_packages):
        raise CharacterActingTransportContractError("upstream Scene Writer scene_packages do not match their source artifact")

    scene_ids: list[str] = []
    record_ids: list[str] = []
    versions: list[str] = []
    evidence_locators: list[str] = []
    for index, package in enumerate(packages):
        if not isinstance(package, Mapping) or set(package) != set(SCENE_PACKAGE_FIELDS):
            raise CharacterActingTransportContractError(f"upstream scene package {index} has an invalid field set")
        attribution = package.get("source_attribution")
        if not isinstance(attribution, Mapping) or set(attribution) != set(SOURCE_ATTRIBUTION_FIELDS):
            raise CharacterActingTransportContractError(f"upstream scene package {index} lost source attribution")
        if attribution.get("source_role") != "Scene Writer":
            raise CharacterActingTransportContractError(f"upstream scene package {index} has the wrong semantic owner")
        scene_id = package.get("scene_id")
        record_id = attribution.get("source_record_id")
        version = attribution.get("version")
        locator = package.get("evidence_locator")
        if not all(isinstance(item, str) and item.strip() for item in (scene_id, record_id, version, locator)):
            raise CharacterActingTransportContractError(f"upstream scene package {index} has incomplete source identity")
        if attribution.get("evidence_locator") != locator:
            raise CharacterActingTransportContractError(f"upstream scene package {index} evidence locator changed")
        scene_ids.append(scene_id)
        record_ids.append(record_id)
        versions.append(version)
        evidence_locators.append(locator)
    if len(scene_ids) != len(set(scene_ids)) or len(record_ids) != len(set(record_ids)):
        raise CharacterActingTransportContractError("upstream Scene Writer source identities are not unique")
    return {
        "source_role": "Scene Writer",
        "source_artifact": str(source_path),
        "source_artifact_sha256": _file_sha256(source_path),
        "source_schema_identity": SOURCE_SCHEMA_IDENTITY,
        "scene_packages_sha256": _stable_json_sha256(packages),
        "scene_package_ids": scene_ids,
        "source_record_ids": record_ids,
        "source_versions": versions,
        "evidence_locators": evidence_locators,
    }


def validate_character_acting_assembly_evidence(evidence: Mapping[str, Any]) -> Dict[str, Any]:
    """Fail closed if source identity or no-mutation evidence is lost."""

    expected = {
        "contract_version",
        "assembly_stage",
        "inserted_transport_fields",
        "transport_field_origins",
        "upstream_scene_packages",
        "raw_role_payload_sha256",
        "final_role_transport_sha256",
        "semantic_mutation",
        "canonical_token_mutation",
        "scene_package_semantic_copy",
    }
    if not isinstance(evidence, Mapping) or set(evidence) != expected:
        raise CharacterActingTransportContractError("Character & Acting assembly evidence lost an exact field")
    source = evidence.get("upstream_scene_packages")
    required_source = {
        "source_role",
        "source_artifact",
        "source_artifact_sha256",
        "source_schema_identity",
        "scene_packages_sha256",
        "scene_package_ids",
        "source_record_ids",
        "source_versions",
        "evidence_locators",
    }
    if not isinstance(source, Mapping) or set(source) != required_source:
        raise CharacterActingTransportContractError("upstream Scene Writer source identity is incomplete")
    if evidence.get("inserted_transport_fields") != ["scene_packages"]:
        raise CharacterActingTransportContractError("reserved transport insertion evidence is not exact")
    if evidence.get("transport_field_origins") != {"scene_packages": "INTEGRATION_TRANSPORT_ABSENCE_SENTINEL"}:
        raise CharacterActingTransportContractError("reserved transport origin is not exact")
    if evidence.get("semantic_mutation") != 0 or evidence.get("canonical_token_mutation") != 0:
        raise CharacterActingTransportContractError("assembly evidence records semantic or canonical mutation")
    if evidence.get("scene_package_semantic_copy") != 0:
        raise CharacterActingTransportContractError("assembly copied Scene Writer semantics into Character & Acting output")
    return copy.deepcopy(dict(evidence))


def assemble_character_acting_transport(
    raw_role_payload: Mapping[str, Any],
    *,
    scene_writer_output: Mapping[str, Any],
    source_artifact_path: Path,
) -> CharacterActingTransportAssembly:
    """Add the reserved ABSENT slot after exact raw/source validation."""

    raw = validate_character_acting_raw_role_payload(raw_role_payload)
    source_identity = scene_packages_source_identity(
        scene_writer_output,
        source_artifact_path=source_artifact_path,
    )
    final_payload = copy.deepcopy(raw)
    final_payload["scene_packages"] = ABSENT
    evidence = {
        "contract_version": CONTRACT_VERSION,
        "assembly_stage": "INTEGRATION RESERVED-SLOT ASSEMBLY",
        "inserted_transport_fields": ["scene_packages"],
        "transport_field_origins": {"scene_packages": "INTEGRATION_TRANSPORT_ABSENCE_SENTINEL"},
        "upstream_scene_packages": source_identity,
        "raw_role_payload_sha256": _stable_json_sha256(raw),
        "final_role_transport_sha256": _stable_json_sha256(final_payload),
        "semantic_mutation": 0,
        "canonical_token_mutation": 0,
        "scene_package_semantic_copy": 0,
    }
    validate_character_acting_assembly_evidence(evidence)
    return CharacterActingTransportAssembly(payload=final_payload, evidence=evidence)


def validate_final_character_acting_transport(payload: Mapping[str, Any]) -> Dict[str, Any]:
    """Validate the full ten-field role-result transport after assembly."""

    if not isinstance(payload, Mapping) or set(payload) != set(CHARACTER_ACTING_FINAL_TRANSPORT_FIELDS):
        raise CharacterActingTransportContractError("final Character & Acting transport field set is not exact")
    if payload.get("scene_packages") != ABSENT:
        raise CharacterActingTransportContractError(
            "final Character & Acting scene_packages slot must be exact ABSENT; Scene Writer retains semantic ownership",
            classification=FAILURE_AUTHORITY,
        )
    raw = {field: copy.deepcopy(payload[field]) for field in CHARACTER_ACTING_RAW_ROLE_FIELDS}
    validate_character_acting_raw_role_payload(raw)
    return copy.deepcopy(dict(payload))


def validate_character_acting_non_strict_transport(*, strict_enabled: bool) -> None:
    """Keep Character & Acting outside the Repair11 strict authorization set."""

    if strict_enabled:
        raise CharacterActingTransportContractError(
            "Character & Acting strict Provider transport is unauthorized",
            classification=FAILURE_AUTHORITY,
        )

