# Unfreezing the derivative p3 dictionary: completed one-case test

At width2048 on alternating labels plus two outliers, training the exact
initialized p3 vectors reduces circle RMS from1.100119 to0.896425. This is
18.52% lower than frozen p3 but18.51% higher than frozen p7's0.756424.
Thus it improves the same p3 representation but does not beat the p7 result
the user identified. Both numerical levels agree on both comparisons.

## What was tested

The user's clarification requested the existing derivative-p3 initialization,
then unfreezing its vectors. The6 lower and12 upper vectors,12-by-6 M,
read-in and readout all start EXACTLY as in the archived p3 model. Only the
basis-freeze decision changes. There is no dense residual, new normalization,
regularizer, seed, learning-rate search, momentum or Adam.

All five blocks follow simultaneous factor-coordinate gradient flow for
unhalved probability MSE. The new basis vectors use the same population L2
metric as the read-in/readout; M retains its Frobenius metric. Finite
mobilities are n for w,c,b1,b2 and1 for M. Adaptive Heun approximates this
specified flow. It is not canonical dense-W2-coordinate flow and it is not
the earlier response-cache/streaming-sketch proposal.

Task: eight angles15,27,39,51,63,75,165,285 degrees with alternating +/-1
labels, original width2048 and seed20260920. Primary metric is8192-angle RMS
agreement with the same archived dense learned function, evaluated at each
model's own first detected training-MSE0.001 crossing. It is not risk against
an independently prescribed whole-circle target.

| Model | Vectors | Trainable scalars | Circle RMS | Fitted flow time |
|---|---:|---:|---:|---:|
| Frozen derivative p3, archived finer |18|6216|1.1001187614|241.985274|
| Trainable derivative p3, primary |18|43080|0.8961921388|2576.970745|
| Trainable derivative p3, finer |18|43080|0.8964250064|2581.882040|
| Frozen derivative p7, archived finer |72|7340|0.7564240400|220.676840|
| Frozen p3, fresh reproduction |18|6216|1.1001187614|241.985274|

The dense reference itself fits at time156.952892. Every listed fitted model
reaches training MSE0.001. The trainable model requires about10.67 times the
flow time of frozen p3 under the declared metric. This is not a hardware
speed benchmark. Read-in/readout/middle coordinates retain their previous
mobilities; the new coordinates change the learning path.

Unfreezing adds36,864 trainable scalars already present as stored dictionary
entries. The working p3 model retains43,080 total scalars and middle rank at
most6. This is the same stored representation size, but not a trainable-
parameter-matched improvement. Final RMS basis motions are0.868289 lower and
0.770762 upper: the vectors actually move substantially. No post-training
projection into the original span is used.

## Validation and numerical scope

Seven CPU checks verify the five gradients by automatic differentiation and
finite differences, the energy identity, frozen reduction against maintained
code, and five-array checkpoint reconstruction including the initial M
anchor. Largest gradient discrepancy is4.17e-17. The runner's approximate
event locator uses30 bisections on the accepted state chord, matching the
historical producer's convention; it is not an exact continuous-flow event.

Primary/finer rtol6.25e-5/1.5625e-5, atol=rtol/100. Their whole-circle
endpoint maximum discrepancy is0.0030338942, below the preregistered0.01.
The8192/4096 RMS changes are at most2.23e-16. Consequently no extra numerical
run is eligible. The frozen reproduction differs from the historical final
prediction by9.46e-14 and fit time by3.95e-12.

The separate NumPy empirical audit replays38 saved snapshots and3 endpoints,
checks all five initial arrays exactly, verifies hashes and first-crossing
histories, and recomputes comparisons without the producer's forward/RHS.
Maximum prediction replay error is1.73e-14 and loss replay error1.67e-15.
Full evidence: TRAINABLE_DICTIONARY_CHECK.md and TRAINABLE_RESULTS_CHECK.md;
raw checks: data/generated/adaptive_response_compression_20260922/
independent_trainable01/checks.json. These are internal checks, not promotion.

The preregistered empirical discriminator passes versus frozen p3 and fails
versus frozen p7. This one task/seed does not establish or rule out hierarchy
convergence, broad usefulness of moving dictionaries, parameter efficiency,
or the efficacy of the distinct response-sketch method. No follow-up tuning
was performed after seeing the results.

## Outputs and exact reproduction

Run from /home/amir/Codes/PDE with /home/amir/miniconda3/bin/python -B.
The interpreter is Python3.10.14, Torch2.9.0+cu130, NumPy1.26.4; float64,
one numerical CPU thread, deterministic CUDA, TF32 disabled. GPU0/GPU1 are
RTX3090. Both base levels ran concurrently. Exact run commands:

```text
/home/amir/miniconda3/bin/python -B studies/adaptive_response_compression_20260922/run_trainable_p3.py --out data/generated/adaptive_response_compression_20260922/trainable_p3_primary01 --device cuda:0 --rtol 6.25e-5 --wall-limit 180
/home/amir/miniconda3/bin/python -B studies/adaptive_response_compression_20260922/run_trainable_p3.py --out data/generated/adaptive_response_compression_20260922/trainable_p3_refined01 --device cuda:1 --rtol 1.5625e-5 --wall-limit 180
/home/amir/miniconda3/bin/python -B studies/adaptive_response_compression_20260922/run_trainable_p3.py --out data/generated/adaptive_response_compression_20260922/frozen_p3_replay01 --device cuda:0 --rtol 1.5625e-5 --wall-limit 100 --frozen
/home/amir/miniconda3/bin/python -B studies/adaptive_response_compression_20260922/analyze_trainable_p3.py --out data/generated/adaptive_response_compression_20260922/trainable_analysis02
```

Reruns require fresh output directory names; the producer refuses overwrite.
Each run retains config/source/input hashes, exact commands, initialization
identities, complete saved states, losses/accepted steps/error estimates,
endpoint curves, summary and output hash. Source files remain unchanged
through all three training runs. The empirical audit retains its own source
and invocation. No maintained code/book or Git index was modified.

Final plots and metrics are in trainable_analysis02. Root inspected the
figure. trainable_analysis01 is retained; analysis02 only fixes the figure's
automatic negative-time axis margin/title, with identical scientific metrics.
The plotted x-axis is symmetric logarithmic restricted to nonnegative time,
and the MSE axis is logarithmic. Full-circle prediction curves are linear.

Recorded GPU-worker times26.428166+26.134480+16.633184 total69.195830 seconds.
They exclude interpreter/device startup; charge the entire40-second overhead
reservation conservatively, for109.195830 seconds total against the600-second
cap. From the inherited996.209566 allowance this leaves887.013736 seconds,
with no reservation, pending worker, eligible extra or authorized tuning
branch. This bounded request is complete.
