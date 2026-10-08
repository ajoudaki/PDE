# Absolute logarithmic exponent for a predeclared passive test panel

## Latest empirical status: rollout initializer, 2026-10-08

The rollout-based practical variant passes the recorded trajectory-RMS,
storage-matched-control, fitting and Euler-refinement checks at dense widths
4096 and 8192, on raw digits 3 versus 8. Its frozen coordinate rule has
`q proportional to log(en)^(5/2)`, hence total model storage proportional to
`log(en)^5` for fixed data dimensions. The measured panel/iid-dense
maximum-time validation-RMS ratios are 0.336 and 0.693, with 1.79-fold and
4.96-fold model-storage reductions. **This is two-width, one-held-out-seed
empirical evidence, not a proof of asymptotic accuracy for this practical
initializer.** At width 8192 the panel model loses to the matched small model
on endpoint RMS, despite winning on maximum-time and time-average RMS.

The implementation and complete outcomes, including failed original
resolution checks, costs, qualifications and reproduction commands, are
recorded in the final sections below. The earlier jet-only experiment is
retained as historical evidence, not the current best empirical result.
The original theorem and its qualifications are unchanged. The setup uses
a cheap full-interval dense solve, not an early-time prefix; no dense solve
or trajectory is retained by the autonomous compressed runtime.

## Research contract

New study, 2026-10-05, for the user's changed observable contract. A finite
panel of p inputs is declared at time zero, before Gaussian initialization.
Its first m points are training examples and its remaining points are passive
tests. All inputs lie on the radius-sqrt(d) sphere. Training inputs span R^d
and m >= d; correlated data remain allowed. The dense network has hidden
width n, depth L >= 2, genuinely nonlinear activations and learned hidden
features. First weights are iid N(0,1), hidden weights iid N(0,1/n), and stored
readout is zero. The MSE is (1/m) sum_{a<=m}(f(x_a)-y_a)^2, with block
mobilities (n,1,...,1,n). Passive points have weight zero and do not change
the loss normalization, any weight update, or physical training time.

Retain the admissible analytic activation class (bounded derivatives on a
strip, possibly unbounded values), positive initialized training-feature Gram
gap and small-label regime. Any sufficient quantitative bounds not proved
from these hypotheses must be exposed as missing or conditional, not silently
imposed. No active loss or residual is assigned to passive observations.

Seek a finite, initialization-only, autonomous and restartable representation
whose error is sup over all physical times including the endpoint and max over
the p declared points. It must approximate the actual dense reference at a
specified dense-vs-dense variability tolerance, not merely some n^(-1/2+o(1))
envelope with an uncontrolled subpolynomial loss. Explicit comparison to an
upper certificate and actual random discrepancy are separate claims.

The desired total retained storage is C (log(en))^a with an absolute exponent
a independent of d,m,p,L and all fixed problem parameters (possibly allowing
activation-dependent a only if explicitly identified). State the entire
prefactor C and width threshold dependence when obtained. Track panel/data
storage explicitly and distinguish fixed p from p=p(n). Removing dimension
from the logarithmic exponent does not by itself control constants in d.
All fixed coefficients, dynamic state, algorithm descriptions and live query
workspace count. No retained dense oracle, future-trajectory playback, free
function-valued state, arbitrary-real packing or hidden program memory is
allowed. Streaming input or arithmetic work cannot conceal retained state.

The finite panel and zero loss weights are the user-authorized relaxation.
Do not additionally freeze features, linearize the model, assume orthogonal
training data, choose a special initialization, discard depth, or replace the
whole training horizon by compact-time convergence. A supplied passive input
does not authorize using its label in training.

## Inputs and process

Allowed scientific inputs: this study, the user's model/target specification,
maintained docs/ and code/, and verified primary external sources. The user
explicitly answered “Yes—reuse the existing compact proof” on 2026-10-05.
This authorizes the current integrated compact-construction proof, its
comparison/runtime/source-energy dependencies and its integrated reference
accuracy statements in studies/integrated_general_compression_20261004.
The earlier compact refinement was consolidated there; its obsolete path is
not used. Other studies remain outside scope. Prior dimension-barrier study
research is not imported into this new study.

Read current AGENTS.md and Part 1 of RESEARCH_WORKFLOW.md, and the rigorous-math
and conjecture-investigation skills. Reuse the already-read current maintained
index/notation and skill references. Custom canonical-notation skill remains
permission-denied; follow the explicit user notation contract. Initial HEAD:
3834145d910202a84824d943fe7d7f65714d96f2, index empty. Unrelated dirty migration
files and other studies are preserved. No experiment, book edit or Git commit
is authorized by this theoretical study.

## Work allocation and status

Lead owns this README and synthesis. Fresh independent scoped routes will
investigate finite-panel dynamic compression, time regularity/source complexity,
and adversarial scope. Each receives a separate file and does not read another
route before freezing its first conclusions. Prior agents or prior unpromoted
studies are not scientific inputs.

## Current result and check status

The requested finite-panel extension is **internally checked, relative to
the explicitly reused source/selection/compilation and fitting theorems**.
The full statement and constructive argument are in [RESULT.md](RESULT.md).
This is not promotion to the maintained book and not a fresh independent
audit of the older stochastic insertion dependency chain.

