# Exact separable continuous-carrier realization of the p=1 flow

Lead-author independent candidate, 2026-09-18. Scientific inputs are the
complete canonical coefficient construction in docs/observable_p1.md,
the physical equations and existence proofs in global_nonlinear.md
C.4.7.9.3--4/C.4.7.10.D.3, and this study's plateau_finite_critical.md.
This file is frozen before comparison with the independent basin routes.
It does not assert an all-time convergence theorem. No numerical work.

## 1. A compact carrier without a Gaussian cutoff

Fix three independent inputs x_i in sqrt(3) S^2, u_i=x_i/sqrt(3),
positive probability weights p_i and binary labels y_i. Retain the exact
canonical odd-sector b_1 in R6 and b_2 in R3, with every initialized
correlation with g and the full 3 by 6 matrix. Put

\[
 z_i^0=\phi(g\cdot u_i),\qquad
 K_1=\operatorname{supp}\operatorname{Law}(b_1,z_1^0,z_2^0,z_3^0),
 \qquad K_2=\operatorname{supp}\operatorname{Law}(b_2).
\]

Both are compact metric spaces: all displayed coordinates are bounded,
and support is closed in their finite-dimensional ambient boxes. Keep
the exact pushforward probability measures nu_1,nu_2. These have full
support by definition, are invariant under simultaneous negation, and
give zero mass to any event |z_i^0|=1. This is a compactification of
the carrier, not Gaussian truncation or replacement of the population law.

For r in [-1,1] and s real define

\[
 T(r,s)=\frac{r+\tanh s}{1+r\tanh s}.
\]

The denominator is positive, and on |s|<=R is at least 1-tanh R>0.
Consequently T and all its s-derivatives are uniformly bounded on each
such compact strip; T(r,s) has absolute value at most one and
partial_s T=1-T^2. On the original Gaussian carrier,

\[
 \phi((g+v)\cdot u_i)=T(z_i^0,v\cdot u_i).
\]

Thus a displacement field v=w-g, rather than w itself, suffices to give
an exact equation on these compact carriers. The finite original g may
be recovered almost surely from the first three normalized coordinates
of b_1; no new information beyond the fixed initialized marks is added.

## 2. Separable state space and smooth exact flow

Let

\[
 X=C_{\rm odd}(K_1;\mathbb R^3)\times C_{\rm odd}(K_2;\mathbb R)
                  \times\mathbb R^{3\times6},
\]

with the sum of supremum and Frobenius norms. The subscript means oddness
under simultaneous negation of the carrier coordinates. Continuous
functions on compact metric spaces are separable in the supremum norm:
for example polynomials with rational coefficients are dense on these
compact Euclidean subsets by the real Stone--Weierstrass theorem, and odd
symmetrization gives a countable dense set in the odd subspace. Equivalently
one can use finite rational-valued approximations built from finite nets
and piecewise-linear distance partitions. X is a separable Banach space.

For theta=(v,c,M) in X set

\[
 h_i=T(z_i^0,v\cdot u_i),\quad a_i=\int b_1h_i\,d\nu_1,
 \quad H_i=\phi(b_2^TMa_i),\quad f_i=\int cH_i\,d\nu_2,
 \quad r_i=f_i-y_i,
 \quad d_i=\int b_2c\phi'(b_2^TMa_i)\,d\nu_2.
\]

The exact canonical field is

\[
 \begin{split}
 \dot v&=-2\sum_i p_i r_i(1-h_i^2)(b_1^TM^Td_i)u_i,\\
 \dot c&=-2\sum_i p_i r_iH_i,\\
 \dot M&=-2\sum_i p_i r_i d_i a_i^T.
 \end{split}
\]

Products, finite-dimensional smooth compositions on bounded ranges, and
bounded linear integrations show directly that this is C-infinity as a
map X to X, with locally bounded derivatives of every fixed order.
One may verify Frechet differentiation by the uniform scalar Taylor
remainders on each bounded state ball. Oddness is preserved term by term.
Canonical initialization is the single deterministic point (0,0,D) in X.
The earlier constructed moment-matching displacements linear in b_1 and
the explicit readouts are also in X.

The physical Hilbert norm on X is

\[
 \|(v,c,M)\|_{\mathcal H}^2
 =\int|v|^2d\nu_1+\int|c|^2d\nu_2+\|M\|_F^2.
\]

