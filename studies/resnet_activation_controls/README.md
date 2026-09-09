# Activation-linearity smoking-gun experiment

This is a study record, not an established-library entry. Historical claims and
review labels below retain their original scope; consult the
[reconciled research map](../project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md)
for current qualifications and the [maintained library](../../docs/README.md)
for accepted self-contained presentations.

This is the frozen, sparse falsification experiment for the question: does
the fixed \(P=5\) neural PDE follow activation-specific nonlinear feature
dynamics, or is it merely reproducing a deep-linear effect?

The completed preregistered verdict is `identity_only`: exact identity
dynamics are decisively rejected by the Gram and output trajectories, but the
gain-matched L2 control remains within the study's 5% Gram tolerance. See
`ACTIVATION_LINEARITY_SMOKING_GUN_REPORT.md` for the numerical result and its
limitations.

The current migration does not renew the historical input freeze. Inspect it
read-only from this directory with:

```bash
python run_experiment.py all --historical-status
```

The retained complete \(T=8\) interface is:

```bash
python run_experiment.py all
```

It is not currently a clean-checkout regeneration promise: without a live
input manifest the runner refuses to recreate the historical freeze. The
stages remain independently resumable only with valid live authorization:

```bash
python run_experiment.py validate
python run_experiment.py pde-primary
python run_experiment.py pde-scramble
python run_experiment.py pde-n32
python run_experiment.py seal-pde
python run_experiment.py dense-primary
python run_experiment.py dense-depth
python run_experiment.py dense-width
python run_experiment.py seal-dense
python run_experiment.py analyze
```

Useful resource controls are `--parallel-pde`, `--parallel-dense`, and
`--dense-workers`. Defaults are 3, 1, and 4 respectively.

The fixed inventory is:

- PDE primary: `C0,C1,C2,C4,L2`, \(P=5,N=16,M=81,R=128\), hybrid
  quadrature, seed `20260723`.
- PDE scramble: `C0,C2,C4,L2` with independent seed `20260724`.
- PDE depth control: `C0,C2` at \(N=32\).
- Dense primary: all five cases at \(n=128,L=32,S=16\), seeds
  `61000..61015`.
- Dense depth control: `C0,C2` at \(n=128,L=64,S=8\), seeds
  `61000..61007`.
- Dense width diagnostic: `C0,C2` at \(n=256,L=32,S=4\), seeds
  `63000..63003`.

Common seed IDs pair activations within each tier. The same numeric seed
across \(L=32\) and \(L=64\) is not a nested parameter coupling, because the
different number of weight draws changes the later RNG position.

`validate` runs the activation/formula, finite-difference, dense-gradient,
PDE-kernel, protocol/CLI-parity, and safe-resume tests. It then creates
`data/generated/resnet_activation_controls/results/FROZEN_INPUTS.json`
(repository-relative), cryptographically binding the audited parent
release, exact source lineage, protocol, cases, runner, analyzer, tests, and
dependency lock before any trajectory can run. It refuses to regenerate this
manifest when only the historical freeze exists. The audited parent release is
`data/historical/studies/resnet_activation_controls/parent/dense_mup_pde_generalization_repro.zip`;
its required
SHA-256 is
`8e66e442fb322380acce93a0b59da4851a319401a087bb4b3e3146ed0c1de003`.

Resume is deliberately strict. An archive is reused only if exactly one file
has matching embedded metadata, exact shapes/time grid/seeds, and finite
arrays. Changed or duplicate archives and `.partial` remnants stop the run.
Dense commands cannot start until the exact 11-file PDE inventory is sealed;
analysis cannot start until the exact 9-file dense inventory is sealed.

Fresh results use repository `data/generated/resnet_activation_controls/results/`,
with `PDE_STAGE_SEAL.json`, `DENSE_STAGE_SEAL.json`, and `processed/` below it.
Retained evidence and seals are under
`data/historical/studies/resnet_activation_controls/evidence/`; they are not
current execution authorization. `make_figures.py` consumes fresh processed
results by default; `--historical-inputs` explicitly selects retained evidence
while still writing fresh figures. Old source hashes and seals are not renewed.

The sole confirmatory nonlinear case is `C2`. `C4` is descriptive
dose-response evidence. The horizon is fixed at \(T=8\); if the preregistered
plateau check fails, plateau and loss-clock claims are reported unresolved
without adaptively extending the run.
