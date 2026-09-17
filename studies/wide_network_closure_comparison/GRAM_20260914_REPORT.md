# Hidden-activation Gram evolution: actual wide networks and observable closures

The full hidden Gram comparison supports the earlier scalar comparison on these
data: increasing the computed closure order from N=1 to N=3 to N=5 decreases the
maximum saved-time matrix RMS discrepancy in all eight combinations of data case,
hidden layer and evaluation panel. This holds separately for the Gram itself and
its change from initialization, at both tested widths. The N=5 discrepancies from
the width-8192 three-seed mean are at most **0.013055 for G** and **0.015735 for
DeltaG**. The second layer remains sensitive to closure quadrature, so the full
numerical-resolution criterion is unresolved. This is checked empirical evidence
for the stated finite comparisons; it is not a population-limit theorem.

The user explicitly continued this study and confirmed the input-index hidden
activation Gram. The [frozen plan](GRAM_20260914_PLAN.md) preceded implementation
and training. All 16 original network trajectories and eight original closure
trajectories were replayed, with two additional declared closure time-step controls.
Every one of the 24 replays reproduces all earlier saved scalar/prediction values
with maximum numerical difference **zero**. The two new controls also completed.
No earlier experimental arrays or reports were overwritten.

For layer l, let H_l(t) have one row per hidden neuron and one column per input.
The new observable is

\[
 G_{\ell,n}(t;a,b)
 =\frac1n\sum_{i=1}^n h^\ell_{n,i}(t,u_a)h^\ell_{n,i}(t,u_b),
 \qquad
 G_{\ell,N}(t;a,b)
 =\sum_j p_{\ell,j}\,h^\ell_{N,j}(t,u_a)h^\ell_{N,j}(t,u_b).
\]

Here p_{l,j} are the closure's population integration weights. Training-input
weights p_a do not enter individual Gram entries. These are uncentered activation
products, not correlation coefficients, weight Grams or coefficient-state matrices.
Each complete stored matrix uses the training inputs followed by all 128 original
circle directions, without deduplication: 130 by 130 for the two-axis case and
144 by 144 for the 16-arc case. Both hidden layers are saved at all 206 original
observation times through physical time T=40. Thus the data include the
training-to-circle cross blocks as well as the two diagonal panel blocks used
for the declared error metrics.

The previous raw RMS satisfies

\[
 R_{\ell,n}(t)^2=\sum_a p_a G_{\ell,n}(t;a,a).
\]

It only retains a weighted diagonal average. The old files stored that and other
scalar moments, but no activation or weight trajectories, so their off-diagonal
Gram entries could not be recovered. Replaying training was necessary. Future
same-time Gram analyses on these saved panels can now use the new arrays directly.
They do not recover raw neurons, arbitrary new inputs or general cross-time Grams.

We also compare DeltaG_l(t)=G_l(t)-G_l(0), subtracting each method's own
initialization. This tests evolution beyond static initialization agreement.
It is different from the displacement Gram formed from h_l(t)-h_l(0), which
would additionally require current-to-initial cross-input products.

The model, initialization and clock are exactly those of the
[original report](WIDE_GPU_20260914_REPORT.md): a dense, bias-free,
two-hidden-layer tanh network, normalized inputs u=x/sqrt(2), weighted unhalved
squared loss, mobilities (n,1,n), Gaussian initial W1, B and small readout c with
entry variances 1, 1/n and 1/n^2, and f=c^T h2/n. Finite Heun integration uses
h=.01; the same initialization is used for h=.005 and float64 controls. Closures
use the unchanged maintained equations and initialization, orders 1/3/5,
Q=1024 and P=512, h=.005, and the original order-dependent ridges. N=3 controls
double Q/P or halve h separately. Gram accumulation is float64 for all runs,
independently of the training dtype. Passive observations do not feed evolution.

The main table gives

\[
 E_{\ell,N}=\max_{t\in\mathcal T}
 \left[\sum_{a,b}q_aq_b
 \left(G_{\ell,N}(t;a,b)-\overline G_{\ell,8192}(t;a,b)\right)^2\right]^{1/2},
\]

and the analogous error for DeltaG. The reference is the arithmetic mean of the
three seeds 11, 29 and 47. q is the training probability vector or uniform 1/128
on the circle. These are absolute matrix RMS errors, not percentages or maximum
entry errors; the time maximum is over saved observations, not a certified
continuous-time supremum. Time integrals, individual seeds, entry errors and
relative errors are retained in the linked results.

