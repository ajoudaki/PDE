# Bounded appendix figure pilots

## Latest completed figures

- **Figure2, genuinely new repetition:**
  `data/generated/paper_appendix_pilots_20261009/figure2_replication/figures/figure2_storage.png`.
  All dense pairs and compressions were newly computed, with seed1701 for
  circle and1901 for digits. Both tasks use the user-approved Euler1/160.
- **Figure3, digits dense controls with three initializations:**
  `data/generated/paper_appendix_pilots_20261009/digits_dense_repeats/figures/figure3_accuracy.png`.
  Digits dense points show mean and sample SD; the original reference903,
  compression curves and sphere panel remain unchanged.

### Fresh Figure2 results

Every listed model passes BOTH endpoint and maximum-recorded query RMS at3x
its fresh independent dense-pair benchmark. Counts below are learned scalars.

| Circle dense width | Legendre | Harmonic | Logarithmic |
|---:|---:|---:|---:|
|512|17,922|16,776|37,448|
|1024|52,226|123,558|91,512|
|2048|71,682|82,088|66,312|
|4096|143,362|37,448|50,856|
|8192|417,794|148,616|83,816|
|16384|835,586|No tested pass|103,368|

All passing circle spectral budgets have local fail/pass brackets within20%
in compact width. These are not global minima or statistical confidence bars.
At16384, Harmonic256/512 fail accuracy and1024 fails the unchanged condition16
gate (observed30.223). No rescue was attempted. Logarithmic320 passes with
endpoint/maximum ratios2.11256/2.45610; its total retained size is410,569 versus
268,484,608 dense:2597x learned-state and654x total-storage reduction.

Descriptive post-search circle fits give Harmonic `C(log n)^3.53982` over five
passing widths and Logarithmic `C(log n)^1.47858` over six. The changed exponent
relative to the earlier seed is evidence of fit sensitivity, not a sharper
asymptotic theorem. Do not pool old fine-grid observations into this curve.

On digits1/7, Legendre order1 passes at all three widths1024/2048/4096.
Logarithmic width256/rank8 passes at all three with82,184 learned,196,609 fixed
and278,793 total scalars. Its endpoint/maximum ratios are0.45308/0.69698,
0.65848/1.03968 and1.12077/1.27431. All nine smaller-constructor requests fail
conditioning, not measured accuracy: these remain sufficient-size upper
bounds, and no image scaling exponent is fitted.

### Additional digits dense seeds

Fourteen new dense models completed: two seeds at each existing width, all
versus the unchanged original reference903. Each fit took3.92--4.12s on the
two GPUs; all reached5120 steps and the common65 observation times. Endpoint
query RMS mean and sample SD (three initializations including the original):

| Width | Mean | Sample SD |
|---:|---:|---:|
|256|0.039276|0.010081|
|384|0.026069|0.010035|
|512|0.026096|0.010944|
|598|0.024942|0.007212|
|648|0.027551|0.010980|
|738|0.021626|0.005725|
|4096|0.012371|0.003496|

The original598-to648 rise shrinks from62.59% to10.46%; the residual rise is
smaller than the observed seed spread. The curve is not strictly monotone,
and three conditional samples do not establish a population trend. The
horizontal digits dense benchmark is also the mean of the three4096 controls,
not the old single comparator. No reference or compression was retrained for
this Figure3 update; it is separate from the fresh Figure2 repetition.

### Reproduction and final check

All implementation remains in `paper/figures/capture_trajectory.py`.
`replicate_fast_circle_n*.json` generate new dense pairs and corresponding
`replicate_fast_circle_search_n*.json` run the adaptive searches. Digits use
`replicate_digits_n*.json` then `replicate_digits_refinement.json`. Plot with:

```sh
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py restored-paper-plot --scaling-only --config studies/paper_appendix_pilots_20261009/replicate_figures.json --out <fresh-root>/figures
```

For dense repeats, `dense-control-repeats --config .../digits_dense_repeats.json`
prepares an immutable generated `source.py` and config; run its `--seed904`
and `--seed905` workers (separate CLI tokens) on distinct GPUs, then its
`--summarize` action. Config `digits_dense_repeats_figures.json` rebuilds the
updated Figure3 via `restored-paper-plot`, with a fresh output directory.
The generated summary retains each individual seed's error, loss, timing,
initialization and input/source hashes. No generated array is overwritten.

Final checks reconstructed plotted RMS and dense mean/SD from saved arrays,
verified source/data/time-grid consistency, syntax and JSON parsing, and
visually inspected both figures. AST comparison confirms that no pre-existing
numerical definition changed (only the restored plotting function, plus the
new repeat orchestration). These are finite-Euler empirical results, not a new
time-step convergence or initialization-only certificate. No further runs
remain active; the earlier fine-step interruption remains archived separately.

## Fresh Figure2 replication (current user priority)

The user clarified that Figure2 should be a NEW-seed experiment, not a redraw
of historical measurements. The preceding restoration is explicitly only a
replot/revalidation. The Figure3 two-seed request below was paused before any
new fit or implementation. It was subsequently completed as reported above.

Frozen replication: circle widths512,1024,2048,4096,8192,16384 with new reference
seed1701 throughout, and raw8x8 digits1/7 widths1024,2048,4096 with new reference
seed1901 throughout. Each width gets a freshly initialized reference and
role-hashed independent same-width dense comparator; all compression sources
and models are rebuilt from its own new reference. Dataset seed47 and all
original data, architecture, runtime steps/horizon and source settings remain
unchanged. No historical prediction array contributes a new observation.
Only the dense pair and Legendre/Harmonic/Logarithmic methods in the original
task's scope run; no matched small dense, low-rank or frozen-feature controls.

