# Direct compact construction for orthogonal two-layer tanh training

2026-10-06. This corollary combines the same-study certified direct search
with the new logarithmic dense-copy estimate. It is not the requested
strict constant-times-root-width theorem. The inherited paired compact
and source/fitting probability statements retain their research-note
status and eventual, unquantified width threshold.

## Setup and result

Fix `m` orthogonal training inputs of norm `sqrt(d)`, with arbitrary fixed
signed nonzero labels in the **existing full common small-label allowance**.
The reference width is `n`. Both hidden activations are tanh. The canonical
reference has independent `A_ij~N(0,1)`, `W_ij~N(0,1/n)`, zero readout,
output `w^T tanh(W tanh(Ax/sqrt(d)))/n`, squared mean loss, and
mobilities `(n,1,n)`.

The compact width budget is `q`, and `delta` is the desired failure
probability. The norm below is the supremum over the entire sphere and
all physical training times, including the fitted endpoint. For each
fixed dataset and `0<delta<1`, at every sufficiently large individual
width `n`, there is a terminating direct initialization algorithm with

\[
q=O\!\left(\log(en)^{3d/2+1}\right),
\qquad
\Pr\!\left[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |f_C(t,x)-f_n(t,x)|
 \le C_{\mathrm{data},\delta}\frac{\log(en)}{\sqrt n}
\right]\ge1-\delta.
\tag{1}
\]

The constant is independent of `n` and time. Moving state has at most
`q^2+q(d+1)+m` real coordinates. Fixed metrics use at most `q(q+1)`
real coordinates; data and optional feature/solve caches are counted
separately in the direct-search theorem. Total retained storage is

\[
O\!\left(\log(en)^{3d+2}\right)
\]

at fixed data. This is the original compact storage exponent. The model
uses the original corrected-readout nonlinear optimizer, with both hidden
matrices trained. Its initialization uses the data and Gaussian law only.
It never instantiates, queries, or trains a realized width-`n` reference.
The reference appearing in (1) is fresh and independent.

The algorithm is a mathematical, certified exhaustive search, not a
practical initialization procedure with a useful complexity bound.
Setup time, temporary storage, and required coefficient precision may
be enormous. The storage statement counts real coordinates, not bits.
The existing unquantified stochastic width threshold is not made
effective by this corollary. Zero labels are handled exactly by the zero
predictor without using any positive-label formula.

## Proof and actual construction

Set each inherited failure budget to `delta/100`. The old paired compact
theorem, with source tolerance `1/n`, supplies a model with the displayed
width order, bounded fitting trajectory, uniformly positive feature Gram,
and paired error `n^(-1+o(1))`. Its exact integer source count and full
label allowance are those identified in Section 6 of
[DIRECT_CERTIFIED_CONSTRUCTION.md](DIRECT_CERTIFIED_CONSTRUCTION.md).
Use certified integer upper rounding of that count, so the budget is
effectively specified without equality decisions at real cutoffs.
For sufficiently large `n` this budget is less than `n`.

[ROOT_WIDTH_CONCENTRATION_ROUTE.md](ROOT_WIDTH_CONCENTRATION_ROUTE.md),
equation (17), proves that two independent canonical dense trajectories
are within `C_data,delta log(en)/sqrt(n)` with the assigned probability.
Its hypotheses are exactly the physical fitting event and the existing
all-time counting fourth-moment and maximum carrier controls, specialized
to orthogonal two-layer tanh data. It introduces no extra label restriction.
Its coordinate transform is used only in the proof; it does not change
either model's physical clock.

Now run the algorithm of DIRECT_CERTIFIED_CONSTRUCTION with tolerance
sixteen times the sum of the two error certificates, using an upper
computable enclosure if necessary. That theorem proves termination and
the full independent-reference guarantee. Its proof includes Gaussian
truncation and finite-width bias, nonlinear feedback, whole-sphere
discretization, all-time fitting tails, endpoint control, rational
initialization perturbations, and probability allocation. Because the
paired compact error is `o(n^(-1/2))`, the resulting tolerance has the
order in (1). The width, optimizer, and retained count are unchanged.

More concretely, initialization enumerates rational compact weights and
positive metrics, certifies small-model finite-time dynamics and fitting
tails, and computes a smooth failure-score expectation under the exact
finite-width Gaussian law. That expectation is computed by polynomial
ODE approximation and symbolic index-equality contractions, not by
evaluating any realized dense trajectory. A strict probability certificate
selects the accepted rational initialization. All search data and
contraction programs are then discarded. Runtime starts the accepted
small model with zero raw readout and initial label deficit equal to the
given labels, and follows the explicit autonomous equations of the direct
theorem.

The constants in the logarithmic dense bound can be selected effectively
from its deterministic hypotheses: the input gap, operator caps, carrier
fourth-moment coefficient and residual decay rate have finite source
recurrences, and every comparison step uses finite sums, products,
Cauchy--Schwarz bounds and an explicit Gronwall exponential. Safe rational
upper bounds propagate through those operations. This observation is
about a deterministic error coefficient, not the unquantified width at
which its source probability event holds. No polynomial dependence on
sample count or inverse gap is asserted for the new coefficient.

## Exactly what remains unresolved

The logarithm in (1) has not been removed. The new tanh coordinates remove
the width-growing dynamical stability exponent, but the current proof
still uses a maximum over initial-source gate ratios and a finite query/time
net. The route note gives a precise sufficient joint Gaussian-gradient
moment and localization estimate for the strict `C_data,delta/sqrt(n)`
target; that estimate is not proved. Separate carrier moments and a global
response norm do not imply it.

This result also does not supply efficient setup, a bit-storage bound,
dataset-blind initialization, or a dimension-independent logarithmic
storage exponent. For nonorthogonal sphere data the direct search still
applies, but only the inherited general `n^(-1/2+o(1))` dense-copy rate
has been supplied. None of these limitations is an impossibility result.
