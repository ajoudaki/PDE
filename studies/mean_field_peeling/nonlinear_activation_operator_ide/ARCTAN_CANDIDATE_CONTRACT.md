# Frozen arctangent candidate contract

Status: superseded by `ARCTAN_THEOREM_AND_PROOF.md`; retained as the
pre-audit frozen candidate contract, 21 August 2026.

## 1. Why this activation

Take

\[
\phi(q)=\arctan q,
\qquad \phi'(q)=\frac1{1+q^2}.
\]

It is smooth, bounded, non-affine, and has a strictly positive derivative.
The natural coordinate

\[
\Theta(q)=\int_0^q\frac{d\xi}{\phi'(\xi)}
=q+\frac{q^3}{3}                                      \tag{1.1}
\]

is a global increasing bijection with a polynomial Gaussian initialization.
Let \(\iota=\Theta^{-1}\), and define

\[
\Psi(r)=\arctan\iota(r),\qquad
C(r)=\frac1{1+\iota(r)^2},\qquad
D(z)=\frac1{1+z^2}.                                     \tag{1.2}
\]

Then \(\Psi,C,D\) are bounded and globally Lipschitz, and

\[
\Psi'(r)=C(r)^2.                                        \tag{1.3}
\]

The comparison is structural.  Tanh has the same useful conjugacy but gives
\(\Theta(U_0)\) an exponentially transformed Gaussian tail; sine has no
global conjugacy because its derivative vanishes; residual activations remain
unbounded in the forward channel.  Arctan retains saturation and a polynomial
seed simultaneously.

## 2. Exact finite-width state

Write \(r=\Theta(u)\).  Given the current state \((A,r,G)\), define

\[
X=\Psi(r),\quad Z=GX,\quad Y=\arctan Z,\quad
B=A\odot D(Z),\quad Q=G^*B.                              \tag{2.1}
\]

Feature ascent is exactly

\[
\boxed{A'=Y,\qquad r'=Q,\qquad G'=B\otimes X.}           \tag{2.2}
\]

Indeed \(r'=\Theta'(u)u'=G^*B\).  Conversely
\(u=\iota(r)\), so no parameter information has been discarded.

The predictor and kernel are

\[
\boxed{f=\langle A,Y\rangle,}                            \tag{2.3}
\]

\[
\boxed{
K=\langle Y^2\rangle
+\langle B^2\rangle\langle X^2\rangle
+\langle C(r)^2Q^2\rangle .}                             \tag{2.4}
\]

Direct differentiation gives

\[
X'=C(r)^2Q,qquad
Z'=B\langle X^2\rangle+G\{C(r)^2Q\},qquad f'=K.         \tag{2.6}
\]

## 3. Physical autonomous IDE

Let the immutable source consist of the pointed Gaussian row mark \(a_0\),
the column mark

\[
r_0=u_0+u_0^3/3,
\]

and the pointed Ginibre action \(\Gamma:H_C\to H_R\).  Put \(G=\Gamma+q\),
where \(q\) is trace class.  The candidate physical system is

\[
\boxed{
\begin{aligned}
\dot A&=2\eta eY,\\
\dot r&=2\eta eQ,\\
\dot q&=2\eta e\,B\otimes X,\\
\dot e&=-2\eta eK,
\end{aligned}}                                           \tag{3.1}
\]

with (2.1), (2.4), \(A(0)=a_0,r(0)=r_0,q(0)=0\), and
\(e(0)=y_\star\).  The intended internal constraint is

\[
f=y_\star-e,\qquad \mathcal L=e^2.                       \tag{3.2}
\]

It uses two vector fields, one trace-class operator perturbation, one scalar,
and one immutable pointed source.

## 4. Proposed solution/source class

The source is not an ordinary graphon kernel.  It is the separable action/GNS
realization of the limiting values of finite programs generated from
\(a_0,r_0,1\) by:

1. \(\Gamma,\Gamma^*\);
2. finite-rank current updates and normalized inner products;
3. the fixed scalar maps \(\Psi,C,D,\arctan\); and
4. multiplication of an \(L^2\) field by a bounded field.

The candidate topology is strong pointed-program convergence: every finite
program converges jointly in \(W_2\), with a common operator-norm bound for
the source.  A solution on a compact interval must satisfy

\[
A(t)=a_0+\alpha(t),\qquad \alpha\in L^\infty,
\]

with a deterministic bound, while \(r\in L^2\), \(q\in\mathfrak S_1\), and
all fields in (2.1), (2.4) belong to the displayed \(L^2\) domains.

## 5. Proof mechanism submitted to audit

The only non-Lipschitz composition left by (1.1) is

\[
(A,Z)\longmapsto A D(Z).
\]

Since \(|Y|\le\pi/2\), feature time gives

\[
|A(s)-a_0|\le(\pi/2)|s|                                  \tag{5.1}
\]

pointwise.  Thus the Gaussian tail of \(A\) persists after every restart.
For a sub-Gaussian \(A\) and bounded \(h\), interpolation gives the Osgood
modulus

\[
\|A\{h(z)-h(\tilde z)\}\|_2
\le C\delta\sqrt{1+\log(C/\delta)},
\qquad \delta=\|z-\tilde z\|_2.                          \tag{5.2}
\]

All other maps in (2.1)--(3.1) are locally Lipschitz in
\(L^2\oplus L^2\oplus\mathfrak S_1\oplus\mathbb R\) on the a-priori
balls.  Equation (5.2) has divergent reciprocal integral, so Bihari--Osgood
is proposed to give uniqueness and cutoff removal.

For a bounded readout cutoff, Picard/Euler iterates make finitely many
adaptive queries to one fixed Ginibre matrix and its transpose.  Conditional
Gaussian projection is proposed to identify each finite query program and
its \(W_2\) energies.  Dimension-free Lipschitz estimates then remove the
time mesh; (5.2) removes the readout cutoff.

## 6. Obligations that must pass before promotion

1. Construct the pointed action source without using an ultraproduct that
   merely stores the finite-width sequence.
2. Prove the adaptive Gaussian query lemma including singular Gram limits,
   joint row/column marks, and nonlinear \(W_2\) tests.
3. Prove a dimension-free continuous-time approximation for the bounded
   cutoff system.
4. Prove cutoff removal uniformly in width, not only uniqueness of two
   already existing limiting trajectories.
5. Prove uniform integrability and compact-time convergence of every term of
   (2.4), especially \(C(r)^2Q^2\).
6. Prove physical-time global existence and convergence without assuming a
   feature-time interval larger than the physical clock image.
7. Audit rare readout rows, rare transformed-input columns, and adaptive
   alignment against the proposed topology.
8. Verify restartability of the named Gaussian-envelope class and the
   internal constraint (3.2).

These obligations were subsequently discharged in
`ARCTAN_THEOREM_AND_PROOF.md`; this sentence records the decision boundary
that applied when the candidate was frozen.
