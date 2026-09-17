# Shifted XOR comparison through T=100

The bias-free wide network learns the shifted XOR task, and hidden-layer training
substantially improves its loss over the matched frozen-feature control. The
computed closures reach similar small endpoint losses, but lag the actual network
during its rapid learning phase and have appreciable Gram errors. Their quadrature
checks remain unresolved, so these calculations do not isolate closure-order error
from numerical integration of the population laws.

All eight GPU networks and eight closures completed the declared T=100 run in
269.8 seconds of scientific wall time. No horizon extension or extra training
campaign was run. Sources remain flat in this new study; all products are under
[run_001](../../data/generated/xor_network_closure/run_001/).

## Inputs and what this tests

The user chose to retain the established model and avoid same-label antipodes.
The centers are **0° (+1), 90° (−1), 150° (+1), 240° (−1)**. Each has four
deterministic offsets −5°, −5/3°, +5/3°, +5°, with equal training weights 1/16.
Thus there are 16 training inputs, with a separate passive 128-point circle.
The normalized directions u have unit norm; physical inputs are x=√2 u.

![Inputs and final predictions](../../data/generated/xor_network_closure/run_001/figures/geometry_and_final_predictions.png)

The original exact-antipodal layout conflicts with the identity f(−u)=−f(u) of
bias-free tanh networks. The new same-label arcs remain at least 20° away from
that conflict. They are still not linearly separable: the segments joining the
two positive and two negative pole means intersect internally, at segment
fractions approximately 0.634 and 0.366. Because each mean is a convex combination
of its four training inputs, the two class convex hulls intersect.

An explicit parity-compatible nonlinear separator on the circle is
s(θ)=cos θ+sin θ/√3+(1+1/√3)sin(3θ). It takes values +1,−1,+1,−1 at the four
centers. Its derivative has magnitude at most 4+4/√3, so its signed margin on
every ±5° arc is at least 1−(4+4/√3)π/36 > 0.449. This certifies a coherent
nonlinear target; it is not supplied to any training or closure calculation.
The [input record](../../data/generated/xor_network_closure/run_001/inputs.json)
retains the exact working arrays and geometry checks.

The network has two hidden tanh layers without biases, ordinary independent
Gaussian initialization in the maintained scaled convention, unhalved MSE and
physical mobilities (n,1,n). Widths are 2048 and 8192 with three seeds each,
plus time-step and precision controls. Closures use orders N=1,3,5 at two
quadrature resolutions each and two time-step controls. See the
[predeclared plan](EXPERIMENT_PLAN.md) for all configurations and thresholds.

## Learning and prediction accuracy

The width8192 three-seed mean terminal loss is **0.00273069**, with individual
losses between 0.00271864 and 0.00273766. The width2048 mean is 0.00268104.
Freezing both hidden layers and training only the readout with the same physical
mobility gives width8192 mean loss **0.389982**. Full training therefore has
about **143 times smaller loss** at this horizon. This supports the declared
hidden-training advantage against this matched control. It does not prove an
advantage over every possible frozen-feature method or optimizer.

The readout-only baseline is solved exactly at the working-matrix level using
f(t)=y+exp(−2tK/16)(f(0)−y), K=G2(0) on training inputs. Its kernel and initial
predictions come from each actual network initialization. It is not a full
frozen tangent-kernel model, and no closure trajectory is fitted to network data.

![Loss and Gram errors](../../data/generated/xor_network_closure/run_001/figures/loss_and_gram_errors.png)

At each width the Gram reference averages the three seeded network matrices
before taking errors. Gℓ(a,b)=hℓ(ua)·hℓ(ub)/n, and matrix RMS error is
||Gclosure−mean Gnetwork||F/m, with m=16 on training and m=128 on the passive
circle. Loss averages the individual network losses, not the residual of the
mean prediction.

| At T=100 | Training MSE | Training G1 error | Training G2 error |
|---|---:|---:|---:|
| Actual width8192 mean | 0.002731 | — | — |
| N1, Q2048/P1024 | 0.003811 | 0.04404 | 0.20724 |
| N3, Q2048/P1024 | 0.004178 | 0.04256 | 0.13432 |
| N5, Q2048/P1024 | 0.003774 | 0.03014 | 0.11496 |
| N5, Q4096/P2048 | 0.003638 | 0.04484 | 0.10847 |
| Frozen initial actual Gram | — | 0.19382 | 0.17323 |

Endpoint losses conceal a substantial timing discrepancy. At t=10 the actual
network mean loss is 0.2663 versus 0.6244 for the finer N5 closure. Their largest
absolute loss discrepancy is 0.4287 at t=12. The finer N5 maximum training G1
error is 0.1048, exceeding its endpoint error; its maximum G2 error is 0.1085.
It does not meet the declared whole-trajectory loss/Gram agreement criteria.

The changing Grams are nontrivial: the frozen-initial-Gram errors reach 0.1938
and 0.1732 on training. Actual activation movement RMS reaches 0.4511 and 0.5392.
N1 eventually predicts the second-layer Gram worse than freezing it. At common
base quadrature, N=1→3→5 reduces both maximum training Gram errors, but quadrature
refinement is not uniformly beneficial. Finer N5 passive-circle endpoint Gram
errors are 0.04058 and 0.10859.

The two matrix-evolution figures show [layer 1](../../data/generated/xor_network_closure/run_001/figures/layer1_gram_evolution.png)
and [layer 2](../../data/generated/xor_network_closure/run_001/figures/layer2_gram_evolution.png)
at t=0,10,40,100 on the passive circle: top actual network mean, middle finer N5,
bottom closure minus actual. The loss plot's solid black curve is the actual
width8192 mean; dashed black is the frozen-feature trained-readout baseline.
In the Gram panels, dashed black instead denotes the frozen-initial-Gram error.

## Checks and reproducibility

All 16 runs pass saved-array validity checks. Time and precision controls pass
the 0.002 diagnostic cutoff: worst network time-step discrepancy 0.00007951,
precision 0.00001003, and closure time-step discrepancies below 0.00000127.
Quadrature discrepancies reach 0.03046, 0.06866 and 0.08126 for N1,N3,N5;
all three remain unresolved. The law and horizon are exploratory, with no
asserted applicability of the maintained convergence theorem.

The CPU and GPU finite-equation checks each passed 29 comparisons, including
maintained RHS, autograd, simultaneous Heun and observation identities. Closure
observation and exact restart checks passed. A separate raw-array calculation,
[independent_check.json](../../data/generated/xor_network_closure/run_001/independent_check.json),
recomputes all Gram comparisons and uses a matrix exponential instead of the
analysis's eigendecomposition for the frozen-readout control. The
[final verification](../../data/generated/xor_network_closure/run_001/final_verification.json)
compares both calculations and validates source, input, output and figure hashes.
These are internal finite numerical checks, not promotion reviews or a hierarchy
convergence result. No prior study supplied code, data or research findings.

Reproduce in a fresh output directory using PREPARE.py --prepare, the NETWORK.py,
CLOSURE.py and ANALYSIS.py --verify modes, PREPARE.py --freeze, SUPERVISE.py,
ANALYSIS.py, CHECK.py, then PLOTS.py. Each accepts --output; runner verification
directories must be fresh and live under this study's generated checks namespace.
Use the recorded Python environment and GPU settings. The frozen plan, manifest,
worker records and supervisor retain exact commands, seeds, dependencies and hashes.
The 201 saved times include full Grams and predictions; endpoint checkpoints are
retained. All scientific work authorized by this plan is complete.
