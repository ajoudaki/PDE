# Mean-field peeling

Mean-field peeling is a proposed general calculus for reducing fixed-order,
width-normalized neural-network derivative contractions to explicit Gaussian
normal form by layerwise conditional Wick--Stein elimination. Its local
Gaussian identities are exact, its detailed muP examples are audited under
named mean-field assumptions, and its one-sample quadratic specialization has
an exact decorated-forest compiler with accepted coefficients through
derivative order eleven. The general observable-grammar theorem and
depth-linear finite-state closure remain open.

| Result | Status |
|---|---|
| Conditional Gaussian laws and Wick--Stein identities | Exact |
| Fixed-network backward and training calculations | Audited under stated assumptions; some higher nonlinear closures remain formal |
| Quadratic decorated-forest reduction | Exact special-case reduction |
| Quadratic derivatives through order eleven | Accepted exact computational certificates |
| General Gaussian-normal-form theorem | Open |
| Depth-independent finite-state closure and shared $O(L)$ DAG | Open |
| Full quadratic order-thirteen coefficient | Open |

## Maintained sources

[`CURRENT_RESEARCH_STATE.md`](CURRENT_RESEARCH_STATE.md) is the
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

[`quadratic_compiler/`](quadratic_compiler/) contains the exact special-case
graph rewrites, connected recurrence, Wick-sector engines, checked arithmetic,
certificates, provenance, and rejected acceleration attempts. It is specific
to the one-sample, two-hidden-layer quadratic model; it is not a generic MLP
compiler.

The downstream
[`../stieltjes_conjecture/`](../stieltjes_conjecture/) study consumes the
quadratic feature derivatives but owns the series inversion, moment problem,
Hankel certificates, rational reconstruction, and numerical conjecture tests.

## Historical source

[`archive/ORIGINAL_NOTES_AND_NTK_SAMPLE.md`](archive/ORIGINAL_NOTES_AND_NTK_SAMPLE.md)
preserves the original proposal and supplied NTK derivation. It is intentionally
not maintained as current mathematics; superseding corrections are stated in
the canonical theory and case study.

## Canonical report

[`report/MEAN_FIELD_PEELING_REPORT.pdf`](report/MEAN_FIELD_PEELING_REPORT.pdf) is the
current offline reading edition. It is generated from the general theory,
detailed training case, and frozen historical source using
[`report/MEAN_FIELD_PEELING_REPORT.tex`](report/MEAN_FIELD_PEELING_REPORT.tex), which owns
only typography, front matter, and inclusion order.

Build it with:

```bash
python3 report/build_report.py
```

The builder protects dollar-delimited mathematics for the workspace's legacy
LaTeX Markdown package, compiles with XeLaTeX in the ignored `build/`
directory, checks the PDF, and copies the final artifact to `report/`.
Generated LaTeX, Markdown, cache, and auxiliary files are not maintained
sources.

## Source-of-truth rule

- Mathematical prose and formulas are edited only in the Markdown sources.
- Presentation is edited only in `report/MEAN_FIELD_PEELING_REPORT.tex`.
- `report/MEAN_FIELD_PEELING_REPORT.pdf` is regenerated; it is not edited directly.
- Historical claims are not silently rewritten in the archive.
- Compiler outputs are accepted only at the claim level recorded by their
  adjacent audit; passing regressions do not upgrade a restricted algorithm
  into the general theorem.

The complete pre-restructure filesystem snapshot, including every earlier
report and build artifact from both document trees, is stored outside this
active directory at
`../../.backups/mean_field_peeling_pre_restructure_20260805T154408Z/` and is
protected by a SHA-256 manifest.
