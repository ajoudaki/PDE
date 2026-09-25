# Width-2048 internal independent audit

2026-09-25. Scoped independent implementation and saved-data checker for the
same-study width-2048 continuation. This is an internal check, not an isolated
promotion review. No dense or scalar research training is performed by this
checker. It does not use a GPU while the research worker is active.

## Verdict

**PASS: 1,693 checks, including 123 deterministic checks.** The complete
receipt is `data/generated/neural_response_memory_20260922/scalar_wide_audit02.json`;
it supersedes the 1,650-check receipt by adding explicit task, solver-control,
pilot and budget checks. The checker is `check_scalar_wide.py`.

All 18 research trajectories (eight primary GPU dense, eight primary scalar,
and the mandatory dense/scalar reproduction pair) reach their own training
MSE target of 1e-6. All four configurations pass integration, spatial and
Fourier encoding gates, and the required first-case reproduction passes.
The resulting accuracy classifications are distinct from these validity gates:

| Task | Seed | Dense fit time | Order-4 fit time | Circle RMS difference | Relative difference | Accuracy verdict |
|---|---:|---:|---:|---:|---:|---|
| Four-input mixed | 20260920 | 16.64417 | 43.62712 | 0.174756 | 0.194521 | Inconclusive |
| Four-input mixed | 20260927 | 16.68637 | 45.69360 | 0.170470 | 0.189853 | Inconclusive |
| Eight-input alternating | 20260920 | 158.01653 | 46056.59843 | 39.274223 | 25.900835 | Adverse |
| Eight-input alternating | 20260927 | 154.44870 | 47815.43517 | 63.810872 | 41.414386 | Adverse |

Times in this table are the original gradient-flow times, not computation
seconds. These are internally checked finite-width results; they establish
neither population convergence nor a general impossibility theorem.

## Completed implementation assessment

The new initializer was read completely together with its derivation and
five deterministic tests. Its rank-one direction actions and rank-two
moving-direction actions are exact algebraic factorizations, not replacements
for the initialized dense Gaussian matrices. Both the actual matrices and
their actual transposes remain in the forward/backward responses. The
normalization is unchanged: hidden matrix actions have no added division by
n, the output has division by n, and internal parameter directions have
division by n. All four mixed backward product-rule terms are retained;
the last two Q indices remain ordered.

Independent small-array checks compare every f/Theta/C/Q tensor against the
complete legacy initializer at both depths, including zero and substantial
readouts, rectangular probes, different batch partitions, input immutability,
and noncommuting derivative directions. Zero-readout C vanishes while Q
remains nonzero in the chosen fixtures. These checks pass. All four stored
width-2048 training kernels are exactly symmetric; no symmetry repair is
needed for their frozen-kernel controls. The mandatory width-2048 comparison
against the original initializer on four probe points also passes for every
stored coefficient tensor.

The dense GPU adapter and the complete reused dense engine, adaptive
controller and event interpolant were read. The actual dense RHS uses the
canonical mobilities (n,1,1,n) and original normalized inputs. An independent
CPU algebraic check compares predictions, every RHS block, both Heun stages
and the quadratic event interpolant against NumPy formulas. It advances no
research trajectory and performs no GPU work.

The adapter preserves NumPy initialization bit for bit on transfer, records
the parameter/data/source hashes and device/precision settings, disables
TF32, and requires deterministic algorithms. It has no silent CPU fallback.
The event bracket uses model forward loss and retains the at-or-below-target
side after bisection. The adapter now checks GPU allocation and process RSS
limits before and after steps and at setup/readout/serialization boundaries.

Two pre-execution implementation concerns were resolved by the authors:
explicit memory-cap enforcement in the GPU adapter, and coherent refined
probe metadata/grid sizes in the predeclared spatial-refinement branch.
These fixes do not change the model or its numerical acceptance criteria.

After all primary coefficient initializations finished, a file-discovery bug
in `run_scalar_wide.py` was corrected: three `*_resolution*` searches now
retain directories only. This prevents adjacent configuration files from
being parsed as run directories. The original preparation snapshots remain
intact; reproduction snapshots contain the correction. A direct comparison
of the two source versions shows only these three directory filters. No
initializer, model equation, solver, event definition or scoring threshold
changed. Source versions are therefore distinguished rather than silently
presented as identical.

## Dense feature movement diagnostic

The four fine dense endpoints were evaluated at their training inputs, and
their initial activations were regenerated from the original NumPy seed.
The saved analysis is `scalar_wide_audit_feature_movement01.json`. For each
hidden layer, the diagnostic is RMS(h_final-h_initial)/RMS(h_initial), with
RMS taken across all neurons and training inputs.

