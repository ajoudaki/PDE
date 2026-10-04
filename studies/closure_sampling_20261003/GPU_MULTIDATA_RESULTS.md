# Sampling budget across sample counts and sphere dimensions

2026-10-04. Empirical continuation of the practical neuron-sampling experiment.
The unchanged circle budget does **not** pass all the new tasks. Nearby pairs
pass for both label signs; larger sample sets and full-sphere prediction expose
limitations in the response basis as well as in the number of selected neurons.
This is a result about the tested construction, not a lower bound on compression.

The most informative controlled comparison is an eight-point circle embedded
in three input dimensions, evaluated over the full sphere. At dense width 2048,
doubling the retained state while keeping response rank 16 barely helps.
At the **same doubled state count**, raising the rank to 24 reduces the measured
trajectory error by a factor of 4.25. Thus changing the sampling representation
can matter more than adding neurons to an inadequate representation.

## Model, construction and measurement

There are m fixed unit training directions u_a in R^d and scalar labels y_a.
The physical inputs are x_a=sqrt(d)u_a. The canonical reference has two tanh
hidden layers, each of width n, no biases, and

\[
h(u)=\tanh(Au),\qquad g(u)=\tanh(Wh(u)),\qquad
f_n(u)=w^\top g(u)/n.
\]

A initially has independent standard Gaussian entries, W has independent
Gaussian entries of variance 1/n, and w starts at zero. All three blocks train
under the unhalved mean squared loss with mobilities (n,1,n). The physical
factor 2/m is included in every velocity. The independently initialized dense
copy is trained on the same data and supplies a variability control.

The reduced network retains A of shape N by d, K of shape N by N, readout w,
and fixed positive unit-sum masses mu and nu. Its forward map is

\[
f_{\rm small}(u)=(\nu\odot w)^\top
 \tanh\!\bigl(K\operatorname{diag}(\mu)\tanh(Au)\bigr).
\]

It evolves autonomously using its own residuals and the consistent weighted
adjoint. The read-in, small mixer and readout all train. No original-width
arrays or future dense trajectory enter its evolution. This is the previously
authorized direct dense-to-small-weighted-network route; it is **not an
unchanged order-q response-memory closure**.

Construction uses only the realized initialization, training inputs/labels,
and 32 fixed setup probes. It selects weighted neurons using initial forward
features and second time derivatives, first reverse responses and mixer
partners, a truncated response basis, approximate positive cubature, and the
same projected mixer construction as the preceding experiment. It never uses
trained predictions or the evaluation panel. This practical witness is not
the full initial-derivative construction in the study's mathematical results.

Including fixed masses and training data, the exact retained scalar count is

\[
P=N^2+(d+3)N+m(d+1).
\]

The moving part is N^2+(d+1)N. The baseline chooses the largest N satisfying

\[
P\le 2550\left[\frac{\log n}{\log512}\right]^4
\]

and uses response rank 16. At n=512,1024,2048, N ranges across these tasks
over 46--48, 58--59, and 71--72 respectively. Setup still reads the original
dense initialization. These experiments demonstrate large savings against
the dense matrix, but their retained counts are still larger than n.

For saved query directions u_j and saved physical times T, the primary error is

\[
E=\left[\frac1J\sum_{j=1}^J
 \max_{t\in T}|f_{\rm small}(t,u_j)-f_n(t,u_j)|^2\right]^{1/2}.
\]

We report sqrt(n)E. This is the query RMS of the pointwise time maximum,
not just the training error, endpoint error, or maximum over time of query RMS.
The latter two are also retained in the raw tables. Circle evaluation uses
257 angular points; sphere evaluation uses 512 fixed normalized-Gaussian
directions over the **full ambient sphere**. These approximate continuum RMS;
they do not bound the error at every possible input. Setup and sphere-query
seeds differ. The old circle grid contains one setup direction up to antipodes,
which is disclosed for comparability and not counted as independent sampling.

## Frozen tasks and decision rules

All 12 datasets were fixed before training, at widths 512,1024,2048 and two
initialization seed clusters, 9411 and 9412. Dense copies use seed+10000.
The 72 baseline cases are not 72 independent seed replications.

- Nearby circle pair: separation 15 degrees, labels (.1,.1) or (.1,-.1).
- Four/eight circle points: theta_a=7 degrees+a*pi/m, a=0,...,m-1. Smooth
  labels are .15*cos(theta)+.05*sin(theta). The four-point harmonic labels
  are .15*cos(3*theta); the eight-point harmonic labels are
  .15*cos(theta)+.05*sin(3*theta).
