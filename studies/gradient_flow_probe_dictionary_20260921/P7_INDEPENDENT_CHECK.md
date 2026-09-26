# Independent saved-state audit for p7

## Frozen audit design

This checker is prepared before inspecting the main p7 analyzer or its
results. It imports no main analyzer, trajectory producer, or producer
prediction routine. It may reuse the already independent
`suite_independent_check.py` memory-mapped archive reader, direct associated
forward arithmetic, source/configuration checks, and saved-state checks.
Only the new p7 `(26,46)` dimensions and raw-feature identity are added.

Every available p7 attempt is replayed, including attempts excluded by the
latest-two numerical selection. For every saved snapshot, independently
evaluate all 2048 saved circle nodes and the mean unhalved training MSE;
evaluate all 8192 endpoint nodes from the final state. Use the direct map
`tanh(((tanh(u w.T) B1)/n) M.T B2.T) c/n`, `n=2048`. Check the accepted
loss trace's first saved threshold crossing, initial read-in/readout, raw
basis dimensions/metadata, ridge normalization, projected initial M0, all
finite values, source/configuration bindings, cases, grids and step settings.
Prediction/loss tolerance is `1e-10`, ridge condition at most `1e10`, and
triangular relative residual at most `1e-8`.

The p7 raw builder is used only to identify the frozen initialization
fields. The checker solves ridge normalization independently and verifies
both inherited p5 raw prefixes. The producer build/engine is not called.

The task's full references and selected old45, Gaussian45, orthogonal45,
and new38 endpoints already have independent state replay records in
`suite_independent01`. Reuse those reconstructed endpoints after binding
the prior checker hash, NPZ file identity and member identities, current
configuration/source hashes, saved summary, and endpoint consistency. Do
not repeat dense historical trajectories or change their selected paths.
Recompute all comparison metrics from endpoint arrays; do not reuse the
historical metric values as the current computation.

For every method, independently recompute RMS, L1, MSE and sampled maximum
against the same selected dense reference pair, plus 8192/4096 changes.
Require model and dense-reference selected-pair endpoint maximum at most
`.01`. Select the latest two p7 attempts. A third p7 attempt is permitted
only if both base attempts fitted and their discrepancy exceeded `.01`;
retain every attempted level. Compare new72 against new38 and separately
against all three archived45 families. A winner requires a valid pair and
the same strict RMS ordering at both selected numerical levels. Preserve
all invalid-cell and unresolved-direction reasons.

GPU execution requires the root's explicit device/reservation assignment.
Each invocation is capped at at most 100 worker seconds, with completed
trajectory and case results durable before proceeding. CPU preparation and
final scalar comparisons are separate. The main p7 outputs may be read
only after independent rows exist, to compare numerical results and
selected paths. This is an internal numerical audit, not an additional
training experiment or a promotion review.

## Completed result: PASS

All 22 p7 base trajectories fitted and passed independent reconstruction.
The checker replayed all 200 saved snapshots, all corresponding saved
training losses, and all 22 final 8192-node endpoints. Initial read-in,
readout, and projected middle matrices agree exactly. Both inherited p5
raw prefixes agree bitwise. There were no state, basis, source/configuration,
case/grid, threshold-trace or metadata failures.

| Check | Largest observed discrepancy or value | Gate |
|---|---:|---:|
| Saved circle predictions | 4.218847493575595e-15 | 1e-10 |
| Saved training loss | 3.6637359812630166e-15 | 1e-10 |
| Final endpoint prediction | 4.440892098500626e-15 | 1e-10 |
| Independently normalized basis entry | 2.466749027263404e-12 | 1e-10 |
| Ridge condition | 5.216299224213303e9 | 1e10 |
| Triangular relative residual | 1.6179618927220254e-14 | 1e-8 |
| p7 selected-pair endpoint maximum | 0.0016901961867825666 | 0.01 |
| Dense-reference selected-pair endpoint maximum | 0.008744696704584434 | 0.01 |

The ridge condition is relatively large, but remains below the fixed gate;
its independent basis and forward replay checks also pass. No columns,
raw scales or regularization parameters were changed in response.

CPU preparation independently rebound all 110 historical trajectories:
22 full references, 22 new38, and 66 archived45 trajectories across the
three separate families. Each reused endpoint has its prior independent
record and current endpoint-file hash recorded, with unchanged raw NPZ
file/member identity and authenticated configuration/source. Their saved
snapshots had already been replayed by the previous independent audit;
this phase does not claim to replay those historical snapshots again.

