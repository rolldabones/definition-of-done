# Trade-Offs

*The settlement behind every definition, constraints against preferences and trade drift*

Part of [The Definition of Done Is the Work of the Human](README.md) | v1.2.0 | CC BY-NC-SA 4.0

> **The closing.** *A signed agreement is a record of trades. The representations that survived, the ones that died in redline and the ones that came back qualified by knowledge and materiality tell the truth of the negotiation more plainly than the recitals do. Nobody reads a contract as a description of the world. It is read as a settlement between parties who wanted incompatible things.*

---

## The claim

Done is a settlement. Every real definition of done resolves competing claims: speed against completeness, precision against recall, cost against assurance, depth against coverage, standardization against fit, confidentiality against explainability. A definition that acknowledges no trade-off was written either for a task with no stakes or by someone who has not yet found where the stakes are. The tests in a definition are the terms of the settlement, and like any settlement, what was given up is as much a part of the deal as what was obtained.

The governing rule: unstated trade-offs do not disappear. They are still made, silently, by whoever controls production at the moment of least visibility, and they are discovered by whoever bears the consequence. In AI-assisted work the party who controls production at the moment of least visibility is the model. A model told to be thorough and brief will trade one against the other somewhere in the document, on grounds nobody chose, differently on each run. The choice does not vanish because it went unstated. It merely stops being the Human's.

## The discipline

**1. Name the settlement.** Every definition of done at Tier 2 or above (the README's [tier table](README.md#proportionate-use-the-tier-table)) carries a trade-off statement: what is privileged, what is subordinated, why and who accepts the subordination. Four lines. The named acceptor is a Human, never the tool and never the deadline. Writing the statement is uncomfortable in exactly the way that matters: it converts a diffuse sense that everything is important into an owned decision that some things will yield.

**2. Fix the boundary between constraints and preferences.** Some criteria are not tradeable. An imposed constraint disqualifies any output that cannot meet it: the legal floor, the safety floor, the data that must not leave the jurisdiction, the representation that must not be made. The companion decision prompt builds this into A2 as hard limits that disqualify, and the worked example there turns on it: an alternative that fails an imposed constraint does not get to be good at other things. The boundary itself is a decision. Classify every criterion as constraint or preference in the definition, because the classification is where the real authority is exercised, and an unclassified criterion will be traded by whoever touches the work next. For each constraint the instrument records three more things: its source, whether it can be waived at all and who holds the authority to waive it. A statutory floor is waived by nobody in the organization. A contractual term is waived by the counterparty, in writing. A policy rule is waived by the policy's owner under the policy's own amendment rule. An instruction is waived by the principal who gave it. The Owner and the Approver appear on that list only when they are the source, and the amendment protocol in [01-done-is-a-decision.md](01-done-is-a-decision.md) stops at this line: an unmet constraint is never amended away, it is met, or refused, or waived by the party named here with the waiver recorded.

**3. Compare at common tolerances.** When trade-offs must be evaluated across options or drafts, hold the tolerance fixed and compare like against like. The A5 discipline applies verbatim: compare at common tolerances, not on mixed performance-and-confidence bundles. A draft that is better on average and worse at the tolerance is worse. The distributional machinery for this is in [06-averages-variances-uncertainties.md](06-averages-variances-uncertainties.md).

**4. Watch for trade drift.** Trade-offs renegotiate themselves silently in the middle of work. Scope creep is a trade-off amendment without a record. So is the model's tendency to improve the property it is best at (coverage, polish) at the expense of the property the definition privileged (brevity, precision, a locked structure). The amendment protocol from [01-done-is-a-decision.md](01-done-is-a-decision.md) governs: the settlement changes only by recorded amendment, and drift discovered at confirmation means the work is not done.

**5. Separate who benefits from who pays.** A trade-off has a distributional footprint. Speed obtained by the drafting team is paid for by the reviewer who inherits a thinner evidence trail, or by the affected party who inherits the error rate. The Kitchen's Gate 3 question extends naturally: for each subordinated criterion, who absorbs the subordination if it turns out to matter? A settlement whose costs land on parties absent from the room is the kind that fails in public later.

## Confirming against the settlement

At confirmation, re-read the trade-off statement before re-reading the work, and ask one question: did the work honor the settlement or quietly re-trade it? The common finding is a document that improved along the dimensions the model finds easy and paid for it along the dimension the definition privileged. That is not a quality failure in the ordinary sense. The work may be objectively better by page count and polish. It is a governance failure: the settlement was renegotiated by a party with no authority to negotiate.

The confirmation record therefore carries a trade-off honor check: privileged criterion held or not, subordinated criterion held at its floor or not, any re-trade found and, if found, whether it is refused or adopted by recorded amendment. Adopting a good re-trade is permitted. Adopting it silently is not. The difference is a signature. One re-trade is never adoptable by amendment: a constraint from Section B that the work has not met. The record checks the constraints before it offers the amend and confirm outcome, and while any applicable constraint is unmet and unwaived by its source the only outcome available is refuse.

---

**Final Liability rests with the Human.**
