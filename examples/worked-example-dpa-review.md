# Worked Example: AI-Assisted First-Pass Review of a Vendor DPA

Part of [The Definition of Done Is the Work of the Human](../README.md) | v1.2.0 | CC BY-NC-SA 4.0

A compressed but complete pass through both instruments on one real task shape, at Tier 3. Entries are illustrative and the vendor, the DPA and the playbook are fictional. The example includes a refusal, because a worked example in which everything passes teaches the wrong lesson, and it shows the full claim register and the full amendment record, because an example that summarizes its own evidence teaches the wrong habit. For the minimum paperwork at the other end of the scale, see the [Tier 1 example](worked-example-tier-1-meeting-summary.md).

---

## The task

In-house counsel must review a vendor's data processing agreement (DPA) against the company playbook before a SaaS renewal, using an approved AI assistant for the first-pass issue spotting and clause comparison. Personal data of EU and Korean customers is processed. Renewal deadline is in six business days.

## The Definition of Done (as completed, abridged)

**Section 0.** Task: first-pass DPA review memo identifying playbook deviations and recommended positions. Tier 3 (regulated data, external counterparty, legal exposure). Intended use: basis for counsel's markup and negotiation posture. Decision supported: sign, negotiate or escalate. Non-recoverable domain: legal and regulatory. Method versions: definition-of-done v1.2.0, Definition of Done template v1.2.0, Slow AI Kitchen v2.9.1. Roles: counsel is Preparer, Builder and Owner, working with the approved assistant as the tool. A second lawyer is Reviewer. The GC is Approver and makes the release decision.

**Section A. Tests.** Seven tests, the Tier 3 maximum. Test 7 is the one the amendment later touches, so it is stated here in the words that were amended.

| # | Test | Evidence expected |
|---|---|---|
| 1 | Every playbook clause category is dispositioned: conforming, deviating with fallback available or deviating requiring escalation | Completed clause table traceable to playbook sections |
| 2 | No error of class X anywhere, where class X is: misstated liability cap, misstated governing law, missed processing-scope expansion, missed audit-right limitation | Line-by-line check of these four categories against the DPA text, its annexes and every schedule the DPA incorporates, by the Reviewer |
| 3 | All sub-processor provisions identified, including flow-down of the vendor's obligations to sub-processors, with gaps stated | Sub-processor clause map; absence expressly stated if absent |
| 4 | Cross-border transfer mechanism for EU and Korea stated and verified against the current playbook position | Citation to the DPA annex and playbook version |
| 5 | Every material claim about the DPA quotes or pins the clause (no unpinned paraphrase) | Claim register: every material claim in the memo and the clause table numbered, the population stated, all of them checked by the Reviewer against the DPA text, zero unpinned. Population is all N, not a sample: at Tier 3 with a legal non-recoverable domain the cost of checking is small against the cost of one unpinned paraphrase surviving |
| 6 | Memo usable by GC in ten minutes: deviations ranked by consequence, one page plus tables | GC read test |
| 7 | Every deviation carries a proposed fallback position or an express "no fallback, escalate" | Fallback column of the clause table complete, no entry blank |

**Section B. Constraints and preferences.** Three constraints, each with its source and its waiver authority recorded, because the amendment protocol stops at this table.

| Criterion | Constraint or preference | Source | Waivable? |
|---|---|---|---|
| No legal position asserted contrary to the playbook without an escalation flag | Constraint | Playbook policy | Yes, by the GC as playbook owner, in writing, under the playbook's own amendment rule |
| Customer personal data is not pasted into unapproved tools | Constraint | Tool registry (Kitchen Step 10) | No. The AI Owner may authorize a tool through the registry, which is a registry change, not a waiver on this task |
| The transfer mechanism relied on for EU and Korean data is one the playbook accepts (GDPR Chapter V and the PIPA overseas-transfer provisions, as applied by the playbook) | Constraint | Law, as applied by the playbook | No |
| Brevity; deviations ranked by consequence | Preference | Owner | Owner |

