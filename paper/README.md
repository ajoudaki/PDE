# Response-memory paper draft

This directory contains the standalone LaTeX report
`How Much Can We Compress Neural Training Dynamics?`

Build it with:

```bash
latexmk -pdf main.tex
```

Both circle-function figures now use the full-width radial PDFs
`figures/circle_deep_radial.pdf` and `figures/circle_shallow_radial.pdf`.
Their captions explain the radius offset, signed ticks, and matched-loss
RMS comparisons. The shallow figure uses the dense references in the table.
The rendering script, compact prediction bundle, and provenance manifest
are documented in [scripts/README.md](scripts/README.md).
These figures reuse saved predictions; no training rerun is needed.

The manuscript states the fixed-width theorem proved in
`studies/neural_response_memory_20260922` and keeps its population-limit
interpretation separate from the proved claim.  Figures are copied from the
study's validated generated artifacts; the paper does not rerun experiments.

Figure sources:

- `data/generated/neural_response_memory_20260922/analysis01/endpoint_functions.pdf`
- `data/generated/neural_response_memory_20260922/deep_circle_analysis01/function_curves.pdf`
- `data/generated/neural_response_memory_20260922/mnist100_analysis01/scatter_primary.pdf`
- `data/generated/neural_response_memory_20260922/mnist100_analysis01/rms_vs_order.pdf`

The main scientific boundaries are:

- compact-horizon convergence is not a uniform-all-time estimate;
- the initialized matrices are retained exactly;
- theorem constants are not uniform in width;
- the scalar nonclosure discussion concerns a restricted bounded-contraction
  encoder class;
- experimental fitted-function comparisons are not theorem-rate estimates.
