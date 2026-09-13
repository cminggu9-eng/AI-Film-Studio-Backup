"""TR-SW-01..20 for the authorised Scene Writer Targeted Repair V0.1.

Only TR-SW-17 and TR-SW-18 call the real provider. They replay frozen existing
outputs through the verifier and never generate or resample a scene.
"""

from __future__ import annotations

import ast
import copy
import inspect
import json
import os
import sys
from pathlib import Path
from typing import Any, Callable, Dict


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
for path in (str(STAGE), str(AUTOMATION_ROOT)):
    if path not in sys.path:
        sys.path.insert(0, path)

from runtime.compliance.compliance_gate import sha256_file  # noqa: E402
from runtime.scene_writer.execution_projection import execution_projection_for_mode, state_projection_matrix  # noqa: E402
from runtime.scene_writer.scene_writer_executor import CanonicalSceneWriterExecutor  # noqa: E402
from runtime.scene_writer.scene_writer_executor_binding import SceneWriterCanonicalBinding, create_scene_writer_binding  # noqa: E402
from runtime.scene_writer.scene_writer_runtime import SceneWriterRuntime  # noqa: E402
from runtime.scene_writer.semantic_assignment_integrity import (  # noqa: E402
    SemanticAssignmentIntegrityVerifier,
    build_assignment_constraint_ledger,
)


EXPECTED_HASH = "93e1be12988f8caa6cdd76acb5e6c1bf6ad3ca0dff5806a2ea93511e66052dfb"
RESULT_PATH = STAGE / "Scene_Writer_Targeted_Repair_TR_SW_Results_V0.1.json"
RAW_FULL = STAGE / "Full_Semantic_Validation_Raw_Results_V0.1"
SMOKE_RAW = STAGE / "SMOKE_SW_EXEC_01_Semantic_Assignment_Integrity_Raw_Result_V0.1.json"


def assignment(request_id: str, mode: str = "CREATE", scene_id: str = "TR-SW") -> Dict[str, Any]:
    return {
        "request_id": request_id,
        "requested_mode": mode,
        "output_language": "en-US",
        "project_id": "TR-SW-SYNTHETIC",
        "episode_id": "TR-SW-EP01",
        "scene_id": scene_id,
        "scene_request": "Synthetic transport contract exercise only.",
        "scene_purpose": "Validate Runtime execution projection only.",
        "repair_target": "No story generation is performed.",
        "canon_locks": ["Only the supplied assignment is authoritative.", "The cause of the supplied fact is unknown."],
        "showrunner_locks": [],
        "participants": [
            {"name": "A", "role": "participant", "knowledge": "A knows the supplied fact.", "constraint": "Do not add history."},
            {"name": "B", "role": "participant", "knowledge": "B does not know the supplied fact at scene entry.", "constraint": "B learns it only after disclosure."},
        ],
        "character_context": {"relationship": "colleagues", "creative_freedom": "Immediate action and dialogue tactics only."},
        "required_event": "A discloses the supplied fact to B.",
        "required_information": "The supplied fact is disclosed during the scene.",
        "required_outcome": "B can respond after disclosure.",
        "prior_scene_state": "A knows the fact; B does not yet know it.",
        "desired_post_state": "B knows the disclosed fact.",
        "production_constraints": None,
        "requested_form": "No story generation is performed.",
        "downstream_requests": [],
        "qa_requests": [],
    }


def handoff() -> Dict[str, Any]:
    return {
        "target_owner": "Showrunner",
        "reason": "An authorised upstream decision is required.",
        "relevant_locks": ["Only the supplied assignment is authoritative."],
        "scene_function": "Report the bounded decision request.",
        "decision_needed": "Choose the authorised story decision.",
        "scene_writer_did_not_decide": "The upstream story decision.",
    }


