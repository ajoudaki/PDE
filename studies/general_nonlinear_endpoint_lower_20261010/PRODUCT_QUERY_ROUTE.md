# Product-query route: centered scalar stability and its limits

2026-10-10. Scoped theoretical derivation; no experiment. This note uses only
`paper/compact.tex`, `paper/compact_fitting.tex`, this study's
`POSITIVE_ROUTE.md`, and the explicitly assigned
`studies/integrated_general_compression_20261004/TANH_ENDPOINT_VARIABILITY_LOWER.md`.
The canonical-notation skill, its neural-network reference, rigorous-math
skill, and conjecture/audit instructions were applied. This is an internally
derived partial result, not an established endpoint lower theorem.

The useful conclusion is that **bounded second-layer activations admit a
centered scalar perturbation bound for arbitrary noncentered first-layer
features**. It does not require a label cap involving a small nonlinear
Hermite coefficient. Extending this conclusion to unbounded second-layer
activations requires a readout moment estimate not supplied by the assigned
fitting theorem. A uniform small perturbation estimate for the complete
centered feature vector is false, even for bounded analytic activations.

## 1. Canonical setup and the exact scalar estimate

There are two hidden layers. Write their matrices as
\(A=W^{(1)}\in\mathbb R^{n\times d}\) and
\(W=W^{(2)}\in\mathbb R^{n\times n}\), and write the readout as
\(w\in\mathbb R^n\). The forward map, loss, and canonical equations are

\[
 h_a=\phi_1(Av_a),\quad g_a=\phi_2(Wh_a),\quad
 f_n(t,v_a)=n^{-1}w^\top g_a,\quad r_a=f_n(t,v_a)-y_a,
 \qquad \mathcal L=m^{-1}\sum_a r_a^2,
\]
\[
 \dot w=-\frac2m\sum_a r_ag_a,\qquad
 \dot W=-\frac2{nm}\sum_a r_a
       [w\odot\phi_2'(Wh_a)]h_a^\top,
\]
\[
 \dot A=-\frac2m\sum_a r_a
 [\phi_1'(Av_a)\odot W^\top(w\odot\phi_2'(Wh_a))]v_a^\top.
\]

Initialization and all normalizations are those of `paper/compact.tex`.
Let \(S=\operatorname{span}\{v_a\}\) be proper, and let \(v\) be a fixed
unit vector in \(S^\perp\). The first equation for \(A\) gives
\(A(t)v=A_0v\). Conditional on the active training initialization,

\[
 Z=A_0v\sim N(0,I_n),\qquad H_j=\phi_1(Z_j),\qquad
 f_n(\infty,v)=n^{-1}w_\infty^\top\phi_2(W_\infty H).
\]

The fitting event is taken in the reduced input space \(S\), so it does
not condition on \(Z\). Define
\(\mu=\mathbb EH_1\) and \(\sigma^2=\operatorname{Var}(H_1)\).
Lipschitz growth of \(\phi_1\) gives their finiteness. Put

\[
 b_1=\sup_{x\in\mathbb R}|\phi_1'(x)|,\quad
 b_2=\sup_{x\in\mathbb R}|\phi_2'(x)|,\quad
 b_{22}=\sup_{x\in\mathbb R}|\phi_2''(x)|.
\]

All are finite under the strip assumptions. In the next calculation
\(W_0,E,w\) are any deterministic matrices/vector of the stated shapes.
Let

\[
 F(Z)=\frac1n w^\top
 [\phi_2((W_0+E)H)-\phi_2(W_0H)].
\]

Write \(u=W_0H\), \(d=EH\), and let activations and derivatives act
coordinatewise. The chain rule gives exactly

