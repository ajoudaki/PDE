# Three inputs: a state-only exponential capture certificate and its open-family gap

Independent bounded route, frozen 2026-09-16. Internal analytical result;
no experiment, external convergence theorem, other route's current work,
shared-file edit, or Git-index operation was used.

**Outcome.** There is a complete strict capture test at a reached state,
with an explicit current-state potential and convergence of the full
canonical population. The test is open in the three directions and in the
reached state. Consequently **one captured generic unit-label triple would
give a genuine open nonsymmetric three-residual family**. This route does
not prove that such a triple enters capture from canonical initialization.
It therefore supplies neither a nonempty initialized open-family theorem
nor the primary theorem for every generic triple.

The capture argument uses physical path length and improves the interface
of `generic3_metric_route.md`: its test does not involve the reached
readout norm. This is not a claim that its sufficient region contains the
entire region of that different certificate.

## 1. Contract and exact equations

The data are three directions `u_i in S1`, with equal masses `1/3`, no
coincidence or antipodality, and labels `y=(1,1,-1)`. Physical inputs are
`sqrt(2)u_i`. Keep order one, ridge `eta=1/4096`, the full joint Gaussian
marks, canonical inverse-Cholesky normalization, prescribed initialization
`(w,c,M)=(g,0,D)`, and the actual transpose of the same evolving `M`.
All trainable blocks evolve. There are no small labels or frozen hidden
features in the theorem.

The only scientific inputs read were `docs/NOTATION.md`,
`docs/global_nonlinear.md` C.4.7.9 and C.4.7.10 B/C.1/D.3, and the five
study files in the source record below. The two required skills were
`investigate-conjectures` and `solve-math-rigorously`. Their research-contract,
adversarial-audit, and bounded-proof-search process references were also read.

On the fixed canonical carriers let `X=(w,M,c)` have physical norm

\[
 \|\delta X\|^2=E_1|\delta w|^2+\|\delta M\|_F^2+E_2|\delta c|^2.
 \tag{1}
\]

The saved populations remain the joint laws `Law(b_1,g,w)` and
`Law(b_2,c)`. For input `u_i`, write

\[
\begin{aligned}
 a_i&=E_1[b_1\tanh(w\cdot u_i)],&
 H_i&=\tanh(b_2^TMa_i),& f_i&=E_2[cH_i],\\
 d_i&=E_2[b_2c(1-H_i^2)],&
 q_i&=b_1^TM^Td_i,& r_i&=f_i-y_i.
\end{aligned}
\]

The exact physical equations are

\[
 \dot w=-\frac23\sum_i r_i\operatorname{sech}^2(w\cdot u_i)q_i u_i,
 \quad \dot M=-\frac23\sum_i r_i d_i a_i^T,
 \quad \dot c=-\frac23\sum_i r_i H_i.
 \tag{2}
\]

Give data space the metric `|z|_mu^2=(1/3)sum_i z_i^2`, and set

\[
 \mathcal L=|r|_\mu^2,\quad R=\sqrt{\mathcal L},\qquad
 (Tv)_i=E_2[vH_i],\quad T^*z=\tfrac13\sum_i z_iH_i.
\]

The readout Gram `TT*` has ordinary matrix `(E[H_iH_j])/3` in this
equal-weight metric. With `J` the derivative of the prediction vector in
`(w,M)`, differentiating (2) gives

\[
 \dot r=-2Kr,\quad K=TT^*+JJ^*,\qquad
 \dot{\mathcal L}=-4\langle r,Kr\rangle_\mu=-\|\dot X\|^2.
 \tag{3}
\]

All coefficients are actual current-state contractions. Canonical ridge
normalization gives contraction maps `v -> b_l^T v` and their adjoints.
In particular `|a_i|<=1`, `|d_i|<=||c||_2`, and
`||q_i||_2<=||M||op ||c||_2`.

The cited exact initialized coefficient map has the form

\[
 H_{i,0}=\tanh\{Z_1\varphi(u_{i,1})+Z_2\varphi(u_{i,2})\},
 \tag{4}
\]

where `Z_i=tanh(xi_i)`, the `xi_i` are independent `N(0,v)` under the
separate upper law, and `varphi` is odd and strictly increasing with the
exact reverse-response term and prescribed ridge retained. The cubic
Vandermonde argument in `three_four_input_extension.md` proves positive
initial Gram for every triple under consideration. It is used only for
that initial-rank fact, not for rank persistence.

