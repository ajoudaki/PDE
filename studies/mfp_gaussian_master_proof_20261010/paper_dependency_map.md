# Standalone MFP extraction: dependency map

This is an editorial dependency audit of maintained material, not a new result or promotion review. Scientific inputs were limited to the assigned maintained sources. No other study, archive, or existing paper was consulted. Source line numbers below refer to the current checkout on 2026-10-11. The canonical-notation skill and its neural-response-memory reference were applied.

## Required source blocks

| Source | Lines | Standalone role |
| --- | ---: | --- |
| `docs/02-gaussian-reuse.qmd` | 252–1293 | Complete central theorem, source evaluator, all-moment lemma and proof, bounded typed extension and proof, clipping argument, physical AD and derivative closure, initialization reduction, six worked examples and compiler introduction. Preserve all of this mathematical content. |
| `docs/12-three-sample-learning.qmd` | 316–684 | Complete bounded-derivative foundation III.F.1–6. The central proof actually uses the operator moments, adaptive Gaussian conditioning, source cancellation, singular-query regularization and causal feedback. This should become a self-contained appendix or earlier foundation section, with all proofs retained. |
| `docs/02-gaussian-reuse.qmd` | 15–95 | Exact one-forward/one-transpose projection law and proof, including `eq-docs-gaussian-calculus-l34`, needed for the finite-width reuse correction. Its elementary limit and Stein argument also provide an accessible introduction. |
| `docs/02-gaussian-reuse.qmd` | 193–251 | Exact Gaussian polynomial recurrence `eq-docs-gaussian-calculus-l211`, its singular-covariance proof, and exact PSD validation. Needed by the activation-moment reduction and rational compiler explanation. |
| `code/MFP_CALCULUS.md` | 1–416 | Complete compiler API, scope, derivative conventions, frozen seeds, simultaneous updates/history pullbacks, executable examples, kernel coefficients, returned graph and independent interpreter. Adapt repository commands and links to the packaged paper code. |
| `docs/notation.qmd` | 8–68 | Import only the needed setup conventions: dimensions and matrix shapes, data Gram, forward model, residual, backward derivative convention, normalized pairings, finite transpose, population expectations and Wasserstein metric. |
| `docs/notation.qmd` | 70–82 | Explain the separate small-readout law explicitly if retaining its comparison: stored readout variance is `1/n^2`; the paper's central theorem instead has a fixed root law and examples use order-one readout. Retain actual physical mobilities. |
| `docs/references.bib` | entry `golikov2022nongaussian` | Preserve the precise attribution of the raw-entry moment mechanism to Appendix J of Golikov and Yang, *Non-Gaussian Tensor Programs* (NeurIPS 2022). The paper proves the form it uses; that reference is attribution, not an unprovided proof hypothesis. |

The adjacent source block `docs/02-gaussian-reuse.qmd:96–160` is optional: it repeats the exact two-sided conditioning supplied in full by the foundation appendix. Including the whole preliminary block 15–251 is a simple, safe presentation choice. Lines 161–192 give the optional moving-gradient illustration referred to by the central text.

The central theorem does not require importing the feature-ascent width theorem, the continuity specializations, the later explicit MLP jet recurrence, or the book's population-flow chapters. Those are contextual comparisons, not missing proof steps.

## Cross-reference conversion

Every `sec-mfp-*`, `def-mfp-*`, `thm-mfp-*`, `lem-mfp-*`, `prp-mfp-*`, `proof-mfp-*`, and `eq-mfp-*` identifier in the central block can retain its exact ID as a LaTeX label. The following are all references that leave that central block:

| Central source location | Target | Required action |
| --- | --- | --- |
| 438 | `golikov2022nongaussian` | Bibliographic citation; retain Appendix J attribution. |
| 553–554 | `eq-docs-special-data-limits-l3859`, `eq-docs-special-data-limits-l3866` | Internal references to foundation III.F.2 (Gaussian operator tails and all fixed moments). |
| 577–579 | `thm-docs-special-data-limits-l3820`, `sec-docs-special-data-limits-l3884`, `lem-docs-special-data-limits-l3966`, `lem-docs-special-data-limits-l4011` | Internal references to foundation III.F.1, III.F.3, III.F.4 and III.F.5. |
| 592, 596, 602, 609 | `eq-docs-special-data-limits-l3896`, `eq-docs-special-data-limits-l3916`, `lem-docs-special-data-limits-l3966`, `lem-docs-special-data-limits-l4011` | Internal appendix references; all proof passages are required. |
| 638 | `sec-docs-special-data-limits-l4054` | Internal reference to foundation III.F.6. |
| 650–651 | `sec-docs-global-nonlinear-l1840`, `thm-docs-gaussian-calculus-l289` | Replace comparison links with a scope sentence: the smooth Gaussian theorem has stronger hypotheses than the preceding bounded-derivative foundation and does not subsume other lower-regularity or differently initialized specializations. No new result is needed. |
| 726 | `lem-docs-special-data-limits-l4011` | Internal reference to covariance-square-root continuity in singular-query proof. |
| 867 | `sec-docs-gaussian-calculus-l170` | If preliminaries 161–192 are included, use an internal reference. Otherwise retain the explicit second-derivative formula immediately preceding this comparison and omit the comparison sentence. |
| 868 | `sec-docs-gaussian-calculus-l5338` | The finite MLP recurrence is an optional illustration. Replace this book-navigation reference with the paper's own general recursion or neural examples; do not assert it is a missing proof premise. |
| 926 | `notation.qmd#sec-docs-notation-l70` | Supply the concrete separate small-readout variance `1/n^2` and contrast the fixed-root scope in prose. |
| 1011 | `eq-docs-gaussian-calculus-l211` | Internal reference to included Gaussian moment recurrence. |
| 1034 | `eq-docs-gaussian-calculus-l34` | Internal reference to included exact one-forward/one-transpose projection law. |
| 1282 | `../code/MFP_CALCULUS.md` | Internal compiler/API appendix and relative link to the packaged code guide. |

