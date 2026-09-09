# FP32 Euler width campaign — Stage V protocol

Status: **unlaunched validation child**.  This protocol is subordinate to the
hybrid parent protocol at SHA-256
`d1e75ad896a3572f77b9bc6ec68a7047219a075645b87d44c520d677fc3b153a`.
It supersedes no mathematical result and does not authorize a scientific width
run.

## Target and reason for the child

The canonical finite network is

\[
z_i=n^{-1/2}\sum_jW_{ij}u_j^2,
\qquad f_n=n^{-1}\sum_i a_i z_i^2,
\]

under ordinary label-one squared-loss flow

\[
\dot\theta=2(1-f_n)n\nabla f_n,
\qquad \dot f_n=2(1-f_n)K_n.
\]

The earlier float64/RK4 child remains an unlaunched draft.  This child tests
whether explicit Euler in FP32 at rescaled step \(h=5\times10^{-6}\) is a
numerically faithful, affordable realization.  FP32 rounding is a separate
approximation axis: agreement here is empirical numerical validation, not an
exact ordinary-Gaussian or infinite-width theorem.

Existing validation-only side artifacts are audited in
`AUDIT_EXISTING_FP32.md`.  In particular, old matched n=8192 trajectories gave
maximum relative effective-kernel error \(1.35\times10^{-4}\) for Euler
\(h=5\times10^{-6}\) versus FP32/RK4, while halving to
\(2.5\times10^{-6}\) worsened the error to \(1.60\times10^{-3}\).  These
external controls eliminate a new broad RK4 ladder but cannot validate the new
nested RNG or one-lineage execution.

## Frozen Stage V points and budget

Generate one n=8192 antithetic lineage twice from exactly the same nested FP32
state:

- Euler \(h=10^{-5}\), \(t_{\max}=0.024\), wall cap 60 seconds;
- Euler \(h=5\times10^{-6}\), \(t_{\max}=0.024\), wall cap 120 seconds.

The cumulative successful-or-failed GPU budget is 180 seconds.  Each GPU batch
contains one lineage, hence two antithetic trajectories.  There is no optional
step and no retry in Stage V.

Width 16384 has zero budget.  It may be proposed only after a completed
2048/4096/8192 scientific ladder shows that width bias, rather than sampling or
roundoff, is the dominant uncertainty.

## Initialization and provenance

Every Gaussian is a deterministic function of seed, lineage, tensor domain,
and coordinate.  Float64 Box--Muller output is rounded exactly once to FP32.
Matrix coordinates use \((i,j)\), never a width-dependent row stride.

Each output contains:

- a full n=8192 initial-state digest;
- width-independent prefix digests at 2048, 4096, and 8192;
- the hash and coordinates of the common representative W sample.

The runner disables TF32, requests IEEE FP32 matrix multiplication, enables
PyTorch deterministic algorithms, and freezes the cuBLAS deterministic
workspace mode before creating a CUDA context.  These settings are recorded in
each point manifest; a later breadth campaign must reuse or separately validate
them.

The two Stage V points must have identical full-state, prefix, and monitor
digests.  Future width analysis must require equality of every common prefix
digest before calling the widths coupled.

The physical target is fixed to exactly (1).  The two antithetic branches
must have initial outputs cancelling within four FP32 ulps (using scale
\(\max(1,|f_+|,|f_-|)\)), and their three kernel components must agree under
the same convention.  The total kernel must equal the component sum within
eight FP32 ulps at every validated state.

## Required raw observables

At every state grid point retain, for both branches:

- output \(f\);
- direct \(K=K_a+K_W+K_u\) and all three positive components;
- weighted numerator \((1-f)K\);
- physical loss \((1-f)^2\).

At the declared output nodes retain separately:

\[
K_{\rm eff}(y)=\frac{\mathbb E[(1-f)K]}{1-y},
\qquad \mathbb E K,
\qquad \mathbb E(1-f)^2,
\qquad (1-\mathbb Ef)^2,
\]

and each path's normalized-progress kernel at

\[
f(\tau_r(y))=f_r(0)+(1-f_r(0))y.
\]

No one of these observables may be substituted for another.

The frozen common-clock/output and normalized-progress grid is

\[
0,\ 0.1,\ 0.25,\ 0.5,\ 0.75,\ 0.9,\ 0.95,\ 0.99.
\]

