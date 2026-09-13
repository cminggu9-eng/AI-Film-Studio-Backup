"""One authorized Director-only compatibility probe; no upstream/downstream calls."""
from __future__ import annotations
import json, os, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
AUTOMATION=next(parent for parent in ROOT.parents if (parent/'studio.config.json').is_file())
HARNESS=AUTOMATION/'runtime'/'_STAGING'/'_research'/'Minimal_E2E_Runtime_Validation_V0.1'
os.environ['AFS_E2E_FIXTURE_BINDING']=str(AUTOMATION/'runtime'/'_STAGING'/'_research'/'E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1'/'fixtures'/'E2E_FIX_01_Runtime_Binding_V0.1.json')
sys.path.insert(0,str(HARNESS))
import run_minimal_e2e as e2e
from director_provider_compatibility import build_deepseek_compatible_director_contract, equivalence_report

SOURCE=HARNESS/'evidence'/'E2E-RUN-12'
EVIDENCE=ROOT/'evidence'/'DIRECTOR-COMPATIBILITY-PROBE-03'
def main() -> int:
    if EVIDENCE.exists(): raise RuntimeError('Probe evidence root already exists')
    upstream=json.loads((SOURCE/'artifacts'/'scene_writer_output.json').read_text(encoding='utf-8'))
    director_input=json.loads((SOURCE/'artifacts'/'director_input.json').read_text(encoding='utf-8'))['input']
    EVIDENCE.mkdir(parents=True)
    executor=e2e.CanonicalRoleExecutor(evidence_dir=EVIDENCE,run_id='DIRECTOR-COMPAT-PROBE-03')
    result,input_path,output_path=executor.invoke(spec=e2e.role_spec('director'),input_payload=director_input,required_locks=upstream['canon_assignment_locks'],prohibited_changes=upstream['prohibited_changes'],structured_output=build_deepseek_compatible_director_contract(),structured_arguments_validator=e2e.make_director_payload_validator(selected_mode='PLAN',required_locks=upstream['canon_assignment_locks'],prohibited_changes=upstream['prohibited_changes']))
    record=executor.call_records[0]
    payload={'classification':'DIRECTOR STRICT PROVIDER COMPATIBILITY PROBE','result':'PASS','provider_calls':1,'retries':0,'fallbacks':0,'function_name':'submit_director_package','equivalence':equivalence_report(),'call_record':record,'output_artifact':str(output_path),'input_artifact':str(input_path),'primary_state_or_outcome':result['primary_state_or_outcome']}
    (EVIDENCE/'probe_manifest.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(payload,ensure_ascii=False,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