For a fixed panel of p total inputs, the original common label cap gives
layer width at most ceil(30000 p log(en)^(5/2)) and all-retained storage at
most 2^36 (L+1) p^2 log(en)^5 + 16p(d+1), plus the fixed activation/runtime
evaluator. Fixed metrics, data, solve caches and even simultaneous passive
feature/velocity buffers are counted. The sharper compact error remains
10 beta^(40L) Y(m/gamma)(1+sqrt(m/gamma)) exp(2sqrt(log(en)))/n, over all
physical times including the fitted endpoint and all declared inputs.
On the full original recurrence label allowance the absolute exponent
five is unchanged, with an activation/depth-only storage factor and the
existing full-range polynomial-prefactor error. No smaller label range,
bounded activation values, orthogonal data or frozen features is required.

For m >= 2, the general dense lower witness is a training input and so is
inside the panel. Compression error divided by the actual independent-dense
discrepancy in the same panel trajectory norm tends to zero in probability.
This does not claim endpoint separation or accuracy at undeclared inputs.

The independent first routes were frozen before comparison:

- `panel_source` owns [PANEL_SOURCE.md](PANEL_SOURCE.md): temporal coefficient
  count, paired initialization and selection transfer; its later separate
  addendum verifies the existing finite-query localization.
- `panel_runtime` owns [PANEL_RUNTIME.md](PANEL_RUNTIME.md): exact corrected
  optimizer, passive chains, full label interval, all-time comparison,
  finite-panel initialization, and actual-variability calibration.
- `panel_audit` owns [PANEL_AUDIT.md](PANEL_AUDIT.md): independent scope,
  source-rank, information-flow and complete-storage audit; its later
  localization addendum is clearly separated from the frozen first route.

The lead read and checked all three complete routes against the authorized
current integrated sources, assembled RESULT.md, and obtained two bounded
post-author checks. Both pass the final result version
`38ca06a2e812d8e2b45c6b7350c0437d710433b11a00b89aa66487a9229b028b`:

- [SYNTHESIS_AUDIT.md](SYNTHESIS_AUDIT.md), by `panel_audit`;
- [SYNTHESIS_RUNTIME_CHECK.md](SYNTHESIS_RUNTIME_CHECK.md), by `panel_runtime`.

These reports record complete read coverage, algebraic and dependency checks,
version hashes and limitations. They are internal checks, not blind promotion
reviews. Two presentation corrections were resolved: displaying the inherited
log(en) >= 2048 e^2 L source moment gate, and separating core network/residual
state from optional passive dynamical buffers already counted in total storage.

## Limits, reproducibility and handoff

The source success/CLT threshold remains unquantified and can depend on all
fixed parameters and confidence; deterministic gates are recorded in RESULT.md
(20). The construction is finite initialization-only compilation under the
inherited evaluator convention. It does not establish cheap preprocessing,
bounded preprocessing workspace, finite-bit storage, numerical conditioning,
or efficient simulation. No original-width object, future trajectory, or
external dense oracle is retained by the autonomous runtime. All fixed
parameters, including p, precede the width limit; growing-panel conclusions
must retain the explicit p factors and recheck probability qualifications.

This is a proof study, with no experiment or generated data. Verification is
by reading RESULT.md and its linked proof dependencies, then the two final
checks. A scoped `git diff --no-index --check /dev/null <file>` pass on the
study Markdown files produced no whitespace errors; the Git index remained
empty. No maintained docs/code, other study, or existing user changes were
edited. The result is ready for the user to inspect. No further campaign or
promotion is started by this handoff.

## 2026-10-08: authorized practical fixed-panel digit comparison

The user now explicitly requests implementing this study's construction and
testing one digit pair against the ordinary large dense reference and a
storage-matched smaller dense model. This authorizes the present empirical
continuation and scoped changes to `paper/figures/capture_trajectory.py`;
the earlier no-experiment statement describes the original theoretical work.
No theorem or paper text will be changed. Other studies are not inputs.

### Frozen experimental contract

Use sklearn's raw 8-by-8 digits, classes 3 and 8, all 64 pixels, per-image
unit normalization and no PCA. Use the existing stratified seed-47 split:
100 training samples, every remaining example in the predeclared validation
panel. Only training labels may enter initialization and dynamics. Reference
width is 4096, with two hidden tanh layers, Gaussian initialization, zero
readout, MSE and canonical mobilities. The comparison is physical-time Euler
for every model, with a half-step check; the panel optimizer is the specified
corrected-readout optimizer, not falsely called ordinary GD.

The practical compiler uses only order-two initialization jets. It retains
exact initialized training feature/image directions and first-weight columns,
and rank-eight approximations of the four panel source families before
forming exact initialized image pairs. Its selected-coordinate metrics are
constructed by oversampled coordinate restriction with exact source isometry;
measured conditioning and diagonal-comparison constants will be reported.
This replaces the expensive BSS selector with a numerical selector and omits
the globally continued high-order jets. Therefore it is an empirical
implementation of the study's architecture/runtime, not a certified
realization of its asymptotic source bounds. It is not trajectory playback,
the bounded Gaussian packet initializer, or a frozen-feature model.

Start with a fixed coordinate budget of 768 per layer. Select the small
dense width to match all retained model arrays, including the fixed metrics
and auxiliary residual, not just trainable weights. Common training and
predeclared validation input storage is reported separately and equally.
No source/dense arrays survive in the panel runtime. All models restart from
their stored initial state for refinement comparisons; trajectories are
experiment outputs, never model inputs.

Primary statistic: validation prediction RMS against the same dense
reference at the same final physical time. Also report the maximum sampled
time RMS and time-averaged RMS, dense-versus-iid-dense RMS, training MSE,
storage, setup time and runtime. RMS is not classification accuracy. A
positive empirical comparison requires lower RMS than the matched small
dense model and Euler refinement error below 10 percent of the smaller
reported nonzero endpoint comparison. Failure of either accuracy comparison
is retained; failed numerical validity is labeled inconclusive.