| Task | Seed | Layer 1 | Layer 2 | Layer 3 |
|---|---:|---:|---:|---:|
| Four-input mixed | 20260920 | 0.5699 | 0.8104 | 1.2081 |
| Four-input mixed | 20260927 | 0.5639 | 0.8196 | 1.2121 |
| Eight-input alternating | 20260920 | 1.0373 | 1.5185 | 1.5002 |
| Eight-input alternating | 20260927 | 1.0321 | 1.5014 | 1.5061 |

Absolute activation RMS changes are 0.354–0.499 for the four-input task and
0.611–0.738 for the eight-input task. These substantial changes support a
nonlazy finite-width target at width 2048. They do not establish a limiting
population model or width convergence. No training was performed to obtain
this diagnostic.

## Completed saved-data checks

The checker independently reconstructs every scalar passive segment and
milestone using its old anchor, verifies unchanged training states and frozen
Q, and reevaluates dense training, grid and off-grid predictions from the full
saved 2048-wide parameters. It verifies exact task and initialization
provenance, source/array hashes, declared tolerance controls, accepted-step
errors, first-loss-crossing brackets, resource limits, and all integration,
spatial, Fourier and reproduction scores. Scalar integrations begin at zero;
probe readouts never feed back into training.

Across the four cases, the largest change in the dense circle function on
tolerance refinement is 9.20e-5; the largest scalar change is 3.26e-5. The
largest 64-mode reconstruction errors are 4.41e-6 grid RMS, 5.51e-6 off-grid
RMS and 2.18e-5 off-grid maximum. The largest 512-versus-1024 quadrature change
is 5.66e-8. All satisfy the frozen protocol. No conditional extra tolerance
or spatial refinement was needed.

The mandatory fresh eight-input seed-20260920 reproduction has bitwise equal
initial and passive coefficient arrays, and exactly matching saved dense and
scalar endpoint times and predictions. Frozen-kernel spectral controls were
independently reconstructed with their residual-integral identity: their fit
times are 1473.37968 and 1406.06073 for the four-input seeds, and 169283590.79877
and 194628259.54626 for the eight-input seeds. Their circle RMS differences
from dense are respectively 0.191298, 0.192063, 160.449303 and 193.554558.

## Recorded computation and resource budget

| Recorded component | Seconds |
|---|---:|
| Primary GPU launch receipts, including subprocess overhead | 149.946 |
| Primary scalar-lane launch receipts, including three initializations and subprocess overhead | 121.417 |
| First primary initialization, outside those receipts | 82.655 |
| Bounded 40-step GPU pilot | 2.382 |
| Fresh reproduction initialization | 59.820 |
| Fresh reproduction GPU dense work | 29.180 |
| Fresh reproduction scalar work | 6.592 |
| Recorded active-work subtotal | **451.991** |

The three initializations already included in the scalar launch receipts are
not counted twice. The first initialization includes the mandatory original
initializer comparison. Standalone pilot, initialization and reproduction
timings measure their reported in-process work; they exclude unrecorded
process startup and separate scoring overhead. Concurrent CPU/GPU lanes are
added here, so this is an active-work subtotal, not an exact campaign elapsed
stopwatch. Recorded work is well below the 7200-second campaign budget.

The prescribed pilot completed 40 accepted steps with no rejection on
CUDA device 1 (RTX 3090), using float64. Its max-steps termination is a
feasibility result, not a fitted research endpoint. The maximum recorded GPU
allocation across pilot, primary and reproduction work is 570819584 bytes
(0.532 GiB); maximum process RSS is 1104592896 bytes (1.029 GiB), below the
12-GiB GPU and 8-GiB RSS caps. No recorded cap was reached. This accounting
ends with the order-4 campaign; separately authorized order-5/6 work is outside
this audit.

## Reproduction

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  /home/amir/miniconda3/bin/python -B \
  studies/neural_response_memory_20260922/check_scalar_wide.py \
  --source data/generated/neural_response_memory_20260922/scalar_wide_source01 \
  --campaign data/generated/neural_response_memory_20260922/scalar_wide_primary01 \
  --reproduction-source data/generated/neural_response_memory_20260922/scalar_wide_source_reproduction01/quadrant_alternating_n2048_seed20260920 \
  --reproduction data/generated/neural_response_memory_20260922/scalar_wide_reproduction01/quadrant_alternating_n2048_seed20260920 \
  --pilot data/generated/neural_response_memory_20260922/scalar_wide_pilot01 \
  --output data/generated/neural_response_memory_20260922/scalar_wide_audit_new.json
```

Only supervisor-assigned files and generated namespaces within this study,
explicitly authorized reused engine sources, and required process skills are
in scope. No other study or Git history is read. The checker owns only its
script, this report and `scalar_wide_audit*` receipts; no Git mutation occurs.
