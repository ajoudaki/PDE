# Advisory coverage: decisions for the maintained book and code

9 September 2026. This is an editorial disposition, not a new mathematical
certificate or a competing repository design. “Included” means that the actual
argument or implementation is in `docs/` or `code/`; an archive, link or sentence
in this ledger does not qualify. The current layout remains
`docs/`, `code/`, flat `studies/`, and separate `data/`.

## Judgment and current changes

The advisory identifies real omissions. The selected library must not be
described as a complete incorporation of all established research. In
particular, the computational MFP contribution, exact scoped Stieltjes
certificates, initialization tradeoffs and generic-correlation partials are not
replaced by the existing global-limit chapters. Their narrower scope is not a
reason to call them speculative.

The initial advisory revision substantially expanded the actual
[book introduction](../../docs/README.md): the two scientific mysteries,
mechanism-preserving approximations, the elementary prescribed-accuracy bridge,
subsequent limits, generalization frontier, and careful prior-art positioning.
That revision left the eight proof chapters and implementation unchanged.
The earlier accepted input edition is frozen in
[the round-2 manifest](reviews/INTEGRATION_ROUND2_LIBRARY_INPUTS.json); the new
guide has a fresh CLEAN [isolated review](reviews/GUIDE_ADVISORY_INTEGRATION.md).
The later user-authorized incorporation is recorded in
[INCORPORATION_ACCEPTANCE.md](INCORPORATION_ACCEPTANCE.md), with exact proof
fragments, source provenance and independent review rounds. The narrative-only
description no longer applies to the current book: the correlated-data partials,
initialization comparison, finite-calculus implementation, quantitative theorem
and exact-capture comparisons below are now actually incorporated.

The three agreed editorial priorities are:

1. **Correlated-data progress and activation tradeoffs:** integrate the closed
   first-layer compactness and finite-fitting partials, and compare the existing
   initialization results in the current special-data/finite-controls chapters.
   This makes visible what is already known outside orthogonal benchmarks.
2. **A small MFP computational core:** specify finite jets, forest factorization
   and independently checked rational certificate primitives before importing
   large tables or historical optimized engines. Extend the calculus chapter
   and existing code rather than preserve every compiler as a public API.
3. **Discretization and representation contrasts:** add the exact-compiler
   fixed-program remainder theorem and carefully delimited shallow/spectral/
   all-depth linear comparisons, after closing their particular dependencies.

These are assembly priorities, not new experiments or proof-search campaigns.
Initialization comparison means incorporating already proved geometry, not
spending another campaign optimizing an initial Gram while trained-response
control remains open. No currently justified extra data or optimizer assumption
is supplied by this coverage pass. Keep correlated data and genuinely nonlinear
hidden learning in the main target; auxiliary caps and changed architectures
remain diagnostic results, not replacements for that target.

## Family-by-family disposition

