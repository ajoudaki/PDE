# Frozen conjecture: quadratic depth-two operator IDE

Status: resolved negatively for the canonical iid-Gaussian sequence,
22 August 2026.

## Resolution

The frozen requirements are mutually impossible for the canonical sequence.
The [covariant Schur no-go theorem](CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md)
proves that, with probability tending to one, the predictor gains a fixed
positive amount by feature time at most
\((0.09+o(1))/\sqrt{\log n}\).  The corresponding physical MSE time tends to
zero.  Compact-time uniform convergence to any continuous predictor readout
would therefore force that fixed jump to vanish, a contradiction.

The pole separation used by the proof is certified by
[`outer_pole_certificate.c`](outer_pole_certificate.c), SHA-256
`f191d9720196e9300b7771a4b9aca4e65340cf3f2399e44d60493ccf062026d1`.
The frozen statement below is retained as the exact contract that has now
been decided.

## Finite model

For \(H_n=\mathbb R^n\) with

\[
\langle v,w\rangle_n=n^{-1}v^{\mathsf T}w,
\]

initialize \(A,u\) with independent standard-Gaussian coordinates and
\(G=W/\sqrt n\), with \(W_{ij}\) independent standard Gaussians.  Define

\[
X=u^{\odot2},\quad Z=GX,\quad B=A\odot Z,\quad R=G^*B,
\quad f=\langle A,Z^{\odot2}\rangle_n.
\]

Feature ascent and physical MSE time are

\[
A'=Z^{\odot2},\quad u'=4u\odot R,\quad G'=2B\otimes X,
\]

\[
\dot\theta=2\eta(y_\star-f)\theta',\qquad
\dot e=-2\eta eK,qquad e=y_\star-f,
\]

where \((p\otimes q)v=p\langle q,v\rangle_n\) and

\[
K=\langle Z^{\odot4}\rangle_n
+4\langle B^{\odot2}\rangle_n\langle X^{\odot2}\rangle_n
+16\langle X\odot R^{\odot2}\rangle_n.
\]

## Conjecture

There is an autonomous, restartable, width-independent description using a
fixed finite number of scalar, vector, measure, spatial-kernel, traffic, or
operator fields on a source fixed before training by the iid-Gaussian
initialization.  It has no two-training-time object and no stored history;
its current state has continuous real-valued readouts for \(f,K,e,e^2\); it is
well posed on every finite physical-time interval; and for every deterministic
\(T<\infty\), the finite-width output and loss converge in probability
uniformly on \([0,T]\) to those readouts.

Infinite-dimensional fields are allowed, but a post-hoc ultraproduct, a
width-sized atomic source, a trajectory oracle, or merely renaming the full
unproved hierarchy is not a resolution.

## Natural candidate

Use the immutable two-sorted pointed Gaussian-traffic source \(C\), write
\(G=C+q\), and evolve the four current fields \((A,u,q,e)\) by the equations
above.  Equivalently, package all present-time pointed traffic observables in
one Liouville probability state.  This candidate is exact algebraically at
every fixed graph order.  The campaign must decide its positive-time status,
not merely restate the formal hierarchy.

## Decisive outcomes

The campaign completes only with one of the following.

1. A named source space and topology, a globally well-posed autonomous
   evolution, continuous \(f,K,e,e^2\) readouts, a no-leakage theorem, and
   uniform compact-physical-time iid-Gaussian finite-width identification.
2. A theorem showing that the frozen requirements are mutually impossible
   for the canonical iid-Gaussian sequence itself (for example, a rigorously
   proved concentration layer incompatible with uniform convergence to a
   continuous readout).

Ambient spike examples, fixed-order Wick convergence, formal Liouville
notation, and no-go theorems for only finitely many moments do not decide the
conjecture.

## Fixed gates

Any positive construction must reproduce

\[
f(0)=0,\quad K(0)=111,
\]

and the accepted feature jet

\[
F'(0)=111,\quad F^{(3)}(0)=1\,685\,184,
\quad F^{(5)}(0)=77\,400\,633\,120.
\]

Matrix reuse, \(G^*\), and coordinatewise multiplication must coexist in the
same source.  Every invoked theorem must have its hypotheses checked for the
unbounded Gaussian marks and the positive-time width limit.
