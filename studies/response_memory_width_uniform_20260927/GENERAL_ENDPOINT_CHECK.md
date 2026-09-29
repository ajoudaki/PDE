# Check of the width-first old-clock endpoint

28 September 2026. This is the coordinator's bounded check of the frozen
endpoint additions in `GENERAL_REFERENCE_PROJECTION.md`, Sections 11--13,
and `GENERAL_GAUSSIAN_TRANSPORT.md`, Section 7. Their required earlier
projection/comparison identities were read in full. The complete maintained
C.1--C.2 and A.1--A.2 dependencies had been read for the preceding check;
their scopes and formulas were checked again against this transfer. The
`solve-math-rigorously` skill was applied. No new research route, numerical
experiment, literature search, other study, or other review was used.

**Verdict: PASS for the width-first `C_T/P` statement, locally
unconditionally and on a prescribed longer horizon under the stated
dense Gaussian carrier-tail premise.** The half-Hölder source argument,
the actual-clock estimate, the signed reference projection error, the
absorbable remainder, and the full finite-program transfer are valid.
Neither dense-source bounded variation nor a trained finite-network
tail theorem is required.

The conclusion is

\[
 \forall P_0\ge1,\ \forall\zeta>0:\qquad
 \lim_{n\to\infty}\Pr\!\left\{
  \sup_{P\ge P_0}\sup_{t\le T}
       d_n(\widehat\theta_{n,P}(t),\theta_n^D(t))
                   >C_T/P_0+\zeta\right\}=0,
 \tag{1}
\]

for the original autonomous tanh old-clock closure, arbitrary fixed
depth and arbitrary fixed correlated finite data. The distance is
first-row RMS plus hidden Frobenius differences plus readout RMS.
The constant is deterministic and depends on the fixed data, depth,
horizon and stated dense/initialization bounds.

This is not a quantitative supremum over all widths, an expectation
bound, or a construction/identification of a fixed-order population
closure. The earlier qualitative all-width check remains separate and
unchanged. No unconditional arbitrary-horizon Gaussian tail extension
is established here.

## 1. Frozen inputs and clarifications

The checked Gaussian report hash is
`87cb947df965cca701dbe20d6179a74e49dad99a866fa7e40a145f06f5e6baeb`.
The initially checked reference-projection report hash was
`aa235b74c2958d7df3e1723cdd46d75f454b798939aba0728b1540a5512cca5b`.
Two small explanatory additions requested during this check were then
verified: its equation (59a), and the zero-label completion following
(66). The resulting full-file hash was
`26d16be936e6222850b0dd431300c85d46100246fae0e9085e7d0d3fd27ef4b0`.
That last file also contains an optional Section 14. It was outside
the initial endpoint check. The separately requested additional check
in Section 8 below now covers that optional section; the core `C/P`
verdict does not depend on it.

The additions clarify facts already available from the constructed
reference. First, its learned adjoint is pointwise bounded directly
because its prescribed forward history is clipped to `[-1,1]`.
Second, with all labels zero the entire error vanishes with the small
initial readout uniformly over memory orders, justifying even the
stronger envelope in reference equation (66). Their complete
justifications are included below.

## 2. Dense source regularity follows from dense tails

On the compact dense path, bounded forward/backward RMS norms and
hidden operator norms bound every parameter velocity in the stated
sum norm. For hidden blocks this uses the Hilbert--Schmidt identity
`||u tensor v||_(HS)=||u||_2||v||_2`; initialized operators cancel
from differences. Consequently the dense parameter path is Lipschitz.

The one-reference cutoff estimate applied to times `s,t` yields, for
the weighted backward source `a=r delta`,

\[
 \|a(t)-a(s)\|_{L^2}
 \le C[(1+M)|t-s|+e^{-cM^2}],\qquad M\ge1.
 \tag{2}
\]

