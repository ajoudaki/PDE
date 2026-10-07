# Compressing Global Dynamics of Deep Nonlinear Feature Learning

The working manuscript is [main.tex](main.tex), compiled to [main.pdf](main.pdf).
The 2026-10-07 revision replaces the former results and proof chain with the
integrated Dense, Legendre, Harmonic and Logarithmic results. It is a working
paper, not promotion into the maintained Quarto book.

## Reading and source structure

- `main.tex`: canonical network setup, motivation, existing numerical
  illustrations, discussion, and appendix guide.
- `results.tex`: forward size-to-error interfaces, inverse accuracy-to-storage
  prescriptions, dense variability bounds and the three compression guarantees.
- `methods.tex`: retained states, update rules and the core theoretical ideas.
- `costs.tex`: initialization, training and query work, with peak-memory and
  arithmetic-model qualifications kept separate.
- `integrated_appendix.tex`: complete parameter-explicit scientific statements,
  certificates and proofs, statically included in the paper.
- `references.bib`: literature bibliography.

Main-text constants depend only on activation and fixed depth. Error is
normalized by the fixed label RMS, confidence is fixed at 99%, and structural
parameters remain distinct. The appendix restores label factors, arbitrary
confidence, full label allowance, width gates, internal setup orders, and
finite-word evaluator/access costs. Its notation correspondence and a linked
page guide precede the detailed material.

The following distinctions are intentional:

- Legendre compresses the moving state but retains its fixed dense mixers.
- Harmonic tracks a coupled dense reference. Its explicit and implicit
  initializers have different setup costs; the latter samples a fresh latent
  reference rather than reading a supplied dense matrix cheaply.
- The Logarithmic decoder has finite-word storage and an independent-reference
  upper-certificate guarantee. No below-variability or width-independent query
  guarantee is claimed for it.
- Dense, Legendre and Harmonic count real coordinates; decoder word lengths
  and finite execution costs are stated separately.
- The dense lower bound is transient, not an endpoint result. The first three
  stochastic width thresholds remain qualitative; the decoder gate is explicit
  and conservative.

The scientific integration source is the owning study's
[RESULT.md](../studies/integrated_general_compression_20261004/RESULT.md).
The appendix contains that source's scientific Parts I–III, omitting only
conversion comments and historical provenance. LaTeX does not read any study
file. The deterministic study-local converter retains a line/math/reference
coverage manifest:

```bash
# From the repository root; regenerates the static appendix and checks it.
node studies/integrated_general_compression_20261004/paper_appendix_build.mjs --check
```

The revision's source hashes, scoped checks, build and visual-inspection record
are in [PAPER_REWRITE_CHECK.md](../studies/integrated_general_compression_20261004/PAPER_REWRITE_CHECK.md).
These are editorial and bounded mathematical integration checks, not formal
verification or a new independent review of every proof.

## Build

From `paper/`, use an existing output directory to keep auxiliary files out
of the manuscript folder:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/home/amir/Codes/PDE/data/generated/integrated_general_compression_20261004/paper_rewrite_KFCZPBuv \
  main.tex
```

The checked combined PDF is copied to `paper/main.pdf` for convenient reading.
The static TeX sources, bibliography and included figures suffice to compile
the manuscript; regenerating the appendix is not a build prerequisite.

## Existing illustrations

Only `figures/trajectory.pdf` and `figures/circles_deep.pdf` are included.
The first depicts recorded common-time Legendre predictions; the second
compares individually fitted endpoints. Captions preserve the architecture,
orders, query count and measurement qualifications. They are illustrations,
not evidence for Harmonic or Logarithmic compression, confidence rates,
continuous-time supremum bounds, or practical setup speedups.

This revision did not rerun training. Portable source bundles, capture
commands and renderers are documented in [scripts/README.md](scripts/README.md)
and [FIGURE_EXPERIMENT.md](FIGURE_EXPERIMENT.md). Other figures, old proof
modules, notes and trial manuscripts are preserved but are not inputs to
the rewritten paper. They are not alternative current theorem interfaces.
