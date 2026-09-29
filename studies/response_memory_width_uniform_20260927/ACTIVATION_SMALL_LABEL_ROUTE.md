# Small-label autonomous old-clock fitting for unbounded smooth activations

Scoped proof candidate, 28 September 2026. This is a continuation of the
small-label investigation in this study. Scientific inputs were only
`docs/notation.qmd`, the setting and complete old-clock construction/proof in
`paper/main.tex`, and this study's `LOSS_DECAY_ACTIVITY_BOOTSTRAP.md`,
`SMALL_LABEL_SPECTRAL_SLACK.md`, and `SMALL_LABEL_ENERGY.md`. The
`solve-math-rigorously` skill was applied. No experiment, external source,
other study, maintained-file edit, or Git mutation was used. The candidate
is an author derivation; it has not received an independent complete review
and is not promoted material.

The boundedness of the activation can be removed from the small-label,
all-order theorem. Globally bounded slope supplies linear growth and hence
RMS feature bounds on a fixed parameter tube. The tube, the activity budget,
and the feature Gram margin are all proved by a simultaneous bootstrap.
Globally Lipschitz activation derivatives then give the same finite-width
source tail and all-time tracking exponent as in the tanh case. Every history
below is produced by the actual autonomous closure in its own clock.

## 1. Statement and conventions

Use fixed finite depth `L >= 2`, sample count `m`, inputs `x_a in R^d`,
width `n`, scalar output, and the canonical model

\[
 z_a^{(1)}=W^{(1)}x_a/\sqrt d,\qquad
 z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
 h_a^{(\ell)}=\phi^{(\ell)}(z_a^{(\ell)}),\qquad
 f_a=w^Th_a^{(L)}/n.
 \tag{1}
\]

Set `r=f-y`, `rho=||r||_m`, where
`||u||_m^2=m^-1 sum_a u_a^2`. The loss is `rho^2`; block mobilities are
`(n,1,...,1,n)`. The backward responses exclude the residual:

\[
 \delta_a^{(L)}=w\odot(\phi^{(L)})'(z_a^{(L)}),\qquad
 \delta_a^{(\ell)}=(\phi^{(\ell)})'(z_a^{(\ell)})\odot
               (W^{(\ell+1)})^T\delta_a^{(\ell+1)}.
 \tag{2}
\]

Suppose every activation is continuously differentiable and there are finite
constants

\[
 a_\ell=|\phi^{(\ell)}(0)|,\qquad
 \sup_{u\in\mathbb R}|(\phi^{(\ell)})'(u)|\le s_\ell,
 \qquad
 |(\phi^{(\ell)})'(u)-(\phi^{(\ell)})'(v)|\le j_\ell|u-v|.
 \tag{3}
\]

Thus the activations are globally `C^{1,1}`, with globally bounded slope;
the activations themselves may be unbounded. No positivity, monotonicity,
oddness, analyticity, or nonaffinity is assumed. The actual deterministic
initial feature Gram condition below is required even for an activation
class whose random initialization may fail to provide it.

Write

\[
 X=\max_a\|x_a\|_2/\sqrt d,\qquad
 Y=\|y\|_m,\qquad B_0=\|w_0\|_2/\sqrt n.
\]

Fix `K,A_0 < infinity` and `lambda_0>0`, and assume

\[
 \max_{2\le\ell\le L}\|W_0^{(\ell)}\|_{\rm op}\le K,
 \qquad
 \max_a\frac{\|z_a^{(1)}(0)\|_2}{\sqrt n}\le A_0,
 \qquad B_0\le Y,
 \qquad
 \Gamma_w(0):=\frac{H_L(0)^TH_L(0)}{mn}
                         \succeq\lambda_0 I_m.
 \tag{4}
\]

Here `H_L` has columns `h_a^(L)`. An initial first-matrix bound
`||W_0^(1)||_F/sqrt(n)<=A_0` suffices after replacing the preactivation
constant in (4) by `A_0 X`. The preactivation formulation allows large
components of `W_0^(1)` invisible to the training inputs. The initialization
is otherwise arbitrary and finite. In particular, (4) is not a claimed
probabilistic initialization theorem. A full-space gap requires `n>=m`.

Let `theta_D` solve the dense canonical flow and let `theta_hat_P` solve the
original raw old-clock moment closure, both from the same physical initial
parameter, with its usual initial moment prefix. Its clock is
`tau=1+integral_0^t rho_hat`, its forward prefix on `[0,1]` is the initial
feature, and its backward prefix is zero. Its moments of degree below `P`
have physical sources `rho_hat h` and `r_hat_a delta_a`; reconstructed hidden
matrices are exactly

\[
 \widehat W^{(\ell)}=W_0^{(\ell)}-
 \frac{2}{nm\tau}\sum_{a=1}^m\sum_{k<P}(2k+1)
                 \bar b_{\ell,a,k}\bar h_{\ell-1,a,k}^{T}.
 \tag{5}
\]

The first matrix and readout follow the canonical gradient equations,
evaluated in the reconstructed network. Thus the algorithm is autonomous
and has no division by its residual; the normalized backward history
`b_a=(r_a/rho)delta_a` is only an equivalent proof representation on a
nonstationary interval.

