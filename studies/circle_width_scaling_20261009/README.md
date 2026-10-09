# Circle width-scaling pilot

## Question and scope

New study for the user's five-width test: how much learned state is sufficient
for each existing compression to match an independent same-width dense run?
This is a bounded exploratory calibration, not a proof of a logarithmic exponent.
Inputs are the user-requested implementation in paper/figures/capture_trajectory.py,
its public JSON interface, and established docs. No other study's results or
arrays enter this pilot. The existing sphere3 display remains a separate task
context; no real-image campaign is launched before this circle pilot is reported.

## Frozen experiment

Use widths512,1024,2048,4096,8192, one reference/independent-dense pair per width,
reference seeds701 through705 respectively, deterministic role-hashed independent
partner seeds. All share circle data seed47:8 training points,30 equally spaced
query inputs with angular offset0.137, target sin(3theta)+0.5cos(5theta), rescaled
to unit training-label RMS. Two tanh hidden layers, Gaussian canonical weights,
zero readout, mean squared training loss, mobilities(n,n,1) in(A,w,B) order.
All runtime models use float32 Euler h0.0015625,T32,20480 steps,65 saved times.
TF32 off, one CPU thread, one width job per RTX3090. No small-dense, low-rank,
frozen-feature, new digit-task or additional seed fits in this stage.

Logarithmic compact widths are ceil(c*(log n)^1.5), c=6,12,24. Thus its candidate
learned storage is cubic-logarithmic up to the explicitly retained lower terms.
Harmonic tries constant widths100 and200, then ceil(200*sqrt(log(n)/log(512))),
ceil(200*log(n)/log(512)), ceil(400*log(n)/log(512)); duplicates are removed.
These test constant, linear-log and quadratic-log learned-storage envelopes,
with a second quadratic-log prefactor. Legendre orders are
ceil(c*(n/512)^0.25), c=1,2,4. Compact source rank is
max(1,floor((compact_width/4-17)/3)), leaving approximately fourfold coordinate
oversampling of the source span. These are empirical ranks, not the full certified
source orders. Fixed geometry/matrix storage is always counted separately.

At d2,m8,L2 the exact learned/fixed counts are: dense n^2+3n /0;
Legendre (16q+19)n+2 /n^2+2q; Harmonic b^2+3b+8 /3b^2;
Logarithmic b^2+3b+8 /3b^2+1, where b is compact network width and q is
Legendre order. Source arrays are temporary setup state, not retained runtime
state. Both spectral methods currently use full-horizon dense RK4 setup at
step0.125, degree8 temporal fits and float64 coefficient assembly. Harmonic uses
degree5 Fourier modes and32 independent quadrature nodes; Logarithmic includes
the30 declared query inputs but never their labels. The experiment does not
certify initialization-only setup or accuracy on undeclared Logarithmic inputs.

## Metrics, branches and stopping

User-requested revision during the first two widths: accept2 times dense
variability as the primary comparison and3 times as a secondary comparison,
each for BOTH endpoint and maximum-recorded RMS. This replaces the original
1-times analysis threshold below, not the saved trajectories. The already
launched frozen numerical jobs retain their stricter1-times early-stop rule;
rescoring all completed candidates at2/3 requires no reruns and preserves
the original data, tested ladder and budget. Display both thresholds explicitly;
do not portray this revised threshold as the original preregistration.

H1: one modest cubic-log storage coefficient suffices for Logarithmic over the
five tested widths, and low-log-power budgets suffice for Harmonic. H0: this
particular empirical implementation requires larger budgets or loses accuracy.
The original numerical early-stop rule requires BOTH final query RMS and
maximum-recorded query RMS versus the coupled reference to be no greater than
the corresponding independent-dense discrepancy. The revised analysis applies
the factors2 and3 to each benchmark separately. Record ratios and full curves.
Also measure pointwise exceedances: the two primary scalar tests do not imply
the compression error is below the dense pair at every time. No sphere-supremum,
continuous-time GF, endpoint-convergence or asymptotic certificate is inferred.

Try candidates in increasing learned size and stop a family after its first
passing candidate. Larger unused candidates are explicitly marked skipped.
Report smallest tested passing size, not an optimal size. Constructor-condition
failure(>16 after64 candidates), truncation, nonfinite output, wrong grid/data
or timeout is inconclusive; do not replace seeds or relax gates. A finite
completed inaccurate candidate is a fail. Final training MSE is reported;
T32 need not give interpolation on this oscillatory circle target.

