# Paper figure tools

The legacy circle/sphere renderers are in **`figures.py`**. This guide replaces
the three separate circle, sphere and training-stage guides. The existing
`order_decay.tex` is the independent TeX source for the Cartesian order plot.

This is also a historical tool and figure catalog. Figure numbers, placement
recommendations and references to the "current manuscript" in the older
sections describe their original edition, not the unified 2026-10-08 paper.
See [the paper README](../README.md) for the maintained manuscript structure
and current experiment suite. Unused figure exports remain available for
reproduction and alternative layouts.

## Config-driven experiments

The current runner is still the single `paper/figures/capture_trajectory.py`.
Start from `paper/figures/compression_experiment.json`; defaults are identical
when no JSON is supplied. Commands below run from the repository root, using
a Python environment with PyTorch, NumPy, SciPy, scikit-learn and Matplotlib
(`/home/amir/miniconda3/bin/python` on this host).

```bash
python -B paper/figures/capture_trajectory.py run --config paper/figures/compression_experiment.json
python -B paper/figures/capture_trajectory.py plot --config paper/figures/compression_experiment.json

# Preview only; all dotted options are generated from the configuration schema.
python -B paper/figures/capture_trajectory.py run --print-config --seeds 601 602 603
# Short implementation smoke test, not a scientific accuracy benchmark.
python -B paper/figures/capture_trajectory.py run --config studies/cubic_log_comparison_20261008/runner_smoke.json
```

Precedence is defaults, then JSON, then CLI. Dictionaries merge; lists replace.
Use `[]` to disable a width/order/budget list, and `--no-...enabled` for a boolean.
For example, `--methods.non_oblivious.harmonic.budgets '[{"width":424,"source_rank":29}]'`.
Shared initialization options live under `methods.non_oblivious.setup`; an
optional method-local `setup` overrides individual fields. Add budgets for curves
and seeds for independent repetitions. The dataset seed is separate and stays fixed.

Each repetition rebuilds Legendre, Harmonic and Logarithmic from its own dense
reference. Independent dense widths, low-rank factors, sources and selectors use
recorded, deterministic role-specific seeds. `devices="auto"` schedules one
repetition per available GPU; use `"cpu"`, `"cuda:0"`, or `["cuda:0","cuda:1"]`
to select devices explicitly. A single repetition occupies one device.

Datasets are `sphere` (dimension >= 2), raw 8x8 sklearn `digits` (dimension inferred
as 64, no PCA), and `npz`. The latter requires `train_inputs`, `train_labels`,
`query_inputs`, `query_labels`, disjoint supplied splits and scalar labels;
configured row counts are sampled reproducibly and input rows normalized to unit
length. Labels are multiplied by `label_scale`. Test labels are used only for
scoring. For high-dimensional inputs disable Harmonic with `budgets=[]`.
Current Legendre, low-rank, frozen-features and Harmonic implementations require
two tanh hidden layers; other architectures are supported by dense and Logarithmic.
Unsupported combinations fail explicitly. The current non-oblivious setup uses
full-horizon RK4 rollouts and empirical source ranks, not the paper's jet compiler.
Extra constructor truncation is rejected rather than silently changing a model.

