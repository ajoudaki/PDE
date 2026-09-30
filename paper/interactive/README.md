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
