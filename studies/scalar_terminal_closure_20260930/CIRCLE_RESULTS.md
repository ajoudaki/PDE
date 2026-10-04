# Scalar ODE versus width-1024 dense training on the circle

Research experiment, 2026-09-30. Both the original campaign and the separately
planned continuation of center/edges are complete, with independent checks.
All five dense and q=1 reference pairs now have training MSE below 1e-7 at
their recorded common physical times. Every numerical refinement gate passes.

The original experiment supports a useful **terminal approximation of q=1**,
with limitations for reproducing dense training. A small training residual
does not by itself ensure an accurate unseen function. There are three
distinct discrepancies: q=1 versus dense, freezing the remaining q=1 dynamics,
and representing the query responses with finitely many Fourier coefficients.

Final primary results, switching from q=1 to the scalar ODE at training MSE
0.01, are below. Only the center/edges endpoint uses the supplemental horizon;
the original capped-horizon comparison is preserved later in this report.

| Task | Scalar vs dense circle RMS | Scalar vs dense sign disagreement | Scalar vs q=1 circle RMS |
|---|---:|---:|---:|
| Two outliers, alternating | 0.236905 | 2.490% | 0.003869 |
| Quadrant, alternating | 0.382254 | 1.587% | 0.007184 |
| Quadrant, paired labels | 0.049760 | 0.146% | 0.033491 |
| Quadrant, center/edges | 0.035672 | 1.172% | 0.024929 |
| Equally spaced, mixed labels | 0.014001 | 0.415% | 0.000654 |

[Final circle functions](../../data/generated/scalar_terminal_closure_20260930/circle_analysis_final_02/final-circle-functions.png),
[training loss curves](../../data/generated/scalar_terminal_closure_20260930/circle_analysis_final_02/losses.png),
and [all switch errors](../../data/generated/scalar_terminal_closure_20260930/circle_analysis_final_02/error-vs-handoff.png)
are available as PNG and companion PDF files. Final numerical tables are in
[metrics.csv](../../data/generated/scalar_terminal_closure_20260930/circle_analysis_final_02/metrics.csv).

## What was tested

All five shallow circle tasks from the authorized manuscript bundle were used,
with eight binary-labeled points each. Exact inputs and provenance are in
[CIRCLE_TASK_INPUTS.md](CIRCLE_TASK_INPUTS.md) and
[circle_task_inputs.json](circle_task_inputs.json). Both hidden layers have
width 1024; activation is tanh, without biases. Dense and q=1 use identical
initial first weights and middle mixer, seed 20260920, and exactly zero
readout. The same initialization is reused across tasks. These are new
matched runs on the manuscript's task geometries, rather than a replay of
the historical width-2048, small-random-readout figures.

The scalar model starts from the actual q=1 state when its training MSE
first crosses 0.1, 0.01, or 0.001 on the coarse integration grid. The primary
switch is 0.01; all three switches are reported. It uses its own residual
feedback after switching. Full q=1 continues separately as the reference.
This experiment does **not** replace the preceding q=1 training by a scalar
model. No future full-model outputs or unseen labels enter the scalar model.

There are eight evolving residuals, their eight time integrals, and one
integral of the residual norm. The equations are

    residual_dot = -response_matrix @ residual
                   + norm(residual) * memory_correction
    integrated_residual_dot = residual
    integrated_norm_dot = norm(residual).

The response matrix and memory correction are the exact q=1 aggregates at
the switch, including moving-key effects. The query output is its switch
value minus its frozen query response applied to integrated residual, plus
its frozen query memory correction times integrated norm. The derivation,
normalizations, and distinction between scalar loss and the truncated
query function are checked in [CIRCLE_QUERY_CHECK.md](CIRCLE_QUERY_CHECK.md).

The ten functions of circle angle needed for this readout are represented
by 32 odd Fourier frequencies, 1 through 63, with sine and cosine terms.
Their coefficients use 2048 switch-time q=1 queries. Endpoint validation uses
8192 independent, midpoint-shifted circle angles. Those queries have no
assigned test labels: sign disagreement means disagreement with dense,
not error against an unknown true classification rule.

