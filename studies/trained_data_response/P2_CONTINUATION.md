# P2 continuation route: exponential tails suffice; their persistence remains open

Author: `/root/p2_continuation`, fresh scoped author, 2026-09-11.
Status: conditional theorem and auxiliary lemmas proved below; the requested
nonlinear neighborhood theorem is **not proved**. No training experiment was
run. This is study material, not a proposed established-book addition.

## 1. Contract and strongest conclusion

The target is a genuine radius `rho>0` about
`nu*=1/2 delta_(sqrt(2)e1,+1)+1/2 delta_(sqrt(2)e2,-1)` in the Wasserstein
metric with cost `|x-x'|/sqrt(2)+|y-y'|`, relative to all Borel probability
laws on `sqrt(2)S1 x [-Y,Y]`, `Y>=1`. It asks for autonomous, uniquely
restartable strong population GF through physical time `T=40`, continuity
of its full raw state in the law, and finite-GF capture for every
simultaneous empirical-law/width limit, without a relative rate.

The exact model has two equal-width tanh hidden layers, no biases,
independent centered Gaussian stored variances `(1,1/n,1/n^2)`, mobilities
`(n,1,n)`, and unhalved exactly integrated mean-square loss. The initial
population state is `(g,A0,0)`, with the full two-coordinate Gaussian row,
the canonical Gaussian action, and its actual adjoint. A finite actual
readout is retained. The state is

\[
 \mathcal E=L^2(\Omega_1;\mathbb R^2)\oplus
 \mathcal S_2(H_1,H_2)\oplus H_2,
 \qquad \theta=(w,K,c),\quad A=A_0+K.
\]

We use the equivalent sum distance

\[
 d(\theta,\bar\theta)=\|w-\bar w\|_2+
 \|K-\bar K\|_{HS}+\|c-\bar c\|_2.                 \tag{1}
\]

Its finite same-width version is
`||w-wbar||F/sqrt(n)+||K-Kbar||F+||c-cbar||2/sqrt(n)`.
No cross-carrier operator distance is introduced.

The central result of this route is the following sufficient criterion:
**uniform exponential, rather than Gaussian, integrated backward tails
on the finite-law raw Euler family through 40 imply the entire target**.
The proof below includes law completion, raw HS convergence, uniqueness,
restart, and the simultaneous finite-GF comparison. The supplied sources
do not verify that exponential-tail premise on any fixed positive ball
through 40. Compactness of an already constructed path, finite-time
energy bounds, or fixed positive proximity to the reference do not fill
that gap.

## 2. Exact field and unconditional bounds

Put `u=x/sqrt(2)`, `phi=tanh`, and, on the respective layer spaces, define

\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad
 H^2(u)=\phi(Z^2(u)),\quad f(u)=\langle c,H^2(u)\rangle,
\]
\[
 r(u,y)=f(u)-y,\quad \delta(u)=c\phi'(Z^2(u)),\quad
 Q(u)=A^*\delta(u).
\]

The exact autonomous field is

\[
 F_\mu(\theta)=-2\left(
 \int r\phi'(w\cdot u)Q(u)u\,d\mu,
 \int r\delta(u)\otimes H^1(u)\,d\mu,
 \int rH^2(u)\,d\mu\right).                         \tag{2}
\]

The rank means `(a tensor b)v=a E[bv]`, and its finite representative is
`ab^T/n`. In particular the middle norm in (1) is the correct raw metric.

### 2.1. Global bounds for every finite raw Euler calculation

Fix any finite mesh with nonnegative steps summing to at most `T` and any
probability law. A coarse, law-independent bound exists without a discrete
energy inequality. If `c0=0`, the node supremum `C_k=||c_k||infty` obeys

\[
 C_{k+1}+Y\le(1+2h_k)(C_k+Y).
\]

