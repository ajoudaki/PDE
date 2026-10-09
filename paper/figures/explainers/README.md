# Explainer figures

Interactive sketches of the three compression mechanisms (Legendre, Harmonic,
Logarithmic). Open `index.html` in a browser for a grid of clickable thumbnails. Every
page in `html/` is self-contained (inline data, no network access).

To add an explainer, put its widget code in `fragments/figNN_name.frag` (optionally
add a `STATUS` entry in `build_html.py`) and run `python build_html.py`. The build
writes the page, screenshots it with headless Firefox into `thumbs/` (only pages whose
thumbnail is missing or stale, about 1 s each in parallel) and regenerates the index.
When the index is served over HTTP it also shows any page in `html/` that is not yet
indexed, with a live preview in place of a thumbnail.

## Layout

| Path | Contents |
|---|---|
| `fragments/figNN_*.frag` | Exact widget code of each figure version, data inline. Source of truth. |
| `templates/figNN_*.tpl` | The seven data-driven fragments with their payload replaced by `__DATA__`. |
| `scripts/` | Training and export scripts for the data-driven figures. |
| `build_html.py` | Regenerates data-driven fragments from JSON (optional) and writes `html/`, `thumbs/` and `index.html`. |
| `html/`, `index.html` | Built standalone pages and the thumbnail index. |
| `thumbs/figNN_*.webp` | 480×360 screenshots of each page (top of the page, without the nav line). |

Large arrays live outside Git in `data/generated/explainer_figures_20261009/`
(`sphere3_t32/`, `sphere3_t112/`, `legendre_restarts/`, `rich_target/`, plus derived
`spectra/` and `json/`).

## Current figures

| Fig | Mechanism | Data |
|---|---|---|
| 15c Moments are enough to continue | Legendre | Real: dense run plus the paper's moment model restarted at t = 2, 4, 8 from q = 1, 2, 4, 8 moments |
| 16c The clock folds an infinite run into a finite interval (appendix) | Legendre | Real: dense run to t = 112 |
| 17c Only like pairs with like | Legendre | Real normalized moments of three links; identity check against the direct integral |
| 18b Pick and weigh, don't mix | Selection | Illustrative, twelve neurons |
| 19c The price of random neurons | Selection (Harmonic, Logarithmic) | Illustrative 2-D source space |
| 20c Every petal is spelled with the same few shapes | Harmonic, circle | Exact Fourier coefficients of tanh ridges |
| 21c A real neuron, spelled in spherical harmonics | Harmonic, sphere | Real: network trained on a degree-3/5 target |

Earlier versions (1–21, b) are kept; `build_html.py` records each one's status.

## Reproduction

All runs use `DeepDense` from `../capture_trajectory.py`: width 1024, two tanh
hidden layers, zero initial readout, squared loss, float64 on `cuda:0`, explicit
Euler with step 0.0015625. Each command finishes in under two minutes on one RTX 3090.

```bash
G=data/generated/explainer_figures_20261009
E=paper/figures/explainers/scripts
python $E/train_sphere3_t32.py $G/sphere3_t32/real.npz
python $E/run_sphere3_moments.py $G/sphere3_t112/long.npz 112
for t in 2 4 8; do python $E/run_legendre_restart.py $G/sphere3_t112/long.npz $t 32 $G/legendre_restarts/rs$t.npz; done
python $E/train_rich_target.py $G/rich_target/rich2.npz 64
python $E/export_data.py --data $G
python paper/figures/explainers/build_html.py --json $G/json
```

| Script | Setup | Time |
|---|---|---|
| `train_sphere3_t32.py` | sphere3 (`validation_data(3, 8, 30, 601, task='toy')`), model seed 601, t ≤ 32; records 64 neurons per layer every 16 steps and sphere fields | ~25 s |
| `run_sphere3_moments.py` | same network to t = 112; integrates the Legendre moment equations (order 8) driven by the dense histories; restart snapshots at t = 2, 4, 8 | ~86 s |
| `run_legendre_restart.py` | the paper's moment model (A, w, moments, τ) restarted from a snapshot, orders 1, 2, 4, 8 batched, to t = 32 | ~25 s each |
| `train_rich_target.py` | 128 points uniform on S² (seed 7), odd target 15xyz + 2.5(5z³ − 3z) + 0.7x + 3(y⁵ − 10y³x² + 5yx⁴), model seed 11, t ≤ 64 | ~86 s |

Check, 9 October 2026: `export_data.py` reproduces every embedded payload
exactly, and `build_html.py --json` reproduces all 34 fragments byte for byte.
The restarted moment model tracks the dense test outputs to an RMS difference of
about 3e-5 (q = 8), 3e-4 (q = 4) and 2e-3 (q = 2) from t = 8 to 32. The
recorded weight change of W₂[6, 6] matches −(2/(mn)) Σₐ ∫ bᵢ hⱼ dτ to 1.6e-7.
