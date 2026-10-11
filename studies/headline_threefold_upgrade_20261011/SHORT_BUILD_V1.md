# SHORT_BUILD_V1 — isolated mechanical build and visual check

## Scope and input integrity

This was a scoped mechanical build/visual inspection, not a scientific, proof,
notation, or reference audit.  The frozen input was
`data/generated/headline_threefold_upgrade_20261011/short_paper_v1/paper/`.
There is no `README` in that paper directory or its parent short-paper folder;
therefore no paper metadata README was available to read.  Part 2 of
`RESEARCH_WORKFLOW.md` was read as required for build delegation.

All eleven frozen top-level source hashes were captured before and after the
build and matched exactly (`cmp` exit status 0):

```
62cbca244c507a581f462e0cc8c6a023c21a5ba2d3efba76f5998ffa9ef8bae6  compact.tex
71f50a55613a3df12398d6226b8fe2380805f2f32082e134e7ab45846bfa4bd1  compact_feature_learning.tex
6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f  compact_fitting.tex
44c201bda34d1eac488c9cc3347a4d2cf608128a3f774df65210584606feaf6a  compact_foundations.tex
eccbf4cad4e215fbcfc18263850165b0fd7dc6d8934de7c189a5e12ec89edd22  compact_initialization.tex
862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9  compact_legendre.tex
38e50dee3b89a755e4efb719a8cf3396cd70f78a1cf163dbf0ff91076505a616  compact_nth.tex
cce32506923384c8124e0a5f965591ad3ae67a51b62377098563eda9b4ff54fd  compact_selected.tex
09ae31ecae93a8ba295e3baa8e21d66ed19f6caa7d6a25f71d559df099a0924e  compact_width.tex
f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f  feature_learning_theorem.tex
1a5611e65d89ce20de47c62488c1fa34eb6e80c1777ab310e29723a94a0457a9  references.bib
```

## Build result

Command, run from the frozen `paper/` directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../build compact.tex
```

The command exited successfully and produced
`short_paper_v1/build/compact.pdf`:

```
e800eb5b5095902b1af3a7fdb2c71cceb7cea830d5ad417c205ff73e5082284d  compact.pdf
```

`pdfinfo` reports letter pages and **89 pages**.  This is **5 pages shorter**
than the supplied 94-page baseline.  The build log has no unresolved-reference
or unresolved-citation warning after the final LaTeX/BibTeX passes.

## Section-boundary coverage

The new polynomial-width module begins on PDF page 36.  Its visible boundaries
are: section 6 (p. 36), 6.1 (p. 37), 6.2 (p. 44), 6.3 (p. 45), and 6.4
(p. 48).  The efficient-initialization/setup module begins on PDF page 62.
Its visible boundaries are: section 8 and 8.1 (p. 62), 8.1.1 (p. 63), 8.1.2
(p. 64), 8.2 and 8.2.1 (p. 67), 8.2.2 (p. 68), 8.3 (p. 70), 8.3.1 (p. 71),
8.4 and 8.4.1 (p. 73), and 8.4.2 (p. 74).

## Rendered-page inspection

Pages were rasterized with `pdftoppm -png -r 150` into
`short_paper_v1/visual/` and visually inspected.

- p. 36: width-module opening; heading, displays, theorem opening, and footer
  render cleanly.
- p. 39: dense width proof and an inline ledger; no clipping or overlap seen.
- p. 62: initialization-module opening and first subsection; clean hierarchy
  and page break.
- p. 68: dense initialization proof; formulas and subsection transition are
  legible with no visible collision.
- pp. 73–74: operation/storage ledger and finite-execution cost formulas;
  clean page transition and no visible clipping.
- p. 4: Proposition 1.2 setup-work/peak-memory cost table; rules, columns, and
  all four rows are legible and contained.

## Diagnostics and non-editing recommendation

The final `compact.log` contains two overfull boxes, both in
`compact_width.tex`, plus one nonfatal package warning:

- 8.15297 pt overfull `\\hbox`, source lines 263–281 (the source-initialization
  paragraph; rendered around p. 39).
- 25.07611 pt overfull `\\hbox`, source lines 348–356 (the time-modulus/control
  speed paragraph; rendered in the subsequent width-proof material).
- `amsmath` warns on `compact_initialization.tex` line 580 that foreign command
  `\\atopwithdelims` should be replaced by `\\frac` or `\\genfrac`.

Neither overfull box visibly clips in the inspected raster pages, but they are
real layout defects.  A localized harmless repair for the first is to make the
long `D_{\\rm init}` relation at lines 267–268 a displayed equation (or otherwise
break that formula before the Gram sentence).  For the second, put the long
`D_c=\\max\\{...\\}` definition at lines 349–352 into its own display and begin
the following sentence after it.  These are recommendations only; no frozen
source was edited.  The `\\atopwithdelims` replacement is a separate
compatibility cleanup, not a build blocker.

## Artifacts

- Build artifacts and logs: `data/generated/headline_threefold_upgrade_20261011/short_paper_v1/build/`
- Rendered inspection images: `data/generated/headline_threefold_upgrade_20261011/short_paper_v1/visual/`
- No frozen source, live paper, book, or Git state was modified by this check.
