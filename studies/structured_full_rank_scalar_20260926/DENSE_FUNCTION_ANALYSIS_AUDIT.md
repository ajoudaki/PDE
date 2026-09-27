# Bounded audit of canonical-Gaussian function analysis

2026-09-26. Collaborative code audit of the current analyzer, plotting script,
and revised frozen protocol. No training or scientific selection was performed.
The audit was stopped at the user's request for an immediate report; no new
raw-pair calculation or extended numerical check was undertaken in this pass.

The primary analyzer implements the corrected objective correctly. For each
matching task/width/seed/stage pair it computes
`D=RMS(f_candidate-f_Gaussian)` and then `D/RMS(f_Gaussian)` on the same
saved grid. It summarizes the per-seed ratios, rather than dividing two
across-seed averages. It retains absolute error, canonical norm, sampled
maximum error, and worst-seed relative error. A zero canonical norm is
explicitly excluded from relative screening. The Gaussian replicate is
context only; teacher-risk classifications are separate historical outputs.

Per-cell bootstrap resampling preserves candidate/Gaussian pairing by using
the already paired seed measurements. Aggregate bootstrap resamples whole
seed blocks across all tasks and widths, retaining their shared-initialization
dependence. The revised 5% screen requires all twelve paired snapshots,
fitting in both models, and the specified numerical gates. Missing fit6
snapshots remain missing and prevent a pass. Failed continuations preserve
prior valid snapshots and retain their failed-attempt metadata.

The paired function quadrature gate checks both D and the canonical norm
against their nested half grid. It does not substitute teacher-risk similarity
for function agreement. If only one member has a refined circle array, the
pair uses their shared base grid and checks that grid directly. This can
conservatively leave a pair unresolved; it does not justify inventing the
other member's fine-grid predictions.

Actionable caveats:

1. **Curve plots mix endpoint types.** `curve_plot` uses fit6 when available
   and otherwise each run's final state. Its page title calls these “fitted
   functions,” but some lines can be nonfitting T=300 states. The subtitle
   mentions the fallback without identifying individual lines. Use separate
   fit6 and common-time panels, omit unavailable fit6 lines with an explicit
   count, or label every fallback and its time/fitting status. Do not present
   this mixed panel as a uniformly matched-fit comparison.
2. **The time300 heatmap footer misstates fitting coverage.** Its pair count
   is based on snapshot availability. The footer calls these fitted pairs,
   although every valid T=300 trajectory has that snapshot irrespective of
   training convergence. Label them available common-time pairs and show
   fitting coverage separately. The heatmap also bypasses the analyzer's
   numerical gates and bootstrap intervals, so it is descriptive only.
3. **Refinement coverage is not enforced automatically.** Numerical issues
   are constructed from the refinement runs actually supplied. An omitted
   planned refinement directory creates no missing-check warning. Therefore
   “numerically valid” means the supplied checks did not fail, not that the
   full planned refinement program was completed. The final report must
   explicitly state that support is limited to the completed 42 checks;
   interrupted long-horizon refinements provide no completed validation.
4. **Keep the two endpoint questions distinct.** Common T=300 function
   discrepancies remain useful even for nonfitting runs, while the operational
   agreement screen deliberately remains inconclusive without twelve fitted
   pairs. Reporting the observed discrepancy is not equivalent to passing
   the screen. With continuation interrupted, use the complete principal
   dataset and identify unavailable matched-fit comparisons explicitly.

No defect was found in the primary function-distance formula, canonical
normalization, per-seed pairing, or aggregate bootstrap dependence. This
bounded audit does not certify unexamined final output files or the
interrupted continuation/refinement campaigns.