- The eight smooth circle points are embedded in R^3 and R^5 with unchanged
  intrinsic geometry and labels, but queries span the full ambient sphere.
- A tetrahedron in R^3 has labels (.15,-.1,.1,-.15).
- Eight fixed general-position sphere directions in R^3 and R^5 have labels
  .15*u_1+.05*u_2. A second labeling of the R^3 data uses
  .15*u_1+.15*u_1*u_2*u_3.

All labels have absolute value below .2; this is a numerical label scale,
not a verification of a theorem's unspecified small-label threshold. There
are no duplicate or antipodal training pairs. Exact vectors, seeds and labels
are in the two baseline JSON configurations.
The embedded tasks preserve intrinsic training geometry and initialization
law, but do not force identical realized training features across different
ambient dimensions; setup probes also change with dimension. They test
transfer across those tasks, not a pure change of query domain on one frozen
trained realization. The rank comparison below is exactly paired within a
single dimension and initialization.

The frozen error ceiling is sqrt(n)E<=.15. The width-trend criterion requires
the median scaled error at n=2048 divided by its median at n=512 to be <=1.5.
A larger constant alone need not violate root-width behavior. Conversely,
three favorable finite widths do not prove an asymptotic rate. Trends on the
common interval [0,120] are also retained, because full observation horizons
can differ across cases.

Heun integration uses float64, dt=.2, observations every unit time and no
TF32. A run starts at T=120 and extends in increments of 120, up to T=1200.
Numerical settlement requires each actual model to have training residual RMS
<=1e-6 and maximum query change <=1e-5 across all observations in its last ten
time units. An unsettled run still gives a finite-horizon discrepancy, but
does not establish an error at a fitted limit.

## Baseline outcome

Every baseline dense case completed. There were 70 constructed reduced models
and two preserved construction failures. The table gives the largest scaled
error over constructed baseline models and the two-seed median width ratio.
"Settled" requires the dense reference, copy and reduced model in every case.

| Task | Largest sqrt(n)E | Width ratio | All settled? | Interpretation |
|---|---:|---:|---|---|
| Nearby pair, same labels | .01897 | .553 | Yes | Passes baseline checks |
| Nearby pair, opposite labels | .12104 | 1.411 | Yes | Passes baseline checks |
| Four circle points, smooth | .03598 | Incomplete | Yes, where constructed | One construction failure |
| Four circle points, harmonic | .13829 | 2.674 | Yes | Ceiling passes; width trend fails |
| Eight circle points, smooth | .02566 | .853 | No | Small finite-time error; fitted endpoint unresolved |
| Eight circle points, harmonic | .07915 | 2.325 | No | Width trend fails; fitted endpoint unresolved |
| Same eight-point circle in R^3 | .33873 | 1.795 | No | Ceiling and width trend fail |
| Same eight-point circle in R^5 | .46249 | 1.872 | No | Ceiling and width trend fail |
| Four-point tetrahedron in R^3 | .10749 | 1.519 | Yes | Marginal width-trend failure |
| Eight sphere points in R^3, smooth | .0540 | Incomplete | No | One construction failure; endpoint unresolved |
| Eight sphere points in R^3, nonlinear | .0677 | 1.387 | No | Small finite-time error; endpoint unresolved |
| Eight sphere points in R^5, smooth | .1940 | 1.394 | No | Common ceiling fails; larger-constant root trend remains plausible |

The tetrahedron ratio is only narrowly above the prespecified 1.5 cutoff and
rests on two seed clusters. It is a trigger for further assessment, not strong
evidence of a different asymptotic exponent. The two constructor failures are
circle4_smooth and sphere3_eight_smooth at n=2048, seed9411. Dense-only records
are retained and never treated as successful reduced trajectories.

## What the larger budgets show

The prescribed candidates were twice the old budget at rank16, twice at
rank24, and four times at rank32. Diagnostic tasks were selected by the frozen
group rule, with construction failures taking priority. All diagnostics use
n=2048 and seed9411. Selection therefore uses a diagnostic case, followed by
explicitly identified second-seed confirmations where time permits.

For the eight-point circle embedded in R^3, all comparisons share the same
realized initialization, dataset, query panel and horizon [0,1200]:

| Budget multiplier | Response rank | Neurons per layer N | Retained scalars P | sqrt(n)E |
|---:|---:|---:|---:|---:|
| 1 | 16 | 72 | 5648 | .3137 |
| 2 | 16 | 103 | 11259 | .30752 |
| 2 | 24 | 103 | 11259 | .07242 |
| 4 | 32 | 147 | 22523 | .05005 |

