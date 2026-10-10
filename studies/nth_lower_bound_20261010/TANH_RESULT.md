# Two-hidden-layer tanh: proved fixed-order bounds and the unresolved size question

This continues the NTH investigation on the nonlinear architecture requested
by the user. It does not replace the remaining growing-order problem with the
linear witness or with a conditional approximation theorem. Status: internally
checked fixed-order theorem; the requested growing-order result remains open. No paper,
maintained book, implementation, or experiment is changed.

## Current conclusion

For general fixed input configurations, the standard frozen-top orders two
and three have a nonvanishing error floor. An explicit whole-trajectory upper
bound also holds. These statements are unconditional within the stated
initialization, gap, and label assumptions: they require no unproved population
flow or high-order tensor estimate.

They do **not** determine which growing order attains dense-versus-dense
accuracy. No polynomial, superpolynomial, or exponential necessary or sufficient
NTH storage law for that target is proved here. The growing-order claim remains
open; the conditional criterion in TANH_UPPER_ROUTE is not an unconditional
answer to it.

## Setup

Let the fixed training inputs satisfy \(\|x_a\|_2=\sqrt d\),
\(a=1,\ldots,m\), with \(m\ge2\). Put \(v=x/\sqrt d\). The network is

\[
h^{(1)}(x)=\tanh(W^{(1)}v),\qquad
h^{(2)}(x)=\tanh(W^{(2)}h^{(1)}(x)),\qquad
f_n(x)=\frac{u^\top h^{(2)}(x)}n.
\]

The shapes are \(n\times d\), \(n\times n\), and \(n\). Independently,
the first weights have law \(N(0,1)\), the second weights have law
\(N(0,1/n)\), and \(u(0)=0\). All layers train with mobilities
\((n,1,n)\) and loss \(\|f-y\|_2^2/(2m)\). This is the canonical
feature-learning metric, not native lazy NTK scaling. The maintained full-MSE
convention doubles the vector field and makes no difference to the complete
trajectory norm below.

Starting with \(Q^{(0)}_{ab}=v_a^\top v_b\), define for \(\ell=1,2\)

\[
Q^{(\ell)}_{ab}=\mathbb E[\tanh Z_a\tanh Z_b],
\qquad Z\sim N(0,Q^{(\ell-1)}).
\]

Assume \(\gamma=\lambda_{\min}(Q^{(2)})>0\), and set
\(Y=\|y\|_2/\sqrt m\). The theorem below allows

\[
0<Y\le\frac{\gamma}{64m}.
\]

This includes the original, more restrictive small-label regime. All problem
parameters and labels are fixed independently of width. No orthogonality,
input-rank, label-sign, or extra dimension hypothesis is imposed. Probability
statements are for each prescribed dataset and label vector, not a single
event simultaneous over label vectors selected after seeing initialization.

Let \(M\) denote the mobility matrix. Define \(K_1=f\),
\(V_b=M\nabla f(x_b)\), and
\(K_{s+1,a_1\ldots a_s b}=D K_{s,a_1\ldots a_s}[V_b]\).
The order-\(q\) hierarchy copies these tensors through rank \(q\) at
initialization, freezes rank \(q\), and evolves lower ranks with its own
residual controls \((y_b-f_{q,b})/m\). It receives no dense future trajectory.

## Unconditional two-sided fixed-order theorem

For \(q=2\) or \(q=3\), every \(0<\delta<1\), and

\[
n\ge247808\left(\frac m\gamma\right)^4
               \log\frac{10m^2}{\delta},
\tag{0}
\]

with probability at least \(1-\delta\),

\[
\frac{Y^3}{384\cdot10^{15}}\left(\frac\gamma m\right)^8
\le
\sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}
 |f_q(t,x)-f_n(t,x)|
\le
7300Y^3\left(\frac m\gamma\right)^3.
\tag{1}
\]

Both systems exist globally and fit the training labels. The lower bound is
witnessed at the positive physical time
\(t=(\gamma/m)^2/10^5\), not at the fitted endpoint. Its witness is one of
the training predictions, so any declared panel containing those inputs also
inherits the lower bound. The upper bound includes every unseen sphere query
and the fitted limit.

The lower-bound initialization event has the explicit failure estimate

\[
2e^{-(8-2\log9)n}
+2m^2\exp\left[-\frac{n(\gamma/m)^4}{247808}\right]
+\exp\left[-\frac{n(\gamma/m)^4}{128}\right].
\tag{2}
\]

The upper bound uses only the additional initialized feature-Gram event
\(K_2(0)\succeq\gamma I/2\). Besides the common matrix-operator event in
(2), its failure probability is at most

\[
2m^2\exp\left[-\frac{n(\gamma/m)^2}{288}\right]
+2m^2\exp\left[-\frac{n(\gamma/m)^2}{32}\right].
\tag{3}
\]

The sum of (2) and (3) is at most \(\delta\) under (0). The complete
covariance-interpolation and concentration calculation is in
[TANH_CHECK.md](TANH_CHECK.md). There is no unquantified extra width
threshold or hidden derivative-growth premise in (1).

