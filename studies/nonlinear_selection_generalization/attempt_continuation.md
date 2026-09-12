# Bounded-law continuation and capture route

Status: candidate proof, not independently checked or promoted. Author: scoped
agent `continuation_route`, 2026-09-12. No experiments or Git writes were made.
This report addresses continuation, whole-circle prediction and finite-width
capture, and gives a sampling bridge. It does not establish a nonzero learning
margin for a specified member of the frozen target class.

## Input scope and provenance

Allowed scientific inputs were the frozen study README, `docs/NOTATION.md`,
complete C.4.9 and necessary established dependencies. A subsequent scope
clarification permitted III.F in `docs/special_data_limits.md`. No other
attempt, study, conversation, historical finding or web science was read.

Actual scientific read coverage:

- `global_nonlinear.md`: complete C.4.9, lines 12994–15322; elementary limits
  and finite Gaussian proof, 185–504; A.1–A.4, 1840–1898; canonical carrier
  and law-integrability construction, 4210–4364; complete reference
  construction/endpoint proof C.4.5.1 §§1–3, 5475–5782; its complete rational
  constant certificate, 5999–6103; complete C.4.5.2, 6104–6595.
- C.4.6 §6, 8142–8258, was read as a locator, but its cavity proof was not
  read and is not imported. The integrated-source argument in §2 below
  supplies the moment input needed for endpoint conditioning.
- `special_data_limits.md`: complete III.F.1–III.F.11. A truncated initial
  output was repaired by overlapping reads of 3995–4135. A few following
  III.S header lines were visible in the supplied range but are unused.
- Complete frozen README and notation; required proof and research skills,
  research-contract, proof-search-orchestration, evidence-ledger and
  adversarial-audit references; shared workflow process instructions.

Source HEAD was `b14dc38bdca0c7835685e768e6ca0657d60cf10d`. SHA-256:

```
global_nonlinear.md    7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465
special_data_limits.md 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489
NOTATION.md            199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b
study README           e74b04e95b4363a32dc887c244dbdf0370418f2c98770a98decff48d89358956
```

The pre-edit status check showed concurrent changes elsewhere; their names
were metadata only. This author owns only this report.

## 1. Statement

Keep exactly C.4.9's network, initialization, unhalved probability-weighted
square loss, mobilities `(n,1,n)` and original-initialization physical GF.
Write `u=(cos alpha,sin alpha)`, use circular arc distance `d_c`, and set

\[
\mathcal Z_Y=S^1\times[-Y,Y],\quad
d_Z((u,y),(v,z))=d_c(u,v)+|y-z|,\quad Y\ge1.
\]

Let `nu_*` be the two exact anchor atoms, each of mass `1/2`, and let
`theta_dagger` be the specified reference endpoint on C.4.9's canonical
generated carrier. Use its raw Hilbert metric, and `g_theta(u),G_theta,
M_theta,Pi_theta` from NS2. Define Bochner integrals

\[
v_\nu(\theta)=\int(f_\theta(u)-y)g_\theta(u)\,d\nu(u,y),\qquad
V_\nu(\theta)=-2\Pi_\theta v_\nu(\theta).
\tag{1}
\]

**Candidate theorem.** There exist `epsilon_0,tau_0>0`, depending only on
`Y` and the fixed reference, independent of the Borel added law, support
size, smallest atom and quantization, with the following properties.

1. For every probability `nu` on `Z_Y`, the strong equation
   \[
   \dot{\bar\theta}_\nu=V_\nu(\bar\theta_\nu),\qquad
   \bar\theta_\nu(0)=\theta_\dagger
   \tag{2}
   \]
   has a unique solution on `[0,tau_0]` in a common conditioned neighborhood.
   It preserves the anchor predictions. Its whole-circle prediction is
   \[
   P_\nu(\tau,\sqrt2u)=\langle\bar c_\nu(\tau),
   \tanh((A_0+\bar K_\nu(\tau))\tanh(\bar w_\nu(\tau)\cdot u))\rangle.
   \tag{3}
   \]
2. The original-initialization mixture `(1-epsilon)nu_*+epsilon nu` has a
   unique strong population GF through `tau_0/epsilon`. For each
   `0<tau_-<tau_0`,
   \[
   \sup_\nu\sup_{\tau_-\le\tau\le\tau_0}
   \|\theta_{\epsilon,\nu}(\tau/\epsilon)-\bar\theta_\nu(\tau)\|_{raw}
   \longrightarrow0.
   \tag{4}
   \]
   Prediction converges uniformly over the whole circle; both hidden
   activations converge uniformly in input in population `L2`.
3. At separately fixed `epsilon>0` and `nu`, actual finite GF retains its
   actual Gaussian readout and converges in probability to the mixture
   population prediction in `C([0,tau_0/epsilon] x sqrt(2)S1)`. Joint
   same-array reference/mixture programs give paired hidden observation
   limits at finitely many inputs or integrated over any fixed observation
   law. Thus width first and epsilon second give (3).
