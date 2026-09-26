# Standalone scalar ODE and challenging circle validation

**Status: experimental campaign cancelled before training, 2026-09-26.**
The user's latest instruction is to consolidate the code but run no new
experiments if the construction retains the dictionary limitation. The
structural assessment establishes that fixed-span restriction. No new neural
trajectory runs were launched. Only consolidation, deterministic algebra checks,
and documentation remain in scope. The experimental plan below is retained as
an unexecuted proposal; it is not a pending campaign. The standalone CLI has no
automatic campaign command.

2026-09-26. User-authorized continuation of the response-basis construction.
Freeze before consolidated implementation and new trajectory runs. Root owns
this protocol, benchmark/analysis integration, results and README. scalar_bundle
owns the standalone core until handoff; scalar_circle_design supplies a scoped
task compatibility check and subsequent scoring audit. Existing sources and
results remain intact. No book/API promotion or Git write is requested.

## Construction and question

Create one portable `scalar_ode.py` containing the current fixed-response-basis
scalar model, initializer, dense reference, terminal weight decoder, generic
label-aware fitting routine, benchmark CLI, saved-model prediction CLI, and
algebra self-check. NumPy/SciPy and the standard library are sufficient;
matplotlib may be imported optionally for figures. No local-module imports.
This bundles the current successful method, not the earlier unrelated tree,
Fourier or polynomial-potential prototypes. Preserve the numerical model:
three hidden tanh layers, no biases/normalization, physical mobilities
(n,1,1,n), mean squared error, output c^T h3/n, unit circle directions already
including the input normalization, standard-normal first weights, hidden
entries N(0,1/n), readout entries N(0,1/n^2). Preserve sequential NumPy draws
and the basis feature ordering/SVD/sign/completion policy exactly.

H1: fixed ranks retain useful dense-function agreement beyond the two-point
witness, including clustered, oscillatory and restricted-support training.
H0: missing response directions/decoder consistency cause substantial error,
possibly despite internal fitting. A dense failure to fit is a third outcome,
not evidence that compression is inaccurate at fitted endpoints.

## Frozen tasks

Angles are degrees in this table; trigonometric formulas use radians.
Every task is compatible with f(theta+pi)=-f(theta). No training labels are
changed in response to an outcome.

| ID | Training angles | Labels / known target |
|---|---|---|
| two_point | 10,125 | +1,-1; no asserted full-circle target |
| close_pairs | -1,1,59,61,119,121 | -1,+1,+1,-1,-1,+1; optional smooth target tanh(3 sin(3 theta)/sin(3 degrees))/tanh(3) |
| quadrant_alternating | 5+10j, j=0,...,7 | (-1)^j; no asserted full-circle target |
| harmonic3_full | 7+30j, j=0,...,11 | sqrt(2) sin(3 theta) |
| harmonic5_full | 7+22.5j, j=0,...,15 | sqrt(2) sin(5 theta) |
| harmonic5_arc | 10+10j, j=0,...,7 | sqrt(2) sin(5 theta); only the 10–80 degree arc is labeled |

The close-pair angular separation is two degrees. The quadrant task requires
seven sign changes inside 70 degrees. Full harmonic panels include redundant
antipodal constraints; their effective distinct directions are six/eight.
The arc task tests extrapolation and is reported separately inside/outside
the observed arc and its antipodal copy. Known-target scores measure task
generalization separately from approximation of the dense fitted function.

## Runs, metrics, and gates

Pre-run amendment, before any trajectory: include matched old-clock population
P1 and P3 to test the fixed-dictionary concern against the evolving-history
construction. The scalar equations and all tasks stay fixed. The standalone
file includes these baselines through a generic PopulationReference; they are
labelled as population methods, not scalar-only compression. Refine P3 too.

Primary width64; seeds20260920 and20260921. For each of six tasks and each
seed, run dense, population P1/P3, and scalar ranks12,24,40: 72 primary fits. All ranks and both
seeds are reported, with no best-seed or per-task rank selection. Track four
passive inputs at12.5,57.5,102.5,157.5 degrees. They enter no training sums or
basis selection. Evaluate decoded and dense networks AFTER fitting on4096
uniform circle angles with half-grid offset; those angles are never evolved
inside the scalar ODE.