Original cap:120s per source construction/fit, at most63 fits plus10 shared source
setups across the five widths, and25min total numerical-job wall clock. The user
allowed a brief extension to finish the same batch: only the existing timeout
watchdog was paused, with an independent five-minute deadline to resume it.
No additional candidates, widths or seeds were launched. Two GPUs
run widths in parallel. No extra orders, numerical-refinement batch, new seeds,
condition-trial searches or rescue after this frozen ladder. Stop when all five
widths or the cap is reached and report failures/unbracketed minima honestly.
Any fitted power is a descriptive fit to selected five-point data, not a recovered
asymptotic exponent; changing the selected prefactor can dominate that fit.

Root owns configuration, run scheduling, stop-after-match implementation, this
record and Git. A scoped agent owns only scaling/time plotting in the same
executable; a separate read-only check covers saved arrays and reported costs.
Generated products stay in data/generated/circle_width_scaling_20261009/.
The five n*.json files are the complete frozen numerical configurations.

## Execution record

Five-width batch ran on both GPUs, queues(512,2048,8192) and(1024,4096),
under a1500s outer timeout. All jobs execute the same frozen snapshot at
data/generated/circle_width_scaling_20261009/software_stop/source.py,
SHA2564798c58ad336f6c6f335bc81ee2166bd046e40a998c326eb6368807f6560342d.
This captures the maintained executable immediately after the stop-after-match
addition; later plot-only changes cannot alter the queued numerical runs.
The tiny CPU software check(16 neurons,10 Euler updates,3 fits) confirmed that
the first passing Legendre candidate skips the larger order explicitly. All five
scientific configs passed schema validation. No software fixture contributes
scientific evidence. Plot-only support separately passed synthetic checks for
both error thresholds, missing/failed/skipped candidates and NPZ hash rejection.
The final batch completed all scheduled attempts in1618.35s (26min58s), with52
complete saved trajectories and10 shared source constructions. Per-width job
wall times were479.25,530.42,527.81,571.30,599.68s. These are whole budget
searches, not per-model setup times. The watchdog emitted shell exit124 when
resumed after the batch-complete record; no numerical job was left unfinished.

Reproduce one width with the maintained executable (or its recorded snapshot
for exact source identity), replacing512 with any of the five widths:

```sh
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py run --config studies/circle_width_scaling_20261009/n512.json
```

## Checked pilot results

All five independent dense pairs reached T32. Their reference training MSEs
range from0.003081 to0.003558. The dense-pair endpoint/worst-recorded query RMSs
are, in increasing width order:
0.011112/0.044305,0.013790/0.037675,0.010482/0.026717,
0.006431/0.015234,0.006029/0.009172.

Smallest **tested** passing learned-state counts (both endpoint and maximum
recorded RMS must pass):

| Dense width | Legendre,2x or3x | Harmonic,2x | Harmonic,3x | Logarithmic,2x | Logarithmic,3x |
|---:|---:|---:|---:|---:|---:|
|512|17922|40608|40608|141006|35538|
|1024|52226|40608|40608|48626|48626|
|2048|104450|240596|49958|64776|64776|
|4096|208898|no passing candidate|286766|83816|83816|
|8192|417794|no passing candidate|58812|106608|106608|

At3x, selected Harmonic widths are200,200,222,534,241; selected Logarithmic
widths are187,219,253,288,325. The selected Legendre orders are1,2,2,2,2.
Every selected3x Logarithmic width equals ceil(12*(log n)^1.5): the frozen
cubic-log learned-storage schedule passes at all five widths. Its endpoint
ratios are2.373,1.288,1.857,1.559,1.422; its worst-recorded ratios are
0.700,0.850,1.356,0.998,0.935. Its half-prefactor schedule fails throughout.
At2x, width512 needs the next tested Logarithmic budget; the other four do not.

The frozen largest Harmonic schedule ceil(400*log(n)/log(512)), whose learned
storage grows quadratically in log n, also passes3x at every width. Smaller
passing budgets are noisy, including a large budget at4096 and a much smaller
one at8192. Do not interpret a log-power regression on these selected minima
as the smallest possible exponent. A descriptive fitted exponent near3 for
the minima does not contradict the tested quadratic-log upper schedule;
the latter uses a larger common prefactor. The Logarithmic fit near3 reflects
the imposed schedule, not an independently recovered exponent.

