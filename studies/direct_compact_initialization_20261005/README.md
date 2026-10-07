# Direct compact initialization without a dense intermediate

Started 2026-10-05. This is a new investigation, distinct from realization-dependent compression. The root agent owns this README and synthesis; scoped agents own separately assigned flat proof files. No shared book/code changes, Git mutations, or training experiments are planned.

## Contract

Construct a finite autonomous model from the dataset, architecture and Gaussian initialization law, reference width `n` or accuracy, and optionally independent randomness. Neither initialization nor runtime may construct a realized width-`n` network, query its trajectory, use population-response oracles, or hide such information in coefficients. Count moving and fixed retained coordinates separately and state initialization and runtime costs.

The reference has two tanh hidden layers, `h(x)=tanh(Ax/sqrt(d))`, `g(x)=tanh(W h(x))`, `f_n(x)=w^T g(x)/n`; independent `A_ij~N(0,1)`, `W_ij~N(0,1/n)`, `w=0`; squared mean loss and block mobilities `(n,1,n)`. Initially use `m` orthogonal sphere inputs of radius `sqrt(d)` and sufficiently small fixed signed labels. Keep nonlinear feature learning and compare at the same physical time, including the endpoint, uniformly on the entire sphere.

The target is probability at least `1-delta` of error at most `C_data,delta/sqrt(n)` against an independent fresh reference initialization, with polylogarithmic retained storage. A weaker rate, finite-time result, endpoint-only result, or conditional implication does not resolve this target and must be labeled separately.

## Authorized inputs and status

Scientific inputs are the maintained `docs/` and the five notes explicitly authorized in the user assignment, including their relevant proof/correction dependencies: `closure_sampling_20261003/{STORAGE_QUADRATIC_IMPROVEMENT,SPHERICAL_SOURCE_DIMENSION_ROUTE,ERROR_PREFACTOR_GEOMETRIC_ROUTE}.md`, `integrated_general_compression_20261004/README.md`, and `orthogonal_tanh_time_legendre_20261005/README.md`. Other studies, including similarly named concurrent work, are not inputs. Conversation recollections are not theorem dependencies.

Startup: current AGENTS and RESEARCH_WORKFLOW Part 1 read; investigation and rigorous-math skills used; canonical-notation skill at the prescribed path is inaccessible (permission denied), so explicit user rules and `docs/notation.qmd` govern presentation. Initial HEAD `3834145d910202a84824d943fe7d7f65714d96f2`; index empty; unrelated concurrent modifications preserved.

## Current conclusion

The requested strict root-width accuracy with direct polylogarithmic storage
remains **open**, but direct construction at the old retained size now has
an internally checked constructive reduction in
[DIRECT_CERTIFIED_CONSTRUCTION.md](DIRECT_CERTIFIED_CONSTRUCTION.md).
It constructs rational initial weights and metrics from the data and the
finite-width Gaussian law, without a realized dense network, using the
actual nonlinear corrected compact optimizer. It keeps
`O(log(en)^(3d+2))` retained real coordinates and compares to an independent
fresh dense run over the full physical trajectory, sphere, and fitted
endpoint. For orthogonal two-layer tanh data the improved corollary is
`C_data,delta log(en)/sqrt(n)`, proved in
[DIRECT_ORTHOGONAL_COROLLARY.md](DIRECT_ORTHOGONAL_COROLLARY.md), using
the new checked dense comparison below. For general sphere data the
inherited rate remains `n^(-1/2+o(1))`. Both retain the full common label
allowance and unquantified sufficient width. Setup is a certified
exhaustive search with symbolic Gaussian integration; its time, temporary
space and parameter precision can be enormous. This is not an efficient
practical initializer or a strict `C/sqrt(n)` theorem. Fresh isolated
reconstructions passed for the conditional transfer and its effective
tail/expectation components; the inherited neural estimates remain
explicit input dependencies rather than newly promoted results.

[RESULT.md](RESULT.md) remains the earlier qualitative baseline: an ordinary independently initialized width `q=ceil(log(en))` network, with all blocks trained, converges in probability to the independent dense prediction uniformly over the entire physical trajectory and sphere, including fitted endpoints. Its moving state is `q^2+dq+q`; fixed data cost `m(d+1)`; initialization needs only `q^2+dq` Gaussian draws. Its proof has the explicit sufficient label cap `||y||/sqrt(m) <= gamma/(1000m)` and unquantified accuracy/confidence width thresholds. It does not supply `C/sqrt(n)` accuracy or an effective epsilon-to-q choice.

