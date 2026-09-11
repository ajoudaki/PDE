# The actual homogeneous trained propagator in the clock state

Author: `/root/propagator`. Status: complete author proof, pending the
study's independent scientific reviews. This component proves an
unconditional statement about the established reference and its explicitly
defined homogeneous tangent equation. Data-source admissibility and the
finite-width identification of that equation are separate components.

## 1. Exact scope and reference inputs

The model is the two-hidden-layer tanh network with no biases, normalized
input `u=x/sqrt(2)`, stored initial variances `(1,1/n,1/n²)`, stored-weight
mobilities `(n,1,n)`, unhalved mean squared loss, and physical time. The
reference is the equally weighted pair `(e1,+1),(e2,-1)` in normalized
input coordinates. The finite Gaussian readout is retained by the underlying
reference theorem; the population readout starts at zero as its limit.

Use the actual common Gaussian action spaces of established
`docs/global_nonlinear.md` B.1 and C.4.5.1–2:

\[
 H_1=L^2(\Omega_1),\qquad H_2=L^2(\Omega_2),\qquad
 A(t)=A_0+K(t):H_1\longrightarrow H_2.
\]

The action `A0` and its Hilbert adjoint are the jointly generated limits
of the same initialized middle matrix. Only `K` is Hilbert–Schmidt.
The complete source/action construction is special-data III.F.1–9;
global-nonlinear A.1–2 supplies the stated value/response extensions.
No independent Gaussian action is substituted anywhere below.

Write `phi=tanh`, `w=(w1,w2)`, `c=W^(3)`, and

\[
 H_a^1=\phi(w_a),\quad Z_a^2=AH_a^1,\quad H_a^2=\phi(Z_a^2),
 \quad\delta_a=c\phi'(Z_a^2),\quad Q_a=A^*\delta_a.
 \tag{1}
\]

Let `y1=1,y2=-1`, `p1=p2=1/2`. The reference prediction and residual
are `f_a=y_a b(t)` and `r_a=-y_a e(t)`, where `e=1-b>0`.
The established autonomous feature equation has its first `b=1` endpoint
at feature time `s_dagger<=10`; physical time satisfies `ds/dt=2e(t)`.
Its quantitative conclusions, including the endpoint on these same spaces,
are

\[
 e(t)\le e^{-t/5},\qquad
 \Delta(t):=\|\theta(t)-\theta_\infty\|_{\rm raw}
       \le\sqrt{10}\,e(t),
 \tag{2}
\]
\[
 \|A(t)\|\le M:=2+\sqrt{10},\quad
 \|c(t)\|_2\le C:=\sqrt{10},\quad
 \|c(t)\|_\infty\le10.
 \tag{3}
\]

The endpoint has all the same bounds. Here the raw increment norm is
row `L²` plus middle `HS` plus readout `L²`, combined in a square sum.
The active source result C.4.5.2, (R17), also gives at the endpoint

\[
 Q_{a,\infty}=\zeta_a+D_a,\qquad
 \zeta_a\sim N(0,v_a),\quad v_a\le10,\quad |D_a|\le B_Q,
 \quad B_Q=225400e^{2880}+180.
 \tag{4}
\]

No independence of `D_a` and `zeta_a` is needed. In particular,

\[
 \max_a\|Q_{a,\infty}\|_4\le
 M_4:=3^{1/4}\sqrt{10}+B_Q<\infty,
 \tag{5}
\]

by the triangle inequality and `E G^4=3` for a standard normal.
These are reference-only, active-query facts. No passive-query higher
moment claim or finite-width higher moment inference is used here.

## 2. The typed tangent equation and its bounded coefficients

Let `F(z)=z/2+sinh(2z)/4`, and define
`X_a=F(w_a)-F(g_a)`. Its scalar inverse obeys `w_{a,X}=phi'(w_a)`.
The clock tangent space is the Hilbert space

\[
 \mathcal V=L^2(\Omega_1;\mathbb R^2)
       \oplus\mathcal S_2(H_1,H_2)\oplus H_2,
 \quad
 \|v\|_{\mathcal V}^2=\|V\|_2^2+\|B\|_{\rm HS}^2+\|d\|_2^2,
 \quad v=(V,B,d).
 \tag{6}
\]

The raw variation is the bounded injective image