Use the existing paper script and copied explicit configs `replicate_*.json`.
First run the original budget ladders, then the same bounded adaptive search:
3x endpoint AND maximum-recorded RMS,20% local width bracket, at most4 new
candidate requests per family/width after the ladders. Circle16384 retains its
original fresh doubling/search plan (at most8 requests per family). Preserve
each width's original maximum source rank and prefix rule. Failure of a
constructor or numerical gate is inconclusive, not an accuracy-failing lower
bound. No new seed, larger source space or extra search is allowed to rescue
an adverse result. Fit any descriptive log-power curves only after measurement.

Circle uses GPU0, digits GPU1. Per-fit/source caps120s, circle16384 dense fits
retain the original300s cap; circle queue wall cap25minutes, digits12minutes.
Stop with partial results at the caps. Report the new points separately from
old observations, including missing crossings, not a pooled or selected-seed
curve. Generated outputs are under `figure2_replication/`. Parent owns circle
execution, plot assembly, this record and Git; helper owns only digit configs
and execution. No numerical code change is needed for this replication.

Scheduling update: after the digits queue completed, GPU1 was reassigned to
the already planned circle8192/16384 jobs and their same bounded refinements.
The original circle shell launcher was paused between children, without
interrupting its active1024 fit, to prevent duplicate width jobs. The original
25-minute cumulative circle deadline remains unchanged. A question about using
the coarser pilot step was sent to the user; until answered, the exact old
1/640 circle step remains in force. This is scheduling only, not a numerical
change or added experiment.

User-authorized supersession: the user selected Euler1/160 for a fast first
replication. Fine-step circle jobs were stopped; their partial arrays stay
archived and are not mixed into the new curve. Fresh `replicate_fast_circle_*`
configs restart every circle width with seed1701, step0.00625 and record_every80
(same65 physical observation times). Sources, maximum source ranks and all
other mathematical settings are unchanged. Digits already used this step.
To avoid redundant initial candidates trained under the old1x early-stop rule,
the fast circle runs generate the fresh dense pair first, then directly use
the existing3x adaptive search. Start spectral width256, cap at each original
source family's largest width, preserve its original maximum source rank, and
halve/refine after passing. At most7 requests per family at the first five
widths (no larger than the old ladder-plus-refinement budget),8 at16384.
GPU0 handles512/2048/8192; GPU1 handles1024/4096/16384. Fast-stage cap600s per
GPU queue,120s per fit/setup; stop and label any remaining cases incomplete.
The fast run is a new-seed/coarser-step replication, not an exact fine-grid
reproduction or a new GF numerical certificate.

## Digits dense-curve replication (two additional seeds)

The user requested two more seeds to test whether Figure3's nonmonotone
digits1/7 dense curve stabilizes. Frozen scope: the existing seven widths
256,384,512,598,648,738,4096; two new initialization seeds per width, derived
by the existing role hash from repetition labels904 and905. Keep the SAME
saved reference903, eight training and thirty declared query inputs, all
labels, two tanh hidden layers, float64 Gaussian initialization converted to
float32, TF32 off, Euler step0.00625, horizon32 and65 recorded times. No new
reference, compression, task, width, tuning or resolution study is authorized.

Primary output is endpoint query RMS versus that fixed dense reference,
reported as mean and sample SD over the original plus two new models at each
width. Also retain the individual values, maximum-recorded RMS, training loss,
times and raw predictions. This estimates conditional initialization spread,
not variability across datasets or independently rebuilt compressions. A
monotone mean would support seed variation as an explanation for the original
bend; a remaining bend is reported as such, without forcing a fitted trend.
Three observations are not a significance test or a monotonicity guarantee.

Budget: fourteen new dense fits, at most120s each, split across both available
GPUs with a10-minute batch cap. Stop after this batch; no retries or additional
seeds. Incomplete/nonfinite or mismatched-time runs remain inconclusive. Parent
owns this record, plot aggregation and Git; scoped helper owns only the lean
saved-reference repetition entry point/config and its execution. Generated
products live in this study's `digits_dense_repeats/` namespace. Old figures
and arrays remain unchanged; the revised Figure3 gets a fresh destination.

## Figure 2/3 restoration requested by the user

The user has restored the primary constant-comparability criterion to 3x and
asked for fine-grained budget measurement in Figure 2 and the original 3D-sphere
task with higher-order compressions in Figure 3. The feedback attachment asked
for finer, not coarser, budget measurement; the coarse grid was our pilot shortcut.
The 1x feedback figures below remain a separately qualified stricter analysis.

This is a correction/continuation of the same figure investigation. Explicitly
authorized restoration inputs are the measured circle adaptive-search results
under `circle_width_scaling_20261009` and the screenshot's exact sphere3 results
under `cubic_log_comparison_20261008/sphere3_compression_larger`, including their
recorded dependency chain, in addition to the existing assigned pilot inputs.
No other study is an input. Root owns this record, bounded image-budget fits
and Git; a scoped helper owns only the restored-figure rendering entry point
in the existing paper script and its JSON manifest.

