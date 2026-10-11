# Final corrected paper build

2026-10-11. The coordinator compiled the final frozen sources in
`data/generated/headline_threefold_upgrade_20261011/paper_integration_v3/paper/`
using

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../build compact.tex
```

The command exited 0. Its complete final LaTeX transcript is `../build/compact.log`.
The 94-page PDF has SHA-256
`9c805f6cd89280b7ce92435e3c3a66ecda2e578c03b69c73b98ee60ac7ae13f9`.
The final log has no unresolved references/citations, duplicate-label errors,
overfull boxes, underfull boxes or LaTeX errors. The only warning is the
approved source's nonfatal legacy `\choose` notation warning from amsmath.

Version 3 clarifies the source-proof opening as well as its concluding
reduction paragraph: the width and initialization arguments explicitly recall
the coefficient recurrences they reuse. The changes are prose-only. All
mathematics, labels and bounds are unchanged from the first integrated paper.
The book has the corresponding two prose clarifications and no mathematical
changes from its approved version 6.

`PAPER_INTEGRATION_check.py` verifies all original model, norm, small-label,
storage and error equations, the 30-symbol inventory, unchanged feature-learning
and NTH dependencies, immediate theorem/proposition placement, references and
book correspondence. The frozen hashes/results are in
`paper_integration_v3/preservation.json`.

The theorem/proposition pages 3–4 have identical `pdftotext -layout` output
to version 1, whose actual render was independently inspected and viewed by
the coordinator; see `PAPER_BUILD_V1.md`. No unchanged visual check was repeated.
This record documents compilation and preservation, not mathematical acceptance;
the fresh independent final integration report supplies that separate review.
