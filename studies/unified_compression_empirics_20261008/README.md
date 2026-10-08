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
The confirmation source was frozen at commit `62425c9`, SHA256
`681771a9a29146cb2992a4e7f883606543777273f3120a967a03fa8b0975fb7b`.
Only plotting was subsequently corrected: show small nonzero discrepancies
on the logarithmic scale and tolerate empty storage panels in partial reports.

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

## Completed results

The fixed sweep completed all 12 cases and 168 integrations in about 40.1
minutes elapsed on two RTX3090 GPUs. No timeout, source-construction failure,
nonfinite run or scientific rerun occurred. All 30 compression numerical
gates passed; the largest dense-plus-compression refinement discrepancy was
7.72% of the corresponding dense-pair discrepancy, below the 10% gate.
Every dense and compressed run reached final training MSE below 0.01.

The following values are maximum recorded-time test RMS divided by the
same case's iid-dense maximum recorded-time RMS. These are finite-panel,
finite-time Euler measurements, not continuum-supremum error certificates.
Accuracy requires ratio at most 3; values above 3 are retained failures.

| Dataset | Dense width | Legendre | Harmonic | Logarithmic |
|---|---:|---:|---:|---:|
| Circle, d=2 | 1024 | 0.00274 | 3.30035 | 4.35771 |
| Circle, d=2 | 2048 | 0.01092 | 12.15881 | 7.69122 |
| Circle, d=2 | 4096 | 0.00252 | 3.01456 | 4.60038 |
| Sphere, d=3 | 1024 | 0.00154 | 0.38193 | 0.35865 |
| Sphere, d=3 | 2048 | 0.00220 | 0.70652 | 0.24622 |
| Sphere, d=3 | 4096 | 0.00748 | 0.98563 | 1.32402 |
| Sphere, d=10 | 1024 | 0.00124 | — | 0.57249 |
| Sphere, d=10 | 2048 | 0.00133 | — | 1.09755 |
| Sphere, d=10 | 4096 | 0.00720 | — | 2.21407 |
| Raw digits1/7, d=64 | 1024 | 0.00084 | — | 0.51397 |
| Raw digits1/7, d=64 | 2048 | 0.00174 | — | 0.64319 |
| Raw digits1/7, d=64 | 4096 | 0.00267 | — | 0.45799 |

Legendre passes 12/12 accuracy tests, Harmonic 3/6, and Logarithmic 9/12.
Every passing compression also beats both of its learned-state-matched
controls in maximum-time RMS. All six failures are the two spectral models
on the circle: both lose to the small MLP there but still beat the tested
low-rank optimizer. Neither failures nor the borderline 3.01456 result are
rounded into success. No order was retuned in response to these outcomes.

### Largest-width storage and matched controls

At width 4096, the actual retained scalar counts are:

| Dataset | Dense | Legendre moving / total | Harmonic moving / total | Logarithmic moving / total |
|---|---:|---:|---:|---:|
| Circle | 16,789,504 | 864,258 / 17,641,498 | 45,588 / 180,420 | 45,588 / 180,421 |
| Sphere3 | 16,793,600 | 868,354 / 17,645,594 | 45,800 / 180,632 | 45,800 / 180,633 |
| Sphere10 | 16,822,272 | 897,026 / 17,674,266 | — | 50,828 / 196,029 |
| Raw digits | 17,043,456 | 1,118,210 / 17,895,450 | — | 218,444 / 788,733 |

On the successful d=3 test the spectral models reduce moving state by 367x
and total model storage by 93x. Logarithmic reductions are 331x/86x in d=10
and 78x/22x on raw digits. Legendre saves 15.2–19.4x moving state across these
four cases, but **does not save total model storage** because of its fixed
dense mixer. Storage counts exclude common data and disposable workspace,
but include every retained metric/inverse and the rank-safe floor.

The absolute RMS values below make the baseline comparisons explicit.
Each small/low-rank control is independently matched to that row's moving
budget. The NTK is the full initial kernel with eight moving dual coefficients,
not an artificially parameter-padded baseline.

