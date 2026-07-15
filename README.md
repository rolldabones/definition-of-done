# The Definition of Done Is the Work of the Human

*Done is a decision, not an observation.*

**Son-U Michael Paik**
CEO, GRC Solutions Korea | General Counsel, BABL AI
[www.grcskorea.com](http://www.grcskorea.com)

| Version | Date | Status | License |
|---|---|---|---|
| v1.1.0 | 2026-07-15 (KST) | Final | CC BY-NC-SA 4.0 (see [License](#license)) |

AI can produce work. It cannot decide that work is done. This repository is about the two moments that cannot be delegated: defining what done means before the work begins and confirming that the work is done before anyone relies on it. It is written for professionals who use AI on work that carries consequence. Much of what lies between the two moments can be delegated in bounded ways, under the method's own gates. The bracket itself cannot be delegated at all. It is built on one principle.

**Final Liability rests with the Human.**

---

## Contents

- [The Claim](#the-claim)
- [Why the Definition of Done Is the Locus of the Three Doctrines](#why-the-definition-of-done-is-the-locus-of-the-three-doctrines)
- [The Complication: Salient Factors](#the-complication-salient-factors)
- [The Four Lenses](#the-four-lenses)
- [Where This Sits](#where-this-sits)
- [Repository Contents](#repository-contents)
- [How to Use This Repository](#how-to-use-this-repository)
- [Not the Scrum Definition of Done](#not-the-scrum-definition-of-done)
- [Design Principles](#design-principles)
- [A Note on the Closing](#a-note-on-the-closing)
- [Related Work](#related-work)
- [Part of the Ecosystem](#part-of-the-ecosystem)
- [How to Cite](#how-to-cite)
- [License](#license)
- [Changelog](#changelog)
- [About the Author](#about-the-author)

---

## The Claim

Work is done when it meets a standard that a named person can be held to. Nothing about the artifact itself establishes this. An artifact never announces its own completion. A draft does not know that it is a draft. In craft work this was obscured because production was slow and the maker's own effort supplied a rough gauge of completeness. In AI-assisted work the gauge is gone. Every output arrives looking finished. Fluency simulates completion, structure simulates coverage and confidence simulates verification.

So done must be decided, and it must be decided twice.

**Moment one: Define.** Before the work begins and before any AI touches the task, the Human states what done means: a small set of observable pass or fail tests anchored to consequence, not to effort. This is [Gate 1 of the Slow AI Kitchen](https://github.com/rolldabones/slow-ai-kitchen), stated there as three to seven tests covering substance, usability, constraints and sign-off. This repository is about what it takes to write those tests well.

**Moment two: Confirm.** After verification and before reliance, a named Human decides that the definition is met and takes the outcome. Review inspects the work. Confirmation attaches the Human to it. These are Gates 6 and 7 of the Kitchen. This repository is about what it takes to make that decision honestly.

The two moments bracket the middle, where bounded delegation happens under the method's gates. The bracket does not license wholesale delegation of what lies between: the Kitchen's Manual First Pass, for one, is never delegable to the tool. What the bracket locates is the two decisions that cannot be delegated even in part, and what makes any delegation safe is not trust in the tool. It is the integrity of the bracket. Throughout this repository the word Human is capitalized when it names the person who holds the bracket, in the same way the doctrine line capitalizes it.

## Why the Definition of Done Is the Locus of the Three Doctrines

The three doctrines of this body of work are Slow AI, Informed Intent and Final Liability. Each is stated at board altitude in [AI Governance for Boards](https://github.com/rolldabones/ai-governance-for-boards), at enterprise altitude in the [GRC Workbook](https://github.com/rolldabones/grc-workbook) and at task altitude in the [Slow AI Kitchen](https://github.com/rolldabones/slow-ai-kitchen). The Definition of Done is where all three compress into a single working artifact.

**Informed Intent.** The Definition of Done is the task-level instrument of intent. Authorization is meaningful only when the authorizing Human knows what is being authorized, and at task level that knowledge has a test: can the Human state, in advance and in observable terms, what the finished work must do? A Human who cannot state what done looks like has not formed intent. They have formed appetite. The Workbook's five conditions of valid authorization (knowledge, evidence, authority, time and permission, Module 10) apply to the confirmation moment without modification.

**Slow AI.** Slow AI places inspection at the points where work crosses a governance boundary. A gate is only as good as the standard it inspects against. The Definition of Done is that standard. A gate without a definition is a pause, not a control. The discipline of running at the speed of human verification presupposes that someone has defined what verification must establish.

**Final Liability.** Liability attaches at confirmation. The confirmation is the moment a named Human takes the outcome, and the confirmation record is the evidence that the taking was knowing. Work that is relied on without a confirmed Definition of Done is an orphaned outcome waiting for a name to be assigned after the fact, which is the standard institutional dodge the doctrine exists to prevent.

One artifact carries all three doctrines. That makes the Definition of Done the smallest unit of governance: the board directs, the enterprise builds, the professional practices, the programs deliver and at the center of all four a Human decides that work is done.

## The Complication: Salient Factors

If defining and confirming done were easy, a checklist would suffice. They are not easy, because at both moments the Human's attention is captured by Salient Factors: whatever the presentation of the work makes prominent. Salience is a property of presentation. Materiality is a property of consequence. The two correlate weakly, and AI-mediated work widens the gap, because generated output is optimized for exactly the properties that capture attention: fluency, structure, coverage and confidence.

The work of the Human is to close that gap: to discount salient factors that are not material and to hunt material factors that are not salient. [Salient Factors](02-salient-factors.md) develops the diagnosis and supplies a Salience Audit for both moments.

## The Four Lenses

Four lenses discipline the digging. Each exposes a class of material factors that salience hides.

1. **[Order of Elimination](03-order-of-elimination.md).** What was removed early was removed when the least was known, and it disappears from view. Elimination is lossy and path-dependent. The lens: record the order and grounds of every elimination and resurrect the strongest discard before confirming.
2. **[Choice Architecture](04-choice-architecture.md).** Whoever structures the options holds power over the choice without holding accountability for it. When AI mediates work, the model becomes the architect by default. The lens: own the architecture of the acceptance decision instead of inheriting it.
3. **[Trade-Offs](05-trade-offs.md).** Every real definition of done settles competing claims. Unstated trade-offs do not disappear. They are made silently by whoever controls production and discovered by whoever bears the consequence. The lens: name the settlement in the definition and verify at confirmation that the work honored it.
4. **[Averages, Variances and Uncertainties](06-averages-variances-uncertainties.md).** A standard keyed to average performance accepts work that fails where failure matters. Averages are salient. Variances and tails are not. The lens: write tail tests, state tolerances and classify what remains unknown before release.

## Where This Sits

This repository is a companion to a four-repository suite. The board directs, the enterprise builds, the professional practices and the programs deliver. This work sits at the center of the four: the moment of decision.

| Repository | Audience | Function | License |
|---|---|---|---|
| [AI Governance for Boards](https://github.com/rolldabones/ai-governance-for-boards) | Directors, officers, general counsel | Direct. What the board must own, ask and refuse | CC BY-NC-SA 4.0 |
| [GRC Workbook](https://github.com/rolldabones/grc-workbook) | GC, compliance officers, risk leaders, auditors | Build. The eighteen-module instrument on the OCEG GRC Capability Model 3.5 | CC BY-SA 4.0 |
| [Slow AI Kitchen](https://github.com/rolldabones/slow-ai-kitchen) | Individual professionals, team leads, program owners | Practice. The twelve-step, ten-gate method for governed AI use | CC BY-NC-SA 4.0 |
| [AI Governance Academy](https://github.com/rolldabones/AI-Governance-Academy) | Advisors and organizations engaging structured delivery | Deliver. Engagement templates for six structured programs | CC BY-NC-SA 4.0 |
| **The Definition of Done** (this repository) | The Human at the moment of acceptance | Decide. How done is defined and confirmed under the three doctrines | CC BY-NC-SA 4.0 |

The relationship to the Kitchen is deliberate and narrow. The Kitchen establishes Gate 1 (Definition of Done) and confirms against it at Gate 6 (Verification and Validation) and Gate 7 (Human Release Decision). The Kitchen tells you where the gates are. This repository is the depth work inside those gates: what a Human must actually think about to define and confirm done on a real task with real stakes. Nothing here modifies the method. Where this repository and the Kitchen conflict, the Kitchen controls.

The relationship to the Academy is instructional. The material here is designed to be taught: it supplies the doctrinal depth for the Definition of Done segments of the Practitioner Academy and the Executive Workshop, and the [worked example](examples/worked-example-dpa-review.md) and [interrogation prompt](prompts/dod-interrogator.md) are built to run as classroom exercises.

## Repository Contents

| File | What it is | Use it when |
|---|---|---|
| [README.md](README.md) | The canonical statement: claim, doctrines, complication, lenses | Always; every other file defers to this one |
| [00-quick-start.md](00-quick-start.md) | The minimal loop, a worked miniature and the deadline rule | You want to run this on a real task in the next ten minutes |
| [01-done-is-a-decision.md](01-done-is-a-decision.md) | The two moments, the bracket, exploratory work, the amendment protocol and the six false forms of done | You want the thesis in full |
| [02-salient-factors.md](02-salient-factors.md) | Salience against materiality, the four distortions of AI-mediated work and the Salience Audit | You are writing or confirming a definition today |
| [03-order-of-elimination.md](03-order-of-elimination.md) | Path dependence in elimination, the four mechanisms and the discard register | The task selects among alternatives, issues or candidates |
| [04-choice-architecture.md](04-choice-architecture.md) | Defaults, anchors, framing and the asymmetry of accepting against rejecting | AI drafted the options or the work you are about to accept |
| [05-trade-offs.md](05-trade-offs.md) | The settlement behind every definition, constraints against preferences and trade drift | Criteria compete and something must give |
| [06-averages-variances-uncertainties.md](06-averages-variances-uncertainties.md) | The flaw of averages, tail tests, the single-run illusion and uncertainty routing | The work carries numbers, estimates or recurring runs |
| [07-the-confirmation.md](07-the-confirmation.md) | The confirmation protocol, the three lawful outcomes and confirming under pressure | You are about to say the work is done |
| [templates/definition-of-done-template.md](templates/definition-of-done-template.md) | The define-side instrument | Moment one |
| [templates/confirmation-record-template.md](templates/confirmation-record-template.md) | The confirm-side instrument | Moment two |
| [examples/worked-example-dpa-review.md](examples/worked-example-dpa-review.md) | One task run through both instruments, including a refusal | You want to see the method on a real deliverable |
| [prompts/dod-interrogator.md](prompts/dod-interrogator.md) | A model-agnostic prompt that interrogates a draft definition without authoring it | You want the discipline challenged inside the AI session |

## How to Use This Repository

**One professional, one task, today.** Start with the [Quick Start](00-quick-start.md): the minimal loop and a worked miniature, one page. It needs nothing else in the repository to work.

**One professional, one task, properly.** Read [01](01-done-is-a-decision.md) and [02](02-salient-factors.md), then open the [Definition of Done template](templates/definition-of-done-template.md) and write the definition before you prompt anything. Consult the lens files as the task demands: [03](03-order-of-elimination.md) when selecting, [04](04-choice-architecture.md) when AI frames the options, [05](05-trade-offs.md) when criteria compete, [06](06-averages-variances-uncertainties.md) when the work carries numbers.

**Confirming today.** Read [07](07-the-confirmation.md) and complete the [Confirmation Record](templates/confirmation-record-template.md). Three outcomes are available. Pick one and sign it.

**A team lead or trainer.** Run the [worked example](examples/worked-example-dpa-review.md) as an exercise: give the team the task, have them write the definition cold, then compare against the worked instrument. Load the [interrogator prompt](prompts/dod-interrogator.md) as the session prompt so the discipline is enforced inside the tool.

**An Academy facilitator.** The seven numbered files map to a half-day module. Files 01 and 02 are the instruction block, files 03 through 06 are breakout lenses and file 07 plus the templates are the closing exercise.

## Not the Scrum Definition of Done

The term Definition of Done has an honorable lineage in agile software practice, where it names a team convention for shippability: the checklist an increment must satisfy before it counts as complete. This repository keeps the term and changes the register. Here the Definition of Done is a liability instrument, not a team convention. The difference is who can be held to it. An agile team's definition binds a process. The definition here attaches an outcome to a named Human with decision rights, oversight and the power to intervene. Practitioners who know the agile term will find the mechanics familiar and the stakes changed.

## Design Principles

1. **The definition precedes the draft.** A definition written after the output exists is a rationalization with a checklist format. The only anchor that can compete with the model's anchor is the one set before the model speaks.
2. **The tool may question the definition. It may not author it.** AI is a capable interrogator of acceptance criteria and a disqualified author of them, because the author of the standard controls the outcome of the test. The [interrogator prompt](prompts/dod-interrogator.md) enforces this boundary in the session itself.
3. **Confirmation has three lawful outcomes.** Confirm, refuse or amend and confirm, each with a record. There is no fourth outcome. Done enough given the deadline is an amendment seeking anonymity.
4. **Salience is data about presentation, not about the world.** Prominence tells you what the presentation rewards. It tells you nothing about consequence until you check.
5. **One doctrine set across the suite.** Slow AI, Informed Intent and Final Liability are used here exactly as stated in the companion repositories. This repository adds instruments, not doctrine.

## A Note on the Closing

The GRC Workbook uses the mechanical watch as its recurring illustration and the Kitchen uses the professional kitchen. This repository uses the closing: the moment in a negotiated transaction when a deal becomes done. The closing earns its place because it is the oldest working Definition of Done in professional life. Done is defined at signing as conditions precedent. Done is confirmed at closing by bring-down certificates that a named person signs. Waivers are express, recorded and owned. Nobody at a closing table asks whether the deal feels closed. The closing is a thinking aid, not a thesis. Readers who prefer to read past it lose nothing of the method.

## Related Work

- [Slow AI Kitchen](https://github.com/rolldabones/slow-ai-kitchen): the method this repository deepens at Gates 1, 6 and 7.
- [GRC Workbook](https://github.com/rolldabones/grc-workbook): Modules 10 through 12 supply the enterprise-altitude doctrine this repository applies at task altitude.
- [AI Governance for Boards](https://github.com/rolldabones/ai-governance-for-boards): the board layer, including the appetite and oversight language that task-level definitions roll up into.
- [AI Governance Academy](https://github.com/rolldabones/AI-Governance-Academy): the delivery programs this material is taught through.
- [Risk-Informed Decision Making Prompt](https://github.com/rolldabones/risk-informed-decision-making-prompt): the companion decision scaffold whose downselect grounds, tolerance discipline and uncertainty treatment this repository builds on.
- [GRCnext™ Copilot](https://github.com/rolldabones/grcnext-copilot): evidence-led assessment of executable optionality at enterprise scale. Its rule that only verified evidence earns verified credit is the program-level analogue of the confirmation record, and completed confirmation records are the kind of recoverable evidence its method credits.
- **Final Liability Rests with the Human** (book): [github.com/rolldabones/final-liability-rests-with-the-human-book-wip](https://github.com/rolldabones/final-liability-rests-with-the-human-book-wip).

## Part of the Ecosystem

This repository is part of the [rolldabones governance ecosystem](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md), classified in Layer 1 (doctrine and method). The Where This Sits section above describes its function inside the four-repository suite; the canonical map places all repositories in one structure. Nearest neighbors:

- [slow-ai-kitchen](https://github.com/rolldabones/slow-ai-kitchen) - the method whose Gates 1, 6 and 7 this repository is the depth work inside
- [origami-method](https://github.com/rolldabones/origami-method) - the workflow discipline whose context packet begins with a definition of done
- [grc-workbook](https://github.com/rolldabones/grc-workbook) - the enterprise instrument whose evidence and sign-off modules the Confirmation Record serves
- [ai-governance-for-boards](https://github.com/rolldabones/ai-governance-for-boards) - the board mandate that makes the accountable Human's decision rights explicit
- [AI-Governance-Academy](https://github.com/rolldabones/AI-Governance-Academy) - the delivery programs this material is taught through

## How to Cite

> Paik, Son-U Michael. *The Definition of Done Is the Work of the Human*, v1.1.0. GRC Solutions Korea, 2026. https://github.com/rolldabones/definition-of-done

## License

This repository is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0). You may share and adapt this material for non-commercial purposes provided you give appropriate credit, indicate if changes were made and distribute your contributions under the same license. Commercial use requires the author's prior written permission.

Suggested attribution: "The Definition of Done Is the Work of the Human by Son-U Michael Paik, GRC Solutions Korea, licensed under CC BY-NC-SA 4.0."

Full license text: https://creativecommons.org/licenses/by-nc-sa/4.0/

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## About the Author

Son-U Michael Paik is an attorney, AI auditor and governance architect with more than 25 years of experience designing risk and compliance systems for cross-border institutions in regulated, high-stakes sectors across Asia, Europe and the United States. He is General Counsel at BABL.ai, a global AI audit provider, and Founder and Chief Executive Officer of GRC Solutions Korea. He holds a Juris Doctor from Columbia Law School, a Master of Business Administration from the Yale School of Management and a Bachelor of Arts in Economics from Syracuse University, is admitted to the New York Bar and holds AI audit certifications from BABL.ai and ForHumanity, including certifications under the EU AI Act, GDPR and the Digital Services Act.

**GRC Solutions Korea:** [www.grcskorea.com](http://www.grcskorea.com)
**LinkedIn:** [linkedin.com/in/sonupaik](https://linkedin.com/in/sonupaik)

---

*Done is a decision, not an observation.*

**Final Liability rests with the Human.**
