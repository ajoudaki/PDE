# Outcome-free static audit of the factor control

A scoped code reviewer received only `factor_hypergradient.py`,
`FACTOR_HYPERGRADIENT_PROTOCOL.md`, `hypergradient.py`, and relevant portions
of `baseline_compact_flow.py`, plus required presentation instructions. The
reviewer read no experimental outcomes, made no changes and ran no experiments.
This was a static implementation audit, not an independent promotion review.

Findings:

- No derivative or initialization mismatch was found. Factor mobility one
  reproduces source `LowRankFlow`; normalization and zero-readout initialization
  are consistent.
- The 173 planned inner solves are correctly counted, including seven CPU
  validation trajectories.
- The five-minute budget is checked only before an inner solve, and the main
  timer begins after GPU initialization. It is not a strict process deadline.
  The actual run's recorded interval is 67.67 seconds, so no overrun occurred.
- Peak allocation and per-design time include dense retraining and concurrent
  model storage. The report therefore calls them pipeline costs. The factor
  implementation separately retains 19n initializer coordinates, omitted from
  the raw `fixed_weight_coordinates` field; the report explicitly records them.
- The raw refinement sensitivity measures designed-label MSE drift only.
  The report additionally computes the change in improvement from already
  saved values: abs((E0r-Er)-(E0-E))/(E0-E), where E0,E are original/designed
  dense errors and the suffix r denotes half-step evaluation. Its maximum
  across six runs is .003918; no additional fit was required.
- No test-dependent label selection or material fairness violation was found
  in the fixed six-design comparison.

The source remained unchanged from validation through all six fits. Audit
clarifications changed reporting, not the frozen experiment or its outcomes.
