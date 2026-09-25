# Autonomous moment-closure experiment protocol

Frozen before GPU trajectories, 2026-09-24. User explicitly authorized a concrete
first-principles construction and numerical comparison on earlier hard tasks.
This continues the response-memory study; older empirical inputs are narrowly
authorized for matched reproduction. No external theory or unrelated study
conclusions are imported. Both available GPUs are used.

## Candidate and questions

Replace only the integrated rank-one middle-layer gradient by products of
evolving response-history moments. Retain the actual initialized W0 and its
transpose. Outer-layer updates, loss, initialization and activation stay
canonical. A rational lift evolves the training responses and residual RMS.
Its exact continuous equations agree with tanh on the initialized invariant
manifold. The sole physical defect is the explicitly derived middle-layer
covariance defect. Moments admit exact derivative-memory coordinates; they
are not a truncated time Taylor series or freely trained dictionary.

Two constructions derived before results: rational activity bins from
RATIONAL_CANDIDATE_ROUTE.md, eta=1e-3/P**6; and orthogonal projection of response
histories on their current activity interval. The latter is the primary
candidate, because compactification assigns coarse resolution to late learning
when cumulative activity is large. It uses a virtual prefix of fixed length1
with zero backward source and constant initial forward response; this adds
exactly zero to the dense history integral. Its theory and code must be frozen
before its runs. The bins candidate is limited to a P=1 diagnostic if useful.
No fitted gate centers, teacher trajectory, label changes or random restarts.

## Fixed primary comparison

- n=2048, two hidden tanh layers, canonical NumPy seed20260920; exact archived
  first-layer, middle-layer and readout initial arrays must match bitwise.
- Eight compatible inputs in each of two original cases:
  two_outliers_alternating and quadrant_alternating. See frozen
  HARD_BENCHMARK_INPUTS.md for literal data, normalizations and references.
- Unhalved mean square loss and original block mobilities (n,1,n).
- P=1,3,7, corresponding to at most 8,24,56 learned matrix rank and 16,48,112
  history vectors. Retained training responses are additional state.
- Own first training MSE0.001 crossing; 8192-node circle prediction RMS versus
  archived dense own endpoint, nested4096-grid check, and matched-time RMS at
  archived snapshots. The full-circle labels are undefined: this measures
  approximation to dense learning, not a test-label error.
- Baselines: prior derivative p3,p5,p7 and nearest vector-count old dictionary,
  Gaussian and orthogonal controls, with original numerical validity flags.
  New method retains dense W0, unlike dictionaries compressing the whole
  middle matrix. There is no claim of matched total storage or compute.

## Numerical controls and bounded branches

Float64 CUDA, deterministic arithmetic, TF32 disabled. Adaptive Heun with
Euler difference, starting step0.05, maxstep2.0. Control moving coordinates
and the induced learned-matrix Frobenius error through low-rank factors.
No loss-monotonicity rejection: a modified physical field can be nonmonotone.
Stop at physical time10000, 30000 accepted steps or 240 seconds per trajectory.
The whole campaign is capped at 3600 GPU-seconds of integration, at most
20 trajectories (short invariant checks excluded). Two workers share no outputs.

Primary tolerances rtol6.25e-5, atol6.25e-7; refinement divides both by4.
All reported successful primary levels are refined. Endpoint sampled maximum
primary/refined discrepancy must be <=0.01. Nested circle RMS discrepancy
must be <=1e-5. Lifted h1/h2 maximum consistency drift must be <=0.001 and
decrease under refinement. Failure triggers one further refinement or direct
tanh-coordinate parity check within the same total budget; otherwise flag
the cell unresolved. Do not interpret numerical drift as closure benefit.

CPU identity tests must check the exact initial canonical derivative, shared
forward/transpose action, derivative of K, and rational response tangency.
Endpoint states and all trajectories are saved under a fresh study-owned run.
If the two primary tasks pass numerical controls, quadrant_pairs is an
optional compatible third-case check at P=3,7 with refinement, budget allowing.
P=15 is permitted only when P=7 has larger approximation error than0.1 and
the P=3 to P=7 trend improves, or as a labeled resolution diagnostic for the
orthogonal-history branch. No extra task or new seed is allowed.

## Claim gates

Compatible sample geometry is not itself a global tracking theorem. Any
all-time approximation claim must state source, total-activity and stability
hypotheses explicitly. Finite runs can establish these errors and invariants
on these realized trajectories only. No asymptotic rate is inferred. An
independent scoped checker audits the formula, saved predictions, reference
selection and numerical gates before synthesis. Failed outcomes are retained.

Pre-outcome numerical clarification: runner status `fit` records a lifted-loss
crossing, not a validity verdict. Require recomputed physical training MSE to
be within 1% of0.001 as well as the activation drift/refinement gates before
reporting a valid endpoint. This was added immediately after independent
review and before observing any numerical trajectory output.

## User-authorized additional tasks (2026-09-24)

During the initial campaign the user explicitly requested two or three further
hard original tasks. In addition to quadrant_pairs already under way, select
quadrant_center_edges and equal_mixed_odd: the next two by the larger of the
old45-vector and derivative38-vector errors, among remaining original cases.
The addendum ADDITIONAL_BENCHMARK_INPUTS.md records selection and references.
No rotation, negative control, label change or seed change is introduced.

Complete P=1,3,7 at primary/refined levels for all three additional tasks.
For equal_mixed_odd merge its redundant opposite-label antipodal pairs into
four uniformly weighted representatives. Oddness makes the original eight-
point loss and gradient exactly equal to this four-point form for every
parameter value. This produces compatible representative inputs and lowers
its history-vector count to8P. Save original and used data explicitly.

The prospective total campaign cap is now44 trajectories and3600 integration
GPU-seconds (unchanged time cap). The initial20 trajectories remain frozen
and counted. Preserve the original runner as run_moment_experiment_initial.py
before extending the active runner; new outputs record its revised hash.
All existing numerical gates, including sampled trajectory activation maxima,
remain in force. Optional further levels are only for failed numerical gates.

Dense reference refinement branch: when the selected moment error is less
than three times the archived dense primary/refined RMS change, run fresh
canonical dense references at rtol1.5625e-5 and3.90625e-6, atol=rtol/100, under
the same initialization and loss crossing. At most four cases, two levels
each, fit inside the44-run cap with the planned34 closure trajectories.
Keep archived-reference metrics for comparison with frozen old baseline
scores, and report fresh-reference sensitivity separately. Baseline prediction
arrays must be re-evaluated against a changed reference before making any
comparison against that changed target. Reference refinement differences are
empirical numerical sensitivities, not certified exact-flow error bounds.