| Data | Layer | Panel | G: N1 | G: N3 | G: N5 | DeltaG: N1 | DeltaG: N3 | DeltaG: N5 |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| 2 axes | 1 | Training | 0.012342 | 0.008642 | 0.005525 | 0.011710 | 0.007805 | 0.004357 |
| 2 axes | 1 | Circle | 0.008689 | 0.006365 | 0.004356 | 0.008455 | 0.005977 | 0.003516 |
| 2 axes | 2 | Training | 0.060917 | 0.028806 | 0.012758 | 0.069793 | 0.028386 | 0.015077 |
| 2 axes | 2 | Circle | 0.048365 | 0.022371 | 0.008613 | 0.052816 | 0.022002 | 0.011219 |
| 16 arcs | 1 | Training | 0.011584 | 0.008105 | 0.005218 | 0.010987 | 0.007290 | 0.004027 |
| 16 arcs | 1 | Circle | 0.008154 | 0.005998 | 0.004187 | 0.007906 | 0.005587 | 0.003271 |
| 16 arcs | 2 | Training | 0.061332 | 0.028795 | 0.013055 | 0.070709 | 0.028701 | 0.015735 |
| 16 arcs | 2 | Circle | 0.048615 | 0.022539 | 0.008946 | 0.053592 | 0.022335 | 0.012008 |

The feature geometry changes substantially. In the 16-input case the maximum
matrix RMS size of the network's own DeltaG is 0.191629 in layer 1 and 0.358315
in layer 2 on training inputs; on the circle it is 0.153024 and 0.285934.
Consequently, the small N=5 discrepancy is not explained by almost-static Grams.
At t=40, N=5's relative DeltaG errors on the 16 training inputs are 1.57% and
4.39% for the two layers. Relative error is larger during early, very small
movement: the maximum saved-time relative DeltaG error is about 50%, across the
eight panels. Undefined ratios at zero movement are omitted, not set to zero.
The terminal percentages must not be read as uniform-in-time relative guarantees.

![Layer 2 Gram evolution on the circle, trained on 16 arcs](../../data/generated/wide_network_closure_comparison/GRAM_20260914_v1/figures/arcs_layer2_gram_evolution.png)

Rows are the network seed mean, N=5 closure, and their signed difference. The
first two rows share their color scale; the last has a smaller scale to expose
the error. Columns are t=0,1,5,40. The [layer 1 matrix figure](../../data/generated/wide_network_closure_comparison/GRAM_20260914_v1/figures/arcs_layer1_gram_evolution.png)
and both corresponding axis-case figures are in the same figures directory.

![Full Gram discrepancy curves](../../data/generated/wide_network_closure_comparison/GRAM_20260914_v1/figures/gram_errors.png)

![Gram increment discrepancy and frozen-initial baseline](../../data/generated/wide_network_closure_comparison/GRAM_20260914_v1/figures/gram_increment_errors.png)

The dashed baseline is the error incurred by freezing the network Gram at its
initial value. Early times are expanded on the horizontal axis. Increasing order
improves the declared maximum RMS metric in every panel, but this does not assert
that every entry, every instant or every relative metric improves monotonically.
Against individual width-8192 seeds, the largest N=5 primary error over both
observables and all panels is 0.016300. Comparing the two width means changes
G/DeltaG by at most 0.006309; pairwise seed differences at width8192 reach
0.006817. Three seeds and two widths are not certified uncertainty intervals
or identification of the infinite-width limit.

The numerical controls below take the largest primary error across both cases,
both panels and G/DeltaG within each layer. The frozen diagnostic cutoff is 0.002.

| Control | Layer 1 | Layer 2 |
|---|---:|---:|
| Network h=.01 versus .005, width8192 seed11 | 0.00004589 | 0.00016028 |
| Network float32 versus float64, width2048 seed11 | 0.00002007 | 0.00002203 |
| Closure N3 h=.005 versus .0025 | 0.00000039 | 0.00000068 |
| Closure N3 doubled Q/P | 0.00161271 | 0.00521215 |

The network precision/time controls and closure time control pass comfortably.
Layer 1 passes the declared diagnostic gate; layer 2 fails its quadrature gate.
The order improvements are numerically attributable under the plan's diagnostic
rule in four of eight panels, separately for G and DeltaG at width8192. N3
controls are diagnostics, not error bounds for N5. Thus the computed higher-order
trend is clear, while a fully resolved claim about the ideal closure remains open.

