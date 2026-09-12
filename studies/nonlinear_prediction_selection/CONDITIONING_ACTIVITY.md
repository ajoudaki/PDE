# One-atom conditioning and nonlinear hidden-activity episode

Second-round candidate, 2026-09-12. The first-round
`ROUTE_CONDITIONING.md` is preserved unchanged. This note proves the
conditioning and activity component conditional on existence of the stated
constrained evolution. It does not construct that evolution, identify it with
the changed-law singular limit, or prove the common-primitive finite capture
premise used in the final transfer statement.

The new input is the coordinator's complete `ROUTE_RESIDUAL_CLOCK.md`.
The fixed-readout contrast below was supplied in the second-round assignment;
it is not presented as an independent second discovery. No continuation or
geometric route was read, and no external input, experiment, or Git call was
used. The scientific model, notation, original initialization, and unhalved
loss are unchanged from the first report.

## 1. Statement and the exact conditional premise

Write `u_alpha=(cos alpha,sin alpha)` and set

\[
 I=[\pi/4-1/1216,\pi/4+1/1216],\qquad
 Y_0=[3/8,5/8],\qquad
 \nu_{\alpha,y}=\delta_{(\sqrt2u_\alpha,y)}.
 \tag{1.1}
\]

The forward equations use normalized input `u=x/sqrt(2)`. The parameter
rectangle `I times Y0` is compact, and its interior is an open family in both
position and label. Every added input is nonorthogonal to both reference
inputs and distinct from them modulo antipodes.

Let `theta_dagger=(w_dagger,A_dagger,c_dagger)` be the actual fitted reference
endpoint from C.4.5, with `A=A0+K` and raw Hilbert increment space

\[
 \mathcal H=L^2(\Omega_1;\mathbb R^2)
   \oplus\mathcal S_2(H_1,H_2)\oplus L^2(\Omega_2).
\]

Let `g_theta(u)` denote the raw gradient of the scalar prediction, and put

\[
 G_\theta=(g_\theta(e_1),g_\theta(e_2)),\quad
 M_\theta=G_\theta^*G_\theta,\quad
 \Pi_\theta=I-G_\theta M_\theta^{-1}G_\theta^*.
 \tag{1.2}
\]

The only dynamical premise for the population conclusion is the following.
There is a common `tau_ex>0` such that, for every `(alpha,y)` in (1.1), an
existing raw-continuous curve on `[0,tau_ex]` starts at `theta_dagger` and
satisfies the strong integral equation

\[
 \theta'=V_{\alpha,y}(\theta)
   :=-2(f_\theta(u_\alpha)-y)\Pi_\theta g_\theta(u_\alpha).
 \tag{1.3}
\]

The equation is required only in the local region where `M_theta` is
invertible; the estimates below prove that the chosen episode stays there.
The source-regular, bounded-readout evolution contemplated by the coordinator
is more than sufficient for this premise. No new reached-state Gaussian
estimate is needed for the activity implication: the proved endpoint L4
query envelope and raw continuity give the quantitative local comparisons.

A common existence interval is explicit because separately positive local
existence times for individual parameters do not by themselves imply a
uniform positive minimum. If the constructed flow is available only separately
for each law, the conclusions below hold per law with a possibly smaller
time; a uniform `tau0` requires the common interval just stated. No uniqueness
or continuous dependence on the law is additionally assumed for this
activity argument; every curve satisfying (1.3) obeys the same bounds.

There are positive constants `tau0`, `eta_R`, and `eta_H`, independent of
`epsilon`, width, and `(alpha,y)` in (1.1), such that these existing curves
satisfy

\[
 f_{\theta(\tau)}(e_1)=1,\quad f_{\theta(\tau)}(e_2)=-1,
 \qquad 0\le\tau\le\tau_0,
 \tag{1.4}
\]

\[
 (f_\dagger(u_\alpha)-y)^2
   -(f_{\theta(\tau_0)}(u_\alpha)-y)^2\ge\eta_R>0,
 \tag{1.5}
\]

\[
 J_{2,\alpha,y}(\tau_0):={1\over3}\sum_{i=1}^3
 \|H^2_{\theta(\tau_0)}(v_i)-H^2_\dagger(v_i)\|_2^2
 \ge\eta_H>0,\quad (v_1,v_2,v_3)=(e_1,e_2,u_\alpha).
 \tag{1.6}
\]

