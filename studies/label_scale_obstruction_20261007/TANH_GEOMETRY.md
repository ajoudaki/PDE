# Why the both-tanh failure needs different geometry

2026-10-10. Internally derived complementary results for the same study.
These arguments use only the canonical finite network below. They do not
establish typical Gaussian failure, incompressibility, or a large-label
threshold. The explicit positive bad-basin construction is in
`TANH_BAD_BASIN.md`.

## 1. Setup and exact flow

Let `X` have columns `x_a/sqrt(d)`, where the training inputs have norm
`sqrt(d)`. There are `m` inputs and `n` neurons in each hidden layer. Set
\[
U=\tanh(AX),\quad Z=WU,\quad H=\tanh Z,\quad
f=H^\top w/n,\quad r=f-y,\quad
\mathcal L=\|r\|^2/m,\quad Y=\|y\|/\sqrt m.
\]
The mean-loss gradient flow has block mobilities `(n,1,n)`, and `w(0)=0`.
All activations and their derivatives are applied entrywise. For each top
neuron `i`, write
\[
D_i=\operatorname{diag}_{a=1}^m\bigl(\operatorname{sech}^2 Z_{ia}\bigr).
\]
At finite parameters these diagonal matrices are strictly positive. In
particular,
\[
\dot w=-\frac2m Hr,\qquad
\dot W_{i:}=-\frac{2w_i}{mn}(U D_i r)^\top.
\tag{1}
\]
The full tangent Gram `K` includes the positive semidefinite contributions
of all three trained blocks. Its `W` contribution is exactly
\[
K_W=\frac1{n^2}\sum_i w_i^2D_iU^\top U D_i,
\quad \dot r=-\frac2m Kr,\quad
\dot{\mathcal L}=-\frac4{m^2}r^\top Kr.
\tag{2}
\]

## 2. A finite non-fitting endpoint must lose lower-feature rank

Suppose a finite critical point has `rank(U)=m` and some `w_i!=0`.
Stationarity of the corresponding row of `W`, by (1), gives
`U D_i r=0`. Injectivity of `U` and invertibility of `D_i` imply `r=0`.
Thus it fits exactly.

Consequently, suppose a zero-readout trajectory has strictly decreased its
loss at some finite time and converges to finite parameters. Its limiting
readout cannot be zero: zero readout would give limiting loss `Y^2`,
whereas loss monotonicity keeps it below `Y^2` after the strict decrease.
If the limit does not fit, its first-layer feature matrix must therefore
be rank deficient.

This excludes the cosine construction's particular endpoint geometry:
with tanh at the top, a finite non-fitting endpoint after learning cannot
retain a full-rank preceding feature matrix. The reason is
`tanh'(z)>0` at every finite real `z`, not a generic guarantee of fitting.

## 3. Quantitative fitting while enough lower geometry survives

Define along a trajectory
\[
\kappa(t)=\lambda_{\min}\bigl(U(t)^\top U(t)/n\bigr),\qquad
B(t)=\max_{i,a}|Z_{ia}(t)|.
\]
Equation (2) gives the valid scalar lower bound
\[
K(t)\succeq K_W(t)
\succeq \kappa(t)\operatorname{sech}^4 B(t)
\frac{\|w(t)\|^2}{n}I_m.
\tag{3}
\]
Indeed `U^T U>=n kappa I`, and each `D_i^2` is bounded below by
`sech^4(B) I`. No commutation of `D_i` and `U^T U` is assumed.

Fix a time `t_0` with strict loss improvement, and put
\[
b=Y-\sqrt{\mathcal L(t_0)}>0.
\]
For every `t>=t_0`, loss monotonicity and the triangle inequality give
`||f(t)||>=sqrt(m)b`. Since every top feature has absolute value at most
one,
\[
\|f(t)\|\le\sqrt{m/n}\,\|w(t)\|,
\qquad \frac{\|w(t)\|^2}{n}\ge b^2.
\]
Combining this with (2)--(3) and integrating yields
\[
\mathcal L(t)\le\mathcal L(t_0)
\exp\!\left[-\frac{4b^2}{m}
\int_{t_0}^t\kappa(s)\operatorname{sech}^4 B(s)\,ds\right].
\tag{4}
\]
In particular, a uniformly positive lower-feature gap and uniformly
bounded top preactivations force exponential fitting. More generally,
divergence of the integral in (4) forces fitting. Conversely, strictly
positive limiting loss requires this integral to be finite. This
necessary condition alone constructs no non-fitting trajectory.

The first-layer rank collapse in the both-tanh bad basin is compatible
with (4). The bound neither excludes that collapse nor proves that it
occurs typically at Gaussian initialization.

## 4. Independent inputs exclude nonzero-readout bad local minima

Assume now `rank(X)=m` and `n>=m`. Every finite non-fitting critical point
with a nonzero readout is a strict saddle, meaning that the parameter
Hessian of the loss has a strictly negative quadratic direction.

To prove this, Section 2 allows us to assume `rank(U)<m`. Choose
`v!=0` in `ker(U^T)`, possible since `rank(U)<m<=n`, and choose a row `i`
with `w_i!=0`. Use the parameter variation
\[
\delta_1 W=e_i v^\top,
\]
with the other blocks fixed. Along this entire parameter line,
`delta_1 W U=0`, so the predictions are constant. Both its first prediction
variation and its pure loss Hessian entry are zero.

Independently choose a first-layer variation that induces
\[
\delta_2 U=v(D_i r)^\top.
\]
It is realizable: all entries of `sech^2(AX)` are positive, and the
explicit choice
\[
\delta_2 A=
\left[\delta_2 U\mathbin{\oslash}\operatorname{sech}^2(AX)\right]
(X^\top X)^{-1}X^\top
\tag{5}
\]
has the required derivative. Here `oslash` denotes entrywise division.
The mixed prediction derivative is
\[
\delta_1\delta_2 f_a
=\frac{w_i}{n}(D_i)_{aa}\,v^\top\delta_2U_{:a}.
\]
The Jacobian-square part of the mixed loss Hessian vanishes because
`delta_1 f=0`. Its remaining entry is
\[
D^2\mathcal L[\delta_1,\delta_2]
=\frac{2w_i}{mn}\|v\|^2\|D_i r\|^2\ne0.
\tag{6}
\]
Thus the Hessian restricted to these two variations has a zero first
diagonal entry and a nonzero off-diagonal entry. Its determinant is
strictly negative, proving a negative direction.

This does not by itself prove that the exact zero-readout initialization
slice avoids every stable set of a strict saddle. Nor does it exclude
non-fitting escape toward infinite parameters. It does show that the
finite attracting local-minimum mechanism used in the explicit both-tanh
construction cannot be transferred unchanged to linearly independent
training inputs. In particular, two distinct nonantipodal sphere inputs
are linearly independent; the 18-point circle construction deliberately
has dependent inputs.

## Status

These are direct identities and elementary finite-dimensional arguments,
not imported neural-network theorems. They clarify the scope of the
positive example rather than solving arbitrary-label, large-width
Gaussian fitting. The underlying coordinates and mean-loss factors were
reconstructed by the lead and checked in the reused
`two_layer_persistence` and `residual_alignment_route` agent contexts;
that is internal checking, not an independent promotion review.