Frozen plan: reuse the original adaptive circle measurements at widths512--16384
and the saved sphere3 width4096 trajectories, including Legendre order12 and
Harmonic/Logarithmic widths600/850 with source ranks44/65. Do not rerun or alter
their seeds, query panels or resolution, and do not describe replotting as new
replication. Preserve the absent Harmonic16384 crossing and every old failure.
Figure3 keeps the image panel, all existing controls, and both learned and total
storage disclosures; the sphere's dense medians remain conditional on its
original fixed reference, not independently rebuilt compression repetitions.

For the image Figure2 panel only, refine the existing raw8x8-digits1/7 runs at
widths1024/2048/4096 using their exact saved dense pair, data and horizon. Keep
Euler0.00625, sourceRK4 0.125, float32/float64 settings and selector condition16.
Use factor3 for endpoint AND maximum-recorded RMS, width tolerance20%, at most
four new candidates per family/width (no new dense fits, seeds or widths), and
the existing refinement width-to-source-rank rule with the original maximum
source basis. Failed numerical/constructor gates remain inconclusive, not
accuracy failures. No budget interpolation is presented as a measured model.
Per-fit/source cap120s, combined two-GPU queue cap10min. Stop at the cap or the
local bracket; do not rescue an adverse result. Outputs go under `restored/`.
Any logarithmic-power curve is an exploratory fit to measured passing budgets;
three image widths alone do not identify an exponent. No theory or main-paper
claim is changed by this plotting correction.

### Bounded image refinement result

The image refinement is complete. All nine requests at compact widths128,192,224
failed the unchanged condition16 constructor before training; none is counted
as an accuracy failure. Each width's source/reconstruction queue took4.7--6.1s.
The original width256/rank8 Logarithmic witness remains the smallest constructed
passing candidate, with82,184 learned and196,609 fixed scalars at all three
dense widths. Endpoint/dense-pair ratios are0.64870,1.12383,2.15862; maximum-
recorded ratios are0.88383,0.92967,2.75641. All meet the requested3x criterion.
These are sufficient-size upper bounds, not resolved accuracy crossings, and
no image exponent is fitted. Arrays from all three original runs are preserved
bitwise, including their dense pairs and controls. No new dense training ran.

This does not affect the original circle adaptive crossings: all available
Harmonic/Logarithmic circle crossings were already bracketed to within20% in
compact width (except the absent Harmonic16384 pass). Original raw arrays and
protocols, including the failed Harmonic16384 candidates, remain unmodified.

### Restored figures and reproduction

Completed outputs are `restored/figures/figure2_storage.png` and
`restored/figures/figure3_accuracy.png` in this study's generated-data directory,
with PDF companions, full captions and hash-linked metrics. Figure2 restores
the six-width adaptive circle measurements and the 3x criterion. Its descriptive
learned-storage fits are `(log n)^3.50871` for Harmonic over five widths and
`(log n)^5.19661` for Logarithmic over six; these are not asymptotic certificates.
The image panel marks the unresolved lower-budget construction gates explicitly.

Figure3 restores the original 3D-sphere task, Legendre order12 and compact
widths600/850, preserving the original controls and conditional dense medians.
At the largest plotted budgets, endpoint RMS is0.0000593923 for Legendre,
0.000400495 for Logarithmic and0.00349048 for Harmonic, versus0.00338088 for
the independent dense pair. Harmonic width600 has RMS0.00337697. Both figures
show learned and total retained storage; fixed mixers are not omitted.
Saved circle/sphere data were revalidated, not regenerated. These experiments
still use full-horizon source rollouts, as the captions disclose.

Reproduce the plots from the saved inputs with:

```sh
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py restored-paper-plot --config studies/paper_appendix_pilots_20261009/restored_figures.json --out <fresh-output-root>/figures
```

The bounded image-refinement plan is `restored_digits_budget.json`. Final
checks covered saved-array/hash consistency, syntax, manifest parsing and
visual inspection of both figures. No numerical method or training routine
was changed in this restoration.

## Earlier feedback round (1x; retained separately)

The feedback continuation below supersedes the original pilot's presentation,
not its saved observations. Revised figures use a strict 1x dense-pair criterion,
show learned AND total retained storage, distinguish censored minima and failures,
and disclose the offline full-horizon source rollout. The original 3x choice was
user-authorized, not a hidden implementation error; 1x was that round's stricter
test and is not the restored primary criterion above.

Panel-span reduction now permits raw MNIST and dimension784 Logarithmic pilots.
At dense width2048, the smallest tested passing MNIST model has58,920 learned
and180,321 fixed scalars (239,241 total), with endpoint RMS0.017086 versus
dense-pair RMS0.021206. The local tested width crossing is192--224. On sphere3,
the Harmonic and Logarithmic crossings are288--320 and224--256. These are
single-seed, finite-grid comparisons, not global optimality or asymptotic rates.

Three independent dense pairs per width are complete on sphere3 and raw MNIST
at widths1024/2048/4096, using the same seed lists across widths. Compressions
have NOT been rebuilt for all these pairs. The representative sphere3 half-step
check passes; the16-example compact case fails its numerical gate and remains
unresolved. The SiLU endpoint and pooled-label transfer tests do not pass1x.
No failed result has been relabelled a success or removed.

All new evidence lives in `data/generated/paper_appendix_pilots_20261009/feedback/`.
Hand-written reproduction configs are `feedback*.json` alongside this README;
implementation remains solely `paper/figures/capture_trajectory.py`.
Detailed corrected results and remaining limitations are at the end of this file.
The original protocol and results below are retained for provenance.

## Scope and design frozen before runs