Outputs include `config.json`, the source snapshot, run identity, per-seed logs,
timings, learned/fixed/total storage and raw trajectories. Exact completed runs
can be reused; changed configurations/code/data need a fresh output directory.
Failed attempts are retained and retried in new attempt directories. Plotting
never trains: it verifies saved arrays and computes each model's RMS against its
own reference before aggregation. Median/mean and observed ranges are supported;
ranges are not confidence intervals. Worst-time means worst *recorded* time.
For mean plus/minus one sample standard deviation across repetitions, use
`--plots.aggregate mean --plots.spread sd` (ddof=1, not standard error).
For a bounded ascending-budget search, `--execution.stop_after_match` stops
each compression family at its first candidate whose endpoint and maximum
recorded RMS both match the independent dense comparator. Include the reference
width in `methods.oblivious.dense.widths`; larger skipped budgets are recorded
explicitly. This yields a smallest tested passing size, not a global optimum.
For a one-pair-per-width pilot, `scaling-plot --runs RUN_DIRS --out OUTPUT
--factor 2 --fit-log-powers` rescores existing trajectories and plots selected
learned storage, endpoint/maximum errors and the largest-width time curves.
`--factor 3` gives the relaxed comparison without rerunning models. The optional
log-power fits are descriptive fits to selected budgets, not exponent estimates
from independently tested data; fixed storage is retained in the metrics/caption.
Figures, per-seed metrics and a caption/storage table are saved in fresh
`plots/plot_NNN/` folders. Frozen features use an equivalent dual Euler computation;
the displayed parameter count is the width-sized primal readout, with both storage
accounts retained. No numerical-refinement certificate is implied by this runner.

To combine completed batches without rerunning them, use `plot` with
`plots.runs` listing their output directories and `plots.methods` selecting
the families to show. Set `execution.output` to a fresh analysis directory.
The plotter checks compatible producer/data/training/method settings, rejects
duplicate repetition seeds, and keeps each original reference pairing and
run provenance. For the three-seed Dense/Legendre/Logarithmic comparison:

```bash
python -B paper/figures/capture_trajectory.py plot --config studies/cubic_log_comparison_20261008/runner_three_seeds_plot.json
```

## Earlier Harmonic and Logarithmic validation commands

One implementation, `paper/figures/capture_trajectory.py`, contains both new
closures, their numerical checks, dense/NTK/small-MLP/LoRA controls, capture
and plotting. Its `validate` path does not load the archived Legendre producer.
Use a PyTorch environment and fresh output directories; CUDA runs are float64
with TF32 disabled. On the current host, use
`/home/amir/miniconda3/bin/python` in place of `python`.

```bash
python -B paper/figures/capture_trajectory.py validate --check-only --device cpu \
  --out /tmp/compression-checks

# Frozen circle confirmation rule, one of three held-out seeds.
python -B paper/figures/capture_trajectory.py validate --device cuda:0 \
  --width 4096 --dimension 2 --samples 7 --seed 201 --refine \
  --harmonic-budget 1535 --source-rank 19 --time-degree 5 --spatial-degree 9 \
  --out /tmp/compression-harmonic

# Independent-reference, dimension-five finite-program decoder.
python -B paper/figures/capture_trajectory.py validate --device cuda:1 \
  --width 4096 --dimension 5 --samples 5 --queries 32 --seed 201 \
  --horizon 5 --refine --log-probe --log-steps 10 --log-step .5 --log-queries 32 \
  --out /tmp/compression-logarithmic

# Portable publication figures: no raw run directories are needed.
python -B paper/figures/capture_trajectory.py plot-validation \
  --bundle paper/figures/compression_validation_source.json \
  --out /tmp/compression-figures
```

Each capture records exact configuration, code hash, orders, state counts,
timings, numerical sensitivity and failures in `report.json`, plus predictions
in `trajectories.npz`. The bundled reports contain all curves needed to render
the paper figures. Model caps include query evaluation; setup is charged.
Harmonic uses a full finite-horizon teacher rollout and paired-metric dynamics.
Logarithmic is an empirical float64, numerical-rank, counter-PRNG backend;
its fixed Euler horizon is not a continuous-flow convergence certificate.
Neither the finite width grid nor the factor-three practical threshold proves
the paper's asymptotic or probabilistic statements.

The following sections document older figure products and the separate sphere
capture. Their historical missing-trajectory caveat does not apply to the new
validation runs or to `figures/trajectory.pdf`.

## Commands

Run from `/home/amir/Codes/PDE`, choosing fresh output directories.

