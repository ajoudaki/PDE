# Frozen protocol: global Stieltjes proxy hierarchy

Status: **frozen before any scientific finite-width trajectory was run**.  The
CPU and GPU smoke configurations are validation-only and are not scientific
evidence.  This protocol authorizes only the branches written below; a failed,
timed-out, memory-limited, or statistically unresolved point is closed as
inconclusive without a retry at a larger budget.

## 1. Decision question and claim level

For every already-audited scalar training channel, let

$$
R(x)=\frac{K(\sqrt x)-A}{x}=\sum_{r\geq0}(-1)^r\mu_r x^r,
\qquad A=K(0).
$$

The strong hypothesis tested here is the conjunction:

1. finite-width natural squared-loss flow has a deterministic width-first
   kernel $K_\infty(y)$ on the training range $0\leq y\leq0.99$;
2. its right jet is the accepted fixed-order MFP jet; and
3. $K_\infty$ is the Stieltjes resolvent selected by those moments.

This campaign cannot prove all-order Hankel positivity, moment determinacy, or
the width-first/global-trajectory bridge.  A valid bracket violation rejects
the conjunction for that channel; it does not retroactively invalidate an
exact finite-order MFP or Hankel certificate.

## 2. Frozen approximation hierarchy

Level zero is the frozen-feature/NTK kernel $K_0(y)=A$.  Adding one accepted
moment at a time gives the Stieltjes continued-fraction convergents.  Odd
moment counts are zero-Radau upper kernels and even moment counts are Gaussian
lower kernels.  Conditional on a representing measure,

$$
K_1^-\leq K_2^-\leq K_\infty\leq K_2^+\leq K_1^+\leq K_0^+.
$$

The primary improvement statistic is contraction of this two-sided envelope,
not monotonic error of the alternating single sequence.  Equal-information
Taylor polynomials are a control only: their eventual deterioration is not a
falsifier because the formal series has zero radius.

Every proxy curve is constructed from the hitting-time maps

$$
S(y)=\int_0^y\frac{du}{K(u)},\qquad
T(y)=\int_0^y\frac{du}{2(1-u)K(u)},
$$

not by proxy ODE time stepping.  Output and loss are obtained by inversion and
$L=(1-y)^2$.

## 3. Primary metrics and classifications

The common primary grid is

$$
\mathcal Y=(0,.1,.25,.5,.75,.9,.95,.99).
$$

The primary kernel metrics are the simultaneous-band bracket escape and

$$
W_m^K=\max_{y\in\mathcal Y}
\log\!\frac{K_m^+(y)}{K_m^-(y)}.
$$

Secondary metrics are the errors in $T(y)$, output, absolute loss, $4K(.99)$,
and equal-information Taylor error.  Relative or log-loss error as
$t\to\infty$ is forbidden.

At every tested prefix:

- **compatible** means the complete 99% simultaneous reference band lies
  inside the rational bracket at all grid nodes;
- **contrary** means the complete band is outside one side at some node, the
  same signed escape appears at the two largest valid widths, and all
  discretization, extrapolation, initialization, and symmetry gates pass;
- **inconclusive** covers every overlap, insufficient resolution, or failed
  validity gate.

The campaign-level outcome is **supportive** only if every statistically
resolvable prefix is compatible, the two fixed-parity rational subsequences
move toward the extrapolated reference, and rational proxies outperform the
equal-information Taylor control in the primary sup-log metric at the deepest
resolvable level.  One valid contrary prefix makes that channel contrary.
Nothing here is classified as a proof.

## 4. Reference estimand and validity gates

The primary finite-width reference is ordinary Gaussian initialization with
antithetic readout signs under the actual natural squared-loss flow.  The
effective ensemble kernel is formed **after averaging**:

$$
K_{\mathrm{eff},n}(y)=
\frac{\mathbb E[(1-f_n)K_n]}{1-\mathbb E[f_n]}.
$$

The direct analytic $K_n=n\nabla f_n^TM\nabla f_n$ is never obtained by
numerically differentiating a curve.  A separate rank-one readout-centered
output-clock ensemble is a variance-reduced sensitivity only; it may not
replace the ordinary ensemble.  Its projection norm must vanish with width
and the two ensembles must agree within their combined extrapolation bands.

Mandatory gates are:

1. float64, TF32 disabled, analytic gradients and kernels matching autograd at
   small width;
2. source/config hashes frozen before scientific execution;
3. exact initial antithetic cancellation and finite states/kernels;
4. nondecreasing ensemble mean output, nonincreasing mean physical loss, and
   output-clock identity defect at most $10^{-7}$;
5. RK4 step-halving change at most $2\times10^{-3}$ relative in $K$ through
   $y=.95$ and $5\times10^{-3}$ at $y=.99$;
6. no clipping, dropped trajectories, isotonic repair, post-hoc seed changes,
   or replacement of finite-width means by limiting MFP values;
7. 99% pair-lineage bootstrap bands with 2,000 frozen resamples, plus the
   union of $1/n$, $1/\sqrt n$, leave-smallest-width-out, and top-width-only
   sensitivity bands;
8. Jensen/self-averaging gaps and, for multiple inputs, transverse symmetry
   leakage must decrease across the two largest widths.  A nondecrease larger
   than the joint 99% uncertainty makes the channel inconclusive.

## 5. Hard resource ceilings applying to every point

No point may exceed:

