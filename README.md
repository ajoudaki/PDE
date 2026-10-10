# Deep nonlinear learning dynamics

The project asks whether actual deep, nonlinear feature learning admits a
well-defined population evolution that finite networks approximate jointly in
width and gradient-descent step—and what that evolution can explain about
optimization and, ultimately, generalization.

## Start here

This page is the repository gateway, not part of the established theorem book.
The book is **A Dynamical Theory of Deep Learning** by **Amir Joudaki**, subtitled
*Population Dynamics, Autonomous Approximation, and Nonlinear Learning*.
The Quarto book begins at `docs/index.qmd` and never refers back to research studies.

- [Established theory: reading guide](docs/index.qmd), with one
  [notation contract](docs/notation.qmd) and complete modular proofs.
- [Reusable code and API](code/README.md): finite all-depth network dynamics
  and exact rational Gaussian moments.
- [Study workflow and promotion gates](RESEARCH_WORKFLOW.md): automatically
  introduced to new tasks by [AGENTS.md](AGENTS.md), with study setup, independent
  audits, reusable-code review and reproducibility requirements.
- [Study catalogue](studies/README.md): exploratory work and historical sources.
- [Data policy](data/README.md): generated outputs and figures, separate from
  source and excluded from new Git commits.

The theory and code libraries stand on their own. Exploratory material can use
them, but the established library has no dependency in the reverse direction.
Historical labels and old review verdicts do not automatically confer current
established status.

The pre-Quarto edition is retained under `old_docs/` only for diagnosing a
specific migration ambiguity or broken reference. It is not the maintained
scientific authority and should not be used when the current book is clear.

Render the maintained book with Quarto from its project directory:

```sh
cd docs
quarto render --to html
quarto render --to pdf
quarto render --to latex
```

Exports are written to `data/generated/DTDL/`: `DTDL.pdf` for PDF and
`index.html` for the HTML book. The full title, subtitle and author remain
inside the book.

## Check the library

The tested baseline is Python 3.10.12 and NumPy 1.26.4. The minimal dependency
is recorded in [requirements.txt](requirements.txt).

```sh
python -m pip install -r requirements.txt
make check
```

This checks the library boundary and links, then runs the small deterministic
test suite. It does not run historical experiments, install optional scientific
packages, generate figures or claim a population theorem from a numerical test.
The [API guide](code/README.md) includes an example and the equivalent direct
Python command.

## Research state and preservation

The [reconciled research map](studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md)
retains the broader positive, negative, conditional and open results. It is a
research ledger, not an additional established theorem book.

The [refactor record](studies/repository_refactor_2026_09_09/PLAN.md) records
preservation, path changes, promotion decisions and validation. Rollback sources
were committed before reorganization: `25dfbf2` (repository source snapshot),
then `4753435` (recovered temporary and archived sources). `4e6ff81` is the
byte-verified layout change. Existing history has not been rewritten.

Tasks may contribute to several studies, and studies may have several contributing
tasks. Each study's README is its current record; additional ledgers and the helper
are optional. The workflow separates internal checks and reproducibility from
promotion, which requires independent relevance screening, fresh complete reviews,
canonical self-contained theory/reusable code, user approval of the reviewed
addition, and verification of the final integration.