The sharper constructive route has exact one-sample feedback equations and a complete all-time conditional stability theorem. Dense-copy concentration alone does not settle finite-width bias. The supplied hidden-feature-space lower bound remains restricted to that representation, not arbitrary compact predictors.

The earlier continuation supplied a directly computable **cubic** decoder on the
whole sphere, with root-width convergence of its two coefficients at each
fixed query. It does not establish a convergent high-order decoder or a
trajectory error at fixed nonzero labels. It also establishes a conditional
**virtual-reference transfer**: a canonical dense marginal can exist only in
the proof, and adding the dense-copy discrepancy compares the direct model
to a fresh independent dense run. For this route, a population-bias theorem
is unnecessary. At that stage the missing step was an admissible direct
initializer and quantitative feedback guarantee at the old retained size,
not the triangle inequality. The certified finite-width search above now
supplies that step at the inherited variability scale, with no useful
setup-efficiency guarantee. [DIRECT_INITIALIZER_TARGET.md](DIRECT_INITIALIZER_TARGET.md)
records that earlier stage rather than the current final status.

The 2026-10-06 Gaussian-calculus continuation is synthesized in
[GAUSSIAN_INITIALIZATION_RESULT.md](GAUSSIAN_INITIALIZATION_RESULT.md).
It gives an effective synthetic source-selection theorem with at most
`16R` neurons and quadratic metric/mixer storage; a complete direct,
dataset-blind first-layer tanh construction on the circle with
`O(log(1/epsilon)^(3/2))` neurons and `O(log(1/epsilon)^3)` retained
coordinates; explicit general-dimensional feature quadrature; and a
three-Gaussian limiting source for the first nonzero hidden-feature jet.
The circle theorem controls initial feature pairings, not trained
predictions. Full nonlinear feedback and a growing-order dense comparison
remain open for that jet-synthesis route; the separate certified search
does not require solving them. The supplied single-origin continuation has a very large
sufficient jet cutoff; this affects setup work, not the old retained count.

## Evidence and bounded routes

### Completion attempt: certified finite-width derandomization

The 2026-10-06 request to finish the proof continues this study. A new
bounded route seeks to turn the previously nonconstructive compact witness
into a direct initializer by rational enumeration, finite-time integration,
computable fitting-tail certificates, and exact finite-width Gaussian
expectations. Original-width Gaussian variables may occur as formal
indices in contraction graphs; no realized dense array or dense trajectory
may be constructed. Setup work and precision can be enormous and are not
identified with retained storage.

Root owns the selection/termination theorem and synthesis.
`orthogonal_route` owns `FINITE_WIDTH_EXPECTATION_COMPILER.md`;
`tail_certificate` owns `COMPUTABLE_TAIL_CERTIFICATES.md` in a fresh,
restricted author context; `analytic_construction` independently examines
the strict root-width concentration obligation in
`ROOT_WIDTH_CONCENTRATION_ROUTE.md`. These are proof-development routes,
not isolated reviews. The first two author continuations retain their
prior study context. The inherited `n^{-1/2+o(1)}` variability estimate
and the requested strict `C/sqrt(n)` estimate remain distinct targets.
The plan itself did not assume a completed direct trained-model theorem.

The completed selection theorem is
[DIRECT_CERTIFIED_CONSTRUCTION.md](DIRECT_CERTIFIED_CONSTRUCTION.md),
bound to `db6a744b0ca1c45b23f58f5705c5b1078ca590971a9c9780c213d67509a0cce1`.
Its constructive expectation dependency is
[FINITE_WIDTH_EXPECTATION_COMPILER.md](FINITE_WIDTH_EXPECTATION_COMPILER.md),
bound to `d78ac0bbff53cd60829b01f17b228114211716f8d17ee2701acdc382100536ec`;
its fitting/openness dependency is
[COMPUTABLE_TAIL_CERTIFICATES.md](COMPUTABLE_TAIL_CERTIFICATES.md),
bound to `c605ad12f7308568770a03d47c78305d5f01c29af37ed354dcf2f1434bfcf9d9`.
Root read both modules completely and reconstructed their composition.