4. For a deterministic modulus `Psi(a)->0`, depending only on the common
   episode and `Y`,
   \[
   \sup_{\tau\le\tau_0}\|\bar\theta_\nu(\tau)-\bar\theta_\lambda(\tau)\|_{raw}
   \le\Psi(\mathcal W_1(\nu,\lambda)).
   \tag{5}
   \]
   Prediction and hidden differences obey the same modulus up to fixed
   constants. Section 7 separates sampling and centered noise.

This is a finite-episode result, with no simultaneous width/epsilon rate or
GD extension. Uniform strict risk decrease over all Borel laws is not
claimed: an added fitted-anchor law gives zero projected force.

## 2. Source bounds independent of spatial slot count

Use C.4.9 unit A with arbitrary `J`, the same two reference slots, and zero
reference coefficients elsewhere. Its constants are independent of `J`.
The following audits the full proof, beyond the shorter A.1 independence
list. For nonzero slots let

\[
m_{kj}=|\gamma_{kj}|+|\bar\gamma_{kj}|,\quad m_k=\sum_jm_{kj},\quad
e_p=|\gamma_p-\bar\gamma_p|/m_p.
\]

Then `sum_p m_p e_p=q` and `sum_p m_p<=2L_*+1`. Every spatial summation in
CT12–CT45 uses these masses. Directions enter only through `|u|=1`,
`|u.v|<=1`, and bounded tanh. CT29–CT31 attach `|gamma_p|` to each old
source pulse. CT28 uses weighted Jensen, not a Gaussian maximum over the
input/time list. CT40 divides by `m_p`; CT41 sums against `m_p`, and
CT43–CT44 exchange finite sums with bounded total mass. CT36 explicitly
states independence of source-slot number; its Gronwall factor depends on
`sum m_k`. Hence the closing `delta` in CT45 is uniform in `J`.

The A.4 raw reference anchor has only two nonzero controls. Extra zero slots
have no later influence, by A.3's chronological induction. A passive query
adds only one distinguished current source, never an accumulating diagonal.
Coincident or antipodal inputs and zero masses do not require a new case:
the complete singular-query proof retains distinct formal names.

The reference anchor, its raw/clock defect estimate and the A-supplement
were read in full. They take width first at fixed graph/forcing, then remove
forcing, then prove the mesh-uniform cap; normalized defects are summed
against source mass. No graph-size constant survives in their final cap.

Thus a single source tube supplies, uniformly over all such finite programs,

\[
\|c\|_\infty\le L,\quad\|K\|_{HS}\le L^2/2,\quad\|A\|\le2+L^2/2,
\quad\sup_u\|Q(u)\|_p\le C_p,\quad
\sup_u\tau_R(Q(u))\le Ce^{-cR^2},
\tag{6}
\]

where `L=10+delta` and every finite `p` is fixed separately. These are
marginal bounds for deterministic inputs, not a random uncountable supremum.
Minkowski applied to the full-row update additionally gives

\[
\|w\|_{L^p(\Omega_1;\mathbb R^2)}
\le\|g\|_p+\sum_{k,j}|\gamma_{kj}|\|Q_{kj}\|_p
\le\|g\|_p+LC_p.
\tag{7}
\]

Only the two-anchor Gram is needed below. Its positivity can be recovered
without importing the unread C.4.6 cavity dependencies. Along the reference,
`F(w_a)=F(g_a)+X_a`, `F'=cosh^2`, and `X_a=integral y_a Q_a/2` in feature
time. The Gaussian-plus-bounded decomposition proved by unit A and C.4.5.2
implies `||Q_a(s)||_p<=C sqrt(p)` on the bounded feature segment. Put

\[
N=\tfrac12\int_0^{s_\dagger}(|Q_1(s)|+|Q_2(s)|)ds.
\]

Then `||N||p<=C sqrt(p)` and `sup_s |X_a(s)|<=N` by Minkowski/Fubini.
Markov with `p` proportional to `r^4` gives
`Pr(N>r^2)<=exp(-c r^4)`. For any `v` with nonzero coordinates the
Gaussian box `|g-rv|_infty<=1` has probability at least
`c_v exp(-C_v r^2)`, so it intersects `N<=r^2` with positive probability
for large `r`. There `F` monotonicity and its exponential derivative give
`sup_s |w_a(s)-g_a|<=C r^2 exp(-2r|v_a|+2)->0`.
An almost sure linear dependence between `tanh(w_dagger.e1)` and
`tanh(w_dagger.e2)` therefore induces a dependence between their sign
patterns in every such direction `v`. Changing one sign forces the
corresponding coefficient to vanish. The first-feature Gram is positive.
Also `c_dagger!=0` because it fits an anchor, and strictly positive upper
gates make both `delta(ea)` nonzero in `L2`. Pointwise application of the
first-feature Gram inequality followed by integration gives

\[
\left\|\sum_a b_a\delta_a\otimes H_a^1\right\|_{HS}^2
\ge\lambda_{min}(\operatorname{Gram}(H_1^1,H_2^1))
       \sum_a b_a^2\|\delta_a\|_2^2.
\tag{8}
\]

The middle blocks alone prove `M_dagger>0`. No added-input Gram is inverted.

