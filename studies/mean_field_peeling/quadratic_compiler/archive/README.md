# Historical and rejected compiler artifacts

These files are retained for provenance and comparison, not presented as the
active exact compiler.

- `MATROID_WICK_AUDIT.md`, `matroid_wick_evaluator.cpp`, and
  `matroid_sector_driver.cpp` preserve a useful restricted no-weight-hit
  theorem and an explicitly rejected unrestricted rank shortcut.
- `component_recursion_parallel.cpp` and `component_term_evaluator.cpp` refer
  to missing temporary implementation files and are not reproducible active
  drivers.
- `leading_wick_jet_forest.cpp` and `maximal_sector_peeling.cpp` are older
  precursors superseded by the current exhaustive and connected engines.
- `peeling_lower_bound_order13_historical.json` preserves exact integer lower
  bounds but also contains an obsolete threshold, path, and concluding status;
  current interpretation is in the Stieltjes report.
- `derivatives_order5.json` is a strict historical subset of the current
  order-eleven derivative certificate.

Nothing in this directory should be used as an active certificate without the
scope and supersession warnings in its adjacent audit.