| Retained model quantities | Number of scalars |
|---|---:|
| Evolving residuals and integrals | 17 |
| Frozen training response matrix and correction | 72 |
| Frozen circle-function coefficients | 640 |
| **Total scalar model** | **729** |
| Dense moving parameters | 1,051,648 |
| q=1 moving coordinates | 19,457 |
| q=1 fixed mixer, required before the switch | 1,048,576 |

The 729 count includes all fixed model coefficients, but excludes numerical
solver workspace, requested outputs and optional provenance. Producing those
coefficients still requires the full q=1 switch state and mixer. One observed
count below 1024 is not an asymptotic sublinear-storage accuracy theorem.

## Original, precommitted comparison

[CIRCLE_EXPERIMENT_PLAN.md](CIRCLE_EXPERIMENT_PLAN.md) was frozen before
implementation and training. Dense and q=1 used float64 RK4, steps 1/8 and
1/16 independently from initialization. Both resolutions used identical
switch times and endpoint time. Scalar integration used DOP853 with relative
tolerance 1e-10 and absolute tolerance 1e-12. The coarse run stopped when
both full-model MSEs were <=1e-7, or at time 512. The reporting criterion
for a fitted full-model endpoint was MSE <=1e-6 for both models.

The following is the original comparison, including the unfinished case.
RMS errors are absolute prediction errors in label units, over the circle
validation grid. All scalar entries here use the primary 0.01 switch.

| Task | Recorded common time | Full models fitted? | q=1 vs dense RMS | Scalar vs dense RMS | Scalar vs dense sign disagreement | Scalar vs q=1 RMS |
|---|---:|---|---:|---:|---:|---:|
| Two outliers, alternating | 244.5 | Yes | 0.236240 | 0.236905 | 2.490% | 0.003869 |
| Quadrant, alternating | 346.375 | Yes | 0.381049 | 0.382254 | 1.587% | 0.007184 |
| Quadrant, paired labels | 292.125 | Yes | 0.020984 | 0.049760 | 0.146% | 0.033491 |
| Quadrant, center/edges | 512 | **No** | 0.037766 | 0.035136 | 1.147% | 0.023070 |
| Equally spaced, mixed labels | 31.125 | Yes | 0.014276 | 0.014001 | 0.415% | 0.000654 |

At time 512, center/edges has dense MSE 1.33940e-5 and q=1 MSE 4.69165e-5.
Its row is a finite-horizon comparison, not a fitted-endpoint claim.

Original scalar-versus-q=1 circle RMS, for every prescribed switch:

| Task | Switch at 0.1 | Switch at 0.01 | Switch at 0.001 |
|---|---:|---:|---:|
| Two outliers, alternating | 0.031538 | 0.003869 | 0.003011 |
| Quadrant, alternating | 0.087254 | 0.007184 | 0.006925 |
| Quadrant, paired labels | 0.113615 | 0.033491 | 0.002696 |
| Quadrant, center/edges, time 512 | 0.467170 | 0.023070 | 0.015756 |
| Equally spaced, mixed labels | 0.008958 | 0.000654 | 0.0000669 |

The full 15-switch metrics, maxima, sign errors away from near-zero dense
outputs, and refinement diagnostics are retained in the original analysis
CSV and JSON. No switch was selected after seeing its accuracy.

## Error sources and the loss/readout distinction

The following decomposition is at the original endpoint and primary switch.
The first error compares the untruncated frozen observer to q=1; the second
compares its finite Fourier readout to that observer. These RMS values need
not add because pointwise errors can cancel.

