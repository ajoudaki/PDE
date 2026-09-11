# Combined P2 tail contract: active averages, probe atoms, and radial saturation

Author: `/root/p2_continuation`, 2026-09-11. This is a mature comparison
following the freeze of the independent routes, not another blind attempt.
Status: the implications and reductions below are proved conditionally on
one explicit raw-Euler tail hypothesis. That hypothesis remains open; no
unconditional positive-neighborhood theorem is claimed.

## 1. Result and new input scope

The same averaged exponential-tail hypothesis used for raw continuation
also suffices for the uniform nonlinear response remainder. Two bridges
remove apparently stronger extra requirements:

1. Add a small training atom at a chosen passive input. Uniform law
   continuity then upgrades training-law averaged tails to passive-input
   tails, uniformly on a smaller neighborhood.
2. The exact radial tanh identity from `P2_REACHED_TAILS.md` upgrades
   exponential query marginals to a Gaussian-square moment for the full
   reached row. Jensen in time and data eliminates the need for a query
   supremum inside the moment bound.

Together these give all finite moments of the inverse-gate forcing and
therefore the condition (UI) of `P2_VARIATION.md`. This does not require
Gaussian query tails, an Lp action estimate for A0, or uniform integrability
of the divided nonlinear deviations as a separate assumption.

The supervisor authorized complete mature comparison inputs
`P2_VARIATION.md` and `P2_REFERENCE_COMPARISON.md`, then added the frozen
`P2_REACHED_TAILS.md`. All three were read completely before their use;
the updated observation-contract paragraph in the reference comparison
was also read. Previous permitted inputs remain the established C.4.1-C.4.6
and invoked dependencies, NOTATION, the frozen P1 packet, and this author's
frozen `P2_CONTINUATION.md`. No other P2 artifact, study history, prior
review, or other study is used. The original frozen reports are unchanged.

## 2. Exact model and the single extra hypothesis

Set `T=40`, `Y>=1`, `Z=S1 x [-Y,Y]`, and use transport cost
`|u-v|+|y-z|`, with `u=x/sqrt(2)` and diameter `D=2+2Y`.
The reference is `nu*=1/2 delta_(e1,+1)+1/2 delta_(e2,-1)`.
Write `U_r={mu:W1(mu,nu*)<r}`. The model has two equal-width tanh hidden
layers, no biases, Gaussian stored variances `(1,1/n,1/n^2)`, mobilities
`(n,1,n)`, and unhalved exactly integrated mean-square physical GF.

Use the common canonical spaces and the exact fields

\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad
 H^2(u)=\phi(Z^2(u)),\quad f(u)=\langle c,H^2(u)\rangle,
