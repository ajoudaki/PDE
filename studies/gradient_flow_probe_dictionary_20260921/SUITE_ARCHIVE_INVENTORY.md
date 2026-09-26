# Earlier circle-suite archive inventory

Scoped read-only inventory, 2026-09-21. Scientific inputs were restricted to
`studies/random_dictionary_learned_circle_20260920`, its generated namespace,
and this study's P45 protocol/results. No baseline was rerun, no GPU work was
performed, and no other study was inspected. This is an inventory, not a new
scientific verdict or independent numerical replay.

The machine-readable companion is
`data/generated/gradient_flow_probe_dictionary_20260921/suite_inventory01/inventory.json`.
It preserves the twelve original case definitions, 132 current old-baseline
rows (108 p1/3/5 rows plus 24 higher-order discovery rows), every current
dense-reference selection, the original selected-level inventory, coverage
at other widths, and hashes of consumed JSON. All 576 selected raw
`summary.json`/`arrays.npz` files referenced by those rows exist. File existence
is not a fresh checksum or predictor-replay audit.

The user subsequently confirmed **new p1,3,5 on eleven original tasks,
excluding `equal_semicircles` as the previous negative control**. The producer
and analyzer input is the flat study file `SUITE_MANIFEST.json`: eleven exact
case definitions, 110 selected dense/old-model cell pairs, 99 p1/3/5 baseline
rows, two invalid-control flags, precise producer configuration paths and
archived executed-module dependency hashes. The broader inventory is retained
to make exclusions and unavailable alternatives explicit. No other original
easy task is excluded.

## Width and task coverage

Width **2048** has the broadest archived old closure/Gaussian/orthogonal
comparison: all twelve original qualitative eight-input tasks have p1,3,5.
Two of those tasks also have p6,7,8,9. Six later confirmation task labels add
fresh seeds/perturbed geometries; one duplicates an original geometry. Thus
2048 has eighteen named task/seed conditions and seventeen distinct
geometry/label pairs, before exclusions. The twelve-case original suite is
the only broad original suite common to all three old orders p1,3,5.

| Reference width | Archived tasks | Old closure/control orders | Current analysis |
|---:|---|---|---|
| 512 | `four`, `eight` | ours/Gaussian/orthogonal p1,3 | `analysis01` |
| 1024 | `quadrant_alternating`, `two_outliers_alternating` | ours p1,3,5; parameter-matched small exact networks, no Gaussian/orthogonal | `matched_network_analysis01` |
| 2048 | twelve original qualitative tasks below | ours/Gaussian/orthogonal p1,3,5 | `diverse_analysis01`, with two tasks superseded as described below |
| 2048 | original `quadrant_pairs`, `two_outliers_alternating` | ours/Gaussian/orthogonal p1,3,5,6,7,8,9 | `scaling_discovery_analysis01` |
| 2048 | `pairs_confirm1`, `outliers_confirm1`, `negative_confirm1` | ours/Gaussian/orthogonal p1,5,9 | `scaling_confirm1_analysis02` |
| 2048 | `pairs_confirm2`, `outliers_confirm2`, `negative_confirm2` | ours/Gaussian/orthogonal p1,5,9 | `scaling_confirm2_analysis03` |
| 4096 | original `quadrant_pairs`, `two_outliers_alternating` | ours/Gaussian/orthogonal p1,3,5,7 | `scaling_width4096_analysis02` |

All analysis names in this document are beneath
`data/generated/random_dictionary_learned_circle_20260920/`.
The small exact-network widths in the 1024 campaign are 55/58/75 for the
trained-parameter matches and 105/221/397 for total-model-size matches. They
are different model sizes within those two task conditions, not extra full
reference widths with a broad dictionary-control suite.

The original phase-I `four` and `eight` tasks are distinct from all twelve
phase-II tasks. Their baselines exist only at n512. If “all earlier tasks”
includes these two, an all-at-2048 comparison cannot reuse an existing 2048
dense/control archive for them. This inventory does not authorize reruns.

## Exact original width-2048 inputs

