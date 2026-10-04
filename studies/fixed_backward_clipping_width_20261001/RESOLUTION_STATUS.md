# Attempt to resolve the full root-width question

2026-10-01. Same-study continuation explicitly requested by the user.
**The general full root-width theorem and an actual slower-rate lower bound
are both unresolved.** This record concerns the fixed positive hard-clipped
q=1 closure and its own population, not a different training rule or a
dense/unclipped target.

## 1. Exact decision problem

The regime is the actual two-hidden-layer tanh closure with cap \(M=1\),
fixed finite data, canonical Gaussian initialization, zero initial readout
and values, matching initial keys, and the residual-RMS clock. The small
label RMS \(Y>0\), data, and positive initial population Gram margin are
fixed independently of width.

On the initialized fitting event \(\mathcal G_n\), set

\[
 \bar f_n(t,x)=\mathbb E[f_n(t,x)\mid\mathcal G_n],\qquad
 \beta_n=\left(\int\sup_{t\ge0}
              |\bar f_n(t,x)-f_*(t,x)|^2\,d\mu(x)\right)^{1/2}.
\]

Here \(f_*\) is the own clipped population from CLIPPED_POPULATION_ROUTE.md.
For bounded query sets, the existing centered estimate gives

\[
 \left(\mathbb E\left[\int\sup_{t\ge0}|f_n-f_*|^2\,d\mu
                    \,\middle|\,\mathcal G_n\right]\right)^{1/2}
 \le C_\mu n^{-1/2}+\beta_n.
\]

The decisive missing upper estimate is \(\beta_n\le C_\mu n^{-1/2}\).
A slower-rate counterexample must come from this actual flow. An abstract
sequence, a bad intermediate norm estimate, or a different matrix
observable does not qualify.

The previous bound \(\beta_n\le C_\mu(Y/n+Y^3)\) controls the full size of
feature learning rather than its finite-width discrepancy. Its \(Y^3\)
term is not a proved limiting bias. Qualitative all-time convergence and
bounded good-event predictions imply \(\beta_n\to0\). Thus a positive
constant asymptotic error on this event is already excluded, but no rate
follows.

An all-initialization all-time second-moment theorem additionally needs
control on \(\mathcal G_n^c\). Exponential exceptional probability and the
finite-horizon energy estimate do not alone control an infinite-time
supremum there. This issue is separate from \(\beta_n\).

## 2. Attempts and checks

Fresh scoped upper, lower, and interpolation attempts began without each
other's reports. Their complete records are RESOLUTION_UPPER_ROUTE.md,
RESOLUTION_LOWER_ROUTE.md, and RESOLUTION_INTERPOLATION_ROUTE.md.
The coordinator read all three completely. Separate complete scoped
checks are ORTHOGONAL_QUERY_CHECK.md and CAP_ANTICONCENTRATION_CHECK.md.
The latter's operator-cutoff and activity/domain corrections were applied
by the route author. These are internal checks, not promotion reviews.

### A complete rate for orthogonal queries

Let \(U=\operatorname{span}\{x_a\}\). For every fixed \(x\perp U\),

\[
 f_*(t,x)=0,\qquad
 \mathbb E[\sup_{t\ge0}|f_n(t,x)|^2\mid\mathcal G_n]\le CY^2/n.
\]

This is a theorem about the actual evolving closure. Training leaves
\(A(t)x=A_0x\), and these first-row Gaussian projections are independent
of the entire training environment, including \(\mathcal G_n\).
Conditional on that environment, the query coordinates
\(H_j=\tanh(A_{0,j}x/\sqrt d)\) are independent, symmetric, and bounded.
The output \(n^{-1}w^T\tanh(BH)\) is odd in \(H\), with conditional mean
exactly zero. Its actual velocity has gradient bound \(C\rho/\sqrt n\)
and diagonal second-derivative bound \(C\rho/n\). Coordinate replacement
and \(\int\rho\le Y/\lambda\) prove the temporal-supremum estimate.

The constant is independent of query magnitude, so any fixed probability
law supported on \(U^\perp\) is allowed. Conditioning requires positive
probability, automatic at sufficiently large width. If \(U\) fills input
space, only the zero query is covered. This is not the general-query rate.

### Clipping and adaptive linear feedback

The cap route proves probability at most \(C\varepsilon\) that an actual
lower preclip carrier lies within \(\varepsilon\) of either hard threshold,
on its specified column-cavity events. It uses a first-row Gaussian
direction away from the maximum of the activation gate and an independent
column direction near that maximum. The statement concerns actual
canonical flows and true cavities, not arbitrary interpolated histories.

Cavity-measurable linear response kernels also obey a root-width
Gaussian quadratic-form estimate uniform over bounded driving paths that
depend on the same Gaussian row. Taking absolute values before integration
avoids a false independence assumption. Thus adaptive row feedback is not
itself an obstruction to the linear estimate. This does not identify its
finite-width trace with the population trace.

### Fixed-program cancellation

Every fixed polynomial program built from coordinate operations,
normalized averages, and actual \(W_0,W_0^T\) actions has \(O(1/n)\)
full-matrix versus block-matrix mean discrepancy. The complete counting
proof uses exact cancellation of variance-weighted forests; collisions
and cycles cost \(1/n\).

