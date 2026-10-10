# Independent check of the two-hidden-layer derivative example

This is a scoped, prompt-only derivation for the study
`mfp_gaussian_master_proof_20261010`. Its scientific inputs are exactly the
model and Gaussian evaluation rules supplied in the assignment. I read the
required canonical-notation skill and its neural-network reference, the
rigorous-math skill, and repository process instructions. I did not retrieve
book material, study history, another derivation, or external scientific
sources, and did not execute code or experiments. This report provides exact
finite-width identities and Gaussian-rule limit targets; it is not a general
master-theorem proof or a promotion review.

## Exact finite-width quantities

There is one scalar input, \(x=1\), and two hidden layers, each of width
\(n\geq1\). The stored vectors \(w^{(1)},w^{(3)}\in\mathbb R^n\) have
independent \(N(0,1)\) entries; in particular the stored readout
\(w^{(3)}\) is order one. The independent matrix
\(W^{(2)}\in\mathbb R^{n\times n}\) has independent \(N(0,1/n)\) entries.
The activation \(\phi\) is smooth, with polynomial growth of itself and its
derivatives. Every quantity below is evaluated at initialization. No loss,
training dynamics, or time limit is involved.

The forward pass and scalar output are

\[
z^{(1)}=w^{(1)},\qquad h^{(1)}=\phi(z^{(1)}),\qquad
z^{(2)}=W^{(2)}h^{(1)},\qquad h^{(2)}=\phi(z^{(2)}),\qquad
f_n=\frac1n w^{(3)\top}h^{(2)}.
\]

