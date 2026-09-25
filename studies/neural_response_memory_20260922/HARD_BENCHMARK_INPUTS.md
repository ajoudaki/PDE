# Frozen recovery of earlier hard circle benchmarks

Read-only empirical-input recovery, 2026-09-24. This report identifies exact
earlier configurations, normalization, selected references, and baseline scores
for the supervisor's authorized numerical comparison. It imports no unrelated
research conclusions. No training, GPU computation, Git operation, or old-file
mutation was performed. The `investigate-conjectures` skill's source hierarchy
and supersession discipline were applied. This report is the only new artifact.

## Identified benchmark and representative cases

The hard case is `two_outliers_alternating`, at n=2048 with network seed
20260920. The final derivative-p7 finer RMS is **0.7564240400073452**, against
the selected dense endpoint. This resolves the approximate recollection of
0.78. A nearby **0.7885934435962814** is derivative p5 at **n=4096**, from
`gradient_flow_probe_dictionary_20260921/P45_RESULTS.md`; it must not be used
as a width-2048 baseline. At n=2048 final derivative p5 is 0.8682871537888046.

The following are original cases, with no confirmation rotation or fresh seed.
Here “exclude negative controls” means excluding `equal_semicircles` and the
later `negative_confirm*` variants; it does not mean making labels nonnegative.
All original labels are ±1.

| Case | Angles, degrees | Labels in order | Role |
|---|---|---|---|
| `two_outliers_alternating` | 15,27,39,51,63,75,165,285 | +−+−+−+− | Hardest final derivative-p7 case |
| `quadrant_alternating` | 10,20,30,40,50,60,70,80 | +−+−+−+− | Tight alternating case; second-largest p7 RMS |
| `quadrant_pairs` | 10,20,30,40,50,60,70,80 | ++−−++−− | Same tight geometry with paired labels |
| `two_clusters_grouped` | 10,22,34,46,125,137,149,161 | ++++−−−− | Optional easier separated-cluster check |

These cases have eight uniformly weighted training points, with normalized API
coordinates u=(cos θ,sin θ), corresponding to physical x=√2 u. Their complete
authoritative literal definitions are `random_dictionary_learned_circle_20260920/diverse_cases.py`.
The original source explicitly checks consistency with oddness at antipodes.

## Canonical model, initialization, and optimization

The archived dense target is the finite bias-free two-hidden-layer tanh network

    h1 = tanh(w @ u)
    h2 = tanh(W2 @ h1)
    f  = c @ h2 / n.

Both hidden widths are n; w has shape (n,2), W2 (n,n), c (n,). All blocks train.
`code/pde/finite_network.py:initialize` draws from a **NumPy**
`np.random.default_rng(20260920)` sequentially:

    w  = rng.standard_normal((n,2))
    W2 = rng.standard_normal((n,n)) / sqrt(n)
    c  = rng.standard_normal(n) / n.

Thus stored variances are (1,1/n,1/n²), while f has the additional 1/n
readout normalization. `NetworkEngine` copies these arrays to Torch; replacing
this with `torch.manual_seed`/`torch.randn` does not reproduce initialization.
Loading the archive's first w,c,M snapshots is the strongest finite-realization
match. Dense M denotes W2; closure M denotes its much smaller middle core.

Loss is the **unhalved** mean squared error, (1/8) sum(f−y)². Optimization is
simultaneous full-batch **physical gradient flow**, with block mobilities
(n,1,n), numerically integrated using adaptive Heun with embedded Euler error
estimation. It is not L-BFGS. `code/pde/finite_torch.py:NetworkEngine.rhs`
implements the exact finite gradient field, including the factor 2 from the
unhalved loss. Readout initialization is the actual nonzero finite draw.