This is a paired second-hidden-activation displacement, with the same
canonical neuron coordinate at the two states. It is neither a parameter
norm nor a distance between separately chosen marginal couplings. It does
not assert first-hidden-layer displacement.

The predictor in (1.5) is the actual nonlinear constrained predictor on this
finite interval. No frozen-kernel or initial-velocity trajectory substitutes
for it. The constants can be very small, but their strict positivity is
proved without numerical evaluation.

## 2. Endpoint conditioning, with a complete proof

The supplied C.4.5–C.4.6 facts used here are

\[
 \|A_\dagger\|\le M:=2+\sqrt{10},\quad
 \|c_\dagger\|_2\le C:=\sqrt{10},\quad
 \|c_\dagger\|_\infty\le H:=10,\quad
 \|w_\dagger\|_2\le W:=\sqrt2+\sqrt{10}.
 \tag{2.1}
\]

The endpoint predictor is 76-Lipschitz, vanishes at
`(e1+e2)/sqrt(2)`, and fits `(1,-1)`. Thus, on (1.1),

\[
 |f_\dagger(u_\alpha)|\le76/1216=1/16,
 \qquad 5/16\le y-f_\dagger(u_\alpha)\le11/16.
 \tag{2.2}
\]

In particular the added-law endpoint risk is at least `25/256`, even though
its contribution to the mixture risk is only `epsilon` times that number.

C.4.6.S40–S44 supplies one nonnegative random envelope `N`, with finite
`C_*`, such that on the reference feature segment

\[
 \|N\|_p\le C_*\sqrt p\ (p\ge2),\quad
 \sup_s|X_a(s)|\le5N,\quad
 F(w_a(s))=F(g_a)+X_a(s),\quad F'(z)=\cosh^2z,
 \tag{2.3}
\]

where `g1,g2` are independent standard normals. It also gives
`||Q_dagger(u)||_4<=L4:=2C_*` uniformly over every deterministic circle
input. Its countable-source construction and Fubini supply the simultaneous
active-clock bounds in (2.3). Independence of `N` and `g` is not asserted.

Here is the endpoint first-feature independence argument in full. Fix
`v in R2` with nonzero coordinates. Markov's inequality with
`p=(R/(eC_*))^2>=2` gives

\[
 \Pr(N>R)\le\exp[-R^2/(e^2C_*^2)].
\]

The Gaussian density gives

\[
 \Pr\{|g-rv|_\infty\le1\}
    \ge {2\over\pi}\exp[-(r|v|+\sqrt2)^2/2].
\]

For all sufficiently large `r` this exceeds `Pr(N>r^2)`, so their box
intersected with `{N<=r^2}` has positive probability. On that event put
`rho=min(|v1|,|v2|)/2`; for large `r`, `|g_a|>=rho r`. The minimum of
`F'` on `[g_a-1,g_a+1]` is at least `exp(2(|g_a|-1))/4>5r^2`.
Monotonicity of `F` in (2.3) therefore gives

\[
 \sup_s|w_a(s)-g_a|
    \le20r^2e^{-2(|g_a|-1)}\le20e^2r^2e^{-2\rho r}\longrightarrow0.
 \tag{2.4}
\]

If a finite nonantipodal list `u1,...,um` satisfied
`sum a_j tanh(w_dagger.u_j)=0` almost surely, choose such a `v` also
avoiding all lines `v.u_j=0`. On the preceding positive-probability events,
the features tend uniformly to `sign(v.u_j)`. Hence

\[
                   \sum_j a_j\operatorname{sign}(v\cdot u_j)=0.
 \tag{2.5}
\]

Cross the line perpendicular to any `u_k` on the circle of `v` directions.
The nonantipodal condition means no other sign changes there. Choose points
on both sides with nonzero coordinates, also when the crossing is on an axis.
Subtracting (2.5) gives `2a_k=0` up to orientation. Thus all `a_k=0`.
The features are linearly independent.

At the endpoint define

\[
 H^1(u)=\tanh(w_\dagger\cdot u),\quad Z^2(u)=A_\dagger H^1(u),
 \quad H^2(u)=\tanh Z^2(u),\quad
 \delta(u)=c_\dagger\operatorname{sech}^2Z^2(u),\quad
 Q(u)=A_\dagger^*\delta(u).
\]

