# Route local: an explicit fitting basin and finite physical state length

Status: frozen independent analytical candidate, 2026-09-16. This file was
completed before sharing its mathematical contents with the supervising agent.
It is an internally derived result, not established library material or an
independently reviewed theorem.

## Scope and contract

The object is the exact canonical order-one population closure, with the full
five-coordinate lower dictionary, three-coordinate upper dictionary, prescribed
Cholesky normalization and ridge `eta=1/4096`, correlated lower marks, initial
state `w=g,c=0,M=D`, actual transpose `M^T`, and unhalved probability-weighted
squared loss in physical time. No particle approximation, frozen-feature
substitution, neural-width assertion or closure-order limit is used.

Scientific inputs were restricted to `docs/NOTATION.md` and
`docs/global_nonlinear.md` lines 12084–12410, 13177–13469, 13470–13710 and
15258–15392. These supplied the characteristic state, its metric and equations,
the exact order-one dictionary and core contraction, and fixed-order global
existence. No other study or agent's route was consulted. The research and
rigorous-mathematics skills, research-contract reference and adversarial-audit
reference were read. No experiments were run and no missing input is needed
for the result below.

The result concerns an explicit open family of variable-angle opposite-label
two-atom laws with sufficiently small nonzero labels. It proves all-time
convergence of the complete closure state, a current-state transverse gradient
inequality, local fitting geometry with infinitely many neutral directions,
and finite length in the physical state metric. It does not resolve unit-label
global convergence or stability for a continuum of input directions.

## 1. Exact state, metric and derivative

Write `b=L_1^{-1}psi_1`, `beta=L_2^{-1}psi_2`, and use the two fixed canonical
mark probability spaces. The characteristic state is

\[
 S=(v,c,M),\qquad w=g+v,
 \qquad
 \mathcal H=L^2(\lambda_1;\mathbb R^2)\oplus
             L^2(\lambda_2)\oplus\mathbb R^{3\times5}.
\]

Its physical norm is
`||delta S||_H^2=E_1|delta v|^2+E_2|delta c|^2+||delta M||_F^2`.
The initial state is `S_0=(0,0,D)`. Expectations always preserve the full joint
correlations of the fixed marks and current variables. Put

\[
 \begin{split}
 h(u)&=\tanh(w\cdot u),& a(u)&=E_1[bh(u)],\\
 H(u)&=\tanh(\beta^TMa(u)),& f(u)&=E_2[cH(u)],\\
 d(u)&=E_2[\beta c(1-H(u)^2)],&
 q(u)&=b^TM^Td(u).
 \end{split}                                                    \tag{1}
\]

The maps `U_1 z=b^Tz`, `U_2 z=beta^Tz` and their adjoints are contractions,
and `||D||_op<=2`, by the cited exact normalization and contraction results.
In particular

\[
 |a(u)|\le1,\qquad |d(u)|\le\|c\|_2,\qquad
 \|q(u)\|_2\le\|M\|_{\rm op}\|c\|_2.                 \tag{2}
\]

For a state increment the exact derivative is

\[
 Df(u)[\delta S]
 =E_1[q(u)(1-h(u)^2)u\cdot\delta v]
   +E_2[H(u)\delta c]+d(u)^T\delta M a(u).              \tag{3}
\]

This is a continuously differentiable map from `H` to `R`. To check the only
potential issue with this topology, Taylor's bound for tanh gives a remainder
at most `C |delta v|^2` in the finite vector `E_1[b tanh(w.u)]`; bounded marks
make its integral `O(||delta v||_2^2)`. This vector map has derivative continuous
in operator norm, because the gate difference is bounded in `L2` by
`2||delta v||_2`. All later nonlinearities act on finite vectors with bounded
upper marks; their products with `c` are controlled by `||c||_2`. These facts
also show that (3), as an `H` gradient, is locally Lipschitz on bounded state
sets. They do not require a false differentiability assertion for an arbitrary
Nemytskii map from `L2` to `L2`.

For two equally weighted data points define

\[
 F(S)=2^{-1/2}(f(u_1),f(u_2)),\qquad
 Y=2^{-1/2}(y_1,y_2),\qquad R(S)=F(S)-Y,
 \qquad \mathcal L(S)=|R(S)|^2.
\]

Let `J=DF`. The exact equations of the source are

