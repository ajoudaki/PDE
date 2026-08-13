# Corrected common-clock Loewner result

> **Post-run calibration audit:** the width-256 proxy fails the known exact
> local-coefficient check by about 14%. Its fitted
> `R_proxy(0)=78.0869824`, whereas the exact target has
> `R(0)=68.3866569`; the conditional Padé/local target remains about
> `68.21--68.38` across the tested nodes while the proxy gives
> `77.99--78.08`. Consequently this run is **not calibrated closely enough to
> supply target Loewner evidence**. The matrix calculations remain valid for
> the declared robust proxy, but finite-scope compatibility of that proxy must
> not be promoted to compatibility of the target `K`. See
> `corrected_clock_bias_audit.md`.

## Corrected conclusion

The independent corrected experiment finds **no robust falsification**, but its
14% local-coefficient bias makes the target-level result **inconclusive**, not
meaningful finite-scope compatibility. There is no empirical certificate of
positive semidefiniteness.

The earlier `direct_test_report.md` used feature time `s` as the argument `y`
of `K` and is superseded for Loewner purposes. Its finite-time escape statement
remains valid, but its matrices were not matrices of the intended object. Here
the procedure is instead

\[
s\longmapsto (F_n(s),G_n(s)),\qquad
y=F_n(s),\qquad K_n(y)=G_n(F_n^{-1}(y)).
\]

Because ordinary finite-width expectations are obstructed by rare blow-up, the
objects tested here are the preregistered clipped median-of-means typical
proxies. They are not ordinary expectations.

No independently selected negative direction has a Bonferroni-corrected
bootstrap upper bound below zero. Apparent negative full-sample eigenvalues are
unstable under sample splitting, blocking, or polynomial degree. They therefore
do not count as falsification.

## Scientific run

The exact command was

```text
python studies/stieltjes_conjecture/numerics/direct_loewner/run_corrected_clock_test.py
```

Independent scientific seeds used output nodes

\[
y=(0.04,0.08,0.12,0.16),\qquad
x=(0.0016,0.0064,0.0144,0.0256).
\]

The table reports the primary 7-block, `111*sqrt(n)`-cutoff, degree-3 fit.
`lambda_min` is descriptive on the full sample. `qMq` uses a direction selected
only on the discovery half and evaluated on the confirmation half. `upper` is
the one-sided 5000-resample percentile upper bound at Bonferroni familywise
level 0.01 over the six width-by-matrix tests.

| width | matrix | full `lambda_min` | confirmation `qMq` | bootstrap upper | confirmed negative? |
|---:|:---:|---:|---:|---:|:---:|
| 64 | A | -2.73570 | -7.06e-8 | 0.33336 | no |
| 64 | B | -7.67e-9 | -5.30e-9 | 0.08342 | no |
| 128 | A | -1.12e-3 | 14.9420 | 1893.68 | no |
| 128 | B | -1.04e-8 | -1.46e-8 | 0.03676 | no |
| 256 | A | -7.35e-5 | -4.91e-4 | 1287.79 | no |
| 256 | B | -1.35e-8 | -1.71e-8 | 0.04081 | no |

The very wide `A` bounds are not typographical errors. The discovery minimum
eigenvector has median bootstrap angle about 87.4, 88.2, and 86.2 degrees at
widths 64, 128, and 256: its direction is essentially unreproducible. The `B`
direction is much more stable geometrically, but its effect is only about
`1e-8`; its confidence bounds cross zero and its sign changes under fit-degree
sensitivity.

## Robustness and numerical audit

- No scientific trajectory reached the `1e12` state ceiling through
  `s=0.003`. One width-64 pair touched the primary scalar kernel cutoff; no
  width-128 or width-256 pair was clipped.
- Robust full-sample initial kernels were `148.19`, `133.50`, and `112.07` for
  widths 64, 128, and 256, respectively. The trend toward the exact limiting
  initial value 111 is reassuring but is not a convergence proof.
- Endpoints `F_n(0.003)` were `0.4643`, `0.4149`, and `0.3453`; all frozen
  output nodes were bracketed with margin.
- Degree-3 fit RMS residuals were between `4.28e-9` and `5.55e-9`.
- Direct median-of-means paired `f(s)-f(0)` agreed with integrated robust `G`
  to relative maximum discrepancies `9.3e-8`, `2.0e-3`, and `5.9e-8`. The
  width-128 discrepancy records the fact that coordinatewise medians and time
  integration need not commute; the declared estimand is the integrated `G`.