```bash
# Both circle-function figures; saved data only.
python -B paper/scripts/figures.py circles \
  --bundle paper/figures/radial_source_data.npz \
  --out /tmp/paper-circles

# Both endpoint sphere layouts; saved data only.
OPENBLAS_NUM_THREADS=1 python -B paper/scripts/figures.py spheres \
  --bundle paper/figures/sphere_source_data.npz \
  --out /tmp/paper-spheres

# Training-stage layouts, once genuine snapshots have been captured.
python -B paper/scripts/figures.py training-render \
  --bundle PATH/sphere_training_data.npz \
  --out /tmp/paper-sphere-training
```

Rendering writes PDF/SVG/PNG, plot-data bundles where applicable, and a
manifest with source hashes and metric checks. Existing manifests are never
overwritten. Omit `--bundle` for `circles` or `spheres` to load their original
run archives and recheck the available provenance. Preserve the compact NPZ
bundles when sharing a reproduction package; large training archives are not
needed for bundle-based rendering.

Rendering requires NumPy and ReportLab; sphere rendering additionally needs
SciPy and Pillow. PNG previews need `pdftoppm`; `--no-png` gives PDF/SVG only.
All render commands support `--dpi` and `--font-dir`. Sphere commands also
support `--resolution` for texture size. DejaVu Sans is the default font and
is embedded in PDFs. Native PDF width is 6.5 inches; use full text width.

## Which figures to include

For the current manuscript, include **`sphere_orders.pdf` in the appendix**.
Its dense-output column and P1/P2/P3 error columns communicate the order
comparison with one shared error scale. The front/back rows cover the entire
sphere. It adds a three-dimensional-input, four-hidden-layer ReLU example
to the circle/MNIST evidence. Keep its caption explicit about the one seed,
fixed-step integration and individually fitted endpoints.

Omit `sphere_comparison.pdf` from the paper: dense/P3/difference repeats much
of the same information, while showing less about approximation order.

A **real, checked common-physical-time figure** would be a stronger main-text
candidate, since the central claim concerns tracking training dynamics.
Such data have not been captured yet. The training-stage sample shown in
chat is explicitly synthetic and is **not a paper result**. A matched-loss
time-series layout would be supplementary to the common-time comparison.

## Circle figures

Assets: `../figures/circle_{deep,shallow}_radial.{pdf,svg,png}`.
Data/provenance: `radial_source_data.npz`, `radial_source_manifest.json`
in the same figures directory.

- Deep: three hidden tanh layers, width 4096, orders P1/P2/P3.
- Shallow: two hidden tanh layers, width 2048, orders P1/P3/P7.
- Five tasks at each depth, with all 8192 saved circle samples drawn.
- Each model is at its own training-MSE 0.001 endpoint, not a common time.

The polar angle is the input angle and radius is **3 + signed prediction**,
on one scale across all panels and both depths. Radial ticks show the
prediction itself; the dashed ring marks zero. The positive offset prevents
negative outputs from moving to the opposite angle. Black is dense, colors
are memory orders, and black dots mark the original training labels, including
all eight points of the antipodal-quotient task. Colored RMS numbers follow
the order in the legend and use the raw predictions, not plotted distances.

Deep inputs come from the finest selected endpoints in the response-memory
study's `deep_circle_analysis01/metrics_summary.json`. Shallow inputs match
the paper's table: four fresh dense references plus the refined archived
reference for `two_outliers_alternating`, as selected by `analysis01/metrics.json`.
The old Cartesian shallow figure used archived references for every task.

The renderer verifies selected data/hashes and recomputes all 30 RMS values.
The results match their analysis records exactly. No smoothing, resampling,
amplitude normalization or new model evaluation is used. Circle PDFs/SVGs
have vector curves and text.

Suggested caption: fitted circle predictions at each model's training-MSE
10^-3 endpoint; angle represents input direction, radius is 3 + f(theta),
radial ticks show f(theta), and the dashed ring is zero. Black dots show
training labels. Colored numbers are dense-versus-memory RMS discrepancies
on 8192 angles, in legend order. Specify the depth, width and orders above.

## Sphere endpoint figures

