# Retaining small activity in the corrected-readout runtime

2026-10-04. Collaborative bounded refinement suggested by the coordinator,
not an independent review. The source theorem, canonical ordinary-tanh
reference, corrected-readout optimizer, physical clock, and coordinate
tolerance are unchanged. This derives sharper finite deterministic
constants from their existing comparison inequalities. No experiment,
other-study read, Git operation, or maintained-book change was made.
The numerical work evaluates deterministic recurrences only.

At hidden depth two, the full explicit source label coefficient
\(c_{\rm src}=2.857680896\ldots\,10^{-7}\) is retained, and the improved
error coefficient evaluates to \(271420.3955\ldots\), instead of
\(1.6438\ldots\,10^{24}\) at the older joint cap
\(4.7559\ldots\,10^{-16}\). A conservative certified coefficient
\(2.8\,10^5\) is proved below. These are sufficient existence estimates;
the width threshold, preprocessing cost, precision, and inverse-gap
dependence remain unchanged and unquantified where they previously were.

Complete inputs are EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md,
ACTIVATION_CONSTANTS_REFINEMENT_ROUTE.md (frozen SHA-256
407f0b1079c7f65dd09960bc45c78a4f266c30054585c9aa9df8b7ab61859660),
STORAGE_QUADRATIC_IMPROVEMENT.md, and the same-study source/label
dependencies already read for the preceding checks. No sibling review is
an input. Canonical-notation and neural conventions, rigorous-proof, and
research-audit instructions were applied. A scoped subagent independently
derived the error-system algebra in Section 4 from the complete explicit
runtime input and the sharper layer inequality supplied here. Its
damping allocation was then reconstructed in this note.

## 1. Reference, source interface, and an explicit cap

For \(v=x/\sqrt d\in S^{d-1}\), the reference is
\[
z^{(1)}=Av,\qquad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
h^{(\ell)}=\tanh z^{(\ell)},\qquad f_n=w^\top h^{(L)}/n.
\]
Initialization and mean-square-loss mobilities are the canonical Gaussian
ones and \((n,1,\ldots,1,n)\), with zero initial readout. Set
\(\gamma=\lambda_{\min}(Q^{(L)})>0\) for the initialized limiting
feature covariance, \(\lambda=\gamma/m\le1\),
\(Y=\|y\|_2/\sqrt m\), \(u=Y/\lambda\), and
\(\alpha=Y/\sqrt\lambda=u\sqrt\lambda\).

The source interface is exactly the finite construction in the frozen
activation refinement: initial mixer cap \(K_0=7/2\), real tube
\(R=15/4\), fixed metric \(D/4\preceq H\preceq D\),
coordinate approximation error \(\epsilon=n^{-1}\le Y\) for each paired
member, exact initialized feature/image inclusion, and
\[
\max_{a,\ell,i,t\le T}|k_{a,i}^{(\ell)}(t)|
 \le16K_{\rm src}u\sqrt{\ell_n},\qquad
\ell_n=\log(en),\quad T=32\lambda^{-1}\ell_n.
\tag{1}
\]
The carrier itself, without an added one, appears in (1).
For ordinary tanh the source recurrence gives
\[
K_{\rm src}=64s(4s)^{L-1},\qquad s=16/15.
\]
Its finite source cap \(c_{\rm src}\) is exactly equations (3)--(4) of
ACTIVATION_CONSTANTS_REFINEMENT_ROUTE.md. Its dimension-independent
angular and time caps \(c_{\rm ang},c_{\rm time}\) are exactly equation
(14) there. These are specified source recurrences, not new unknown
constants.

