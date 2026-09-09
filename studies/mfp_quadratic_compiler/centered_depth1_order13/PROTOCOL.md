# One-hidden-layer normalized Hermite-2 audit: frozen protocol

Status: frozen before coefficient production, 20 August 2026.

## 1. Model and normalization

The network has one trainable hidden layer and one unit-RMS input:

\[
f_n=\frac1n\sum_{i=1}^n A_i\phi(u_i),\qquad
\phi(u)=\frac{u^2-1}{\sqrt2}.
\]

Thus `phi` is the probabilists' Hermite polynomial `He_2` divided by
`sqrt(2!)`; for a standard Gaussian `G`, `E phi(G)=0` and
`E phi(G)^2=1`.  Both `A_i` and `u_i` train in the same mean-field metric,
and initially they are independent standard Gaussians.

Under feature-ascent time, neurons decouple:

\[
A'=\phi(u),\qquad u'=A\phi'(u).
\]

Putting `b=sqrt(2) A` and `v=u^2` gives the rational polynomial system

\[
b'=v-1,\qquad v'=2bv,\qquad
F(s)=\frac12\,\mathbb E[b(s)(v(s)-1)].
\]

The initial variables are independent, `b=sqrt(2)G_1` and `v=G_2^2`.

## 2. Exact order-thirteen decision

Compute every derivative `F^(k)(0)`, `0 <= k <= 13`, by two independent
exact routes:

1. repeated polynomial Lie differentiation of the observable;
2. ordinary Taylor solution of the two ODEs followed by series composition.

The two vectors must agree exactly.  Every even derivative must be zero.
Gaussian expectations are evaluated from the explicit formulas

\[
\mathbb E[b^{2p}]=2^p(2p-1)!!,\qquad
\mathbb E[v^q]=(2q-1)!!,
\]

with every odd `b` moment zero.

## 3. Moment and Hankel decision

Use

\[
K(y)=F'(F^{-1}(y))
 =F'(0)+\sum_{r\ge0}(-1)^r\mu_ry^{2r+2}.
\]

Recover `mu_0,...,mu_5` both by exact reversion/composition and by the
triangular identity `F'=K(F)`.  Enumerate every distinct square Hankel minor
using no moment after `mu_5`: 6 one-by-one, 13 two-by-two, and 4
three-by-three minors.  In particular audit every principal minor of
`H_2=(mu_{i+j})` and `H_2^+=(mu_{i+j+1})`.

A negative principal minor is an exact finite-order Stieltjes violation.  A
strict pass is finite-order compatibility only.

## 4. Closed-form attempt and claim boundary

First derive any genuine coordinate invariant and resulting quadrature.
Optionally extend the cheap exact Lie jet and subject the moment OGF to the
same discovery/holdout algebraic and P-recursive search frozen in the
depth-two identity protocol.  A quadrature for each neuron is not a closed
scalar formula for the Gaussian average `F`; a coefficient fit is only a
candidate.  No all-order claim is allowed without an independent derivation
and, for Stieltjes positivity, a representing measure or all-order PSD proof.

