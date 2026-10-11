# A first-feature endpoint gap for any number of active orthogonal samples

Status: candidate strengthening for independent internal checking,
2026-10-11. It concerns the scalar-ascent reference in
GAUSSIAN_POSITIVE_GEOMETRY.md. It is not a new arbitrary-data population
construction.

## Statement

Take any fixed number \(k\ge1\) of orthonormal unit inputs, canonical
Gaussian hidden initialization, two hidden tanh layers, and exact zero
readout. On the globally constructed scalar-ascent population path for
\(g=k^{-1}\sum_{a=1}^k f_a\), its first-feature covariance
\[
 Q(s)=\mathbb E[u(s)u(s)^\top]
\]
is positive definite at every finite feature time \(s\).
Consequently it is positive definite at the finite endpoint \(s_*\)
where the common prediction first reaches any prescribed \(a>0\).

This supplies the common-mode gap missing from the elementary argument
for \(k\ge3\). It does **not** use the false implication that
\(\sum_a u_a=0\) forces \(\sum_a\tanh(Wu_a)=0\).

## 1. Finite scalar ascent and uniform conditional moments

Use the notation and parameter normalization of
ZERO_LABEL_EXTENSION_RESULT.md. At finite width, scalar ascent means
the metric gradient flow of \(g\), not training the squared loss:
\[
 w'=\frac1k\sum_a h_a,\qquad
 W'=\frac1{kn}\sum_a b_a u_a^\top,\qquad
 \xi_a'=\frac1k B_a,\qquad
 \xi_a=\zeta(Ax_a),\quad u_a=\psi(\xi_a),
 \tag{1}
\]
where \(\zeta(z)=z/2+\sinh(2z)/4\) and
\(\psi=\tanh\circ\zeta^{-1}\). The variables \(b_a=w(1-h_a^2)\),
\(B_a=W^\top b_a\) retain their earlier meanings.
The physical population reference is a time change of this ascent;
the finite-width physical flow need not be.

For each fixed \(S<\infty\),
\[
 \|w(s)\|_\infty\le s,\qquad
 \|W(s)-W_0\|_F\le s^2/2,\qquad
 \|W(s)\|_{\rm op}\le\|W_0\|_{\rm op}+s^2/2.
 \tag{2}
\]
The natural-coordinate vector field is locally Lipschitz in its
mean-square/Frobenius state, uniformly in width on these bounded sets.
In particular these scalar-ascent flows exist through \(S\).

We claim that for all sufficiently large \(n\),
\[
 \sup_{\substack{\text{all fixed first-layer roots}\\
                 a,j,\ 0\le s\le S}}
 \mathbb E_{W_0}|B_{a,j}(s)|^2\le C_S<\infty.
 \tag{3}
\]
Constants may depend on \(k,S\), but not on the conditioned roots.
Here and below a subscript on a constant indicates its allowed
dependence, not an optimized order parameter.

