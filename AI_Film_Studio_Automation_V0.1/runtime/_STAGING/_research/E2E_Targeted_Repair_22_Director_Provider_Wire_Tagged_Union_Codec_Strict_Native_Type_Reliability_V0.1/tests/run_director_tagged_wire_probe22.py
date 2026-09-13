"""The single authorized Director-only Probe22; no retry, fallback, or R03 restart."""
from __future__ import annotations
import copy, json
from pathlib import Path
from repair22_support import *
from director_provider_compatibility import build_deepseek_compatible_director_contract, decode_director_provider_wire_arguments, validate_director_provider_wire_arguments

PROBE_ID="DIRECTOR-TAGGED-WIRE-PROBE-22-F03"
ROOT_OUT=Path(__file__).resolve().parents[1]/"reports"/PROBE_ID
SOURCE=R26_ARTIFACTS/"director_input.json"
def main():
    if ROOT_OUT.exists():
        print(json.dumps({"probe_id":PROBE_ID,"overall":"BLOCKED","detail":"existing evidence prohibits a second provider probe","provider_calls":0},ensure_ascii=False)); return 1
    compiled,contract=state_contract(); source=read(SOURCE); scene=read(R26_ARTIFACTS/"scene_writer_output.json")
    skill,skill_hash=e2e.canonical_skill(e2e.role_spec("director"))
    report={"classification":"DIRECTOR DEEPSEEK TAGGED WIRE PROBE 22","probe_id":PROBE_ID,"source_run":"E2E-RUN-26","source_input":str(SOURCE.resolve()),"source_input_sha256":sha(SOURCE),"provider_calls":1,"retry_count":0,"fallback_count":0,"r03_restarted":False,"strict_function_name":"submit_director_package","codec_id":"DIRECTOR_DEEPSEEK_TAGGED_UNION_CODEC_V1"}
    executor=e2e.CanonicalRoleExecutor(evidence_dir=ROOT_OUT,run_id=PROBE_ID)
    try:
        result,input_path,output_path=executor.invoke(spec=e2e.role_spec("director"),input_payload=copy.deepcopy(source["input"]),required_locks=scene["canon_assignment_locks"],prohibited_changes=scene["prohibited_changes"],structured_output=build_deepseek_compatible_director_contract(contract),wire_arguments_validator=lambda args: validate_director_provider_wire_arguments(args,contract),wire_arguments_decoder=lambda args: decode_director_provider_wire_arguments(args,contract),structured_arguments_validator=canonical_validator(contract),director_state_contract=contract)
        call=executor.call_records[0]; report.update({"overall":"PASS","call_record":call,"input_artifact":str(input_path),"output_artifact":str(output_path),"wire_schema_validated":call["structured_transport"].get("provider_wire_schema_validated") is True,"wire_decoded":call["structured_transport"].get("provider_wire_decoded") is True,"canonical_validated":call["structured_transport"].get("schema_validated") is True,"decoded_unresolved_type":type(result["unresolved_decisions"]).__name__,"decoded_unresolved_value":result["unresolved_decisions"]})
    except Exception as exc:
        call=executor.call_records[0] if executor.call_records else {}; category=getattr(exc,"category","DIRECTOR PROVIDER-WIRE STRICT CONFORMANCE FAILURE")
        report.update({"overall":"FAIL","failure_category":category,"failure":f"{type(exc).__name__}: {exc}","call_record":call,"raw_first_persisted":bool(call.get("raw_response_artifact")),"retry_performed":False})
    e2e.write_json(ROOT_OUT/"Director_DeepSeek_Tagged_Wire_Probe_22.json",report); print(json.dumps(report,ensure_ascii=False,indent=2)); return 0 if report["overall"]=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
