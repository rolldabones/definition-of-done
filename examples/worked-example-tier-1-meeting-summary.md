# Worked Example: A Tier 1 Meeting Summary

Part of [The Definition of Done Is the Work of the Human](../README.md) | v1.2.0 | CC BY-NC-SA 4.0

The minimum paperwork. One professional, one low-stakes task, both instruments completed at the depth the README's [tier table](../README.md#proportionate-use-the-tier-table) requires for Tier 1: Sections 0, A and H of the definition, Sections 0, 1, 5 and 6 of the record, one to three tests. Everything below took about ten minutes around the assistant's work. Names are placeholders. For the full apparatus at the other end of the scale, see the [DPA review example](worked-example-dpa-review.md).

---

## The task

A project lead posts a summary of the weekly project meeting to the team channel: one paragraph, the decisions taken and the action list. The meeting was recorded and transcribed. An approved assistant drafts the summary from the transcript. Eight people attended and two who did not will read the post.

## The Definition of Done (Sections 0, A and H)

**Section 0.**

| Field | Entry |
|---|---|
| Task (one sentence) | Post a summary of Tuesday's project meeting to the team channel: one paragraph, decisions taken, action list |
| Date and timezone | Tuesday, 14:10, Asia/Seoul |
| Risk tier with one-line basis | Tier 1: internal, non-public, read by the people who were in the room, no decision rests on it alone |
| Intended use of the output | Team channel post; the action list is the team's working reminder until the next meeting |
| Audience | The eight attendees and two absentees |
| Decision the output supports | None directly; the action list assigns follow-ups already agreed in the meeting |
| Non-recoverable domain, if any | None |
| Method version | definition-of-done v1.2.0 |
| Instrument version | Definition of Done template v1.2.0 |
| Kitchen version applied | Slow AI Kitchen v2.9.1 |

Roles: the project lead holds every role (Preparer, Builder, Reviewer, Owner), as Tier 1 permits. Review is still a separate act against the tests, after the draft exists.

**Section A. Tests.** Three, the Tier 1 maximum. Test 1 hunts an absence, which the tier table recommends and does not require at Tier 1. Test 3 restates an imposed constraint and is marked as one, which is how Tier 1 carries Section B without completing it.

| # | Test (pass/fail) | Evidence expected at confirmation |
|---|---|---|
| 1 | Every action item names an owner and a date, and every action item was actually assigned in the meeting; an item the transcript does not support is deleted, not repaired | Each action item searched for in the transcript, with the timestamp noted |
| 2 | Every item listed as a decision was stated as decided in the meeting, not merely discussed; discussed items go under a separate "raised, not decided" line | Each decision searched for in the transcript, with the timestamp noted |
| 3 | (constraint) The post contains no client names or client personal data; the transcript was redacted before it reached the assistant. Source: tool registry rule on client data in AI tools. Waivable: no | Search of the post against the client list, zero hits; redaction confirmed before upload |

**Section H. Amendment log.** No entry. The definition was not amended.

## What happened

The lead read the transcript once (Kitchen Gate 2, the light form: a skim and a five-line outline of what was decided), redacted two client names, then had the assistant draft the summary and the action list. The draft was fluent and complete-looking. It listed five action items and three decisions.

## The Confirmation Record (Sections 0, 1, 5 and 6)

**Section 0.** Artifact: meeting summary, draft 1 then draft 2. Definition: the three tests above, amendment log empty. Tier 1. Confirmer: the project lead, Owner. Date and time: Tuesday 14:40, Asia/Seoul; material available since 14:25. Method versions: definition-of-done v1.2.0, Confirmation Record template v1.2.0, Slow AI Kitchen v2.9.1.

**Section 1, first run, against draft 1.**

| # | Test | Pass / Fail | Evidence |
|---|---|---|---|
| 1 | Action items assigned in the meeting, with owner and date | Pass | Five items, five found in the transcript (00:12, 00:19, 00:27, 00:41, 00:52). The item at 00:41 was assigned to nobody in the meeting; the assistant had given it an owner. Owner removed and the item marked "unassigned, raise Thursday" rather than repaired |
| 2 | Decisions were decided, not discussed | Fail | Three decisions listed. Two found as decided (00:33, 00:48). The third, "launch moved to October", was proposed at 00:44 and deferred at 00:46; the transcript has nobody deciding it |
| 3 | (constraint) No client names or client personal data | Pass | Post searched against the client list, zero hits; redaction done before upload |

**Section 5, first run.** Constraint check: the one constraint is Met. Outcome: **Refuse.** Failed test 2, returned to self. The fix took two minutes: the October item moved to "raised, not decided".

**Section 1, second run, against draft 2.** Test 1 pass, unchanged. Test 2 pass: two decisions listed, both found as decided; one item under "raised, not decided". Test 3 pass, unchanged.

**Section 5, second run.** Constraint check: Met. Outcome: **Confirm.**

**Section 6. Scope of release.** Released for: the team channel post. Released to: the project team. Valid until: the next weekly meeting. Reopen conditions: any attendee's correction in the channel, which the lead applies and notes. Remediation or rollback plan: not required at Tier 1; a corrected post replaces the original.

## What the example teaches

Tier 1 does not mean no definition. It means three tests and four record sections, written in the time the assistant takes to draft. The refusal cost two minutes and prevented a decision that nobody took from becoming the team's record of a decision that was taken, which is the small, ordinary way that fluent drafts rewrite what happened. The test that caught it was written before the draft existed. That is the whole method, at its smallest.

---

**Final Liability rests with the Human.**
