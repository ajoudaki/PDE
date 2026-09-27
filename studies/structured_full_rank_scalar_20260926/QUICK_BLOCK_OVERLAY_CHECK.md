# Width-1024/2048 overlay check

Scoped continuation using the assigned seed-1 width-2048 baseline, its
block16/block64 fill, and the new width-1024 output. No training was
performed by this reviewer; all verification used one BLAS thread.

`run_block_overlay.py` calls unchanged `quick_block_compare.run_one`
exactly seven times, serially: Gaussian, independent Gaussian middle-matrix
control, and block sizes 8, 16, 32, 64, 128. All use seed 1 and target
training MSE 0.001, with matched outer-weight streams within each width.
Initialization changes only the initial matrix; training remains dense.

Checks passed:

- All current and frozen source hashes agree with their manifests, and
  canonical source hashes agree across the three input directories.
  The baseline manifest hashes and all saved state hashes match.
- All 15 saved states (seven new, eight existing) have the declared shapes,
  seed, target, training inputs and uniform 2048-angle circle grid.
  Independent forward evaluation from their saved weights reproduces both
  training and circle predictions exactly. Recomputed MSEs and RMS values
  equal every saved comparison; all endpoints are fitted.
- The seven fresh MSEs lie between 0.0009999999997079934 and
  0.0009999999999999848. Each fresh trajectory took 6.6765–8.3981 seconds;
  the full batch took 50.8403 seconds. Each respects the 60-second ceiling.
  Maximum new 2048-versus-1024-angle RMS change is 1.3878e-17.
- Before/after hashes of all 39 existing width-2048 baseline and fill files
  are unchanged, including their original plots and comparison records.

| Block size | RMS, n=1024 | RMS, n=2048 |
|---:|---:|---:|
| 8 | 0.06656543727865252 | 0.04751698055676166 |
| 16 | 0.03210558819410114 | 0.02869702817418038 |
| 32 | 0.02571372689308521 | 0.01969806985889745 |
| 64 | 0.03545402505515821 | 0.01795165188133373 |
| 128 | 0.06303078437193642 | 0.02471218051848554 |

The independent Gaussian controls have RMS 0.012918556489056226 at n=1024
and 0.02140953076878774 at n=2048, each against its corresponding width's
Gaussian reference. In this draw, the sampled minimum is k=32 at n=1024
and k=64 at n=2048. One realization per method and width does not establish
a population optimum or width rate; using the same seed does not imply
identical or fully nested matrices across widths.

`plot_block_width_overlay.py` validates saved data and renders a single
panel with log2 block-size coordinates and a linear absolute-RMS axis.
Colors and marker shapes identify width, and matching dashed lines show
Gaussian controls. HD is omitted. The PNG was visually inspected after
correcting the renderer DPI. PNG and vector PDF are saved only in
`data/generated/structured_full_rank_scalar_20260926/quick_blocks1024_seed1_overlay_20260926/`
as `block_width_overlay.png` and `block_width_overlay.pdf`.
