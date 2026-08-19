# Canonical hidden-norm high-order successor

Status: frozen before interpretation of the order-sixteen hidden-observable
results, 19 August 2026.

## Decision question

For the canonical one-input quadratic network with

\[
D=D_a+D_u+D_W,
\]

use the proved fixed-order Gaussian-program recurrence through feature order
seventeen to extend the two hidden preactivation squared-RMS observables

\[
Q_1(s)=\mathbb E[u(s)^2],\qquad Q_2(s)=\mathbb E[z(s)^2].
\]

Writing \(F\) for the canonical feature curve, \(G=F^{-1}\), and

\[
N_j(y)=Q_j(G(y)),
\]

test the exact moment candidates in

\[
\frac{N_j(\sqrt x)-N_j(0)}{x}
=\sum_{r\geq0}(-1)^r\nu^{(j)}_r x^r.
\]

The literal RMS is a derived observable.  To test it directly as well, define

\[
\frac{\sqrt{N_j(\sqrt x)/N_j(0)}-1}{x}
=\sum_{r\geq0}(-1)^r\omega^{(j)}_r x^r.
\]

Multiplication by \(\sqrt{N_j(0)}\) recovers the unnormalized literal-RMS
increment and cannot change any Hankel sign.

## Frozen outputs

1. Reproduce the accepted canonical feature jet through \(F^{(17)}(0)\).
2. Compute \(Q_2^{(k)}(0)\) exactly for every \(0\leq k\leq16\).
3. Obtain \(Q_1^{(k)}(0)\) through order eighteen from the exact Ward identity
   \(Q_1'=8F\).  No order-nineteen feature derivative is required.
4. Determine \((\nu^{(1)}_0,\ldots,\nu^{(1)}_8)\) and
   \((\nu^{(2)}_0,\ldots,\nu^{(2)}_7)\), together with the corresponding
   literal-RMS sequences \(\omega^{(1)}\) and \(\omega^{(2)}\).
5. Evaluate every accessible ordinary and shifted Hankel matrix and every
   nonempty principal minor using exact arithmetic.

## Exact validity gates

1. The two recurrence implementations must reproduce independently the full
   canonical feature jet through order seventeen and the full second-hidden
   jet through order sixteen.
2. Both implementations must reproduce the accepted Campaign-1 canonical
   values for \(Q_1,Q_2\) through order eight before higher orders are used.
3. Hidden-observable parity must hold exactly: all odd derivatives vanish.
4. The first-hidden jet must agree coefficientwise with \(Q_1'=8F\).
5. Formal inversion, square root, moments, determinants, and all principal
   minors use exact rational arithmetic.  Floating-point values are
   descriptive only.
6. A negative principal minor is a finite-order counterexample for the
   corresponding companion sequence.  Positive finite matrices are only
   finite-order compatibility evidence.

## Resource and stop rule

Each complete order-seventeen recurrence has a 30-minute wall-time and 8-GiB
resident-memory cap, inherited from the accepted canonical feature successor.
No \(F^{(19)}(0)\), \(Q_2^{(18)}(0)\), or larger-order branch is authorized.

## Interpretation boundary

This is a fixed-order width-limit calculation.  It does not prove all-order
Hankel positivity, moment determinacy, a positive-time mean-field limit, or
identification with a global neural trajectory.  The first-hidden claim is
structurally inherited from the inverse-output Stieltjes conjecture; the
second-hidden claim is an independent companion conjecture.
