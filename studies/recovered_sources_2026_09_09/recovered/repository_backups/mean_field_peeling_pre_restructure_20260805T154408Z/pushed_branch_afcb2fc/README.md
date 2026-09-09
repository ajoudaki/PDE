# Mean-field derivative/Wick calculus

This directory contains the living research document for the mean-field
peeling program: a layerwise conditional Gaussian calculus for normalized
derivative contractions in wide neural networks.

## Offline consolidated report

[`MEAN_FIELD_PEELING_FULL_REPORT.pdf`](MEAN_FIELD_PEELING_FULL_REPORT.pdf) is
the typeset, 95-page offline compendium. It begins with a guided synthesis and
then includes the complete maintained program, the audited backward-kernel and
μP training case study, and the theorem/literature-positioning report. The
build source is [`MEAN_FIELD_PEELING_FULL_REPORT.tex`](MEAN_FIELD_PEELING_FULL_REPORT.tex);
`render_markdown_math.py` protects the canonical dollar-delimited mathematics
when compiling against the workspace's legacy Markdown-to-LaTeX package.

[`MEAN_FIELD_PEELING_SELF_CONTAINED_REPORT.pdf`](MEAN_FIELD_PEELING_SELF_CONTAINED_REPORT.pdf)
is the shorter, 32-page narrative version. Its maintained prose source is
[`MEAN_FIELD_PEELING_SELF_CONTAINED_REPORT.md`](MEAN_FIELD_PEELING_SELF_CONTAINED_REPORT.md),
with `render_mean_field_report.py` providing the lightweight PDF build path.

## Canonical living document

[`MEAN_FIELD_PEELING_PROGRAM.md`](MEAN_FIELD_PEELING_PROGRAM.md) is the
canonical maintained document. It contains:

- the original source notes, preserved separately from later revisions;
- the current formal interpretation of groups, scalarization, conditional
  Gaussian elimination, Wick–Stein branches, equality partitions, and width
  power counting;
- the programmatic theorem schema and its open proof obligations;
- the feature-learning and gradient-flow interface;
- a worked execution on the backward sensitivity kernel, including the first
  explicit Onsager correction and concentration argument;
- a dated change log for future updates.

## Consolidated μP training case study

[MUP_TRAINING_PEELING_CASE_STUDY.md](MUP_TRAINING_PEELING_CASE_STUDY.md)
is the self-contained, calculation-level companion to the canonical program.
For one fixed three-hidden-layer μP network it consolidates:

- the complete backward-sensitivity-kernel peel;
- the one-step output and loss coefficients at linear order;
- the hidden-Gram calculation through quadratic order, including the
  off-diagonal fluctuation branch;
- the exact two-step Euler/Hessian decomposition, a formal nonlinear
  multichannel recursion schema, and a verified deep-linear specialization;
- deep-linear audits and the resulting amendments to the general peeling
  program.

## Research-positioning report

[`TENSOR_PROGRAMS_CONTRAST_AND_THEOREM_FRAMING_REPORT.md`](TENSOR_PROGRAMS_CONTRAST_AND_THEOREM_FRAMING_REPORT.md)
records the current comparison with Tensor Programs, the distinction between
recursive limiting semantics and an explicit Gaussian normal form, a sharp
target theorem contract, feature-learning-jet framing, required nonclaims,
open proof obligations, and recommended names and paper titles. It is kept
separate from the canonical mathematical document because its novelty and
literature-positioning conclusions remain provisional.

## Earlier placeholder

[`MEAN_FIELD_DERIVATIVE_WICK_CALCULUS.tex`](MEAN_FIELD_DERIVATIVE_WICK_CALCULUS.tex)
is retained as the earlier minimal placeholder. It is not the current source
of truth and should not be expanded independently of the Markdown document.