| Task | Freezing error RMS | Fourier contribution RMS | Improvement over static Fourier switch function |
|---|---:|---:|---:|
| Two outliers, alternating | 0.002436 | 0.002957 | 17.45 times |
| Quadrant, alternating | 0.001967 | 0.007012 | 8.73 times |
| Quadrant, paired labels | 0.033469 | 0.001233 | 7.21 times |
| Quadrant, center/edges, time 512 | 0.017685 | 0.012825 | 5.22 times |
| Equally spaced, mixed labels | 0.000654 | 0.000000094 | 138.70 times |

The continuation does more than retain a nearly finished function: it improves
the circle RMS error over the original direct-handoff static control by
17.43, 8.68, 7.21, 5.19, and 138.70 times in task order. All five satisfy the
prescribed meaningful-improvement criterion. The table additionally reports
the representation-matched Fourier static control, computed during analysis.
This control does not establish that every
term of the ODE is essential; no term-ablation experiment was performed.

The internal residual ODE and the compressed circle function have different
training losses. Without Fourier truncation their training predictions obey
the same integrated identity. Finite Fourier truncation can break that
identity, so fitting the internal residual does not automatically fit the
readout function at the training angles.

| Task | Largest recorded tail residual-MSE error vs q=1 | Scalar residual endpoint MSE | Fourier function training MSE |
|---|---:|---:|---:|
| Two outliers, alternating | 1.55884e-4 | 3.87009e-7 | 6.61266e-6 |
| Quadrant, alternating | 2.05557e-4 | 4.72431e-7 | 2.89479e-5 |
| Quadrant, paired labels | 7.08586e-4 | 1.27136e-9 | 5.23053e-6 |
| Quadrant, center/edges, time 512 | 2.69980e-4 | 2.09484e-5 | 4.92873e-4 |
| Equally spaced, mixed labels | 9.35323e-5 | 2.19220e-7 | 2.19287e-7 |

The primary dense-imitation criterion was circle RMS <=0.05 and sign
disagreement <=1%. Among the originally fitted cases, paired labels and
equally spaced mixed labels meet these two fidelity thresholds; the two
alternating tasks do not. The primary q=1 fidelity criterion was RMS <=0.01
and maximum error <=0.05: the two alternating tasks and the equally spaced
task meet it, while paired labels and the original center/edges comparison
do not. Fitting flags are reported separately. The analyzer's additional
combined `imitation_outcome` field also requires Fourier training MSE <=1e-6;
that is a stricter diagnostic, not the originally specified fidelity test.

## Supplemental fitted-endpoint continuation

[CIRCLE_ENDPOINT_EXTENSION_PLAN.md](CIRCLE_ENDPOINT_EXTENSION_PLAN.md) was
recorded during the original campaign, after observing slow convergence and
before extension implementation or execution. It extends every originally
unfitted task with a valid coarse/fine comparison, selected solely by fitting
status, to both losses <=1e-7 or time 1024. Only center/edges qualifies.
It keeps the original states, steps, switch times, coefficients and Fourier
mode count, and preserves the original time-512 comparison above.

The supplemental coarse and fine runs both reach the same time **950**.
Selected fine losses are dense **1.49329e-8** and q=1 **9.99540e-8**. The
q=1-versus-dense circle RMS is **0.0398025**. The other four task results
are unchanged.

| Center/edges switch | Scalar vs dense RMS | Scalar vs dense sign disagreement | Scalar vs q=1 RMS | Scalar residual MSE | Fourier function training MSE |
|---|---:|---:|---:|---:|---:|
| 0.1 | 0.534041 | 36.426% | 0.558039 | 1.79540e-5 | 2.79332e-5 |
| 0.01, primary | 0.035672 | 1.172% | 0.024929 | 4.30765e-8 | 6.10323e-4 |
| 0.001 | 0.038748 | 1.196% | 0.017064 | 1.24647e-7 | 7.82401e-4 |

The primary freezing error is 0.0195600 RMS and the Fourier contribution is
0.0131408 RMS. At the later switch these become 0.00664525 and 0.0157999.
The primary continuation improves over its Fourier static control by 5.10
times. In contrast, the early 0.1-switch continuation becomes worse than its
static control at the extended endpoint: a much smaller internal residual
coexists with a substantially wrong unseen function. The extra drift of that
early approximation was missed by stopping the comparison at time 512.

