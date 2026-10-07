# Direct response construction: a cubic sphere decoder and the high-order obstruction

Status: bounded constructive attempt, 2026-10-05. The scope is one training
sample with a fixed nonzero sufficiently small label. The proved advance is
a law-computable autonomous cubic model with a decoder defined on the whole
input sphere, together with an explicit obstruction to deriving a convergent
high-order response expansion from the available deterministic bounds.
This is **not** the requested \(n^{-1/2}\)-accurate compact construction.

Only the assignment, `docs/notation.qmd`, and this agent's own
`ANALYTIC_ROUTE.md` and `RANDOM_SMALL_LIMITATION.md` were used. Those frozen
artifacts were not edited. The previously read investigation and proof
skills apply. The required canonical-notation skill remains inaccessible;
the supervisor-authorized explicit-notation fallback is retained. No
experiment, other study, dense trajectory, or response oracle was used.

## 1. The exact response coefficients to be generated

Let \(\phi=\tanh\). Fix \((x_1,y)\) with
\(\|x_1\|_2=\sqrt d\). The dense width-\(n\) network is

\[
 u(x)=Ax/\sqrt d,\quad h(x)=\phi(u(x)),\quad
 v(x)=Wh(x),\quad g(x)=\phi(v(x)),\quad
 f_n(x)=w^Tg(x)/n.
\]

The loss is \((f_n(x_1)-y)^2\), with mobilities \((n,1,n)\).
Initially \(A_{ij}\) are iid \(\mathcal N(0,1)\), \(W_{ij}\) are
iid \(\mathcal N(0,1/n)\), independently, and \(w=0\).

Use the feature flow