\[
 S'=-2J^*R=-\nabla_{\mathcal H}\mathcal L,
 \qquad \mathcal L'=-\|S'\|_{\mathcal H}^2.             \tag{4}
\]

The readout part of `J` is the operator

\[
 T(S)c_*=2^{-1/2}(E_2[c_*H(u_1)],E_2[c_*H(u_2)]).
\]

It depends only on `(v,M)`, and

\[
 JJ^*\succeq TT^*,\qquad
 (TT^*)_{ij}=\tfrac12E_2[H(u_i)H(u_j)].                 \tag{5}
\]

Every factor of two here uses the unhalved loss and the physical metric.

## 2. Explicit initialization positivity

Use the exact canonical scalar constants

\[
 v_0=E\tanh^2G,\quad
 \tau=E\tanh^2(\sqrt{v_0}G),\quad \alpha=1-\tau,
 \quad \eta=1/4096.
\]

Let `g~N(0,1)` and `zeta~N(0,tau)` be independent, and set

\[
 h=\tanh g,\qquad t=\tanh(\zeta+\alpha h),\qquad
 k=E[ht],\quad \ell=E[t^2],\quad
 b_0=E[1-t^2].
\]

All `v_0,tau,alpha,b_0` are strictly positive, and `k>0`: the function
`m(x)=E_zeta tanh(zeta+alpha x)` is odd, strictly increasing and zero at zero,
so `h m(h)>0` almost surely except at `h=0`. The exact lower raw Gram splits,
apart from its constant, into two identical blocks

\[
 B=\begin{pmatrix}v_0&k\\ k&\ell\end{pmatrix}
\]

on the coordinate pairs `(h_i,t_i)`. The upper raw Gram has diagonal
`(1,tau,tau)`. This is a description of the exact block entries, not a change
of the required feature ordering or normalization.

The initialized raw contraction row for upper feature `tanh xi_i`, restricted
to `(h_i,t_i)`, is precisely

\[
 (\alpha v_0,\ \alpha k+\tau b_0),                     \tag{6}
\]

by the two terms of the supplied core formula (H3.1). All its other entries
are zero. Define

\[
 \Delta=(v_0+\eta)(\ell+\eta)-k^2>0,
\]
\[
 \gamma=
 \frac{\alpha v_0\{v_0(\ell+\eta)-k^2\}
       +(\alpha k+\tau b_0)k\eta}
      {(\tau+\eta)\Delta}>0.                          \tag{7}
\]

Positivity follows from `k^2<=v_0 ell` and strictly positive `eta`.
This constant uses the required ridge, including its effect on both lower
and upper normalized dictionaries.

Indeed, with `m(u)=E_1[psi_1 tanh(g.u)]`, the initial preactivation is exactly

\[
 \psi_2^T(G_2+\eta I)^{-1}C(G_1+\eta I)^{-1}m(u).       \tag{8}
\]

For `u=e_i`, the only nonzero block of `m(u)` is `(v_0,k)^T` in coordinate
pair `i`. Multiplication of (6) by

\[
 (B+\eta I)^{-1}\binom{v_0}{k}
 =\frac1\Delta\binom{v_0(\ell+\eta)-k^2}{k\eta}
\]

proves

\[
 H_0(e_i)=\tanh(\gamma Z_i),\qquad
 Z_i=\tanh\xi_i,
 \qquad \xi_1,\xi_2\ \text{independent }N(0,v_0).
\]

Thus, putting the explicitly defined Gaussian integral

\[
 m_0=E\tanh^2(\gamma\tanh(\sqrt{v_0}G))>0,             \tag{9}
\]

independence and oddness give `T_0T_0^*=(m_0/2)I_2` at the pair `(e_1,e_2)`.
No empirical Gram estimate or numerical nondegeneracy assumption is involved.

Now take

\[
 u_1=e_1,\quad u_2=u_\theta=(\cos\theta,\sin\theta),
 \qquad |u_\theta-e_2|\le\frac{\sqrt{m_0}}4.             \tag{10}
\]

This is an explicit interval of positive width around `pi/2`, and contains
nonorthogonal inputs on both sides of `pi/2`. At initialization, contraction
of the two feature maps, `||D||<=2`, and Gaussian isotropy give

