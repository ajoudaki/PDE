# Dense training after structured initialization: frozen protocol

**User correction during the principal run (after approximately1323 of2016
trajectories): the only scientific objective is agreement of the predicted
whole-circle function with the canonical Gaussian dense network. Similar
test error against the teacher is explicitly not success.** All trajectories
already retain the needed paired circle predictions, and none of the models,
tasks, seeds, training rules or numerical checks are changed. The risk-based
decision rules below are superseded and retained only as protocol history.

The revised primary metric is
`D=RMS_circle(f_candidate-f_canonical_Gaussian)`, with absolute RMS,
relative RMS `D/RMS_circle(f_canonical_Gaussian)`, and sampled maximum absolute
discrepancy all reported. Analyze matched-fit endpoints and common physical
times separately. Gaussian-versus-Gaussian function discrepancy is contextual
initialization variability; matching it does NOT satisfy the user's objective.

As an explicit descriptive screen, report whether the upper95% paired-seed
bootstrap bound on mean relative function RMS is at most5%, with all12 seeds
fitted and all numerical gates passed. Also report worst-seed discrepancy,
not just the mean. This5% screen is an operational choice, not a user-specified
tolerance or a theorem. Actual errors and curves remain the primary evidence.
The revised metric precedes analysis or selection of a winning candidate.

User-authorized empirical continuation, 2026-09-26. This tests the initialized
matrix substitution before attempting any scalar or history compression.
No historical study code or result is an input. The exact task inventory
below is the scope of this campaign; it is not claimed to exhaust every
configuration in older studies.

## Model and candidates

Two bias-free tanh hidden layers, equal width n, normalized circle direction
u(theta)=(cos(theta),sin(theta)), first preactivation w u, output c^T h2/n.
Unhalved mean squared training loss and physical GF mobilities (n,1,n).
All weights train unrestricted, including every entry of the middle matrix.
No structural projection, low-rank truncation, closure, frozen features,
Fourier approximation, or resampling of the middle matrix during training.
First entries are N(0,1); readout entries are N(0,1/n^2).

Middle initializations, all materialized as dense arrays:

1. `gaussian`: iid N(0,1/n), the reference.
2. `gaussian_control`: independent middle Gaussian, same outer weights.
3. `hd`: normalized Walsh H times independent sign diagonal.
4. `hdhd`: D1 H D2 H D3, all independent sign diagonals.
5. `fastfood`: S H G Pi H B, normalized H, Gaussian diagonal G,
   random permutation Pi and signs B. Set S_i=chi_n/||G||_2 using independent
   chi-square(n) draws, so its row norms have the Gaussian row-norm law.
6. `reflection4`: D1 H D2 H D3 with exactly four negative central signs;
   this is the fixed-rank-interaction full-rank construction relevant to the
   proved compression theorem.
7. `diagonal`: independent signs on the diagonal, a full-rank local control.

The random streams are explicit and independent. At each width/seed every
method shares exactly the same initial first weights and readout. The middle
matrix draw is reused across tasks. There is no outcome-dependent tuning of
initialization scale. The signed orthogonal matrices have Frobenius squared
norm n; Gaussian and Fastfood match that scale in expectation.

## Tasks

The executable source of the exact task definitions is `circle_tasks.py`.
All targets are odd under theta -> theta+pi, as required by this architecture.
Every task retains a target function on the full circle, separate from its
finite training subset. Angles below are radians; no labels contain test noise.

- `pair_cos1`: cos(theta), training at (0,0.9).
- `pair_cos3`: cos(3 theta), training at (0,pi/3).
- `near_pair_sin9`: sin(9 theta), training at (-pi/18,pi/18).
- `triple_cos3`: cos(3 theta), at (0,pi/5,-pi/5), the maintained book's
  Chapter 14 fixed correlated-three-input risk example.
- `triple_mixed`: 0.6 cos(theta)+0.25 sin(3 theta)+0.15 cos(7 theta),
  at (0.13,1.02,2.41).
- `cluster_triple_cos9`: cos(9 theta), at (-pi/9,0,pi/9).
- `broad_ridge6`: tanh(3 cos(theta-0.35)), at
  (0,0.22,0.8,1.45,2.23,2.9).
- `sharp_ridge8`: tanh(10 cos(theta-0.37)), at
  0.07+j*pi/8, j=0,...,7.
- `alternating3`: cos(3 theta), at j*pi/3, j=0,...,5.
- `alternating5`: cos(5 theta), at j*pi/5, j=0,...,9.
- `alternating9`: cos(9 theta), at j*pi/9, j=0,...,17.
- `multiscale12`: the mixed target above, at
  (0.03,0.24,0.61,0.94,1.19,1.66,1.92,2.21,2.58,2.83,3.07,4.31).

These cover sparse interpolation, correlated/opposing labels, localized
nonlinear ridges, and increasingly difficult oscillations. They do not test
non-odd activations, biases, noisy labels, or other depths.

## Hypotheses and metrics