\[
 w'=g_1,\qquad W'=\frac{(w\odot\phi'(v_1))h_1^T}{n},\qquad
 A'=[\phi'(u_1)\odot W^T(w\odot\phi'(v_1))]\frac{x_1^T}{\sqrt d},
 \tag{1}
\]

where primes denote feature-time derivatives and subscripts 1 denote the
training point. Its physical-time parametrization is

\[
 \dot s=2[y-F_n(s)],\qquad
 F_n(s)=f_n(x_1;s),\qquad s(0)=0.
 \tag{2}
\]

For a spherical test input \(x\), put \(c=x_1^Tx/d\in[-1,1]\).
The exact first-layer relation is
\(u(x;s)=u(x;0)+c[u_1(s)-u_1(0)]\).
At feature time zero define

\[
 h=h_1,\quad k=h(x),\quad v=v_1,\quad z=v(x),\quad
 b=\phi(v)\odot\phi'(v),\quad
 D_1=\operatorname{diag}(\phi'(u_1)^2),\quad
 D_2=\operatorname{diag}(\phi'(u_1)\phi'(u(x))).
\]

Products between vectors in these formulas are entrywise unless a matrix
product is written. All first derivatives of the hidden coordinates vanish
at zero because \(w(0)=0\). Differentiating (1) twice gives

\[
 \begin{aligned}
 v_1''&=\left(\frac{h^Th}{n}I+WD_1W^T\right)b,\\
 v(x)''&=\frac{h^Tk}{n}b+cWD_2W^Tb.
 \end{aligned}
 \tag{3}
\]

The feature flow is even in its hidden parameters and odd in the readout.
Since \(w'=g_1\), its prediction has the finite-width expansion

\[
 f_n(x;s)=\kappa_n(x)s+C_n(x)s^3+O_{n,x}(s^5),
 \quad \kappa_n(x)=\frac{\phi(v)^T\phi(z)}n.
 \tag{4}
\]

The cubic coefficient is explicitly

\[
 \begin{aligned}
 C_n(x)={}&\frac{h^Th}{6n}\frac{\ell_1^Tb}{n}
 +\frac{h^Tk}{2n}\frac{\ell_2^Tb}{n}\\
 &+\frac{\ell_1^TWD_1W^Tb}{6n}
 +\frac{c\,\ell_2^TWD_2W^Tb}{2n},\\
 \ell_1&=\phi'(v)\odot\phi(z),\qquad
 \ell_2=\phi(v)\odot\phi'(z).
 \end{aligned}
 \tag{5}
\]

Indeed, the cubic product coefficient is
\(g_1''(0)^Tg(x;0)/(6n)+g_1(0)^Tg(x)''(0)/(2n)\), and (3)
gives (5). The width-dependent remainder in (4) is deliberately not
replaced by a uniform estimate.

## 2. Direct Gaussian formulas for the whole-sphere decoder

The following definitions involve at most two Gaussian variables in any
one integral. Let \((U,U_x)\) be a centered Gaussian pair with variances
one and covariance \(c\). Set

\[
 H=\phi(U),\qquad H_x=\phi(U_x),\qquad
 q=\mathbb EH^2,\qquad p(c)=\mathbb E[HH_x].
\]

Separately let \((Z,Z_x)\) be centered Gaussian with covariance matrix

\[
 \begin{pmatrix}q&p(c)\\p(c)&q\end{pmatrix}.
 \tag{6}
\]

All expectations involving \(U,U_x\) are over the first pair; all
expectations involving \(Z,Z_x\) are over the second. These are products
of numerical expectations, not unspecified mixed correlations.
Define

\[
 \begin{aligned}
 b(z)&=\phi(z)\phi'(z),\\
 \ell_1(z,z_x)&=\phi'(z)\phi(z_x),\qquad
 \ell_2(z,z_x)=\phi(z)\phi'(z_x),\\
 D_1(U,U_x)&=\phi'(U)^2,\qquad
 D_2(U,U_x)=\phi'(U)\phi'(U_x).
 \end{aligned}
\]

For one of these functions \(D\) and a smooth function \(\ell\), put

\[
 \begin{aligned}
 T(D,\ell)={}&\mathbb E[D]\,\mathbb E[\ell(Z,Z_x)b(Z)]\\
 &+\mathbb E[b'(Z)]\left(
 \mathbb E[DH^2]\,\mathbb E[\partial_1\ell(Z,Z_x)]
 +\mathbb E[DHH_x]\,\mathbb E[\partial_2\ell(Z,Z_x)]
 \right).
 \end{aligned}
 \tag{7}
\]

The desired law-generated linear and cubic decoder functions are

\[
 \begin{aligned}
 \kappa(c)&=\mathbb E[\phi(Z)\phi(Z_x)],\\
 C_3(c)&=\frac q6\mathbb E[\ell_1(Z,Z_x)b(Z)]
 +\frac{p(c)}2\mathbb E[\ell_2(Z,Z_x)b(Z)]\\
 &\hspace{1em}+\frac16T(D_1,\ell_1)+\frac c2T(D_2,\ell_2).
 \end{aligned}
 \tag{8}
\]

These expressions have no singular inverse Gram matrix. They are defined
also at \(c=\pm1\), where the Gaussian pairs are degenerate. In
particular, \(\kappa(-1)=-\kappa(1)\),
\(C_3(-1)=-C_3(1)\), and both functions vanish at \(c=0\), as also
follows from the sign symmetries of the centered Gaussian pairs.

For the training input, set \(\kappa=\kappa(1)>0\). The cubic
coefficient becomes

\[
 C_3(1)=\frac23\left[(q+a_1)\beta+q_D\zeta^2\right]>0,
 \tag{9}
\]

where
\(a_1=\mathbb E\phi'(U)^2\),
\(q_D=\mathbb E[\phi(U)^2\phi'(U)^2]\),
\(\beta=\mathbb E b(Z)^2\), and
\(\zeta=\mathbb E b'(Z)\), with \(Z\sim\mathcal N(0,q)\).
Thus (8) agrees with the previously checked training-point coefficient.

## 3. Proof that these are the dense coefficients, without a response oracle

For every fixed spherical test input \(x\), there is an absolute finite
constant \(K\), independent of \(n,d,x\), such that

\[
 \mathbb E|\kappa_n(x)-\kappa(c)|^2
 +\mathbb E|C_n(x)-C_3(c)|^2\le K/n.
 \tag{10}
\]

Consequently their errors are at most \(K_\delta/\sqrt n\) with
probability \(1-\delta\) for each fixed input. Although the constant is
uniform in the choice of input, this is not a simultaneous supremum over
the sphere.

Here is a direct contraction argument establishing (10). Condition on the
first-layer vectors \(h,k\). Each row pair \((v_i,z_i)\) is an
independent Gaussian with covariance

\[
 \Sigma_n=\frac1n
 \begin{pmatrix}h^Th&h^Tk\\h^Tk&k^Tk\end{pmatrix}.
\]

For bounded smooth \(\ell,b\), consider
\(J_n=n^{-1}\ell(v,z)^TWDW^Tb(v)\), where \(D\) is any bounded
diagonal matrix determined by the first layer. Write \(\mathbb E_W\)
for expectation over \(W\) conditional on that layer. Gaussian integration
by parts in a row gives

\[
 \begin{aligned}
 \mathbb E_W[W_{ij}\ell(v_i,z_i)]
 &=\frac1n\left(h_j\mathbb E_W\partial_1\ell
                   +k_j\mathbb E_W\partial_2\ell\right),\\
 \mathbb E_W[W_{ij}b(v_i)]&=\frac{h_j}{n}\mathbb E_W b'.
 \end{aligned}
 \tag{11}
\]

For two equal row indices, applying the same identity twice gives, with
\(L_j=h_j\partial_1+k_j\partial_2\),

\[
 \mathbb E_W[W_{ij}^2\ell(v_i,z_i)b(v_i)]
 =\frac1n\mathbb E_W[\ell b]
 +\frac1{n^2}\mathbb E_W[L_j^2(\ell b)].
\]

Separate equal and unequal row indices in \(J_n\). Since
\(|h_j|,|k_j|\le1\) and the required derivatives are bounded, one
obtains the exact formula up to a uniformly bounded \(O(n^{-1})\) term:

\[
 \begin{aligned}
 \mathbb E_WJ_n={}&\left(\frac1n\sum_jD_j\right)\mathbb E_W[\ell b]\\
 &+\left(1-\frac1n\right)\mathbb E_Wb'
 \left[
 \left(\frac1n\sum_jD_jh_j^2\right)\mathbb E_W\partial_1\ell
 +\left(\frac1n\sum_jD_jh_jk_j\right)\mathbb E_W\partial_2\ell
 \right]+O(n^{-1}).
 \end{aligned}
 \tag{12}
\]

More explicitly, the omitted term is
\(n^{-2}\sum_jD_j\mathbb E_W[L_j^2(\ell b)]\).
The formulas use differentiation with respect to the original Gaussian
matrix entries, so they remain valid when \(\Sigma_n\) is singular.

To bound fluctuations about (12), a useful elementary Gaussian inequality
is

\[
 \operatorname{Var}J_n\le\frac1n
 \mathbb E_W\|\nabla_WJ_n\|_F^2.
 \tag{13}
\]

For clarity, (13) follows from an integration argument, not from an assumed
population theorem. For a standard Gaussian vector \(X\), an independent
copy \(Y\), and a smooth function \(F\), define
\(X_t=e^{-t}X+\sqrt{1-e^{-2t}}Y\). Differentiating
\(\mathbb E[F(X)F(X_t)]\), and integrating by parts in \(X,Y\), gives
\(-e^{-t}\mathbb E[\nabla F(X)\cdot\nabla F(X_t)]\).
Integrating from zero to infinity and using Cauchy--Schwarz yields
\(\operatorname{Var}F(X)\le\mathbb E\|\nabla F(X)\|_2^2\).
Rescaling the entries to variance \(1/n\) gives (13). Smooth cutoffs
justify the calculation first for bounded derivatives; the polynomial
Gaussian moment bounds below allow the cutoff to be removed.

Let \(a=W^T\ell(v,z)\) and \(b_0=W^Tb(v)\), so
\(J_n=a^TDb_0/n\). Differentiating these two vectors shows

\[
 \|\nabla_WJ_n\|_F
 \le K_1\bigl(\|W\|_{\rm op}+\|W\|_{\rm op}^2\bigr),
 \tag{14}
\]

with a constant depending only on the bounded functions and their first
derivatives. For example, differentiating the explicit \(W^T\ell\)
factor gives a matrix of norm at most
\(\|\ell\|_2\|Db_0\|_2/n\le K_1\|W\|_{\rm op}\).
Differentiating \(\ell(v,z)\) gives matrices such as
\(\operatorname{diag}(\partial_1\ell)WD b_0h^T/n\), with norm at
most \(K_1\|W\|_{\rm op}^2\). The other terms obey the same bounds.

The elementary Gaussian net bound
\(\mathbb P(\|W\|_{\rm op}>u)
\le2\exp[-n(u^2/8-2\log9)]\) for sufficiently large \(u\)
implies uniformly bounded second and fourth operator-norm moments by
integrating its tail. Its proof is the one-quarter-net and scalar Gaussian
tail argument given in `RANDOM_SMALL_LIMITATION.md`. Equations (13)--(14)
therefore give
\(\mathbb E_W|J_n-\mathbb E_WJ_n|^2\le K_2/n\).

It remains to compare (12) with (7). Every first-layer average in (12) is
an average of bounded independent functions of the iid Gaussian pairs
\((u_i,u(x)_i)\), so its mean squared error is \(O(n^{-1})\).
Gaussian expectations of a smooth function with bounded second derivatives
are Lipschitz in their covariance entries: interpolate linearly between
the two covariance matrices, differentiate the Gaussian density, and
integrate by parts twice to obtain

\[
 \frac d{dt}\mathbb EF(G_t)
 =\frac12\sum_{ij}(\Sigma_1-\Sigma_0)_{ij}
     \mathbb E[\partial_i\partial_jF(G_t)].
 \tag{15}
\]

Adding \(\varepsilon I\) first proves the identity for positive definite
matrices; bounded derivatives and convergence in distribution allow
\(\varepsilon\downarrow0\). Thus no inverse covariance bound is
needed. Equations (12), (15), and the empirical-average bounds prove that
\(J_n\) approaches (7) in mean square at rate \(O(n^{-1})\).
The same conditional-average argument applies to the first two terms in
(5), and to \(\kappa_n(x)\). This proves (10), including \(c=\pm1\).

## 4. A direct finite model and its source cost

Define

\[
 P_3(s)=\kappa(1)s+C_3(1)s^3,\qquad
 R_3(s,x)=\kappa(c)s+C_3(c)s^3,
 \quad c=x_1^Tx/d.
\]

The compact model is the scalar autonomous system

\[
 \dot\sigma=2[y-P_3(\sigma)],\qquad \sigma(0)=0,
 \qquad f_{\rm cubic}(t,x)=R_3(\sigma(t),x).
 \tag{16}
\]

Its training decoder agrees exactly with its feedback:
\(R_3(s,x_1)=P_3(s)\). Since \(P_3'\ge\kappa(1)>0\), (16) is
gradient flow of its own squared training loss with scalar mobility
\(1/P_3'(\sigma)\). The unique scalar equilibrium attracts either
sign of label, and \(|\sigma(t)|\le |y|/\kappa(1)\). Thus this is a
defined, restartable, directly initialized model, with a full-sphere
decoder and an explicit optimizer. It does not use physical-time playback.

All decoder coefficients are computable directly from (6)--(8). One
conservative implementation is streamed two-dimensional Gaussian
quadrature. For target absolute precision \(\eta\), truncate each
standard Gaussian coordinate at
\(R=O(\sqrt{\log(1/\eta)})\). The Gaussian tail error is
\(O(\eta)\), since all integrands are bounded. On the square, the
integrand and its first derivatives have fixed bounds; a midpoint mesh
of spacing \(O(\eta/R^2)\) has error \(O(\eta)\) and uses
\(O(\eta^{-2}\log^3(1/\eta))\) points, visited one at a time.

For a fully conservative treatment of nearly degenerate covariance,
compute upstream covariance entries to precision \(O(\eta^2)\) and
clip their correlation to its valid interval. Use

\[
 Z=\sqrt{(q+p)/2}\,G_1+\sqrt{(q-p)/2}\,G_2,\qquad
 Z_x=\sqrt{(q+p)/2}\,G_1-\sqrt{(q-p)/2}\,G_2.
\]

The inequality \(|\sqrt a-\sqrt b|\le\sqrt{|a-b|}\) for
nonnegative \(a,b\), followed by the bounded first derivatives of the
integrands, controls the resulting error by \(O(\eta)\). This gives
the explicit conservative source/evaluation cost

\[
 O(\eta^{-4}\log^3(1/\eta))
\]

elementary-function evaluations for the fixed finite collection of
integrals. Storage is a fixed number of accumulators and counters with
\(O(\log(1/\eta))\) bits, plus the input vector and scalar state.
Elementary functions are evaluated to enough extra bits to make the sum
of per-operation roundoff errors \(O(\eta)\); the number of extra bits
is logarithmic in the displayed operation count. These are finite
law-integral calculations, not Gaussian neuron generation or evaluation
of an unknown population response.

At \(\eta=n^{-1/2}\), this elementary implementation uses
\(O(n^2\log^3n)\) evaluations and \(O(\log n)\) scalar precision.
That is an expensive computation, but its stored size does not hide a
dense network. Positivity and training compatibility can be retained by
using the same rounded training coefficients in the feedback and decoder;
sufficiently small coefficient errors keep \(P_3'\ge\kappa(1)/2\).
The scalar contraction estimate then bounds the numerical-coefficient
error uniformly in physical time on the fixed label range. No claim is
made that this removes the cubic model's truncation error.

The proved approximation assertion is (10), for its first two response
coefficients. At fixed nonzero label, (10) says nothing by itself about
the fifth and higher terms of the dense response. Consequently (16) is a
nontrivial direct model, but not a solution of the original accuracy goal.

## 5. A deterministic analytic-bound route fails already at order five

One tempting continuation is to combine the width-independent real
feature-flow bounds with analyticity of \(\tanh\) and conclude a
width-independent Taylor or Gevrey bound. The following explicit example
disproves that inference, even with zero readout and a nondegenerate
initial training kernel.

Fix \(u_0>0\), and take the initial training preactivations all equal to
\(u_0\). Put \(h_0=\phi(u_0)\), and initialize every row of \(W\)
identically by

\[
 W_{i1}=n^{-1/2}+n^{-1},\qquad
 W_{ij}=n^{-1}\quad(j>1),\qquad w_i=0.
 \tag{17}
\]

This is a deterministic configuration, not a typical Gaussian draw. Its
operator norm is at most two, since
\(W=n^{-1/2}{\boldsymbol 1}a^T\) with
\(a=e_1+n^{-1/2}{\boldsymbol 1}\) and
\(\|a\|_2^2=2+2/\sqrt n\). Its initial second preactivations all
equal
\(v_n=(1+n^{-1/2})h_0\), so its initial training kernel stays bounded
away from zero.

The feature flow preserves identical rows and identical readout
coordinates. Write their common readout as \(\omega\), their common
second preactivation as \(v\), the first training preactivation as
\(U\), and the common remaining preactivation as \(V\). Scale the
two types of row weights as \(a_1=nW_{i1}\), \(a_2=nW_{ij}\), and
put \(\eta=\omega\phi'(v)\). Equations (1) reduce exactly to

\[
 \begin{aligned}
 \omega'&=\phi(v),&
 a_1'&=\eta\phi(U),&a_2'&=\eta\phi(V),\\
 U'&=a_1\phi'(U)\eta,&
 V'&=a_2\phi'(V)\eta,&
 v&=\frac{a_1\phi(U)+(n-1)a_2\phi(V)}n.
 \end{aligned}
 \tag{18}
\]

Initially \(U=V=u_0\), \(a_1=\sqrt n+1\), \(a_2=1\), and
\(\eta=0\). Define

\[
 B_n(s)=\frac{\phi(U)^2+(n-1)\phi(V)^2}{n}
 +\frac{a_1^2\phi'(U)^2+(n-1)a_2^2\phi'(V)^2}{n}.
\]

Then \(v'=B_n\eta\). Put \(b_n=\phi(v_n)\phi'(v_n)\).
At zero feature time,
\(\eta'=b_n\),
\(U''=\phi'(u_0)(\sqrt n+1)b_n\),
\(V''=\phi'(u_0)b_n\), and
\(a_1''=a_2''=b_nh_0\).
Differentiating the displayed formula for \(B_n\) therefore gives
the exact expression

\[
 \begin{aligned}
 B_n''(0)={}&4h_0\phi'(u_0)^2b_n(1+n^{-1/2})\\
 &+2\phi'(u_0)^2\phi''(u_0)b_n
        (\sqrt n+4+3n^{-1/2}).
 \end{aligned}
 \tag{19}
\]

For example, the growing term comes from
\(n^{-1}\sum_i a_i^3\), which equals
\(\sqrt n+4+3n^{-1/2}\). Both \(B_n(0)\) and \(v''(0)\) are
bounded uniformly in \(n\). Since \(B_n'(0)=0\), differentiating
\(v'=B_n\eta\) three more times gives

\[
 v^{(4)}(0)=3B_n''(0)b_n+O(1).
\]

The remainder is uniform: its only additional term is
\(B_n(0)\eta'''(0)\), where
\(\eta'''(0)
 =[\phi'(v_n)^2+3\phi(v_n)\phi''(v_n)]v''(0)\).
If \(g=\phi(v)\), then
\(g^{(4)}(0)=3\phi'(v_n)b_nB_n''(0)+O(1)\).
The exact prediction is \(F_n=\omega g\) with \(\omega'=g\).
Its fifth Taylor coefficient is therefore

\[
 [s^5]F_n(s)=\frac{g(0)g^{(4)}(0)}{20}
                  +\frac{g''(0)^2}{12}.
\]

Combining these expressions yields

\[
 \frac{[s^5]F_n(s)}{\sqrt n}
 \longrightarrow
 \frac3{10}\phi'(u_0)^2\phi''(u_0)
       [\phi(h_0)\phi'(h_0)]^3\ne0.
 \tag{20}
\]

The limit is nonzero because \(u_0>0\), \(\phi''(u_0)<0\), and
the other factors are positive. Thus neither a uniform analytic bound nor
any fixed-order Gevrey bound can hold on the entire deterministic set
defined only by bounded initial \(\|W\|_{\rm op}\), bounded hidden
activations, zero readout, and a nondegenerate initial training kernel.
Those are exactly the norm conditions used in the earlier deterministic
small-label localization.

This example does not refute a high-probability bound for Gaussian
initialization: its aligned configuration can be excluded by additional
probabilistic conditions. It shows precisely that a proof needs new
control of concentrated backward coordinates and their nonlinear
products, beyond the established operator-norm and RMS bounds. It also
shows why replacing those products by functions of a few bounded norms
would lose essential information.

## 6. The remaining constructive obligation

The cubic calculation supplies a finite law-generation rule only through
degree three. To use truncation order \(K=O(\log n)\), the route still
requires all of the following in one compatible theorem:

- A coefficient-generation recurrence using only the initialization law
  and data, with specified finite computation and polynomial-in-\(K\)
  storage, including the decoder's dependence on \(c\).
- A geometric truncation bound on a fixed feature interval large enough
  for the fixed nonzero label. The bound must control all generated high
  orders and their feedback, not just every fixed-order coefficient.
- A simultaneous whole-sphere finite-width comparison at order
  \(n^{-1/2}\), together with the derivative control needed to preserve
  the scalar feedback's monotonicity.

The first two items are not supplied by repeatedly applying (11). That
operation correctly generates contractions at a fixed low order, but it
does not bound the growing family of contractions, their source cost, or
the remainder. Equation (20) proves that the existing deterministic bounds
cannot supply the missing estimate.

A Gevrey derivative estimate of order \(r>1\) would not by itself repair
the Taylor route. A bound
\(\sup|F^{(k)}|\le A B^k(k!)^r\) only gives the Taylor remainder
estimate

\[
 A(BS)^{K+1}((K+1)!)^{r-1}
\]

on a fixed interval \(|s|\le S\); it eventually increases with
\(K\). Obtaining arbitrary precision from such regularity would require
a different approximation and a lawful way to compute its coefficients.
In particular, evaluating an unknown response at quadrature nodes would
reintroduce the forbidden response oracle. Analytic regularity with a
controlled radius, or another constructive summation theorem, remains an
unproved requirement.

The exact scalar stability reduction from `ANALYTIC_ROUTE.md` would
propagate a valid response approximation uniformly in physical time and
to the endpoint. This attempt improves the directly computable decoder
and identifies a concrete failure of the current high-order proof route;
it does not replace the missing approximation theorem with that stability
result.

## Author check

This is an internal check, not independent review. The frozen hash is
reported separately after the final edit.

- The finite test-input relation carries the factor \(c=x_1^Tx/d\)
  only in the first-layer-motion contribution, producing exactly the
  final factor \(c/2\) in (5) and (8).
- The training decoder at \(c=1\) reduces to the previously checked
  positive cubic coefficient and agrees exactly with scalar feedback.
- Gaussian contractions keep the dependence of \(W\) and its initial
  activations. Equal-row terms, unequal-row terms, and the
  \(O(n^{-1})\) correction are displayed in (12).
- No inverse covariance is used, so the formula and its pointwise
  coefficient bound include the degenerate endpoint inputs.
- The rate (10) is explicitly pointwise in the input. No simultaneous
  sphere comparison or high-order remainder is inferred from it.
- The direct cubic model has an actual law-based coefficient algorithm,
  stated arithmetic cost, bounded working storage, and a compatible
  optimizer. Its nonvanishing truncation uncertainty remains visible.
- The rank-one example has bounded operator norm, zero initial readout,
  and nonzero initial training kernel. Its order-five divergence is an
  exact deterministic calculation, not a claim about typical Gaussian
  samples.
- The fixed label is never replaced by a label tending to zero with
  width. No dense realization is needed by the constructed cubic model;
  dense arrays appear only as mathematical reference variables in the
  proof of its low-order coefficients.
