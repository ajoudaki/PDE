# Unseen-input decoding within a dense forward-pass budget

The stronger current resource interface is
[QUADRATIC_RESOURCE_RESULT.md](QUADRATIC_RESOURCE_RESULT.md): explicit
memory exponent 722, dense-budget initialization and updates, and no
calibration. It has the same \(3b_n(\delta/256)\) error and replaces
the expensive preprocessing/calibration limitation of this earlier
variant. The construction below remains a separate valid historical route.

2026-10-06. Constructive result under the same inherited dense/source
certificates as `RESULT.md`. The proof is the
[complete assembly](DENSE_BUDGET_DECODER_CANDIDATE.md), with separate
[probabilistic](DENSE_BUDGET_BRIDGE_CHECK.md) and
[numerical](DENSE_BUDGET_NUMERICAL_CHECK.md) internal checks. This is a
research-study result, not promotion into the maintained book or a practical
implementation benchmark.

## Shared setup

Let \(n\) be the dense hidden width, \(L\ge2\) its fixed depth,
and \(1-\delta\) the required confidence. Retain the original Gaussian
initialization, zero readout, mean squared loss, block mobilities
\((n,1,\ldots,1,n)\), nonlinear hidden-feature learning, and fixed
training data with \(m\ge d\) spanning \(\mathbb R^d\) on the
radius-\(\sqrt d\) sphere. Keep the original positive initial feature-Gram
gap and full small-label condition. Strip-analytic activations with bounded
first derivative are allowed even when their values are unbounded.

Write \(b_n(\delta)\) for the existing dense-versus-independent-dense
upper error certificate, displayed in `RESULT.md`. Every \(C\) below
may depend on the fixed dataset, dimension, sample count, depth, gap,
labels, activation and confidence, but not on \(n\). The integer \(k\)
is absolute: it does not depend on those problem parameters. Its numerical
value has not been extracted; it is not a tunable model order or an
exponent-five claim.

## The result

There is a compact current-state response model with

\[
 \text{retained storage}+\text{peak query workspace}
 \le C[\log(en)]^k,
 \qquad
 \text{work per query}\le Cn^{3/2}[\log(en)]^k.
\]

At every sufficiently large individual width, with probability at least
\(1-\delta\),

\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |f_{\rm compact}(t,x)-f_n(t,x)|
 \le 3b_n(\delta/256).
\]

One event covers the entire sphere, every physical training time, and
the fitted endpoint, including adaptively selected late queries. Neither
test inputs nor test labels are needed during initialization or training.
The model is autonomous and restartable in the same finitely scheduled,
clocked-algorithm sense as the existing compact response construction.
Decoding uses its present compressed state: no dense weights, saved
width-\(n\) activations, future-output table, or replay of scalar training
updates is available or required.

For fixed problem parameters, \(n^{3/2}\log^k(en)=o(n^2)\).
Thus the query work is eventually bounded by the ordinary dense forward
cost \(O(Ln^2+dn)\), while the query workspace remains logarithmic.
This is a bound for every query on the finite implemented algorithm, not
an expected stopping-time bound for a rejection sampler.

The sufficient width can depend on every fixed problem parameter and is
unquantified. It includes both the inherited source thresholds and the
additional thresholds needed for the displayed work and error comparisons.
There is no assertion of one success event across infinitely many widths.

## What changed in the proof

The retained training moments define a calibrated probability law for one
row of the response circuit. Expensive, finite preprocessing computes its
coefficients and normalizer with counted compact memory. During querying,
a short stored random seed regenerates rows one at a time. Robust averages
evaluate the new point's layer moments; no row panel is retained.

Three estimates make this a neural-decoder proof rather than just a fast
integrator. Retained raw Grams control nearly dependent history directions
without a new spectral-gap assumption. The opposite-orientation Gaussian
covariance correction has only polylogarithmic rank, so omitting it costs
root-width error. Integrating each fresh Gaussian before comparing nonlinear
moments propagates variance errors linearly, avoiding a square-root loss.
The full finite-width posterior comparison is proved; equality with a
population law is not assumed.

## Qualifications that remain

The error is at the dense-variability **upper-certificate scale**, not
near-\(1/n\) matched-reference accuracy or a bound relative to the
realized discrepancy of a particular dense pair. The sharper bookkeeping
form is

\[
 2b_n(\delta/256)+C[\log(en)]^{C_L}/\sqrt n.
\]

Here the finite error exponent \(C_L\) may depend on fixed depth; the
storage exponent \(k\) does not. For every fixed nonzero label size,
the certificate's positive \(\exp(CY^2\sqrt{\log(en)})\) factor,
where \(Y=\|y\|_2/\sqrt m\),
eventually dominates this logarithmic remainder. Zero labels use the
exact zero predictor. This proves the simpler factor-three statement
without imposing a new label condition, but does **not** preserve the
old literal \(2b_n+1/n\) remainder.

Preprocessing may still inspect the completed finite dense source computation.
Calibrating a current summary can be extremely expensive. No training-time
speedup, strictly online compression, polynomial-in-compact-size query
bound, small fixed-parameter prefactor, or practical width threshold is
proved. The representation is a response circuit, not an ordinary tiny
network evaluated by a conventional forward pass.

Work is counted in the same arithmetic and activation-primitive model as
the dense forward comparison. The inherited precision-access assumptions
give the finite-bit memory statement. Polynomial bit-time additionally
requires polynomial-time precision access to activations and numerical
inputs; it does not follow from analyticity or polynomial-space access
alone. The construction uses supplied finite certificates, as before,
not a uniform compiler for arbitrary raw activation code.
