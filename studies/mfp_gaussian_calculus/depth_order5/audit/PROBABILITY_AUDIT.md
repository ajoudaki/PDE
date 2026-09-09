# Probability and annealed-limit audit at fixed depth

## 1. Exact finite algebra versus a width theorem

At any finite width, the order-five moving-flow construction uses only
`phi,...,phi^(5)`.  A sufficient finite-algebra envelope is

\[
\phi\in C^5,
\qquad
|\phi^{(r)}(x)|\le C_r(1+|x|^{m_r}),\quad0\le r\le5,
\]

together with finiteness of the displayed contractions.  This statement by
itself gives neither a population limit nor expectation convergence.

## 2. Fixed-program theorem tier

For each separately fixed `H in {3,4}`, fixed `B=1`, and fixed finite
`Q0>=0`, the exact Taylor construction is a finite NETSOR-transpose-plus
program:

- the matrices are `W^ell/sqrt(n)` with independent `N(0,1/n)` entries;
- the first preactivation and readout are Gaussian vectors;
- every forward and transpose reuse is a program line;
- all coordinatewise nonlinearities, empirical moments, scalar products, and
  rank-one Taylor updates form a finite graph independent of `n`.

A sufficient activation hypothesis for direct annealed convergence is

\[
\phi\in C^\infty,
\qquad
\forall r\ge0\ \exists C_r,m_r<\infty:
|\phi^{(r)}(x)|\le C_r(1+|x|^{m_r}).
\tag{2.1}
\]

Under (2.1), all coordinate maps in the finite graph are polynomially smooth.
Setup 3.6 and Theorem 3.7 of Golikov--Yang, *Non-Gaussian Tensor Programs*,
then apply; Gaussian matrices are a special case and the language permits
repeated matrix/transpose use and empirical scalar moments.  Every final
scalar converges almost surely and in every finite `L^p`.  In particular,
for `k=1,3,5`, `L^1` convergence gives

\[
\lim_{n\to\infty}\mathbb E[D_n^kf_n]
=\mathbb E[\lim_{n\to\infty}D_n^kf_n].
\]

No separately assumed uniform integrability is needed in this strong tier,
because any `L^(1+epsilon)` convergence supplied by the theorem implies it.
Singular forward Grams, including constant/zero activations or `Q0=0`, do not
require a covariance pseudoinverse or rank-stability assumption in this
route.

## 3. Weaker tier

If only a convergence-in-probability or almost-sure tensor-program limit is
available, expectation convergence requires a separate bridge.  A sufficient
condition is, for some `epsilon>0`,

\[
\sup_n\mathbb E|D_n^kf_n|^{1+\epsilon}<\infty,
\qquad k\in\{1,3,5\}.
\tag{3.1}
\]

Equation (3.1) gives uniform integrability; combined with convergence in
probability it yields `L^1` and the annealed coefficient.  It is not
equivalent to `L^(1+epsilon)` convergence.  Merely assuming `C^5` and
finite-order polynomial growth does not invoke the all-orders theorem and
does not prove (3.1).

## 4. Depth scope

All statements are pointwise at fixed `H`.  They provide no convergence for
`H=H(n)`, no depth-uniform integrability constants, and no depth-uniform
conditioning or error estimates.  A finite transition rule that can be
executed for arbitrary fixed depth is therefore not, by itself, a theorem in
a simultaneous width/depth limit.

