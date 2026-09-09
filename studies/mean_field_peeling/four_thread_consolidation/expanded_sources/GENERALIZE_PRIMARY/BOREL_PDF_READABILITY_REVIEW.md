# Independent readability and coverage review of the combined PDF additions

Date: 2026-09-06.

Scope: the user's request to incorporate the prior Borel, Padé and Stieltjes discussion into the existing population-GF paper, with the main exposition kept at no more than ten pages and detailed mechanics in appendices. This review checks exposition, notation, completeness, epistemic status and visual layout. It is not a new proof audit of the underlying general-depth GF theorem.

## Material read

- `BOREL_HYPOTHESIS_AND_LOCAL_IMPLICATIONS.md`, in full.
- `PADE_BOREL_UNIFORM_APPROXIMATION.md`, in full.
- The inherited user conversation, including the Hausdorff coefficient criterion that appears in the conversation but not in the earlier Padé synthesis note.
- `gf_exposition/borel_population.tex`, in full.
- `gf_exposition/pade_stieltjes.tex`, in full.
- Extracted text of the new appendices in `gf_exposition/gf-complete.txt`.
- Visual renders of every page of the new appendices in the first compilation, followed by a check of the final compilation, where those appendices occupy pages 21–33 of `gf_exposition/gf-complete.pdf`. The final rendered bodies were compared pixel for pixel with the individually inspected earlier pages; all thirteen bodies were unchanged. Final pages 21, 26, 27 and 33 were also directly viewed.

Reviewed final PDF: 34 pages, SHA-256 `f1da61e0a49bb3e960651186a8f897f29cab4a4e497fc001abdc69540427d5ae`.

## Coverage

The new appendices cover all substantive topics in the prior discussion:

1. The original one-input output-dependent-kernel conjecture and its stronger all-time and weaker compact-time versions.
2. Formal initialization jets and their conversion into kernel coefficients, with physical time normalized consistently with the main paper.
3. Borel coefficient damping, continuation, Laplace reconstruction, finite rational approximation and finite quadrature as distinct steps.
4. Why exact integration of a truncated Borel series simply returns Taylor truncation.
5. Actual-target identification, the flat-function ODE counterexample, and the fact that the broad GF theorem does not supply all-order jets or summability.
6. Local scalar kernel-to-prediction and loss error bounds, the time margin, the conditional all-time bound, and the additional matrix reconstruction premise for multiple inputs.
7. The existing joint width/GD theorem combined with finite reconstruction by a triangle inequality, including the fixed positive time and approximation-order quantifiers.
8. Genuine Padé matching, the compact positive Stieltjes theorem and its Gaussian-quadrature proof, explicit finite-order bounds, determinate unbounded measures and the divergent factorial example.
9. Borel-to-Laplace error transfer, full-integral versus cutoff constructions, quadrature and the distinction between a rational final expression and ordinary direct Padé.
10. Stieltjes structure of the Borel transform, the direct-Padé bridge for Borel exponent at most two, the Hausdorff and Hankel coefficient criteria, and the all-order nature of those tests.
11. Meromorphic fixed-denominator rows, the limitations of diagonal/capacity statements, and constructive conformal rational approximation.

## Readability and notation

The exposition retains the main mechanisms rather than reducing them to theorem names. In particular, positivity is explained through Gaussian quadrature; Borel transfer is explained by splitting the reconstruction integral; scalar stability is explained through travel time along the output coordinate; and matrix stability is explained through the weighted residual energy.

Notation is locally introduced and economical. The scalar output-dependent kernel is explicitly distinguished from fixed layer learning multipliers. The Borel exponent is distinguished from initialization scales, and the support bound is distinguished from the earlier localization cutoff. Explicit minima and maxima of the kernel replace unnecessary numerical aliases. The main network notation is preserved, and separate multiple-input reconstruction is clearly marked as an additional conjecture.

No apparent claim was found that the nonlinear neural kernel is already Stieltjes, Borel summable, or generically recoverable by diagonal Padé. The text also avoids claiming that reconstruction of predictions automatically reconstructs the full hidden population state.

## Requested clarifications and resolution

- Requested explicit `C>0` and `b>=0` in the Borel exponential-envelope example, so the bound is uniform over the whole nonnegative output interval. Applied.
- Requested the same local sign clarification in the conformal exponential-bound example. Applied.
- Suggested an explicit sentence distinguishing scalar `kappa` from layer multipliers `kappa_ell`. Applied.
- Flagged that the conversation's Hausdorff finite-difference criterion should be included in addition to the earlier note's Hankel criterion. Both are present.

## Visual check and verdict

All thirteen new appendix pages were rendered and inspected. Equations, subscripts, fractions, sums and integrals are properly typeset, with no clipped expressions or overlapping text. The page transitions are ordinary continuous-paper transitions. In the final compilation Appendix A occupies pages 10–20, Appendix B pages 21–26, Appendix C pages 27–33, and references follow on page 34. The main exposition remains pages 1–9. The final adjustment compacted equivalent general-loss displays in Appendix A and changed bibliography alignment; the new appendix bodies are unchanged.

**PASS.** No unresolved substantive readability, coverage or layout issue remains in the inspected version. The extra technical derivations are located in the appendices, as requested.
