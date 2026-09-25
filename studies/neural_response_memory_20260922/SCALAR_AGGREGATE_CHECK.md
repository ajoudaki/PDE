# Independent scalar aggregate checks

2026-09-25. This check is scoped to the new observable-generator scalar
hierarchy and its frozen protocol. It does not review unrelated study artifacts
or promote the approximation to established theory.

## Deterministic implementation audit

**PASS: 82 independent checks.** Final algebra receipt:
`data/generated/neural_response_memory_20260922/scalar_aggregate_audit01/algebra02/check.json`.
The receipt records the exact checker, candidate engine and protocol hashes,
Python executable and software versions. Check computation took 0.586 seconds,
excluding interpreter imports. This is deterministic validation, not a research
trajectory or an additional empirical seed.

The oracle writes the bias-free tanh network directly in Torch and differentiates
it with autograd in the original physical parameter coordinates, using diagonal
mobilities `(n,1,...,1,n)`. It does not call the candidate's jet routines or dense
RHS. Tests use width 3, three nonorthogonal inputs, and both two and three hidden
layers. Gaussian initialization is checked bit-for-bit, then the readout is
perturbed to make omitted derivative terms measurable.

Checked quantities and maximum absolute discrepancies:

| Check | Maximum discrepancy |
|---|---:|
| Scalar outputs, kernel, C, Q and dense RHS versus independent autograd | 2.00e-15 |
| Moving sample-direction derivative versus independent Hessian action | 3.33e-16 |
| C and Q versus centered directional differences | 8.78e-9 |
| Scalar own-state restart versus uninterrupted tiny integration | 8.33e-17 |

The directional-difference tests use step `2e-5`; their tolerance includes
finite-difference truncation. Direct autograd checks use absolute tolerance
`2e-10` and relative tolerance `2e-8`. All higher derivatives differentiate the
sample vector fields themselves. In particular, the full Q tensor includes
`Dg_c[g_d]`. Omitting that term changes Q by as much as 1.19 and 3.11 in the two
tested depths. Swapping the ordered second and third indices of C changes it
by as much as .216 and .447. These cases therefore distinguish the implemented
generator hierarchy from frozen-direction derivatives or a falsely symmetric
tensor hierarchy.

A direct test also swaps the final two derivative indices of Q. The independent
Q changes by .1703 and .5954 in the two depths, while the candidate agrees with
the correctly ordered autograd tensor to the tolerance above. The initial
80-check receipt `algebra01` remains preserved; `algebra02` adds these two checks.

For every scalar order, the checker independently contracts the next tensor
with `-2(f-y)/M`, verifies zero residual is absorbing and the RHS is autonomous,
checks pack/unpack consistency, and verifies that only degrees below the
terminal tensor are integrated. The terminal tensor is read-only, has exactly
`M**order` entries and remains bitwise unchanged. A short own-state restart
passes for all orders. These tests establish implementation consistency for
the tested inputs, not convergence of the frozen-terminal approximation.

Reproduction, with a new output directory:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  /home/amir/miniconda3/bin/python -B \
  studies/neural_response_memory_20260922/check_scalar_aggregate.py \
  --out data/generated/neural_response_memory_20260922/scalar_aggregate_audit_new
```

## Saved-run and reproduction audit

**PASS: 2294 checks across all eight configurations and their reproduction.**
Final receipt:
`data/generated/neural_response_memory_20260922/scalar_aggregate_audit01/saved_runs02/check.json`.
The preserved `saved_runs01` receipt covers the primary campaign alone;
`saved_runs02` adds the completed reproduction/restart evidence. These are
implementation and evidence checks. The approximation's scientific outcomes
are adverse below.

The independent scorer reads the saved arrays and uses no producer scoring
functions. It covers all 64 primary trajectories, 16768 observations and 320
saved checkpoints. All 80 dense checkpoints are reconstructed with the existing
independently checked Torch `DeepDenseEngine`, with their predictions, mobility-
weighted kernels and hidden activation motion recomputed. The largest observed
checkpoint discrepancy is 4.27e-14. Every scalar trajectory's predictions and
kernels are reconstructed from its saved scalar state; recorded losses and
kernel eigenvalues are recomputed. Source snapshot hashes, canonical
initialization hashes, coefficient hashes, case inputs, labels, state counts,
sample times, tolerances and completion claims pass.

All scalar-dense errors, refinement changes, prefix coverage flags and outcome
labels are independently rescored. The largest metric discrepancy is 2.23e-16.
Every primary trajectory completes through physical time 128. All numerical
gates pass and no conditional refinement run is required. Each configuration
has substantial measured dense feature motion and frozen-kernel discrepancy,
so the predeclared extension condition is false.

The order-4 result is adverse in every configuration under the frozen criteria:

| Task | Width | Seed | Maximum sampled prediction RMS | Maximum loss difference |
|---|---:|---:|---:|---:|
| Equal mixed odd | 128 | 20260920 | .692114 | .515917 |
| Equal mixed odd | 128 | 20260927 | .571352 | .410711 |
| Equal mixed odd | 256 | 20260920 | .414292 | .300888 |
| Equal mixed odd | 256 | 20260927 | .828069 | .718088 |
| Quadrant alternating | 128 | 20260920 | .895164 | .883457 |
| Quadrant alternating | 128 | 20260927 | .735479 | .762677 |
| Quadrant alternating | 256 | 20260920 | .859377 | .860134 |
| Quadrant alternating | 256 | 20260927 | .861704 | .839344 |

The four-point order-4 endpoint losses are nevertheless between 5.00e-17 and
6.80e-12, and endpoint prediction RMS differences from dense are between
7.07e-9 and 2.61e-6. Agreement at a fitted endpoint would therefore conceal the
large discrepancies during learning. The reported failure concerns the frozen
matched-physical-time trajectory criterion, not merely ability to fit labels.

The independent reproduction check verifies all four newly recomputed
aggregate tensors and all 13 scientific arrays in the repeated trajectory
bit-for-bit, including saved checkpoints. The own-state restart begins at the
saved scalar state at time 1. Its maximum prediction RMS change is
4.62357e-8, maximum loss change 1.25555e-10 and maximum scalar-state change
6.04718e-8. These pass the recorded numerical gate. Reproduction and restart
use neither fresh dense trajectories nor resets from dense states.

Source inspection confirms that `ScalarHierarchy` retains only labels,
sample-indexed initial scalar coordinates, its terminal scalar tensor and
shape metadata. Its RHS uses tensor contractions on its own state; no network,
population or initialized hidden operator is retained. The initializer's use
of dense neural arrays is separate and explicit. This satisfies the stated
scalar-runtime information contract, while the accuracy test rejects this
specific order-4 frozen-terminal witness on the tested configurations. It
does not disprove the broader existence of useful finite scalar models.

Reproduce the complete saved-output audit without running new research flows:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  /home/amir/miniconda3/bin/python -B \
  studies/neural_response_memory_20260922/check_scalar_aggregate.py \
  --runs data/generated/neural_response_memory_20260922/scalar_aggregate_primary01 \
  --reproduction data/generated/neural_response_memory_20260922/scalar_aggregate_reproduction01 \
  --out data/generated/neural_response_memory_20260922/scalar_aggregate_audit_new
```
