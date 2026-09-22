# Sources and Evidence Status

*What the chapters' empirical claims rest on*

Part of [The Definition of Done Is the Work of the Human](README.md) | v1.2.0 | CC BY-NC-SA 4.0

This repository asks the Human to distinguish the confidence of the prose from the state of the record. This file applies that rule to the repository itself. Every claim in the chapters that asserts something about how people or systems behave is listed here with its source, where one exists, and with one of four labels. A claim with no entry here is doctrine, method or argument, which the reader accepts or rejects on its reasoning, not a claim about the world.

**The four labels.**

- **Established.** Published, peer-reviewed or canonical work states the finding and the chapter uses it as stated.
- **Supported, partial.** Published work supports the direction of the claim; the effect is partial, the studied population differs from professional acceptance decisions, or the chapter's application goes beyond what was measured. The chapter says so.
- **Practitioner heuristic** (or practitioner observation). The author's working rule, or repeated observation, from practice. Stated as such, not as a finding, and with no comparison claimed that was not measured.
- **Author's characterization.** A restatement or extension of an established finding in this repository's vocabulary. The restatement is the author's, the finding is not.

Comparatives that could not be supported ("more often than any other", "neutralizes most of") were removed from the chapters in v1.2.0 and are recorded below under the claims they qualified.

---

## 02-salient-factors.md

| Claim in the chapter | Source | Status |
|---|---|---|
| What comes to mind easily is judged more frequent and more important | Tversky, A. and Kahneman, D. (1973). Availability: a heuristic for judging frequency and probability. *Cognitive Psychology*, 5(2), 207 to 232. | Established |
| What is out of sight is, in practice, priced at approximately zero | Extension of the availability finding to the acceptance decision | Author's characterization |
| Generated output is optimized for the properties that capture attention (fluency, structure, coverage, confidence) and is indifferent to materiality | No study cited; an argument from what a text generator is trained to produce | Practitioner heuristic |

## 03-order-of-elimination.md

| Claim in the chapter | Source | Status |
|---|---|---|
| Two fixed thresholds applied independently produce the same survivors in either order; relative or re-baselined cuts can produce different survivors in different orders | Arithmetic; demonstrated in the chapter on six candidates | Established (by demonstration) |
| Early cuts are made on the thinnest evidence and are rarely revisited | No study cited | Practitioner heuristic |
| Resurrecting the strongest discard is the cheapest test in this repository and the one that most often catches path dependence | The author's practice. Until v1.2.0 the chapter read "catches path dependence more often than any other"; no measured comparison across the tests exists and the comparative was removed | Practitioner heuristic |
| A weighted average lets an option that is fatal on one dimension survive on its composite | Arithmetic | Established |

## 04-choice-architecture.md

| Claim in the chapter | Source | Status |
|---|---|---|
| Choice architecture is never neutral; the term and the argument | Thaler, R. H. and Sunstein, C. R. (2008). *Nudge: Improving Decisions About Health, Wealth, and Happiness*. Yale University Press. | Established |
| The first number or structure presented anchors subsequent judgment | Tversky, A. and Kahneman, D. (1974). Judgment under uncertainty: heuristics and biases. *Science*, 185(4157), 1124 to 1131. | Established |
| Presenting the same decision as gains or as losses changes the choice | Tversky, A. and Kahneman, D. (1981). The framing of decisions and the psychology of choice. *Science*, 211(4481), 453 to 458. | Established |
| Considering the opposite reduces biased assimilation of evidence | Lord, C. G., Lepper, M. R. and Preston, E. (1984). Considering the opposite: a corrective strategy for social judgment. *Journal of Personality and Social Psychology*, 47(6), 1231 to 1243. | Established |
| Considering the opposite compensates for anchoring | Mussweiler, T., Strack, F. and Pfeiffer, T. (2000). Overcoming the inevitable anchoring effect: considering the opposite compensates for selective accessibility. *Personality and Social Psychology Bulletin*, 26(9), 1142 to 1150. | Established |
| A structured listing of each option's advantages and disadvantages removed the framing effect in the studied vignettes | Almashat, S., Ayotte, B., Edelstein, B. and Margrett, J. (2008). Framing effect debiasing in medical decision making. *Patient Education and Counseling*, 71(1), 102 to 107. Undergraduate sample, medical treatment vignettes, control group engaged in comparable cognitive activity; the finding is established on that population and not measured on any other. | Established |
| One deliberate reframe reduces the framing distortion in a professional acceptance decision | Application of the three studies above to a setting none of them measured. Until v1.2.0 the chapter read "neutralizes most of the framing effect"; no study supports "most" and the word was removed | Supported, partial |
| Accepting AI output is the default because rejecting costs more effort than accepting | No study cited; an argument from the asymmetry of effort | Practitioner heuristic |

## 06-averages-variances-uncertainties.md

| Claim in the chapter | Source | Status |
|---|---|---|
| Plans evaluated at the average of their inputs are systematically wrong: the flaw of averages | Savage, S. L. (2002). The flaw of averages. *Harvard Business Review*, November 2002. Savage, S. L. (2009). *The Flaw of Averages: Why We Underestimate Risk in the Face of Uncertainty*. Wiley. | Established |
| When consequences are nonlinear, the outcome at the average is not the average of the outcomes | Jensen, J. L. W. V. (1906). Sur les fonctions convexes et les inégalités entre les valeurs moyennes. *Acta Mathematica*, 30, 175 to 193. | Established |
| The same prompt, model and documents produce different work across runs, and the differences are often material | The author's practice for the second clause. The first clause is a property of sampled generation and is not disputed; the frequency and materiality of the differences are not measured here, and the chapter now tells recurring processes to measure their own spread | Practitioner observation |

## The closing illustration

The recurring closing-table illustration in the chapters (conditions precedent, bring-down certificates, express waivers) describes ordinary practice in negotiated transactions. It is offered as a thinking aid and makes no empirical claim.

---

## Maintenance

A new empirical claim in any chapter adds a row here in the same release. A comparative that cannot be sourced is not written. When a source is superseded or a claim is re-labeled, the change is logged in [CHANGELOG.md](CHANGELOG.md).

**Final Liability rests with the Human.**
