# Rank-matched directly trained factors versus response moments

The moment closure has lower whole-circle error than directly trained factors
in all 29 numerically resolved comparisons. All five tasks were tested at
P=1,3,7 with two separately reported factor initializations. One factor cell
(hard outliers, P=1, seed 20260925) did not reach the common loss threshold
within its wall cap at either numerical resolution. Its terminal function
is excluded from the endpoint comparison.

Status: completed finite empirical comparison; final independent audit is
recorded in FACTOR_CONTROL_CHECK.md. No population, asymptotic-rate or optimal
compression theorem is asserted. This continues the same response-memory
study and leaves prior moment/dictionary results unchanged.

## What was compared

Both models have n=2048, the same two-hidden-layer tanh architecture, exactly
the same initialized W1,W0,W3, and the same original training data. Both retain
the actual dense initialized W0 and its transpose. Outer layers train with
the canonical mobilities (n,n). The factor control uses W2=W0+AB, with both
A and B trained by ordinary Euclidean full-batch gradient flow, mobility one.
No Adam, momentum, weight decay, optimizer tuning or reference-fitting is used.

A starts at zero. B has independent Gaussian entries with variance 1/rank.
This preserves the exact initial physical network and matches the initial
dense middle velocity in expectation. It does not match that velocity for
every realization. The factor seeds are 20260924 and 20260925; the dense
network seed is 20260920. Neither factor seed is selected as a method score.
The normalization was fixed before results, as recorded in
FACTOR_CONTROL_PROTOCOL.md.

The rank bound matches P times represented sample count: 8,24,56 for the
eight-sample cases and 4,12,28 for the four-representative antipodal quotient.
Thus the two factor arrays match the 2n times rank history-factor coordinate
budget. The closure also has auxiliary response states; equal rank is not
an assertion of identical total state or computational cost.

Each model stops at its own first physical training-MSE 0.001 crossing.
The comparison is sqrt(mean((model prediction-dense prediction)^2)) over
8192 uniform circle angles, checked against the nested 4096 grid. The dense
target is identical for all methods within each row. Four tasks use the
newly refined dense references; hard outliers use the previously selected
refined dense target. There is no full-circle label function in this metric.
Training loss sets the stopping point; the score measures reproduction of
the dense learned function on the circle.

## Results

The P=3 comparison is:

| Configuration | Correction rank | Response moments | Factor seed 20260924 | Factor seed 20260925 |
|---|---:|---:|---:|---:|
| Two outliers, alternating | 24 | 0.0729531 | 0.465456 | 0.460915 |
| Quadrant, alternating | 24 | 0.0456113 | 0.676639 | 1.54131 |
| Quadrant, paired labels | 24 | 0.00281761 | 0.375464 | 0.203580 |
| Quadrant, center/edges | 24 | 0.00487776 | 0.257864 | 0.249269 |
| Equal mixed odd | 12 | 0.000525665 | 0.0606940 | 0.0687051 |

At P=7 on the hardest case, moment RMS is 0.00466307 versus 0.516210 and
0.251026 for the two factor seeds: about 111 and 54 times smaller error.
The complete 15-row table, individual seed results, numerical sensitivities
and all failures are in factor_analysis01/summary.md and metrics.json under
this study's generated namespace. The P=7 paired-label and mixed-odd moment
scores retain their earlier precision limitations; their separation from
the much larger factor errors is resolved.

All 29 fitted comparisons pass the declared refinement and grid gates and
the score gap exceeds three times the largest factor/moment/dense finest-pair
RMS refinement sensitivity. Twenty-eight exceed a factor of two; the hard
P=1 seed 20260924 comparison is about 1.96. These numerical changes are empirical
sensitivity diagnostics, not rigorous error bounds. No monotone rank trend
is imposed on directly trained factors, and none is inferred from their data.

The hard P=1 seed 20260925 run ended with physical MSE 0.0572439 at level 0 and
0.0595962 at level 1 after its nominal 240-second cap. This is a bounded-run
non-hit, not a proof that the factor network cannot fit. Its terminal RMS
values are diagnostic only and are absent from the primary score curves.

## Interpretation

The result supports the specific response-moment evolution as a substantially
more faithful representation of dense learning than this directly trained
factor model at the same correction rank. The advantage persists even when
both models retain W0 and both have evolving correction directions.

Direct factor training changes the induced middle-matrix gradient flow:

    A_dot = -(d loss/d W2) B^T
    B_dot = -A^T (d loss/d W2)
    (AB)_dot = -(d loss/d W2) B^T B - A A^T (d loss/d W2).

Consequently the control's factor scale and metric are part of its definition.
The experiment establishes a comparison with that explicit baseline; it does
not test truncating canonical matrix-gradient updates by QR/SVD. That earlier
suggested comparator was not run. Final predicted-function agreement is the
observable here; no claim about matching all internal states is added.

## Execution, checks and reproduction

All 60 prescribed trajectories completed their recorded stopping rules: five
cases, three ranks, two factor seeds and two solver tolerances. There were 58
threshold hits and two caps for the same factor cell. No conditional level 2
trajectory was necessary for any fitted comparison. Recorded integration time
totals 2153.564842 GPU-seconds; summed per-run wall time is 2201.909124 seconds,
within the 3600 integration-second cap. Both GPUs were used concurrently.
The nominal per-run wall cap is checked between trials; capped runs exceed it
by less than 0.05 seconds, and those actual times are included in accounting.

The new implementation is factor_control_engine.py and run_factor_control.py.
Six deterministic CPU tests in test_factor_control.py cover gradient and
energy identities, forward/transpose actions, canonical initialization,
matrix-error control, restart and failure retention. Independent raw-input
autograd and saved-state reconstruction use check_factor_control_engine.py
and check_factor_control_endpoints.py. The independent report records exact
source hashes, commands, coverage, and final outcomes.

The four GPU batch commands use this common environment and runner:

```text
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 CUBLAS_WORKSPACE_CONFIG=:4096:8 /home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/run_factor_control.py --cases two_outliers_alternating quadrant_alternating quadrant_pairs quadrant_center_edges equal_mixed_odd --orders 1 3 7 --factor-seeds SEED --level LEVEL --device DEVICE --batch-seconds 900 --out FRESH_OUTPUT_DIRECTORY
```

Run (SEED,DEVICE)=(20260924,cuda:0) and (20260925,cuda:1), each at LEVEL 0 and 1.
The completed outputs are in data/generated/neural_response_memory_20260922/
factor_control01. Every cell retains its exact command, data/source/array
hashes, precision, software/device settings, final factors and weights,
8192-node function, loss/time trace, and status. Existing paths are refused.

Regenerate the existing campaign analysis with:

```text
OPENBLAS_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/analyze_factor_control.py
OPENBLAS_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/check_factor_control_endpoints.py --device cpu --compare-analysis
```

Plots in factor_analysis01 are rms_vs_rank.png/pdf and
endpoint_functions_P3.png/pdf, endpoint_functions_P7.png/pdf. The primary
metrics.json SHA256 is
2d11a1d0e80ba61a064c5db8381601de609472f7bf49b131684c07dc3f39b54c.
No further training, promotion or Git write is part of this completed control.
