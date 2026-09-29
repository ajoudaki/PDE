# Gaussian source transport: a uniform-width convergence theorem and the endpoint bridge

Scoped analytic attempt, 28 September 2026. The mathematical skill
`solve-math-rigorously` was applied. Inputs were `OLD_CLOCK_ROUTE.md`,
`ENERGY_STABILITY_ROUTE.md`, `LEARNED_GATE_RESTORATION.md`, the setting,
closure and old-clock proof in `paper/main.tex`, `docs/notation.qmd`, and
the maintained Gaussian-program and local-population proof units specified
below. No other study, sibling report, experiment or literature search was
used. This is a candidate study result, not a promoted theorem.

**Outcome.** There is an unconditional local, arbitrary-fixed-depth theorem
of convergence of the original autonomous closure, uniform over *all finite
widths in probability*. It uses finite Gaussian programs as reference paths;
it does not require a tail theorem for actual trained finite networks. The
same argument works on a prescribed longer interval if the actual dense
population flow has uniform Gaussian carrier tails. A precise sufficient
dense-only condition is an exact Gaussian-source representation with uniformly
bounded response-row total variation. Ordinary strong population regularity
alone does not establish that additional condition. The quantitative result
with width taken first is `P^-1 exp(C sqrt(log P))`; an all-width `C/P` bound
is not proved.

**Post-freeze synthesis.** Section 7, added after authorization to read
`GENERAL_REFERENCE_PROJECTION.md` and `GENERAL_GEOMETRIC_STABILITY.md`,
improves the width-first rate to `C/P`. Gaussian reference tails and bounded
dense velocity already imply the half-Hölder source regularity needed by
that projection argument; no additional bounded-variation premise remains.
The endpoint is unconditional locally and conditional only on the explicit
dense tail premise (10) on a prescribed longer interval. The all-width
statement remains qualitative (2).

## 1. Maintained inputs and their exact scope

The proof uses the following complete proof units, with the same Gaussian
initialization, tanh activation, finite arbitrary data and canonical mobilities.

1. `docs/03-local-population.qmd`, C.1, lines 56--555: a local fixed-depth
   strong canonical population flow, every-vanishing-step finite approximation,
   its one-reference cutoff estimate, and its fixed-mesh same-array oracle
   comparison. The dataset Gram may be singular. Its state uses hidden
   operator norm; the rank-one estimates used below also hold in Frobenius
   or Hilbert--Schmidt norm for *differences of learned increments*.
2. The same chapter, C.2, lines 556--1049: mesh-uniform local sub-Gaussian
   population backward carriers, obtained from causal named-source response
   bounds. Its deterministic coefficients and covariance laws are frozen
   when taking source derivatives. The theorem is local, not arbitrary-time.
3. `docs/02-gaussian-reuse.qmd`, A.1--A.2, lines 1803--1834: fixed finite
   Gaussian programs preserve the joint values, second moments and both
   directions of every reused initialized matrix. The named-source derivative
   specialization freezes deterministic coefficients. The fixed-program
   result does not supply a growing-transcript concentration rate.
4. `OLD_CLOCK_ROUTE.md`, Section 1: for every finite width and every order,
   the original autonomous tanh closure exists through each finite horizon,
   satisfies uniform physical RMS/operator bounds on initialized-operator
   events, and has actual accumulated velocity defect at most `C/P`.
5. `paper/main.tex`, old-clock theorem and proof: at each fixed width and
   every finite realized initialization, its trajectory error is at most
   a finite initialization-dependent constant divided by `P` for all orders.

The cutoff inequality used below can also be read directly from C.1,
equations with stable identifiers `eq-docs-global-nonlinear-l2701`,
`eq-docs-global-nonlinear-l2724`, and its finite oracle comparison
`eq-docs-global-nonlinear-l2815`. The proof here retains the order of
limits in that comparison.

## 2. The completed uniform-width statement

For each width, couple the dense flow and every closure order using the same
initial arrays. Write their paths as `theta_n` and `theta_hat_(n,P)` and set