At8192 the dense model has67133440 learned coordinates. Selected3x Harmonic
has58812 learned plus174243 fixed, total233055:1141x learned compression but
288x total compression. Logarithmic has106608 learned plus316876 fixed,
total423484:630x learned and159x total. Legendre retains67108868 fixed
coordinates in addition to417794 learned; its learned-state reduction must
not be described as a comparable total-storage reduction.

Three width100 Harmonic candidates (dense widths2048,4096,8192) failed the
float32 runtime feature-Gram positivity check. They are inconclusive, not
accuracy failures; no ridge or rescue was added. Their run-level complete
flags remain false even though later candidates completed successfully.
The final, larger-than-needed width650 Logarithmic candidate at8192 failed
the source-condition gate:16.0128928 exceeds16 after64 selections. This is
also inconclusive; the smaller width325 model already passes2x and3x.
Other finite completed candidates that exceeded the accuracy threshold remain
failures. All selected models use the same65 observation times and their own
width's coupled reference. Source/config/data/trajectory hashes and exact
storage counts were checked, with a separate read-only reconstruction from NPZ.

The stronger pointwise-in-time claim is **not** established: the selected8192
Harmonic model exceeds3 times the instantaneous dense-pair RMS at28 of the64
positive-time observations, despite passing the endpoint and maximum tests.
The result is a finite-panel, finite-time Euler pilot using full-horizon source
setup and empirical source ranks. It is not an initialization-only result,
a no-fixed-rank certified construction, an unseen-input Logarithmic guarantee,
a proof of asymptotic storage, or a continuous-time/sphere-supremum certificate.
One pair per width and query-based budget selection provide no independent
post-selection confidence or evidence ruling out lazy/low-rank explanations.

For the paper, the width-versus-learned-state plot is useful as an explicitly
exploratory scaling figure, with the3x rule and fixed storage disclosed. The
time-curve figure is useful precisely because it prevents the false stronger
claim of pointwise dominance. No new image-data panel, undeclared-input test,
baseline campaign or additional seeds were run in this stage.

Final generated outputs are
data/generated/circle_width_scaling_20261009/factor2/plots/plot_004/ and
data/generated/circle_width_scaling_20261009/factor3/plots/plot_003/.
Each contains storage_vs_width, trajectory_errors and errors_vs_width as PNG/PDF,
metrics.json with exact counts/errors and input hashes, and captions.txt.
Regenerate without numerical work (change factor3 to2 in both places for2x):

```sh
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py scaling-plot \
  --runs data/generated/circle_width_scaling_20261009/n512 \
         data/generated/circle_width_scaling_20261009/n1024 \
         data/generated/circle_width_scaling_20261009/n2048 \
         data/generated/circle_width_scaling_20261009/n4096 \
         data/generated/circle_width_scaling_20261009/n8192 \
  --out data/generated/circle_width_scaling_20261009/factor3 \
  --factor 3 --fit-log-powers
```

## Authorized adaptive continuation (frozen before new fits)

The user requested measure-first budget refinement on the same five dense pairs,
then plotting and only then descriptive fitting. Reuse all old trajectories;
do not retrain either dense reference or change seeds, data, time grids, numerical
gates or the3x endpoint-AND-maximum criterion. Refine Harmonic and Logarithmic
network width; test Legendre order1 where only order2 has passed so far.

Use the smallest known passing upper width and largest completed accuracy-failing
width below it. Refine the midpoint until upper/lower<=1.2, or integer adjacency
for Legendre. If there is no failing lower observation, halve the passing width
until one is found or the minimum allowed order passes. Existing upper brackets
make a doubling phase unnecessary for this continuation. At most4 new candidate
evaluations per family/width,40 new spectral evaluations and4 new Legendre fits,
120s per fit/setup,25min total numerical batch; no retries or extra seeds.
On a numerical/constructor failure, retain it as inconclusive and select the
nearest untested midpoint within the same valid bracket; never treat it as an
accuracy-failing lower bound. At the cap, report the unresolved bracket.

