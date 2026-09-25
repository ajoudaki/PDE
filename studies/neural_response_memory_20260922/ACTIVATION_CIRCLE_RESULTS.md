# Activation robustness of the three-hidden-layer circle closure

Status: the bounded campaign and all planned checks are complete. All64
primary runs, two conditional refinements and eight cross-GPU repetitions
finished. Final scores are internally checked for their stated finite-instance
scope, with capped/unavailable comparisons and one retained checker anomaly
qualified below. This is the user-requested2026-09-25 continuation of this study.

## Question and comparison

Use ReLU, exact GELU, standard SELU and uncentered logistic sigmoid in all
three hidden layers at width 4096. Compare each activation's freshly trained
dense network with its P=1,2,3 chronological response-history closures on the
two previously hardest tasks: alternating labels on the six-point cluster
with two outliers, and alternating labels on eight quadrant points.

All eight literal input directions are retained. Parameters, input scaling,
loss, mobilities and seed are held at the inherited values. In particular,
there is no activation-specific initialization or centering. This is a test
of closure fidelity under that fixed setup, not a ranking of optimally tuned
activation functions. See [the frozen protocol](ACTIVATION_CIRCLE_PROTOCOL.md)
and [literal cases](activation_circle_cases.json).

The primary observable is uniform-circle prediction RMS from the same
activation's dense reference, at each model's own training-MSE .001 crossing.
The panel contains 8192 directions. This measures disagreement with dense
training, not error against a known target function away from training points.
The predeclared coarse-agreement threshold is RMS <= .1 for labels +/-1.
Intermediate matched-loss and fixed-time comparisons are reported separately
when a model does not fit. A missing crossing or failed numerical gate is
inconclusive, rather than an adverse closure result.

The crossing is located by 32 bisections of an accepted step's quadratic
Heun interpolant after its endpoints bracket the loss threshold. For a
nonmonotone trajectory this is not a certified earliest crossing, and a
tolerance-defined fitted endpoint is not an infinite-time limit. Numerical
refinement checks are empirical diagnostics rather than rigorous error bounds.

## What changes in the closure

The [activation-general derivation](ACTIVATION_CIRCLE_DERIVATION.md) replaces
the forward response and its derivative in both hidden links. The same
four moment populations, common activity clock, lower-triangular Legendre
transport, physical matrix reconstruction and two exact defect identities
remain. Initial moments must use the selected activation.

GELU and sigmoid give locally Lipschitz direct-coordinate fields on the
positive-length domain. ReLU and SELU require the declared selected kink
derivatives; their algebra holds along an existing absolutely continuous
selected-field trajectory almost everywhere. Neither a nonsmooth uniqueness
theorem nor smooth-solver order across switches is asserted. The implementation
uses direct activations; the optional coordinate lifts in the derivation are
not the numerical model.

Both initialized dense matrices remain stored and used. The low-rank history
closure compresses their learned corrections, with per-link rank at most
8P. It is not compression of the entire initialized network.

Writing \(\rho=\sqrt{M^{-1}\sum_a r_a^2}\), \(\dot L=\rho\), and
\(T_k(X)=kX_k+\sum_{j<k}(2j+1)X_j\), the implemented closure for each
internal link \(\ell=2,3\) is

\[
\dot A_{\ell,k,a}=r_a\delta_{\ell,a}-(\rho/L)T_k(A_{\ell,\cdot,a}),
\qquad
\dot B_{\ell,k,a}=\rho h_{\ell-1,a}-(\rho/L)T_k(B_{\ell,\cdot,a}),
\]
\[
\widehat W_\ell=W_{\ell0}
-\frac{2}{MnL}\sum_{a=1}^M\sum_{k=0}^{P-1}(2k+1)
A_{\ell,k,a}B_{\ell,k,a}^{T}.
\]

