# Numerical investigations

The numerical work is split into only two branches:

- [`direct_loewner/`](direct_loewner/) records the initial direct Loewner and
  common-clock investigations;
- [`finite_width/`](finite_width/) records the later preregistered calibration,
  stopped-flow, and order-thirteen pilot experiments.

Each branch keeps code and protocols at its root and stores generated outputs
under one `runs/` directory.  Frozen manifests and integrity files preserve
their original paths and hashes as historical provenance.

Git tracks compact JSON summaries, manifests, integrity notes, and run
commands. Raw `.npz` arrays, logs, diagnostic CSV files, and bootstrap payloads
are excluded; manifests or `RAW_DATA_SHA256.txt` files retain their hashes and
sizes.
