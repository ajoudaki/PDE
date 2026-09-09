# Research state: three-hidden-layer two-step/one-step comparison

## Scope and non-circularity contract

This study concerns only the three-hidden-layer scalar-input mean-field network defined in PROOF.md. For each fixed nonzero step size, width tends to infinity first. Only after the fixed-step limit is identified do we study the small-step limit.

The target discrepancy is

\[
\Delta_{21}(\eta)=F_2(\eta)-F_1(2\eta).
\]

The desired theorem has activation-defined quantities

\[
\kappa_\phi,\qquad B_\phi<\infty,\qquad h_\phi>0
\]

such that

\[
|\Delta_{21}(\eta)-\kappa_\phi\eta^3|
\le B_\phi|\eta|^5,
\qquad |\eta|\le h_\phi.
\]

No constant may be defined through a trained output, a trajectory supremum, an unknown continuity modulus, or a finite-width Taylor/width-limit interchange.

## Proof obligations

1. Give the exact finite-width network and exact ascent updates.
2. Identify its one- and two-step fixed-step width limits by an explicit Gaussian operator DAG.
3. Prove the adaptive Gaussian conditioning result for both reused matrices, including cross-layer adaptive queries.
4. Prove concentration and uniform integrability for every empirical Gram, response coefficient, and output.
5. Establish explicit nonzero-step radii for all four singular two-time Gram matrices.
6. Build a finite Price-jet compiler directly on the width-first DAG and prove fifth-order activation-envelope bounds.
7. Compute the cubic coefficient as finite Gaussian activation integrals and prove the Euler/DAG intertwining identity used to simplify it.
8. Audit all parity cancellations and the final epsilon implication.

## Claim status

Complete for the quantitative theorem in PROOF.md, with the cubic
coefficient defined by the exact seven-call Price-jet recursion.  The
fixed-step two-matrix identification is proved in WIDTH_DAG.md, and the
rank and activation-envelope estimates are proved in RANK_REMAINDER.md.

The optional nine-moment simplification in CUBIC.md remains conditional on
a separate cylindrical population-intertwining theorem and is not used by
the quantitative result.