def valid_output(state: str, mode: str) -> Dict[str, Any]:
    control: Dict[str, Any] = {"primary_state": state, "flags": [], "handoffs": []}
    creative: Dict[str, str] | None = None
    if state == "SCENE_CREATED":
        creative = {"kind": "scene", "content": "A gives B the supplied notice. B reads it after receiving it."}
        control["scene_function"] = "A disclosure changes B's information state."
    elif state == "SCENE_REVISED":
        creative = {"kind": "revision", "content": "A asks. B pauses, then makes a present-tense condition."}
        control["scene_function"] = "A local revision adds resistance without new facts."
    elif state == "NO_MATERIAL_CHANGE":
        control["material_rewrite_claimed"] = False
        if mode == "DIAGNOSE":
            control["diagnosis_summary"] = "The supplied text lacks a playable resistance and turn."
    elif state == "NEEDS_CONTEXT":
        control["material_missing_context"] = {
            "missing": "Participants, a scene event, and a desired outcome.",
            "why_material": "Without them, a scene would require invented story facts.",
            "target_owner": "Showrunner",
        }
    elif state == "UPSTREAM_DECISION_REQUIRED":
        control["flags"] = ["UPSTREAM_HANDOFF_REQUIRED"]
        control["handoffs"] = [handoff()]
        control["upstream_decision_needed"] = "Decide whether the protected fact may be disclosed."
    elif state == "REQUEST_OUT_OF_SCOPE":
        control["out_of_scope_boundary"] = "The requested role-substitution work is outside Scene Writer authority."
    else:
        raise ValueError(state)
    return {"creative_deliverable": creative, "control_data": control}


def sandbox_result(case_id: str, state: str, mode: str) -> Dict[str, Any]:
    output = valid_output(state, mode)
    runtime = SceneWriterRuntime(synthetic_executor=lambda _: copy.deepcopy(output), test_sandbox=True)
    response = runtime.execute(assignment(case_id, mode, case_id))
    assert response["runtime_status"] == "SUCCESS", response
    return response


def run_case(case_id: str, function: Callable[[], Any]) -> Dict[str, Any]:
    try:
        detail = function()
        return {"id": case_id, "result": "PASS", "detail": detail}
    except Exception as exc:  # Every test must leave an auditable failure rather than stop the matrix.
        return {"id": case_id, "result": "FAIL", "detail": f"{type(exc).__name__}: {exc}"}


def request_prompt(mode: str = "CREATE") -> tuple[Any, Dict[str, Any]]:
    binding = SceneWriterCanonicalBinding.load()
    executor = CanonicalSceneWriterExecutor(
        skill_path=binding.canonical_path,
        expected_sha256=binding.sha256,
        model_executor=object(),  # _request is inspected only; no provider call occurs.
        model="test-model",
        thinking_mode="disabled",
    )
    payload = assignment("TR-PROMPT-" + mode, mode, "TR-PROMPT")
    ledger = build_assignment_constraint_ledger(payload)
    model_request = executor._request(payload, {
        "contract_identity": "scene-writer-runtime",
        "contract_version": "0.1",
        "classification": "SYNTHETIC / NON-CANON / NON-SEMANTIC",
        "output_language": "en-US",
        "output_language_resolution": "EXPLICIT",
        "assignment_constraint_ledger": ledger,
    })
    return model_request, ledger


def full_replay_case(fixture_id: str) -> Dict[str, Any]:
    raw = json.loads((RAW_FULL / f"{fixture_id}_raw_result.json").read_text(encoding="utf-8"))
    runtime_result = raw["runtime_result"]
    scene_writer = runtime_result["scene_writer"]
    if not isinstance(scene_writer, dict):
        raise ValueError(f"{fixture_id} has no frozen accepted Scene Writer output")
    return {
        "id": fixture_id,
        "assignment": raw["assignment"],
        "creative": scene_writer["creative_deliverable"],
        "control": scene_writer["control_data"],
    }


def smoke_replay_case() -> Dict[str, Any]:
    smoke = json.loads(SMOKE_RAW.read_text(encoding="utf-8"))
    scene_writer = smoke["runtime_result"]["scene_writer"]
    smoke_source = (STAGE / "tests" / "run_smoke_sw_exec_01.py").read_text(encoding="utf-8")
    smoke_assignment = None
    parsed_source = ast.parse(smoke_source)
    literal_names: Dict[str, Any] = {}
    for statement in parsed_source.body:
        if isinstance(statement, ast.Assign) and len(statement.targets) == 1 and isinstance(statement.targets[0], ast.Name):
            try:
                literal_names[statement.targets[0].id] = ast.literal_eval(statement.value)
            except ValueError:
                pass

    class _LiteralNameResolver(ast.NodeTransformer):
        def visit_Name(self, node: ast.Name) -> ast.AST:
            if node.id in literal_names:
                return ast.copy_location(ast.Constant(literal_names[node.id]), node)
            return node

    for statement in parsed_source.body:
        if isinstance(statement, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "assignment" for target in statement.targets):
            smoke_assignment = ast.literal_eval(_LiteralNameResolver().visit(copy.deepcopy(statement.value)))
            break
    if not isinstance(smoke_assignment, dict):
        raise ValueError("Frozen Smoke assignment literal is unavailable without executing its runner")
    return {
        "id": "SMOKE-SW-EXEC-01",
        "assignment": copy.deepcopy(smoke_assignment),
        "creative": scene_writer["creative_deliverable"],
        "control": scene_writer["control_data"],
    }