Fresh isolated [CERTIFIED_TRANSFER_CHECK.md](CERTIFIED_TRANSFER_CHECK.md)
passed the full conditional selection theorem, the Gaussian compiler,
all-time probability/endpoint and rational-openness arguments, and the
stated real-coordinate and per-evaluation resource counts. Its hash is
`c035d62f4d4f5153cf8dd54d4f4d518a8350df80dfac742961a3c2e64ea3dd63`.
Fresh isolated [TAIL_CERTIFICATE_CHECK.md](TAIL_CERTIFICATE_CHECK.md)
independently reconstructed the entire tail module against the actual
corrected compact equations; its hash is
`bc35ca592faf1fb115a7e97227ac44aaff806638721a360ff6a9e45747c9b4c4`.
Root read both reports completely. Neither report re-verifies the inherited
neural source/concentration theorems, proves practical preprocessing
efficiency, or establishes the strict root-width target. The current
corollary explicitly imports the authorized integrated result's full
common label allowance, original-tolerance compact source count and
paired error, and independent-dense certificate. No book/paper promotion
or experimental verification is claimed.

The separate tanh-coordinate argument in
[ROOT_WIDTH_CONCENTRATION_ROUTE.md](ROOT_WIDTH_CONCENTRATION_ROUTE.md)
removes the growing carrier maximum from the dynamical stability exponent
for **orthogonal** training data. Its checked hash is
`4b96d88be6ac85f932ba8c30d63ddd7f513074277965d87edb80142768b4760e`.
Root read its complete proof and the complete inherited quadratic-exponential
training-budget correction (authorized integrated bridge, section 12).
Fresh isolated [LOG_DENSE_RATE_CHECK.md](LOG_DENSE_RATE_CHECK.md), hash
`45d80b1fd1d542c9fea167ac57caefbdd066e4f6d0a0b3c3aecd101279daba95`,
reconstructed the deterministic comparison, inherited fourth-moment
implication, confidence accounting, and all-time/sphere/endpoint topology.
Root read the report completely. The sole candidate correction was a
missing backslash in a spacing command; the review binds the corrected
version. The upstream source probability theorem is inherited, not
independently reproved by this check.

Root assembled and checked
[DIRECT_ORTHOGONAL_COROLLARY.md](DIRECT_ORTHOGONAL_COROLLARY.md), hash
`aea0cef2d7df93f649ffc9a0bcabdcf0ac785b7651227ba01354236220345722`,
by applying the checked constructive transfer to this new dense estimate
and the original paired compact count/error. It keeps the old
`log(en)^(3d+2)` retained exponent and gives error
`C_data,delta log(en)/sqrt(n)`. No strict root-width claim follows.

| Completion route | Current result | Remaining boundary |
| --- | --- | --- |
| Finite-width Gaussian integration and rational selection | Complete conditional direct-construction theorem; all-time nonlinear feedback, probability and endpoints certified | Setup work, temporary space and precision can be enormous |
| Exact tanh coordinates for orthogonal inputs | Checked dense-copy error `O(log(en)/sqrt(n))`; same clock and full sphere | Inherits source/fitting event and unquantified width |
| Log-free directional moments and localization | Proved sufficient implication and explicit failure of a separate-moment shortcut | Required joint sensitivity bound and global extension not proved |

Scoped whitespace and control-character checks on the new author proof
files produced no diagnostics. No renderer, formal proof assistant,
executable initializer, or numerical training experiment was run. These
are internally checked mathematical constructions, not software benchmarks.

### Continuation: Gaussian jet calculus and synthetic selection

On 2026-10-06 the user asks whether Gaussian expectations, including the
angular/harmonic integrations of initialization jets, can supply theoretical
neurons and reduced weights. This continues the same direct-initialization
question. The newly supplied complete input is
`closure_sampling_20261003/DIMENSION_PREFACTOR_OPTIMIZATION.md`.
Dataset access remains allowed for this construction; a dataset-blind
initializer is a separate stronger qualification, not inferred from the
absence of a dense realization.

