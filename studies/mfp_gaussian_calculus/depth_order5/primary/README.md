# Primary Route S artifacts

The primary deliverable is the generated self-contained report
`H3_H4_ORDER5_SELF_CONTAINED.md`.  It embeds byte-for-byte copies of the four
terminal CSE formulas:

- `H3_LAYER_TAGGED_ABC.cse.txt`
- `H3_UNIT_ABC.cse.txt`
- `H4_LAYER_TAGGED_ABC.cse.txt`
- `H4_UNIT_ABC.cse.txt`

The corresponding fully distributed exact-rational maps are the four
`*_COEFFICIENTS.json` files.  The pre-comparison producer freeze is
`PRIMARY_FREEZE_MANIFEST.json`, whose exact-file hash is recorded in
`PRIMARY_FREEZE_SHA256.txt`.

Source roles:

- `depth_population_jet.py`: typed arbitrary-fixed-depth response/Wick--Stein
  compiler;
- `ARBITRARY_DEPTH_RECURSION.md`: mathematical compiler specification and
  state census;
- `generate_frozen_artifacts.py`: deterministic formula/map emitter;
- `compare_frozen_routes.py`: post-freeze literal map comparison;
- `normalized_sine_control.py`: analytic-Fourier moment evaluation;
- `build_self_contained_report.py`: deterministic report builder;
- `run_lightweight_checks.py`: integrity and report-consistency gate.

`POST_FREEZE_EVIDENCE_LEDGER.md` is the current claim ledger.  The older
`EVIDENCE_LEDGER.md` is retained byte-identically because it is part of the
pre-comparison primary freeze.

The frozen formula and map files must not be regenerated in place.  Any
revised producer should use a new freeze/version and rerun all cross-route
comparisons.
