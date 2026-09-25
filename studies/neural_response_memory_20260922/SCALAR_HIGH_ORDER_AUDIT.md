# Orders five and six: internal implementation and saved-evidence audit

2026-09-25. This is a scoped internal check of the same-study higher-order
continuation, not an isolated promotion review. The checker performs only
small deterministic CPU checks; research trajectories and GPU work remain
producer-owned.

## Verdict

**PASS: 3,671 independent checks, including 294 deterministic checks.** The
complete receipt is
`data/generated/neural_response_memory_20260922/scalar_high_order_audit01.json`;
the checker is `check_scalar_high_order.py`. It covers seven initialization
actions, twelve scalar integrations, seven passive replays, both fixed seeds,
both conditional refinements, fresh reproduction, final numerical scores and
recorded computation costs. The complete check takes 60.50 seconds and uses
no GPU. Scientific gate failures below are retained as failures; an audit
PASS means that implementation and reporting agree with the evidence.

The analyzer subsequently corrected a reporting-only cost label: passive
preparation is attributed only to order five, which actually uses it. The
final analysis/manifest refresh passes 537 checks in
`scalar_high_order_audit_analysis02.json`; scientific metrics and figures
are unchanged. This refresh supplements the complete raw-data receipt.

| Quantity | Seed 20260920 | Seed 20260927 |
|---|---:|---:|
| Selected order-5 fitting time | 47273.897923 | 46088.041297 |
| Order-5 circle RMS discrepancy | 40.63438467 | 63.35941419, diagnostic |
| Order-5/order-4 error ratio | 1.03463242 | 0.99292506, diagnostic |
| Latest scalar refinement RMS change | 0.000520824 | 0.001251412 |
| Peak passive training-output gap | 0.0000864443 | 0.0001632108 |
| Order-5 direct-grid qualification | PASS, adverse | FAIL, consistency gap |
| Order-5 Fourier encoding through mode 256 | FAIL | FAIL |
| Order-6 fine stopping time | 1629.857895 | 318.604784 |
| Order-6 training outcome | Solver failure before fitting | Solver failure before fitting |

All seven order-5 integrations reach their own first detected MSE1e-6
crossing. All five order-6 integrations stop without a fitted endpoint.
The first order-5 result is 3.46% worse than order four. The second nominal
0.71% reduction is unqualified and also below the predeclared 1% improvement
margin. There is no resolved improvement for either seed and no matched
order-6 function. These are finite-width internal results, not a population
limit, hierarchy convergence result, or universal failure theorem.

Read completely: the frozen high-order protocol, initializer and derivation,
separate multijet oracle, scalar engine, both producer test files, and the
campaign runner, sequential launcher and final analyzer with its reused
same-study analysis dependencies. Previously scoped exact same-study engine
dependencies were also read. The installed SciPy BDF step/cache implementation was inspected. No
other study or Git history enters this audit.

## Ordered initialization and independent oracle

For a word w=(i1,...,ik), the derivative convention is
`A_w = D_ik ... D_i1 A`. The subset product rule preserves the relative order
of each subword and counts repeated indices as distinct positions. Applying
it to `D_i W_l = delta_l,i h_(l-1),i^T/n` differentiates both factors and
therefore includes the changes in the direction itself. The forward tanh
recursion and backward product rules retain the actual initialized matrices
and their transposes. No low-rank replacement of these matrices is made.
The canonical normalization and parameter mobilities are unchanged.

The oracle is algorithmically distinct: it carries full dense parameter
multijets with independent commuting square-zero variables, composes the
first-order flows in reverse word order, and extracts the full mixed
coefficient. It evaluates each direction at the current parameter jet.
Thus it retains moving directions without using the production recursion
for hidden fields. It shares the canonical model and basic validation helpers;
algorithmic independence is not independent authorship or scientific review.

The checker compares every T1 through T6 entry for two small noncanonical
fixtures with zero and substantial readout, tests arbitrary rectangular
probes, query and word batching, immutable input arrays, all repeated words,
and genuinely noncommuting last derivative axes. An independent outer
directional finite difference of the order-five oracle verifies the order-six
composition convention. T1 through T4 agree with the original producer.
Explicit antipodal queries agree at every order.

