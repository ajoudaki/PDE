# Independent finite-jet algebra check

## Scope and status

This is a scoped, prompt-only algebra derivation. The supplied scientific inputs were the canonical population gradient-flow equations, the zero population readout initialization, the normalization by `sqrt(2)`, the iid Gaussian first-layer initialization, and the requested two-axis/equal-weight specialization. The only process source read was `/etc/codex/skills/solve-math-rigorously/SKILL.md`. No repository scientific source, other study, author history, source audit, numerical experiment, or other review was read or used. The supervisor subsequently supplied a candidate equal-weight simplification, which is checked explicitly below.

The conclusions are finite algebraic/Peano-jet identities for any continuous local strong solution of the stated integral equations. This report does not prove existence of that solution from boundedness of the initialized middle operator alone, convergence of an all-order Taylor series, or an exact finite-dimensional closure at positive time. It is an independent derivation, not a source audit or numerical verification.

## Model and notation

Write `A = W2(0)` and `V = W1(0)`. The initialized middle operator is a bounded map from `L2(Omega1)` to `L2(Omega2)`, and every backward occurrence below is its actual Hilbert-space adjoint. Set

\[
z_a=\frac{Vx_a}{\sqrt2},\qquad h_a=\tanh z_a,\qquad p_a=1-h_a^2,
\]
\[
s_a=Ah_a,\qquad g_a=\tanh s_a,\qquad
D_a=1-g_a^2,\qquad E_a=-2g_aD_a.
\]

Here `h_a,p_a` are lower-population functions; `g_a,D_a,E_a` are upper-population functions. Inner products are population expectations. Products within one population are pointwise. For upper `u` and lower `v`, the rank-one operator convention is

\[
(u\otimes v)q=u\langle v,q\rangle_1.
\]

Define three deterministic Gram matrices:

\[
C_{ab}=\langle h_a,h_b\rangle_1,\qquad
K_{ab}=\langle g_a,g_b\rangle_2,\qquad
G_{ab}=x_a\cdot x_b.
\]

The supplied canonical equations are

