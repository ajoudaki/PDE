# Fixed-budget tests across sample count and sphere dimension

Frozen before scientific training, 2026-10-04. Continuation of the practical
sampling experiments; no mathematical approximation theorem is inferred.

## Question and reference

Does the previously successful rank-16 initialization-only sampler with total
state budget P(n)=2550[log(n)/log(512)]^4 retain its accuracy on more samples,
close inputs and higher-dimensional query spheres? If not, can a fixed budget
multiplier and response-rank increase repair the observed failure?

The reference remains the realized canonical two-hidden-layer width-n tanh
network, Gaussian read-in/mixer, zero readout, no biases, physical mean-squared
loss flow with mobilities (n,1,n). Inputs x=sqrt(d)u have unit directions u.
All blocks train. The smaller weighted network uses only its own residuals,
selected read-in, small learned mixer, readout and fixed positive masses.
Construction sees initialization, labels/training directions and fixed setup
probes; it never sees trained states or evaluation predictions. This practical
truncated witness is not the full initial-derivative theorem construction.

For m samples in dimension d, equal selected widths N retain exactly
N^2+(d+1)N moving and 2N+m(d+1) fixed scalars. Both count against the budget.
The m-dependent factor 2/m must multiply every physical velocity; using the
old two-input factor would change the experiment's clock.

## Fixed configurations

The companion generator saves every actual direction and label in JSON.

1. Two circle points separated by 15 degrees, labels (.1,.1).
2. The same pair with labels (.1,-.1).
3. Four circle points theta_j=7 degrees+j*pi/4, labels
   .15*cos(theta_j)+.05*sin(theta_j).
4. The same four points, labels .15*cos(3*theta_j).
5. Eight circle points theta_j=7 degrees+j*pi/8, smooth labels as in item3.
6. The same eight points, labels .15*cos(theta_j)+.05*sin(3*theta_j).
7. Item5 embedded in R^3, evaluated over the full two-dimensional sphere.
8. Item5 embedded in R^5, evaluated over the full four-dimensional sphere.
9. Four tetrahedron vertices in R^3, labels (.15,-.1,.1,-.15).
10. Eight fixed Gaussian-normalized directions in R^3, labels .15*u1+.05*u2.
11. Eight fixed Gaussian-normalized directions in R^5, same label rule.
12. Item10 directions, labels .15*u1+.15*u1*u2*u3.

Circle inputs contain no exact antipodal pairs. Sphere inputs are checked for
duplicates/antipodes; they remain fixed across widths and network seeds. The
embedded cases separate unchanged intrinsic training geometry from expansion
of the prediction domain. No uniformity over all data or a theorem's numerical
small-label threshold is asserted.

32 fixed setup probes are used in each dimension: the old half-circle grid
for d=2 and independent normalized-Gaussian directions for d>2. Evaluation
uses the old 257-point circle grid or 512 fixed normalized-Gaussian sphere
directions from a distinct seed. In d=2 an antipodal coincidence with one
setup direction is retained for comparability and disclosed. Query panel
doubling uses the same circle points as a subset, or a sphere prefix extension.

## Main test and criteria

Widths 512,1024,2048; two new network seeds9411,9412, each with independent
dense copy seed+10000; all12 configurations. Shared seed identifiers form
clusters, not72 independent draws. Baseline uses rank16 and budget multiplier1.
No sampler fitting tolerance is changed. Construction failures and unsuccessful
final optimization are separate from observed prediction inaccuracy.

Primary E is sqrt(mean_query(max_saved_time |f_small-f_dense|^2)). Also retain
maximum-time query RMS, endpoint RMS, dense-copy discrepancy, and E restricted
to the common initial horizon [0,120]. Use full-sphere prediction RMS, not
training error or classification accuracy. A task-budget pair passes only if
all six prescribed baseline runs are complete, have valid construction,
sqrt(n)E<=.15, and numerical settlement. For adapted candidates the confirmation
subset is reported explicitly rather than called a complete baseline sweep.
Median scaled E at2048 divided by that at512 must be <=1.5; also
report the ratio on the common [0,120] interval to expose unequal-horizon
effects. These are empirical criteria, not asymptotic rate tests.

Float64, TF32 off, Heun physical dt=.2, observations every1. Start at T120;
every120 thereafter stop when all actual models have training residual RMS
<=1e-6 and maximum endpoint-relative query excursion over all observations
in the last10 units <=1e-5. Absolute cap T1200. Unsettled endpoints remain
inconclusive for endpoint accuracy; valid finite-time errors remain reportable.

## Prespecified follow-up branches

For a task with invalid construction, sqrt(n)E>.15, or failed growth criterion,
test increased budgets on seed9411 at n2048. Candidates are exactly:
2x budget/rank16, 2x/rank24, 4x/rank32. To bound cost, group tasks as close
pairs, multi-input circle, embedded sphere d3, embedded sphere d5, full sphere
d3, full sphere d5; use the worst completed scaled-error task per group
(construction failures precede metric ranking). At most six diagnostic cases.
Failure only to settle does not itself trigger an increased budget.

Choose the smallest multiplier passing each diagnosed group; for ties use the
smaller worst error, then smaller rank. This is adaptation, not independent
confirmation. Confirm chosen candidates on seed9412 at n512 and2048 for each
triggered task, as remaining budget permits, recording missing confirmations.
No further rank, node or solver optimization is permitted in this campaign.

Two resolution checks are permitted/required before calling a successful new
budget validated: worst completed circle reduced discrepancy and worst sphere
reduced discrepancy, repeated at half time step, twice observation frequency
and doubled nested query panel. Compare same-point/time numerical errors
separately from quadrature variation. Same-point error and primary-metric
change on the common query set must be <=max(1e-4,.05*E) for the compared
model; sphere panel change is descriptive quadrature sensitivity, not a time
solver failure. If a check fails, label conclusions numerically unresolved;
do not launch a refinement search.

## Bounds, preservation and stopping

Hard cumulative active GPU-worker union budget25minutes, at most two workers,
at most8GiB allocated per worker. Main workers each get at most900seconds;
follow-ups/refinements must fit the remaining cumulative budget. Check actual
worker timestamps/durations. Maximum72 main,6 diagnostic,24 confirmation,
2 refinement cases. Interrupted/failed runs remain archived; incomplete
predeclared cases can resume unchanged within these totals/budget, but do not
replace seeds or delete failures. Stop after these branches or budget cap.
No CPU scientific training if GPUs unavailable. No manuscript/maintained-code
or Git writes. Every run archives sources, configs, versions, precision,
hardware, seeds, raw queries/predictions, setup defects, final restart and
status. Old files stay unchanged.

Root owns generator/configs/protocol/report and README. multidata_runner owns
new sampler adapter/runner; multidata_design owns analysis/design check;
multidata_audit owns independent implementation/evidence audit. Scope is this
study and directly used maintained APIs. These are internal research checks.