Assets: `../figures/sphere_{orders,comparison}.{pdf,svg,png}`.
Data/provenance: `sphere_source_data.npz`, `sphere_source_manifest.json`.
Source task:
`data/generated/neural_response_memory_20260922/compact_sphere01/xyz_m64/`.

The target is sqrt(105) x1 x2 x3 on unit-sphere directions in three input
dimensions, with 64 training points and four hidden ReLU layers of width 2048.
These are population response-memory closures. Black dots mark training
locations, not label magnitudes. Both layouts show complementary hemispheres
using a common camera; every training point is displayed once per model.

Radius is fixed. Output color limits are [-2.5, 2.5]. **All signed-error maps
in both figures share limits [-0.1, 0.1]**. The output and error bars have
different scales; no per-order normalization or artificial lighting is used.

| Model | Training RMS | Sphere RMS vs dense | Flow time |
|---|---:|---:|---:|
| Dense | 0.00994721 | 0 | 60 |
| P1 | 0.00995515 | 0.02193417 | 75.5 |
| P2 | 0.00993561 | 0.01279610 | 63.25 |
| P3 | 0.00995327 | 0.00454013 | 60 |

The reported runs use one network seed, float32 Euler steps of 1/128, and
individual training-RMS <=0.01 stops (MSE <=0.0001). There is no refinement
certificate for continuous gradient flow. The historical producer named
`quick_sphere_flow.py` is missing from the current checkout. Replotting saved
arrays does not independently reproduce the training experiment. The order
trend is specific to this comparison; it is not a universal monotonicity claim.

Surface textures use barycentric interpolation on the 16380-triangle convex
hull of the 8192 stored equal-area sphere queries. There is no extrapolation
or fitted smoothing. Interpolation recovers stored vertices to 8.9e-16 maximum
error. RMS always uses original arrays before interpolation. Sphere PDFs/SVGs
combine raster surface textures with vector text, dots and graticules.

Suggested caption:

> Dense fitted output and signed response-memory errors on the unit sphere
> for the target sqrt(105) x1 x2 x3, with 64 training directions and four hidden
> ReLU layers of width 2048. Rows show complementary hemispheres; black dots
> mark training inputs. All error panels share one color scale. RMS differences
> use 8192 equal-area sphere queries at each model's own training-RMS 0.01
> endpoint. Surface colors interpolate saved queries. Runs use float32 Euler
> steps of 1/128, with one seed and no continuous-flow refinement certificate.

## Training-stage capture: prepared, not yet run

The existing sphere archives store final predictions only. An inventory of
948 sphere/xyz NPZ files found no intermediate state/query histories. Genuine
training-stage data require a new capture; endpoint interpolation cannot
recover them. CUDA was unavailable in the side-conversation environment;
no full new run was launched.

The capture command imports the current study's `compact_flow.py` Flow,
retains the original training/query data, and explicitly records width 2048,
four ReLU layers, seed 20260920, hidden gain 1, readout standard deviation
1/2048, float32, no normalization, Euler step 1/128, checked blocks of 32,
and TF32 disabled. It records:

- Common times 0, 4, 16, 80. Models continue after fitting to reach shared times.
- Initialization and first checked crossings of training RMS 0.5, 0.1, 0.01.
  These are comparable losses, not exactly equal losses or interpolated states.

On a GPU-enabled session, choose a fresh directory and a free GPU:

```bash
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
/home/amir/miniconda3/bin/python -B paper/scripts/figures.py training-capture \
  --device cuda:0 --seconds 60 \
  --out data/generated/paper_radial_figures_20260927/sphere_training_capture01

python -B paper/scripts/figures.py training-render \
  --bundle data/generated/paper_radial_figures_20260927/sphere_training_capture01/sphere_training_data.npz \
  --out data/generated/paper_radial_figures_20260927/sphere_training_render01
```