Use model seeds 201 (source/reference), 202 (independent dense) and 203
(matched small dense); this is one initialization comparison, not a
multi-seed scaling claim. Choose the horizon from training losses only:
start with the reference's first sampled MSE below 0.005, then extend to
a common horizon if another model has MSE at least 0.01, up to time 200.
Initial Euler steps are 0.05 and 0.025; if their comparison fails the
discretization gate, one further 0.0125 refinement is allowed. No orders,
seeds or digit pair may be selected by validation RMS. Conditioning failures
permit one increase to 1024 coordinates, explicitly recorded, not a silent
accuracy-tuned replacement. Each training run is capped at 300 seconds;
setup is capped at 300 seconds, with no full dense rollout. Maximum 16
training runs, two numerical setup attempts, and 60 minutes total compute.
The experiment stops after these outcomes and reports any unmet gate.

Lead owns implementation, this README and experiment synthesis. A fresh
read-only scoped agent reads this study's three construction notes and checks
the runtime/initial-jet mapping. A separate code check will inspect the final
implementation. Generated records belong under
`data/generated/finite_panel_absolute_compression_20261005/` in fresh folders.

### Implementation and checks

The new `panel-fit` and `panel-summary` commands live in the existing single
`paper/figures/capture_trajectory.py` executable. `FinitePanelCompression`
reuses the exact corrected runtime, not the bounded-packet ordinary-GF class.
The compiler uses full panel forward jets and training-only backward jets;
it truncates primary families before adding their exact initialized images.
No global truncation destroys those paired directions. The setup object is
discarded; a saved compiled checkpoint contains only selected weights, metrics,
the incoming metric inverse, and scalar provenance.

Checked implementation SHA256:
`e6b50d066283dde9de2e2cc06e281efb1d706f8b99764fc3a822a9ffa45f7dec`.
The fresh source-mapping agent read the three construction notes completely.
The independent `finite_panel_code_check` agent read those notes and the
relevant current implementation, without empirical results or other studies.
It checked the runtime, coefficient provenance, storage, label isolation and
summary contracts. Its independent backward-jet differentiation errors were
at most 2.8e-17; no algebra or information-flow defect remained.
Two reporting/audit corrections were implemented and rechecked: distinguish
deployable storage from the benchmark restart copy and work buffers, and
explicitly validate all model roles, source seeds, precision and matched
budgets in the summary command.

The persisted `--check-only` test compares the hidden/readout accelerations
and forward jets against independent automatic differentiation, checks the
metric/isometry and initialized forward/reverse identities, and checks
nonlinear-runtime training constraints and restartability. Final fresh output:
`data/generated/finite_panel_absolute_compression_20261005/check_final_v2/`.
This is implementation validation, not promotion or a certificate for the
empirical source truncation.

The initial 768-coordinate setup completed in 2.35 seconds on an RTX 3090.
Source ranks were 189 and 225; isometry error was at most 1.97e-14.
Its measured diagonal-comparison factors were 7.63 and 12.22, not the
theoretical BSS factor four. This qualification is retained in every report;
the positive metrics and runtime are well defined, but the theorem is not
invoked for these empirical orders, labels or metric constants.
The source/state checkpoint is in `digits38_setup_q768_v1/` under the
generated namespace. It has 639,844 moving and 1,769,472 fixed coordinates,
2,409,316 total; the matched ordinary network has width 1,520 and
2,409,200 weights. The common 357-input panel plus training labels adds
22,948 real coordinates to either model.

### Final empirical result: unfavorable at these fixed orders

The finished comparison used float64 Euler step 0.0125 through common physical
time 79 (6,320 updates per model), with all 257 validation images. Values
below are prediction differences against the same width-4,096 seed-201 dense
reference, not classification accuracy. The reference's final training MSE
was 0.005006330720. The time-average column integrates the validation-RMS
curve by the trapezoidal rule over the 159 saved times 0, 0.5, ..., 79.

| Model | Deployable coordinates | Final training MSE | Final validation RMS | Time-average validation RMS |
|---|---:|---:|---:|---:|
| Independent dense, width 4,096 | 17,043,456 | 0.005293986552 | 0.008108730967 | 0.009213783518 |
| Fixed-panel model, widths 768/768 | 2,409,316 | 0.000298388258 | 0.063598161146 | 0.066259545238 |
| Matched ordinary dense, width 1,520 | 2,409,200 | 0.004842170325 | 0.009837093148 | 0.011393522391 |

The panel model's endpoint discrepancy is 6.465 times the matched small
network's and 7.843 times the independent dense discrepancy. It fits the
training labels, but that does not make it a faithful approximation of the
dense predictions. These empirical orders/selection do not deliver the
desired comparison on this split and seed. No orders, seed or digit pair
were changed after observing validation scores.

The extra precommitted step refinement was used. Comparing steps 0.025 and
0.0125, endpoint prediction differences were 5.79e-5 for the reference,
5.85e-5 for the iid dense run, 1.12e-4 for the panel model, and 5.76e-5 for
the matched small model. Summing both sides of each comparison keeps the
endpoint diagnostic below 1.70e-4, comfortably below the descriptive
10-percent endpoint threshold 8.11e-4. Endpoint RMS is therefore stable in
these measured refinements; this is not a rigorous solver-error bound.

The **original stricter maximum-over-saved-times gate remains failed**:
the corresponding per-model maximum step changes are 0.001577, 0.001616,
0.003159 and 0.001536. It has not been replaced by an endpoint gate.
Accordingly the preregistered full-trajectory numerical-validity outcome
is inconclusive, while the displayed endpoint comparison is unfavorable
and numerically stable. The added endpoint diagnostics are explicitly
secondary reporting, not a post-hoc change to the original gate. No further
refinement or hyperparameter search was run after the allowed branch.