## 3. Spatial regularity and one-reference comparison

At a source-tube state, for `h=|u-v|`, factor subtraction gives

\[
\|H^1(u)-H^1(v)\|_2\le\|w\|_2h,
\quad\|Z^2(u)-Z^2(v)\|_2\le\|A\|\|w\|_2h,
\tag{9}
\]

with the same bound for `H2`. As `|phi''|<=2`,

\[
\|\delta(u)-\delta(v)\|_2\le2\|c\|_\infty\|A\|\|w\|_2h,
\quad\|Q(u)-Q(v)\|_2\le2\|A\|^2\|c\|_\infty\|w\|_2h.
\tag{10}
\]

For the first-row gradient, subtract its explicit vector, query and gate.
The first two changes cost `Ch`; the gate change costs

\[
\|[\phi'(w\cdot u)-\phi'(w\cdot v)]Q(v)\|_2
\le2h\||w|Q(v)\|_2\le2h\|w\|_4\|Q(v)\|_4\le Ch.
\tag{11}
\]

The rank difference identity controls the middle block and (9) controls
the readout block. Consequently

\[
\|g_\theta(u)-g_\theta(v)\|_{raw}\le C|u-v|,
\quad \operatorname{Lip}_u f_\theta\le\|c\|_2\|A\|\|w\|_2\le C.
\tag{12}
\]

This is the required quantitative spatial regularity. In particular
`(u,y)->(f_theta(u)-y)g_theta(u)` is `C_Y`-Lipschitz on `Z_Y`. Its range
is compact in the raw Hilbert space, hence separable and Bochner integrable.

For state comparison put `d=||theta-bar theta||raw`, with only the barred
state required to bear (6). The forward maps and prediction are Lipschitz
on a bounded raw/action ball. Upper-gate subtraction is
`(c-bar c)phi'(Z)+bar c[phi'(Z)-phi'(bar Z)]`, which costs `Cd`.
The remaining lower product is at most

\[
\|[\phi'(w\cdot u)-\phi'(\bar w\cdot u)]\bar Q(u)\|_2
\le2Rd+2\tau_R(\bar Q(u)).
\]

Optimize `C(1+R)d+Ce^{-cR^2}` with `R` proportional to
`sqrt(log(e/d))`. This gives `C omega(d)`, where

\[
\omega(d)=d\sqrt{\log(e/d)}\ (0<d\le1),\qquad\omega(0)=0.
\tag{13}
\]

Extend it increasingly beyond 1. Its reciprocal integral diverges at zero.
Bounds (6)–(7) survive strong completion: readout bounds pass by an almost
sure subsequence; queries pass using
`tau_(2R)(Q)<=2||(|Q|-R)_+||2` and continuity of the positive-part norm;
row moments pass by Fatou. Thus (9)–(13) apply to the constructed limits.
Moreover raw convergence gives query convergence in `L2` by factor
subtraction with the bounded comparison readout. Interpolation against the
uniform `L8` bounds gives convergence in `L4`. Thus the query maps and row
velocities used in measure/time integrals are strongly measurable into
`L4`; their Bochner integrals obey the Minkowski estimates used below.

Scalar-gradient continuity and (8) give `rho,kappa>0` with
`M>=4 kappa I` on `N={||theta-theta_dagger||raw<rho}`. There the inverse
identity and bounded Gram factors give

\[
\|V_\nu(\theta)-V_\lambda(\bar\theta)\|_{raw}
\le C_Y\omega(d)+C_Y\mathcal W_1(\nu,\lambda).
\tag{14}
\]

For the law term, couple the laws and integrate (12) at the barred state.
For the projector, expand `GM^{-1}G*` and use
`M^{-1}-bar M^{-1}=M^{-1}(bar M-M)bar M^{-1}`. The same comparison applies
to the bounded coefficients

\[
B=GM^{-1},\qquad b_\nu=2M^{-1}G^*v_\nu.
\tag{15}
\]

If `D(t)<=a+C integral_0^t omega(D(s))ds`, then for sufficiently small `a`
on a fixed bounded interval,

\[
D(t)\le\mathcal O_t(a):=
e\exp\{-\big(\sqrt{\log(e/a)}-Ct/2\big)^2\}.
\tag{16}
\]

Indeed its integral upper comparison `Z` obeys `Z'<=C omega(Z)`, so
`(sqrt(log(e/Z)))'>=-C/2`. Choose `a` small so the parenthesis stays
positive and `Z<1`; a first-exit argument validates these restrictions.
For larger `a`, bound by the common raw diameter. At zero let `a` decrease
to zero to obtain uniqueness.

## 4. Construction of the constrained Borel flow

For a finite law `nu=sum_j p_j delta_(u_j,y_j)`, the constrained field has
anchor coefficients `b_nu` and added coefficients `-2p_j(f(u_j)-y_j)`.
On `N` their total absolute mass per slow-time unit is at most `A_Y`;
the raw speed is at most `V_Y`. Both constants use `sum p_j=1`.

Append constrained Euler to successively longer reference raw-Euler
prefixes approaching `theta_dagger`, retaining the entire history. Choose
`tau_0>0` with