Use float64 DOP853, target MSE.001 (training RMS0.0316228), horizon1000,
rtol1e-7/atol1e-9. Same settings for every task, seed and model. Store training,
passive and decoded training outputs, parameter endpoints, initial provenance,
coefficient tables, decoder arrays, trace data, state/static-table size and
timing. Compare independently fitted endpoints and also passive outputs at
the earlier of the two stopping times using accepted-state interpolation.
Never extrapolate beyond a trajectory's computed interval.

Primary metric: decoded network versus matching dense whole-circle RMS.
Call it good agreement only when dense and scalar reach the internal target,
decoded training RMS<=.05, and decoded circle RMS<=.05. Errors>=.10 are
substantial; intermediate values remain intermediate. Report internal passive
RMS/max and internal/decoder disagreement separately. Failure to fit, numerical
failure, timeout or invalid refinement makes fitted-model interpretation
inconclusive; retain available accepted endpoints with explicit status.
No predicted-target accuracy claim follows from dense agreement alone.

Diagnostic (post-fit only): evaluate dense activation and backward-response
escape from each candidate's original fixed bases, plus hidden-feature movement.
For each dense learned middle increment D, compare ||D-P_l D P_prev||_F with
its best unrestricted rank-r SVD tail. These are representation diagnostics,
not coefficient fitting, lower bounds on output error, or additional training.
Record ratios to ||D||_F and avoid attributing output discrepancies solely to
this source when decoder consistency and changed trajectories also contribute.

## Verification and bounded follow-up

Before the primary campaign, algebraically compare consolidated initialization,
fixed coefficients, initial/nonzero-state RHS and decoder to original modules;
verify canonical dense gradient by finite differences, passive independence,
all-rank loss dissipation, full-rank response-lift identity and isolated import.
The standalone `self-check` requires no original module. A separate migration
audit may import the original modules for comparison. Correctness checks have
300 CPU seconds total and do not choose scientific hyperparameters.

Regression: rerun the original width16,seed20260920,two_point task at ranks12
and16 plus dense, with the OLD passive panel30,60,90 and horizon40. All previous
fitted output predictions must agree within1e-5. Full rank16 is a validation
control, never counted as compressed success. Three regression trajectories.

Numerical follow-up: for seed20260920 only, repeat dense, P3 and rank40 on all six
tasks at rtol1e-9/atol1e-11, with every other setting unchanged: eighteen fits.
If either original cell failed numerically or timed out, retain the refinement
as diagnostic, not a silently substituted primary result. A fitted endpoint
comparison passes refinement if decoded-circle RMS change and passive maximum
change are each<=.002. No other rank/tolerance/seed/architecture/initialization
search follows. Stop after these checks regardless of outcome.

## Resource and provenance contract

Each fit:30 solver wall seconds, state magnitude cap1e8 and nonfinite guard;
retain accepted states only. Each preparation:30 seconds,3GiB RSS. At most
three single-thread CPU worker processes. The pre-run population-baseline
amendment sets at most93 fits (72 primary,3 regression,18 refinement),2790
maximum solver seconds and up to930 anticipated preparation seconds inside
a4500-second cumulative worker-phase allowance. Each preparation still has
a30-second hard cap; the controller reserves at least preparation+solver
hard limits for in-flight jobs rather than assuming anticipated preparation.
The campaign controller also imposes a45-minute elapsed deadline measured
from the first regression fit, and refuses new work without the remaining
reservation. Algebra and post-fit plotting are outside solver time but timed
and reported. No GPU experiments are needed. No dynamic cap increases.

Use fresh `data/generated/neural_response_memory_20260922/scalar_standalone01/`.
Save commands, source/protocol hashes, exact inputs/labels, seeds, environment,
CPU/BLAS thread settings, initialization hash, raw arrays, all failures and
machine-readable scores. Standalone serialization uses JSON/NPZ rather than
requiring old Python modules. Root will provide a short user guide and complete
outcome table. These are internal finite-width empirical checks; no general
rank-versus-accuracy or total-memory advantage is asserted.
