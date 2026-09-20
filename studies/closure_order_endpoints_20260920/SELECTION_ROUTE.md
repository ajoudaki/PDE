# Selected optimizer route: nonlinear burn-in and exact readout fitting

Status: complete internally checked derivation. This is a modified-optimizer
theorem, not an endpoint theorem for continued full gradient flow.

## Scope and research contract

This scoped independent route initially reads only `docs/NOTATION.md` and
`docs/global_nonlinear.md` C.4.7.9, C.4.7.10.B–C, and D.3. The supervisor
subsequently explicitly expanded the allowed source scope to complete
C.4.7.10.A.1–A.4 (lines 12594–13160); Section 9 proves the resulting extension
instead of silently enlarging B's written theorem. It uses the
investigate-conjectures and solve-math-rigorously skills and their required
contract/adversarial references. It reads no other study or another route.

The canonical hierarchy is precisely the full initialized-word augmented
Chebyshev hierarchy, Cholesky normalization, ridge schedule and joint Gaussian
initialization in (H40.C5)–(H40.C8), equivalently C.4.7.10.B–C on its shorter
certified domain. Order is denoted `p`; it is not numerical precision,
particle count or neural width. Every order is an exact population closure.

The primary modified optimizer is fixed now: run the full nonlinear closure
to one common positive time `T`, chosen solely from the data, the initialized
full Gaussian kernel and a certified canonical horizon. Freeze its current
lower rows and middle action, then run unregularized squared-loss gradient
flow of the readout alone, starting from the learned readout at `T`. The
training law is a finite positive-weight law in an established canonical
domain, with distinct input directions modulo antipodal sign after merging
duplicates and consistently signed antipodes. The target is uniform error on
the whole circle between fitted predictors at `p` and `p+1`, and their common
limit as `p` tends to infinity. The limit must be the same optimizer applied
to the canonical nonlinear population flow, not a separately chosen kernel.

This changes the optimizer after `T`. It preserves actual nonlinear hidden
learning before `T`; it does not identify the endpoint of continued full
gradient flow. It uses no future target prediction and no order-dependent
burn-in time. Positive readout regularization is a secondary biased benchmark,
not the exact-fitting target. No computation or numerical experiment is run.

The proof obligations are: positivity of the actual initialized Gaussian
training Gram; positivity after a sufficiently short common nonlinear
burn-in; eventual positivity for the actual canonical hierarchy; an explicit
readout-flow endpoint including the inherited nullspace component; and a
whole-circle perturbation bound that uses the genuine learned-feature defect.

## 1. Data, canonical objects, and the modified optimizer

Write the training law as

\[
 \mu=\sum_{a=1}^m\pi_a\delta_{(u_a,y_a)},\qquad
 \pi_a>0,\quad\sum_a\pi_a=1,\quad |u_a|=1,\quad |y_a|\le Y,
 \qquad Y\ge1.
\]

Assume the law belongs to a domain on which the cited canonical theorem
holds through a positive horizon `T_cert`. One may take the explicit D.3
domain and `T_cert=40`, where `Y=1`, or the C.4.7.9 domain and its certified
short horizon. For the finite supported D.3 class this is an actual source
theorem, not an extra infinite-time existence assumption.

Section 9 below proves that the hierarchy convergence needed here also
holds for every Borel circle law with labels in `[-1,1]` through
`T_cert=1/200`. Accordingly every finite compatible binary circle dataset,
and more generally every finite compatible dataset with `|y_a|<=1`, is
covered with `Y=1`, without a two-arc or small-neighborhood restriction.

Every represented predictor is odd in input. Identical inputs can therefore
be merged if their labels coincide, and antipodal inputs can be merged after
changing the sign of one label if those signed labels coincide. This preserves
the training loss. Assume this reduction has been performed, so
`u_a != u_b` and `u_a != -u_b` for `a != b`. Without the stated label
compatibility, exact fitting is impossible for every order and for the full
model. Zero labels are permitted; hidden motion is not asserted for every
such degenerate problem.

On the one canonical carrier let

\[
 H_p(u)=\tanh(A_p(T)\tanh(w_p(T)\cdot u)),\quad c_p=c_p(T),
 \qquad
 H(u)=\tanh(A(T)\tanh(w(T)\cdot u)),\quad c=c(T).
\]

Here `A_p=B_p+K_p`, with exactly the order-dependent filtered initialization
and learned increments of (H40.C5)–(H40.C8); the full dictionary tail is
retained. The canonical source results give

