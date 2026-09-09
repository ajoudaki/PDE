# First feature/Stieltjes correction for two hidden layers and one sample

**Status:** audited exact Gaussian normal form and width-limit theorem under
the polynomially-smooth activation envelope stated in Section 9  
**Date:** 2026-08-18  
**Scope:** the model and limit order frozen in
[`PROOF_CONTRACT.md`](PROOF_CONTRACT.md)

This note gives a literal Gaussian-normal-form expression for

\[
C=\lim_{n\to\infty}\mathbb E[D_n^3f_n]
\]

for one fixed input and two hidden layers.  It uses no Hermite or polynomial
approximation of the activation.  The independent atomwise implementation,
exact controls, and fixed-program probabilistic bridge have passed the base
proof-contract gates under the activation envelope in Section 9.

## 1. Model and the atom grammar

The network is

\[
u_j=\frac{w_j^\top x}{\sqrt{d_0}},\qquad
z_i=\frac1{\sqrt n}\sum_{j=1}^nW_{ij}\phi(u_j),\qquad
f_n=\frac1n\sum_{i=1}^na_i\phi(z_i),
\]

with independent standard-Gaussian parameters and
\(q_0=\|x\|^2/d_0>0\).  The feature operator is

\[
D_n=n\nabla_\theta f_n\mathbin\cdot\nabla_\theta.
\]

Put \(\phi_r=\phi^{(r)}\), including \(\phi_0=\phi\).  Define

\[
G_1\sim N(0,q_0),\qquad
q_1=\mathbb E\phi_0(G_1)^2,\qquad
G_2\sim N(0,q_1).
\]

For a finite derivative multi-index \(\mathbf r=(r_1,\ldots,r_m)\), write

\[
\langle\mathbf r\rangle_\ell
:=
\mathbb E\!\left[\prod_{s=1}^m\phi_{r_s}(G_\ell)\right]
=\mathcal I\!\left(
[q_{\ell-1}];(1,\ldots,1);\mathbf r
\right),\qquad \ell\in\{1,2\}.
\tag{1.1}
\]

Thus every bracket in this note is a one-dimensional Gaussian atom with its
covariance and all derivative orders explicit.  Repeated entries are never
implicit; for example

\[
\langle0,2,1,1\rangle_1
=\frac1{\sqrt{2\pi q_0}}\int_{\mathbb R}
\phi(x)\phi''(x)\phi'(x)^2e^{-x^2/(2q_0)}\,dx.
\]

No multidimensional atom survives in the final \(B=1\) expression.  A
two-dimensional correlated Gaussian occurs in the peel and is integrated out
exactly by Price's identity in Section 6.

## 2. Complete atom dictionary

The first-layer atoms are

\[
\begin{aligned}
q_1&=\langle0,0\rangle_1,&
d_1&=\langle1,1\rangle_1,&
e_1&=\langle1,1,1,1\rangle_1,\\
m_1&=\langle0,2,1,1\rangle_1,&
j_1&=\langle3,1,1,1\rangle_1,&
s_1&=\langle2,2,1,1\rangle_1,\\
\ell_1&=\langle0,0,1,1\rangle_1.
\end{aligned}
\tag{2.1}
\]

The second-layer atoms are

\[
\begin{aligned}
q_2&=\langle0,0\rangle_2,&
d_2&=\langle1,1\rangle_2,&
e_2&=\langle1,1,1,1\rangle_2,\\
b_2&=\langle0,2\rangle_2,&
r_2&=\langle1,3\rangle_2,&
s_2&=\langle2,2\rangle_2,\\
p_2&=\langle0,0,1,1\rangle_2,&
u_2&=\langle0,1,1,2\rangle_2,&
v_2&=\langle1,1,2,2\rangle_2,\\
w_2&=\langle3,1,1,1\rangle_2.
\end{aligned}
\tag{2.2}
\]

These seventeen displayed atoms are the entire final grammar.  The largest
activation derivative order is three and the largest simultaneous product
contains four factors.

## 3. Closed normal form

Define the following scalar contractions, solely from (2.1)--(2.2):

\[
c=q_1+q_0d_1,
\tag{3.1}
\]

\[
\tau
=p_2+2cu_2+3c^2v_2+q_0^2e_1d_2s_2,
\tag{3.2}
\]

