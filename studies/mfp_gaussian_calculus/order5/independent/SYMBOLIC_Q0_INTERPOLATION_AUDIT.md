# Independent symbolic-\(Q^0\) interpolation audit

**Status:** exact rational reconstruction, unused-point validation, and
post-freeze atomwise comparison all passed  
**Frozen map:** `independent_symbolic_q0_coefficient_map.json`  
**Exact-file SHA-256:**
`e682c708fedadc577b7446a7b9c07b79262c945fbae5726918436153876f889a`

## 1. What is polynomial in \(Q^0\)

The layer atoms remain formal:

\[
X_\nu=\mathbb E_{N(0,Q^0)}\prod_r\phi^{(r)}(G)^{\nu_r},
\qquad
Y_\nu=\mathbb E_{N(0,Q^1)}\prod_r\phi^{(r)}(G)^{\nu_r},
\qquad Q^1=X_{200000}.
\]

Their implicit dependence on the forward variances is not expanded.  The
interpolation reconstructs the **explicit** rational coefficient multiplying
each (X/Y)-atom monomial as a polynomial in (Q^0).

## 2. Degree bound

In the exact feature vector field

\[
\dot a=\phi(z),\qquad
\dot A={1\over n}bh^T,\qquad
\dot u=Q^0\phi'(u)A^Tb,
\]

the only explicit occurrence of (Q^0) is in the (u)-velocity.  Applying
the directional operator once selects exactly one component of this vector
field through the chain rule, and hence can insert at most one new explicit
factor of (Q^0).  The initial output has explicit degree zero.  Induction on
the number of directional derivatives therefore gives

\[
\deg_{Q^0}D^kf_n\le k.
\]

Gaussian expectation, equality partitioning, and Wick--Stein elimination are
linear operations and products whose total Taylor order is preserved, so
they cannot increase this bound.  Consequently

\[
\deg A\le1,\qquad \deg B\le3,\qquad \deg C\le5.
\]

This proof treats (X_\nu,Y_\nu) as degree-zero formal atoms, exactly as the
emitted layer-separated normal form does.

## 3. Preregistered reconstruction

Before loading the primary symbolic map, the independent compiler was run at

\[
Q^0\in\left\{\frac12,1,\frac32,2,\frac52,3\right\}.
\]

For every activation-atom monomial, its six exact `Fraction` coefficients
were interpolated in the monomial basis (1,Q^0,\ldots,(Q^0)^5) by the
Lagrange formula.  Six distinct points uniquely determine every polynomial
allowed by the degree bound.  The observed maximum degrees were exactly

\[
(\deg A,\deg B,\deg C)=(1,3,5).
\]

An additional exact compilation at (Q^0=7/2), not used in interpolation,
agreed coefficientwise with the reconstructed map.  Its discrepancy counts
were zero for (A,B,C).

The reconstructed map was then serialized and hashed.  Only after this
freeze did `interpolate_symbolic_q0.py` import and expand the primary
symbolic-(Q^0) compiler.

## 4. Literal comparison

The comparison uses keys

\[
(\text{sorted tuple of }X/Y\text{ atoms},\;\text{power of }Q^0)
\]

and exact rational coefficients.  The result in
`SYMBOLIC_Q0_PRIMARY_COMPARISON.json` is

| coefficient | independent graded terms | primary graded terms | discrepancies |
|---|---:|---:|---:|
| \(A\) | 3 | 3 | 0 |
| \(B\) | 50 | 50 | 0 |
| \(C\) | 1045 | 1045 | 0 |

Thus the independent and primary formulas agree not only after setting
(Q^0=1), but coefficientwise as full symbolic polynomials in explicit
(Q^0), with the layer-specific Gaussian moments left arbitrary.

Neither the previously frozen unit map nor the previously frozen
(Q^0=1) tagged map was modified by this audit.
