# Scoped runner audit and independent checkpoint replay

Assignment: read the complete study-owned `NETWORK_ENGINE.py`, `RUN.py`,
`DATA.py`, `BATCH.py`, and `PLAN.md`; inspect physical scaling, split/test
handling, checkpoint selection, and compute reporting. Inputs are limited to
the current study and the previously assigned established equations. This is
a scoped implementation audit, not an isolated mathematical review or a
population-convergence certification. No root-owned file was edited and no
scientific training was executed by this reviewer.

## Current assessment

The actual-network equations, stored initialization, full-batch integration,
split construction, and validation-only checkpoint rule are correct for the
declared configurations. Four pre-main findings were sent immediately to the
root; the corrected source and frozen final numerical gate were reread before
this assessment. The history below preserves what changed.

The actual network computes `h1=tanh(w U.T)`, `h2=tanh(M h1)`, and
`f=c.T h2/n`, with `U=x/sqrt(d)`. Its independent Gaussian stored variances
are `Var(w)=1`, `Var(M)=1/n`, and `Var(c)=1/n^2`. For unhalved mean squared
loss, ordinary gradients in all blocks carry the output factor `1/n`.
Multiplying first/readout gradients by mobility `n` gives the implemented
`-2/m` first/readout contractions; the middle mobility is one, so the
implemented middle contraction is `-2/(mn)`. The backward pass uses the same
`M.T`. Every block accumulates contributions from the complete fixed training
set before any state update. Both Heun stages are simultaneous full-state
evaluations, without minibatch updates.

`DATA.py` samples validation indices only from the official training split,
reserving 500 examples per selected digit. It then uses every remaining
selected training example and all selected official-test examples. The
transform is independently applied to each image and estimates no statistic
from test inputs or labels. Training/validation labels are the only labels
read by optimization, continuation, checkpoint selection, and precision
probes. Test arrays are extracted for final metrics after those choices.
The toy producer generates all three splits in advance, but its test values
are unused by those choices. No computational test leakage was found.

The corrected main selector evaluates validation MSE only at the prescribed
eligible times `(0,10,20,50,100,150,200)` and multiples of 100 thereafter.
Strict improvement implements the earlier-time tie rule. Extra curve points
every 10 units do not enter checkpoint selection. Extension at time `T`
compares validation MSE at `T-100` against `T`, and obeys the stated 0.001
improvement threshold, T600 ceiling, and per-run wall cap. Runtime-truncated
terminal states remain distinct from the best eligible checkpoint.

Integration timing synchronizes the GPU around each Heun step. Training wall
time includes observations and checkpoint clones, while initialization,
optional late precision probes, and final reporting are separate. Comparing
per-step or total integration cost should state the different chosen time
steps and physical horizons. Matching nominal particle count and network
width is the declared scientific comparison, not matching parameter counts
or FLOPs. GPU peak allocation measures live tensor allocation, not device
reservation or system process RSS.

## Findings and resolutions before main training

1. **Unverified pilot fallback.** The original `BATCH.pilot_report` could
   choose one more halving when its current comparison failed, without
   checking that newly selected step against its own half-step. It also
   omitted the plan's loss-difference trigger. The root ran the additional
   closure 0.125-versus-0.0625 comparison and froze `pilot_gate_final.json`.
   Final main steps are 0.25 for the network and 0.125 for the closure.
   Prediction RMS differences are `6.50e-5` and `4.37e-5`; validation loss
   differences are `7.11e-6` and `1.69e-6`. Corrected main dispatch requires
   both `step_gate_pass` and `precision_pass`. Historical intermediate pilot
   summaries remain retained and must not be treated as the final gate.
2. **Extra selection opportunities.** The original runner selected from all
   every-10-unit curve points, exceeding the plan's checkpoint schedule.
   Corrected `observe` restricts eligibility to the plan's times while still
   saving the dense curves. The plan explicitly records this distinction.
3. **Asymmetric retained memory.** Closure memory included fixed marks and
   cached contractions, while network memory counted only current trainable
   arrays even though its initial state was also retained for observations.
   Corrected reports count initial plus current network arrays, distinguish
   moving state from retained model storage, and separately include the best
   checkpoint. Historical toy summaries predate this correction; recompute
   or label their old memory field before comparing it.
