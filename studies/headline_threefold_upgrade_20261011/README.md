# Three proposed upgrades of the compression headline

## Follow-up: final figure collection and notation-table presentation

At the user's request, `paper/compact_figures.tex` now places every top-level
static figure asset after the bibliography, with concise captions. The user
explicitly excluded interactive-explainer thumbnails. There are 44 PDF stems
and 50 included panels: `experimental_gallery.pdf` contributes all seven
pages; same-stem PNG/SVG format copies are not repeated. Alternate assemblies
are retained and identified. No figure was regenerated and no experiment was
run. The symbol table's count column and counting prose are removed, with all
symbols and definitions retained.

The bounded [caption inventory](FIGURE_CAPTION_INVENTORY.md) and
[layout inventory](FIGURE_LAYOUT_INVENTORY.md) use only the assigned paper
assets and their adjacent metadata, not the other studies named by their
historical producers. Captions distinguish model-discrepancy RMS from label
error, individual fitted endpoints from common times, old eight-checkpoint
plots from the newer replay, and the old seeded decoder from the later
Taylor-family plots. Existing artwork labels are not silently relabelled.
The plots remain earlier illustrations, not certificates for the current
theorem; this distinction is also reflected in the abstract.

The build is retained at
`data/generated/headline_threefold_upgrade_20261011/figure_appendix.833uww/`.
It has 113 pages: the figure collection occupies pages 90–113. Nonfloating
image/caption blocks avoid float-only or orphan-caption pages; tall galleries
have individual height limits. The final log has no unresolved references,
overfull or underfull boxes, or new warnings; the inherited `amsmath`
compatibility warning remains. The proof modules and theorem statements are
unchanged. `SHORTEN_check.py` permits only the requested relocation and exact
figure/table editorial edits in the main file, while continuing to check the
older scientific sources, references, and book preservation.
The new PDF has SHA-256
`d922d0397a1646189af4e12e4fabe45a7c40ad87c3c9226bb17ed5dd999f8666`.
The scoped Terra build check and coordinator inspected the rendered collection:
all 50 asset-page pairs occur once, with no blank pages, stranded captions, or
visible clipping. The final contact sheet and mechanical evidence are in the
build directory. The coordinator also checked the compiled two-column symbol
table (Symbols/Meaning) and published the checked PDF as `paper/compact.pdf`.
This is an editorial continuation, not a new mathematical audit or promotion.

## Follow-up: feature-learning theorem placement

At the user's request, the unchanged `feature_learning_theorem.tex` input now
appears directly after the main compression theorem and before efficient
initialization. It is Theorem 1.2 on page 4; the main theorem is 1.1 on page 3,
and initialization is Proposition 1.3 on page 5. A subsection heading keeps
the initialization material separate. No theorem statement, proof, assumption
or mathematical conclusion changed. The separate NTH storage benchmark stays
in its existing proof section.

The build at
`data/generated/headline_threefold_upgrade_20261011/feature_theorem_move.RsouOA/`
passes and remains 89 pages. A scoped Terra check inspected pages 3–5 and
verified unchanged before/after hashes for all ten included TeX files. The
final log has no unresolved references/citations or overfull/underfull boxes;
the inherited `amsmath` compatibility warning remains. The coordinator
checked the actual auxiliary numbering, final log, and page count. The current
published `paper/compact.pdf` has SHA-256
`cab13b27428ab50d483a9777a05c16e58376c6de87c57f86b85fdc350d7b4ba2`.
`SHORTEN_check.py` now permits exactly this requested reorder and new heading
while continuing to require all mathematical text to match. This is a
statement-placement check, not another mathematical audit or book change.

## Current continuation: shorten the new paper proofs

The user requests a rollback commit first, then a substantial structural
shortening of only the newly added width/setup arguments, with no loss of
rigor, self-containment, quantitative strength or scope, followed by fresh
independent audits. The rollback commit is
`aa28e4693eecb93e6770db404878e959f5161fdf`. It includes this task's promoted
chapter, paper and research package, but not unrelated concurrent work.
The preceding compiled paper has 53 pages; the integrated rollback paper has
94. Page reduction is an outcome, not an assumption or a target obtained by
changing typography or moving necessary proofs outside the paper.