Indeed `|r_k|<=||c_k||2+Y<=C_k+Y` and `|H2|<=1` in the readout update.
Thus `C_k<=Y(e^{2T}-1)=:C_T`. If `||A0||<=M0`, set

\[
 K_T=2T(C_T+Y)C_T,\quad A_T=M_0+K_T,\quad
 W_T=\sqrt2+2T(C_T+Y)A_TC_T.                         \tag{3}
\]

The middle rank bound gives `||K_k||HS<=K_T`, and the row update gives
`||w_k||2<=W_T`. The interpolated states obey the same bounds by convexity
of each norm. Their assigned velocities have a uniform bound

\[
 V_T=2(C_T+Y)(A_TC_T+C_T+1).                         \tag{4}
\]

These are finite for `T=40`, however poor numerically. They do not depend
on atom counts, weights, or ranks. The same argument works on finite
normalized spaces with initial row bound two and initial readout supremum
one, replacing `Y` in the first recurrence by the initial value `Y+1`.
It is an estimate for the actual raw Euler equations, not transformed
Euler or a modified optimizer.

Every separately fixed finite-law Euler calculation exists by direct
recursion on the canonical action spaces: bounded multiplication maps
L2 fields to L2, each rank is HS, and (3) bounds every resulting node.
The finite-program construction in the source supplies this same state
and its actual two action orientations.

### 2.2. Energy and a strong endpoint for any existing strong solution

For any strong solution of (2) on `[0,S)`, with the stated initialization,

\[
 R_\mu(t)+\int_0^t\|\theta'(s)\|_{\rm raw}^2ds=R_\mu(0)\le Y^2.
                                                               \tag{5}
\]

To justify this statement for arbitrary Borel laws, use the strong curve
chain rule for bounded activation derivatives successively through the
forward equations. The three scalar prediction-gradient blocks are
`phi'(w.u)Q(u)u`, `delta(u) tensor H1(u)`, and `H2(u)`.
Their raw norms are bounded uniformly in `u` on every bounded state
interval. Thus the derivative of `r^2` is dominated by an integrable
constant times the continuous raw speed, and differentiation of its data
integral is justified. Pairing the gradient with (2) gives (5), including
the mean-loss factor two. No derivative of an ambient L2 Nemytskii map
is used.

Consequently, for `s<t<S`,

\[
 \|\theta(t)-\theta(s)\|_{\rm raw}\le Y\sqrt{t-s}.    \tag{6}
\]

If `S<infinity`, this proves a strong endpoint in the full raw space.
It also bounds every block displacement by `Y sqrt(S)`.
The readout equation and `int |r| dmu<=sqrt(R)<=Y` give
`||c(t)||infty<=2Yt`. These facts rule out raw norm blowup of an existing
population solution. They do **not** construct a solution starting from
the endpoint: the raw field is continuous there, and local Lipschitzness
on the full L2 space has not been supplied.

The finite-dimensional exact Borel-loss GF does have local smoothness.
On the event `||A0,n||<=10`, `||g_n||F/sqrt(n)<=2`, `||c0,n||infty<=1`,
its initial loss is at most `(Y+1)^2`. The finite version of (5) proves
global finite existence and uniform raw bounds through 40; in particular
the readout supremum is at most `1+2T(Y+1)`. This event tends to probability
one by the initialized Gaussian bounds. These finite existence facts are
unconditional and do not imply a population limit.

### 2.3. The learned transpose term is pointwise bounded

For an existing strong path, the integral of the middle equation gives,
for every fixed deterministic passive `u`,

\[
 (K(t)^*\delta(t,u))(\omega)
 =-2\int_0^t\int r(s,v,y)H^1(s,v)(\omega)
       \langle\delta(s,v),\delta(t,u)\rangle\,d\mu(v,y)ds.
                                                               \tag{7}
\]

The integrand is bounded in absolute value by
`2 |r(s,v,y)| ||c(s)||2 ||c(t)||2`, an integrable deterministic
majorant on a finite interval. It defines an L-infinity representative,
and equality with the HS integral follows first for simple rank sums and
then by their L2/HS limits. Hence

