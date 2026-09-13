"""Isolated filesystem context for runtime and black-box fixtures.

This helper never points at the formal Obsidian Vault.  A test may only write
its canon, project state, logs, and temporary output below ``_TEST_SANDBOX``.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from uuid import uuid4


ROOT = Path(__file__).resolve().parents[2]
SANDBOX_ROOT = ROOT / "runtime" / "_TEST_SANDBOX"


def create_test_sandbox(test_id: str) -> Path:
    safe_id = "".join(char if char.isalnum() or char in "-_" else "_" for char in test_id)
    target = SANDBOX_ROOT / safe_id / f"{datetime.now().strftime('%Y%m%d-%H%M%S-%f')}-{uuid4().hex[:8]}"
    for name in ("canon", "character_files", "project_state", "logs", "temporary_outputs"):
        (target / name).mkdir(parents=True, exist_ok=False)
    manifest = {
        "test_id": test_id,
        "sandbox_root": str(target),
        "formal_vault_write_allowed": False,
        "allowed_write_roots": [str(target / name) for name in ("canon", "character_files", "project_state", "logs", "temporary_outputs")],
    }
    (target / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return target


def write_sandbox_canon(sandbox: Path, filename: str, content: str) -> Path:
    target = sandbox / "canon" / filename
    target.write_text(content, encoding="utf-8")
    return target