| Advisory family | Actual maintained coverage | Decision and remaining boundary |
|---|---|---|
| 1. Scientific narrative | Expanded in this revision, with explicit accuracy-transfer proof and cited non-exhaustive prior-art orientation | Incorporated; fresh isolated guide review CLEAN. No global novelty, optimization or generalization claim is added. |
| 2. MFP computational machinery | Now includes complete moving L2 one-sample physical jets through order three, leading Gaussian forest expectation factorization, canonical colored-forest keys and rational reversion/determinant/certificate primitives, alongside the earlier foundations | Small common core incorporated with two independent complete proof/code reviews per module. General-depth/high-order packed compilers, pruning engines and historical coefficient tables are not promoted. |
| 3. Quantitative discretization and physical loss | Fixed-program width theorem; exact-compiler cubic step-doubling coefficient and explicit fifth-order remainder; moving physical-loss jets through order three | Contained Section 8 has two fresh full CLEAN reviews. Depth/update count are fixed and its clock is feature ascent with order-one readout. Sharper shallow/linear bounds, other physical pullback expansions and growing-update claims remain separate. |
| 4. Stieltjes and formal Taylor | Now includes the complete quadratic zero-first-mobility annealed initialization-jet bridge, six rational moments, negative shifted determinant and polynomial witness, with a direct coefficient-regeneration command; also the earlier norm/jet obstructions and smooth-ODE correction | Scoped axis certificate incorporated and independently regenerated by different algebraic routes. Strictly positive-metric extension, canonical order-17 prefix, and quadratic formal factorial-divergence proof remain separate unpromoted items. No unit-metric or positive-time no-go is inferred. |
| 5. Shallow and broader linear capture | Existing L3 operator/GF/GD theorem and restricted nonclosure; now also shallow nonlinear marked GF, L2 linear spectral GF with fitting, and every-fixed-depth linear operator GF with trace-norm increment control | Complete Sections 8–12 and trace-class foundations have two fresh full CLEAN reviews. Added results are one-input, order-one-readout and GF-only; all-depth fitting, arbitrary data and new raw-GD limits are not inferred. |
| 6. Broader nonlinear and correlated-data progress | Earlier global families plus complete generic-correlation L2 arctangent first-layer GF/raw-GD compactness, mixed-activation finite-GF fitting/endpoints, and permanent first-gate mass with the necessary augmented event | These partials are incorporated with two independent complete reviews each; first-layer notation repairs received fresh complete reviews. They do not supply a unique generic-correlation population or a mixed-model GD/feature-velocity theorem. Broad activation/local and perturbation families retain their specific import/ancestral-review gates. |
| 7. Initialization geometry | Existing gain-based results plus a complete Part V: sharp odd-mixture bounds and matching examples, convex-offset contraction despite scalar nonaffinity, calibrated sequential depth geometry, and absolute/relative comparisons | Incorporated after explicit statement/endpoint repairs and two fresh complete CLEAN reviews of the final version. Every width result fixes depth and activation; the later calibrated depth limit is sequential. None provides trained-flow continuation. |
| 8. Clipping/filtering/continuation | Global fixed coordinate-query-cap population theorem; separate finite metric projection, integrated L1 defect and sufficient C sqrt(n) exactness | Given-space dissipative caps and integrated-query compression are useful missing auxiliaries. Growing-cap comparison has a specialized concentration-proof containment gate and, even if imported, would not give a common varying-cap population limit. |
| 9. Further negatives and finite reductions | Restricted linear bounded-contraction nonclosure; some norm/jet obstructions; general finite energy continuation | Worth adding selected exact QI/IQ and RMS formulas and rigorously scoped obstruction arguments. Preserve the unresolved canonical quadratic adaptive bridge; deterministic reachable Hessian examples are not typical-Gaussian counterexamples. |
| 10. Response compiler and dense ResNet | Finite feedforward APIs and the distinct scalar-particle continuous-depth theorem | Curvature-word algebra and dense chronological/variational identities are substantive omissions. A small algebraic module is a candidate. Dense solvers and empirical panels need a complete accepted reproduction chain; dense-limit and hierarchy claims remain open. |

## Decisive scope checks and source routes

### MFP, coefficients and physical loss

The [Gaussian chapter](../../docs/gaussian_calculus.md) already proves a fixed
depth, fixed update-count, fixed nonzero feature-step width theorem. The older
completeness audit's “missing” classification of that theorem has been
superseded. Section 7 now adds the moving finite-jet oracle, forest
factorization and canonical keys, and a small exact certificate generator.
It still does not contain a general forest compiler, canonical counting engine,
or the complete high-order coefficient machinery.

The [finite jet oracle](../mfp_gaussian_calculus/compiler/finite_width_jet.py)
propagates ordinary Taylor coefficients through order three for its particular
two-hidden-layer finite model. Its recurrence is an exact differentiation
identity; float64 execution is not exact rational arithmetic. The
[quadratic compiler](../mfp_quadratic_compiler/README.md) contributes decorated
forests, leading-width component factorization and Leibniz convolution. The
[tree enumerator](../mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/count_free_trees.py)
counts abstract shapes; that count is not certification of weighted,
rank-labelled, width-audited contractions. Fixed-order tables and hidden
activation-RMS heads retain their exact observable and generator obligations.