\[
 \|K(t)^*\delta(t,u)\|_\infty
 \le2\|c(t)\|_2\int_0^t\!\int|r(s,v,y)|\,d\mu\,\|c(s)\|_2ds
 \le\tfrac43Y^3t^2.                                  \tag{8}
\]

The last step uses (5), `||c(s)||2<=Y sqrt(s)` and the integral of
`sqrt(s)`. This bound is uniform in passive input. The corresponding
finite sum proof gives for all raw Euler nodes the bound
`2T(C_T+Y)C_T^2`, using (3).

Thus the sole unbounded part of the lower reverse field is the actual
initialized adjoint query `A0*delta`. Bounded `delta` and bounded `A0`
give its L2 norm, not exponential coordinate tails for these adapted
queries. Replacing that query by independent Gaussian noise would remove
the missing issue rather than resolve it.

## 3. The full raw transport estimate

For `tau_R(v)=||v 1_(|v|>R)||2`, define

\[
 \tau_{\nu,R}(\bar\theta)=\tau_R(\bar c)+
           \int\tau_R(\bar Q(u))\,d\nu(u,y).            \tag{9}
\]

On any common ball for the individual row L2, action operator and readout
L2 norms, the established C.4.1 estimate has the following stronger
middle-norm form:

\[
 \|F_\mu(\theta)-F_\nu(\bar\theta)\|_{(1)}
 \le C(1+R)\{d(\theta,\bar\theta)+W_1(\mu,\nu)\}
       +C\tau_{\nu,R}(\bar\theta),\quad R\ge1.          \tag{10}
\]

Here `C` depends only on the state bounds and `Y`. To verify the upgrade,
all forward and adjoint differences use
`||K-Kbar||op<=||K-Kbar||HS`. The only middle velocity operations are rank
differences, for which

\[
 \|a\otimes b-\bar a\otimes\bar b\|_{HS}
 \le\|a-\bar a\|_2\|b\|_2+\|\bar a\|_2\|b-\bar b\|_2.
\]

This is identical to the rank inequality used in C.4.1. For completeness,
the only unbounded coordinate products in that proof are controlled by

\[
 \|[\phi'(z)-\phi'(\bar z)]P\|_2
 \le2R\|z-\bar z\|_2+2\tau_R(P).                      \tag{11}
\]

It follows by splitting `|P|<=R` and its complement, using respectively
`Lip(phi')<=2` and `|phi'|<=1`. Backward subtraction encounters this
estimate first with `P=cbar` and then with `P=Qbar`; the intervening
operation is bounded `Abar*`, so there is one power of `R`, not two.
Input subtraction uses `||wbar.u-wbar.v||2<=||wbar||2 |u-v|`, retaining
the full row. The first gradient also has the explicit term from changing
`u`. Coupling the laws and integrating leaves precisely (9), because only
the reference marginal carries tails. This proves (10) in the stronger
raw topology, and the identical finite normalized argument proves its
finite same-width form.

The field (2) is jointly continuous in raw state and W1 law. Bounded
multiplier continuity proves each backward field's L2 continuity.
Compactness of the data space makes it uniform in the data variable.
The rank inequality makes the middle integrand HS-continuous; a continuous
Banach-valued integrand on the compact data space has separable compact
range and is Bochner integrable. For a fixed continuous integrand `G`,
coupling at mean distance `q` bounds the law change by
`omega_G(a)+2||G||infty q/a`; first send `q` to zero, then `a` to zero.
These statements are exactly the continuity mechanism of C.4.2, with the
rank norm strengthened as above.

## 4. Conditional continuation theorem

Fix `rho>0`, and write `U_r={mu:W1(mu,nu*)<r}`. Assume the following
**additional, currently unverified hypothesis**:

