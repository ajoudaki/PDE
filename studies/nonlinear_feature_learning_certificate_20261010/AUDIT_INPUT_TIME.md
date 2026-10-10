# Scoped audit: real-time bound, finite-query limit, and compression transfer

Date: 2026-10-10.

Verdict: no substantive defect found in Sections 3 and 4 of
`INPUT_NONLINEARITY_RESULT.md`. The explicit constants, first-layer scaling,
finite-query covariance argument, fixed-time probability quantifiers, and
Taylor panel costs are valid. This is a scoped mathematical check, not a
promotion review or a verification of the supplied all-layer feature-learning
theorem.

## Scope and inputs

I read the complete candidate and `paper/compact.tex`, using the latter for
the canonical network, exact flow, probability convention, compression
conclusions, and Taylor storage formula. I applied the rigorous-math and
canonical-notation skills, including the neural-network reference. I did not
read other study artifacts or prior checks. Kernel nonaffinity, the four-point
witness, and the previously established feature-learning separation are
treated as inputs for the checks below.

The network uses normalized inputs \(v=x/\sqrt d\), \(\|v\|_2=1\), first
preactivation \(W^{(1)}v\), hidden preactivations
\(W^{(\ell)}h^{(\ell-1)}\), and output \(f_n=w^\top h^{(L)}/n\).
Residuals are \(r_a=f_n(x_a)-y_a\), and
\(Y=(m^{-1}\sum_a y_a^2)^{1/2}>0\). The response
\(\delta_a^{(\ell)}\) is exactly the residual-free backward response in
the paper. This symbol is distinct from the positive scalar witness margin
\(\delta\) in the candidate's equation (4).

## 1. Width-uniform bootstrap and its constants

Use precisely the candidate's constants

\[
A=B+1,\quad H=(2A^2)^L,\quad D=A^{2L},\quad
E=2Y^2DH^2,\quad T=\min\{1,(2YH\sqrt D)^{-1}\}.
\]

While \(\|W^{(1)}\|_{\rm op}/\sqrt n<A\) and
\(\|W^{(\ell)}\|_{\rm op}<A\) for \(\ell\ge2\), linear growth gives

\[
\frac{\|h^{(1)}(x)\|_2}{\sqrt n}\le B+BA\le2A^2,
\qquad
\frac{\|h^{(\ell)}(x)\|_2}{\sqrt n}
\le B+BA\frac{\|h^{(\ell-1)}(x)\|_2}{\sqrt n}
\le(2A^2)^\ell\le H.
\]

This is uniform on the input sphere and does not require bounded activation
values or bounded individual coordinates. Backward recursion gives

\[
\|\delta_a^{(\ell)}\|_2
\le B^{L-\ell+1}A^{L-\ell}\|w\|_2
\le D\|w\|_2.
\]

Positive gradient-flow mobilities make the mean-square loss nonincreasing;
zero readout therefore gives \(m^{-1}\sum_a r_a^2\le Y^2\).
The exact readout equation and Cauchy--Schwarz over training examples yield

\[
\frac{\|\dot w\|_2}{\sqrt n}\le2YH,
\qquad \frac{\|w(t)\|_2}{\sqrt n}\le2YHt.
\]

The matrix speeds have the following normalizations:

\[
\begin{aligned}
\frac{\|\dot W^{(1)}\|_{\rm op}}{\sqrt n}
&\le\frac2m\sum_a |r_a|\frac{\|\delta_a^{(1)}\|_2}{\sqrt n}
\le2YD\frac{\|w\|_2}{\sqrt n},\\
\|\dot W^{(\ell)}\|_{\rm op}
&\le\frac2m\sum_a |r_a|
\frac{\|\delta_a^{(\ell)}\|_2}{\sqrt n}
\frac{\|h_a^{(\ell-1)}\|_2}{\sqrt n}
\le2YDH\frac{\|w\|_2}{\sqrt n}.
\end{aligned}
\]

Thus hidden-matrix increments are at most \(Et^2\), and the scaled
first-matrix increment is at most \(2Y^2DHt^2\le Et^2\). There is no
missing factor of \(n\), \(\sqrt n\), or \(d\) in the first layer.
Furthermore \(ET^2\le1/2\), so all bootstrapped matrix norms stay at most
\(B+1/2<A\). The bounded readout and matrices also justify finite-dimensional
ODE continuation through this interval.

For feature increments, the first layer starts at \(BEt^2\). At later
layers the current-matrix/initial-feature decomposition gives the recursion

\[
\frac{\|h^{(\ell)}(t,x)-h^{(\ell)}(0,x)\|_2}{\sqrt n}
\le BA\frac{\|h^{(\ell-1)}(t,x)-h^{(\ell-1)}(0,x)\|_2}{\sqrt n}
+BEHt^2.
\]

Consequently the proposed common bound
\(Jt^2\), where \(J=BEH\sum_{k=0}^{L-1}(BA)^k\), is sufficient.

To check the last constant, use

\[
\dot w(t)-\dot w(0)
=-\frac2m\sum_a\left[
r_a(t)(h_a^{(L)}(t)-h_a^{(L)}(0))
+f_n(t,x_a)h_a^{(L)}(0)\right].
\]

