# Preregistration: endpoint-weighted off-column response

**Frozen before generation of the data described here:** 23 August 2026.

## Question

The feeding two-cavity proof reduces the remaining row multiplier to the
off-column field

\[
 (1+|A_0|)\odot C_j\,D_{\Gamma_{2,·j}}X_2(t),
\]

where \(C_j\) is the static second bulk with column \(j\) set to zero.  Does
its normalized Hilbert--Schmidt scale remain width-stable even after the
endpoint Gaussian weight, or does it acquire the \(\sqrt{\log n}\) growth
allowed for an arbitrary anticipative direction?

This is a mechanism diagnostic only.  A pass cannot prove the two-cavity
lemma; a fail can reject its proposed weighted-norm form.

## Frozen simulation

- Exact model: the fully trained, bias-free, one-sample, three-hidden-layer
  arctan feature-time flow in the frozen core contract.
- Integrator: midpoint RK2.
- Main step: \(h=0.01\); independent paired solver audit: \(h=0.005\).
- Horizons: \(s=1,2,4\).
- Widths and independent networks in the main run:
  \((256,64),(512,32),(1024,16),(2048,8)\).
- Four independent Rademacher probes per network and one tagged static
  \(\Gamma_2\) column.  Exchangeability permits using column zero.
- Central feeding perturbation:
  \(\Gamma_{2,·0}\mapsto\Gamma_{2,·0}±
  \varepsilon v/\sqrt n\), with \(\varepsilon=0.002\).  Both perturbed
  networks are trained fully; this is not a passive probe.
- Perturbation audit: common draws with \(\varepsilon=0.001\) at widths
  256 and 512, eight networks each, step \(0.005\).
- Arithmetic audit: the same small block in float64, using common float64
  initial draws before casting in the float32 branch.

For each probe, set

\[
 J_X=\frac{X_2^+-X_2^-}{2\varepsilon},\qquad
 Y=C_0J_X.
\]

After averaging \(Y_i^2\) over the four probes, record

\[
 F_C=\Big(\sum_i\overline{Y_i^2}\Big)^{1/2},\quad
 F_A=\Big(\sum_i(1+|A_{0,i}|)^2\overline{Y_i^2}\Big)^{1/2},
 \quad Q_A=F_A/F_C,
\]

as well as the inverse participation ratio and top-one-percent mass of the
weighted row energy.  The same statistics are recorded with \(J_X\) replaced
by the full \(B_3\) response for comparison with the earlier experiment.

## Numerical validity rule

At every common width and horizon, the coarse/fine and epsilon/2 relative
differences of \(F_C,F_A,Q_A\) must be at most 5 percent; differences below
\(10^{-6}\) in both values pass absolutely.  The float32/float64 relative
difference must be at most 2 percent.  If a horizon fails, no formal
interpretation is made there and the main run is repeated at half step before
any scientific reading.

## Frozen interpretation

Use a network-cluster bootstrap with 2,000 resamples and report log--log width
slopes with 95-percent percentile intervals.

Formal support for the proposed weighted two-cavity scale requires, at both
horizons 2 and 4,

1. the upper confidence endpoint of the \(F_A\) width slope is below 0.15;
2. the upper confidence endpoint of the \(Q_A\) width slope is below 0.10;
3. the median \(Q_A\) at width 2048 is at most 1.25 times its value at width
   256.

Formal evidence against requires, at a numerically valid horizon,

1. the lower confidence endpoint of the \(F_A\) slope exceeds 0.30; and
2. the width-2048 median \(Q_A\) exceeds 1.35 times the width-256 median.

Any other result is inconclusive.  Localization statistics are descriptive
and cannot override these frozen rules.