\[
 \|H_0(u)-H_0(e_2)\|_2
 \le2\|\tanh(g\cdot u)-\tanh(g\cdot e_2)\|_2
 \le2|u-e_2|.
\]

Only the second row of `T_0` changes, so its operator difference is at most
`sqrt(2)|u_theta-e_2|`. Applying the reverse triangle inequality to `T_0^*z`
for every unit `z in R2` proves

\[
 T_0T_0^*\succeq\lambda I_2,
 \qquad \lambda:=m_0/8>0.                              \tag{11}
\]

The entire interval (10) shares this one lower bound.

## 3. Basin theorem with proved initialization hypotheses

**Theorem.** Keep the exact canonical order-one initialization and constants
(7)–(11). For any angle satisfying (10), consider the probability law

\[
 \mu_{\theta,\varepsilon}
 =\tfrac12\delta_{(e_1,+\varepsilon)}
  +\tfrac12\delta_{(u_\theta,-\varepsilon)},\qquad
 0<\varepsilon\le\frac{\lambda}{8\sqrt5}
                  =\frac{m_0}{64\sqrt5}.               \tag{12}
\]

Its exact population closure exists for every physical time, stays in a fixed
neighborhood of initialization, and converges to a fitting state `S_infty`
with finite physical length. More precisely, set

\[
 \rho=\frac{\sqrt\lambda}{2\sqrt5},\qquad
 \kappa=\lambda/4.
\]

On the entire physical ball `||S-S_0||_H<rho` one has the current-state
inequality

\[
 TT^*\succeq\kappa I_2,
 \qquad \|\nabla\mathcal L\|_{\mathcal H}^2
       \ge4\kappa\mathcal L=\lambda\mathcal L.          \tag{13}
\]

Along the prescribed initialized trajectory,

\[
 \mathcal L(t)\le\varepsilon^2e^{-\lambda t},\qquad
 \int_t^\infty\|S'(s)\|_{\mathcal H}\,ds
 \le\frac{2\varepsilon}{\sqrt\lambda}e^{-\lambda t/2},  \tag{14}
\]
\[
 \|S(t)-S_0\|_{\mathcal H}\le\rho/2,
 \qquad
 \|S(t)-S_\infty\|_{\mathcal H}
 \le\frac{2\varepsilon}{\sqrt\lambda}e^{-\lambda t/2}.  \tag{15}
\]

The moving coordinates in fact converge in the characteristic topology
`L_infty` for `w-g,c`, with finite `M`, as well as in the physical metric.
Consequently their full current joint laws converge under the coupling by
their original marks, and their limit fits the two labels exactly.

**Proof.** At a state `S`, subtraction using `a_0` and `D` yields

\[
 \|H(u)-H_0(u)\|_2
 \le\|(M-D)a(u)+D(a(u)-a_0(u))\|
 \le\|M-D\|_F+2\|v\|_2
 \le\sqrt5\|S-S_0\|_{\mathcal H}.                     \tag{16}
\]

The weighted sum of its two squared row bounds controls
`||T-T_0||_op`. Hence the least singular value of `T` is at least
`sqrt(lambda)-sqrt(5)rho=sqrt(lambda)/2`. This proves the first part of
(13); (4)–(5) give the second part exactly.

Within this ball, (4) and (13) imply
`L'<=-4 kappa L`. Also, whenever `L>0`,

