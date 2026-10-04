# RMS growth-rule design check

The final section records the adopted protocol and subsequent direct calibration
audit. Earlier design recommendations below remain a dated proposal; the adopted
protocol uses the stricter calibration ceiling 0.10 and its stated rank tie rule.

2026-10-03. Scoped analysis by `rms_growth_design`. This report reanalyses
existing arrays and proposes a new calibration/holdout design; it launches no
training and does not claim an independently reproduced experiment. Allowed
scientific inputs were this study's `GPU_SAMPLING_PROTOCOL.md`,
`GPU_SAMPLING_RESULTS.md`, `GPU_NUMERICAL_CODE_CHECK.md`,
`neuron_sampling_setup.py`, `gpu_sampling_experiment.py`,
`analyze_gpu_sampling.py`, and their generated `gpu_sampling_20261003_*`
archives. All six source files were read completely. No other study or book
material was read. Required canonical-notation, neural-network conventions,
conjecture-investigation references, and shared process instructions were read.

## Recommendation

Precommit a primary root-width constant **C = 0.15** and test every held-out
trajectory against it. Use **0.12** as a calibration safety target, and report
**0.10** as a predeclared stricter secondary target. Keep C fixed when observing
holdout data. Select the smallest fixed neuron-count/basis-rank pair that passes
all calibration configurations before introducing width-dependent growth. If
growth is necessary, freeze an explicit rule for both selected neuron count and
source rank, including integer rounding, before opening the holdout results.

These are recommendations for a concrete protocol, not an assertion that any
candidate will pass. In particular, a large source rank with too few cubature
nodes may lose accuracy, so rank and node count must be varied separately.

## Metric and scope

The reference is the realized width-n, two-hidden-layer tanh network from the
old protocol: two-dimensional inputs, zero initialized readout, no biases,
Gaussian read-in and mixer, two equally weighted training examples, squared
loss, mobilities `(n,1,n)`, and all parameter blocks trained in physical time.
The two training directions have angle 60 or 90 degrees and labels
`(0.2,0.1)` or `(0.2,-0.1)`. The reduced network is autonomous and initialized
only from the reference initialization, labels, training directions, and fixed
circle probes. It evolves its own residuals.

Let `e(t,x) = f_reduced(t,x) - f_dense(t,x)` be the prediction error, let
`t_0,...,t_K=T` be the saved physical times, and let `x_1,...,x_M` be the equally
spaced circle panel. The primary metric, consistent with the supervisor's
stated formula to the user, is

\[
 E=\left[\frac1M\sum_{j=1}^M
              \max_{0\le k\le K}|e(t_k,x_j)|^2\right]^{1/2}.
\]

Also retain the ordinary time-uniform circle RMS and endpoint RMS,

\[
 E_{\mathrm{time}}=\max_k
        \left[\frac1M\sum_j |e(t_k,x_j)|^2\right]^{1/2},
 \qquad
 E_{\mathrm{end}}=\left[\frac1M\sum_j |e(T,x_j)|^2\right]^{1/2}.
\]

The deterministic relation is
`E_end <= E_time <= E`. Thus a bound on E controls circle RMS at every saved
time and the saved endpoint. It remains a sampled-time, finite-panel statement.
The old CSV's `rms_time_sup` is E; it is neither the old primary maximum over
both time and angle nor E_time. In the 180 distinct old reduced trajectories,
`E/E_time` ranges from 1.00020 to 1.42748. Report both to prevent ambiguity.

## Direct recomputation from existing data

All 36 main raw observation archives matched their stored hashes. Direct NumPy
subtraction, absolute values, maxima over time, and averages over the 257 angles
gave exactly the stored RMS and endpoint RMS for all 216 old schedule rows.
There are 180 distinct reduced models; duplicated schedules were not counted
as additional observations.

For selected neuron count N in each hidden layer, the retained state count is
`P=N^2+5N+6`, comprising `N^2+3N` moving and `2N+6` fixed coordinates.
Pooled descriptive medians below use the 12 angle/sign/seed configurations at
each width. They are not confidence intervals or cellwise acceptance tests.

