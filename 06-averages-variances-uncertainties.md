# Averages, Variances and Uncertainties

*The flaw of averages, tail tests, the single-run illusion and uncertainty routing*

Part of [The Definition of Done Is the Work of the Human](README.md) | v1.0.0 | CC BY-NC-SA 4.0

> **The closing.** *Parties refuse to close on averages. Purchase price adjustments, escrows, earn-outs and holdbacks exist because a number that is right on average and wrong in this deal is wrong. The closing mechanics of every substantial transaction are variance instruments, negotiated by people who understood that the mean is not the outcome.*

---

## The claim

A definition of done stated as a point estimate, or confirmed on average performance, will accept work that fails exactly where failure matters. The average is the most salient summary a body of work produces and among the least informative for an acceptance decision, because acceptance is about consequence, consequence lives in particular outcomes and particular outcomes are draws from a distribution, not visits to its mean.

The general result has a name in the decision literature: the flaw of averages, the error of evaluating a plan at the average of its inputs. Its formal engine is Jensen's inequality, which needs no formula to use: when consequences are nonlinear, the outcome at the average is not the average of the outcomes. Every professional task with a floor, a cap, a threshold or a penalty is nonlinear. That is nearly every task worth defining done for.

## The four failure patterns

**1. Average quality, fatal tail.** A contract review that is right 95 percent of the time is not 95 percent done. Done is a function of which five percent is wrong and what those errors cost. An error distribution with a benign mean and a catastrophic tail (the missed exclusivity clause, the wrong governing law, the liability cap off by a factor of ten) fails any honest definition, while sailing through any average-based one. Where consequence is asymmetric, the mean is close to irrelevant.

**2. Averaged criteria.** Scoring a deliverable as a composite across criteria lets excellence in the easy dimensions subsidize failure in the material one. This is elimination by aggregation from [Order of Elimination](03-order-of-elimination.md), now operating on the acceptance decision itself: formatting, fluency and coverage average out a substantive miss. Pass or fail per test, no composites, is the countermeasure, and it is why the Kitchen's Gate 1 specifies pass or fail tests rather than scores.

**3. The single-run illusion.** An AI deliverable is one draw from a distribution over outputs. The same prompt, the same model and the same documents produce materially different work across runs. Judging the system by one polished draw is judging a die by one roll. For one-off tasks this argues for verification depth matched to the tier. For recurring tasks (the triage that runs weekly, the template that fills monthly) the definition of done governs the distribution, not the draw: it states re-run stability requirements, the acceptable variance across runs and the worst draw the process may produce, and confirmation samples accordingly. A recurring process confirmed on its best output has not been confirmed.

**4. Uncertainty laundering.** A point estimate presented without its band converts uncertainty into false precision, and generated prose launders this conversion at scale, because the model's register is equally settled at every confidence level. The companion decision prompt states the countermeasures as core discipline: characterize uncertainty as a distribution where evidence supports one and as a bounded qualitative range where it does not, record the basis for every estimate and report bands, not false precision. A material number arriving in the work without a band and a basis is not a fact. It is a decoration shaped like one.

## The discipline for the definition

1. **Write tail tests beside mean tests.** For every material quality dimension: one test at the level of overall performance and one at the level of the worst permissible instance. The form is "no error of class X anywhere" alongside "accuracy of at least Y overall". Class X is defined by consequence: the error classes that are non-recoverable for the intended use.
2. **State the tolerance and the percentile.** Where the work is quantifiable, the definition states the risk tolerance per measure and the percentile at which it is evaluated, uniformly. The A5 discipline transfers whole: evaluate at the stated tolerance (for example the 95th percentile worst case), compare like against like and show mean and tail separately, because an option or draft that looks worst at the mean can be best against the tail and the reverse.
3. **Bound the recurring process.** For tasks that will run repeatedly, the definition adds distribution clauses: sample size for confirmation, maximum variance across runs and the floor below which no single run may fall.
4. **Demand the band and the basis.** Any material estimate in the work carries its uncertainty band and the basis on which it rests: the data, the expert, the assumption. Unbanded numbers are returned, not debated.

## The discipline for the confirmation

Classify what remains uncertain at confirmation and route it by type, because the types demand different actions and confusing them wastes the response. The routing follows the companion prompt's uncertainty treatment.

- **Aleatory** (irreducible randomness): cannot be researched away. Design margin, hold reserve or accept, and say so in the record.
- **Epistemic** (reducible by knowledge): either close it before confirming or place it under Watch with named parameters, a named schedule and named triggers. All three are required, or it is not a Watch, it is a hope.
- **Endpoint** (the target itself is ill-defined): the definition of done is the defect. Amend it by the recorded protocol before confirming anything against it.

The confirmation record then states the residual: what remains unknown, of what type, and why release is defensible anyway. Unknown is an admissible entry in an honest record. False precision is not. A confirmation that admits its residual uncertainty in writing is stronger evidence of Informed Intent than one that claims none, because the reviewer who was not present can see that the Human saw the edge.

---

**Final Liability rests with the Human.**
