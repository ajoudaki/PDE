# Dataset and dimension continuation: design check

2026-10-04. Scoped design and numerical-analysis check within this study. This
document checks the planned experiment; it is not a promotion review, a theorem,
or an independent replication of the GPU training. Inputs are this study's
sampler, preceding RMS protocol/results, and the new runner/protocol as they are
made concrete. No other study supplies evidence.

## Decision and preserved model

The decision is whether the previously selected practical response-rank-16
sampler and retained-state budget

\[
 P_{\rm budget}(n)=2550\left[\frac{\log n}{\log512}\right]^4
\]

remain adequate on the prescribed new training datasets. Here \(n\) is the
dense hidden width. This is a test of one concrete initialization-only witness
on a finite width range. It cannot identify a necessary asymptotic exponent or
validate arbitrary dataset dependence.

Write \(u_a\in\mathbb R^d\), \(\lVert u_a\rVert_2=1\), for normalized training
directions and \(y_a\in\mathbb R\) for their labels, with \(a=1,\ldots,m\).
The physical input is \(x_a=\sqrt d\,u_a\), so the Gaussian first-layer
preactivation convention is preserved across ambient dimensions \(d\).
Both hidden layers train, the readout starts at zero, and the network has no
biases. The weighted reduced model retains its own evolving read-in matrix
\(A\in\mathbb R^{N\times d}\), mixer \(K\in\mathbb R^{N\times N}\), and
readout \(w\in\mathbb R^N\), together with fixed positive masses
\(\mu,\nu\in\mathbb R^N\). Its output is

\[
 f(u)= (\nu\odot w)^\top
       \tanh\!\left(K\operatorname{diag}(\mu)\tanh(Au)\right).
\]

The moving scalar count is \(N^2+(d+1)N\). Counting both mass vectors and all
training directions and labels gives fixed storage \(2N+m(d+1)\), hence

\[
 P_{d,m}(N)=N^2+(d+3)N+m(d+1).
\]

For a fixed budget, \(N\) must be chosen using this dimension-dependent total,
not the previous special case \(N^2+5N+6\). Temporary dense initialization
arrays and the experiment's controls are outside retained model state; their
construction and runtime costs must nevertheless remain visible.

## Geometry and label audit

The proposed twelve datasets separate four questions:

1. Two inputs at 15 degrees, with equal labels \((.1,.1)\) or opposite labels
   \((.1,-.1)\), isolate a label contrast at identical geometry and scale.
2. Four and eight distinct half-circle directions
   \(\theta_a=7^\circ+a\pi/m\), \(a=0,\ldots,m-1\), use smooth labels
   \(.15\cos\theta_a+.05\sin\theta_a\). Eight directions with
   \(.15\cos\theta_a+.05\sin(3\theta_a)\), and four with
   \(.15\cos(3\theta_a)\), test label complexity on matching inputs.
3. The same eight smooth circle directions and labels embedded in dimensions
   three and five isolate ambient dimension while preserving the intrinsic
   training geometry. Their queries cover the full ambient sphere.
4. A three-dimensional tetrahedron with four modest mixed labels, Gaussian
   unit directions with eight samples in dimensions three and five, and an
   additional nonlinear labeling of the three-dimensional Gaussian directions
   test genuinely higher-dimensional training geometry. The smooth labels
   are \(.15u_1+.05u_2\); the nonlinear labels are
   \(.15u_1+.15u_1u_2u_3\). Since
   \(|u_1u_2u_3|\le 1/(3\sqrt3)\) on the unit sphere, all of these labels
   remain below .2 in absolute value. The tetrahedron labels are
   \((.15,-.1,.1,-.15)\).

The bias-free tanh network is exactly odd: \(f(-u)=-f(u)\), because each linear
map and each tanh layer preserves this identity. Therefore exact antipodal
training pairs require opposite labels. The prescribed half-circle directions
avoid this compatibility issue and avoid counting duplicate antipodal fitting
constraints as added sample complexity. The generic Gaussian datasets must be
stored explicitly and checked for duplicate or antipodal directions. The
tetrahedron has no antipodal pairs.

