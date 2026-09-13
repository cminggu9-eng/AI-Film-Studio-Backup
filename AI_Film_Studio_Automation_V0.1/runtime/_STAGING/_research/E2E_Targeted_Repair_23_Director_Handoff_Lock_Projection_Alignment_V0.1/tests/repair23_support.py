"""Repair23 offline evidence bindings; no provider or live-run capability."""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict

STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
REPAIR22 = RESEARCH / "E2E_Targeted_Repair_22_Director_Provider_Wire_Tagged_Union_Codec_Strict_Native_Type_Reliability_V0.1"
REPAIR22_SUPPORT = REPAIR22 / "tests"
PROBE22 = REPAIR22 / "reports" / "DIRECTOR-TAGGED-WIRE-PROBE-22-F03"
PROBE22_RAW = PROBE22 / "artifacts" / "director_provider_response.json"
PROBE22_MANIFEST = PROBE22 / "Director_DeepSeek_Tagged_Wire_Probe_22.json"
R26 = HARNESS / "evidence" / "E2E-RUN-26"
R26_SCENE_WRITER = R26 / "artifacts" / "scene_writer_output.json"
R26_DIRECTOR_INPUT = R26 / "artifacts" / "director_input.json"
REPORTS = STAGE / "reports"

for directory in (REPAIR22_SUPPORT, HARNESS, AUTOMATION_ROOT):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

from repair22_support import state_contract
import run_minimal_e2e as e2e
from director_provider_compatibility import decode_director_provider_wire_arguments, validate_director_provider_wire_arguments
from director_structured_submission import make_director_payload_validator


def read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def probe22_arguments() -> Dict[str, Any]:
    persisted = read_json(PROBE22_RAW)
    response = json.loads(persisted["raw_provider_response"])
    outer = response["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"]
    return json.loads(outer)


def authoritative_projection() -> Dict[str, Any]:
    return e2e.project_authoritative_handoff_constraints(read_json(R26_SCENE_WRITER))


def canonical_validator(contract, projection):
    return make_director_payload_validator(
        selected_mode="PLAN",
        required_locks=projection["canon_assignment_locks"],
        prohibited_changes=projection["prohibited_changes"],
        state_contract=contract,
    )


def tree_digest(path: Path) -> str:
    digest = hashlib.sha256()
    for item in sorted((candidate for candidate in path.rglob("*") if candidate.is_file()), key=lambda p: p.relative_to(path).as_posix()):
        digest.update(item.relative_to(path).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(item.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def historical_e2e_digests() -> Dict[str, str]:
    evidence = HARNESS / "evidence"
    result = {}
    for number in range(6, 27):
        path = evidence / f"E2E-RUN-{number:02d}"
        if not path.is_dir():
            path = evidence / f"E2E-RUN-{number}"
        if not path.is_dir():
            raise RuntimeError(f"missing immutable historical evidence root: E2E-RUN-{number:02d}")
        result[path.name] = tree_digest(path)
    return result