**Theorem.** There are `Y_*>0`, `kappa>0`, `Lambda<infinity`, and finite
constants `C`, depending only on `L,m,X,K,A_0,lambda_0` and the activation
constants in (3), such that the following hold whenever `0<Y<=Y_*`.
They hold for every finite width satisfying (4), simultaneously for every
integer `P>=1`. Constants do not depend on `n,P,t,Y` or label direction.

Both the dense flow and the original closure exist uniquely for all
`t>=0`, have finite total parameter variation in the mobility norm, and
converge to finite interpolating parameters. Each has total residual
activity at most `CY`, readout RMS and backward-response RMS at most `CY`,
uniformly bounded hidden operators and feature RMS, and
`Gamma_w(t)>=lambda_0 I_m/2`. Their residuals obey

\[
 \rho_0e^{-\Lambda t}\le\rho(t)\le\rho_0e^{-\kappa t}.
 \tag{6}
\]

For a stationary initial residual, both paths are constant and (6) has
both sides zero. The case `Y=0`, hence `w_0=0`, is likewise stationary.

For the closure, let
`dot theta_hat=F(theta_hat)+E`, with `E_1=E_w=0`, and put
`e_E=sum_(ell=2)^L ||E_ell||_F`. Its forward clock derivative energy satisfies

\[
 Z_\ell(t):=\frac1{mn}\sum_a\int_0^{\tau(t)}
       \|\partial_\xi h_a^{(\ell)}(\xi)\|_2^2d\xi\le CY^3,
 \qquad e_E(t)\le CY^{5/2}\widehat\rho(t).
 \tag{7}
\]

Its actual backward histories have the uniform-in-endpoint tail

\[
 \left[\frac1{mn}\sum_a\int_0^{\tau(t)}
       \|(I-\Pi_P)b_{\ell,a}(\xi)\|_2^2d\xi\right]^{1/2}
 \le C\left\{\frac{B_0}{\sqrt P}
       +\frac{Y\sqrt{1+nY^4+\log(e+P)}}P\right\}.
 \tag{8}
\]

Consequently, either of the following bounds may be used for the total
velocity defect `epsilon_P=integral_0^infinity e_E(t)dt`:

\[
 \varepsilon_P\le\frac{CY^3}{\sqrt{P(P+1)}},
 \qquad
 \varepsilon_P\le C\left\{
     \frac{B_0Y^{3/2}}{P^{3/2}}+
     \frac{Y^{5/2}\sqrt{1+nY^4+\log(e+P)}}{P^2}\right\}.
 \tag{9}
\]

Use the canonical mobility distance

\[
 d_n(\theta,\widetilde\theta)^2=
 \frac{\|W^{(1)}-\widetilde W^{(1)}\|_F^2}{n}
 +\sum_{\ell=2}^L\|W^{(\ell)}-\widetilde W^{(\ell)}\|_F^2
 +\frac{\|w-\widetilde w\|_2^2}{n}.
\]

Then

\[
 \sup_{t\ge0}d_n(\widehat\theta_P(t),\theta_D(t))
       \le C\varepsilon_P\exp\{CY+C\sqrt n\,Y^2\}.
 \tag{10}
\]

The same bound controls the distance between the fitted limits, and
`integral_0^infinity ||f_hat-f_D||_m dt<infinity` at every finite width.
This is an all-time finite-width theorem with explicit width dependence,
not a fixed-label, width-uniform trajectory estimate.

The label threshold `Y_*`, residual exponents `kappa,Lambda`, tube and
activity constants, the forward energy, the relative defect in (7), and
the first estimate in (9), and the physical velocity and forward-speed
bounds (34)--(35) depend only on the values `a_ell,s_ell`, not on
`j_ell`. These conclusions and their proofs in Sections 2--5 and in the
derivation of (35) remain valid
if (3)'s global derivative-Lipschitz condition is replaced by
`phi^(ell) in C^{1,1}_loc(R)`, while the slopes stay globally bounded.
Local derivative regularity is used there only for local uniqueness and
continuation at each finite width. Quantitative derivative Lipschitz
constants first enter the source derivative estimate (36) and the gate
difference estimate (45). Thus the globally Lipschitz derivative assumption
is needed for the width-independent coefficients of (8) and (10) in
their displayed form, not for the all-order small-label fitting bootstrap.

## 2. Projection identities and elementary endpoint estimates

All vector norms in the argument remain ordinary Euclidean norms, with
RMS factors displayed. In particular,

\[
 \|uv^T/n\|_F=(\|u\|_2/\sqrt n)(\|v\|_2/\sqrt n).
 \tag{11}
\]

Let `Pi_P` project onto polynomials of degree below `P` on `[0,tau]`.
For a history `q`, put
`D_q(t)=integral_0^tau ||q-Pi_P q||_2^2` and
`q^*=(Pi_P q)(tau)`. Orthogonality in the least-squares minimization gives

\[
 \dot D_q=\rho\|q-q^*\|_2^2,
 \qquad
 D_q(t)=\int_0^t\rho(s)\|q(s)-q^*(s)\|_2^2ds.
 \tag{12}
\]

To see the derivative, differentiate the integral of the squared error.
The moving endpoint gives the displayed endpoint term; the remaining
term pairs `q-Pi_Pq` against the derivative of a polynomial of degree below
`P` and vanishes. The initial errors are zero because each prefix is
constant and `P>=1`. The backward jump at `xi=1` does not affect this
growing-integral identity, which holds almost everywhere and in integrated
form for square-integrable histories.

