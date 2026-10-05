# Polynomial compact error on the full recurrence allowance

2026-10-05. Current deterministic proof, conditional on the integrated
source, selection, and independent dense/compact fitting event. The
complete argument below includes the matched readout–residual reduction,
its corrected source forcing, and the full recurrence domination.
[COMPACT_FULL_LABEL_RANGE_CHECK.md](COMPACT_FULL_LABEL_RANGE_CHECK.md)
records the original mathematical reconstruction and the provenance of
this editorial consolidation.

For the existing corrected-readout model, throughout the full intersection
of the dense fitting, compact fitting, and source label allowances, a
universal numerical constant \(C\) gives
\[
\sup_{t\in[0,\infty],\,\|v\|=1}|f_C-f_n|
\le C\beta^{42L}Y\frac m\gamma
\max\left(1,\sqrt{\frac m\gamma}\right)
\frac{(1+\sqrt{\log(en)})e^{32\sqrt{\log(en)}}}{n},
\]
and
\[
\sup_{t\in[0,\infty],\,\|v\|=1}|f_C-f_n|
\le C\beta^{42L}Y(1+m/\gamma)^2n^{-1/2}.
\]
The source tolerance, horizon, selected dimensions, optimizer, and retained
state are unchanged. On this full label interval, size and storage use the
original exact source coefficients \(U,V\), as specified in Section 8.
The sharper common-cap numerical theorem and its simplified storage
envelope are in
[COMPACT_POLYNOMIAL_COMPARISON.md](COMPACT_POLYNOMIAL_COMPARISON.md).
The source-energy support is
[COMPACT_SOURCE_ENERGY.md](COMPACT_SOURCE_ENERGY.md).

## 1. Model, assumptions, and coefficient recurrences

Fix \(L\ge2\), \(d,m\ge1\), unit training inputs
\(v_a=x_a/\sqrt d\), and arbitrary fixed real labels \(y_a\).
The dense reference has
\[
z^{(1)}=Av,\quad z^{(j)}=W^{(j)}h^{(j-1)},\quad
h^{(j)}=\phi_j(z^{(j)}),\quad f_n(v)=w^\top h^{(L)}(v)/n.
\]
Its initialization has independent \(N(0,1)\) first-weight entries,
independent \(N(0,1/n)\) hidden-mixer entries, independent blocks, and zero
readout. Training is physical-time mean-square gradient flow with
mobilities \((n,1,\ldots,1,n)\), as defined in
[GENERAL_EXPLICIT_FITTING.md](GENERAL_EXPLICIT_FITTING.md).

Activations are real on the real axis, holomorphic on a horizontal strip,
and have bounded first derivative on that full strip; activation values
may be unbounded. Write \(a_{\rm strip}\) for the source's strip width
\(a\), reserving \(a(t)\) below for hidden-parameter error. Define
\[
b=\max_j|\phi_j(0)|,\quad
s=\max\left(1,\sup_{j,|\operatorname{Im}w|\le a_{\rm strip}/2}
|\phi'_j(w)|\right),\quad
t=\max\left(1,\sup_{j,|\operatorname{Im}w|\le a_{\rm strip}/2}
|\phi''_j(w)|\right),
\]
\[
\beta=\max(10,1+b,16/a_{\rm strip},s,t).
\]
Here \(t\) in derivative-coefficient formulas is the fixed second-derivative
bound; the argument of a trajectory denotes physical time. All formulas
retain the source convention.

The unweighted initialized covariance is
\[
Q^{(0)}_{ab}=v_a^\top v_b,\qquad
Q^{(j)}_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)],
\quad Z\sim N(0,Q^{(j-1)}),\qquad
\gamma=\lambda_{\min}(Q^{(L)})>0.
\]
Set \(\lambda=\gamma/m\) and \(Y=\|y\|_2/\sqrt m\), without
capping \(\lambda\) at one.
Use residuals \(c=y-f\), and set
\[
\rho_n=\|c_n\|_2/\sqrt m,\quad
\rho_C=\|c_C\|_2/\sqrt m,\quad \alpha=Y/\sqrt\lambda.
\]
Selected-neuron norms use fixed metrics \(M_j\), with
\(\mathsf D_j/4\preceq M_j\preceq\mathsf D_j\), where
\(\mathsf D_j\) is positive diagonal. Source selection is an exact
isometry on each selected source space,
\(\|1\|_{M_j}=1\), and \(\|1\|_{\mathsf D_j}\le2\).
Hidden tuples have the direct-sum Hilbert norm of first-weight and mixer
Hilbert–Schmidt norms. A star denotes the appropriate Hilbert adjoint;
sample space is Euclidean. These are the exact runtime metrics of
[EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md](EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md).

