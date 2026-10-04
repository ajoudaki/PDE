# Audit of the gated initial/current overlap model

2026-09-30. Scoped algebraic and theoretical audit, before testing this
candidate. No code or training was run for this audit. Inputs were the
supervisor's frozen equations, the existing kernel/cubic route, and the
preceding bounded-Gram construction. This is an internal result, not an
independent promotion review or established material.

**Verdict:** the proposed equations have the claimed positive kernel,
energy identity, gated feature bounds, and exact training aliases. Both
the gated and ungated variants are globally well posed. The training cubic
response survives. The arbitrary-query cubic projection defect remains
and must be reported explicitly. Retaining the initial/current overlap
does recover information missing from the previous current-Gram closure;
its effectiveness on dense trajectories remains an empirical question.

## Frozen equations and algebra

Let `alpha=2/m`, `K0` be positive definite with diagonal below one, and
`S0[(a,e),(c,f)]` the fixed positive response Gram. Evolve
`R in R^(m x m)` and `w in R^m`, starting from `R=I`, `w=0`. Set

\[
K=R^TK_0R,\quad f=R^TK_0w,\quad r=f-y,\quad
g_a=\frac{1-K_{aa}}{1-K_{0,aa}},
\]

\[
T_{ea}=-\alpha g_a\sum_{cf}r_c g_c w_f S_0[(a,e),(c,f)],
\qquad \dot R=K_0^{-1}T,\qquad \dot w=-\alpha Rr.        \tag{1}
\]

Define

\[
N_{ac}=g_ag_c\sum_{ef}w_ew_fS_0[(a,e),(c,f)].
\]

This is positive semidefinite: its quadratic form is the quadratic form
of `S0` on the paired-index vector `b_a g_a w_e`. Direct differentiation
then gives

\[
\dot f=T^Tw-\alpha Kr=-\alpha(K+N)r,\qquad
\frac{d}{dt}\frac{\|r\|^2}{m}
=-\frac4{m^2}r^T(K+N)r\le0.                            \tag{2}
\]

For `q=w^T K0 w`,

\[
\dot q=2w^TK_0\dot w=-2\alpha r^Tf.                    \tag{3}
\]

The energy identity is exact for the surrogate, and matches the dense
identity's form. It does not assert equality of their energy trajectories.
No inverse of the evolving `R` or `K` is needed. **The matrix `R` may lose
rank, so `K` is guaranteed positive semidefinite, not positive definite.**
Any implementation should preserve this distinction.

The feature diagonal obeys `Kdot_aa=2 R[:,a]^T T[:,a]`. This contains
`g_a`, so `1-Kaa` solves a homogeneous scalar linear equation and remains
positive at every finite time of existence. All derivatives vanish at
zero residual. Neither positivity nor stopping guarantees that every
label vector will be fitted.

## Passive query geometry

Initialize

\[
b_{0,x}=K_0^{-1}k_{0,x},\qquad
d_{0,x}=\kappa_{0,x}-k_{0,x}^TK_0^{-1}k_{0,x}\ge0.
\]

Use

\[
\kappa_x=d_{0,x}+b_x^TK_0b_x,\quad
g_x=\frac{1-\kappa_x}{1-\kappa_{0,x}},\quad
(T_x)_e=-\alpha g_x\sum_{cf}r_cg_cw_f S_0[(x,e),(c,f)],
\]

\[
\dot b_x=K_0^{-1}T_x,\qquad \widehat f_x=b_x^TK_0w.      \tag{4}
\]

The initial inequality for `d0` is the initial feature Gram's Schur
inequality. Its small numerical violations require a declared tolerance;
they are not grounds for silently changing the model.

Since `kappa_dot=2 b_x^T T_x` contains `g_x`, the query diagonal also stays
below one. Cauchy--Schwarz in the fixed `K0` metric gives the stronger bound

\[
|\widehat f_x|^2\le q(\kappa_x-d_{0,x})\le q.            \tag{5}
\]

All-query positive Gram geometry is realizable: retain the fixed initial
orthogonal feature remainders, whose joint covariance is the initial Schur
kernel, and change only the coefficients `b_x` in the initial training
span. This argument does not require storing the orthogonal fields.

