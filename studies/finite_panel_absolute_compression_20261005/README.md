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
