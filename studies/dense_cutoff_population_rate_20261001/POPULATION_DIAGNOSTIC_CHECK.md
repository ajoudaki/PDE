# Coordinator reconstruction of the population diagnostics

2026-10-03. Internal within-study reconstruction, not an independent
promotion review. The coordinator read every line of the two candidates
identified below, including their claim limitations. The negative
candidate was initially produced without access to the positive route;
the subsequent checks and source exchanges were collaborative.

## Frozen inputs and scope

- POPULATION_NEGATIVE_SEARCH.md:
  b138ab48bdccf280c217c2d513a0abfcc96e46c4be1ef35adc6fe9ce96700f43.
- POPULATION_DIRECT_COUPLING.md:
  145895536ea2e006ff444e2ca4eeb8b408ee1adf594dc317e9ea28a05936cb00;
  this report checks Sections 6–8. Its Sections 3–5 have the separate
  complete POPULATION_DIRECT_CHECK.
- The complete current manuscript and the finite concentration/tube
  dependencies had already been read in this investigation. The
  Gaussian population construction in paper/proof_alltime.tex was
  reread. Their versions agree with the negative candidate's table.
  No other study, archived book or numerical evidence was used.

**Verdict:** the exact diagnostic statements pass in their specified
scopes. Neither candidate proves a dense-to-population rate or a
slower canonical rate. The first-chaos identity is initially a
fixed-feature-space identity; its comparison across different source
realizations is not established in these frozen inputs.

## Negative-route reconstruction

The normalized dense equations match the manuscript: read-in and
readout mobility is \(n\), hidden-matrix mobility is one, and the
hidden update has the factor \(1/n\). At zero readout every hidden
velocity vanishes and \(\dot w=2\sum_a p_a y_a h_a\). Thus the
initial output velocity is the claimed initialized feature pairing.
Differentiating the backward chain once, then the hidden update once,
gives the stated second derivatives. Projecting off the initialized
span proves the \(t^2\) innovation and \(t^4\) squared-norm assertions.
The remainder is correctly restricted to fixed width.

For the Gaussian covariance map, differentiating the regularized
Gaussian density gives one half of its covariance increment contracted
with the Hessian of the test. For
\(\phi(z_a)\phi(z_b)\), that Hessian has at most linear growth under
the supplied derivative bounds. Uniform Gaussian moments justify
integration and removal of the regularization. This proves
Lipschitz continuity even at a singular covariance. Conditional
independence of initialized rows then gives the stated root-width
induction, including a fixed appended test list. It does not apply
that independence to trained rows.

If a population feature relation has zero second moment, continuity
and full Gaussian support make it an identity on the preactivation
support. The inductive range inclusion for the finite covariance
places every finite row in that support. Taking a finite kernel
basis proves simultaneous null-relation preservation. This is
initialization-specific; there is no asserted trained rank theorem.

For the cutoff of \(s_+^{3+\beta}\), rescaling \(s=\sqrt v Z\)
gives the exponent \((3+\beta-j)/2\) for derivative order \(j\).
Cutoff derivative terms occur outside a fixed neighborhood of zero
and are exponentially small in \(1/v\). The function is \(C^3\)
with bounded first three derivatives, while the \(j=2,3\)
covariance maps have non-Lipschitz powers. The source explicitly
does not embed this observable as an uncancelled trained prediction
term. Its zero-marginal attempted embedding is correctly rejected:
a nondegenerate Gaussian and a continuous nonzero activation have
positive activation second moment.

The fixed-gap residual inequality follows by differentiating the
weighted squared residual norm. Integrating the supplied exponentially
decaying prediction speed proves the logarithmic-horizon reduction,
with the time supremum inside the query integral and the envelope
\(1+\|x\|/\sqrt d\). The heavy-tail abstract construction satisfies
the finite-second-moment condition, but is correctly labeled
non-neural. The same-width state Lipschitz estimate retains exactly
that linear query envelope. The Gaussian tail calculation for a
probability-\(1/n\) rare coordinate gives \(O(\log n/n)\), which
cannot supply the requested polynomially larger error by itself.

Finally, choose the confidence failure of finite-center concentration
below half the positive probability of a putative lower-bound event.
The two events intersect for large width. The triangle inequality
then forces the deterministic center displacement stated in the
candidate. The reverse implication uses the same triangle inequality.
This verifies the restriction on a possible counterexample without
assuming a quantitative population limit.

## First-chaos and singular-step reconstruction

Equality of source and physical-feature Gram matrices makes the map
from each Gaussian source to its feature a well-defined isometry of
their finite spans. Pairing the Gaussian integration-by-parts identity
with every source gives the orthogonal projection of the scalar
observable onto that Gaussian span. This proves the represented
response identity and its norm contraction, including null Gram
directions. Extra independent variables can be integrated out before
this calculation. No pseudoinverse continuity is invoked.

In the first Euler step, hidden weights stay fixed and the updated
backward signal is \(2\eta y\phi(\xi_0)\phi'(\xi_1)\).
At the repeated source, the two response derivatives sum to
\((\phi')^2+\phi\phi''\). One-dimensional integration by parts turns
its Gaussian expectation into
\(q^{-1}\mathbb E[G_q\phi(G_q)\phi'(G_q)]\).
The density derivative is integrable on every fixed
\(0<c\le q\le C\), so this coefficient is covariance-Lipschitz
without a fourth activation derivative.

For the added orthogonal direction,
\(\xi_1=G_q+\epsilon g\), integration by parts in \(G_q\) gives
the same combined coefficient. Taylor expansion of \(\phi'\)
uses only bounded \(\phi'''\); its linear term integrates to zero
over the independent centered \(g\). The change is \(O(\epsilon^2)\).
The new orthogonal physical vector has length \(|\epsilon|\) and
a bounded coefficient. This verifies the stated rank-change test,
not a global history-stability theorem.

The covariance calculation in the final section of the direct note
uses weighted Cauchy--Schwarz in an arbitrary positive matrix \(K\),
then the covariance identity. It does not assume a common eigenbasis
for \(K\) and the covariance. The complete auxiliary Gaussian
coupling theorem has its own source and reconstruction in
POPULATION_COVARIANCE_CHECK.

No source was changed by this check. No simulation, numerical
rate fit, formal proof assistant or Git write was used.