Residuals are Lipschitz by the bounded predictor differential, so
multiplication by the residual does not weaken this bound. Choose
`M` proportional to `sqrt(log(e/|t-s|))`; the Gaussian tail is then
at most a fixed multiple of `|t-s|`, or of its square root. Since
`h sqrt(log(e/h))<=C sqrt(h)` on a bounded interval,

\[
 \|a(t)-a(s)\|_{L^2}\le C_T|t-s|^{1/2}.
 \tag{3}
\]

No backward time derivative and no product of two unbounded fields
was used. Dense forward histories are Lipschitz in `L2` by the
ordinary forward recurrence, hence have bounded `H1` seminorms.
The only additional probabilistic hypothesis in this step is the
stated marginal exponential-square bound for the full dense
carriers, uniformly in time. Maintained C.2 supplies it on its
local interval; it supplies no arbitrary-horizon version.

## 3. The actual closure clock has the required uniform regularity

The old-clock squared-defect estimate has the form

\[
 \int_0^T\frac{\|E_\ell(t)\|_F^2}{\widehat\rho(t)}dt\le I_\ell.
\]

Since `rho_hat<=Q`, summation over the fixed number of hidden links
gives `integral ||E||_sum^2<=C`. The actual forced equation and the
bounded predictor differential therefore give

\[
 \int_0^T|\dot{\widehat\rho}(t)|^2dt\le C.
\]

Thus the actual residual is half-Hölder, uniformly over widths and
orders on the common initialization event. The estimate for the
norm of the residual vector holds almost everywhere, including at
zero values, so no unjustified differentiation of a norm at zero
is needed.

For positive label RMS, the direct consistency-based lower bound

\[
 \widehat\rho(t)\ge\widehat\rho(0)e^{-2J^2T}
                         -J C_{\rm comp}/P
\]

gives a fixed positive floor for every sufficiently large order,
on one initialization event of probability tending to one. This
is independent of a tracking theorem. The alternative stopped
comparison in the reference report is also valid and removes its
stop by first exit.

The inverse clock is consequently Lipschitz. A bounded half-Hölder
source divided by this positive half-Hölder residual remains
half-Hölder; composition with the inverse clock preserves that
exponent. Forward `H1` energy transforms as

\[
 \int\|\partial_\xi H\|_2^2d\xi
       =\int\|\partial_t H\|_2^2/\widehat\rho\,dt\le C.
\]

These are deterministic estimates for every actual closure clock
on the good event. The transfer never applies a Gaussian-program
theorem to an order-dependent random clock or projector.

## 4. Projection and comparison algebra

For a Hilbert-valued `alpha`-Hölder path, piecewise linear
interpolation on `P` equal cells gives approximation error
`O(P^-alpha)` in time `L2` and derivative norm `O(P^(1-alpha))`.
Applying the Legendre `H1` error bound to this interpolant proves
the same `O(P^-alpha)` polynomial projection error. Constant
components are reproduced exactly. A possible prefix jump adds
`O(P^-1/2)` through the independently proved step estimate.

Thus the actual-clock prescribed forward and backward histories
satisfy

\[
 \|(I-\Pi_P)H\|_{L^2_\xi L^2}\le C/P,
 \qquad
 \|(I-\Pi_P)B\|_{L^2_\xi L^2}\le C/P^{1/2}.
\]

Projection orthogonality then gives a signed reference matrix
error of order `P^-3/2`. This is a same-reference reconstruction
estimate. It is not asserted to improve the actual closure's
absolute accumulated velocity defect to that order.

The decisive exact product splitting is

\[
 \begin{split}
 \int\Pi\widehat b\otimes\Pi\widehat h-Pi B\otimes\Pi H
 ={}&\int(\widehat b-B)\otimes\Pi\widehat h
       +\int B\otimes(\widehat h-H)\\
 &-\int(I-\Pi)B\otimes(I-\Pi)(\widehat h-H).
 \end{split}
\]

The actual forward projection has a uniform Hilbert-valued
`L-infinity`-in-time bound from its proved `H1` history estimate.
The first term is therefore an `L1` physical-time source
discrepancy: `d xi=rho_hat dt` cancels the denominator in the
backward history. The second term has the same `L1` structure.
The last term is at most `C P^-1/2` times the supremum parameter
error, plus the prescribed/reference forward mismatch. It is
absorbed at large order. No pointwise bound for a projected
backward history is required.

