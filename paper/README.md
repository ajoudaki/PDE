# Response-memory paper draft

This directory contains the standalone LaTeX report
`Compressing Global Dynamics of Deep Nonlinear Feature Learning`.

Build it with:

```bash
latexmk -pdf main.tex
```

An alternative draft from the user's September 27 attachment is saved as
`main_alternative.tex` and compiled as `main_alternative.pdf` (28 pages).
Build it with `latexmk -pdf main_alternative.tex`. Its wording and figure
choices are preserved; only the PDF bookmark text for two appendix headings
was adjusted to remove hyperref warnings. The current `main.tex` and
`main.pdf` are unchanged by this alternative build.

Both circle-function figures now use the full-width radial PDFs
`figures/circle_deep_radial.pdf` and `figures/circle_shallow_radial.pdf`.
Their captions explain the radius offset, signed ticks, and matched-loss
RMS comparisons. The shallow figure uses the dense references in the table.
The rendering script, compact prediction bundle, and provenance manifest
are documented in [scripts/README.md](scripts/README.md).
These figures reuse saved predictions; no training rerun is needed.

The comparison revision is organized in `comparison.tex`, included after
the population interpretation. It gives a common test-function error target,
separates regime simplifications from representations of deep feature
learning, and compares moving state with fixed resources. The conditional
population memory scalings and their assumptions are stated there;
`comparison_appendix.tex` provides the self-contained derivations and
computational accounting. The existing fixed-width response-memory theorems
remain the main proved results.

The revised manuscript compiles to 31 pages. Section 7 starts on page 10,
the comparison table and optimized moving-state laws are on page 11, and
Appendix E starts on page 27. Both radial circle figures are retained.
The final latexmk build completed without warnings or unresolved references;
the new table and representative equation pages were checked visually.

The pre-revision rollback checkpoint is Git commit
`1a12bd63e83a48eb5c2638ba1911a60213cab278`, which includes the paper,
its current figure assets and portable bundles, and the comparison report.

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