## 2. A strict current-state capture theorem

At any reached finite time `t_0`, calculate

\[
 R_0=\sqrt{\mathcal L(X_0)},\quad m_0=\|M_0\|_{\rm op},\quad
 \lambda_0=\lambda_{\min}(T_0T_0^*),\quad
 B_0=\sqrt{1+m_0^2}.
\]

Here `X_0=X(t_0)` is a snapshot; these are not a new initialization rule.
Assume

\[
 \lambda_0>0,\qquad R_0<\frac{\lambda_0}{4B_0}.
 \tag{5}
\]

Define the current-state potential, with no saved clock or path integral,

\[
 \Phi(X)=\mathcal L(X)\bigl(1+E_2[c^2]\bigr).
 \tag{6}
\]

Then for all `t>=t_0`, the complete canonical continuation satisfies

\[
 \lambda_{\min}(T_tT_t^*)\ge\lambda_0/4,
 \qquad \mathcal L(t)\le\mathcal L(t_0)e^{-\lambda_0(t-t_0)},
 \tag{7}
\]

\[
 \dot\Phi(t)\le-\frac{\lambda_0}{2}\Phi(t),\qquad
 \mathcal L(t)\le\Phi(t)
 \le\Phi(t_0)e^{-\lambda_0(t-t_0)/2},
 \tag{8}
\]

\[
 \int_t^\infty\|\dot X(s)\|\,ds
 \le\frac{2R(t)}{\sqrt{\lambda_0}}.
 \tag{9}
\]

The full state converges to a fitting endpoint in the physical metric,
in the bounded-increment characteristic topology, and in the corresponding
same-mark joint-law `W2` topology. In particular all three independent
residuals converge to zero. This is a local capture theorem for the
original unit labels, not a theorem with small labels.

### Proof: physical length closes the evolving-feature bound

Put

\[
 \rho=\frac{\sqrt{\lambda_0}}{2B_0},\qquad
 \kappa=\lambda_0/4.
\]

For any current state `X` within physical distance `rho` of the reached
snapshot, first subtract the lower coefficient fields, using contraction
and the Lipschitz property of tanh:

\[
 |a_X(u)-a_0(u)|\le\|w-w_0\|_2.
\]

Next use the exact split

\[
 Ma_X-M_0a_0=(M-M_0)a_X+M_0(a_X-a_0).
\]

Upper contraction and tanh Lipschitzness therefore give, for every `u`,

\[
 \|H_X(u)-H_0(u)\|_2
 \le\|M-M_0\|_F+m_0\|w-w_0\|_2
 \le B_0\|X-X_0\|\le\sqrt{\lambda_0}/2.
 \tag{10}
\]

Weighted Cauchy--Schwarz gives the same bound on
`||T_X*-T_0*||op`. Thus

\[
 \|T_X^*z\|_2\ge\tfrac12\sqrt{\lambda_0}|z|_\mu,
 \qquad K_X\succeq T_XT_X^*\succeq\kappa I.
 \tag{11}
\]

For as long as the trajectory stays in this ball, (3) gives
`L'<=-4 kappa L`. More is needed than energy dissipation. If `R>0`,

\[
 \|\dot X\|\ge2\sqrt\kappa R,\qquad
 -\dot R=\frac{\|\dot X\|^2}{2R}
 \ge\sqrt\kappa\|\dot X\|.
 \tag{12}
\]

Consequently its physical length up to any time before first exit is at
most

\[
 \frac{R_0-R(t)}{\sqrt\kappa}
 \le\frac{2R_0}{\sqrt{\lambda_0}}<\rho.
\]

The last strict inequality is exactly (5), so first exit is impossible.
The source theorem supplies global finite-time continuation of the exact
fixed-order flow, so this proves (7). If `R` reaches zero, (2) makes all
velocities zero and uniqueness fixes the state thereafter; this handles
the division by `R`. Integrating (12) to infinity proves (9).

This proof measures all moving blocks in the fixed physical metric.
The reference hidden fields in (10) are comparison values only; no hidden
equation is frozen or replaced.

### Proof: the complete potential derivative

Set `Q=E_2[c^2]` to avoid confusing it with the lower backward field.
The readout equation gives

\[
 \dot Q=-4\langle f,r\rangle_\mu
 \le4\|c\|_2 R\le2R(1+Q).
 \tag{13}
\]