This is a new study of source transfer and empirical mechanism/scope tests.
User-authorized inputs are `paper/figures/capture_trajectory.py`, established
docs, and the explicitly cited Figure2–4 configs/results in
`studies/paper_figure_drafts_20261009/` and its generated-data namespace.
No other studies are inputs. Code stays in the existing single paper script;
generated products go in `data/generated/paper_appendix_pilots_20261009/`.
Root owns this record, source-transfer runner and final assembly; scoped helpers
own saved-data analysis, source-spectrum instrumentation, and new standard
runner configs/runs. Only root writes Git.

These are first-version, single-seed empirical figures, not theorem audits or
asymptotic certificates. Preserve unfavorable results. No search for favorable
seeds or activations, no dense widths above2048, no numerical-refinement round.
Use Euler step0.00625,T32,record spacing0.5,float32 execution and float64 setup,
TF32off, full-horizon RK4 source rollout step0.125,time degree8,64 selection
trials,condition cap16. At most120s per fit/source,18minutes per GPU queue.
Stop at the fixed cases; incomplete/nonfinite/conditioning failures are
inconclusive, finite completed inaccuracies are recorded as failures. No
continuous-time or resolution-certified statements are made.

### 1. Source transfer (priority)

Circle,n1024,L2,tanh,m8,p30,dataset seed47,reference seed901. Build Logarithmic
sources under the original target; construct the compact model before changing
the target. Then reset only its label-dependent residual initial state and
train on a different angular target (not a scalar/sign change). Compare to
coupled new-target dense, independent new-target dense, a compact model built
with new-target sources, and original-target dense predictions as literal
replay control. Width256,source rank15 fixed before results. No new-target
trajectory information may enter transferred geometry or weights. Success:
endpoint AND maximum-recorded RMS <=3 times corresponding new-task dense-pair
errors, while replay exceeds that criterion. Failure only rejects this witness;
success supports transfer, not initialization-only practical setup.

### 2. Spectral mechanism

Circle sources at n512,1024,2048,one seed,width-independent settings. Measure
full singular values of coefficient matrices after mandatory-span removal;
fixed relative Frobenius-tail thresholds1% and0.1%. Separate spectral shape
from approximation error on source holdouts. No fixed-rank truncation of the
measured spectrum, no fitted asymptotic exponent from three widths.

### 3. Dimension and4. architecture

Sphere n2048,m8,p30,dataset seed47,reference seed901. Dimensions2,3,10,64,784;
Logarithmic widths256 and512,ranks15 and37; Harmonic only d2,3 with the same
budgets,spatial degree5. Record constructor/source restrictions explicitly;
do not bypass mandatory first-layer coordinates to force a dimension-free
plot. The displayed minimum is smallest TESTED passing learned-state budget,
using the same endpoint AND maximum-recorded3x dense-pair criterion. Bounds
are not optimized minima. Low-dimensional targets and high-dimensional target
geometry must be described, not conflated with increasing intrinsic complexity.
Additional cases change one baseline setting: depth3,depth4,SiLU,m16. Logarithmic
width512/rank37 only for these; dense pair in each case. Fixed horizon remains
even if a setting fits poorly; report final training loss rather than rescuing.

### 5. Scope

Use saved Figure3 pointwise query errors versus nearest declared-input angular
distance (unlabeled inputs only). This is observational, not a causal distance
experiment. Panel-size test uses the dimension2 standard case as p30 baseline,
plus p8 andp60, same two fixed budget candidates; plot minimum tested passing
storage or failure honestly. Query labels remain held out.

### 6. Costs and free ratio plot

Reuse saved run timings; separate full-rollout source setup, compact construction,
training and query time, learned and fixed storage. CUDA peak reports include
resident references and cannot be called isolated model peak memory. Defer
equation-changing ablations in this first pass. Plot fixed existing budgets
across Figure2 widths, error/dense-pair error, separately endpoint and worst
recorded error. Constant budgets are a fixed growth schedule; neither declining
ratios nor asymptotic vanishing is presupposed.

## Status

Design frozen before execution. One bounded consistency check at completion;
no campaign expansion or unfavorable-result rescue.

### Source-transfer first result

Completed in49.8s on GPU0. Endpoint RMS against new-target dense: transferred
0.0850457, rebuilt0.00684973, independent dense0.00853602, literal old-target
replay1.374497. Worst-recorded ratios to the dense pair are9.575,0.771,1,and
154.754 respectively; endpoint ratios9.963,0.802,1,and161.023. Transferred and
rebuilt retain66,312 learned+196,609 fixed coordinates. This rejects literal
unchanged playback as a description of runtime, but the transferred witness
FAILS the3x fidelity discriminator: it does not close the reviewer objection
that accurate practical geometry depends on the original training trajectory.
No initialization-only practical claim follows. No rescue budget was tried.

The new target is cos(theta)+0.5sin(5theta), normalized to training RMS1.
Its training-label cosine with the old target is0.05891. Constructor weights,
metrics and inverses are hashed before/after resetting only the initial
label-dependent deficit; hashes agree. New-task sources are computed only
after that freeze and are used solely by the rebuilt positive control.
All five Euler runs complete on the same65 times. Dense reference final
training MSE0.01714; transferred0.003902; rebuilt0.01777. Better target fitting
does not imply better capture of the dense trajectory.

Reproduce: `/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py
appendix-transfer --config studies/paper_appendix_pilots_20261009/transfer.json`.
The configured output must be fresh (existing runs are not overwritten).
Raw arrays, config, source snapshot/hash, timings and figure are in
`data/generated/paper_appendix_pilots_20261009/transfer/`.

### Spectral mechanism