Define the following runtime constants before choosing the cap:
\[
h=g=2,\quad q=gR=15/2,\quad
\beta_\ell=gq^{L-\ell},\quad \beta=\max_\ell\beta_\ell,\quad
U=\left(\beta_1^2+h^2\sum_{\ell=2}^L\beta_\ell^2\right)^{1/2},
\]
\[
F_1=g,\quad F_\ell=g(h+RF_{\ell-1}),\quad F=\max_\ell F_\ell,
\]
\[
D_\delta=3\beta+3,\quad W=64,\quad
J_0=h\sqrt L(7\beta+3),\quad V_0=14FU,
\]
\[
P_h=17,\quad P_\delta=18\beta+11,\quad D_r=8P_h,\quad
c_{\rm rt}=\min\{1,(224FU)^{-1/2},(6J_0)^{-1}\}.
\tag{2}
\]
Choose once, independently of width and labels,
\[
c=\min\{c_{\rm src},c_{\rm rt},c_{\rm ang},c_{\rm time}\},
\qquad 0<u\le c.
\tag{3}
\]
The last two entries keep the improved source-radius and storage
formulas. They may be omitted if only the earlier source construction
is desired. Unlike the preceding activation refinement, (3) does not
include \(C_1^{-1}\) or \(C_2^{-1/2}\). The coefficient computed below
retains its complete finite exponential instead.

The source and independent runtime fitting proofs give
\[
\int\rho_n,\int\rho_C\le4u,\quad
\|w_R\|\le W\alpha,\quad
\|\mathcal J_C\|,\|\mathcal J_R\|\le J_0\alpha,
\quad \int\nu\le(W/2)\alpha,
\quad \|\dot V_C\|\le V_0\alpha\rho_C.
\tag{4}
\]
Here \(\rho_n,\rho_C\) are residual RMS norms,
\(V_C,V_R\) are normalized training-feature operators,
\(\nu=\|V_Rc_n/\sqrt m\|\), and \(\mathcal J_C,\mathcal J_R\)
are the normalized hidden update-direction operators from the exact
runtime proof. All neuron norms use its fixed metrics. The reference
state is a proof object; it is not supplied to the autonomous runtime.

## 2. Learned source defects and the exact readout coefficients

The learned forward and reverse action errors are respectively
\(8D_\delta P_hu\alpha\epsilon\) and
\(8hP_\delta u\alpha\epsilon\). Since \(u\alpha\le c^2\), set
\[
A_0=1+2(K_0+1)+8c^2(D_\delta P_h+hP_\delta),\qquad
C_f=F(1+A_0).
\tag{5}
\]
The initialized defect remains \(2(K_0+1)\epsilon\); it is not scaled
by the activity. Forward subtraction still proves
\[
\|\Delta z\|,\ \|\Delta h\|,\ \|V_C-V_R\|
\le C_f(a+\epsilon),
\tag{6}
\]
where \(a\) is the hidden-parameter tuple error in the direct-sum
first-weight and mixer Hilbert--Schmidt norm. Here \(g\ge1\), so the
same envelope covers both preactivations and features.

Write the negative residual vectors as \(c_n=y-f_n\) and \(c_C=y-f_C\),
and define
\[
e=(c_C-c_n)/\sqrt m,\quad
T_C=V_C(V_C^*V_C)^{-1},\quad P_C=T_CV_C^*,\quad p=T_Ce,
\]
\[
z=w_C-w_R,\quad \zeta=z+p,\quad
b=\|p\|+\|\zeta\|,\quad E=a+b,\quad r=\epsilon/\sqrt\lambda.
\]
A star denotes the appropriate Hilbert adjoint. The exact readout identity is
\[
\eta:=\widehat w_C-w_R
=(I-P_C)\zeta-p-T_C(V_C-V_R)^*w_R-T_Cd_R,
\]
where \(d_R=V_R^*w_R-(y-c_n)/\sqrt m\) and
\(\|d_R\|\le D_ru\epsilon\). Since
\(\|T_C\|\le3/\sqrt\lambda\), it gives
\[
\|\eta\|\le b+uA_r(a+\epsilon)+uB_r r,\qquad
A_r=3WC_f,\quad B_r=3D_r.
\tag{7}
\]
In particular the coefficient of \(b\) is one. No condition involving
an artificial common readout envelope is required.

