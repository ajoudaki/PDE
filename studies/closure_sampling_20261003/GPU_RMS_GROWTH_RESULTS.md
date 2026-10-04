# Circle-RMS experiments: a sufficient tested log-four state schedule

2026-10-04 local time (execution began 2026-10-03 UTC). Numerical continuation
of this sampling study. This is empirical evidence, not a new approximation
theorem or an optimal-exponent claim.

## Result

The practical initialization-only sampler with response rank 16 and state budget

\[
 P_{\mathrm{budget}}(n)=2550
       \left[\frac{\log n}{\log512}\right]^4
\]

passed all 80 fresh-seed validation cases at widths 512,1024,2048,4096 and all
four stress cases using one additional seed at width 8192. It uses the largest integer
selected width N satisfying P(N)=N^2+5N+6<=P_budget(n), in each hidden layer.
The primary error E is circle RMS of the pointwise maximum error over saved
training times, defined below. All 84 completed validation/stress cases obeyed

\[
 \sqrt n E\le 0.056597 <0.15,
\]

where 0.15 was fixed before these runs. All fitted and reached the numerical
settlement criteria. The main sweep's four geometry/sign cells had ratios of
median scaled error at n4096 versus n512 equal to .790,.922,.988,.920;
each passes the predeclared maximum growth factor 1.5. Two required solver and
query/time-grid refinement checks passed.

This is a concrete sufficient **tested** schedule. It does not establish that
p=4 is minimal, that p=1 or p=2 is impossible, or that this fixed-rank sampler
has root-width accuracy at arbitrarily large widths. The incomplete smaller
schedules had numerical setup failures, not demonstrated lower bounds.

## Model, metric and retained information

The reference is the realized canonical dense network: two width-n tanh hidden
layers, independent Gaussian read-in and mixer with entry variances 1 and 1/n,
zero readout, no biases, mean squared loss, and mobilities (n,1,n). All layers
train in physical time. Training inputs are sqrt(2)(1,0) and
sqrt(2)(cos(alpha),sin(alpha)), alpha=60 or90 degrees, with labels (.2,.1)
or(.2,-.1). These are fixed modest labels; the unspecified theoretical
small-label threshold is not numerically certified by this experiment.

The autonomous small weighted network is exactly the runtime already used in
[GPU_SAMPLING_RESULTS.md](GPU_SAMPLING_RESULTS.md): read-in A, small learned
mixer K, readout w, and positive masses mu,nu. Its forward map on the normalized
query u=x/sqrt(2) is

\[
 h=\tanh(Au),\qquad
 g=\tanh(K\operatorname{diag}(\mu)h),\qquad
 f=w^\top\operatorname{diag}(\nu)g.
\]

Its updates use its own residuals, the weighted transpose action, and no dense
trajectory information. This is the direct dense-to-weighted-network route;
it is not an unchanged order-q closure or a dense-to-population experiment.

Setup uses only the original initialization, training inputs/labels and 32
fixed probe directions. It retains initial forward derivatives through order
two and reverse derivatives through order one, a rank-16 response basis,
positive approximate cubature with mass-floor fraction .05, and an isometric
projected mixer. It does not implement the theorem's full initial-jet source
construction. There are no trained snapshots or future residuals in setup.

The smaller runtime stores N^2+3N moving scalars and 2N+6 fixed scalars, including
the entire learned mixer, both mass vectors, and the two training inputs and
labels. Temporary original-width setup arrays are not retained by the model.
Setup work, dense controls and diagnostic arrays belong to the experiment and
are not a claim of small end-to-end process memory. Array-only reduced restarts
were checked against saved predictions.

For x_j=sqrt(2)(cos(theta_j),sin(theta_j)) at 257 equally spaced offset angles,
write e(t,x_j)=f_small(t,x_j)-f_dense(t,x_j). The primary metric is

\[
 E=\left[\frac1{257}\sum_{j=1}^{257}
              \max_{t\in\mathcal T}|e(t,x_j)|^2\right]^{1/2},
\]

where the saved physical times are T={0,1,...,120} for the successful p4
validation and stress runs. Also retain max_t RMS_j e and endpoint RMS.
Both are bounded by E on this grid. This is neither an exact continuum-circle
supremum nor an all-real-time certificate. It measures predictor agreement,
not error relative to an assumed test-label truth.

## Design, calibration and independent validation

[GPU_RMS_GROWTH_PROTOCOL.md](GPU_RMS_GROWTH_PROTOCOL.md) was fixed before new
training. Calibration used seed8411, all four geometry/sign configurations,
widths512,1024,2048, and the declared neuron/rank grid. It selected N0=48,
rank16, P0=2550: maximum sqrt(n)E=.0751641. Rank12 at the same size also passed,
with slightly larger maximum .0776434. The fixed tie rule selected the lower
worst-case error at the smallest passing state count. The selection and all
future state counts were frozen in
[GPU_RMS_GROWTH_SELECTION.md](GPU_RMS_GROWTH_SELECTION.md) before validation.

