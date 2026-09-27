# Increasing scalar output-dependency depth

2026-09-27. At the MSE0.01 stopping threshold, increasing output-dependency
depth from J=1 to J=2 reduced circle error substantially on the orthogonal
pair, slightly increased it on the smooth cluster, and barely changed it
on the spread-out mixed triple. Thus this refinement gives mixed benefits
at approximately8–10 times the full query-panel state size.

## Meaning of this scalarization order

Keep the essential output, feedback and hidden-Gram moments and their
immediate derivative constituents. J=1 additionally follows one generation
of moment dependencies from each output; J=2 follows the next generation.
The variables are evolving aggregate contractions, not sampled neurons or
initialization dictionaries. Block size k4 and response-history P1 do not
change. Unretained moment children are still set to zero.

The retained sets are nested. J=2 preserves the complete immediate rows of
the first output-derivative children. This does not establish exact second
time derivatives of outputs: derivatives of state-dependent coefficients
involve additional feedback moments that are still truncated. A saved-cache
audit found explicit missing derivative children of dot-s constituents.
Consequently neither monotone error reduction nor convergence in this
particular selective parameter has been proved. The full-degree hierarchy's
theorem cannot silently be transferred to this selective family.

## Matched results

Both scalar orders use tanh, k4/P1, n1024 initial contractions, seed1, the
same actual block initialization, and a shared autonomous training core with
64 passive circle queries and passive copies of every training input. All
new runs and all saved controls reached core training MSE0.01. Each function
comparison uses its model's own first-threshold endpoint; it is not a
same-physical-time trajectory bound.

Raw circle RMS means the RMS of the difference between predicted functions,
without division by reference signal amplitude or comparison to teacher labels.

| Task | Scalar–block J1 | Scalar–block J2 | Change | Scalar–Gaussian J1 | Scalar–Gaussian J2 |
|---|---:|---:|---:|---:|---:|
| Orthogonal cosine pair | 0.057236 | 0.042814 | 25.20% lower | 0.061283 | 0.047334 |
| Smooth clustered triple | 0.073745 | 0.076171 | 3.29% higher | 0.076832 | 0.079223 |
| Spread-out mixed triple | 0.044282 | 0.044274 | 0.017% lower | 0.042913 | 0.042889 |

Only the pair exceeds the predeclared5% improvement screen. The cluster's
increase is below the5% adverse screen. No uniform improvement trend is
established, and one seed/two orders cannot establish a convergence rate.

| Samples | Training scalars including clock, J1 to J2 | Full probe-panel scalars, J1 to J2 |
|---|---:|---:|
| 2 | 527 to2247 | 23627 to188367 |
| 3 | 1824 to9807 | 53012 to513513 |

These state sizes are independent of original width and elapsed time.
The panel cost is explicit: this does not furnish arbitrary post-training
input queries without having evolved their passive moments.

## Consistency, numerical checks and costs

Maximum discrepancies between core and passive predictions at identical
training inputs are J1→J2: pair0.01096→0.02717, cluster0.03671→0.03991,
mixed0.01262→0.01128. The passive predictor's training RMS at J2 is
0.08084,0.13694 and0.10707 (see raw records for exact values).
Core fit quality and passive fit quality remain distinct quantities.

Independent saved-cache checks verify set nesting and protected exact rows.
Every common initial scalar, across the shared core, all circle queries,
training aliases and clock, matches bit for bit between orders. Independent
raw-state decoding, source/checkpoint hashes, circle indices and RMS
recomputation pass for all three. The scalar-versus-block64/32-grid RMS
changes are below3.9e-7. These checks do not supply a continuum quadrature
bound or a repeated-seed experiment. In the cluster, one normalized moment
slightly exceeds the unit box and activates the existing stabilization at
both orders; the other new runs do not activate clipping.

New J2 training costs were2.43,23.89 and9.08 seconds; initialization costs
were23.73,82.14 and82.61 seconds. Total new training35.39seconds, compilation
8.39seconds, initialization188.47seconds. No existing run was overwritten
or retrained. Setup is a material cost even though training remains quick.

## Evidence and reproduction

- [Protocol](SELECTIVE_ORDER_PROTOCOL.md)
- [Runner](run_selective_order.py)
- [Raw-metric analysis](analyze_selective_order.py)
- [Independent checker](check_selective_order.py)

Generated records:
`data/generated/structured_full_rank_scalar_20260926/selective_order_20260927/`.
The `scalar/` folder retains exact commands, configuration/source hashes,
cached templates and complete endpoints; `analysis/summary.csv` and JSON
derive the tables; `checks/independent_order_audit.json` and
`checks/common_initialization_audit.json` retain the audit results.

Run the analysis without training:

```bash
OPENBLAS_NUM_THREADS=1 python studies/structured_full_rank_scalar_20260926/analyze_selective_order.py
```

This campaign is complete. The user's subsequent tighter-stop request is
a separate continuation with old endpoints preserved and explicit resume
provenance; its results must not replace the MSE0.01 comparison silently.