\[
A_Y\tau_0<\delta_{src}/8,\qquad V_Y\tau_0<\rho/8.
\tag{17}
\]

Make prefix endpoint, reference-control approximation and omitted suffix
errors smaller than the corresponding eighth margins. The full appended
history is source admissible before invoking (6). Comparison of two
interpolants by (14)–(16), with preceding-node errors controlled by the
speed times the mesh, makes them Cauchy as prefixes and meshes converge.
The integral equation passes to a strong solution. This is the full C.4.9
C.4 construction with a mass-bounded finite sum; §2 checks its uniformity.

For Borel `nu`, choose finite maps `T_l:Z_Y->Z_Y` with
`sup_z d_Z(T_lz,z)<=h_l->0`, and set `nu_l=(T_l)#nu`. Arbitrary real
weights are represented by the III.F common-carrier completion. Then

\[
\sup_{\tau\le\tau_0}\|\bar\theta_{\nu_l}(\tau)-\bar\theta_{\nu_k}(\tau)\|_{raw}
\le\mathcal O_{\tau_0}(C_Y\tau_0(h_l+h_k)).
\tag{18}
\]

The resulting limit is independent of quantization. Bounds (6)–(7) pass;
(14) makes its integrand errors uniformly small, so (2) holds. Its field
is continuous and hence the solution is strongly `C1`. A countable dense
family of finite laws suffices on the prescribed carrier; this estimate
extends uniquely to all laws without new independent Gaussian carriers.

Integrating (14) proves (5) with
`Psi(q)=O_(tau_0)(C_Y tau_0 q)` near zero. The one-reference inequality
also compares any other strong raw solution to the constructed one, proving
uniqueness on `N` and from each reached state on the remaining interval.
It is not an arbitrary-state existence assertion. Finally the scalar chain
rule gives `d(f(e1),f(e2))/d tau=G*V_nu=0`.

## 5. Original-initialization continuation and the singular clock

The following quantities are uniform over finite support and then pass to
Borel laws. Write `r=(f(e1)-1,f(e2)+1)`. Exact physical GF is

\[
\theta'=-(1-\epsilon)Gr-2\epsilon v_\nu,\qquad
r'=-(1-\epsilon)Mr-2\epsilon G^*v_\nu.
\tag{19}
\]

Its tagged controls are the two anchor coefficients and the signed added
measure `-2epsilon(f-y)nu`. Slots remain tagged when an added atom coincides
with an anchor. Their absolute mass is bounded by `C_Y(|r|+epsilon)` on `N`.

For each separately fixed physical prefix `b`, every finite mixture Euler
program has `||c_k||infty<=Y(e^(2b)-1)` and bounded raw speed, action and
row norms, uniformly in the law and fine mesh. The readout bound follows
from `|f|<=||c||infty`, unit law mass and discrete Gronwall; summing its
bounded-activation updates gives the other bounds. Compare this arbitrary
mixture Euler program with the existing reference GF, using only reference
tails. The cutoff comparison of §3 gives, with maximal physical mesh `h`,

\[
\sup_{t\le b}\|\theta^h_{\epsilon,\nu}(t)-\theta_*(t)\|_{raw}
\le C_b e^{C_b(1+R)b}
  \{(1+R)(\epsilon+h)+e^{-cR^2}\}=:\omega_b(\epsilon+h).
\tag{20}
\]

Here `R` is chosen proportional to `sqrt(log(e/(epsilon+h)))` with a
sufficiently large fixed factor, making `omega_b(z)->0`. At the reference
state the changed force is `O_Y(epsilon)`, because the added law has mass
one and bounded labels. Prediction continuity also gives the tagged
integrated control discrepancy

\[
D^h_{\epsilon,b}:=\int_0^b\left[
 \sum_{a=1}^2|a_a^h-a_{*,a}|+
 2\epsilon\int|f_{\theta_k^h}(u)-y|\,d\nu\right]dt
\le C_b(\epsilon+h+\omega_b(\epsilon+h)).
\tag{21}
\]

This precedes any changed-program source cap. For small `epsilon+h`, the
prefix is strictly source admissible, and its now capped Euler refinements
have a Cauchy completion on `[0,b]`.

Continue the Euler program after a node at `b` with its actual mixture
residuals. Stop at inner radii `rho/2,delta_src/2`, with outer radii
`rho,delta_src`. Choose the step so every affine segment from an inner
node remains within the outer regions and meets the source control-mesh
bound. An intermediate affine point is obtained by a fractional version of
the last controlled Euler update; SCT therefore bounds its passive queries.
This observation is needed for the residual Taylor estimate below.

The fixed node velocity on such a segment has row `L4` norm at most
`C_Y(|r_k|+epsilon)` by (6), and readout derivative pointwise at most that
quantity. Strong differentiation of forward maps and actual adjoints gives

\[
(Z^2(u))'=K'H^1(u)+A[\phi'(w\cdot u)w'\cdot u],
\]
\[
\delta(u)'=c'\phi'(Z^2(u))+c\phi''(Z^2(u))(Z^2(u))',
\quad Q(u)'=K'^*\delta(u)+A^*\delta(u)'.
\]

