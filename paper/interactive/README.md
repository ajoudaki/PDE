# Interactive circle explorer

`circle_explorer.html` is a self-contained viewer (d3 7.9.0 inlined; opens
offline in any browser) of the closure-vs-dense circle campaign from
`studies/closure_circle_spectral_mechanism`: 15 cases, dense networks at
widths 2048/4096 with three seeds, closures N = 1, 2, 3, 5, and the analytic
frozen NTK, with a time slider and playback, aligned by physical time,
matched loss, or recorded endpoints.

It is the compiled fragment `radial_viewer_multi_001/circle-experiments.html`
(built by `BUILD_VIEWER.py` from `MULTI_VIEWER_DATA.py`) wrapped in a
standalone page that defines the host CSS variables in the paper's palette.
Note these are the older study runs (N = closure order there), not the
paper's paired-label 39-checkpoint replay behind the trajectory figure.

## `neuron_clocks.html`

Ten neuron histories, read off like electrode traces: five forward activations
$h_a$ (left column, one colour) and five normalised backward carriers
$r_a\delta_a/\rho$ (right column, one colour), each at its own gain with no
axes or boxes, plus the residual $\rho$ on top. A segmented control (or the
space bar) morphs the horizontal axis between physical time $t$ and the
learning clock $\tau=\int_0^t\rho$. The run is the small network of
`scripts/tikz_figures.py::moments()` (seed 3, width 512, two hidden tanh
layers, Euler step 0.05) on a harder target — 16 inputs on the circle, labels
$2(0.9\cos\theta+0.9\sin5\theta)$ — so that features move visibly; the five
neurons per column are the most active among 512. Shown until $\rho<10^{-6}$.
Self-contained: data inlined, no external scripts.