The 16-input task used **simple labels**, not a complicated target. Eight unit
directions within about five degrees of the first axis have target +1; eight
near the second axis have target -1. All training weights are 1/16. This is
squared-loss fitting to binary-valued regression targets, with labels separated
by sign(u1-u2); the minimum margin for the unit separator (1,-1)/sqrt(2) is
0.642651. There is no label variation within either cluster. The 128-circle panel
is passive and includes directions away from training inputs, but has no separate
ground-truth labels and is not a classification generalization benchmark.

![Exact 16-input labels](../../data/generated/wide_network_closure_comparison/GRAM_20260914_v1/figures/arcs16_training_labels.png)

The original two-axis precision-collapse and exploratory resolved-arc scope
remain in force. Matching the original data preserved a controlled comparison,
but did not establish performance on complex labels. No difficult-label campaign
was added to this experiment.

The complete [comparison JSON](../../data/generated/wide_network_closure_comparison/GRAM_20260914_v1/gram_comparison.json)
and nine CSV tables contain all comparisons, controls, replay checks and matrix
validation. Every Gram is finite and symmetric, satisfies the bounded-entry and
weighted-diagonal/RMS checks, and passes positive-semidefiniteness inspection
within roundoff at t=0,1,5,40. The largest diagonal/RMS-squared discrepancy is
1.074e-7 in float32 training. The observation formulas were checked against
explicit entrywise products, weighted population sums and neuron permutations
before trajectories. A separate [raw-array spot check](GRAM_20260914_SPOTCHECK.py)
recomputes the arc-case metrics without importing the analyzer. These are internal
checks of this finite experiment, not promotion reviews.

Sources remain flat in this study. [Preparation](GRAM_20260914_PREPARE.py),
[GPU replay](GRAM_20260914_NETWORK.py), [closure replay](GRAM_20260914_CLOSURE.py),
[analysis](GRAM_20260914_ANALYSIS.py), and [figures](GRAM_20260914_PLOTS.py) are
retained with hashes in execution records. The original literal input
specification and original scalar arrays remain this study's own replay inputs.
No other study is a live reproduction dependency. Scientific producer sources
were unchanged during execution; the final checks also verify their hashes.

GPU runs used two RTX3090 24-GiB cards, CUDA 13.0, PyTorch 2.9.0+cu130,
Python 3.10.14 and NumPy 1.26.4, with TF32 disabled and at most four CPU threads
per network. Closures used Python 3.10.12/NumPy 1.26.4 with one numerical thread.
The GPU supervisor completed in 244.02 seconds, with 464.91 aggregate worker
seconds; the closure workers took 215.70 seconds in total. All fixed-menu runs
finished within the declared resource limits, without failure or extra branches.
The [final verification](../../data/generated/wide_network_closure_comparison/GRAM_20260914_v1/gram_verification.json)
records source/product preservation, validation and resource checks.

For reproduction, choose a fresh GRAM_* directory immediately before starting
the scientific workers. Preparation starts the shared 2400-second clock. From
the repository root, use the following recipe; the two campaigns may run
concurrently. The environment must expose both GPU devices.

```bash
GRAM_REPLAY_RUN=data/generated/wide_network_closure_comparison/GRAM_fresh_replay
PYTHONDONTWRITEBYTECODE=1 /usr/bin/python studies/wide_network_closure_comparison/GRAM_20260914_PREPARE.py --output "$GRAM_REPLAY_RUN"
CUDA_VISIBLE_DEVICES=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 /home/amir/miniconda3/bin/python studies/wide_network_closure_comparison/GRAM_20260914_NETWORK.py --output "$GRAM_REPLAY_RUN" --campaign
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 /usr/bin/python studies/wide_network_closure_comparison/GRAM_20260914_CLOSURE.py --output "$GRAM_REPLAY_RUN" --run
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 /home/amir/miniconda3/bin/python studies/wide_network_closure_comparison/GRAM_20260914_ANALYSIS.py --output "$GRAM_REPLAY_RUN"
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 /home/amir/miniconda3/bin/python studies/wide_network_closure_comparison/GRAM_20260914_PLOTS.py --output "$GRAM_REPLAY_RUN"
```

Existing completed run directories are evidence, not reproduction destinations.
This bounded campaign is complete. The remaining scientific gaps are complex
targets, resolved N5 quadrature and larger width/seed coverage; they were not
silently added to the run menu. Root owns the report, figures and shared README;
scoped collaborators implemented closure observations and analysis and performed
the separate metric cross-check. No established book or maintained API was changed.
