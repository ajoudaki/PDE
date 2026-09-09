# Order-five limit, inversion, and Padé audit

Status: the algebra in Sections 1--3 is exact conditional on accepted values
of \(A,B,C\).  Section 4 states the probability hypotheses required to
promote the flattened finite formula to the annealed width limit.

## 1. Local inverse calculation

Readout-sign parity gives an odd route

\[
F(t)=At+\frac{B}{3!}t^3+\frac{C}{5!}t^5+O(t^7).
\]

For \(A\ne0\), let \(t=F^{-1}(y)\).  Direct series reversion gives

\[
t=\frac yA-\frac{B}{6A^4}y^3
+\frac{10B^2-AC}{120A^7}y^5+O(y^7).
\]

Since

\[
F'(t)=A+\frac B2t^2+\frac C{24}t^4+O(t^6),
\]

substitution yields

\[
\boxed{
K(y)=F'(F^{-1}(y))
=A+\mu_0y^2-\mu_1y^4+O(y^6),
}
\]

where

\[
\boxed{
\mu_0=\frac{B}{2A^2},\qquad
\mu_1=\frac{4B^2-AC}{24A^5}.}
\]

The sign in front of \(\mu_1\) is part of the convention.

## 2. One-pole Padé kernel

Matching the two displayed nonlinear coefficients gives

\[
\boxed{
K_{[0/1]}(y)=
A+\frac{\mu_0y^2}{1+(\mu_1/\mu_0)y^2}.}
\]

This formula assumes \(\mu_0\ne0\).  If \(\mu_0=0\), the requested
one-pole parametrization is singular and must be replaced by the appropriate
degenerate Padé problem.  The expression is always a local Padé approximant
away from its pole.  Calling it a positive Stieltjes approximant additionally
requires \(\mu_0\ge0\), \(\mu_1\ge0\), and the corresponding nondegeneracy;
generic smooth activations do not automatically satisfy these signs.

## 3. Induced one-sample loss curve

For label one and the no-\(1/2\) squared loss, the Padé kernel induces

\[
\dot y=2\eta(1-y)K_{[0/1]}(y),\qquad
L_{[0/1]}=(1-y)^2.
\]

Separating variables from \(y(0)=0\) gives the exact implicit curve

\[
\boxed{
2\eta t=
\int_0^{y(t)}
\frac{1+(\mu_1/\mu_0)s^2}
{(1-s)\left[A+(A\mu_1/\mu_0+\mu_0)s^2\right]}
\,ds,
\qquad
L_{[0/1]}(t)=(1-y(t))^2.}
\]

This is an exact solution of the rational-kernel ODE on the connected interval
from zero that contains no zero or pole of the displayed denominator.  It is
not a theorem that the finite-width neural-network loss follows this curve at
positive time; only the kernel's local Taylor coefficients are matched.

## 4. Annealed width-limit hypotheses

For any fixed derivative order five, the exact finite-width observable can be
encoded as one finite NETSOR\({}^\top+\) scalar program: the matrix
\(W/\sqrt n\) and its transpose are reused finitely many times, and all other
operations are coordinatewise nonlinearities, empirical `Moment` scalars,
and deterministic scalar arithmetic.

Two theorem tiers must be kept separate.

1. If \(\phi^{(r)}\) is pseudo-Lipschitz for \(0\le r\le5\), the Gaussian
   tensor-program master theorem gives the almost-sure limit of the exact
   scalar program, including all transpose responses and singular covariance
   cases.  This alone does not imply convergence of expectations.
2. If \(\phi\) is polynomially smooth--\(C^\infty\), with every derivative
   polynomially bounded--then Theorem 3.7 of Golikov--Yang,
   *Non-Gaussian Tensor Programs*, applies (Gaussian matrices are a special
   case) and gives convergence almost surely and in every finite \(L^p\).
   Hence the family is uniformly integrable and
   \(\mathbb E[D_n^5f_n]\) converges to the flattened Gaussian normal form.

Under only finite-order regularity, an annealed theorem instead requires an
explicit hypothesis such as

\[
\sup_n\mathbb E|D_n^5f_n|^{1+\epsilon}<\infty
\]

for some \(\epsilon>0\), together with the almost-sure program limit.  Mere
pointwise polynomial growth through derivative five is not by itself that
uniform-integrability proof.

## 5. Variance normalization and the quadratic certificate

The unit-Gram presentation \(Q^0=Q^1=Q^2=1\) uses one standard-normal
moment alphabet.  The mandated unnormalized control \(\phi(x)=x^2\) does not
lie in that specialization: with \(Q^0=1\), it has

\[
Q^1=\mathbb E G^4=3,\qquad
Q^2=\mathbb E Z^4=27\quad(Z\sim N(0,3)).
\]

It must therefore be checked against the arbitrary-forward-variance formula.
This is a scope distinction, not a rescaling of the requested model.

