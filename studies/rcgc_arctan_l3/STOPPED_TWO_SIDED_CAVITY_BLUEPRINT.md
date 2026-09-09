# Stopped two-sided cavity blueprint

**Provenance:** isolated clean-slate machinery designer; it was given only
the exact D3 model, the fixed-grid fact, and the no-history final-state
contract. It had no project access and no communication with other agents.

**Date:** 2026-08-24  
**Claim level:** constructive design evidence, not a theorem; rejected as
written by a subsequent hostile audit. See
[the audit](STOPPED_CAVITY_HOSTILE_AUDIT.md) for the narrower restartable
\(\psi_1\) target.

## Proposed master certificate

The design independently selected the same missing object exposed by the
direct calculus execution: a mesh-uniform quantitative tail for the middle
backward action. It proposed the stronger stopped moment statement

\[
 \limsup_{n\to\infty}\max_Y
 \left(\mathbb E\frac1n\sum_i\sup_{t\le T}|Y_i(t)|^p\right)^{1/p}
 \le C_T\sqrt p,                                      \tag{M}
\]

for every fixed \(p<\infty\), uniformly over the exact flow and every Euler
mesh, with \(Y\) ranging over the forward/backward fields. A
subexponential \(C_Tp\) bound would already give the borderline Osgood
modulus; the sub-Gaussian \(C_T\sqrt p\) claim is stronger than necessary.

If (M), or a suitable subexponential replacement, is proved, quantitative
tail splitting yields

\[
 \|q d(z)-\widetilde qd(\widetilde z)\|_2
 \le \|q-\widetilde q\|_2
 +C d_0\sqrt{\log(C/d_0)},qquad d_0=\|z-\widetilde z\|_2,
\]

and Bihari--Osgood supplies the deterministic exact/Euler stability missing
from the promoted calculus.

## Proposed spatial cavity mechanism

For one deleted Gaussian row \(a\), write the exact identity

\[
 (G^0x)_a=\frac1{\sqrt n}\sum_jg_{aj}x_j^{(a)}
 +\frac1{\sqrt n}\sum_jg_{aj}(x_j-x_j^{(a)}).         \tag{1}
\]

The first term is an exact conditional Gaussian path. The second term is
expanded through the exact continuous-time first variation, not a finite
time Taylor jet. After stopping all relevant coordinates at
\(L_n=L\sqrt{\log n}\), the design proposes:

1. row/column cavity influence \(n^{-1/2+o(1)}\) in bulk state norm;
2. a remainder \(n^{-1+o(1)}\) after subtracting the exact first variation;
3. a return quadratic form
   \(n^{-1}g_a^*\mathcal R_x^{(a)}g_a\), whose conditional mean is the
   normalized response trace and whose conditional variance is controlled
   by \(2n^{-2}\|\operatorname{sym}\mathcal R_x^{(a)}\|_{HS}^2\);
4. row/column Efron--Stein self-averaging of normalized covariance and
   response traces;
5. exact-time Duhamel/Neumann summation with the time-simplex factorial,
   so response depth does not create a constant exponential in the number of
   mesh lines; and
6. a bootstrap showing that the stopped fields remain strictly below
   \(L_n\), allowing removal of the stop.

The two-colour word

\[
 D_1G_2^*D_2G_3^*E_3G_3D_2G_2D_1
\]

is retained in the response trace rather than declared negligible.

## Why this is a meaningful direction

Unlike the rejected global augmented-state Cauchy theorem, these proposed
estimates are spatial, local to one independent Gaussian row/column, and do
not assume a mesh limit. If established, the remaining passage is a
deterministic Osgood argument followed by the already proved fixed-grid
semantics. The response chart disappears from the final current
Gaussian-action/trace-class IDE.

## Unproved and potentially fatal leaves

The blueprint has not proved (M). In particular, the following claims may
still hide an uncontrolled response hierarchy:

- that the stopped first/second variation equations close under alternating
  \(G_2,G_2^*,G_3,G_3^*\) reuse;
- that resampling one row/column changes every normalized response trace by
  \(n^{-1+o(1)}\), rather than merely changing the primary orbit by
  \(n^{-1/2+o(1)}\);
- that the trace self-averaging remainder carries the time-step or spatial
  normalization needed for summability;
- that stop removal does not assume the very uniform tail bound it is meant
  to prove; and
- that a finite response order suffices after high-moment estimates are
  differentiated.

For this reason the blueprint is recorded as the leading constructible
program, not as a conditional proof or a passed calculus rule. A separate
hostile audit is required before even this program-level recommendation is
promoted.
