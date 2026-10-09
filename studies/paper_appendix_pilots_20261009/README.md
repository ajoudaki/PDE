# Bounded appendix figure pilots

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
