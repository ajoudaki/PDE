# Width-1024 parameter-matched comparison

Both smaller exact-network baselines have lower whole-circle RMS discrepancy
than the constructed dictionary closure at every tested p in both complex
configurations. All 12 pairwise comparisons favor the smaller network at both
numerical levels, and all pass the declared validity gates. This experiment
does not support the proposed closure advantage over parameter-matched smaller
networks on these instances.

Our closure improves as p grows in both cases, but this improvement does not
make it the more efficient approximation among the methods tested here.
Earlier comparisons with random dictionaries remain their own observations;
they do not establish an advantage over ordinary smaller trained networks.

## Design and exact budgets

The full reference is the same bias-free, two-hidden-layer tanh model at
n=1024. Its 1,051,648 scalars are all trained. The two existing cases are eight
tightly spaced alternating labels and six alternating labels with two remote
outliers. Original geometry/labels, full-network seed 20260920, eight equally
weighted training inputs and canonical physical gradient flow are retained.
No new geometry, negative control, seed search or random dictionary was run.

The user selected both parameter definitions explicitly. For dictionary
dimensions K1,K2, the closure has 3n+K1*K2 trained coefficients and additionally
n(K1+K2) fixed dictionary entries. The total model count includes both;
temporary construction arrays, duplicate caches and diagnostic initial copies
are excluded. Actual retained engine memory is recorded separately. A smaller
equal-width exact network has m*m+3m trained/model scalars. Each matching width
is rounded upward to ensure its count is at least the closure's budget.

| p | Dictionary vectors | Closure trained | Closure total | Trained-count match: width / count | Total-size match: width / count |
|---|---:|---:|---:|---:|---:|
| 1 | 8 | 3,087 | 11,279 | 55 / 3,190 | 105 / 11,340 |
| 3 | 45 | 3,422 | 49,502 | 58 / 3,538 | 221 / 49,504 |
| 5 | 149 | 5,760 | 158,336 | 75 / 5,850 | 397 / 158,800 |

Thus sqrt(n times dictionary vectors) is a leading approximation for the total
representation match, not the trained-count match. The exact quadratic count
also includes input/readout weights and the closure's middle coefficient matrix.
Nominal p5 redundant columns remain counted rather than silently discarded.

Small networks use the first m initialized neurons in both layers, with middle
weights scaled by sqrt(1024/m) and readout by 1024/m. Fixed indices preserve the
canonical marginal Gaussian law at m and couple the reference and comparator
without choosing favorable neurons or outcomes. Each network uses its own
width in readout normalization and physical mobilities. This coupling does not
make the initial predicted functions identical.

Every model trains every prescribed block to its own first detected training
MSE 0.001 crossing. RMS compares that endpoint with the full network at its own
crossing, on 8192 uniform circle angles. It is approximation error against the
full network, not error against unseen target labels. See the complete frozen
[protocol](MATCHED_NETWORK_PROTOCOL.md).

## Results: selected finer RMS

| Configuration | p | Ours | Small: trained-count match | Small: total-size match |
|---|---:|---:|---:|---:|
| Tight alternating labels | 1 | 2.211645 | 0.142448 | 0.198671 |
| Tight alternating labels | 3 | 1.296558 | 0.085776 | 0.083395 |
| Tight alternating labels | 5 | 0.828471 | 0.422203 | 0.030361 |
| Alternating labels + two outliers | 1 | 1.068625 | 0.106043 | 0.030427 |
| Alternating labels + two outliers | 3 | 0.445081 | 0.103834 | 0.055154 |
| Alternating labels + two outliers | 5 | 0.417358 | 0.242954 | 0.026768 |

All three approaches fit the training labels, including widths 55,58,75. These
outcomes provide no evidence that these smaller networks lack sufficient
features to fit these cases; they also approximate the full learned function
better in the measured comparisons. The two matches are always reported
separately, with no best-of-two selection.

