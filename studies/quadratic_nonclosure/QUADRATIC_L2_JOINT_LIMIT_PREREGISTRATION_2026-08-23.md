# Preregistered experiment: quadratic L=2 joint width/step limit

**Frozen before implementation and execution:** 23 August 2026.

## 1. Decision question

For the exact two-hidden-layer quadratic laboratory underlying the
conditional step-loss conjecture, does ordinary simultaneous gradient
descent show a shrinking initial boundary layer as width \(n\to\infty\) and
step size \(\Delta\downarrow0\), qualitatively unlike the depth-three arctan
control?

Physical time is \(t=k\Delta\); \(\Delta\) is the discrete learning step and
there is no additional learning-rate multiplier.

## 2. Canonical model

The activation is the audited convention

\[
 \phi(v)=\frac12v^2.
\]

For one input and equal width \(n\), put

\[
 h_i=\frac12x_i^2,qquad z_j=\sum_iW_{ji}h_i,qquad
 f_n=\frac1{2n}\sum_ja_jz_j^2,qquad \mathcal L_n=(1-f_n)^2.
\]

Independently initialize

\[
 x_i,a_j\sim N(0,1),qquad W_{ji}\sim N(0,1/n).
\]

Writing \(e=1-f\) and \(\nu=a\odot z\), one exact simultaneous metric-GD
step is

\[
\begin{aligned}
a^+&=a+2\Delta e\,(z^2/2),\\
x^+&=x+2\Delta e\,\{x\odot W^{\mathsf T}\nu\},\\
W^+&=W+\frac{2\Delta e}{n}\nu h^{\mathsf T}.
\end{aligned}                                           \tag{2.1}
\]

All fields in (2.1) are evaluated at the old state.  This is the exact model
and \(\mu\)P metric in the quadratic audit, with \(\gamma=1\).  There is no
clipping, normalization, regularization, or planted extreme neuron.

The exact metric tangent kernel recorded at every step is

\[
 \kappa_n=\frac14\langle z^4\rangle_n
 +\langle h^2\rangle_n\langle(a z)^2\rangle_n
 +\left\langle\{x\odot W^{\mathsf T}(az)\}^2\right\rangle_n. \tag{2.2}
\]

Consequently the continuous physical flow obeys \(\dot f=2e\kappa_n\).

## 3. Competing hypotheses

**Regular-flow hypothesis.**  After resolving the step size, predictor/loss
curves, threshold times, and \(\kappa_n\) stabilize with width, as they did in
the arctan control.

**Visible boundary-layer hypothesis.**  For every fixed \(q<1\),

\[
 \tau_q(n,\Delta)=\inf\{k\Delta:f_k\ge q\}
\]

shrinks with width after step-size resolution.  The raw kernel or its
readout-tail concentration grows correspondingly.  A sufficiently strong
trend would be qualitatively consistent with the conditional trace
\(f(0)=0,f(t)=1\) for \(t>0\).

An intermediate or slowly varying trend is inconclusive.  The tagged-site
step trace is conditional, so failure to see a boundary layer would weigh
against its visibility at attainable widths, not mathematically refute it.

## 4. Frozen design

- widths \(n\in\{128,256,512,1024,2048\}\);
- steps \(\Delta\in\{.02,.01,.005,.0025,.00125\}\);
- six initialization keys \(8101,\ldots,8106\), paired across step sizes and
  independent across widths via `SeedSequence([key,n,20260824])`;
- physical horizon \(T=2\);
- thresholds \(q\in\{.10,.25,.50,.75,.90,.95\}\);
- float64, exact dense matrices, at most six CPU workers;
- 30 minutes, 1 GiB output, and no post-result extension.

Record every step: predictor, loss, the three blocks of (2.2),
\(\|a\|_\infty,\|x\|_\infty,\|z\|_\infty\), and the fraction of the
readout-kernel block carried by its largest coordinate.

The matched simultaneous sequence is

\[
(n,\Delta)=(128,.02),(256,.01),(512,.005),(1024,.0025),
(2048,.00125).                                         \tag{4.1}
\]

## 5. Numerical validity

For \(\Delta=.0025\) versus \(.00125\):

1. all finest-step trajectories must remain finite through the first
   \(f=.95\) crossing or through \(T=2\);
2. at every width, the 95th percentile of the paired maximum predictor
   discrepancy is at most \(.01\);
3. median paired hitting-time differences are at most \(.005\) for
   \(q=.25,.50,.75,.90\);
4. at the finest step, no loss increase exceeds \(10^{-5}\), and the median
   normalized defect in \((f_{k+1}-f_k)/\Delta=2e_k\kappa_k\) is below .01.

Coarser trajectories may fail from explicit-step instability without
invalidating the fine comparison; such failures must be retained and
reported.  Failure of a fine gate makes the scientific verdict inconclusive.

## 6. Frozen interpretation

Conditional on numerical validity, record **the same regular-flow signature
as the arctan control** if for \(q=.25,.50,.75,.90\):

1. \(\tau_q(2048)/\tau_q(128)\in[.75,1.25]\);
2. the central log--log slope is in \([-.10,.10]\) and its bootstrap 95%
   interval lies in \((-.20,.20)\);
3. the maximum difference between the \(n=1024\) and \(2048\) median curves
   on \(t\in\{0,.005,.01,.02,.05,.1,.2,.5,1,2\}\) is at most .05; and
4. both \(\kappa(0)\) and the maximum \(\kappa\) before \(f=.75\) change by
   a factor below 1.5 from width 128 to 2048 and have central slope below .20.

Record **evidence for a visible shrinking boundary layer** if the fine gates
pass and, for each \(q=.25,.50,.75\), the endpoint hitting-time ratio is
below .5 and the upper bootstrap slope endpoint is below -.20, or if median
\(f(.01)>.75\) at width 2048 while increasing monotonically over the last
three widths.  Any other result is inconclusive.

The boundary-layer verdict is evidence, not construction of the asserted
mean-field trace.  The regular verdict does not disprove a tail-driven layer
that shrinks more slowly than the accessible widths.
