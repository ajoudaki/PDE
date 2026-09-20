# Independent width4096 output audit

**Final verdict: 23 of 24 closure comparisons pass the numerical gates.**
The outlier-case orthogonal p5 comparison remains unresolved after its one
permitted extra refinement: its latest endpoint discrepancy is
**0.05371220463817572**, above 0.01. No further rerun is permitted by this
protocol. All 3,231 technical output checks pass, and all 48 independently
computed metric records agree exactly with the final reported errors.

This is an internal empirical audit of the explicitly user-requested width4096
continuation. It does not alter the earlier conditional width-branch decision
or establish population/infinite-width convergence.

## Assigned and actual input scope

The assigned scientific inputs are `SCALING_WIDTH4096_PROTOCOL.md`, the existing
independent checker, maintained dependencies if needed, raw producer configs
and archives under the width4096 primary/refined/explicit-extra roots, and the
final analysis outputs as claims to compare. No analyzer source, author report,
other study or other review is read. Manifest-listed sources may be hashed as
bytes by the existing checker; their contents are not interpreted. Root
`AGENTS.md` and workflow hashes remain unchanged from the process instructions
already read. The investigate-conjectures skill and its experiment/audit
references continue to govern interpretation.

At preparation, both primary configs match the new protocol hash, declare
width4096, orders1,3,5,7, the original two case declarations, and thirteen cells
per worker (full plus twelve closures). The intended completed input contains
52 base trajectories, 24 closure comparisons, and 48 model/reference metric
records across two selected levels. Each case and order compares Gaussian and
orthogonal controls separately with ours; no minimum-of-two is a baseline.

## Checker compatibility and planned method

`scaling_independent_check.py` already uses recorded width for state shapes,
normalization and carrier checks. Its historical selection input is guarded by
width2048, so the width4096 run imports no earlier endpoints or selections.
The only preparation change makes protocol hashing honor `config.protocol_path`,
with the original protocol as a fallback for older configs. Syntax and both
current config/protocol metadata checks pass; no GPU work was performed.

The checker independently replays initial/final saved predictions and training
losses; computes CUDA float64 L1, MSE, RMS and sampled maximum endpoint errors;
checks nested8192/4096-grid sensitivity; selects the latest two attempted
levels; and checks each predictor's own endpoint refinement, fit, finite
arrays, dictionary spectra/algebra metadata, declared/executed cells and
producer source hashes. Analysis errors must agree within1e-11, replay within
1e-10, and selected endpoint refinement maxima must be at most0.01. Raw
whitening basis/Cholesky factors are not persisted, so their condition and
triangular residual gates remain checks of recorded metadata with unchanged
producer hashes; normalized spectra and random-basis algebra are recomputed.

The required command, after allocating a GPU, is:

```bash
env PYTHONDONTWRITEBYTECODE=1 PYTHONFAULTHANDLER=1 \
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  CUBLAS_WORKSPACE_CONFIG=:4096:8 \
  /home/amir/miniconda3/bin/python -B \
  studies/random_dictionary_learned_circle_20260920/scaling_independent_check.py \
  --raw-roots \
    data/generated/random_dictionary_learned_circle_20260920/scaling_width4096_primary01 \
    data/generated/random_dictionary_learned_circle_20260920/scaling_width4096_refined01 \
  --cases quadrant_pairs two_outliers_alternating \
  --analysis data/generated/random_dictionary_learned_circle_20260920/scaling_width4096_analysisNN \
  --out data/generated/random_dictionary_learned_circle_20260920/scaling_independent_check_width4096_01 \
  --device cuda:I --max-seconds 180
```

Replace `NN` and `I` with the final completed analysis and allocated GPU; add
only explicitly executed width4096 extra roots if needed. Preserve initial
failed numerical gates rather than selecting by method accuracy. No training
is performed by this audit.

## Preliminary paired-case audit

On the supervisor's explicit CUDA0 allocation, the checker ran with only
`--cases quadrant_pairs` and no `--analysis`, using the primary/refined width4096
roots. It exited0 in 9.449 seconds and saved
`scaling_independent_check_width4096_paired01/checks.json` plus a retained log.
It replayed26 trajectories, recomputed24 paired model/reference metric records,
and verified all thirteen paired predictors' fit, replay, dictionary and own
endpoint-refinement gates. The maximum own endpoint discrepancy is
**0.001028291530585243**; no paired cell qualifies for extra resolution.
The largest prediction/loss replay discrepancy is 4.774e-15.

The overall artifact's `technical_checks_passed` is false because its worker
manifest checks also inspect the unselected outlier worker, which was still
running. Exactly two checks are pending outside the requested paired subset:
outlier refinement worker1's declared/executed cell set lacked five not-yet-
completed cells, and its executed order set did not yet include p7. Every
paired check passes, and `all_selected_numerically_valid` is true. These partial
worker-record flags must be resolved by the final all-case audit; they are not
silently dropped or interpreted as paired numerical failures. No producer or
training action was performed, and CUDA0 was released immediately afterward.

## Complete base-run audit

After all52 base trajectories fitted and all four workers exited0, the
supervisor allocated CUDA1. The checker read only width4096 primary/refined
inputs and compared `scaling_width4096_analysis01`. Its process exited0 in
14.931 seconds, passing all3,204 technical checks over52 replayed trajectories
and48 model/reference metric records. The unselected-worker pending flags
from the preliminary paired audit are now resolved. Exact commands, raw input
hashes and all check values are retained in
`scaling_independent_check_width4096_01/checks.json` and its log.