| n | N | P | Median E | Median sqrt(n) E | Largest sqrt(n) E |
|---:|---:|---:|---:|---:|---:|
| 512 | 8 | 110 | 0.047326 | 1.07087 | 1.32515 |
| 512 | 13 | 240 | 0.010549 | 0.23870 | 0.56836 |
| 512 | 20 | 506 | 0.003465 | 0.07841 | 0.34628 |
| 1024 | 9 | 132 | 0.053233 | 1.70346 | 2.62299 |
| 1024 | 10 | 156 | 0.032575 | 1.04239 | 2.03298 |
| 1024 | 14 | 272 | 0.013631 | 0.43620 | 0.68065 |
| 1024 | 15 | 306 | 0.008524 | 0.27275 | 0.68381 |
| 1024 | 21 | 552 | 0.004263 | 0.13641 | 0.41101 |
| 1024 | 22 | 600 | 0.003857 | 0.12342 | 0.38361 |
| 2048 | 10 | 156 | 0.032514 | 1.47140 | 2.38125 |
| 2048 | 11 | 182 | 0.024465 | 1.10718 | 1.58082 |
| 2048 | 15 | 306 | 0.009784 | 0.44279 | 0.86716 |
| 2048 | 17 | 380 | 0.006769 | 0.30635 | 0.63265 |
| 2048 | 22 | 600 | 0.003558 | 0.16100 | 0.52739 |
| 2048 | 25 | 756 | 0.003806 | 0.17224 | 0.52685 |

The largest old p=2 schedule has median scaled endpoint RMS
`0.06349, 0.09752, 0.16302` at widths `512,1024,2048`. Under the proposed
individual-trajectory target C=0.15, only `10/12, 7/12, 4/12` cases would pass,
respectively. This target is therefore meaningfully stricter than the existing
evidence at larger widths. It is not calibrated to make the old method pass.

The independent-dense control's median scaled E is
`0.21870, 0.11426, 0.08262`, with largest individual values
`0.35448, 0.17561, 0.12658`. Its rapid decrease over this short range illustrates
why a paired ratio with an accidentally small denominator is a noisy primary
criterion. For context, report at each width the ratio of the pooled median
compressed E to the pooled median dense-control E, and separately show all
four geometry/sign cells. Do not call this ratio a median paired ratio.

## What the fixed rank-eight cap does and does not explain

At n=2048, increasing N from 22 to 25 reduces median first/second cubature Gram
operator errors from `0.0746/0.0884` to `0.0436/0.0497`, while median scaled E
increases from `0.1610` to `0.1722`. More nodes improve the fitted initialization
moments without giving monotone prediction improvement. These selected-node
constructions are not nested.

For all old N>=9, the rank-eight source bases at a fixed reference instance do
not depend on N. Their median relative Frobenius residuals on initialized
first/second hidden features are approximately:

| n | First-layer feature residual | Second-layer feature residual |
|---:|---:|---:|
| 512 | 0.04007 | 0.06600 |
| 1024 | 0.04006 | 0.06779 |
| 2048 | 0.04092 | 0.06547 |

These are relative norms, not fractions of squared feature energy. They show
that the source representation retains a nonvanishing approximation defect
over these widths. They do not prove that this defect causes the prediction
floor, or that raising rank alone repairs it.

The rank-r moment vector has `1+r(r+1)/2` constant/product entries before any
accidental dependencies. The proposed calibration grid exposes an important
second approximation axis:

| Source rank r | Moment entries | Node counts proposed |
|---:|---:|---|
| 8 | 37 | 24, 48, 96 |
| 12 | 79 | 24, 48, 96 |
| 16 | 137 | 24, 48, 96 |
| 24 | 301 | 48, 96 |

There is no general exact moment-fit guarantee when the available positive
weights are fewer than the moment constraints. Even with more nodes, positivity,
selection, the prescribed floor, and constraint dependence matter. Accordingly,
N=96 with r=8 versus r=12 is the cleanest proposed count-matched test of the
rank cap. The r=16 and r=24 runs are useful stress tests but can worsen cubature
error as they enrich the source space. Retain both layer Gram errors and source
residuals for every result; do not discard unsuccessful optimizers or numerical
rank deletions.

## Proposed calibration and holdout commitment

1. **Freeze the design before new training.** Use calibration seed 8411 and
   all four angle/sign configurations at n=512,1024,2048. Evaluate the
   predetermined N/r grid above with unchanged witness construction, mass
   floor, and retained dynamics. If C=0.15 and the 0.12 safety target are
   accepted, write them into the campaign protocol now. The calibration data
   may select a rule; it is not holdout evidence for that rule.

2. **Choose one rule using calibration only.** First consider fixed `(N,r)`
   pairs passing every calibration case with `sqrt(n) E <= 0.12`. Prefer the
   smallest P, with a predetermined tie-break on r and then error. If none
   passes, use only a prelisted family of nondecreasing `(N(n),r(n))` rules.
   Publish actual integer N, r, P at each width, and freeze the extrapolation
   to 4096. A rule that uses an untested intermediate N needs its own explicit
   calibration evaluation before freezing. If the grid supplies no passing
   rule, report that outcome rather than raising C or expanding the grid
   without a previously authorized branch.

