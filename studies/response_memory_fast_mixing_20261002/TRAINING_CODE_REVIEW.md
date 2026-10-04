# Internal code review of the initialized-learning gate

Verdict for producer v1: **PASS for the implemented q=1 arithmetic and CPU
checks; INCOMPLETE for the protocol's scientific gate.** The original producer
does not retain the feature and Gram trajectories needed for its stated
comparison. This is an evidence blocker for declaring that gate passed. No
scaling, transpose, or fixed-feature-baseline blocker was found. GPU execution
and numerical refinement were not independently exercised in this review.

This is a scoped internal code review, not a fresh blind proof review. It uses
only the assigned training protocol and producer, the already reviewed reuse
sources, and independent synthetic CPU checks. Neither reserved GPU was used.
No producer source was edited. A later source version requires a separate
addendum; the findings below are pinned to v1, even if the active producer has
subsequently changed.

## Input hashes

| Input | SHA-256 |
|---|---|
| Original `TRAINING_PROTOCOL.md` | `b7aa9783995aab9e65752dd36c7a16d3b493ba20f673fe30586f9041093447f8` |
| Original `fast_training.py`, preserved identically as `fast_training_v1.py` | `753beb081da05f3f73394e423142bbff52fbe5ce3ac9e53273f33e87314353b0` |
| Previously reviewed `reuse_check.py` | `3eb7e3e3bd07f1c5ae636dd30b180e4f5fe2403d6a06f9fd9ad3a66aaae6a3b2` |
| Previously reviewed `REUSE_THEORY.md` | `8a58f0b887ab5d907aeb1c1f849e4b623e58248650157a152132cb5b28be962d` |

The original training inputs were hashed before review. The preserved v1 copy
was checked against that hash before extracting its CPU-compatible functions.
Scratch, the exact extraction/check script, and numerical results are in
`data/generated/response_memory_fast_mixing_20261002/training_review/`.

## Blocking and material findings

1. **Missing trajectory evidence.** `run_one` saves predictions, fixed-feature
   predictions, the initial second-layer training Gram, and scalar motion/Gram
   summaries. It does not save any hidden activations or evolving Gram
   matrices. Two Gram matrices can have the same trace and squared Frobenius
   norm while being very different matrices. Consequently `gram_trace` and
   `gram_square` cannot substitute for the required comparison of mean Gram
   trajectories. Nor does RMS displacement determine a feature Gram. A fresh
   reproduction retaining training activations or both layers' training Grams
   at every scheduled snapshot can repair this evidence gap; the original
   outputs must remain identified as incomplete for that criterion.
2. **The comparison rule is underspecified.** The protocol does not define the
   trajectory norm, time aggregation, prediction sample partition, or which
   layer's feature Gram enters “closer.” The producer contains no implementation
   of that spectral decision rule. These choices must be disclosed before the
   repaired outputs are compared, with any post-pilot choice marked as such.
   Coordinatewise neuron comparisons across ensembles would not be suitable:
   compare sample-indexed Gram matrices and within-model RMS feature motion.
   A split outcome remains inconclusive under the written protocol.
3. **GPU correctness remains conditional on execution checks.** Static inspection
   found coherent graph capture/reset/replay logic, but this review used CPU
   only and did not read run outputs. The actual recorded action, graph,
   reproduction, and step-refinement checks remain necessary evidence. In
   particular, the script does not itself run the reserved finer-step or
   identical-seed reproductions or compare their predictions.

## Model, scaling, and numerical arithmetic

For (m) training examples and width (n), the stored state is
(A\in\mathbb R^{n\times d}), (w\in\mathbb R^n),
(H,D\in\mathbb R^{m\times n}), and scalar clock (\tau>0). Rows of (H,D)
are the protocol's raw moments, not normalized moments. For a query matrix
(X\in\mathbb R^{p\times d}), define

