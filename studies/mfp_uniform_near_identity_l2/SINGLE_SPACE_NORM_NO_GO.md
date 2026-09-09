# No-go theorem for the requested single reachable-source norm

Date: 25 August 2026.

## 1. Statement

Let \((\Omega,\mathcal F,\mathbb P)\) carry a standard Gaussian \(G\).  Fix
positive weights \(w_m\) and exponents \(p_m\in[1,\infty]\), and suppose

\[
 \|V\|_{\mathfrak X}
 =\sum_{m\ge0}w_m\|\mathcal D^mV\|_{p_m}
 \tag{1.1}
\]

is a norm on a vector space \(\mathfrak X\) which contains the constants and
the raw Gaussian \(G\).  Assume pointwise multiplication is quantitatively
closed on this same space, in the sense needed for a one-step Banach
estimate:

\[
 \|UV\|_{\mathfrak X}
 \le C_\times\|U\|_{\mathfrak X}\|V\|_{\mathfrak X}
 \qquad(U,V\in\mathfrak X)
 \tag{1.2}
\]

for some finite \(C_\times\).  Then no such \(\mathfrak X\) exists.

This conclusion is independent of the definition of the higher source
derivatives \(\mathcal D^m\), their tensor aggregation, and the weights
\(w_m\) for \(m\ge1\).  The obstruction is already in the value term
\(m=0\).

## 2. Proof

Because constants have zero source derivatives of positive order, (1.1) is
a norm only if \(w_0>0\).  If \(p_0=\infty\), then
\(\|G\|_{p_0}=\infty\), contradicting \(G\in\mathfrak X\).  Hence
\(1\le p_0<\infty\).

Iterating (1.2) gives, for every integer \(n\ge1\),

\[
 \|G^n\|_{\mathfrak X}
 \le C_\times^{n-1}\|G\|_{\mathfrak X}^n.
 \tag{2.1}
\]

On the other hand, the zeroth summand in (1.1) gives

\[
 \|G^n\|_{\mathfrak X}
 \ge w_0\|G^n\|_{p_0}
 =w_0\|G\|_{np_0}^{n}.
 \tag{2.2}
\]

For \(q\ge2\), the exact Gaussian moment is

\[
 \mathbb E|G|^q
 =\frac{2^{q/2}\Gamma((q+1)/2)}{\sqrt\pi}.
 \tag{2.3}
\]

Stirling's lower inequality applied to (2.3) gives a numerical
\(c_G>0\) such that

\[
 \|G\|_q\ge c_G\sqrt q,
 \qquad q\ge2.
 \tag{2.4}
\]

For all sufficiently large \(n\), combine (2.1), (2.2), and (2.4), then
take \(n\)-th roots:

\[
 w_0^{1/n}c_G\sqrt{np_0}
 \le C_\times^{1-1/n}\|G\|_{\mathfrak X}.
 \tag{2.5}
\]

The left side tends to infinity and the right side remains bounded.  This
is a contradiction. \(\square\)

## 3. Reachable-source and one-step consequences

The width-first OMFP DAG contains standard Gaussian endpoint and raw-source
fields at initialization.  Therefore a norm used to estimate the actual
DAG must contain such a \(G\).  If the requested phrase “closure under
products” means only algebraic membership, without a finite quantitative
estimate such as (1.2), it cannot be used to prove the requested one-step
bound or any explicit recursion.  A locally bounded bilinear product on a
normed vector space is equivalent, after rescaling the neighborhood, to an
estimate of the form (1.2), so weakening “bounded” to “continuous” does not
evade the theorem.

The same obstruction appears directly in the genuine nonlinear tangent.
At initialization the derivative of

\[
 \delta=a\psi_\alpha'(z)
\]

in a preactivation direction \(v\) contains

\[
 a\psi_\alpha''(z)v.
 \tag{3.1}
\]

For every \(\alpha\ne0\) with \(\varphi''\not\equiv0\), the multiplier
\(a\psi_\alpha''(z)\) contains the independent standard Gaussian readout
field \(a\), multiplied by a bounded coefficient which is nonzero on a set
of positive probability.  This exhibits the unbounded coefficient that a
candidate tangent theory must handle.  It does not, by itself, isolate a
bounded copy of Gaussian multiplication inside the full block operator
\(Dg(\theta_0)\): that stronger conclusion would require bounded component
inclusions/projections and a range theorem for the reachable directions.
The product-algebra contradiction in Section 2 is independent of this
observation and needs no such isolation claim.

## 4. What the theorem does and does not refute

The theorem refutes the requested **single-space** analytic Banach-algebra
architecture and therefore blocks items 2--4 of the requested proof as
stated.  It does not disprove the scalar estimate

\[
 |\Delta_t(\eta)-\kappa_t\eta^3|
 \le Ct^4|\eta|^5.
\]

A radius-loss scale \(\mathfrak X_R\to\mathfrak X_r\), \(r<R\), can allow
pointwise multiplication or Gaussian creation at the price of analytic
radius.  Such a scale is not the same-space norm or the same-space one-step
estimate demanded in the question, and its required chronological
radius-recovery theorem is not currently proved by OMFP.
