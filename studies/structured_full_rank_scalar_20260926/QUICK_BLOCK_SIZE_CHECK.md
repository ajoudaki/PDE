# Intermediate block-size check

Scoped audit of `fill_block_sizes.py` and its assigned seed-1 baseline and
fill outputs. No training was performed by this reviewer; numerical
verification used one BLAS thread.

The driver launches exactly two serial trajectories, block16 and block64,
through unchanged canonical `quick_block_compare.run_one`, at width 2048,
seed 1, target training MSE 0.001. Its block streams are [1,316] and [1,364].
The other fitted states, including the single Gaussian reference, are
reused after hash checks. Outer weight streams and block variance 1/k are
unchanged, and every trajectory learns an unrestricted dense matrix.

Independent checks passed:

- Current and frozen source hashes, baseline manifest hash, all reused
  baseline state hashes, and fresh data hashes match exactly.
- Both new saved states have the declared width and shape. Their final
  training MSEs recompute exactly and are at or below 0.001.
- All seven comparison rows use the identical saved Gaussian reference
  and identical circle grid. Their absolute circle RMS values recompute
  exactly, and all fitted-pair flags are true.
- Only block16 and block64 appear in the new training results. Maximum
  recorded new-run duration is 38.11253246665001 seconds.

| Block size | Absolute circle RMS vs Gaussian |
|---:|---:|
| 8 | 0.04751698055676166 |
| 16 | 0.02869702817418038 |
| 32 | 0.019698069858897452 |
| 64 | 0.017951651881333734 |
| 128 | 0.024712180518485543 |

HD is 0.052540724986446276 and the Gaussian control is
0.02140953076878774. In this saved-seed sample, the distance decreases
through block64 then increases at block128. The independent block-size
streams and single realization do not establish a population optimum.

`plot_block_sizes.py` produces a single panel on a log2 block-size axis,
with labeled HD and Gaussian-control reference lines. PNG and vector PDF
are saved only in `quick_blocks2048_seed1_fill_20260926`. The PNG was
visually inspected and labels adjusted to avoid overlaps.