3. **Open untouched holdout seeds 8511,...,8515.** Evaluate the one frozen
   rule, the dense reference, and an independent dense copy for every fixed
   geometry/sign cell at all three main widths and optionally 4096. Include
   4096 before looking at holdout data, either as a required fourth width or
   as a predeclared resource-dependent extrapolation test. There are 60 or 80
   holdout configurations; shared seed numbers across widths/cells should be
   treated as five seed blocks, not 60 or 80 independent replicates.

4. **Primary success is all-case success.** Require `sqrt(n) E <= 0.15` in
   every complete, numerically valid held-out case, along with settled dense
   and reduced endpoints. The corresponding raw RMS limits are:

   | n | C/sqrt(n), C=0.15 |
   |---:|---:|
   | 512 | 0.00662913 |
   | 1024 | 0.00468750 |
   | 2048 | 0.00331456 |
   | 4096 | 0.00234375 |

   A valid case above the threshold fails this particular sufficient rule.
   Missing cases, unsettled endpoints, optimizer validity failures, or
   unresolved discretization classify the all-case result as inconclusive.
   Report case fractions and the predeclared C=0.10 secondary outcome even if
   the primary rule fails; they do not replace the original acceptance test.

5. **Preserve numerical gates.** Use float64, disable TF32, retain fixed
   common query panels/times, and perform the prescribed half-step and nested
   panel/time checks. Compare changes in the new RMS metrics, not only the
   old maximum metric. A suitable absolute discrepancy gate is
   `min(1e-4, 0.05*C/sqrt(n))`. Treat threshold crossings within measured
   numerical variation as inconclusive unless a predeclared refined run
   resolves them. Settlement should check residual RMS <=1e-6 and the largest
   saved prediction excursion over the whole final ten-unit window <=1e-5,
   rather than only its end-to-end change. The horizon, one continuation
   branch, refinement remedy, total runtime/memory cap, and terminal stop must
   be specified in the new protocol before execution.

The numerical changes from the old pilot are small enough to make this target
plausibly resolvable, but those old checks do not validate new larger reduced
models automatically. Each rule's runtime storage is P; source rank, setup
workspace/cost, diagnostic archives, and the dense comparison process must be
reported separately. A successful fit at both training points is required for
settlement but does not replace unseen-circle accuracy.

## Finite-range identifiability

An unspecified constant C is always obtainable after finitely many finite
errors have been observed. Fixing C before holdout is what makes this a test.
Success would establish empirical sufficiency of the particular state rule on
the declared seeds, widths, geometry, labels, observation panel, and settled
finite endpoints. It would not prove root-width convergence, an optimal growth
exponent, all-time validity, or high-probability performance on unseen seeds.

Between n=512 and 2048, `log(n)` increases only by `11/9`. Thus
`P proportional to log(n)^p` changes by `(11/9)^p`, equal over those endpoints
to `P proportional to n^(0.144753 p)`. Adding 4096 changes the logarithm by
only `4/3` relative to 512; the corresponding endpoint power is `0.138346 p`.
These finite-range curves are too close to identify asymptotic log versus
power growth. Integer node counts make discrimination harder.

The proposed N=24,48,96 ladder has P=702,2550,9702. If N doubles at each
doubling of dense width, the actual endpoint state ratio is 13.8205 over a
fourfold width increase, equivalent to a state power exponent 1.89437.
Calling this a mild logarithmic rule would be misleading. A fixed successful
pair is the stronger practical result over the tested interval, while still
leaving its large-width asymptotics open. The study should report the smallest
tested sufficient rule, without interpreting a coarse-grid selection as a
minimal required rate.

## Reanalysis artifacts

Derived outputs are under
`data/generated/closure_sampling_20261003/gpu_rms_growth_design_20261003/`:

- `rms_models.csv`: 180 deduplicated reduced-model RMS and setup diagnostics;
- `rms_controls.csv`: 72 independent-dense/frozen-control RMS records;
- `raw_hashes.json`: verified SHA-256 values of all 36 input observation archives;
- `check_summary.json`: old-CSV agreement and proposed constants.

The recomputation used `/home/amir/miniconda3/bin/python`, NumPy, the two
`gpu_sampling_20261003_main_*` roots, and the existing analysis CSV. Its essential
calculation was `error=predictions-predictions[:,0:1,:]`, followed by
`sqrt(mean(max(abs(error),axis=0)**2,axis=1))` for E,
`sqrt(mean(error**2,axis=2)).max(axis=0)` for E_time, and
`sqrt(mean(error[-1]**2,axis=1))` for E_end. This is an independent metric
recomputation from retained evidence, not a fresh execution of the producer.
The shared Git index and all scientific source code were left unchanged.

