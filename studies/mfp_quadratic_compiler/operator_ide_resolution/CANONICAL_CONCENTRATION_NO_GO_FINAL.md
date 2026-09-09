# Canonical concentration no-go for the quadratic depth-two network

Status: withdrawn proof candidate, 22 August 2026.  A hostile audit found
that the Hessian estimate below was applied to the full inserted-tag space,
where it is false at the mesoscopic cap; it is valid only on a reduced bath
after the singular tag modes are projected into their exact local blocks.
Sections 3--6 therefore remain a repair program, not a theorem.  This note
supersedes the
mechanisms in `CANONICAL_CONCENTRATION_NO_GO.md` and
`CANONICAL_CONCENTRATION_NO_GO_REPAIRED.md`.  Those files are retained as an
audit trail.

Throughout,

\[
 \langle v,w\rangle_n=n^{-1}v^{\mathsf T}w,
 \qquad \|v\|_{p,n}=\langle |v|^p\rangle_n^{1/p},
 \qquad L=L_n=\sqrt{\log n}.
\]

## 1. Result

Let \(A_i,u_j,W_{ij}\) be independent standard Gaussians, put
\(G(0)=W/\sqrt n\), and define

\[
 X=u^{\odot2},\qquad Z=GX,\qquad B=A\odot Z,
 \qquad R=G^{\mathsf T}B,
 \qquad f_n=\langle A,Z^{\odot2}\rangle_n .                 \tag{1.1}
\]

In feature time \(s\), consider

\[
 A'=Z^{\odot2},\qquad X'=8X\odot R,
 \qquad G'=\frac2nBX^{\mathsf T}.                           \tag{1.2}
\]

Then

\[
 K_n:=f_n'
 =\langle Z^{\odot4}\rangle_n
 +4\langle X^{\odot2}\rangle_n\langle B^{\odot2}\rangle_n
 +16\langle X\odot R^{\odot2}\rangle_n\ge0.               \tag{1.3}
\]

**Theorem 1 (initial concentration layer).**  There are deterministic
constants \(c_0,\delta_0>0\) such that

\[
 \Pr\left\{
  \inf\{s:f_n(s)-f_n(0)\ge\delta_0\}
       \le \frac{0.09+o(1)}{\sqrt{\log n}}
 \right\}\longrightarrow1.                                \tag{1.4}
\]

For a fixed positive label \(y_\star>0\), learning rate
\(\eta\ge\eta_0>0\), and physical MSE time

\[
 \dot\theta=2\eta(y_\star-f_n)\theta',                    \tag{1.5}
\]

choose \(\delta_0<y_\star/4\).  The corresponding physical hitting time
converges to zero in probability.  Hence \(f_n\) cannot converge uniformly
on a nontrivial compact physical-time interval to a continuous readout.
Consequently the autonomous operator/traffic/measure IDE required in
`FROZEN_CONJECTURE.md` does not exist for the canonical iid-Gaussian
sequence.

The proof has four ingredients.  Sections 2--4 establish a sharp stopped
susceptibility theorem.  Section 5 certifies the finite-dimensional extreme
column mechanism.  Section 6 uses a shrinking extreme window and exact
clock coarea.  Section 7 converts the first mesoscopic cap into fixed output
action.

## 2. Exact finite-width identities

The trained matrix and the two preactivations have the Volterra forms

\[
 G(t)=G(0)+\frac2n\int_0^tB(r)X(r)^{\mathsf T},dr,           \tag{2.1}
\]

\[
\begin{aligned}
 Z(t)&=G(0)X(t)
  +2\int_0^tB(r)\langle X(r),X(t)\rangle_n,dr,\\
 R(t)&=G(0)^{\mathsf T}B(t)
  +2\int_0^tX(r)\langle B(r),B(t)\rangle_n,dr .
\end{aligned}                                               \tag{2.2}
\]

For a tagged column (j), write

\[
 x=X_j,\quad g=G_{\cdot j},\quad z=Z-xg,
 \quad H_-=G_{\cdot,-j}D_{X_{-j}}G_{\cdot,-j}^{\mathsf T}, \tag{2.3}
\]

\[
 h=g^{\mathsf T}D_Ag,\qquad
 \rho=g^{\mathsf T}D_Az,\qquad R_j=hx+\rho.                \tag{2.4}
\]

Direct differentiation gives

\[
 x'=8x(hx+\rho),                                           \tag{2.5}
\]