This is a continuation of the same proof integration. The maintained book is
read-only for this pass. The public paper theorem, initialization proposition,
all quantitative powers and qualifications, and older proof bodies are frozen
except for necessary reference/interface edits. Author candidates are separate
study-owned TeX files; the coordinator owns integration and this record.
Fresh reviewers receive frozen candidates and full necessary dependencies,
without author discussion or earlier verdicts. No empirical campaign is added.

The shortened candidate is frozen in
`data/generated/headline_threefold_upgrade_20261011/short_paper_v2/`.
It compiles to **89 pages**, versus 94 at rollback. The two proof modules
contain 9,970 whitespace-delimited words versus 12,840 (22.4% fewer).
These source-word and whole-PDF measurements are distinct; the paper has not
been made smaller through font, margin or spacing changes. Only the width
and initialization proof modules change. The main theorem, initialization
proposition, all older included scientific sources, bibliography, book
chapter and global notation are byte-identical to rollback.

The structural changes replace auxiliary map recurrences by a verified
power ledger, reuse the existing source/domain, signed-comparison,
innovation and panel-construction arguments, exploit forward/transpose
symmetry in the Gaussian sampler, and factor the eight finite cost bounds
through four completely explicit common sums. The finite probability,
numerical restart, exact pairing, adaptive Gaussian conditioning and full
parameter/primitive-cost calculations remain in the paper. The author
candidates and their exact reduction maps are
[width](SHORT_WIDTH_NOTES.md), [setup](SHORT_SETUP_NOTES.md), and the
[shared-opportunity analysis](SHORT_SHARED_OPPORTUNITIES.md); none is an
independent acceptance report.

The [paired-review assignment](SHORT_REVIEW_ASSIGNMENT.md) applies to the
immutable version-1 scientific candidate. A separate frozen
`short_preservation_evidence/baseline/` supplies all unchanged original paper
sources for byte comparison. Version 2 changes only two inline formulas
into displays, reorders one clause, and removes obsolete TeX comments;
the [fresh final-integration assignment](SHORT_INTEGRATION_ASSIGNMENT.md)
includes verifying that correspondence. Both fresh isolated mathematical
reviews, [A](SHORT_REVIEW_A_V1.md) and [B](SHORT_REVIEW_B_V1.md), are complete
and **PASS**, with no required correction. The separate fresh
[final integration review](SHORT_INTEGRATION_V2.md) is also complete and
**PASS**. The coordinator read all three full reports and checked their
source identities. These are scoped audits of the two rewritten proofs and
their complete necessary dependencies, not new audits of the whole book or
the unchanged feature-learning/NTH theorems. All seven formal statements
inside the rewritten modules match their originals.
Both [version-1](SHORT_BUILD_V1.md) and [version-2](SHORT_BUILD_V2.md) build
records are retained. Version 2 has no unresolved references/citations or
overfull/underfull boxes; one inherited nonfatal `amsmath` compatibility
warning remains. That pass published the reviewed 89-page PDF as `paper/compact.pdf`,
SHA-256 `e1befdf23ffb05b4165c17048082da945e54a02305bc1cdd1f6766d5775bc122`.
The later statement-only relocation and current PDF are recorded above.
The 94-page rollback PDF remains in the rollback commit and in
`paper_integration_v3/build/compact.pdf` under this study's generated folder.
`SHORTEN_check.py` reproduces the preservation and reference checks and can
freeze a fresh packet without changing Git. The shortening is left as
uncommitted changes after the requested rollback commit. Unrelated concurrent
edits are preserved.

## Approved promotion: width and efficient setup only

### Approved integration, 2026-10-11

The user explicitly approved the reviewed book package and requested the same
content in the current compact paper: polynomial width conditions in its main
theorem and an initialization proposition immediately below it, preserving all
other qualifications and claims. The maintained Chapter 9 contains the approved
version-6 candidate, with two prose-only clarifications that the quantitative
proofs explicitly recall the source-coefficient recurrences they reuse. No
mathematical content, other book chapter or notation contract is changed.
Its final SHA-256 is
`4b18d60c47f760e91d0077182b56c97484697753937c814d64264d52df2d03aa`.
The compact paper includes the complete transferred proofs; its main Theorem
1.1 incorporates the Legendre/Taylor polynomial widths, and Proposition 1.2
immediately below it gives the four initialization variants.