The source-only normalized Gram defect also retains its original powers:
\[
\|D\|\le D(c)\epsilon,\qquad
D(c)=P_h+L(P_\delta h^2c+9\beta^2P_hc^2).
\tag{8}
\]
This follows from the source proof's response-pair error
\(P_\delta\alpha\epsilon\) and dense response pairing
\(9\beta^2\alpha^2\), using \(\alpha\le u\le c\).

## 3. Backward propagation with its separate forcing terms

Set \(X_L=Y_L=0,\ Z_L=gC_f\), and descend by
\[
X_\ell=qX_{\ell+1}+gD_\delta,\quad
Y_\ell=qY_{\ell+1}+gA_0,\quad
Z_\ell=qZ_{\ell+1}+gC_f.
\tag{9}
\]
The exact subtraction, with the changed gate multiplying the actual
reference carrier, gives
\[
\|\Delta\delta^{(\ell)}\|
\le\beta_\ell\|\eta\|+X_\ell\alpha a+Y_\ell\epsilon
 +Z_\ell(16K_{\rm src}u\sqrt{\ell_n})(a+\epsilon).
\tag{10}
\]
The four terms are the terminal readout error, changed mixer, reverse
source defect, and changed gate. The last gate Lipschitz coefficient is
at most two in the fixed metric, since the real tanh curvature is at
most one. Every forcing in (9) is propagated once through the actual
finite recurrence.

For a layer array \(v_\ell\), write
\[
\mathcal N(v)=\left(v_1^2+h^2\sum_{\ell=2}^Lv_\ell^2\right)^{1/2},
\quad \bar X=\mathcal N(X),\quad
\bar Y=\mathcal N(Y),\quad \bar Z=\mathcal N(Z).
\]
The hidden update-direction subtraction has a response difference
multiplied by a compressed feature, plus a reference response multiplied
by a feature difference. Minkowski's inequality in the parameter tuple,
followed by the RMS bound on normalized sample columns, therefore gives
\[
\|\Delta\mathcal J\|
\le U\|\eta\|+\bar X\alpha a+\bar Y\epsilon
 +16K_{\rm src}\bar Z u\sqrt{\ell_n}(a+\epsilon)
 +D_\delta C_f\sqrt{L-1}\,\alpha(a+\epsilon).
\]
Using (7), \(\alpha\le u\), and \(\epsilon\le r\), define
\[
E_a=UA_r+\bar X+D_\delta C_f\sqrt{L-1},\qquad
E_q=16K_{\rm src}\bar Z.
\]
Then, with \(\chi=\sqrt{\ell_n}\),
\[
\|\Delta\mathcal J\|
\le Ub+u(E_a+E_q\chi)(a+\epsilon)+(\bar Y+uUB_r)r.
\tag{11}
\]
This retains the actual carrier's factor \(u\). No coordinate bound
on the compressed carrier is used.

## 4. Spend the lifted damping once

