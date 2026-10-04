# New-seed confirmation and bounded scaling test

Frozen after training01/training02 inspection, before these new seeds or
widths are run. The original aggregate-metric ambiguity is acknowledged, not
retroactively repaired. No novelty for fast prescribed-spectrum matrices is
claimed: see LITERATURE_AUDIT.md. The question is whether such an environment
is useful for implementing the manuscript's own response-memory learner.

## Confirmation: unchanged learning question, larger width and fresh seeds

Use exactly the digits3/8 data and q=1 system in TRAINING_PROTOCOL.md,
physical horizon40, dt=.02, float32 without TF32. Width8192, seeds
7501,7502,7503,7504,7505, all four mixer laws:20 fits. Keep both hidden
training activations and all train/held-out predictions at the21 fixed times.

For each law first average over its five seeds. Compare with the Gaussian
ensemble mean using precisely these five distances:

1. RMS prediction difference over all21 times and all357 input examples.
2. RMS entrywise difference of first-layer training Gram matrices h h^T/n,
   over all21 times and all64x64 entries.
3. The corresponding second-layer Gram difference.
4. RMS difference over21 times of first-layer RMS feature displacement
   (displacement itself uses all357 inputs and n neurons).
5. The corresponding second-layer displacement difference.

Each metric is computed separately, never combined with fitted weights.
Report seed variability and individual-seed task performance. Primary pass:
quarter-circle is closer than BOTH alternatives on all five distances, and
its prediction distance is at most.01. At least4/5 quarter-circle runs must
move first-layer features by.03 RMS and improve held-out MSE at least5%
against their own exact fixed-feature readout atT40. Otherwise the result
is inconclusive or adverse as appropriate, with no new seed/spectrum search.
These thresholds are engineering gates, not confidence intervals or a
universality theorem. The data task and split are shared with the pilot;
this is fresh-initialization confirmation, not independent dataset validation.

## Scaling gate only after the first gate passes

Use width16384, same task and times, three fresh seeds7511,7512,7513,
Gaussian and quarter-circle:6 fits. Use TF32 for BOTH methods as a practical
matmul setting, with all fixed/learned state float32. Compare wall time for
complete training including saved-time evaluation and data transfer, report
setup/compilation separately, and disclose both persistent array counts
and measured peak allocated CUDA bytes. No inference about other hardware.

For seed7511 repeat both methods without TF32:2 additional fits. TF32 change
in maximum-over-time prediction RMS must be below.002. Repeat the two TF32
seed7511 runs in a fresh directory:2 additional fits, tolerance1e-6 RMS.
Reserve two half-step runs only if a validity threshold is approached.
Thus at most32 trained runs and30 GPU-process minutes, GPU1 only. Stop a
single run after5minutes; no OOM retry at a scientifically different width.

Computational benefit requires at least2x median warmed end-to-end speed and
at least2x lower measured peak allocated bytes. Both methods must still pass
the feature-learning gate. These criteria concern implementing the same class
of population learner efficiently; they do not establish improved task risk,
universality, or superiority to direct low-rank/other fast architectures.
If the gate passes, those remain necessary strong comparisons before a broad
architecture claim. Dense results from a narrower width must be reported as
a cheaper alternative when its accuracy already suffices.

Checks before large width: fast-Hadamard involution and adjoint checks at every
new width; finite states; compare exact source hashes; retain original source
and every failed/partial run. Use source snapshot fast_training_v2.py for the
old run; new optional precision/protocol arguments must not alter float32
dt=.02 dynamics. Statistical aggregation code is frozen before confirmation.

## Verification allowance, after the scientific result

Confirmation passed all five fixed metrics, and scaling met its thresholds.
Before labelling the five-seed empirical result internally reproduced, repeat
its exact20 trajectories in a fresh directory. This adds20 verification fits,
not new statistical replicates or parameter choices. Compare every saved
prediction and both training activation arrays at tolerance1e-6. The30-minute
wall budget remains ample; the first confirmation/scaling/precision/replay
campaign used under4minutes. A separate reviewer may independently rerun the
Gaussian and quarter-circle seed7501 cases on GPU0 (at most2 of its4 allowed
verification runs). These cross-device checks supplement the full reproduction.
