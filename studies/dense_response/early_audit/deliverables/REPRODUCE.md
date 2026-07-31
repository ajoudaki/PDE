# Reproducing the numerical audit

Requirements:

- Python 3.10 or newer
- NumPy
- Matplotlib

From the bundle root:

```bash
python -m src.run_dense_resnet_audit --out results/reproduced
GALERKIN_OUT=results/reproduced python -m src.run_response_galerkin_projection
```

The first command regenerates the scaling audit, initialization-depth test,
smooth-depth convergence table, truncated-response experiments, restart and
horizon tests, parameter sweep, and plots. The second regenerates the raw
triangular Galerkin diagnostic.

The archived `results/final/` directory is the frozen result set cited in the
main report. All recorded numerical “sup” values are maxima over the saved
time/depth grid, not certified continuous-time suprema.