\[
 \rho'=x\mathcal P+\mathcal E_0+x^2\mathcal E_2,          \tag{2.6}
\]

where

\[
\begin{aligned}
\mathcal P={}&2\langle A^2z^2\rangle_n
 +2\sum_i g_i^2z_i^2
 +2Q_-\sum_iA_i^2g_i^2
 +8g^{\mathsf T}D_AH_-D_Ag,\\
\mathcal E_0={}&\sum_i g_iz_i^3
 +2Q_-\sum_iA_i^2g_iz_i
 +8g^{\mathsf T}D_AH_-D_Az,\\
\mathcal E_2={}&\frac2n\sum_iA_i^2g_iz_i+\sum_i g_i^3z_i,
 \qquad Q_-=\langle X_{-j}^2\rangle_n .
\end{aligned}                                               \tag{2.7}
\]

Also

\[
 h'=\sum_i\left(g_iZ_i+\frac{2x}{n}A_i^2\right)^2
 -\frac{4x^2}{n^2}\sum_iA_i^4
 \ge-\frac{4x^2}{n}\langle A^4\rangle_n .                \tag{2.8}
\]

For a row (i), put (a=A_i,z_i=Z_i,b_i=a z_i), and

\[
 Q=\langle X^2\rangle_n,\quad
 S_i=\sum_jG_{ij}^2X_j,\quad
 R_j^{(-i)}=\sum_{k\ne i}G_{kj}B_k,
 \quad N_i=\sum_jG_{ij}X_jR_j^{(-i)} .                     \tag{2.9}
\]

Then exactly

\[
 a'=z_i^2,\qquad
 z_i'=(2Q+8S_i)a z_i+8N_i.                                 \tag{2.10}
\]

For every fixed initial column set (D), integration by parts gives

\[
8\int_0^t\sum_{j\in D}G_{ij}X_jR_j^{(-i)},ds
=\left[\sum_{j\in D}G_{ij}X_j\right]_0^t
-\int_0^t(2q_D+8S_{iD})B_i,ds,                            \tag{2.11}
\]

where

\[
q_D=n^{-1}\sum_{j\in D}X_j^2,
\qquad S_{iD}=\sum_{j\in D}G_{ij}^2X_j.                   \tag{2.12}
\]

No time-dependent layer is used in (2.11), so it has no hidden boundary
flux.

## 3. Sharp regular-bath susceptibility

This section gives the finite-width probability theorem used later.  It is
stated in a little more detail than usual because a coarse (L^2) Hessian
bound is insufficient: the row core cutoff must be (o(L)).

### 3.1 Gated flows and the normalized Hessian

For contractive gates (0\le\alpha_i,\beta_j\le1), define

\[
 f_{\alpha,\beta}
 =\frac1n\sum_i\alpha_iA_i
 \left(\sum_j\beta_jG_{ij}u_j^2\right)^2.                 \tag{3.1}
\]

We use only the following gates: a fixed (X(0))-measurable column mask,
one or two column insertions, finitely many row deletions, and their affine
interpolations.  In particular, there is no bulk data-dependent row
selector.  Every gated evolution is again a gradient flow.

The natural metric is

\[
 \|(a,v,H)\|_*^2=\|a\|_{2,n}^2+\|v\|_{2,n}^2+\|H\|_F^2.  \tag{3.2}
\]

If

\[
 \delta X=2D_uv,qquad \delta Z=HX+G\delta X,
\]

then the normalized Hessian quadratic form is

\[
 D^2f[(a,H,v)]^2
 =4\langle a,Z\delta Z\rangle_n
 +2\langle A,(\delta Z)^2\rangle_n
 +4\langle B,H\delta X\rangle_n
 +4\langle R,v^2\rangle_n.                                \tag{3.3}
\]

Put (C(t)=A(t)-A(0)=\int_0^tZ(s)^2ds\ge0).  Termwise
Cauchy--Schwarz in (3.3) gives

\[
 \lambda_{\max}(D^2f)\le C\mathcal M(t),                  \tag{3.4}
\]

where (mathcal M) is the maximum of

\[
 \|Z\|_\infty\|X\|_{2,n},\quad
 \|D_ZGD_u\|,\quad
 \|A_+\|_\infty\|X\|_{2,n}^2,\quad
 \|D_AGD_u\|\|X\|_{2,n},                                 \tag{3.5}
\]