All source recurrences and pairings below refer to
[UNBOUNDED_COMPRESSOR_BRIDGE.md](UNBOUNDED_COMPRESSOR_BRIDGE.md).
The full label allowance is
\[
\frac Y\lambda\le
\min\{(8H_d\sqrt{F_d})^{-1},
      (16H_c\sqrt{F_c})^{-1},S_*^{\rm src}/16\},
\]
where \(H_d,F_d\) are the dense fitting recurrences, \(H_c,F_c\) are the
compact recurrences below, and \(S_*^{\rm src}\) is source (10).
Keep the inherited construction/probability event and every existing
width qualification. The source horizon is
\(T=32\lambda^{-1}\log(en)\); no source statement after \(T\) is needed.

Set \(\lambda=\gamma/m>0\), \(Y=\|y\|_2/\sqrt m>0\),
\(z=Y/\lambda\), \(S=16z\), and \(\ell_n=\log(en)\).
The derivative constants defined above satisfy \(s,t\ge1\), and \(b\ge0\).
Write \(H_j^{\rm src}\), \(P_j^{\rm src}\) for the source recurrences

\[
H_1^{\rm src}=b+20s,\quad
H_j^{\rm src}=b+10sH_{j-1}^{\rm src},\quad
P_1^{\rm src}=3,\quad
P_j^{\rm src}=H_{j-1}^{\rm src}+10sP_{j-1}^{\rm src}+1.
\]

Their original maxima with one are inactive. Define
\(f_j=sP_j^{\rm src}\) and \(f_*=\max_j f_j\), as in the source
recurrence. Source carriers have
\(k_j=H_L^{\rm src}(10s)^{L-j}\), \(\tau_j=sk_j\), and
\(\tau=\max_j\tau_j\). The forward activity recurrence is
\(V_1=\tau_1\),
\(V_j=\tau_j(H_{j-1}^{\rm src})^2+10sV_{j-1}\).
The source constants obey their exact definitions, in particular

\[
D_*=t\sum_j(P_j^{\rm src})^2,\quad
H_*\ge t(P_L^{\rm src})^2 H_L^{\rm src},\quad
D_0\ge \max\{\tau^2,2H_*^2\},
\]
\[
C_F=s[8f_*^2+(H_L^{\rm src})^2+1],\quad
C_{\rm abs}=8(D_0+1),\quad
W_{\rm G}\ge128sV_L,
\]
\[
\eta=\min\{1,(1024C_{\rm abs}W_{\rm G})^{-1}\},\quad
D_1=576e^3(1+b+s)D_*^3,\quad
\mathcal B=1024e^2L.
\]

Only two entries of the existing source minimum are needed in this proof:

\[
16z\le\min\left\{1,\ (8D_0C_F)^{-1/2},
                       (\eta^3/(D_1\mathcal B))^{1/4}\right\}.
\]

Let \(H_c,F_c,d_j^c\) be the current compact fitting constants, so that

\[
H_1^c=2b+16s,\quad H_j^c=2b+18sH_{j-1}^c,\quad H_c=H_L^c,
\]
\[
d_j^c=2s(18s)^{L-j},\qquad
F_c=(d_1^c)^2+4H_c^2\sum_{j=2}^L(d_j^c)^2.
\]

The exact existing compact allowance and its gap consequence are

\[
z\le\frac1{16H_c\sqrt{F_c}},\qquad \lambda\le H_c^2.
\tag{A}
\]

The dense fitting allowance in the displayed intersection is retained. The existing source
tolerance is \(\epsilon=n^{-1}\le\min(1,Y,S)\).
No additional label or width restriction is imposed.

For complete reproducibility of the coefficient being bounded, define
\(H_r=H_L^{\rm src}+3\), \(H_C=2H_c\),
\(P_h=6H_L^{\rm src}+9\), \(P_\delta=6\tau+9\),
\(A_f=18+S^2(\tau+3)P_h\), and
\(A_b=18+S^2H_rP_\delta\). Let

\[
F_1^z=1,\quad F_1^h=2s,\quad
F_j^z=9F_{j-1}^h+H_r+A_f,\quad F_j^h=2sF_j^z,\quad
F=\max_jF_j^h.
\]

The dense response coefficient is \(d_j^{\rm dense}=s(9s)^{L-j}\).
Define

\[
d_j^E=2d_j^{\rm dense}+3H_c,\quad
c=5\sqrt{F_c},\quad
j=\left[(d_1^E)^2+H_r^2\sum_{\ell=2}^L(d_\ell^E)^2\right]^{1/2},
\]
\[
B_L=2s(1+6zF+32zP_h)+2tF_L^z,
\quad
B_j=18sB_{j+1}+2s(d_{j+1}^EzH_c+A_b)+2tF_j^z
\quad(j<L),
\]
\[
B_h=\sqrt L\left[\max(1,H_C)\max_jB_j
                   +(\max_jd_j^E)zH_cF\right],
\quad K_1=12F+2B_h+20z(c+j)B_h+20D_s.
\tag{B}
\]