\]
\[
 \delta(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\delta(u),\quad
 r(u,y)=f(u)-y,\quad A=A_0+K,\quad\phi=\tanh.
\]

The raw state has full row L2, middle increment HS, and readout L2, with
sum distance `d=||Delta w||2+||Delta K||HS+||Delta c||2`. Its initialization
is `(g,0,0)`, `g~N(0,I2)`, while A0 and A0* are the actual initialized
Gaussian action and its Hilbert adjoint. Only K is HS. At finite width the
three norms are respectively Frobenius/sqrt(n), Frobenius, and
Euclidean/sqrt(n), with the actual finite random readout retained.

The exact field, in `(w,K,c)`, is

\[
 F_\mu(\theta)=-2\left(
 \int r\phi'(w\cdot u)Q(u)u\,d\mu,
 \int r\delta(u)\otimes H^1(u)\,d\mu,
 \int rH^2(u)\,d\mu\right).                         \tag{1}
\]

For `tau_R(v)=||v 1_(|v|>R)||2`, the sole unverified hypothesis is:

**Raw-Euler contract H.** There is `rho>0` such that, for every `r<rho`,
there are `a_r,M_r,h_r>0` for which every finite Borel law `lambda in U_r`
and every finite raw population Euler mesh of maximal step at most `h_r`
through T, from the above initialization, obey at every grid node

\[
 \tau_R(c_k)+\int\tau_R(Q_k(u))\,d\lambda(u,y)
             \le M_r e^{-a_r R},\qquad R\ge1.            \tag{H}
\]

Here a finite law means finitely supported. There is no support-count,
weight, Gram-rank, or angle restriction. Each mesh is a separately fixed
finite Gaussian program before any width limit. The constants are uniform
in its length. Readout tails are already zero beyond a uniform bound, so
the substantive part of (H) is its integral of individual Q tails.

The complete proof in `P2_CONTINUATION.md`, Section 4, establishes from
(H) strong population construction on `U_rho`, raw law continuity,
uniqueness/restart, and arbitrary simultaneous empirical-law/width finite-GF
capture. That construction uses fixed same-array proxies and finite-rank
HS contractions; no cross-carrier operator distance is used. The present
report proves the additional implications required for nonlinear response.

## 3. Uniform law comparison on one fixed raw Euler mesh

We first make the comparison independent of the mesh size. The global
Euler bounds (3)-(4) of `P2_CONTINUATION.md` give finite constants for row
L2, action norm, c L2 and c supremum through T, uniformly in law and mesh.
They follow directly from `C_(k+1)+Y<=(1+2h_k)(C_k+Y)`, then the bounded
rank and row increments. Fix a ball containing these states.

On that ball the raw HS transport estimate is

\[
 \|F_\lambda(\theta)-F_\kappa(\bar\theta)\|_{\rm sum}
 \le C(1+R)\{d(\theta,\bar\theta)+W_1(\lambda,\kappa)\}
       +C\tau_{\kappa,R}(\bar\theta).                  \tag{2}
\]

It is C.4.1 with the identical HS rank difference inequality; the full
proof and norm upgrade are in `P2_CONTINUATION.md`, Section 3.

Consider two finite laws on exactly the same mesh. At grid node k let
`e_k=d(theta_lambda,k,theta_kappa,k)` and `q=W1(lambda,kappa)`.
There is no interpolation defect in their exact recursion:

\[
 e_{k+1}\le e_k+h_k C\{(1+R)(e_k+q)+M_r e^{-a_rR}\}.
\]

Set `s_k=e_k+q`. For `0<s_k<=1`, choosing
`R=1+a_r^{-1}log(1/s_k)` gives, for a fixed `L<infinity`,

\[
 s_{k+1}\le s_k+h_k Ls_k\log(e/s_k).                  \tag{3}
\]

The scalar function `v->Lv log(e/v)` is increasing on `(0,1)`.
Its exact scalar flow from q is

\[
 y(t)=e^{1-e^{-Lt}}q^{e^{-Lt}}.
\]

While `y<=1`, integration of its increasing positive velocity gives
`y(t+h)>=y(t)+hL y(t)log(e/y(t))`. Induction in (3) therefore yields
`s_k<=y(t_k)`. Choose a fixed `q0>0` small enough that `y(T)<=1/2`
whenever `q<=q0`; this closes the condition used in the induction.
Consequently, with `alpha=e^{-LT}>0`,

\[
 \max_k d(\theta_{\lambda,k},\theta_{\kappa,k})
             \le C_0q^\alpha,\qquad q\le q_0.           \tag{4}
\]

Every constant is independent of the mesh. Unlike a comparison of
different meshes, (4) has no additive `h` term. At `q=0`, the two literal
recursions agree; the estimate extends by zero. This same-mesh fact allows
a probe atom of arbitrarily small mass before the mesh is removed.

## 4. Probe atoms turn active averages into passive exponential tails

Choose fixed `0<r0<r1<rho`. All constants in this section use (H) on
`U_r1`. Let lambda be any finite law in `U_r0`, fix any passive input u,
and choose the valid label zero. Define another finite training law

\[
 \lambda_\eta=(1-\eta)\lambda+\eta\delta_{(u,0)}.
                                                               \tag{5}
\]

Use the same initialized carrier and mesh. There is a fixed
`eta_bar>0` such that `eta<=eta_bar` ensures both
`lambda_eta in U_r1` and `D eta<=q0`: for instance take
`eta_bar<min(1,(r1-r0)/D,q0/D)`. The direct mixture coupling gives
`W1(lambda,lambda_eta)<=D eta`.

At a fixed passive input, Q is Lipschitz in raw state on the above ball
with its readout supremum bound. Indeed

\[
 \|Z^2-\bar Z^2\|_2\le\|K-\bar K\|_{HS}
                              +\|\bar A\|\|w-\bar w\|_2,
\]
\[
 \|\delta-\bar\delta\|_2
 \le\|c-\bar c\|_2+2\|\bar c\|_\infty\|Z^2-\bar Z^2\|_2,
\]
\[
 \|Q-\bar Q\|_2
 \le\|K-\bar K\|_{HS}\|\delta\|_2
                    +\|\bar A\|\|\delta-\bar\delta\|_2.
                                                               \tag{6}
\]

There is no first gate multiplying Q in (6). Equations (4)-(6) give
`||Q_lambda,k(u)-Q_lambda_eta,k(u)||2<=C1 eta^alpha`.
Since the law in (5) has mass at least eta at the chosen atom, (H) gives

\[
 \tau_{R/2}(Q_{\lambda_\eta,k}(u))
                       \le\eta^{-1}M_{r1}e^{-a_{r1}R/2}.
\]

The elementary tail inequality
`tau_R(P)<=2||P-P'||2+2tau_(R/2)(P')` therefore proves

\[
 \tau_R(Q_{\lambda,k}(u))
 \le2C_1\eta^\alpha+2\eta^{-1}M_{r1}e^{-a_{r1}R/2}.
                                                               \tag{7}
\]

The atom mass is chosen only as an analysis device. Set

\[
 \eta=\bar\eta\exp\{-a_{r1}R/[2(1+\alpha)]\},\qquad
 b={a_{r1}\alpha\over2(1+\alpha)}>0.
\]

Both terms in (7) are bounded by a fixed constant times `e^{-bR}`.
For all `R>=2`, uniformly in the original law, node, mesh, and passive u,

\[
                       \tau_R(Q_{\lambda,k}(u))\le C_2e^{-bR}.
                                                               \tag{8}
\]

This obtains the passive uniformity without asserting that an averaged
tail bound for the original law controls an off-support query directly.
The factor `eta^-1` in (7) is paid for by a quantitative comparison with
the law in which the query is active. No division by a possibly vanishing
preexisting atom weight occurs.

For example, (8) implies constants `beta>0,M<infinity` with

\[
 \sup_{\lambda\in U_{r0}\ {m finite},h,k,u}
           E\exp(\beta|Q_{\lambda,k}^h(u)|)\le M.        \tag{9}
\]

Take `beta=b`: for `R>=2`,
`P(|Q|>R)<=R^-2 tau_R(Q)^2<=C2^2 e^{-2bR}`; integrating
`beta exp(beta R)P(|Q|>R)` and bounding the interval `[0,2]` proves (9).

Apply the strong raw construction already obtained from (H). For each
target `mu in U_r0`, use finite laws and meshes converging to it within
`U_r0`. The c supremum bound passes to the strong L2 limit by an almost
sure subsequence. Equation (6) then gives Q convergence in L2, uniformly
in deterministic passive inputs. At each fixed time/input, bounded
continuous truncated exponentials and monotone convergence pass (9) to
the limiting strong flow, including limits of preceding grid nodes.
The same constants at every deterministic time and input give

\[
 \sup_{\mu\in U_{r0},\,t\le T,\,u\in S^1}
                    E e^{\beta|Q_\mu(t,u)|}\le M.        \tag{10}
\]

No moment of `sup_(t,u)|Q|` is asserted. Equation (10) is a bound on
individual marginals uniform in their parameters.

## 5. Radial saturation needs only query marginals

Use now the complete radial argument in `P2_REACHED_TAILS.md`, Section 3.
We reproduce it and its strengthened consequence to expose all hypotheses.
The strong path has pointwise absolutely continuous row representatives
by Fubini. Since
`cosh^2 z>=1+z^2>=2|z|`, one has `|z|phi'(z)<=1/2`. Equation (1) yields

\[
 {d\over dt}|w(t)|^2
 =-4\int r(t,u,y)Q(t,u)(w(t)\cdot u)\phi'(w(t)\cdot u)d\mu
 \le2\int |r(t,u,y)|\,|Q(t,u)|d\mu.                  \tag{11}
\]

The population energy identity gives `||c(t)||2<=Y sqrt(T)` and hence
`|r(t,u,y)|<=R_T:=Y(1+sqrt(T))`. These are uniform for all laws here.
Define the nonnegative coordinate field

\[
 J_\mu=\int_0^T\int |Q_\mu(s,u)|d\mu(u,y)ds.
\]

Its integral is finite almost surely, by (10) and Fubini. Integrating
(11) gives the pathwise bound

\[
 W_\mu^2:=\sup_{t\le T}|w_\mu(t)|^2
                        \le|g|^2+2R_TJ_\mu.             \tag{12}
\]

For `lambda T<=beta`, Jensen against the probability measure
`T^-1 ds dmu` and (10) give

\[
 E e^{\lambda J_\mu}
 \le {1\over T}\int_0^T\int E e^{\lambda T|Q_\mu(s,u)|}d\mu ds
 \le M.                                                \tag{13}
\]

This is precisely the replacement for a coordinate supremum estimate:
we exponentiate an integral of query magnitudes, not their supremum.
Choose `0<eta<=min(1/8,beta/(8R_T T))`. By Holder, the Gaussian root
integral in dimension two, and (12)-(13),

\[
 \sup_{\mu\in U_{r0}}E e^{\eta W_\mu^2}
 \le(E e^{2\eta|g|^2})^{1/2}
                       (E e^{4\eta R_TJ_\mu})^{1/2}
 \le(1-4\eta)^{-1/2}M^{1/2}=:M_w<\infty.              \tag{14}
\]

The scalar Gaussian formula is obtained by combining the normal density
with the exponential and integrating the two independent coordinates.
No independence between the reached Q and g is used; that is the purpose
of Holder in (14). This is a Gaussian-square *moment bound*, not a claim
that the row's law remains Gaussian.

For every separately fixed positive integer p, the exponential series
in (10) gives `E|Q(t,u)|^(2p)<=M(2p)!/beta^(2p)`. Also
`4pW<=eta W^2+4p^2/eta`. Consequently

\[
 \sup_{\mu\in U_{r0},t,u,j}
 E\{\cosh^2(w_{\mu,j}(t))|Q_\mu(t,u)|\}^p
 \le e^{2p^2/\eta}M_w^{1/2}
                 \{M(2p)!/\beta^{2p}\}^{1/2}<\infty.    \tag{15}
\]

Here `cosh^2(w_j)<=exp(2W)` and Cauchy-Schwarz gives the two factors.
This bound uses only individual Q marginals, together with the row path
bound already proved. It holds for the entire reached family on the
smaller neighborhood, not only along contamination rays.

In particular, the actual clock forcing field

\[
 Z_{\mu,j,u}=u_j\cosh^2(w_{\mu,j})\phi'(w_\mu\cdot u)Q_\mu(u)
\]

satisfies `sup E|Z|^3<=C3`, because `|u_j|,|phi'|<=1`. Therefore

\[
 \sup_{\mu\in U_{r0},t,u,j}
 E|Z_{\mu,j,u}|^2 1_{|Z_{\mu,j,u}|>R}\le C_3/R.        \tag{16}
\]

Equation (16) is the explicit (UI) needed by the variation route. No
special contamination fraction is needed for this tail implication.

## 6. Combined consequences and identification with P1

Choose `epsilon0>0` with `epsilon0 D<r0`, for example
`epsilon0=min(1/2,r0/(2D))`. Then every contamination law
`mu_(epsilon,nu)=(1-epsilon)nu*+epsilon nu`, with any Borel probability
nu and `0<=epsilon<=epsilon0`, lies strictly in `U_r0`.

Under (H), the construction from `P2_CONTINUATION.md` supplies all these
strong paths, uniformly bounded in the raw norms. Equations (15)-(16)
verify the additional hypothesis of `P2_VARIATION.md` uniformly over the
entire contaminating law class. Its theorem consequently gives

\[
 \sup_{\nu,t\le40}
 \|\theta_{\mu_{\epsilon,\nu}}(t)-\theta_*(t)
                   -\epsilon\dot\theta_{\nu-\nu_*}(t)\|_{\rm raw}
                                                    =o(\epsilon),
                                                               \tag{17}
\]
\[
 \sup_{\nu,t\le40,u\in S^1}
 |f_{\mu_{\epsilon,\nu}}(t,u)-f_*(t,u)
                 -\epsilon\mathscr D_{\nu-\nu_*}f(t,u)|
                                                    =o(\epsilon).\tag{18}
\]

The clock conventions match exactly. The variation report uses
`X_j=F(w_j)`, whereas P1 uses `X_j=F(w_j)-F(g_j)` with
`F(z)=z/2+sinh(2z)/4`. The difference is the same fixed L2 Gaussian-root
field for every law, so clock differences and linear tangents coincide.
Both give `delta w_j=phi'(w_*,j)xi_j`, and at the reference axes the
clock field is `X_j'=-r_j Q(e_j)`. Its differentiated equation and signed
forcing are precisely P1.T5-T6; uniqueness of that bounded linear
equation identifies the response in (17)-(18) with P1. No derivative is
interchanged with a width limit.

For clarity, the variation theorem's remaining mechanism is independent
of the tail construction. Its atom-forcing family is continuous on the
compact time/input/label set; probability integrals lie in the compact
closed convex hull of that image. The bounded linear solution map makes
the P1 tangent family compact in the continuous-curve L2/HS/L2 space.
The reference clock field is Lipschitz when one compared readout is
bounded pointwise. Taylor consistency on that compact tangent family
uses bounded multipliers and fixed-vector truncation, not ambient
L2 differentiability. The actual perturbed curve has the needed bounded
readout; (16) supplies continuity of its contamination forcing. These
are exactly the hypotheses and proof steps checked in the complete
variation report.

One can additionally use (14)-(15) in the Holder/interpolation argument
of `P2_REACHED_TAILS.md`, Section 5. It gives a `d^(1/3)` modulus for
the weighted forcing between reached raw states. Every moment needed
there is supplied by individual marginal bounds in (14)-(15); a Q path
supremum is unnecessary. This makes the contamination forcing defect
`O(epsilon^(4/3))` after the clock `O(epsilon)` estimate. The total
nonlinear remainder remains the asserted `o(epsilon)`, since no
quantitative compact-tangent Taylor modulus has been established.

Thus (H) is a single sufficient finite-program contract for: strong
autonomous neighborhood flow, raw law continuity and unique restart,
arbitrary simultaneous empirical-law/width finite-GF capture, and uniform
first-order population contamination response. Width capture retains
the fixed generated observation contract, HS contractions and both
action directions. No finite-width nonlinear remainder, growing-time
claim, or simultaneous epsilon/width rate follows from this argument.

## 7. Why the remaining contract is not supplied by P1

The learned transpose has a bounded-coordinate contribution. At a raw
Euler node it is the literal rank sum

\[
 K_k^*\delta_k(u)
 =-2\sum_{s<k}h_s\int r_s(v,y)H_s^1(v)
                    \langle\delta_s(v),\delta_k(u)\rangle d\lambda,
\]

and the uniform c and residual bounds give an L-infinity bound `B_T`
independent of mesh and law. The integral version is proved in
`P2_CONTINUATION.md`, Section 2.3, and `P2_REACHED_TAILS.md`, Section 2.
Hence (H) is equivalent, up to fixed tail constants/cutoff rescalings,
to the following specific initialized-query estimate:

\[
 \sup_{\lambda\in U_r\ {\rm finite},h,k}
 \int\|[A_0^*\delta_{\lambda,k}^h(u)]
              1_{|A_0^*\delta_{\lambda,k}^h(u)|>R}\|_2d\lambda(u,y)
                         \le M'_r e^{-a'_rR}.           \tag{19}
\]

