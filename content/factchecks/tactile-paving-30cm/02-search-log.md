# Search log

In source-priority order: (1) Korean statutes/시행령/시행규칙 → (2) government ministries/national agencies → (3) local government/public design guidelines → (4) national/official technical standards → (5) academic papers → (6) disability organizations → (7) other reliable secondary sources.

## Tier 1 — statutes / 시행령 / 시행규칙

- Query: "점자블록 설치기준 30cm 이격거리 법령" → surfaced 장애인·노인·임산부 등의 편의증진 보장에 관한 법률 시행규칙 [별표 2], among others. **Productive.**
- Query: "교통약자의 이동편의 증진법 시행규칙 점자블록 별표" → located the statute on law.go.kr but its attachment could not be parsed as plain text via WebFetch (navigation-only page). Did not pursue further once the 편의증진법 별표2 attachment (below) turned out to be the operative tactile-paving standard; **logged as not separately confirmed**, a gap worth closing in any follow-up pass.
- Downloaded and read in full (via direct PDF fetch + `pdftotext`): **장애인·노인·임산부 등의 편의증진 보장에 관한 법률 시행규칙 [별표 2] "편의시설의 세부설치기준과 대상시설"** (law.go.kr attachment, flSeq 86610217). This is the primary source for tactile-block dimensions and placement. See Evidence Log #1–#2.
- Downloaded and read in full: **보행안전 및 편의증진에 관한 법률 시행규칙 [별표 1] "보행안전 및 편의증진 시설의 구조 및 기준"** (law.go.kr attachment, flSeq 116980749). Item 11 covers 점자블록 but only defines color and functional purpose — **no dimensional figures of any kind, 30cm or otherwise.** See Evidence Log #3.
- Query: "도로의 구조ㆍ시설 기준에 관한 규칙" 점자블록 — located the statute (law.go.kr lsiSeq=173203) but did not download its attachment within the time available for this pass; **not found / not checked, logged as a gap.**

## Tier 2 — government ministries / national agencies

- Query: "도로안전시설 설치 및 관리지침 장애인 안전시설" — this is a 국토교통부 (Ministry of Land, Infrastructure and Transport) administrative guideline (행정규칙), registered on law.go.kr (admRulSeq=2100000000833) and mirrored as PDF on codil.or.kr. **Repeated connection failures** (TLS reset) prevented retrieval of the PDF via direct fetch, and WebFetch was blocked by the target's robots.txt. **Inconclusive — could not verify content.** This is flagged as the single most important open gap, since it is the one government-ministry-level document most likely to contain an authoritative clearance figure if one exists.
- Query: "KS F 4561 점자블록 규격" — located the Korean national standard's registry page (standard.go.kr) but did not retrieve the full standard text in this pass. KS F 4561 governs the physical/tactile block product (dot size, height, spacing, slip resistance), not urban placement clearances, based on its title and scope as listed; **not fully verified, logged as a gap.**

## Tier 3 — local government / public institution design guidelines

- Query: "서울시 보도공사 설계시공 매뉴얼 pdf 점자블록 장애물 이격" — located a Seoul Facilities Corporation (서울시설공단, public institution) page hosting "보도공사 설계시공 매뉴얼(ver2.0)" and "보도공사 상세설계 표준도" (detailed design standard drawings) as downloadable PDFs. The page itself contains no numeric standard; **the PDFs were not retrieved** (download links not resolvable via the tools available). **Inconclusive — logged as a gap.** This is the most likely place for a literal sidewalk cross-section clearance dimension, and its absence from this fact-check is a real limitation, noted in the Editorial Recommendation.
- Query: Seoul news article on the sidewalk manual's release (news.seoul.go.kr) — read in full; describes improvements to tactile-block continuity at driveway crossings and traffic islands, but **states no specific clearance number.**

## Tier 4 — national / official technical standards

- KS F 4561 — see Tier 2 above (not fully retrieved).

## Tier 5 — academic papers

- Query: "tactile paving 30 cm both sides South Korea regulation" and a ScienceDirect paper on TGSI (tactile ground surface indicator) installation errors across Europe/America/Oceania/Asia — the fetch was rate-limited (HTTP 429) and not retried within this pass. **Inconclusive.**

## Tier 6 — disability-related organizations

- Downloaded and read in full: 한국시각장애인연합회(Korea Blind Union) technical appendix **"부록1. 점자블록"** (kbufac.or.kr). This document explicitly states an obstacle-free-both-sides rule — but at **60cm**, not 30cm, and only for 선형블록 (linear guide blocks). See Evidence Log #4.
- Found and read: a 2025-06-30 article from **시각장애인편의시설지원센터** (Support Center for Convenience Facilities for the Visually Impaired, operating under/affiliated with the Korea Blind Union) titled "선형블록 좌우 60cm 공간 확보로 시각장애인의 안전보장해야!" — this piece is unusually explicit that 60cm is **their own manual's recommendation**, derived by combining the statute's 30cm pre-hazard offset with a separate bollard-spacing rule — not itself a quoted statute. See Evidence Log #5. This is the strongest lead for how a "30cm" figure could plausibly get attached to "tactile paving clearance" in secondary retellings.
- Fetched 한국시각장애인복지관 (Korea Welfare Center for the Blind) explainer page "시각장애인 편의시설 설치기준 및 해설." The automated extraction returned partially garbled Korean text (an encoding artifact), yielding an unverifiable fragment that appears to reference "30cm of flexible clearance from the edge of the tactile block." **This could not be confirmed with confidence and is logged as a low-reliability, unverified lead** rather than treated as evidence either way. See Evidence Log #6.

## Tier 7 — other secondary sources

- General web searches in both Korean and English for "tactile paving 30cm both sides Korea" returned no independent Korean-regulation-specific source repeating the claim's exact figure or framing; results were generic international tactile-paving product/marketing pages unrelated to Korean law.

## Summary of what was and was not confirmed

Confirmed by direct reading of primary legal text: the only "30cm" (0.3m) figures connected to tactile paving in the two statutes read in full are (a) the minimum size of a single tactile block (0.3m × 0.3m) and (b) the distance a warning block must be laid in front of a hazard. Neither is a lateral, both-sides clearance requirement. A genuine "no obstacles within X cm on both sides of the block" concept does exist in Korean accessibility practice, but the figure attached to it by the two disability-organization sources found is 60cm, explicitly framed as their own non-binding recommendation, not a quotation of law. Three tier-2/tier-3/tier-4 sources that might plausibly contain a different, authoritative figure (the 국토교통부 road-safety-facility guideline, the Seoul sidewalk design manual's detailed drawings, and KS F 4561) could not be retrieved in this pass and remain open.