The constant depends on program size and degree. No summability estimate
for the exact tanh/hard-clip trajectory was proved. The report's bounded
operator-Lipschitz matrix observable with order-one interpolation bias is
only a counterexample to a proposed generic proof principle, not a neural
output or a slower-rate closure counterexample.

## 3. What the lower-bound search excluded

1. Clipping is Lipschitz. It cannot turn an already-proved root-width
   input coupling into a quarter-width output error. A threshold atom
   can give root-width bias; this is not a slower-rate mechanism.
2. An initial population raw-covariance null direction is exactly null
   empirically, almost surely. The support argument also applies to the
   initial Gaussian tanh layer. A generic covariance square-root
   inequality does not establish an initial quarter-width counterexample.
3. Motion after \(T_n=(\log n)/(2\lambda)\) adds at most root-width error
   on the fitting event for finite-second-moment query laws. This does
   not provide a quantitative comparison up to that growing horizon.
4. Under the bounded prediction envelope, queries of norm greater than
   \(\sqrt n\) contribute \(o(n^{-1/2})\) for a fixed finite-second-moment
   law. This tail alone cannot supply a slower rate.

No admissible actual-flow slower lower bound was found.

## 4. Remaining source estimate

Row removal must retain the nonvanishing causal response caused by
reinsertion. Its linear part is controlled at root width. The subsequent
targeted attempt in WEIGHTED_REMAINDER_ROUTE.md also proved the nonlinear
weak remainder; WEIGHTED_REMAINDER_CHECK.md checked its complete proof
separately. The coordinator read both complete files. The envelope
qualification from that check was applied.

Precisely, freeze the residual, clock, and finite scalar memory pairings
at their actual row-cavity values. Let \(H_n(t;\omega,\eta)\) be the resulting
forced first-layer feature, where the removed Gaussian row
\(\omega\sim N(0,I/n)\) enters through the true backward action and
\(|\eta_a(t)|\le C_\eta s^c(t)\). The path \(\eta\) may depend arbitrarily on
that same row. Let \(J_n[\eta]\omega\) be the genuine first response at zero
row with the selected path held fixed. On the specified common cavity
event \(\mathcal C\),

\[
 \mathbb E\left[\mathbf1_{\mathcal C}\sup_{t\ge0}
  \left|\omega^T\bigl(
    H_n(t;\omega,\eta(\omega))-H_n(t;0)
                     -J_{n,t}[\eta(\omega)]\omega\bigr)\right|\right]
 \le Cn^{-1/2}.
\]

This is an all-time first-moment theorem for a precisely specified
auxiliary comparison within the actual closure equations. It is not yet
the full finite-system versus population theorem.

The useful mechanism is the difference between a vector norm and a
weighted scalar response. The ordinary state Taylor remainder satisfies
\(\mathbb E[\mathbf1_{\mathcal C}\sup_t\|R_n(t)\|_2^2]\le Cn^{-1/2}\).
Taking its square root gives only a quarter-width vector bound.
Instead, an exact local clipping inequality puts the nonlinear input
error into its squared norm. The remaining terms are weighted by
cavity-measurable Gaussian projections and controlled by the checked
near-cap estimate. Exact propagation through the cavity linearization
then gives the displayed root-width scalar estimate. No nonlinear
propagator is falsely declared independent of the row.

The uniform \(C_\eta s^c\) envelope includes the actual full row history
on simultaneous fitting events by activity comparability; this does not
restore the other scalar histories. The upper route separately proves
the root-width contribution of their linear perturbation, while leaving
their mixed nonlinear perturbation open.

The remaining tasks are that mixed empirical-history remainder and
comparison of the finite-width covariance/response law with the fixed
population law, with constants uniform under time-history refinement.
The required mean-law comparison is not supplied by the local row theorem.
Its hard-clip response selectors are not Lipschitz in an ordinary state
metric merely because the carriers have bounded densities. A weaker
centered, second-order mean-law argument could suffice; the upper route
states its exact missing assumptions without claiming them.

The weighted report also constructs a quarter-width RMS example for
abstract correlated cap distances. It is solely a counterexample to an
unnecessary RMS upgrade of the local lemma, not an actual closure
trajectory or a slower prediction-rate lower bound.

## 5. Process and source screening

Current instructions, workflow Part 1, this study's README, maintained
scientific entry points, and required research/proof skills were read.
AGENTS.md changed during the continuation; it was reread, and its newly
required canonical-notation skill and neural-network reference were read
before the final mathematical account.
The current paper and included mathematical files had been read completely;
unchanged hashes were verified. No other study supplied scientific inputs.
No manuscript edit, Git mutation, training experiment, or promotion was
performed.

A bounded external screen inspected the displayed models and rate
statements of
[adaptive Langevin DMFT](https://arxiv.org/html/2504.15556v2),
[general first-order methods](https://arxiv.org/html/2406.19061v2), and
[ResNet training limits](https://arxiv.org/html/2603.18168v1).
They supplied no applicable theorem for this hard-clipped continuous
training flow. No external proof was imported or claimed to have been
verified in full.

The user requested complete resolution. These checked advances are not a
substitute for either required outcome. The general verdict is unresolved.