This is not a counterexample to the finite-panel theorem: the global
continued source compiler and its BSS selector were not implemented. These
are practical order-two/rank-eight sources, with label RMS one and measured
metric factors above four. Moreover the raw training-input matrix has rank
50 in the 64-dimensional pixel space, so the theorem's full input-span
condition is not met either. No PCA or other projection was inserted to
change the requested raw-image experiment. The exact corrected autonomous
runtime was implemented, but its theoretical dense-comparison certificate
is not invoked. One digit pair and one seed comparison cannot establish
or disprove an asymptotic compression rate.

### Costs, evidence and reproduction

Both RTX 3090 GPUs were used. The original panel compilation took 2.355
seconds and reached 487.80 MiB allocated CUDA memory, including the temporary
dense source, with zero dense training updates. At step 0.0125 the measured
whole-run times (training, loss checks and sparse validation together) were
181.25 seconds for the dense reference, 178.71 seconds for its iid copy,
45.91 seconds for the panel runtime, and 25.91 seconds for the matched small
network. Their peak allocated CUDA memory was 468.24, 468.24, 63.91 and
94.09 MiB respectively. These are per-process allocation peaks, not physical
device-wide memory or minimal workspace estimates; they include benchmark
restart copies. Checkpoint-loading time in the individual panel run report
is not the original compilation time. The summary field `training_seconds`
contains this whole-run wall time; the underlying run report separately
records training, loss-check, query and readout-refresh times.

There were 13 training runs, one setup, and two tiny deterministic check
invocations, all within the recorded budgets. The initial pilot and coarser
results remain preserved, not overwritten. Final raw trajectories and run
reports are the four `digits38_*_h00125_T79_v1/` directories; the complete
computed comparison is
`data/generated/finite_panel_absolute_compression_20261005/digits38_summary_final_v2/report.json`.
The intermediate comparison remains in `digits38_summary_v1/`. Every run
report retains its exact command, source hash, model/input initialization
hashes, precision, seeds, versions, stopping reason and actual horizon.
Run hashes differ because metadata and summary auditing were improved;
the compiler and nonlinear RHS were unchanged throughout the experiments.
The independent `finite_panel_code_check` agent recomputed both intermediate
and final comparisons from raw NPZ to 1e-14 and verified the checkpoint
inventory. It confirmed all four final 6,320-step runs, unchanged input and
initial-state hashes, the common step/time, all MSE values below 0.01, and
the separate endpoint-pass/strict-trajectory-fail numerical diagnostics.
No additional dataset run was performed by the checker.

Final summary SHA256:
`1064e1377dfd8c9cc1a587b55adcca594b246f2f81aa25e08b6f51e6bbf6b96b`.
Compiled checkpoint SHA256:
`4e25ff7e6445bf614bfc7c4badb586f5d60436461575fdb54f5d49f68f1d16a1`.
Final raw NPZ hashes, independently verified:

| Run | SHA256 |
|---|---|
| Dense reference | `f1b24cde49d0ba3a2e72e6f1c235a54517a9eab7828479f60fbc1b7208c5d133` |
| Independent dense | `b5eaee54c904d89cd2439401df214d0a2a4cc9633183c46ddbfdfea0b9849e2c` |
| Panel | `3f9fe548cd34026cdec1554d782c5e3d5b9186910311900b533f86a308b64dc0` |
| Matched small | `9b0c4acd0c7b4c566a530630ffa5cd8e83f2007b8e98dc5db8d3573c1222d859` |

The final summary-reporting source hash is
`8af7741b9bd7dad1e2b803f0d6591f602cc2193c5d7d2375364a0e7c2fdbdcb1`.
It differs from the earlier checked implementation only by the secondary
endpoint refinement fields and compact summary stdout. The original strict
numerical gate and all model/solver equations remain unchanged.

Environment: Python 3.10.12, PyTorch 2.6.0+cu124, NumPy 1.26.4,
scikit-learn 1.6.1; one CPU thread per process, TF32 disabled, float64 state.
Executable used: `/home/amir/Codes/sber-swap/.venv/bin/python`.
No new dependencies were installed. The dataset is sklearn's bundled digits.

To reproduce in a fresh output root, run `panel-fit --model panel
--setup-only --width 4096 --budget 768 --source-rank 8 --seed 201` first,
with a new `--out` path and an available `--device`. It writes
`compiled_model.pt`. Run `panel-fit` for each of the two dense seeds 201/202,
panel seed 201, and small seed 203, using `--horizon 79` and each of
`--step 0.025` and `--step 0.0125`; panel and small require `--checkpoint`
pointing to that same compiled file. All commands use the default digits
3/8, split seed 47 and raw preprocessing. Each run needs its own new `--out`.
Then call `panel-summary` with `--dense`, `--iid`, `--panel`, `--small`
pointing to the step-0.0125 directories and the corresponding `--*-coarse`
arguments pointing to step 0.025. The summary rejects incompatible inputs,
times, initialization, model identities, precision or storage budgets.
The preserved reports contain the exact executed versions of these commands.

This empirical continuation changes no theorem, proof, or paper claim.
The bounded test campaign is complete; no additional experiment is implied.

## 2026-10-08: authorized rollout-source continuation

The user explicitly authorizes replacing the inadequate low-order jet compiler
by rollout-derived temporal sources and testing practical logarithmic scaling.
This is a continuation of the same finite-panel implementation investigation,
not a modification of the theorem. The lead owns this README and changes to
the existing single executable `paper/figures/capture_trajectory.py`. Generated
products remain in this study's namespace. No maintained book or paper claims
are changed. Initial HEAD is `99f6930`; the shared index was empty. Unrelated
migration changes and the untracked transparent-learning study are preserved.

