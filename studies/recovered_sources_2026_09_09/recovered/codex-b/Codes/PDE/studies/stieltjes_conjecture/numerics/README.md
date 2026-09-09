# Numerical investigations

The numerical work is split into four branches:

- [`direct_loewner/`](direct_loewner/) records the initial direct Loewner and
  common-clock investigations;
- [`finite_width/`](finite_width/) records the later preregistered calibration,
  stopped-flow, and order-thirteen pilot experiments;
- [`global_proxy_campaign/`](global_proxy_campaign/) records the exact
  Lambert-$W$ rational-hierarchy calibration and the closed canonical
  finite-width global-curve pilot. Its [terminal result](global_proxy_campaign/RESULTS.md)
  is exact-boundary positive but neural-bridge inconclusive; the frozen hard
  stop prevented all later branches of that campaign;
- [`hybrid_mean_field_campaign/`](hybrid_mean_field_campaign/) records the
  subsequent direct-width/DMFT route audit, [bounded DMFT Stage 0](hybrid_mean_field_campaign/bounded_dmft/STAGE0_REPORT.md),
  the stopped [FP32 Euler qualification](hybrid_mean_field_campaign/width_ladder/euler_fp32/STAGE_V_REPORT.md), and a
  separately frozen [breadth-first panel](hybrid_mean_field_campaign/breadth_panel/RESULTS.md)
  that stopped at FP32 Euler qualification before width extrapolation or any
  Stieltjes proxy-accuracy claim.

Each branch keeps code and protocols near the relevant campaign and stores
generated outputs under branch- or campaign-local `runs/` directories.
Frozen manifests and integrity files preserve their original paths and hashes
as historical provenance.

Git tracks compact JSON summaries, manifests, integrity notes, and run
commands. Raw `.npz` arrays, logs, diagnostic CSV files, and bootstrap payloads
are excluded; manifests or `RAW_DATA_SHA256.txt` files retain their hashes and
sizes.