To check equivalence, write `Q=P+B`, `|B|<=B_T`. For `R>=2B_T`, the
event `|Q|>R` implies `|P|>R/2` and `|Q|<=2|P|` there; thus
`tau_R(Q)<=2tau_(R/2)(P)`. Interchanging P and Q gives the converse.
Smaller cutoffs are covered by the uniform L2 bound. This removes all
learned-rank tails from the remaining question, but it does not estimate
the adapted initial query in (19).

P1 proves its needed reference estimates using the special reference
clock's width-independent column response. For a changed-law comparison,
the extra raw term is

\[
 [\phi'(w\cdot u)-\phi'(\widetilde w\cdot u)]\widetilde Q(u).
                                                               \tag{20}
\]

It does not cancel at general inputs. Bounding (20) in L2 needs a
reached weighted sensitivity or query-tail estimate; bounded A0 and
bounded upper backward input do not supply one. The cavity-Gaussian
part itself is controlled in `P2_REACHED_TAILS.md`, Section 7, but the
learned cavity response remains the unproved term there. The radial
bound yields row fourth moments unconditionally; it gives (14) only
after an exponential query estimate is available. It cannot bootstrap
(19) from itself.

The new probe-atom argument also does not prove (19): its first use of
the quantitative law comparison (4) explicitly consumes (H). P1's
one-reference comparison controls distance to nu* only, leaving a fixed
positive error at a changed law. That error survives tail removal. Thus
using P1 to invoke (4) for two arbitrary changed laws would be circular.
The present report makes no such invocation.