For precision, the variational argument establishing (3) is the one in
Section 3 of GAUSSIAN_NONORTHOGONAL_EXTENSION.md, with the bounded
residual coefficients replaced by \(1/k\); no loss-feedback derivatives
are then present. Write \(W_0=Q_0/\sqrt n\) and
\(V=W-W_0\). For a perturbation \(\Delta Q_0\), let
\((\eta,v,E)\) be the resulting derivatives of \((\xi,w,V)\), and set
\[
 R=\|\eta\|_F+\|v\|_2+\sqrt n\|E\|_F,\qquad
 F_U=\|(\Delta Q_0/\sqrt n)U\|_F,\qquad
 F_b=\|(\Delta Q_0^\top/\sqrt n)b\|_F.
\]
All variational initial conditions are zero because the first roots
are conditioned and fixed. Since \(|\psi'|\le1\), \(|u_a|\le1\),
\(|w|\le S\) and \(|\tanh'|,|\tanh''|\le2\), expansion of the
forward, backward and rank-one equations gives
\[
 D^+R\le C_S(1+\|W_0\|_{\rm op}^2)R+
 C_S(1+\|W_0\|_{\rm op})(F_U+F_b).                   \tag{4}
\]
For arbitrary \(\Delta Q_0\),
\(F_U+F_b\le C_S\|\Delta Q_0\|_F\).
For a single-entry perturbation, the direct products have only one
nonzero row or column, and their entries are bounded; hence
\(F_U+F_b\le C_S/\sqrt n\).
Gronwall and the differentiated forward/backward equations give
\[
 \|\delta B\|_F+\|\delta b\|_F
 \le C_S e^{C_S\|W_0\|_{\rm op}^2}\|\Delta Q_0\|_F,
 \quad
 \left\|\frac{\partial b}{\partial(Q_0)_{ij}}\right\|_F
 \le \frac{C_S e^{C_S\|W_0\|_{\rm op}^2}}{\sqrt n}.
 \tag{5}
\]
These bounds contain no magnitude of the conditioned natural roots.

The Gaussian operator-norm tail, obtained by the two-sphere net
argument, implies
\(\mathbb E e^{C\|W_0\|_{\rm op}^2}\le C'\) uniformly over all
sufficiently large widths, for each fixed \(C\).
Gaussian integration by parts therefore yields
\[
 \left|\mathbb E\frac1{\sqrt n}\sum_i
        (Q_0)_{ij}b_{a,i}(s)\right|
 =\left|\frac1{\sqrt n}\sum_i
        \mathbb E\frac{\partial b_{a,i}(s)}
                          {\partial(Q_0)_{ij}}\right|
 \le C_S.                                           \tag{6}
\]
The learned part has a deterministic coordinate bound:
\[
 (V(s)^\top b_a(s))_j
 =\frac1k\int_0^s\sum_c u_{c,j}(v)
          \langle b_c(v),b_a(s)\rangle_n\,dv,\qquad
 |(V^\top b_a)_j|\le S^3/2.                          \tag{7}
\]
Thus \(|\mathbb E B_{a,j}|\le C_S\). The first bound in (5) bounds
the Euclidean Gaussian gradient of each scalar \(B_{a,j}\).
Gaussian Poincare and the operator-norm tail give
\(\operatorname{Var}(B_{a,j})\le C_S\).
Together these prove (3). Smooth cutoff and dominated convergence
justify Poincare and integration by parts: (5) is square integrable
at sufficiently large width, while
\(|B_{a,j}|\le S\sqrt n(\|W_0\|_{\rm op}+S^2/2)\).

From (1), conditional Cauchy–Schwarz gives the uniform row bound
\[
 \mathbb E_{W_0}\sum_{a=1}^k
       |\xi_{a,j}(s)-\xi_{a,j}(0)|^2
 \le S^2 C_S/k,\qquad s\le S.                        \tag{8}
\]

## 2. A positive common mode

Choose a finite \(R>1\) so large that
\[
 \zeta(R)-\zeta(1)\ge 2S\sqrt{C_S/k}.
 \tag{9}
\]
For a fixed first neuron \(j\), consider the event
\((Ax_a)_j(0)\ge R\) for all active \(a\).
Its Gaussian probability is
\(p=(1-\Phi(R))^k>0\). Conditional on **every** first-layer root,
(8) and Markov show that with probability at least \(3/4\) no
coordinate of that row moves in \(\xi\) by more than the right side
of (9). On this event all its active features remain at least
\(\tanh(1)\) at the specified time \(s\). Hence
\[
 \mathbb E\left[
     \left(\frac1k\sum_a u_{a,j}(s)\right)^2\right]
 \ge \frac34 p\,\tanh(1)^2.                         \tag{10}
\]
The square is nonnegative off the event, so no cancellation is possible.
Exchangeability gives the same lower bound for the expectation of
the empirical squared common feature.

The scalar-ascent fixed-horizon Gaussian-program theorem in
GAUSSIAN_POSITIVE_GEOMETRY.md applies on \([0,S]\).
The common feature is bounded, so convergence in probability of its
empirical second moment to the deterministic population moment also
implies convergence of expectations. Passing to the limit in (10)
proves that the common eigenvalue of \(Q(s)\) is positive.

## 3. Contrast modes and conclusion

Permutation symmetry makes \(Q(s)\) of the form
\(\alpha(s)I+\beta(s)\mathbf1\mathbf1^\top\).
For \(a\ne b\), equations (1) give
\[
 \|(\xi_a-\xi_b)'(s)\|_2
 \le \frac{2S}{k}
       (\|W_0\|_{\rm op}+S^2/2)^2
       \|\xi_a(s)-\xi_b(s)\|_2                       \tag{11}
\]
on the population operator space, where the initialized operator norm
has its fixed deterministic bound. This uses
\(|\tanh'(\zeta)-\tanh'(\widetilde\zeta)|
 \le2|\zeta-\widetilde\zeta|\) at the top layer and
\(|\psi'|\le1\) at the bottom.
The initially nonzero norm in (11) stays nonzero on every finite
interval by the reverse Gronwall inequality. If
\(u_a=u_b\) almost surely at such a time, injectivity of \(\psi\)
would contradict this fact. Therefore
\(\alpha(s)=\frac12\|u_a(s)-u_b(s)\|_2^2>0\).
Together with (10) this proves \(Q(s)\succ0\).

For \(k=1\) only the common argument is needed.
All estimates permit a fixed but arbitrarily large \(S\), with
constants and sufficient width depending on \(S\). Thus they apply
at the prescribed-amplitude feature endpoint.

If this lemma passes internal checking, the entire proof in
ZERO_LABEL_EXTENSION_RESULT.md extends from \(k\in\{1,2\}\) to any
fixed \(k\ge1\), with this lemma replacing its Section 5 common-mode
argument. No other part of that proof uses \(k\le2\).
