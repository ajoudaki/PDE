# Chapter 9 upgrade package

## Status

**Approved by the user and integrated into Chapter 9 and the current compact
paper.** The independent relevance screen, both complete scientific reviews
and the version-6 independent integration review passed before approval.
The final live book has also passed HTML, PDF and editable-LaTeX builds, and
the compact paper compiles successfully. The paper's main Theorem 1.1 now
contains the quantitative Legendre/Taylor width conditions; Proposition 1.2
immediately below it states all four initialization variants. Complete proofs
are included in both editions, without a research-note dependency.

The final book differs from approved version 6 only in two prose clarifications
of which source-coefficient recurrences the quantitative proofs explicitly
recall. Its mathematical content is unchanged. The final independent
paper/book integration check is recorded below. No commit was requested or
made; unrelated concurrent changes and the shared Git index are untouched.

## Integrated scientific additions

1. Polynomial sufficient widths for the existing Legendre and Taylor
   compression headlines, with the same retained-state formulas and comparison
   to actual dense-run discrepancy in the complete-trajectory norm.
2. Efficient initialization for both selected constructions, each under two
   different reference-input contracts.

At separately fixed admissible data, activation, depth and confidence, the
exact-real setup costs are:

| Method | Reference supplied to setup | Work | Peak setup memory |
|:--|:--|:--|:--|
| Harmonic | Actual dense matrices | `O(n²[log(en)]^(3d/2+1))` | `O(n²)` |
| Taylor | Actual dense matrices | `O(n²[log(en)]^(5/2))` | `O(n²)` |
| Harmonic | Fresh Gaussian reference sampled implicitly | `O(n[log(en)]^(9d/2+3))` | `O(n[log(en)]^(3d/2+1))` |
| Taylor | Fresh Gaussian reference sampled implicitly | `O(n[log(en)]^5)` | `O(n[log(en)]^(5/2))` |

“Linear” and “quadratic” here mean a linear or quadratic power of width times
the displayed logarithmic factors. Computational constants in this table may
depend on all separately fixed problem parameters; both editions also give
the full finite-order ledgers instead of hiding those dependencies there.

The near-linear initializer couples to a fresh ordinary Gaussian dense model.
It does not compress access to an arbitrary externally supplied dense matrix or
a prescribed entrywise seed. The numerical algorithms cover the complete finite
approximation horizon `32(m/γ)log(en)`, then discard their dense or implicit
working structures. They are not short-physical-prefix algorithms. The final
compressed model starts at time zero and retains the existing autonomous
nonlinear optimizer, storage bounds, `Y/n` approximation guarantee and original
query domain. Taylor's passive inputs are declared before setup, without labels;
Harmonic retains whole-sphere queries.

The exact-real operation model charges scalar arithmetic, comparisons, square
roots, elementary functions, original activation values and Gaussian draws.
Nonprimitive evaluator work, scratch and description are additional. It does
not assert finite-bit complexity, numerical conditioning or practical speedup.
Certified activation envelopes and the population Gram-gap lower bound are
inputs; computing these mathematical certificates is not charged as setup work.
The initialized-jet compiler remains a separate provenance alternative without
the new efficient setup bound.

## Preserved scope and exclusions

The activation class still permits unbounded activation values. The existing
small-label condition, Gaussian initialization, loss, mobilities, fixed-depth
setting, model definitions, query domains and retained-state parameter powers
are unchanged. The relative error compares two complete-trajectory norms; it
is not a same-time ratio at every time and not an endpoint dense lower bound.

The polynomial-width addition concerns Legendre and Taylor only. Harmonic's
width threshold and the separate nonlinear-feature-learning certificates are
not strengthened by it. Polynomial dependence is quantified in `β^L`, not in
depth `L` separately. The dense lower coefficient used for this quantitative
upgrade is weaker than the older sharp coefficient; polynomial onset of that
older coefficient is not claimed.

## Integrated editions and validation

- [Maintained Chapter 9](../../docs/08b-trajectory-compression.qmd).
- [Current compact-paper source](../../paper/compact.tex), with self-contained
  [width proofs](../../paper/compact_width.tex) and
  [initialization proofs](../../paper/compact_initialization.tex).
- [Updated compact-paper PDF](../../paper/compact.pdf).
- [Final book PDF](../../data/generated/headline_threefold_upgrade_20261011/book_live_integration_v2/live_source_snapshot/data/generated/DTDL/DTDL.pdf).
- [Final rendered Chapter 9](../../data/generated/headline_threefold_upgrade_20261011/book_live_integration_v2/live_source_snapshot/data/generated/DTDL/08b-trajectory-compression.html).
- [Final editable book LaTeX](../../data/generated/headline_threefold_upgrade_20261011/book_live_integration_v2/live_source_snapshot/data/generated/DTDL/book-latex/DTDL.tex).
- [Book integration/build check](BOOK_INTEGRATION_CHECK.md).
- [Final paper build check](PAPER_BUILD_V3.md).
- [Fresh final paper/book integration review: PASS](FINAL_INTEGRATION_REVIEW_V3.md).
- [Source-preservation checker](PAPER_INTEGRATION_check.py).

