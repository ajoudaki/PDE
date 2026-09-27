# Quick test of direct aggregate dynamics

2026-09-27. User explicitly authorizes implementation and quick experiments
against canonical dense Gaussian networks at n=1024, stopping at training
MSE 0.01. This continues the current study's direct contraction construction.

## Question and allowed model

Does the direct scalar contraction ODE in TRUE_AGGREGATE_CONSTRUCTIVE.md,
section 11, produce fitted circle functions close to canonical Gaussian
training, and does increasing the aggregate order improve the discrepancy?
H1: a modest executable order fits and improves against a matched block-memory
reference, with small total Gaussian discrepancy. H0: truncation error or
state/evaluation cost prevents that at quick-run resolutions. A capacity
failure is an implementation-feasibility outcome, not an incompressibility
theorem. Scalar failure must not be replaced by a particle or histogram result.

The candidate evolves only current-state aggregate contractions and the
clock. Initial averages may be computed from the known n=1024 initialized
block network once; the original arrays are then discarded by the scalar
solver. There is no evolved quadrature population, density, oracle forcing,
Fourier approximation, or fitted future trajectory. Matrix reuse and learned
cross-block global overlaps must remain in the generated equations.

Use tanh, canonical unhalved MSE and mobilities, the original activity clock,
and current study circle tasks. The initial block entries have variance 1/k.
Use entry bound K=3: reject and regenerate any offending Gaussian entries,
recording their count. Initial first weights remain fully Gaussian. Preserve
the usual finite canonical readout N(0,1/n^2) in scalar initial averages and
both finite reference models. Its bound |c(0)|<=2 is checked; this extends
the normalization bounds since |c|<=|c(0)|+2(L-1) and
|A_j|<=sqrt(m)[max|c(0)|(L-1)+(L-1)^2].

## Tasks, configurations, and branching

Seed 1, n=1024. Preselected tasks: pair_cos1, triple_mixed,
cluster_triple_cos9, with data exactly from circle_tasks.py. No search for a
favorable task or seed. Main candidate k=4, memory P=1, aggregate degrees
R=9,11. Attempt R=13 only if both smaller degrees compile and remain within
the runtime/state budget. Optional parameter checks are k=8 at the largest
quick executable degree and P=2,k=4 at that same degree; do not form a large
Cartesian sweep. These optional checks are attempted only after primary
configurations can actually be integrated within the quick-run budget.

Compiler feasibility may first use m=1 and m=2 as deterministic engineering
checks. A k=1 specialization is not a scientific replacement for the intended
k>=2 mixing-block test. Stop a compilation at 100000 states, 1000000 sparse
terms, or 60 seconds. Retain counts/status; do not launch a known huge run.
The implemented compiler may retain only the derivative-reachable subset
through the cutoff, provided every retained in-cutoff dependency and all
feedback observables are included. It must retain this exact truncation rule.

For circle evaluation, one symbolic passive query can be vectorized across
256 equally spaced angles, sharing the training aggregates; no cross-query
products are required. A 128-node subset provides a circle-integration
sensitivity diagnostic. If passive compilation itself exceeds the budget,
report that obstruction rather than replacing it with a trained population
decoder or an unvalidated post-training reconstruction.

## References and primary metric

One dense Gaussian reference per task, canonical initialization seed 1 and
n=1024. If candidate compilation passes, also run a matched finite block-memory
reference for each tested (k,P), using the same initialized block realization
as the scalar initial averages. Reference populations are controls only.

At the first fitted endpoint with training MSE<=0.01, compare

    sqrt(mean_angles (f_scalar(theta)-f_Gaussian(theta))^2).

This is the absolute RMS of the function difference, without division by the
Gaussian signal RMS. Also report scalar-versus-matched-block RMS and
matched-block-versus-Gaussian RMS, separately. The three errors do not add
in quadrature. Comparisons of independently stopped fitted endpoints are not
common-time trajectory convergence tests. Partial endpoints get their actual
MSE/time and are never described as fully fitted.

This is an exploratory screen. A promising candidate fits, has total RMS
<=0.05, and improves by at least 0.001 on increasing R, with changes larger
than the numerical diagnostics. Values are still reported if these screens
fail. No asymptotic or population-limit claim follows from one seed.

## Numerical checks and budget

Before training, check generated contractions and their derivatives against
the original block equations on tiny deterministic multiblock states with
nonzero readout and memories. Check normalization, global coupling, true
transpose reuse, and scalar-only restart. Separate omitted-boundary terms
from compiler error; do not demand equality where truncation applies.

Use float64 and adaptive RK45, target rtol=1e-5, atol=1e-7 for the scalar
system unless a deterministic validity check requires a disclosed change.
References use the existing validated fast integrators. Keep BLAS thread
counts modest. Each training trajectory has a 45-second wall ceiling and
physical-time ceiling 3000, retaining its last accepted state. This matches
the existing quick reference integrator; the wall ceiling controls cost.
Total training
budget <=12 minutes; no extensions, reruns to improve the table, or extra
seeds. A single half-tolerance check is allowed only on a fitted primary
candidate; circle discrepancy <=0.002 is the diagnostic threshold. The
128/256-angle RMS discrepancy threshold is 0.001. Failures make the relevant
comparison diagnostic/inconclusive, not certified accurate.

Keep source hashes, commands, environment, solver status, elapsed time, state
and sparse-term counts, initial bound diagnostics, and prediction arrays in
data/generated/structured_full_rank_scalar_20260926/true_aggregate_quick_20260927/.
Stop after the specified screen or a demonstrated compiler/solver budget
failure. No further theory search is authorized by this experiment plan.

## Ownership

Root: protocol, run coordination, synthesis, README, and final report.
aggregate_quick_compiler: true_aggregate_ode.py and compiler scratch.
aggregate_quick_references: true_aggregate_references.py and reference runs.
aggregate_quick_validation: check_true_aggregate_ode.py and deterministic checks.