All48 metric records agree exactly with the reported L1, MSE, RMS and maximum
errors. The largest initial/terminal prediction or loss replay discrepancy is
5.552e-15. All60 producer/maintained source-hash records match. The largest
nested4096-grid metric sensitivity is2.724e-6 for L1,4.441e-16 for MSE,
2.221e-16 for RMS and6.523e-6 for maximum error. The largest recorded raw-Gram
regularized condition is251913.848; the largest recorded triangular residual
is4.330e-15. These satisfy their metadata gates; their reconstruction limit
remains as stated above.

Exactly these cells have both endpoints fitted but fail their own0.01 maximum
endpoint-refinement gate:

| Cell | Maximum endpoint discrepancy | Gate |
|---|---:|---|
| two_outliers_alternating_gaussian_p1 | 0.011023455544842964 | Fail |
| two_outliers_alternating_orthogonal_p1 | 0.01814546073319301 | Fail |
| two_outliers_alternating_orthogonal_p5 | 0.043742954232485864 | Fail |

They qualify for the frozen once-per-cell resolution branch, within its cap
of eight. No paired cell, full reference or other closure fails. These failures
remain in the initial evidence; final selection must use the latest two
attempted levels rather than selecting by method accuracy. CUDA1 was released
after the audit; the independent checker launches no training.

## Final audit after the three permitted refinements

After the extra worker completed all three trajectories, the supervisor
allocated CUDA1 for the final check. The checker waited for the completed
`scaling_width4096_analysis02/provenance.json`, then audited primary, refined
and extra roots into `scaling_independent_check_width4096_02`. The process
exited 0 in 14.864 seconds with all 3,231 technical checks passing. Every
selected initial/final output and loss replay agrees within 5.552e-15; all
48 L1/MSE/RMS/maximum metric records agree exactly with the claimed values.
All 75 producer/maintained source-hash records match their recorded versions.

For every extra cell, the independently selected latest two levels are
refinement `(1.5625e-5,1.5625e-7)` and extra refinement
`(3.90625e-6,3.90625e-8)`, with both endpoints fitted. Their gates are:

| Outlier cell | Initial-pair max discrepancy | Latest-pair max discrepancy | Final gate |
|---|---:|---:|---|
| Gaussian p1 | 0.011023455544842964 | 0.0018859777885733564 | Pass |
| Orthogonal p1 | 0.01814546073319301 | 0.009840226156567766 | Pass |
| Orthogonal p5 | 0.043742954232485864 | 0.05371220463817572 | **Unresolved** |

The orthogonal p5 latest-pair RMS discrepancy is 0.024918533290947367; refining
once did not satisfy the fixed numerical criterion. The earlier and latest
failed pairs are both retained. Its reported endpoint errors are correctly
computed saved-output discrepancies, but cannot support a numerically validated
method-ordering claim under this protocol. There is no authorized second extra
run for this cell. The other 23 closure comparisons and both full references
pass. This is an unresolved numerical approximation, not evidence against
existence of a suitable dictionary approximation.

The maximum final nested-grid sensitivity is 1.942e-6 for L1, 4.441e-16 for
MSE, 2.221e-16 for RMS, and 6.523e-6 for maximum error. These are sampled-grid
consistency diagnostics, not rigorous continuous-circle or flow error bounds.
The raw-Gram/triangular reconstruction limitation remains unchanged.

A separate CPU structural-metadata check confirms the exact 26-predictor cell
set, all 48 unique case/method/order/level records, all 55 declared/executed
training attempts, and every saved nominal dictionary pair
`p1=(5,3), p3=(35,10), p5=(128,21), p7=(333,36)`. No generated input outside
the assigned width4096 roots/analysis was used. This check performs no
scientific metric arithmetic; it is retained in
`scaling_independent_check_width4096_final_scope.json`.

The final numerical-validity flag is therefore false, while the technical
saved-output audit passes. Plots and text must keep the orthogonal p5 outlier
comparison explicitly unresolved. Gaussian and orthogonal remain separate
comparators; no minimum-of-two baseline is introduced by this audit. CUDA1 was
released after the process exited, and this checker performed no training.

## Fingerprints

| Preparation input | SHA-256 |
|---|---|
| SCALING_WIDTH4096_PROTOCOL.md | `f3fa46a38b788d99abe18a51ce1d4bfb224e657222fd051009cab27c04f2a90c` |
| Checker before protocol-path change | `3c1666d0fb5cb83b4175c9a97f27609fd784b44fa314a2e83af5d98020ed3a67` |
| Checker after protocol-path change | `8e2f3684287cbb23aa967cc6c87d14544cb38b08f54b73dfece318348868a382` |
| Preliminary paired checks.json | `a5b69e3e3401dd605993135d73e4b354d04423cf3359f177244564f852401853` |
| Complete base-run checks.json | `76d9efbf83a5f89cd6ca0ae26d20d5183ff73252d0f28fe41b1192fe6804c568` |
| Final checks.json | `819f0c655e685be69391b5a0c8ef27e9d5cc35c38cd0354ebded9c2fe5026ca8` |
| Final structural-scope check | `645ed08b41b152d7c79984ac85c7a9a1ccea1278c212714d7ea354818593746e` |
