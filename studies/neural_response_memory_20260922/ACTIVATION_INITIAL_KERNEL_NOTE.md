# Initial prediction kernels for the activation continuation

Date: 2026-09-25. Status: exploratory initial-state diagnostic, computed after
the activation campaign was frozen. This is not a training experiment, a
selection rule or a claim about later nonlinear fitting. The calculation
uses exactly the four prescribed activations, two literal eight-point tasks,
width 4096, seed 20260920 and original Gaussian draw order. No cap, phase,
numerical gate, initialization or activation choice is changed.

The authoritative calculation is `activation_circle_initial_kernel02`.
It supersedes `activation_circle_initial_kernel01` only to match the frozen
launcher's input arithmetic exactly: convert each degree value with
`value*math.pi/180`, then evaluate scalar `math.cos` and `math.sin`.
All eight input arrays were checked bit-for-bit against all 64 configurations
returned by the frozen launcher's `build_jobs` function, without launching
any process. The earlier arrays used NumPy degree conversion and trig, which
differed by at most 8.33e-16 in a coordinate. The first calculation's data
remain unchanged; its executed source is preserved in its own
`source_snapshot.py` with `source_snapshot_receipt.json`.

The main observation is a weak initial label response for sigmoid and strong
spectral anisotropy for GELU on these alternating-label tasks. For every
activation, most label energy lies in the two slowest initial eigenmodes.
These observations describe the starting point. They cannot establish the
cause of later slow fitting once hidden features and the kernel move, or
explain the wall-clock cost of an adaptive solver crossing activation kinks.

## Exact finite-width formula

Use the frozen bias-free network

\[
 h_{1,a}=\phi(W_1U_a),\quad h_{2,a}=\phi(W_2h_{1,a}),\quad
 h_{3,a}=\phi(W_3h_{2,a}),\quad f_a=c^Th_{3,a}/n,
\]

where \(U_a=(\cos\theta_a,\sin\theta_a)\), \(n=4096\), \(M=8\),
\(r_a=f_a-y_a\), and \(\mathcal L=M^{-1}\sum_a r_a^2\).
Let \(J_b\) be the \(M\)-row Jacobian of predictions with respect to the
flattened parameter block \(b\in\{W_1,W_2,W_3,c\}\). With mobilities
\((n,1,1,n)\), define the mobility-weighted prediction kernel

\[
 K=nJ_{W_1}J_{W_1}^T+J_{W_2}J_{W_2}^T+J_{W_3}J_{W_3}^T+nJ_cJ_c^T.
 \tag{1}
\]

It is an \(8\times8\) positive semidefinite matrix in exact arithmetic.
Using the residual-free backward signals

\[
 \delta_{3,a}=c\odot\phi'(z_{3,a}),\quad
 \delta_{2,a}=\phi'(z_{2,a})\odot W_3^T\delta_{3,a},\quad
 \delta_{1,a}=\phi'(z_{1,a})\odot W_2^T\delta_{2,a},
\]

the prediction derivatives are
\(\partial_{W_1}f_a=\delta_{1,a}U_a^T/n\),
\(\partial_{W_\ell}f_a=\delta_{\ell,a}h_{\ell-1,a}^T/n\) for
\(\ell=2,3\), and \(\partial_cf_a=h_{3,a}/n\).
The Frobenius identity
\(\langle uv^T,\widetilde u\widetilde v^T\rangle
=(u^T\widetilde u)(v^T\widetilde v)\) then gives the four blocks

\[
 K^{W_1}_{ab}=\frac{(\delta_{1,a}^T\delta_{1,b})(U_a^TU_b)}n,
 \qquad K^c_{ab}=\frac{h_{3,a}^Th_{3,b}}n,
\]
\[
 K^{W_2}_{ab}=\frac{(\delta_{2,a}^T\delta_{2,b})(h_{1,a}^Th_{1,b})}{n^2},
 \qquad
 K^{W_3}_{ab}=\frac{(\delta_{3,a}^T\delta_{3,b})(h_{2,a}^Th_{2,b})}{n^2}.
 \tag{2}
\]

These formulas require only thin response matrices and their Gram matrices;
no full \(n\times n\) gradient for each training example is formed. The two
initialized hidden matrices are still stored and multiplied. The derivative
conventions are the frozen ones, including ReLU zero and SELU negative-branch
selection at zero. A same-input forward verification found no exact zero
preactivation in any of the eight initialized networks, so their ordinary
first derivatives exist at the evaluated states.

Since \(\nabla_b\mathcal L=(2/M)J_b^Tr\), physical gradient flow gives