\[
 \lambda_{\max}(D_uG^{\mathsf T}D_AGD_u),\quad
 \|B\|_{2,n}\|u\|_\infty,\quad \|R_+\|_\infty.         \tag{3.6}
\]

The signed term in (3.6), rather than its absolute positive-part bound, is
essential.  It splits exactly as

\[
D_uG^{\mathsf T}D_AGD_u
=D_uG^{\mathsf T}D_{A(0)}GD_u
 +(D_{\sqrt C}GD_u)^{\mathsf T}(D_{\sqrt C}GD_u).          \tag{3.7}
\]

### 3.2 Uniform Gaussian design event

The following standard simultaneous submatrix estimate is the only random
matrix input.  For iid (G(0)_{ij}\sim N(0,1/n)), with probability
(1-n^{-D}) for every fixed (D), simultaneously for all row subsets
(I) and all fixed initial Gaussian column-type blocks (J),

\[
 \|P_IG(0)P_J\|
 \le C_D\left[
  \sqrt{|I|/n}+\sqrt{|J|/n}
 +\sqrt{\{ |I|\log(en/|I|)+|J|\log(en/|J|)+\log n\}/n}
 \right].                                                  \tag{3.8}
\]

This follows from the fixed-submatrix Gaussian norm tail and a union bound.
Dyadic layer-cake decomposition therefore gives, for every later adaptive
row weight (r) satisfying fixed-moment and maximum type bounds and every
column weight (c) dominated by its fixed initial Gaussian type,

\[
 \|D_rG(0)D_c\|
 \le C_D\bigl(\|r\|_\infty\|c\|_{2,n}
      +\|r\|_{2,n}\|c\|_\infty\bigr)(\log L)^C.           \tag{3.9}
\]

Thus (3.9) is valid even though (r) is (G(0))-adaptive.  For the
centered signed matrix, Gaussian block decoupling gives

\[
 \|D_{u(0)}G(0)^{\mathsf T}D_{A(0)}G(0)D_{u(0)}\|
 \le CL(\log L)^C.                                        \tag{3.10}
\]

Indeed, on initial (u)-type blocks of sizes (m_s,m_t), the unweighted
block is at most

\[
 C\left(\sqrt{m_s/n}+\sqrt{m_t/n}+L/\sqrt n\right)(\log L)^C,
\]

and (m_s/n\le Ce^{-cs^2}).  Summation after multiplying by the two
types proves (3.10).  Removing finitely many rows changes (3.10) by only
finitely many rank-one terms.  A contractive column mask is a principal
congruence and cannot increase its norm.

On the stopped interval \(t\le0.09/L\), \(u(t)=D_{\lambda(t)}u(0)\) with
\(\|\lambda\|_\infty\le C\).  Moreover

\[
 \|\sqrt C\|_\infty\le C\sqrt L,\qquad
 \|\sqrt C\|_{2,n}\le CL^{-1/2}.                          \tag{3.11}
\]

Equations (3.9)--(3.11) yield

\[
 \|D_{\sqrt C}G(0)D_{u(t)}\|^2\le CL(\log L)^C.           \tag{3.12}
\]

Finally, the rank-one identity (2.1) and fixed moments give the same bounds
with (G(t)) in place of (G(0)).  Hence, uniformly over the permitted
gated paths,

\[
 \mathcal M(t)\le CL(\log L)^C.                            \tag{3.13}
\]

Because the Jacobian is self-adjoint in (3.2), (3.4) and (3.13) imply for
the regular-bath Green operator

\[
 \|\Phi(t,s)\|_{\rm op}
 +n^{-1/2}\|\Phi(t,s)\|_{\rm HS}
 \le \Gamma_L:=\exp\{C(\log L)^C\}=n^{o(1)}.              \tag{3.14}
\]

The same estimate holds for analytic gate derivatives because one
differentiates the actual gated flow,

\[
 \partial_t\partial_q\theta_q
 =D^2f_q(\theta_q)\partial_q\theta_q
 +\partial_q\nabla f_q(\theta_q),                          \tag{3.15}
\]

rather than estimating a straight secant.

### 3.3 Exact Schur centering and the row primitive

Deleting row (i) makes (G_{i\cdot}(0)) independent of the punctured
bath.  The entire row-to-bath-to-row channel is retained by the exact causal
Schur complement.  If (K) is the tangent Volterra kernel, then