The first inequality uses `||f||_mu<=||c||_2`, since `|H_i|<=1`.
The second is `2||c||_2<=1+||c||_2^2`. Combining the actual derivative
of both factors of (6), rather than holding its weight fixed, yields

\[
 \dot\Phi
 =\dot{\mathcal L}(1+Q)+\mathcal L\dot Q
 \le(-\lambda_0+2R)\Phi
 \le-\tfrac12\lambda_0\Phi.
\]

Indeed `R<=R_0<lambda_0/(4B_0)<=lambda_0/4`. This proves (8).
The factor `1+Q` is an actual state-dependent weight whose derivative
has been included. It is not a changing training metric.

### Full-state endpoint and stronger tails

Let `C_*=||c_0||_2+rho`, `m_*=m_0+rho`, and
`B_1=(sum_j ||b_{1,j}||_infty^2)^(1/2)`. Staying in the physical ball
gives `||c||_2<=C_*`, `||M||op<=m_*`. From (2),

\[
 \|\dot c\|_\infty\le2R,\quad
 \|\dot M\|_F\le2C_*R,\quad
 \|\dot w\|_\infty\le2B_1m_*C_*R.
 \tag{14}
\]

The exponential bound started again at any `t>=t_0` gives
`int_t^infty R(s)ds<=2R(t)/lambda_0`. Integrating (14) proves

\[
\begin{aligned}
 \|c(t)-c_\infty\|_\infty&\le4R(t)/\lambda_0,\\
 \|M(t)-M_\infty\|_F&\le4C_*R(t)/\lambda_0,\\
 \|w(t)-w_\infty\|_\infty&\le4B_1m_*C_*R(t)/\lambda_0.
\end{aligned}
 \tag{15}
\]

The reached initial increments are bounded by the canonical finite-time
existence theorem. Completeness gives bounded endpoint increments as well.
The same lower and upper contraction subtractions as in (10) show hidden
field convergence uniformly over `u in S1` in `L2`. Splitting
`E[cH]-E[c_infty H_infty]` proves uniform prediction convergence.
Equation (7) identifies its three training values with the unit labels.
Coupling unchanged frozen marks and converging moving coordinates makes
the squared joint-law `W2` distances at most their squared `L2` distances.

## 3. Strict openness: precisely what one initialized seed would buy

Let `U=(u_1,u_2,u_3)` denote an ordered triple, retaining the same labels
and masses. Suppose a particular generic triple `U_*`, started at the
canonical initialization, satisfies (5) at a finite time `T`.
Then there is an open neighborhood `V` of `U_*` in `(S1)^3`, consisting
of distinct non-antipodal triples, on which every canonical trajectory
satisfies (5) at that same `T`. The potential (6) has the same formula
throughout the neighborhood. After shrinking `V`, put
`lambda_* = lambda_min(T_{U_*}(T)T_{U_*}(T)*)`; then for every `U in V`,

\[
 \mathcal L_U(t)\le\mathcal L_U(T)e^{-(\lambda_*/2)(t-T)},
 \quad
 \Phi_U(t)\le\Phi_U(T)e^{-(\lambda_*/4)(t-T)},\quad t\ge T.
 \tag{16}
\]

All three Gram modes remain positive. In particular this would be a
three-independent-residual theorem on an open set, which contains triples
with no exact dictionary symmetry.

Here are the required finite-time continuity details. The canonical source
bounds, independent of the input triple, give through `T`

\[
 \|c\|_\infty\le2T,\quad \|M\|op\le2+2T^2,\quad
 \|w\|_2\le\sqrt2+4T^2+2T^4.
 \tag{17}
\]

For two states in these bounds and two unit inputs, lower contraction
gives

\[
 |a_X(u)-a_{\widetilde X}(v)|
 \le\|w-\widetilde w\|_2+\|\widetilde w\|_2|u-v|.
\]

Upper contraction, bounded readout, and the Lipschitz gate give the same
type of bound for `H`, `f`, and `d`. The `d` subtraction is explicitly
`E[b_2(c-c_tilde) gate]+E[b_2 c_tilde(gate-gate_tilde)]`; the latter
uses the supremum readout bound in (17), rather than an invalid `L2`
algebra estimate. For the lower velocity, subtract `q` first in `L2`;
the remaining lower-gate difference is multiplied by the unchanged
`q_tilde`, with
`||q_tilde||infty<=B_1 ||M_tilde||op ||c_tilde||_2`.
It is therefore controlled by
`2(||w-w_tilde||_2+||w_tilde||_2 |u-v|)` times this finite envelope.
Subtracting residuals and unit directions in (2) introduces only the
same bounds. The middle equation is a finite product subtraction.

