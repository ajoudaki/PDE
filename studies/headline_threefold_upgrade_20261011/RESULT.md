# Threefold headline upgrade: proved additions and precise limits

2026-10-11. This is a joint research packet, not a manuscript modification or
a promoted theorem. The paper and maintained book are unchanged.

## Bottom line

The requested threefold upgrade is **not established under the claimed sole
addition of nonaffine activations**. The current target is unambiguously
compression error divided by dense discrepancy, taking a separate spatial
supremum in each before division, and then a positive-time supremum. Taylor's
revised domain is a nonempty test-only panel, now with test directions
nonparallel to the training directions. The earlier training-only and
antipodal-panel objections do not apply to this more restrictive domain.

The user's nonlinear-rank argument is correct at initialization. Under
pairwise nonparallel directions, the augmented training-and-test feature Gram
is positive definite at every hidden layer, even when the training inputs
span the whole input space. This now yields a fixed-test derivative lower
bound and a simultaneous near-zero lower bound. It does **not** by itself
prove persistence through training or at the fitted endpoint.

The subsequent circle-supremum investigation makes quantitative progress
without closing that endpoint gap: it proves a width-independent trained
probe readout signal and finite-width generic-label nonconstancy of the
actual fitted predictor. It does not yet prove the actual dense-copy
circle discrepancy has size `n^(-1/2)`. No counterexample to that target
was found. The precise results, qualifications and checks are collected
in [CIRCLE_ENDPOINT_RESULT.md](CIRCLE_ENDPOINT_RESULT.md).

There is also a checked obstruction to a universal same-time lower bound:
for one admissible, genuinely nonlinear two-layer problem with a nonparallel
single-test panel, two fully trained dense predictions cross at a positive
time with probability bounded away from zero as width grows. Thus the
requested all-time Taylor statement fails under the current zero-denominator
failure convention. This is not a counterexample to the whole-sphere version,
the endpoint lower theorem, or the paper's existing ratio of trajectory norms.

The positive additions, without increasing the headline storage, are:

1. All three compression errors have the missing initial-time factor
   \(\min\{t,1\}\).
2. A real-node interpolation initializer for the current Taylor family has
   near-quadratic exact-real setup work. Harmonic's earlier near-quadratic
   initializer transfers to the current source tolerance. Neither needs
   high-order source derivatives as an oracle.
3. The endpoint lower bound extends from an orthogonal query to **any fixed
   query outside the training span**, with the same activation class and label
   cap. It does not yet cover arbitrary full-span training configurations.
4. The newly authorized quantitative dependencies close the polynomial
   Legendre and Taylor source-event width gates. Their deterministic repairs
   and probability estimates are now assembled and checked.
5. The initial dense lower bound now holds at any fixed nonparallel test
   input, with no off-training-span restriction. This supplies the near-zero
   same-time comparison also on the revised Taylor test-only panel.

For Harmonic there is a new, precisely limited obstruction: with the unchanged
coordinate-source construction and displayed storage bound, an onset polynomial
jointly in inverse gap and inverse labels cannot hold uniformly over the full
small-label range, even at fixed dimension. This does **not** disprove a
fixed-positive-label statement or a different output-only construction.

| Requested upgrade | Status of this packet |
|---|---|
| Pointwise query quotient, with only nonaffinity added | Not well-defined throughout the proposed domain under the current zero-denominator failure convention; exact separated tanh zeros persist for every positive time. |
| Separate spatial suprema, then simultaneous same-time relative error | Fails for general allowed Taylor test panels under the zero-denominator failure convention: an actual-network singleton-panel crossing has nonvanishing probability. The whole-sphere version is not disproved. |
| Correct near-zero compression upper bounds | Proved for all three original runtime constructions, with unchanged retained-state orders. |
| Nonparallel fixed-test initial lower bound | Proved, including full-span training; it gives a simultaneous interval of length proportional to \(1/(\sqrt n\log(en))\), not the whole pre-endpoint interval. |
| Late same-time comparison including the endpoint | Follows if the query domain contains a fixed point outside the training span; onset remains unquantified. |
| Remove off-span endpoint qualification | Not closed. New exact endpoint and compensated-neuron arguments establish qualitative noncancellation on the sphere, but not a width-uniform fluctuation scale or its transfer to the actual network. |
| Polynomial Legendre/Taylor width onset | Deterministic and source-probability repairs checked for the existing trajectory-norm headline. This does not supply a polynomial same-time or endpoint lower event. |
| Polynomial Harmonic onset at fixed dimension | Impossible uniformly in inverse gap and inverse labels for the unchanged source interface and count. Fixed positive label-to-gap ratio is not settled. |
| Efficient supplied-dense setup | Exact-real arithmetic result, conditional on the existing source event; not a finite-bit implementation theorem. |

