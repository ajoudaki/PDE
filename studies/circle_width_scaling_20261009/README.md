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