**Section C. Trade-off statement.** Privileged: accuracy of deviation identification. Subordinated: completeness of drafting suggestions, floor being that every escalation-class deviation carries at least one fallback or an express "no fallback, escalate". Why: six-day window; wrong deviations are non-recoverable, thin suggestions are recoverable. Accepted by: counsel (Owner). Absorbed by: negotiation timeline if suggestions prove thin. Note the relationship between this floor and Test 7: Test 7 requires a fallback for every deviation; the Section C floor requires one for every escalation-class deviation. Test 7 is the Owner's preference and can be amended. The floor is the settlement's term and is checked at confirmation.

**Section D. Distribution clauses.** Tail test is test 2 (error classes prohibited anywhere). Band-and-basis: any risk rating in the memo carries its basis (clause text, playbook rule or judgment, labeled).

**Section E. Salience audit at define time (selected).** Quiet giant: sub-processor flow-down, historically under-litigated in-house but the largest consequence under Korean PIPA enforcement posture. Missing heading: the DPA is expected to be silent on government access requests; silence must be surfaced, not skipped. Inherited agenda: the vendor's DPA structure will set the review order; the playbook's category list, not the DPA's table of contents, governs the clause table.

**Section G. Architecture note.** The assistant drafts the clause table and memo skeleton; counsel writes conclusions. Default posture: rejected until confirmed; the memo does not reach the GC folder without a completed Confirmation Record. Presenter and verifier separated: Reviewer never sees the assistant's chat, only the memo and the DPA. Not-offered test: assistant must state the strongest vendor-favorable reading it did not include, and the answer is labeled proposed until counsel has verified it against the clause.

**Section H. Amendment log at define time.** Empty.

## What happened

The assistant produced a fluent, well-structured clause table and memo skeleton in minutes. The manual first pass (Kitchen Gate 2) had already put counsel through the DPA once with a highlighter, which is why two problems were findable at all.

## The Confirmation Record (first pass: Refuse)

**Section 1.** Test 1 pass. Test 2 fail: the memo stated the liability cap as the general cap; the DPA carves data-protection breaches out of the cap in a schedule the assistant's table did not reach (Schedule A to the master agreement, paragraph 4, incorporated by DPA clause 12.1). Class X error, found by the Reviewer's line check. Test 3 fail: the table marked sub-processor provisions "present, conforming" but the flow-down obligation was absent from the DPA; the assistant had matched the heading of clause 6 to the playbook category, not the obligation. The absence was caught by define-time salience entry "quiet giant" plus test 3's requirement that absence be expressly stated. Test 4 pass. Test 5 pass, on the register below: 22 material claims, 22 checked, 22 pinned. Test 6 pass. Test 7 pass: the fallback column was complete, in fact over-complete, which Section 3 returns to.

**The claim register for Test 5, first pass.** Every material claim in the memo and the clause table, numbered in the order the memo makes them. Checked by the Reviewer against the DPA text on day 2. The result column records the pin, which is what Test 5 tests. Two claims were pinned and wrong, which is a finding under Tests 2 and 3, not under Test 5, and the register says so rather than letting a pass on Test 5 imply a pass on substance.

