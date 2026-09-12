# Authorized bounded validation budget

Recorded before solver/test execution, 2026-09-12.

Purpose: deterministic checks of the candidate's Gaussian source reuse,
directional-response identities, finite recurrences, refinement axes and
checkpoint restart. These do not certify milestone C.

Budget: at most 12 solver trajectories in total, at most 256 physical Euler
steps each, at most 4096 representatives per population and at most 8 active
data nodes. Sum of all training call counts across trajectories <= 3000.
Peak resident memory target <= 1 GiB; total wall time <= 10 minutes. Small
identity tests use at most 200000 scalar random samples or deterministic
enumeration of at most 4096 Rademacher sign vectors. No finite-network
training or broad sweep is included. If this budget is inadequate, revise
the plan with a reason before further runs, within the user's bounded-run
authorization; do not silently expand it.

Required checks, kept separate:

1. Polynomial Stein/directional identities and an exactly evaluable reused
   forward/adjoint response; correlated and singular clean source Grams.
2. Prefix-preserving covariance extension; independent orientation sources;
   no replacement of an old source on restart.
3. Bitwise checkpoint/restart equivalence for a trajectory split at a reached
   step, including all random state and numerical configuration.
4. Time, representative count, source noise, passive Gaussian quadrature and
   precision changed separately on a fixed law. Report measured differences
   without equating them to a rigorous error bound.
5. A short nonlinear trajectory before an optional bounded T40 diagnostic.
   Stop on nonfinite state or failed covariance floor; save diagnostics.

Generated reports, checkpoints and outputs belong only in
data/generated/population_flow_computation/. Code/tests/configuration remain
flat in this study. No images are necessary for these checks.

## Frozen main run design

The exact cases and seeds are in validation_cases.json. After the three small
implementation trajectories (13 steps, 26 training calls), run at most the
eight listed cases, sequentially, within the original 10-minute total budget.
The first is a short reference trajectory; abort subsequent cases if it fails
to produce finite state or valid source covariances. Later validity failures
are recorded, with the last completed checkpoint, and are adverse results.
Single-thread BLAS is used to bound resources and aid reproduction.

Reference comparisons change exactly one specified numerical axis relative to
reference_base. Different dimensions/time meshes do not give perfectly coupled
random draws; observed differences include numerical sampling fluctuations.
No empirical convergence rate is inferred from one seed. The two arc cases
are quadratures of the SAME fixed nonatomic correlated law (a=.03,b=.02,p=.53),
used only in the broader exploratory scope. They are not called admitted by
the extremely small conservative neighborhood certificate.

Record physical node predictions on a fixed 65-point circle grid, final
quadrature orders 16 and 32 on the identical saved state, initial/current
hidden moments at four fixed directions with an explicit independent query
seed, all source validity diagnostics, checkpoint size, measured wall time,
peak process memory and input/source hashes. A grid maximum is reported as a
grid maximum, never as the requested time/whole-circle supremum certificate.

Operational success means valid completion, exact restart identities in tests,
and reproduction from the saved configuration. Numerical evidence is favorable
only if independent refinements reduce or stabilize discrepancies without
growing response/tangent diagnostics. A failure or mixed refinements is adverse
or inconclusive, respectively. Neither outcome proves convergence. An actually
certified useful accuracy would require a separate proven bound <=0.1 or 0.02;
no measured refinement difference is substituted for that missing bound.

The eight main cases completed in under 14 seconds, with peak process RSS
below 250 MiB. Their separate time and sample refinements changed predictions
on the retained grid by approximately .065 and .056. Before a further run,
add exactly one combined refinement (reference_combined: P=4096,h=.15625,
T=40,s=.05,float64, same seed) to check whether both changes together remain
within the observed scale. This uses the twelfth and final authorized
trajectory, raises total calls to 2490, and stays within the original state,
time and memory limits. It does not authorize further trajectories. Store it
in a separate fresh run directory so the original case definition/hash and
eight-case evidence remain intact.

After all twelve trajectories, a deterministic analysis of the retained
reference_base and reference_combined final states is permitted within this
budget: evaluate the new analytic passive-quadrature bound at q=16 and q=32
using their already recorded residual-scale summaries and saved w arrays.
No new trajectory, passive Gaussian draw or covariance query is needed.
Limit this analysis to those two states, at most one minute and 256 MiB;
retain the producer evaluate_quadrature_bound.py and use a fresh data folder.
The result is only a floating evaluation of an exact-arithmetic component
bound, not an interval-certified population error. This does not extend the
trajectory budget.
