# C-X1: many-point nonlinear observable closure

Opened 2026-09-19 at the user's explicit request to conduct and prove C-X1.
Initial HEAD: `019e3630237e33f58b9636c0aa67a039bebf0182`; the Git index was
empty. Pre-existing modifications and untracked studies are unrelated and
must be preserved. This task is the sole Git writer for this study.

## Frozen research contract

For every separately fixed integer `1 <= m <= d`, binary labels
`y_a in {-1,+1}`, and normalized inputs `u_a in S^(d-1)` sufficiently close
to the distinct coordinate vectors `e_a`, study two tanh hidden layers with
canonical independent stored Gaussian variances `(1,1/n,1/n^2)`, output
`c^T h2/n`, physical mobilities `(n,1,n)`, and unhalved **mean** squared loss.
The finite random readout is retained. The full first-row field and the
actual Gaussian middle action and its adjoint are retained.

The required result supplies a positive geometric radius and finite physical
learning horizon (allowed to depend on fixed m,d, independent of width and
every approximation resolution), canonical strong population dynamics and
finite-network capture through that horizon, final loss at most 1/4, positive
paired motion in both hidden layers at a specified positive time, and an
autonomous restartable finite observable hierarchy with qualitative numerical
and order convergence in whole-sphere prediction and declared joint hidden /
action observations. A short-time theorem or a conditional source-tail bound
alone does not resolve C-X1. No growing-m/d limit, approximation-order rate,
automatic accuracy certificate, all-time perturbed-law theorem or model
superiority is required. An actual raw-GD bridge must state and prove its
step condition; finite GF and numerical ODE integration remain distinct.

Primary data are equal-weight finite point configurations. Explicit supported
nonatomic families are a strengthening only if justified without displacing
the required finite-data result. Numerical closure state size may depend on
fixed dimension and order, not on neural width or elapsed training steps.
Coefficients must be obtained from initialization, not fitted trajectories.

## Scope and evidence

Scientific inputs: this study and established `docs/` and `code/`, with their
designated reproduction inputs. Other studies and their unpromoted findings
are not inputs. Required skills are `solve-math-rigorously` and
`investigate-conjectures`. Full independent review is required before calling
the package established; promotion additionally requires explicit approval
of the concrete reviewed book/code addition.

Current status: C-X1 resolved as an independently reviewed study. Both fresh
complete scientific reviews accepted every theorem conclusion, and the separate
integration/reproduction review passed its assigned scope. No scientific
correction remains required; no book/code promotion has occurred. THEOREM.md states the
assembled result: T=5m, explicit positive geometric radius, risk below 9/64,
both-layer paired motion and visited-law nonaffinity, actual finite GF and
raw GD with eta_n->0, and the dense hierarchy's qualitative numerical limits.
The perturbed source/tail obligation is proved rather than left as an
assumption. REVIEW_COMPLETION.md records complete reports, hash verification,
validation and precise acceptance limits. Pre-review status sentences in the
frozen theorem/proof units are retained as historical packet metadata; this
README and the completion record give their current review status.

No training campaign is authorized by this record. Deterministic verification
of the construction and code is within scope. Any bounded numerical validation
will receive a recorded purpose, configuration, resource cap, and fresh output
directory before execution. Generated files belong exclusively to
`data/generated/cx1_many_point_closure_20260919/`.

## Ownership and routes

- Supervisor owns this README, THEOREM.md, ASSEMBLY_PROOF.md, validation,
  FINITE_CAPTURE_PROOF.md, final theorem assembly, integration and Git.
- `cx1_reference` owns REFERENCE_PROOF.md. Its isolated scope is the exact
  orthogonal reference and positive paired activity.
- `cx1_perturbation` owns PERTURBATION_PROOF.md. Its isolated scope is
  reached-source control, perturbation continuation and finite capture.
- `cx1_closure` owns CX1_CLOSURE_PROOF.md, cx1_closure.py and
  test_cx1_closure.py. Its isolated scope is general-dimensional closure,
  numerical consistency and implementation, conditional on the named target
  flow/tail interface until that interface is independently proved.