The exact normalized Gram decomposition from the runtime proof gives
the lifted forcing estimate
\[
\mathscr F\le
\left(2C_f\rho_n+\frac{6C_f\nu}{\sqrt\lambda}\right)(a+\epsilon)
 +12J_0u\rho_n\|\Delta\mathcal J\|+6D(c)\rho_n r.
\tag{12}
\]
Put \(T'=6V_0\), \(P=\|p\|\), \(\rho_e=\|e\|\), and
\[
I(t)=\int_0^t[T'u\rho_CP+\mathscr F]\,ds,\qquad
Z(t)=\int_0^t\rho_e^2/P\,ds,\qquad
\kappa=2-18J_0^2u^2.
\]
The quotient is zero where \(P=\rho_e=0\); norm regularization supplies
the integrated inequality there. The lifted residual energy proves
\[
P+\kappa Z\le I,\qquad
\int_0^t\rho_e\,ds\le3Z/\sqrt\lambda,
\tag{13}
\]
where the latter uses \(P\le3\rho_e/\sqrt\lambda\).

Readout cancellation and hidden-state subtraction give respectively
\[
b\le P+I+18J_0^2u^2Z
       +2C_f\int_0^t\rho_n(a+\epsilon),
\quad
a\le6J_0uZ+2\int_0^t\rho_n\|\Delta\mathcal J\|.
\]
For \(v=6J_0u\le1\),
\(18J_0^2u^2+6J_0u=v^2/2+v\le2-v^2/2=\kappa\).
Combining the two inequalities with (13), rather than bounding \(P\)
and \(Z\) separately, yields
\[
E\le2I+2C_f\int_0^t\rho_n(a+\epsilon)
            +2\int_0^t\rho_n\|\Delta\mathcal J\|.
\tag{14}
\]

Let \(g_u=2+24J_0u\). Substitution of (11)--(12) into (14) gives
\[
E(t)\le\int_0^t[L_a a+L_b b+r(\sqrt\lambda L_a+L_r)]\,ds,
\]
where
\[
L_a=[6C_f+g_u u(E_a+E_q\chi)]\rho_n
                       +12C_f\nu/\sqrt\lambda,
\quad
L_b=g_uU\rho_n+2T'u\rho_C,
\]
\[
L_r=[g_u(\bar Y+uUB_r)+12D(c)]\rho_n.
\tag{15}
\]
All coefficients are nonnegative. With \(k=\max(L_a,L_b)\) and
\(f=\sqrt\lambda L_a+L_r\), the integral majorant and an integrating
factor give
\[
E(t)\le r\int_0^t f(s)\exp\!\left(\int_s^t k(\tau)\,d\tau\right)ds.
\tag{16}
\]
The source Gram defect is a forcing coefficient, not an exponential
coefficient.

Define the following finite numbers, all evaluated at the chosen cap:
\[
g_c=2+24J_0c,\qquad
A=4\max\{6C_f+g_ccE_a,g_cU\}+6C_fW+8T'c,
\]
\[
B_{\exp}=4g_cE_q,\qquad
F_{\rm src}=24C_f+4g_ccE_a+6C_fW
             +4g_c(\bar Y+cUB_r)+48D(c).
\tag{17}
\]
Using (4), \(\lambda\le1\), and \(u\le c\), one obtains
\[
\int k\le Au+B_{\exp}u^2\chi,\qquad
\int f\le u(F_{\rm src}+B_{\exp}u\chi).
\]
Thus
\[
E(t)\le ur(F_{\rm src}+B_{\exp}u\chi)
                 e^{Au+B_{\exp}u^2\chi}.
\tag{18}
\]
No coefficient in (17) has been transferred into the width threshold.

## 5. Query output and the fitted endpoint

The direct query decomposition uses (7) and the source pairing defect:
\[
|f_C-f_n|
\le hb+WC_fu(3h+\sqrt\lambda)(a+\epsilon)
                    +D_ru(3h+\sqrt\lambda)r.
\]
Define
\[
O=\max\{h,WC_fc(3h+1)\},\qquad
R_{\rm out}=(3h+1)(WC_f+D_r).
\]
Then on the source horizon,
\[
|f_C-f_n|\le ur\left[
R_{\rm out}+O(F_{\rm src}+B_{\exp}u\chi)
                     e^{Au+B_{\exp}u^2\chi}\right].
\tag{19}
\]
Since \(\epsilon=n^{-1}\) and
\(n^{-1/2}=\sqrt e\,e^{-\chi^2/2}\), the elementary inequalities
\[
B_{\exp}c^2\chi\le\chi^2/4+B_{\exp}^2c^4,\qquad
\sup_{\chi\ge0}\chi e^{-\chi^2/4}=\sqrt{2/e}
\]
give the complete finite-horizon coefficient
\[
C_{\rm finite}
=R_{\rm out}
 +O(\sqrt e\,F_{\rm src}+\sqrt2\,B_{\exp}c)
                  e^{Ac+B_{\exp}^2c^4}.
\tag{20}
\]
It multiplies \(Y/(\lambda^{3/2}\sqrt n)\).

The tail constants can also retain activity. Differentiating the exact
readout, use
\(\|\dot P_C\|\le6\lambda^{-1/2}\|\dot V_C\|\),
\(\|\dot T_C\|\le16\lambda^{-1}\|\dot V_C\|\),
\(\|w_C\|\le3\alpha\), and
\(\|\dot c_C\|_m\le2(h^2+J_0^2\alpha^2)\rho_C\).
The projection and inverse motion terms sum to
\(50V_0u^2\sqrt\lambda\,\rho_C\), rather than a coefficient
independent of activity. Hence define
\[
W_{\rm tail}=2h+6h^2+(50V_0+6J_0^2)c^2,\qquad
T_{\rm tail}=hW_{\rm tail}+7V_0c^2.
\tag{21}
\]
The corrected prediction speed is at most
\(T_{\rm tail}\lambda^{-1/2}\rho_C\).
The dense speed is at most \((2+3V_0c^2)\rho_n\), which is smaller
than the same bound. Each tail is consequently at most
\(4T_{\rm tail}Y\lambda^{-3/2}e^{-\lambda t/4}\).
At the actual source horizon \(T=32\lambda^{-1}\ell_n\), both tails
together add at most
\[
8T_{\rm tail}e^{-8}\frac{Y}{\lambda^{3/2}\sqrt n},
\]
because \(n^{-8}\le n^{-1/2}\). Thus the all-time statement, including
the endpoint, has coefficient
\[
C_{\rm all}=C_{\rm finite}+8T_{\rm tail}e^{-8}.
\tag{22}
\]

A simple optional specialization improves (20). If
\[
B_{\exp}c^2+\frac{B_{\exp}c}{F_{\rm src}+B_{\exp}c}\le1,
\tag{23}
\]
the logarithmic derivative of
\((F_{\rm src}+B_{\exp}c\chi)
e^{B_{\exp}c^2\chi-\chi^2/2}\) is nonpositive for \(\chi\ge1\).
Its maximum is therefore at one. Equations (20)--(22) may then use
the smaller explicit coefficient
\[
C_{\rm all}^{(1)}
=R_{\rm out}+O(F_{\rm src}+B_{\exp}c)
                 e^{Ac+B_{\exp}c^2}+8T_{\rm tail}e^{-8}.
\tag{24}
\]
This maximizes over all \(n\ge1\); it imposes no additional width
threshold to discard a structural coefficient.

## 6. Depth-two certificate and deterministic diagnostics

At \(L=2\), exact preliminary values are
\[
\beta=15,\quad U=\sqrt{241},\quad F=19,\quad
D_\delta=48,\quad J_0=216\sqrt2,\quad
V_0=266\sqrt{241},\quad K_{\rm src}=65536/225.
\]
Equation (5) gives \(A_0=10+11024c^2\).
The source cap is the minimum in (3): the other three bounds are
larger. For a conservative elementary verification it suffices to
check the old source recurrences at \(u=3\,10^{-7}\):
the runtime, angular, and time restrictions all hold there, whereas
\(c_{\rm src}<3\,10^{-7}\). The latter follows already from the
feedback entry of its source minimum. Indeed
\[
A_H=57032/225,\quad H_2=64712/225,\quad D_H=4,\quad
D_0>1.8\,10^6,\quad D_1>737280,\quad \mathcal B>944,
\]
using \(e^2>7.38,e^3>20\). Thus
\[
c_{\rm src}\le\frac1{16}
[(1.8\,10^6)^{-2}/(737280\cdot944)]^{1/4}<3\,10^{-7}.
\]
The inequalities \(u\le c_{\rm ang},c_{\rm time}\) at
\(3\,10^{-7}\) follow by substituting their finite rational source
coefficients; conservatively \(c_{\rm ang}>2\,10^{-5}\) and
\(c_{\rm time}>1.3\,10^{-6}\). Their calculations use only the
source endpoint recurrences, not the budget exponent.

For every \(c\le3\,10^{-7}\), elementary bounds on (5)--(21) give
\[
C_f<210,\quad E_a<656000,\quad E_q<1.767\,10^7,\quad
D(c)<17.001,\quad g_c<2.003,
\]
\[
A<85700,\quad B_{\exp}<1.42\,10^8,\quad
F_{\rm src}<86700,\quad O=2,\quad
R_{\rm out}<95032,\quad T_{\rm tail}<56.000001.
\]
For (23), \(F_{\rm src}\ge24C_f\ge5016\), so its left side is
less than \(1.278\,10^{-5}+42.6/5016<1\).
Also \(Ac+B_{\exp}c^2<0.026\), and \(e^{0.026}<1.027\).
Substitution in (24) gives \(C_{\rm all}^{(1)}<2.8\,10^5\).
Consequently the complete explicit depth-two certificate is
\[
0<Y\le c_{\rm src}\frac{\gamma}{m}
\quad\Longrightarrow\quad
\sup_{t\in[0,\infty],\,\|x\|=\sqrt d}|f_C-f_n|
\le2.8\,10^5\,Y(m/\gamma)^{3/2}n^{-1/2}.
\tag{25}
\]
It keeps the refined activation route's source rank and storage bounds.

The following are rounded deterministic evaluations of the exact
recurrences, not certified floating-point upper bounds. For these three
depths the minimum (3) equals \(c_{\rm src}\), and (23) holds.

| \(L\) | cap \(c\) | \(A\) | \(B_{\exp}\) | \(F_{\rm src}\) | \(C_{\rm all}^{(1)}\) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | \(2.857680896\,10^{-7}\) | \(8.527350548\,10^4\) | \(1.362254601\,10^8\) | \(8.624966178\,10^4\) | \(2.714203955\,10^5\) |
| 3 | \(1.138046480\,10^{-9}\) | \(6.574923484\,10^5\) | \(3.433848257\,10^{10}\) | \(6.597055293\,10^5\) | \(2.043381111\,10^6\) |
| 5 | \(3.567411493\,10^{-14}\) | \(3.713651703\,10^7\) | \(1.992911443\,10^{15}\) | \(3.721794941\,10^7\) | \(1.152144438\,10^8\) |

At depth two the more detailed values are
\(C_f=209.0000000171\), \(R_{\rm out}=94584.00000766\),
\(T_{\rm tail}=56.0000001275\),
\(Ac+B_{\exp}c^2=0.0243795714\ldots\), and \(O=2\).
The endpoint coefficient contributes about \(0.1502873\).
The main remaining terms are the direct query source-error coefficient
and the finite lifted forcing, not a large comparison exponential.

## 7. Scope and reproducibility

The general cap is the explicit minimum (3); no claim that the source
cap is always its smallest entry is needed. Equations (2), (5),
(8)--(9), (17), and (20)--(22) give an evaluable all-depth runtime
coefficient. Formula (24) is used only when its displayed condition
holds. No source approximation was differentiated or made more accurate.

The reductions are algebraic: preserve \(u\alpha\) in learned actions;
preserve the unit readout-error coefficient; use the actual carrier
bound without an added one; separate backward forcing terms; retain
\(\alpha,\alpha^2\) in the source Gram defect; spend the damping once;
keep source defects out of the exponent; and retain \(u^2\) in endpoint
speeds. They change no optimizer or reference dynamics.

The embedded evaluator in the frozen activation candidate supplies
\(c_{\rm src},c_{\rm ang},c_{\rm time},K_{\rm src}\). The diagnostic
calculation then evaluates this note's displayed recurrences directly
with ordinary Python floating-point arithmetic. Independent rational
depth-two reductions and the explicit inequalities preceding (25)
supply its conservative certified coefficient. The source candidate's
earlier numerical tables remain valid but are superseded as runtime
bookkeeping by this sharper certificate.

This is a candidate internal derivation awaiting the coordinator's
complete reconstruction. It is not promotion or a new proof of the
inherited stochastic insertion/source-selection interfaces. It makes
no practical precision claim, no growing-depth probability claim, and
no removal of the actual inverse-gap or exponential angular-depth
storage factors.
