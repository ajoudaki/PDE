# Frozen additional benchmark inputs

Read-only recovery, 2026-09-24. The supervisor selected two additional original
cases: `quadrant_center_edges` and `equal_mixed_odd`. With `quadrant_pairs`
already underway, these complete the three additional cases beyond the first
two hard runs. No `two_clusters_split` run is selected this round. No training,
GPU computation, scientific trajectory generation, or Git action occurred in
this recovery. Only this report is written.

## Selection rule and full remaining ranking

Exclude already tested `two_outliers_alternating`, `quadrant_alternating`,
and already scheduled `quadrant_pairs`; the historical explicit negative
control `equal_semicircles` is excluded from the eleven-case input manifest.
Use comparable nontrivial dictionary budgets: derivative p5 has 38 vectors,
old action-word p3 has 45. Rank by the larger RMS of these two methods, so a
case may qualify by being hard for either family. This is deliberate historical
stress-case selection, not a fresh unbiased test sample. Both numerical levels
give the same ordering below. The two selected cases are also the next two
hardest by derivative p7 alone and by the comparable small budgets6/8.

| Rank | Remaining original case | max(primary derivative38,old45) | max(refined derivative38,old45) |
|---|---|---:|---:|
| 1 | `quadrant_center_edges` | 0.471047206917 | 0.471448297623 |
| 2 | `equal_mixed_odd` | 0.090854463990 | 0.090831380863 |
| 3 | `two_clusters_split` | 0.073577190241 | 0.073834069567 |
| 4 | `three_clusters_mixed` | 0.068710068222 | 0.068313731056 |
| 5 | `quadrant_grouped` | 0.036941320129 | 0.036727351602 |
| 6 | `one_outlier_grouped` | 0.032974962149 | 0.032950621480 |
| 7 | `near_equal_grouped` | 0.025398470646 | 0.025418253361 |
| 8 | `two_clusters_grouped` | 0.009892758183 | 0.010019697250 |

The alternative maximum of derivative p7 (72 vectors) and old p3 (45) places
`two_clusters_split` narrowly ahead of `equal_mixed_odd`; those are less closely
matched budgets. This alternative ranking is recorded rather than hidden.

## Exact cases and antipodal quotient

All cases use n2048, network seed20260920, d2, tanh without biases, physical
x=√2(cos θ,sin θ), and normalized API input u=(cos θ,sin θ). Frozen dictionary
control seed remains7319. Labels are ±1; “nonnegative-control” does not mean
nonnegative labels. Original arrays are:

```json
{
  "case": "quadrant_center_edges",
  "angles_degrees": [
    15,
    21,
    27,
    33,
    39,
    45,
    53,
    60
  ],
  "labels": [
    -1,
    -1,
    1,
    1,
    1,
    1,
    -1,
    -1
  ],
  "description": "A narrower 45-degree quadrant arc; four central positives and two negatives at each edge."
}
```

```json
{
  "case": "equal_mixed_odd",
  "angles_degrees": [
    0,
    45,
    90,
    135,
    180,
    225,
    270,
    315
  ],
  "labels": [
    1,
    1,
    -1,
    1,
    -1,
    -1,
    1,
    -1
  ],
  "description": "The same equal spacing; neighboring positive and negative pairs plus isolated signs, preserving opposite antipodal labels."
}
```

Center_edges uses all eight samples with equal probability1/8 and has no
antipodal pairs. For equal_mixed_odd use the exact four-representative form:

```json
{"case":"equal_mixed_odd","representation":"antipodal_quotient","angles_degrees":[0,45,90,135],"labels":[1,1,-1,1],"probabilities":[0.25,0.25,0.25,0.25],"original_sample_count":8,"represented_sample_count":4}
```

