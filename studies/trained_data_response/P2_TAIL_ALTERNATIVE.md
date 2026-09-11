# P2: independent bounded-feature and row-stability attempt

Author: scoped agent `/root/p2_tail_final_attempt`, 2026-09-11.
Status: partial mathematical results and a proved limitation of one proof route;
the requested neural tail estimate remains open. No experiment, sweep, Git
operation, or promotion was performed.

## Scope, provenance, and exact target

The permitted scientific inputs were the supervisor's prompt and the frozen
`P1_SECTION.md` and `P1_DEPENDENCIES.md`. No study README, other P2 report,
other study, history, or review verdict was read. The following source ranges
were read in full: P1_SECTION 1–131 and 838–1083; P1_DEPENDENCIES 1786–2110
and 2800–2943. A heading/keyword search also exposed excerpts elsewhere in
those same two permitted files. No proof here invokes a theorem from those
unread excerpts. The canonical action and adjoint are premises of the
assignment; this report does not reprove their Gaussian-program construction.
The useful transport estimate read at P1_DEPENDENCIES C.4.1 is reproduced
only as an explicitly identified input in the optional conditional result
below. Its full proof was read.

Process inputs read completely: shared AGENTS.md and RESEARCH_WORKFLOW.md;
the solve-math-rigorously and investigate-conjectures skills; and the latter's
research-contract, adversarial-audit, and proof-search-orchestration references.

The corrected canonical scaling is

\[
 w=W^1,\quad A=W^2=A_0+K,\quad c=W^3,\qquad
 f_n=\frac1n c^T\tanh(A\tanh(wu)).
\]

The stored initial variances are `(1,1/n,1/n^2)`. In particular, `c` is
**not** `n W3`; its initial normalized RMS is of order `1/n`. Mobilities are
`(n,1,n)` and the loss is the unhalved mean square. The initial population
state is `(g,A0,0)` with `g ~ N(0,I2)`. Only `K`, not `A0`, is HS.

We use the exact raw fields, on the actual common action spaces,

\[
 h^1(u)=\phi(w\cdot u),\quad z^2(u)=Ah^1(u),\quad
 h^2(u)=\phi(z^2(u)),\quad d^2(u)=c\phi'(z^2(u)),\quad
 Q(u)=A^*d^2(u),\quad r(u,y)=\langle c,h^2(u)\rangle-y,
 \qquad\phi=\tanh,
\]