| Dataset / method, n=4096 | Compression RMS | Matched small RMS | Matched low-rank RMS | NTK RMS | Dense-pair RMS |
|---|---:|---:|---:|---:|---:|
| Circle / Legendre | 0.000070 | 0.026374 | 0.945729 | 0.983859 | 0.027832 |
| Circle / Harmonic | 0.083903 | 0.031003 | 0.546471 | 0.983859 | 0.027832 |
| Circle / Logarithmic | 0.128040 | 0.031003 | 0.546471 | 0.983859 | 0.027832 |
| Sphere3 / Legendre | 0.000059 | 0.019497 | 0.691515 | 0.552208 | 0.007936 |
| Sphere3 / Harmonic | 0.007822 | 0.030425 | 0.777587 | 0.552208 | 0.007936 |
| Sphere3 / Logarithmic | 0.010508 | 0.030425 | 0.777587 | 0.552208 | 0.007936 |
| Sphere10 / Legendre | 0.000120 | 0.057468 | 0.700840 | 0.577896 | 0.016675 |
| Sphere10 / Logarithmic | 0.036919 | 0.076008 | 0.719280 | 0.577896 | 0.016675 |
| Raw digits / Legendre | 0.000066 | 0.027896 | 0.745109 | 0.604140 | 0.024673 |
| Raw digits / Logarithmic | 0.011300 | 0.040532 | 0.817776 | 0.604140 | 0.024673 |

The final dense training-feature-Gram relative Frobenius changes at n=4096
are 0.726, 1.184, 1.327, 1.703 for the four datasets. Combined with the NTK gaps,
these support non-lazy behavior. They do not rule out every possible kernel
or low-rank algorithm. In particular, Legendre itself uses low-rank history
factors: the control comparison tests a conventional factor-gradient
optimizer, not a lower bound against all low-rank representations. LoRA
mobilities were fixed by initial expected block-velocity matching, not tuned
on validation results. At the largest circle width, its two spectral-matched
controls did not fit below 0.01; that limitation is preserved in the figures.

### Ground truth and measured work

These are separate from dense-reference RMS. On raw digits at n=4096,
the two dense models' average test-label MSE is 0.057674. Legendre is 0.056637
versus 0.061507 for its small control; Logarithmic is 0.059052 versus 0.060359
for its small control. The corresponding low-rank controls do better on
labels (0.001509 and 0.000294) despite matching the dense trajectories poorly.
Thus this is evidence for trajectory preservation, not universal superiority
in prediction risk. At n=1024 Logarithmic's label MSE is 0.05376 versus 0.06265
for its small control. The dataset is sklearn's raw 8x8 optical digits, not
MNIST, and the thirty test inputs are a declared unlabeled panel.

At n=4096, construction excluding dense allocation/CPU staging takes about
0.04s for Legendre, 2.75–3.83s for Harmonic, and 2.21–2.45s for Logarithmic.
The spectral timings include the full-horizon disposable RK4 source rollout
and source/metric construction. A complete fine Euler trajectory takes
19.1–19.5s dense, 47.4–48.5s Legendre, 50.2–50.7s Harmonic and 63.2–64.5s
Logarithmic. All are below the 120s cap. The current eager-PyTorch closures
are **not a measured training-speedup** over dense at these widths.
Training/query timing breakdowns and process/incremental GPU peaks are in
the reports; common data and other resident arrays are identified there.

### Evidence, checks, and paper recommendation

Evidence root:
`data/generated/unified_compression_empirics_20261008/confirmation/`.
Each case has `report.json`, `trajectories.npz` and an external case log;
the root has the frozen configuration and sweep summary. The source manifest,
seeds and built-in deterministic datasets reproduce the cases without any
other study's experiment arrays. Generated products remain outside Git.

Scoped saved-array checks covered all 126 models/comparisons, 168 saved
trajectories and 30 compression gates. They checked RMS/endpoint/time-average
errors, held-out-label MSE, observation times, hashes, exact storage and
maximal budget-fitting small/LoRA widths/ranks. Final training-loss fields
match both saved loss traces; final training states/predictions were not
retained, so those losses are not independently reconstructed from arrays.
No discrepancy was found. These are internal empirical checks, not promotion
reviews, numerical error certificates or theorem verification.

All three final figures were rendered and visually inspected:

- `figures/unified_width_accuracy.{png,pdf}`: all twelve cases, including
  failures. Recommend this for the main paper alongside the storage figure.
- `figures/unified_state_storage.{png,pdf}`: moving versus total state and
  the fixed-mixer distinction. Harmonic/Logarithmic curves overlap in d=2,3
  because they have the same chosen width and differ by only the floor scalar.
- `figures/unified_matched_controls.{png,pdf}`: largest-width fidelity and
  training-loss controls. Recommend for the appendix, with raw-digits RMS
  and label-MSE values summarized in the main text if space permits.

The figure paths are relative to this study's generated-data root. The figure
summary preserves all method outcomes. Do not infer a logarithmic exponent,
a success probability, arbitrary-unseen-input Logarithmic decoding, or
initialization-only setup from this finite three-width, single-seed study.
The circle failure and the lack of a measured GPU training-speedup must stay
visible wherever these results are used. No manuscript figure was silently
replaced. This bounded campaign is complete; no further sweep is authorized
by this record.
