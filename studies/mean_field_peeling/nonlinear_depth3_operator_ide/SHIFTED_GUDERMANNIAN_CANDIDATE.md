# Shifted Gudermannian depth-three candidate

Status: exact C0--C1 contract and activation-comparison candidate; no
continuous-width theorem is claimed.

## Activation and bounded coordinates

Fix

\[
 \phi(z)=c+\epsilon\operatorname{gd}(z),\qquad
 \operatorname{gd}(z)=\arctan(\sinh z),
 \qquad c>{\pi\epsilon\over2}>0.
\]

For \(Z_1=u\), define

\[
 \vartheta_j=\operatorname{gd}(Z_j),\qquad
 d_j=\cos\vartheta_j=\operatorname{sech}Z_j,
 \qquad X_j=c+\epsilon\vartheta_j.
\]

Then \(|\vartheta_j|<\pi/2\), \(d_j>0\), and
\(\phi'(Z_j)=\epsilon d_j\).  With the frozen architecture and normalized
outer-product convention, put

\[
 B_3=\epsilon d_3A,\quad R_2=G_2^*B_3,
 \quad B_2=\epsilon d_2R_2,\quad Q_1=G_1^*B_2.
\]

## Exact activated-coordinate equations

Let \(a_j=\langle X_j^2\rangle_n\).  Feature ascent obeys

\[
\begin{aligned}
 A'&=X_3,\\
 G_2'&=B_3\otimes X_2,\\
 G_1'&=B_2\otimes X_1,\\
 \vartheta_1'&=\epsilon d_1^2Q_1,\\
 \vartheta_2'&=\epsilon a_1d_2^2R_2
     +\epsilon^2d_2G_1(d_1^2Q_1),\\
 \vartheta_3'&=\epsilon a_2d_3^2A
     +\epsilon d_3G_2\vartheta_2'.
\end{aligned}                                                    \tag{1}
\]

The last two identities follow from

\[
 Z_2'=a_1B_2+\epsilon^2G_1(d_1^2Q_1),
 \qquad
 Z_3'=a_2B_3+\epsilon G_2\vartheta_2'
\]

and \(\operatorname{gd}'(z)=\operatorname{sech}z\).

The predictor and raw tangent kernel are

\[
 f=\langle A,X_3\rangle_n,
\]

\[
 K=a_3+\|B_3\|_n^2a_2+\|B_2\|_n^2a_1
      +\|\epsilon d_1Q_1\|_n^2,
 \qquad f'=K.                                      \tag{2}
\]

Equations (1)--(2) are a fixed-species, current-time lift.  A minimal
operator state can retain only

\[
 (A,\vartheta_1,P_1,P_2,e;\Gamma_1,\Gamma_2),
 \qquad G_j=\Gamma_j+P_j,
\]

because \(\vartheta_2,\vartheta_3\) are reconstructed from the current
forward pass.  Keeping all three bounded \(\vartheta_j\)'s is an equivalent
redundant differential-algebraic realization.

## Finite clock and local characteristic

The feature floor

\[
 m=c-\pi\epsilon/2>0
\]

gives \(K\ge m^2\).  In physical MSE time,

\[
 \int_0^\infty 2\eta|e(t)|\,dt\le {|e(0)|\over m^2}.
\]

Thus \(A\) is a Gaussian initialization plus a bounded coordinatewise
shift, and the learned operators have bounded trace-norm variation.

The direct local activated-coordinate equation has an exact polynomial
characteristic.  If

\[
 \vartheta'=\epsilon a(s)C(s)\cos^2\vartheta
\]

with \(a,C\) prescribed, then \(r=\tan\vartheta=\sinh Z\) satisfies

\[
 r(t)=r(s)+I_{s,t},\qquad
 I_{s,t}=\int_s^t\epsilon a(q)C(q)\,dq.
\]

Consequently

\[
 \left|{\partial\vartheta(t)\over\partial\vartheta(s)}\right|
 ={1+r(s)^2\over1+r(t)^2}
 \le2(1+I_{s,t}^2).                                \tag{3}
\]

Unlike shifted sine, the exact local response is polynomial in a Gaussian
carrier rather than lognormal.  This is the candidate's principal new
advantage.

## Remaining theorem boundary

The nonlocal terms in (1) reuse both immutable Gaussian matrices and their
true adjoints.  Linearizing them creates products such as

\[
 \delta d_2\,G_2^*B_3,
 \qquad d_3(\delta G_2)\vartheta_2',
 \qquad d_3G_2\delta\vartheta_2'.
\]

Separate normalized-\(L^2\) estimates do not control their coordinatewise
co-localization.  In the natural coordinate \(r=\tan\vartheta\), the same
issue appears as the lognormal endpoint factor \(1/d=\cosh Z\).  A positive
theorem therefore still needs a mesh-free rooted row/column-cavity estimate
for the canonical trajectory, including chronological \(P/P^*\) feedback,
uniform integrability of \(R_2,Q_1\), and uniqueness of the represented
current operator flow.  Equation (3) resolves only the direct local chain.

## Surviving learned-through ladder

The preceding boundary is not merely a crude norm estimate.  Let
`P2=delta G2` be a cavity or comparison variation.  Since

\[
 P_2(t)=\int_0^t\{\delta B_3(s)\otimes X_2(s)
                 +B_3(s)\otimes\delta X_2(s)\}\,ds,
\]

the term `epsilon d3 P2 theta2'` in the variation of the last equation in
(1) contains

\[
 -\epsilon^2d_3(t)\int_0^t
 \beta(s,t)A(s)\sin\vartheta_3(s)\,
 \delta\vartheta_3(s)\,ds,
 \qquad
 \beta(s,t)=\langle X_2(s),\vartheta_2'(t)\rangle_n.       \tag{4}
\]

There is no raw Gaussian edge or centered empirical scalar on the active
line of (4).  Moreover,

\[
 \beta(t,t)={1\over2\epsilon}{d\over dt}\langle X_2(t)^2\rangle_n,
\]

so no conservation law makes it identically zero.  Its deterministic
small-time expansion is generically nonzero.  Repeating (4) therefore
retains one unsummed readout amplitude at every chronological insertion.
The resulting moment scale is

\[
 { (C\epsilon^5S)^m(mp)^{m/2}\over m!},                 \tag{5}
\]

not a uniformly sub-Gaussian `C^m sqrt(p)` scale.  The time simplex still
sums (5), giving at worst `exp(C epsilon^10 S^2 p)`.  Consequently this is
not an impossibility result: a high-temperature dynamic-cavity theorem
could in principle absorb the growth for `p=c log n`.  It does show that
the exact local characteristic is insufficient, and that any positive
proof must explicitly identify and control the averaged through/Onsager
response rather than silently treating it as a centered collision.
