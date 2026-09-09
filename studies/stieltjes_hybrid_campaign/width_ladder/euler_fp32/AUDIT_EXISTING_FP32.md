# Read-only audit of the pre-existing FP32/RK4 side artifacts

This audit was completed before any fresh Euler trajectory.  No file under
`global_proxy_campaign/` was modified.

## Artifacts

| artifact | initialization/evolution | status | array SHA-256 |
|---|---|---|---|
| `canonical_n4096_r8_fp32_control_20260814` | native PyTorch FP32 draws, FP32 RK4, h=2e-5, 8 pairs | validation only | `f342176c43ff063d3ae07cff1bfa2627c8c8452270989bf13d2e527020d357e1` |
| `canonical_n4096_r8_fp32_cast_control_20260814` | PyTorch FP64 draws cast once to FP32, FP32 RK4, h=2e-5, 8 pairs | validation only | `0858bdf27e67629e94b7656677de32e24f34cf2bd3283722d4c1b06bce28af15` |
| `canonical_n8192_r8_fp32_holdout_20260814` | PyTorch FP64 draws cast once to FP32, FP32 RK4, h=2e-5, 8 pairs | validation only | `67320120f7d4499ae2ee2bce84a95f6ee6a4589de85cf176dcaed8e6d1a1048f` |

All three use canonical model source SHA-256
`57c8f7732ff164582a02578a30c747c22c5f27a54ca3c3624e7f6aff62a8be7e`.

## Reusable information

- They establish that FP32 evolution of the canonical model is operational on
  RTX 3090 GPUs through width 8192.
- The measured wall times were about 102 seconds for n=4096, 8 pairs, and 400
  seconds for n=8192, 8 pairs, using the older RK4 engine.
- The float64-draw-then-cast runs give gross curve controls: at y=0.9 the old
  effective kernels were 164.75845 (n=4096) and 164.23494 (n=8192).
- The arrays contain raw output, direct kernel, weighted kernel, loss,
  component means, and pair summaries, so they can be compared descriptively
  against a fresh validation run.

## What cannot be reused as scientific evidence

- The runs are explicitly marked `complete_validation_only` and
  `scientific_evidence_admissible=false`.
- Reusing a stateful PyTorch seed with differently shaped tensors did not make
  the n=4096 state a coordinatewise prefix of the n=8192 state.  They are not a
  coupled width ladder.
- Native FP32 draws and float64-draw-then-cast produce materially different
  eight-lineage initialization samples: K_eff(0) was 107.66053 versus
  114.94235 at n=4096.  This is sampling/RNG-stream confounding, not a precision
  comparison.
- No exact unchanged-update fractions, representative W-coordinate monitor,
  or per-step update/state norm diagnostics were recorded.  The artifacts
  therefore cannot rule out FP32 update stalling.
- They used RK4 at h=2e-5, not explicit Euler at h=5e-6.
- Their batching (four lineages at n=4096, two at n=8192) can change GPU
  reduction order and does not validate the new one-lineage execution path.

Conclusion: the artifacts are valuable performance and gross-curve validation
controls only.  They cannot authorize or substitute for the fresh nested,
stall-monitored Euler campaign.

## Later side-check artifacts found in the shared visualization workspace

A second read-only pass found additional validation-only work under
`/home/amir/.codex/visualizations/2026/08/14/019fff0b-20b5-7c23-8d3e-178d14b24fdd/`:

- `gd-vs-rk4-n8192-h5e-6.json`: matched old PyTorch initialization, Euler
  h=5e-6 versus the frozen FP32/RK4 curve.  Maximum relative effective-kernel
  error was `1.3506519139232681e-4`.
- `gd-vs-rk4-n8192-h2p5e-6.json`: halving Euler to h=2.5e-6 worsened the
  maximum relative error to `1.603835023649116e-3`, direct evidence that FP32
  rounding—not Euler truncation alone—becomes relevant at smaller steps.
- `gd-vs-rk4-n4096-result.json`: among h=2e-5, 1e-5, 5e-6, the finest step
  had maximum relative effective-kernel error `1.393450455136175e-4`, although
  the old preregistered output-error gate left the overall run inconclusive.
- `gd-n16384-eight-pair-h5e-6.json`: eight-pair exploratory Euler result.
  First-step sampled-W unchanged fractions ranged from about 44.7% to 46.8%;
  readout unchanged fractions were about 2.4%--2.6%.  This makes per-step
  realized-update monitoring mandatory and is why width 16384 receives zero
  fresh budget in the initial campaign.

These checks use the old non-nested RNG/batching and remain external
validation.  They remove the need for a fresh broad RK4 ladder.  The smallest
new validation is one nested n=8192 antithetic lineage at Euler h=1e-5 and
h=5e-6, with exact update diagnostics; the h=5e-6 scientific step is retained
only if that gate passes.
