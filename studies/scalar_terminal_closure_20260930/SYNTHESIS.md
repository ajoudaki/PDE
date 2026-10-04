# Scalar compression — STUDY MISSED THE REQUESTED OBJECTIVE

> [!WARNING]
> **STATUS CORRECTION — 2026-10-01: THIS STUDY MISSED THE MARK.**
>
> The requested system was a small autonomous scalar ODE operating from
> initialization through feature learning and terminal stabilization. Instead,
> the assistant used full-closure training to produce a late learned state and
> compressed only its continuation. The user did not authorize this replacement
> of the central problem. The original objective remains unsolved by this work.
>
> The scalar–closure error tables and 729-number evaluator do **not** establish
> compression of the full training trajectory from initialization. They rely
> on preceding full-closure training and supplied learned coefficients. The
> higher-order experiments and newer memory-transport proposal retain this
> dependency. Internal PASS reports do not validate fulfillment of the request.
>
> The earlier success framing and next-step language below are superseded by
> this correction. Retain this synthesis as a historical record; do not use it
> as evidence that the requested scalarization was achieved. See the prominent
> [README status correction](README.md) for the authoritative study status.

Historical synthesis, originally 2026-09-30, subject to the correction above.
It uses the current manuscript, maintained sources, and this study's own
derivations. No earlier unpromoted study is a proof dependency.

## Historical partial result — not the requested construction

There is a concrete, conditionally proved terminal scalar model for the
actual finite-width response-memory dynamics at every fixed finite order q.
The q=1 proof and its higher-order transfer are internally checked.
At a certified small-residual handoff it
uses m moving residual scalars and m^2+m frozen aggregate coefficients,
with all-time loss error of order R^3, where R is the residual norm at
handoff. It also tracks its own activity clock at equal physical times.
The proof is internally checked, not promoted.

This result makes part of the user's stabilization argument quantitative.
It does **not** establish the requested initialization-to-endpoint scalar
compression with total storage o(epsilon^-2). In particular, the early
coefficient evaluator, its source error, its width-uniform constants, and
its route to a fitting terminal region remain unproved. Computing the
handoff using the full population would not solve that problem.

The substantive direction suggested by the new results is to approximate
the changing **response of the residual**, with a truncation error weighted
by the remaining residual, rather than demand reconstruction of the full
population density. This is a design criterion and partial theorem, not an
assertion that a low-complexity evaluator already exists.

The subsequently requested numerical comparison is now complete in
[CIRCLE_RESULTS.md](CIRCLE_RESULTS.md). It tests a 729-number terminal circle
evaluator against dense width 1024 and full q=1 on all five manuscript tasks.
All full-model pairs fit after one explicitly recorded horizon extension.
The terminal approximation can track q=1 closely, but it does not uniformly
reproduce dense scores; q=1 itself already differs substantially from dense
on the alternating-label tasks. A low internal scalar loss also does not
guarantee an accurate circle readout. These are finite-grid, one-initialization
empirical results, with source and numerical checks, not a new compression
theorem or a replacement for the unresolved early evaluator.

The higher-order continuation now establishes the same exact scalar response
form and conditional terminal theorem for every fixed finite q; see
[HIGHER_ORDER_SCALAR.md](HIGHER_ORDER_SCALAR.md) and its internal check.
The higher moments enter through weighted endpoint sums in the prediction
velocity, while the full network still uses all matched mode pairs.
The terminal scalar count therefore stays unchanged for q=2 and q=3.
Their dense and scalar empirical comparisons are specified separately in
[HIGHER_ORDER_EXPERIMENT_PLAN.md](HIGHER_ORDER_EXPERIMENT_PLAN.md).

Those comparisons are complete in
[HIGHER_ORDER_RESULTS.md](HIGHER_ORDER_RESULTS.md). On the two alternating
tasks, q2 reduces dense endpoint circle RMS from q1's 0.2362/0.3810 to
0.02969/0.04121 and passes the preset endpoint criterion. q3 tracks the
dense training loss more closely than q2, but has worse endpoint circle
RMS, 0.07214/0.05247. All four primary scalarizations track their own
closure within RMS 0.00298--0.00670 and pass the separate scalar/closure
criterion. The finite Fourier query representation retains measurable error
even after internal scalar residuals fit. The q3 Euclidean contraction
diagnostics are negative, so observed convergence is not a certificate
from the sufficient Euclidean theorem. All-time tube hypotheses remain
unverified for these numerical trajectories.