For any bias-free tanh parameter state, f(−u)=−f(u). Thus each pair
(u,y),(−u,−y) contributes two identical squared residuals. Combining their
probabilities preserves the exact empirical loss as a function of every
parameter, and hence preserves its parameter gradient and canonical physical
GF. The same initialized dense network therefore has exactly the same
mathematical target flow and MSE threshold under this quotient. Ordinary
floating-point trigonometric arrays can differ from exact negation at roundoff;
new reproduction should verify that discrepancy stays at numerical precision.
This is not an assertion that arbitrary closure approximations are invariant
under duplicate constraints. The new closure is explicitly run with **N=4**,
so its sample-indexed states, quadrature dimension and state/storage cost must
be counted at4 and disclosed. Center_edges remains N=8. No angular jitter,
label change or new initializer is authorized by this quotient representation.
Queries remain the same8192-angle circle metric and can use odd reconstruction.

## Selected dense references and tolerances

The dense reference is each model's first detected unhalved MSE0.001 endpoint,
with canonical physical mobilities(n,1,n). New method endpoint comparison is
against this frozen selected dense pair. All four dense references fitted.
The selected dense rtols are1e−3 and2.5e−4, atols rtol/100. These are coarser
than the derivative dictionary's own6.25e−5/1.5625e−5 levels; do not silently
substitute numerical tolerances or reference directories.

| Case | Level | Dense arrays path | Config path | rtol | Endpoint time |
|---|---|---|---|---:|---:|
| `quadrant_center_edges` | primary | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/quadrant_center_edges_full/arrays.npz` | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/config_worker1.json` | 0.001 | 266.29681238284911 |
| `quadrant_center_edges` | refined | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/quadrant_center_edges_full/arrays.npz` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/config_worker1.json` | 0.00025 | 266.12141225172928 |
| `equal_mixed_odd` | primary | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/equal_mixed_odd_full/arrays.npz` | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/config_worker1.json` | 0.001 | 17.50229155934517 |
| `equal_mixed_odd` | refined | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/equal_mixed_odd_full/arrays.npz` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/config_worker1.json` | 0.00025 | 17.47097331756737 |

Selected dense endpoint-refinement sampled maxima: center_edges `0.005136308843798128`; equal_mixed_odd `7.574993125694651e-05`. Both pass .01.

## Frozen selected baseline RMS table

All26 listed case/method rows are valid in the final143-row metrics. These are
8192-angle RMS errors against the corresponding selected dense endpoint, with
each method evaluated at its own first MSE0.001 crossing. The dimensions and
vector counts are nominal retained dictionaries, not all trainable/storage
costs. Gaussian and orthogonal remain separate. `new` denotes derivative;
`old` denotes initialized action-word/Chebyshev.

| Method | K1,K2 | Vectors | Center primary | Center refined | Equal primary | Equal refined |
|---|---|---:|---:|---:|---:|---:|
| new_p1 | 2,4 | 6 | 0.6141474067538121 | 0.6143798228109213 | 0.380797375457646 | 0.3807794356722664 |
| new_p3 | 6,12 | 18 | 0.1701238848597646 | 0.1705427158813994 | 0.1368990934775517 | 0.1368774991048227 |
| new_p5 | 14,24 | 38 | 0.1269961406620676 | 0.1274712524717946 | 0.09085446398979208 | 0.09083138086254233 |
| new_p7 | 26,46 | 72 | 0.141734303807877 | 0.1422116909042145 | 0.07221578269773855 | 0.0721929915492928 |
| old_p1 | 5,3 | 8 | 0.605065332619412 | 0.6051081024685026 | 0.1046857959188783 | 0.1046424111691822 |
| old_p3 | 35,10 | 45 | 0.4710472069171343 | 0.4714482976229638 | 0.02614237790312745 | 0.02618287547096693 |
| old_p5 | 128,21 | 149 | 0.1583468342791029 | 0.1593076573538794 | 0.03022910858283124 | 0.03018924915186365 |
| gaussian_p1 | 5,3 | 8 | 0.5370362163394052 | 0.5380687633325724 | 0.172038086380967 | 0.1724604189507034 |
| gaussian_p3 | 35,10 | 45 | 0.5115896922061238 | 0.5120776513127285 | 0.1525246607090395 | 0.1528706591806871 |
| gaussian_p5 | 128,21 | 149 | 0.2720767222562749 | 0.2720253234126042 | 0.09596684671686606 | 0.09608795593515371 |
| orthogonal_p1 | 5,3 | 8 | 0.530339255824428 | 0.531228608411244 | 0.1735990219504546 | 0.1739185918634389 |
| orthogonal_p3 | 35,10 | 45 | 0.5025953468295171 | 0.502740103074746 | 0.1666360761714858 | 0.1671043078711743 |
| orthogonal_p5 | 128,21 | 149 | 0.4755969222238725 | 0.4760512841925649 | 0.1230364847054151 | 0.1231742847860456 |