`training-capture` imports no plotting packages, so a Torch environment without
ReportLab can run it. It records only dense/P1/P2/P3 on this task, with a
60-second fitter/observation budget per model; setup and I/O are additional.
It refuses a full-width CPU fallback, retains partial data and stops on an
incomplete model without retries. Capturing does not render automatically.

This is a new explicitly configured run. Its report includes each newly fitted
endpoint's whole-sphere difference from the archived endpoint. Review those
differences before treating it as a faithful replay of the missing historical
producer. `--hidden-gain` and `--readout-std` allow a recovered configuration
to be supplied explicitly.

Training-stage rendering outputs `sphere_training_{time,loss}.{pdf,svg,png}`
and a metric manifest. One hemisphere is displayed; RMS uses the entire sphere.
The same output/error scales are used across every row/order and both layouts.
Every panel reports its actual training RMS and, for matched-loss rows, time.

The observation scheduler passed an analytic exponential-decay check. The
layout was checked with visibly marked synthetic fixtures; those are not
experimental data. GPU capture, archive compatibility and genuine trajectory
figures remain pending.

## Consolidation and reproducibility

`figures.py` replaces `radial_figures.py`, `sphere_figures.py` and
`sphere_training_figures.py`. There are no sibling Python helper dependencies.
Earlier exports and manifests retain their original provenance; they have not
been relabeled as outputs of this consolidated version. Superseded source
snapshots are retained in the maintenance study's generated audit directory.
No training or manuscript-placement changes are part of the consolidation.

## Explanatory TikZ figures

`tikz_figures.py` renders the current manuscript's TikZ figures into
`paper/figures/`. It needs NumPy and pdflatex with TikZ. Pass a figure name
to rebuild just that figure; with no names it rebuilds all figures, including
the separate small-network training used by the `moments` illustration.

```bash
python paper/scripts/tikz_figures.py mechanism
python paper/scripts/tikz_figures.py trajectory  # saved bundle only; no training
```

The trajectory bundle now contains 39 actual shared checkpoints and both
numerical resolutions for dense and P1/P3/P7. The figure displays 38 positive
times on a log axis, with points, thin connecting guides and light shading
below the coarse/fine sensitivity scale. Its four radial times remain
0, 5, 20, 80. Do not regenerate this bundle with the historical eight-checkpoint
`experimental_figures.py --from-archives` extraction.

The bounded GPU capture script is `../figures/capture_trajectory.py`.
It writes to a fresh `--out` directory and never replaces the paper bundle.
Full protocol, numerical checks and commands are in
the trajectory replay (`figures/capture_trajectory.py`); provenance and all replay checks
are in `../figures/trajectory_capture_manifest.json`. Rendering the portable
bundle does not require the original training archives or a GPU.

### Figure 4 radial preview (not inserted into the manuscript)

```bash
python -B paper/scripts/tikz_figures.py same_rank_radial_preview
pdftoppm -png -singlefile -scale-to 2200 \
  paper/figures/same_rank_radial_preview.pdf \
  paper/figures/same_rank_radial_preview
```

This opt-in preview uses the existing `polar` renderer and the saved paired-label
endpoints in `response_memory_source.npz`. It shows trained factors (both seeds,
red), dense training (black/gray), and P3 memory (purple). The corrections have
matched rank bound 24; each model is at its own training-MSE 0.001 endpoint.
Shading marks the gap from the dense curve. Circle RMS values are recomputed
from all 8192 saved predictions and checked against the recorded metrics:
0.375464 / 0.203580 for factors, 0.00281761 for memory. These are prediction
discrepancies from dense, not errors against unseen labels. No training runs
or manuscript edits are performed. Default rendering does not build previews.

### Frozen-NTK radial preview (not inserted into the manuscript)

```bash
python -B paper/scripts/tikz_figures.py frozen_ntk_radial_preview
pdftoppm -png -singlefile -scale-to 2200 \
  paper/figures/frozen_ntk_radial_preview.pdf \
  paper/figures/frozen_ntk_radial_preview
```

