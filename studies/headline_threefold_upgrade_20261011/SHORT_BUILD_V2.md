# SHORT_BUILD_V2 — isolated mechanical build and visual check

## Scope and packet integrity

This is a mechanical build/visual check of the immutable V2 packet only; it is
not a proof, scientific-content, or citation audit.  The inspected input was
`data/generated/headline_threefold_upgrade_20261011/short_paper_v2/paper/`.
The permitted V1-to-V2 diff check confirms the scope: the two formerly long
inline expressions in `compact_width.tex` are displays (with a harmless clause
reorder), and the leading historical comments in `compact_initialization.tex`
were replaced by one self-contained comment.  No scientific source change was
inspected or assessed.

The before/after top-level source hash manifests are identical (`cmp` exit
status 0).  V2 input hashes:

```
62cbca244c507a581f462e0cc8c6a023c21a5ba2d3efba76f5998ffa9ef8bae6  compact.tex
71f50a55613a3df12398d6226b8fe2380805f2f32082e134e7ab45846bfa4bd1  compact_feature_learning.tex
6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f  compact_fitting.tex
44c201bda34d1eac488c9cc3347a4d2cf608128a3f774df65210584606feaf6a  compact_foundations.tex
f50b3d6f45d7aebdb37cfe6486b0f55637be5c7fc27386e52094112ca76f091a  compact_initialization.tex
862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9  compact_legendre.tex
38e50dee3b89a755e4efb719a8cf3396cd70f78a1cf163dbf0ff91076505a616  compact_nth.tex
cce32506923384c8124e0a5f965591ad3ae67a51b62377098563eda9b4ff54fd  compact_selected.tex
e28d2e777447c2f49ca5b97554ff5a3d2b50f8b867dd0284af96b51eaab49dfe  compact_width.tex
f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f  feature_learning_theorem.tex
1a5611e65d89ce20de47c62488c1fa34eb6e80c1777ab310e29723a94a0457a9  references.bib
```

## Build result

From the V2 frozen `paper/` directory, the prescribed command succeeded:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../build compact.tex
```

The PDF is letter-size, **89 pages** (again five pages below the supplied
94-page baseline):

```
e1befdf23ffb05b4165c17048082da945e54a02305bc1cdd1f6766d5775bc122  compact.pdf
```

The final log has no unresolved labels/citations and no overfull or underfull
box diagnostics.  The only remaining warning is the pre-existing amsmath
compatibility warning in `compact_initialization.tex`, now at input line 578:
foreign command `\\atopwithdelims` should be replaced by `\\frac` or
`\\genfrac`.

## Visual coverage and outcome

Pages were rasterized via `pdftoppm -png -r 150` to
`data/generated/headline_threefold_upgrade_20261011/short_paper_v2/visual/`
and inspected visually.

- p. 39 contains the first repair: the source-initialization Gaussian-tail
  expression is a centered display.  The surrounding dense proof, inline
  ledger, margins, and footer are clean; no clipping or collision observed.
- p. 40 contains the second repair: the `D_c` definition is a centered display.
  It fits cleanly with its adjacent displayed recursions and the dense proof
  text.
- pp. 73–74 cover the common operation/storage and finite-execution cost
  material.  Formula blocks, hierarchy, page break, and margins render cleanly.

The two V1 overfull boxes are therefore mechanically resolved in V2.  No source
was edited during this check.

## Artifacts

- Build products/logs/hashes: `data/generated/headline_threefold_upgrade_20261011/short_paper_v2/build/`
- Rendered images: `data/generated/headline_threefold_upgrade_20261011/short_paper_v2/visual/`
