# General nonlinear endpoint variability

## Question and scope

User-requested investigation, 2026-10-10: can the specialized dense-versus-dense
endpoint lower bound extend to the compact paper's canonical Gaussian network,
arbitrary fixed depth, non-affine strip-analytic activations with bounded strip
derivative (values may be unbounded), positive training feature-Gram gap, and
nonzero labels under the existing small-label cap? Training directions are
pairwise neither parallel nor antiparallel. The user subsequently clarified
that the target is the supremum over query directions positively separated
from both signs of every training direction, not a bound at every fixed query.
The separated region is required to be nonempty; no interior assumption is
part of the target. An analytic-continuation proof route would need to state
any additional interior hypothesis separately.
The target is an actual fitted-endpoint lower bound, not an
initialization-derivative or transient bound.

All problem parameters, including labels and separation, are fixed before width
tends to infinity. We investigate a positive fixed-confidence root-width lower
bound, allowing its coefficient to depend explicitly on the fixed problem.
Whether it has a uniform coefficient from the advertised scalar parameters is
a separate question. No new empirical campaign or paper/book edits are in scope.

## Permitted inputs and provenance

- Current `paper/compact.tex` setup and its directly needed proof dependencies.
- The seven endpoint files expressly supplied by the user in
  `studies/integrated_general_compression_20261004/`: `ENDPOINT_LOWER_RESULT.md`,
  `TANH_ENDPOINT_VARIABILITY_LOWER.md`, `TANH_ENDPOINT_VARIABILITY_LOWER_CHECK.md`,
  `LINEAR_ENDPOINT_VARIABILITY_LOWER.md`, `LINEAR_ENDPOINT_VARIABILITY_LOWER_CHECK.md`,
  `NONLINEAR_ENDPOINT_VARIABILITY_LOWER.md`, `ENDPOINT_LOWER_CHECK.md`.
- Established Quarto book, subject to the repository's source rules.

No other study result is imported through a link or conversation recollection.
The older endpoint notes are research inputs to check, not established theorems.

## Work and check status

The user briefly requested a lower bound at all times, then clarified that
**only the final fitted model** is required. The current endpoint-only target
and status are in [RESULT.md](RESULT.md). The elementary time-zero obstruction
in `ALL_TIME_OBSTRUCTION.md` concerns the withdrawn contract and is not an
answer to the current question.

The endpoint-only generalization remains open in this study, not disproved.
The subsequent request to broaden the old two-tanh result is investigated
while retaining its proper-training-span and orthogonal-query geometry.
[ODD_DEPTH_ENDPOINT.md](ODD_DEPTH_ENDPOINT.md) now gives an actual trained-
endpoint theorem at arbitrary fixed depth for odd activations under an
explicit Gaussian-variance qualification. This qualification follows
automatically for arbitrary layerwise mixtures of tanh, arctan, sine, erf,
arsinh, and $z+\tanh z$, using the paper's unchanged label cap. The last two
are unbounded; erf and arsinh are separately checked consequences in the
new theorem's audit report.
It is not a theorem for all non-odd activations or full-span data.
The complete argument passed the fresh isolated reconstruction in
`ODD_DEPTH_ENDPOINT_CHECK.md`, tied to its recorded final source hashes;
no promotion is being requested.
Its supporting independent derivation is `DEPTH_COVARIANCE_ROUTE.md`.
`PRODUCT_QUERY_ROUTE.md` gives a scalar noncentered two-layer estimate and
explains why the whole-feature argument cannot simply discard oddness.
[ENDPOINT_IDENTITY.md](ENDPOINT_IDENTITY.md) records an exact actual-
endpoint decomposition and why an absolute cubic label remainder cannot
transfer a root-width random-feature lower bound at fixed labels.

### Current continuation: full nonaffine activation class, 2026-10-11

The user first asked for a sustained attempt covering GELU and SiLU at every
layer, then asked to generalize the resulting mechanism to the compact
paper's entire activation class with only nonaffinity added. The theorem in
`GAUSSIAN_ORACLE_ENDPOINT.md` now covers arbitrary layerwise nonaffine
activations in that class, including heterogeneous choices. It uses a
polylogarithmic-length adaptive
Gaussian matrix-oracle approximation of the actual fitted parameters,
exact deferred decisions, projected query-innovation propagation, and a
weighted nonlinear scalar anti-concentration bound. The result is now
internally checked: for every fixed confidence $1-\delta$, at each
sufficiently large individual width the two actual fitted endpoints differ
at the orthogonal query by at least $C/\sqrt n$, with $C>0$ independent
of width. The sufficient label cap is unchanged. Activation values may be
unbounded; no oddness, centering or named-family property is used. The
coefficient may depend on the fixed problem; the width threshold is
unquantified.

The new modules and their exact roles are:

- `GELU_SILU_FLOW_ROUTE.md`, Section 6: a finite-oracle approximation of
  the actual fitted parameters with $O(n^{-16})$ physical-norm error and
  $O_{\mathrm{data}}(mL[\log(en)]^{9/2})$ matrix actions. Sections 1--5
  concern the earlier incomplete centered-comparison route and are not
  premises of this new argument.
- `GELU_SILU_PROJECTED_INNOVATION.md`: query energy survives successive
  projections of rank $o(n)$ at arbitrary fixed depth, under the explicit
  conditional Gaussian representation.
- `GELU_SILU_PROJECTED_SCALAR.md`: scalar variance and uniform normal
  approximation with arbitrary conditioned biases/readouts, using a fixed
  empirical fourth-moment bound; the full covariance matrix need not have
  a uniform gap.
