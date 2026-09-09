# Orthogonally invariant SK theorem: limited applicability check

Checked 2026-09-05 against the primary HTML of Fan, Misiakiewicz, Wang,
and Wen, arXiv:2607.10102v1, Sections 2.1 and introductory proof discussion:
https://arxiv.org/html/2607.10102v1 .
This is not a complete paper audit.

Theorem 2.4 proves an all-fixed-time empirical path limit for
d theta = [f(theta)+X theta] dt + sqrt(2 gamma) db.
Assumption 2.1 makes X a fixed symmetric orthogonally invariant random
matrix with bounded operator norm and a limiting spectral law.
Assumption 2.2 requires a fixed scalar coordinatewise f with bounded
first three derivatives and independent initialization. Zero noise is
explicitly allowed.

This theorem does not directly cover the canonical three-hidden-layer
network. Its two reused initial matrices can be placed in a symmetric
block array, but the resulting trained, composed forward/backward drift
is not a fixed scalar coordinate map plus one fixed linear matrix action.
Nor does such a block array have the asserted full orthogonal invariance.
The response equation (2.3) uses the bounded scalar f' hypothesis; it
does not supply the target's unbounded middle-multiplier estimate.

No global theorem upgrade follows. These are specific unmet premises,
not a claim that adapting the proof is impossible or that no other
published theorem could apply.
