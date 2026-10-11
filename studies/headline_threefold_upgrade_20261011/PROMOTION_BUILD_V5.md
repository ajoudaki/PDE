# Promotion build validation: corrected frozen v5

## Result

The frozen standalone v5 project at
`data/generated/headline_threefold_upgrade_20261011/promotion_v5/docs` passed
the required full-book renders, in order: HTML, PDF, and editable LaTeX. Every
command exited `0`. The diagnostic scan found no unresolved references or
citations, missing targets, malformed environments, duplicate identifiers,
renderer errors, or build failures.

Candidate source integrity passed: before/after manifests of every `.qmd` and
`_quarto.yml` file are identical (SHA-256
`263ffa7df58a3afd48ccfdc856881a6e31ce8215dfa4fc5b19cf6a39c3d10860`),
and their diff is empty. No source was edited in this validation.

## Environment, commands, and outputs

- Quarto: `/tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto`,
  version `1.8.27`.
- XeLaTeX: `XeTeX 3.141592653-2.6-0.999993 (TeX Live 2022/dev/Debian)`.
- latexmk: version `4.76`.
- Working directory:
  `data/generated/headline_threefold_upgrade_20261011/promotion_v5/docs`.
- Cache:
  `/home/amir/Codes/PDE/data/generated/headline_threefold_upgrade_20261011/promotion_v5/quarto-cache`.

The following commands were run once, in the stated order:

```sh
XDG_CACHE_HOME=/home/amir/Codes/PDE/data/generated/headline_threefold_upgrade_20261011/promotion_v5/quarto-cache /tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto render --to html
XDG_CACHE_HOME=/home/amir/Codes/PDE/data/generated/headline_threefold_upgrade_20261011/promotion_v5/quarto-cache /tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto render --to pdf
XDG_CACHE_HOME=/home/amir/Codes/PDE/data/generated/headline_threefold_upgrade_20261011/promotion_v5/quarto-cache /tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto render --to latex
```

| Format | Exit status | Primary output |
|---|---:|---|
| HTML | `0` | `data/generated/DTDL/index.html` |
| PDF | `0` | `data/generated/DTDL/DTDL.pdf` |
| editable LaTeX | `0` | `data/generated/DTDL/book-latex/DTDL.tex` |

HTML packaging rewrote zero code links. The index contains the expected
sidebar, breadcrumb, TOC, and page-navigation elements; no navigation defect
was reported by the renderer.

## Corrected-reference and PDF checks

The complete extracted PDF contains no `Section .` occurrence
(`empty-section-reference-pages.txt` is empty). The generated LaTeX has two
`Section` cross-reference strings, both resolved and numbered as `Section
C.4.7` (`generated-tex-section-reference-strings.txt`); they are retained as
nonempty existing references, not a candidate defect. Thus no remaining empty
section-reference issue was detected in v5, including the new material.

The page-967 text extraction contains the revised descriptive wording,
`Full parameter and finite-order costs are given in the detailed cost ledger`,
with no empty section label (`page-967-extract.txt`). This record treats the
following as coordinator checks, not an independent visual review: the
coordinator rasterized and viewed v5 PDF page 967, found the table fitted with
legible exponents, and confirmed the corrected cost-ledger link has proper
descriptive text; the coordinator had already viewed unchanged page 923 in v4.

For orientation, text extraction locates the nonlinear-feature theorem at PDF
page 991, its proof at page 999, and the headline-theorem assembly proof at
page 1000 (`new-material-pdf-pages.txt`).

## Preserved evidence

All listed artifacts are under
`data/generated/headline_threefold_upgrade_20261011/promotion_v5/`:

- `candidate-source-sha256-before.txt`, `candidate-source-sha256-after.txt`,
  and `candidate-source-hash-diff.txt` preserve input integrity.
- `build-html.stdout-stderr.log`, `build-pdf.stdout-stderr.log`, and
  `build-latex.stdout-stderr.log` preserve complete renderer output.
- `build-log-diagnostics.txt` is empty (SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).
- `rendered-output-paths.txt` and `rendered-output-sha256.txt` enumerate and
  hash all 25 HTML/PDF/TeX output artifacts; their own SHA-256 values are
  `6a968b6114ab181884793ec5a75cf59f84e0df106c7ed418804e48a9215f8edc`
  and `26f3553be5ebd870c0ec7aba13ae8adb410bc826673b2f1b7f357f1b9a189ead`.
- `empty-section-reference-pages.txt`, `page-967-extract.txt`,
  `generated-tex-section-reference-strings.txt`,
  `new-material-pdf-pages.txt`, and `html-navigation-check.txt` record the
  targeted cross-reference, page, and navigation checks.
- `validation-artifact-sha256.txt` hashes the validation records.
