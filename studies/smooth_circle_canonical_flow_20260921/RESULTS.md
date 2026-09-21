# Smooth mixed-frequency circle: canonical-flow results

Against width55: **strong separation not observed**. Closure/dense median terminal training RMSE ratio: 0.834186.

Against width105: **strong separation not observed**. Closure/dense median terminal training RMSE ratio: 0.987341.

All three models fitted all three seeds. At the common terminal time, the closure had a 16.6% lower median RMSE than width55 and a 1.27% lower median RMSE than width105. This small descriptive accuracy advantage was not consistent across every individual seed: on seed 20260921 both dense networks had lower terminal error than the closure. At the saved checkpoints, width105 reached the fitting threshold by time 100 on all seeds, while the closure first met it at time 160 on all seeds.

These are descriptive results for the three fixed seeds 20260921–20260923, the explicit finite initialized dictionary, and physical time 1000. They do not establish a representation lower bound, a population approximation theorem, a nonlazy theorem, or an all-time advantage.

The fixed regression target is `sqrt(32/21)*(cos(theta)+sin(3*theta)/2+cos(5*theta)/4)`, with unit mean square. Training uses 126 equally spaced unit-circle x values and u=x/sqrt(2); the passive panel uses 1024 midpoint angles. Both hidden layers use tanh, canonical Gaussian initialization, unhalved squared loss, and raw block mobilities (n,1,n).

| Model | Trainable / retained predictor scalars | Fits / 3 | Median training RMSE | Median passive RMSE | Numerical gates |
|---|---:|---:|---:|---:|---|
| width55 | 3190 / 3190 | 3 | 0.00342535 | 0.00342535 | pass |
| closure1024 | 3087 / 11279 | 3 | 0.00285738 | 0.00285738 | pass |
| width105 | 11340 / 11340 | 3 | 0.00289401 | 0.00289401 | pass |

A fit means MSE≤0.001. The strong-separation rule additionally requires closure fits on at least two seeds, dense fits on no seeds, and a closure median RMSE at most one third the dense median. Error ratios remain informative when that conjunction fails; fitting by both methods does not by itself imply equal accuracy or equal fitting time.

| Model | Seed | Level | Last saved t | Training RMSE | Passive RMSE | First saved fit t | Hidden RMS motion (layer 1, 2) |
|---|---:|---|---:|---:|---:|---:|---|
| width55 | 20260921 | fine | 1000 | 0.00337525 | 0.00337525 | 100 | 0.416072, 0.465914 |
| width55 | 20260922 | fine | 1000 | 0.00420695 | 0.00420695 | 160 | 0.509613, 0.541257 |
| width55 | 20260923 | fine | 1000 | 0.00342535 | 0.00342535 | 160 | 0.488773, 0.508378 |
| closure1024 | 20260921 | fine | 1000 | 0.00342653 | 0.00342653 | 160 | 0.570214, 0.303734 |
| closure1024 | 20260922 | fine | 1000 | 0.00285738 | 0.00285738 | 160 | 0.594914, 0.359207 |
| closure1024 | 20260923 | fine | 1000 | 0.00281273 | 0.00281273 | 160 | 0.571031, 0.294492 |
| width105 | 20260921 | fine | 1000 | 0.00234484 | 0.00234484 | 100 | 0.416725, 0.469839 |
| width105 | 20260922 | fine | 1000 | 0.0032082 | 0.0032082 | 100 | 0.468415, 0.49662 |
| width105 | 20260923 | fine | 1000 | 0.00289401 | 0.00289401 | 100 | 0.478443, 0.528455 |

First saved fit times only bracket a crossing between the preceding checkpoint and the displayed time. `endpoints.csv` retains those brackets. Missing fit times mean no saved checkpoint met the threshold. Hidden motion is descriptive.

Fourier coefficients on each panel are `a_k=2 mean(f cos(k theta))` and `b_k=2 mean(f sin(k theta))`. Harmonic loss is `((a_k-a_target)^2+(b_k-b_target)^2)/2`; outside energy is the mean square after removing the predicted harmonics 1,3,5. Their sum reconstructs the total MSE to roundoff. Full per-seed coefficients, coefficient errors and outside energies for both panels are in `harmonics.csv`; every saved time appears in `checkpoints.csv` and `analysis.json`.

At time 1000, all models recovered all three target harmonics accurately. The median coefficient error energies were:

| Model | Harmonic 1 | Harmonic 3 | Harmonic 5 | Outside energy |
|---|---:|---:|---:|---:|
| width55 | 8.20830e-10 | 1.17732e-8 | 1.17918e-7 | 1.15661e-5 |
| closure1024 | 3.61814e-11 | 1.84700e-9 | 5.92271e-8 | 8.10858e-6 |
| width105 | 7.09852e-10 | 6.68697e-9 | 6.66934e-8 | 8.29756e-6 |

Training and passive values agree at the displayed precision; the complete coefficients and their cosine/sine errors on each panel are retained in the CSV. Across the nine selected model/seed runs, frequencies outside 1, 3, 5 account for 98.58–99.31% of terminal training MSE. Thus the remaining error is mainly extra frequency content, rather than a failure to learn the third or fifth target harmonic. Agreement of these two finite panels is not a whole-circle error certificate.

![Loss versus physical time](../../data/generated/smooth_circle_canonical_flow_20260921/analysis01/loss_physical_time.png)

![Harmonic losses](../../data/generated/smooth_circle_canonical_flow_20260921/analysis01/harmonic_loss.png)

![Final passive predictions](../../data/generated/smooth_circle_canonical_flow_20260921/analysis01/final_circle_prediction.png)

The physical-time and harmonic plots show medians and ranges across the fixed seeds; these ranges are not confidence intervals. Cost curves retain each seed separately. Corresponding PDF files are provided for export.

Across all retained refinement comparisons, the largest saved prediction discrepancy was 2.42733e-06 and the largest RMSE discrepancy was 1.43608e-08. Failed coarse comparisons remain recorded; the selected pair alone determines resolution acceptance.

| Model | First-seed reproduction |
|---|---|
| width55 | pass |
| closure1024 | pass |
| width105 | pass |

The 21 retained worker attempts used 634.031 cumulative process wall seconds against the 4200-second allowance. Maximum worker wall time was 84.479 seconds. This accounting includes failed and reproduction attempts. Numerical integration, full-array replay, saved-array metrics, source hashes, and budget checks are recorded separately in `analysis.json`.

The numerical gates compare both panels at all 19 checkpoints, all three parameter blocks, terminal fit decisions, and accepted-step loss monotonicity. Selected first-seed reproductions additionally compare parameters, predictions, and all saved fit decisions. Independent replay checks the raw-state forward map and RHS; this analysis independently recomputes metrics and selection from saved arrays.

No additional target, seed, width, initialization, optimizer, horizon or tolerance search is implied by this report. The prescribed experiment terminates with this comparison regardless of outcome.

Provenance: manifest SHA-256 `e846e002818282761339bf7a5a4d1fee1265308814977c0365b11bca195852da`; analyzer SHA-256 `81654206f57fcb27ff4475a57355ea4c6dbb601b69f935ddc6841cfe5d2a730d`; protocol SHA-256 `4216873a1246566c05fd9ce3815940801787c59df2a297faa9025a4c4ce02966`.