For discretization, the primary
[unconditional audit](../mfp_depth_time_doubling/AUDIT_UNCONDITIONAL.md) makes a
useful refinement to a coarse dependency list: its accepted coefficient is the
**exact-compiler** coefficient from `WIDTH_DEPTH_TIME.md` and
`COMPILER_DEPTH_TIME.md`, expressly not the compact nine-moment coefficient
or a claim in `CUBIC_DEPTH_TIME.md`. Its C12 hypotheses yield an explicit
fifth-order remainder for every fixed finite depth/update pair. This does not
establish the stronger update-uniform remainder or the compact coefficient
identity. The complete Section 8 assembly now follows that exact route,
including singular-covariance differentiation and its existing fixed-program
probability dependency; both full reviews are clean. The separate
[L2 half-step proof](../mfp_quantitative_width_first_bound/PROOF.md) takes width
first at fixed nonzero step; differentiation is then on the identified program.

The [physical-loss expansion](../mfp_loss_gradient_time_doubling/LOSS_GRADIENT_EXPANSION.md)
and [time-change analysis](../mfp_loss_time_doubling/LOSS_TIMECHANGE_ANALYSIS.md)
contain useful algebra beyond the now-incorporated third-order physical-flow
clock calculation. Their higher pullback words
and fixed-update Taylor identities should be distinguished from a neural
probability identification and a horizon-uniform remainder bound. Raw loss-GD
has a state-dependent residual multiplier. A continuous residual clock does
not turn it into constant-step feature ascent. These sources also use a
different residual sign and half-loss convention; promotion must translate
them to the shared notation rather than transplant their symbols.

### Stieltjes and Taylor: useful negatives, not universal nonexistence

The [block-metric report](../stieltjes_resolution/BLOCK_METRIC_RESOLUTION.md)
and [rational generator](../stieltjes_resolution/block_metric_counterexample.py)
supplied the compact axis certificate now proved in Section 7.2 with its direct
expectation argument and independent implementation. This is a
diagnostic negative for a specified model/metric family, not a proposal to
freeze layers in the main learning theorem. The maintained implementation has
no historical regression-file/hash dependency: it derives the coefficients
directly and tests the complete displayed certificate.
The more informative all-blocks-training extension at positive metric parameter
uses the [positive-parameter recurrence](../stieltjes_resolution/POSITIVE_ALPHA_JET_DERIVATION.md);
its generation and probabilistic interpretation need separate acceptance.

The retained [canonical calculation](../stieltjes_resolution/canonical_high_order/README.md)
reaches output order **17**, eight moments and positive ordinary/shifted 4x4
tests. A hidden ninth moment obtained by an identity is not output order 19.
Neither those positive tests nor a six-moment metric-parameter transition
settles canonical all-order Stieltjes positivity or identifies a trajectory.

The quadratic formal factorial-growth argument and its consequences for
specified coefficientwise-positive approximation families are also absent.
They are worth a scoped presentation after their coefficient/probability
chain is checked. Formal divergence does not, without identification, establish
an actual training initial layer. It does not rule out general smooth ODEs,
signed resummations or arbitrary operator descriptions. The existing smooth-ODE
correction must remain beside, not be displaced by, a stronger scoped negative.

### Shallow, linear and correlated-data partials

The [shallow theorem](../rcgc_shallow/GENERIC_L1_THEOREM.md),
[L2 spectral construction](../mfp_identity_compiler/linear_gaussian_program/depth2_autonomous_mse_closure/THEOREM_AND_PROOF.md)
and [fixed-depth linear theorem](../rcgc_linear_depth/LINEAR_FIXED_DEPTH_THEOREM.md)
are genuinely different capture mechanisms. Complete Sections 8–12 now contain
their characteristic/clock, rooted spectral and two-endpoint operator proofs.
The source's short Wick-counting and sharp-norm references are replaced by a
contained fixed-word argument and a sufficient elementary norm bound. The
spectral measure, including its negative atom, is verified without importing
an inversion theorem. Section 2.A also derives the required trace-class
foundations. Both fresh complete amended-chapter reviews are CLEAN.
The new statements retain GF-only, one-input and order-one-readout scope;
the existing L3 raw-GD theorem is neither a missing dependency nor permission
to attach a GD conclusion to every new family.

For opposite labels at general correlations, the
[all-angle first-layer proof](../four_thread_consolidation/expanded_sources/OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/ALL_ANGLE_FIRST_LAYER_COMPACTNESS_COMPLETE_PROOF.md)
is a particularly valuable partial: actual GF/raw-GD first-layer path and
velocity compact containment, row reconstruction and no first-layer kinetic
defect. Its controlled kernel conclusion is residual-weighted, node-controlled
L1 convergence along convergent subsequences. It is not an unweighted first
kernel theorem, second-layer identification, full-sequence result or equality
of GF/GD subsequential limits.

