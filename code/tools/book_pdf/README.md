# Book PDF exporter

This optional publishing tool produces the reading-edition PDF from the current
book without editing its Markdown, running repository research code, or changing
Git state. It is separate from the numerical library and its required dependencies.

## Run

From the repository root:

```sh
./code/tools/book_pdf/build-pdf.sh
./code/tools/book_pdf/build-pdf.sh /tmp/my-book.pdf
./code/tools/book_pdf/build-pdf.sh --keep-build
```

The default output is `/tmp/PDE-book-latest.pdf`. Choose a persistent destination
outside the repository if you want to keep it longer. A neighboring `.build.json`
receipt records source hashes, coverage, and rendering checks. Output paths inside
the source repository are rejected, keeping generated artifacts out of the book
and code. A previously successful PDF is replaced only after the new PDF passes
the rendering checks.

The script locates the repository from its own location, so it also works when
called by absolute path from another directory. `--repo /path/to/PDE` overrides
the source checkout. Keep the shell script, Python helpers, and layout together.

## Dependencies

Python 3.9+, Pandoc **3.6.4**, XeLaTeX, `qpdf`, and `pdftotext` are required.
The TeX installation must include KOMA-Script, `unicode-math`, `adjustbox`,
`fvextra`, `mathrsfs`, `xurl`, `etoolbox`, and the TeX Gyre Pagella (including
Math), TeX Gyre Heros, and DejaVu Sans Mono fonts. This exporter is tested on
Linux. Its optional archived Pandoc executable is specifically Linux x86-64.

Pandoc may be installed on `PATH`. Alternatively, provide its unmodified official
Linux x86-64 release archive with `--pandoc-archive /path/to/pandoc.tar.gz`.
If Pandoc is absent from `PATH`, the exporter also checks this user-local cache:

```text
~/.cache/pde-book-pdf/pandoc-3.6.4-linux-amd64.tar.gz
```

The archive comes from the [official Pandoc 3.6.4 release](https://github.com/jgm/pandoc/releases/tag/3.6.4).
Its download URL and required SHA-256 are:

```text
https://github.com/jgm/pandoc/releases/download/3.6.4/pandoc-3.6.4-linux-amd64.tar.gz
5def6e1ff535e397becce292ee97767a947306150b9fb1488003b67ac3417c5e
```

No converter binary, archive, PDF, or generated data belongs in Git. The exporter
never downloads or installs dependencies automatically. It verifies an archive
before extracting its one executable into a fresh private build directory.
An installed Pandoc must report the pinned version because the renderer consumes
its JSON syntax tree. An explicit archive overrides the installed converter.

## Coverage and layout

The exporter includes the full `docs/README.md`, `docs/NOTATION.md` when present,
all Markdown files under `docs/`, and `code/README.md` when present as an appendix.
Chapters follow the order of links in the introduction; unlisted Markdown files
are appended and announced, rather than silently omitted.

A private `/tmp` snapshot isolates the build from the maintained files. Sources
are checked for edits during capture and after compilation. If they change while
the PDF is typeset, the exporter reports that it represents the captured snapshot;
it never locks, edits, or reverts the book. Successful temporary builds are removed
unless `--keep-build` is supplied. Failed builds retain their printed diagnostic
directory.

The reading edition uses A4 pages, Pagella body/math fonts, restrained blue
headings, linked contents and bookmarks, and retained source equation tags.
PDF-only transformations namespace cross-references, wrap code/tables, fit wide
equations, reflow long literal integer tuples, and group two existing
matrix-transpose expressions that otherwise produce invalid double superscripts.
They act on the copy only, retaining the integer tuple's values and order.

Checks cover unresolved local links, LaTeX errors, missing glyphs, overfull boxes,
unsettled references, PDF structural validity, off-page extracted text, and a
minimum 60% equation scale. These are rendering checks, not proof audits or a
guarantee against every possible visual defect. Plain-text and code-formatted
mathematics remain literal. Unsupported future image dependencies, custom macros,
or unusually wide equations may require an export-only adjustment; the tool does
not silently omit unresolved book links or repair original documents.

XeLaTeX runs with shell execution disabled. Only use the exporter with trusted
book sources; this is not a sandbox for hostile Markdown or TeX.

## Tests

The exporter safety tests use Python's standard library and temporary fixtures;
they need neither Pandoc nor TeX and do not run research experiments:

```sh
python3 -B code/tests/test_book_exporter.py
```

They are also discovered by the repository's existing test command. A real full
book build exercises the optional external typesetting dependencies separately.
