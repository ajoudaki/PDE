# Three hidden layers on the circle, width 4096

This continues the five circle tasks in `neural_response_memory_20260922`,
as explicitly requested. The architecture now has three tanh hidden layers
and two dense internal matrices. The width is 4096 in every hidden layer.
The derivation preceded the experiments; the frozen design is in
`DEEP_CIRCLE_PROTOCOL.md`. The completed reading and reconciliation of the
relevant earlier constructions and corrections is recorded in
`DEEP_CIRCLE_CONTEXT_DIGEST.md`.

The main finding is empirical: P=2 and P=3 both improve prediction agreement
with dense training over P=1 on all five tasks. P=2 is best on the two
alternating-label tasks; P=3 is best on the other three. The hierarchy is
therefore not monotone over these tested orders. This is one shared random
initialization, not an average over seeds or a convergence theorem.

## Closure for the deeper network

The physical network is

\[
h_1=\tanh(W_1U),\quad h_2=\tanh(W_2h_1),\quad
h_3=\tanh(W_3h_2),\quad f=c^Th_3/n.
\]

Here U is a unit-circle input, the loss is the unhalved mean squared error,
and the gradient-flow mobilities for `(W1,W2,W3,c)` are `(n,1,1,n)`.
The full proof, initialization, reverse responses, rational lift and
zero-residual boundary are in `DEEP_CIRCLE_DERIVATION.md`.

For each internal link ell=2,3, retain a distinct pair of P-mode history
arrays A and B. They represent the backward source and the incoming hidden
activation, respectively. All four arrays share the activity clock
`s_dot = rho`, where `rho = sqrt(mean(r^2))`, `r=f-y`, and `L=1+s`.
For sample a and mode k=0,...,P-1,

\[
\dot A_{\ell,k,a}=r_a\delta_{\ell,a}
-\frac{\rho}{L}\left(kA_{\ell,k,a}
+\sum_{j<k}(2j+1)A_{\ell,j,a}\right),
\]
\[
\dot B_{\ell,k,a}=\rho h_{\ell-1,a}
-\frac{\rho}{L}\left(kB_{\ell,k,a}
+\sum_{j<k}(2j+1)B_{\ell,j,a}\right).
\]

The backward signals are
`delta3=c*(1-h3^2)`,
`delta2=(What3.T delta3)*(1-h2^2)`, and
`delta1=(What2.T delta2)*(1-h1^2)`.
Initialize A=0, B at mode zero to the initial incoming activation, and the
remaining B modes to zero. Reconstruct both internal operators as

\[
\boxed{\widehat W_\ell=W_{\ell0}
-\frac{2}{MnL}\sum_{a=1}^{M}\sum_{k=0}^{P-1}
(2k+1)A_{\ell,k,a}B_{\ell,k,a}^{T},\qquad \ell=2,3.}
\]

The same reconstructed operator and its actual transpose are used in
forward and reverse propagation. The first-layer weights and readout obey
their original gradient equations evaluated at this current network.
Both memories are coupled through the current network; no dense reference
trajectory, fitted coefficients or independently trained reverse map is
used. P counts chronological shifted-Legendre history modes.

The exact physical defect is `(0,E2,E3,0)`, where

\[
E_\ell=\frac{2}{Mn}\sum_a
\left(r_a\delta_{\ell,a}-\rho u_{\ell,P,a}\right)
\left(h_{\ell-1,a}-h_{\ell-1,P,a}\right)^T,
\]

with `u_P=sum_k (2k+1)A_k/L` and
`h_P=sum_k (2k+1)B_k/L` at the current history endpoint.
Each defect has rank at most M and vanishes at initialization. Each learned
matrix increment has rank at most MP. These exact identities identify the
omitted history covariance; they alone do not bound accumulated trajectory
error or imply loss monotonicity.

The production solver recomputes tanh responses at every stage. This
implements the nonlifted form of the same continuous closure and avoids
redundant response-invariant drift. Its evaluated right-hand side is not
rational. The equivalent rational response lift is derived separately.

## Tasks, initialization and observable