For each `0<r<rho` there are `a_r,M_r>0` such that every finite-law
population raw Euler calculation from `(g,A0,0)`, with law in `U_r` and
any sufficiently fine mesh through `T=40`, satisfies at every grid node

\[
 \tau_{\nu,R}(\theta^h_\nu(t_k))\le M_r e^{-a_r R},
 \qquad R\ge1.                                         \tag{H}
\]

The mesh threshold may depend on `r`, but not on the law, atom count or
weights. A uniform bound on `int E exp(beta |Q|) dnu` suffices for (H):
`z^2 1_(z>R)<=C_beta e^{-beta R/2}e^{beta z}`, followed by integration
and Cauchy-Schwarz over the law, proves the required RMS-tail bound.
Readout tails are already zero above the bound (3).

**Conditional theorem.** Under (H), every law in `U_rho` has the target
strong autonomous population solution through 40, unique among strong
solutions on the canonical initialized spaces and uniquely restartable
at its reached states. On each smaller neighborhood the raw law map is
uniformly continuous; more precisely it has a Hölder modulus at small
distances, with exponent depending on `r,Y,T,a_r,M_r`. The finite-GF
capture conclusion holds for arbitrary simultaneous deterministic
empirical-law/width sequences tending to any fixed law in `U_rho`.

### 4.1. Why an exponential tail, including a small exponent, is enough

Let two finite-law Euler interpolants have maximal steps `h,h'`, and put
`q=W1(mu,nu)`. Their preceding-node distance is at most their current
distance plus `V_T(h+h')`. With