H1: structured initialization preserves attained circle test RMS closely
enough to justify investing in its scalar compression. H0: it changes
fitting or the selected whole-circle predictor materially on at least part
of this task suite. A third outcome is similar risk but different predictors.

Primary metric: sqrt(mean_circle (f-target)^2), using 4096 equispaced
directions. Also retain normalized error (divide by target circle RMS),
training MSE, physical fitting time, hidden activation motion, and middle
weight motion. Never infer fitting from test risk alone.

For each structured/Gaussian pair retain RMS_circle(f_struct-f_gaussian).
Compare that with RMS_circle(f_gaussian_control-f_gaussian), separating
initialization variation from systematic model differences. Save the actual
circle predictions so every risk and discrepancy can be recomputed.

Widths 128 and 256; seeds 0,...,11; all seven methods and twelve tasks:
2016 principal trajectories. Seeds are the replication unit. Report paired
means, medians, standard deviations and 95% bootstrap intervals (20000 fixed
resamples) per task/width. Intervals are descriptive per-comparison intervals,
not simultaneous confidence guarantees over the entire suite.

For risk equivalence, predeclare margin
delta = 0.02*target_RMS + 0.05*mean_Gaussian_test_RMS.
A cell passes the strict screen when its paired-mean 95% interval lies
inside [-delta,delta] and both methods fit. Clearly separated intervals
outside this band are adverse evidence; overlap without containment is
inconclusive. Report direction: a lower structured risk can fail two-sided
equivalence while being beneficial. The separate noninferiority margin is
0.10*target_RMS. Do not select only favorable tasks or seeds.

## Training, numerical checks and conditional branches

Float64 explicit Heun physical-flow integration, provisional dt=0.05.
A numerical pilot may lower dt before the principal suite. It may not select
candidates or tasks. Verify manual RHS against maintained finite-network GF,
loss directional dissipation, transpose action, initializer ranks/scales,
and step refinement before interpreting results.

Integrate genuinely to common time T=300, saving observations at T=100 and
300, and retain the first state reaching training MSE<=1e-6. Continue rather
than freezing a fitted state when reporting common-time results. Save a
second threshold at 1e-8 when reached. Report threshold comparisons and
fixed-time comparisons separately. The 1e-6 snapshot gives the primary
matched-fit endpoint; 1e-8 sensitivity checks whether stopping matters.

Runs not reaching 1e-6 by T=300 continue conditionally to T=1500. If still
not fit, continue to T=3000 within the total resource limit. Retain all
nonfitting runs and label their endpoint comparison unresolved or adverse,
never silently exclude them from the fitting-rate denominator.
All principal trajectories through T=300 take priority over continuation.
Continuation is a separate phase using retained final dense states, in the
same deterministic seed/task/width/method order. Extended trajectories stop
at the fitting threshold; their endpoints are not called common-time results.

Numerical refinement: all seven methods, seed 0, both widths, on
triple_cos3, near_pair_sin9 and alternating9 at half dt; refine additional
task/method cells if loss grows by >1e-7 in a step, a state is nonfinite, or
coarse/fine circle prediction RMS exceeds 0.002*target_RMS. A failed cell is
not certified merely by taking another random seed. Double the final circle
grid from 2048 to4096 and require risk change <=1e-4*target_RMS; failing
cases use8192 and retain the discrepancy.

Continuation validity addition, before extended runs: repeat all seven
methods at width256, seed0, on each of the three slow ridge/multiscale tasks
(broad_ridge6, sharp_ridge8, multiscale12), from initialization at half dt
through the same stopping rule and maximum horizon. This checks long-horizon
numerics, not candidate selection. It changes no scientific task, metric,
equivalence margin or training horizon.

At most 2800 trajectory segments including pilots, continuation/refinements; at
most 60 wall minutes for the numerical campaign, 8 worker processes with
one BLAS thread each, and 4 GiB aggregate target memory. Before starting the
principal suite, use a small runtime pilot to check feasibility; reduce
the plan only explicitly and before viewing scientific comparisons. Record
unfinished work if the cap is reached. Numerical validity, not agreement,
controls refinement. Do not begin a scalar-compression experiment in this
campaign.

Budget bookkeeping correction made during the principal run, before any
continuation: the original2600-segment allowance undercounted the already
declared full continuation branch (2016 main +504 possible slow-task
continuations +84 numerical pilot trajectories +12 smoke trajectories
=2616). The corrected2800 allowance also includes21 long-horizon numerical
checks. The wall-time/worker limits and scientific selection criteria are
unchanged. No user-imposed compute budget was increased.

## Provenance and outcome

Use a fresh directory under data/generated/structured_full_rank_scalar_20260926.
Retain the configuration, source hashes, Git HEAD (including dirty source
hashes), Python/NumPy/SciPy and BLAS settings, commands, seeds, per-run status,
timings, complete metrics and circle prediction arrays. Source and analysis
live in this study. Findings are empirical for this fixed suite and finite
widths; they cannot establish Gaussian universality or a scalar-closure bound.
