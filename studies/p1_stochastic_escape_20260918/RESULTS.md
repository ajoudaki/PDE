# What minibatches and added noise prove for p=1

2026-09-19. Lead synthesis of this new stochastic-optimizer study.
All arguments were derived within this study from the established p=1
definitions. No unpromoted result from another study was used. Complete
proofs and check provenance are linked below and recorded in the README.

## The strongest positive conclusion

For every finite set of normalized sphere inputs in dimension d>=2,
with positive probability weights and arbitrary +1/-1 labels satisfying
the odd architecture's compatibility rules, the exact p=1 population
model admits an explicitly constructed finite-norm exact fit. The only
compatibility requirements are equal labels at identical inputs and
opposite labels at antipodal inputs. Arbitrary linear dependencies and
sample counts greater than dimension are allowed.

There are explicit open regions of starting population states from
which **actual iid minibatch SGD, including batch size three, converges
to a finite zero-loss state with probability at least 1-delta**, for
any prescribed delta in (0,1). The region and positive step bound are
computed from the data and canonical Gaussian expectations. On a
specified successful event A with P(A)>=1-delta,

\[
 E[L_k\mid A]\le\frac{L_0}{1-\delta}(1-2\eta\lambda)^k,
 \qquad \lambda>0.
\]

This is an unconditional local starting-region theorem, not an assumption
that future hidden Grams remain positive. It proves that control within
the region persists with the stated probability, and that the whole
state converges there. It does **not** establish entry into these regions
from the prescribed canonical initial state (g,0,D).

The proof in [local_minibatch_fitting.md](local_minibatch_fitting.md)
first selects a direction whose projections of the distinct input
representatives have distinct nonzero magnitudes. A bounded lower field
and one legal middle-matrix row produce upper tanh functions with
distinct slopes. Their Gram is invertible by a Vandermonde argument,
giving an explicit fitting readout. Around this state, a proved Gram
bound controls the residual gradient and the minibatch gradient's second
moment is bounded by a constant times loss. A stopped-process and
total-travel estimate prove both the high-probability invariant region
and the displayed convergence. All three blocks continue to train.

## Exact stochastic dynamics and noise directions

On the fixed canonical Gaussian carriers, let theta=(w-g,c,M). For
physical inputs x_i of norm sqrt(d), set

\[
 a_i=E_1[b_1\phi(w\cdot x_i/\sqrt d)],\quad
 H_i=\phi(b_2^TMa_i),\quad f_i=E_2[cH_i],
 \qquad \ell_i=(f_i-y_i)^2,
\]

with phi=tanh and the full physical population-L2/Frobenius gradient.
An iid minibatch consists of B independent indices sampled with the
data probabilities p_i. The exact update and conditional covariance are

\[
 \theta_{k+1}=\theta_k-\frac\eta B\sum_{j=1}^B
                            \nabla\ell_{I_{k,j}}(\theta_k),
\]
\[
 \mathcal C_B(\theta)=\frac1B\sum_i p_i
 (\nabla\ell_i-\nabla L)\otimes
 (\nabla\ell_i-\nabla L).
\]

Thus batch three divides the covariance by three, without adding
directions to its range. The population fields share the same random
data batch; the frozen neuron marks are not resampled. On the physical
clock t=k eta the increment covariance per unit time is eta C_1/B.
A fixed-temperature Brownian perturbation is a different optimizer,
not the eta->0 limit asserted without further scaling.

For a constant nonzero step, if even one individual sample gradient is
nonzero at a state, iid batches almost surely exit a sufficiently small
neighborhood of it. One repeated-index batch has positive probability
of forcing exit; independent trials give a geometric exit-time bound.
The allowed neighborhood size depends on the step. More generally any
finite state limit of constant-step iid SGD must have

\[
                        \nabla\ell_i=0\quad\text{for every }i.
\]

For p=1 these common stationary states can be described exactly. At an
incorrectly predicted nonzero-label observation they require