At a fixed carrier cutoff, this produces

\[
 D(t)\le CP^{-3/2}+CP^{-1/2}D(t)+C\eta
       +C\int_0^t[(1+M)D(s)+e^{-cM^2}]ds,
 \tag{4}
\]

where `eta` collects only prescribed-reference discrepancies.
The coefficient of `M` stays affine through arbitrary fixed
depth by the descending one-reference subtraction. The input
Gram may be singular throughout.

## 5. Two-stage finite-program transfer

The Gaussian report uses a coarse history mesh `h` and a fine
program mesh `Delta`. The reference report instead chooses a
finite program approximating all sampled dense nodes to an
explicit error `epsilon=h^2`. Both are valid realizations of the
same finite approximation procedure.

Fix `h` first. The finitely many dense forward/source samples
belong to the canonical generated `L2` spaces. They can be
approximated simultaneously by one finite union of allowed
programs. Alternatively, population Euler convergence and
backward continuity supply these approximating nodes as the
program mesh tends to zero. Both constructions preserve the
same initialized operators and their true adjoints. Clip forward
nodes to `[-1,1]`, which cannot increase their error from tanh
features. Use exact initial forward nodes and zero initial
weighted sources. Finite small-readout discrepancies are retained
as a vanishing initialization/mismatch error.

At the population level, nodal error `epsilon` increases the
forward interpolant derivative norm by at most
`2 sqrt(T) epsilon/h`, and the source half-Hölder seminorm by at
most `C epsilon/sqrt(h)`. Choosing `epsilon=h^2` gives uniform
constants. In the two-mesh formulation, choosing the program
mesh sufficiently fine at each fixed history mesh has the same
effect.

These finite temporal norms transfer at fixed programs: the
forward energy is a finite sum of empirical squared nodal
differences divided by cell lengths; a source Hölder bound
follows from the maximum of finitely many nodal difference
quotients and the elementary interpolation estimate. Their
second moments converge by A.1. Width is taken large only after
the history mesh and program approximation have been fixed.
No convergence uniform in program length is required or claimed.

Define reference parameters by exact integrals of the prescribed
histories. A product of two affine histories integrates to the
displayed cubic combination of four rank-one tensors. Thus the
hidden history identity is exact, finite rank, and correctly
typed. Neither numerical quadrature nor an implicit reference
ODE is involved.

The reference learned adjoint is pointwise bounded directly:

\[
 \|(W_\ell^R-W_{0,\ell})^*v\|_\infty
 \le\frac2m\sum_a\int_0^t\|A_{\ell,a}(s)\|_2\|v\|_2ds,
\]

because the prescribed forward coordinates have absolute value
at most one. This justifies applying the initialized-carrier
version of the source subtraction even though the prescribed
source is not identically the recomputed `r delta`. The top
readout increment has the analogous pointwise bound. The
Gaussian report can instead use full carrier tails throughout;
that is also valid.

At a fixed reference time, append recomputed network evaluations
to the same finite program. A proxy action differs from the
prescribed action only by finitely many terms

\[
 u_n(v_n^Tz_n/n-\mathbb E[VZ]).
\]

Each tends to zero in RMS at fixed program. Backward
recomputation uses a cutoff against the appended reference
nodes, as in C.1. Rank-one differences turn these field
consistency estimates into Frobenius parameter-velocity
consistency. No empirical higher moments or unproved finite
scalar-feedback derivative formula is needed.

Population reference parameters converge in the sum norm to the
dense path because their prescribed sources converge and the
rank-one integrals converge in Hilbert--Schmidt norm. The
recomputed reference carriers consequently converge uniformly
in `L2`, using the dense cutoff estimate. Tail transfer at a
fixed cutoff produces a dense Gaussian tail plus a vanishing
reference approximation error. At finite width, continuous
quadratic tail majorants make this a legitimate A.1 observation
even if a limiting carrier has an atom at a cutoff.