### Prospective experiment contract

The disputed mechanism is whether responses spanning the actual nonlinear
training interval, rather than only their second-order initial jets, support
a genuinely compressed autonomous runtime at dense-pair prediction accuracy.
The alternative is that source rank/selection or the corrected runtime still
requires substantially larger state in this practical label regime. Ordinary
small dense networks matched to **all** retained parameters and metrics, and
an independent full-width dense reference, are the primary controls.

Keep raw digits 3 versus 8, 100 training inputs, the 257 predeclared passive
inputs, split 47, two hidden tanh layers, zero readout, canonical mobilities,
and labels of magnitude one. No PCA, test labels, trajectory playback,
retained dense model, frozen features, or modified physical clock. Setup may
evolve a disposable dense reference across the relevant physical interval,
using a higher-order solver; report its full work and do not call a full
interval a short initial-time prefix. Actual compared training remains Euler.

Pilot seed 301 is used only for source construction and numerical choices;
confirmation seeds are 401 and 402, with iid controls offset by 10000 and
small controls by 20000. Start at width 4096, source horizon 100, source RK4
step at most 0.5, and piecewise Chebyshev interpolation on geometric time
panels. Interlaced unused source observation nodes check interpolation error.
Retain exact mandatory initialization directions and exact initialized images
of every retained paired source. When residualizing coefficient families,
remove only already represented directions with their required images intact.
All source, selection, precision and runtime errors remain separately recorded.

