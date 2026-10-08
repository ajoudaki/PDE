# Bounded experiment-evidence audit

Status: internally checked evidence audit, 2026-10-07. No new simulations, proof claims, or changes to the analyzed code or shared notes.

## Scope and verdict

I read `analyze_learning_experiment.py`, `compare_causal_experiment.py`, and both complete summaries under `data/generated/transparent_learning_dynamics_20261007/beyond_initialization_v1/{analysis_v2,comparison_v1}/summary.json`. For the requested provenance and comparability checks I additionally inspected saved `record.json` metadata: source hashes and execution accounting across the 98 records, and configurations of the 30 primary comparison/refinement runs. I hashed, but did not reread, the dense and causal solver sources. I used my own simulator implementation knowledge only for the rank-tolerance coupling qualification below. No other study, report, or review was consulted. The saved trajectory arrays were not independently reprocessed; this is a complete analysis-code/summary audit plus a metadata check, not a fresh reconstruction of every statistic from raw arrays.

The displayed headline numbers agree with their definitions in the analysis code, and the standard-error formulas are correct. I found no arithmetic contradiction in the supplied summaries. Their defensible interpretation is restricted empirical evidence on the specified finite grids and small replicate cohorts. The following qualifications are material:

- The 3.4% cubic-clock error is normalized by the magnitude of the **mean final feature change**, not by the feature change at each time and not separately for each realization.
- The causal comparison is to dense **Euler at the same step size**, not directly to continuous-time gradient flow. The reported envelope omits the separately measured timestep-refinement change.
- The envelope covers two cross-feature changes and the passive prediction, not every training/panel prediction. It is neither a confidence band nor an error certificate.
- Mean causal-versus-dense discrepancies and pairwise dense-copy discrepancies are different statistics. Their observed ordering is not a theorem or a per-realization guarantee.

## 1. What is measured

For hidden layer \(\ell=1,2\), write \(C_{\ell,12}(t)\) for its cross-feature Gram entry on the two training inputs and

\[
\Delta C_{\ell,12}(t)=C_{\ell,12}(t)-C_{\ell,12}(0).
\]

Both scripts form the observable vector

\[
\bigl(\Delta C_{1,12}(t),\ \Delta C_{2,12}(t),\ f_3(t)\bigr),
\]

where input 3 is passive. A bar below denotes the mean over the specified simulation seeds, not a population expectation. Feature changes are centered **within each run** before averaging. This avoids confusing a nonzero finite-width initial cross-Gram entry with learned change.

`analysis_v2` uses four width-512 dense runs per opposite-label amplitude \(Y\in\{0.075,0.15,0.6\}\), with labels \((Y,-Y)\), RK4 step 0.1 and horizon 24. The same four seed IDs are used for the reported controls. The metadata confirms RK4 step 0.05 for the saved refinement runs.

`comparison_v1` uses, at each \(Y\in\{0.15,0.6\}\): four width-1024 dense Euler runs, three population-size-4096 causal runs, and common step 0.4 through time 24. Its refinements use four width-512 dense Euler runs, two population-size-1024 causal runs at step 0.4, and those two causal seed IDs at step 0.2. All 30 primary comparison/refinement metadata records match these intended labels, sizes, steps, horizon, modes, and reciprocal/middle-memory settings. The scripts compare arrays by position and subsample the finer arrays by `[::2]`; they contain no explicit time-array equality assertions. The metadata supports matching, but raw time-array equality was not independently checked here.

## 2. Cubic-clock claim

The autonomous scalar clock in the analysis script is

\[
\dot u=Y-\nu u-\kappa u^3,\qquad u(0)=0,
\qquad
\widehat{\Delta C}_{\ell,12}(t)=-b_\ell u(t)^2.
\]

The coefficients are evaluated from fixed Gaussian quadratures in the code; the code contains no trajectory-fitting operation for them. This audit does not independently rederive their scientific formula or establish when the approximation was selected relative to observing the data. Thus “no fitted trajectory coefficients” is supported by the code; “preregistered” is not established by these files alone.

For each amplitude and layer the reported normalized error is exactly

\[
\frac{\max_{t\text{ recorded}}
 |\widehat{\Delta C}_{\ell,12}(t)-\overline{\Delta C}_{\ell,12}(t)|}
 {|\overline{\Delta C}_{\ell,12}(24)|}.
\]

| Label amplitude \(Y\) | Layer 1 | Layer 2 |
| --- | ---: | ---: |
| 0.075 | 2.04249% | 0.65701% |
| 0.15 | 3.38032% | 2.08902% |
| 0.6 | 2.44166% | 1.51958% |

The maximum is 3.3803166187%, so “at most 3.4% of the observed mean final feature change” is an accurate rounding for these six finite-grid mean-curve comparisons. It does not mean a 3.4% pointwise relative error, a 3.4% error for each seed, an infinite-width error bound, a passive-prediction accuracy result, or an all-time guarantee. No uncertainty interval for this normalized model-error statistic is reported.

