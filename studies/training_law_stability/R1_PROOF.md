# Frozen research proof, version R1

Authors: `/root`, `/root/transport`, `/root/population`, `/root/nonlazy`.
Assembler: `/root`. Scientific review status is not part of this input.

This document contains the theorem followed by Parts I–IV. References to
component filenames mean the corresponding included part. References to
pre-existing Gaussian and response proofs mean the complete excerpts in
`R1_DEPENDENCIES.md`. C.1/C.3 mentions are provenance only: all needed
full-state existence, oracle and activity arguments are supplied here.



<!-- Complete component: THEOREM.md -->

# Training-law stability for two hidden tanh layers

This study proves a local quantitative statement about the actual nonlinear
learning algorithm. The proof retains the Gaussian matrix action and its
adjoint and permits every training law on the compact observation space.

Fix Y>0. Inputs are `x(alpha)=sqrt(2)(cos(alpha),sin(alpha))` in R²;
`u=x/sqrt(2)` and `G(x,x')=u·u'`. The observation space is
`Z=sqrt(2) S^1 x [-Y,Y]`, with metric
`d_Z((x,y),(x',y'))=|x-x'|/sqrt(2)+|y-y'|`. The Wasserstein distance
`W1(mu,nu)` is the infimum over couplings of the expectation of this metric.
No restriction is imposed on atom counts, atom weights, correlations,
coincident inputs, labels conditional on input, or Gram ranks.

The finite network has equal hidden width n, no biases, and

\[
 z^1(x)=W^{(1)}x/\sqrt2,\quad h^1(x)=\tanh z^1(x),\quad
 z^2(x)=W^{(2)}h^1(x),\quad h^2(x)=\tanh z^2(x),\quad
 f_n(x)=(W^{(3)})^Th^2(x)/n.
\]

All entries and blocks are independent initially, with variances
`W^(1):1`, `W^(2):1/n`, `W^(3):1/n²`, and zero Gaussian means. All blocks
train by mean squared loss, with stored-weight mobilities `(n,1,n)`.
Raw GD updates all blocks from the same preceding state, with physical
step eta. Parameters are interpolated linearly and forward quantities are
recomputed. Initialization is independent of random training observations.

**Theorem.** There exist `T_*>0`, `C<infinity` depending only on Y and this
fixed model, with the following properties.

1. On common canonical Gaussian action spaces there is a strong autonomous
   population flow for every law mu. Its state is a full first-row field
   `w in L²(Omega_1;R²)`, a bounded action
   `A: L²(Omega_1)->L²(Omega_2)` and stored readout `c in L²(Omega_2)`.
   Its initialized action is the actual joint forward/transpose limit of
   the Gaussian middle matrix, and its reverse is the Hilbert adjoint.
   Initial state is `(g,A_0,0)` with `g~N(0,I_2)`; the finite random
   readout is retained and has vanishing normalized RMS. The integral
   equations are (P3)–(P5) below. The state is continuously differentiable
   in the sum of full-row L², action operator norm and readout L²; it is
   unique among strong continuous integral solutions on these initialized
   spaces. At reached states it is uniquely restartable on the remaining
   local interval in the stated bounded-state class. Learned action
   increments are Hilbert–Schmidt, while the initialized action need not be.

2. For `0<q=W1(mu,nu)<=1`, the entire state and all forward hidden fields
   obey the modulus `Cq exp(C sqrt(log(e/q)))` in their stated norms,
   uniformly in time, and the forward fields uniformly in input. In
   particular

   \[
   \sup_{t\le T_*,\,x\in\sqrt2S^1}|f_\mu(t,x)-f_\nu(t,x)|
   \le Cq\exp(C\sqrt{\log(e/q)}).
   \]

   For q=0 the flows agree. For q>1 their predictions differ by at most
   2B, where B is the fixed common state bound defined in the proof. No
   logarithmic expression is evaluated beyond its stated domain.