\[
 F_\lambda(w,K,c)=-2\int r(u,y)
 \bigl(\phi'(w\cdot u)Q(u)u,\ d^2(u)\otimes h^1(u),\ h^2(u)\bigr)
 \,d\lambda(u,y).
\tag{1}
\]

Population norms are row L2, middle HS, and readout L2. At width `n` these
are respectively `Frobenius/sqrt(n)`, ordinary Frobenius, and
`Euclidean/sqrt(n)`; rank-one operators have finite representative `ab^T/n`.
All constants below are independent of width and support cardinality.

The central unresolved target is a positive W1 neighborhood of
`nu* = (delta_(e1,1)+delta_(e2,-1))/2` on which all raw population Euler
programs through `T=40`, with sufficiently small maximum step, satisfy

\[
 \int\|Q_k(u)1_{\{|Q_k(u)|>R\}}\|_2\,d\lambda(u,y)
 \le M e^{-aR}\qquad(R\ge1),
\tag{2}
\]

with common `a,M>0`. None of the partial results below proves (2).

## 1. Global raw Euler bounds require no loss-decrease assertion

Let `T<infinity`, `Y>=1`, `||A0||op<=A_*`, `K0=0`,
`||c0||infinity<=C_*`, and `||w0||2<=W_*`. These hypotheses hold with
`(A_*,C_*,W_*)=(10,0,sqrt(2))` in the population and on the stated finite
initialization event with `(10,1,2)`.

For every positive-step raw Euler mesh with terminal time at most `T`, define

\[
 D=(C_*+Y)e^{2T},\qquad B=A_*+2TD^2,\qquad
 W=W_*+2TBD^2.
\tag{3}
\]

Then every node, for every Borel training law with `|y|<=Y`, obeys

\[
 \|c_k\|_\infty+Y\le D,\quad
 \|K_k\|_{HS}\le2TD^2,\quad
 \|A_k\|_{op}\le B,\quad \|w_k\|_2\le W,
\tag{4}
\]

\[
 |r_k(u,y)|\le D,\quad \|d^2_k(u)\|_2\le D,\quad
 \|Q_k(u)\|_2\le BD.
\tag{5}
\]

These estimates impose no maximum-step restriction. Their very large
constants are a priori existence-of-node bounds, not an accuracy estimate.

**Proof.** Write `C_k=||c_k||infinity`. Since `|h2|<=1`,
`|f_k|<=C_k`, and the readout update gives

\[
 C_{k+1}+Y\le(1+2h_k)(C_k+Y).
\]

The inequality `1+2h<=exp(2h)` proves the first part of (4). Bounded gates
give `||d2_k||2<=D`. The HS norm of a rank-one action is the product of its
two L2 norms, hence

\[
 \|K_{k+1}-K_k\|_{HS}\le2h_kD^2.
\]

Summing proves the middle bounds. Finally, (1) and the operator bound give
`||w_(k+1)-w_k||2<=2h_kBD^2`. Summation proves the last part. Every norm and
rank-one identity used also holds with the stated finite normalization. ∎

Consequently the affine Euler interpolants have a common raw speed bound

\[
 V=2BD^2+2D^2+2D.
\tag{6}
\]

All Euler nodes are well defined on the canonical action spaces. This
assertion by itself supplies neither strong compactness of the interpolants
nor uniqueness or convergence as the mesh is refined. Bounded sets in the
row L2 and middle HS spaces are not strongly compact.

For a Borel law, the integrands in (1) are strongly measurable. For example,
`u -> w.u` is continuous in L2; its bounded tanh feature is continuous in L2;
bounded action and bounded `c` give L2 continuity of `d2` and `Q`.
For the remaining product, split
`phi'(w.u)Q(u)-phi'(w.v)Q(v)` into a bounded-gate times `Q(u)-Q(v)` and a
gate difference times the fixed L2 field `Q(v)`. The latter tends to zero
by truncating that fixed field at a finite level and then removing the
truncation. The integrands have the bounds already proved, so their
Bochner integrals exist. The same argument treats the rank-one HS integral.

## 2. The learned transpose contribution is pointwise bounded

At an Euler node `k`, the exact rank history gives

\[
 (K_k^*d^2_k(u))(\omega)
 =-2\sum_{j<k}h_j\int r_j(v,y)h^1_j(v)(\omega)
          \langle d^2_j(v),d^2_k(u)\rangle\,d\lambda(v,y).
\tag{7}
\]

Thus (4)–(5) imply, pointwise in the first population and uniformly in `u`,

\[
 |K_k^*d^2_k(u)|\le 2TD^3.
\tag{8}
\]

The same conclusion follows by replacing the sum with a time integral
along any existing strong raw flow satisfying the same caps. No property
of a Gaussian matrix is used here.

In particular, if `Z_k(u)=A0^*d2_k(u)` and `R>=4TD^3`, then

\[
 \|Q_k(u)1_{\{|Q_k(u)|>R\}}\|_2
 \le2\|Z_k(u)1_{\{|Z_k(u)|>R/2\}}\|_2.
\tag{9}
\]

Indeed `|Q|>R` implies `|Z|>R/2`, and on this event `|Q|<=2|Z|`.
The missing tail estimate is therefore already present in the adapted
initialized transpose term. The learned increment is not the bottleneck.

## 3. Radial tanh control helps for GF but does not bound curvature

For real `s`,

\[
 |s|\phi'(s)\le\tfrac12.
\tag{10}
\]

To verify this, `cosh^2(s)=1+sinh^2(s)>=1+s^2>=2|s|`, with the value at
zero treated directly. Along an existing raw GF define the nonnegative
first-population field

\[
 b_t(\omega)=\int|Q_t(u)(\omega)|\,d\lambda(u,y).
\]

By Minkowski and (5), `||b_t||2<=BD`. Taking the scalar product of the first
equation in (1) with `2w` and using (10) gives

\[
 \frac d{dt}|w_t|^2
 =-4\int r_t Q_t\phi'(w_t\cdot u)(w_t\cdot u)\,d\lambda
 \le2Db_t.
\]

Consequently

\[
 \sup_{t\le T}|w_t|^2\le |w_0|^2+2D\int_0^T b_s\,ds,
\tag{11}
\]

\[
 \left\|\sup_{t\le T}|w_t|^2\right\|_2
 \le \||w_0|^2\|_2+2TBD^2.
\tag{12}
\]

At the population Gaussian root, `E|g|^4=3+2+3=8`, so the first term on the
right is `sqrt(8)`. At finite width (12) requires the empirical initial
fourth moment; a bound on initial RMS alone is not a deterministic bound
on that fourth moment. Gaussian initialization supplies the extra bound
with probability tending to one, by the finite variance of `|g|^4` and
Chebyshev's inequality applied to its empirical average.

There is an exact Euler correction that must not be dropped:

\[
 |w_{k+1}|^2\le |w_k|^2+2Dh_kb_k+4D^2h_k^2b_k^2.
\tag{13}
\]

The final term follows from `|F_w|<=2Db_k`. An L2 cap on `b_k` bounds the
expectation of the sum of those final terms by `4D^2 T h_max (BD)^2`.
It does not bound their L2 norm, which would require fourth moments of
`b_k`. Thus (12) is not, from these premises alone, a uniform Euler
fourth-moment estimate.

### An explicit stationary row with arbitrarily fast expansion

Write the tanh row vector field for one direction as

\[
 V_u(w)=\phi'(w\cdot u)u.
\]

Consider directions `e1,e2,v`, where `v=(e1+e2)/sqrt(2)`. Fix `x>0`,
`w_*=(x,x)`, `d=phi'(x)`, `d_s=phi'(sqrt(2)x)`, and the frozen scalar
controls

\[
 p_1=p_2=-\frac{d_s}{\sqrt2d},\qquad p_v=1,
 \qquad G=p_1V_{e1}+p_2V_{e2}+p_vV_v.
\tag{14}
\]

Direct substitution shows `G(w_*)=0`. Since
`D V_u(w)=phi''(w.u) u u^T` and `phi''(s)=-2tanh(s)phi'(s)`,

\[
 DG(w_*)=d_s\left(\sqrt2\tanh(x)I
             -2\tanh(\sqrt2x)vv^T\right).
\tag{15}
\]

The transverse unit vector `v_perp=(e1-e2)/sqrt(2)` is an eigenvector with
strictly positive eigenvalue

\[
 \kappa=\sqrt2d_s\tanh(x)>0.
\tag{16}
\]

Multiplying all controls by any `L>0` leaves the stationary row unchanged
and changes this expansion rate to `L kappa`. In particular, zero row
speed and zero radial growth do not bound the positive curvature term.

This obstruction survives every fixed smooth positive-definite local
metric. At the equilibrium, the derivative of the metric along the base
curve is zero; for the variational vector `v_perp`,

\[
 \frac d{dt}\|\delta w\|_{M(w_*)}^2
 =2L\kappa\|\delta w\|_{M(w_*)}^2.
\]

It also survives the bounded-feature map
`w -> (tanh(w1),tanh(w2),tanh(w.v))`, whose derivative on `v_perp` is
nonzero and therefore retains the same linearized expansion eigenvalue.

For the true first-row equation, the frozen controls have the form
`p_u=-2 lambda_u r(u)Q(u)`. The example is an algebraic test of that row
curvature term; it is **not** a claim that these three controls are attained
by the canonical neural trajectory. Varying the full neural state also
varies residuals and queries, and that adds other derivative terms.

Nevertheless it invalidates an attempted deterministic estimate of this
curvature term using only row speed, radial growth, or bounded features.
The issue is present arbitrarily close in data law to the reference:
`(1-epsilon)nu*+epsilon delta_(v,1)` approaches `nu*` in W1 and has all
three positive atom masses. Small mass alone does not make the effective
control small without a query-amplitude estimate; writing a prescribed
control as `-2 lambda_u r(u)Q(u)` exposes the inverse atom mass. This last
observation is not a reachable-state counterexample either.

### No common clock can flatten the correlated row fields

For directions `u,v`, direct differentiation gives the bracket

\[
 [V_u,V_v](w)
 =(u\cdot v)\left[
   \phi'(w\cdot u)\phi''(w\cdot v)v
  -\phi'(w\cdot v)\phi''(w\cdot u)u\right],
\tag{17}
\]

where the bracket convention is `D V_v V_u - D V_u V_v`.
With `u=e1`, `v=(e1+e2)/sqrt(2)`, and `w=(x,0)`, the second coordinate is
`phi'(x)phi''(x/sqrt(2))/2`, which is nonzero for `x>0`.

Suppose a C2 local change of coordinates with invertible derivative made
both row fields constant vectors. Differentiating their transformed fields
and subtracting cancels the second derivatives of the coordinate change;
the transformed bracket is its derivative applied to (17). Constant fields
have zero bracket, contradicting invertibility. Thus the orthogonal
two-clock elimination of query amplitudes has no extension by one common
smooth coordinate change flattening these correlated fields.

This proves a specific obstruction to a proposed coordinate mechanism,
not the impossibility of a nonlinear population continuation.

## 4. Why the deterministic caps do not furnish backward tails

Here is a sharp ambient-state check retaining the actual Gaussian matrix.
Let `A0` have iid entries `N(0,1/n)` and define

\[
 c_j=\operatorname{sgn}((A_0)_{j1}),\quad w=0,\quad K=0.
\]

This is a legitimate state with `||c||infinity=1`, `h1=h2=0`, and
`d2=c`. Its backward field is `Q=A0^T c`, independent of the passive input,
and

\[
 Q_1=\sum_{j=1}^n |(A_0)_{j1}|.
\]

Writing `(A0)_(j1)=Z_j/sqrt(n)`, the Gaussian integral gives
`E|Z_j|=sqrt(2/pi)` and finite variance. Chebyshev's inequality yields

\[
 \frac{Q_1}{\sqrt n}\longrightarrow \sqrt{2/\pi}
 \quad\hbox{in probability}.
\]

Choose any fixed `0<b<sqrt(2/pi)` and `R_n=b sqrt(n)/2`. With probability
tending to one,

\[
 \|Q1_{\{|Q|>R_n\}}\|_{2,n}\ge Q_1/\sqrt n\ge b,
\tag{18}
\]

whereas every proposed bound `M exp(-aR_n)` tends to zero. Intersecting
with the supplied high-probability event `||A0||op<=10` does not change
this conclusion. Thus an operator bound, a readout supremum bound, and
bounded features do not imply (2) for arbitrary adapted states. Equivalently,
one cannot use a general width-uniform Gaussian `L-infinity -> Lp` operator
bound for `p>2` here.

The state in this construction has neither the canonical Gaussian row nor
the canonical small initial readout. It is **not** a counterexample to
(2), to an actual neural trajectory, or to the desired continuation.
Its only conclusion is that a proof must use more of reachability than
the deterministic caps (4)–(5).

## 5. A slightly weaker conditional tail criterion

This subsection records a sufficient condition, not a newly proved neural
estimate. It can modestly weaken the quantitative target if a reachable
tail argument naturally produces logarithmic losses.

On a fixed raw ball with a common readout supremum cap, the complete
factor-subtraction proof in P1_DEPENDENCIES C.4.1 gives

\[
 \|F_\lambda(\theta)-F_\mu(\bar\theta)\|
 \le C(1+R)\bigl(\|\theta-\bar\theta\|+W_1(\lambda,\mu)\bigr)
       +C\int\tau_R(Q_{\bar\theta}(u))\,d\mu.
\tag{19}
\]

Here the middle norm may be HS: the only rank estimate in that proof is
`||a tensor b||=||a||2||b||2`, true for both operator and HS norms, while
action differences are bounded by HS differences. For `R` beyond the
common readout cap its separate readout tail vanishes. This is the only
imported analytic estimate in this subsection, and its proof was read in
full at lines 1891–2010 of the frozen dependency file.

Assume, instead of (2), a uniform raw-node estimate

\[
 \int\tau_R(Q_k(u))\,d\lambda
 \le M\exp\left(-a\frac{R}{\log(e+R)}\right)
 \qquad(R\ge1)
\tag{20}
\]

over the same law/mesh class. Then those Euler interpolants are uniformly
Cauchy as `h_max -> 0`; their strong limits are unique solutions among
strong solutions with the deterministic caps above. The statement is
uniform in finite laws in the class and extends by W1 completion wherever
that class is dense in the desired data-law neighborhood.

Here is a self-contained proof of the comparison step. For sufficiently
small `z>0`, put `L=log(1/z)` and choose `R=C_a L log(e+L)` with fixed
`C_a` sufficiently large. Since
`log(e+C_a L log(e+L)) <= 2 log(e+L)` for all sufficiently large `L`,
`aR/log(e+R)>=L` if `C_a>=2/a`. Thus (19)–(20), enlarging constants over
the omitted compact range, produce the modulus

\[
 \omega(z)=Cz\log(e/z)\log\bigl(e+\log(e/z)\bigr)
\tag{21}
\]

near zero. Extend it positively and monotonically on the bounded distance
range of the state ball. It has

\[
 \int_{0^+}\frac{dz}{\omega(z)}=\infty,
\tag{22}
\]

as is seen by the substitution `L=log(e/z)` and the divergent integral
`int^infinity dL/(L log(e+L))`.

For two affine interpolants with mesh bounds `h,h'`, let `d(t)` be their
raw distance and let `epsilon=V(h+h')+W1(lambda,mu)`. Their node distance
is at most `d(t)+V(h+h')`. Applying (19) at the two nodes and optimizing
`R` as above gives the almost-everywhere upper derivative inequality

\[
 d'(t)\le\omega(d(t)+\epsilon),\qquad d(0)=0,
\tag{23}
\]

after another fixed enlargement of the constant in (21). Set
`z(t)=epsilon+int_0^t omega(d(s)+epsilon) ds`. Then
`d+epsilon<=z`, so `z'<=omega(z)`. Therefore

\[
 \int_\epsilon^{z(t)}\frac{dq}{\omega(q)}\le t.
\]

By (22), for every fixed `eta>0` this inequality prevents `z` reaching
`eta` by time `T` when `epsilon` is sufficiently small. This proves the
uniform Cauchy and W1-continuity claims. Completeness gives a strong limit
in row L2, middle HS, and readout L2. The readout supremum cap is closed
under L2 convergence: a subsequence converges almost everywhere, retaining
the bound. Comparing each Euler node to the limit using (19), with that
node as the reference, first lets the mesh vanish at fixed `R` and then
lets `R` grow. The field discrepancy tends uniformly to zero; hence the
Euler integral equations pass to the strong integral equation.

For comparison with any other strong solution having the caps, use the
Euler node, which has (20), as the reference in (19). Its distance to its
own interpolation is at most `Vh`; the argument (23) again applies with
`epsilon=Vh`. Letting `h` tend to zero proves uniqueness. No tail estimate
on the competing solution is required for this comparison.

This conditional result does not establish (20), and it does not identify
the resulting solution with actual finite neural GF or GD. Those passages
require their own fixed-program and mesh consistency arguments. It also
does not supply the stronger inverse-gate-force estimate below by itself
for all positive-step Euler programs.

## 6. Exact inverse-gate bound and its remaining integrability gap

For an existing GF, the reached first-row inverse-gate factor is

\[
 J_a(t,u)=u_a\frac{\phi'(w_t\cdot u)}{\phi'(w_{t,a})}Q_t(u).
\]

Since `cosh^2(s)<=exp(2|s|)`, (11) gives the pointwise bound

\[
 |J_a(t,u)|^2
 \le |Q_t(u)|^2\exp\left(
 4|g|+4\sqrt{2D\int_0^T b_s\,ds}\right).
\tag{24}
\]

Equation (12) alone does not make the right-hand side integrable. One
sufficient GF condition is a uniform joint law/time marginal bound

\[
 \sup_{t,\lambda}\int E\exp(\alpha |Q_t(u)|^\beta)\,d\lambda
 <\infty\quad\hbox{for some }\beta>1/2,
\tag{25}
\]

with the same law family and `alpha>0`. Here is a proof avoiding an
unjustified concave Jensen step when `beta<1`. Choose
`gamma` with `1/2<gamma<min(beta,1)`; if necessary increase the moment
constant so (25) implies all moments of `Q` obey
`||Q||p <= C p^(1/beta)` for `p>=1`. To verify that implication, maximize
`s^p exp(-alpha s^beta/2)` over `s>=0`, obtaining the bound
`s^p <= (2p/(alpha beta e))^(p/beta) exp(alpha s^beta/2)`, and integrate.
Minkowski in time and data gives the same moment bound, multiplied by
`T`, for `B_T=int_0^T b_s ds`. Expanding the exponential series and using
those moment bounds shows `E exp(c B_T^gamma)<infinity` uniformly for
every fixed `c>0`: the `m`-th series term is at most
`[C_c m^(gamma/beta-1)]^m`, using `m!>= (m/e)^m`, and is summable because
`gamma/beta<1`. Since `gamma>1/2`, every
`E exp(c sqrt(B_T))` is therefore finite. The Gaussian root has every
linear exponential moment, directly by completing the square in its
density. Finally Hölder, the exponential moments just proved, and the
arbitrarily high polynomial moments of `Q` imply, for any fixed `p>1`,

\[
 \sup_{t,\lambda}\int E|J_a(t,u)|^{2p}\,d\lambda<\infty.
\]

This implies square uniform integrability by
`E[|J|^2 1_(|J|>R)] <= R^(-2(p-1)) E|J|^(2p)`, also after data integration.
No independence between `Q`, the row root, and the accumulated field is
needed. This conditional GF result separates the tail strength needed
for inverse-gate integrability from the Osgood strength needed by (19).

For Euler, (13) adds the term
`2D sqrt(sum h_k^2 b_k^2)` to the corresponding upper bound for `|w_k|`.
The above GF proof must not simply be copied to raw Euler with only
`beta>1/2`; exponential integrability of that extra term is a separate
requirement. In particular, a small coefficient does not give a linear
exponential moment to a random variable known only to have a stretched
exponential tail of exponent below one.

## Frozen conclusion and reopen condition

The following are proved from the stated premises: global raw Euler node
and speed bounds; a pointwise bound on the learned transpose contribution;
the GF radial/fourth-moment inequality and its exact Euler correction; and
the stationary-row expansion and noncommuting-clock obstructions. The
ambient Gaussian-state example disproves only an inference from the
deterministic caps to neural tails.

The conditional criteria (20) and (25) make separate sufficient estimates
precise. Neither is proved for the actual reached states. No exponential
neural tail, full perturbed population continuation, or reached raw-Euler
inverse-gate square uniform integrability is claimed.

Route status: blocked at the adapted initialized-transpose tail, with the
bounded-feature/amplitude-free row-stability subroute refuted in its stated
controlled-field form. Reopen only with an estimate using actual neural
reachability that bounds the curvature/query feedback or the relevant
source-response coefficients uniformly over raw mesh refinement and data
laws. Row motion and bounded features alone cannot supply that estimate.

Independence note: after these row calculations, the supervisor sent a
speculative source-response bootstrap suggestion, explicitly not another
report's result. It was not used in the derivations above; this report was
frozen before reading or comparing any other attempt. Source and report
hashes are retained in the assigned scratch namespace.
