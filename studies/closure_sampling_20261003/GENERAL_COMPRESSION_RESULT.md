# Polylogarithmic neuron compression at fixed depth and sample count

2026-10-03. Research synthesis. The complete mathematical statement and
construction are in [GENERAL_ANALYTIC_COMPRESSION.md](GENERAL_ANALYTIC_COMPRESSION.md).
Check status is recorded there and in the linked complete reconstructions.

## The answer and its exact scope

The three axes can be combined for **bounded analytic activations**:
fixed finite sample count, arbitrary fixed hidden depth, and layer-dependent
activations from a concrete class wider than tanh. The combined argument
also permits nonorthogonal data under the existing initial feature-Gram
gap. It does not establish the same theorem for every merely $C^3$
activation in the earlier closure result.

The reference is the actual canonical dense network with $L\ge2$
hidden layers, each of width $n$. Its first weights are iid $N(0,1)$,
hidden entries are iid $N(0,1/n)$ independently, and its initial readout
is zero. It trains by the manuscript's physical gradient flow with squared
mean loss and mobilities $(n,1,\ldots,1,n)$ on fixed inputs
$x_1,\ldots,x_m\in\sqrt d S^{d-1}$. Labels are arbitrary fixed
real numbers satisfying the sufficiently small RMS condition
$(m^{-1}\sum_a y_a^2)^{1/2}\le Y_*$. All signs and label ratios are
allowed. The input dimension $d$, depth $L$, and sample count $m$ stay
fixed as $n$ grows.

Each activation must be real on the real axis, holomorphic and bounded on
a fixed horizontal complex strip. Tanh, sigmoid, erf, arctan, and sine
are examples. Different layers may use different such functions. There
is no clipping, monotonicity condition, or positive lower slope bound.

As before, require a positive limiting initialized readout-feature Gram.
For nonconstant activations in this class this condition holds, in
particular, for distinct sphere inputs with no antipodal pairs. There is
no restriction $m\le d$: a fixed circle can contain arbitrarily many
such training points.

For every fixed confidence $1-\eta$, and all sufficiently large widths,
initialization-only coordinated neuron selection constructs a smaller
weighted network with

\[
 \boxed{\text{total retained real coordinates}
       \ \le C[\log(en)]^{P}=o(n),\qquad
       P=4[d(L+5)+1],}
\]

and, with probability at least $1-\eta$,

\[
 \boxed{\sup_{t\in[0,\infty]}
        \sup_{x\in\sqrt d S^{d-1}}
        |f_C(t,x)-f_n(t,x)|\le\frac C{\sqrt n}.}
\]

The constant does not grow with width or physical time. The sufficiently
large width threshold may depend on the fixed confidence and labels.
The probability statement is for each width, not one simultaneous event
covering every width. The endpoint is included: both networks converge
and interpolate the training labels.

The logarithmic exponent is conservative. The previously proved
two-layer orthogonal tanh construction has the sharper exponent $6d+4$,
including $16$ on the circle. No practical claim follows from these
asymptotic counts at accessible widths.

## What the smaller system retains

Each hidden layer retains a positively weighted subset of original neuron
indices. Selection depends on the initialization, training inputs and labels;
it is coordinated across the responses the network will need. It preserves
finite sets of scalar products and both directions of each initialized
mixing operation. The smaller initial matrices are projections of the
original random mixers, not fresh independent Gaussian draws.

After setup, retain only the smaller first-weight array, smaller hidden
matrices, readout, positive masses and fixed training data. Every hidden
matrix continues to train. The model computes its own forward pass,
backward responses and residuals, and uses those residuals in its own
autonomous gradient equations. The state count includes every entry of
those learned matrices and all fixed data retained by the construction.
There are no original-width matrices or source-basis arrays at runtime.

This uses the user's permitted direct dense route. It is not a claim that
the original order-$q$ closure remains unchanged under neuron selection.
The error is against the particular original finite-width run; no
dense-to-population rate or ignored population bias is involved.

## Why the depth extension works

Two observations close different parts of the proof.

First, **the coordinate response bound can be proved upward through the
layers**. Removing one neuron exposes independent incoming and outgoing
Gaussian initialization vectors. Its effect on learning includes both
directions and the change in the model's residual. In the resulting trace
formula, the forward-response maximum needed to control layer $\ell+1$
comes only from layers up to $\ell$. Backward carriers are controlled
by the existing finite-network small-label estimate. The enlarged
calculation also tracks query derivatives and mixed responses; marginal
Gaussian initialization alone would not suffice. This produces a verified
inverse-power-of-logarithm complex neighborhood for the actual moving
responses at every fixed depth.

Second, **intermediate stability need not have a width-independent
constant**. The comparison between the original and selected models costs
at most $\exp(C\sqrt{\log n})$ times the response approximation error.
Approximate those responses to
$n^{-1/2}\exp(-D\sqrt{\log n})/\log n$, with fixed sufficiently large
$D$. Analytic approximation still needs only polynomially many logarithmic
coefficients, because the logarithm of the reciprocal tolerance is still
$O(\log n)$. The final error is therefore strictly $C/\sqrt n$, not
$n^{-1/2+o(1)}$.

Positive cubature preserves products in those small source spaces, giving
a finite selected model. Comparing the two actual residual equations
controls feedback over the finite total learning activity. The two models'
own exponential fitting tails handle the remaining infinite time interval.
The proof includes selection bias and repeated feedback, rather than only
matching a fixed collection of initial predictions.

## Feature learning and the remaining limitations

This is a trained nonlinear network throughout. An additional exact
certificate shows that, for linearly independent inputs, nonconstant
activations and nonzero labels, every hidden feature layer has nonzero
initial curvature, almost surely on the fitting event. The selection can
preserve this certificate. The new arbitrary-depth certificate does not
give a width-independent lower bound on the amount of motion; the earlier
two-layer result has that stronger bound in its original scope.

The main resource qualification remains substantial: setup uses exact
real arithmetic and may require an enormous finite number of initial
time derivatives, temporary coordinates and bits of precision. Those are
discarded before training the selected model. No trained snapshots enter
the construction, but **this is an existence theorem for small autonomous
representations, not an efficient numerical compression algorithm**.

The proof does not cover growing sample count, dimension or depth, large
labels, arbitrary smooth nonanalytic activations, or finite-precision
preprocessing. It does not establish improved test classification against
unknown ground-truth labels. No numerical experiment or manuscript edit
was made.

Complete proofs and checks:

- [General construction and theorem](GENERAL_ANALYTIC_COMPRESSION.md).
- [Actual deep finite-network complex sources](DEEP_COMPLEX_SOURCE.md),
  [activation and mixed-response extension](DEEP_ACTIVATION_EXTENSION.md),
  and [their complete reconstruction](DEEP_COMPLEX_SOURCE_CHECK.md).
- [Weighted own-feedback comparison](GENERAL_WEIGHTED_COMPARISON.md)
  and [complete reconstruction](GENERAL_WEIGHTED_COMPARISON_CHECK.md).
- [Assembly reconstruction](GENERAL_ANALYTIC_COMPRESSION_CHECK.md) and
  [coordinator source, normalization and scope audit](GENERAL_COMPRESSION_COORDINATOR_CHECK.md).

All check designations are internal research checks. They are not independent
promotion reviews or claims that the maintained manuscript/book has changed.
