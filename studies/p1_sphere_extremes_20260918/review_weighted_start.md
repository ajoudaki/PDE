# Independent review of weighted three-input slow-onset classification

Verdict: **PASS**, within the exact initialized canonical `d=3,p=1`
population closure and the physical metric stated in the candidates.
There is no mathematical blocker to the six-way equivalence or to the
finite-slot criterion. The quantitative lower bound is valid with the
displayed constants and hypotheses. One nonblocking notation issue is
recorded below: the explicit slot defect is not an intrinsic function of
a law after repeated atoms are identified.

This is an isolated analytic review, not promotion approval. No experiment,
quadrature, finite population calculation, other study, study history,
README, other review, or current author finding was used.

## Frozen inputs and scope

The primary frozen inputs were read completely and their assigned SHA256
values verified:

- `start_hitting_classification.md`:
  `9190848b4a54e7597a54d1dbbd44ab4c4fe8d30b270cd76a4eeff567f5801225`.
- `start_classification.md`, added by the supervisor as a second frozen
  candidate:
  `e13f3c5720d24ddf56b1b1d034d0a458c6581e66c8786cd2dac466fb502b864d`.

The complete supplied `initialization_positivity.md`, `early_delay.md`,
`necessary_potential_growth.md`, and established `docs/observable_p1.md`
were also read. The established dynamics and local/global existence
arguments were checked in `docs/global_nonlinear.md`, C.4.7.9.3--4 and
the dictionary/state/equations and energy/existence portions of
C.4.7.10.D.3. The rigorous-math skill and the research-contract and
adversarial-audit instructions were applied.

The second candidate lists `terminal_geometry.md` in its provenance. It
was outside this review's input packet and was not read. No assertion
needed for the reviewed proofs remains dependent on that file: the
initialization, equations, energy, existence, and continuity arguments
needed here are supplied by the permitted sources and the candidates.

The object is the exact population closure, with its fixed correlated
lower marks, independent upper population, ridge `eta=1/4096`, full
evolving `3 x 6` active matrix and its actual transpose. Inputs are
`u=x/sqrt(3)` on `S2`; data weights are nonnegative and sum to one;
labels are binary. The result is about compact time intervals before
taking the data limit. It asserts neither identification with a
general-dimensional trained-network limit nor terminal fitting.

## 1. Initialization and the geometric kernel

The normalization and factors agree with `docs/observable_p1.md`.
Deleting the inactive constant features is justified by the initialized
mark-negation invariant sector; it imposes no diagonal constraint on the
moving matrix. If `U_l v=b_l^T v`, ridge normalization gives

\[
 U_l^*U_l=E[b_lb_l^T]
 =I-\eta L_l^{-1}L_l^{-T}\preceq I.
\]

The same contraction bound holds for the active subblock. Feature
envelopes `K_l=ess sup |b_l|` are finite because tanh is bounded and the
fixed normalizing denominators are strictly positive. These facts
justify the analysis and synthesis bounds used throughout both papers.

The supplied positivity proof includes the reverse response and ridge
subtraction. Its crucial inequalities check as follows. Gaussian
integration by parts against the independent reverse noise gives
`b^2 >= tau gamma^2+eta`. For
`B_*=[alpha beta eta/(nu+eta)+tau gamma]/b^2`, positivity of beta and
`beta<=alpha nu` give `0<B_*<=1/gamma`. Integrating
`sech^2 z>=1-z^2` gives

\[
 K(h)/h\ge\alpha^2(1-\alpha/3)=m<\alpha,
\]

and therefore

\[
 c_*\Psi(h)/h\ge\frac\alpha\gamma
 \left[\gamma\frac\nu{\nu+\eta}-1+\alpha-\frac{\alpha^2}{3}\right].
\]

The elementary bounds `nu<3/7`, `alpha>11/15`,
`eta/(nu+eta)<1/65`, and `gamma>=alpha-alpha^2 nu` imply the
stated lower bound `2552/61425>0` for the bracket. Its value comes from
`7/15-1936/4725-1/65`; the expression increases with alpha and decreases
with nu on the ranges used. The Gaussian integrations have bounded
integrands/derivatives and vanishing boundary terms. Thus the sign of
`Psi(h)` is proved without an empirical coefficient premise.

For `F(G)=Psi(tanh G)`, conditioning the actual lower joint law gives

\[
 Da_0(u)=(T(u_1),T(u_2),T(u_3)),\qquad
 T(r)=E[F(G)\tanh(rG+\sqrt{1-r^2}N)].
\]

This operation integrates out the prescribed reverse noise conditionally;
it does not replace correlated lower marks by independent ones.