\[
\alpha=d_2+b_2+c(r_2+s_2),
\qquad
k=d_2+\alpha,
\tag{3.3}
\]

and

\[
\kappa=3q_0^2d_2m_1+3q_0^3d_2j_1.
\tag{3.4}
\]

The Hessian-square contribution is

\[
\begin{aligned}
H_\star={}&c^2e_2+q_1\tau+2q_0^2e_1d_2^2\\
&+q_0\left(
3q_0^2d_2^2s_1+k^2\ell_1+\tau d_1
+2q_0d_2km_1
\right).
\end{aligned}
\tag{3.5}
\]

The straight-line third-derivative contribution is

\[
\begin{aligned}
S_\star={}&3c^2u_2+3q_0^2e_1d_2b_2
+3q_0^2d_2m_1(d_2+b_2)\\
&+3c^3w_2+3cq_0^2e_1d_2r_2
+3q_0^2cd_2m_1(r_2+s_2)
+\kappa d_2.
\end{aligned}
\tag{3.6}
\]

The claimed Gaussian normal form is

\[
\boxed{
A=q_2+q_1d_2+q_0d_1d_2,
\qquad
C=4H_\star+2S_\star,
\qquad
\mu_0=\frac{C}{2A^2}
}
\tag{3.7}
\]

whenever \(A>0\).  Formula (3.7), together with the explicit one-dimensional
integrals (1.1), contains no random weights, neuron sums, empirical
covariances, tangent variables, response variables, or unevaluated Gaussian
derivatives.

## 4. Exact finite-width source identity

Let \(p_\theta=\nabla_\theta f_n\),
\(H_\theta=\nabla_\theta^2f_n\), and let
\(v=n p_\theta\).  Along the frozen straight line

\[
\widehat f(s)=f_n(\theta+sv),
\]

ordinary differentiation gives the exact identity

\[
D_n^3f_n=4n\|H_\theta v\|^2+2\widehat f'''(0).
\tag{4.1}
\]

This is the raw-coordinate version of
\(4\|Hp\|^2+2T[p,p,p]\) after metric whitening.  It gives two genuinely
different routes to the coefficient and fixes every power of \(n\).

For compactness, set at initialization

\[
h_j=\phi(u_j),\quad h_{r,j}=\phi_r(u_j),\qquad
g_i=\phi(z_i),\quad g_{r,i}=\phi_r(z_i),
\]

and

\[
R_j=\frac1{\sqrt n}\sum_iW_{ij}a_ig_{1,i}.
\tag{4.2}
\]

The frozen straight-line parameter velocities are

\[
\dot a_i=g_i,\qquad
\dot W_{ij}=\frac1{\sqrt n}a_ig_{1,i}h_j,\qquad
\dot u_j=q_0h_{1,j}R_j.
\tag{4.3}
\]

Writing \(\zeta_i=\dot z_i\), direct product rules give

\[
\begin{aligned}
\zeta_i
&=a_ig_{1,i}\frac1n\sum_jh_j^2
+\frac{q_0}{\sqrt n}\sum_jW_{ij}h_{1,j}^2R_j,\\
\ddot z_i
&=\frac1{\sqrt n}\sum_j
\left(2\dot W_{ij}h_{1,j}\dot u_j
+W_{ij}h_{2,j}\dot u_j^2\right),\\
\dddot z_i
&=\frac1{\sqrt n}\sum_j
\left(3\dot W_{ij}h_{2,j}\dot u_j^2
+W_{ij}h_{3,j}\dot u_j^3\right).
\end{aligned}
\tag{4.4}
\]

Consequently,

\[
\begin{aligned}
\widehat f'''(0)=\frac1n\sum_i\{&
3g_i(g_{2,i}\zeta_i^2+g_{1,i}\ddot z_i)\\
&+a_i(g_{3,i}\zeta_i^3
+3g_{2,i}\zeta_i\ddot z_i
+g_{1,i}\dddot z_i)\}.
\end{aligned}
\tag{4.5}
\]

No parity simplification has been used in (4.2)--(4.5).

## 5. Peeling the recurrent use of the middle weight matrix

The only nontrivial reuse is the alternating chain

