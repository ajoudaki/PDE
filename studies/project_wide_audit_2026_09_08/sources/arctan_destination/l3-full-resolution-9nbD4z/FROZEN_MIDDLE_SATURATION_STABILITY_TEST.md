# Frozen-middle saturation: a sharp finite-time RMS modulus

Scope: one exact lemma for the stated autonomous, frozen-upper-parameter subflow with fixed positive scalar \(c_1\). Classification: **no canonical continuation progress**. No estimate for full feedback or moving \(h^{(1)}\) is established; no prior full-feedback identities are used or reviewed.

The endpoint map has a width-uniform modulus of order \(d^{3/5}\) on RMS-bounded initial sets. This exponent is optimal under the stated assumptions, even for a rank-one frozen \(W^{(3)}\). The proof requires neither small initial natural-coordinate differences nor initial \(L^6\) bounds.

## Setup and statement

For \(v\in\mathbb R^n\), write

\[
 \|v\|_{p,n}=\left(n^{-1}\sum_{i=1}^n|v_i|^p\right)^{1/p}.
\]

Let \(A=W^{(3)}\in\mathbb R^{m\times n}\), \(b=W^{(4)}\in\mathbb R^m\), and apply scalar functions componentwise. Assume

\[
 \|A\|_{\ell^2\to\ell^2}\le K,\qquad \|b\|_\infty\le B,
 \qquad \sup_z\|q(z)\|_{2,n}\le Q,
\]
\[
 q(z)=A^T[b\odot\phi'(A\phi(z))],\qquad \phi(s)=\arctan s,
 \qquad z'=c_1\phi'(z)\odot q(z).
\]

Here \(K,B,Q\ge0\) and \(c_1>0\) are fixed independently of \(n,m\). The bound \(Q\) is the uniform RMS forcing bound stipulated in the question. With ordinary Euclidean operator norms, the matrix bounds give \(\sup_z\|q(z)\|_{2,n}\le KB\sqrt{m/n}\): equal widths allow \(Q=KB\), while arbitrary aspect ratios require the separately stated uniform \(Q\) bound. A uniform bound in unnormalized Euclidean norm also implies the required RMS bound.

Since \(|\phi'|\le1\) and

\[
 |\phi''(s)|=\frac{2|s|}{(1+s^2)^2}\le1,
\]

successive application of the scalar Lipschitz bounds and the two matrix operator bounds gives

\[
 \|q(z)-q(w)\|_{2,n}\le K^2B\|z-w\|_{2,n}.
\]

Put \(L=K^2B\), and let \(S_t x\) be the solution with initial state \(x\). Both solutions compared below use exactly the same \(A,b,c_1\).

**Lemma.** For every finite \(n,m\ge1\), every admissible frozen pair \(A,b\), every \(x,y\in\mathbb R^n\), and every \(T\ge0\), with \(d=\|x-y\|_{2,n}\),

\[
 \sup_{0\le t\le T}\|S_t x-S_t y\|_{2,n}
 \le e^{c_1LT}\left[2d+24(c_1QT)^{2/5}d^{3/5}\right]. \tag{1}
\]

On \(\|x\|_{2,n},\|y\|_{2,n}\le R\), this is a uniform \(3/5\)-Hölder bound with coefficient

\[
 e^{c_1LT}\left[2(2R)^{2/5}+24(c_1QT)^{2/5}\right]. \tag{2}
\]

Bound (1) itself requires no bound on the initial RMS. The displacement also satisfies

\[
 \|S_t x-x\|_{6,n}\le(12c_1Qt)^{1/3}. \tag{3}
\]

## Proof

First bound how one scalar natural-coordinate translation transports an initial perturbation. Hölder's inequality then converts this to RMS using RMS cumulative forcing. Finally control the difference between the two cumulative forcings using \(L\).

Let \(F(s)=s+s^3/3\), and \(g=F^{-1}\). Since \(F'>0\) and \(F(s)\to\pm\infty\) as \(s\to\pm\infty\), \(g\) is defined on all of \(\mathbb R\). For \(r\ge s\), with \(D=r-s\),

\[
 F(r)-F(s)
 =D\left[1+\left(\frac{r+s}{2}\right)^2+\frac{D^2}{12}\right]
 \ge D+\frac{D^3}{12}. \tag{4}
\]

Consequently \(g\) is 1-Lipschitz and

\[
 |g(F(a)+u)-a|\le(12|u|)^{1/3}. \tag{5}
\]

For this frozen subflow, \(u(t)=F(z(t))\) solves \(u'=c_1q(g(u))\). Its right-hand side is globally \(c_1L\)-Lipschitz and bounded in RMS by \(c_1Q\). To verify global existence directly, use the integral iteration
\(u^{(0)}(t)=F(x)\),
\(u^{(k+1)}(t)=F(x)+c_1\int_0^tq(g(u^{(k)}(s)))\,ds\).
Induction bounds consecutive differences by

\[
 c_1Q\frac{(c_1L)^kt^{k+1}}{(k+1)!},\qquad k\ge0.
\]

This series converges uniformly on every finite time interval; Lipschitz continuity permits passage to its integral limit. The integral comparison below gives uniqueness. No uniform bound on \(\|F(x)\|_{2,n}\) is needed for this construction.

Write

\[
 S_t x=g(F(x)+U(t)),\qquad
 U(t)=c_1\int_0^tq(S_s x)\,ds,\qquad
 \|U(t)\|_{2,n}\le c_1Qt. \tag{6}
\]

Raising (5) to the sixth power and averaging gives

\[
 \|S_t x-x\|_{6,n}^6\le144\|U(t)\|_{2,n}^2,
\]

which proves (3). This controls the increment and assumes no uniform initial \(L^6\) bound.

We next prove the scalar translation estimate

\[
 |g(F(a)+u)-g(F(b)+u)|
 \le2|a-b|+24|a-b|^{3/5}|u|^{2/5}. \tag{7}
\]

Exchange \(a,b\) if necessary to take \(a\ge b\). Put \(d_0=a-b\), \(r=g(F(a)+u)\), \(s=g(F(b)+u)\), \(D=r-s\ge0\), \(\mu=(a+b)/2\), \(\nu=(r+s)/2\), and \(H=(12|u|)^{1/3}\). If \(d_0=0\), then \(D=0\). Otherwise (5) gives \(|\mu-\nu|\le H\), hence \(\mu^2\le2\nu^2+2H^2\). Equal translations and (4) give

\[
 D(1+\nu^2+D^2/12)
 =d_0(1+\mu^2+d_0^2/12)
 \le d_0(1+2\nu^2+2H^2+d_0^2/12).
\]

If \(D<2d_0\), (7) already holds. If \(D\ge2d_0\), rearrangement yields

\[
 (D-d_0)+(D-2d_0)\nu^2+\frac{D^3-d_0^3}{12}
 \le2d_0H^2,
\]
\[
 \frac D2+\frac{7D^3}{96}\le2d_0H^2,
 \qquad D+D^3\le32d_0H^2.
\]

For \(0\le D\le1\), \(D^{5/3}\le D\); for \(D\ge1\), \(D^{5/3}\le D^3\). Therefore

\[
 D\le(32d_0H^2)^{3/5}
 =8\,12^{2/5}d_0^{3/5}|u|^{2/5}
 \le24d_0^{3/5}|u|^{2/5},
\]

where \(12^{2/5}\le3\) follows from \(144\le243\). This proves (7), including \(u=0\).

For vectors, let \(T_U(x)=g(F(x)+U)\). Applying (7) componentwise, then the RMS triangle inequality and Hölder's inequality with exponents \(5/3,5/2\), gives

\[
 \|T_U(x)-T_U(y)\|_{2,n}
 \le2d+24d^{3/5}\|U\|_{2,n}^{2/5}. \tag{8}
\]

Indeed,

\[
 n^{-1}\sum_i|x_i-y_i|^{6/5}|U_i|^{4/5}
 \le\left(n^{-1}\sum_i|x_i-y_i|^2\right)^{3/5}
      \left(n^{-1}\sum_i|U_i|^2\right)^{2/5}.
\]

Let \(V(t)=c_1\int_0^tq(S_s y)\,ds\) and \(E(t)=\|S_t x-S_t y\|_{2,n}\). Insert \(T_{U(t)}(y)\) between the two endpoints. Since \(g\) is 1-Lipschitz, (6), (8), and the Lipschitz bound on \(q\) give

\[
 E(t)\le2d+24d^{3/5}(c_1Qt)^{2/5}
             +c_1L\int_0^tE(s)\,ds. \tag{9}
\]

For fixed \(T\), denote the first two terms with \(t=T\) by \(M\), and put \(\lambda=c_1L\). On \([0,T]\), set \(h(t)=M+\lambda\int_0^tE(s)\,ds\). Then \(E\le h\), \(h'\le\lambda h\), and \((e^{-\lambda t}h(t))'\le0\). Thus \(E(t)\le Me^{\lambda t}\), proving (1). This same calculation with \(M=0\) proves the uniqueness used above. Finally \(d\le2R\) implies \(2d\le2(2R)^{2/5}d^{3/5}\), proving (2).

## Exact sharpness within the retained upper-layer structure

Fix any \(c_1>0\) and \(T>0\). For each width \(n=m\), choose

\[
 A_n=n^{-1/2}{\bf1}_n e_1^T,\qquad b_n=-{\bf1}_n.
\]

Here \(e_1\) is the first coordinate vector. These choices have \(\|A_n\|_{2\to2}=1\), \(\|b_n\|_\infty=1\), and exactly

\[
 q_n(z)=-\frac{\sqrt n}{1+\phi(z_1)^2/n}\,e_1,
 \qquad \|q_n(z)\|_{2,n}\le1.
\]

Only the first coordinate moves. Define the strictly increasing, onto scalar function

\[
 H_n(s)=\int_0^s(1+r^2)\left(1+\frac{\arctan(r)^2}{n}\right)dr.
\]

The scalar equation gives \(H_n(z_1(t))=H_n(z_1(0))-c_1\sqrt n\,t\). Set

\[
 a_n=H_n^{-1}(c_1T\sqrt n),\qquad
 r_n=H_n^{-1}(c_1T\sqrt n+H_n(1)),\qquad
 x_n=a_ne_1,\quad y_n=r_ne_1.
\]

Their time-\(T\) endpoints are exactly \(0\) and \(e_1\). For \(s\ge0\),

\[
 F(s)\le H_n(s)\le\left(1+\frac{\pi^2}{4n}\right)F(s).
\]

Hence \(H_n(1)\to4/3\), and \(F(a_n),F(r_n)\sim c_1T\sqrt n\). Both initial scalar values tend to infinity; using \(F(s)/(s^3/3)\to1\) gives

\[
 a_n\sim r_n\sim a_*n^{1/6},\qquad a_*=(3c_1T)^{1/3}.
\]

The mean value identity \(H_n(1)=H_n'(\xi_n)(r_n-a_n)\), with \(\xi_n\) between these two values, gives \(H_n'(\xi_n)\sim a_*^2n^{1/3}\). Consequently

\[
 \|x_n\|_{2,n}\sim\|y_n\|_{2,n}\sim a_*n^{-1/3},
 \qquad d_n:=\|x_n-y_n\|_{2,n}
       \sim\frac{4}{3a_*^2}n^{-5/6},
\]
\[
 \|S_Tx_n-S_Ty_n\|_{2,n}=n^{-1/2}.
\]

For every fixed \(R>0\), both initial states eventually lie in the RMS ball of radius \(R\). For every \(\alpha>3/5\), their endpoint difference divided by \(d_n^\alpha\) diverges like \(n^{(5\alpha-3)/6}\). Thus no width-uniform Hölder estimate with exponent greater than \(3/5\), including a Lipschitz estimate, follows from these assumptions. This is an exact frozen-network example, not an externally prescribed forcing example.

## Natural-coordinate metric and limits of scope

The natural-coordinate metric \(D_F(x,y)=\|F(x)-F(y)\|_{2,n}\) separately satisfies

\[
 D_F(S_t x,S_t y)\le e^{c_1Lt}D_F(x,y).
\]

Indeed the two natural-coordinate solutions satisfy the integral inequality with initial term \(D_F(x,y)\), because \(q\circ g\) is \(L\)-Lipschitz; the integrating-factor argument above applies. This is a different assertion from (1). The augmented metric \(d+D_F\) is equivalent to \(D_F\), since (4) gives \(d\le D_F\), but neither is uniformly controlled by initial RMS distance on RMS-bounded sets. For example, take \(x=\sqrt n\,e_1\) and \(y=(\sqrt n+1)e_1\). Their RMS norms are at most 2, while

\[
 \|x-y\|_{2,n}=n^{-1/2}\to0,\qquad
 D_F(x,y)=\sqrt n+1+\frac{4}{3\sqrt n}\to\infty.
\]

No such initial metric comparison occurs in the proof of (1).

The norm convention matters for sharpness. If one instead assumes the stronger, width-uniform bound \(\sup_z\|q(z)\|_{\ell^2}\le Q_E\), then \(\|q(z)\|_\infty\le Q_E\). Splitting the difference of \(\phi'(z)\odot q(z)\) into its two factors and using \(|\phi''|\le1\) bounds it in RMS by \((L+Q_E)\|z-w\|_{2,n}\). The integral comparison therefore gives the Lipschitz bound \(e^{c_1(L+Q_E)T}d\). The \(3/5\) optimality statement concerns RMS-bounded forcing, which allows concentrated coordinates of size \(\sqrt n\).

If \(d=0\), uniqueness makes the endpoint difference zero. If \(T=0\), the endpoint map is the identity. If \(Q=0\), \(q\equiv0\) and the entire flow is the identity. When \(R=0\), the only initial state in the ball is zero, so the sharpness assertion correctly requires \(R>0\). No positivity or sign condition on the readout is assumed.

All conclusions concern the same frozen \(W^{(3)},W^{(4)}\) and the same fixed \(h^{(1)}\), through fixed \(c_1\). The \(L^6\) displacement gain (3) supplies no estimate for additional terms generated by moving \(h^{(1)}\) or training the upper parameters. No bridge to full-feedback stability, full training, or canonical continuation is claimed.