The claimed strict monotonicity of T is valid even though F is not
assumed increasing. For fixed `g>0` and `|r|<1`, put
`X=rg+sqrt(1-r^2)N`. Differentiation and Gaussian integration by parts
give

\[
 \partial_rE\tanh X=gE\operatorname{sech}^2X-rE\tanh''X>0.
\]

The first term is positive. The second is nonnegative because the odd
function `tanh''` is negative on the positive half-line, and pairing
positive/negative Gaussian integration variables shows that its
expectation has sign opposite to `rg`. The derivative is odd in g and
bounded in absolute value by `|g|+2`. Since F is bounded and has the
strict sign of g, dominated differentiation gives `T'(r)>0` in the
open interval. Dominated convergence at the endpoints and interior
strict increase prove strict increase on the whole closed interval.
Oddness is preserved. Hence `Da_0(u)` is nonzero on the sphere and
identifies u injectively, including modulo sign.

The upper mark law has a strictly positive density on its stated open
cube: each coordinate is a strictly monotone smooth transform of a
nondegenerate Gaussian. A continuous feature identity holding almost
surely therefore holds at every point of that cube. For at most three
nonzero vectors distinct modulo sign, choose q outside the finitely
many hyperplanes making `q.v_i` zero or equal up to sign. On the line
`b=tq`, the first k odd Taylor coefficients of tanh yield a Vandermonde
system in the distinct numbers `(q.v_i)^2`. The coefficients
`1,-1/3,2/15` are nonzero. Thus the ridge functions are independent.
This argument also covers collinear vectors with different magnitudes;
no linear independence of the effective vectors is assumed.

It follows that the exact kernel is precisely antipodal signed-mass
cancellation within each active class:

\[
 m_0(\mu)=0
 \iff \sum_{i\text{ in each class}}p_i y_i\sigma_i=0,
 \quad u_i=\sigma_i v.
\]

A nonempty class requires at least two positive slots. With at most
three slots there is one class; its two effective signs each carry mass
one half. One sign has a singleton slot of weight one half. Two active
slots must both have weight one half, and one active slot cannot cancel.
These statements correctly ignore arbitrary zero-weight directions.

Every current feature map is odd in the input. Consequently this
cancellation persists at every state, and expanding the loss gives
`L_mu(theta)=1+integral f_theta^2 dmu>=1`. At initialization all
velocities except the readout vanish, and

\[
 F_\mu(\theta_0)=(0,2m_0(\mu),0),\qquad
 -L_\mu'(0)=4\|m_0(\mu)\|_2^2.
\]

The factor four is correct for unhalved square loss and the prescribed
physical population/Frobenius metric. Uniqueness makes this state
stationary exactly on the identified set Z.

## 2. Existence, Hilbert estimates, and all weights

The local contraction argument in the supplied established source is
dimension-independent for fixed finite feature dimensions. Its state
space is bounded `w-g,c` and finite M; the unbounded fixed Gaussian g
appears inside globally Lipschitz gates. Direct loss differentiation
along these characteristic solutions gives

\[
 L(t)+\int_0^t\|\theta'(s)\|_{raw}^2ds=1,
 \qquad R(t)^2\le t[1-L(t)]\le t.
\]

The norm uses the two population probabilities and the ordinary matrix
Frobenius norm. No division by an input weight occurs. Thus zero input
weights cause no singularity. Because `integral |r| dmu<=1`, direct
integration gives

\[
 \|c(t)\|_\infty\le2t,\quad
 \|M(t)-D\|_F\le2t^2,\quad
 \|w'(t)\|_\infty\le4tK_1(d_*+2t^2).
\]

These are bounds in the local existence norms; their finite-horizon
speed bounds provide Cauchy endpoints and continuation. Existence and
uniqueness therefore hold through every finite time, including boundary
laws. The argument does not mistake bounded Hilbert balls for compact
sets or rely on an unrestricted L2 multiplication rule.

I checked every bound in equations (17)--(21) of
`start_hitting_classification.md`. On its radius-R ball, write
`B=d_*+R`, `C=R`, `W=sqrt(3)+R`, `J=1+C`. The identities

\[
 Z_1=Be_w+e_M,\quad F_1=e_c+CZ_1,\quad
 D_1=e_c+2CK_2Z_1
\]

give valid bounds on the upper preactivation/feature, prediction, and
reverse contraction differences. In particular, the product containing
c is controlled by `||c||2 ||Delta gate||infinity`, and
`||Delta z||infinity<=K2 Z1`. The lower reverse action and its difference
are bounded in supremum norm by
`K1 B C` and `K1(C e_M+B D1)`. Subtracting the three factors in each
velocity gives exactly the three bounds in (18), including its factor
`2BC e_w` for the lower gate difference. Summing them and using
`e_w+e_c+e_M<=sqrt(3)||Delta theta||raw` supplies a finite common L_R.