The [mixed-activation clock theorem](../four_thread_consolidation/expanded_sources/OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/COMPACT_FIRST_LINEAR_TAIL_TOP_CLOCK.md)
gives finite-GF fitting, residual clocks and endpoints at interior correlations,
with a compact first derivative and top activation `z+epsilon arctan(z)`.
The [gate extension and audit](../four_thread_consolidation/expanded_sources/OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/COMPACT_LINEAR_TAIL_PERMANENT_FIRST_GATES_REVIEW.md)
require the augmented strip-count event; dropping it has an explicit
counterexample. Positive unsaturated mass is not a lower bound on feature
velocity. No mixed-model GD or population theorem is added by these results.

Broad L2 activation, affine-first arbitrary-data and local C1,1 population
families retain the specialized probability-import gates in the
[completeness audit](source_audits/PROMOTION_COMPLETENESS.md). The broad local
finite-GF corollary is not a separate open bridge: it inherits the local
population theorem's qualification. Perturbed two-sample families have a
different ancestral proof-review gate. Consolidate superseded threshold powers
into one current entry per model: the two-input L3 arctangent `delta^2`
refinement is not the same scope as a general-shape or all-depth bound. These
qualifications are not counterexamples to the claimed statements.

### Initialization and continuation

The [odd-mixture report](../odd_mixture_general_depth/REPORT.md),
[convex-offset report](../convex_offset_all_depths/REPORT.md) and
[calibrated manuscript](../calibrated_near_identity_reviews/manuscript.md)
now form one contained Part V, retaining each exact activation and normalization.
Odd-mixture absolute versus normalized conditioning have different depth
scales; relative scalar nonaffinity can decay despite normalized sample
conditioning. Literal convex offsets can contract initialized pair distances
geometrically, obstructing a depth-uniform kernel-floor argument, not each
fixed-depth theorem. Calibrated near-identity initialization gives a sequential
width-first/depth-second correlation evolution, not joint trained-depth control.
These proofs are separate from the gain-based three-sample training result;
the latter's initialized Gram estimate is not used as a substitute. The new
comparison also explicitly proves why scalar gain normalization generally
changes the next nonlinear argument, with the identity-scaling exception.

The [moderate-sine report](../moderate_sine_global/RESULT.md) also contains finite
and endpoint partials beyond general finite-GF existence. Strong endpoints of
an existing path are not restartability; the global tail premise remains open.
These are reasons for qualified placement, not for erasing the finite partials.

The three clipping scales/rules already have a precise
[ledger entry](PROMOTION_LEDGER.md). The
[growing-cap comparison](../project_wide_audit_2026_09_08/sources/arctan_destination/l3-full-resolution-9nbD4z/FILTERED_QUERY_GROWING_CLIP_TRANSFER.md)
includes `sqrt(log n)` but does not construct a common varying-cap population
limit. Its six-file chain invokes specialized matrix concentration whose full
proof is not contained in the book. This is separate from the missing canonical
cap-removal premise. The
[given-space capped theorem](../practical_fixed_depth2/CAPS_MANUSCRIPT.md)
and [integrated-query compression](../project_wide_audit_2026_09_08/sources/arctan_destination/l3-full-resolution-9nbD4z/INTEGRATED_INITIAL_QUERY_COMPRESSION.md)
are useful auxiliary candidates: prescribed operator-space existence does not
construct the canonical Gaussian action space, and sampling an actual
Lipschitz query path does not establish causal autonomous approximation.

### Additional obstructions, exact reductions and dense ResNet

Use the reconciled [quadratic/ReLU assessment](../project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md),
not an old “no-go” title. Width-first fixed-update quadratic Euler results and
the [arbitrary-diagonal frozen-bottom theorem](../mfp_joint_width_mesh_quadratic/ARBITRARY_DIAGONAL_FROZEN_THEOREM_AND_FULL_GAP.md)
have scopes distinct from the canonical finite-GF initial layer, whose adaptive
bridge is unresolved. ReLU failure of a prescribed classical GF at some
finite-width initializations is distinct from local Euler tightness and from
macroscopic nonexistence. The
[reachable Hessian witness](../project_wide_audit_2026_09_08/sources/arctan_destination/l3-full-resolution-9nbD4z/ACTUAL_ZERO_READOUT_REACHABLE_HESSIAN.md)
uses deterministic correlated hidden initialization, not typical independent
Gaussians. Its failure of a deterministic signed pointwise bound does not
refute the canonical population theorem.

