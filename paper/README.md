# Compressing Global Dynamics of Deep Nonlinear Feature Learning

The working manuscript is [main.tex](main.tex), compiled to [main.pdf](main.pdf).
The 2026-10-07 revision replaces the former results and proof chain with the
integrated Dense, Legendre, Harmonic and Logarithmic results. It is a working
paper, not promotion into the maintained Quarto book.

## Reading and source structure

- `main.tex`: canonical network setup, motivation, existing numerical
  illustrations, discussion, and appendix guide.
- `results.tex`: one prescribed-size compression theorem for all three methods,
  actual dense variability and the theoretical consequences.
- `methods.tex`: retained states, update rules and the core theoretical ideas.
- `costs.tex`: initialization, training and query work, with peak-memory and
  arithmetic-model qualifications kept separate.
- `integrated_appendix.tex`: complete parameter-explicit scientific statements,
  certificates and proofs, statically included in the paper.
- `references.bib`: literature bibliography.

Main-text constants depend only on activation and fixed depth. Error is
absolute. The benchmark is the 99.99% quantile of actual independent-dense
discrepancy, with compression success at least 99%; structural parameters
remain distinct. The appendix retains label factors, arbitrary
confidence, full label allowance, width gates, internal setup orders, and
finite-word evaluator/access costs. Its notation correspondence and a linked
page guide precede the detailed material.

The following distinctions are intentional:

- Legendre compresses the moving state but retains its fixed dense mixers.
- Harmonic tracks a coupled dense reference. Its explicit and implicit
  initializers have different setup costs; the latter samples a fresh latent
  reference rather than reading a supplied dense matrix cheaply.
- The Logarithmic decoder has finite-word storage and the same constant-factor
  actual-variability guarantee against an independent reference. Its explicit
  finite-width statement has an additional numerical remainder; factor three
  follows eventually for nonzero labels and at least two samples.
  No width-independent query guarantee is claimed for it.
- Dense, Legendre and Harmonic count real coordinates; decoder word lengths
  and finite execution costs are stated separately.
- The dense lower bound is transient, not an endpoint result. The first three
  stochastic width thresholds remain qualitative. The decoder's additive and
  analytic absolute certificates have an explicit conservative gate; its purely
  multiplicative intrinsic comparison also uses the lower bound's eventual onset.

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

The rollback version is commit 2c27cbc; its frozen checks remain in
[PAPER_REWRITE_CHECK.md](../studies/integrated_general_compression_20261004/PAPER_REWRITE_CHECK.md).
The new intrinsic-benchmark proof and scoped audit are in the owning study;
the current build record is
[PAPER_INTRINSIC_REVISION_CHECK.md](../studies/integrated_general_compression_20261004/PAPER_INTRINSIC_REVISION_CHECK.md).
These are editorial and bounded mathematical integration checks, not formal
verification or a new independent review of every proof.

## Build

From `paper/`, use an existing output directory to keep auxiliary files out
of the manuscript folder:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/home/amir/Codes/PDE/data/generated/integrated_general_compression_20261004/paper_intrinsic_D3pc1mpR \
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
