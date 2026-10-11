# Circle endpoint variability: quantitative progress and remaining gap

2026-10-11. Continuation of the full-span endpoint investigation, narrowed
to a spatial supremum on the circle. These are internally checked research
results, not a replacement for the paper's endpoint theorem. No paper or
book was changed, and no experiment or Git write was performed.

## Target and status

Use the canonical network and gradient flow of `paper/compact.tex`: width
\(n\), fixed depth \(L\ge2\), Gaussian hidden initialization, zero
initial readout, output \(w^\top h^{(L)}/n\), and the original block
mobilities. The \(m\ge2\) fixed training inputs lie on the radius
\(\sqrt2\) circle and are pairwise nonparallel. They may span the entire
input plane. Retain the population training-feature gap \(\gamma>0\),
fixed nonzero labels of scale \(Y=\|y\|/\sqrt m\), and the exact cap
\(Y\le(\gamma/m)\beta^{-30L}\). Every layer activation is nonaffine
and belongs to the paper's strip-analytic, bounded-strip-derivative class;
activation values need not be bounded.

For two independently initialized, fully trained networks, the requested
claim is: for every fixed confidence \(1-\delta\), there is
\(c_\delta>0\), independent of width, such that eventually

\[
\Pr\!\left\{
\sup_{\|x\|=\sqrt2}
 |f_n(\infty,x)-\widetilde f_n(\infty,x)|
 \ge c_\delta n^{-1/2}\right\}\ge1-\delta.
\]

The search also considers the stronger version with the spatial supremum
restricted to any fixed nonempty open arc separated from the training
directions and their antipodes. Neither version is proved by this packet.
No counterexample to either canonical-network claim was found. In
particular, no result here shows that an off-training-span assumption is
mathematically necessary.

## New proved steps

### 1. Dimension-free control of a trained probe

Delete one top neuron while retaining the original width normalizations,
and drive an independent Gaussian-root probe by that cavity's exact
training residual and hidden-feature paths. The Gaussian projections of
these paths have moments and exponential moments bounded independently of
width. The endpoint incoming-weight map differs from the identity by a
matrix with width-independent trace-norm moments. These are estimates on
the nonlinear trained probe, not on frozen initialized features.

Full derivation: [CIRCLE_TRANSPORT_ROUTE.md](CIRCLE_TRANSPORT_ROUTE.md).
These upper bounds do not guarantee invertibility on every root or a
lower bound on the compensated endpoint variance.

### 2. A trained probe retains a uniformly nonzero readout signal

Let \(a_\infty(g)\) be the physical readout of that trained probe with
standard Gaussian incoming root \(g\). On a cavity event whose probability
tends to one,

\[
\left(\mathbb E_g|a_\infty(g)|^2\right)^{1/2}
\ge \frac{Y}{6H},
\]

where \(H\) is the fixed activation-and-depth constant already defined
in the fitting proof. No smaller label cap or new query qualification is
used. The bound is uniform in width.

The new estimate compares the entire trained readout path to the
minimum-norm interpolant in the initialized training features. Its
Lyapunov inequality makes the frozen-feature comparison errors small
relative to that particular interpolant, without losing extra gap powers.
Final fitting then supplies the lower bound, and the empirical/population
Gram comparison transfers it to the independent probe.

Proof: [CIRCLE_PROBE_READOUT.md](CIRCLE_PROBE_READOUT.md).
Fresh reconstruction:
[CIRCLE_PROBE_READOUT_CHECK.md](CIRCLE_PROBE_READOUT_CHECK.md).
This is an uncentered second-moment lower bound. It is not a centered
variance bound, a lower bound after the other neurons compensate, or a
two-network fluctuation theorem.

### 3. Actual finite-width endpoints are generically nonconstant

Fix a nonzero label direction and a nonempty circle arc. At each
sufficiently large individual width, outside a finite set of possible
label amplitudes within the original cap, the actual fitted prediction
at a suitable query in the arc is a nonconstant analytic function of
hidden initialization on an open fitting event. Its conditional law on
that event is non-atomic. Outside a countable union of exceptional
amplitudes, this holds at every sufficiently large individual width.

This uses the actual nonlinear endpoint map and its exact zero-label
derivative; it does not replace positive-label training by frozen-feature
training. Neither the probability of the witnessing event nor the size
of the variation is controlled uniformly in width. The exceptional label
amplitudes have not been eliminated.

Proof: [CIRCLE_ADVERSARIAL_ROUTE.md](CIRCLE_ADVERSARIAL_ROUTE.md).

## Why the endpoint theorem is not yet closed

A trained probe's direct prediction is only part of its endpoint effect.
The other neurons respond throughout training, and that response cancels
the direct effect exactly at training inputs. The previously proved
infinite-rank covariance of the compensated probe on an open arc prevents
complete cancellation at each width, but does not bound a surviving
covariance scale independently of width. That theorem uses both the
fitting event and its additional two-query initialization event (13);
their intersection has probability tending to one.

The missing steps are quantitative survival of a spatial fluctuation
after this compensation, and its transfer to an anti-concentration bound
for two actual networks. Qualitative rank, finite-width nonconstancy,
and the probe's uncentered second moment do not supply these steps.

The independent angular-score route proves a sufficient local-limit
criterion: a nonzero, regular endpoint response to a root-\(n\) angular
tilt forces an independent Gaussian component and the desired
every-confidence lower bound. The required local-limit hypothesis is
not established for the trained networks; it is not treated as a theorem
input already available. See
[CIRCLE_FOURIER_ROUTE.md](CIRCLE_FOURIER_ROUTE.md).

A further high-angular-mode attempt found that nonzero analytic readout
and near-identity hidden transport alone do not force the needed
hidden-tangent lower bound: a static cosine-feature example suppresses
the high-mode mass with a decaying readout. It is not known to be
reachable by the canonical training flow and is not a counterexample
to the requested theorem. See
[CIRCLE_TANGENT_ROUTE.md](CIRCLE_TANGENT_ROUTE.md).

## Checks and disposition

[CIRCLE_ROUTE_CHECK.md](CIRCLE_ROUTE_CHECK.md) independently reconstructs
the first three routes, including the conditional Fourier theorem and
the generic-label actual-flow result. Its requested event qualification
and terminology clarifications have been applied. The separate direct
readout proof was independently reconstructed as linked above. The
coordinator also checked the second-round tangent example's integration
by parts, Gaussian normalization and Fourier coefficients. These checks
validate the stated partial results, not the unproved circle endpoint
claim. The off-span restriction has therefore not been removed from any
claimed endpoint lower theorem.