\[
 s(t)=d(\theta^h_\mu(t),\theta^{h'}_\nu(t))+q+V_T(h+h'),
\]

(10) and (H) imply, almost everywhere while `0<s<=1`,

\[
 s'(t)\le Ls(t)\log(e/s(t)).                            \tag{12}
\]

Indeed take `R=1+a_r^{-1}log(1/s)` in (10); the tail is at most a constant
times `s`, and `(1+R)s` is at most a constant times `s log(e/s)`.
One may increase `L` to include all these fixed constants.

This differential inequality gives, with `alpha(t)=e^{-Lt}`,

\[
 s(t)\le e^{1-\alpha(t)}s(0)^{\alpha(t)}.                \tag{13}
\]

For verification, `z=log(e/s)` obeys `z'>=-Lz`; multiplication by `e^{Lt}`
and integration gives (13). If `s` vanishes, start instead from `s+epsilon`,
use that `v log(e/v)` is increasing on `(0,1)`, and let `epsilon` decrease
to zero. The same regularization proves uniqueness at initial zero.
For sufficiently small initial `s(0)`, the right side of (13) stays below
one through `T`, so a first-exit argument justifies using (12) throughout.
At larger initial errors the global bound (3) suffices.

This is why it is unnecessary to demand `a_r>C T`: an exponential tail
with any positive exponent yields the logarithmic uniqueness modulus.
Using only one fixed cutoff and a whole-interval Gronwall bound would
miss that fact.

### 4.2. Strong construction and completion in the law

For one finite law, (13) with `q=0` makes its Euler family Cauchy in
`C([0,T];mathcal E)`, since `h+h'` tends to zero. More generally, choose
finite laws `nu_j->mu` in W1 and steps `h_j->0`. If `mu` lies in `U_rho`,
choose `r<rho` larger than `W1(mu,nu*)`; the approximants eventually belong
to `U_r`. Equation (13) makes the corresponding paths Cauchy. Their limit
is independent of both the laws and meshes by the same two-family estimate.

The preceding-node states converge uniformly to this path. Joint field
continuity from Section 3 passes their integral equations to

\[
 \theta_\mu(t)=(g,0,0)+\int_0^t F_\mu(\theta_\mu(s))ds.  \tag{14}
\]

Uniform convergence of the integrands follows by a compact-time
subsequence argument: otherwise there are times `t_j->t` with a
nonvanishing discrepancy, contradicting joint continuity at the limiting
state and law. Thus the solution is strong C1 in all three raw components,
including HS for K. Every coefficient of (14) is computed from its
current state and its fixed law.

The limit retains exponential tails, possibly with a smaller exponent.
For fixed `R`, the map `v->(|v|-R)_+` is 1-Lipschitz on L2. Uniform state
convergence makes its Q norm converge uniformly in input, and integration
against the converging laws passes by compact-domain continuity. Use

\[
 \|v1_{|v|>2R}\|_2\le2\|(|v|-R)_+\|_2
                         \le2\tau_R(v).               \tag{15}
\]

This proves (H) for the constructed path with exponent `a_r/2` and an
enlarged constant. The same argument handles c. It applies separately
at every deterministic time with common constants; it assumes no
coordinate supremum over times or inputs.

Comparing two constructed solutions with (10), (15), and (12)-(13)
gives the announced Hölder law modulus. Comparing an arbitrary competing
strong solution to the constructed one uses only the latter's tails.
The competing path is bounded on a compact interval; alternatively (5)
supplies its initialized bound. Zero initial discrepancy in (13) proves
equality. The same argument on `[s,T]` proves unique restart at every
reached state. Reinitialized Euler calculations use the current raw
state; comparison with the existing reference continuation proves their
convergence by (10)-(13), without asserting fresh Gaussian roots at restart.

### 4.3. Finite-GF capture without a relative rate

We give the needed ordered comparison explicitly; (H) alone is not a
finite-width moment assertion. Fix an approximating finite law `nu` and
one mesh `h`. Its population raw Euler states are fixed finite programs.
Expand K as the finite sum of its ranks. Use the population residuals
and contractions to construct the same-array finite oracle. Its proxy
parameters include the actual finite initial readout additively, exactly
as in C.4.3 (A3); assigned increments are the deterministic-coefficient
oracle increments. The true network and proxy have identical initial arrays.

The fixed-program theorem III.F.1-7 and A.1 identify joint same-layer
node laws and second moments. Here the roots are the two Gaussian first
coordinates, each application uses A0 or its actual transpose, and every
coordinate instruction is continuous of at most linear growth. The
backward product is a bounded gate times an L2 field. At fixed graph,
its finite empirical feedback is recovered by clipping the *oracle*
field in (11), taking the width limit, and removing that clip using its
fixed second-moment limit. Scalar contractions converge by their two-factor
RMS inequality. Expanding the rank actions treats both directions.
The finite initial readout RMS and supremum tend to zero; the same finite
induction carries this discrepancy without changing the actual flow.

Consequently, at fixed `(nu,h)`, recomputed proxy fields agree with their
oracle nodes up to `o_P(1)`, assigned-velocity defects are `o_P(1)`, and
the proxy lies on one deterministic enlarged version of the ball (3) with
probability tending to one. Its HS rank norms and pairings are finite
double sums of the two layer Gram contractions, so their limits have
exactly the HS interpretation in (1).

For every fixed cutoff R, (15), convergence of continuous positive-part
quadratic tests, and (H) give at the finitely many proxy grid nodes

\[
 \tau_{\nu,R}(\bar\theta_n^h(t_k))
       \le M'e^{-a'R}+o_P(1).                           \tag{16}
\]

The constants `a',M'>0` are independent of the mesh and law in `U_r`;
fixed cutoff rescalings only decrease `a_r` by a fixed factor. No growing
transcript is sent through a finite-program theorem.

Let `lambda_j->mu` in W1 and `n_j->infinity`, with no relative condition.
Compare actual finite GF for `lambda_j` with this proxy on their common
finite carrier. Actual GF has the law-independent energy bounds of
Section 2.2. At time t the proxy's preceding state differs from its
interpolant by at most `V'h+o_P(1)`. Thus, on any subinterval of length
`ell`, (10) and (16) give the scalar comparison