Differentiating (5), or using the same orthogonality, gives exactly

\[
 E_\ell=\frac{2\rho}{nm}\sum_a
       (b_{\ell,a}-b_{\ell,a}^*)
       (h_{\ell-1,a}-h_{\ell-1,a}^*)^T,
 \tag{13}
\]
\[
 \int_0^t\|E_\ell\|_Fds
 \le\frac2{mn}\sum_a\sqrt{D_{b,\ell,a}(t)D_{h,\ell-1,a}(t)}.
 \tag{14}
\]

We use three projection inequalities. For every Hilbert-valued
`q in H^1(0,tau)`, with its Hilbert norm denoted only within this paragraph
by `||.||`,

\[
 \|(I-\Pi_P)q\|_{L^2}^2
 \le\frac1{P(P+1)}\int_0^\tau
             \xi(\tau-\xi)\|q'(\xi)\|^2d\xi
 \le\frac{\tau^2}{4P(P+1)}\|q'\|_{L^2}^2,
 \tag{15}
\]
\[
 \|q(\tau)-(\Pi_Pq)(\tau)\|
       \le C\sqrt{\tau/P}\,\|q'\|_{L^2},
 \qquad
 \| (\Pi_P b)(\tau)\|
       \le C\sqrt P\,\|b\|_{L^\infty(0,\tau)}.
 \tag{16}
\]

Here the last inequality only requires a bounded measurable history `b`.
The constants are absolute, also for finite Hilbert direct sums of samples.
For completeness, the following proves the projection facts needed here.

Let `L_j` be the Legendre polynomial on `[-1,1]`, normalized by `L_j(1)=1`,
and write `p_j(u)=L_j(2u-1)`. Its equation
`-(u(1-u)p_j')'=j(j+1)p_j` gives weighted derivative orthogonality.
Bessel applied to the derivative of `q`, followed by Parseval, bounds its
squared tail by `[P(P+1)]^-1 integral_0^1 u(1-u)||q'||^2`. Rescaling proves
(15); vector components can be summed or the argument can be made directly
in a Hilbert space.

The endpoint reproducing kernel on `[0,1]` is

\[
 K_P(u)=\sum_{j<P}(2j+1)p_j(u)
       =\tfrac12\{p'_P(u)+p'_{P-1}(u)\}.
\]

The identity comes from summing
`L'_(j+1)-L'_(j-1)=(2j+1)L_j`.
Integration by parts gives

\[
 q(\tau)-(\Pi_Pq)(\tau)
   =\tfrac12\int_0^\tau
       [p_P(s/\tau)+p_{P-1}(s/\tau)]q'(s)ds.
 \tag{17}
\]

The boundary multiplier is zero at `s=0` and one at `s=tau`.
Its squared integral is
`tau[1/(2P+1)+1/(2P-1)]/4`, proving the first inequality of (16).
For the second, it suffices to prove `integral_0^1 |K_P|<=C sqrt(P)`.
Here is a proof of that estimate without a regularity assumption on `b`.

For `j>=1`, set

\[
 v(\theta)=\sqrt{\sin\theta}\,L_j(\cos\theta),\qquad
 Q(\theta)=(j+\tfrac12)^2+\frac1{4\sin^2\theta}.
\]

The Legendre equation gives `v''+Qv=0`, and hence

