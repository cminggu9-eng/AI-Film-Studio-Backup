"""One complete non-semantic Scene Writer Runtime transport E2E."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
for path in (str(STAGE), str(AUTOMATION_ROOT)):
    if path not in sys.path:
        sys.path.insert(0, path)

from runtime.scene_writer.scene_writer_runtime import SceneWriterRuntime  # noqa: E402


fixture_path = STAGE / "fixtures" / "scene_writer_runtime_synthetic_fixtures.json"
fixture = json.loads(fixture_path.read_text(encoding="utf-8"))["fixtures"]["RT-SW-MULTI-01"]


def synthetic_executor(invocation: dict) -> dict:
    assert invocation["runtime"]["classification"] == "SYNTHETIC / NON-CANON / NON-SEMANTIC"
    assert invocation["canonical_skill"]["identity"] == "scene-writer"
    return copy.deepcopy(fixture["output"])


def main() -> int:
    """Run only after an explicit command-line synthetic-test request."""
    runtime = SceneWriterRuntime(synthetic_executor=synthetic_executor, test_sandbox=True)
    result = runtime.execute({
        "request_id": "SYN-E2E-01",
        "requested_mode": "CREATE",
        "assignment_language": "en-US",
        "project_id": "SYNTHETIC-PROJECT",
        "episode_id": "SYNTHETIC-EPISODE",
        "scene_id": "RT-SW-MULTI-01",
        "scene_purpose": "synthetic E2E transport validation",
        "canon_locks": [], "showrunner_locks": [], "participants": [], "character_context": {},
        "required_event": None,
        "required_information": None,
        "required_outcome": None,
        "prior_scene_state": None,
        "desired_post_state": None,
        "production_constraints": None,
        "requested_form": None,
        "downstream_requests": [],
        "qa_requests": []
    })

    assert result["runtime_status"] == "SUCCESS", result
    assert result["canonical_binding"]["passed"] is True, result
    assert result["scene_writer"]["control_data"]["primary_state"] == "SCENE_CREATED", result
    assert set(result["scene_writer"]["control_data"]["flags"]) == {"SHARED_QA_HANDOFF_ELIGIBLE", "DIRECTOR_HANDOFF_ELIGIBLE"}, result
    assert len(result["scene_writer"]["control_data"]["handoffs"]) == 2, result

    print(json.dumps({
        "classification": "SYNTHETIC / NON-CANON / NON-SEMANTIC",
        "result": "RUNTIME TRANSPORT / CONTRACT E2E PASS",
        "runtime_status": result["runtime_status"],
        "primary_state": result["scene_writer"]["control_data"]["primary_state"],
        "flags": result["scene_writer"]["control_data"]["flags"],
        "canonical_path": result["canonical_binding"]["canonical_path"],
        "real_semantic_executor": runtime.registry_status()["real_semantic_executor"]
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