Preserve the original rank rule max(1,floor((q/4-17)/3)) and each family's original
largest source rank. Rebuild that source once from the hash-verified Gaussian
initialization and original seed, then slice its nested prefixes. Increasing the
source maximum changes the randomized SVD, so no such extension is allowed here.
This measures the existing implementation's one-parameter width/rank family,
not separately optimized source orders. Original dense and reused candidate
outputs retain their explicit old-source provenance; new fits are separately
identified. Every newly requested budget is persisted before evaluation.

Errors need not be monotone (Harmonic241 passes but289 fails at8192). The20%
criterion is therefore a local sampled fail/pass bracket, not a global optimality
guarantee. Preserve all contrary observations.20% in width also allows up to
roughly44% in quadratic storage. Plot smallest tested passing states, show raw
budgets and failures in the accompanying metrics, and fit powers only afterward.
No new proof, independently validated scaling exponent, paper edit or broad
baseline campaign is part of this continuation.

Run the continuation from its single plan:

```sh
timeout --signal=TERM --kill-after=10s 1500 /home/amir/miniconda3/bin/python -B -u \
  paper/figures/capture_trajectory.py refine-budgets \
  --plan studies/circle_width_scaling_20261009/adaptive.json
```

The frozen numerical source is
data/generated/circle_width_scaling_20261009/adaptive/source.py,
SHA25628b37d9d7a569eddae30ca0e26265f642cfe583b61d43d21e245c05d27e2f4ab.
Before launch, synthetic tests covered20% brackets, integer/minimum orders,
inconclusive midpoint handling and nonmonotonic observations. AST comparison
confirmed that dense/compact constructors, both source builders, Legendre,
integrator and initialization helpers were unchanged from the original pilot.
A scoped read-only check found no scoring/reuse blocker. The frozen launcher's
aggregate exit code does not propagate child failures, so each child exit and
each per-family final bracket is checked explicitly; search_complete alone
means execution finished, not that every local bracket is resolved.

### Adaptive results (supersede the pilot's smallest-tested budget table)

All five width jobs exited0. The continuation took approximately812s (13min32s),
with24 new completed fits:4 Legendre,7 Harmonic,13 Logarithmic. No new source,
constructor or fit failure occurred. The old pilot's failures remain recorded.
All dense trajectories and data were reused bit-for-bit. The earlier sufficient
schedules remain valid; they were not measurements of minimum required storage.

| Dense width | Legendre order | Harmonic fail/pass width | Logarithmic fail/pass width | Legendre learned | Harmonic learned | Logarithmic learned |
|---:|---:|---:|---:|---:|---:|---:|
|512|1|150/175|140/163|17922|31158|27066|
|1024|1|125/150|110/123|35842|22958|15506|
|2048|1|200/222|158/174|71682|49958|30806|
|4096|1|400/467|252/288|143362|219498|83816|
|8192|2|200/220|223/244|417794|49068|60276|

All spectral brackets are within20% in width. For Legendre, order1 is minimal
at the first four widths; the last is resolved by integer adjacency (order1
fails maximum-time accuracy, order2 passes), not by a20% ratio. Nonmonotonicity
at8192 Harmonic remains recorded, so these are local sampled brackets, not
global-optimum certificates. The source rank/width rule and all other source
settings stayed fixed; this is not a joint optimization of hidden orders.

Only after completing the searches, unweighted least squares of log learned
state against log(log n) gives Harmonic43.0916*(log n)^3.50871 and
Logarithmic29.2349*(log n)^3.52513. Log-space RMS residuals are0.62762 and
0.38574 respectively. Both fits are descriptive over five independent dense
pairs, not asymptotic exponents or evidence that the minimum power is3.5.
The small log-width range and noisy budgets do not resolve quadratic versus
cubic logarithmic growth. Logarithmic uses less learned state at four of the
five widths. At8192, Harmonic has49068 learned+145200 fixed=194268 total;
Logarithmic has60276 learned+178609 fixed=238885 total, versus67133440 dense.

The final saved-array check reconstructed all classifications/counts/brackets,
verified hashes and unchanged dense/data/time arrays, and confirmed24 complete
new fits without errors. A scoped read-only agent independently checked the
same facts. No new Euler refinement, repeated-seed validation or promotion is
claimed. The maintained launcher's child-exit propagation was fixed after the
frozen numerical launch; no running source or numerical function was changed.

