# Scalar output-dependency order on three fitted configurations

2026-09-27. Continuation explicitly requested by the user: test a parameter
specific to scalarization, holding the block population model fixed.

## Question and frozen comparison

Does adding the next generation of output-derivative contractions lower
the raw circle RMS discrepancy from the matched block population closure?
The competing outcome is that the remaining feedback truncations or their
coupling prevent consistent improvement. This tests this selective refinement,
not all scalar closures or the convergence of the full degree hierarchy.

Call the output-dependency depth J. Compare the saved J=1 runs with new J=2
runs on exactly `pair_orthogonal_cos1`, `cluster_triple_cos1`, and
`triple_wide_mixed`. J=2 retains the derivative children of the derivative
children of the output contractions, alongside the existing protected
feedback/Gram set. All retained variables are aggregate contractions.
No population, histogram, frozen dictionary or reference trajectory enters
the runtime ODE. The sets are nested, but monotone error reduction is not
assumed; fixed feedback truncations remain.

Keep tanh, k=4, history P=1, seed1, n=1024 initialization, mark bound3,
essential feedback protection, zero omitted-term boundary, dependency_depth0,
64 equally spaced circle queries plus passive copies of every training
input. Initial contractions use exactly the same matched block realization,
which is discarded before scalar integration. Preserve canonical scaling,
original activity clock, and core training MSE threshold0.01.

Read-only J=1 observations and both fitted controls are in
`data/generated/structured_full_rank_scalar_20260926/selective_geometry_20260927/`.
New outputs go in the separate `selective_order_20260927/` namespace.
Do not rerun controls or J=1 merely to produce a new table.

## Metrics, hypotheses and numerical gates

Primary: raw circle RMS of scalar output minus matched block-population
output (k4/P1), evaluated at each model's first MSE0.01 endpoint. Secondary:
the same RMS relative to fitted canonical Gaussian. These are differences
between predicted functions, not label risk or signal-normalized error.
Report both orders, fractional changes, actual scalar counts and wall times.
Report the core and passive training losses and same-input alias gaps.

A reduction of at least5% in all three fitted comparisons is evidence of a
consistent practically visible benefit at these two orders; mixed signs or
smaller effects are reported as such. An increase of at least5% is adverse
evidence for monotone improvement on that task. An unfinished run is a
partial comparison, not a fitted improvement or a hierarchy failure.

Keep float64 RK45 rtol1e-5, atol1e-7, first step0.01, maximum step1,
maximum physical time3000; error norm is maximum scaled RMS over the shared
core, each passive-query block and clock. Check passive independence and
vectorized versus separate RHS; initial alias equality; finite accepted
states; saved-state prediction decoding; source/data hashes; same exact
reference circle angles. Compare 64-point RMS to its 32-point subset;
a change above0.001 flags insufficient quadrature evidence. No new numerical
reruns are authorized by this protocol; flag an unresolved issue explicitly.

## Budget and terminal condition

Three new J=2 trainings only. Per task: compilation<=60seconds,
100000 template states,1000000 retained terms; initialization<=90seconds;
training<=45seconds, keeping the last accepted state on timeout. Cumulative
scalar training<=135seconds; campaign wall ceiling12minutes. Use BLAS1 and
at most one scalar training job at a time. No deeper order, seed sweep,
scientific cutoff modification, or resumption of stopped runs.

Exact implementation improvements may remove redundant setup or evaluation
only when they preserve the selected ODE and numerical checks. Record any
such change; never substitute a smaller scientific problem silently.

Root owns protocol, interpretation and README. Runner agent owns the new
driver and run records. Independent checker owns its checker and check
outputs. Stop after the three results and their bounded read-only audits.