## Common setup and what “same time” means

Use exactly the Gaussian-initialized canonical network in `paper/compact.tex`:
width \(n\), \(L\ge2\) hidden layers, \(m\ge2\) training inputs in
\(\mathbb R^d\) of norm \(\sqrt d\), zero initial readout, scalar output
\(w^\top h^{(L)}/n\), squared loss \(m^{-1}\sum_a(f(x_a)-y_a)^2\),
and block mobilities \((n,1,\ldots,1,n)\). The population feature Gram has
gap \(\gamma>0\). Its label scale is \(Y=\|y\|_2/\sqrt m>0\).
The unchanged sufficient cap is

\[
m/\gamma\ge1,\qquad
0<Y\le(\gamma/m)\beta^{-30L}.
\]

Each layer activation is real on the real axis, holomorphic in a common
horizontal strip, and has bounded first derivative there. Its values may be
unbounded. The definition of \(\beta\) is unchanged. Nonaffinity in every
layer is required for the imported endpoint lower theorem, not for the new
compression upper estimates or setup bridge. All problem parameters are fixed
separately as \(n\to\infty\); “similar size” does not identify any of them.

Write \(\mathcal X\) for the sphere for Legendre/Harmonic, or, for the
user's revised Taylor comparison, the \(p\ge1\) declared test inputs alone.
Taylor's construction still uses all \(m+p\) inputs, with labels only on
the \(m\) training inputs. For the current nonlinear-rank route, training
directions are pairwise nonparallel and a selected test is nonparallel to
every training direction. At fixed finite geometry this entails positive
separation from both training inputs and their antipodes; its size may enter
lower-bound constants. Define

\[
E_n(t)=\sup_{x\in\mathcal X}|f_{\rm model}(t,x)-f_n(t,x)|,
\qquad
D_n(t)=\sup_{x\in\mathcal X}|f_n(t,x)-\widetilde f_n(t,x)|,
\]

where the two dense runs are independent on the same data. The working
statement is \(\sup_{t\in(0,\infty]}E_n(t)/D_n(t)\to0\) in
probability. It is not the already established
\((\sup_t E_n(t))/(\sup_t D_n(t))\to0\). Time zero is excluded
because every predictor starts at zero. At a zero denominator we retain the
paper's failure convention; defining zero/zero differently would change the
target. The current user display confirms this direction and placement.

For clarity, the paper's existing Taylor relative-error theorem uses the
combined training-and-test domain. Restricting its numerator to tests preserves
the upper bound; restricting its denominator does not preserve the lower bound.
The polynomial-width result below concerns the original trajectory-norm
headline, not an unproved replacement of its denominator by a test-only norm.

Every probability statement below concerns each sufficiently large individual
width at fixed confidence. No simultaneous event over independent widths is
claimed. Constants \(C\) in headline displays depend only on activations and
depth; numerical and problem-dependent coefficients are exposed in the proof
modules.

## 1. Initial-time comparison at unchanged storage

On the existing fitting/source event, simultaneously for all times including
the fitted limit,

\[
\begin{aligned}
E_n(t)&\le
\frac{CY}{\sqrt n[\log(en)]^3}\min\{t,1\}
&&\text{Legendre},\\
E_n(t)&\le\frac{CY}{n}\min\{t,1\}
&&\text{Harmonic and Taylor}.
\end{aligned}                                                    \tag{1}
\]

