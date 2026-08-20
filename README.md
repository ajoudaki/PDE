# Finite causal neural PDE research

This repository studies whether dense nonlinear feature-learning dynamics can
be represented by a finite, autonomous, causal PDE state.

The dated project-wide baseline is
[`FINITE_CAUSAL_NEURAL_PDE_MASTER_MONOGRAPH_v2.2_2026-07-31.md`](FINITE_CAUSAL_NEURAL_PDE_MASTER_MONOGRAPH_v2.2_2026-07-31.md).
It records the state on 31 July 2026 and does not contain later MFP or
Stieltjes work. The later cross-study orientation is
[`UNIFIED_FINITE_CAUSAL_NEURAL_PDE_SYNTHESIS_2026-08-19.md`](UNIFIED_FINITE_CAUSAL_NEURAL_PDE_SYNTHESIS_2026-08-19.md).
Within each active program, that program's maintained
`CURRENT_RESEARCH_STATE.md` or README-designated current report takes
precedence over the older monograph and historical reports.

## Research map

The repository is organized by scientific question, not by software artifact
type:

| Program | Question |
|---|---|
| [`studies/quadratic_nonclosure`](studies/quadratic_nonclosure/) | What fails in the prescribed quadratic Taylor/Wick closure? |
| [`studies/mean_field_peeling`](studies/mean_field_peeling/) | How can fixed-order μP derivative observables be peeled layer by layer into explicit Gaussian calculations, and which parts are proved or compiled exactly? |
| [`studies/stieltjes_conjecture`](studies/stieltjes_conjecture/) | Does the quadratic-network output kernel define a Stieltjes moment sequence and a convergent rational ODE hierarchy? |
| [`studies/resnet_pde`](studies/resnet_pde/) | How much of the fully connected residual-network dynamics is captured by finite response structure and an explicit finite-source PDE, and what still blocks convergence and dense-limit identification? |

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
  environment used for the 31 July numerical execution audit.

There is deliberately no repository-wide `src`, `tests`, `tools`, `releases`,
or `runs` layer. Tests remain beside the experiment they validate, and new
reproductions remain beside the study they reproduce.