4. **Precision-probe contamination of production peak.** The original peak
   was queried after the optional simultaneous float32/float64 continuation.
   Corrected reports capture production peak before this probe and retain a
   separately named peak including controls and test evaluation. This avoids
   attributing validation overhead to production training memory.

The intermediate `pilot_report` helper still writes provisional decisions;
the corrected main path consumes only the explicitly checked final gate.
The late precision-probe pass flag and full-data half-step controls must be
checked by the campaign analysis before making an accuracy-preservation
claim. The runner records a failed late probe but does not itself invalidate
its saved test report. A failed numerical control must therefore be labeled
unresolved or repaired according to the plan, rather than being ignored.

## Independent replay and data audit

`REPLAY.py` contains no imports from either engine, the runner, initializer,
or dataset producer. It uses NumPy float64 to evaluate the saved raw weights
and fixed marks directly, preserving input values rounded to each run's
working dtype. It never retrains a trajectory. Its checks cover best and
terminal train/validation/test predictions, recomputed MSE, classification
sign changes, the first eligible validation minimizer, panel hidden Grams,
and initial/current RMS motion. Archives and reports are hashed.

All eight completed toy and toy-control runs passed. Maximum prediction
discrepancy was `1.754e-7` among float32 runs and `2.443e-15` among float64
runs, with zero sign disagreements. This confirms the correspondence
between saved checkpoints and reported finite predictions; it does not
verify every intermediate trajectory state or remove discretization error.

The independent local-IDX audit additionally verifies all four raw MD5 and
SHA256 hashes, reconstructs the seeded splits, regenerates mapped labels,
and recomputes every normalized image. Every saved ID, label, and float32
input coordinate agrees exactly. There are 10,552 training, 1,000 validation,
and 1,902 official-test examples; the training and validation IDs are disjoint.
The test image/label origin is the official test files rather than the
training files. Output: `replaychecks/dataset_audit.json`.

Toy replay reports and independently recomputed prediction arrays are under
`data/generated/first_order_dimension_mnist/replaychecks/`. Main replay
results are under its `main/` subdirectory. All six main runs passed direct
best/final checkpoint replay, with maximum prediction difference `4.873e-7`
and zero classification sign changes. The aggregate record is
`replaychecks/main/all_main_summary.json`. This confirms every saved terminal
and selected validation coordinate; arbitrary intermediate curve points have
no saved weights and are not independently replayed here. Campaign training
and numerical controls are outside this reviewer's execution scope.

## User clarification and primary validation analysis

The user subsequently clarified that the primary question is approximation
of each actual-network validation prediction; classification is secondary.
The root preserved training configurations and amended the interpretation in
the plan. `VALIDATION_ANALYSIS.py` was read completely under this additional
scope. It intersects saved physical times across all six runs and compares
the complete validation vectors at those common times. It reports every
closure/network seed pair as well as comparisons against the three-network
mean. Relative RMS divides raw discrepancy RMS by raw reference RMS; no
amplitude fit, calibration, or per-image renormalization is performed.

The individual pair and ensemble calculations, axis ordering, time lookup,
and worst-example extraction are algebraically correct. Worst-example IDs
refer to the official training images assigned to validation and are ranked
by discrepancy between the model means, explicitly labeled as such. Seed
number matching is not a coupling of initial weights. Three-network mean
outputs provide a descriptive finite ensemble, not an exact population
target; network/network pairwise spread and closure/ensemble spread have
different reference variances and are not a calibrated error bound.

Before execution, two improvements were reported to the root: avoid
silently clipping the absolute-error ECDF at 0.4, and assert both dataset
hash identity and 1,000 unique validation IDs before attaching image IDs to
predictions. Label equality alone would not detect a hypothetical
within-class reorder. Float64 seed averaging was also recommended to avoid
unnecessary rounding. The root implemented all three improvements; the
complete corrected analysis was reread.

Independent output audit now passes for `validation_analysis_001`: all
1,000 unique validation images, all 51 common times from T0 through T500,
all nine individual seed pairs, ensemble comparisons, correlations, error
quantiles, sign metrics, and the 20 worst-example identities were recomputed.
The maximum scalar difference was `8.89e-16`. The exported NPZ pointwise
arrays and CSV columns match their independent reconstructions exactly.
The audit is recorded in `replaychecks/validation_analysis_audit.json` with
hashes of the source observations, dataset, analysis summary, and checker.
No unresolved arithmetic, row-identity, or time-alignment issue was found in
the primary analysis. Full-path numerical controls are evaluated separately
below.

