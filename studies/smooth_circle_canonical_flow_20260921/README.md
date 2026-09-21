# Smooth mixed-frequency circle under canonical gradient flow

Status: implementation complete; independent model preflight passed456 checks.
Scientific training has not yet started. User authorized this task on 2026-09-21: implement
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
The per-attempt400-second allowance was calibrated from a no-training RHS
timing; the4200-second total worker budget is unchanged.

Scoped analyst `/root/smooth_flow_analysis` owns `flow_analyze.py` and
`RESULTS.md`, with the same study/established-input restriction. The analyst
independently recomputes Fourier errors, refinement/replication gates and
aggregate decisions; it does not import the producer's metrics.

Next authorized action: freeze the reporting source, then execute the bounded
protocol. Maintained code/docs are read-only. The intended command is:

```sh
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/smooth_circle_canonical_flow_20260921/flow_runner.py --output data/generated/smooth_circle_canonical_flow_20260921/run01 --preflight data/generated/smooth_circle_canonical_flow_20260921/check_scratch/preflight_01/preflight.json
```