All models share the exact NumPy `default_rng(20260920)` draws, in order
W1, W20, W30, c. Entry standard deviations are respectively
`1, 1/sqrt(n), 1/sqrt(n), 1/n`. The stored readout c is additionally divided
by n in the output. The common initialization SHA256 is
`6043d3c0097c6cdb4c22b6db84fc4d5975b61dbeac895b6f6a2a2a8402e79ca0`.

| Task | Angles in degrees | Labels |
|---|---|---|
| Two outliers, alternating | 15,27,39,51,63,75,165,285 | + - + - + - + - |
| Quadrant, alternating | 10,20,30,40,50,60,70,80 | + - + - + - + - |
| Quadrant, pairs | 10,20,30,40,50,60,70,80 | + + - - + + - - |
| Quadrant, center/edges | 15,21,27,33,39,45,53,60 | - - + + + + - - |
| Equally spaced, odd labels | 0,45,90,135,180,225,270,315 | + + - + - - + - |

The last task uses the exact bias-free oddness quotient: its first four
points with equal weights. The physical loss equals that of the original
eight-point task. `deep_circle_cases.json` retains both definitions.

Every comparison uses each model's own numerical training-MSE crossing.
At the primary target MSE=.001, measure the RMS difference between the
closure and dense predictions over 8192 equally spaced circle directions.
These are matched-loss comparisons, not matched-time comparisons or errors
against held-out target labels. Dense references were trained anew at this
depth and width. All 40 primary trajectories reached the target.

## Prediction results

All entries below use rtol=3.125e-6 and the same finest dense reference
within a task. Smaller RMS means closer agreement with dense training.

| Task | P=1 RMS | P=2 RMS | P=3 RMS | Best tested order |
|---|---:|---:|---:|---:|
| Two outliers, alternating | 0.108086211 | **0.023797219** | 0.031476459 | 2 |
| Quadrant, alternating | 0.274642803 | **0.028358443** | 0.058491243 | 2 |
| Quadrant, pairs | 0.012185557 | 0.003708120 | **0.001214942** | 3 |
| Quadrant, center/edges | 0.078973166 | 0.025701932 | **0.007246026** | 3 |
| Equally spaced, odd labels | 0.014984607 | 0.002412359 | **0.000281860** | 3 |

P=1 exceeds the predeclared coarse-agreement threshold RMS=.1 on the two
alternating tasks. P=2 and P=3 satisfy that threshold on all five tasks.
The relative deterioration from P=2 to P=3 on the two alternating tasks is
retained, rather than treating the largest order as automatically best.

For the outlier task, the P3-minus-P2 RMS gap is .00767924; the corresponding
sum of observed dense and closure refinement sensitivities is .000564743.
For the quadrant alternating task, these quantities are .03013280 and
.000323306. All 15 endpoint pairwise order comparisons are resolved under
the frozen empirical sensitivity rule. This rule provides numerical
diagnostics, not certified error bars.

Figures and machine-readable results are under
`data/generated/neural_response_memory_20260922/deep_circle_analysis01/`:

- `rms_vs_order.png` / `.pdf`: all five order curves.
- `function_curves.png` / `.pdf`: dense/P1/P2/P3 functions and training points.
- `endpoint_differences.png` / `.pdf`: signed differences from dense.
- `loss_trajectories.png` / `.pdf`: the physical training histories.
- `comparison_metrics.csv`: all 75 milestone comparisons.
- `endpoint_metrics.csv`, `order_comparisons.csv`, `run_inventory.csv`.
- `metrics_summary.json`: unrounded values, selections, gates and provenance.

## Numerical checks and reproduction status

The primary campaign is 5 tasks x 4 models x 2 tolerances, namely
rtol=1.25e-5 and 3.125e-6 with atol=rtol/100. Computation uses deterministic
float64 on two RTX 3090s, one worker per GPU, without TF32. The method is
adaptive Heun with an Euler error estimate, physical internal-matrix error
control and 32 bisections of its quadratic continuous extension for loss
events. The event is the first bracketed crossing found by this numerical
procedure; it is not a proof that no unobserved within-step crossing exists.