The scalar \(j\) in \(c+j\) is a norm coefficient, while subscripts label
layers; neither is an additional state. The source Gram coefficient is

\[
D_s=P_h+16zP_\delta[1+(L-1)H_r^2]
             +(L-1)(16z)^2\tau^2P_h.
\tag{C}
\]

## 2. Energy-scale source transfer

Write \(w_R=w_{n,I_L}\) for the actual selected dense readout.
Let \(V_n\) have columns equal to the dense top features divided by
\(\sqrt m\), with the dense neuron RMS norm, and let \(V_R\) have
columns equal to their actual selected restrictions divided by
\(\sqrt m\). Inserting the same source approximants into both maps
and using exact source isometry gives, for every \(\xi\in\mathbb R^m\),

\[
\|V_R\xi\|\le\|V_n\xi\|+3\epsilon\|\xi\|_2.
\tag{2}
\]

Indeed the original and selected normalized column-error operators have
Hilbert–Schmidt norm at most \(\epsilon\) and \(2\epsilon\),
respectively. There is no extra \(\sqrt m\) factor.

Dense fitting gives
\(\int\rho_n\le2z\), \(\int\|\dot\theta_n\|\le2\alpha\),
and \(\|w_n\|_n\le2\alpha\). With
\(\nu=\|V_Rc_n/\sqrt m\|\), (2) therefore yields

\[
\int_0^T\nu\le\alpha+6\epsilon z.
\tag{3}
\]

Integrating the feature source approximants against \(2c_n/m\)
produces a vector in the fixed top source space whose coordinate error
from \(w_n\) is at most \(4\epsilon z\). Applying the same two-sided
source-isometry comparison gives

\[
\|w_R\|\le2\alpha+12\epsilon z.
\tag{4}
\]

The runtime already proves \(\lambda\le H_c^2\). Since
\(\epsilon\le Y\), (A) implies

\[
\frac{\epsilon}{\sqrt\lambda}
\le z\sqrt\lambda\le zH_c\le\frac1{16\sqrt{F_c}}\le\frac1{16}.
\]

Consequently (3)–(4) imply, on the entire recurrence interval,

\[
\int_0^T\nu\le2\alpha,\qquad \|w_R\|\le3\alpha.
\tag{5}
\]

Let \(d_j^{\rm dense}=s(9s)^{L-j}\), the real dense response
coefficient. Dense fitting and source isometry similarly give

\[
\|\delta_{n,a,I_j}^{(j)}\|
\le2d_j^{\rm dense}\alpha+3\epsilon
\le(2d_j^{\rm dense}+3H_c)\alpha.
\tag{6}
\]

Thus the selected reference responses retain the energy scale. The
older shortcut \(\epsilon\le Y\le\alpha\) is invalid when
\(\lambda>1\); (6) is its valid replacement. Neither a capped gap
nor a smaller approximation tolerance is required.

## 3. Exact runtime identities

