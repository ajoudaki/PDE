# Finite causal neural PDE research

This repository studies whether dense nonlinear feature-learning dynamics can
be represented by a finite, autonomous, causal PDE state.

The authoritative synthesis is
[`FINITE_CAUSAL_NEURAL_PDE_MASTER_MONOGRAPH_v2.1_2026-07-28.md`](FINITE_CAUSAL_NEURAL_PDE_MASTER_MONOGRAPH_v2.1_2026-07-28.md).
Its claim ledger takes precedence over the older reports preserved here.

## Research map

The repository is organized by scientific question, not by software artifact
type:

| Program | Question |
|---|---|
| [`studies/quadratic_nonclosure`](studies/quadratic_nonclosure/) | What fails in the prescribed quadratic Taylor/Wick closure? |
| [`studies/dense_response`](studies/dense_response/) | How far can a finite-matrix chronological response hierarchy go? |
| [`studies/operator_pde`](studies/operator_pde/) | Does the explicit low-order operator–Galerkin PDE reproduce dense dynamics and transfer across controls? |
| [`studies/pde_convergence`](studies/pde_convergence/) | Can the finite-cutoff PDE hierarchy be connected to an arbitrary-accuracy theorem? |

Each program keeps its reports, code, protocols, and evidence together.
Sequential investigations are arranged as phases only when chronology is
scientifically important. Release-only wrappers and exact historical layouts
live in the archive rather than in the active research tree.

## Other material

- [`archive/bundles`](archive/bundles/) contains the original immutable ZIP
  releases.
- [`archive/earlier_documents`](archive/earlier_documents/) contains superseded
  project-wide syntheses and reports.
- [`requirements-lock.txt`](requirements-lock.txt) records the common Python
  environment used for the recent operator-PDE work.

There is deliberately no repository-wide `src`, `tests`, `tools`, `releases`,
or `runs` layer. Tests remain beside the experiment they validate, and new
reproductions remain beside the study they reproduce.
