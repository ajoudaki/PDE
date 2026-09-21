# Alternating-circle fitting at a matched training budget

Status: the Adam campaign and its subsequently authorized GD-only continuation
are completed and internally checked, 2026-09-21. The separately frozen
[GD_PROTOCOL.md](GD_PROTOCOL.md) governed the new runs and their own budget;
the previous Adam protocol and results remain unchanged. The GD experiment
started from commit `ed00a1ad0a98d7e0fd5abb9382f2c3c130bfe5d4`.

The completed Adam result below is an empirical
fitting result within a declared optimization budget, not an established
capacity theorem or a promotion. The bounded campaign is closed; no further
training remains authorized by the original Adam protocol.

The user requested alternating labels on a circle: first test the width-55
network, then test the comparable closure if the smaller network does not fit.
This study directly fits labels. It does not approximate an earlier trained
full-network endpoint, and no other study supplied research inputs.

## Interactive radial viewer: both completed rounds

The user subsequently requested a shared radial visualization of the Adam and
GD rounds. This is a plotting continuation, with no new optimization. The
[interactive fragment](../../data/generated/alternating_circle_fit_capacity_20260921/radial_view01/final/alternating-circle-adam-gd.html)
also appears in the current task's visualization directory as
`alternating-circle-adam-gd.html`.

The controls select round, sample count, initialization, seed and available GD
step cap. Following the user's display preference, radial spread defaults to
35% of the original displacement and can be adjusted from10% to100%;
this leaves predictions, sign decisions and reported errors unchanged.
Model toggles compare closure n1024,p1, trainable-count-matched width55
and total-retained-count-matched width105. The closure order is fixed at p1;
unrun configurations are labelled rather than invented. The viewer includes
all69 original attempts (30 Adam and39 GD), excluding reproductions. Each
model shows its best saved parameter witness, training RMS/sign errors and
actual best optimizer phase. Adam is explicitly labelled as allowing polishing.

Target marks appear only at labelled inputs. Colored markers preserve checked
sample predictions in binary64; lines show predicted values between samples,
where no target is supplied. There are65 independently replayed circle curves.
The four previously precision-adjudicated Adam cases show their existing
60/90-digit checked sample predictions only; unavailable reliable circle
curves are omitted and labelled. The radial extent includes the full saved
grid's extrema, including large Adam overshoots, and remains fixed across
seeds, methods and step caps at a given round/sample-count/initialization.

Display curves retain128–2048 adaptive vertices from8192 saved angles,
including their global extrema, and use float32 values. The largest actual
interpolation discrepancy on the saved grid is0.0585252 (Adam) and0.00749136
(GD); the viewer displays the current discrepancy. These are sampled-grid
checks, not continuous-angle or pixel-error bounds. Thirty curves reached
the vertex cap before the nominal0.002 simplification target; the viewer
makes no universal0.002 claim. Training errors are never computed from these
display-only curves.

The final [export audit](../../data/generated/alternating_circle_fit_capacity_20260921/radial_view01/final/audit.json)
and [independent data check](../../data/generated/alternating_circle_fit_capacity_20260921/radial_browser01/data_check.json)
passed all69 records, best-state/phase bindings, sample metrics, all65 curve
subsets/extrema, and the four high-precision sample-only arrays. Browser checks
cover all33 selectable combinations and69 records, missing-model states,
method toggles, tooltips, saved-state restoration, 320/360/736px layouts,
dark mode, animated transitions and exact radial-spread scaling without
metric changes. The final browser report is
[check04/browser_check.json](../../data/generated/alternating_circle_fit_capacity_20260921/radial_browser01/check04/browser_check.json).
Browser evidence is stored under
`data/generated/alternating_circle_fit_capacity_20260921/radial_browser01/`.

Rebuild only the presentation, without training:

```bash
python -B studies/alternating_circle_fit_capacity_20260921/radial_data.py --out data/generated/alternating_circle_fit_capacity_20260921/NEW_RADIAL_EXPORT
python -B studies/alternating_circle_fit_capacity_20260921/radial_view.py --data data/generated/alternating_circle_fit_capacity_20260921/NEW_RADIAL_EXPORT --output data/generated/alternating_circle_fit_capacity_20260921/NEW_RADIAL_EXPORT/alternating-circle-adam-gd.html
```

The first compression draft remains at `radial_view01/`; the consumed,
validated final payload is `radial_view01/final/`. Root owns `radial_view.html`,
`radial_view.py`, `radial_view_check.cjs`, integration and README; the scoped
analyst owns `radial_data.py`; the independent checker owns `radial_data_check.py`
and its data audit.
Scientific sources, training records and previous reports remain unchanged.

## GD-only continuation

