# Precommitted equilateral diagnostic

Date 2026-09-18; no results inspected before this plan. The user authorizes
small targeted reproducible diagnostics. This is a diagnostic of the exact
p=1 equations' population discretization, not a theorem about population
convergence or a computer-assisted proof.

Question: do representative members of the specified equilateral rotation
family fit under the full p=1 dynamics, and is that observation resolved under
population quadrature refinement? A failure to reach the threshold does not
prove permanent failure. A success does not prove all rotations succeed.

Use exactly the active Cholesky p=1 coefficient formulas of
docs/observable_p1.md, all four lower and both upper marks, full evolving 2x4
M, original physical time, weights (3/8,1/8,1/2), labels (+,+,-), and rotations
0, pi/12, pi/6. No initialization fit or frozen hidden block. Constants use
positive Gaussian-weighted Legendre rules on [-10,10], orders 128 and 256;
use 256 and require coefficient differences <=1e-9 for numerical validity.
Discarded scalar Gaussian mass is <2e-23; this alone is not a complete
derived-coefficient error bound.

Population integration uses tensor Gauss-Hermite rules with 8,12,16 nodes
per independent Gaussian coordinate: four lower, two upper. Independent
population integrations preserve the complete lower correlations. Evolve
with float64 DOP853, rtol=2e-7, atol=2e-9, through T=120; sample at
t=0,1,2,5,10,20,40,80,120. Do not stop early on apparent success, so
refinements compare identical horizons. Retain losses, predictions, upper
code vectors M a_i, readout norm, matrix norm, readout-Gram eigenvalues,
energy-dissipation values, and paired hidden displacement at these times.
One precommitted tighter-solver repeat uses q=12,theta=pi/12,
rtol=2e-9,atol=2e-11. No extra angles, horizons or refinement branches.

Validity gates: all outputs finite; sampled loss increases <=1e-7; the
tighter-solver repeat changes each prediction by <=2e-5 and each code vector
by <=2e-4 at common times. For an angle to count as empirically resolved
fitting, both q=12 and q=16 must have final loss <=1e-6, predictions differ
by <=2e-4 at every common time, and upper code vectors differ by <=2e-3 at
every common time. Other cases are explicitly unresolved, even if one grid
has tiny loss. Report actual differences and threshold attainment; do not
interpret numerical monotonicity as a Lyapunov proof.

Resource cap: one CPU thread, 120 seconds wall time for the whole campaign,
maximum ten solves, at most 16^4 lower nodes and 16^2 upper nodes, no GPU.
Stop at the cap, preserving completed/partial outputs as interrupted; do not
expand the campaign. Store source and plan hashes, exact command, versions,
precision, coefficients, run status and artifacts under a fresh directory
data/generated/p1_three_input_geometry_20260918/equilateral_01/.
The producer remains in this flat study. No maintained code API is used.