- Independent proof routes start in fresh contexts and do not read each
  other's outputs until frozen. Reviewers receive complete frozen inputs
  without author history or earlier verdicts.

## Frozen inputs and next gate

REVIEW_INPUTS_R1.json freezes all scientific inputs for the complete reviews.
REVIEW_DEPENDENCY_SUPPLEMENT_R1.json additionally freezes the package initializer
and its two eager imports, completing the runtime dependency inventory without
changing the original candidate. Both manifests are supplied to all reviewers.
These inputs remain unchanged after review. Any later scientific correction
requires a new frozen edition and fresh complete review. Maintained book/code
changes still require a concrete reviewed promotion package and explicit user
approval. Such a package has not been applied by this task. Other axes
(activation, depth, architecture) are not part of this study.

Notation clarification: the normalized prediction written f_n(u) in THEOREM.md
is the physical-input prediction f_n(sqrt(d)u) in the reference and finite-capture
units. The executable always receives normalized unit directions u.

## Proof and executable map

- REFERENCE_PROOF.md: mixed-label signed symmetry, autonomous global reference,
  strict learning at 5m, specified paired activity/nonaffinity time and finite
  reference comparison.
- PERTURBATION_PROOF.md: independent clock source anchor, raw-reference transfer,
  supported-input source bootstrap, explicit radius and strong continuation.
- FINITE_CAPTURE_PROOF.md: fixed-proxy identification of actual finite GF/GD,
  including the random readout and precise order of probability/mesh limits.
- CX1_CLOSURE_PROOF.md and cx1_closure.py: full current hierarchy, dense finite
  closures, numerical consistency, restart and operation/bit/storage accounting.
- ASSEMBLY_PROOF.md: explicit final radius and transfer of all strict margins.
- VALIDATION.md and VALIDATION_PLAN.md: exact checks, bounded numerical runs,
  reproducibility and their accuracy limitations.

Earlier component screening is preserved in RELEVANCE_REVIEW.md and
IMPLEMENTATION_AUDIT.md. The latter identified an executable recursion ceiling;
REVIEW_CORRECTIONS.md records its iterative repair and required fresh review.
These prior reports are excluded from fresh reviewers' inputs. Seven semantic
tests and the five bounded operational runs pass on the corrected module;
no finite-resolution accuracy or practical radius claim follows from them.

Final reviews: SCIENTIFIC_REVIEW_R1_A.md, SCIENTIFIC_REVIEW_R1_B.md and
INTEGRATION_REVIEW_R1.md. Review A independently reran all seven semantic tests;
review B independently checked the exact certificate, all 43 moving-coordinate
gradients of a supplied state, energy and weighted adjunction. The integration
review reran the five declared operational configurations, reproducing every
reported numerical value and all ten checkpoint/observation hashes exactly.
The final-source fresh-directory initialization check in standalone_02 also
passed and fingerprints every loaded project module against the two manifests.

Scoped commits so far: 60ba365 (contract), 4c4bef5 (conditional closure and
validation), 07e627a (complete frozen candidate). Generated outputs remain
separate and are not committed.

## Checks completed during authoring

The unchanged exact rational Gaussian certificate from maintained C.4.5.1
was extracted as `check_reference_constants.py` and executed with Python
3.10.12, exit zero, in 3.272 seconds. Its exact assertions give
`0.39 < E tanh(G)^2 < 0.4`, the needed upper-feature variance `v>1/5`,
and the two positive gate-moment bounds. It is constant verification, not a
training experiment or a check of the new continuation proof.

Reproduce: `python -B studies/cx1_many_point_closure_20260919/check_reference_constants.py`
from the repository root. Source SHA256:
`1dd6ae76d2b20d3878658d5fb1b5e0d3e94bbed91ea3a855134a536cc5073867`.
The command, output and environment record are in
`data/generated/cx1_many_point_closure_20260919/reference_constants_01/`.
The source and complete maintained analytic certificate, not these generated
outputs, carry the proof dependency.
