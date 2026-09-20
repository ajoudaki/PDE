# C-H3 depth closure: predeclared operational checks

Declared before test execution, 2026-09-20. These are deterministic verification
and bounded finite operation of the authorized contract implementation. They
are not a neural training campaign, an empirical proof of convergence, or a
claim that a tested finite order approximates the target to a known tolerance.

## Decision and controls

Check that the implemented multiedge initializer and finite closure implement
their stated equations, retain each actual transpose, and restart with complete
current state. Alternatives to exclude are cross-matrix source mixing, missing
reuse response, wrong metric factors, and an incomplete restart state.

Independent controls: exact Gaussian-source covariance/derivative identities
for tiny programs; parity with the maintained two-population compiler and
two-layer solver; explicit dense weighted action and numerical differentiation
of the finite closure's scalar loss; exact same-backend restart comparison.
Use d=2,3 and L=2,3,4 in algebraic checks. No random-network width is present.

Algebraic gates: identity/parity discrepancies <=1e-11 in float64 unless a
test explicitly uses a finite-difference gate <=3e-6; exact checkpoint working
values and deterministic resumed state; finite arrays and strictly positive
resolved regularized Cholesky pivots. Check matrix groups and response support
exactly. Unresolved pivots/nonfinite arrays are failures, never rank deletions.

## Operational configurations

Use L=3,d=2, original C-H3 ArcLaw with p=1/2 and a=c=-1/20,b=d=1/20.
Each configuration starts independently from its prescribed initializer and
evolves through t=1/200. This horizon exercises implementation only; the new
local theorem supplies a positive depth-dependent horizon and need not certify
the literal 1/200 at L=3. Use four input nodes per arc initially.

Run these five configurations, no adaptive replacements:

| ID | order N | initializer Q | population P | steps | nodes per arc |
|---|---:|---:|---:|---:|---:|
| a | 1 | 64 | 32 | 8 | 4 |
| b | 3 | 64 | 32 | 8 | 4 |
| c | 5 | 64 | 32 | 8 | 4 |
| d | 3 | 128 | 64 | 16 | 8 |
| e | 1 | 64 | 32 | 16 | 4 |

All use float64 and source regularization epsilon=1/10000. Retain every
declared feature and use ridge 1/[1024(N+1)^2]. At halfway, serialize the full
state/law; finish both directly and from disk and compare exact working values.
Record predictions on the fixed 16 rational directions obtained by U(k/8),
k=-8,...,7, paired motions for all three layers, risk, initializer/evolution/
restart timings, peak process RSS, retained-state bytes, normalized and raw
regularized Gram condition diagnostics, and source/configuration hashes.
Refinement differences are diagnostics only and have no pass threshold.

Successful finite completion, finite observations, reported diagnostics, and
exact own-state restart are the operational pass criteria. Neither monotone
accuracy nor a neural target-error certificate is inferred.

## Hard limits and stopping

One numerical thread and one worker. Deterministic checks: at most 240 CPU
seconds total (120 assigned to solver agent, 120 initializer/root). Operational
checks: at most 120 wall/CPU seconds per configuration, 600 cumulative CPU
seconds, and 2 GiB process memory. Compiler allowances: max_nodes=20000,
max_sources=2048, max_points=1024, max_working_bytes=1 GiB,
max_work_units=100000000000, max_scalar_bits=65536. These are conservative
preallocation estimates, distinct from actual measured work/RSS.

Generated logs, checkpoints and observations go to a fresh directory under
data/generated/cx3_depth_extension_20260920/. Preserve failed configurations.
Correctness defects may be fixed and deterministic checks rerun within the
total check budget; archive prior failures. Stop the operational sequence on
a resource breach rather than searching for favorable replacement settings.
All observed outcomes update only implementation/operation claims. The
mathematical convergence and finite-network identification require proofs.