def verifier_replay(bundle: Any, case: Dict[str, Any], group: str) -> Dict[str, Any]:
    invocation_id = f"targeted-repair-replay:{group}:{case['id']}"
    response = bundle.semantic_verifier({
        "assignment_constraint_ledger": build_assignment_constraint_ledger(case["assignment"]),
        "generated_creative_deliverable": copy.deepcopy(case["creative"]),
        "relevant_control_data": copy.deepcopy(case["control"]),
        "runtime": {"invocation_id": invocation_id, "classification": "TARGETED REPAIR / FROZEN OUTPUT / VERIFIER-ONLY"},
    })
    usage = bundle.semantic_verifier.usage_for(invocation_id)
    adjudication_usage = bundle.semantic_verifier.adjudication_usage_for(invocation_id)
    usage_records = [record for record in (usage, adjudication_usage) if isinstance(record, dict)]
    estimated_cost = sum(
        bundle.provider.estimate_cost_cny(record["usage"])
        for record in usage_records
        if isinstance(record.get("usage"), dict)
    )
    return {
        "id": case["id"],
        "response": response,
        "claim_audit": bundle.semantic_verifier.claim_audit_for(invocation_id),
        "usage": usage,
        "adjudication_usage": adjudication_usage,
        "estimated_cost_cny": round(estimated_cost, 8) if usage_records else None,
    }