Adding neurons at rank16 barely changes the error. Raising rank16 to rank24
at exactly the same retained state count improves the error by a factor of
4.25. The larger basis affects which neurons and mixer are constructed; the
experiment isolates response rank at fixed final count, not a post-training
projection. All these runs remain unsettled at T1200. The improvement is
empirical and finite-horizon, with no endpoint or general-rate claim.

There is a concrete initial representation limitation. With eight samples,
the constructor's priority matrix concatenates eight initial training-feature
columns and eight training-preactivation columns. Its resolved rank is 16 in
the checked circle and embedded cases, consuming the entire rank16 basis.
No extra basis directions remain for the other setup sources. An independent
SVD reconstruction at n2048, seed9411 gives relative Frobenius projection
defects for the initial second-layer features over the constructor's source
directions of .00533 on the circle, .55870 in R^3, and .68029 in R^5.
Adding nodes without changing rank cannot change that initial priority span.
Together with the controlled rank comparison, this supports a representation
bottleneck. It does not prove a formula relating those source defects to the
whole nonlinear trajectory error.

On the four-point smooth circle diagnostic, twice-budget/rank16 settled with
scaled error .00431; twice-budget/rank24 also settled, at .01194. The prescribed
choice was therefore twice-budget/rank16. On confirmation seed9412:

| Task | sqrt(n)E at n512 | At n2048 | Width ratio | Outcome |
|---|---:|---:|---:|---|
| Four-point smooth circle | .009776 | .007361 | .753 | Settled; passes the confirmation checks |
| Four-point harmonic circle | .045665 | .092180 | 2.019 | Settled, but width trend still fails |
| Eight-point harmonic circle | .027773 | Incomplete | Unavailable | n512 reaches T1200 without settlement |

The eight-point n2048 confirmation was stopped by the campaign limit at state
time507, with observations through506. It is not a completed comparison.
Doubling the budget thus repairs the smooth four-point case in this limited
confirmation, but **does not establish a common successful rule for all circle
tasks**, even though the completed errors remain below .15.

In R^5, twice-budget/rank16 changed the embedded-circle scaled error from
.46249 to .43749, still above the ceiling. Rank24 and rank32 failed numerical
construction. The independent setup-only replay found finite positive weights
above their prescribed floors, but mass-sum errors 6.82e-8 and 3.68e-8 exceeded
the 1e-8 validity threshold; both solves hit the fixed 150-iteration limit.
No tolerances, ranks or solver settings were changed to rescue these runs.
These failures are numerical construction limitations, not evidence that the
required cubature or compression is mathematically impossible.

For the eight general-position R^3 smooth sphere points, only twice-budget/
rank24 constructed in the diagnostic, with scaled error .04016 and unfinished
fitting at T1200. The rank16 and rank32 alternatives failed construction.
The general-position R^5 diagnostic was interrupted at state time84.2 and
does not yield a completed full-horizon result. No sphere candidate satisfied
all construction, error and settlement gates for selection and confirmation.

## Numerical checks, controls and limits

The unchanged flow/sampler implementation was checked independently against
the maintained dense equations, weighted-loss autograd, initial derivative
identities, exact scalar counts and restart reconstruction. The final raw audit
covers all 83 complete case records, including the two refinements. The two
interrupted baseline cases were rerun unchanged; their saved
prefixes reproduced bitwise. No adverse constructor or partial record was
deleted or counted as an independent replicate.

Both required refinements used the worst completed raw-error circle/sphere
cases, halved dt, doubled observation frequency, doubled nested query panels,
and exactly the same constructed initialization. The largest same-point
prediction changes across the compared models were 1.54e-6 for the circle
and 2.00e-5 for the sphere. The reduced primary-metric changes on the common
query panels were 1.11e-7 and 3.30e-7. Both pass the frozen numerical tolerances.
The sphere's additional query points changed reduced E by 3.16e-4; this is
panel sensitivity, separately recorded from integration error.

Dense-versus-dense controls, endpoint RMS, both time/RMS orderings, full
settlement traces, initialization Gram spectra, source/mixer defects and
feature-motion diagnostics are retained in the final tables. The controls
do not replace the absolute ceiling and trend gates. For example, baseline
medians of sqrt(n)E pooled over the three widths and two seeds are:

