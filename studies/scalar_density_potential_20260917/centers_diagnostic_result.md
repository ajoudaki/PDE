# Result: inverse full-metric candidate increases on a genuine triple

Executed 2026-09-18 from `/home/amir/Codes/PDE`, exit status 0:

```bash
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 90s python studies/scalar_density_potential_20260917/centers_diagnostic.py --output data/generated/scalar_density_potential_20260917/centers_check_20260918_01
```

This is the exact experiment precommitted in centers_diagnostic_plan.md.
All three declared Gaussian grids completed; the conditional tighter
48-node repeat was triggered by the declared positive full-metric slope
criterion and also completed. Total program time was 2.425 seconds, within
the 90-second cap. No additional configurations or horizons were run.

The data angles are 60,126,99 degrees, labels (+,+,-), weights
(3/8,1/8,1/2). Initial absolute probe projections are positive and distinct;
all three initial upper features are independent. The negative direction
lies between the two positive directions. The full moving w field, M and
c were integrated; no symmetry or frozen-feature reduction was imposed.

Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0, x86_64, float64, one
BLAS/OpenMP thread. Integration used DOP853, initial 128-node quadrature
constants, rtol=2e-8 and atol=2e-10 except for the declared tighter repeat
at 2e-9 and 2e-11. All runs reached physical time 200; none reached the
loss stopping threshold 1e-10. Source copy, hash, environment and complete
sampled scalar outputs are retained in the generated directory.

| Grid | RHS calls | Maximum valid full log slope | Time of maximum | Loss there | Full-Gram condition there | Loss at 200 |
|---|---:|---:|---:|---:|---:|---:|
| 24 | 1643 | 0.14492298 | 7.498119 | 0.49798179 | 127.51950 | 0.31216585 |
| 32 | 1598 | 0.14261165 | 8.156774 | 0.49261525 | 137.00095 | 0.34572861 |
| 48 | 1439 | 0.14679180 | 7.931033 | 0.49464107 | 136.73797 | 0.40988095 |
| 48 tighter | 1784 | 0.14679180 | 7.931033 | 0.49464107 | 136.73797 | 0.40988095 |

Here the full candidate is V=R^T Theta^(-1)R, where Theta includes the
first-layer and trainable-M response as well as the readout. The analytic
derivative includes the complete Theta_dot. At the 48-node maximum,
V=162.88567 and V_dot/V=0.14679180, while loss decreases. Both finer grids
pass the precommitted 20% slope and 10% peak-time agreement tests. The
tighter repeat changes the peak slope by less than 8e-11.

This is **empirical evidence against monotonicity of this candidate** along
the population flow. It is an exact numerical sign observation for the
declared quadrature ODEs, not a rigorous continuum sign proof. It does not
exclude a different potential, or a correction to this candidate.

The readout-only candidate's positive peaks were 2.97395,3.31924,2.18049
at times 79.2142,24.3712,31.3744. Their peak comparisons fail the
preregistered agreement criterion. Its sign test is therefore formally
inconclusive under this preregistration. No alternative post hoc peak was
selected to change that classification.

Validation checks:

- Maximum absolute defect in L_dot+physical_speed_squared: 9.72e-17.
- Maximum norm defect in R_dot+2Theta R: 2.59e-16.
- Initial Phi_dot+4L defects: at most 7.92e-9, with initial Gram condition
  numbers about 5.5e7--6.0e7 and initial potentials about 8.8e7--9.6e7.
  This loss of absolute precision is localized to an ill-conditioned
  initial inverse; the positive full-metric peak has condition about 137.
- Central differences along the physical velocity at a retained state
  near time 10 checked both Gram derivatives. Relative errors were below
  1.49e-9 for the readout Gram and 8.62e-10 for the full Gram, well within
  the declared 1e-4 tolerance. This check exercises the independent finite
  difference of the producer rather than repeating the derivative formula.
- The 32/48-node late-time losses differ substantially; no late-time rate,
  convergence, or positive limiting loss claim is made.

The primary agent read the entire producer and checked the velocity, d_dot,
lower gate-Gram derivative, symmetric weighting, and inverse derivative
against the exact equations. Diagnostics are reproducible from grid_N.csv
and summary.json; the additional table entries are the CSV row attaining
the valid full logarithmic-slope maximum. No regression or fitted exponent
was used. Current source and generated artifact hashes are in manifest.sha256.