## Adopted protocol and direct calibration audit, 2026-10-04

The supervisor subsequently authorized `GPU_RMS_GROWTH_PROTOCOL.md`, the new
`gpu_rms_growth_experiment.py`, and the generated calibration roots ending
`_calibration_90`, `_calibration_60`, and `_calibration_60_resume` under
`data/generated/closure_sampling_20261003/gpu_rms_growth_20261003_*`.
This is additional scope within the same study. No holdout outputs were read
for this audit. The new protocol uses 32 initialization probes, calibration
ceiling 0.10, and selection by smallest N, then smallest worst-case calibration
error, then smaller rank for exact ties. These adopted settings replace the
earlier proposal's 0.12 calibration margin and rank-first tie suggestion.

Direct NumPy reanalysis, without importing the new analysis script or producer,
confirms **N=48, rank=16, P=2550** as the selected calibration candidate. Its
maximum `sqrt(n) E` across all twelve prescribed cases is
`0.07516408706344334`; the maximum occurs at n=1024 with orthogonal inputs and
same-sign labels. Its largest scaled endpoint RMS is `0.032216527537428714`.
All twelve selected-model cases fit, settle, retain their selected frame modes,
and finish cubature optimization successfully. The paired rank-12 candidate
also passes, but has the slightly larger worst-case error
`0.07764335792216384`; therefore the frozen tie rule selects rank 16.

| N | Rank | Completed cases | Maximum sqrt(n) E | Selection result |
|---:|---:|---:|---:|---|
| 24 | 8 | 12 | 0.351041 | Above calibration ceiling |
| 24 | 12 | 12 | 0.228231 | Above calibration ceiling |
| 24 | 16 | 12 | 0.716124 | Above calibration ceiling |
| 48 | 8 | 12 | 0.351123 | Above calibration ceiling |
| 48 | 12 | 12 | 0.0776434 | Passes; loses fixed-state accuracy tie rule |
| 48 | 16 | 12 | 0.0751641 | Selected |
| 48 | 24 | 12 | 0.319076 | Final optimizer failure and excessive error |
| 96 | 8 | 12 | 0.327804 | Above calibration ceiling |
| 96 | 12 | 12 | 0.0490883 | Passes; larger state |
| 96 | 16 | 12 | 0.0176413 | Passes; larger state |
| 96 | 24 | 8 | 0.0352477 | Incomplete; ineligible |

The original 60-degree worker stopped while constructing N96/rank24 at n=1024,
same-sign labels. Its failure archive records invalid positive cubature masses,
ten completed sampler constructions, zero completed evolution steps, and zero
observations. The four remaining configurations were rerun excluding exactly
N96/rank24. The original failure remains archived. The resulting missing four
cases disqualify that candidate; they are not silently treated as successful.
N48/rank24 separately reports a failed final optimizer at n=2048, 60 degrees,
opposite-sign labels. Intermediate optimizer warnings are retained without
automatically disqualifying a candidate whose final fits are valid.

The audit covered 12 distinct completed cases and 128 reduced comparisons.
All three RMS metrics agree exactly with stored metrics. All 72 record-hashed
artifacts and 39 archived source copies matched their expected SHA-256 values;
all three run roots use identical producer source manifests. Reconstructing
each reduced endpoint from its saved `A,K,w,mu,nu` agrees with the raw prediction
panel within `2.220446049250313e-16`, and actual restart storage equals
`N^2+5N+6`, including the six training-data scalars. The final runner hash is
`83be73776a1c3f2da778ecd7da770fea987a519dc6cdc0f064ade82234a0fc3e`;
the sampler retains the original
`f3199851e30e267bab005b06ccf16f68f05b0307695d9d4cbca64aa2ddc28f02` hash.

Detailed evidence is in this report's previously assigned generated namespace:
`calibration_direct_rows.csv`, `calibration_direct_candidates.csv`,
`calibration_direct_check.json`, and `calibration_direct_hashes.json` under
`gpu_rms_growth_design_20261003/`. This verifies calibration arithmetic and
selection from retained evidence. It does not constitute a fresh training
reproduction, holdout confirmation, a step-size accuracy certificate, or an
independent full producer-code review. No model training was launched by this
auditor. The chosen candidate's width-growth rule still requires the separate
fresh-seed validation and prescribed numerical refinements.
