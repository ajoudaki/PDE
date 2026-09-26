# Independent check of the eleven-case derivative dictionary suite

Status: independent reconstruction and comparison checks passed. Three
selected numerical cells remain invalid and are excluded where relevant.
This is an internal numerical check, not a promotion review or a claim about
other widths, seeds or tasks.

The frozen scope is all eleven requested width-2048 original circle cases,
new p1/p3/p5 and the manifest-selected old, Gaussian and orthogonal p1/p3/p5
baselines. The excluded negative control and fresh or rotated configurations
are not numerical inputs. The checker did not read the main analyzer or its
findings before constructing its reconstruction and comparison routines.

`suite_independent_check.py` implements its own forward map directly from
the saved state arrays. For input row u it computes h1=tanh(u w^T). The dense
model uses h2=tanh(h1 M^T); a dictionary model uses
h2=tanh(((h1 B1)/2048) M^T B2^T). Both outputs are h2 c/2048. It imports no
producer engine prediction, trajectory routine or main analysis functions.
The frozen raw-feature builders identify the new initialized feature tables;
the checker independently solves their ridge normalization, recomputes
projected M0 and compares all saved new bases. Previously checked high-order
symbolic coefficient identities are not rederived here.

Each raw trajectory is checked for exact case/grid inputs, uniform population
weights, dimensions, finite states, common initial w/c, dense initial M or
projected M0, retained random readout, raw dictionary metadata, the numerical
configuration and recorded executed dependency hashes. Every saved snapshot
is reconstructed on all 2048 saved circle nodes, and its mean unhalved
training loss is matched to the accepted-step trace. The final state is also
reconstructed on all 8192 endpoint nodes. The recorded accepted losses must
first cross 0.001 at the fitted final entry. This checks the saved first
crossing and the frozen producer's crossing procedure; it is not a proof of
the exact continuous flow's first-crossing time between numerical steps.

Independent CUDA float64 reductions compute RMS, L1, MSE and sampled maximum
against the same selected dense reference at each numerical level. They also
compute the nested 4096-node metrics and selected-pair maximum discrepancies.
Both model and dense reference require discrepancy at most 0.01. Any extra
new numerical attempt must satisfy the frozen two-fitted-attempts and
discrepancy-greater-than-0.01 gate. All attempts and reasons are retained.
The two inherited invalid cells remain invalid even if raw replay succeeds.

The source check authenticates the current executed dependency graph except
for four dense discovery references whose recorded wrapper predates a later
width-only extension. For those four, it authenticates the recovered exact
source bytes against both the configuration's recorded HEAD and original
digest. The current hash mismatch is retained in each provenance record.
The complete recovered wrapper and current diff were inspected independently:
the differences add a width4096 stage, its guards and a protocol-path metadata
argument; the original discovery/stage-A trajectory path is unchanged. No
source mismatch is waived on the basis of a compatibility assertion.

GPU invocations reserve at most 100 worker seconds, normally with an internal
95-second stop. Every completed trajectory has a durable replay report and
independently reconstructed endpoint array; every completed case has a durable
metric report. Dense histories are memory mapped from uncompressed NPZ members.
The replay tolerance is 1e-10. A final scalar comparison against the separately
computed main analysis is performed only after the independent case results
exist.

The completed check covers 287 trajectories: 220 archived selected baseline
and dense-reference trajectories, 66 new base trajectories and the one
permitted new refinement. It reconstructs all 2672 saved snapshots, all 287
8192-node endpoints and all associated saved-snapshot training losses.
There are no raw replay, initialization, source/configuration or metadata
errors. The maximum snapshot and endpoint prediction discrepancy is
1.865174681370263e-14; the maximum training-loss discrepancy is
1.8318679906315083e-15. All projected initial middle matrices agree exactly
in this arithmetic. The largest independently reconstructed new-basis entry
discrepancy is 1.865174681370263e-14. The largest new regularized condition
number is 32789.177903829404, and the largest triangular relative residual is
7.805448843203957e-16, both comfortably within the frozen gates.