## 1. The exact object that needs approximation

Use the manuscript's two-layer q=1 specialization, with zero readout,
binary labels, fixed finite training inputs, tanh, and the original fixed
Gaussian mixer and its true transpose. In manuscript coordinates the
study's normalized variables are

    k_a = bar h_(a,0)/tau,       v_a = -2 bar delta_(a,0),
    tau(0)=1,                  taudot=||r||/sqrt(m).

The complete finite model and derivation are in
`TERMINAL_SCALAR_THEOREM.md`. Its exact aggregate equation is

    rdot = -C(X)r + ||r|| b(X),                                  (1)

where X is the full state and

    C_ab = (2/m)[ <g_a,g_b> + I_ab<ell_a,ell_b>
                           +<d_a,d_b><k_b,h_a> ],
    b_a  = (1/(m sqrt(m) tau)) sum_j <d_a,v_j><h_j-k_j,h_a>.

Here <p,q>=p^Tq/n and I_ab=x_a^Tx_b/d. These scalar quantities capture
the instantaneous response of the training residual, but their evolution
does not close automatically.

Two features matter for a faithful compression. C need not be symmetric,
because memory keys and current features differ. Also the b term is
first order in ||r||; it does not become a second-order correction merely
because the loss is small. At a fixed interpolating state, the map
u -> -Cu+||u||b is not differentiable at zero when b is nonzero. Thus a
linear positive-kernel approximation can omit part of the leading terminal
dynamics. `TERMINAL_HANDOFF.md` proves this precise differentiability claim.

## 2. A terminal finite ODE with a proved error budget

At a reached handoff t_0, save C_0,b_0,r_0 and optionally tau_0. Then evolve

    rhatdot = -C_0 rhat + ||rhat|| b_0,
    tauhatdot = ||rhat||/sqrt(m),
    Lhat=||rhat||^2/m.                                         (2)

This is an actual autonomous scalar evaluator. No neuron fields, mixer
actions, density queries, or growing history occur after the handoff.
It uses m moving scalars, one more for the clock, and O(m^2) fixed storage
and work per evaluation, for fixed training-set size m.

One sufficient certificate is

    lambda = lambda_min(sym C_0)-||b_0|| > 0,

together with a small terminal tube in which the full state speed is at
most H||r|| and the coefficients C,b are J-Lipschitz in the state. If
R=||r_0|| is small enough for the explicit tube inequalities, then

    sup_(t>=t_0) |L(t)-Lhat(t)| <= (2JH/(m lambda^2)) R^3,
    sup_(t>=t_0) |tau(t)-tauhat(t)|
                              <= (4JH/(sqrt(m)lambda^3)) R^2.   (3)

The full state and both clocks converge, and both residuals decay to zero.
The constants and sufficient smallness conditions are explicit in the
theorem. They are not assumed uniform in width.

The mechanism behind the cubic loss error is simple and useful:

1. Contraction makes the remaining integral of ||r|| of order R.
2. Every full-state velocity contains a residual factor, so the remaining
   feature/memory movement is also of order R.
3. The resulting coefficient error is of order R, and its contribution
   to rdot is multiplied by another residual, giving order R^2 error.
4. Loss is quadratic in r, giving one further factor R.

A constant zero-loss tail would only have error of order R^2. The response
model in (2) resolves more of the tail and can start at a larger residual
for a given loss tolerance.

The Euclidean certificate is not essential. `TERMINAL_METRIC_EXTENSION.md`
uses a positive quadratic form P and provides explicit matrix certificates
for contraction. It covers some nonnormal generators with temporarily
increasing Euclidean loss. The actual evaluator (2) is unchanged, including
its Euclidean norm in the b term. Its algebraic nonnormal examples are not
claimed reachable q=1 endpoints.

## 3. Required handoff precision is weaker than full-state accuracy

`TERMINAL_HANDOFF.md` permits approximate residual and aggregate data.
For uniformly controlled tube constants, a residual error O(R^2) and
coefficient error O(R) preserve the O(R^3) terminal loss estimate.
Hence a terminal error tolerance epsilon permits the scaling

    R=O(epsilon^(1/3)),
    residual handoff error=O(epsilon^(2/3)),
    coefficient handoff error=O(epsilon^(1/3)).                 (4)

This is a concrete target for the earlier scalar approximation. It need
not reconstruct a population state at handoff. It must accurately deliver
the finite response coefficients and residual, certify entry into the
terminal regime, and approximate the preceding loss curve as well.

