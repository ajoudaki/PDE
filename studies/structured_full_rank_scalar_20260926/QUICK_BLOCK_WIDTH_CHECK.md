# Width and seed quick-check audit

Scope: assigned quick-comparison driver, dense solver and circle tasks;
the earlier width-1024 MSE-0.001 campaign; the width-2048 seed-0 initial and
finished campaigns; and the width-2048 seed-1 campaign. No training was
performed by this reviewer. Verification used one BLAS thread.

The parameter audit found width, seed, task selection, worker count and
target passed consistently through initialization, job dispatch, output
records and manifests. Canonical unrestricted dense training and Gaussian
block scaling remain unchanged. Matching outer weights is within each
seed; changing seed changes both outer and middle initialization.

The seed-0 initial campaign hit its internal deadlines for five methods.
The finished campaign loads those accepted states and offsets physical time
and history without reinitialization. Previous elapsed time is included
when assigning the remaining cumulative budget. Independent checks found:

- Current and frozen source hashes, saved NPZ hashes and resumed checkpoint
  hashes all match exactly.
- Saved width-2048 states have the declared shapes. Recomputed final
  training MSEs match their recorded values exactly.
- Resumed starting times and MSEs exactly match preceding endpoints and
  the first resumed history row.
- Every saved absolute circle RMS against Gaussian and HD recomputes
  exactly. Fitted-pair flags correctly require both method and Gaussian
  reference to reach the target.
- Seed 0 has five valid target fits. Block8 remains at training MSE
  0.0017236789212103025 and is excluded from matched-target comparisons.
  Maximum recorded cumulative duration is 58.54863676801324 seconds.
- Seed 1 has six valid target fits, all with MSE at or below 0.001.
  Maximum recorded cumulative duration is 45.30073554441333 seconds.
  Maximum 2048-versus-1024-grid RMS change is 2.7755575615628914e-17.

`plot_block_width_seed.py` produces a width panel and a seed panel using a
common vertical scale. Each configuration uses its own fitted Gaussian
reference. HD and Gaussian-control lines are labeled; the invalid seed-0
block8 point is omitted and explicitly identified. The PNG was inspected.
PNG and vector PDF are saved only in the width-2048 seed-1 output directory.

The block32-to-block128 increase in Gaussian-reference error persists in
both width-2048 seeds. The full three-point shape is available only for
seed 1 at width 2048. This bounded evidence does not establish a width rate,
an ensemble distribution, isolated middle-matrix variability, or a
solver-refined or zero-loss limit.