The [book build check](BOOK_INTEGRATION_CHECK.md) and
[final paper build](PAPER_BUILD_V3.md) passed. The source-preservation check
`PAPER_INTEGRATION_check.py` verifies the original model, small-label, norm,
storage and error equations, unchanged 30-symbol inventory and untouched
Legendre, fitting, feature-learning and NTH proof files. It also checks all
paper references and exact book correspondence to the approved text plus the
two locality clarifications. No Git commit or index mutation is part of this
integration request. See [the package](PROMOTION_PACKAGE.md) for final artifacts
and the independent integration verdict.

Final status: the fresh isolated
[version-3 integration review](FINAL_INTEGRATION_REVIEW_V3.md) is complete and
**PASS**, with no required or optional correction. The coordinator read the
entire report and verified its frozen source hashes against the maintained
files. It covers the new proofs and their necessary dependencies, both
interfaces, preservation, references and focused rendered pages; it is not a
new audit of unrelated book chapters or the unchanged NTH/feature-learning
proof complements. The earlier paper transfer review's locality objection
was corrected; the interrupted version-2 report remains PARTIAL, not an
acceptance verdict. The final compiled PDF is published as
`paper/compact.pdf`; the previous PDF is retained at
`data/generated/headline_threefold_upgrade_20261011/paper_integration_v3/prior_compact.pdf`.

Paper ownership: the coordinator edits `compact.tex`, necessary existing proof
interfaces and `paper/README.md`; `paper_width_transfer` owns the new
`paper/compact_width.tex`; `paper_setup_transfer` owns the new
`paper/compact_initialization.tex`. These are authors, not independent reviewers.
The longer legacy manuscript, feature-learning theorem/proofs and separate NTH
benchmark are not rewritten. No empirical campaign is included.

### Preparation record before approval (historical)

The following preparation restrictions and pending-approval statements record
the earlier stage. They are superseded by the explicit approval and integration
above; they are retained to preserve the review history.

2026-10-11. The user now requests a book-promotion package for exactly two
additions: polynomial sufficient width thresholds for the existing Legendre
and Taylor compression headlines, and four efficient initialization variants
(supplied explicit dense / fresh implicit Gaussian, for Harmonic and Taylor).
The complete-trajectory norm, activation class, small-label condition, query
domains, retained-state dependencies and corrected optimizers are unchanged.
The efficient algorithms use disposable numerical continuation across the
required finite horizon. They are not short-prefix-only or finite-bit results.
The implicit algorithms couple to a fresh ordinary Gaussian dense reference,
not an externally supplied matrix or prescribed entrywise random seed.

The endpoint and simultaneous same-time investigations below are excluded from
this promotion. No new nonaffinity or query-separation assumption is imported.
The positive width repair uses a weaker quantitative dense lower coefficient;
polynomial onset of the older sharper coefficient is not part of the package.
Harmonic's width qualification is unchanged.

Preparation, isolated reviews and a staged full-book rendering are authorized;
changing the maintained book or paper is not. The concrete reviewed book
addition will be returned for user approval, followed only later by paper
adaptation. All promotion artifacts remain flat in this study; generated
staging/render products belong to `data/generated/headline_threefold_upgrade_20261011/`.

The coordinator owns the package manifest, integration proposal and this README.
`compression_upgrade_selector` owns `PROMOTION_SELECTION.md` and independently
screens relevance and placement. The two scoped assemblers own respectively
`PROMOTION_WIDTH.qmd` / `PROMOTION_WIDTH_SOURCES.md` and
`PROMOTION_SETUP.qmd` / `PROMOTION_SETUP_SOURCES.md`. They are authors, not
independent promotion reviewers. New paired scientific reviewers and a separate
integration reviewer must be fresh contexts distinct from these contributors.
The permitted scientific inputs are the existing relevant width/setup packets
listed below, the three explicitly authorized raw quantitative dependencies,
and the established Quarto edition. No historical endpoint findings enter the
candidate. No experiment or Git mutation is planned.

