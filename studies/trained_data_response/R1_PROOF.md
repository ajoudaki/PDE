# Frozen scientific candidate

Authors: `/root`, `/root/propagator`, `/root/weighted_source`, `/root/capture`.
Each component below is included verbatim; equation numbers are local to it.


<!-- BEGIN THEOREM.md -->

# Trained data response at a nonlinear fitted reference

Author/assembler: `/root`, with component authors named in their proofs.
Status: candidate theorem under author reconstruction; not independently
accepted or promoted. The conclusions below require the complete component
proofs, not their summaries.

## 1. Model and meaning of the response

Let `Y≥1`, `u=x/sqrt(2)∈S¹`, and use two tanh hidden layers of equal width n,
no biases, and

\[
 z^1=W^1u,\quad h^1=\tanh z^1,\quad z^2=W^2h^1,\quad
 h^2=\tanh z^2,\quad f_n=(W^3)^Th^2/n.
\]

All initialized entries and blocks are independent centered Gaussians, with
stored variances `(1,1/n,1/n²)`. The mobilities are `(n,1,n)` and the loss
is the unhalved mean square. Time t is physical GF time. For a nonatomic
training law the finite loss is integrated exactly against that law.

Fix `nu*=½delta_(sqrt(2)e1,+1)+½delta_(sqrt(2)e2,-1)` and any deterministic
Borel probability law nu on `Z=sqrt(2)S¹×[-Y,Y]`. Set
`mu_epsilon=(1-epsilon)nu*+epsilon nu`, `sigma=nu-nu*`. Use the same three
initialized arrays for every epsilon, retaining the actual finite Gaussian
readout. The observable is the right derivative

\[
 D_\sigma f_n(t,x)=\left.\frac{d}{d\epsilon^+}
                  f_{n,\mu_\epsilon}(t,x)\right|_{\epsilon=0}.
 \tag{1}
\]

This derivative is taken at each finite n before n tends to infinity.
It is not defined by differentiating a nonlinear population law-to-flow
map. No such perturbed population map through an arbitrary T is assumed.

## 2. State, exact equation and observations

Use the established canonical reference action spaces
`H_i=L²(Omega_i)` and the actual reference `(w(t),A(t),c(t))`, including its
full first row and both orientations of `A=A0+K`. The initialized action
A0 is bounded and its reverse is its actual Hilbert adjoint; only K is
Hilbert–Schmidt. The fitted endpoint is the established first b=1 state
of the autonomous reference feature equation, at feature time at most ten.

Put `phi=tanh`, `F(z)=z/2+sinh(2z)/4`, and
`X_a=F(w_a)-F(g_a)`. The tangent Hilbert space and finite same-width norm are

\[
 \mathcal V=L^2(\Omega_1;\mathbb R^2)\oplus
             \mathcal S_2(H_1,H_2)\oplus H_2,\qquad
 \|V\|_{\mathcal V}^2=\|\xi\|_2^2+\|B\|_{HS}^2+\|d\|_2^2,
 \tag{2}
\]
\[
 \|V_n\|^2=\|\xi_n\|_F^2/n+\|B_n\|_F^2+\|d_n\|_2^2/n.
 \tag{3}
\]

Here `V=(xi,B,d)` and the raw variation is
`((phi'(w_a)xi_a)_a,B,d)`. Thus its raw norm is at most `||V||_V`.
The inverse conversion need not be bounded. The population norm (2) and
finite norm (3) are never subtracted across different carriers.

At every passive direction u define

\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad
 H^2(u)=\phi(Z^2(u)),\quad \delta(u)=c\phi'(Z^2(u)),\quad
 Q(u)=A^*\delta(u),\quad r(u,y)=\langle c,H^2(u)\rangle-y.
 \tag{4}
\]

The forcing, linear in the signed measure sigma, is

\[
 b_\sigma(t)=-2\int_Z r(t,u,y)
 \left(
  \left(u_a\frac{\phi'(w(t)\cdot u)}{\phi'(w_a(t))}Q(t,u)\right)_{a=1,2},
  \delta(t,u)\otimes H^1(t,u),\ H^2(t,u)
 \right)\,d\sigma(u,y).
 \tag{5}
\]

The rank-one action is `(q tensor h)v=q E_1[hv]`; its finite representative
is `q h^T/n`. Formula (5) includes the loss factor two and the signed
reference subtraction. It also retains the forward and adjoint uses of
the same initialized Gaussian action.

With the exact synthesis, evaluation and residual-curvature operators
defined in PROPAGATOR.md (8)–(11), the forced evolution is

\[
 \dot V_\sigma(t)=\mathcal L(t)V_\sigma(t)+b_\sigma(t),\qquad
 \mathcal L(t)=-2S(t)E(t)+\mathcal C(t),\qquad V_\sigma(0)=0.
 \tag{6}
\]

All coefficients are computed from the autonomous reference state.
Their source is not a future-trajectory oracle. They define bounded
strongly continuous operators on (2); no ambient Fréchet differentiability
of an L²-valued nonlinear vector field is asserted.

The prediction derivative produced by (6) is

