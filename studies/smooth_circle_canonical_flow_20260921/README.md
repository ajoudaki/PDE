# Smooth mixed-frequency circle under canonical gradient flow

Status: complete and internally checked. The campaign ran from frozen commit
`cd851aac4e4ecca0555968ae8647d7eb59f3d3c0`. All three models fitted all three
initializations; the predefined strong separation did not appear. See
[RESULTS.md](RESULTS.md) for the full comparison and figures.
User authorized this task on 2026-09-21: implement
`y(theta)=C[cos(theta)+sin(3theta)/2+cos(5theta)/4]` and test whether the finite
closure separates from parameter-matched dense networks with canonical
initialization and gradient flow.

This is a new study because the smooth regression target and continuous-flow
comparison define a different benchmark. Its research inputs are its own
artifacts and the established `docs/` and `code/`. No other study's source,
data, results or tuning choices are imported. The model choices below are
the comparison requested in the current task, explicitly frozen anew.

The [protocol](PROTOCOL.md) defines the model, data, solver, numerical gates,
budget and terminal stopping rule before training. The canonical finite dense
model is supplied by `docs/NOTATION.md` and `code/pde/finite_network.py`.
The finite dictionary model is an explicitly specified initialized-observable
construction with the maintained physical closure metric; no population
approximation theorem for this target or horizon is asserted.

Root owns this README, protocol, runner, integration and the sole Git writing
transaction. Scoped producer `/root/smooth_flow_producer` owns
`flow_benchmark.py`. Scoped checker `/root/smooth_flow_check` owns
`flow_check.py`, `flow_check.md` and its checking scratch. Their allowed inputs
are this study and explicitly assigned maintained source, without other-study
research. Independent verification is internal checking, not promotion.

Generated evidence belongs only to
`data/generated/smooth_circle_canonical_flow_20260921/`.
The [independent derivation and check](flow_check.md) records the exact formulas,
sources and actual preflight. Its evidence is
`data/generated/smooth_circle_canonical_flow_20260921/check_scratch/preflight_01/preflight.json`.
The producer hash is
`e3dfab2aad9e57f889cb5597288e59af61242a0b24ce25119d893bda906a60dd`;
the protocol hash is
`4216873a1246566c05fd9ce3815940801787c59df2a297faa9025a4c4ce02966`.
The per-attempt 400-second allowance was calibrated from a no-training RHS
timing; the 4200-second total worker budget is unchanged.

Scoped analyst `/root/smooth_flow_analysis` owns `flow_analyze.py` and
`RESULTS.md`, with the same study/established-input restriction. The analyst
independently recomputes Fourier errors, refinement/replication gates and
aggregate decisions; it does not import the producer's metrics.

The analyzer was also frozen before outcomes, at SHA256
`81654206f57fcb27ff4475a57355ea4c6dbb601b69f935ddc6841cfe5d2a730d`.
Its synthetic Fourier/gate/plot checks used 7.27 process seconds; producer
smoke checks used 0.9252 seconds, and the independent checker used a conservative
1.77 seconds before campaign replay. A 20-second allowance covers these and
the coordinator's syntax/small deterministic checks within the 600-second
checking budget.

## Completed comparison

The target has unit RMS, with `C=sqrt(32/21)`. The same 126 training angles,
1024 passive midpoint angles, physical horizon `T=1000`, and three prescribed
Gaussian initialization seeds were used for every model. These are separate
initializations, not target rotations. All models use two bias-free tanh hidden
layers and the canonical physical gradient-flow vector field, integrated by
DOP853 with tolerance refinement. There is no initialization gain or optimizer
substitution.

| Model | Trainable / retained predictor scalars | Median final RMS error | Fits / 3 |
|---|---:|---:|---:|
| Dense width 55 | 3190 / 3190 | 0.00342535 | 3 |
| Closure width 1024, dictionary dimensions 5 and 3 | 3087 / 11279 | 0.00285738 | 3 |
| Dense width 105 | 11340 / 11340 | 0.00289401 | 3 |

Width 55 approximately matches trainable parameters; width 105 approximately
matches total retained predictor scalars, including fixed dictionary entries.
The closure's median final RMS error was 16.6% below width 55 and 1.27% below
width 105. Seed ranges overlap and the advantage is not present on every seed.
Width 105 reached the fit threshold at an earlier saved checkpoint on every
seed. Passive and training errors agree at the displayed precision. All three
target harmonics were learned; most residual error is outside those harmonics.
This target did not produce a fitting failure for the small dense network.

All nine primary/fine comparisons passed. The largest saved prediction
discrepancy was `2.42733e-6`; the largest RMS-error discrepancy was `1.43608e-8`.
The three first-seed reproductions matched parameters and predictions exactly
at all saved checkpoints. Independent replay passed 3661 gates over all
21 attempts, 399 checkpoints and 21 final states. Independent analysis and a
separate coordinator calculation agree on the final errors and decision.

The campaign used 634.031 cumulative worker process wall seconds out of 4200;
the longest worker used 84.479 seconds. No attempts failed or were censored,
and the conditional finer level was unnecessary. The checking allocation is
conservatively rounded up to 45 seconds out of 600: 20 seconds before replay,
15.08 seconds for replay, 8.513 seconds for analysis, and small final checks.
The bounded protocol is closed; there are no remaining authorized training
runs. No representation lower bound, population theorem, asymptotic rate, or
general architectural dominance is asserted. Maintained code/docs were not
modified and these results have not been promoted.

## Reproduction and evidence

The campaign record is
`data/generated/smooth_circle_canonical_flow_20260921/run01/run_record.json`.
Its SHA-256 is
`e846e002818282761339bf7a5a4d1fee1265308814977c0365b11bca195852da`.
It binds frozen source hashes, exact commands, all attempt directories, timings,
refinement comparisons and reproduction records. The independent checker
report supplies the replay command and evidence hash. Aggregate tables,
four PNG/PDF figure pairs and machine-readable metrics are in
`data/generated/smooth_circle_canonical_flow_20260921/analysis01/`.
The coordinator's independent metric reconstruction is
`data/generated/smooth_circle_canonical_flow_20260921/check_scratch/coordinator_metrics.json`.

Actual campaign launch command, from the repository root (fresh output is
required for any future authorized reproduction):

```sh
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/smooth_circle_canonical_flow_20260921/flow_runner.py --output data/generated/smooth_circle_canonical_flow_20260921/run01 --preflight data/generated/smooth_circle_canonical_flow_20260921/check_scratch/preflight_01/preflight.json
```

Actual aggregate-analysis command:

```sh
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 MPLCONFIGDIR=data/generated/smooth_circle_canonical_flow_20260921/analysis_scratch /home/amir/miniconda3/bin/python -B studies/smooth_circle_canonical_flow_20260921/flow_analyze.py --runs data/generated/smooth_circle_canonical_flow_20260921/run01 --output data/generated/smooth_circle_canonical_flow_20260921/analysis01 --replay data/generated/smooth_circle_canonical_flow_20260921/check_scratch/replay_01/replay.json --report studies/smooth_circle_canonical_flow_20260921/RESULTS.md
```

The analysis command writes the deterministic numerical report. The study
report additionally contains a short outcome interpretation; its numerical
tables are unchanged. The frozen analyzer and protocol were not changed after
outcomes.
