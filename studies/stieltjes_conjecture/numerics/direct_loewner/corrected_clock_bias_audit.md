# Local-coefficient audit of the corrected robust proxy

## Revised conclusion

The common-clock coordinate correction was necessary, but the resulting
finite-width robust proxy is too biased to provide evidence about the target
Loewner matrices. The run remains useful as a diagnostic of this proxy only.

The exact target coefficient supplied by the analytical calculation is

\[
R(0)=\kappa_1=68.3866569,
\qquad K_{yy}(0)=2\kappa_1=136.7733138.
\]

Refitting the saved width-256 primary curve by the frozen degree-3 procedure
and evaluating at zero gives

\[
R_{256}^{\rm proxy}(0)=78.0869824,
\qquad K_{yy}^{\rm proxy}(0)=156.1739648.
\]

Thus the local error is

\[
78.0869824-68.3866569=9.7003255,
\qquad
\frac{9.7003255}{68.3866569}=14.1845\%.
\]

Across the four tested nodes the proxy is `77.9907--78.0809`, whereas the exact
local/conditional-Padé range is about `68.21--68.38`. Depending on endpoints,
the discrepancy is `9.61--9.87`, or `14.05%--14.47%`.

## The additive restoration is not the cause

The proxy used

\[
K^{\rm corr}(y)=111+G(s(y))-G(0),
\qquad
R^{\rm proxy}(x)=\frac{G(s)-G(0)}{F(s)^2}.
\]

Subtracting `G(0)` and adding 111 fixes only the constant value
`K_corr(0)=111`; it does not alter curvature. The robust width-256 initial
value was already close to the limit:

\[
G_{256}(0)=112.0680243,
\qquad (G_{256}(0)/111)^2=1.0193363.
\]

Near zero,

\[
R^{\rm proxy}(0)=\frac{G_{ss}(0)}{2G(0)^2}.
\]

The implied feature-time curvatures are

\[
G_{ss}^{\rm exact}(0)=2(68.3866569)(111)^2=1{,}685{,}183.9993,
\]

\[
G_{ss}^{\rm proxy}(0)=2(78.0869824)(112.0680243)^2
=1{,}961{,}426.6293,
\]

so the proxy feature-time curvature is `16.3924%` high. If one merely replaced
the proxy clock slope 112.068 by 111 while retaining this curvature, the inferred
coefficient would increase to `79.5969`, not move toward 68.3867. The dominant
error is therefore the finite-width/robust curvature estimate, not constant
centering.

## Why a good `G(0)` did not calibrate the slope

At width 256 the seven block initial means were

```text
(156.82, 112.07, 109.77, 103.77, 121.57, 137.78, 97.54).
```

The coordinatewise median selected the second block at all 61 feature-time
grid points; it did not switch blocks in this width. But local coefficients
estimated separately from the seven ten-pair block means ranged from `69.43`
to `84.32`, with median `81.22`. The selected block happened to have
`R_proxy(0)=78.09`. Selecting a block because its kernel *level* is median does
not make its curvature a consistent median or mean curvature estimate.

Alternative aggregations on the same saved width-256 data remain biased:

| aggregation | `G(0)` | fitted `R(0)` | relative error |
|---|---:|---:|---:|
| 7-block median-of-means | 112.0680 | 78.0870 | +14.18% |
| 5-block median-of-means | 115.1450 | 75.8646 | +10.93% |
| full arithmetic mean | 119.9014 | 81.7716 | +19.57% |
| discovery 7-block proxy | 112.2714 | 79.0383 | +15.58% |
| confirmation 7-block proxy | 113.8930 | 83.7400 | +22.45% |

The primary fitted coefficients at widths 64, 128, and 256 were respectively
`94.6247`, `90.9843`, and `78.0870`, or `+38.37%`, `+33.04%`, and `+14.18%`
relative to the exact coefficient. This suggests decreasing finite-width bias,
but three noisy widths do not justify an extrapolation.

The construction `F=integral G_robust` also need not equal a robust typical
mean output because coordinatewise median aggregation and integration do not
generally commute. At width 128 the selected median block changes once and the
direct robust `f` curve differs from integrated `G` by about `0.2%`. At width
256 the median block does not switch and that clock discrepancy is below
`6e-8` relative, so it cannot explain the 14% coefficient error there.

## Evidence downgrade

- The previous negative-eigenvalue non-confirmation remains valid: this run did
  not falsify the conjecture.
- The stronger phrase “finite-scope compatibility of the target” is withdrawn.
  The experiment establishes only internal properties of a biased robust proxy.
- Even a perfectly positive proxy Loewner matrix would not be persuasive until
  the estimator reproduces the known exact local coefficient within its stated
  uncertainty.
- No new scientific simulation was used in this audit; every number above was
  recomputed from the saved run artifacts.