- `GAUSSIAN_ORACLE_ENDPOINT.md`: exact adaptive two-sided Gaussian
  conditioning, transcript-measurable good events, and the complete
  endpoint assembly. The original network is neither frozen nor changed.

The reviewed packet consists of these new modules, the fitting/source
proofs in the current compact paper, and the explicit readout moment
extraction in `NONODD_MOMENT_ROUTE.md`. There are separate fresh reviews
for the Gaussian lemmas (`PROJECTED_GAUSSIAN_CHECK.md`), oracle integrator
(`ORACLE_INTEGRATOR_CHECK.md`), and theorem assembly
(`GAUSSIAN_ORACLE_ASSEMBLY_CHECK.md`). Their scopes are explicit and their
statement clarifications are incorporated. The current-paper fitting/source
proofs remain scientific inputs; these checks do not claim a new audit
of every source-cavity argument. No
numerical experiment, manuscript change, book change or commit is made.
The generic activation replacement is reconstructed in
`GENERAL_ACTIVATION_ENDPOINT_CHECK.md`; it reuses the older checks only for
the unchanged oracle, conditioning, source and transfer modules.

The additional frozen-feature bound in `GELU_SILU_INNOVATION.md`, and the
weighted-covariance progress in `GELU_SILU_DIRECT_ROUTE.md`, remain useful
independent results but are not dependencies of the oracle endpoint proof.

### Earlier oddness-removal routes

The user now asks to lift oddness while retaining the orthogonal-query
geometry and the existing label restriction; the unrelated full-span problem
is not being folded into this continuation. Values may remain unbounded.
`NONODD_ENDPOINT_PROGRESS.md` records a positive actual-endpoint extension
allowing an arbitrary last activation with an explicit centered-variance
qualification. In particular GELU, SiLU, and softplus are allowed at the
last hidden layer after any of the previously checked odd families, without
another label cap. This does not yet allow nonodd activations in every layer.
That limitation belongs to this earlier comparison route; it is removed by
the current oracle theorem above.
The new endpoint theorem passed the fresh isolated reconstruction in
`NONODD_ENDPOINT_CHECK.md`. The all-layer mean-adapted comparison and scalar
reduction passed `NONODD_COMPARISON_CHECK.md`; its required first-layer
normalization qualification was corrected and the final source rechecked.
`NONODD_ROUTE_CHECK.md` independently checks the conditional fluctuation,
source-moment extraction, and specifically scoped shortcut obstructions.
Each report states its limited verdict and records the reviewed sources.

The same continuation has three bounded, separately recorded routes:

- `NONODD_INNOVATION_ROUTE.md`: frozen-feature anti-concentration conditional
  on the entire active training initialization, using independent replicas of
  the unused Gaussian query. This holds without oddness at arbitrary depth.
- `NONODD_SCALAR_ROUTE.md`: an exact scalar reduction, and a stronger
  mean-adapted endpoint comparator with the original sharp root-width
  stability coefficient, without oddness anywhere.
- `NONODD_MOMENT_ROUTE.md`: training moment extraction from the complete
  current-paper source proof and the two-layer unbounded-activation scalar
  consequence. Its sharper proposed energy-only fourth-moment bound is
  refuted in the precisely stated scope; this does not refute the endpoint
  lower-bound target.

In that earlier comparison route, the unresolved bridge is anti-concentration for the mean-adapted
comparator, whose offsets depend on the trained network. It is not the
frozen-feature predictor in the first route, and their two theorems cannot
simply be composed. That route alone proves neither a full nonodd endpoint
theorem nor a counterexample to one. No activation centering, stronger label cap, or
readout-only conclusion is substituted for the requested theorem.

### Earlier endpoint routes and checks

Independent scoped routes are retained in `OBSTRUCTION_ROUTE.md`,
`POSITIVE_ROUTE.md`, and `LINEAR_RESPONSE_ROUTE.md`. Their claims must be read
with their individual qualifications, not as proofs of the original broad
endpoint theorem. The endpoint identity and its quantitative bounds passed
the scoped reconstruction in `ENDPOINT_IDENTITY_CHECK.md`. A fresh isolated
review in `PARTIAL_RESULTS_CHECK.md` checked all four principal positive
partial claims and the hidden-nullspace feedback calculation, with exact
source hashes. These **partial results** are internally checked, not promoted.
The general trained-endpoint theorem remains open. The separately scoped
direct endpoint-sensitivity attempt is recorded in `DIRECT_ROUTE.md`.
The coordinator read the complete note and checked its finite-width
variational equation, convergence to the endpoint derivative, late-time
kernel injectivity/rank argument, Gaussian normalization, and final
second/fourth-moment implication. It has no fresh isolated review. Its
parameter-rank conclusion does not supply observable nondegeneracy or the
required width-uniform probabilistic constants.

No numerical reproduction is applicable: these are analytic derivations, and
no experiment was run. To check them, use the complete proof notes and their
recorded source versions. The unresolved geometric obligation concerns
full-span training. Under the proper-span/orthogonal-query geometry, the
entire nonaffine part of the paper's activation class is now resolved by the
oracle argument, whereas the earlier odd theorem used a fluctuation-scale
endpoint comparison. Ordinary fitting or an absolute small-label
approximation alone supplies neither result.

Coordinator owns this README and the eventual synthesis. Scoped independent
routes own their separately assigned flat files. No Git commit or shared
manuscript modification is authorized by this investigation.