The node-only argument in the Gaussian report is sufficient:
within a history cell, bounded reference parameter speed costs
`O(h)`, and interpolated prescribed histories move by at most
`O(sqrt(h))`. Apply the one-reference estimate against the
preceding reference node; no actual finite trained tail between
nodes is used. The reference report's stronger uniform-time
recomputation statement is also justified by a separate finite
time net, reference cutoff, and bounded proxy speed. Either
version closes (4).

## 6. Endpoint constants, order supremum, and limit order

All initialization events, finite-program observations,
regularity estimates and reference mismatches above are
independent of memory order. The actual closure's physical
bounds, residual floor and squared-defect bounds hold
simultaneously for all orders beyond one fixed threshold.
Consequently absorption in (4) gives one estimate for the
supremum over every `P>=P_0`, without a union bound over orders.

Comparing the actual finite dense flow to the same reference
uses its exact integral equation and gives the same inequality
without the projection-error terms. The triangle inequality
therefore yields

\[
 \sup_{P\ge P_0}e_{n,P}
 \le Ce^{C(1+M)T}
   [P_0^{-3/2}+e^{-cM^2}+\eta_{n,h,\Delta,M}],
 \tag{5}
\]

with, for example,

\[
 \eta_{n,h,\Delta,M}
   \le C(1+M)\sqrt h+q_h+q_{h,\Delta}+o_{\Pr}(1).
\]

Here `q_h->0`, `q_(h,Delta)->0` as the program mesh tends to
zero for each fixed history mesh, and the random term tends to
zero at fixed meshes and cutoff. Its lack of a quantitative
width rate is harmless for the claimed limit order.

For each fixed sufficiently large `P_0`, choose
`M=max(1,sqrt((3/(2c))log(e+P_0)))`. Take width to infinity
with both meshes and cutoff fixed, then refine the program
approximation at fixed history mesh, then refine the history
mesh. Equation (5) gives the stronger large-order envelope

\[
 C P_0^{-3/2}e^{C_T\sqrt{\log(e+P_0)}}\le C_T'/P_0.
\]

The inequality follows because
`C_T sqrt(log(e+P_0))-(1/2)log P_0` is bounded above.
Each prescribed threshold margin `zeta>0` permits all reference
errors to be chosen below it in this ordered fashion. The
width threshold may depend on `P_0`, which is permitted by
(1). Enlarging `C_T` covers the finitely many orders below
the residual/absorption threshold using the uniform physical
increment bounds on high-probability initialization events.

If the stopped residual argument is used, first take `P_0`
large enough that the envelope is below its fixed stopping
margin. The same reference errors can then be chosen within
the remaining margin; the estimate excludes each stopped
exit on the same event. The alternative direct residual floor
already avoids this stopping step.

## 7. Zero labels and precise remaining boundaries

When all labels vanish, the actual and dense readout RMS
never exceeds `R=||w_0||_2/sqrt(n)`. On bounded initialized
operator events, the backward RMS bounds are `O(R)`,
uniformly in order. The residual is at most `R`, so
first-row increments are `O(R^2)`, readout increments are
`O(R)`, and dense hidden increments are `O(R^2)`.
Projection contraction bounds the closure hidden
Hilbert--Schmidt increments by

\[
 2\sqrt{(1+TR)TR}\,\beta_\ell=O(R^{3/2}).
\]

Canonical small readout has `R->0` in probability. Hence
`sup_(P>=1)e_(n,P)->0` in probability, which covers both
(1) and the stronger fixed-`P_0` envelope, without dividing
by a zero limiting residual. The separate direct `C/P`
estimate in reference Section 8 is also valid.