\[
\dot W_3=-2\sum_a\omega_ar_aH_{2a},
\]
\[
\dot W_2=-2\sum_a\omega_ar_a
\bigl(W_3\phi'(Z_{2a})\bigr)\otimes H_{1a},
\]
\[
\dot W_1=-2\sum_a\omega_ar_a\phi'(Z_{1a})
W_2^*\bigl(W_3\phi'(Z_{2a})\bigr)\frac{x_a^T}{\sqrt2},
\]

with `phi = tanh`, `r_a = f_a-y_a`, and `W3(0)=0`. No independent replacement for an adjoint field is made.

## Complete jet for general deterministic inputs

Define bounded upper functions and scalar output coefficients by

\[
u=2\sum_a\omega_ay_ag_a,\qquad
m_a=\langle u,g_a\rangle_2,
\]
\[
v=-\sum_a\omega_am_ag_a,\qquad
n_a=\langle v,g_a\rangle_2.
\]

Equivalently,

\[
m_a=2\sum_b\omega_by_bK_{ab},\qquad
n_a=-\sum_b\omega_bm_bK_{ab}.
\]

Set

\[
B=\sum_a\omega_ay_a(uD_a)\otimes h_a,
\qquad
b=\sum_a\omega_ay_ap_aA^*(uD_a)\frac{x_a^T}{\sqrt2}.
\]

Then the first nonconstant weight coefficients are

\[
W_1(t)=V+t^2b+o(t^2),\qquad
W_2(t)=A+t^2B+o(t^2).
\]

The lower hidden coefficient and upper preactivation coefficient are

\[
\eta_a
=\frac12\sum_b\omega_by_bG_{ab}\,
p_ap_bA^*(uD_b),
\qquad
\xi_a=Bh_a+A\eta_a.
\]

Consequently,

\[
H_{1a}(t)=h_a+t^2\eta_a+o(t^2),
\]
\[
Z_{2a}(t)=s_a+t^2\xi_a+o(t^2),\qquad
H_{2a}(t)=g_a+t^2D_a\xi_a+o(t^2).
\]

Finally define

\[
w=\frac23\sum_a\omega_a
\bigl(y_aD_a\xi_a-n_ag_a\bigr).
\]

The readout and residual coefficients are

\[
W_3(t)=tu+t^2v+t^3w+o(t^3),
\qquad
r_a(t)=-y_a+tm_a+t^2n_a+o(t^2).
\]

The requested middle-velocity expansion is

\[
\dot W_2(t)=t\mathcal D_1+t^2\mathcal D_2+t^3\mathcal D_3+o(t^3),
\]

where

\[
\mathcal D_1
=2\sum_a\omega_ay_a(uD_a)\otimes h_a,
\]
\[
\mathcal D_2
=2\sum_a\omega_a\bigl((y_av-m_au)D_a\bigr)\otimes h_a,
\]
\[
\begin{aligned}
\mathcal D_3=2\sum_a\omega_a\Big[
&\bigl((y_aw-m_av-n_au)D_a+y_auE_a\xi_a\bigr)\otimes h_a\\
&+y_a(uD_a)\otimes\eta_a
\Big].
\end{aligned}
\]

Thus

\[
W_2(t)=A+\frac{t^2}{2}\mathcal D_1
+\frac{t^3}{3}\mathcal D_2
+\frac{t^4}{4}\mathcal D_3+o(t^4).
\]

If the corresponding classical derivatives exist, their values are

\[
W_2'(0)=0,\qquad W_2''(0)=\mathcal D_1,\qquad
W_2'''(0)=2\mathcal D_2,\qquad
W_2''''(0)=6\mathcal D_3.
\]

### Derivation of the coefficients

At time zero, `W3=0` makes both hidden-weight velocities zero, while the readout velocity is `u`. Therefore `W3(t)=tu+o(t)`. Inserting this into the two hidden-weight equations gives

\[
\dot W_2(t)=2t\sum_a\omega_ay_a(uD_a)\otimes h_a+o(t),
\]
\[
\dot W_1(t)=2t\sum_a\omega_ay_ap_aA^*(uD_a)
\frac{x_a^T}{\sqrt2}+o(t).
\]

Integration gives `B,b`. The coefficient of `Z1a` is

\[
\frac{bx_a}{\sqrt2}
=\frac12\sum_b\omega_by_bG_{ab}p_bA^*(uD_b),
\]

and multiplying by `p_a` gives `eta_a`. Expanding `W2 H1a` gives `xi_a = B h_a + A eta_a`.

Since the first hidden change is order two, the first two output coefficients are simply `m_a=<u,g_a>` and `n_a=<v,g_a>`. The coefficients of the readout ODE therefore give

\[
2v=-2\sum_a\omega_am_ag_a,
\]
\[
3w=2\sum_a\omega_a(y_aD_a\xi_a-n_ag_a).
\]

Finally,

\[
W_3(t)\phi'(Z_{2a}(t))
=tuD_a+t^2vD_a+t^3(wD_a+uE_a\xi_a)+o(t^3).
\]

Multiplying by `-2 omega_a r_a(t)` and tensoring with
`h_a+t^2 eta_a+o(t^2)` produces the three displayed middle-velocity coefficients. In particular, residual order three is not needed at this order because the readout already starts at order one.

## Literal unit axes and label-independent features

For `x_a=e_a`, `a=1,2`, and `V=(G1,G2)` with independent standard Gaussians,

\[
z_a=G_a/\sqrt2,\qquad G_{ab}=\delta_{ab},\qquad
C_{ab}=c\,\delta_{ab},
\quad c=\mathbb E\tanh^2(G/\sqrt2).
\]

The factor `1/sqrt(2)` remains present for literal unit axes. Put
`alpha_a = omega_a y_a` and define

\[
U_{ab}=D_ag_b,\qquad
L_{ab}=p_a^2A^*U_{ab},\qquad
F_{ab}=2c\,U_{ab}+AL_{ab}.
\]

These functions do not depend on the labels. The hidden coefficients reduce to

\[
B=2\sum_{a,b}\alpha_a\alpha_bU_{ab}\otimes h_a,
\]
\[
\eta_a=\alpha_a\sum_b\alpha_bL_{ab},\qquad
\xi_a=\alpha_a\sum_b\alpha_bF_{ab}.
\]

The feature order is as follows.

| Coefficient | Features first needed |
| --- | --- |
| Readout, order `t` | `g_1,g_2` |
| Middle velocity, order `t` | Upper products `U_ab=D_a g_b`, paired with `h_a` |
| Middle velocity, order `t^2` | The same `U_ab tensor h_a` family |
| Lower hidden state, order `t^2` | `L_ab=p_a^2 A*(D_a g_b)` |
| Upper preactivation, order `t^2` | New forward images `A L_ab`, assembled in `F_ab` |
| Middle velocity, order `t^3` | Upper products with `F_ab`, and tensors pairing `U_ab` with `L_ac` |

For explicit label separation, write

\[
w=w_{\rm old}+w_{\rm new},\qquad
w_{\rm old}=-\frac23\sum_a\omega_an_ag_a,
\]
\[
w_{\rm new}=\frac23\sum_{a,b}\alpha_a^2\alpha_bD_aF_{ab}.
\]

The degree-four part in the labels of `D_3` is

\[
\begin{aligned}
\mathcal D_3^{[4]}
={}&\frac43\sum_{a,b,c}
\alpha_a\alpha_b^2\alpha_c
(D_aD_bF_{bc})\otimes h_a\\
&+4\sum_{a,c,d}\alpha_a^2\alpha_c\alpha_d
(g_dE_aF_{ac})\otimes h_a\\
&+4\sum_{a,c,d}\alpha_a^2\alpha_c\alpha_d
U_{ad}\otimes L_{ac}.
\end{aligned}
\]

Its degree-two part is

\[
\mathcal D_3^{[2]}
=2\sum_a
\bigl((\alpha_aw_{\rm old}-\omega_am_av-\omega_an_au)D_a\bigr)
\otimes h_a.
\]

All indices here range over `{1,2}`. Hence `D_1,D_2` are homogeneous quadratic label polynomials, and `D_3` has quadratic and quartic parts. A precise label-independent dictionary can be defined as the vector or tensor coefficients of these label monomials.

Coefficient separation yields symmetrized combinations when monomials coincide. It does not by itself identify each factor in an overcomplete displayed expansion. For example,

\[
[y_1y_2]\mathcal D_1
=4\omega_1\omega_2
\left(U_{12}\otimes h_1+U_{21}\otimes h_2\right).
\]

## Explicit verification of the supervisor's equal-weight formula

In this subsection, use the supervisor's notation `H_a=g_a`, `Y_a=s_a`,
`v0=c`, and equal weights `omega_1=omega_2=1/2`. The iid upper-forward initialization assumption gives

\[
\langle H_a,H_b\rangle_2=\tau\delta_{ab}.
\]

This upper Gram identity is an additional initialization property; it does not follow from a generic bounded operator alone. Given this identity, set

\[
S=y_1H_1+y_2H_2,
\qquad
J_2=\sum_a y_a(SD_a)\otimes h_a.
\]

Then the general formulas give

\[
u=S,\quad m_a=\tau y_a,\quad
v=-\frac\tau2S,\quad n_a=-\frac{\tau^2}{2}y_a.
\]

The lower and upper hidden coefficients are exactly

\[
\eta_a=\frac{y_a}{4}p_a^2A^*(SD_a),
\qquad
R_a=\xi_a=\frac{v_0y_a}{2}SD_a+A\eta_a.
\]

The factor `1/4` in `eta_a` consists of the equal sample weight `1/2` and the input Gram normalization `1/2`. The coefficient `v0 y_a/2` in `R_a` comes from `B h_a` and the diagonal lower Gram matrix.

With

\[
\mathcal V=\sum_b y_bD_bR_b,
\]

the readout coefficients are

\[
c_1=S,\qquad c_2=-\frac\tau2S,\qquad
c_3=\frac{\tau^2}{6}S+\frac13\mathcal V.
\]

Here `mathcal V` is the supervisor's `V`; the distinct font avoids collision with the initialized first-layer row denoted `V` earlier in this report.

For the middle velocity, the coefficient multiplying `J_2` at time order two is

\[
-\frac\tau2-\tau=-\frac{3\tau}{2}.
\]

At time order three, its three quadratic-label contributions are respectively

\[
\frac{\tau^2}{6}\quad\text{from }y_aw_{\rm old},
\qquad
\frac{\tau^2}{2}\quad\text{from }-m_av,
\qquad
\frac{\tau^2}{2}\quad\text{from }-n_au.
\]

Their sum is `7 tau^2/6`. Consequently the proposed expression is correct:

\[
\begin{aligned}
\dot W_2(t)
={}&tJ_2-\frac{3\tau}{2}t^2J_2\\
&+t^3\Bigg[\frac{7\tau^2}{6}J_2
+\sum_a y_a\Big\{
\bigl(\tfrac13\mathcal VD_a+S\phi''(Y_a)R_a\bigr)\otimes h_a
+(SD_a)\otimes\eta_a
\Big\}\Bigg]+o(t^3).
\end{aligned}
\]

This verifies every supplied constant and both readout coefficients. Since `phi''(Y_a)=E_a=-2H_aD_a`, the named gate functions also agree.

## Time order versus middle-operator passes

Initialization already uses the forward probes `A h_a`. The newly introduced feedback chain is

\[
U_{ab}\ \xrightarrow{A^*}\ A^*U_{ab}
\ \xrightarrow{\times p_a^2}\ L_{ab}
\ \xrightarrow{A}\ AL_{ab}.
\]

This adds one adjoint pass and one forward pass. It appears in hidden features at time order two, in the middle velocity at time order three, and in the middle weights at time order four. Including the initialized forward probe gives three operator applications along this dependency path. That count is separate from the time exponent. The order-two middle-velocity coefficient introduces no additional operator pass.

## What changes when the inputs vary

For nonorthogonal training inputs, the general lower coefficient is

\[
\eta_a=\sum_{b,c}\alpha_b\alpha_cG_{ab}
\,p_ap_bA^*(D_bg_c).
\]

The mixed lower functions with `b != a` no longer disappear, and their forward images must be included. In addition, the initial nonlinear probes themselves change with the inputs.

For example, a new input `x` requires

\[
h_x=\tanh\!\left(\frac{G_1x_1+G_2x_2}{\sqrt2}\right),
\qquad Ah_x.
\]

The function `h_(e1+e2)` is not in the linear span of `h_e1,h_e2`. Otherwise Gaussian full support and continuity would imply

\[
\tanh(z_1+z_2)=a\tanh z_1+b\tanh z_2
\]

for every pair of real arguments. Setting one argument to zero forces `a=b=1`; taking equal nonzero arguments contradicts the identity. If `q` is the nonzero component of `h_x` orthogonal to the two original lower probes, then `A` and `A+v tensor q` agree on those probes but differ on `h_x` by `v ||q||_2^2`. Thus two retained forward images do not determine the new forward image for an arbitrary bounded operator.

This is a limitation of fixed finite probes or a fixed linear-feature span. It does not say that `h_x` requires a new underlying Gaussian coordinate: invertibility of `tanh` makes `h_x` a measurable function of the two original lower features. Applying a linear operator to that new nonlinear function still requires a new operator query. Nor does this finite-order argument prove a general impossibility theorem about any conceivable infinite dictionary.

## Population regularity needed for this low order

Boundedness of `A:L2->L2` does not make the nonlinear vector field analytic on `L2`, guarantee a local solution by itself, or control arbitrary products of unbounded fields. These issues must not be inferred from the displayed algebra. For the particular low-order coefficients above, however, no product of two newly created unbounded fields is required.

Assume a continuous local solution of the supplied strong integral equations, with the first layer continuous in `L2(Omega1;R2)`, the middle operator continuous in operator norm, and the readout continuous in `L2(Omega2)`. The integrals are assumed meaningful in those spaces. Then the residuals are continuous and bounded on a sufficiently short interval. Since `|tanh|<=1`, the readout integral equation supplies the stronger bound

\[
\|W_3(t)\|_\infty\le
2\sum_a\omega_a\int_0^t|r_a(s)|\,ds=O(t).
\]

The hidden-weight velocities are therefore `O(t)` in the first-layer `L2` norm and middle Hilbert--Schmidt perturbation norm. Thus the hidden-weight increments and hidden-feature increments are `O(t^2)`.

Two elementary facts justify the successive expansions without an all-order smoothness assertion.

1. If `F` has bounded continuous first derivative, `z,v` are finite almost everywhere with `v in L2`, and `epsilon -> 0`, then

   \[
   \frac{F(z+\epsilon v)-F(z)}{\epsilon}
   \longrightarrow F'(z)v\quad\text{in }L^2.
   \]

   The pointwise convergence is ordinary scalar differentiability, and the difference quotient is dominated by `||F'||_infty |v|`. Dominated convergence gives the `L2` result. If the argument has an additional `o_L2(epsilon)` remainder, global Lipschitz continuity of `F` absorbs it. This applies to both `tanh` and its first derivative.

2. If uniformly bounded multipliers `q_t` converge to `q` in `L2` (or in measure on the probability space), then `(q_t-q)f -> 0` in `L2` for each fixed `f in L2`. For `L2` convergence, truncate `f` at height `R`: the bounded part is controlled by `R ||q_t-q||_2`, and the tail by the uniform multiplier bound times `||f 1_(|f|>R)||_2`. First take `t -> 0`, then `R -> infinity`.

For example, `A*(u D_a)` is in `L2` because `u,D_a` are bounded and `A*` is bounded. Multiplying it by the bounded first-layer gates gives `eta_a in L2`. Hence `A eta_a`, `xi_a`, and `w` are in `L2`. In the middle-velocity coefficient, the potentially unbounded factors `xi_a,w,eta_a` are multiplied only by bounded initialized functions, or occur as separate factors of a rank-one tensor. Such tensors satisfy

\[
\|u\otimes v\|_{\rm HS}=\|u\|_2\|v\|_2.
\]

For the expansion of the upper gated readout, the term `t^3 w (D_a(t)-D_a)` is `o_L2(t^3)` by the multiplier fact; it does not require `w` to be bounded. The leading terms `u,v` are bounded, so the order-two directional expansion of `D_a(t)` can safely be multiplied by them. These observations validate all products used through the requested order and the remainder estimates in `L2` and the Hilbert--Schmidt perturbation norm.

At higher order, expressions such as the square of a backpropagated `L2` direction can occur. Their `L2` control can require initialized higher moments, and an all-order analytic claim requires substantially more. Neither is established or needed by this finite-jet report. Classical higher derivatives, as distinct from the finite Peano coefficients established from the integral equations, should be asserted only when their additional regularity is supplied.