def main() -> int:
    result_path = Path(os.environ.get("TR_SW_RESULT_PATH", str(RESULT_PATH)))
    if result_path.exists():
        raise RuntimeError(f"Targeted Repair test evidence already exists: {result_path}")

    results: list[Dict[str, Any]] = []

    def create_projection() -> str:
        projection = execution_projection_for_mode("CREATE")
        assert projection["permitted_primary_states"] == ["SCENE_CREATED", "NEEDS_CONTEXT", "UPSTREAM_DECISION_REQUIRED", "REQUEST_OUT_OF_SCOPE"], projection
        assert "SCENE_REVISED" not in projection["states"], projection
        return "CREATE allows success and lawful non-creative boundary states"
    results.append(run_case("TR-SW-01", create_projection))

    def revise_projection() -> str:
        projection = execution_projection_for_mode("REVISE")
        assert projection["permitted_primary_states"] == ["SCENE_REVISED", "NO_MATERIAL_CHANGE", "NEEDS_CONTEXT", "UPSTREAM_DECISION_REQUIRED", "REQUEST_OUT_OF_SCOPE"], projection
        return "REVISE projection permits local revision or lawful non-creative states"
    results.append(run_case("TR-SW-02", revise_projection))

    def no_material_projection() -> str:
        details = state_projection_matrix()["NO_MATERIAL_CHANGE"]
        assert details["creative_deliverable"] == "required null" and "material_rewrite_claimed=false" in details["required_control_fields"], details
        response = sandbox_result("TR-SW-03", "NO_MATERIAL_CHANGE", "REVISE")
        assert response["scene_writer"]["creative_deliverable"] is None, response
        return "NO_MATERIAL_CHANGE validates with null creative and false rewrite claim"
    results.append(run_case("TR-SW-03", no_material_projection))

    def diagnose_no_rewrite() -> str:
        response = sandbox_result("TR-SW-04", "NO_MATERIAL_CHANGE", "DIAGNOSE")
        assert response["scene_writer"]["creative_deliverable"] is None, response
        invalid = valid_output("NO_MATERIAL_CHANGE", "DIAGNOSE")
        invalid["creative_deliverable"] = {"kind": "scene", "content": "Replacement scene."}
        runtime = SceneWriterRuntime(synthetic_executor=lambda _: copy.deepcopy(invalid), test_sandbox=True)
        rejected = runtime.execute(assignment("TR-SW-04-INVALID", "DIAGNOSE", "TR-SW-04"))
        assert rejected["runtime_status"] == "FAIL_SAFE", rejected
        return "DIAGNOSE accepts diagnosis-only packet and rejects a replacement scene"
    results.append(run_case("TR-SW-04", diagnose_no_rewrite))

    results.append(run_case("TR-SW-05", lambda: "NEEDS_CONTEXT accepts no creative deliverable" if sandbox_result("TR-SW-05", "NEEDS_CONTEXT", "CREATE")["scene_writer"]["creative_deliverable"] is None else (_ for _ in ()).throw(AssertionError("creative present"))))
    results.append(run_case("TR-SW-06", lambda: "UPSTREAM_DECISION_REQUIRED accepts no creative deliverable" if sandbox_result("TR-SW-06", "UPSTREAM_DECISION_REQUIRED", "CREATE")["scene_writer"]["creative_deliverable"] is None else (_ for _ in ()).throw(AssertionError("creative present"))))
    results.append(run_case("TR-SW-07", lambda: "REQUEST_OUT_OF_SCOPE accepts non-creative boundary packet" if sandbox_result("TR-SW-07", "REQUEST_OUT_OF_SCOPE", "CREATE")["scene_writer"]["creative_deliverable"] is None else (_ for _ in ()).throw(AssertionError("creative present"))))

    def state_required_fields() -> str:
        cases = [
            ("SCENE_CREATED", "CREATE"), ("SCENE_REVISED", "REVISE"), ("NO_MATERIAL_CHANGE", "REVISE"),
            ("NEEDS_CONTEXT", "CREATE"), ("UPSTREAM_DECISION_REQUIRED", "CREATE"), ("REQUEST_OUT_OF_SCOPE", "CREATE"),
        ]
        for index, (state, mode) in enumerate(cases, start=1):
            sandbox_result(f"TR-SW-08-{index}", state, mode)
        return "all six state packets satisfy their required Runtime fields"
    results.append(run_case("TR-SW-08", state_required_fields))

    def state_forbidden_fields() -> str:
        cases = [
            ("SCENE_CREATED", "CREATE", "material_rewrite_claimed", False),
            ("SCENE_REVISED", "REVISE", "upstream_decision_needed", "unexpected decision"),
            ("NO_MATERIAL_CHANGE", "REVISE", "out_of_scope_boundary", "unexpected boundary"),
            ("NEEDS_CONTEXT", "CREATE", "upstream_decision_needed", "unexpected decision"),
            ("UPSTREAM_DECISION_REQUIRED", "CREATE", "material_missing_context", {"missing": "x"}),
            ("REQUEST_OUT_OF_SCOPE", "CREATE", "upstream_decision_needed", "unexpected decision"),
        ]
        for index, (state, mode, field, value) in enumerate(cases, start=1):
            output = valid_output(state, mode)
            output["control_data"][field] = value
            runtime = SceneWriterRuntime(synthetic_executor=lambda _, frozen=output: copy.deepcopy(frozen), test_sandbox=True)
            response = runtime.execute(assignment(f"TR-SW-09-{index}", mode, f"TR-SW-09-{index}"))
            assert response["runtime_status"] == "FAIL_SAFE", (state, response)
        return "all six non-null forbidden-field cases fail safe"
    results.append(run_case("TR-SW-09", state_forbidden_fields))

    def ledger_injected() -> str:
        model_request, ledger = request_prompt()
        transported = json.loads(model_request.user_prompt)["execution_metadata"]["assignment_constraint_ledger"]
        required = {
            "LOCKED_FACTS", "EXPLICIT_UNKNOWNS", "CHARACTER_KNOWLEDGE_LIMITS", "TEMPORAL_CONSTRAINTS",
            "RELATIONSHIP_CONSTRAINTS", "CAPABILITY_CONSTRAINTS", "REQUIRED_EVENTS", "REQUIRED_INFORMATION",
            "REQUIRED_OUTCOME", "OPEN_CREATIVE_SPACE",
        }
        assert required <= set(ledger) <= set(transported), transported
        assert "BINDING GENERATION AUTHORITY" in model_request.system_prompt, model_request.system_prompt
        return "all named constraint domains are structurally injected into generation request"
    results.append(run_case("TR-SW-10", ledger_injected))

    def unknown_preservation() -> str:
        model_request, ledger = request_prompt()
        assert ledger["EXPLICIT_UNKNOWNS"], ledger
        assert "never authorizes" in model_request.system_prompt and "explicit unknown" in model_request.system_prompt.lower(), model_request.system_prompt
        return "explicit unknowns are carried by ledger and barred from concretization"
    results.append(run_case("TR-SW-11", unknown_preservation))

    def knowledge_timing() -> str:
        model_request, ledger = request_prompt()
        timing = ledger["KNOWLEDGE_TIMING"]
        assert {"world_facts", "knowledge_at_scene_entry", "explicit_not_yet_known_or_unknown", "discovery_during_scene"} <= set(timing), timing
        assert "CHARACTER KNOWLEDGE TIMING GATE" in model_request.system_prompt, model_request.system_prompt
        return "world fact, entry knowledge, unknown, and in-scene discovery timing are distinct"
    results.append(run_case("TR-SW-12", knowledge_timing))

    results.append(run_case("TR-SW-13", lambda: "generation prompt prohibits capability ranking" if "capability ranking" in request_prompt()[0].system_prompt else (_ for _ in ()).throw(AssertionError("missing capability gate"))))
    results.append(run_case("TR-SW-14", lambda: "generation prompt prohibits pre-existing obligation" if "pre-existing obligation" in request_prompt()[0].system_prompt else (_ for _ in ()).throw(AssertionError("missing obligation gate"))))
    results.append(run_case("TR-SW-15", lambda: "generation prompt permits a present scene-local proposal" if "conditional proposal made now" in request_prompt()[0].system_prompt else (_ for _ in ()).throw(AssertionError("missing proposal distinction"))))
    results.append(run_case("TR-SW-16", lambda: "REVISE prompt carries a fact-expansion ceiling" if "fact-expansion ceiling" in request_prompt("REVISE")[0].system_prompt else (_ for _ in ()).throw(AssertionError("missing revision ceiling"))))

    replay_details: Dict[str, Any] = {"known_bad": [], "known_clean": [], "provider_called": False}

    def known_bad_replay() -> str:
        if not os.environ.get("DEEPSEEK_API_KEY", "").strip():
            raise RuntimeError("DEEPSEEK_API_KEY is unavailable; verifier replay cannot be performed")
        bundle = create_scene_writer_binding(execution_classification="TARGETED REPAIR / FROZEN OUTPUT / VERIFIER-ONLY")
        cases = [full_replay_case("F03"), full_replay_case("F09"), full_replay_case("F10"), full_replay_case("F14"), smoke_replay_case()]
        reports = [verifier_replay(bundle, case, "known-bad") for case in cases]
        for report in reports:
            assert report["response"]["integrity_result"] == "FAIL", report
        f09 = next(report for report in reports if report["id"] == "F09")
        assert "CHARACTER_KNOWLEDGE_TIMING_DRIFT" in [item["category"] for item in f09["response"]["violations"]], f09
        replay_details["known_bad"] = reports
        replay_details["provider_called"] = True
        return "all five frozen human-fail outputs are detected; F09 is classified as knowledge-timing drift"
    results.append(run_case("TR-SW-17", known_bad_replay))

    def clean_replay() -> str:
        if not os.environ.get("DEEPSEEK_API_KEY", "").strip():
            raise RuntimeError("DEEPSEEK_API_KEY is unavailable; verifier replay cannot be performed")
        bundle = create_scene_writer_binding(execution_classification="TARGETED REPAIR / FROZEN OUTPUT / VERIFIER-ONLY")
        reports = [verifier_replay(bundle, full_replay_case(fixture_id), "known-clean") for fixture_id in ("F04", "F05", "F07", "F08")]
        for report in reports:
            assert report["response"]["integrity_result"] == "PASS", report
        replay_details["known_clean"] = reports
        replay_details["provider_called"] = True
        return "four frozen human-clean outputs remain PASS"
    results.append(run_case("TR-SW-18", clean_replay))

    def no_lexical_arms_race() -> str:
        source = inspect.getsource(SemanticAssignmentIntegrityVerifier)
        assert "re.search(" not in source and "re.compile(" not in source, source
        assert "CLAIM-TO-LEDGER COMPARISON" in source and "keyword list" in source, source
        return "recall repair is prompt-level claim comparison, not a lexical catalogue"
    results.append(run_case("TR-SW-19", no_lexical_arms_race))

    results.append(run_case("TR-SW-20", lambda: "canonical hash unchanged" if sha256_file(SceneWriterRuntime().canonical_skill_path).lower() == EXPECTED_HASH else (_ for _ in ()).throw(AssertionError("canonical hash changed"))))

    report = {
        "classification": "TARGETED REPAIR / STAGING / SYNTHETIC / NON-CANON; TR-SW-17/18 ARE FROZEN-OUTPUT VERIFIER-ONLY REAL PROVIDER REPLAYS",
        "result_policy": "ALL 20 REQUIRED",
        "results": results,
        "passed": sum(item["result"] == "PASS" for item in results),
        "total": len(results),
        "replay_details": replay_details,
    }
    result_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] == report["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