For Legendre, the proof retains the **elapsed residual-clock activity** in
the terminal forward-history projection tail. The original absorption and
signed stability estimates then preserve this factor. No change to its clock,
optimizer or order is required.

For the selected methods, the exact readout starts at zero. Integrating its
source-pairing error only up to time \(t\) yields a factor \(Yt\).
Retaining this factor through the readout--deficit cancellation gives (1).
No derivative of a source-approximation error is taken. This is important for
both the original jet compiler and the new interpolation compiler.

Complete proof and bounded adversarial reconstruction:
[EARLY_ERROR_BOUNDS.md](EARLY_ERROR_BOUNDS.md),
[EARLY_ERROR_CHECK.md](EARLY_ERROR_CHECK.md).

### What the dense lower bounds actually permit

The original initial-derivative witness was a training input. The new
nonparallel-query argument removes that limitation. For any fixed test
\(x\) nonparallel to every training input, and each fixed confidence,
there is \(c_\delta>0\) such that eventually, with probability at least
\(1-\delta\),

\[
|f_n(t,x)-\widetilde f_n(t,x)|
\ge \frac{c_\delta Yt}{2\sqrt n}
\quad\text{for every }0<t\le t_n,
\qquad
t_n=\min\left\{
\frac{m}{2\gamma\sqrt{\log(en)}},
\frac{c_\delta m}{128\beta^{6L}\gamma\sqrt n\log(en)}
\right\}.                                                     \tag{2}
\]

The coefficient can depend on the fixed augmented geometry, depth,
activations and confidence, but not width or time. Width onset remains
eventual and unquantified here. The label vector is fixed before
initialization; the event is not simultaneous over all label choices.
Combining (2) with (1) proves the same-time ratio on this interval, with
bounds \(2C/(c_\delta[\log(en)]^3)\) for Legendre and
\(2C/(c_\delta\sqrt n)\) for Harmonic/Taylor. This applies to a
nonempty test-only panel as well as the sphere. At fixed problem and
confidence, \(t_n\) has order \(1/(\sqrt n\log(en))\).

The proof also establishes initialized augmented full column rank almost
surely at every layer for \(n\ge m+1\). It needs a nonaffine first
activation and nonconstant later activations in the existing analytic class;
activation values may be unbounded. The rank and derivative statements need
no label cap; the time interval uses the existing source event and original
cap. See [NONPARALLEL_INITIAL_VARIABILITY.md](NONPARALLEL_INITIAL_VARIABILITY.md)
and its [reconstruction](NONPARALLEL_INITIAL_CHECK.md).

The endpoint lower theorem has a different scope: the query domain must
contain a fixed query outside the training span. Orthogonality has now been
removed. Under layerwise nonaffinity, that theorem gives a fitted discrepancy
at least \(c_\delta/\sqrt n\), eventually at confidence \(1-\delta\).
Dense fitting tails then give the same-time comparison uniformly for

\[
t\ge\frac{2m}{\gamma}\log(en),\qquad\text{including }t=\infty.
\]

Both the coefficient and onset in this endpoint input can depend on all
fixed problem parameters. They are not quantified polynomially by this study.
There is an uncontrolled interval between the near-zero and late windows.
An endpoint result and a positive-time witness do not close that interval.