\[
 \dot r=-\frac2M Kr,\qquad
 -\dot{\mathcal L}=\frac4{M^2}r^TKr.
 \tag{3}
\]

Here \(K\) is the current kernel; (3) does not assert that it remains fixed.
At initialization the dense and P=1,2,3 closures share the same physical
weights and have zero moment defects, so their instantaneous prediction
velocities agree with this calculation. The diagnostic does not distinguish
their subsequent closure errors.

The label quadratic \(y^TK_0y\) gives the proxy rate
\(4y^TK_0y/M^2\) that would hold at exactly zero initial output. The actual
rate uses \(r_0=f_0-y\), retained separately in every output. Initial prediction
RMS is between \(5.92\times10^{-7}\) and \(6.04\times10^{-6}\), so the two
rates are close but are not equated.

If the kernel were held fixed, an eigenmode of eigenvalue \(\lambda\) would
have residual rate \(2\lambda/M\), and its squared residual would have rate
\(4\lambda/M\). This conditional linear calculation motivates recording the
label weights \(|v_j^Ty|^2\). No frozen-kernel trajectory or extrapolated
fitting time was used as an experimental reference.

## Results at the prescribed initialization

“Outliers” and “quadrant” denote the two frozen alternating-label tasks.
The table reports the actual rate \(-\dot{\mathcal L}(0)\). Conditions marked
unresolved are withheld under the precision screen described below; raw
eigenvalues and ratios remain in the saved data.

| Activation | Task | Initial loss-decay rate | Smallest eigenvalue | Largest eigenvalue | Condition, if resolved | Label energy in two slowest modes |
|---|---|---:|---:|---:|---:|---:|
| ReLU | Outliers | 0.00674794 | 1.28820e-4 | 0.734625 | 5.70271e3 | 59.3% |
| ReLU | Quadrant | 0.00136274 | 6.47402e-5 | 0.851024 | 1.31452e4 | 78.2% |
| Exact GELU | Outliers | 0.00437694 | 2.89864e-7 | 0.238768 | 8.23723e5 | 54.4% |
| Exact GELU | Quadrant | 0.000896176 | 5.61539e-9 | 0.305469 | 5.43986e7 | 65.3% |
| SELU | Outliers | 0.0869837 | 3.18093e-4 | 5.56287 | 1.74882e4 | 59.7% |
| SELU | Quadrant | 0.0257377 | 1.52148e-4 | 6.64778 | 4.36928e4 | 76.5% |
| Sigmoid | Outliers | 1.04372e-5 | 1.13227e-11 | 2.12728 | unresolved | 54.8% |
| Sigmoid | Quadrant | 3.30269e-6 | 1.71600e-13 | 2.12731 | unresolved | 63.2% |

The label-only decay rates, in the same order, are 0.00674793328,
0.00136273293, 0.00437693692, 0.000896176995, 0.0869825918,
0.0257380904, 1.04370348e-5 and 3.30279087e-6. The actual residual rates
above are preferable when describing the initialized network.

The readout block contributes over 99.99997% of the initial kernel trace
and over 99.9999% of its label quadratic in every case. This agrees with
the prescribed small-readout scaling: each hidden backward signal is linear
in c, so its kernel block is quadratic in c, whereas the readout kernel
does not contain c. It does not imply that feature learning remains negligible.

For sigmoid the label Rayleigh quotients \(y^TK_0y/\|y\|^2\) are approximately
2.08741e-5 and 6.60558e-6, despite largest eigenvalues near 2.1273. Thus a
large leading response direction coexists with very weak label-aligned
response. Balanced alternating labels cancel any exactly shared hidden
feature offset; the measured quadratic records the small remaining response
for these actual initialized features. This is evidence about initial
geometry, not a proof of later saturation or a causal explanation of a cap.

GELU's minimum eigenvalues are much smaller than ReLU's or SELU's on the
same task, especially in the quadrant. Since more than half the label energy
lies in the slowest two modes for every activation, an initial-rate summary
alone does not describe all label directions. A stronger interpretation
would require kernel or feature-motion observations along training, which
this bounded diagnostic does not add.

## Precision and independent formula check

All calculations use float64. We use

\[
 \tau=64\max(n,M)\,\epsilon_{64}\max_j|\lambda_j|
\]

as a conservative heuristic screen for small eigenvalues after length-n
contractions. It is not an interval-arithmetic or certified error bound.
Condition numbers are reported only when every eigenvalue exceeds this
screen. Sigmoid has seven resolved modes on outliers and six on quadrant;
its raw ratios are approximately 1.88e11 and 1.24e13. The energy in modes
below the screen is approximately 54.8% and 63.2%. Individual eigenvectors
within a poorly separated cluster need not be numerically stable; clustered
mode weights and the screen are descriptive diagnostics.

