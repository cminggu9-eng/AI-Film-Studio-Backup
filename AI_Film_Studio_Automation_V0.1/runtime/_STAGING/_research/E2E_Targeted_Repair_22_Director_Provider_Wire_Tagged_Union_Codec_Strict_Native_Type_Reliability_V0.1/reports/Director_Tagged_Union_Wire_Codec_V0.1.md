# Tagged union wire codec

Codec `DIRECTOR_DEEPSEEK_TAGGED_UNION_CODEC_V1` is owned by `director_provider_compatibility.py`. It recognizes only the canonical `ABSENT | array[text]` schema shape, projects only `unresolved_decisions`, and never parses field strings with `json.loads`.
