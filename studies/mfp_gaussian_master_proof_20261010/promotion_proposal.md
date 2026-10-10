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

The corrected standalone edition has passed all 72 tests, imports, library
boundary checks, all guide snippets and all example producers. The full HTML
build passes 7,490 local link/fragment checks across 18 pages with no duplicate
IDs. Complete PDF and editable-LaTeX builds also pass. Structural checks retain
all 466 older Chapter 2 anchors and resolve all 50 new anchors, verify the
formal environments, and confirm the frozen 116-file source edition and
18-file dependency packet remain unchanged. The root inspected the new PDF
definition, theorem and adjoint rules. Both fresh complete scientific reviews
pass: [review one](promotion_review_one_v3.md) and
[review two](promotion_review_two_v3.md). The root read both full reports and
verified their input identities. They independently reconstructed the full
proof and implementation, ran all supplied tests/recipes and added separate
exact Gaussian and finite-width algebraic attacks.

The [v3 integration review](promotion_integration_review_v3.md) accepted its
assembled edition. At the final concurrency check, an independently committed
addition to the maintained trajectory-compression chapter required refreshing
the whole-edition context. [Exact input correspondence](promotion_scientific_input_correspondence_v4.json)
confirms that all 18 scientific packet files, all 18 required edition reads
and all 15 proposed file changes remain identical. The scientific verdicts
stay attached to those unchanged inputs; they do not extend to the other
chapter. A fresh integration review includes that chapter's complete new
section as placement, duplication and normalization context. Its final
report is pending; no whole-book proof audit is claimed.

Frozen inputs and validation outputs:
`data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v4/`.
The run's `mfp_book_preview.pdf` is an exact extract of pages 117–136 from
the fully rendered PDF, including the adjoining book context. Its
`reviewed_changes.patch` contains every proposed source change, and
`edition/code/MFP_CALCULUS.md` is the complete maintained API guide candidate.
Both preview and patch have source/hash manifests in that run.
Exact neutral review scopes are retained in `promotion_review_assignment_v3.md`
and `promotion_integration_assignment_v4.md`. The complete reports and original
adverse v1 evidence remain retained. The reviewed source-manifest SHA-256 is
`30a4f627f2937664ce2e66fbb620d09331a285c713f561e0075fe3cf15e0cdca`;
the exact 15-file changed-manifest SHA-256 is
`ff6d10776f3add6a276f39be80e23a3517cf2b6d007a20c1eb40fa62299a69d8`.

## Recommendation and remaining action

The MFP source addition is recommended for integration at the destinations above.
The final approval request awaits correction of the overwide HTML displays,
revalidation and a fresh complete independent integration review.
On approval,
recheck the shared checkout and dependencies, apply the reviewed source bytes,
verify live correspondence and affected integration checks, and record the
scoped commit using the repository's shared Git-writer lock. Any substantive
change to the reviewed package reopens the applicable gates.

Part 2, step 5 of `RESEARCH_WORKFLOW.md` requires approval of the concrete
reviewed package before established book/code is changed. That approval is
required before live integration; the refreshed edition review is being completed first.