\[
 E(b)\le e^{C(1+R)\ell}E(a)
   +C\ell e^{C(1+R)\ell}
       \{(1+R)(W_1(\lambda_j,\nu)+h)+M'e^{-a'R}+o_P(1)\},
                                                               \tag{17}
\]

also for the supremum of E on that interval. All errors here are at fixed
`nu,h,R`. The same-width distance E is (1)'s finite version.

Choose a finite time partition with `C ell<a'/2`. On one interval the
tail term in (17) tends to zero as `R->infinity`. To reach any prescribed
final accuracy, choose its cutoff first, then the preceding interval's
required initial accuracy, then that preceding cutoff, and continue
backward across this finite partition. This gives finitely many fixed
cutoffs and positive tolerances. Now choose `nu` close enough to `mu`
and h small enough that all deterministic law/mesh source terms in (17)
meet those tolerances. Finally send j to infinity. The finitely many
`o_P(1)` terms and `W1(lambda_j,mu)` vanish simultaneously. Forward induction
over the partition proves the requested uniform finite/proxy raw error
is arbitrarily small in probability. This order avoids multiplying one
fixed cutoff's tail error by `exp(CRT)` over the full horizon.

The population proxy converges to (14) by Section 4.2. At each fixed
proxy, joint node laws, HS pairings, and action/adjoint tests converge.
The ordered same-width estimate just proved identifies the actual full
raw state by these proxies; finite matrices are never subtracted from
operators on another carrier. The forward formulas are Lipschitz from a
bounded raw ball, uniformly in u. Input and time nets, with the full row
bound and velocity bound, therefore give

\[
 \sup_{t\le40,u\in S^1}|f_{n_j,\lambda_j}(t,u)-f_\mu(t,u)|
       \longrightarrow0\quad\hbox{in probability}.      \tag{18}
\]

Finite lists of forward/backward fields and same-layer quadratic
contractions have the corresponding fixed-program/proxy identification;
bounded multipliers are passed by (11) with a fixed testing proxy.
The same argument covers iid empirical laws independent of initialization:
their W1 distance tends to zero in probability on this compact data space,
as proved by the finite Borel-partition argument in C.4.3. The proxy
random errors depend only on its fixed law and initialization. No
support-size restriction, minimum atom weight, Gram inverse, or
sample/width rate appears.

This finishes the conditional theorem, not the verification of (H).

## 5. Compactness route: what it would and would not provide

For each fixed mesh, its complete family of raw Euler states as the law
varies over all probability laws is contained in a compact set. Here is
a direct proof that avoids any compactness theorem for probability laws.
The initial state is a singleton compact set. If the current states lie
in a compact set C, the gradient integrand's image of `C x Z` is compact
by Section 3. Every law integral lies in the closed convex hull of this
image. That closed convex hull is compact: an epsilon-net of the image
approximates each finite convex combination within epsilon by a convex
combination of finitely many fixed centers; the latter combinations form
a compact finite-dimensional simplex image. Hence the convex hull is
totally bounded, and its closure is complete and compact. Bochner simple
approximations put each integral in this closure. Adding a fixed step
times that compact set to C gives a compact containing set for the next
state. This finite induction, followed by the compact images of the
finitely many interpolation segments, proves the assertion. Thus there
is no compactness obstacle at any single fixed mesh.

The unresolved step is uniformity as the mesh tends to zero. A countable
union of these compact sets need not be relatively compact. Bounds (3),
(5), and (6) do not give the missing spatial compactness of the full row
or the HS increment.

Even a separately supplied compact family of Q fields only gives uniformly
vanishing L2 tails, not a uniqueness modulus. For a compact L2 family,
take a finite epsilon-net and use (15) with the net centers; this proves
uniform integrability. It supplies no decay rate. Concretely, on `(0,1)`
take `Q(x)=x^{-b}`, `0<b<1/2`. The singleton `{Q}` is compact in L2, but

