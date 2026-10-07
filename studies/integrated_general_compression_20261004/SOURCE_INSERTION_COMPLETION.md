# Completion of the local insertion and finite training-source proof

2026-10-07. Author integration fragment. This file is not an independent
review. Its intended destinations are the subsection `source-local-insertion`
(replace its proof), the derivation immediately preceding (S.15) (insert
the trace identities below), and `The finite source event` in the Logarithmic
decoder proof (replace that subsection). The source definitions (S.1)--(S.14)
and (S.17)--(S.32) remain the definitions used here. Formula labels beginning
IC are new, unique labels for this fragment. References to S and to the
explicit dense-fitting theorem refer to the existing RESULT, not to an
external research file.

The first conclusion has fixed deletion count and the original complex
query tube; its width onset is qualitative. The second conclusion concerns
only the finitely many training queries and has the explicit power-1100
width gate. These scopes must not be interchanged. Throughout, retain the
complete common label allowance, including (S.10). No restriction depending
on a deletion count or on a confidence is added to that allowance.

## 1. Coordinates and the exact retained equation

Write \(\ell=\log(en)\), \(\lambda=\gamma/m\), and
\(S=16Y/\lambda\). For \(Y=0\), the readout and all parameter
velocities vanish and the predictor is zero; the argument with barred
variables below is only for \(Y>0\). Use Euclidean/Frobenius norm on
the direct sum of the mobility coordinates
\[
 \Theta=(A,H^{(2)},\ldots,H^{(L)},w),\qquad H^{(j)}=\sqrt nW^{(j)}.
\]
Here \(H^{(j)}\) is a rescaled matrix; the scalar RMS bound remains
\(H_j\). Write \(v_a=x_a/\sqrt d\) for a normalized training
input and \(F_a=n f(t,x_a)=w^\top h_a^{(L)}\) for its unnormalized
prediction. Delete activations in one layer, keeping normalization \(n\)
in every rectangular matrix. For a deleted interior neuron \(i\), its
initialized incoming row transpose \(y_i\) and outgoing column \(x_i\)
have law \(N(0,I/n)\) and are independent of the entire retained
initialization and of the other omitted root pairs. At the first layer
only \(x_i\) enters the retained forcing; the initialized incoming
row has law \(N(0,I_d)\) and is used separately to evaluate its own
preactivation. At the top there is no \(x_i\).

Add forward ports \(e_a^{(j)}\) to preactivations and set
\[
 \bar u=(\Theta-\Theta_0)/S,\quad
 \bar F_a=F_a(\Theta_0+S\bar u,e_a)/S,
 \quad\bar r_a=\bar F_a/n-y_a/S,\quad
 \bar k=k/S,\quad\bar\delta=\delta/S.
 \tag{IC.1}
\]
Zero initial readout gives \(\bar F_a=\bar u_w^\top h_a^{(L)}\).
The scaled backward recursion and gradient blocks are
\[
 \bar k_a^{(L)}=\bar u_w,\quad
 \bar\delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot\bar k_a^{(j)},\quad
 \bar k_a^{(j)}=W^{(j+1)\top}\bar\delta_a^{(j+1)},
\]
\[
 \nabla_{\bar u_A}\bar F_a=S\bar\delta_a^{(1)}v_a^\top,
 \quad\nabla_{\bar u_{H^{(j)}}}\bar F_a
 ={S\over\sqrt n}\bar\delta_a^{(j)}h_a^{(j-1)\top},
 \quad\nabla_{\bar u_w}\bar F_a=h_a^{(L)}.
 \tag{IC.2}
\]
For deletion at layer \(j\), the actual ports are
\[
 e_a=\sum_{i\in I}W^{(j+1)}_{:,i}h_{a,i}^{(j)},\qquad
 \bar q_a=\sum_{i\in I}W^{(j)\top}_{i,:}\bar\delta_{a,i}^{(j)}.
\]
Differentiating through the deleted activation accounts for exactly the
second summand in the following equation:
\[
 \dot{\bar u}=-{2\over m}\sum_a\bar r_a
 \left[\nabla_{\bar u}\bar F_a+
       D_{\bar u}h_a^{(j-1)\top}\bar q_a\right].
 \tag{IC.3}
\]
In particular \(D_{\bar u}h=S D_\Theta h\). The reverse source
does not enter the forward residual. At the top the additional scalar
\(\bar d_a=n^{-1}\sum_{i\in I}\bar u_{w,i}h_{a,i}^{(L)}\)
is added to \(\bar r_a\) and multiplies both terms in the bracket.

Each reference is the zero-source cavity with its own initialization
test, real stopping time and complex stopping domain. Failed own
initializations give identically zero coefficient paths. This convention
is fixed before any omitted root is integrated. On a successful stopped
reference, the physical RMS bounds are (S.5)--(S.6), its budgets are
at most \(2\mathcal B\), its operator caps are ten, and
\[
 2\int\bar\rho\,|dt|\le1,\quad
 \bar\rho=\big(m^{-1}\sum_a|\bar r_a|^2\big)^{1/2},\quad
 \bar\rho\le\lambda/8,\quad
 M_n=\eta^{-1}\log(2n\mathcal B).
 \tag{IC.4}
\]
For the original qualitative source, the short-contour conditions in
(S.31) give (IC.4). For the quantitative training source, they will be
proved directly in Section 7 at a smaller radius.

The independent complex stops and their extensions are defined as follows.
For a fixed target rectangle
\(K=[-r_t,T+r_t]+i[-r_t,r_t]\), use the nested closed convex
rectangles \(K_s=sK\), \(0\le s\le1\). Each cavity starts
from its own initial germ and has its own first-exit level \(s_c\):
all its running budgets, maxima, pole and response stops are suprema on
\(K_s\). In the qualitative passive-query construction, take those
suprema on \(K_s\) times the intrinsic query tube of thickness
\(s r_q\), retaining the full real sphere at every level. Thus
the first level has only real initial queries. This is the same target
domain and the same stops at \(s=1\), with a precise nested-prefix
convention. The real fitting trajectory is already defined independently
for all positive time. Before a stop, finite-width parameter bounds and
the strict separation from the activation singularities permit local
holomorphic ODE continuation. Compactness and uniqueness glue these
extensions. At a first stopped level the coefficients have continuous
values on its closed rectangle; the activation strip still has strict
slack, so the same local continuation justifies the one-sided derivative
bounds there. A failed own initialization is treated separately by the
identically zero convention.

Let \(P_c\) be Euclidean projection onto the fixed rectangle
\(K_{s_c}\), explicitly clamping its real and imaginary coordinates
to the two closed intervals. It is 1-Lipschitz, fixes this rectangle,
and is measurable in that cavity's retained initialization only. Extend
each of its coefficient paths \(b_c\) to the whole target rectangle
by \(\widetilde b_c(z)=b_c(P_cz)\). A derivative bound on the
convex rectangle gives the corresponding Lipschitz bound by integration
on a segment, and composition with \(P_c\) preserves that bound.
For passive-query grids also clamp the intrinsic imaginary-circle
coordinate to \([-s_cr_q,s_cr_q]\); the real frame ranges over
the full frame manifold. These extensions need not be holomorphic outside
their own stopped domains. Holomorphic identities are used only on the
common successful prefix, where the projections are identity.

In particular define the real-anchor map
\(a(z)=\min\{T,\max\{0,\operatorname{Re}z\}\}\).
The correct complex-minus-real coefficient is
\[
 b_c(P_cz)-b_c(P_ca(z))
       =b_c(P_cz)-b_c(a(P_cz)).
 \tag{IC.stop}
\]
The two projections commute because both real intervals contain zero
and the anchor interval is \([0,T]\). Both arguments lie in
\(K_{s_c}\), their distance is at most \(|z-a(z)|\le2r_t\),
and both argument maps are 1-Lipschitz. Thus the small-radius and
global modulus bounds for this difference follow from the derivative
bounds on the closed stopped rectangle. Its real anchors trace a
monotone interval from zero to \(\min\{s_c(T+r_t),T\}\),
then freeze. The original real activity modulus and moment proof therefore
apply to that real coefficient path. For two different cavities, extend
each with its own projection before subtracting; the sum of their
Lipschitz constants bounds the difference. On a successful full prefix,
strict cavity-stop transfer proves \(s_c\) is at least its level,
so these extended paths equal the actual paths there. This construction
supplies the globally defined coefficient processes used in all later
conditional Gaussian integrals.

## 2. Derivative maps, control moduli, and terminal interpolation

