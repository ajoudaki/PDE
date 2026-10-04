# Frozen second-stage test: is generic low-rank compression sufficient?

Frozen before new training outputs, 2026-10-02. This protocol continues the
controlled-response-memory investigation. It does not alter the candidate or
first-pilot gates. Its purpose is to reject an overinterpretation of that
pilot if a stronger generic compression method explains the same decision
quality. No adaptation of the menu, thresholds, data, rank, order or seed
after seeing outputs is allowed. Implementation bugs can be repaired with a
dated explanation before restarting within the same aggregate budget.

## Data, network and checkpoint

Use the locally installed sklearn load_digits dataset, real 8x8 handwritten
digit images, classes 3 and 8 only. Record the raw arrays' hash, package
version and exact indices. The data description identifies it as the UCI
Optical Recognition of Handwritten Digits test collection. Dataset access is
local; no other study is an input. Use NumPy default_rng seed 20261003 to
shuffle each class's indices separately in ascending class order. Per class,
the first 4 images are old training, next 4 new training, next 64 old
validation, next 64 new validation. Rotate new images by 90 degrees using
np.rot90. Flatten and scale each image to Euclidean norm sqrt(64), without
centering. Labels are -1 for 3 and +1 for 8. Reorder the 16 training images
as 8 old followed by 8 new; queries are 128 old followed by 128 new, all
disjoint from training and each other. This is domain adaptation with a
small fixed training list, not a claim about image-classification benchmarks.

The network has two tanh hidden layers of width n=512 and input d=64:
h1=tanh(W1 x/sqrt(d)), h2=tanh(W2 h1), f=w^T h2/n. Initial entries of W1
are standard Gaussian and of W2 Gaussian with variance 1/n; w=0. Use torch
CPU generator seed 20261003 and float64. Canonical gradient-flow mobilities
are (n,1,n) for (W1,W2,w), with mean squared error. Pretrain only old data
with unit weights until MSE <=0.001 or time 80; if not fitted, stop and report
the gate failed. The actual shared endpoint is the checkpoint for all trials.

## Fixed controls and decision

Continue to physical time T=24 with weights u_old=2 lambda(t) and
u_new=2[1-lambda(t)]. The finite menu, with tie order as listed, is:

1. P2: on each 12-unit half, mean lambda is 0.15 then 0.35, plus a square
   burst of amplitude 0.1 with 2 periods per half, positive first.
2. P32: the same envelope and amplitude, 32 periods per half.
3. NP: the same envelope and amplitude; divide each half into 8 equal bins;
   burst signs in the first half are [+,+,+,-,-,+,-,-], and in the second
   half are the reversed sequence. This is not a periodic square wave.
4. SAFE: constant lambda=0.65.

The first three have identical old/new exposure in each half. SAFE deliberately
changes exposure and is available to every method. It is a candidate, not
assumed feasible. The average-schedule predictor uses the dense continuation
of the burst-free envelope for P2/P32/NP and the dense SAFE continuation for
SAFE. The controls themselves are stored explicitly and every switch is
resolved. No averaging baseline uses outcomes of a switched dense policy.

For each policy define C as the maximum over the fixed observation grid of
old-validation RMS function drift from the checkpoint. Define J as trapezoid
time-average new-validation RMSE against labels over [0,24]. The retention
threshold is **c=0.25**, a quarter of the unit label magnitude. Each method
selects the first minimizer of its J among its predicted C<=0.25; no feasible
policy means abstention. The dense fine-resolution menu defines the empirical
oracle. Evaluate every selected policy by its dense fine-resolution outcome.
The threshold is empirical and has no theorem-based safety margin.

## Models and a strong storage-matched competitor

Dense canonical flow is ground truth up to its reported discretization error.
Response memory uses q=3, endogenous weighted-residual clock, constant forward
and zero backward prefixes, and the exact outer-block updates from the frozen
candidate. Checkpoint NTK contains all parameter blocks and canonical
mobilities; integrate its controlled linear ODE by matrix exponentials.

The competitor stores a low-rank **increment around the same dense checkpoint**,
W2=W2_c+U diag(s) V^T, with orthonormal U,V, initially rank zero. It receives
the full current gradient update evaluated in its own reconstructed network.
At each Heun predictor and corrector, take the best rank-r truncated SVD of
the increment plus the low-rank gradient increment. Do this online through
thin QR of concatenated factors followed by the small-core SVD; do not form
a full dense increment or train factors by Euclidean gradient descent. The
predictor uses Y+dt G(Y); the corrected increment uses
Y+dt/2[G(Y)+G(Y_predictor)], truncating each to rank r. The outer W1,w blocks
use the same Heun stages. This is an online truncated-SVD/retraction method;
no second-order convergence assertion for its constrained flow is presumed.

