# Unseen-input decoding with an absolute logarithmic storage exponent

## Question and scope

Started 2026-10-05 at the user's request. Can a compact autonomous model
decode an input not supplied during preprocessing or training, using comparisons
with training data or their representations, while preserving whole-sphere,
all-physical-time accuracy at the dense width-n variability scale and retained
storage with absolute logarithmic exponent five? The stronger n^(-1+o(1))
matched-reference error is a separate target, not silently substituted for
the requested dense-variability scale.

Keep arbitrary fixed depth L >= 2, nonlinear learned hidden features, fixed
training data spanning R^d with m >= d, the strip-analytic activation class
with bounded derivatives but possibly unbounded values, original Gaussian
initialization and zero readout, original small-label allowance and positive
training feature-Gram gap. Loss is the mean over the m training examples,
with block mobilities (n,1,...,1,n). The query is any input on the radius-sqrt(d)
sphere, supplied only at decoding. No query labels are available or required.

All retained state, fixed arrays, program parameters and live decoding workspace
count. No discarded dense-weight oracle, arbitrary-real packing, future-output
playback, free function-valued state, frozen-feature substitution or merely
fixed-query probability guarantee may replace the target. Computational time
is not assumed efficient, but its workspace cannot be hidden. Any relaxation
of these requirements is to be identified, not presented as the requested result.

## Authorized inputs and process

The user explicitly authorized reuse of both the finite-panel construction and
integrated compact proofs on 2026-10-05. Allowed repository scientific inputs:
this study; studies/finite_panel_absolute_compression_20261005; and the relevant
proofs in studies/integrated_general_compression_20261004; maintained docs/ and
code/. On 2026-10-07 the user additionally authorized inspecting the original
finite-neuron insertion proofs in
studies/dense_cutoff_population_rate_20261001, to quantify the inherited
stochastic width threshold. That authorization covers those proofs and their
local supporting arguments, not unrelated research in the older study.
The user subsequently authorized the two exact files
`studies/closure_sampling_20261003/ACTIVATION_CLASS_EXTENSION_ROUTE.md`
and `ACTIVATION_CLASS_EXTENSION_CHECK.md` to trace the imported
complex-time mixed-response proof. No other files in that study are inputs.
Other studies and old_docs/ are not inputs. External primary sources
may be consulted if needed and must be verified before use.

Read current AGENTS.md, RESEARCH_WORKFLOW.md Part 1, docs/index.qmd and
docs/notation.qmd. Use investigate-conjectures and solve-math-rigorously.
The required custom canonical-notation skill was permission-denied during
the earlier rounds. It became readable in the renewed 2026-10-06 search;
the lead and current authors read it and its neural-response reference in
full. The earlier fallback reports remain historical provenance.

Initial HEAD: 3834145d910202a84824d943fe7d7f65714d96f2. Preserve all existing
dirty files and other study work. No Git mutation, maintained-book edit,
numerical training campaign or promotion is part of this task.

## Bounded proof search and ownership

Lead owns README and synthesis. Three fresh scoped routes independently examine
training-comparison decoders, nonlinear population-response decoding, and
query-uniform source/sketch constructions. Each owns a separate flat note.
They do not read one another before freezing their initial findings. An exact
partial lemma or failed construction is not a proof of the full target or an
impossibility theorem for all admissible decoders.

## Current outcome

### Method cleanup and word-cost refinement, 2026-10-07

The user requests a bounded simplification of the current source-seeded
construction, a word-memory/word-operation interface with precision stated
separately, safe exponent reductions, and a realistic implementation plan.
The full model, original label range, whole-sphere/all-time comparison,
endpoint, present-state querying and counted decoding memory remain fixed.
No cheaper historical passive estimator is substituted for the final decoder.

The current resource/method interface is
[STREAMLINED_METHOD_RESULT.md](STREAMLINED_METHOD_RESULT.md). It combines
three scoped author refinements with the lead's confidence separation:

- [WORD_COST_REFINEMENT.md](WORD_COST_REFINEMENT.md): numerical-word costs,
  packed exact hashes, depth-first seed expansion, indexed Jacobi pivots
  with cached exact residuals, and cached selected-field metric products.
- [WIDTH_GATE_REFINEMENT.md](WIDTH_GATE_REFINEMENT.md): the source gate's
  outer power falls from 20,000 to 1,100; a sharper factorized gate is also
  given. The original scientific estimates remain component assumptions.
- [CONFIDENCE_SEPARATION_REFINEMENT.md](CONFIDENCE_SEPARATION_REFINEMENT.md):
  implemented members need fixed source confidence; only the independent
  reference retains the confidence-dependent moment order in its width.
- [IMPLEMENTATION_STREAMLINE.md](IMPLEMENTATION_STREAMLINE.md): the
  three-phase executable structure, exact tiled scheduling, and explicit
  practical/GPU limitations, without a speedup or implementation claim.

At fixed problem parameters the refined retained size is
`O(log(n)^6 log log(n))` numerical words, with sufficient word precision
`O(beta^(110L) Z)` bits. Initialization, complete compact training and one
unseen-input query take respectively `O(n log(n)^(29/2))`,
`O(log(n)^12 log log(n))`, and `O(n log(n)^12 + log(n)^14)` word operations.
The full parameter table, input/evaluator charges, and setup's noncompact
temporary memory are explicit in the synthesis. Word counts are not bit
counts or single-instruction hardware estimates.

Separate bounded reconstructions are `WORD_COST_REFINEMENT_CHECK.md`,
`WIDTH_GATE_REFINEMENT_CHECK.md`, `CONFIDENCE_SEPARATION_CHECK.md`, and
`IMPLEMENTATION_STREAMLINE_CHECK.md`. These disclose reused contexts and
accepted scientific boundaries; they are not blind promotion reviews.
The word check's required tiny-label numerical RMS qualification and the
width check's carrier-gate citation correction are incorporated. A final
separate read-only assembly check found no composition mismatch; its
generated-member independence wording correction is included.

Five deterministic exact-algebra tests pass. Reproduce with
`python3 -B studies/unseen_query_decoder_20261005/test_streamline_kernels.py`.
They cover packed hashes, generator sequences/stacks, cached bilinear forms,
exact tiling and indexed pivots, not full neural transcripts or GPU timing.
The clean table retains `nY >= 1`; tiny-label resource refinement must also
retain the Gaussian RMS gate with its enlarged field count. The original
leading dense-error coefficients remain structural, not fully parameter-
quantified by this cleanup. Practical width, FP32/FP64 sufficiency, and an
actually scalable compressor remain unestablished. No scientific scope,
label allowance, error certificate or old bit envelope is weakened.

This is continuation in the same study, not promotion or a neural training
campaign. Historical proof files and the two-gap scientific synthesis below
are retained. No Git commit or maintained-book/API change is made in this
cleanup round.