The center/edges coarse/fine endpoint changes are 1.58e-9 RMS for dense,
5.78e-10 for q=1, and 7.88e-10 for the primary scalar function. The primary
scalar loss step sensitivity is 1.68e-11. All prescribed gates and the
supplementary scalar-loss gate pass. The final analyzer again reports 1390
passing checks. Its plot-only revision gives each loss row its own recorded
time range; all metrics are unchanged from `circle_analysis_final_01`.

The independent empirical check reconstructs both extended endpoints,
verifies bitwise preservation of all four full-history prefixes, verifies
the six unchanged handoff file hashes, and verifies all 48 copied artifacts
of the other four cases against their originals. Supplemental reconstruction
and observer discrepancies are at most 1.93e-12. The source and resume checks
are in [CIRCLE_EXTENSION_SOURCE_CHECK.md](CIRCLE_EXTENSION_SOURCE_CHECK.md)
and [CIRCLE_EXTENSION_CHECK.md](CIRCLE_EXTENSION_CHECK.md).

## Numerical evidence and scope

The original five resolution pairs all pass the predeclared refinement
thresholds, as well as the supplementary scalar-loss refinement check.
The largest full-model training-loss step change is 7.04e-8, and the largest
primary scalar endpoint circle RMS step change is 1.33e-7. These are much
smaller than the reported approximation errors. No step-1/32 rerun was needed.
The original analyzer reports 1390 passing checks, including finite saved
arrays, direct recomputation of metrics and both query readouts, and
coarse/fine sensitivity.

[CIRCLE_EMPIRICAL_CHECK.md](CIRCLE_EMPIRICAL_CHECK.md) independently rebuilds
predictions from the saved dense and q=1 states, explicitly forms the q=1
middle operator, and checks training/query response coefficients and Fourier
construction. Its original coverage is all five tasks, both resolutions,
and all 30 handoff states. Construction and reconstruction discrepancies
are at most 2.43e-12. Those small consistency errors are distinct from the
actual Fourier representation error.

The original producer checks finite loss at every recorded RK step and saved
states are independently finite. It does not log every full state block at
every intermediate RK stage. Its memory statistic is sampled RSS, not a
continuous high-water measurement or an enforced 4-GiB bound. These protocol
limitations are retained in the source audit. The supplemental producer
checks all accepted state blocks, uses a guarded deadline, and records
process high-water RSS. A finite numerical endpoint and 8192 validation
queries are not infinite-time or uniform-circle certificates.

The original run took 1615.084 seconds on CPU with two BLAS threads; the
supplement took 502.925 seconds, for 2118.009 seconds of main campaign runtime.
The original maximum sampled RSS was 136.16 MiB. The supplemental measured
process high-water RSS was 143.86 MiB, below its enforced guard threshold.
The original analysis took 12.123 seconds, the first final analysis 12.343
seconds, the plot-only revision 11.257 seconds, and all five portable endpoint
checks together 3.330 seconds. These analyses and bounded independent checks
fit comfortably within the unchanged 3600-second cumulative budget. The
1200-second supplemental allocation preserved more than the required
120-second final-analysis reserve.
No GPU or installation was used.

An initial attempt, `circle_width1024_01`, failed before training on the
stored input-array orientation. It is preserved; the corrected fresh run
is `circle_width1024_02`. No task, seed, Fourier cutoff, or model parameter
was changed in response to the scientific results.

The standalone export in [CIRCLE_PORTABLE_MODEL.md](CIRCLE_PORTABLE_MODEL.md)
contains exactly 729 float64 entries and runs without neuron states, a mixer,
labels, or an endpoint-output oracle. All five standalone primary models were
exported and checked against their recorded final scalar endpoints, including
the extended center/edges endpoint. Every model has exactly 729 entries and
passes the assigned endpoint check; the largest circle-output discrepancy is
2.21e-12. Their models, copied standalone evaluator, predictions and checks
are in `data/generated/scalar_terminal_closure_20260930/circle_portable_final_01/`.
An extra, unrequested
whole-trajectory state diagnostic narrowly exceeds its 1e-8 threshold
(1.02738e-8); that false diagnostic is preserved, and no solver tolerance
was retuned. This portability check does not improve the scientific errors.