\[
 R(t)v=((\phi'(w_a)V_a)_{a=1,2},B,d),\qquad \|R(t)\|\le1.
 \tag{7}
\]

Its inverse is not assumed bounded. In particular, (6) is a stronger
norm than the pulled-back raw norm and is the norm used for the propagator.

For each training datum define the following bounded directional maps:

\[
 h_a[v]=\phi'(w_a)^2V_a,\quad
 z_a[v]=BH_a^1+Ah_a[v],\quad
 d_a[v]=d\phi'(Z_a^2)+c\phi''(Z_a^2)z_a[v],
\]
\[
 q_a[v]=B^*\delta_a+A^*d_a[v],\qquad
 \ell_a[v]=\langle d,H_a^2\rangle_2+
                       \langle\delta_a,z_a[v]\rangle_2.
 \tag{8}
\]

Define synthesis `S(t):R²->V` and evaluation `E(t):V->R²` by columns
and components,

\[
 G_a=(\mathbf e_a Q_a,\delta_a\otimes H_a^1,H_a^2),\quad
 S\alpha=\sum_a\sqrt{p_a}\alpha_aG_a,\quad
 (Ev)_a=\sqrt{p_a}\ell_a[v].
 \tag{9}
\]

The residual-curvature part is the bounded linear map

\[
 \mathcal C(t)v=-2\sum_a p_ar_a(t)T_a(t)v,
\]
\[
 T_av=(\mathbf e_a q_a[v],
             d_a[v]\otimes H_a^1+\delta_a\otimes h_a[v],
             \phi'(Z_a^2)z_a[v]).
 \tag{10}
\]

The homogeneous generator is exactly

\[
 \mathcal L(t)=-2S(t)E(t)+\mathcal C(t).
 \tag{11}
\]

Indeed the transformed reference vector field is
`-2 sum_a p_a r_a G_a`: its first block is
`X'_a=-2p_a r_a Q_a`, with no own first gate. The product rule produces
`-2 sum p_a ell_a[v] G_a` and (10). Equations (8) follow successively
by scalar differentiation, action differentiation and actual adjunction.
In raw first coordinates differentiating the gate would give
`phi''(w_a) delta w_a Q_a`; differentiating
`delta w_a=phi'(w_a)V_a` in physical time produces the same term
on the left and cancels it. Thus its absence in (10) is exact.

All maps in (8)–(11) exist on every `v in V`. Put

\[
 a_1=1+20(1+M),\quad a_q=C+Ma_1,\quad
 a_*=[a_q^2+(a_1+C)^2+(1+M)^2]^{1/2},\quad
 L_0=[1+C^2(1+M^2)]^{1/2}<17.
 \tag{12}
\]

For a unit `v`, (3), `|phi'|<=1`, `|phi''|<=2`, and
`||B||op<=||B||HS` give

\[
 \|h_a[v]\|_2\le1,\quad\|z_a[v]\|_2\le1+M,
 \quad\|d_a[v]\|_2\le a_1,\quad\|q_a[v]\|_2\le a_q.
\]

The middle component of `T_a v` has HS norm at most `a1+C`, and
the last has norm at most `1+M`. Consequently

\[
 \|T_a(t)\|\le a_*,\quad
 \|\mathcal C(t)\|\le2a_*e(t),\quad
 \|S(t)\|\le L_0,\quad\|E(t)\|\le L_0.
 \tag{13}
\]

For the synthesis estimate, each column before its `sqrt(p_a)` factor
has squared norm at most `M²C²+C²+1`; the column Cauchy–Schwarz
inequality gives the operator bound. The evaluation estimate follows
also from (14) below.

The generator is strongly continuous on `V`. To see this without an
unjustified operator-norm continuity assertion, first fix `v`. The
reference raw fields are strongly continuous, `A` is HS-continuous in
its increment, and `c` is continuous in supremum norm because
`c_s=(H1²-H2²)/2` is bounded by one pointwise. If bounded continuous
multipliers converge in probability, their product with a fixed L²
vector converges in L²: truncate that fixed vector, then use bounded
convergence on its bounded part. Apply this statement successively
in (8), using the uniform multiplier bounds and rank-one HS inequality.
It proves strong continuity of (10); the finitely many fields in (9)
are L²-continuous by the same argument. General varying multiplier
operators need not converge in operator norm. Nor does this argument
assert ambient Fréchet differentiability of an L² Nemytskii vector field.

## 3. The canonical metric and the singular endpoint

Set `D(t)=R(t)*R(t)`, explicitly multiplication by `phi'(w_a)^2`
in the row blocks and identity in the other blocks. Adjunction in (8)
gives the exact identities

\[
 E(t)=S(t)^*D(t),\qquad
 K(t):=E(t)S(t)=S(t)^*D(t)S(t)\succeq0.
 \tag{14}
\]

Thus `K` is the raw training-gradient Gram with the square roots of
the training weights in both indices. In particular, if `Ev` is the
weighted training-prediction variation, its Gauss–Newton-only equation
is `(Ev)'=-2K(Ev)` at a frozen state. There is no missing mean-loss factor.

Although `D` has no positive lower operator bound, it is injective:
`phi'(w_a)>0` almost surely since the L² field `w_a` is finite almost
surely. For any `alpha in R²`,

\[
 \alpha^TK\alpha=\|RS\alpha\|_{\rm raw}^2.
\]

It vanishes if and only if `S alpha=0`. Therefore, at every time,

\[
 \ker K=\ker S=\ker E^*,\qquad
                    \operatorname{ran}E\subseteq\operatorname{ran}K.
 \tag{15}
\]

The second kernel equality uses `E*=DS` and injectivity of `D`.
For the range assertion take orthogonal complements in finite-dimensional
`R²`: `ran E=(ker E*)perp` and `ran K=(ker K)perp`.
This is the required zero-mode compatibility. Positivity of `ES` alone
without (15) would be insufficient: `ES=0` can coexist with nonzero
nilpotent `SE` for general rectangular maps.

For any fixed pair `S,E` satisfying (14)–(15), let `K+` denote the
Moore–Penrose inverse defined by orthogonal diagonalization of the
finite symmetric matrix `K`: invert its positive eigenvalues and
retain zero on its kernel. Directly,

\[
 V_\infty(\tau):=\exp(-2\tau S_\infty E_\infty)
 =I+S_\infty K_\infty^+
       [\exp(-2\tau K_\infty)-I]E_\infty,\qquad\tau\ge0.
 \tag{16}
\]

For completeness, the bounded-operator exponential is its absolutely
convergent power series. For `j>=1`,
`(SE)^j=S K^(j-1) E`. On `ran K`,
`K+ K^j=K^(j-1)`, and (15) says `E` takes values there. Substituting
these identities in the two absolutely convergent series proves (16),
also at `tau=0` and also when `K=0`. In the latter case (15) implies
`S=0`, so both sides are identity.

Since all eigenvalues of `K` are nonnegative,
`||exp(-2tau K)-I||<=1`. Consequently

\[
 \sup_{\tau\ge0}\|V_\infty(\tau)\|\le
 B_\infty:=1+\|S_\infty\|\,\|K_\infty^+\|\,\|E_\infty\|
       \le1+L_0^2\|K_\infty^+\|<\infty.
 \tag{17}
\]

This is a finite precisely defined reference quantity. It is not an
evaluated numerical conditioning certificate and imposes no lower
bound on a positive eigenvalue, no full-rank assumption, and no
continuity assumption on pseudoinverses along the trajectory.

## 4. Integrability of the actual perturbation of the endpoint

Only the finite-rank fields, rather than all multiplier operators,
need endpoint convergence in operator norm. Factor subtraction using
(2)–(3) gives

\[
 \|H_a^1-H_{a,\infty}^1\|_2\le\Delta,
 \quad\|Z_a^2-Z_{a,\infty}^2\|_2\le(1+M)\Delta,
\]
\[
 \|\delta_a-\delta_{a,\infty}\|_2\le a_1\Delta,
 \quad\|Q_a-Q_{a,\infty}\|_2\le a_q\Delta.
 \tag{18}
\]

For example, split the backward product with the endpoint readout
as the fixed factor; its supremum is at most ten. Split the adjoint
product with the endpoint `delta`, whose L² norm is at most `C`.
The rank difference in `G_a` is at most `(a1+C)Delta`, so

\[
                       \|S(t)-S_\infty\|\le a_*\Delta(t).
 \tag{19}
\]

The evaluation column is `(e_a phi'(w_a)^2Q_a,
delta_a tensor H_a^1,H_a²)`. For its extra first-block difference,
use the exact pointwise bounds

\[
 |\phi'(z)^2-\phi'(\bar z)^2|\le\min(1,4|z-\bar z|).
\]

If the left side is `b`, then `|b|^4<=|b|²<=16|z-bar z|²`.
Hölder's inequality and (5) thus give

\[
 \|[\phi'(w_a)^2-\phi'(w_{a,\infty})^2]Q_{a,\infty}\|_2
 \le2M_4\|w_a-w_{a,\infty}\|_2^{1/2}.
\]

Combining the finitely many weighted columns yields

\[
 \|E(t)-E_\infty\|\le a_*\Delta(t)+2M_4\Delta(t)^{1/2}.
 \tag{20}
\]

No product of two arbitrary L² tangent fields occurs here; the only
unbounded multiplied field is the fixed endpoint `Q_a` with its
proved L⁴ bound. In particular (20) does not promote L² convergence
of a general multiplication operator to operator-norm convergence.

Set

\[
 \mathcal B(t)=\mathcal L(t)+2S_\infty E_\infty.
\]

Equations (13), (19), (20), and `||S||,||E||<=L0` give

\[
 \|\mathcal B(t)\|
 \le(4L_0a_*\sqrt{10}+2a_*)e(t)
                  +4L_0M_4\,10^{1/4}e(t)^{1/2}.
 \tag{21}
\]

The norm is measurable: on separable `V`, it is the supremum of
`||B(t)v||` over a countable dense subset of the unit sphere, each
continuous in `t`. Integration of (21), using (2), proves

\[
 J:=\int_0^\infty\|\mathcal B(t)\|\,dt
 \le J_0:=20L_0a_*\sqrt{10}+10a_*
                         +40L_0M_4\,10^{1/4}<\infty.
 \tag{22}
\]

This includes both integrability of residual curvature and integrable
operator-norm approach of the Gauss–Newton finite-rank part to its
endpoint. The active Gaussian moment enters the latter implication.

## 5. Construction and uniform estimate for the actual propagator

There is a unique strong evolution `U(t,s)` on `V`, `0<=s<=t<infinity`,
satisfying

\[
 U(t,s)v=v+\int_s^t\mathcal L(q)U(q,s)v\,dq.
 \tag{23}
\]

Here and below integrals are strong vector integrals. To construct it
on a compact interval with coefficient bound `L`, set `u0(t)=v` and
successively integrate `u_(j+1)(t)=int_s^t L(q)u_j(q)dq`.
Strong continuity, (13), and induction give
`||u_j(t)||<=||v|| L^j(t-s)^j/j!`. The sum is uniformly convergent
and satisfies (23) by the same summable bound. Iterating the integral
inequality for the difference of two solutions makes that difference
zero, since its bound contains `L^j(t-s)^j/j!` for every `j`.
Uniqueness gives `U(t,r)U(r,s)=U(t,s)`. This argument constructs
bounded operators, although the coefficients need not be continuous
in operator norm.

For fixed `v`, differentiating the constant-coefficient exponential
in (16), or substituting (23) into its convergent power series and
integrating, gives variation of constants:

\[
 U(t,s)=V_\infty(t-s)+
       \int_s^t V_\infty(t-q)\mathcal B(q)U(q,s)\,dq
 \tag{24}
\]

as an identity on each vector. Taking norms and iterating the scalar
integral inequality yields

\[
 \|U(t,s)\|\le B_\infty
     \exp\!\left(B_\infty\int_s^t\|\mathcal B(q)\|\,dq\right)
 \le C_U:=B_\infty e^{B_\infty J_0}.
 \tag{25}
\]

One way to verify the scalar step is to substitute the bound repeatedly;
the `j`th ordered integral of the nonnegative function `||B||`
is at most `(int ||B||)^j/j!`, giving the exponential series.
Thus

\[
                  \sup_{0\le s\le t<\infty}\|U(t,s)\|<\infty.
 \tag{26}
\]

The conclusion concerns the actual trained homogeneous coefficients,
not solely a frozen endpoint system. All conditioning dependence is
exposed by `||K_infty+||`. The displayed crude constants establish
finiteness; they are not useful numerical magnitudes.

For any strongly measurable forcing `F in L1_loc([0,infinity);V)`,
the unique solution with initial value zero is

\[
 v(t)=\int_0^tU(t,s)F(s)\,ds,
 \qquad
 \sup_{t\le T}\|v(t)\|_{\mathcal V}
             \le C_U\int_0^T\|F(s)\|_{\mathcal V}\,ds.
 \tag{27}
\]

Approximation by simple forcing functions and (25) proves existence
of this integral; substitution using the integrable majorants proves
the equation, and homogeneous uniqueness proves uniqueness.
If the separate off-support source proof establishes
`sup_s ||F_sigma(s)||_V<=C_source,Y ||sigma||TV`, then (27) gives
`sup_(t<=T)||v_sigma(t)||<=C_U C_source,Y T ||sigma||TV`.
That hypothesis is not established by this homogeneous component.

## 6. Passive evaluation and the endpoint's fitted-prediction kernel

For any normalized `u` on the entire circle define
`H1(u)=phi(w dot u)`, `Z2(u)=A H1(u)`, `H2(u)=phi(Z2(u))`,
`delta(u)=c phi'(Z2(u))`, and `Q(u)=A*delta(u)`. Its tangent response is

\[
 \delta H^1(u)=\phi'(w\cdot u)\sum_a u_a\phi'(w_a)V_a,
 \quad\delta Z^2(u)=BH^1(u)+A\delta H^1(u),
\]
\[
 \ell(t,u)v=\langle d,H^2(u)\rangle_2+
               \langle\delta(u),\delta Z^2(u)\rangle_2.
 \tag{28}
\]

The raw predictor gradient has block norms at most `MC,C,1`;
the first estimate is `||u phi'(w dot u)Q(u)||2<=MC`.
Combining this with (7) proves, simultaneously for all circle inputs,

\[
 \|R(t)v\|_{\rm raw}\le\|v\|_{\mathcal V},\qquad
 \|\delta H^1(u)\|_2\le\|v\|_{\mathcal V},\qquad
 \|\delta Z^2(u)\|_2,\|\delta H^2(u)\|_2
                         \le(1+M)\|v\|_{\mathcal V},
\]
\[
                 \sup_{|u|=1}|\ell(t,u)v|\le L_0\|v\|_{\mathcal V}.
 \tag{29}
\]

For each fixed `v`, this predictor response is continuous in `u`.
The raw fields are L²-continuous in `u` by bounded slopes; the
bounded-multiplier argument already proved after (13) applies to
the fixed row tangent. Formula (28) then passes continuity through
the bounded action and scalar pairing. Uniform quantitative input
derivative tails are not asserted. Combining (27) and (29) gives
the analogous forced whole-circle output bound.

At the fitted endpoint the frozen semigroup has limit

\[
 P_\infty=I-S_\infty K_\infty^+E_\infty,
 \quad P_\infty^2=P_\infty,
 \quad\operatorname{ran}P_\infty=\ker E_\infty,
 \quad\ker P_\infty=\operatorname{ran}S_\infty.
 \tag{30}
\]

The square identity uses `K+ K K+=K+`. The range and kernel use
`KK+E=E` and `S K+K=S`, which follow from (15).
Furthermore

\[
 D_\infty(I-P_\infty)=E_\infty^*K_\infty^+E_\infty
\]

is self-adjoint. More explicitly, put `G=R_infty S_infty`, the
weighted raw gradient synthesis. Then `G*G=K_infty` and

\[
 R_\infty P_\infty v
      =(I-GK_\infty^+G^*)R_\infty v.
 \tag{31}
\]

The middle operator is the raw Hilbert orthogonal projection off
the span of the two weighted training gradients: on that span it
is identity before subtraction by (15), and it annihilates its
orthogonal complement. Thus (30) separates fitted training-prediction
changes from parameter changes preserving both training predictions
to first order, using the canonical raw metric on the admissible
clock domain. An unseen evaluation `ell(infty,u)P_infty v` may
survive; its value, sign, or usefulness is not determined by (30).
No assertion that the nonautonomous propagator itself converges
to `P_infty` is required here.

## 7. Check scope and downstream use

The proof is exact at the population reference and all physical times.
It does not imply uniform-in-time finite-width convergence. It needs
neither a short initialization interval nor new training experiments.
It does not reconstruct a nonlinear population flow for perturbed laws,
nor identify this equation as a derivative of an unavailable law-to-flow
map. Its new structural steps are the injective-clock metric kernel
identity (15), the singular semigroup formula (16), and integrable
finite-rank convergence (19)–(22). The earlier reference's energy
path-length improvement is an explicit imported dependency, not a new
claim of this study.

For nonlinear continuation, this component supplies an actual bounded
propagator, the compatible `V` state and `L1_t V` forcing norms,
and bounded whole-circle observation maps. A future nonlinear
comparison must additionally control off-support weighted gate ratios,
products of reference or perturbed backward fields with variations,
and quadratic remainders such as a varying readout times a hidden
tangent. Those estimates do not follow from (25) or from a raw L²
energy bound. The ambient curvature and multiplier obstructions in
the maintained library are therefore respected rather than bypassed.
