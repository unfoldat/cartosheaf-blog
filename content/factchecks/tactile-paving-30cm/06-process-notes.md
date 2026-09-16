## Why this exists as a separate page

The Fact-Checking Sample is the result. This page is the process behind it — kept separate on purpose, so the finished document reads cleanly while the reasoning, dead ends, and unresolved gaps stay visible to anyone who wants to check the checking.

## Claim decomposition

Before any search was run, the claim — "South Korean accessibility regulations require at least 30 cm of unobstructed space on both sides of tactile paving" — was broken into six separately verifiable questions: does a 30cm figure appear in Korean statute at all; what does it actually measure if it does; is there a distinct both-sides clearance concept in Korean practice and what is its real figure; is any of this binding law or non-binding guidance; does "both sides" match the source; and, if the claim turns out to be wrong, is there an evidenced explanation for how it could have arisen rather than just a shrug.

That last question turned out to matter. Finding *why* a claim is wrong is more useful, and more honest, than just marking it false.

## Search path, in brief

Searches followed the required priority order: Korean statutes first, then ministries and national agencies, then local-government design guidelines, then national technical standards, then academic papers, then disability organizations, then other secondary sources. The full source-by-source log — including every inconclusive search — lives alongside this page as the Evidence Log.

Two statutes were the breakthrough: rather than trusting a search snippet or a third-party summary, both were downloaded as PDF attachments directly from law.go.kr and read in full locally. That is what made it possible to say with confidence what the 30cm figures in Korean law actually measure (block size, and a pre-hazard installation offset) — and, just as importantly, what they do *not* measure (a lateral clearance zone).

The single most useful non-legal source was a 2025 article from a Korea Blind Union–affiliated support center, because it did something unusual: it showed its own work. It stated plainly that its 60cm "both sides" recommendation was derived by the organization itself from the statute's 30cm pre-hazard rule plus an unrelated bollard-spacing rule — not quoted from law. That single admission did more to explain a plausible origin for the tested claim than any amount of searching for the exact phrase "30cm both sides" would have.

## Dead ends and what wasn't found

Several leads did not pan out within this research pass, and are logged rather than hidden:

- A Ministry of Land, Infrastructure and Transport road-safety-facility administrative guideline (도로안전시설 설치 및 관리지침) could not be retrieved — repeated direct downloads failed with connection resets, and a fetch-and-summarize attempt was blocked by the target site's robots.txt.
- Seoul Facilities Corporation's detailed sidewalk design standard drawings (보도공사 상세설계 표준도) — the most likely place a literal cross-section clearance dimension would be drawn, if one exists — were located but not retrieved; they sit behind a download link this session's tools could not resolve.
- The full text of KS F 4561, the national technical standard for the tactile block product itself, was located in a public registry but not fetched.
- An academic paper on international tactile-paving installation errors was found but the fetch was rate-limited and not retried.
- One disability-organization explainer page was fetched, but the extracted text came back with corrupted Korean encoding. Rather than guess at the corrupted fragment's meaning, it was logged as unverified and excluded from the evidence the verdict relies on.

None of this changes the verdict — every source that *was* successfully read pointed the same direction — but a "False" verdict on a specific number deserves the caveat that three plausible tie-breaker sources remain unchecked, and that caveat is carried into the Editorial Recommendation rather than smoothed over.

## Workflow reflection

What worked well: reading primary sources as full documents rather than search snippets. The two statutes' PDF attachments were each only a few pages, and reading them completely — not just the paragraph a search engine surfaced — is what caught the distinction between "block size," "pre-hazard offset," and "both-sides clearance," three genuinely different things that all happen to use round numbers near 30cm in Korean regulatory text. A search-snippet-only approach would very plausibly have stopped at the first "0.3미터" match and called the claim confirmed.

What was harder than expected: government and public-institution web infrastructure. Several official and quasi-official PDF hosts (codil.or.kr, a Seoul Facilities Corporation download link) either refused connections outright or were blocked by robots.txt, which is a meaningful practical obstacle to fact-checking Korean administrative guidance specifically, as opposed to statute text on law.go.kr, which was comparatively easy to reach.

What would improve this process next time: building in a retry-with-backoff step for the government hosts that failed by connection reset rather than by an explicit error, since at least one (law.go.kr itself, on a different attachment) succeeded on a second attempt after an initial reset — the ministry and Seoul design-manual hosts were not retried enough times before being logged as gaps, and a few more attempts, possibly spread further apart, might have closed them. It would also help to fetch KS-series national standards earlier in the process, since they are a distinct, high-priority source tier that ended up receiving less attention than the statutes and the disability-organization material simply because those were easier to reach first.
