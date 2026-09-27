# J2 coverage of all circle toy tasks

2026-09-27. Read-only inventory and independent audit for the same study. This checker ran no compilation or training; selected campaign outcomes are incorporated below.

The two task catalogs contain 17 distinct tasks: 12 circle tasks plus 8 geometry tasks, with three identical overlaps. Three tasks already have fitted J2 results at MSE 0.001; fourteen remain.

| Task | Training inputs | J2 at MSE 0.001 |
| --- | ---: | --- |
| `pair_cos1` | 2 | Missing |
| `pair_cos3` | 2 | Partial; not fitted |
| `near_pair_sin9` | 2 | Partial; not fitted |
| `triple_cos3` | 3 | Missing |
| `triple_mixed` | 3 | Missing |
| `cluster_triple_cos9` | 3 | Partial; not fitted |
| `broad_ridge6` | 6 | Compile/reporting failure; no endpoint |
| `sharp_ridge8` | 8 | Missing |
| `alternating3` | 6 | Compile/reporting failure; no endpoint |
| `alternating5` | 10 | Missing |
| `alternating9` | 18 | Missing |
| `multiscale12` | 12 | Missing |
| `pair_orthogonal_cos1` | 2 | Already fitted |
| `cluster_triple_cos1` | 3 | Already fitted |
| `triple_wide_mixed` | 3 | Already fitted |
| `quartet_broad` | 4 | Missing |
| `quartet_mixed` | 4 | Partial; not fitted |

The duplicate catalog entries are `pair_cos3`, `near_pair_sin9`, and `triple_cos3`; their angles, teacher definitions, and labels agree exactly.

## Feasibility evidence

| Measured case | Template contractions | Retained terms | Full scalar state | Initial integration |
| --- | ---: | ---: | ---: | ---: |
| `cluster_triple_cos1`, J2 | 17,324 | 82,179 | 513,513 | 82.14 s |
| `pair_orthogonal_cos1`, J2 | 5,066 | 21,180 | 188,367 | 23.73 s |
| `triple_wide_mixed`, J2 | 17,324 | 82,179 | 513,513 | 82.61 s |
| `quartet_broad`, J1 | 6,030 | 62,416 | 99,965 | 15.43 s |
| `quartet_mixed`, J1 | 6,030 | 62,416 | 99,965 | 15.35 s |

At the initial inventory, no J2 counts had been measured for m = 4, 6, 8, 10, 12, or 18. The final screen below adds the m = 4 count and two m = 6 failure records. The m = 3 initialization already required about 82 seconds under the existing initializer. Both measured J1 quartet runs reached their 45-second training budget without fitting. These are capacity warnings, not results about higher-input J2 accuracy.

For fixed memory order, the source loops give conservative upper bounds of O(m^5) selected-tree proposals at J2 and O(m^7) raw derivative proposals when building all selected rows. They do not supply useful numerical counts or predict actual runtime. Every new size needs a bounded feasibility result.

The existing internal compilation timer excludes construction of the local generator, and not every essential-set loop checks the timer. A hard outer wall limit must include constructor and selection work before high-input cases are attempted.

## Reference coordination

The reference agent owns the exact checkpoint inventory. Its current count over all 34 controls is seven reusable fitted MSE 0.001 checkpoints, fifteen MSE 0.01 checkpoints suitable for continuation, and twelve fresh references required. The six tasks with no matching n = 1024, seed = 1 Gaussian or k = 4/P = 1 block checkpoint are `broad_ridge6`, `sharp_ridge8`, `alternating3`, `alternating5`, `alternating9`, and `multiscale12`. Old controls with a different width, seed, block size, or memory order are not interchangeable.

Machine-readable task definitions, existing J2 record hashes, and measured feasibility provenance are in `data/generated/structured_full_rank_scalar_20260926/all_tasks_j2_20260927/coverage.json`.

The verified per-reference inventory is saved in `data/generated/structured_full_rank_scalar_20260926/all_tasks_j2_20260927/references/inventory.json`; its SHA256 is pinned in the coverage JSON. A metadata scan of 17 same-study scalar result records found exactly the three fitted J2/MSE0.001 results listed above.

## Revised execution scope after user efficiency steering

The full inventory above remains seventeen tasks. The current authorized campaign selects only six new tasks: `pair_cos3`, `near_pair_sin9`, `cluster_triple_cos9`, `quartet_mixed`, `broad_ridge6`, `alternating3`. The three previously completed J2/MSE0.001 tasks are carried forward.

Eight tasks are explicitly not selected: `pair_cos1`, `triple_cos3`, `triple_mixed`, `sharp_ridge8`, `alternating5`, `alternating9`, `multiscale12`, `quartet_broad`. They remain untested at the requested setting; their omission is a scope choice rather than a fit or resource result.

Attempt each selected task within the declared caps: 60 seconds for compilation including constructor work, 90 seconds for initial contractions, 45 seconds for training, two million dynamic scalar states, and one GiB estimated workspace. Preserve resource-limited and partial outcomes. The earlier 34-control inventory describes full-catalog availability, not authorization to execute all controls after this scope reduction.


## Completed selected screen

The independent audit passes for all six new attempt records, eighteen fitted
reference records, and the three carried-forward fitted scalar cases. None of
the six new scalar attempts fitted at core MSE 0.001. Four have valid finite
partial checkpoints from the 45-second training limit:

| Task | Core MSE | Passive training MSE | Maximum alias gap | Partial RMS vs matched block |
| --- | ---: | ---: | ---: | ---: |
| `pair_cos3` | 0.0135618 | 0.00262131 | 0.0697406 | 0.2105 |
| `near_pair_sin9` | 1.10781 | 0.410649 | 0.52853 | 0.368181 |
| `cluster_triple_cos9` | 1.03854 | 0.983908 | 0.0583355 | 0.875043 |
| `quartet_mixed` | 0.0766024 | 0.0366701 | 0.237062 | 0.174212 |

All four same-input alias gaps exceed the predeclared 0.05 flag. Their circle
errors describe partial endpoints and do not establish fitted high-error cases.
The quartet completed compilation with 45,662 template contractions and
235,776 retained terms; its 68-query panel uses 1,113,509 evolving scalars and
436.67 MiB estimated workspace, within the declared limits.

Both six-input attempts (`broad_ridge6`, `alternating3`) exited during bounded
selection before producing a valid template. A caught compilation limit was
followed by a reporting bug accessing the still-missing `essential_trees`
attribute. The exact triggering limit and partial counts were not saved.
Preserved logs support a compile/reporting failure, not an accuracy claim.
Neither attempt trained; no retry or smaller substitute was run.

For the sharp cluster, block–Gaussian control RMS changes by 0.001113 between
64 and 256 angles although its 64/32 difference is smaller. This is a control
grid diagnostic; no additional scalar query panel was evaluated. The eight
unselected tasks remain untested. Full details and hashes are in
`checks/independent_selected_audit.json` under the campaign data directory.