The subsequent `validation_analysis_002` revision was also read completely
and independently checked. Its within-class calculations use the correct
500-image subsets for each digit; raw output spread and all correlations
and error statistics agree with recomputation. Within-class correlations
range from `0.9034` to `0.9454`, supporting substantial association beyond
the separation of the two label groups. The true-label predictor is
correctly labeled an oracle diagnostic, not a deployable or trained model.
Its output RMS discrepancy from the network mean is `0.17637`, versus
`0.06378`–`0.06714` for the individual closures. These are descriptive
post-training comparisons, without model selection or calibration.
Version 002's analysis, dataset, and run-summary hashes verify correctly;
its error statistics agree within `8.89e-16`. The figure was visually
inspected: digit colors are identified, the full ECDF tail is visible, and
axis labels distinguish the network mean from individual closures.
Record: `replaychecks/validation_002/validation_analysis_audit.json`.

## Full-horizon numerical controls

Both completed T600 half-step controls independently replay their best and
final raw weights, validation predictions, hidden Grams, and motion metrics.
The largest replay prediction difference is `4.905e-7`, with zero sign
changes. Independently comparing each half-step trajectory to its original
trajectory at all 61 shared saved times gives:

| Model | T600 validation RMS difference | T600 maximum absolute difference | T600 sign changes |
|---|---:|---:|---:|
| Actual network | `2.12662e-5` | `2.19644e-4` | 0 |
| Closure | `1.02369e-5` | `8.34763e-5` | 0 |

Every shared saved time satisfies the planned RMS and accuracy-shift gates.
The largest RMS over those saved times is `5.70840e-4` for the network and
`9.61117e-5` for the closure. The secondary analysis's final-time and
maximum-over-recorded-times control metrics agree with this independent
calculation, allowing its float32 aggregation roundoff. Records and replayed
predictions are retained under `replaychecks/controls/`. This supports the
specified step comparison at saved times; it is not a rigorous continuous-
time error certificate or an independent bound for every seed.

## Fresh trajectory reproduction and final report check

The root executed fresh seed1729 runs for both models in new
`reproduction/` directories. This reviewer independently compared their
training configurations, dataset hashes, selected/final times, step counts,
stop reasons, and every stored validation coordinate against the original
main runs. For each model, all `61 x 1000` validation outputs are bitwise
identical: largest per-time RMS and largest absolute discrepancy are both
zero, with no sign changes. Both select and finish at T600. Training
predictions, hidden Grams, selected/terminal test outputs, and every array
in the best/final checkpoints are also bitwise identical. The same
checkpoint arrays had already passed independent NumPy forward replay in
the original runs. Records: `replaychecks/reproduction/`.

These fresh runs satisfy the declared reproduction tolerances without
adding an independent scientific seed. They reproduce the finite working
computation; they do not certify its distance from continuous flow or an
infinite-population limit.

The complete drafted `REPORT.md` was read for outcome, verification, and
scope. No material overstatement was found. In particular it states the
finite three-network mean reference, substantial tail errors, within-class
correlations, validation's use in stopping, different independently selected
times, noncoupled initial seeds, and the absence of a full T600 float64 run
or a width/order convergence experiment. Its statement that half-step
endpoint classification signs are unchanged is independently verified for
both models. The primary numerical evidence remains raw same-time
validation prediction fidelity; supporting classification performance is
clearly secondary.

## Reviewed corrected source identity

At the completed source reread:

| File | SHA256 |
|---|---|
| NETWORK_ENGINE.py | `0c2fedf6ef6350b3715c6b0df0de91b90cba2c94a9895b970cb25ab067dc55bc` |
| RUN.py | `19c76bbb5b8ae012c13fd5c926cea0be43ab5f852fab84e35190d0001009a69e` |
| DATA.py | `e597bf39f578e240b3500186a0daf2da3ac5a124eb1a7b58b3cbc8e8770f9075` |
| BATCH.py | `2088fdf6fd8d92fd5a9ef99b280589aea3555471e6aebd1ff2297a536ecd5af7` |
| PLAN.md | `c3d1e38070225cdd1c1cbcd43dffc9aee481b31b2b9fbdcb45f2eb24b31a3a52` |

Each run's frozen source snapshot remains the authoritative record for that
run. Later substantive edits require a scoped follow-up review.