Their `L2` norms are at most `C_Y(|r_k|+epsilon)`. The derivative of an
anchor row gradient additionally contains `(w'.ea)Q(ea)`, whose `L2`
norm is at most `||w'||4||Q(ea)||4`. Hence each anchor gradient derivative
is bounded in raw norm by the same quantity. A second integration of the
scalar chain rule proves the exact residual expansion

\[
r_{k+1}=[I-h_k(1-\epsilon)M_k]r_k
 -2h_k\epsilon G_k^*v_{\nu,k}+R_k,
\quad |R_k|\le C_Yh_k^2(|r_k|+\epsilon)^2.
\tag{22}
\]

With `epsilon<=1/2`, `M>=4kappa I`, and `h_k M_max<=1`, the first factor
has norm at most `1-2kappa h_k`. Outer-region residuals are bounded.
Decrease the step so the quadratic remainder can be absorbed; this gives

\[
|r_{k+1}|\le(1-\kappa h_k)|r_k|+C_Yh_k\epsilon,
\qquad\sum_{k:b\le t_k<t_N}h_k|r_k|
\le C_Y|r_b|+C_Y\epsilon(t_N-b).
\tag{23}
\]

The sum follows by telescoping, with no `hT` accumulation. The post-prefix
control mass and displacement have the same bound. Keeping the reference
running throughout, the full source distance through `T=b+tau_0/epsilon`
is bounded by

\[
D^h_{\epsilon,b}+(s_\dagger-s_*(b))+C_Y|r_b|+C_Y\tau_0.
\tag{24}
\]

Choose `b` large so the reference endpoint error, residual and suffix mass
are far smaller than the inner margins. Then choose `epsilon+h` small in
(20)–(21), and decrease the fixed positive `tau_0` so its last term and
displacement use less than one quarter of both inner margins. A first
exiting node would remain strictly inside by (23)–(24), a contradiction.
Thus the histories continue through `T` with uniform source bounds.
For each fixed positive `epsilon`, one-reference Osgood comparison makes
their vanishing-mesh limits Cauchy. This constructs original mixture GF.

For Borel laws use the finite quantizations of §4. At this fixed finite
physical horizon, the equal-state law discrepancy is
`C_Y epsilon W1(nu_l,nu_k)` by (12). Integrating the Osgood inequality
makes these finite-law paths Cauchy. Equations (19), (23)–(24), tails and
raw bounds pass to the unique Borel limit. The constants used for exit are
independent of quadrature. This includes every fixed empirical law,
including repeated samples and degenerate support configurations.

The continuous residual equation gives

\[
|r(t)|\le e^{-2\kappa(t-b)}|r(b)|+C_Y\epsilon,
\quad\int_b^t|r(s)|ds\le C_Y|r(b)|+C_Y\epsilon(t-b).
\tag{25}
\]

To prove this, pair the second equation of (19) with `r/|r|`, use the
Gram lower bound and bounded added force, and regularize the norm at zero.
For general measure controls, Minkowski replaces the sums in the preceding
derivative argument. In particular `||w'||4<=C m(t)` and the readout
derivative is pointwise at most `m(t)`, where
`m(t)<=C_Y(|r(t)|+epsilon)`.

Here are the regularity details needed for integration by parts. The `L2`
strong equations and their integrable velocity bounds give coordinatewise
absolutely continuous representatives by Fubini. Apply the ordinary scalar
chain rule to tanh almost everywhere. The resulting derivatives are
Bochner integrable in `L2`, so their integrals equal the strong differences.
The bounded readout handles its product with `(Z2)'`. For gradients the
only additional factor is `w' Q`, controlled by the two `L4` bounds.
This proves the fundamental theorem for their derivatives, not just a
formal Hessian calculation. Therefore `G` is absolutely continuous with
`||G'||<=C m(t)`. The finite inverse product rule gives

\[
B'=G'M^{-1}-GM^{-1}(G'^*G+G^*G')M^{-1},\qquad
\|B'\|\le C_Y(|r|+\epsilon).
\tag{26}
\]

Multiplying the residual equation by `B=GM^{-1}` gives the exact identity

\[
\theta'=\epsilon V_\nu(\theta)+B(\theta)r'.
\tag{27}
\]

The exact anchor weights are included in (19); this identity would change
if they were silently rescaled. Its justified product integration yields

\[
\theta(t)=\theta(b)+B(t)r(t)-B(b)r(b)
 +\epsilon\int_b^tV_\nu(\theta(s))ds-\int_b^tB'(s)r(s)ds.
\tag{28}
\]

Equations (25)–(26) bound the last integral by
`C_Y(|r(b)|^2+epsilon|r(b)|+epsilon^2(t-b))`. At
`tilde theta_(epsilon,b,nu)(tau)=theta_(epsilon,nu)(b+tau/epsilon)`, (28)
is (2)'s integral equation plus an error, uniform in `nu,tau<=tau_0`, of
norm at most