A stronger but concrete possible resolver of (19) is a uniform bound
on the total absolute named-forward-source response coefficients of each
active reverse query in these finite raw programs. Since tanh features
are bounded, the source formula would then write the query as a bounded
variance Gaussian plus a bounded remainder. C.2 proves those coefficient
bounds only on its chosen short interval; P1 obtains a separate global
reference bound through its clock cancellation. Neither supplied proof
extends them through 40 for the required changed-law family. No new
unconditional bound on those coefficients was obtained in this subtask.

## 8. Check record and current status

| Statement | Status and dependency |
|---|---|
| Same-mesh Hölder law estimate (4) | Proved from (H), with no additive mesh error. |
| Passive exponential marginals (8)-(10) | Proved from (H) by probe-atom insertion and strong completion. |
| Gaussian-square reached row moment (14) | Proved from passive exponential marginals and the exact radial identity. |
| Weighted forcing moments and UI (15)-(16) | Proved by Holder/Jensen; no supremum-Q premise or Lp action bound. |
| All requested continuation/capture/response conclusions | Conditional on the single contract (H). |
| Contract (H), equivalently sufficient initialized estimate (19) | Open. P1 and learned-transpose boundedness do not verify it. |

This is a genuine reduction of the additional estimate: averaged active
exponential tails already suffice, whereas separately assuming all-passive
Gaussian tails or a finite-GF time/input query supremum is unnecessary
for this combined proof. The approximation families differ from those
in P2_REACHED_TAILS's hypothesis E, so no unproved logical equivalence
between H and E is asserted.

