# Bounded numerical results and their limits

Twelve trajectories were executed in total: three implementation tests, eight
initial main cases and one combined refinement. They used 2490 training calls.
No finite-network training or broad sweep was run. Main-case evolution and
observations took about 33 seconds as recorded; the largest saved array state
was 172,267,520 bytes. Its checkpoint was 172,279,128 bytes. Peak recorded
process RSS was 430,560 KiB. The original driver measured case time/RSS before
checkpoint hashing; RSS is a cumulative process high-water mark. These are
resource observations, not hard memory enforcement or certified total timings.

The solver uses statistical representatives of its causal source process,
all Gaussian histories, covariance factors and one weighted directional tangent
per representative. It does not evolve a trainable all-to-all hidden matrix.
All reference cases reached physical time 40; the fixed arc-law quadratures
reached time 4. All source covariance validity gates passed.

The reference baseline used P=1024 per population, h=.3125, s=.05, float64.
On nine recorded physical times and 65 circle directions:

| Change relative to baseline | Maximum checked prediction difference |
|---|---:|
| Halve h | 0.064681 |
| Increase P to 4096 | 0.055997 |
| Halve s | 0.002128 |
| Use float32 | 0.00000222 |
| Halve h and increase P to 4096 | 0.110017 |

The combined refinement differs from each separate refinement by about .052
and .055. Thus even the observed data do not justify calling this a .1-accurate
population computation, let alone .02 accuracy. Sampling and time changes
are not perfectly coupled across the different source dimensions, so these
single-seed differences are not estimates of separate error terms or a rate.

The baseline current passive training loss was about 4.9e-5. Its lower hidden
squared motions at the two training axes were about .093 and .067; upper
motions were about .189 and .184. These are substantial nonlinear movements
in the COMPUTED process, not certified limits or merely a tiny changed-law
effect. The fixed exploratory arc law a=.03,b=.02,p=.53 had a difference .0332
between its two four/eight-node quadratures on the recorded grid. Input
transport errors for those quadratures are .01 and .005 respectively; the
measured prediction difference also contains sampling effects.

Increasing conditional Gaussian quadrature from order 16 to 32 changed
float64 predictions by at most about 7e-16 on the recorded final grids.
This observed agreement is not a quadrature certificate. The exact-arithmetic
transport bound in passive_quadrature.md gives an independently calculable
bound; its floating evaluation and conditional variances are in the analysis
JSON. Interval node/function rounding is not yet implemented.

A later analytic derivative bound addresses this component more sharply.
analytic_passive_quadrature.md proves the exact-arithmetic Gauss-Hermite error
bound Cbar q! max(1,tan r) (sigma/r)^(2q), uniform in every conditional mean,
and extends a finite variance grid to the whole circle. Its projection
hypothesis is checked in passive_quadrature.md. Evaluation using only retained
final-state data gave whole-circle component estimates 1.08e-11 (baseline)
and 5.11e-12 (combined) at q=16; at q=32 they were 3.91e-15 and 8.37e-16.
These are floating evaluations of the analytic formula, not certified upper
bounds including covariance/node/function rounding. The q=16 grid formula is
already below observed roundoff, illustrating why that distinction matters.
This supports treating final-state passive integration as a small component;
it does not bound the dominant dynamical/source errors or the earlier times.
No additional trajectory, covariance query or random draw was used.

Implementation checks covered Gaussian-prefix reuse, singular clean Grams,
weighted-sign identities, current-source handling, frozen-coordinate
derivatives, same-state initial/current queries and bitwise reached restart.
An independent static/algebraic code check is recorded separately. A malformed
checkpoint missing a random stream was initially accepted; this was corrected,
and malformed copies of an existing checkpoint were rejected without running
another trajectory. The driver now streams checkpoint hashing and retains
budget-skipped outcomes. These changes leave the training recurrence used in
the preserved runs unchanged.

## Reproduction and provenance

The generation/configuration files are directional_solver.py,
run_validation.py and validation_cases.json. The exact older case definitions,
source hashes, environment, thread settings, seeds and outcome/checkpoint hashes
are retained in each run's provenance.json. The code was NumPy 1.26.4,
SciPy 1.13.0, Python 3.10.12, with single-thread BLAS in the main runs.

Original main command, from /home/amir/Codes/PDE:

```sh
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B studies/population_flow_computation/run_validation.py --output data/generated/population_flow_computation/FRESH_MAIN
```

The current case file additionally includes the combined refinement. To
reproduce the historical eight-case batch exactly, pass --case once for each
of its eight names from the retained provenance. The combined run used:

```sh
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B studies/population_flow_computation/run_validation.py --case reference_combined --output data/generated/population_flow_computation/FRESH_COMBINED
```

Analysis (no trajectories):

```sh
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B studies/population_flow_computation/analyze_validation.py --runs data/generated/population_flow_computation/main_validation_20260912_01 data/generated/population_flow_computation/combined_validation_20260912_01 --output data/generated/population_flow_computation/FRESH_ANALYSIS
```

Analytic quadrature component evaluation from retained data (no trajectories
or new random samples):

```sh
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B studies/population_flow_computation/evaluate_quadrature_bound.py --summary data/generated/population_flow_computation/validation_analysis_20260912_01/summary.json --case reference_base --case reference_combined --output data/generated/population_flow_computation/FRESH_QUADRATURE_ANALYSIS
```

Its recorded output is analytic_quadrature_validation_20260912_01/results.json
under the study data root, including source/input hashes and saved-array hashes.
Only saved w arrays and previously computed scale summaries were read. This
evaluated the bound without computing an unavailable population trajectory.

Existing evidence: main_validation_20260912_01/, combined_validation_20260912_01/,
validation_analysis_20260912_01/, implementation_tests_0188cbdb3759/,
implementation_observation_check_20260912/ and
checkpoint_metadata_check_20260912_01/, all under this study's generated root.
Do not overwrite any of them. The twelve-trajectory budget is exhausted;
reproduction commands are documentation, not instructions to execute more runs
under that spent budget.