\[
C_Y\{\|\theta_{\epsilon,\nu}(b)-\theta_\dagger\|_{raw}
       +|r_{\epsilon,\nu}(b)|+|r_{\epsilon,\nu}(b)|^2+\epsilon\}.
\tag{29}
\]

At fixed `b`, the epsilon-limsup is at most `C exp(-b/5)` by the established
reference endpoint convergence and (20). Compare with (2) using (14) with
the constrained path as the tail-bearing side. Equation (16) followed by
`b->infinity` proves shifted capture. For unshifted `tau>=tau_->0`, write
`sigma=tau-epsilon b`; the slow path difference is at most
`V_Y epsilon b`. This proves (4). The reference continues at these same
physical times and converges to `theta_dagger`. Capture cannot include
zero slow time. There is no pretraining stage or reset in any actual run.

## 6. Actual finite GF for a Borel training integral

Fix `epsilon>0` and `T=tau_0/epsilon<infinity`. At each width the Borel-law
gradient is smooth in finite parameters: on compact parameter sets its
integrand derivatives are bounded uniformly over the compact data space,
so differentiation under the law integral is justified. Loss dissipation
gives `integral_0^T ||theta_n'||raw^2<=L_n(0)`, bounding displacement by
`sqrt(T L_n(0))`. Also

\[
\|c_n(t)\|_\infty\le\|c_n(0)\|_\infty+2T\sqrt{L_n(0)}.
\tag{30}
\]

The action is its initialized action plus a Frobenius increment, so these
bounds prevent finite-time escape and prove global finite GF. They are
uniform on initial events whose probabilities tend to one.

Take a finite quadrature `nu_l` with `W1(nu,nu_l)<=h_l`, and a fixed
population Euler partition for its actual mixture. Freeze that population
program's scalar coefficients and run it on the actual arrays. It is a
fixed finite transcript before width grows. III.F and global-nonlinear
A.1–A.2 identify its values and second moments. To retain its actual readout,
use the fixed-program oracle comparison proved in C.4.9 D.2. The initial
readout maximum tends to zero since
`Pr(max_j|c0,j|>a)<=2n exp(-n^2 a^2/2)`, and its RMS tends to zero.
At each changed gate, split the fixed oracle factor at a cutoff, pass the
oracle soft-tail second moment at fixed transcript, and remove the cutoff.
Induction gives the actual-readout proxy's joint law. No finite array is reset.

The additional step for Borel training is explicit. Couple `nu` to `nu_l`.
For a pair of inputs `u,v`, finite forward/action subtraction gives
`C_T(d_n+|u-v|)`, where
`d_n^2=||Delta W1||F^2/n+||Delta W2||F^2+||Delta c||2^2/n`.
Splitting the lower gate against the proxy query gives

\[
\|g_{n,\theta}(u)-g_{n,\bar\theta}(v)\|_{raw}
\le C_T(1+R)(d_n+|u-v|)+C_T\tau_{R,n}(\bar Q(v)).
\tag{31}
\]

Every vector block here has its explicit RMS norm. For the middle block,
`||ab^T/n||F=(||a||2/sqrt(n))(||b||2/sqrt(n))`. Readout suprema from
(30) and the proxy control bound handle the upper gate. Residual changes
cost `C_T(d_n+|u-v|+|y-z|)`. Integrating over the coupling adds
`C_T(1+R)h_l` and a proxy-weighted finite sum of query tails. The anchors
are coupled identically. No supremum over random feedback controls is used.

Let `h` be maximal physical mesh and `zeta_(n,h,l)` the finite maximum
coefficient-prediction discrepancy of the proxy. Exactly C.4.9 D.2's
one-reference comparison, with this extra transport term, gives

\[
\sup_{t\le T}d_n(t)\le C_Te^{C_TR}\left[
 (1+R)(h+h_l+\zeta_{n,h,l})
 +\sup_t\sum_jp_j\tau_{R,n}(Q_{proxy}(t,u_j))
 +\sup_t\tau_{R,n}(c_{proxy}(t))\right].
\tag{32}
\]

Both states have identical initial arrays. The constants can be fixed
independently of quadrature using the uniform population proxy control
mass and raw bounds, together with the initial events above. At fixed
`l,h,R`, `zeta` vanishes in probability. Proxy soft tails converge by its
fixed-program second-moment law. Finite interpolation grids and `L2`
Lipschitz bounds for `Q,c` extend their convergence over interpolation
time. The hard/soft inequality
`tau_(2R,n)(Q)<=2||(|Q|-R)_+||2/sqrt(n)` bounds the width-limsup of the
tail term by `C exp(-cR^2)`, uniformly in quadrature and fine mesh.
Given an error, choose `R` first, then finite `l` and `h` controlling the
amplified transport/mesh errors, and finally let width increase. Strong
population quadrature/mesh completion identifies the unique mixture path.

Finite and population prediction input Lipschitz constants are bounded by
the product of readout RMS/`L2`, action norm and first-row RMS/`L2`.
Hidden activations have the corresponding bounds (9). Finite input/time
nets therefore yield whole-circle/time prediction convergence.
For paired observations use the union of reference and mixture proxy
programs on the same arrays. Paired hidden products are bounded admissible
observations; RMS hidden error transfers their limits to the actual flows.
Uniform input Lipschitz bounds then permit integration against a fixed
observation law on the circle.