The deterministic window arguments and exact missing sufficient lower bound
are in [TIME_COMPARISON.md](TIME_COMPARISON.md). The fitted-panel
counterexamples and the distinction between fixed-time and uniform-time limits
are proved in [UNIFORM_TIME_SCOPE.md](UNIFORM_TIME_SCOPE.md), with the revised
test-only and quotient-placement analysis in
[QUERY_RATIO_SCOPE.md](QUERY_RATIO_SCOPE.md) and its independent check
[QUERY_RATIO_CHECK.md](QUERY_RATIO_CHECK.md). The new off-span endpoint
argument is in [TEST_PANEL_DENSE_ROUTE.md](TEST_PANEL_DENSE_ROUTE.md), Section 2.
Its conditioning, layer recursion, and transfer to the actual fitted network
are reconstructed in [OFF_SPAN_ENDPOINT_CHECK.md](OFF_SPAN_ENDPOINT_CHECK.md).
That note also gives a fixed-test crossing theorem for a frozen-feature
comparator, not the actual fully trained nonlinear network. The separate new
proof [ACTUAL_TIME_BRIDGE.md](ACTUAL_TIME_BRIDGE.md) changes the lower
activation and supplies an actual-flow bridge, independently reconstructed in
[ACTUAL_TIME_BRIDGE_CHECK.md](ACTUAL_TIME_BRIDGE_CHECK.md). The deterministic
window calculation is checked in
[TIME_COMPARISON_CHECK.md](TIME_COMPARISON_CHECK.md).

### Why the whole pre-endpoint interval cannot have a universal lower profile

The checked actual-network example has \(m=d=L=2\), normalized training
inputs \(e_1,e_2\), test \((e_1+e_2)/\sqrt2\), layer activations
\(z+\tanh z\) and \(\tanh z\), and labels \(Y(1,-1)\).
Both activations satisfy the paper's class and are nonaffine. The augmented
feature Gram is positive definite. Choose one strictly positive \(Y\),
independent of width, within the original small-label cap as in the proof.
There is \(\eta>0\), independent of width, for which

\[
\liminf_{n\to\infty}\Pr\left\{
f_n(1,x)>\widetilde f_n(1,x),\quad
f_n(2,x)<\widetilde f_n(2,x)
\right\}\ge\eta.                                             \tag{3}
\]

Continuity forces a dense crossing in \((1,2)\), which is contained in
\((0,(2m/\gamma)\log(en))\) eventually. On the singleton test panel,
the separate spatial supremum in the denominator is then exactly zero.
Nonparallel geometry and initialized full rank do not prevent this scalar
crossing. The proof evolves every parameter block of both networks. A frozen
comparator is used only together with a proved centered remainder variance
bound \(C Y^6/n\), not as a replacement for feature learning.

Under the current failure convention, (3) rules out the requested universal
all-time ratio. If zero-denominator times are instead omitted, the conclusion
needs a numerator argument. [ACTUAL_CROSSING_QUOTIENT.md](ACTUAL_CROSSING_QUOTIENT.md)
shows that a nonexact analytic compressed predictor, independent of the
second dense initialization, almost surely has nonzero error at these
crossings, so its quotient genuinely diverges nearby. Analyticity and
nonexactness of the particular selected Taylor predictor are **not** established
by that conditional strengthening. No convention-independent counterexample
for that specific construction is claimed here.

This singleton result does not make the sphere supremum vanish and does not
settle the Legendre/Harmonic whole-sphere same-time question. It also says
nothing negative about the fitted endpoint: crossing occurs at intermediate
positive time. The paper's existing complete-trajectory denominator stays
positive on (3), so its headline comparison is not contradicted.

### Why initial full rank does not yet remove the endpoint restriction

The new rank argument is not being discarded: it proves positive initialized
query innovation relative to the **initialized training-feature span**.
The endpoint proof conditions on a larger space of vectors generated during
training. Distance from that larger space can be smaller, even zero, so
the initialized Schur complement is not a lower bound for the remaining
conditional query variance.

[NONPARALLEL_ENDPOINT_ROUTE.md](NONPARALLEL_ENDPOINT_ROUTE.md) gives a
precise conditional restart from the second hidden layer. It would suffice
that the normalized query-feature distance from that larger training-source
space stay bounded away from zero in probability. This is an explicit
remaining obligation, not an extra hypothesis being silently added to a
claimed solution. No general full-span endpoint lower theorem is asserted.

### Further endpoint investigation under the unchanged label cap