\[
h=\tanh(XA^\top/\sqrt d),\qquad
B=W_0-\frac{2D^\top H}{mn\tau},\qquad
g=\tanh(hB^\top),\qquad f=gw/n.
\]

The producer's low-rank evaluations of (hB^\top) and
(\delta B), where (\delta=(1-g^2)\odot w), exactly match this dense
construction. Its first-layer physical velocity equals (-n\nabla_A\mathcal L)
and its readout velocity equals (-n\nabla_w\mathcal L) for
(\mathcal L=m^{-1}\|f-y\|^2), with the reconstructed (B) held fixed when
taking these two derivatives. This matches the stated mobilities.

With training residual (r=f-y) and (\rho=\sqrt{m^{-1}\|r\|^2}), the code
stores (\dot H=\rho h), (\dot D=r\odot\delta), and (\dot\tau=\rho).
It uses (H/\tau,D/\tau) only in the reconstruction, and initializes
(H=h(0),D=0,\tau=1,w=0), preserving the stated unit forward prefix.
There is no missing normalization of the raw moments. The CPU oracle's
reconstruction derivative and product-defect identity also have the stated
factors and signs. Its division by (\rho) occurs only in that random oracle,
not in the training equations, so residual-zero training is well defined.

An independent float64 dense/autograd oracle, using a nonzero arbitrary
moment state, produced:

| Check | Maximum absolute error |
|---|---:|
| Entire RHS versus independent dense oracle | (2.22\times10^{-16}) |
| Reconstructed matrix derivative plus loss gradient minus product defect | (5.55\times10^{-17}) |
| One Heun step versus independently assembled dense Heun step | (5.55\times10^{-17}) |
| Fixed-feature predictions versus affine matrix exponential | (9.66\times10^{-15}) |

The Heun implementation forms both stages before mutating any component of
the stored state. The two-stage evaluations use their respective raw moments
and clocks. This is the expected explicit trapezoidal method, not an Euler
update with partially updated coordinates.

The fixed-feature baseline also has the correct readout mobility. With initial
training features (G\in\mathbb R^{m\times n}), training kernel
(K=GG^\top/n), and query cross-kernel (K_*=G_*G^\top/n), the training
prediction obeys
(\dot f=-2K(f-y)/m), (f(0)=0). If (K=Q\operatorname{diag}(\lambda)Q^\top),
the saved baseline computes

\[
f_*(t)=K_*Q\operatorname{diag}\left(
\frac{1-e^{-2\lambda t/m}}{\lambda}\right)Q^\top y.
\]

This was checked against an independent augmented matrix exponential for the
affine readout dynamics. The implementation forms its Gram in float32 before
converting to float64, and replaces eigenvalues below (10^{-12}) by that
threshold. Thus “exact” means the analytic fixed-feature solution evaluated
numerically; it is not an exact-arithmetic certificate. Near-null eigenvalues
would be handled more faithfully by the continuous limit (2t/m) and a stable
`expm1` evaluation. No baseline normalization error was found.

## Mixer and CUDA graph audit

The XOR butterfly in `_hadamard` gives (u+v) in the lower-bit position and
(u-v) in the higher-bit position, followed by (n^{-1/2}) normalization.
Independent CPU emulation of exactly that butterfly agreed with explicitly
constructed Sylvester matrices at widths 8, 128, and 512 to at most
(4.89\times10^{-15}) in float64. This checks the mathematical butterfly,
not Triton's GPU lowering or GPU rounding behavior. The scripted widths are
powers of two; the wrapper has no general non-power-of-two guard.

The extra outer row and column permutations are reversed with their inverses
in `transpose`, in the correct order relative to the signs and Hadamards.
Using independent dense Hadamards on CPU, all four mixers passed explicit
matrix and transpose checks in float32, with relative errors below
(2.43\times10^{-7}). Additional inner-product adjoint checks were consistent
with float32 rounding. The production `checks` function already compares
forward/transpose actions with a materialized matrix, although it does not
separately record the protocol's dot-product adjoint check.