Here \(h\) and \(\delta\) are the current forward and backward responses
of that closure, using its selected activation and the actual reconstructed
transpose. Initially \(L=1\), \(A=0\), \(B_{\ell,0,a}=h_{\ell-1,a}(0)\)
and the higher B modes vanish. The first layer and readout follow their
canonical gradient equations. P changes only the number of retained
chronological modes; it does not add independently trained factors.

The four history populations use 1, 2, or 3 MiB for P=1,2,3 at this width
and sample count, alongside the two fixed matrices' 256 MiB. These counts
exclude first-layer/readout state, work arrays, solver stages and outputs.

## Completed scientific comparisons

The primary campaign contains64 valid trajectories:28 reached MSE .001 and
36 reached the300-second integration-wall limit. The two predeclared SELU
refinements also ended at their wall limits. There are66 valid scientific
trajectories in `activation_circle_analysis_final03/metrics_summary.json`;
the separately retained externally interrupted attempt is not a valid
scientific trajectory. Pilots, repeats and optimization validation are excluded
from the comparison inventory.

All nine available fitted comparisons pass the declared loss, solver-refinement
and circle-grid gates. The whole-circle RMS differences from the common finest
same-activation dense reference are:

| Activation and task | P1 | P2 | P3 |
|---|---:|---:|---:|
| GELU, two outliers |1.439745959|.242388805|.024854432|
| GELU, quadrant |5.783894822|.663486173|.260103786|
| Sigmoid, two outliers |.664149236|.268268541|.241369637|

P3 is best at all three available fitted comparisons, but only GELU P3 on the
outlier task meets the predeclared absolute RMS<=.1 agreement criterion. The
closure's fitted fidelity therefore depends on activation and task; these data
do not support uniform robustness of P<=3 across the tested activation changes.
In particular, the sigmoid discrepancy is resolved by the numerical checks,
not an artifact of an unresolved solver comparison.

For descriptive scale context, the corresponding dense circle RMS values are
2.115098825,5.453962949 and1.411327199. P3's discrepancy divided by dense circle
RMS is respectively1.1751%,4.7691% and17.1023%. These supplementary normalizations
are post hoc, calculated directly as
\(\sqrt{\operatorname{mean}(f_P-f_D)^2}/\sqrt{\operatorname{mean}f_D^2}\)
on the same saved8192-point `loss_0.001` panels. They do not replace the
predeclared absolute threshold. The GELU quadrant dense function ranges from
approximately-8.27 to8.46 away from its eight unit-label training constraints;
a few-percent relative discrepancy can exceed .1 in absolute units.

Sigmoid's quadrant comparison is unavailable at MSE .001: the finest dense
and P1 runs stop at losses .077876579 and .012692678, while P2 and P3 fit.
At their deepest all-model shared milestone, MSE .1, the P1/P2/P3 circle
errors are .267296612/.203490369/.157355042. All three numerical gates pass.
This is an intermediate-learning comparison, not a fitted-endpoint result.

All16 ReLU primary runs and all16 SELU primary runs end at their wall limits
without fitting. Their finest selected final losses lie between .938 and .992
for ReLU, and .821 and .958 for SELU. These outcomes leave fitted closure
fidelity inconclusive; they do not establish inability to fit given more
resources or failure of the closure. No ReLU shared .9 milestone is available
at the selected resolutions.

SELU needs an additional qualification. At MSE .9 on the outlier task,
primary P2/P3 comparisons failed relative sensitivity gates. The prescribed
extra dense and P3 trajectories were executed at rtol7.8125e-7. The extra
dense trajectory stops at loss .909167934 before reaching .9, while P3 reaches
.9. Consequently the final selected-resolution comparison is unavailable.
An empty final refinement-request list does not mean this earlier failed
accuracy check was resolved. The original primary gates, the two refinement
attempts and the missing crossing remain recorded. No further tolerance or
cap-rescue branch is authorized by this protocol.

The final selected resolutions provide72 shared-loss comparisons, all passing
the numerical gates, and27 matched-time diagnostics,15 passing and12 unresolved
by their relative sensitivity tests. The secondary time failures do not trigger
refinement under the protocol. All72 available order-pair comparisons are
resolved:70 improvements and two worsenings when increasing P. Both worsenings
are P2 to P3 at MSE .5 for sigmoid, one on each task. Thus P3's best fitted
scores are not a claim of monotone improvement at every stage of training.