Embedded-circle tests alone cannot establish intrinsic dimension robustness.
Conversely, a full-sphere error panel is needed even for embedded training data:
restricting all queries to the training plane would hide ambient-direction
errors. The prescribed embedded and full-dimensional datasets serve different
roles and should remain separate in summaries.

## Metric, fitting and numerical decisions

For query directions \(u_j\), \(j=1,\ldots,J\), and saved physical times
\(\mathcal T\), let
\(e(t,u_j)=f_{\rm reduced}(t,u_j)-f_{\rm dense}(t,u_j)\). The primary recorded
error is

\[
 E=\left[\frac1J\sum_{j=1}^J\max_{t\in\mathcal T}|e(t,u_j)|^2\right]^{1/2}.
\]

This differs from \(\max_t[\frac1J\sum_j|e(t,u_j)|^2]^{1/2}\); both, plus
endpoint RMS, should be recomputed from raw arrays. Higher-dimensional panels
approximate the uniform sphere measure using fixed normalized Gaussian
directions. They measure sampled sphere RMS, not a certified continuum norm.
Panel random seeds are shared across widths within dimension. Refinement uses
nested query panels.

The predeclared scaled-error ceiling is \(\sqrt n E\le .15\), with .10 as a
secondary descriptive diagnostic. Width trend compares each dataset's median scaled error
at 2048 with its median at 512 and requires a factor at most 1.5. Both seed
clusters must be reported, not counted as independent replications within each
of the twelve datasets. Two clusters support only a descriptive width trend.

Fitting and trajectory approximation are distinct. The residual RMS threshold
is \(10^{-6}\), and numerical settlement additionally requires a maximum query
change of at most \(10^{-5}\) during the final ten physical time units. A
dense-unsettled case can still measure approximation over its observed finite
time interval. It cannot certify, or refute solely by non-fitting, agreement
of fitted endpoints. If the independent dense copy is unsettled, its endpoint
variability also does not represent a settled reference baseline.

The frozen protocol starts at physical time 120 and extends in increments of
120 until all actual models settle or time 1200 is reached. When these horizons
differ across cases, the primary width-trend criterion still uses the complete
observed intervals, exactly as preregistered. The analyzer additionally reports
the common interval from zero to 120 to expose possible horizon effects.

The independent dense copy uses the same input data and physical clock, with
its prescribed independent initialization. Its discrepancy is an observed
baseline, not a proved root-width constant or a selection denominator. A
small reduced/dense-copy ratio cannot rescue violation of the fixed .15
ceiling, an invalid constructor, or missing settlement.

Same-query prediction changes under time-step halving test integration error.
Changes caused by doubling a random sphere panel instead test query
quadrature. They must be reported separately: a random panel's quadrature
fluctuation is not evidence that the dynamical solver is wrong. A positive
adequacy claim requires the protocol's integration gates: both the largest
same-point/time prediction change and the primary-metric change on the common
query set must be at most \(\max(10^{-4},.05E)\) for the compared model.
Sphere-panel variation is descriptive and is not an additional acceptance
threshold. Two checks cover the worst completed circle and sphere cases.

## Conditional increases and terminal limits

The initial run uses the old rank and budget without dataset-specific tuning.
Construction failures, source truncation, priority-source rank, both selected
Gram defects, forward/reverse mixer defects, and optimizer status remain
visible. If the initial witness is inadequate, the predeclared larger-budget
and higher-rank diagnostic candidates must be compared on identical cases,
initializations, horizons, and query panels. Enlarging the response rank and
node count are separate approximation changes; improvement cannot be
attributed to nodes alone when both change.