\[
 \tau_R(Q)^2=\int_0^{R^{-1/b}}x^{-2b}dx
       ={R^{-(1/b-2)}\over1-2b},\qquad R\ge1.           \tag{19}
\]

Writing `p=1/(2b)-1>0`, minimization of `Rs+const R^{-p}` is of order
`s^{p/(p+1)}`. Both bounds follow by balancing at
`R=s^{-1/(p+1)}` and considering separately `R` above and below that value.
The reciprocal of this modulus is integrable at zero. Therefore (10)
with such a tail does not force zero discrepancy from zero initial error.
This example concerns the proposed inference from compactness; it is not
a claim that the target neural flow has these tails or is nonunique.

More generally, a sufficient tail criterion is an increasing continuous
majorant omega of

\[
 C\inf_{R\ge1}\{(1+R)s+\tau(R)\}
\]

for which `int_(0+) ds/omega(s)=infinity`. The proof separates variables
as in (12)-(13). Exponential tails give `omega(s)=L s log(e/s)`, and
Gaussian tails are stronger. Merely knowing `tau(R)->0` does not verify
this criterion.

Fixed positive reference proximity has a still earlier defect: the points
`theta_*+epsilon v_k`, for orthonormal raw Hilbert vectors `v_k`, all lie
at distance epsilon from `theta_*` and have pairwise distance
`sqrt(2)epsilon`. Such a tube is not a Cauchy or compactness assertion.
For Q itself, (15) gives only a constant multiple of the Q proximity
plus the reference tail. At a fixed neighborhood radius that positive
error floor does not disappear as R grows.

## 6. Exact obstacle in the supplied reference mechanisms

P1's cavity proof controls deletion of one initialized column by a
width-independent Lipschitz estimate in the reference **clock** metric.
Its decisive step is `||H1-H1_tilde||2<=||X-X_tilde||2`, together with
the gate-free clock velocity `X_a'=-r_a Q_a`. At the two reference axes,
the lower gate cancels before differentiating or comparing flows.

For a general law the exact clock velocity instead is

\[
 X_a'=-2\int r(u,y)u_a
          {\phi'(w\cdot u)\over\phi'(w_a)}Q(u)\,d\mu.    \tag{20}
\]

The factor `1/phi'(w_a)=cosh^2(w_a)` is unbounded. Neither its nonlinear
state differences nor the resulting products have bounded L2 bilinear
norms from the supplied state assumptions. In raw coordinates the
corresponding difference is (11) with the varying reference Q factor;
the cavity estimate becomes dependent on the very tail control sought.
Thus P1's reference-only small column response does not establish (H)
for a changed-law Euler family. Equation (8) removes the trained rank
part from this issue, leaving adapted queries of A0*.

C.2's complete proof obtains Gaussian tails by simultaneous field and
source-response caps, then chooses a short total time so their exponent
bounds improve the caps. Its construction starts from the independent
initialized roots and matrix, and it does not give the same cap selection
for a restarted correlated trained state. C.4.2's restart result is
explicitly on the already constructed local interval. C.4.5 compares
changed finite laws to one reference to a fixed positive accuracy;
it does not complete changed laws to arbitrary accuracy. C.4.6 bounds
the linear trained response and its forcing at that reference, while its
nonlinear remainder boundary explicitly retains (20)'s product issue.

The single highest-leverage unresolved lemma for this route is therefore
(H), or a weaker reached-family tail estimate satisfying the reciprocal
integral condition in Section 5. It must hold for a fixed positive W1
ball through 40, uniformly in law complexity and the auxiliary mesh.
A bound at nu* alone, a bound for a law-dependent mesh of fixed length,
or radii shrinking to zero with the desired approximation error would
not discharge it.

## 7. Claims, checks, and source coverage

