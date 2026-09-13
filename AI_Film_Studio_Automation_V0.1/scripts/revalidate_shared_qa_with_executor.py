"""Re-run the unchanged Shared QA V0.1 pack through the registered real executor."""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.shared_qa.contemporary_handoff_coordinator import ContemporaryHandoffCoordinator
from runtime.shared_qa.contemporary_language_runtime import ContemporaryLanguageRuntime
from runtime.shared_qa.language_voice_qa_binding import create_language_voice_qa_binding
from scripts.run_shared_qa_e2e_validation import FIXTURE_ROOT, GOLD_SUMMARIES, parse_fixture, runtime_envelope

RESULT_ROOT = ROOT / "runtime" / "_TEST_SANDBOX" / "validation" / "results" / "shared_qa" / "v0.1" / "executor_revalidation"
STAGING_ROOT = ROOT / "runtime" / "_STAGING" / "_research" / "Language_Voice_QA_Executor_Binding_Repair_V0.1"
MANIFEST = ROOT / "runtime" / "_STAGING" / "_research" / "Shared_QA_End_to_End_Validation_V0.1" / "03-fixture-manifest.json"


def evidence_records(fixture_id: str) -> List[Dict[str, Any]]:
    if fixture_id == "C01":
        rows = [
            ("xinhua-waic-2026", "新华网", "https://www.news.cn/tech/20260719/30c96f9724774a508baf9efe704ef286/c.html", "B", "XINHUA-WAIC-2026", "2026-07-19T00:00:00Z"),
            ("state-tax-2026", "国家税务总局", "https://www.chinatax.gov.cn/chinatax/n810219/n810724/c5250672/content.html", "A", "STATE-TAX-2026", "2026-06-30T00:00:00Z"),
            ("drc-2026", "国务院发展研究中心", "https://www.drc.gov.cn/DocViewH5.aspx?chnid=379&docid=2910171&leafid=1338", "A", "DRC-2026", "2026-07-28T00:00:00Z"),
        ]
        question_type = "CURRENT_USAGE"
    else:
        rows = [
            ("bjyouth-2025", "北京青年研究", "https://bjqz.cbpt.cnki.net/portal/journal/portal/client/paper/c8db884c87f755dbb454b80c5e267efc", "A", "BJYOUTH-RESEARCH-2025", "2025-11-10T00:00:00Z"),
            ("rmlt-2025", "人民论坛网", "https://www.rmlt.com.cn/2025/0401/726756.shtml", "B", "RMLT-2025", "2025-04-01T00:00:00Z"),
            ("linguistic-2025", "网络流行语班味探析", "https://pdf.hanspub.org/ml_2915237.pdf", "B", "LINGUISTIC-STUDY-2025", "2025-01-01T00:00:00Z"),
        ]
        question_type = "CURRENT_USAGE"
    return [{
        "source_id": source_id, "source_name": name, "source_url": url, "source_tier": tier,
        "independence_group": group, "usage_kind": "NATURAL_USE", "stance": "SUPPORTS",
        "published_at": date, "accessed_at": "2026-08-24T00:00:00Z", "geography": "中国大陆",
        "platform": "public technical communication" if fixture_id == "C01" else "public discussion",
        "register_observation": "R4", "semantic_drift": "NONE", "raw_excerpt": "Source record retained as evidence data only.",
    } for source_id, name, url, tier, group, date in rows], question_type


def one_call(bundle, fixture: Mapping[str, str], envelope: Dict[str, Any], suffix: str) -> Dict[str, Any]:
    data = dict(envelope)
    data["invocation_id"] = f"revalidation-{fixture['fixture_id'].lower()}-{suffix}"
    data["caller"] = f"VALIDATION / SYNTHETIC / NON-CANON / fixture {fixture['fixture_id']}"
    runtime = bundle.runtime.invoke(data)
    invocation_id = runtime["internal_runtime_result"]["invocation_id"]
    usage = bundle.executor.usage_for(invocation_id)
    return {
        "runtime_result": runtime,
        "canonical_semantic_output": bundle.executor.output_for(invocation_id),
        "usage": usage,
        "estimated_cost_cny": bundle.provider.estimate_cost_cny(usage["usage"]) if usage else None,
    }


