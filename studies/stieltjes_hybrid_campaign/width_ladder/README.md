# Coupled finite-width ladder

This directory is the isolated direct-network branch of the hybrid mean-field
campaign.  It leaves every artifact under `global_proxy_campaign/` untouched.

The campaign adds three things missing from the earlier wide-network pilots:

1. coordinate-indexed Gaussian randomness whose arrays are genuinely nested
   across widths;
2. exact finite-width initialization controls and paired-lineage inference;
3. two faithful physical-flow estimands, including bootstrap re-inversion of
   the mean trajectory.

The authoritative scientific design is [PROTOCOL.md](PROTOCOL.md).  A production
configuration is deliberately locked until source tests and GPU preflight pass
and a separate execution unlock is issued.  Generated trajectory arrays live
under `runs/` and are ignored by Git; small manifests and final derived
certificates may be promoted deliberately after validation.

Files:

- `nested_rng.py`: stateless, prefix-consistent Gaussian initialization;
- `width_engine.py`: bounded ordinary physical-flow simulation;
- `width_analysis.py`: estimands, cross-fitted controls, paired bootstrap, and
  frozen extrapolation union;
- `run_width_point.py`: fail-closed, digest-locked point runner;
- `gpu_preflight.py`: non-scientific float64 device/RNG/RK4 viability check;
- `configs/FROZEN_WIDTH_LADDER.json`: declared points and resource caps;
- `tests/`: CPU source and statistical-mechanism tests.

No `n=16384` point exists in the executable config.  The protocol specifies
only the gate that could make such a holdout eligible for later authorization.
