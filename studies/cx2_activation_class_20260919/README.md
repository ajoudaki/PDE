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

## Revised contract: activation extensions of C-H3 and C-H4

On 2026-09-19 the user explicitly resumed this study with a revised target.
The original full-class substantial-training target below remains preserved,
but its unbounded long-horizon requirement is no longer a completion condition
for this revised package. Current work starts from commit
`78119b1f32cb472e86ebc446b31d5dc6a62172ed` with this study and the index clean;
unrelated existing checkout changes remain untouched.

The common exact model, initialization, loss, physical metric, Gaussian action,
finite random readout and observable conventions below are retained. Complete
the following two separate results, without changing activation or data with
width, hierarchy order or numerical resolution:

1. **C-H3 extension.** For every separately fixed phi in A, prove a positive
   physical interval `[0,T_phi^local]` independent of resolution and data within
   the stated bounded-label domain. Include at least the entire represented
   C-H3 rational two-arc family (normalized cross-component inner products
   between 2/5 and 4/5, weights between 1/3 and 2/3), not only a near-orthogonal
   family. Seek the underlying population construction for every Borel law
   on `sqrt(2) S^1 x [-1,1]`, as in C-H3. Prove the compatible hierarchy and
   separate numerical limits, whole-circle predictions and paired observations.
   This assertion requires no substantial loss reduction or universal activity
   for arbitrary laws (for example, zero-label laws can be stationary).
2. **C-H4 extension.** For every bounded phi in A, prove a fixed positive
   perturbation radius around the opposite-label orthogonal pair and a finite
   activation-dependent substantial-training horizon. The family must contain
   nonorthogonal pairs; retain supported represented two-arc/nonatomic laws
   where the same construction permits, to preserve C-H4's computational scope.
   Prove strong actual population construction, loss at most 1/4 from initial
   loss one, early positive paired hidden activity/nonaffinity, and hierarchy
   and numerical convergence through the whole learning interval. Boundedness
   does not impose oddness, monotonicity, analyticity or nonzero gates. A global
   exactly orthogonal reference alone does not complete this assertion.

Both parts require an executable reusable closure under explicit locally
consistent activation/derivative evaluation interfaces; arbitrary C1,1 functions
need not be computable. Any narrower required regularity must be reported as a
gap, not silently substituted. Qualitative iterated limits suffice; no rate,
arbitrary diagonal, tolerance selector or cost-to-accuracy theorem is required.
No new neural training campaign or established-book/code promotion is authorized.

The supervisor has read C-X1 only to answer the user's separate read-only
question about its scope. That exposure is not authority to import its
unpromoted proofs or code here. All new delegated routes start fresh and use
only the permitted C-X2 and maintained inputs specified in their assignments.

## Original contract and selected data scope

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

## Revised contract resolved: exact scope and complete audits

The assembled result is [REVISED_RESULT.md](REVISED_RESULT.md). Complete new
arguments are in [ONSET_EXTENSION.md](ONSET_EXTENSION.md),
[COMMUTATOR_RESPONSE.md](COMMUTATOR_RESPONSE.md), and
[BOUNDED_EXTENSION.md](BOUNDED_EXTENSION.md). The reviewed conclusions are:

- Full A, every Borel circle/bounded-label training law, on a common positive
  activation-dependent onset interval; the full C-H3 represented family is
  included.
- Bounded A, opposite-label two-point data in a fixed positive neighborhood
  of the orthogonal pair, through substantial training and a whole-circle
  reference-endpoint comparison. The neighborhood is fixed before all limits.
- Bounded C2 with bounded second derivative, additionally supported Borel
  and nonatomic near-orthogonal input families through that horizon.

Both complete isolated internal audits accepted this exact scope without
required corrections: [review A](EXTENSION_REVIEW_R1_A.md) and
[review B](EXTENSION_REVIEW_R1_B.md). The supervisor personally read both full
reports and verified every input hash, before/after check, evidence hash,
test record and exact correspondence with the live proofs and dependencies.
The complete decision and reproducibility record is
[EXTENSION_REVIEW_RESOLUTION.md](EXTENSION_REVIEW_RESOLUTION.md).
The frozen manuscripts retain their pre-audit candidate headers byte-for-byte;
this README and that record state the subsequent review outcome.

The neutral assignment is [EXTENSION_R1_ASSIGNMENT.md](EXTENSION_R1_ASSIGNMENT.md);
the complete frozen input manifest is [EXTENSION_R1_INPUTS.json](EXTENSION_R1_INPUTS.json).
The packet contains thirty files and 16,155 lines. The supervisor verified
all hashes, exact live correspondence and complete excerpt boundaries before
launching both reviewers. Scoped author checks are retained separately in
[ONSET_AUTHOR_CHECK.md](ONSET_AUTHOR_CHECK.md) and
[TANGENT_PARITY_CHECK.md](TANGENT_PARITY_CHECK.md); reviewers do not receive
these checks or prior verdicts.

The reviewed implementation and its numerical consistency argument are in
[NUMERICAL_EXTENSION.md](NUMERICAL_EXTENSION.md), with source
[activation_closure.py](activation_closure.py). All eight preregistered
supplied-state checks passed; the plan, exact commands and evidence are
linked there. No training experiment ran. This implementation alone supplies
neither a target-existence theorem nor fitting-neighborhood tails; those are
separate conclusions of the new mathematical manuscripts. Each fresh reviewer
independently reproduced the same eight checks from the frozen implementation.
The earlier reviews below were not used to accept the extension by association.

The revised primary contract is complete. General unbounded-activation fitting
and bounded-C1,1 nonatomic fitting remain open, separately from the proved
bounded-C1,1 pair and bounded-C2 supported-law results. The changed-law theorem
is through a fixed finite substantial-training horizon; only the orthogonal
reference is global in time. No hierarchy-order rate or practical accuracy
certificate is supplied. Established book/code promotion remains on standby,
and no maintained file has been edited. Do not reopen the excluded extensions
without a new user direction.

## Earlier partial result and exact gap (before the revised contract)

The original full-class substantial-training package was **not resolved** at
this earlier checkpoint. Its reviewed partial result is
[PARTIAL_RESULT.md](PARTIAL_RESULT.md), with complete
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
package supported its principal conclusions with two narrow corrections.
Those corrections are applied; two fresh complete reviews of the corrected
packet both accept the exact partial and conditional results, with no
required corrections. The supervisor read both complete reports, verified
all input and evidence hashes, and checked exact live-file correspondence.
Assignments, manifests, full reports, objections
and verified evidence are indexed in [REVIEW_RESOLUTION.md](REVIEW_RESOLUTION.md).
The additional prompt-only route is outside the frozen review scope and
must not acquire these verdicts by association. The first scoped commit is
`6a39978fd161a12de3ae410bfaefad878251ea7b`.

The supplied-state validation [check_identities.py](check_identities.py)
passed both tests (each across four activation choices), checking exact
symmetry and the radial feature-ascent metric identities against the finite
reference API and independent directional differences. No training experiment
was run. At this checkpoint a general-activation executable closure solver
had not been built; the numerical consistency theorem specified the necessary activation
evaluation interface rather than claiming an implementation for arbitrary
noncomputable functions.

The outstanding obligations then were unbounded reference continuation,
uniform reached tails, a positive correlated-input fitting neighborhood and
the executable implementation. The later revised-contract result above supplies
the bounded-activation fitting neighborhood and general executable hierarchy;
it does not settle unbounded substantial training. The failed ambient
Lipschitz, energy-only and uncontrolled reinsertion inferences remain invalid.
No established promotion is authorized by the current research request.
