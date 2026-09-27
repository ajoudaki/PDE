# HD versus Gaussian: width2048 fitted-function results

**Complete: all twelve tasks, all36 selected networks, reached training MSE1e-4. The experiment was not restarted when the user specified that threshold. Remaining queued work and additional refinement runs have been stopped.**

Each row uses the first paired seed (seed0), selected before inspecting2048 comparisons to avoid waiting for repeated seeds. HD, Gaussian reference and Gaussian control share the outer initialization; the Gaussian control uses an independent middle matrix. All middle entries train unrestricted. HD is only the initialization.

The reported quantity is the absolute RMS of the predicted-function difference over the circle: sqrt(mean_theta (f_candidate-f_Gaussian)^2), evaluated at4096 uniform angles. There is no division by Gaussian signal amplitude and no teacher-risk comparison.

| Task | RMS(HD − Gaussian) | RMS(Gaussian control − Gaussian) |
|---|---:|---:|
| pair_cos1 | 0.008871 | 0.002534 |
| pair_cos3 | 0.008500 | 0.002415 |
| near_pair_sin9 | 0.001562 | 0.004414 |
| triple_cos3 | 0.009276 | 0.005282 |
| triple_mixed | 0.003163 | 0.003922 |
| cluster_triple_cos9 | 0.045780 | 0.013199 |
| broad_ridge6 | 0.001497 | 0.000780 |
| sharp_ridge8 | 0.001859 | 0.000913 |
| alternating3 | 0.005880 | 0.009914 |
| alternating5 | 0.005853 | 0.005576 |
| alternating9 | 0.024136 | 0.034503 |
| multiscale12 | 0.001851 | 0.000556 |

HD is of similar or smaller discrepancy than the Gaussian control on several tasks, including all three alternating designs in this paired realization (alternating5 is slightly larger). The clustered three-point case remains notably different:0.045780 versus0.013199. Two-point cosine cases also exceed their control discrepancies. These are observations for one paired seed at2048; they do not establish a seed-averaged bias or prove equality/inequality of infinite-width limits.

## Numerical and stopping checks

- All36 selected saved networks independently satisfy MSE<=1e-4; maximum recorded MSE is9.999999999999998e-5.
- No accepted training-loss increase was recorded for the selected runs.
- Largest change in either reported RMS difference between4096 and2048 circle grids is3.123e-17.
- Prelaunch2048 tolerance refinement on the three-point Gaussian case changed its fitted circle function by4.376e-7 RMS. Additional refinement campaigns were cancelled at the user’s request; this is not an all-task refinement certificate.
- Saved dense weights reproduce the independently audited training and full-circle predictions exactly.
- The slow multiscale fits stopped at physical times850.237 (Gaussian),829.991 (control),948.389 (HD). They are included as fitted results, not replaced by an earlier endpoint.

## Artifacts and reproduction

- [Machine-readable analysis](../../data/generated/structured_full_rank_scalar_20260926/wide_hd_analysis_20260926/summary.json) and [per-seed table](../../data/generated/structured_full_rank_scalar_20260926/wide_hd_analysis_20260926/per_seed.csv).
- [Protocol](WIDE_HD_PROTOCOL.md), [driver](run_wide_hd.py), [adaptive dense integrator](dense_wide_integrator.py), [analysis](analyze_wide_hd.py).
- [Prelaunch numerical validation](../../data/generated/structured_full_rank_scalar_20260926/wide_integrator_validation_20260926/validation.json) and [saved-weight audit](../../data/generated/structured_full_rank_scalar_20260926/wide2048_saved_state_audit.json).
- Raw runs, full fitted weights, exact commands, source snapshot and hashes: `data/generated/structured_full_rank_scalar_20260926/wide_hd_main_20260926/`.
- The original queued campaign was stopped immediately after all36 seed0 fits were available.34 other already-queued runs finished in the meantime; they remain retained and are excluded from this uniformly selected one-seed table. No confidence intervals are inferred from one seed.

Reproduce the selected design in a fresh directory with `python studies/structured_full_rank_scalar_20260926/run_wide_hd.py --output NEW_DIRECTORY --width 2048 --seeds 0 --target 1e-4 --workers 3`. This command is documentation only; no further run was started.
