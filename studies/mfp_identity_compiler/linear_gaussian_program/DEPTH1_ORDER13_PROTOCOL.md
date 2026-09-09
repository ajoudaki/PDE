# One-hidden-layer identity model: order-thirteen and Stieltjes protocol

## Frozen model

Use one hidden layer of width \(n\), raw identity activation, independent
standard-Gaussian initialization, and unit metric on both trainable parameter
blocks:

\[
 X=u,\qquad f_{n,1}=n^{-1}A^\top u,
 \qquad D_n=n\nabla f_{n,1}\mathbin\cdot\nabla.
\]

Define

\[
 F_1^{(r)}(0)=\lim_{n\to\infty}D_n^r f_{n,1}
\]

with width taken first at every fixed order.  No matrix layer, activation
rescaling, frozen parameter block, or depth substitution is admissible.

## Exact method and derivative gates

Solve the finite-width feature-ascent flow for \((A,u)\) directly, then take
the almost-sure width limit using

\[
 n^{-1}\|A_0\|^2\to1,\qquad
 n^{-1}\|u_0\|^2\to1,\qquad
 n^{-1}A_0^\top u_0\to0.
\]

Compute every derivative through order thirteen from the resulting closed
form.  The accepted independent low-order deep-linear controls are

\[
 F_1'(0)=2,\qquad F_1^{(3)}(0)=8,\qquad F_1^{(5)}(0)=32.
\]

All even derivatives must vanish and all reported values must be integers.

## Moment and finite Hankel audit

Use the same output-coordinate convention as the depth-two and depth-three
identity audits:

\[
 K_1(y)=F_1'\!\left(F_1^{-1}(y)\right)
 =F_1'(0)+\sum_{r\ge0}(-1)^r\mu_{r,1}y^{2r+2}.
\]

The order-thirteen jet determines \(\mu_0,\ldots,\mu_5\).  Rational series
reversion/composition, the triangular identity \(F_1'(t)=K_1(F_1(t))\), and
direct expansion of the closed-form \(K_1\) must agree exactly.

Enumerate all 23 distinct accessible square Hankel minors:

- six moment signs;
- thirteen distinct two-by-two minors;
- four distinct three-by-three minors.

In particular, evaluate every principal minor of
\(H_0,H_1,H_2,H_0^+,H_1^+,H_2^+\).

## Stronger all-order check

If the closed-form moments can be represented as

\[
 \mu_r=\int_0^\infty x^r\,d\nu(x)
\]

for an explicit nonnegative measure \(\nu\), verify its normalization and
moment formula exactly.  A measure with positive density on an interval would
prove every ordinary and shifted Hankel matrix positive definite at every
finite order for this depth-one architecture.

## Decision rule

- **Finite-order pass:** all 23 order-thirteen-accessible minors are
  nonnegative; strict positivity makes all six matrices positive definite.
- **Finite-order violation:** at least one exact principal minor is negative.
- **All-order pass:** an explicit nonnegative representing measure is proved
  and has the derived moments at every order.
- **Inconclusive:** the flow derivation, width limit, moment routes, or exact
  minor computations disagree.

The computation budget is 60 seconds and 512 MiB.  No numerical fitting or
finite-width extrapolation is allowed.

## Claim boundary

Any all-order conclusion applies only to this exactly solvable one-hidden-
layer identity architecture under the frozen scaling.  It does not transfer
to identity depth two or three, or to nonlinear activations.