Author checks: scalar discrete comparison with its monotone exact flow;
probe mass and neighborhood margins; the `eta^-1` tail factor; tail-to-
exponential integration; radial sign and mean-loss factor four;
Jensen's normalized time/law measure; Gaussian-root/Holder exponents;
clock affine identification; and all places where (H) is consumed.
No experiment, numerical training, formal verification, or independent
acceptance review was performed. Original reports and the shared Git
index were not changed.

Source SHA-256 values used:

| Source | SHA-256 |
|---|---|
| P2_CONTINUATION.md | `fe59ffe02281be549d6d7815d9c3b58bfe9b51545236cbffb9899339838669d2` |
| P2_VARIATION.md | `ef28df6745758adc1c587a4d73442c3a49db575026ac2bee86708a24de44c5fd` |
| P2_REFERENCE_COMPARISON.md, updated 227-line version | `869415030167bf422c5a0a5fad05cd35fafc5bbe5221e40968e8ae4db4cafba3` |
| P2_REACHED_TAILS.md | `837535f363d8140516ed993698f0e48d183dc029fe66cffc1277aff79e328716` |
| P1_SECTION.md | `33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38` |
| P1_DEPENDENCIES.md | `ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79` |
| docs/global_nonlinear.md | `3f32122dea7915e25e4abc7abe9d74017d535badfa5abbe1939e84fe2b100bdf` |

Shared instructions were reread and their hashes were unchanged from the
frozen continuation report. The evidence-ledger skill reference was read
for this mature comparison, in addition to the already applied rigorous
math and conjecture-investigation instructions. The original scientific
source coverage is recorded in the frozen report; the three newly
authorized P2 reports were read completely. There was no external
scientific retrieval and no additional scientific dependency.
