# Order of Elimination

*Path dependence, the four mechanisms and the discard register*

Part of [The Definition of Done Is the Work of the Human](README.md) | v1.2.0 | CC BY-NC-SA 4.0

> **The closing.** *A document pulled from the data room in week one never reaches the closing set, and by closing nobody remembers it existed. Diligence teams therefore index what was removed as carefully as what remains. The index of removals is the only defense against a record that curates itself.*

---

## The claim

In any decision that selects among alternatives, candidates, issues or criteria, the order in which items are eliminated can change the outcome, and in the screens professionals actually run it usually does. This is not a marginal effect. Elimination is lossy and path-dependent: an item removed at step one is not merely disfavored, it is gone, and it takes with it the comparisons that would have disciplined every later judgment. By the final round, the survivor looks inevitable, because everything that would have made it look contestable has been deleted from view.

This matters to the Definition of Done in both directions. Many professional tasks are selection tasks: choose the vendor, the structure, the argument, the jurisdiction, the remediation. For those, the definition must govern how elimination proceeds, or the elimination order will silently decide what done means. And every task is a selection task at the level of issues: which points the work treats, which it drops. The dropped issue is the least salient object in the finished artifact, which is why this lens follows [Salient Factors](02-salient-factors.md).

## The four mechanisms

**1. Early elimination under weak information.** Items are cut earliest, when the least is known, and cuts are almost never revisited when more is learned. The information asymmetry runs exactly backwards: the decisions with the largest effect on the final option set are made on the thinnest evidence. Unless a reopen condition is recorded, the early cut is permanent by default.

**2. Criterion sequencing.** Two fixed thresholds applied independently are order-insensitive: an option that must cost no more than X and must score at least Y clears both screens in either order, because clearing both is a property of the option and not of the sequence. Sequencing bites when a cut is relative or re-baselined rather than fixed: keep the cheapest three, drop the bottom quartile, advance the top half, retain whatever clears a bar set by the best of what remains. Relative cuts are how most real screens work, because a fixed threshold requires knowing in advance where the bar belongs, and the screen applied first also decides which candidates the second screen ever examines, so information is gathered for survivors and never for the cut. Under those conditions whoever sets the screening order is choosing among outcomes while appearing to choose among procedures. When an AI performs the screening, the sequencing was chosen by nobody, which is worse. The demonstration below shows both halves on six candidates.

**3. Survivorship framing.** Each elimination round re-baselines the comparison. The final candidate is judged against the two weakest survivors rather than against the strongest option that ever existed. The Human confirming the selection sees a winner that beat its visible field and cannot see that the field was constructed by the path.