The readout is nonzero since `<c_dagger,H2(e1)>=1`. Because `Z2(u)`
is finite almost surely and its gate is strictly positive, every `delta(u)`
is nonzero in L2. The raw gradient, at this or any admissible state, is

\[
 g_\theta(u)=\big(u\operatorname{sech}^2(w\cdot u)Q(u),
                    \delta(u)\otimes H^1(u),\ H^2(u)\big).
 \tag{2.6}
\]

For a finite list, if `lambda_H` is its first-feature Gram minimum eigenvalue,
then

\[
 \left\|\sum_i a_i\delta_i\otimes H_i^1\right\|_{HS}^2
    \ge\lambda_H\sum_i a_i^2\|\delta_i\|_2^2.
 \tag{2.7}
\]

Indeed at each second-layer coordinate apply the first-feature Gram
inequality to `sum_i a_i delta_i(omega2)H_i^1` and integrate. This also
identifies the integral with the tensor's Hilbert–Schmidt norm. Thus the
middle gradient blocks, hidden gradient blocks and full gradients are
independent. No injectivity of the trained action is assumed.

The first-feature Gram is continuous in the input list by the L2 Lipschitz
bound for tanh. The fields `delta(u)` are L2-continuous: first pass input
continuity through `w_dagger`, tanh and the bounded action, then use the
bounded fixed readout in (2.1). Their nonzero L2 norms therefore have a
positive minimum on the present compact input set. Define

\[
 \kappa:=\min_{\alpha\in I}\lambda_{\min}
     \big(\langle H^1(v_i),H^1(v_j)\rangle\big)_{i,j=1}^3
       \ \min_{\alpha\in I,\,i\le3}\|\delta(v_i)\|_2^2>0.
 \tag{2.8}
\]

Continuity of the minimum eigenvalue follows from the Rayleigh formula,
`|lambda_min(B)-lambda_min(D)|<=||B-D||`; a continuous positive function
on a compact set has positive minimum. This proves every positivity step
in (2.8). It is a precisely defined endpoint constant, not an evaluated
numerical lower bound.

Consequently the endpoint three-input middle Gram is at least `kappa I`.
The full anchor Gram `M_dagger` is at least `kappa I`. Let

\[
 d_\alpha=\Pi_\dagger g_\dagger(u_\alpha),\quad
 \beta_\alpha=M_\dagger^{-1}G_\dagger^*g_\dagger(u_\alpha),\quad
 t_\alpha=(-\beta_{\alpha,1},-\beta_{\alpha,2},1).
 \tag{2.9}
\]

Since `d=sum_i t_i g_dagger(v_i)` and `|t|>=1`, (2.7) implies

\[
 \|d_\alpha\|^2\ge\|d_{\alpha,H}\|^2
       \ge\|d_{\alpha,K}\|_{HS}^2\ge\kappa.
 \tag{2.10}
\]

The hidden block `H` consists of the first row and middle increment; the
`K` subscript means only the middle increment. The upper gradient bound is

\[
 \|g_\dagger(u)\|\le L_0:=\sqrt{1+C^2(1+M^2)}<17.
\]

Therefore `||d_alpha||<=L0`, `||G_dagger||<=G0:=sqrt(2)L0`, and

\[
 |t_\alpha|\le T_0:=\sqrt{1+2L_0^4/\kappa^2}.
 \tag{2.11}
\]

## 3. Quantitative gradient continuity from raw distance and endpoint L4 tails

This paragraph verifies input continuity and state continuity together. Put
`d=||theta-theta_dagger||_H`, `h=|u-v|`, `rho=d+h<=1`. Here `A-A_dagger`
is measured in HS norm, hence also bounded in operator norm. Use endpoint
quantities at `v` as fixed factors. Successive subtraction gives

\[
 \|Z^1_\theta(u)-Z^1_\dagger(v)\|_2\le a_1\rho,
 \quad\|H^1_\theta(u)-H^1_\dagger(v)\|_2\le a_1\rho,
 \quad a_1=1+W,
\]

\[
 \|Z^2_\theta(u)-Z^2_\dagger(v)\|_2,
 \ \|H^2_\theta(u)-H^2_\dagger(v)\|_2\le a_2\rho,
 \quad a_2=1+Ma_1,
\]

\[
 \|\delta_\theta(u)-\delta_\dagger(v)\|_2\le a_\delta\rho,
 \quad a_\delta=1+2Ha_2,
\]