The new [endpoint separation report](ENDPOINT_SEPARATION_RESULT.md) records
two additional routes, without substituting a frozen-feature predictor.
One derives an exact fitted residual decomposition and its local cubic label
coefficient. The other includes the full compensating response to a trained
probe neuron and proves that its sphere covariance has infinite rank on
each open patch, at each successful finite-width cavity. Its variance is
positive at almost every query, with no input-span restriction.

Neither is yet the required dense endpoint lower bound. The nonzero
covariance eigenvalues have no width-uniform lower estimate, and a
collective fluctuation argument transferring infinitesimal insertion to the
actual network remains missing. These conclusions therefore do not remove
the off-span qualification above. They do not disprove its removal under
positive separation from training directions and their antipodes either.

## 2. Width conditions: separate structural gates from probability gates

The prior Legendre repair gives a sharper \(q^{-3}\) forcing estimate for
the same closure, at the same prescribed order, and polynomial structural
gates. Taylor uses a capped analytic radius and a repaired deterministic
prefix mesh, preserving its optimizer and headline storage powers. The
inverse-label gate used to simplify the Taylor count remains explicit;
it is not confused with a source-event gate.

Those routes compare to a weaker, polynomially quantitative lower bound for
the **trajectory supremum**, sufficient for the existing headline comparison.
They neither prove polynomial onset of the paper's sharper dense coefficient
nor supply a polynomial same-time or endpoint lower event.

After the user's authorization, the three raw quantitative dependencies were
read and their recurrences checked. The explicit source gates are polynomial
in \(\beta^L,m,d,m/\gamma,\delta^{-1}\), and also \(p\) for Taylor.
Taylor's separate storage-simplification gate is polynomial in \(Y^{-1}\)
as well. This is not polynomial dependence on \(L\) separately.
The Legendre proof uses a smaller confidence-dependent analytic rectangle;
Taylor uses its capped radius and deterministic level-mesh repair. Both
preserve the prescribed runtime and displayed storage powers.

The source reconstruction, including the first-layer normalization exception,
finite initialization, all four nonzero Gaussian trace terms, collision budget,
and own-stopped prefix mesh, is recorded in
[WIDTH_DEPENDENCY_CHECK.md](WIDTH_DEPENDENCY_CHECK.md). No further uninspected
raw source lemma is left in that finite-query composition.

For Harmonic, the new obstruction is stronger than a failed radius estimate,
but has an important scope limit. Fix \(m=d=L=2\) and the admissible activation
\(\phi(u)=u+\cos u\). Its initialized whole-sphere feature family has
arbitrarily large finite rank. On a high-probability empirical Gram event,
approximating that family to coordinate tolerance \(\eta\le Y\) forces
arbitrarily large finite source dimension as \(Y\) decreases. The current
exact source metric injects this dimension into the stored coordinates.

For a fixed activation/depth headline coefficient \(C\), put locally
\(\lambda=\gamma/m\). Along compatible two-sample problems with
\(Y=\lambda^2\) and \(\lambda\downarrow0\), preserving the exact displayed
Harmonic count forces

\[
n\ge \exp\!\left(c_C\sqrt{m/\gamma}-1\right)
\]

once the fixed empirical rank event is likely. Here \(c_C>0\) is independent
of the varying labels, gap, and width. Thus no threshold polynomial jointly in
\(\gamma^{-1},Y^{-1}\) can uniformly deliver that source interface and count.
The counterfamily varies the problem across instances; every individual
instance still has fixed labels as width grows.

This does not test fixed positive \(Y\) or fixed positive \(Ym/\gamma\),
does not lower-bound arbitrary prediction-only compression, and does not
contradict the paper's eventual theorem. It cannot be used to assert that the
user's narrower fixed-label scaling question has been disproved. The complete
rank argument and fresh check are in
[HARMONIC_ONSET_ROUTE.md](HARMONIC_ONSET_ROUTE.md) and
[HARMONIC_ONSET_CHECK.md](HARMONIC_ONSET_CHECK.md).

The exact gates, coefficient accounting, and reconstructed calculations are
in [WIDTH_UPGRADE.md](WIDTH_UPGRADE.md), with its former uninspected-input
qualification superseded by the new dependency check.