- 20 minutes for a pilot or 30 minutes for a preauthorized main-width point;
- 18 GiB PyTorch allocation on one 24-GiB GPU and 16 GiB host RSS;
- 4,096 stored output nodes, 200,000 batch-integrator steps, or 512 MiB raw
  arrays;
- width 4,096 and 64 antithetic pairs;
- one ordinary attempt and one predeclared step-halving subset.  There is no
  retry, grace period, automatic batch-size reduction, or larger-width rescue.

The entire suite is capped at **8 GPU-device-hours**, including failed and
timed-out scientific points.  Validation smoke runs have a separate maximum
of 15 GPU-minutes total.  Stages stop when their own cumulative cap is reached
even if unused budget exists elsewhere.

## 6. Stages and fail-closed branches

### Stage 0: exact no-width calibration

Run the exact Lambert-$W$ variance boundary on 501 equally spaced points in
$0\leq y\leq.99$.  Caps: 120 CPU seconds, 4 GiB RSS, no subprocess, no GPU.
All rational levels must have the prescribed side, all envelopes must be
nested, and the final sup-log kernel error must be below $10^{-5}$.  Failure
stops the suite as an implementation failure.  Taylor behavior has no gate.

### Stage 1: engine validation

Both RTX 3090s must expose at least 18 GiB free memory and pass a tiny float64
matmul.  Each GPU then runs the fixed width-16 validation configuration under
210 seconds and 2 GiB.  The CPU/autograd tests and CPU smoke must also pass.
Any failure stops scientific execution; it does not authorize environment or
solver substitution.

### Stage 2: canonical pilot

The pilot uses ordinary physical flow at $(n,R)=(256,32),(512,16)$ and the
separate output-clock sensitivity at $(512,16)$.  A held-out four-pair
width-512 half-step run is the discretization check.  Each point is capped at
10 minutes, 8 GiB GPU allocation, and 8 GiB host RSS; the whole pilot is
capped at 1 GPU-device-hour.

The canonical main ladder is authorized only if all validity gates pass and
the 99% band at $y=.9$ is narrower than one half of the bracket available from
$\mu_0,\mu_1$.  Otherwise the canonical result is inconclusive and all neural
branches close.

### Stage 3: canonical main ladder

Use ordinary physical flow at

$$
(n,R)=(512,64),(1024,32),(2048,16),
$$

sharded across the two GPUs, with a held-out four-pair half-step check at the
largest completed width.  Per-point cap: 30 minutes and 18 GiB.  Stage cap:
3 GPU-device-hours.  A conditional $(4096,8)$ point is allowed only if the
completed width extrapolation is valid, its projected 99% half-width is at
most one half of the next unresolved rational bracket at $y=.9$, and the
measured resource projection fits 30 minutes/18 GiB.  It has its own 30-minute
cap and counts inside the same 3-hour stage budget.

### Stage 4: one-input deformation pilots

This stage is authorized only if the canonical run is compatible at two or
more nontrivial moment prefixes.  Proxy curves are generated for the full
accepted domains, but neural references are restricted to the six frozen
stress points

$$
c=1,2;\quad (\alpha,\beta)=(4,1),(1,4);\quad
v=\tfrac12,2,
$$

where $c$ is activation centering, $(\alpha,\beta)$ is the block metric, and
$v$ is middle-weight initialization variance.  Each begins with
$(n,R)=(256,16)$ under 10 minutes.  A point gets $(512,16),(1024,8)$ only if
its pilot band is narrower than one half of its deepest available bracket at
$y=.9$.  Total per parameter point: at most 40 GPU-minutes; whole stage: at
most 2 GPU-device-hours.  At most three points may receive the main-width
branch, ranked before their neural results by deepest proxy-bracket width.

The first- and second-hidden squared RMS observables are recorded on every
relative-metric trajectory.  $Q_1$ is a consistency check inherited from
$K$; $Q_2$ is a separate companion hierarchy and is never counted as another
output-kernel confirmation.

### Stage 5: two-input pilots

Authorized only after Stage 4 has no contrary result.  Run the full natural
batch loss, never an imposed scalar ascent, at

$$
t=\theta^2=.25,.75
$$

for equal and opposite labels.  Pilot $(n,R)=(256,16)$; conditional main
$(512,16),(1024,8)$.  Per parameter/label point cap: 40 GPU-minutes; stage cap:
2 GPU-device-hours.  Nonvanishing transverse signed-margin leakage makes the
point inconclusive.  The singular opposite-label endpoint $t=1$ is forbidden.

### Stage 6: three-input pilots

Authorized only if Stage 5 has at least one compatible equal-label and one
compatible opposite-label point.  Test equal labels at

$$
\rho=-\tfrac14,\tfrac12
$$

with pilot $(256,16)$ and conditional main $(512,8)$.  Per point cap: 30
GPU-minutes; stage cap: 1 GPU-device-hour.  Only two moments exist, so failure
to resolve the first bracket closes the point without further widths.

There is no four-input, generic multi-angle, cubic/mixed-activation, greater-
depth, or new-MFP branch in this suite.

## 7. Artifact and stopping policy

Code, protocol, frozen JSON configurations, compact summaries, manifests,
hashes, and derived certificates are retained in Git.  Large NPZ arrays,
logs, binaries, caches, and checkpoints are ignored but must be named and
hashed in tracked manifests.  Each run records command, timestamps, device,
source/config hashes, exit status, wall time, peak allocations, seeds, and all
failed points.  A run directory is never overwritten.

No branch may be added after inspecting a scientific trajectory.  Any desired
change requires a separately named future campaign and does not alter this
classification.
