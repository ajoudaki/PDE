<a id="harmonic-efficient-orders"></a>
<a id="setup-orders"></a>
#### Deterministic orders for both efficient initializers

The following finite recipe supplies all orders used by the explicit and
implicit local-continuation algorithms. It reuses the exact source and fitting
coefficients already defined in this document. Every new radius, tolerance,
degree and panel count is displayed here; their error and operation arguments
are in [the complete initializer proofs](#efficient-setup-proofs).
No norm of an unknown trained path is an input. Confidence affects the
inherited admissible-width qualification, whose source portion is still not
numerically quantified.

The proof components use shorter locally scoped names. In this prescription
\(R_{\rm loc},J_{\rm loc},V_{\rm loc}\) mean their local-continuation
\(R,J,V\); \(U_j^{\rm act},K_j^{\rm act},Q_j^{\rm act},C_F^{\rm act}\)
mean the activation component's \(U_j,K_j,Q_j,C_F\); and
\(B_{\rm act},\Delta_{\rm act}\) mean its ellipse scale \(B\) and gap
\(\Delta\). Quadrature names \(a_t,h_{\rm ang},\sigma_{\rm ang},\ell_*,\mathcal Y\)
mean its \(a,h,\sigma,\ell_*,\mathcal Y_{\ell_*}\). These are exact renamings, with
no rescaling of coefficients or changes to the inequalities.

<a id="setup-orders-detail-1"></a>
##### Inputs and conventions

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
components' local notation.

<a id="setup-orders-detail-2"></a>
##### Existing source constants and exact notation correspondence

Compute the source coefficients from the complete recurrences
(S.5)--(S.10), (S.22), (S.24)--(S.25), and (S.30) in
[the source foundations](#source-explicit-recurrences), in their displayed
order. Those recurrences already define every activation-only coefficient,
the source allowance \(S_*^{\rm src}\), \(K_{\rm src}\), and the actual-label
query radii \(r_t,r_q\); no source recurrence is duplicated here.

The notation correspondence is exact. Source-section
\(H_j,P_j,k_j,f_j,q_j,\tau_j\) become
\(H_j^{\rm src},P_j^{\rm src},k_j^{\rm src},f_j^{\rm src},q_j^{\rm src},\tau_j^{\rm src}\).
Write \(H_{\max}^{\rm src}=\max_jH_j^{\rm src}\),
\(k_*^{\rm src}=\max_jk_j^{\rm src}\),
\(f_*^{\rm src}=\max_jf_j^{\rm src}\), and
\(\tau_*^{\rm src}=\max_j\tau_j^{\rm src}\).
The \(V\) of (S.25) is denoted \(V_{\rm qry}\) here; \(U,T_Q,T_J,G_d\),
\(K_{\rm src},c_t,c_q,\mathcal K\) retain their source meanings.
The \(S=16Ym/\gamma\) appearing in those recurrences is the actual activity
allowance, not its upper bound one. The \(a\) in \(c_t,c_q\) is the activation
strip width. The source-budget tolerance in (S.10) is distinct from the
requested approximation error \(\eta\).


<a id="setup-orders-detail-3"></a>
##### Full original label interval

Use the [common exact label allowance](#detailed-statements), or the
[full Harmonic allowance](#harmonic-fitting-coefficients) when only the
Harmonic theorem is needed. With \(H_D=H_d\) and \(F_D=F_d\) from
(Harmonic dense coefficients), it is
\[
0<Y\le\lambda\min\{(8H_D\sqrt{F_D})^{-1},
S_*^{\rm Leg}/8,(16H_c\sqrt{F_c})^{-1},S_*^{\rm src}/16\}.
\]
The Legendre entry is omitted for Harmonic alone. The actual activation
Gaussian moments defining \(H_D\) are those of the dense fitting theorem;
they are supplied certificates when an exact allowance is evaluated.
The setup prescription adds no label restriction and does not replace this
interval by the optional sufficient cap \(Y\le\lambda\beta^{-30L}\).


<a id="setup-orders-detail-4"></a>
##### Width, confidence and inherited gates

Require \(n\ge\max(m,d)\), the explicit dense initialization threshold
\(N_{\rm fit}(\delta/32)\) from [dense fitting](#dense-fitting), and the
same source event at failure allowance at most \(\delta/32\).
The source threshold remains existential. The union bound needs no
independence; the lower-bound and central-limit events are not used here.
Retain every original radius, counting and analytic-extension gate in
[the Harmonic storage-and-gate statement](#harmonic-storage-count), including
the dimension-one gate and \(n^{-1}\le\eta_0\). These are explicit scalar
comparisons already written there. They do not test sampled matrix norms.

For use below, define the late-state displacement bound from
[the all-horizon extension](#harmonic-analytic-extension-proof),
\[
Z_n=(2Y/\sqrt\lambda+8Y\sqrt{\mathcal K}\,r_t)(en)^{-16}.
\]
The extension requires \(Z_n<b_{\rm ext}/2\), where \(b_{\rm ext}\) is
the radius denoted \(b_n\) in that earlier proof; this is distinct from the
numerical restart radius \(b_n\) defined below. Its second carrier gate is
also retained. The source amplitude and dimension coefficients used for the
exact mode count are
\[
M_{\rm amp}=10\max(H_L^{\rm src},\tau_*^{\rm src}),\qquad
b_d=2d-2,\quad D_d=2^{d+1}d^{d-2}\quad(d\ge2).
\]
No deterministic gate supplies the missing numerical confidence-to-width
threshold of the source event.


<a id="setup-orders-detail-5"></a>
##### Retained modes, rank and selected budget

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

A deterministic sufficient supplied budget is \(Q=\min(n,9R)\).
If \(9R\ge n\), use the original exact full-width fallback, rather than
assert compression. If the headline convention \(Q\ge18(2m+d+9)\) is
desired, use \(Q=\min(n,\max\{9R,18(2m+d+9)\})\).
The actual rank \(r=\max_j\dim E_j\le\min(n,R)\) may permit a smaller
budget \(9r\); that is computed after coefficient assembly and is not an
order-only prediction. No preservation of accidental rank deficiencies is
assumed. In the selected branch, the actual supports satisfy
\(q_j\le9r_j\), and the actual maximum \(q=\max_jq_j\) is the
quantity charged in the setup costs. Unused supplied budget \(Q\) is not padded.

<a id="setup-orders-detail-6"></a>
##### Positive quadrature orders

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

<a id="setup-orders-detail-7"></a>
##### Complex local continuation constants

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

<a id="setup-orders-detail-8"></a>
##### One activation polynomial and complete local degree

For the strong source-jet interface use
\(\delta_*=\delta_{\rm node}/(32\sqrt n)\), [the source-jet bridge](#setup-bridge)'s tightened
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
K=\max\bigg\{&8,
\left\lceil2\log_2\max\{1,16TV_{\rm loc}/e_d\}\right\rceil,
\left\lceil\log_2\max\{1,8V_{\rm loc}\widehat R_n/b_n\}\right\rceil,\\
&\left\lceil\log_2\max\left\{1,
\frac{128V_{\rm loc}\widehat R_n C_{\rm src}n^{3/2}}
     {\delta_{\rm node}}\right\}\right\rceil,
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
passive source jets. The first three cutoffs are backend [(Setup-A.22)](#eq-setup-a-22); the final
two are [the source-jet bridge](#setup-bridge)'s source-jet cutoffs. This is an explicit sufficient
choice, not a claim of minimal degree.

<a id="setup-orders-detail-9"></a>
##### What is and is not expressed solely through beta

There is no suppressed structural parameter in the preceding recipe.
Substituting inputs successively produces all
\(J,K,D,p,\ell_*,N_t,N_x,N,R,Q\). The dataset enters through \(m,d\),
its actual label size \(Y\), its population gap \(\gamma\), and, for
exact qualification, its actual activation moments and source event.

The [source power ledger](#source-power-ledger) provides useful bounds, already before its optional
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
