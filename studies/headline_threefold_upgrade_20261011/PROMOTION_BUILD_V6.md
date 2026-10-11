# Promotion build validation: final frozen v6

## Result

The frozen standalone project
`data/generated/headline_threefold_upgrade_20261011/promotion_v6/docs` passed
the complete requested render sequence: HTML, PDF, then editable LaTeX. Each
command ran once and exited `0`. No source file was edited during validation.

The candidate `.qmd`/`_quarto.yml` manifests before and after rendering have
the same SHA-256,
`5b11521842db1b2a4d20f035a6a26b038fa78b31e808128ecec557df436e379e`,
and their diff is empty.

## Environment and exact commands

- Quarto: `/tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto`
  (version `1.8.27`).
- Cache:
  `/home/amir/Codes/PDE/data/generated/headline_threefold_upgrade_20261011/promotion_v6/quarto-cache`.
- Working directory:
  `data/generated/headline_threefold_upgrade_20261011/promotion_v6/docs`.

```sh
XDG_CACHE_HOME=/home/amir/Codes/PDE/data/generated/headline_threefold_upgrade_20261011/promotion_v6/quarto-cache /tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto render --to html
XDG_CACHE_HOME=/home/amir/Codes/PDE/data/generated/headline_threefold_upgrade_20261011/promotion_v6/quarto-cache /tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto render --to pdf
XDG_CACHE_HOME=/home/amir/Codes/PDE/data/generated/headline_threefold_upgrade_20261011/promotion_v6/quarto-cache /tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto render --to latex
```

| Format | Exit status | Primary output |
|---|---:|---|
| HTML | `0` | `data/generated/DTDL/index.html` |
| PDF | `0` | `data/generated/DTDL/DTDL.pdf` |
| editable LaTeX | `0` | `data/generated/DTDL/book-latex/DTDL.tex` |

HTML packaging rewrote zero code links. The index has sidebar, breadcrumb,
TOC, and page-navigation elements (`html-navigation-check.txt`).

## Mechanical diagnostics and targeted layout check

The combined log diagnostic scan is empty: no unresolved references/citations,
missing targets, malformed environments, duplicate identifiers, or build
errors were reported. Complete PDF text contains no empty `Section .`
reference (`empty-section-reference-pages.txt` is empty). The two generated
LaTeX `Section` references both resolve to `C.4.7`; they are retained existing
references, not empty or new defects.

The corrected mobility tuple is within **Lemma 29, “Finite training and panel
sources”**: the lemma begins on PDF page 923 and continues onto page 924.
For the precisely checked width/setup interval, pages 923--991, `pdftotext -bbox`
found no word with `xMax > 545 pt`
(`width-setup-pages-923-991-bbox.html` and empty
`width-setup-pages-923-991-xmax-over-545.txt`). Thus the requested
right-margin overflow threshold is not reached anywhere in the complete
checked interval; the former inline tuple no longer produces the detected
overflow. The earlier pages-923--967 scan is retained as superseded evidence;
it did not cover the full setup span and is not the basis for this conclusion.

This validation did not independently perform a visual review. The coordinator
separately rasterized and viewed v6 PDF page 924, reporting that the mobility
tuple is centered in a display within normal margins and that the remaining
lemma/proof start is legible. The coordinator also supplied the normalized
v5/v6 full-chapter-string SHA-256
`9783236b8d73ece12faee44483ddd81733410e85c6e2e2592796832ad40558ad`,
after removal of whitespace and dollar math delimiters; this is recorded as a
coordinator check, not independently recomputed here.

## Preserved artifacts

All evidence below is in
`data/generated/headline_threefold_upgrade_20261011/promotion_v6/`:

- `candidate-source-sha256-before.txt`, `candidate-source-sha256-after.txt`,
  and `candidate-source-hash-diff.txt` record input integrity.
- `build-html.stdout-stderr.log`, `build-pdf.stdout-stderr.log`, and
  `build-latex.stdout-stderr.log` retain the complete format logs.
- `build-log-diagnostics.txt`, `empty-section-reference-pages.txt`, and
  `width-setup-pages-923-991-xmax-over-545.txt` are empty; each has the empty-file SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- `rendered-output-paths.txt` and `rendered-output-sha256.txt` enumerate and
  hash all 25 present HTML/PDF/TeX artifacts; their own SHA-256 values are
  `b2ae2ee1ef944b06b68f49b85949acf2ed6d273527216cbb5f8c7bb33d9e9365`
  and `18347bbd3dcbe9d64a5893585ffdbe7573767bf740e11aff17b2f7e689606b7b`.
- The bbox, PDF-page extraction, source-context, navigation, and generated-TeX
  reference records are named and hashed in `validation-artifact-sha256.txt`.