The original closure replaces the entire middle action by B2 M B1ᵀ/n, with
no dense residual. Its moving count is 3n+K1 K2, and fixed dictionary storage
is n(K1+K2). Frozen derivative dimensions are p1=(2,4), p3=(6,12),
p5=(14,24), p7=(26,46), i.e. 6,18,38,72 vectors. At n2048 the moving
counts are 6152,6216,6480,7340. Old action-word/Gaussian/orthogonal p1,p3,p5
dimensions are (5,3),(35,10),(128,21), i.e. 8,45,149 vectors and moving
counts 6159,6494,8832. Order labels between these constructions are different
budgets. Random dictionary seed is 7319, with layer offsets; the original
Gaussian/orthogonal controls use the same underlying raw columns, RMS
normalization versus QR. Derivative dictionaries have no extra random draw.

## Endpoint target and numerical settings

Each model stops at its **own** first detected training-MSE 0.001 crossing.
The dense target is that dense model's own crossing, not a prescribed teacher
function, common physical time, fixed epoch count, or fitted-label interpolation.
The primary metric is RMS difference on θ_j=2πj/8192, j=0,...,8191.
The nested 4096-node check takes every other node; stored trajectory snapshots
use 2048 nodes. Secondary metrics are L1 and sampled maximum, not a certified
continuous-circle supremum.

Typical primary/finer tolerances are (rtol,atol)=(6.25e−5,6.25e−7) and
(1.5625e−5,1.5625e−7). Initial/max/min step sizes are .05/2/1e−7, maximum
time 10000, maximum accepted steps 30000, and per-trajectory integration wall
cap 180 seconds. The error controller scales w,c by RMS and the middle error
by the Frobenius norm of its trained increment, clamped below by 1. Accepted
steps pass both error and loss-decrease gates. The first threshold crossing is
localized by 30 bisections on the accepted Heun step's parameter chord.

Float64 CUDA, deterministic algorithms, and TF32 disabled were used. Original
replay tolerance was 1e−10 and selected-pair endpoint sampled maximum gate .01.
Do not assign a single numerical level to every historical control: selected
levels differ by cell and are frozen in the manifest and final metrics.

## Selected raw references

All paths below are relative to the repository; each trajectory directory has
`arrays.npz` and `summary.json`.

