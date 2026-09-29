# General autonomous closure: the new theorem and the remaining rate distinction

28 September 2026. Coordinator synthesis of the current investigation.
This is a study result, not a promoted change to the manuscript or book.
The original old-clock algorithm is retained. No experiment, altered
initialization, supplied gate, supplied residual, or replacement matrix is
part of the algorithm proved about here.

## 1. Precise model and conclusions

Fix the input dimension, a finite dataset of size `m`, and a finite number
`L>=2` of hidden layers. Inputs can be correlated and their Gram matrix can
be singular. All hidden activations are tanh. At width `n`, write

\[
 h_{1,a}=\tanh(W_1x_a/\sqrt d),\quad
 h_{\ell,a}=\tanh(W_\ell h_{\ell-1,a}),\quad
 f_a=n^{-1}w^Th_{L,a},\quad r_a=f_a-y_a.
\]

The canonical gradient-flow equations are

\[
 \begin{split}
 \dot W_1&=-\frac2m\sum_a r_a\delta_{1,a}(x_a/\sqrt d)^T,\\
 \dot W_\ell&=-\frac2{mn}\sum_a r_a\delta_{\ell,a}h_{\ell-1,a}^T,
                  &&2\le\ell\le L,\\
 \dot w&=-\frac2m\sum_a r_a h_{L,a},\\
 \delta_{L,a}&=w\odot\tanh'(W_Lh_{L-1,a}),\qquad
 \delta_{\ell,a}=\tanh'(z_{\ell,a})\odot W_{\ell+1}^T\delta_{\ell+1,a}.
 \end{split}
 \tag{1}
\]

Use the canonical independent Gaussian hidden initialization, with middle
entries of variance `1/n`, the prescribed Gaussian first rows, and zero
or small stored readout (`w_0,i ~ N(0,n^-2)` is included). Each finite dense
network and all its closure orders share exactly the same initialized
arrays. No coupling between different widths is required.

The old clock has speed `rho=(m^-1 sum r_a^2)^(1/2)` and length
`tau=1+integral rho`. For every hidden link and sample the closure stores
`P` forward and backward raw moments. A moment `M_k` has equation

\[
 \dot M_k=s-\frac{\rho}{\tau}
       \left[kM_k+\sum_{j<k}(2j+1)M_j\right],
 \quad k=0,\ldots,P-1,
 \tag{2}
\]

with source `s=rho h` for the forward moments and `s=r delta` for the
backward moments. Only the zeroth forward moment is initially nonzero,
equal to the initial feature. Reconstruct each hidden link as

\[
 \widehat W_\ell=W_{0,\ell}
 -\frac{2}{mn\widehat\tau}
       \sum_{a,k}(2k+1)M^b_{\ell,a,k}(M^h_{\ell-1,a,k})^T.
 \tag{3}
\]

All responses, residuals and clocks in (2)--(3) are those of the current
closure. Its outer weights obey (1) evaluated on its own network.

Measure discrepancies by

