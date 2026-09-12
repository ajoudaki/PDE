# Finite normalization correction and internal check for v3

The original v1 integration report is preserved intact. Its N1 objection is
valid: under the explicit ordinary-Euclidean finite norm convention, tails
need a 1/sqrt(n) factor to converge to population L2 tails. The raw metric
and theorem observable already had their factors, but D.2's displayed tail
comparison and finite rank/hidden counterparts did not make them consistent.

Coordinator /root corrected D.2 in the complete v3 candidate. It now defines
finite RMS hard and soft tails, uses those norms in the cutoff inequality
and raw-distance comparison, displays ||ab^T/n||_F and the finite hidden
1/sqrt(n) bound, and normalizes first-row/readout input constants. Fixed-program
convergence is stated for continuous soft tails; hard tails are bounded by
twice the soft tail at half the cutoff. This avoids assuming convergence at
a discontinuous hard threshold. Population identities are unchanged.

Direct verification: for q=2*ones(n), R=1, the finite hard RMS tail is 2;
for a=b=ones(n), ||ab^T/n||_F=1; for any q, pointwise
|q|*1_{|q|>R} <= 2*(|q|-R/2)_+. These equalities/inequality prove the
normalizations and hard/soft bridge for every width. Splitting changed-gate
products at R and dividing each Euclidean term by sqrt(n) proves the
displayed finite product bound. Cauchy–Schwarz with c/n and two RMS factors
proves the scalar prediction bound; bounded tanh derivatives prove the
finite hidden bound. No new conditioning, horizon or constant premise enters.

The pairwise-distinct correction from v2 is retained. No theorem, law family,
episode, margin, initialization or limit order changes. Previous packets and
all original reports remain unchanged. Two fresh complete v3 mathematical
reviews and a fresh v3 integration review are required. The v2 review still
in progress remains attached only to its own frozen inputs.

Candidate v3 SHA-256: `c858c7b41d90b490871450b8bf7494afe8c6cd7f39bebd3f1faa89f3604a5879`.
