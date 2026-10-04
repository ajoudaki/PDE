# Bounded replay of two multidata cubature failures

2026-10-04. Setup-only diagnostic within the existing sampling study. No
training, solver repair, tolerance change, or scientific-source modification
was performed. Both original failures reproduced.

The case is `embedded_circle8_d5`, with eight fixed training samples, input
dimension five, dense width 2048, and reference seed 9411. The original run is
`data/generated/closure_sampling_20261003/gpu_multidata_20261004_diagnostic_1`.
The exact archived resolved configuration supplies the training directions,
labels, and 32 setup directions. Evaluation queries do not enter construction.
Both reconstructed initialization-array fingerprints equal their original
recorded fingerprints.

The declared candidates use the state-budget multipliers two and four, with
response ranks 24 and 32, respectively. Their target selected neuron counts
per layer are 102 and 146. The diagnostic calls the unchanged constructor and
wraps its existing `minimize` call only to record the returned result. All
optimizer arguments, starting values, greedy selections, objective evaluations,
and subsequent validity decisions are unchanged.

Let `sum_error` denote the floating-point sum of the returned mass vector
minus one, and `floor_margin` its smallest mass minus the prescribed floor.
The constructor rejects a result if it is nonfinite, if `abs(sum_error)>1e-8`,
or if `floor_margin < -1e-9`. The floor is `.05/N`, where `N` is the target
selected width, including at intermediate greedy selection counts.

| Candidate | First failing layer | Selected count at failure | Minimum mass | Sum error | Floor margin | SLSQP result |
|---|---:|---:|---:|---:|---:|---|
| `budget2_rank24` | 2 | 91 of 102 | 0.0004901960784314786 | 6.820571196719527e-8 | 1.0603497246908233e-16 | status 9, iteration limit, 150 iterations |
| `budget4_rank32` | 1 | 143 of 146 | 0.0003424657534246663 | 3.681773708130720e-8 | 8.782037597132586e-18 | status 9, iteration limit, 150 iterations |

Both returned mass vectors are finite, strictly positive, and above the
prescribed floor. The mass-sum test alone triggers the reported invalid-mass
exception. The first candidate fails during second-layer construction; the
second fails during first-layer construction. Their objectives at the failing
calls are 0.05451422082146894 and 0.04974234350546547. These are unsuccessful
numerical constraint/termination outcomes under the declared solver settings.
They do not establish that the corresponding cubature or approximation is
mathematically impossible. The candidates remain failed under the unchanged
campaign rules; this replay provides no repaired candidate or training result.

The complete diagnostic took 31.090 wall seconds and 31.241 process CPU
seconds including imports, within the 60-second CPU allowance. The script
enforces CPU limits of 58 seconds soft and 60 seconds hard, plus a 60-second
wall timer. Both candidates completed their replay within this allowance.
Original scientific source hashes were checked against the archived run before
execution and again afterward.

The new observational diagnostic is
[diagnose_gpu_multidata_solver.py](diagnose_gpu_multidata_solver.py). Its output
is in
[`gpu_multidata_20261004_solver_diagnostic`](../../data/generated/closure_sampling_20261003/gpu_multidata_20261004_solver_diagnostic/diagnostic.json).
It includes the original exact configurations and provenance, the diagnostic
source snapshot/hash, the full sequence of optimizer-result summaries, both
first-invalid mass vectors and initial weight vectors, NPZ hashes, floating
drifts in hexadecimal, and exact rational sums of the stored binary masses.

Reproduce into a fresh output directory from the repository root:

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/closure_sampling_20261003/diagnose_gpu_multidata_solver.py --run data/generated/closure_sampling_20261003/gpu_multidata_20261004_diagnostic_1 --output data/generated/closure_sampling_20261003/gpu_multidata_20261004_solver_diagnostic_replay
```
