# Order-four and order-five extension

User-authorized continuation, 2026-09-21: derive the next two derivative
dictionary levels and measure RMS on the same two tasks. The existing
COMPARISON_PROTOCOL.md supplies all unchanged model, case, initialization,
flow, ridge, endpoint and archive rules. No other study is an input except
the already authorized original circle study's frozen references/settings.

New p4 retains middle-weight terms through t5, and p5 through t6, at zero
population readout and the fixed normalized axis probes. The actual finite
experiment retains its archived random readout. This distinction is unchanged.
Derivations and dictionary verification must pass before any training.
Keep existing files and completed runs unchanged.

Theory predicts no additional spans at p4: (K1,K2)=(6,12), exactly the p3
raw tables, but inherited eta=1/[1024(p+1)^2]. At p5 append the eight quartic
lower coefficient functions and twelve quintic upper coefficient functions
in P45_DERIVATION_ROUTE.md, giving (14,24). Existing columns retain exactly
their scales/order. New lower/upper columns use 4! and 5! times the ordinary
Taylor coefficient, respectively, after removing already retained lower
degree terms. This clears the common derivative factorials, analogously to
the existing L and C columns. No column RMS tuning, rank deletion, basis
changes or performance-selected alternatives are permitted. If the independent
algebra contradicts these prescribed lists, correct and document the theory
before training. Population scalar contractions use Gaussian quadrature;
no empirical task labels or training input enters a frozen feature.
Use the 256-node one-dimensional Gauss-Hermite moments and compare128 nodes;
require maximum moment discrepancy<=1e-9 before training. This is a numerical
agreement gate, not a rigorous quadrature-error bound. The inherited v remains
exactly the preceding builder's256-node value.

Primary question: does p5 improve circle RMS discrepancy from the saved dense
learned function compared with new p3? Report p4 too, while identifying that
its only change is ridge. Both numerical levels must give the same ordering
for a supported direction; reversed ordering or invalid endpoints is unresolved.
Report all four case/order cells, not a selected winner. The primary metric
is the 8192-angle RMS at each model's own first MSE=0.001 crossing; use the
archived dense endpoint at the corresponding tolerance. This is function
approximation of the trained dense model, not label generalization or a rate.
New p3 already has valid saved comparison endpoints. No baseline retraining.

Eight base trajectories: two cases, p4/p5, numerical levels0/1. Same CUDA
float64 Heun producer, rtol=(6.25e-5,1.5625e-5), atol=rtol/100, h0=.05,
hmax=2, hmin=1e-7, T<=10000, accepted steps<=30000, 180 integration seconds
per trajectory. Preserve all states, losses, curves, failures and diagnostics.
Check condition<=1e10, triangular residual<=1e-8, independent state replay
<=1e-10, finite values, common case/init, source hashes, fit status and grid
8192/4096 agreement. Per-model endpoint refinement sampled maximum must be
<=.01, including the archived reference. One extra /4 tolerance attempt per
cell is allowed only when both earlier attempts fit and this gate fails.
Use the latest two attempts after an extra; retain failed earlier attempts.
At most four extras, lexical cell order if the budget constrains execution.
No new attempts merely for a unfavorable score or ranking reversal.

Conservative available balance before this extension: 2174.519788134843
summed worker seconds. Hard new ceiling2100 seconds for new GPU workers,
including construction, output, preflight and replay/audit; leave at least
74.519788134843 unspent. Initially reserve four base workers <=400 seconds
each, release unused time after completion, then reserve conditional extras
<=200 seconds each only within the remaining ceiling. Preflight<=60 and
combined analysis/audit<=120 seconds are included, not added to the ceiling.
CPU-only symbolic derivation and small deterministic checks do not consume
the GPU-worker balance. Stop when the gated comparison is complete or the
bounds are met; do not expand the experiment grid.

This is a finite empirical test of a population-derived dictionary candidate.
It does not assert exact finite-width Taylor containment, preservation of the
initial dense function, all-order population regularity, positive-time series
convergence, or an asymptotic approximation rate. All additions stay internal
to this study; no promotion or shared Git-index operation is requested.
