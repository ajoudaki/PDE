# Accuracy and cost for population trajectory observables

Frozen before the new campaign. This follows the specific unresolved question
in CONTRIBUTION_REVIEW.md, within the same fast-initializer study. It is not
a new architecture-performance benchmark or a search for a better dataset.

## Question and exact target

Does the fast Gaussian-spectrum q=1 learner estimate a wide-population
trajectory more cheaply than averaging independent narrower Gaussian learners?
Retain the existing digits3/8 split, exact normalization, tanh q=1 equations,
Heun dt=.02 through40, and21 saved times. All methods use float32 and TF32;
the existing IEEE/TF32 discrepancy check is documented separately.

Use two observable vectors: predictions on all357 examples at all21 times;
and the second-layer64x64 training Gram at all21 times. Each has its own
normalized Euclidean (RMS) norm. Do not select an observable after running.
The operational reference is the mean of32 independent fast width32768
trajectories, seeds8001--8032. This is a finite numerical reference, not a
certified exact infinite-width limit. Its sampling error and width stability
must be reported.

Candidate widths are512,2048,8192,16384, each with both Gaussian and fast
quarter-circle mixers and16 fresh seeds7601--7616. The two laws and widths
share seed labels for paired uncertainty accounting. Reference seeds are
separate. This is128 candidate fits plus32 reference fits. No fitting or
hyperparameter changes may follow the outcome within this campaign.

## Efficient producer and validity gates

The existing producer will gain an optional compact recording mode: compute
and save the two training feature Grams instead of full per-neuron activation
histories. The learning equations, schedule, predictions, frozen-feature
control, and feature-motion diagnostics remain exactly the same. Before the
campaign, two width8192 seed7501 IEEE cases (Gaussian and fast) must reproduce
the existing confirmation prediction arrays bitwise, and saved compact Grams
must agree with recomputation from the old retained activations within1e-6
maximum absolute discrepancy. Preserve the prechange producer as v4.

Every run retains data/config/source hashes, predictions, both feature Grams,
frozen trajectories, feature motion and the existing finite/action/adjoint/
graph oracles. Record complete per-trajectory time including construction,
graph setup, training, evaluation and NPZ serialization. Dataset loading and
process-level imports are shared campaign overhead and reported separately
through total process runtime, not charged once per averaged trajectory.
No classifier-accuracy advantage is being tested.

To balance hardware, GPU0 runs Gaussian seeds7601--7608 and fast7609--7616;
GPU1 runs fast7601--7608 and Gaussian7609--7616. Each GPU then runs16 reference
seeds. All four widths are covered by each candidate batch. No concurrent
jobs share a GPU. Ordinary GPU desktop allocation is recorded.

## Error curves and fixed decision rule

For each candidate law/width and observable, let X_i be its16 full trajectory
vectors, xbar their mean, rbar the independent reference mean, and

    V = sum_i ||X_i-xbar||_RMS^2 / 15.

For averaging K in {1,2,4,8,16} independent candidate trajectories, estimate
the expected squared reference error by

    E_K = ||xbar-rbar||_RMS^2 + (1/K-1/16) V.

This nonnegative statistic is unbiased, over candidate sampling with fixed
reference, for the mean-square error of a fresh K-run average relative to that
reference. It does not subtract finite-reference noise or certify population
bias. Its square root is the plotted RMS-error estimate. Cost is K times the
median complete trajectory time for that condition. All widths/K values are
shown, including dominated choices. Do not call any curve globally optimal.

The primary tolerance is.0025 RMS for EACH observable simultaneously. The
cheapest eligible fast condition must cost at most half the cheapest eligible
Gaussian condition. Uncertainty:1000 bootstrap draws, resampling candidate
seed labels jointly across widths/laws and reference seeds independently;
recompute the error curves and cheapest eligible cost in each draw. Require
the twofold advantage in at least90% of draws to pass the empirical decision
gate. Report the full ratio distribution, eligibility failures, and absolute
costs; this bootstrap fraction is not a rigorous confidence guarantee.

Reference-resolution gates: its estimated sampling RMS standard error must be
<=.0025/3 for both observables. Also, the fast width16384 candidate mean and
width32768 reference mean must differ by no more than twice the combined
sampling RMS standard error sqrt(V16384/16+V32768/32), for each observable.
This is a width-stability check, not a bound on unknown reference bias. Failure
of either gate blocks a claimed population-simulation accuracy--cost success;
do not increase width/seeds or change tolerance in response within this protocol.

Secondary tolerances.00125 and.005 may be plotted descriptively, without
replacing the primary decision. No full-spectrum-necessity or general-purpose
architecture claim follows from a pass.

## Resources and stop

Two producer-verification fits,128 candidate fits and32 reference fits, at
most20 GPU-process minutes and30 wall minutes. Stop on numerical/action
failure or a reference width32768 kernel resource failure; retain all partial
outputs and do not silently substitute a narrower reference. At most2 GB new
retained data is expected with compact diagnostics. No manuscript/shared-code/
Git-index writes, package installation or external compute.