The clock estimate is at the same physical t, not at matched activity
times. This distinction is necessary because a finite activity interval
can represent infinite physical time. Moreover finite activity by itself
does not give a regular activity-time trajectory: a contracting rotating
residual provides an explicit counterexample in the terminal note.

## 4. The early phase needs response evolution

`INITIAL_RATE_CURVATURE.md` proves an initialized statement for one input,
arbitrary width, and every finite initialization with g_0 nonzero. Put

    G=<g_0,g_0>,
    T=||(1-h_0^2) odot W_0^T[g_0 odot(1-g_0^2)]||^2/n
       + <h_0,h_0> ||g_0 odot(1-g_0^2)||^2/n > 0.

Then the actual q=1 loss satisfies

    L'(0)=-4G,       L''(0)=16G^2,
    L'''(0)=-64G^3-64T,
    (log L)''(0)=0,  (log L)'''(0)=-64T<0.                     (5)

The two terms in T come from the moving read-in and the value-memory
correction. A positive mixture of fixed exponential rates has initial
logarithmic curvature equal to the variance of those rates. Matching the
first two derivatives in (5) forces that variance to be zero, hence forces
a single exponential, which misses the third derivative.

This proves a specific necessary enrichment: response rates must evolve
to capture early feature learning. It does not validate any chosen
nonlinear scalar approximation, or prove all-time acceleration. The
one-input theorem has no imposed neuron symmetry but does not settle the
multiple-input compression problem.

## 5. What the independent routes ruled out or left open

The complete independent route notes were frozen before comparison.

`AGGREGATE_ROUTE.md` derives exact current cross-Gram equations. It also
constructs same-source current states that preserve the specified typed
pairwise Grams and all their linear mixer/adjoint-word pairings, yet have
different third derivatives of loss. Fourth/sixth coordinate moments
explain the discrepancy. This rejects an exact identity for that encoding
on all current states. The examples are **not** proved reachable from the
stipulated initialization; they are no population approximation lower bound.
Its internally checked correction makes the precise field list explicit
and records a nonzero V' term that cancels in the final loss calculation.

`INFORMATION_ROUTE.md` proves that, at fixed width, the q=1 training-path
law depends on the data through its Gram matrix and labels. A deterministic
population loss, if established, therefore has only that finite instance
information. This is not a finite efficient evaluator. Generic arbitrary-law
moment obstructions cannot automatically supply a lower bound for this fixed
Gaussian initialization class. The note also gives analytic stable scalar
systems matching arbitrarily many initial and terminal derivatives while
remaining separated in the middle. Initial matching plus endpoint stability
alone cannot prove accuracy.

`CONTROL_ROUTE.md` analyzes an explicit finite control-signature system
driven by its own predicted residual. It shows exactly how a uniform
directional-response approximation error would imply all-time physical
loss and clock accuracy under a strong contraction certificate. But its
state count grows as (m+1)^p, and a geometric error exp(-beta p) beats
epsilon^-2 only if beta>log(m+1)/2. No such q=1 source bound is proved.
The Gaussian/activation derivative-growth issue is exposed rather than
assumed away. This hierarchy is therefore a conditional diagnostic route,
not the achieved scalar compression or the preferred unresolved answer.

## 6. The decisive remaining problem

The next substantive proof must supply a finite initialized evaluator of
the changing directional responses in (1), on a reachable family robust
to the evaluator's own feedback, **with a quantitative cost/error rate**.
It should stop resolving those responses once the certified terminal
budget (4) is met. A useful rate must beat the requested epsilon^-2
storage scale after including every frozen coefficient and its precision.
No approximation source may be replaced by a population query or a saved
future trajectory.

The target population q=1 dynamics and a matched root-width dense-model
error also need their own existence/comparison hypotheses: the current
manuscript does not establish them in the generality needed to infer
o(n) from epsilon approximately n^(-1/2).

The present result is therefore a checked terminal compression mechanism,
a precise earlier-stage accuracy budget, and an initialized restriction on
what an early scalar response model must represent. The end-to-end generic
sublinear-state theorem remains open. The later user-authorized training
campaign is recorded separately in [CIRCLE_RESULTS.md](CIRCLE_RESULTS.md),
including every prescribed switch and the original unfinished time-512
comparison. No manuscript, maintained book/code, or Git index was changed
by this study.
