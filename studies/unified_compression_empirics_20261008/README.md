# Unified compression width-scaling experiments

## Contract

This study follows the explicit request to integrate Legendre, Harmonic and
the current rank-safe finite-panel Logarithmic compression into the existing
single executable `paper/figures/capture_trajectory.py`, including low-rank,
initial frozen-NTK and small-dense controls. It is a new empirical comparison
direction, distinct from the previous q<m construction investigation. Root owns
the unified runner, reporting and this README. Scoped implementation agents own
only new Legendre, baseline and Harmonic-source blocks in that same executable.
No paper theorem, maintained book or unrelated study is changed.

Inputs: the current paper and its capture executable; established docs/code;
the two directly imported historical code modules `moment_engine.py` and
`orthogonal_moment_engine.py` in `neural_response_memory_20260922/legacy_experiments.zip`
solely for the authorized reuse/check of the legacy Legendre implementation.
No other study's findings or experiment arrays are inputs. Concurrent untracked
studies are unrelated and must remain untouched. Initial HEAD: `a9adb25`.

Use the research-validation and canonical-notation skills. Primary observable
is prediction RMS relative to the coupled dense reference, maximized over
the common recorded physical times; also report endpoint and time-average RMS,
test-label MSE, dense feature motion, model storage and measured costs. A finite
width sweep is empirical evidence, not a proof of a logarithmic asymptotic law.

## Frozen scientific design

- Two hidden tanh layers; canonical Gaussian initialization, zero readout,
  full-batch squared-loss flow and the existing block mobilities. Eight
  training examples; thirty scored test examples. Unit-sphere inputs, no PCA.
- Four datasets: circle d=2 (existing odd Fourier target), spheres d=3 and d=10
  (existing odd linear+cubic target), raw sklearn digits1/7 in d=64. Existing
  data seed47; fixed held-out selection seed48. Dense seed601, iid seed10601,
  small seed20601, low-rank seed30601. No seed or task-pair search.
- Three widths:1024,2048,4096. Legendre and Logarithmic on all datasets;
  Harmonic only d=2,3. Same source truncation law and no per-case accuracy tuning:
  source rank ceil(8[log(en)/log(e1024)]^(5/2)); selected width
  max(192,4[max(d+m+1,2m+1)+3 source_rank]). For low-dimensional Harmonic use
  this same supplied width and source rank. These are practical choices, not
  theorem-prescribed sufficient orders. Legendre order ceil(8(n/1024)^(1/4)).
- Harmonic uses independent designed sphere nodes (32 circle nodes or a
  6x12 spherical product grid), degree5 spatial harmonics, degree8 piecewise
  Chebyshev fits on dyadic time intervals. Logarithmic uses the declared thirty
  test INPUTS in setup; their labels never enter any source or training update.
  Both practical source producers use a disposable full-horizon dense RK4
  rollout, step0.125. This is not a cheap initialization-only experiment.
- Rank-safe floor is fixed from initialization as min(1e-4, dense normalized
  training-feature-Gram gap/8). Record its value and sampled runtime margins.
- Controls are matched to MOVING state separately for each compression.
  Small MLP uses the largest fitting width. Low-rank uses frozen dense first
  and hidden matrices, trainable factors on both, and full readout; rank is the
  largest common rank that fits. All frozen arrays are charged separately.
  Full-width NTK is the exact zero-readout initial kernel with an Euler dual
  state of m coefficients; it is deliberately a smaller-state control, not
  padded with meaningless parameters. No deep-linear baseline is added.
- Common physical horizon32; fine Euler step0.0015625 and coarse0.003125.
  Dense and each compression have a coarse/fine check. Controls use the fine
  step. Source construction remains RK4 but all compared predictions are Euler.
  Dense and compression fitting MSEs are reported separately from trajectory
  accuracy; a baseline that fits slowly is not excluded. No endpoint-to-zero
  claim is made if a model has not reached training MSE0.01 by this horizon.

## Gates, budgets and stopping

The compression comparison passes numerically when summed dense+compression
coarse/fine max-time test RMS is below10% of the fine iid-dense discrepancy.
Accuracy means at most3 times that iid-dense discrepancy. Compare both matched
controls explicitly rather than declaring a win from the threshold alone.
Failures remain in every report; fitting, accuracy and numerical validity are
different fields. Legendre lifted-state drift is recorded, not silently reset.

Before confirmation, allow two explicitly labelled engineering pilots only:
d2 and raw digits, width512, same data/seeds/horizon/orders law, used to check
runtime, integration and interfaces. These are not independent confirmations.
If a systematic implementation/numerical defect is found, correct it, rerun
only the minimal affected pilot, and freeze the final source before the twelve
confirmation cases. No tuning to test-error wins. Cap each integration at120s,
each source setup at120s, each case at900s. Use both GPUs, at most two workers.
No scientific repeats, rank sweeps or expanded architecture grid after the
confirmation batch; a failed gate is inconclusive. Aim for <=45 minutes GPU
batch elapsed, and stop if the hard per-case budgets are exceeded.

All executable logic stays in the existing capture script. Generated runs and
figures belong in `data/generated/unified_compression_empirics_20261008/` and
remain outside Git. Persist the exact plan, source hash, commands and essential
results here. Provide figures and paper-placement recommendations; do not
silently add exploratory results to the manuscript.

## Implementation checkpoint

All methods, controls, case orchestration, small algebra checks and plotting
are integrated in the one capture executable. Legendre no longer requires the
archived ZIP at runtime. The ZIP was used only to compare its equations with
the old implementation: RHS agreement3.5e-18, five-step state agreement1.8e-15.
The committed `unified-check` covers implicit matrix action, lifted tangency,
low-rank gradients/mobility/budget edges, exact kernel Euler and both geometric
quadratures. Maximum geometry/product residual was4.5e-15. A scoped runner
check found no device/label/budget blocker; failed setup methods are retained
as inconclusive and construction versus deployment precision is distinguished.

Engineering pilots live in
`data/generated/unified_compression_empirics_20261008/pilots/`.
Their executable hash precedes only reporting/plotting corrections; their
scientific settings are unchanged. Raw-digits pilot Legendre/Logarithmic RMS
ratios to the dense pair were0.00126/0.375, both numerically resolved and better
than both learned-state-matched controls. Circle Legendre/Harmonic/Logarithmic
ratios were0.00494/7.92/6.69: the latter two fail the accuracy target despite
passing refinement. These failures are not grounds for an order or data search.
The confirmation source will be frozen after the two pilots complete.

Reproduction from repository root (use a Python environment with NumPy,
PyTorch, scikit-learn and Matplotlib):

```bash
python paper/figures/capture_trajectory.py unified-check
python paper/figures/capture_trajectory.py compression-sweep --protocol unified \
  --plan studies/unified_compression_empirics_20261008/plan.json \
  --devices cuda:0 cuda:1 --case-seconds 900 \
  --out data/generated/unified_compression_empirics_20261008/confirmation
python paper/figures/capture_trajectory.py unified-plot \
  --root data/generated/unified_compression_empirics_20261008/confirmation \
  --out data/generated/unified_compression_empirics_20261008/figures
```

Pilot commands use `unified-case --dataset sphere2 --width 512` (or
`--dataset digits17`), with
the default horizon/step and separate output directories. Recorded GPU runs
use `/home/amir/miniconda3/bin/python`, one worker per RTX3090. Exact commands,
software versions, source/data hashes, scalar counts, training/query timings
and numerical margins are retained in each report. No generated products are
added to Git.
