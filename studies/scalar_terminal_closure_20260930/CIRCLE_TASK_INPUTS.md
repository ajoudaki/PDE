# Five shallow manuscript circle tasks

Extracted 2026-09-30 from the authorized portable manuscript bundle. No training was run, no plotting module was imported, and no referenced study/archive path was opened. NumPy loaded the bundle with `allow_pickle=False`. The bundle hash equals the one recorded in its companion manifest.

All five tasks have **m=8 physical samples and d=2**, two hidden tanh layers, binary labels, and no biases. The stored task order is the one in `description_json["shallow"]`. The degrees below are human-readable nominal values; the JSON retains the exact stored binary64 radians.

| Case | Nominal angles in degrees | Labels in the same order |
|---|---|---|
| `two_outliers_alternating` | 15, 27, 39, 51, 63, 75, 165, 285 | 1, -1, 1, -1, 1, -1, 1, -1 |
| `quadrant_alternating` | 10, 20, 30, 40, 50, 60, 70, 80 | 1, -1, 1, -1, 1, -1, 1, -1 |
| `quadrant_pairs` | 10, 20, 30, 40, 50, 60, 70, 80 | 1, 1, -1, -1, 1, 1, -1, -1 |
| `quadrant_center_edges` | 15, 21, 27, 33, 39, 45, 53, 60 | -1, -1, 1, 1, 1, 1, -1, -1 |
| `equal_mixed_odd` | 0, 45, 90, 135, 180, 225, 270, 315 | 1, 1, -1, 1, -1, -1, 1, -1 |

## Data fields and exactness

The JSON contains `tasks`, with `case`, `title`, `m`, `d`, `bundle_fields`, `train_angles_radians`, `labels`, `normalized_inputs_u`, and `paper_inputs_x`. Corresponding hexadecimal values and per-array SHA256 hashes record the exact float64 payloads. The original bundle labels are int64; conversion of ±1 to float64 is exact. Reloading the JSON reproduces every recorded float64 array hash.

Task i uses `shallow_i_train_angles`, `shallow_i_labels`, and the optional 8192-query field `shallow_i_angles`. The saved prediction arrays `P0/P1/P3/P7` were not copied into the experimental input JSON.

Cartesian inputs are derived by NumPy float64 `u = column_stack((cos(theta), sin(theta)))`, using the exact copied bundle radians. The portable bundle has no original Cartesian input arrays. This derivation reproduces the manifest-recorded original Cartesian hashes for both quadrant-alternating and quadrant-pairs tasks. It does not reproduce those hashes for the other three tasks, so those arrays are explicitly marked as reconstructions. For equal-mixed-odd, reconstruction directly from its nominal integer-degree angles does match the original hash, demonstrating the effect of an angle round trip on final bits. No unverified claim of bitwise original Cartesian recovery is made.

The equally spaced task retains all eight physical points and the listed odd antipodal labels. Historical closure archives used a four-point antipodal quotient; this extraction does not impose that reduction.

## Normalization and physical-time model

Use the stored `normalized_inputs_u` directly in `h_a=tanh(A @ u_a)`. These are unit directions with input Gram `G_ab = u_a.T @ u_b`. In the manuscript notation, `x_a=sqrt(2)*u_a` and `d=2`, so `A @ x_a/sqrt(d)=A @ u_a`. The JSON also supplies these `paper_inputs_x`. Do not divide unit u by sqrt(2) a second time. This matches the manuscript circle convention `x/sqrt(d) in S^1`, and the paper tools describe the unit direction as an already normalized input.

The model uses `g_a=tanh(B @ h_a)`, `f_a=w.T @ g_a/n`, residual `f-y`, and unhalved mean squared loss. Canonical block mobilities are `(n,1,n)`. Dense training updates the full middle matrix; q=1 uses the study reconstruction with the same fixed W0 and its true transpose, and `tau_dot=sqrt(loss)`.

## Initialization and historical comparison boundary

- First-weight entries: independent N(0,1). Fixed middle-mixer entries: independent N(0,1/n), independent of first weights.
- Current study: stored readout is exactly zero; q=1 starts with v=0, k=h, tau=1. Dense and q=1 should share their sampled A and W0 in the proposed comparison.
- Historical small-readout convention: stored entries N(0,1/n^2), hence standard deviation 1/n, as specified by maintained `docs/notation.qmd`; the manuscript itself says small readout. The portable bundle does not contain initial arrays or all producer settings, so it does not independently certify each historical draw or RNG sequence.
- Historical shallow gallery: width 2048, q=1/3/7, and each model at its own training-MSE 0.001 endpoint. The requested width 1024 and exact-zero-readout comparison is a new experiment on these task geometries, not a bitwise replay of those endpoints. No experiment seed is selected by this extraction.
- The unrelated `tikz_figures.py` moments illustration uses width 512 and stored readout standard deviation 0.1. Its settings must not be mistaken for the five shallow-circle datasets.

## Provenance

| Authorized source | SHA256 |
|---|---|
| `paper/main.tex` | `fa44deda090a456640b64080767511003dc8bc385790ccc49fd039c931a67605` |
| `paper/scripts/README.md` | `bd2d5d494b395a76813c7fa7127772abb3b0e4ba64ca47cddc79872c299d11c8` |
| `paper/scripts/figures.py` | `2c6e6385fd4add52ae3af2c589bf7f291914aaab6e4eb71a4047f8a484704c0a` |
| `paper/scripts/tikz_figures.py` | `852cf19bc08762727655cbbeff2db1926d74cc13c9004c4b1b9d75db21cbdc2b` |
| `paper/figures/radial_source_data.npz` | `b7abae22e5513da1233842d9b204c5af9c069949cbc76c5a2c4f05d3dd28684e` |
| `paper/figures/radial_source_manifest.json` | `f8bf276fe9ce2c9dba857d585dab9008607a548d47a890525aa1c3d881b40df9` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |

The manifest contains historical source-record paths and hashes; these were treated only as metadata and were not followed. Its stored array hashes were used for the Cartesian reconstruction checks above.

`circle_task_inputs.json` SHA256: `9bef8baaec4fd2def993eb9849236a8f3a0042eb9bd7a8d0305f1d55172b7400`.

Validation completed: portable bundle hash, five task identities, 8-by-2 shapes, binary labels, unit-direction norms, and exact float64 JSON round trips. No original initialization array, future training trajectory, or other study result was imported.