The live chapter has SHA-256
`4b18d60c47f760e91d0077182b56c97484697753937c814d64264d52df2d03aa`.
The final compiled compact paper has SHA-256
`9c805f6cd89280b7ce92435e3c3a66ecda2e578c03b69c73b98ee60ac7ae13f9`.
The final paper snapshot and preservation results are in
`data/generated/headline_threefold_upgrade_20261011/paper_integration_v3/`.
The complete book was rendered from a byte-matched documentation snapshot
because the checkout's inherited Quarto project-cache database was read-only;
the maintained sources and cache permissions were not altered to bypass it.

The preservation check authenticates the original model, data, label, norm,
relative-error and three storage displays against the pre-integration source.
The global notation inventory and the fitting, Legendre, nonlinear-feature-
learning and NTH proof files remain unchanged. Neither the older longer
manuscript nor historical experiments are rewritten.

The coordinator read the complete final review and verified all candidate
hashes against the maintained files. It completed the new width/setup proof
audit and required dependencies, both interfaces, preservation and references,
plus focused visual checks of the paper and Chapter 9. No required or optional
correction remains. It is not a whole-book audit or a reproof of the unchanged
feature-learning/NTH complements. The initial paper transfer review's stale
locality sentence was corrected in both formats; the interrupted version-2
report is PARTIAL and is not used as acceptance evidence. The fresh complete
version-3 review is the final integration verdict.

The preceding compiled paper is recoverable from
`data/generated/headline_threefold_upgrade_20261011/paper_integration_v3/prior_compact.pdf`;
the published `paper/compact.pdf` matches the final validated build exactly.

## Approved candidate and pre-approval review history

- [Complete proposed Chapter 9](../../data/generated/headline_threefold_upgrade_20261011/promotion_v6/docs/08b-trajectory-compression.qmd).
- [Rendered chapter](../../data/generated/headline_threefold_upgrade_20261011/promotion_v6/data/generated/DTDL/08b-trajectory-compression.html).
- [Full proposed book PDF](../../data/generated/headline_threefold_upgrade_20261011/promotion_v6/data/generated/DTDL/DTDL.pdf).
- [Editable LaTeX edition](../../data/generated/headline_threefold_upgrade_20261011/promotion_v6/data/generated/DTDL/book-latex/DTDL.tex).
- [Width addition](PROMOTION_WIDTH.qmd).
- [Four-initializer addition and proofs](PROMOTION_SETUP.qmd).
- [Independent placement review](PROMOTION_SELECTION.md).
- [Neutral scientific-review assignment](PROMOTION_REVIEW_ASSIGNMENT_V5.md).
- [Mechanical staging script](assemble_promotion.py).

The staging script copies only the Quarto documentation and its linked code
resources into a fresh study-owned generated directory. It checks exact
integration anchors, produces the complete proposed Chapter 9, a diff, input
hashes and structural-reference checks. It does not modify the maintained book
or create a parallel checkout.

```bash
python -B studies/headline_threefold_upgrade_20261011/assemble_promotion.py \
  data/generated/headline_threefold_upgrade_20261011/promotion_v6
```

The two fresh complete scientific reviews passed without required corrections:
[review A](PROMOTION_REVIEW_A_V5.md) and [review B](PROMOTION_REVIEW_B_V5.md).
The coordinator read both reports completely and verified frozen-input identity
and independence.
The [version-5 integration review](PROMOTION_INTEGRATION_V5.md) found one
layout-only defect and no scientific/interface objection. Version 6 places the
overlong mobility tuple in display math; it preserves every word, formula and
reference. The chapter is identical after removing whitespace and math-dollar
delimiters. The scientific reviews therefore carry over under promotion gate 4;
the [fresh complete integration review](PROMOTION_INTEGRATION_V6.md) of version 6
has now accepted the addition. The coordinator read its full report and verified
the candidate and rendered-artifact hashes. The reviewer visually checked all
added PDF pages and changed interfaces; one minor typography observation is
explicitly nonblocking. HTML was checked structurally, not through a successful
browser screenshot. [Final build validation](PROMOTION_BUILD_V6.md) passed HTML,
PDF and editable LaTeX with unchanged source hashes and clean reference checks.
Any scientific correction would reopen both scientific reviews. These reviews
do not authorize live integration without approval of this concrete package.

The current frozen Chapter 9 has SHA-256
`3b6ca32de3f4feef6771c15c7826edc4c38d70836e7d261fa06468582f4646f1`.
The script requires a fresh destination; the displayed command records how the
existing version was assembled, not an instruction to overwrite it. Earlier
formatting snapshots and interrupted reviews are retained but are not promotion
approvals. No mathematical claim changed between those snapshots and version 6.

The preceding record describes the package as reviewed before approval. The
user subsequently approved book integration and explicitly requested the same
content in the compact paper. That adaptation is now included above, without
importing the excluded endpoint investigations.
