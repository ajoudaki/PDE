# Result of the bounded three-input diagnostic

Executed 2026-09-18 from `/home/amir/Codes/PDE`:

```bash
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 90s python studies/scalar_density_potential_20260917/three_diagnostic.py --output data/generated/scalar_density_potential_20260917/three_check_20260918_01
```

Exit status 0. Total program time 3.1091 seconds. All three integrations
reached physical time 1000 before the precommitted resource caps. None
reached loss 1e-10. No additional configurations or resolutions were run.
The preregistration is `three_diagnostic_plan.md`; source is
`three_diagnostic.py`. The generated run retains an exact source copy,
metadata, summaries, all sampled diagnostics and each sampled endpoint.
Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0, x86_64, float64,
one BLAS/OpenMP thread; deterministic Gauss--Hermite rules, no random seed.
Repository HEAD was 019e3630237e33f58b9636c0aa67a039bebf0182. The study
source hash is in metadata.json; source/input and output hashes are in
this study's manifest.sha256.

The model is the exact declared scalar characteristic field evaluated
with deterministic quadrature. The discretization is evidence about the
population equations, not an exact population simulation or a neural-net
comparison. Both components of w, c and M were evolved. The reflected
symmetry was checked rather than imposed on the lower dynamics.

| Nodes per Gaussian coordinate | RHS calls | L(1000) | Phi_read(1000) | largest sampled valid Phi_dot/Phi | ||c(1000)||_2 |
|---|---:|---:|---:|---:|---:|
| 16 | 4079 | 4.07101735e-5 | 0.16566665 | -0.00154626 | 1.58150321 |
| 24 | 3869 | 4.16686812e-5 | 0.21659961 | -0.00138324 | 1.53669658 |
| 32 | 3869 | 4.60646086e-5 | 0.34709554 | -0.00107500 | 1.49529196 |

The candidate uses the two distinct folded upper features (axis and the
reflected positive pair), not the singular three-row Gram. At all sampled
points each loss exceeded 1e-8 and each Gram condition number was below
1e10; maximum condition numbers were respectively 2714.43, 3330.52,
4755.28. Initial candidate values were 569.540, 598.140, 602.125. All
sampled candidate derivatives were negative. This does not exclude an
unsampled sign change and does not establish monotonicity in the exact
population model.

The first sampled negative axial residual occurred at t=3.08303, 3.18424,
3.18424 respectively. This agrees qualitatively with the independently
proved finite-time residual overshoot; the sample times are not event-time
estimates. The candidate continued decreasing despite that overshoot on
the sampled semidiscrete trajectories.

Validation observations:

- The absolute error in Phi_dot(0)+4L(0) was at most 1.14e-13.
- The largest sampled absolute defect in L_dot+speed^2 was 4.45e-16.
- The largest sampled reflected-output difference was 1.45e-15.
- Constants nu,tau from 128 and 192 Gaussian nodes differed by less than
  1.24e-13 and 4.94e-14 respectively.
- The code differentiates the Gram using both feature velocities and
  differentiates the predictions using both c_dot and H_dot. The energy
  check therefore compares separately assembled expressions, not the
  same stored scalar with its negative.
- DOP853 used rtol=2e-8 and atol=2e-10. No separate time-tolerance refinement
  was preregistered or executed. These are solver controls, not certified
  global errors.

The final candidate differs by about 60% between the two finest grids;
their final logarithmic slopes differ by about 22% relative to the
24-node value. Late-time population quadrature is unresolved. The exact
energy identity within a quadrature system does not bound this quadrature
error. There is no numerical counterexample meeting the preregistered
positive-slope criterion, and no resolved asymptotic-rate claim. These
results justify neither exponential nor polynomial asymptotic decay.

To reproduce the table, the loss, slope, call counts and readout norm are
in summary.json; the last row of each grid_N.csv supplies the potential.
The initial potential, maximum Gram condition, and first negative
error_axis sample are obtained by the corresponding first row, column
maximum, and first row satisfying error_axis<0. This analysis makes no
new numerical trajectory or fit. Repeat the command only with a fresh
output directory; the producer refuses to overwrite an existing run.
