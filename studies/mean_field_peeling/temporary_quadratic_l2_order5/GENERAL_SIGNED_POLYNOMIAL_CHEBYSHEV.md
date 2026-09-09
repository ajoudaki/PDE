# Signed polynomial activations: a scalar uniform-tail theorem

This note supersedes the unresolved scalar conclusion in Sections 4--5 of
`GENERAL_POLYNOMIAL_FROZEN_OBSTRUCTION.md`.  It does not supersede that
note's warning about transferring a frozen scalar comparison to the full
two-hidden-layer network when activation coefficients have arbitrary signs.

## Theorem

Let

\[
 \phi(x)=\sum_{k=0}^d c_kx^k,\qquad d\ge2,\qquad c_d>0,
 \qquad \mathbb E\phi(G)^2=1,
\]

where the lower coefficients may have arbitrary signs.  Starting from
independent standard Gaussians \(A_0,Z_0\), define

\[
 A_{n+1}=A_n+h\phi(Z_n),\qquad
 Z_{n+1}=Z_n+hA_n\phi'(Z_n),\qquad
 O_n=A_n\phi(Z_n),
\]

and

\[
 D_t(h)=\mathbb EO_{2t}(h)-\mathbb EO_t(2h).
\]

For every \(\rho>0\), every real sequence \((\kappa_t)\), and every fixed
\(q\in\mathbb R\),

\[
 \sup_{0\le h\le \rho/t}
 \left|D_t(h)-\kappa_t h^3\right|
 \not\le C t^q(\rho/t)^5
\]

for all \(t\), for any finite constant \(C\).  More strongly, the supremum
on the left tends to \(+\infty\) super-exponentially in \(t\).

Consequently, the proposed estimate

\[
 |D_t(h)-\kappa_t h^3|\le Ct^4|h|^5,
 \qquad |h|\le\rho/t,
\]

is false for the scalar frozen subsystem for every genuinely nonlinear
polynomial, regardless of the signs of its lower coefficients.

The theorem is about the supremum on the shrinking interval.  It does not
assert that the endpoint value \(D_t(\rho/t)\) diverges for an arbitrary
signed polynomial.

## 1. Degrees and the exact top coefficient

Put

\[
 \delta_N=\frac{d^N-1}{d-1},\qquad
 m_N=(d+1)\delta_N,
 \qquad r=d^{N-1},\quad s=d^N.
\]

The state coordinates after \(N\) steps have degree \(\delta_N\) in \(h\),
and \(O_N\) has degree at most \(m_N\).  Define the homogeneous maps

\[
 H(a,z)=(c_dz^d,dc_daz^{d-1}),\qquad P(a,z)=c_daz^d.
\]

A direct induction gives

\[
 P\circ H^{N-1}(a,z)=C_Na^rz^s,                 \tag{1}
\]

where

\[
 C_N=c_d^{Q_N}d^{R_N},\qquad
 Q_N=\frac{(d+1)d^{N-1}-2}{d-1},\qquad
 R_N=\frac{d(d^{N-1}-1)}{d-1}.                  \tag{2}
\]

Indeed, \(C_1=c_d\), and composition with \(H\) sends

\[
 C_Na^rz^s
 \mapsto C_Nc_d^{r+s}d^s a^s z^{dr+(d-1)s};
\]

the exponent row \((r,s)\) becomes \((s,ds)\), and summing the added
exponents of \(c_d\) and \(d\) gives (2).

The coefficient of the maximal power is therefore exactly