Oddness applies to every parameter value in the bias-free tanh model:
`f_theta(-u)=-f_theta(u)`. Parameter differentiation and application of the
unchanged training directions preserve this identity. It therefore permits
passive antipodal reconstruction at every derivative order. It does not
identify or remove any of the eight training directions.

## Exact Jacobian and structured BDF

Write alpha=2/M, v=-alpha(f-y), and w=gamma*v. For the Newton matrix
`I-gamma*J`, the j-th tensor equation is

    deltaT_j = b_j - alpha*gamma*T_(j+1):deltaf + deltaT_(j+1):w.

Eliminating the tensors from the highest degree down leaves an M-by-M
system for deltaf. In every kernel term the first and last axes remain
free; only the intervening axes contract against w. This order is essential
for nonsymmetric higher tensors. Local-signature increments are then solved
forward using their triangular dependence on deltaf and the previous level.
The implementation matches this elimination without approximating the
Newton linear system.

SciPy deliberately retains an existing factor after some error-based step
reductions. Each structured factor owns its original immutable Jacobian
snapshot and original gamma, so later state or step-size changes do not
silently alter a cached factor. The subclass inherits SciPy's step method,
convergence tests, error control and dense output. It changes numerical cost,
not the defining ODE or physical clock.

Independent checks cover every complex-step Jacobian column at orders two
through six, signatures enabled and disabled, real and complex forcing,
multiple right-hand sides, stale snapshots after state changes, and full
linear solves. The actual M=8, P=6 dimensions are checked with an independent
directional Jacobian and backward solve residual, avoiding a quadratic dense
allocation. Small deterministic integrations agree with ordinary sparse BDF
and an independent explicit reference. Generic order four agrees with the
original order-four RHS and Jacobian.

## Passive transport and runner review

The recentering formula is checked by explicit scalar index sums over the
old coefficient arrays, with extended precision at each boundary. The
terminal tensor remains unchanged. Two consecutive segments driven by a
nonconstant, noncommuting input path agree with independent integration of
the full passive chain. Resetting signatures preserves the directly
integrated training state bit for bit; changes to passive history have no
effect on the training RHS.

The runner retains segment endpoints before reset, rebuilds each training
model from its integrated tensors, and transports passive queries separately
from their original network initialization. Its expanded query ordering is
grid, off-grid, training checks, with exact negatives defining antipodes.
When a fitting crossing and signature boundary occur in one accepted step,
it selects the earlier detected event. The target is the first detected
downward MSE crossing, not an assertion about unobserved crossings within
accepted steps.

Two prelaunch review suggestions were resolved by the runner author:
whole-action wall/RSS checks now cover passive expansion and serialization,
and fitting-crossing brackets are retained for direct saved-data audit.
Resource-limited coefficient products cannot be used by integration or
replay. The final initializer also records timing components and enforces
wall/RSS limits after its optional antipodal expansion. These changes concern
resource accounting and reviewability; no mathematical defect was found.
The final-source receipt records all producer, test and derivation hashes.

## Completed saved-evidence checks

Actual source, input and output hashes pass. All initialized tensors are
finite with the prescribed scalar axes, GPU float64 settings and original
network hash. T1 through T4 agree with the prior width-2048 coefficients to
within the frozen bounds; the largest recorded first-seed difference is
8.33e-16. All eight literal training inputs and labels are retained.

Every archived training reset retains its old integrated tensors exactly.
The checker independently transports all passive tensors through every
saved segment using bounded-memory extended-precision matrix contractions,
after verifying those contractions against explicit scalar index sums.
Full-circle readouts, training-probe gaps, first-crossing brackets, final
states, accepted times and status records agree with the raw evidence.
The stored `accepted_steps` counter includes the final failed `solver.step()`
attempt in each order-six failure. It therefore exceeds the number of saved
accepted advances by one for those runs. The checker explicitly verifies
this convention; frozen producer records have not been rewritten.