\[
 \delta_p:=\sup_{u\in S^1}\|H_p(u)-H(u)\|_2\longrightarrow0,
 \qquad \zeta_p:=\|c_p-c\|_2\longrightarrow0.             \tag{S1}
\]

This is the substantive hierarchy-consistency input. It holds for this
specific evolving nonlinear hierarchy. An arbitrary assumed sequence of
convergent kernels would not replace it.

After physical time `T`, keep `w_p(T),M_p(T)` fixed and use a new elapsed
phase time `s>=0` for the readout equation

\[
 \frac{dc_p^{\rm ro}}{ds}
 =2\sum_a\pi_a\{y_a-\langle c_p^{\rm ro},H_p(u_a)\rangle\}H_p(u_a),
 \qquad c_p^{\rm ro}(0)=c_p.                              \tag{S2}
\]

The original residual convention is unchanged: (S2) equals minus twice
the residual-weighted hidden field. Its unhalved loss and readout metric
are the original ones. The only alteration is setting both hidden-block
mobilities to zero after `T`. In particular the existing readout is not
reset and its component invisible to the training points is retained.

## 2. Positivity of the actual initialized full Gaussian kernel

At initialization put

\[
 h_a(g)=\tanh(g\cdot u_a),\qquad
 V_{ab}=E[h_a(g)h_b(g)],\qquad g\sim N(0,I_2).
\]

**Lemma 1.** `V` is positive definite for the reduced input set above.

Suppose `sum_a v_a h_a=0` almost surely. The function of `g` on the left
is continuous. Since every nonempty open ball has positive Gaussian
probability, it vanishes everywhere on `R^2`. Choose a vector `z` outside
the finite collection of lines

\[
 z\cdot u_a=0,\qquad z\cdot(u_a-u_b)=0,\qquad
 z\cdot(u_a+u_b)=0.
\]

Each is a proper line because the reduced directions are nonzero and distinct
modulo sign. Such a `z` exists, and `s_a=z·u_a` are nonzero with pairwise
distinct squares. Restrict the zero function to `g=t z`.

To verify the Taylor coefficients being used, write the convergent local
series of tanh as `sum_(k>=1) (-1)^(k-1) a_k t^(2k-1)`. Oddness eliminates
even powers and the equation `tanh'=1-tanh²` gives `a_1=1` and

\[
 (2k-1)a_k=\sum_{i+j=k}a_i a_j>0\quad(k\ge2).
\]

Thus all coefficients are nonzero. Differentiating the restricted identity
at orders `1,3,...,2m-1` gives

\[
 \sum_a(v_as_a)(s_a^2)^{k-1}=0,\qquad 1\le k\le m.
\]

The Vandermonde determinant is `prod_(a<b)(s_b²-s_a²)`, which is nonzero;
hence `v_as_a=0` for every `a`, and `v=0`. Therefore
`v^T V v=E(sum_a v_a h_a)^2>0` for every nonzero `v`.

The complete canonical Gaussian initialization rule for forward queries
gives the joint vector

\[
 Z=(A_0h_a)_{a=1}^m\sim N(0,V).
\]

These queries can be evaluated together before any reverse query, so there
is no earlier opposite-orientation response term. Since `V` is positive
definite, `Z` has a density positive everywhere on `R^m`.

**Lemma 2.** The actual initialized upper-hidden Gram

\[
 S^0_{ab}=E[\tanh Z_a\tanh Z_b],\qquad
 G^0_{ab}=\sqrt{\pi_a\pi_b}\,S^0_{ab}
\]

is positive definite. Indeed a vanishing linear combination of `tanh Z_a`
would vanish everywhere by continuity and full support. Set all coordinates
except coordinate `a` to zero; then its coefficient times `tanh Z_a` vanishes
for every real `Z_a`, forcing that coefficient to zero. Multiplication by the
invertible positive diagonal matrix `diag(sqrt(pi_a))` preserves positivity.
Define the strictly positive, data-dependent number

\[
 \gamma_0=\lambda_{\min}(G^0)>0.                         \tag{S3}
\]

Every entry of `G^0` is an initialized finite-dimensional Gaussian integral.
This definition depends only on the known data and canonical initialization,
not on any learned trajectory. No universal lower bound over arbitrarily
close input directions is claimed.

## 3. An order-independent positive nonlinear burn-in time