| Case/model | Primary directory | Finer directory |
|---|---|---|
| Hard dense | `data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_primary01/two_outliers_alternating_full` | `data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_refined01/two_outliers_alternating_full` |
| Quadrant alternating dense | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/quadrant_alternating_full` | `data/generated/random_dictionary_learned_circle_20260920/diverse_fine_early01/quadrant_alternating_full` |
| Quadrant pairs dense | `data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_primary01/quadrant_pairs_full` | `data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_refined01/quadrant_pairs_full` |
| Hard derivative p3 | `data/generated/gradient_flow_probe_dictionary_20260921/suite_primary01/two_outliers_alternating_new_p3` | `data/generated/gradient_flow_probe_dictionary_20260921/suite_refined01/two_outliers_alternating_new_p3` |
| Hard derivative p7 | `data/generated/gradient_flow_probe_dictionary_20260921/p7_primary01/two_outliers_alternating_new_p7` | `data/generated/gradient_flow_probe_dictionary_20260921/p7_refined01/two_outliers_alternating_new_p7` |

For quadrant alternating the selected dense rtols are **2.5e−4 / 6.25e−5**,
with atols rtol/100. Hard and quadrant-pairs selected dense rtols are
6.25e−5 / 1.5625e−5. The dictionary's own primary/finer levels need not match
the dense reference's numerical tolerances. Use the selected reference mapping.
For the two discovery cases the later scaling dense pair supersedes the older
diverse dense pair, so earlier report scores cannot simply be spliced in.

The raw archive contains endpoint_prediction, endpoint_angles, endpoint_inputs,
training_inputs, labels, times, losses, accepted_steps, local_error_ratios,
and snapshots of w,c,M. Read state index 0 for initialization and index −1
for endpoint. Frozen closures also store b1,b2,D,g,p1,p2. The p3 factors and
initial middle core are available directly; no feature reconstruction is needed
merely to load their exact baseline.

`studies/gradient_flow_probe_dictionary_20260921/SUITE_MANIFEST.json` is the
authoritative per-cell selection map (`archive_cells`). The final 143-row
metrics are `data/generated/gradient_flow_probe_dictionary_20260921/p7_analysis_final01/metrics.json`.
Three rows are unresolved: quadrant_alternating new_p3, gaussian_p1,
orthogonal_p5. Preserve these flags. Final derivative p7 and p5 are valid on
both requested hard cases.

## Antipodal inputs and compatible finite-sample variants

None of the four candidate training geometries above contains exact antipodal
pairs. The original `equal_mixed_odd` geometry does: angles 0,45,...,315 with
labels ++−+−−+−. Its four pairs have opposite labels. Bias-free tanh networks
are exactly odd at every parameter state, so this is consistent; labels all
nonnegative would be a different and, at these antipodes, incompatible target.

Every **8192-node evaluation grid** has antipodal pairs j and j+4096. An odd
hidden-feature Gram over that entire grid is necessarily singular. Do not
treat the grid as an invertible training covariance. Queries can stay passive,
or one can evaluate one representative of each antipodal pair and reconstruct
the opposite output by oddness. Also distinguish the raw input Gram, whose
rank is at most 2 here, from a nonlinear hidden-feature Gram; absence of
antipodes alone is no proof of a quantitative minimum-eigenvalue bound.

For an odd model and opposite antipodal labels, merging each training pair
(u,y),(−u,−y) into representative (u,y) with combined probability preserves
the exact empirical loss and its parameter gradient: both squared residuals
are identical. Thus the equal_mixed_odd data have a four-representative form
at angles [0,45,90,135], labels [1,1,−1,1], probabilities 1/4. This is an
explicit quotient representation, not an eight-independent-sample test. It
does not cure raw input rank ≤2, and its new closure state dimension must be
reported. Altering angles, adding coordinate jitter, changing labels, or
using a new finite-width/population initializer is a **new derived variant**:
freeze it under a new identifier, recompute the matched dense reference, and
do not compare its RMS directly with the archived p7 score as if identical.

For the requested hard and quadrant-alternating comparison, retaining their
literal eight training samples avoids an unnecessary geometry change. Any
conditioning problem still requires measurement for the actual matrix used.

## Width 1024 coverage

The archived n1024 experiment contains exactly `quadrant_alternating` and
`two_outliers_alternating`, seed20260920, with old action-word p1,p3,p5 plus
ordinary smaller exact networks. It has **no** Gaussian/orthogonal control
suite and **no** derivative-p7 baseline at this width. References live in
`data/generated/random_dictionary_learned_circle_20260920/matched_network_primary01`
and `matched_network_refined01`, with task directories suffixed `_full`.
Final metrics are in `matched_network_analysis01/metrics.json`.

Finer old closure RMS on quadrant alternating is 2.211645,1.296558,0.828471
for p1,p3,p5; on hard outliers it is 1.068625,0.445081,0.417358. These are
different finite targets from n2048 and must be kept separate. Smaller exact
network widths were 55,58,75 for moving-parameter matches and 105,221,397 for
total-storage matches. They take fixed prefixes of the n1024 initializer,
rescaling middle by sqrt(1024/m) and readout by 1024/m; they are not newly
seeded independent networks. All 12 comparisons favored the smaller exact
networks at both levels. This is historical finite-realization evidence only.

## Reproduction entrypoints and environment

The recorded interpreter is `/home/amir/miniconda3/bin/python -B`, Python
3.10.14, Torch2.9.0+cu130, NumPy1.26.4. Worker environment:

    PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 CUBLAS_WORKSPACE_CONFIG=:4096:8

`studies/random_dictionary_learned_circle_20260920/diverse_benchmark.py:trajectory`
is the reusable canonical integrator. Its arguments are
`(engine, initial, case, directory, rtol, atol, worker_start, worker_limit)`.
It can run a dense `code/pde/finite_torch.py:NetworkEngine` or compatible
closure engine. The original full-suite CLI uses coarser default tolerances;
calling the function with explicit settings avoids accidentally inheriting
those defaults. Derivative runners are `suite_run.py` (p1,p3,p5) and
`p7_run.py` in `gradient_flow_probe_dictionary_20260921`. They load the same
archived dense initial arrays. Width1024 runner is `matched_network_benchmark.py`
in the original-circle study.

The original hard dense primary command was:

```sh
/home/amir/miniconda3/bin/python -B studies/random_dictionary_learned_circle_20260920/scaling_benchmark.py --out data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_primary01 --group discovery --stage A --orders 6 7 --all-orders 6 7 8 9 --include-full --worker 1 --device cuda:1 --level 0 --budget 400
```

Its finer command replaces `primary01` with `refined01` and `--level 0` with
`--level 1`. These are provenance commands pointing to existing immutable
outputs, not instructions to rerun or overwrite them. New runs require fresh
study-owned output paths and a separately frozen scope. The original p7
worker0 command uses `p7_run.py --out .../p7_primary01 --worker 0 --level 0
--device cuda:0 --budget 225`, with corresponding level1/refined01.

The complete `HANDOFF_SCALING.md` was read as requested. It records an earlier
pause; its unfinished-stage status and older scores are superseded by the
actual completed final archive and are not a current instruction to resume
that campaign.

## Evidence boundary

Recovered numbers below are parsed from the final saved metrics, with selected
paths/configuration cross-checked. This is not a new independent full-state
replay, integrator validation, or theorem about the current autonomous closure.
The new model's comparability to the finite target, initialization coupling,
query readout and optimization must be checked by its experiment producer.

## Frozen final n2048 baseline table

All entries are the selected finer RMS against the task-specific selected dense
reference. “Unresolved” preserves the original numerical validity failure.

| Method | K1,K2 | Vectors | Outliers | Quadrant alternating | Quadrant pairs |
|---|---|---:|---:|---:|---:|
| new_p1 | 2,4 | 6 | 2.5924157727 | 3.4048174944 | 0.8243076524 |
| new_p3 | 6,12 | 18 | 1.1001187614 | 0.1552626892 (unresolved) | 0.0725992023 |
| new_p5 | 14,24 | 38 | 0.8682871538 | 0.1206759358 | 0.1049956623 |
| new_p7 | 26,46 | 72 | 0.7564240400 | 0.4053070204 | 0.0437607177 |
| old_p1 | 5,3 | 8 | 1.0375956546 | 2.2819170174 | 0.2855114107 |
| old_p3 | 35,10 | 45 | 0.5497616018 | 1.2888273625 | 0.1653880265 |
| old_p5 | 128,21 | 149 | 0.3815793961 | 1.1146217332 | 0.0944342626 |
| gaussian_p1 | 5,3 | 8 | 1.5623915773 | 2.9656721220 (unresolved) | 0.6585710858 |
| gaussian_p3 | 35,10 | 45 | 1.3792666460 | 2.4618823002 | 0.5507259089 |
| gaussian_p5 | 128,21 | 149 | 1.2024059456 | 2.3314518521 | 0.4872423173 |
| orthogonal_p1 | 5,3 | 8 | 1.5857121278 | 2.8966576497 | 0.6326299691 |
| orthogonal_p3 | 35,10 | 45 | 1.3028328933 | 2.4810545925 | 0.5991560090 |
| orthogonal_p5 | 128,21 | 149 | 1.1764175473 | 2.3307599145 (unresolved) | 0.4562408611 |

`new` means derivative dictionary; `old` means initialized action-word/Chebyshev
dictionary. Gaussian and orthogonal controls remain separate.

## Fresh source identities

SHA-256 hashes computed on 2026-09-24 for consumed key files. Raw NPZ hashes
from the earlier input audit remain available in
`studies/adaptive_response_compression_20260922/BENCHMARK_INPUT_CHECK.md`;
this recovery does not claim to have recomputed those raw hashes.

| File | SHA-256 |
|---|---|
| `studies/random_dictionary_learned_circle_20260920/HANDOFF_SCALING.md` | `8d3a2984a47fb08c05a9fd9e26f0c588df4bef755eb4b45aa8a45e618b0cf824` |
| `studies/random_dictionary_learned_circle_20260920/diverse_cases.py` | `65942e3e8e52b2f4af10242963c0159cda80a8c80f9d2c8dc9f77c5d9d3aa6f4` |
| `studies/random_dictionary_learned_circle_20260920/diverse_benchmark.py` | `9556b9baaa89643a6dc474873b6536f6dda7a4e3cad0bd3fbba9fee2a9a3b43e` |
| `studies/gradient_flow_probe_dictionary_20260921/SUITE_MANIFEST.json` | `d34ea135c3a2d60dcccce94f23114d92a3692ac3475d13fc3d20dd68387b3670` |
| `studies/gradient_flow_probe_dictionary_20260921/P7_RESULTS.md` | `3e42499f82a3db4ef7cde71fc4db4bfa7144d130db15bfe4f47d21caacb3389a` |
| `studies/adaptive_response_compression_20260922/BENCHMARK_INPUT_CHECK.md` | `70ecd326c8b20f47bb0a4651978773865a86e28b0d9ef8f2ecec4deaa32cb074` |
| `data/generated/gradient_flow_probe_dictionary_20260921/p7_analysis_final01/metrics.json` | `26f2fb79228f04e23609e295b84589b5261dfa444d88abedfe4388e6c1d7316f` |
| `data/generated/gradient_flow_probe_dictionary_20260921/p7_analysis_final01/validation.json` | `72ef70c1cee548e927216b601474c909323afeede56c081c45538faf4888f391` |
| `data/generated/random_dictionary_learned_circle_20260920/matched_network_analysis01/metrics.json` | `9a487e1a5cd6f739acb12cf246119e861ae82608362648c9f48b9f4083316a3a` |
| `data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_primary01/config_A_worker1.json` | `c903ac22d84fb8cf1af3274c20e85f35b026d5614d77648f9d0e27b95de1076d` |
| `data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_refined01/config_A_worker1.json` | `2fb526af2112725ab42efa561d2f4067e01ace2ec7dd1f1fb9da37c6d2074508` |
| `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/config_worker1.json` | `77f9555d2ea6a912d2a3e79e00d68a018652b3ac62be45bc9003ac65159637de` |
| `data/generated/random_dictionary_learned_circle_20260920/diverse_fine_early01/config_worker0.json` | `ab4697a5c4a9764f00b3905de8369462ddb303228b27c1baed7375d7d57fc3f2` |
| `code/pde/finite_network.py` | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/finite_torch.py` | `76d87cb0ddd25e974acf85935dc8fbfc8bc4a9eb829d5e60782e64d20e4f55a8` |

## Higher-order old action-word controls on discovery cases

These additional archived orders are different constructions and budgets from
derivative p7. Finer RMS uses the same selected dense references above.

| Order | K1,K2 | Vectors | Hard old | Hard Gaussian | Hard orthogonal | Pairs old | Pairs Gaussian | Pairs orthogonal |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 6 | 213,28 | 241 | 0.3967536399 | 1.0187985723 | 0.9939627774 | 0.0869890178 | 0.3900507036 | 0.3890828103 |
| 7 | 333,36 | 369 | 0.4303998289 | 1.0150085308 | 0.8554135081 | 0.0500180355 | 0.3168031603 | 0.3648066556 |
| 8 | 499,45 | 544 | 0.3569042745 | 0.9176082453 | 0.7145763682 | 0.0448557781 | 0.2624468169 | 0.2962522166 |
| 9 | 720,55 | 775 | 0.3347863906 | 0.8201736894 | 0.6486360851 | 0.0259805097 | 0.1900525483 | 0.2723617570 |

Source `data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_analysis01/metrics.json` SHA-256 `63453140ed57a4a67e0fbf8ad95179c7417d7d6c7d432a4f2c780ab1c5bcb4ea`.
