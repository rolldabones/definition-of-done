# Worked Example: AI-Assisted First-Pass Review of a Vendor DPA

Part of [The Definition of Done Is the Work of the Human](../README.md) | v1.0.0 | CC BY-NC-SA 4.0

A compressed but complete pass through both instruments on one real task shape. Entries are illustrative and the vendor is fictional. The example includes a refusal, because a worked example in which everything passes teaches the wrong lesson.

---

## The task

In-house counsel must review a vendor's data processing agreement (DPA) against the company playbook before a SaaS renewal, using an approved AI assistant for the first-pass issue spotting and clause comparison. Personal data of EU and Korean customers is processed. Renewal deadline is in six business days.

## The Definition of Done (as completed, abridged)

**Section 0.** Task: first-pass DPA review memo identifying playbook deviations and recommended positions. Tier 3 (regulated data, external counterparty, legal exposure). Intended use: basis for counsel's markup and negotiation posture. Decision supported: sign, negotiate or escalate. Non-recoverable domain: legal and regulatory. Roles: counsel is Preparer, Builder and Owner, working with the approved assistant as the tool. A second lawyer is Reviewer. The GC is Approver and makes the release decision.

**Section A. Tests.**

| # | Test | Evidence expected |
|---|---|---|
| 1 | Every playbook clause category is dispositioned: conforming, deviating with fallback available or deviating requiring escalation | Completed clause table traceable to playbook sections |
| 2 | No error of class X anywhere, where class X is: misstated liability cap, misstated governing law, missed processing-scope expansion, missed audit-right limitation | Line-by-line check of these four categories against the DPA text by the Reviewer |
| 3 | All sub-processor provisions identified, including flow-down of the vendor's obligations to sub-processors, with gaps stated | Sub-processor clause map; absence expressly stated if absent |
| 4 | Cross-border transfer mechanism for EU and Korea stated and verified against the current playbook position | Citation to the DPA annex and playbook version |
| 5 | Every material claim about the DPA quotes or pins the clause (no unpinned paraphrase) | Spot check of ten claims by Reviewer, zero unpinned |
| 6 | Memo usable by GC in ten minutes: deviations ranked by consequence, one page plus tables | GC read test |

**Section B.** Constraints: no legal position asserted contrary to the playbook without an escalation flag (source: playbook policy); customer personal data is not pasted into unapproved tools (source: tool registry). Preferences: brevity, ranking style.

**Section C. Trade-off statement.** Privileged: accuracy of deviation identification. Subordinated: completeness of drafting suggestions, floor being that every escalation-class deviation carries at least one fallback or an express "no fallback, escalate". Why: six-day window; wrong deviations are non-recoverable, thin suggestions are recoverable. Accepted by: counsel (Owner). Absorbed by: negotiation timeline if suggestions prove thin.

**Section D. Distribution clauses.** Tail test is test 2 (error classes prohibited anywhere). Band-and-basis: any risk rating in the memo carries its basis (clause text, playbook rule or judgment, labeled).

**Section E. Salience audit at define time (selected).** Quiet giant: sub-processor flow-down, historically under-litigated in-house but the largest consequence under Korean PIPA enforcement posture. Missing heading: the DPA is expected to be silent on government access requests; silence must be surfaced, not skipped. Inherited agenda: the vendor's DPA structure will set the review order; the playbook's category list, not the DPA's table of contents, governs the clause table.

**Section G. Architecture note.** The assistant drafts the clause table and memo skeleton; counsel writes conclusions. Default posture: rejected until confirmed; the memo does not reach the GC folder without a completed Confirmation Record. Presenter and verifier separated: Reviewer never sees the assistant's chat, only the memo and the DPA. Not-offered test: assistant must state the strongest vendor-favorable reading it did not include.

## What happened

The assistant produced a fluent, well-structured clause table and memo skeleton in minutes. The manual first pass (Kitchen Gate 2) had already put counsel through the DPA once with a highlighter, which is why two problems were findable at all.

## The Confirmation Record (first pass: Refuse)

**Section 1.** Test 1 pass. Test 2 fail: the memo stated the liability cap as the general cap; the DPA carves data-protection breaches out of the cap in a schedule the assistant's table did not reach. Class X error, found by the Reviewer's line check. Test 3 fail: the table marked sub-processor provisions "present, conforming" but the flow-down obligation was absent from the DPA; the assistant had matched the heading, not the obligation. The absence was caught by define-time salience entry "quiet giant" plus test 3's requirement that absence be expressly stated. Tests 4, 5, 6 pass.

**Section 2 (selected).** Naked assertion: two risk ratings carried confident language with no stated basis; returned under the band-and-basis rule. Missing heading: government access silence was surfaced, correctly.

**Section 3.** Trade-off honor: the assistant had quietly re-traded, expanding drafting suggestions (subordinated criterion) while compressing the deviation analysis for two annex clauses (privileged criterion). Refused; the settlement stands. Architecture: not-offered test returned a vendor-favorable reading of the audit clause that became escalation item 3. The lens paid for itself here.

**Section 5.** Outcome: **Refuse.** Failed tests 2 and 3, refused by the Owner on the Reviewer's evidence before the record ever reached the Approver. Refusal needs no seniority; anyone in the chain who finds a failed test may return the work.

## The second pass (Amend and confirm)

The cap carve-out and the flow-down gap were corrected and re-verified by the Reviewer. One amendment was recorded: with two days consumed, the Owner amended Section A to defer the fallback drafting for two low-consequence deviations to the negotiation itself, recording the reason (time), the authority (Owner with the Approver's sign-off, as Tier 3 requires) and the residual risk (thinner first offer on those two points). Outcome: **Amend and confirm**, the release decision signed by the GC as Approver on the Reviewer's re-verification. Scope of release: GC and negotiation team, this renewal only, reopen if the vendor swaps any sub-processor before signature.

## What the example teaches

The two failures were exactly the kind this repository predicts. The cap error was a tail event: one schedule, one carve-out, invisible to any average judgment of a memo that was 95 percent excellent. The flow-down gap was an absence: maximally material, minimally salient, caught only because a define-time test forced absence to be stated expressly. Neither would have been caught by reading the memo for quality. Both were caught by confirming against a definition written before the assistant produced a single fluent page.

The deadline did not force a dishonest confirmation. It forced a recorded amendment, owned by a named Human, with the residual risk stated. That is the method working under pressure, not despite it.

---

**Final Liability rests with the Human.**