The first coefficient-only measurement was supplemented by one instrumentation
correction at the SAME three widths: directly measure actual top-layer h
histories at128 held-out times and38 training/declared inputs. One of129
candidate times coincides with fitting and is excluded. The n-by4864 history
matrix has its initialized mandatory span removed; its full singular spectrum
is measured without a rank cap. This avoids interpreting a fitted polynomial's
built-in finite rank as evidence about the original dense histories.

| Dense width | History rank,1% relative tail | History rank,0.1% relative tail |
|---:|---:|---:|
|512|42|104|
|1024|44|111|
|2048|44|115|

Ranks are minimal for relative Frobenius reconstruction error, not uniform
prediction error. The removed mandatory span remains additionally necessary.
Projected history RMS0.279–0.296 and energy fractions22.9–25.9% show that the
measured history is not vanishing. Full coefficient rank maxima over all layers
and both source families are48/50/52 at1%,116/124/131 at0.1%. Degree8 temporal
interpolation has maximum held-out relative RMS below7.8e-7. Each corrected
width took less than8s including process startup. This is evidence for similar
finite-width spectral structure, not proof of polylogarithmic growth, exponential
spectral decay, or a uniform all-input/all-time approximation.

All15 full spectra passed singular-count, finiteness, sorting, Frobenius-energy,
and independently minimal tail-rank checks. A small producer check also showed
that optional instrumentation leaves the original randomized source outputs
unchanged. Primary figures and full provenance live in
`data/generated/paper_appendix_pilots_20261009/spectral_history/`; prior
coefficient-only results are auxiliary in `spectral_gpu/`. The initial
unprivileged invocation in `spectral/` failed before CUDA construction; it is
an infrastructure failure, not experimental evidence.

Reproduce with `/home/amir/miniconda3/bin/python -B
paper/figures/capture_trajectory.py appendix-spectral --out <fresh-output>
--device cuda:0`. The executable/config snapshots record all settings.

### Saved-data scope, ratios and costs

No new training runs are used by `appendix-saved-plot`. Scope scatterplots use
angle to the nearest member of the complete declared panel (8training+30query
inputs), and compare endpoint absolute prediction error on30 undeclared queries.
Descriptive distance/error correlations are0.551(circle),0.505(digits), versus
0.084 and0.003 for independent dense. This is observational and confounded by
query geometry, not a causal distance intervention or a monotonic-error theorem.

Across n1024,2048,4096, fixed-width512 Logarithmic endpoint/dense-pair ratios
are0.139/0.130/0.279 oncircle and0.226/0.312/0.763 ondigits; corresponding
worst-recorded ratios0.201/0.176/0.431 and0.226/0.256/0.575. These budgets pass
but do NOT demonstrate a ratio tending tozero. The Legendre comparison keeps
order4 fixed, so its learned storage grows with n; it is not a fixed-size model.

At n4096 the recorded compressed update loops take about11–15s, compared with
about3.8–3.9s for dense updates. Thus these small-data implementations demonstrate
storage savings, not training-time speedups. Source setup, construction and
query/refresh times are shown separately. Source timing is shared across the
tested family budget ladder, not a separately isolated per-model setup trial.
Retained payload is4bytes per float32 coordinate; measured CUDA peaks include
resident references and must not be interpreted as isolated deployment memory.
All fixed mixers/metrics are counted separately from learned state.

Reproduce: `/home/amir/miniconda3/bin/python -B
paper/figures/capture_trajectory.py appendix-saved-plot`. Images, captions and
hash-checked metrics are in this study's generated `figures/` directory.

### Dimension, architecture and panel-size results

All11 cases finished in452.78s on GPU1:39 completed Euler fits, including17
complete compact candidates. Every completed compact candidate meets both3x
criteria. Three construction-conditioning failures and two analytical exclusions
remain explicit; no further selector, budget, seed or step searches were made.

| Logarithmic case | Smallest tested passing learned state | Endpoint/dense-pair ratio | Worst-recorded ratio |
|---|---:|---:|---:|
|d2|66,312|2.391|1.088|
|d3|66,568|0.925|0.530|
|d10|68,360|0.734|0.734|
|d64|295,432|0.0249|0.0249|
|Depth3,only width512 tested|525,832|0.315|0.0679|
|Depth4,only width512 tested|787,976|1.651|0.361|
|8 declared queries|66,312|2.210|1.217|
|60 declared queries|66,312|2.471|1.091|

Harmonic also passes at width256 for d2/d3, with66,312/66,568 learned coordinates.
The d64 width256 candidate fails condition18.098>16; SiLU width512 fails17.341>16;
m16 width512 fails21.863>16. These are inconclusive construction outcomes, not
measured approximation failures. d784 width256/512 candidates cannot retain the
mandatory full first-layer span, whose rank is at least784 almost surely.
The dense pair still ran; reference final training MSE3.95e-5. No dimension-free
practical-storage claim is supported by this implementation.

Depth3/4 dense final training MSEs are0.000487/0.000169, compared with compressed
0.000482/0.000127. The SiLU andm16 dense models also fit (MSE0.00900/0.00264),
so absence of compressed results must not be blamed on a failed dense task.
For d>2 the toy target uses only the first three coordinates, rescaled with d;
this changes ambient dimension, not the number of target-relevant coordinates.
Every dataset's training labels have RMS1; m16 also changes that normalization.
Panel sizes8,30,60 all pass at66,312 learned coordinates. This is a coarse
sufficient-size observation, not proof of independence from panel size.