A diagnostic case used to choose the increase is calibration, not independent
confirmation. The frozen candidates are exactly two times the old budget at
rank 16, two times at rank 24, and four times at rank 32. For each triggered
group, the worst task is diagnosed at width 2048 and seed 9411. Confirmation
uses seed 9412 at widths 512 and 2048 for each triggered task. That seed has
already appeared in baseline comparisons; only the increased candidate is
newly evaluated, so this is candidate confirmation rather than a completely
untouched seed. Failure only to settle does not trigger an increased budget.
At most six diagnostic cases and 24 confirmation cases are permitted.

The second-layer constructor prioritizes the concatenated initial training
activation and preactivation columns. Eight training points can therefore
consume all 16 available priority directions. In that event no basis direction
remains for the residual source expansion, despite the number of retained
neurons being larger than 16. Report this rank exhaustion directly; higher
rank at fixed budget separates it from a pure node-count limitation.

If larger candidates do not settle, their
errors remain too large, a validity gate fails, or the hard 25-minute union
of GPU-worker intervals is exhausted, the result stays unresolved for the
corresponding claim. No CPU scientific training is authorized.

This design check does not authorize extra datasets, sampler algorithms,
label changes, discarded seeds, or unbounded retries after seeing results.

## Implemented configuration and analysis checks

An independent direct read of both persisted baseline JSON files verified 12
datasets and exactly 72 distinct dataset/width/seed cases, with no missing or
extra Cartesian-product combinations. Every training direction, setup probe,
and query direction has unit norm to within \(10^{-12}\). Each dataset has
32 setup directions and either 257 circle or 512 sphere queries. Labels have
absolute value below .2. No training set has duplicate or antipodal directions.
Each sphere query panel has full ambient rank; each embedded training set has
rank two and exactly preserves the circle training coordinates and labels.
The known circle setup/query coincidence up to sign is present and disclosed
in the protocol. No such coincidence occurs in the sphere panels.

Independent integer budget maximization gives the following retained widths:

| Ambient dimension and sample count | At dense width 512 | At 1024 | At 2048 |
|---|---:|---:|---:|
| \(d=2,m=2\) | 48 | 59 | 72 |
| \(d=2,m=4\) or \(m=8\) | 47 | 59 | 72 |
| \(d=3,m=4\) or \(m=8\) | 47 | 59 | 72 |
| \(d=5,m=8\) | 46 | 58 | 71 |

The complete machine-readable check is
`data/generated/closure_sampling_20261003/gpu_multidata_design_config_check_20261004.json`.

The new analyzer reads raw arrays without importing the training runtime or
sampler. It verifies archive hashes, unit directions, shapes, signed training
residuals, archived errors, state counts, and maximal retained widths. It
retains construction failures even when a case never produces a final record.
It reports both dense controls, feature motions, initial training Gram spectra,
all source truncation residuals, source-priority exhaustion, and separate
trajectory/settled validity flags. Missing expected cases cannot pass a
dataset decision.

Deterministic analysis checks cover the noncommutation of time maxima and RMS,
the state count, completeness, a pure settlement failure that must not trigger
an increased budget, a fixed-ceiling failure that must trigger it, and a
width-growth failure with all errors still below the ceiling. Raw-array
recomputation of the first 22 completed live cases agreed with the archived
metrics; this early check is an implementation check, not the final empirical
conclusion.

The refinement selector uses the largest **unscaled** primary error separately
over circle and sphere comparisons, as clarified before the resolution runs.
The same-point integration comparison uses matching saved times. The
common-query primary comparison retains all finer saved times, so it also
tests whether the coarser observation clock missed a temporal peak. The fine
run must cover the complete coarse horizon. Dense-reference and independent
dense-copy changes are reported and checked alongside reduced-model changes.

Failure of the common .15 ceiling does not establish failure of root-width
behavior with a different dataset-dependent constant. Conversely, a favorable
three-width trend does not prove a root-width limit. These two numerical
criteria remain distinct in the decisions and interpretation.

## Final archived analysis

The checked final analysis is in
`data/generated/closure_sampling_20261003/gpu_multidata_20261004_final_analysis_checked`.
It includes 83 completed case records and 84 completed reduced-model rows:
70 baseline comparisons from all 72 baseline dense cases, seven diagnostic
comparisons, five confirmation comparisons, and two refinement comparisons.
Two baseline reduced constructions failed; their completed dense controls
remain included. Interrupted diagnostic/confirmation cases do not supply a
completed comparison and remain missing in the decisions.