Pilot optional per-family rank caps are 32, 64 and 128; coordinate budgets
are 1024, 1536 and 2048, in that order and only as needed for source quality,
metric conditioning or an unsuccessful pilot comparison. A numerical selector
must preserve source isometry, and report its actual diagonal-comparison
factor; factor four is checked rather than inferred. Four predetermined
uniform-coordinate candidates are compared using only embedding condition,
with an empirical acceptance cap of 16 (not the theorem's factor four).
Pilot comparisons are
explicitly exploratory and never counted as confirmation. Freeze the smallest
successful pilot pair before confirmation. Across widths use that pair times
`(log(en)/log(e*4096))^(5/2)`, rounding upward; also report all fixed-data terms.
This prescribes O(log(n)^5) storage but does not prove its accuracy scaling.
Do not replace a budget failure by hidden full-width retention.

The bounded width sweep is 2048, 4096, 8192, with 16384 permitted only if
the 8192 runs finish below 150 seconds each and memory permits. Seed 401
covers the sweep; seed 402 repeats its smallest and largest genuinely
compressed successful widths. If the lowest width has no total-storage
compression, report that rather than silently omitting it.

The common training horizon starts at 100, with one extension to 150 only
if a model's training MSE remains at least 0.01. Source horizon is extended
with it. Initial Euler steps are 0.025 and 0.0125; a further 0.00625 branch
is allowed for failed numerical validity. Float32 is permitted only after
a float64 comparison of the same initialized models; all compared models
use the same runtime precision. Source assembly and metric checks use float64.

Primary accuracy is maximum-over-saved-times validation prediction RMS
against the same reference; endpoint RMS and time-average RMS are secondary.
The empirical dense-variability target is at most three times the corresponding
independent-dense RMS, plus improvement over the total-state-matched small
network. These are separate criteria, not a redefinition of the primary norm.
Every compared model must fit below 0.01 MSE. For each metric separately, the
sum of both models' step-refinement changes must be below 10 percent of the
corresponding dense-pair discrepancy; precision changes must be below that
same threshold. Failed gates make that metric inconclusive, not a success.
Predictions and source checks use all declared passive inputs without their
labels. Validation labels are only recorded for dataset provenance.

One source-step halving and one temporal-degree doubling are allowed to
resolve source numerical/temporal defects before freezing the pilot. Their
effects are checked separately from rank and selection. If the largest
pilot budget fails, retain the negative result and stop confirmation rather
than inventing a new architecture. At most 8 pilot assemblies, 36 training
runs, and 2 hours of total GPU wall time; every assembly or training operation
is capped at 300 seconds. Use both available RTX 3090 GPUs, one run per GPU.
Stop after the prescribed outcomes, even if no logarithmic empirical rule
succeeds. All failures and partial runs are retained in fresh directories.

Theoretical qualification remains unchanged: these practical label/data and
finite-precision choices do not invoke the small-label theorem. A successful
finite width grid supports a specified logarithmic budget rule; it cannot
establish the infinite-width exponent, the whole-sphere guarantee, or a new
all-time theorem. Fresh implementation and result checks are required before
calling the new empirical conclusion internally checked.

### Implementation checkpoint (before confirmation)

`panel-fit --source-mode rollout` now constructs piecewise Chebyshev sources
on `[0,1,2,4,8,16,32,64,100]`, using the actual dense nonlinear flow and
training-only gradients. It fits on even Chebyshev nodes, audits interlaced
odd nodes, residualizes only safe mandatory directions, and uses a seeded
randomized SVD before forming exact initialized image pairs. No dense/source
tensor survives in the autonomous deployment state. The summary's new
`--primary trajectory` option uses the prospective trajectory-RMS criterion;
the old endpoint-based summary remains reproducible by its default.

The independent scoped audit [ROLLOUT_IMPLEMENTATION_CHECK.md](ROLLOUT_IMPLEMENTATION_CHECK.md)
passes implementation hash
`d505c8c8df4d176afba2dda8a0366209f9635536b1b1f6872c4cf39aee4422ab`.
It tested heldout-value isolation, initialized two-way actions, restart at a
noninitial state, and zero-label/null-source robustness. The lead read the
full report. It is an internal implementation check, not a theorem audit or
empirical-results reproduction. Fresh standard tiny checks are in
`rollout_checks_v1/` and `rollout_checks_v2/` under the generated namespace.

Pilot results remain exploratory. At reference width 4096, seed 301,
Euler step 0.0125 through time 100, rank 32/budget 1024 gave maximum-time
RMS 0.02017, and rank 64/budget 1024 gave 0.01823. The latter's matched
small network gave 0.01672 and the iid dense reference gave 0.01284.
Rank 128/budget 1536 gave 0.01014 against a matched-small value 0.01668;
its endpoint 0.01014 was slightly worse than matched-small endpoint 0.00874.
All fit below 0.01 MSE. These numbers have not yet passed the final solver
refinement/precision gates or held-out-seed confirmation. They must not be
described as a confirmed scaling result. All corresponding `rollout_pilot_*`
directories are preserved. Dense float32 versus float64 at the identical
initialization/step changed maximum-time predictions by 1.36e-7; the panel
precision check remains pending at this checkpoint.

The first three pilot compilations used the initial source code revision;
their run report records the compiler hash, but their checkpoint predates the
explicit compiler-hash payload field. Restoring them correctly reports null
for that field rather than inventing provenance. Subsequent compilations
carry the hash and effective configuration in both checkpoint and report.

The source teacher may additionally use float32, followed by float64 source
assembly and metric construction. This is a precision implementation choice,
not a changed response family or budget rule. Before confirmation it must be
compared on pilot seed 301 against the already compiled float64-teacher model,
at the same RK4 step, temporal degree, rank and coordinate budget. Its effect
on model predictions is tested against the existing precision gate. This
check consumes the existing pilot/run budget; it does not add a new campaign.

### Frozen confirmation choices

After the prescribed pilot branches, freeze reference budget 1536 and optional
rank 128 at width 4096, scaled by `(log(en)/log(e*4096))^(5/2)`. Use temporal
degree eight per geometric interval, RK4 source step 0.25 through time 100,
float32 disposable source evolution, and float64 source/metric assembly.
Actual compared training uses float32 Euler at 0.0125 and 0.00625. The finer
pair is the predeclared resolution branch: pilot dense step 0.025 versus
0.0125 changed maximum-time predictions by 0.001554, too large for the
prospective trajectory gate. No gate is relaxed for confirmation.

Pilot precision checks found maximum-time differences 1.36e-7 for dense
float32 versus float64, 2.22e-6 for panel runtime float32 versus float64,
and 6.98e-7 for float32 versus float64 source evolution, all at identical
respective initializations and orders. Increasing temporal degree four to
eight reduced the largest heldout temporal RMS from 7.81e-4 to 7.92e-6;
halving the source RK4 step gave 7.46e-6. These are measured finite-source
checks, not a coordinate-uniform certificate. Float32 source evolution reduced
the final 4096-width setup from 62.8 seconds to 9.65 seconds.

The rule gives `(q, optional rank)` equal to `(1267,106)`, `(1536,128)`,
`(1838,154)`, `(2173,182)` at widths 2048, 4096, 8192, 16384. At 2048,
the full metric/state inventory `4q^2+65q+100` already exceeds the reference
`n^2+65n`; record a **noncompressing budget** without spending training runs
on that failed storage criterion. This is not an omitted favorable-width
selection. Confirm at 4096 and 8192, adding 16384 only under the recorded
8192 timing/memory condition. The existing 36-training-run cap has priority
over optional second-seed replication. All first-seed confirmation results
must be reported, even if they fail accuracy or numerical gates.

### Recorded confirmation outcome and numerical follow-up

The original frozen-resolution confirmation is preserved without changing its
gate: width 4096 passed, whereas width 8192 had promising model error but an
**inconclusive trajectory result** because the sum of separate Euler
refinement discrepancies exceeded 10 percent of its iid-dense discrepancy.
The endpoint diagnostic is distinct. Reports remain in the two
`rollout_confirm_n*_summary_v1/` directories and are never overwritten.

For the user's request to test the construction as well as practicable, the
remaining eight training runs are reassigned from the optional width-16384
extension to a separately labeled numerical follow-up: rerun all four models
at each of 4096 and 8192 with step 0.003125, reusing the identical compiled
checkpoints, data, seeds, source budgets and horizon. This is an explicit
post-confirmation resolution amendment, not an originally preregistered pass
or a new search for favorable model orders. All accuracy/validity thresholds
stay unchanged, the initial inconclusive outcome is retained, and the hard
36-training-run and 300-second per-run caps remain. No claim of width-16384
accuracy or second-seed confirmation will be made. If this follow-up still
fails a gate, the remaining result is reported as inconclusive and stops.

### Completed rollout experiment: results and interpretation

All 36 allowed training runs completed: 12 exploratory pilot runs, 16 initial
confirmation runs and eight separately recorded finer-resolution follow-up
runs. There were six pilot source compilations and two confirmation source
compilations. No width-16384 or second-confirmation-seed run was performed.
The final implementation is commit `4d23438`, source SHA256
`3ad9b8bfe43c42fccca1e752c2aa0759ee2c98c3b1ec2a4313dc4c491e526eff`.
The initial implementation was committed separately as `0bcf836`.

The final experiment is raw sklearn digits 3 versus 8, 64 pixel coordinates,
100 training images and all 257 remaining images as a predeclared passive
panel. No PCA is used. Passive labels never enter compilation or dynamics.
The network has two hidden tanh layers, canonical mobilities, zero readout
and label RMS one. Setup/reference, iid-dense and small-dense seeds are 401,
10401 and 20401. Pilot seed 301 is distinct. All four models use float32
Euler at step 0.003125 through physical time 100: 32,000 updates, not a
two-step experiment. Predictions are recorded at 201 common times, spaced
by 0.5. The panel uses the study's corrected nonlinear optimizer, not an
ordinary smaller network's gradient flow.

The coordinate budget is frozen before the confirmation runs:

\[
q(n)=\left\lceil1536
 \left(\frac{\log(en)}{\log(e\,4096)}\right)^{5/2}\right\rceil.
\]

The optional source rank uses the same rule with 128 replacing 1536.
Thus `(q, optional rank)` is `(1536,128)` at 4096 and `(1838,154)` at
8192. The actual assembled source ranks are `(549,585)` and `(627,663)`.
The runtime has four moving arrays and three fixed arrays: first weights,
readout, hidden mixer, training deficit, two metrics and an incoming metric
inverse. Its complete deployable model inventory is

\[
q^2+65q+100\ \text{moving numbers},\qquad
3q^2\ \text{fixed numbers},\qquad
4q^2+65q+100\ \text{total numbers}.
\]

The same data add 22,948 numbers to every model. Counts exclude benchmark
restart copies, saved output histories and execution workspaces; measured
process peaks below include those allocations. For fixed panel size and
dimension the runtime buffers also grow at most quadratically in q, but
the displayed exact number is model storage, not peak execution storage.
The budget law proves a storage-growth statement, **not** preservation of
accuracy at every larger width.

The primary error is the maximum, over the 201 saved times, of prediction
RMS across all 257 validation images against the same dense reference.
These are prediction discrepancies, not classification accuracies.

| Dense width | Model | Total model numbers | Final training MSE | Maximum-time validation RMS | Time-average validation RMS | Endpoint validation RMS |
|---:|---|---:|---:|---:|---:|---:|
| 4096 | Independent dense | 17,043,456 | 0.00297243 | 0.02080351 | 0.00784317 | 0.00687829 |
| 4096 | Rollout panel | 9,537,124 | 0.00235681 | 0.00698120 | 0.00509722 | 0.00698120 |
| 4096 | Matched dense, width 3055 | 9,531,600 | 0.00303269 | 0.02587738 | 0.00923382 | 0.00856915 |
| 8192 | Independent dense | 67,641,344 | 0.00305818 | 0.01163048 | 0.00622576 | 0.00623520 |
| 8192 | Rollout panel | 13,632,546 | 0.00233783 | 0.00805827 | 0.00565780 | 0.00805827 |
| 8192 | Matched dense, width 3659 | 13,626,116 | 0.00298448 | 0.01069626 | 0.00692150 | 0.00672397 |

The reference dense training MSEs are 0.00293098 and 0.00291327. All eight
final models fit below 0.01. The time-average column integrates the RMS
curve, not its square. Panel maximum-time RMS is 0.336 and 0.693 times the
actual respective iid-dense discrepancy, below the declared factor-three
target. It also beats the matched small control at both widths on that
primary statistic. At 8192 it **does not beat the small model at the
endpoint**; no blanket endpoint-superiority claim is made. Even the matched
small control satisfies the factor-three variability target on this dataset,
so passing that target alone is not distinctive evidence for this method.

As a secondary, post-hoc diagnostic closer to pointwise error, the maximum
absolute discrepancy across all saved times and all validation images is:

| Dense width | Independent dense | Rollout panel | Matched small dense |
|---:|---:|---:|---:|
| 4096 | 0.04142284 | 0.02654889 | 0.05446383 |
| 8192 | 0.04026198 | 0.03645322 | 0.04994781 |

This does not replace the primary RMS criterion and is not a continuous-time
supremum certificate. Only endpoint training predictions, rather than their
full trajectory, are saved, so this secondary table is specifically the
validation subset, not the entire 357-point panel.

### Numerical checks, initialization work and runtime costs

The unchanged trajectory gate requires the sum of both models' measured
step-refinement RMS maxima to be below ten percent of the iid-dense RMS
maximum. The endpoint gate is evaluated separately against ten percent of
the iid-dense endpoint RMS. At the finer follow-up resolution all three
comparisons (panel, iid and small, each versus the reference) pass both
gates. For the panel comparison:

| Dense width | Trajectory refinement sum | Trajectory threshold | Endpoint refinement sum | Endpoint threshold |
|---:|---:|---:|---:|---:|
| 4096 | 0.00103367 | 0.00208035 | 0.00023780 | 0.00068783 |
| 8192 | 0.00103638 | 0.00116305 | 0.00021721 | 0.00062352 |

These are measured refinement diagnostics, not rigorous bounds on exact
gradient-flow error. The originally frozen 8192-resolution trajectory gate
failed; the separately disclosed follow-up resolved it without changing
orders, seeds, models, horizon, checkpoints or thresholds. Pilot precision
checks support the precision choice, but are not direct float64 replications
of the final 8192/finer-step experiment. Some pilot comparisons span compiler
hashes as precision/configuration plumbing changed; this provenance
qualification remains explicit in the independent raw-results check.

Compilation uses eight geometric time intervals with boundaries
`0,1,2,4,8,16,32,64,100`, degree-eight Chebyshev fits, and 129 distinct
observation times. Odd interlaced nodes are held out from fitting. The
disposable RK4 solve takes 470 steps, hence 1880 dense training RHS calls,
versus 32,000 Euler updates in each final comparison. It covers the **full
physical interval**, not a short initial window. The sources are forward
responses on the full panel and backward responses on training inputs only.
Rank compression is applied before forming their exact initialized matrix
images. Four fixed-seed coordinate candidates are compared by source-metric
conditioning, never by validation predictions or labels. Assembly is float64;
the disposable solve and the compared training runs are float32, with TF32
disabled. Dense state, source coefficients and observations are discarded
after compilation; the seven-tensor deployment checkpoint has no history.

Both RTX 3090 GPUs were used, with no overlapping training jobs on the same
GPU. All individual training and source-compilation runs stayed below their
300-second limit. The final timings and peak allocated CUDA memory are:

| Operation | Dense width 4096 | Dense width 8192 |
|---|---:|---:|
| Original panel compilation time | 9.65 s | 21.31 s |
| Compilation process peak | 7.20 GiB | 14.59 GiB |
| Dense reference full Euler run | 42.32 s | 120.04 s |
| Panel full Euler run, excluding compilation | 114.10 s | 112.57 s |
| Matched small full Euler run | 37.61 s | 38.00 s |
| Dense run process peak | 274.12 MiB | 996.15 MiB |
| Panel run process peak | 93.60 MiB | 120.44 MiB |
| Matched small run process peak | 168.11 MiB | 225.43 MiB |

The peaks are allocator/process measurements including benchmark restart
copies and temporaries, not device-wide memory or a minimal implementation
bound. Run wall times include loss checks and sparse queries. The summary
field `training_seconds` is that whole-run time; each raw report separately
records the training-only, loss-check, query and readout-refresh times.
Checkpoint-loading time is not compilation cost. This implementation gives
a memory reduction, **not an end-to-end speedup**: setup plus training is
slower than the Euler dense reference at both widths. Nor is this a benchmark
against the fastest possible dense solver; dense could also use RK4.

### Scope of the evidence and reproducibility

This practical method preserves the nonlinear corrected runtime, paired
initialized actions, exact selected-source isometry, passive-label isolation
and restartability. It does not certify the theorem's complete source
approximation or selector constants. The measured metric factors are
10.50/11.01 and 12.80/13.34, not four. The largest sampled source-projection
RMS is about 0.0973 and 0.0861, so these experiments do not establish the
theorem's uniform vanishing source-error requirement. Degree-eight temporal
heldout RMS is below 7.4e-6 for these two sources, but that does not remove
the rank-truncation error. Label RMS one and the rank-50 training-input
matrix in 64 raw dimensions also do not meet the original certificate's
small-label/full-span hypotheses. Those qualifications have not been erased
to call the experiment a theorem test.

Accordingly, the result is an empirically successful architecture-faithful
variant under a fixed log-fifth-power budget, **not** a new unconditional
log-fifth-power theorem for that variant, arbitrary future queries, all
continuous times or the fitted infinite-time endpoint. Two widths and one
confirmation seed cannot identify an asymptotic exponent or success
probability. At width 2048 the same rule is noncompressing. No low-rank,
lazy-feature or equal-budget jet-only ablation was added in this bounded
campaign, so the improvement cannot be attributed to the rollout alone
rather than the larger source ranks and changed coordinate selector.

The independent scoped implementation check is
[ROLLOUT_IMPLEMENTATION_CHECK.md](ROLLOUT_IMPLEMENTATION_CHECK.md).
The independent raw-result reconstruction is
[ROLLOUT_RESULTS_CHECK.md](ROLLOUT_RESULTS_CHECK.md); it checks data/seed/
solver compatibility, checkpoint tensor inventory, measured costs and all
comparisons directly from the saved arrays. These are internal checks, not
promotion reviews or theoretical certificates. No paper or theorem is
changed by this empirical continuation.

All generated evidence is under
`data/generated/finite_panel_absolute_compression_20261005/`:

- `rollout_pilot_*`: every pilot, including unfavorable branches;
- `rollout_confirm_n{4096,8192}_setup_v1/`: original compilation reports and
  the immutable compiled checkpoints;
- `rollout_confirm_n{4096,8192}_{dense,iid,panel,small}_h{0.0125,0.00625}_v1/`:
  all original confirmation trajectories;
- `rollout_confirm_n{4096,8192}_summary_v1/`: original pass/failure outcomes;
- `rollout_followup_n{4096,8192}_{dense,iid,panel,small}_h0003125_v1/`:
  all eight finer-resolution trajectories;
- `rollout_followup_n{4096,8192}_summary_v1/`: final comparisons.

Each run report contains its exact command, configuration, initialization,
data and source hashes, versions, elapsed costs and stopping reason. Final
summary SHA256 values, for 4096 then 8192, are
`f6b85770264011be105f9597d34c1542ae8e35823c4cefe80f7a30b5bf98938e` and
`b23a7936a54d570a8d54ad81d8ce3ae4d6d7339439a86738fc8aafede7b301a5`.
The following reconstructs each final summary into a fresh output directory;
use the recorded run commands with fresh outputs for a new training rerun:

```bash
experiment_root=data/generated/finite_panel_absolute_compression_20261005
for n in 4096 8192; do
  summary_args=()
  for model in dense iid panel small; do
    summary_args+=("--$model" "$experiment_root/rollout_followup_n${n}_${model}_h0003125_v1")
    summary_args+=("--$model-coarse" "$experiment_root/rollout_confirm_n${n}_${model}_h0.00625_v1")
  done
  /home/amir/Codes/sber-swap/.venv/bin/python -B paper/figures/capture_trajectory.py \
    panel-summary --primary trajectory "${summary_args[@]}" \
    --out "$experiment_root/rollout_followup_n${n}_summary_reproduction"
done
```
