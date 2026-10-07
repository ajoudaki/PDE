# Experimental figure edition

For the current Harmonic/Logarithmic experiments and portable figure bundle,
see [scripts/README.md](scripts/README.md) and the empirical appendix in
[main.pdf](main.pdf). The fresh campaign ran on two RTX 3090 GPUs; the
historical no-training statements below describe only the older edition.

Historical record of the original experimental edition. It has since been
merged into `main` and combined with the TikZ figures. The current Figure 3
uses a new 39-checkpoint replay.
The descriptions, eight-checkpoint data and manifest below describe the earlier
exports, whose source bundle remains available in Git history.

This version lives on **`codex/paper-figure-experiment`**. It is a local paper
experiment; `main` and the GitHub remote are unchanged. No training was run.
The response-memory study sources are unchanged.

## Manuscript and placement

[main.pdf](main.pdf) is the 37-page compiled manuscript. It compiles without
warnings, unresolved references, or overfull/underfull boxes.

| Figure | Location | Role |
|---|---|---|
| Paired-memory mechanism | Main text, page 2 | Explain the method before the equations |
| Common-time learning | Main text, page 13 | Show the developing function at genuine shared times |
| Same-rank comparison | Main text, page 13 | Separate a compact representation from its evolution law |
| Deep radial overview | Main text, page 14 | Retain a whole-function overview across tasks |
| Order errors and feature movement | Main text, page 15 | Show measured error and numerical sensitivity |
| MNIST residuals | Main text, page 16 | Make small prediction discrepancies visible |
| Paired-projection identity | Appendix A, page 19 | Explain the two cancellations and product of errors |
| Clock geometry | Appendix B, page 23 | Explain the coordinate change and its scope |
| Sphere orders | Appendix F, page 36 | Retain the existing supplementary sphere example |
| Two-hidden-layer radial gallery | Appendix G, page 37 | Preserve the broader endpoint evidence |

Experimental prose now separates common-time measurements from individually
fitted endpoints, identifies the particular trained-factor baseline, and
calls activation movement **absolute RMS change**, matching the recorded
quantity. The old order plot with theoretical reference slopes is replaced
by measured discrepancies and empirical numerical sensitivity. The original
radial/sphere assets and alternative manuscript snapshot are preserved.

## Files and rendering

All new plotting code, data, figures and provenance are in `paper/figures/`:

- `experimental_figures.py`: the renderer; it never trains models.
- `response_memory_source.npz`: portable saved predictions and plotting metadata.
- `memory_mechanism`, `learning_in_motion`, `same_rank_dynamics`,
  `learning_clocks`, `paired_projection`, `mnist_residuals`, `order_sensitivity`:
  each has PDF, SVG and PNG exports.
- `experimental_manifest.json`: source hashes, numerical checks, render
  environment, source-bundle hash and output hashes.
- `experimental_gallery.pdf`: seven full presentation pages with headings
  and explanatory footnotes.
- `experimental_gallery.html`: a local preview of the individual paper figures.

Individual paper exports omit the gallery headers and footnotes because the
manuscript supplies captions. The renderer writes to its own `paper/figures/`
directory by default, independent of the current working directory, and only
replaces its explicitly named products when passed `--overwrite`.

From the repository root:

```bash
OPENBLAS_NUM_THREADS=1 MPLCONFIGDIR=/tmp/pde-paper-figure-mpl \
  /home/amir/miniconda3/bin/python -B paper/figures/experimental_figures.py --overwrite
```

Dependencies are NumPy and Matplotlib. To render elsewhere without replacing
anything, pass `--out /tmp/new-figure-preview`. The adjacent NPZ bundle is
used by default, so the original large training archives are unnecessary.
`--from-archives` explicitly re-extracts the same designated source records;
it performs plotting-data checks, not training. The existing general
circle/sphere renderer remains documented in `scripts/README.md`.

Build with auxiliary files outside the paper directory:

```bash
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/tmp/pde-paper-figure-experiment-build main.tex
cp /tmp/pde-paper-figure-experiment-build/main.pdf main.pdf
```

Only manuscript/figure products and their source data are versioned on this
experimental branch. LaTeX auxiliary files remain ignored.

## Evidence and limits

- **Mechanism and clock panels are schematics.** The clock example is a smooth
  illustrative path, not a measured response. The simple clock integrates
  residual RMS, not loss-decay rate. The joint clock bounds speed; it promises
  neither constant speed nor a universally sufficient small order. Its mass
  remains residual-weighted and requires a shared Gram matrix.
- **Trajectory panel:** paired-label task, two hidden tanh layers, width 2048,
  orders 1/3/7; 2048 circle queries at the exact common times
  0,1,2,5,10,20,40,80. Four snapshots are displayed. No temporal interpolation
  or nearest-time matching is used. RMS is recomputed against the finest fresh
  dense reference. Dotted sensitivity is the sum of separate dense/closure
  coarse-fine RMS changes, not a certificate. The older saved matched-time
  RMS arrays reproduce exactly against their own archived reference, with
  maximum difference zero for every order. The finer-reference plot is not
  relabeled as that older score.
- **Factor panel:** rank 24 on paired labels gives memory RMS 0.00281761 and
  factor-seed RMS 0.375464 / 0.203580. The five-task rank plots preserve all 29
  resolved fitted comparisons and explicitly exclude the one capped run.
  Both factor seeds are shown. Hollow memory markers are precision-limited.
  Equal rank does not assert equal total storage or runtime.
- **MNIST:** 100 training images, 1984 held-out images, width 4096, two tanh
  hidden layers. Endpoint RMS values are 0.00324756, 0.00108443, 0.00119922;
  all were recomputed from the saved predictions and checked against records.
  A shared signed-error scale preserves the small P2/P3 nonmonotonicity.
- **Order/feature panel:** the five three-hidden-layer, width-4096 tasks are
  shown without fitted convergence slopes. Feature intervals are the recorded
  absolute RMS movement ranges over 20 finest runs, not new hidden-state
  reconstructions, relative changes, confidence intervals, or measurements
  from the separate two-hidden-layer trajectory example.
- **Projection diagram:** both histories must use the same orthogonal
  projection and integration measure. The cancellation identity is separate
  from the feedback-stability argument needed for network tracking.

Input records and hashes are retained in the source bundle and manifest.
Plotting checks are not a new independent reproduction of the training runs.
The seven figure layouts and their manuscript placement were visually checked.
Earlier prototype scratch was moved out of the study namespace to
`/tmp/pde-paper-figure-prototype-archive`; it is not part of this edition.
