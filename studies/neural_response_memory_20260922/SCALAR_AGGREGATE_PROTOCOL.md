# Scalar aggregate dynamics: frozen bounded experiment

2026-09-25. The user explicitly authorizes implementation and empirical testing
of scalar-only compression as continuation of this study. This protocol is
written before any candidate training/comparison trajectory is run. Root owns
this protocol, runner, analysis, results and the matching README entry.
The scalar engine/unit tests belong to aggregate_criterion_check; independent
checks belong to scalar_execution_design; the derivation belongs to
scalar_candidate_theory. Concurrent activation files are outside this task's
write scope. No old campaign is reopened and no Git-index change is planned.

## Candidate and information contract

Use the canonical three-hidden-layer bias-free tanh network, all four blocks
trained with physical mobilities (n,1,1,n), unhalved probability MSE and the
study's small stored readout. Input rows U=x/sqrt(d) have unit length, d=2.
Independent NumPy default_rng draws are w, W2, W3, c with standard deviations
1, 1/sqrt(n), 1/sqrt(n), 1/n. Output is c^T h3/n.

For original parameter vector theta and diagonal mobility B, define
g_a=B grad f_a and D_a=g_a dot grad. The scalar hierarchy is

    Theta_ab=D_b f_a,
    C_abc=D_c Theta_ab,
    Q_abcd=D_d C_abc.

Along the exact dense flow each current tensor's time derivative contracts
its next derivative tensor against -2r/M. The candidates retain levels through
order 2, 3, or 4 and set the derivative of the highest retained level to zero.
Order 2 is the initialized frozen-gradient-kernel control. Orders 3 and 4 allow
the learning kernel to evolve. Derivative indices are ordered; no symmetry
between the last two indices is imposed. Initial coefficients are evaluated
at the shared original network, with no future trajectory, fitting, reseeding,
teacher forcing, or later population reinitialization.

Initialization can use the original neuron arrays and dense matrices once;
their cost is reported. Runtime state and fixed terminal tensors have at most
M+M^2+M^3+M^4 real entries, independent of n. The standalone reduced RHS must
accept only these arrays and labels. It retains no initialized dense operator,
neuron vectors, quadrature particles, population sampling loop, or encoded
target trajectory. Runtime may use only ordinary tensor contractions.

This is a direct observable-generator truncation of canonical dense dynamics.
It implements the preceding scalar aggregation idea but is not an exact
algebraic collapse of the existing P-history model. Its approximation is the
missing highest generator derivative, a new closure choice. A failed witness
does not disprove all finite aggregate approximations. No convergence theorem
or positive Taylor-radius assumption is made.

## Fixed cases and primary comparisons

Read literal inputs only from this study's deep_circle_cases.json:

1. equal_mixed_odd: angles 0,45,90,135; labels +,+,-,+ (the documented exact
   antipodal quotient).
2. quadrant_alternating: angles 10,20,30,40,50,60,70,80; labels +,-,+,-,+,-,+,-.

Both use three learned hidden layers. Run widths 128 and 256, and seeds
20260920 and 20260927, for 8 fixed configurations. These finite widths retain
Gaussian bulk, actual transpose reuse, nonlinear gates, and correlated data.
They test finite dense dynamics, not an infinite-width theorem or an exact
repetition of the old width-4096 campaign. No data choice depends on results.

Each configuration has one coefficient initializer through order 4, a fresh
dense reference at two tolerances, and each scalar order at two tolerances:
64 primary integrations total. The primary physical horizon is T=128, with
outputs recorded at t=0 and a fixed panel containing 0.01,0.025,0.05,0.1,0.25,
0.5,1,2,4,8,16,32,64,128 and 257 evenly spaced points on [0,128]. Report error
over prefixes T=1,8,32,128 as well. All models use the same physical time.
No matched-loss endpoint is substituted for trajectory comparison.

Primary prediction error is the maximum, over the declared sampled times,
of RMS across the M training samples of f_scalar-f_dense. Labels have RMS one.
Also report maximum absolute training-loss difference, endpoint loss, each
sample's output curve, and loss curves. These are sampled-time measurements,
not certified continuous-time suprema. No held-out prediction or generalization
claim is attached to this first scalar test.

H1: order 4 is a useful nonlinear scalar approximation through T=128.
H0: aggregate feedback lost by the truncation causes large trajectory error,
instability, or no improvement over the frozen-kernel control.

- Per-case practical agreement: prediction error <=0.1 and absolute loss
  difference <=0.05, with numerical gates passed and no truncation failure.
- Per-case adverse result: prediction error >0.2, absolute loss difference
  >0.1, or finite-state escape/integration failure reproduced on refinement.