It follows that a finite `A_T`, depending only on `T` and fixed feature
envelopes, obeys

\[
 \|F_U(X)-F_V(\widetilde X)\|
 \le A_T\bigl(\|X-\widetilde X\|+max_i|u_i-v_i|\bigr)
 \tag{18}
\]

along these bounded canonical paths. Integrate their difference from the
same initialization and use the elementary integrating factor to obtain

\[
 \sup_{t\le T}\|X_U(t)-X_V(t)\|
 \le(e^{A_TT}-1)\max_i|u_i-v_i|.
 \tag{19}
\]

If desired enlarge `A_T` to be positive. This does not assert input
continuity in the supremum norm of `w-g`; Gaussian `g` is unbounded and
only its finite `L2` norm was used in the input subtraction.

The preceding subtractions imply continuity of the finite Gram and loss
at `T`; the operator norm of `M` is continuous as well. The function

\[
 \lambda_{\min}(TT^*)-4\sqrt{1+\|M\|op^2}\sqrt{\mathcal L}
\]

is thus continuous and strictly positive at the hypothesized seed.
This proves openness of (5), and continuity of `lambda_min` gives the
common lower bound `lambda_*/2` used in (16).

There is also an all-time exponential envelope for this same state-only
potential, conditional on that seed. The exact identity

\[
 \frac d{dt}\|c\|_2^2
 =4\langle y-f,f\rangle_\mu
 =1-4\|f-y/2\|_\mu^2\le1
\]

gives `Q(t)<=t` from the prescribed zero readout, and energy gives
`L(t)<=1`. Hence `Phi(t)<=1+T` for `t<=T`. Combining with (16),

\[
 \Phi_U(t)\le(1+T)e^{\lambda_*T/4}e^{-\lambda_*t/4},
 \qquad t\ge0,\quad U\in V.
 \tag{20}
\]

This is a global exponential envelope, with a finite prefactor; the
pointwise differential inequality (8) was proved only from capture time.
No prefix monotonicity of (6) is asserted.

**The unproved premise must remain visible:** no `U_*` satisfying (5)
from the canonical unit-label initialization has been established in
this route. A strict conditional set is not proof that its initialized
preimage is nonempty.

## 4. Why splitting a scalar reference does not prove the premise

Oddness holds at every state. Absorb the labels into directions
`v_i=y_i u_i`, so fitting the original labels is exactly fitting target
`+1` at all three `v_i`. Conjugating the Gram by the diagonal label
matrix preserves its eigenvalues.

First, if two signed directions approach one another and the state stays
in a bounded physical/characteristic neighborhood, their upper fields
obey `||H(v_1)-H(v_2)||_2<=C|v_1-v_2|`. Testing the ordinary Gram
matrix divided by three on `(1,-1,0)/sqrt2` gives

\[
 \lambda_{\min}(TT^*)
 \le\tfrac16\|H(v_1)-H(v_2)\|_2^2
 \le C^2|v_1-v_2|^2/6.
 \tag{21}
\]

Thus the capture threshold deteriorates quadratically or faster under
duplicate or compatible-antipodal splitting. A small geometric change
alone gives no inequality comparing the new residual to this threshold.

For three signed directions coalescing at one scalar reference, there is
a sharper fourth-order degeneration. Parameterize
`v_i(epsilon)=u(theta_0+epsilon a_i)` with three fixed distinct real
`a_i`. At any fixed reached scalar-reference state and in a sufficiently
bounded neighborhood, the angular field `theta -> H(u(theta))` is twice
continuously differentiable into `L2`, with a bounded second derivative.
To check this, `w=g+bounded` has finite fourth moment; differentiating the
lower tanh twice produces terms bounded by `2|w|^2+|w|`; bounded marks
and finite `M` pass these derivatives through the two coefficient
integrals and the upper tanh. The same argument gives local uniform
bounds in a bounded-increment characteristic neighborhood.

Choose a Euclidean unit vector `z in R3` solving
`sum_i z_i=sum_i z_i a_i=0`, possible since these are two independent
linear conditions. Banach-valued Taylor expansion then gives

\[
 \left\|\sum_i z_iH(v_i(\epsilon))\right\|_2\le C\epsilon^2,
 \qquad
 \lambda_{\min}(TT^*)\le C^2\epsilon^4/3.
 \tag{22}
\]

