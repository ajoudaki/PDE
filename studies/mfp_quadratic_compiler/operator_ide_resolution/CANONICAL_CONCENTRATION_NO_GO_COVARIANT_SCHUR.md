# Canonical concentration no-go: covariant Schur proof

Status: proved and independently audited, 22 August 2026.

The final isolated end-to-end audit returned a strict pass on the mathematical
body at SHA-256
`be9d0d95d12bd20f55429c1d57bcf431b7cfcd27885a447ed361a6a4f1587f37`.

This note replaces the invalid full-state susceptibility claim in
`CANONICAL_CONCENTRATION_NO_GO_FINAL.md`.  Singular row and column modes are
never estimated by a global Hessian norm.  Rows are Schur-resummed first;
then each exact one-column insertion is solved against the resulting
row-dressed bath.  A fast column is compared only at moving reciprocal
levels.  These two choices remove the two fixed-time tangent losses found in
the preceding audits.

Throughout,

\[
 \langle v,w\rangle_n=n^{-1}v^{\mathsf T}w,
 \qquad \|v\|_{p,n}=\langle |v|^p\rangle_n^{1/p},
 \qquad L=\sqrt{\log n}.
\]

## 1. The theorem and the contradiction

Let (A_i,u_j,W_{ij}) be independent standard Gaussians, put
(G(0)=W/\sqrt n), and define

\[
 X=u^{\odot2},\quad Z=GX,\quad B=A\odot Z,\quad
 R=G^{\mathsf T}B,\quad f_n=\langle A,Z^{\odot2}\rangle_n .
\]

In feature time (s), let

\[
 A'=Z^{\odot2},\qquad X'=8X\odot R,
 \qquad G'=\frac2nBX^{\mathsf T}.                         \tag{1.1}
\]

Then

\[
 K_n:=f_n'
 =\langle Z^{\odot4}\rangle_n
 +4\langle X^{\odot2}\rangle_n\langle B^{\odot2}\rangle_n
 +16\langle X\odot R^{\odot2}\rangle_n\ge0.             \tag{1.2}
\]

**Theorem 1 (canonical initial layer).**  There are constants
(\delta_0,c_0>0) such that

\[
 \Pr\left\{
   \inf\{s:f_n(s)-f_n(0)\ge\delta_0\}
       \le \frac{0.09+o(1)}{L}
 \right\}\longrightarrow1.                              \tag{1.3}
\]

For any fixed (y_\star>0) and (\eta\ge\eta_0>0), physical MSE time is

\[
 \dot\theta=2\eta(y_\star-f_n)\theta'.                  \tag{1.4}
\]

Choose \(\delta_0<y_\star/4\).  Since \(f_n(0)\to0\), before the hit in
(1.3) the physical time is at most \(C/L\), hence tends to zero.  If the
frozen contract held, its continuous readout \(F\) and compact-time uniform
convergence would give, at the random hitting time \(t_n\),

\[
 \delta_0
 \le 2\|f_n-F\|_{\infty,[0,T]}
       +|F(t_n)-F(0)|\ \xrightarrow{\mathbb P}\ 0,        \tag{1.5}
\]

a contradiction.  Thus Theorem 1 decides the frozen conjecture negatively.
The rest of the note proves Theorem 1.

## 2. Exact identities and local variables

The trained matrix and the two preactivations have the exact forms

\[
 G(t)=G(0)+\frac2n\int_0^tB(r)X(r)^{\mathsf T}\,dr,        \tag{2.1}
\]

\[
\begin{aligned}
 Z(t)&=G(0)X(t)
 +2\int_0^tB(r)\langle X(r),X(t)\rangle_n\,dr,\\
 R(t)&=G(0)^{\mathsf T}B(t)
 +2\int_0^tX(r)\langle B(r),B(t)\rangle_n\,dr.
\end{aligned}                                             \tag{2.2}
\]

For a column (j), write

\[
 x=X_j,\quad g=G_{\cdot j},\quad z=Z-xg,\quad
 h=g^{\mathsf T}D_Ag,\quad \rho=g^{\mathsf T}D_Az,
 \quad R_j=hx+\rho .                                     \tag{2.3}
\]

With (H_-=G_{\cdot,-j}D_{X_{-j}}G_{\cdot,-j}^{\mathsf T}) and
(Q_-=\langle X_{-j}^2\rangle_n), direct differentiation gives

\[
 x'=8x(hx+\rho),                                         \tag{2.4}
\]

\[
 \rho'=x\mathcal P+\mathcal E_0+x^2\mathcal E_2,        \tag{2.5}
\]

where

\[
\begin{aligned}
\mathcal P={}&2\langle A^2z^2\rangle_n
+2\sum_i g_i^2z_i^2+2Q_-\sum_iA_i^2g_i^2
+8g^{\mathsf T}D_AH_-D_Ag\ge0,\\
\mathcal E_0={}&\sum_i g_iz_i^3
+2Q_-\sum_iA_i^2g_iz_i+8g^{\mathsf T}D_AH_-D_Az,\\
\mathcal E_2={}&\frac2n\sum_iA_i^2g_iz_i+\sum_i g_i^3z_i.
\end{aligned}                                             \tag{2.6}
\]

Also

\[
 h'=\sum_i\left(g_iZ_i+\frac{2x}{n}A_i^2\right)^2
 -\frac{4x^2}{n^2}\sum_iA_i^4
 \ge-\frac{4x^2}{n}\langle A^4\rangle_n.               \tag{2.7}
\]

For a row (i), put (b_i=A_iZ_i),

\[
 S_i=\sum_jG_{ij}^2X_j,\qquad
 R_j^{(-i)}=R_j-G_{ij}b_i,
 \qquad N_i=\sum_jG_{ij}X_jR_j^{(-i)}.
\]

Then exactly

\[
 A_i'=Z_i^2,\qquad
 Z_i'=(2Q+8S_i)A_iZ_i+8N_i,
 \qquad Q=\langle X^2\rangle_n.                          \tag{2.8}
\]

The identity that removes the false fixed-time candidate Green is the
following.  For every *fixed initial* column set (D),

\[
\begin{aligned}
8\int_0^t\sum_{j\in D}G_{ij}X_jR_j^{(-i)}\,ds
={}&\left[\sum_{j\in D}G_{ij}X_j\right]_0^t\\
&-\int_0^t(2q_D+8S_{iD})B_i\,ds,                         \tag{2.9}
\end{aligned}
\]

where

\[
 q_D=n^{-1}\sum_{j\in D}X_j^2,
 \qquad S_{iD}=\sum_{j\in D}G_{ij}^2X_j.                \tag{2.10}
\]

At a moving hit \(X_j=x_{\rm cap}\), the dangerous variation of the
endpoint \(G_{ij}X_j\) is \(x_{\rm cap}\,\delta G_{ij}\), not
\(G_{ij}\delta X_j\).  This is the cancellation on which Section 4 rests.

## 3. The certified finite-dimensional separation

Set \(\tau=Ls\).  For an extreme column define

\[
 x=L^2U,\qquad H=Lh,\qquad P=\rho/L .                    \tag{3.1}
\]

The limiting tagged system is

\[
 U_\tau=8U(HU+P),\qquad H_\tau=3,
 \qquad P_\tau=26U,                                     \tag{3.2}
\]

with Gaussian rate

\[
 I_c(a,b)=a/2+b^2/6,\qquad U(0)=a,\quad P(0)=b.          \tag{3.3}
\]

For a row, (A_i=L\alpha,Z_i=L\zeta) give

\[
 \alpha_\tau=\zeta^2,\qquad
 \zeta_\tau=14\alpha\zeta,\qquad
 I_r=\alpha_0^2/2+\zeta_0^2/6.                           \tag{3.4}
\]

The checked integer-arithmetic program `outer_pole_certificate.c`, whose
SHA256 is

```text
f191d9720196e9300b7771a4b9aca4e65340cf3f2399e44d60493ccf062026d1
```

proves

\[
 0.08389<T_*:=\inf_{I_c\le1}T_c<0.0839,                 \tag{3.5}
\]

and certifies \(T_c(335/192,7/8)<0.0839\) and a rate-\(9/10\)
witness with
clock (<0.088572).

The row bound is analytic, not delegated to the program.  For
\(x=\alpha_0\ge0\), \(z=|\zeta_0|>0\), put
\(r=\sqrt{14}x/z\).  The invariant
\(C=\zeta^2-14\alpha^2\) gives

\[
 T_r^2=\frac{3r^2+14}{1176}F(r)^2,\qquad
 F(r)=\int_r^\infty\frac{dy}{y^2+1-r^2},               \tag{3.5a}
\]

where the rate-one identity was used to obtain
\(z^2=84/(3r^2+14)\).  If \(0\le r\le1\), write
\(r=\cos\theta\); then \(F=\theta/\sin\theta\).  On
\(r\in[1/3,1]\), \(F\ge1\) and
\(T_r^2\ge43/3528>0.11^2\).  On \(r\le1/3\), use
\(\theta>1\) and \(\sin1<101/120\), which is stronger.  If
\(r=\cosh x\ge1\), then

\[
 1176T_r^2=3x^2+17(x/\sinh x)^2
 \ge3y+17e^{-y/3},\qquad y=x^2,                         \tag{3.5b}
\]

because \(\log(\sinh x/x)\le x^2/6\).  The last expression has
minimum \(9+9\log(17/9)>189/13>1176(0.11)^2\).
Negative \(\zeta_0\) is equivalent by sign, while a negative
\(\alpha_0\) must first traverse to zero and is no faster.  Thus every
rate-one row pole is strictly later than \(0.11\).

The column system has the exact homogeneity

\[
 T_c(\lambda^2a,\lambda b)=\lambda^{-1}T_c(a,b),
 \qquad I_c(\lambda^2a,\lambda b)=\lambda^2I_c(a,b).     \tag{3.6}
\]

Every minimizing type has (a>0): (a=0) never moves.  It also has
(b>0).  Replacing (b<0) by (-b) makes the cooperative solution
earlier, and at (b=0) a positive (b)-perturbation changes the clock to
first order whereas the cost-preserving change in (a) is second order.
Compactness therefore supplies constants (a_0,b_0>0) for all types in a
small clock neighborhood of (T_*).

## 4. Covariant ordered Schur peeling

This section states and proves the probability lemma that replaces every
global full-state Hessian assertion.

### 4.1 Stops, fixed layers, and the bounded core

Put
\[
 h_L=(\log L)^{-1},\qquad T_{\rm pre}=T_*+5h_L<0.09.   \tag{4.0}
\]
For \(j\notin S\), \(|S|\le2\), define the punctured initial score
\[
 b_j^{[-S]}=L^{-1}g_j(0)^{\mathsf T}D_{A(0)}
       \sum_{k\notin S\cup\{j\}}g_k(0)X_k(0),\qquad
 a_j=X_j(0)/L^2.                                       \tag{4.0a}
\]
On the simultaneous Gaussian block event,
\[
 \max_{j,S}|b_j^{[-S]}-b_j^{[-\varnothing]}|
 \le L^{-1}\max_jX_j(0)
       \max_{j\ne k}|g_j(0)^{\mathsf T}D_{A(0)}g_k(0)|
 =n^{-1/2+o(1)}=o(h_L).                                \tag{4.0b}
\]
Define the buffered formal candidate set before any dynamics or selector:
\[
 \mathscr C_L=\left\{j:\ I_c(a_j,b_j^{[-S]})\le1+\eta
 \text{ and }T_c(a_j,b_j^{[-S]})\le T_*+8h_L
 \text{ for some }|S|\le2\right\}.                   \tag{4.0c}
\]
Here \(\eta>0\) is fixed and small.  Compactness of the near-minimizing
type set, (4.0b), and the exact homogeneity (3.6) give
\[
 \mathbb E|\mathscr C_L|
 \le L^Cn^{1-(T_*/(T_*+9h_L))^2+o(h_L)}
 =e^{O(h_LL^2)},\qquad |\mathscr C_L|=n^{o(1)}         \tag{4.0d}
\]
with probability tending to one.  This is only an upper count and uses
the one-column Gaussian density, not the later coarea selection.

The pre-cap argument is stopped at
\[
 \sigma_{\rm pre}=\inf\left\{s:\ s=T_{\rm pre}/L,
 \ \int_0^sK_n(r)\,dr=\delta,
 \ \text{or }\max_{j\in\mathscr C_L}X_j(s)=n^{1/3}\right\}, \tag{4.1}
\]
where \(\delta>0\) is fixed and small.  A candidate cap is retained as a
successful branch and continued only by Section 7.  Since
\(T_{\rm pre}<0.09\), every estimate below may harmlessly use
\(0.09/L\) as an upper bound on elapsed feature time.  From (1.2),

\[
\begin{aligned}
\int\|A'\|_{2,n}^2&\le\delta,\\
\int\|u'\|_{2,n}^2&\le\delta,\\
\int\|G'\|_F^2&\le\delta.
\end{aligned}                                             \tag{4.2}
\]

Choose an integer \(D>10\), larger than the degree of every coefficient
used below, choose \(0<\varepsilon<1/(16(D+2))\), and put

\[
 R_L=L^\varepsilon,\qquad M_L=L^{3/4},\qquad
 \gamma_L=\frac{M_LR_L^D}{L}=o((\log L)^{-1}).          \tag{4.3}
\]

Put \(J_X=\{j:X_j(0)>R_L\}\).  For every fixed deletion
\(S\), \(|S|\le2\), define

\[
 P^{[-S]}=\{k\notin S:X_k(0)\le R_L\},\qquad
 z_i^{[-S]}=\sum_{k\in P^{[-S]}}G_{ik}(0)X_k(0).       \tag{4.3a}
\]

Use buffered dyadic row layers \(I_k^{[-S]}\), based on
\(\max(|A_i(0)|,|z_i^{[-S]}|)\asymp r_k\), and buffered
\(X\)-layers \(J_\ell\).  The bounded common core has
\(|A_i(0)|\vee|z_i^{[-S]}|\le R_L\) and \(X_j(0)\le R_L\).
The cavity buffer \(\beta_n=n^{-1/3}\) is wider than every change caused
by deleting one or two parent columns,
\(\max_i|G_{ij}(0)X_j(0)|=n^{-1/2+o(1)}\), on the parent set used in
Section 6.  To compare the bounded-\(X\) and full row scores, also put
\(\eta_L=e^{-R_L/16}\).  The contribution of all \(X>R_L\) columns is
\(e^{-cR_L+O(\log L)}=o(\eta_L)\), whereas
\(\beta_n=o(\eta_L)\).  A row or column in either buffer is declared a
separate portal.  Thus the interiors of the one- and two-punctured gates
agree exactly, and the global and bounded-\(X\) gates agree outside the
\(\eta_L\)-boundary layer.  The latter layer has superpolynomially small
influence in \(L\).
No gate is defined using \(R_j\): its order-\(L\) maximum is instead
removed from the core Jacobian exactly below.

For unpunctured notation write

\[
 \widetilde Z_i(0)=\sum_{j:X_j(0)\le R_L}G_{ij}(0)X_j(0).
\]

Gaussian tails and binomial Bernstein give, simultaneously,

\[
 \pi_k:=|I_k|/n\le L^C e^{-cr_k^2}+C\log n/n,
 \qquad
 \theta_\ell:=|J_\ell|/n
       \le L^Ce^{-cx_\ell}+C\log n/n.                   \tag{4.4}
\]

The removed-column contribution to the full initial \(Z\) has maximum

\[
 O_{\mathbb P}\!\left(
 L\langle X^2 1_{X>R_L}\rangle_n^{1/2}
 \right)=o(1),                                           \tag{4.5}
\]

because
\(\mathbb E[X^2 1_{X>R_L}]\le C R_L^{3/2}e^{-R_L/2}\).
Thus buffered full-\(Z\) and \(\widetilde Z\) row layers agree away from
the declared \(\eta_L\)-boundary portals.

Let \(P=P^{[-S]}\).  Conditional on \(X(0)\) and
\(z_i^{[-S]}\), the exact row regression on \(P\) is

\[
 G_{iP}(0)
 =\frac{z_i^{[-S]}}{\|X_P(0)\|_2^2}X_P(0)^{\mathsf T}
 +w_iP_{X_P(0)}^\perp,\qquad
 w_i\sim N(0,n^{-1}I).                                  \tag{4.6}
\]

Restriction to a layer \(C\subset P\) uses the restricted mean
\(z_i^{[-S]}X_C^{\mathsf T}/\|X_P\|_2^2\) and the corresponding
principal covariance of \(n^{-1}P_{X_P}^\perp\); it is not a fresh
\(P_{X_C}^\perp\) regression.  Standard Gaussian net bounds, followed
by a union over the \(O(\log L)\) fixed layers and the one-/two-fiber
cavities, give

\[
 \|P_{I_k}(G(0)-G_{\rm reg})P_{J_\ell}\|
 \le C L^C\left(\sqrt{\pi_k}+\sqrt{\theta_\ell}
 +\sqrt{\log n/n}\right).                               \tag{4.7}
\]

The rank-one regression mean \(G_{\rm reg}\) obeys the product of the
corresponding layer tail factors and is smaller than the right side.

Although it is not used as a gate, the initial core score has the exact
one-column decomposition

\[
 R_j(0)=g_j^{\mathsf T}D_{A(0)}z^{[-j]}
       +X_j(0)g_j^{\mathsf T}D_{A(0)}g_j
       +\hbox{fixed-layer portals}.                    \tag{4.7g}
\]

Conditional regression makes the first term a Gaussian of uniformly
bounded variance plus its rank-one mean.  A union bound over columns,
the leverage bound for the second term, and (4.7) therefore give
\(\max_{j\in P}|R_j(0)|\le C_0L\) with probability tending to one.
This order-\(L\) maximum is real and is not replaced by a smaller
regular-score assertion.

We now spell out the dimension-free core estimate.  If
\(\xi=(\alpha,\nu,M)\) is a perturbation, set

\[
 \delta X=2D_u\nu,\qquad \delta Z=MX+G\delta X,
 \qquad
 \|\xi\|_*^2=\|\alpha\|_{2,n}^2+
                    \|\nu\|_{2,n}^2+\|M\|_F^2.        \tag{4.7a}
\]

The feature vector field is the gradient of \(f\) for this metric.  Its
Jacobian is therefore the metric Hessian, whose exact quadratic form is

\[
 \begin{aligned}
 D^2f[\xi,\xi]={}&4\langle\alpha,Z\delta Z\rangle_n\\
 &+2\langle A,(\delta Z)^2\rangle_n\\
 &+4\langle B,M\delta X\rangle_n
 +4\langle R,\nu^2\rangle_n .                         \tag{4.7b}
 \end{aligned}
\]

There is no missing dimensional factor in (4.7b): the \(A,u\) norms are
normalized and the matrix norm is Frobenius, exactly as in (4.2).  On a
common-core first-exit event put

\[
 \begin{gathered}
 \max_{i\in I_C}(|A_i|+|Z_i|)\le M_L,\qquad
 \max_{j\in P}X_j\le C_XR_L,\qquad
 \max_{j\in P}|R_j|\le C_RL,\\
 \|X\|_{2,n}+\|B\|_{2,n}+\|G\|_{\rm op}\le R_L^{D_0},
 \qquad D_0<D.                                         \tag{4.7c}
 \end{gathered}
\]

Here \(C_X,C_R\) are fixed with slack and \(D\) in (4.3) is chosen
strictly larger than the moment exponent \(D_0\).  Under (4.7c),

