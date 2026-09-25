# A sharper conditional bound for the response-speed clock

Theory clarification, 2026-09-25. Root owns this note. It concerns exactly
the finite two-hidden-layer tanh, finite-M, unscaled Euclidean-monitor,
weighted-Gram closure with continuous matching prefix in
RESPONSE_CLOCK_FULL_CLOSURE.md. It does not change the algorithm.

The unconditional O_T(P^-1) dense-trajectory theorem in
ORACLE_FINITE_HORIZON_BOUND.md is for the ORIGINAL activity clock.
The newer clock admits the following sharper conditional estimate.

## Projection comparison

Fix a regular time of the new closure with finite coordinate length L.
Its histories h_a,u_a have Euclidean derivative norm at most one in xi,
and are constant on [0,1]. The insertion measure obeys dmu<=dxi:
its density is one on the prefix and rho/g<=1 on actual history.

Let Pi_mu be orthogonal projection in L2(mu) onto degree<P polynomials,
and Q_P ordinary unweighted Legendre projection on [0,L]. Their polynomial
spaces coincide even though their orthogonality measures differ. For either
vector history f, best approximation and measure domination give

    ||f-Pi_mu f||_L2(mu)
       <= ||f-Q_P f||_L2(mu)
       <= ||f-Q_P f||_L2(dxi).

The unweighted derivative estimate, proved in the finite-horizon note, is

    ||f-Q_P f||_L2(dxi)^2
       <= [P(P+1)]^-1 integral_0^L xi(L-xi)||f'(xi)||_2^2 dxi
       <= L^2 ||f'||_L2(dxi)^2/[4P(P+1)].

The prefix derivative vanishes and ||f'||<=1 on the remaining interval.
Therefore for every integer P>=1,

    ||f-Pi_mu f||_L2(mu)
       <= L sqrt(L-1)/(2sqrt(P(P+1))).                 (1)

This does not assume that the Legendre basis is orthogonal in mu, or
apply an unweighted differential identity directly to the weighted
projection. Q_P is only an admissible comparator in the proof; no
additional solver state or historical evaluations are required.

## Accumulated matrix error and conditional tracking

Weighted orthogonality gives exactly

    J_a-S_a = integral (u_a-Pi_mu u_a)(h_a-Pi_mu h_a)^T dmu.

The continuous-prefix contribution C_a=u_a(0)h_a(0)^T is subtracted in
the physical reconstruction. Consequently the discrepancy R_P between
the reconstructed W2 and the exact accumulator of its OWN histories is

    R_P = (2/(nM))sum_a(J_a-S_a).

Cauchy--Schwarz and (1) imply

    ||R_P(t)||_F <= L_P(t)^2(L_P(t)-1)/[2n P(P+1)].     (2)

In particular, it is at most L_P(t)^3/[2n P(P+1)]. This is valid for
each regular finite trajectory segment. It vanishes at L=1. The earlier
Bernstein bound A_P L_P^2/[2n max(1,P-1)] remains valid and may be smaller
when L_P/A_P is large at a given P; either bound may be used.

If the closures exist regularly on [0,T] and L_P(t)<=L_T^* uniformly in
P,t, the common physical bounds and integral comparison in the
finite-horizon note give

    sup_(t<=T)||theta_hat_P(t)-theta_dense(t)||_*
       <= (L_T^*)^2(L_T^*-1) exp(K_T^* T)/[2n P(P+1)]. (3)

Here K_T^* is the physical vector-field Lipschitz constant for the common
bounded region, independent of P. Thus the new construction has a
conditional O_T(P^-2) tracking bound, improving the earlier conditional
O_T(P^-1) bound for that same construction.

Regular existence and the P-uniform clock-length bound are not established
here. A pointwise derivative cap is not a bound on accumulated length.
The L_P^3 factor, potentially long clocks, and numerical Gram conditioning
can offset an apparent rate advantage. No uniform all-time or practical
efficiency result follows. The original O_T(P^-1) theorem is an upper
bound, not a lower bound: the new estimate does not prove that the original
closure actually converges more slowly. The comparison also changes the
prefix treatment, so it does not isolate the benefit of clock adaptation.

## Check provenance

Inputs read by root: RESPONSE_CLOCK_FULL_CLOSURE.md sections 1--4,
SHA256 06560b5a53bbff5d0de7640ca2162f56d36ae25e7e57eb5b565505a951e8fa67;
and the already fully read ORACLE_FINITE_HORIZON_BOUND.md, SHA256
bfe32ba200b980f088846f5c9e902f08e6e740219368b6cbbfc19616029f16c1.

Root derived and checked (1)--(3). The existing scoped mathematical checker
oracle_original_bound independently checked a self-contained prompt giving
the measure domination, history regularity, prefix, polynomial comparator
and proposed estimates. Its complete response confirmed every displayed
constant for all M,P>=1 and the conditional tracking implication, with
the limitations stated above. It did not read this finished file; root
checked correspondence to that response. This is a bounded collaborative
mathematical check, not an independent promotion review. No numerical
experiment, code change, external-source retrieval or Git write occurred.