Both prescribed refinement checks pass, including both dense controls. For
the reduced model on the 15-degree opposite-label circle case, the largest
same-point/time prediction change is \(1.47646\times10^{-6}\), and the
common-query primary error changes by \(1.10652\times10^{-7}\), against a
threshold \(2.67461\times10^{-4}\). For the embedded circle in dimension five,
these numbers are \(1.72188\times10^{-5}\) and \(3.30371\times10^{-7}\),
against \(5.65917\times10^{-4}\). Both checks preserve the full original
horizon, respectively 240 and 1200. The latter sphere-panel doubling changes
the reduced primary error by \(3.16453\times10^{-4}\), about 2.8 percent of
the original error; this is the declared descriptive quadrature check.

Only the two close-input label configurations pass every baseline criterion.
The principal contrasts are visible without interpreting unresolved endpoints
as fitted limits:

| Dataset or comparison | Maximum \(\sqrt n E\) | Scaled width-growth factor | Interpretation |
|---|---:|---:|---|
| Baseline close pair, same labels | .0189691 | .553277 | All criteria pass |
| Baseline close pair, opposite labels | .121039 | 1.41141 | All criteria pass |
| Baseline four-input harmonic circle | .138286 | 2.67377 | Fits and stays below .15; fails growth criterion |
| Baseline tetrahedron | .107490 | 1.51933 | Fits and stays below .15; marginal growth-criterion failure |
| Baseline embedded circle, dimension three | .338733 | 1.79522 | Finite-time ceiling and growth failures; endpoint unsettled |
| Baseline embedded circle, dimension five | .462494 | 1.87184 | Finite-time ceiling and growth failures; endpoint unsettled |
| Baseline eight smooth sphere inputs, dimension five | .194005 | 1.39405 | Ceiling failure; growth criterion itself passes; endpoint unresolved |
| Two-times budget, rank 16, four smooth circle inputs, confirmation | .00977570 | .752952 | Both candidate-confirmation widths fit and pass |
| Same candidate, four harmonic circle inputs, confirmation | .0921803 | 2.01863 | Both widths fit and stay below .15; growth criterion fails |

For the last row, errors at widths 512 and 2048 are .00201812 and .00203692.
Thus the absolute error is almost unchanged even as the required root-width
scale halves. The common-horizon scaled-growth factor is 2.05232, so the
failure is not explained by unequal final horizons. For the smooth
confirmation, scaled errors are .00977570 and .00736063, with common-horizon
growth .743749. These are confirmations of the selected candidate on seed
9412, not a new two-seed grid.

The eight-input harmonic confirmation completes only width 512: scaled error
.0277727, reduced residual \(9.79116\times10^{-4}\), and dense residuals
\(8.18941\times10^{-4}\) and \(1.10367\times10^{-3}\) at time 1200. Width
2048 on seed 9412 is missing. Neither the fitting condition nor the full
candidate confirmation passes.

The rank control is informative at dimension three. For the same embedded
dataset, width 2048, seed 9411, and two-times budget, increasing rank from 16
to 24 changes scaled error from .307524 to .0724196 while retaining the same
103 neurons per hidden layer and 11,259 total scalars. Rank 16 has no residual
second-layer source modes; rank 24 has eight. Four-times budget/rank 32 gives
.0500508. All corresponding dense/reduced runs remain unsettled at time
1200, so these are finite-time improvements, not accepted endpoint repairs.

One presentation defect was corrected after the first final analysis: passing
decision status strings still said numerical checks were pending when the
global required checks had passed. The checked output changes only those
status strings to `performance_pass_checked`; underlying numerical values,
scientific inputs, and pass/fail booleans are unchanged. The first final
analysis directory is preserved. Growth failures, missing comparisons, and
unsettled cases remain nonpassing.