This preview adds a full initialization-frozen empirical NTK control for the
same paired-label task: eight training inputs, two tanh hidden layers, width
2048, seed 20260920. The dense and P3 memory endpoints are the existing saved
predictions. The kernel uses the identical initialization and canonical
parameter mobilities `(n, 1, n)` for first weights, middle weights, and readout.
All three parameter blocks are included, without ridge regularization or tuning.

To specify the control completely, let the already normalized input be `u`,
`h1 = tanh(w u)`, `h2 = tanh(W0 h1)`, and `f0 = cᵀ h2/n`, all at initialization.
Set `δ2 = c ⊙ (1 − h2²)` and `δ1 = (W0ᵀ δ2) ⊙ (1 − h1²)`. The frozen kernel is

```text
K(q,x) = [δ1(q)ᵀδ1(x)] [qᵀx]/n
       + [δ2(q)ᵀδ2(x)] [h1(q)ᵀh1(x)]/n²
       +  h2(q)ᵀh2(x)/n.
```

For unhalved mean squared loss on `m = 8` inputs, the exact frozen flow is
`f(X,t) − y = exp(−2 K(X,X)t/m) (f0(X) − y)`. With
`K(X,X) = V diag(λ) Vᵀ`, its prediction at any query is

```text
f(q,t) = f0(q) + K(q,X) V diag((1 − exp(−2λt/m))/λ) Vᵀ (y − f0(X)).
```

The script evaluates this formula by an 8-by-8 eigendecomposition and locates
the first training-MSE 0.001 crossing by bisection. Each plotted model is at
its own fitting time; these are not matched-time trajectories. The frozen
control reaches this threshold at approximately 885686.05. Its RMS difference
from dense over 8192 uniform circle queries is **13.69016**, compared with
**0.00281761** for P3 memory. Its infinite-time interpolating limit still differs
from the saved dense endpoint by **9.37122** RMS. These are discrepancies from
the dense predictor, not errors against unknown test labels.

The frozen prediction spans approximately ±25.34, so all three panels use
the same linear radius `30 + f(θ)`, with signed-output ticks. This avoids both
clipping the large excursions and folding negative radii onto other angles.
Blue denotes frozen NTK, black/gray dense, purple memory, and black dots labels.
The result supports the importance of evolution beyond the initial tangent
model on this task; it is not a comparison with every possible kernel or a
claim about the infinite-width NTK regime under a different parameterization.

Rendering only needs `../figures/frozen_ntk_source.npz`. To recompute the
kernel and its predictions, choose a fresh output directory:

```bash
OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 \
  python -B paper/figures/frozen_ntk.py --out /tmp/paper-frozen-ntk-new
```

Computation requires NumPy, SciPy, and PyTorch (only for a tiny independent
Jacobian check); it requires no GPU and performs no neural-network training.
The capture writes its protocol, predictions, and checks to the requested
directory. Published preview inputs and checks are in
`../figures/frozen_ntk_source.npz` and `../figures/frozen_ntk_manifest.json`.
Initial weight hashes and initial predictions match the dense reference.
Each kernel block is checked against autograd, and the spectral flow is checked
against a matrix exponential and the independent training cross-kernel formula.
The smallest training eigenvalue is 1.84e−7; no modes were truncated. This is an
opt-in preview: neither default figure rendering nor the manuscript is changed.

### Four-method comparison across five circle tasks

The `learning_controls_*` figures place **dense, frozen NTK, rank-matched
trained factors, and response memory** in four columns. All five tasks from
the existing factor campaign are included, always at P3 and with both recorded
factor seeds. Figure 4 now uses `learning_controls_quadrant_alternating.pdf`;
the old compact factor figure is retained in the appendix. The full five-task
gallery is included there as `learning_controls_gallery_a.pdf` (three rows)
and `learning_controls_gallery_b.pdf` (two rows) for readable page layout.
These three adopted figures are included in the renderer's default build;
the other task rows and the single-sheet gallery remain optional exports.
For the clearest visual contrast, use the alternating task; the paired-label
task is a useful companion showing much smaller memory discrepancy.

