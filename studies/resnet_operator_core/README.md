# Core operator–Galerkin PDE experiment

This is a study record, not an established-library entry. Historical claims and
review labels below retain their original scope; consult the
[reconciled research map](../project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md)
for current qualifications and the [maintained library](../../docs/README.md)
for accepted self-contained presentations.

This directory is the working form of the direct finite neural-PDE study. The
outer release wrapper has been removed; the report, runners, source, protocol,
evidence, and audits are now visible together.

## Read first

- [`CONJECTURE_REPORT.md`](CONJECTURE_REPORT.md): current construction and
  project-level assessment.
- [`REPORT.md`](REPORT.md): completed direct experiment and limitations.
- [`theory/operator_galerkin_pde.md`](theory/operator_galerkin_pde.md): PDE
  derivation.
- [`results/processed/summary.json`](../../data/historical/studies/resnet_operator_core/results/processed/summary.json): compact
  machine-readable evidence.
- [`audits/final_adversarial_pde_audit.md`](audits/final_adversarial_pde_audit.md):
  final hostile audit.

## Quick check

From this directory, using the repository environment:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Run a small PDE:

```bash
PYTHONPATH=src python run_pde.py \
  --quadrature sobol --P 5 --N 8 --M 64 --R 32 \
  --duration 2 --dt 0.02 --sample-dt 0.04
```

The complete, expensive regeneration is:

```bash
WORKERS=8 PYTHON_BIN=python bash protocol/reproduce_full.sh
```

Raw canonical trajectories are intentionally not part of the original compact
release. The later locally generated trajectories are kept separately under
[`../rerun_2026-07-31`](../resnet_reproduction_2026_07_31).

Fresh runners and analyses now write to `data/generated/resnet_operator_core/`
under the repository root. Set `PDE_OPERATOR_OUTPUT_ROOT` to choose a distinct
run directory; for offline analysis only, `PDE_OPERATOR_INPUT_ROOT` may select
a different, read-only evidence directory. The full reproduction script uses
the same selected directory for its producers, restart, merges and consumers.
It does not implicitly mix in historical evidence or update historical seals.
Imports do not create output directories. These workflows require their own
optional scientific dependencies; they are not run by the core `make check`.

The `audits/` directory contains independent derivations, numerical probes,
statistical analyses, and hostile reviews. These are scientific notes and
diagnostics, not a second implementation to edit as the primary PDE.