All 75 comparisons across loss milestones .1,.03,.01,.003,.001 pass the
frozen numerical gates. The maximum individual coarse/fine predictor RMS
change across these comparisons is .000181207. Every dense and closure
change is below .005 and below 10% of its paired discrepancy. The maximum
8192-versus-4096 nested-grid score change is 1.39e-15. Physical milestone
losses pass the 1% criterion. No conditional third tolerance was triggered;
the branch decision is `DEEP_CIRCLE_NUMERICAL_DECISIONS.md`.

Nine deterministic implementation tests pass. The separate checker checks
dense gradients against the maintained NumPy implementation, both transpose
actions, moment transport by numerical quadrature, both derivative and
defect identities, the physical error controller, noninitial zero-residual
states and the exact antipodal quotient. Independent CPU rescoring agrees
on all 75 milestone, 15 endpoint and 75 order-comparison rows; maximum
metric difference is 1.09e-19. All 40 primary run hashes and metadata pass.

Both predeclared opposite-GPU repetitions (dense and P3 on the outlier task)
reached MSE=.001 and reproduce every saved scientific array and checkpoint
field bit-for-bit. Only wall-clock timing arrays are excluded. The dense
comparison covers 48 fields across six NPZ files; P3 covers 66 fields across
six files. Evidence is `deep_circle_audit01/reproduction_check01/check.json`.
Full independent saved-state replay passes for all 42 primary/repeated
trajectories, covering 294 observations and 210 checkpoint states after the
verified recovery described below. The largest pointwise difference between
reconstructed and recorded circle predictions is 3.39e-13. The supervisor
also checks that the combined replay contains every expected trajectory
exactly once (`deep_circle_audit01/supervisor_final_verification.json`).
`DEEP_CIRCLE_CHECK.md` is the authoritative check record. A separate bounded
report consistency check is retained in `DEEP_CIRCLE_REPORT_CHECK.md`.
No result here is a promotion to the established book/code.

The first replay exposed one damaged archive member: W3 in the MSE=.001
checkpoint of the coarse-tolerance quadrant-pairs dense run. Its whole-file
hash still matches the producer's recorded hash, but its internal CRC fails.
A scan of all 252 primary/repeat NPZ archives finds exactly this one failure.
The separately saved final state has the same physical time, loss and all
other checkpoint fields byte-for-byte; its W3 differs in one bit of one
float64 word (absolute difference 1.862645149e-9). Restoring that bit from the
valid final state reproduces the original recorded CRC exactly. The original
archive is retained, and the repair uses a fresh file with explicit provenance.
No prediction array, model trajectory, analysis metric or training input is
changed. This is a verified recovery of a redundant saved state; the cause of
the original bit discrepancy has not been established. Evidence is in
`deep_circle_audit01/corruption_diagnostic01/` and
`deep_circle_audit01/all_archive_integrity01/check.json`.
`repair_deep_circle_checkpoint.py` performs the narrow verified repair;
`deep_circle_recovery01/repair_manifest.json` records the original/recovered
hashes, bit position and unchanged fields. The supervisor independently
compared all 268535252 archive bytes, finding exactly the one-bit change,
and checked the repaired CRC and the sole copied-summary hash update
(`deep_circle_recovery01/supervisor_verification.json`). The replay view
under `deep_circle_recovery01/run_view` links every unchanged run artifact
to its original and substitutes only the recovered checkpoint and its hash.

Hidden features move substantially. Over the 20 finest primary trajectories,
the RMS change of training-set activations from initialization ranges from
.345441 to .648572 in layer 1, .382720 to .736775 in layer 2, and .460717
to .677563 in layer 3. These are direct finite-width measurements on tanh
features in [-1,1], not a theorem about an asymptotic nonlazy limit.

## State, measured memory and runtime

The four history arrays use `4*n*M*P` scalars. For the eight-point tasks,
each learned matrix increment has rank at most 8,16,24 at P=1,2,3, and the combined
history arrays use 1,2,3 MiB in float64. For the four-point quotient the
bounds are 4,8,12 and the history storage is .5,1,1.5 MiB.

The direct-coordinate moving state has `nd+n+4*n*M*P+1` scalars, including
W1,c and the clock. For eight points it uses approximately
1.094,2.094,3.094 MiB. The dense moving state uses 256.094 MiB.
However, the closure also retains both fixed initialized matrices, totaling
256 MiB, and their dense multiplication cost. Its minimal moving-plus-fixed
storage is therefore slightly larger than the minimal current dense network.
This is a reduction of learned moving state, not compression of the entire
stored network. Actual implementations also retain initialization copies
for checks/control and allocate solver workspaces; those are separate from
the minimal counts.