Status: version 6 has passed the prescribed reviews and builds and is ready for
user approval, not yet integrated. The independent placement screen accepted
assembly in Chapter 9. Start with
[PROMOTION_PACKAGE.md](PROMOTION_PACKAGE.md). The complete width and setup
additions are in [PROMOTION_WIDTH.qmd](PROMOTION_WIDTH.qmd) and
[PROMOTION_SETUP.qmd](PROMOTION_SETUP.qmd); both include their full arguments.
The implicit-Taylor execution and its compatibility with polynomial width are
included, not left as sourced conditional inputs.

The staged edition is
`data/generated/headline_threefold_upgrade_20261011/promotion_v6/`; its complete
Chapter 9 SHA-256 is
`3b6ca32de3f4feef6771c15c7826edc4c38d70836e7d261fa06468582f4646f1`.
The scientific assignment is [PROMOTION_REVIEW_ASSIGNMENT_V5.md](PROMOTION_REVIEW_ASSIGNMENT_V5.md).
The final integration assignment is
[PROMOTION_INTEGRATION_ASSIGNMENT_V6.md](PROMOTION_INTEGRATION_ASSIGNMENT_V6.md).
Candidate inputs remain frozen. Both fresh complete
scientific reviews have passed: [review A](PROMOTION_REVIEW_A_V5.md) and
[review B](PROMOTION_REVIEW_B_V5.md). The coordinator read both full reports,
verified their hashes and distinct isolated identities, and confirmed full
scientific coverage.
The completed [version-5 integration review](PROMOTION_INTEGRATION_V5.md)
held acceptance for one layout-only defect: an inline mobility tuple overflowed
the PDF text margin. Version 6 changes only that tuple to display math. The
complete chapter is byte-identical after removing whitespace and dollar math
delimiters; all words, formulas, references and hypotheses are unchanged.
Under promotion gate 4 this presentation repair retains the completed
scientific reviews, but requires a fresh complete integration review and builds
of the corrected edition. Those version-6 checks are complete:
[independent integration ACCEPT](PROMOTION_INTEGRATION_V6.md) and
[HTML/PDF/editable-LaTeX build PASS](PROMOTION_BUILD_V6.md). The coordinator read
the full final reports and checked input/output hashes. All added PDF pages and
changed interfaces were visually inspected by the integration reviewer. One
minor text overhang is nonblocking; HTML was checked structurally, with browser
screenshot testing unavailable. User approval of the concrete final package is
still required before any live integration. No live book or paper file changed.

Version 1 was withdrawn after its build found eleven malformed internal
references and an unescaped closing math brace. Its two review reports are
retained as PARTIAL / NOT COMPLETE, not acceptance verdicts; neither had found
a scientific objection before withdrawal. Its build report records the failures.
Versions 2 and 3 are unused intermediate formatting snapshots. Version 4 fixes
the reference syntax and brace, without changing a mathematical claim or proof.
Its full HTML/PDF/LaTeX render succeeded, but visual inspection then found four
new section references rendered as empty “Section .” labels under the book's
unnumbered-section setting. Version 4 was also withdrawn before acceptance;
its incomplete review reports are retained. Version 5 changes those four
references to descriptive anchor links, without changing mathematical content.
The fresh complete scientific reviews used version 5, not interrupted reports.

## Original investigation record (not the promoted scope)

The original scope and subsequent investigation records below are historical.
Only the width and setup additions identified above are promoted; the endpoint
and simultaneous same-time investigations are not part of this integration.

User-requested joint study, 2026-10-11. This study assembles and checks three
proposed improvements before any paper edit: a simultaneous same-time relative
error bound through the fitted endpoint; quantitative width conditions without
exponential sample/gap dependence; and a computationally efficient rollout-based
initializer for the selected Harmonic and Taylor methods.

## Contract

The model, activations, data, loss, mobilities, compression methods, retained
counts and query domains are those of `paper/compact.tex` and its included
proofs. The proposed sole added activation assumption is layerwise nonaffinity.
All other data and geometry qualifications must be accounted for explicitly.
Width tends to infinity. The requested time comparison is the supremum over
positive physical times (including the fitted limit) of the ratio of the two
spatial supremum discrepancies at the same time. It is not a ratio of trajectory
suprema. At time zero all predictors vanish; its zero denominator must be treated
explicitly. Taylor's published scope allows any declared finite panel, including
no additional inputs. The user's continuation explicitly replaces the Taylor
comparison domain by a nonempty test-only panel, distinct from training
inputs. The construction still uses the training inputs as well. Results on
the original combined domain are not silently claimed on the smaller domain.

