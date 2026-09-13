"""One provider-free mandatory preflight and regression pass for Repair22."""
from __future__ import annotations
import json, os, subprocess, sys
from pathlib import Path
from repair22_support import ROOT, RESEARCH
import run_minimal_e2e as e2e

def invoke(script: Path):
    p=subprocess.run([sys.executable,"-X","utf8","-B",str(script)],cwd=str(ROOT),capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return p.returncode,json.loads(p.stdout)
    except json.JSONDecodeError: return p.returncode,{"stdout_tail":p.stdout[-2000:],"stderr_tail":p.stderr[-2000:]}
def main():
    for key in tuple(os.environ):
        if key.upper().startswith("AFS_E2E_"): os.environ.pop(key)
    preflight=e2e.rerun_preflight()
    generic_code,generic=invoke(RESEARCH/"E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1"/"tests"/"run_fixture_generality_tests.py")
    phase_code,phase=invoke(RESEARCH/"Systemic_Hardening_Phase_2_Runtime_Reliability_Regression_Enforcement_V0.1"/"run_systemic_regression_gate.py")
    result={"classification":"REPAIR22 OFFLINE GATE RUN","mandatory_preflight":{"passed":preflight.get("passed") is True,"suite_count":len(preflight.get("required_suites",{}))},"genericity":{"returncode":generic_code,"passed":generic.get("passed"),"total":generic.get("total")},"unified_phase2":{"returncode":phase_code,"overall":phase.get("overall"),"record_count":len(phase.get("records",[]))},"provider_calls":0,"executor_calls":0,"role_calls":0,"live_e2e_runs":0}
    result["overall"]="PASS" if result["mandatory_preflight"]=={"passed":True,"suite_count":15} and result["genericity"]=={"returncode":0,"passed":18,"total":18} and result["unified_phase2"]=={"returncode":0,"overall":"PASS","record_count":25} else "FAIL"
    print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if result["overall"]=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