Full support makes its embedding injective. The usual differentiation
under these bounded integrals gives the exact physical gradient and
energy identity for L=sum_i p_i r_i^2. No clock or metric is changed.

All finite-time trajectories from X exist in X. Indeed c velocity has
supremum bound 2 sqrt(L), so on a finite horizon c is bounded by its
initial bound plus 2t sqrt(L(0)); a_i are bounded by the frozen mark
bound and d_i by a constant times ||c||_2. Hence M' is bounded by a
constant times sqrt(L(0)) ||c||_2, giving a finite polynomial bound on M.
The displayed lower equation then bounds v' by a constant times
sqrt(L(0)) ||M|| ||c||_2. Thus no X-norm blowup occurs at finite time.
These are horizon-dependent bounds, not all-time boundedness.

On every finite trajectory segment the local reverse ODE exists as well.
Uniqueness gives inverse time maps on their images. Continuous dependence
on a neighborhood of a compact time segment gives an open image, and
differentiating the integral equation gives C1 dependence and an
invertible variational operator (its inverse solves the reversed linear
equation). Thus each finite forward-time map is a C1 diffeomorphism from
X onto an open subset of X. Global backward existence is not claimed.

## 3. Finite-rank critical Hessian for independent inputs

At a critical point, lower stationarity and independent u_i imply

\[
             p_i r_i M^Td_i=0\quad\hbox{for every }i.
\]

Indeed the gates are positive almost surely, and the Gram of b_1 is
positive definite. The only local multiplication term in the loss
Hessian is, on two lower variations h,k,

\[
 2\sum_i p_i r_i\int
   (b_1^TM^Td_i)\phi''((g+v)\cdot u_i)
             (h\cdot u_i)(k\cdot u_i)\,d\nu_1,
\]

which vanishes by the individual identities. All other terms factor
through finitely many bounded linear moment maps. More explicitly the
Hessian's range is contained in the space spanned by:

* 18 lower vector functions b_{1,j}(1-h_i^2)u_i;
* 3 upper functions H_i and 9 upper functions
  b_{2,k} phi'(b_2^TMa_i);
* all 18 matrix-coordinate directions.

This gives rank at most 48. The Hessian is symmetric in the physical
Hilbert inner product; all its coefficient functions are continuous and
bounded, so it extends to a bounded finite-rank self-adjoint operator on
the physical Hilbert completion. Its range lies in X, and its nonzero
eigenvectors lie in that range. Finite-dimensional symmetric matrix
diagonalization on the range gives a splitting of X into finite-dimensional
positive- and negative-eigenvalue spaces and the closed kernel. The
projections are bounded on X, since they use finitely many integrals
against bounded eigenvectors.

For a finite critical point with 0<L<1, M cannot be zero, because M=0
would give f_i=0 and L=1. The own-study strict-saddle theorem supplies a
negative Hessian direction. If its proof's initial direction is only
bounded measurable, continuous odd fields approximate it in L2 (regular
Borel measures on compact metric spaces permit continuous approximation
of indicator functions, followed by odd symmetrization). The bounded
Hilbert Hessian then preserves negativity for a sufficiently close
continuous approximation. Thus the negative-eigenvalue space is nonzero.

There is also a positive direction: some H_j is nonzero, since otherwise
all predictions vanish and L=1. Varying only c by H_j has loss Hessian
2 sum_i p_i (E[H_j H_i])^2>0. Hence the positive-eigenvalue space is
nonzero. For the gradient-flow linearization these are respectively
repelling and attracting spaces; the kernel is neutral to first order.

This proves the spectral prerequisites in an exact separable C1 flow
space containing the canonical initialized trajectory and explicit bad
states. A nonlinear trapping-graph proof and a global basin statement
are separate obligations, supplied or checked in subsequent integration.

## 4. Scope cautions

This continuous-carrier state class is an invariant subset of the full
bounded-measurable field class. It contains every canonical finite-time
state, but an arbitrary bounded-measurable restart need not belong to it.
Neither boundedness nor convergence as t tends to infinity is asserted.
The Gaussian carrier measure describes neurons inside one deterministic
population state; it is not a random law on X. Any probability of avoiding
a basin must explicitly specify a random law on initial population fields.
