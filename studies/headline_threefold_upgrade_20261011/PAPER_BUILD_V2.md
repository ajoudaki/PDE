# Final paper compilation and source correspondence

2026-10-11. Coordinator check of the corrected frozen paper at
`data/generated/headline_threefold_upgrade_20261011/paper_integration_v2/`.
This is a compilation/preservation check, not an independent mathematical review.

The only scientific-source difference from the first integrated paper is a
prose clarification in `compact_foundations.tex`: the later quantitative
width/setup proofs explicitly recall and reuse its source coefficients.
No equation, hypothesis, reference target, algorithm or cost changes.
The matching book clarification is recorded by `PAPER_INTEGRATION_check.py`.

From the frozen `paper/` directory the coordinator ran:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../build compact.tex
```

The command exited 0, including bibliography and repeated LaTeX passes needed
to resolve references. The complete final engine transcript is
`paper_integration_v2/build/compact.log`. The output is 94 pages, SHA-256
`63bac960e3bdeead403274b49a302740f4de1d868ad634f88d20c390e7ff345d`.

The final log has no unresolved reference/citation, duplicate-label error,
overfull box, underfull box or LaTeX error. The one retained nonfatal amsmath
warning concerns the approved source's legacy `\choose` notation; it does
not change the rendered formula or require a mathematical correction.

`pdftotext -layout` outputs for pages 3–4 of versions 1 and 2 are identical.
Those are the headline theorem and immediately following initialization
proposition, already visually checked at 1500-pixel resolution by the
coordinator and independently in `PAPER_BUILD_V1.md`. No repeated unchanged
visual inspection was needed. All equations and conditions, the new proposition
table, the detailed widths and eight setup ledgers are present.

`PAPER_INTEGRATION_check.py` verifies the unchanged original model, norm,
label and headline storage/error equations, unchanged 30-symbol inventory,
unmodified feature-learning/NTH inputs, no duplicate labels or missing references,
and exact source correspondence to the approved book except the two recorded
locality clarifications. Its frozen result is `paper_integration_v2/preservation.json`.
No source file was changed by this build.