The storage implication is deliberately limited: fixed orders two and three
cannot achieve an absolute error tending to zero, in particular an
\(n^{-1/2}\)-scale target with fixed problem parameters. This does not imply
anything yet about the required growth of \(q\). Orders two and three are
identical here because zero readout makes the initialized third tensor zero.

On a finite declared panel, the order-two model retains its initialized
\((m+p)\times m\) kernel and predictions. The sphere accuracy statement does
not provide a constant-size representation of its query kernel: evaluating
arbitrary future inputs still requires an initialized feature evaluator or
another separately charged representation.

## The proof mechanisms

The complete lower proof is [TANH_LOWER_ROUTE.md](TANH_LOWER_ROUTE.md).
For a normalized label direction \(c=y/(mY)\), introduce only within this
argument
\(H(Z)=\sum_a c_a\tanh Z_a\), \(Z\sim N(0,Q^{(1)})\).
The label-contracted fourth NTH tensor contains a nonnegative squared norm
from training the last hidden matrix. Its population value, after dividing
out \(Y^4\), is

\[
\mathbb E\left[H^2(c\odot\operatorname{sech}^2 Z)^\top
 Q^{(1)}(c\odot\operatorname{sech}^2 Z)\right]
\ge\frac14\mathbb EH^4
\ge\frac{\gamma^2}{4m^2}.
\]

The first inequality is Gaussian Poincare applied to the odd function
\(H|H|\); the second uses the feature-Gram gap. This works even if an
intermediate covariance is singular. Bounded Gaussian row averages transfer
the inequality to finite width. An integrated energy estimate then turns it
into an actual prediction gap, with the nonlinear dense and frozen-kernel
residuals compared at the same physical time.

Section 4 of [TANH_UPPER_ROUTE.md](TANH_UPPER_ROUTE.md) proves the upper
bound. Readout energy and the initial feature gap bound total parameter motion
and preserve that gap. Kernel subtraction controls the training prediction
error. Splitting the readout difference into the span of the initialized
training features and its orthogonal complement then controls every sphere
query without an additional exponential stability factor. Hidden layers in
the reference network remain fully trained.

## Why this does not yet settle growing order

The initialized hierarchy has an exact ordered-integral representation using
its own residual. A convergent high-order tail would give a sufficient order
and therefore a tensor-storage count. The missing step is such a tail bound
for the actual tanh model, uniformly as order and width grow together.

The obstruction to one simple proof is itself rigorous. The exact conditional
Gaussian calculation in [TANH_GENERIC_ROUTE.md](TANH_GENERIC_ROUTE.md) shows
that the largest initialized first-feature acceleration is of order
\(\sqrt{\log n}\), despite bounded tanh features. A complex time disk on
which every such coordinate has a fixed modulus bound must therefore have
radius at most a constant times \((\log n)^{-1/4}\). A width-independent
coordinatewise analytic radius cannot be assumed.

This is not a prediction-error lower bound. Gaussian averaging can cancel
individual-coordinate analytic obstructions. Conversely, bounded tanh and
finite Gaussian moments do not by themselves prove convergence of the
averaged hierarchy. A general growing-order upper or lower bound still needs
to control those cancellations, the entire omitted tail, and the closure's
own residual feedback. No storage exponent is inferred from the number of
formal tensor entries alone.

The additional bounded follow-up
[TANH_HIGH_ORDER_ROUTE.md](TANH_HIGH_ORDER_ROUTE.md) derives the exact next
source contraction. Unlike the fourth-order squared norm, it includes an
indefinite feature-curvature term. A scalar tanh example makes its sign change
and cancellation explicit, but is labeled as a diagnostic rather than a
counterexample to the canonical Gaussian model. Conditional Gaussian moments
also fail to isolate a noncancelling component of the prediction error. These
attempts did not resolve the growing-order question.

## Check status

Root read all three new route files completely and reconstructed their central
claims. The additional scoped check identified and repaired a factor-of-two
error in one early-time remainder integral: its correct coefficient is
\(B^2Y^3t^3/3\), not \(B^2Y^3t^3/6\). A sharper short-time estimate
preserves (1). Root then read the complete amended proof and
[TANH_CHECK.md](TANH_CHECK.md), including its explicit joint width bound.
The check records the exact source hashes and verifies the lower proof and
Sections 1 and 4 of the upper proof. It does not validate the conditional
growing-order criterion or solve the remaining storage question. Subsequent
high-order diagnostics are separately labeled. Root also checked the subsequent
lower-route replacement of the external fitting dependency by the same-study
bootstrap; its early-time proof is unchanged. That cleanup changes the lower
file hash to `3764da5fedbf1e8be8384638f9b29d9cfce6290a886db878a9b0c2ea87f130e0`.
Root reconstructed the sixth-contraction identity and read the complete
high-order diagnostic; it does not yield a storage theorem.
This is not an independent
promotion review and does not authorize paper or book edits.