| Task | Frozen NTK RMS | Factor seed 1 / seed 2 RMS | Memory P3 RMS |
|---|---:|---:|---:|
| Two outliers, alternating | 14.47884 | 0.46546 / 0.46091 | 0.072953 |
| Quadrant, alternating | 171.03262 | 0.67664 / 1.54131 | 0.045611 |
| Quadrant, paired labels | 13.69016 | 0.37546 / 0.20358 | 0.002818 |
| Quadrant, center/edges | 193.55560 | 0.25786 / 0.24927 | 0.004878 |
| Equally spaced, mixed | 0.14983 | 0.06069 / 0.06871 | 0.000526 |

All RMS values compare with the same dense endpoint within each task, using
8192 uniform circle queries. Each method reaches training MSE approximately
0.001 at its own stopping time. This is fitted-function fidelity, not a
matched-time comparison or an error against unseen ground-truth labels.
The four-dimensional antipodal quotient for the equally spaced odd task gives
rank 12; all other rows use rank 24. Its frozen flow also uses the same exact
quotient, with an additional loss check on the original eight physical inputs.

Dense/factor/memory predictions are reused from the saved experiment; only the
analytic frozen-kernel flows are new. They use the full kernel and initialization
specified above. Factors use `W0 + AB`, Euclidean mobility one for A and B,
`A(0)=0`, and Gaussian B entries with variance `1/rank`; outer weights use
canonical mobilities. Thus these controls test freezing the initial tangent
model and changing the evolution law at the same correction rank, respectively.
The result supports accurate reproduction of the nonlinear-trained predictor
beyond either simplification. Endpoint agreement alone does not establish
agreement of every internal representation or superiority to all low-rank methods.

The NTK can make much larger excursions. To keep the factor comparison visible,
the plots explicitly widen **only the NTK output scale**, including its gray
dense reference and training dots. The respective factors are 10, 100, 10, 200,
and 1 in the table's order. All plots are linear in output: radius is
`s*(b + f/u)`, where `u` is the marked output scale, and `b,s` are common within
each row. Signed ticks always show original output units, and numerical RMS
values are never rescaled. There is no clipping, negative-radius folding,
per-curve normalization, or logarithmic transformation.

Regenerate the full gallery or individual rows from the portable bundle:

```bash
python -B paper/scripts/tikz_figures.py learning_controls_gallery
python -B paper/scripts/tikz_figures.py learning_controls_quadrant_alternating
python -B paper/scripts/tikz_figures.py learning_controls_quadrant_pairs
python -B paper/scripts/tikz_figures.py learning_controls_gallery_a learning_controls_gallery_b
```

Other suffixes are `two_outliers_alternating`, `quadrant_center_edges`, and
`equal_mixed_odd`. Outputs are in `paper/figures/`. Rendering uses only
`learning_controls_source.npz` and the existing TikZ renderer. The capture
script `paper/figures/learning_controls.py` can recompute the comparison:

```bash
OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 \
  python -B paper/figures/learning_controls.py --out /tmp/paper-controls-new
```

Capture needs the current paper bundles and this study's saved factor archives;
it writes to a fresh directory. It verifies their hashes, physical inputs,
initialization matches, training losses, and all 15 memory/factor RMS scores.
The five frozen controls are solved analytically and checked with matrix
exponentials and independent training cross-kernel predictions. The existing
paired-label frozen prediction is reproduced exactly. The center/edges kernel
is ill-conditioned (condition number about 2.29e9); its independent training
prediction checks differ by at most 2.1e-8, much smaller than the reported
discrepancy. No kernel eigenmodes are discarded. The capture took about 4.2
seconds with two CPU BLAS threads and performed no neural training.
`learning_controls_manifest.json` records the protocol, sources and checks,
all individual fitting times, eigenvalues, and infinite-time kernel comparisons.
