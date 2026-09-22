# Definition of Done (Instrument)

Part of [The Definition of Done Is the Work of the Human](../README.md) | v1.2.0 | CC BY-NC-SA 4.0

**Complete before any AI touches the task.** The README's [tier table](../README.md#proportionate-use-the-tier-table) is the authoritative statement of what each tier completes. Tier 1 work completes Sections 0, A and H only, with one to three tests, and writes any imposed constraint that applies as one of those tests, marked as a constraint. Tier 2 and Tier 3 complete every applicable section; in Section F the elimination fields apply only where the task selects among alternatives, while the issues-considered field applies to every task. Tier 3 retains this instrument as evidence. Where a field does not apply, write "n/a" and the reason. Where a field cannot be completed, write "Unknown" and treat closing it as part of the task.

---

## Section 0. The Task

| Field | Entry |
|---|---|
| Task (one sentence) | |
| Date and timezone | |
| Risk tier (Kitchen T1, T2, T3) with one-line basis | |
| Intended use of the output | |
| Audience | |
| Decision the output supports | |
| Non-recoverable domain, if any (legal, safety, regulatory, financial, reputational) | |
| Method version: the release of this repository this definition is made under (the README's version table; see Governing methods and versions) | definition-of-done v |
| Instrument version | Definition of Done template v1.2.0 |
| Kitchen version applied (tiers, gates and roles) | Slow AI Kitchen v2.9.1 |

**Roles** (one person may hold several roles in small settings, per the Kitchen; Builder and Reviewer are different people wherever the team allows; Reviewer, Approver and Owner are distinct at Tier 3; review is always a distinct act against the definition, never a re-reading of one's own draft)

| Role | Name |
|---|---|
| Preparer | |
| Builder | |
| Reviewer | |
| Approver (Tier 3) | |
| Owner | |

## Section A. Pass or Fail Tests (3 to 7; 1 to 3 for Tier 1)

Each test is observable, is anchored to consequence and states the evidence that will establish it at confirmation, including the population checked and the sampling rule where the evidence is a check of claims or items (all N, or a sample of n from N chosen how). Cover substance, usability, constraints and sign-off. No composites and no scores: each test passes or fails alone. At Tier 2 and above at least one test originates from the Salience Audit in Section E (a test for an absence, an assumption or a tail rather than for a visible feature of the artifact); at Tier 1 this is recommended. A test that restates an imposed constraint from Section B is marked (constraint) and is outside the amendment log's reach.

| # | Test (pass/fail) | Evidence expected at confirmation |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |

## Section B. Constraints Against Preferences

Imposed constraints disqualify. They are not tradeable, no test may be averaged against them and they are not amended in Section H. A constraint is met, or the work is refused, or the party named in the last column waives it in writing and the waiver is recorded in Section H under that party's name. The Owner and the Approver hold that authority only where they are the source.

| Criterion | Constraint or preference | If constraint: source (law, contract, policy, instruction) | If constraint: waivable? (no; or yes, and by whom: a statute by nobody in the organization, a contract by the counterparty in writing, a policy by its owner under its amendment rule, an instruction by the principal) |
|---|---|---|---|
| | | | |
| | | | |

## Section C. Trade-Off Statement (Tier 2 and above)

| Field | Entry |
|---|---|
| Privileged criterion | |
| Subordinated criterion and its floor | |
| Why this settlement | |
| Subordination accepted by (named Human) | |
| Who absorbs the subordination if it matters (affected party) | |

## Section D. Distribution Clauses (where the work carries numbers, estimates or recurring runs)

| Field | Entry |
|---|---|
| Tail test(s): error classes prohibited anywhere ("no error of class X") | |
| Tolerance and percentile per measure, applied uniformly | |
| Recurring process only: confirmation sample size, maximum variance across runs, floor for any single run | |
| Band-and-basis rule: material estimates carry uncertainty band and basis | Yes / n/a |

## Section E. Salience Audit at Define Time

One line each. See [02-salient-factors.md](../02-salient-factors.md).

1. Hostile reader: what would a hostile, competent reviewer look for first, and which test covers it?
2. Quiet giant: least discussed element with the largest consequence if wrong?
3. Unnamed party: which affected party is not yet named?
4. Naked assertion: which claim will need evidence rather than confidence?
5. Missing heading: what would a specialist expect that the expected structure omits?
6. Inherited agenda: the matter arrived framed by someone (requester, counterparty, tool); what does the framing make prominent and what does it bury?
7. Absent evidence: what must exist if the work is right, and will it be attached?

## Section F. Elimination Plan (selection tasks) and Issues Considered (all tasks)

| Field | Entry |
|---|---|
| Grounds order: infeasibility and dominance cuts precede preference cuts (selection tasks) | Confirmed / adjusted because: |
| Criterion sequence for preference cuts, with rationale for the order (selection tasks) | |
| Discard register location (what was cut, when, ground, information state, reopen condition), written as each cut is made (selection tasks) | |
| Relative cuts (top n, bottom quartile, a bar set by the field) recorded as preference cuts with their order fixed here before screening runs (selection tasks) | |
| Tool-generated option sets: the full candidate list is produced before any screening and each cut is shown as made, with criterion and ground, at the register location above; otherwise the set is treated as unvetted and the elimination is run again under this definition | Required / n/a because: |
| Retrospective explanations (the tool's or a person's account of what was discarded, given after the fact) are labeled proposed and verified against the sources before entering the register; they add candidates and never validate the set | Confirmed |
| Issues-considered list (all tasks, Tier 2 and above): the work must record which issues were treated and which were dropped, so a dropped issue is a decision rather than an absence | Required / n/a because: |

## Section G. Architecture Note

| Field | Entry |
|---|---|
| Who or what drafts | |
| Default posture (Tier 3: rejected until confirmed) | |
| Presenter and verifier separated how | |
| Not-offered test: strongest option or issue not presented must be stated by the tool, labeled proposed until the Human has verified it | Required / n/a |
| Time in the moment: when material must be available relative to the confirmation decision | |

## Section H. Amendment Log

The definition changes only by entry here. Silent drift voids the confirmation. Amendment authority is the Owner at Tiers 1 and 2 and the Owner with the Approver's sign-off at Tier 3. An imposed constraint from Section B is not amended here: it is met, or the work is refused, or its waiver by the party Section B names is recorded here with that party's name and date.

| Date | Test or criterion amended, original wording | Amended wording | Source of the requirement (preference; or constraint and its Section B source) | Why | Amended by (for a constraint: the waiving party named in Section B) |
|---|---|---|---|---|---|
| | | | | | |

---

**Defined by (Owner):** ______________________ **Date:** ______________

*Done is a decision, not an observation.*

**Final Liability rests with the Human.**