\[
 d_n(\theta,\vartheta)=
 \frac{\|W_1-V_1\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|W_\ell-V_\ell\|_F
 +\frac{\|w-v\|_2}{\sqrt n},\qquad
 e_{n,P}(T)=\sup_{0\le t\le T}d_n(\widehat\theta_{n,P}(t),\theta_n^D(t)).
 \tag{4}
\]

The normalization is substantive. Hidden matrix differences are learned
differences, because the initialized arrays cancel. Their ordinary
Frobenius norm is the Hilbert--Schmidt norm between finite RMS spaces.

**General theorem, locally unconditional.** On the deterministic local
interval `[0,T_*]` of the maintained canonical Gaussian population theorem,
there are constants independent of width and memory order such that:

1. For every error tolerance `epsilon>0`,

\[
 \lim_{P_0\to\infty}\sup_{n\ge1}
  \Pr\!\left\{\sup_{P\ge P_0}e_{n,P}(T) >\epsilon\right\}=0.
 \tag{5}
\]

2. There is a width-independent sufficient order and, for every fixed
   sufficiently large `P_0` and every `zeta>0`,

\[
 \lim_{n\to\infty}\Pr\!\left\{
   \sup_{P\ge P_0}e_{n,P}(T)>B_T(P_0)+\zeta\right\}=0,
 \quad
 B_T(P_0)=C_T P_0^{-3/2}
             \exp\!\bigl(C_T\sqrt{\log(e+P_0)}\bigr)
             \le \widetilde C_T/P_0.
 \tag{6}
\]

Increasing the constant and leaving a strict margin absorbs `zeta` into a
bound `C_T/P_0` in the probability limit for each fixed `P_0`. Bounded small
orders can also be included by increasing the constant, using the common
physical bounds. This does not make the width threshold independent of
`P_0`.

Equation (5) is uniform over all finite widths and all larger memory
orders. It implies convergence in probability for every deterministic
joint sequence with `P_j -> infinity`, whatever the widths `n_j` are.
Equation (6) retains the old theorem's order exponent with width taken
first. Neither conclusion is restricted to one input or two hidden layers.

**Prescribed finite horizons.** The same statements hold on any fixed
`[0,T]` on which the strong dense canonical population flow exists and has
the following explicitly stated dense-only regularity:

\[
 \sup_{t\le T}\max_{\ell,a}
 \mathbb E_\ell\exp(c_T|c^D_{\ell,a}(t)|^2)\le C_T,
 \quad c^D_{L,a}=w_D,\quad
 c^D_{\ell,a}=(W_{\ell+1}^D)^*\delta^D_{\ell+1,a}.
 \tag{7}
\]

The maintained local theorem verifies (7) on its local interval. A
sufficient longer-horizon condition is that each initialized backward
carrier is its Gaussian innovation of bounded variance plus a bounded
response-history term. For bounded tanh features, a uniform bound on the
total variation of its deterministic response measures supplies that
bounded term. This is regularity of the dense population object only;
neither closure regularity nor a trained finite-network tail estimate is
assumed. Ordinary strong `L2` continuity by itself does not assert (7).

## 2. The new proof mechanism

The complete constituent arguments are in
`GENERAL_GAUSSIAN_TRANSPORT.md` and
`GENERAL_REFERENCE_PROJECTION.md`, especially the latter's Sections 11--13.
Here the main deductions are collected in their logical order.

### Autonomous bounds before comparison

`OLD_CLOCK_ROUTE.md` proves global finite-width existence for every order,
bounded physical operator/RMS norms, bounded forward-history derivative
energies, and the exact physical identity

\[
 \dot{\widehat\theta}=F_n(\widehat\theta)+E_{n,P},\qquad
 \int_0^T\|E_{n,P}\|_{\rm sum}\,dt\le C_T/P,
 \qquad \int_0^T\|E_{n,P}\|_{\rm sum}^2dt\le C_T.
 \tag{8}
\]

The first and last blocks of `E` vanish. Its last displayed bound follows
from the proved squared clock-defect estimate and the bounded clock speed.
All constants are uniform on common initialized-operator/readout RMS
bounds, events with probability tending to one in the Gaussian model.
These bounds hold simultaneously for every order. They do not use a
stability assumption or a bound on the closure's backward derivatives.

The predictor differential is bounded in (4), so (8) implies
`integral |dot rho_hat|^2 <= C_T`. Hence the closure residual is
one-half Hölder in physical time, uniformly in order and width on those
events. If the label RMS is positive, the dense residual has a positive
lower bound on every fixed interval: `|dot rho_D| <= C_T rho_D`.
One can provisionally stop the comparison before the closure residual
leaves half that lower bound; the eventual error estimate excludes this
exit. Alternatively, `GENERAL_GEOMETRIC_STABILITY.md` derives the floor
directly for sufficiently large orders from (8).

### Dense tails give time regularity, without differentiating backward fields

For two physical states on the common ball, backward subtraction with the
second state as reference gives

\[
 \|\delta(\theta)-\delta(\vartheta)\|_{\rm RMS}
 \le C_T(1+M)d_n(\theta,\vartheta)+C_T H_\vartheta(M),
 \tag{9}
\]

where `H` is a sum of reference carrier RMS tails above `M`. The only
delicate term is bounded by

\[
 \|[\tanh'(z)-\tanh'(z_D)]c_D\|_{\rm RMS}
 \le 2M\|z-z_D\|_{\rm RMS}
       +\|c_D\mathbf1_{|c_D|>M}\|_{\rm RMS}.
\]

Descending through the network adds such terms and propagates them through
bounded operators. It yields one power of `M`, not `M^L`.

The dense parameter velocity is bounded in (4). Apply (9) at two dense
times and use (7). The residual-weighted backward source `a_D=r_D delta_D`
then satisfies, for `h=|t-s|`,

\[
 \|a_D(t)-a_D(s)\|_2
 \le C_T[(1+M)h+e^{-c_T M^2}]
 \le C_T h^{1/2},
 \tag{10}
\]

where the last step chooses `M` of size `sqrt(log(1/h))`; larger time
separations are covered by bounded source norms. In fact every Hölder
exponent strictly below one follows, but one-half suffices here.

### A half-derivative of additional approximation accuracy

At a fixed time put the dense histories into the *closure's* clock:

\[
 H(\xi)=h_D(t(\xi)),\qquad
 B(\xi)=\frac{r_D(t(\xi))\delta_D(t(\xi))}
                  {\widehat\rho(t(\xi))}.
 \tag{11}
\]

Use the common constant forward prefix and zero backward prefix. Since
`d xi = rho_hat dt`, their exact pairing is exactly the dense learned
matrix. Thus a different residual clock introduces no algebraic bias.

The forward history is `H1`. Equations (8), (10) and the residual floor
make the non-prefix part of `B` one-half Hölder in `xi`. Any initial
prefix jump has its explicit step-function projection estimate.

For a Hilbert-valued Hölder-`gamma` function, interpolate on `P` uniform
cells. Its `L2` interpolation error is `O(P^-gamma)` and its interpolant
has derivative `L2` norm `O(P^(1-gamma))`. The Legendre derivative bound
for that interpolant gives an `O(P^-gamma)` polynomial projection tail.
For a step, replacement by a ramp of width `tau/P` gives a
`O(P^-1/2)` tail by the same derivative inequality. Consequently

\[
 \|(I-\Pi_P)H\|_{L^2}\le C_T/P,
 \qquad \|(I-\Pi_P)B\|_{L^2}\le C_T/P^{1/2}.
 \tag{12}
\]

Orthogonality cancels both mixed terms of the paired projection. The
remaining matrix error is

\[
 \frac2m\sum_a\int
       (I-\Pi_P)B_a\otimes(I-\Pi_P)H_a\,d\xi,
 \tag{13}
\]

whose Hilbert--Schmidt norm is at most `C_T P^-3/2`. Here `u tensor v`
means `uv^T/n` at finite width. This is signed reference reconstruction
accuracy, not a claim that the actual velocity defect in (8) improved
at every hidden layer.

### Restore the full feedback without a backward projection supremum bound

For closure histories `b_hat,h_hat`, subtract the reference histories.
The exact splitting is

\[
 \begin{split}
 \int\Pi_P\widehat b\otimes\Pi_P\widehat h
          -\Pi_PB\otimes\Pi_PH
 ={}&\int(\widehat b-B)\otimes\Pi_P\widehat h
      +\int B\otimes(\widehat h-H)\\
 &-\int(I-\Pi_P)B\otimes(I-\Pi_P)(\widehat h-H).
 \end{split}
 \tag{14}
\]

The uniform `H1 -> L-infinity` bound for Legendre projection controls the
first integral, since the closure forward history has a uniform `H1`
bound. Clock substitution cancels its denominator. The second integral
is an ordinary integral of the state error. The last term is bounded by
`C_T P^-1/2 D(t)`, where `D(t)` is the running supremum state error;
absorb it for all sufficiently large orders. This avoids the false need
for a uniform supremum bound on projected backward histories.

Using (9) for the remaining nonlinear feedback gives, at cutoff `M`,

\[
 D(T)\le C_T e^{C_T M}
                  [P^{-3/2}+e^{-c_T M^2}].
 \tag{15}
\]

Choose `M` so that `exp(-c_T M^2)` is of order `P^-3/2`. This gives the
function `B_T` in (6). Its comparison with `C_T/P` is explicit:
`C sqrt(log P) - (1/2)log P` has a finite maximum. The residual first-exit
condition is then removed for large orders.

### Transfer through finite arrays rather than assume trained finite tails

Equation (15) cannot simply be applied to a trained finite network using
population tails. To bridge that distinction, sample the dense population
histories on a fixed physical-time mesh. Approximate the resulting finite
list of typed population fields by a finite union of Gaussian programs
on the canonical generated spaces. The maintained fixed-program theorem
preserves joint values, second moments and both orientations of each
reused initialized matrix.

Clip prescribed forward fields to `[-1,1]`, interpolate the sampled
features and sources, and reconstruct proof-only proxy parameters by
integrating their outer products exactly. If the time mesh is `Delta`,
choose the population nodal approximation error at most `Delta^2`.
Then the forward interpolation `H1` constants and source one-half Hölder
constants stay bounded as the mesh is refined. At fixed mesh, their
finite-array versions inherit those bounds by convergence of a finite
list of squared norms and contractions.

The proxy is generally not a solution of the dense ODE. Its discrepancy
from that ODE, and from its prescribed histories, tend to zero first with
width at fixed program and then with mesh refinement. Its carrier tails
are controlled by the dense population tails plus these vanishing errors.
Continuous quadratic majorants justify empirical tail bounds without any
assumption that limiting laws have no atoms. The proxy's learned adjoint
is pointwise bounded directly by its integral representation and the
clipped prescribed forward fields.

All these proxy errors are independent of memory order. Comparing both
the actual closure and actual finite dense flow with this same proxy
therefore gives, simultaneously for every `P>=P_0`,

\[
 \sup_{P\ge P_0}e_{n,P}(T)
 \le C_T e^{C_T M}
  [P_0^{-3/2}+e^{-c_T M^2}+\nu_\Delta+o_{\Pr}(1)],
 \quad \nu_\Delta\longrightarrow0.
 \tag{16}
\]

First take width large at fixed cutoff and fixed program, next refine
the mesh, and then use the cutoff selected for the fixed order threshold.
This proves (6). This proof uses no tail estimate for the actual trained
finite network and no estimate of derivatives of its backward history.

For (5), fix error and probability tolerances. Choose a fixed cutoff, a
fixed fine proxy, a sufficiently large width threshold and a sufficiently
large order threshold, in that order. Equation (16) controls every width
above that threshold and every larger order. At the finitely many remaining
widths, the original fixed-width theorem has a finite random constant;
enlarge the order threshold to control this finite list in probability.
This proves the stated supremum over *all* widths, without extracting a
rate for the finite-list completion.

If all labels vanish, the zero-readout population is stationary. At finite
width the readout norm cannot increase. The canonical small initialization
then controls all dense carriers in coordinate supremum on uniform
ordinary-readout-norm events. The direct Lipschitz comparison in
`GENERAL_REFERENCE_PROJECTION.md`, Section 8, gives the required conclusion
without dividing by a zero population residual.

### Further sharpening for the zero limiting readout

There is additional approximation slack under exactly the same dense tail
premise. This sharpening is proved separately in
`GENERAL_REFERENCE_PROJECTION.md`, Section 14. Optimize (10) to obtain the
stronger source modulus

\[
 \|a_D(t)-a_D(s)\|_2
   \le C_T |t-s|\sqrt{\log(eT_1/|t-s|)},\qquad T_1=\max(1,T).
 \tag{16a}
\]

Do not replace this modulus by the coarser one-half Hölder estimate. In the
closure clock, write `B=gA`, where `A` is the reparameterized source and
`g=1/rho_hat`. The source vanishes at the beginning of the history because
the limiting readout is zero. Extend `A` by zero and `g` constantly over
the prefix. Then `g` is a scalar `H1` function:

\[
 \int |g'(\xi)|^2d\xi
       =\int_0^t\frac{|\dot{\widehat\rho}(s)|^2}
                         {\widehat\rho(s)^5}ds\le C_T.
 \tag{16b}
\]

Interpolate only `A` on `P` uniform clock cells. Its approximation error
is `O(P^-1 sqrt(log(e+P)))`, its interpolant derivative norm is
`O(sqrt(log(e+P)))`, and its `L-infinity(time;L2)` norm is bounded.
The product rule for `g` times that interpolant and the Legendre derivative
bound therefore give

\[
 \|(I-\Pi_P)B\|_{L^2}\le C_T P^{-1}\sqrt{\log(e+P)}.
 \tag{16c}
\]

Together with the forward `P^-1` tail, the signed consistency error is
`O(P^-2 sqrt(log(e+P)))`. The same source modulus is preserved by the
finite sampled-history proxies: it is increasing and concave, and nodal
errors of size `Delta^2` do not increase its constant without bound.
The prefix sources of those proxies are exactly zero; the actual small
finite readout enters their vanishing recomputation mismatch.

Replacing the forcing term in (16) by this sharper expression and choosing
the cutoff of size `sqrt(2 log(e+P_0)/c_T)` proves (6) with the smaller
envelope

\[
 B_T^{\rm sharp}(P_0)
  =\frac{C_T\sqrt{\log(e+P_0)}}{P_0^2}
           \exp\!\bigl(C_T\sqrt{\log(e+P_0)}\bigr)
  \le C_{T,\gamma}P_0^{-\gamma}
       \quad\text{for every fixed }0<\gamma<2.
 \tag{16d}
\]

This is a **width-first** statement for the old clock, including arbitrary
fixed depth and correlated data. It proves neither the exact exponent two
nor a simultaneous finite-width rate. Its constants can deteriorate as
`gamma` approaches two. The coarser derivation above remains sufficient
for the original `C_T/P` endpoint.

## 3. Test functions and a useful simultaneous error-floor formulation

For every bounded test-input set `K`, the forward recurrence and common
operator/readout bounds give the following estimate on the common
initialization/physical-bound events, whose probabilities tend to one.
The constant is deterministic on those events; it is not asserted to
bound every Gaussian realization:

\[
 \sup_{x\in K}|\widehat f_{n,P}(t,x)-f_n^D(t,x)|
       \le C_{T,K}d_n(\widehat\theta_{n,P}(t),\theta_n^D(t)).
 \tag{17}
\]

Start at the first layer with the Lipschitz tanh bound times
`||x||/sqrt(d)`. At each later layer split the feature difference into
the propagated earlier difference and the changed matrix acting on a
bounded feature. At the readout apply Cauchy--Schwarz in RMS norms.
This proves (17), with no sampling of test points. For any probability
measure supported in `K`, its test-function `L2` discrepancy is at most
the supremum in (17). The two models' test RMSE against any fixed
square-integrable target differs by at most that same discrepancy.

There is also a precise way to combine a uniform order constant with a
vanishing finite-width floor. From (6), with an enlarged constant `C_T`,

\[
 a_n(T):=\sup_{P\ge1}\bigl(e_{n,P}(T)-C_T/P\bigr)_+
                    \longrightarrow0\quad\hbox{in probability}.
 \tag{18}
\]

To prove this, fix a tolerance and a sufficiently large integer `J`.
Equation (6) makes the entire tail `sup_(P>=J)e_(n,P)` smaller than that
tolerance in the width limit. The finitely many orders below `J` are
handled by (6) at each fixed threshold, taking a finite union of events.
Increase `C_T` to cover bounded small orders with the common physical
bounds. These two steps prove (18). Thus, simultaneously in `P`,

\[
 e_{n,P}(T)\le C_T/P+a_n(T),\qquad a_n(T)=o_{\Pr}(1).
 \tag{19}
\]

This is not a quantitative Monte Carlo estimate: (18) is a proof-level
finite-width error floor, and no power of `n` has been proved for it.
Using (16d), the same finite-head/tail proof works with `C_(T,gamma)/P^gamma`
for each fixed `0<gamma<2`, with a corresponding vanishing floor.
If `s_n(T,K)` denotes the dense network's error to its population
prediction, then (17)--(19) give

\[
 \sup_{t\le T,x\in K}|\widehat f_{n,P}(t,x)-f_\infty(t,x)|
 \le C_{T,K}/P+C_{T,K}a_n(T)+s_n(T,K).
 \tag{20}
\]

Equation (20) holds on the same common events as (17). Equation (19)
itself is pathwise for every realization by the definition (18).

On compact `K`, fixed-test convergence from the dense population theorem
upgrades to uniform test-input convergence using a finite input net and
the common predictor Lipschitz constant in `x`. That constant follows
from bounded first-row RMS, hidden operator norms and readout RMS. Thus
`s_n -> 0` in probability on the same dense regularity horizon. No
`n^-1/2` rate is silently assigned to either term in (20).

## 4. What this settles and what remains unresolved

This completes an arbitrary-fixed-depth, arbitrary-correlated-data
approximation result for the **fully autonomous original old-clock
closure**. All oracle inputs have disappeared from the implemented
algorithm. The Gaussian proxy is only an object in the proof. The result
supplies both qualitative uniform convergence over all widths and the
original `C_T/P` exponent in the width-first population approximation.

It does not yet prove the stronger simultaneous finite-width assertion

\[
 \sup_n\Pr\!\left\{\sup_{P\ge P_*}P e_{n,P}(T)>C_T(q)\right\}\le q
 \tag{21}
\]

with `P_*` and `C_T(q)` independent of width. The fixed-program transfer
in (16) is qualitative at fixed approximation resolution. Its width
threshold can depend on the desired memory order. The finite-list
completion proving (5) supplies no uniform bound on its scaled constants.
Removing the floor in (19) at the exact rate requires an additional
quantitative argument, not a relabeling of (6).

Nor does this prove the unchanged joint-clock `C_T/P^2` theorem uniformly
in width. Its original unnormalized speed, weighted projector and sharper
endpoint rate have separate unresolved estimates. The manuscript remains
unchanged.

## 5. Evidence and check scope

- `GENERAL_GAUSSIAN_TRANSPORT.md`: independent initial route, complete
  qualitative theorem and Gaussian proxy proof; later combined endpoint.
- `GENERAL_REFERENCE_PROJECTION.md`: independent reference projection
  route; Sections 11--13 implement the coordinator's Hölder reduction
  and the full endpoint transfer.
- `GENERAL_GEOMETRIC_STABILITY.md`: independent geometric route, positive
  top-link consistency theorem and diagnostics of the common-metric route.
- `GENERAL_UNIFORM_CONVERGENCE_CHECK.md`: completed separate check of the
  qualitative theorem and its exact quantifiers, against complete maintained
  C.1--C.2 and A.1--A.2. It does not certify later appended statements.
- `GENERAL_ENDPOINT_CHECK.md`: separate check of the appended endpoint
  construction and subsequent sharpenings; its recorded hashes define
  each check's scope.

The coordinator read the complete three route reports, the complete local
population/source arguments, the fixed-program specializations and the
fixed-program conditioning/common-action construction. Equations (18)--(20)
are additional coordinator deductions with their proofs above. Study
checks do not constitute promotion reviews or published external evidence.
