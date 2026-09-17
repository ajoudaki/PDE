# Train-only 98% PCA preparation

## Frozen preprocessing and validity check

This is an internal data-preparation check for the explicitly requested
continuation of this study. The sole data input is the frozen `data_3_5`
archive. Fit ordinary centered PCA to its saved, already L2-normalized
`train_u` rows in float64. Retain the smallest dimension whose cumulative
centered sample variance is at least 0.98. Apply the training mean and basis
unchanged to validation and test rows; do not whiten or normalize again.
Preserve every split's labels and image IDs. No test value chooses the fit,
retained dimension, numerical tolerance, or model configuration.

`PCA_DATA.py` checks the alternative that a coding, centering, truncation, or
split error has invalidated the requested transformation. Before execution,
the numerical gates are: orthonormality maximum error < 1e-11; covariance
eigen residual relative Frobenius error < 1e-11; covariance trace and direct
centered energy relative discrepancy < 1e-11; reconstruction/retained-energy
fraction discrepancy < 1e-11; retained fraction >= 0.98 and previous fraction
< 0.98; full centered-matrix SVD eigenvalues relative L2 discrepancy < 1e-10;
training centering maximum error < 1e-12; saved float32 rows exactly equal the
direct float64 projection rounded to float32; and labels/IDs exactly
unchanged. The transform must also reproduce its fit when the covariance
eigensolver is repeated in the same single-threaded environment.

One deterministic preparation/check run is authorized, with at most 120 CPU
seconds and less than 200 MiB of new generated output. Stop after producing
the archive and diagnostics, or on a failed gate. No GPU training occurs in
this subtask. A pass establishes these finite numerical data properties only;
it makes no prediction-agreement, accuracy, or closure-convergence claim.

## Interpretation of input scale

Write the saved original input as U, training mean as mu, and retained
orthonormal component rows as V. The new model input is
Z = (U - mu) V^T. The 98% criterion concerns centered training variance,
sum ||Z_i||^2 / sum ||U_i - mu||^2, rather than 98% of the original
uncentered image energy. Row norms vary; centering can make some rows longer
than one even though their typical norm decreases.

The assigned `MODEL_SCOPE_CHECK.md` describes both engines as accepting
U = x/sqrt(d), and its sign-folding argument holds for arbitrary data.
Accordingly the reduced inputs have the same canonical interpretation with
x_new = sqrt(d_new) Z. The assigned `P1_INITIALIZATION.py` constructs its
dictionary for any positive d and does not impose a data-row norm check.
No obstruction from varying input norms was found in these scoped inputs;
this does not establish general-d network/closure convergence. Centering and
preserving projected amplitudes changes input scale as well as dimension,
which qualifies a causal interpretation of later accuracy comparisons.

The machine-readable result will be written to
`data/generated/first_order_dimension_mnist/pca_data_check/check.json`;
the prepared archive, fit transform and provenance will be in `data_pca98/`.

## Observed result, 2026-09-15

**PASS:** the smallest retained dimension is **240 of 784**, retaining
**98.0016736563%** of centered training variance. With 239 components the
retained fraction is 97.9819755595%. Total centered sample variance is
0.541351370311094 and discarded sample variance is 0.010817967044707588.
The discarded reconstruction-energy fraction is 0.019983263436630604.

The retained training energy is only 53.0483125190% of original uncentered
training energy; the squared norm of the removed training mean is
0.458699933043234. Thus the 98% centered-variance statement must not be
described as retaining 98% of the original input energy.

| Split | Projected norm minimum | Mean | Maximum | Mean squared norm |
|---|---:|---:|---:|---:|
| Train | 0.465565 | 0.722311 | 1.021606 | 0.530483 |
| Validation | 0.491334 | 0.722485 | 1.023699 | 0.530834 |
| Test | 0.463083 | 0.710102 | 1.006798 | 0.513302 |

All 10,552 training, 1,000 validation and 1,902 test labels and IDs agree
exactly with the source archive. Every saved float32 input agrees exactly
with direct projection using the reloaded training transform. Repeated
eigendecomposition agrees bit for bit in the recorded single-threaded
environment. Orthonormality maximum error is 3.00e-15, eigen residual relative
Frobenius error is 1.58e-15, direct energy-fraction discrepancy is 2.55e-15,
and the independent full rectangular-matrix SVD eigenvalue discrepancy is
1.12e-15 relative L2. The smallest raw covariance eigenvalue, -2.61e-18,
is numerical roundoff and is clipped to zero in the saved spectrum.

Fit cost is 0.4280 seconds wall / 0.4258 seconds CPU. Preparing and writing
the data and transform costs 1.1725 seconds wall / 1.1688 seconds CPU;
its peak process RSS is 306.102 MiB. The complete run, including validation
and SVD, costs 2.3005 seconds wall / 2.2952 seconds CPU and peaks at
372.574 MiB process RSS. These are CPU-process measurements, including
Python/NumPy and loading, rather than GPU or array-payload measurements.
Data and transform archives occupy 13,339,239 bytes (12.721 MiB); the small
JSON metadata/check files add several KiB, well below the 200 MiB generated
output budget.

Reproduction command: `python studies/first_order_dimension_mnist/PCA_DATA.py`.
It requires fresh output and check directories; defaults identify the saved
source and output namespaces. The environment is Python 3.10.12, NumPy
1.26.4, one BLAS/OpenMP thread, float64 fitting and float32 saved scores.

```text
Source dataset SHA256:
bc18a91521dff93f563a3828a0ba3d941ac7f23436978db7810aeeee06ef8c7f
Prepared dataset SHA256:
420da6f2ca6fb3c6163d9d91f32ddf95b1c3258c98f5e26cea6860f43dfa1b54
Transform SHA256:
c8b49915538949a3f1ae5bf4eda8cf610fdb0d261241190e31be9f83a369e6da
PCA_DATA.py SHA256:
cefa4493f94ea2a4108164cc273a6b0806fa588824fed8fcc43631bbc299014f
```
