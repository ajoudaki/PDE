# Depth-3 quadratic Gaussian-program jet: frozen protocol

## Frozen object

Fix one input, three hidden layers of equal width (n), the raw activation
(phi(x)=x^2), independent standard-Gaussian initialization, and

\[
X_i=u_i^2,
\qquad
Z_j=\frac1{\sqrt n}\sum_i W_{ji}X_i,
\qquad
Y_j=Z_j^2,
\qquad
T_k=\frac1{\sqrt n}\sum_j V_{kj}Y_j,
\]

\[
f_n=\frac1n\sum_k A_kT_k^2,
\qquad
D_n=n\nabla f_n\mathbin\cdot\nabla,
\qquad
F^{(r)}(0)=\lim_{n\to\infty}D_n^r f_n.
\]

All four parameter blocks ((A,V,W,u)) have unit metric weight.  The limit is
always width first at a fixed derivative order.  This is the raw quadratic
model, whose forward Gram chain begins (1,3,27,2187); no unit-Gram quotient
or normalized activation is substituted.

## Frozen exact reduction

Put

\[
B_3=A\odot T,
\quad R_2=n^{-1/2}V^\top B_3,
\quad B_2=Z\odot R_2,
\quad R_1=n^{-1/2}W^\top B_2.
\]

The feature-ascent flow has the exact finite-width equations

\[
\dot A=T^2,
\qquad
\dot V=\frac2{\sqrt n}B_3Y^\top,
\qquad
\dot W=\frac4{\sqrt n}B_2X^\top,
\qquad
\dot X=16X\odot R_1.
\]

Both fixed matrices are integrated before the width limit.  Their forward
and transpose uses are then detransposed by chronological Gaussian
innovations and exact Stein-response terms.  The calculation uses three
scalar Gaussian polynomial laws:

1. bottom: (u) and the (W^\top) innovations;
2. middle: the (W) innovations and the (V^\top) innovations;
3. top: (A) and the (V) innovations.

The two innovation families in the middle law have zero cross-covariance;
their dependence is retained by the two response sums.  All arithmetic is
rational and every Gaussian expectation is evaluated by Wick recurrence.

## Research contract and decision rule

- **Hypothesis H1.**  The nested two-matrix detransposition closes as an
  exact finite Gaussian program and remains computationally practical
  through (F^{(9)}(0)).
- **Null H0.**  A missing transpose response invalidates the extension, or
  the exact sparse-polynomial state grows beyond the frozen resource bound.
- **Primary output.**  The exact integer jet
  (F^{(r)}(0)), (0\le r\le9), with the new (r=7,9) values accepted only
  after every validation gate passes.

## Validation gates

1. The depth-3 raw-quadratic controls are reproduced exactly:

   \[
   F'(0)=14\,175,
   \quad F^{(3)}(0)=139\,445\,032\,896,
   \quad
   F^{(5)}(0)=4\,298\,284\,752\,832\,899\,360.
   \]

2. Parity gives exact zeros at orders (0,2,4,6,8).
3. A second coefficient assembler, using derivative-normalized jets and
   binomial/multinomial product rules rather than ordinary Taylor
   coefficients, agrees exactly through order nine.  It may share the
   audited polynomial and Wick primitives, but not the recurrence assembler.
4. Every reported rational has denominator one.
5. The initial first-derivative block audit is
   (2187+2916+3888+5184=14\,175), corresponding respectively to
   ((A,V,W,u)).

A lower-order mismatch is a failed computation, not evidence about the new
orders.  Exhausting the resource bound is inconclusive.

## Frozen resource and claim boundary

- Maximum order: nine.
- Per exact route: 10 minutes wall time and 4 GiB virtual memory.
- No positive-time trajectory, convergence radius, all-order sign pattern,
  Stieltjes representation, or arbitrary-depth efficiency claim is in scope.
- “Efficient” here means that both exact depth-3 order-nine routes finish
  inside this explicit bound without enumerating derivative forests.
