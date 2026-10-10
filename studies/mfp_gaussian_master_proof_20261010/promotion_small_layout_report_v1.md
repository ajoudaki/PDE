# Narrow display-layout proposal

## Scope and inputs

This proposal covers only the four overflow displays identified at the
1280-pixel viewport by
`data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v5/math_layout_check_scoped/result.json`:
`eq-mfp-activation-growth`, the unlabeled bounded-map RMS inequality in
`sec-mfp-clipping-proof`, `eq-mfp-clipping-errors`, and
`eq-mfp-forward-covariances`. The source inspected was
`studies/mfp_gaussian_master_proof_20261010/promotion_theory.qmd`.

## Proposed replacements

`promotion_small_layout_patches_v1.json` is a top-level array of exact
whole-display `{old,new}` pairs. Each `old` string matches the current source
exactly once. Each replacement preserves the existing formula's ordered
mathematical content, punctuation, label (where present), and surrounding
prose. It only wraps existing terms with `aligned` or `gathered` rows. The
unlabeled target is unambiguous: it is the display beginning
`\\frac{\\|F(u_n;s_n)-F(\\bar u_n;s_*)\\|_2}{\\sqrt n}` immediately after
the bounded-map convergence statement.

The widest proposed row is intentionally shorter than the original full
display; the RMS inequality splits its left side, first sum, and scalar-error
sum across three gathered rows. No source, candidate, live-book, or Git file
was modified.
