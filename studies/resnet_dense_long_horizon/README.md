# Dense Euclidean continuous-depth-scaled μP ResNet: long-horizon bundle

This bundle reproduces the corrected long-horizon experiment for finite-depth
residual approximants to the continuous-depth-scaled, fully dense network

\[
H^0=BX,\qquad
H^{\ell+1}=H^\ell+\frac{\gamma}{L}\tanh(W_\ell H^\ell),
\qquad
f=\frac1n a^\top H^L,
\]

trained by ordinary Euclidean μP gradient flow with

\[
\eta_{W_\ell}=L,\qquad \eta_B=\eta_a=n.
\]

All \(W_\ell\) are unconstrained dense matrices; \(B,W,a\) are all trained.
The primary instance is \(X=I_3\),
\(y=(0.8,-0.55,0.35)\), \(\sigma_w=0.65\), and \(A=\gamma=1\).

## What is actually simulated

There are two dynamical systems:

1. The exact finite dense network.
2. The coupled grade-\(K\) chronological \(q/r\) training-response
   projection for \(K=0,1,2,3\).

The projected system evolves \(W,a,H,P\) and retains every \(n\times n\)
matrix \(W_\ell\). It tests the response-truncation mechanism, including its
complete predicted output and every depth-wise Gram curve.

It is **not** an implementation of the conjectured width-independent
Liouville PDE. The latter additionally requires the width limit, fast
Gaussian conditioning/Onsager compiler, nonlinear grammar budget \(J\), and
depth-Galerkin budget \(N\). The precise conjectural PDE specification is
included under `theory/`.

## One-command reproduction

From this directory:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
./reproduce.sh
```

`reproduce.sh` fixes BLAS thread counts, runs the algebraic and detector
tests, executes the audit-fixed extension grid, produces tables/plots, and writes
checksums.

For a quick algebra-only check:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

For a selected experiment group:

```bash
python run_all.py --only central
```

Use `--force` to overwrite traces even when their configuration hash
matches.

## Audit-fixed extension protocol

`config/protocol.json` fixes, before looking at the new results:

- the seeds and width/depth/stress/neighborhood/restart cells;
- response orders;
- RK4 step and sampling grid;
- horizons \(4,8,16,32\);
- the plateau thresholds;
- the representative plot.

Chronology is explicit: the seed grid, response orders, plateau thresholds,
and \(T\le16\) ladder were fixed for the first pilot. That pilot showed that
some otherwise-flat runs lacked the next required doubling. The \(T=32\)
extension and the displayed absolute accuracy levels were then frozen before
running any \(T=32\) result.

The main runs continue to \(T=32\). A horizon \(H\) is called a plateau
candidate only if all stored samples in \([H/2,H]\) have:

- residual at most \(10^{-5}\) of the fixed output scale;
- output and every depth-Gram close to their value at \(H\);
- small vector-field output and all-depth Gram speeds;
- small trapezoidal estimates of output and Gram arclength.

The absolute/motion tolerance is

\[
\delta=10^{-6}S+10^{-4}M,
\]

where \(S\) is the initialization scale and \(M\) the observed total motion.
A candidate at \(H\) is accepted only when the same fixed-order trajectory
passes every later available doubling through \(T=32\), with each successive
doubling drift remaining within the earlier threshold.

Prediction accuracy is not assessed from terminal loss. The primary metrics
are maxima on the stored time grid:

\[
\max_{t_i\le T}\|f_K(t_i)-f(t_i)\|_2
\]

and

\[
\max_{t_i\le T,\ell}
\|G_K^\ell(t_i)-G^\ell(t_i)\|_F.
\]

All depth nodes and all Gram entries are stored.

## File map

- `src/dense_mup/core.py`: exact model, μP flow, q/r hierarchy, RK4, kernels,
  analytic observable speeds, and constraint defects.
- `src/dense_mup/experiment.py`: trace runner and provenance.
- `src/dense_mup/analysis.py`: plateau detector, recorded-grid metrics, tables,
  and plots.
- `tests/test_core.py`: finite differences, \(K=L\) derivative identity,
  exact kernel identity, zero-residual freeze, integrated RK4 floor, and
  hostile synthetic plateau tests.
- `results/raw/*.npz`: non-pickle raw traces.
- `results/processed/`: run-level and aggregate summaries.
- `figures/`: representative curves, every selected Gram entry,
  time-depth errors, and order convergence.
- `REPORT.md`: concise scientific interpretation.
- `metadata/`: environment, source hash, run manifest, and checksums.

## Scientific scope

A successful run supports the statement that a fixed, low response order
predicts the entire simulated finite-network transient through an operational
plateau and its simulated \(T=32\) feature state, not merely a local
training-time Taylor expansion.

It does not prove the all-time, width-independent finite-PDE conjecture.
There are zero compiled Liouville-PDE runs in this bundle, and every summary
records that fact explicitly.
