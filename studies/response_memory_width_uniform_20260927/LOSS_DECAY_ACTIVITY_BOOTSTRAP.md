# Fitting and finite activity for the autonomous old clock

Scoped analytic argument, 28 September 2026. Inputs: the canonical setting,
old-clock equations and complete old-clock proof in `paper/main.tex`, and
this study's `OLD_CLOCK_ROUTE.md`, `ENERGY_STABILITY_ROUTE.md` and
`GENERAL_AUTONOMOUS_SYNTHESIS.md`. The `solve-math-rigorously` skill was
applied. No external search, experiment, other study or maintained-file
change was used. This is an internally derived study result, not a
promoted theorem or an independent review.

**Result.** The original autonomous closure has finite total residual
mass and converges to an interpolating parameter for every sufficiently
large memory order if a fixed-width dense trajectory converges to a
regular fitted parameter. There is also a genuine all-order theorem:
if the initial readout feature Gram has a positive gap, sufficiently
small labels and zero initial readout give fitting for every `P >= 1`.
The latter extends to an initial readout whose normalized norm is at
most the label RMS. Neither conclusion assumes decay of the closure's
own residual. Neither proves an exponential decay rate or fitting at
every order for arbitrary label amplitudes.

## 1. Model, exact residual equation, and the exponential criterion

Use the manuscript's canonical finite network, with tanh at every hidden
layer, fixed finite width `n`, depth `L >= 2`, and `m` samples. The raw
old-clock system is exactly manuscript equations `eq:old-clock`,
`eq:old-ode` and `eq:old-recon`; its first layer and readout follow
`eq:dense-flow`, evaluated at its own reconstructed network. Put

\[
 \|u\|_m^2=\frac1m\sum_a u_a^2,\qquad
 \|v\|_{\rm mob}^2=\frac{\|v_1\|_F^2}{n}
    +\sum_{\ell=2}^L\|v_\ell\|_F^2+
       \frac{\|v_w\|_2^2}{n}.
\]

Write `r = f-y`, `rho = ||r||_m`, and `s(t) = integral_0^t rho` so that
`tau = 1+s`. Let `J = D_theta f` be the ordinary `m`-by-parameter
Jacobian and `D = diag(n,1,...,1,n)` the manuscript's mobility matrix.
The physical closure equation, from manuscript `eq:defect`, is

\[
 \dot{\widehat\theta}=F(\widehat\theta)+E,
 \qquad E_1=E_w=0,
 \qquad F=-\frac2m\mathcal D J^T r.
 \tag{1}
\]

Consequently its actual residual equation is

\[
 \dot r=-2\Gamma r+JE,\qquad
 \Gamma=\frac1mJ\mathcal D J^T,
 \tag{2}
\]

with all entries evaluated at the current closure state, and

\[
 \Gamma_{ab}=\frac1m\left[
 \frac{h_{L,a}^Th_{L,b}}n+
 \frac{(\delta_{1,a}^T\delta_{1,b})(x_a^Tx_b)}{nd}
 +\sum_{\ell=2}^L
 \frac{(\delta_{\ell,a}^T\delta_{\ell,b})
       (h_{\ell-1,a}^Th_{\ell-1,b})}{n^2}\right].
 \tag{3}
\]

Each term is positive semidefinite: it is the Gram of the corresponding
parameter derivatives with their positive mobility. In particular, if
`H_L` is the `n`-by-`m` matrix with columns `h_(L,a)`, then

\[
 \Gamma\succeq\Gamma_w:=\frac{H_L^T H_L}{mn}.
 \tag{4}
\]

At positive residual,

\[
 \dot\rho=-\frac{2r^T\Gamma r}{m\rho}
                +\frac{r^TJE}{m\rho},\qquad
 \dot{\mathcal L}=-4\langle r,\Gamma r\rangle_m
                         +2\langle r,JE\rangle_m.
 \tag{5}
\]

Thus `Gamma_w >= lambda I` and `||JE||_m <= eta rho`, with
`eta < 2 lambda`, imply

\[
 \rho(t)\le\rho(t_0)e^{-(2\lambda-\eta)(t-t_0)}.
 \tag{6}
\]

This is an exact sufficient exponential criterion. The existing
projection estimates do not prove that its relative-error coefficient
`eta` becomes small uniformly in time as `P` grows. Backward polynomial
endpoint evaluation can amplify with `P`; a small integrated defect is
not a pointwise bound on `E/rho`. The cross term in (5) has no sign
provided by the old-clock identities. This observation alone is not a
counterexample to fitting.