\[
h\xrightarrow{W}z
\xrightarrow{\ a\phi'(z)\ }v
\xrightarrow{W^\top}R
\xrightarrow{\ \phi'(u)^2R\ }y
\xrightarrow{W}s.
\tag{5.1}
\]

Let \(U\sim N(0,q_0)\), \(Z\sim N(0,q_1)\),
\(A_0\sim N(0,1)\), and \(R\sim N(0,d_2)\) be independent.  Exact
Gaussian conditioning, with the equality sector retained before taking the
width limit, yields

\[
\frac1{\sqrt n}W(\phi_1(u)^2R)
\ \Longrightarrow\ d_1A_0\phi_1(Z)+\Gamma,
\qquad
\Gamma\sim N(0,e_1d_2),
\tag{5.2}
\]

where \(\Gamma\) is independent of \((Z,A_0)\).  The first term is the
same-row Wick/Onsager sector; deleting it changes \(c\) from
\(q_1+q_0d_1\) to \(q_1\) and already corrupts the NTK.

It follows from (4.4) that the first top-layer tangent has the representative
law

\[
\zeta=cA_0\phi_1(Z)+q_0\Gamma.
\tag{5.3}
\]

Define

\[
T=\phi_0(Z)\phi_1(Z)+A_0\phi_2(Z)\zeta.
\tag{5.4}
\]

Then direct Gaussian moments in \((A_0,\Gamma)\) give

\[
\mathbb E T^2=\tau.
\tag{5.5}
\]

The transpose peel of \(W^\top T/\sqrt n\) has two potential response
directions.  The \(\phi_1(U)^2R\) direction has coefficient
\(q_0\mathbb E[A_0\phi_2(Z)]=0\).  The \(h\) direction has the full
nested Stein coefficient

\[
\alpha
=\mathbb E\left[
\phi_1(Z)^2+\phi_0(Z)\phi_2(Z)
+c\{\phi_1(Z)\phi_3(Z)+\phi_2(Z)^2\}
\right],
\tag{5.6}
\]

which is exactly (3.3).  Hence, if

\[
\dot R_j
=\frac1{\sqrt n}\sum_i
\left(\dot W_{ij}a_ig_{1,i}
+W_{ij}g_ig_{1,i}
+W_{ij}a_ig_{2,i}\zeta_i\right),
\]

then

\[
\dot R\ \Longrightarrow\ k\phi_0(U)+R_2,
\qquad R_2\sim N(0,\tau),
\tag{5.7}
\]

with \(R_2\) independent of \((U,R)\).  The cross covariance of the two
fresh transpose channels is zero because

\[
\mathbb E[A_0\phi_1(Z)T]=0.
\tag{5.8}
\]

Equations (5.2) and (5.6) are precisely the two response terms most easily
lost by an independence shortcut.

## 6. Second and third straight tangents

Put

\[
\Omega_n=\frac1{\sqrt n}\sum_j
W_{ij}\phi_2(u_j)\phi_1(u_j)^2R_j^2.
\]

The response proportional to
\(\mathbb E[2\phi_2(U)\phi_1(U)^2R]\) vanishes.  Its joint Gaussian limit
with \(Z\) has covariance matrix

\[
\operatorname{Cov}\binom{Z}{\Omega}
=
\begin{pmatrix}
q_1 & d_2m_1\\
d_2m_1 & 3d_2^2
\langle2,2,1,1,1,1\rangle_1
\end{pmatrix}.
\tag{6.1}
\]

Thus

\[
\ddot z\Longrightarrow q_0^2\Omega.
\tag{6.2}
\]

For every differentiable integrable \(F\), Price/Stein differentiation of
the explicit two-dimensional Gaussian in (6.1) gives

\[
\mathbb E[\Omega F(Z)]=d_2m_1\mathbb E[F'(Z)].
\tag{6.3}
\]

The cubic input channel is
\(\phi_3(U)\phi_1(U)^3R^3\).  Its same-row response is
\(3d_2j_1A_0\phi_1(Z)\).  Combining it with the first term of
\(\dddot z\) in (4.4) gives

\[
\dddot z\Longrightarrow
\kappa A_0\phi_1(Z)+q_0^3\Lambda,
\tag{6.4}
\]

where \(\Lambda\) is centered and independent of \(A_0\).  Its covariance
with \(\Gamma\) need not vanish, but the only occurrence of \(\Lambda\) in
(4.5) is
\(\mathbb E[A_0\phi_1(Z)\Lambda]=0\).  This is an exact parity/covariance
certificate, not an independence assumption; all fresh cubic-channel atoms
therefore cancel from the final normal form.

Substitution of (5.3), (6.2), and (6.4) into (4.5), followed only by the
standard Gaussian moments
\(\mathbb EA_0^2=1\), \(\mathbb EA_0^4=3\),
\(\mathbb E\Gamma^2=e_1d_2\), and (6.3), yields

\[
\lim_{n\to\infty}\mathbb E\widehat f'''(0)=S_\star.
\tag{6.5}
\]

Term by term, the seven summands in (3.6) arise respectively from

\[
\begin{array}{c|c}
\text{source in (4.5)} & \text{normal-form contribution}\\ \hline
3gg_2\zeta^2 & 3c^2u_2+3q_0^2e_1d_2b_2\\
3gg_1\ddot z & 3q_0^2d_2m_1(d_2+b_2)\\
A_0g_3\zeta^3 & 3c^3w_2+3cq_0^2e_1d_2r_2\\
3A_0g_2\zeta\ddot z & 3q_0^2cd_2m_1(r_2+s_2)\\
A_0g_1\dddot z & \kappa d_2.
\end{array}
\tag{6.6}
\]

This table is also a complete product-rule audit of the straight-line part.

## 7. Hessian-square peel

Differentiate each raw parameter-gradient block along the same frozen line.
After multiplying its squared norm by the factor \(n\) in (4.1), the three
blocks converge to

\[
\begin{aligned}
\mathcal H_a
&=\mathbb E[\phi_1(Z)^2\zeta^2]
=c^2e_2+q_0^2e_1d_2^2,\\
\mathcal H_W
&=\mathbb E\left[
\phi_0(U)T+q_0A_0\phi_1(Z)\phi_1(U)^2R
\right]^2\\
&=q_1\tau+q_0^2e_1d_2^2,\\
\mathcal H_w
&=q_0\mathbb E\left[
q_0\phi_2(U)\phi_1(U)R^2
+\phi_1(U)\{k\phi_0(U)+R_2\}
\right]^2\\
&=q_0\left(
3q_0^2d_2^2s_1+k^2\ell_1+\tau d_1
+2q_0d_2km_1
\right).
\end{aligned}
\tag{7.1}
\]

The mixed term in \(\mathcal H_W\) vanishes because
\(\mathbb E[\phi_0(U)\phi_1(U)^2R]=0\).  The mixed term containing \(R_2\)
in \(\mathcal H_w\) vanishes by (5.8).  Therefore

\[
\lim_{n\to\infty}n\,\mathbb E\|H_\theta v\|^2
=\mathcal H_a+\mathcal H_W+\mathcal H_w=H_\star.
\tag{7.2}
\]

Together, (4.1), (6.5), and (7.2) prove the normal form (3.7); Section 9
supplies the theorem-covered finite-width-to-limit passage.

## 8. Exact regression controls

### 8.1 Constant activation

For \(\phi\equiv c_0\), all derivative atoms vanish.  Equations (3.1)--(3.7)
give \(A=c_0^2\) and \(C=0\), as required for a readout-only affine model.

### 8.2 Linear activation

For \(\phi(x)=x\),

\[
q_1=q_0,\quad d_1=e_1=d_2=e_2=1,\quad
\ell_1=p_2=q_0,
\]

and every atom containing \(\phi_2\) or \(\phi_3\) is zero.  Hence

\[
c=2q_0,\qquad \tau=q_0,\qquad k=2,
\qquad H_\star=12q_0^2,\qquad S_\star=0,
\]

so

\[
A=3q_0,\qquad C=48q_0^2,\qquad \mu_0=\frac83.
\tag{8.1}
\]

The independent finite-width calculation in
[`AUDIT_REPORT.md`](AUDIT_REPORT.md) gives the stronger identity

\[
\mathbb E[D_n^3f_n]=q_0^2(48+60/n),
\]

so (8.1) checks both the metric power and the limiting coefficient.

### 8.3 Quadratic activation

For \(q_0=1\) and \(\phi(x)=x^2\), the atom dictionary evaluates to

\[
\begin{array}{c|rrrrrrr}
&q_1&d_1&e_1&m_1&j_1&s_1&\ell_1\\ \hline
\text{value}&3&4&48&24&0&16&60
\end{array}
\]

and

\[
\begin{array}{c|rrrrrrrrrr}
&q_2&d_2&e_2&b_2&r_2&s_2&p_2&u_2&v_2&w_2\\ \hline
\text{value}&27&12&432&6&0&4&1620&216&48&0.
\end{array}
\]

Consequently,

\[
c=7,\quad \tau=14004,\quad \alpha=46,\quad k=58,
\quad H_\star=375180,\quad S_\star=92232,
\]

and

\[
A=111,\qquad
C=4(375180)+2(92232)=1\,685\,184,
\]

\[
\mu_0=\frac{1\,685\,184}{2(111)^2}
=\frac{280864}{4107}.
\tag{8.2}
\]

Both integers in (8.2) agree exactly with the independent exhaustive pairing
and recursive quadratic compilers.

## 9. Probabilistic theorem and regularity boundary

The displayed algebra uses the following finite-order mean-field statements:

1. the finite collection of forward, backward, and tangent channels in
   Sections 5--7 has the stated joint Gaussian/Onsager limit;
2. empirical moments such as \(n^{-1}\sum h_j^2\) may be replaced by their
   displayed deterministic atoms after all equality sectors have been
   extracted;
3. every term in (4.1) is uniformly integrable, so expectation commutes with
   the fixed-order width limit.

A complete proof of these statements is now recorded in
`PEELING_AND_PROBABILITY_LEDGER.md`.  It encodes the exact finite-width
observable \(C_n\) as one fixed NETSOR\({}^\top+\)/Tensor Program.  Theorem
E.15 of Tensor Programs III gives the complete joint Gaussian/Onsager and
empirical-moment limit under pseudo-Lipschitz coordinate maps.  If \(\phi\) is
polynomially smooth---\(C^\infty\), with every derivative of every order
polynomially bounded---Theorem 3.7 of Non-Gaussian Tensor Programs further
gives \(C_n\to C\) almost surely and in \(L^p\) for every finite \(p\).
Consequently hypotheses 1--3, including uniform integrability and
\(\mathbb EC_n\to C\), are discharged under that envelope.

The algebra itself only contains \(\phi\) through \(\phi'''\).  If one assumes
polynomial control only through this finite derivative order, Theorem E.15
still supplies the almost-sure statement when these maps are pseudo-Lipschitz,
but Theorem 3.7 is not applicable as written.  In that weaker tier the
annealed conclusion requires the explicit uniform-integrability condition in
Section 8.3 of `PEELING_AND_PROBABILITY_LEDGER.md` (or an
activation-specific substitute).

For the physical one-sample MSE loss, let
\(\mathcal J_3[h](t)=\sum_{k=0}^3h^{(k)}(0)t^k/k!\).  The separate
finite-width audit and the same fixed-program \(L^p\) theorem give the
coefficientwise limit

\[
\lim_{n\to\infty}\mathcal J_3[\mathbb E L_n](t)
=1-4\eta At+8\eta^2A^2t^2
-\left(\frac{32}{3}\eta^3A^3+\frac83\eta^3C\right)t^3
\pmod{t^4}.
\tag{9.1}
\]

Thus the first feature-dependent correction to frozen NTK loss is

\[
-\frac83\eta^3C\,t^3
=-\frac{16}{3}\eta^3A^2\mu_0\,t^3.
\tag{9.2}
\]

For an arbitrary fixed scalar label \(y_\star\), the Gaussian normal form
itself is unchanged.  Repeating the finite-width loss calculation with
\(L_n=(y_\star-f_n)^2\) gives, again coefficientwise,

\[
\begin{aligned}
\lim_{n\to\infty}\mathcal J_3[\mathbb E L_n](t)
={}&y_\star^2-4\eta y_\star^2At
+8\eta^2y_\star^2A^2t^2\\
&-\left(
\frac{32}{3}\eta^3y_\star^2A^3
+\frac83\eta^3y_\star^4C
\right)t^3\pmod{t^4}.
\end{aligned}
\tag{9.3}
\]

Thus changing the single label introduces no new Gaussian atom; its first
feature correction scales as \(y_\star^4\).

No positivity is asserted.  In particular, the nonnegative Hessian-square
piece \(4H_\star\) is accompanied by the signed piece \(2S_\star\).
