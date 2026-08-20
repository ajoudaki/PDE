# Core operator–Galerkin PDE experiment

This directory is the working form of the direct finite neural-PDE study. The
outer release wrapper has been removed; the report, runners, source, protocol,
evidence, and audits are now visible together.

## Read first

- [`CONJECTURE_REPORT.md`](CONJECTURE_REPORT.md): current construction and
  project-level assessment.
- [`REPORT.md`](REPORT.md): completed direct experiment and limitations.
- [`theory/operator_galerkin_pde.md`](theory/operator_galerkin_pde.md): PDE
  derivation.
- [`results/processed/summary.json`](results/processed/summary.json): compact
  machine-readable evidence.
- [`audits/final_adversarial_pde_audit.md`](audits/final_adversarial_pde_audit.md):
  final hostile audit.

## Quick check

From this directory, using the repository environment:

```bash
PYTHONPATH=src ../../../../.venv/bin/python -m unittest discover -s tests -v
```

Run a small PDE:

```bash
PYTHONPATH=src ../../../../.venv/bin/python run_pde.py \
  --quadrature sobol --P 5 --N 8 --M 64 --R 32 \
  --duration 2 --dt 0.02 --sample-dt 0.04
```

The complete, expensive regeneration is:

```bash
WORKERS=8 PYTHON_BIN=../../../../.venv/bin/python bash protocol/reproduce_full.sh
```

Raw canonical trajectories are intentionally not part of the original compact
release. The later locally generated trajectories are kept separately under
[`../rerun_2026-07-31`](../rerun_2026-07-31/).

The `audits/` directory contains independent derivations, numerical probes,
statistical analyses, and hostile reviews. These are scientific notes and
diagnostics, not a second implementation to edit as the primary PDE.
