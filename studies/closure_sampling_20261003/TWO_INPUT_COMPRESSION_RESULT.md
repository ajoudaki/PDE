# Positive autonomous compression for two canonical training inputs

2026-10-03. Research result in the existing neuron-sampling study. The
full compression proof and its two mathematical dependencies have complete
internal reconstructions. This is not an established-book or manuscript
claim, and no promotion is attempted.

## What is resolved

For **two orthogonal circle inputs and arbitrary sufficiently small fixed
labels**, the actual initialized width-$n$ dense network admits an autonomous
weighted network with at most $C\log^{16}(en/\eta)$ retained real coordinates
and prediction error $C/\sqrt n$ at confidence $1-\eta$, uniformly over the
whole circle and all physical training time, including the fitted endpoint.
Both hidden layers of the original network have width $n$ and train.

The smaller network uses coordinated, initialization-dependent selection
of neurons and positive weights. It is a direct dense-model construction,
as allowed by the later user request. It is not a theorem about reducing
neurons inside the unchanged order-$q$ response-memory equations.

## Exact setup and theorem

Let $e_1,e_2$ be the coordinate vectors of $\mathbb R^2$. Train on

\[
 x_1=\sqrt2e_1,\qquad x_2=\sqrt2e_2,
 \qquad y=(y_1,y_2)\in\mathbb R^2.
\]

For any input $x$, the reference network is

\[
 h(t,x)=\tanh(A(t)x/\sqrt2),\qquad
 g(t,x)=\tanh(W(t)h(t,x)),\qquad
 f_n(t,x)=w(t)^\top g(t,x)/n.
\]

Here $A\in\mathbb R^{n\times2}$, $W\in\mathbb R^{n\times n}$,
and $w\in\mathbb R^n$. Initially the entries of $A$ are independent
$N(0,1)$, those of $W$ are independent $N(0,1/n)$, the two arrays are
independent, and $w=0$. Use the manuscript's gradient mobilities $(n,1,n)$
and loss $\frac12\sum_{a=1}^2(f_n(x_a)-y_a)^2$. All comparisons below
use the same physical time.

There are fixed constants $Y_*,C>0$ with the following property. For every
fixed $y$ with $\|y\|_2\le Y_*$, chosen independently of initialization,
every fixed $0<\eta<1/2$, and all sufficiently large $n$, the construction
produces a predictor $f_C$ such that, with probability at least $1-\eta$,

\[
 \sup_{t\in[0,\infty]}\sup_{\theta\in\mathbb R}
 \left|f_C\bigl(t,\sqrt2(\cos\theta,\sin\theta)\bigr)
       -f_n\bigl(t,\sqrt2(\cos\theta,\sin\theta)\bigr)\right|
 \le \frac{C}{\sqrt n}.
\]

The notation $t=\infty$ includes the fitted limit, whose existence is
proved for each model. Both interpolate the two training labels. The
constant in the error bound is independent of width and time. The width
threshold may depend on the fixed label vector and confidence.

The number of retained moving and fixed real coordinates after setup is

\[
 P_n\le C[\log(en/\eta)]^{16}=o(n)
 \qquad\text{for fixed }\eta.
\]

In particular, the theorem includes $y=(\varepsilon,2\varepsilon)$ and
$y=(\varepsilon,-2\varepsilon)$ whenever $\sqrt5\varepsilon\le Y_*$.
It also includes unequal magnitudes of any ratio, negative common sign,
and zero components. The all-zero label vector is stationary and trivial.
The construction is allowed to depend on the specified labels; it is not
one compressed initialization for all subsequent training tasks.

## What the smaller system stores and evolves

The construction selects $N_1,N_2\le C\log^8(en/\eta)$ neurons from
the original layers, together with positive diagonal mass matrices
$D_1,D_2$, each of total mass one. It stores a read-in $A_C$, the entire
small learned matrix $B_C$, and a readout $w_C$. Its forward pass is

\[
 h_C(x)=\tanh(A_Cx/\sqrt2),\qquad
 g_C(x)=\tanh(B_Ch_C(x)),\qquad
 f_C(x)=w_C^\top D_2g_C(x).
\]

Define $c_{C,a}=y_a-f_C(x_a)$,
$\delta_{C,a}=w_C\odot[1-g_C(x_a)^2]$, and the weighted adjoint
$B_C^*=D_1^{-1}B_C^\top D_2$. Its complete training equations are

\[
 \dot A_C=\sum_{a=1}^2c_{C,a}
 [\operatorname{sech}^2(A_Ce_a)\odot B_C^*\delta_{C,a}]e_a^\top,
\]
\[
 \dot B_C=\sum_{a=1}^2c_{C,a}\delta_{C,a}h_C(x_a)^\top D_1,
 \qquad \dot w_C=\sum_{a=1}^2c_{C,a}g_C(x_a).
\]

Thus it trains with its own errors and its own changing representations.
The weighted projected initialization of $B_C$ preserves both directions
of the original random interaction on the paired response coefficients. The
full construction and exact initializations are in Sections 3–5 of
[the main proof](TWO_INPUT_CANONICAL_COMPRESSION.md).

