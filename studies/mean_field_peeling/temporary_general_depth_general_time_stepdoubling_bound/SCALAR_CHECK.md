# Exact one-hidden-layer check and sharpness

For \(L=1\), the width limit is unnecessary.  The network is

\[
 f_n(a,u)=\frac1n\sum_{i=1}^na_i\phi(u_i),
\]

and each coordinate follows the exact two-dimensional Euler recursion

\[
 A_{s+1}=A_s+h\phi(U_s),\qquad
 U_{s+1}=U_s+hA_s\phi'(U_s),                           \tag{1.1}
\]

with \((A_0,U_0)\) independent standard Gaussians.  Hence

\[
 F_{k,1}(h)=\mathbb E[A_k\phi(U_k)]                   \tag{1.2}
\]

for every width \(n\).

Let \(G\sim N(0,1)\), and abbreviate
\(g=\phi(G)\), \(p=\phi'(G)\), \(q=\phi''(G)\), and
\(r=\phi'''(G)\).  Direct differentiation of
\(f(a,u)=a\phi(u)\) in its gradient direction gives

\[
 S_1=3\mathbb E[p^3r+gp^2q],                           \tag{1.3}
\]

\[
 H_1=\mathbb E[p^4+g^2p^2+2gp^2q+3p^2q^2].           \tag{1.4}
\]

The abstract Euler algebra therefore yields the cubic coefficient

\[
 [h^3]\,\Delta_{t,1}(h)
 =t(2t-1)\left(\frac12S_1+2H_1\right).                \tag{1.5}
\]

This case has no reused-matrix response bridge, so (1.5) is
unconditional.

For the normalized linear activation \(\phi(x)=x\), diagonalizing (1.1)
with \(A_s\pm U_s\) gives

\[
 F_{k,1}(h)
 =\frac{(1+h)^{2k}-(1-h)^{2k}}2.                      \tag{1.6}
\]

Consequently,

\[
 \begin{aligned}
 \Delta_{t,1}(h)
 ={}&4t(2t-1)h^3\\
 &+\frac43t(t-1)(2t-1)(8t-9)h^5+O(h^7).
 \end{aligned}                                        \tag{1.7}
\]

The quintic coefficient in (1.7) has degree exactly four.  Therefore no
uniform theorem over this activation class can replace the \(t^4\)
factor by a polynomial of smaller degree.  This validates the proposed
powers but does not resolve the reused-matrix population-state bridge for
\(L\ge2\).

