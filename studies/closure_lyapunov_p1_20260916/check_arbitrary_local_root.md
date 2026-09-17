# Root internal check: arbitrary-pair initialization and small-label theorem

2026-09-16. Root read every section and equation (1)–(16) of the frozen
arbitrary_pair_local.md and recalculated the key inequalities. This is an
internal analytical check, not a fresh isolated review or promotion audit.
No experiment or formal machine verification was used.

Candidate SHA256: 4bdb878378518455ca4e0cf7ea2ded8281d056b7aec98cef36c5ebf337c47b9a
Canonical source SHA256: 81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c

Verdict: PASS for the stated arbitrary-orientation initialization rank and
small-label convergence theorem. No mathematical correction was required.

Checks performed:

1. Reconstructed the raw contraction (alpha*v,alpha*r+tau*chi), both ridge
   inverse factors and upper normalization. The scalar coefficient formula
   uses division by tau+eta, not its square root, because it multiplies the
   raw upper tanh(xi). Its representation through the correlated pair
   (g_i,g·u) uses correlation u_i and preserves the reverse mark response.
2. Verified tanh²x>=x²/(1+x²), then the displayed Cauchy-Schwarz calculation.
   It gives v>=1/4, tau>=v/(1+3v)>=1/7 and alpha<=6/7 with no numerics.
3. Checked Gaussian convolution upper bound through symmetric intervals,
   the paired sech² addition identity and the factorial/geometric-series
   bound for cosh(6/7)<=32/23. Hence q0=529/1024 is a valid lower ratio.
4. Checked the conditional Gaussian integration by parts and variance
   lower bound; subtracting r²/(v+eta) leaves a nonnegative conditional-mean
   remainder. The numerator of b is at most tau*chi+eta/chi because
   alpha*r/(v+eta)<=alpha²*v/(v+eta)<=1<=1/chi. Thus b<=1/chi.
5. With R_eta=v/(v+eta)>q0, the sign of the negative b coefficient in the
   derivative bound is handled correctly. Substitution gives precisely
   alpha*(2-1/q0)=34*alpha/529. This proves j'>0 without assuming that
   the first raw regression coefficient is nonnegative.
6. Recomputed the Gaussian interpolation derivative of varphi: the two
   tanh'' terms cancel. Bounded derivatives justify the integrations on
   interior correlation intervals, and dominated convergence extends the
   derivative formula to the endpoints. The event |G|,|Z|<=1 gives the
   claimed positive uniform lower derivative bound sigma0.
7. Strict coordinatewise monotonicity and the unit-norm constraint prove
   that two coefficient vectors are collinear only for equal or opposite
   inputs. Positive upper density and differentiation of any alleged hidden
   linear relation at its origin then prove exact full readout Gram rank.
   The least-eigenvalue formula includes the probability factor 1/2.
8. Repeated the first-exit calculation: feature-map change <=sqrt(5) times
   physical displacement, rho=sqrt(lambda)/(2sqrt(5)), and labels bounded
   by lambda/(8sqrt(5)) give total physical length <=rho/2. This preserves
   the evolving readout Gram and yields the stated exponents and topology.
   The original complete local proof supplies the explicit manifold graph,
   and the same derivative/rank argument applies at these arbitrary inputs.
9. Tested coordinate zeros, input coincidence, antipodality, small angle,
   labels of unequal small magnitudes, and the distinction between fixed
   mark coupling and ordinary joint-law Wasserstein distance. All scope
   qualifications in the candidate are necessary and correctly stated.

This result does not supply unit-label convergence for generic oriented
pairs. The all-antipodal small-label restriction in its frozen Section 6
is subsequently superseded by the separately proved scalar-margin theorem;
that does not invalidate the weaker statement originally proved here.
The initialized-rank result is unconditional over every nondegenerate pair,
but preservation of two-mode rank during large nonlinear unit-label motion
is not inferred from it.
