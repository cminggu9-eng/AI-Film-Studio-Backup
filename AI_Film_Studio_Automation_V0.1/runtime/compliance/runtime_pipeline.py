"""Observable Router -> Gate runtime adapter used by production-runtime tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

from runtime.compliance.compliance_gate import build_runtime_record, gate_candidate, gate_with_correction, load_rules, write_compliance_log
from scripts.showrunner_role_router import route_request


def run_runtime(request: str, candidate_v1_text: str, *, candidate_v2_text: Optional[str] = None, project_state: str = "DRAFT", log_dir: Optional[Path] = None) -> Dict[str, Any]:
    rules = load_rules()
    route = route_request(request, rules)
    base: Dict[str, Any] = {
        "task": request,
        "routed_role": route["routed_role"],
        "skill_name": route.get("skill_name"),
        "skill_path": route.get("skill_path"),
        "mode": route["mode"],
        "output_type": route["output_type"],
        "activated_modules": route["activated_modules"],
        "boundary_contract": route.get("boundary_contract"),
        "project_state": project_state,
    }
    candidate_v1 = dict(base, candidate_version="V1", candidate_output=candidate_v1_text)
    gate_v1 = gate_candidate(candidate_v1, rules)
    candidate_v2 = dict(base, candidate_version="V2", candidate_output=candidate_v2_text) if candidate_v2_text is not None else None
    gate_v2 = gate_candidate(candidate_v2, rules) if candidate_v2 is not None else None
    final_gate = gate_with_correction(candidate_v1, candidate_v2, rules)
    record = build_runtime_record(candidate_v1, gate_v1, candidate_v2, gate_v2, final_gate["final_delivery_status"])
    record.update({"router": route, "gate_final": final_gate})
    record["log_path"] = str(write_compliance_log(record, log_dir))
    return record
