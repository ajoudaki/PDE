# Standalone promotion build preparation

Operational preparation only, checked on 2026-10-10. No scientific candidate
has been assembled, no complete render or test suite has run, no dependency has
been installed, and no maintained file or Git state has been changed.
The root coordinator must pass the placement gate before assembling the edition.

The observed environment and hashes of inspected build inputs are recorded in
`data/generated/mfp_gaussian_master_proof_20261010/promotion_build_prep/environment_20261010.json`.
The recorded checkout HEAD was `c17cb8c2e8d486ccc1d2b80e8cd173ba551145ae`.
Other tasks have unrelated working changes; none were read as research inputs or
modified. The Git index was empty at this check.

## Maintained build route

`docs/_quarto.yml` declares a book, 18 chapter/front-matter files, the bibliography
`references.bib`, and output directory `../data/generated/DTDL`. The output base
name is `DTDL`. Its declared formats are `html`, `pdf`, and `latex`.
The PDF format uses XeLaTeX, retains the TeX source, and explicitly disables
automatic LaTeX installation and TinyTeX. PDF and LaTeX use both
`pdf_breakable_tables.lua` and `print_code_links.lua`.

Use the Quarto executable provisioned by the coordinator and record its exact
version and checksum. From the isolated edition's `docs/`, the expected full-book
commands are:

```sh
quarto render --to html
quarto render --to pdf
quarto render --to latex
```

These commands follow the declared formats; their help/options and output
locations still need confirmation against the provisioned Quarto version.
Run one format at a time. Preserve and hash each complete output tree before the
next render because a later render may clean or replace prior output. The
default output tree stays inside the isolated edition, so no override of the
maintained configuration is necessary. Separate archival copies of generated
HTML, PDF and LaTeX deliverables may be retained beside that edition. Preserve
their complete `code/`, `docs/`, figure and support directories, not just the
top-level PDF or TeX file.

`code/tools/book_pdf/` is expressly an **archived Markdown exporter**. Its discovery
function reads `old_docs/`, requires Pandoc 3.6.4, and cannot validate the maintained
Quarto book. Do not execute it for this promotion. Its files may remain in a full
maintained-code snapshot because library tests can exercise the exporter using
synthetic fixtures; their presence does not authorize reading the archive.

## Minimal standalone layout

After placement approval, create a fresh, uniquely named directory below
`data/generated/mfp_gaussian_master_proof_20261010/`, for example
`promotion_validation_<run>/edition/`. Selectively copy source files; do not clone
or copy the checkout, create a worktree, or bring Git metadata into this directory.

The edition requires:

- `docs/`: the 18 current `.qmd` files, `references.bib`, `_quarto.yml`, both Lua
  filters, and `package_code_links.py`, with the reviewed candidate edits applied
  there after the placement gate. Preserve any future explicitly referenced
  source assets if the final frozen candidate introduces them.
- `code/`: maintained source, guides, tests, scripts, tools, and validation
  configurations, preserving relative paths. This is approximately 80 files and
  1.36 MB before any candidate change. Its guide links justify retaining the
  maintained code tree rather than copying only `code/pde/`.
- Root `requirements.txt` and `Makefile` for the declared environment and commands.
  Required review instructions and the frozen candidate manifest belong in the
  review packet outside `edition/`; they are not runtime dependencies.

Exclude `.git`, `studies`, `old_docs`, existing `data`, `.quarto`, `__pycache__`,
`.pytest_cache`, `node_modules`, `_book`, `_site`, hidden caches, bytecode and
previous render products. Reject symlinks leaving an allowed source tree;
no docs/code symlinks were found in the metadata inspection. Do not copy shell
environment files, local virtual environments, or repository history.
Create a new empty edition-local `data/` only for new validation outputs.

Capture a sorted source inventory and SHA-256 manifest before copying. Copy only
those explicit paths, verify copied bytes, then recheck the source inventory and
hashes so concurrent edits cannot silently mix source versions. Freeze the final
candidate manifest separately from the unmodified baseline. Preserve the old
frozen packet and use a new run directory if candidate inputs change.

## Linked code and source packaging

`docs/package_code_links.py` runs after rendering. It obtains the project/output
paths from Quarto's environment, resolves `code/` as the project's sibling, and
rewrites rendered HTML links beginning `../code/` to packaged `code/` resources.
It rejects missing or escaping linked code files.

The helper additionally copies the complete visible source trees of `docs/` and
`code/` into the output root and beside PDF/TeX outputs. The complete sibling
layout is needed because linked Markdown guides themselves link back to `docs/`
and into other code files. `print_code_links.lua` removes the initial `../` from
those code links for LaTeX/PDF, matching the adjacent packaged `code/` directory.
The helper does not itself validate every source-guide fragment or every
rendered link, so successful packaging is only one part of integration validation.

A lexical asset/link inventory found 30 distinct path-like local targets across
the `.qmd`, maintained Markdown guides and source HTML. All currently exist and
all lie inside `docs/` or `code/`. No Markdown image links, Quarto include/embed
directives, or source-HTML runtime resource URLs were found. The current source
docs directory contains no asset files apart from its config, bibliography,
filters and helper. These are inventory observations, not a completed link audit:
native cross-references, citations, HTML IDs, fragments and dynamic resources must
be checked in the rendered edition. A broad Markdown regex also matches some
math/code syntax; such non-path tokens were excluded from the path inventory.