| Claim | Status | Check/limitation |
|---|---|---|
| Raw HS transport estimate (10) | Proved extension of supplied estimate | Only the identical rank inequality changes; full row and actual adjoint retained. |
| Global raw Euler bounds (3)-(4) | Proved | Direct unhalved-loss recurrences; no discrete energy claim. |
| Strong finite endpoint (6) | Proved for an existing strong path | Does not construct continuation at that endpoint. |
| Learned transpose L-infinity bound (8) | Proved for existing paths, with Euler counterpart | Initial adapted Gaussian action remains. |
| Exponential-tail completion theorem | Conditional proof complete | Premise (H) unverified on a positive neighborhood through 40. |
| Arbitrary simultaneous finite-GF capture | Conditional on (H) | Fixed proxies, finitely many cutoffs, then joint sequence limit; no rate. |
| Compactness/tube argument alone | Insufficient proof route | Exact examples (19) and the orthonormal tube test identify the failed implications. |
| Requested nonlinear neighborhood theorem | Open in this route | No claim of a counterexample to that theorem. |

Checks performed by this author: full factor/type/normalization derivation,
tail/mesh limit-order reconstruction, comparison with the complete supplied
source proofs, and the explicit compactness and zero-error tests above.
No independent reviewer or formal proof checker has checked this report;
it should not be labeled independently validated or promoted.

Scientific input scope was the supervisor's selected established sections
and frozen P1 packet. No study README, study history, prior reviews, other
P2 author file, or other study's research was read. Repository-wide status
was inspected only as write-safety metadata; preexisting changes were left
untouched. No Git operation changed the index or HEAD.

Complete mathematical units read: `docs/NOTATION.md`; current
`docs/global_nonlinear.md` C.4 introduction and C.4.1-C.4.5 (lines
3836-6897); all of frozen `P1_SECTION.md`, whose text was checked to equal
current C.4.6 (lines 6898-8959); invoked C.2 (2924-3440); frozen dependency
excerpts for finite dynamics §§1-4, special-data III.F.1-11, global-nonlinear
A.1-A.4 and B.1. The remaining invoked C.4 excerpts in the frozen dependency
packet duplicate the complete current sections already read. P1's manifest
was read as provenance. Unused navigation/README text is not an additional
scientific dependency of this argument. There was no external scientific
retrieval; every nontrivial imported theorem is among these supplied proofs.

Required process inputs read: root AGENTS, workflow Part 1,
`solve-math-rigorously/SKILL.md`, `investigate-conjectures/SKILL.md`, and
the latter's research-contract, adversarial-audit and proof-search references.
The assignment was a bounded theory route with no training authorization.

Source SHA-256 values at construction:

| Source | SHA-256 |
|---|---|
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | `3f32122dea7915e25e4abc7abe9d74017d535badfa5abbe1939e84fe2b100bdf` |
| Current C.2, complete lines 2924-3440 with line endings | `cf223a3eed88b3755d0379948316534fb44febc9fa1d6f0bb5d282ff8be4ac94` |
| Current C.4 introduction through C.4.6, lines 3836-8959 | `135e9a5f7e949ae93c3eb6191f34e98e8b7c766d11483fb493833154b1c59d19` |
| `P1_SECTION.md` | `33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38` |
| `P1_DEPENDENCIES.md` | `ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79` |
| `P1_MANIFEST.json` | `f9f3ac7dd834429f2afd1b2d819e20cf04da37446311405943332300ca4fa53d` |
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |

The two frozen content hashes match `P1_MANIFEST.json`. The current book
hash differs from P1's recorded integration base, as expected because its
C.4.6 now equals P1_SECTION. HEAD at metadata inspection was
`96e02035386b24d058b623dcd53186ff5afbca45`. This author owns only this
report and its assigned continuation scratch namespace.

Route recommendation: retain the conditional theorem and exact transpose
bound; leave the target open. Reopen this route only with a proved
reached-query tail mechanism, or a distinct strong existence/uniqueness
mechanism that avoids its need. Ordinary reference proximity and norm
continuation are already exhausted as standalone justifications.