\[
 \|S'\|\ge2\sqrt\kappa\sqrt{\mathcal L},\qquad
 \|S'\|=\frac{-\mathcal L'}{\|S'\|}
 \le\frac{-\mathcal L'}{2\sqrt\kappa\sqrt{\mathcal L}}.
\]

Integration between times `a,b` before a possible exit gives

\[
 \int_a^b\|S'\|\,dt
 \le\frac{\sqrt{\mathcal L(a)}-\sqrt{\mathcal L(b)}}{\sqrt\kappa}
 \le\frac{\sqrt{\mathcal L(a)}}{\sqrt\kappa}.           \tag{17}
\]

If the loss reaches zero, all three exact velocities vanish, and uniqueness
extends the stationary state; the same estimates apply. Initially
`L(0)=epsilon^2`. Thus before any first exit, (12) and (17) bound the traveled
length by `2 epsilon/sqrt(lambda)<=rho/2`. A first exit at distance `rho`
is impossible by continuity. The fixed-order characteristic existence result
from the allowed sources applies to this bounded-label two-atom probability
law on every finite interval, so the trajectory is global and the argument
holds for all times. Taking `b` to infinity proves (14), makes the trajectory
Cauchy in the complete physical Hilbert space, and proves (15).

For the stronger characteristic convergence, (1)–(2) and the exact equations
give, with `B_1=ess sup|b|<infty`,

\[
 \|c'\|_\infty\le2\sqrt{\mathcal L},\quad
 \|M'\|_F\le2\|c\|_2\sqrt{\mathcal L},\quad
 \|v'\|_\infty
 \le2B_1\|M\|_{\rm op}\|c\|_2\sqrt{\mathcal L}.
\]

The factors other than `sqrt(L)` are bounded by (15), and `sqrt(L)` is
integrable by (14). These velocities therefore have finite integrals in the
claimed norms. Continuity of (1), or (3), gives `F(S_infty)=Y`. This also
justifies convergence of the full joint population laws, without replacing
them by independent marginals. QED.

## 4. Geometry, neutral directions and a current-state fitting certificate

The following statements hold throughout the same ball, and hence at every
state reached in the theorem. They describe the fitting set itself, rather
than assuming isolated minimizers or positive definite full-state Hessians.

For a current state write `G_c=TT^*`. The explicit readout correction

\[
 c_{\rm fit}=c-T^*G_c^{-1}R(S)                          \tag{18}
\]

with `v,M` unchanged fits both data points exactly. Its physical distance is

\[
 \|c_{\rm fit}-c\|_2^2
   =R(S)^TG_c^{-1}R(S)
   \le\kappa^{-1}\mathcal L(S).                       \tag{19}
\]

This is a certificate computed entirely from the current state. The corrected
state need not lie in the same ball for arbitrary states near its boundary;
the fitting statement and distance bound themselves do not need that extra
claim. For states sufficiently close to the trajectory's limiting state,
the correction remains in the ball.

The fitting set inside the ball is a `C1` Hilbert submanifold of codimension
two. Here is a direct local graph construction, without an unstated compactness
or implicit-function hypothesis. Fix a fitting state `S_*`, write `h=(v,M)`,
and let `T_*` be its readout operator and
`P_*=T_*^*(T_*T_*^*)^{-1}` its bounded right inverse. Put `N=ker T_*`.
For `h` close to `h_*`, the two-by-two matrix `A(h)=T(h)P_*` is invertible:
it equals the identity at `h_*` and its difference has operator norm below
one nearby, where the inverse is the convergent geometric series. Every
nearby fitting state has the unique representation

\[
 c=k+P_*A(h)^{-1}\{Y-T(h)k\},\qquad k\in N.            \tag{20}
\]

Indeed `T(h)c=Y`, while decomposition into `N` and `ran P_*` is unique since
`T_*P_*=I`. Conversely the equation `T(h)c=Y` solves uniquely for the
`ran P_*` coordinate of any such decomposition. The maps in (20) are `C1`
by the finite-moment differentiability checked after (3). This proves the
claimed graph structure. Its tangent and physical normal spaces at `S_*` are

\[
 T_{S_*}\mathcal Z=\ker J_*,\qquad
 (T_{S_*}\mathcal Z)^\perp=\operatorname{ran}J_*^*.      \tag{21}
\]

The first identity follows by differentiating the fitting equation and the
graph; the second follows because `J_*` is onto, and
`I-J_*^*(J_*J_*^*)^{-1}J_*` is the orthogonal projection onto its kernel.
At a fitting state the gradient has derivative

\[
 D(\nabla\mathcal L)(S_*)=2J_*^*J_*;                   \tag{22}
\]

the term differentiating `J^*` is zero because `R(S_*)=0`. More explicitly,
local Lipschitz continuity of `J` and
`R(S_*+delta)=J_*delta+o(||delta||)` give (22) directly. The operator has
exactly two positive eigenvalues, equal to those of `2J_*J_*^*`, both at
least `2 kappa`. Its remaining directions form precisely the tangent kernel
(21). Thus the linearized flow contracts the two normal modes and has
infinitely many neutral tangent modes. The finite-length conclusion (14)
controls the nonlinear drift along these neutral directions; positive full
state curvature is neither true nor needed.

For completeness, on the physical ball (3) implies the uniform derivative
bound

\[
 \|J(S)\|\le
 C_\rho:=\sqrt{1+\rho^2\{1+(2+\rho)^2\}}.
\]

Integrating along any segment inside the ball yields
`sqrt(L(S))<=C_rho ||S-S_fit||` for every fitting state in the ball. Together
with (19), this identifies the loss locally as a squared transverse distance,
with explicit constants. It does not make loss control all neutral coordinates.

## 5. The system has actual middle-feature motion

The theorem evolves all three blocks. At the central angle `theta=pi/2`, one
can also rule out exact accidental freezing of the middle matrix.
Put `F_i=tanh(gamma Z_i)`, `s_i=1-F_i^2`, where the independent `Z_i` are
as above. Initially `c'=epsilon(F_1-F_2)` and `v'=M'=0`. The two vectors
`a_i=a_0(e_i)` are nonzero and have disjoint coordinate supports even in the
prescribed interleaved Cholesky ordering, so `a_1.a_2=0`. The coefficient of
the first odd upper coordinate in `d'_1` is

\[
 (d'_1)_1=\frac{\varepsilon}{\sqrt{\tau+\eta}}
 E[Z_1F_1s_1]>0.                                      \tag{23}
\]

Here the term involving `F_2` integrates to zero by its oddness and
independence. Differentiating the exact middle equation at initialization
gives

\[
 M''(0)=\varepsilon(d'_1a_1^T-d'_2a_2^T),\qquad
 M''(0)a_1=\varepsilon\|a_1\|^2d'_1\ne0.               \tag{24}
\]

Bounded differentiation under the Gaussian integrals makes this expression
continuous in the second input direction. It remains nonzero on some open
angular neighborhood of `pi/2`, which contains nonorthogonal members of (10).
The existence of that smaller neighborhood is rigorous; no numerical width
is claimed for it. Hidden motion is of order `epsilon^2` at onset, so this
observation does not turn the perturbative basin theorem into a large-motion
feature-learning result.

## 6. Adversarial audit and unresolved scope

* **Initialization and normalization:** Equations (6)–(9) retain the reverse
  response contribution `tau b_0`, both ridge factors and the original joint
  lower marks. Dropping any of those terms gives a different initialization.
* **Transposition and metric:** Equations (1), (3) and (4) use one `M` and its
  actual transpose, the two population `L2` metrics, the coefficient Frobenius
  metric and physical time. The rate in (14) belongs to the unhalved loss.
* **Full-state convergence:** A square-integrable speed alone would not imply
  finite length. Estimate (17) supplies the missing `L1` speed bound using
  current transverse coercivity, and the exit argument proves this coercivity
  remains available.
* **Neutral directions:** The fitting set is not isolated; its tangent kernel
  is infinite-dimensional. The argument proves convergence to some fitting
  state, not to a prescribed state or unique minimizer.
* **Nuisance explanation:** Readout separability and small labels are the main
  reason the basin can be certified. This is a rigorous perturbative theorem
  for the full nonlinear closure, compatible with readout-dominated behavior.
  Formula (24) proves nonzero hidden motion but does not exclude small-motion
  descriptions as an approximation.
* **Angle uniformity:** The explicit interval (10) has positive width and
  includes variable nonorthogonal angles, but is centered on an orthogonal
  pair. No claim is made for every distinct pair, near-coincident directions,
  or the particular unit-label arc family elsewhere in the source.
* **Label magnitude:** Positivity of `m_0` proves the bound (12) admits nonzero
  labels without a numerical assertion about its practical size. Unit labels
  are outside this theorem; rescaling physical time does not remove that gap.
* **Population versus width:** The theorem concerns the exact order-one
  closure itself. The source's short-horizon identification of a hierarchy
  limit with neural population dynamics supplies no all-time neural-width
  or closure-accuracy consequence here.
* **State-law topology:** The common canonical carrier is used only for proof
  and the physical length. The operational state is still the same pair of
  current joint laws and finite matrix. No past trajectory is needed for the
  correction (18), the equations, or a restart.

There is no identified internal proof gap in (7)–(22), subject to ordinary
independent checking of the calculations. The major remaining scientific
gap is extension beyond the explicit small-label basin. A global unit-label
claim cannot be inferred from this local result.