This is one fixed, coupled initialization on two previously used configurations.
The closure retains information about the entire initial full network in its
dictionary; a small network retains a subset. Success or failure therefore
concerns this finite-realization approximation scheme, not a pure parameter-
count mechanism, population generalization, or a universal capacity theorem.
Small-network error is not monotone across every tested width. No asymptotic
approximation rate follows from these finite experiments.

## Validation and stopping

All 40 base trajectories fitted. All 20 distinct case/model endpoint pairs pass
the two-tolerance maximum-discrepancy limit 0.01; the largest discrepancy is
0.0038649122, for outlier ours p1. No cell qualifies for the numerical-resolution
branch, so no extra trajectory ran. All 18 approximation rows and all 12 pairwise
comparisons are numerically valid, with the same winner at both levels.

The deterministic launch preflight checked exact parameter budgets and ceiling
widths, initial prefix coupling and zero hidden-displacement diagnostics, all
gradient blocks against independent autograd at each of the six small widths,
dictionary algebra and a complete-basis closure/network identity. All13 grouped
checks passed. The final extended checker repeats this preflight successfully
in matched_network_preflight02; the original preflight01 is preserved.

Independent CUDA reconstruction, without importing or reading the analyzer
before freezing its result, passes all 40 raw attempts. It replays initial/final
losses, every saved circle snapshot and8192-angle endpoint, counts, coupling,
dictionary algebra, grids, execution metadata and hashes. Maximum endpoint
replay discrepancy is 8.11e-15; the nested 4096/8192 RMS change is at most 4.45e-16,
and sampled maximum-error change at most 7.77e-6. These are operational numerical
checks, not certified exact-flow error bounds. Full evidence and limitations:
[independent report](matched_network_check.md).

The new training used 496.17049358040094 summed worker seconds; cumulative
scaling/width4096/this extension spend 3390.744892962277 of 6000, leaving
2609.255107037723 unused. No reservation or further training remains. All
workers exited0. Exact commands, sources and accounting are in
[execution record](MATCHED_NETWORK_RUN_RECORD.md).

## Reproducible evidence and figures

All generated products are under
data/generated/random_dictionary_learned_circle_20260920/:

- matched_network_primary01 and matched_network_refined01: configs, full saved
  states, dictionaries, endpoint/snapshot predictions, every accepted loss/time,
  summaries, completions and producer hashes.
- matched_network_analysis01: all 18 metric rows at both levels,12 separate
  comparisons, raw-attempt validation, selected endpoints, pointwise arrays,
  tables and source/input/output provenance.
- matched_network_independent01: independent 40-attempt reconstruction and
  comparison results; matched_network_preflight01/02 retain deterministic checks.
- matched_network_logs01: exact process logs and completed budget accounting.
- matched_network_plots01: two RMS figures with linear dictionary-vector and
  logarithmic error axes, two training-loss figures, PDF/SVG/PNG exports,
  selected data CSVs and provenance. Parameter counts/widths appear in the figures.
- matched_network_radial01: saved finer endpoint curves and interactive viewer,
  with configuration/p selectors, actual widths and both budgets. Curves use
  every eighth 8192-angle value, rounded to six decimals; displayed RMS values
  retain the full saved 8192-angle computation. The radial scale is fixed across
  p within each configuration, with signed values offset from a zero-output ring.

Saved-data export checking confirms all 20 radial curves, 18 RMS rows,
40 selected loss traces and 76,237 loss samples exactly, with current hashes
and parameter counts. Browser checks pass all six configuration/p choices,
legend toggles, hover/pin interactions and light/dark layouts at 320, 360 and
736 pixels, with no script errors or overflow. All four static figures and
representative radial views were visually inspected. Full evidence is in
matched_network_preview01. The independent raw/analysis agreement check also
matches all 36 model-level metric records, all 20 selections and all 12 verdicts.
Results remain study-owned empirical evidence; no promotion to established
theory or maintained code is implied.