For the data estimate, the residual has Lipschitz constant
`P=max(CBW,1)` for cost `|u-v|+|y-z|`. The respective input Lipschitz
constants for a, H, d, and Q are

\[
 W,\quad BW,\quad2CK_2BW,\quad2K_1K_2B^2CW.
\]

The lower gate has L2 constant `2W`; the final input-vector factor in
the row velocity contributes the last `Q_*` term of A_w. Therefore all
three constants A_c, A_M, A_w in (21) are valid, and their sum bounds
the raw norm. Integrating against any finite coupling includes label
changes, mass changes, repeated atoms, and zero limiting masses.

Both solutions stay in the radius-`sqrt(T)` ball. The integral
inequality gives (22) with
`A_R (exp(L_R T)-1)/L_R`. Squared residuals are bounded in difference
by `2J` times the residual difference and have data Lipschitz constant
`2JP`; this proves the claimed uniform loss continuity (23). The
shorter Hilbert-continuity argument in the second candidate is also
valid: its bounded c and M region suffices for state continuity, and
the extra common bound on `||w||2` supplies input continuity.

## 3. Equivalences and quantitative delay

The data space K is compact in the specified transportation metric.
For converging indexed parameters, common masses can be matched while
the unmatched mass travels at cost at most four. Quotienting repeated
atoms does not change compactness. The initialized signed feature is
Lipschitz with constant `Lambda_0=max(d_*sqrt(3),1)`. Thus Z is closed,
compact, and nonempty; a nearest point exists. Compactness gives a
positive minimum of s on every nonempty set `dist(mu,Z)>=a>0`, and
`s<=Lambda_0 dist(mu,Z)`. This proves equivalence of vanishing s,
vanishing distance, and all subsequential limits lying in Z.

Uniform finite-time flow continuity against a nearest stationary law
implies complete raw-state stagnation. Conversely the energy-path
inequality shows that loss stagnation implies complete raw-state
stagnation. Since `|f(u)|<=||c||2`, raw-state stagnation implies loss
stagnation. A convergent data subsequence with stagnant losses has
limiting loss identically one, hence zero initial slope and limit in Z.
No infinite-time limit is interchanged with a data limit.

The direct initial-speed estimates furnish a second check. On a fixed
horizon, state Lipschitz continuity gives

\[
 \|\theta'(t)\|\le2s e^{L_Rt},\qquad
 1-L(t)\le\frac{2s^2}{L_R}(e^{2L_Rt}-1).
\]

On `0<=t<=t_0=min(1,log(3/2)/L_1)`, the speed differs from its
initial value by at most s and is therefore at least s. This gives
`1-L(t)>=s^2t`. The second candidate's equivalent expressions using
`S=4s^2` have the correct factors. These uniform estimates validate
the inference from vanishing initial slope to finite-horizon stagnation.

Loss continuity and monotonicity make this equivalent to divergence of
the hitting time for **every** fixed drop `delta in (0,1)`: failure of
stagnation leaves a subsequence with a fixed positive deficit at some
finite T, which crosses a smaller fixed drop by T. Conversely, loss
remaining uniformly near one on each fixed horizon excludes each
fixed positive drop on that horizon. Never-attained thresholds are
correctly assigned infinite hitting time.

For the quantitative statement, exact cancellation for every state of
a nearest law in Z and the input Lipschitz bound give, when `R(t)<=r`,

\[
 \|m_\mu(\theta(t))\|_2\le\Lambda_r\rho,
 \quad\Lambda_r=\max((d_*+r)(\sqrt3+r),1).
\]

Expanding loss and applying the path-energy inequality yield

\[
 0\le1-L(t)\le2\Lambda_r\rho R(t),\qquad
 R(t)^2\le t[1-L(t)].
\]

Division only for positive R proves
`R(t)<=2 Lambda_r rho t` and
`1-L(t)<=4 Lambda_r^2 rho^2 t` while in the ball. A first exit at
radius r cannot occur before `r/(2 Lambda_r rho)`, so the estimates
hold throughout that interval, including its endpoint by continuity.
If `2r Lambda_r rho<delta`, the drop cannot occur in the ball;
therefore (33) follows. For `rho=0` stationarity supplies the stated
infinite-time convention. The result is a lower bound, not a matching
asymptotic. It is consistent with the stronger centered-difference
delay in `early_delay.md` and the necessary-potential-growth argument.

## 4. Explicit slot defect and balanced specialization