\[
 \|G(t)-G(0)\|_{\rm op}\le\sqrt{(0.09/L)\delta},\qquad
 \|X(t)-X(0)\|_{2,n}\le C(R_L/L)^{1/2}.                \tag{4.7c'}
\]

The first inequality is Cauchy--Schwarz applied to (4.2); the second uses
\(X=u^2\), \(\|u-u(0)\|_{2,n}\le\sqrt{(0.09/L)\delta}\), and the stopped
bound on \(\|u\|_\infty\).  In particular the core \(G\)-operator norm
and the second \(X\)-moment stay \(O(1)\).  Also

\[
 \|\delta Z\|_{2,n}
 \le \|M\|_F\|X\|_{2,n}
      +2\|G\|_{\rm op}\|u\|_\infty\|\nu\|_{2,n}.       \tag{4.7d}
\]

The last term of (4.7b) cannot be included in an
\(M_LR_L^D\)-bound because \(\max_jR_j\asymp L\).
Let \(\mathcal D_R(t)\) be zero on the \(A,G\) components and equal to
\(4D_{R_P(t)}\) on the \(u_P\) component, and put

\[
 K_C(t)=J_C(t)-\mathcal D_R(t),                         \tag{4.7e}
\]

where \(J_C\) is the projected metric Hessian.  The first three terms of
(4.7b), (4.7d), and Cauchy--Schwarz give

\[
 \|K_C(t)\|_{*\to *}\le C M_LR_L^D                     \tag{4.7f}
\]

under every fixed one-/two-star deletion.  Thus the large diagonal score,
and only that score, has been separated from genuine core scattering.

Use the global diagonal gauge

\[
 T_D(t)=\operatorname{diag}\!\left(
 I_A,\operatorname{diag}_{j\in P}\frac{u_j(t)}{u_j(0)},I_G
 \right).                                              \tag{4.7h}
\]

It is the exact propagator of \(v'=4D_Rv\), because
\(u_j'=4u_jR_j\).  Before the first exit,

\[
 \|T_D^{\pm1}\|\le e^{4C_R(0.09)},\qquad
 \operatorname{Var}_{[0,0.09/L]}T_D^{\pm1}\le C(C_R).  \tag{4.7i}
\]

If \(\Phi_C(t,s)\) is the physical core Green, define
\(\Psi_C(t,s)=T_D(t)^{-1}\Phi_C(t,s)T_D(s)\).  Then

\[
 \partial_t\Psi_C=
 T_D(t)^{-1}K_C(t)T_D(t)\Psi_C,
\]

and therefore

\[
 \|\Psi_C(t,s)-I\|+
 \operatorname{Var}_{r\in[s,t]}\Psi_C(t,r)
 \le C\gamma_L.                                       \tag{4.8a}
\]

The correct physical-frame conclusion is only

\[
 \|\Phi_C(t,s)\|+
 \operatorname{Var}_{r\in[s,t]}\Phi_C(t,r)\le C.       \tag{4.8b}
\]

For every zero-initial source curve \(v\), the product rule gives the
substitution used below:

\[
 \|T_Dv\|_{\infty,*}+\operatorname{Var}_*(T_Dv)
 \le C\{\|v\|_{\infty,*}+\operatorname{Var}_*v\}.       \tag{4.8c}
\]

Thus a small portal remains small after diagonal score dressing.  No
later step uses the false assertion \(\Phi_C-I=o(1)\).

It remains to de-stop (4.7c), including the premise of (4.7i).  At time
zero the gates, (4.7), and (4.7g) give strict versions of all its bounds.
For coordinate propagation use the exact equations

\[
 Z_i'=(2Q+8S_i)A_iZ_i+8N_i,                             \tag{4.8d}
\]

\[
 R_j'=2X_j\langle B^2\rangle_n
 +G_{\cdot j}^{\mathsf T}
 \{Z^3+2QA^2Z+8D_AG(XR)\}.                              \tag{4.8e}
\]

Delete the displayed row or column before forming its coefficient
primitive.  The punctured path is measurable off the fresh Gaussian
fiber.  In (4.8d) retain \((2Q+8S_i)A_iZ_i\) in the exact row block; in
(4.8e), equivalently in (2.3)--(2.7), retain every same-column return in
the exact column block.  More explicitly, (2.2) gives after deleting
column \(j\)

\[
 R_j(t)-R_j(0)
 =g_j(0)^{\mathsf T}
   \{B_c^{[-j]}(t)-B_c^{[-j]}(0)\}+\mathfrak L_j(t),    \tag{4.8e'}
\]

where \(\mathfrak L_j\) is the sum of the exact same-column Volterra
block, the aligned \(2\int x_j\langle B(s),B(t)\rangle_n ds\) term, and
the rank-one trained remainder.  Equations (2.3)--(2.7), \(X_j\le
C_XR_L\), and the finite moment stop give
\(\sup_j\|\mathfrak L_j\|_\infty\le R_L^{O(1)}=o(L)\).
Moreover
\[
 \sup_t\|B_c^{[-j]}(t)-B_c^{[-j]}(0)\|_{2,n}
 +\operatorname{Var}_{2,n}B_c^{[-j]}
 \le C\gamma_L .
\]

Writing the remaining row source as a cavity-measurable coefficient
curve \(v_i(t)\), the action bound and the finite moment stop give
\[
 \sup_t\|v_i(t)\|_{2,n}^2\le CR_L/L,\qquad
 \operatorname{Var}_{2,n}v_i\le R_L^{D}/L.             \tag{4.8e''}
\]
The first estimate is Cauchy--Schwarz in time with
\(\int\langle XR^2\rangle_n\le\delta/16\); differentiating the primitive
and using \(X\le C_XR_L\) gives the second.  Diagonal dressing changes
the variation to at most a constant times the sum of the displayed
radius and variation by (4.8c).  Hence (4.23a) makes its maximum over all
rows
\[
 O\{\sqrt{LR_L}+R_L^D\}=o(M_L).
\]
The remaining column primitive has normalized
radius and variation \(O(\gamma_L)\); (4.23a) gives
\(O(L\gamma_L)=o(L)\).  Rank-one trained pieces carry an explicit
\(1/n\) and are smaller by (2.1).  Hence

\[
 \sup_{i\in I_C}|Z_i(t)-Z_i(0)|=o(M_L),\qquad
 \sup_{j\in P}|R_j(t)-R_j(0)|=o(L).                    \tag{4.8f}
\]

These are leave-one-star Gaussian-curve estimates, not a conversion from
a Hilbert norm to a maximum.  The deleted fiber is held out before the
time net is formed, so the same master event is simultaneous for all
one-row, one-column, and leave-two-column cavities.

Now
\(|A_i(t)-A_i(0)|\le(0.09/L)M_L^2=o(M_L)\), while
\(X_j(t)/X_j(0)=\exp(8\int_0^tR_j)\) stays between two fixed constants.
Choose \(C_X\) and \(C_R>C_0\) with fixed slack and assign the fixed
column boundary to a portal layer.  Equations (4.8f) strictly improve
the three coordinate stops.  Finally (2.1), (4.2), and the finite layer
moments strictly improve
\(\|X\|_{2,n},\|B\|_{2,n},\|G\|_{\rm op}\le R_L^{D_0}\).
Thus the first exit cannot occur and (4.8a)--(4.8c) hold on the whole
interval.  A common deletion core is independent of the deleted star's
score; after that star is restored its response is a portal propagated
by (4.8c), rather than a derivative of the large core diagonal.

### 4.2 Ordered local blocks

Rows are inserted first, with all noncore columns still deleted.  Every
same-row incidence, including the trace of the row-to-core-to-row return,
is retained in its exact local Volterra block.  Equations (2.8)--(2.10),
(4.7), and (4.8a)--(4.8c) give, uniformly over all rows,

\[
 A_i'=Z_i^2,\qquad
 Z_i'=14A_iZ_i+o(L^2)                                    \tag{4.9}
\]

in the scaled row equation, with the same statement for one radial
derivative.  The one-leg core primitive has conditional variance at most

\[
 (0.09/L)R_L\int\langle XR^2\rangle_n
 \le C R_L/L.                                            \tag{4.10}
\]

The maximum over (n) fresh row fibers is therefore
(O(L\sqrt{R_L/L})=o(L)).  The local row resolvent is uniformly bounded by
the (0.11-0.09) pole gap.  Row--row mixed returns carry (4.7), so a
Neumann contraction restores all rows.  Precisely, this is the row-only
specialization of the typed collective synthesis estimate proved in
Section 4.3: the direct row fibers are synthesized first, every
same-row return remains in its exact local block, and the common core
Green is applied only after their canonical sources have been summed.
That specialization uses no column block from the following paragraph,
so this forward reference is not circular.  It produces a
**row-dressed bath** with bounded local row resolvents; no tail row is
subsequently treated as an independent perturbative coordinate.

Next insert one column into this full row-dressed bath.  Thus every
high-row/that-column intersection and every repetition of it belongs to
one exact column block.  Direct differentiation of (2.3)--(2.7) gives

\[
 U_\tau=8U(HU+P),\qquad
 H_\tau=3+e_H,\qquad P_\tau=26U+e_P.                     \tag{4.11}
\]

The four zero-deficit contributions to (26) are, respectively,

\[
 6\quad(g'\hbox{ training}),\qquad
 6\quad(A'=Z^2),\qquad
 6\quad(G_{-j}'\hbox{ training}),\qquad
 8\quad(\hbox{Wishart return}).                          \tag{4.12}
\]

Every repeated same-column trace is already inside (4.11).  Every column
outside \(\mathscr C_L\) has formal pole at least \(T_*+8h_L-o(h_L)\),
whereas the pre-cap horizon is \(T_{\rm pre}=T_*+5h_L\).  Its local
resolvent is therefore at most a fixed power of \(h_L^{-1}\), absorbed
in the displayed \(L^C\) factors.  The \(n^{o(1)}\) columns in
\(\mathscr C_L\) are handled by reciprocal levels in Section 5.  Thus
there is neither an undefined fixed-\(0.095\) class nor a dependence on
the later coarea-selected set.

### 4.2.1 Same-star reciprocal source

The local candidate resolvent needed below is established here, before
the mixed-star homotopy.  Let \((A_c,z_c,G_c,X_c)\) be the common
column-deleted, row-dressed bath and \(B_c=A_c\odot z_c\).  Define

\[
 J(\tau)=L^{-1}g(0)^{\mathsf T}
          \{B_c(\tau/L)-B_c(0)\}.                       \tag{4.12a}
\]

The exact bath equation is

\[
 B_c'=z_c^3+2Q_cA_c^2z_c+8D_{A_c}H_cD_{A_c}z_c,
 \qquad H_c=G_cD_{X_c}G_c^{\mathsf T}.                 \tag{4.12b}
\]

Define
\[
 \mathcal E_0^\circ(s):=g(0)^{\mathsf T}B_c'(s).         \tag{4.12b'}
\]
Thus \(L^{-2}\mathcal E_0^\circ=\partial_\tau J\)
exactly.  The exact one-column equations can consequently
be written

\[
 e_P=r_P+\partial_\tau J,                               \tag{4.12c}
\]

\[
 r_P=U(\mathcal P-26)
 +L^{-2}(\mathcal E_0-\mathcal E_0^\circ)
 +L^2U^2\mathcal E_2 .                                  \tag{4.12d}
\]

Let \(D_b^W\) denote differentiation in the initial Gaussian score while
holding the reciprocal level \(W=U^{-1}\) fixed.  On every compact
outgoing contender set, uniformly for all one- and leave-two-column
baths and for every fixed \(X(0)\)-measurable parent deletion with
normalized \(X^2\)-mass \(n^{-c+o(1)}\), and
\(W\ge W_{\rm cap}=L^2n^{-1/3}\), the reduced-core Green and
conditional Gaussian estimates give

\[
 \max_{k=0,1}\sup_W
 \left\{|(D_b^W)^ke_H|+|(D_b^W)^k(Wr_P)|
                    +|(D_b^W)^kJ|\right\}
 +|H(0)|+|D_bH(0)|\le \epsilon_n,                       \tag{4.12e}
\]

\[
 \epsilon_n=C\gamma_L+n^{-1/6+o(1)}=o((\log L)^{-1}).   \tag{4.12f}
\]

Here are the quantitative estimates proving (4.12e).  Conditional on the
deleted bath and \(g(0)^{\mathsf T}B_c(0)=Lb\),

\[
 g(0)=\frac{Lb}{\|B_c(0)\|_2^2}B_c(0)+\xi,\qquad
 \xi\sim N(0,n^{-1}P_{B_c(0)}^\perp).                  \tag{4.12g}
\]

The diagonal-dressed core Green (4.8a)--(4.8c) gives

\[
 \sup_s\|B_c(s)-B_c(0)\|_{2,n}\le C\gamma_L,\qquad
 \sup_s\|B_c'(s)\|_{2,n}
 +\operatorname{Var}_{2,n}\{B_c'(s):s\le\sigma_{\rm pre}\}
 \le C M_LR_L^D.                                       \tag{4.12h}
\]

The variation assertion in (4.12h) is a separate finite-moment estimate,
not a consequence of the variation of \(B_c\).  Differentiating (4.12b)
gives exactly
\[
\begin{aligned}
B_c''={}&3z_c^2z_c'
+2Q_c'A_c^2z_c+4Q_cA_cA_c'z_c+2Q_cA_c^2z_c'\\
&+8\{D_{A_c'}H_cD_{A_c}z_c+D_{A_c}H_c'D_{A_c}z_c\\
&\hspace{34mm}+D_{A_c}H_cD_{A_c'}z_c
+D_{A_c}H_cD_{A_c}z_c'\},                             \tag{4.12h'}
\end{aligned}
\]
where
\[
\begin{gathered}
 A_c'=z_c^2,\qquad z_c'=2Q_cB_c+8H_cB_c,\qquad
 Q_c'=16\langle X_c^2R_c\rangle_n,\\
 H_c'=G_c'D_{X_c}G_c^{\mathsf T}
       +G_cD_{8X_cR_c}G_c^{\mathsf T}
       +G_cD_{X_c}G_c'^{\mathsf T}.                    \tag{4.12h''}
\end{gathered}
\]
For the only apparently nonlocal term one may use the exact contraction
\[
\begin{aligned}
D_{A_c}H_c'D_{A_c}z_c
={}&2D_{A_c}B_c\,\langle X_c^2R_c\rangle_n
 +8D_{A_c}G_c(X_cR_c^2)\\
&+2\langle B_c^2\rangle_nD_{A_c}G_c(X_c^2).            \tag{4.12h'''}
\end{aligned}
\]
The row and regular-column pole gaps give all normalized moments in this
finite list (degree at most the enlarged master degree \(D\)).
More explicitly, dyadic peeling and (4.7) give
\[
 \sup_{s\le\sigma_{\rm pre}}\left\{
 \langle X_c^3\rangle_n+
 \|D_{A_c}G_c(X_c^2)\|_{2,n}^2+
 \|D_{A_c}G_c(X_cR_c^2)\|_{2,n}^2+
 \mathfrak M_D(s)\right\}
 \le h_L^{-C_D}R_L^{D_0},                              \tag{4.12h4}
\]
where \(\mathfrak M_D\) is the finite sum of the remaining scalar and
one-design words displayed in (4.12h').  Also
\[
 \int_0^{\sigma_{\rm pre}}|\langle X_c^2R_c\rangle_n|\,ds
 \le\left\{\sigma_{\rm pre}\sup_s\langle X_c^3\rangle_n
          \int_0^{\sigma_{\rm pre}}\langle X_cR_c^2\rangle_n ds
    \right\}^{1/2}
 \le h_L^{-C_D}L^{-1/2}.                               \tag{4.12h4a}
\]
Hölder, (4.2), and (4.12h4) now bound every term of
(4.12h') by
\[
 C h_L^{-C_D}R_L^{D_0}(L^{-1}+L^{-1/2})
 \le C M_LR_L^D.
\]
Consequently, uniformly in the one-/two-column cavities,
\[
 \int_0^{\sigma_{\rm pre}}\|B_c''(s)\|_{2,n}\,ds
 \le C M_LR_L^D.                                      \tag{4.12h''''}
\]
This proves the second term in (4.12h) and is included among the strict
first-exit moment stops in Section 4.4.

Gaussian chaining for these rectifiable coefficient curves, including
the union over the required deletion baths, costs at most \(CL\).
At fixed \(W\), the exact derivative is
\[
\begin{aligned}
D_b^WJ={}&L^{-1}(D_bg(0))^{\mathsf T}
              \{B_c(s)-B_c(0)\}\\
&+L^{-2}(D_b^W\tau)\,g(0)^{\mathsf T}B_c'(s),
\qquad s=\tau(W)/L.                                    \tag{4.12h5}
\end{aligned}
\]
The first term is \(O(\gamma_L)\) by (4.12g)--(4.12h).
For the adaptive-time second term, (4.12h'''') and conditional
Gaussian chaining give
\(\sup_s|g(0)^{\mathsf T}B_c'(s)|\le
CLM_LR_L^D\); since \(|D_b^W\tau|\le C\), division by \(L^2\)
again gives \(O(\gamma_L)\).  Thus (4.12g)--(4.12h'''') prove

\[
 \sup_W\{|J|+|D_b^WJ|\}\le C\gamma_L.                  \tag{4.12i}
\]

The first term of \(\mathcal P\) is cavity-measurable, not a quadratic
form in \(g(0)\).  The initial layer law and (4.12h)--(4.12h'''') give
uniformly
\[
 2\langle A_c^2z_c^2\rangle_n=6+O(\gamma_L).
\]
The remaining three \(g(0)\)-quadratic forms have conditional trace
errors \(O(\gamma_L+n^{-1/2+o(1)})\) around \(6,6,8\), respectively;
the quadratic part of (2.7) has trace error of the same size around
\(3\).  Conditional Hanson--Wright is applied only to those three
quadratic forms on the deterministic coefficient net.  Together with
the one-star response bootstrap this gives

\[
 \|\mathcal P-26\|_{C_b^1(W)}+|e_H\|_{C_b^1(W)}
 \le C\gamma_L+n^{-1/6+o(1)},
 \qquad
 \|\mathcal E_2\|_{C_b^1(W)}\le n^{-1+o(1)}.           \tag{4.12j}
\]

The last estimate is a cubic Gaussian-chaos bound, not an application of
Hanson--Wright.  Conditional on the cavity, the two terms have scales
\[
 n^{-1}g(0)^{\mathsf T}(A^2z)=n^{-1+o(1)},\qquad
 \sum_i g_i(0)^3z_i=n^{-1+o(1)},                       \tag{4.12j''}
\]
because the latter has conditional variance
\(O(n^{-2+o(1)})\).  Indeed, after score conditioning
\(g=\mu+\xi\), \(\operatorname{Cov}\xi=n^{-1}P_{B^\perp}\);
Isserlis' formula adds the off-diagonal terms
\(9C_{ii}C_{jj}C_{ij}+6C_{ij}^3\) and the \(\mu\)-terms, but
\(\|C\|_{\rm op}\le n^{-1}\) and \(\|\mu\|_2=n^{-1/2+o(1)}\)
make their total \(O(n^{-2+o(1)})\).  One score derivative replaces
one \(g_i\) by \(L B_i(0)/\|B(0)\|_2^2\) and has the same
\(n^{-1+o(1)}\) scale.  A polynomial time net plus the response estimate
(4.12j') makes this uniform at fixed \(W\).

Likewise
\[
 H(0)=L\sum_iA_i(0)g_i(0)^2,\qquad
 D_bH(0)=2L\sum_iA_i(0)g_i(0)D_bg_i(0)
\]
are \(n^{-1/2+o(1)}\) by the same conditional chaos estimate.  This
supplies the initial errors in (4.12e).

For clarity, the “response bootstrap” in this sentence is the following
quantitative estimate.  After the explicit \(xg\) component of \(Z\) and
the exact diagonal \(j\)-return have been removed, the forcing of the
common bath has normalized \(L^1\)-size

\[
 a_j\le n^{-1/2}L^C\int_0^{s_x}x(s)\,ds
       +n^{-1}L^C\int_0^{s_x}x(s)^2\,ds
     =n^{-1/2+o(1)}+n^{-2/3+o(1)}.                     \tag{4.12j'}
\]

The diagonal-dressed source estimate (4.8c) preserves this bound.  At fixed
terminal \(W\),
differentiating the two exposure integrals gives the same estimate.
Therefore every adaptive coefficient matrix in (4.12j) is its
cavity-measurable counterpart plus \(n^{-1/2+o(1)}\) in the relevant
quadratic-form norm.  Hanson--Wright is applied only to the latter; the
response difference is then bounded deterministically.  This avoids
conditioning a Gaussian fiber on its own evolved coefficient.

For the only remaining response term, differentiating the full bath from
the deleted bath and retaining the explicit \(xg\) source gives

\[
 \|\mathcal E_0-\mathcal E_0^\circ\|_{C_b^1(W)}
 \le C M_LR_L^D\int_0^s x
 +n^{-1/2+o(1)}\int_0^s x^2
 +n^{-1/6+o(1)}x .                                     \tag{4.12k}
\]

Here is the promised exact response estimate.  In the bath coordinates
with column \(j\) omitted, let
\[
 \vartheta_c=(A_c,u_c,G_c),\qquad
 X_c=u_c^2,\quad z_c=G_cX_c,\quad B_c=D_{A_c}z_c
\]
be the row-dressed cavity, and let
\(\vartheta=(A,u,G)\) be the corresponding bath after inserting the
tag \((x,g)\).  Put
\[
 a=A-A_c,\quad v=u-u_c,\quad M=G-G_c,\quad
 \delta g=g-g(0),
\]
\[
\begin{aligned}
 \delta X&=2u_c\odot v+v^2,\\
 \delta z&=MX_c+G_c\delta X+M\delta X,\\
 \delta B&=D_{A_c}\delta z+D_a z_c+D_a\delta z .
\end{aligned}                                           \tag{4.12n}
\]
Direct subtraction of the two canonical systems gives the exact
full-minus-cavity equations
\[
\begin{aligned}
a'={}&2z_c\delta z+(\delta z)^2
 +2x(z_c+\delta z)(g(0)+\delta g)
 +x^2(g(0)+\delta g)^2,\\
v'={}&4\{(u_c+v)\odot(G_c+M)^{\mathsf T}(B_c+\delta B)
             -u_c\odot G_c^{\mathsf T}B_c\}\\
&\quad+4x(u_c+v)\odot(G_c+M)^{\mathsf T}
                 D_{A_c+a}(g(0)+\delta g),\\
M'={}&\frac2n\{(B_c+\delta B)(X_c+\delta X)^{\mathsf T}
                  -B_cX_c^{\mathsf T}\}\\
&\quad+\frac{2x}{n}D_{A_c+a}(g(0)+\delta g)
                         (X_c+\delta X)^{\mathsf T},\\
\delta g'={}&\frac{2x}{n}B_c+\frac{2x^2}{n}D_{A_c}g(0)
 +\frac{2x}{n}\delta B\\
&\quad+\frac{2x^2}{n}
       \{D_{A_c+a}(g(0)+\delta g)-D_{A_c}g(0)\}.
\end{aligned}                                           \tag{4.12o}
\]
In particular, after the cavity-linear part is put in its Green, the
only response-free sources are
\[
\begin{aligned}
S_1={}&\left(2xz_cg(0),\
 4xu_c\odot G_c^{\mathsf T}D_{A_c}g(0),\
 \frac{2x}{n}D_{A_c}g(0)X_c^{\mathsf T},\
 \frac{2x}{n}B_c\right),\\
S_2={}&\left(x^2g(0)^2,\ 0,\ 0,\
 \frac{2x^2}{n}D_{A_c}g(0)\right).
\end{aligned}                                           \tag{4.12p}
\]
Every other monomial in (4.12o) contains at least one of
\(a,v,M,\delta g\).

Define
\[
 V(\vartheta)=z^3+2QA^2z+8D_AHD_Az,\qquad
 H=GD_XG^{\mathsf T},\qquad Q=\langle X^2\rangle_n,
\]
and put
\[
 \delta Q=\langle (X+X_c)\delta X\rangle_n,
\]
\[
 \delta H
 =M D_XG^{\mathsf T}
  +G_cD_{\delta X}G^{\mathsf T}
  +G_cD_{X_c}M^{\mathsf T}.                             \tag{4.12q}
\]
These identities are exact.

For the fixed layers of Section 4.1, write
\(\langle r_k\rangle=1+r_k\), \(\langle x_\ell\rangle=1+x_\ell\), and
for nonempty layers define
\[
\begin{aligned}
 \|y\|_{\mathrm r,D}
 &=\|y\|_{2,n}
   +\max_k\frac{\langle r_k\rangle^D}{\sqrt{\pi_k}}
                 \|P_{I_k}y\|_{2,n},\\
 \|w\|_{\mathrm c,D}
 &=\|w\|_{2,n}
   +\max_\ell\frac{\langle x_\ell\rangle^D}{\sqrt{\theta_\ell}}
                 \|P_{J_\ell}w\|_{2,n},\\
 \|N\|_{\mathrm{rc},D}
 &=\|N\|_F+\max_{k,\ell}
   \frac{\langle r_k\rangle^D\langle x_\ell\rangle^D}
        {\sqrt{\pi_k\theta_\ell}}
   \|P_{I_k}NP_{J_\ell}\|_F .                           \tag{4.12r}
\end{aligned}
\]
For a row-indexed fresh-fiber response \(h\), also put
\[
 \|h\|_{\mathrm f,D}
 =\|h\|_2+\sqrt n\max_k
 \frac{\langle r_k\rangle^D}{\sqrt{\pi_k}}
 \|P_{I_k}h\|_{2,n}.                                   \tag{4.12s}
\]
The powers exceed the degree of every multiplier below.  Consequently
multiplication by any permitted product of cavity row or column marks
maps these influence norms to ordinary normalized \(L^2\), without an
\(L^\infty\)-to-\(L^2\) loss.

For \(d=(a,v,M)\), set
\[
\begin{aligned}
 \mathfrak I_D(d):={}&
 \|a\|_{\mathrm r,D}+\|\delta z\|_{\mathrm r,D}
 +\|\delta B\|_{\mathrm r,D}
 +\|v\|_{\mathrm c,D}+\|\delta X\|_{\mathrm c,D}
 +\|M\|_{\mathrm{rc},D}\\
 &+|\delta Q|+\|\delta H\|_{\rm op}\\
 &+\max_{p+q+r+t\le D}
 \|D_{A_c^pz_c^q}\delta H(A_c^rz_c^t)\|_{2,n}.
                                                               \tag{4.12t}
\end{aligned}
\]
The final line is the finite \(2\to\infty\) family needed when
\(\delta H\) lies between row multipliers.  The fixed-layer block bound
(4.7), exact row resolvents, and (4.8c) say that the original
row-/diagonal-dressed state Green acts boundedly on \(\mathfrak I_D\).
No augmented-observable Green is introduced.

For a reciprocal hit \(W\), let
\[
 I_m(W)=\int_0^{s(W)}x(r)^m\,dr,
\]
\[
\begin{aligned}
 A_*(W)&=L^{C_D}\{n^{-1/2}I_1(W)+n^{-1}I_2(W)\},\\
 \beta_g(W)&=R_L^D\{n^{-1/2}I_1(W)+n^{-1}I_2(W)\},\\
 \Omega(W)&=M_LR_L^DI_1(W)+n^{-1/2+o(1)}I_2(W)
             +n^{-1/6+o(1)}x(W),
\end{aligned}                                           \tag{4.12u}
\]
where \(C_D\) covers the finitely many layer nets.  Define the direct
output
\[
 Y(W)=g(0)^{\mathsf T}
       \{V(\vartheta(s(W)))-V(\vartheta_c(s(W)))\}.
\]
The response norm is
\[
\begin{aligned}
 \|(d,\delta g)\|_{\mathcal R,1}
 :=\sup_{W_{\rm cap}\le W\le W_0}\Bigg[
 &\frac{\mathfrak I_D(d)+\mathfrak I_D(D_b^Wd)}{A_*(W)}\\
 &+\frac{\|\delta g\|_2+\|D_b^W\delta g\|_2}{\beta_g(W)}\\
 &+\frac{\|\delta g\|_{\mathrm f,D}
              +\|D_b^W\delta g\|_{\mathrm f,D}}{A_*(W)}\\
 &+\frac{|Y(W)|+|D_b^WY(W)|}{\Omega(W)}
 \Bigg].                                                \tag{4.12v}
\end{aligned}
\]
Zero-over-zero values at \(W=W_0\) mean right limits.

To estimate the output, telescope its factors exactly:
\[
 z^3-z_c^3=3z_c^2\delta z+3z_c(\delta z)^2+(\delta z)^3, \tag{4.12w1}
\]
\[
 QA^2z-Q_cA_c^2z_c
 =\delta Q\,A^2z+Q_c(2A_ca+a^2)z+Q_cA_c^2\delta z,     \tag{4.12w2}
\]
and
\[
\begin{aligned}
 D_AHD_Az-D_{A_c}H_cD_{A_c}z_c
={}&D_aHD_Az+D_{A_c}\delta H D_Az\\
 &+D_{A_c}H_cD_az+D_{A_c}H_cD_{A_c}\delta z.           \tag{4.12w3}
\end{aligned}
\]
Thus every term contains a response factor.  Its exact linear part is
\[
\begin{aligned}
 \mathcal L_Vd={}&3z_c^2\delta z_1
 +2\delta Q_1A_c^2z_c+4Q_cA_ca z_c+2Q_cA_c^2\delta z_1\\
 &+8\{D_aH_cD_{A_c}z_c
 +D_{A_c}\delta H_1D_{A_c}z_c
 +D_{A_c}H_cD_az_c
 +D_{A_c}H_cD_{A_c}\delta z_1\},                       \tag{4.12w4}
\end{aligned}
\]
where
\[
\begin{gathered}
 \delta X_1=2u_c\odot v,\qquad
 \delta z_1=MX_c+G_c\delta X_1,\qquad
 \delta Q_1=2\langle X_c,\delta X_1\rangle_n,\\
 \delta H_1=MD_{X_c}G_c^{\mathsf T}
  +G_cD_{\delta X_1}G_c^{\mathsf T}
  +G_cD_{X_c}M^{\mathsf T}.
\end{gathered}
\]
Every term in
\(\mathcal N_V(d)=V(\vartheta)-V(\vartheta_c)-\mathcal L_Vd\)
has at least two response factors.  Equations
(4.12w1)--(4.12w3) and \(\mathfrak I_D\) turn each multiplication here
into an ordinary normalized-\(L^2\) estimate.

Apply the original dressed state Green to (4.12o).  The three sources
linear in \(g(0)\) give
\[
 d_1(s)=\int_0^s x(r)\Phi_c(s,r)\mathsf S_1(r)g(0)\,dr.
\]
Consequently
\[
 g(0)^{\mathsf T}\mathcal L_Vd_1(s)
 =\int_0^s x(r)g(0)^{\mathsf T}K_1(s,r)g(0)\,dr,       \tag{4.12w5}
\]
where \(K_1\) is cavity-measurable.  The influence bounds and the
row-/diagonal-dressed Green give, uniformly on the two-parameter
rectifiable net,
\[
 \sup_{s,r}\|K_1(s,r)\|_{\rm op}
 +\operatorname{Var}_{s,r}K_1\le L^{C_D}=n^{o(1)},
 \qquad
 n^{-1}|\operatorname{tr}K_1(s,r)|\le CM_LR_L^D,\qquad
 n^{-1}\|K_1(s,r)\|_F\le n^{-1/2+o(1)}.                \tag{4.12w6}
\]
The loose operator bound allows the genuine diagonal multiplier
\(\operatorname{diag}(8Q_cA_iz_i^2)\), whose largest entry can be
polylogarithmic.  The normalized trace bound is proved separately:
expand the finite kernel into its diagonal row multipliers and
row--column design blocks; then
\(\sum_k\pi_kr_k^{D'}\le CM_LR_L^D\) for every occurring degree
\(D'\), while centered design blocks have zero trace up to
\(n^{-1/2+o(1)}\).  The normalized Frobenius bound follows from the
same layer square-moment sum (or from
\(\|K_1\|_F\le\sqrt n\|K_1\|_{\rm op}\)).
The variation bound follows by differentiating the finite kernel once;
its coefficient derivatives are exactly the finite family already
bounded in (4.12h')--(4.12h'''') and the dressed Green has bounded
physical variation by (4.8b).
Conditional Hanson--Wright, including the rank-one mean and covariance
correction in (4.12g), bounds (4.12w5) by
\(CM_LR_L^DI_1(W)\).  The \(x^2g(0)^2\) source gives a cubic conditional
Gaussian kernel, and the same influence estimates or conditional chaos
give
\[
 |g(0)^{\mathsf T}\mathcal L_Vd_2|
 \le n^{-1/2+o(1)}I_2(W).                               \tag{4.12w7}
\]

The preceding \(L^2\) estimates are not, by themselves, an algebra: an
arbitrary vector of bounded normalized \(L^2\)-norm may concentrate on
one coordinate.  We therefore record the special multiplier estimate
which is used for the nonlinear insertion response and for its one score
derivative.  This estimate concerns only the full-minus-cavity
difference; neither endpoint score jet is claimed to be small.

Put

\[
 \eta=\delta g,\qquad \xi=\delta X,\qquad
 \zeta=\delta z,\qquad \beta=\delta B.
\]

If \(i\in I_k\) and \(r\in J_\ell\), set
\(\varpi_i=\langle r_k\rangle\) and
\(\upsilon_r=\langle x_\ell\rangle\).  Enlarge the fixed master degree
once, if necessary, and fix \(d_0<D-10\).  Define the sharp difference
norm

\[
\begin{aligned}
 [d]_{\sharp}:={}&
 \max_i\varpi_i^{-d_0}
    (|a_i|+|\zeta_i|+|\beta_i|+\sqrt n\,|\eta_i|)\\
 &+\max_{r\ne j}\upsilon_r^{-d_0}(|v_r|+|\xi_r|)\\
 &+\sqrt n\max_i\varpi_i^{-d_0}\|e_i^{\mathsf T}M\|_2
   +\sqrt n\max_{r\ne j}\upsilon_r^{-d_0}\|Me_r\|_2 .
                                                               \tag{4.12w7a}
\end{aligned}
\]

The last line is the layerwise row and column \(2\to\infty\) norm.
For a curve on \([W,W_0]\), append \({\rm BV}\) to the bracket to mean
its supremum plus
\(\int_W^{W_0}[\partial_\omega d(\omega)]_\sharp\,d\omega\).

**Special difference-score multiplier lemma.**  On the master
one-/two-cavity event, uniformly in the parent deletion and in
\(W_{\rm cap}\le W\le W_0\),

\[
 \sum_{m=0}^1[(D_b^W)^m d]_{\sharp,{\rm BV};[W,W_0]}
 \le C L^{C_D}\{n^{-1/2}I_1(W)+n^{-1}I_2(W)\}.        \tag{4.12w7b}
\]

The same estimate holds for \(\delta Q,\delta H\), with absolute value
and operator norm respectively, and for every sandwiched
\(2\to\infty\) occurrence of \(\delta H\) in (4.12t).  Moreover

\[
 \max_i\varpi_i^{-d_0}x
 \bigl(|g_i(0)+\eta_i|+|D_b^Wg_i(0)+D_b^W\eta_i|\bigr)
 \le n^{o(1)}\frac{x}{\sqrt n}.                        \tag{4.12w7c}
\]

Write \(\Lambda=H+PW\), the radial quantity denoted by \(\lambda\) in
Section 5.  This capital letter anticipates the distinction from the
mixed homotopy parameter in Section 4.3.
Since \(\Lambda\ge c/2\), the exact reciprocal formula gives

\[
 I_1(W)\le CL\{1+\log(W_0/W)\},\qquad
 I_2(W)\le CLx(W).
\]

Consequently the right side of (4.12w7b) is
\(n^{-1/2+o(1)}\), while (4.12w7c) is at most
\(n^{-1/6+o(1)}\).

To prove the lemma, first observe the exact moving-clock cancellation.
If \(e_c\) is a cavity bath variable, \(e=e_c+\Delta e\) is its full
counterpart, and \(c_b=D_b^W\Theta_j/L\), then

\[
 D_b^W\Delta e=(D_be-D_be_c)|_{s=\Theta_j/L}
                  +c_b(e'-e_c').                       \tag{4.12w7d}
\]

Thus the common velocity cancels.  Equivalently, along the reciprocal
curve, with \(\Delta F\) equal to the right side of (4.12o),

\[
 \partial_W\widehat d=-\frac{\Delta F}{8L\Lambda},\qquad
 \partial_WD_b^W\widehat d
 =-\frac{D_b^W\Delta F}{8L\Lambda}
   +\frac{(D_b^W\Lambda)\Delta F}{8L\Lambda^2}.        \tag{4.12w7e}
\]

Here \(x=L^2/W\) is fixed under \(D_b^W\).  Formula (4.12w7e),
rather than differentiation of the two endpoints separately, also
gives the asserted one-\(W\)-derivative estimate.  Its integral is
measured by the same \(I_1,I_2\); in particular, there is no boundary
term of size \(xD_b^W\Theta_j\).

The score regression (4.12g) gives

\[
 D_bg(0)=\eta_b:=\frac{LB_c(0)}{\|B_c(0)\|_2^2},\qquad
 \|\eta_b\|_2=O(L/\sqrt n),\qquad
 |\eta_{b,i}|\le n^{-1+o(1)}\varpi_i^{d_0}.            \tag{4.12w7f}
\]

The same regression, (4.6), and Gaussian chaining on the rectifiable
coefficient curves give, simultaneously on the deletion nets,

\[
\begin{aligned}
 |g_i(0)|&\le n^{-1/2+o(1)}\varpi_i^{d_0},\\
 |(G_c^{\mathsf T}D_{A_c}g(0))_r|
 +|D_b^W(G_c^{\mathsf T}D_{A_c}g(0))_r|
 &\le n^{-1/2+o(1)}\upsilon_r^{d_0}.
                                                               \tag{4.12w7g}
\end{aligned}
\]

When a tested row or column occurs in the coefficient curve, delete it
first.  The cavity part is then independent of its residual Gaussian
fiber, so the elementary arc-length estimate (4.23a) applies.  The
regression mean and the change from the punctured score are rank-one
terms of size \(n^{-1+o(1)}\).  Restore the fiber through its exact row
or column block.  The row pole gap and the regular-column gap bound the
first derivative of that local map by \(n^{o(1)}\); every same-row or
same-column repetition remains in that block.

For the score derivative, make the otherwise implicit two-direction
bootstrap explicit.  Let \(\mathfrak E_2^{\rm sp}\) be the stopped norm
of the mixed derivative of the one-star local solution map in the score
direction and one residual-fiber direction, and let

\[
 \kappa(W)=L^{C_D}\{n^{-1/2}I_1(W)+n^{-1}I_2(W)\},\qquad
 q_n^\sharp=n^{o(1)}x/\sqrt n+\kappa=o(1).
\]

At score order zero, first telescope every polynomial between the two
stopped endpoints.  One finite difference is then a pointwise
endpoint-dominated multiplier and the other operations are the
fixed-block \(G,G^{\mathsf T}\) maps and the normalized outer product.
The row/regular-column local Greens therefore give
\(\mathfrak E_1\le C+Cq_n^\sharp\mathfrak E_1\), so
\(\mathfrak E_1\le2C\) before the score bootstrap.  This preliminary
step uses no product of two arbitrary \(L^2\) tangents.

Conditional Gaussian log-Sobolev/chaining and the exact local equations
give the coupled first-exit inequalities

\[
\begin{aligned}
 \mathfrak P&\le C\kappa(W)(1+\mathfrak E_2^{\rm sp})
       +Cq_n^\sharp\mathfrak P,\\
 \mathfrak E_2^{\rm sp}&\le C(1+\mathfrak E_1^2)
       +C(q_n^\sharp+\mathfrak P)\mathfrak E_2^{\rm sp}.
                                                               \tag{4.12w7g'}
\end{aligned}
\]

Here \(\mathfrak P\) is the left side of (4.12w7b), and the ordinary
first-derivative constant \(\mathfrak E_1\) is bounded by the already
proved undifferentiated local block estimate.  The only new coefficient
in the second inequality is a polarization of the finite word list
below; it is either an explicit star operator or a sharp difference
multiplier.  Start with fixed loose stops for
\(\mathfrak E_2^{\rm sp}\) and \(\mathfrak P/\kappa\).  The first
inequality strictly improves the sharp stop, and then the second
strictly improves the mixed-derivative stop.  This is a simultaneous
finite-dimensional first-exit argument, not an invocation of (4.15m)
or of the collective mixed theorem.

The chaining input in this argument is only the elementary
leave-one-fiber Gaussian curve estimate stated later as (4.23a); its
proof is an arc-length net and a union bound and is independent of
(4.16).  Conditioning on the score changes the fresh column by the
rank-one mean and projector in (4.12g).  Deleting the tested row first
makes the remaining curve measurable off that row.  The deleted summand
changes the score by \(n^{-1/2+o(1)}\); multiplied by the loose radial
response, its sharp bath contribution is \(n^{-1+o(1)}\).  The
rank-one mean and covariance-projector corrections have the same or
smaller size and are included in (4.12w7g').

The response-free sources (4.12p) have sharp size

\[
 CL^{C_D}\{n^{-1/2}I_1+n^{-1}I_2\}.                   \tag{4.12w7h}
\]

Indeed, their components use, respectively,
\(xz_cg(0)\), \(xu_cG_c^{\mathsf T}D_{A_c}g(0)\),
\(xD_{A_c}g(0)X_c^{\mathsf T}/n\), and \(xB_c/n\);
the \(S_2\)-components use \(x^2g(0)^2\) and
\(x^2D_{A_c}g(0)/n\).  For example,

\[
\begin{aligned}
 \sqrt n\left\|e_i^{\mathsf T}
   \int\frac{2x}{n}D_{A_c}g(0)X_c^{\mathsf T}ds\right\|_2
 &\le n^{-1/2+o(1)}I_1,\\
 \sqrt n\left|\int\left(\frac{2x}{n}B_{c,i}
       +\frac{2x^2}{n}A_{c,i}g_i(0)\right)ds\right|
 &\le n^{o(1)}\{n^{-1/2}I_1+n^{-1}I_2\}.
\end{aligned}
\]

The column bounds are identical after transposition.  Differentiating
these sources replaces one \(g(0)\) by (4.12w7f), or differentiates a
cavity coefficient which still multiplies the displayed fresh star
leg.  It therefore gives no larger bound.

For exhaustiveness split the exact derived differences as

\[
\begin{gathered}
 \xi_1=2u_c\odot v,\qquad \xi_2=v^2,\qquad
 \xi=\xi_1+\xi_2,\\
 \zeta_1=MX_c+G_c\xi_1,\qquad
 \zeta_2=G_c\xi_2+M\xi,\qquad \zeta=\zeta_1+\zeta_2,\\
 \beta_1=D_{A_c}\zeta_1+D_a z_c,\qquad
 \beta_2=D_{A_c}\zeta_2+D_a\zeta,\qquad
 \beta=\beta_1+\beta_2.                                \tag{4.12w7i0}
\end{gathered}
\]

After the cavity-linear terms and \(S_1,S_2\) are removed, the response
words in (4.12o) are exactly

\[
\begin{array}{c|l}
a'&
 2z_c\zeta_2+\zeta^2;\quad
 2x(z_c\eta+\zeta g(0)+\zeta\eta);\quad
 x^2(2g(0)\eta+\eta^2)\\[1mm]
v'/4&
 u_c\odot G_c^{\mathsf T}\beta_2
 +v\odot M^{\mathsf T}B_c+v\odot G_c^{\mathsf T}\beta
 +u_c\odot M^{\mathsf T}\beta+v\odot M^{\mathsf T}\beta;\\
&x\displaystyle\sum_{e\in\{0,1\}^4\setminus\{0\}}
 u^{(e_1)}\odot(G^{(e_2)})^{\mathsf T}
 D_{A^{(e_3)}}g^{(e_4)}\\[1mm]
M'& (2/n)\{\beta_2X_c^{\mathsf T}+B_c\xi_2^{\mathsf T}
                     +\beta\xi^{\mathsf T}\};\quad
 (2x/n)\displaystyle\sum_{e\in\{0,1\}^3\setminus\{0\}}
 D_{A^{(e_1)}}g^{(e_2)}(X^{(e_3)})^{\mathsf T}\\[1mm]
\eta'& (2x/n)\beta+(2x^2/n)
       \{D_ag(0)+D_{A_c}\eta+D_a\eta\}.
                                                               \tag{4.12w7i}
\end{array}
\]

Here
\(u^{(0)}=u_c,u^{(1)}=v\),
\(G^{(0)}=G_c,G^{(1)}=M\),
\(A^{(0)}=A_c,A^{(1)}=a\),
\(g^{(0)}=g(0),g^{(1)}=\eta\), and
\(X^{(0)}=X_c,X^{(1)}=\xi\).  Thus a one bit selects the response
entry and a zero bit selects the cavity entry; the all-zero word is
precisely the already removed source.  The cavity-linear Green terms are

\[
 2z_c\zeta_1,\qquad
 v\odot G_c^{\mathsf T}B_c+u_c\odot M^{\mathsf T}B_c
 +u_c\odot G_c^{\mathsf T}\beta_1,\qquad
 \frac2n(\beta_1X_c^{\mathsf T}+B_c\xi_1^{\mathsf T}).
\]

For clarity, polarize this finite table once in the special score
difference \(\dot d=D_b^Wd\) and once in an arbitrary local tangent
\(\widehat d\).  The coordinatewise products with no Hilbert-space
normalization are precisely
\[
\begin{array}{c|l}
a'&
2\dot\zeta\,\widehat\zeta,\quad
2x(\dot\zeta\,\widehat\eta+
      \widehat\zeta\,\dot\eta),\quad
2x^2\dot\eta\,\widehat\eta\\
v'&
\dot v\odot\widehat M^{\mathsf T}B_c+
 \widehat v\odot\dot M^{\mathsf T}B_c,\quad
\dot v\odot G_c^{\mathsf T}\widehat\beta+
 \widehat v\odot G_c^{\mathsf T}\dot\beta,\\
&u_c\odot(\dot M^{\mathsf T}\widehat\beta+
                  \widehat M^{\mathsf T}\dot\beta),\\
\text{derived}&
2\dot v\odot\widehat v,\quad
G_c(2\dot v\odot\widehat v)+
 \dot M\widehat\xi+\widehat M\dot\xi,\quad
D_{\dot a}\widehat\zeta+D_{\widehat a}\dot\zeta,\\
\eta'&D_{\dot a}\widehat\eta+D_{\widehat a}\dot\eta .
                                                               \tag{4.12w7i'}
\end{array}
\]
The pair polarizations of the tagged four-bit words are obtained by
choosing the two differentiated one-bits; any word with at least three
one-bits retains an endpoint-dominated difference.  The \(M'\)-words
are normalized outer products, and the \(Q,H\)-words are normalized
inner products or sandwiched matrix maps.  Thus (4.12w7i') is the
complete list of places where a coordinatewise multiplier estimate,
rather than a Hilbert-space identity, is required.

Every remaining word either has two response factors or an explicit
candidate operator.  In the existing norms the latter have sizes

\[
 n^{o(1)}x/\sqrt n,\qquad n^{o(1)}x^2/n,
\]

and \(x^2/n\le x/\sqrt n\) before the cap.  The exact endpoint
telescopes

\[
 \xi=(u+u_c)\odot v,\qquad
 \zeta=M(X_c+\xi)+G_c\xi,\qquad
 \beta=D_a(z_c+\zeta)+D_{A_c}\zeta                    \tag{4.12w7j}
\]

show explicitly how one undifferentiated response in a nonlinear word
is pointwise dominated by its two stopped endpoints.

For the output remainder set
\[
\begin{gathered}
 q_1=2\langle X_c,\xi_1\rangle_n,\qquad
 q_2=\delta Q-q_1
      =2\langle X_c,\xi_2\rangle_n+\langle\xi^2\rangle_n,\\
 h_1=\delta H_1,\qquad h_2=\delta H-h_1\\
 =M D_{X_c}M^{\mathsf T}+M D_\xi G_c^{\mathsf T}
   +M D_\xi M^{\mathsf T}
   +G_cD_{\xi_2}G_c^{\mathsf T}+G_cD_\xi M^{\mathsf T}.
                                                               \tag{4.12w7j''}
\end{gathered}
\]
Then the remainder after (4.12w4) is exactly
\[
 \mathcal N_V=N_z+2N_Q+8N_H,                           \tag{4.12w7j'''}
\]
where
\[
\begin{aligned}
N_z={}&3z_c^2\zeta_2+3z_c\zeta^2+\zeta^3,\\
N_Q={}&q_2A_c^2z_c+\delta Q(2A_ca+a^2)z_c
       +\delta Q A^2\zeta+Q_ca^2z_c\\
 &\quad+Q_c(2A_ca+a^2)\zeta+Q_cA_c^2\zeta_2,\\
N_H={}&D_aH_cD_az_c+D_aH_cD_A\zeta+D_a\delta H D_Az\\
 &\quad+D_{A_c}h_2D_{A_c}z_c
       +D_{A_c}\delta H(D_az_c+D_A\zeta)\\
 &\quad+D_{A_c}H_cD_a\zeta+D_{A_c}H_cD_{A_c}\zeta_2.
\end{aligned}
\]
Thus the output table also contains no hidden \(L^2\cdot L^2\)
operation: after one score derivative, every coordinatewise
polarization has either an endpoint-dominated difference or the sharp
score multiplier (4.12w7b); the remaining contractions are normalized
inner products, sandwiched \(H\)-maps, or \(1/n\) outer products.  A
score derivative
either hits a sharp difference or a common coefficient still multiplied
by a sharp difference.  In addition,

\[
 \delta Q=\langle(2X_c+\xi)\xi\rangle_n,\qquad
 \delta H=MD_XG^{\mathsf T}+G_cD_\xi G^{\mathsf T}
             +G_cD_{X_c}M^{\mathsf T},
\]

and their score derivatives give

\[
 \|\delta H\|_{\rm op}+\|D_b^W\delta H\|_{\rm op}
 +|\delta Q|+|D_b^W\delta Q|\le n^{o(1)}\mathfrak P(W),
\]

with the same bound for the finite sandwiched family in (4.12t).
Hadamard products use the pointwise part of (4.12w7a), matrix products
use its two \(2\to\infty\) parts together with (4.12r), and outer
products use the exact \(1/n\) Frobenius identity.  Thus the special
insertion first exit gives

\[
 \mathfrak P(W)
 \le C\kappa(W)
 +C\{n^{o(1)}x/\sqrt n+\mathfrak P(W)\}\mathfrak P(W).
                                                               \tag{4.12w7j'}
\]

Starting from zero at \(W_0\), (4.12w7g') and (4.12w7j') strictly
improve both loose stops and prove (4.12w7b), using only the special
insertion sources and the already constructed row and regular-column
blocks.

Finally, the special lemma is precisely the missing multiplier estimate.
For every arbitrary local tangent \(\widehat Y\), the fixed-layer
definitions, with the finite layer powers absorbed in \(n^{o(1)}\),
give

\[
 \|2(D_b^W\zeta)\odot\widehat Z\|_{\mathrm r,D}
 \le n^{-1/2+o(1)}\|\widehat Z\|_{\mathrm r,D}.         \tag{4.12w7k}
\]

All other cross terms are the polarizations of (4.12w7i),
(4.12w7j), and (4.12w1)--(4.12w3).  If \(\Delta J\) denotes the
full-minus-cavity bath Jacobian, its large same-star outer block being
kept in the exact \((P,\Lambda)\) system, they obey

\[
 \|\Delta J\,\widehat Y\|_{\mathrm{src},j}^{W}
 \le C\{\gamma_L+n^{-1/6+o(1)}\}
      \|\widehat Y\|_{\mathrm{loc},j}^{W},              \tag{4.12w7l}
\]

and

\[
 \|D_b^W(\Delta J\,\widehat Y)\|_{\mathrm{src},j}^{W}
 \le C\{\gamma_L+n^{-1/6+o(1)}\}
   \{\|\widehat Y\|_{\mathrm{loc},j}^{W}
    +\|D_b^W\widehat Y\|_{\mathrm{loc},j}^{W}\}.        \tag{4.12w7l'}
\]

Algebraically, the zero-label common term is absent because

\[
 D_b^W\{DF(e)-DF(e_c)\}
 =[D^2F(e)-D^2F(e_c)][D_b^We_c,\,\cdot]
   +D^2F(e)[D_b^W(e-e_c),\,\cdot].                     \tag{4.12w7m}
\]

The first bracket retains an undifferentiated insertion leg; the second
is controlled by (4.12w7b).  The common-clock derivative belongs to
the doubled common Green and is not claimed to be small.  Along the
mixed homotopy the same proof adds the already exposed factor \(q_L\)
to (4.12w7l)--(4.12w7l') and closes simultaneously with (4.19a4).

Equations (4.12w7i)--(4.12w7m) now exhaust the step which cannot be
obtained from \(L^2\) algebra.  At score order zero, each nonlinear word
is endpoint-dominated and carries either another response or an explicit
candidate factor.  At score order one, its only potentially unsafe
polarization has one sharp difference-score multiplier and is bounded by
(4.12w7k).  The exact \(\mathcal N_V\)-table
(4.12w7j'')--(4.12w7j''') has the same alternatives.  The state and
output estimates therefore combine to
\[
 \|(d,\delta g)\|_{\mathcal R,1}
 \le C+Cq_n\|(d,\delta g)\|_{\mathcal R,1},             \tag{4.12w8}
\]
\[
 q_n=C\{\gamma_L+\sup_Wx(W)/\sqrt n+\sup_WA_*(W)\}
 =C\{\gamma_L+n^{-1/6+o(1)}\}=o(1).                    \tag{4.12w9}
\]
This is exhaustive because (4.12p) lists every response-free source and
(4.12w7i) lists every remaining primitive response word.

For the fixed-\(W\) derivative,
\[
 I_m(W)=\frac{L^{2m-1}}8
 \int_W^{W_0}\frac{d\omega}{\omega^m\lambda(\omega)}.
\]
The loose reciprocal bounds imply
\(|D_b^WI_m(W)|\le CI_m(W)\).  Moreover
\[
 D_bg(0)=\frac{LB_c(0)}{\|B_c(0)\|_2^2},\qquad
 \|D_bg(0)\|_2=O(L/\sqrt n),
\]
while \(D_b^Wx=0\) and \(D_b^W\tau=O(1)\).
Differentiating (4.12w1)--(4.12w7) gives the same bounds and never invokes
a fixed-time candidate tangent.

Finally, exactly,
\[
 \mathcal E_0-\mathcal E_0^\circ
 =\delta g^{\mathsf T}V(\vartheta)+Y.                  \tag{4.12z}
\]
The finite bath-moment event gives
\(\|V(\vartheta)\|_{2,n}\le R_L^D\).  Hence the
\(\delta g\)-part of (4.12v), using \(R_L^D\ll M_L\), and the output
part of (4.12v) give
\[
 \|\mathcal E_0-\mathcal E_0^\circ\|_{C_b^1(W)}
 \le CM_LR_L^DI_1(W)
 +n^{-1/2+o(1)}I_2(W)+n^{-1/6+o(1)}x(W),
\]
which is (4.12k).

Since on the outgoing branch \(x'=8\lambda x^2/L\), \(\lambda\ge c\),

\[
 \sup_x\frac1x\int_0^{s_x}x(s)\,ds\le C/L,\qquad
 \sup_x\frac1{x\sqrt n}\int_0^{s_x}x(s)^2\,ds
 \le CL/\sqrt n,                                      \tag{4.12l}
\]

and the same inequalities hold after \(D_b^W\).  Dividing (4.12k) by
\(x\), then using

\[
 Wr_P=(\mathcal P-26)+
       \frac{\mathcal E_0-\mathcal E_0^\circ}{x}
       +x\mathcal E_2,                                  \tag{4.12m}
\]

proves (4.12e).  This is a simultaneous first-exit argument: the right
side of (4.12e) assumes only the loose reciprocal bounds
\(\lambda\ge c/2\), \(|D_b^W\lambda|\le C\); the fixed-\(W\) triangular
system in Section 5 improves both.  Hence the candidate local resolvent
is established independently of the mixed-star contraction (4.16).

### 4.3 The lifted mixed-defect lemma

For completeness, the deterministic superposition argument is recorded
explicitly.  Let (q_0) be a common-deletion path and (d_\alpha) the exact
increment obtained by inserting star (\alpha) alone.  For the polynomial
vector field (F), put

\[
 \mathcal M(q_0,d)=F\!\left(q_0+\sum_\alpha d_\alpha\right)-F(q_0)
 -\sum_\alpha\{F(q_0+d_\alpha)-F(q_0)\}.                 \tag{4.13}
\]

Consider

\[
 q_0'=F(q_0)+\lambda\mathcal M,\qquad
 d_\alpha'=F(q_0+d_\alpha)-F(q_0),\quad 0\le\lambda\le1. \tag{4.14}
\]

At \(\lambda=0\) these are the exact core and one-star problems.  To see
the block structure without a hidden triangular term, use

\[
 y_0=q_0,\qquad y_\alpha=q_0+d_\alpha .                 \tag{4.14a}
\]

Then every block satisfies

\[
 y_\beta'=F(y_\beta)+\lambda\mathcal M,
 \qquad \beta\in\{0\}\cup\{\alpha\}.                  \tag{4.14b}
\]

At \(\lambda=1\), \(q_0+\sum d_\alpha\) solves the full
equation.  If \(Y_\beta=\partial_\lambda y_\beta\), differentiation of
(4.14b) gives

\[
 Y_\beta'=DF(y_\beta)Y_\beta+S,\qquad
 S=\mathcal M+\lambda D\mathcal M[Y].                  \tag{4.14c}
\]

Thus the diagonal resolvent in the \(y\)-coordinates is the direct sum
\(\mathcal R_\oplus=\bigoplus_\beta\mathcal R_\beta\) of the exact
common-core and exact core-plus-one-star resolvents.  Put
\[
 \mathbf ES=(S,S,\ldots,S),\qquad
 \mathcal K S:=D_{q_0}\mathcal M[\mathcal R_0S]
 +\sum_\alpha D_{d_\alpha}\mathcal M[
       (\mathcal R_\alpha-\mathcal R_0)S].
\]
This is just the chain rule in the coordinates
\(d_\alpha=y_\alpha-y_0\).  The first term still contains two
undifferentiated insertion legs; in the second, differentiating one
insertion leaves another distinct leg and the reachable variation is
precisely \(Z_\alpha(S)=(\mathcal R_\alpha-\mathcal R_0)S\).
The tangent problem is exactly the *common-source* equation
\[
 Y=\mathcal R_\oplus\mathbf E
       \{\mathcal M+\lambda D\mathcal M[Y]\}
   =\mathcal R_\oplus\mathbf ES,\qquad
 S=\mathcal M+\lambda\mathcal KS.                      \tag{4.15}
\]
This replaces the false core-only injection and also avoids estimating
arbitrary direct-sum tangents, which are not reachable here.

No source or response norm is left implicit.  If
\(y=(A,u,G)\), \(S=(S_A,S_u,S_G)\) is an additive canonical source, and
\(Y=(a,v,M)\) is a tangent, define their exact seven-component jets by
\[
\begin{array}{c|c|c}
 &\mathcal J_yS&\mathcal T_yY\\ \hline
A&S_A&a\\
u&S_u&v\\
G&S_G&M\\
X&2u\odot S_u&2u\odot v\\
Z&S_GX+G(2u\odot S_u)&MX+G(2u\odot v)\\
B&S_A\odot Z+A\odot(\mathcal J_yS)_Z
 &a\odot Z+A\odot(\mathcal T_yY)_Z\\
R&S_G^{\mathsf T}B+G^{\mathsf T}(\mathcal J_yS)_B
 &M^{\mathsf T}B+G^{\mathsf T}(\mathcal T_yY)_B.
\end{array}                                                \tag{4.15a}
\]
For a seven-tuple \(V\), put
\[
 |V|_D=\|V_A\|_{\mathrm r,D}+\|V_u\|_{\mathrm c,D}
 +\|V_G\|_{\mathrm{rc},D}+\|V_X\|_{\mathrm c,D}
 +\|V_Z\|_{\mathrm r,D}+\|V_B\|_{\mathrm r,D}
 +\|V_R\|_{\mathrm c,D},                                \tag{4.15b}
\]
using the completely explicit fixed-layer norms (4.12r).  On the common
core,
\[
 \|h\|_{\mathrm{row}G,D}
 =\|h\|_2+\max_\ell
   \frac{\langle x_\ell\rangle^D}{\sqrt{\theta_\ell}}
       \|hP_{J_\ell}\|_2 .                              \tag{4.15b'}
\]
This is the weighted Euclidean norm of one matrix row.  One matrix
column uses the fresh-fiber norm \(\|\cdot\|_{\mathrm f,D}\) in
(4.12s).  These local norms are distinct from the \(\sqrt n\)-scaled
fibers used later when many matrix rows or columns are synthesized.
The local spaces also admit an optional fresh initial-fiber datum:
\[
 M_{i\cdot}(0)=\eta_i^{\rm r}\quad\hbox{for a row},\qquad
 \delta g_j(0)=\eta_j^{\rm c}\quad\hbox{for a column}.   \tag{4.15b''}
\]
Its norm is respectively
\(\|\eta_i^{\rm r}\|_{\mathrm{row}G,D}\) or
\(\|\eta_j^{\rm c}\|_{\mathrm f,D}\), added to the local source norm.
The response Green then has this initial value instead of zero.  The
mixed common-source fixed point always uses \(\eta=0\); the optional
channel is used only when exposing an initial Gaussian fiber in the
synthesis lemma.
On the common core,
\[
 \|S\|_{\mathrm{src},0}=\int_0^{\sigma_{\rm pre}}
             |\mathcal J_{y_0}S|_D\,ds,                  \tag{4.15c}
\]
and \(\|Y\|_{\mathrm{loc},0}\) is the supremum plus total variation of
the same jet after applying \(T_D^{-1}\) to its primitive
\((A,u,G)\)-components.  Equations (4.7f)--(4.8c) give
\[
 \|\mathcal R_0S\|_{\mathrm{loc},0}
 \le L^C\|S\|_{\mathrm{src},0}.                         \tag{4.15d}
\]

The local pullbacks are as follows.  For a row \(i\), in \(\tau=Ls\),
\[
 f_{A,i}^{\rm r}=L^{-2}S_{A,i},\qquad
 f_{Z,i}^{\rm r}=L^{-2}\{S_GX+G(2u\odot S_u)\}_i,
 \qquad f_{g,i}^{\rm r}=L^{-1}S_{G,i\cdot}.             \tag{4.15e}
\]
If \(f_{Z,i}^{\rm r}=\partial_\tau J_i+r_i\), take the infimum, over
all such decompositions with \(J_i(0)=0\), of
\[
 \|S^{[-i]}\|_{\mathrm{src},0}
 +\int_0^{T_{\rm pre}}(|f_{A,i}^{\rm r}|+|r_i|)\,d\tau
 +\int_0^{T_{\rm pre}}\|f_{g,i}^{\rm r}\|_{\mathrm{row}G,D}\,d\tau
 +\sup_\tau|J_i(\tau)|.                                  \tag{4.15f}
\]
This is \(\|S\|_{\mathrm{src},i}^{\rm r}\); the row response norm is
\(\|Y^{[-i]}\|_{\mathrm{loc},0}\) plus
\(\sup_\tau L^{-1}(|a_i|+|(\mathcal T_yY)_{Z,i}|)\) and
\[
 \sup_\tau\|M_{i\cdot}(\tau)\|_{\mathrm{row}G,D}
 +\operatorname{Var}_\tau
       \{M_{i\cdot}\}_{\mathrm{row}G,D}.
\]
The endpoint channel in (4.15f) is precisely (2.9).  The exact local
row Green and the \(0.11-0.09\) gap give, also with the optional datum
in (4.15b''),
\[
 \|\mathcal R_i(\eta_i^{\rm r},S)\|_{\mathrm{loc},i}
 \le L^C\{\|\eta_i^{\rm r}\|_{\mathrm{row}G,D}
                  +\|S\|_{\mathrm{src},i}^{\rm r}\}.    \tag{4.15g}
\]
In this row block the remaining derived legs are not implicit:
\(B_i=A_iZ_i\) and the row contribution to \(R\) is
\(G_{i\cdot}^{\mathsf T}B_i\); their tangents are exactly those in
(4.15a).

For a column \(j\), write \(g=G_{\cdot j}\),
\(z=G_{\cdot,-j}X_{-j}\), and set
\[
\begin{aligned}
 f_U&=2u_jS_{u,j}/L^3,\\
 f_H&=2S_{G,\cdot j}^{\mathsf T}D_Ag
       +g^{\mathsf T}D_{S_A}g,\\
 f_g^{\rm c}&=L^{-1}S_{G,\cdot j},\\
 f_P&=L^{-2}\{S_{G,\cdot j}^{\mathsf T}D_Az
       +g^{\mathsf T}D_{S_A}z+g^{\mathsf T}D_As_z^{[-j]}\},\\
 s_z^{[-j]}&=S_{G,-j}X_{-j}+G_{-j}(2u_{-j}\odot S_{u,-j}).
\end{aligned}                                             \tag{4.15h}
\]
For a regular column, \(\|S\|_{\mathrm{src},j}^{\rm c}\) is the
core source norm with column \(j\) removed plus
\[
 \int_0^{T_{\rm pre}}
 \left(|f_U|+|f_H|+|f_P|+\|f_g^{\rm c}\|_{\mathrm f,D}\right)d\tau .
\]
Its response norm is the corresponding core norm plus
\[
 \sup_\tau(|\delta U|+|\delta H|+|\delta P|
             +\|\delta g\|_{\mathrm f,D})
 +\operatorname{Var}_\tau\{\delta g\}_{\mathrm f,D}.
\]
The formal
\(3h_L\) pole gap and the exact one-column block give, also with the
optional datum in (4.15b''),
\[
 \|\mathcal R_j(\eta_j^{\rm c},S)\|_{\mathrm{loc},j}
 \le L^C\{\|\eta_j^{\rm c}\|_{\mathrm f,D}
                    +\|S\|_{\mathrm{src},j}^{\rm c}\}.  \tag{4.15i}
\]
For this column the local derived legs are
\(Z^{(j)}=xg\), \(B^{(j)}=xD_Ag\), and
\(R_j=hx+\rho\), together with their exact tangents from (4.15a).

For a candidate, no fixed-time \(U\)-norm is used.  Let
\(\mathscr L_j(W)\) be the linearization, at fixed
\(W\), of the exact one-star system on the variables
\[
 \mathcal Y_j=(A,u_{-j},G_{-j},g,P,\lambda),
\]
including the same-star bath response (4.12o).  On the
zero-common-forcing reference path put
\[
 \Lambda:=H+PW,
\]
the radial quantity denoted by \(\lambda\) in Section 5; this capital
letter distinguishes it from the homotopy parameter in (4.14).  Put
\[
\begin{gathered}
 b_W^{0}=-8\Lambda,\qquad b_P^{0}=26/W+e_P,\qquad
 b_\lambda^{0}=29+e_H+We_P-8P\Lambda,\\
 b_{\rm bath}^{0}=\frac d{d\tau}(A,u_{-j},G_{-j}),\qquad
 b_g^{0}=\frac{dg}{d\tau}.                              \tag{4.15j}
\end{gathered}
\]
Along a block at homotopy value \(\lambda_{\rm hom}\), let
\(b_W,b_P,b_\lambda,b_{\rm bath},b_g\) mean its **actual** velocities.
They equal the displayed reference velocities plus
\(\lambda_{\rm hom}\) times the corresponding components of the common
source \(\mathcal M\).  The loose simultaneous first-exit stop requires
this perturbation to be at most half the reference transversality
margin; (4.23) strictly improves it to \(o(1)\).  Thus
\(|b_W|\ge c\), and the fixed-\(W\) triangular bounds are unchanged.
All quotient rules below use these actual velocities.
For an additive canonical source define
\[
\begin{gathered}
 f_{\rm bath}=L^{-1}(S_A,S_{u,-j},S_{G,-j}),\qquad
 f_g=L^{-1}S_{G,\cdot j},\\
 f_W=-W^2f_U,\qquad f_\lambda=f_H+Wf_P+Pf_W.             \tag{4.15j'}
\end{gathered}
\]
For an optional initial fresh-column datum
\(\delta g(0)=\eta_j^{\rm c}\), the induced initial outer data are
\[
 \eta_P=L^{-1}(\eta_j^{\rm c})^{\mathsf T}D_Az,\qquad
 \eta_H=2L(\eta_j^{\rm c})^{\mathsf T}D_Ag,\qquad
 \eta_\Lambda=\eta_H+W_0\eta_P.                         \tag{4.15j_a}
\]
Let
\[
 \mathfrak i_j(\eta_j^{\rm c})
 =\sum_{m=0}^1\left\{
   \|(D_b^W)^m\eta_j^{\rm c}\|_{\mathrm f,D}
   +|(D_b^W)^m\eta_P|+|(D_b^W)^m\eta_\Lambda|\right\},
                                                               \tag{4.15j_b}
\]
where the fresh direction itself has zero \(b\)-derivative and
\(D_b^W\) acts on the displayed coefficients.
Changing from \(\tau\) to \(\sigma=\log(W_0/W)\) gives the exact
quotient-rule pullbacks
\[
\begin{aligned}
 \varphi_{\rm bath}
  &=-\frac W{b_W}\left(f_{\rm bath}
                  -\frac{b_{\rm bath}}{b_W}f_W\right),&
 \varphi_g
  &=-\frac W{b_W}\left(f_g-\frac{b_g}{b_W}f_W\right),\\
 \varphi_P
  &=-\frac W{b_W}\left(f_P-\frac{b_P}{b_W}f_W\right),&
 \varphi_\lambda
  &=-\frac W{b_W}\left(f_\lambda-\frac{b_\lambda}{b_W}f_W\right).
                                                               \tag{4.15j''}
\end{aligned}
\]
If \(f_P=r_P+\partial_\tau j\), with \(j(W_0)=0\), put
\[
 E_j(\sigma)=(0,0,j(\sigma),W(\sigma)j(\sigma))
\]
in the \(({\rm bath},g,P,\lambda)\) coordinates and define the
endpoint-removed source
\[
 \widetilde\varphi
 =(\varphi_{\rm bath},\varphi_g,\varphi_P,\varphi_\lambda)
   -(\partial_\sigma-\mathscr L_j)E_j.                  \tag{4.15j'''}
\]
The two derivatives of \(j\) cancel identically in (4.15j'''); only
\(r_P\), the direct sources, and bounded coefficients times \(j\)
remain.  This is the linear, source-covariant version of the endpoint
normal form (5.4a); it neither places \(J\) in the background state nor
estimates \(J_\tau\) by absolute value.
Write
\(\widetilde\varphi=(\widetilde\varphi_{\rm bath},
\widetilde\varphi_g,\widetilde\varphi_P,
\widetilde\varphi_\lambda)\).  Define
\[
\begin{aligned}
\|(\eta_j^{\rm c},S)\|_{\mathrm{src},j}^{W}:=
 \mathfrak i_j(\eta_j^{\rm c})
 +\inf_{f_P=r_P+\partial_\tau j}\sum_{m=0}^1\Bigg\{&
 \int_0^{\sigma_{\rm cap}}
  |\mathcal J_{y^{[-j]}}(D_b^W)^m
          \widetilde\varphi_{\rm bath}|_D\,d\sigma\\
 &+\int_0^{\sigma_{\rm cap}}
     \|(D_b^W)^m\widetilde\varphi_g\|_{\mathrm f,D}\,d\sigma\\
 &+\sup_{\sigma}
   \frac{\left|\int_0^\sigma
     (D_b^W)^m\widetilde\varphi_P\,d\varsigma\right|}
        {1+\sigma}
 +\int_0^{\sigma_{\rm cap}}
     |(D_b^W)^m\widetilde\varphi_\lambda|\,d\sigma\\
 &+\int_0^{\sigma_{\rm cap}}
      W|(D_b^W)^mf_W|\,d\sigma
 +\sup_W|(D_b^W)^mj(W)|\Bigg\}.                         \tag{4.15k}
\end{aligned}
\]
Every term is a norm of a displayed source curve; in particular a
direct \(G_{\cdot j}\)-source cannot have zero norm.
For a response at fixed \(W\), put hats on its components and set
\[
\begin{aligned}
 \mathcal N_j^W(\widehat Y):={}&
 \|\widehat A\|_{\mathrm r,D}
 +\|\widehat u_{-j}\|_{\mathrm c,D}
 +\|\widehat G_{-j}\|_{\mathrm{rc},D}
 +\|\widehat g\|_{\mathrm f,D}
 +\|\widehat X_{-j}\|_{\mathrm c,D}\\
 &+\|\widehat z^{[-j]}\|_{\mathrm r,D}
 +x^{-1}\|x\widehat g\|_{\mathrm f,D}
 +\|\widehat B^{[-j]}\|_{\mathrm r,D}\\
 &+x^{-1}\|x(D_{\widehat A}g+D_A\widehat g)\|_{\mathrm f,D}
 +\|\widehat R_{-j}\|_{\mathrm c,D}
 +\frac WL|\widehat R_j| .                              \tag{4.15l}
\end{aligned}
\]
Here \(\widehat X_j=0\), and
\(\widehat R_j=(L/W)\widehat\lambda\), at fixed \(W\).
The hatted \(z,B,R\) are reconstructed from the hatted primitive
variables by (4.15a); thus (4.15l) is a finite graph norm, not a list
of independent observables.

Let \(\widehat Y=\mathcal R_j(\eta_j^{\rm c},S)\), with
\(\widehat Y(W_0)\) equal to the initial graph datum (4.15j_a).
For every admissible decomposition
\(f_P=r_P+\partial_\tau j\), use the **same** representative in
\(\widetilde Y_j=\widehat Y-E_j\).  Its graph size is the sum, for
\(m=0,1\), of
\[
\begin{aligned}
 &\sup_W\left\{
 \mathcal N_j^W((D_b^W)^m\widetilde Y_j)
 +|(D_b^W)^m\widetilde\lambda_j|
 +\frac{|(D_b^W)^m\widetilde P_j|}{1+\sigma}
 +|(D_b^W)^m\delta\Theta|\right\}\\
 &\quad+\operatorname{Var}_{W;\mathbb G_j}
       ((D_b^W)^m\widetilde Y_j)
 +\operatorname{Var}_W((D_b^W)^m\delta\Theta),          \tag{4.15l'}
\end{aligned}
\]
where \((\widetilde P_j,\widetilde\lambda_j)\) are the last two
components of \(\widetilde Y_j\).  Here
\(\mathbb G_j\) is the fixed ambient product space of all components in
(4.15l), with norm
\(\|V\|_{\mathbb G_j}=\sup_W\mathcal N_j^W(V)\), and
\[
 \operatorname{Var}_{W;\mathbb G_j}V
 =\sup_{\Pi}\sum_k
   \|V(W_k)-V(W_{k-1})\|_{\mathbb G_j}.
\]
Thus “variation” means Banach-valued variation, not variation of the
scalar \(W\mapsto\mathcal N_j^W(V(W))\).
The candidate response quotient norm is the infimum of (4.15l') over
the same endpoint representatives used in (4.15k).  Equivalently, the
source and response are elements of the common quotient by
\((\partial_\tau j,E_j)\).
Linearizing the exact fixed-\(W\) system gives
\[
 \partial_\sigma\widetilde Y
   =\mathscr L_j(W)\widetilde Y+\widetilde\varphi .
\]
The triangular \((P,\lambda)\) estimate of (5.4c)--(5.4d), the
row-/diagonal-dressed bath Green, and variation of constants therefore
give, for every initial datum and additive source in the domain (4.15k),
\[
 \|\mathcal R_j(\eta_j^{\rm c},S)\|_{\mathrm{loc},j}^{W}
 \le C\|(\eta_j^{\rm c},S)\|_{\mathrm{src},j}^{W}.      \tag{4.15m}
\]
Indeed the \(P\)-equation has at most linear growth in \(\sigma\), the
\(\lambda\)-equation has the integrable coefficient
\(W(1+\sigma)\).  Along the actual homotopy block the clock variation is
the quotient-rule identity
\[
 \delta\Theta_\sigma
 =\frac{W\{D b_W^{0}[\widetilde Y]+\widetilde f_W\}}{b_W^2}
 =\frac{W\{-8\,\delta\widetilde\Lambda
                  +f_W(S)-8Wj\}}{b_W^2},               \tag{4.15m'}
\]
where \(\widetilde f_W:=f_W(S)-8Wj\).  Indeed
\(\delta\Lambda=\delta\widetilde\Lambda+Wj\) under the endpoint lift
\(E_j\).
Here the numerator differentiates the reference canonical velocity
\(b_W^0=-8\Lambda\), while the denominator is the actual homotopy
velocity.  Thus the homotopy \(D\mathcal M\)-term is counted exactly once,
inside the common source \(S\).  Since \(|b_W|\ge c\), (4.15m') has
exactly the integrable bound used in (4.15l'): the endpoint contribution
is bounded by \(\sup|j|\int W^2\,d\sigma\).
The same-star bath part is exactly the linearization of
(4.12o), (4.12w1)--(4.12w3).  In the unweighted graph (4.15l), the
common cavity clock derivative remains in the doubled common Green and
is handled by the quotient pullback (4.15j'').  For an arbitrary
canonical source \(T\), the response \(\widehat Y_T\) is linear about
the stopped reachable one-star base.  Its score derivative satisfies,
in the endpoint-removed reciprocal coordinates,
\[
 (\partial_\sigma-\mathscr L_j)D_b^W\widehat Y_T
 =(D_b^W\mathscr L_j)\widehat Y_T+D_b^W\widetilde\varphi_T .
\]
There is no square of \(\widehat Y_T\).  The only coordinatewise
polarization not controlled by endpoint multiplication has the form
\((D_b^W\Delta e)\widehat Y_{T,e}\); it is bounded by the special
difference-score estimate (4.12w7b)--(4.12w7l').  The remaining
polarizations are the \(G,G^{\mathsf T}\), sandwiched \(H\), normalized
inner-product, or \(1/n\) outer-product operations displayed above.
Thus the termwise estimates (4.12w8)--(4.12w9) read
\[
 \|\widetilde Y\|_{\mathrm{loc},j}^W
 \le C\|\widetilde\varphi\|_{\mathrm{src},j}^W
   +C\{\gamma_L+n^{-1/6+o(1)}\}
       \|\widetilde Y\|_{\mathrm{loc},j}^W .
\]
The estimate holds for every admissible endpoint representative; taking
the common source/response infimum therefore gives (4.15m) on the
quotient Banach spaces.
They hold for an arbitrary source because every response-free term is
charged in (4.15k), while the special difference-score multiplier was
proved before any arbitrary tangent was introduced.  An optional fresh
initial direction has zero \(b\)-derivative and is covered by the same
linear estimate.  The special denominators in (4.12v) are not used.
Absorbing the last term proves (4.15m).  Thus
(4.15m) is an arbitrary-reachable-source statement, not an extrapolation
from the special insertion source.
In the common-source fixed point, \(\eta=0\); below
\(\|S\|_{\mathrm{src},j}^{W}\) abbreviates
\(\|(0,S)\|_{\mathrm{src},j}^{W}\), and likewise for the row and
regular-column local norms.

Finally put
\[
 \|S\|_{\mathfrak S}=\max\left\{\|S\|_{\mathrm{src},0},
 \max_i\|S\|_{\mathrm{src},i}^{\rm r},
 \max_{j\notin\mathscr C_L}\|S\|_{\mathrm{src},j}^{\rm c},
 \max_{j\in\mathscr C_L}\|S\|_{\mathrm{src},j}^{W}\right\}. \tag{4.15n}
\]
The common injection \(\mathbf E\) has norm one by definition.  All
domains, time pullbacks, endpoint primitives, and radial derivatives used
below are now explicit.
Precisely, each source space is the completion of smooth zero-initial
reachable canonical sources under its displayed norm, modulo
almost-everywhere zero curves.  Each response space is the completion of
smooth zero-initial responses under the displayed supremum plus graph-
variation norm.  The estimates above extend the resolvents uniquely to
these Banach spaces.

Consequently the required contraction is the source-space estimate
\[
 \|\mathcal KS\|_{\mathfrak S}\le q\|S\|_{\mathfrak S},
 \qquad q<1/2.                                         \tag{4.16}
\]
When it holds,
\[
 S=(I-\lambda\mathcal K)^{-1}\mathcal M,\qquad
 \|S\|_{\mathfrak S}\le2\|\mathcal M\|_{\mathfrak S},  \tag{4.17}
\]
and \(Y=\mathcal R_\oplus\mathbf ES\) recovers the full-flow tangent.

We next prove the collective synthesis estimate; it is not an RMS
reconstruction of already-dense \(R\)-legs.  Write
\[
 d_\alpha=(a_\alpha,v_\alpha,M_\alpha),\qquad
 A^0=A_0,\quad u^0=u_0,\quad G^0=G_0,
\]
\[
 A^\alpha=a_\alpha,\qquad u^\alpha=v_\alpha,\qquad
 G^\alpha=M_\alpha .
\]
For an ordered six-tuple
\(\boldsymbol\alpha\in(\{0\}\cup\mathcal I)^6\), define
\[
\begin{aligned}
\Phi_A(\boldsymbol\alpha)
 &=[G^{\alpha_1}(u^{\alpha_2}\odot u^{\alpha_3})]
   \odot[G^{\alpha_4}(u^{\alpha_5}\odot u^{\alpha_6})],\\
\Phi_u(\boldsymbol\alpha)
 &=4u^{\alpha_1}\odot(G^{\alpha_2})^{\mathsf T}
   [A^{\alpha_3}\odot
     G^{\alpha_4}(u^{\alpha_5}\odot u^{\alpha_6})],\\
\Phi_G(\boldsymbol\alpha)
 &=\frac2n[A^{\alpha_1}\odot
     G^{\alpha_2}(u^{\alpha_3}\odot u^{\alpha_4})]
     (u^{\alpha_5}\odot u^{\alpha_6})^{\mathsf T}.
\end{aligned}                                             \tag{4.18a}
\]
These are the three components of \(F\), term for term.  If
\(\operatorname{supp}\boldsymbol\alpha\) denotes its nonzero labels, then
\[
 \mathcal M_\bullet
  =\sum_{|\operatorname{supp}\boldsymbol\alpha|\ge2}
       \Phi_\bullet(\boldsymbol\alpha).                  \tag{4.18b}
\]
Consequently \(D_{q_0}\mathcal M\) retains two insertion labels, while
\(D_{d_\alpha}\mathcal M\) retains a label different from \(\alpha\).
This is an exact finite identity: every output has primitive degree six.

For reference, the same identity in the derived variables is
\[
\begin{aligned}
\chi_X&=2\sum_{\alpha<\beta}v_\alpha\odot v_\beta,\\
\chi_Z&=G_0\chi_X+\sum_{\alpha\ne\beta}M_\alpha x_\beta
       +\bar M\chi_X,\\
\chi_B&=A_0\odot\chi_Z+\sum_{\alpha\ne\beta}a_\alpha\odot z_\beta
       +\bar a\odot\chi_Z,\\
\chi_R&=G_0^{\mathsf T}\chi_B+
       \sum_{\alpha\ne\beta}M_\alpha^{\mathsf T}b_\beta
       +\bar M^{\mathsf T}\chi_B ,
\end{aligned}                                             \tag{4.18c}
\]
where \(x_\alpha,z_\alpha,b_\alpha,r_\alpha\) are the exact singleton
increments obtained successively from
\(X=u^2,Z=GX,B=A\odot Z,R=G^{\mathsf T}B\), and bars denote sums over
\(\alpha\).  Direct expansion gives the complete polarization
table
\[
\begin{array}{c|l}
\text{source}&\text{all of its mixed terms}\\ \hline
\mathcal M_A&
2Z_0\odot\chi_Z+
2\sum_{\alpha<\beta}z_\alpha\odot z_\beta+
2\bar z\odot\chi_Z+\chi_Z^2\\[1mm]
\mathcal M_u/4&
u_0\odot\chi_R+
\sum_{\alpha\ne\beta}v_\alpha\odot r_\beta+
\bar v\odot\chi_R\\[1mm]
n\mathcal M_G/2&
B_0\chi_X^{\mathsf T}+\chi_BX_0^{\mathsf T}
+\sum_{\alpha\ne\beta}b_\alpha x_\beta^{\mathsf T}
+\bar b\chi_X^{\mathsf T}
+\chi_B\bar x^{\mathsf T}+\chi_B\chi_X^{\mathsf T}.
\end{array}                                               \tag{4.18d}
\]
Thus there is no unlisted \(A,u,G,X,Z,B,R\) occurrence.

The collective norm is evaluated recursively in the order
\[
 (A,u,G)\longmapsto X\longmapsto Z\longmapsto B
 \longmapsto R\longmapsto F\longmapsto\mathcal J_yF.     \tag{4.18e}
\]
Coordinate fibers are synthesized first:
\[
 \left\|\sum_{i\in I}c_ie_i\right\|_{2,n}^2
   =\frac1n\sum_{i\in I}|c_i|^2.                         \tag{4.18f}
\]
For a matrix row or column fiber, the local entry in this normalized
square sum is \(\sqrt n\) times its Frobenius norm:
\[
 \left\|\sum_{i\in I}e_im_i^{\mathsf T}\right\|_F^2
 =\frac1n\sum_{i\in I}
       \bigl(\sqrt n\,\|m_i\|_2\bigr)^2.                 \tag{4.18g}
\]
Raw inserted Gaussian rows or columns are retained in their local blocks;
they are never assigned a small aggregate Frobenius norm.  Only their
actual occurrences \(M_\alpha x_\beta\),
\(M_\alpha^{\mathsf T}b_\beta\), the trained outer product, and
response-difference matrices are synthesized.  After the primitive
fibers have been summed, \(X,Z,B,R\) are formed by (4.18e).  In
particular, a family of dense \(R_\alpha\)-legs is not reconstructed from
its own RMS.
After each primitive source word \((F_A,F_u,F_G)\) is synthesized, its
\(X,Z,B,R\) source legs are formed by the seven exact formulas (4.15a).
This uses only the same Hadamard, \(G\), \(G^{\mathsf T}\), and trained
outer-product operations and introduces no new insertion label.  The
largest primitive degree is ten, in the \(R\)-source leg; \(D\) in
(4.3) was chosen larger than this finite degree.

Here is the deterministic collective response step.  Put
\[
 \Delta J_\alpha=DF(y_\alpha)-DF(y_0),\qquad
 T_\alpha=\Delta J_\alpha\mathcal R_0S .
\]
The second resolvent identity gives, exactly,
\[
\begin{aligned}
 Z_\alpha(S):=(\mathcal R_\alpha-\mathcal R_0)S
   &=\mathcal R_\alpha T_\alpha
     =\mathcal R_0\{T_\alpha+\Delta J_\alpha Z_\alpha(S)\},\\
 \sum_\alpha Z_\alpha(S)
   &=\mathcal R_0\sum_\alpha
       \{T_\alpha+\Delta J_\alpha Z_\alpha(S)\}.          \tag{4.18h}
\end{aligned}
\]
Thus the whole family is synthesized at the canonical-source DAG level
before one application of the common Green.  The source
\(\Delta J_\alpha Z_\alpha\) is a same-star self-return estimated in the
exact \(\alpha\)-local norm; it incurs no additional density loss.
Whenever it occurs in \(D\mathcal M\), the distinct portal is supplied
by the mixed word itself.  This identity is the required recursive
reconstruction and rules out the false operation of summing dense
derived legs or dense local-resolvent outputs.

For ordinary layers set

\[
 p_L^{\rm mix}=L^C\left(
 \sum_k r_k^D\sqrt{\pi_k}
 +\sum_\ell x_\ell^D\sqrt{\theta_\ell}
 \right)+n^{-c}=o(L^{-N})\quad\hbox{for every fixed }N. \tag{4.18}
\]

The noncore row sum is \(L^Ce^{-cR_L^2}\), the noncore column
sum is \(L^Ce^{-cR_L}\), and there are only \(O(\log L)\) dyadic layers.

The common-core factor \(\gamma_L\) from the dressed estimate (4.8a) is
deliberately absent
from \(p_L^{\rm mix}\).  It dresses every local resolvent in
\(\mathcal R_{\rm loc}\); it is not a noncore insertion in
\(\mathcal M\) or \(D\mathcal M\).  Treating it as a portal and then
squaring it against the candidate logarithm would give a generally
non-small bound \(\log n\,\gamma_L^2\).  The core error is compared only with
the macroscopic pole-window width \(h_L=(\log L)^{-1}\), for which
\(\gamma_L=o(h_L)\).  Pair spacings use exact quenched one-column clocks
in that dressed core and never compare the core to its time-zero
approximation at the spacing scale.

The only analytic mappings used in (4.18d)--(4.18h) are
\[
\begin{array}{c|c}
\text{mapping}&\text{bound}\\ \hline
(a,b)\mapsto a\odot b&
\|a\odot b\|_{2,n}\le\|a\|_\infty\|b\|_{2,n}\\
v\mapsto Gv,\ b\mapsto G^{\mathsf T}b&
\text{the fixed block bound (4.7)}\\
(b,x)\mapsto 2bx^{\mathsf T}/n&
\|2bx^{\mathsf T}/n\|_F
       =2\|b\|_{2,n}\|x\|_{2,n}.
\end{array}                                               \tag{4.18i}
\]
The trained mixed block also obeys, directly,

\[
 \|P_I\Delta G P_J\|
 \le2\int\|P_IB\|_{2,n}\|P_JX\|_{2,n}\,ds,             \tag{4.19}
\]

and has the same layer deficit.  Same-fiber identities are not placed in
\(p_L^{\rm mix}\); they are the exact local blocks in (4.9) and (4.11).

The estimate is layer-first, not a starwise absolute sum and not an
appeal to a hidden graph expansion.  For a row layer \(I_k\) and a
column layer \(J_\ell\), put
\[
 \epsilon_k^{\rm r}=L^Cr_k^D\sqrt{\pi_k},\qquad
 \epsilon_\ell^{\rm c}=L^Cx_\ell^D\sqrt{\theta_\ell}.  \tag{4.19a}
\]
The following finite-word synthesis lemma is the probabilistic input.
Derivative closure is part of its statement.  Regard each word
\(\Phi_\bullet\) in (4.18a) as a six-linear typed form.  For slot order
\(r\in\{0,1,2\}\) and fixed-\(W\) score order \(k\in\{0,1\}\) with
\(r+k\le2\), include every ordered slot derivative
\[
 D^r\Phi_\bullet(\boldsymbol\alpha)[V_1,\ldots,V_r],    \tag{4.19a0}
\]
its \(k\) score derivatives, its seven-component source-jet lift through
(4.15a), and its row, regular-column, and endpoint-removed fixed-\(W\)
pullbacks.  The allowed directions are common responses
\(\mathcal R_0T\), one-star differences \(Z_\alpha(T)\), optional
initial-fiber responses \(\mathcal R_\alpha(\eta_\alpha,0)\), and the
score derivatives allowed by \(r+k\le2\).  In particular the candidate
catalogue contains \(\mathcal R_j(\eta_j^{\rm c},0)\).  All these
words are placed on every fixed one-/two-star deletion and every point of
the deterministic \((s,\lambda,W,b)\)-nets.  A direction
\(Z_\alpha(T)\) carries the label \(\alpha\); only the target label may be
absorbed by its own local source norm.  The recursively synthesized word
with distinct ordinary layer labels is at most \(L^C\) times the product
of the remaining \(\epsilon\)'s.  Matrix fibers use (4.18g), not their
raw RMS.

This triangular catalogue is finite.  Before the source-jet lift its
coefficient degrees are at most \(6,5,4\) for \(r=0,1,2\), and after the
lift they are at most \(10,9,8\).  If an entry has \(r+k\le1\), its one
score-differentiated endpoint pullback is also included.  Indeed, for
such a lifted source \(\Xi\),
\[
 D_b^W\widetilde\varphi_\Xi
 =D_b^W\varphi_\Xi
  -(\partial_\sigma-\mathscr L_j)E_{D_b^Wj}
  +(D_b^W\mathscr L_j)E_j.                             \tag{4.19a1}
\]
Thus no derivative of \(j_\tau\) is estimated.  The first two terms are
charged by the \(m=1\) and \(\sup|D_b^Wj|\) terms of (4.15k), while
\(D_b^W\mathscr L_j\) is an order-two slot derivative.  Since
\(D_b^WW=0\), the same statement applies to
\(\widetilde f_W=f_W-8Wj\).

Here is the noncircular proof.  For \(m=1,2\), let
\(\mathfrak E_m\) be the least constant in the asserted synthesis
inequality for the triangular catalogue of total order \(r+k\le m\),
simultaneously for the finite typed words (4.18a), the lifted and
pulled-back words just listed, every fixed layer/deletion net, and
\(0\le\lambda\le1\) before the first exit.
It is finite for each \(n\), because the stopped system is
finite-dimensional.

At \(\lambda=0\), split each direct Gaussian row or column into its
regression mean and the residual in (4.6), and split every trained fiber
by (2.1).  Coordinate fibers are summed by (4.18f), response-difference
matrix fibers by (4.18g).  In a word with support \(\Gamma\), choose one
exposed label \(\alpha\).  Same-\(\alpha\) repetitions stay inside the
exact \(\alpha\)-block.  After deleting \(\alpha\), every coefficient
multiplying its initial residual fiber is cavity-measurable.
The exact one-star output is not declared to be a polynomial of that
residual: differentiating its local solution map in the fresh fiber is
exactly the optional initial-data version of the row, regular-column,
or fixed-\(W\) source-to-state problem (4.15g), (4.15i), or (4.15m).
Before applying Gaussian log-Sobolev, stop this local map at the loose
local exit and extend it with the displayed Lipschitz constant; the
strict first-exit improvement makes the extension agree with the
physical map.  Gaussian log-Sobolev concentration therefore gives the
same \(\epsilon_\alpha\) scale for the centered local output.  Its
conditional mean is a regression/self-return term
and carries the smaller layer density, which is bounded by the required
square-root density.  For a raw initial residual word,
hypercontractivity is used only at degree at most ten after the
seven-jet source lift (4.15a).  A row--column
intersection is exposed as its single common Gaussian entry; it carries
an explicit \(n^{-1/2}\) influence and is covered by the fixed
leave-two event.  The other labels are handled inductively in
\(|\Gamma|\) and in the recursion \(X\to Z\to B\to R\).
With \(p=C\log n\), the finite time/deletion/layer nets cost
\(n^{o(1)}\).  Trained occurrences are deterministic consequences of
(4.19), and a single exposed row--column occurrence uses (4.23a).

The differentiated resolvent recursion is also explicit.  At fixed
physical time write \(\partial_j^\tau=D_{b_j}|_\tau\), and, for a common
source \(T\), put
\[
\begin{gathered}
 H_0=\mathcal R_0T,\qquad
 T_\alpha=\Delta J_\alpha H_0,\qquad
 U_\alpha=T_\alpha+\Delta J_\alpha Z_\alpha,\qquad
 Z_\alpha=\mathcal R_0U_\alpha,\\
 \partial_j^\tau H_0
 =\mathcal R_0\{\partial_j^\tau T+
                  (\partial_j^\tau J_0)H_0\},\\
 \partial_j^\tau T_\alpha
 =(\partial_j^\tau\Delta J_\alpha)H_0+
                  \Delta J_\alpha\partial_j^\tau H_0,\\
 \partial_j^\tau U_\alpha
 =\partial_j^\tau T_\alpha+
   (\partial_j^\tau\Delta J_\alpha)Z_\alpha+
   \Delta J_\alpha\partial_j^\tau Z_\alpha,\\
 \partial_j^\tau Z_\alpha
 =\mathcal R_0\{\partial_j^\tau U_\alpha+
                  (\partial_j^\tau J_0)Z_\alpha\}.
                                                               \tag{4.19a1'}
\end{gathered}
\]
Here
\(\partial_j^\tau J_\beta
 =D^2F(y_\beta)[\partial_j^\tau y_\beta,\cdot]\).
Thus every differentiated family is synthesized as a canonical source
before one common \(\mathcal R_0\); no dense derived leg is summed
afterward.  Formula (4.19a1') is only the algebraic fixed-time recursion
for smooth sources; the response norm does not separately charge
\(\partial_j^\tau T\).  After the moving-level lift, every
\((\partial_\tau T)D_j\Theta\) term combines with the quotient rule
(4.15j'') and the endpoint formula (4.19a1), so the estimate uses only
the displayed \(D_b^W\widetilde\varphi_T\) source.  The next paragraph
performs precisely that lift.

To record the second-derivative charge at a candidate, first make the
moving-level pullback explicit.  Put
\[
 Q=(q_0,(d_\alpha)_\alpha),\qquad
 V_T=(\mathcal R_0T,(Z_\alpha(T))_\alpha),
\]
and, for target candidate \(j\), define
\[
 \widehat Q_j(\lambda,W)
   :=Q(\lambda,\Theta_{j,\lambda}(W)),
 \qquad
 \widehat V_T^{(j)}
   :=V_T+\partial_\tau Q\,\delta\Theta_j[T],           \tag{4.19a2}
\]
with the terms on the right evaluated at the same moving hit.  Thus
\(\widehat V_T^{(j)}\) is the exact fixed-\(W\) response, including the
clock shift; it is one of the allowed directions in (4.19a0).  Write
\(D_j=D_{b_j}^W\).  For the pulled-back canonical coefficient part of
the candidate source,
\[
 D_j\!\left(D\mathcal M(\widehat Q_j)
                 [\widehat V_T^{(j)}]\right)
 =D^2\mathcal M(\widehat Q_j)
       [D_j\widehat Q_j,\widehat V_T^{(j)}]
  +D\mathcal M(\widehat Q_j)[D_j\widehat V_T^{(j)}].   \tag{4.19a2'}
\]
The remaining quotient and endpoint terms are exactly the pulled-back
words already listed in (4.19a1).
When a slot in (4.19a2') is a coordinatewise product inside the target
one-star block, its special score direction is estimated by
(4.12w7k)--(4.12w7l'), not by an \(L^2\)-algebra inequality.  Matrix,
inner-product, and trained outer-product slots use the other three
operations in the same finite table.
At \(\lambda=0\), the **unhatted** deleted core and every
\(d_\alpha(0)\), \(\alpha\ne j\), are independent of the fresh score of
\(j\) at fixed physical time.  After pullback their only fixed-\(W\)
score derivative is the clock lift
\((\partial_\tau Q)D_j\Theta_{j,0}\), controlled by
(4.15l')--(4.15m').  This is target-\(j\) local; when placed in
\(D^2\mathcal M\) it replaces a slot without deleting any non-\(j\)
insertion label.  In a support \(\Gamma\), \(|\Gamma|\ge2\),
differentiating a
\(j\)-slot leaves \(\Gamma\setminus\{j\}\) unless the other displayed
slot is \(d_\alpha\), \(\alpha\ne j\); in that extremal case the direction
\(Z_\alpha(T)\) itself is the remaining non-target \(\alpha\)-leg.  If
\(D_j\) hits \(Z_j(T)\), then \(D_{d_j}\mathcal M\) retains a different
label, while for \(\alpha\ne j\) the \(Z_\alpha\)-leg remains.  A
\(q_0\)-derivative never removes an insertion label.  Hence no coefficient
term in (4.19a2') has zero deficit after the target norm absorbs \(j\).

For \(\lambda>0\), the exact identities **at fixed \(W\)** are
\[
 \widehat Q_j(\lambda,W)=\widehat Q_j(0,W)
    +\int_0^\lambda\widehat V_{S_\mu}^{(j)}(\mu,W)\,d\mu,\qquad
 D_j\widehat Q_j(\lambda,W)=D_j\widehat Q_j(0,W)
    +\int_0^\lambda D_j\widehat V_{S_\mu}^{(j)}(\mu,W)\,d\mu. \tag{4.19a3}
\]
The initial terms have the preceding support count.  Every feedback term
contains \(S_\mu\) or \(D_jS_\mu\), and hence a mixed portal already
charged by \(q_L\).  Telescope a typed word one slot at a time.  With
\(T_\alpha=\Delta J_\alpha\mathcal R_0S_\mu\), identity (4.18h)
synthesizes
\(\sum_\alpha\{T_\alpha+\Delta J_\alpha Z_\alpha\}\)
at the canonical-source level before the common Green is applied.
Differentiating this identity produces only the order-two words in
(4.19a2'), derivatives of the exact local resolvents controlled by
(4.15g), (4.15i), and (4.15m), or an additional feedback factor already
charged by \(q_L\).

The new clock-lift terms are
\(\partial_\tau Q\,\delta\Theta_j[T]\) and, after \(D_j\),
\((D_j\partial_\tau Q)\delta\Theta_j[T]\) and
\(\partial_\tau Q\,D_j\delta\Theta_j[T]\).  The coefficient factors are
finite source-jet words of order at most two, while
\(\delta\Theta_j[T]\) and its score derivative are controlled by
(4.15l')--(4.15m').  Since the clock response is linear in the same mixed
source \(T\), it retains its non-target portal.  Thus the moving-level
lift adds no zero-deficit term and no new \(n\)- or \(L\)-factor.

The second summand is a same-\(\alpha\) local return and loses no
additional density factor; the original mixed word still supplies a
distinct portal.  The already proved block source-to-state estimates
therefore give
\[
\begin{aligned}
 \mathfrak E_1&\le C+Cq_L\mathfrak E_1,\\
 \mathfrak E_2&\le C(1+\mathfrak E_1^2)
                    +Cq_L\mathfrak E_2.                \tag{4.19a4}
\end{aligned}
\]
On the loose first-exit assumption \(Cq_L\le1/2\), this yields
\(\mathfrak E_1\le2C\) and then \(\mathfrak E_2\le C'\), strictly
improving both synthesis stops.  There is only one score derivative, so
no term contains two uncontrolled \(\mathfrak E_2\)-factors.  Products
of two first-order quantities use \(\mathfrak E_1^2\) and the same
surviving portal.  No
initial residual is conditioned on an evolved coefficient.  Notice
also that \(Gv\) and \(G^{\mathsf T}b\) use (4.7) only after primitive
layer synthesis; if one input is a single exposed fiber, (4.23a), not a
bare coherent block norm, supplies its deficit.

For example, if a column layer has
\(N=n\theta\) columns with \(x_j\asymp x\), its same-layer cross term in
\(A'=Z^2\) is
\[
 \mathcal M_{A,i}=2\sum_{j<k}(xg_{ij})(xg_{ik}),
 \qquad
 \mathbb E\|\mathcal M_A\|_{2,n}^2
   =2x^4\frac{N(N-1)}{n^2}.                            \tag{4.19b}
\]
On the fixed one-/two-cavity block event this is
\(n^{o(1)}x^2\theta=n^{o(1)}(x\sqrt\theta)^2\), not a
sum of \(N\) individual estimates.  Cross-layer terms follow by
polarization and Cauchy--Schwarz.  Diagonal coincidences retain their
explicit \(n^{-1}\) factor.
Equations (4.18a)--(4.18i) now check every term of the three vector-field
components.  A core source sees the product of all insertion deficits.  A
local-star source norm absorbs its own local scale and retains at least
one other portal.  The potentially order-\(L\) diagonal \(R\)-factor is
already in \(T_D\), and its remaining \(L\) is canceled by the interval
\(0.09/L\).  Thus, for the ordinary part,
\[
 \|\mathcal M\|_{\mathfrak S}\le Cp_L^{\rm mix},\qquad
 \left\|D_{q_0}\mathcal M[\mathcal R_0S]
 +\sum_{\alpha\in\mathrm{ord}}D_{d_\alpha}\mathcal M[
       (\mathcal R_\alpha-\mathcal R_0)S]\right\|_{\mathfrak S}
 \le Cp_L^{\rm mix}\|S\|_{\mathfrak S}.                 \tag{4.19d}
\]
The weaker first bound is the honest max-local-source estimate; a
quadratic bound is neither needed nor used.

For a candidate followed to \(x_{\rm cap}=n^{1/3}\), its normalized
endpoint influence is

\[
 x_{\rm cap}/\sqrt n=n^{-1/6}.                           \tag{4.20}
\]

The apparent \(U_{\rm cap}(p_L^{\rm mix})^2\) return is a fixed-time
tangent artifact.
Using (2.9) at a moving reciprocal hit replaces it by

\[
 L^C\log n\,(p_L^{\rm mix})^2+n^{-1/6+o(1)},             \tag{4.21}
\]

because

\[
 \int X_j\,ds=O(L\log n),\qquad
 n^{-1}\int X_j^2\,ds=O(Ln^{-2/3}).                     \tag{4.22}
\]

Let \(m_{\rm cand}=n^{o(1)}\) be the number of marked candidates in the
common-source system (and \(m_{\rm cand}\le2\) in a one-/two-star
cavity), and set
\[
 c_L=m_{\rm cand}\frac{x_{\rm cap}}{\sqrt n}
     =n^{-1/6+o(1)}.                                   \tag{4.22a}
\]
Combining the ordinary layer mapping (4.19d), the moving-level estimate
(4.21), and the exact local resolvents gives the source estimates
\[
 \|\mathcal M\|_{\mathfrak S}
 \le q_L,                                                \tag{4.22b}
\]
\[
 \|\mathcal KS\|_{\mathfrak S}
 \le q_L\|S\|_{\mathfrak S},\qquad
 q_L=C\{p_L^{\rm mix}+c_L
          +L^C\log n\,(p_L^{\rm mix})^2\}=o(1).       \tag{4.23}
\]
Here the first term in the exact chain-rule formula for \(\mathcal K\)
retains two insertion legs, while the \(d_\alpha\)-terms are controlled
by the recursive synthesis (4.18h).  A target local norm may absorb its
own star, but one distinct ordinary or candidate portal remains.
Differentiating a candidate
return leaves its two distinct ordinary portals, so the logarithmic term
in (4.23) still contains \((p_L^{\rm mix})^2\).  Same-star terms remain
inside their exact local resolvents.  Hence (4.16) holds for large
\(n\), and (4.17) controls the only reachable common-source tangent.

The derivative of the reconstructed physical state
\(Q=q_0+\sum_\alpha d_\alpha\) is
\[
 \partial_\lambda Q
   =Y_0+\sum_\alpha(Y_\alpha-Y_0).                      \tag{4.23b}
\]
Apply (4.18h) to the primitive \((A,u,G)\)-components in (4.23b), using
the matrix scaling (4.18g), and only then obtain \(X,Z,B,R\) from the
tangent table (4.15a).  Equations (4.7) and (4.18i) bound every regular
projected component by \(C\|S\|_{\mathfrak S}\); singular star
coordinates remain in their local norms.  No dense derived family is
summed, so no cardinality factor reappears at reconstruction.

The construction is ordered: after the row restoration, a one-column
block already contains every high-row/that-column loop.  Hence no
high-row/high-column edge is counted twice or left outside the local
blocks.  Only distinct-column interactions occur in the final use of
(4.13).

The (2\to\infty) estimates used for row and column margins are separate
from (4.16).  They follow from leave-one-star conditioning, the
diagonal-dressed source estimate (4.8c), the Gaussian primitive bound
(4.10), and the endpoint bound (4.20), as follows.  If
\(g\sim N(0,n^{-1}I)\) is independent of a
rectifiable cavity-measurable curve \(v(\eta)\), Gaussian chaining on an
arc-length net gives

\[
 \max_{|S|\le2}\sup_\eta|g_S^{\mathsf T}v_S(\eta)|
 \le C L\left\{\sup_\eta\|v_S(\eta)\|_{2,n}
             +\operatorname{Var}_{2,n}v_S\right\}       \tag{4.23a}
\]

with probability \(1-o(1)\).  Indeed, each increment is sub-Gaussian
with metric \(\|v(\eta)-v(\eta')\|_{2,n}\); a dyadic arc-length net has
polynomial entropy, and the union over at most \(n^2\) cavities costs the
single factor \(L\).  For a regular layer the braces in (4.23a) are
\(O(\gamma_L)\), hence the maximum is \(O(L\gamma_L)=o(L)\).
For a capped candidate they are \(n^{-1/6+o(1)}\), again giving \(o(1)\).
The punctured buffered construction (4.3a)--(4.7) makes the coefficient
curve independent of the displayed fresh fiber.  Thus (4.23a), rather
than a conversion of a normalized \(2\to2\) bound, supplies every
coordinate margin and is uniform at the adaptive first exit.

### 4.4 First-exit closure

Define a simultaneous first exit of the loose core bounds, the local row
and regular-column pole margins, the special difference-score and mixed
derivative stops (4.12w7b)--(4.12w7g'), the layer counts, (4.16), and
the finitely many bath moments appearing in (4.11).  Before the exit,
(4.8a)--(4.23)
give strict improvements of every core, portal, and individual-star bound.
The row comparison improves its pole margin by a fixed amount.  The
ordinary column comparison improves its \(3h_L\) formal pole gap to at
least \(2h_L\).  The no-action estimates (4.2)
close the finite core moment family as follows.

The master one-/two-cavity layer, block, time, \(\lambda\), and reciprocal
nets used above are fixed before this adaptive exit or any candidate
selector.  Their coefficient curves are deletion-measurable; evolved
full-minus-cavity feedback is controlled deterministically by
\(Z_\alpha=\mathcal R_\alpha S-\mathcal R_0S\).  Moreover, for every
regular finite-moment functional \(m\),
\[
 |m(q_{0,\lambda})-m(q_{0,0})|
 \le C\int_0^\lambda
       \|Y_0(\mu)\|_{\mathrm{loc},0}\,d\mu=o(1),       \tag{4.23c}
\]
by (4.17), (4.22b), and (4.15d).  Candidate and other singular stars are
excluded from these regular moments and retained in their local blocks.
Thus the new common-source norm explicitly transfers and strictly
improves the moment stops used to construct the master event.

For rows, dyadically peel the initial rate
\[
 I_i=A_i(0)^2/(2L^2)+Z_i(0)^2/(6L^2).
\]
The analytic \(0.11\) row gap and the \(o(L)\) punctured primitive imply
a uniform scalar envelope on \(\tau\le0.09\) for every cell
\(I_i\le1+\eta\).  Gaussian moderate-deviation counts give
\[
 n^{-1}\sum_i |A_i|^p|Z_i|^q\le C_{p,q}
\]
for every one of the finitely many pairs \(p+q\le 12\) used in
the core estimates (4.7b)--(4.8f) and in (4.12b).  Cells of rate
\(>1+\eta\) are absent with high
probability after a union bound.  The regular-column gap
\((T_*+8h_L)-(T_*+5h_L)=3h_L\) gives the analogous finite
\(X,R\) moments with only polylogarithmic resolvent loss; columns in
\(\mathscr C_L\) are excluded from these moments and retained in their
exact local blocks.  In particular,
\[
 \sup_s\|B_c'(s)\|_{2,n}\le C M_LR_L^D,\qquad
 \operatorname{Var}_{2,n}B_c\le C\gamma_L,\qquad
 \operatorname{Var}_{2,n}B_c'
 =\int_0^{\sigma_{\rm pre}}\|B_c''(s)\|_{2,n}\,ds
 \le CM_LR_L^D,
\]
which are the estimates used in (4.12h).  The last follows term by term
from (4.12h')--(4.12h'''), so it adds only a finite collection of
degree-\(D\) moment stops.  Hölder and (2.1) close the mixed and trained
moments.  Each estimate is strict relative to its
loose first-exit threshold, so continuity rules out an exit.

We record the result.

**Lemma 2 (covariant Schur peeling).**  On the pre-cap interval
\([0,\sigma_{\rm pre}]\), with probability tending to one:

1. every row is \(o(1)\)-close in scaled endpoint and radial-response norm
   to (3.4), uniformly to \(\tau=T_{\rm pre}\) unless action or a
   candidate cap occurs first;
2. every regular column is (o(1))-close to (3.2), uniformly on the same
   interval;
3. a candidate one-column clock and its radial derivative have error
   \(O(\gamma_L+p_L^{\rm mix}+n^{-1/6+o(1)})=o(1/\log L)\) down to
   \(X_j=n^{1/3}\);
4. the corresponding one-row, one-column, and leave-two-column versions
   hold simultaneously, as do the fixed \(X(0)\)-measurable
   parent-deleted versions with normalized \(X^2\)-mass
   \(n^{-c+o(1)}\).

## 5. Reciprocal one-column clock

The candidate state Green is not bounded at a fixed time.  The clock is.
Put

\[
 W=U^{-1},\qquad \lambda=H+PW=-\frac18W_\tau.            \tag{5.1}
\]

Write the exact reduced equations as

\[
 H_\tau=3+e_H,\qquad P_\tau=26/W+e_P.                    \tag{5.2}
\]

Then

\[
 W_\tau=-8\lambda,\qquad
 \lambda_\tau=29+e_H+We_P-8P\lambda.                    \tag{5.3}
\]

On the outgoing branch (\lambda\ge c>0), use (W) as independent
variable:

\[
 \frac{dP}{dW}=-\frac{13}{4W\lambda}-\frac{e_P}{8\lambda},
 \qquad
 \frac{d\lambda}{dW}
 =P-\frac{29+e_H+We_P}{8\lambda}.                        \tag{5.4}
\]

Equation (5.4) is not estimated by inserting
\(e_P=r_P+\partial_\tau J\) pointwise, because (4.12e) controls \(J\),
not \(J_\tau\).  Put

\[
 \sigma=\log(W_0/W),\qquad
 \bar P=P-J,\qquad \bar\lambda=\lambda-WJ
                  =H+W\bar P.                           \tag{5.4a}
\]

Since \(d\tau/d\sigma=W/(8\lambda)\) and
\((WJ)_\sigma=-WJ+WJ_\sigma\), the endpoint derivative cancels
identically:

\[
 \begin{aligned}
 \bar P_\sigma&=\frac{13}{4\lambda}
                 +\frac{Wr_P}{8\lambda},\\
 \bar\lambda_\sigma&=-W\bar P+
 \frac{W(29+e_H+Wr_P)}{8\lambda},\qquad
 \lambda=\bar\lambda+WJ.                                \tag{5.4b}
 \end{aligned}
\]

The difference from the formal system therefore has the triangular form

\[
 p_\sigma=O(\ell)+O(\epsilon_n),\qquad
 \ell_\sigma=-Wp+O(W\ell)+O(W\epsilon_n).               \tag{5.4c}
\]

On a fixed initial \(\sigma\)-interval ordinary Gronwall applies.  On
the tail, \(\int W(1+\sigma)d\sigma<\infty\), so the integral form of
(5.4c) gives

\[
 \sup_\sigma|\ell|+
 \sup_\sigma\frac{|p|}{1+\sigma}\le C\epsilon_n.         \tag{5.4d}
\]

Fixed-\(W\) score differentiation gives the same system, because
(4.12e) controls one \(D_b^W\)-derivative of every source.  Thus
\(\lambda\) and its score derivative have \(O(\epsilon_n)\) error even
though \(P\) may have \(O(\epsilon_n\log(W_0/W))\) error.

For the formal system, (P=O(1+\log(W_0/W))) while
(c\le\lambda\le C).  If (s=\log(W_0/W)), the fixed-(W) radial tangent
satisfies

\[
 \partial_s(DP)=O(D\lambda),\qquad
 \partial_s(D\lambda)=-WDP+O(WD\lambda).                \tag{5.5}
\]

Since (W=W_0e^{-s}), the second equation has an integrable coefficient.
Thus

\[
 \sup_{W\ge w}|D\lambda(W)|\le C,\qquad
 |DP(W)|\le C(1+\log(W_0/W)).                            \tag{5.6}
\]

The hit of a fixed reciprocal level (w) is

\[
 \Theta_w=\int_w^{W_0}\frac{dW}{8\lambda(W)},           \tag{5.7}
\]

and consequently both (Theta_w) and its radial derivative are bounded
uniformly as (w\downarrow0).

The source (mathcal E_0) in (2.6) is not estimated by absolute value.
In the column-deleted bath it is the derivative of the endpoint

\[
 g(0)^{\mathsf T}D_{A^\circ(s)}z^\circ(s).               \tag{5.8}
\]

Equivalently, one may use the exact normal form

\[
 \Phi(W,\lambda)=-\frac{13}{4\lambda}\log W,
\]

\[
 \partial_\tau\Phi
 =\frac{26}{W}+\frac{13}{4}\frac{\lambda_\tau}{\lambda^2}\log W.
                                                                    \tag{5.9}
\]

The logarithmic endpoint in (5.9) and the logarithmic integral cancel in
the derivative of (5.7).  At geometric reciprocal resets the additive
constant in (Phi) is chosen to make the transformed (P) continuous, so
the cancellation telescopes.

The relevant perturbation norm is therefore the fixed-\(W\), endpoint-
primitive norm induced by (5.4), not a supremum norm on \(DU\).  The
same-star estimate (4.12e), followed by the distinct-star contraction,
gives in this norm

\[
 |\widehat\Theta_w-\Theta_w|
 +|D\widehat\Theta_w-D\Theta_w|
 \le C\{\gamma_L+p_L^{\rm mix}+n^{-1/6+o(1)}\}.        \tag{5.10}
\]

The collision arithmetic at

\[
 w_{\rm cap}=L^2n^{-1/3},\qquad x_{\rm cap}=n^{1/3},     \tag{5.11}
\]

is (x_{\rm cap}^2/n=n^{-1/3}).  In (5.4) its integrated contribution is
smaller than (n^{-1/6+o(1)}).  A centered error of pointwise size
(n^{-1/2+o(1)}/W) costs only (n^{-1/2+o(1)}\log(1/w_{\rm cap})).
Thus (5.10) holds all the way to (5.11), although (DU) itself diverges.

The formal radial tangent is strictly cooperative.  If
(u=D_bU,p=D_bP), then

\[
 u_\tau=8(P+2HU)u+8Up,\qquad p_\tau=26u,
 \qquad u(0)=0,\quad p(0)=1.                             \tag{5.12}
\]

The off-diagonal coefficients are positive; if (u) attempted to return to
zero, its derivative would be (8Up>0).  To make the limiting pole
derivative quantitative, put
\[
 w_b=D_bW=-u/U^2,\qquad p=D_bP.
\]
Then \(p_\tau=26u\), \(p(0)=1\), and
\[
 (w_b)_\tau=-8(pW+Pw_b),\qquad
 w_b(\tau)=-8\int_0^\tau p(t)W(t)
       \exp\!\left\{-8\int_t^\tau P(r)\,dr\right\}dt.  \tag{5.12a}
\]
On the compact contender set, \(p\ge1\); on a fixed initial time
interval, \(W\ge c\); and
\(\int_0^{T_c}P\,d\tau\le C\), because
\(P=O(1+\log(W_0/W))\) and \(d\tau=dW/(-8\lambda)\).
Therefore \(w_b(T_c)\le-c<0\) uniformly.  Moreover
\[
 W_\tau(T_c)=-8H(T_c),\qquad H(T_c)=3T_c\in[c,C],
\]
since \(PW\to0\).  Implicit differentiation of
\(W(T_c(b),b)=0\) now gives
\[
 \partial_bT_c=-\frac{w_b(T_c)}{W_\tau(T_c)},
\]
which is uniformly negative.  Hence every contender clock has

\[
 -C\le \partial_bT_c(a,b)\le-c<0                       \tag{5.13}
\]

on the compact outgoing contender set.  Equations (5.6)--(5.10) transfer
this transversality to the exact one-column clocks.

## 6. Moving window, quenched coarea, and the first cap

Recall \(h_L=(\log L)^{-1}\) from (4.0), and set

\[
 S_L=h_LL^2,\qquad
 T_L^-=T_*+h_L,\quad T_L^+=T_*+4h_L.                     \tag{6.1}
\]

Both cutoffs are below (0.09) for large (n).  The smaller one contains the
witness; the larger one is the buffered candidate window.

Delete the common (X(0))-measurable parent set

\[
 \mathscr P=\{j:X_j(0)\ge a_0L^2\},                     \tag{6.2}
\]

where (a_0) is smaller than the compact contender lower bound from
Section 3.  Put
\[
 q_j=g_j(0)^{\mathsf T}B^{(-\mathscr P)}(0).
\]
The fixed \(X(0)\)-measurable block has
\[
 q_{\mathscr P}:=\langle X(0)^2
                    1_{\{X(0)\ge a_0L^2\}}\rangle_n
 \le n^{-a_0/2+o(1)}.                                  \tag{6.2a}
\]
Conditional Gaussian bilinear concentration and a union over the parent
labels give
\[
\max_{j\in\mathscr P}L^{-1}\left|
g_j(0)^{\mathsf T}D_{A(0)}
\sum_{k\in\mathscr P\setminus\{j\}}g_k(0)X_k(0)\right|
\le n^{-a_0/4+o(1)}=o(h_L).                            \tag{6.2b}
\]
Together with (4.0b), this proves uniformly for \(|S|\le2\)
\[
 \left|q_j/L-b_j^{[-S]}\right|=o(h_L).                 \tag{6.2c}
\]
The parent deletion is therefore an ordinary fixed tail-layer deletion
in the source-space norm: it perturbs every regular bath moment and the
one-star \(C_b^1(W)\) clock estimate by
\(n^{-c(a_0)+o(1)}=o(h_L)\).  Lemma 2 and (5.10) consequently hold
simultaneously for this common \(\mathscr P\)-deleted bath, not only for
one-/two-column deletions.  Types of cost \(>1+\eta\) are absent from
the early-clock region with probability \(1-o(1)\) by the same
moderate-deviation union bound used in (4.0d).

Against the common bath, insert each parent column alone and
let (Theta_j) be its exact cap clock (5.11).  Conditional on the bath,
the columns are independent, and the exact regression is

\[
 g_j(0)=\frac{q_j}{\|B^{(-\mathscr P)}(0)\|_2^2}
 B^{(-\mathscr P)}(0)+\xi_j,\qquad
 \xi_j\perp B^{(-\mathscr P)}(0),                       \tag{6.3}
\]

and, conditionally, \(q_j\) is Gaussian with variance
\(\sigma_n^2=3+o(h_L)\), independent of \(\xi_j\).  The triples
\((X_j,q_j,\xi_j)\) are independent across parents.  Consequently the
scaled marks

\[
 a_j=X_j(0)/L^2,\qquad b_j=q_j/L                       \tag{6.4}
\]

have raw-label density
\(L^C n^{-I_c(a,b)+o(h_L)}\) on compact type cells.  The
\(o(h_L)\), rather than a bare \(o(1)\), follows from the Gaussian
density formula, \(\sigma_n^2=3+o(h_L)\), and the fixed-degree moment
estimates in Lemma 2.

Let \(\mathcal F_n\) be the common-bath sigma-field together with the
parent membership pattern, but not the fresh parent values.  If
\(\pi_L=\Pr\{X\ge a_0L^2\}\), the conditional density of \(a\) for one
known parent contains \(\pi_L^{-1}\).  The invariant statement is
therefore the *aggregate raw-label* intensity.  By (5.10), (5.13), and
one-dimensional coarea in \(b\), with \(\xi\) integrated as an
independent nuisance Gaussian,

\[
 \Lambda_n(t):=
 \sum_{j\in\mathscr P}\frac d{dt}
 \Pr\{\Theta_j\le t,\ (a_j,b_j)\in\mathcal K
                   \mid\mathcal F_n\}
 \le L^C n^{1-I_*(t)+o(h_L)},                            \tag{6.5}
\]

where (I_*(t)=\inf\{I_c(a,b):T_c(a,b)\le t\}).  Exact homogeneity gives

\[
 I_*(t)=(T_*/t)^2.                                       \tag{6.6}
\]

Let

\[
 E_L=\{j\in\mathscr P:\Theta_j\le T_L^+\}.             \tag{6.7}
\]

Equations (6.2b)--(6.2c), Lemma 2, and (5.10) give
\[
 \max_{j\in\mathscr P,\ |S|\le2}
 |\Theta_j-T_c(a_j,b_j^{[-S]})|=o(h_L)                 \tag{6.7c}
\]
on the compact contender set.  Hence, on the master leave-two event,
\(E_L\subset\mathscr C_L\) for all sufficiently large \(n\), because
\(T_L^+=T_*+4h_L<T_*+8h_L-o(h_L)\).  Thus the reciprocal clocks used
here are exactly the predeclared candidate blocks, not a set selected
after invoking Lemma 2.

For the lower bound, radially scale a certified cost-one minimizing cell
so that its formal clock is \(T_*+\theta h_L\), \(0<\theta<1\), and
then take an \(O(h_L)\)-by-\(O(h_L)\) cell around it.  Throughout that
cell,

\[
 T_c\le T_*+(1-\delta)h_L,\qquad
 I_c\le1-\kappa h_L                                    \tag{6.7a}
\]

for fixed \(\delta,\kappa>0\).  The exact clock error is \(o(h_L)\),
so every good-fiber mark in this cell belongs to \(E_L\).  Its raw-label
probability is

\[
 n^{-1}\exp\{(\kappa+o(1))S_L\}.                       \tag{6.7b}
\]

Conditional Chernoff gives the lower count.  Integrating the aggregate
upper intensity (6.5) gives the upper count.  Hence constants
\(0<c<C\) exist such that

\[
 e^{cS_L}\le |E_L|\le e^{CS_L}                           \tag{6.8}
\]

with probability tending to one.

For spacing, write \(p_j=\Pr\{\Theta_j\le T_L^+\mid\mathcal F_n\}\)
and let \(\rho_j\) be its clock density.  Conditional independence gives
the exact factorial formula

\[
 \begin{aligned}
 &\mathbb E\!\left[\sum_{j\ne k}
 1_{\{j,k\in E_L\}}1_{\{|\Theta_j-\Theta_k|\le\Delta\}}
 \middle|\mathcal F_n\right]\\
 &\quad\le2\Delta
 \left(\sum_jp_j\right)\left(\sup_t\sum_j\rho_j(t)\right)
 \le \Delta e^{C'S_L}.                                  \tag{6.9}
 \end{aligned}
\]

Taking

\[
 \Delta_L=e^{-D_0S_L}                                   \tag{6.10}
\]

with \(D_0>C'\) yields, with high probability,

\[
 \min_{j\ne k\in E_L}|\Theta_j-\Theta_k|\ge\Delta_L.   \tag{6.11}
\]

The coarea is restricted to a compact rate set containing all types of
cost at most \(1+\eta\).  Its complement has raw probability
\(L^Cn^{-1-\eta}\), and the bad Gaussian-fiber event is chosen with
probability \(n^{-M}\).  Both are negligible relative to (6.9).  This
argument uses exact one-column clocks; no formal-clock ordering is
assumed, and the dependence on \(\xi_j\) has been integrated rather than
dropped.

Restore the columns in \(E_L\) by the exact homotopy (4.13)--(4.15).
At a candidate cap each insertion has normalized endpoint size
\(n^{-1/6+o(1)}\).  Since \(|E_L|=n^{o(1)}\),

\[
 \|\mathcal M\|_{\mathfrak S}\le n^{-1/6+o(1)},
 \qquad
 \|\mathcal K\|_{\mathfrak S\to\mathfrak S}
       \le n^{-1/6+o(1)}.                               \tag{6.12}
\]

The first estimate is intentionally stated at the honest max-local-source
scale.  A target local norm can absorb its own candidate leg, so a second
candidate deficit need not remain; the stronger quadratic bound is neither
asserted nor needed.

Here the candidate component of the common source norm
\(\mathfrak S\) is exactly the fixed-\(W\) reciprocal/output
\(C_b^1\) norm of Sections 4.2.1 and 5; (2.9) is used on every
candidate-to-row leg.  Equations (4.15d), (4.17), and (5.10) therefore
give

\[
 \max_{j\in E_L}
 \|\Theta_j^{\rm full}-\Theta_j\|_{C^1}
 \le n^{-1/6+o(1)}=o(\Delta_L).                          \tag{6.13}
\]

The noncandidate part of \(\mathscr P\) has clock margin at least
\(2h_L\) at the eventual first cap.  Reciprocal transversality therefore
bounds each such column by \(X_j\le L^C/h_L\).  Since its initial
normalized \(X^2\)-mass is \(n^{-c(a_0)+o(1)}\), the layer portal bound
and the exact homotopy give a collective clock perturbation
\[
 n^{-c(a_0)/2+o(1)}=o(\Delta_L).
\]
This argument restores the noncandidates as a block; it does not union
bound separate adaptive one-column baths.

It follows that the first full cap is unique, occurs by
((T_*+2h_L)/L<0.09/L), and has an index (e) such that

\[
 X_e=n^{1/3},\qquad
 \max_{k\ne e}X_k\le L^C\Delta_L^{-1}=n^{d_L},
 \qquad d_L\to0.                                        \tag{6.14}
\]

Moreover, with (h_e=g_e^{\mathsf T}D_Ag_e) and

\[
 \Psi_e=\rho_e+h_eX_e/2,
\]

the outgoing reciprocal branch and (5.10) imply

\[
 h_e\ge c/L,\qquad \Psi_e\ge cX_e/L.                    \tag{6.15}
\]

## 7. One-leader release and fixed action

Let (s_0) be the cap time, write (j=e,x=X_j), and stop at fixed action
or at

\[
 x=C_1\sqrt{nL}.                                         \tag{7.1}
\]

Lemma 2 is not extended past \(s_0\).  Everything below is a direct
one-leader comparison on the short interval (7.3), using only the
cap-time master event, the exact equations (2.4)--(2.7), and
leave-two estimates fixed before selection.

Bootstrap (h\ge c/(2L)), (Psi\ge0), and the rival bound in (6.14).
Then \(R_j=hx+\rho=\Psi+hx/2\), so

\[
 x'=8xR_j\ge cx^2/L.                                     \tag{7.2}
\]

Consequently, until (7.1),

\[
 \int ds\le L^{C}n^{-1/3},\qquad
 \int x\,ds\le L^C,
 \qquad \int x^2\,ds\le L^C\sqrt n.                   \tag{7.3}
\]

The leader remains delocalized:
\[
 \max_i|g_{ij}|\le L^C/\sqrt n,\qquad
 \max_i|g_{ij}|x\le L^C.                                 \tag{7.3b}
\]
The first bound holds at (s_0) by the one-column cavity event; (2.1) and
(7.3) improve it for the trained part.  The row pole gap gives
(\|z\|_\infty+\|A\|_\infty\le L^C) at (s_0).  Equations (2.8), (7.3),
and (7.3b) preserve these polylogarithmic bounds during the release.

The pure leader chain is kept exact.  Every leader--rival portal contains
a distinct initial Gaussian column factor.  Before selecting the leader,
construct one master leave-two event, uniform over all ordered column
pairs and a deterministic reciprocal/time net; its interpolation modulus
is supplied by the short release bounds (7.3).  Thus adaptive selection
of \(j\) and \(s_0\) does not change the conditioning.  On this event,
leave-two-column Gaussian bilinear concentration gives
\[
 \max_{k\ne j}|g_k^{\mathsf T}D_Ag_j|
 \le n^{-1/2+o(1)}.                                      \tag{7.3a}
\]
During the release, expand \(A-A(s_0)=\int(z+xg_j)^2ds\).  The three
resulting off-diagonal contractions are respectively a centered quadratic,
\(\sum_i g_{ik}z_i g_{ij}^2\), and
\(\sum_i g_{ik}g_{ij}^3\).  Their conditional standard deviations are
at most \(n^{-1/2+o(1)},n^{-1+o(1)},n^{-3/2+o(1)}\).
After multiplication by the three exposures in (7.3), all are
\(n^{-1/3+o(1)}\).  Replacing either column by its trained part uses (2.1)
and is smaller.  Thus (6.14), (7.3), and (2.1) give

\[
 |g_k^{\mathsf T}D_Ag_j|\le n^{-1/3+o(1)},\qquad
 \max_{k\ne j}X_k\le n^{d_L+o(1)}                      \tag{7.4}
\]

throughout the release.  The first estimate may be weakened substantially;
its role is only to make
(\int x|g_k^{\mathsf T}D_Ag_j|ds=o(1)).  The exact rank-one update gives
the same estimate for the trained part.

For a rival, split
\[
 R_k=x\,g_k^{\mathsf T}D_Ag_j+R_k^{(-j)}.
\]
At (s_0), reciprocal separation gives
(|R_k^{(-j)}|\le n^{d_L+o(1)}).  On the bootstrap
(\max_{k\ne j}X_k\le2n^{d_L+o(1)}), the Jacobian of the tag-deleted
coordinate equations is (n^{d_L+o(1)}), whereas the release lasts
(n^{-1/3+o(1)}).  The first term has integrated size (o(1)) by
(7.3)--(7.4).  A coordinatewise Grönwall estimate therefore gives
\[
 \int_{s_0}^s|R_k(r)|\,dr=o(1)
\]
uniformly, which strictly improves the rival bootstrap in (7.4).
Fixed bath moments and (7.3)--(7.4) now yield

\[
 \langle A^4\rangle_n=n^{o(1)},\qquad
 |\mathcal E_0|\le n^{1/2+o(1)},\qquad
 |\mathcal E_2|\le n^{-1/2+o(1)}.                        \tag{7.5}
\]

At a hypothetical first zero of (Psi), one has (R_j=hx/2).  From
(2.5)--(2.7),

\[
 \Psi'\ge2h^2x^2
 -n^{1/2+o(1)}-x^2n^{-1/2+o(1)}-2x^3n^{-1+o(1)}>0       \tag{7.6}
\]

uniformly for (n^{1/3}\le x\le C_1\sqrt{nL}).  Also

\[
 \int(h')_-ds
 \le\frac4n\langle A^4\rangle_n\int x^2ds=o(L^{-1}).  \tag{7.7}
\]

Thus the bootstrap cannot fail and

\[
 R_j\ge cx/L.                                             \tag{7.8}
\]

If fixed action has not occurred first, (7.1) is reached after
(L^{C}n^{-1/3}=o(L^{-1})) further feature time.  Finally,

\[
 (x^2)'=16x^2R_j,\qquad K_n\ge\frac{16}{n}xR_j^2,
\]

so along the actual trajectory

\[
 \frac{df_n}{d(x^2)}\ge\frac{R_j}{nx}\ge\frac{c}{nL}.  \tag{7.9}
\]

Integrating from (x=n^{1/3}) to (7.1) gives

\[
 f_n(s)-f_n(s_0)\ge cC_1^2-o(1).                         \tag{7.10}
\]

Choose (C_1) so that the right side exceeds a fixed (delta_0), or
stop earlier when the same action is reached.  This proves (1.3).

## 8. Logical dependencies and audit points

The proof uses the following three distinctions; dropping any one recreates
an already identified false statement.

1. **Local blocks versus the bath.**  The full-state Hessian at a candidate
   cap is polynomially large.  Only the bounded core is estimated by an
   absolute Jacobian norm.  Every singular same-row and same-column chain is
   solved in its exact local block.

2. **Fixed time versus moving reciprocal level.**  A fast column has a
   polynomial fixed-time state tangent.  The endpoint identity (2.9) and
   the fixed-(W) equations (5.4) cancel it.  Only clocks and moving-hit
   endpoint states are compared.

3. **One-star returns versus mixed portals.**  Trace and same-edge returns
   are retained before centering.  The lifted defect (4.13) contains two
   distinct insertions, and its derivative retains one.  The exact homotopy,
   not conditioning on an adaptive full resolvent, propagates the cavity
   estimates.

The exact arithmetic certificate has been rerun from the recorded source,
and `sha256sum -c outer_pole_certificate.sha256` passes.  The remaining
claims in this note are analytic and probabilistic; no simulation or
finite-width extrapolation is used.
