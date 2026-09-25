# Orders five and six on the eight-input circle task

2026-09-25. The user explicitly requests orders5 and6 to test whether the
improvement from order2 to order4 continues. This is an authorized continuation
of the scalar experiment in this study. Freeze this design before higher-order
research execution; implementation and deterministic verification may precede it.

## Model, hypotheses and information

Use exactly the width2048, three-hidden-layer tanh quadrant_alternating task,
the eight literal inputs and seeds20260920/20260927 from SCALAR_WIDE_PROTOCOL.md.
Reuse its audited fine GPU dense endpoints and order2/order4 controls. No new
dense training is required. All parameter draws, mobilities, normalization and
unhalved MSE remain unchanged. There is no population-limit claim.

Let T1=f, T2_ab=D_b f_a, and T(j+1)_(a1,...,aj,b)=D_b Tj_(a1,...,aj), where
D_b=(B grad f_b) dot grad. For orderP, freeze TP at initialization and evolve
Tj'=T(j+1):v for j<P, v=-2(f-y)/8. Derivative axes remain ordered; no clipping,
symmetrization, damping, trajectory fitting or dense refresh is allowed.
Passive queries have their first axis at a test input and every other axis
at a training input. Their coefficients are evaluated only at the original
network initialization, even if computed after a training-only screening run.
The scalar RHS uses only scalar tensors, labels and local ordered signatures.

H1: orders5/6 reduce matched-loss circle error beyond order4 in both fixed seeds.
H0: additional exact initial derivatives fail to improve the final function,
or the higher-order truncated dynamics do not attain a qualified fitted endpoint.
A resource cap or failed numerical gate is inconclusive, not proof of permanent
nonfitting or divergence of the entire hierarchy.

## Primary comparison and validity

Each scalar run starts at timezero and stops at its first detected downward
crossing of MSE1e-6, physical cap1e9. Compare its circle output with the same
seed's previously validated dense MSE1e-6 endpoint, using1024 uniform angles
and32 fixed off-grid angles. Report absolute RMS, relative RMS, maximum error,
physical fitting time, integration/initialization cost and scalar counts.
The primary order comparisons are E5/E4, E6/E4 and E6/E5, separately by seed.
Call an improvement resolved only if the reduction exceeds1% of the lower-order
error and ten times the sum of the two scalar refinement changes and the dense
refinement change. Agreement with dense remains RMS<=.1, adverse RMS>.2.
Mixed seed outcomes or unresolved changes are reported individually; no new seed
is selected. Improvement in two further orders is not a convergence theorem.

Use implicit BDF with exact Jacobian and algebraically exact block elimination
of the Newton linear system. Primary rtol1e-7/1e-9, atol=rtol/100. This changes
numerical solution cost, not the ODE. Local signatures reset at
max_k(max_abs(sigma_k)/64^k)=1; the integrated training tensors are retained.
Transport passive coefficients from their previous anchor with all signatures
through orderP-1 in extended precision. No reset to dense information occurs.

Require fitted statuses, endpoint coarse/fine RMS change<=.002 and<=10% of
scalar/dense discrepancy (floor1e-6), fitting-time relative change<=.001, and
passive training-output RMS gap<=1e-4 throughout saved segment boundaries.
If these fail for a fitted pair, one rtol1e-11 run is permitted for that
order/seed; compare the latest two. Missing fitted endpoints are recorded,
without retuning the closure. Keep direct-grid validity separate from encoding.
Nested512/1024 error change must be<=.001 and<=1% of error (floor1e-6).
If needed, one2048-point passive reevaluation is allowed per seed, replaying
saved scalar segments and saved dense parameters without retraining.
Fourier modes64, conditionally128 then256, must give grid/off-grid RMS<=1e-5
and max error<=1e-4 for the optional encoded-function claim.

## Exact initialization and implementation checks

Compute ordered derivatives with exact product/chain rules and low-rank
parameter-direction actions, retaining actual initialized matrices/transposes.
GPU float64, deterministic algorithms and TF32 disabled. A separate small-width
square-zero multijet oracle must verify T1 throughT6, including moving directions,
repeated indices and nonzero readouts. Compare T1..T4 at width2048 against the
previously audited coefficients with max difference<=1e-11+1e-9 max magnitude.
Check genericP4 dynamics against the old implementation, Jacobians against
independent derivatives, and structured Newton solves against full linear solves.
Check recentering with multisegment passive/training identities.

First compute training coefficients only, shared by orders5/6. One first-seed
training-only initializer and one32-probe throughput block form a bounded
feasibility pilot. They may supply original coefficients to primary runs;
their timing does not select scientific outcomes. Exact oddness permits
initializing512 grid and16 off-grid queries and reconstructing their antipodes
by a minus sign. Verify explicit antipodal queries in deterministic checks.
If an order attains the training target, compute its required passive original
coefficients and replay its archived scalar segments. Compute no larger passive
order than required by fitted runs. Train inputs remain explicit probe checks.

## Replication, budgets and stop

Two fixed seeds and two integration tolerances give8 primary scalar runs.
At most4 conditional finer runs, one full first-seed fresh coefficient generation
and fine integration for each fitted order, and one conditional spatial panel
per seed are allowed. Reproduction repeats coefficients, scalar integration
and passive endpoint from scratch in fresh directories; require the same
endpoint/time gates. A nonfitted order is repeated at the same fine settings
to check reproducibility of its failure/cap if budget permits. No dense rerun.

One GPU worker, GPU1 when available, max12GiB allocated; process RSS max8GiB.
One CPU scalar worker with one numerical thread. Pilot limits:600s training-only
initialization and300s32-probe block. Each primary/reproduction training
initialization has600s; each full passive initialization has2400s; each scalar
integration has600s and100000 accepted steps. The cumulative active research
wall budget is10800s, including pilots, initialization, integration and replay,
excluding waiting for a GPU and ordinary deterministic implementation tests.
Stop on budget/cap and retain all partial evidence. The bounded campaign ends
after declared comparisons/reproduction or exhausted limits, regardless of
scientific outcome. Unused budget authorizes no additional order, width or task.

Root owns protocol, runner, results and README. scalar_wide_dense_gpu owns
scalar_high_order_initialization.py, its independent small multijet oracle,
tests and derivation. long_time_scalar_design owns scalar_high_order_engine.py
and tests. A separate scoped checker audits the implementation and saved evidence.
Generated products use scalar_high_order_* in this study. Earlier wide results
are retained unchanged; no maintained-source, promotion or Git-index write.
