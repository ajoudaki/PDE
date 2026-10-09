# First drafts of paper Figures 2–4

## Scope and frozen first-pass design

User requests quick first versions, not final numerical certification or a
multi-seed campaign. This new study uses the assigned maintained implementation
paper/figures/capture_trajectory.py and established docs only; no other study's
results or arrays are inputs. All fits are fresh. Root owns configuration,
extra-query scoring and runs; scoped helpers own matched-budget controls and
the three-panel-pair plotting routine in that same executable.

The empirical question is whether existing nonlinear response compressions
match independently initialized dense variability using less learned state,
and outperform ordinary size-matched controls. Failure on a dataset/budget is
retained; the intended visual message is a hypothesis, not a required outcome.

Two tasks: circle inputs (d=2), and sklearn's raw8x8 digit images1 versus7
(d=64), normalized to unit norm, no PCA. Each has8 training examples,30 declared
query inputs and30 separate undeclared queries; labels from both query panels
are used only after prediction. Panel membership is fixed before model runs.
Same dataset seed47 across widths1024,2048,4096. One reference seed901,902,903
respectively, plus the role-hashed independent same-width dense partner. All
models use two tanh hidden layers, canonical Gaussian initialization, zero
readout, squared loss and original block mobilities. Euler step0.00625,T32,
65 observations at spacing0.5; float32 runtime, float64 initialization, TF32off.
No half-step numerical audits or seed replication in this first draft.

Legendre orders1,2,4; circle Harmonic and Logarithmic compact widths128,256,512,
with source ranks5,15,37. Image Logarithmic widths256,384,512, source ranks8,16,32.
Harmonic is excluded from images. Source setup is the optimized existing GPU
implementation: full-horizon RK4 step0.125, degree8 temporal coefficients,
float64 coefficient assembly,64 coordinate-selection trials andcondition16.
Harmonic circle degree5 uses input-geometry quadrature. These are empirical
rank truncations and offline dense rollouts, not a demonstration of the
initialization-jet-only theorem or the full untruncated coefficient spaces.
No setup-time speedup or asymptotic compression theorem is inferred.

At4096 only, small dense widths and BudgetLoRA ranks are chosen by exact learned
counts to fit every requested compression budget, rounded down and deduplicated.
Impossible rank-one budgets are disclosed rather than silently overspent.
Low-rank retains both frozen Gaussian matrices. Frozen features are a dashed
reference; their width-n readout is trained, with fixed dense features additional.
Learned and fixed storage are recorded separately throughout; learned-state
compression must not be described as total-storage compression for Legendre.

Figure2 selects the smallest TESTED size in each family that satisfies BOTH
endpoint and worst-recorded query RMS <=3 times the corresponding independent
dense-pair discrepancy. This is the previously user-accepted constant-factor
criterion; it is not pointwise domination or a global optimal-budget search.
Report missing passing candidates honestly. Three widths do not justify a
fitted logarithmic exponent or asymptotic scaling claim. Figure3 uses all tested
4096 budgets, endpoint RMS, and separately marked undeclared Logarithmic error
against the dense predictions on that same undeclared panel. Figure4 uses the
selected passing budget per family (largest complete tested candidate if none,
explicitly labelled), dense-pair RMS throughout time, and matched controls.
Zero initial errors are not plotted on log axes. The observed dense discrepancy
is one realized pair, not an estimated standard deviation.

Each model/setup has a120s wall cap. One dataset queue per GPU, at most12min
per queue. No further widths, seeds, rank/selector searches, source rescue,
adaptive search or numerical refinements. Finite completed inaccuracies are
failures; incomplete/nonfinite/domain/conditioning failures are inconclusive.
No failed run is hidden or reclassified merely to achieve the intended message.
Root may render partial drafts as jobs finish. Stop after these six configs;
publish the three draft figures, scope/cost captions and recommendations.

Generated outputs belong in data/generated/paper_figure_drafts_20261009/.
The six task-width JSONs freeze all run settings. Reproduction uses
`python -B paper/figures/capture_trajectory.py run --config <task_width.json>`
and `python -B paper/figures/capture_trajectory.py paper-draft-plot --manifest
studies/paper_figure_drafts_20261009/figures.json`. Rendering is diagnostic; the
main paper is not rewritten to assert unrefined single-seed findings as final.

## Status

Design frozen before numerical runs. Existing source/readout/mobility algebra
tests were reused; the new data-panel and matched-budget interfaces passed
tiny CPU checks. All six numerical configurations subsequently completed with
83 complete fits and no reported errors or skips. Full resolution/seed audits
remain deferred as requested; this is empirical first-draft evidence only.

