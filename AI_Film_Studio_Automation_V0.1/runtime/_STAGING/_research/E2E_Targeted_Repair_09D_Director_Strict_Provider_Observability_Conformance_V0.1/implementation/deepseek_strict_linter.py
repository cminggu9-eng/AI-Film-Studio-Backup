from __future__ import annotations
from typing import Any, Mapping
UNSUPPORTED={"minLength","maxLength","minItems","maxItems"}
ALLOWED={"type","properties","required","additionalProperties","enum","items","anyOf","$ref","$defs","description"}
NODE_ANCHORS={"type","anyOf","$ref"}
def lint(schema: Any, pointer: str="") -> list[dict[str,Any]]:
    findings=[]
    if isinstance(schema,Mapping):
        bad=sorted(set(schema)&UNSUPPORTED); unknown=sorted(set(schema)-ALLOWED)
        if bad or unknown: findings.append({"pointer":pointer or "/","unsupported":bad,"unverified":unknown})
        if not (set(schema) & NODE_ANCHORS):
            findings.append({"pointer":pointer or "/","code":"NODE_ANCHOR_REQUIRED","message":"schema node must contain type, anyOf, or $ref"})
        if "enum" in schema:
            enum=schema["enum"]
            if not isinstance(enum,list) or not enum:
                findings.append({"pointer":pointer or "/","code":"ENUM_DOMAIN_INVALID","message":"enum must be a non-empty list"})
            elif all(isinstance(value,str) for value in enum) and schema.get("type") != "string":
                findings.append({"pointer":pointer or "/","code":"ENUM_STRING_TYPE_REQUIRED","message":"string enum must declare type string"})
            elif schema.get("type") == "string" and not all(isinstance(value,str) for value in enum):
                findings.append({"pointer":pointer or "/","code":"ENUM_STRING_VALUE_TYPE_MISMATCH","message":"string enum values must all be strings"})
        if schema.get("type")=="object":
            props=schema.get("properties",{}); required=schema.get("required",[])
            if not isinstance(props,Mapping) or set(props)!=set(required) or schema.get("additionalProperties") is not False: findings.append({"pointer":pointer or "/","object_rule_failure":True})
        for key,value in schema.items():
            if key in {"properties","$defs"} and isinstance(value,Mapping):
                for child,sub in value.items(): findings.extend(lint(sub,f"{pointer}/{key}/{child}"))
            elif key=="items": findings.extend(lint(value,f"{pointer}/items"))
            elif key=="anyOf" and isinstance(value,list):
                for i,sub in enumerate(value): findings.extend(lint(sub,f"{pointer}/anyOf/{i}"))
    return findings