The measured-clock diagnostic is different: it integrates each dense run's own signed training residual, using sampled trapezoidal integration. Its endpoint ratio is formed separately for each run and then averaged. The collapse plot uses the mean of the **squared** measured clocks, not the square of their mean. These operations are coherent with the script, but this diagnostic uses the dense trajectory and cannot itself demonstrate autonomous prediction.

The frozen-clock errors have the same final-change normalization. At \(Y=0.15\) their maxima are about 40.6% and 42.5%, and at \(Y=0.6\) about 331.7% and 342.2%. These should not be replaced by a pointwise-relative or asymptotic-error interpretation.

## 3. Causal-versus-dense comparison

The all-panel prediction discrepancy is

\[
\max_{t\text{ recorded},\ a\in\{1,2,3\}}
 |\bar f_a^{\mathrm{dense}}(t)-\bar f_a^{\mathrm{causal}}(t)|.
\]

The dense-copy comparator first takes the same time/panel maximum for each of the six unordered pairs of four dense runs, then averages those six numbers.

| \(Y\) | Causal/dense mean prediction discrepancy | Mean pairwise dense-copy discrepancy |
| --- | ---: | ---: |
| 0.15 | 0.0029140035 | 0.0069808114 |
| 0.6 | 0.0087408911 | 0.0171869590 |

The saved six pairwise values reproduce the reported arithmetic means exactly. It is legitimate to report this observed comparison. It is not legitimate to interpret the six pairs as six independent replicates: they share four trajectories. Nor does the smaller mean-versus-mean discrepancy prove approximation of an individual dense realization at its intrinsic fluctuation scale, a width rate, or a bound in expectation. Ensemble averaging reduces sampling variation, and the two columns deliberately measure different objects.

The separate `max_mean_discrepancy` vector concerns only \((\Delta C_{1,12},\Delta C_{2,12},f_3)\). Its passive entry is therefore not generally the all-panel prediction discrepancy above. The values are respectively

\[
Y=0.15:\quad(0.00183010,\ 0.00215547,\ 0.00282762),
\]
\[
Y=0.6:\quad(0.00459267,\ 0.00506370,\ 0.00841520).
\]

### Envelope and refinements

For each of those three observables and each stored time, the code constructs

\[
3\sqrt{\mathrm{SE}_{\mathrm{dense}}^2+
             \mathrm{SE}_{\mathrm{causal}}^2}
+|\bar O_{N=1024}-\bar O_{N=4096}|
+|\bar O_{n=512}-\bar O_{n=1024}|.
\]

Both summaries of maximum positive envelope excess are zero in all three coordinates. This supports only “the observed mean discrepancies lie inside this diagnostic envelope on the recorded mesh.” In particular:

- The multiplier 3 does not confer simultaneous coverage across time, observables, or amplitudes; with only three and four replicates it is not automatically a pointwise confidence guarantee either.
- The two refinement terms are observed differences, not bounds on unknown finite-size biases. The causal size comparison uses two small-population runs versus three large-population runs, so it changes cohort composition as well as population size; it is not a clean paired size-bias estimate.
- No timestep-refinement term appears in the envelope. The script reports that diagnostic separately.
- Zero excess for the passive prediction does not establish zero excess for the two training predictions, which are absent from this envelope calculation.

The largest recorded population timestep-refinement changes, in the same three-observable order, are

\[
Y=0.15:\quad(0.00068114,\ 0.00123687,\ 0.00061539),
\]
\[
Y=0.6:\quad(0.00552017,\ 0.00989576,\ 0.00475922).
\]

At \(Y=0.6\), the second-layer timestep change is larger than the corresponding matched-step mean discrepancy. The successful matched-Euler comparison therefore must not be presented as continuous-time accuracy at that discrepancy level. These timestep checks themselves use population size 1024 and two seeds; they are not a bound on the size-4096 continuum error.

The dense RK4 0.1/0.05 check in `analysis_v2` is distinct. For seed 101 its maximum prediction differences are approximately \(5.07\times10^{-10}\) at \(Y=0.15\) and \(6.45\times10^{-8}\) at \(Y=0.6\). These are reassuring grid-refinement observations for those runs, not rigorous global integration-error bounds, and they do not remove the causal Euler discretization qualification.

## 4. Standard errors and controls

All displayed ordinary standard errors are sample standard deviations with `ddof=1`, divided by the square root of the number of seed replicates. The division by 2 in `analysis_v2` is correct for its four-seed cohorts. Paired control errors are correctly formed by taking each same-seed control-minus-full difference first, then computing its sample standard error. The causal paired controls similarly use three pairs, not the full particle population as a replicate count.

These standard errors quantify replicate-to-replicate Monte Carlo variation for the recorded statistic. They do not include discretization, population-size bias, model error, or uncertainty in an unproved extrapolation. Endpoint standard errors are not uncertainty bands for a maximum over time. Small cohorts should remain explicit.