\[
 \Sigma_i=K_{ii}+K_{iB}\star(I-K_{BB})_\star^{-1}\star K_{Bi},
 \qquad S_i=(I-\Sigma_i)_\star^{-1}.                       \tag{3.16}
\]

Every repetition of the same row stays inside (S_i).  Conditional
Hanson--Wright is applied only after writing a full response contraction as

\[
 g_i^{\mathsf T}J^{(i)}g_i
 =\frac1n\operatorname{tr}J^{(i)}
  +\left(g_i^{\mathsf T}J^{(i)}g_i
        -\frac1n\operatorname{tr}J^{(i)}\right),           \tag{3.17}
\]

with the conditional regression mean added if (Z_i(0)) is fixed.  The
trace in (3.17) belongs to (3.16); it is not called a small error.  From
(3.14), the centered term is (n^{-1/2+o(1)}), uniformly on a polynomial
time net and over all single and fixed-finite deletions.  The static incident
row is likewise part of the Schur boundary operator; only its punctured
training remainder is treated perturbatively.

To bound the one-leg primitive, fix (0<\varepsilon<1) and split regular
columns by the initial set

\[
 \mathcal C=\{j:X_j(0)\le cL^\varepsilon\},
 \qquad \mathcal T=\mathcal C^c.                           \tag{3.18}
\]

In the row cavity,

\[
 V_i(t)=\int_0^t1_{\mathcal C}X(s)R^{(-i)}(s),ds
\]

is independent of (g_i=G_{i\cdot}(0)), and the no-action bound gives

\[
 \|V_i(t)\|_{2,n}^2
 \le tL^\varepsilon\int_0^t\langle X(R^{(-i)})^2\rangle_n ds
 \le CL^{\varepsilon-1}.                                  \tag{3.19}
\]

Gaussian chaining for this one-dimensional Hilbert curve and the maximum
over (n) rows therefore give

\[
 \max_i\sup_{t\le0.09/L}|g_i^{\mathsf T}V_i(t)|
 \le L^{(1+\varepsilon)/2}(\log L)^C=o(L).                 \tag{3.20}
\]

The direct primitive in (3.20) enters only the local ((A_i,Z_i)) block;
it is not multiplied by (Gamma_L).  The local Schur resolvent is uniformly
bounded by the strict row pole gap below.  Only the centered Schur remainder
sees (Gamma_L), and (n^{-1/2+o(1)}\Gamma_L=o(1)).

The fixed tail is handled by (2.11).  Initial Gaussian tails and the regular
column multiplier bound give

\[
 \sup_{t\le0.09/L}\langle X(t)^p1_{\mathcal T}\rangle_n
 \le C_pL^{p\varepsilon}e^{-cL^\varepsilon}.              \tag{3.21}
\]

Since (e^{-cL^\varepsilon}\Gamma_L=o(1)), every tail endpoint and feedback
term is (o(L)).

Together with

\[
 \langle X(t)^2\rangle_n=3+O(L^{-1/2}),\qquad
 S_i(t)=1+O(L^{-1/2}),                                     \tag{3.22}
\]

equations (2.10), (3.16), and (3.18)--(3.21) imply

\[
 Z_i(t)=Z_i(0)+14\int_0^tA_i(s)Z_i(s)\,ds+o(L),            \tag{3.23}
\]

uniformly in (i).  The coefficient error in (3.22) costs only
(O(\sqrt L)=o(L)) after integration.  The scalar comparison

\[
 \alpha_\tau=\zeta^2,\qquad \zeta_\tau=14\alpha\zeta      \tag{3.24}
\]

has, at Gaussian rate at most one, pole time greater than (0.11); hence
the local Schur resolvent in (3.16) is bounded on ([0,0.09/L]).

### 3.4 Moment and first-exit closure

All stops are simultaneous over the permitted gates.  A finite sacrificial
moment family closes them.  For example,

\[
 \int_0^t\left|\frac d{ds}\langle X^p\rangle_n\right|ds
 \le8p\left(\int_0^t\langle XR^2\rangle_n ds\right)^{1/2}
       \left(t\sup_{s\le t}\langle X^{2p-1}\rangle_n\right)^{1/2}.
                                                               \tag{3.25}
\]

The highest sacrificial moment is bounded by the regular column multiplier
stop; descending (3.25) gives (O(L^{-1/2})) changes at every needed lower
degree.  Equation (3.23) and the row gap give the row moments, Hölder gives
the (B)-moments, and (2.1) gives the weighted training bounds.  Every
threshold is therefore strictly improved at the first putative exit.
Continuity rules out an exit before (0.09/L).