| Task | Independent dense copy | Reduced network |
|---|---:|---:|
| Nearby pair, same labels | .13770 | .01108 |
| Nearby pair, opposite labels | .14387 | .09337 |
| Eight-point smooth circle | .07453 | .01152 |
| Same circle embedded in R^3 | .10958 | .22142 |
| Same circle embedded in R^5 | .16668 | .33633 |
| Eight general-position sphere points in R^5 | .12664 | .14074 |

The embedded-circle errors are therefore larger than the observed independent
dense-run variability, not merely larger than the common ceiling. These are
descriptive pooled medians, not confidence bounds or matched ratios. All
per-dataset ranges are in `gpu_multidata_20261004_report_support/baseline_support.json`
under the study's generated namespace. Baseline numerical settlement counts
are 36/72 for the dense reference, 36/72 for its copy and 34/70 for constructed
reduced models. Both hidden layers and both hidden parameter blocks move.
The experiment uses trainable nonlinear features, but does not by itself prove
that each observed prediction requires feature learning rather than a simpler
alternative model.

Training used both RTX3090 GPUs, float64, peak allocated memory 421450752
bytes per worker. The union of intervals from archived provenance timestamps
through final-status timestamps was
1496.853589 seconds, below the 1500-second limit under this timer convention.
The timers include numerical validation, model construction, evolution and
failed attempts, but start after environment startup and source archival;
the worker timers agree with these starts within milliseconds. Neither
measurement covers complete process lifetimes. The last confirmation
received an external budget alarm before the computed deadline. There were 72 completed
baseline cases, four completed diagnostic cases, five completed confirmations,
and two completed refinements. Partial diagnostics/confirmations remain
archived. The setup-only optimizer replay used 31.24 CPU seconds and no training.

The tested rule remains a useful dataset-dependent practical heuristic.
The stronger claim that the old budget and rank work unchanged across all
these configurations is rejected by the frozen criteria. No new logarithmic
exponent, minimal neuron count, impossibility theorem, uniform-in-time theorem,
or all-input error bound follows from this campaign. More samples, label
structure, and the domain on which predictions are required must all inform
the representation; state count as a function of n alone misses those factors.

## Evidence and reproduction

- [Frozen protocol](GPU_MULTIDATA_PROTOCOL.md) and
  [design/analysis checks](GPU_MULTIDATA_DESIGN_CHECK.md).
- [Independent implementation and raw-evidence audit](GPU_MULTIDATA_AUDIT.md).
- [Exact setup-failure replay](GPU_MULTIDATA_SOLVER_DIAGNOSTIC.md).
- [Adapter](neuron_sampling_multidata.py), [runner](gpu_multidata_experiment.py),
  [analysis](analyze_gpu_multidata.py), and
  [follow-up config generator](make_gpu_multidata_followups.py).
- Final tables, plot, exact analysis command and source snapshot:
  `data/generated/closure_sampling_20261003/gpu_multidata_20261004_final_analysis_checked/`.
- Final independent checks and worker-interval accounting:
  `data/generated/closure_sampling_20261003/gpu_multidata_audit_final_20261004/`.

From the repository root, reproduce a particular scientific configuration into
a **fresh** output directory with the following command, changing the named
configuration and GPU to the desired archived worker. GPU access is required.

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/closure_sampling_20261003/gpu_multidata_experiment.py --config studies/closure_sampling_20261003/gpu_multidata_baseline_0.json --device cuda:0 --output data/generated/closure_sampling_20261003/gpu_multidata_baseline_0_reproduction
```

The original baseline configurations have 900-second worker limits; their
explicit unchanged resume configurations identify the remaining original
cases. Each worker root archives its resolved config, source snapshots and
hashes, initialization recipes, environment, exact command and exit status.
All nine execution roots share the prefix `gpu_multidata_20261004_`, with
suffixes `baseline_0`, `baseline_1`, `baseline_0_resume`, `baseline_1_resume`,
`diagnostic_0`, `diagnostic_1`, `confirmation_multi_circle`,
`refinement_circle`, and `refinement_sphere`. Failed and partial outputs remain
in place. The final analysis provenance supplies the complete multi-root
command and both coarse/fine case pairs; analysis alone launches no training.

These are collaborative internal research checks, not promotion reviews.
Root coordinated the frozen protocol, execution and report; multidata_runner
implemented the adapter/runner and replay diagnostic; multidata_design checked
the design and independently recomputed analysis; multidata_audit checked
equations and raw evidence. No manuscript, maintained code, other study,
Git index, commit or remote was changed by this continuation.
