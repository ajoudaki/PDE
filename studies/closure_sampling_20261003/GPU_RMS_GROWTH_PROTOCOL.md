# Bounded RMS state-growth continuation

2026-10-03. User-authorized continuation of the completed GPU sampler study.
This protocol is frozen before the new training results. Prior maxima and
RMS evidence are calibration context, not new confirmation. Use both RTX
3090 devices; no CPU training if GPUs become unavailable. No shared code,
manuscript, other study, index, or remote writes.

## Target, comparison and permissible construction

Empirically identify a sufficient retained-state schedule for approximating
the realized canonical dense two-hidden-layer tanh model at circle RMS error
C/sqrt(n), throughout observed training and at settled endpoints. Preserve
the Gaussian reference initialization, zero readout, mean squared loss,
mobilities (n,1,n), both learned hidden layers, and all learned small-mixer
coordinates. The smaller weighted network uses only its own residuals.
Setup may use the original initialization and the prescribed training task;
it never consumes trained dense snapshots or future residuals.

Continue the practical low-order sampler, not the full theorem construction.
Use `neuron_sampling_setup.py` unchanged, with 32 initialization-only probe
directions (previous sweep: 16), explicit basis rank, mass floor .05 and
singular tolerance 1e-10. All retained masses and the complete learned mixer
count: P(N)=N^2+5N+6 for N selected neurons in each layer. Temporary original
initialization/setup arrays and experimental dense controls are excluded
from model state, but their setup cost is reported. Archive selected Gram
defects, source truncation, both mixer-direction defects and optimizer status.

H1: enough response rank and positive cubature nodes remove the observed
error floor at a slowly growing state budget. H0: this bounded response
construction retains a systematic trajectory/predictor error even with more
nodes. Distinguish these by varying rank and node count separately.

## Error and controls

Let e(t,x) be small minus reference output. Primary metric is

    E = sqrt(mean_j max_recorded_t |e(t,x_j)|^2).

This is the RMS of the time supremum used in the preceding clarification.
Also report max_t sqrt(mean_j |e(t,x_j)|^2), endpoint RMS, and the earlier
maximum norm. Use 257 equally spaced offset full-circle queries. Dense-copy
controls use independent seed seed+10000 on the identical physical clock.
Keep frozen-feature controls as in the first campaign. Record both hidden
feature motions and training residuals. RMS does not mean classification risk.

Choose the width-independent empirical ceiling C=.15 before new training,
with C=.10 as a stricter secondary diagnostic. The previous dense-control
median sqrt(n)*E was .219,.114,.083 at n=512,1024,2048. This empirical C is
not a theorem constant or a certified population quantile. Report paired
ratios, but do not select using an unusually small individual dense baseline.

## Calibration and fixed selection rule

Calibration uses seed 8411, widths 512,1024,2048, angles 90 and 60 degrees,
and labels (.2,.1) and (.2,-.1): 12 cases. Test N in {24,48,96} with
rank in {8,12,16}; additionally rank24 at N48 and N96. No stochastic sampler
restarts or searches over seeds. The same setup probes and tolerances apply
to every rank. Changing rank changes the number of product moments; it is
not itself a pure neuron-count experiment.

Select the smallest anchor N for which a single rank has max sqrt(n)*E <=.10
over all twelve calibration cases and all relevant fits and numerical checks
pass. At the same anchor N, choose the rank with the smallest worst-case
calibration error; break exact ties by smaller rank. Rank does not increase
retained runtime state. This tie rule was clarified before the first new
training run. An intermediate cubature optimizer warning
does not discard a case; report it. Final optimizer failure or removed selected
frame modes invalidates that candidate for positive selection.

If no calibration candidate passes, the only expansion is N192 at ranks
12,16,24 on the same twelve cases. Stop with an unresolved practical-bias
finding if none of these passes. This is an explicit futility branch, not
a license for unlimited sampler tuning. The user requested a confident
growth rule; inconclusive evidence must not be described as such a rule.

## Fresh-seed validation and growth schedules

After calibration, freeze the selected rank and anchor state P0=P(N0) in a
separate hand-written selection artifact before any holdout run. For each
p in {0,1,2,4}, impose

    P_budget(n)=P0 [log(n)/log(512)]^p,

and choose the largest integer N with P(N)<=P_budget(n). Deduplicate models
within a case. Rank stays at the selected calibration value. Every model
still selects/reweights neurons from that case's own initialization.

Validation widths are 512,1024,2048,4096; reference seeds 8511--8515; both
angles and label signs: 80 cases. The repeated seed numbers across widths
and geometries are treated as clusters, not eighty independent samples.
All four schedules and every failed/unfavorable instance are reported.

A schedule is empirically sufficient over this grid only if all held-out
trajectories have sqrt(n)*E<=.15, all settle and pass validity gates, and
each geometry/sign cell's median sqrt(n)*E grows by at most 1.5 between
512 and 4096. A clear violation rejects this tested schedule under that
criterion, not its asymptotic exponent. Report maxima, medians, individual
points and seed-cluster bootstrap descriptive uncertainty; small replication
cannot justify universal or strong high-probability conclusions.

If any schedule passes, one additional extrapolation at n8192 uses reference
seed 8611 and all four geometry/sign cells, testing the smallest passing p
and p4 as a conservative control. The same ceiling and settlement gates apply.
It is a four-case stress, not a new rate fit or a confidence certificate.
No exponent is called optimal. A finite width range cannot distinguish
polylogarithmic growth from small powers or an eventual approximation floor.

## Numerical validity and budget

Reuse the already checked maintained-code-compatible batched equations and
run their deterministic RHS/Heun, weighted autograd and restart tests. Add
a metric oracle showing the two RMS/time orders differ. Float64, TF32 off,
dt=.2, observations every 1, physical T120 with whole-case extension to240
if a moving model has residual RMS>1e-6. Settled requires residual<=1e-6
and last-ten-unit query change<=1e-5. Otherwise no endpoint claim.

Half-step checks at n4096, seed8511, angle60, opposite signs, and the held-out
case with the largest scaled error for the smallest passing schedule (or p4
if none passes). Use dt=.1 and doubled nested query/time panels. Require
matched prediction difference <=min(1e-4,.05*dense-copy E) and primary-metric
change <=that threshold. If needed, exactly one further dt halving is allowed
for these checks; unresolved discretization forbids a positive claim.

Hard campaign budget: 25 wall-clock minutes of actual experiment execution,
two workers, <=8GiB GPU allocation each, at most 12 initial calibration,
12 expansion, 80 validation, four extrapolation and four resolution cases.
Do not use this cap to launch every optional branch automatically. Stop if
budget or futility criteria apply. Initialization setup counts toward runtime.
No change of sampler algorithm, jet order, labels or data after observing
this campaign is allowed under this protocol.

## Evidence and outputs

New runner/configs/report live in this study; generated output roots start
`gpu_rms_growth_20261003_`. Archive exact commands/configs/source hashes,
environment and device settings, raw query/training/feature traces, reduced
restart arrays, setup diagnostics, every status/failure, and derived figures.
The previous campaign remains unchanged. The report and README distinguish
calibration from held-out evidence, actual counts from growth labels, and
sampled finite-time findings from mathematical all-time guarantees.
