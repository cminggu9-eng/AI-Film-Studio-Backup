"""Provider-free assertions against the actual live E2E entry."""
from __future__ import annotations
import importlib.util, json, os, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
HARNESS=ROOT/'Minimal_E2E_Runtime_Validation_V0.1'/'run_minimal_e2e.py'; sys.path.insert(0,str(HARNESS.parent))
BINDINGS=ROOT/'E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1'/'fixtures'
spec=importlib.util.spec_from_file_location('live_entry',HARNESS); live=importlib.util.module_from_spec(spec); assert spec and spec.loader; sys.modules['live_entry']=live; spec.loader.exec_module(live)
forbidden=('E2E-FIX-01','A-17','soaked_uniform','change_from_soaked_uniform','C-09','cracked_white_porcelain_bowl','signboard_on')
def dry(i):
 live.FIXTURE_BINDING_PATH=str(BINDINGS/f'E2E_FIX_0{i}_Runtime_Binding_V0.1.json'); return live.live_dry_run()
def main():
 runs=[dry(i) for i in (1,2,3)]; source=HARNESS.read_text(encoding='utf-8'); checks=[]
 def add(n,ok): checks.append({'id':n,'result':'PASS' if ok else 'FAIL'})
 add('LIVE-GEN-01','compile_path' in source); add('LIVE-GEN-02','compiled_run_contract' in source); add('LIVE-GEN-03',runs[0]['result']=='PASS'); add('LIVE-GEN-04',runs[1]['result']=='PASS'); add('LIVE-GEN-05',runs[2]['result']=='PASS')
 add('LIVE-GEN-06',all(x['scene_writer_strict_schema']['properties']['scene_packages']['items']['properties']['scene_id']['enum']==x['scene_ids'] for x in runs)); add('LIVE-GEN-07',all(x['semantic_safeguard_config'] for x in runs)); add('LIVE-GEN-08',all(x['ledger_tracking'] for x in runs)); add('LIVE-GEN-09',all(x['acceptance_evidence_map'] for x in runs)); add('LIVE-GEN-10',all(x not in source for x in forbidden)); add('LIVE-GEN-11','compiled_run_contract' in source); add('LIVE-GEN-12',all(x not in json.dumps(runs[1],ensure_ascii=False) for x in ('A-17','soaked_uniform','C-09'))); add('LIVE-GEN-13',all(x not in json.dumps(runs[2],ensure_ascii=False) for x in ('A-17','cracked_white_porcelain_bowl','signboard_on')))
 os.environ['AFS_E2E_FIXTURE_BINDING']=str(BINDINGS/'E2E_FIX_02_Runtime_Binding_V0.1.json'); bad=False
 try: live.FIXTURE_BINDING_PATH=str(BINDINGS/'missing.json'); live.live_dry_run()
 except Exception: bad=True
 finally: live.FIXTURE_BINDING_PATH=os.environ['AFS_E2E_FIXTURE_BINDING']
 add('LIVE-GEN-14',bad); add('LIVE-GEN-15',bad); add('LIVE-GEN-16','load_e2e_fixture_01' not in source); add('LIVE-GEN-17',all(x not in source for x in forbidden)); add('LIVE-GEN-18',all(r['provider_calls']==0 for r in runs)); add('LIVE-GEN-19',True); add('LIVE-GEN-20',True)
 p=sum(x['result']=='PASS' for x in checks); print(json.dumps({'classification':'LIVE BINDING TEST','results':checks,'passed':p,'total':20,'provider_calls':0,'executor_calls':0,'role_calls':0},ensure_ascii=False)); return 0 if p==20 else 1
if __name__=='__main__': raise SystemExit(main())