No substantive proof gap remains in the checked endpoint.
Its local Gaussian source bounds are established by
maintained C.1--C.2. A longer horizon still needs the stated
dense marginal Gaussian carrier-tail bound, or the sufficient
bounded source-response representation from the Gaussian
report. The finite-program construction gives no all-width
quantitative rate and does not identify a fixed-order
population closure. The optional stronger exponents and the
coordinator's error-floor deduction have separate checks below;
neither is needed for the central `C/P` result.

## 8. Separate check: the optional exponent below two

**PASS for reference-projection Section 14, equations (67)--(73),
with its stated zero limiting readout and width-first quantifiers.**
This section was checked after the central endpoint review was
completed. Its full reference-file hash is
`db29db73c99b309d77f8233c4e0e1b3060ba8905588a7a893ddc9ccbf177801c`.
The coordinator synthesis has hash
`8ea4888e9874250e8386f32c492781dbc111fceda17ad5afc4e77a1b6980e735`;
its equations (16a)--(16d) make the same deductions and pass.

The additional verdict and its decisive calculations were sent to
the coordinator before reading the Gaussian report's later Section 8,
which records a separate analytic check of the same sharpening.
That subsequent Gaussian report has hash
`004a7b6ed9ec193fd906e336a82baa7d456098925fe209e17d947ba21d7d93d5`.
It introduced no new step into the check below. These are shared
internal checks, not independent promotion reviews.

Optimizing (2) with the Gaussian tail of order `h` yields
`||a(t)-a(s)||<=C psi(|t-s|)`, where

\[
 \psi(h)=h\sqrt{\log(eT_1/h)},\qquad T_1=\max(1,T).
\]

On its stated domain this function is increasing and concave,
and `psi(h)/h` decreases. Thus piecewise linear interpolation
preserves this modulus up to an absolute factor. An interpolated
nodal error bounded by `epsilon` has increments at most
`min(2epsilon,2epsilon h/Delta)`; comparison with `psi(h)` gives
modulus constant `2epsilon/psi(Delta)`. The chosen
`epsilon=Delta^2` keeps this bounded under refinement.
At fixed meshes, finite nodal difference observations transfer
the modulus to finite program histories. No new finite-width
regularity theorem is required.

Write the reference backward history as `B=gA`, where
`g=1/rho_hat` in clock coordinates. Its derivative and energy
are exactly

\[
 g'(\xi)=-\frac{\dot{\widehat\rho}(t(\xi))}
                    {\widehat\rho(t(\xi))^3},\qquad
 \int|g'|^2d\xi
       =\int\frac{|\dot{\widehat\rho}|^2}{\widehat\rho^5}dt.
\]

The derived residual floor and physical `H1` bound control this
energy. Constant extension over the prefix is continuous. The
source `A` has zero initial value, since the limiting readout
is zero and the prescribed proxy's initial source is exactly
zero. Its zero prefix therefore has the same modulus without
a jump. This zero-prefix condition is essential.

Interpolate only `A` on `P` equal clock cells. The cell estimates
give

\[
 \|A-A_P\|_{L^2}\le CP^{-1}\sqrt{\log(e+P)},\quad
 \|A_P'\|_{L^2}\le C\sqrt{\log(e+P)},\quad
 \|A_P\|_{L^\infty(L^2)}\le C.
\]

The scalar-Hilbert product `gA_P` belongs to `H1`, with

\[
 \|(gA_P)'\|_{L^2}
 \le\|g\|_\infty\|A_P'\|_{L^2}
       +\|A_P\|_{L^\infty(L^2)}\|g'\|_{L^2}
 \le C\sqrt{\log(e+P)}.
\]

Legendre best approximation applied to this product proves
the improved backward tail `CP^-1 sqrt(log(e+P))`. This does
not assign a better pointwise Hölder exponent to `g`; it uses
the stronger scalar `H1` information directly.

Pairing with the forward `P^-1` tail yields signed consistency
`CP^-2 sqrt(log(e+P))`. The absorbable coefficient becomes
`CP^-1 sqrt(log(e+P))`, which tends to zero and decreases for
positive integer orders. The preceding finite-program comparison
and limit order are unchanged. Selecting the Gaussian cutoff
with squared size proportional to `2 log P` gives

