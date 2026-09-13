"""Execute the one authorized real, non-canon Scene Writer smoke; writes no files."""

from __future__ import annotations

import json
import sys
from pathlib import Path


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
for path in (str(STAGE), str(AUTOMATION_ROOT)):
    if path not in sys.path:
        sys.path.insert(0, path)

CLASSIFICATION = "VALIDATION / SYNTHETIC / NON-CANON / REAL SEMANTIC EXECUTION"
REQUEST_ID = "SMOKE-SW-EXEC-01"
INVOCATION_ID = f"scene-writer:{REQUEST_ID}"
VERIFY_INVOCATION_ID = f"scene-writer-integrity:{REQUEST_ID}"

ASSIGNMENT = {
    "request_id": REQUEST_ID,
    "requested_mode": "CREATE",
    "output_language": "zh-CN",
    "project_id": "VALIDATION / SYNTHETIC / NON-CANON",
    "episode_id": "TEST-EP01",
    "scene_id": "SMOKE-SW-EXEC-01",
    "scene_request": "Write one short playable scene only; do not expand into a full plot.",
    "scene_purpose": "Test whether clear objective, resistance, and information limits become a short playable scene.",
    "repair_target": None,
    "canon_locks": [
        "Do not invent the absent presenter's reason.",
        "Lin Yan does not know that reason and may not claim otherwise.",
        "Chen Mo does not agree immediately.",
        "The two are not enemies.",
        "No third character.",
        "Do not change the office meeting-room location.",
    ],
    "showrunner_locks": [
        "Required post-scene state: Chen Mo conditionally accepts the presentation and requires all existing materials tonight.",
    ],
    "participants": [
        {
            "name": "Lin Yan",
            "role": "project team lead",
            "objective": "Confirm tonight who will handle tomorrow morning's presentation.",
            "knowledge": "The original presenter cannot attend tomorrow morning; the specific reason is unknown.",
            "constraint": "She will not explain for that person without permission.",
        },
        {
            "name": "Chen Mo",
            "role": "project member",
            "objective": "Avoid an imposed last-minute responsibility unless conditions are clear.",
            "capacity": "Can take over the presentation.",
            "constraint": "He was preparing to leave and dislikes being pressured with 'everyone is counting on you'.",
        },
    ],
    "character_context": {
        "relationship": "colleagues under immediate work pressure, not enemies",
        "creative_freedom": "Dialogue, pauses, actions, and negotiation method may be chosen within the locks.",
    },
    "required_event": "Lin Yan must ask Chen Mo to take tomorrow morning's presentation.",
    "required_information": "The original presenter cannot attend tomorrow morning; the reason is unknown and must not be invented.",
    "required_outcome": "Chen Mo agrees to take it for now, conditional on Lin Yan sending all existing materials tonight.",
    "prior_scene_state": "The meeting has just ended; only Lin Yan and Chen Mo remain in the office meeting room.",
    "desired_post_state": "Chen Mo has conditionally accepted; Lin Yan must send the existing materials tonight.",
    "production_constraints": None,
    "requested_form": "Short, normal readable Scene Writer scene. No camera/lens/coverage directions and no acting system.",
    "downstream_requests": [],
    "qa_requests": [],
}


def main() -> int:
    """Run only after an explicit command-line execution request."""
    from runtime.scene_writer.scene_writer_executor_binding import create_scene_writer_binding

    bundle = create_scene_writer_binding(execution_classification=CLASSIFICATION)
    result = bundle.runtime.execute(ASSIGNMENT)
    usage_record = bundle.executor.usage_for(INVOCATION_ID)
    usage = usage_record.get("usage") if isinstance(usage_record, dict) else None
    verification_usage_record = bundle.semantic_verifier.usage_for(VERIFY_INVOCATION_ID)
    verification_usage = verification_usage_record.get("usage") if isinstance(verification_usage_record, dict) else None
    generation_cost = bundle.provider.estimate_cost_cny(usage) if isinstance(usage, dict) else None
    verification_cost = bundle.provider.estimate_cost_cny(verification_usage) if isinstance(verification_usage, dict) else None
    payload = {
        "classification": CLASSIFICATION,
        "real_execution": True,
        "mock": False,
        "stub": False,
        "canonical_binding": result.get("canonical_binding"),
        "runtime_result": result,
        "provider": bundle.provider.provider,
        "model": bundle.provider.model,
        "generation_usage": usage_record,
        "verification_usage": verification_usage_record,
        "cost_cny": {
            "generation": generation_cost,
            "verification": verification_cost,
            "total": round(generation_cost + verification_cost, 8) if generation_cost is not None and verification_cost is not None else None,
        },
        "pricing_basis": bundle.provider.pricing_basis(),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if result.get("runtime_status") == "SUCCESS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