The count includes $N_1N_2$ moving matrix entries, all read-in and readout
coordinates, positive masses, and any retained initial-state copy. The
full original matrix, full-width response vectors, basis matrices and
initial-derivative arrays are discarded after setup. Runtime requires no
external residual path or original-network evaluation.

## Why two different label signs do not break the argument

With two examples, the two residuals need not maintain a fixed ratio.
Their associated parameter updates do not commute, so the two accumulated
activities cannot be treated as path-independent state coordinates.
The new comparison works directly
in physical time and keeps that changing residual direction.

Write $c_n(t)=(y_a-f_n(t,x_a))_{a=1}^2$ and similarly $c_C(t)$.
The useful error variable is the signed integral

\[
 p(t)=\int_0^t[c_C(s)-c_n(s)]\,ds.
\]

The initial upper-feature Gram matrix
$G_0=(g(0,x_a)^\top g(0,x_b)/n)_{a,b=1}^2$ has a positive gap
with high probability. Integration by parts in the full nonlinear state
equations yields a stable equation whose principal part is
$\dot p=-G_0p$. All remaining feedback terms are bounded by the
total residual activity, which is $O(\|y\|_2)$, times the state and
integrated-residual errors, plus the controlled sampling defect.
Small fixed labels let those terms be absorbed. This proves an all-time
comparison without demanding that residual components have equal signs,
equal magnitudes, or a constant direction. The exact inequalities and
their proof are in [the stability note](TWO_INPUT_STABLE_GEOMETRY.md).

## Why so few neurons suffice

The proof controls the actual finite-network forward and reverse responses
on a complex neighborhood of physical time and query angle. The neighborhood
has width $c/\sqrt{\log n}$ through a physical horizon $C\log n$.
Autonomous neuron-deletion comparisons justify the needed Gaussian bounds;
no population approximation or clipping modification is used.

Analytic approximation then represents all required responses using
$O(\log^4 n)$ vector coefficients. Positive cubature selects
$O(\log^8 n)$ neurons per layer while preserving their inner products
and paired forward/reverse mixer actions. The physical-time stability
estimate turns these response errors into trajectory and prediction errors.
Exponential fitting controls the entire remaining interval and endpoint.

The coefficients are computed from finitely many derivatives of the
initialized differential equations. A potentially enormous temporary
derivative list is first converted to approximate polynomial interpolation
data; only the much smaller final coefficient space is retained for neuron
selection. No trained trajectory is supplied as input. This distinction
between temporary derivative order and retained dimension gives the
polylogarithmic state bound.

## Feature learning and qualifications

[The feature-motion certificate](TWO_INPUT_FEATURE_LEARNING.md) proves
that both original hidden feature tuples move by at least
$c\|y\|_2^2$ at a fixed positive physical time, with high probability.
The constants and time are independent of width and label direction.
For every fixed nonzero small label vector, the same conclusion transfers
to the compressed model for sufficiently large $n$. This is a statement
about feature motion at a fixed time; no separate lower bound on final
feature displacement is asserted.

The following boundaries are material:

- The proved input pair is orthogonal, or a common rotation of it. General
  nonorthogonal pairs are not settled by this theorem.
- The activation is tanh, depth is two nonlinear hidden layers, and labels
  are fixed and sufficiently small. Large labels and arbitrary depth are
  not covered.
- Setup may require enormous work, temporary memory and numerical precision.
  The theorem counts exact real coordinates retained **after** setup. It is
  an autonomous representation theorem, not an efficient preprocessing or
  bit-complexity theorem.
- The smaller initialization and weights depend on the original realization
  and the task. It is not ordinary independent Gaussian resampling.
- The result compares the actual dense run with its constructed smaller run.
  It needs no dense-to-population theorem and leaves no unestimated population
  bias. It does not yet compress the unchanged order-$q$ closure uniformly
  in $q$.

## Evidence and status

The full proof is [TWO_INPUT_CANONICAL_COMPRESSION.md](TWO_INPUT_CANONICAL_COMPRESSION.md).
Its dependencies are [TWO_INPUT_STABLE_GEOMETRY.md](TWO_INPUT_STABLE_GEOMETRY.md)
and [TWO_INPUT_COMPLEX_SOURCE.md](TWO_INPUT_COMPLEX_SOURCE.md), plus the
already checked scalar inverse-coordinate strip in this study's
`COMPLEX_ACTIVITY_ROUTE.md`. Complete reconstruction reports are
[TWO_INPUT_CANONICAL_COMPRESSION_CHECK.md](TWO_INPUT_CANONICAL_COMPRESSION_CHECK.md)
and [TWO_INPUT_COMPLEX_SOURCE_CHECK.md](TWO_INPUT_COMPLEX_SOURCE_CHECK.md).
The feature certificate has its own check. The coordinator check records
final hashes, source reconciliation and full-chain scope.

No numerical experiment was used. No manuscript or maintained-book claim
was changed. These are internally checked study results, not independent
promotion reviews.
