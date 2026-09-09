# Tame-gate H2 hostile audit 01

**Provenance:** clean-room referee agent; it was given a self-contained
statement and proof skeleton, was forbidden to inspect the repository or
communicate with other agents, and returned an independent reconstruction.

**Date:** 2026-08-24  
**Verdict on the submitted first draft:** reject as written, but repairable;
no arctangent-specific obstruction was found for the integer family
\(\phi_m(x)=\int_0^x(1+u^{2m})^{-1}du\).

## Accepted modules

The auditor independently verified:

1. the natural-coordinate identities
   \(r'=Q\), \(\psi'=c^2\), and the three-term formula for \(K\);
2. the mixed vector/Frobenius scaling and the trace norm of the rank-one
   matrix velocity;
3. fixed-mesh elimination of the trained matrix into one finite two-sided
   Tensor Program;
4. the Gaussian-multiplier Osgood modulus
   \(\delta\sqrt{\log(e/\delta)}\), without an independence assumption;
5. the fixed-mesh fourth-moment-to-uniform-square-integrability argument,
   provided the deterministic Euler comparison controls all intermediate
   times; and
6. the complete integer activation family, including
   \(\Theta_m(x)=x+x^{2m+1}/(2m+1)\).  For \(m=1\), the auditor emphasized
   that \(\iota=\Theta^{-1}\), not \(\tan\).

## Fatal defect in the first draft

The map

\[
 (A,Z)\longmapsto A\,d(Z)
\]

is not locally Lipschitz from \(L^2\times L^2\) to \(L^2\), even for
\(d(z)=(1+z^2)^{-1}\).  If \(E_\varepsilon\) has measure
\(\varepsilon\), take

\[
 A_\varepsilon=\varepsilon^{-1/4}{\bf1}_{E_\varepsilon},
 \qquad Z_\varepsilon={\bf1}_{E_\varepsilon}.
\]

Both inputs approach zero in \(L^2\), but the ratio of the output
difference to \(\|Z_\varepsilon\|_2\) grows as
\(\tfrac12\varepsilon^{-1/4}\).  Saying that each multiplier is
individually bounded does not supply one common \(L^\infty\) envelope.

## Mandatory repair adopted by the theorem

For a level-\(M\) initial mark and a fixed slab \([-S,S]\), the repaired
proof saturates the **current** \(A\) only inside \(B=A d(Z)\), at a level
strictly larger than \(M+\|\phi\|_\infty S\).  This defines a genuinely
locally Lipschitz ambient \(L^2\oplus L^2\oplus\mathfrak S_1\) field.  The
pointwise identity

\[
 |A(s)-a_0|\le \|\phi\|_\infty |s|
\]

then proves that the auxiliary saturation is inactive on that slab.  This
is an invariant-envelope construction, not a claim of ambient Hilbert
local Lipschitzness for the original field.

## Other audit requirements incorporated

- Tensor Programs III is invoked only at fixed program length.  Coordinate
  maps and tests must be pseudo-Lipschitz jointly in all coordinate and
  random scalar arguments.
- The simultaneous event is only over a declared countable language:
  rational meshes and coefficients and integer cutoffs/saturations.
- The limit source must retain probability-algebra operations, not merely
  Hilbert pairings, because coordinate products and Nemytskii maps occur in
  the IDE.
- Uniqueness is asserted in the marked class
  \(A-a_0\in L^\infty_{\rm loc}\), and restart retains that mark.
- The cutoff comparison exponent must grow only linearly in \(M\); a
  quadratic exponential is not defeated by the Gaussian clipping tail.
- Finite-width and limiting Euler errors are proved separately.  Fixed
  Euler program observables, rather than a cross-width state norm, bridge
  the two spaces.
- Raw-square transfer uses a Lipschitz saturation of \(Q\), and the
  fourth-moment bound is converted to uniform integrability in the order:
  choose the mesh error, then the tail level.  The fixed-mesh fourth-moment
  constant may diverge as the mesh is refined.
- Cutoff removal precedes the final unbounded-square passage and uses an
  explicit epsilon order; no width-dependent diagonal choice of cutoff,
  mesh, or saturation is inferred from the fixed-program theorem.
- The target, learning rate, residual, and scalar clock are explicit, with
  \(\eta\ge0\) and the exact finite initialization
  \(e_n(0)=y_\star-f_n(0)\).
- The reciprocal-polynomial family is indexed by integer \(m\ge1\).  A
  real-parameter version would require absolute powers.

## Disposition

All identified repairs were inserted into
arctan_l2/TAME_NATURAL_GATE_H2_THEOREM.md.  That document remains a
repaired candidate until a second isolated referee verifies that the
repairs close the proof rather than merely move the gaps.
