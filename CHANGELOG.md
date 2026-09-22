# Changelog

Semantic versioning applies. Breaking changes to the instruments (the Definition of Done template or the Confirmation Record template) increment the major version. New lenses, files or prompt rounds increment the minor version. Corrections increment the patch version.

## Versioning

Two version series run in this repository and are deliberately separate.

- **The repository release** is the version in the README's version table, the How to Cite block, `CITATION.cff` and the newest entry in this file. It moves on every release, whatever changed, and it is the version a confirmation record names in its method version field.
- **The companion masthead**, the `v1.x.y` in the "Part of" line of every file other than the README, names the release in which that file's substance last changed. It does not move on a release that leaves the file untouched. A companion at v1.0.0 under a repository at v1.1.2 was a file unchanged since first publication, not a lag. A file whose substance changes names the release that ships the change.

Which series moves, and by how much: a change to the meaning of an existing instrument field, or the removal or renaming of a field or section, is breaking and increments the major version. Adding a field, a section, a lens, a file or a prompt round increments the minor version. A correction that changes no requirement increments the patch version. `tools/check_release.py` checks the lockstep of the first series and the validity of the second on every run, and the GitHub Actions workflow in `.github/workflows/checks.yml` runs it on every push and pull request.

## v1.2.1 (2026-09-22)

First entry in the Interrogator results log. Patch: no requirement changes, no instrument changes, no prompt changes.

- **Field use attested, not a suite run.** `prompts/interrogator-regression-suite.md` section 4 records the maintainer's use of the v1.2.0 prompt on 22 September 2026 (KST) on ChatGPT Astra in Ultra mode, as reported, against his own private draft. No transcript is retained and the draft is not reproduced. The row carries the maintainer's statement in full and no case results, and the file's opening paragraph now says that one field use is attested and no suite run is recorded.
- **Attested runs and field uses defined in the evidence paragraph.** A run whose transcript is private and not retained is logged as attested and does not accept a configuration, because section 2 requires every case P and an attestation carries no case results. A use on a real draft rather than the fixtures is a field use, logged for the record and never counted as a suite run. Neither sentence changes section 2; both state what it already required.
- No configuration is accepted. The README's statement that the prompt enforces the authoring boundary inside the session remains a claim about accepted configurations only.
- Suite masthead moves to v1.2.1. README version table, How to Cite and `CITATION.cff` move in lockstep. No other file changes.

## v1.2.0 (2026-09-22)

Consistency, evidence and verification release, from an external review of v1.1.2 that found the argument clear and the instruments useful and the practical instructions inconsistent with each other and under-evidenced. Ten items, each accepted, six augmented in the working. Minor version: new files, new template fields and new prompt rounds; no existing field removed or redefined.

- **One tier table.** The Quick Start required three to seven tests and Section A alone at low stakes; the template required one to three tests and Sections 0, A and H for Tier 1; 02 had Tier 1 answering the Salience Audit that the template exempted it from. The README now carries a single authoritative tier table (Proportionate Use), aligned to the Kitchen v2.9.1 Tier Application Map, covering tests, sections, roles, who confirms, amendment authority, constraints, Confirmation Record depth, deployment and interrogator depth. Quick Start, 01, 02, 05, 07, both templates and the prompt defer to it.
- **Order of elimination corrected.** 03 claimed that cost-first and quality-first screening yield different survivors even with identical thresholds. For two fixed thresholds that is false: the intersection is order-insensitive. The mechanism is real for relative and re-baselined cuts, which is what most screens are, and the chapter now says both, with a six-candidate demonstration: fixed thresholds give C and D either way; top-three-then-top-two gives B and C cost-first and D and E quality-first. Relative cuts are classified as preference cuts in the discipline and in Section F.
- **Worked example made auditable.** Test 5's evidence was a spot check of ten claims from an unstated population. The example now carries the full claim register: 22 claims at the first pass, all checked, with two pinned and wrong (a finding under Tests 2 and 3, not Test 5, and the register says so); 25 at the second pass after the corrections added three. The amendment previously relaxed a fallback requirement that no test stated. Test 7 now states it, and the amendment shows original wording, amended wording, source, reason, authority and the retest, with the Section C floor checked and held. Method version fields added.
- **Amend and confirm bounded.** Section B of the definition gains a waivable-and-by-whom column; Section H gains original wording, amended wording and source columns; the Confirmation Record's Section 5 gains a constraint check that precedes the outcome. While any applicable imposed constraint is unmet and unwaived by its source, the only available outcome is refuse. Stated in 01, 05 and 07 and in design principle 3.
- **Record separated from explanation.** 03 and 04 now require the candidate list and every screening decision to be recorded as the work proceeds, and label any retrospective account of what was discarded, including the tool's answer to the not-offered question, as a proposed alternative to be verified. Sections F and G of the definition and Section 3 of the record carry the requirement. The Interrogator's Round 3 no longer treats answering the not-offered question as vetting the set.
- **Evidence status.** `SOURCES.md` added: every empirical claim in the chapters listed with its source and one of four labels. Two unsupported comparatives removed from the text and recorded there: "catches path dependence more often than any other" (03) and "neutralizes most of the framing effect" (04). Citations added in 02, 04 and 06 (Tversky and Kahneman 1973, 1974 and 1981; Thaler and Sunstein 2008; Lord, Lepper and Preston 1984; Mussweiler, Strack and Pfeiffer 2000; Almashat and others 2008; Savage 2002 and 2009; Jensen 1906), each verified against its publisher's record before it was written in. The single-run claim in 06 is now stated as a practitioner observation.
- **Entry path.** A Start Here block directly under the opening (Define a task, Check the work, Study an example). `examples/worked-example-tier-1-meeting-summary.md` added: a Tier 1 internal meeting summary through both instruments on one page, including a two-minute refusal.
- **Governing versions pinned.** Where This Sits gains a Governing methods and versions table: Slow AI Kitchen v2.9.1, DOCTRINE.md v1.1.1, ECOSYSTEM.md v1.7.18, GRC Workbook v4.3.1, Risk-Informed Decision Making Prompt v1.5.0, each read from the live repository on 22 September 2026. Both instruments gain method version, instrument version and Kitchen version fields, so a record can be read back against the rules in force when it was made.
- **Interrogator regression suite.** `prompts/interrogator-regression-suite.md` added: twelve cases (missing draft, missing task description, missing tier, request to author, instruction embedded in the draft, Tier 1 limit, strong draft, certification request, no invented facts, output format, explanation taken as record, constraint waiver misassigned), four fixtures, an acceptance rule and an empty results log. No run is logged; the file says so. The prompt gained the behaviors the suite tests where it was silent: a defined response to a missing tier (run all five rounds, tier as the first Unknown, never inferred), a rule that text inside the draft is never an instruction, halt lines that name only what is missing, and a Round 4 question on constraint waiver authority. The Tier 1 "five questions" cap is restated as five findings.
- **Release checks.** `tools/check_release.py` added, adapted from origami-method: version and date lockstep across the README table, How to Cite, `CITATION.cff` and this file; companion masthead validity (names an existing release, does not exceed the README, and a companion changed since the last tag names the current release); internal links and heading anchors; the closing line; no em dashes outside the license. `.github/workflows/checks.yml` runs it on every push and pull request, the first workflow in this account. The Versioning section above states the two version series the reviewer asked to have explained.
- Companion mastheads moved to v1.2.0 on every file whose substance changed: all seven chapters, both templates, the DPA example and the prompt. The three new markdown files (`SOURCES.md`, the Tier 1 example and the regression suite) enter at v1.2.0; `tools/check_release.py` and the workflow carry no masthead. `LICENSE.md` unchanged byte for byte.