All subsequent Gram conditions may instead be imposed on a fixed
nonzero subspace `U` containing the label vector and every network
prediction vector under consideration. Then `r in U`, and only
`r^T Gamma_w r >= lambda ||r||_2^2` on `U` is needed. This covers
architecture-imposed compatible relations such as tanh oddness on
antipodal samples. Taking `U = R^m` is sufficient throughout.

## 2. Old-clock bounds with an activity cap, independent of physical time

Fix `S > 0` and stop a regular closure interval before `s(t)` exceeds
`S`. Define

\[
 X=\max_a\|x_a\|_2/\sqrt d,\quad
 B_0=\|w_0\|_2/\sqrt n,\quad
 K_\ell=\|W_{0,\ell}\|_{\rm op},\quad
 A=1+S,\quad B=B_0+2S.
\]

The unchanged readout equation gives

\[
 \frac{\|\dot w\|_2}{\sqrt n}
 \le\frac2m\sum_a |r_a|\frac{\|h_{L,a}\|_2}{\sqrt n}
 \le2\rho,
\]

so `||w||_2/sqrt(n) <= B`. Define downward in layer

\[
 \beta_L=B,\qquad D_\ell=K_\ell+2A\beta_\ell,
 \qquad \beta_{\ell-1}=D_\ell\beta_\ell
 \quad(\ell=L,\ldots,2).
 \tag{7}
\]

These give, on the stopped interval,

\[
 \|W_\ell\|_{\rm op}\le D_\ell,\qquad
 \max_a\frac{\|\delta_{\ell,a}\|_2}{\sqrt n}\le\beta_\ell,
 \qquad
 \frac{\|W_1(t)\|_F}{\sqrt n}
 \le\frac{\|W_1(0)\|_F}{\sqrt n}+2SX\beta_1.
 \tag{8}
\]

For completeness, the downward induction uses the zero backward prefix,
the normalized backward history `b_a = r_a delta_a/rho`, and

\[
 \frac1{mn}\sum_a\int_0^\tau\|b_{\ell,a}\|_2^2d\xi
 \le S\beta_\ell^2,
 \qquad
 \frac1{mn}\sum_a\int_0^\tau\|h_{\ell-1,a}\|_2^2d\xi\le A.
\]

Projection contraction in manuscript `eq:projection-form` therefore
bounds the learned operator by `2 sqrt(AS) beta_l <= 2A beta_l`.
The tanh backward recursion then bounds the next lower response.

Let

\[
 Z_\ell(t)=\frac1{mn}\sum_a\int_0^{\tau(t)}
                   \|(h_{\ell,a})'(\xi)\|_2^2d\xi,
\]

where the prime means differentiation in the clock and the constant
forward prefix has derivative zero. Define upward in layer

\[
 Z_1^*=4SX^4\beta_1^2,
 \qquad
 Z_\ell^*=3\left[4S\beta_\ell^2+
       (D_\ell^2+2A^2\beta_\ell^2)Z_{\ell-1}^*\right]
       \quad(2\le\ell\le L).
 \tag{9}
\]

Then `Z_l(t) <= Z_l*`. Here is the normalization and argument behind
the reused old-clock estimate. The first-layer clock derivative has
normalized norm at most `2 X^2 beta_1`. For later layers,
`||F_l/rho||_F <= 2 beta_l`; the forward chain rule and the exact
projection-error energy from manuscript `eq:projection-energy` give

\[
 \int_0^t\rho\|E_\ell/\rho\|_F^2du
       \le2A^2\beta_\ell^2 Z_{\ell-1}(t).
 \tag{10}
\]

To verify (10), degree-below-`P` endpoint evaluation has norm
`P/sqrt(tau)`, so the sample RMS backward endpoint error, divided by
`sqrt(n)`, is at most `(P+1) beta_l`. Combine this with the defect
product formula and

\[
 \frac1{mn}\sum_a D_{h,\ell-1,a}(t)
 \le\frac{A^2 Z_{\ell-1}(t)}{4P(P+1)}.
\]

The resulting coefficient is
`A^2 beta_l^2 (P+1)/P <= 2 A^2 beta_l^2`.
Applying `||u+v+w||^2 <= 3(||u||^2+||v||^2+||w||^2)` to the forward
chain rule yields precisely (9).

The exact identities used here, with unnormalized squared projection
errors `D_h,D_b`, are