The three upgrades are separate proof obligations. Successful construction of
one does not establish the others. No numerical experiments or manuscript/book
edits are authorized by this study. The user permits numerical dense evolution
for the efficient initializer; initialization-only information provenance and
rollout-based computational complexity must be distinguished.

## Permitted scientific inputs

The user explicitly requests assembly of the earlier findings, so the inputs
are the current compact paper and its directly relevant older cost appendices,
the established Quarto book, and these directly relevant research packets:

- `studies/general_nonlinear_endpoint_lower_20261010/`: the Gaussian-oracle
  endpoint proof, its numerical and projected-Gaussian modules and checks.
- `studies/polynomial_width_compression_20261010/`: the width repairs and checks.
- `studies/integrated_general_compression_20261004/`: the local numerical setup
  construction, integration interfaces and their directly cited setup proofs.

These inputs are to be checked, not imported on the strength of earlier verdicts.
Unrelated studies, historical experiments and the frozen pre-Quarto archive are
outside scope.

## Work allocation and initial status

The coordinator owns this README, the joint result and same-time proof synthesis.
Scoped contributors own separate notes for width, setup, and the exact scope of
the time-uniform claim. All shared inputs are read-only.

Initial decisive questions: the endpoint theorem currently needs a proper
training span and an orthogonal query; the current headline does not. Taylor's
training-only panels have zero endpoint dense discrepancy. The near-zero
compression estimate and simultaneous dense lower bound also remain to be proved.
No threefold theorem upgrade is claimed at study start.

## Current deliverables and status

Start with `RESULT.md`. The exact full-scope requested theorem is not
established. Current additions and limitations are:

- `EARLY_ERROR_BOUNDS.md` and its check prove the initial-time upper factor
  for all three compression methods.
- `TIME_COMPARISON.md` and its check give the precise near-zero and
  geometrically qualified late windows, without claiming they meet. The
  nonparallel-query continuation below now extends the near-zero window to
  test-only domains.
- `QUERY_RATIO_SCOPE.md` and its check address the revised test-only domain:
  separated pointwise zeros persist at positive time, and a test-only panel
  of antipodes can have zero fitted discrepancy for an even architecture.
- `TEST_PANEL_DENSE_ROUTE.md` extends the actual endpoint bound to any fixed
  query outside the training span, not merely orthogonal queries. Its separate
  frozen-feature crossing result is not asserted for actual feature learning.
  `OFF_SPAN_ENDPOINT_CHECK.md` reconstructs the actual-network extension.
- `WIDTH_UPGRADE.md` and `WIDTH_DEPENDENCY_CHECK.md` now assemble the positive
  polynomial Legendre/Taylor repairs and their finite source probabilities.
- `HARMONIC_ONSET_ROUTE.md` and its fresh check give a fixed-dimension
  source-rank obstruction uniform over shrinking-label/gap families. Fixed
  positive labels and arbitrary output-only compression are not disproved.
- `SETUP_UPGRADE.md` and its bridge check supply the real-node Taylor
  initializer and Harmonic setup transfer, with complete order/cost accounting
  and an explicit exact-real arithmetic qualification.

The user has now authorized the three named raw quantitative dependencies
under `unseen_query_decoder_20261005`: `INSERTION_MAP_MODULI.md`,
`EXPLICIT_FITTING_WIDTH.md`, and `QUANTITATIVE_INSERTION_WIDTH.md`.
Only these three are additionally authorized; their linked files are not
automatically added to the input scope. They have now been read and checked.
No paper/book edit or commit is made. This packet is internally checked
research, not a promoted addition or a claim that all requested upgrades hold.

## Continuation: test-only comparisons

