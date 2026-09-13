"""Offline positive/negative proof for the Repair22 Director provider-wire codec."""
from __future__ import annotations
import copy, json
from pathlib import Path
from repair22_support import *
from director_provider_compatibility import DirectorProviderWireError, decode_director_provider_wire_arguments, validate_director_provider_wire_arguments

OUT=Path(__file__).resolve().parents[1]/"reports"/"Repair22_Codec_Test_Results.json"
def rejected(payload, contract):
    try: validate_director_provider_wire_arguments(payload, contract)
    except DirectorProviderWireError: return True
    return False
def main():
    compiled, contract=state_contract(); audit=projection_audit(contract); canonical=canonical_fixture(); validator=canonical_validator(contract)
    present=wire_fixture(contract); absent=wire_fixture(contract,"ABSENT",[]); empty=wire_fixture(contract,"PRESENT",[])
    decoded_present=decode_director_provider_wire_arguments(validate_director_provider_wire_arguments(present,contract),contract)
    decoded_absent=decode_director_provider_wire_arguments(validate_director_provider_wire_arguments(absent,contract),contract)
    decoded_empty=decode_director_provider_wire_arguments(validate_director_provider_wire_arguments(empty,contract),contract)
    r26=outer_arguments(R26_ARTIFACTS/"director_provider_response.json"); probe21=outer_arguments(PROBE21)
    bad=[]
    for label, mut in (("r26_string",r26),("probe21_string",probe21),("absent_nonempty",wire_fixture(contract,"ABSENT",["x"])),("present_string",wire_fixture(contract,"PRESENT","[x]")),("missing_status",wire_fixture(contract)),("missing_items",wire_fixture(contract)),("unknown_status",wire_fixture(contract,"UNKNOWN",[]))):
        p=copy.deepcopy(mut)
        if label=="missing_status": p["unresolved_decisions"].pop("status")
        if label=="missing_items": p["unresolved_decisions"].pop("items")
        bad.append((label,rejected(p,contract)))
    positive={
      "canonical_15_fields_unchanged": set(audit["canonical"]["required"])==set(canonical),
      "only_approved_field_tagged": audit["manifest"]["tagged_union_fields"]==["unresolved_decisions"],
      "wire_is_fixed_object": audit["wire"]["properties"]["unresolved_decisions"]=={"type":"object","additionalProperties":False,"required":["status","items"],"properties":{"status":{"type":"string","enum":["ABSENT","PRESENT"]},"items":{"type":"array","items":{"type":"string"}}}},
      "present_round_trip": decoded_present["unresolved_decisions"]==["unresolved-decision"],
      "absent_round_trip": decoded_absent["unresolved_decisions"]=="ABSENT",
      "empty_round_trip": decoded_empty["unresolved_decisions"]==[],
      "absent_not_empty": decoded_absent["unresolved_decisions"]!=decoded_empty["unresolved_decisions"],
      "canonical_after_decode": bool(validator(decoded_present)) and bool(validator(decoded_absent)) and bool(validator(decoded_empty)),
      "r26_replay_new_wire_fails": rejected(r26,contract), "probe21_replay_new_wire_fails": rejected(probe21,contract),
      **production_guards(),
    }
    result={"positive":positive,"negative":dict(bad),"counts":{"positive":len(positive),"negative":len(bad)},"overall":"PASS" if all(positive.values()) and all(v for _,v in bad) else "FAIL","r26_raw_sha256":sha(R26_ARTIFACTS/"director_provider_response.json"),"probe21_raw_sha256":sha(PROBE21)}
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8"); print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if result["overall"]=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
