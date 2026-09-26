# Broad smooth ridges: canonical gradient-flow probe

Status: closed. All eight bounded attempts and independent checks are complete.
The pilot did not produce the desired closure advantage. No further computation
is authorized or running. See [RESULTS.md](RESULTS.md).
This is a new study for the changed input distribution and target. Research
inputs are this study and established `docs/` and `code/` only. No other study's
source, outputs, evidence or tuning is imported. Maintained files are read-only.

Question: can an initialized-observable closure retain enough smooth nonlinear
features to outperform two parameter-matched dense models under canonical
initialization and gradient flow? The target is a sum of 768 ordinary-slope
tanh ridges on 64-dimensional Gaussian inputs, with its linear component
cancelled. The test is a pilot, not a lower bound or a population theorem.

[PROTOCOL.md](PROTOCOL.md) freezes the scientific design before execution.
Root owns the README, protocol, coordination, analysis and all Git writes.
Scoped producer `/root/broad_ridge_producer` owns `probe.py`. Scoped checker
`/root/broad_ridge_checker` owns `probe_check.py`, `CHECK.md` and checking scratch.
Their scientific scope is their explicit assignments, this study, and the
specified complete maintained finite-model source and notation. The producer
also read the shared code/book guides. No other studies were accessed.

Generated evidence belongs to
`data/generated/broad_ridge_canonical_probe_20260921/`.
The canonical sources, dictionaries and data reproduce independently to roundoff.
The implementation agrees with maintained dense dynamics and an independently
differentiated closure. The preflight is retained at
`data/generated/broad_ridge_canonical_probe_20260921/check_preflight01/checks.json`.

Before training, descriptive target diagnostics found a residual-feature
effective rank of 681.88 on 8192 calibration inputs. A fitted linear predictor
has training/passive normalized RMS errors 0.9846/1.0131. These diagnostics
support the intended nonlinear target construction, but feature covariance
rank is not a neural-network width lower bound. The exact calculation is in
`target_diagnostics.py`; initial evidence is in the generated namespace's
`target_diagnostics.json`. It was computed before any trajectory, using the
same calculation subsequently saved as that script.

Actual data and campaign commands, from the repository root:

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/broad_ridge_canonical_probe_20260921/probe.py make-data --output data/generated/broad_ridge_canonical_probe_20260921/data01
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/broad_ridge_canonical_probe_20260921/run_probe.py
```

The campaign's `run01/run_record.json` records all exact worker commands,
source/data hashes, wall times, exit statuses and results. The eight attempts
share a 960-worker-second cap. No model, target, initialization-gain or optimizer
search is authorized.

## Outcome and closure

The width-244 dense network reached training normalized RMS error 0.008335 at
physical time 242.326 with median first-weight norm only 1.210 times its initial
value. Its unseen normalized RMS error was 1.11859 (zero prediction gives 1).
The task therefore did not force the smaller model to fail to fit these 2048
training examples. Neither closure nor dense models improved on the zero
predictor at their terminal unseen panels. This does not exclude later learning
or a population approximation gap; the experiment is a one-seed, bounded pilot.

All eight runs hit the compute cap before the planned horizon 5000. The last
checkpoint shared by all four models at both tolerances was only time 30.
The three parameter-matched predictors share a checked time-100 comparison:
closure/dense244/dense492 training normalized RMS 0.9271/0.8762/0.8682 and unseen
1.0195/1.0187/1.0167. This descriptive supplement is separately labelled and
does not replace the frozen all-four decision. Different terminal times are
never ranked as equal-time comparisons.

All refinement gates passed at common saved checkpoints; maximum prediction
difference was 1.86814e-4 and RMS-error difference 3.08428e-6. Independent replay
checked 47 checkpoints and eight final states, reproducing saved predictions
and losses exactly and terminal RHS to 2.09e-16. [CHECK.md](CHECK.md) records
scope and limitations. Final endpoint fitting is a directly replayed property
of the saved model; late endpoints at different times are not a refined
same-time trajectory comparison.

Training workers used 884.540 cumulative process-wall seconds of the 960-second
cap. Preflight checks, data, timing diagnostics, replay (16.59 seconds) and
analysis are conservatively covered by 50 seconds of the separate 240-second
allowance. Raw data, attempts, numerical checks, figures and all unfavorable
outcomes remain in the generated namespace. The frozen producer, checker,
protocol and primary analyzer were unchanged throughout training. The final
report helper adds terminal reporting and a labelled matched-model supplement;
it changes no frozen primary decision. No maintained code/docs were changed.

Analysis and figures were produced by `analyze.py`, followed by
`finish_report.py`, using the same Python executable and single-thread
environment shown above. The replay uses `probe_check.py --producer --data
data/generated/broad_ridge_canonical_probe_20260921/data01/data.npz --runs`
followed by the eight `run01/<model>_<level>` directories, with `--output
data/generated/broad_ridge_canonical_probe_20260921/check_replay01`.
Fresh output directories are required for reproduction. The bounded protocol
is finished; there is no remaining training branch or promotion claim.