We record the conclusion.

**Lemma 2 (regular susceptibility).**  On the no-action interval and with
probability tending to one, (3.14), (3.21)--(3.23), all fixed moments needed
below, and their one-row, one-column, and fixed-finite deleted versions hold
uniformly to time (0.09/L).

## 4. Exact one-tag clock

Scale the tagged variables by

\[
 x=L^2U,\qquad H=Lh,\qquad P=\rho/L,\qquad \tau=Ls.         \tag{4.1}
\]

Then (2.5)--(2.7) become

\[
 U_\tau=8U(P+HU),\qquad
 P_\tau=U\mathcal P+L^{-2}\mathcal E_0+L^2U^2\mathcal E_2. \tag{4.2}
\]

The full column Schur complement, with every repeated tag incidence kept
inside its local block, gives uniformly until (x=n^{1/3})

\[
 \mathcal P=26+\delta_{\mathcal P},\qquad
 H_\tau=3+\delta_H,                                        \tag{4.3}
\]

\[
 \|\delta_{\mathcal P}\|_{C_b^1}
 +\|\delta_H\|_{C_b^1}
 \le L^{-1/2}(\log L)^C+n^{-1/6+o(1)}.                    \tag{4.4}
\]

Here \(b=\rho(0)/L\), reset at fixed reciprocal levels, and \(C_b^1\) means
one radial score derivative of the stopped map.  The four contractions in
\(\mathcal P\) are respectively

\[
 6+o(1),\qquad6+o(1),\qquad6+o(1),\qquad8+o(1).            \tag{4.5}
\]

The last one is the trace of the full bath response, and its centered part
is controlled by (3.14) and conditional Hanson--Wright.  Likewise
\(H_\tau=3+o(1)\).  Tag self-powers are smaller by
\(x/\sqrt n\le n^{-1/6}\).

The apparently nonlocal source \(\mathcal E_0\) is an endpoint primitive.
In the exact column cavity,

\[
 \frac d{ds}\bigl[g(0)^{\mathsf T}D_{A^\circ(s)}z^\circ(s)\bigr]
 =\mathcal E_0^\circ(s).                                  \tag{4.6}
\]

The full-minus-cavity correction, including one reset radial derivative,
is (n^{-1/6+o(1)}).  Moreover

\[
 \mathcal E_2=O(n^{-1+o(1)})                               \tag{4.7}
\]

in the same stopped norm.

Put (W=U^{-1}).  The clock equation is

\[
 W_\tau=-8H-8PW.                                           \tag{4.8}
\]

On the outgoing branch \(H+PW\ge c>0\).  If \(F_P\) denotes all sources in
\(P_\tau-26U\), the correct clock norm is

\[
 \|F_P\|_{\rm clk}
 =\sup_{\sigma}\left|
 \int^{\sigma}W(t)\left(\int^tF_P(r)dr\right)dt
 \right|,                                                  \tag{4.9}
\]

together with its reset radial derivative.  Since

\[
 \int W(t)\left(\int^tU(r)dr\right)dt\le C,               \tag{4.10}
\]

(4.3)--(4.7) give

\[
 \|F_P\|_{\rm clk}+\|\partial_bF_P\|_{\rm clk}
 =o((\log L)^{-1}).                                        \tag{4.11}
\]

The endpoints in (4.6) telescope over geometric reciprocal windows.  At a
fixed reciprocal cutoff the hit is transverse, so the implicit-function
formula transfers (4.11) to the clock and its radial derivative.  Resetting
at geometric levels continues the estimate down to

\[
 W_{\rm cap}=L^2n^{-1/3}.                                  \tag{4.12}
\]

No small fixed-time tag tangent near (4.12) is asserted.

**Lemma 3 (one-tag clock).**  Let \(\Theta_j\) be the exact cap clock against
the common regular bath.  Uniformly on every compact outgoing type set,

\[
 \|\Theta_j-T_c(a_j,b_j)\|_{C^1_{\rm radial}}
 =o((\log L)^{-1}),                                        \tag{4.13}
\]

where \(a_j=X_j(0)/L^2\), \(b_j=\rho_j(0)/L\), and \(T_c\) is the pole time
of

\[
 U_\tau=8U(HU+P),\qquad H_\tau=3,\qquad P_\tau=26U.        \tag{4.14}
\]

