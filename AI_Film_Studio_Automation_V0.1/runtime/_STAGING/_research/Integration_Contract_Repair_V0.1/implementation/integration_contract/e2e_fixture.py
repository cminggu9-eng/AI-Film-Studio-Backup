"""Provider-free loader for the frozen E2E-FIX-01 source document."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict


E2E_FIXTURE_ID = "E2E-FIX-01"
FROZEN_CONCEPT = "暴雨夜，夜班管理员许宁把一把刻有“A-17”的黄铜钥匙交给久未联系的姐姐许曼；许曼承认这是母亲留给两人一起打开储物间的钥匙，要求许宁先换下湿透的制服、等天亮再开门。"
FIXTURE_DOCUMENT = "AI_Film_Studio_E2E_Fixture_01_V0.1.md"


def _automation_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "studio.config.json").is_file():
            return candidate
    raise RuntimeError("AI Film Studio Automation root not found")


def load_e2e_fixture_01() -> Dict[str, Any]:
    """Load and attest the one frozen input without invoking any role."""

    automation_root = _automation_root()
    config = json.loads((automation_root / "studio.config.json").read_text(encoding="utf-8-sig"))
    document_path = Path(config["vault_path"]) / "00_HOME" / FIXTURE_DOCUMENT
    text = document_path.read_text(encoding="utf-8")
    if FROZEN_CONCEPT not in text:
        raise ValueError("Frozen E2E-FIX-01 concept was not found in its canonical fixture document")
    return {
        "fixture_id": E2E_FIXTURE_ID,
        "concept": FROZEN_CONCEPT,
        "source_document": str(document_path.resolve()),
        "source_document_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "execution": "NOT_AUTHORIZED",
    }