\[
 \frac d{d\theta}\left(v^2+\frac{(v')^2}Q\right)
       =-\frac{Q'}{Q^2}(v')^2\ge0
               \quad(0<\theta\le\pi/2).
\]

At `pi/2`, the formulas
`L_(2k)(0)=(-1)^k binom(2k,k)/4^k`, `L_(2k+1)(0)=0`, and
`L'_j(0)=jL_(j-1)(0)`, together with
`binom(2k,k)/4^k<=1/sqrt(k+1)`, bound this quantity by `C/j`.
The binomial bound follows by induction, comparing successive ratios
`(2k+1)/(2k+2)` with `sqrt((k+1)/(k+2))`.
It follows that, on `1/j<=theta<=pi/2`,

\[
 \left|\frac d{d\theta}L_j(\cos\theta)\right|
  \le\frac C{\sqrt j}
       \left\{\frac j{\sqrt{\sin\theta}}
                     +\frac1{\sin^{3/2}\theta}\right\}.
\]

The integral is at most `C sqrt(j)`, using
`sin(theta)>=2theta/pi`. On `0<=theta<=1/j`, the bound
`|L'_j|<=j(j+1)/2` gives a contribution bounded by a constant.
To justify this derivative bound, the generating function gives the
integral representation
`L_k(cos(theta))=pi^-1 integral_0^pi
(cos(theta)+i sin(theta)cos(alpha))^k d alpha`, so `|L_k|<=1`.
Summing the derivative identity above then gives the claimed bound on
`|L'_j|`. Parity handles the other half of the interval. Thus
`Var_[-1,1] L_j<=C sqrt(j)`, and the displayed formula for `K_P` proves
its required `L^1` bound. The case `P=1` is immediate. This completes
the proof of (15)--(16).

## 3. A fixed tube supplies RMS bounds for unbounded activations

Set `D=K+1` and define fixed numbers

\[
 M_1=a_1+s_1(A_0+1),\qquad
 M_\ell=a_\ell+s_\ell D M_{\ell-1}\quad(2\le\ell\le L),
 \qquad c_0=1+M_L,
 \qquad c_S=4c_0/\lambda_0.
 \tag{18}
\]

The elementary estimate
`|phi^(ell)(u)|<=a_ell+s_ell |u|` follows by integrating its bounded
derivative. Therefore, on the tube

\[
 \|W^{(\ell)}\|_{\rm op}<D\quad(\ell\ge2),
 \qquad
 \max_a\|z_a^{(1)}\|_2/\sqrt n<A_0+1,
 \tag{19}
\]

forward induction gives
`max_a ||h_a^(ell)||_2/sqrt(n)<=M_ell`.
This is RMS control only; individual feature coordinates need not be
bounded independently of `n`.

Take `S=c_S Y`, shrink the eventual label threshold so `S<=1`, and stop a
local closure before first exit from (19) or first activity
`s(t)=integral_0^t rho=S`. Write `A=1+S<=2` and set

\[
 B=Y+2M_LS,
 \qquad\beta_L=s_L B,
 \qquad\beta_\ell=s_\ell D\beta_{\ell+1}\quad(\ell<L).
 \tag{20}
\]

The readout equation gives
`||dot w||_2/sqrt(n)<=2M_L rho`, so `||w||_2/sqrt(n)<=B`.
The backward recurrence (2) then proves
`max_a ||delta_a^(ell)||_2/sqrt(n)<=beta_ell`.
Each `beta_ell` equals a fixed constant times `Y`.
Also `rho(0)<=Y+B_0 M_L<=c_0 Y`.

By the zero backward prefix and `||r/rho||_m=1`,

\[
 \frac1{mn}\sum_a\int_0^\tau\|b_{\ell,a}\|_2^2d\xi
       \le S\beta_\ell^2,
 \qquad
 \frac1{mn}\sum_a\int_0^\tau\|h_{\ell-1,a}\|_2^2d\xi
       \le A M_{\ell-1}^2.
 \tag{21}
\]

The projection representation of (5), contraction, (11), and
Cauchy--Schwarz in history and sample index imply

\[
 \|\widehat W^{(\ell)}-W_0^{(\ell)}\|_F
       \le2M_{\ell-1}\beta_\ell\sqrt{AS}=O(Y^{3/2}).
 \tag{22}
\]

The first-matrix equation gives

\[
 \frac{\|\widehat W^{(1)}(t)-W_0^{(1)}\|_F}{\sqrt n}
       \le2X\beta_1S,
 \qquad
 \max_a\frac{\|\widehat z_a^{(1)}(t)-z_a^{(1)}(0)\|_2}{\sqrt n}
       \le2X^2\beta_1S=O(Y^2).
 \tag{23}
\]

Consequently, making `Y_*` small keeps both kinds of tube boundary a
strict distance away. These are bounds derived inside a stopped tube,
not assumptions on the closure trajectory.

## 4. Forward energy and relative defect on the stopped interval

We first obtain the forward derivative energy without using a backward
derivative or a pointwise relative defect estimate. The first-layer clock
derivative has RMS at most `2s_1 X^2 beta_1`, so

\[
 Z_1(t)\le4S s_1^2X^4\beta_1^2.
 \tag{24}
\]

Degree-below-`P` endpoint evaluation has `L^2` operator norm
`P/sqrt(tau)`, since `sum_(k<P)(2k+1)=P^2`.
Applied to the sample direct sum and (21), this bounds the RMS backward
endpoint error by `(P+1)beta_ell`. Combining (12), (13), and (15) yields

\[
 \int_0^t\rho\|E_\ell/\rho\|_F^2du
       \le2A^2\beta_\ell^2 Z_{\ell-1}(t).
 \tag{25}
\]

Indeed the left side is at most `4(P+1)^2 beta_ell^2` times the averaged
forward squared tail, and that tail is at most
`A^2 Z_(ell-1)/(4P(P+1))`; `(P+1)/P<=2` completes (25).

The canonical hidden velocity obeys
`||F_ell/rho||_F<=2beta_ell M_(ell-1)`.
The forward chain rule, with primes denoting clock derivatives, is

\[
 (h_a^{(\ell)})'=(\phi^{(\ell)})'(z_a^{(\ell)})\odot
 \{(F_\ell/\rho+E_\ell/\rho)h_a^{(\ell-1)}
                      +\widehat W^{(\ell)}(h_a^{(\ell-1)})'\}.
\]

Use (25), `||h_a^(ell-1)||_2/sqrt(n)<=M_(ell-1)`, and the
squared three-term triangle inequality. Inductively,

\[
 Z_\ell(t)\le Z_\ell^*,\qquad Z_1^*=4Ss_1^2X^4\beta_1^2,
\]
\[
 Z_\ell^*=3s_\ell^2\left[
      4S\beta_\ell^2M_{\ell-1}^4+
      \{D^2+2A^2\beta_\ell^2M_{\ell-1}^2\}Z_{\ell-1}^*
                         \right]\le CY^3.
 \tag{26}
\]

All constants are independent of `n,P` and of the physical endpoint.
The powers `M_(ell-1)^4` in the dense source and
`M_(ell-1)^2` in the defect term account for unbounded features; replacing
these by one would not be justified for the present activation class.

The backward history satisfies
`sup_xi ||b_(ell,a)(xi)||_2/sqrt(n)<=sqrt(m) beta_ell`.
The second bound in (16) therefore gives backward endpoint error at most
`C sqrt(P)Y` for each sample. The first bound in (16), applied to the
forward histories and averaged in samples, gives forward endpoint error
at most `C sqrt(A Z_(ell-1)/P)<=C Y^(3/2)/sqrt(P)`.
Using (11) and (13) now proves

\[
 e_E\le CY^{5/2}\rho.
 \tag{27}
\]

There is no derivative assumption on the backward history in this step.
The cancellation of the two endpoint powers is also why (27) holds for
all orders, including `P=1`.

For later use, (14), (15), and (21) give the first estimate in (9):

\[
 \int_0^t e_E\,du
 \le\frac A{\sqrt{P(P+1)}}
       \sum_{\ell=2}^L\beta_\ell\sqrt{S Z_{\ell-1}^*}
 \le\frac{CY^3}{\sqrt{P(P+1)}}.
 \tag{28}
\]

## 5. Gram stability, activity closure, and continuation

For the ordinary prediction Jacobian `J`, the tangent Gram is
`Gamma=m^-1 J D_mob J^T`, with `D_mob=diag(n,1,...,1,n)`. Explicitly,

\[
 \Gamma_{ab}=\frac1m\left[
 \frac{(h_a^{(L)})^Th_b^{(L)}}n+
 \frac{(\delta_a^{(1)})^T\delta_b^{(1)}}n\frac{x_a^Tx_b}d+
 \sum_{\ell=2}^L
 \frac{(\delta_a^{(\ell)})^T\delta_b^{(\ell)}}n
 \frac{(h_a^{(\ell-1)})^Th_b^{(\ell-1)}}n\right].
 \tag{29}
\]

Each term is a parameter-derivative Gram, hence positive semidefinite.
In particular `Gamma>=Gamma_w`. The feature drift and (26) give

\[
 \frac{\|H_L(t)-H_L(0)\|_F}{\sqrt{mn}}
       \le\sqrt{S Z_L^*},\qquad
 \|\Gamma_w(t)-\Gamma_w(0)\|_{\rm op}
       \le2M_L\sqrt{S Z_L^*}\le CY^2.
 \tag{30}
\]

The first inequality is Cauchy--Schwarz on the nonconstant clock interval
of length at most `S`; the second expands the difference of two Gram
products and uses the RMS feature bound on both endpoints.
Shrink `Y_*` so the last quantity is at most `lambda_0/2`.
Also (29) bounds `||Gamma||op<=G_*` independently of `n,P,Y` on the
stopped interval, since the forward RMS is bounded and every backward
RMS is `O(Y)`.

The defect is supported on hidden blocks. For each sample its output
differential is
`sum_(ell>=2) delta_a^(ell)T E_ell h_a^(ell-1)/n`, so
`||JE||_m<=C Y e_E`. The exact residual equation is consequently

\[
 \dot r=-2\Gamma r+JE,
 \qquad \|JE\|_m\le CY^{7/2}\rho.
 \tag{31}
\]

Taking the inner product with `r/rho` yields

\[
 -(2G_*+CY^{7/2})\rho\le\dot\rho
       \le-(\lambda_0-CY^{7/2})\rho.
 \tag{32}
\]

Make `CY_*^(7/2)<=lambda_0/2` and set `kappa=lambda_0/2`.
For a fixed finite `Lambda` dominating the left coefficient, integration
proves (6) on the stopped interval, and

\[
 s(t)\le\rho(0)/\kappa
       \le2c_0Y/\lambda_0=S/2.
 \tag{33}
\]

Together with the strict tube margins in (22)--(23), (33) excludes every
stopping boundary.

For completeness, the raw moment vector field is locally Lipschitz for
`tau>0`: the reconstruction is smooth there, the network is `C^1` with
locally Lipschitz derivative by (3), and the residual norm is locally
Lipschitz. All raw velocities vanish when `rho=0`. Local uniqueness
backwards from this equilibrium excludes a first zero at a finite
regular endpoint of a nonstationary solution. This justifies the clock
change on every compact regular interval, even before (32) is available.

On an activity-capped interval, (19)--(23) bound the physical variables
at each fixed width, and (21) plus the finite norms of the first `P`
Legendre polynomials bound every raw moment for each fixed `n,P`.
The first matrix is bounded by its finite initial value plus (23),
also in the preactivation-only version of (4). The raw state therefore
lies in a compact subset of `tau>0`. Its locally Lipschitz vector field
is bounded there; a finite maximal endpoint would have a limiting state
from which the solution extends. Since neither a stopping boundary nor
such an endpoint is possible, the closure is global and all estimates
hold for all time.

The dense flow has the same bootstrap. Its hidden update integral gives
`||W^(ell)-W_0^(ell)||_F<=2S beta_ell M_(ell-1)`, which is even smaller
than (22). Its forward energy satisfies (26) with the defect term removed,
and (31) has `E=0`. The same strict margins and continuation argument
prove its global existence and fitting bounds. Dense global existence
can alternatively be obtained from the exact loss dissipation identity.

From (27) and the canonical update equations,

\[
 \frac{\|\dot W^{(1)}\|_F}{\sqrt n}
       +\sum_{\ell=2}^L\|\dot W^{(\ell)}\|_F\le CY\rho,
 \qquad \frac{\|\dot w\|_2}{\sqrt n}\le C\rho
 \tag{34}
\]

for either flow. Integrability of `rho` implies finite total physical
variation, hence a finite parameter limit. Equation (6) and continuity
of the network show that its limit interpolates the data. The moment
equations likewise have integrable velocities at fixed `n,P`, so their
limits exist as well.

The constants in the bootstrap are explicit fixed functions of the stated
data: use (18)--(20), then (26), and require the finitely many strict
inequalities used in (22), (23), (30), (32), together with `S<=1`.
Each left side tends to zero as `Y` tends to zero. Their common positive
threshold depends on none of `n,P,t`.

## 6. Actual backward source regularity and its terminal cutoff

This section concerns the actual closure after the bootstrap, not an
assumed smooth closure history or a source transported from the dense flow.
Its forward derivatives satisfy

\[
 \max_{\ell,a}\frac{\|\dot z_a^{(\ell)}\|_2}{\sqrt n}
 +\max_{\ell,a}\frac{\|\dot h_a^{(\ell)}\|_2}{\sqrt n}
       \le CY\rho.
 \tag{35}
\]

For the first layer this follows from (34); at each next layer use
`dot z=dot W h+W dot h`, the RMS feature bound and bounded operator norm.
No coordinate bound on the feature is used.

Each *full* backward carrier has supremum norm bounded by `C sqrt(n)Y`:
at the top it is `w`, and below it is `(W^(ell+1))^T delta^(ell+1)`.
Indeed its Euclidean norm bounds its supremum norm, and its RMS follows
from (20). This applies to the trained operator as a whole. A separate
coordinate estimate for the learned part is unnecessary.

A Lipschitz derivative composed with an absolutely continuous coordinate
is absolutely continuous and has derivative bounded in absolute value
by its Lipschitz constant times that coordinate's speed, almost everywhere.
This follows directly from the Lipschitz difference inequality and the
absolute-continuity criterion, then from differentiation of that inequality
at Lebesgue points. Applying it to the gates in (2) avoids requiring a
continuous second activation derivative. The differentiated top relation
and (34)--(35) give

\[
 \frac{\|\dot\delta_a^{(L)}\|_2}{\sqrt n}
 \le s_L\frac{\|\dot w\|_2}{\sqrt n}
       +j_L\|w\|_\infty
                         \frac{\|\dot z_a^{(L)}\|_2}{\sqrt n}
 \le C(1+\sqrt nY^2)\rho.
\]

At each lower layer, the differentiated operator term has RMS at most
`C Y^2 rho`, the gate derivative term at most `C sqrt(n)Y^2 rho`, and
the remaining derivative is propagated by an operator of fixed norm.
Downward induction proves, almost everywhere,

\[
 \max_{\ell,a}\frac{\|\dot\delta_a^{(\ell)}\|_2}{\sqrt n}
       \le C(1+\sqrt nY^2)\rho.
 \tag{36}
\]

Equation (31) gives `||dot r||_m<=C rho`. For `c=r/rho`,
`||dot c||_m<=2||dot r||_m/rho<=C`. Hence `b_a=c_a delta_a` obeys

\[
 \left[\frac1{mn}\sum_a\|\dot b_{\ell,a}\|_2^2\right]^{1/2}
      \le C\{Y+(1+\sqrt nY^2)\rho\},
\]
\[
 \frac1{mn}\sum_a\int_0^T\|\dot b_{\ell,a}\|_2^2dt
      \le CY^2(T+1+nY^4).
 \tag{37}
\]

The second inequality uses (6), `rho(0)<=c_0Y`, and
`(1+sqrt(n)Y^2)^2<=2(1+nY^4)`. It does not assert a square-integrable
normalized-residual direction derivative over the whole infinite
physical interval.

To convert (37) into a clock tail, combine the `m` vector histories in
the ordinary Hilbert direct sum with squared norm
`m^-1 sum_a ||v_a||_2^2/n`. Denote its norm only in the next paragraph
by `||.||`, and write `A_infinity=1+integral_0^infinity rho`.
The right limit `b_0=b(1+)` has `||b_0||<=CB_0` by the initial backward
recursion. Subtract its prefix jump:

\[
 \widetilde b(\xi)=b(\xi)-b_0\mathbf1_{[1,A_\infty)}(\xi).
 \tag{38}
\]

This joins continuously to zero at `xi=1`, has norm at most `CY`, and
has the same physical derivative as `b` for positive time.
Let `q_T` agree with `tilde b` up to `tau(T)` and stay constant thereafter.
It is `H^1` on every finite clock interval. From (32), the remaining
activity `a(t)=integral_t^infinity rho` satisfies
`a(t)<=rho(t)/kappa`. For every endpoint `tau(t)`, changing variables in
the weighted energy gives

\[
 \int_0^{\tau(t)}\xi(\tau(t)-\xi)\|q_T'(\xi)\|^2d\xi
 \le\int_0^{\min(t,T)}
       \tau(s)a(s)\frac{\|\dot b(s)\|^2}{\rho(s)}ds
 \le CY^2(T+1+nY^4).
 \tag{39}
\]

If `t>T`, the cutoff error is supported in a clock interval of length at
most `a(T)`; if `t<=T`, it is zero. Thus in either case

\[
 \|\widetilde b-q_T\|_{L^2(0,\tau(t))}
       \le CY\sqrt{a(T)}\le CY^{3/2}e^{-\kappa T/2}.
 \tag{40}
\]

The weighted tail inequality (15), best approximation, and (39)--(40)
give

\[
 \|(I-\Pi_P)\widetilde b\|_{L^2(0,\tau(t))}
 \le\frac{CY\sqrt{T+1+nY^4}}{\sqrt{P(P+1)}}
                 +CY^{3/2}e^{-\kappa T/2}.
 \tag{41}
\]

The step subtracted in (38) has tail at most `CB_0/sqrt(P)` since
`1<=tau(t)<=2`. For `P>=2`, replace the scalar step by a linear ramp
on `[1-tau/P,1]`. This interval lies in `[0,1]`; its squared `L^2`
approximation error is at most `tau/P` and its derivative squared norm
is at most `P/tau`. Applying (15) to the ramp yields the required
`C sqrt(tau/P)` bound. Multiplying by `b_0` proves the vector step
bound; for `P=1` use projection contraction. If the endpoint is exactly
one, the step is zero almost everywhere and the same bound holds.

Choose `T=(2/kappa)log(e+P)`. Since `Y<=1`, (41) and the step estimate
prove (8). The forward energy and (15) give

\[
 \left[\frac1{mn}\sum_a\int_0^{\tau(t)}
       \|(I-\Pi_P)h_{\ell-1,a}\|_2^2d\xi\right]^{1/2}
                         \le CY^{3/2}/P.
 \tag{42}
\]

Use sample Cauchy--Schwarz in (14), apply (8) and (42), and sum in
layer. Increasing `t` to infinity on the nonnegative left side proves
the second estimate in (9). This controls total absolute velocity
defect, not only a signed reconstruction discrepancy.

## 7. All-time comparison with only one square-root width loss

Use the scaled block errors

\[
 x(t)=\frac{\|\widehat W^{(1)}-W_D^{(1)}\|_F}{\sqrt n}
       +\sum_{\ell=2}^L\|\widehat W^{(\ell)}-W_D^{(\ell)}\|_F,
 \qquad
 z(t)=\frac{\|\widehat w-w_D\|_2}{\sqrt n},\qquad
 d(t)=x(t)+z(t).
 \tag{43}
\]

The scalar `z(t)` in this section is a readout error, not a preactivation.
The sum `d` dominates `d_n` and is at most `sqrt(L+1)d_n`.
The tube and RMS feature bounds give, by forward subtraction,

\[
 \max_{\ell,a}\frac{\|\widehat z_a^{(\ell)}-z_{D,a}^{(\ell)}\|_2}{\sqrt n}
 +\max_{\ell,a}\frac{\|\widehat h_a^{(\ell)}-h_{D,a}^{(\ell)}\|_2}{\sqrt n}
       \le Cx.
 \tag{44}
\]

At the first layer use `X ||Delta W^(1)||_F/sqrt(n)`.
At higher layers write the preactivation difference as
`Delta W h_D+W_hat Delta h`; its RMS is bounded by
`M_(ell-1)||Delta W||_F+D ||Delta h||_2/sqrt(n)`.
The activation is `s_ell`-Lipschitz, proving (44) by induction.

Let
`b_ell(t)=max_a ||delta_hat_a^(ell)-delta_D,a^(ell)||_2/sqrt(n)`.
At the top, subtract the backward equations, placing the dense readout
in the gate-difference term. At lower layers place the full dense carrier
`(W_D^(ell+1))^T delta_D^(ell+1)` in that term. Using its proved
`C sqrt(n)Y` supremum bound, (3), and (44), gives

\[
 b_L\le C[z+\sqrt nYx],\qquad
 b_\ell\le Cb_{\ell+1}+CYx+C\sqrt nYx.
\]

Since depth is fixed and `n>=1`,

\[
 \max_\ell b_\ell\le C[z+\sqrt nYx].
 \tag{45}
\]

This uses no learned-carrier coordinate estimate and no coordinate bound
on an unbounded feature. The only coordinate inequality is
`||carrier||_infinity<=||carrier||_2`.

Set `q=f_hat-f_D`, `v=||q||_m`, and `Q(t)=integral_0^t v`.
Subtracting the two exact residual equations yields

\[
 \dot q=-2\widehat\Gamma q
       -2(\widehat\Gamma-\Gamma_D)r_D+\widehat J E.
 \tag{46}
\]

A forward normalized pairing changes by at most `Cx`, and a backward
normalized pairing by at most `CY max b_ell`.
Use (29) and the fact that an `m`-by-`m` matrix with entries bounded
by `A/m` has operator norm at most `A`. Equations (44)--(45) prove

\[
 \|\widehat\Gamma-\Gamma_D\|_{\rm op}
       \le C[(1+\sqrt nY^2)x+Yz].
 \tag{47}
\]

The readout Gram gap and `||J_hat E||_m<=CY e_E` then give the norm
inequality

\[
 D^+v\le-\lambda_0v+
       C\rho_D[(1+\sqrt nY^2)x+Yz]+CY e_E.
 \tag{48}
\]

At a zero of `v` this means the upper right derivative; equivalently one
can regularize the norm by `sqrt(v^2+eta^2)` and pass to zero after
integrating on a finite interval. Since `q(0)=0`, integration and
discarding the nonnegative endpoint give, with
`epsilon_P(t)=integral_0^t e_E`,

\[
 Q(t)\le C\int_0^t\rho_D[(1+\sqrt nY^2)x+Yz]ds
                                     +CY\varepsilon_P(t).
 \tag{49}
\]

Subtract the readout updates as
`r_hat h_hat-r_D h_D=q h_hat+r_D(h_hat-h_D)`.
Subtract a hidden update as
`q delta_hat h_hat^T+r_D(delta_hat-delta_D)h_hat^T
+r_D delta_D(h_hat-h_D)^T`.
For the first matrix use the corresponding fixed-input formula.
The rank-one identity (11), RMS feature bounds and (44)--(45) yield

\[
 z(t)\le C Q(t)+C\int_0^t\rho_D x\,ds,
\]
\[
 x(t)\le CY Q(t)+C\int_0^t\rho_D[z+\sqrt nYx]ds
                                         +\varepsilon_P(t).
 \tag{50}
\]

To check the width power, put `g=sqrt(n)Y`. The integrand in (49)
is `(1+Yg)x+Yz`. Inserting it into the first inequality of (50) produces
at most `(1+g)x+z`; inserting it into the second produces the coefficients
`Y+Y^2g+g<=C(1+g)` on `x` and `1+Y^2<=2` on `z`.
Here only `0<Y<=1` is used. Thus no multiplication of two width losses
occurs, and

\[
 d(t)\le C\varepsilon_P(t)
             +C(1+\sqrt nY)\int_0^t\rho_D(s)d(s)ds.
 \tag{51}
\]

For any terminal `t`, replace the nondecreasing inhomogeneous term on
`[0,t]` by `C epsilon_P(t)`. Its integral majorant has derivative bounded
by `C(1+sqrt(n)Y)rho_D` times itself; integration gives

\[
 \sup_{0\le s\le t}d(s)
 \le C\varepsilon_P(t)
       \exp\!\left\{C(1+\sqrt nY)\int_0^t\rho_D(s)ds\right\}.
\]

Since dense activity is at most `CY`, increasing `t` proves (10).
The integrability of `v` follows from (49), the uniform bound on `d`,
finite dense activity and finite `epsilon_P`, at each fixed width.
The limits exist by Section 5, so (10) also bounds their difference.

## 8. Scope, examples, and check record

The hypotheses allow smooth unbounded activations such as softplus,
exact GELU, and SiLU. This can be checked directly without using a bound
on the activation itself. For softplus `log(1+exp(u))`, its derivative is
the sigmoid and its second derivative lies in `[0,1/4]`. For exact GELU
`u Phi(u)`, its derivative is `Phi(u)+u varphi(u)` and its second
derivative is `(2-u^2)varphi(u)`, both bounded, where `Phi,varphi` are the
standard normal CDF and density. For SiLU `u sigma(u)`, the derivative
is `sigma+u sigma(1-sigma)` and the second derivative is
`2sigma(1-sigma)+u sigma(1-sigma)(1-2sigma)`; boundedness follows from
the exponential tail of `sigma(1-sigma)`. These examples do not certify
the initial Gram gap for a particular data set. Piecewise linear ReLU
is outside (3) because its derivative is discontinuous.

At fixed width, (9)--(10) give all-time `O(P^-1)` tracking and the
stronger displayed spectral rate. The `B_0 P^-3/2` term disappears at
exactly zero initial readout. The tracking constant is width-uniform
under a common bound on `sqrt(n)Y_n^2`, using the first estimate in (9).
At fixed positive labels the exponential width factor remains. Removing
it requires an additional estimate on the actual gate/carrier product;
neither feature RMS control nor exponential residual fitting supplies
such an estimate. For unrestricted pairs `(n,P)`, `C^{1,1}_loc` alone
does not supply common constants in the displayed source tail (8) and
tracking estimate (10). An explicit derivative-Lipschitz modulus on the
visited preactivation range, combined with a joint order/width scaling,
is a separate possible extension. This limitation concerns those
quantitative approximation bounds and does not change the
modulus-independent all-order fitting bootstrap proved above.

The derivation explicitly checked the unbounded-feature factors in (22),
(25)--(26), (30)--(31), (34)--(36), and (44)--(50); the endpoint kernel
calculation; the initial backward jump; the terminal cutoff; zero initial
residual; `P=1`; and the absence of width powers beyond `sqrt(n)` in
the comparison exponent. This is an author algebraic check only. The
supervisor should check the complete candidate before recording it as an
internally checked study result. No numerical validation is claimed.

Input SHA-256 values at derivation time:

| Input | SHA-256 |
| --- | --- |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `paper/main.tex` | `a1d861c53a76959bd607aeb03cec39639b522bf48014a14cda597ef9b856c386` |
| `LOSS_DECAY_ACTIVITY_BOOTSTRAP.md` | `1d630d9c6efab174a1dfb8d8d43390d635b90b3dbc40e58211a74bd440fe6215` |
| `SMALL_LABEL_SPECTRAL_SLACK.md` | `8200da95597b38856ab41c803c6966e398224ded0944d1e4664eda1943976967` |
| `SMALL_LABEL_ENERGY.md` | `f53e24682c7c51ea70b09570aa1c478822c48466d5b5aa8f5bca57d1827d9119` |