The user now restricts Taylor's comparison domain to a nonempty declared
test panel, distinct from training inputs, and asks to complete the upgrades.
This supersedes the training-only-panel objection for that revised target,
but not architectural identifications of distinct inputs. An earlier message
wrote the reciprocal ratio and placed the spatial supremum outside it.
The subsequent explicit display confirms compact/dense error divided by
dense/dense discrepancy, with separate spatial suprema followed by the
time supremum. The earlier ambiguity is resolved, not a remaining blocker.
The fitted endpoint remains in scope. Mere test/train distinctness is not
assumed to establish a nonzero denominator.

The bounded parallel tasks audited the three authorized width dependencies,
tested a fixed-dimension Harmonic onset repair, and examined the dense lower
bridge on genuinely nonparallel passive inputs. The coordinator owns query/ratio
scope and synthesis. New mathematical claims have recorded derivations and
checks, including a separate narrow check of the off-span endpoint extension.
No experiment or manuscript edit is added to the scope.

## Continuation: nonparallel queries and the pre-endpoint interval

The user asks to replace the off-training-span qualification by a fixed query
nonparallel to every training input, and to close the same-time comparison on
the remaining interval before `(2m/gamma) log(en)`. This continues the same
investigation. The working target is now explicitly the ratio of separate
spatial suprema, followed by the positive-time supremum. Time zero itself has
two zero predictors and is handled by a right limit, not literal division.
Training inputs and passive tests are taken pairwise nonparallel wherever
the proposed augmented-rank argument is used. For fixed finite inputs this
gives a positive projective separation, whose size may enter constants.

The current bounded proof-search round separates three obligations: nonlinear
initialized rank and a test-input initial-derivative lower bound; survival of
query innovation to the fitted nonlinear endpoint with full-span training;
and a simultaneous-time lower bound or an actual-network crossing obstruction.
No frozen-feature comparator is substituted for the fully trained model.
The coordinator owns synthesis and rank/conditioning interfaces; contributors
own separate new proof notes. Existing proof notes remain valid only at their
stated scopes until a new complete argument supersedes them. No experiment,
paper edit, promotion, or commit is added to this request.

The completed positive continuation is `NONPARALLEL_INITIAL_VARIABILITY.md`:
strictly positive augmented feature Grams at every initialized hidden layer,
an initial-velocity lower bound at a fixed nonparallel test, and a simultaneous
near-zero interval on that same test. `NONPARALLEL_INITIAL_CHECK.md`
reconstructs these claims and their exact probability constants. Nonparallel
directions suffice; no input-span exclusion is needed for these conclusions.

`NONPARALLEL_ENDPOINT_ROUTE.md` isolates the remaining endpoint issue as
second-layer innovation after the training-source transcript is revealed.
It gives a conditional restart, not an unconditional removal of the off-span
qualification. Initial rank alone concerns a smaller conditioning space.

`ACTUAL_TIME_BRIDGE.md` supplies a new actual-network crossing theorem
for a nonparallel single-test panel with full-span training, rather than
substituting frozen features for learned ones. `ACTUAL_TIME_BRIDGE_CHECK.md`
is its fresh isolated reconstruction, with a positive verdict for the stated
crossing theorem. Its conclusion concerns the requested same-time denominator,
not the paper's existing complete-trajectory denominator. Under the current
zero-denominator failure convention it prevents the universal Taylor upgrade
on arbitrary nonempty test panels. It does not disprove the sphere-norm or
endpoint statements.

`ACTUAL_CROSSING_QUOTIENT.md` additionally proves fixed-time atomlessness
for this actual network and a conditional quotient-divergence statement for
any nonexact analytic compressed predictor independent of the second run.
The selected Taylor construction's analyticity and nonexactness have not
been established by this note and are not silently assumed.

## Continuation: remove the endpoint span restriction

The current request targets only the remaining endpoint dense lower bound:
replace a nonzero component outside the training span by a fixed test's
positive separation from the training directions and their antipodes, retaining
the original activation class, nonaffinity, fixed depth, positive feature gap,
fixed nonzero labels and the original sufficient label cap. Separation only
from the training points cannot exclude antipodal architecture identities;
this distinction was stated to the user before the new proof search.