For `z_i=y_i u_i`, the kernel classification is equivalent to an index
k with `p_k=1/2` and `z_j=-z_k` whenever `j!=k` and `p_j>0`.
Each summand in the proposed defect is nonnegative, so its zero set is
exactly that condition. On the compact indexed parameter space, both
the slope and defect are continuous with this common zero set. The
subsequence argument proves their simultaneous convergence to zero
for arbitrary sequences, including changing labels and vanishing
weights. It does not assume that one distinguished k works for the
whole sequence. The fixed-positive-weight corollary `max p_i=1/2`
and the uniform positive lower slope for three equal weights follow.

Within the balanced slice, raw antipodal orientations would each have
to contain both labels: adding/subtracting label balance and signed
cancellation gives zero signed label mass in each raw orientation.
Two nonempty orientations would require four active atoms. With at
most three, all active raw inputs coincide. Conversely coincident
active inputs and label balance cancel exactly. The weighted
dispersion

\[
 \sum_{i<j}p_ip_j\|u_i-u_j\|^2
\]

has exactly this zero set. Compactness proves the second candidate's
balanced criterion, also for asymptotically balanced sequences because
all their accumulation points are balanced. Vanishing-weight inputs
need not coalesce. If all weights have a common positive lower bound,
the criterion reduces to pairwise coalescence.

For the first candidate's balanced subclass, the target cancellation
law is `1/2 delta_(v,+)+1/2 delta_(v,-)`. Every coupling to it pays
`sum p_i |u_i-v|` in input cost, and matching equal label masses removes
the label cost. Thus (35) is exactly its transportation distance after
minimization in v. This is a distance to the balanced zero set; the
paper correctly does not assert equality with distance to unrestricted Z.

**Nonblocking notation clarification.** The formula called `Delta(mu)`
is a defect of the listed three slots, not an intrinsic function of
the quotient law used in the first candidate. For example, represent
the same one-atom law by three identical active slots of mass one
third, all with the same label. The formula gives `Delta=17/6`.
Represent it by masses `(1,0,0)` and it gives `Delta=1/2`.
Its zero set and convergence-to-zero criterion are nevertheless
representation invariant by the proved equivalence with the slope.
When presenting the explicit formula alongside the law metric, write
`Delta((p_i,u_i,y_i)_{i=1}^3)` or say that the indexed representation
is fixed. This clarification requires no change to the proof.

## 5. Single-threshold counterexamples

Both examples check under the full dynamics.

In the first candidate, the limiting weights at `(e1,e1,e2)` give

\[
 L_*=\tfrac34(f(e_1)+\tfrac13)^2
       +\tfrac14(f(e_2)-1)^2+\tfrac23.
\]

The initialized feature is `(H_0(e2)-H_0(e1))/4`, which is nonzero:
the two features are independent, centered, nonconstant functions of
different upper coordinates, with coefficient `T(1)>0`. The limiting
loss therefore decreases strictly initially but remains at least
two thirds. Its finite-time limiting law proves divergence of every
hitting time to a fixed level below two thirds, while early stagnation
fails. The perturbed inputs have determinant epsilon and retain
positive balanced weights. Finite-time loss continuity supplies the
required strict margins. The asserted limiting plateau belongs to
the degenerate limit law only.

The second candidate strengthens this to any prescribed drop delta.
For `0<kappa<min(1/2,delta/(1+delta))`, the stated square completion
gives the lower floor `1-kappa/(1-kappa)>1-delta`, while

\[
 S=4\kappa^2\|H_0(e_1)-H_0(e_2)\|_2^2>0.
\]

Replacing the second e1 direction by
`(e1+epsilon e3)/sqrt(1+epsilon^2)` makes the three inputs linearly
independent. The weights stay fixed and positive, labels stay exactly
balanced, slopes tend to the positive displayed value, and uniform
finite-horizon loss continuity keeps the selected threshold out of
every fixed horizon. Thus one-threshold divergence is strictly weaker
even under all those nondegeneracy conditions on actual family members.
Neither example needs eventual threshold attainment by the approximants.

## Claim boundaries and final disposition

No fatal, major, or conditional gap survives within the stated
contract. The proof accounts for all trained blocks, population
weights, physical time, zero-mass limits, and the exact prescribed
initialization. It uses compactness of finite data parameters, not
compactness of infinite-dimensional state balls. Every dynamical
claim is on a separately fixed finite horizon, except for lower
hitting-time bounds and stationary laws where the arguments explicitly
justify the extension.

The strongest surviving alternative is eventual fitting after a long
delay for each fixed nondegenerate dataset. Both candidates leave it
open, as they should. The results do not identify a terminal rate, an
optimal distance exponent, or any upper bound on hitting times.
The only recommended edit is the explicit slot-defect notation above.

**Final verdict: PASS for both frozen candidates, with one nonblocking
notation clarification.**
