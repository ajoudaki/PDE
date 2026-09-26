# Independent saved-state audit: trainable derivative-p3 vectors

2026-09-22. **Numerical/provenance checks PASS. The preregistered improvement
criterion passes against frozen p3 and fails against frozen p7.** At the finer
tolerance, unfreezing p3 changes circle RMS from `1.1001187613717833` to
`0.896425006407051` (18.52% lower). Frozen p7 remains better at
`0.7564240400073452`; trainable p3 is 18.51% higher. Both numerical levels agree
on each direction with margins exceeding the fixed `.01` RMS threshold.

## Scope and independence

The supervisor assigned a CPU-only empirical audit of the three named new runs,
using the already authorized exact derivative-dictionary benchmark archives,
the new frozen protocol, and producer sources. The inherited input scope is
documented in `BENCHMARK_INPUT_CHECK.md`. No unrelated study was accessed.

The checker `independent_trainable_analysis.py` imports NumPy and Python standard
libraries only. It imports neither the training model/runner nor the root
analysis, and performs no training, GPU action, or Git action. Its forward
reconstruction is direct matrix arithmetic from every saved `w,c,M,b1,b2`
snapshot. The root analyzer was not read or used. Current producer code and
the frozen protocol were inspected to identify file semantics and declared
gates. This is an independent empirical replay, not a promotion review or a
fresh proof of the factor-gradient formulas.

Raw machine-readable evidence:
`data/generated/adaptive_response_compression_20260922/independent_trainable01/checks.json`.
The run completed in 7.454 CPU wall seconds with 223 passing checks.

Reproduction command from the repository root:

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B studies/adaptive_response_compression_20260922/independent_trainable_analysis.py --out data/generated/adaptive_response_compression_20260922/independent_trainable02
```

Use a fresh output directory; existing evidence is never overwritten.

## Matched comparison

All scores in this report use the identical **finer dense endpoint** at
`data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_refined01/two_outliers_alternating_full/arrays.npz`.
The exact 8192-point grid and eight training inputs/labels are equal across
archives. Each model uses its own first detected unhalved training-MSE `.001`
crossing. These are learned-function discrepancies, not ground-truth test
errors or common-flow-time comparisons.

| Model | Tolerance | Circle RMS | Sampled maximum error | Own fitted flow time |
|---|---:|---:|---:|---:|
| Trainable p3 | `6.25e-5` | 0.8961921387733306 | 1.9088918224339744 | 2576.970745289502 |
| Trainable p3 | `1.5625e-5` | 0.8964250064070510 | 1.9089042993406466 | 2581.8820402527654 |
| Frozen p3 reproduction | `1.5625e-5` | 1.1001187613717724 | 1.9950108554213910 | 241.9852741495650 |
| Archived frozen p3 | `1.5625e-5` | 1.1001187613717833 | 1.9950108554214510 | 241.98527414956894 |
| Archived frozen p7 | `1.5625e-5` | 0.7564240400073452 | 1.1921374185095880 | 220.6768397610208 |

The trainable finer L1 discrepancy is `0.7262426780688291`. Its flow fitting
time is 10.67 times frozen p3's, under the stated factor mobilities. This is a
flow-time comparison, not a wall-time or hardware-efficiency claim.

The new primary/finer RMS reductions against frozen p3 are respectively
`0.20392662259845273` and `0.2036937549647323`. Against frozen p7, the new RMS
increases are `0.1397680987659854` and `0.14000096639970583`. Thus the full
proposal to improve over both frozen comparators is not supported on this task,
despite the clear improvement over its own frozen-p3 initialization.

## Replay and validity evidence

- Reconstructed all **38 saved circle snapshots** and all three 8192-point
  endpoints directly from the saved five state arrays. Maximum prediction
  discrepancy: `1.7263968032921184e-14`, below `1e-10`.
- Recomputed the unhalved training MSE at every saved state and matched it to
  the accepted loss-history entry at that exact snapshot time. Maximum loss
  discrepancy: `1.6653345369377348e-15`, below `1e-10`.
- Verified every initialized `w,c,M,b1,b2` array bit for bit against the exact
  archived finer frozen-p3 arrays, including independent byte hashes. Factor
  tables now have a snapshot axis; their first slice matches the original
  constant table. The frozen control retains identical factor tables at every
  saved time.
- Verified expected state shapes, finite arrays, exact case inputs/labels,
  grid counts and grids, protocol settings, mobilities, accepted time/step
  consistency, step/error bounds, fitted status, and loss acceptance rules.
  All accepted loss histories have every preterminal loss above `.001` and the
  terminal loss at or below `.001`; endpoint time/loss match their summaries.
- Recomputed new-run RMS, L1, sampled maximum, and 4096-node metrics. New-run
  summaries agree within `1e-10`; the independent RMS 8192/4096 difference is
  zero at printed float64 precision for all three runs.
- Independent trainable primary/finer endpoint sampled-maximum difference is
  `0.0030338941672472496`, below `.01`. **No extra numerical run is eligible.**
- Frozen reproduction differs from the archived p3 endpoint by at most
  `9.85878045867139e-14`; fitted flow-time difference is
  `3.950617610826157e-12`. Both are far below the frozen-replay `.001` limits.
- Recomputed final factor motions, column RMS norms, and Gram eigenvalues and
  checked every summary value within `1e-10`. Finer RMS factor motion is
  `0.8682894441318729` for `b1` and `0.7707617381220189` for `b2`, confirming
  substantial movement rather than an accidentally frozen trainable run.

Source hashes recorded in each config agree with the current complete
`trainable_dictionary.py`, `run_trainable_p3.py`, and
`TRAINABLE_P3_PROTOCOL.md`. The source set is checked explicitly. Input archive
hashes are pinned to the prior benchmark audit; all three configs name those
exact inputs and hashes. Each raw `arrays.npz` hash agrees with its summary.
Fresh hashes of configurations, summaries, raw outputs, baseline archives,
and checker source are retained in `checks.json`.

## Size and claim limits

All new states contain `w:2048x2`, `c:2048`, `M:12x6`, `b1:2048x6`, and
`b2:2048x12`. These give 43,080 working-model scalars. Training both factor
tables uses all 43,080; freezing them leaves 6,216 trained scalars. Thus
trainable p3 uses 36,864 additional trained scalars, and the improvement over
frozen p3 is not parameter matched. P7 has 7,340 trained scalars. The p3
factorized middle rank remains at most six.

This is one initialized task and one declared factor-gradient metric. It does
not establish monotonic hierarchy convergence, dense-coordinate gradient-flow
equivalence, or accuracy of a streaming response-cache algorithm. The audit
replays all saved states, not every unsaved accepted state or rejected trial;
the accepted history checks do not by themselves independently reconstruct
the complete integrator path. The dense and historical p7 endpoints are the
fixed, previously audited raw references; this checker hashes them and
recomputes comparative metrics, without rerunning their training.
