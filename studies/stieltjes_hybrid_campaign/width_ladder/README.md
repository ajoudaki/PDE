# Coupled finite-width ladder

This directory is the isolated direct-network branch of the hybrid mean-field
campaign. It leaves the separate `studies/stieltjes_proxy_campaign/` source
and its retained data untouched.

The campaign adds three things missing from the earlier wide-network pilots:

1. coordinate-indexed Gaussian randomness whose arrays are genuinely nested
   across widths;
2. exact finite-width initialization controls and paired-lineage inference;
3. two faithful physical-flow estimands, including bootstrap re-inversion of
   the mean trajectory.

The authoritative scientific design is [PROTOCOL.md](PROTOCOL.md).  A production
configuration is deliberately locked until source tests and GPU preflight pass
and a separate execution unlock is issued.  Generated trajectory arrays live
under repository `data/generated/stieltjes_hybrid_campaign/width_ladder/`
for migrated defaults and are ignored by Git. Retained runs are under
`data/historical/studies/stieltjes_hybrid_campaign/width_ladder/`.
Small manifests remain at their explicitly bound source locations. Old source
hashes/unlocks have not been renewed; these paths do not authorize a rerun.
The original width-point runner requires an explicit `--run-root`; its retained
shell launcher's source-local destination is historical and is not a current
migrated default. Its lock/unlock checks must pass before any attempt is created.

Files:

- `nested_rng.py`: stateless, prefix-consistent Gaussian initialization;
- `width_engine.py`: bounded ordinary physical-flow simulation;
- `width_analysis.py`: estimands, cross-fitted controls, paired bootstrap, and
  frozen extrapolation union;
- `run_width_point.py`: fail-closed, digest-locked point runner;
- `configs/FROZEN_WIDTH_LADDER.json`: declared points and resource caps;
- `tests/`: CPU source and statistical-mechanism tests.

No `n=16384` point exists in the executable config.  The protocol specifies
only the gate that could make such a holdout eligible for later authorization.
The historical `gpu_preflight.py` entry is not present in this directory;
its old command is not a current executable interface. The separate Euler
Stage-V runner preserves its frozen numerical caps and execution gates, and
its old unlock does not bind the migrated generated run root.