The established full flow and every exact finite closure satisfy, on their
certified common interval,

\[
 \|c(t)\|_\infty\le2Yt,\quad
 \|K(t)\|_{\rm HS}\le2Y^2t^2,\quad
 \|w(t)-g\|_2\le4Y^2t^2+2Y^4t^4.                       \tag{S4}
\]

For completeness these bounds do not assume fittedness. Loss decreases from
at most `Y²`, so `int |r| dmu<=Y`. The readout speed is at most `2Y`.
The rank speed is at most `2Y||c||_2<=4Y²t`; integrate to bound `K`.
Then `||A||op<=2+2Y²t²` and the lower-row speed is at most
`2Y||A||op||c||_2<=8Y²t+8Y⁴t³`; integrate once more. The finite closure
has the same bounds by contraction of its two filters.

For the full flow, Lipschitz continuity of tanh and

\[
 A(t)\tanh(w(t)\cdot u)-A_0\tanh(g\cdot u)
 =A_0\{\tanh(w(t)\cdot u)-\tanh(g\cdot u)\}
   +K(t)\tanh(w(t)\cdot u)
\]

give the explicit upper-hidden drift bound

\[
 d(t):=\sup_u\|H^2(t,u)-H^2(0,u)\|_2
 \le10Y^2t^2+4Y^4t^4.                                  \tag{S5}
\]

If bounded feature fields `F_a,F'_a` have `L2` distance at most `d` and
norm at most one, each Gram entry changes by at most `2d`. For their
probability-weighted Gram and any Euclidean vector `v`,

