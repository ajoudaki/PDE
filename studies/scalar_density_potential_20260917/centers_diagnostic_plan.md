# Center/scatter and full-metric candidate diagnostic, precommitment

Question: does including the exact first-layer and connector response in the
inverse tangent Gram repair a sign failure of the inverse readout Gram on
a genuinely independent three-input trajectory? Neither candidate is assumed
to be a theorem. A negative sampled derivative is not proof of monotonicity.

Keep the exact scalar initialization and full physical characteristic flow.
Use input angles (60,126,99) degrees, labels (+,+,-), weights
(3/8,1/8,1/2). All three initial absolute projections on the frozen probe
are nonzero and distinct; there is no antipodal pair or reflection reduction.
The negative input lies between the positives on the short arc. This retains
the independent within-positive-class constraint that the pair lacked.

Compare on the same moving state: Phi_read=R^T G^{-1}R and
Phi_full=R^T Theta^{-1}R, where R_i=sqrt(p_i)(f_i-y_i), G is the weighted
readout Gram, and Theta contains the readout, M and w derivative blocks.
Differentiate both metrics analytically along the exact vector field.
Primary observable: Phi_dot/Phi. Full metric derivative must include
a_dot,d_dot,M_dot and the lower derivative-Gram velocity.

Use deterministic product Gauss--Hermite rules with 24,32,48 nodes per
Gaussian coordinate, separate upper grid at the same node count. Constants
nu,tau use 128 nodes. DOP853 rtol=2e-8, atol=2e-10, integrate to physical
time 200 or loss 1e-10. Sample 600 logarithmically spaced positive times
plus zero. One BLAS/OpenMP thread, at most 30000 RHS calls per resolution,
90 seconds total external wall cap and 85-second internal cutoff. No
additional datasets, grids, or time horizons after inspecting results.

A candidate sign failure is empirically supported only if positive log slope
exceeds 1e-4 with L>1e-8 and candidate Gram condition number below 1e10 at
both finer grids; positive peaks must agree within 20% relative to their
larger value, and occur within 10% of the larger peak time (or within 0.02
physical time for peaks earlier than 0.2). Otherwise the sign evidence is
inconclusive. Validate the initial identities Phi_dot=-4L, the physical
energy identity, and one central finite-difference check of each analytic
metric velocity at a retained interior state (relative tolerance 1e-4).
These are semidiscrete checks, not bounds on population quadrature error.

If a sign failure passes these criteria, one extra repeat of the 48-node
run at rtol=2e-9, atol=2e-11 is authorized only within the same cumulative
wall cap. Its peak must meet the same comparison bounds. No other branch.
Stop after the declared grids/optional repeat or the resource cap.

Save source/configuration, complete sampled scalar diagnostics, source
hash and package versions; retain failures. Generated products belong in
data/generated/scalar_density_potential_20260917/centers_check_20260918_01/.
The only claim upgraded by a valid positive sign is evidence against that
specific candidate, not nonexistence of a different potential. No valid
positive sign leaves the global monotonicity question unresolved.