These fits include substantial feature learning. At the fitted GELU outlier
dense endpoint, hidden-feature RMS motions in layers1/2/3 are
1.4221/2.4504/2.5145. At the sigmoid outlier dense endpoint they are
.34350/.22185/.13856, with first-layer parameter RMS motion7.4260 and about
48.4% of first-layer sigmoid activations in the recorded saturation region.
These are descriptive diagnostics, not a proof of the mechanism behind the
activation-dependent closure error.

For context, the completed [tanh experiment](DEEP_CIRCLE_RESULTS.md) used the
same architecture, initialization, fitted-loss observable and tolerance pair.
Its P1/P2/P3 circle discrepancies were .108086211/.023797219/.031476459 on the
outlier task and .274642803/.028358443/.058491243 on the quadrant task. P2 was
best for both tanh cases. The present GELU outlier P3 has comparable absolute
error, while GELU quadrant P3 and sigmoid outlier P3 are less accurate. The old
per-run wall allowance was600s versus300s here; capped activation outcomes
cannot rank ultimate learnability against tanh. One seed, two tasks and three
orders do not establish convergence in P or width, or optimized activation
performance.

## Checks and artifacts

Implementation and independent algebra checks passed before width4096
execution, and all eight feasibility pilots passed. The [implementation audit](ACTIVATION_CIRCLE_CHECK.md)
retains exact scopes and receipts. An independent NumPy rescore of the final
66 trajectories agrees exactly on all scores, sensitivities, available/unavailable
primary slots, loss/time gates and order-ranking margins. Its flat source is
`check_activation_final_metrics.py` and receipt is
`activation_circle_audit_final01/panel_rescore01.json`.

All eight fresh dense/P3 outlier repetitions pass the independent checker,
including actual swaps between GPUs0 and1. Fitted trajectories reproduce their
endpoints; capped trajectories reproduce the shared deterministic accepted
prefix and common saved events, excluding unequal wall-cap endpoints.
Explicit physical-matrix replay covers82 saved runs (66 scientific runs,
eight pilots and eight repeats) and499 distinct saved observation panels.
Every physical panel passes: maximum circle prediction discrepancy is
4.682e-12, training prediction discrepancy6.308e-12, and diagnostic discrepancy
6.253e-13, all below the frozen2e-9 replay thresholds.

One original batch record reports a failed regenerated-initialization hash
for the repeated extra-fine SELU dense run. All its19 archive/config/source
integrity checks and both physical panels passed, with exactly matching circle
and training predictions; its cross-GPU reproduction also passed. Independent
fresh CPU regeneration gives the expected canonical hash, and a fresh isolated
replay with the unchanged checker, inputs and gates passes the hash and both
panels. The discrepancy did not reproduce; its cause is unidentified because
the initial checker did not record the computed digest. No scientific artifact
was edited and no training was repeated to obtain this recovery.

The original `activation_circle_audit03/replay_batch_018.json` and controller
status `complete_with_audit_failures` remain unchanged as historical evidence.
The passing recovery is `activation_circle_audit03/replay_recovery01.json`, with
command, environment and source/input/output hashes in
`replay_recovery_execution01.json`; independent CPU confirmation is
`activation_circle_audit_final01/initialization_recheck01.json`.
The [final internal check](ACTIVATION_CIRCLE_FINAL_METRICS_CHECK.md) reconciles
these records. Thus all82 saved runs have passing verification after one
explicitly retained, isolated checker recheck; this does not erase the first
failure or establish its cause.

The campaign executes83 attempts: eight pilots,64 logical primary runs, one
retained external interruption and its already-counted primary replacement,
two refinements and eight repetitions. Summed charged integration time is
18424.841682184488s against the33000s cap, below the amended113-attempt ceiling.
This charge includes the externally interrupted attempt. Setup, serialization,
independent replay and bounded execution-optimization validation are separately
recorded, not hidden in the training budget. No further research trajectory is
pending under this protocol.

