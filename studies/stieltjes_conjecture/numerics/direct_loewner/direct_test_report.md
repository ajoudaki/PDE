# Direct Loewner test: preregistered result

> **Superseded coordinate warning (2026-08-12):** this report incorrectly
> treated feature-flow time `s` as the output argument `y` of the intended
> object `K(y)=G(F^{-1}(y))`. Its escape calculation remains a valid statement
> about finite-width feature trajectories, but its four-node design did **not**
> test the intended Loewner matrices. No conclusion about those target matrices
> should be drawn from this report. The corrected conditional experiment first
> forms robust ensemble curves `F(s),G(s)`, eliminates their common clock, and
> is documented separately in `corrected_clock_protocol.md`.

## Outcome

The preregistered four-node, wrong-coordinate test is **inconclusive because its numerical
validity gate failed before any target Loewner matrix could be formed**. This is
not finite-scope evidence for or against positive semidefiniteness.

The exact superseded command was

```text
python studies/stieltjes_conjecture/numerics/direct_loewner/simulate_loewner.py \
  --output studies/stieltjes_conjecture/numerics/direct_loewner/runs/run_20260812
```

At width 64, the primary run produced nonfinite trajectories before all four
nodes and stopped as prescribed. A direct reproduction showed the number of
antithetic pairs with finite `K` at
`y=(0.02,0.04,0.06,0.08)` to be `(62,6,1,0)` under `h=0.001`. For the first
eight pairs, both `h=0.001` and `h=0.0005` gave `(6,0,0,0)`. Because no pair
reaches all nodes, neither `A` nor `B` exists for the stipulated ensemble of
replicates. Dropping exploded pairs would condition on survival and change the
observable.

The failed command log is `runs/run_20260812/run.log`. The later command

```text
python studies/stieltjes_conjecture/numerics/direct_loewner/diagnose_blowup.py \
  --output studies/stieltjes_conjecture/numerics/direct_loewner/runs/failure_diagnostic_20260812
```

is explicitly a post-failure numerical diagnosis, not a replacement primary
test. It stops trajectories once any component reaches magnitude `1e12`, saves
all crossing times and initial quantities, and does not compute selected-survivor
Loewner matrices.

## Escape summary

Counts below are antithetic pairs remaining below the `1e12` escape ceiling at
the four frozen `y` nodes:

| width | pairs | main step `0.001` | half step `0.0005`, first 8 pairs |
|---:|---:|---:|---:|
| 64 | 96 | `(61, 6, 1, 0)` | `(6, 0, 0, 0)` |
| 128 | 64 | `(38, 0, 0, 0)` | `(5, 0, 0, 0)` |
| 256 | 32 | `(17, 0, 0, 0)` | `(4, 0, 0, 0)` |

For the same first eight pairs at each width, changing from `h=0.001` to
`h=0.0005` changes each recorded threshold-crossing time by at most `0.001`.
Thus halving the step does not restore survival and the escape is not explained
by the originally chosen RK4 step.

Median times at which any component first crosses `1e12`, using all raw
trajectories (the two signs counted separately), are `0.028`, `0.0255`, and
`0.024` at widths 64, 128, and 256. For the guaranteed-positive-`f(0)` member
of each antithetic pair, the corresponding medians are `0.023`, `0.022`, and
`0.021`.

## Exact structural explanation

Let `theta=(a,W,u)` and `q=||theta||^2`. The stated equations are exactly

\[
\dot\theta=n\nabla f.
\]

Under simultaneous scaling of all coordinates, `f` is homogeneous of degree
seven: `f(c theta)=c^7 f(theta)`. Euler's identity therefore gives

\[
\theta\mathbin\cdot\nabla f=7f.
\]

Along the ascent flow,

\[
q'=14nf,
\qquad
q''=14n^2\lVert\nabla f\rVert^2
\ge \frac{14n^2(\theta\cdot\nabla f)^2}{q}
=\frac72\frac{(q')^2}{q}.
\]

If `f(0)>0`, then `q'(0)>0`. Writing `v=q'` and integrating the differential
inequality gives

\[
v(q)\ge v(q_0)(q/q_0)^{7/2},
\qquad
T_{\rm blow}\le\frac{2q_0}{5v(q_0)}
=\frac{q_0}{35n f(0)}<\infty.
\]

Changing `a(0)` to `-a(0)` changes the sign of `f(0)` and leaves `q_0` and
`K_n(0)` fixed. Consequently every antithetic pair has one member for which
finite-time blow-up is guaranteed.

Moreover Gaussian initialization has positive density on every finite point.
Scaling any configuration with positive `f` by `c` changes the displayed upper
bound by `c^{-5}`. Hence, at every finite width and for every positive time,
there is positive Gaussian probability of blow-up before that time. If the
observable is extended by `+infinity` after escape, its ordinary finite-width
expectation is infinite; without such an extension it is not defined on the
whole sample space.

This is an exact obstruction to an unqualified finite-width Monte Carlo
interpretation. It does **not** by itself disprove an object defined by taking
`n -> infinity` first, by formal coefficient extraction at time zero, by a
stopped/truncated flow, or by another explicitly stated continuation. Those are
different limit/observable contracts and must be declared before another
direct test.

## Positive Stieltjes controls

The matrix implementation was independently exercised on the frozen exact
atomic controls. Eigenvalues in increasing order were:

| control | `eig(A)` | `eig(B)` |
|---|---|---|
| 2 atoms | `(-7.72e-14, -1.17e-14, 0.3830, 125.4791)` | `(1.29e-16, 4.06e-16, 0.01464, 3.28293)` |
| 3 atoms | `(9.23e-15, 9.09e-4, 0.81398, 117.14210)` | `(-3.30e-16, 4.68e-5, 0.01736, 3.33245)` |

The nominally negative values are `1e-13`--`1e-16` roundoff at exact rank
deficiency. They demonstrate why an uncertified floating-point negative
eigenvalue must not be called a falsification. The complete matrices, nodes,
weights, and transform derivatives are in
`runs/failure_diagnostic_20260812/failure_summary.json`.

## Artifact map

- `protocol.md`: frozen design and decision rule.
- `simulate_loewner.py`: model, observable, analytic derivative, Loewner
  construction, split confirmation, and controls.
- `runs/run_20260812/run.log`: aborted primary command log.
- `diagnose_blowup.py`: post-failure escape diagnostic.
- `runs/failure_diagnostic_20260812/trajectory_escape.csv`: raw per-trajectory
  initial values, crossing times, survival flags, and surviving `K` values.
- `runs/failure_diagnostic_20260812/escape_*.npz`: exact raw arrays.
- `runs/failure_diagnostic_20260812/failure_summary.json`: summaries and control
  matrices.
- `runs/failure_diagnostic_20260812/manifest.json`: byte sizes and SHA-256 hashes.

The SHA-256 hashes of the diagnostic manifest and summary are respectively
`d4ca00350fbeb8e66723439bc8b51ee189152c96888f6f93678d878cdc55b8f0` and
`01c6b35009885a096a84f00cc04447839b61673dc5db6839b8fe863cb492513d`.