### Exploratory display update during the first batch

Figure4 will use the largest complete tested compression in each family rather
than the minimum3x-passing budget. This separates its question (best achieved
trajectory fidelity within the displayed budget ladder) from Figure2's minimum
tested size. Selection depends only on requested size and run completeness,
not a search over favorable time windows. All budgets remain visible inFigure3;
Figure2 and the fixed3x criterion are unchanged. Captions give the selected
state counts. This is an explicitly exploratory first-draft display decision,
not a newly preregistered confirmatory test. No numerical runs are added.

## First-draft results

Circle queue elapsed478.56s and digits queue360.19s, on separate RTX3090 GPUs.
Each includes all three widths, controls at4096, setup, training and recording.
No additional seed, width, order, selector search or step refinement was run.
Raw batch timings and every config/source/trajectory hash are retained in the
generated namespace. Each task-width root records the saved source, resolved
config and trajectories; only plotting was polished after completion.

Figure2 smallest tested passing learned-state counts (both endpoint and worst
recorded RMS must be <=3 times their respective dense-pair discrepancies):

| Task | Width | Legendre | Harmonic | Logarithmic |
|---|---:|---:|---:|---:|
| Circle |1024|35842|66312|66312|
| Circle |2048|104450|66312|66312|
| Circle |4096|143362|263688|263688|
| Digits1/7 |1024|99330|excluded|82184|
| Digits1/7 |2048|198658|excluded|82184|
| Digits1/7 |4096|397314|excluded|82184|

This supports a flat tested Logarithmic budget on raw images, but the circle
budget jumps at4096. The coarse ladder provides upper bounds on a sufficient
tested size, not certified minima or logarithmic asymptotics. No exponent is
fitted to three points. Learned-state savings exclude fixed matrices/metrics;
the generated captions and metrics expose those separately.

At4096, the endpoint RMS versus the coupled dense reference is:

| Model | Circle | Digits1/7 |
|---|---:|---:|
| Independent dense |0.00695505|0.00837822|
| Legendre, order4 |0.00129434|0.000234429|
| Largest Logarithmic, width512 |0.00194260|0.00639487|
| Largest Harmonic, width512 |0.01497291|excluded|
| Matched small dense, width512 |0.01235313|0.01967630|

The width512 dense control is matched to width512 compact learned storage to
within the compact model's eight residual coordinates; it is not the budget
match for order4 Legendre. Figure3 includes Legendre's own matched controls.
Legendre order4 and Logarithmic width512 lie below the independently initialized
dense-pair RMS at every one of the64 positive recorded times on both declared
panels. Harmonic does not: it exceeds the pair on37 of64 circle observations,
and its endpoint error exceeds its width512 small-dense control. Thus the
proposed universal favorable message for every method/size is not supported.
Figure4 shows these exceptions rather than suppressing them.

Logarithmic's undeclared digits endpoint RMS at width512 is0.01003316, compared
with0.00639487 on declared inputs and0.00833281 for the dense pair on that same
undeclared panel. On the circle the undeclared endpoint RMS is0.00226502, still
below the corresponding dense-pair discrepancy. This demonstrates a scope
distinction, not universal failure on unseen inputs. Different panels need
their own dense baseline; their errors are not directly interchangeable.

## Checks, scope and handoff

A scoped read-only reconstruction checked exact learned/fixed counts for all
45 compressed models and all30 matched-control target comparisons. Extra
query panels are disjoint from both training and declared queries; their
labels never enter training or source setup. Plot checks validate saved hashes,
common grids, complete runs, exact RMSs, and selection rules. These software
checks do not replace the deliberately deferred half-step and seed studies.
The baseline is one realized independent dense pair per width, not a confidence
interval. Recording65 times does not establish a continuous-time supremum.
The offline source rollout and empirical source truncation are not the paper's
initialization-only compiler or an asymptotic logarithmic certificate.

The research-experiment skill kept the fixed cases/thresholds and adverse
outcomes visible; no witness failure was reinterpreted as a theorem failure,
and no success was promoted beyond the empirical claim level. Recommended
first-paper drafts are Figure3 for equal-budget comparison and Figure4 for
trajectory fidelity of Legendre/Logarithmic. Figure2 remains exploratory until
denser budget bracketing and independent repetitions resolve its sensitivity.
All requested drafts are delivered; no further runs are pending.