Validation used untouched reference seeds8511--8515, independent dense-copy
seeds+10000, the four fixed geometry/sign cases, and widths512--4096. Shared
seed numbers across cells/widths are clusters, not 80 independent seed draws.
The additional n8192 stress used seed8611 and all four configurations.

Four budget exponents p=0,1,2,4 were prescribed. No parameters were retuned
using held-out prediction errors. The runner redundantly computed the four
identical width512 models instead of deduplicating their execution as planned;
they are bitwise-identical schedule aliases, not additional independent
replicates. Their actual storage counts remain those of a single model.

| Dense width n | Neurons per hidden layer N | Total retained P | Cases | Median E | Median sqrt(n)E | Maximum sqrt(n)E |
|---:|---:|---:|---:|---:|---:|---:|
| 512 | 48 | 2550 | 20 | .00116598 | .0263830 | .0565967 |
| 1024 | 59 | 3782 | 20 | .000716257 | .0229202 | .0428928 |
| 2048 | 72 | 5550 | 20 | .000488490 | .0221065 | .0300797 |
| 4096 | 87 | 8010 | 20 | .000403951 | .0258529 | .0426995 |
| 8192 | 102 | 10920 | 4 | .000301063 | .0272491 | .0329318 |

The final row is a separately seeded extrapolation stress, with one seed
rather than five. It is not an equally replicated fifth width.

![Complete p4 RMS comparisons](../../data/generated/closure_sampling_20261003/gpu_rms_growth_20261003_summary_figure/p4_rms_summary.png)

The shaded ranges contain five seed pairs through width 4096. Separate markers
at 8192 show one seed pair per geometry/sign case. The figure includes only
the complete p4 schedule and its matched independent-dense baseline.

For widths512,1024,2048,4096, the ratio of the pooled median compressed E to
the pooled median independent-dense E was .233,.134,.152,.183. These are
ratios of medians, not median paired ratios. The CSV outputs contain both
individual discrepancies and the descriptive paired ratios. Dense variability
is a matched baseline, not a proved rate estimate from these few seeds.

Endpoint RMS medians for the main four widths were .0006185,.0004353,.0003659,
.0003300. The largest final compressed training residual RMS was 8.30e-10;
the largest query excursion during the final ten saved time units was 5.08e-9.
These demonstrate numerical settlement. They do not by themselves prove an
infinite-time tail estimate.

## What changed relative to the first sampler

The first campaign kept rank at most eight and too few cubature nodes. The
new calibration separately varied these two approximation axes. At width2048,
the worst scaled error at rank8 remained about .35 at N48 and .33 at N96.
At rank16 it fell from .075 at N48 (maximum over all calibration widths) to
.0176 at N96. More neurons alone were not enough for the rank-eight version.

Higher rank also makes moment matching harder: ranks8,12,16,24 require up to
37,79,137,301 constant/product moments. Rank24 with48 nodes was inaccurate
and encountered a failed final optimization. Thus enriching the response
basis and improving its weighted quadrature must be considered together.
The algebraic whitening distortion from inaccurate selected Grams is derived
in [GPU_RMS_SAMPLER_AUDIT.md](GPU_RMS_SAMPLER_AUDIT.md). Operator-norm stability
alone does not imply a small forward or reverse approximation defect.

All p4 validation trajectories moved both hidden representations. Final
training-feature RMS motion ranged .0344--.0827 in the first layer and
.0426--.1136 in the second. Frozen-hidden controls are archived alongside
the moving dense copies. These facts exclude literal frozen-feature execution;
they are not a theorem identifying all latent representations or a comparison
of complete hidden geometries.

## Failures and recovery, without changing the sampler

Calibration produced128 completed reduced comparisons. N96/rank24 failed
construction on one nonorthogonal case and was globally ineligible; N48/rank24
also had a failed final optimizer on a completed case. Both remain visible.

Validation produced267 completed schedule rows: p0/p1/p2/p4 have76/49/62/80.
The smaller schedules remain incomplete and ineligible under the all-case
criterion because the numerical constructor failed on these cases:

| Schedule | n | Reference seed | Angle | Labels |
|---|---:|---:|---:|---|
| p1 | 2048 | 8512 | 60 degrees | opposite signs |
| p2 | 2048 | 8514 | 90 degrees | same signs |
| p0 | 4096 | 8514 | 60 degrees | same signs |

Each failure occurred before any training of that case. Recovery resumed
the remaining original cases for unchanged surviving schedules; no failed
candidate was silently counted as successful and no seed was replaced.
The p0 completed orthogonal cells also showed growing scaled errors, with
512-to4096 median factors2.60 and3.08. This concerns the fixed-state witness.