**4. Elimination by aggregation.** A weighted average eliminates by blending. An option that is fatal on one dimension survives on a good composite score, and an option that is superb where it matters dies of mediocre averages. Aggregation is an elimination mechanism that never announces itself as one. The [Risk-Informed Decision Making Prompt](https://github.com/rolldabones/risk-informed-decision-making-prompt) states the countermeasure at A5: compare alternatives at common tolerances, not on mixed bundles. The distributional version of this failure is treated in [06-averages-variances-uncertainties.md](06-averages-variances-uncertainties.md).

## A demonstration of mechanism two

Six candidates, two criteria, one screen applied after the other. Cost is in thousands. Quality is a score from 1 to 10 given by the same reviewer.

| Candidate | Cost | Quality |
|---|---|---|
| A | 10 | 9 |
| B | 4 | 5 |
| C | 5 | 6 |
| D | 6 | 8 |
| E | 8 | 8.5 |
| F | 3 | 3 |

**Fixed thresholds, either order.** Cost no more than 7 and quality at least 6. Cost first leaves B, C, D and F; quality then leaves C and D. Quality first leaves A, C, D and E; cost then leaves C and D. The survivors are C and D both ways. A fixed threshold tests a property of the candidate, so the order of two fixed thresholds cannot change who clears both.

**Relative cuts, same data, same rules.** Keep the cheapest three, then keep the best two of those on quality: F, B and C survive the cost cut, and C and B survive the quality cut. Survivors: B and C. Reverse the order, keep the best three on quality and then the cheapest two of those: A, E and D survive the quality cut, and D and E survive the cost cut. Survivors: D and E. The rules are identical, the data is identical and the two orders share no survivor. D, the better of the two candidates that clear both fixed thresholds, does not exist in the cost-first process, and nobody in that process ever compared it with anything.

The lesson for the definition of done is not that relative cuts are wrong. It is that a relative cut is a decision about outcomes, so the definition fixes the order and the grounds before the screening runs, and the record shows them as they were applied.

## The discipline

1. **Eliminate on order-insensitive grounds first.** Two grounds do not depend on sequence: infeasibility, meaning the option cannot meet an imposed constraint, and dominance, meaning the option is categorically worse than another on every measure. These are the only grounds on which early, cheap elimination is safe, and they are the grounds the companion decision prompt permits for early downselects. State the ground for each cut.
2. **Preference-based elimination comes last and is order-sensitive, so record the order.** Once cuts depend on weights, sequences or judgment, the path is part of the decision. Any relative cut (top n, bottom quartile, a bar set by the field) is a preference cut for this purpose whatever the criterion, because it depends on who else is in the field. The record states which criterion was applied at which step, to which candidates, on what information.
3. **Keep a discard register, as the work proceeds.** One line per eliminated item: what it was, when it was cut, on what ground, on what information then available and the condition that would reopen it. The line is written when the cut is made, not reconstructed afterwards, because a register reconstructed at the end is written by the survivor. The register is the antidote to mechanism one, and reopen conditions are the same discipline the decision prompt requires at A6: name the conditions that would reopen the decision.
4. **Resurrect the strongest discard at confirmation.** Before confirming a selection, write one paragraph: the strongest eliminated alternative, and whether it would still lose on what is known today. If it would not still lose, the work is not done, however finished the recommendation memo looks. In the author's practice this is the cheapest test in this repository and the one that most often catches path dependence. That is a practitioner heuristic and is labeled as one in [SOURCES.md](SOURCES.md); no measured comparison across the tests exists.
5. **Never accept silent elimination by the tool, and never accept a reconstruction as a record.** A model that presents three options has already eliminated the others, and asking it afterwards which alternatives it discarded produces a generated explanation, not evidence of what it considered. The answer is a fresh output shaped by the question. It can name candidates that were never in play and omit ones that were, and nothing in the text distinguishes the two. So the record is made as the work proceeds. For any tool-generated option set, require the full candidate list to be produced before any screening, and require each screening step to be shown with its criterion and its ground, in the order applied, before the survivors are presented. Anything the tool offers afterwards in answer to the not-offered question in [Choice Architecture](04-choice-architecture.md) is a proposed alternative: a hypothesis that a candidate was missed, to be verified by the Human against the sources and, if it holds, entered in the register under its own ground. Answering the question can add candidates to the set. It never validates the set. Where no contemporaneous record exists, the presented set is unvetted input, and the elimination is run again under the definition, by the Human or by the tool under instruction to show its steps as it takes them.

## The hook into the Definition of Done

For selection tasks, the definition of done carries two additional tests:

- The elimination record exists and was kept as the work proceeded: the candidate list before any cut, then the order, grounds and information state for every cut, with infeasibility and dominance cuts distinguished from preference cuts and relative cuts recorded as preference cuts.
- The strongest discard is named, and the confirmation includes the resurrection paragraph.
- Any retrospective explanation of what was discarded, by the tool or by a person, is labeled as proposed and verified before it enters the record.

For non-selection tasks, the same discipline applies to issues rather than options: the definition requires an issues-considered list, so that the dropped issue is a recorded decision rather than an invisible one.

---

**Final Liability rests with the Human.**