Activation functions act componentwise. Define the vector
\(u=w^{(3)}\odot\phi'(z^{(2)})\in\mathbb R^n\). Differentiation gives

\[
\begin{aligned}
\nabla_{w^{(1)}}f_n
 &=\frac1n\phi'(z^{(1)})\odot W^{(2)\top}u,\\
\nabla_{W^{(2)}}f_n&=\frac1n u h^{(1)\top},\\
\nabla_{w^{(3)}}f_n&=\frac1n h^{(2)}.
\end{aligned}
\]

Consequently the requested derivative block and its empirical square are

\[
b^{(1)}=n\nabla_{w^{(1)}}f_n
       =\phi'(z^{(1)})\odot W^{(2)\top}u,\qquad
O_n=\frac1n\|b^{(1)}\|^2
   =n\|\nabla_{w^{(1)}}f_n\|^2.
\]

The full metric norm has the exact identity

\[
\begin{aligned}
K_n
&=n\|\nabla_{w^{(1)}}f_n\|^2
  +\|\nabla_{W^{(2)}}f_n\|_F^2
  +n\|\nabla_{w^{(3)}}f_n\|^2\\
&=O_n+\left(\frac1n\|u\|^2\right)
           \left(\frac1n\|h^{(1)}\|^2\right)
      +\frac1n\|h^{(2)}\|^2.
\end{aligned}
\]

The middle block is a product of two empirical means: both \(1/n\)
factors from its outer-product gradient are essential.

## Evaluation using the supplied Gaussian rules

Let \(X,A,Z,Y\) be independent standard Gaussian random variables, with
\(X\) representing \(w^{(1)}\) and \(A\) representing \(w^{(3)}\). Define

\[
q=\mathbb E[\phi(X)^2],\qquad
a=\mathbb E[\phi'(X)^2],\qquad
s=\mathbb E[\phi'(\sqrt q\,Z)^2],\qquad
t=\mathbb E[\phi(\sqrt q\,Z)^2].
\]

These deterministic numbers are finite under the growth assumptions.
In particular \(q\) is a second moment, without subtraction of the
mean of \(\phi(X)\). The first forward matrix call produces

\[
\xi=\sqrt q\,Z,\qquad H^{(2)}=\phi(\xi),\qquad
U=A\phi'(\xi).
\]

There is no earlier reverse call at this first forward call. At the
subsequent transpose call, the supplied rule includes the earlier forward
input \(H^{(1)}=\phi(X)\) multiplied by the response coefficient

\[
\mathbb E[\partial_\xi U]
 =\mathbb E[A\phi''(\xi)]
 =\mathbb E[A]\,\mathbb E[\phi''(\xi)]
 =0.
\]

This partial derivative holds the already computed deterministic
coefficient \(q\) fixed. Independence and centering of the readout root
\(A\) justify the zero; ignoring matrix reuse without this computation
would not justify it. The Gaussian part of the transpose call has variance

\[
\mathbb E[U^2]
 =\mathbb E[A^2]\,\mathbb E[\phi'(\xi)^2]=s.
\]

The reverse-oriented Gaussian group is independent of the forward group
and roots under the supplied rules. Thus the scalar derivative block is

\[
B^{(1)}=\phi'(X)\sqrt s\,Y.
\]

The Gaussian expectation targets are therefore

\[
O_\infty=\mathbb E[(B^{(1)})^2]=as,\qquad
K_\infty=as+qs+t.
\]

These are the limits predicted by the supplied empirical Gaussian
evaluation rules. This calculation does not independently establish
their general convergence theorem or its convergence mode. The
construction permits \(q=0\) or \(s=0\), without division. A vanishing
limit response does not imply absence of finite-width dependence
between \(W^{(2)}\) and \(u\).

## Polynomial limit checks

For \(\phi(z)=z\),

\[
q=a=s=t=1,\qquad O_\infty=1,\qquad K_\infty=3.
\]

For \(\phi(z)=z^3\), Gaussian moments
\(\mathbb E Z^4=3\) and \(\mathbb E Z^6=15\) give

\[
\begin{aligned}
q&=15,& a&=9\mathbb E X^4=27,\\
s&=9\mathbb E[(\sqrt{15}Z)^4]=6075,&
t&=\mathbb E[(\sqrt{15}Z)^6]=50625.
\end{aligned}
\]

Thus the three metric contributions are

\[
O_\infty=164025,\qquad qs=91125,\qquad t=50625,
\qquad K_\infty=305775.
\]

## Supplemental exact finite-width expectation check

This supplemental calculation gives an algebraically checked expectation
oracle. It is optional for the example and does not require a simulation.

For \(r\geq0\), define

\[
S(r)=\mathbb E[\phi'(\sqrt r\,Z)^2],\qquad
D(r)=\mathbb E\left[
 \left.\frac{d^2}{dz^2}\{\phi'(z)^2\}\right|_{z=\sqrt r\,Z}
\right],\qquad
T(r)=\mathbb E[\phi(\sqrt r\,Z)^2].
\]

Using the realized first-layer vector, put

\[
q_n=\frac1n\sum_j\phi(w^{(1)}_j)^2,\quad
a_n=\frac1n\sum_j\phi'(w^{(1)}_j)^2,\quad
c_n=\frac1n\sum_j
       \phi'(w^{(1)}_j)^2\phi(w^{(1)}_j)^2.
\]

The exact expectations over \(W^{(2)}\) and \(w^{(3)}\) are

\[
\begin{aligned}
\mathbb E[O_n\mid w^{(1)}]
 &=a_nS(q_n)+\frac{c_n}{n}D(q_n),\\
\mathbb E[K_n\mid w^{(1)}]
 &=a_nS(q_n)+\frac{c_n}{n}D(q_n)
   +q_nS(q_n)+T(q_n).
\end{aligned}
\]

For a proof, hold \(h=h^{(1)}\) fixed and let
\(g\sim N(0,I_n/n)\) be one row of \(W^{(2)}\), written as a column.
For smooth \(F\), with \(F,F',F''\) of polynomial growth, integration
by parts in the Gaussian coordinates gives

\[
\begin{aligned}
\mathbb E[g_jg_kF(g^\top h)]
&=\frac{\delta_{jk}}n\mathbb E[F(g^\top h)]
 +\frac{h_j}n\mathbb E[g_kF'(g^\top h)]\\
&=\frac{\delta_{jk}}n\mathbb E[F(g^\top h)]
 +\frac{h_jh_k}{n^2}\mathbb E[F''(g^\top h)].
\end{aligned}
\]

Polynomial growth makes the boundary terms vanish. Set \(F=(\phi')^2\).
The independent centered readout eliminates all products of different
rows in the square of \(W^{(2)\top}u\). Summing the \(n\) remaining
row contributions yields

\[
\mathbb E[(W^{(2)\top}u)_j^2\mid w^{(1)}]
  =S(q_n)+\frac{h_j^2}{n}D(q_n).
\]

Multiplication by \(\phi'(w^{(1)}_j)^2\) and averaging proves the
first oracle. The other two metric blocks have conditional expectations
\(q_nS(q_n)\) and \(T(q_n)\), proving the second oracle. This proof
also applies at \(q_n=0\), without division.

For the linear activation \(D(r)=0\), so
\(\mathbb E O_n=1\) and \(\mathbb E K_n=3\) for every \(n\geq1\).

For the cubic activation, define
\(m_k=n^{-1}\sum_j(w^{(1)}_j)^k\). Since
\(S(r)=27r^2\), \(D(r)=108r\), and \(T(r)=15r^3\),

\[
\mathbb E[O_n\mid w^{(1)}]
 =243m_4m_6^2+\frac{972}{n}m_6m_{10},\qquad
\mathbb E[K_n\mid w^{(1)}]
 =\mathbb E[O_n\mid w^{(1)}]+42m_6^3.
\]

To expose every coefficient of the finite-width oracle, let
\(\mu_k=\mathbb E X^k\). Grouping coincident indices gives

\[
\begin{aligned}
\mathbb E[m_4m_6^2]
 &=\frac{(n-1)(n-2)\mu_4\mu_6^2
       +(n-1)(\mu_4\mu_{12}+2\mu_{10}\mu_6)
       +\mu_{16}}{n^2},\\
\mathbb E[m_6m_{10}]
 &=\frac{(n-1)\mu_6\mu_{10}+\mu_{16}}{n},\\
\mathbb E[m_6^3]
 &=\frac{(n-1)(n-2)\mu_6^3
        +3(n-1)\mu_{12}\mu_6+\mu_{18}}{n^2}.
\end{aligned}
\]

The recurrence \(\mu_{2k}=(2k-1)\mu_{2k-2}\), obtained by Gaussian
integration by parts, gives
\(\mu_{10}=945\), \(\mu_{12}=10395\),
\(\mu_{16}=2027025\), and \(\mu_{18}=34459425\). Substitution yields

\[
\begin{aligned}
\mathbb E[m_4m_6^2]
 &=675+\frac{57510}{n}+\frac{1968840}{n^2},\\
\mathbb E[m_6m_{10}]
 &=14175+\frac{2012850}{n},\\
\mathbb E[m_6^3]
 &=3375+\frac{457650}{n}+\frac{33998400}{n^2}.
\end{aligned}
\]

The exact unconditional means are consequently

\[
\begin{aligned}
\mathbb E O_n
 &=164025+\frac{27753030}{n}+\frac{2434918320}{n^2},\\
\mathbb E K_n
 &=305775+\frac{46974330}{n}+\frac{3862851120}{n^2}.
\end{aligned}
\]

As an independent algebraic boundary check, at \(n=1\) the network is
\(f_1=w^{(3)}(W^{(2)})^3(w^{(1)})^9\). Its first-layer derivative gives

\[
\mathbb E O_1
 =81\,\mathbb E[(W^{(2)})^6]\,
       \mathbb E[(w^{(1)})^{16}]
 =2462835375,
\]

agreeing with the formula. The other two gradient-block expectations
sum to \(42\mu_{18}=1447295850\), agreeing with the \(K_n\) formula.

The positive cubic finite-width corrections are substantial. A numerical
check should distinguish exact derivative identities, finite-width
expectations, and limiting targets; convergence alone does not justify
a tight tolerance around a limiting target at modest width.
