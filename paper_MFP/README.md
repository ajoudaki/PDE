# Mean-Field Peeling

A standalone LaTeX paper and executable source bundle extracted from the
established Quarto book and maintained compiler.

- [Read the paper](main.pdf) or edit [main.tex](main.tex).
- [Compiler guide](code/MFP_CALCULUS.md): typed input, exact differentiation,
  returned Gaussian expectation graphs, symbolic geometry and labels.
- [Code inventory](code/README.md) and [source map](SOURCE_MAP.json).

The paper includes the complete fixed finite Gaussian derivative-program
theorem and proof, finite derivative rules, the initialization activation-moment
reduction, worked calculations, the compiler guide, and the bounded-program
foundation with its proofs. The examples cover matrix reuse, normalized
updates, singular queries, moving directions, a two-hidden-layer MLP parameter
derivative, and feature-kernel jets with symbolic geometry and labels.

Differentiation and represented-matrix expansion are exact at finite width.
Gaussian evaluation computes the infinite-width limit. All depth, data
dimensions, derivative order and update counts stay fixed in that limit;
the paper retains the theorem's other assumptions and scope restrictions.

## Build the paper

From this directory, with a TeX Live installation containing XeLaTeX,
BibTeX and `latexmk`:

```sh
make pdf
```

This produces `main.pdf`; intermediate files are in `build/`.
The delivered manuscript is native LaTeX: building it requires neither Quarto
nor the surrounding repository. `references.bib` contains the maintained
bibliographic entries; only cited entries appear in the paper.

## Run the compiler and examples

Use Python 3.10 or later and install the pinned dependency in your preferred
environment:

```sh
python -m pip install -r requirements.txt
make check
make examples
```

The guide provides five executable Python snippets and full API conventions.
To regenerate the generic, identity and quadratic kernel-jet variants:

```sh
mkdir -p build
PYTHONPATH=code python -B code/scripts/example_mfp_kernel_jets.py --activation all --output-dir build/kernel_jets_01
```

The output directory must not already exist. It receives the full formulas,
JSON graphs and a producer manifest. Generic Gaussian integrals remain
symbolic; the compiler performs no numerical integration.

## Source provenance

The manuscript was assembled from `docs/02-gaussian-reuse.qmd` (the Gaussian
preliminaries and complete promoted MFP section), `docs/12-three-sample-learning.qmd`
(the complete bounded-program foundation), `docs/notation.qmd`, and
`code/MFP_CALCULUS.md`. `SOURCE_MAP.json` records source hashes, exact extraction
ranges and editorial changes. Those changes supply standalone setup, adapt
headings and cross-references, and relocate run commands; they introduce no new
theorem or compiler behavior. All accompanying Python files and `requirements.txt`
are byte-identical copies of the maintained sources. The Markdown guide has
only the documented standalone path and wording adaptations.

This directory is a paper snapshot. The maintained authority remains `docs/`
and `code/` in the parent repository; future scientific changes should be
reconciled there through the repository workflow.

## Validation of this snapshot

On 2026-10-11, `make pdf` produced a 36-page PDF. All LaTeX references and
citations resolved, with no missing characters or overfull boxes. The PDF
passed `qpdf --check`, and representative theorem, proof, equation, table,
code and front-matter pages were visually inspected.

All 72 bundled tests, all five Python guide snippets and all three example
scripts passed, including all three kernel-jet activation variants. The
13 Python files and dependency pin matched the maintained sources before
and after execution. All 91 extracted display-math blocks and 94 source
anchors were preserved in the manuscript conversion. These are extraction,
build and implementation checks; the scientific results come from the
established book passages recorded in the source map.