Reproduce each case with the existing `run --config <study-json>` command.
The queue used the first case's immutable `source.py` for subsequent cases,
so ongoing additions to plotting code could not alter its scientific executable.
Regenerate figures with `/home/amir/miniconda3/bin/python -B
paper/figures/capture_trajectory.py appendix-sweep-plot`. Complete candidate
tables, exact failure reasons, timings and fixed-coordinate counts are in
`data/generated/paper_appendix_pilots_20261009/sweep_metrics.json` and the
generated figure metrics/captions. Configs are flat in this study directory.

## Completion and recommendations

The final root consistency check verified all39 sweep fit arrays against saved
hashes, finite values,65 common time points, recorded training losses and exact
learned+fixed totals. The transfer hashes and frozen geometry check passed;
all five transfer fits also completed. Scoped checks independently reconstructed
spectral tail ranks and plotting metrics. These are software/data-consistency
checks, NOT the intentionally deferred Euler refinement or independent-seed
replications. The research-experiment skill kept hypotheses, fixed budgets,
failures and claim levels separate; canonical notation was used in interpretation.

Keep the spectral figure as the strongest new positive mechanism illustration;
the scope scatter is a useful companion to the main equal-budget figure.
Include transfer as an honest limitation: autonomous changed-label learning is
observed, but dense-level source transfer fails at this tested budget. Dimension,
architecture and cost drafts expose current implementation qualifications.
The flat panel-size draft and fixed-budget-ratio draft are secondary; neither
establishes an asymptotic rate. Equation-changing ablations are deliberately
deferred. No paper theorem/text has been changed, no promotion is claimed,
and no further runs are pending.

## User-requested feedback fixes (new bounded continuation)

The user supplied a review of the eleven drafts and authorized strategic fixes,
prioritizing high leverage and deferring exorbitant campaigns. Preserve the
original pilot results; new outputs are under `feedback/`. Continue this study
as corrections/validation of the same empirical investigation. The supplied
feedback is an input, not automatically an established conclusion.

Priorities frozen before new runs: (1) strict 1x selection, learned AND total
storage, censored budget crossings, and smallest-selected-model timewise ratios;
(2) check factorized low-rank dynamics against autograd and distinguish them
from fixed-right projected updates; (3) replace uniform coordinate search in
the three conditioning failures with one deterministic selector, same budget,
same condition cap16 and no additional source truncation; (4) panel-span first
layer, with an exact finite-panel small-step oracle and explicit basis storage;
(5) three independent dense pairs per width using identical reference/partner
seed lists across widths, on sphere3 and raw MNIST if available; (6) one
Euler half-step check for dense and compressed trajectories; (7) targeted
budget bracketing rather than a full eight-size multi-seed campaign.

Standard new fits remain L2 tanh,m8,p30,T32,h0.00625,float32,TF32off, source
RK4h0.125/degree8 unless a case explicitly tests SiLU,m16 or refinement. Each
fit/source retains120s cap, total new GPU work bounded to25min per device.
Reference seeds901/902/903 and independent partner seeds1901/1902/1903 are
fixed across widths1024/2048/4096. Report empirical means/SD; any fitted
c/sqrt(n) curve is descriptive, not a replacement for actual dense-pair errors
or a certificate. Existing one-seed compressions remain one-seed evidence.

The panel-span implementation may only discard input directions orthogonal
to ALL training and declared query inputs. It must count its d-by-r fixed
projection basis and state that off-panel decoding has no equivalence guarantee.
Never normalize projected inputs. No initialization-only source claim follows.
The conditional new-model pilots are d784 and MNIST at n2048,width256/rank15;
if a numerical/construction gate fails, report it rather than escalating size.
Conditioning has at most three rebuilds and three successful-gate fits, no
trial/width grid. Tiny deterministic solver/control checks are not training
campaigns. More replication, larger spectra and broad joint size/seed searches
are deliberately deferred until these basic corrections have passed.

Root owns this record, dense-pair/refinement/budget probes and Git. Scoped
helpers own revised plotting, panel projection/data loading, and selector/control
checks in the SAME existing paper script. Shared edits preserve original defaults.
No new theorem or paper-scope change is authorized by a successful pilot.

Final bounded follow-ups, fixed before execution: extend the identical source
spectral measurement to widths4096/8192, at most120s each and no retries. For
MNIST, the first budget search spent its three requests on128/127/129, all
inconclusive constructors. Correct the proposal rule to move upward across a
constructor failure, without counting it as an accuracy failure, and allow at
most two further candidates. Preserve all failed requests on continuation;
only actual measured accuracy failures can establish a lower crossing bound.

### Completed corrections and bounded results

All reported error ratios below compare query RMS with the coupled dense run
against an independent dense pair on the SAME task, query panel and recorded
time grid. A pass requires both endpoint RMS and maximum-over-recorded-times
RMS to be no larger than their respective dense-pair benchmarks. A ratio of
maxima is not pointwise domination. The timewise figure separately displays
the pointwise ratio, omitting time zero where both numerator and denominator
vanish. Unless stated otherwise, results use one compression seed, not three.

#### Presentation and storage

`feedback/figures/figure2_storage` now shows learned and total storage separately,
labels the dense formula, marks left-censored minima and missing passes, and
separates overlapping markers. No exponent is fitted to the coarse pilot grid.
`figure3_accuracy` also has both storage axes. `figure4_training` selects the
same smallest tested passing model as Figure2, plots error/dense-pair error
at each recorded time, and explicitly labels the nonpassing Harmonic witness.
The strict criterion leaves Harmonic without a circle pass at widths2048/4096.
It changes the old raw8x8-digits Logarithmic selected widths to256/384/512;
the previous flat line is not retained as evidence of a measured minimum.