## Exact baseline trajectory paths

Every directory below contains `arrays.npz` and `summary.json`. “Primary” and
“refined” retain the actual selected pair. No case here required an extra
selected level. Derivativep1/p3/p5 use rtols6.25e−5/1.5625e−5; derivativep7
uses the same. Old and random controls use rtols1e−3/2.5e−4; atols=rtol/100.

| Case | Method | Primary directory | Refined directory |
|---|---|---|---|
| `quadrant_center_edges` | new_p1 | `data/generated/gradient_flow_probe_dictionary_20260921/suite_primary01/quadrant_center_edges_new_p1` | `data/generated/gradient_flow_probe_dictionary_20260921/suite_refined01/quadrant_center_edges_new_p1` |
| `quadrant_center_edges` | new_p3 | `data/generated/gradient_flow_probe_dictionary_20260921/suite_primary01/quadrant_center_edges_new_p3` | `data/generated/gradient_flow_probe_dictionary_20260921/suite_refined01/quadrant_center_edges_new_p3` |
| `quadrant_center_edges` | new_p5 | `data/generated/gradient_flow_probe_dictionary_20260921/suite_primary01/quadrant_center_edges_new_p5` | `data/generated/gradient_flow_probe_dictionary_20260921/suite_refined01/quadrant_center_edges_new_p5` |
| `quadrant_center_edges` | new_p7 | `data/generated/gradient_flow_probe_dictionary_20260921/p7_primary01/quadrant_center_edges_new_p7` | `data/generated/gradient_flow_probe_dictionary_20260921/p7_refined01/quadrant_center_edges_new_p7` |
| `quadrant_center_edges` | old_p1 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/quadrant_center_edges_ours_p1` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/quadrant_center_edges_ours_p1` |
| `quadrant_center_edges` | old_p3 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/quadrant_center_edges_ours_p3` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/quadrant_center_edges_ours_p3` |
| `quadrant_center_edges` | old_p5 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/quadrant_center_edges_ours_p5` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/quadrant_center_edges_ours_p5` |
| `quadrant_center_edges` | gaussian_p1 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/quadrant_center_edges_gaussian_p1` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/quadrant_center_edges_gaussian_p1` |
| `quadrant_center_edges` | gaussian_p3 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/quadrant_center_edges_gaussian_p3` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/quadrant_center_edges_gaussian_p3` |
| `quadrant_center_edges` | gaussian_p5 | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/quadrant_center_edges_gaussian_p5` | `data/generated/random_dictionary_learned_circle_20260920/diverse_fine_late01/quadrant_center_edges_gaussian_p5` |
| `quadrant_center_edges` | orthogonal_p1 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/quadrant_center_edges_orthogonal_p1` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/quadrant_center_edges_orthogonal_p1` |
| `quadrant_center_edges` | orthogonal_p3 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/quadrant_center_edges_orthogonal_p3` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/quadrant_center_edges_orthogonal_p3` |
| `quadrant_center_edges` | orthogonal_p5 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/quadrant_center_edges_orthogonal_p5` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/quadrant_center_edges_orthogonal_p5` |
| `equal_mixed_odd` | new_p1 | `data/generated/gradient_flow_probe_dictionary_20260921/suite_primary01/equal_mixed_odd_new_p1` | `data/generated/gradient_flow_probe_dictionary_20260921/suite_refined01/equal_mixed_odd_new_p1` |
| `equal_mixed_odd` | new_p3 | `data/generated/gradient_flow_probe_dictionary_20260921/suite_primary01/equal_mixed_odd_new_p3` | `data/generated/gradient_flow_probe_dictionary_20260921/suite_refined01/equal_mixed_odd_new_p3` |
| `equal_mixed_odd` | new_p5 | `data/generated/gradient_flow_probe_dictionary_20260921/suite_primary01/equal_mixed_odd_new_p5` | `data/generated/gradient_flow_probe_dictionary_20260921/suite_refined01/equal_mixed_odd_new_p5` |
| `equal_mixed_odd` | new_p7 | `data/generated/gradient_flow_probe_dictionary_20260921/p7_primary01/equal_mixed_odd_new_p7` | `data/generated/gradient_flow_probe_dictionary_20260921/p7_refined01/equal_mixed_odd_new_p7` |
| `equal_mixed_odd` | old_p1 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/equal_mixed_odd_ours_p1` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/equal_mixed_odd_ours_p1` |
| `equal_mixed_odd` | old_p3 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/equal_mixed_odd_ours_p3` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/equal_mixed_odd_ours_p3` |
| `equal_mixed_odd` | old_p5 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/equal_mixed_odd_ours_p5` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/equal_mixed_odd_ours_p5` |
| `equal_mixed_odd` | gaussian_p1 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/equal_mixed_odd_gaussian_p1` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/equal_mixed_odd_gaussian_p1` |
| `equal_mixed_odd` | gaussian_p3 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/equal_mixed_odd_gaussian_p3` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/equal_mixed_odd_gaussian_p3` |
| `equal_mixed_odd` | gaussian_p5 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/equal_mixed_odd_gaussian_p5` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/equal_mixed_odd_gaussian_p5` |
| `equal_mixed_odd` | orthogonal_p1 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/equal_mixed_odd_orthogonal_p1` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/equal_mixed_odd_orthogonal_p1` |
| `equal_mixed_odd` | orthogonal_p3 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/equal_mixed_odd_orthogonal_p3` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/equal_mixed_odd_orthogonal_p3` |
| `equal_mixed_odd` | orthogonal_p5 | `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/equal_mixed_odd_orthogonal_p5` | `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/equal_mixed_odd_orthogonal_p5` |

## Initialization and fresh identity checks

Canonical initialization is NumPy `default_rng(20260920)` in layer order:
w=standard_normal((2048,2)); W2=standard_normal((2048,2048))/sqrt(2048);
c=standard_normal(2048)/2048. The forward readout has the additional1/2048.
The actual finite random readout is retained. Loading the dense archive's first
w,c,M snapshots reproduces this realization without relying on a new RNG call;
dense M is W2. It is not the compressed dictionary core. Torch random draws
with the same seed would be a different realization.

Fresh contiguous float64 byte hashes below were computed from each selected
**finer** dense archive's initial snapshots. They agree exactly between the
two cases and with the earlier hard-case initializer hashes in
`HARD_BENCHMARK_INPUTS.md`'s designated input audit. This is an initialization
identity check, not a full-state dynamics replay.

| Case | Initial array | SHA-256 |
|---|---|---|
| `quadrant_center_edges` | `w[0]` | `da24d2b86aed45dfa6e7442e24bfcb968ec28fcfbcfb2f5f07ac066601fffd63` |
| `quadrant_center_edges` | `c[0]` | `460ee22d13695cbe3226805bf5b24b124100e32be5717737508c79d8679b0db6` |
| `quadrant_center_edges` | `M[0]` | `559c9ad62fd9feab4fb4671e854b86ec975240a12aa8792873824ebe2344b3f9` |
| `equal_mixed_odd` | `w[0]` | `da24d2b86aed45dfa6e7442e24bfcb968ec28fcfbcfb2f5f07ac066601fffd63` |
| `equal_mixed_odd` | `c[0]` | `460ee22d13695cbe3226805bf5b24b124100e32be5717737508c79d8679b0db6` |
| `equal_mixed_odd` | `M[0]` | `559c9ad62fd9feab4fb4671e854b86ec975240a12aa8792873824ebe2344b3f9` |

## Frozen file provenance

SHA-256 identities freshly computed2026-09-24. The source manifest records the
executed source chain in each selected configuration; no historical producer
hash mismatch has been repaired or waived by this recovery. Complete literal
case definitions were reread; all143 final metric rows were parsed for the
ranking. No theory sources from other studies were read.

| File | SHA-256 |
|---|---|
| `studies/random_dictionary_learned_circle_20260920/diverse_cases.py` | `65942e3e8e52b2f4af10242963c0159cda80a8c80f9d2c8dc9f77c5d9d3aa6f4` |
| `studies/gradient_flow_probe_dictionary_20260921/SUITE_MANIFEST.json` | `d34ea135c3a2d60dcccce94f23114d92a3692ac3475d13fc3d20dd68387b3670` |
| `data/generated/gradient_flow_probe_dictionary_20260921/p7_analysis_final01/metrics.json` | `26f2fb79228f04e23609e295b84589b5261dfa444d88abedfe4388e6c1d7316f` |
| `code/pde/finite_network.py` | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/finite_torch.py` | `76d87cb0ddd25e974acf85935dc8fbfc8bc4a9eb829d5e60782e64d20e4f55a8` |
| `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/quadrant_center_edges_full/arrays.npz` | `353e1989a8b512e59c04b97b0e91f7c82d355f3c986c01e7968185b0e23d5d5a` |
| `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/config_worker1.json` | `98bc7097f4fafb918f4368cfd543cd3600f7bdaa046500a6a56eb30dc04c8699` |
| `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/quadrant_center_edges_full/summary.json` | `445523dc7323f0e9bc4c4e3aa9dd6277cbaa602ed83013c1e0df77602cf580ea` |
| `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/quadrant_center_edges_full/arrays.npz` | `78393a58cc234fa75efb2571ea65555abf531939eed5e21ae616dd8c421bb377` |
| `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/config_worker1.json` | `77f9555d2ea6a912d2a3e79e00d68a018652b3ac62be45bc9003ac65159637de` |
| `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/quadrant_center_edges_full/summary.json` | `ab48dcbaa154349f043d460190d08bd1f057e12785976aa870e9e502bf4ed03a` |
| `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/equal_mixed_odd_full/arrays.npz` | `8e974ab6f6dfc844c555095aa4cdb04252ed0e5bed35a542daadf4dfff10bb22` |
| `data/generated/random_dictionary_learned_circle_20260920/diverse_primary01/equal_mixed_odd_full/summary.json` | `6344b85ce689aa4a5aec4e866ae7aaf2f43fb332a7a1b46f7f719f642611dd8c` |
| `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/equal_mixed_odd_full/arrays.npz` | `af722eccd7aadd2e70104b12970359aa7d3189a8175e3fd5ee2bc5b3dc35f1e6` |
| `data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/equal_mixed_odd_full/summary.json` | `85c9df21425491687f17fc4e1c5790f5fbb761446f5246123cec1b54b958a2c7` |

Historical scores and selection validity are inherited from the final archive.
Fresh work here comprises parsing, configuration/path checks, file hashes and
initialization identities only. The autonomous-closure comparison, trajectory
validity and finite-sample closure query readout remain the responsibility of
the new producer and its separate checker.
