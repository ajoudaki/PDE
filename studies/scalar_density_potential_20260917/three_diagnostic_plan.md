# Targeted diagnostic precommitment, 2026-09-18

Question: does the minimum-readout-correction potential already fail to be
monotone on the symmetric, nonredundant three-input family, or does a trajectory
suggest a useful sign mechanism beyond the disproved positive-error cone?

Use only the declared scalar closure and exact initialization constants from
one-dimensional Gaussian quadrature. Set delta=1/2; inputs are
sqrt(2)(delta,+sqrt(1-delta^2)), sqrt(2)(delta,-sqrt(1-delta^2)) with labels +1
and weights 1/4 each, and -sqrt(2)e1 with label -1 and weight 1/2. This law
has two independent feature/label constraints after its preserved symmetry.

Deterministic product Gauss--Hermite population rules at 16,24,32 nodes per
lower Gaussian coordinate and the same upper scalar node count. Constants
nu,tau use 128 nodes, with a 192-node comparison. Integrate the full three-input
characteristic equations, not a frozen kernel, and differentiate the two-mode
potential analytically using the state velocity. Use DOP853 at rtol=2e-8,
atol=2e-10. Stop each run at loss 1e-10 or physical time 1000, whichever occurs
first. Cap RHS evaluations at 30000 per run and total process wall time at
90 seconds, one BLAS thread, no parallel training jobs. Run no additional
configurations without a new recorded discriminating question.

Check the initial slope Phi_dot=-4 L0 and the exact semidiscrete energy
identity. Record conditioning of the 2 by 2 activation Gram. A numerical
counterexample candidate requires a positive logarithmic slope above 1e-4
while loss is above 1e-8 and Gram condition number below 1e10, present at
both finer resolutions with differences below 20% of the positive peak
(or a conservatively explained comparable criterion). Otherwise results
are inconclusive about a sign change. A positive sign is empirical evidence
for the exact population, not a proof; failure to see a positive sign is
not proof of monotonicity or exponential convergence.

Also record loss, readout norm, M, two residuals, two feature amplitudes,
potential, derivative and quadrature comparisons. Failure of refinement,
resource caps or numerical conditioning remains explicitly inconclusive.
Generated products go to a fresh data/generated/scalar_density_potential_20260917/
run directory. Source and configuration stay in this flat study. No network
comparison, broad parameter sweep or Monte Carlo simulation is authorized.