The q=3 moving hidden arrays contain 2mnq=49,152 scalars. Grant the competitor
r=floor(49,152/(2n+1))=47, so U,V,s use 48,175 scalars. Both also store identical
outer blocks and the shared fixed dense W2_c. Count its thin-QR/SVD workspace,
memory diagnostics, baseline checkpoint and observed CUDA peak separately.
There is no factor-training or fixed-subspace restriction. Validate the
incremental SVD against explicit dense SVD on small matrices and show that
an uncapped update agrees with dense Heun before running training.

## Numerical resolution and hard budget

Use fixed-step float64 Heun with dt<=1/64 and refine to dt<=1/128, clipping
all steps to switches and observations. Common observations are every 1/16
time unit plus every event of any menu policy, identical for every method.
Pretraining uses dt<=1/128 and ends on the first grid step reaching its fit
threshold; its endpoint is a definition, not an approximation to a required
hitting time. Record first-layer RMS feature motion on training data relative
to this checkpoint for both dense and memory. Accumulate the memory histories'
projection-error energies, including the prefix, as in the first pilot.

At most 27 trained trajectories: one pretrain; four policies times three
models (dense, q3, SVD47) times two resolutions =24; and two dense envelope
runs. NTK predictions are not training but all elapsed process time counts
toward the **1200-second GPU-process cap**. GPU0 only. Stop and retain partial
outputs when the time or count cap is reached. No extra seeds or rank sweeps
in this stage. CUDA synchronization brackets runtimes. Report all failures,
runtime, actual allocator peaks and analytic persistent-state counts.

## Frozen interpretation and stopping rules

1. Numerical validity requires every dense/q3/SVD47/envelope coarse-fine
   maximum prediction RMS difference <=0.003. No passing claim if incomplete.
2. A nontrivial decision menu requires at least one dense policy with C<=0.23,
   at least one with C>=0.27, and dense J range >=0.03. Otherwise the proposed
   retention-selection discriminator is inconclusive; do not tune c.
3. A same-policy mechanism witness requires q3 prediction discrepancy <=0.02
   against dense throughout saved times, terminal relative credit-history
   projection error >=0.30, and first-layer motion >=0.10 in **both** dense
   and q3 on that policy. Credit and accuracy must refer to the same q=3 run.
4. Memory decision usefulness requires its selected policy to have dense
   C<=0.25 and J regret <=0.02 versus the dense feasible oracle. To claim a
   distinctive advantage over generic low rank, SVD47 must either select a
   policy with dense C>=0.27, incur regret >=0.05, or abstain when q3 succeeds.
   All decision claims also require conditions 1 and 2. NTK and averaging are
   reported with identical selection rules regardless of result.
5. If SVD47 matches or beats q3 on decision quality and its maximum trajectory
   discrepancy is <=0.02 on every policy, generic low-rank compression remains
   a sufficient explanation of this instance. Stop expansion; do not rescue
   the candidate by lowering its rank or tuning a harder instance after output.
6. Even if q3 is distinctive, report whether its storage buys a plausible
   planning niche after shared source and workspace. If measured runtime is
   worse than dense and same-storage SVD with no observed resource advantage,
   do not claim efficient planning. Concurrency capacity inferred from array
   counts is hypothetical unless actually measured. No extra concurrency
   experiment is part of this gate.

These are bounded empirical gates, not general falsification of the reviewed
theorem. The desirable outcome is an honest distinction among mechanism,
compression, decision utility and computational cost.

## Sources and scope

Scientific sources: the frozen CONTROL_CANDIDATE.md (including its recorded
primary literature), CONTROL_PROOF_REVIEW.md, CONTROL_PILOT_REPORT.md and own
control_pilot.py. New data: locally installed sklearn load_digits, originating
from UCI Optical Recognition of Handwritten Digits. The competitor is the
explicit algorithm above, not a claim to have exactly implemented DLRT.
No other study, external agent draft, held-out new run or pilot from another
direction is an input. Code/source/data hashes will be saved before execution.
