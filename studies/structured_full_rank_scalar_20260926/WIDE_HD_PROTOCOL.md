# Width2048 HD rerun: frozen scientific contract

User explicitly requested the same circle tasks with HD and n=2048, 2026-09-26.
Before the principal run, the user explicitly set training MSE stopping to1e-4.
This continues the dense initialization comparison, without scalar compression.

Use all twelve designs in circle_tasks.py, n=2048, seeds0,...,11. Only three
methods: Gaussian reference, independent-middle Gaussian control, and HD.
All methods share the first/readout initialization within each seed. Canonical
small-readout tanh model and all block mobilities are exactly dense_compare.py.
Every middle weight is materialized and evolves freely. HD is initialization,
not a constraint on the trained matrix. No other structured candidates run.

Primary observable per seed is the absolute circle RMS difference
sqrt(mean_theta (f_HD-f_G)^2). Also compute sqrt(mean_theta (f_G2-f_G)^2).
No normalization by Gaussian output or teacher amplitude. Predictions use4096
uniform circle directions; compare with alternating2048-point subset. Report
seed means/spreads and matched paired differences versus Gaussian variability.
The finite-width Gaussian control is an empirical variability baseline, not a
mathematical lower bound for every possible coupling or approximation.

Interpretation: same-scale discrepancy as the Gaussian control is evidence
supporting replacement at this width; clearly larger discrepancy is adverse
evidence. Report actual values and paired95% bootstrap intervals, without an
arbitrary percentage-of-signal acceptance threshold. An interval for the mean
paired difference D_HD-D_G2 excluding zero establishes its direction within
this finite suite; overlapping zero is inconclusive about that direction.
It is not a proof of identical population limits.

Train until the first detected downward crossing of MSE=1e-4, located using
the adaptive integrator dense interpolant and independently checked by a
forward evaluation. Preserve the enclosing accepted-step bracket. Both networks must reach it
before a fitted-predictor comparison is reported. Physical horizon initially
3000, with a preauthorized extension to10000 for nonfitting trajectories if
resources permit. Save complete final physical weights, training loss/time,
first-crossing bracket, solver history and circle predictions. No asymptotic
fit is claimed from a finite training threshold. No post-fitT300 work is needed.

A new adaptive explicit integrator may accelerate computation but must integrate
the same dense vector field. Error control must protect first weights, middle
weights and readout separately; no flat RMS dominated by the n^2 middle block.
Main adaptive Dormand–Prince5(4) tolerances are rtol=1e-5 and
atol=1e-8 for the outer blocks, atol=1e-8/sqrt(n) for middle entries.
Refinements reduce both tolerances by a factor10. A numerical pilot checks
these before the main run; any required change is recorded here. Validate
against existing small-width RK4/Heun. At2048, seed0 triple_cos3 and alternating9
are rerun with tighter tolerance for all three methods; require absolute circle
prediction RMS change<=1e-3. Also check seed0 on the slowest completed task by
training time if not already covered. This latter selection depends on runtime,
not comparative scientific outcome. Quadrature change in paired D<=1e-4.
A loss-increasing accepted step>1e-7, nonfinite state, numerical refinement
failure, or missing fitted endpoint prevents a certified fitted comparison.
Failure permits one tighter-tolerance rerun for that cell; retain original data.

Execution plan:432 principal trajectories, at most12 focused refinement runs,
at most12 failed-numerics reruns, and bounded implementation checks. Main
workers at most12, one BLAS thread each; numerical campaign at most120 wall
minutes, target memory below16GiB. Do not reduce width, replace tasks, or stop
because a scientific outcome is unfavorable. The user may interrupt earlier.
If resources expire, report unresolved cells rather than substitute smaller n.

Retain exact configuration, command, environment, source snapshots/hashes,
per-run status and full output arrays in a new generated directory. No Git
index changes, maintained-code changes, or other-study scientific inputs.
Root owns protocol/driver/report; generic-route agent owns new integrator;
restricted-route agent checks implementation. Existing source core is frozen.