\[
 \|Q_\theta(u)-Q_\dagger(v)\|_2\le a_Q\rho,
 \quad a_Q=C+1+Ma_\delta.
 \tag{3.1}
\]

For the backward product split it as
`(c-c_dagger)phi'(Ztheta)+c_dagger[phi'(Ztheta)-phi'(Zdagger)]`.
This uses the bounded endpoint readout, not an unproved L-infinity smallness
of the evolving readout difference. For the adjoint split use the current
backward field, whose L2 norm is at most `C+1`, in the changed-action term.

The only additional row product is a changed first gate times the fixed
endpoint `Q_dagger(v)`. For gates `b=phi'(z)-phi'(z0)`,
`|b|<=min(1,2|z-z0|)` implies

\[
 \|b\|_4\le\sqrt2\|z-z_0\|_2^{1/2},\qquad
 \|bQ_\dagger(v)\|_2\le\sqrt{2a_1}L_4\rho^{1/2}.
 \tag{3.2}
\]

This is Holder's inequality and the proved endpoint L4 bound. It does not
multiply two uncontrolled L2 increments. Also
`||Q_theta(u)||2<=(M+1)(C+1)=:Q1`. Subtracting the explicit input vector
in the row gradient, the middle rank factors and the final hidden value gives

\[
 \|g_\theta(u)-g_\dagger(v)\|\le C_g\rho^{1/2},
\]

\[
 C_g=Q_1+a_Q+a_\delta+Ca_1+a_2+\sqrt{2a_1}L_4.
 \tag{3.3}
\]

The raw Hilbert norm is bounded above here by the sum of its three component
norms. This proves uniform endpoint state/input continuity, including that
of `beta_alpha`, `t_alpha`, and `d_alpha` in (2.9). No input derivative of a
query is required.

At fixed `u`, prediction subtraction also gives

\[
 |f_\theta(u)-f_\dagger(u)|\le C_f d,
 \qquad C_f=1+Ca_2,
 \tag{3.4}
\]

uniformly on the circle. The scalar differentiation formula (2.6) along
strongly C1 raw curves follows from the strong L2 chain rule: for a fixed
direction the tanh difference quotient is dominated by its L2 direction,
and the error of replacing a C1 increment by that direction is controlled
by the one-Lipschitz activation. Differentiating the bounded action product
and the scalar readout pairing gives the three blocks in (2.6). Bounded
multiplier convergence against fixed L2 fields proves their continuity.
Explicitly, if bounded multipliers `b_k` converge in probability to `b`,
split a fixed `q in L2` at `|q|=R`. The bounded part of
`||(b_k-b)q||2` tends to zero by bounded convergence in probability; its
tail is at most `2 sup_k||b_k||infty ||q 1_(|q|>R)||2`. Let `k` grow
first and then `R` grow. Applying this fact successively to the fixed-state
backward and row factors proves continuity at any state, without requiring
an L4 bound at that state.
An ambient Frechet derivative of an L2-valued hidden map is not used.

For explicit projector estimates set

\[
 a_G=\sqrt2 C_g,\quad G_1=G_0+a_G,\quad
 a_M=(2G_0+a_G)a_G.
\]

Then `||G_theta-G_dagger||<=a_G sqrt(d)` and
`||M_theta-M_dagger||<=a_M sqrt(d)`. If
`a_M sqrt(d)<=kappa/2`, the Rayleigh formula gives
`M_theta>=kappa I/2`, and the inverse identity yields

\[
 \|M_\theta^{-1}-M_\dagger^{-1}\|
       \le(2a_M/\kappa^2)\sqrt d.
\]

Expanding the three changed factors in `G M^-1 G*` proves

\[
 \|\Pi_\theta-\Pi_\dagger\|\le C_\Pi\sqrt d,
 \quad C_\Pi={2a_GG_1\over\kappa}
       +{2G_0a_MG_1\over\kappa^2}+{G_0a_G\over\kappa}.
 \tag{3.5}
\]

Writing `d_theta,alpha=Pi_theta g_theta(u_alpha)`, it follows that

\[
 \|d_{\theta,\alpha}-d_\alpha\|\le C_d\sqrt d,
 \qquad C_d=C_g+C_\Pi L_0.
 \tag{3.6}
\]

All constants are uniform over (1.1).

## 4. The hidden contrast and its derivative along the reached path

Keep the endpoint readout and coefficients fixed during the episode:

\[
 O_\alpha(\theta)=\sum_{i=1}^3 t_{\alpha,i}
                 \langle c_\dagger,H^2_\theta(v_i)\rangle.
 \tag{4.1}
\]

This functional depends only on hidden parameters. Its raw gradient is
`o_alpha(theta)=(sum_i t_i h_i^fixed(theta),0)`, where `h_i^fixed` is the
first-row/middle portion of (2.6) with the readout set to `c_dagger`.
The proof is the strong curve chain rule just given, with a fixed bounded
readout in the scalar pairing. In particular

\[
 o_\alpha(\theta_\dagger)=(d_{\alpha,H},0),\qquad
 \|o_\alpha(\theta)-o_\alpha(\theta_\dagger)\|
       \le C_o\sqrt d,\quad C_o=\sqrt3T_0 C_g.
 \tag{4.2}
\]

For the last inequality apply (3.3) to the auxiliary state `(w,A,c_dagger)`
and sum its three hidden-gradient differences using
`sum|t_i|<=sqrt(3)|t|`. Thus derivative continuity of this hidden contrast
uses only raw distance and fixed endpoint L4 tails, even if the evolved
query field is known only through the source-regular flow premise.

The field in (1.3) is continuous on the neighborhood under consideration:
(3.3) and its fixed-state bounded-multiplier proof give gradient continuity,
and (3.5) gives inverse/projector continuity. A raw-continuous solution of
the strong integral equation therefore has a continuous raw derivative.
Its two hidden maps are strongly C1 by the chain rule above. Consequently

\[
 {d\over d\tau}O_\alpha(\theta(\tau))
       =\langle o_\alpha(\theta(\tau)),V_{\alpha,y}(\theta(\tau))\rangle.
 \tag{4.3}
\]

At the endpoint, writing `r_dagger=f_dagger(u_alpha)-y`, (2.2) and (2.10)
give the uniform strictly positive value

\[
 O_\alpha'(0)=-2r_\dagger\|d_{\alpha,H}\|^2\ge5\kappa/8.
 \tag{4.4}
\]

This explicitly checks hidden representation motion. A nonzero hidden
parameter block is only the input to the identity, not its conclusion.

For a quantitative derivative modulus put

\[
 L_1=\sqrt{1+(C+1)^2(1+(M+1)^2)},\quad
 R_1=C+1+5/8,\quad V_1=2R_1L_1.
\]

On the unit raw ball and the invertible-Gram region, `||g_theta(u)||<=L1`,
`|f_theta(u_alpha)-y|<=R1`, and `||V_alpha,y(theta)||<=V1`, because
an orthogonal projector has norm at most one. Equations (3.4) and (3.6) give

\[
 \|V_{\alpha,y}(\theta)-V_{\alpha,y}(\theta_\dagger)\|
      \le C_V\sqrt d,
 \quad C_V=2C_fL_1+(11/8)C_d.
\]

Use (4.2), `||o_alpha(theta_dagger)||<=L0`, and the last bound in (4.3):

\[
 |O_\alpha'(\theta)-O_\alpha'(\theta_\dagger)|
       \le A_O\sqrt d,
 \qquad A_O=C_oV_1+L_0C_V.
 \tag{4.5}
\]

Here `O'(theta)` means its derivative in the actual field (1.3), not a
derivative of a frozen trajectory. This estimate supplies uniform
continuity along all the reached paths in the family.

## 5. A uniform, finite nonlinear episode

Choose the following positive raw radius:

\[
 \rho_0=\min\left\{1,\left({\kappa\over2a_M}\right)^2,
             {\kappa\over4C_d^2},\ {5\over32C_f},
             \left({5\kappa\over16A_O}\right)^2\right\}>0.
 \tag{5.1}
\]

Every denominator is finite and positive by its displayed definition. Let

\[
 \tau_0=\min\{\tau_{ex}/2,\rho_0/(2V_1)\}>0.
 \tag{5.2}
\]

Before a possible first exit from the raw ball of radius `rho0`, the
velocity bound `V1` gives `||theta(tau)-theta_dagger||<=V1 tau`.
If that first exit occurred by `tau0`, this distance would be at most
`rho0/2`, a contradiction. Thus all paths stay in the ball through `tau0`.
The Gram is at least `kappa I/2` there. This is a first-exit estimate for the
existing nonlinear equation, not a conclusion from the initial linear term.