\[
 \nabla_ZF=\frac1n\operatorname{diag}(\phi_1'(Z))
 \left\{E^\top\operatorname{diag}(\phi_2'(u+d))w
 +W_0^\top\operatorname{diag}(w)
                  [\phi_2'(u+d)-\phi_2'(u)]\right\}.
\]

The squared norm of a sum is at most twice the sum of its squared norms.
The mean-value theorem bounds the bracketed derivative difference in
coordinate \(i\) by \(b_{22}|d_i|\). Independence of the \(H_j\) gives

\[
 \mathbb E\|\operatorname{diag}(w)EH\|^2
 =\sigma^2\sum_i w_i^2\|E_i\|^2
   +\mu^2\sum_i w_i^2(E_i\mathbf1)^2,
 \tag{1}
\]

where \(E_i\) is row \(i\). Gaussian Poincare therefore gives the exact
upper bound

\[
 \operatorname{Var}_ZF\le\frac{2b_1^2}{n^2}\left[
 b_2^2\|E\|_{\rm op}^2\|w\|^2
 +\|W_0\|_{\rm op}^2b_{22}^2
 \left\{\sigma^2\sum_iw_i^2\|E_i\|^2
       +\mu^2\sum_iw_i^2(E_i\mathbf1)^2\right\}\right].
 \tag{2}
\]

Poincare here means \(\operatorname{Var}F\le\mathbb E\|\nabla F\|^2\).
It follows by expanding a smooth square-integrable function in orthonormal
Gaussian Hermites: the variance weights each positive-degree coefficient
by one and the gradient energy weights it by its degree. Truncation and
smooth approximation apply here because bounded derivatives give at most
linear growth for the functions and the displayed gradients have finite
second moments. Thus no integrability hypothesis is implicit in (2).

Using \(\|E\mathbf1\|^2\le n\|E\|_F^2\) in (1) yields a convenient
consequence:

\[
 \operatorname{Var}_ZF\le
 \frac{2b_1^2\|E\|_F^2}{n}
 \left[b_2^2\frac{\|w\|^2}{n}
 +\|W_0\|_{\rm op}^2b_{22}^2\|w\|_\infty^2
                      \left(\mu^2+\frac{\sigma^2}{n}\right)\right].
 \tag{3}
\]

The mean of \(F\) is unrestricted. Equations (2)--(3) bound its centered
Gaussian \(L^2\) norm, which is the relevant norm for a conditional
variance comparison.

### Bounded second activation

Assume additionally \(B_2=\sup_{x\in\mathbb R}|\phi_2(x)|<\infty\).
Let \(\lambda=\gamma/m\) and \(Y=\|y\|/\sqrt m\), as in the paper.
Its fitting theorem gives
\(\rho(t)=\|r(t)\|/\sqrt m\le Ye^{-\lambda t/2}\). Directly from the
readout equation and sample Cauchy--Schwarz,

\[
 |\dot w_i(t)|\le2B_2\rho(t),\qquad
 \sup_t\|w(t)\|_\infty\le\frac{4B_2Y}{\lambda}.
 \tag{4}
\]

This coordinate estimate is deterministic on the fitting event; it makes
no trained-coordinate independence assertion. The same event supplies

\[
 \frac{\|w_\infty\|^2}{n}\le\frac{4Y^2}{\lambda},\quad
 \|W_0\|_{\rm op}\le8,\quad
 \|W_\infty-W_0\|_F\le
                 \frac{8U_2Y^2}{\lambda^{3/2}},
\]

where \(U_2=2Hs\), with \(H,s\) exactly as in the fitting proof.
Substitution into (3) proves

\[
 \operatorname{Var}_Z\!\left[
 \frac1n w_\infty^\top
 \{\phi_2(W_\infty H)-\phi_2(W_0H)\}\right]
 \le\frac{128b_1^2U_2^2Y^6}{n\lambda^3}
 \left[\frac{4b_2^2}{\lambda}
 +\frac{1024b_{22}^2B_2^2}{\lambda^2}
            \left(\mu^2+\frac{\sigma^2}{n}\right)\right].
 \tag{5}
\]

In particular, for fixed data and activations, the centered root-mean-square
error is \(O(Y^3/\sqrt n)\), with the displayed gap factors. This uses
only the existing fitting cap; it introduces no Hermite-tail-dependent
small-label condition. Equation (5) covers bounded outer activations such
as tanh, arctan and sigmoid, with noncentered and potentially unbounded
first-layer activations. It alone does not establish that its constant is
small relative to the desired random-feature fluctuation under every
admissible data condition.

A changed readout is easier to handle after centering: for any
\(a\in\mathbb R^n\), the same Poincare argument gives

\[
 \operatorname{Var}_Z[n^{-1}a^\top\phi_2(W_0H)]
 \le b_1^2b_2^2\|W_0\|_{\rm op}^2\|a\|^2/n^2.
 \tag{6}
\]

Consequently a separate \(O(Y^3\sqrt n)\) readout comparison would give
another centered \(O(Y^3/\sqrt n)\) error. This note does not assume or
prove that comparison, nor a nonzero random-feature endpoint fluctuation
for arbitrary noncentered activations.

## 2. The whole-feature estimate fails after centering

The defect is not merely an uncontrolled deterministic mean. Take
\(\phi_1(z)=1+\tanh z\), \(\phi_2(z)=\tanh z\), and let
\(W_0\) have independent \(N(0,1/n)\) entries. Fix any nonzero scalar
\(a\), as small as desired, and set

\[
 E=\frac an\mathbf1\mathbf1^\top,\qquad
 \|E\|_F=\|E\|_{\rm op}=|a|.
\]

Let \(D(H)=\tanh((W_0+E)H)-\tanh(W_0H)\). Then

\[
 \frac1n\mathbb E_H\|D(H)-\mathbb E_HD(H)\|^2
 \xrightarrow{\mathbb P}_{W_0} c_a>0.
 \tag{7}
\]

Here is a direct proof. Let \(H'\) be an independent copy of \(H\).
The variance identity expresses the left side as the average over rows
of \(\frac12\mathbb E_{H,H'}(D_i(H)-D_i(H'))^2\). These row quantities
are independent identically distributed functions of Gaussian rows, and
are bounded by eight, since each activation difference has magnitude at
most two. Their average minus their expectation tends to zero in
probability by the variance bound \(64/n\).

Conditional on \(H,H'\), the pair
\((W_{0,i}H,W_{0,i}H')\) is centered Gaussian with variances
\(\|H\|^2/n,\|H'\|^2/n\) and covariance \(H^\top H'/n\). The law
of large numbers sends these to \(q,q,1\), where
\(q=1+\operatorname{Var}(\tanh Z_1)>1\), and sends both coordinates
of \(EH,EH'\) to \(a\). Continuity of Gaussian expectations in their
covariance matrix and bounded convergence therefore identify the limit as

\[
 c_a=\frac12\mathbb E[g_a(U)-g_a(V)]^2,
 \qquad g_a(x)=\tanh(x+a)-\tanh x,
\]

where \((U,V)\) is Gaussian with covariance
\(\begin{pmatrix}q&1\\1&q\end{pmatrix}\). This matrix is positive
definite. If \(c_a=0\), its everywhere-positive density and continuity
would force \(g_a(u)=g_a(v)\) for all real \(u,v\). But \(g_a\) tends
to zero at infinity and \(g_a(0)=\tanh a\ne0\), a contradiction.
This proves (7).

Thus a Frobenius perturbation of fixed arbitrarily small size can produce
centered total feature energy of order \(n\). It cannot be bounded by a
constant times \(\|E\|_F^2\), uniformly in width. This is a counterexample
to that proposed perturbation lemma, **not** a counterexample for the
actual trained endpoint: the displayed \(E\) was not asserted reachable
by canonical training. The scalar bound (3) remains valid for this example.

## 3. What remains for unbounded second activations

For softplus, GELU, SiLU, and the full permitted strip-analytic class,
the coordinate bound (4) cannot be obtained by inserting a finite \(B_2\).
The fitting theorem controls \(\|w\|^2/n\); it does not supply
\(\|w\|_\infty\) or a fourth empirical moment of the readout along the
whole trajectory. Replacing \(\|w\|_\infty\) in (3) by \(\|w\|\)
loses one power of \(n\), so it does not prove the required fluctuation
scale.

The precise unresolved quantity is exposed by (1):
\(\sum_iw_i^2(E_i\mathbf1)^2\), together with its centered-input
analogue \(\sum_iw_i^2\|E_i\|^2\). The canonical row update does help
identify a sufficient moment condition. On the fitting event the first-layer
training features have norm at most \(2H\sqrt n\), so

\[
 \|\dot W_i(t)\|\le
 \frac{4Hb_2}{\sqrt n}\rho(t)|w_i(t)|.
\]

Writing \(M_i=\sup_{t\ge0}|w_i(t)|\), integration gives

\[
 \|E_i\|\le\frac{8Hb_2Y}{\lambda\sqrt n}M_i,
 \qquad |E_i\mathbf1|\le\frac{8Hb_2Y}{\lambda}M_i.
 \tag{8}
\]

Hence the weighted quantity in (1) is bounded by

\[
 \left(\frac{8Hb_2Y}{\lambda}\right)^2
 \left(\mu^2+\frac{\sigma^2}{n}\right)\sum_iM_i^4.
 \tag{9}
\]

A width-uniform estimate
\(n^{-1}\sum_iM_i^4\le C Y^4\), with its actual data factors stated,
would therefore restore an \(O(Y^6/n)\) variance bound in (2).
Equation (9) is conditional on that estimate; it is not a proof of it.
Neither Frobenius displacement nor global readout energy implies this
fourth-moment statement. Treating trained coordinates as independent
Gaussians would not be legitimate.

## 4. Claim status

Proved here: the deterministic scalar covariance estimate (2), its bounded
outer-activation consequence (5), the readout perturbation estimate (6),
the obstruction (7), and the sufficient weighted-moment reduction (9).

Open here: a sufficiently strong endpoint random-feature comparison and
nondegenerate random-feature fluctuation for general noncentered
activations; a trajectory fourth-moment estimate for unbounded outer
activations; and the full two-layer endpoint theorem requested by the
supervisor. No extra activation-tail-dependent label cap has been imposed,
and no trained matrix or query law has been silently replaced by a
Gaussian surrogate.