The target is the actual fitted prediction, with a fixed positive confidence
coefficient multiplying `n^(-1/2)`, not initialized rank, a frozen-feature
endpoint, finite-time atomlessness, or a width-dependent label limit. A fixed
separated test would imply the desired supremum result; a proof only for a
supremum must be labeled accordingly. No paper edit, experiment or commit is
authorized here.

This bounded round uses two independent scoped attempts: endpoint conditional
innovation/cavity (`ENDPOINT_SEPARATION_CAVITY.md`) and endpoint structural
identification or tangent mechanisms (`ENDPOINT_SEPARATION_STRUCTURE.md`).
They do not read one another's active notes. The coordinator examines the
exact endpoint identity, the initialization-kernel comparison, and alternate
conditioning/perturbation mechanisms. New restrictions on labels or query
geometry would be partial results, not completion of the contract. The old
conditional restart is not counted as new progress merely by restating it.

The saved first-round separation attempts remain partial: the cavity note
derives the compensated trained-neuron endpoint response, and the structural
note derives the admissible endpoint pullback and a Gaussian small-ball
criterion. Neither verifies noncancellation at the original fixed label cap.
The current continuation tests two more specific estimates in
`ENDPOINT_TRANSVERSE_ROUTE.md` (relative transverse metric) and
`ENDPOINT_PROBE_NONCANCELLATION.md` (compensated probe noncancellation).
They have disjoint write ownership and do not read one another's active work.
The coordinator checks endpoint interpolation identities and the distinction
between surviving conditional randomness and fluctuations already revealed
by the training transcript. The target, proof scope and forbidden substitutions
are unchanged.

The continuation's endpoint outcome is summarized in
`ENDPOINT_SEPARATION_RESULT.md`. The transverse route obtains an exact
fitted-residual identity, a cubic readout-leakage bound and a local cubic
coefficient. The probe route obtains infinite-rank compensated endpoint
covariance on every open sphere patch, under the original cap, at each
successful finite-width cavity. Neither supplies the width-uniform
fluctuation and collective-transfer estimates needed for the requested
actual-network `n^(-1/2)` bound. The new route checks are
`ENDPOINT_TRANSVERSE_CHECK.md` and `ENDPOINT_PROBE_NONCANCELLATION_CHECK.md`.
No off-span qualification has been removed from a stated dense endpoint
theorem, and no manuscript or book changes were made.

## Continuation: the circle supremum itself

The user now asks to concentrate on dimension two and the supremum over
the circle, rather than every prescribed separated test point. This is the
same endpoint investigation at a narrower input geometry and a weaker
observable target. There are finitely many fixed training directions; they
may span the whole input plane. The original activation class, nonaffinity,
fixed depth and exact label cap remain unchanged. The desired constant in
the fitted dense-copy lower bound `c_delta/sqrt(n)` may depend on every
fixed problem parameter and confidence, but not on width. A proof on a
nonempty separated open arc is sufficient. Finite-width nonconstancy,
initial rank and frozen-feature comparisons alone do not resolve it.

The bounded first round assigns spatial Fourier/score ideas to
`CIRCLE_FOURIER_ROUTE.md`, exact flow transport to
`CIRCLE_TRANSPORT_ROUTE.md`, and a fresh canonical counterexample or
endpoint-identification search to `CIRCLE_ADVERSARIAL_ROUTE.md`.
The attempts have separate write ownership and no access to one another's
active work. The coordinator examines the actual endpoint and the
distinction between infinite spatial rank and width-uniform fluctuation
scale. No experiment, paper edit, promotion or Git write is authorized.

The circle round is summarized in `CIRCLE_ENDPOINT_RESULT.md`. It adds
dimension-free probe transport, a width-independent lower bound on the
trained probe's uncentered readout second moment, and actual finite-width
endpoint nonconstancy outside countably many possible label scales.
`CIRCLE_ROUTE_CHECK.md` and `CIRCLE_PROBE_READOUT_CHECK.md` reconstruct
the stated partial claims. A second tangent-mode route is recorded in
`CIRCLE_TANGENT_ROUTE.md`; its obstruction is to a proposed operator
shortcut, not to canonical-network endpoint variability. The desired
actual dense-copy `c_delta/sqrt(n)` circle endpoint bound remains open.
No counterexample to it was found, and no headline theorem was upgraded.