Three bounded author continuations examine different obligations:
`analytic_construction` owns Gaussian/harmonic coefficient moments;
`orthogonal_route` owns synthetic source sparsification and reduced metrics;
`dense_bias` owns the finite-jet continuation cost and Gaussian-compiler
interface. Root owns a concrete deterministic Gaussian feature quadrature
and synthesis. These continuations have prior study context and are not
independent isolated reviews. No numerical experiments are authorized or
performed. The research and rigorous-proof workflows keep finite identities,
conditional construction, and the requested full neural theorem separate.

The authorized integrated study now has a variable compact-budget theorem
and an all-time analytic tail extension. Its `COMPACT_VARIABLE_SOURCE.md`,
`ANALYTIC_TAIL_EXTENSION.md`, and `FREE_ORDER_INTERFACE_CHECK.md` were read
completely for interface reconciliation. They remain internally checked
results conditional on inherited source theorems. They still construct
source vectors from original-width initialized objects; their new arbitrary
tolerance interface does not itself provide a direct initializer. No
concurrent integrated-study file was modified.

The resulting proof modules are:

| Artifact | Result and qualification |
| --- | --- |
| [GAUSSIAN_INITIALIZATION_RESULT.md](GAUSSIAN_INITIALIZATION_RESULT.md) | Current synthesis and complete direct circle first-layer theorem; not a nonlinear trajectory theorem |
| [GAUSSIAN_HARMONIC_JETS.md](GAUSSIAN_HARMONIC_JETS.md) | Harmonic covariance/tails, zero-mean symmetry, exact second-jet moments, jointly evaluable tagged limiting law, and finite polynomial-jet contraction evaluator |
| [GAUSSIAN_SYNTHETIC_SELECTION.md](GAUSSIAN_SYNTHETIC_SELECTION.md) | At most `16R` synthetic marks and exact corrected source geometry; supplied joint source law and cross pairings are explicit hypotheses |
| [GAUSSIAN_ENVELOPE_TRANSFER.md](GAUSSIAN_ENVELOPE_TRANSFER.md) | Adding one known error envelope per source family transfers population tail control to selected neurons |
| [GAUSSIAN_FEATURE_QUADRATURE.md](GAUSSIAN_FEATURE_QUADRATURE.md) | Elementary-formula, dataset-blind first-layer initialization on the entire sphere, with explicit setup work |
| [GAUSSIAN_JET_CONTINUATION.md](GAUSSIAN_JET_CONTINUATION.md) | Exact single-origin cutoff audit, conditional staged Gaussian recursions, and a counterexample to unconditional expected-jet analytic continuation |
| [GAUSSIAN_INITIALIZATION_CHECK.md](GAUSSIAN_INITIALIZATION_CHECK.md) | Scoped reconstruction of the selection and general-dimensional quadrature modules; prior context disclosed |
| [GAUSSIAN_HARMONIC_SYNTHESIS_CHECK.md](GAUSSIAN_HARMONIC_SYNTHESIS_CHECK.md) | Scoped reconstruction of the full circle initialization theorem, second-jet identities and limiting law, and continuation exponent; prior context disclosed |

The direct-circle synthesis uses its own explicitly computable harmonic
source law, not an assumed population-response oracle. Its source rank and
moments are certified in the proof. The general neural initializer remains
conditional on a substantially larger source-law and feedback theorem.
All setup quadrature, conditioning, and precision costs remain distinct
from retained coordinates. No polynomial-time or polylogarithmic-time
initializer for the full trained model is claimed.

Root read both Gaussian check reports completely. They certify their
explicit initialization/calculus modules, not the full trained-network
target. Their checks prompted safe integer-rounding guidance, an explicit
distinction between the runtime state `y-f` and canonical residual `f-y`,
and explicit nonnegative stability exponent/maximal-step choices in the
conditional staged-continuation lemma. No promoted files were changed.
The synthesis binding is
`1bd076c5061aae43385c779fe8da2f38f869dbb765b0fcf2424f634cd23777da`;
the clarified continuation binding is
`e69d7f8542eb0aae29bbee829121cf61dea00f32b264de7744123e5e9aae28bc`.
The first Gaussian check binds lattice module
`5636b9964b1e6adae2771c2325ce134b6f7ac3ad0df815a2e53c978f4825d042`
and synthetic selection
`3eb17a6963242bf9336e645a203fd6e67983e626de0ef39a85d917cb44a9e384`.
The other checked inputs and author hashes are recorded in the reports.
Scoped whitespace/control-character scans were clean; no renderer or
formal proof assistant was run.