To avoid cancellation in \(q^TKq\), the reported label and residual
quadratics are evaluated as sums of nonnegative squared norms. For an
internal block let \(A=[q_a\delta_{\ell,a}]_a\),
\(B=[h_{\ell-1,a}]_a\), and compute thin QR factorizations
\(A=Q_AR_A\), \(B=Q_BR_B\). Since the Q factors have orthonormal columns,

\[
 q^TK^{W_\ell}q=\|AB^T\|_F^2/n^2=\|R_AR_B^T\|_F^2/n^2.
\]

The first-layer and readout terms are evaluated directly as
\(\|(\delta_1\operatorname{diag}q)U\|_F^2/n\) and
\(\|h_3q\|_2^2/n\), where U has sample rows. The maximum absolute difference
between these stable label quadratics and direct Gram-matrix quadratics is
1.56e-15; the maximum eigendecomposition residual entry is 1.78e-15. These
checks support the reported aggregate initial rates without certifying the
smallest sigmoid eigenvalues.

One independent autograd suite uses width 7, the same seed and eight literal
outlier inputs, with PyTorch's built-in activation implementations. Explicit
Jacobian Gram blocks agree with (2) for all four activations and all four
parameter blocks: 16 comparisons pass, with maximum entry error 1.67e-16.
The largest stable-quadratic discrepancy is 7.78e-16. This checks the
mobilities, factors of n, activation derivatives and QR-norm formula
independently of the width-4096 implementation's block contractions.

## Reproduction and scope

The author read the frozen activation protocol and literal cases, used their
canonical model definitions and the authorized frozen launcher source, and
read only newly generated diagnostic data
for the results above. No completed tanh result, running campaign result or
other study supplied scientific evidence. The script and note are owned by
the scoped activation-theory author. This is an author-checked exploratory
diagnostic, not an independent promotion review.

`activation_initial_kernel.py` completed all eight corrected cases in 3.091 CPU-wall
seconds, including the tiny autograd check and initialization; its declared
computation limit was 120 seconds. It used one CPU thread and no GPU or
training. A separate verification first matched each saved input array
against the frozen launcher, then found no zero preactivations and reproduced
the corrected diagnostic's own initial predictions bit-for-bit. This
distinguishes agreement with the actual input source from a same-code forward
consistency check. No extra seed or activation variant was evaluated; the
single repeated calculation corrects input representation. Existing campaign
settings remain frozen.

Relative to the preserved first calculation, the maximum absolute changes
are 7.18e-16 in a kernel entry, 8.88e-16 in an eigenvalue, and 5.56e-17 in an
actual initial loss-decay rate. All resolved-mode counts and condition-number
availability flags are unchanged; the table's displayed precision and
qualitative interpretation are unchanged. The full per-case differences and
separate input/forward checks are in `correction_verification.json`. This
small observed effect does not justify retaining mismatched inputs or
certifying eigenvalues below the stated precision screen.

The generated directory is
`data/generated/neural_response_memory_20260922/activation_circle_initial_kernel02/`.
It contains the eight NPZ kernels, block kernels, complete eigenvalues and
eigenvectors, modal label/residual weights, initial predictions and input
data; `kernel_metrics.csv`; `metrics_summary.json`; `tiny_autograd_check.json`;
`input_verification.json`; `correction_verification.json`; and the original
artifact hashes. The separately written correction verification receipt is
outside that earlier artifact manifest.

Reproduction uses a fresh output directory:

```bash
/home/amir/miniconda3/bin/python -B \
  studies/neural_response_memory_20260922/activation_initial_kernel.py \
  --out data/generated/neural_response_memory_20260922/activation_circle_initial_kernel_NEW
```

The initialization SHA256 is
`6043d3c0097c6cdb4c22b6db84fc4d5975b61dbeac895b6f6a2a2a8402e79ca0`.
Executed source hashes:

| Source | SHA256 |
|---|---|
| activation_initial_kernel.py | b6042f13fc91018791365a357421067a9840b8b8e06e273fdda04b012a29ffea |
| ACTIVATION_CIRCLE_PROTOCOL.md | 50a4df06992311b168446d9dec05fc10a5e86a3542cf429babfefc9c114d30c5 |
| activation_circle_cases.json | 603235601e132f875f091b39c55bae6c09148324b2451df87385b2b20c5af37e |
| run_activation_circle_campaign.py | 0f34943923886590d2e2c6c68f207c3f0064b33e72c5fa2b2d9f03c33c0baf14 |
