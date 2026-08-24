# Results: preregistered diagonal loop-erasure experiment

**Run date:** 23 August 2026.

**Formal verdict:** **inconclusive**.  The evidence-against rule did not
trigger, but the frozen mechanistic-support rule failed on three horizon-two
cavity slopes (and, under the stricter both-horizons reading, narrowly on the
horizon-one leverage slope).  These computations do not change C-13 or prove
any probabilistic lemma.

## 1. Executed design

The coarse run used widths \(128,256,512,1024\), four independent seeds per
width, horizon \(2\), step \(0.01\), four paired middle-column cavities per
seed, and sixteen sampled top rows.  The solver audit repeated widths
\(128,256\) and all four corresponding seeds at step \(0.005\).  Thus the
coarse and fine datasets contain sixteen and eight main/cavity bundles,
respectively.

For a compact-time diagnostic, the analysis first took the maximum over
checkpoints within each run (and, for cavity quantities, the median of the
four cavity maxima within a seed), then the median across the four seeds at a
width.  Log--log slopes are ordinary least-squares slopes over the four
widths.  This aggregation prevents the four cavities in one seed from being
treated as independent replications.

The raw datasets and mechanical evaluator are:

- `experiment_diagonal_gauge_2026-08-23.jsonl`;
- `experiment_diagonal_gauge_fine_2026-08-23.jsonl`;
- `analyze_diagonal_gauge.py`.

## 2. Numerical-integrator audit

The largest predictor-energy identity defect over every coarse/fine main and
cavity run was

\[
 1.522\times10^{-6}<10^{-4}.
\]

Across all aggregated primary diagnostics at widths \(128,256\), the largest
relative change under step halving was \(1.79\times10^{-9}\), attained by the
top characteristic cavity norm at width \(128\).  The first frozen condition
therefore passed by a wide margin.

## 3. Diagonal return and bath moments

The smallest reported one-percent quantile of either \(\kappa_2\) or sampled
\(\kappa_3\), over all runs and checkpoints, was \(0.640\), well above the
frozen \(0.02\) floor.  The width-median compact-time minima increased mildly:

| width | \(\kappa_{2,.01}\) | sampled \(\kappa_{3,.01}\) |
|---:|---:|---:|
| 128 | 0.826 | 0.749 |
| 256 | 0.847 | 0.787 |
| 512 | 0.865 | 0.801 |
| 1024 | 0.892 | 0.833 |

Every frozen middle-bath moment criterion passed.  For
\(p=2,4,6,8\), the endpoint factors from width 128 to 1024 were
\(1.10\)--\(1.15\), below \(1.5\).  The horizon-two log--log slopes were
negative:

| field | \(p=2\) | \(p=4\) | \(p=6\) | \(p=8\) |
|---|---:|---:|---:|---:|
| \(\|Y_2\|_{p,n}/p\) | -0.030 | -0.034 | -0.039 | -0.039 |
| \(\|C_2\|_{p,n}/p\) | -0.048 | -0.036 | -0.035 | -0.030 |

## 4. Paired-cavity characteristic scale

All four rescaled cavity medians changed by factors below \(1.5\) from width
128 to 1024:

| statistic | width 128 | width 1024 | endpoint factor | horizon-1 slope | horizon-2 slope |
|---|---:|---:|---:|---:|---:|
| \(\sqrt n\|\Delta Z_2\|_n\) | 0.662 | 0.730 | 1.102 | 0.045 | 0.023 |
| \(\sqrt n\|\Delta\Theta(Z_2)\|_n\) | 1.173 | 1.601 | 1.365 | 0.073 | **0.125** |
| \(\sqrt n\|\Delta Z_3\|_n\) | 0.803 | 1.069 | 1.332 | 0.080 | **0.111** |
| \(\sqrt n\|\Delta\Theta(Z_3)\|_n\) | 1.853 | 2.574 | 1.389 | 0.094 | **0.133** |

The bold slopes exceed the frozen \(0.10\) support threshold.  They remain far
below \(0.25\), and none exceeds \(0.25\) at both horizons, so the
evidence-against clause does not trigger.  The pattern is compatible with a
finite-width crossover or with slow genuine growth; four widths and four
seeds do not distinguish them.

## 5. Leverage diagnostic

The largest width-median compact-time leverage ratio was \(1.484<4\).  Its
log--log slope was \(0.0964\) at horizon two and \(0.1038\) at horizon one.
The stated horizon-two compact-interval reading passes the \(0.10\) rule; a
stricter requirement that both auxiliary horizons pass would fail narrowly.
In neither reading does the \(0.25\) evidence-against threshold trigger.

## 6. Frozen-rule disposition

The support conjunction is false because the horizon-two characteristic
cavity slopes are above \(0.10\).  The evidence-against disjunction is also
false because:

1. no bath or rescaled-cavity statistic has slope above \(0.25\) at both
   horizons;
2. neither diagonal-return quantile has slope below \(-0.25\); and
3. the leverage slope is below \(0.25\).

Accordingly the only admissible verdict is **inconclusive but
mechanistically encouraging**.  In particular, the experiment cannot replace
the missing dressed-cavity/signed-nonalignment theorem, and it cannot promote
the finite-width or operator-IDE convergence claims.