\[
 \dot D_h=\rho\|h-h^*\|_2^2,\qquad
 \dot D_b=\rho\|b-b^*\|_2^2,
 \qquad
 E_\ell=\frac{2\rho}{nm}\sum_a
       (b_{\ell,a}-b_{\ell,a}^*)
       (h_{\ell-1,a}-h_{\ell-1,a}^*)^T.
 \tag{11}
\]

Their Cauchy--Schwarz consequence, followed by the forward Legendre
tail bound and the backward mass bound, is

\[
 \int_0^t\sum_{\ell=2}^L\|E_\ell(u)\|_Fdu
 \le\varepsilon_P(S):=\frac{C(S)}{\sqrt{P(P+1)}},
 \qquad
 C(S)=A\sum_{\ell=2}^L\beta_\ell\sqrt{S Z_{\ell-1}^*}.
 \tag{12}
\]

Every constant in (7)--(12) is independent of elapsed physical time
and of `P`. This is a direct version of the manuscript's old-clock
proof with a prescribed residual-mass budget, not a substitution of a
finite-horizon estimate into an infinite-horizon limit. The proof uses
only `integral rho <= S`, the physical bounds just derived, and the
clock length `tau <= 1+S`.

Two further bounds will be used:

\[
 \|F\|_{\rm mob}\le V(S)\rho,
 \qquad V(S)=2\left[X\beta_1+\sum_{\ell=2}^L\beta_\ell+1\right],
 \tag{13}
\]

and, with `b(S) = max_(2<=l<=L) beta_l`,

\[
 \|JE\|_m\le\sum_{\ell=2}^L\beta_\ell\|E_\ell\|_F
       \le b(S)\sum_{\ell=2}^L\|E_\ell\|_F.
 \tag{14}
\]

For (14), each sample's hidden-block differential is
`delta_(l,a)^T E_l h_(l-1,a)/n`, whose absolute value is at most
`beta_l ||E_l||_F` by (8) and bounded tanh features. Equation (13)
follows by bounding each canonical velocity block and using the
triangle inequality for the mobility norm.

### Continuation and the zero-residual endpoint

For each fixed `n,P`, the raw moment vector field is locally Lipschitz
on `tau > 0`: it uses the locally Lipschitz norm `rho`, the smooth
sources `r_a delta_a`, and division only by `tau`. At `rho = 0` every
raw velocity vanishes. Local uniqueness backward from such an
equilibrium excludes its first attainment at a finite regular time by
a nonstationary path. Hence the clock-coordinate calculations are valid
on every nonstationary compact regular interval. A zero-residual initial
state is stationary.

On an activity-capped interval, (8), `1 <= tau <= A` and the moment
integral representations bound every raw coordinate at fixed `n,P`.
For the moments one can use the finite supremum of each fixed Legendre
polynomial on `[0,1]` and the history bounds above. Thus the raw state
stays in a compact subset of `tau > 0`. A finite maximal endpoint
before activity exit is impossible: the bounded locally Lipschitz
vector field gives a limiting state, from which the local solution
extends. This continuation argument does not assume infinite-time
boundedness in advance.

If an argument below excludes activity exit for all time, (12)--(13)
give

\[
 \int_0^\infty\|\dot{\widehat\theta}\|_{\rm mob}dt
 \le V(S)S+\varepsilon_P(S)<\infty.
 \tag{15}
\]

The physical parameters therefore converge to a finite limit. Their
residual has a limit by continuity; if `integral rho < infinity`, this
limit must be zero. The raw moments also converge, because their
bounded-state equations have absolute velocity bounded by a fixed
constant times `rho`. Only physical convergence and fitting are needed
below.

## 3. All memory orders fit sufficiently small labels: zero readout

**Theorem.** Fix the hidden initialization and data inputs, take `w_0=0`,
and suppose the initial readout Gram has a gap `lambda_0 > 0` on the
compatible residual subspace `U`:

\[
 u^T\Gamma_w(0)u\ge\lambda_0\|u\|_2^2\qquad(u\in U).
 \tag{16}
\]

There exists `Y_* > 0`, depending on `lambda_0`, depth, `X` and the
initialized hidden operator norms, such that for every label vector
`y in U` with `0 < Y=||y||_m <= Y_*`, every old-clock order `P >= 1`
exists globally, converges to an interpolating parameter, and satisfies