def execute_fixture(fixture: Mapping[str, str]) -> Dict[str, Any]:
    bundle = create_language_voice_qa_binding(log_dir=RESULT_ROOT / "runtime_audit_logs" / fixture["fixture_id"])
    envelope = runtime_envelope(fixture)
    if fixture["fixture_id"] not in {"C01", "C02"}:
        result = one_call(bundle, fixture, envelope, "initial")
        return {"fixture_id": fixture["fixture_id"], "mode": "DIRECT_RUNTIME", "initial": result, "final": result, "evidence": None}
    records, question_type = evidence_records(fixture["fixture_id"])
    calls: List[Dict[str, Any]] = []
    def qa_call(payload: Dict[str, Any]) -> Dict[str, Any]:
        suffix = "callback" if "contemporary_evidence_return" in payload else "initial"
        record = one_call(bundle, fixture, payload, suffix)
        calls.append(record)
        internal = record["runtime_result"]["internal_runtime_result"]
        if internal["runtime_status"] != "SUCCESS" or record["canonical_semantic_output"] is None:
            raise RuntimeError("Formal Runtime did not yield canonical semantic output")
        return record["canonical_semantic_output"]
    phrase = "具身智能" if fixture["fixture_id"] == "C01" else "班味"
    coordinator = ContemporaryHandoffCoordinator(qa_call, ContemporaryLanguageRuntime(lambda _request: records))
    coordinated = coordinator.run({
        "qa_input": envelope,
        "contemporary_request": {
            "phrase": phrase, "question": fixture["context"], "production_run_id": f"revalidation-{fixture['fixture_id'].lower()}",
            "question_type": question_type, "requested_action": "EVIDENCE_ONLY", "scope": {"geography": "中国大陆"},
            "as_of": "2026-08-24T00:00:00Z",
        },
    })
    final = calls[-1] if calls else None
    return {"fixture_id": fixture["fixture_id"], "mode": "CONTEMPORARY_COORDINATED", "initial": calls[0] if calls else None, "final": final, "evidence": coordinated.get("evidence_result"), "coordinator": coordinated, "calls": calls}


def fixture_hashes_ok() -> bool:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for item in manifest["fixtures"]:
        path = ROOT / item["path"]
        if hashlib.sha256(path.read_bytes()).hexdigest().upper() != item["sha256"]:
            return False
    return True


def review_sheet(fixtures: List[Mapping[str, str]], results: List[Mapping[str, Any]]) -> None:
    by_id = {row["fixture_id"]: row for row in results}
    lines = ["---", "type: human-review-sheet", "status: pending-human-acceptance", "version: 0.1", "---", "", "# Human Review Sheet V0.1｜Real Semantic Revalidation", "", "> 请重点判断：1. 不该改的有没有乱改；2. 人物声音是否被洗平；3. 原意是否变化；4. 真问题是否修好；5. 是否增加 AI 味；6. DeepSeek Provider 质量是否足够。", ""]
    for fixture in fixtures:
        row = by_id[fixture["fixture_id"]]
        final = row["final"]
        semantic = final["canonical_semantic_output"] if final else None
        runtime = final["runtime_result"]["internal_runtime_result"] if final else {}
        revised = semantic.get("revised_text") if isinstance(semantic, Mapping) else None
        lines.extend([f"## Fixture {fixture['fixture_id']}", "", "### Original", "", fixture["text"], "", "### Context", "", fixture["context"], "", "### Real QA Output", "", f"- decision: `{semantic.get('decision') if semantic else None}`", f"- severity: `{semantic.get('severity') if semantic else None}`", f"- route: `{semantic.get('route') if semantic else None}`", f"- diagnosis: {semantic.get('diagnostics') if semantic else None}", f"- detector: `{semantic.get('detector_ownership') if semantic else None}`", f"- meaning lock: `{semantic.get('meaning_lock_status') if semantic else None}`", f"- benefit: `{semantic.get('benefit_result') if semantic else None}`", f"- rewrite scope: `{semantic.get('rewrite_scope') if semantic else None}`", f"- handoff: `{semantic.get('role_handoff') if semantic else None}`", f"- contemporary: `{semantic.get('contemporary_state') if semantic else None}`", f"- Runtime: `{runtime.get('runtime_status')} / {runtime.get('failure_code')}`", f"- token usage: `{final.get('usage') if final else None}`", f"- estimated cost CNY: `{final.get('estimated_cost_cny') if final else None}`", "", "### Revised Text", "", revised or "`NONE — Original retained`", "", "### Diff", "", "`Human review required; no automated acceptance decision.`", "", "### Gold Criteria", "", GOLD_SUMMARIES[fixture["fixture_id"]], "", "### Human Review", "", "- [ ] Accept", "- [ ] Reject", "- [ ] Needs Discussion", "", "### Human Notes", "", ""])
    (STAGING_ROOT / "06-Human_Review_Sheet_V0.1.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    fixtures = [parse_fixture(path) for path in sorted(FIXTURE_ROOT.glob("*.md")) if path.name != "README.md"]
    results = [execute_fixture(fixture) for fixture in fixtures]
    for row in results:
        (RESULT_ROOT / f"{row['fixture_id']}.json").write_text(json.dumps(row, ensure_ascii=False, indent=2), encoding="utf-8")
    review_sheet(fixtures, results)
    successful = sum(1 for row in results if row.get("final") and row["final"]["runtime_result"]["internal_runtime_result"]["runtime_status"] == "SUCCESS")
    handoffs = sum(1 for row in results if row.get("coordinator", {}).get("coordinator_status") == "EVIDENCE_RETURNED_TO_QA")
    costs = [call["estimated_cost_cny"] for row in results for call in row.get("calls", [row.get("final")]) if call and call.get("estimated_cost_cny") is not None]
    report = {"fixtures": len(fixtures), "successful_runtime_results": successful, "contemporary_handoffs_completed": handoffs, "fixture_hashes_ok": fixture_hashes_ok(), "total_estimated_cost_cny": round(sum(costs), 8), "human_acceptance": "PENDING"}
    (RESULT_ROOT / "revalidation-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if successful == len(fixtures) and report["fixture_hashes_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

