# HTML book: KaTeX renderer

2026-10-11. User-authorized presentation maintenance: switch the existing
Quarto HTML book to KaTeX without rewriting chapter sources or changing PDF
compilation. No scientific promotion or new research is involved.

## Change

`docs/_quarto.yml` selects `html-math-method: katex`. The HTML-only filter
`docs/html_katex_compat.lua` expresses the unsupported `psmallmatrix`
environment as `smallmatrix` inside scalable parentheses. It applies to the
environment generally, not one particular formula. All `.qmd` files remain
unchanged; PDF/LaTeX settings are unchanged.

## Validation

- Complete 18-page HTML render passed with Quarto 1.10.19.
- The exact library URL emitted by Quarto resolved to KaTeX 0.19.0.
  All 36,881 generated formula occurrences pass `renderToString` with
  `throwOnError: true`; nonfatal strict-mode warnings are excluded from this
  compatibility test. It is not a new proof audit.
- All 7,332 internal book-page links/fragments resolve.
- Hash comparison confirms all 18 chapter sources and the existing PDF are
  unchanged. All 18 generated HTML pages use KaTeX instead of MathJax.
- Terra's bounded Chromium check rendered 2,175 KaTeX nodes in Chapter 7
  and 3,175 in Chapter 10, with zero `.katex-error` nodes on either page.
  Viewport inspection of the NTH theorem and converted small matrix found
  no obvious clipping, overlap, or missing math. Screenshots, the check
  script, and report are in the run's `browser/` directory. These are two
  representative views, not an inspection of every page. Direct `file://`
  loading blocked Quarto navigation/tabset fetches through browser CORS;
  browse the book through its HTTP server for normal navigation.

Evidence: `data/generated/book_katex_20261011/`, including `render.log`,
`final_math_check.json`, `links.json`, and `preserve_hashes.json`.

The existing shared `docs/.quarto` cache has read-only SQLite sidecar files
from another account. The successful render therefore used a temporary
snapshot of the 25 book source/support files under this maintenance run's
`build/docs/`, with a symlink to maintained code for source-link packaging,
and its own cache. Only the snapshot's output directory was redirected to
the usual `data/generated/DTDL/`; the packaged `_quarto.yml` was restored to
the maintained configuration. No checkout was cloned and the shared cache
was not reset. This is an environment workaround, not part of the renderer.

Normal reproduction, with a writable Quarto project cache:

```sh
quarto render docs --to html --no-clean
```

To repeat the complete formula compatibility check, download the KaTeX JS
from the URL in the generated HTML, then run:

```sh
python3 studies/book_katex_20261011/check_math.py \
  data/generated/DTDL /path/to/katex.min.js /path/to/math-check.json
```

Quarto currently emits an `@latest` CDN URL. The recorded check certifies
the observed version, not future CDN updates. Browser-load speed has not
been benchmarked against MathJax; this change is the requested KaTeX trial.