\[
 \int_0^\infty\rho_P(t)dt\le\frac{3Y}{2\lambda_0}.
 \tag{17}
\]

Zero labels and zero readout give the stationary fitted solution.

**Proof.** Choose the activity cap `S=2Y/lambda_0` and form all constants
in Section 2 with `B_0=0`. As `S` decreases to zero, downward induction
in (7) and upward induction in (9) give

\[
 \beta_\ell=O(S),\quad D_\ell=O(1),\quad
 Z_\ell^*=O(S^3),\quad C(S)=O(S^3),\quad b(S)=O(S).
 \tag{18}
\]

All these constants involve only the fixed quantities in the statement;
they do not depend on label direction or memory order. For example,
`Z_1*=4 S X^4 beta_1^2=O(S^3)` and each term in the later recursion has
the same upper order. Each summand in `C(S)` is
`O(S) sqrt(S O(S^3))=O(S^3)`.

By the fundamental theorem of calculus in the clock and
Cauchy--Schwarz, the top feature matrix obeys

\[
 \frac{\|H_L(t)-H_L(0)\|_F}{\sqrt{mn}}
       \le\sqrt{S Z_L^*}.
\]

Both top feature matrices have Frobenius norm at most `sqrt(mn)`.
Writing their Gram difference as two products therefore gives

\[
 \|\Gamma_w(t)-\Gamma_w(0)\|_{\rm op}
       \le 2\sqrt{S Z_L^*}.
 \tag{19}
\]

For sufficiently small positive `Y`, (18) ensures both explicit
inequalities

\[
 2\sqrt{S Z_L^*}\le\lambda_0/2,
 \qquad b(S)C(S)/\sqrt2\le Y/2.
 \tag{20}
\]

The first uses an `O(S^2)` left side. The second uses an `O(S^4)` left
side while `Y=lambda_0 S/2`. Thus one common `Y_* > 0` exists.

Until first activity exit, (16), (19) and (20) keep the readout Gram
at least `lambda_0/2` on `U`. Equations (5) and (14) yield

\[
 \dot\rho\le-\lambda_0\rho+
             b(S)\sum_{\ell=2}^L\|E_\ell\|_F.
\]

Integrating and dropping the nonnegative terminal residual, with
`rho(0)=Y`, gives

\[
 s(t)\le\frac{Y+b(S)\varepsilon_P(S)}{\lambda_0}
 \le\frac{Y+b(S)C(S)/\sqrt2}{\lambda_0}
 \le\frac{3Y}{2\lambda_0}=\frac34S.
 \tag{21}
\]

This contradicts first attainment of `S`. The continuation argument in
Section 2 excludes any earlier finite maximal endpoint. Thus the
solution exists for all time and (21) holds for every finite `t`.
Monotone convergence of `s(t)` proves (17). Equation (15) proves
parameter convergence and interpolation. This completes the proof.

## 4. Small-readout extension, including the canonical small initialization

The preceding theorem extends to readouts satisfying

\[
 B_0=\|w_0\|_2/\sqrt n\le Y.
 \tag{22}
\]

Retain the initial feature gap (16), use the cap `S=4Y/lambda_0`, and
form the same constants with `B=B_0+2S`. Bounded features give
`rho(0) <= Y+B_0 <= 2Y`. Uniformly over (22), as `Y` tends to zero,

\[
 B=O(Y),\quad\beta_\ell=O(Y),\quad
 Z_\ell^*=O(Y^3),\quad C(S)=O(Y^3),\quad b(S)=O(Y).
\]

Choose the small-label threshold so that

\[
 2\sqrt{S Z_L^*}\le\lambda_0/2,
 \qquad b(S)C(S)/\sqrt2\le Y.
\]

The same differential inequality now gives, for every order,

\[
 s(t)\le\frac{2Y+b(S)C(S)/\sqrt2}{\lambda_0}
       \le\frac{3Y}{\lambda_0}=\frac34 S.
 \tag{23}
\]

The identical first-exit, continuation and total-variation arguments
give global fitting for all `P >= 1`, with total residual mass at most
`3Y/lambda_0`.

For canonical small random readout, this is a deterministic implication
on the event (22) together with the operator bounds and feature Gram
gap. No probabilistic feature-Gram theorem is proved here. The
small-label threshold and conclusions are uniform over families with
common bounds on `X`, depth and hidden initialized operator norms and a
common positive lower bound for `lambda_0`; all the displayed recursions
are normalized and contain no additional width dependence.