Since `G_theta^*Pi_theta=0`, the chain rule applied to the two anchors proves
(1.4). The choices in (5.1), (2.2), and (3.6) give throughout the interval

\[
 |r(\tau)|\ge5/32,\qquad r(\tau)<0,\qquad
 \|d_{\theta(\tau),\alpha}\|^2\ge\kappa/4.
 \tag{5.3}
\]

The exact added prediction and risk identities are

\[
 f_\theta(u_\alpha)'=-2r\|d_{\theta,\alpha}\|^2,\qquad
 (r^2)'=-4r^2\|d_{\theta,\alpha}\|^2.
 \tag{5.4}
\]

They retain every moving hidden field and the recomputed projector. Integrating
(5.3)–(5.4) gives (1.5) with

\[
 \eta_R={25\kappa\over1024}\tau_0>0,
 \qquad f_{\theta(\tau_0)}(u_\alpha)-f_\dagger(u_\alpha)
                        \ge {5\kappa\over64}\tau_0>0.
 \tag{5.5}
\]

By (4.4)–(4.5) and (5.1), `O_alpha'(theta(tau))>=gamma_O:=5kappa/16`.
Hence `Delta O_alpha>=gamma_O tau` for `0<=tau<=tau0`. Cauchy–Schwarz,
first in the second population and then in the three coefficients, yields

\[
 |\Delta O_\alpha|^2
 \le\|c_\dagger\|_2^2|t_\alpha|^2
             \sum_{i=1}^3\|\Delta H_i^2\|_2^2
 \le30T_0^2 J_{2,\alpha,y}(\tau).
 \tag{5.6}
\]

Thus (1.6) holds with the explicit positive constant

\[
 \eta_H={\gamma_O^2\tau_0^2\over30T_0^2}>0.
 \tag{5.7}
\]

This finite episode has actual upper hidden activation displacement. Its
proof uses derivative continuity of a scalar hidden contrast to retain a
strict sign over a finite interval; it does not extrapolate the initial
velocity as the finite trajectory. The interval and margins have no
`epsilon` dependence.

The whole-circle map is
`P_(alpha,y)(tau,sqrt(2)u)=<c(tau),tanh(A(tau)tanh(w(tau).u))>`.
It is jointly continuous in time and input and has a uniformly bounded input
Lipschitz constant on this episode, since it is bounded by
`||c||2 ||A||op ||w||2`. Equation (3.4) gives a uniform whole-circle
comparison to the endpoint on the local ball. This defines the prediction
to be captured; the present note supplies no singular-limit identification.

## 6. What common-primitive finite capture transfers, exactly

This is a transfer implication, not a new finite-width theorem. Define the
actual finite changed-law and reference GF using the same initialized arrays,
including their actual finite Gaussian readout. Let the changed-law observation
time `t_epsilon(tau0)` be the physical time selected by a proved continuation
and singular-limit theorem. Let `b` be a separately fixed reference physical
time. A directly observable finite paired quantity is

\[
 J_{2,n,\epsilon,b}={1\over3n}\sum_{i=1}^3
 \|h^2_{n,\mu_\epsilon}(t_\epsilon(\tau_0),v_i)
          -h^2_{n,\nu_*}(b,v_i)\|_2^2.
 \tag{6.1}
\]

No finite trained endpoint has been invented in this definition. The reference
baseline is actual same-array GF at a fixed finite time.

The required paired-capture premise is convergence, in the intended width and
`epsilon` order, of the joint same-layer empirical tuples containing all

\[
 \big(h^2_{n,\mu_\epsilon}(t_\epsilon(\tau_0),v_i),
                 h^2_{n,\nu_*}(b,v_i)\big)_{i=1}^3
\]

to the canonical tuples
`(H2_theta(tau0)(v_i),H2_*(b,v_i))_(i=1)^3`, with both states represented
on the same initialized primitive. For example an admissible proved order
would be width first for each fixed `epsilon,b`, then `epsilon->0` at fixed
`b`; no uniform width rate is assumed here. Joint capture cannot be replaced
by separate marginal convergence.

The test function in (6.1) is continuous and bounded by four per input,
because both activations lie in `[-1,1]`. Therefore this paired-capture
premise implies convergence of (6.1) to

\[
 J_{2,b}={1\over3}\sum_i
 \|H^2_{\theta(\tau_0)}(v_i)-H^2_*(b,v_i)\|_2^2.
\]