The [summary figure](../../data/generated/neural_response_memory_20260922/activation_circle_summary01/activation_circle_summary.png)
shows fitted errors alongside all32 finest selected final losses and physical
times. Gray primary cells mean no fitted comparison. The
[circle functions](../../data/generated/neural_response_memory_20260922/activation_circle_analysis_final03/function_curves.png)
show fitted predictions for GELU and sigmoid-outliers and explicitly label the
sigmoid-quadrant MSE .1 fallback. Matching PDF exports, loss trajectories,
endpoint differences, RMS-versus-order figures, all metric CSVs and provenance
manifests are retained in the same final analysis/summary directories.
The plot sources select from the frozen metrics; no gate or score is changed
for presentation.

The user temporarily restricted execution to GPU0 and later explicitly released
GPU1. The [execution amendment](ACTIVATION_CIRCLE_EXECUTION_AMENDMENT.md) and
`activation_circle_finish03/user_gpu1_reauthorization01.json` preserve both
instructions. The [bounded execution optimization](ACTIVATION_GPU_OPTIMIZATION.md)
yielded roughly2x faster closure execution with roundoff-scale validation
agreement. Both GPUs were used for the completed remaining runs and checks. Model, seed, precision,
tolerances, clock and stopping rules are unchanged; actual execution backends
are recorded per run. All earlier evidence remains intact.

The separately labeled [initial-response diagnostic](ACTIVATION_INITIAL_KERNEL_NOTE.md)
concerns only the prescribed initialization. It finds weak label-aligned
response for sigmoid and strong spectral anisotropy for GELU, but supplies no
long-time learning or closure-fidelity conclusion. The sigmoid fitting outcomes
above must not be replaced by an inference from that initial kernel. Its
corrected inputs, original calculation and16 small Jacobian-block checks remain
in `activation_circle_initial_kernel02` and the linked note.

This is study-owned internal research; no maintained-source change, promotion
or Git-index write is part of this work.

## Reproduction and retained execution

The numerical environment is Python 3.10.14, NumPy 1.26.4 and Torch
2.9.0+cu130, float64 with deterministic operations and TF32 disabled.
Numerical CPU libraries use one thread. The recorded executable is
`/home/amir/miniconda3/bin/python`; the actual environment, source/configuration
hashes, initialization hash, commands, device assignment and exit status are
also retained per run. All activations use initialization hash
`6043d3c0097c6cdb4c22b6db84fc4d5975b61dbeac895b6f6a2a2a8402e79ca0`.

The original `activation_circle_primary01` and user-amended
`activation_circle_primary_continuation01/02` together retain the primary
schedule. `activation_circle_finish01` records the stopped original
coordinator and first GPU-release receipts; `activation_circle_finish02`
records the first continuation and its clean pause for optimization.
`activation_circle_finish03` records the completed continuation, renewed two-GPU
authorization, conditional branch, repetitions and audit commands.
No old trajectory is overwritten. The controller is
`continue_activation_circle_campaign.py`; its seven scientific producer and
protocol hashes remain the same as the original scheduler's manifest.

For a fresh individual reproduction, use a retained run's `config.json`
with its recorded runner, either `activation_circle_run.py` or
`activation_circle_fast_run.py`, and `--config CONFIG --out FRESH_DIRECTORY`.
Retain its execution backend and record any device change in the new
configuration. `analyze_activation_circle.py --runs`
accepts all three primary roots and any conditional refinement root, with
`--out` naming a fresh analysis directory. Set `CUBLAS_WORKSPACE_CONFIG=:4096:8` before invoking a deterministic CUDA
check. The independent checker supports
`replay RUN... --device cuda:0 --output FRESH_JSON` and
`reproduction ORIGINAL REPEATED --output FRESH_JSON`. These are reproduction
recipes, not authorization to reopen completed or capped campaigns.
