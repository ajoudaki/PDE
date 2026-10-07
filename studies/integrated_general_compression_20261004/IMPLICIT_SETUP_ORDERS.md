# Explicit deterministic orders for the certified Taylor setup interface

2026-10-06. Interface analysis within the current study; no new activation
proof, sampler theorem, experiment or promotion is claimed. The author also
authored LOCAL_CONTINUATION_ASSEMBLY.md and cross-checked the continuation and
activation-backend candidates. This is not an independent research context.
No new implicit-sampler or implicit-execution candidate was read.

The recipe below chooses the original weighted-simplex source modes and the
positive quadrature, then the polynomial-activation Taylor backend with the
stronger source-jet interface in LOCAL_TAYLOR_ASSEMBLY_BRIDGE.md. Every order
is given by finite recurrences and rounded formulas. No norm of an unknown
trained path is an input. Confidence affects the inherited admissible-width
qualification; its stochastic portion is not numerically quantified.

Scientific inputs read completely where relevant were RESULT.md: shared
setup, common label and confidence conventions, dense fitting, source
recurrences and their proofs, whole-sphere source domain, all-horizon
extension, mode counts and original gates; the complete prior ODE and
quadrature route notes; LOCAL_CONTINUATION_SETUP.md; LOCAL_ACTIVATION_BACKEND.md;
and LOCAL_TAYLOR_ASSEMBLY_BRIDGE.md. The existing notation contract and
required accessible skills were applied. The prescribed canonical-notation
skill remains inaccessible, as previously disclosed.

The fixed input versions are RESULT.md at
c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278;
the ODE route at
46e9c2b4ed9f118b3812ce8208d26ebbfa9c9f1fb3efc6e68f3854e0be8cf5a6;
the quadrature route at
2d58da5a418f6d5a8f1bb54ce343b205978770424c0940789b15231e251daf42;
the continuation core at
c4c12b38e49e37ac5096e69ceabee1d41be6ad6bc4a1c57ece943959ef425bbe;
the activation backend at
cbf26326c081fc19da31f5d38781eff2dfa2a5b97dee12eb1a8022770a2843e4;
and the bridge at
dedba0b570d6a73b5c9eabbd414953d01fdc6d46056de023748eede621c64f2b.

## 1. Inputs and conventions

Supply integers \(n,m,d\ge1\), hidden depth \(L\ge2\), normalized data
\(\|x_a\|_2=\sqrt d\), the layer activations, positive gap \(\gamma\),
label RMS \(Y=\|y\|_2/\sqrt m\), confidence \(0<\delta<1\), source
horizon \(T\), and source-coordinate tolerance \(\eta\). Put

\[
\lambda=\gamma/m,\qquad S=16Y/\lambda,\qquad
T_0=32\lambda^{-1}\log(en),\qquad \eta_0=\min(1,Y,S).
\]

The nontrivial branch has \(Y>0\), \(T\ge T_0\) and \(0<\eta\le\eta_0\).
For \(Y=0\), retain the exact zero-predictor branch and do not evaluate formulas
dividing by \(Y\). All logarithms are natural except \(\log_2\).
Impossible binomial coefficients are zero.

The activations are real on the real axis and holomorphic on
\(|\operatorname{Im}z|<a\), with bounded first derivative on that full
open strip, as in the original activation hypothesis. Use the exact bounds
or certified upper bounds

