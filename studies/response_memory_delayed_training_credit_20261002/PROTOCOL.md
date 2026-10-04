# First execution protocol — frozen before outcomes

Frozen 2026-10-02, before downloading data or running training. This protocol
implements the supervisor's first-thrust ordering and replaces the screen's
three-seed/two-device-hour launch with one seed and an early significance stop.

## First decision

Does the exact full-horizon width-512 schedule improve unseen target MSE by
at least 5%, while the ordinary width-128 full-horizon proxy recovers no more
than 50% of that improvement when both schedules train the same width-512
network? If this necessary distinction is absent, stop this witness without
running memory orders. This is a significance screen, not a search for a
favorable task. The full-gradient reference and proxy have identical data,
validation objective, horizon, schedule family and intervention amplitude.

## Fixed data and learner

Download only the public MNIST training image and label IDX archives from
https://storage.googleapis.com/cvdf-datasets/mnist/ into this study's generated
namespace. Independently held-out splits all come from that archive because
the official MNIST test 3/8 subset has fewer than 2,048 images. Use NumPy RNG
seed 20261002 to sample without replacement, stratified equally by digit:
128 training, 512 validation and 2,048 test images. Each image is unique across
splits. Digits 3 and 8 have labels -1 and +1. Downsample 28x28 to 14x14 by exact
2x2 average pooling, map grayscale to [-1,1], append a two-column +/-1 strip,
and flatten to dimension 224. No outcome-dependent preprocessing is allowed.

Training source A and B each contain 64 images and are individually balanced
by digit. A's strip is exactly balanced within each digit; B's strip equals
its digit label. Validation/test strips are exactly balanced within each
digit, using independent RNG permutations. Source index is +1 for A, -1 for B.
This controls a shortcut on real digit images; it is not a benchmark claim.

Use the supplied scalar-output two-hidden-layer tanh network, canonical
Gaussian A and W0 initialization, readout zero, seed 0. Dense widths are 512
and 128. Loss is mean squared residual. Mobilities and factors are exactly
those in paper/main.tex: A'=-2/m sum lambda*r*ell*x^T/sqrt(d),
B'=-2/(mn) sum lambda*r*delta*h^T, w'=-2/m sum lambda*r*g.

## Schedule and numerical reference

Fix T=80, Heun step 0.05, and eight controls. On the sixteen length-5 windows
define b_j(t)=sin^2(pi*(t-5j)/5), zero elsewhere. The source contrast is
c(t;u)=sum_{j=0}^7 u_j*(b_j-b_{j+8}), and lambda_a=1+s_a*c.
This keeps integrated source exposure fixed and the instantaneous mean weight
one. All derivatives are with respect to u at zero. Actual interventions use
u=-0.25*gradient/max(abs(gradient)); no line search is permitted. The maximum
absolute contrast is 0.25 and every loss weight stays in [0.75,1.25].

Implement explicit differentiable RHS expressions and checkpointed fixed-step
Heun. Differentiate the actual discrete map, not a reverse-integrated
continuous adjoint. Run float64 on GPU0 using existing PyTorch; no installs.
Initial conditions are reproduced exactly for intervention reruns. All GPU
jobs and outputs stay in the study-owned namespace. Use fixed checkpoint
chunks of 20 steps unless memory requires a smaller chunk before outcomes.

Before interpreting the first outcome, check the width-512 gradient against
one centered directional difference at epsilon=0.001 in the normalized
all-ones direction; require relative discrepancy <=2%, or label the check
inconclusive if cancellation makes its denominator too small. Basic physical
gates are dense terminal training MSE<0.02 and RMS movement of both hidden
layers >0.10. Their failure prevents a positive mechanism claim. Report all
values even if a gate fails. A useful intervention/proxy distinction triggers
step-halving and epsilon-halving audits before being accepted.

## Conditional memory work

Only if the early significance distinction survives, implement/run q=1 and
q=2 from the exact moments and reconstruction in paper/main.tex lines 318–374.
The clock is explicitly unweighted rho, tau'=rho; only the backward source is
lambda*r*delta. Moment dilation row k is k on its diagonal and 2j+1 for j<k.
Initialization is hbar[:,0]=h(0), all higher hbar and all deltabar zero, tau=1.
Differentiate both moment families and the clock. A feature-history tangent
ablation detaches hbar only in B reconstruction, retaining its exact primal
trajectory. q=4 is available only as a diagnostic if q<=2 fails.

Subsequent pass thresholds remain the screen's: relative gradient error<=0.15,
cosine>=0.98, closure intervention recovers >=80% of the exact benefit, and
feature-tangent ablation <=50%. A delayed-credit claim additionally requires
a statistically/numerically resolved sign reversal between an early-window
validation gradient and its final-horizon counterpart. The present fixed task
may fail to contain such a reversal; no task/horizon/corruption sweep follows.

## Provenance, budget and stopping

Save downloaded archive hashes, data indices and strips, source hash, software
versions, seed, timings, peak allocated GPU memory, complete gradients,
schedules, MSE, accuracy and raw predictions. Save first-discriminator results
before any optional work. The strongest ordinary proxy is a primary result.

The cap is 30 cumulative GPU-process minutes and 45 wall minutes, measured
from this first execution thrust, on GPU0 only. The initial work began at
approximately 15:12 UTC on 2026-10-02. No other studies, Git writes, package
installs, shared-code edits or manuscript/book edits are allowed. If the first
distinction fails, report the failure and stop. If an integrity or numerical
gate fails, report inconclusive and stop unless the prescribed basic audit
resolves it within budget. Do not recast gradient alignment as a breakthrough.