### Continuation: a virtual dense reference

The user's follow-up asks whether the original polylogarithmic-size compact
model can be built directly, with a dense reference existing only in the
proof. This continues the same investigation. The original strict root-width
target remains recorded above; comparison at the available dense-variability
scale is also examined, without calling an `n^{-1/2+o(1)}` bound a strict
`C/sqrt(n)` bound. A favorable exceptional dense witness is not sufficient:
the proof-only reference must have the canonical Gaussian marginal law.

This bounded continuation examines three complementary obligations: a
finite-width coupling transfer that avoids population bias, direct synthesis
of reused Gaussian responses, and convergence of directly generated scalar
response coefficients. Root owns the synthesis and old-construction audit;
the existing `check_iid_limitation`, `dense_bias`, and `analytic_construction`
agents respectively own VIRTUAL_REFERENCE, DIRECT_GAUSSIAN_ATTEMPT, and
DIRECT_RESPONSE_ATTEMPT. They are author continuations, not fresh independent
reviews. No experiment or shared book/code/Git mutation is authorized here.

| Artifact | Result and status |
| --- | --- |
| [RESULT.md](RESULT.md) | Main qualitative construction and complete proof; passed [fresh scoped reconstruction](QUALITATIVE_CHECK.md) |
| [SOURCE_ASSESSMENT.md](SOURCE_ASSESSMENT.md) | Full assigned-proof reading, source/correction scope, dense preprocessing dependence, maintained dependency hashes |
| [DENSE_BIAS_ROUTE.md](DENSE_BIAS_ROUTE.md) | Independent population-bridge route: passive queries, whole-sphere/all-time convergence, nonlinear motion, and exact missing quantitative estimate |
| [ORTHOGONAL_ROUTE.md](ORTHOGONAL_ROUTE.md) | Prompt-only route: deterministic global fitting/tails, explicit initialization event, cubic frozen-feature comparison and nonlinear coefficient; author-checked, narrower local claims retained |
| [ANALYTIC_ROUTE.md](ANALYTIC_ROUTE.md) | Prompt-only route: one-sample feature response and conditional all-time transfer, directly computable cubic coefficient, explicit remainder/decoder gap; author-checked |
| [RANDOM_SMALL_LIMITATION.md](RANDOM_SMALL_LIMITATION.md) | Two ordinary iid width-q runs separate by at least `c|y|/q` with fixed positive probability for one sample; rules out that baseline's root-n target for `q=o(sqrt(n))` at sufficiently small fixed failure probability; passed [fresh isolated reconstruction](IID_LIMITATION_CHECK.md) |
| [DIRECT_INITIALIZER_TARGET.md](DIRECT_INITIALIZER_TARGET.md) | Current synthesis: virtual-reference criterion, old joint initialization dependence, exact elementary Gaussian checks, and missing quantitative direct construction |
| [VIRTUAL_REFERENCE.md](VIRTUAL_REFERENCE.md) | Complete conditional finite-width transfer, confidence accounting, exact/approximate initializer laws, and nonconstructive deterministic witnesses; does not supply a sampler |
| [DIRECT_GAUSSIAN_ATTEMPT.md](DIRECT_GAUSSIAN_ATTEMPT.md) | Law-computable reduced mixer and autonomous finite equations using the maintained finite Gaussian compiler; explicit fresh-innovation calculation and its predictor effect; no polylogarithmic accuracy schedule |
| [DIRECT_RESPONSE_ATTEMPT.md](DIRECT_RESPONSE_ATTEMPT.md) | One-sample direct cubic sphere decoder and pointwise root-width coefficient bound; exact fifth-order example rules out a uniform high-order bound from the earlier deterministic norms alone, not from typical Gaussian initialization |

The ordinary iid limitation is not an impossibility theorem for better initialization, architecture, quadrature, or optimizer design. It explains why the complete qualitative baseline does not answer the requested precision question.