Take width first at each fixed epsilon, then apply (4) as epsilon decreases.
This proves the nonlinear prediction and paired reference-endpoint limits.
For a random empirical added law independent of initialization, condition
on its realized samples. The result holds for every such fixed law, not
merely almost every law in an auxiliary parameterization. Conditional
failure probabilities tend to zero and are bounded by one; dominated
convergence gives the unconditional result. No width rate uniform in sample
size or epsilon is inferred.

## 7. Sampling bridge with centered noise separated

For the frozen class write `nu_X=lambda` and `Y=q(U)+xi`, with
`E[xi|U]=0`, `E[xi^2|U]<=sigma^2`. Population dynamics depend only on
`lambda,q`: the integrand in (1) is affine in `y`, so

\[
v_\nu(\theta)=\int(f_\theta(u)-q(u))g_\theta(u)\,d\lambda(u).
\tag{33}
\]

Let `m` denote sample count, and `hat nu_m,hat lambda_m` the empirical
joint and input laws. This sample count is distinct from the target's
Fourier cutoff `N`. Anchor weights remain their exact known halves.
At the deterministic population slow path `theta(tau)=bar theta_nu(tau)`,
put

\[
Z_m(\tau)=m^{-1}\sum_{i=1}^m\xi_i g_{\theta(\tau)}(U_i).
\tag{34}
\]

Independence and conditional zero means cancel all off-diagonal terms in
the raw Hilbert squared norm, giving

\[
E\|Z_m(\tau)\|_{raw}^2\le C\sigma^2/m,\qquad
E\int_0^{\tau_0}\|Z_m(\tau)\|_{raw}d\tau\le C\tau_0\sigma/\sqrt m.
\tag{35}
\]

The gradient's uniform bound justifies all integrals by Fubini. The sample
path does not occur inside `Z_m`; feedback is handled by the one-reference
state comparison, without conditioning on trained empirical features.

The frozen target has a uniform circular Lipschitz bound. Since `s>=1`,
`sum frequency*(|a_k|+|b_k|)<=R`; thus `||v||infty<=R`, `Lip(v)<=R`.
The product `sin^2(2alpha)v` has Lipschitz constant at most `3R`, while
the derivative of the cubic part has magnitude at most 6. Therefore

\[
\operatorname{Lip}(q)\le L_q:=6+3R\le51/8.
\tag{36}
\]

The infinite-series version satisfies the same bound by uniform convergence
of both its series and its absolutely summable derivative series.
At the deterministic population path, `(f_theta-q)g_theta` is
`C(1+L_q)`-Lipschitz in circular arc distance by (12). Its noiseless
empirical integral error is at most
`C(1+L_q)W1(hat lambda_m,lambda)`. For its remaining noise error use (34).
At the changed empirical state apply (14) with the population state on
the tail-bearing side. Integration gives the pathwise bound

\[
\sup_{\tau\le\tau_0}
\|\bar\theta_{\hat\nu_m}(\tau)-\bar\theta_\nu(\tau)\|_{raw}
\le\mathcal O_{\tau_0}(A_m),
\]
\[
A_m=C\tau_0(1+L_q)\mathcal W_1(\hat\lambda_m,\lambda)
          +2\int_0^{\tau_0}\|Z_m(\tau)\|_{raw}d\tau.
\tag{37}
\]

The large-argument extension of `O` uses the common raw diameter as in
(16). The noise factor 2 comes from (1); the projector has norm one.
This holds for every empirical law on the probability-one event of the
prescribed label bound.

An elementary one-dimensional calculation makes the input term explicit.
Cut the circle at zero and let `F_m,F` be empirical/population CDFs on
`[0,2pi]`. Couple their quantiles with one uniform variable. The distance
between two real points equals the integral of the absolute difference of
their threshold indicators. In a quantile coupling those two indicators
are nested events at each threshold. Fubini therefore gives coupling cost
`integral_0^(2pi)|F_m(a)-F(a)| da`. Circular distance is no larger, and the
variance of an empirical threshold average is `F(a)(1-F(a))/m`. Hence

\[
E\mathcal W_1(\hat\lambda_m,\lambda)
\le\int_0^{2\pi}\sqrt{F(a)(1-F(a))/m}\,da\le\pi/\sqrt m.
\tag{38}
\]

Combining (35), (37) and (38) yields

\[
E A_m\le C\tau_0(1+L_q+\sigma)/\sqrt m.
\tag{39}
\]

For every `0<eta<1`, Markov's inequality gives probability at least `1-eta`
that (37)'s argument is no more than
`C tau_0(1+L_q+sigma)/(eta sqrt(m))`. This conservative high-probability
estimate separates centered noise and design variation. The constants do
not depend on the target Fourier cutoff `N`.