At a training alias `x=u_a`, `b0=e_a`, `d0=0`, and the query response
slice is the corresponding training slice. Equation (4) is exactly the
equation for column `a` of `R`. Therefore `b_x=R[:,a]` and
`fhat_x=f_a` for all time. The training state has `m^2+m` scalars, and
each query has `m` passive evolving scalars plus fixed initialization
coefficients. This remains a separately initialized query construction,
not a fixed-state decoder of the complete input function.

## Global existence for both variants

For either the gated equations or the otherwise identical choice `g=1`,
equation (2) gives `||r||<=||y||` and `||f||<=2||y||`. Consequently

\[
|\dot q|\le4\alpha\|y\|^2,\qquad
\lambda_{\min}(K_0)\|w\|^2\le q\le4\alpha\|y\|^2t.    \tag{6}
\]

Thus `w` is bounded on every finite interval. For the ungated model,
`Rdot` and every `bdot_x` are bounded by a fixed coefficient times
`||r|| ||w||`, which excludes finite-time escape. For the gated model,
the feature-diagonal bounds give finite bounds on the columns of `R`;
the gates are then bounded by their fixed initial inverse slacks. These
bounds and (6) keep the coefficients in the slack equations finite, so
no slack can first reach zero at finite time. The same argument bounds
each query coefficient vector through its diagonal. This proves global
existence without an assumption that `R` remains invertible.

## Local response and the retained information

In the original small-label expansion, let `z`, `J`, and `M` denote the
original residual integrals and quadratic feature cross Gram. Then

\[
w=-\alpha z+O(a^3),\qquad
R=I+K_0^{-1}M+O(a^4),\qquad
K=K_0+M+M^T+O(a^4),\qquad g=1+O(a^2).                 \tag{7}
\]

Substituting in (2) reproduces the original training kernel through
quadratic response and hence the training output through cubic response.
The gated and ungated versions agree at that order. This audit establishes
the local expansion, not a new all-time approximation theorem.

The retained matrix has a specific interpretation. If the current
features are represented by `H0 R`, their initial/current overlap is
`Gamma=K0 R`; their current/current Gram is `R^T K0 R`. These are different
objects. A current Gram alone does not determine `Gamma`: transformations
`R -> O R` with `O^T K0 O=K0` preserve the former and generally change the
latter. At quadratic response, `Gamma=K0+M`, while the current Gram sees
only `K0+M+M^T`. The new state retains the nonsymmetric response information.

The readout coefficients `w` also describe the readout in a fixed initial
feature frame. Reconstructing them as `K0^-1 f`, as in the earlier closure,
ignores the intervening overlap `Gamma`. That replacement is correct only
to leading order. Keeping `R` and evolving `w` removes this extra closure
assumption, including the old response amplification through `A=K K0^-1`.
This is a justified information repair; it is not a proof that its
strong-response predictions match the dense network.

## Surviving query defect and approximation status

The readout is still restricted to the initial training-feature span.
Define

\[
E_{x;acf}=S_0[(a,x),(c,f)]
-\sum_e(k_{0,x}^TK_0^{-1})_eS_0[(a,e),(c,f)].
\]

With the original third response integral `P_a;cf=integral r_a J_cf`,

\[
\widehat f_x-f_{\rm cub}(x)
=\alpha^3\sum_{acf}P_{a;cf}E_{x;acf}+O(a^5).            \tag{8}
\]

This is the same explicit arbitrary-query cubic defect as the previous
bounded-Gram candidate. It vanishes on training aliases and need not
vanish elsewhere. The fixed orthogonal feature remainder contributes to
`d0` but carries no readout component; the stronger bound in (5) also
exhibits this modeling restriction.

Finally, replacing current activation derivatives by the scalar mean-slack
factors `g` is a closure assumption. Tanh's pointwise derivative identity
motivates the available slack, but does not make this factorization of
the derivative correlations exact. The frozen response tensor also omits
later changes in the neural derivative fields. Matched gated/ungated
experiments can test the value of the scalar boundary feedback; they do
not validate these remaining closures or remove defect (8).