These regenerated main figures still identify their original circle/8x8-digits
tasks in their titles. Sphere3/MNIST now have new baseline replications and
midwidth compression probes below, but the entire main-figure size sweep has
NOT been migrated to those tasks. Existing fixed-budget ratio curves likewise
retain their original paired runs; new denominators are not substituted into
old compression trajectories.

The saved cost-bars figure is replaced by a table separating source compilation,
assembly, training and query timings, learned/fixed storage and leading MAC
counts. `feedback_controls.md` defines those counts and their exclusions.
Reported process CUDA peaks include other resident models and are not isolated
model peaks. The panel-span implementation also retains its projection basis;
its scalar count must not be hidden in a claim of dimension-independent total
storage. One-off source work still consumes a complete dense trajectory.

#### Panel-span implementation and correct tasks

The opt-in `methods.non_oblivious.logarithmic.panel_span` uses an orthonormal
basis of all training and declared query inputs, and projects the first-layer
weights and inputs without renormalizing them. Dense first-layer velocities
lie in the training-input span; consequently projection preserves the coupled
dense dynamics on the declared panel, up to the recorded numerical rank
tolerance. Hidden weights/readout are unchanged. This is a coordinate change,
not PCA and not a certificate for the subsequent empirical source truncation.
Off-span queries can be evaluated but have no equivalence guarantee.

The tiny float64 oracle checks full-rank, redundant, rank-deficient and zero
panels. Maximum state/prediction/velocity discrepancies are1.34e-15,3.56e-17,
9.72e-17 respectively. Float32 device/restart checks also passed. Reproduce
with the `panel-span-check` subcommand.

Dimension784 and raw MNIST1-vs-7 pilots use n2048, m8, p30, compact width256,
source rank15 and panel rank38. Both retain75,528 learned +226,401 fixed
scalars, including the29,792-scalar784-by-38 projection. Endpoint and
maximum-recorded ratios are0.37055 on the spherical task and0.83939 on MNIST.
The spherical dense trajectories match the original dimension784 pair bitwise.
MNIST uses the official training/test split, four training examples per class
and fifteen test examples per class, raw784 coordinates and no PCA. Only test
inputs, never test labels, enter source construction. Cache/download options
are explicit in the common dataset config. Evidence: `feedback/panel_d784/`
and `feedback/mnist/`; corresponding configs are `feedback_panel_d784.json`
and `feedback_mnist.json`.

The paired-baseline runs use reference seeds901/902/903 and partner seeds
1901/1902/1903, fixed across every width. Each task finishes18 dense fits.
Endpoint query RMS mean +/- sample SD is:

| Dense width | Sphere3 | Raw MNIST1 vs7 |
|---:|---:|---:|
|1024|0.01791 +/-0.00783|0.03485 +/-0.00777|
|2048|0.01063 +/-0.00394|0.02299 +/-0.00372|
|4096|0.00835 +/-0.00468|0.01367 +/-0.00189|

GPU queues took73.0s and72.5s respectively, including scoring/plotting. Any
fitted inverse-square-root guide is explicitly descriptive. It does not replace
measured thresholds, and these are not three independent compression trials.
Evidence/plots: `feedback/pairs_sphere3/` and `feedback/pairs_mnist/`; reproduce
using `feedback-dense-pairs --config feedback_pairs_<task>.json` with the full
study-relative config path and a fresh output directory.

#### Targeted budget measurements

Refinement reuses hash-verified dense trajectories and reconstructs the same
largest-rank source basis and selector seed. Intermediate ranks are fixed by
the existing width-to-rank rule; no seed or source search is performed.

| Task at n2048 | Method | Failed width | Passing width | Passing endpoint ratio | Learned | Fixed | Total |
|---|---|---:|---:|---:|---:|---:|---:|
|Sphere3|Harmonic|288|320|0.89339|103,688|307,200|410,888|
|Sphere3|Logarithmic|224|256|0.92511|66,568|196,609|263,177|
|MNIST|Logarithmic|192|224|0.80575|58,920|180,321|239,241|

The brackets are11.1%,14.3%,16.7% wide. They are observed local crossings,
not proofs of monotonicity or global minimum, and no interpolated unmeasured
model is presented as a successful construction. Worst-recorded ratios for
the passing rows are0.51186,0.53004,0.80575. The MNIST failed width192 ratio
is1.49709; the previous width256 model remains a valid, slightly worse witness.

The first MNIST search wasted its three requests at128/127/129 on constructor
failures. The corrected proposal rule moves upward across a construction
failure without converting it into an accuracy failure, preserving all past
requests on continuation. Exactly two follow-up candidates192/224 closed the
local bracket. Evidence is in `feedback/budget_sphere3/`, `budget_mnist/`,
and `budget_mnist_followup/`; the corresponding JSON plans reproduce each
bounded stage using `refine-budgets --plan <path>`.

#### Numerical and baseline checks

The sphere3 representative half-step repeats both dense runs, Harmonic512/r37
and Logarithmic512/r37 at0.003125 instead of0.00625, keeping the identical65
recorded times. Their maximum coarse/fine RMS divided by the coarse dense-pair
maximum is respectively0.01253,0.01260,0.02806,0.02834. All pass the predeclared
0.1 numerical gate. This is one representative test, not a continuum theorem
or a validation of every smaller-budget/activation/sample-size run.
Evidence: `feedback/refine_sphere3/` and the original `dimension_d3/` arrays.