Both primary order-5 tolerance pairs fail the 0.002 function-refinement
threshold, justifying exactly one declared finer run per seed. Their latest
pairs pass the function and physical-time refinement tests. The second
seed's passive consistency gap still exceeds 1e-4, so its function remains
diagnostic. No additional refinement is performed. Nested circle quadrature
passes for both seeds. All 64/128/256-mode Fourier attempts fail the strict
encoding gate; at mode 256 the off-grid RMS errors are 1.68367e-5 and
3.89813e-5. This separate encoding failure does not invalidate the first
seed's qualified direct-grid discrepancy.

Fresh first-seed T1 through T6 training coefficients and T1 through T5
passive coefficients are bitwise equal to the original arrays. The selected
order-5 reproduction has identical saved trajectory, endpoint and fitting
time. The order-6 fine reproduction has identical saved trajectory, stopping
time, status and failure message. Reproducing a nonfitted failure is recorded
separately from matched-endpoint qualification, which remains false.

## Interpretation of order-six loss growth

For M=8, the exact scalar identity is `L'/L=-rho/2`, where
`rho=(r^T Theta r)/(r^T r)`. A negative residual-aligned rate implies
instantaneous growth. Indefiniteness alone is insufficient. Negative rates
are already present at saved boundaries far before numerical termination,
and agree across tolerances: approximately -0.00451641 at t=850.768 for the
first seed and -0.00560923 at t=226.357 for the second. These are the first
saved negative-rate boundaries, not a claim of monotone growth thereafter.
The saved diagnostic is `scalar_high_order_audit_order6_kernel01.json`.

Minimum saved fine losses are 0.47345982 and 0.80117026. The last 100 saved
increments in each fine run are positive. The fine terminal effective rates
are -28878.8153 and -19184.6800, but terminal losses differ by orders of
magnitude between tolerances. Those terminal states are not numerically
qualified approximations. The first seed's order-six training-only passive
gap also reaches 2.49029e-4. The results support measured loss growth and
reproducible solver failure under these controls; they establish no
finite-time blowup or permanent nonfitting theorem.

## Recorded computation and resource budget

| Component | Recorded seconds |
|---|---:|
| Three training preparations, shared by orders five and six | 74.518 |
| One 32-query order-six pilot | 40.939 |
| Three order-five passive preparations | 162.331 |
| Eight primary integration launch receipts, including subprocess overhead | 133.055 |
| Two conditional refinements and two reproduction integrations | 102.571 |
| Seven passive replays | 66.090 |
| Recorded active-work subtotal | **579.504** |

The shared training preparation is counted once per seed or reproduction,
not once per order. Full-circle order-six coefficients were not computed.
Standalone action timings omit unrecorded process startup, source-copy and
scoring overhead; launch receipts include their subprocess overhead.
Concurrent CPU/GPU work is added, so this is an active-work subtotal rather
than an exact campaign elapsed stopwatch. It is well below the 10800-second
budget. No new dense training occurs in this continuation.

Peak recorded GPU allocation is 6268598784 bytes (5.838 GiB), from the bounded
order-six pilot, below 12 GiB. Peak process RSS is 1072603136 bytes
(0.999 GiB), below 8 GiB. All initialization and replay actions finish within
their caps. Order-six stops are numerical solver failures, not resource caps.
Selected order-five integrations take 22.41/27.11 CPU seconds, separate from
their 8.26/10.88-second passive replays and GPU preparation. These timings
do not represent accuracy-matched speedups against the dense GPU reference.

## Reproduction of this audit

The deterministic-only audit can be rerun as follows. The full audit accepts
repeated `--initialization`, `--run` and `--replay` directory arguments plus
`--analysis`, `--reproduction` and `--budget`. Its exact complete argument
list is retained in `scalar_high_order_audit_command01.json` alongside the
receipt. Paths in that argument list are relative to the repository root.

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  /home/amir/miniconda3/bin/python -B \
  studies/neural_response_memory_20260922/check_scalar_high_order.py \
  --output data/generated/neural_response_memory_20260922/scalar_high_order_audit_deterministic_new.json
```

The checker owns only its script, this report and `scalar_high_order_audit*`
generated receipts. No maintained-source, promotion or Git-index write occurs.
