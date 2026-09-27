# Saved-state continuation check

Scoped implementation and output check only; no training was run by this
reviewer. Inputs were the assigned quick-comparison code and the two quick
campaigns `quick_blocks1024_20260926` and
`quick_blocks1024_loss001_20260926` in this study's generated directory.

The updated driver loads saved w, W, c rather than calling initialization
when resuming. It verifies the checkpoint hash and canonical source hashes,
then uses the unchanged unrestricted dense canonical RK45 implementation.
The continuation clock is offset by the saved physical time in the result
and every recorded history row. The stopping target is passed explicitly.

All 12 outputs passed independent saved-data checks:

- Checkpoint hashes match both the source files and recorded old hashes;
  new output hashes and source hashes match their manifests.
- Initial continuation history time and MSE equal the saved previous
  endpoint time and MSE exactly.
- Recomputed final training MSE equals its saved value exactly, and is at
  or below 0.001 for every trajectory; all stop reasons are target.
- Every saved absolute RMS against Gaussian and HD recomputes exactly.
- Maximum recorded total continuation duration is 2.199077632278204 s.

For each method m, the RMS change in its difference function relative to
Gaussian is RMS((f_m,new - f_G,new) - (f_m,old - f_G,old)). This is distinct
from the change in the scalar RMS distance itself:

| Task | HD | block8 | block32 | block128 |
|---|---:|---:|---:|---:|
| cluster_triple_cos9 | 0.002426246 | 0.001635178 | 0.000942177 | 0.003181079 |
| alternating5 | 0.003337074 | 0.006097643 | 0.005545828 | 0.004561489 |

The cluster block32-to-block128 upturn persists after this tighter loss
stop. This continuation changes only the stopping loss and does not resolve
middle-weight sampling variability, solver refinement, width dependence,
or the zero-loss limit.

The plotting script `plot_block_continuation.py` reads only the two saved
comparison JSON files and writes `block_continuation.png` and
`block_continuation.pdf` in the continuation output directory. The two
panels show block sizes 8, 32, 128 at both stopping losses, with clearly
labeled HD and Gaussian-control reference lines. Both files use the same
vector drawing; the PNG was visually inspected. Installed ReportLab was
used because Matplotlib is unavailable; no dependency was installed.