## 5. Transfer from a regular fitted dense limit for sufficiently large orders

**Theorem.** At a fixed finite width and finite initialization, suppose
the canonical dense tanh flow converges to a finite parameter
`theta_*`, with `f(theta_*)=y`, and the readout Gram at `theta_*` is
strictly positive on the compatible residual subspace `U`. Then there
exists `P_0 < infinity` such that every original autonomous old-clock
closure with `P >= P_0` has finite total residual mass, converges to a
finite interpolating parameter, and exists for all physical time.
Its interpolating limit need not equal `theta_*`.

**Proof.** By continuity of the finite-dimensional feature Gram, choose
a mobility-norm ball of radius `R > 0` centered at `theta_*` and a
constant `lambda > 0` on which `Gamma_w >= lambda I` on `U`. Choose
`J_* > 0` bounding the operator norm of `J` from the mobility norm to
the sample RMS norm on the closed ball. Such a finite bound exists by
smoothness and compactness. From the exact gradient relation,

\[
 \|F\|_{\rm mob}\le2J_*\rho
\]

there. Set

\[
 d_*:=\min\{1/4,\ R/(8J_*)\}>0.
\]

Dense convergence and interpolation provide a finite `t_0` such that

\[
 \|\theta_D(t_0)-\theta_*\|_{\rm mob}<R/4,
 \qquad \rho_D(t_0)<\lambda d_*/4.
\]

Let `S_D=integral_0^(t_0) rho_D` and choose the fixed global activity
cap `S=S_D+1`. The manuscript's finite-width compact-horizon theorem
gives uniform parameter convergence on `[0,t_0]` as `P -> infinity`.
On this fixed interval continuity of predictions gives convergence of
the residual uniformly, and hence convergence of its integral.
Therefore, for every sufficiently large `P`,

\[
 \|\widehat\theta_P(t_0)-\theta_*\|_{\rm mob}<R/2,
 \quad \widehat\rho_P(t_0)<\lambda d_*/2,
 \quad s_P(t_0)<S_D+1/4.
 \tag{24}
\]

The same order threshold can be increased until the constants of
Section 2, computed with the fixed cap `S`, satisfy

\[
 \varepsilon_P(S)\le\min\{R/8,\ \lambda d_*/(2J_*)\}
 \qquad(P\ge P_0).
 \tag{25}
\]

Starting at `t_0`, stop at first exit from the physical ball or first
attainment of activity `S`. The finite-horizon segment before `t_0`
has smaller activity by (24). On the stopped segment, (5) gives

\[
 \dot\rho\le-2\lambda\rho+J_*\|E\|_{\rm mob}.
\]

The defect bound (12) controls the entire history, so it also bounds
the integral over this terminal segment. Hence, by (24)--(25),

\[
 \int_{t_0}^t\rho\,du
 \le\frac{\rho_P(t_0)+J_*\varepsilon_P(S)}{2\lambda}
 \le d_*/2\le1/8.
 \tag{26}
\]

The total physical displacement after `t_0` is at most

\[
 2J_*\int_{t_0}^t\rho\,du+\varepsilon_P(S)
 \le J_*d_*+R/8\le R/4.
 \tag{27}
\]

Together with (24), this keeps the state strictly inside the radius-`R`
ball. The total activity is at most `S_D+1/4+1/8 < S_D+1=S`, also a
strict margin. Thus neither stopping event can occur. Section 2
excludes finite maximal endpoints while activity is bounded. The
closure is global, (26) proves finite total residual mass, and (15)
proves convergence to an interpolating parameter.

This is a fixed-width theorem. A uniform order threshold over a family
of widths additionally requires a corresponding uniform finite-time
entry estimate and uniform positive Gram and norm margins. Those
quantifiers do not follow merely by applying the fixed-width theorem
separately at each width.

## 6. Boundary of the conclusions

The proofs exploit integrated velocity error through a time-independent
activity cap. They do not replace it by an unproved pointwise relative
error estimate. They establish finite `integral rho` and actual fitting,
not an exponential rate. The all-order theorem has an explicit
small-label/readout regime; the dense-limit transfer requires a regular
fitted neighborhood and sufficiently large order. Neither proves nor
disproves the unrestricted claim that separated compatible data of any
label amplitude are fitted sufficiently fast by every finite old-clock
memory order. Establishing an initial Gaussian feature Gram gap, or a
dense fitting theorem supplying the transfer hypothesis, is separate
from the deterministic results proved in this note.
