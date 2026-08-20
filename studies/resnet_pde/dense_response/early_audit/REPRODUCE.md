# Reproducing the numerical audit

Requirements:

- Python 3.10 or newer
- NumPy
- Matplotlib

From this directory:

```bash
python run_dense_resnet_audit.py --out results/reproduced
GALERKIN_OUT=results/reproduced python run_response_galerkin_projection.py
```

The first command regenerates the scaling audit, initialization-depth test,
smooth-depth convergence table, truncated-response experiments, restart and
horizon tests, parameter sweep, and plots. The second regenerates the raw
triangular Galerkin diagnostic.

The `results/` directory is the frozen result set cited in the
main report. All recorded numerical “sup” values are maxima over the saved
time/depth grid, not certified continuous-time suprema.
