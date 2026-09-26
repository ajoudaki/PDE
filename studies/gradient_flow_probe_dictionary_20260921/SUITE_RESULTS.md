# Derivative dictionary: eleven original width2048 tasks

The 38-vector derivative dictionary improves on the nearest archived45-vector
old closure in8/11 tasks, and on each random baseline in10/11. All44 endpoint
comparisons underlying this statement pass numerical gates and independent
raw-state checks. Both selected numerical levels agree on every direction.
Its mean per-task circle RMS is 0.135539, compared with 0.249717 old closure,
0.485137 Gaussian and 0.484999 orthogonal. These are arithmetic
means over the same fixed eleven tasks, not repeated-seed estimates.

## Design and comparison

User-confirmed scope: all11 original n2048 qualitative tasks except the
equal_semicircles negative-control geometry; no fresh/rotated confirmations.
The earliest two n512-only tasks have no n2048 baseline archive and are outside
this width-matched suite. Reuse all old baselines and dense references. The
later dense-reference pair supersedes earlier references on quadrant_pairs
and two_outliers_alternating; every method uses the same pair for its task.

New p1,p3,p5 have6,18,38 frozen vectors and8,72,336 middle coefficients.
Archived p1,p3,p5 have8,45,149 vectors and15,350,2688 coefficients. All models
also train6144 read-in/readout parameters. Thus new38 and archived45 have
6480 and6494 trainable parameters, respectively. They have the same width,
seed, initialized read-in/readout, canonical tanh network, loss, flow and
stopping rule; frozen bases and compressed middle initializations differ.
There is no retained dense middle residual, task-label-dependent dictionary,
new seed, basis tuning or baseline retraining.

The user's reporting correction selects the nearest AVAILABLE total-vector
count, separately for every family. It supersedes the first live updates'
equal-order framing. There is no21-vector old p2 archive at this width, so
the18/8 comparison retains a substantial size difference. All archived8/45/149
and new6/18/38 points remain in the figures and complete metric table.

Mean unhalved training MSE stopping threshold0.001, at each model's own first
detected crossing. Reported RMS compares the resulting function with the
dense network's learned function on8192 uniform circle angles. This measures
approximation of that learned dense function, not unseen-label generalization.
Training is full-batch coefficient gradient flow numerically integrated with
the unchanged simultaneous adaptive Heun method, not Adam or SGD.

## Nearest-size results

Entries below count lower RMS at BOTH selected numerical levels, divided by
the number of numerically valid comparisons for that pair. Invalid cells are
excluded only from the affected denominator and remain explicitly reported.
No supported comparison reverses between numerical levels.

| New / closest archived vectors | Old closure | Gaussian | Orthogonal |
|---|---:|---:|---:|
| 6 / 8 | 2/11 | 4/10 | 3/11 |
| 18 / 8 | 7/10 | 8/10 | 8/10 |
| 38 / 45 | 8/11 | 10/11 | 10/11 |

For the most comparable38/45 sizes, the old closure wins on equal_mixed_odd,
two_clusters_grouped and two_outliers_alternating. Both random baselines win
only on near_equal_grouped. Every value in this next table is validated.

| Task | New 38 | Old 45 | Gaussian 45 | Orthogonal 45 |
|---|---:|---:|---:|---:|
| quadrant_grouped | 0.030705 | 0.036727 | 0.044188 | 0.044713 |
| quadrant_alternating | 0.120676 | 1.288827 | 2.461882 | 2.481055 |
| quadrant_pairs | 0.104996 | 0.165388 | 0.550726 | 0.599156 |
| quadrant_center_edges | 0.127471 | 0.471448 | 0.512078 | 0.502740 |
| equal_mixed_odd | 0.090831 | 0.026183 | 0.152871 | 0.167104 |
| near_equal_grouped | 0.024656 | 0.025418 | 0.009445 | 0.009014 |
| two_clusters_grouped | 0.010020 | 0.008036 | 0.011018 | 0.011654 |
| two_clusters_split | 0.035046 | 0.073834 | 0.073872 | 0.077456 |
| three_clusters_mixed | 0.052237 | 0.068314 | 0.099164 | 0.097373 |
| one_outlier_grouped | 0.026002 | 0.032951 | 0.041993 | 0.041885 |
| two_outliers_alternating | 0.868287 | 0.549762 | 1.379267 | 1.302833 |

## Size trend and limitations

New6 to new38 improves RMS inall11 tasks at both numerical levels. The
successive increases are not monotone: among10 tasks where both endpoints
are valid,6 to18 improves9 and worsens1;18 to38 improves8 and worsens2.
The unresolved intermediate point is quadrant_alternating/newp3. A richer
dictionary is useful here, but finite results do not establish an asymptotic
approximation rate, arbitrary-accuracy convergence or universal superiority.

## Numerical checks and retained unresolved cells

All66 base trajectories plus the one permitted numerical extra fitted. New
base tolerances were6.25e-5/1.5625e-5 with atol=rtol/100. The sole extra used
rtol3.90625e-6 on quadrant_alternating/newp3 after its fitted base pair had
sampled maximum discrepancy0.02375835597. Its latest pair still differs by
0.01499866628, above0.01. Latest-pair RMS0.155262689 is retained as unresolved;
no further extra is allowed by the frozen protocol. Its favorable apparent
ranking is not counted as a validated win.

Inherited unresolved controls remain quadrant_alternating/Gaussianp1
(0.01012700963) and orthogonalp5(0.04146386791). These do not affect the
38-versus45 comparisons. Final coverage129/132 model rows valid,32/33 new
dictionary rows valid, all11 dense references valid.

Independent replay covers287 distinct trajectories and2672 saved snapshots,
with separately associated forward arithmetic, training losses, initial
states/projections, basis reconstruction, case/seed/grid and executed-source
checks. Final scalar agreement and detailed maxima are in
SUITE_INDEPENDENT_CHECK.md. All failures/earlier attempts remain preserved.
Four archived wrapper hashes were authenticated against exact files recovered
from their recorded commits; see SUITE_SOURCE_RECONCILIATION.md.

## Artifacts and resources

Authoritative metrics/validation/curves: generated suite_analysis_final01.
Figures: generated suite_plots02. Nearest-size counts, means, size trends,
explicit task lists and every compute charge: generated suite_summary01.
Exact schedule/configuration provenance: SUITE_RUN_RECORD.md and all raw
suite_primary01/suite_refined01/suite_extra01 configurations. Frozen inputs:
SUITE_PROTOCOL.md,SUITE_MANIFEST.json; report mapping amendment:
SUITE_REPORTING_AMENDMENT.md.

Both RTX3090 GPUs ran concurrent training workers and independent checks.
Charged new GPU-worker time850.653435293585s, remaining inherited allowance
1177.529446322471s, no outstanding reservations or further training branch.
The shared checkout, tracked files/index and previous runs were preserved.
These are internally checked study results; no established-source promotion.