Graph warmup and the eager test use clones/reset copies of the same initial
state. Captured operations refer to stable state buffers; replay updates those
buffers in place. A reset before the checked replay and another reset before
the training loop prevent warmup/checking from advancing the scientific
initial condition. The loop saves time zero, performs exactly (40/dt)
replays, and saves the endpoint. The comment that capture itself “executes
once” should not be relied on as CUDA semantics; the resets make the intended
count independent of that comment.

The producer assumes its selected CUDA device is also the current device.
`synchronize`, `CUDAGraph`, peak-memory reset/reporting, and device-name queries
use the current device rather than `args.device` explicitly. Masking physical
GPU1 as the sole visible device and using `cuda:0` satisfies that assumption.
Passing `--device cuda:1` with a different current device is not reliably
supported by this implementation and should not be treated as equivalent.

## Data, metrics, and protocol qualifications

The split uses labels only to select 32 examples per class. Centering uses the
training mean only; each image's later norm depends only on that centered
image. Training RHS calls receive only the first 64 images and labels.
Held-out images participate in evaluation, not updates. A synthetic-loader
test changed every held-out image and verified bit-for-bit unchanged training
arrays and labels, disjoint split indices, and 32 training labels per class.
No train/test preprocessing leakage was found. The held-out loss controls the
feature-learning gate as preregistered, so it functions as a validation gate;
it should not simultaneously be advertised as a wholly untouched final test.

Saved MSEs, held-out classification error, RMS feature displacement, and Gram
scalar summaries implement their formulas correctly. Feature displacement
uses all train and held-out images together, whereas the Gram summaries use
training images. This distinction should be stated in the analysis. Training
classification error is not separately recorded, but is recoverable from the
saved predictions and labels.

The useful-feature gate applies `all(low_motion or insufficient_improvement)`
over all width/seed/law runs. This means scaling is allowed if at least one run
has both enough motion and enough improvement. It does not establish useful
feature learning for every ensemble. The word “all laws” in the prose should
not be paraphrased as though each law must independently pass. The producer
also applies this stopping rule at every requested width, not only width 512.

All laws share the same initial (A) at a given seed and width; structured
laws share signs and permutations as stated. The Gaussian matrix and the
Gaussian-diagonal spectrum reuse `seed+19000` for their separate random
generators: the latter's unnormalized magnitudes are the absolute first row
draws of the former before scaling. Their marginal laws are correct and each
is separate from (A), but the two ensembles are not mutually independent.
If “Gaussian W0 is independent” intends independence across ensembles, that
is a protocol discrepancy; account for the actual pairing in uncertainty
statements rather than assuming independent replicates.

`moving_scalars` correctly counts the mathematical state (A,w,H,D,\tau),
and `fixed_entries` counts the initialized mixer representation. These are
not total live-array counts: initial/eager state copies, initial features,
kernel arrays, data, graph intermediates, and saved trajectory buffers are
also resident. The reported allocator peak is the useful empirical complement
on the correct current device. Integer and float entries also have different
byte sizes. None of these counts yet demonstrates a total-memory advantage.

`compilation_seconds` includes initialization and eigendecomposition as well
as warmup/capture; `training_seconds` includes scheduled evaluations and host
transfers. These names should not imply isolated kernel compilation or pure
update-kernel time. The 1800-second guard uses wall time between trajectories,
not a hard GPU-process timer, and does not interrupt a long trajectory. A
mid-trajectory exception does not save that partial trajectory; a failure in
the initial checks occurs before the configuration file is written. Thus
retention of failed attempts currently depends on external logs. Completed
trajectory files are retained, and the output directory is correctly required
to be new.

The Wang–Zhong–Fan theorem's applicability and the protocol's claim of exact
correspondence to an external manuscript were outside this input scope. The
review verifies correspondence to the fully stated equations in the supplied
protocol. It does not certify an external theorem's hypotheses or a scientific
winner from training results that were not supplied to this review.
