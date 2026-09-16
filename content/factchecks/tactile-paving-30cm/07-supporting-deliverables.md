# Supporting deliverables — YNC application package

## CV "Projects" bullet (2–3 lines)

Independent Fact-Check, Korean Accessibility Regulation (2026) — Traced a "30cm tactile-paving clearance" claim to Korea's two governing statutes by reading primary legal text directly; found the claim conflated an unrelated block-size/pre-hazard figure and issued a "False" verdict with full evidence log and source-reliability assessment. Published at cartosheaf.com.

## Portfolio / LinkedIn description (short)

An independent fact-check of a specific claim about South Korean tactile-paving accessibility regulation, built as a portfolio sample for editorial fact-checking work. I decomposed the claim, located and read the two Korean statutes that actually govern tactile-block installation, traced a plausible 30cm→60cm conflation back to a disability-organization's own guidance, and delivered a verdict, evidence log, and editorial recommendation rather than an opinion piece. Process and result are published separately: cartosheaf.com/projects/tactile-paving-30cm.

## Talking points: "Why YNC? Why this role?"

- **This is the exact workflow YNC's Research & Verification Editor role asks for**: I didn't start from an opinion about accessibility policy and go looking for support. I decomposed a claim into checkable parts first, then let source-tiered research — statute before ministry before guideline before advocacy group — decide the answer, and the answer I found (False) went against the more sympathetic reading of the claim, not toward it. I'd rather show that discipline on a sample than assert it in a cover letter.
- **I can tell the difference between "the law says" and "an advocate recommends,"** and I think that distinction is exactly where a lot of accessibility and disability-rights claims go soft in casual reporting — a real, well-intentioned recommendation gets restated as a legal requirement, and the restatement is what spreads. Catching that (not just catching outright fabrication) is a harder and more useful skill for a verification role than simple true/false triage.
- **I surfaced my own gaps instead of hiding them.** Three sources I couldn't retrieve are logged by name in the evidence log, and the editorial recommendation explicitly says the verdict should get one more confirmatory pass before being treated as fully closed. I'd rather a fact-check read as "strongest currently available answer, with named open questions" than as falsely total confidence — that's the standard I'd want to hold YNC's published fact-checks to as well.
- **I kept the research trail and the final deliverable physically separate** (a process log and evidence log the reader can audit, versus a clean 2–3 page verdict document), because I think that separation is what makes a fact-check trustworthy rather than just readable — anyone can check my checking.

## Reflection on the research workflow (what would I improve)

The single biggest lesson from this project was that reading two short primary documents in full beat dozens of targeted searches for a specific phrase. Search snippets kept surfacing plausible-looking "0.3미터" matches that turned out, on full reading, to mean something else entirely (block size, pre-hazard offset) from what the claim asserted (lateral clearance) — a search-only approach would very plausibly have stopped early and wrongly confirmed the claim. I'd generalize that into a rule for future work: once a primary source is found, read the whole relevant section before searching further, rather than pattern-matching on the first number that looks right.

The clearest weakness was infrastructure, not method: several official and quasi-official Korean government document hosts (an administrative-guideline PDF archive, a public corporation's document server) either reset connections or blocked automated fetches outright, and I didn't retry them enough times before logging them as gaps. A better version of this workflow would build in a deliberate retry-with-backoff step for exactly that failure mode before moving on, since at least one government host did succeed on a later attempt after an earlier failure.