These are the literal `CASES_V2` definitions in `diverse_cases.py`, and the
executed `diverse_primary01/config_worker0.json` agrees. All use physical
circle radius sqrt(2), normalized API inputs `(cos(theta), sin(theta))`, and
the same network seed **20260920** and coupled random-dictionary seed **7319**
(layer index is added for separate layer draws). All have eight points,
four positive labels and four negative labels. No original case is marked
as a rotated confirmation variant.

| Case | Angles in degrees | Labels in listed order |
|---|---|---|
| `quadrant_grouped` | 10,20,30,40,50,60,70,80 | ++++---- |
| `quadrant_alternating` | 10,20,30,40,50,60,70,80 | +-+-+-+- |
| `quadrant_pairs` | 10,20,30,40,50,60,70,80 | ++--++-- |
| `quadrant_center_edges` | 15,21,27,33,39,45,53,60 | --++++-- |
| `equal_semicircles` | 0,45,90,135,180,225,270,315 | ++++---- |
| `equal_mixed_odd` | 0,45,90,135,180,225,270,315 | ++-+--+- |
| `near_equal_grouped` | 8,48,96,142,187,230,281,322 | ++++---- |
| `two_clusters_grouped` | 10,22,34,46,125,137,149,161 | ++++---- |
| `two_clusters_split` | 10,22,34,46,125,137,149,161 | ++--++-- |
| `three_clusters_mixed` | 15,27,39,140,152,263,275,287 | +++--+-- |
| `one_outlier_grouped` | 12,22,32,42,52,62,72,225 | ++++---- |
| `two_outliers_alternating` | 15,27,39,51,63,75,165,285 | +-+-+-+- |

`equal_semicircles` was subsequently reused as the geometry of an explicit
negative control with a fresh seed. `near_equal_grouped` is an original task
where old random controls also did well, but it is not named an explicit
confirmation negative control. Performance alone does not define a case
exclusion. Keep the prior negative-control exclusion as directed by the user;
the confirmed suite exclusion is the original `equal_semicircles` geometry.

## Confirmation variants and explicit negative controls

The exact later definitions are in `scaling_cases.py`.

| Task | Angles | Labels | Seeds network/dictionary | Classification |
|---|---|---|---|---|
| `pairs_confirm1` | 19,28,38,47,58,67,79,88 | ++--++-- | 20260921/8521 | shifted/jittered nearby paired task; not an exact rotation |
| `outliers_confirm1` | 25,37,50,60,74,84,178,297 | +-+-+-+- | 20260921/8521 | shifted/jittered cluster and moved outliers; not an exact rotation |
| `negative_confirm1` | 0,45,90,135,180,225,270,315 | ++++---- | 20260921/8521 | explicit negative; exact original `equal_semicircles` geometry, fresh seed |
| `pairs_confirm2` | 96,106,116,125,137,146,158,169 | ++--++-- | 20260922/9623 | explicitly rotated/jittered paired variant |
| `outliers_confirm2` | 91,104,116,129,142,154,238,351 | +-+-+-+- | 20260922/9623 | explicitly rotated cluster with moved outliers |
| `negative_confirm2` | 17,62,107,152,197,242,287,332 | ++++---- | 20260922/9623 | explicit negative; exact 17-degree rotation of regular grouped octagon |

The group-2 positive variants also change gaps; they are not exact duplicate
geometries modulo rotation. Calling them rotated variants follows their
frozen descriptions. Group 1 remains a separate possible interpretation of
“earlier tasks except rotated variants”; it is not part of the original
twelve-case suite. Confirmation has no p3 archive, so requesting matched
old p1,3,5 on those variants exposes a missing p3 cell rather than a failed fit.

## Authoritative current references and selection

For ten original cases use `diverse_analysis01/{metrics,validation,selected_levels,
summary,analysis_provenance}.json`. For `quadrant_pairs` and
`two_outliers_alternating`, use
`scaling_discovery_analysis01/{metrics,validation,summary,provenance}.json`.
The latter retains the historical p1/3/5 closure endpoints but recomputes their
errors against newly tightened dense endpoints. Do not splice values from
`diverse_analysis01` into a comparison using these newer dense endpoints.