The [mixed quadratic/identity reductions](../mfp_quadratic_compiler/autonomous_single_source_closure/THEOREM_AND_AUDIT.md)
and [differentiated RMS identities](../mfp_quadratic_compiler/rms_normalized_operator_closure/FINITE_WIDTH_THEOREM.md)
are finite algebra worth incorporating after explicit verification and notation
translation. Spectra-only insufficiency is an orientation-sensitive statement,
not impossibility of retaining the actual operators. Correct finite RMS energy
does not close population tails or uniqueness.

The [response/curvature compiler](../rcgc_compiler/rcgc_compiler.py) has a small
algebraic core distinct from Gaussian integration. Its expansion of nested
curvature returns is useful; classifying a word that uses multiple matrices
identifies an analytic obligation, not a nonclosure or convergence certificate.
Its historical tests do not by themselves establish a maintained API.

The [reconciled dense-ResNet state](../resnet_program_history/CURRENT_RESEARCH_STATE.md)
separates exact finite chronological memory and projected-gradient geometry
from unproved dense-limit identification and arbitrary-accuracy hierarchy
convergence. These exact identities merit a future section in the current
continuous-depth chapter with an explicit different-model boundary. Internal
geometry is stated for sufficiently regular candidate solutions, not used to
assert general well-posedness. Parity corrections and later adverse cutoff
evidence must accompany any empirical hierarchy discussion. The existing
scalar-particle theorem is not evidence for the dense Gaussian candidate.

## Implementation and empirical acceptance

A result need not have a simulation to be valuable. For an empirical inclusion,
however, require the complete chain: mathematical specification and claim,
maintained implementation, parameters/seeds and environment, commands,
generated products under `data/established/`, independent checks, and the
displayed result. Performance claims also need a specified workload and
measurement procedure. Agreement between two evaluators of one recurrence
does not verify that recurrence's network interpretation. Reproducing a table
from retained coefficients is not regenerating its coefficients.

No historical coefficient campaign, training experiment, installation, native
build, seal reset or source-budget reuse was performed. The small deterministic
certificate is newly regenerated by the maintained exact module and independently
checked; it does not use a retained table. No historical array or empirical
figure was promoted. Existing frozen campaigns remain frozen. The finite
reference, moving jets and exact primitives are accepted at their stated scopes,
not advertised as a population solver or full MFP compiler.

## Evidence and read coverage

This disposition combines the earlier full-source consolidation and its
qualifications with bounded current coverage checks. It is **not a fresh
complete proof/code audit of the 105 study folders**. The older completeness
audit is retained unchanged even where current chapters supersede its rows.

The coordinator reread the current guide, notation, promotion ledger and
completeness audit, the older master's relevant scientific/strategic sections,
the complete exact-compiler unconditional audit, and selected statements and
scope sections of the quantitative half-step, physical-loss and dense-ResNet
sources. Primary external papers were checked for the guide's narrow context
claims, not used as proof imports or represented as freshly proof-audited.

Two isolated read-only sidecars checked disjoint coverage families:
[MFP/Stieltjes/curvature machinery](source_audits/ADVISORY_MFP_STIELTJES_COMPILER.md)
and [initialization/correlated-data partials](source_audits/ADVISORY_GEOMETRY_CORRELATED_DATA.md). Their
reports record which primary files were read fully or selectively and expressly
decline fresh proof/generator certification. The guide's independent review is
separate from those coverage recommendations. Later incorporation uses complete
source assemblies and fresh paired full-proof/code reviews, including new
rounds after every required correction. Those are stronger, separately scoped
checks than the earlier coverage sidecars. Exact reports and final acceptance
status are recorded in [VALIDATION.md](VALIDATION.md) and
[INCORPORATION_ACCEPTANCE.md](INCORPORATION_ACCEPTANCE.md).