The established reference convergence gives
`sup_u ||H2_*(b,u)-H2_dagger(u)||2 ->0` as `b->infty`: use its raw endpoint
bound and the forward Lipschitz estimates. For each term, the difference
between the two squared distances is at most
`4||H2_*(b,v_i)-H2_dagger(v_i)||2`, since each displacement norm is at most
two. Hence `J_(2,b)->J_(2,alpha,y)(tau0)>=eta_H`. This bound is uniform over
the parameter family. Fix one sufficiently large `b`, independently of
`epsilon` and width, so that `J_(2,b)>=3eta_H/4`. The paired-capture premise
then yields

\[
 \lim_{\epsilon\downarrow0}\liminf_{n\to\infty}
       \Pr\{J_{2,n,\epsilon,b}\ge\eta_H/2\}=1
 \tag{6.2}
\]

when that is the order supplied by the capture theorem. If another order is
proved, the same bounded-observable implication uses that order verbatim.
The probability is over the common original initialization. Equation (6.2)
is for every separately fixed law; a failure probability uniform over all laws
does not follow merely from the uniform deterministic margins.

Similarly, suppose the same theorem captures the actual changed-law predictor
uniformly on the circle and identifies its limit with `P_(alpha,y)(tau0)`.
Then (1.5), continuity of scalar squared loss on the bounded prediction region,
and its strict margin imply an actual finite added-risk gain of at least
`eta_R/2`, measured relative to the fixed reference endpoint prediction. If
the baseline is the finite reference predictor at `b`, choose `b` still larger
so its risk error is less than `eta_R/4`; joint convergence then gives a finite
same-array gain of at least `eta_R/2`. This is the risk on the one added atom,
not its vanishing mixture-weighted contribution.

Thus one common-primitive theorem with whole-circle prediction and paired
hidden observation capture is sufficient to transfer both margins. The
existence, nonlinear selection and capture premises remain the responsibility
of the continuation argument; infinitesimal response capture does not supply
them.

## 7. Check status, scope and provenance

The proved deductions here are endpoint conditioning for the entire compact
one-atom family, explicit gradient and projector continuity, and finite
nonlinear risk/upper-hidden margins for every existing constrained evolution
on a common local interval. The final finite-GF statement is conditional on
the precise paired-capture and prediction-capture premises in §6.

Main hostile checks: the rare-root event does not assume independence from
the clock envelope; antipodal and coincident inputs are excluded; the trained
readout is proved nonzero; tensor independence uses no trained-action inverse;
the changed first gate multiplies a fixed endpoint L4 query in (3.2); an
unbounded readout difference is not used as an L-infinity error; the hidden
observable has no evolving-readout contribution; its finite-time margin is
proved on the full nonlinear path; joint paired capture is not inferred from
separate marginals. No claim about first-layer activity is made.

The source proofs in C.4.5–C.4.6 were read completely in round one, including
the actual finite cavity source proof and endpoint passage. The new coordinator
route was read completely in this round as a candidate architecture, not as a
proved continuation theorem. Shared instruction and source hashes were checked
and unchanged before substantive second-round work. No tests or experiments
were authorized or run.

| Source | SHA-256 |
|---|---|
| `ROUTE_CONDITIONING.md` frozen first round | `8d62c9c5efce6f591a36f8509e32e1641b3d45dec1151e33189424a82ef0b12a` |
| `ROUTE_RESIDUAL_CLOCK.md` read in full | `6cb2b1dfb815aa2c579a4e85f4ece77c713e2bcacfa19ee5bf9c7133455a0c9d` |
| `docs/global_nonlinear.md` metadata, only scoped sections read | `bda93ec446425c05f8c06ac3a67fa1505906dff309b74e13bab4effc1527bf05` |
| C.4.5 exact lines 5269–6902 | `4e35f6b1dc336083aaefc4cc8ad15a40e42af1e6b93eadc37da0a32a32b00933` |
| C.4.6 exact lines 6903–8976 | `0bcc4bdf9ea8a02fa7337b42b09395924097f109a56191354e4129806ba071eb` |
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |

The route author checked the displayed constants by direct inequalities,
including the factor two from the unhalved loss, the factor three in normalized
hidden displacement, projector conditioning, and the reference-baseline error.
These are candidate proofs pending supervisor reconstruction or independent
review, not claims of completed independent verification or promotion.
