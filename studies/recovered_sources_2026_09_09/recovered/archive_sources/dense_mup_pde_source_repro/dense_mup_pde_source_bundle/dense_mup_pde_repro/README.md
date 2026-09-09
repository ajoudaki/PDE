# Dense Euclidean \(\mu\)P: genuine neural-PDE simulation

> **Compact-edition note.** This directory is distributed inside a
> source-first bundle without raw `.npz` trajectories. Read the bundle-level
> `../README.md` first. The commands below regenerate the omitted arrays.
> Run `../verify_source_only.sh` on the compact release and
> `../verify_reproduced_core.sh` after the full protocol.

This bundle directly integrates a width-independent neural PDE for the
canonical fully dense residual-tanh network with ordinary Euclidean
\(\mu\)P training.

The central result is no longer a finite-matrix \(q/r\) surrogate. The
primary PDE state contains a conditional law of finitely many Hermite row
coefficients, represented by numerical characteristics. It contains no
network width \(n\), no \(n\times n\) matrix, and no reference trajectory in
its velocity.

Read these first:

- `REPORT.md`: scientific result and limitations.
- `theory/operator_galerkin_pde.md`: complete PDE derivation.
- `src/dense_pde/operator_galerkin.py`: PDE and characteristic solver.
- `src/dense_reference/core.py`: self-contained exact dense-network reference.
- `results/processed/summary.json`: machine-readable metrics.
- `protocol/reproduce_full.sh`: regenerate the full main evidence grid.
- `protocol/verify_bundle.sh`: explicit `snapshot`, `source`, and `evidence`
  verification modes.
- the archive-level `agent_outputs/`: independent derivation, numerical,
  statistical, and hostile code audits.

## Quick verification

From this directory:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-lock.txt
PYTHONPATH=src python -m unittest discover -s tests -v
```

`requirements-lock.txt` records the exact top-level versions used for the
release; `requirements.txt` gives compatible lower bounds.

Run a small genuine PDE:

```bash
PYTHONPATH=src python run_pde.py \
  --quadrature sobol --P 5 --N 8 --M 64 --R 32 \
  --duration 2 --dt 0.02 --sample-dt 0.04
```

Run the primary PDE:

```bash
PYTHONPATH=src python run_pde.py \
  --quadrature sobol --P 5 --N 16 --M 256 --R 128 \
  --seed 20260723 --duration 8 --dt 0.02 --sample-dt 0.04
```

Continue the primary PDE through the plateau:

```bash
PYTHONPATH=src python run_pde.py \
  --quadrature sobol --P 5 --N 16 --M 256 --R 128 \
  --seed 20260723 --duration 24 --dt 0.1 --sample-dt 0.1 \
  --restart-from \
  results/raw/pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz
```

The restart loader hashes the static PDE compiler and every quadrature
array. A same-shaped state from another seed or compiler is rejected.

Generate a dense reference ensemble:

```bash
PYTHONPATH=src python run_exact_reference.py \
  --n 256 --depth 32 --seeds 32 --seed-start 6000 \
  --workers 8 --duration 8 --dt 0.02 --sample-dt 0.04
```

Dense references are used only after PDE integration. The PDE code never
loads them.

Regenerate processed tables and figures:

```bash
MPLCONFIGDIR=/tmp/matplotlib-cache \
MPLBACKEND=Agg PYTHONPATH=src python analyze.py
```

After regenerating the raw arrays, run all algebraic and core scientific
checks:

```bash
bash protocol/verify_bundle.sh evidence
```

Regenerate the entire primary PDE/refinement/reference protocol:

```bash
WORKERS=8 bash protocol/reproduce_full.sh
```

The latter is intentionally expensive. It recomputes the primary PDE,
the \(t=8\to32\) autonomous continuation, every reported refinement, all
dense reference ensembles, the paired-\(W\) homogenization diagnostic, and
the independent statistical audit. The project has no source-code
dependency on the earlier finite-matrix response bundle.

## Scientific boundary

The experiment establishes that the explicit operator-Galerkin equation is
a genuine, internally consistent finite neural PDE, numerically resolved at
the stated \(P,N,M,R\), whose curves closely track dense-network ensemble
dynamics.

It does not prove the PDE is the exact ordered \(n\to\infty\), then
\(L\to\infty\) limit. That identification still requires a trained
iid-depth homogenization theorem and Hermite-tail control. It also does not
simulate the earlier response-word \(K/J/N\) compiler, because that note
never emitted a concrete drift.

The preregistered held-out-reference audit reaches a deliberately narrower
verdict. With 128 independent \(n=256,L=32\) networks, the \(P=5\) PDE's
Gram-increment gap is \(7.243\times10^{-3}\), or 1.14% of the nonlazy
feature motion, and is statistically resolved relative to this *finite*
reference (pooled bootstrap \(p\approx0.0030\)). Thus the curves are close
but not indistinguishable.

Two additional held-out exact-network blocks test the limit axes without
fitting the PDE. The \(n=256\to512\) width Cauchy gap at \(L=32\) is
\(9.350\times10^{-3}\), and the \(L=32\to64\) depth Cauchy gap at \(n=256\)
is \(4.226\times10^{-3}\); neither exceeds its preregistered curvewise 95%
bootstrap threshold. The \(P=5\) PDE gap against the pooled
\(n=256,L=64,S=64\) reference is \(6.564\times10^{-3}\), also unresolved
at 5%, whereas its gap against the noisier \(n=512,L=32,S=16\) block is
\(9.897\times10^{-3}\) and narrowly resolved. These finite-grid outcomes
do not identify an ordered limit.

The first complete quadratic Hermite refinement, \(P=5\to15\), moves
statistically farther from every audited exact reference, and the
complete-cubic run is only a directional stress test because its fast
cubature was not refined. The experiment therefore does not identify how
much of the finite gap comes from \(n,L,P,N\), or cubature, and does not
certify arbitrary-accuracy convergence. The exact frozen protocols and
bootstrap decisions are under `agent_outputs/statistical_audit/`.
