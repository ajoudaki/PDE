# Long-horizon dense Euclidean μP response audit

## Bottom line

The audit-fixed horizon-doubling plateau test passed for 16/16 exact trajectories and for K=0: 16/16, K=1: 16/16, K=2: 16/16, K=3: 16/16 projected trajectories. Quantitative recorded-grid prediction errors are reported below.

**This is not a numerical run of the conjectured width-independent Liouville PDE.** Every projected simulation still retains all dense W matrices. Any positive numerical result here concerns the response-compression mechanism behind the PDE conjecture, not the homogenized finite-PDE limit itself.

## Provenance

- Completed primary finite-network runs: 16
- Exact trajectories passing the audit-fixed doubling test: 16/16
- K=0 projected trajectories passing the same test: 16/16
- K=1 projected trajectories passing the same test: 16/16
- K=2 projected trajectories passing the same test: 16/16
- K=3 projected trajectories passing the same test: 16/16
- Integrator: fixed-step classical RK4
- Observable error: maximum over recorded times and every discrete depth node
- Plateau test: residual, terminal drift, sampled vector-field speed, and trapezoidal tail-arclength estimate on the half-horizon tail
- Representative trace: `central_n64_L16_s4_sw0p65_A1_g1_r0_dt0p02`
- Actual compiled Liouville PDE runs: **0**

## Recorded-grid errors over the full simulated horizon

| Order | Runs | Output median (max) | All-depth Gram median (max) | Gram error / feature motion, median (max) |
|---:|---:|---:|---:|---:|
| 0 | 16 | 8.510e-03 (1.579e-02) | 2.501e-02 (5.189e-02) | 4.136e-02 (8.251e-02) |
| 1 | 16 | 2.378e-04 (1.397e-03) | 1.875e-03 (3.616e-03) | 2.761e-03 (6.175e-03) |
| 2 | 16 | 1.418e-05 (5.711e-05) | 1.183e-04 (5.517e-04) | 1.923e-04 (9.355e-04) |
| 3 | 16 | 9.768e-07 (6.250e-06) | 6.083e-06 (5.925e-05) | 8.494e-06 (1.005e-04) |

These are curvewise prefix maxima on the stored time grid, not terminal-only errors. Near zero loss, loss error is deliberately not used as the main accuracy statistic because both systems fit the labels.

The exact all-depth feature motion had median 6.299e-01 and range [2.756e-02,7.869e-01].

## Plateau interpretation

For a candidate horizon H, the test uses every stored sample in [H/2,H]. It requires small residual, small distance to the terminal output and every terminal depth-Gram, small sampled vector-field output/Gram speeds, and small trapezoidal tail arclength. A candidate is accepted only when every later audit-fixed doubling through the final horizon passes and each successive drift stays below the earlier tolerance.

This rules out two misleading shortcuts: a nearly constant Gram-motion radius while the matrix moves tangentially, and a prefix-maximum error that looks flat merely because its maximum occurred early.

## Error growth across horizon doublings

| H | K | max output error | max all-depth Gram error | max new output-prefix increment | max new Gram-prefix increment |
|---:|---:|---:|---:|---:|---:|
| 4 | 0 | 1.579e-02 | 5.189e-02 | 0.000e+00 | 0.000e+00 |
| 4 | 1 | 1.397e-03 | 3.616e-03 | 0.000e+00 | 0.000e+00 |
| 4 | 2 | 5.711e-05 | 5.517e-04 | 0.000e+00 | 0.000e+00 |
| 4 | 3 | 6.250e-06 | 5.925e-05 | 0.000e+00 | 0.000e+00 |
| 8 | 0 | 1.579e-02 | 5.189e-02 | 0.000e+00 | 1.206e-07 |
| 8 | 1 | 1.397e-03 | 3.616e-03 | 0.000e+00 | 1.532e-07 |
| 8 | 2 | 5.711e-05 | 5.517e-04 | 0.000e+00 | 5.460e-09 |
| 8 | 3 | 6.250e-06 | 5.925e-05 | 0.000e+00 | 3.654e-10 |
| 16 | 0 | 1.579e-02 | 5.189e-02 | 0.000e+00 | 8.082e-13 |
| 16 | 1 | 1.397e-03 | 3.616e-03 | 0.000e+00 | 3.176e-12 |
| 16 | 2 | 5.711e-05 | 5.517e-04 | 0.000e+00 | 2.266e-13 |
| 16 | 3 | 6.250e-06 | 5.925e-05 | 0.000e+00 | 6.404e-15 |
| 32 | 0 | 1.579e-02 | 5.189e-02 | 0.000e+00 | 0.000e+00 |
| 32 | 1 | 1.397e-03 | 3.616e-03 | 0.000e+00 | 0.000e+00 |
| 32 | 2 | 5.711e-05 | 5.517e-04 | 0.000e+00 | 0.000e+00 |
| 32 | 3 | 6.250e-06 | 5.925e-05 | 0.000e+00 | 0.000e+00 |

