# Alternating-circle fitting at a matched training budget

Status: completed and internally checked, 2026-09-21. This is an empirical
fitting result within a declared optimization budget, not an established
capacity theorem or a promotion. The bounded campaign is closed; no further
training remains authorized by this protocol.

The user requested alternating labels on a circle: first test the width-55
network, then test the comparable closure if the smaller network does not fit.
This study directly fits labels. It does not approximate an earlier trained
full-network endpoint, and no other study supplied research inputs.

## Result

At 254 equally spaced circle points with alternating labels ±1, the n=1024,
p=1 finite closure fitted in all three prescribed high-gain runs. Neither
width-55 nor width-105 dense networks fitted in their three high-gain runs.
All three architectures failed with canonical initialization (0/3 each).
Thus the observed advantage requires the tested initialization and training
protocol; it is not evidence that arbitrary standard initialization suffices.

A fit means training MSE <=0.001 and every label sign correct. The high-gain
initialization multiplies initial first-layer weights by m/2=127 before any
dictionary construction, identically for each architecture.

| Model at m=254 | Trainable scalars | High-gain fits | RMS error across three seeds | Incorrect signs |
|---|---:|---:|---:|---:|
| Dense width55 | 3190 | 0/3 | 0.58944–0.64856 | 40, 50, 42 |
| Closure n1024,p1 | 3087 | 3/3 | 0.031283–0.031597 | 0, 0, 0 |
| Dense width105 | 11340 | 0/3 | 0.24148–0.31284 | 8, 8, 16 |

Width55 approximately matches the closure's trainable count. Width105 is the
separate total-size comparison: the closure retains 11279 predictor scalars
including its frozen dictionaries, versus 11340 for width105. These conventions
exclude optimizer and diagnostic storage; they are not peak-memory matches.

All three successful closure runs reached the threshold during Adam, after
1725–3453 steps, without readout least-squares polishing. The dense controls
completed 8000 Adam steps, subsequent LBFGS, and the prescribed readout solve
without fitting. Early stopping means the reported errors are not converged
best achievable errors.

The width55 ladder was: m30 canonical3/3 fits; m62 canonical2/3 fits;
m126 canonical0/3 and high-gain1/3 fits; m254 canonical0/3 and high-gain0/3
fits. Therefore254 was the first qualifying case for the conditional comparison.
Having more than55 labels alone does not force failure. Independent finite
constructive witnesses also fit m30/62 with width55; witnesses at width63 for
m126 and width127 for m254 give upper bounds only.

The result supports a closure fitting advantage under this finite protocol.
It does not prove that widths55 or105 cannot represent these labels, isolate
frozen-dictionary quality from all architectural differences, establish an
asymptotic rate, or establish behavior between the sampled points.

## Method, evidence and checks

[PROTOCOL.md](PROTOCOL.md) preserves the exact pretraining README bytes,
SHA256 `77852e218f16e47af83ea13410b598d57a0a1f178d7bde4e56f6108f7277e3a5`.
It specifies the architecture, label parity, initialized finite dictionary,
optimizer coordinates, parameter counts, thresholds, gates and budgets.
The producer remained fixed at SHA256
`6d16168b069ccbfef078bbe748fb0e760689187531e671901c8618f797f104a1`.

- [Full results and figures](RESULTS.md).
- [Independent mathematical and numerical check](fit_check.md).
- [Raw campaign manifest](../../data/generated/alternating_circle_fit_capacity_20260921/run01/run_record.json): all33 attempts, configurations, commands, gates and reproductions.
- [Independent replay](../../data/generated/alternating_circle_fit_capacity_20260921/check_scratch/producer_replay.json).
- [Independent protocol/provenance audit](../../data/generated/alternating_circle_fit_capacity_20260921/check_scratch/campaign_audit.json): PASS, no unresolved failures.
- [Independent analysis](../../data/generated/alternating_circle_fit_capacity_20260921/analysis01/analysis.json), [all attempt rows](../../data/generated/alternating_circle_fit_capacity_20260921/analysis01/attempts.csv), and [loss plots](../../data/generated/alternating_circle_fit_capacity_20260921/analysis01/selected_m254_loss.png).

Every m254 comparison and reproduction passes strict independent float64
prediction, loss and sign checks. All three same-settings fresh training
reproductions exactly matched their original endpoint MSE and fit status.
All initial Gaussian draws, finite dictionary construction, raw artifact
hashes, source/configuration hashes, conditional gates and budgets were checked.

Four earlier attempts (all three canonical m62 runs and canonical m126 seed21)
failed strict cross-backend prediction tolerance because readout polishing
produced large cancelling coefficients. Independent evaluations of the saved
weights at60 and90 decimal digits stabilized their fit classifications; the
original strict failures remain recorded. These exceptions do not affect the
strict numerical validity of the m254 comparison. Detailed hash-bound evidence
is in [numerical_adjudications.json](../../data/generated/alternating_circle_fit_capacity_20260921/check_scratch/numerical_adjudications.json).

The runner paused twice for those diagnostics, then resumed without repeating
completed training or changing the producer/protocol. It was amended to reuse
completed jobs and invoke independent precision replay when necessary. Resume
commands and runner hashes are retained in the manifest and interruption
snapshots. A post-campaign runner fix permits a fresh, initially absent
adjudication map; it changes no completed training or scientific calculation.

There were30 original attempts and3 prescribed reproductions. Summed worker
wall time was821.842654s of2500s; maximum attempt time36.941737s of60s;
maximum training concurrency2, with no overlapping runs on the same GPU.
Independent CPU checking remained below the separate300s cap: prior checks
were conservatively below20s, automatic precision replay1.166s, final replay
below1s and protocol audit below1s. Generated artifacts remain outside Git.

## Reproduction and ownership

The executed training command, before its two recorded resumptions, was:

```bash
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/alternating_circle_fit_capacity_20260921/fit_runner.py --output data/generated/alternating_circle_fit_capacity_20260921/run01
```

Both resumptions added `--resume --adjudications
data/generated/alternating_circle_fit_capacity_20260921/check_scratch/numerical_adjudications.json`.
Every underlying producer invocation and input configuration is preserved in
the manifest. The three actual fresh reproductions are its `reproductions`
entries; no new run is needed to complete the study.

After closing this README, the independent audit was rerun against the exact
preserved protocol and passed, without any training:

```bash
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/alternating_circle_fit_capacity_20260921/fit_campaign_audit.py data/generated/alternating_circle_fit_capacity_20260921/run01 --replay data/generated/alternating_circle_fit_capacity_20260921/check_scratch/producer_replay.json --adjudications data/generated/alternating_circle_fit_capacity_20260921/check_scratch/numerical_adjudications.json --output data/generated/alternating_circle_fit_capacity_20260921/check_scratch/campaign_audit_after_close.json
```

The independent tools are `fit_check.py replay-campaign`,
`fit_check.py adjudicate`, `fit_campaign_audit.py`, and `fit_analyze.py`.
The analysis command and evidence are documented in the results report.
Analysis requires `--adjudications` to retain the explicit precision
resolutions, and requires a fresh output directory. No training module is
imported by analysis or the independent forward checker.

Root owns README, protocol preservation, runner, GPU preflight, execution and
sole Git-writer duties. Scoped producer owns `fit_benchmark.py`; scoped checker
owns `fit_check.py`, `fit_campaign_audit.py` and `fit_check.md`; scoped analyst
owns `fit_analyze.py` and `RESULTS.md`. Their input scopes and checks are recorded
in the reports. The shared checkout was used directly; no maintained source,
other study, worktree or repository copy was modified or created.