\[
 |v^T(G-G')v|
 \le2d\left(\sum_a\sqrt{\pi_a}|v_a|\right)^2
 \le2d|v|^2.
\]

Consequently the learned full training Gram `G` at time `T` satisfies
`lambda_min(G)>=gamma_0-2d(T)`.

One explicit choice, fixed identically for all orders, is

\[
 0<T=\min\left\{T_{\rm cert},1,
              \sqrt{\frac{\gamma_0}{56Y^4}}\right\}.     \tag{S6}
\]

Since `Y>=1` and `T<=1`, (S5) is at most `14Y⁴T²`, so
`2d(T)<=gamma_0/2` and

\[
 \lambda_{\min}(G)\ge\gamma_0/2.                        \tag{S7}
\]

This proves the needed learned-kernel condition from the canonical model.
It does not silently impose a positive gap at an arbitrary late training
time. A longer chosen burn-in can also be used if its actual learned Gram
has a positive smallest eigenvalue, but that is a separate check.

By (S1), `||G_p-G||op<=2delta_p`, so for all sufficiently large `p`,

\[
 \lambda_{\min}(G_p)\ge\gamma:=\gamma_0/4>0.             \tag{S8}
\]

Thus eventual nonsingularity is proved for the exact full canonical closure
hierarchy. An effective numerical threshold in `p` is not supplied by the
source's qualitative feature approximation theorem.

## 4. Exact endpoint and the inherited nullspace component

Define the bounded linear training-evaluation map and weighted label vector

\[
 E_p:L^2(\Omega_2)\to\mathbb R^m,\quad
 (E_pz)_a=\sqrt{\pi_a}\langle z,H_p(u_a)\rangle,
 \qquad \bar y_a=\sqrt{\pi_a}y_a.
\]

Then `||E_p||op<=1`, `E_p^*v=sum_a sqrt(pi_a)v_a H_p(u_a)`, and
`G_p=E_pE_p^*`. Let `r_p=bar y-E_pc_p`; this is the negative weighted
residual. Energy at the end of burn-in gives `|r_p|<=Y`.
For every order with `G_p` positive definite, (S2) has the exact solution

\[
 c_p^{\rm ro}(s)
 =c_p+E_p^*G_p^{-1}(I-e^{-2G_ps})r_p.                   \tag{S9}
\]

To check it, differentiation gives `2E_p^*e^{-2G_ps}r_p`, and applying
`E_p` to the displayed formula gives training residual `e^{-2G_ps}r_p`.
These match (S2) and its initial condition. Any difference of two solutions
has squared norm derivative `-4||E_p difference||²<=0`, which proves
uniqueness from zero initial difference.

The limit and its whole-circle prediction are

\[
 c_p^*=c_p+E_p^*G_p^{-1}r_p
       =(I-P_p)c_p+E_p^*G_p^{-1}\bar y,\qquad
 P_p=E_p^*G_p^{-1}E_p,                                  \tag{S10}
\]
\[
 f_p^*(u)=f_p(T,u)+k_p(u)^TG_p^{-1}
                   \{\bar y-E_pc_p\},\qquad
 [k_p(u)]_a=\sqrt{\pi_a}\langle H_p(u),H_p(u_a)\rangle.   \tag{S11}
\]

`P_p` is the orthogonal projection onto `range(E_p^*)`: it is self-adjoint,
`P_p²=P_p`, and fixes that range. Formula (S10) therefore records, rather
than discards, the readout component created during nonlinear training that
is orthogonal to all final training feature vectors. In particular this
endpoint generally differs from fitting a zero readout in the learned kernel.

Applying `E_p` to (S10) gives `E_pc_p^*=bar y`, hence zero training loss.
Moreover, diagonalization of the symmetric positive matrix `G_p` gives

\[
 \|E_p^*G_p^{-1}\|_{\rm op}^2=\|G_p^{-1}\|_{\rm op}
 \le\gamma^{-1},
\]
\[
 \sup_{u\in S^1}|f_p^{\rm ro}(s,u)-f_p^*(u)|
 \le\|c_p^{\rm ro}(s)-c_p^*\|_2
 \le\frac{Y}{\sqrt\gamma}e^{-2\gamma s}.                 \tag{S12}
\]

For an early singular order the same linear ODE still converges: diagonalize
`G_p`, integrate only its positive eigenvalues, and use `E_p^*v=0` on its
kernel because `||E_p^*v||²=v^TG_pv`. The formula then uses `G_p^dagger`;
training residual retains its component in `ker(G_p)`. Exact fitting is
guaranteed by the theorem only for the eventual orders (S8), or for an early
order whose nonsingularity is verified separately.

## 5. Quantitative comparison of consecutive fitted predictors

The following applies to any two actual orders `p,q` on the common carrier,
including `q=p+1`, whose learned Grams have smallest eigenvalue at least
`gamma>0`. Put

\[
 \delta_{p,q}=\sup_u\|H_p(u)-H_q(u)\|_2,\quad
 \zeta_{p,q}=\|c_p-c_q\|_2,\quad
 b_{p,q}=\zeta_{p,q}+2YT\delta_{p,q}.
\]

Then

\[
 \|f_p^*-f_q^*\|_{C(S^1)}
 \le(1+\gamma^{-1})b_{p,q}
       +2Y(\gamma^{-1}+\gamma^{-2})\delta_{p,q}.
                                                         \tag{S13}
\]

Here is the full perturbation calculation. Boundedness `||H_p(u)||_2<=1`
and `||c_q||_2<=2YT` gives

\[
 \|f_p(T,\cdot)-f_q(T,\cdot)\|_\infty\le b_{p,q},
 \qquad |r_p-r_q|\le b_{p,q}.
\]

The same weighted-sum estimate used above gives

\[
 \|G_p-G_q\|_{\rm op}\le2\delta_{p,q},\quad
 \sup_u|k_p(u)-k_q(u)|\le2\delta_{p,q},\quad
 \sup_u|k_q(u)|\le1.
\]

The resolvent identity, checked by multiplication, is

\[
 G_p^{-1}-G_q^{-1}=G_q^{-1}(G_q-G_p)G_p^{-1},
\]

so its norm is at most `2delta_(p,q)/gamma²`. Subtract the correction
in (S11) as

\[
 (k_p-k_q)^TG_p^{-1}r_p
 +k_q^T(G_p^{-1}-G_q^{-1})r_p
 +k_q^TG_q^{-1}(r_p-r_q).
\]

Use `|r_p|<=Y` and the preceding bounds, then add the initial predictor
difference. This gives exactly (S13). No coefficient/ridge nesting,
angular cutoff, stationary input kernel or small action operator-norm
difference was assumed.

For comparison with the canonical full flow's selected endpoint `f^*`,
the same calculation yields, for all sufficiently large `p`,

\[
 \|f_p^*-f^*\|_\infty
 \le(1+\gamma^{-1})(\zeta_p+2YT\delta_p)
      +2Y(\gamma^{-1}+\gamma^{-2})\delta_p
 \longrightarrow0.                                      \tag{S14}
\]

Thus consecutive fitted predictors stabilize, and their limit is the
specified optimizer applied to the canonical nonlinear population dynamics.
Combining (S12) and (S14) gives the stronger bound

\[
 \|f_p^{\rm ro}(s,\cdot)-f^*\|_\infty
 \le\frac{Y}{\sqrt\gamma}e^{-2\gamma s}
       +\|f_p^*-f^*\|_\infty.                            \tag{S15}
\]

In particular every joint sequence `p->infinity,s->infinity` converges to
`f^*`; the two iterated limits commute. This is established for the modified
two-stage optimizer because the fitting phase has a proved uniform gap.
It does not interchange order and infinite time for the original full GF.

There is no guaranteed sign of `loss_(p+1)-loss_p` during burn-in, no universal
decrease of whole-circle endpoint error at each consecutive order, and no
rate purely in the integer `p`. The exact bound is in the actual nonlinear
feature/readout defects. The source proves these defects vanish for its
specific hierarchy, not at a quantitative dictionary-degree rate.

## 6. Finite-rank identifiability obstruction and interpretation

The finite training law alone cannot generally determine a whole-circle
predictor, even after hidden features have been fixed. At any order with
positive training Gram, put `V_p=span{H_p(u_a):1<=a<=m}`. If some test input
`u_0` has `H_p(u_0) notin V_p`, let

\[
 z=(I-P_p)H_p(u_0)\ne0.
\]

Replacing any interpolating readout `c_p^*` by `c_p^*+a z` leaves every
training prediction unchanged, while changing the test prediction at `u_0`
by `a||z||_2²`. Both claims follow directly from orthogonality. Thus arbitrarily
different test predictions have identical zero training loss whenever this
explicit feature-span condition holds. This is a finite-rank obstruction,
not a claim that the condition has been proved at every reached canonical
state. It explains why (S10)'s optimizer-dependent nullspace selection is
essential, and why loss convergence alone does not prove endpoint selection.

The two-stage procedure retains both the learned hidden fields and the
readout's previously acquired nullspace component. It is consequently not
the initialized frozen-feature comparator. The original nonlinear learning
mechanism operates for a positive common interval; hidden motion is a
separate claim and may vanish for special labels. The source's activity
results can be used on their stated family/time, but no activity guarantee
has been assumed at an arbitrary chosen burn-in time here.

One can verify actual hidden-action learning near initialization without
assuming the source's separate activity conclusion. Suppose at least one
label is nonzero. Put

\[
 v=c'(0)=2\sum_a\pi_a y_a H^2(0,u_a).
\]

Lemma 2 implies `v != 0`. The middle rank equation, `c(0)=0`, and continuity
of its other factors give the strong Hilbert–Schmidt limit

\[
 \lim_{t\downarrow0}\frac{K'(t)}t
 =K''(0)
 =2\sum_a\pi_a y_a
       [v\,\phi'(Z^2(0,u_a))]\otimes h_a.                \tag{S16}
\]

To justify the product limit, `c(t)/t -> v` in `L2`, its supremum norm
is bounded by `2Y`, and all tanh gates converge in `L2` and are bounded.
The remaining factors converge in `L2` or as finite scalars; the two-factor
rank inequality therefore gives convergence in Hilbert–Schmidt norm. No
unproved global twice-differentiability theorem is needed.

The independent lower fields from Lemma 1 have dual vectors
`tilde h_b=sum_j(V^{-1})_(jb) h_j` satisfying
`<h_a,tilde h_b>=1_(a=b)`. Applying (S16) to `tilde h_b` gives
`2pi_b y_b v phi'(Z^2(0,u_b))`. For any nonzero `y_b` this is nonzero:
`v` is nonzero in `L2`, and the derivative of tanh is strictly positive at
every finite real argument. Thus `K''(0) != 0`. Integrating (S16) yields
`K(t)/t² -> K''(0)/2`, so `K(t) != 0` for all sufficiently small positive
`t`. Every positive burn-in interval therefore contains genuine learning of
the middle action. Canonical compact-time convergence also gives nonzero
middle-action learning at that same fixed early time for all sufficiently
large orders. This does not assert a lower bound on final hidden displacement
at the particular endpoint (S6).

## 7. Claim status and hostile audit

| Claim | Status | Boundary |
|---|---|---|
| Initial full Gaussian training Gram is positive | Proved above | Finite directions distinct modulo sign |
| A data-computable common positive burn-in preserves a gap | Proved, (S3)–(S7) | Canonical existence domain and finite training law |
| Canonical order hierarchy inherits that gap | Proved using the actual source convergence, (S1), (S8) | Eventual orders; no effective threshold |
| Modified-optimizer endpoint exactly fits | Proved, (S9)–(S12) | Positive training Gram |
| Consecutive endpoint comparison and whole-circle stabilization | Proved, (S13)–(S15) | Same burn-in and same phase optimizer |
| Nonzero hidden-action learning occurs during burn-in | Proved, (S16) | At least one nonzero compatible label; eventual orders |
| Original full-GF fitted endpoints stabilize | Open in this route | Hidden mobilities are switched off in (S2) |
| Rate expressed only in order `p` | Not proved | Source provides strong compact-set approximation without a rate |
| Nonzero hidden motion for every finite data law | Not claimed | Zero/degenerate labels can produce no motion |

The strongest substitution objection is real and is stated at the theorem:
the optimizer changes after the common burn-in. The nonlinear dictionary,
the initializing action and its true adjoint, the original full GF before
burn-in, and the whole-circle prediction norm are all retained. The proof
requires no target trajectory in the order rule; (S6) uses only initialized
Gaussian integrals. It uses a finite-training spectral gap only after proving
one. Poor conditioning as inputs approach duplicate or antipodal directions
is visible in `gamma_0`, the chosen burn-in and the comparison constants.
There is no uniform sample-count or input-separation claim.

No numerical experiment was needed or run. No changes to established theory,
maintained code, other study files, Git state, or promotion status were made.

## 8. A distinct noisy selector with a unique minimum-norm endpoint

This section specifies a second optimizer. The hidden fields are again frozen
after the same nonlinear burn-in. In contrast to (S2), it also damps the
readout component invisible to the training data, and injects bounded random
forcing into precisely that component with amplitude tending to zero with
the loss. Its endpoint is therefore different from (S10) in general.
The noise here is a bounded measurable random forcing; it is not Brownian
white noise, Langevin dynamics, or an assertion about noisy full-network GF.

At a fixed eventual order suppress `p` and use its fixed `E,G` from Section 4,
with `G>=gamma I`. Set

\[
 P=E^*G^{-1}E,\qquad N=I-P,\qquad
 L(c)=|Ec-\bar y|^2.
\]

Choose `nu=gamma`, `0<=eta<=gamma`, and a strongly measurable process `U_s`
in the upper population Hilbert space with `||U_s||_2<=1` almost everywhere,
and solve pathwise

\[
 c'=-2E^*(Ec-\bar y)-\nu Nc
                +\eta\sqrt{L(c)}\,NU_s,\qquad c(0)=c_p(T). \tag{S17}
\]

There is a concrete finite-mark choice at every canonical order: take
`U_s=sigma(s) tanh(xi_1)`, where `|sigma(s)|<=1` is any measurable bounded
random scalar signal and `xi_1=A_0 tanh(g_1)` is the initialized upper probe
already retained in the degree-one polynomial core. Thus this forcing can
be supplied from an existing static mark and one exogenous scalar signal;
it need not encode an extra field or a target trajectory. Different orders
may use any allowed signal without changing the limiting selected endpoint.
If literal own-state autonomy is required, a specified finite-state random
signal generator can be included in the saved state; (S17) itself is an
explicitly forced optimizer.

For each fixed forcing path, its vector field is globally Lipschitz in `c`
with a uniform finite bound: `E,N` are bounded, and
`c -> ||Ec-bar y||` is Lipschitz with constant `||E||<=1`.
On an interval whose length times that bound is less than one, the integral
map is a contraction on continuous Hilbert-space paths (with the forcing
integrated as a strongly measurable bounded function). Iterating intervals
gives the unique absolutely continuous solution for all finite `s`; the
linear-growth bound prevents finite-time escape. This argument applies
pathwise and requires no stochastic-calculus limit exchange.

Let `r=Ec-bar y` and `z=Nc`. Since `EN=0` and `NE^*=0`, (S17) gives

\[
 r'=-2Gr,\qquad z'=-\nu z+\eta\sqrt L\,NU_s.
\]

Therefore, almost everywhere,

\[
 L'=-4r^TGr\le-4\gamma L,
\]
\[
 (\|z\|_2^2)'
 \le-2\nu\|z\|_2^2+2\eta\sqrt L\,\|z\|_2
 \le-\nu\|z\|_2^2+\frac{\eta^2}{\nu}L.
\]

The final inequality is the elementary square
`(sqrt(nu)||z||-eta sqrt(L)/sqrt(nu))²>=0`. For
`V=L+||z||²`, our choices `nu=gamma` and `eta<=gamma` yield

\[
 V'\le-3\gamma L-\gamma\|z\|_2^2\le-\gamma V,
 \qquad V(s)\le V(0)e^{-\gamma s}.                        \tag{S18}
\]

The endpoint is consequently

\[
 c^\dagger=E^*G^{-1}\bar y,\qquad
 f^\dagger(u)=k(u)^TG^{-1}\bar y.                         \tag{S19}
\]

Indeed `c-c^dagger=E^*G^{-1}r+z`, with orthogonal summands, so

\[
 \|c-c^\dagger\|_2^2=r^TG^{-1}r+\|z\|_2^2
 \le\max\{\gamma^{-1},1\}V(0)e^{-\gamma s}.              \tag{S20}
\]

This proves convergence on the whole circle, zero limiting training loss,
and independence of the endpoint from the forcing path. It also identifies
the selection: every interpolating readout equals `c^dagger+z` with
`z in ker E`; orthogonality makes its squared norm
`||c^dagger||²+||z||²`, uniquely minimized by `z=0`.

At every sufficiently large canonical order and for the full target,
`V(0)<=Y²+4Y²T²` by the burn-in energy and readout bounds. The same positive
`gamma=gamma_0/4` therefore gives a uniform bound (S20). Subtracting (S19)
at two orders, using Section 5's Gram/kernel estimates, gives

\[
 \|f_p^\dagger-f_q^\dagger\|_{C(S^1)}
 \le2Y(\gamma^{-1}+\gamma^{-2})\delta_{p,q}.              \tag{S21}
\]

In particular the consecutive-order bound uses `q=p+1`, and comparison
with the full canonical learned hidden field gives

\[
 \|f_p^\dagger-f^\dagger\|_\infty
 \le2Y(\gamma^{-1}+\gamma^{-2})\delta_p\longrightarrow0.  \tag{S22}
\]

Together with the uniform transient estimate (S20), this proves convergence
along every joint sequence of order and fitting time tending to infinity,
independently of the admissible forcing paths. For a positive chosen noise
coefficient the forcing is nonzero only when both the loss and `NU_s` are
nonzero; a positive coefficient alone does not ensure actual noise injection.
This exact-fitting optimizer has a stable whole-circle selected endpoint.
Its nonlinear hidden learning occurs
only during the initial burn-in, as in the first optimizer; after burn-in
the hidden fields are frozen. No claim is made for noise in the original
full nonlinear GF or for a positive fixed noise floor at zero loss.

## 9. Verified short-horizon extension to all bounded circle laws

This section is an additional derivation from the complete newly authorized
C.4.7.10.A.1–A.4. Part B states its hierarchy theorem for a represented
two-arc law. We do not attribute a broader written theorem to B: we verify
that its proof extends to each separately fixed Borel probability law on
`sqrt(2) S^1 x [-1,1]`. This concerns exact population closures, not extending
the represented-law interface or claiming a new numerical tolerance rule.

Fix such a law `mu` and `T_0=1/200`. A.1 and the complete construction in
A.2–A.4 give its actual canonical strong `C1` population GF through `T_0`,
uniqueness on the same carrier, the energy identity (H3.S17), raw/action
bounds (H3.S18), `||c(t)||infty<=2t`, and the individual passive-query bound

\[
 \sup_{t\le T_0,u\in S^1}\tau_s(Q(t,u))
 \le4(C+D)\exp\left(-\frac{(s-D)^2}{8C^2}\right),\quad s\ge D, \tag{S23}
\]

where `C,D` are A's explicit constants. The construction and bounds are for
every Borel law, not only the executable family later described in A.1.

Use exactly B's initialized-word augmented Chebyshev lists and its fixed
ridge `eta_p=1/[1024(p+1)²]`. Their law-independent finite feature maps
`U_(ell,p)`, positive contractions `Q_(ell,p)=U_(ell,p)U_(ell,p)^*`, and
initialized action `B_p=Q_(2,p) A_0 Q_(1,p)` are unchanged. The dense
initialized-word span and the bound

\[
 \|(I-Q_{\ell,p})S_{\ell,p}a\|_2
       \le\tfrac12\sqrt{\eta_p}\,|a|
\]

for every vector from a fixed earlier raw span prove strong convergence
of `Q_(ell,p)` to the identity on the initialized observable spaces, by
zero-padding coefficients, density, and contraction. Hence both `B_p` and
`B_p^*` converge strongly to the corresponding full initialized actions,
with common operator bound two. No training-law condition enters this step.

The reference trajectory for this broader `mu` stays in the same initialized
observable spaces. To verify this without a new invariance premise, take A's
finite-law raw Euler construction on the common carrier. Initially `g,0,0`
are in those spaces/block. Each Euler step applies finite sums, bounded
coordinate gates, the retained action or its adjoint, and finite learned
ranks. The observable spaces are generated sigma-field `L2` spaces, closed
under those bounded gates and preserved by both action directions; their
HS block is closed. Induction keeps the rows, readout and learned ranks
there. A.3's strong completion, first for finite approximations and then
for the fixed Borel law, retains that property. Difference quotients and
closedness also put the continuous derivative `K'(t)` in the same HS block.
Real marks cause no obstruction: B's rational-word completion proof already
places every finite real-mark observable in these spaces.

The exact reference fields `H^1(t,u)` and `Delta^2(t,u)` are continuous
`L2` images of the compact set `[0,T_0] x S^1`. For the second field use
the bounded reference readout and A.3's proved bounded-multiplier continuity.
The curve `K'(t)` is compact in HS norm. Uniform strong approximation on
compact sets (choose a finite net and use the common operator bound), and
finite-rank approximation in the HS block, give

\[
 \begin{split}
 \epsilon_p={}&\sup_{t,u}\|(B_p-A_0)H^1(t,u)\|_2
   +\sup_{t,u}\|(B_p^*-A_0^*)\Delta^2(t,u)\|_2\\
 &+\sup_t\|Q_{2,p}K'(t)Q_{1,p}-K'(t)\|_{\rm HS}
 \longrightarrow0.                                    \tag{S24}
 \end{split}
\]

Every exact finite closure is globally well posed by C.4.7.9.4 for this
bounded-label law; its energy proof does not restrict the law. Its raw/action
bounds and A's reference bounds therefore give one common comparison ball,
independent of `p`. For

\[
 e_p=\|w_p-w\|_2+\|K_p-K\|_{\rm HS}+\|c_p-c\|_2,
\]

the forward difference splits as

\[
 A_p(H_p^1-H^1)+(K_p-K)H^1+(B_p-A_0)H^1,
\]

which bounds both upper hidden and prediction differences by
`C_1(e_p+epsilon_p)`. Subtract the bounded-reference-readout upper
backward field and then its reverse action to get the same bound for
`Delta_p^2-Delta^2` and `Q_p-Q`. For the remaining lower gate split only
the unchanged reference reverse field at magnitude `s>=1`; its difference
is bounded by `C_2(e_p+epsilon_p)+2s e_p+2tau_s(Q)`.
Finally the learned-rank derivative difference is exactly

\[
 Q_{2,p}\{F_K(w_p,A_p,c_p)-F_K(w,A,c)\}Q_{1,p}
          +Q_{2,p}K'Q_{1,p}-K'.
\]

Subtracting its two factors and residual and using contraction bounds the
first term by `C_3(e_p+epsilon_p)` and the second by `epsilon_p`.
Thus the same proved subtraction as B, now with A's all-law reference,
gives

\[
 D^+e_p\le C_4(1+s)(e_p+\epsilon_p)+C_4\tau(s),\quad e_p(0)=0,
\]
\[
 \sup_{t\le T_0}e_p(t)
 \le C_4T_0e^{C_4(1+s)T_0}
             \{(1+s)\epsilon_p+\tau(s)\}.                \tag{S25}
\]

The error is absolutely continuous as a sum of norms of strong Hilbert
curves, so the scalar integrating-factor argument applies, including at
zero norm. First send `p` to infinity with `s` fixed using (S24), and then
send `s` to infinity using (S23). Its negative quadratic exponent dominates
the fixed positive linear exponent. This proves compact-time raw convergence,
and the forward subtraction proves uniform whole-circle hidden-field and
prediction convergence. In particular it supplies exactly (S1) for this
general law and every burn-in `T<=T_0`.

The remaining exact-fit and endpoint-comparison proofs need a finite law
and the compatibility condition because they invert its finite training
Gram. They consequently apply to every finite compatible dataset on the
circle with labels in `[-1,1]`. Binary labels are a special case. This is a
verified extension within this study, not a promotion or a claim that B's
maintained text already states the expanded result.