The normalized-progress table omits the trivial zero node.  Every comparison
"through 0.9" uses exactly the nodes at or below 0.9.  Its relative-error
convention is the symmetric pointwise error

\[
\operatorname{rel}(x,z)=
\frac{|x-z|}{\max((|x|+|z|)/2,10^{-12})},
\]

and a vector comparison means the maximum of this quantity on the frozen
nodes and retained branches/components.

## Per-step FP32 update audit

For every Euler step and branch retain:

- exact fractions of a and u entries unchanged by the FP32 addition;
- exact unchanged fraction on 8192 deterministic, hash-bound W coordinates;
- ideal and realized a/u update norms and their cosine;
- ideal and realized sampled-W update norms and their cosine;
- a/u actual state norms, sampled-W actual state norm, and an explicitly
  labeled *ideal algebraic* full-W norm recurrence.

Actual full-W norms are recomputed at five sparse diagnostic checkpoints
(including endpoints) in each point.  The ideal recurrence is never used as
state-ceiling evidence; its relative discrepancy from the actual checkpoint
norm is reported.

GPU work is synchronized every 100 Euler steps for truthful internal wall
telemetry, and at every endpoint.  A separate process timeout enforces the
declared 60/120-second point caps even between those synchronization points.
CUDA peak-allocation statistics are reset at each point.

## Runtime validity gates

Every point fails closed if any of these occurs:

- wall, step, host-memory, or GPU-memory cap is reached;
- a state or observable is nonfinite;
- a kernel component is nonpositive, or total K leaves [1e-10, 1e10];
- sampled or checkpointed full state reaches magnitude 1e4;
- ensemble mean output decreases by more than 1e-6;
- ensemble mean physical loss increases by more than 1e-6;
- a declared output/progress node is not reached.

The analytic gradient and sum-of-squares kernel must match automatic
differentiation in source tests.  K must match the sum of its components at
runtime to FP32 roundoff.

## Stage V decision gates

Let the fine point be h=5e-6.  Stage V passes only if all runtime gates pass,
the digest identities hold, and:

1. Through y=0.9, the h=1e-5 and h=5e-6 common-clock effective kernels and
   normalized-progress kernels differ by at most 0.2% relatively; each direct
   component differs by at most 0.3%.
2. Through ensemble mean output 0.9 for h=5e-6, maximum unchanged fractions
   are at most 5% for a, 1% for u, and 75% for the sampled W coordinates.
   All-time maxima are retained descriptively and cannot fail this gate.
3. Over the same inferential steps through ensemble mean output 0.9,
   realized/ideal norm ratios lie in [0.95,1.05] for a and u and [0.80,1.20]
   for sampled W.  Minimum update cosines are 0.999 for a/u and 0.995 for
   sampled W.  Late residual-decay stalling is reported but is not a gate.
4. With \(m_k=\mathbb E f_k\), define the left-driver defect

   \[
   d_k=\frac{m_{k+1}-m_k}{2h}-\mathbb E[(1-f_k)K_k].
   \]

   Through y=0.9, the fine maximum relative defect is at most 1%, relative RMS
   defect at most 0.3%, and cumulative relative defect at most 0.1%.  Each fine
   defect metric must be no larger than 0.75 times its coarse counterpart plus
   5e-4 absolute slack.

The old same-state Euler/RK4 discrepancy is historical method validation only.
Because that artifact uses a different shape-dependent RNG and lineage, its
curve is not compared pointwise with this fresh Stage-V curve and is not an
acceptance gate.

Pass status is `eligible_to_freeze_stage_W`; it does not itself launch Stage W.
Any failed gate is `Euler_FP32_h5_invalid_or_inconclusive`, closes this child,
and cannot be interpreted against the Stieltjes conjecture.

## Conditional future Stage W

Only after Stage V passes and a new hash-bound unlock is approved may a fresh
nested h=5e-6 ladder be frozen at n=2048,4096,8192 with 16 common antithetic
lineages.  The prospective cumulative cap is 1500 GPU-seconds; n=16384 remains
closed.  Its statistical analysis must re-invert every resampled mean clock and
retain both raw and normalized-progress estimands.  These future rules do not
authorize any Stage-W point now.
