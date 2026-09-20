# Equilateral diagnostic: completed, population refinement unresolved

Date: 2026-09-18. This is empirical evidence, not a population convergence
theorem. The question, all ten solves, precision controls, success criteria,
resource cap, and terminal stopping rule were fixed in `diagnostic_plan.md`
before execution. No campaign extension was run after seeing the results.

## Reproduction

Working directory: `/home/amir/Codes/PDE`.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python studies/p1_three_input_geometry_20260918/diagnostic.py
```

The executed producer requires its output directory not to exist, so it
preserves this run rather than overwriting evidence. An intentional fresh
reproduction must use a newly named output directory and record that source
change. The retained run is
`data/generated/p1_three_input_geometry_20260918/equilateral_01/`.
It includes the executed source, frozen plan, metadata, summary, all ten
observation files and all ten endpoint arrays.

HEAD: `019e3630237e33f58b9636c0aa67a039bebf0182`.
Producer SHA256: `f602da70c4b3eefcd8665d1e3f90a0d73d71ed05e742f47e0a8e4d13e9b67965`.
Plan SHA256: `b3573039b29b68c57bc410345e7711509b7bcba4b5f95d0e880c48c24f027f8a`.
Scientific-input hashes and all numerical coefficients are in metadata.

Environment: Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0,
Linux 5.15.0-151-generic x86_64, float64, one BLAS/OpenMP/MKL thread.
The population rules and constants are deterministic; no random seed is
used. The four lower Gaussian coordinates and the two upper Gaussian
coordinates are integrated separately, with the canonical lower correlations
constructed inside the four-dimensional rule. Full evolving M and its
transpose are retained. The inactive constant coordinates are removed only
by the exact canonical parity invariant.

All ten solves completed. Exit status was zero; actual wall time was
18.8292 seconds, below the 120-second cap. No GPU was used.

## Observed outcomes and declared gates

The following values are the stored T=120 losses; angles are simultaneous
rotations of the equilateral triple, not changes to relative input angles.

| Rotation | q=8 | q=12 | q=16 |
|---|---:|---:|---:|
| 0 degrees | 0.0003153451 | 0.0003129088 | 0.0003082310 |
| 15 degrees | 0.0003297054 | 0.0003200718 | 0.0003306680 |
| 30 degrees | 0.0006364046 | 0.0005054319 | 0.0004897602 |

All endpoint arrays and all reported observations were explicitly checked
finite after execution. Sampled loss had no increase on any run. The
128/256 coefficient-rule difference was 1.5421e-13, passing its 1e-9
refinement threshold. This is a numerical refinement diagnostic, not a
rigorous integration error certificate.

The tighter time-solver repeat at q=12,15 degrees changed predictions by at
most 5.0538e-7 and code coordinates by at most 1.2834e-7 on the common time
panel. These pass the declared 2e-5 and 2e-4 time-refinement thresholds.

Population refinement did not pass:

| Rotation | Maximum q=12/16 prediction difference | Maximum code-coordinate difference |
|---|---:|---:|
| 0 degrees | 0.00166049 | 0.00853592 |
| 15 degrees | 0.00305944 | 0.01156588 |
| 30 degrees | 0.00674943 | 0.02323432 |

The respective declared thresholds were 2e-4 and 2e-3 at every common time.
Neither finer grid reached the declared loss threshold 1e-6 by T=120.
Thus **none of the three angles satisfies the precommitted resolved-fitting
criterion**. Stable-looking small losses are not substituted for that test.

For additional descriptive context from the predeclared observations, the
q=16 losses at T=10 were 0.00535524,0.00551013,0.00599279; at T=40 they
were 0.00157087,0.00156248,0.00180230. The smallest unweighted upper-Gram
eigenvalues at T=120 were 0.000568073,0.000588351,0.00110233. These remain
finite-quadrature values. A shrinking upper eigenvalue is not a test of the
full tangent matrix, which also contains both hidden gradient blocks.

## Interpretation

At the tested finite rules all representative rotations train well below
one half. This is suggestive that the extra canonical channels change the
dynamics substantially. The failed population refinement gate prevents
claiming a resolved population trajectory, and no particular bad scalar
angle was an input to this experiment. There is no proof of all-angle
fitting, exponential convergence, absence of saddle approach, or absence of
eventual escape. The main analytic theorems do not depend on this diagnostic.

The full observations reproduce the tables without another solve: read
each `q*_angle*.json`, select its final record for the first table, and
take maxima of prediction/code differences at corresponding records for
the refinement table. The producer performs these comparisons and saves
them in `summary.json`. File hashes are in the study manifest. No broader
numerical campaign is launched from this completed diagnostic.
