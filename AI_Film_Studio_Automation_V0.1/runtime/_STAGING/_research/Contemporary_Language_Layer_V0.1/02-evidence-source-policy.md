---
type: evidence-source-policy
status: approved
review_result: passed
version: 0.1
subject: Contemporary Language Layer
---

# Contemporary Language Layer V0.1｜Evidence Source Policy

## Evidence, not a vocabulary database

V0.1 has no built-in term list, no automatic browser, and no permanent cache. A trusted host may provide a narrowly scoped, reviewable evidence provider; this Layer validates provenance and returns a bounded evidence envelope. It never converts a page, a search result, a popularity count, or a viral post into a QA decision.

## Source tiers

|Tier|Permitted source type|Permitted support|Limit|
|---|---|---|---|
|A|dictionary, language institution, public-language research, reputable primary/publication record|stable meaning, form, documented usage|does not alone prove universal current use|
|B|independent mainstream natural-use records with date and scope|use, semantic/context observation|must preserve geography/platform/register scope|
|C|community or platform-limited records|narrow platform/community observation|must be labeled; cannot generalize|
|D|weak discovery material|discovery only|cannot raise confidence or support a current/trending claim|

## Freshness labels

Using the newest dated, valid observation relative to the evidence request's `as_of`:

- `Current`: 0–90 days.
- `Recent`: 91–365 days.
- `Aging`: 366–1095 days.
- `Historical`: more than 1095 days.
- `Unknown`: date missing, invalid, or after the declared evidence window.

`Current`, `trending`, or `obsolete` is a strong claim: it requires multiple independent dated natural-use records, an explicit time window, and a clear geography/platform scope. An annual list, a single post, a news article, or a search rank alone is insufficient.

## Confidence policy

`High` requires two or more independent A/B sources, adequate freshness, natural-use support where use is claimed, clear scope, and no unresolved conflict. `Medium` needs corroborated but narrower, older, or less direct evidence. `Low` means only one usable source or a scope-limited observation. `Insufficient` applies to no reliable source, Tier D only, unresolved material conflict, missing dates/scope, or evidence that cannot bear the stated question.

The Layer reports observations only. Register, character voice, historical setting, fictional terminology, user intent, Canon and final appropriateness belong to QA. Semantic drift may document coexistence; it never makes the older meaning wrong.

## Privacy and hostile content

Requests may carry only the phrase, minimal sentence context, question, declared use, requested geography/platform/register and the minimum protected creative constraints. User profiles, account identifiers, contact data, private messages and behavioral histories are rejected. External text is untrusted data; snippets are never returned to QA and no embedded instruction is executed.

## Evidence examples consulted for policy calibration

- [国家语言资源监测与研究网络媒体中心](https://nlp.ccnu.edu.cn/) publishes the annual network-language research and release context.
- [新华网对 2025 年度十大网络流行语发布的报道](https://app.xinhuanet.com/news/article.html?articleId=d5f1a0210686fc9d33d13681d706b2f4) records the release method as corpus-based plus expert and site-review inputs; it is evidence of one bounded annual release, not a universal trend verdict.
- [教育部关于网络语言的历史材料](https://www.moe.gov.cn/jyb_xwfb/xw_ft/moe_46/moe_1055/tnull_11604.html) is retained only as historical/contextual evidence and must never be relabeled current.