| # | Claim (memo location) | Pinned to | Pinned? | Note |
|---|---|---|---|---|
| C-01 | Vendor acts as processor, customer as controller (memo §1) | cl. 2.1 | Yes | |
| C-02 | Processing only on documented instructions (table row 1) | cl. 3.1 | Yes | |
| C-03 | Vendor must notify if an instruction infringes law (table row 1) | cl. 3.2 | Yes | |
| C-04 | Personnel bound by confidentiality (table row 2) | cl. 4.1 | Yes | |
| C-05 | Security measures as listed in Annex 2 (table row 3) | cl. 5.1, Annex 2 | Yes | |
| C-06 | General authorization of sub-processors with 30-day objection right (table row 4) | cl. 6.1 | Yes | |
| C-07 | Current sub-processor list at Annex 3 (table row 4) | cl. 6.2, Annex 3 | Yes | |
| C-08 | Vendor's obligations flow down to sub-processors: "present, conforming" (table row 4) | cl. 6.3 | Yes | Pinned and wrong. Clause 6.3 requires notice of sub-processor changes; no clause imposes the vendor's obligations on sub-processors. Test 3 failure |
| C-09 | Assistance with data subject requests within 10 business days (table row 5) | cl. 7.1 | Yes | |
| C-10 | Personal data breach notified without undue delay and within 48 hours (table row 6) | cl. 8.1 | Yes | |
| C-11 | Breach notice content matches the playbook minimum (table row 6) | cl. 8.2 | Yes | |
| C-12 | Audit right once per year on 30 days' notice (table row 7) | cl. 9.1 | Yes | |
| C-13 | Audit satisfied by third-party reports unless a regulator requires more (table row 7) | cl. 9.2 | Yes | Audit-right limitation, correctly identified as a deviation |
| C-14 | EU transfers under the SCCs, controller-to-processor module (table row 8) | cl. 10.1, Annex 1 Part C | Yes | |
| C-15 | Korean transfer basis stated as data subject consent obtained by the customer (table row 8) | cl. 10.3 | Yes | |
| C-16 | Return or deletion within 90 days of termination (table row 9) | cl. 11.1 | Yes | |
| C-17 | Certificate of deletion on request (table row 9) | cl. 11.2 | Yes | |
| C-18 | DPA liability subject to the master agreement's general cap (table row 10, memo §3) | cl. 12.1 | Yes | Pinned and wrong. Clause 12.1 incorporates Schedule A to the master agreement, whose paragraph 4 carves data-protection breaches out of the cap. Test 2 failure |
| C-19 | DPA term coextensive with the master agreement (table row 11) | cl. 13.1 | Yes | |
| C-20 | Data subject categories: customer employees and end users (memo §2) | Annex 1 Part A | Yes | |
| C-21 | Processing purposes limited to providing the service (memo §2) | Annex 1 Part B | Yes | |
| C-22 | Retention period 90 days after termination (memo §2) | Annex 1 Part D | Yes | |

Population: 22. Checked: 22. Unpinned: 0. Test 5: pass.

**Section 2 (selected).** Naked assertion: two risk ratings carried confident language with no stated basis; returned under the band-and-basis rule. Missing heading: government access silence was surfaced, correctly.

**Section 3.** Trade-off honor: the assistant had quietly re-traded, expanding drafting suggestions (subordinated criterion) while compressing the deviation analysis for two annex clauses (privileged criterion), Annex 1 Part D on retention and Annex 2 paragraph 6 on encryption at rest. Refused; the settlement stands, and the two clauses are re-analyzed in the second pass. Architecture: the not-offered test returned a vendor-favorable reading of the audit clause, that clause 9.2 read with 9.1 confines the customer to third-party reports in every year a regulator does not intervene. Labeled proposed, verified by counsel against the two clauses, held and entered as escalation item 3. The lens paid for itself here, and it paid because the answer was verified rather than adopted.

**Section 5.** Constraint check: all three constraints Met. Outcome: **Refuse.** Failed tests 2 and 3, refused by the Owner on the Reviewer's evidence before the record ever reached the Approver. Refusal needs no seniority; anyone in the chain who finds a failed test may return the work.

## The second pass (Amend and confirm)

The cap carve-out and the flow-down gap were corrected and re-verified by the Reviewer. The re-analysis of the two annex clauses added two deviations to the table, D-12 (retention 90 days against the playbook's 30) and D-13 (encryption standard at rest unspecified against the playbook's named standard), both ranked low consequence under the playbook's own ranking and neither escalation-class. With two days consumed by the corrections, the fallback positions for D-12 and D-13 were not drafted, so Test 7 as written failed on the re-run.

**The amendment, in full.** One entry in Section H, made on day 4.