At a fitted scalar endpoint `X_*`, let `F(theta)=f_{X_*}(u(theta))`
and `F(theta_0)=1`. If `F'(theta_0)!=0`, the residual at that unchanged
reference state is of order `|epsilon|`. If `F'(theta_0)=0` but
`F''(theta_0)!=0`, it is of order `epsilon^2`: componentwise,

\[
 F(\theta_0+\epsilon a_i)-1
 =\epsilon a_iF'(\theta_0)
  +\tfrac12\epsilon^2a_i^2F''(\theta_0)+o(\epsilon^2).
 \tag{23}
\]

At least one `a_i` is nonzero, so the relevant residual norm has a
strictly positive leading coefficient in either case. Equations
(22)--(23) make (5) fail at this reference state for all sufficiently
small nonzero `epsilon`. This statement is conditional on the displayed
nonzero derivative; neither its sign nor nonvanishing at every trained
scalar endpoint was assumed or proved here.

This is an obstruction to direct perturbative certification, **not** a
counterexample to training the split triple. Slow additional learning
could change its state substantially before capture. Proving that stage
would require a new argument.

The corresponding equilibrium issue is precise. At the unsplit compatible
scalar data, the prediction derivative has rank one and the fitted-loss
Hessian has at most one positive normal mode. A generic split triple has
three independent modes; the new small normal modes vanish in the limit
above. Thus a uniform three-normal-mode stability bound cannot be inherited
from that scalar endpoint. Ordinary persistence of the scalar attracting
direction does not prove fitting of the two new constraints. No external
normal-hyperbolicity theorem was invoked without checking this rank change.

Nor do the known dictionary symmetries immediately supply a different
three-point scalar seed. The proved signed-permutation group has order
eight, so a transitive orbit has size dividing eight and cannot have size
three. This rules out that particular transitive-symmetry construction;
it does not rule out an accidental scalar reduction, a different symmetry,
or a nonscalar exact three-point solution. No such solution was established
in this bounded route.

## 5. Frozen claim and adversarial audit

| Claim | Status | Exact bridge or limitation |
|---|---|---|
| Capture criterion (5), full-state convergence | Proved conditionally | A strict inequality at an actual reached state |
| Current-state potential (6), full derivative (8) | Proved in capture | Uses all of the weight derivative (13) |
| Strict openness and uniform family bounds | Proved conditionally | Requires one canonical captured generic seed |
| Global envelope (20) | Proved conditionally | Prefix uses only energy and the exact readout bound |
| Initialization itself meets (5) | False for this sufficient test | See the bound below |
| A nonempty initialized generic unit-label open family | Open | No seed entry proof |
| Every canonical generic unit-label triple is captured | Open | Stronger than the missing seed premise |
| Scalar splitting automatically gives capture | Not justified | Rank loss (21)--(22), residual mismatch (23) |
| Primary universal exponential theorem | Not established | No all-time global coercivity or initialized capture theorem |

Indeed at canonical initialization `R_0=1`, while
`lambda_0<=tr(T_0T_0*)/3<1/3`, since every upper tanh has square strictly
less than one. Thus `lambda_0/(4sqrt(1+||D||op^2))<1/12<1`; (5)
cannot hold there. Its utility is as a reached-state certificate.

The strongest unresolved objection is that loss and feature conditioning
could deteriorate together in a way preventing (5). Initial Gram rank,
representability by a bounded readout, existence at every finite time,
and finite dissipated energy do not exclude this. The conditional theorem
does not replace that missing mechanism with continuity or a symmetry
limit. A positive answer for one generic initialized triple would resolve
the nonemptiness bottleneck and give the stated open family, but would
still not resolve the user's universal target.

Internal checks completed: all `1/3` and physical-time factors; the
readout Gram's data metric; both inequalities in (12); strict first exit;
zero-loss continuation; the complete derivative in (13); endpoint norms;
the input continuity estimate without a Gaussian supremum bound; the
`1/6` and `1/3` Rayleigh factors in (21)--(22); and the distinction between
pointwise exponential differential decay and the global envelope (20).
These are author-side checks, not an independent or promotion review.

## Source identities

SHA-256 values recorded after reading. The large canonical source was read
only on the assigned sections; its whole-file hash identifies that version.

