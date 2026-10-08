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
