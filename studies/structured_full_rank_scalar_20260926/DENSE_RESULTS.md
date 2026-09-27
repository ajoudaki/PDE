# Dense structured initialization: predicted-function comparison

**Outcome: the tested structured initializations do not reliably reproduce the particular canonical Gaussian network’s fitted circle function across the suite. HD and D1 H D2 H D3 are close on several easy tasks, but retain substantial discrepancies on clustered and oscillatory tasks.**

This conclusion concerns the predicted functions themselves, not their errors against a teacher. The user explicitly corrected this criterion during the run, before completed-data analysis. No candidate, seed, task or trajectory was changed.

## Completed experiment

2016 dense training runs: twelve circle tasks, widths128 and256, twelve paired seeds, and seven middle initializations. First-layer and readout initial weights are shared within each pair; middle matrices are independent draws under their respective laws. Every middle entry trains freely. Both networks are fully dense throughout training. This tests independent structured replacement, not an optimized coupling or approximation to a given Gaussian matrix. FD was not tested.

All runs reached physical time300. Nine task designs reached training MSE<=1e-6 for every method/width/seed;503 of504 runs on the remaining three designs did not. The latter are not called fully fitted. The user requested the report immediately, so the continuation and long-horizon refinement campaigns were interrupted; partial extension outputs are not used in these results.

For each paired seed, the metric is RMS_circle(f_structured-f_Gaussian)/RMS_circle(f_Gaussian), evaluated on4096 directions. Matched-fit comparisons use each network’s first MSE<=1e-6 endpoint. Common-time comparisons and the tighter1e-8 endpoints are reported separately.

## Fitted-function discrepancies at width256

Entries are mean relative function RMS percentages over12 seeds. All nine tasks below have matched fitted endpoints. No teacher error appears in this table.

| Task | HD | D1 H D2 H D3 | Fastfood | Four reflections | Diagonal |
|---|---:|---:|---:|---:|---:|
| pair_cos1 | 1.98% | 2.05% | 3.42% | 2.54% | 2.59% |
| pair_cos3 | 1.40% | 1.26% | 1.29% | 1.79% | 1.74% |
| near_pair_sin9 | 1.21% | 0.95% | 1.35% | 1.39% | 1.38% |
| triple_cos3 | 3.50% | 4.00% | 6.98% | 6.35% | 8.93% |
| triple_mixed | 1.10% | 0.89% | 1.61% | 0.95% | 0.93% |
| cluster_triple_cos9 | 6.74% | 7.45% | 11.29% | 12.99% | 17.07% |
| alternating3 | 1.89% | 1.87% | 3.10% | 2.20% | 2.47% |
| alternating5 | 4.21% | 3.54% | 5.89% | 4.56% | 4.42% |
| alternating9 | 10.28% | 8.02% | 11.29%† | 8.94% | 9.25% |

† Fastfood on alternating9 has unresolved time-step warnings: seed4 showed a loss-increasing step at both widths. These cells are not numerically certified. All other main trajectories passed the loss-rise screen.

For D1 H D2 H D3 at width256, the clustered-three-point discrepancy is7.45% on average (95% paired bootstrap interval6.53–8.46%), with worst seed10.51%. On alternating9 it is8.02% (6.83–9.45%), with worst seed13.96%. The latter has mean absolute function RMS discrepancy0.06179, against Gaussian function RMS0.76984; its worst sampled pointwise discrepancy across seeds is0.46295. Thus small training loss does not imply agreement away from training points.

Width128 makes these two D1 H D2 H D3 discrepancies9.30% and13.09%, respectively. Increasing width helps in these cases, but two widths do not establish eventual equivalence or a convergence rate. Tightening the fitting threshold to1e-8 changes the width256 numbers only to7.44% and8.05%; early stopping is not the explanation.

HD and D1 H D2 H D3 have almost equal average discrepancies across the completed common-time suite (3.27% each), but that average hides the hard-task failures. No candidate passes the descriptive5% mean-error screen on every fitted task/width. The5% threshold is an explicit reporting convention, not a user-imposed tolerance or a theorem. Independent Gaussian-vs-Gaussian variability is contextual only and does not excuse a discrepancy from the chosen reference.

## Numerical support and limits

The canonical RHS was checked against maintained finite-network code. All42 planned early half-step pairs passed: maximum saved-function discrepancy was3.411e-5 times teacher RMS. This is a numerical-error scale, not the scientific success metric. All paired function quadrature checks passed when comparing4096 with2048 directions. The grid maximum is sampled, not a certified continuous supremum. The two Fastfood warnings above remain unresolved. No long-horizon numerical conclusion is claimed.

The slow broad_ridge6, sharp_ridge8 and multiscale12 designs have valid common-time300 comparisons in the full tables; their final fitted comparisons remain unresolved. No scalar closure was tested. These finite-width independent-replacement results neither prove scalar incompressibility nor validate a Gaussian-preserving structured substitute.

## Reproducible artifacts

- [Complete function report](../../data/generated/structured_full_rank_scalar_20260926/dense_main_function_analysis_20260926/report.md), including all tasks, widths, seeds, confidence intervals and numerical gates. Its historical teacher-risk appendix is not used for this conclusion.
- [Machine-readable function table](../../data/generated/structured_full_rank_scalar_20260926/dense_main_function_analysis_20260926/function_summary.csv).
- [Protocol](DENSE_PROTOCOL.md), [dense core](dense_compare.py), [driver](run_dense_comparison.py), [analysis](analyze_dense_comparison.py).
- Principal raw results and source snapshot: `data/generated/structured_full_rank_scalar_20260926/dense_main_20260926/`.
- No maintained scientific book/code changes or Git commits were made.
