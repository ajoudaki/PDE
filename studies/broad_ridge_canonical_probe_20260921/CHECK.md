# Independent surgical checks

This check is scoped to the assigned target and canonical finite network. Its
scientific inputs are the assignment, complete `docs/NOTATION.md`, complete
`code/pde/finite_network.py`, and the new study's producer/protocol when supplied.
It does not use another study's evidence. The checker runs no training.

## Exact target cancellation

Write the implemented target as
\(y(X)=C K^{-1/2}\sum_{j=1}^K a_j\tanh(v_j^T X)\), where
\(X\sim N(0,I_d)\), every \(\|v_j\|_2=1\), and \(Va=0\). The optional
\(K^{-1/2}\) can be absorbed into the calibration constant. Oddness gives
\(E[y]=0\). Gaussian integration by parts, with the vanishing boundary term
justified by bounded tanh and the Gaussian density, gives

\[
E[X_i\tanh(v_j^T X)]
=v_{j,i}E[\operatorname{sech}^2(v_j^T X)]
=v_{j,i}E[\operatorname{sech}^2(Z)],\qquad Z\sim N(0,1).
\]

Consequently \(E[Xy(X)]=C K^{-1/2}E[\operatorname{sech}^2(Z)]Va=0\).
Conditioning on the independently generated directions, signs and calibration
constant preserves this identity. The target has no population degree-one
Hermite component; its nonzero Hermite components have odd degrees at least
three. This does not assert zero correlations in a finite training sample, or
that the empirical calibration fixes population variance exactly to one.

The construction \(a_*=s-V^T(VV^T)^{-1}Vs\), followed by scalar normalization,
satisfies \(Va=0\) when \(V\) has full row rank and \(a_*\ne0\). These conditions
hold almost surely for independent Gaussian directions and independent signs
when \(K>d\); the saved numerical realization is checked directly.

## Gradients, clock and closure

For raw input columns \(X\in\mathbb R^{d\times m}\), set
\(H=\tanh(WX/\sqrt d)\), \(S=\tanh(AH)\), \(f=c^T S/n\), and
\(r=f-y\). For the mean squared loss without a half, define

\[
D_2=c\odot(1-S^2),\qquad D_1=(A^TD_2)\odot(1-H^2).
\]

Here the vector \(c\) broadcasts over sample columns. The ordinary derivatives
are

\[
g_W=\frac{2}{mn\sqrt d}(D_1\odot r)X^T,\qquad
g_A=\frac{2}{mn}(D_2\odot r)H^T,\qquad
g_c=\frac{2}{mn}Sr^T.
\]

The canonical physical velocity is \((-ng_W,-g_A,-ng_c)\). The maintained
finite-network code uses precisely these normalizations.

With fixed bases and \(A=B_2MB_1^T/n\), the chain rule gives
\(g_M=B_2^Tg_AB_1/n\). Unit mobility on \(M\) therefore gives

\[
\dot A=-P_2g_AP_1,\qquad P_i=B_iB_i^T/n,
\]

while \(W,c\) retain mobility \(n\). Also
\(M_0=B_2^TA_0B_1/n\) gives \(A_{\mathrm{eff},0}=P_2A_0P_1\).
For \(LL^T=F^TF/n+\lambda I\) and \(B=FL^{-T}\),

\[
B^TB/n=I-\lambda L^{-1}L^{-T}.
\]

Thus the ridge-regularized \(P_i\) are positive contractions, not orthogonal
projections. Their eigenvalues lie in \([0,1)\) for positive ridge.

## Parameter counts

| Representation | Trainable scalars | Stored model scalars |
|---|---:|---:|
| Closure, \(n=1024,r_1=129,r_2=65\) | 74,945 | 273,601 |
| Dense, \(n=244\) | 75,396 | 75,396 |
| Dense, \(n=492\) | 274,044 | 274,044 |
| Dense, \(n=1024\) | 1,115,136 | 1,115,136 |

Dense counts are \(n^2+65n\). Closure trainables are
\(65\cdot1024+129\cdot65\), with \(1024(129+65)\) additional frozen basis
scalars. Stored-model counts exclude common data/target, temporary activations,
solver workspaces, and archived construction source \(A_0\).

## Core numerical checks

