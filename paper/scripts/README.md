# Paper figure tools

All circle/sphere figure code is in **`figures.py`**. This guide replaces
the three separate circle, sphere and training-stage guides. The existing
`order_decay.tex` is the independent TeX source for the Cartesian order plot.

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
