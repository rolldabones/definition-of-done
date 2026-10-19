# Changelog

Semantic versioning applies. Breaking changes to the instruments (the Definition of Done template or the Confirmation Record template) increment the major version. New lenses, files or prompt rounds increment the minor version. Corrections increment the patch version.

## Versioning

Two version series run in this repository and are deliberately separate.

- **The repository release** is the version in the README's version table, the How to Cite block, `CITATION.cff` and the newest entry in this file. It moves on every release, whatever changed, and it is the version a confirmation record names in its method version field.
- **The companion masthead**, the `v1.x.y` in the "Part of" line of every file other than the README, names the release in which that file's substance last changed. It does not move on a release that leaves the file untouched. A companion at v1.0.0 under a repository at v1.1.2 was a file unchanged since first publication, not a lag. A file whose substance changes names the release that ships the change.

Which series moves, and by how much: a change to the meaning of an existing instrument field, or the removal or renaming of a field or section, is breaking and increments the major version. Adding a field, a section, a lens, a file or a prompt round increments the minor version. A correction that changes no requirement increments the patch version. `tools/check_release.py` checks the lockstep of the first series and the validity of the second on every run, and the GitHub Actions workflow in `.github/workflows/checks.yml` runs it on every push and pull request.

## v1.2.6 (2026-10-19)

Patch, from the weekly maintenance sweep of 19 October 2026 (KST) and Michael Paik's review of the T5 runs, completed 19 October 2026 (KST), on which he concurs with the scoring as recorded. The weekly sweep raised A1 HIGH at `prompts/interrogator-regression-suite.md:88` ("its named reviewer's review is pending", true when written on 18 October 2026). No requirement changes, no instrument field changes, no change to what the Interrogator does.

- **Regression suite, run T5 reviewed.** The lead paragraph, the results log line, the run's configuration line, the scoring note, the eleven P rows (now "P (scorer), reviewer concurs") and the counts line record the review: the reviewer concurs with every scorer verdict, IR-07 included. IR-09 stays F and open, so no configuration is accepted, as before.
- Companion masthead of the regression suite to v1.2.6. Version table, How to Cite and `CITATION.cff` to v1.2.6 in lockstep.

## v1.2.5 (2026-10-18)

Tests sprint, from the whole-account review of 15 October 2026 (doc section 5; reviewer report 13, items A7, B1 and B2), session T5. Patch: no requirement changes, no instrument field changes, no change to what the Interrogator does. The first logged suite run: 11 of 12 cases P on the scorer's verdicts, IR-09 F, no configuration accepted.

