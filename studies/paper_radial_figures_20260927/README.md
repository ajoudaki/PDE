# Paper circle and sphere figures

This is scoped figure maintenance requested by the user, begun 2026-09-27.
The task renders existing paper data and prepares an optional, bounded sphere
trajectory capture. It does not change scientific claims or manuscript placement.
No Git staging or commits. Preserve concurrent main-thread manuscript work.

## Current code and documentation

All figure code is now `paper/scripts/figures.py`; the single reproduction and
interpretation guide is `paper/scripts/README.md`. The four commands are
`circles`, `spheres`, `training-capture` and `training-render`. Only capture
launches training, and it requires a working CUDA device. It remains unrun.
The independent pre-existing `paper/scripts/order_decay.tex` is preserved.

The user requested consolidation of the three figure scripts and three guides.
Their superseded versions and hashes are retained under
`data/generated/paper_radial_figures_20260927/consolidation01/previous_sources/`.
The paper README link was updated; no manuscript text or existing figure asset
was changed by the consolidation. Existing figure manifests keep their historical
source hashes rather than being rewritten to credit the consolidated script.

## Authorized source data

Circle inputs are the manuscript's selected records in
`data/generated/neural_response_memory_20260922/`, plus its expressly selected
archived two-outlier dense array in
`data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_refined01/`.
Deep circles use the finest endpoints in `deep_circle_analysis01/metrics_summary.json`.
Shallow circles use the four fresh references and one refined archived reference
selected by `analysis01/metrics.json`, matching the paper table.

Sphere inputs are the ReLU rows and saved predictions in
`data/generated/neural_response_memory_20260922/compact_sphere01/xyz_m64/`,
plus that campaign's qualifications/table. The target is sqrt(105) x1 x2 x3,
with 64 training inputs, four hidden layers and width 2048. Its historical
`quick_sphere_flow.py` producer is unavailable; no independent training
reproduction is claimed.

## Completed figures and checks

Paper assets:

- `paper/figures/circle_{deep,shallow}_radial.{pdf,svg,png}`.
- `paper/figures/sphere_{orders,comparison}.{pdf,svg,png}`.
- Corresponding `radial_source_data.npz` / `sphere_source_data.npz` and source
  manifests, sufficient for saved-data rendering without training archives.

Original new render records are in this study's generated namespace under
`final/` (circles) and `sphere_v1/` (spheres). The 30 circle RMS comparisons
match the original analysis exactly. Circle curves use all 8192 saved angles.
Sphere P1/P2/P3 RMS values match the records exactly: 0.02193416923,
0.01279609769 and 0.00454012729. All four sphere models reached training
RMS <=0.01 at their own endpoints. These are float32 Euler results at step
1/128, one seed, without a continuous-GF refinement certificate.

Sphere surface rendering uses every saved query in a 16380-triangle mesh;
interpolation at stored vertices agrees to 8.9e-16. Both hemispheres and all
64 training dots are displayed. RMS uses original samples, not interpolated
pixels. Sphere PDFs/SVGs have raster textures and vector annotations; circle
curves are vector. Fonts are embedded and text-overlap checks pass.

Consolidation checks under `consolidation01/` regenerated all four scientific
figures: SVGs are byte-identical and PNGs pixel-identical to the originals.
Both synthetic stage layouts also reproduce byte-identical SVGs. PDF Creator
metadata now names the consolidated script. The capture CLI loads in the
Torch Python without ReportLab. No training was launched for consolidation.

## Training-stage request: prepared, pending real capture

An NPZ-key inventory of 948 sphere/xyz archives found only input data and final
predictions. CUDA is unavailable here; a bounded CPU timing check measured
0.143 seconds per width-2048 Euler step with four threads. No full replay ran.

The prepared capture uses one dense/P1/P2/P3 quartet, the original data,
explicit initialization settings, fixed step 1/128, and a 60-second per-model
budget. It records common times 0/4/16/80 and first-crossing training RMS
levels initialization/0.5/0.1/0.01. It compares newly fitted endpoints to the
archived predictions rather than assuming compatibility with the missing
historical producer. Incomplete runs are preserved and stop without retries.

The scheduler passed an analytic exponential-decay test. Rendering was checked
using explicitly marked synthetic fixtures under `training_layout_validation/`.
Those previews are not experimental results or paper assets. Actual GPU
execution, endpoint compatibility and genuine training-stage figures remain
pending. Full commands and scope are in the single scripts guide.

## Figure-placement recommendation

Include the existing dense-plus-P1/P2/P3-error sphere figure in the appendix.
It adds higher-dimensional inputs, depth and ReLU evidence, with weaker
numerical validation than the main circle comparisons. Omit the redundant
dense/P3/difference version. A real, numerically checked common-time sphere
figure would be a strong main-text candidate; exclude the synthetic preview.
This is a recommendation only; no manuscript placement was edited.