`probe_check.py` independently implements forward evaluation and the derivatives
above. It compares the dense derivatives and physical velocity to the maintained
API, checks dense and closure derivatives with PyTorch float64 automatic
differentiation, and checks closure derivatives with central directional
differences. The test is a tiny nondegenerate two-hidden-layer network with
\(n=11,d=3,m=7\); no optimization or time integration is performed.

The run passed: maximum absolute discrepancy was \(1.12\times10^{-16}\) for
the maintained physical RHS, \(2.09\times10^{-17}\) for automatic derivatives,
\(6.59\times10^{-12}\) for directional differences, and
\(5.00\times10^{-15}\) for the ridge Gram identity. The independently
regenerated target has \(\|Va\|_2\le2.2\times10^{-14}\). Raw values are in
`data/generated/broad_ridge_canonical_probe_20260921/check/checks.json` and the
frozen preflight archive below. The tiny difference in cancellation residual
between the first run and the frozen run is floating-point BLAS evaluation.

## Frozen producer and data preflight

Read the complete producer and frozen protocol. The producer's tiny dense and
closure RHS agree with the independent formulas to maximum absolute errors
\(1.12\times10^{-16}\) and \(1.67\times10^{-16}\), respectively.

Independently regenerate every saved Gaussian sample from its separate seed,
the normalized directions, projected coefficients, calibration constant and
labels. Directions, coefficients, all input panels, and calibration values
match exactly. Training/passive labels match to \(4.44\times10^{-16}\).
The actual saved \(\|Va\|_2\) is \(1.9901\times10^{-14}\). Training/passive
target RMS values are 1.004559330948 and 1.006215302189.

All four canonical source initializations reproduce. Dense sources match
exactly. Independent closure features, Cholesky factors, bases, \(M_0\), and
initial state agree to \(1.70\times10^{-15}\). Counts match the table above.

Frozen preflight output:
`data/generated/broad_ridge_canonical_probe_20260921/check_preflight01/checks.json`.
The first data-preflight run completed before the fresh-output policy was
requested and updated `check/checks.json`; the frozen invocation and all
subsequent invocations refuse to overwrite an existing output directory.

SHA256 fingerprints at freeze:

- Producer: `18acd8a89cdd3d607e74b7b61cdb79a0cde00aabd859c9059118a2889ebad915`.
- Protocol: `04b0afea0dd39efde4bb0d7b2924166410ae401d846e05b7090e3f206d61bc28`.
- Checker: `b3ca4005de561f3c335a7337ca50ad992efe755b0acc4ef391cc0f41d51af7a0`.
- Data archive: `c5f581ee8f36ab90b48f336d7f8e5b3f822838a70aa5a759ac53820e484b0ffd`.

The command uses `/home/amir/miniconda3/bin/python`, this study's
`probe_check.py`, `--producer`, `--data` pointing to `data01/data.npz`, and
`--output` pointing to a fresh directory. `--runs` takes completed run directories
and independently replays every saved checkpoint and terminal prediction/loss,
source construction, initial/terminal RHS, motion and norm statistics, and
accepted-loss summary. No training occurs in the checker.

## Completed replay and refinement

The frozen checker completed replay of all eight runs in 16.59 external
process-wall seconds. Evidence is in
`data/generated/broad_ridge_canonical_probe_20260921/check_replay01/checks.json`
(SHA256 `6271301976934089eb9c343aa1e132df07ea0cb9e758abb71f75e3420920a46b`).
All 47 checkpoints and eight final states passed. Recomputed predictions,
losses, motion and norm summaries matched exactly. Initial RHS discrepancy
was at most 3.47e-18, terminal RHS discrepancy at most 2.09e-16 absolute
and 2.15e-15 relative in L2. Source arrays reproduced as in the preflight,
and every accepted-step loss increase was zero. All source/data hashes and
tolerance configurations matched their frozen values.

The checker separately applied the refinement formulas to raw saved arrays,
without importing the analyzer. All gates passed; worst prediction difference
was 1.86814e-4, worst RMS-error difference 3.08428e-6, and the largest block
discrepancy was 0.005022 times its permitted threshold. Evidence is in adjacent
`independent_refinement.json`. That calculation took about 0.22 seconds.
All-four common checkpoint 30 and matched-three common checkpoint 100 were
confirmed. Every attempt was time-censored; this validation does not imply
completion through time 5000 or a scientific separation.

The coordinator appended this completed-replay summary from the checker's
delivered results and saved evidence when the user requested immediate closure.
The checker source remained frozen. No further training or checking is pending.