All eleven p7 selected pairs pass the `.01` gate. No p7 numerical extra is
eligible. All 44 p7-versus-new38/archived45 comparisons are valid, and their
RMS ordering agrees at both levels. The three previously unresolved cells
elsewhere in the full suite are unaffected; none belongs to this comparison
subset, and no historical refinement branch was reopened.

The main analysis was read only after independent per-case metrics were
saved. All 55 relevant metric rows (11 p7 plus 44 comparison rows) agree
in selected paths, validity and scalar metrics. The maximum metric
discrepancy is `2.6645352591003757e-15`. All 44 displayed pair comparisons
also agree in count mapping and both winners; their largest ratio
discrepancy is `1.7763568394002505e-15`.

## Independently recomputed comparison

New p7 has 72 vectors. Its nearest available archived size is 45 vectors,
and the previous new dictionary has 38. All denominators below are the
complete frozen eleven-case set; there are no invalid or excluded cases in
these four pairings.

| Comparison | p7 RMS wins at both levels |
|---|---:|
| New38 | 8/11 |
| Old closure45 | 8/11 |
| Gaussian45 | 10/11 |
| Orthogonal45 | 10/11 |

P7 worsens relative to new38 on `quadrant_alternating`,
`quadrant_center_edges`, and `two_clusters_split`. Its mean per-case RMS
also worsens despite improving on eight cases:

| Method | Earlier selected level mean RMS | Refined selected level mean RMS |
|---|---:|---:|
| New72 | 0.14527862136085798 | 0.1453305677935917 |
| New38 | 0.13530601198316286 | 0.13553891832208068 |
| Old closure45 | 0.24978985289507286 | 0.24971714410930745 |
| Gaussian45 | 0.48478276656720903 | 0.48513655110945453 |
| Orthogonal45 | 0.4845401555300949 | 0.48499850181573545 |

The full common case intersection is `quadrant_grouped`,
`quadrant_alternating`, `quadrant_pairs`, `quadrant_center_edges`,
`equal_mixed_odd`, `near_equal_grouped`, `two_clusters_grouped`,
`two_clusters_split`, `three_clusters_mixed`, `one_outlier_grouped`, and
`two_outliers_alternating`. These are finite single-initialization
comparisons, not hierarchy monotonicity or population convergence results.

Across all 55 metric rows and both numerical levels, the largest
8192-versus-4096 changes are `1.1102230246251565e-16` for RMS,
`2.056637682379403e-6` for L1, and `0.0001421082129997031` for sampled
maximum. The sampled maximum does not certify the continuous-circle
supremum. Threshold verification concerns the first saved accepted loss
crossing and does not prove a continuous-flow crossing time between steps.

## Source, timing and evidence

The frozen checker `p7_independent_check.py` has SHA256
`b019dbced729d62e57bc85ab7a7f860151bb597318687c480d622cb99863db88`.
The reused independent suite checker has SHA256
`4f4c18ca42c13bead253edec758e0ddac5a1f86a12859f4637a18ce973ee4b54`.
Neither checker imports a main analyzer or trajectory producer.

The root explicitly assigned GPU1 and a reservation of at most 100 worker
seconds. A default-sandbox attempt failed before CUDA initialization,
recording `0.12092182785272598` seconds and zero completed trajectories.
The same unchanged checker then ran with GPU access, a 95-second internal
cap, and completed all eleven cases in `3.3198407888412476` recorded worker
seconds. The conservative total including the failed startup is
`3.4407626166939735` seconds. No additional GPU invocation was needed;
preparation and final scalar checks used CPU only.

Machine evidence is in
`data/generated/gradient_flow_probe_dictionary_20260921/p7_independent01/`:

- `preparation.json` and `historical_bindings/`: 110 authenticated historical
  endpoint reuses, including old checker/configuration/source identities.
- `replays/`: 22 independent p7 state replay reports and reconstructed
  endpoint arrays; each report binds the checker and raw NPZ identities.
- `cases/`: eleven independently computed five-method metric tables and
  four pair comparisons per case.
- `audit_summary.json`: all maxima, explicit valid/win/loss case lists and
  arithmetic means stated above.
- `comparison.json`: agreement of all 55 metric rows with the main p7 and
  historical analyses. The main p7 metric-file hash is
  `c4253f5a817fa017ebfbf2501a01755d22d0c1016601f735cdbfae9da61634e3`.
- `final_scalar_check.py` and `final_scalar_check.json`: separate scalar
  comparison of all 44 displayed pair comparisons, including exact count
  mappings and both numerical-level winners.
- `completion_001.json` and `completion_002.json`: failed CUDA startup and
  completed GPU1 audit, with commands, source hash, reservations and timings.

All authorized audit checks are complete. No training, additional seed,
alternative dictionary, or numerical refinement was performed by this checker.
