# Quick Gaussian-block implementation check

Scope: the four assigned files `dense_compare.py`, `dense_wide_integrator.py`,
`circle_tasks.py`, and `quick_block_compare.py`, followed by the explicitly
assigned `quick_blocks1024_20260926` generated manifest, results, comparisons,
completion record, and saved NPZ states. No training was performed. This is a scoped implementation check, not a
promotion review or numerical-convergence certification.

Checked final `quick_block_compare.py` SHA-256:
`1f382fa1dc1a87b27309885ffc5442eec1a019de27efef6ea0f0ce0c4267d0b8`.

No blocking correctness issue found:

- Each k-by-k Gaussian block contains independent standard normals divided
  by sqrt(k), hence entry variance 1/k and expected Frobenius norm squared
  divided by width equal to one. All remaining initial entries are zero.
- Outer weights use exactly the same seed streams as HD and Gaussian.
  Block streams depend only on seed and block size, independently of the
  task, and receive no realized-norm normalization.
- Training calls the full dense canonical RHS with an unrestricted dense
  middle matrix. At width 8, packed canonical RHS and optimized flat RHS
  agreed exactly. With 2-by-2 Gaussian blocks, all 48 initially off-block
  entries had nonzero canonical velocity.
- At width 128 and seed 17, block8/block32/block128 initialization exactly
  matched explicit reconstruction and matched HD outer weights bit for bit.
  Packed RHS equality held exactly for every method tested. All 15,360
  off-block velocities for block8 and 12,288 for block32 were nonzero.
- Both circle discrepancy expressions are absolute function RMS without
  output normalization. Synthetic constant predictions verified both
  Gaussian-reference and HD-reference values for all 12 analysis rows.
- MSE 0.01 stopping uses the existing dense interpolant and Brent boundary
  refinement. Results independently recompute training MSE before setting
  the fitted flag. The checkpoint retains an accepted state; solver stage
  construction does not mutate the previously accepted arrays.
- The final source sets BLAS thread environment variables before importing
  NumPy/SciPy and no longer imports the unavailable optional threadpoolctl.

Limits to preserve in reporting:

- The 50-second solver deadline and 55-second interrupt cover training.
  Whole-circle evaluation and serialization follow afterward; actual
  end-to-end duration must therefore be inspected for the under-60-second
  requirement. The recorded total_seconds precedes final JSON hashing and
  writing by a small amount.
- The generated prose assumes fitted endpoints, so any timeout or failure
  needs explicit partial-result labeling. The Gaussian-reference fitted_pair
  flag does not certify the HD endpoint used by rms_vs_hd.
- One seed and width, and no solver refinement, support only this bounded
  initialization comparison.

## Completed-output verification

All 12 saved trajectories stopped at the target and independently recomputed
to training MSE at or below 0.01. Maximum recorded run duration was
12.584342643618584 seconds. Every current source hash matched the frozen
manifest and every saved NPZ hash matched its result record.

Recomputing each saved state's training predictions and all 2048 circle
predictions gave zero difference from the saved values. Recomputing every
absolute circle RMS against both Gaussian and HD references gave zero
difference from the comparison records. The maximum 2048-versus-1024-grid
RMS change was 2.42861286636753e-17. All fitted-pair flags were true, so the
partial-result caveats above do not apply to this completed campaign.