An unchanged CPU replay of the p1/p2 optimizer failures found finite positive
weights with mass-sum drifts2.17e-7 and6.85e-8, and unsuccessful SLSQP status8.
These are small numerical feasibility/termination defects, not proofs that
log or log-squared growth is inadequate. The solver was not relaxed or tuned.
See [GPU_RMS_SOLVER_DIAGNOSTIC.md](GPU_RMS_SOLVER_DIAGNOSTIC.md).

The first two-case workers at8192 exhausted their210-second individual limits
after completing the same-sign case and recording partial opposite-sign paths.
Their failures/partials remain archived. The global active-execution budget
still had room, so each unchanged opposite-sign case was rerun once in a
single-case150-second worker and completed throughT120. These are four unique
scientific stress cases, not six independent replicates. No model/solver
parameters changed during recovery.

## Numerical checks, resources and inference limits

The batched equations reuse the earlier runner and were checked against the
maintained dense RHS and Heun step, uniform weighted specialization, an
independent nonuniform weighted autograd oracle, and own-state restart.
Deterministic errors were below1.12e-16. Independent archive audits verify
raw metrics, initialization fingerprints, retained state counts, final
optimizer/frame status and final prediction reconstruction.

Main calibration, validation and stress runs used float64, TF32 off, and dt=.2.
The predeclared worst p4 case
(n512,seed8515,60 degrees,opposite signs) and fixed large case
(n4096,seed8511,60 degrees,opposite signs) were repeated with dt=.1 and
doubled nested angular/time panels. Maximum matched prediction changes were
2.39e-5 and2.41e-5; full-primary metric changes were1.38e-5 and1.34e-5.
For p4 itself the primary changes were3.10e-6 and1.08e-7. Both checks passed
their predeclared1e-4 gates, so no extra refinement was needed.

Two RTX3090 GPUs were used. The union of actual worker execution intervals,
including setup and failed attempts, was about22.17 minutes, below the
25-minute cap; peak allocated GPU memory was6.02GiB, below8GiB. Idle gaps
and report/plot processing are excluded from this active-execution measure.
Individual status files, timestamps and the calculation are retained in
`execution_budget_complete.json` under the validation analysis directory.
No further training was run after the four stress cases completed.

The strongest remaining limits are substantive:

- The tested range is finite. A fixed rank16 basis could develop an error
  floor at much larger n. The full theorem's higher response construction
  has not been numerically implemented here.
- Only five held-out seed clusters and one extrapolation seed were used.
  Descriptive bootstrap intervals are not high-probability population bounds.
- All-circle and all-time statements are sampled numerically, not certified
  for continuous angle, every real time, or the exact fitted limit.
- p4 is one sufficient tested rule; p3 was not tested and p1/p2 were not
  fully validated. No optimal or necessary growth exponent follows.
- Actual total P remains above n at the tested widths. The displayed
  polylogarithmic budget is asymptotically sublinear as a formula, but these
  experiments do not prove its unlimited validity or demonstrate a concrete
  P<n implementation over this range. Savings relative to the dense n^2
  learned matrix are substantial and explicitly counted.

## Artifacts and reproduction

Sources: [protocol](GPU_RMS_GROWTH_PROTOCOL.md),
[frozen selection](GPU_RMS_GROWTH_SELECTION.md),
[GPU runner](gpu_rms_growth_experiment.py),
[unchanged sampler](neuron_sampling_setup.py),
[raw-data analysis](analyze_gpu_rms_growth.py),
[focused summary plots](plot_gpu_rms_growth_summary.py),
[design/raw calibration check](GPU_RMS_GROWTH_DESIGN_CHECK.md),
[implementation and independent evidence audit](GPU_RMS_SAMPLER_AUDIT.md).

All JSON configs are `gpu_rms_growth_*.json` in this study. The runner accepts
`--config CONFIG --device cuda:0 --output FRESH_DIRECTORY`; the recorded
commands used `/home/amir/miniconda3/bin/python -B` with
`PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
MKL_NUM_THREADS=1`. Every run archives its exact argv, resolved config,
source snapshots/hashes and environment. Reproduction requires fresh output
directories; outputs are never overwritten.

Generated roots are under `data/generated/closure_sampling_20261003/`, with
prefix `gpu_rms_growth_20261003_`. Calibration uses `calibration_90`,
`calibration_60`, `calibration_60_resume`. Validation uses `validation_90`,
`validation_60`, `validation_90_resume`, `validation_60_resume`,
`validation_60_resume2`. Resolution checks are `refinement_fixed` and
`refinement_worst`. Stress uses `extrapolation_90`, `extrapolation_60` and
their `_resume` completions. Failed outputs remain in their original roots.

Final tables/figures and complete analysis commands are in
`calibration_analysis`, `validation_analysis`, and
`extrapolation_analysis_complete` under that prefix. Earlier pending/partial
analyses remain labelled by their names. Independent checks are research
implementation/evidence checks, not promotion reviews. No manuscript,
maintained code, other study, Git index, commit or remote was changed.
