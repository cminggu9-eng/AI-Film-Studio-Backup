"""Provider-free static discovery harness for Integration Contract Repair."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from .e2e_fixture import load_e2e_fixture_01
from .state_evidence import ABSENT, ENVELOPE_FIELDS


def _automation_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "studio.config.json").is_file():
            return candidate
    raise RuntimeError("AI Film Studio Automation root not found")


def load_static_configuration() -> Dict[str, Any]:
    root = _automation_root()
    config = json.loads((root / "studio.config.json").read_text(encoding="utf-8-sig"))
    return {
        "automation_root": str(root),
        "vault_path": config["vault_path"],
        "operation": "STATIC_CONFIGURATION_LOAD",
    }


def discover_scene_writer_role() -> Dict[str, str]:
    """Read binding metadata only; do not construct provider or executor."""

    from runtime.scene_writer.scene_writer_executor_binding import SceneWriterCanonicalBinding

    binding = SceneWriterCanonicalBinding.load()
    return {
        "identity": binding.identity,
        "version": binding.version,
        "sha256": binding.sha256,
        "canonical_path": str(binding.canonical_path),
        "operation": "STATIC_ROLE_DISCOVERY",
    }


def discover_scene_writer_adapter() -> Dict[str, str]:
    """Discover the adapter class only; do not instantiate Runtime or executor."""

    from runtime.scene_writer.scene_writer_runtime import SceneWriterRuntime

    return {
        "adapter": SceneWriterRuntime.__name__,
        "operation": "STATIC_ADAPTER_DISCOVERY",
        "provider_or_executor_construction": "PROHIBITED",
    }


def load_state_envelope_contract() -> Dict[str, Any]:
    return {
        "field_count": len(ENVELOPE_FIELDS),
        "absent_token": ABSENT,
        "operation": "STATIC_STATE_ENVELOPE_LOAD",
    }


def startup_discovery() -> Dict[str, Any]:
    """Complete all allowed startup/discovery operations without execution."""

    return {
        "configuration": load_static_configuration(),
        "role": discover_scene_writer_role(),
        "adapter": discover_scene_writer_adapter(),
        "state_envelope": load_state_envelope_contract(),
        "fixture": load_e2e_fixture_01(),
        "provider_calls": 0,
        "executor_calls": 0,
        "real_execution": "NOT_AUTHORIZED",
    }