## Contributors, verification, and remaining work

Root owns README, RESULT, and SOURCE_ASSESSMENT. `orthogonal_route`, `analytic_construction`, and `dense_bias` first worked in fresh, restricted contexts and separately froze their candidates. Their explicit source scopes are recorded in the reports; no findings from other studies were passed to them. After its first freeze, the analytic route received the separate bounded iid-baseline limitation task. Fresh isolated checkers own QUALITATIVE_CHECK and IID_LIMITATION_CHECK; they received frozen statements and dependencies, not other review findings. Both reconstructed their complete assigned claims and found no substantive defect. Root read their complete reports. These are internal study checks, not promotion reviews.

For the continuation, root read all new proofs. The Gaussian-compiler and
cubic-response notes have author checks plus root reconstruction of the new
calculations, not fresh isolated reviews. The elementary virtual-reference
transfer and Gaussian projection calculations additionally passed
[DIRECT_TRANSFER_CHECK.md](DIRECT_TRANSFER_CHECK.md), a bounded same-study
check with prior context disclosed. Its PASS does not certify a direct
sampler, inherited neural estimates, or the target compression theorem.
The full checked bindings are VIRTUAL_REFERENCE
`526da5e8d7325cbb2dfec919d54170a4ad0b4764ba00ea5a6abe56f484a75ef8`,
DIRECT_INITIALIZER_TARGET
`e5c54849f72322eee0aa0e471bf5afee787ff75069b75b2d1ad408f03f602c5b`,
and DIRECT_TRANSFER_CHECK
`d4ea6be8ba1ee3b805c0e1292e690ada4a9c3e90dfda3f576ead8b8cad4de182`.
The author-frozen DIRECT_RESPONSE_ATTEMPT is
`163f5ff0aac85385805d054f47d80d2b8a3fb8de6211931d7f597744048bbc59`.
The corrected author-frozen DIRECT_GAUSSIAN_ATTEMPT is
`07a5115ca278016b113ae8cca1423a72e8790a2603856b2640fdc7cbcd3d9ac5`;
root verified the source-word scope and the distinction between retained
size and potentially larger dense-free setup work. Scoped whitespace and
control-character checks found no remaining diagnostics in the new notes.
The additional maintained source is `docs/08-autonomous-computation.qmd`,
SHA-256 `72224d6c545531a768e090ac24b681c58046de0a42b37105a9a6ad51316c8b54`:
its complete C.1, C.2 and C.6 units were read, with the full-trajectory
theorem's narrower scope retained rather than imported into this task.

Current bindings: RESULT SHA-256 `c196f9a76dd860da68157a311a053e0536155635718c18e600ec391327485e51`, QUALITATIVE_CHECK `656a0dd3c8216a9519510587424a53bbeaa14b3ae4d0fb6844e6dfd446b0fbce`; RANDOM_SMALL_LIMITATION `608ca4aa83134aa6559a101994fd32751bf64dfe76d4c6fa03999b8dc18e2d83`, IID_LIMITATION_CHECK `571b8606b5b0d42a5edf3fd2a95779865d40239135f5aaab50e8ef97e1930aea`. The qualitative report retains its original frozen hashes and separately verifies the subsequent scalar-gap rename and inline-math delimiter corrections byte-for-byte. No mathematical statement changed in those corrections. Scoped whitespace checks produced no diagnostics; no Markdown/TeX rendering or formal proof assistant was run.

No training experiments, empirical claims, numerical solver implementation, or Git mutations were undertaken. The mathematical arguments and source hashes are the reproduction record; arithmetic-cost statements concern exact-real initialization and individual vector-field/prediction evaluations, not a hidden certified solver complexity.

The new finite-width search bypasses the earlier response-series and
growing-jet obligations for an existence/effectivity result. It does not
solve them as efficient methods. The highest-leverage remaining rate
obligation is a strict root-width concentration estimate for the actual
dense prediction trajectory; the inherited estimate has logarithmic and
subpolynomial losses. Efficient law-only synthesis, coefficient precision,
dataset-blind initialization, and avoiding dimension-dependent logarithmic
exponents also remain unresolved. Construction work is reported separately
and may exceed dense training cost; no polylogarithmic setup claim follows
from polylogarithmic retained storage.
