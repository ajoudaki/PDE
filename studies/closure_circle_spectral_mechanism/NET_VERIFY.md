# Supplemental verification of saved wide-network results

2026-09-14. Same-study collaborator check of the frozen `NET_RUN.py` and
`NET_PLAN.md`; this is internal validation, not an independent promotion review.
No training was rerun and the frozen producer was not changed.

The full producer audit confirms the physical stored-coordinate equations:
`h1=tanh(W1 u)`, `h2=tanh(V h1)`, `f=c^T h2/n`, with first/readout
mobilities `n`, middle mobility `1`, unhalved mean squared loss, and
independent stored initializer variances `(1,1/n,1/n^2)`. Both Heun stages
evaluate complete simultaneous states before any block is updated. NumPy
initialization followed by an explicit dtype conversion provides the intended
same-seed pairing of main, half-step, and precision runs. The settling test
uses the disjoint windows `[t-40,t-20]` and `[t-20,t]`, first admitting a stop
at physical time 100. Its 512-angle panel is separate from final 1440-angle
outputs. The wider-branch decision and source archiving are supervisor-owned.

`NET_VERIFY.py` checks the completed 20-run manifest against the prescribed
geometry/width/seed/control design; exact agreement of manifest, per-run
configuration, and record; source bytes against the frozen manifest and
available archived copies; every recorded output-file digest; seeded initial
weight digests after dtype conversion; all saved-array finiteness and shapes;
loss reconstructed from training predictions; recorded loss monotonicity;
clock, endpoint and stopping consistency; and antipodal oddness of both final
curves and all stopping-panel observations.

All eight retained checkpoints are scanned for finite parameters and exact
shapes/dtypes. Their preserved arrays are cast to float64 and evaluated by
independent NumPy matrix equations on all 1440 original circle angles. This
replay does not invoke the trainer. A separate maintained `finite_network`
evaluation on fixed indices `0,10,...,1430` verifies the explicit input
`sqrt(2)` and readout `/n` conventions against those equations. A 64-column
timing estimate selected the full grid under the predeclared 30-CPU-second
replay threshold; the complete verifier used one CPU thread and 8.544 seconds
of CPU time, below its hard 60-second limit.

Command, from the repository root:

```text
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python studies/closure_circle_spectral_mechanism/NET_VERIFY.py --campaign data/generated/closure_circle_spectral_mechanism/network_comparison_001 --output data/generated/closure_circle_spectral_mechanism/network_verification_main
```

All checks passed. Maximum GPU-to-independent-CPU absolute prediction error
was `2.510207970651823e-7` (tolerance `2e-5` for float32); the maximum difference
between the independent equations and maintained NumPy reference was
`4.440892098500626e-16`. Maximum final antipodal discrepancy was
`2.384185791015625e-7`. Every saved observation and all eight retained full
parameter sets were finite. All four source hashes matched both live and
archived bytes, and every recorded output and initialization digest matched.

Evidence is in
`data/generated/closure_circle_spectral_mechanism/network_verification_main/verification.json`
and `independent_replay.npz`; the JSON records individual errors, replay
indices, file/source hashes, timings, and verifier SHA256
`922a6d05a809f482068ff22555350f06560bfde8f30024c34d2e7e23dad274d3`.

Limitations: the 12 unretained full parameter sets cannot be scanned or
independently replayed from endpoints. Their saved observations and recorded
identity/initialization checks pass. No claim is made that every intermediate
parameter state was independently checked. The producer stores initial/final
training Grams and 128-angle paired hidden-motion RMS values, rather than full
paired activation arrays or a time series of hidden Grams. GPU bitwise
reproducibility across different hardware/software is not established by
saved-state replay. Numerical comparisons between trajectories should use
the retained common-time curves when isolating integration/precision effects;
all 20 trajectories here stopped at that common physical time 100.