The full-batch GD ladder fitted both width55 and the closure in3/3 seeds at
m30 and m62. At m126 the primary closure fitted2/3 seeds and both dense
networks fitted0/3, so126 was the first candidate and254 was not run.
Halving the maximum scalar step reduced the closure fit count to1/3; both
dense controls remained0/3. Thus the registered requirement of at least2/3
closure fits at both step caps was not met.

A fit retains the threshold MSE<=0.001 plus all label signs correct. All six
original high-gain closure attempts at126 classified every point correctly,
including the three that stopped just above the loss threshold. These are
three fixed seeds under two step caps, not six independent seeds.

| Model at m126 | Trainable scalars | Fits, maximum step1 | Fits, maximum step0.5 | RMS error, both caps | Incorrect signs per seed, both caps |
|---|---:|---:|---:|---:|---|
| Dense width55 | 3190 | 0/3 | 0/3 | 0.54429–0.57477 | 22,14,22 |
| Closure n1024,p1 | 3087 | 2/3 | 1/3 | 0.031621–0.040749 | 0,0,0 |
| Dense width105 | 11340 | 0/3 | 0/3 | 0.18535–0.34359 | 4,8,4 |

The initialization multiplies W by m/2=63 before dictionary construction,
for every architecture. With ordinary gain1, all three models fitted0/3 and
ended near MSE1 at physical clock10000. The error advantage therefore concerns
the high-gain initialization. Width55 approximately matches trainable scalars;
width105 separately matches total retained predictor scalars, including the
closure dictionaries:11340 versus11279.

The optimizer is simultaneous full-batch GD with the maintained model
scaling, canonical mobilities(n,1,n), and one scalar Armijo backtracking step.
It uses no Adam, momentum, readout solve or quasi-Newton stage. Every attempt
is capped at30000 accepted updates,90000 training forward evaluations,
physical clock10000 and75 seconds including initialization/export. The
primary dense runs reached30000 updates at physical clocks921–1306; closure
endpoints reached clocks3302–3454 and stopped on fit or wall time. These
unequal physical clocks matter when interpreting the common finite budgets.

The result is a large empirical training-error advantage and perfect sampled
sign classification for the closure. The stricter fitting separation is
sensitive to the declared step-cap/wall-time protocol. No nonrepresentation,
converged-minimum, continuous-flow, asymptotic-rate or generalization claim
follows. No additional training is authorized by this closed GD protocol.

GD evidence and final checks are recorded in [GD_RESULTS.md](GD_RESULTS.md),
[gd_check.md](gd_check.md), [gd_audit.md](gd_audit.md), and the
[raw manifest](../../data/generated/alternating_circle_fit_capacity_20260921/gd_run01/run_record.json).
The exact training command was:

```bash
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/alternating_circle_fit_capacity_20260921/gd_runner.py --output data/generated/alternating_circle_fit_capacity_20260921/gd_run01
```

The45 attempts comprise39 originals and6 prescribed reproductions. Every
reproduction exactly matched its original endpoint MSE and fit status. Summed
worker-process time was1771.514387s of2500s; the maximum attempt time was
71.022697s of75s. The frozen protocol and producer remained unchanged,
with hashes bound in every record and the campaign manifest.

Independent NumPy replay passed all45 attempts, all815613 accepted-step trace
entries and220 retained full GD update pairs. Maximum prediction discrepancy
was3.153e-14; maximum parameter-update discrepancy was1.732e-14. All sources,
datasets, dictionaries, configurations, gate decisions and budgets passed.
Separate analysis also passed every prediction/gradient/trace/reproduction
check, with no unresolved numerical conditions. Valid evidence does not turn
the failed scientific separation criterion into a pass.

The combined no-training checking/analysis accounting is170.44s of300s:
a conservative20s for earlier preflights,92.32s external final replay and
58.12s external final analysis including plots. The evidence and products are:

- [Independent replay](../../data/generated/alternating_circle_fit_capacity_20260921/gd_check_scratch/replay.json).
- [Final analysis](../../data/generated/alternating_circle_fit_capacity_20260921/gd_analysis01/analysis.json) and [timing](../../data/generated/alternating_circle_fit_capacity_20260921/gd_analysis01/timing.json).
- [Loss curves versus GD updates](../../data/generated/alternating_circle_fit_capacity_20260921/gd_analysis01/gd_selected_m126_accepted_steps.png).
- [Loss curves versus physical clock](../../data/generated/alternating_circle_fit_capacity_20260921/gd_analysis01/gd_selected_m126_physical_clock.png).
- [Sample-size ladder](../../data/generated/alternating_circle_fit_capacity_20260921/gd_analysis01/gd_sample_ladder.png).

Root owns the GD protocol, runner, GPU preflight, README and Git transaction;
scoped producer owns `gd_benchmark.py`; independent checker owns `gd_check.py`,
`gd_check.md`, `gd_replay.py` and `gd_audit.md`; scoped analyst owns
`gd_analyze.py` and `GD_RESULTS.md`. All generated data remain outside Git.

## Completed Adam campaign

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