- **Tier 3 worked example completed.** `examples/worked-example-dpa-review.md` omitted Section F, which the tier table requires at Tier 3, so Fixture S could not be pasted as the suite describes it. Section F is added at define time (not a selection task, so the elimination fields are n/a with the reason; the issue set is the playbook's category list, not tool-generated; retrospective explanations labeled proposed and verified; issues-considered list required). The Confirmation Record gains Section 4 (residual uncertainty, three rows typed and routed as `06` requires, Watch with parameter, schedule and trigger) and Section 7 (file and feed) at the second pass, with one-line Sections 4 and 7 at the refused first pass.
- **Fixture S aligned.** The suite now names the exact passage to paste: the define-time definition, Section H empty, Test 7 in its original wording, with the task paragraph as the task description.
- **Design principle 2 scoped.** README "enforces this boundary in the session itself" now reads "on an accepted configuration only", pointing at the regression suite, as the suite's acceptance rule already said.
- **Risk-Informed Decision Making Prompt re-pinned** from v1.5.1 to v1.6.0, shipped in the same session and read on 18 October 2026: v1.6.0 changes the likelihood bands, the escalation test, the tolerance line and the register format, and touches none of the parts the pin names (A2 imposed constraints, A5 common tolerances, A6 reopen conditions, the Bias Check and the Uncertainty Treatment table).
- **First logged suite run (run T5, 18 October 2026, KST).** The twelve cases ran on `claude-opus-5-5` against the v1.2.4 prompt, loaded as everything below its horizontal rule (6,725 bytes, SHA-256 `85bb8e7631c7d34bed3fd68650046bc4e4779efb5188b1025538183542ba9127`), through the Anthropic API with no tools and max_tokens 16,000, and were scored by `claude-sonnet-5-5`. LLM scoring is developer testing, not independent assurance. Scorer: 11 P, 1 F (IR-09: no Unknown names the missing audience, and finding 5 asserts "The draft's intended reader is procurement"). Session review: IR-09 concur, model behavior; no instrument defect, no dissent, no case defect; IR-01, IR-02, IR-06 and IR-10 spot-checked and concurred; IR-07 flagged for the reviewer on a sub-claim the scorer itself calls inaccurate. **Not accepted** under section 2: IR-09 is open and the named reviewer's review is pending (Michael Paik). Section 4 carries the run, the opening paragraph and the section 4 status line now say so, and the twelve transcripts with the run summary are published in `evidence/transcripts-2026-10-18-T5/`, copied byte for byte with the closing line appended.
- **`tools/check_release.py`:** run records under `evidence/` are excluded from the companion masthead check only; links, the closing line and the em-dash check still read them. Proved on a copy: a companion without a masthead and an evidence file without the closing line each still fail.
- Findings by class: A7, B1 and B2 confirmed and edited (B2: run and logged, one case open). Not taken in this release, and reported: A10 (IR-02's "may also list the tier as awaited" against the prompt's three halt strings), B2's en dash or hyphen question, the same unscoped enforcement claim in the team-lead paragraph ("so the discipline is enforced inside the tool") and Confirmation Record template Section 7's missing Service Record row (B3).
- Companion mastheads moved to v1.2.5 on the DPA example and the regression suite. Both templates and the Interrogator unchanged byte for byte. Version table, How to Cite and `CITATION.cff` move to v1.2.5 in lockstep.

## v1.2.4 (2026-10-17)

Doctrine pointer, pin re-verification and mechanical corrections, from the whole-account review of 15 October 2026 (doc sections 1 and 8; reviewer report 13, items A6, A11, C1, C4 and C5), session T3. Patch: no requirement changes, no instrument field changes, no change to what the Interrogator does.

- **Governing versions re-verified.** DOCTRINE.md re-pinned from v1.1.1 to v1.2.0 and ECOSYSTEM.md from v1.7.18 to v1.7.28, each read from the profile repository on 17 October 2026: DOCTRINE.md v1.1.2 and v1.2.0 correct two statutory status tags and add the sanctioned short forms, and no rule this repository applies moved; ECOSYSTEM.md still classifies this repository in Layer 1 and its protocol gains lockstep (item 5) and reciprocity (item 9). The Slow AI Kitchen pin stays at v2.11.0 and lags by design: the Kitchen re-versions in the same review session, and the pin is re-verified against that release, not against one already superseded.
- **GRC Workbook and Risk-Informed Decision Making Prompt re-pinned** to v4.3.2 and v1.5.1, shipped in the same session: their T3 changes are doctrine wording and punctuation and touch none of the parts the pins name (Modules 10 and 11; A2, A5, A6, the Bias Check and the uncertainty treatment). The Slow AI Kitchen pin stays at v2.11.0 until it is re-verified against v2.12.0, which moves the Owner sequence and so touches the task roles the pin names.
- **Design principle 5** points to DOCTRINE.md, the normative text, instead of "the companion repositories".
- **03-order-of-elimination:** "two additional tests" before three bullets now reads "three".
- ***Human* as a common noun** lowercased at three places the review named (00 "a human who has not worked the task", 04 "a fully qualified human", 07 "their humans"). The README's local convention, capitalizing *Human* for the person who holds the bracket, is unchanged and awaits the author's ruling against DOCTRINE.md section 6.
- **Serial commas** removed in 06 (the residual sentence) and in the Interrogator's Round 2 question, which is split into two questions with the same content.
- **Part of the ecosystem** heading in the protocol's form; Related Work names computational-drafting, which names this repository as a neighbor.
- The v1.2.0 entry below says the regression suite carries "four fixtures"; the suite has five, one by reference. The entry is shipped history and stays as written.
- Companion mastheads moved to v1.2.4 on 00, 03, 04, 06, 07 and the Interrogator. Both templates, `SOURCES.md`, `LICENSE.md` and `tools/check_release.py` unchanged byte for byte. Version table, How to Cite and `CITATION.cff` move to v1.2.4 in lockstep.

## v1.2.3 (2026-10-15)

Byline correction, on the author's instruction of 15 October 2026 (KST). Patch: no requirement changes, no instrument field changes, no prompt changes.

- **README credit line:** "CEO, GRC Solutions Korea | former General Counsel, BABL AI" now reads "CEO, GRC Solutions Korea". About the Author, which names the former role in prose, is unchanged.
- Version table, How to Cite and `CITATION.cff` move to v1.2.3 in lockstep. No companion file is touched, so no companion masthead moves under the versioning rule above, and both templates stay at Instrument version v1.2.2.

## v1.2.2 (2026-10-11)

The Slow AI Kitchen pin moves from v2.9.1 to v2.11.0 after re-verification. Patch: no requirement changes, no instrument field changes, no prompt changes.

- **Re-verified against Slow AI Kitchen v2.11.0 on 11 October 2026 (KST)**, at the parts the pin names: Gates 1, 6 and 7, the three risk tiers, the Tier Application Map and the task roles. Between v2.9.1 and v2.11.0 the Kitchen changed three of them. Step 8 (Gate 6) now states that the gate is performed by the human Reviewer against something outside the model and that a model's review of its own output is not verification; this repository already says the same at `01-done-is-a-decision.md` ("Self-attestation by the system under review is evidence of nothing"), `04-choice-architecture.md` (separate the presenter from the verifier) and `07-the-confirmation.md` (test by test, with evidence). Risk Tiers now states that the tier is assigned before the work begins by a named human with the reason recorded, and in organizational use by the Step 10 registry, with no team classifying its own work down; the Definition of Done template already records the tier with a one-line basis and names the Owner. Step 9 (Gate 7) now carries a test of ownership at release, that the owner can explain the work to a prepared listener with no model in the room; this repository's `07-the-confirmation.md` already requires the confirming Human to state, test by test, what was checked and against what evidence, and the Confirmation Record is that account in writing, so the test and the record agree. Gate 1, the tier definitions, the test counts, the Tier Application Map rows this repository relies on and the task roles are unchanged between the two versions. Nothing here needed to change.
- **The governing-versions table and the tier paragraph** name v2.11.0 (2026-10-11, KST). Both templates' "Kitchen version applied" field moves with them; because that field is part of the template's content, the two templates carry companion masthead and Instrument version v1.2.2 under the versioning rule above.
- `DOCTRINE.md` v1.1.1, `ECOSYSTEM.md`, the GRC Workbook and the Risk-Informed Decision Making Prompt pins are not re-verified in this release and do not move; `ECOSYSTEM.md` is at v1.7.22 against the pinned v1.7.18, a lag recorded in the account runbook as governed parts unchanged.
- Version table, How to Cite and `CITATION.cff` move to v1.2.2 in lockstep.

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
