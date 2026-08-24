# Shallow normalized Hermite-2 activation: exact order-13 violation

Status: **exact finite-order Stieltjes violation**, 20 August 2026.

## 1. Model and exact two-dimensional reduction

The activation is the unit-Gaussian-variance probabilists' Hermite
polynomial

\[
\phi(u)=\frac{u^2-1}{\sqrt2},\qquad
\mathbb E\phi(G)=0,\quad \mathbb E\phi(G)^2=1.
\]

For

\[
f_n=\frac1n\sum_i A_i\phi(u_i),
\]

feature-ascent time gives independent neuron characteristics

\[
A'=\phi(u),\qquad u'=A\phi'(u).
\]

With `b=sqrt(2)A` and `v=u^2`, all irrational coefficients disappear:

\[
b'=v-1,\qquad v'=2bv,qquad
F(t)=\frac12\mathbb E[b(t)(v(t)-1)].
\tag{1.1}

Initially `b=sqrt(2)G_1` and `v=G_2^2` are independent.

## 2. Exact derivatives

Repeated polynomial Lie differentiation of (1.1) and an independently
assembled ordinary-Taylor ODE recurrence agree exactly.  Every even
derivative through order twelve is zero, and

\[
\begin{aligned}
F'(0)&=3,\\
F^{(3)}(0)&=192,\\
F^{(5)}(0)&=38592,\\
F^{(7)}(0)&=16882272,\\
F^{(9)}(0)&=13710887424,\\
F^{(11)}(0)&=18618267830400,\\
F^{(13)}(0)&=39219558574625280.
\end{aligned}
\tag{2.1}

These are exact Gaussian expectations, not floating-point numerics.

## 3. Output-kernel moments

For

\[
K(y)=F'(F^{-1}(y))
=F'(0)+\sum_{r\ge0}(-1)^r\mu_ry^{2r+2},
\]

exact series reversion and the separate triangular solve `F'=K(F)` agree on

\[
\boxed{
\begin{aligned}
\mu_0&=\frac{32}{3},&
\mu_1&=\frac{440}{81},&
\mu_2&=\frac{160738}{10935},\\
\mu_3&=\frac{30517412}{688905},&
\mu_4&=\frac{85823505179}{558013050},&
\mu_5&=\frac{13556868117611}{23675696550}.
\end{aligned}}
\tag{3.1}

All six moments are positive.  The ordinary matrices `H_0,H_1,H_2` and the
shifted matrices `H_0^+,H_1^+` are positive definite.  Every accessible
one-by-one and two-by-two Hankel minor is positive.  However,

\[
\boxed{
\det H_2^+
=-\frac{515758203187135106171912}
        {485517025870694173125}<0.}
\tag{3.2}

Thus `H_2^+` is indefinite.  Among all 23 distinct square Hankel minors
using only `mu_0,...,mu_5`, (3.2) is the sole negative one; the other 22 are
strictly positive.  The normalized centered quadratic model therefore
**fails** the Stieltjes conditions at order 13.

## 4. Closed-form attempt

The neuron flow is integrable by quadrature.  On `v>0`,

\[
I=b^2-v+\log v
\tag{4.1}

is conserved.  Equivalently, for `q=log v`,

\[
q''=2(e^q-1),\qquad
q'^2=4(I+e^q-q).
\tag{4.2}

This gives each characteristic implicitly between its turning points, and

\[
F(t)=\frac14\frac d{dt}\mathbb E[b(t)^2].
\tag{4.3}

Equations (4.1)--(4.3) are a genuine per-neuron closed reduction, but the
Gaussian average over the random invariant and initial phase does not
collapse to an elementary scalar `F` or `K` in the calculation.  Since the
exact determinant (3.2) already decides the conjecture for this model, no
all-order positivity claim is possible.

For a bounded closed-form check, the exact Lie recurrence was extended
through \(F^{(81)}(0)\), giving forty output-kernel moments.  A fit using only
\(\mu_0,\ldots,\mu_{24}\) found neither an algebraic moment OGF of degree at
most four in the OGF and six in its argument nor a polynomial recurrence of
order/degree at most four.  Therefore there was no candidate to validate on
the sealed \(\mu_{25},\ldots,\mu_{39}\) range.  This rules out only those
predeclared low-complexity classes, not every possible special-function
formula.

The machine-readable derivatives, moments, and all 23 minors are in
[RESULTS.json](RESULTS.json).
