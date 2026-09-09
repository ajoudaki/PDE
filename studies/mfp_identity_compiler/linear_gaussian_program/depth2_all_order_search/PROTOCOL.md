# Depth-two identity all-order closure search: frozen protocol

Status: frozen before the long-jet and equation-guessing runs, 20 August
2026.

## 1. Mathematical object

Use exactly the accepted one-input, equal-width, identity-activation model
and feature-ascent convention from the parent directory.  With

\[
x=A/\sqrt n,\qquad y=u/\sqrt n,\qquad B=W/\sqrt n,
\]

the finite-width characteristic equations are

\[
f=x^TBy,\qquad x'=By,\qquad y'=B^Tx,\qquad B'=xy^T.
\]

Initialization is independent standard Gaussian in the original
coordinates, the width limit is taken at each fixed derivative order, and

\[
K(z)=F'(F^{-1}(z))
    =F'(0)+\sum_{r\ge0}(-1)^r\mu_rz^{2r+2}.
\]

No loss-time or positive-time convergence claim is part of this search.

## 2. Exact-coefficient gate

The existing two algebraically distinct assemblers must agree exactly at
every order through 81:

1. ordinary Taylor/Volterra coefficients;
2. derivative-normalized/binomial coefficients.

All even derivatives must vanish, all derivatives must be integers, and the
accepted prefix through order 13 must be reproduced.  Exact triangular
solution of `F'=K(F)` and exact series reversion/composition must agree on
all 40 moments `mu_0,...,mu_39`.

Per assembler the resource ceiling is two minutes and 2 GiB.  A failed gate
makes the closure search inconclusive.

## 3. Precommitted discovery/holdout split

Only `mu_0,...,mu_24` may be used to fit an equation.  The fifteen moments
`mu_25,...,mu_39` are sealed holdout coefficients.

The following low-complexity classes are searched in increasing parameter
count and then lexicographic degree order.

### Algebraic ordinary generating function

For

\[
M(q)=\sum_{r\ge0}\mu_rq^r,
\]

search nonzero primitive rational polynomials

\[
P(q,M)=\sum_{i=0}^{d_q}\sum_{j=0}^{d_M}c_{ij}q^iM^j
\]

with `1 <= d_M <= 4`, `0 <= d_q <= 6`, and at most 25 coefficients before
normalization.  A fit is retained only if it annihilates all 15 held-out
coefficients exactly.

### P-recursive moment sequence

Search recurrences

\[
\sum_{j=0}^{R}p_j(r)\mu_{r+j}=0
\]

with `1 <= R <= 4`, `deg p_j <= 4`, and at most 25 coefficients before
normalization.  Again, every unused available equation must vanish exactly.

Equivalent scalar rescalings and polynomial common factors are removed.
The search space is deliberately bounded: failure means only that no formula
in these frozen classes was found.

## 4. Promotion rule

An exact held-out pass yields a **candidate equation**, not an all-order
theorem.  It may be promoted to an all-order moment result only after an
independent derivation from the matrix characteristic flow (or an equivalent
proved recurrence) establishes the equation and selects the analytic branch
at the origin.  Stieltjes positivity at all orders additionally requires an
explicit nonnegative representing measure or a separate all-order positivity
proof.