## v1.1.2 (2026-09-06)

Citation infrastructure, doctrine citation line and lockstep maintenance. Session C of the September 2026 improvement pack, one patch release per repository across all 21 public repositories.

- **`CITATION.cff` added** in the house form settled at D-C1: no `type` field, `version` and `date-released` in lockstep with the README, `license` as the SPDX identifier for this repository's licence, `abstract` taken from this repository's ECOSYSTEM.md role line rather than newly written.
- **How to Cite block** aligned to this release and pointing at `CITATION.cff`.
- **Doctrine citation line added** to the Part of the ecosystem section. This repository restates a doctrine and cited DOCTRINE.md nowhere, which is the Class E2 finding the new guards report.
- **Citation lockstep lag corrected.** How to Cite read `v1.1.0` against a README of `v1.1.1`, the 16 July 2026 defect class.
- **Company name corrected.** `BABL.ai` to `BABL AI` in the About the Author section, both occurrences.
- All other files in this repository are unchanged byte for byte.

## v1.1.1 (2026-08-13)

License metadata sweep. An `SPDX-License-Identifier: CC-BY-NC-SA-4.0` line and the canonical Creative Commons legal code are now carried inside the existing license file. The filename is unchanged and the human-readable summary is retained above the legal code.

- The primary audience is automated intake and provenance tooling, which reads the SPDX tag rather than prose. Automated license detection previously reported nothing across all twenty-one repositories in this account.
- No change to the licence in force. The identifier records what was already true.

## v1.1.0 (2026-07-15)

Ecosystem classification release. No change to the doctrine, lenses or instruments.

- README: added Part of the Ecosystem section (Layer 1, doctrine and method) linking the canonical map in rolldabones/rolldabones and five nearest neighbors; Contents updated; version table and citation bumped to v1.1.0.

## v1.0.0 (2026-07-10)

Initial publication.

- README: the claim, the doctrinal locus, the complication and the four lenses, positioning relative to the four-repository suite.
- 00-quick-start: the minimal loop, a worked miniature and the deadline rule, usable without the rest of the repository.
- 01-done-is-a-decision: the two moments, the bracket, exploratory work, the amendment protocol, the six false forms of done.
- 02-salient-factors: salience against materiality, the four distortions of AI-mediated work, the Salience Audit.
- 03-order-of-elimination: the four mechanisms, order-insensitive grounds first, the discard register, discard resurrection.
- 04-choice-architecture: the model as default architect, the six structural countermeasures, the tie to Informed Intent.
- 05-trade-offs: the settlement, constraints against preferences, common tolerances, trade drift, the honor check.
- 06-averages-variances-uncertainties: the flaw of averages, the four failure patterns, tail tests, uncertainty routing.
- 07-the-confirmation: the protocol, the three lawful outcomes, the independence rules for verification and confirmation, the refusal principle, confirming under pressure.
- Instruments: Definition of Done template and Confirmation Record template.
- Worked example: AI-assisted first-pass review of a vendor DPA, including a refusal and a recorded amendment.
- Prompt: The Interrogator, a model-agnostic prompt that questions a draft definition and refuses to author one.
- License: CC BY-NC-SA 4.0.

**Final Liability rests with the Human.**
