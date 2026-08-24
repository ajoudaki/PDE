# Preregistered side experiment: joint width/step-size limit

**Frozen before implementation and execution:** 23 August 2026.

## 1. Decision question

For the exact canonical three-hidden-vector arctangent network, does ordinary
simultaneous gradient descent exhibit a numerically stable joint limit as
width \(n\to\infty\) and step size \(\Delta\downarrow0\), or is there a
shrinking initial boundary layer compatible with

\[
 f(0)=0,\qquad f(t)=1\quad(t>0)?
\]

Here \(\Delta\) is the discrete gradient-descent step.  Physical time is
\(t=k\Delta\); there is no additional learning-rate multiplier.  This
distinguishes the numerical \(\Delta\downarrow0\) limit from a mere slowing
of the same flow by changing time units.

## 2. Exact model and update

The target is \(y_\star=1\).  Initialization and all normalizations are those
of `FROZEN_CORE_CONTRACT_2026-08-23.md`.  At step \(k\), compute the fields

\[
X_1=\arctan u,\quad Z_2=G_1X_1,\quad X_2=\arctan Z_2,
\quad Z_3=G_2X_2,\quad X_3=\arctan Z_3,
\]

\[
B_3=AD_3,quad R_2=G_2^{\mathsf T}B_3,quad
B_2=D_2R_2,quad Q_1=G_1^{\mathsf T}B_2,quad
f=n^{-1}A^{\mathsf T}X_3,quad e=1-f.
\]

One exact simultaneous metric-gradient step is

\[
\begin{aligned}
A^+&=A+2\Delta eX_3,\\
u^+&=u+2\Delta eD_1Q_1,\\
G_1^+&=G_1+\frac{2\Delta e}{n}B_2X_1^{\mathsf T},\\
G_2^+&=G_2+\frac{2\Delta e}{n}B_3X_2^{\mathsf T}.
\end{aligned}                                           \tag{2.1}
\]

All right-hand sides in (2.1) are evaluated at the old state.  No clipping,
regularization, early stopping, normalization layer, or activation change is
allowed.

## 3. Competing hypotheses

**Regular-flow hypothesis \(H_{\rm reg}\).**  After the step-size error is
resolved, predictor/loss curves, threshold hitting times, and the raw kernel
stabilize with width.  In particular, for fixed \(q\in(0,1)\),

\[
 \tau_q(n,\Delta)=\inf\{k\Delta:f_k\ge q\}
\]

approaches a positive number as \(\Delta\downarrow0\), \(n\to\infty\).

**Instantaneous-collapse hypothesis \(H_{\rm jump}\).**  Step-size-resolved
hitting times \(\tau_q\) shrink toward zero with width for every fixed
\(q<1\).  Equivalently, the near-zero modulus of continuity grows toward a
unit jump.  A growing initial or pre-threshold raw kernel supplies the
expected mechanism.

**Third outcome.**  Slow width drift, unresolved discretization, or mixed
threshold behavior is inconclusive.  No finite computation rules out a
slower-than-polynomial boundary layer.

## 4. Frozen design

- widths: \(n\in\{128,256,512,1024,2048\}\);
- step sizes:
  \(\Delta\in\{0.04,0.02,0.01,0.005,0.0025\}\);
- six initialization keys \(7101,\ldots,7106\) per width, paired across step
  sizes at fixed \((n,\text{key})\) and independent across widths through
  `SeedSequence([key,n,20260823])`;
- physical horizon \(T=2\);
- predictor thresholds
  \(q\in\{0.10,0.25,0.50,0.75,0.90,0.95\}\);
- float64 arithmetic and exact dense Gaussian matrices;
- at most six CPU workers, 30 minutes wall time, and 1 GiB retained output.

At every gradient step record \(f\), loss \((1-f)^2\), raw kernel

\[
K=\|X_3\|_n^2+
  \|B_3\|_n^2\|X_2\|_n^2+
  \|B_2\|_n^2\|X_1\|_n^2+
  \|D_1Q_1\|_n^2,                                     \tag{4.1}
\]

its four blocks, and \(L^p\) norms of \(R_2\) for \(p=2,4,8\).  Threshold
times use linear interpolation across the first crossing.

The predefined diagonal joint-limit sequence is

\[
(n,\Delta)=(128,.04),(256,.02),(512,.01),(1024,.005),
(2048,.0025).                                          \tag{4.2}
\]

## 5. Numerical validity gates

All trajectories must remain finite.  For the paired
\(\Delta=.005,.0025\) runs:

1. the 95th percentile across seeds of
   \(\sup_{t\le2}|f_{.005}(t)-f_{.0025}(t)|\), evaluated at common times,
   is at most \(0.01\) at every width;
2. the median absolute paired difference in \(\tau_q\) is at most \(0.01\)
   for \(q=.25,.50,.75,.90\) at every width where both cross;
3. at \(\Delta=.0025\), no single-step loss increase exceeds \(10^{-5}\)
   and the discrete defect
   \(|(f_{k+1}-f_k)/\Delta-2e_kK_k|/(1+2|e_k|K_k)\)
   has median below \(0.01\).

Failure of a gate makes the scientific verdict inconclusive.

## 6. Frozen interpretation

Subject to the validity gates, record **evidence against a polynomially
visible instantaneous jump on the tested range** if all of the following
hold for \(q=.25,.50,.75,.90\), using the finest-step medians:

1. \(\tau_q(2048)/\tau_q(128)\in[0.75,1.25]\);
2. the central log--log width slope of \(\tau_q\) lies in \([-0.10,0.10]\)
   and its bootstrap 95% interval lies in \((-0.20,0.20)\);
3. the maximum difference between the width-median predictor curves at
   \(n=1024\) and \(2048\), on the frozen grid
   \(t\in\{0,.01,.02,.05,.1,.2,.5,1,2\}\), is at most \(0.05\); and
4. both \(K(0)\) and the maximum \(K\) before \(f=.75\) change by a factor
   below \(1.5\) from width 128 to 2048 and have central width slope below
   \(0.20\).

Record **evidence for a visible shrinking boundary layer** if the validity
gates hold and, for each \(q=.25,.50,.75\), the endpoint hitting-time ratio
is below \(0.5\) and the upper bootstrap slope endpoint is below \(-0.20\),
or if the median \(f(.02)\) exceeds \(.75\) at width 2048 while increasing
monotonically over the last three widths.  Any other valid result is
inconclusive.

The first verdict is deliberately not called proof of a mean-field limit.  It
rules out only a boundary layer visible at these widths and polynomial
scales.  The second is evidence, not proof, of discontinuity.

## 7. Branch and stopping rule

No width, seed, horizon, step size, or threshold may be added after inspecting
the result.  If a process fails for resource reasons, retain completed runs,
report the deviation, and stop.  No quadratic-activation control is included:
the exact earlier quadratic model/scaling has not been frozen here, and an
ill-matched positive control would be misleading.