Dense-reference selections are:

| Cases | Selected coarser root | Selected finer root | rtol pair |
|---|---|---|---|
| nine originals other than the three rows named below | `diverse_primary01` | `diverse_refined01` | 1e-3 / 2.5e-4 |
| `quadrant_alternating` | `diverse_refined01` | `diverse_fine_early01` | 2.5e-4 / 6.25e-5 |
| `quadrant_pairs` | `scaling_discovery_primary01` | `scaling_discovery_refined01` | 6.25e-5 / 1.5625e-5 |
| `two_outliers_alternating` | `scaling_discovery_primary01` | `scaling_discovery_refined01` | 6.25e-5 / 1.5625e-5 |

Each root contains `<case>_full/{arrays.npz,summary.json}`. Atol is rtol/100.
Every selected dense reference currently passes its archived <=0.01 endpoint
refinement gate. Exact discrepancies and paths are in the inventory JSON's
`current_original_dense_references`.

The original suite selected each model's latest two attempted levels,
independent of fitting status or comparative performance. There were 101
cells with two levels, eleven with three, and eight with four. Extra cohorts
at equal tolerances are disjoint: `diverse_fine_early01` and
`diverse_fine_late01` use 6.25e-5; `diverse_finer_early01` and
`diverse_finer_late01` use 1.5625e-5. Nineteen selected cells differ from the
original primary/refined pair. The companion JSON contains all nineteen
explicit selections as well as all 120 original cell selections. No reuse
code should infer a model's numerical pair from the dense-reference pair.

Scaling selection similarly uses the latest two attempted levels, retaining
failed attempts. The discovery outlier Gaussian p7 uses its refinement and
one extra attempt, with rtol 1.5625e-5 / 3.90625e-6. Fresh group-1 outlier
orthogonal p5 and fresh group-2 outlier orthogonal p1 have the same extra-level
pattern. The complete authoritative selections are inside `validation.json`
and `provenance.json`, not a scaling `selected_levels.json` file.

## Missing, unfitted, and invalid cells

All 267 original width-2048 trajectories fitted: 120 primary, 120 tighter,
and 27 selected additional accuracy attempts. All selected original endpoints
passed archived fitting and replay. There are no missing files among the
selected original/current-discovery paths checked for this inventory.

Two original comparison cells remain unresolved by the fixed own-endpoint
sampled-maximum discrepancy cutoff 0.01:

| Case/model | Selected own-endpoint discrepancy | Status |
|---|---:|---|
| `quadrant_alternating_gaussian_p1` | 0.010127009631221817 | fitted/replayed, refinement unresolved |
| `quadrant_alternating_orthogonal_p5` | 0.04146386790700052 | fitted/replayed, refinement unresolved |

All other original p1/3/5 rows pass, including all three old closure orders on
`quadrant_alternating`. Thus 106/108 original method/reference comparisons
are valid; the all-method common valid case set has eleven cases. The original
twelve-case descriptive aggregate remains explicitly not wholly validated.
These two cells must remain visible and flagged if their task is included;
there is no baseline rerun in the present assignment.

All 42 current discovery comparisons and all 27+27 final confirmation
comparisons pass the archived numerical and separate metadata checks.
The 4096 archive has a different unresolved cell:
`two_outliers_alternating_orthogonal_p5`, discrepancy 0.05371220463817572;
23/24 comparisons pass there. This is not a failure of its n2048 counterpart.
The phase-I 512 comparisons and all 1024 matched-network rows passed.

Missing orders are untested cells, not fitting failures: p2/p4 are absent from
old suites, most original tasks have no orders above p5, confirmation lacks
p3, and n2048 has no `four`/`eight` baselines. The old p1/3/5 counts are
(K1,K2)=(5,3),(35,10),(128,21). The derivative p1/3/5 counts differ; matching
an order label does not match dictionary size or middle-parameter count.

## Equations and reuse conventions

`analyze.evaluate_saved` implements, for normalized direction u,