3. Let `mu_S=m^(-1) sum_i delta_(x_i,y_i)` and `f_S=f_mu_S`. Samples
   differing in one observation satisfy

   \[
   \sup_{t\le T_*,x}|f_S(t,x)-f_{S'}(t,x)|
   \le\frac C m\exp(C\sqrt{\log(em)}).
   \]

   Define `R_mu(g)=int (g(x)-y)² dmu` and
   `Rhat_S(g)=m^(-1)sum_i(g(x_i)-y_i)²`. For iid observations from mu,

   \[
   \sup_{t\le T_*}\left|\mathbb E_S
   [R_\mu(f_S(t))-\widehat R_S(f_S(t))]\right|
   \le\frac C m\exp(C\sqrt{\log(em)}).
   \]

   The expectation and time supremum have exactly this order.

4. For every deterministic sequence of empirical laws lambda_k converging
   in W1 to mu, every `n_k->infinity`, and every `eta_k->0`, actual finite
   GD satisfies

   \[
   \sup_{t\le T_*,x}|f_{n_k,\eta_k,\lambda_k}(t,x)-f_\mu(t,x)|
     \longrightarrow0\quad\hbox{in probability}.
   \]

   In particular this holds for iid samples of any sizes m_k tending to
   infinity, independent of initialization. No relative growth restriction
   is required among n_k, m_k and eta_k. The finite empirical training loss
   and population risk both converge uniformly in time, in probability,
   to `R_mu(f_mu(t))`. This assertion also retains the paired initial/current
   activation displacement observations described next.

5. Define

   \[
   J_\ell(\mu,t)=\int\mathbb E_\ell
   |H^\ell_\mu(t,x)-H^\ell_0(x)|^2\,d\mu(x,y),\qquad\ell=1,2.
   \]

   For the reference
   `mu_0=½ delta_(sqrt(2)e1,Y/2)+½ delta_(sqrt(2)e2,Y/2)` there are a
   specified positive time t_0<=T_*, a radius r_0>0 and j_0>0, defined
   from its actual flow in Part IV, such that
   `J_ell(mu,t_0)>=j_0/2` for both layers whenever
   `W1(mu,mu_0)<r_0`. For the finite networks in assertion 4 converging
   to any such mu, both corresponding training-averaged squared RMS
   displacements exceed j_0/4 with probability tending to one. The family
   is open relative to all admissible laws and contains correlated and
   nonatomic laws.

The conclusion concerns finite-time training-law stability with genuine
nonlinear hidden learning. It does not assert activity for every law,
fitting, endpoint selection, a risk reduction, excess-risk control,
feature-learning superiority, global-time control, or quantitative
finite-width replacement or approximation rates.

The proof first compares changed-law vector fields using only weighted
individual reference tails. It builds the common strong flow by completing
finite training laws in the full state topology, then compares actual GD
directly to a fixed finite reference oracle. A ghost-sample exchange proves
the precise statistical assertion. Finally an actual-flow expansion and
positive adjunction identity give nonzero representation displacement,
which state continuity transfers to an open family. Complete Gaussian and
response dependencies accompany the frozen proof packet.


<!-- Complete component: TRANSPORT.md -->

# Coupled-law comparison in the full first-row state

This proof unit supplies a deterministic comparison estimate, its quantitative
consequences for reference flows with Gaussian tails, and continuity of the
averaged displacement observables. It does not independently construct the
Gaussian action spaces or prove a finite-width identification theorem. Those
obligations are in the other proof units of this study. All statements below
use the actual two-hidden-layer tanh network and its matrix adjoint.

## 1. State, finite interpretation, and exact field

Write `u=x/sqrt(2)`, so `|u|=1`, and put `phi=tanh`. Let
`H_1=L2(Omega_1)` and `H_2=L2(Omega_2)` be real probability Hilbert spaces
with their coordinate operations. A population state is

\[
 \theta=(w,A,c)\in L^2(\Omega_1;\mathbb R^2)
       \times\mathcal B(H_1,H_2)\times H_2.
\]

The vector field preserves the affine class `A=A_0+K` where `K` is a
norm-limit of finite-rank operators: the rank-one integrand in (T2) is
continuous on the compact data support, so finite simple approximations
converge in operator norm, as do their time integrals. Define

\[
\begin{aligned}
 Z^1_\theta(u)&=w\cdot u,& H^1_\theta(u)&=\phi(Z^1_\theta(u)),\\
 Z^2_\theta(u)&=A H^1_\theta(u),& H^2_\theta(u)&=\phi(Z^2_\theta(u)),\\
 f_\theta(u)&=\langle c,H^2_\theta(u)\rangle_{H_2},&
 r_\theta(u,y)&=f_\theta(u)-y,\\
 P^2_\theta(u)&=c,&\delta^2_\theta(u)&=\phi'(Z^2_\theta(u))c,\\
 P^1_\theta(u)&=A^*\delta^2_\theta(u),&
 \delta^1_\theta(u)&=\phi'(Z^1_\theta(u))P^1_\theta(u).
\end{aligned}                                                   \tag{T1}
\]

All pairings use a single neuron population. The population rank-one
operator is `(a tensor b)v=a E_1[bv]`. For a probability law `mu` of `(u,y)`
on `S^1 x [-Y,Y]`, the exact mean-square-loss physical vector field is

\[
 F_\mu(\theta)=\left(
 -2\int r_\theta\delta^1_\theta u\,d\mu,
 -2\int r_\theta\delta^2_\theta\otimes H^1_\theta\,d\mu,
 -2\int r_\theta H^2_\theta\,d\mu\right).                         \tag{T2}
\]

In the first integral the scalar field multiplies the explicit input
vector `u`, producing a two-component row. For a finite network, take
`w=W^(1)`, `A=W^(2)`, `c=W^(3)`, replace field norms by the Euclidean or
Frobenius norm divided by `sqrt(n)`, inner products by `a^T b/n`, and
rank-one actions by `a b^T/n`. Formula (T2) then gives exactly the raw
stored-weight mobilities `(n,1,n)`, as follows from
`docs/finite_dynamics.md` §§1–2. Raw GD is
`theta_(j+1)=theta_j+eta F_mu(theta_j)` with all three blocks evaluated at
the preceding state. Parameter interpolation does not interpolate hidden
features: (T1) is recomputed at the interpolated parameters.

On a common carrier define

\[
 D(\theta,\bar\theta)=\|w-\bar w\|_{L^2(\mathbb R^2)}
                  +\|A-\bar A\|_{\rm op}+\|c-\bar c\|_2.       \tag{T3}
\]

Its finite version is exactly the full-first-matrix distance requested in
the research contract. No cross-width or finite-to-population operator
distance is used anywhere in this proof.

The bound `|phi|<=1`, `|phi'|<=1`, and `Lip(phi')<=2` will be used throughout.
If every individual state norm is at most `B>=1`, then, for every input,

\[
 \|H^1\|_2,\|H^2\|_2\le1,\quad
 \|\delta^2\|_2\le B,\quad \|P^1\|_2,\|\delta^1\|_2\le B^2,
 \quad |f|\le B,\quad |r|\le B+Y.                                \tag{T4}
\]

Consequently the sum of the three velocity norms is at most
`V=2(B+Y)(B^2+B+1)`. If initial individual norms are at most `S_0`, choose
`B=2S_0+2` and

\[
 T_{\rm ball}=\min\{1,(B-S_0)/(4V)\}>0.                          \tag{T5}
\]

The integral-flow first-exit argument and the sum of Euler increments show
that both stay inside this ball up to `2T_ball` for Euler mesh at most
`T_ball`: before a putative first exit the increment of each norm is at most
`2T_ball V<(B-S_0)`. Piecewise affine interpolants have speed bounded by
`V`. These bounds hold for every probability law and every finite empirical
law, regardless of its cardinality.

For the specified initialization, `||W^(1)_0||_F^2/n` tends in probability
to `2`, and `||W^(3)_0||_2^2/n` has expectation `n^(-2)`. The initialized
middle operator is bounded with probability tending to one by the elementary
sphere-net argument in finite dynamics §4. Thus a fixed `S_0` gives a common
high-probability finite ball, independent of the training data. The population
root is the full row `w_0=(g_1,g_2)` with independent standard normals and
`c_0=0`. Retaining the second root coordinate remains necessary even if a
reference training law sees only the first coordinate.

## 2. The one-reference transport estimate

For a field `P`, write `tau_R(P)=||P 1_{|P|>R}||_2`. If the reference
state is `bar theta`, set

\[
 \mathfrak T_{\nu,R}(\bar\theta)
 =\tau_R(\bar c)+\int\tau_R(P^1_{\bar\theta}(u'))\,
                                  \nu(du',dy').                    \tag{T6}
\]

At finite width these are individual empirical neuron RMS tails. In
particular, for a finite reference law with weights `omega_b`, the second
term is the weighted sum of the individual reference tails, not a tail of a
maximum over the reference inputs or over the actual dataset.

**Transport lemma.** On the ball above, for every `R>=1`, every two laws
`mu,nu`, and every two states on the same carrier,

\[
 \|F_\mu(\theta)-F_\nu(\bar\theta)\|_{T3}
 \le C(1+R)\bigl(D(\theta,\bar\theta)+\mathcal W_1(\mu,\nu)\bigr)
       +C\mathfrak T_{\nu,R}(\bar\theta).                           \tag{T7}
\]

Here `W1` uses `|u-u'|+|y-y'|`, and `C` depends only on `B,Y`. The same
constant works for the normalized finite-network norms and actions. Only
the reference state requires tails.

**Proof.** Fix any coupling `pi` of the two laws, and abbreviate
`h=|u-u'|`, `D=D(theta,bar theta)`. Keeping the full first row gives

\[
 \|Z^1_\theta(u)-Z^1_{\bar\theta}(u')\|_2
 \le\|w-\bar w\|_2+\|\bar w\|_2 h\le D+Bh.
\]

The activation is 1-Lipschitz. Expanding
`A H^1-bar A bar H^1=(A-bar A)H^1+bar A(H^1-bar H^1)` therefore gives

\[
 \max_{\ell=1,2}\bigl(\|Z^\ell_\theta(u)-Z^\ell_{\bar\theta}(u')\|_2
          +\|H^\ell_\theta(u)-H^\ell_{\bar\theta}(u')\|_2\bigr)
       \le C(D+h),                                                   \tag{T8}
\]
\[
 |f_\theta(u)-f_{\bar\theta}(u')|\le C(D+h),\qquad
 |r_\theta(u,y)-r_{\bar\theta}(u',y')|
                         \le C(D+h)+|y-y'|.                         \tag{T9}
\]

For any two preactivations and any reference field `bar P`, pointwise
splitting at `|bar P|=R` gives

\[
 \|[\phi'(Z)-\phi'(\bar Z)]\bar P\|_2
       \le2R\|Z-\bar Z\|_2+2\tau_R(\bar P).                        \tag{T10}
\]

For the top backward field, split its difference as
`phi'(Z^2)(c-bar c)+[phi'(Z^2)-phi'(bar Z^2)]bar c`. Thus

\[
 \|\delta^2_\theta(u)-\delta^2_{\bar\theta}(u')\|_2
       \le C(1+R)(D+h)+2\tau_R(\bar c).                             \tag{T11}
\]

Expanding the adjoint difference, and using (T4), bounds the corresponding
`P^1` difference by `B` times (T11) plus `BD`. Split the first backward
field in the same way, now applying (T10) to `P^1_bar theta(u')`. The result is

\[
 \|\delta^1_\theta(u)-\delta^1_{\bar\theta}(u')\|_2
 \le C(1+R)(D+h)
       +C\tau_R(\bar c)+2\tau_R(P^1_{\bar\theta}(u')).                \tag{T12}
\]

There is one power of `R`: the earlier backward error is multiplied only
by a bounded operator and bounded activation derivative. The new gate
cutoff adds an `R` term and does not multiply that earlier error by `R`.

For the first-weight integral the exact decomposition is

\[
\begin{aligned}
 r\delta^1u-\bar r\bar\delta^1u'
  &=(r-\bar r)\delta^1u
    +\bar r(\delta^1-\bar\delta^1)u
    +\bar r\bar\delta^1(u-u').
\end{aligned}
\]

The row-field norm of a product `P u` equals `||P||_2 |u|`. Therefore
(T4), (T9), and (T12) bound this difference by
`C(1+R)(D+h+|y-y'|)` plus the two reference tails. This verifies the
explicit changing-input factor in the first-weight gradient.

For the middle integral use the identity

\[
 r\delta^2\otimes H^1-\bar r\bar\delta^2\otimes\bar H^1
 =(r-\bar r)\delta^2\otimes H^1
 +\bar r(\delta^2-\bar\delta^2)\otimes H^1
 +\bar r\bar\delta^2\otimes(H^1-\bar H^1)
\]

and `||a tensor b||_op=||a||_2||b||_2`. Equations (T4), (T8), (T9),
and (T11) give the same bound. The readout integral uses
`rH^2-bar r bar H^2=(r-bar r)H^2+bar r(H^2-bar H^2)` and needs no tail.
Integrate these three estimates against `pi`. Every tail depends only
on the second marginal, so its integral is exactly (T6). Taking the
infimum of the coupling costs proves (T7); existence of an optimal
coupling is unnecessary. All the norm inequalities also hold under the
finite normalized pairings, proving the finite assertion. ∎

The full Gaussian first-row root is not multiplied by a backward field
in this argument. It enters (T8) only through its RMS norm. In particular,
no unproved Gaussian estimate for products of root and backward fields,
no Gaussian maximum over observations, and no Gram inverse is hidden in
(T7).

## 3. Reference tails and the quantitative modulus

For fixed finite reference laws the established C.2 response lemma proves,
on a common time interval `T_response>0`,

\[
 \sup_{t\le T_{\rm response}}\max_b
 E\exp(c_0|P^1_{\bar\theta(t)}(u_b)|^2)\le C_0,
 \qquad \sup_t E\exp(c_0|\bar c(t)|^2)\le C_0.                       \tag{T13}
\]

Its full weighted response proof is in `docs/global_nonlinear.md` C.2:
the current application has depth two, `|G_ab|<=1`, weights summing to
one, tanh with the three displayed derivative bounds, full independent
Gaussian first roots, zero readout, Gaussian middle matrix, and the
RMS/residual bounds (T4). These verify every bound parameter of that lemma;
its constants are independent of the number and sizes of atom weights.
The named-source rule is supplied by A.2 and its contained III.F.1–III.F.7
dependencies in `docs/special_data_limits.md`. Both orientations are retained.
Arbitrary step sizes of bounded total time and affine Euler-state evaluations
are explicitly included in C.2. The full-row fields are obtained by their
exact row update (T2); passive first directions do not change any trained
preactivation or source recurrence.

The tail implication is elementary: for a constant depending on `c_0`,
`s^2 1_{|s|>R} <= C exp(c_0 s^2) exp(-c_0 R^2/2)`. Taking expectation
and square roots in (T13) yields

\[
 \sup_{t\le T_*}\mathfrak T_{\nu,R}(\bar\theta(t))
                  \le C e^{-cR^2},\qquad
 T_*\le\min(T_{\rm ball},T_{\rm response}).                         \tag{T14}
\]

For an input-population reference the sufficient hypothesis is exactly
the integrated bound (T14). No assertion about exponential tails uniformly
over a continuum of inputs, or about a supremum over time inside a random
tail, is needed. Its passage from finite-law references is proved with the
strong state construction in `POPULATION.md`.

Let `theta(t),bar theta(t)` be strong flows with laws `mu,nu`, common
initial state, and a reference satisfying (T14). Integrating (T7) and
applying the elementary integral Gronwall inequality gives

\[
 \sup_{t\le T_*}D(\theta(t),\bar\theta(t))
 \le C e^{aR}\left((1+R)q+e^{-cR^2}\right),
 \qquad q=\mathcal W_1(\mu,\nu),\ R\ge1.                            \tag{T15}
\]

For completeness, if `d(t)<=b+L int_0^t d(s)ds`, define
`v(t)=b+L int_0^t d(s)ds`; then `v'(t)<=Lv(t)` and
`e^(-Lt)v(t)<=b`. Here `b=CT_*[(1+R)q+e^(-cR^2)]` and
`L=C(1+R)`, which proves (T15) after enlarging constants. Unequal
initial states add their distance inside the parentheses.

For `0<q<=1` put `s=log(e/q)>=1` and choose
`R=max(1,c^(-1/2)) sqrt(s)`. Then `e^(-cR^2)<=e^(-s)=q/e`, and
`1+R<=C exp(C sqrt(s))`. Consequently

\[
 \sup_{t\le T_*}D(\theta(t),\bar\theta(t))
           \le Cq\exp\!\left(C\sqrt{\log(e/q)}\right).              \tag{T16}
\]

The uniform prediction conclusion follows from (T8)–(T9) with `u=u'`.
For `q=0`, let `R` tend to infinity in (T15); the right side tends to
zero, giving equality of states and predictions. For `q>1`, the a priori
bound gives `D<=6B` and `sup_u|f-bar f|<=2B`; the asserted local modulus
is not evaluated at a negative logarithm. All admissible distances are
at most `2+2Y`.

The same argument applies to differently meshed Euler interpolants or a
finite proxy with velocity defect. If the grid states differ from their
interpolated states by at most `V eta` and `V Delta`, and the reference
velocity defect is at most `epsilon` in the sum norm, (T15) becomes

\[
 \sup_{t\le T_*}D(\theta(t),\bar\theta(t))
 \le C e^{aR}\left[D(\theta(0),\bar\theta(0))
 +(1+R)(q+\eta+\Delta)+\epsilon
 +\int_0^{T_*}\mathfrak T_{\nu,R}(\bar\theta_{\rm grid}(s))ds\right].
                                                                    \tag{T17}
\]

This formulation needs only integrated reference tails. A fixed number of
reference proxy grid states can have a common defect tending to zero in
probability. Such a finite-program identification is an input to (T17),
not a conclusion from deterministic stability. Taking width limits with
the reference law, cutoff, and coarse mesh fixed is therefore legitimate;
using a growing Gaussian program without a separate estimate would not be.

## 4. Strong continuity and averaged representation displacement

The maps in (T1) are jointly continuous in `(theta,u)` into their field
spaces on every ball. For the unbounded backward multiplier the needed
fact is: if `Z_j->Z` and `P_j->P` in `L2`, then
`phi'(Z_j)P_j->phi'(Z)P` in `L2`. Subtract the changing `P_j` first.
For the remaining term restrict to `|P|<=M`, use the Lipschitz bound
on `phi'`, then bound the complement by `2 tau_M(P)` and send `M`
to infinity. The argument is uniform on compact sets of states and
inputs by continuity and a finite subcover. Hence the integrands in (T2)
are continuous functions of data and states into their respective Banach
spaces. They are Bochner integrable: their ranges on the compact data
support are compact and therefore separable, and (T4) bounds their norms.

Fix the common initial state `theta_0`. For either hidden preactivations
or activations, write `V_theta^ell(u)` for that field and define

\[
 J_\ell(\theta,\mu)
   =\int\|V_\theta^\ell(u)-V_{\theta_0}^\ell(u)\|_2^2\,\mu(du,dy).
                                                                    \tag{T18}
\]

This is a mean-square displacement averaged over the training-input law;
its RMS is `sqrt(J_ell)`. Initial and current individual norms are bounded
by fixed constants on the ball. Equations (T8) for both current and initial
states imply, with any coupling of `(u,y)` and `(u',y')`,

\[
 \left|\|V_\theta^\ell(u)-V_{\theta_0}^\ell(u)\|_2^2
       -\|V_{\bar\theta}^\ell(u')-V_{\theta_0}^\ell(u')\|_2^2\right|
                       \le C(D(\theta,\bar\theta)+|u-u'|).
\]

Indeed use `|a^2-b^2|<= (a+b)|a-b|` for the two field norms and the
triangle inequality for their difference. Integrate and minimize the
coupling cost to obtain

\[
 |J_\ell(\theta,\mu)-J_\ell(\bar\theta,\nu)|
                 \le C\bigl(D(\theta,\bar\theta)+\mathcal W_1(\mu,\nu)\bigr).
                                                                    \tag{T19}
\]

Combined with (T16), this is quantitative continuity of the squared
displacement at any fixed time. A reference law with `J_ell>0` for both
layers therefore has an open `W1` neighborhood retaining positive margins.
Its reference activity still needs the actual-flow C.3 argument, provided
in `NONLAZY.md`; this continuity lemma by itself makes no activity claim.

## 5. Checks and precise dependencies

The proof covers coincident inputs, singular canonical Grams, atomic laws,
vanishing atom weights after deleting zero-mass atoms, arbitrary joint
input-label correlations, and zero labels. For a zero-signal stationary
reference, no positive displacement is inferred. The input metric is exactly
the requested cost after `u=x/sqrt(2)`. Every field estimate is in normalized
RMS or an actual operator norm on one carrier.

The transport lemma (T7), the conditional reference-flow comparison
(T15)–(T17), continuity, and the displacement estimate (T19) have complete
arguments here. The quantitative law theorem additionally requires the
constructed common carrier, strong distribution-driven flows, and inherited
integrated reference tails. The simultaneous algorithm theorem additionally
requires the fixed-oracle identification and its ordered approximation
limits. These dependencies are kept explicit and are not renamed assumptions
of the requested final result. No finite-width quantitative replacement rate
or claim about expected absolute generalization gaps is made.


<!-- Complete component: POPULATION.md -->

# Autonomous evolution driven by an arbitrary training law

Author: `/root/population`. Status: candidate proof, pending the study's
independent complete reviews. No established file is changed by this document.

This component proves full-state construction, law continuity and uniqueness.
The deterministic comparison lemma is proved in `TRANSPORT.md`; its exact form
used here is restated below. The only pre-existing scientific dependencies are
the complete proofs of `docs/special_data_limits.md` III.F.1–9 and
`docs/global_nonlinear.md` A.1–2, C.2. Their fixed-program scopes are
retained. Their finite Gaussian conditioning, singular-query
regularization, generated action construction, bounded multiplier argument and
weighted response proof are needed, not merely their theorem statements.

## 1. Model, state and equations

Write (u=x/\sqrt2\in S^1), and keep the stated cost

\[
 d_{\mathcal Z}((x,y),(x',y'))=|u-u'|+|y-y'|.
\]

Let \(\mathcal H_i=L^2(\Omega_i,\mathbb P_i)\), one separate neuron
probability space per hidden layer. Section 2 constructs these spaces, a
first-row root \(w_0=(g_1,g_2)\in L^2(\Omega_1;\mathbb R^2)\) with law
\(N(0,I_2)\), and a bounded initialized action
\(A_0:\mathcal H_1\to\mathcal H_2\), together with its actual adjoint.
No joint matching of neuron indices in different populations is used.

The state is

\[
 \theta=(w,A,c)\in
 \mathcal E=L^2(\Omega_1;\mathbb R^2)
 \times\mathcal B(\mathcal H_1,\mathcal H_2)\times\mathcal H_2,
 \qquad \theta_0=(w_0,A_0,0),
\tag{P1}
\]

with distance

\[
 D(\theta,\bar\theta)=\|w-\bar w\|_2+
 \|A-\bar A\|_{\rm op}+\|c-\bar c\|_2.
\tag{P2}
\]

Here the first norm sums both input-coordinate squares inside the expectation.
In particular the full first-row root is retained even for a training law
supported on a single input. For every passive or active input define

\[
 Z^1_\theta(x)=w\cdot u,\quad H^1_\theta(x)=\tanh Z^1_\theta(x),\quad
 Z^2_\theta(x)=AH^1_\theta(x),\quad H^2_\theta(x)=\tanh Z^2_\theta(x),
\]
\[
 f_\theta(x)=\mathbb E_2[cH^2_\theta(x)],\quad
 P^2_\theta(x)=c,\quad \delta^2_\theta(x)=\tanh'(Z^2_\theta(x))c,
\]
\[
 P^1_\theta(x)=A^*\delta^2_\theta(x),\qquad
 \delta^1_\theta(x)=\tanh'(Z^1_\theta(x))P^1_\theta(x).
\tag{P3}
\]

Expectations only contract fields in the same population. Set
\((v\otimes h)g=v\mathbb E_1[hg]\). For a probability law \(\mu\) on
\(\mathcal Z\), put \(r_\theta(x,y)=f_\theta(x)-y\), and define

\[
 F_\mu(\theta)=\left(
 -2\int r_\theta(z)\delta^1_\theta(x)u\,d\mu(z),\quad
 -2\int r_\theta(z)\delta^2_\theta(x)\otimes H^1_\theta(x)\,d\mu(z),\quad
 -2\int r_\theta(z)H^2_\theta(x)\,d\mu(z)
 \right).
\tag{P4}
\]

The strong population equation is

\[
 \theta_\mu(t)=\theta_0+\int_0^t F_\mu(\theta_\mu(s))\,ds.
\tag{P5}
\]

All integrals are strong Bochner integrals in the indicated spaces, with
operator norm for the middle component. Section 3 verifies their existence.
The factors two correspond to the unhalved mean squared loss and physical
time. The three stored-weight mobilities are exactly \((n,1,n)\).

## 2. One compatible initialized Gaussian action space

Start the countable language of III.F.7 with the full independent Gaussian
pair \((g_1,g_2)\) at population 1, a zero readout at population 2, constants,
both orientations of one initialized matrix, rational linear combinations,
tanh, smooth clipped products, and a countable family of smooth bounded
globally Lipschitz coordinate functions dense on each finite compact box.
Close under finite composition. The actual finite roots are the two columns
of \(W^{(1)}_0\), and the actual finite action is the same matrix
\(W^{(2)}_0\) in both orientations. They have the required independent laws.

The deterministic finite-program theorem III.F.1, including the proof of
singular-query regularization in III.F.5, identifies the joint limiting law
of every finite collection of these programs. Finite unions share the same
initialized arrays; deleting unused instructions changes no finite vector.
Consequently these joint laws are compatible. The chronological Gaussian
extension construction of III.F.4 and III.F.7 realizes the countable language
on two generated probability spaces. It does not sample a fresh independent
backward answer: independent oriented *source groups* acquire the response
corrections in equations (III.F.9)–(III.F.10).

For clarity, the operator-completion step uses three concrete facts from that
proof. The finite initialized norm obeys

\[
 \mathbb P(\|W^{(2)}_0\|_{\rm op}>10)
 \le2\,9^{2n}e^{-100n/8}\longrightarrow0.
\]

Second-moment convergence passes the inequality
\(\|W^{(2)}_0v\|_2/\sqrt n\le10\|v\|_2/\sqrt n\)
to every rational combination of generated nodes. Exact finite linear
identities and zero squared differences make the limiting assignment
linear and well-defined on its \(L^2\) classes. Generated smooth cylinder
functions are dense in each generated \(L^2\) space: cylinder simple
functions approximate measurable functions, bounded continuous functions
approximate finite-dimensional Borel functions in \(L^2\), and the included
smooth functions approximate those on compact boxes, with tails removed by
truncation. Thus the assignment extends to a bounded map \(A_0\), of norm
at most 10. The reverse assignments extend in the same way. Passing the
exact finite normalized identity

\[
 v^TW^{(2)}_0h/n=((W^{(2)}_0)^Tv)^Th/n
\]

through the finite-program theorem and then through density identifies the
reverse map with \(A_0^*\).

This language can be fixed independently of the training law. Arbitrary
real directions \(u\in S^1\) are limits of rational linear combinations of
the retained root pair; their initial projections have the joint law
\(\mathbb E[(w_0\cdot u)(w_0\cdot v)]=u\cdot v\).
Arbitrary real coefficients in each separately fixed program are obtained
by rational approximation. For continuous coordinate instructions of at
most linear growth, including the backward products in (P3), A.1 supplies
the extension by smooth clipping and \(L^2\) completion. Its proof chooses
one fixed approximation before taking width to infinity and then removes
the approximation, so no growing-program assertion is introduced here.
The response formulas for these fixed neural programs are those in A.2:
bounded derivatives of tanh and its derivative meet the stated hypotheses.

As a result all rational finite laws and rational-mesh Euler calculations,
their finite unions and full first-row updates belong to one common action
realization. A countable list of additional finite laws may equally be
included. Alternatively the preceding completion represents each of their
fixed calculations directly. This construction also includes any finite
list of passive input directions. There is no data-law-dependent arbitrary
extension of the initialized operator and no comparison of a finite matrix
to a population operator in operator norm.

Different causal enumerations have the same finite generated laws because
their finite arrays agree. Their generated spaces are therefore identified
by the \(L^2\) isometry sending each named coordinate expression to its
counterpart. The isometry preserves coordinate operations and intertwines
the actions and adjoints. This is the precise canonical-realization claim.

## 3. A common ball and continuity of the field

Take \(S_0=11\), so \(\|w_0\|_2=\sqrt2\),
\(\|A_0\|_{\rm op}\le10\), and \(c_0=0\) are strictly inside the ball
of radius \(S_0\) in each component. Put \(B=2S_0+2=24\).
On the ball where each component norm is at most \(B\), bounded tanh gives

\[
 \|H^i(x)\|_2\le1,\quad |f(x)|\le B,\quad |r(x,y)|\le B+Y,
 \quad \|\delta^2(x)\|_2\le B,
 \quad \|P^1(x)\|_2,\|\delta^1(x)\|_2\le B^2.
\tag{P6}
\]

Hence the sum of the three norms of (P4) is bounded by

\[
 V=2(B+Y)(B^2+B+1).
\tag{P7}
\]

These bounds are independent of sample number, individual atom weights,
coincident inputs, covariance ranks and the law. Choose a positive
\(T_{\rm ball}=\min\{1,(B-S_0)/(4V)\}\).
Until a first possible exit, every integral or Euler trajectory has
cumulative increment at most \(2T_{\rm ball}V\); it therefore cannot exit
the ball on \([0,2T_{\rm ball}]\). This is an a priori statement for any
solution, not an existence proof.

On this ball, forward expansion and \(\|\tanh'\|_\infty\le1\) give

\[
 \max_{i=1,2}\bigl(\|Z^i_\theta(x)-Z^i_{\bar\theta}(x')\|_2
 +\|H^i_\theta(x)-H^i_{\bar\theta}(x')\|_2\bigr)
 +|f_\theta(x)-f_{\bar\theta}(x')|
 \le C_B\bigl(D(\theta,\bar\theta)+|u-u'|\bigr).
\tag{P8}
\]

The backward fields are jointly continuous in \((\theta,x)\) with values
in the corresponding \(L^2\) spaces. Here is the necessary product detail.
For \(Z_j\to Z\), \(Q_j\to Q\) in \(L^2\), and bounded continuous \(b\),

\[
 b(Z_j)Q_j-b(Z)Q=b(Z_j)(Q_j-Q)+(b(Z_j)-b(Z))Q.
\]

The first term tends to zero in \(L^2\). For the second, restrict to
\(|Q|\le M\), use bounded convergence in probability there, and bound the
complement by \(2\|b\|_\infty\|Q1_{|Q|>M}\|_2\).
Let \(j\to\infty\) and then \(M\to\infty\). Apply this first to
\(\delta^2\), then use operator/adjoint continuity for \(P^1\), and then
apply it to \(\delta^1\). The same argument works when \(x_j\to x\).
Compactness of the circle shows that for \(\theta_j\to\theta\) this
continuity is uniform over \(x\): a contrary sequence has a subsequence of
inputs converging to one input, contradicting joint continuity.

Each integrand in (P4) is therefore continuous as a Banach-valued function
of \(z=(x,y)\) on the compact data space. Its range is compact and hence
separable; uniform boundedness makes it Bochner integrable. This argument
also resolves measurability despite the possibly nonseparable ambient
operator space. The middle integrand can in fact be integrated in the
Hilbert–Schmidt norm, since
\(\|v\otimes h\|_{\rm HS}=\|v\|_2\|h\|_2\) and the corresponding
rank-one difference bound is the same in that norm. Thus every learned
increment of a strong solution constructed below is Hilbert–Schmidt;
\(A_0\) itself need not be.

We shall use joint continuity

\[
 \theta_j\to\theta,\quad\mathcal W_1(\mu_j,\mu)\to0
 \quad\Longrightarrow\quad
 F_{\mu_j}(\theta_j)\to F_\mu(\theta)\text{ in }\mathcal E.
\tag{P9}
\]

To prove it, uniform continuity just established makes the change in the
integrand caused by \(\theta_j\to\theta\) uniformly small on \(\mathcal Z\).
For the remaining fixed continuous Banach-valued function \(g\), take a
coupling with mean distance \(q_j+o(1)\to0\). If
\(\omega_g(a)=\sup_{d(z,z')\le a}\|g(z)-g(z')\|\), then

\[
 \left\|\int g\,d\mu_j-\int g\,d\mu\right\|
 \le\omega_g(a)+2\|g\|_\infty(q_j+o(1))/a.
\]

First let \(j\to\infty\) and then \(a\downarrow0\). This proves (P9)
without invoking differentiability of a nonlinear map on all of \(L^2\).

## 4. Finite reference flows and the comparison estimate

For a fixed finite probability law
\(\nu=\sum_{a=1}^m\omega_a\delta_{(x_a,y_a)}\), discard zero weights
and combine identical atoms if desired. For each rational mesh \(\Delta>0\)
construct the full-state Euler recursion

\[
 \theta^\Delta_{\nu,k+1}=\theta^\Delta_{\nu,k}
                 +\Delta F_\nu(\theta^\Delta_{\nu,k}),\qquad
 \theta^\Delta_{\nu,0}=\theta_0,
\tag{P10}
\]

and interpolate the three parameters linearly between its grid points.
At every separately fixed mesh there are finitely many calls. Expanding
the learned middle action as a finite sum of rank-one increments rewrites
these calls using only \(A_0,A_0^*\), coordinate maps and deterministic
population contractions. These are the fixed neural programs represented
in Section 2. Each contraction is computed from earlier generated nodes;
no prospective trajectory value is supplied. The full first-row update
is included literally in this recursion. Projection on \(u_b\) gives
the first equation of C.2, since \(u_a\cdot u_b=G_{ab}\). Thus its
active fields obey precisely the equations to which that lemma applies,
without requiring the active directions to span \(\mathbb R^2\).
All full-row Euler velocities have the bound (P7).

The C.2 response bound applies here with \(L=d=2\),
\(|G_{ab}|\le1\), marginal first preactivation variance one, zero population
readout, bounded tanh and its first two derivatives, and all mobilities one.
The preliminary source RMS and residual bounds are (P6). Its complete
weighted argument supplies numbers \(\gamma_0,C_0,T_{\rm response}>0\), depending
only on these bounds and \(Y\), for which every separately fixed finite law
and all its Euler mesh states satisfy

\[
 \sup_{\Delta}\sup_{k\Delta\le T_*}\max_a
 \mathbb E_1 e^{\gamma_0|P^1_{\theta^\Delta_{\nu,k}}(x_a)|^2}\le C_0,
 \qquad \sup_{\Delta}\sup_{k\Delta\le T_*}
 \mathbb E_2 e^{\gamma_0|c^\Delta_{\nu,k}|^2}\le C_0,
\tag{P11}
\]

where
\(0<T_*\le\min(T_{\rm ball},T_{\rm response})\).
The constants do not depend on \(m\), the atom weights or Gram rank.
The C.2 proof uses weighted sums of individual subGaussian marginal bounds;
it makes no estimate of a maximum over a data set or Gaussian history.
The full-row updates change none of its active projected recursions.
C.2's hypotheses therefore remain exactly verified.

For later use, define the *integrated individual tail norm*

\[
 \tau_\nu(\bar\theta,R)=
 \|\bar c1_{|\bar c|>R}\|_2+
 \int\|P^1_{\bar\theta}(x)1_{|P^1_{\bar\theta}(x)|>R}\|_2\,d\nu(x,y).
\tag{P12}
\]

`TRANSPORT.md` proves, at finite width and on these population spaces,

\[
 \|F_\mu(\theta)-F_\nu(\bar\theta)\|_{\mathcal E}
 \le C(1+R)\bigl(D(\theta,\bar\theta)+\mathcal W_1(\mu,\nu)\bigr)
       +C\tau_\nu(\bar\theta,R).
\tag{P13}
\]

Its proof couples \((x,y)\) with \((x',y')\), uses (P8), cuts off only
the reference backward factors, and includes the explicit changed input
factor in \(\delta^1(x)u-\bar\delta^1(x')u'\).
In particular no Gaussian tail bound for \(\theta\) is a hypothesis.
From (P11) the Euler-grid reference tails are bounded by
\(C e^{-cR^2}\). Compare two Euler interpolants for the same finite law.
At time \(t\), each assigned velocity uses its preceding grid state.
Their grid-state distance is at most their interpolant distance plus
\(V(\Delta+\Delta')\), by (P7). Apply (P13) at these grid states,
integrate, and use scalar Gronwall. With fixed \(a,c,C>0\),

\[
 \sup_{t\le T_*}D(\theta^\Delta_\nu(t),\theta^{\Delta'}_\nu(t))
 \le Ce^{aR}\bigl((1+R)(\Delta+\Delta')+e^{-cR^2}\bigr).
\tag{P13a}
\]

Fix \(R\), send the meshes to zero, and then send \(R\to\infty\).
The paths are Cauchy in the complete full-state path space. Their limit
\(\theta_\nu\) satisfies the strong integral equation (P5): the
preceding grid states converge uniformly to this continuous path, and
continuity of \(F_\nu\), uniformly on this convergent family of compact
path ranges, passes their integrated assigned velocities to
\(\int_0^t F_\nu(\theta_\nu(s))ds\). This also proves strong \(C^1\)
regularity. At a fixed time, the reference backward fields at preceding
grid states converge in \(L^2\) by Section 3. Taking an almost surely
convergent subsequence and applying Fatou to (P11) transfers its bounds
to the finite-law flow. Hence
\(\tau_\nu(\theta_\nu(t),R)\le C e^{-cR^2}\), uniformly in time.

Integrating (P13) for two resulting finite-law solutions from their common
initial state now gives

\[
 \sup_{t\le T_*}D(\theta_\lambda(t),\theta_\nu(t))
 \le C e^{aR}\bigl((1+R)\mathcal W_1(\lambda,\nu)+e^{-cR^2}\bigr),
 \qquad R\ge1.
\tag{P14}
\]

For completeness, set \(L_R=C(1+R)\) and
\(b_R=C(1+R)q+C e^{-cR^2}\). The integral inequality is
\(D(t)\le\int_0^t(L_RD(s)+b_R)ds\).
Iterating it, or differentiating its scalar upper comparison, gives
\(D(t)\le b_R t e^{L_Rt}\), which is (P14).

## 5. Completion in the training law and identification of the equation

Every probability measure on the compact \(\mathcal Z\) admits finitely
supported approximations \(\nu_j\) with \(\mathcal W_1(\nu_j,\mu)\le1/j\):
take a finite \(1/j\)-net, partition measurably by the first nearest eligible
net point, and move the measure in each cell to that point. The transport
cost is at most \(1/j\); no boundary-zero assumption is needed. One may
choose the net points from a fixed countable dense set of input angles and
labels. The finite laws' weights need not be rational.

For fixed \(R\), (P14) bounds the limiting Cauchy error by
\(C e^{aR-cR^2}\). Let \(R\to\infty\). Thus \(\theta_{\nu_j}\) is
Cauchy in \(C([0,T_*];\mathcal E)\), which is complete. Let
\(\theta_\mu\) be its limit. It stays in the common ball and its forward
fields converge uniformly in time and input by (P8).

The vector fields converge uniformly in time:

\[
 \sup_{t\le T_*}\|F_{\nu_j}(\theta_{\nu_j}(t))-
                         F_\mu(\theta_\mu(t))\|_{\mathcal E}\to0.
\tag{P15}
\]

Indeed a contrary subsequence has times \(t_j\to t\). Uniform state
convergence and continuity of the limiting curve give
\(\theta_{\nu_j}(t_j)\to\theta_\mu(t)\), so (P9) contradicts the
nonvanishing field difference. Equation (P15) passes the finite-law integral
equations to (P5). The field there is continuous in time, so the result is
a strongly \(C^1\) solution. This proves existence of the autonomous
equation, rather than only Cauchy convergence of its scalar predictions.

It remains to transfer the tails in exactly the strength needed for
uniqueness. For fixed \(t\), backward continuity in Section 3 gives

\[
 \sup_x\|P^1_{\nu_j}(t,x)-P^1_\mu(t,x)\|_2\to0,
 \qquad \|c_{\nu_j}(t)-c_\mu(t)\|_2\to0.
\tag{P16}
\]

For \(M<\infty\), the function
\(b_M(s)=\min\{e^{\gamma_0s^2},M\}\) is bounded and globally Lipschitz.
Equation (P16) therefore shows uniform-in-input convergence of its
expectations. The function
\(x\mapsto\mathbb E_1 b_M(P^1_\mu(t,x))\) is continuous, so weak
convergence of \(\nu_j\) passes its integral to \(\mu\). From (P11),

\[
 \int\mathbb E_1 b_M(P^1_\mu(t,x))\,d\mu(x,y)\le C_0.
\]

Let \(M\uparrow\infty\) by monotone convergence. The same argument for
the readout proves

\[
 \sup_{t\le T_*}\int\mathbb E_1 e^{\gamma_0|P^1_\mu(t,x)|^2}\,d\mu(x,y)
 \le C_0,
 \qquad
 \sup_{t\le T_*}\mathbb E_2 e^{\gamma_0|c_\mu(t)|^2}\le C_0.
\tag{P17}
\]

The supremum is legitimate because the preceding argument holds separately
for every \(t\) with the same constants. No common almost-sure bound on
all times or inputs is asserted. In particular (P17) is an *integrated*
input-law bound, not a pointwise continuum-wide subGaussian statement.

The elementary bound
\(s^2 1_{|s|>R}\le C e^{-\gamma_0R^2/2}e^{\gamma_0s^2}\), followed by
Cauchy–Schwarz over \(\mu\), implies

\[
 \sup_{t\le T_*}\tau_\mu(\theta_\mu(t),R)\le C e^{-cR^2}.
\tag{P18}
\]

This is precisely the reference-tail estimate used by (P13).

## 6. Uniqueness, restart and quantitative law continuity

Let \(\widetilde\theta\) be any other strong solution of (P5) on the
same initialized spaces with initial state \(\theta_0\). Its components
are continuous in the topology (P2), its integrals have the meaning in (P4),
and no tail condition is imposed on it. The first-exit bound of Section 3
keeps it in the common ball. Apply (P13) with \(\mu=\nu\), constructed
\(\theta_\mu\) as reference, and (P18). Gronwall gives

\[
 \sup_{t\le T_*}D(\widetilde\theta(t),\theta_\mu(t))
 \le C e^{aR-cR^2}\quad\hbox{for every }R\ge1.
\]

Sending \(R\to\infty\) proves equality. It also proves independence of
the chosen finite-law approximating sequence: (P14) applied across two
approximating sequences gives the same conclusion directly.

For any two arbitrary laws, (P13) and (P18) prove (P14) with
\((\lambda,\nu)\) replaced by \((\mu,\nu)\). For
\(0<q=\mathcal W_1(\mu,\nu)\le1\), choose

\[
 R=K\sqrt{\log(e/q)},\qquad K\ge1,\qquad cK^2\ge2.
\]

Then \(e^{-cR^2}\le q^2\), while
\(1+K\sqrt{\log(e/q)}\le C e^{C\sqrt{\log(e/q)}}\).
Substitution yields

\[
 \sup_{t\le T_*}D(\theta_\mu(t),\theta_\nu(t))
 \le Cq\exp\bigl(C\sqrt{\log(e/q)}\bigr).
\tag{P19}
\]

Constants depend only on \(Y\) and the frozen model and support bounds.
For \(q=0\), the laws coincide and the solutions are identical; the right
side is interpreted as its zero limit. For \(q>1\), the common ball gives
\(D\le6B\), and in particular \(D\le6Bq\). The maximum possible
distance is at most \(2+2Y\).

Equation (P8) now proves the requested whole-input prediction bound and,
more strongly, the same modulus for the \(L^2\) displacement between
the two forward hidden fields, uniformly over time and the circle.
For \(q>1\) the prediction difference is at most \(2B\).

The equation depends only on the current \((w,A,c)\), its coordinate
functions and the fixed training law. At a time \(s<T_*\), restrict the
constructed path to \([s,T_*]\). The preceding uniqueness argument applied
on this interval, with initial distance zero and this path as reference,
gives unique restart among strong solutions staying on the common ball.
No extra response history must be supplied. More intrinsically, close the
current full-row coordinates, readout, actions and adjoints under the same
coordinate operations; their generated \(L^2\) spaces contain their
subsequent Euler constructions and limits. To justify this last statement
without presupposing Gaussian tails for restarted Euler trajectories,
compare such an Euler trajectory directly against the existing solution
as reference. At each time its preceding grid state differs from its
interpolated state by at most \(V\Delta\). Equation (P13), with reference
tails (P18) at that time, gives the upper error
\(Ce^{aR}((1+R)\Delta+e^{-cR^2})\). Sending \(\Delta\to0\) and then
\(R\to\infty\) proves convergence to the reference continuation. The
Euler law integrals also stay in the generated spaces: their continuous
integrands are limits of finite weighted sums using a dense countable
set of input directions, and the generated spaces are closed.
Equal current generated joint laws define the isometry described in
Section 2 and intertwine the equation. Uniqueness identifies their future
laws. This is a restart claim
on the constructed local interval, not global-time well-posedness from
every arbitrary operator state.

## 7. Forward displacement observables and the small readout

The initialized forward fields \(H^i_0(x)\) are the same for every law.
For each hidden layer put

\[
 M_i(\mu,t)=\int\|H^i_{\theta_\mu(t)}(x)-H^i_0(x)\|_2^2\,d\mu(x,y).
\tag{P20}
\]

They average representation motion over the actual training-input law.
Bounded tanh makes the norms inside the square at most 2. The difference
of their squares at a common input is bounded by four times the
\(L^2\) difference of the moving representations. Each field in (P20)
is uniformly Lipschitz in \(u\) by (P8), including the initialized field.
Coupling the two input laws therefore gives

\[
 \sup_{t\le T_*}|M_i(\mu,t)-M_i(\nu,t)|
 \le C\left(q+\sup_{t\le T_*}D(\theta_\mu(t),\theta_\nu(t))\right).
\tag{P21}
\]

Thus any positive finite-time activity margins for a reference finite law
persist in a sufficiently small open \(\mathcal W_1\)-ball. The actual
positive margins, their nondegenerate witness and their finite-width
transfer are proved separately in `NONLAZY.md` and the algorithm-limit
component; (P21) does not assert activity for every law.

Finally the finite stored readout entries have variance \(n^{-2}\), so

\[
 \mathbb E\left[\|W^{(3)}_0\|_2^2/n\right]=n^{-2},\qquad
 \|W^{(3)}_0\|_2/\sqrt n\longrightarrow0\text{ in probability}.
\tag{P22}
\]

Since \(|\tanh|\le1\), its initial prediction is bounded uniformly on
the circle by this RMS norm. The finite algorithm retains this small
random readout; the same-array comparison to a zero-readout fixed
reference has initial distance exactly this quantity, and the comparison
estimate propagates it at every fixed cutoff. Thus zero in (P1) is the
justified population initial condition, not a modified finite optimizer.

This component establishes a positive local interval, autonomous strong
law-driven dynamics, full-state law continuity and its prediction/feature
consequences. It asserts neither fitting nor a risk improvement, feature
superiority, global-time control, or any quantitative finite-width rate.


<!-- Complete component: ALGORITHM_AND_STATISTICS.md -->

# Actual GD, simultaneous limits, and the statistical consequence

Author: `/root`. Candidate proof, subject to complete paired review.
This component uses the common-state construction in `POPULATION.md` and
the proved comparison in `TRANSPORT.md`; those are proof obligations of the
package, not assumptions added to its final theorem. Write `u=x/sqrt(2)`.
All measures below are on `S^1 x [-Y,Y]` in these isometric input coordinates,
with cost `|u-v|+|y-z|`. Let `d` denote the full-row population state distance
and `D_n` its same-width analogue. The canonical notation and finite equations
are stated in those components. Every constant below is independent of the
number and weights of observations and the smallest Gram eigenvalue.

## 1. A preliminary ball for every data law and every mesh

Choose an initial bound `S0=11`, enlarged if necessary so all three initial
block norms are at most S0 with probability tending to one. This event uses
only the initialization: the first squared Frobenius norm divided by n
converges to 2; the initialized matrix has norm at most 10 with probability
tending to one by the net proof in special-data III.F.2; and

\[
 \mathbb E\frac{\|W^{(3)}_{n,0}\|_2^2}{n}=n^{-2}.
\tag{A1}
\]

The population first-row norm is sqrt(2), the initialized action norm is at
most 10, and the readout is zero. Put B=2S0+2. If the maximum of the three
state norms is at most B, tanh and its derivative give

\[
 \|H^1_u\|_2,\|H^2_u\|_2\le1,\quad |f(u)|\le B,\quad
 \|\delta^2_u\|_2\le B,\quad \|\delta^1_u\|_2\le B^2.
\tag{A2}
\]

The finite statements use Euclidean vector norms divided by sqrt(n).
The three velocity norms are bounded respectively by
`2(B+Y)B²`, `2(B+Y)B`, and `2(B+Y)`. Let V bound their sum, with V>=1,
and choose `Tball <= min(1,(B-S0)/(4V))`. For every positive Euler mesh
of maximum step at most Tball, all preceding states and interpolants through
2Tball stay inside the ball: before a first exit their accumulated block
increment is at most 2Tball V < B-S0. The same first-exit proof holds for
strong flows. Reduce the common T_* so it is at most Tball and the uniform
response time in C.2. Enlarge this ball by a fixed amount for the proxy
below, reducing T_* further if needed. All time choices depend only on Y
and fixed model constants. No finite-GD energy inequality is assumed.

## 2. The fixed finite reference proxy

Fix a finite probability law
`nu=sum_(b=1)^J omega_b delta_(u_b,y_b)`, positive weights summing to one,
and a positive rational proof mesh Delta. These remain fixed as n tends
to infinity. Let the population Euler states for nu and Delta be denoted
`Theta^(nu,Delta)_s`. They use zero initial population readout.

Use the same initialized first and middle arrays as actual GD. Construct
the finite deterministic-coefficient oracle from C.1: replace its scalar
residuals and within-layer contractions by the corresponding population
Euler values, expand the trained middle matrix into initialized action
plus accumulated rank-one updates, and perform the resulting finite list
of actions and coordinate operations. Denote its nodes by superscript o.
The oracle readout root is zero. Define actual finite proxy parameters by

\[
\begin{split}
 \bar W^1_{n,k}&=W^1_{n,0}
 -2\Delta\sum_{s<k,b}\omega_b r_{b,s}
               \delta^{1,o}_{b,s}u_b^T,\\
 \bar W^2_{n,k}&=W^2_{n,0}
 -\frac{2\Delta}{n}\sum_{s<k,b}\omega_b r_{b,s}
               \delta^{2,o}_{b,s}(h^{1,o}_{b,s})^T,\\
 \bar W^3_{n,k}&=W^3_{n,0}
 -2\Delta\sum_{s<k,b}\omega_b r_{b,s}h^{2,o}_{b,s}.
\end{split}\tag{A3}
\]

Interpolate these parameters linearly. In particular the proxy and actual
network have exactly the same initial arrays, including the random readout.
The small readout in (A3) is an additive parameter term, and not a change to
the actual algorithm. Its RMS tends to zero by (A1) and Markov's inequality.

At fixed `(nu,Delta)` the program has finitely many instructions. The
fixed-program theorem III.F.1–7 and global-nonlinear A.1–2 apply: tanh is
smooth with bounded first two derivatives, the gates are bounded smooth
functions times L2 fields, and the roots are Gaussian. Every same-layer
tuple and second moment of oracle nodes converges in probability. For a
proxy middle action applied to an oracle node, its discrepancy from the
prescribed oracle action is a finite sum of terms

\[
 -2\Delta\omega_b r_{b,s}\delta^{2,o}_{b,s}
 \left[\frac{(h^{1,o}_{b,s})^Th^{1,o}_{a,k}}n
             -\mathbb E_1(H^1_{b,s}H^1_{a,k})\right].
\tag{A4}
\]

Each bracket tends to zero; each multiplying node has bounded RMS in
probability. The transpose expansion has the same form with the corresponding
backward contraction. First-row oracle consistency is exact for its input
projections, since (A3) retains the whole root row and exact factors u_b.
Forward induction and (A4) give consistency of recomputed proxy forward
fields. Recomputed proxy backward fields converge by descending induction:
for any reference oracle field p and gate g=tanh',

\[
 \|[g(z)-g(\bar z)]p\|_2
 \le 2R\|z-\bar z\|_2+2\|p\mathbf1_{|p|>R}\|_2.
\tag{A5}
\]

For each fixed cutoff take n to infinity using oracle cutoff second moments;
then remove that cutoff. This controls the only unbounded multiplier. The
readout discrepancy in this step includes exactly the vanishing RMS in (A1).
Thus assigned proxy velocities differ from `F_nu(barTheta_n,k)` by o_P(1)
uniformly over the fixed finite coarse grid in D_n's block norm.

More precisely, for each fixed cutoff R, the reference tail sum satisfies

\[
 \max_k\sum_b\omega_b\sum_{\ell=1}^2
 \frac{\|\bar P^\ell_{b,k}
             \mathbf1_{|\bar P^\ell_{b,k}|>R}\|_2}{\sqrt n}
 \le C e^{-cR^2}+o_{\mathbb P}(1).
\tag{A6}
\]

Here and subsequently an inequality with o_P(1) means its positive excess
over the deterministic bound tends to zero in probability. To verify (A6)
without a discontinuous-test assertion, use
`||v 1_|v|>R|| <= 2||v-p|| + 2||p 1_|p|>R/2||`, and dominate the latter
by a continuous positive-part cutoff at R/4. The oracle cutoff moments
converge; C.2 bounds their population values by a Gaussian tail. Constants
are enlarged and c reduced once. These are individual weighted tails.

The proxy full-row and readout norms and its rank-one velocity norms are
bounded, with limiting upper bounds uniform in Delta and nu. For the middle
block use its initial norm plus the sum of the normalized rank-one norms
in (A3); their limiting total is bounded by the integral velocity bound.
For first rows and readout use the same triangle inequality and the full
root-row second moment. These observations place the proxy in a fixed
enlarged comparison ball and bound its interpolation speed independently
of Delta, with probability tending to one at fixed `(nu,Delta)`.

## 3. Direct comparison with arbitrary growing data and every vanishing step

Let lambda_k be arbitrary deterministic finite probability laws such that
`W1(lambda_k,mu)->0`, let `n_k->infinity`, and let `eta_k->0`. The atom count
and weights of lambda_k are unrestricted. Choose the fixed reference nu above
so that `W1(mu,nu)<=delta`. At each time compare actual GD's preceding fine
state with the proxy's preceding coarse state. Their D_n distance is bounded
by their interpolant distance plus `C(eta_k+Delta)`. The transport estimate
of `TRANSPORT.md`, (A6), and the assigned-velocity error give

\[
\begin{split}
\sup_{t\le T_*}D_{n_k}(\Theta^{GD}_{k}(t),\bar\Theta^{nu,\Delta}_{n_k}(t))
\le C e^{aR}\bigl[(1+R)
 \{\eta_k+\Delta+\mathcal W_1(\lambda_k,\nu)\}
 +e^{-cR^2}+o_{\mathbb P}(1)\bigr].
\end{split}\tag{A7}
\]

This follows by integrating assigned velocities and iterating
`E(t)<=C(1+R) integral_0^t E(s)ds + b`; the exponential series bounds E by
`b exp(C(1+R)T_*)`. Initial discrepancy is zero. The o_P(1) is at fixed
`(nu,Delta,R)`. The first-exit ball in section 1 already bounds actual GD
using only initialized arrays; no Gaussian tail theorem is applied to it.
In particular no maximum over lambda_k's observations or fine GD history
occurs. The same proof would cover GF with eta_k=0.

On the comparison ball, all forward fields in RMS and scalar predictions
are uniformly Lipschitz in the full state and in u, and uniformly Lipschitz
in time along parameter interpolants of bounded speed. For instance
`||z1(u)-z1(v)||<=B|u-v|`,
`||z2(u)-z2(v)||<=B²|u-v|`, and `|f(u)-f(v)|<=B³|u-v|`.
The normalized finite versions are identical. A fixed finite input net,
then a fixed finite time net, therefore transfers fixed-program proxy
prediction convergence to

\[
 \sup_{t\le T_*,u\in S^1}
 |\bar f^{nu,\Delta}_n(t,u)-f^{nu,\Delta}(t,u)|
 \longrightarrow0\quad\hbox{in probability}.
\tag{A8}
\]

At each chosen time and passive input, append its forward evaluation to the
same fixed oracle program. Proxy recomputation follows (A4); at an interior
coarse time the parameters have the affine coefficients from (A3). This
identifies precisely the prediction of the population parameter interpolant,
rather than interpolation of predictions. Its Lipschitz bounds justify the
two nets and remove them after the fixed-program width limit.

The population comparison gives

\[
 \sup_t d(\Theta^{nu,\Delta}(t),\Theta_\mu(t))
 \le C e^{aR}\{(1+R)(\Delta+\delta)+e^{-cR^2}\}.
\tag{A9}
\]

Combining (A7)–(A9), `W1(lambda_k,nu)<=W1(lambda_k,mu)+delta`, and forward
Lipschitz continuity proves the required convergence. The order is explicit:
take k to infinity at fixed delta, fixed finite nu, fixed Delta and R;
send Delta to zero; send delta to zero through finite reference laws;
then send R to infinity. Equivalently, for a desired positive error choose
R first sufficiently large for the Gaussian remainder, then delta and Delta
small enough, and only afterwards take k large. No program whose length
grows with k is passed through a fixed-program theorem. There is no
comparison in operator norm between different spaces or different widths.

## 4. Random observations, the two risks, and their limits

For a law rho and bounded predictor g define

\[
 R_\rho(g)=\int(g(x)-y)^2\,\rho(dx,dy),\qquad
 \widehat R_S(g)=\frac1m\sum_{i=1}^m(g(x_i)-y_i)^2.
\tag{A10}
\]

For any fixed bounded state ball these integrands have a uniform Lipschitz
constant on the joint observation space: if `|g|<=B` and g has input
Lipschitz constant L in u, the difference of squared residuals is at most
`2(B+Y)(L|u-v|+|y-z|)`. Thus for deterministic lambda_k as above, uniformly
on `[0,T_*]`, both the actual empirical training loss
`R_lambda_k(f_(n_k,eta_k,lambda_k)(t))` and its population risk under mu
converge in probability to `R_mu(f_mu(t))`. Indeed predictor uniform error
changes either risk by at most `2(B+Y)` times that error on the initial
high-probability ball; changing lambda_k to mu for the limiting predictor
costs at most `C W1(lambda_k,mu)`. Also
`R_lambda_k(f_lambda_k(t)) -> R_mu(f_mu(t))` and
`R_mu(f_lambda_k(t)) -> R_mu(f_mu(t))` uniformly in time by law stability.

For iid observations of size m from mu, `W1(mu_S,mu)->0` in probability.
Here is an elementary proof sufficient for arbitrary atomic or singular mu.
Partition the compact observation space into finitely many Borel cells of
diameter at most epsilon, and choose a representative in each nonempty cell.
Push both laws to these representatives. Each push costs at most epsilon.
If p_j are true cell masses and p_hat_j empirical masses, their discrete
W1 distance is at most `(diam Z)/2 sum_j |p_hat_j-p_j|`: match the common
mass at each representative and couple remaining masses arbitrarily.
Each empirical cell mass has variance at most 1/(4m), so this finite sum
tends to zero in probability (even in mean). Then let epsilon go to zero.
No boundary-zero partition is needed, since the observations are iid and
the same fixed Borel cells are used for their indicators.

The proof of (A7) is uniform in the actual training law on the event
`W1(mu_S,mu)<=epsilon`: its remaining random errors involve only the fixed
reference program and initialized arrays. Initialization independent of S
has the required unconditional Gaussian law for this reference and the
required joint model. A union bound with the event just proved therefore
extends (A7)–(A10) to arbitrary `n_k,m_k->infinity`, `eta_k->0`. This does
not require a uniform-in-data fixed-program theorem, or a rate for W1.

## 5. Sample replacement and the exactly ordered expected gap

Let `rho(q)=C q exp(C sqrt(log(e/q)))` for `0<q<=1`, with constants enlarged
as in `TRANSPORT.md`, and rho(0)=0. For q>1 use the uniform predictor bound.
The observation space has diameter at most `L_Z=2+2Y`. If S and S' differ
in one observation, match their other m-1 observations and couple the last
two. This gives `W1(mu_S,mu_S')<=L_Z/m`. Law stability and the uniform
predictor bound imply, for every m>=1,

\[
 \sup_{t\le T_*,x\in\sqrt2S^1}|f_S(t,x)-f_{S'}(t,x)|
 \le \beta_m:=\frac{C}{m}\exp(C\sqrt{\log(em)}).
\tag{A11}
\]

For m>=L_Z insert `q<=L_Z/m` into the nondecreasing enlarged modulus
(or use its unspecialized cutoff estimate with q<=L_Z/m). Taking
`R=K sqrt(log(em))` gives (A11) directly. Finitely many smaller m are
covered by enlarging C. Coincident data, identical replacement and q=0
are included. These are the deterministic infinite-width learning maps
`f_S=f_mu_S`; no quantitative finite-width replacement estimate follows.

For any observation z=(x,y), the squared-loss difference for two such
predictors is at most `2(B+Y) beta_m`, uniformly in z and time. Let
`S=(Z_1,...,Z_m)` be iid from mu and let `Z_i'` be an independent copy.
Write `S^(i)` for S with coordinate i replaced by `Z_i'`. All quantities
are measurable: the law-to-predictor map is continuous by law stability,
empirical-law formation is continuous in each observation, and the risks
are integrals of bounded continuous functions. With
`ell(g,z)=(g(x)-y)^2`, independence gives, at each fixed deterministic t,

\[
\begin{split}
\mathbb E_S[R_\mu(f_S(t))-\widehat R_S(f_S(t))]
 &=\frac1m\sum_i\mathbb E_{S,Z_i'}
      [\ell(f_S(t),Z_i')-\ell(f_S(t),Z_i)]\\
 &=\frac1m\sum_i\mathbb E_{S,Z_i'}
      [\ell(f_{S^{(i)}}(t),Z_i)-\ell(f_S(t),Z_i)].
\end{split}\tag{A12}
\]

The second equality exchanges the iid pair `(Z_i,Z_i')` while leaving all
other observations fixed. It uses the fact that the algorithm is the same
measurable empirical-law map for both samples. Every summand has absolute
value at most `2(B+Y) beta_m` by (A11). Taking absolute value of the
expectation and then the supremum over deterministic t yields

\[
 \sup_{t\le T_*}\left|\mathbb E_S
  [R_\mu(f_S(t))-\widehat R_S(f_S(t))]\right|
 \le\frac{C}{m}\exp(C\sqrt{\log(em)}).
\tag{A13}
\]

No expectation of an absolute gap or a time supremum has been taken.
This conclusion gives neither excess risk, useful risk reduction,
endpoint selection, nor superiority over another learning model.

## 6. Representation observables in the joint limit

For ell=1,2 let

\[
 J_{\ell,n}(t;\lambda)=\int
 \frac{\|h^\ell_n(t,x)-h^\ell_n(0,x)\|_2^2}{n}\,\lambda(dx,dy).
\tag{A14}
\]

The integrand is bounded by 4, is uniformly Lipschitz in input on the ball,
and its change between two same-width states with the same initialization
is at most C D_n by the forward estimates and
`| ||v||²-||w||² | <= (||v||+||w||)||v-w||`.
For the fixed proxy its value at finitely many inputs and times converges
by joint oracle second moments including time zero. Input and time nets
then give uniform convergence of the whole integrand to the population
Euler integrand, just as in (A8). Coupling the input laws and using (A7)
therefore proves

\[
 \sup_{t\le T_*}|J_{\ell,n_k}(t;\lambda_k)-J_{\ell}(t;\mu)|
 \longrightarrow0\quad\hbox{in probability}.
\tag{A15}
\]

This holds for the deterministic and independent iid cases above. It
supplies the width-persistent representation displacement required by
`NONLAZY.md`. It asserts no convergence of individual finite neurons to
population coordinates and requires no such artificial coupling.


<!-- Complete component: NONLAZY.md -->

# A finite-time open family with motion in both hidden representations

This proof concerns the model in this study: two tanh hidden layers, `d=2`,
Gaussian initialization of stored weights with variances `(1,1/n,1/n^2)`,
mobilities `(n,1,n)`, mean squared loss, and physical time. Its reference-flow
calculation is unconditional under the established finite-data local theorem
in `docs/global_nonlinear.md` C.1. The open-law and simultaneous-width
conclusions use the state-continuity and observable-convergence conclusions
proved in this study's other components, explicitly identified below. This
file alone does not establish those conclusions.

The argument uses a positive-time consequence of the integral equations,
then continuity of an averaged activation displacement. It requires no
lower bound on a Gram eigenvalue for the full class of laws. The particular
reference below has orthogonal inputs; its open neighborhood permits all
admissible laws sufficiently close to it, including correlated and nonatomic
laws.

## 1. State and observables

Put `u=x/sqrt(2)`, so `|u|=1`. On the compatible common Gaussian spaces of
the population construction, write the first row field as
`w_mu(t) in L2(Omega_1;R^2)`, the middle action as `W_mu^(2)(t)`, and the
stored readout as `W_mu^(3)(t)`. Define

\[
 Z_\mu^{(1)}(t,x)=w_\mu(t)\cdot u,\quad
 H_\mu^{(1)}(t,x)=\tanh Z_\mu^{(1)}(t,x),\qquad
 Z_\mu^{(2)}(t,x)=W_\mu^{(2)}(t)H_\mu^{(1)}(t,x),\quad
 H_\mu^{(2)}(t,x)=\tanh Z_\mu^{(2)}(t,x).
\]

The initialization is common to all laws: `w_0=(g_1,g_2)` with independent
standard Gaussians, `W_0^(2)` the actual Gaussian matrix action with its
adjoint, and `W_0^(3)=0`. Write `H_0^(ell)(x)` for the initialized activation.
For `ell=1,2` define the training-input averaged squared displacement and RMS
displacement

\[
 J_\ell(\mu,t)=\int_{\mathcal Z}
 \|H_\mu^{(\ell)}(t,x)-H_0^{(\ell)}(x)\|_{L^2(\Omega_\ell)}^2
 \,\mu(dx,dy),\qquad
 A_\ell(\mu,t)=\sqrt{J_\ell(\mu,t)}.                       \tag{1}
\]

The coordinate pairing at the two times is the same neuron population,
not an arbitrary coupling of the two activation marginal laws. Since tanh
is bounded by one, `0<=J_ell<=4`.

The common bounded-state interval supplies a deterministic `B>=1` such that
`||w_mu(t)||_2<=B` and `||W_mu^(2)(t)||_op<=B` for all laws and times under
consideration, including initialization. The 1-Lipschitz property of tanh
then gives, with `rho(x,x')=|x-x'|/sqrt(2)`,

\[
 \|H_\mu^{(1)}(t,x)-H_\mu^{(1)}(t,x')\|_2\le B\rho(x,x'),
 \qquad
 \|H_\mu^{(2)}(t,x)-H_\mu^{(2)}(t,x')\|_2\le B^2\rho(x,x').   \tag{2}
\]

Thus one may use `K=B^2` in both layers, for all laws, times and initialization.
These estimates use the full first-row field; controlling only projections
on a fixed training list would not justify them.

## 2. An explicit reference law and actual-flow expansion

Fix `y_0=Y/2>0` and

\[
 x_1=\sqrt2(1,0),\qquad x_2=\sqrt2(0,1),\qquad
 \mu_0=\tfrac12\delta_{(x_1,y_0)}+
       \tfrac12\delta_{(x_2,y_0)},\qquad p=y_0/2=Y/4.          \tag{3}
\]

The Gram is `G=I_2`, and `p` is the label multiplied by its atom weight.
All constants below may depend on this reference and on `Y`.
Suppress `mu_0` in the notation. Set

\[
 h_a=\tanh g_a,\qquad q_0=\mathbb E\tanh^2 g_1>0,
 \qquad \xi_a=W_0^{(2)}h_a\quad (a=1,2).
\]

Oddness and independence of the lower Gaussian roots give
`E[h_a h_b]=q_0 1_(a=b)`. The first forward Gaussian calculation gives
independent `xi_1,xi_2~N(0,q_0)` in the second population. This calculation
can also be read directly at finite width: conditioned on the first-layer
arrays, each row output is Gaussian with covariance
`(h_a^T h_b/n)_(a,b)`, which converges to `q_0 I_2`; row averages of bounded
continuous functions concentrate conditionally, and Gaussian second moments
give the same conclusion for quadratic-growth tests. No trained matrix has
been replaced by an independent map.

Let `b(s)=sech^2(s)=tanh'(s)` and define the following fields, each in its
displayed layer:

\[
 S=p(\tanh\xi_1+\tanh\xi_2),\qquad U_a=S b(\xi_a)
       \quad\hbox{in }L^2(\Omega_2),
\]
\[
 P_a=(W_0^{(2)})^*U_a,\qquad
 T_a=p b(g_a)P_a,\qquad C_a=p b(g_a)^2P_a
       \quad\hbox{in }L^2(\Omega_1),
\]
\[
 M_a=pq_0U_a,\qquad R_a=M_a+W_0^{(2)}C_a,\qquad
 E_a=b(\xi_a)R_a
       \quad\hbox{in }L^2(\Omega_2).                       \tag{4}
\]

All these fields are well defined: `S,U_a` are bounded, the initial action
and its adjoint are bounded on the generated `L2` spaces, and every remaining
multiplier is bounded. The exact weighted physical equations are

\[
 \dot Z_a^{(1)}=-\sum_b G_{ab}r_b\delta_b^{(1)},\qquad
 \dot W^{(2)}=-\sum_b r_b\delta_b^{(2)}\otimes H_b^{(1)},
 \qquad \dot W^{(3)}=-\sum_b r_bH_b^{(2)},                 \tag{5}
\]

where `r_b=f_b-y_0`, `delta_b^(2)=W^(3)b(Z_b^(2))` and
`delta_b^(1)=b(Z_b^(1))(W^(2))*delta_b^(2)`. The factors in (5) are
`-2 omega_b=-1`, since this is a two-point mean loss.

The strong integral equations and continuity give

\[
 \begin{aligned}
 W^{(3)}(t)&=2tS+o_{L^2}(t),&
 \delta_a^{(2)}(t)&=2tU_a+o_{L^2}(t),\\
 \delta_a^{(1)}(t)&=2t b(g_a)P_a+o_{L^2}(t),&
 Z_a^{(1)}(t)-g_a&=2t^2T_a+o_{L^2}(t^2),\\
 H_a^{(1)}(t)-h_a&=2t^2C_a+o_{L^2}(t^2),&
 W^{(2)}(t)-W_0^{(2)}
   &=2t^2\sum_b p U_b\otimes h_b+o_{\rm op}(t^2),\\
 Z_a^{(2)}(t)-\xi_a&=2t^2R_a+o_{L^2}(t^2),&
 H_a^{(2)}(t)-\tanh\xi_a&=2t^2E_a+o_{L^2}(t^2).
 \end{aligned}                                                        \tag{6}
\]

Here is the justification of every passage needed for (6). Divide the
readout integral in (5) by `t` and use `r_b(0)=-y_0`, continuity and
`H_b^(2)(0)=tanh xi_b`. The limit is `y_0 sum_b tanh xi_b=2S`.
If `V_t->V` in `L2` and `a_t->a` in probability with uniformly bounded
`a_t`, then `a_t V_t->a V` in `L2`: bound the part multiplying `V_t-V`
by the uniform multiplier bound, and split the part multiplying `V` at
`|V|<=M`, then let `M` increase. Apply this fact to `b(Z_a^(2)(t))`, and
then to the continuous adjoint and lower gate. It gives the two backward
limits in (6). Integrating `s` times a field converging in `L2` uses
`integral_0^t s ds=t^2/2`, which proves the lower preactivation and matrix
limits, including their factors `2p`.

For either activation difference use the identity

\[
 \frac{\tanh(z+v_t)-\tanh z}{t^2}
 =\frac{v_t}{t^2}\int_0^1 b(z+s v_t)\,ds.
\]

If `v_t/t^2` converges in `L2`, its right side converges to the limit
multiplied by `b(z)`, by the bounded-multiplier argument. Finally expand
`W(t)H_a(t)-W_0h_a` as `(W(t)-W_0)h_a+W_0(H_a(t)-h_a)` plus the product of
the two increments; the latter is `O_L2(t^4)`. The matrix term is
`2t^2 sum_b p U_b E[h_bh_a]=2t^2 M_a`. This gives the upper two limits.
These steps derive (6) along the existing actual flow; no formal power-series
existence argument is used.

## 3. Strict positivity of both activation displacements

Actual adjunction and independence of the upper initial Gaussian coordinates
give, for each `a`,

\[
 \langle h_a,P_a\rangle_1
 =\langle\xi_a,U_a\rangle_2
 =p\,\mathbb E[\xi_a\tanh\xi_a\,b(\xi_a)]>0.             \tag{7}
\]

The other summand in `S` contributes zero, since its tanh has mean zero and
is independent of `xi_a`. In the remaining expectation the integrand is
strictly positive whenever `xi_a!=0`; the nondegenerate Gaussian gives
probability one to that event. It is integrable because it is at most
`|xi_a|`. Thus `P_a` is nonzero in `L2`. Since `p>0` and `b(g_a)>0` almost
surely, `C_a=p b(g_a)^2 P_a` is also nonzero. In particular

\[
 c_1^2=\tfrac12\sum_{a=1}^2\|C_a\|_2^2>0.               \tag{8}
\]

For the upper layer, adjunction yields the positive identity

\[
 \begin{aligned}
 p\sum_a\langle U_a,R_a\rangle_2
 &=p^2q_0\sum_a\|U_a\|_2^2
   +p\sum_a\langle P_a,C_a\rangle_1\\
 &=p^2q_0\sum_a\|U_a\|_2^2
   +p^2\sum_a\mathbb E[b(g_a)^2 P_a^2]>0.                \tag{9}
 \end{aligned}
\]

Its left side is `p sum_a E[S E_a]`. Consequently the `E_a` cannot all
vanish in `L2`, and

\[
 c_2^2=\tfrac12\sum_{a=1}^2\|E_a\|_2^2>0.               \tag{10}
\]

This proves precisely the averaged upper-layer assertion needed here; an
individual upper-input activity assertion is unnecessary. Formula (9) also
retains both upper-preactivation contributions, from the moving middle
matrix and from the moving lower representation.

By (6), (8) and (10),

\[
 A_\ell(\mu_0,t)=2c_\ell t^2+o(t^2),\qquad \ell=1,2.     \tag{11}
\]

There exists `tau in (0,T_*]` such that
`A_ell(mu_0,t)>=c_ell t^2` for both layers and all `0<t<=tau`.
For a completely specified choice from the actual reference solution, let
`s_0` be the supremum of `s in (0,T_*]` such that

\[
 \left|t^{-2}A_\ell(\mu_0,t)-2c_\ell\right|\le c_\ell
 \quad(\ell=1,2;\ 0<t\le s).
\]

Equation (11) gives `s_0>0`; take `tau=s_0/2` and the fixed positive
observation time `t_0=tau/2`. No explicit numeric lower bound on `t_0` is
claimed. The constants `c_ell` are the positive Gaussian-action expressions
(8), (10), rather than fitted or numerically selected quantities.

## 4. Transport continuity and the open family

The state theorem needed from the other proof components is this precise
conclusion: on common generated Gaussian spaces, for `q=W_1(mu,nu)<=1`,

\[
 \sup_{t\le T_*}\bigl(\|w_\mu(t)-w_\nu(t)\|_2+
 \|W_\mu^{(2)}(t)-W_\nu^{(2)}(t)\|_{\rm op}\bigr)
 \le C\,\omega(q),\qquad
 \omega(q)=q\exp(C\sqrt{\log(e/q)}),\quad\omega(0)=0.       \tag{12}
\]

It suffices equally to use any established modulus tending to zero in (12).
The forward formulas on the bounded state ball imply

\[
 \sup_{t,x,\ell}
 \|H_\mu^{(\ell)}(t,x)-H_\nu^{(\ell)}(t,x)\|_2
 \le C_H\omega(q).                                      \tag{13}
\]

Indeed the lower difference is bounded by the first-row difference; the
upper preactivation difference is at most the matrix difference times
`||H_mu^(1)||_2<=1`, plus `B` times the lower difference. Applying tanh
preserves these bounds.

To compare (1), first hold the training law fixed and change the evolved
state. Each activation displacement has norm at most two, so its squared
norm changes by at most `4C_H omega(q)`. Next hold the state `nu` fixed
and change the averaging law. Equation (2) bounds the difference of
displacement fields at `x,x'` by `2K rho(x,x')`; therefore their squared
norms differ by at most `8K rho(x,x')`. Integrating against any coupling
of `mu,nu` and taking the infimum gives

\[
 \sup_{t\le T_*}|J_\ell(\mu,t)-J_\ell(\nu,t)|
 \le 4C_H\omega(q)+8Kq,\qquad\ell=1,2.                  \tag{14}
\]

The joint transport cost dominates `rho`; labels need not be deterministic
functions of inputs for this argument. Approximate minimizers suffice, so
existence of an optimal coupling need not be invoked. The same proof is
valid for atoms, coincident inputs and singular Grams.

Set `j_0=min(c_1^2,c_2^2)t_0^4>0`. Choose a radius `r_0 in (0,1)` such
that `4C_H omega(q)+8Kq<j_0/2` for all `0<q<r_0`; such a radius exists
because the displayed expression tends to zero. Then the relative open set

\[
 \mathcal U=\{\mu\in\mathcal P(\mathcal Z):
                  \mathcal W_1(\mu,\mu_0)<r_0\}          \tag{15}
\]

satisfies, at the specified time `t_0`,

\[
 J_\ell(\mu,t_0)\ge j_0/2,
 \qquad A_\ell(\mu,t_0)\ge\sqrt{j_0/2}>0,
 \quad\mu\in\mathcal U,\quad\ell=1,2.                  \tag{16}
\]

The same construction works at any chosen reference time in `(0,tau]`,
with its own neighborhood and positive margin. For example, spreading each
reference atom over a sufficiently short input arc and a sufficiently short
label interval preserves membership in (15), so the open family contains
nonatomic laws. Moving the second reference input through a sufficiently
small nonzero angle gives correlated two-input laws in (15).

## 5. Transfer to actual finite networks

For a finite network trained on an empirical law `lambda_n`, with its actual
random initial readout, define

\[
 J_{n,\eta,\ell}(t)=\int_{\mathcal Z}\frac1n
 \|h_{n,\eta,\lambda_n}^{(\ell)}(t,x)
       -h_{n,\lambda_n}^{(\ell)}(0,x)\|_2^2\,\lambda_n(dx,dy).
                                                               \tag{17}
\]

For `lambda_n->mu` in `W_1`, the fixed-reference comparison and
finite-program identification must retain the paired initial/current
activation observations. Their required conclusion is

\[
 \sup_{t\le T_*}|J_{n,\eta_n,\ell}(t)-J_\ell(\mu,t)|
       \longrightarrow0\quad\hbox{in probability},       \tag{18}
\]

as `n->infinity` and `eta_n->0`, with no restriction between these sequences
and the sample counts. This is stronger than scalar predictor convergence;
(18) is not inferred from predictor convergence. It follows from the same
state comparison as follows. Against a fixed finite reference proxy, a
state error `e` changes each recomputed activation RMS by at most `Ce`
uniformly in `x`, so changes (17) by at most `Ce`. On the bounded-state
event, (2) has the identical finite RMS form. It permits transport of the
averaging law with error `8K W_1` and reduction of the remaining reference
input integral to a fixed finite input net. At that fixed net, paired
initial/current proxy activations form a fixed finite program, whose
quadratic displacement observations converge. Its finite time mesh is
fixed during width identification; bounded state interpolation speeds and
the activation Lipschitz bound control the intervals between its time
points. Remove the proxy state error, transport error, input net and proof
mesh in the ordered limits used by the joint-algorithm theorem. This yields
(18), without a distance between finite matrices and population operators.

For iid empirical laws independent of initialization, use the corresponding
in-probability joint-limit statement with these same observations. In
particular, for every `mu in U` and either deterministic empirical
approximation or iid sampling, (16), (18) imply

\[
 \Pr\{J_{n,\eta_n,\ell}(t_0)\ge j_0/4
                 \text{ for both }\ell=1,2\}\longrightarrow1. \tag{19}
\]

Thus both hidden activation displacements stay bounded away from zero as
width increases, at a physical time and activity margin independent of
width, sample count and GD step. The finite initialization is the one in
the question: its readout RMS has squared expectation `1/n^2`, hence tends
to zero in probability and is covered by the initialization-perturbation
comparison. It has not been set to zero in (17).

This result asserts finite-time motion of both hidden representations on an
open family. It asserts no activity for every law, no fitting, no risk
improvement, no endpoint selection and no global-time property. In
particular a law with zero conditional label mean can have the stationary
zero-readout population solution, consistently with the stated scope.

## Proof dependencies and checks

Read for this derivation: `docs/global_nonlinear.md` C.1, C.2, C.3 in full,
including weighted-loss corrections; A.1–A.2; the complete III.F in
`docs/special_data_limits.md`; `docs/finite_dynamics.md` §§1–4; the notation
and research guides. The reference satisfies C.1's bounded-derivative tanh
hypotheses, independent Gaussian initialization, fixed dimension/data and
positive weights. C.3 is the source of the onset architecture, while (6)–(10)
above supply all needed activity details directly. No specialized external
theorem or computational experiment is a dependency.

Author: `/root/nonlazy`. Author check: derived every coefficient from the
weighted equations (5), checked the factor `p=omega y`, retained actual
adjunction in (7), (9), checked activation rather than parameter displacement,
and exposed the state/observable dependencies (12), (18). The decisive
population construction and transport estimates remain the responsibility
of the other proof components; this file does not label them assumptions
to declare the full study resolved. Fresh isolated package reviews remain
required.
