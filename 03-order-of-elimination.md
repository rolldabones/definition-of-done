# Order of Elimination

*Path dependence, the four mechanisms and the discard register*

Part of [The Definition of Done Is the Work of the Human](README.md) | v1.0.0 | CC BY-NC-SA 4.0

> **The closing.** *A document pulled from the data room in week one never reaches the closing set, and by closing nobody remembers it existed. Diligence teams therefore index what was removed as carefully as what remains. The index of removals is the only defense against a record that curates itself.*

---

## The claim

In any decision that selects among alternatives, candidates, issues or criteria, the order in which items are eliminated changes the outcome. This is not a marginal effect. Elimination is lossy and path-dependent: an item removed at step one is not merely disfavored, it is gone, and it takes with it the comparisons that would have disciplined every later judgment. By the final round, the survivor looks inevitable, because everything that would have made it look contestable has been deleted from view.

This matters to the Definition of Done in both directions. Many professional tasks are selection tasks: choose the vendor, the structure, the argument, the jurisdiction, the remediation. For those, the definition must govern how elimination proceeds, or the elimination order will silently decide what done means. And every task is a selection task at the level of issues: which points the work treats, which it drops. The dropped issue is the least salient object in the finished artifact, which is why this lens follows [Salient Factors](02-salient-factors.md).

## The four mechanisms

**1. Early elimination under weak information.** Items are cut earliest, when the least is known, and cuts are almost never revisited when more is learned. The information asymmetry runs exactly backwards: the decisions with the largest effect on the final option set are made on the thinnest evidence. Unless a reopen condition is recorded, the early cut is permanent by default.

**2. Criterion sequencing.** Screening by cost first and quality second yields a different surviving set than quality first and cost second, even when the thresholds are identical. Whoever sets the screening order is choosing among outcomes while appearing to choose among procedures. When an AI performs the screening, the sequencing was chosen by nobody, which is worse.

**3. Survivorship framing.** Each elimination round re-baselines the comparison. The final candidate is judged against the two weakest survivors rather than against the strongest option that ever existed. The Human confirming the selection sees a winner that beat its visible field and cannot see that the field was constructed by the path.

**4. Elimination by aggregation.** A weighted average eliminates by blending. An option that is fatal on one dimension survives on a good composite score, and an option that is superb where it matters dies of mediocre averages. Aggregation is an elimination mechanism that never announces itself as one. The [Risk-Informed Decision Making Prompt](https://github.com/rolldabones/risk-informed-decision-making-prompt) states the countermeasure at A5: compare alternatives at common tolerances, not on mixed bundles. The distributional version of this failure is treated in [06-averages-variances-uncertainties.md](06-averages-variances-uncertainties.md).

## The discipline

1. **Eliminate on order-insensitive grounds first.** Two grounds do not depend on sequence: infeasibility, meaning the option cannot meet an imposed constraint, and dominance, meaning the option is categorically worse than another on every measure. These are the only grounds on which early, cheap elimination is safe, and they are the grounds the companion decision prompt permits for early downselects. State the ground for each cut.
2. **Preference-based elimination comes last and is order-sensitive, so record the order.** Once cuts depend on weights, sequences or judgment, the path is part of the decision. The record states which criterion was applied at which step, to which candidates, on what information.
3. **Keep a discard register.** One line per eliminated item: what it was, when it was cut, on what ground, on what information then available and the condition that would reopen it. The register is the antidote to mechanism one, and reopen conditions are the same discipline the decision prompt requires at A6: name the conditions that would reopen the decision.
4. **Resurrect the strongest discard at confirmation.** Before confirming a selection, write one paragraph: the strongest eliminated alternative, and whether it would still lose on what is known today. If it would not still lose, the work is not done, however finished the recommendation memo looks. This is the single cheapest test in this repository and it catches path dependence more often than any other.
5. **Never accept silent elimination by the tool.** A model that presents three options has already eliminated the others. Either demand the elimination record (what was considered, what was cut, on what ground) or treat the presented set as unvetted input rather than as a decision-ready menu. The strongest option the model did not present is a standing entry in the Salience Audit and in [Choice Architecture](04-choice-architecture.md).

## The hook into the Definition of Done

For selection tasks, the definition of done carries two additional tests:

- The elimination record exists: order, grounds and information state for every cut, with infeasibility and dominance cuts distinguished from preference cuts.
- The strongest discard is named, and the confirmation includes the resurrection paragraph.

For non-selection tasks, the same discipline applies to issues rather than options: the definition requires an issues-considered list, so that the dropped issue is a recorded decision rather than an invisible one.

---

**Final Liability rests with the Human.**
