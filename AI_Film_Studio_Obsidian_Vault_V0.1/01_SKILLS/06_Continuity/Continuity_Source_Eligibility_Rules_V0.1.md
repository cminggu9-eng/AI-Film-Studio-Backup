---
type: source-eligibility-rules
role: continuity
phase: 1-capability-discovery
status: complete
version: 0.1
---

# Continuity Source Eligibility Rules V0.1

## Authority tiers

| Tier | Eligible evidence | Use in this project |
| --- | --- | --- |
| A | Practitioner methodology book; official professional training; accredited course body; guild/institution teaching; first-party long lecture; authoritative practitioner article; authorized archive | Eligible for formal Phase 2 only when the exact lawful body is available and method is explicit. |
| B | Institutional long interview; university lecture; professional transcript; production training material | May support or supplement; formal use requires the same body/access audit. |
| C | Credible secondary source | Discovery and triangulation only; not a stand-alone formal CT-D source. |
| D | Unprovenance blog/video, fan/wiki/IMDb/social thread, AI output, listicle or SEO page | Never a formal source. |

## Body-access states

| State | Meaning |
| --- | --- |
| `DISTILLABLE_BODY_CONFIRMED` | A lawful, sufficiently complete public body is presently visible and can be re-verified in a future authorized Phase 2. |
| `BODY_AVAILABLE_BUT_LIMITED` | A lawful body exists, but visible material is curriculum, outline, archive interpretation or otherwise insufficient for deep method extraction. |
| `USER_PROVIDED_LAWFUL_COPY_REQUIRED` | A high-value copyrighted book/source needs a user-supplied lawful copy before its full body can be analyzed. |
| `PAID_ACCESS_REQUIRED` | The relevant methodology sits behind paid access; do not bypass it. |
| `LANDING_PAGE_ONLY` | Only a marketing/overview page is available; it is not a source body. |
| `UNAVAILABLE` | No lawful usable body is presently available. |

## Non-negotiable rules

- Source existence, author reputation, a book description, a table of contents, a course title and a search-result snippet are **not** a distillable body.
- No paywall bypass, unauthorized course recording, piracy, copied complete books or storage of copyrighted full source bodies in the Vault.
- Select source bodies for complementary method coverage, traceability and transferability—not fame, celebrity or repeated role descriptions.
- Separate transferable continuity judgment from `ON_SET_SPECIFIC` paperwork and `EDITORIAL_SPECIFIC` craft. Neither imports production forms or editorial authority.
- Formal Phase 2 chain is immutable: `Verified Body → actual huashu-nuwa → Codex Audit → Accepted CT-Dxx`.
- Formal CT-D without an actual Nuwa invocation is `0`. Phase 1 creates no CT-D extraction.
