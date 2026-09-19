# C-X2: smooth bounded-slope activation class

Opened 2026-09-19 at the user's request to conduct and resolve C-X2 for

`A = {phi in C^{1,1}(R): ||phi'||_infinity < infinity, phi nonaffine}`.

The derivative is globally Lipschitz. The same separately fixed activation
is used in both hidden layers. Boundedness, oddness, monotonicity, a positive
gate and analyticity are not assumptions. Constants may depend on the fixed
activation; no uniform horizon over arbitrarily small gains is requested.
Exact ReLU and derivative-jump activations are outside this package.

Initial checkout HEAD: c809bffe50488e7c3ca2667ce0a7dee73040ae03. The shared
Git index was empty. Pre-existing modifications and other untracked studies
are unrelated and must be preserved. The supervisor is this study's sole
Git writer and uses the common writer lock for scoped commits.

## Contract and selected data scope

Retain the bias-free two-hidden-layer model, independent stored Gaussian
variances `(1,1/n,1/n^2)`, physical mobilities `(n,1,n)`, output `c^T h2/n`,
and unhalved mean squared loss. Finite random readout is retained; only the
population initial readout is zero. Retain the full first-row field and the
actual Gaussian action with its adjoint; only the learned increment is HS.

Completion requires a unique autonomous canonical population flow through a
positive substantial-learning horizon, actual finite GF and a justified raw
GD bridge, training loss at most 1/4 from initial loss one, positive paired
motion and visited-law nonaffinity in both layers, and an autonomous finite
observable hierarchy with numerical and order convergence to that same flow.
The numerical state must not accumulate history or scale with neural width.
Whole-input prediction and fixed same-population joint observations, including
initial/current hidden pairs, must retain their precise convergence scopes.
No approximation-order rate, arbitrary refinement diagonal, or practical
cost-to-accuracy certificate is required.

The user explicitly delegated the data-scope choice, authorizing two inputs
if that helps the proof. The supervisor selects the original two-anchor
opposite-label setting, because swapping the two anchors and negating the
readout preserves its reference symmetry for nonodd activations. Normalized
inputs lie on S^1 near e_1,e_2; physical inputs are sqrt(2) times these unit
directions, with labels (+1,-1) and weights (1/2,1/2). The neighborhood and
learning horizon may depend on phi but are fixed before width, order and
numerical limits. The primary contract includes genuinely nonorthogonal
two-point configurations. Supported nonatomic families are a strengthening,
not a replacement for this finite-data claim. The wider-data combination
remains a later distinct package.

The maintained original reference has labels (+1,-1), not (+1,+1). The latter
was mistakenly named in the initial route assignments; the supervisor corrected
all three assignments before any claimed result. Opposite labels remain the
primary two-anchor contract. Swapping the two first-row coordinates while
negating the readout is a candidate nonodd symmetry, to be proved here.

## Scientific boundary

Inputs are this study and the established docs/code with their designated
reproduction inputs. No other study's unpromoted proof, code, arrays, verdicts
or summaries are scientific dependencies. C-X1 promotion remains on standby.
The supervisor necessarily remembers prior conversation, but the new proof
routes start in fresh contexts using only their explicit maintained inputs.
Any needed statement must be derived here from those permitted inputs.

Required skills: solve-math-rigorously and investigate-conjectures. External
specialized theorems require full checked statements/proofs/dependencies.
No training campaign is authorized. Ordinary deterministic verification of
the requested method is allowed; any bounded numerical validation requires
a predeclared purpose, configuration and resource limits. Generated products
belong under data/generated/cx2_activation_class_20260919/.

## First proof routes and ownership

- Supervisor: contract, synthesis, strong comparison/finite capture, shared
  notes, final assembly, validation, reviews and Git.
- Reference route: nonodd opposite-label orthogonal reference, fitting-time
  reduction, precise continuation interface and initial activity.
- Source route: global-reference/reached source and tail control for unbounded
  C1,1 activations, and perturbative continuation to correlated inputs.
- Closure route: generic activation hierarchy and closure convergence under
  explicit target hypotheses, including unbounded fields and only C1,1
  regularity. Conditional progress is not completion of C-X2.

Each route uses a separate flat file, does not read another active route, and
must return complete derivations, exact dependencies, counterchecks and any
unresolved implication. Complete candidates require fresh isolated reviews.
Maintained book/code files remain unchanged without the separate promotion
gate and explicit user approval.

## Current result and exact gap

The full requested C-X2 package is **not resolved**. The current author
candidate is [PARTIAL_RESULT.md](PARTIAL_RESULT.md), with complete new
arguments in [REFERENCE_PROOF.md](REFERENCE_PROOF.md),
[CLOSURE_PROOF.md](CLOSURE_PROOF.md), and
[SOURCE_PROOF.md](SOURCE_PROOF.md).

- The full activation class has an autonomous dense observable closure
  converging to the actual neural population flow on the established positive
  local interval. This includes both hidden-layer activation displacements,
  whole-circle predictions, actual finite GF/GD and the stated separate
  numerical limits. It is not a substantial-learning-horizon theorem.
- The opposite-label symmetry and radial readout convexity prove the exact
  fitting estimate `L(t)<=exp(-4*q0*t)` on every strong symmetric reference
  interval, with an explicit positive initialization expectation `q0`.
  B.1 makes this an unconditional global orthogonal reference theorem for
  the bounded subclass, including nonodd/nonmonotone activations.
- Dense closure on longer intervals and finite neural capture follow from
  explicit strong-target and exponential-tail premises. Those premises have
  not been proved through the fitting horizon for all unbounded activations.
- The source route, bounded-activation truncation, feature-energy route and
  row-removal route leave explicit reached-source estimates unproved.
  An additional fresh prompt-only attempt is retained in
  [ALTERNATIVE_PROOF.md](ALTERNATIVE_PROOF.md); it proves a strong endpoint
  and an integrated-forward-source reduction but does not close continuation.
- The raw/clock Hilbert local-Lipschitz shortcut actually fails at the first
  Euler state for `phi(z)=z+epsilon*sin(z)`. This is a proof-tool obstruction,
  not a counterexample to the requested neural theorem.

Two complete isolated internal scientific reviews of the frozen partial
package are in progress. Their assignments and input hashes are retained in
`REVIEW_R1_ASSIGNMENT_A.txt`, `REVIEW_R1_ASSIGNMENT_B.txt`, and
`REVIEW_R1_INPUTS.json`. The additional prompt-only route is outside that
frozen review scope and must not acquire their verdict by association.

The supplied-state validation [check_identities.py](check_identities.py)
passed both tests (each across four activation choices), checking exact
symmetry and the radial feature-ascent metric identities against the finite
reference API and independent directional differences. No training experiment
was run. A general-activation executable closure solver has not been built;
the numerical consistency theorem specifies the necessary activation
evaluation interface rather than claiming an implementation for arbitrary
noncomputable functions.

Remaining substantive requirements are unbounded reference continuation,
uniform reached-tail construction, transfer to a positive correlated-input
neighborhood through fitting, and the general-activation implementation.
Neither a conditional theorem nor a documented deferral completes C-X2.
The next authorized work is to resolve review objections and preserve the
proved partials, then pursue the explicitly identified source estimate only
if a mathematically new route is available. No established promotion is
authorized by the current research request.