### Closing the two remaining gates, 2026-10-07

The user requests a complete finite-confidence source probability and final
dense-error comparison, not another asymptotic width assertion. This is
continuation of the polynomial-width investigation below. The component
closures now have separate bounded independent checks. Current synthesis
is [TWO_GAP_CLOSURE_RESULT.md](TWO_GAP_CLOSURE_RESULT.md): it uses a
modified decoder and does not assign the old sixth-power bit table to it.

Fresh scoped authors examined finite insertion probability, acquired-pair
likelihood calibration, and nonlinear weak covariance error. Their separate
notes are `FULL_FINITE_SOURCE_PROBABILITY.md`,
`FINAL_ERROR_CLOSURE_ROUTE.md`, and `NEURAL_WEAK_ERROR_ROUTE.md`.
The probability theorem has a fresh isolated reconstruction in
`FULL_FINITE_SOURCE_PROBABILITY_CHECK.md`; its sufficient width is an
explicit, very conservative fixed-degree polynomial, with no inverse
positive label amplitude in that scientific theorem. The two error routes
derive useful partial identities, not a final error
bound for the unchanged decoder. In particular zero initial readout does
not force the passive covariance bias to vanish.

The lead's `SOURCE_SEED_EXACT_QUERY.md` instead proposes retaining a short
seed for the finite source and regenerating its empirical rows at a query,
including the full conditional covariance correction. Its finite-transcript
argument and complete-source ensemble are separately assessed in the
collaborative `SOURCE_SEED_TRANSCRIPT_CHECK.md`. A fresh isolated review
in `SOURCE_SEED_EXACT_QUERY_CHECK.md` found two corrections: the query
error recurrence must be additive, and source and query precision must
be chosen together before setup. Both are incorporated and rechecked.
This construction avoids the old
prior/population substitutions; it does not prove their missing estimates.
It has different costs: at fixed problem parameters the proposed retained
bit memory is `O(log(en)^7 log(e+log(en)))`, not the preceding sixth
power, and query work still contains a factor of dense width. All members'
compact states, both seed levels and regeneration work are counted.
Its physical source probability is supplied by the finite training-source
theorem above. `NUMERICAL_BENCHMARK_ABSORPTION.md`, Section 5, explicitly
instantiates the structural dense certificate's formerly unspecified mesh
coefficient using its original physical modulus. The independent query
check also reconstructs this lemma: the mesh term is at least `32Y/n`,
so numerical absorption no longer needs an opaque leading-coefficient
inverse or eventual exponential dominance. The leading dense certificate
is unchanged; equality to an arbitrarily fixed smaller mesh coefficient
is not asserted.

The source radius loses a factor of the finite confidence moment order.
That additional cost is composed in `CLOSURE_COMPOSITION_COSTS.md`;
no old table is silently reused. For the clean numerical-precision branch
retain `nY >= 1`, or charge the separately stated extra logarithmic
tiny-label precision. The source probability theorem itself has no such
lower-label condition. The bounded synthesis reconstruction in
[TWO_GAP_CLOSURE_CHECK.md](TWO_GAP_CLOSURE_CHECK.md) passes the combined
probability, center/tail, error and cost interfaces. Its exact scope and
incidental agent-metadata exposure are disclosed in the report; it is not
a promotion review. No promotion is implied.

### Polynomial-width continuation, 2026-10-07

Earlier synthesis, preceding the two-gate closure above:
[POLYNOMIAL_WIDTH_RESULT.md](POLYNOMIAL_WIDTH_RESULT.md), with the bounded
[assembly check](POLYNOMIAL_WIDTH_RESULT_CHECK.md). It replaces two
exponential component thresholds but expressly does **not** certify a
polynomial sufficient width for the full decoder.

The user explicitly requests removing exponentially large sufficient-width
conditions and other hidden parameter costs, preserving the existing model,
small-label scope, whole-sphere/all-time error benchmark and compact present-
state decoder. This is continuation of the same investigation. The lead
retains ownership of this README and synthesis. No numerical experiment,
maintained-book edit, Git mutation or promotion is authorized.

