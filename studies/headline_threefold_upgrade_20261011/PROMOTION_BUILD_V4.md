# Promotion build validation: corrected frozen v4

## Result

The standalone frozen project
`data/generated/headline_threefold_upgrade_20261011/promotion_v4/docs` passed
all requested format commands, in order: HTML, PDF, then editable LaTeX. Each
completed with exit status `0`. The automated log scan found no unresolved
references/citations, missing targets, malformed environments, duplicate
identifiers, or build failures.

No candidate `.qmd` or `_quarto.yml` input changed during validation. The
before and after source manifests have the same SHA-256:
`d019a4e45e135311bea04a16469c1b772a156233657185caa9f307dd433890bb`;
their diff is empty.

## Environment and exact commands

- Quarto: `/tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto`
  (version `1.8.27`).
- XeLaTeX: `XeTeX 3.141592653-2.6-0.999993 (TeX Live 2022/dev/Debian)`.
- latexmk: `4.76` (20 November 2021).
- Working directory:
  `data/generated/headline_threefold_upgrade_20261011/promotion_v4/docs`.
- Cache:
  `/home/amir/Codes/PDE/data/generated/headline_threefold_upgrade_20261011/promotion_v4/quarto-cache`.

Commands, run once each in the listed order:

```sh
XDG_CACHE_HOME=/home/amir/Codes/PDE/data/generated/headline_threefold_upgrade_20261011/promotion_v4/quarto-cache /tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto render --to html
XDG_CACHE_HOME=/home/amir/Codes/PDE/data/generated/headline_threefold_upgrade_20261011/promotion_v4/quarto-cache /tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto render --to pdf
XDG_CACHE_HOME=/home/amir/Codes/PDE/data/generated/headline_threefold_upgrade_20261011/promotion_v4/quarto-cache /tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto render --to latex
```

| Format | Status | Primary output |
|---|---:|---|
| HTML | `0` | `data/generated/DTDL/index.html` |
| PDF | `0` | `data/generated/DTDL/DTDL.pdf` |
| editable LaTeX | `0` | `data/generated/DTDL/book-latex/DTDL.tex` |

HTML packaging completed and reported that it rewrote zero HTML code links.
The navigation document contains sidebar, breadcrumb, TOC, and page-navigation
elements; no navigation error was reported in the renderer logs.

## Output and integrity evidence

Under `data/generated/headline_threefold_upgrade_20261011/promotion_v4/`:

- `candidate-source-sha256-before.txt`, `candidate-source-sha256-after.txt`,
  and `candidate-source-hash-diff.txt` are the immutable-input records.
- `build-html.stdout-stderr.log`, `build-pdf.stdout-stderr.log`, and
  `build-latex.stdout-stderr.log` are the complete command logs.
- `build-log-diagnostics.txt` is empty (SHA-256 of the empty file:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).
- `rendered-output-paths.txt` and `rendered-output-sha256.txt` enumerate and
  hash the 25 produced HTML/PDF/TeX artifacts. Their SHA-256 values are,
  respectively,
  `5523083fbc66132ac1df496f24f246b7b4f1bb64b37fdd0dc13a986263d4d141`
  and `7c92dd7e4a007c31f82798a1820ccd60bb6ed14e568d88a911784484f32eb3ff`.
- `validation-artifact-sha256.txt` hashes the validation records.

Simple text extraction locates the assembled nonlinear-feature theorem at PDF
page 991, its proof at page 999, and the headline-theorem assembly proof at
page 1000 (`new-material-pdf-pages.txt`). The coordinator separately visually
checked pages 923 and 967 and found the table fit.

## Limitation discovered after the mechanical log scan

The coordinator's visual PDF check found four newly added `@sec-*` references
that render as empty `Section .` references under the existing
`number-sections: false` configuration (one example is at the end of the
proposition on PDF page 967). This is a visual/cross-reference presentation
defect not emitted as a Quarto log warning, so it is not contradicted by the
clean automated scan above. It concerns only four new candidate references;
older unrelated empty section references are outside this candidate scope.
The coordinator staged v5 to change only these four references. No v4 source
was altered here.
