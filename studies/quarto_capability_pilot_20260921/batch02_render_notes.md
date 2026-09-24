# Batch 02 render tooling

Final study tooling files are `render_linear.py`,
`check_linear_render.py`, `migration_render_tests.py`,
`migration_quarto.yml`, and `pdf_breakable_tables.lua`.
`migration_render_rules.md` is the governing bounded print amendment.

`render_linear.py` verifies accepted candidate hashes from the immutable
before-progress record, requires a same-source contiguous prefix from line 1,
and byte-concatenates accepted pieces plus the current candidate. A run freezes
all component inputs, `assembled.qmd`, `assembled_source.json`, the print rules,
the Lua filter, and the small browser launcher. `check_linear_render.py` checks
the assembled source and the union of the before-registry and current targets;
its packet-001 fallback remains. The focused assembly and prior reference-gate
suite passes all 14 tests.

Native Mermaid PNG production uses pinned Quarto 1.10.18 and the retained
Chrome Headless Shell at
`data/generated/quarto_capability_pilot_20260921/batch02-render-tooling/browser/chrome-headless-shell-linux64/chrome-headless-shell`.
The generated launcher `browser/chrome-padded-viewport` adds only
`--hide-scrollbars --window-size=1600,1600`; this corrects the observed SVG
capture clipping. Future diagrams still require visual inspection; the viewport
setting is not a guarantee for arbitrarily large diagrams. The Lua filter removes
Quarto's inferred Mermaid image width and height in LaTeX, causing Pandoc's
native `\pandocbounded{\includegraphics[keepaspectratio]{...}}` to fit both page
dimensions while preserving aspect ratio. HTML remains native Mermaid.

The launcher is executable and has exactly these contents, so it can be recreated
next to the retained `chrome-headless-shell-linux64/` directory:

```sh
#!/bin/sh
exec "$(dirname "$0")/chrome-headless-shell-linux64/chrome-headless-shell" --hide-scrollbars --window-size=1600,1600 "$@"
```

Quarto's local browser debugging port must be permitted during rendering. A
sandboxed run that denies that port cannot produce the diagram; use the same
authorized local-render permission as the accepted runs.

For LaTeX/PDF only, the same small filter converts simple, uncaptioned,
unlabelled, unspanned two-column tables into ordered breakable row blocks. Each
cell repeats its column header in bold, so column identity stays explicit.
Cell blocks retain links, math and inline/block content. Three-column tables and
other shapes remain ordinary tables. Captioned, labelled, spanning, multi-header,
row-header, table-foot and inconsistent two-column structures are reported and
left unchanged. Markdown source and HTML tables are untouched.

Final packet-002 evidence is
`data/generated/quarto_capability_pilot_20260921/batch02-render-tooling/linear002-render-repaired-v5/`.
HTML, PDF and LaTeX exited zero; the partial-reference gate passed. The complete
Mermaid raster is 3664 by 3992 pixels, exported TeX uses `\pandocbounded`, and
the inspected PDF page is `layout-pages/page-08.png`.

The final provisional 001+002+003 layout preview is
`data/generated/quarto_capability_pilot_20260921/batch02-render-tooling/PROVISIONAL-linear003-preview-repaired-v2/`.
It is an exact 60,764-byte concatenation and creates no acceptance, progress or
registry receipt. HTML, PDF and LaTeX exited zero. The prior page-tall chapter
rows are breakable blocks; the three-column milestone table remains a table.

Earlier evidence is preserved. The original packet-002 and provisional-003
renders show the page overflow. Repair v1 did not affect Quarto's cell-local
Mermaid dimensions; v2 used a hard-coded width and was superseded; v3 used the
general page bound but exposed raster-edge clipping. The bounded native-SVG
diagnostic in v4 failed because Quarto emitted a malformed multi-line Mermaid
SVG for `rsvg-convert`; it is not part of the final recipe. The browser-flag
probe established the source-independent capture fix used in v5.
