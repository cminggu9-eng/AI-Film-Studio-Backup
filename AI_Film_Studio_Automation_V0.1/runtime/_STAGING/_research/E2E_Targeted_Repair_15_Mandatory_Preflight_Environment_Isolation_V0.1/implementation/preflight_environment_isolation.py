"""Deterministic, redacted environment projection for offline preflight suites.

This module contains no fixture identities or role semantics.  Fixture choice
belongs to the caller-owned suite manifest, while the live runner retains its
own process environment unchanged.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping


ENVIRONMENT_POLICY_VERSION = "PREFLIGHT-SUBPROCESS-ENV-ISOLATION-V0.1"
LIVE_RUN_SCOPED_AFS_E2E = frozenset(
    {
        "AFS_E2E_RUN_ID",
        "AFS_E2E_EVIDENCE_ROOT",
        "AFS_E2E_RECOVERY_OF",
        "AFS_E2E_AUTHORIZATION_LABEL",
        "AFS_E2E_FIXTURE_BINDING",
    }
)
SAFE_GLOBAL_EXACT = frozenset(
    {
        "ALLUSERSPROFILE",
        "APPDATA",
        "COMSPEC",
        "HOMEDRIVE",
        "HOMEPATH",
        "LOCALAPPDATA",
        "NUMBER_OF_PROCESSORS",
        "OS",
        "PATH",
        "PATHEXT",
        "PROCESSOR_ARCHITECTURE",
        "PROCESSOR_IDENTIFIER",
        "PROCESSOR_LEVEL",
        "PROCESSOR_REVISION",
        "PROGRAMDATA",
        "PUBLIC",
        "PYTHONHOME",
        "PYTHONIOENCODING",
        "PYTHONPATH",
        "PYTHONUTF8",
        "SYSTEMROOT",
        "TEMP",
        "TMP",
        "USERPROFILE",
        "VIRTUAL_ENV",
        "WINDIR",
    }
)


@dataclass(frozen=True)
class PreflightSuiteManifest:
    suite_id: str
    script: Path
    expected_total: int
    fixture_binding: Path | None = None

    def record(self) -> dict[str, object]:
        return {
            "suite_id": self.suite_id,
            "script": str(self.script),
            "expected_total": self.expected_total,
            "fixture_binding_source": "SUITE_MANIFEST"
            if self.fixture_binding is not None
            else "NO_FIXTURE_BINDING_REQUIRED",
            "declared_fixture_binding": str(self.fixture_binding) if self.fixture_binding is not None else "ABSENT",
        }


def _normalized(name: str) -> str:
    return name.upper()


def classify_afs_e2e_environment(parent_env: Mapping[str, str]) -> dict[str, str]:
    """Classify present AFS_E2E variables without exposing their values."""

    classification: dict[str, str] = {}
    for key in sorted(parent_env):
        normalized = _normalized(key)
        if not normalized.startswith("AFS_E2E_"):
            continue
        classification[key] = (
            "LIVE_RUN_SCOPED" if normalized in LIVE_RUN_SCOPED_AFS_E2E else "UNKNOWN_AFS_E2E"
        )
    return classification


def _is_safe_global(name: str) -> bool:
    normalized = _normalized(name)
    return normalized in SAFE_GLOBAL_EXACT or normalized.startswith("PROCESSOR_")


def _environment_hash(environment: Mapping[str, str]) -> str:
    material = "\n".join(f"{key}={environment[key]}" for key in sorted(environment, key=str.upper))
    return hashlib.sha256(material.encode("utf-8")).hexdigest().upper()


def build_preflight_subprocess_env(
    suite_manifest: PreflightSuiteManifest,
    parent_env: Mapping[str, str],
) -> tuple[dict[str, str], dict[str, object]]:
    """Return a suite-owned child environment and redacted provenance.

    Only an approved, non-secret global base is copied.  All parent AFS_E2E
    variables are removed, including unknown variables, before an optional
    suite-declared fixture binding is injected.
    """

    parent_snapshot = {str(key): str(value) for key, value in parent_env.items()}
    classifications = classify_afs_e2e_environment(parent_snapshot)
    child_env = {
        key: value
        for key, value in parent_snapshot.items()
        if _is_safe_global(key) and not _normalized(key).startswith("AFS_E2E_")
    }
    injected: dict[str, str] = {}
    if suite_manifest.fixture_binding is not None:
        fixture_path = Path(suite_manifest.fixture_binding)
        if not fixture_path.is_file():
            raise ValueError(f"suite fixture binding is unavailable: {fixture_path}")
        child_env["AFS_E2E_FIXTURE_BINDING"] = str(fixture_path)
        injected["AFS_E2E_FIXTURE_BINDING"] = str(fixture_path)

    removed = [
        {"name": key, "classification": classifications[key]}
        for key in sorted(classifications, key=str.upper)
    ]
    provenance: dict[str, object] = {
        "environment_policy_version": ENVIRONMENT_POLICY_VERSION,
        "suite": suite_manifest.record(),
        "parent_afs_e2e_classification": classifications,
        "removed_live_run_variables": removed,
        "explicitly_injected_variables": sorted(injected),
        "effective_fixture_binding": injected.get("AFS_E2E_FIXTURE_BINDING", "ABSENT"),
        "safe_global_names": sorted(child_env_key for child_env_key in child_env if not _normalized(child_env_key).startswith("AFS_E2E_")),
        "provider_credentials_injected": False,
        "environment_hash": _environment_hash(child_env),
    }
    return child_env, provenance


def provenance_json(provenance: Mapping[str, object]) -> str:
    """Stable serialization used by tests to assert that evidence is redacted."""

    return json.dumps(dict(provenance), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