Final figures and their full metrics/captions are under
data/generated/circle_width_scaling_20261009/adaptive/final/plots/plot_001/.
Regenerate them with the same scaling-plot command above, inserting adaptive/
before each n* directory, setting --out to the adaptive/final directory, and
retaining --factor3 (as separate CLI tokens: --factor 3) and --fit-log-powers.
Progress figures omitted fitted curves; adaptive figures also omit the old
theoretical n^(5/4) guide so a prescribed rate is not presented as measured.

## One additional width:16384

The user requested one additional point, not additional repetitions or a new
campaign. Use reference seed706 and its role-hashed independent dense partner,
the same data/architecture/Euler grid and3x endpoint-AND-maximum criterion above.
The previous five runs remain unchanged. The512-update timing probe projected
192s per dense fit; the user explicitly approved a300s cap for these two dense
fits only. Source setup and compression fits remain capped at120s. The pair
and subsequent search share a1500s outer wall-clock cap.

The complete numerical configs are n16384.json and adaptive_16384.json here.
First run the dense pair only. Then search Legendre from order1 up to8 and
Harmonic/Logarithmic from width256 up to1024, doubling until a pass and then
using the same local20% refinement. Allow at most8 evaluations per family;
stop with an unresolved/inconclusive record if a cap or numerical gate prevents
completion. Both spectral sources use a fixed maximum rank79 (the rank rule
at width1024), with nested prefixes throughout the search; never recompute a
new randomized source at each candidate width. Source settings/selection gates
and empirical rank rule are unchanged. The new source maximum is fixed before
seeing any16384 compression errors. No certified full-source claim is made.

The runner now supports bounded doubling for a fresh dense pair and an explicit
dense-only runtime cap. Numerical constructors, source algorithms, integrators,
data and initialization helpers are unchanged. The plotter verifies each saved
whole-file hash and recursively compares the numerical definitions across source
versions, allowing these scheduling/plotting changes without pretending all
runs used one file hash. Original hashes remain in the plot provenance.

Run the new point with:

```sh
timeout --signal=TERM --kill-after=10s 1500 bash -c \
  '/home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py run --config studies/circle_width_scaling_20261009/n16384.json && /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py refine-budgets --plan studies/circle_width_scaling_20261009/adaptive_16384.json'
```

### Checked16384 result

The combined batch exited0 within its wall-clock cap. Both stages used source
SHA256727d11c2a0572ddfa173fad645a91b254ac17a5253c407b6dd37d8042bf9fdc5.
Reference seed706 and independent partner83709591014928178 completed in222.68s
and253.98s, with final training MSE0.00334687 and0.00331080. Their endpoint and
maximum-recorded test RMSs are0.001536952691 and0.006051064310. The stricter
endpoint benchmark is a measured property of this pair, not a changed threshold.

| Method | Passing order/width | Learned | Fixed | Total | Endpoint RMS | Maximum-recorded RMS |
|---|---:|---:|---:|---:|---:|---:|
| Dense |16384|268484608|0|268484608|0.001536953|0.006051064|
| Legendre |3|1097730|268435462|269533192|0.002524973|0.002673401|
| Logarithmic |512|263688|786433|1050121|0.002540978|0.002540978|

Legendre endpoint/maximum ratios are1.64284/0.44181. Order2 fails the endpoint
test (4.88907x), resolving the integer-adjacent2/3 bracket. Logarithmic ratios
are1.65326/0.41992. Width448 fails the endpoint test (4.32286x), resolving the
448/512 bracket with ratio1.14286. Width384 also fails at3.83674x endpoint;
errors are not monotone even among these failing points. The selected width512
uses source rank37. Logarithmic compresses learned storage by1018.19x and total
retained storage by255.67x. Legendre's fixed quadratic storage remains additional.

Harmonic has **no passing point from this bounded search**. Width256 gives
endpoint/maximum RMS0.020940546/0.031642383 (13.62472x/5.22923x); width512 gives
0.022744556/0.022744556 (14.79847x/3.75877x). Both are completed accuracy failures.
Width1024 is not an accuracy failure: its constructor condition21.6753085
exceeds the unchanged limit16 after64 selections, so it is inconclusive.
The search stops at its predeclared cap, without retries, a new selector seed,
an altered rank rule or a relaxed conditioning gate. This does not establish
that no other Harmonic budget can pass; the16384 Harmonic point is omitted.