The compressed forward pass is
\(z_C^1(v)=A_Cv\), \(z_C^j(v)=B_C^jh_C^{j-1}(v)\), and
\(h_C^j(v)=\phi_j(z_C^j(v))\). Its normalized top training feature map
is \(V_C=[h_C^L(v_a)/\sqrt m]_a\), and
\[
\widehat w_C=w_C+V_C(V_C^*V_C)^{-1}
[(y-c_C)/\sqrt m-V_C^*w_C],\qquad
f_C(v)=\langle\widehat w_C,h_C^L(v)\rangle_{M_L}.
\]
Thus \(c_{C,a}=y_a-f_C(v_a)\). The specified backward signals are
\(k_{C,a}^L=\widehat w_C\),
\(\delta_{C,a}^j=\phi_j'(z_{C,a}^j)\odot k_{C,a}^j\), and
\(k_{C,a}^j=(B_C^{j+1})^*\delta_{C,a}^{j+1}\).
The residual equations are
\(\dot c_C=-2K_Cc_C/m\) and \(\dot c_n=-2K_nc_n/m\).
All initial parameter and residual discrepancies vanish.

Let \(V_C\) have columns \(h_C^{(L)}(v_a)/\sqrt m\). Let
\(\mathcal J_C\) have columns equal to the entire specified raw hidden
update direction divided by \(\sqrt m\):

\[
\frac1{\sqrt m}\left(\delta_{C,a}^{(1)}v_a^\top,
\big(\delta_{C,a}^{(j)}h_{C,a}^{(j-1)\top}M_{j-1}\big)_{j=2}^L\right).
\]

Define \(\mathcal J_R\) with actual selected dense features and
responses. The selected reference mixer is the initialized selected mixer
plus the rank-one integral specified in source §13. Its forward pass need
not equal these actual features; its paired action defect is retained.
The identities are

\[
\dot\theta_{h,C}=2\mathcal J_Cc_C/\sqrt m,\quad
\dot\theta_{h,R}=2\mathcal J_Rc_n/\sqrt m,\quad
\dot w_C=2V_Cc_C/\sqrt m,\quad
\dot w_R=2V_Rc_n/\sqrt m,
\]
\[
K_C/m=V_C^*V_C+\mathcal J_C^*\mathcal J_C.
\tag{7}
\]

The last identity is a Gram of the specified directions. It does not
identify those directions with derivatives of the corrected predictor.

Define

\[
a=\|\theta_{h,C}-\theta_{h,R}\|,\quad
e=(c_C-c_n)/\sqrt m,\quad u=\|e\|_2,\quad z_w=w_C-w_R,
\]
\[
q=V_C^*V_C\succeq\lambda I/4,\quad T_C=V_Cq^{-1},\quad
P_C=T_CV_C^*,\quad p=T_Ce,\quad \zeta=z_w+p,
\quad b_e=\|p\|+\|\zeta\|.
\]

Here \(z_w\) is a vector and the previously defined \(z=Y/\lambda\)
is a scalar. The following are exact:

\[
T_C^*T_C=q^{-1},\quad V_C^*T_C=I,\quad
P_C=P_C^*=P_C^2,\quad \|T_C\|\le2/\sqrt\lambda,
\]
\[
\dot T_C=(I-P_C)\dot V_Cq^{-1}-T_C\dot V_C^*T_C.
\tag{8}
\]

Let \(\Delta V=V_C-V_R\) and
\(d_R=V_R^*w_R-(y-c_n)/\sqrt m\). Forward subtraction and the
existing source readout pairing give

\[
\|\Delta V\|\le F(a+\epsilon),\qquad
\|d_R\|\le16zP_h\epsilon.
\tag{9}
\]

Substitution into the corrected-readout formula gives

\[
\widehat w_C-w_R=(I-P_C)z_w-p-T_C\Delta V^*w_R-T_Cd_R.
\tag{10}
\]

Since \((I-P_C)p=0\), (5), (8), and (9) imply

\[
\|\widehat w_C-w_R\|
\le b_e+6zF(a+\epsilon)+32zP_h\epsilon/\sqrt\lambda.
\tag{11}
\]

Define the source Gram defect

\[
D=V_R^*V_R+\mathcal J_R^*\mathcal J_R-K_n/m.
\]

The source pairings (43), including their hidden-layer products, give
\(\|D\|\le D_s\epsilon\), where one valid explicit coefficient is

\[
D_s=P_h+16zP_\delta[1+(L-1)H_r^2]
 +(L-1)(16z)^2\tau^2P_h.
\tag{12}
\]

The normalized sample operator norm is bounded by the maximum
unnormalized entry error. With
\(\Delta\mathcal J=\mathcal J_C-\mathcal J_R\), the factorization

\[
\Delta\mathcal K:=K_C/m-K_n/m
=V_C^*\Delta V+\Delta V^*V_R
 +\mathcal J_C^*\Delta\mathcal J
 +\Delta\mathcal J^*\mathcal J_R+D
\tag{13}
\]

is exact. In particular the second feature term acts on the actual
selected readout velocity, whose integral is (5).

The residual/readout equations now yield

\[
\dot e=-2(q+\mathcal J_C^*\mathcal J_C)e
 -2\Delta\mathcal Kc_n/\sqrt m,
\qquad \dot z_w=2V_Ce+2\Delta Vc_n/\sqrt m,
\]
\[
\dot\zeta=2\Delta Vc_n/\sqrt m+\dot T_Ce
 -2T_C\mathcal J_C^*\mathcal J_Ce
 -2T_C\Delta\mathcal Kc_n/\sqrt m.
\tag{14}
\]

The cancellation uses \(T_Cq=V_C\). No source approximation is
differentiated.

## 4. Hidden-Gram absorption under the existing allowance

Unrolling the compact fitting recurrence gives the exact identity used
for the hidden-direction norm:

\[
F_c=(d_1^c)^2+4H_c^2\sum_{j=2}^L(d_j^c)^2.
\tag{15}
\]

Indeed \(d_j^c=2s(18s)^{L-j}\); the initial term of \(F_L\)
is \(4s^2(18s)^{2L-2}\), and its other terms are
\(16s^2H_c^2(18s)^{2(L-j)}\). Rank-one Hilbert–Schmidt norms and
the effective-readout bound therefore give

\[
\|\mathcal J_C\|\le5\alpha\sqrt{F_c}.
\tag{16}
\]

Pairing the equation for \(p=T_Ce\) with \(p\) gives dissipation
\(-2\|e\|_2^2\), because \(\langle p,V_Ce\rangle=\|e\|_2^2\).
The hidden Gram is not assumed dissipative in this lifted metric. Its
absolute contribution is at most

\[
2\|p\|\|T_C\|\|\mathcal J_C\|^2u
\le8\|\mathcal J_C\|^2u^2/\lambda
\le200z^2F_cu^2\le\frac{25}{32H_c^2}u^2.
\tag{17}
\]

The final inequality uses precisely (A). Thus at least
\(39u^2/32\) of dissipation remains, without shrinking a structural
label constant.

Runtime differentiation gives
\(\|\dot V_C\|\le10\alpha F_c\rho_C\). Since
\(q^{-1}e=T_C^*p\), (8) implies

\[
\|\dot T_Ce\|\le40zF_c\rho_C\|p\|.
\tag{18}
\]

Put \(\mathcal F=2\|T_C\Delta\mathcal Kc_n/\sqrt m\|\) and

\[
I(t)=\int_0^t[40zF_c\rho_Cb_e+\mathcal F]\ \mathrm{d}r.
\]

Regularizing \(\|p\|\) by
\((\|p\|^2+\delta^2)^{1/2}\), integrating, and letting
\(\delta\downarrow0\) gives

\[
\|p(t)\|\le I(t),\qquad
\int_0^t u\le2I(t)/\sqrt\lambda.
\tag{19}
\]

For the latter use \(u^2/\|p\|\ge\sqrt\lambda\,u/2\).
The damping quotient is zero at \(p=0\), where \(e=V_C^*p=0\).
Monotone convergence justifies the regularization limit.

The remaining hidden-Gram term in (14), after (19), costs at most
\(200z^2F_c I\le25I/32\). Consequently

\[
b_e(t)\le2F\int_0^t\rho_n(a+\epsilon)+3I(t).
\tag{20}
\]

These statements apply throughout the full recurrence allowance.

## 5. Hidden-direction subtraction and factored forcing

The coefficients \(c,j,B_h\) in (B) obey
\(\|\mathcal J_C\|\le c\alpha\) and
\(\|\mathcal J_R\|\le j\alpha\), by (6) and (16). Let
\(M=1+16zK_{\rm src}\sqrt{\ell_n}\); source (23) bounds every actual
training carrier by \(M\).

Backward subtraction gives

\[
\|\Delta\mathcal J\|
\le B_h[b_e+M(a+\epsilon)+\epsilon/\sqrt\lambda].
\tag{22}
\]

To verify it, split each changed response into the changed upper response,
a changed mixer times its actual selected response, a paired reverse
action defect, and a changed gate times its actual selected carrier.
Their coefficients are respectively \(18s\),
\(2sd_{j+1}^E\alpha\le2sd_{j+1}^EzH_c\),
\(2sA_b\), and \(2tMF_j^z\). The top response uses (11).
Finally split each rank-one update direction into changed response times
compressed feature plus actual reference response times changed feature.
This proves (B) and (22). There is a single carrier factor \(M\).

Applying (13) in its displayed order gives

\[
\begin{split}
\mathcal F\le{}&2F\rho_n(a+\epsilon)
 +4F\frac\nu{\sqrt\lambda}(a+\epsilon)\\
&+4z(c+j)B_h\rho_n
 [b_e+M(a+\epsilon)+\epsilon/\sqrt\lambda]
 +4D_s\epsilon\rho_n/\sqrt\lambda.
\end{split}
\tag{23}
\]

The hidden-parameter equation and (19) imply

\[
a(t)\le\frac54 I(t)
 +2B_h\int_0^t\rho_n[b_e+M(a+\epsilon)+\epsilon/\sqrt\lambda],
\tag{24}
\]

since \(4cz=20z\sqrt{F_c}\le5/(4H_c)\le5/4\).

## 6. Scalar comparison with the complete forcing envelope

For \(E=a+b_e\) and \(r_\lambda=\max(1,\lambda^{-1/2})\), define
\[
B(t):=\int_0^t
\left[200zF_c\rho_C(r)+K_1M\rho_n(r)
                  +20F\nu(r)/\sqrt\lambda\right]\,dr.
\]
The comparison reduction is

\[
E(t)\le\epsilon(1+\lambda^{-1/2})(e^{B(t)}-1)
\le2\epsilon r_\lambda(e^{B(t)}-1),
\]
\[
B(t)\le400z^2F_c+2zK_1+40zF
                  +32z^2K_1K_{\rm src}\sqrt{\ell_n}.
\tag{D}
\]

The forcing envelope must retain both source-error terms. Set
\(M=1+16zK_{\rm src}\sqrt{\ell_n}\ge1\), let
\(\rho_C,\rho_n\) be the two residual RMS values, and let
\(\nu=\|V_Rc_n/\sqrt m\|\) be the reference readout-velocity
quantity. The already derived energy bounds are
\(\int\rho_C,\int\rho_n\le2z\) and
\(\int\nu\le2Y/\sqrt\lambda\). Combining (20), (23), and (24),
and enlarging \(17I/4\) to \(5I\), gives
\[
E(t)\le\int_0^t
\left[200zF_c\rho_C+K_1M\rho_n+20F\nu/\sqrt\lambda\right]
\left[E+\epsilon(1+\lambda^{-1/2})\right]\,ds.
\]
Indeed the two source-error terms obey
\[
b_e+M(a+\epsilon)+\epsilon/\sqrt\lambda
\le M\left[E+\epsilon(1+\lambda^{-1/2})\right].
\]
Replacing the sum by its maximum without the factor two would be
incorrect. Integral Gronwall proves (D). The integrated bound uses
\(\int\rho_C,\int\rho_n\le2z\) and \(\int\nu\le2\alpha\).

For every sphere query, with \(\alpha=Y/\sqrt\lambda\),

\[
\|\widehat w_C-w_R\|
 \le b_e+6zF(a+\epsilon)+32zP_h\epsilon/\sqrt\lambda,
\]
\[
|f_C-f_n|\le H_C\|\widehat w_C-w_R\|
                   +3\alpha F(a+\epsilon)+16zP_h\epsilon.
\tag{E}
\]

All errors vanish initially. The proof variable \(B(t)\) is the integrated
coefficient of a scalar comparison inequality, not a hidden matrix. This
note checks, throughout the existing recurrence interval, that

\[
zK_1\le1,\qquad zF\le1,\qquad z^2K_1K_{\rm src}\le1.
\tag{F}
\]

## 7. Recurrence domination and the output bound

For this calculation only, define source-dependent positive scalars

\[
r_0=10s\ge10,\quad r=L-1\ge1,\quad
u_0=H_L^{\rm src},\quad p_0=P_L^{\rm src},\quad
\kappa=(9/5)^r,\quad \tau=s u_0r_0^r,
\quad A_0=(18s)^r=\kappa r_0^r.
\]

All abbreviations here are proof-local and none denotes the compact
width budget. The source forward and port recurrences imply

\[
u_0\ge20s r_0^r,\qquad p_0\ge3r_0^r,
\qquad H_c\le2\kappa u_0.
\tag{33}
\]

The last inequality follows by induction from
\(2b+16s\le2(b+20s)\) and
\(18s=(9/5)(10s)\). All these recurrences have positive terms, so
the largest source feature and response coefficients are \(u_0\) and
\(\tau\), respectively.

The last entry in source (10) gives

\[
z\le\frac1{16\sqrt{8D_0C_F}}
\le\frac1{16\sqrt8\,\tau u_0},
\tag{34}
\]

because \(D_0\ge\tau^2\) and \(C_F\ge s u_0^2\).
The extra factor \(\sqrt s\ge1\) was harmlessly discarded.
Moreover \(P_h\le7u_0\), \(P_\delta\le7\tau\), and
\(H_r\le2u_0\). Thus the correction in each of \(A_f,A_b\)
is at most
\(14\tau u_0/(8s\tau^2u_0^2)<1\), proving

\[
A_f,A_b\le19.
\tag{35}
\]

Unrolling the forward subtraction recurrence and using
\(2s/(18s-1)\le1/8\) gives

\[
F\le A_0\left[2s+\frac{H_r+A_f}{8}\right]
\le u_0A_0.
\tag{36}
\]

For the last step use \(H_r+A_f\le u_0+22\),
\(u_0\ge20s\), and \(u_0\ge20\). The maximum
preactivation coefficient is at most \(F/(2s)\).

Since \(d_j^E\le7\kappa u_0\), (33)–(34) give

\[
(\max_jd_j^E)zH_c
\le\frac{14\kappa^2}{16\sqrt8\,s r_0^r}\le1,
\qquad 6zF\le1,\qquad32zP_h\le1.
\tag{37}
\]

Indeed \(\kappa^2/r_0^r\le(3.24/10)^r\le1\),
and \(u_0,\tau\ge20\) make the other two inequalities stronger.
Inserting (35)–(37) into the backward recurrence (B) gives

\[
\max_jB_j
\le A_0[9s+2tF/s]
\le3t u_0A_0^2/s.
\tag{38}
\]

The first estimate is the geometric sum with forcing
\(40s+tF/s\); the terminal coefficient is at most
\(6s+tF/s\). For the second, the term \(9sA_0\) is absorbed
by \(t u_0A_0^2/s\), since \(u_0\ge20s\),
\(A_0\ge18s\), and \(t\ge1\).

Since \(H_C\le4\kappa u_0\), (B), (37), and (38) imply

\[
B_h\le13\sqrt L\,\kappa^3 t u_0^2r_0^{2r}/s
       \le t u_0^2p_0^3.
\tag{39}
\]

For the last inequality,
\(\sqrt L\,\kappa^3\le r_0^r\): at \(L=2\) the ratio is
\(\sqrt2(5.832/10)<1\), and increasing \(L\) multiplies it
by at most \(\sqrt{3/2}(5.832/10)<1\). Now use
\(p_0\ge3r_0^r\) and \(13/(27s)\le1\).

The existing compact cap gives \(zc\le5/(16H_c)\le5/16\).
Also
\(j\le14\sqrt L\,\kappa u_0^2\), so (34) gives
\(zj\le14/(16\sqrt8)<1/3\), using
\(\sqrt L(1.8/r_0)^r\le1\). Consequently
\(z(c+j)<1\). Directly from (C) and (34),

\[
D_s\le7u_0+10Lu_0+(3+L)/u_0\le15Lu_0.
\tag{40}
\]

For its middle term one uses the sharper version
\(16z\le1/(\sqrt8\,\tau u_0\sqrt s)\); its final term is
at most \(7L/(8s u_0)\). Equations (36), (39), and (40) now prove

\[
K_1\le400t u_0^2p_0^3.
\tag{41}
\]

Here \(F\le t u_0^2p_0^3\), \(Lu_0\le t u_0^2p_0^3\),
and the coefficients in \(K_1\) total at most
\(12+22+300=334<400\).

It remains to compare this explicit polynomial with the existing stronger
source cap. The source definitions give

\[
D_0\ge2t^2u_0^2p_0^4,\qquad D_*\ge t p_0^2,
\qquad W_{\rm G}\ge u_0^3.
\tag{42}
\]

The first two use the top terms of \(H_*\) and \(D_*\).
For the third,
\(W_{\rm G}\ge128sV_L\ge128s^2u_0(H_{L-1}^{\rm src})^2\),
while \(u_0=b+10sH_{L-1}^{\rm src}\le(10s+1)H_{L-1}^{\rm src}\).
Since \(10s+1\le11s\), the lower bound is at least
\((128/121)u_0^3\).

The fourth-root entry in source (10), together with
\(\eta^{-1}\ge8192D_0W_{\rm G}\) and
\(D_1\mathcal B\ge D_*^3\), proves

\[
z\le\frac1{16}(8192D_0W_{\rm G}D_*)^{-3/4}.
\tag{43}
\]

Combining (41)–(43) yields the explicit bound

\[
zK_1\le\frac{25}{2^{21/2}}
 t^{-5/4}u_0^{-7/4}p_0^{-3/2}\le1.
\tag{44}
\]

For the carrier product, \(C_G=32\tau\),
\(C_{\rm abs}=8(D_0+1)\le16D_0\), and \(\tau\ge1\)
give \(K_{\rm src}\le8448D_0\tau\). Hence

\[
z^2K_1K_{\rm src}
\le\frac{13200}{8192^{3/2}}
 \frac{t u_0^2p_0^3\tau}
 {\sqrt{D_0}W_{\rm G}^{3/2}D_*^{3/2}}
\le\frac{13200}{\sqrt2\,8192^{3/2}}
 \frac{\tau}{t^{3/2}p_0^2u_0^{7/2}}
\le1.
\tag{45}
\]

For the last inequality substitute \(\tau=s u_0r_0^r\), use
\(p_0\ge3r_0^r\), \(u_0\ge20s\), and observe that the
numerical coefficient is less than one. Finally (34)–(36) give
\(zF\le\kappa/(16\sqrt8\,s u_0)\le1\).

Thus all three combinations in (F) are universally bounded by one
throughout the existing larger recurrence allowance. Equation (D)
consequently yields the sufficient universal bound

\[
B(t)\le44+32\sqrt{\ell_n}.
\tag{46}
\]

This is a looser numerical exponent than the common-cap theorem, but it
contains no sample/gap or activation/depth parameter. It is derived from
existing gates, not a new label restriction or an eventual-width
absorption.

For completeness, the prefactor also has a polynomial envelope on this
larger interval. For this power audit put \(X=\beta^L\ge100\), with
\(\beta\) exactly the activation envelope defined in Section 1. In particular
\(\beta\ge\max(10,1+b,s,t)\). A constant \(C\) below is universal
and numerical, independent of every structural, data, width, and confidence
parameter; it may be enlarged between inequalities. The unconditional
source/runtime recurrences give
\(u_0,H_c\le X^3\), \(p_0\le X^3\),
\(F\le X^6\), \(F_c\le X^{15}\),
\(K_1\le X^{17}\), and \(K_{\rm src}\le X^{21}\).
Since \(z\le1/16\), (D) implies
\(B/z\le C X^{38}(1+\sqrt{\ell_n})\). Equations (E),
with \(zF\le1\), then give a sufficient bound

\[
\sup_{t\le T,v}|f_C-f_n|
\le C X^{42}z r_\lambda\,n^{-1}(1+\sqrt{\ell_n})
 e^{44+32\sqrt{\ell_n}}.
\tag{47}
\]

The exponential and polynomial in \(\sqrt{\ell_n}\) are absorbed
into a numerical root-width constant by completing the square, uniformly
in all structural parameters. For tails, the runtime identities and
(A) give \(G_c\le5H_c^2\),
\(B_w^c\le25H_c^2r_\lambda\), and
\(B_f\le51H_c^3r_\lambda\). The source bound gives
\(\mathcal K\le2u_0^2\). Thus the existing all-time tail coefficient
is at most \(CzX^9r_\lambda\), and is covered by the same polynomial
root-width bound. These estimates use \(\lambda\le H_c^2\), not
\(\lambda\le1\).

Thus a universal numerical constant \(C\) gives, on the same inherited
source event and throughout the full existing recurrence allowance,
\[
\boxed{
\sup_{t\in[0,\infty],\ \|v\|=1}|f_C-f_n|
\le C\beta^{42L}Y\frac m\gamma
\max\left(1,\sqrt{\frac m\gamma}\right)
\frac{(1+\sqrt{\log(en)})e^{32\sqrt{\log(en)}}}{n},
}
\]
and, after enlarging the same universal constant,
\[
\boxed{
\sup_{t\in[0,\infty],\ \|v\|=1}|f_C-f_n|
\le \frac{C\beta^{42L}Y(1+m/\gamma)^2}{\sqrt n}.
}
\]
The factor \(e^{44}\) in (47) is included in the universal numerical
constant, not in a problem-dependent coefficient. The first bound remains
\(n^{-1+o(1)}\) at fixed task. These conclusions preserve the full
existing label interval; only their numerical constants are looser than
the separate common-cap result. They do not enlarge a construction width
threshold or change the compact model's retained storage. The mathematical reconstruction is recorded in
[COMPACT_FULL_LABEL_RANGE_CHECK.md](COMPACT_FULL_LABEL_RANGE_CHECK.md).

## 8. Exact retained storage and scope

For \(d\ge2\), the existing leading source rank is
\[
A_n(Y)=\frac{2^{20}9^d}{d!}\frac U{a_{\rm strip}}\,c_q^{-(d-1)}
       (Y/\lambda)^2\ell_n^{3d/2+1},\qquad
c_q=\min\{1/8,a_{\rm strip}/(8V)\},
\]
with the **actual original** source recurrences \(U,V\) evaluated at
\(S=16Y/\lambda\). For \(d=1\), use its existing replacement
\(A_n(Y)=8\cdot514\cdot1024\,(U/a_{\rm strip})(Y/\lambda)^2\ell_n^{5/2}\).
The unchanged inventory is
\[
2040(L+1)A_n(Y)^2+
2040(L+1)(2m+d+1)^2+10m(d+1).
\]
The common-cap simplified storage coefficient
\(\beta^{(64+6d)L}\) applies on that companion theorem's smaller
label interval; the full interval here uses the displayed exact coefficients.
No retained runtime variable or source family is added by the comparison.
Exact-real preprocessing, precision qualifications, and
all original source construction gates remain in force.


Bounded activation values are not required. Feature, rank-one direction,
and pairing bounds use RMS norms and linear growth. The only coordinate
maximum in the comparison is the actual training carrier multiplying a
changed gate. Diagonal domination controls gate operator norms; it does
not make gates self-adjoint in the selected metrics.

The proof variables \(p,\zeta,\nu\) and the selected reference arrays are
not retained runtime coordinates. Source defects are neither discarded
nor differentiated. No query or time-dependent reference signal enters
the autonomous model.

The inherited stochastic source and construction threshold remains a
conditional input and is not claimed polynomial. This internally checked
deterministic result is not a promotion certificate. If \(Y=0\), both
predictors are the exactly stationary zero function, with no division by
\(Y\) and no additional width condition.