\[
 [h^{m_N}]\mathbb EO_N
 =C_N\,\mathbb EA_0^s\,
   \mathbb E\!\left[\phi(G)^r\phi'(G)^s\right].  \tag{3}
\]

If \(d\) is even, \(r,s\) are even, so the two factors in (3) are strictly
positive.  Thus \(\mathbb EO_N\) has exact degree \(m_N\).

## 2. The exact parity-repaired coefficient for odd degree

Suppose now that \(d\) is odd.  Then (3) vanishes because \(s\) is odd.
We compute the entire coefficient one order below it, including every
possible source of that order.

Write the leading and first subleading state coefficients as

\[
 A_n=h^{\delta_n}a_n+h^{\delta_n-1}\widetilde a_n+\cdots,
 \qquad
 Z_n=h^{\delta_n}z_n+h^{\delta_n-1}\widetilde z_n+\cdots.
\]

At the first step,

\[
 (a_1,z_1)=(\phi(Z_0),A_0\phi'(Z_0)),\qquad
 (\widetilde a_1,\widetilde z_1)=(A_0,Z_0).       \tag{4}
\]

For every transition after the first, a lower outer activation monomial
loses at least \(\delta_n>1\) powers of \(h\).  Hence, after step two, a
one-degree deficit can only propagate through the derivative of \(H\).
At the first-to-second transition there is one additional source, namely
the degree-\((d-1)\) outer monomial:

\[
 K(a,z)=\big(c_{d-1}z^{d-1},(d-1)c_{d-1}az^{d-2}\big).          \tag{5}
\]

Likewise, for \(N\ge2\), a lower monomial in the terminal observable loses
\(\delta_N>1\) powers and cannot enter the coefficient \(m_N-1\).  Thus the
complete coefficient is the sum of

* the derivative of (1) in the old-state direction \((A_0,Z_0)\); and
* the derivative of \(P\circ H^{N-2}\) in the direction (5).

No other source has the required degree.  Substituting (1) into these two
derivatives, and using \(s=dr\), gives the exact random coefficient

\[
 C_N\left[
 rA_0a_1^{r-1}z_1^s+sZ_0a_1^rz_1^{s-1}
 +r\frac{c_{d-1}}{c_d}a_1^rz_1^{s-1}
 \right].                                                        \tag{6}
\]

For completeness, the coefficient in the last term is exact.  If
\(P\circ H^{N-2}=C_{N-1}a^uz^v\), then \(v=du=r\).  Differentiating in the
direction (5) and factoring
\(C_N=C_{N-1}c_d^u(dc_d)^v\) produces

\[
 c_{d-1}\left(\frac{u}{c_d}
 +\frac{v(d-1)}{dc_d}\right)
 =r\frac{c_{d-1}}{c_d}.                         \tag{7}
\]

Let \(a=c_{d-1}/c_d\).  Since
\(\mathbb EA_0^{s+1}=s\mathbb EA_0^{s-1}\), taking expectation in (6)
yields

\[
\begin{split}
 L_N &:=[h^{m_N-1}]\mathbb EO_N\\
 &=C_N\mathbb EG^{s-1}\,
 \mathbb E\!\left[
 \phi(G)^{r-1}\phi'(G)^{s-1}
 \{rs\phi'(G)+(sG+ra)\phi(G)\}
 \right]                                                   \\[2mm]
 &=sC_N\mathbb EG^{s-1}\,
 \mathbb E\!\left[
 \phi(G)^{r-1}\phi'(G)^{s-1}
 \{r\phi'(G)+(G+a/d)\phi(G)\}
 \right].                                                   \tag{8}
\end{split}
\]

Formula (8) is the full \(m_N-1\) coefficient, not a selected branch.

We next prove that it is positive for every sufficiently large \(N\).
Choose an explicit \(R\ge\max\{1,2|a|/d\}\) so large that, for
\(|x|\ge R\),

\[
 |\phi(x)|\ge\frac{c_d}{2}|x|^d,qquad
 \phi'(x)\ge\frac{dc_d}{2}|x|^{d-1},qquad
 x\phi(x)\ge\frac{c_d}{2}|x|^{d+1}.             \tag{9}
\]

Such an \(R\) is computable from the coefficients, for example by requiring
the sum of every lower-term absolute bound to be at most half the leading
term in each of \(\phi\) and \(\phi'\).  On this tail,

\[
 (x+a/d)\phi(x)\ge\frac12x\phi(x)
 \ge\frac{c_d}{4}|x|^{d+1},                      \tag{10}
\]

and \(r\phi'(x)\ge0\).  Since \(r-1,s-1\) are even, the integrand in (8)
is bounded below on the tail by

\[
 \frac{sc_d}{4}
 \left(\frac{c_d}{2}\right)^{r-1}
 \left(\frac{dc_d}{2}\right)^{s-1}|x|^K,
 \qquad K=ds-d+2.                                \tag{11}
\]

The integer \(K\) is even.  Put

\[
 U=\max\left\{1,\sup_{|x|\le R}|\phi(x)|,
                  \sup_{|x|\le R}|\phi'(x)|\right\}.
\]

The absolute contribution from \(|G|<R\) is at most

\[
 Q_s=s(s+R+|a|)U^{r+s-1}.                         \tag{12}
\]

For every even \(K\),

\[
 \mathbb E|G|^K=\frac{K!}{2^{K/2}(K/2)!}
 \ge\left(\frac{K}{e^2}\right)^{K/2}.           \tag{13}
\]

Here \(K!\ge(K/e)^K\), obtained by integrating \(\log x\), and
\((K/2)!\le(K/2)^{K/2}\).  If

\[
 K\ge 2e^2\max\{R^2,1\},                         \tag{14}
\]

then \(R^K\le\tfrac12(K/e^2)^{K/2}\), and hence

\[
 \mathbb E[|G|^K\mathbf1_{\{|G|\ge R\}}]
 \ge\frac12\left(\frac{K}{e^2}\right)^{K/2}.   \tag{15}
\]

To make the eventual quantifier explicit, put

\[
\begin{split}
 B_1={}&\frac1d\left|\log\frac{c_d}{2}\right|
       +\left|\log\frac{dc_d}{2}\right|
       +\left|\log\frac{c_d}{8}\right|,\\
 B_2={}&B_1+\frac d4\left|\log\frac d2-2\right|,\\
 B_3={}&3+\left(1+\frac1d\right)\log U .          \tag{16}
\end{split}
\]

Choose \(S_0\) larger than

\[
 2,\quad R+|a|,\quad \frac{2e^2\max\{R^2,1\}+d-2}{d},\quad
 \frac{2e}{d},\quad
 \exp\!\left(\frac{4(B_2+B_3+1)}d\right),        \tag{17}
\]

and let \(N_0(\phi)=\max\{2,\lceil\log_d S_0\rceil\}\).  This is a
finite formula in the activation coefficients.  Indeed, for every
\(s=d^N\ge S_0\), the logarithm of the tail lower bound obtained from
(11) and (15) is at least

\[
 \frac d4s\log s-B_2s.                            \tag{18}
\]

To see this, use \(K\ge ds/2\), the fact that
\(x(\log x-2)\) is increasing for \(x\ge e\), and bound every possibly
negative activation logarithm by its absolute value times \(s\).  On the
other hand, because \(s\ge R+|a|\), (12) gives

\[
 \log(2Q_s)\le(B_3+1)s.                           \tag{19}
\]

The last condition in (17) makes (18) at least (19).  Consequently the
positive tail is at least twice the absolute compact contribution for
every \(N\ge N_0(\phi)\).  Equations (11)--(19) prove \(L_N>0\) for all
such \(N\), with a completely explicit lower bound.

Thus, for odd \(d\), \(\mathbb EO_N\) has exact degree \(m_N-1\) for all
sufficiently large \(N\).

## 3. Chebyshev prevents cancellation on the whole shrinking interval

We use the following exact extremal inequality.  If a real polynomial
\(P\) has degree \(M\) and leading coefficient \(b_M\), then, for every
\(H>0\),

\[
 \sup_{0\le h\le H}|P(h)|
 \ge 2^{1-2M}|b_M|H^M.                            \tag{20}
\]

To prove it, set \(Q(x)=P(H(x+1)/2)\).  Its leading coefficient is
\(b_M(H/2)^M\).  The monic Chebyshev extremal inequality on \([-1,1]\)
says that a degree-\(M\) polynomial with leading coefficient \(b\) has
supremum norm at least \(|b|/2^{M-1}\).  Applying it to \(Q\) gives (20).
The monic inequality follows from the alternation points of \(T_M\): if a
monic polynomial had smaller norm than \(2^{1-M}\), subtracting the monic
polynomial \(2^{1-M}T_M\) would have alternating signs at \(M+1\) points
and hence at least \(M\) roots, impossible for a polynomial of degree at
most \(M-1\).

Take \(N=2t\), \(H=\rho/t\), and

\[
 R_t(h)=D_t(h)-\kappa_th^3.
\]

The coarse term has degree at most \(m_t<m_{2t}-1\), and subtracting a
cubic cannot affect the high coefficient.  Therefore the degree and leading
coefficient of \(R_t\) are

\[
 (M_t,b_t)=
 \begin{cases}
 (m_{2t},[h^{m_{2t}}]\mathbb EO_{2t}),&d\text{ even},\\
 (m_{2t}-1,L_{2t}),&d\text{ odd and }2t\ge N_0(\phi).
 \end{cases}                                      \tag{21}
\]

In the even case, choose \(R\) so that the first two inequalities in (9)
hold.  Because \(r,s\) are even, (3), (9), and (15), now with
\(K=ds=d^{2t+1}\), give

\[
 b_t\ge
 \frac{C_{2t}}2
 \left(\frac{s}{e^2}\right)^{s/2}
 \left(\frac{c_d}{2}\right)^r
 \left(\frac{dc_d}{2}\right)^s
 \left(\frac{ds}{e^2}\right)^{ds/2}              \tag{22}
\]

for all sufficiently large \(t\).  In the odd case, (8)--(19), together
with (13) for \(\mathbb EG^{s-1}\), gives the same logarithmic lower rate.
Since \(C_{2t}\) in (2) costs or contributes only \(\exp(O_\phi(s))\), in
both cases

\[
 \log b_t\ge\frac{d+1}{2}s\log s-O_\phi(s),
 \qquad s=d^{2t}.                                 \tag{23}
\]

Combining (20)--(23), and using
\(M_t=(d+1)(s-1)/(d-1)+O(1)\), yields

\[
\begin{split}
 \log\sup_{0\le h\le\rho/t}|R_t(h)|
 &\ge \frac{d+1}{2}s\log s-M_t\log t-O_{\phi,\rho}(s)\\
 &\ge (d+1)s\,t\log d
 -\frac{d+1}{d-1}s\log t-O_{\phi,\rho}(s),       \tag{24}
\end{split}
\]

which tends to \(+\infty\).

On the other hand, an estimate

\[
 |R_t(h)|\le Ct^q|h|^5,\qquad 0\le h\le\rho/t,
\]

would imply

\[
 \sup_{0\le h\le\rho/t}|R_t(h)|
 \le C\rho^5t^{q-5},                              \tag{25}
\]

only polynomial growth.  Equations (24) and (25) contradict one another.
This proves the theorem.

## 4. Exact scope: scalar versus the full two-hidden-layer network

The argument above proves a signed-coefficient theorem for the frozen
two-dimensional subsystem.  It does **not** by itself compare that subsystem
with the complete \(L=2\) OMFP DAG.  With nonnegative activation
coefficients, deletion of the bottom update is coefficientwise monotone, so
the scalar lower bound transfers to the full network.  Normalized monomials
and shifted powers also transfer by the positivity/sign-conjugacy arguments
already recorded in `GENERAL_POLYNOMIAL_FROZEN_OBSTRUCTION.md`.

For a general signed polynomial there is no proved order relation between
the full output and the frozen output.  The full network can contain
additional high-degree terms of either sign, and Chebyshev must be applied
to a nonzero high coefficient of the **full** width-first polynomial, not
to a coefficient of an un-ordered subsystem.  The fixed-\(h\) NETSOR bridge
identifies either polynomial but does not prevent their algebraic
cancellation.

Therefore:

* the uniform \(t^4h^5\) theorem is rigorously false for every signed
  polynomial in the frozen scalar model;
* it is rigorously false for the full \(L=2\) model for the previously
  proved nonnegative, monomial, shifted-power, and quadratic classes;
* for a completely arbitrary signed polynomial, transfer of this new
  scalar obstruction to the full \(L=2\) model remains open.

No claim about the general signed full network is made without that missing
bridge.
