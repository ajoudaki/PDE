# Strong low-rank competitor explains the control pilot's accuracy

The stronger test does **not** establish a distinctive planning advantage for
paired response histories. On a fresh real-image adaptation problem, order-3
memory predicts nonlinear training accurately while its credit history is
poorly reconstructed and its recorded first-layer features move substantially.
But a storage-matched online truncated-SVD increment predicts every dense
trajectory considerably more closely. All five decision methods, including
the frozen kernel and averaged schedule, select the same policy. The frozen
decision-discriminator gate also fails because the menu's objective spread is
too small. The appropriate decision is to stop this practical control route
at this gate, without changing thresholds or searching for a rescuing task.

All 27 preregistered trained trajectories completed without failure in
487.247 seconds (8.12 minutes) of the 1200-second process allowance. GPU 0 was
released. No extra rank, seed, policy or dataset runs followed the result.
The possible two additional diagnostic runs discussed during execution were
not used. The original candidate and stage-two preregistration remain frozen.

## What changed from the first pilot

The new seed is 20261003. The data are locally installed sklearn digits 3 and
8, with ordinary images as the old domain and 90-degree rotated images as the
new domain. There are eight training examples per domain and 128 disjoint
validation examples per domain. Exact indices, raw-array hash and package
version are in `dataset.json`; the underlying 8x8 handwritten digit collection
is due to E. Alpaydin and C. Kaynak, 1998
([primary UCI dataset page](https://archive.ics.uci.edu/dataset/80/optical%2Brecognition%2Bof%2Bhandwritten%2Bdigits)).
This small fixed-list problem exercises the mechanism; it is not an image
classification benchmark result or evidence for broad continual-learning gains.

Both tanh hidden layers have width 512. All parameter blocks learn with the
paper's canonical mobilities. Old-only pretraining reaches MSE
0.000999262 after 1644 steps of length 1/128 (time 12.84375). Every trial
starts from that same physical checkpoint and continues for time 24.

The storage-matched competitor evolves

\[
W^{(2)}=W_c^{(2)}+U\operatorname{diag}(s)V^\top,
\]

where the columns of U and V are orthonormal and at most 47 singular values
are retained. At each Heun stage it receives the actual full current gradient
increment, then takes its best rank-47 SVD through thin QR and a small-core
SVD. Its outer parameter blocks learn too. It starts at rank zero and changes
its subspaces online. Thus this is neither factor-gradient training, a fixed
subspace, nor an endpoint low-rank fit to a dense trajectory. The moment
method's hidden correction has rank at most mq=48; a rank-47 online competitor
uses slightly fewer persistent scalars once singular values are included.

## Frozen decision and its outcome

The two periodic policies P2/P32 and the nonperiodic NP policy share the same
old/new exposure on each 12-unit half. They differ in the switching pattern.
SAFE is the fixed old-replay fraction 0.65 and was not assumed feasible.
Every model predicts all four policies. It chooses the smallest predicted
time-average new-validation RMSE, J, among policies whose maximum saved-time
old-function RMS drift, C, is at most the frozen threshold 0.25. There are
385 common observation times, including every switch. These are empirical
saved-grid objectives, not continuously certified maxima.

| Policy | Dense C | Dense J | Feasible at C <= 0.25? |
|---|---:|---:|---|
| P2 | 0.291939 | 0.545851 | No |
| P32 | 0.274119 | 0.544270 | No |
| NP | 0.279116 | 0.545959 | No |
| SAFE | 0.214771 | 0.569210 | Yes |

Dense, q3 memory, SVD47, checkpoint NTK and the dense averaged-schedule
predictor all identify SAFE as their only feasible policy and select it.
Their selected policy consequently has the same dense retention and zero
regret against this finite dense menu. This is an actual computed selection,
but it exhibits no method-dependent improvement. A method with a noticeably
less accurate trajectory can still make the same coarse decision.

The frozen nontrivial-menu gate required a feasible policy with C<=0.23,
an infeasible policy with C>=0.27, and J spread at least 0.03. The first two
conditions pass; the spread is only **0.0249402**, so the combined gate fails.
The small discrepancy from the threshold does not justify rounding it into
a pass. There is also only one feasible policy, so this instance does not
assess ranking among competing feasible actions. No post hoc retention or
objective threshold was substituted.

![Dense outcomes of the frozen menu](/home/amir/Codes/PDE/data/generated/response_memory_frontiers_20261002/control_stage2_20261002/menu_decision.png)

## Prediction and mechanism evidence

The table gives maximum saved-time RMS prediction discrepancy over all 256
passive images against the dense trajectory with the same fine time step.

| Policy | Memory q3 | Online SVD47 | Checkpoint NTK | Dense average schedule |
|---|---:|---:|---:|---:|
| P2 | 0.00055337 | 2.4941e-7 | 0.21411 | 0.035982 |
| P32 | 0.00054065 | 2.2634e-7 | 0.22390 | 0.032527 |
| NP | 0.00051763 | 2.4029e-7 | 0.21072 | 0.035982 |
| SAFE | 0.00037820 | 1.4314e-7 | 0.16965 | 0 |

The averaged predictor for SAFE is that very policy, explaining its zero.
The first three averaged predictors all use one dense burst-free envelope.
The very small SVD discrepancies quantify agreement with the same-step dense
discretization. They are **not** absolute errors against exact continuous
gradient flow; the dense refinement sensitivity is larger, as reported below.

![Discrepancy from the dense fine-step trajectory](/home/amir/Codes/PDE/data/generated/response_memory_frontiers_20261002/control_stage2_20261002/trajectory_errors.png)

All four same-policy mechanism witnesses pass the frozen requirements:

| Policy | Dense first-layer motion | q3 first-layer motion | q3 credit-history error | q3 feature-history error |
|---|---:|---:|---:|---:|
| P2 | 0.33484 | 0.33503 | 0.41837 | 0.077205 |
| P32 | 0.33488 | 0.33506 | 0.41027 | 0.077578 |
| NP | 0.33436 | 0.33454 | 0.41253 | 0.076769 |
| SAFE | 0.33452 | 0.33468 | 0.32873 | 0.069985 |

Motion is the maximum RMS change of the actually compressed first-layer
features on training examples. Both history errors are terminal relative
L2 projection errors in the memory model's own residual clock, including its
prefix. Thus accurate q3 prediction, poor q3 credit reconstruction and feature
motion occur in the same run, fixing the logical weaknesses of the first
pilot's gates. The SAFE row also shows why poor credit reconstruction cannot
be attributed solely to switching: the zero-backward prefix creates a common
initial discontinuity. This experiment supports the paired-history mechanism
as an internal explanation of the closure, but does not make it uniquely
necessary for compressed prediction. The strong SVD competitor is sufficient.

## Numerical and code validation

Every dense, memory and SVD policy was run at step bounds 1/64 and 1/128,
as was the dense averaged envelope. All steps resolve all switches explicitly.
The maximum coarse/fine prediction changes are:

| Method | Largest change across its policies |
|---|---:|
| Dense | 0.000304444 |
| q3 | 0.000300340 |
| SVD47 | 0.000304444 |
| Dense average envelope | 0.000312438 |

All pass the frozen 0.003 gate. These are observed convergence diagnostics,
not validated numerical enclosures. They are small relative to the policy
constraint margins. In P2 the largest dense sensitivity occurs at time 0.25;
the largest memory discrepancy occurs at time 16.125, where dense sensitivity
is only 3.02e-6. Conversely, the SVD discrepancy lies below the reference's
numerical sensitivity, so claiming continuous-flow accuracy of order 1e-7
would be unjustified.

Before training, the QR/core implementation matched explicit dense truncated
SVD to 1.95e-14, and uncapped online SVD Heun matched dense Heun to 1.11e-16
on a small independently generated problem. Autograd verified all dense
canonical velocities to 5.55e-17. The reused exact product-defect check gives
4.86e-17; every velocity is zero under zero drive. The control exposure and
event-grid checks passed. An additional CPU autograd calculation checked all
checkpoint-kernel blocks to 6.66e-16 (seed 882, width 7, dimension 3, five
training and four query inputs). No GPU training was used for these checks.

The separate `control_stage2_figures.py` independently recomputes dense C and
J directly from saved arrays and agrees to machine precision. The source and
preregistration hashes saved before training were checked unchanged afterward.
There has not yet been a separate human or isolated-agent code audit of this
stage; an attempted delegation failed because the thread limit was exhausted.

## Cost does not establish a practical win

Persistent evolving counts include the trainable first layer and readout:

| Representation | Moving scalars | Moving MiB in float64 | Fixed hidden checkpoint MiB |
|---|---:|---:|---:|
| Dense branch | 295,424 | 2.25391 | No extra matrix required once branches are initialized |
| q3 branch | 82,433 | 0.628914 | 2 shared among branches |
| SVD47 branch | 81,455 | 0.621452 | 2 shared among branches |

The memory diagnostic accumulators add 64 scalars (0.000488 MiB). Input,
query, controller and checkpoint outer-block storage are separate common
costs. For four simultaneous branches, counting the shared hidden matrix
but not workspace, both compressed representations use about half the dense
persistent state. This is array arithmetic, not a measured concurrency gain.

| Method | Fine-run elapsed range | Measured peak CUDA allocated | Peak increase above entry allocation |
|---|---:|---:|---:|
| Dense | 2.85–3.02 s | 26.0967 MiB | 13.2661 MiB |
| q3 | 7.33–7.55 s | 15.9692 MiB | 4.7603 MiB |
| SVD47 | 67.31–72.12 s | 20.4731 MiB | 9.6426 MiB |

Peaks are allocator measurements for the actual sequential implementation,
including resident data/checkpoint and stage/query work arrays. The increase
includes low-rank state growth as well as temporary workspace, so it is not
an isolated workspace count. External driver/context allocations are outside
PyTorch's allocated-tensor counter. Thin QR/SVD workspace was not silently
excluded. CUDA synchronization brackets every reported run.

Memory is faster than this deliberately high-rank SVD implementation, but
SVD47 is far more accurate. A lower rank might already match q3 accuracy at
much lower cost. Therefore this table does not establish a memory speed
advantage at matched accuracy. Sequential dense rollouts are faster than
both compressed methods. No measured planning workload, concurrency benefit
or end-to-end resource bottleneck establishes a compelling practical niche.

## Status, sources and reproduction

The reviewed theorem is unaffected: at fixed finite width and horizon it
gives a control-uniform O(1/q) approximation using smoothness of the forward
factor without differentiating the credit history or control. Its possibly
large Gronwall constant is not converted into a useful certificate by these
data. The observed mechanism survives this stronger test; the proposed
distinctive control utility does not. The frozen generic-low-rank sufficiency
condition is true, and the stopping rule is followed.

This stage read its own frozen candidate, proof review, first-pilot report and
code, the required mathematical/research skills, local dataset metadata and
the primary UCI dataset page above. Earlier complete current-paper inputs and
targeted control/low-rank literature are recorded in CONTROL_CANDIDATE.md.
The first 180 lines of maintained `code/README.md` and targeted dataset-name
searches in maintained code and non-generated data were checked for input
availability; no maintained API was invoked or modified.
No other study's unpromoted findings were read or used. Proof clarifications
are in CONTROL_ADDENDUM.md; no maintained source was changed.

Frozen SHA256:

```text
c0b8662393ac1459319d01e75bf71a76493b278b1652f2576676485d8968ba7b CONTROL_STAGE2_PREREG.md
39b96ec6caf5d04dd1db2dcd3bf5f9951ec8fd9a05f8bf87bf103508620a8c88 control_stage2.py
cebe78cac01f339a1abb497982acc4a7ed678cf3ad429022e15c3b9a02acb78d CONTROL_CANDIDATE.md
```

The complete run is under
`data/generated/response_memory_frontiers_20261002/control_stage2_20261002/`.
It contains the frozen-source hashes, explicit control tables, dataset indices
and hash, checkpoint and terminal states, all prediction arrays, diagnostics,
timings, status, analysis and independently reduced dense decision metrics.
The sibling `control_stage2_20261002.log` records progress and completion.

```bash
env CUDA_VISIBLE_DEVICES=0 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
 /home/amir/miniconda3/bin/python -u \
 studies/response_memory_frontiers_20261002/control_stage2.py \
 --device cuda:0 --output <new-empty-run-directory>

/home/amir/miniconda3/bin/python \
 studies/response_memory_frontiers_20261002/control_stage2.py \
 --analyze-only --output data/generated/response_memory_frontiers_20261002/control_stage2_20261002

/home/amir/miniconda3/bin/python \
 studies/response_memory_frontiers_20261002/control_stage2_figures.py \
 data/generated/response_memory_frontiers_20261002/control_stage2_20261002
```

No further training is recommended within this control route on the current
evidence. Reopening it would require a new substantive reason beyond accurate
small-order prediction, which generic low-rank compression already explains
on this mechanism-preserving real-data instance.