## 3. Efficient setup with unchanged retained-state bounds

There is a disposable numerical dense rollout producing source spaces that
satisfy the current selected-model transfer theorem. This is a high-order
rollout over the finite approximation horizon, not merely a short initial
physical-time window. Numerical panels are short and their number is
polylogarithmic. The output compressed model starts at original time zero and
retains no rollout, polynomial forcing table, or dense matrices.

For separately fixed parameters the sufficient costs are:

| Cost | Harmonic | Taylor |
|---|---:|---:|
| Setup arithmetic | \(O(n^2[\log(en)]^{3d/2+1})\) | \(O(n^2[\log(en)]^{5/2})\) |
| Peak setup real coordinates | \(O(n^2)\) | \(O(n^2)\) |
| Retained real coordinates | unchanged \(O([\log(en)]^{3d+2})\) | unchanged \(O([\log(en)]^3)\) |
| Complete-trajectory error | \(Y/n\) | \(Y/n\) |

The retained parameter dependence is still

\[
\begin{aligned}
\mathrm{Harmonic}:\quad&
C(m+d)^2+\left(\frac Cd\right)^{d+1}
\left(\frac{Ym}\gamma\right)^4[\log(en)]^{3d+2},\\
\mathrm{Taylor}:\quad&
C(m+p)^2\left[
\left(\frac{Ym}\gamma\right)^4[\log(en)]^3+
\left(\frac m\gamma\right)^2[\log(en)]^2
\{\log(e+\log(en))\}^2\right]+C(m+p)d.
\end{aligned}
\]

The Taylor bridge replaces literal local Taylor-coefficient generators by
approximate source values at real Chebyshev nodes on the same certified
analytic panels. Interpolation has controlled value error; applying initialized
matrices to those generators enforces exact image pairing. The generator
count and selected runtime are unchanged in order, although a different valid
support/metric may be selected. No claim of bitwise identity with the previous
compiler is made.

The table uses exact-real arithmetic. All orders, dimensions, gap and label
scales, evaluator work, selector work, source-image costs and peak live arrays
are exposed in [SETUP_UPGRADE.md](SETUP_UPGRADE.md); its new Taylor bridge and
cost ledger are checked in [SETUP_BRIDGE_CHECK.md](SETUP_BRIDGE_CHECK.md).
Finite-bit guarantees for
rank decisions, metric conditioning, exact initialized additions and subsequent
infinite-time execution remain unproved. Analyticity by itself does not supply
a constant-cost algorithm for evaluating an arbitrary activation.

This setup is asymptotically cheaper than ordinary dense Euler on the same
horizon **if** its step is a fixed inverse power of width. No proof that Euler
requires that step is supplied. Nor does this claim a speedup over a dense
solver using the same high-order continuation technique.

## Checks and manuscript disposition

The early-upper proof was checked independently within the study against the
actual paper equations. A separate reviewer checked the new Taylor interpolation
bridge and costs; the inherited numerical backend and source probabilities
are distinguished from that new bridge. The time-window argument received a
separate bounded review. The revised query-zero examples and Harmonic
source-rank obstruction each received a fresh mathematical check. The
Legendre/Taylor dependencies were reconstructed after permission was granted.
The off-span endpoint extension also received a separate narrow reconstruction
against its Gaussian-oracle and projected-innovation dependencies.
The nonparallel-query initialized rank, small-ball constants, and shrinking
time window received a separate reconstruction. The actual-network crossing
bridge received a fresh isolated review of its complete frozen proof and the
canonical paper setup; this review did not read other route findings or
earlier review reports.
These are internal reconstruction checks, not the repository's promotion
gates and not audits of every historical source.

The packet is suitable as a record of the positive additions and precise
remaining obligations, **not** as a fully closed threefold replacement theorem.
No paper/book files or existing study arguments have been changed. In
particular, no endpoint geometry has been silently dropped, no trajectory
supremum lower bound has been relabeled a same-time bound, and no conditional
probability input has been relabeled an unconditional theorem.
