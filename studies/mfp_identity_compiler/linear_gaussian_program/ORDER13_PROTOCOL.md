# Identity depth-2/depth-3 order-thirteen extension: frozen protocol

## Canonical extension

Preserve without modification the architectures, initialization, metric,
width-first limit, feature-ascent derivation, and output-coordinate convention
in `PROTOCOL.md`, `DERIVATION.md`, and `STIELTJES_PROTOCOL.md`.  The exact jet
engine frozen for this extension has SHA-256

`d9218bd819a4ad5e7aea6c7a772a3c6d53291e5a7f52d26755b9e85b8d13e986`.

Extend both identity models from order eleven through exactly order thirteen.
No derivative or moment is extrapolated.

## Primary derivative decision

For each hidden depth \(H\in\{2,3\}\), compute

\[
 F_H^{(12)}(0),\qquad F_H^{(13)}(0)
\]

with both exact coefficient assemblers:

1. ordinary Taylor coefficients with explicit Volterra denominators;
2. derivative-normalized coefficients with binomial/Volterra weights.

The routes must agree at every order through thirteen, reproduce the accepted
order-eleven prefix, give exact zero at every even order, and return integers.

## New moment and PSD decision objects

Use

\[
 K_H(y)=F_H'\!\left(F_H^{-1}(y)\right)
 =F_H'(0)+\sum_{r\ge0}(-1)^r\mu_{r,H}y^{2r+2}.
\]

Order thirteen determines the new moment \(\mu_{5,H}\).  Rational series
reversion/composition and the independent triangular identity
\(F_H'(t)=K_H(F_H(t))\) must agree exactly.

The newly complete shifted matrix is

\[
 H_{2,H}^+=
 \begin{pmatrix}
 \mu_1&\mu_2&\mu_3\\
 \mu_2&\mu_3&\mu_4\\
 \mu_3&\mu_4&\mu_5
 \end{pmatrix}.
\]

Its new distinct PSD inequalities are

\[
 \mu_5\ge0,\qquad
 \mu_1\mu_5-\mu_3^2\ge0,\qquad
 \mu_3\mu_5-\mu_4^2\ge0,\qquad
 \det H_2^+\ge0.
\]

Together with the order-eleven conditions, these are all 14 distinct scalar
PSD inequalities supported by \(\mu_0,\ldots,\mu_5\).

## Complete accessible Hankel-minor audit

Enumerate every distinct square minor of the infinite Hankel array that uses
no moment beyond \(\mu_5\).  There are

- six one-by-one moment signs;
- thirteen distinct two-by-two minors of the form

  \[
  \mu_s\mu_{s+p+q}-\mu_{s+p}\mu_{s+q},
  \qquad s\ge0,\quad1\le p\le q,\quad s+p+q\le5;
  \]

- four distinct three-by-three minors: \(\det H_2\),
  \(\det H_2^+\), and the cross determinants

  \[
  \det\!\begin{pmatrix}
  \mu_0&\mu_1&\mu_3\\
  \mu_1&\mu_2&\mu_4\\
  \mu_2&\mu_3&\mu_5
  \end{pmatrix},
  \qquad
  \det\!\begin{pmatrix}
  \mu_0&\mu_2&\mu_3\\
  \mu_1&\mu_3&\mu_4\\
  \mu_2&\mu_4&\mu_5
  \end{pmatrix}.
  \]

Thus 23 unique accessible square Hankel minors are checked at each depth.

## Competing outcomes and gates

- **H1 / strict finite-order pass:** both exact derivative routes and both
  moment routes agree, and all 23 accessible minors are strictly positive at
  both depths.
- **H0 / finite-order violation:** any exact principal minor is negative; a
  negative cross minor is separately reported as a total-positivity
  violation.
- **Inconclusive:** any route, parity, prefix, hash, integer, runtime, or
  memory gate fails.

Per route and depth, the resource bound is two minutes and 1 GiB.  The audit
stops after order thirteen and the complete \(\mu_0,\ldots,\mu_5\) minor
enumeration.

## Claim boundary

A pass establishes strict compatibility only through the matrices
\(H_2,H_2^+\).  It does not prove an infinite Stieltjes sequence, construct a
representing measure for all orders, establish formal-series convergence, or
imply a positive-time trajectory.  The next ordinary matrix \(H_3\) requires
\(\mu_6\), hence \(F^{(15)}(0)\); its shifted partner additionally requires
\(\mu_7\), hence \(F^{(17)}(0)\).