- Halving the RK4 step changes the fixed-direction statistic by about `0.21`
  bootstrap standard deviations at width 64 and below `2e-8` bootstrap standard
  deviations at widths 128 and 256. The width-64 full matrix is numerically and
  robust-aggregation sensitive; it cannot support a sign claim.
- The two declared cutoffs agree on the confirmation samples because no
  confirmation value is clipped.
- Changing 7 blocks to 5 changes the width-256 `A` confirmation score from
  `-4.91e-4` to `+2.79e-4`.
- Changing polynomial degree flips the tiny `B` sign at every width. Thus none
  of the `B` negatives survives the prespecified sensitivity gate.

At width 256, the proxy `R` is positive and decreasing at all four
nodes:

```text
R  = (78.08087, 78.06259, 78.03240, 77.99069)
R' = (-3.81908, -3.79421, -3.75322, -3.69680)
```

This is only an internal shape property of a proxy whose level is about 14%
wrong. It should not be counted as support for the target Stieltjes constraints,
and it does not settle the nearly null four-point directions.

## Exact controls

The same construction of `A` and `B` was applied to exact atomic Stieltjes
transforms:

| control | `eig(A)` | `eig(B)` |
|---|---|---|
| 2 atoms | `(-9.28e-15, 1.13e-14, 1.36235, 72.61144)` | `(-4.75e-17, 4.58e-17, 0.04030, 2.45447)` |
| 3 atoms | `(3.94e-16, 0.01923, 1.66800, 65.48791)` | `(2.33e-16, 5.94e-4, 0.04257, 2.59726)` |

Only roundoff-scale signs appear at the expected rank deficiencies. This
validates the divided-difference signs and diagonal formulas, while also
showing why `1e-8`-scale target eigenvalues require uncertainty analysis.

## Evidence classification

- **Exact:** the feature equations, `df/ds=G`, the common-clock construction of
  the declared proxy, and the atomic-control matrices.
- **Empirical:** internal finite-scope behavior of the robust proxies at three
  widths and four output nodes. The exact-coefficient calibration failure blocks
  its use as target-level compatibility evidence.
- **Not established:** positive semidefiniteness of the limiting Loewner
  matrices, convergence of the robust proxy to a unique deterministic `K`, or
  existence/uniqueness of a Stieltjes measure.
- **Not a falsifier:** every negative eigenvalue in this run, because it fails
  held-out uncertainty or a preregistered sensitivity gate.

The most informative follow-up would first construct an estimator that recovers
the exact `R(0)=68.3866569` within declared error—preferably by estimating the
low-order common-clock derivative analytically or by a controlled width
extrapolation—before spending more samples on four-point Loewner matrices. The
present `A` minimum direction is too unstable for simply adding more output
nodes to help.

## Artifacts

- `corrected_clock_protocol.md`: frozen corrected protocol.
- `runs/clock_pilot_20260813/`: validity-only pilot, distinct seeds.
- `run_corrected_clock_test.py`: independent scientific runner.
- `runs/corrected_clock_run_20260814/summary.json`: complete numerical summaries,
  matrices, sensitivities, confidence bounds, and controls.
- `runs/corrected_clock_run_20260814/raw_width_*.npz`: per-pair raw curves.
- `runs/corrected_clock_run_20260814/half_step_width_*.npz`: step-halving data.
- `runs/corrected_clock_run_20260814/bootstrap_scores_width_*.npz`: raw held-out
  bootstrap scores.
- `runs/corrected_clock_run_20260814/primary_proxy_width_*.npz`: `F`, `G`, and
  primary matrices.
- `runs/corrected_clock_run_20260814/run.log`: exact run log.
- `runs/corrected_clock_run_20260814/manifest.json`: hashes and byte sizes.

SHA-256:

```text
manifest  20f373cc615f88d8d5055e5504271c195a31e5dd21b197a9eea7cf0c4a0f92da
summary   f5a27e7326ad8e84e9ef4a70979a24fe38c5c299806b834ae023a70f9b71a86b
protocol  0b332f21d8b17f3f804aba879d6aa80a6431d33614c0d79dc1f140888720e433
```