```
h1 = tanh(w @ u)
z2 = b2 @ M @ (b1.T @ h1 / n)     # closure
z2 = A @ h1                       # dense
f  = c @ tanh(z2) / n
```

The compressed initial middle coefficient is
`D = b2.T @ A0 @ b1 / n`; first weights and actual random readout are shared
with the dense initialization. The effective middle action and its transpose
use the same coefficient matrix. Every model trains all three moving blocks.
Old dictionaries use only initialized fields, Chebyshev words/tails and
ridge eta=1/[1024(p+1)^2]; Gaussian and orthogonal dictionaries share random
spans but have different frame conditioning. Phase-I random maximal draw
shape is (35,10), while phase-II is (128,21). Scaling preserves the phase-II
prefix and appends a separate block through (720,55). A seed alone does not
identify the same random basis when the maximal draw shape changes.

For selected numerical level ell, theta_j=2*pi*j/8192 and j=0,...,8191,

```
e_j = f_model(theta_j; own first MSE<=0.001 endpoint)
    - f_full(theta_j; full's own first MSE<=0.001 endpoint)
RMS_ell = sqrt(mean_j(e_j**2))
L1_ell  = mean_j(abs(e_j))
max_ell = max_j(abs(e_j))
```

The stored field `l2` means RMS, and `refined_l2` is the selected-finer score.
The own-endpoint refinement gate is `max_j|f_finer-f_coarser|<=0.01` for
both model and dense reference, separate from the discrepancy between their
RMS errors. Eligibility requires fitted/replayed model and dense endpoints;
validity also requires their refinement gates and aligned finite grids.
The first crossing is localized by parameter-chord bisection inside an
accepted Heun step. It is not an analytically exact gradient-flow crossing.
Sampled maxima are not continuous-circle supremum certificates. A suite
mean is the arithmetic mean of case RMS values, not pooled RMS.

## Minimal complete source/evidence reading for implementation

For the original twelve tasks and their current baselines, read completely:

1. `diverse_cases.py` for exact inputs; the original-study README's complete
   phase-II protocol, amendment, final-result and source sections.
2. `diverse_benchmark.py` for the accepted-step controller, own-endpoint
   localization, snapshot schema and resource stops, plus `benchmark.py`
   for initialization imports, circle convention, shared setup and helpers.
3. `diverse_dictionary.py` for old basis/count/seed conventions and
   `analyze.py` for exact saved-state replay.
4. `diverse_analyze.py` and `diverse_refine.py` for the latest-two rule,
   validity, common-case aggregation and numerical selection criterion.
5. `diverse_analysis01/{metrics,validation,selected_levels,summary,
   analysis_provenance}.json`; all selected cell `summary.json`, worker
   config JSON and needed NPZ members; `diverse_analysis_check.md` for the
   final selection/metric audit and its precise limitations.
6. For the two superseded-reference cases, `scaling_analyze.py`, complete
   `SCALING_RESULTS.md`, and
   `scaling_discovery_analysis01/{metrics,validation,summary,provenance}.json`.
   Also read the executed scaling producer/configuration and its dictionary
   helper if regenerating or independently verifying basis construction.

For confirmation scope add `scaling_cases.py`, `SCALING_PROTOCOL.md`, the
matching final analysis roots above, and `scaling_gate_audit.md`. The analyzer's
`valid` flag alone does not enforce dictionary metadata or declared execution;
the archived separate metadata checks supply those gates. Relevant archived
evidence is `scaling_gate_audit01/D_gate.json`. The failed C2 analysis and
one-bit archive repair are historical provenance, and only final
`scaling_confirm2_analysis03` should be used.

For the two n512-only tasks add the original README protocol/results and
`primary01/config.json`, `refinement01/config.json`, plus the phase-I
analysis files and selected raw files. For n1024 or n4096, use their separate
complete protocols/results and named final analyses; do not substitute their
reference curves at n2048.

The confirmed execution scope is derivative p1/3/5 on the eleven original
qualitative cases other than `equal_semicircles`. Both confirmation groups
and the n512-only phase-I tasks are outside that fixed scope. None of the
included cases was selected or excluded by its new-model performance.
