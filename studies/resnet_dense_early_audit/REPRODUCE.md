# Reproducing the numerical audit

Requirements:

- Python 3.10 or newer
- NumPy
- Matplotlib

From this directory:

```bash
python run_dense_resnet_audit.py
python run_response_galerkin_projection.py
```

The first command regenerates the scaling audit, initialization-depth test,
smooth-depth convergence table, truncated-response experiments, restart and
horizon tests, parameter sweep, and plots. The second regenerates the raw
triangular Galerkin diagnostic.

Both defaults write to repository `data/generated/resnet_dense_early_audit/results/`.
For a distinct reproduction, give both programs the same fresh subdirectory
under `data/generated/resnet_dense_early_audit/`, using `--out` and
`GALERKIN_OUT` respectively. Do not select a source or historical directory.
The original frozen result set is retained under
`data/historical/studies/resnet_dense_early_audit/results/` at the repository root.
All recorded numerical “sup” values are maxima over the saved
time/depth grid, not certified continuous-time suprema.