Measured peak CUDA allocated memory is 432.063 MiB for the closure runs
versus 2592.938--2849.032 MiB for the dense runs. This is a property of these
implementations and solver workspaces. The closure is modestly slower in
every finest-resolution comparison below; no runtime improvement is claimed.
Times include observations performed during integration.

| Task | Dense seconds | P1 seconds | P2 seconds | P3 seconds |
|---|---:|---:|---:|---:|
| Two outliers, alternating | 100.143 | 124.119 | 116.032 | 102.497 |
| Quadrant, alternating | 98.963 | 127.102 | 118.807 | 107.892 |
| Quadrant, pairs | 70.580 | 83.767 | 83.120 | 76.249 |
| Quadrant, center/edges | 85.890 | 100.065 | 99.802 | 92.583 |
| Equally spaced, odd labels | 47.719 | 57.064 | 55.450 | 51.657 |

Two 30-step feasibility pilots, 40 primary trajectories and two repeats
used 3114.516 summed GPU integration-wall seconds including in-loop
observations, or 2826.286 seconds excluding them. This is below the frozen
12600-second cap. Pilots intentionally stopped at their step cap and are
not fitted scientific endpoints. All 42 full trajectories fitted; no training
trajectory failed or hit a cap. The archive recovery described above is
separate from integration. Setup, final inference, serialization, analysis
and independent replay are outside this integration budget and retained
separately in receipts. No further training is planned.

## Reproduction and limits

Use a fresh output directory for every command. From the repository root,
the executed primary/analysis/repeat forms are:

```bash
/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/run_deep_circle_campaign.py \
  --phase primary \
  --out data/generated/neural_response_memory_20260922/deep_circle_primary01 \
  --prior-roots data/generated/neural_response_memory_20260922/deep_circle_pilot01

/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/analyze_deep_circle.py \
  --runs data/generated/neural_response_memory_20260922/deep_circle_primary01 \
  --out data/generated/neural_response_memory_20260922/deep_circle_analysis01

/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/run_deep_circle_campaign.py \
  --phase repeat \
  --selections studies/neural_response_memory_20260922/DEEP_CIRCLE_REPETITIONS.json \
  --out data/generated/neural_response_memory_20260922/deep_circle_reproduction01 \
  --prior-roots data/generated/neural_response_memory_20260922/deep_circle_pilot01 \
                data/generated/neural_response_memory_20260922/deep_circle_primary01
```

The existing names above are receipts, not overwrite targets. Replace them
with new study-owned paths for another execution. Exact pilot inputs are
retained in study source as `deep_circle_pilot_dense.json` and
`deep_circle_pilot_moment.json`, byte-identical to the executed inputs under
`deep_circle_pilot_configs01`; each can be run by `deep_circle_run.py --config
<json> --out <new-directory>`. All literal tasks and launcher defaults are
retained in study source. Campaign and per-run receipts retain effective
configurations, source/data/query/initialization/checkpoint hashes, exit
status, solver traces, software versions, hardware, time and memory.
The generation environment is Python 3.10.14, NumPy 1.26.4 and
Torch 2.9.0+cu130. Audit commands and their evidence are in the check report.
To reproduce the specific saved-archive recovery, run
`studies/neural_response_memory_20260922/repair_deep_circle_checkpoint.py --out <new-study-generated-directory>`
with the same Python environment. It requires the exact recorded damaged
archive and independently valid redundant final state, checks their hashes,
and refuses any discrepancy beyond the specified verified bit. A newly
generated intact checkpoint does not require this repair.

This experiment supports useful low-order prediction agreement for the
tested width, initialization, tasks and fitted finite horizon. It does not
establish a universal best P, monotone convergence in P, a width-uniform
bound, a population limit, all-time tracking, or a speed advantage. The
tasks were inherited hard examples, not a random benchmark sample. Both
depth and width differ from earlier circle runs, so these results do not
isolate a causal effect of depth. Repetition verifies determinism for its
two specified configurations and supplies no additional random seeds.
