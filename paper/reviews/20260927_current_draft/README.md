# Fresh current-draft feedback — 27 September 2026

Two fresh, independent agents read the same frozen current manuscript and paper-owned evidence. Neither received the conversation, earlier reviews, or the other reader's conclusions. The reviewer assessed mathematical support and scientific scope; the visionary assessed the strongest defensible contribution and presentation. This is an author-requested assessment, not a journal decision or an exhaustive novelty determination.

**Later draft:** [Updated revision plan for commit `7ffb91f`](UPDATED_REVISION_PLAN_7ffb91f.md) reconciles these reviews with the subsequent editorial changes and the successful 40-page rebuild. The original reports and frozen inputs below remain unchanged.

- [Critical reviewer](reviewer/review.md)
- [Scientific visionary](visionary/review.md)
- Each directory also contains its own claim ledger, evidence log, and code audit.
- [Assignment](ASSIGNMENT.md) and [frozen-input manifest](inputs/manifest.json)

The snapshot is the 41-page manuscript at repository commit `b7b5424bc382e4e8c8cec402cd090f24a9f16a51`. The source hash is `ca76e3568263db1d219ed80f13fd52006598572e6f4f1a8608f68f9c1a40c4ca`. All 31 manifest entries were verified. No manuscript edits or training runs were made for this assessment.

## Restoring the local evidence bundles

The five NPZ copies in `inputs/figures/` are ignored generated-data copies of
bundles already tracked in the snapshot commit above. Their SHA-256 hashes were
checked against that commit before archiving this review. From the repository
root, restore them after a fresh checkout with:

```bash
for bundle in frozen_ntk_source learning_controls_source radial_source_data response_memory_source sphere_source_data; do
  git show "b7b5424bc382e4e8c8cec402cd090f24a9f16a51:paper/figures/${bundle}.npz" > "paper/reviews/20260927_current_draft/inputs/figures/${bundle}.npz"
done
```

Disposable page-render PNGs and contact sheets are not versioned. The frozen
manuscript, figure PDFs, source, manifest, checking scripts and reports are retained.

## Shared scientific assessment

Both readers independently found the central fixed-width proof chain coherent: the learning-speed clock gives uniform finite-horizon parameter-trajectory error of order `P^-1`, and the joint clock gives `P^-2`, under their respective stated regularity and existence conditions. They checked the projection-energy identity, paired velocity defect, depth recursion, feedback comparison, and the noncircular joint-clock bound. Neither established a material error in these arguments.

Their strongest common formulation of the contribution is:

> Deep nonlinear learned interactions admit an autonomously evolving, finite response memory that approximates the specified full training trajectory on every prescribed finite horizon. The proof controls the feedback between that memory and the network whose responses it stores.

This is stronger than compressing a fitted snapshot or selecting a low-rank parameterization. At a fixed order the number of evolving memory coordinates does not grow with elapsed training steps. It is not a proof that one fixed order works for all horizons, that the required order is uniform in width, or that total storage/runtime improves after including the initialized matrices.

The visionary would center this constructive theorem and use the idealized-learning analogy afterward. The reviewer likewise regards the theorem as the paper's strongest established contribution, while asking that auxiliary claims receive the same level of proof support.

## Prioritized revisions

1. **Complete or qualify the auxiliary proofs.** Appendix C uses a correlated initialized operator, density and reference-field exponential-tail facts without providing the necessary construction/lemmas. Appendix D gives proof roadmaps for the operator limit and restricted scalar/PDE nonclosure rather than complete arguments. Both readers classify these as substantive gaps in those supporting results, not counterexamples and not defects in Theorems 6.1–6.2. Results available in unpublished author material must be made self-contained or explicitly conditional here; an implicit reference cannot supply them.

2. **Finish the notation migration.** In `main.tex`, line 1162 still uses depth `H` instead of `L`; lines 1286, 1497 and 1502–1503 use `K` where the defined Lipschitz constant is `Lambda_F`. Line 1359 uses the same barred activation for an n-vector history and its n-by-P moment matrix. Distinguish current responses, histories, stored raw moments, normalized coefficients, and projected endpoints; declare the block Euclidean/Frobenius parameter norm. Figure 2 depicts post-hoc normalized coefficients with an illustrative prefix convention, so its labels should explicitly connect those quantities to the stored moments.

3. **Make the summary comparison as precise as Appendix E.** Put each row's target observable, conditionality, and horizon directly in Table 1. The population root-width estimate is conditional; the published NTH estimate concerns a different scaling/horizon; the DMFT solver costs require specified sampling, discretization and stability assumptions. Preserve the distinction between moving state and fixed resources. The readers found the appendix's conditional allocation algebra sound; the issue is how the table communicates its status.

4. **Sharpen attribution and reconcile the clock conventions.** HiPPO already includes recurrent feedback. The new distinction is paired neural-interaction reconstruction with a quantitative approximation theorem for the prescribed training flow. The two clock constructions also use different backward prefixes. Coordinate independence at P=1 holds with a fixed prefix, and should not suggest equality of the two complete constructions.

5. **Explain the controls using existing records.** State the Gaussian readout initialization divided by width. Report frozen-kernel fitted times and conditioning: some analytic matched-loss endpoints occur around `7.09e7` or `3.33e9`, well beyond the shared-time trajectory panel. This does not invalidate the endpoint-function comparison, but makes its meaning clear. Identify the MNIST task as binary digits 3 versus 8. No new training is needed for these reporting improvements.

## Empirical and source-check coverage

Both readers recomputed the supplied circle, MNIST, sphere and five-task control discrepancies. The reviewer independently checked the empirical-NTK formula by tiny-network finite differences and the joint reconstruction derivative algebra. The 29 factor wins agree with saved aggregate records; not all 29 runs were independently regenerated from raw predictions. Most of the smallest P=7 shared-time discrepancies lie at or below the saved numerical-sensitivity scale, so they should not be used to infer an empirical convergence exponent.

The packet intentionally omitted study-owned training engines and some original producers. This is a limit on these reviews, not evidence that those files are absent from the repository. Neither reader reran training. Targeted primary full texts were consulted for attribution and comparable scope; this was not an exhaustive priority search.

## Recommended next step

Preserve and foreground the core response-memory results. Repair notation and reporting surgically, and handle Appendices C–D separately by supplying their missing arguments or narrowing their stated status. Both readers see a substantive contribution in the surviving core; neither assessment warrants converting that judgment into a definitive historical breakthrough claim without further evidence.