There is one plain `mermaid` fence at `docs/outlook.qmd:69`. PDF conversion may
require browser tooling. The sole Python fence found in the book is a plain
`python` example at `docs/13-predictor-selection.qmd:900`, not a Quarto executable
chunk. No research execution is needed merely to render those examples.

## Installed tools and baseline blockers

- **Quarto is unavailable to this account through checked locations.** It is not
  on `PATH`; `/opt/quarto`, `/opt/quarto/bin/quarto`, `/usr/local/bin/quarto`,
  `/usr/local/share/quarto`, `/home/amir/.local/bin/quarto`, and
  `/home/codex-c/.local/bin/quarto` do not exist. No relevant top-level installation
  was found under readable `/opt`, `/usr/local/bin`, `/usr/share`, `/usr/lib`, or
  the current account's `.cache`/`.local`. `/home/amir/.cache` is unreadable, so its
  contents are unknown and must not be treated as an available dependency.
  The coordinator plans official Quarto provisioning into study-owned generated
  tooling, without changing system installations.
- Pandoc is absent from `PATH`. The maintained route should use the converter
  supplied with the chosen Quarto release; the archived exporter's separate
  Pandoc pin does not determine the maintained edition's converter version.
- There is no Chromium/Chrome executable on `PATH`. The existing
  `/usr/lib/chromium-browser` contains only `master_preferences`. Verify Quarto's
  Mermaid-to-PDF browser requirement and browser availability when provisioned.
- Present: Python 3.10.12, NumPy 1.26.4, psutil 5.9.0, Node 19.9.0,
  XeTeX 0.999993 / TeX Live 2022/dev/Debian, latexmk 4.76, qpdf 10.6.3,
  and pdftotext 22.02.0.
- `kpsewhich` found KOMA-Script, fontspec, unicode-math, mathtools, fvextra,
  longtable, booktabs, hyperref, adjustbox, etoolbox, newunicodechar, mathrsfs,
  xurl, bookmark, footnotehyper, tcolorbox and soul. Fontconfig found Latin Modern
  Roman/Math, TeX Gyre Pagella/Math, TeX Gyre Heros and FreeMono. This is a useful
  preflight, not proof that the provisioned Quarto template has no further needs.
- Torch, Matplotlib, Playwright, Beautiful Soup and lxml are absent from this
  Python environment. No Torch test is required for this change. The core package
  import succeeded with installed NumPy and did not import Torch.

The exact import check executed from the checkout was:

```sh
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B -c 'import sys, numpy, pde; print(pde.__file__, numpy.__version__, "torch" in sys.modules)'
```

It resolved the maintained `code/pde/__init__.py`, printed NumPy `1.26.4`, and
reported `False` for Torch in `sys.modules`. Repeat from the final isolated
edition to verify its own import path, including with the live checkout removed
from `PYTHONPATH` and the command's working directory.

## Bounded validation plan

Read the provisioned Quarto version/help first, then run complete HTML, PDF and
editable-LaTeX renders from the frozen edition. Retain exact commands, environment,
start/end times, exit status, logs and output hashes in the run directory. Use a
per-command wall limit, initially 900 seconds for each complete render, and do not
silently relaunch a timed-out process. Poll running processes so the coordinator
can report progress. This limit is a proposed operational bound, not a measured
book render time. Never invoke a training campaign or replace proof checking
with a successful render.

Set `PYTHONDONTWRITEBYTECODE=1`, all numerical thread counts to one, and `TMPDIR`
to a fresh directory in this run. Use edition-local `data/established/<run>/` for
test output. The maintained README additionally specifies
`H4_LAW_TEST_SCRATCH` and `H4_VALIDATION_TEST_SCRATCH` for observable tests.
The Makefile's broad test target lacks those explicit scratch settings, so invoke
tests with them set. Run the candidate's relevant deterministic tests and guide
examples first; inspect applicability before any broader suite. Full-suite runtime
and optional-dependency skip behavior were not tested in this preparation.
`code/tools/check_library.py` was outside the assigned read scope, so its standalone
requirements need coordinator inspection before running `make check`.

For each rendered format, reject unresolved references/citations, duplicate
identifiers, missing targets, malformed formal environments or an unintended
chapter/part structure. Check local HTML links and IDs with a real HTML parser
(Python's standard `html.parser` is available), including the packaged source
guide targets. Audit generated TeX labels/reference warnings and the preserved
theorem/proof structure. Run `qpdf --check DTDL.pdf` and `pdftotext` on the new PDF;
use its extraction and page inspection for layout/overflow checks. Retain and
validate the editable TeX and its dependent assets, rather than treating
`keep-tex: true` alone as completion of the separate LaTeX export requirement.

These checks complement, and cannot replace, the independent scientific and
integration reviews required by Part 2 of `RESEARCH_WORKFLOW.md`.

## Input scope and work performed

Read repository instructions, Makefile, requirements, Quarto configuration,
render/package helpers and archived-exporter source, plus operational portions of
the maintained code README. Inspected docs/code file and link/asset metadata;
executed version/availability queries, font/TeX-package queries and the core import
check. No scientific source retrieval outside the assigned maintained inputs,
other study reading, archived book reading, render, installation or Git mutation
was performed. This preparation is not a scientific or promotion review.
