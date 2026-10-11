# Polynomial qualifying widths for the current three compressions

## Contract and status

Started 2026-10-10 at repository HEAD `ef8362764b4eb8144d7af8d6f8db080fdaaf82ca`.
The user authorizes new proof work, inspired by the directly relevant older
proofs, and final rigorous adversarial checks. **Do not edit the paper or book.**

Target: remove super-polynomial qualifying-width dependence for the current
Legendre, Harmonic and Taylor methods in `paper/compact.tex`, without changing
their architecture, optimizer, activation class, Gaussian initialization,
small-label hypothesis, test domains or complete-trajectory error contract.
In particular, retain unbounded activation values, arbitrary fixed depth,
correlated sphere inputs, and a positive initial feature-Gram gap. Preserve
the headline storage powers and expose rather than hide sample, dimension,
gap, depth, activation and confidence dependence. Separate the width needed
for a probability event, for an approximation estimate, for a simplified
storage display, and for a requested relative-error tolerance.

The requested joint strengthening meets a proved, construction-specific
Harmonic obstruction; see [RESULT.md](RESULT.md) and the exact scope below.
Earlier finite-training-source repairs do not imply a polynomial threshold
for the current whole-sphere source compression and its unchanged storage
display. An exponential transferred to storage or constants, a weaker
dense-upper-bound benchmark, or a smaller activation/data class is not a
resolution.

## Authorized inputs

- Current compact paper and its proof modules, with corresponding longer
  paper passages only to resolve source provenance.
- The established Quarto book, especially its notation contract.
- Directly relevant proofs and corrections in
  `unseen_query_decoder_20261005`, `integrated_general_compression_20261004`,
  `closure_sampling_20261003`, `finite_panel_absolute_compression_20261005`,
  `initialization_panel_compression_20261008`,
  `adaptive_clock_compression_20261008`, and
  `response_compression_framework_20261008`, as authorized in the conversation.

## Work assignments

- Coordinator: common source-dependency reconstruction, assembly, and checks;
  owns this README and final synthesis.
- Dense/Legendre route: quantitative initial fluctuation and lower-bound
  bridge; polynomial source transfer and all-order closure thresholds.
- Harmonic route: quantitative whole-query analytic source and exact spatial
  counts, including whether simplification gates are avoidable.
- Taylor route: finite passive-panel source and flaring analytic domain,
  preserving the logarithmic-cubed retained-state conclusion.

Route files are candidate research until reconstructed and independently
checked. Final reviews will use frozen inputs and fresh reviewer contexts.
No experiments, commits, or shared-document changes have been made by this study.

## Current evidence and review status

- [HARMONIC_ROUTE.md](HARMONIC_ROUTE.md): elementary finite-probability
  source-rank lower bound. It rules out every polynomial qualifying-width
  threshold in dimension for the present source approximation, exact-metric
  selection, and literal selected-array inventory with the unchanged headline.
  It does **not** rule out all output-only compression algorithms or contradict
  the current fixed-problem eventual theorem.
- [HARMONIC_REVIEW_A.md](HARMONIC_REVIEW_A.md) and
  [HARMONIC_REVIEW_B.md](HARMONIC_REVIEW_B.md): two fresh independent
  reconstructions accepted that exact scope.
- [HARMONIC_TOLERANCE_COROLLARY.md](HARMONIC_TOLERANCE_COROLLARY.md)
  extends the obstruction to every vanishing source tolerance, not just
  the current accuracy target. A separate fresh check in
  [HARMONIC_TOLERANCE_REVIEW.md](HARMONIC_TOLERANCE_REVIEW.md) accepted
  the extension. Its two suggested wording clarifications were applied.
- [FINITE_ANTI_CONCENTRATION.md](FINITE_ANTI_CONCENTRATION.md): a
  self-contained finite scalar lemma replacing the qualitative CLT. The first
  review accepted the proof and requested explicit conditional-iid wording;
  that clarification is now applied. The second review accepted the revised
  proof and supplied explicit conditional centering in the application;
  that wording clarification was also applied.
- [DENSE_LEGENDRE_ROUTE.md](DENSE_LEGENDRE_ROUTE.md): candidate quantitative
  dense lower bridge and a new third-order Legendre history estimate.
  [LEGENDRE_REVIEW.md](LEGENDRE_REVIEW.md) accepted the new estimates
  conditional on the finite training-source dependency.
  [SOURCE_SCOPE_CHECK.md](SOURCE_SCOPE_CHECK.md) reconstructs that dependency,
  removes the unnecessary `m>=d` restriction by an exact training-span
  reduction, and completes its random-prefix interpolation geometry. The
  final addendum in the Legendre review accepts the assembled polynomial-width
  conclusion. It explicitly distinguishes this from polynomial onset for
  the original stronger dense lower-bound coefficient.
- [TAYLOR_ROUTE.md](TAYLOR_ROUTE.md): candidate capped flaring domain and
  finite common-cavity probability transfer preserving the current state
  powers. [TAYLOR_REVIEW.md](TAYLOR_REVIEW.md) accepted the calculations
  conditional on repairing a random-prefix endpoint-test gap.
  [TAYLOR_PREFIX_REPAIR.md](TAYLOR_PREFIX_REPAIR.md) supplies a uniform
  deterministic prefix mesh at the unchanged polynomial width. The Taylor
  review's final addendum accepts the repaired source, absolute-accuracy and
  storage assembly. A separate fresh review of the new completions is in
  [PREFIX_COMPLETION_REVIEW.md](PREFIX_COMPLETION_REVIEW.md).
- [HARMONIC_FIXED_DIMENSION_SCOPE.md](HARMONIC_FIXED_DIMENSION_SCOPE.md)
  distinguishes the remaining fixed-dimension sample/gap proof gate from
  the growing-dimension rank obstruction. It does not claim a fixed-dimension
  impossibility result. The unchanged fixed-dimension repair remains open.

The coordinator has reconstructed the complete Harmonic rank proof, the
standalone anti-concentration lemma, and the new Legendre and Taylor route
calculations. The inherited local insertion proof chain is not silently
certified by those new calculations; it has its separate reconstruction and
stated review boundary. No success of all three repairs is
claimed. A replacement Harmonic source criterion is a separate research
question; it is not the polynomial-threshold upgrade of the unchanged
construction tested here.