Regular types with pole margin beyond (0.09) satisfy

\[
 C^{-1}\le X_j(s)/X_j(0)\le C,qquad s\le0.09/L.           \tag{4.15}
\]

## 5. Certified outer separation

For (4.14), set

\[
 I_c(a,b)=a/2+b^2/6,\qquad U(0)=a,\quad H(0)=0,\quad P(0)=b. \tag{5.1}
\]

The exact homogeneity is

\[
 T_c(\lambda^2a,\lambda b)=\lambda^{-1}T_c(a,b),\qquad
 I_c(\lambda^2a,\lambda b)=\lambda^2I_c(a,b).              \tag{5.2}
\]

The fixed-point program `outer_pole_certificate.c` proves

\[
 0.08389<T_*:=\inf_{I_c\le1}T_c<0.0839.                    \tag{5.3}
\]

The lower bound is global; the upper bound is supplied by
((a,b)=(335/192,7/8)).  The infimum is attained.  Every minimizer has
(a>0), and it also has (b>0): at (b=0), moving in the positive (b)
direction lowers the clock to first order, whereas the cost-preserving loss
of (a) is quadratic.

For rows, the invariant \(\zeta^2-14\alpha^2\) in (3.24) and an elementary
one-variable estimate give

\[
 \inf_{\alpha_0^2/2+\zeta_0^2/6\le1}T_r(\alpha_0,\zeta_0)
 >0.11.                                                     \tag{5.4}
\]

Finally, homogeneity implies exactly

\[
 \inf\{I_c:T_c\le T\}=(T_*/T)^2.                          \tag{5.5}
\]

## 6. Shrinking-window selection and reinsertion

Choose

\[
 h_L=(\log L)^{-1},\qquad S_L=h_LL^2,\qquad
 T_L=T_*+h_L.                                               \tag{6.1}
\]

Let \(a_0>0\) be smaller than the minimum \(a\)-coordinate of all rate-one
types with clock at most (0.09), and form the common parent set

\[
 \mathscr P=\{j:X_j(0)\ge a_0L^2\}.                        \tag{6.2}
\]

It is (X(0))-measurable.  Delete all of (mathscr P), evolve the common
bath, and insert one parent column at a time.  Conditional on the bath, the
initial columns are independent.  Decomposing

\[
 g_j=\frac{Lb_j}{\|B^\circ(0)\|_2^2}B^\circ(0)+g_j^\perp  \tag{6.3}
\]

shows that the moderate-deviation rate is (5.1).  Lemma 3 and coarea give,
uniformly for clocks at most (T_L+o(h_L)), a conditional density with
two-sided logarithmic distortion (o(S_L)).

Let

\[
 E_L=\{j\in\mathscr P:\Theta_j\le T_L\}.                   \tag{6.4}
\]

From (5.5), conditional first and second moment estimates give

\[
 1\le |E_L|\le\exp(CS_L)                                   \tag{6.5}
\]

with probability tending to one.  For the lower bound, radially scale an
attained minimizer so that its clock is (T_*+h_L/4); its cost is
(1-c h_L+O(h_L^2)), and a shrinking open mark cell contains
(exp(cS_L+o(S_L))) columns.

Fix (D>2C) and put

\[
 \Delta_L=\exp(-DS_L)=n^{-d_L},\qquad d_L=D/\log L\to0.     \tag{6.6}
\]

The two-tag coarea formula yields the factorial intensity estimate

\[
 \mathbb E\sum_{j\ne k\in E_L}
 1_{\{|\Theta_j-\Theta_k|\le3\Delta_L\}}
 \le\exp\{(2C-D+o(1))S_L\}=o(1).                           \tag{6.7}
\]

Thus the earliest cavity cap is separated by (3\Delta_L).

It remains to restore the network.  This does not require a global Taylor
expansion through the singular tag coordinates.  Let (q_0) be the common
bath and (d_j) the exact one-tag increment.  For
(Q=q_0+\sum_{j\in E_L}d_j), define

\[
 \mathcal M=F(Q)-F(q_0)-\sum_j\{F(q_0+d_j)-F(q_0)\},        \tag{6.8}
\]

and the lifted homotopy

\[
 q_0'=F(q_0)+\lambda\mathcal M,\qquad
 d_j'=F(q_0+d_j)-F(q_0),\qquad0\le\lambda\le1.             \tag{6.9}
\]