All other cross-references in the central block are internal to that block. All equation, theorem and lemma cross-references in foundation III.F.1–6 resolve within lines 316–684. Its remaining Markdown links are references among III.F.2–5; replace the displayed book-specific names “III.F.*” with the resulting paper section numbers. The bare “Part III.M” reference in line 331 is the one non-link external dependency; remove only the network-application aside described below.

The compiler guide has a link to the central finite-program theorem and links to `scripts/example_mfp_mlp_derivative.py` and `scripts/example_mfp_kernel_jets.py`; repoint these to bundled files. Its run commands mention `code/`, `data/established/` and the edition root, so describe the packaged execution root explicitly. Keep the fresh-output-directory requirement for the kernel producer.

## Self-containment repairs that are purely editorial

1. Before the neural model, state that `L` is the fixed hidden depth, `m` the fixed sample count, `d` the input dimension, `n` the width, `a,b` sample indices, and `ell` a hidden-layer index; give `W^(1)` shape `n by d`, hidden matrix shape `n by n`, and readout length `n`. Define fixed inputs and scalar labels. Define `G_ab=x_a^T x_b/d` where first used. No input whitening or Gram nonsingularity is assumed.
2. Foundation line 331 has an unrelated three-sample application aside, beginning “In the network application” and ending “Part III.M.” It introduces `w_0`, `u_i` and `V^(1)` not otherwise defined in the extraction. Omit this aside; retain the general iid root assumptions and the independent Gaussian probe/regularization sentence. The foundation's theorem and proof are unaffected.
3. Foundation line 322 uses adjacent-layer types; retain this narrower foundation statement. The central bounded typed extension explicitly proves the extension to arbitrary fixed named edges, parallel edges and type-graph cycles. Do not silently rewrite the foundation itself as the stronger graph theorem.
4. In the reuse example, explicitly recall that the single named `W` is an `n by n` matrix with independent `N(0,1/n)` entries between two distinct types and that `e` is the length-`n` constant-one vector. Define `N(0,K)`, the empirical law and `W_2` using the foundation's own formulas.
5. Keep distinct source symbols and physical derivative coordinates. Singular support does not identify formal source arguments before differentiating. Frozen physical seed values retain their Gaussian source dependence. Source groups are independent; output fields generally are not.
6. Keep every loss normalization local. The general neural model uses full mean square loss; the normalized-update example uses a different explicitly stated scalar loss; the kernel jets use half mean square loss, so their physical velocity is halved. Jets contain `1/r!`; moving derivatives include vector-field and residual motion.
7. Keep the fixed-root restriction and the exact/asymptotic boundary prominent. Finite AD, rank lowering, finite update identities and the displayed finite reuse correction are exact. Gaussian compilation returns width limits, not finite-width expected values. No growing order/depth/update count or positive-time reconstruction follows.
8. Preserve the literal-original-preactivation restriction of the activation-moment normal form. Generic nonlinear compositions remain finite Gaussian expectation graphs; they need not reduce to that restricted normal form. Concrete root covariances in the frontend and fixed symbolic geometric factors are different API features.

## Suggested paper order and titles

Use an introduction stating the exact finite computation / asymptotic Gaussian evaluation distinction, a short canonical setup, the one-forward/transpose illustration, then the complete central block in its existing order. Put the complete bounded-derivative foundation and exact Gaussian polynomial recurrence in appendices, followed by the full compiler guide and bundled source listings or file inventory. Forward references from the main proof to those appendices are sufficient for self-containment.

Purely editorial titles can be “Mean-Field Peeling for Fixed Finite Gaussian Derivative Programs,” “Typed programs and the scalar limit theorem,” “Exact finite differentiation,” “Gaussian source-response evaluation,” and “Bounded-derivative foundation.” Remove the original chapter numbers, “III.F.*,” “older foundation,” “the maintained interface,” and unrelated book-navigation language where those presume the book. Preserve mathematical theorem names and every hypothesis, limitation and attribution.

No missing scientific premise remains after including the required source blocks and making these setup/reference repairs. This report does not audit implementation files or certify compiled output; those were outside its allowed input scope.
