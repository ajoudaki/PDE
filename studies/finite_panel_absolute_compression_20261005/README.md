# Absolute logarithmic exponent for a predeclared passive test panel

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