At \(\lambda=0\) this is the common bath plus independent exact one-tag
systems; at \(\lambda=1\), their sum solves the full ODE.  Every same-tag
singular chain remains inside its exact Green block.  Expanding the finite
polynomial (F), every term in (mathcal M) contains two distinct tag
increments or an explicit (1/n) trained/empirical contraction.  In the
reciprocal Green forcing norm,

\[
 \|\mathcal M\|_{L^1_G}\le |E_L|^2n^{-1/3+o(1)},\qquad
 \|D\mathcal M\|_{L^1_G}\le |E_L|n^{-1/6+o(1)}.          \tag{6.10}
\]

The worst off-diagonal term illustrates the bound.  With
(K_{jk}=\sum_iA_iG_{ij}G_{ik}=n^{-1/2+o(1)}),

\[
 \int|K_{jk}X_k|ds
 \le n^{-1/2+o(1)}\int X_kds
 \le n^{-1/3+o(1)}.                                       \tag{6.11}
\]

Coincident Wick bubbles retain their (1/n); for example
((X_j/n)\int X_k^2ds=Ln^{-1/3+o(1)}).  Equations
(6.8)--(6.11), Lemma 2, and variation in (lambda) give

\[
 \max_{j\in E_L}
 \|\Theta_j^{\rm full}-\Theta_j\|_{C^1}
 \le n^{-1/3+o(1)}=o(\Delta_L).                            \tag{6.12}
\]

The noncandidate part of (mathscr P) has normalized Gaussian tail mass
(n^{-c(a_0)+o(1)}).  Until the first cap its one-tag clocks have a gap at
least (h_L/3), hence its multiplier is only polylogarithmic; the same
susceptibility argument makes its aggregate effect
(n^{-c(a_0)+o(1)}=o(\Delta_L)).

Consequently, with probability tending to one, the first full cap is unique
and occurs by ((T_*+2h_L)/L).  At that time, for its index (e),

\[
 X_e=n^{1/3},\qquad
 \max_{k\ne e}X_k\le n^{d_L+o(1)},                         \tag{6.13}
\]

\[
 h_e\ge c/L,qquad
 \Psi_e:=\rho_e+h_eX_e/2\ge cX_e/L.                       \tag{6.14}
\]

The last line follows from the outgoing formal branch:
(H\to3T_*>0) and (P/U\to0) at its pole, together with Lemma 3 and
(6.12).

## 7. From the first cap to fixed output action

Let \(s_0\) be the cap time, write \(j=e,x=X_j,g=G_{\cdot j}\), and stop at
fixed action or at

\[
 x=C\sqrt{nL}.                                              \tag{7.1}
\]

Bootstrap \(h\ge c/(2L)\) and \(\Psi\ge0\).  Then

\[
 x'=8xR_j\ge cx^2/L.                                       \tag{7.2}
\]

Thus, up to (7.1),

\[
 \int ds\le n^{-1/3+o(1)},\qquad
 \int x\,ds=n^{o(1)},\qquad
 \int x^2ds\le n^{1/2+o(1)}.                              \tag{7.3}
\]

All norms in the rest of this section are unnormalised.  The exact
tag-deleted equations are

\[
\begin{aligned}
g-g_0&=\frac2n\int xA(xg+z)ds,\\
g_k-g_{k0}&=\frac2n\int X_kA(xg+z)ds,\\
z-z_0&=\int(2Q_-I+8H_-)A(xg+z)ds,\\
A-A_0&=\int(xg+z)^{\odot2}ds.
\end{aligned}                                               \tag{7.4}
\]

Since \(d_L=o(1)\), (6.13), (7.3), fixed moments at \(s_0\), and (7.4)
give

\[
 \|z-z_0\|_2\le n^{1/6+o(1)},\qquad
 \|z-z_0\|_\infty\le n^{1/6+o(1)},                       \tag{7.5}
\]

\[
 \|A-A_0\|_4=n^{o(1)},\quad
 \|A-A_0\|_\infty=n^{o(1)},\quad
 \langle A^4\rangle_n=n^{o(1)},                           \tag{7.6}
\]

\[
 \|g-g_0\|_2\le n^{-1/2+o(1)},\qquad
 \|G-G_0\|_{\rm op}\le n^{-1/3+o(1)}.                   \tag{7.7}
\]

For \(k\ne j\), write

\[
 R_k=x\,g_k^{\mathsf T}D_Ag+g_k^{\mathsf T}D_Az.
\]

