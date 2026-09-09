# Adversarial audit of UNIFORM_L1.md

## Verdict

**PASS.** Under (1.1), the one-hidden-layer actual-network theorem
(1.22) is unconditional. The proof respects the width-first order, its
constant is activation-envelope-defined, and no trained-output
regularity is assumed. The checks below target possible failures of the
exact factorization, path count, differentiation under expectation, and
cubic coefficient.

## 1. Width-first order

At \(L=1\), neuron pairs never interact:

\[
(a_i,u_i)^+=(a_i+h\phi(u_i),\,u_i+ha_i\phi'(u_i)).
\]

They remain iid at every finite horizon, and

\[
\mathbb E f_{n,1}^N=\mathbb E[a_N\phi(u_N)]
\]

for every \(n\), not merely asymptotically. Linear growth gives an
integrable quadratic bound on the terminal summand. Hence the fixed-\(h\)
width identification is exact before the proof differentiates anything.
There is no limit interchange.

## 2. Exact local defect and telescoping order

For \(E_h=I+hg\), \(C_h=E_{2h}\), and \(B_h=E_h^2\),

\[
B_hz-C_hz
=h\{g(z+hg(z))-g(z)\}
=h^2\int_0^1Dg(z+shg(z))g(z)\,ds.
\]

The hybrids

\[
H_q=f\!\left(B_h^q(C_h^{t-q}z)\right)
\]

have \(H_0=f(C_h^tz)\), \(H_t=f(B_h^tz)\), and

\[
H_q-H_{q+1}
=(f\circ B_h^q)(C_hx_q)-(f\circ B_h^q)(B_hx_q),
\quad x_q=C_h^{t-1-q}z.
\]

The segment integral therefore has the negative sign in (3.5), and
\(f(C_h^tz)-f(B_h^tz)=h^2Q_t(h,z)\) exactly. No commutation of \(B_h\)
and \(C_h\) is used.

## 3. State envelope and interpolation

With \(R(z)=1+\|z\|_1\),

\[
R(E_{\alpha h}z)\le(1+\alpha M|h|)R(z).
\]

The two local-defect endpoints are genuine variable-step Euler paths and
are bounded by \(e^{4M|h|t}R(z_0)\). Their convex interpolation has the
same bound because \(R\) is convex. Restarting the Euler estimate for the
post-defect path multiplies by at most \(e^{2M|h|t}\). Thus the displayed
\(e^{6M|h|t}\) is valid even though the interpolation itself is not an
Euler step. At \(c_\phi=1/(16M)\), this is below \(2R(z_0)\).

This rules out the possible loophole that the proof silently treats the
defect interpolation as part of one Euler trajectory.

## 4. Derivative envelopes

For \(0\le q\le4\), differentiation of

\[
g(a,u)=(\phi(u),a\phi'(u))
\]

gives

\[
\|D^qg(a,u)\|_{\ell^1\to\ell^1}\le6MR(a,u).
\]

The largest derivative required is \(D^4g\), whose only potentially
unbounded term is \(a\phi^{(5)}(u)\). It is covered by (1.1). Likewise,
\(\|D^qf\|\le5MR\) for \(1\le q\le4\). On every relevant point both are
bounded by \(K(r)=12Mr\).

The homogeneous tangent products before and after the defect are bounded
by \(P(r)=e^{4c_\phi K(r)}=e^{3r}\). Re-deriving the first three
parameter derivatives of an Euler step gives exactly (4.10)--(4.12).
After division by \(t,t^2,t^3\), respectively:

- the sums without \(h\) contribute \(4,8,12\);
- the sums carrying \(h\) contribute \(4c_\phi\);
- post-defect sums replace \(4\) by \(2\);
- differentiating the transported tangent produces the two terms in
  (1.16).

Consequently each local defect has third derivative at most
\(6\mathcal C_M(r)t^3\), and summing the \(t\) defects gives precisely
\(6\mathcal C_M(r)t^4\). No fifth derivative of the output is invoked.

## 5. Differentiation under the Gaussian expectation

Equations (4.20a)--(4.20b), not merely the third-derivative estimate,
give a single envelope for derivative orders \(0,1,2,3\). Every entry of
the finite recursion is a polynomial with nonnegative coefficients in

\[
K(r)=12Mr,\qquad P(r)=e^{3r},\qquad c_\phi.
\]

It is therefore bounded by a polynomial in \(r\) times \(e^{Cr}\), for
some finite numerical \(C\) read from the displayed finite expression.
For \(r=1+|A|+|U|\), all such functions are integrable because Gaussian
tails dominate every linear exponential times a polynomial. The
parameter-differentiation theorem under an integral applies successively
through order three on the whole closed interval. Hence (5.2) is
justified and is not assumed output regularity.

## 6. Parity and coefficient

The source transformation

\[
(h,A,U)\mapsto(-h,-A,U)
\]

leaves \(u_s\) fixed, negates \(a_s\), and preserves the Gaussian law.
Thus the expected discrepancy is odd. Parity is used only after
expectation; no false pointwise parity claim is made.

For \(f(a,u)=a\phi(u)\), \(g=\nabla f\). Direct differentiation gives

\[
\mathsf S=\mathbb ED^3f[g,g,g]=3(j+m),
\]

\[
\mathsf H=\mathbb E\|Dg[g]\|_2^2=u+\ell+2m+3e.
\]

The Euler-jet sums yield (6.5), and direct polynomial substitution gives

\[
\frac{8F_{t,1}^{(3)}(0)-F_{2t,1}^{(3)}(0)}6
=-\frac{t(2t-1)}2(\mathsf S+4\mathsf H).
\]

Thus the coefficient is the explicit Gaussian integral (1.20), rather
than a definition through an unknown output derivative.

## 7. Falsification checks

- If \(\phi\equiv\pm1\), both the discrepancy and \(J_{\phi,1}\) vanish.
- If \(\phi(x)=x\),

  \[
  F_{N,1}(h)=\frac{(1+h)^{2N}-(1-h)^{2N}}2.
  \]

  Its discrepancy has cubic coefficient \(-4t(2t-1)\). Formula (1.20)
  gives \(J_{x,1}=8\), so the theorem agrees exactly. Its fifth
  coefficient is

  \[
  -\frac43t(t-1)(2t-1)(8t-9),
  \]

  confirming both the sign convention and the sharp \(t^4\) power.

No failed bridge remains at \(L=1\). The obstruction identified for
reused-matrix depths begins only at \(L\ge2\).