All 132 final per-cell metric rows, their selected paths and validity flags
agree with the separate main analysis. The maximum scalar metric difference
is 4.884981308350689e-15. All 99 closest-available-count comparisons agree in
validity, count mapping, winner at each level and agreement of the two level
directions. The maximum absolute 8192-versus-4096 change over reported cell
metrics and levels is 4.440892098500626e-16 for RMS,
3.4439286817899983e-06 for L1 and 0.00016093255818017127 for sampled maximum.
The sampled maximum is not a certified continuous-circle supremum.

The final invalid cells, all on `quadrant_alternating`, are:

| Cell | Selected-pair endpoint maximum | Reason |
|---|---:|---|
| new p3, 18 vectors | 0.014998666278685846 | Still above 0.01 after the permitted extra |
| Gaussian p1, 8 vectors | 0.010127009631220929 | Inherited unresolved numerical cell |
| orthogonal p5, 149 vectors | 0.04146386790700185 | Inherited unresolved numerical cell |

The new p3 extra satisfies the frozen gate: both original attempts fitted and
their endpoint maximum difference exceeded 0.01. Its final comparison uses
`suite_refined01` and `suite_extra01`, while retaining the first attempt and
the original invalid comparison in `base_cases` and `base_comparison.json`.
No further training or favorable-level fallback was used. All other 129
requested method/case cells are valid under the stated gates.

The nearest available total dictionary counts are 6 versus 8, 18 versus 8,
and 38 versus 45. No 21-vector archived comparison exists. The following
counts are new-model RMS wins at both selected numerical levels; each
denominator is the valid case intersection for that pair:

| New versus archived vectors | Old closure | Gaussian | Orthogonal |
|---|---:|---:|---:|
| 6 versus 8 | 2/11 | 4/10 | 3/11 |
| 18 versus 8 | 7/10 | 8/10 | 8/10 |
| 38 versus 45 | 8/11 | 10/11 | 10/11 |

Every ten-case intersection in this table excludes only
`quadrant_alternating`; every eleven-case intersection is the entire frozen
manifest. The common valid intersection across all requested methods is
explicitly `quadrant_grouped`, `quadrant_pairs`, `quadrant_center_edges`,
`equal_mixed_odd`, `near_equal_grouped`, `two_clusters_grouped`,
`two_clusters_split`, `three_clusters_mixed`, `one_outlier_grouped`, and
`two_outliers_alternating`. No reported valid pair has a reversed RMS winner
between the two selected levels.

Within the new family, 18 vectors improve on 6 on 9/10 valid cases, and 38
improve on 18 on 8/10. The 38-vector model improves on the 6-vector model on
all 11 cases at both levels. These are instance comparisons, not monotone
hierarchy or asymptotic convergence results.

For the 38-versus-45 comparison, all eleven cases are valid for every family.
Independently checked arithmetic means of per-case RMS discrepancies are:

| Method | Earlier selected numerical level | Refined selected numerical level |
|---|---:|---:|
| new, 38 vectors | 0.1353060119831629 | 0.13553891832208065 |
| old closure, 45 vectors | 0.24978985289507286 | 0.24971714410930745 |
| Gaussian, 45 vectors | 0.48478276656720903 | 0.48513655110945453 |
| orthogonal, 45 vectors | 0.4845401555300949 | 0.4849985018157355 |

The three GPU audit invocations consumed 10.695641931146383,
24.874052811414003 and 0.7606001682579517 recorded worker seconds, totaling
36.33029491081834. Each used an internal 95-second cap within its separate
100-second reservation. The frozen checker SHA256 is
`4f4c18ca42c13bead253edec758e0ddac5a1f86a12859f4637a18ce973ee4b54`.

Machine evidence is in
`data/generated/gradient_flow_probe_dictionary_20260921/suite_independent01/`:
`replays/` binds reconstructed endpoints to raw NPZ member identities and
source/configuration digests; `cases/` holds the final independent metrics;
`comparison.json` records the final 132-row agreement;
`closest_count_check.json` lists all per-pair valid cases, wins and losses;
`final_scalar_check.json` checks all 99 displayed comparisons and the means;
and `completion_001.json` through `completion_003.json` record commands and
timings. The main final metric file authenticated by this comparison has
SHA256 `b16f060adb1dc212c9cc4eddc5ffc4e75035a60d34820a221565aebe11f5dd67`.