\[
 f_i=0,\qquad Ma_i=0,\qquad
 E_2[b_2c]a_i^T=0,\qquad M^TE_2[b_2c]=0.
\]

All other observations are fitted. These are much more restrictive
than cancellation of the weighted full gradient, but they are not empty.
For decreasing steps the point-limit implication weakens: with
sum eta_k=infinity and sum eta_k^2<infinity, the proved necessary
condition is mean stationarity, not individual sample stationarity.
Complete derivations are in [sgd_geometry.md](sgd_geometry.md).

## Why cubic descent alone does not settle SGD

A nonzero cubic loss term along one direction gives lower-loss states
arbitrarily near the stationary point. It does not by itself prove that
the full state flow attracts from one side or that the sampling noise
has a component across that direction.

There is an exact counterexample to that latter inference in this model.
Take three normalized circle inputs

\[
 x_1=\sqrt2 e_1,\quad x_2=e_1+e_2,\quad x_3=e_1-e_2,
 \qquad (y_1,y_2,y_3)=(1,1,-1),\quad p_i=1/3.
\]

These distinct nonparallel inputs are exactly fittable in p=1. At the
ambient state w=0,c=0,M=0 the loss is one and every sample gradient
vanishes. Yet a bounded admissible three-block variation has

\[
                        L(\theta_\epsilon)=1-C\epsilon^3
                                     +O(\epsilon^5),\quad C>0.
\]

Every minibatch and every step schedule started exactly at that state
leaves it fixed. The noise covariance is zero. This is an ambient
cubic-state obstruction, **not** a failure trajectory from canonical
initialization. Section 9 of the minibatch report proves the mixed-label
fit and cubic coefficient explicitly.

The opposite behavior also occurs. In the balanced four-input family
\(\sqrt3(C,\pm S,0)\) labelled +1 and
\(\sqrt3(C,0,\pm S)\) labelled -1, with C,S>0 and C^2+S^2=1,
there is an explicitly constructed cubic bad equilibrium at loss one
whose batch-three updates always move. Under a stated positive step
bound both w and M change at the second update. Its first update raises
total loss and its initial covariance points solely along the positive
Hessian direction; the subsequent coupling is what creates hidden motion.
These data also admit an exact fit. The complete independent construction
is [four_input_noise_geometry.md](four_input_noise_geometry.md).

## Added noise: escape is easier than convergence

An independently chosen Gaussian perturbation in a finite-dimensional
flat subspace with a nonzero leading cubic term lowers loss with
probability tending to one half as its amplitude tends to zero. The
subspace qualification matters. Nonzero trace-class additive Brownian
noise in the physical Hilbert state also forces almost-sure exit from
every fixed bounded ball. That exit statement applies around minima
too, so it supplies no loss-convergence theorem.

Persistent readout noise repeatedly creates positive loss near any finite
fitting state where its covariance acts on a nonzero training feature.
Minibatch noise has an advantage: it vanishes at an exact fit. Artificial
noise requires a suitable decay or stopping rule for convergence, and
then its remaining ability to escape degenerate bad sets must be proved.
Independent noise inside each population expectation has yet another
meaning; it can average away without creating the feature correlations
needed to learn. Exact examples and all stochastic assumptions are in
[noise_escape.md](noise_escape.md).

## What remains open

The positive local stochastic fitting theorem covers general finite input
geometry. The constant-step classification eliminates ordinary
full-gradient cancellation points as possible finite SGD limits.
Neither supplies the missing global theorem from canonical initialization.
That requires ruling out approach to the remaining collapsed common
stationary sets and positive-loss behavior without a finite state limit,
and proving entry into a region where fitting succeeds. No such canonical
failure has been constructed here, and no canonical global fitting theorem
is claimed.

The earlier idea of using a three-input deterministic theorem on successive
triples has no automatic implication: the objective and current state change
with each batch. The exact covariance and update analysis above is the
required stochastic replacement. All results remain within the new study;
no promotion or numerical experiment was performed.
