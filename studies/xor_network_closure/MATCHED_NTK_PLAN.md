# NTK radial comparison at matched training loss

User-authorized correction of the radial comparison, 2026-09-14. Preserve the
same-time comparison as a valid historical artifact; create a new plot comparing
training accuracy. This continues the explicitly named XOR experiment.

Use only the checked initial full mobility-weighted kernel blocks, cross-kernel
blocks, initial predictions and retained network/closure outputs in
`data/generated/xor_network_closure/radial_ntk_001/`. The original models and
physical clock are specified in RADIAL_NTK_PLAN.md. No new network training,
kernel fitting, regularization or coefficient selection from off-training outputs.

For each seed 11/29/47, solve the monotone spectral loss equation for the first
time at which the initial frozen NTK reaches that seed's actual-network T=100
training MSE. Reuse the exact exponential propagation formula in RADIAL_NTK.py.
Select stopping time using training loss only. Average the three predictions.
Retain the actual and N1/N3/N5 curves bitwise. This deliberately compares distinct
training times and must be labelled as such. It does not claim infinite-time fit.

Use positive kernel eigenvalues without clipping or a ridge. Bracket by doubling
time from 100, at most 60 doublings; then use 90 bisections. Per-seed loss matching
must have absolute error below 1e-9, and reconstructed training predictions must
agree with the spectral residual formula within 1e-7. Check the 16x16 spectral
calculation and 64 evenly spaced circle points plus all training points using
70-decimal arithmetic on the same stored kernel: prediction error below 1e-6 and
training-loss error below 1e-9. This checks numerical propagation of the saved
kernel; the producer's initialization/forward checks remain separate.

Report stopping times, per-seed/ensemble losses and distances from the actual
network's circle function. These are descriptive; no threshold is set for which
method should win. Do not fit or adjust the curve after viewing the result.
Plot rho=2+f if positive for all curves; if necessary increase the common offset
to ceil(max absolute output)+1 and state it. Expand radial limits rather than
clipping any prediction. Also retain the f-versus-angle plot as an unambiguous
view of off-training predictions and the training targets.

One CPU evaluation of the three retained kernels, no subagents or GPU access,
120-second execution cap and 100 MiB generated output budget. Preserve failures;
stop if numerical gates fail, with no unplanned scientific runs. Output namespace:
`data/generated/xor_network_closure/radial_ntk_matched_001/`. This side-task owns
MATCHED_NTK.py, this plan, its outputs and the scoped README update.