One-column-deleted fixed moments and (7.5)--(7.7) give

\[
 |g_k^{\mathsf T}D_Ag|\le n^{-1/3+o(1)},\qquad
 |g_k^{\mathsf T}D_Az|\le n^{1/6+o(1)}.                  \tag{7.8}
\]

Using (7.3) in ((\log X_k)'=8R_k) shows

\[
 \max_{k\ne j}X_k(s)\le n^{d_L+o(1)}                     \tag{7.9}
\]

throughout the release.  Hence all estimates improve their bootstrap.

From (2.7), (7.5)--(7.9), and
\(\|H_-\|\le n^{d_L+o(1)}\),

\[
 |\mathcal E_0|\le n^{1/2+o(1)},\qquad
 |\mathcal E_2|\le n^{-1/2+o(1)}.                         \tag{7.10}
\]

At a hypothetical first zero of \(\Psi\), \(R_j=hx/2\).  Equations
(2.6)--(2.8) then give

\[
 \Psi'\ge2h^2x^2
 -n^{1/2+o(1)}-x^2n^{-1/2+o(1)}-2x^3n^{-1+o(1)}>0,         \tag{7.11}
\]

uniformly for \(n^{1/3}\le x\le C\sqrt{nL}\).  Moreover

\[
 \int(h')_-ds
 \le \frac4n\langle A^4\rangle_n\int x^2ds=o(L^{-1}).   \tag{7.12}
\]

Thus \(h\ge c/(2L)\), \(\Psi\) cannot cross zero, and

\[
 R_j\ge cx/L.                                              \tag{7.13}
\]

If the action stop has not occurred first, (7.1) is reached in additional
outer time (O(L^2n^{-1/3})=o(1)).  Finally,

\[
 (x^2)'=16x^2R_j,\qquad K_n\ge\frac{16}{n}xR_j^2,
\]

so along the actual trajectory

\[
 \frac{df_n}{d(x^2)}=\frac{K_n}{(x^2)'}
 \ge\frac{R_j}{nx}\ge\frac c{nL}.                         \tag{7.14}
\]

Choosing \(C\) sufficiently large in (7.1) yields a deterministic
\(\delta_0>0\) such that

\[
 f_n(s_1)-f_n(s_0)\ge\delta_0.                             \tag{7.15}
\]

Together with the action-stop alternative, this proves (1.4).

## 8. Physical time and the frozen contract

At initialization, \(f_n(0)\to0\) in probability.  Before the
\(\delta_0\)-hit, \(y_\star-f_n\ge y_\star/2\) with probability tending to
one.  Hence the physical hitting time is bounded by

\[
 \int_0^{s_1}\frac{ds}{2\eta(y_\star-f_n(s))}
 \le\frac{s_1}{\eta_0y_\star}\xrightarrow{\mathbb P}0.   \tag{8.1}
\]

Suppose the frozen contract held.  Then on a fixed physical interval,
\(f_n\) would converge uniformly in probability to a continuous \(f\) with
\(f(0)=0\).  At the random hitting times \(t_{1,n}\to0\), however,

\[
 f_n(t_{1,n})-f_n(0)\ge\delta_0.
\]

Therefore

\[
 \delta_0
 \le2\|f_n-f\|_\infty+\omega_f(t_{1,n})
 \xrightarrow{\mathbb P}0,                                \tag{8.2}
\]

a contradiction.  The argument is topology independent once the frozen
contract requires a continuous real-valued output readout and compact-time
uniform finite-width identification.  It therefore rules out the proposed
finite-field operator IDE as well as any other autonomous current-state
packaging satisfying that contract.  \(\square\)

## 9. Reproducibility and scope

The only computer-assisted statement is (5.3), certified by outward-rounded
integer arithmetic in `outer_pole_certificate.c`; its adjacent SHA256 file
fixes the source.  The row bound (5.4) is analytic.

Two-time response kernels occur only inside finite-width proof estimates;
they are not proposed state variables.  Pure repeated row/column returns are
resummed exactly before Gaussian centering.  The susceptibility theorem is
restricted to fixed-finite row gates and contractive column masks; arbitrary
data-dependent bulk row selection would invalidate the signed Hessian bound
and is neither used nor needed.

The theorem is stated for a fixed positive label.  This is already enough to
disprove the universal frozen contract for the canonical initialization and
training rule.  A negative-label statement requires the separate
time-reversed concentration analysis and is not claimed here.
