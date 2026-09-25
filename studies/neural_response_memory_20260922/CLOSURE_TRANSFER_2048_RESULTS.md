# Width-2048 closure transfer: final reported results

Stopped at the user’s request on 2026-09-25; no further experiments are scheduled. All 18 activation/task/P combinations fitted at both the original and half Euler step to training MSE <=1e-8. Two additional refinements fitted, giving 38 fitted runs. A finer SELU quadrant P=1 run hit its time cap before fitting; interrupted extra refinements are excluded from the scores.

Architecture: three hidden layers, width 2048. Activations: ReLU, GELU, SELU. Two circle tasks, eight training samples each, one shared initialization (seed 20260920). The original residual-activity Legendre closure and simultaneous Euler dynamics are retained.

Reported RMS is sqrt(mean((closure-dense)^2)) on 8192 uniformly spaced circle points, at each model’s own first endpoint with training MSE <=1e-8. It is agreement with the fitted dense predictor, not target-function error. Each cell uses its finest completed fitted closure endpoint and the preserved finest fitted dense reference.

| Task | Activation | P=1 | P=2 | P=3 |
|---|---|---:|---:|---:|
| Two outliers | ReLU | 0.180006 | 0.069730 | 0.012589 |
| Two outliers | GELU | 1.309973 | 0.206706 | 0.032047 |
| Two outliers | SELU | 0.167786 | 0.046989 | 0.016324 |
| Quadrant | ReLU | 1.092277 | 0.262672 | 0.022826 |
| Quadrant | GELU | 6.516777 | 0.972281 | 0.390550 |
| Quadrant | SELU | 1.658280 | 0.052751 | 0.146507 |

Fitting transfers to all tested closures. P=3 gives small discrepancies on the outlier task and for ReLU on the quadrant task. GELU quadrant retains a substantial discrepancy, and SELU quadrant is nonmonotone in P. These outcomes do not show a positive training-loss floor.

Numerical qualifications: 14 of 18 comparisons meet the chosen absolute closure step-halving screen (prediction RMS change <=0.01 and maximum change <=0.05). SELU outliers at all three P and SELU quadrant P=1 remain unresolved under that screen. Dense step-halving sensitivity is approximately 0.007–0.008 for ReLU, 0.00021–0.00022 for GELU, and 0.0065 / 0.0203 for SELU outliers / quadrant. Thus the smallest ReLU/SELU discrepancies should not be interpreted as precisely resolved continuous-gradient-flow errors. This is a one-seed finite-width experiment.

All 36 initial and half-step endpoints passed independent physical-matrix replay. The two additional fitted refinements use the same validated solver. Final analysis reports no invalid saved runs. These results remain internally checked study material.

Artifacts: [CSV](../../data/generated/neural_response_memory_20260922/closure_transfer_2048_final01/rms_table.csv), [figure](../../data/generated/neural_response_memory_20260922/closure_transfer_2048_final01/rms_vs_P.png), [complete numerical analysis](../../data/generated/neural_response_memory_20260922/closure_transfer_2048_final01/analysis.json).
