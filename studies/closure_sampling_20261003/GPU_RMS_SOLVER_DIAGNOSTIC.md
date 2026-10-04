# Initialization-only cubature solver diagnostic

2026-10-04. Bounded diagnostic of two failed constructors in the frozen
RMS-growth validation. No network trajectory was integrated, no solver result
was altered, and the sampler/runner sources were not changed.

Both failures were reproduced using the exact archived sampler and the same
NumPy/SciPy/PyTorch environment. Reconstructed initialized read-in and mixer
arrays matched the archived raw SHA-256 hashes in both cases. Total diagnostic
work took 2.843 seconds, within the 60-second bound.

| Case | Requested width/rank | Failing layer / selected count | Sum of masses minus one | Smallest mass minus prescribed floor | SLSQP status |
|---|---:|---:|---:|---:|---|
| n2048, seed8512, 60 degrees, opposite signs | 53 / 16 | 2 / 46 | 2.170829949e-7 | +1.669671346e-15 | 8, unsuccessful |
| n2048, seed8514, 90 degrees, same signs | 59 / 16 | 2 / 57 | 6.849225032e-8 | +7.643625316e-17 | 8, unsuccessful |

Every offending mass was finite and above its prescribed positive floor.
The rejection came from the equality constraint: the unit-sum errors exceeded
the frozen `1e-8` guard by factors 21.7 and 6.85. Both solver returns had
`success=False`, status 8, with message “Positive directional derivative for
linesearch,” after 60 and 70 iterations respectively. These are small numerical
feasibility errors accompanied by unsuccessful optimizer termination. They
are not negative weights or divergent masses, and they are larger than mere
float64 rounding. The frozen validity rule correctly retains both failures;
this replay does not establish that either solve met its optimization target.
Neither failure implies a rank requirement or a lower bound on state-growth
exponents.

The complete fit histories and offending returned vectors are in
[`gpu_rms_growth_solver_diagnostic_20261003`](../../data/generated/closure_sampling_20261003/gpu_rms_growth_solver_diagnostic_20261003/).
The probe count was 32, floor fraction .05, source rank 16, and source singular
tolerance `1e-10`. Instrumentation only wrapped `minimize` and cubature calls
to record returned values and layer indices; no feasibility projection,
reinitialization, solver option, or tolerance adjustment was performed.

Reproduce into a fresh directory from the repository root:

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/closure_sampling_20261003/diagnose_gpu_sampling_solver.py --output data/generated/closure_sampling_20261003/gpu_rms_growth_solver_diagnostic_20261003_replay
```

The study source adds only an explicit fresh output argument and its own source
hash to the executed diagnostic, whose snapshot remains in the original output.

- Study diagnostic source SHA-256: `9222e2b0d7a703eb5f768bd8edec489768f76a2e4388c89e10d76a6c4c4047f7`.
- Executed diagnostic snapshot SHA-256: `f313b6e28d0f73ae3fecf0df6f2d9937e41de2d4935c6899fa7678328f9b1388`.
- Diagnostic JSON SHA-256: `d95c1055f81f60eba3138baac320f14a348086382bcfc6eee4d12085aab700a9`.
- Archived sampler SHA-256: `f3199851e30e267bab005b06ccf16f68f05b0307695d9d4cbca64aa2ddc28f02`.

The output `source_manifest.json` records the source relocation correspondence;
`diagnostic.json` retains both exact initialization hashes and every optimizer
return through the failing fit.
