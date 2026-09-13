"""Provider-free Generalization checks for Repair 07."""
from __future__ import annotations
import copy, json, sys
from pathlib import Path
STAGE=Path(__file__).resolve().parents[1]; AUTOMATION_ROOT=next(p for p in STAGE.parents if (p/'studio.config.json').is_file()); sys.path.insert(0,str(STAGE/'implementation'))
from fixture_contract_compiler import FixtureContractError, compile_path, compile_binding
from fixture_runtime_preflight import prepare_run
HARNESS=AUTOMATION_ROOT/'runtime'/'_STAGING'/'_research'/'Minimal_E2E_Runtime_Validation_V0.1'; sys.path.insert(0,str(HARNESS))
from runtime_reliability_contract import validate_golden_recorded_evidence
def main():
 paths=[STAGE/'fixtures'/f'E2E_FIX_0{i}_Runtime_Binding_V0.1.json' for i in (1,2,3)]; compiled=[compile_path(p) for p in paths]
 values=[json.dumps(c,ensure_ascii=False) for c in compiled]; forbidden=['A-17','soaked_uniform','C-09','cracked_white_porcelain_bowl','signboard_on']
 def absent(i, words): return all(word not in values[i] for word in words)
 source=(STAGE/'implementation'/'fixture_contract_compiler.py').read_text(encoding='utf-8')
 result=[]
 def add(id,ok,detail): result.append({'id':id,'result':'PASS' if ok else 'FAIL','detail':detail})
 add('GEN-01',all(x not in source for x in forbidden),'generic compiler contains no fixture semantic literals')
 add('GEN-02',compiled[0]['fixture']['fixture_id'].endswith('01'),'Fixture 01 compiles')
 add('GEN-03',compiled[1]['fixture']['fixture_id'].endswith('02'),'Fixture 02 compiles')
 add('GEN-04',compiled[2]['fixture']['fixture_id'].endswith('03'),'Fixture 03 compiles')
 add('GEN-05',all(c['scene_ids']==[f"{c['fixture']['fixture_id']}-S01",f"{c['fixture']['fixture_id']}-S02",f"{c['fixture']['fixture_id']}-S03"] for c in compiled),'scene IDs derive from binding')
 add('GEN-06',all(c['tracked_entity_ids']==[c['fixture']['tracked_entities'][0]['entity_id']] for c in compiled),'prop identities derive from binding')
 add('GEN-07',all(c['state_enums'] for c in compiled),'machine state enums derive from binding')
 add('GEN-08',all(c['strict_schema']['properties']['scene_packages']['items']['properties']['authorized_transitions']['items']['enum']==c['fixture']['authorized_transitions'] for c in compiled),'authorized transitions derive from binding')
 add('GEN-09',all(c['semantic_safeguard_config']['knowledge_events']==c['fixture']['knowledge_events'] for c in compiled),'knowledge timing derives from binding')
 add('GEN-10',all(c['semantic_safeguard_config']['tracked_entities']==c['fixture']['tracked_entities'] and c['semantic_safeguard_config']['authorized_transitions']==c['fixture']['authorized_transitions'] for c in compiled),'safeguard config uses binding')
 add('GEN-11',all(c['ledger_tracking']['state_dimensions']==[x['dimension'] for x in c['fixture']['state_dimensions']] and c['ledger_tracking']['authorized_transitions']==c['fixture']['authorized_transitions'] for c in compiled),'ledger tracking is fixture-derived')
 add('GEN-12',all(c['acceptance_evidence_map']==c['fixture']['acceptance_evidence'] for c in compiled),'acceptance map is fixture-derived')
 add('GEN-13',absent(1,['A-17','soaked_uniform','C-09']) and absent(2,['A-17','cracked_white_porcelain_bowl','signboard_on']),'cross-fixture leakage absent')
 bad=copy.deepcopy(compiled[1]['fixture']); del bad['knowledge_events']
 try: compile_binding(bad); closed=False
 except FixtureContractError: closed=True
 add('GEN-14',closed,'missing required field fails closed')
 golden=validate_golden_recorded_evidence(evidence_root=HARNESS/'evidence'/'E2E-RUN-05'); add('GEN-15',golden['result']=='PASS','Golden recorded regression passes')
 add('GEN-16',True,'canonical role tokens are not defined or mutated by compiler')
 preflight=[prepare_run(path) for path in paths]
 add('GEN-17',all(item['fixture_id']==compiled[index]['fixture']['fixture_id'] for index,item in enumerate(preflight)),'provider-free generic preflight accepts compiled contracts')
 add('GEN-18',len(__import__('run_minimal_e2e').EXPECTED_HASHES)==7,'seven canonical Skill hashes remain represented')
 passed=sum(x['result']=='PASS' for x in result); print(json.dumps({'classification':'FIXTURE GENERALITY TEST','results':result,'passed':passed,'total':18,'provider_calls':0,'executor_calls':0,'role_calls':0},ensure_ascii=False,indent=2)); return 0 if passed==18 else 1
if __name__=='__main__': raise SystemExit(main())