We give recurrences rather than a dimension-dependent estimate for the
parameter Hessian. In augmented mobility/port coordinates put
\(Z_a^{(j)}U=D z_a^{(j)}[U]\). Then
\[
 Z_a^{(1)}U=U_Av_a+U_{e^{(1)}},\quad
 Z_a^{(j)}U={U_{H^{(j)}}\over\sqrt n}h_a^{(j-1)}
       +W^{(j)}\operatorname{diag}(\phi_{j-1}')Z_a^{(j-1)}U
       +U_{e^{(j)}}.
 \tag{IC.5}
\]
The coefficients \(P_j,f_j\) in (S.6) bound these maps and their
activated versions. The exact Hessian is
\[
\begin{aligned}
 D^2F_a[U,V]={}&U_w^\top\operatorname{diag}(\phi_L')Z_a^{(L)}V
 +V_w^\top\operatorname{diag}(\phi_L')Z_a^{(L)}U\\
 &+\sum_j(Z_a^{(j)}U)^\top
       \operatorname{diag}(k_a^{(j)}\phi_j'')Z_a^{(j)}V\\
 &+\sum_{j\ge2}{\delta_a^{(j)\top}\over\sqrt n}
 \{U_{H^{(j)}}\operatorname{diag}(\phi_{j-1}')Z_a^{(j-1)}V
  +V_{H^{(j)}}\operatorname{diag}(\phi_{j-1}')Z_a^{(j-1)}U\}.
\end{aligned}\tag{IC.6}
\]
Each cross term factors through a hidden space of dimension at most \(n\).
Each curvature term has exactly one carrier diagonal. Schatten ideal
inequalities applied to these displayed factors give (S.13); the port
identity \(\partial_{e_a^{(j)}}F_a=\delta_a^{(j)}\) proves the
same bounds for both endpoint blocks \(D_\Theta\delta\).

The zero-source variational generator is
\[
 \mathscr L=-{2\over mn}\sum_a g_ag_a^\top
             -{2\over m}\sum_a r_a D^2_\Theta F_a,
 \qquad g_a=\nabla_\Theta F_a.
 \tag{IC.7}
\]
Its first summand contracts along forward real time. Along disjoint
short nonreal/backward pieces its accumulated norm cost is at most two.
By (S.13) and (IC.4), its propagator \(J(t,s)\) therefore satisfies
\[
 \|J(t,s)\|\le
 2e^{SA_*+(S^2D_*/\eta)\log(2n\mathcal B)}
 \le J_0n^\kappa,
 \quad J_0=2e^{1/4}(2\mathcal B)^{1/4000},\quad\kappa=1/4000.
 \tag{IC.8}
\]
The coefficient of \(\log n\) is bounded using the unchanged
label condition, before any width is enlarged.

For deterministic scalar controls \(a_{a,i},b_{a,i}\), put
\(e_a=\sum_i x_i a_{a,i}\), \(\bar q_a=\sum_i y_i b_{a,i}\).
The three derivative maps from these ports to (IC.3), at zero ports,
are exactly
\[
 -{2\over mn}\nabla_{\bar u}\bar F_a\bar\delta_a^{(j+1)\top},
 \qquad-{2\over m}\bar r_a(D_{\bar u}\bar\delta_a^{(j+1)})^\top,
 \qquad-{2\over m}\bar r_a(D_{\bar u}h_a^{(j-1)})^\top.
 \tag{IC.9}
\]
The first is required because the residual depends on the forward port.
Let \(\Gamma=\sqrt{\mathcal K}\), \(\tau_*=\max\tau_j\),
\(f_*=\max f_j\), and take a contour length at most
\(T_*\ell\), where \(T_*=32/\lambda+2c\) if its half-width
is \(c/\sqrt\ell\). Define
\[
\begin{gathered}
 M_0=\eta^{-1}[1+\log(2\mathcal B)],\quad
 A_0=b+sM_0,\quad B_0=sM_0,\quad E_0=A_*+SD_*M_0,\\
 v_0=J_0\{A_0(2T_*\Gamma\tau_*+E_0)+Sf_*B_0\},\\
 z_j^0=P_j(Sv_0+A_0),\quad h_j^0=sz_j^0,\quad
 k_L^0=v_0,\\
 d_j^0=sk_j^0+t_2M_0z_j^0,\qquad
 k_j^0=10d_{j+1}^0+S\tau_{j+1}v_0+B_0\quad(j<L).
\end{gathered}\tag{IC.10}
\]
As maps from the concatenation \(g\) of the omitted roots,
the mobility, preactivation and feature variations have norms at most
\(\sqrt p n^\kappa\ell^2(v_0,z_j^0,h_j^0)\);
the scaled carrier/response variations have norms at most
\(\sqrt p n^\kappa\ell^3(k_j^0,d_j^0)\).
Indeed integrate (IC.9), using \(\|g_a\|\le\sqrt n\Gamma\),
\(\|\bar\delta_a\|\le\sqrt n\tau_*\),
\(\|D_{\bar u}\bar\delta_a\|\le A_*+SD_*M_n\),
\(\|D_{\bar u}h_a\|\le Sf_*\), and (IC.4).
Cauchy--Schwarz over roots gives \(\sqrt p\). The subsequent
forward/backward differentiation is, explicitly,
\[
\begin{aligned}
 z_{[1]}^{(j)}&={S V_{H^{(j)}}\over\sqrt n}h^{(j-1)}
                  +W^{(j)}h_{[1]}^{(j-1)}+e_{[1]}^{(j)},\\
 h_{[1]}^{(j)}&=\phi'_j\odot z_{[1]}^{(j)},\\
 \bar k_{[1]}^{(j)}&=W^{(j+1)\top}\bar\delta_{[1]}^{(j+1)}
       +{S V_{H^{(j+1)}}^\top\over\sqrt n}\bar\delta^{(j+1)}
       +\bar q_{[1]}^{(j)},\\
 \bar\delta_{[1]}^{(j)}&=\phi'_j\odot\bar k_{[1]}^{(j)}
                    +\phi_j''\odot\bar k^{(j)}\odot z_{[1]}^{(j)}.
\end{aligned}\tag{IC.11}
\]
Only one forward and one reverse port is present in an actual deletion;
allowing a port at every layer only enlarges these bounds. A logarithm
is introduced by the reference carrier once, in the inhomogeneous last
term, and is propagated by \(10s\), not by a carrier maximum.

For a control difference of supremum norm \(\epsilon\), replace
\(A_0,B_0\) by one in the forcing coefficients of (IC.10), retaining
\(M_0,E_0,J_0\). Explicitly set
\[
 v_c=J_0(2T_*\Gamma\tau_*+E_0+Sf_*),\quad
 z_j^c=P_j(Sv_c+1),\quad h_j^c=sz_j^c,
\]
\[
 k_L^c=v_c,\quad d_j^c=sk_j^c+t_2M_0z_j^c,
 \quad k_j^c=10d_{j+1}^c+S\tau_{j+1}v_c+1,
 \quad C_c=\max(v_c,z_j^c,h_j^c,k_j^c,d_j^c).
 \tag{IC.12}
\]
Linearity of the variational equation in its controls proves
\(\|\Delta L\|\le C_c\sqrt p n^\kappa\ell^2\epsilon\)
for every map just listed.
Indeed the difference forcing has amplitude \(\epsilon\), rather
than \(A_0\ell\) or \(B_0\ell\). Its mobility integral has
only one factor \(\ell\), from the horizon or the reference Hessian
bound. Forward differences retain that one factor. The backward gate
multiplies by \(M_0\ell\) once, giving \(\ell^2\). This is
why the control modulus has one fewer logarithm than the amplitude bound.

All quadratic matrices and their moduli are now explicit. If \(E_i\)
selects one root block and \(L\) maps roots to a lower feature or
upper response variation, its pairing is
\[
 (E_ig)^\top Lg=g^\top R_i g,\qquad
 R_i={1\over2}(E_i^\top L+L^\top E_i).
 \tag{IC.13}
\]
Thus \(\|R_i\|\le\|L\|\) and
\(\|\Delta R_i\|\le\|\Delta L\|\). Only the selected
diagonal root block contributes to \(\operatorname{tr}R_i/n\).
In particular an incoming/outgoing cross block is centered. On
\(\|g\|\le2\sqrt{2p}\), centered-form interpolation costs
\[
 |\Delta(g^\top Rg-\operatorname{tr}R/n)|
 \le10p\|\Delta R\|.
 \tag{IC.14}
\]
The trace term has been included; it costs at most
\(2p\|\Delta R\|\).

Here are terminal-time moduli, including the normalization needed for
off-grid interpolation. Define
\[
 T_L^0=2sH_L+2t_2M_0V_L,\quad
 T_j^0=10sT_{j+1}^0+2s\tau_{j+1}^2H_j+2t_2M_0V_j,
\]
\[
 D_c=\max\{\lambda s\max_jV_j/4,\lambda\max_jT_j^0/8\},
\]
\[
 a_j^z=\lambda S^2V_j/4,\quad a_j^h=sa_j^z,\quad
 a_j^W=\lambda S^2\tau_jH_{j-1}/4,
 \quad a_j^\delta=\lambda T_j^0/8,
\]
\[
 a_L^k=\lambda H_L/4,\quad
 a_j^k=a_{j+1}^W\tau_{j+1}+10a_{j+1}^\delta,
 \quad A_t=2\mathcal K+(\lambda/4)SE_0,
\]
\[
 v_t=A_tv_0+A_0(2\Gamma\tau_*+\lambda E_0/4)
                              +(\lambda/4)Sf_*B_0.
 \tag{IC.15}
\]
Raw scalar control speeds are bounded by \(D_c\sqrt n\ell\).
The reference RMS speeds are bounded by \(a_j^z,a_j^h,a_j^W\)
and \(\ell a_j^\delta,\ell a_j^k\). Differentiating (IC.11)
gives the following coefficient recurrences:
\[
\begin{gathered}
 z_1^t=Sv_t+D_c,\quad h_1^t=sz_1^t+t_2a_1^zz_1^0,\\
 z_j^t=S(H_{j-1}v_t+a_{j-1}^hv_0)
       +a_j^Wh_{j-1}^0+10h_{j-1}^t+D_c,\quad
 h_j^t=sz_j^t+t_2a_j^zz_j^0,\\
 k_L^t=v_t,\quad
 k_j^t=a_{j+1}^Wd_{j+1}^0+10d_{j+1}^t
            +S\tau_{j+1}v_t+Sa_{j+1}^\delta v_0+D_c,\\
 d_j^t=sk_j^t+t_2a_j^zk_j^0
       +(t_3M_0a_j^z+t_2a_j^k)z_j^0+t_2M_0z_j^t,
 \qquad t_3=16\beta/a\le\beta^2.
\end{gathered}\tag{IC.16}
\]
Forward derivatives have bound \(\sqrt{pn}n^\kappa\ell^3\)
times their coefficients; backward ones have
\(\sqrt{pn}n^\kappa\ell^4\) times theirs. The factor
\(\sqrt n\) comes from a reference coordinate speed and appears
once. The homogeneous propagated derivative still costs \(10s\).
For the control-independent lower probes, differentiate (IC.5):
\[
 z_1^J=0,\quad h_1^J=t_2a_1^zP_1,\quad
 z_j^J=a_{j-1}^h+a_j^Wf_{j-1}+10h_{j-1}^J,\quad
 h_j^J=sz_j^J+t_2a_j^zP_j.
 \tag{IC.17}
\]
Restriction to a lower port and transposition give the raw adjoint probes
used below. Their operator time derivatives are bounded by
\(\sqrt n\max(z_j^J,h_j^J)\).

Let \(C_t\) be the maximum of all coefficients in (IC.16)--(IC.17)
and \(v_t\). A terminal mesh of size
\[
 h_t\le\min\left\{1,
 {n^{-1/10-1/2-\kappa}\over80p^{3/2}(1+C_t)\ell^4}\right\}
 \tag{IC.18}
\]
makes both the linear and centered-quadratic off-grid errors less than
\(n^{-1/10}/4\), using (IC.14). A rectangle of real length
\(32\ell/\lambda+2r_t\) and height \(2r_t\) has at most
\([2+(32\ell/\lambda+2r_t)/h_t][2+2r_t/h_t]\) grid points.
On complex rectangles these derivative identities apply to analytic
actual controls. At grid points the Gaussian union uses deterministic
one-dimensional control histories along the prescribed contour. Actual
analytic controls are substituted only after that uniform event. No
path independence is asserted for arbitrary two-dimensional controls.

## 3. Exact nonlinear remainder and reverse probes

Here is a deterministic local lemma that specifies every term used in
the first-exit argument. Write the augmented displacement as
\(\eta_a=(V,e_a)+(U,0)\), with
\[
 \|V\|,\|e_a\|,\|Dg_0(V,e_a)\|_2\le N,
 \quad\|Dg_0(V,e_a)\|_\infty\le d_0,\quad\|U\|\le u,
 \tag{IC.19}
\]
where the bound on the combined augmented norm may be obtained by
enlarging \(N\) by a fixed factor. The quantities \(g\) here
are all forward vectors and scaled backward vectors in (IC.11).
Assume \(N\ge1\), \(u,d_0\le1\), \(N+u\le\sqrt n\),
and put
\[
 R=d_0N+d_0u+u^2,\quad P=(N+u)^2/\sqrt n,
 \qquad u+R+P\le1.
 \tag{IC.20}
\]
With reference scaled carrier maximum \(M\), define
\(g_{[1]}=Dg_0\eta\) and \(E_g=g_1-g_0-g_{[1]}\).
Feature RMS, first forward derivative, and first backward derivative
bounds on the joining segment/reference are, respectively,
\(\beta^{3L}\), \(J_f=\beta^{10L}\), and
\(J_b=\beta^{20L}(1+M)\). To verify the latter two, use
(IC.5), then the backward derivative in (IC.11): its forcing is a
single reference carrier times the forward derivative, and its
homogeneous propagation is \(10s\). Along a unit segment, physical
operators are at most eleven and ports at most \(\sqrt n\);
the affine feature recurrence is bounded by \((13\beta)^L\).

The localized product bound is
\[
 \|z_{[1]}\odot z_{[1]}\|_2
 \le d_0N+2d_0J_fu+J_f^2u^2\le3J_f^2R.
 \tag{IC.21}
\]
The following identities are exact, so their use does not assume a
bound on an uncontrolled changed carrier:
\[
 E_{z^{(1)}}=0,\quad
 E_{z^{(j)}}=W_1^{(j)}E_{h^{(j-1)}}
        +{S\Delta\bar u_{H^{(j)}}\over\sqrt n}h_{[1]}^{(j-1)},
 \tag{IC.22}
\]
\[
 E_{\bar k^{(L)}}=0,\quad
 E_{\bar k^{(j)}}=W_1^{(j+1)\top}E_{\bar\delta^{(j+1)}}
   +{S\Delta\bar u_{H^{(j+1)}}^\top\over\sqrt n}
                  \bar\delta_{[1]}^{(j+1)},
 \tag{IC.23}
\]
\[
 E_{\bar\delta}=g_1\odot E_{\bar k}
 +(g_1-g_0)\odot\bar k_{[1]}
 +\bar k_0\odot[g_1-g_0-\phi''(z_0)z_{[1]}],
 \qquad g_i=\phi'(z_i).
 \tag{IC.24}
\]
For activation subtraction insert \(z_0+z_{[1]}\); this gives
\(\|E_h\|\le\beta\|E_z\|+
 (\beta/2)\|z_{[1]}^{\odot2}\|\).
The cross term in (IC.22) is at most \(J_fP\). Summing its
geometric propagation gives
\[
 \max_j(\|E_z\|,\|E_h\|)\le\beta^{30L}(R+P).
 \tag{IC.25}
\]
In (IC.24), the second term is bounded by
\[
 \beta\{3J_fJ_bR+\beta^{30L}(R+P)(d_0+J_bu)\};
\]
the last is at most
\(M[\beta\|E_z\|+(\beta^2/2)
\|z_{[1]}^{\odot2}\|]\). The matrix cross term in (IC.23)
is at most \(J_bP\). Homogeneous propagation uses only the
perturbed mixer and slope, so
\[
 \max_j(\|E_{\bar k}\|,\|E_{\bar\delta}\|)
 \le\beta^{60L}(1+M)(R+P).
 \tag{IC.26}
\]
For a hidden gradient block its exact product remainder is
\[
 {S\over\sqrt n}
 [E_{\bar\delta}h_1^\top+
   \bar\delta_{[1]}(h_1-h_0)^\top+\bar\delta_0E_h^\top].
 \tag{IC.27}
\]
Use reference feature/response RMS in its first and last terms and
\(J_fJ_bP\) in its middle term. The first-layer and readout
blocks give the gradient remainder bound
\(\beta^{70L}(1+M)(R+P)\).

Applying (IC.26) to each initial part of the joining segment proves
a carrier cap \(\beta^{62L}(1+M)\) on that segment. Hence
(IC.6) gives an augmented Hessian bound \(\beta^{87L}(1+M)\),
and \(\|D\bar F\|\le\beta^{13L}\sqrt n\). Thus
\[
 |\Delta\bar r|\le\beta^{13L}(N+u)/\sqrt n,\quad
 |\Delta\bar r-D\bar r_0\eta|
 \le\tfrac12\beta^{87L}(1+M)(N+u)^2/n.
 \tag{IC.28}
\]
The constant labels \(y_a/S\) cancel from both differences.
For \(g=\nabla\bar F\), the product remainder is exactly
\[
 \bar r_0E_g+
 (\Delta\bar r-D\bar r_0\eta)g_0+
 \Delta\bar r\,(g_1-g_0).
 \tag{IC.29}
\]
Its last two terms cost \(2\beta^{100L}(1+M)P\).

For the reverse force, fix an omitted incoming root \(y_i\) and
write \(\psi_i=y_i^\top h_a^{(j-1)}\). Include in the Gaussian
event all its lower adjoint carriers. Their Euclidean norms are bounded
by the forward operator recurrences and their coordinate maxima by
\(d_0\). For an aggregate \(q=\sum_i y_ib_{a,i}\) with
\(\|y_i\|\le2\), \(|b_{a,i}|\le\beta M\), put
\(Q=2p\beta M\) and \(P_q=p\beta Md_0\).
Subtracting the probe adjoint recursion along a parameter segment gives
\[
 \max_j\|k_{q,t}^{(j)}-k_{q,0}^{(j)}\|_2
 \le\beta^{20L}(P_q+Q/\sqrt n)(N+u).
 \tag{IC.30}
\]
The changed gate multiplies the reference probe maximum \(P_q\);
the changed mixer costs \(Q(N+u)/\sqrt n\); the propagated
difference costs \(11s\). These are all three terms in the
recursion. Apply (IC.6) to the scalar lower-network output \(\psi_q\)
and integrate its Hessian to obtain
\[
 \|(Dh_1-Dh_0)^\top q\|
 \le\beta^{50L}(P_q+Q/\sqrt n)
                 [N+u+(N+u)^2].
 \tag{IC.31}
\]
The exact extra nonlinear terms in (IC.3) are
\(\bar r_0(Dh_1-Dh_0)^\top\bar q\) and
\(\Delta\bar r\,Dh_1^\top\bar q\). Equations (IC.28),
(IC.31) bound both. Combining them with (IC.29) proves
\[
\begin{aligned}
 \|\overline{\mathcal V}_1-\overline{\mathcal V}_0
       -D_{\bar u}\overline{\mathcal V}_0\Delta\bar u
       -D_e\overline{\mathcal V}_0e
       -D_{\bar q}\overline{\mathcal V}_0\bar q\|
 \le{}&\beta^{120L}(1+p)(1+M)\\
 &\cdot\{\bar\rho_0[R+d_0(N^2+Nu+u^2)]
                         +(1+\bar\rho_0)P\}.
\end{aligned}\tag{IC.32}
\]
For complex application, every scalar Taylor point must remain in the
half-strip. Starting from imaginary parts at most \(7a/16\), the
explicit sufficient gate is
\[
 d_0+\beta^{10L}u+\beta^{30L}(R+P)<a/32.
 \tag{IC.33}
\]
A first-exit argument using (IC.22) places the joining segments and the
auxiliary points \(z_0+z_{[1]}\) within \(15a/32\).
Cauchy's formula for \(\phi''\), on radius \(a/64\), bounds
the third derivative by \(64\beta/a\le4\beta^2\).
Replacing the coefficient \(\beta^{120L}\) in (IC.32) by
\(\beta^{240L}\) pays for all complex versions above. Transposes
remain algebraic; no complex energy inequality has been used.

There is no hidden division by \(S\) in this proof. More formally,
the effective network with actual hidden matrices and readout \(\bar u_w\)
is the original architecture pulled back by the affine map whose derivative
multiplies hidden parameter blocks by \(S\), the readout by one,
and ports by one. This derivative and its transpose are contractions.
Its second and higher derivatives vanish. Thus every displayed scaled
derivative is the corresponding effective derivative with a factor \(S\)
per hidden parameter argument, and never a negative power of \(S\).

Finally integrate the actual omitted row/column equations, not Gaussian
surrogates. Their learned parts obey
\[
 \|\Delta W_{:,i}^{(j+1)}\|
 \le S^2\tau_*A_n/\sqrt n,\qquad
 \|\Delta W_{i,:}^{(j)}\|
 \le S^2H_{\max}B_n/\sqrt n,
 \quad A_n=b+sM_n,\quad B_n=sM_n.
 \tag{IC.34}
\]
Multiplying by the actual controls gives forward and scaled reverse
source errors at most
\(pS^2(\tau_*A_n^2+H_{\max}B_n^2)/\sqrt n\).
Differentiating (IC.3) in its ports using (IC.28) shows that their
additional force is at most
\[
 S^2\beta^{260L}(1+p)^2(1+M_n)^3(1+\bar\rho)/\sqrt n.
 \tag{IC.35}
\]
At the top, \(|\bar d_a|\le pM_nA_n/n\), and its multiplication
of both retained terms costs at most
\(\beta^{32L}(1+p)^2(1+M_n)^3/\sqrt n\).
This includes the reverse-offset product. Current row norms are at most
three once the row increment in (IC.34) is below one.

## 4. Passive-query derivatives and the uniform Gaussian event

For a passive query \(q\), set \(C_q^{(j)}=D_\Theta h_q^{(j)}\).
For evaluated query \(q\) and training driver \(a\), define
\(\bar R_{qa}^{(j)}=S^{-1}D_\Theta z_q^{(j)}g_a\),
\(\bar Q_{qa}^{(j)}=\phi_j'(z_q^{(j)})\odot\bar R_{qa}^{(j)}\).
The exact response recurrences are
\[
 \bar R_{qa}^{(1)}=\bar\delta_a^{(1)}v_a^\top q,
 \quad\bar R_{qa}^{(j)}=
 \bar\delta_a^{(j)}c_{aq}^{(j-1)}+W^{(j)}\bar Q_{qa}^{(j-1)},
 \quad c_{aq}^{(j-1)}=h_a^{(j-1)\top}h_q^{(j-1)}/n.
 \tag{IC.36}
\]
For a complex great circle \(q(\zeta)=u\cos\zeta+v\sin\zeta\),
write \(J^{(j)}=\partial_\zeta z_q^{(j)}\) and
\(I^{(j)}=\phi_j'(z_q^{(j)})\odot J^{(j)}\). Then
\[
 J^{(1)}=Aq',\qquad J^{(j)}=W^{(j)}I^{(j-1)}.
 \tag{IC.37}
\]
These are passive derivatives; none changes the training equation.

The complete additional first-variation recurrences are
\[
\begin{aligned}
 c_{aq,[1]}&=(h_{a,[1]}^\top h_q+h_a^\top h_{q,[1]})/n,\\
 \bar R_{qa,[1]}^{(j)}&=
 \bar\delta_{a,[1]}^{(j)}c_{aq}
 +\bar\delta_a^{(j)}c_{aq,[1]}
 +{S V_{H^{(j)}}\over\sqrt n}\bar Q_{qa}^{(j-1)}
 +W^{(j)}\bar Q_{qa,[1]}^{(j-1)}+e_{qa,[1]}^{R,j},\\
 \bar Q_{qa,[1]}^{(j)}&=
 \phi_j'\odot\bar R_{qa,[1]}^{(j)}
       +\phi_j''\odot\bar R_{qa}^{(j)}\odot z_{q,[1]}^{(j)},\\
 J_{[1]}^{(1)}&=S V_Aq',\qquad
 J_{[1]}^{(j)}={S V_{H^{(j)}}\over\sqrt n}I^{(j-1)}
                  +W^{(j)}I_{[1]}^{(j-1)}+e_{[1]}^{J,j},\\
 I_{[1]}^{(j)}&=\phi_j'\odot J_{[1]}^{(j)}
                  +\phi_j''\odot J^{(j)}\odot z_{q,[1]}^{(j)}.
\end{aligned}\tag{IC.38}
\]
At the layer immediately above the deleted layer the extra ports are
\(e_{qa}^{R,j+1}=\sum_i x_i\bar Q_{qa,i}^{(j)}\) and
\(e^{J,j+1}=\sum_i x_i I_i^{(j)}\). At all other layers these
ports are zero. There is also a direct lower reverse observable, which
must be included in addition to (IC.38): below the deleted layer,
\[
 Q_{qa,\mathrm{full}}^{(j-1)}
   =C_q^{(j-1)}[g_a+C_a^{(j-1)\top}q_a],
 \quad S^{-1}(Q_{qa,\mathrm{full}}-C_qg_a)
                   =C_qC_a^\top\bar q_a.
 \tag{IC.39}
\]
Thus its reference linear map includes \(C_q^0C_a^{0\top}y_i\)
for every driver and omitted incoming root. Include the reference
forward images of \(\xi=C_a^{0\top}y_i\) at every lower layer
in the same Gaussian coordinate event. This explicitly lists the
additional probes. Their coefficient operators are measurable in retained
initialization and independent of the omitted root; the probe vectors
themselves depend linearly on that root. Their operator bounds therefore
give the claimed centered Gaussian vector estimates.

Here are remainder bounds for these additions. The feature-pairing
product identity gives
\[
 |c_{aq,[1]}|\le\beta^{10L}(N+u)/\sqrt n,\quad
 |E_c|\le\beta^{40L}\{(R+P)/\sqrt n+(N+u)^2/n\}.
 \tag{IC.40}
\]
The exact product/mixer remainders in (IC.36) are
\[
 E_{\bar R}=E_{\bar\delta}c_1+
       \bar\delta_{[1]}(c_1-c_0)+\bar\delta_0E_c
       +W_1E_{\bar Q^{\rm prev}}
       +\Delta W\bar Q_{[1]}^{\rm prev}+E_{\rm ports},
\]
\[
 E_{\bar Q}=\phi'(z_1)E_{\bar R}
       +[\phi'(z_1)-\phi'(z_0)]\bar R_{[1]}
       +\bar R_0[\phi'(z_1)-\phi'(z_0)-\phi''(z_0)z_{[1]}].
 \tag{IC.41}
\]
Equations (IC.23)--(IC.24) apply verbatim to \(J,I\), with
\(E_{J^{(1)}}=0\), their displayed response ports, and \(J_0\)
in place of a reference carrier. In (IC.41), \(\bar\delta_0E_c\)
uses response RMS \(\sqrt n\tau_j\), canceling the first
\(1/\sqrt n\) in (IC.40). Every product of two changed factors
retains a width or localized-coordinate factor. Reference \(\bar R\)
and \(J\) coordinate caps appear only in additive gate remainders.

For (IC.39), subtract the directional forward recursions in the fixed
direction \(\xi\). The new forcing terms are
\(\xi_H\Delta h/\sqrt n\), \(\Delta H Dh_0[\xi]/\sqrt n\),
and a changed activation gate multiplying \(Dz_0[\xi]\).
On the enlarged Gaussian event that last vector has maximum \(d_0\).
Propagation through the perturbed bounded mixers/slopes gives
\[
 \|(C_q^1-C_q^0)\xi\|
 \le\beta^{50L}(d_0+n^{-1/2})(N+u).
 \tag{IC.42}
\]
The other product difference is
\(C_q^1(C_a^1-C_a^0)^\top y_i\); use (IC.31) and
\(\|C_q^1\|\le\beta^{10L}\). Multiplication by the actual
controls and summation over roots gives
\[
 \|C_q^1C_a^{1\top}\bar q_a-C_q^0C_a^{0\top}\bar q_a\|
 \le\beta^{70L}(1+p)(1+M_n)
 (d_0+n^{-1/2})[N+u+(N+u)^2].
 \tag{IC.43}
\]
The missing feature-pairing term is at most \(pA_n^2/n\);
the learned response and angular ports are bounded using (IC.34)
times their actual stopped controls. These are additional
\(n^{-1/2}\) vector errors. This accounts for every term hidden by
rectangular deletion in (IC.36)--(IC.39).

For fixed \(p,m,d,L\), use the temporary query preactivation cap
in S.6 and doubled response/angular caps from (S.25). Equations
(IC.10)--(IC.17), (IC.38), and the product rule give operator bounds
\(n^\kappa\) times fixed polynomials in \(\ell\) for all the
listed linear maps. For completeness, each differentiated gate is
\(\phi''z_{[1]}\), each differentiated carrier gate is
\(\phi'''z_t z_{[1]}\bar k+\phi''z_{[1]}\bar k_t
 +\phi''\bar k z_{[1],t}\), and the response/angular gate has
the same three terms with \(\bar R\) or \(J\). At most one
raw reference coordinate derivative is used in each term. Its bound
is \(\sqrt n\) times a fixed polynomial in \(\ell\).
All homogeneous propagated derivatives have multiplier \(10s\).
This proves terminal and frame derivative bounds
\(\sqrt n n^\kappa\operatorname{poly}(\ell)\), with no
power of \(n\) depending on depth. Frame derivatives of the input
and of \(q'\) are bounded on a fixed tubular neighborhood of the
orthonormal-frame manifold. Differentiating (IC.38) in those variables
uses the same gate terms just listed. Polar normalization provides
bounded local frame-coordinate derivatives.

The controls in (IC.38) have polynomial logarithmic amplitudes. Their
time speeds cost one \(\sqrt n\): for example
\(\partial_t\bar Q=\phi'\partial_t\bar R+
\phi''\bar R\partial_tz\), where the stopped coordinate cap
on \(\bar R\) and the RMS bound on \(\partial_tz\) give a
polynomial logarithmic RMS speed. The same calculation with \(J\)
gives the angular-control speed. Thus the complete control net at
accuracy \(\tau=n^{-1/8}\) has logarithmic cardinality bounded
by \(n^{5/8}\operatorname{poly}(\ell)\). In detail, \(q_c\)
real component controls with amplitude \(M_c\), Lipschitz constant
\(D_c'\sqrt n\), and contour length \(T_c\) admit a net with
\[
 \log N_{\rm ctrl}\le
 q_c(2+8T_cD_c'n^{5/8})\log(1+8M_cn^{1/8}).
 \tag{IC.44}
\]
Sample each real/imaginary component at spacing
\(\tau/(8D_c'\sqrt n)\), round on mesh \(\tau/4\),
and interpolate. This proves both its accuracy and cardinality.

For fixed controls, the conditional root covariance is \(I/n\).
After eventual absorption of the fixed logarithmic coefficients, every
listed linear operator and quadratic matrix has norm at most
\(n^{1/200}\). A coordinate has variance at most \(n^{-99/100}\).
For a centered form, diagonalizing its real symmetric part and using
\[
 \mathbb E e^{t(G^\top RG-\operatorname{tr}R)}
   =\prod_\alpha e^{-t\lambda_\alpha}
                         (1-2t\lambda_\alpha)^{-1/2},
\]
\[
 -\log(1-v)-v\le v^2/[2(1-|v|)]\quad(|v|<1)
 \tag{IC.45}
\]
gives a tail bounded by the minimum of threshold squared divided by
Hilbert--Schmidt variance and threshold divided by operator scale.
Here \(\|R\|_{\rm HS}\le\sqrt{2pn}\|R\|\).
At threshold \(n^{-1/10}/8\), real/imaginary splitting yields
\(4e^{-n^{0.78}}\) eventually. Independent-root bilinear forms
are the symmetric off-diagonal block case of (IC.45).
Root norms \(\|g\|\le2\sqrt{2p}\) have failure at most
\(e^{-pn}\). They also give whole-vector image bounds below
\(n^{1/100}\) after coefficients are absorbed. Use a smaller
fixed share of this bound for each of the finitely many augmented
components, so their combined norm in (IC.19) is at most that radius.

Control interpolation uses (IC.12)--(IC.14); its error is
\(n^{-1/8+1/200}\operatorname{poly}(\ell)\), smaller than
\(n^{-1/10}/4\). A time/query/frame mesh of size
\(n^{-2}/\operatorname{poly}(\ell)\) gives the other
\(n^{-1/10}/4\). There are \(2d+3\) real frame/time/tube
coordinates, so for fixed parameters its point count is at most
\(n^{4d+10}\) eventually. The entropy (IC.44), this grid, the
coordinate/probe tests, and at most \(pLn^p\) deletion sets cost
less than \(n^{0.65}\) in logarithmic cardinality. The resulting
uniform failure is at most \(e^{-n^{0.7}}\) eventually. Only
now substitute the adaptive training and passive-query controls.

Let \(V\) solve the exact linear variational equation and let \(U\)
be the retained scaled displacement minus \(V\). It satisfies
\[
 U(t)=\int_0^t J(t,s)
  [\mathcal R(\Delta\bar u(s),e(s),\bar q(s))
       +\mathcal R_{\rm learned}(s)+\mathcal R_{\rm top}(s)]\,ds,
 \qquad U(0)=0,
 \tag{IC.46}
\]
where the three terms have exactly the bounds (IC.32), (IC.35),
and the top-offset bound following it. Take
\(N=n^{1/100}\), \(d_0=n^{-1/10}\), \(u_0=n^{-1/25}\).
On a first-exit prefix \(\|U\|\le u_0\), integration with
(IC.4) and (IC.8) bounds (IC.46) by
\[
 n^\kappa\operatorname{poly}(\ell)
       [n^{-8/100}+u_0^2+n^{-48/100}+n^{-1/2}]
                     =o(u_0).
 \tag{IC.47}
\]
This strictly improves the remainder stop. Equations (IC.25)--(IC.26)
and (IC.40)--(IC.43) then give retained coordinate discrepancies
at most \(n^{-1/30}\) eventually, for preactivations, scaled
carriers, responses and angular derivatives, and whole-vector
discrepancies at most \(2n^{1/100}\). The strict strip condition
(IC.33) closes simultaneously. The reference is always its independently
stopped cavity; this argument transfers its prefix rather than conditioning
a Gaussian law on full-network survival.

## 5. The actual contractions behind (S.15) and the mixed endpoints

We now write the singleton expansion in unscaled mobility coordinates;
all \(1/n\) factors remain visible. At an interior omitted neuron,
put
\[
 C_a(t)=D_\Theta h_a^{(j-1)}(t),\quad
 B_a(t)=D_\Theta\delta_a^{(j+1)}(t),\quad
 E_a(t)=D_{e_a^{(j+1)}}\delta_a^{(j+1)}(t).
\]
All three are zero-source cavity derivatives. With deterministic
controls \(\alpha_a=h_{a,i}^{(j)}\),
\(b_a=\delta_{a,i}^{(j)}\), the linear mobility response is
\[
 V(t)=-{2\over m}\sum_b\int_0^t J(t,s)
 \left[{g_b(s)d_b(s)^\top\over n}x_i\alpha_b(s)
       +r_b(s)B_b(s)^\top x_i\alpha_b(s)
       +r_b(s)C_b(s)^\top y_i b_b(s)\right]ds,
 \quad d_b=\delta_b^{(j+1)}.
 \tag{IC.48}
\]
The two scalar linearized pairings are
\[
 z_{a,i}=y_i^\top h_a^0+y_i^\top C_aV
                 +(\Delta W_{i,:})h_a+\varepsilon_z,
\]
\[
 k_{a,i}=x_i^\top\delta_a^0+x_i^\top B_aV
                 +x_i^\top E_ax_i\alpha_a
                 +(\Delta W_{:,i})^\top\delta_a+\varepsilon_k.
 \tag{IC.49}
\]
The remainders include the nonlinear vector errors and their root
pairings; they are uniform small errors from (IC.46)--(IC.47).
For the scaled statement apply the same identities before dividing
the carrier terms by \(S\), as in (IC.1)--(IC.35).

Substituting (IC.48) into (IC.49) identifies all nonzero Gaussian means:
\[
\begin{array}{ll}
 \text{incoming reverse mean:}&
 -{2\over m}\displaystyle\sum_b\int_0^t
 r_b(s)b_b(s){\operatorname{tr}[C_a(t)J(t,s)C_b(s)^\top]\over n}\,ds,\\[2mm]
 \text{outgoing Hessian mean:}&
 -{2\over m}\displaystyle\sum_b\int_0^t
 r_b(s)\alpha_b(s){\operatorname{tr}[B_a(t)J(t,s)B_b(s)^\top]\over n}\,ds,\\[2mm]
 \text{direct outgoing mean:}&
 \alpha_a(t)\operatorname{tr}E_a(t)/n,\\[1mm]
 \text{adaptive-residual mean:}&
 -{2\over mn^2}\displaystyle\sum_b\int_0^t
 \alpha_b(s)d_b(s)^\top B_a(t)J(t,s)g_b(s)\,ds.
\end{array}\tag{IC.50}
\]
Every remaining linearized pairing has distinct incoming/outgoing roots
and hence zero conditional mean, or is a centered same-root form. Their
fluctuations are already controlled by (IC.13)--(IC.45). In particular,
the direct mean multiplies the evaluated sample's current \(\alpha_a\),
whereas the integrated means retain a sum over driving samples.
The last line has the additional \(1/n\): using
\(\|d_b\|,\|g_b\|=O(\sqrt n)\) bounds it by
\(n^{-1+\kappa}\operatorname{poly}(\ell)\) on a logarithmic
horizon. It belongs to the small remainder, not to a nonzero limiting
trace coefficient.

Here is the complete trace bound for the second line. Split the
propagator into its negative-Gram base and residual-Hessian insertions.
An ordered term with \(h\) insertions has residual-activity integral
at most \(S^h/h!\). The product of base propagators costs at most
two: their disjoint short contour pieces have total norm-growth integral
at most \(\log2\), while forward real pieces contract. Normalized
Schatten Hölder with exponent \(h+2\) on the two endpoint Hessian
blocks and all \(h\) inserted Hessians bounds its normalized trace by
\[
 {2S^h\over h!}
 [A_*+(SD_*/\eta)(h+2)(2\mathcal B)^{1/(h+2)}]^{h+2}.
 \tag{IC.51}
\]
The term \(h=0\) is at most \(2H_*^2\), using both endpoint
Hilbert--Schmidt bounds. For \(h\ge1\), use
\((x+y)^{h+2}\le2^{h+1}(x^{h+2}+y^{h+2})\).
The bounded part sums to \(4A_*^2(e^{2SA_*}-1)\).
For the carrier part, \(h!\ge(h/e)^h\) and
\((1+2/h)^h\le e^2\) bound its sum by
\[
 {8e^2D_*^2S^2\mathcal B\over\eta^2}
 \sum_{h\ge1}(2eD_*S^2/\eta)^h(h+2)^2
 \le{576e^3D_*^3\mathcal B S^4\over\eta^3}.
 \tag{IC.52}
\]
The last inequality uses \(q=2eD_*S^2/\eta\le1/2\) and
\(\sum_{h\ge1}q^h(h+2)^2\le36q\), obtained by differentiating
the geometric series twice. Equation (S.10) gives this condition.

For the first line of (IC.50), the zero term is at most \(2f_*^2\).
For \(h\ge1\), give one forward endpoint exponent two, the other
infinity, and each Hessian exponent \(2h\). The bounded part of
the inserted series is controlled by \(e^{2SA_*}-1\), and the
carrier part by
\(\sqrt{2\mathcal B}\sum_{h\ge1}(4eD_*S^2/\eta)^h\).
Both are at most one by (S.10). Their factors, together with the zero
term, give
\[
 {1\over n}|\operatorname{tr}(C_aJ C_b^\top)|\le8f_*^2.
 \tag{IC.53}
\]
These uses of Schatten Hölder have total reciprocal exponent one.
The normalizations multiply to exactly \(n^{-1}\), independent
of the parameter dimension.

For the direct term, let \(T_{r,j+1}\) be the forward derivative
from the port in layer \(j+1\) to preactivation in layer \(r\).
The port Hessian is exactly
\[
 E_a=\sum_{r=j+1}^L T_{r,j+1}^\top
       \operatorname{diag}(k_a^{(r)}\phi_r'')T_{r,j+1}.
\]
Here \(\|T_{r,j+1}\|\le(10s)^{r-j-1}\), and the nuclear
norm per width of the diagonal is at most \(t_2Sk_r\), by
the carrier RMS. Thus \(|\operatorname{tr}E_a|/n\le SE\)
with exactly the coefficient \(E\) in (S.8).

The learned outgoing column paired with the current upper response has
bound \(s^2k_*^2S^3\) times the driving forward amplitude after
the residual average. The learned incoming row paired with a current
feature has bound \(sS^2U_iH_{j-1}^2\). Both follow by substituting
their rank-one update integrals and applying RMS Cauchy--Schwarz to
each retained vector. At the first layer its direct update has bound
\(sS^2U_i\). Finally, for every driving time,
\[
 {1\over m}\sum_b|r_b||h_{b,i}|\le\rho(b+sZ_i),\qquad
 {1\over m}\sum_b|r_b||\delta_{b,i}|\le\rho sS U_i.
 \tag{IC.54}
\]
These follow from the running sample RMS definitions (S.12), so they
also bound all past integrands. Combine (IC.50)--(IC.54) and divide
the backward inequality by \(S\). The constants (S.8) give exactly
\[
 K_{a,i}/S\le G_{\delta,a,i}/S+
 [D_0+D_1\mathcal B S^4/\eta^3](1+Z_{a,i}+Z_i)+\varepsilon_n,
 \quad
 Z_{a,i}\le G_{h,a,i}+C_FS^2U_i+\varepsilon_n.
 \tag{IC.55}
\]
This is (S.15) with its contractions specified. For fixed parameters
\(\varepsilon_n\to0\); under the finite gate below it is at most
\(n^{-1/40}\), in the scaled norms. At the top use the exact
readout integral \(\sup|w_i|/S\le b+sZ_i\), taking
\(G_{\delta,a,i}=0\). At the first layer take
\(G_{h,a,i}=\sup|A_{0,i}v_a|\). These endpoint formulas prove
the same absorption, without inventing absent roots.

The mixed endpoint constants in (S.24) can now be checked directly.
For \(Q_{qa}=C_qg_a\),
\[
 DQ_{qa}=C_qDg_a+(DC_q)[\,\cdot\,]g_a.
 \tag{IC.56}
\]
The first term has normalized Hilbert--Schmidt bound \(f_jH_*\).
For the second, differentiating its forward recursion gives respectively
the curvature diagonal \(\operatorname{diag}(\phi''R)Dz\),
the changed mixer \(U_HQ/\sqrt n\), the term where the fixed
gradient block acts on a changed feature, and the propagated lower
derivative. Their normalized Hilbert--Schmidt coefficients are
\(t_2r_jP_j\), \(sq_{j-1}\),
\(s\tau_jH_{j-1}f_{j-1}\), and \(10s e_{j-1}\),
respectively. This is precisely the recurrence defining \(e_j\).
For example
\(\|\operatorname{diag}(R)Dz\|_{\rm HS}/\sqrt n
\le P_j\|R\|_2/\sqrt n\); no response maximum is needed
for this Hilbert--Schmidt estimate. Replacing \(R\) by \(J\)
gives \(t_2j_jP_j+s(b_{j-1}+10a_{j-1})\); at the first layer
the map \(U_Aq'\) adds at most two. These are the coefficients
\(a_j\) in (S.24). Applying the asymmetric estimate (IC.53) with
these endpoints gives exactly \(T_Q,T_J\).

For clarity, row insertion of (IC.36) has four noncentered terms:
the direct feature pairing, the direct reverse observable (IC.39),
the integrated mixed endpoint (IC.56), and the learned incoming row.
After division by \(S\), their coefficients are
\[
 sK_{\rm src}H_{j-1}^2,\quad
 sK_{\rm src}f_{j-1}^2,\quad
 sK_{\rm src}ST_Q,\quad
 sK_{\rm src}S^2H_{j-1}q_{j-1}.
 \tag{IC.57}
\]
For (IC.37) there are the mixed endpoint and learned row, with
coefficients \(sK_{\rm src}S^2T_J\) and
\(sK_{\rm src}S^2H_{j-1}b_{j-1}\). The incoming-root Gaussian
reference contributes \(G_dq_{j-1}\) or \(G_db_{j-1}\).
Every forward-source pairing uses one incoming and one outgoing root
and is centered; the training reverse source supplies the same incoming
root twice. This proves the enumeration and the coefficients (S.25),
including the lower direct reverse term. Its factor two leaves strict
margin for the uniform errors in Section 4. The Gaussian mesh count
there and \(G_d=16\sqrt{d+3}\) give (S.26). No exponential
query budget has been added.

## 6. A sharper initialization gate, needed for the finite width claim

The older displayed \(N_{\rm fit}\) has a sphere-net cardinality
outside a logarithm. It cannot be used to justify a width polynomial in
dimension. The following replacement has the same event and label cap.
Here only write \(H=H_D\) for the population RMS coefficient of
the existing dense-fitting theorem, and define
\[
 R_0=2H,\quad K_0=b+sR_0,\quad D_0^{\rm init}=2sb+4s^2R_0,
 \quad T_1=\sum_{j=0}^{L-1}s^j,\quad T_2=\sum_{j=0}^{L-1}s^{2j},
\]
\[
 C_0=T_2(2K_0+1+D_0^{\rm init}T_1),\qquad
 \epsilon_0=\min\{(8T_1)^{-1},\lambda/(2C_0)\},
 \quad h_0=\min\{1/2,H/[4(8s)^L]\}.
\]
For failure \(\alpha\in(0,1)\), set
\[
 \Xi_0=\log[16L(m+1)^2/\alpha]+d\log(1+2/h_0),
\]
\[
 N_{\rm fit}^{\rm exp}(\alpha)=\left\lceil\max\left\{
 1,{\log(8L/\alpha)\over8-2\log9},
 {d\log9+\log(8/\alpha)\over8-\log9},
 {32s^2R_0^2\Xi_0\over\epsilon_0^2}\right\}\right\rceil.
 \tag{IC.58}
\]
For every \(n\ge N_{\rm fit}^{\rm exp}(\alpha)\), with
probability at least \(1-\alpha\), initial operators are at most
eight, all initial sphere feature RMS norms are at most \(11H/8\),
and the normalized training Gram gap is at least \(\lambda/2\).

We supply the concentration proof. If \(F\) is \(a_0\)-Lipschitz
in a standard Gaussian vector, then
\[
 \log\mathbb E e^{t(F-\mathbb EF)}\le a_0^2t^2/2,
 \qquad\operatorname{Var}F\le a_0^2.
 \tag{IC.59}
\]
One proof uses the Gaussian semigroup
\(P_tg(x)=\mathbb E g(e^{-t}x+\sqrt{1-e^{-2t}}G)\).
Differentiating its invariant entropy and integrating by parts gives
\[
 \operatorname{Ent}_\gamma(g)=
 \int_0^\infty\mathbb E{|\nabla P_tg|^2\over P_tg}\,dt
 \le\int_0^\infty e^{-2t}\mathbb E P_t(|\nabla g|^2/g)\,dt
 ={1\over2}\mathbb E|\nabla g|^2/g.
\]
The inequality is weighted Cauchy--Schwarz and
\(\nabla P_tg=e^{-t}P_t\nabla g\). Apply it to \(g=e^{uF}\)
and integrate the differential inequality for
\(u^{-1}\log\mathbb E e^{uF}\). Truncation and smoothing extend
the bounded smooth calculation to Lipschitz \(F\); its Gaussian
exponential integrability follows from linear growth. This proves
(IC.59), its variance statement by differentiation at zero, and tails
\(2e^{-t^2/(2a_0^2)}\). For nonnegative \(F\), its mean differs
from \(\sqrt{\mathbb EF^2}\) by at most \(a_0\). Therefore
at tolerance \(\epsilon\ge2a_0\) its deviation from that RMS
has probability at most \(2e^{-\epsilon^2/(8a_0^2)}\).

Conditioned on preceding layers, an individual empirical feature RMS is
\(sR_0/\sqrt n\)-Lipschitz. The empirical RMS of
\(\phi(Z_a)\pm\phi(Z_b)\) is
\(2sR_0/\sqrt n\)-Lipschitz, including singular pair covariances.
Polarization of these two norms shows that simultaneous RMS errors at
most \(\epsilon_0\le1\) give covariance-entry error at most
\((2K_0+1)\epsilon_0\) relative to the conditional covariance
transform.

Two distinct propagation estimates avoid a depth-squared power. The
population scalar RMS transform is \(s\)-Lipschitz in its input
standard deviation, by coupling with the same scalar Gaussian. If two
Gaussian pair covariances have diagonal standard deviations at most
\(R_0\), differing by at most \(\Delta\), their activation
covariances differ by at most
\[
 s^2|C_{ab}-C'_{ab}|+(2sb+4s^2R_0)\Delta.
 \tag{IC.60}
\]
To prove this, shrink both marginal standard deviations to their common
minimum, preserving correlations. The total scaling cost is at most
\(2sK_0\Delta\), by subtracting product factors and applying
Cauchy--Schwarz. At fixed marginal standard deviations \(\tau_a,\tau_b\),
Gaussian density differentiation and two integrations by parts give
correlation derivative
\(\tau_a\tau_b\mathbb E[\phi'(Z_a)\phi'(Z_b)]\), of modulus
at most \(s^2\tau_a\tau_b\). Direct subtraction of the two
correlations gives
\(\tau_a\tau_b|\varrho-\varrho'|
 \le|C_{ab}-C'_{ab}|+2R_0\Delta\).
These estimates prove (IC.60). Degenerate variances and correlations
\(\pm1\) follow by Gaussian dominated convergence, using linear
activation growth; no variance is divided out in the final bound.

Take a sphere \(h_0\)-net of cardinality at most
\((1+2/h_0)^d\), obtained from disjoint balls centered at a maximal
separated set. At each layer test its individual norms, the training
individual norms, and the two polarization norms for every training
pair. If \(\Delta_j\) is the largest individual RMS error and
\(E_j\) the largest training covariance-entry error, the stopped
induction is
\[
 \Delta_j\le\epsilon_0+s\Delta_{j-1},\qquad
 E_j\le(2K_0+1)\epsilon_0+s^2E_{j-1}
                             +D_0^{\rm init}\Delta_{j-1}.
\]
It gives \(\Delta_j\le1/8\), \(E_j\le\lambda/2\), and
conditional input standard deviations below \(H+1/8<R_0\).
There are at most \(L[3m^2+(1+2/h_0)^d]\) tests. Their union
failure is at most
\[
 2L[3m^2+(1+2/h_0)^d]
       e^{-n\epsilon_0^2/(32s^2R_0^2)}\le\alpha/2.
\]
The two one-quarter operator nets have scalar threshold exponent
\(-8n\) and cardinalities \(9^{2n}\) or \(9^{n+d}\).
The second and third gates in (IC.58) pay their total failure
\(\alpha/2\). On that operator event, normalized features are
\((8s)^j\)-Lipschitz in the query. Their off-net increment is at
most \(H/4\), so their sphere RMS is at most
\(H+1/8+H/4\le11H/8\). Finally
\(\|\mathsf H^\top\mathsf H/n-Q^{(L)}\|\le mE_L\le\gamma/2\).
This proves the asserted event.

The deterministic fitting proof already in RESULT applies to this
stronger event with its unchanged condition
\(Y\le\lambda/(8H_D\sqrt{F_D})\). Its stop improvements use
only the initial operator/RMS/Gram bounds just proved. In particular
\(\rho(t)\le Ye^{-\lambda t/2}\), and the weaker decay
(S.3) is available. Direct finite-sum estimates give
\[
 H\le\beta^{2L},\quad R_0,K_0\le\beta^{3L},\quad
 D_0^{\rm init}\le\beta^{4L},\quad T_1\le\beta^{2L},\quad
 T_2\le\beta^{3L},\quad C_0\le\beta^{10L},
\]
\[
 \epsilon_0^{-1}\le\beta^{11L}(1+\lambda^{-1}),\quad
 32s^2R_0^2\le\beta^{8L},\quad
 \log(1+2/h_0)\le3L\log\beta.
\]
Thus a convenient sufficient envelope for (IC.58) is
\[
 n\ge\beta^{32L}(1+\lambda^{-1})^2
 [dL\log\beta+\log(16L(m+1)^2/\alpha)]+1.
 \tag{IC.61}
\]
This gate replaces, rather than assumes domination of, the older
exponential-in-dimension initialization gate in the Logarithmic proof.

## 7. Quantitative training-source coefficient and width ledger

Fix failure \(0<\rho<1/4\) for this one source event, and set
\[
 p=\max\left\{1,\left\lceil{\log(4emL/\rho)\over\log(64e^2)}
                         \right\rceil\right\},\qquad
 Q=m+d+p+1,\qquad
 \mathcal A=\beta^{2000L}(1+\lambda^{-1})^4Q^4.
 \tag{IC.62}
\]
The time domain is the neighborhood of the closed rectangle
\[
 [-r_t,32\ell/\lambda+r_t]+i[-r_t,r_t],\qquad
 r_t={1\over p\beta^{100L}(1+\lambda)\sqrt\ell}.
 \tag{IC.63}
\]
Only the \(m\) training queries and \(m^2\) training responses
are used in the finite union. Define \(U_j^{\rm fin}\) by (S.25)
with \(G_d\) replaced by 64. There is no dimension mesh in this
source event. The exact response, reverse-observable and probe
calculations are (IC.36)--(IC.43).

Here is a numerical coefficient ledger from those displayed recurrences.
All powers of \(\ell,n,\sqrt p\) stated separately below are
removed before bounding a coefficient.

| Coefficient | Sufficient bound |
| --- | --- |
| \(H_j,P_j,k_j,\tau_j\) | \(\beta^{3L},\beta^{3L},\beta^{5L},\beta^{6L}\) |
| \(A_*,D_*,H_*,D_0,C_{\rm abs},W_{\rm G}\) | \(\beta^{11L},\beta^{8L},\beta^{13L},\beta^{30L},\beta^{32L},\beta^{23L}\) |
| \(\eta^{-1},M_0,A_0,B_0\) | \(\beta^{80L}\) |
| \(\max U_j^{\rm fin}\) | \(\beta^{72L}\) |
| (IC.10)--(IC.17), including control/time moduli | \(\beta^{300L}(1+\lambda^{-1})\) |
| Additional response/probe maps (IC.38)--(IC.43) | \(B=\beta^{1000L}(1+\lambda^{-1})^2\) |
| Integrated local, learned-port and top-offset coefficients | \(B(1+p)^2\) |

To check the depth dependence in this ledger, every homogeneous layer
propagation is bounded by \(10s\le\beta^2\), and every finite
layer sum costs at most \(L\le\beta^L\). In (S.7), substitute
\(P_j\le\beta^{3L}\), \(k_j\le\beta^{5L}\): the mixed,
curvature and squared trace coefficients then have the exponents in
the first two rows. The sums (S.9) give
\(V_*\le\beta^{15L}\), \(G_*\le\beta^{20L}\), hence
the displayed \(W_{\rm G}\). Inserting these into
\(\eta^{-1}=1024C_{\rm abs}W_{\rm G}\) and multiplying by
\(1+\log(2\mathcal B)\) gives the third row with numerical slack.
For (S.24), its terms give
\(g\le\beta^{10L}\), \(r_j\le\beta^{13L}\),
\(q_j\le\beta^{14L}\), \(e_j\le\beta^{21L}\), and
\(T_Q\le\beta^{27L}\). Substitution into (IC.57) gives the
\(72L\) response envelope. The largest operation in (IC.16) is
one additional reference-carrier factor times a forward time derivative;
the entire recurrence has degree at most four in \(M_0\) and
degree one in \(T_*\). This gives its \(300L\) envelope.
To check this last power without repeatedly using the deliberately loose
\(80L\) row, retain the sharper intermediate bounds
\(\eta^{-1}\le\beta^{57L}\),
\(M_0,A_0,B_0\le\beta^{60L}\), and \(E_0\le\beta^{69L}\).
They give \(v_0,v_c\le\beta^{133L}(1+\lambda^{-1})\),
forward coefficients at most \(\beta^{137L}(1+\lambda^{-1})\),
backward coefficients at most \(\beta^{202L}(1+\lambda^{-1})\),
\(A_t\le\beta^{76L}\), and forward time coefficients at most
\(\beta^{217L}(1+\lambda^{-1})\). The final backward time
forcing adds at most \(61L\), and its geometric propagation at
most \(3L\), remaining below \(300L\). These estimates also
use \(\lambda\le\beta^{6L}\), so no positive-gap power is
left uncharged.

More explicitly, the enlargement from base to response maps has
coefficient at most
\[
 \beta^{100L}(1+M_0+4U_*^{\rm fin})^2(1+C_*)^2,
 \quad C_*=\max\{1,\hbox{coefficients in (IC.10)--(IC.17)}\}.
 \tag{IC.64}
\]
In (IC.38), its four preactivation forcing terms are respectively a
backward variation times a bounded scalar, a reference response times
the pairing variation, a changed mixer times response RMS, and a lower
propagated variation. The new gate term adds one reference response cap.
The additional reverse map (IC.39) is a product of two bounded forward
derivatives. Time differentiation adds one reference speed, and control
subtraction is linear in the control differences. Thus (IC.64) covers
the map, control modulus, and time modulus with respective powers
\(\sqrt p n^\kappa\ell^5\),
\(\sqrt p n^\kappa\ell^4\epsilon\), and
\(\sqrt{pn}n^\kappa\ell^8\).
It is at most the stated \(B\), since its numerical/depth factors
cost less than \(100+160+600+20=880\) powers of \(\beta^L\).
The response remainder from (IC.40)--(IC.43) is bounded by
\[
 \beta^{240L}(1+p)^2(1+M_n+4U_*^{\rm fin}\sqrt\ell)^3
 [R+P+d_0(N+u+(N+u)^2)].
 \tag{IC.65}
\]
The homogeneous terms in (IC.41) cost \(10s\); the reference
cap occurs only in forcing. This proves the fixed cutoff degree three.
The coefficient in (IC.35), contour length, and (IC.8) also fit the
last ledger row with room below \(1000L\). No depth-dependent
power of \(\ell\) or cutoff is absorbed into that row.

There is a sharper bound useful to the numerical decoder:
\(K_{\rm src}\le\beta^{21L}\), and hence certainly
\(K_{\rm src}\le\beta^{40L}\). It follows directly from the
S-independent source recurrence ledger:
\(C_{\rm abs}\le\beta^{16L-1}\),
\(H_j\le3\beta^{2j}\),
\(\tau_j\le3\beta^{4L-2j+1}\), and (S.22).
These bounds concern source constants and do not require a stronger
label cap.

The useful width conditions are
\[
 \mathcal A\ell^{16}\le n^{1/1000},\qquad n\ge64mL/\rho.
 \tag{IC.66}
\]
They are implied by the factorized gate
\[
 n\ge\left\lceil\max\left\{
 [2\mathcal A(2000\log(2\mathcal A))^{16}]^{1000},
 64mL/\rho\right\}\right\rceil,
 \tag{IC.67}
\]
which is in turn implied by \(n\ge\lceil(\mathcal A/\rho)^{1100}\rceil\).
To prove this without an implicit logarithmic onset, put
\(u=\log(2\mathcal A)>9000\). The increasing function
\(u/320-\log(2000u)\) is positive at 9000, so
\(x_0=1000[u+16\log(2000u)]\le1050u\), and
\(1+x_0\le2000u\). Hence
\(\mathcal A(1+x_0)^{16}\le\tfrac12 e^{x_0/1000}\).
The function \(x/1000-16\log(1+x)\) increases for \(x>15999\),
proving (IC.66) at every larger width. Also
\(1050\log(2\mathcal A)\le1100\log\mathcal A\) and
\(\mathcal A\ge64mL\), proving the power-1100 envelope.

For explicit checking of the remaining inequalities, (IC.66) implies
\[
 \log n>9\cdot10^6,\quad
 p,m,d\le n^{1/4000},\quad L\le n^{1/2000000},\quad
 \log(1/\rho)\le\log n,\quad
 \log(64nmL/\rho)\le2\log n.
 \tag{IC.68}
\]
Every numerical comparison of logarithms with positive powers below is
valid already at this displayed lower endpoint and improves with width.

The following table gives the actual finite Gaussian-union and remainder
bounds. It instantiates Sections 2--4 at the coefficients just proved.

| Step | Bound or sufficient inequality |
| --- | --- |
| Linear/quadratic map norm | \(B\sqrt p n^{1/4000}\ell^5\le n^{3/4000}<n^{1/200}\) |
| Quadratic fixed-grid exponent at \(n^{-1/10}/8\) | \(\min\{n^{.79}/(8192p),n^{.895}/128\}>n^{.78}\) |
| Centered control interpolation | \(80Bp^{3/2}\ell^4\le n^{99/4000}\) |
| Terminal mesh | \(h_t=n^{-2}/(1+\mathcal A\ell^8)\), at most \(n^6\) terminals |
| Terminal error | \(10\sqrt2Bp^{3/2}n^{1/2+1/4000}\ell^8h_t<n^{-1/10}/8\) |
| Control entropy | \(\log N_{\rm ctrl}\le\mathcal A\ell^8n^{5/8}\le n^{.626}\) |
| Remaining coordinate/probe/form tests | at most \(\mathcal A n^3\) per deletion set and terminal |
| Local total failure | \(4pL\mathcal A n^{p+9}e^{n^{.626}-n^{.78}}+pLn^pe^{-pn}<e^{-n^{.7}}<\rho/16\) |
| Integrated nonlinear force | \(\mathcal A\ell^8n^{1/4000}[n^{-.08}+u_0^2+n^{-.48}+n^{-1/2}]<u_0/2\) |
| Coordinate transfer | \(16\mathcal A\ell^8[d_0+u_0+R+P+d_0(N+u_0+(N+u_0)^2)]<n^{-1/30}\) |
| Scalar trace error | \(32\mathcal A\ell^8n^{-1/30}<n^{-1/40}\) |

For example, \(B=\sqrt{\mathcal A}/Q^2\), so the control
interpolation left side is at most \(80n^{1/2000}\).
The nonlinear-force left side is at most \(4n^{-.07875}\),
whereas \(u_0/2=n^{-.04}/2\). The coordinate-transfer left
side is at most \(256n^{-.039}\), whose exponent is strictly
smaller than \(-1/30\). These verify the margins; the exceptional
probability row follows by taking logarithms and (IC.68).
The terminal mesh count uses side lengths at most
\(34(1+\lambda^{-1})\ell\), and control count at most
\(4p(m+1)^2\) real components. Their speeds are at most
\(\sqrt n\ell^3\) times the ledger coefficient, as shown by
(IC.38). Thus the powers used in this table do not presume the
desired Gaussian event.

Full budgets stop at \(\mathcal B\), cavity budgets at
\(2\mathcal B\); temporary full coordinate and response caps are
twice their claimed values and cavity caps four times. Full and cavity
pole stops are \(3a/8\) and \(7a/16\). The coordinate table
gives, on their common prefix,
\[
 \max|\Delta z|+\max|\Delta\bar k|\le n^{-1/30},\quad
 \max|\Delta\bar R|\le n^{-1/30},\quad
 \mathcal H_a^{-I}\le e^{2\eta n^{-1/30}}\mathcal H_a+p/n
                                    <2\mathcal B.
 \tag{IC.69}
\]
The local size, learned-row norm, and strip gates (IC.20), (IC.33)
hold because \(R\le3n^{-.08}\), \(P\le4n^{-.48}\), and
\(a^{-1}\le\beta/16\). Thus no cavity stop occurs first.

There is no exponential short-contour gate at (IC.63). The physical
coefficient bounds are \(\mathcal K\le\beta^{20L}\),
\(D_W\le\beta^{9L}\), \(U_*^{\rm fin}\le\beta^{72L}\),
and \(\lambda\le H_D^2\le\beta^{6L}\). With
\(c=[p\beta^{100L}(1+\lambda)]^{-1}\), each of
\[
 8c,\quad\lambda c,\quad4\mathcal Kc/\log2,
 \quad32YSD_Wc
\]
is below one for every \(n\ge1\). Follow a real solution to its
nearest real anchor and then at most two short pieces. Residual growth
is at most \(e^{4\mathcal Kr_t}\le2\), extra activity at most
\(8Yr_t\le S/2\), hidden normalized increments at most
\(8YSD_Wr_t\le1/4\), and, once the response cap is improved,
the preactivation displacement is at most
\[
 8YSU_*^{\rm fin}c\le a/8.
 \tag{IC.70}
\]
This improves the pole stop. It uses \(64YS=4\lambda S^2\)
and \(S\le1\), so no inverse label amplitude occurs.
The source rectangle therefore supplies exactly the decoder radius
\(\lambda r_t=[p\beta^{100L}(1+\lambda^{-1})\sqrt\ell]^{-1}\).
Using this source in a Taylor construction requires the corresponding
factor \(p\) in the number of time patches; it does not license
the former larger complex radius.

## 8. Initializing every cavity and improving the finite stops

Apply (IC.58) at failure \(\rho/32\). Gate (IC.66) implies
its sufficient envelope (IC.61), since the latter is at most
\(\mathcal A\ell\). Conditional initial Gaussian tails, before
conditioning on the current operator event, also give
\[
 Z_0=2H_D\sqrt{2\log(64nmL/\rho)}\le4H_D\sqrt\ell
 \tag{IC.71}
\]
as a simultaneous initial training-preactivation cap, with failure
at most \(\rho/32\). Initial exponential budgets are controlled
directly: \(\eta(2H_D)\le1\), so for a centered Gaussian with
standard deviation at most \(2H_D\),
\(\mathbb E e^{\eta|Z|}<4\) and
\(\mathbb E e^{2\eta|Z|}<15\). Conditional Chebyshev at layer
average eight gives failure \(15/(16n)\). The stopped layer/sample
union therefore bounds all initial budgets by \(8L\) with failure
at most \(15mL/(16n)<\rho/32\). Initial carriers are zero.
Gaussian norm concentration gives all initialized hidden rows/columns
norm at most two, with failure at most
\(4nLe^{-n/2}<\rho/32\); the first layer's incoming rows are
not needed for a reverse source and are excluded from this norm bound.

Delete at most \(p\) neurons at one layer. Zero-embedding its
rectangular features, the omitted initialized feature vector has norm
at most \(\sqrt p(b+sZ_0)\). Every subsequent initialized
feature difference has norm at most
\[
 D_{\rm init}=(8s)^L\sqrt p(b+sZ_0)
                \le\beta^{10L}\sqrt{p\ell}.
 \tag{IC.72}
\]
Restrictions do not increase initial operator norms. Gate (IC.66)
implies
\(D_{\rm init}/\sqrt n\le\min\{H_D/8,\sqrt\lambda/32\}\).
Thus each cavity starts with training feature RMS below \(3H_D/2\)
and least singular value of its normalized feature matrix at least
\((1/\sqrt2-1/32)\sqrt\lambda\). Under the unchanged label
condition its later feature-matrix motion is at most
\(\sqrt\lambda/8\), by the existing deterministic fitting
calculation. Its Gram gap stays strictly above \(\lambda/4\).
This proves the fitting tube for all cavities from one full initialization
event, without union-bounding a cavity Gram probability.
In particular (IC.58) is not applied literally to a rectangular cavity.
Its empirical norm, if estimated directly, would have mean-square factor
\((n-p)/n\), hence an RMS bias at most \(pH_D/n\). The
zero-embedded difference bound (IC.72) already includes the missing
coordinates themselves and dominates this bias. The strict RMS and Gram
margins above therefore pay for original normalization \(n\) without
any false claim that a cavity's empirical covariance has the full-network
expectation. The \(n^p\) multiplicity is used only in the coordinate
comparison (IC.73), with its exponential Gaussian tail.

For initial coordinate localization at a layer above the deletion,
condition on the lower initialized layers and project their complete
feature difference onto the deterministic ball of radius (IC.72).
The current row is still independent Gaussian, so each pairing has
variance at most \(D_{\rm init}^2/n\). At threshold
\(n^{-1/10}\) its tail is
\(2e^{-n^{4/5}/(2D_{\rm init}^2)}\). The union over deletion
sets and tests costs at most
\[
 2pmL^2n^{p+1}e^{-n^{4/5}/(2D_{\rm init}^2)}<\rho/32.
 \tag{IC.73}
\]
The negative exponent is at least \(n^{.799}/2\), while the
logarithm of the prefactor is at most \(10n^{1/4000}\ell\),
by (IC.68). At the deleted layer retained coordinates agree. Hence
each cavity starts with budget at most
\(e^{\eta n^{-1/10}}8L+p/n<\mathcal B/2\).
These initial failure allocations sum to less than \(\rho/4\).
Each cavity nevertheless uses its own initialization test (including
the just specified initial Gram margin), with the zero-reference
convention of Section 1. This is needed when the full initial-event
indicator is subsequently dropped.

On the local uniform event in Section 7, (IC.55) and the unchanged
scalar absorption (S.16) give
\[
 Z_{a,i}+K_{a,i}/S\le C_{\rm abs}
 [1+G_{h,a,i}+G_{\delta,a,i}/S+
                      \overline G_{h,i}+\overline G_{\delta,i}]
                       +n^{-1/40}.
 \tag{IC.74}
\]
Its coefficient remains the singleton coefficient, independent of the
moment order \(p\). Each Gaussian reference has coefficient RMS
at most \(V_*=\max(1,H_{\max},\tau_*)\). Its raw time
derivative costs \(\sqrt n\) times the proved coefficient and
a power of \(\ell\), so a mesh of size \(n^{-2}\) has vanishing
interpolation error and at most \(n^5\) points under (IC.66).
Use scalar grid threshold \(31V_*\sqrt\ell\), reserving
\(V_*\sqrt\ell\) for interpolation. Real/imaginary splitting
gives tail \(4e^{-31^2\ell/8}\). There are at most
\(\mathcal A n^6\) tests. Their union is below \(n^{-100}\).
Consequently (IC.74) improves the temporary full maxima to exactly
\[
 \max_{a,j,i}|z_{a,i}^{(j)}|\le K_{\rm src}\sqrt\ell,
 \qquad\max_{a,j,i}|k_{a,i}^{(j)}|
                          \le SK_{\rm src}\sqrt\ell.
 \tag{IC.75}
\]
Apply the explicit response contractions (IC.57) in increasing layer
order and use the Gaussian multiplier 64. The \(m^2\) driver/evaluated
training pairs and the same mesh have total additional failure below
\(n^{-100}\), and the response stops improve to
\[
 \max_{a,b,j,i}|R_{ba,i}^{(j)}|
                         \le S U_j^{\rm fin}\sqrt\ell.
 \tag{IC.76}
\]
The direct reverse mean here is explicitly
\(\bar\delta_{a,i}\operatorname{tr}(C_bC_a^\top)/n\);
its integrated term is (IC.56), and its cross forms are centered.
Thus this step includes the reverse observable instead of inferring a
response cap from a feature cap. Equations (IC.70), (IC.76) now improve
the full pole stop. Budget removal has not yet been invoked.

## 9. Finite-order common-cavity moments and collisions

We first state an elementary Gaussian rectangle estimate, including its
constants. If a deterministic complex coefficient map \(b_z\) on a
rectangle with sides at most \(H_0\) satisfies
\(\sup\|b_z\|\le D\) and
\(\|b_z-b_{z'}\|\le K\|z-z'\|\), then for a standard
real Gaussian vector \(G\),
\[
 X=\sup_z|G^\top b_z|,\quad
 M=256D\sqrt{\log(e+H_0K/D)},\quad
 \log\mathbb E e^{uX}\le uM+2u^2D^2.
 \tag{IC.77}
\]
If \(D=0\), interpret the process as zero. To prove the mean
bound, use dyadic meshes of size proportional to \(D2^{-j}/K\),
with at most \(4(1+H_0K/D)^2 4^j\) points. Connect each point
to the preceding mesh; increment standard deviations are at most
\(3D2^{-j}\). The bound
\(\mathbb E\max_{r\le N}|Z_r|\le\sigma\sqrt{2\log(2N)}\)
for Gaussian variables of standard deviation at most \(\sigma\)
follows by their exponential moments and a union bound. Summing uses
\(\sum2^{-j}=1\), \(\sum2^{-j}\sqrt j\le2\).
The constant 128 covers the real initial grid and increments; using
real and imaginary parts gives 256. The supremum is at most
\(2D\)-Lipschitz in \(G\), so (IC.59) proves its exponential
moment. For samplewise processes sharing the same root, their RMS
\(\bar X\) is also \(2D\)-Lipschitz, and
\(\mathbb E\bar X\le M+2D\) by the variance estimate.
Thus (IC.77) holds for the sample RMS with \(M\) replaced by
\(M+2D\), without independence between samples. For a root with
covariance \(I/n\), use coefficient norms divided by \(\sqrt n\).

For a set \(I\ni i\), both the singleton cavity and the common
\(I\)-cavity omit the particular root against which their difference
is paired. Their complete independently stopped coefficient paths,
including their own failed-initialization conventions, are independent
of that root. Project the whole difference path onto a deterministic
Euclidean ball of radius \(4n^{1/100}\), before restricting to the
successful full prefix. Projection is nonexpansive, preserves root
independence, and agrees with the difference on that prefix by the
\(2n^{1/100}\) comparison proved above. Its normalized Gaussian
radius is
\[
 v_n=4n^{-49/100}.
\]
The raw normalized derivative recurrences give rectangle modulus at
most \(\beta^{300L}(1+\lambda)\ell^3\); its side length is
at most \((64/\lambda+4)\ell\). Applying (IC.77), and its
RMS version, to the sum of the two cavity moduli yields
\[
 \log\mathbb E e^{uE_i}\le u\mu_n+2u^2v_n^2,
 \quad\mu_n\le256v_n\sqrt{\log\left(e+
 {\beta^{400L}(1+\lambda^{-1})\ell^4\over v_n}\right)}+2v_n.
 \tag{IC.78}
\]
The two cavity paths need not be independent of each other. Equations
(IC.66)--(IC.68) imply
\[
 p\mu_n+p^2v_n^2
 \le1032n^{-.48975}\sqrt\ell+16n^{-.9795}<10^{-3}.
 \tag{IC.79}
\]

We also need finite moments for complex-minus-real corrections, rather
than a limit at fixed moment degree. The sharp derivative calculation
in S.7, now using (IC.76), gives
\[
 \|\partial_t\delta_a^{(j)}\|_{2,n}
 \le J\rho\left[1+{S^2\over\eta}
                       (4+\log(2\mathcal B)+\log\ell)\right],
 \qquad J=\beta^{80L}.
 \tag{IC.80}
\]
To see that the constant is finite with this power, interpolate the
RMS and maximum bounds on \(\dot z\), then use the carrier
Schatten bound at real exponent
\(r=\max\{4,\log(2\mathcal B\ell)\}\). The product
\(k\odot\dot z\) is at most
\((2\rho S^2N_*/\eta)r(2\mathcal B\ell)^{1/r}\) in RMS,
where \(N_*\le\beta^{72L}\). The last exponential is at most
\(e\). Differentiate the backward pass: the propagated upper
derivative costs \(10s\), changed mixer costs
\(2s^3k_{j+1}^2H_j\), and changed gate costs \(4et_2N_*\).
Each forcing coefficient is at most \(\beta^{75L}\), and its
geometric sum at most \(\beta^{78L}\). Enlarging to \(J\)
also pays for the forward derivative and fixed contour factors.
This proves (IC.80) for every width, retaining the fixed budget
logarithm instead of assuming it is below \(\log\ell\).

Call the bracket in (IC.80) \(A_\ell\). The unchanged condition
\(S^2\Lambda/\eta\le1\) gives
\(A_\ell\le8[1+\log(e+\ell)]\). Subtract the coefficient
at the nearest real anchor. With \(c\) from Section 7, its
normalized radius, Lipschitz coefficient, and rectangle side are bounded by
\[
 D={\lambda cJ A_\ell\over\sqrt\ell},\quad
 K=\lambda J A_\ell,\quad
 H_0=64\ell/\lambda+4c/\sqrt\ell.
 \tag{IC.81}
\]
These bounds also hold after a reference's own clamping; the nearest
real-anchor map is Lipschitz. Set \(r=\lambda^{-1}\) only in the
following arithmetic. Then
\[
 D\le{\beta^{-20L}\over p(1+r)}{A_\ell\over\sqrt\ell},
 \quad H_0K/D=64p\beta^{100L}(1+r)\ell^{3/2}+4,
 \quad D\le32\beta^{-20L}/p.
\]
The logarithm in (IC.77) is at most
\(6+100L\log\beta+\log p+\log(1+r)+2\log(e+\ell)\).
Use \((2+u)e^{-u/2}\le2\) and
\((2+u)^{3/2}e^{-u/2}\le4\) for \(u=\log\ell\ge0\),
\(\sqrt{\log p}/p\le1\), and
\(\sqrt{\log(1+r)}/(1+r)\le1\).
Substitution gives \(M+2D\le2^{16}\beta^{-18L}\). Therefore
for a complex-minus-real correction \(X\), including its sample RMS,
\[
 (\mathbb E e^{apX})^{1/p}
 \le\exp\{a2^{16}\beta^{-18L}+2^{11}a^2\beta^{-40L}/p\}
 \le e^{\beta^{-10L}},\qquad0\le a\le8.
 \tag{IC.82}
\]
This holds at every width for the stopped references. It is why the
factor \(p\) in (IC.63) suffices without an exponential width in
the moment order or the inverse gap.

On the common cavity, the real Gaussian references have the squared
exponential bound (S.20), including the sample RMS form. Completing the
square and Hölder for the four references in (IC.74) give a main
one-neuron exponential moment below four at exponent at most \(8\eta\),
exactly as in (S.21). Distinct omitted root pairs are conditionally
independent on that common cavity. Bound each full singleton by its
common-cavity real reference plus the projected correction (IC.78)
and complex correction (IC.82), then drop the event indicator from
these nonnegative bounds. Cauchy--Schwarz separates the product of main
references from all corrections. Hölder over the at most \(p\) roots
and four reference families pays for the corrections: their required
coefficient is at most eight because
\(\eta C_{\rm abs}\le(1024W_{\rm G})^{-1}\).
Equation (IC.79) makes the projected factor smaller than
\(e^{1/10}\), (IC.82) makes the complex factor smaller than
\(e^{1/10}\), and the scalar error in (IC.74) contributes less
than \(e^{1/10}\). These margins are per root; together with the
main bound below four they are below sixteen. Thus, with \(E\)
the common initialization, local and maximum event,
\[
 \mathbb E\left[1_E\prod_{i\in I}
 e^{\eta(Z_{a,i}^{(j)}+K_{a,i}^{(j)}/S)}\right]\le16^{|I|},
 \qquad1\le|I|\le p.
 \tag{IC.83}
\]
At no point was \(E\), or full survival, a Gaussian conditioning
event. Samples and correction processes have not been assumed independent.

Repeated indices require separate treatment. The unchanged constants
obey
\[
 2\eta K_{\rm src}\le{1+C_G\over32W_{\rm G}}
                  \le33/4096<1/100.
\]
Indeed \(W_{\rm G}\ge128\max(1,H_{\max},\tau_*)\), since
\(V_1=\tau_1=\max_j\tau_j\). On (IC.75), put
\(B_i=e^{\eta(Z_{a,i}^{(j)}+K_{a,i}^{(j)}/S)}\); then
\[
 0\le B_i\le e^{\sqrt\ell/100}\le e^{1/100}n^{1/100}=W_n.
 \tag{IC.84}
\]
Expand \((n^{-1}\sum_i B_i)^p\). For a partition of its ordered
positions into \(k\) equal-index blocks, retain one factor per
distinct index and bound the repeated factors by \(W_n^{p-k}\).
The retained expectation is at most \(16^k\) by (IC.83), and
there are at most \(n^k\) distinct index assignments. Partitions
with \(j=p-k\) identifications are at most
\(\binom{\binom p2}{j}\): map each block to the star joining
its least position to all others; the resulting \(j\) edges
determine the partition. Consequently
\[
 \mathbb E[1_E(n^{-1}\sum_iB_i)^p]
 \le16^p\exp\{\tbinom p2 W_n/(16n)\}\le e16^p,
 \tag{IC.85}
\]
where \(n\ge4p^3\), implied by (IC.68), suffices for the last
inequality. This does not request an exponential moment at coefficient
\(p\eta\) of a repeated main root.

If any full budget reaches \(\mathcal B\), some sample/layer
average reaches \(\mathcal B/L\). Markov and the \(mL\)
union give
\[
 \Pr(\hbox{a budget is hit},E)
 \le emL(16L/\mathcal B)^p
 =emL(64e^2)^{-p}\le\rho/4.
 \tag{IC.86}
\]
Initialization costs less than \(\rho/4\), the local event less
than \(\rho/16\), and the two maximum events together cost
\(2n^{-100}<\rho/16\). All stops are therefore removed with
total failure less than \(\rho\). Their strict margins give
holomorphy on a neighborhood of the closed rectangle (IC.63).
The original RMS and operator bounds, (IC.75)--(IC.76), the real
fitting trajectory and endpoint all hold on this event.

For the Logarithmic decoder, use \(\rho=2^{-20}\delta\) and
\(p=p_{\rm ref}\) for the independent dense reference. A constructed
member uses \(\rho=2^{-20}\), giving the stated implemented order
\(p\) independent of \(\delta\). The reference gate dominates
the member gate because both \(p\) and \(\rho^{-1}\) are
larger for the reference. Whole-experiment amplification, proved in
the decoder section, pays for member failure. It is not a union-bound
requirement that every member source succeed. Substitution in (IC.67)
and its envelope gives exactly
\[
 n\ge\left\lceil\left[
 {2^{20}\beta^{2000L}\over\delta}
 (1+m/\gamma)^4(m+d+p_{\rm ref}+1)^4
 \right]^{1100}\right\rceil.
 \tag{IC.87}
\]
Additional numerical-precision or decoder-work gates remain their
separately stated conditions. In particular this source proof does not
remove a separately chosen \(n\ge Y^{-1}\) precision convention,
and it imposes no positive lower label bound of its own.

The independent dense-reference certificate also follows from this
training-only source, with no qualitative complex-sphere event. Here is
the exact bridge. Put \(T_0=32\ell/\lambda\) and define
\[
 C_L^k=1,\qquad
 C_j^k=S\tau_{j+1}+10sC_{j+1}^k
                +10t_2SP_{j+1}k_{j+1},\qquad
 C_{\rm carrier}=\max_j C_j^k.
 \tag{IC.88}
\]
For two real states in the physical operator/RMS tube, forward
subtraction bounds a preactivation RMS difference by
\(P_j\|\Delta\theta\|_{\rm par}\). In the backward subtraction,
the changed mixer costs \(S\tau_{j+1}\|\Delta\theta\|_{\rm par}\),
propagation costs \(10s\), and the changed gate costs
\(10t_2SP_{j+1}k_{j+1}\sqrt n\|\Delta\theta\|_{\rm par}\).
The first \(\sqrt n\) is the preactivation coordinate conversion;
after the final carrier coordinate conversion this gives
\[
 \max_{a,j}\|k_a^{(j)}(t)-k_a^{(j)}(T_0)\|_\infty
 \le C_{\rm carrier} n\|\theta(t)-\theta(T_0)\|_{\rm par}.
\]
Apply the real fitting energy/path-length inequality starting at \(T_0\):
the rightmost parameter difference is at most
\(2\rho(T_0)/\sqrt\lambda\le2Y(en)^{-16}/\sqrt\lambda\).
Consequently the exact sufficient carrier-tail gate is
\[
 {2C_{\rm carrier}Y\over\sqrt\lambda}\,n(en)^{-16}
                    \le K_{\rm src}S\sqrt\ell.
 \tag{IC.89}
\]
It is implied by
\[
 n\ge\max\left\{1,
 \left({C_{\rm carrier}\sqrt\lambda\over8K_{\rm src}}\right)^{1/15}
 \right\}
 \quad\text{and hence by}\quad
 n\ge\max\{1,(\beta^{23L}/8)^{1/15}\}.
 \tag{IC.90}
\]
Indeed \(S=16Y/\lambda\), \(K_{\rm src}\ge1\),
\(C_{\rm carrier}\le\beta^{20L}\) by (IC.88)'s single
geometric sum, and \(\sqrt\lambda\le\beta^{3L}\). Gate
(IC.87) dominates (IC.90). Adding (IC.75) at \(T_0\) gives
the exact all-time training-carrier bound used in dense comparison,
\(M_n=2K_{\rm src}S\sqrt\ell\), also at the fitted endpoint.

Define the real dense good set by the fitting operator/RMS/Gram tube,
its endpoint tail, and this training-carrier bound. Its definition is
independent of \(p\), the complex radius, and confidence. Both the
fixed-confidence members and the high-confidence independent reference
belong to that same set on their respective source events. The dense
endpoint-subtraction proof uses coordinate carrier maxima only for
training samples: its arbitrary-query step is forward RMS subtraction
in the real operator tube. Its Gaussian extension then uses a real
sphere net, a real compactified-time grid, and the real fitting tail.
Thus the signed dense Lipschitz constant, its common extension center,
and the whole-sphere/all-time certificate \(B_n\) are unchanged
when this finite-training event replaces the original qualitative
source event. No analyticity or carrier maximum at passive complex
queries is a hypothesis of that comparison. This explicitly closes
the reference-event dependency of the Logarithmic decoder.

## 10. Integration and provenance

Sections 1--5 replace the existing local-comparison proof and supply its
passive-query and S.15 trace calculations. The existing S.5--S.8
real-activity, scalar absorption, qualitative moment-limit and query-tube
arguments may then use the proved fixed-parameter local theorem. For
that qualitative source, first fix a deletion count, send width to
infinity, and only then take the infimum over fixed moment degrees.
Neither the shrinking finite-training radius nor (IC.87) is asserted
for its entire complex sphere tube.

Sections 6--9 replace `The finite source event` in the Logarithmic
proof. Section 6 should also be linked from the explicit Logarithmic
source-width inventory, because its exponential-concentration gate is
essential to the displayed polynomial dimension dependence. The older
Chebyshev fitting gate remains a valid sufficient condition for results
that use it; it is not the gate used for (IC.87).

Scientific inputs read completely were the relevant RESULT source
foundation/probabilistic sections and the following explicitly authorized
decoder dependencies: `FIXED_ORDER_INSERTION_JETS.md`,
`SCALED_INSERTION_REMAINDER.md`, `INSERTION_MAP_MODULI.md`,
`QUANTITATIVE_INSERTION_WIDTH.md`, `FULL_FINITE_SOURCE_PROBABILITY.md`,
`FINITE_COMPLEX_MOMENT_GATE.md`, `POLYNOMIAL_SOURCE_WIDTH.md`,
`WIDTH_GATE_REFINEMENT.md`, `CONFIDENCE_SEPARATION_REFINEMENT.md`,
and, after the supervisor's explicit scope extension,
`EXPLICIT_FITTING_WIDTH.md`. The current RESULT dense-fitting definitions
were also read. Links from those inputs to other studies or review
reports were not followed. Canonical-notation, neural-network notation,
and rigorous-proof instructions were read and applied. Only this fragment
was written; no Git operation or experiment was performed.

This is a candidate complete author proof for the assigned source
interfaces, requiring fresh independent checking before integration can
be represented as independently verified. It makes no claim that the
downstream decoder arithmetic or finite generator has been proved by
this fragment.