\[
b=\max_j|\phi_j(0)|,\quad
s=\max\{1,\sup_{j,|\operatorname{Im}z|\le a/2}|\phi_j'(z)|\},\quad
t_2=\max\{1,\sup_{j,|\operatorname{Im}z|\le a/2}|\phi_j''(z)|\},
\]
\[
\beta=\max\{10,1+b,16/a,s,t_2\}.
\]

The second-derivative bound is needed by the proof even though setup does not
ask for second-derivative values. A bound on \(\phi'\) only on the same
closed half-strip is insufficient to infer that bound on its boundary.
If a bound \(s_{\rm full}\) on \(\phi'\) on the full strip is supplied,
one may use \(t_2=\max(1,2s_{\rm full}/a)\), by Cauchy. Alternatively a
supplied valid \(\beta\) provides \(t_2\le\beta\).

Using looser bounds may reduce a sufficient label allowance. To preserve the
full original allowance for a given activation, evaluate the original
recurrences with its stated original bounds rather than silently replacing
them by worst-case \(\beta\) values.

The notation below distinguishes source coefficients by superscript
\({\rm src}\), the real stability coefficients by \({\rm r}\), and the
Legendre/runtime coefficients by their own labels. Unsuperscripted
\(H_j,P_j,B_j,G,J_{\rm loc}\) introduced later belong only to the
local complex continuation. These are exact translations of the component
notes' local notation.

## 2. Source constants, with no omitted recurrence inputs

First compute

\[
H_1^{\rm src}=\max(1,b+20s),\quad
H_j^{\rm src}=\max(1,b+10sH_{j-1}^{\rm src}),
\]
\[
k_L^{\rm src}=H_L^{\rm src},\quad
k_j^{\rm src}=10s k_{j+1}^{\rm src},\quad
\tau_j^{\rm src}=s k_j^{\rm src},
\]
\[
P_1^{\rm src}=3,\quad
P_j^{\rm src}=H_{j-1}^{\rm src}+10sP_{j-1}^{\rm src}+1,\quad
f_j^{\rm src}=sP_j^{\rm src}.
\]

Forward recurrences have \(2\le j\le L\), backward recurrences
\(1\le j<L\), unless explicitly stated otherwise. Define maxima
\(H_{\max}^{\rm src}=\max_jH_j^{\rm src}\),
\(k_*^{\rm src}=\max_jk_j^{\rm src}\), \(f_*^{\rm src}=\max_jf_j^{\rm src}\)
and \(\tau_*^{\rm src}=\max_j\tau_j^{\rm src}\). Then

\[
A_*=2sP_L^{\rm src}
 +2s^2\sum_{j=2}^L k_j^{\rm src}P_{j-1}^{\rm src},\quad
D_*=t_2\sum_{j=1}^L(P_j^{\rm src})^2,
\]
\[
H_*=A_*+t_2\sum_{j=1}^L(P_j^{\rm src})^2k_j^{\rm src},\quad
E_{\rm src}=t_2\sum_{j=1}^L(10s)^{2(j-1)}k_j^{\rm src},
\]
\[
\mathcal T_{\rm src}=2H_*^2+4A_*^2(e^2-1),
\]
\[
D_0=(1+b+s)[1+\mathcal T_{\rm src}+E_{\rm src}
                         +s^2(k_*^{\rm src})^2],
\quad D_1=576e^3(1+b+s)D_*^3,
\]
\[
C_F^{\rm src}=s[8(f_*^{\rm src})^2+(H_{\max}^{\rm src})^2+1],
\qquad C_{\rm abs}=8(D_0+1).
\]

For the source activity moduli use

\[
V_1^{\rm mod}=\tau_1^{\rm src},\quad
V_j^{\rm mod}=\tau_j^{\rm src}(H_{j-1}^{\rm src})^2+10sV_{j-1}^{\rm mod},
\]
\[
G_L^{\rm mod}=sH_L^{\rm src}+14t_2V_L^{\rm mod}+s,
\]
\[
G_j^{\rm mod}=10sG_{j+1}^{\rm mod}
 +s^3(k_{j+1}^{\rm src})^2H_j^{\rm src}+14t_2V_j^{\rm mod}+s,
\]
\[
W_{\rm G}=128[1+H_{\max}^{\rm src}
                    +s\max_jV_j^{\rm mod}+\max_jG_j^{\rm mod}].
\]

The source budget tolerance below is not the requested source error \(\eta\):

\[
\eta_{\rm bud}=\min\{1,(1024C_{\rm abs}W_{\rm G})^{-1}\},\quad
\mathcal B=1024e^2L,\quad
\Lambda_{\rm bud}=\log(e+\mathcal B)+\log(1/\eta_{\rm bud}),
\]
\[
\begin{split}
S_*^{\rm src}=\min\{&
1,(4A_*)^{-1},
\sqrt{\eta_{\rm bud}/(4000D_*)},
\sqrt{\eta_{\rm bud}/(16eD_*\sqrt{2\mathcal B})},\\
&\sqrt{\eta_{\rm bud}/\Lambda_{\rm bud}},
(\eta_{\rm bud}^3/(D_1\mathcal B))^{1/4},
(8D_0C_F^{\rm src})^{-1/2}\}.
\end{split}
\]

Set

\[
C_G=32\max(1,H_{\max}^{\rm src},\tau_*^{\rm src}),\qquad
K_{\rm src}=16C_{\rm abs}(1+C_G).
\]

The remaining query-radius coefficients are

\[
g_{\rm src}=\tau_1^{\rm src}
             +\sum_{j=2}^L\tau_j^{\rm src}H_{j-1}^{\rm src},\quad
r_j^{\rm src}=P_j^{\rm src}g_{\rm src},\quad
q_j^{\rm src}=f_j^{\rm src}g_{\rm src},
\]
\[
j_j^{\rm ang}=20(10s)^{j-1},\qquad b_j^{\rm ang}=sj_j^{\rm ang},
\]
\[
e_1^{\rm src}=t_2r_1^{\rm src}P_1^{\rm src},\quad
e_j^{\rm src}=t_2r_j^{\rm src}P_j^{\rm src}
 +s[q_{j-1}^{\rm src}+\tau_j^{\rm src}H_{j-1}^{\rm src}f_{j-1}^{\rm src}
                                              +10e_{j-1}^{\rm src}],
\]
\[
a_1^{\rm ang}=t_2j_1^{\rm ang}P_1^{\rm src}+2s,\quad
a_j^{\rm ang}=t_2j_j^{\rm ang}P_j^{\rm src}
                                      +s(b_{j-1}^{\rm ang}+10a_{j-1}^{\rm ang}),
\]
\[
T_Q=8f_*^{\rm src}\max_j(f_j^{\rm src}H_*+e_j^{\rm src}),
\qquad T_J=8f_*^{\rm src}\max_ja_j^{\rm ang}.
\]

With \(G_d=16\sqrt{d+3}\), define

\[
U_1=4sK_{\rm src},\quad
U_j=2\{sK_{\rm src}[(H_{j-1}^{\rm src})^2+(f_{j-1}^{\rm src})^2
             +ST_Q+S^2H_{j-1}^{\rm src}q_{j-1}^{\rm src}]
                                     +G_dq_{j-1}^{\rm src}+1\},
\]
\[
V_1^{\rm qry}=2(2G_d+2sK_{\rm src}S^2+1),\quad
V_j^{\rm qry}=2\{G_db_{j-1}^{\rm ang}
 +sK_{\rm src}S^2(T_J+H_{j-1}^{\rm src}b_{j-1}^{\rm ang})+1\},
\]
\[
U=\max_jU_j,\qquad V_{\rm qry}=\max_jV_j^{\rm qry},\qquad
c_t=\frac{a}{64YSU},\quad c_q=\min\{1/8,a/(8V_{\rm qry})\},
\]
\[
r_t=\frac{c_t}{\sqrt{\log(en)}},\qquad
r_q=\frac{c_q}{\sqrt{\log(en)}},\qquad
\mathcal K=(H_L^{\rm src})^2+
 S^2[(\tau_1^{\rm src})^2+
           \sum_{j=2}^L(\tau_j^{\rm src})^2(H_{j-1}^{\rm src})^2].
\]

These are exactly source S.5--S.10, S.22, S.24--S.25 and S.30, with only
notation changed to avoid collisions. In particular \(U,V_{\rm qry}\)
retain their dependence on the actual \(S=16Ym/\gamma\).

## 3. Full original label interval

The scalar Gaussian moments are activation-dependent inputs, defined by

\[
\mu_{2,0}=1,\quad
\mu_{2,j}=\mathbb E[\phi_j(\sqrt{\mu_{2,j-1}}Z)^2],\quad Z\sim N(0,1),
\qquad H_D=\max(1,\sqrt{\mu_{2,1}},\ldots,\sqrt{\mu_{2,L}}).
\]

They are finite by linear growth. They are not determined exactly by
\(\beta\). Put

\[
D_j^D=s(9s)^{L-j},\quad
F_D=s^2[(9s)^{2L-2}+4H_D^2\sum_{j=0}^{L-2}(9s)^{2j}].
\]

For the optional common Legendre restriction define

\[
C_1^{\rm Leg}=4s^2(D_1^D)^2,\quad
C_j^{\rm Leg}=3s^2[64H_D^4(D_j^D)^2+82C_{j-1}^{\rm Leg}],
\quad E_{\rm Leg}=130\sum_{j=2}^LD_j^D\sqrt{C_{j-1}^{\rm Leg}},
\]
\[
S_*^{\rm Leg}=\min\{1,(64H_D^2D_1^D)^{-1},
 (8\sqrt{C_L^{\rm Leg}})^{-1/2},
 (8H_D^2D_1^DE_{\rm Leg})^{-2/7}\}.
\]

For Harmonic runtime fitting define

\[
H_1^c=2b+16s,\quad H_j^c=2b+18sH_{j-1}^c,\quad H_c=H_L^c,
\quad d_j^c=2s(18s)^{L-j},
\]
\[
F_c=(d_1^c)^2+4H_c^2\sum_{j=2}^L(d_j^c)^2.
\]

The full original common interval is

\[
0<Y\le\lambda\min\{(8H_D\sqrt{F_D})^{-1},\
S_*^{\rm Leg}/8,\
(16H_c\sqrt{F_c})^{-1},\
S_*^{\rm src}/16\}.
\]

For the Harmonic result alone the Legendre entry can be omitted, exactly as
in RESULT.md. None of the order prescriptions below adds a label restriction.
The simpler \(Y\le\lambda\beta^{-30L}\) is sufficient but is not substituted
for this full interval.

## 4. Width and confidence qualification

For \(0<\alpha<1\), define

\[
A_D=s^2+t_2(b+\sqrt2sH_D),\quad T_D=\sum_{j=0}^{L-1}A_D^j,\quad
e_D=\min\{1/4,\gamma/(2m)\},
\]
\[
M_D=8b^4+96s^4H_D^4,\quad
h_D=\min\{1/2,H_D/[4(8s)^L]\},\quad P_D=(1+2/h_D)^d,
\]
\[
N_{\rm fit}(\alpha)=\left\lceil\max\left\{
1,\frac{\log(8L/\alpha)}{8-2\log9},
\frac{d\log9+\log(8/\alpha)}{8-\log9},
\frac{2L(m^2+P_D)M_DT_D^2}{\alpha e_D^2}
\right\}\right\rceil.
\]

Use the conservative existing explicit initialization gate
\(n\ge N_{\rm fit}(\delta/32)\), and \(n\ge\max(m,d)\) for the
stated common cost simplifications. Also require the existing source event
at a sufficiently small allocated failure probability, for example
\(\delta/32\). Its sufficient width is existential, not given by a numerical
function here or in the source proof. A union bound does not require
independence. Additional lower-bound/CLT events are irrelevant to this setup
interface.

The original deterministic gates are included explicitly. Set

\[
D_W=\max\{\tau_1^{\rm src},
                    \max_{j\ge2}\tau_j^{\rm src}H_{j-1}^{\rm src}\}.
\]

Require \(n^{-1}\le\eta_0\) and

\[
\sqrt{\log(en)}\ge
c_t\max\{8,\lambda,4\mathcal K/\log2,32YSD_W\}.
\]

For all-horizon extension define

\[
b_{\rm ext}=\min\{1/4,SH_L^{\rm src}/4,
             a/[8\sqrt n\max_jP_j^{\rm src}]\},
\]
\[
C_L^k=1,\quad C_j^k=S\tau_{j+1}^{\rm src}+10sC_{j+1}^k
                  +10t_2SP_{j+1}^{\rm src}k_{j+1}^{\rm src},
\quad C_{\rm carrier}=\max_jC_j^k,
\]
\[
Z_n=(2Y/\sqrt\lambda+8Y\sqrt{\mathcal K}\,r_t)(en)^{-16}.
\]

Require

\[
Z_n<b_{\rm ext}/2,\qquad
\frac{2C_{\rm carrier}Y}{\sqrt\lambda}\,n(en)^{-16}
                   \le K_{\rm src}S\sqrt{\log(en)}.
\]

For the original simplified counting gates put
\(M_{\rm amp}=10\max(H_L^{\rm src},\tau_*^{\rm src})\).
When \(d\ge2\), set
\(b_d=2d-2\), \(D_d=2^{d+1}d^{d-2}\), and

\[
C_d^*=16\cdot128\cdot18M_{\rm amp}D_db_d!2^{b_d+1}
                  \lambda^{-1}c_t^{-1}c_q^{-(b_d+1)}.
\]

Retain

\[
\log C_d^*\le\log(en),\quad
(d+1)\log\log(en)\le\log(en),\quad
\frac{(d-1)c_q}{\sqrt{\log(en)}}\le1,\quad
\frac{r_t}{4T_0}\le1.
\]

When \(d=1\), retain \(r_t/(4T_0)\le1\) and
\(\log[8192M_{\rm amp}/(c_t\lambda)]\le\log(en)\).
All these gates are explicit; they do not supply the missing stochastic
confidence-to-width threshold. No path-dependent norms are measured to
certify them.

## 5. Retained modes, rank and selected budget

Put \(M_n=M_{\rm amp}\sqrt n\) and \(\alpha_T=r_t/(4T)\).
For \(d\ge2\), define

\[
P_T=\frac{18D_db_d!2^{b_d+1}}{\alpha_T r_q^{b_d+1}},\qquad
H(T,\eta)=2\log\frac{16M_nP_T}{\eta},
\]
\[
p=\left\lfloor\frac{H(T,\eta)}{\alpha_T}\right\rfloor,\quad
\ell_*=\left\lfloor\frac{H(T,\eta)}{r_q}\right\rfloor,\quad
h_\ell={\ell+d-1\choose d-1}-{\ell+d-3\choose d-1},
\]
\[
p_\ell=\left\lfloor\frac{H(T,\eta)-r_q\ell}{\alpha_T}\right\rfloor,
\quad
N=\sum_{\ell=0}^{\ell_*}(p_\ell+1)h_\ell,\quad
H_{\rm sph}=\sum_{\ell=0}^{\ell_*}h_\ell,\quad
\mathcal Y=\max_{\ell\le\ell_*}\sqrt{h_\ell}.
\]

The retained set contains precisely \(0\le k\le p_\ell\) and all
\(h_\ell\) harmonics at degree \(\ell\). Set
\(R=2m+d+1+4N\).

For \(d=1\), instead use

\[
H_1(T,\eta)=\log\frac{64M_n}{\alpha_T\eta},\quad
N_1=1+\lfloor H_1(T,\eta)/\alpha_T\rfloor,\quad p=N_1-1,
\]
\[
N=2N_1,\quad H_{\rm sph}=2,\quad N_x=2,\quad
R=2m+d+1+8N_1.
\]

Here \(N\) counts both point families; the quadrature accuracy formulas below
use the per-point \(N_1\). There is no spherical degree at \(d=1\).

A deterministic sufficient selected budget is \(q=\min(n,9R)\).
If \(9R\ge n\), use the original exact full-width fallback, rather than
assert compression. If the headline convention \(q\ge18(2m+d+9)\) is
desired, use \(q=\min(n,\max\{9R,18(2m+d+9)\})\).
The actual rank \(r=\max_j\dim E_j\le\min(n,R)\) may permit a smaller
budget \(9r\); that is computed after coefficient assembly and is not an
order-only prediction. No preservation of accidental rank deficiencies is
assumed.

## 6. Positive quadrature orders

For \(d\ge2\), define \(I_0=\pi\), \(I_1=2\),
\(I_b=(b-1)I_{b-2}/b\) for \(b\ge2\), and

\[
A_d=\prod_{b=1}^{d-2}\frac{\pi}{I_b},\quad
D_d^{\rm ang}=(d-2)(d-1)/2,\quad
h_{\rm ang}=\frac{r_q}{2(d-1)},\quad
\sigma_{\rm ang}=\operatorname{arsinh}(2h_{\rm ang}/\pi).
\]

Empty products equal one. Put \(a_t=\alpha_T/2\) and

\[
\epsilon_c=\frac{\eta}{16N\mathcal Y},\qquad
\delta_{\rm node}=\frac{\eta}{64NA_d\mathcal Y^2},
\]
\[
B_{\rm int}=2M_n\mathcal YA_d
 \exp[a_tp+\ell_*(d-1)h_{\rm ang}]
                    (\cosh h_{\rm ang})^{D_d^{\rm ang}}.
\]

Then take

\[
N_t=\max\{1,\lceil a_t^{-1}\log(1+4dB_{\rm int}/\epsilon_c)\rceil\},
\]
\[
N_\varphi=\max\{1,\lceil h_{\rm ang}^{-1}
                              \log(1+4dB_{\rm int}/\epsilon_c)\rceil\}.
\]

For \(d\ge3\), take

\[
N_\theta=\max\left\{1,\left\lceil\sigma_{\rm ang}^{-1}
\log\frac{8dB_{\rm int}}{\epsilon_c(1-e^{-\sigma_{\rm ang}})}
\right\rceil\right\},\qquad N_x=N_\varphi N_\theta^{d-2}.
\]

For \(d=2\), use \(N_x=N_\varphi\) and no polar rule. For \(d=1\), use

\[
\epsilon_c=\frac{\eta}{16N_1},\quad
\delta_{\rm node}=\frac{\eta}{64N_1},\quad
B_{\rm int}=2M_ne^{a_tp},\quad
N_t=\max\{1,\lceil a_t^{-1}\log(1+4B_{\rm int}/\epsilon_c)\rceil\}.
\]

These are the original positive periodic/Fejér orders. No equalities
\(N_t=p+1\) or \(N_x=H_{\rm sph}\) are used.

## 7. Complex local continuation constants

Define the real-stability coefficients first:

\[
H_1^{\rm r}=\max(1,b+10s),\quad
H_j^{\rm r}=\max(1,b+10sH_{j-1}^{\rm r}),\quad H^{\rm r}=H_L^{\rm r},
\]
\[
R^{\rm r}=1+2Y/\sqrt\lambda,\quad
B^{\rm r}=R^{\rm r}s(10s)^{L-1},\quad
F_z^{\rm r}=H^{\rm r}(10s)^{L-1},\quad
P_{\rm layer}^{\rm r}=1+(L-1)H^{\rm r},
\]
\[
D^{\rm r}(M)=(10s)^{L-1}
 [s(1+B^{\rm r})+Lt_2F_z^{\rm r}M],
\]
\[
J^{\rm r}(M)=\sqrt{L+1}
 [P_{\rm layer}^{\rm r}D^{\rm r}(M)
                  +(1+(L-1)B^{\rm r})sF_z^{\rm r}],
\]
\[
C^{\rm r}(M)=sF_z^{\rm r}\sqrt L+LB^{\rm r}sF_z^{\rm r}
                       +\tfrac12L^2t_2(F_z^{\rm r})^2M.
\]

Evaluate \(J^{\rm r},C^{\rm r}\) at
\(M=2K_{\rm src}S\sqrt{\log(en)}\), then set

\[
A_n=4J^{\rm r}Y/\lambda,\quad
K_{\rm qry}^{\rm r}=R^{\rm r}(10s)^{L-1},
\]
\[
C_{\rm src}=8\sqrt{L+1}\max\left\{sF_z^{\rm r},
(10s)^{L-1}[s(1+B^{\rm r})+Lt_2F_z^{\rm r}K_{\rm qry}^{\rm r}]\right\}.
\]

The different local complex coefficients are

\[
R_{\rm loc}=1+SH_L^{\rm src},\quad
H_1=\max(1,b+11s),\quad H_j=\max(1,b+11sH_{j-1}),
\]
\[
B_j=R_{\rm loc}s(11s)^{L-j},\quad
P_1=1,\quad P_j=H_{j-1}+11sP_{j-1},\quad P_*=\max_jP_j,
\]
\[
\kappa_L(M)=1,\quad
\kappa_j(M)=11s\kappa_{j+1}(M)+11t_2MP_{j+1}+B_{j+1},
\quad D_j(M)=s\kappa_j(M)+t_2MP_j,\quad
\kappa_*(M)=\max_j\kappa_j(M),
\]
\[
G=H_L+B_1+\sum_{j=2}^LB_jH_{j-1},
\quad
J_{\rm loc}(M)=sP_L+D_1(M)+
 \sum_{j=2}^L[H_{j-1}D_j(M)+B_jsP_{j-1}].
\]

Put

\[
M_0=K_{\rm src}S\sqrt{\log(en)},\quad
M_c=M_0+\sqrt n\kappa_*(M_0)Z_n,
\]
\[
b_n=\min\{1/4,a/(16\sqrt nP_*),1/(\sqrt n\kappa_*(M_c))\},
\]
\[
L_n=2G^2+2(2Y+G)J_{\rm loc}(M_c+1),\quad
V_{\rm loc}=2G(2Y+G),\quad
\widehat R_n=\min\{r_t/2,(8L_n)^{-1}\}.
\]

The symbols \(b_n,V_{\rm loc}\) here are the backend's local tube radius
and velocity coefficient; they are not \(b_{\rm ext}\) or \(V_{\rm qry}\).

## 8. One activation polynomial and complete local degree

For the strong source-jet interface use
\(\delta_*=\delta_{\rm node}/(32\sqrt n)\), the bridge's tightened
backend nodal target. Define

\[
e_d=e^{-A_n}\min\left\{
\frac14,\frac1{\sqrt8(C^{\rm r}+J^{\rm r})\sqrt T},
\frac{\delta_*}{4C_{\rm src}n},\frac{b_n}{16}\right\},
\]
\[
\zeta_F=\min\{e_d/(2T),b_nL_n/4,V_{\rm loc}/2\}.
\]

For the activation substitution put

\[
U_0^{\rm act}=0,\quad U_j^{\rm act}=1+11sU_{j-1}^{\rm act},\quad
U_*^{\rm act}=\max_jU_j^{\rm act},\quad
K_j^{\rm act}=R_{\rm loc}(11s)^{L-j},
\]
\[
Q_{L+1}^{\rm act}(M)=0,\quad
Q_j^{\rm act}(M)=11(s+1)Q_{j+1}^{\rm act}(M)
                   +K_j^{\rm act}+11t_2M U_{j-1}^{\rm act}.
\]

Evaluate the following training constants at \(M=M_c+1\):

\[
Q_\xi=U_L^{\rm act}+Q_1^{\rm act}(M)
 +\sum_{j=2}^L[Q_j^{\rm act}(M)(H_{j-1}+1)+B_jU_{j-1}^{\rm act}],
\quad Q_f=R_{\rm loc}U_L^{\rm act},
\]
\[
C_F^{\rm act}=2Q_f(G+1)+2(2Y+G)Q_\xi.
\]

For passive sources use

\[
M_q=\sqrt n\max_jK_j^{\rm act},\qquad
C_p=8\sqrt n\max\{U_*^{\rm act},\max_jQ_j^{\rm act}(M_q)\},
\]
\[
\epsilon=\min\left\{
1,(U_*^{\rm act})^{-1},
\frac{a}{5632\sqrt nU_*^{\rm act}},
Q_\xi^{-1},\frac{\zeta_F}{C_F^{\rm act}},\frac{\delta_*}{2C_p}\right\}.
\]

The activation ellipse scale and degree are

\[
Z_*=(K_{\rm src}+G_dH_{\max}^{\rm src}+1+US^2)\sqrt{\log(en)}
                                +a/8+\sqrt nP_*Z_n,\quad
B_{\rm act}=8(Z_*+a+1),
\]
\[
\tau_o=\operatorname{arsinh}\frac{31a}{64B_{\rm act}},\quad
\tau_i=\operatorname{arsinh}\frac{29a}{64B_{\rm act}},\quad
\Delta_{\rm act}=\tau_o-\tau_i,\quad
M_\phi=b+s(B_{\rm act}+a),
\]
\[
C_a=\max\{1,512/a,2(512/a)^2\},\quad \epsilon_p=\epsilon/C_a,
\]
\[
D=\max\left\{1,\left\lceil\Delta_{\rm act}^{-1}
\log\max\{e,24M_\phi/(\epsilon_p\Delta_{\rm act})\}\right\rceil\right\},
\qquad N_\phi=4(D+1).
\]

Each layer's polynomial uses real activation values at
\(B_{\rm act}\cos(2\pi r/N_\phi)\). If those values are inexact, the
sufficient individual accuracy is

\[
\epsilon_{\rm eval}=
\frac{\epsilon_p}{4(D+1)e^{D\tau_i}}.
\]

Exact initialized source additions remain original-activation evaluations
under the inherited exact-real convention. They are not replaced by these
polynomial values.

Finally set \(C_g=\max_j\{H_j+1,B_j+1\}\) and choose

\[
\begin{split}
K=\max\bigg\{&8,\
\left\lceil2\log_2\max\{1,16TV_{\rm loc}/e_d\}\right\rceil,\
\left\lceil\log_2\max\{1,8V_{\rm loc}\widehat R_n/b_n\}\right\rceil,\\
&\left\lceil\log_2\max\left\{1,
\frac{128V_{\rm loc}\widehat R_n C_{\rm src}n^{3/2}}
     {\delta_{\rm node}}\right\}\right\rceil,\
\left\lceil\log_2\max\left\{1,
\frac{64\sqrt nC_g}{\delta_{\rm node}}\right\}\right\rceil
\bigg\}.
\end{split}
\]

Take exactly

\[
J=\left\lceil\frac{2T}{\widehat R_n}\right\rceil
 =\left\lceil\max\{4T/r_t,16TL_n\}\right\rceil
\]

equal physical-time panels, and use degree \(K\) for both parameter and
passive source jets. The first three cutoffs are backend (A22); the final
two are the bridge's source-jet cutoffs. This is an explicit sufficient
choice, not a claim of minimal degree.

## 9. What is and is not expressed solely through beta

There is no suppressed structural parameter in the preceding recipe.
Substituting inputs successively produces all
\(J,K,D,p,\ell_*,N_t,N_x,N,R,q\). The dataset enters through \(m,d\),
its actual label size \(Y\), its population gap \(\gamma\), and, for
exact qualification, its actual activation moments and source event.

The source power ledger provides useful bounds, already before its optional
small-label specialization:

\[
H_j^{\rm src}\le3\beta^{2j},\quad
k_j^{\rm src}\le3\beta^{4L-2j},\quad
\tau_j^{\rm src}\le3\beta^{4L-2j+1},\quad
P_j^{\rm src}\le\beta^{3j-2},\quad f_j^{\rm src}\le\beta^{3j-1},
\]
\[
K_{\rm src}\le\beta^{20L+2},\quad
T_Q\le\beta^{14L-3},\quad T_J\le\beta^{8L-1},\quad
S_*^{\rm src}\ge\beta^{-26L}.
\]

The full label interval implies \(S\le1\). Using this fact and the displayed
source formulas gives conservative full-interval envelopes

\[
U\le\beta^{40L}\sqrt{d+3},\qquad
V_{\rm qry}\le\beta^{36L}\sqrt{d+3},
\]
\[
c_t^{-1}\le4YS\beta^{40L+1}\sqrt{d+3},\qquad
c_q^{-1}\le\max\{8,\tfrac12\beta^{36L+1}\sqrt{d+3}\}.
\]

For example, the largest term inside the \(U_j\) bracket is bounded using
\(T_Q\le\beta^{14L-3}\); multiplication by
\(sK_{\rm src}\le\beta^{20L+3}\) is well below the generous
\(\beta^{40L}\) envelope. The \(G_dq_{j-1}^{\rm src}\) term is smaller.
Likewise \(sK_{\rm src}T_J\) is below
\(\beta^{28L+2}\), leaving ample room for the second envelope.
The radius bounds then use \(a^{-1}\le\beta/16\).
These bounds describe dependence; replacing exact mode definitions by looser
bounds may enlarge a sufficient budget and is not an assertion of unchanged
minimal counts.

On the additional smaller cap \(Y/\lambda\le\beta^{-30L}\), the source
ledger gives the sharper \(U\le\beta^{26L}\sqrt{d+3}\) and
\(V_{\rm qry}\le\beta^{2L}\sqrt{d+3}\). They are not used for the full
interval recipe.

Beta alone cannot recover the actual Gaussian moments \(H_D\), the data gap
\(\gamma\), the full original label interval, the scalar activation value
algorithm, or the effective stochastic width threshold. Coarse bounds can
replace some of these numerical coefficients conservatively, but cannot be
represented as exact recovery of them.

The formulas display powers exponential in depth, factorial/binomial and
tensor-product dependence on dimension, and possible exponential factors in
stability constants. They do not assert polynomial dependence jointly on
\(m,d,L,\beta,\gamma^{-1},Y^{-1},\delta^{-1}\).
In particular, \(N_x=N_\varphi N_\theta^{d-2}\) is not a dimension-free
polynomial bound. The qualitative source-width threshold prevents a complete
numerical confidence-to-work theorem, even though the conditional deterministic
orders at a supplied admissible width are explicit.

Confidence \(\delta\) does not otherwise enter the order formulas at fixed
admissible \(n\); the same source event covers every permitted \(T,\eta\).
No new tolerance-dependent probability event, label restriction, or unknown
trained-state norm has been inserted.