There were10 complete new compression fits (4 Legendre,2 Harmonic,4 Logarithmic)
and one constructor failure. The compression search took883.86s; the dense-pair
stage took480.26s including initialization/recording, approximately22min44s total.
Legendre fits took98.63--111.13s, Harmonic50.69--51.45s and Logarithmic63.00--63.60s.
Harmonic source setup took30.61s. All numerical fits respected their caps.

One final read-only reconstruction checked the seeds, hashes, common65-point
time grid, raw RMS metrics, exact storage counts and final brackets. Original
16384 data/dense arrays were reused bit-for-bit. The combined figure's first
five selected points and dense-pair metrics exactly match the previous figure.
The numerical-definition fingerprint matches the two earlier source versions.

The six-width plot is under
data/generated/circle_width_scaling_20261009/adaptive_16384/final/plots/plot_001/,
with PNG/PDF figures, metrics.json and captions.txt. Regenerate using the earlier
scaling-plot command with the five adaptive/n* roots plus
data/generated/circle_width_scaling_20261009/adaptive_16384/n16384,
--out data/generated/circle_width_scaling_20261009/adaptive_16384/final,
--factor 3 and --fit-log-powers. The Harmonic fit still uses only the original
five passing widths (power3.50871). The descriptive six-point Logarithmic fit
has power5.19661 and log-space RMS residual0.47683. Its change from the five-point
fit illustrates sensitivity to the measured threshold and selected budgets;
neither fit establishes a logarithmic asymptotic exponent. All earlier finite
panel, empirical-rank, full-rollout and no-independent-post-selection caveats
continue to apply. No further numerical work is pending in this extension.

## Targeted Euler performance correction

The user requested a short code diagnosis/fix, not another scientific campaign.
Two avoidable costs were found: DeepDense formed an n-by-n derivative and then
performed a separate weight update; fixed-horizon integration also scanned the
entire state and recomputed training loss every8 steps. The saved16384 reference
timings were197.48s training,24.89s loss/finiteness checks and0.25s queries.

Exact DeepDense instances now use a fused addmm_ Euler mixer update from saved
pre-update fields. Subclasses retain their own RHS. Fixed-horizon diagnostics
run at observations and at most256 updates apart, while loss-based stopping
retains its8-step cadence. Full-state finiteness is still checked; detection
can be delayed to the next check. Already queued GPU updates can overrun a wall
cap by up to a block, recorded in the existing timing report. No step size,
horizon, model precision, TF32 setting or mathematical dynamics was changed.

The existing euler_small_checks now also compares fused updates to the original
RHS for depths1,2,5 and all6 activations: maximum float64 state difference
1.39e-17. Loss-stop, shortened final step, observation grid and unchanged initial
state checks pass. One scoped code review checked old-state dependency ordering,
exact-type dispatch and diagnostic cadence; no further audit campaign was run.

One1024-step GPU comparison used the same16384 seed706 circle configuration,
float32, TF32 off, h0.0015625,T1.6, record_every320 and a16-step untimed warmup.
The old integrator came from the frozen n16384/source.py; both integrators used
identical initial state and inputs. On RTX3090, elapsed time fell9.3784s to5.8981s
(1.5901x), training8.1775s to5.8080s and checks1.1584s to0.0731s. Prediction
maximum difference was7.45e-9; state maximum difference2.38e-7. Incremental
peak memory was unchanged (2952986624 bytes); no peak-memory reduction is claimed.
Full-horizon timing extrapolates to117.96s but was not measured again. The short
check is under data/generated/circle_width_scaling_20261009/euler_performance_check/timing.json.
No saved scientific trajectory or figure was replaced. Numerical implementation
hashes change, so old and new runs must not silently be treated as identical code.

### GPU-resident observations and source fitting

The next user-requested correction removes avoidable device/host transfers.
Training inputs and weights were already GPU-resident, but Euler/RK4 copied
each recorded prediction to CPU; source observers copied dense fields to CPU,
Harmonic fitted coefficients there, and Logarithmic later copied fields back.
Predictions/report scalars are now buffered on the simulation device and
exported at the end. Source snapshots remain on device; Harmonic fitting uses
GPU batches of512 neurons rather than CPU batches of64. Logarithmic no longer
round-trips its source observations. Source buffers therefore consume VRAM,
not host RAM; no claim of reduced peak setup memory is made.

