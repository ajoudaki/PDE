# Endpoint separation: what the new arguments establish

2026-10-11. Continuation of the endpoint part of this study. The requested
removal of the training-span restriction is **not established**. This note
records two concrete advances and the exact remaining implication; it does
not replace the current endpoint theorem or modify the paper.

## The requested theorem

Keep the canonical Gaussian-initialized, fully trained network in
`paper/compact.tex`, fixed depth, layerwise nonaffine strip-analytic
activations with bounded strip derivative but possibly unbounded values,
positive training feature-Gram gap, fixed nonzero labels, and exactly the
original label cap. All parameters except width are fixed separately.

The desired extension would give, at every fixed confidence, a constant
\(c_\delta>0\) independent of width such that eventually

\[
\Pr\!\left\{
\sup_{x\in\mathcal X}
 |f_n(\infty,x)-\widetilde f_n(\infty,x)|
 \ge \frac{c_\delta}{\sqrt n}
\right\}\ge1-\delta.
\]

Here the dense runs are independent, and the query domain is either the
separated part of the input sphere or a fixed declared test panel. The
extension must allow the training inputs to span all of input space. It is
not enough to show positive finite-width variance, initialized full rank,
or a lower bound for frozen-feature regression.

For the entire admitted activation class the meaningful pointwise/panel
separation condition is

\[
\min_{1\le a\le m}\min\{\|x-x_a\|,\|x+x_a\|\}\ge\epsilon>0.
\]

This removes both a training point and its antipode. Distance only from the
training points cannot suffice for every panel: an even first activation
forces \(f_n(t,-x_a)=f_n(t,x_a)\), so every fitted run equals \(y_a\)
at \(-x_a\). The admissible two-sample cosine example and its positive
Gram check are recorded in `QUERY_RATIO_SCOPE.md` and
`UNIFORM_TIME_SCOPE.md`. This finite-panel obstruction does **not** refute a
supremum over an entire separated sphere region.

The main proof search therefore addresses the stronger projective
separation condition above, not merely this parity objection. Even under
that condition, the requested endpoint scale remains open.

## Two concrete advances

### 1. An exact fully trained endpoint decomposition

`ENDPOINT_TRANSVERSE_ROUTE.md` subtracts the initialized training-feature
projection of the test feature. It expresses the difference between the
actual fitted prediction and the initialized frozen-feature interpolant as
two exact terms: motion of that test residual and readout motion transverse
to the initialized training-feature span. The latter is bounded by a
width-independent multiple of \(Y^3\) under the original cap. The note also
derives the exact cubic coefficient in a local label-amplitude expansion.

The remaining gap is not an algebraic omission: an absolute cubic error
does not control fluctuations of order \(Y/\sqrt n\) at fixed nonzero
\(Y\). A relative estimate must retain the test innovation and its hidden
derivatives. A common-strip, common-envelope nonaffine activation family in
the same note shows that generic small feature motion does not yield such a
relative estimate. This is an obstruction to that estimate, not a
counterexample to the actual gradient-flow theorem.

### 2. Complete cancellation of the probe's sphere dependence is impossible

`ENDPOINT_PROBE_NONCANCELLATION.md` removes one top hidden neuron and runs
the remaining network to its fitted limit. An independently initialized
probe neuron is trained using that network's evolving features and
residuals. Its infinitesimal contribution includes the exact compensating
response of all retained parameters; the other neurons are not frozen.

On cavity events of probability tending to one, the centered compensated
probe influences have infinite-rank covariance on every nonempty open sphere
patch. In particular, at each such finite-width cavity the influence has
positive variance at almost every query, with no off-training-span
condition and no smaller label cap.

The reason is structural. The trained probe still parametrizes an open
family of ridge functions. Its direct query dependence spans an
infinite-dimensional family. The compensation contributed by the fixed
cavity has only finitely many parameter-derivative functions, so it cannot
cancel that entire family. The proof includes preservation of a sufficiently
rich lower-feature map through the full training trajectory.

This conclusion concerns the **infinitesimal compensated probe**, not the
prediction of the actual full network. Its exceptional query set is not
identified with the training inputs and their antipodes.

## What is still missing

Two implications are not proved:

1. The surviving endpoint fluctuation must have a nonvanishing scale as
   width increases. Infinite covariance rank at each width does not give a
   width-independent lower bound on any covariance eigenvalue. The cavity's
   tangent dimension itself grows with width.
2. An infinitesimal neuron-insertion response must be transferred to the
   collective fluctuations of the actual width-\(n\) network, with a
   sufficiently small remainder and a probability-of-small-values estimate.
   One independent probe at output scale \(1/n\) does not supply a dense
   discrepancy of order \(1/\sqrt n\).

These are substantial remaining proof obligations. Positivity alone cannot
replace them: multiplying an infinite-rank random function by \(e^{-n}\)
preserves its rank and positive-variance statements while destroying the
required scale. That observation is a logical distinction, not a canonical
network counterexample.

The complementary endpoint derivative route in
`ENDPOINT_SEPARATION_STRUCTURE.md` instead gives a sufficient Gaussian
small-ball criterion for the actual endpoint map. Its normalized derivative
and derivative-regularity bounds also remain unverified. It does not supply
the missing collective result by another name.

## Disposition

The new notes keep the activation scope and original label condition intact.
They establish genuine finite-width endpoint structure, but not the requested
quantitative extension. The previously checked actual-network lower theorem
therefore still requires the query domain to contain a fixed point outside
the training span. No necessity of that span restriction is proved for a
projectively separated query or an open sphere patch.

Fresh isolated checks are recorded separately in
`ENDPOINT_TRANSVERSE_CHECK.md` and
`ENDPOINT_PROBE_NONCANCELLATION_CHECK.md`. Their scope is these new partial
arguments, not certification of the unresolved endpoint lower theorem.
No paper/book edit, experiment, commit, or promotion is part of this work.