Whole-circle prediction error is bounded by a fixed constant times raw
error. For excess test risk, subtract the two squared errors and use the
common prediction bound: the risk discrepancy is at most
`2(sup|P|+1) sup|P_emp-P_pop|`. All bounds are uniform over the episode,
so they hold at every data-selected stopping time in `[0,tau_0]`. This
controls sampling at a separately supplied stopping rule; it does not
itself give a target-dependent improvement margin. Actual finite transfer
takes width first, epsilon second and sample count last, by §6's conditional
argument followed by (37)–(39).

## 8. Exact risk identity and the remaining learning obligation

The strong scalar chain rule, bounded gradients and differentiation under
the law integral give the exact nonlinear identity

\[
\frac d{d\tau}R_\nu(P_\nu(\tau))
=-4\|\Pi_{\bar\theta_\nu(\tau)}v_\nu(\bar\theta_\nu(\tau))\|_{raw}^2.
\tag{40}
\]

For the frozen class this is also the derivative of excess test risk: the
irreducible conditional variance is constant. Hidden features and the
projector continue changing in this equation.

A useful conditional criterion is as follows. Suppose a family of laws has

\[
\|S_\nu\|\ge a_0>0,\qquad\|(S_\nu)_h\|\ge j_0>0,
\qquad S_\nu=\Pi_\dagger v_\nu(\theta_\dagger),
\tag{41}
\]

where `h` comprises the first-row and middle blocks. The endpoint continuity
estimate (13) and common speed bound let one shrink the common positive
episode so the projected norm remains at least `a_0/2`. Then (40) gives
risk gain at least `a_0^2 tau_0`.

For upper-hidden adaptation put
`beta_nu=M_dagger^{-1}G_dagger^*v_nu(theta_dagger)`. Keep its coefficients
and endpoint readout fixed in the hidden scalar functional

\[
O_\nu(\theta)=\int(f_\dagger(u)-y)
 \langle c_\dagger,H^2_\theta(u)\rangle\,d\nu
-\sum_{a=1}^2(\beta_\nu)_a
 \langle c_\dagger,H^2_\theta(e_a)\rangle.
\tag{42}
\]

Its endpoint hidden gradient is `(S_nu)_h`, and its readout gradient is
zero. Thus along (2), `O_nu'(0)=-2||(S_nu)_h||^2<=-2j_0^2`.
The fixed-readout gradient is uniformly continuous in raw state by the
endpoint `L4`/bounded-multiplier argument of C.4.9 B.3–B.4, also obtained
by the cutoff argument of §3 with the fixed endpoint readout. Coefficient
total variation in (42) is bounded in terms of `Y` and the anchor gap.
Shrink the interval so `O_nu'<=-j_0^2`. Cauchy–Schwarz gives

\[
|O_\nu(\theta)-O_\nu(\theta_\dagger)|^2
\le C_Y\left[\int\|H^2_\theta(u)-H^2_\dagger(u)\|_2^2d\nu_X(u)
 +\sum_{a=1}^2\|H^2_\theta(e_a)-H^2_\dagger(e_a)\|_2^2\right].
\tag{43}
\]

For example the integral term is bounded by
`||c_dagger||2 ||f_dagger-y||L2(nu)` times the square root of its displayed
hidden integral, and the anchor term by `||c_dagger||2 |beta_nu|` times
the square root of the anchor sum. Squaring their sum proves (43).
The bracket is therefore at least `j_0^4 tau_0^2/C_Y`. Divide by three
to obtain the probability observation law
`(nu_X+delta_e1+delta_e2)/3`, adjusting the constant. Law continuity in
(12) makes strict endpoint bounds of the form (41) an open condition in
`W1`, so a verified witness would give a robust subfamily.

This does not establish a witness inside the frozen full-support Fourier
class. Nor does (40) supply a target-dependent approximation floor or
quantitative contraction by itself. Those are the remaining learning
obligations. This route supplies the nonlinear population/empirical
evolution, common positive existence episode, original-initialization
capture, spatial regularity, centered-noise sampling control and actual
finite-GF transfer needed to use a separately verified witness.

## 9. Adversarial checks and status

- Tiny, zero or arbitrarily many masses: every source estimate uses total
  mass, and old response bounds retain their injection mass.
- Identical/antipodal inputs: formal source names are retained; no added
  Gram inverse occurs. Only the fixed two-anchor Gram is inverted.
- Borel quadrature: (9)–(12) prove uniform spatial regularity, and §§4–6
  explicitly remove quadrature. Pointwise continuity is not substituted
  for a uniform approximation estimate.
- Initial layer: prefixes compare the unchanged mixture from original
  initialization; the zero slow-time endpoint is correctly excluded.
- Finite readout: it remains in both actual flow and finite proxy.
- Width order: every transcript and quadrature is fixed before the
  fixed-program theorem; no growing-program width claim is used.
- Empirical noise: centering is used at the deterministic population path;
  one-reference comparison treats the empirical feedback.
- Universal strict gain is false and expressly excluded. A robust witness
  in the frozen class and a useful approximation/contraction statement are
  separate, still unproved by this route.

Verification performed: the author's line-by-line dependence audit and the
persisted derivations against the recorded source hashes. No independent
review, machine proof, training or numerical constant evaluation was done.
Thus this is a **candidate proof**, not internally checked or promoted.
