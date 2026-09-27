# Fixed selective closure across new input configurations

2026-09-27. The user explicitly requests a broader empirical test on other
input configurations. This continues the same scalar-compression study.
The previous selective campaign is closed; all new outputs go under
`data/generated/structured_full_rank_scalar_20260926/selective_geometry_20260927/`.

## Decision question

Does the smallest feature-motion-preserving selective closure maintain
useful circle-function agreement when input spacing, label variation, and
training sample count change? H1: the previously observed fitted cases
extend to varied configurations with circle discrepancy around 0.1 or less.
H0: easy input/label patterns explain those cases; sharper or more numerous
constraints cause fitting failure or large circle discrepancy even after
the core training loss becomes small. This tests one fixed construction,
not existence or convergence of all scalar closures.

## Frozen model and tasks

Use the existing selective zero-boundary rule, essential-feedback and both
hidden-Gram derivatives protected, output dependency depth1, no additional
dependency expansion. Keep tanh, block size k=4, memory order P=1, original
activity clock, seed1, n=1024 initialization/reference width, canonical
unhalved MSE, and target training MSE0.01. The bounded mark initialization
uses K=3 and records any redraws. Initial contractions use the matched
finite block realization, then discard population arrays. Runtime is only
aggregates, passive query aggregates, and the clock.

The eight tasks are frozen in `geometry_tasks.py`, in this order:

1. `pair_cos3`: moderately separated, opposite labels.
2. `near_pair_sin9`: closely spaced, opposite labels.
3. `pair_orthogonal_cos1`: orthogonal directions with smooth labels.
4. `triple_cos3`: symmetric three-point curvature.
5. `cluster_triple_cos1`: the earlier difficult cluster geometry with smooth
   labels, separating geometry from sharp label variation.
6. `triple_wide_mixed`: three inputs spread around the circle.
7. `quartet_broad`: four constraints on a broad ridge.
8. `quartet_mixed`: four mixed-frequency constraints.

No architecture, cutoff, order, seed, or stop-loss tuning between tasks.
Canonical dense Gaussian and matched block-memory controls use the same
task, width, seed and stop target. Every reference has its actual stop status.

## Metrics and interpretation

The primary metric is raw RMS of scalar passive predictions minus fitted
canonical Gaussian predictions on 64 equally spaced circle angles; no
normalization by signal RMS and no teacher-risk substitution. Also report
scalar versus matched block, and block versus Gaussian separately. Gaussian
and block reference outputs are saved on 256 angles.

Append passive copies of every training input to the query panel. Report
core training MSE/RMS, passive predictor training MSE/RMS, and maximum/RMS
disagreement between the two representations. Query copies do not enter the
residual or train any additional samples. This exposes the existing input
identification defect on every task, without changing the cutoff to fix it.

Descriptive screens: a fitted candidate with circle RMS<=0.1 is a useful
coarse-accuracy result; fitted circle RMS>0.3 is a strong failure of the
small-discrepancy hypothesis; intermediate values are reported without a
binary success claim. These are absolute differences from Gaussian, not
generalization gaps against labels. Maximum core/passive disagreement>0.05
flags inconsistent decoding separately. Unfinished references or candidates
are partial comparisons, never fitted-network success/failure evidence.

## Numerical validity and efficiency

Float64 RK45, rtol1e-5, atol1e-7; error norm is the maximum of scaled RMS
over the shared core, each passive block, and the clock. Preserve the
existing reference integrators. Check passive independence, vectorized
versus individual RHS, exact initialization reuse, and all checkpoint hashes.

A compiler-only optimization may reject a child before expensive graph
canonicalization if its additive decoration/node-count signature matches
no retained contraction. This cannot reject any retained child. It must
produce identical selected trees, coefficients and RHS to the frozen
compiler, with explicit comparisons before training. Missing-term counts
from this shortcut are raw proposals, not counts of combined unique terms.
This changes computation, not the scientific cutoff. Cache compiled models
with task/configuration/source hashes so each task is compiled only once.

For circle quadrature, compare the 64-angle result to its 32-angle subset;
a difference>0.001 flags coarse resolution. If a fitted case has circle
RMS>0.3, allow one campaign-wide half-tolerance check of the first such
case. If that case also has coarse quadrature, allow one 128-angle query
check. These are the only extra runs, share the total budget, and cannot be
used to select a favorable seed or replace an adverse result silently.

## Budgets and terminal stop

Each compilation: at most60seconds,100000states,1000000 evaluated RHS terms.
Each training: at most45seconds and physical time3000, preserving the last
accepted state. Initial-query integration has a90-second wall ceiling to
avoid a large setup silently consuming the quick-test budget. Use BLAS1;
at most two training jobs concurrently. Cumulative scalar training<=6minutes,
reference training<=8minutes, and total campaign wall time<=12minutes from
the first training run. Stop after all eight tasks and triggered checks, or
the first applicable total budget. Preserve every failure/skip status.

No further order sweep, Fourier decoder, density/population substitution,
new seed, optimization of scientific rules, or resumption of the earlier
closed campaign. No theorem follows from passing this screen.

## Ownership and records

Root owns tasks, this protocol, analysis, plots, report and README.
Compiler agent owns `true_aggregate_selective_fast.py` and compiler checks.
Runner agent owns `run_selective_geometry.py` and scalar run records.
Reference agent owns the new reference records and wrapper.
Record commands, source hashes, HEAD, environment, exact task labels,
initialization, solver settings, timings, state sizes, raw predictions and
metric derivations. Preserve unrelated shared-checkout changes; no Git writes.
