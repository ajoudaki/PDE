# Paper build and narrow layout diagnostic (v1)

Scope: frozen compact-paper inputs only at
`data/generated/headline_threefold_upgrade_20261011/paper_integration_v1/paper/`.
No source files were edited. This is a build/layout diagnostic, not a
mathematical audit.

## Inputs and preservation

`preservation.json` was the initial manifest. Before the build, all ten
listed source SHA-256 values matched it. The same values were recomputed after
the build and still match:

```
compact.tex                    62cbca244c507a581f462e0cc8c6a023c21a5ba2d3efba76f5998ffa9ef8bae6
feature_learning_theorem.tex   f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f
compact_fitting.tex            6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f
compact_foundations.tex        5b7ca22ab6f18cdde4cb3f2c7e733ce02ac7d834eb22047c90ec53a65d84f86e
compact_legendre.tex           862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9
compact_width.tex              07cdfeda14ee650ae4d8b804cc7317f6046cd470542ec5edfb380b9c5f363988
compact_selected.tex           cce32506923384c8124e0a5f965591ad3ae67a51b62377098563eda9b4ff54fd
compact_initialization.tex     f2f801a714205d28930c9887ded1d4028350c5a11379ba6440f6f9747f8366c5
compact_feature_learning.tex   71f50a55613a3df12398d6226b8fe2380805f2f32082e134e7ab45846bfa4bd1
compact_nth.tex                38e50dee3b89a755e4efb719a8cf3396cd70f78a1cf163dbf0ff91076505a616
```

## Commands and retained outputs

Working directory for the build was the frozen `paper/` directory.

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../build compact.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../build compact.tex > ../build/latexmk.stdout.log 2>&1
pdftotext -f 1 -l 4 -layout ../build/compact.pdf ../build/frontmatter.txt
pdftotext -bbox-layout -f 1 -l 4 ../build/compact.pdf ../build/frontmatter.bbox.html
pdftotext -bbox -f 3 -l 4 ../build/compact.pdf ../build/pages3-4.bbox.html
pdftoppm -f 3 -l 3 -r 150 -png -singlefile ../build/compact.pdf ../build/frontmatter_p3
pdftoppm -f 4 -l 4 -r 150 -png -singlefile ../build/compact.pdf ../build/frontmatter_p4
pdftotext -f 36 -l 50 -bbox ../build/compact.pdf ../build/width.bbox.html
```

The primary command exited `0`. Full final TeX transcript is
`data/generated/headline_threefold_upgrade_20261011/paper_integration_v1/build/compact.log`;
the captured follow-up latexmk stdout is `build/latexmk.stdout.log` (reports
“Nothing to do” because the primary build had already completed). Supporting
text, bbox, and 150-dpi raster inspection artifacts are retained in that same
generated `build/` directory.

## Result

- **Build:** PASS. PDF created with 94 letter pages (612 x 792 pt).
  SHA-256: `a24dc0a5a532588d89883ebbbe4274748caf7d949b1d238f81d4cc037a320345`.
- **Cross-references/citations:** PASS. Final `compact.log` has no unresolved
  references or citations; latexmk's final target state was up to date.
- **Box diagnostics:** PASS. `compact.log` contains no `Overfull` or
  `Underfull` box message.

## Front matter and requested layout checks

The front-matter theorem begins on PDF page 3 (source `compact.tex:203`), and
the efficient-initialization proposition/table begins on PDF page 4 (source
`compact.tex:270-289`). Visual raster inspection and `pdftotext -bbox` show no
clipping or text overflow.

- PDF p.3 theorem band: rightmost extracted item was equation number `(8)` at
  `xMax=541.277 pt`, `yMin=471.669 pt`; it is visibly intact. The page-wide
  text maximum is `xMax=542.144 pt` (ordinary microtype margin protrusion),
  with no clipped content.
- PDF p.4 initialization-table band: rightmost extracted table-band glyph was
  at `xMax=539.945 pt`, `yMin=385.058 pt`, within the nominal 1-inch right
  margin boundary at 540 pt. The page-wide maximum was `xMax=542.137 pt`,
  again normal text protrusion rather than overflow; the raster is clean.
- New width section (`compact_width.tex`, all display starts inspected; PDF
  pp.36--50) and the setup/headline displays (`compact.tex:72-262`) have no
  TeX box warning. Width-section bbox maximum is `xMax=542.153 pt`, at most
  2.153 pt of microtype character protrusion beyond the nominal text boundary,
  with no display clipping or reported overflow.

## Warnings distinguished from build failures

There is one non-fatal, source-level warning:

```
Package amsmath Warning: Foreign command \atopwithdelims;
  \frac or \genfrac should be used instead
  on input line 703.
```

It points to `compact_initialization.tex:703`, where legacy `{j+d-1\choose
d-1}` syntax is used. It is not a build failure, reference/citation failure,
or a detected overflow. No prior frozen build log was supplied, so its
preexistence cannot be established from this packet; it is therefore recorded
as an inherited-source warning of undetermined baseline provenance, not as a
new failure from the compilation procedure.