Pivoted-QR/log-determinant coordinate selection is opt-in, keeps the entire
given source span, and uses the unchanged condition cap16. It fixes the
dimension64 width256 constructor and obtains0.67862 endpoint/worst ratio.
It also builds the16-example width512 model, but the latter's half-step change
is3.129 times the endpoint and6.520 times the maximum dense-pair benchmark.
Its original poor accuracy is numerically unresolved, not evidence of an
intrinsic source-approximation obstruction. SiLU width512 still fails the
constructor gate; one width768 follow-up builds but has endpoint ratio1.35382
and maximum-recorded ratio0.44550. No further rescue fits were made.

The low-rank implementation passes automatic differentiation and induced-metric
checks. A fixed-right, full-rank additive oracle reproduces dense Euler to
8.89e-16. Training BOTH factors changes the induced matrix metric, even at full
rank, so full-rank LoRA is not required to follow dense Euler thereafter. No
baseline equations were changed and optimal baseline tuning is not claimed.
Detailed definitions, checks, conditioning results and their follow-up are in
`feedback_controls.md`; tiny checks rerun through `feedback-control-check`.

#### Transfer and controlled scope

The pooled-source test uses the old target plus two fixed Rademacher-label
source tasks, pooling then truncating to the SAME rank15 and compact width256.
It retains the same storage and never uses the new target's rollout in those
sources. Transferred endpoint/worst ratios worsen from9.963/9.575 to
15.026/15.050; target-specific rebuilt sources remain0.802/0.771. The old-only
comparison reproduces previous predictions bitwise. Construction conditions
pass. This fixed-budget pool does not solve source transfer; it is not a proof
that all pooling schemes fail. Evidence and plot: `feedback/pooled_transfer/`.
One denied-CUDA launch before model construction is retained separately as an
infrastructure failure, not silently treated as a scientific trial.

The controlled distance test uses d10, n2048, three declared anchors and two
fixed geodesic directions per anchor, at nine distances. Its54 new query
inputs are excluded from all source construction. The maximal angle0.42323
is less than half the minimum inter-panel separation, so the chosen anchor
remains nearest. Endpoint RMS rises from0.03739 to0.05585 for width256 and
from0.01134 to0.02886 for width512, versus dense-pair0.03986 to0.04184.
Zero-distance approximation error is measured, not artificially subtracted.
Plot: `feedback/scope/controlled_query_paths`.

The companion d10 fixed-budget panel test uses8/30/60 declared queries, with
separately built sources at each panel size. Endpoint ratios at width256 are
0.6249/0.7343/0.8097, and at width512 they are0.04858/0.3779/0.4141. It displays
accuracy at fixed budgets, not a flat bottom-of-grid minimum. The d10 target
still depends on the first three coordinates, an explicit intrinsic-complexity
qualification. Plot: `feedback/scope/fixed_budget_panel_size`; both scope
figures reproduce via `feedback-scope-pilot --config feedback_scope.json`
using the full study-relative path, or its plot-only option on saved data.

#### Spectral extension

The unchanged circle source-history measurement now includes dense widths4096
and8192; these GPU workers finished in9.93s and22.86s. Full spectra are measured,
not capped at the construction's retained rank. The minimum rank for the stated
relative Frobenius tail of the residual top-layer feature history is:

| Dense width | 1% tail | 0.1% tail | Tail tolerance0.01 sqrt(512/n) |
|---:|---:|---:|---:|
|512|42|104|42|
|1024|44|111|51|
|2048|44|115|61|
|4096|45|117|72|
|8192|45|117|83|

Histories are sampled at common temporal holdouts after mandatory-span removal.
The shrinking tolerance is motivated by dense fluctuation scaling but is a
source-history relative error, NOT a direct prediction-error certificate.
The five-width pattern is empirical and does not establish an asymptotic law.
Coefficient spectra remain auxiliary diagnostics, not a separate headline
figure. Evidence is in `feedback/spectral_n4096/`, `feedback/spectral_n8192/`
and the original `spectral_history/`. Reproduce the new workers with
`appendix-spectral --worker-width 4096 --out <fresh-output> --device cuda:0`
(and8192), using the same paper script and Python interpreter as above.
The updated `feedback/figures/appendix_response_history_spectra` shows all five
widths and both fixed and shrinking-tolerance rank requirements.

#### Remaining limits and final consistency check

Defer the full eight-budget x three-compression-seed x all-width x two-task
campaign: it multiplies these targeted probes into hundreds of source/fit
jobs. In particular, a replicated asymptotic compression curve, complete
sphere3/MNIST replacement of all main panels, finer16-example integration and
tuned activation/baseline sweeps remain undone. No new expensive search is
pending or implied by this record. The current empirical source compiler still
uses a full-horizon RK4 dense rollout (step0.125); training is Euler, not setup.
Neither cheap initialization nor initialization-jet-only implementation has
been demonstrated by these experiments.

The final root consistency check parsed all feedback configs and the single
script, verified hashes and common65-point grids for42 completed standard
trajectories, checked finite arrays and learned+fixed=total storage, recomputed
every refined budget classification, and verified both three-pair datasets.
Tiny panel-span and low-rank checks were rerun after integration and passed.
The original data, failed constructors and mixed-step failures are preserved.
The research workflow kept finite-grid successes distinct from numerical
qualification failures, empirical mechanisms and theorem-level claims.