A zero late increment means the largest recorded-grid error occurred in an earlier prefix; it is not an infinite-time tail bound.

## Required response order

For each absolute tolerance ε, the table counts primary runs at the final common horizon whose recorded-grid output and all-depth Gram maxima are both at most ε.

| ε | final H | K=0 | K=1 | K=2 | K=3 | unresolved |
|---:|---:|---:|---:|---:|---:|---:|
| 1e-02 | 32 | 2 | 14 | 0 | 0 | 0 |
| 1e-03 | 32 | 0 | 4 | 12 | 0 | 0 |
| 1e-04 | 32 | 0 | 1 | 5 | 10 | 0 |
| 1e-05 | 32 | 0 | 0 | 2 | 11 | 3 |

## RK4 refinement on the representative trace

| Method | Comparison | output difference | all-depth Gram difference | ratio to fine-grid model Gram error |
|---|---|---:|---:|---:|
| exact | dt_0.02_vs_0.005 | 1.750e-07 | 3.195e-07 | — |
| exact | dt_0.01_vs_0.005 | 1.007e-08 | 1.834e-08 | — |
| K1 | dt_0.02_vs_0.005 | 1.641e-07 | 3.153e-07 | 2.130e-04 |
| K1 | dt_0.01_vs_0.005 | 9.439e-09 | 1.812e-08 | 1.224e-05 |
| K2 | dt_0.02_vs_0.005 | 1.637e-07 | 3.147e-07 | 1.919e-03 |
| K2 | dt_0.01_vs_0.005 | 9.413e-09 | 1.808e-08 | 1.103e-04 |
| K3 | dt_0.02_vs_0.005 | 1.637e-07 | 3.147e-07 | 4.054e-02 |
| K3 | dt_0.01_vs_0.005 | 9.412e-09 | 1.808e-08 | 2.329e-03 |

The reconstructed tangent kernel for a projected state is a PSD proxy, not automatically the kernel driving its output rate. The raw traces therefore store the independent defect `||f_dot + theta_hat e||`; no surrogate coercivity claim is deduced merely from the proxy's eigenvalues.

## Scientific status

- Observed exact plateau-test count: 16/16.
- Observed K=0 plateau-test count: 16/16.
- Observed K=1 plateau-test count: 16/16.
- Observed K=2 plateau-test count: 16/16.
- Observed K=3 plateau-test count: 16/16.
- The response order is fixed for each complete trajectory; no training-time Taylor restart or outcome-dependent order change is used.
- Not tested: the J nonlinear grammar cutoff, N depth-Galerkin limit, Gaussian conditioning/Onsager compiler, width limit, or full outgoing residual of the finite Liouville PDE.
- Not proved: literal uniformity on t in [0,∞), interchange of width/depth/response/time limits, or the PDE conjecture.

## Files to inspect

- `results/processed/per_run.csv`: one row per run and order.
- `results/processed/errors_by_horizon.csv`: prefix maxima and new increments at every horizon doubling.
- `results/processed/required_order.csv`: minimum K for each declared absolute tolerance.
- `results/processed/refinement.csv`: common-grid RK4 refinement.
- `results/processed/aggregate.json`: group/order quantiles.
- `results/raw/*.npz`: loss, output, every depth-Gram, analytic speeds, kernels, constraint defects, and instantaneous q/r errors.
- `figures/representative_curves.png`: complete simulated transient and operational plateau test.
- `figures/time_depth_gram_error.png`: error over time and depth.
- `tests/test_core.py`: algebraic and plateau-detector controls.
- `theory/dense_euclidean_continuous_depth_pde_conjecture.md`: the finite-PDE specification whose homogenized convergence remains conjectural.