Fixed-horizon intermediate finiteness flags are accumulated on device and all
validated before results return; failures are not silently accepted. Loss-stop
decisions still read a scalar, and model-internal Cholesky/domain/zero-clock
gates remain immediate. Wall-clock GPU synchronizations remain. One-off
CPU initialization/source hashing also remains for coupled-run provenance;
this is outside the training loop, not repeated dataset/weight streaming.
Small prediction snapshots use clone to protect against mutable state aliases.
Euler/geometry checks and a scoped device/aliasing review passed.

A single short comparison against commit764ae21 (so both sides already have
the fused Euler update) is saved at
data/generated/circle_width_scaling_20261009/gpu_transfer_check/timing.json.
The same16384 seed706 dense run,1024 steps toT1.6, took5.8320s before and5.8865s
after: no demonstrated training speedup. States and predictions were bitwise
identical; final training MSE0.9621078968. The5 recorded38-input predictions
occupy only760 bytes, consistent with reporting copies not being the dense
runtime bottleneck. This was not another complete training run.

At width2048,8 training points and the same circle data, T32 RK4 step0.125,
degree8 and source rank14, complete Harmonic setup fell1.9057s to1.3242s
(1.439x); new-partition Logarithmic setup fell4.8995s to3.7431s (1.309x).
Source-subspace relative differences were4.61e-15 and5.61e-15. These are
single short implementation comparisons, not repeated timing estimates or
new compression-accuracy evidence. No old result array or figure was changed.

### Legendre and low-rank hot-loop check

The next targeted implementation check covered LegendreCompression and the
active BudgetLoRA baseline, plus the older LoRA helper in the same executable.
Neither low-rank RHS transfers data to the CPU. BudgetLoRA unnecessarily
recomputed two forward projections in its gradient calculation; these are now
reused within each call. The older LoRA reuses its one analogous projection and
now initializes its factors with the reference dtype rather than the global
default. No persistent cache or extra retained state was introduced.

A trial combined Legendre's domain and zero-clock decisions into one scalar GPU
synchronization and used addmm for its dense-plus-low-rank actions. It showed
no meaningful speedup and was reverted when the user requested no further
optimization without an obvious problem. Legendre is unchanged. Both methods
still pay for their frozen dense mixer's forward/reverse actions. The retained
low-rank edit changes no dynamics, parameter budget, integration step or storage.

A more aggressive low-rank rewrite using backward-projection reuse and fused/
reassociated arithmetic passed the tiny algebra checks but changed a float32
trajectory by0.00064754, exceeding the preset2e-6 implementation tolerance.
That rewrite was discarded. The retained narrower version is bitwise identical
to the old state and all recorded predictions in the targeted GPU check.
The trial Legendre state/predictions were also bitwise identical in that check.

Timing used RTX3090, TF32 off, one CPU thread, float64 initialization and
float32 Euler, n4096,m8,d2,L2,tanh, reference seed704, dataset seed47 and30 query
points from n4096.json. Legendre used order3; BudgetLoRA hidden rank24 and
first rank2, with adapter seed _experiment_seed(704,'low_rank_24'). Each run
used2048 updates of0.0015625 toT3.2, record_every320, with16 untimed warmup
updates. Old/new/new/old timing order compared commitf6a4b3f against the saved
updated source hash. Mean elapsed seconds were4.4857/4.4832 for Legendre
(no meaningful improvement) and3.5778/3.3266 for BudgetLoRA (1.076x).
These short runs are not converged training: final training MSEs are0.8978975
and0.0913349 respectively, unchanged by the edits. Learned/fixed counts remain
274434/16777222 and208900/16785408 respectively.

Tiny CPU checks cover Legendre's explicit-matrix/product-rule oracle, zero
flow and invalid clocks, both low-rank autograd gradients, full-rank induced
mobilities, storage budgets, and float32 legacy initialization with a float64
global default. Maximum gradient error is2.22e-16. A scoped read-only review
checked projection reuse and the shared clock gate; no broad audit or new
scientific experiment was launched. Full timing reports, configuration, hashes,
the discarded-candidate failure and check results are in
data/generated/circle_width_scaling_20261009/legendre_lowrank_performance_check/timing.json.
The final code restores the original Legendre implementation; its unchanged
low-rank class definitions match those in the timing check. No more benchmarks
were run after the user's stop instruction. The benchmark harness initially
called the legacy autograd oracle under
no_grad; rerunning that oracle outside no_grad passed. No saved scientific
trajectory, accuracy comparison or figure was replaced.