- Intermediate errors or unresolved numerical gates are inconclusive.
- Evidence of capturing nonlinear improvement additionally requires order 4
  prediction error <= half the frozen-kernel error, frozen-kernel error >=0.05,
  and dense activation RMS motion >=0.1 in at least one hidden layer by T.
  Report this separately from absolute agreement. A small control discrepancy
  cannot establish nonlinear efficacy merely by a ratio.

Overall label each case independently. Do not discard hard tasks, average away
divergence, tune the terminal law, add damping/PSD projection, fit coefficients
to dense paths, or present a favorable prefix as success through T=128.

## Numerical validity, pilots, branches and resources

Use float64 NumPy/SciPy on CPU, one worker with numerical BLAS threads fixed
to one. CUDA is currently unavailable; no GPU budget is assumed. SciPy DOP853
integrates both dense and scalar ODEs, with rtol 1e-7 and 1e-9, atol=rtol/100,
and max_step=2. Scalar terminal tensors are stored once, outside evolving
coordinates. No loss-decrease or positive-kernel constraint is imposed.

Before research integrations, deterministic tests must check canonical gradients,
kernel normalization, C and Q against independent directional differences,
the Dg_c[g_d] term, tiny noncommuting derivative cases, zero residual,
runtime payload size and own-state restart. An independently written dense
RHS or existing checked dense engine verifies the reference at a tiny state.

Two predeclared feasibility pilots use n=32 and the four-sample task, seed
20260920: one coefficient construction through order 4 and one dense/each-order
integration through T=0.25. Limit cumulative pilot time to 120 seconds.
Pilots test numerical feasibility only and are not independent efficacy data.
If coefficient construction fails the limit, stop and report implementation
feasibility rather than changing the scientific model after observing accuracy.

Numerical gate: each fine/coarse prediction change must be <=0.002 and
<=10% of the associated measured scalar-dense error (with a 1e-6 floor),
and loss changes <=0.002. Dense must meet the gate for each scalar pair.
If a gate fails, the affected dense or scalar model gets at most one further
run at rtol=1e-11, same horizon/max_step/atol rule. At most 32 conditional
refinement runs are allowed. Retain all resolutions; use one common finest
dense reference for all orders in that configuration.

Stop a scalar integration at |f|_infinity>=10 or any evolving scalar magnitude
>=1e12, nonfinite state, solver failure, 120 wall seconds per trajectory, or
the horizon. A protective stop is a recorded adverse candidate event if it
repeats on refinement. Compare predictions only where both runs exist and
report the full-horizon failure explicitly. If the candidate fails, do not
reinterpret partial overlap as full-horizon agreement.

For a complete configuration record dense hidden activation RMS changes and
kernel evolution. If neither task at either width/seed meets the nonlinear
motion/control gate by T=128, allow exactly the four-sample seed-20260920
n=256 configuration to extend to T=512 at both primary tolerances, for dense
and all orders (8 conditional integrations). Start from that model's saved
state; no dense-state reset of the scalar model. No extension is triggered
to rescue an already adverse aggregate approximation.

Repeat one n=128, four-sample, seed-20260920 fine coefficient construction and
scalar order-4 trajectory in a fresh directory to test reproducibility.
Check own-state scalar restart at t=1 on the same configuration separately.
This is operational evidence, not another scientific seed.

Hard total budget: 3600 cumulative measured computation-wall seconds across
initializers, pilots, primary/conditional integrations and repeats; 4 GiB
process memory target; one worker; at most 106 integrations including pilots,
conditional branches and repeat. Stop at the first hard budget regardless of
accuracy. If coefficient setup or a dense run exhausts a per-operation cap,
record it and skip dependent comparisons rather than inventing new settings.
Analysis/plotting and deterministic audit are separately limited to 300 seconds.

## Reproducibility and interpretation

Use fresh scalar_aggregate_* generated namespaces. Retain literal configuration,
initial aggregate tensors, timestamps, source/config hashes, Python/NumPy/SciPy
and platform details, seed/draw order, precision, all errors/failures, solver
statistics, sampled trajectories, terminal tensors and restart state.
Dense state arrays are for reference/audit only and are never passed to scalar
evolution after initialization. Record moving scalars, fixed scalar constants,
dense parameter count, initializer time, reduced runtime, dense runtime and
peak resource observations separately. Cheap evolution does not hide an
expensive initializer, and scalar-only runtime is not a population-limit result.

Independent saved-output rescoring checks labels, losses, error formulas,
thresholds, terminal-state preservation, source hashes and any claimed success.
All results, including failure, stay in the study. No promotion is requested.