\[
 B_{**}(P_0)=CP_0^{-2}\sqrt{\log(e+P_0)}
                    e^{C_T\sqrt{\log(e+P_0)}}.
\]

For every fixed `0<gamma<2`, its ratio to `P_0^-gamma` is
bounded: the negative term `-(2-gamma)log P_0` dominates
both `sqrt(log P_0)` and `log log P_0`. This proves the
asserted width-first `C_(T,gamma)P_0^-gamma` envelope.
It does not prove the exact exponent two. Nonzero limiting
readout would restore the prefix jump; the stated canonical
zero or vanishing stored-readout regime avoids that jump
through its prescribed zero initial source and vanishing
proxy mismatch.

## 9. Separate check: the simultaneous width floor and test inputs

**PASS for synthesis equations (18)--(20), including the now
explicit high-probability qualification on prediction bounds.**
The checked synthesis hash is recorded in Section 8. The
parameter-floor inequality itself is pathwise by definition.

Take one deterministic constant `C_T` large enough for the
width-first `C_T/P_0` envelope at every fixed threshold,
including the finite list of small thresholds. Define

\[
 a_n=\sup_{P\ge1}(e_{n,P}-C_T/P)_+.
\]

This is measurable because the orders are countable. It is
finite almost surely because all physical increments have a
bound independent of order at each finite initialized network.
For a tolerance `eta>0`, choose `J` so large that
`C_T/J<eta/2`. On the tail,

\[
 \Pr\{\sup_{P\ge J}(e_{n,P}-C_T/P)_+>\eta\}
 \le\Pr\{\sup_{P\ge J}e_{n,P}>\eta\}\longrightarrow0.
\]

For every fixed `P<J`, the width-first theorem gives
`Pr{e_(n,P)>C_T/P+eta}->0`. A finite union controls the
head. These two statements prove `a_n->0` in probability.
The simultaneous inequality `e_(n,P)<=C_T/P+a_n` is then
immediate from its definition. The same argument works with
`C_(T,gamma)/P^gamma` for any fixed checked exponent
`0<gamma<2`. This floor has no quantitative width rate and
does not remove the floor at the scale `1/P` for growing orders.

For test inputs, first-row discrepancy is bounded by
`(||Delta W_1||_F/sqrt(n)) ||x||/sqrt(d)`. Repeating the
forward recurrence and the readout Cauchy--Schwarz inequality
gives the synthesis's uniform bound on every bounded test set
`K`. On the common initialized events its constant is
deterministic and independent of width/order. Gaussian
operator norms are unbounded over all realizations, so this
fixed prediction constant is asserted on those events, whose
probabilities tend to one. The synthesis now states this
qualification explicitly for equations (17) and (20).

The dense finite predictor has an input Lipschitz constant
bounded by

\[
 \frac{\|w\|_2}{\sqrt n}
       \left(\prod_{\ell=2}^L\|W_\ell\|_{\rm op}\right)
       \frac{\|W_1\|_F}{\sqrt{nd}}.
\]

The physical estimates and first-row Gaussian concentration
bound this on the same high-probability events. The population
predictor has the corresponding finite bound. Fixed test-input
queries are appended as passive forward observations to the
same finite Gaussian programs; they add no training residuals.
Their initial projections can be obtained from the finite
first-row root tuple, without inverting the training Gram.
Thus the maintained local theorem, or the conditional
longer-horizon proxy argument, gives convergence uniform in
training time for any fixed finite test set.

For a compact `K`, choose a finite input net. The maximal
prediction error over `K` is at most the maximal error over
that finite net plus the sum of the two predictor Lipschitz
constants times the net radius. First choose the radius,
then take width to infinity. This proves the asserted dense
test error `s_n(T,K)->0` in probability. Combining it with
the parameter floor yields synthesis (20) on the same
high-probability events. The test-law `L2` and RMSE transfers
follow from the supremum bound and reverse triangle inequality.
No Monte Carlo rate or independent replacement of test roots
is implicit.