## Research interpretation

On the alternating tasks, q=1 itself differs from dense by 0.236 and 0.381
RMS. By the triangle inequality, making the scalar approximation of q=1
arbitrarily accurate cannot remove those discrepancies from dense. Improving
the second compression alone therefore cannot meet the dense fidelity target
on those runs.

Later switches reduce the freezing error substantially, but leave a floor
when the finite angular representation dominates. The paired-label task is
a useful counterexample to judging unseen fidelity by scalar loss alone:
its primary residual MSE is about 1e-9 while its query error against q=1 is
0.0335 RMS. The center/edges geometry additionally exposes appreciable error
from the finite circle readout itself.

These are empirical conclusions for five prescribed tasks and one shared
initialization. The conditional terminal theorem remains unchanged. None
of these runs certifies its full terminal tube; a positive instantaneous
margin is not such a certificate, and several observed margins are negative.
For the antipodal task, the physical odd-residual subspace has a positive
reported restricted margin, while the redundant full-space diagnostic is
negative. No universal fitting or population-limit claim follows.

| Claim | Current evidence status |
|---|---|
| Exact finite q=1 residual/query identities | Internally derived and checked; numerically verified on saved states |
| Autonomous 729-number terminal circle evaluator | Implemented and independently executable |
| Accurate q=1 terminal continuation for every task at the primary switch | Not supported by the prescribed fidelity thresholds |
| Accurate dense unseen function for every tested task | Not supported; the two alternating cases show a large first-closure gap |
| Very small internal scalar loss is sufficient evidence of accurate unseen output | Contradicted as an empirical inference by the paired-label example |
| Initialization-to-endpoint, sublinear-state dense approximation | Open; this experiment does not construct or test it |

## Reproduction and artifacts

Run from the repository root, using fresh output names when reproducing:

```bash
env OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 \
  /home/amir/miniconda3/bin/python -B \
  studies/scalar_terminal_closure_20260930/circle_terminal_experiment.py \
  --output data/generated/scalar_terminal_closure_20260930/circle_width1024_02 \
  --budget 3599

env OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 \
  /home/amir/miniconda3/bin/python -B \
  studies/scalar_terminal_closure_20260930/analyze_circle_experiment.py \
  --run data/generated/scalar_terminal_closure_20260930/circle_width1024_02 \
  --output data/generated/scalar_terminal_closure_20260930/circle_analysis_original_01

env OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 \
  /home/amir/miniconda3/bin/python -B \
  studies/scalar_terminal_closure_20260930/extend_circle_experiment.py \
  --run data/generated/scalar_terminal_closure_20260930/circle_width1024_02 \
  --output data/generated/scalar_terminal_closure_20260930/circle_width1024_extension_01 \
  --budget 1200

env OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 \
  /home/amir/miniconda3/bin/python -B \
  studies/scalar_terminal_closure_20260930/analyze_circle_experiment.py \
  --run data/generated/scalar_terminal_closure_20260930/circle_width1024_extension_01 \
  --output data/generated/scalar_terminal_closure_20260930/circle_analysis_final_02
```

The original data directory contains initializer, frozen source/configuration,
provenance, all full endpoint states, all handoff states/coefficient arrays,
and trajectories. Its analysis directory contains `analysis.json`,
`metrics.csv`, and PNG/PDF figures `final-circle-functions`, `losses`, and
`error-vs-handoff`. Supplemental artifacts use the distinct extension root.
Source hashes are recorded in the corresponding provenance and audit files.
No manuscript, maintained book/code, Git index, commit, or push was changed.