Three fresh scoped author routes own `POLYNOMIAL_SOURCE_WIDTH.md`
(deterministic analytic-source gates), `EXPLICIT_FITTING_WIDTH.md`
(initial Gram concentration, fitting and remaining stochastic gates), and
`POLYNOMIAL_ACCURACY_ONSET.md` (the decoder's dense-error comparison).
They use only their separately specified permitted inputs and do not read
one another's initial results. The lead audits the tiny-label normalization,
remaining external computational interfaces and full-chain composition.
Proofs are required; an adjusted radius, smaller stochastic remainder or
polynomial execution table alone does not certify polynomial sufficient
width for the final theorem. Stronger error targets, free wider virtual
sources, tighter label caps, or uncounted sample/generator costs are excluded.
The preceding checked table remains current until specific replacements
have been derived and checked.

Two component replacements now have fresh bounded checks:

- [EXPLICIT_FITTING_WIDTH.md](EXPLICIT_FITTING_WIDTH.md), Sections 1--5,
  with [its isolated reconstruction](EXPLICIT_FITTING_WIDTH_CHECK.md),
  replaces the exponential sphere-net fitting threshold by the sufficient
  width
  `ceil(beta^(32L) (1+m/gamma)^2 [d L log(beta) + log(16L(m+1)^2/delta)])`.
  It retains the exact original fitting label allowance, permits unbounded
  activation values, and proves global nonlinear fitting and the real
  whole-sphere endpoint tail. It does not prove a source/decoder width.
- [POLYNOMIAL_SOURCE_WIDTH.md](POLYNOMIAL_SOURCE_WIDTH.md), with
  [its isolated reconstruction](POLYNOMIAL_SOURCE_WIDTH_CHECK.md),
  removes the large complex-radius gate by choosing the physical radius
  coefficient `1/[beta^(100L)(1+gamma/m)]`. The existing actual Taylor
  step and resource table are unchanged. The optional tiny-label precision
  branch and deterministic tail gates are also checked conditionally on
  their named numerical/source interfaces; stochastic uniformity in tiny
  labels is not asserted.

The original insertion proofs have now been read, not merely their recorded
verdicts. `QUANTITATIVE_INSERTION_WIDTH.md` develops a finite-order
collision/local-net reduction and exact label-scaled linear recurrences.
`FINITE_COMPLEX_MOMENT_GATE.md`, with the fresh bounded check in
`FINITE_COMPLEX_MOMENT_GATE_CHECK.md`, proves confidence-order Gaussian
correction control with its additional Taylor patch cost stated. Their
local insertion probability still requires a quantitative theorem.
`POLYNOMIAL_ACCURACY_ONSET.md` separates the passive
estimator bias from sampling variance: more prior samples alone do not
repair the dense-error comparison. A further bounded weak-observable route
is recorded in `WEAK_PASSIVE_WIDTH_ROUTE.md`. A further bounded
fixed-order remainder calculation is recorded in
`FIXED_ORDER_INSERTION_JETS.md`, with a fresh bounded independent
reconstruction in `FIXED_ORDER_INSERTION_JETS_CHECK.md`. It replaces a
depth-dependent cutoff power by one for the main remainder, and at most
three for learned-source and top-offset corrections. The author corollary
`SCALED_INSERTION_REMAINDER.md` gives the label-normalized transfer
without inverse activity, and `INSERTION_MAP_MODULI.md` supplies
explicit Gaussian control/time interpolation recurrences. The latter
two are author-level conditional results. These
routes do not supersede the full cost/error theorem or certify a polynomial
width for it.

Post-check presentation corrections restored six carriage-return-damaged
`\rm` commands in `POLYNOMIAL_SOURCE_WIDTH.md` and inline math delimiters
in `FINITE_COMPLEX_MOMENT_GATE.md`; their mathematical formulas did not
change. The corrected hashes are respectively
`4821875988b8f7f493e776e9147da09ac27a547125d29eea0e84b98e8559e916`
and `6922cc2630f335903352fab360d3b56b72ccdd10d248ea8e49abe73759b48f18`.
The original review hashes remain recorded in their reports. A missing
backslash in the weak-route Taylor remainder was also restored, without
changing its author-only claim level.

### Renewed fast-query search, 2026-10-06

The user requested a substantially harder continuation, preserving the
complete model/error/information contract and targeting genuinely small
absolute logarithmic powers and preferably logarithmic unseen-query work.
This is the same investigation. Existing large-power theorems are not
silently upgraded by a smaller count for one component.

Three fresh scoped author routes own `FAST_TAYLOR_NOISE.md` (stable noisy
Taylor source and activation-jet precision), `FAST_QUERY_STRUCTURE.md`
(actual nonlinear Gaussian contractions), and `FAST_UNIFORM_QUERY.md`
(reachable contexts, retained seeds, and query sampling). Their first
derivations use disjoint specified input sets, not one another's new
notes. After freezing its first note, the uniform-query author is separately
investigating local conditional-kernel coupling in
`FAST_LOCAL_KERNEL_AUDIT.md`; the lead supplied that proposed mechanism and
its fresh-innovation conditioning hazard. It is not an isolated review.
The lead owns synthesis and interface checks. No experiment or promotion
is authorized; retained descriptions, precision and peak memory still count.

Current parameter-explicit synthesis:
[GAP_REFINED_PHASE_COSTS.md](GAP_REFINED_PHASE_COSTS.md), with the bounded
[physical-source check](GAP_SOURCE_CHECK.md) and
[finite/passive/resource check](GAP_TRANSPORT_CHECK.md). A one-sided
gradient stability estimate removes an algebraic sample/gap factor from
both numerical degree and precision. Compared with the preceding explicit
table, the powers of (1+m/gamma) fall from five to two in retained and
post-initialization peak memory, from thirteen and twelve to five in
initialization and all-training work, and from ten to four in query
preparation. The streaming query term no longer has an algebraic gap factor.
Bit memory remains logarithmic power six, counted numerical words power
five; query work still has a factor n. Scientific width and dense-certificate
absorption thresholds remain unquantified and potentially exponential.
Activation, input and certificate interfaces retain their actual charges.
These bounded conditional checks are not promotion.

The preceding parameter-explicit synthesis is
[EXPLICIT_PHASE_COSTS.md](EXPLICIT_PHASE_COSTS.md), with the
[precision-confidence check](PRECISION_CONFIDENCE_CHECK.md) and
[cached-phase check](CACHED_PHASE_CHECK.md). Separating numerical words
from external-code confidence removes a dimension factor from precision;
caching already acquired coefficients reduces query preparation from
logarithmic power 29/2 to 12. The three-phase table exposes all internal
sample, gap, dimension, activation, depth and confidence factors, and
retains evaluator/input charges and unquantified width/absorption gates.
The source accuracy and full original label scope are unchanged.

The [dependency audit](HIDDEN_DEPENDENCY_AUDIT.md) distinguishes polynomial
internal work from unrestricted external interfaces and potentially very
large accuracy-onset width. The [memory route](MEMORY_POWER_REFINEMENT.md)
gives a component noise-mark saving and a selected-packet lossless-encoding
obstruction, not a lower bound against all equivalent-summary models.
These are bounded internal research results, not promotion.

The preceding synthesis is
[FAST_LOCAL_EFFICIENCY_RESULT.md](FAST_LOCAL_EFFICIENCY_RESULT.md).
Its completed [assembly reconstruction](FAST_LOCAL_ASSEMBLY_CHECK.md)
accepts the source/passive/resource composition under the inherited
scientific and finite-generator interfaces. It records retained and peak
post-initialization memory of logarithmic power **six bits**, or power
**five finite numerical words** with their precision counted. Internal
work is n times logarithmic power **31/2** at initialization, power
**29/2** for all compact updates, and n times power **four** plus power
**29/2** preparation for one unseen query. Explicit major-parameter
factors and evaluator/input charges are in the synthesis. Tanh evaluation
fits these powers by `FAST_TANH_EVALUATION.md`, checked in the assembly.
Neither a logarithmic-work query nor a practical crossover width is proved.

The previous synthesis is preserved in
[FAST_EFFICIENCY_RESULT.md](FAST_EFFICIENCY_RESULT.md).
The corrected Taylor source and uniform-query component have separate
bounded independent reconstructions in `FAST_TAYLOR_NOISE_CHECK.md` and
`FAST_UNIFORM_QUERY_CHECK.md`. The complete smaller conditional assembly
in `FAST_COMPOSITION.md` passed a separate **author-style**, non-blind
reconstruction in `FAST_COMPOSITION_CHECK.md`. The physical-versus-normalized
noise distinction and real whole-sphere cap transport were corrected
during that assembly check; its exact source hashes are recorded there.

That previous construction uses logarithmic power five variable-precision
numerical words, and logarithmic power 17/2 total bits, for retained and
peak post-initialization memory. An absolute integer bit exponent nine
suffices. The further checked physical-query grid gives query work
n times logarithmic power 20 plus preparation of power 41/2;
all explicit sample/gap, dimension, depth and activation factors
and evaluator additions are in the synthesis. This is not a logarithmic-
query result, not a fifth-power bit result, and not a practical uniform
width guarantee. The earlier cost contract remains the reporting contract
for the old panel and old decoder implementation; the new checked variant
has its own explicit ledger rather than silently changing the old one.

The nonlinear Gaussian contractions in `FAST_QUERY_STRUCTURE.md` are
author-derived partial mechanisms, not a full fast evaluator or a
decoder lower bound. A further author continuation,
`FAST_LOCAL_PRECISION_TEST.md`, proves exact finite-tape reproduction by
a rounded selected metric under a specified rounded-noisy-source interface.
Its local-precision full-decoder application is now assembled in the
current synthesis above, with the additional source, posterior, passive,
and resource checks below. Query control-variate and multilevel routes
remain partial author work, not substitutes for that complete decoder.

#### Local finite-source continuation and fast-integral search

The further continuation separates source law, exact compact acquisition,
finite posterior moments, passive queries, and full resource accounting.
`FAST_SCALAR_FORCING.md`, `FAST_FINITE_SOURCE_BRIDGE.md`,
`FAST_FINITE_POSTERIOR.md`, and `FAST_FINITE_PASSIVE.md` supply those
interfaces together with `FAST_LOCAL_PRECISION_TEST.md`. The separate
bounded component reconstructions disclose their reused context; they
are not fresh isolated promotion reviews. The passive reconstruction
caught and corrected a missing vector factor in the block-estimator
error. The population comparison and implemented-estimator rates remain
distinct in the corrected proof.

`FAST_LOCAL_COMPOSITION.md` then gives a complete actual-pair schedule,
a noncircular local-precision choice, and simultaneous block vectors.
The latter fit the already charged seed-space allowance and remove
repeated coordinate passes. Its author-assisted accounting is in
`FAST_LOCAL_RESOURCE_CHECK.md`; separate assembly reconstruction is the
acceptance gate for `FAST_LOCAL_EFFICIENCY_RESULT.md`. That gate passed
in `FAST_LOCAL_ASSEMBLY_CHECK.md` at frozen report hash
`6eac888940549718b659218bba203ce0e172c2944aa24cacb5efb55dce246e57`.
The check discloses reused component-review context, not a fresh isolated
review. Its exact frozen scientific inputs and numerical synthesis are
recorded there. Earlier proof drafts retain their frozen status wording;
the current synthesis records their later scoped acceptance. No maintained
book, other-study artifact, Git index, or experiment was changed by this
continuation; concurrent unrelated changes were preserved.

The fast-integral route has a concrete new partial construction in
`FAST_MULTILEVEL_QUERY.md`: an exact correlated-Gaussian Fourier
recurrence with a factorial tail for a genuine leading learned-mean
gate. Its explicit order and coefficient count do not extend to the
full nonlinear trajectory with an absolute logarithmic query exponent.
Fixed-order control variates and ordinary independent multilevel
sampling leave a positive variance in an admissible example. These are
scoped limitations, not a universal decoder lower bound.

The suggested adaptive late-time patch shortcut was checked against
`SANE_ADAPTIVE_TIME.md`, Section 5. Residual decay alone does not supply
the larger complex-time domain needed to remove the remaining half
power from the source count; that existing obstacle was not rebranded
as a proof. A primary-source literature screen also considered
[analytic Hermite integration](https://arxiv.org/abs/1403.5102) and the
[Gaussian-kernel integration paper](https://web.maths.unsw.edu.au/~fkuo/pubs/preprint/Kuo_Sloan_Wozniakowski_2017.pdf),
including the latter's Theorem 1.1. No external quadrature theorem or
black-box lower bound is imported into the neural result: applicability
to the special response family has not been proved. The highest-leverage
open step remains a counted fast evaluator for the full nonlinear query
expectation, not another substitution of an analytic-integral oracle.

### Small-exponent efficiency search, 2026-10-06

The user has authorized strategic, opportunistic proof search to replace
the very large logarithmic and parameter powers by genuinely economical
unseen-input decoding, preferably near logarithmic powers four or five.
This continues the same decoder question, rather than changing the
network, label class, information interface, or error norm. Retained state
and peak query workspace count; exact-real arithmetic and finite-bit
claims remain separate. No numerical training campaign is authorized.

The lead coordinates a bounded initial round and a bottleneck-focused
followup, reserving a separate reconstruction before accepting any new
theorem. Three fresh author routes have disjoint write ownership:
`SANE_PANEL_EXTENSION.md` (query-independent extension of the selected
panel), `SANE_DECODER_CORE.md` (actual compiler/precision costs), and
`SANE_RESPONSE_MEMORY.md` (compressed nonlinear response actions).
They do not inspect one another's new notes before freezing their first
results. The lead owns the synthesis and investigates conditional-law
evaluation and the distinction between temporal and query complexity.
The existing resource theorems are not strengthened merely by opening
these routes; powers four or five are targets, not established bounds.

Current synthesis: [SANE_EFFICIENCY_RESULT.md](SANE_EFFICIENCY_RESULT.md).
The first independent checks accepted the integrated-collocation bound,
the residual-decay source improvement, and the smaller decoder core under
their stated interfaces. The core's one spectral guard-precision correction
was incorporated and rechecked. The panel-extension and nonlinear-response
notes also passed bounded reconstruction, but establish partial mechanisms
and scoped obstructions, not the requested decoder.

The followup produced two structurally smaller constructions: an elementary
finite-bit coordinate metric in [SANE_METRIC_PACKETS.md](SANE_METRIC_PACKETS.md),
and a logarithmic-power `5/2` causal source in
[SANE_TAYLOR_SOURCE.md](SANE_TAYLOR_SOURCE.md). Their separate bounded
reconstructions are [the metric check](SANE_METRIC_PACKETS_CHECK.md) and
[the Taylor-source check](SANE_TAYLOR_SOURCE_CHECK.md). The metric review's
setup-memory finding was repaired by streaming small-matrix rank tests
and rechecked. The Taylor check's finite-difference-spacing clarification
was incorporated and rechecked. Its disclosed late supervisory comment means that check
is not described as blind; neither report is a promotion review.

These results identify the highest-leverage continuation: a stable noisy
Taylor-source/metric composition, then reducing its true query state and
workspace. Training-summary coordinates, source noise, scalar/jet precision,
retained query randomness and peak query scratch remain distinct obligations.
No fourth- or fifth-power complete unseen-query theorem is claimed. The
checked cost contract has not been overwritten by partial or candidate
counts. No experiment, Git write, maintained-file change or promotion was
performed in this round; all unrelated dirty work remains untouched.

### Bounded cost-interface closure, 2026-10-06

At the user's request, [COST_CONTRACT.md](COST_CONTRACT.md) now gives one
reporting contract for the old finite-panel and new unseen-input logarithmic
models. Every resource `C` is universal. The existing internal polynomial
powers are unchanged; activation/data evaluator calls and precision,
certificate acquisition, raw-label normalization, scale encoding and query
input/output are explicit extra charges, not fixed-problem constants.

The scoped supporting notes are
[COST_INTERFACE_PANEL.md](COST_INTERFACE_PANEL.md) and
[COST_INTERFACE_EVALUATORS.md](COST_INTERFACE_EVALUATORS.md). The panel
note supplies the nonmaterializing, linear-scratch collocation schedule
and an explicit sufficient envelope for the deterministic width gates.
The evaluator note expands phase-specific calls/precision and identifies
the input-precision dependence on tiny labels. The lead owns the combined
contract and shared links; the two scoped agents own only their respective
notes. No experiment or new broad compression proof was authorized.

This closes the reporting/scheduling ambiguities, not the still-unproved
finite-bit, accuracy-certified numerical simulation of the old compact ODE,
nor the inherited stochastic width thresholds. Obtaining scientific
certificates and implementing arbitrary mathematical activations cannot
be assigned an arbitrary universal cost. The lead reconstructed both
supporting notes and checked the exponent substitutions. A fresh
[bounded check](COST_CONTRACT_CHECK.md) found four specification issues,
all corrected and rechecked; no issue remains within that accounting
scope. It did not reprove inherited source theorems or the missing panel
numerical-training theorem. This is internal checking, not promotion.

### Parameter-explicit resource continuation, 2026-10-06

The user now asks to expose the dependence on sample count, inverse Gram
gap, label size and input dimension in every resource bound, preferably
with small polynomial degrees, and to give comparable accounting for the
authorized earlier predeclared-panel construction. This is a continuation
of the resource analysis, not a new claim that the previously unspecified
constants were polynomial. No poor dependence may be silently transferred
to the sufficient-width threshold. Real-coordinate arithmetic, numerical
precision, a vector-field evaluation and a complete numerical integration
are separate interfaces.

Fresh bounded author routes have disjoint write ownership:

- `panel_parameter_costs`: `FINITE_PANEL_PARAMETER_COSTS.md`, explicit
  panel-runtime arithmetic and the construction-cost boundary;
- `source_parameter_costs`: `PHYSICAL_PARAMETER_ACCOUNTING.md`, physical
  horizon, Lipschitz/analytic certificates, causal schedule and precision;
- `compiler_parameter_costs`: `COMPILER_PARAMETER_ACCOUNTING.md`, counted
  packet/compiler/seed algorithms before fixed-parameter absorption.

The lead owns the synthesis and full-label activation-envelope check.
The routes start from their specified source files, not one another's
working notes. These are scoped author derivations, not independent
promotion reviews. The required custom notation skill remains unreadable;
the explicit user notation contract is the fallback. No experiment,
maintained-book change, Git mutation or unrelated study edit is authorized.

The completed synthesis is
[PARAMETER_EXPLICIT_RESOURCES.md](PARAMETER_EXPLICIT_RESOURCES.md).
It proves a full-label finite-panel radius envelope `chi^(-1) <= beta^(36L)`,
counts its retained/live real coordinates and runtime arithmetic, and
supplies a controlled dense coefficient producer plus constructive spectral
selection for its offline initialization. The retained logarithmic exponent
five and original error/label scope are unchanged. The direct warmup has
inverse-normalized-gap degree four and can have sample degree five.

For the unseen decoder, the normalized adaptive physical schedule and a
counted numerical-certificate expansion give explicit polynomial resource
factors in sample count, dimension and inverse gap. Their degrees are large:
the conservative query count includes `(1+m/gamma)^584`, for example.
These are algorithmic bounds under the existing activation/data-primitive
and supplied-certificate interfaces, not a degree-three/four or practical
efficiency theorem. Input/evaluator implementation costs, stochastic source
thresholds and the fixed-label statistical-remainder absorption are stated
separately. The proof does not make the full success width polynomial.

The lead read all three complete routes, verified the BSS primary theorem
and exact metric correction, and checked the substitutions. Post-author
cross-checks reconstructed the finite-panel radius, coefficient accuracy,
work/memory assembly and the unseen polynomial table. These are internal
author checks, not promotion reviews. No executable experiment was run.

### Continuation authorized 2026-10-06

The user explicitly requested continuation to a complete proof and clarified
the objective as trading training-time storage/compute for expensive test-time
decoding. Any absolute logarithmic power is now acceptable, not just five.
The accuracy target is the existing dense-variability upper certificate,
not the stronger near-1/n matched-reference bound. The original nonlinear
model, all-time horizon and whole-sphere norm remain fixed.

The user confirmed that peak live decoding workspace counts. The second
clarification rejects retaining all past forward and backward passes and
prefers a compact representation with economical decoding where possible.
It does not require a saved raw trajectory. Compressed temporal summaries
and explicitly counted recomputation are candidate mechanisms, not automatic
solutions or permission to retain a dense initialization oracle. New proof
rounds must attack new mechanisms or the precise previous gaps, not
repeatedly restate them.
The earlier bounded-search stopping record below is historical; this request
authorizes a resumed campaign in the same study.

The current-state response-circuit construction is **proved under the
inherited dense certificates**. The latest strengthening is
[QUADRATIC_RESOURCE_RESULT.md](QUADRATIC_RESOURCE_RESULT.md): explicit
combined memory exponent 722, initialization `C n log(en)^1700`, all compact
updates `C log(en)^1700`, and query work `C n log(en)^2100`. Recalibration
is eliminated. Two isolated internal reviews checked the new implications
under the inherited interfaces. [RESULT.md](RESULT.md) indexes this and the
earlier variants. Completed-source preprocessing is still allowed, constants
and sufficient widths remain unquantified, and no practical speedup or
exponent-five claim is made. The study does not extend or retract the
inherited finite-panel theorem, and proves no general decoder-size lower bound.

### Current-state construction completed 2026-10-06

The latest user clarification favors decoding from the **present** state,
with compressed historical response moments allowed, rather than replaying
training from the data. The current route obeys this interface: retained
noisy scalar-history prefixes and a row-response circuit determine a
conditional query law. Fixed-prefix Fourier integration does not recompute
the scalar training updates. An expensive training-replay decoder is not
being substituted for this target.

[CURRENT_STATE_DECODER_CANDIDATE.md](CURRENT_STATE_DECODER_CANDIDATE.md)
assembles the theorem with an absolute logarithmic storage/workspace
exponent and error twice the inherited dense-pair certificate plus 1/n.
Its historical filename is retained for traceability. A fresh isolated
[complete-chain review](CURRENT_STATE_DECODER_FULL_REVIEW.md) passed the
supplemented construction, and a separate
[Fourier numerical reconstruction](FOURIER_ROW_PROGRAM_NUMERICAL_CHECK.md)
checked the fixed-prefix integration and precision bounds. Required
corrections are incorporated, including expanded innovation caps and a
small-denominator guard. These are internal checks, not promotion.

The new chain is a short causal physical solver; tiny additive matrix
noise with exact two-orientation Gaussian elimination; still smaller
scalar-update noise; positive weighted selection of row packets; and
conditional Fourier integration at the retained prefix. A posterior
maximal inequality plus robust medians supplies one
sphere/time-uniform event. This route evaluates the exact finite-width
proxy law, not a limiting population law. It therefore avoids assuming
the previously missing growing-program mean-field theorem.

Its explicit limitations are significant: source preprocessing can inspect
the completed finite dense computation; no preprocessing resource bound
is claimed; decoding can be extremely slow; the model is a response
circuit/causal algorithm, not a smaller ordinary gradient-flow network;
and no exponent-five or sharp fixed-parameter prefactor is claimed.

The complete finite-precision implementation also uses
[rational source selection](FINITE_PRECISION_SOURCE_SELECTION.md) and
[counted small-matrix functions](SMALL_MATRIX_FUNCTION_EVALUATION.md).
The theorem permits supplied finite fixed-problem bounds; it does not
prove a uniform compiler for arbitrary activation descriptions. The
scalar-register theorem uses the original activation primitives, while
the bit-space version states counted precision-access assumptions.

### Preprocessing and query-time clarification, 2026-10-06

The user asked whether the preprocessing caveat is new, whether decoding
can become reasonably fast, and whether the exponent is a model order.
[PREPROCESSING_AND_QUERY_COST.md](PREPROCESSING_AND_QUERY_COST.md) reconciles
the authorized older source: expensive offline computation of training
information was already allowed, although the present source-selection
procedure differs. It also proves that the training-prefix density can be
cached once per prefix without changing the guarantees. A separate scoped
check reconstructed that cache lemma and its numerical constants. This
amortizes denominator evaluations; it does not solve the numerator cost.

[QUERY_TIME_ROUTE.md](QUERY_TIME_ROUTE.md) records a bounded independent
analysis of rejection sampling, posterior log-concavity and Gaussian
Fourier replacement. Its explicit generic-row counterexamples and
small-frequency bound were reconstructed by the lead. They expose gaps
in those arguments, not an impossibility theorem for neural decoding.
No reasonable-time decoder preserving all qualifications was obtained.

[EXPONENT_ACCOUNTING.md](EXPONENT_ACCOUNTING.md) separates known packet
and raw-state exponents from complete decoder workspace. No numerical
value of the full absolute exponent has been extracted and audited:
physical-compiler and sensitivity polynomial degrees still need explicit
enumeration. The note gives conditional downstream formulas and counts
activation-evaluation time separately from its space assumption. The
existence-of-an-absolute-exponent theorem is unchanged. The exponent is
not a tunable order, and exponent five still belongs to the older
finite-panel theorem. No experiment or maintained-file change occurred.

### Efficient-query proof continuation, 2026-10-06

The user requested new work on efficient querying while retaining the
previous qualifications. This is a continuation of the same decoder
investigation, not authorization to relax its whole-sphere, complete-time,
original-model, current-state or absolute-polylogarithmic workspace
requirements. The user explicitly confirmed polynomial time in the compact
model's size. Polynomial-in-dense-width or dense-forward-pass time is not
an accepted substitute, even with compact memory. The numerical target is
therefore polynomial in retained description and logarithmic accuracy.

Three fresh scoped routes examine low-information posterior summaries,
offline query-circuit compilation, and direct nonlinear response expansion.
Their assigned flat outputs are EFFICIENT_QUERY_INFORMATION.md,
EFFICIENT_QUERY_COMPILATION.md and EFFICIENT_QUERY_DIRECT.md. They do not
read one another before freezing. The lead separately derived
[FAST_SMALL_MATRIX_FUNCTIONS.md](FAST_SMALL_MATRIX_FUNCTIONS.md), replacing
inverse-gap-length series by rational inversion and a rounded Newton
square-root iteration. The
[independent numerical check](FAST_SMALL_MATRIX_FUNCTIONS_CHECK.md)
passed this polynomial-time sublemma. It does not remove the conditional
integration grid. The direct response route also received a
[scoped independent reconstruction](EFFICIENT_QUERY_DIRECT_CHECK.md),
with its real and complex source assumptions kept explicit.
[EFFICIENT_QUERY_PROGRESS.md](EFFICIENT_QUERY_PROGRESS.md) records the
current claims and gaps. No efficient whole-query theorem, experiment,
source-study edit or promotion is currently claimed.

In the second round, the information and direct-response routes were
combined in
[EFFICIENT_QUERY_PHYSICAL_SYNTHESIS.md](EFFICIENT_QUERY_PHYSICAL_SYNTHESIS.md).
It proves a strictly feasible moment-constrained row tilt, finite
multiplier precision, and an identity-preserving compensated query rule.
The [scoped check](EFFICIENT_QUERY_PHYSICAL_SYNTHESIS_CHECK.md) passed those
claims, not the full adaptive neural application or the separate physical
forcing hypothesis. The lead reconstructed the conditional compiler and
[finite-seed cubature route](EFFICIENT_QUERY_RANDOMIZED_INTEGRATION.md).
The latter's possible polynomial-in-width cost is explicitly not an accepted
fallback after the user's clarification. Fast evaluation of the actual
moment-consistent nonlinear query remains the decisive open bridge.

### Dense-forward query budget, 2026-10-06

The latest user request relaxes query time to the cost of one ordinary
dense forward pass, interpreted as `O(L n^2 + d n)` primitive operations
for each fixed admissible problem. This supersedes the compact-polynomial
time requirement above for the current round only. It does not permit an
arbitrary polynomial in dense width, hidden dense workspace, a query panel
known in advance, training replay, a smaller label class, or loss of the
whole-sphere/whole-trajectory event. Peak query workspace still counts.

Three scoped author routes own `DENSE_BUDGET_SAMPLING.md`,
`DENSE_BUDGET_CONDITIONING.md`, and `DENSE_BUDGET_GEOMETRY.md`.
They supplied bounded-likelihood row integration, covariance-energy
comparison, and empirical cross-moment concentration without a history-Gram
gap. The latter also has a separate direct derivation in
`DENSE_BUDGET_SELF_NORMALIZED.md`. Followups completed
`DENSE_BUDGET_ROBUST_CUBATURE.md` and `DENSE_BUDGET_TILT_COMPILATION.md`.
The actual finite nonlinear passive-query identification and resource/
probability assembly are now in
[DENSE_BUDGET_DECODER_CANDIDATE.md](DENSE_BUDGET_DECODER_CANDIDATE.md),
with the clean statement in [DENSE_BUDGET_RESULT.md](DENSE_BUDGET_RESULT.md).

The result has absolute-polylogarithmic retained storage and peak query
workspace, with `n^(3/2)` times an absolute logarithmic power in primitive
query work, hence eventually within `O(L n^2 + d n)`. It preserves the
dense upper-certificate scale, with error `3 b_n(delta/256)`, not the exact
old `2 b_n + 1/n` expression. Constants and sufficient widths remain
fixed-problem dependent; the width threshold is unquantified. No exponent
five, compact-polynomial query time, practical runtime, or training speedup
is claimed.

The isolated [bridge check](DENSE_BUDGET_BRIDGE_CHECK.md) required one
precision correction: privately acquired numerical prefixes need not be
deterministic roundings of the ideal prefix. The revised proof compares
every prefix in the certified error ball to the same proof center before
substituting the actual private acquisition. That correction, distinct
history bases, and the explicit probability budget have been incorporated.
The separate [numerical check](DENSE_BUDGET_NUMERICAL_CHECK.md) reconstructed
the compiled-law entropy bound, buffered Gram acquisition, whole-domain
finite-seed integration and full cost; its revised-assembly check passed.
The isolated bridge reviewer then read the complete compiler and cubature
notes and passed the corrected complete assembly under the inherited
certificates and named numerical interfaces. This final recheck is Section 8
of its report, for assembly SHA-256
`931227ba250cb442013f1ecd42e1fea314b1efa22879cdd12055220fb7769c93`.
These are internal checks under the inherited source certificates, not
promotion into the maintained book.

The complete error before absorption is `2 b_n + C log(n)^(C_L)/sqrt(n)`;
the fixed-depth exponent here is an error exponent, not a storage exponent.
The old slower Fourier result remains valid and separate. No experiment,
Git operation, promotion, or source-study edit is part of this continuation.

### Dense-budget initialization and updates, 2026-10-06

The user requested continuation to remove the superpolynomial construction
and training-summary calibration costs, targeting at most dense-scale
`O(L n^2 + d n)` primitive work, and to extract a numerical absolute
storage exponent. This is a continuation of the same unseen-input decoder
investigation. All earlier scope, complete-trajectory/sphere error,
current-state querying and counted post-construction workspace requirements
remain in force. Dense-sized preprocessing memory was previously permitted;
no new query panel, activation restriction, label cap or history gap is
authorized. The comparison remains the dense-pair upper-certificate scale,
not near-1/n matched-root accuracy. No practical-width assertion follows
from an eventual asymptotic cost bound.

This continuation is complete under the inherited dense/source interfaces.
[QUADRATIC_RESOURCE_RESULT.md](QUADRATIC_RESOURCE_RESULT.md) assembles
four new proofs: [the explicit compiler](EXPLICIT_COMPILER_EXPONENT.md),
[streaming initialization](QUADRATIC_INITIALIZATION.md),
[recalibration-free moments](RECALIBRATION_FREE_MOMENTS.md), and
[the uniform short-seed implementation](SHORT_SEED_PRIOR_BLOCKS.md).
The posterior marginal is proof-only; observed buffered Grams and robust
Gaussian-prior block means replace fitted-law calibration. Nisan's verified
block finite-state generator supplies one repeatable seed without a
repeated-read assumption. An explicit query-whitening precision extension
closes the degree accounting.

The clean bounds are retained bits `C log(en)^245`, retained plus peak
post-initialization bits `C log(en)^722`, warmup work `C n log(en)^1700`,
all compact update work `C log(en)^1700`, and per-query work
`C n log(en)^2100`. Warmup memory is
`C [n log(en)^108 + log(en)^600]` bits, not polylogarithmic. Each work
bound is eventually below dense quadratic work. Source generation uses
a fresh original-law virtual dense source rather than reading a prescribed
realized dense root; the unchanged probability guarantee is at the
independent dense-reference upper-certificate scale, `3 b_n(delta/256)`.

The [isolated mathematical review](QUADRATIC_RESOURCE_ISOLATED_REVIEW.md)
and [isolated numerical review](QUADRATIC_NUMERICS_ISOLATED_REVIEW.md)
both passed within their expressly inherited-interface scopes. Separate
author cross-checks cover [initialization](QUADRATIC_INITIALIZATION_CHECK.md)
and [the compiler/seed interface](SHORT_SEED_COMPILER_CHECK.md).
These are not promotion reviews. Fixed activation/data primitives remain
the work convention; actual precision-evaluator costs are stated separately.
No practical width threshold, sharp fixed-parameter prefactor, strictly
online warmup, or exponent-five unseen-query construction is established.
No experiment, maintained-source edit, or Git mutation was performed.

Earlier partial results and route records (not dependencies substituted
for the completed chain):

- [COMPARISON_DECODER.md](COMPARISON_DECODER.md), by
  unseen_comparison_decoder: exact current-feature projection and its
  moving-span remainder; an admissible spanning-data counterexample to
  input-linear interpolation; conditional error-transfer estimates.
- [UNIFORM_SOURCE_DECODER.md](UNIFORM_SOURCE_DECODER.md), by
  unseen_uniform_sources: exact omitted-action identities and a complete
  low-storage, whole-sphere initial-velocity decoder for deep sine networks.
  Its proof does not cover the subsequent nonlinear training trajectory.
- [POPULATION_DECODER.md](POPULATION_DECODER.md), by
  unseen_population_decoder: a conditional temporal Gaussian-program
  architecture with the desired memory exponent. Quantitative growing-history
  comparison, numerical population stability/evaluation and autonomous
  all-time continuation remain unproved.
- [ANCHOR_DECODER.md](ANCHOR_DECODER.md), by the lead: an exact nearest-anchor
  error extension and the limitations of its covering/storage certificate.
- [Historical synthesis, Section 3](HISTORICAL_ROUTE_RESULTS.md) proves,
  conditional on the inherited general variability
  lower theorem, that a decoder independent of the dense realization cannot
  achieve the stronger near-1/n matched-reference guarantee when m>=2 and
  labels are nonzero. This does not rule out root-width accuracy or an
  initialization-dependent compact decoder.

Continuation notes; check status is scoped to each claim:

- [GROWING_PROGRAM_STABILITY.md](GROWING_PROGRAM_STABILITY.md), by
  decoder_population_stability: inverse-free Gaussian response-energy and
  scalar matrix-divergence estimates, including adaptive fields, good-set
  localization and analytic temporal jets. These are source estimates;
  identification with a compact full nonlinear program remains separate.
- [LABEL_SERIES_DECODER.md](LABEL_SERIES_DECODER.md), by
  decoder_label_series: all-time damping and endpoints for every fixed
  label coefficient of the actual dense flow; a conditional complex-label
  continuation theorem; and a Gaussian-averaging counterexample to a generic
  positive-radius inference. No width-uniform full-label series is proved.
- [RECOMPUTATION_SPACE.md](RECOMPUTATION_SPACE.md), by
  decoder_recompute_space: a streamed dense-flow evaluator using
  absolute-polylogarithmic working memory, conditional on repeatable access
  to its initialized coordinates and scalar activation evaluation. The
  initialized information still counts and is not compressed by this result.
  Its random-tape and generic-integration obstructions are explicitly scoped,
  not decoder impossibility results.
- [ROOT_RESPONSE_AND_COVARIANCE.md](ROOT_RESPONSE_AND_COVARIANCE.md), by
  the lead: RMS-only good-set response localization, inverse-free Gaussian
  covariance coupling, and an exact chronological-factor counterexample.
  [Its check](ROOT_RESPONSE_AND_COVARIANCE_CHECK.md) reconstructs Sections
  1--3; the candidate now explicitly restricts the dense derivative
  specialization to finite times, as the check requested.
- [SOURCE_SUPREMUM_EXTENSION.md](SOURCE_SUPREMUM_EXTENSION.md), by the
  lead: proves the actual complex good-pair premise for training and forward
  query sources, and a simultaneous two-time/whole-sphere scalar defect
  estimate. [Its complete check](SOURCE_SUPREMUM_EXTENSION_CHECK.md)
  passes the frozen finite-horizon statement, without claiming a decoder.
- [GAUSSIAN_EXPECTATION_SPACE.md](GAUSSIAN_EXPECTATION_SPACE.md), by
  decoder_label_series: exact streamed polynomial expectation with counted
  workspace and no Gaussian root oracle, together with its depth-dependent
  activation-degree limitation. Author-checked, not a full target proof.
- [SHORT_CAUSAL_TRAINING_PROGRAM.md](SHORT_CAUSAL_TRAINING_PROGRAM.md),
  by the lead: a positive-endpoint collocation program with O(log^8 n)
  initialized calls. Its separate complete check reconstructed the proof
  and verified the patch-length/counting corrections.
- [NOISY_TWO_ORIENTATION_TRANSCRIPT.md](NOISY_TWO_ORIENTATION_TRANSCRIPT.md)
  and [NOISY_SCALAR_HISTORY_ACQUISITION.md](NOISY_SCALAR_HISTORY_ACQUISITION.md),
  by decoder_population_stability: exact finite-width noisy Gaussian row
  elimination, and compact autonomous acquisition of every scalar prefix
  with quantified perturbation and rounding. They distinguish the exact
  matrix law from the scalar-noise surrogate.
- [FOURIER_ROW_PROGRAM_EVALUATION.md](FOURIER_ROW_PROGRAM_EVALUATION.md),
  by decoder_recompute_space: deterministic counted-space integration,
  including fixed-prefix conditional expectations and retained-state
  precision. It uses no dense-root oracle or training-prefix integration.
- [CONDITIONAL_PREFIX_CENTER.md](CONDITIONAL_PREFIX_CENTER.md), by
  decoder_label_series: a whole-prefix posterior maximal bound and robust
  median transfer, with the necessary conditional query-noise qualification.
- [PHYSICAL_NOISY_PROGRAM_BRIDGE.md](PHYSICAL_NOISY_PROGRAM_BRIDGE.md),
  by the lead: coupling of the physical short program to the globally
  regularized row program; corrected innovation-moment caps and
  completed-patch semantics passed separate reconstruction.

Additional bounded-route outputs include HESSIAN_RESPONSE_CLOSURE.md
(explicit two-reuse Gaussian law, not a general induction),
RESPONSE_TRACE_SKETCH.md (scalar response sketches, not individual response
identification), POPULATION_EVALUATION_SPACE.md (a specified capped Gaussian
program evaluator), EXACT_TRANSCRIPT_UNIFORM_LAW.md (finite transcript
and adaptive-coefficient concentration), FINITE_TRANSCRIPT_WEIGHTED_REPLAY.md
(exact weighted finite-program compression), and PRG_RECOMPUTATION_AUDIT.md
(the counted random-access obstruction and conditional PRG interface).
These are not promoted or claimed to be full decoder proofs.

The lead has reconstructed the label-recursion normalization and damping,
the complex-label bootstrap and counterexample, and Sections 1--5 of the
recomputation note. Its [independent check](RECOMPUTATION_SPACE_CHECK.md)
subsequently prompted explicit projection tolerances, query/time precision
interfaces, a common activation complexity exponent and numerical-bound
certificates. These corrections have been verified at candidate SHA-256
`74adb390a71c76ef21831ac76005288d6827fdc8db072dc271b2c0ea32f2dba3`.
Those earlier checks support their partial mechanisms, not a complete
decoder by themselves; the later full-chain check is recorded above.
The routes remain within
their assigned inputs; no experiments, Git mutations or promotions occurred.

The routes began in fresh contexts with disjoint specified input scopes.
Supervisory followups requested concrete audits and freezing; after the
population route reported its initial mechanism, the lead also suggested a
label-series alternative and supplied the independent-center obstruction.
Its note records this provenance. These are scoped author routes, not blind
promotion reviews. No route read another route's working note before freezing.

The lead read all three complete notes, reconstructed the algebraic identities
and counterexamples, and checked the initial-velocity concentration proof.
Maintained Gaussian-conditioning Section 2 and integrated-memory Sections
13.1--13.4 were read to check the population candidate's exact finite inputs;
they do not close its quantitative or autonomy gaps.

After freezing its own route, unseen_uniform_sources separately reconstructed
the complete anchor note and the earlier synthesis's Sections 1--3 against the full inherited
lower statement. It found no algebraic or probability error and requested two
qualifications now incorporated: procedural grids invalidate an unrestricted
anchor-list storage lower bound, and bare n^(-1/2+o(1)) does not specify a
tolerance above the dense lower obstruction. The scope of that check excludes
the full desired theorem and the population architecture. No internal PASS
for the requested theorem was claimed at that earlier stage. The later
complete construction has its own isolated review, as recorded above.

## Reproduction, limits and handoff

This is a proof-only study. Read RESULT and its linked derivations/checks.
They record model assumptions, exact versus conditional claims, allowed
inputs and source snapshots. No numerical experiment, executable compressor,
preprocessing-time improvement, Git commit or maintained-file change was
made. A total compact-decoder bit bound is now proved under its stated
precision interfaces. All unrelated concurrent work remains untouched.

The finite-width noisy-row/Fourier route supplies an equivalent nonlinear
response description with one sphere/time-uniform bound and counted
workspace. It does not complete the earlier structured-Hessian/population
route, which remains an incomplete alternative. Near-1/n fidelity,
exponent five, compact-polynomial or practically quantified query time,
and efficient or strictly online preprocessing remain open. The later
dense-forward-budget variant is summarized above. Earlier stopping language is preserved only
as provenance in the historical synthesis, not as the current outcome.
