# Results of the First Two Preregistered Probes

## Claim level

These are reproducible numerical witness results.  H1 strongly discriminates between two proposed weight scales.  Q1 validates an exact normalization and exposes a nonzero response contribution.  Neither result proves preservation of a response norm under training.

## H1: arctangent Hermite tail

The script `hermite_tail_probe.py` computed normalized probabilists-Hermite coefficients with quadrature orders 512, 1024, and 2048 through order 240.  The two highest orders agreed under the preregistered tolerance for every parity-allowed coefficient in the analyzed range.  Parity leakage was below `3e-17`.

For arctangent, a fit on odd orders 9--123 and validation on 125--239 gave:

- root-exponential model validation RMSE: `0.00445` in log coefficient magnitude;
- exponential-in-order model validation RMSE: `0.540`.

For `d(s)=(1+s^2)^{-1}`, the corresponding RMSE values were `0.00767` and `0.533`.

The fitted leading laws were approximately

\[
\log|c_k(\arctan)|
\simeq 0.503-0.994\sqrt{k}-0.789\log k,
\]

\[
\log|c_k(d)|
\simeq 0.141-1.011\sqrt{k}-0.186\log k.
\]

### Interpretation

This decisively rejects an **exponentially weighted chaos-degree norm** as the base space: coefficients decaying like `exp(-c sqrt(k))` cannot belong to any `sum exp(rho k)|c_k|^2` with `rho>0`.  It does not reject a factorial Malliavin-derivative generating norm.  Such a derivative norm can correspond to a root-exponential chaos tail, so the two notions of “analytic radius” must remain distinct.

The result is consistent with rigorous Hermite-approximation theory for functions analytic in a finite strip: arctangent and `d` have their nearest complex singularities at `+/- i`, and strip-analytic functions exhibit root-exponential Hermite convergence under the relevant growth conditions.

## Q1: first adaptive transpose query

The script `adaptive_query_probe.py` evaluated

\[
q=\Gamma^*\left[A(1+(\Gamma\arctan u)^2)^{-1}\right]
\]

for widths 64 through 2048.  It computed the first Malliavin Hilbert--Schmidt response norm both from the exact formula and from independent randomized Jacobian-vector probes.

At width 2048 the replicate means were:

\[
\|q\|_{L^2(\text{coordinates})}=0.795,
\qquad
\|q\|_{L^8(\text{coordinates})}=1.420,
\]

and

\[
E_{2,1}(q)^2=0.748.
\]

The exact response energy decomposed as

\[
0.640\quad\text{(creation/direct derivative)}
\;+
0.108\quad\text{(adaptive response)}
\;-
0.00017\quad\text{(finite-width cross term)}.
\]

The randomized estimate was `0.7482`, agreeing with the exact value.  All recorded coordinate moments through order eight and both response estimates remained tight across the width grid, while their replicate variance decreased.

### Interpretation

The proposed normalization

\[
\frac1n\sum_k\sum_{a,b}|D_{ab}q_k|^2
\]

is dimension-uniform in this first genuinely adaptive transpose cell.  More importantly, the adaptive part is approximately fourteen percent of the total response energy and does not vanish.  A calculus that retains only the fresh/creation part is therefore quantitatively wrong even at initialization.

This is a successful atomic gate, not a flow theorem.  Higher response orders and positive-time preservation remain open.

## Artifacts

- `outputs/hermite_tail/coefficients.csv`
- `outputs/hermite_tail/summary.json`
- `outputs/adaptive_query/raw.csv`
- `outputs/adaptive_query/summary.json`

## K1: Koopman/Taylor growth at arctangent depth two

The script `koopman_taylor_probe.py` implements exact ordinary-power-series arithmetic for the complete finite-width `L=2` ODE.  It was checked in three independent ways:

1. the coefficientwise ODE recurrence had relative residual below `2.1e-16`;
2. the gradient identity
   \[
   (k+1)[t^{k+1}]f=[t^k]\Theta
   \]
   held to relative residual `3.9e-17` in the validation case;
3. order-14 series evaluations agreed with a high-accuracy direct ODE solve to machine precision at times 0.005, 0.01, and 0.02.

The deepest run computed coefficients through order 80 at widths 128, 256, and 512.  At order 80, the median/90th-percentile coefficient roots were:

| width | predictor | predictor q90 | kernel | kernel q90 |
|---:|---:|---:|---:|---:|
| 128 | 3.70 | 4.15 | 3.92 | 4.49 |
| 256 | 3.82 | 3.94 | 4.10 | 4.25 |
| 512 | 3.45 | 3.88 | 3.70 | 4.14 |

Across orders 40--80 the roots grew slowly and appeared to enter a finite range; no reproducible order- or width-divergence was observed.  This means the preregistered simple Koopman witness was **not falsified** at the `L=2` initialization gate.  The data are compatible with a local time-analytic radius of order `0.2--0.25`, but they do not prove one.

The unresolved step is uniformity along positive time and under restarts.  An initial Taylor radius alone does not provide a compact-time theorem.

Additional artifacts:

- `outputs/koopman_taylor/` (order-24 pilot; its recorded absolute recurrence residual is scale-sensitive and is superseded by the relative check)
- `outputs/koopman_taylor_v2/` (order-40 run)
- `outputs/koopman_taylor_v3/` (order-80 validated run)
