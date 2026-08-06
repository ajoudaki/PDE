# Mean-field derivative peeling

This study develops a layerwise conditional Gaussian calculus for
width-normalized contractions of neural-network derivatives. The active
directory has two maintained mathematical sources, one frozen historical
source, and one reproducible typeset report.

## Maintained sources

[`MEAN_FIELD_PEELING_THEORY.md`](MEAN_FIELD_PEELING_THEORY.md) is the
canonical theory document. It defines the admissible observable language,
conditional Wick--Stein elimination, equality partitions, global width
counting, deterministic covariance replacement, feature-learning jets, the
target theorem, the relation to Tensor Programs, and the open proof program.

[`MUP_TRAINING_CASE_STUDY.md`](MUP_TRAINING_CASE_STUDY.md) is the complete
calculation audit for one three-hidden-layer muP network. It contains the
backward-kernel peel, the one-step loss and hidden-Gram coefficients, the
two-step gradient correction, deep-linear checks, the general readout-scaled
backward template, and the explicit five-branch two-sample expansion.

The documents distinguish exact finite-width identities, mean-field results
under named probabilistic assumptions, formal nonlinear closures, restricted
audits, and open theorem targets.

## Historical source

[`archive/ORIGINAL_NOTES_AND_NTK_SAMPLE.md`](archive/ORIGINAL_NOTES_AND_NTK_SAMPLE.md)
preserves the original proposal and supplied NTK derivation. It is intentionally
not maintained as current mathematics; superseding corrections are stated in
the canonical theory and case study.

## Canonical report

[`MEAN_FIELD_PEELING_REPORT.pdf`](MEAN_FIELD_PEELING_REPORT.pdf) is the
current offline reading edition. It is generated from exactly the three
Markdown sources above using
[`MEAN_FIELD_PEELING_REPORT.tex`](MEAN_FIELD_PEELING_REPORT.tex), which owns
only typography, front matter, and inclusion order.

Build it with:

```bash
python3 build_report.py
```

The builder protects dollar-delimited mathematics for the workspace's legacy
LaTeX Markdown package, compiles with XeLaTeX in the ignored `build/`
directory, checks the PDF, and copies the final artifact to this directory.
Generated LaTeX, Markdown, cache, and auxiliary files are not maintained
sources.

## Source-of-truth rule

- Mathematical prose and formulas are edited only in the Markdown sources.
- Presentation is edited only in `MEAN_FIELD_PEELING_REPORT.tex`.
- `MEAN_FIELD_PEELING_REPORT.pdf` is regenerated; it is not edited directly.
- Historical claims are not silently rewritten in the archive.

The complete pre-restructure filesystem snapshot, including every earlier
report and build artifact from both document trees, is stored outside this
active directory at
`../../.backups/mean_field_peeling_pre_restructure_20260805T154408Z/` and is
protected by a SHA-256 manifest.
