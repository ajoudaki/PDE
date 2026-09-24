# Quarto 1.10.18 edge probes

Date: 2026-09-21. Scope: Quarto 1.10.18's documented/native behavior only;
no custom filters, runtime patches, or maintained-file edits. Source fixture:
`edge_features.qmd`. Generated evidence is under
`data/generated/quarto_capability_pilot_20260921/edge01/`.

## Findings

### 1. Subequations and separately numbered aligned lines

**PDF passes via raw LaTeX, but the same source does not provide the requested
automatic HTML behavior.** XeLaTeX rendered the parent subequation as `(1)`, its
children as `(1a)` and `(1b)`, and the next aligned lines as `(2)` and `(3)`;
all `\eqref` references resolved. See `edge_features.pdf`,
`edge_features_pdf.txt`, and the preserved `edge_features.tex`.

In HTML, Quarto preserved `subequations`, `align`, `\label`, and `\eqref` inside
MathJax source, but emitted the default MathJax 4 `tex-chtml.js` loader with no
`tex.tags: 'ams'` configuration. MathJax documents that automatic equation
numbering is off by default and requires `tags: 'ams'`; it documents `align`,
`\label`, and `\eqref`, but its complete AMS environment list does not include
`subequations`. Therefore:

- default Quarto HTML does not automatically number or resolve these raw-LaTeX
  line references;
- separately numbered `align` lines could require explicit MathJax configuration,
  but that was not pursued here;
- automatic `(1a)`, `(1b)` `subequations` are not supported by the loaded
  MathJax AMS environment set.

Quarto's documented equation cross-reference syntax labels one display block
with one trailing `{#eq-*}` identifier. It does not document line-level or
subequation labels. Thus no native, portable HTML/PDF solution for this complete
case was found.

### 2. Numbered Assumption

**A document-wide relabelling passes.** The documented
`crossref.thm-title: Assumption` and `crossref.thm-prefix: Assumption` settings
render `#thm-*` blocks and references as numbered Assumptions in both HTML and
PDF. The probe produced `Assumption 1` / `Assumption 2` in HTML and
`Assumption 1.1` / `Assumption 1.2` in PDF.

This changes every theorem in the document because the underlying type remains
`thm`; it does not add an independent `#asm-*` theorem environment. Quarto's
documented `crossref.custom` facility cannot supply that missing environment:
the schema permits only `kind: float`. Therefore a separately numbered theorem-
style Assumption coexisting with ordinary Theorems is not available through the
documented standard configuration tested here.

### 3. Shared theorem/lemma counter

**Unsupported by standard configuration in this runtime.** The same document
rendered the second theorem-like item and first lemma as `Assumption 2` and
`Lemma 1` in HTML, and `Assumption 1.2` and `Lemma 1.1` in PDF. The generated
LaTeX contains independent declarations:

```tex
\newtheorem{theorem}{Assumption}[section]
\newtheorem{lemma}{Lemma}[section]
```

The installed `document-crossref.yml` schema provides title, prefix, and label-
style settings for built-in theorem types, but no counter-sharing setting. The
runtime filter independently emits `\newtheorem{...}[section]` (or `[chapter]`)
for each active theorem type. No standard configuration for a shared
theorem/lemma sequence was found.

## Documentation and runtime evidence

- Quarto cross-reference guide:
  <https://quarto.org/docs/authoring/cross-references>
- Quarto cross-reference options:
  <https://quarto.org/docs/reference/metadata/crossref.html>
- MathJax 4 automatic numbering:
  <https://docs.mathjax.org/en/v4.0/input/tex/eqnumbers.html>
- MathJax 4 AMS environments:
  <https://docs.mathjax.org/en/v4.0/input/tex/extensions/ams.html>
- Installed schema:
  `runtime/quarto-1.10.18/share/schema/document-crossref.yml`
- Installed cross-reference filter:
  `runtime/quarto-1.10.18/share/filters/crossref/crossref.lua`, especially the
  theorem declarations around lines 5992--6021 and custom-float initialization
  around lines 4816--4930.

## Execution record

The final HTML and PDF were rendered from the identical source hash
`e234bc9a5096b072c1e6d62bbbe0e2d3bcdd92325060356e121b24a7a708c7d4`
with the portable Quarto 1.10.18 binary. Both final renders used
`XDG_CACHE_HOME` and `XDG_CONFIG_HOME` below `edge01/`; PDF metadata set
`latex-auto-install: false` and `latex-tinytex: false`. `qpdf --check` passed.

One intermediate PDF attempt combined `crossref.chapters: true` with the
standalone article class and failed because that class has no `chapter` counter.
Removing the inapplicable book-only option produced the final successful PDF.
No package was installed. Four commands reached the render pipeline: two HTML
successes, that diagnostic PDF failure, and the final PDF success. An earlier
CLI invocation was rejected during flag validation before rendering because
`--output-dir` is project-only.