The output bound is \(\sup_x|f_n(t,x)|\le2YH^2t\), so this identity gives
the claimed \(4YH^3t+2YJt^2\) bound for the readout-velocity difference
divided by \(\sqrt n\). Since
\(g_n(x)=\dot w(0)^\top h^{(L)}(0,x)/n\), decompose the remainder as

\[
f_n(t,x)-tg_n(x)
=\frac{(w(t)-t\dot w(0))^\top h^{(L)}(0,x)}n
+\frac{w(t)^\top(h^{(L)}(t,x)-h^{(L)}(0,x))}n.
\]

Integration bounds this by

\[
2YH^4t^2+\left(\frac23+2\right)YHJt^3
\le\left(2YH^4+\frac83YHJT\right)t^2.
\]

Equation (6), including its coefficient \(8/3\), is therefore correct.
This argument uses only real-time estimates and is uniform in width on the
stated initialization event.

The initialization event has probability tending to one. The first-layer
claim follows from \(W^{(1)\top}W^{(1)}/n\to I_d\) with fixed \(d\).
For a hidden Gaussian matrix, two radius-\(1/4\) sphere nets have at most
\(9^{2n}\) pairs, and the net estimate and scalar Gaussian tails give
\(\Pr\{\|W\|_{\rm op}>B\}\le2\exp(2n\log9-nB^2/8)\).
Thus \(B\ge8\) is already sufficient for the elementary net proof.

## 2. Initial finite-query covariance convergence

For any fixed finite query list, write its layer-\(\ell\) empirical Gram as
\(n^{-1}h^{(\ell)}(x)^\top h^{(\ell)}(x')\). At the first layer the rows
of the preactivation tuples are independent centered Gaussians with the
deterministic input Gram as covariance. At each following layer, condition
on the preceding features: the Gaussian weight normalization \(1/n\)
makes this conditional covariance exactly the preceding empirical Gram.

On any bounded set of covariance matrices, linear growth of the activation
and bounded Gaussian fourth moments bound the second moment of each product
\(\phi(Z_a)\phi(Z_b)\). Its empirical average has conditional variance at
most a fixed constant divided by \(n\). The previous covariance convergence
puts the random covariance in such a bounded set with probability tending
to one. Conditional Chebyshev therefore proves convergence to the conditional
mean.

The covariance-to-mean map is continuous, including at singular matrices:
for covariance matrices \(Q_j\to Q\), couple the Gaussian vectors as
\(Q_j^{1/2}G\) and \(Q^{1/2}G\). Continuity of the positive square root
gives convergence in mean square; the Lipschitz activation and bounded
second moments then give convergence of the feature-product expectations.
Induction and a finite union bound establish all required Gram limits.
Finally zero readout gives the exact normalization

\[
g_n(x)=\frac2m\sum_a y_a
\frac{h_a^{(L)}(0)^\top h^{(L)}(0,x)}n.
\]

Thus the displayed convergence to equation (3) is valid at the four fixed
witnesses. It requires neither a trained passive-query population limit nor
a uniform limit over the sphere.

## 3. Fixed-time transfer and Taylor panel costs

Intersect the initialization event above with the event that the witness
applied to \(g_n\) is within \(\delta/4\) of \(\delta\). Both have
probability tending to one. The normalized witness and equation (6) give,
for \(0<t\le\min\{T,\delta/(4C)\}\),

\[
\sum_i c_i f_n(t,\sqrt d\,u_i)
\ge\frac34\delta t-Ct^2\ge\frac12\delta t.
\]

The affine annihilation remains valid in physical coordinates because
\(\sum_i c_i\sqrt d\,u_i=0\). Each compression error tends to zero in
probability on its promised domain. At each fixed positive \(t\), requiring
this error to be at most \(\delta t/4\) leaves a lower bound
\(\delta t/4\). A finite union bound handles all three methods and the
supplied feature-learning events without requiring independence. Taking
minimum positive constants and time thresholds is valid. The argument does
not imply a compression separation uniform over times approaching zero with
width; the candidate correctly claims a fixed-time result.

The witnesses are deterministic functions of fixed training inputs, labels,
and the population kernel. Dependence on training labels does not violate a
panel declaration before random initialization. They use no passive labels,
realized weights, or trained trajectory. No uniform theorem over arbitrary
data-dependent or initialization-dependent panel choices is invoked.

For \(p'\le p+4\), substitution in the paper's existing Taylor bound gives
exactly the displayed sufficient storage. Since \(m+p\ge2\),

\[
\frac{m+p+4}{m+p}\le3,\qquad
\frac{(m+p+4)^2}{(m+p)^2}\le9.
\]

The data factor and quadratic panel factor therefore grow by at most three
and nine, respectively. The \((\log n)^3\) asymptotic order is preserved.

## Minor presentation clarifications

These do not require any change to the conclusions or constants:

- At candidate lines 283–290, explicitly intersect the witness event with the
  initialization operator-norm event when applying equation (6). The intended
  intersection is available and still has probability tending to one.
- At lines 196–197, say “a trained passive-query population limit” to distinguish
  it from the initial finite-query covariance limit used later. At lines
  330–332, say “the exponent of \(\log n\) is still three” instead of “its
  width exponent is still three.”

No experiments were needed. The candidate was not edited.
