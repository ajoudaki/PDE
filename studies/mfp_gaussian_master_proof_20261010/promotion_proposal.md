# Proposed MFP theory and compiler addition

Status: **approved and integrated**. The user approved this exact package on
2026-10-10 with "great, yes I approve". All 15 approved maintained files are
installed; all 116 live source/dependency files match the reviewed edition.
Scientific reviews, integration review and final live checks pass. The
[approval record](promotion_approval_v7.json) and
[live code check](promotion_live_code_check.md) retain the completed gate.

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

The final v7 MFP mathematical content, implementation and proof dependencies
are the same reviewed material. [Exact correspondence](promotion_scientific_input_correspondence_v7.json)
records 17 byte-identical packet files and 17 unchanged required edition reads.
The full current bibliography is preserved with the identical reviewed MFP
citation appended. [Layout equivalence](promotion_layout_equivalence_v6.json)
verifies that thirteen display-only reflows preserve all ordered mathematical
tokens, punctuation and labels; reversing them exactly restores the reviewed
theory and Chapter 2. No MFP scientific verdict is transferred to the concurrent
observable-closure or trajectory-compression results.

The retained v4 standalone code validation passes all 72 tests, imports,
library boundaries, every guide snippet and all example producers. All 92
code and requirements inputs in v7 are byte-identical to that executed
edition. The fresh integration reviewer independently ran the same code and
recipes in v6, then verified exact correspondence before carrying those
unchanged-input checks into the final v7 report. The final HTML build passes 7,515 local
link/fragment checks across 18 pages. Actual MathJax typesetting checks all 44
new displays at 1500×1100 and 1280×1100: zero errors and zero article-boundary
overflows. The complete 1,762-page PDF and editable-LaTeX builds pass.
Structural validation confirms all 116 frozen source files and 18 packet files
are unchanged, all 466 older Chapter 2 anchors remain, and all 50 new anchors
resolve. The PDF syntax check and formal-environment/reference checks pass.

The earlier [v3 integration report](promotion_integration_review_v3.md) passed
its edition. A subsequent concurrent book addition required a refreshed
whole-edition review; the [v4 report](promotion_integration_review_v4.md)
identified overwide HTML equations. That adverse report remains retained.
The corrected candidate received a [fresh complete neutral integration assignment](promotion_integration_assignment_v6.md).
Its [v6 report](promotion_integration_review_v6.md) found no required correction
and withheld the final verdict pending the concurrent current-book refresh.
The completed review includes the full [v7 context and assignment](promotion_integration_assignment_v7.md),
with explicit byte-correspondence rules for carrying its own unchanged-input
checks. The [final v7 integration report](promotion_integration_review_v7.md)
returns **PASS**, with no required correction or missing validation. The
coordinator read the complete report and verified every listed source/output
fingerprint. It independently checks the full added material and assigned old
context, every new PDF section page, all 44 HTML displays at both widths,
5,333 resolved unique LaTeX labels, and all 114 packaged source files in each
format. The assigned older read scope and unread complement are explicit;
this is not a new whole-book proof audit.

Frozen final inputs and validation outputs are in
`data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v7/`.
The [book preview](../../data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v7/mfp_book_preview.pdf)
is an exact extract of pages 117–137 of the complete candidate, including
adjoining context. The [source patch](../../data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v7/reviewed_changes.patch)
contains exactly the 15 declared changes and passes a dry run against the
retained current baseline. The complete maintained
[API guide candidate](../../data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v7/edition/code/MFP_CALCULUS.md)
is included in that patch. Preview and patch have source/hash manifests.
All earlier frozen candidates and original reports remain retained.

The final source-manifest SHA-256 is
`9e70dacf8d37890e03697d0678a29114c53cc498ee167e9b9ae8501968b204ab`;
the exact 15-file changed-manifest SHA-256 is
`818448d710ec30218386805442e113415965f09764f080503f1de7e652549a48`;
the patch SHA-256 is
`f8c05aaa9fcada19262f4e6306abe392a3a824874d525184e4401ea62c411a4d`.

## Completed integration

The user approved the exact package above. The root rechecked the shared
checkout and all dependencies, applied exactly the approved 15 files, and
verified every one of the 116 live source/dependency files against v7. The
[final preapproval check](../../data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v7/preapproval_check.json)
remains retained as the record before the user's approval.

The [live check](promotion_live_code_check.md) confirms all 72 tests, library
boundaries, five actual guide examples and three freshly generated kernel
variants pass. Its initial empty guide-check run is explicitly retained as an
invalid harness run; the corrected guarded execution runs all five examples.
All six formula outputs are byte-identical to the reviewed results. Book
placement, notation, formal environments and cross-references retain their
reviewed source bytes. Full-book render validation carries by exact identity
of every input; no redundant rebuild is substituted for correspondence.

The [live integration evidence](../../data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/)
contains final hashes, commands and the actual scoped commit record. The
repository's shared Git-writer lock protects the short stage/verify/commit
transaction. Unrelated changes are excluded. No scientific addition or
limitation changed after approval.
