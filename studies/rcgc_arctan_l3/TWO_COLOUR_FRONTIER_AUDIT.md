# Depth-three two-colour frontier audit

**Provenance:** isolated clean-room obstruction-reconciliation agent; no
repository access and no communication with other agents.  The agent was
given only the candidate nested word, the two proposed closure semantics,
and the requested claim-level tests.

**Date:** 2026-08-24  
**Verdict:** the nested word is correct and generically order one, but its
nonvanishing does not prove that an independent traffic operator is
necessary.  Conversely, a finite first/second-response bound by itself does
not prove that the word hierarchy closes.

## Exact Jacobian component

For \(\phi=\arctan\), let

\[
 D_j=\operatorname{Diag}(\phi'(h_j)),\qquad
 E_3=\operatorname{Diag}(A\phi''(h_3)).
\]

The top-curvature branch of the derivative of the bottom backward field is

\[
 N_n=D_1G_2^{0*}D_2G_3^{0*}E_3G_3^0D_2G_2^0D_1.       \tag{1}
\]

Thus the compiler orientation word \(2^-3^-3^+2^+\) is correct.  This is a
component of the **first** Jacobian, not the second Fréchet derivative.
There are also local-curvature, learned-matrix, endpoint, and strict-time
branches.

Put \(B=G_3^0D_2G_2^0D_1\), so \(N_n=B^*E_3B\).  Conditional on the
forward fields and with independent centered endpoint coordinates of
variance \(\sigma_A^2\),

\[
 \mathbb E_A\!\left[\frac1n\operatorname{Tr}N_n^2
 \mathrel{\big|}B,h_3\right]
 =\frac{\sigma_A^2}{n}\sum_{k=1}^n
   \phi''(h_{3,k})^2\|B_{k\cdot}\|_2^4.               \tag{2}
\]

For a nondegenerate order-one initialization, the right side is positive
and order one.  Meanwhile the normalized trace itself is centered and has
conditional variance of order \(n^{-1}\).  Hence scalar centering does not
license discarding the glued Hilbert--Schmidt statistic.  Nonvanishing at
initialization still depends on a nondegenerate endpoint/forward law; for
example \(A=0\) or \(h_3=0\) makes this particular branch vanish.

## What the calculation proves

- The word is a genuine degree-zero object in the normalized
  Hilbert--Schmidt scale.
- It cannot be charged as an \(o(1)\) defect solely because its normalized
  trace centers.
- A two-copy covariance of first tangent fields captures its first gluing,
  because an independent isotropic probe \(\xi\) satisfies
  \(\mathbb E_\xi n^{-1}\|N_n\xi\|^2
    =n^{-1}\operatorname{Tr}(N_n^*N_n)\).

## What it does not prove

- It does not show that \(N_n\) must be stored as a new current operator;
  at finite width it is derived from the current fields and frozen actions.
- It does not show that a finite scalar second susceptibility determines
  every mixed word
  \(n^{-1}\operatorname{Tr}(N_nM_1N_nM_2\cdots)\).
- It does not decide whether a complete two-time response propagator
  implicitly closes those words.  That is a closure theorem, not a formal
  consequence of (1).

Bare covariance/first-response data are insufficient in general.  If
\(X\sim N(0,1)\), then

\[
 e=(X^2-1)/\sqrt2,qquad
 \widetilde e=(X^3-3X)/\sqrt6
\]

have the same mean, variance, covariance with \(X\), and mean first source
response, but \(\mathbb E e^4=15\) and
\(\mathbb E\widetilde e^4=93\).  Corresponding fourth mixed traces through
an independent Ginibre action distinguish them.  This refutes a universal
pairwise covariance/first-response closure, though it is not a
counterexample internal to the arctangent flow.

## Exact remaining theorem

The smallest honest response-side target is a **mesh-uniform second-order
reduction and Euler-stability theorem for the finite raw-observable list**.
It must establish:

1. every required raw observable, including the gluing in (2), is uniformly
   reducible up to \(o(1)\) to empirical expressions of degree at most four
   in the state and its first two typed variations;
2. those fields have a uniform \(L^p\) envelope for some \(p>4\), plus a
   uniform time modulus; and
3. aligned Euler states and their first two variations are uniformly Cauchy
   across refining meshes, with uniform integrability of the finite raw
   list.

The condition \(p>4\) is sufficient for uniform integrability **after** the
degree-four reduction has been proved.  It does not itself prove that
reduction, cross-mesh consistency, limit identification, or uniqueness.
If a required observable differentiates to a genuine third response, first
and second variation bounds do not control it.

## Frontier decision

The response backend is the smaller plausible next machinery, while a full
all-word traffic theorem is conservative and may be unnecessarily strong.
Neither is yet proved.  The calculus must therefore register (1) as a
non-negligible frontier witness without promoting it to a mandatory new
final-state variable or claiming that second response already closes it.