| Date | Test amended, original wording | Amended wording | Source of the requirement | Why | Amended by |
|---|---|---|---|---|---|
| Day 4 | Test 7: "Every deviation carries a proposed fallback position or an express 'no fallback, escalate'" | Test 7: "Every deviation carries a proposed fallback position or an express 'no fallback, escalate', except D-12 and D-13, whose fallback positions are deferred to the negotiation and marked 'deferred' in the fallback column" | Preference: the Owner's own criterion, not a Section B constraint | Two days consumed by the Test 2 and Test 3 corrections. The deferred fallbacks are recoverable in the negotiation; a wrong deviation was not. The Section C floor is untouched, because neither D-12 nor D-13 is escalation-class | Owner (counsel), with the Approver's (GC) sign-off, as Tier 3 requires |

**Retest against the amended standard.** Test 2 pass (cap carve-out stated, all four class X categories re-checked line by line by the Reviewer, including Schedule A). Test 3 pass (flow-down absence expressly stated in the sub-processor clause map, citing clauses 6.1 to 6.4 in full). Test 5 pass: the corrections added three material claims, so the population moved and the register was re-run rather than topped up.

| # | Claim (memo location) | Pinned to | Pinned? | Note |
|---|---|---|---|---|
| C-01 to C-22 | As in the first pass, re-checked | As above | Yes | C-08 and C-18 rewritten; the pins now read Annex 3 with the absence statement (C-08) and cl. 12.1 with Schedule A para. 4 (C-18) |
| C-23 | Data-protection breaches are carved out of the general cap (memo §3, table row 10) | Schedule A to the master agreement, para. 4, via cl. 12.1 | Yes | |
| C-24 | No clause imposes the vendor's DPA obligations on sub-processors; the absence is stated (table row 4) | cl. 6.1 to 6.4, quoted in full | Yes | An absence is pinned by quoting the whole of the place where the obligation should be |
| C-25 | Clause 9.2 confines the customer to third-party audit reports in any year a regulator does not intervene (escalation item 3) | cl. 9.1 and 9.2 | Yes | The not-offered answer, verified and entered |

Population: 25. Checked: 25. Unpinned: 0. Test 5: pass.

Test 7 as amended: pass. The fallback column is complete for every deviation other than D-12 and D-13, which carry the word "deferred" and nothing else. Tests 1, 4 and 6: pass, re-run unchanged.

**Constraint check.** All three constraints Met; nothing waived; the amendment touched no constraint.

**Outcome: Amend and confirm**, the release decision signed by the GC as Approver on the Reviewer's re-verification. Residual risk stated: a thinner first offer on D-12 and D-13. Scope of release: GC and negotiation team, this renewal only, reopen if the vendor swaps any sub-processor before signature.

## What the example teaches

The two failures were exactly the kind this repository predicts. The cap error was a tail event: one schedule, one carve-out, invisible to any average judgment of a memo that was 95 percent excellent. The flow-down gap was an absence: maximally material, minimally salient, caught only because a define-time test forced absence to be stated expressly. Neither would have been caught by reading the memo for quality. Both were caught by confirming against a definition written before the assistant produced a single fluent page.

The register teaches something the summary of it would have hidden. Two claims were pinned and wrong. A pin is evidence that the claim can be checked, not evidence that it was right, which is why Test 5 sits beside Tests 2 and 3 rather than in place of them, and why the register records the population rather than a sample: had two of the 22 claims been unpinned, a spot check of ten would have missed at least one of them four times in five.

The amendment teaches the shape an honest relaxation takes. The criterion existed before the work, in words that could be quoted. The amended words could be quoted too. The source was a preference, so the Owner had the authority, and at Tier 3 the Approver signed as well. The settlement's floor was checked and held. The residual risk was named. The deadline did not force a dishonest confirmation. It forced a recorded amendment, owned by a named Human, and that is the method working under pressure, not despite it.

---

**Final Liability rests with the Human.**