```text
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c  docs/global_nonlinear.md
33ce17ba0be80836ba13862eb3ba76b579cabfe2bba1cb4f076be4e2f9de9ec7  all_angles_result.md
3bbf89335a49f9b9c97e4aab8ace450f62d16fc2febe59eaa068b61fcf1dd5e7  scalar_margin_extension.md
4bdb878378518455ca4e0cf7ea2ded8281d056b7aec98cef36c5ebf337c47b9a  arbitrary_pair_local.md
59c93c8756167fef609df326fd1633266c73d526e54e61aadc8f4b05d75791d9  three_four_input_extension.md
c089546aa52eae67f4e9ee75621766d2429475729822d9bcbcd5f32086ffd801  generic3_metric_route.md
a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de  /etc/codex/skills/investigate-conjectures/SKILL.md
9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7  /etc/codex/skills/solve-math-rigorously/SKILL.md
```

## Post-candidate check: root-supplied obstruction to global monotonicity

This section was added after Sections 1--5 were independently frozen at
SHA-256
`20365f97e79e4eab7362a1785478180cb764d0428f9d1ad524d496b10518c353`.
The root then supplied the near-contradiction construction checked below.
Its diagnostic numerical observation is not an input to this proof or
to any positive result above. The following argument is entirely exact.

The candidate (6) **is not globally nonincreasing from canonical
initialization for every generic unit-label triple**. In fact there is an
open set of admissible generic triples on which it exceeds its initial
value at a common finite time.

Start with the limiting, deliberately nongeneric law

\[
 \mu_*=\tfrac13\delta_{(e_1,+1)}+
        \tfrac13\delta_{(e_2,+1)}+
        \tfrac13\delta_{(e_1,-1)}.
\]

Its exact loss at any state is

\[
 \mathcal L_*=\tfrac23+\tfrac23 f(e_1)^2
                         +\tfrac13(f(e_2)-1)^2.
 \tag{24}
\]

Let `P=diag(-1,1)`, and let `S_1,S_2` reverse the first coordinate
block of the lower and upper initialized marks. The exact sign-preserving
dictionary isometry has normalized sign matrices `J_1,J_2` and acts by

\[
 (w,M,c)\longmapsto(Pw\circ S_1,\ J_2MJ_1,\ c\circ S_2).
\]

It fixes canonical initialization and sends predictions to `f(Pu)`.
This is the plus-readout version of the exact reflection symmetry in the
allowed sources. Equation (24) is invariant under it: `e_2` is fixed,
while input oddness changes `f(e_1)` to `-f(e_1)` inside its square.
The physical metric is invariant as well. Uniqueness therefore preserves
the isometry's fixed states, and along this trajectory

\[
 f(e_1)=f(-e_1)=-f(e_1),\qquad f(e_1)=0.
\]

Writing `F=f(e_2)`, the complete gradient, including every hidden block,
thus reduces to

\[
 \dot X=\tfrac23(1-F)\nabla F.
 \tag{25}
\]

The scalar normalized-readout theorem applies to `F=E[cH(e_2)]`
with its exact initialized contrast
`C_0=E[H_0(e_2)^2]>0`. Its proof gives `K=||grad F||^2>=C_0`,
`0<=F<1`, and, with the physical factor in (25),

\[
 1-F(t)\le e^{-(2C_0/3)t}.
\]

Take the explicit finite time `T=3 log(4)/(2 C_0)`. Then `F(T)>=3/4`.
At every state, `F^2<=Q E[H(e_2)^2]<=Q`, where `Q=E[c^2]`.
Equation (24) also gives `L_*>=2/3`. Hence

\[
 \Phi_*(T)\ge\tfrac23(1+F(T)^2)
             \ge\tfrac23(1+9/16)=25/24>1=\Phi_*(0).
 \tag{26}
\]

The finite-time data-continuity proof (17)--(19) does not require distinct
directions or positive Gram rank, so it also applies at this limiting law.
Consequently every sufficiently close ordered triple with labels
`(+1,+1,-1)` has `Phi(T)>49/48>1`. Intersect that neighborhood with the
open set of distinct non-antipodal triples. The intersection is nonempty
(move the third direction a sufficiently small nonzero angle away from
`e_1`) and contains triples without an exact dictionary symmetry.
All have the prescribed canonical `Phi(0)=1`. Thus a global monotonicity
claim for (6) is disproved on actual generic initialized trajectories.

This obstruction does not contradict (8): the latter starts only after
the strict capture test. Nor does it disprove an exponential bound with
a prefactor, a different current-state potential, or the primary universal
convergence conjecture. It confirms why the local qualification on this
particular potential is necessary.