The causal no-reciprocal and no-middle controls have sizable observed mean endpoint shifts in feature change, and their paired standard errors are reported correctly. Under the frozen implementation, each ablation recomputes its own law; disabling middle learning disables both its forward and backward learned-memory terms. These observations discriminate those particular implemented dynamics, not every alternative mechanism or representation. Same integer seeds are a useful pairing label, but do not guarantee identical later Gaussian draws if a control changes retained innovation ranks.

The saved `frozen_middle_dense_endpoint` in the causal-comparison summary is a **width-512** dense Euler mean, whereas the main full dense comparison is width 1024. It has no accompanying standard error in this summary field. Do not present a no-middle/dense-frozen agreement as a width-1024 matched comparison or attach the full-run standard error to this distinct cohort.

The local-affine control is labeled “Local-affine control” in the plot; it should not be described as an otherwise identical tanh forward network with only derivatives frozen without an additional source-level justification. Gate-motion-bin means, passive-motion RMS fields, and kernel-block plots are passed through from the dense solver. Their underlying definitions were not re-audited in this bounded task; the two analysis scripts alone do not establish causal claims from bin ordering.

## 5. Provenance, counts, and numerical diagnostics

The current source hashes are:

| File | SHA-256 |
| --- | --- |
| `analyze_learning_experiment.py` | `5a02e6761c5748f79da40cd123189bea1650d7c4a9926125b6f0e13ddb2ceb91` |
| `compare_causal_experiment.py` | `1649b4fce7317fc026fc55babd82b5b75336af3584cab038fb739cd4e0842b60` |
| `dense_learning_experiment.py` | `58d566adc2898a49389c73d659147dd98d39b4eab0c24aaba444dbc91d8a7942` |
| `causal_population_simulator.py` | `4431bef401087ca0e0f0bd465f1d31d88e7486403ec18d331eab8bbc035e5d76` |

The analysis summary records the first and third hashes, and both match the current files. The comparison summary does not contain its own analysis-source or solver hashes. However, every one of the 77 dense run records reports the dense hash above, and every one of the 21 causal run records reports the causal hash above. This supplies supporting run-level provenance; retaining the comparison script hash alongside the summary remains important.

The frozen summaries themselves hash to:

- `analysis_v2/summary.json`: `f80084356e3feb908edbc993e994fb0603ec4ae8152b31ef7baa24012d1ffa86`.
- `comparison_v1/summary.json`: `d9b90c110c7dcba1192ba9156d2530ac14e2507872c4f2317a90ec17859de41e`.

The analysis summary's `run_count=70` is the number of all run records present under a broad glob when that summary was written, not 70 independent replicates of the clock claim. The comparison's 77 dense plus 21 causal records give 98 records in the presently audited snapshot. Every record has exactly one of the two type markers used by the counting code; there is no double counting. Different snapshot counts are not a contradiction. The earlier summary does not preserve a manifest identifying the membership of its 70-record snapshot.

The current 98 records reproduce the comparison's summed recorded numerical wall time, 440.4036431387 seconds, and maximum recorded peak RSS, 677248 KiB (661.375 MiB). These are sums/maxima of recorded run metrics, not end-to-end research wall time or combined simultaneous-process memory. The earlier summary reports 248.8941105381 seconds for its snapshot. Neither execution count should be confused with the actual two-, three-, or four-seed cohorts defining a reported standard error.

The comparison records maximum primitive covariance reconstruction error \(1.67485\times10^{-9}\), maximum discarded innovation variance \(7.80411\times10^{-13}\), and a one-run tighter-rank-tolerance change below \(4.15\times10^{-7}\) across the reported feature/prediction arrays. These support numerical diagnostics of that factorization and that particular sensitivity test. They are not dense-approximation or trajectory-error certificates. Because fresh random coordinates are consumed only on retained innovations in the frozen simulator, changing the rank pattern can change later seed alignment; the rank-tolerance contrast is not automatically a strictly common-random-number perturbation experiment.

## Recommended compact report wording

“For four width-512 dense RK4 seeds at each label amplitude 0.075, 0.15 and 0.6, the autonomous cubic-clock feature approximation had maximum recorded-time error at most 3.4% of the corresponding observed mean final feature change. Separately, at matched Euler step 0.4 and horizon 24, causal population means from three size-4096 replicates differed from four width-1024 dense means by at most 0.002914 and 0.008741 in prediction over the three-input panel. The corresponding means of six pairwise dense-copy discrepancies were 0.006981 and 0.017187. These are empirical finite-grid comparisons, not per-realization or continuous-time error bounds; the small replicate counts, finite-population effects and Euler refinement remain explicit limitations.”

No edits to either analysis script or shared report were required for arithmetic correctness. The corrections needed are to interpretation if any stronger wording is used. No all-time, width-rate, universal-label, or full-depth conclusion follows from this bounded experiment.