\[
 d_n(\theta,\vartheta)=
 \frac{\|W^{(1)}-V^{(1)}\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|W^{(\ell)}-V^{(\ell)}\|_F
 +\frac{\|w-v\|_2}{\sqrt n},
 \qquad e_{n,P}=\sup_{t\le T}d_n(\widehat\theta_{n,P}(t),\theta_n(t)).
 \tag{1}
\]

Hidden differences in (1) are learned differences: their common initialized
matrix cancels. We never compare an initialized finite matrix in Frobenius
norm with a population Gaussian action.

**Theorem.** Let `T<=T_*`, where `T_*` is the deterministic local interval
of maintained C.1--C.2 for the fixed data and depth. For every `epsilon>0`,

\[
 \lim_{P_0\to\infty}\ \sup_{n\ge1}
 \mathbb P\left\{\sup_{P\ge P_0}e_{n,P}>\epsilon\right\}=0.
 \tag{2}
\]

The supremum over orders is over positive integers, so this is a measurable
event. In particular every deterministic sequence `P_j->infinity`, with
arbitrary widths `n_j`, has `e_(n_j,P_j)->0` in probability.

There are deterministic `C_1,C_2` depending on this interval, data and depth
such that, with

\[
 B(P_0)=\frac{C_1}{P_0}
             \exp\!\bigl(C_2\sqrt{\log(e+P_0)}\bigr),
 \tag{3}
\]

for every fixed `P_0` and every `zeta>0`,

\[
 \lim_{n\to\infty}
 \mathbb P\left\{\sup_{P\ge P_0}e_{n,P}>B(P_0)+\zeta\right\}=0.
 \tag{4}
\]

Thus the width-first bound has every exponent strictly below one. Neither
(2) nor (4) asserts `sup_n E e_(n,P)^2 <= C/P^2`, a uniform high-probability
`C/P` rate, or a common deterministic pathwise constant across widths.

The same conclusions hold on a prescribed finite `[0,T]` under the
dense-only hypotheses of Section 4 below. Their local verification is
unconditional by C.1--C.2.

## 3. Proof using a fixed Gaussian reference program

### 3.1. The uniform comparison estimate

On events where initialized hidden operator norms and the initial readout
RMS are bounded by fixed constants, the old-clock result gives constants
independent of width and order with

\[
 \dot{\widehat\theta}_{n,P}=F_n(\widehat\theta_{n,P})+E_{n,P},
 \qquad \int_0^T\sum_{\ell=2}^L\|E_{n,P,\ell}(t)\|_Fdt\le C/P.
 \tag{5}
\]

Both paths have uniformly bounded hidden operators, readout RMS, backward
RMS and first-layer row RMS on this interval. For dense GF, the analogous
bounds follow either from its exact history equations or from the same
physical estimates with zero projection error. Gaussian initialization
makes these initialized bounds hold with probability tending to one for
suitable fixed constants. All closure bounds hold simultaneously in `P`.

For two finite states on such a physical ball, let `c_(l,a)` be the full
backward carrier of the second, reference state: `c_L=w` and
`c_l=W_(l+1)^T delta_(l+1)`. Define its empirical RMS cutoff tail by

\[
 \mathcal T_R(\vartheta)=
 \sum_{\ell=1}^L\max_a
 \frac{\|c_{\ell,a}(\vartheta)
       \mathbf1_{\{|c_{\ell,a}(\vartheta)|>R\}}\|_2}{\sqrt n}.
\]

For `R>=1`, one-reference subtraction gives

\[
 \|F_n(\theta)-F_n(\vartheta)\|_{\rm sum}
 \le C(1+R)d_n(\theta,\vartheta)+C\mathcal T_R(\vartheta).
 \tag{6}
\]

Here the norm on velocities is the sum norm in (1). To check the stronger
hidden Frobenius conclusion rather than just the book's operator-norm
version, expand every hidden velocity into rank-one differences and use

\[
 \left\|\frac{uv^T-u'v'^T}{n}\right\|_F
 \le\frac{\|u-u'\|_2}{\sqrt n}\frac{\|v\|_2}{\sqrt n}
    +\frac{\|u'\|_2}{\sqrt n}\frac{\|v-v'\|_2}{\sqrt n}.
\]

The forward difference estimates use an operator difference bounded by its
Frobenius norm. The first-layer velocity is a sum of response vectors times
the fixed input rows, so its row-RMS estimate uses only the input norm bound,
with no inverse input Gram. Backward subtraction applies

\[
 \|[\tanh'(z)-\tanh'(z')]c'\|_2/\sqrt n
 \le 2R\|z-z'\|_2/\sqrt n
       +\|c'\mathbf1_{|c'|>R}\|_2/\sqrt n.
\]

At every descending layer the previously obtained difference is multiplied
only by a bounded operator and bounded gate. The new cutoff term is added.
This proves (6) with one power of `R`, at arbitrary fixed depth.

Fix a coarse population Euler mesh `Delta` and construct the C.1 finite
oracle using the actual initialized arrays. All residuals and scalar
contractions in its expanded actions are replaced by their deterministic
population Euler values. Reconstruct its proxy parameters from the resulting
first-layer/readout nodes and finite sums of rank-one increments. Denote its
affine interpolant by `vartheta_n^Delta`.

At each fixed mesh this is one fixed finite computation. A.1--A.2 and the
proxy calculation in C.1 give joint empirical second-moment convergence
of every needed node and cutoff, and consistency of its recomputed vector
field. A typical contraction discrepancy in a hidden block has the form

\[
 u_n\left(\frac{v_n^Tw_n}{n}-\mathbb E[VW]\right),
\]

whose RMS tends to zero; rank-one discrepancies have the corresponding
Frobenius bound above. Consequently its assigned grid velocity differs
from `F_n` at its proxy grid state by `o_Pr(1)`, uniformly over its finitely
many cells. Its interpolation speed stays bounded uniformly in `Delta`
in the limiting sense required here. Initial proxy distance from the finite
initial state tends to zero: use the same Gaussian first and hidden arrays,
and either retain the small readout root or add its vanishing normalized
RMS as an initialization error.

For local `T`, the limiting upper bound on each reference grid tail is
`C exp(-c R^2)`, uniformly in mesh, by C.2 and the proxy consistency in C.1.
Using (6) against the preceding *proxy grid state* yields

\[
 \sup_{t\le T}d_n(\widehat\theta_{n,P}(t),\vartheta_n^\Delta(t))
 \le C e^{C(1+R)T}
 \left[P^{-1}+(1+R)\Delta+e^{-cR^2}+o_{\mathbb P}(1)\right].
 \tag{7}
\]

The small term is at fixed `R,Delta`. It depends on the proxy and initial
arrays, not on `P`. To verify (7), the closure satisfies its actual forced
equation (5), the proxy has its assigned piecewise constant velocity, the
reference grid state differs from its interpolant by `O(Delta)`, and (6)
bounds the difference of those two vector fields. Integrating and applying
the scalar integrating factor gives (7). No derivative of a closure response
and no empirical tail of a closure or actual dense carrier is used.

The same calculation for finite dense GF removes the term `P^-1`. A triangle
inequality therefore gives, simultaneously for all `P>=P_0`,

\[
 \sup_{P\ge P_0}e_{n,P}
 \le C e^{C(1+R)T}
 \left[P_0^{-1}+(1+R)\Delta+e^{-cR^2}+o_{\mathbb P}(1)\right].
 \tag{8}
\]

This is the central estimate. The initialization event and all proxy errors
are independent of order, which is essential for its supremum.

### 3.2. The quantifiers and the two conclusions

In (8), first take `n->infinity` at fixed `R,Delta`; next take `Delta->0`.
For any fixed `P_0`, choose
`R=max(1,sqrt(c^-1 log(e+P_0)))`, increasing harmless constants if needed.
Then `exp(-c R^2)<=C/P_0`, and (8) proves (3)--(4).

For (2), fix `epsilon>0` and an arbitrary probability tolerance `q>0`.
First fix `R` large enough that the tail term in (8) is less than
`epsilon/4`; this is possible because `exp(CR T-cR^2)->0`. Next fix a
mesh small enough that its term is less than `epsilon/4`. At these fixed
values, choose `N` so that for every `n>=N` the initialization/proxy good
event has probability at least `1-q` and its small error contributes at
most `epsilon/4`. Finally choose `P_0` large enough to make the first term
less than `epsilon/4`. This proves

\[
 \sup_{n\ge N}\mathbb P\{\sup_{P\ge P_0}e_{n,P}>\epsilon\}\le q.
 \tag{9}
\]

For each of the finitely many widths `n<N`, the manuscript's deterministic
fixed-width theorem, with globally bounded tanh and its derivative, gives
a finite random `H_n` such that `e_(n,P)<=H_n/P` for every order. Thus
`Pr{sup_(P>=P_0)e_(n,P)>epsilon}<=Pr{H_n>epsilon P_0}->0`.
Enlarge `P_0` to handle this finite list. The full supremum over widths is
then at most `q`. Sending `q` to zero proves (2).

The treatment of finitely many widths supplies no bound on their constants
as `N` changes with `epsilon,q`. This is exactly why this last argument
proves qualitative uniform convergence but not a quantitative uniform rate.

Forward recursion transfers these results to predictions on any fixed
bounded input set. For a population prediction conclusion one also takes
`n->infinity`; the same proxy proof identifies the dense finite predictor
with the canonical population predictor. These operations do not interchange
an infinite training-time limit with width or memory order.

## 4. Extension to a prescribed horizon using only dense population regularity

Here is a sufficient whole-horizon premise stated entirely at the population
level. It does not assume closure stability or finite trained tails.

**Dense premise on `[0,T]`.** On the canonical Gaussian action spaces there
exists a strong dense solution from the prescribed zero limiting readout,
and its full backward carriers satisfy

\[
 \sup_{t\le T}\max_{\ell,a}
 \mathbb E_\ell\exp(c_T|c_{\ell,a}^D(t)|^2)\le C_T
 \quad\hbox{for some }c_T>0, C_T<\infty.
 \tag{10}
\]

Strong means the first-row and readout equations hold continuously in `L2`
and the hidden equations in operator norm. The rank-one right side is also
continuous in Hilbert--Schmidt norm: bounded gates times an `L2`-convergent
reference field converge in `L2` by truncation, and rank-one Hilbert--Schmidt
norms are products of field norms. Thus learned increments are continuously
differentiable in the stronger difference topology used in (1). Physical
norms are bounded on the compact interval.

No uniform mesh response bound is an additional requirement in this premise.
Indeed, population Euler paths converge to this given solution using (6)
against the actual dense reference. Stop Euler paths on a ball one unit
larger than the dense path. Up to that stop, interpolant and grid distance
is `O(Delta)`. The comparison gives

\[
 \sup_{t\le T}d(\theta^\Delta(t),\theta^D(t))
 \le C e^{C(1+R)T}[(1+R)\Delta+e^{-cR^2}].
 \tag{11}
\]

At each fixed `R` let `Delta->0`, then let `R->infinity`; the right side
tends to zero in that order. It also rules out the stopped exit for all
sufficiently fine meshes. This proves strong Euler convergence. Uniform
continuity of the network operations along the compact limiting path gives
uniform `L2` convergence of its recomputed backward carriers. More
explicitly, use a carrier cutoff first, the strong state convergence next,
and then the fixed reference's uniform tail bound (10).

If `q_Delta` is the maximum `L2` discrepancy between Euler and dense carriers,
then `q_Delta->0`, and

\[
 \|c^\Delta\mathbf1_{|c^\Delta|>2R}\|_2
 \le2q_\Delta+2\|c^D\mathbf1_{|c^D|>R}\|_2.
 \tag{12}
\]

Consequently the coarse oracle proof of (8) now has one additional term
`q_Delta`, independent of `n,P`. Its limit vanishes with `Delta`, after
the fixed-program width passage. All conclusions (2)--(4) follow on `[0,T]`.

### A precise bounded-source-response condition implying (10)

For each initialized backward branch, suppose the *actual dense population
law* has the representation

\[
 k_{\ell,a}^D(t):=(W_0^{(\ell+1)})^*\Delta_{\ell+1,a}^D(t)
 =\eta_{\ell+1,a}(t)
   +\sum_b\int_{[0,t]} H_{\ell,b}^D(s),
                          \mu_{\ell+1;a,t,b}(ds),\qquad\ell<L.
 \tag{13}
\]

The measures are deterministic signed source-response measures, including
possible current-time atoms. Assume

\[
 \sup_{\ell,a,t\le T}\sum_b
            |\mu_{\ell+1;a,t,b}|([0,t])\le A_T<\infty.
 \tag{14}
\]

The centered Gaussian field `eta` has the canonical covariance

\[
 \mathbb E[\eta_{\ell+1,a}(t)\eta_{\ell+1,b}(s)]
   =\mathbb E_{\ell+1}
      [\Delta_{\ell+1,a}^D(t)\Delta_{\ell+1,b}^D(s)].
 \tag{15}
\]

All Gaussian variances are therefore bounded by the already bounded dense
backward `L2` norms. The fields on the right of (13) can be dependent; no
independence assertion is needed. Because tanh features have absolute value
at most one, the non-Gaussian remainder in (13) has absolute value at most
`A_T`. Therefore every initialized carrier is a Gaussian variable of bounded
variance plus a bounded random variable. The inequality
`(eta+b)^2<=2 eta^2+2 A_T^2` and the elementary Gaussian exponential-square
integral give a common positive exponential-square parameter.

The learned carrier is bounded pointwise by the exact history identity:

\[
 \|(W^{(\ell+1),D}(t)-W_0^{(\ell+1)})^*
                  \Delta_{\ell+1,a}^D(t)\|_\infty
 \le2\left(\int_0^T\rho_D(s)ds\right)
           \sup_{s,a}\|\Delta_{\ell+1,a}^D(s)\|_2^2.
\]

The top readout is bounded pointwise by `2 integral rho_D` because its
population initial value is zero. Adding these bounded terms proves (10).

Equations (13)--(15) are thus a sufficient *dense Gaussian source regularity*
condition for the arbitrary-horizon version of (2). In a discrete source
program, (14) is exactly a uniform bound on the absolute row sums of the
expected forward-slot derivatives in C.2, multiplied by the initialized
variance. If it is supplied uniformly on a mesh approximation converging to
the dense law, the sub-Gaussian tails pass to the dense solution by Fatou;
there is no need to identify a unique limiting signed measure. Alternatively
an independently established continuous source representation (13) suffices
directly.

C.2 verifies the required source bounds locally by a coupled first-exit
construction. It does not continue them to arbitrary `T`. Strong `L2`
continuity, smooth physical time dependence or ordinary bounded parameter
operator norms do not state (14), and cannot silently be substituted for it.
The conditional whole-horizon theorem therefore has a precise additional
dense-only hypothesis, rather than an unproved finite-network stability
premise.

## 5. Gaussian source differentiation gives a sharper product estimate

There is also a nontrivial estimate that retains the correlation of a
perturbation with its Gaussian source. It identifies what an endpoint proof
using source smoothness would need.

Let `g` be a standard Gaussian vector, let `e` be a deterministic unit vector,
and let `G=sigma e·g`. For every Gaussian Sobolev function `u` with `u` and
its directional weak derivative `D_e u` in `L2`,

\[
 \|Gu\|_2\le\sigma\|u\|_2+2\sigma\|D_eu\|_2.
 \tag{16}
\]

For a smooth compactly supported function, Gaussian integration by parts in
direction `e` gives, with `z=e·g`,

\[
 \mathbb E[z^2u^2]=\mathbb E[u^2]+2\mathbb E[z u D_eu].
\]

Writing `x=||zu||_2`, `a=||u||_2`, `b=||D_eu||_2`, Cauchy--Schwarz gives
`x^2<=a^2+2xb`, hence `x<=b+sqrt(a^2+b^2)<=a+2b`. Smooth approximation
extends this estimate to the directional Sobolev domain: the estimate makes
the products of approximants Cauchy in `L2`, and almost-everywhere
subsequences identify their limit with `zu`. Scaling proves (16).
Degenerate correlated Gaussian arrays are treated by writing them as
deterministic linear images of a standard Gaussian vector; no inverse
covariance is used. The zero-variance case is immediate.

If a dense carrier has the source representation `k=G+b`, `|b|<=A`, then
for a preactivation discrepancy `v`, tanh's gate satisfies

\[
 \|[\tanh'(Z+v)-\tanh'(Z)]k\|_2
 \le2(A+\sigma)\|v\|_2+4\sigma\|D_ev\|_2.
 \tag{17}
\]

Indeed use the pointwise Lipschitz bound by `2|v|`, split `k`, and apply
(16) to `v`. This does not differentiate the reference gate and does not
require `v` to be independent of `G`. It replaces the unavailable essential
supremum by one specific source-direction derivative of the *actual error*.

This is a stronger statement than the generic carrier-tail modulus. However,
the book's bounded expected response coefficients do not supply a bound on
`D_e v` proportional to the memory error. Their derivatives freeze scalar
residuals, contractions and covariance laws; the actual finite-width
derivative also differentiates those quantities. Differentiating the full
error dynamics introduces second derivatives of the source-dependent error
when (16) is reused, so a first-order source norm is not automatically closed.

For a deterministic clock, source differentiation does commute with the
Legendre projection. For Hilbert-valued histories `b,h`, put
`r_b=(I-Pi_P)b`, `r_h=(I-Pi_P)h` and
`R=int r_b tensor r_h`. Whenever the displayed source derivatives exist,

\[
 D_eR=\int (I-\Pi_P)D_eb\otimes r_h
             +r_b\otimes(I-\Pi_P)D_eh,
\]

\[
 \|D_eR\|_{\rm HS}
 \le\|(I-\Pi_P)D_eb\|_{L^2_tL^2}
                           \|r_h\|_{L^2_tL^2}
    +\|r_b\|_{L^2_tL^2}
                           \|(I-\Pi_P)D_eh\|_{L^2_tL^2}.
 \tag{18}
\]

Thus source-derivative history bounds would preserve projection smallness
by the same product cancellation. They are additional estimates to prove,
not a consequence of the undifferentiated forward derivative energy.
In the actual finite closure the clock is a scalar function of the entire
Gaussian initialization. Its derivative is
`D tau(t)=int_0^t D rho(s) ds`, so source differentiation at fixed physical
time also differentiates the moving projection interval and polynomial
arguments. The frozen-coefficient population source calculation omits
exactly these finite scalar-feedback and clock terms. A leave-one-out or
Malliavin transfer must control them; replacing the reused matrix by a fresh
independent Gaussian would delete them rather than estimate them.

## 6. Endpoint status and the next exact bridge

The completed theorem is qualitative uniform convergence (2), with the
width-first quantitative statement (4). It is already about the original
autonomous closure and arbitrary fixed correlated data and depth. Its
unconditional horizon is local; the prescribed-horizon extension follows
from the explicit dense source regularity (13)--(15), or directly (10).

There are two distinct remaining ways to reach a constant-times-`P^-1`
conclusion. One may prove a closed source-derivative estimate for the actual
memory perturbation, including finite scalar feedback and clock transport,
and then use (17)--(18). Alternatively, stronger dense-history reprojection
consistency of order `P^-q`, `q>1`, combined with an appropriate comparison
could absorb the factor `exp(C sqrt(log P))` in the width-first estimate.
That second route must prove its improved forcing estimate and preserve the
finite-width quantifiers; a width-first tail bound alone is insufficient
to give a quantitative supremum over every finite width. No endpoint
`C/P` theorem is asserted in the preceding independent analysis. The
following authorized synthesis improves this width-first conclusion.

## 7. Post-freeze synthesis: the endpoint with width taken first

This section uses the reference-history identity and absorbable remainder
in `GENERAL_REFERENCE_PROJECTION.md`, Sections 2--5, and the actual closure
residual-floor argument in `GENERAL_GEOMETRIC_STABILITY.md`, Section 3.1.
It supplies the necessary time regularity and the finite-reference transfer.
All constants depend on the fixed horizon, data, depth and the stated dense
and initialization bounds. It supersedes only the width-first endpoint
boundary in Section 6.

### 7.1. Dense tails give half-Hölder backward sources

Assume the strong dense solution and (10), and put
`a_(l,a)^D=r_a^D Delta_(l,a)^D`. The rank-one equations and bounded response
norms bound the dense velocity in the sum parameter norm. Therefore

\[
 d(\theta^D(t),\theta^D(s))\le C|t-s|.
 \tag{19}
\]

Apply the backward subtraction behind (6) to these two times, then use
the predictor Lipschitz bound for the residual factor. For every `R>=1`,

\[
 \|a_{\ell,a}^D(t)-a_{\ell,a}^D(s)\|_2
 \le C[(1+R)|t-s|+e^{-cR^2}].
 \tag{20}
\]

For `h=|t-s|<=1/2`, choose `R` proportional to
`sqrt(log(e/h))`, making the tail at most `h`. Since
`h sqrt(log(e/h))<=C sqrt(h)`,

\[
 \|a_{\ell,a}^D(t)-a_{\ell,a}^D(s)\|_2\le C|t-s|^{1/2}.
 \tag{21}
\]

For larger separations bounded source norms give the same result with
a larger constant. Every Hölder exponent strictly below one is in fact
available. This argument never differentiates a backward product.
The forward dense histories are Lipschitz in `L2` by the forward recursion
and (19), hence have uniformly bounded `H1` time seminorms.

Here is the needed Hilbert-valued projection fact. If
`||q(t)-q(s)||<=K|t-s|^alpha`, `0<alpha<=1`, on `[0,A]`, its linear
interpolant `q_J` on `J` equal cells satisfies

\[
 \|q-q_J\|_{L^2}\le CKA^{\alpha+1/2}J^{-\alpha},
 \qquad
 \|q_J'\|_{L^2}\le KA^{\alpha-1/2}J^{1-\alpha}.
\]

The first follows by bounding the interpolation error on each cell; the
second follows from the difference quotient on that cell. Projection
contraction and the Legendre `H1` estimate, with `J=P`, now prove

\[
 \|(I-\Pi_P)q\|_{L^2(0,A;H)}
       \le CKA^{\alpha+1/2}P^{-\alpha}.
 \tag{22}
\]

Constants are annihilated by `I-Pi_P`. A bounded jump at the prefix adds
`C P^-1/2` by the scalar step estimate in the reference-projection report.
Thus half-Hölder regularity on the non-prefix interval gives precisely
the backward-history projection order needed there, without variation or
derivative bounds on that history.

### 7.2. The actual clock preserves the estimate

First suppose the fixed label RMS `Y` is positive. With probability tending
to one, the actual initial residual is at least `Y/2`. The geometric-route
calculation, applied to the actual closure and (5), gives

\[
 \widehat\rho(t)\ge\widehat\rho(0)e^{-2J^2T}
                         -J C_{\rm comp}/P.
\]

Here `J` is a uniform bound for the predictor differential in the mobility
metric on the already established physical bounds. Consequently there are
deterministic `P_*` and `mu>0` such that, on one initialization event
independent of order and of probability tending to one,

\[
 \inf_{t\le T}\widehat\rho_{n,P}(t)\ge\mu
                     \quad\text{for every }P\ge P_*.
 \tag{23}
\]

This uses consistency, not trajectory comparison. Also the old squared-
defect estimate and the predictor differential bound give

\[
 \int_0^T\|E_{n,P}(t)\|_{\rm sum}^2dt\le C,
 \qquad
 \int_0^T|\dot{\widehat\rho}_{n,P}(t)|^2dt\le C.
 \tag{24}
\]

For the first bound multiply the proved
`integral ||E_l||_F^2/rho_hat` bound by `rho_hat<=Q` and sum over the
fixed number of layers. For the second use the bounded predictor
differential and `dot theta_hat=F+E`, with bounded `F`. The derivative
of the sample residual norm is bounded by its sample RMS derivative.

Thus `rho_hat` is uniformly half-Hölder in physical time. Its lower bound
makes the inverse clock Lipschitz. The scalar quotient inequality and
(21) imply that

\[
 B_{\ell,a}(\xi)
  =a_{\ell,a}^D(t(\xi))/\widehat\rho(t(\xi)),\qquad\xi>1,
\]

is half-Hölder in `L2`, uniformly in order, with its zero prefix. The
reference forward history in the same clock has a uniform `H1` seminorm.
Therefore

\[
 \|(I-\Pi_P)H_{\ell-1,a}\|_{L^2_\xi L^2}\le C/P,
 \qquad
 \|(I-\Pi_P)B_{\ell,a}\|_{L^2_\xi L^2}\le C/P^{1/2}.
 \tag{25}
\]

The reference-projection report's exact identity (22) and estimates
(23)--(25) now apply with (25) in place of its variation estimate. On a
common population carrier, whenever the autonomous population closure
exists, they give for `D(t)=sup_(s<=t)d(theta_hat(s),theta_D(s))`

\[
 D(t)\le CP^{-3/2}+CP^{-1/2}D(t)
           +C\int_0^t[(1+R)D(s)+e^{-cR^2}]ds.
 \tag{26}
\]

Absorb the second term at large order and apply the scalar integrating
factor. Choosing `R` proportional to `sqrt(log(e+P))` so that
`exp(-cR^2)<=P^-3/2` yields

\[
 D(T)\le CP^{-3/2}e^{C_T\sqrt{\log(e+P)}}\le C_T/P.
 \tag{27}
\]

The last inequality uses the finite supremum of
`C_T sqrt(log(e+P))-(1/2)log P` over `P>=1`. This is an a priori
population comparison, not a population-closure existence assertion.
The next construction concerns the already existing actual finite closure.

### 7.3. Two finite meshes transfer regular histories without trained tails

Choose a coarse **history mesh** `h` and sample the true dense forward
histories `H_j`, backward sources `a_j`, and readout sources
`U_j=r^D(t_j)H_L^D(t_j)` at its finitely many nodes. Linear interpolation
preserves `|H|<=1` and has forward `H1` seminorm bounded by that of the
dense history: on each cell, Jensen bounds the squared difference quotient
by the cell average of the squared derivative. Interpolation also preserves
the half-Hölder source bound up to a universal constant. Within one cell
use `h^-1/2|t-s|<=sqrt(|t-s|)`; across neighboring cells use the sum of
the two square roots; across separated cells use the endpoint Hölder bound
and the two endpoint interpolation errors.

Approximate this finite list of nodes by canonical population Euler
programs with a finer **program mesh** `Delta`. Equations (11) and the
backward continuity argument show that node errors tend to zero as
`Delta->0` at fixed `h`. The oracle may use the exact deterministic dense
residuals at the nodes: these are fixed scalar coefficients. Evaluate the
finite programs on the same actual initialized arrays at width `n`.
A.1--A.2 and C.1's finite-rank proxy recomputation transfer their joint
second moments at fixed `h,Delta` as `n->infinity`.

The temporal bounds are finite-list observations. The forward derivative
energy is exactly
`sum_j ||H_(j+1)-H_j||_2^2/(t_(j+1)-t_j)`, whose finite empirical value
converges. A node error at most `epsilon` changes the half-Hölder seminorm
of its linear interpolant by at most `C epsilon/sqrt(h)`. Choosing the
program approximation sufficiently fine at each fixed `h`, then width
sufficiently large, makes the history constants uniformly bounded.
This is a transfer of sampled moments, not a claim about trained finite
derivatives or tails.

From these prescribed interpolated histories construct finite reference
parameters

\[
 \begin{split}
 W_1^R(t)&=W_{0,1}-\frac2m\sum_a\int_0^t a_{1,a}^{h,\Delta,n}(s)
                                      x_a^T/\sqrt d\,ds,\\
 W_\ell^R(t)&=W_{0,\ell}-\frac2m\sum_a\int_0^t
             a_{\ell,a}^{h,\Delta,n}(s)\otimes
             H_{\ell-1,a}^{h,\Delta,n}(s)\,ds,\\
 w^R(t)&=-\frac2m\sum_a\int_0^t U_a^{h,\Delta,n}(s)ds.
 \end{split}
 \tag{28}
\]

Finite tensors are `uv^T/n`. The zero proxy readout contributes only the
vanishing initial distance `||w_0||_2/sqrt(n)`; the initialized forward
prefix agrees exactly since it does not use the readout. These paths have
uniform physical bounds and bounded speed. Their hidden history identity
is exact for the prescribed sources in (28), and their learned adjoint
outputs are pointwise bounded by that identity because the prescribed
forward coordinates are bounded.

In the population, as `Delta->0` at fixed `h`, then `h->0`, (28) converges
uniformly in the sum parameter norm to the actual dense path: the source
interpolants converge uniformly and their rank-one products converge in
Hilbert--Schmidt norm. Its recomputed responses therefore converge uniformly
in `L2` by compact-path continuity. In particular at the finitely many
history nodes, tail transfer gives

\[
 \mathcal T_R(\theta^R(t_j))
       \le Ce^{-cR^2}+q_h+q_{h,\Delta},
 \tag{29}
\]

where `q_h->0` and `q_(h,Delta)->0` for fixed `h`. Its finite same-array
version gains `o_Pr(1)` at fixed `h,Delta,R`; the same convergence controls
the algebraic discrepancies between prescribed and recomputed responses.
The C.1 finite-rank proxy argument handles the recomputed fields, so this
step does not require an unproved finite scalar-feedback response theorem.

These node tails suffice. At a physical time within a history cell compare
the actual closure with the reference at the preceding node. Their
parameter distance is at most `D(t)+Ch`. Apply the one-reference source
estimate there. Prescribed source interpolation moves by at most
`C sqrt(h)` on that cell; forward interpolation has the same bound from
its `H1` seminorm. Node algebraic discrepancies contribute
`q_h+q_(h,Delta)+o_Pr(1)`.

For the hidden reconstruction use the exact splitting in the reference-
projection report with these prescribed histories. The first term is the
integral of the source discrepancy times the uniformly bounded projected
actual forward history. The second uses the forward discrepancy. The last
term is bounded by `C P^-1/2` times its `L2` forward discrepancy, which is
at most a constant times `D(t)` plus the same reference mismatch. Initial
row/readout discrepancies and their integral source mismatches are included
additively. This proves the concrete finite inequality

\[
 \begin{split}
 D_{n,P}(t)\le{}&CP^{-3/2}+CP^{-1/2}D_{n,P}(t)
                    +C\varepsilon_{n,h,\Delta,R}\\
   &+C\int_0^t[(1+R)D_{n,P}(s)+e^{-cR^2}]ds,
 \end{split}
 \tag{30}
\]

where `D_(n,P)` compares the closure with (28), and one may take

\[
 \varepsilon_{n,h,\Delta,R}
       =C(1+R)\sqrt h+q_h+q_{h,\Delta}+o_{\mathbb P}(1).
 \tag{31}
\]

The final term includes finite node errors and the initial small readout;
it is at fixed meshes and cutoff and is independent of `P`. Errors
multiplied by `P^-1/2` are also covered since `P>=1`. The reference
backward quotient by the actual closure residual has the uniform
half-Hölder bound from (23)--(24), so its projection constants in (30)
are independent of the order, widths and meshes on the stated events.

For completeness, comparison of actual dense finite GF with (28) uses the
same node cutoffs and algebraic source discrepancies. Its integral
equations have no memory projection error; hence the result is the same
bound with the terms involving `P` removed. No empirical tail of finite
dense GF between the nodes is needed. After absorption and a triangle
inequality, simultaneously for all orders above a fixed threshold,

\[
 \sup_{P\ge P_0}e_{n,P}
 \le Ce^{C(1+R)T}
       [P_0^{-3/2}+e^{-cR^2}+\varepsilon_{n,h,\Delta,R}].
 \tag{32}
\]

Take width to infinity at fixed meshes and cutoff; take the program mesh
to zero at fixed history mesh; then take the history mesh to zero. Choose
`R` as in (27), with `P_0` fixed. This proves

\[
 \forall P_0\ge1,\quad\forall\zeta>0:\qquad
 \lim_{n\to\infty}\mathbb P\left\{
       \sup_{P\ge P_0}e_{n,P}>C_T/P_0+\zeta\right\}=0.
 \tag{33}
\]

Orders below the absorption/residual-floor threshold are covered by
enlarging `C_T`: all physical increments have a uniform bound on the
initialization events of probability tending to one.

When all labels are zero, Section 8 of the reference-projection report
gives the endpoint directly. The actual readout Euclidean norm is
nonincreasing, and every initialized carrier is bounded coordinatewise
by a fixed constant times `||w_0||_2`. Since canonical
`||w_0||_2->0`, direct Lipschitz comparison on these initialization events
gives (33), without a positive residual floor.

The endpoint (33) is consequently unconditional on the maintained local
C.1--C.2 interval for arbitrary fixed depth and arbitrary correlated finite
data. On a longer prescribed interval it follows from a strong dense
solution and (10), which the bounded source-response representation
(13)--(15) implies. No extra source-time smoothness is needed.

The width thresholds for the finite-list approximations have not been
quantified as functions of the two meshes and cutoff. Thus (33) does not
assert a quantitative supremum over all finite widths, or an expectation
bound. Section 3.2 still gives the qualitative all-width statement (2).
If a population-closure existence theorem is separately supplied, its
tracking bound is (27); the finite width-first theorem does not silently
assume that existence or identify a fixed-order population closure limit.

## 8. Scoped verification of the sharper width-first envelope

At the coordinator's request I checked Section 14 of
`GENERAL_REFERENCE_PROJECTION.md`, together with its Section 12 proxy
definitions needed to verify the prefix. **PASS**, within the stated
width-first scope and dense tail premise. This is an internal analytic
check, not an independent promotion review.

The two potentially delicate points check as follows.

1. For `psi(h)=h sqrt(log(eT_1/h))`, concavity and `psi(0)=0` make
   `psi(h)/h` decreasing. The interpolated source increment is bounded
   by `C psi(Delta) h/Delta` for `h<=Delta`, including an increment
   crossing a cell boundary, and by `C psi(h)` for `h>=Delta` using
   adjacent endpoints. These are both at most a constant times `psi(h)`.
   An interpolated nodal error of size `epsilon` has increment at most
   `min(2epsilon,2epsilon h/Delta)`, so its `psi` seminorm is at most
   `2epsilon/psi(Delta)`. Thus `epsilon=Delta^2` gives a uniform source
   modulus. At a fixed mesh the finite empirical bound depends only on
   finitely many node-pair norms divided by fixed positive `psi` values;
   their joint second-moment convergence transfers this bound. The width
   threshold may depend on the mesh, as the claimed quantifiers permit.
2. The prescribed initial source is set to zero exactly, and the prescribed
   forward nodes use the exact common initialized forward pass. Hence the
   clocked source `A` joins its zero prefix continuously at finite width
   too. The physical proxy readout may retain the actual small Gaussian
   root: its residual-weighted backward response then differs from the
   assigned zero initial source, but that is a recomputation mismatch,
   already included in the fixed-program `o_Pr(1)`. It does not become a
   jump in the prescribed history used by the projection identity. This
   distinction is necessary for the claimed sharpening.

The smoothing calculation is also valid. With
`g(xi)=1/rho_hat(t(xi))`, its derivative is
`g'=-dot rho_hat/rho_hat^3`, so the squared clock derivative integral
is exactly `integral |dot rho_hat|^2/rho_hat^5 dt`. The proved residual
floor and squared-defect estimate bound it uniformly. Interpolate only
the `psi`-regular source on `P` clock cells: its `L2` interpolation error
is `O(P^-1 sqrt(log(e+P)))`, its derivative norm is
`O(sqrt(log(e+P)))`, and its `L-infinity` Hilbert norm stays bounded.
The scalar/Hilbert product rule therefore puts `g A_J` in `H1` with
the same derivative order. Projection contraction plus the Legendre
`H1` bound proves the displayed backward tail (72), without requiring
`g` itself to have the stronger `psi` modulus.

Consequently the same reconstruction proof replaces `P^-3/2` by
`P^-2 sqrt(log(e+P))` and its absorbable coefficient by
`P^-1 sqrt(log(e+P))`. The cutoff and ordered-limit argument then yields
the verified width-first envelope

\[
 B_{**}(P)=\frac{C\sqrt{\log(e+P)}}{P^2}
                     \exp(C_T\sqrt{\log(e+P)}).
\]

For every fixed `gamma<2`, its ratio to `P^-gamma` is bounded, since
the negative term `-(2-gamma)log P` dominates the square-root logarithm
and the logarithm of the square root. This verifies every claimed
width-first exponent below two. It does not verify an exact `C/P^2`
rate, a quantitative supremum over widths, or a joint-clock theorem;
the checked section makes none of those claims.
