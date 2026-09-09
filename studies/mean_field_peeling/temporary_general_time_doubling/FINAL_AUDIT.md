# Final independent audit

## Certified theorem

For every fixed integer \(t\ge1\), with the width limit taken at each fixed
step size before the learning-rate limit,

\[
D_t(\eta)=F_t(2\eta)-F_{2t}(\eta)
\]

satisfies

\[
\left|D_t(\eta)-\kappa_{\phi,t}\eta^3\right|
\le B_{\phi,t}|\eta|^5,
\qquad |\eta|\le\frac12,
\]

where

\[
\kappa_{\phi,t}=-\frac{t(2t-1)}2J_\phi,
\qquad
B_{\phi,t}
=\frac{32\overline{\mathcal J}_{t,5}
+\overline{\mathcal J}_{2t,5}}{120}.
\]

The activation integral \(J_\phi\) and the terminating compiler defining
\(\overline{\mathcal J}_{N,5}\) are given in PROOF.md.  Neither constant
is defined from an output supremum, a trained-trajectory modulus, or a
limit whose regularity is assumed.

## Proof dependencies audited

1. **Exact network and fixed-step identification.**
   PROOF.md, Sections 2--4, and FIXED_H_IDENTIFICATION.md prove the
   finite-width normalization, strict population rank for every
   \(h\ne0\), predictable alternating \(W/W^T\) conditioning, and every
   response cancellation.  The dependence of \(H^1\) on the reused
   \(D^0\) action is included.
2. **Concentration and uniform integrability.**
   WIDTH_CONCENTRATION_CLOSURE.md gives one raw/extended/ideal coupling,
   the \(6N+4\) micro-ledger, the explicit moment tower
   \(R_0=8^{6N+4}r_*\), \(O(n^{-m})\) first-failure bounds, stopping
   removal, Gram/cross-moment uniform integrability, and terminal uniform
   integrability.
3. **Singular covariance and activation order.**
   REGULARITY_SUPPLEMENT.md proves fivefold inverse-free Price
   differentiation using Fourier inversion, isotropic domination,
   cutoff--mollification, uniform Gaussian tails, and successive FTC
   closure.  Its structural count
   \(2r+j+|\alpha|\le10\), added to response base order \(2\), proves that
   \(C^{12}\) is sufficient.
4. **Arbitrary-time cubic coefficient.**
   CUBIC_JET_COMPLETE_LEDGER.md displays every lower response atom,
   terminal atom, covariance Price term, finite sum, and final coefficient
   grouping, proving
   \[
   F_N'''(0)
   =\frac{N(4N^2-3N+1)}2S_\phi
    +2N(N-1)(2N-1)H_\phi.
   \]
5. **Taylor remainder.**
   Only after the preceding width-first identification and \(C^5\)
   regularity are established, PROOF.md, Section 8, applies the integral
   Taylor formula.  The factor \(32=2^5\), the divisor \(120\), all three
   concrete coefficients, and their common radii were independently
   recomputed.

## Independent audit outcomes

Five separate hostile audits checked:

- exact finite-width scaling, rank, predictability, and response algebra;
- the concentration coupling, moment tower, stopping exponents, and
  uniform integrability;
- singular-covariance regularity and the \(C^{12}\) derivative budget;
- every arbitrary-\(N\) cubic recurrence and coefficient;
- final theorem assembly, signs, radii, and activation-only constants.

Each audit returned an unconditional pass after its identified presentation
issues were repaired.  The repaired issues included isotropic Fourier
domination, explicit conditional-law notation and innovation scales, an
explicit column-conditioning step, the global extended-action split, a
self-contained Gaussian operator-norm moment bound, the constant-activation
branch, and the explicit conditional operator constant in Section 9.

## Claim boundary

The fixed-\(t\) theorem and one shared constant over every fixed finite
horizon are proved.  A single all-\(t\) actual-network estimate

\[
C_\phi t^4|\eta|^5,\qquad |\eta|\le c_\phi/t,
\]

still requires the autonomous uniformly \(C^5\) population-operator
representation stated in Section 9 and remains open for this network.
A quadratic \(t^2|\eta|^5\) remainder is false; the identity activation
has a nonzero quartic-in-\(t\) fifth coefficient.
