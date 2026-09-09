# Unconditional sharp general-time theorem for \(L=1\)

This is the branch in which no reused-matrix bridge is needed.

## Theorem

Let \(\phi\) satisfy the activation assumptions in
RESEARCH_CONTRACT.md, write \(M=M_\phi\), and set

\[
 \rho_\phi=\frac1{12M}.
\]

Let \(A,U\) be independent standard Gaussians and put

\[
 z(A,U)=6M e^{2M\rho_\phi}(1+|A|+|U|).                \tag{1.1}
\]

Use the Bell polynomials (5.2) of ABSTRACT_STEP_DOUBLING.md.  For
each \(z\ge1\), define the terminating recursion

\[
 R_1(z)=e^{z\rho_\phi}z,                              \tag{1.2}
\]

\[
 R_q(z)=e^{z\rho_\phi}\left[
 \rho_\phi z\sum_{p=2}^q
 B_{q,p}(R_1,\ldots,R_{q-p+1})
 +qz\sum_{p=1}^{q-1}
 B_{q-1,p}(R_1,\ldots,R_{q-p})
 \right],\quad2\le q\le5,                             \tag{1.3}
\]

\[
 q_\phi(A,U)=
 z(A,U)\sum_{r=1}^5\sum_{p=1}^r
 B_{r,p}(R_1,\ldots,R_{r-p+1}),                       \tag{1.4}
\]

where every \(R_j\) in (1.4) is evaluated at \(z(A,U)\).  Finally set

\[
 Q_{\phi,1}=\mathbb E q_\phi(A,U),\qquad
 B_{\phi,1}=\frac83Q_{\phi,1},\qquad
 h_{\phi,1}=\frac{\rho_\phi}{2}.                       \tag{1.5}
\]

These are finite, explicit activation-only quantities.  With
\(G\sim N(0,1)\), \(g=\phi(G)\), \(p=\phi'(G)\),
\(q=\phi''(G)\), \(r=\phi'''(G)\), define

\[
 \kappa_{\phi,1}
 =
 \frac32\mathbb E[p^3r+gp^2q]
 \mathrel{+}2\mathbb E[
 p^4+g^2p^2+2gp^2q+3p^2q^2].                         \tag{1.6}
\]

Then, for every integer \(t\ge1\) and every
\(|\eta|\le h_{\phi,1}/t\),

\[
 \boxed{
 \left|F_{2t,1}(\eta)-F_{t,1}(2\eta)
 -t(2t-1)\kappa_{\phi,1}\eta^3\right|
 \le B_{\phi,1}t^4|\eta|^5.}                          \tag{1.7}
\]

## Proof

At every width, the coordinates are iid copies of

\[
 A_{s+1}=A_s+h\phi(U_s),\qquad
 U_{s+1}=U_s+hA_s\phi'(U_s),                          \tag{2.1}
\]

and \(F_{k,1}(h)=\mathbb E[A_k\phi(U_k)]\).  Thus the width limit is
already exact at fixed \(h\).

Put \(x=(a,u)\),

\[
 f(x)=a\phi(u),\qquad
 V(x)=(\phi(u),a\phi'(u))=\nabla f(x).
\]

For a schedule \(\delta\), (2.1) is exactly
\(x_{s+1}=x_s+\delta_sV(x_s)\).  If
\(\|\delta\|_1\le\rho_\phi\) and
\[
 R_s=1+|A_s|+|U_s|,
\]
then
\[
 R_{s+1}\le(1+2M|\delta_s|)R_s,
\qquad
 R_s\le e^{2M\rho_\phi}(1+|A|+|U|).                  \tag{2.2}
\]

Entrywise differentiation shows, for \(0\le r\le5\) and
\(1\le j\le5\),

\[
 \|D^rV(x_s)\|\le6MR_s,\qquad
 \|D^jf(x_s)\|\le6MR_s.                              \tag{2.3}
\]

Indeed \(V=(\phi,a\phi')\): an \(r\)-th derivative contains at most
one factor \(a\), at most \(r\) placements of an \(a\)-derivative, and
one derivative of \(\phi\); the case \(r=0\) follows from linear
growth.  The same count applies to \(f=a\phi\), with its first
derivative using the linear-growth bound.  Equations (2.2)--(2.3)
give the samplewise majorant (1.1).

Apply the schedule-derivative proof in Section 5 of
ABSTRACT_STEP_DOUBLING.md for each fixed \((A,U)\), without replacing
its factor \(e^{K_1\rho}\) by a constant.  Equations (1.2)--(1.4) give

\[
 \|D_\delta^r f(x_m(\delta))\|_{(\ell^1)^r}
 \le q_\phi(A,U),\qquad1\le r\le5.                   \tag{2.4}
\]

The right side is integrable.  It is a finite sum of a polynomial in
\(1+|A|+|U|\) times
\(\exp\{c_\phi(1+|A|+|U|)\}\), and every such function has finite
two-dimensional Gaussian expectation.  The undifferentiated observable
also satisfies \(|f(x_s)|\le MR_s^2\), so it is covered by the same
Gaussian domination.  Dominated differentiation in
(2.4) therefore proves

\[
 \sup_m\sup_{\|\delta\|_1\le\rho_\phi}
 \|D_\delta^5\mathbb E f(x_m(\delta))\|
 \le Q_{\phi,1}.                                      \tag{2.5}
\]

Changing \((h,A)\) to \((-h,-A)\) in (2.1) leaves every \(U_s\)
unchanged and changes every \(A_s\) in sign.  Since \(A\) is symmetric,
every \(F_{k,1}\), and hence the step-doubling discrepancy, is odd.
The coupled defect lemma (3.4) now gives the right side of (1.7) whenever
\(2t|\eta|\le\rho_\phi\).

It remains only to identify the cubic coefficient.  For
\(V=\nabla f\), equations (4.6)--(4.9) of the same lemma give
\[
 [\eta^3]\{F_{2t,1}(\eta)-F_{t,1}(2\eta)\}
 =t(2t-1)\left(\frac12S_1+2H_1\right).
\]
Direct differentiation of \(f=a\phi(u)\), followed by the Gaussian
average over \(A\), gives
\[
 S_1=3\mathbb E[p^3r+gp^2q],
\]
\[
 H_1=\mathbb E[p^4+g^2p^2+2gp^2q+3p^2q^2].
\]
This is exactly (1.6), completing the proof.
