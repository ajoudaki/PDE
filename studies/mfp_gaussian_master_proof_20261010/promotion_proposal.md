# Proposed MFP theory and compiler addition

Status: the MFP addition passed selection and both fresh scientific reviews.
Candidate v4 was blocked by the independent integration review for overwide
HTML equations. The corrected v6 candidate has thirteen display-only reflows,
with unchanged mathematical content, code and dependencies. Its HTML build
passes; remaining format checks and fresh complete integration review are in
progress. This task has made no maintained-source changes.

## Placement and value

Extend Part I, existing Chapter 2, `docs/02-gaussian-reuse.qmd`, immediately
after the exact polynomial Gaussian-expectation rules and before the existing
reusable finite calculus and forest factorization. Keep the part/chapter list,
all older contents and anchors, and the broader lower-regularity foundation.
The new section connects the conditioning rules to an explicit derivative
language, complete proof, operational calculation rules, neural examples and
an executable symbolic interface. It does not create a new chapter or part.

The proof credits existing Tensor Programs moment machinery and supplies the
needed Gaussian argument; it does not claim a new probabilistic master theorem.
The added practical contribution is a specified derivative calculus and its
typed symbolic implementation, with inspectable Gaussian expectation graphs.

## Exact scope

The theorem fixes program length, depth, data dimensions, derivative order and
update count before width tends to infinity. It admits the declared typed
Gaussian matrix/transpose programs, smooth polynomial-growth activation
derivatives, normalized averages, causal scalar feedback, represented rank
updates, ambient gradients and finite moving-flow jets. Scalar outputs converge
in every finite Lp. The stronger activation-moment reduction is restricted to
nonlinearities applied to the original centered forward preactivations.

Derivative compilation is an exact finite-width algebraic transformation.
Gaussian evaluation then returns its infinite-width limit. No finite-width
expectation formula, positive-time reconstruction, Taylor convergence,
growing-depth/order guarantee, unrestricted tensor contractions or efficiency
bound is added.

The code accepts concrete numeric positive-semidefinite root covariances,
including singular ones. Symbolic input geometry is represented by explicit
shared first-layer factors, and fixed labels by symbolic scalar parameters.
There is no direct symbolic covariance-matrix parser or numerical quadrature.
The examples distinguish the final hidden-feature/readout-block kernel from
the full tangent kernel, and explicitly state their readout law, half-mean
loss and training metric.

## Maintained destinations

The exact 15-file mapping is the frozen candidate's `changed_manifest.json`:

- `docs/02-gaussian-reuse.qmd`: the complete section and three scoped interface
  replacements. The proof, rulebook, matrix-reuse, update, singular-source,
  moving-flow, MLP derivative and symbolic kernel-jet examples are included.
- `docs/references.bib`: the primary attribution entry.
- `docs/_quarto.yml`: the definition-counter convention in PDF and editable
  LaTeX, matching the existing formal-environment convention.
- `code/pde/mfp_compiler.py`, `mfp_expr.py`, `mfp_finite.py`: typed program/AD,
  symbolic Gaussian expressions and the independent finite-array interpreter.
- `code/MFP_CALCULUS.md` and `code/README.md`: complete API conventions,
  executable recipes, supported operations and limits.
- Three `code/scripts/example_mfp_*.py` producers and four
  `code/tests/test_mfp_*.py` modules: complete reproducible examples and
  deterministic independent checks.

All proposed maintained material runs without the study, conversation or
retained research outputs. Ordinary package import retains the existing NumPy
dependency; the new symbolic implementation itself uses the standard library.

## Review and validation record

The independent selector accepted this placement and bounded scope. The first
frozen candidate remains retained with its original reports: one review found
a fixed-seed substitution defect, while the other passed. Candidate v3 fixes
that defect and adds multistep vector/matrix, seed lifecycle, jet and source
response regressions. It also repairs section links, definition numbering and
the new rule layout. No earlier verdict is reused to approve the changed bytes.

Both fresh complete scientific reviews pass: [review one](promotion_review_one_v3.md)
and [review two](promotion_review_two_v3.md). The root read both full reports
and verified their inputs. Both reconstructed the complete proof and code,
executed the supplied tests and recipes, and added independent exact Gaussian
and finite-width algebraic checks.

The final v6 mathematical content, implementation and proof dependencies are
the same reviewed material. [Exact correspondence](promotion_scientific_input_correspondence_v6.json)
records the byte-identical code and dependencies. [Layout equivalence](promotion_layout_equivalence_v6.json)
verifies that thirteen display-only reflows preserve all ordered mathematical
tokens, punctuation and labels; reversing those changes exactly restores the
reviewed theory and Chapter 2. No scientific verdict is transferred to the
concurrent addition in the trajectory-compression chapter.

The v4 standalone code validation passes all 72 tests, imports, library
boundaries, every guide snippet and all example producers. All 92 code and
requirements files in v6 are byte-identical to that executed edition. A fresh
integration reviewer independently executes the current v6 code and recipes.
The final HTML build passes 7,490 local link/fragment checks across 18 pages
with no duplicate IDs. Actual MathJax typesetting checks all 44 new displays
at 1500×1100 and 1280×1100: zero errors and zero article-boundary overflows.
The complete 1,752-page PDF build passes. Editable LaTeX and final structural
validation are pending.

The earlier [v3 integration report](promotion_integration_review_v3.md) passed
its edition. A subsequent concurrent book addition required a refreshed
whole-edition review; the [v4 report](promotion_integration_review_v4.md)
identified overwide HTML equations. That adverse report remains retained.
The corrected candidate has a [fresh complete neutral integration assignment](promotion_integration_assignment_v6.md),
including the complete new compression section as placement/duplication
context. Its independent report is pending. The assigned older read scope
and unread complement are explicit; this is not a new whole-book proof audit.

Frozen final inputs and available validation outputs:
`data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v6/`.
The run's `mfp_book_preview.pdf` is an exact extract of pages 117–137 from
the complete rendered PDF, including adjoining context. Its
`reviewed_changes.patch` contains all 15 proposed source changes and passes
a dry run against the retained current baseline. The complete maintained API
guide candidate is `edition/code/MFP_CALCULUS.md`. Preview and patch have
source/hash manifests. All earlier frozen candidates and original reports
remain retained.

The final source-manifest SHA-256 is
`188c0cc7cf9de7fe29ac8f4786f33448a89e73d11d828b79379088b7136b7c04`;
the exact 15-file changed-manifest SHA-256 is
`9577ec8be09f5dffe4cc5772a2ad3d6d1a87fecaf6d9d572d8ad20e902b48854`;
the patch SHA-256 is
`8f919e8f3a5db9ad5c89eca958b952de7cf85df0ad8e69759c242379094eb7c6`.

## Recommendation and remaining action

The MFP source addition is recommended for integration at the destinations above.
The final approval request awaits completion of format validation and the
fresh complete independent integration review.
On approval,
recheck the shared checkout and dependencies, apply the reviewed source bytes,
verify live correspondence and affected integration checks, and record the
scoped commit using the repository's shared Git-writer lock. Any substantive
change to the reviewed package reopens the applicable gates.

Part 2, step 5 of `RESEARCH_WORKFLOW.md` requires approval of the concrete
reviewed package before established book/code is changed. That approval is
required before live integration; the refreshed edition review is being completed first.