\[
 \mathscr D_\sigma f(t,\sqrt2u)=\ell(t,u)V_\sigma(t),
 \quad \ell(t,u)V=\langle d,H^2(u)\rangle+
 \langle\delta(u),BH^1(u)+A[\phi'(w\cdot u)
                   \sum_a u_a\phi'(w_a)\xi_a]\rangle.
 \tag{7}
\]

The lower hidden response has norm at most `||V||_V`; both the upper
preactivation and activation responses have norm at most `(3+sqrt(10))||V||_V`.
Uniformly in all physical times and circle inputs,
`||ell(t,u)||≤L0<17`, with L0 defined in PROPAGATOR.md (12).

## 3. Candidate conclusions and constants

The complete proofs are PROPAGATOR.md, WEIGHTED_SOURCE.md, and
FINITE_CAPTURE.md. Together they establish the following proposed claims.

**Admissible forcing and well-posed evolution.** Let `M_0(Z)` be the real
Banach space of finite signed Borel measures of mass zero, with total
variation *mass* `||sigma||TV=|sigma|(Z)` (no factor one-half).
The integrand in (5) is a continuous V-valued function and the integral is
a Bochner integral. Its bounded linear extension to `M_0(Z)` is justified
by (5), rather than by a two-sided probability neighborhood. Equation (6)
has a unique strong solution for every such sigma and every finite horizon.

The weighted-source proof establishes finiteness of the reference quantity

\[
 M_w=\sup_{t\ge0,\,u\in S^1,\,a=1,2}
          \|\cosh^2(w_a(t))Q(t,u)\|_2<\infty.
 \tag{8}
\]

In particular, putting

\[
 C_{b,Y}=2(\sqrt{10}+Y)\sqrt{M_w^2+11},
 \qquad \sup_{t\ge0}\|b_\sigma(t)\|_{\mathcal V}
                       \le C_{b,Y}\|\sigma\|_{TV},
 \tag{9}
\]

is valid: the row norm uses `sum_a u_a²=1`, the middle rank has norm
at most `sqrt(10)`, and the readout factor has norm at most one.
The exact envelope `cosh² w_a≤cosh² g_a+2|X_a|` and actual finite cavity
moments supply the weighted integrability in (8). RMS value convergence
alone is not the proof of that step.

**Actual finite-GF capture.** For every fixed nu as above and every fixed
`T<infinity`, including `T=40`,

\[
 \sup_{0\le t\le T,\,x\in\sqrt2S^1}
       |D_\sigma f_n(t,x)-\mathscr D_\sigma f(t,x)|
          \longrightarrow0\quad\hbox{in probability}.
 \tag{10}
\]

The probability is over the initialized arrays. The state is identified
by same-width finite-program approximations in the uniform-in-time norm
(3), whose canonical counterparts converge in (2). Their finite rank
expansions identify middle Hilbert–Schmidt inner products and both action
directions. Joint named same-layer fields converge with their second moments
at every finite list of times and passive inputs. FINITE_CAPTURE.md specifies
this topology and proves the stronger comparison needed to justify (10).
It does not assert operator-norm convergence of finite matrices to operators
on another carrier, or hidden tangent path laws beyond the stated topology.

Every deterministic estimate is independent of the support size, smallest
atom weight and Gram rank of nu. Convergence is for each fixed nu; a failure
probability uniform over all laws is not part of (10). No rate is asserted.

**Uniform population propagation.** Let U(t,s) be the homogeneous evolution
of (6). PROPAGATOR.md proves

\[
 \sup_{0\le s\le t<\infty}\|U(t,s)\|\le C_U<\infty,
 \qquad V_\sigma(t)=\int_0^tU(t,s)b_\sigma(s)\,ds,
 \tag{11}
\]
\[
 \sup_{t\le T}\|V_\sigma(t)\|_{\mathcal V}
       \le C_U C_{b,Y}T\|\sigma\|_{TV},\qquad
 \sup_{t\le T,x}|\mathscr D_\sigma f(t,x)|
       \le L_0 C_U C_{b,Y}T\|\sigma\|_{TV}.
 \tag{12}
\]

The admissible general forcing norm is `L¹([0,T];V)`; (11) bounds response
by C_U times that norm. In (12), contamination directions obey `||sigma||TV≤2`.

For conditioning, `K_infty=E_infty S_infty=S_infty*D_infty S_infty`,
where `D_infty` multiplies the row blocks by `phi'(w_a,infty)²` and is
identity on the other blocks. This operator is injective, although not
uniformly coercive. Hence `ker K_infty=ker S_infty=ker E_infty*`.
The reference Gram may be singular. Its finite-dimensional pseudoinverse
is well defined and the explicit bound is

\[
 B_\infty=1+\|S_\infty\|\|K_\infty^+\|\|E_\infty\|,
 \qquad C_U=B_\infty\exp(B_\infty J_0),
 \tag{13}
\]

with the completely specified finite J0 in PROPAGATOR.md (22). The proofs
give finiteness through reference quantities, not an evaluated numerical
certificate for endpoint conditioning or a useful numerical response constant.
They assume no spectral gap or full-rank endpoint Gram. Uniform population
propagation is separate from fixed-horizon finite-width convergence (10).

## 4. Interpretation and what the next milestone receives

At the fitted endpoint,
`P_infty=I-S_infty K_infty+ E_infty` projects onto `ker E_infty`.
Under the raw conversion it is the canonical raw-metric orthogonal
projection off the span of the weighted training gradients. These directions
preserve both fitted predictions to first order; their unseen evaluations
are `ell(infty,u)P_infty V` and need not be determined by training outputs.
This is an exact decomposition of the actual endpoint tangent operator.
It asserts neither a nonzero unseen change for every direction nor a sign
or risk benefit. A changed scalar clock alone does not describe the response.

The next nonlinear-continuation milestone receives an actual trained
propagator, an admissible full-row clock/HS/readout state, a total-variation
data-to-forcing map, and controlled passive observations. It still must
control nonlinear products away from the reference, including changes of
off-support inverse-gate factors times reverse queries, products of readout
and hidden increments, and the quadratic remainder of hidden activation
changes. These are not bounded bilinear maps on arbitrary L² directions
merely because the present linear equation is bounded.

No nonlinear perturbed population flow, finite-contamination remainder,
large path of laws, sampling CLT, expected-risk expansion, endpoint
continuity, transport forcing modulus, or raw-GD derivative theorem is
included. Empirical laws of nonatomic distributions do not approach them
in total variation. Nothing here is a convergence claim for a training-time
Taylor series or evidence of superiority of one learning mechanism.

<!-- END THEOREM.md -->

<!-- BEGIN PROPAGATOR.md -->

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

<!-- END PROPAGATOR.md -->

<!-- BEGIN WEIGHTED_SOURCE.md -->

# Actual finite reference queries and admissible data forcing

Author: `/root/weighted_source`. This is an author proof candidate, not an
independent review or a promoted result. The new argument is a one-column
deletion comparison for the actual continuous reference flow. It proves the
weighted uniform integrability missing from a value-only Gaussian-program
argument. No training experiment is used.

## 1. Model, notation and conclusions

Use precisely the model in the study assignment: two width-n tanh hidden
layers, no biases, normalized input `u=x/sqrt(2)` on `S^1`, forward equations
`z1=w u`, `h1=tanh(z1)`, `z2=A h1`, `h2=tanh(z2)`,
`f=c^T h2/n`; independent initialized entries of variances `(1,1/n,1/n²)`;
stored-weight mobilities `(n,1,n)`; unhalved mean squared loss; physical time.
Throughout the actual finite reference GF trains on the two atoms
`(e1,+1),(e2,-1)` of weight one half each. Its finite initialized readout is
the prescribed Gaussian vector, never zeroed.

All finite vector norms are ordinary Euclidean norms, with their `sqrt(n)`
normalization displayed. Finite rank-one actions are `v h^T/n`; their ordinary
Frobenius norms equal the corresponding population Hilbert–Schmidt norms.
At population width use the canonical separate spaces
`H1=L²(Omega1)`, `H2=L²(Omega2)`, with the actual initialized Gaussian action
`A0:H1->H2` and its adjoint. Write `A=A0+K`; only `K` is Hilbert–Schmidt.

Let `phi=tanh`, and, for any passive input `u`, define

\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad
 H^2(u)=\phi(Z^2(u)),\quad
 \delta(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\delta(u).
 \tag{S1}
\]

The finite starred action in this display is the actual transpose. Define

\[
 F(z)=z/2+\sinh(2z)/4,\quad
 X_a=F(w_a)-F(g_a),\qquad a=1,2.
 \tag{S2}
\]

Here `g_a` is the unchanged initialized first column. The two active inputs
are exactly the two first-row coordinates, so this is the full first-row
clock. Since `F'=cosh²>0`, the global inverse gives
`w_a=J(X_a,g_a)`, where `J_X=phi'(J)` and `|J_X|<=1`.

For every fixed finite physical `T`, put

\[
 E_n=\{\|A_{0,n}\|_{op}\le10,
          \|c_{0,n}\|_\infty\le1,
          \|g_n\|_F/\sqrt n\le2\}.
 \tag{S3}
\]

Its probability tends to one. The matrix assertion follows from the
contained sphere-net Gaussian estimate in special-data III.F.2; the root
assertion is the iid second-moment law; and
`P(max_j |c0,j|>1)<=2n exp(-n²/2)`. In particular (S3) retains the actual
small Gaussian readout.

**Finite source theorem.** For each finite `p>=1,T<infinity`, there is a
finite deterministic `C_(p,T)` such that

\[
 \mathbb E\left[\mathbf1_{E_n}\frac1n\sum_{i=1}^n
       \sup_{t\le T,u\in S^1}|Q_{n,i}(t,u)|^p\right]
       \le C_{p,T},\qquad n\ge1.                         \tag{S4}
\]

The constants can be chosen with `C_(p,T)^(1/p)<=C_T sqrt(p)` for `p>=2`.
The supremum concerns query **values**; it does not assert Gaussian tails
for input derivatives. Set `N_(n,i)=sup_(t<=T,u)|Q_(n,i)(t,u)|`. Then

\[
 \sup_{t\le T}|X_{n,ia}(t)|\le3T N_{n,i},\qquad
 \sup_{t\le T}|w_{n,i}(t)|\le |g_{n,i}|+6T N_{n,i},
 \tag{S5}
\]

and all finite moments, averaged over coordinates and restricted to `E_n`,
of the following envelopes are bounded independently of width:

\[
 N_{n,i},\quad (1+|g_{n,i}|+N_{n,i})^k,\quad
 \{\cosh^2g_{n,ia}+6T N_{n,i}\}N_{n,i},\quad
 (|g_{n,i}|+6T N_{n,i})N_{n,i}.                    \tag{S6}
\]

Here `k` is any separately fixed finite positive integer. Products of a
fixed number of these envelopes have the same property. These are actual
finite-GF estimates, before any width limit.

**Population source theorem.** For the established reference of C.4.5,
there is a finite `M_*` such that

\[
 \sup_{t\ge0,u\in S^1}
 \left(\sum_{a=1}^2
     \|\cosh^2 w_a(t)Q(t,u)\|_{L^2(\Omega_1)}^2\right)^{1/2}
 \le M_* .                                                 \tag{S7}
\]

The proof below gives an entirely explicit, very large upper bound from
`s_dagger<=10`; alternatively (S7) defines the precise reference quantity
consumed by the forcing theorem. It is not a numerical evaluation of the
actual trained endpoint.

For `Z=sqrt(2)S^1 x [-Y,Y]` and a finite signed Borel measure `sigma`, define
the clock-state forcing, of type

\[
 \mathcal H=L^2(\Omega_1;\mathbb R^2)
          \oplus\mathcal S_2(H_1,H_2)\oplus H_2,
 \tag{S8}
\]

by its Bochner integral

\[
 B_\sigma(t)=\int b(t,u,y)\,d\sigma(\sqrt2u,y),
 \quad b=-2r(t,u,y)\left(
    \left(u_a\frac{\phi'(w\cdot u)}{\phi'(w_a)}Q(u)\right)_{a=1}^2,
    \delta(u)\otimes H^1(u),\ H^2(u)\right).
 \tag{S9}
\]

Then `B_sigma` is continuous in physical time, is linear in `sigma`, and

\[
 \sup_{t\ge0}\|B_\sigma(t)\|_{\mathcal H}
 \le 2(Y+\sqrt{10})\sqrt{M_*^2+11}\,\|\sigma\|_{TV}.
 \tag{S10}
\]

Total variation denotes total mass of the variation measure, with no
factor of one half. The estimate applies in particular to `nu-nu_*`, of
mass at most two. It imposes no support size, atom weight, Gram or
orthogonality restriction on the perturbing law. The same finite forcing
has bounded normalized moments and weighted uniform integrability on
`E_n`, uniformly over `t<=T` and inputs, with constants depending on `T,Y`.

Section 8 states the precise width identification and quadrature conclusion.
These source results alone are not a tangent-capture theorem. They supply
the inhomogeneous term needed by that theorem and by the propagator result.

## 2. Exact physical equations and deterministic reference bounds

The mean loss is `R=(r1²+r2²)/2`. From the stored-weight mobilities the exact
finite reference equations, and their population counterparts, are

\[
 \dot w_a=-r_a\phi'(w_a)Q_a,\quad
 \dot X_a=-r_aQ_a,\quad
 \dot K=-\sum_{a=1}^2r_a\delta_a\otimes H_a^1,\quad
 \dot c=-\sum_{a=1}^2r_aH_a^2 .                    \tag{S11}
\]

Here `Q_a=Q(e_a)`; the two factors of the general `-2 integral` cancel the
two atom weights. Since `F'=1/phi'`, the clock identity in (S11) is exact.
For a general law the corresponding first clock field is
`-2 integral r u_a phi'(w.u)Q(u)/phi'(w_a)`, which gives (S9), with its
displayed sign and normalization. No probability-law derivative is used
to establish these identities.

On (S3), initially `|f_a|<=1`, hence `R(0)<=4`. The true raw energy identity
gives `R(t)<=4` and raw path displacement at most `2sqrt(T)` up to time T.
Therefore, simultaneously for all `t<=T`,

\[
 \|A(t)\|_{op}\le B:=10+2\sqrt T,\quad
 \|c(t)\|_2/\sqrt n\le C:=1+2\sqrt T,
 \quad\|w(t)\|_F/\sqrt n\le W:=2+2\sqrt T,
 \tag{S12}
\]

and `||K||F<=2sqrt(T)`. Moreover `sum_a|r_a|<=4`, `|r_a|<=sqrt(8)<3`.
Integration of `dot c` yields

\[
 \|c(t)\|_\infty\le H:=1+4T.                    \tag{S13}
\]

The raw energy identity follows directly by differentiating the finite
loss and substituting its three negative metric gradients; the three
metric terms are `||dot w||F²/n`, `||dot A||F²`, `||dot c||²/n`.
It prevents finite-time escape for the smooth finite-dimensional field.
These statements also hold for the column-deleted flow below, because it
has the same labels and readout, and its initial matrix norm is no larger.

For passive queries all these bounds are independent of u. Directly from
(S11),

\[
 \|\dot w\|_F/\sqrt n\le4BC,\quad
 \|\dot K\|_F\le4C,\quad \|\dot c\|_\infty\le4.
 \tag{S14}
\]

The chain and product rules in finite dimensions give

\[
 \|\partial_t Z^2(u)\|_2/\sqrt n\le4C(1+B^2),\qquad
 \|\partial_t\delta(u)\|_2/\sqrt n
        \le D_t:=4+8HC(1+B^2),
 \tag{S15}
\]

and factor subtraction gives

\[
 \|\delta(t,u)-\delta(t,v)\|_2/\sqrt n
       \le D_u|u-v|,\quad D_u:=2HBW.
 \tag{S16}
\]

Thus `(t,u)->delta(t,u)` is Lipschitz in normalized L², with deterministic
constants on (S3). Only the first-row **RMS** occurs in (S16). This fact,
applied to the independent cavity, is what permits a whole-circle Gaussian
query-value estimate without bounds on pointwise input derivatives.

## 3. Delete one initialized column, retaining the entire learned flow

Fix neuron i in population 1. Let `a_i=A0 e_i`, an ordinary vector with iid
entries `N(0,1/n)`. Run the full reference GF with the initialized matrix

\[
 \widetilde A_0=A_0-a_i e_i^T
 \tag{S17}
\]

and the same initialized `g,c0`. Denote this flow by tildes. In particular
`tilde K` is trained; no neuron, activation, residual or learned rank is
removed. The flow is independent of the random column `a_i` conditionally
on all remaining initialized variables. Uniqueness of the finite ODE
establishes that measurability and independence.

Define the cavity-good event

\[
 E_n^i=\{\|\widetilde A_0\|_{op}\le10,
            \|c_0\|_\infty\le1,\ \|g\|_F/\sqrt n\le2\}.
 \tag{S18}
\]

It is measurable with respect to the remaining variables, and `E_n` is a
subset of `E_n^i`, because right multiplication by `I-e_i e_i^T` is a
contraction. Conditional Gaussian estimates are always made on (S18),
not by falsely conditioning on an event involving `a_i`.

Set `m_i=||a_i||2`, `epsilon_i=m_i/sqrt(n)` and

\[
 Z_i(t,u)=a_i^T\widetilde\delta(t,u),\qquad
 Z_i^\#=\sup_{t\le T,u\in S^1}|Z_i(t,u)|.
 \tag{S19}
\]

These are scalar probes of the cavity, not replacements for actual query
answers. Their conditional covariance is exactly
`tilde delta(t,u)^T tilde delta(s,v)/n`. Both orientations of the actual
matrix remain in the comparison that follows.

Let

\[
 x=\sum_a\|X_a-\widetilde X_a\|_2/\sqrt n,\quad
 k=\|K-\widetilde K\|_F,\quad
 z=\|c-\widetilde c\|_2/\sqrt n,\quad d=x+k+z.
 \tag{S20}
\]

There is no small operator-norm claim for `A0-tilde A0`. Instead its
forward action on a bounded feature has RMS at most `epsilon_i`. Its
reverse action on a cavity backward field has RMS
`|Z_i(t,e_a)|/sqrt(n)`. With `Delta` denoting full minus cavity, add and
subtract factors in precisely this order:

\[
 \Delta Z_a^2=A\Delta H_a^1
         +(K-\widetilde K)\widetilde H_a^1
         +a_i\widetilde H_{a,i}^1,
\]
\[
 \Delta Q_a=A^T\Delta\delta_a
          +(K-\widetilde K)^T\widetilde\delta_a
          +e_i Z_i(t,e_a).
 \tag{S21}
\]

The second identity deliberately uses the full A in the first term, so
that no uncontrolled column-dependent reverse error appears. On `E_n`,
the deterministic state bounds for both flows yield

\[
 \sum_a\|\Delta H_a^1\|_2/\sqrt n\le x,
 \quad V:=\sum_a\|\Delta Z_a^2\|_2/\sqrt n
                      \le Bx+2k+2\epsilon_i,
\]
\[
 D:=\sum_a\|\Delta\delta_a\|_2/\sqrt n\le2z+2H V,
\]
\[
 P:=\sum_a\|\Delta Q_a\|_2/\sqrt n
       \le BD+2Ck+\frac1{\sqrt n}\sum_a|Z_i(t,e_a)|,
\]
\[
 R_\Delta:=\sum_a|r_a-\widetilde r_a|\le2z+CV.
 \tag{S22}
\]

For the last inequality use `f-tilde f=<Delta c,H2>+
<tilde c,H2-tilde H2>`. The first uses `|J_X|<=1`, with the same roots.
The velocity differences from (S11) satisfy

\[
 \sum_a\|\Delta\dot X_a\|_2/\sqrt n\le BC R_\Delta+3P,
\]
\[
 \|\Delta\dot K\|_F\le C R_\Delta+3(D+Cx),\qquad
 \|\Delta\dot c\|_2/\sqrt n\le R_\Delta+3V.
 \tag{S23}
\]

For example the rank difference is bounded by
`||Delta delta||2/sqrt(n)+C||Delta H1||2/sqrt(n)` before its residual
factor. These estimates include the changed residuals; the cavity has
not been driven by the full flow's residuals.

Write `D0=1+B+C+H+3`, `L=100D0^4`. Substitution of (S22) into (S23)
gives the explicit overestimate

\[
 \dot d\le Ld+\frac L{\sqrt n}
       \left(m_i+\sum_a|Z_i(t,e_a)|\right)
       \quad\hbox{for almost every }t,\qquad d(0)=0.
 \tag{S24}
\]

To check the constant, `V<=3D0 d+2epsilon_i`,
`D<=8D0² d+4D0 epsilon_i`,
`P<=10D0³d+4D0²epsilon_i+sum|Z_i|/sqrt(n)`,
`R_Delta<=5D0²d+2D0epsilon_i`.
The three resulting d coefficients sum to at most `81D0^4`, and the
`epsilon_i` coefficients to at most `36D0³`. Norms of absolutely
continuous finite curves obey the derivative bound by the velocity norm,
which justifies (S24) also at zeros of a component norm. Multiplying its
integral form by the integrating factor gives

\[
 \sqrt n\sup_{t\le T}d(t)
       \le J_T(m_i+2Z_i^\#),\qquad J_T:=LT e^{LT}.
 \tag{S25}
\]

This is the small response to deleting one initialized column that an
operator-norm comparison alone would miss.

For an arbitrary passive input u, the first row still obeys
`||Delta(w.u)||2/sqrt(n)<=x`, so the same forward subtraction gives

\[
 \|\delta(t,u)-\widetilde\delta(t,u)\|_2/\sqrt n
            \le4D0^2(d(t)+\epsilon_i).
 \tag{S26}
\]

The learned transpose contribution has an exact, coordinatewise bound:

\[
 (K(t)^T\delta(t,u))_i
   =-\int_0^t\sum_a r_a(v)H_{a,i}^1(v)
       \frac{\delta_a(v)^T\delta(t,u)}n\,dv,
 \qquad |(K(t)^T\delta(t,u))_i|\le4TC^2.
 \tag{S27}
\]

Using `Q_i=a_i^T delta+(K^T delta)_i`, (S25)–(S27), and `m_i<=10` on
`E_n`, gives

\[
 N_{n,i}\le A_T Z_i^\#+B_T\quad\hbox{on }E_n,
\]
\[
 A_T=1+80D0^2J_T,\qquad
 B_T=400D0^2(J_T+1)+4TC^2.
 \tag{S28}
\]

No independence of the actual `delta` and `a_i` has been assumed. Their
dependence is exactly the error controlled in (S26).

## 4. A contained Gaussian maximum bound

Here are all probability ingredients beyond the initialized operator
bound. If `G_1,...,G_N` are centered jointly Gaussian scalars with
variances at most `v²`, no independence among them is required for

\[
 \Pr\{\max_j|G_j|>r\}\le2N e^{-r^2/(2v^2)}.
 \tag{S29}
\]

This follows by applying the scalar Gaussian exponential moment and
Markov's inequality to each tail and taking a union bound. Consequently,
for `p>=2`,

\[
 \|\max_j|G_j|\|_{L^p}
       \le v\{\sqrt{2\log(2N)}+2\sqrt p\}.
 \tag{S30}
\]

For detail, put `a=v sqrt(2log(2N))` and `V=(max|G_j|-a)_+`.
Equation (S29) implies `P(V>r)<=exp(-r²/(2v²))`.
For `m=ceil(p/2)`, integrating this tail against `2m r^(2m-1)` gives
`E V^(2m)<=(2v²)^m m!`; the integral follows by substituting
`q=r²/(2v²)` and integrating by parts m times. Since `m!<=m^m`,
monotonicity of probability-space Lp norms gives
`||V||p<=||V||_(2m)<=v sqrt(2m)<=v sqrt(2p)`, because
`2m<=p+2<=2p` for `p>=2`. Minkowski gives (S30), with slack in the
constant 2. The case `v=0` is zero.

Suppose a continuous centered Gaussian process `Z(q)`, `q in [0,1]^2`,
has variance at most `C²` and
`||Z(q)-Z(q')||L² <= L0 ||q-q'||_1`. Use square grids of spacing `2^-k`
and round each grid point down to its parent on the preceding grid.
There are at most `4^(k+1)` grid points at level k. Parent increments
have standard deviation at most `2L0 2^-k`. Formula (S30), followed by
Minkowski, bounds the sum over k of their maxima in Lp by

\[
 2L0\sum_{k\ge1}2^{-k}
  \{\sqrt{2\log(2\cdot4^{k+1})}+2\sqrt p\}
       \le60L0\sqrt p.
 \tag{S31}
\]

The inequality follows for instance from `sqrt(k+2)<=k+2` and
`sum_(k>=1) k2^-k=2`, `sum_(k>=1)2^-k=1`. The four level-zero corner
values cost at most `4C sqrt(p)` by (S30). The telescoping sums and
continuity at each q therefore give

\[
 \|\sup_q|Z(q)|\|_{L^p}
                \le64(C+L0)\sqrt p.                    \tag{S32}
\]

This proof works conditionally on arbitrary fixed coefficients. Here,
conditional on all variables except column `a_i`, the process (S19) is
a finite linear combination of independent Gaussians, with continuous
coefficients. On `E_n^i`, (S12), (S15)–(S16) apply to the cavity. Parameterize
`t=T q1`, `u=(cos(2pi q2),sin(2pi q2))`. Thus (S32) gives

\[
 \left(\mathbb E_{a_i}[(Z_i^\#)^p]\right)^{1/p}
       \le C_Z\sqrt p,\qquad
 C_Z:=64\{C+T D_t+2\pi D_u\},\quad\hbox{on }E_n^i.
 \tag{S33}
\]

Since `E_n subset E_n^i`, (S28), conditioning, and then (S33) prove

\[
 \left(\mathbb E[\mathbf1_{E_n}N_{n,i}^p]\right)^{1/p}
     \le (B_T+A_T C_Z)\sqrt p=:C_T\sqrt p.
 \tag{S34}
\]

This bound is the same for every i and n; averaging proves (S4). It has
not inferred empirical moments from RMS convergence or exchangeability.
It used the reached continuous reference flow and its quantitative
column-deletion sensitivity. The selected-column concentrating examples
in special-data J.1 and the three-query obstruction in Gaussian calculus
therefore do not contradict it: those arbitrary adapted queries do not
satisfy (S24) with the present constants.

## 5. Clock weights, products and actual finite uniform integrability

For each fixed g,

\[
 \partial_X\cosh^2 J(X,g)=2\tanh J(X,g),
 \qquad \cosh^2 J(X,g)\le\cosh^2g+2|X|.
 \tag{S35}
\]

The derivative identity follows from `J_X=sech² J`; its absolute value is
at most two, and integration gives the inequality for either sign of X.
This exact estimate avoids an unnecessary exponential in `|X|`. Integrating
`dot X_a=-r_a Q_a` with `|r_a|<=3` proves (S5). The factor 6 in its row
bound is an upper bound for `3sqrt(2)`.

Every Gaussian root has every polynomial and linear-exponential moment.
In particular
`E exp(q|G|)<=E exp(qG)+E exp(-qG)=2exp(q²/2)`.
For any fixed p, the moment of `cosh²g_a N_i` on `E_n` is bounded by
Hölder using the `2p` moments of both factors. No independence between
the evolved query and g is required. The same reasoning applies to all
products in (S6). For example, with

\[
 P_{n,i,a}:=(\cosh^2g_{n,ia}+6T N_{n,i})N_{n,i},
 \tag{S36}
\]

one obtains

\[
 \sup_n\mathbb E\left[\mathbf1_{E_n}\frac1n\sum_i
                          P_{n,i,a}^{p}\right]<\infty.
 \tag{S37}
\]

For the finite source coordinate in (S9), `|r(t,u,y)|<=C+Y` and
`|u_a|,phi'(w.u)<=1`, so its supremum over `t,u,|y|<=Y` is bounded by
`2(C+Y)P_(n,i,a)`. Given any `p>2`,

\[
 \mathbb E\left[\mathbf1_{E_n}\frac1n\sum_i
     P_{n,i,a}^{2}\mathbf1_{P_{n,i,a}>R}\right]
       \le C_{p,T}R^{-(p-2)}.                         \tag{S38}
\]

Markov's inequality shows that these empirical square tails tend to zero
in probability, uniformly in width on `E_n`, as R tends to infinity.
Outside `E_n` the probability tends to zero as n grows. Thus the ordered
statement needed for width passage is

\[
 \lim_{R\to\infty}\limsup_{n\to\infty}
 \Pr\left\{\sup_{t,u,|y|\le Y}
       \frac1n\sum_i |b_{X,a,n,i}(t,u,y)|^2
                     \mathbf1_{|b_{X,a,n,i}|>R}>\varepsilon\right\}=0.
 \tag{S39}
\]

One can put the supremum inside the coordinate envelope as in (S38), so
the stated form follows. The same argument proves weighted tails involving
`|w|Q` or any separately fixed polynomial of the displayed envelopes.
These estimates make no assertion that a bounded initialized Gaussian
action maps every Lp input boundedly into Lp.

## 6. Uniform population bounds from the bounded feature segment

The established physical reference equals the autonomous feature flow

\[
 X_{a,s}=\tfrac12y_a Q_a,\quad
 K_s=\tfrac12\sum_a y_a\delta_a\otimes H_a^1,\quad
 c_s=\tfrac12\sum_a y_aH_a^2,
 \tag{S40}
\]

restricted to `0<=s<s_dagger`, where `s_dagger<=10`, with
`ds/dt=2(1-b)>0`. This is C.4.5.1's actual reference and endpoint, not a
new prescription for physical finite GF. To bound the population sources
uniformly in physical time, apply the preceding cavity argument to the
**auxiliary finite feature equation** (S40) on `0<=s<=S=10`, initialized
with `c0=0`. Only this auxiliary equation has zero finite readout.

Its elementary deterministic bounds, on
`{||A0||op<=10, ||g||F/sqrt(n)<=2}`, are

\[
 \|c(s)\|_\infty\le S,\quad \|K(s)\|_F\le S^2/2,\quad
 B=10+S^2/2,\quad C=H=S+1,
\]
\[
 \|w(s)\|_F/\sqrt n\le
 W:=2+10S^2/2+S^4/8.                               \tag{S41}
\]

Indeed `sum_a |y_a/2|=1`, so `||c_s||infty<=1`,
`||K_s||F<=s`, and
`sum_a ||X_(a,s)||2/sqrt(n)<= (10+s²/2)s`. Integration and
`|J(X,g)-g|<=|X|` give (S41). These bounds prove existence on the entire
finite feature interval as in B.1's transformed integral construction.

The proof of (S21)–(S28) now uses the same fixed controls in both flows;
all residual-difference terms vanish. The retained upper bound `L=100D0^4`
remains valid. The velocity bounds (S14)–(S16) remain upper bounds, since
the absolute sum of feature controls is at most one rather than four.
Consequently the formulas (S28), (S33), (S34), with `T` replaced by S and
the constants (S41), give a number `C_*<infinity` such that

\[
 \mathbb E\left[\mathbf1_{E_n^{feat}}\frac1n\sum_i
      \sup_{s\le S,u}|Q^{feat}_{n,i}(s,u)|^p\right]
         \le(C_*\sqrt p)^p,\qquad p\ge2.             \tag{S42}
\]

Every quantity in this crude bound is explicitly given above. No numerical
flow solution is hidden in `C_*`, and no fitting property of the finite
feature flow is assumed.

We detail how this reaches the *canonical* population flow. On each fixed
transformed Euler mesh, append finitely many passive forward and reverse
queries to the oracle program in B.1. The first-row transform is continuous
with at most linear growth in `(X,g)`, hence global-nonlinear A.1 applies.
Readout products can be clipped outside a fixed open neighborhood of the
bound in (S41), so they meet the fixed-program hypotheses. Both matrix
orientations belong to the same III.F construction. Same-root transformed
stability controls the finite-feature-flow/mesh error uniformly in width.
The corresponding population error tends to zero in clock L², increment
HS and readout L²; the HS assertion is proved in C.4.5.2, §1. Passive Q
errors follow by factor subtraction with bounded readout. Width first at
fixed mesh, then mesh removal, therefore gives the joint empirical W2
limits for every finite list of `(g,X,w,Q(s,u))`.

For a finite list of rational parameter pairs `(s_j,u_j)`, apply this
convergence to the bounded continuous test
`min(R,max_j |Q(s_j,u_j)|^p)`. Its empirical average converges in
probability to the deterministic population expectation; since the test
is bounded, the expectations converge as well. Multiplication by
`1_(E_n^feat)` changes the expectation by at most
`R P((E_n^feat)^c)`, which vanishes. Equation (S42) and monotone convergence,
first in R and then in the finite rational lists, give a population
envelope

\[
 N^\#:=\sup_{(s,u)\in\mathcal D}|Q(s,u)|,
 \qquad\|N^\#\|_{L^p}\le C_*\sqrt p,             \tag{S43}
\]

where `mathcal D` is any fixed countable dense parameter set including
the active directions. This envelope is a statement about simultaneous
representatives on that countable set. For any other fixed deterministic
`(s,u)`, L² continuity of Q supplies an almost surely convergent subsequence
from the dense set; thus `|Q(s,u)|<=N#` in its L² equivalence class.
Fubini gives the bound almost everywhere for any fixed deterministic
observation measure. No assertion of pointwise continuous sample paths
for the population Q, or of Gaussian input-derivative tails, is needed.
The map into L² is jointly continuous and is the canonical action map.

Integration of (S40), followed by Fubini, gives almost surely
`sup_s |X_a(s)|<=S N#/2`, for the absolutely continuous active clocks.
Thus (S35) gives, in every deterministic passive-input equivalence class,

\[
 |\cosh^2w_a(s)Q(s,u)|
          \le(\cosh^2g_a+S N^\#)N^\#.
 \tag{S44}
\]

Hölder, `||N#||4<=2C_*`, and
`||cosh²G||4<=(2e^32)^(1/4)=2^(1/4)e^8` imply the explicit bound

\[
 M_*\le\sqrt2\{2^{5/4}e^8 C_*+4S C_*^2\},\qquad S=10.
 \tag{S45}
\]

The physical path stays in this feature segment, so (S7) holds for all
physical times. This reasoning establishes a uniform population source
bound, separately from the fixed-physical-horizon finite estimate (S4).
It does not claim uniform-in-time finite-width convergence.

## 7. Continuity, admissibility and norms of data forcing

The integrand (S9) has all its components in (S8). For the first component,
`phi'(w_a)^(-1)=cosh²w_a` and (S7) apply. For the others,
`||delta tensor H1||HS<=||c||2`, `||H2||2<=1`.
The established feature endpoint bound gives `||c||2<=sqrt(10)` and
`|f(u)|<=sqrt(10)`, hence `|r(u,y)|<=Y+sqrt(10)`. Squaring the three
component bounds gives (S10).

For completeness the integrand is continuous into (S8) jointly in feature
time, input and label. The bounded reference state and its strong velocity
give deterministic L² Lipschitz bounds for `Q(s,u)` by differentiating
`Q=A*delta` in time and using (S16) in input. Their population derivation
uses III.F.9's strong curve chain rule, not ambient Fréchet differentiability.
The envelope (S43) controls all their higher moments. The elementary
interpolation inequality

\[
 \|V\|_4\le\|V\|_2^{1/3}\|V\|_8^{2/3}
 \tag{S46}
\]

follows by Hölder with `1/4=(1/3)/2+(2/3)/8`. Therefore, for any fixed
weight `W0 in L4`,

\[
 \|W0\{Q(s,u)-Q(s',v)\}\|_2
 \le\|W0\|_4\|Q(s,u)-Q(s',v)\|_2^{1/3}
                         (2\|N^\#\|_8)^{2/3}.
 \tag{S47}
\]

For the changing weight use the exact derivative in (S35):
`|cosh²w_a(s)-cosh²w_a(s')|<=2|X_a(s)-X_a(s')|<=N#|s-s'|`.
Also
`|phi'(w(s).u)-phi'(w(s').v)|`
is bounded by a constant times
`N#|s-s'|+(|g|+S N#)|u-v|`.
Every resulting product with Q and the clock weight is integrable in L²
by (S43), Gaussian root moments, and Hölder. Changing the factors of
`r u_a cosh²w_a phi'(w.u)Q` one at a time, (S47) treats the Q difference
and these bounds treat the remaining factors. This proves continuity,
and in fact a deterministic `1/3` Hölder upper bound in `(s,u,y)` on the
compact feature/data parameter set. Middle and readout factors are simpler
Lipschitz differences in L²/HS.

The range of a continuous map from that compact parameter set into the
Hilbert space (S8) is compact and separable. Finite signed Borel measures
therefore admit its Bochner integral, with norm bounded by the integral
of the norm against the variation measure. This proves existence,
linearity, and (S10). Time continuity of the integral follows from uniform
continuity of its compact-domain integrand. Composing with the physical
clock gives continuity for all finite physical intervals, and the same
estimate holds at the fitted endpoint. This construction does not assume
that every signed zero-mass measure is a two-sided probability-law tangent:
it defines a linear forcing operator after the finite right derivatives
have supplied (S9).

The same reasoning at actual finite width uses (S4)–(S6) and the
deterministic normalized L² Lipschitz bound on `Q(t,u)` from (S14)–(S16).
For example its time constant is at most `4C²+B D_t`, and its input
constant at most `B D_u`. On `E_n` there is a random `Z_n` with bounded
fixed moments, uniformly in n, such that

\[
 \|b_n(t,u,y)-b_n(t',v,y')\|_{\mathcal H_n}
 \le Z_n\{|t-t'|+|u-v|+|y-y'|\}^{1/3}.
 \tag{S48}
\]

Here the finite clock-state norm is
`(||v||F²/n+||B||F²+||d||2²/n)^(1/2)`. To see that `Z_n` has the claimed
moments, use (S47) with normalized empirical norms and the finite envelope
`N_(n,i)`, and bound the remaining factor differences by (S5), (S35).
Every empirical envelope norm involved has bounded moments by (S6),
Jensen, and Hölder. No pointwise-in-input derivative moments are required.
The label term is actually Lipschitz; it is weakened to the displayed
exponent only to use one modulus on the compact set. If its diameter is
larger than one, enlarge `Z_n` by that fixed diameter to cover all pairs.

## 8. Exact identification and arbitrary Borel laws

We specify what convergence this source proof supplies, rather than
inventing an operator-norm distance between different width carriers.

1. For each finite deterministic list of physical times and passive inputs,
   the actual finite reference tuples consisting of the full Gaussian
   roots, clocks, raw first fields, hidden values, c and passive Q have
   their joint within-population W2 limits, identified by B.1 and the
   complete III.F/A.1 fixed-mesh construction. The append-only passive
   reverse call is legitimate for exactly the same reason as C.4.5.3's
   active call: bounded readout makes `c phi'(Z2(u))` a bounded-derivative
   instruction after an inactive fixed readout clip; its response uses
   the same initialized action and transpose. The passive first argument
   `w.u` retains both root coordinates. Actual finite readout is handled
   by the same-root finite-flow/mesh comparison; its supremum vanishes in
   probability as in B.1, rather than by resetting the finite flow.

2. Any finite tuple of the source first components (S9), roots, clocks,
   and query values has joint empirical Wp convergence in probability
   for every separately fixed finite p. First clip the additional
   coordinate functions at a fixed level. The tuple is a bounded
   continuous function of the identified node tuple, so its law converges.
   For any moment exponent p, (S6) with a larger exponent controls the
   unbounded tails by (S38). The same moment bound passes to the limiting
   tuple by bounded tests and monotone convergence. Removing the clipping
   identifies moments as well as weak laws. The elementary finite-cell
   coupling proof in III.F.1 extends verbatim from squared distance to
   p-th distance using `|a-b|^p<=2^(p-1)(|a|^p+|b|^p)`; hence these two
   conclusions give Wp convergence. Roots use their Gaussian moments,
   and clocks use (S5). A claim of all moments for arbitrary unrelated
   Gaussian programs is neither assumed nor concluded.

3. In particular, the W2 source-tuple comparisons extend uniformly over
   compact physical time/input/label parameter sets for each fixed tuple
   arity. Use (S48) and pair equal finite neuron indices to bound empirical
   W2 changes between nearby parameters. Its random modulus is tight by
   the just-proved moment estimates. The limiting modulus follows from
   Section 7 (or the same compact-time physical proof). At a fixed finite
   parameter net every required convergence holds simultaneously by a
   finite union bound. Refine the net after taking width to infinity.
   This proves the asserted uniformity for observable laws, without
   coupling individual finite neurons to invented population neurons.

4. For any fixed Borel probability law nu, choose a deterministic finite
   partition of the compact data space with cells of diameter at most h
   and choose one representative per nonempty cell. Let `pi_h nu` put
   its exact cell mass at that representative. This does not impose a
   lower bound on nonzero masses. Minkowski and (S48) give, uniformly for
   `t<=T`,

   \[
   \|B_{\nu,n}(t)-B_{\pi_h\nu,n}(t)\|_{\mathcal H_n}
          \le Z_n h^{1/3}\quad\hbox{on }E_n.
   \tag{S49}
   \]

   The analogous population bound holds with a deterministic constant.
   For a finite signed measure replace one by its total variation mass
   and partition its positive and negative parts, or retain the fixed
   two reference atoms exactly when forming `nu-nu_*`. At fixed h the
   first forcing field is a finite linear combination of the identified
   source nodes. Middle forcing is a finite sum of ranks; its HS norm
   and its differences are determined by the finite pairwise Gram
   contractions of its factors. All these contractions converge by the
   same-layer tuple statement. Thus fixed-law forcing and any fixed
   finite action/probe extension are obtained in the order: fixed
   quadrature and bounded source clips, width limit, source-clip removal,
   and quadrature refinement. Width-independent tails also allow clips
   and quadrature to be chosen in either prescribed nested order.

For action/probe extensions, a clipped source is first approximated by a
bounded smooth coordinate function on a fixed box of its finite input
tuple. The proof of A.1 permits this fixed approximation. Its normalized
L² error is controlled by (S39) and the corresponding population tail.
The initialized operator norm bound then controls the error after either
matrix orientation; learned ranks use their HS bound. A finite sequence
of such extensions is justified by induction, choosing each fixed smooth
approximation before the width limit. This is the action identification
needed when the linear tangent equation acts on the forcing.

Statements 1–4 provide constants independent of atom count and weights and
convergence for every fixed deterministic nu. They assert no failure
probability supremum over all nu, no convergence rate in width, no
uniform-in-physical-time finite-width approximation, and no convergence
of nonlinear perturbed flows. For nonatomic laws the finite loss and its
forcing are exactly integrated functions; the quadrature above is only a
proof approximation, not an empirical training algorithm.

## 9. Downstream use, remaining products and checks

The supplied admissible state norm is (S8); the admissible measure-forcing
norm is total variation. The exact consumed weighted source moment is
(S7). The proof additionally supplies all fixed moments of the actual
finite reference envelopes in (S6), and population counterparts uniformly
on the fitted feature segment. These are useful for passive output
observations, source truncation and input quadrature. The initialized
middle action is used only as a bounded L² action; no Lp action bound is
claimed.

A future finite-contamination theorem would still have to control
products involving the **perturbed** clocks or differences, such as
`[phi'(w_epsilon.u)/phi'(w_epsilon,a)-
phi'(w_*.u)/phi'(w_*,a)]Q_epsilon(u)`, and nonlinear remainders containing
products of two state variations. The present estimates concern the
reference and its one-column cavity, not those general perturbed paths.
Transport convergence of empirical laws to a nonatomic law is not total
variation convergence; (S49) is a separate quadrature estimate for the
reference's linear forcing.

The author read the complete maintained B.1 and C.4.5 reference/source/
finite bridge bodies, the necessary C.4 full-row/common-space passages,
global-nonlinear A.1–A.2, special-data III.F.1–10 (including the complete
singular-query proof), and the relevant III.V query-extension proof.
III.V was read for context; no III.V theorem is invoked here. The
append-only query proof used in Section 8 is supplied directly by III.F,
A.1, B.1's transformed comparison, and the present source truncation.
The arbitrary-action higher-moment, raw-multiplier/curvature and correlated
clock obstructions were checked explicitly. The invoked tools are the
`solve-math-rigorously` and `investigate-conjectures` skills and the latter's
research-contract, adversarial-audit and proof-search references.

The essential exact checks are reproducible without a training run:

```python
from fractions import Fraction as F
# Laurent polynomials in q=exp(z), represented exactly by exponent:coefficient.
def add(a,b):
    c=dict(a)
    for k,v in b.items(): c[k]=c.get(k,F(0))+v
    return {k:v for k,v in c.items() if v}
def mul(a,b):
    c={}
    for k,v in a.items():
        for l,w in b.items(): c[k+l]=c.get(k+l,F(0))+v*w
    return {k:v for k,v in c.items() if v}
cosh={1:F(1,2),-1:F(1,2)}
sinh={1:F(1,2),-1:F(-1,2)}
cosh2=mul(cosh,cosh)
Fprime={0:F(1,2),2:F(1,4),-2:F(1,4)}
assert Fprime == cosh2
derivative={k:k*v for k,v in cosh2.items() if k*v}
# Cross-multiplied identity (cosh²)'/cosh²=2tanh.
assert mul(derivative,cosh)==mul({k:2*v for k,v in sinh.items()},cosh2)
assert F(1,4) == F(1,3)/2 + F(2,3)/8
# The two atom weights cancel the unhalved-square factor exactly.
assert 2*F(1,2) == 1
print('PASS: primitive, clock envelope derivative, interpolation, loss weights')
```

Source hashes and actual execution evidence are recorded by the study's
coordinator when this candidate is frozen. These checks validate the
displayed identities; they do not replace a complete adversarial review
of the column-deletion and limit arguments.

<!-- END WEIGHTED_SOURCE.md -->

<!-- BEGIN FINITE_CAPTURE.md -->

# Actual finite-GF data derivatives and their population identification

Author component: `/root/capture`. This file proves the finite-width
identification bridge. Its probability input is the actual-reference weighted
source theorem in `WEIGHTED_SOURCE.md`, not a higher-moment assertion inferred
from the fixed-program theorem. The linear equation is stated explicitly below
so that the bridge can be checked independently of the all-time argument in
`PROPAGATOR.md`. This is an author candidate pending the complete paired review.

## 1. Model, tangent equation, and precise claim

Write `u=x/sqrt(2)`, `phi=tanh`, and use the full first row `w=(w_1,w_2)`.
The model, mean squared loss, stored-weight mobilities `(n,1,n)`, independent
Gaussian initial variances `(1,1/n,1/n^2)`, and actual finite readout are those
of the research contract. The reference has weights `p_1=p_2=1/2`, inputs
`e_1,e_2`, labels `y_1=1,y_2=-1`. The finite reference is its actual GF.
In particular it need not have the population exchange symmetry.

On the canonical spaces `H_i=L2(Omega_i)` put

\[
 \mathcal H=L^2(\Omega_1;\mathbb R^2)
       \oplus\mathcal S_2(H_1,H_2)\oplus H_2,
 \qquad \|v\|_{\mathcal H}^2=\|\xi\|_2^2+\|B\|_{HS}^2+\|d\|_2^2.
 \tag{F1}
\]

For finite arrays `v_n=(xi_n,B_n,d_n)` the corresponding norm is

\[
 \|v_n\|_{\mathcal H_n}^2
   ={\|\xi_n\|_F^2\over n}+\|B_n\|_F^2+{\|d_n\|_2^2\over n}.
 \tag{F2}
\]

The same symbol `B_n` here denotes a tangent matrix, not the reference
matrix. An initialized action has no HS assertion; both its learned increment
and its tangent have the indicated HS norm. A rank action has representative
`ab^T/n`, whose ordinary Frobenius norm is the product of the two RMS norms.

At the reference let

\[
 X_a=F(w_a)-F(g_a),\quad F(z)=z/2+\sinh(2z)/4,
 \quad D_a=\phi'(w_a),\quad w_a=j(X_a,g_a),
 \tag{F3}
\]

where `j_X=phi'(j)`. For a tangent `v=(xi,B,d)` define, at each passive `u`,

\[
\begin{aligned}
 \dot z_v^1(u)&=\sum_a u_aD_a\xi_a,&
 \dot h_v^1(u)&=\phi'(w\cdot u)\dot z_v^1(u),\\
 \dot z_v^2(u)&=B H^1(u)+A\dot h_v^1(u),&
 \dot h_v^2(u)&=\phi'(Z^2(u))\dot z_v^2(u),\\
 e_u(v)&=\langle d,H^2(u)\rangle+\langle c,\dot h_v^2(u)\rangle,\\
 \dot\delta_v^2(u)&=d\phi'(Z^2(u))
                     +c\phi''(Z^2(u))\dot z_v^2(u),&
 \dot Q_v(u)&=B^*\delta^2(u)+A^*\dot\delta_v^2(u).
\end{aligned}                                                     \tag{F4}
\]

Dots carrying a subscript `v` in (F4) mean directional variations, not
physical-time derivatives. All products have the displayed layer type.
Both `A` and `A*` are used literally. For training input `e_a` put

\[
 s_a=(\mathbf e_a Q_a,\delta_a^2\otimes H_a^1,H_a^2),
\quad
 Ds_a[v]=(\mathbf e_a\dot Q_v(e_a),
       \dot\delta_v^2(e_a)\otimes H_a^1
                +\delta_a^2\otimes\dot h_v^1(e_a),
       \dot h_v^2(e_a)),
 \tag{F5}
\]

where `bold e_a Q_a` means a two-component first-row field with only
component `a` nonzero. Define

\[
 G(t)v=-2\sum_{a=1}^2p_a
          \{e_{e_a}(v)s_a+r_a Ds_a[v]\},                         \tag{F6}
\]

and, for a finite signed measure `sigma` on `S1 x [-Y,Y]`,

\[
\begin{split}
 q(t,u,y)&=\left(
   (u_a\cosh^2w_a\,\phi'(w\cdot u)Q(u))_{a=1,2},
      \delta^2(u)\otimes H^1(u),H^2(u)\right),\\
 b_\sigma(t)&=-2\int (f(t,u)-y)q(t,u,y)\,d\sigma(u,y).
\end{split}                                                       \tag{F7}
\]

The symbol `q` does not actually depend on `y`; retaining `y` in its
argument makes the data integral's type explicit. The forced equation is

\[
 v_\sigma'(t)=G(t)v_\sigma(t)+b_\sigma(t),\qquad v_\sigma(0)=0.
 \tag{F8}
\]

The source theorem verifies that (F7) is a Bochner integral in (F1), uniformly
bounded on every compact time interval by a constant times total variation.
The generator is bounded and strongly continuous there. Directly from (F4),
if `||A||op, ||c||2, ||c||infinity` and the two residuals are bounded, then
`||G||op<=C`, independently of the carrier. For example

\[
 \|\dot h_v^1(e_a)\|_2\le\|\xi_a\|_2,\quad
 \|\dot z_v^2(e_a)\|_2\le\|B\|_{HS}+\|A\|_{op}\|\xi_a\|_2,
\]
\[
 \|\dot\delta_v^2(e_a)\|_2
 \le\|d\|_2+2\|c\|_\infty\|\dot z_v^2(e_a)\|_2,
\quad
 \|\dot Q_v(e_a)\|_2
 \le\|B\|_{HS}\|c\|_2+\|A\|_{op}\|\dot\delta_v^2(e_a)\|_2.
 \tag{F9}
\]

The other factors in (F5) have bounded L2 norms, and `e_u` is bounded by
`C||v||` uniformly in `u`. These estimates apply also at finite width.
Successive substitution of (F8)'s integral equation converges: its `k`th
iterated homogeneous integral has norm at most `(CT)^k/k!`. The same bound
on differences proves uniqueness. Thus no ambient Frechet differential of
an L2-valued Nemytskii field is an assumption of (F8).

**Finite-capture theorem.** For every fixed deterministic probability law
`nu` on the stated data space and every fixed `T<infinity`, let
`sigma=nu-nu_*`. Differentiate the finite exactly integrated GF along
`mu_epsilon=(1-epsilon)nu_*+epsilon nu` from the right at zero, using the
same initialized arrays. Then

\[
 \sup_{0\le t\le T,\ u\in S^1}
 \left|\left.\partial_{\epsilon+}f_{n,\mu_\epsilon}(t,\sqrt2u)
                    \right|_{\epsilon=0}-e_u(v_\sigma(t))\right|
       \longrightarrow0\quad\hbox{in probability}.                \tag{F10}
\]

This includes `T=40`. Section 5 gives the state/action topology supporting
this assertion. Constants used in estimates depend on the reference, `T`
and `Y`, and not on a support cardinality, a minimum weight or a Gram
eigenvalue. The convergence assertion fixes `nu` before taking width to
infinity; it is not a probability supremum over all laws.

## 2. Finite differentiation precedes every width limit

For fixed `n`, the loss integrated against any such Borel probability law
is a smooth finite-dimensional function of its three parameter arrays.
Indeed on a compact parameter set every derivative of the integrand is
continuous and bounded uniformly in `(u,y)`; differentiation of its integral
is justified by the bound on the difference quotient from the scalar mean
value formula. The vector field depends affinely on `epsilon`.

The finite raw energy identity, with squared increment norm
`||dw||F^2/n+||dA||F^2+||dc||2^2/n`, bounds the parameter displacement on
`[0,T]` by `sqrt(T L_n(0))`. Initial losses are uniformly bounded for
`epsilon in [0,1]`, at this fixed initialized network. The resulting compact
finite-dimensional parameter ball excludes finite-time escape. Local smooth
ODE construction and continuation therefore give all these finite flows.
For a nonatomic law this is GF of the exactly integrated loss, not an
empirical training algorithm.

Here is the parameter differentiation argument without invoking a
population law-to-flow map. Subtract the two finite integral equations.
On the preceding compact ball the derivative of the vector field is
bounded, so the scalar integral inequality gives
`sup_t||theta_epsilon-theta_0||<=C_n,T epsilon`.
Divide the subtracted equation by `epsilon`. The exact mean value formula
expresses its first term using the derivative of the reference vector
field on the line between these two paths; those coefficients converge
uniformly in time to their values at `theta_0`. The direct change of the
law is its signed integral against `sigma`. Subtract the claimed limiting
linear integral equation and use the same integral inequality. This proves
uniform-in-time convergence of the difference quotients, hence the right
derivative. All these arguments are at fixed width; their constants may
depend on `n` and are not used in the width passage.

For every finite coordinate `phi'(w_a)>0`, so differentiate the exact
coordinate change (F3). It gives

\[
 \delta w_a=D_a\xi_a.
 \tag{F11}
\]

For an arbitrary law the transformed first velocity is exactly
`-2 integral r u_a phi'(w.u)Q(u)/phi'(w_a) dmu`. At `nu_*` the only
nonzero contribution to row `a` has `u=e_a`; the two gates cancel
identically, before differentiating. Its homogeneous differential is
therefore `-2p_a[e_a(v)Q_a+r_a dot Q_v(e_a)]`. The direct law derivative
is precisely the first block of (F7). The middle and readout equations
differentiate to the other blocks of (F6)-(F7). This verifies every sign,
training weight and factor 2 in (F8). At time zero all array derivatives
vanish, since initialization is identical for all `epsilon`.

The finite output derivative is the scalar pairing (F4), with normalized
finite pairings. Thus (F8) at finite width is the actual derivative already
constructed, by uniqueness of its finite linear equation. The finite
Gaussian readout is present in every coefficient and forcing field.

After this construction, (F7)-(F8) define a linear extension to all finite
signed zero-mass directions. The extension agrees with the finite right
derivative for each probability-law path above. No assertion that arbitrary
signed directions admit a two-sided probability neighborhood is used.

## 3. Exact probability input and removal of data quadrature

Here is the specific statement consumed from `WEIGHTED_SOURCE.md`. Put

\[
 E_n=\{\|A_{0,n}\|_{op}\le10,
        \|c_{0,n}\|_\infty\le1,\|g_n\|_F/\sqrt n\le2\}.
 \tag{F12}
\]

It has probability tending to one. On it the actual reference, its clock
state and its velocities have deterministic compact-time RMS/action bounds,
and `||c_n(t)||infinity<=C_T`. If

\[
 Q^\#_{n,i}=\sup_{t\le T,u\in S^1}|Q_{n,i}(t,u)|,
 \quad X^\#_{n,ia}=\sup_{t\le T}|X_{n,ia}(t)|,
 \quad W^\#_{n,ia}=\cosh^2g_{n,ia}+2X^\#_{n,ia},
\]

then for every finite `p>=2` the source theorem gives finite constants
independent of width such that

\[
 E\left[1_{E_n}{1\over n}\sum_i
 \left\{(Q^\#_{n,i})^p+
       \sum_a(W^\#_{n,ia}Q^\#_{n,i})^p+
       (\sup_{t\le T}|w_{n,i}(t)|Q^\#_{n,i})^p\right\}\right]
 \le C_{p,T}.
 \tag{F13}
\]

The exact envelope `cosh^2 w_a(t)<=W^#_a` is part of that argument.
The analogous population bounds, on the canonical reference, are also
proved there. Only fixed finite moments and their uniform integrability
are used below. No Gaussian tail bound for input derivatives is asserted.

To check the measure approximation explicitly, let `chi_R(q)` be clipping
to `[-R,R]`, and let `rho_R(w)=min(cosh^2 w,R)`. In the first component
of (F7), replace `cosh^2 w_a Q(u)` by `rho_R(w_a)chi_R(Q(u))`; leave the
other two components unchanged. Call the resulting integrand `q_R` and
forcing `b_sigma,R`. On the compact-time state bounds, `q_R` times the
residual is globally Lipschitz in the data variable with a constant
`C_T,Y,R`, and is Lipschitz in the same-root clock/HS/readout distance.
For completeness, `rho_R` is bounded by `R` and Lipschitz with constant
at most `2R`; `chi_R` is bounded by `R` and 1-Lipschitz. Forward
differences obey

\[
 \|Z^1(u)-Z^1(v)\|_2\le\|w\|_2|u-v|,\qquad
 \|Z^2(u)-Z^2(v)\|_2\le\|A\|_{op}\|w\|_2|u-v|,
\]

and reverse differences obey the same type of bound because `c` is
bounded pointwise. Adding and subtracting the bounded factors in `q_R`
proves the asserted Lipschitz bounds. The middle rank difference has
the identical estimate in HS norm.

The clipping error tends to zero uniformly in `t,u` in probability at
finite width, in the following ordered sense:

\[
 \lim_{R\to\infty}\limsup_{n\to\infty}
 \Pr\{1_{E_n}\sup_{t\le T,u}\|q_n(t,u)-q_{n,R}(t,u)\|_{
                    \mathcal H_n}>a\}=0\quad(a>0).
 \tag{F14}
\]

Indeed the first-block difference is bounded pointwise by
`2 W^#_a Q^# [1_{W^#_a>R}+1_{Q^#>R}]`. Its empirical squared norm has
expectation tending to zero by (F13) and Holder, or by the higher-moment
tail bound `|V|^2 1_{|V|>M}<=|V|^p/M^(p-2)` after splitting the two
factors. The individual moments of `W^#` follow from its envelope and
the `X^#` moment statement in the source theorem. Sum over the two
coordinates and apply Markov. The population version is identical.
Consequently this clipping error also bounds the forcing error by
`2(C_T+Y)||sigma||TV` times its supremum.

Partition the compact data space into finitely many Borel cells of diameter
at most `delta`, and transfer `nu`'s mass in each cell to one point of that
cell. The resulting deterministic finite law `nu^delta` satisfies
`W1(nu,nu^delta)<=delta` and has the same mass. Coupling within the cells
and using the preceding Lipschitz estimate gives

\[
 \sup_{t\le T}\|b_{\nu-\nu_*,R}(t)
               -b_{\nu^\delta-\nu_*,R}(t)\|\le C_{T,Y,R}\delta.
 \tag{F15}
\]

The same bound holds on `E_n`. First choose `R` for (F14), then choose
`delta` for (F15). This proves the required forcing approximation by a
fixed finite list of bounded coordinate instructions and passive queries.
It does not assert total-variation convergence of the quadrature laws.
Constants do not involve the number or weights of the quadrature atoms.

These arguments also prove strong continuity and Bochner measurability
of the uncut forcing: the clipped integrands are continuous on the compact
time/data space into `mathcal H`, and converge uniformly there by the
population version of (F14). Their range is separable, and the uniform norm
bound makes integration against every finite signed measure legitimate.

## 4. Strong multiplier consistency and fixed-program identification

The only finite-program result used is special-data III.F.1-7, with the
contained value extension global-nonlinear A.1. A fixed finite list of
continuous coordinate instructions of at most linear growth, applications
of the same initial action and its transpose, and causal scalar contractions
has joint empirical same-layer `W2` convergence in probability. The metric
for a finite node tuple is its ordinary Euclidean metric. Singular query
Grams are admitted by III.F.5, whose proof adds fresh query noise at a
fixed program, takes the width limit, and then removes that noise. This
does not require a Gram inverse limit. The source-response extension A.2
is needed in the separate source proof, not as an extra assertion that
finite differentiated trajectories already converge.

We record the product principle used twice below. If arrays `z_n,z_n^h`
on the same indices differ by at most `a_h+o_P(1)` in RMS, `a_h->0`,
and `V_n^h` is a fixed-program node with a second-moment limit, then for
bounded Lipschitz `b`, at fixed cutoff `M`,

\[
 {\|[b(z_n)-b(z_n^h)]V_n^h\|_2\over\sqrt n}
 \le \operatorname{Lip}(b)M
          {\|z_n-z_n^h\|_2\over\sqrt n}
       +2\|b\|_\infty
          {\|V_n^h1_{|V_n^h|>M}\|_2\over\sqrt n}.
 \tag{F16}
\]

For a vector-valued bounded multiplier the identical argument applies.
Continuous positive-part cutoffs transfer the tail in (F16) through the
fixed-program W2 limit. For a compact family in population L2, these
tail norms tend to zero uniformly: approximate the compact family by a
finite L2 net and use
`||V1_{|V|>2M}||2<=2||V-W||2+2||W1_{|W|>M}||2`.
For a merely bounded continuous scalar multiplier, first restrict its
arguments to a compact interval; the same argument uses uniform continuity
there. All multipliers below can instead be taken globally Lipschitz.

Let `theta_n^h` be transformed Euler for the reference on a fixed mesh
of maximum step `h`. It starts from the actual finite readout.
The complete B.1 same-root proof applies with `kappa_a=1/2`, and with
HS distance replacing action distance: a rank difference obeys the same
inequality in HS, while the action of a HS difference is bounded by its
HS norm. It gives, on `E_n`, for sufficiently small `h`,

\[
 \sup_{t\le T}\|\theta_n(t)-\theta_n^h(t)\|_{\rm clock,HS,L2}
        \le C_T h.                                             \tag{F17}
\]

Here and below reference-state distance includes its two clocks and the
learned matrix increment. Its readout supremum is bounded separately.
The population reference has the identical Euler estimate. In particular
the full first row is recovered, not only a projection on a new input.

At fixed `R,delta,h`, build tangent Euler along these reference mesh
states, using (F6) and the clipped forcing for `nu^delta-nu_*` at the
preceding node. Expand each learned reference or tangent matrix as its
finite sum of rank-one updates. Every new matrix query then uses the
initialized matrix in its actual orientation plus finitely many scalar
contractions. Every coordinate instruction is continuous with at most
linear growth. For example `phi'(j(X,g))^2 xi` has a bounded multiplying
factor, while `c phi''(Z2) dot z2` has bounded `c` after clipping outside
the already proved readout bound. The clipping of `c` changes no values.
Each `rho_R(w)chi_R(Q)` is bounded. There is no uncut product of two
independent unbounded varying tangent arguments.

The fixed-program theorem therefore identifies the joint deterministic
population mesh law and all its quadratic contractions. Causal empirical
feedback is recovered instruction by instruction. At a scalar step use
`|<u,v>-<u_o,v_o>|<=||u-u_o||||v||+||u_o||||v-v_o||`. At a matrix step
the discrepancy of a recomputed finite rank action and its prescribed
node is a finite sum of scalar contraction discrepancies times nodes of
bounded RMS. At a coordinate product use (F16), taking width to infinity
first and then removing its auxiliary cutoff. Oracle tails are available
from joint W2 convergence of the fixed preceding tuple. Thus actual
empirical coefficients and recomputed nodes have the same limit even
though the coordinate map need not be globally Lipschitz.

The finite initial readout is not discarded in this assertion. One may
construct the deterministic-coefficient oracle with zero limiting readout
and couple the actual fixed recursion to it. The initial readout discrepancy
is its actual RMS, tending to zero, and its coordinate supremum also tends
to zero by the Gaussian union bound. Finite induction with (F16) propagates
that error through every node. This is a comparison at fixed mesh, not a
change to either actual GF or its derivative.

## 5. Removing the time mesh without operator-norm multiplier convergence

Fix `R,delta` temporarily. Denote the population tangent mesh by `v^h`
and the forced solution with this clipped finite-law forcing by `v`.
Their generators have a common operator bound `C_T` by (F9). For each
fixed tangent vector `V`,

\[
 \sup_{t\le T}\|[G(\theta^h(\pi_h t))-G(\theta(t))]V\|
             \longrightarrow0.                                \tag{F18}
\]

Indeed reference clock, HS increment and readout convergence first gives
the forward field and action differences. Every remaining difference
in (F4)-(F6) is a bounded multiplier acting on one fixed L2 field, a
bounded action, a rank pairing, or a bounded finite-rank field. Equation
(F16)'s population proof handles every multiplier. For the evaluation
field use `D_a^2 Q_a`; its change is handled by truncating the fixed
`Q_a`. Strong continuity uniform in time follows by compactness of the
reference path. Bounded operator norms extend (F18) uniformly to compact
sets of `V`, using a finite net.

The set `{v(t):t<=T}` is compact in `mathcal H`. Comparing tangent Euler
with the integral equation on each time cell, (F18), continuity of `v`
and of its forcing make its integrated consistency error tend to zero.
The error recurrence has factor at most `1+C_T h`; its product is at
most `exp(C_T T)`. Therefore

\[
 \sup_{t\le T}\|v^h(t)-v(t)\|\longrightarrow0.                 \tag{F19}
\]

This argument proves consistency on the vectors actually tested; it
does not assert norm convergence of multiplication operators.

It remains to compare actual finite tangents with the finite mesh
proxies. This is a separate step: a finite-program width theorem alone
does not perform it. Let `v_n^h` be the finite mesh from Section 4 and
let `v_n^{R,delta}` solve the actual finite linear equation, with actual
reference generator, but with the clipped finite-law forcing. Its
inhomogeneous defect against the affine interpolant of `v_n^h` is

\[
\begin{split}
 D_{n,h}(t)={}&[G_n(t)-G_n^h(\pi_h t)]v_n^h(\pi_h t)\\
 &+G_n(t)[v_n^h(t)-v_n^h(\pi_h t)]\\
 &+b_{n,R,\delta}(t)-b_{n,R,\delta}^h(\pi_h t).
\end{split}                                                       \tag{F20}
\]

All differences are on the same finite carrier. On `E_n` the operator
bound, (F17), the clipped-forcing Lipschitz bound and the mesh increment
bound control the second and third lines in `L1([0,T];mathcal H_n)` by
`C_T,R,delta h` (with the same conclusion after a fixed-program event
of probability tending to one). The first line is a finite sum of
bounded-action/rank terms and multiplier terms of the form (F16).
For the latter the testing nodes are the mesh tangent components and
their finitely many forward variations, and the reference `Q_a`.

In detail, the first variation of a training hidden feature is
`D_a^2 xi_a`, so its coefficient error is (F16) with test `xi_a^h`.
The upper preactivation adds `(A-A^h)dot h1^h` and
`B^h(H1-H1^h)`, bounded by the action/HS norms and (F17).
The upper backward variation adds a changed bounded gate acting on
`d^h`, and a changed multiplier `c phi''(Z2)` acting on `dot z2^h`.
Both factors in this latter multiplier are bounded; subtract them
separately. In particular `(c-c^h)dot z2^h` uses (F16) with the
identity clipped outside the common readout interval as multiplier.
It uses L2 smallness of `c-c^h`, not a claimed L-infinity smallness.
The reverse variation next adds `(A-A^h)*dot delta2^h` and
`(B^h)*(delta2-delta2^h)`. For its rank block use the two-factor
HS difference inequality, and for the scalar evaluation block use
Cauchy-Schwarz on the finitely many changed L2 representing fields.
The only product in a representing field requiring a tail cutoff
is a changed bounded first gate multiplying `Q_a^h`; it is again
(F16). This list exhausts (F4)-(F6).

Here the order of cutoffs is essential. By (F19) and strong multiplier
continuity, the population testing nodes, along a chosen countable
refining mesh sequence and all its time nodes, form a relatively compact subset of
the appropriate L2 space. For `dot z2`, for example, use HS convergence
of `B^h`, strong convergence of `dot h1^h`, and the bounded continuous
action curve. Thus their L2 tails vanish uniformly as `M->infinity`.
At every separately fixed mesh their finite empirical cutoff moments
converge to the corresponding population moments. Apply (F16) at each
of that mesh's finitely many nodes, multiply by its time-cell length,
and sum. First send width to infinity, then `h->0` at fixed `M`, then
`M->infinity`. This gives

\[
 \lim_{h\downarrow0}\limsup_{n\to\infty}
 \Pr\{1_{E_n}\int_0^T\|D_{n,h}(t)\|_{\mathcal H_n}\,dt>a\}=0
 \quad(a>0).                                                     \tag{F21}
\]

Subtract the two finite linear integral equations and use the actual
generator bound `C_T`, with initial discrepancy zero. Iterating that
inequality bounds their uniform state difference by
`exp(C_T T) integral ||D_n,h||`. This proves strong finite-mesh
approximation of `v_n^{R,delta}`. Finally the same bound compares its
forcing with the original forcing: (F14)-(F15) make that `L1` difference
arbitrarily small, first choosing `R`, then `delta`. This proves capture
for every fixed `nu`, including a nonatomic one, without constructing
any nonlinear perturbed population flow.

The precise state topology is the following. There are fixed finite
programs, indexed by an accuracy `k` (including fixed source cutoff,
data quadrature and time mesh), with population tangent paths `v^[k]`
and finite same-array realizations `v_n^[k]`, such that

\[
 \sup_{t\le T}\|v^{[k]}(t)-v_\sigma(t)\|_{\mathcal H}\to0,
\]
\[
 \lim_{k\to\infty}\limsup_{n\to\infty}
 \Pr\{\sup_{t\le T}\|v_n(t)-v_n^{[k]}(t)\|_{\mathcal H_n}>a\}=0
 \quad(a>0),                                                     \tag{F22}
\]

and at each fixed `k` every finite same-layer node tuple has its joint
W2 limit. The middle tangent in each program is a finite sum of ranks;
its squared HS norm is the sum of products of their two layer Gram
entries. Consequently its Frobenius norm, and its Frobenius pairings
with fixed generated finite-rank tests, converge to their population
HS counterparts. The action of this tangent and of its adjoint on
each finite list of generated test fields is identified by the same
rank expansion and limiting contractions. Passing through (F22)
extends these assertions to the actual tangent.

In particular at any fixed finite list of times and inputs, same-layer
tuples of clocks, readout, raw first-row variations, hidden variations,
and the responses in (F4) converge in W2 with all pairwise contractions.
For products involving a changed bounded gate, uniform L2 tails of the
testing tangent fields follow from (F22) and (F19), and (F16) again
passes the product. No individual-neuron coupling across widths, or
operator-norm comparison between different carriers, is being claimed.
No W2 statement for hidden tangent paths in the coordinate supremum
norm is needed here.

## 6. Passive output observations and uniformity on the circle

The Riesz field representing `e_u` in (F1) is

\[
 \ell_u=\left((u_aD_a\phi'(w\cdot u)Q(u))_{a=1,2},
                \delta^2(u)\otimes H^1(u),H^2(u)\right).
 \tag{F23}
\]

It satisfies `||ell_u||<=C_T` uniformly in `u`, using only bounded gates,
the action bound and `||c||2`. Thus (F22), joint fixed-program second
moments for the reference fields and finite tangent fields, and their
rank pairings prove prediction-derivative convergence at each fixed
time/input. The same argument is uniform in time at a fixed input:
the reference and tangent are approximated uniformly in their stated
Hilbert norms; multiplication against a fixed proxy uses (F16).
At a fixed proxy all remaining time dependence lies in finitely many
continuous interpolated coefficients/coordinate instructions, so a
finite time net and their compact-family L2 tails give uniform
convergence. An equivalent route is the time equicontinuity argument
in the next paragraph.

For clarity the output fields have adequate time regularity without a
hidden tangent higher-moment assumption. Reference `Q(u)` is uniformly
L2 Lipschitz in time: differentiate
`Q=A*delta2`, `delta2=c phi'(Z2)` and
`Z2=A phi(w.u)` and use the compact-time raw velocity and `c` supremum
bounds. Multipliers in (F23) involving `w` are handled by clipping
the reference `Q(u)` and using its tails from (F13). Hence for every
`a>0`, the probability that the modulus
`sup_{|t-s|<=h,u}||ell_n(t,u)-ell_n(s,u)||` exceeds `a` tends to zero
as `h->0`, in the `limsup_n` sense. The tangent itself is equicontinuous
in `mathcal H_n` in probability since (F8), the generator bound and
`sup_t||b_n(t)||=O_P(1)` give `sup_t||v_n'(t)||=O_P(1)`. These two
facts prove the corresponding scalar time equicontinuity of
`<ell_n(t,u),v_n(t)>`.

Whole-circle regularity is a separate estimate. Parametrize
`u(alpha)=(cos alpha,sin alpha)`. Strong curve differentiation gives

\[
 \partial_\alpha H^1=\phi'(w\cdot u)(w\cdot u'),\quad
 \partial_\alpha Z^2=A\partial_\alpha H^1,
\quad
 \partial_\alpha Q=A^*[c\phi''(Z^2)\partial_\alpha Z^2].
 \tag{F24}
\]

The last two derivatives have L2 norms bounded by `C_T||w||2`.
Differentiate the first field in (F23). Its only additional unbounded
product is

\[
 u_aD_a\phi''(w\cdot u)(w\cdot u')Q(u).
 \tag{F25}
\]

Its L2 norm is bounded by twice that of `|w|Q(u)`, supplied by (F13).
This is a strong derivative, not only a formal product rule. Equation
(F24) first makes `Q(alpha)` a strongly C1 L2 curve and, by integrating
its derivative coordinatewise using Fubini, gives almost-everywhere
absolutely continuous coordinate representatives. In the gate difference
quotient the mean value bound is `2|w| |Q(alpha)|`; the source envelope
`|w| sup_alpha |Q(alpha)|` belongs to L2. Dominated convergence therefore
passes that quotient to (F25). The other term is a bounded multiplier
times the strongly convergent difference quotient of `Q`. The same
envelope gives continuity of the resulting derivative where needed;
in particular it justifies the H1 assertion and its fundamental theorem.
The other first-field terms are bounded by `||Q||2` and
`||partial_alpha Q||2`. Differentiating the other two fields in
(F23) uses the rank product rule and (F24); `||c||infinity` suffices.
Consequently

\[
 \|\ell\|_{H^1([0,2\pi];\mathcal H)}\le C_T
 \quad\hbox{in the population},\qquad
 \sup_{t\le T}\|\ell_n(t,\cdot)\|_{H^1([0,2\pi];\mathcal H_n)}
          =O_P(1).                                             \tag{F26}
\]

The finite assertion follows by integrating the squared estimate and
using (F13) for the supremum in time. There is no claimed Gaussian
distribution or Gaussian tail for (F25). For any absolutely continuous
Hilbert-valued field, the fundamental theorem of calculus and
Cauchy-Schwarz give
`||ell_alpha-ell_beta||<=|alpha-beta|^(1/2)||partial_alpha ell||L2`.
Apply this to (F26). The derivative predictors consequently have a
uniform-in-time circle modulus `O_P(1)|alpha-beta|^(1/2)`, because
`sup_t||v_n(t)||=O_P(1)`. Their population counterpart obeys the
deterministic version.

Choose a finite circle net and finite time net. At every point of their
product the scalar convergence follows from Section 5 and (F23).
A finite union bound gives convergence on the net. The two moduli just
proved bound the interpolation error to the whole compact time/circle
domain. First let width tend to infinity at fixed nets, and then refine
the nets. This proves (F10).

## 7. Scope and limit order

The order is finite-width right differentiation first; then, for each
fixed target accuracy, fix a source cutoff, deterministic data quadrature
and auxiliary time mesh; take width to infinity; remove these auxiliary
approximations using (F14)-(F22). There is no interchange of a derivative
with an unconstructed population law-to-flow map. All physical horizons
are separately fixed, with no restriction near initialization.

The proof supplies actual finite-GF derivative capture, the compatible
clock/HS/L2 state identification, and passive whole-circle observations.
It proves no raw-GD derivative theorem, no finite-contamination remainder,
no sampling CLT, and no uniform-in-time finite-width convergence. The
uniform population propagator is a distinct claim established, if valid,
by the complete argument in `PROPAGATOR.md`. Transport approximation in
Section 3 is used only to construct a fixed Borel forcing integral; it
is not a claimed transport bound for a nonlinear perturbed flow.

<!-- END FINITE_CAPTURE.md -->
