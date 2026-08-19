# RMS-normalized and direction-only weight-normalized mean-field \(\mu\)P networks

> **Corrected scope.**  The exact nonclosure statement in this report is
> non-invariance of the displayed frozen top-block ordinary monomial
> degree/rectangular cutoffs.  Full-system projector and matrix-word
> proliferation is diagnostic; it is not a proved dimension lower bound
> against every nonlinear, operator-valued, or approximate compressed state.
> The low-order coefficients are formal annealed jets unless a separate
> concentration/trajectory bridge is supplied.

## Audited order-four Taylor expansions and closure classification

### Executive conclusion

For the canonical two-hidden-layer, one-sample, scalar-output \(\mu\)P network, the two normalizations behave very differently at low Taylor order.

With quadratic activation \(\phi(u)=u^2/2\), middle-layer variance
\(\gamma/n\), centered Gaussian initialization, and the same \(\gamma=4/3\)
used in the unnormalized project notes, encode the formal annealed
feature-time jet through cubic order by

\[
F(\tau)\equiv A\tau+\frac{B}{3!}\tau^3\pmod{\tau^5}.
\]

The audited coefficients are

\[
\begin{array}{c|cc}
\text{model}&A=F'(0)&B=F'''(0)\\ \hline
\text{unnormalized}&\dfrac{17}{6}&\dfrac{229957}{216}\\[2mm]
\text{global readout direction-WN}&\dfrac{17}{6}&\dfrac{223939}{216}\\[2mm]
\text{RMS after both hidden activations}&\dfrac{34}{9}&-\dfrac{273712}{729}
\end{array}
\]

Thus RMSNorm causes a genuine sign reversal in the cubic feature-time coefficient. Direction-only weight normalization changes it by only

\[
\frac{229957-223939}{216}=\frac{1003}{36}.
\]

For label one and squared loss \(\mathcal L=(1-f)^2\), the formal
physical-time loss jet through order four is

\[
\boxed{
\mathcal L(t)
\equiv1-4At+8A^2t^2
-\frac{32A^3+8B}{3}t^3
+\frac{32A^4+44AB}{3}t^4
\pmod{t^5}.
}
\]

Consequently,

\[
\boxed{
\mathcal L_{\rm RMS}(t)
\equiv1-\frac{136}{9}t
+\frac{9248}{81}t^2
+\frac{103552}{243}t^3
-\frac{40745600}{2187}t^4
\pmod{t^5},
}
\]

whereas

\[
\boxed{
\mathcal L_{\rm WN}(t)
\equiv1-\frac{34}{3}t
+\frac{578}{9}t^2
-\frac{81197}{27}t^3
+\frac{14181587}{324}t^4
\pmod{t^5}.
}
\]

These are formal Taylor coefficients, not derivatives of an independently
constructed curve. Multiplying the coefficient of \(t^m\) by \(m!\) gives
the corresponding formal value denoted \(\mathcal L^{(m)}(0)\) below.

The closure conclusion is more subtle:

1. In the displayed frozen reductions, neither normalization leaves any
   finite ordinary degree/rectangular monomial cutoff invariant. RMSNorm adds
   reciprocal-moment, projection, and Bell-partition vertices; WN leaves a
   proliferating tangential word grammar in the full formal calculation.
2. The old coefficientwise-positive Wick lower bound does **not** transfer to RMSNorm or to global readout direction-WN, because both introduce negative projection terms. Therefore the old zero-radius proof cannot simply be reused.
3. If WN is applied only to hidden rows and not to the readout, the source's
   fixed-order calculation makes its corrections vanish under the declared
   large-fan-in convention; subject to that reduction, the raw formal-jet
   Taylor no-go transfers.
4. The broad impossibility of every non-Taylor, accuracy-dependent finite PDE
   remains unproved.  Full-system word proliferation alone does not upgrade
   the frozen-cutoff theorem to such a result.

---

## 1. Exact model and coordinate convention

There is one fixed input, so it is suppressed. Both hidden widths are \(n\). In the rescaled mean-field coordinates,

\[
z_i^{(1)}(0)\sim N(0,1),\qquad
W_{ji}^{(2)}(0)\sim N\!\left(0,\frac\gamma n\right),\qquad
a_j(0)\sim N(0,1),
\]

independently. The raw \(\mu\)P readout is

\[
W_j^{(3)}=\frac{a_j}{n},
\qquad
W_j^{(3)}(0)\sim N(0,n^{-2}),
\]

and

\[
f_n=\sum_jW_j^{(3)}h_j^{(2)}
=\frac1n\sum_ja_jh_j^{(2)}.
\]

Thus the use of \(a\sim N(0,1)\) below is only the rescaled version of the raw readout specified by \(W^{(3)}\sim N(0,n^{-2})\).

For the unnormalized network,

\[
h^{(1)}=\phi(z^{(1)}),\qquad
z^{(2)}=W^{(2)}h^{(1)},\qquad
h^{(2)}=\phi(z^{(2)}),\qquad
f_n=\langle a,h^{(2)}\rangle,
\]

where

\[
\langle v,w\rangle:=\frac1n\sum_i v_iw_i,
\qquad
\langle v\rangle:=\frac1n\sum_i v_i.
\]

The feature-ascent derivation is

\[
D_+z^{(1)}=n\nabla_{z^{(1)}}f_n,
\qquad
D_+W^{(2)}=\nabla_{W^{(2)}}f_n,
\qquad
D_+a=n\nabla_af_n.
\]

For label \(y\) and loss

\[
\mathcal L_n=(y-f_n)^2,
\]

write \(F_n(\tau)\) for the value of \(f_n\) along the finite-width
feature-ascent orbit. Physical gradient flow follows exactly the same orbit
with clock

\[
\dot\tau_n=2\bigl(y-F_n(\tau_n)\bigr),
\qquad
f_n(t)=F_n(\tau_n(t)).
\]

All network-dependent Taylor calculations can therefore be done once in feature time and converted exactly to physical time.

---

## 2. Universal loss jet through order five

All equalities in this section are identities of formal annealed power
series. They do not assert existence of a positive-time limiting trajectory.

Let

\[
k_j=D_+^j\kappa(0)=F^{(j+1)}(0),
\qquad
\kappa=F'.
\]

For centered mean-field initialization, \(F(0)=0\). For label one, direct series substitution into

\[
\dot\tau=2(1-F(\tau)),\qquad \mathcal L=(1-F(\tau))^2
\]

gives

\[
\mathcal L'(0)=-4k_0,
\]

\[
\mathcal L''(0)=16k_0^2-8k_1,
\]

\[
\mathcal L'''(0)
=-64k_0^3+112k_0k_1-16k_2,
\]

\[
\mathcal L^{(4)}(0)
=256k_0^4-1056k_0^2k_1+224k_1^2+352k_0k_2-32k_3,
\]

and

\[
\begin{aligned}
\mathcal L^{(5)}(0)
={}&-1024k_0^5+8384k_0^3k_1-6016k_0k_1^2
-4928k_0^2k_2\\
&+1600k_1k_2+1024k_0k_3-64k_4.
\end{aligned}
\]

The centered readout law is antipodally symmetric. At the finite-width formal
level, replacing \(a(0)\) by \(-a(0)\) reverses feature time in the hidden
variables and reverses the readout sign. After annealed averaging, the formal
jet obeys

\[
F(-\tau)=-F(\tau).
\]

This symmetry survives RMSNorm and global direction-only readout WN. Hence

\[
k_1=k_3=0.
\]

Writing

\[
A=k_0=F'(0),\qquad
B=k_2=F'''(0),\qquad
C=k_4=F^{(5)}(0),
\]

one obtains

\[
F(\tau)\equiv A\tau+\frac{B}{3!}\tau^3+\frac{C}{5!}\tau^5
\pmod{\tau^7},
\]

and

\[
\begin{aligned}
\mathcal L(t)
\equiv{}&1-4At+8A^2t^2
-\frac{32A^3+8B}{3}t^3\\
&+\frac{32A^4+44AB}{3}t^4\\
&-\left(\frac{128}{15}A^5+\frac{616}{15}A^2B+\frac{8}{15}C\right)t^5
\pmod{t^6}.
\end{aligned}
\]

Order four therefore requires only \(A\) and \(B\). Order five additionally requires the fifth-order Gaussian jet \(C\).

For a general label \(y\), the same formula holds after multiplying the pure-\(A\) terms by \(y^2\), the terms linear in \(B\) by \(y^4\), and the term linear in \(C\) by \(y^6\). In particular,

\[
\begin{aligned}
\mathcal L_y(t)
\equiv{}&y^2-4y^2At+8y^2A^2t^2\\
&-\left(\frac{32}{3}y^2A^3+\frac83y^4B\right)t^3\\
&+\left(\frac{32}{3}y^2A^4+\frac{44}{3}y^4AB\right)t^4
\pmod{t^5}.
\end{aligned}
\]

---

## 3. RMSNorm after each hidden activation

### 3.1 Convention

The primary calculation uses true across-width RMSNorm, recomputed at every feature time, with no learned gain, no centering, and \(\varepsilon_1=\varepsilon_2=0\):

\[
s_\ell^2=\langle (h^{(\ell)})^2\rangle,
\qquad
u^{(\ell)}=\frac{h^{(\ell)}}{s_\ell}.
\]

The network is

\[
h^{(1)}=\phi(z^{(1)}),\qquad
u^{(1)}=\frac{h^{(1)}}{s_1},
\]

\[
z^{(2)}=W^{(2)}u^{(1)},\qquad
h^{(2)}=\phi(z^{(2)}),\qquad
u^{(2)}=\frac{h^{(2)}}{s_2},
\]

\[
f=\langle a,u^{(2)}\rangle.
\]

Freezing \(s_\ell\) at initialization would be fixed rescaling, not RMSNorm, and gives the wrong higher coefficients.

### 3.2 Exact feature-time vector field

Define the normalized-activation Jacobian

\[
J_\ell
=\frac1{s_\ell}
\left(I-u^{(\ell)}\otimes u^{(\ell)}\right)
\operatorname{diag}\phi'(z^{(\ell)}),
\]

where

\[
(u\otimes u)v=u\langle u,v\rangle.
\]

Put

\[
\delta_2=J_2^*a
=\frac{\phi'(z^{(2)})}{s_2}
\odot\bigl(a-fu^{(2)}\bigr),
\]

\[
b=(W^{(2)})^\top\delta_2,
\qquad
\delta_1=J_1^*b.
\]

Then

\[
D_+a=u^{(2)},
\]

\[
D_+W^{(2)}=\frac1n\delta_2(u^{(1)})^\top,
\]

\[
D_+z^{(1)}=\delta_1,
\]

and

\[
D_+z^{(2)}
=\delta_2+W^{(2)}J_1\delta_1.
\]

The tangent kernel is the exact sum of metric-gradient squares

\[
\boxed{
\kappa_{\rm RMS}
=1+\langle\delta_2^2\rangle+\langle\delta_1^2\rangle.
}
\]

The constant \(1\) is only the normalized readout contribution. The two hidden terms remain distributional/message-valued.

### 3.3 General-activation value of \(A\)

The formula with fixed \(\varepsilon_\ell\ge0\) is useful. Let

\[
G_1\sim N(0,1),
\]

\[
q_1=\mathbb E\phi(G_1)^2,
\qquad
s_1^2=q_1+\varepsilon_1,
\qquad
\rho_1=\frac{q_1}{s_1^2},
\qquad
\chi_1=\frac{\mathbb E\phi'(G_1)^2}{s_1^2}.
\]

Since \(\mathbb E[(u^{(1)})^2]=\rho_1\),

\[
G_2\sim N(0,\gamma\rho_1).
\]

Define

\[
q_2=\mathbb E\phi(G_2)^2,
\qquad
s_2^2=q_2+\varepsilon_2,
\qquad
\rho_2=\frac{q_2}{s_2^2},
\qquad
\chi_2=\frac{\mathbb E\phi'(G_2)^2}{s_2^2}.
\]

An explicit Gaussian contraction gives

\[
\boxed{
A_{\rm RMS}
=\rho_2+\rho_1\chi_2+\gamma\chi_1\chi_2.
}
\]

For exact RMSNorm, \(\rho_1=\rho_2=1\), so

\[
A_{\rm RMS}=1+\chi_2(1+\gamma\chi_1).
\]

### 3.4 Exact Gaussian-jet formula for \(B\)

This subsection gives a finite, directly evaluable Gaussian integral formula; it does not hide a positive-time solution.

For a vector \(x\), define

\[
N(x)=\frac{\phi(x)}{\sqrt{\langle\phi(x)^2\rangle+\varepsilon}}.
\]

Let

\[
y=\phi(x),\qquad s^2=\langle y^2\rangle+\varepsilon.
\]

For a direction \(p\), put

\[
y_p=\phi'(x)p,
\qquad
r_p=\langle y,y_p\rangle.
\]

Then

\[
N'[p]=\frac{y_p}{s}-\frac{yr_p}{s^3}.
\]

For directions \(p,q\), put

\[
y_{pq}=\phi''(x)pq,
\qquad
r_{pq}=\langle y_p,y_q\rangle+\langle y,y_{pq}\rangle.
\]

Then

\[
\boxed{
N''[p,q]
=\frac{y_{pq}}s
-\frac{y_pr_q+y_qr_p+yr_{pq}}{s^3}
+\frac{3yr_pr_q}{s^5}.
}
\]

For a third direction \(r\), define

\[
y_{pqr}=\phi'''(x)pqr,
\]

\[
r_{pqr}
=\langle y_{pr},y_q\rangle
+\langle y_p,y_{qr}\rangle
+\langle y_r,y_{pq}\rangle
+\langle y,y_{pqr}\rangle.
\]

Writing

\[
g_p=-\frac{r_p}{s^3},
\]

\[
g_{pq}=-\frac{r_{pq}}{s^3}+\frac{3r_pr_q}{s^5},
\]

\[
g_{pqr}
=-\frac{r_{pqr}}{s^3}
+\frac{3(r_pr_{qr}+r_qr_{pr}+r_rr_{pq})}{s^5}
-\frac{15r_pr_qr_r}{s^7},
\]

the full third derivative is

\[
\boxed{
\begin{aligned}
N'''[p,q,r]
={}&\frac{y_{pqr}}s
+y_{pq}g_r+y_{pr}g_q+y_{qr}g_p\\
&+y_pg_{qr}+y_qg_{pr}+y_rg_{pq}+yg_{pqr}.
\end{aligned}
}
\]

At Gaussian initialization abbreviate

\[
v=N_1(z^{(1)}),\qquad
z=Wv,
\qquad
u=N_2(z),
\]

\[
J_\ell=N_\ell',
\qquad
\delta=J_2^*a,
\qquad
b=W^\top\delta.
\]

The feature-ascent direction is

\[
g_a=u,
\qquad
g_W=\frac1n\delta v^\top,
\qquad
g_x=J_1^*b.
\]

Form the straight-direction activation jets

\[
v_1=J_1g_x,
\qquad
v_2=N_1''[g_x,g_x],
\qquad
v_3=N_1'''[g_x,g_x,g_x],
\]

\[
z_1=g_Wv+Wv_1,
\]

\[
z_2=2g_Wv_1+Wv_2,
\]

\[
z_3=3g_Wv_2+Wv_3,
\]

\[
u_1=J_2z_1,
\]

\[
u_2=N_2''[z_1,z_1]+J_2z_2,
\]

\[
u_3=N_2'''[z_1,z_1,z_1]+3N_2''[z_1,z_2]+J_2z_3.
\]

The first directional derivative of the backpropagated message is

\[
\delta_1
=N_2''[z_1,\cdot]^*a+J_2^*u,
\]

\[
b_1=g_W^\top\delta+W^\top\delta_1.
\]

The Hessian-gradient components are

\[
r_a=u_1,
\]

\[
r_W=\frac1n(\delta_1v^\top+\delta v_1^\top),
\]

\[
r_x=N_1''[g_x,\cdot]^*b+J_1^*b_1.
\]

Define the two explicit Gaussian contractions

\[
T_{\rm RMS}
=\lim_{n\to\infty}
\mathbb E\left[\langle a,u_3\rangle+3\langle u,u_2\rangle\right],
\]

\[
Q_{\rm RMS}
=\lim_{n\to\infty}
\mathbb E\left[
\langle r_a^2\rangle+\|r_W\|_F^2+\langle r_x^2\rangle
\right].
\]

Then the exact full-model cubic coefficient is

\[
\boxed{
B_{\rm RMS}=2T_{\rm RMS}+4Q_{\rm RMS}.
}
\]

Every quantity on the right is an explicit polynomial/rational function of initialization Gaussians and the scalar expectations appearing in \(N'\), \(N''\), and \(N'''\). Expanding its Wick pairings gives the requested finite sum of products of Gaussian integrals. For a generic activation, \(\phi'''\) genuinely appears at this order. Restriction to only \(\phi,\phi',\phi''\) is automatic for the quadratic activation because \(\phi'''=0\). Gaussian integration by parts can sometimes eliminate higher activation derivatives under additional boundary assumptions, but that is a separate identity, not an automatic property of the Taylor expansion.

### 3.5 Fully evaluated quadratic result

For

\[
\phi(u)=\frac12u^2,
\qquad
\varepsilon_1=\varepsilon_2=0,
\]

one has

\[
u^{(1)}=\frac{G_1^2}{\sqrt3},
\qquad
G_2\sim N(0,\gamma),
\qquad
u^{(2)}=\frac{G_2^2}{\sqrt3\,\gamma}.
\]

Using

\[
\mathbb E[G^{2m}]=(2m-1)!!
\]

in the preceding jet gives

\[
\boxed{
A_{\rm RMS}(\gamma)
=\frac{25}{9}+\frac{4}{3\gamma},
}
\]

and

\[
\boxed{
B_{\rm RMS}(\gamma)
=-\frac{117760}{729}
-\frac{15616}{81\gamma}
-\frac{2848}{27\gamma^2}
-\frac{640}{27\gamma^3}.
}
\]

For the old project value \(\gamma=4/3\),

\[
A_{\rm RMS}=\frac{34}{9},
\qquad
B_{\rm RMS}=-\frac{273712}{729}.
\]

The independently audited Wick groups at this value are

\[
T_{\rm RMS}=-\frac{9445}{18},
\qquad
Q_a=\frac{881}{27},
\qquad
Q_W=\frac{15233}{324},
\qquad
Q_x=\frac{64772}{729},
\]

so that

\[
Q_a+Q_W+Q_x=\frac{491333}{2916},
\qquad
2T_{\rm RMS}+4(Q_a+Q_W+Q_x)
=-\frac{273712}{729}.
\]

If instead \(\gamma\) is retuned to \(1\), so that \(z^{(2)}(0)\sim N(0,1)\) after first-layer RMSNorm, then

\[
A_{\rm RMS}=\frac{37}{9},
\qquad
B_{\rm RMS}=-\frac{352480}{729},
\]

and

\[
\mathcal L_{\rm RMS,\gamma=1}(t)
\equiv1-\frac{148}{9}t
+\frac{10952}{81}t^2
+\frac{133216}{243}t^3
-\frac{57096032}{2187}t^4
\pmod{t^5}.
\]

---

## 4. Direction-only weight normalization

### 4.1 The convention is part of the model

"Weight normalization" is ambiguous unless the following are fixed:

1. direct projected/Riemannian gradient on the weight sphere versus Euclidean training of an auxiliary \(v\) in \(w=g v/\|v\|\);
2. rowwise hidden normalization versus one global readout sphere;
3. whether the readout is included;
4. fixed input dimension versus a large-fan-in first layer;
5. deterministic versus random fixed gains.

The primary calculation uses direct projected gradient

\[
D_+w=P_wG,
\qquad
P_w=I-\frac{ww^\top}{\|w\|^2},
\]

on every hidden row and on the global rescaled readout vector. Hidden incoming dimensions are taken large in the fixed-order tensor-program sense. This is the convention under which the Gaussian-kernel initialization in the question remains coherent.

For the rescaled readout, put

\[
C=\langle a^2\rangle.
\]

The global sphere projection gives

\[
\boxed{
D_+a=h^{(2)}-\frac fC a,
}
\]

and keeps \(C\) exactly constant.

Its tangent-kernel contribution is

\[
\langle(h^{(2)})^2\rangle-\frac{f^2}{C}.
\]

For a middle row \(W_j\) with fixed \(\|W_j\|^2=g_j^2=O(1)\),

\[
D_+W_j
=\frac{a_j\phi'(z_j^{(2)})}{n}
\left(
h^{(1)}-\frac{z_j^{(2)}}{g_j^2}W_j
\right).
\]

Therefore

\[
(D_+W_j)\cdot h^{(1)}
=a_j\phi'(z_j^{(2)})
\left(
q_1-\frac{(z_j^{(2)})^2}{ng_j^2}
\right).
\]

The displayed first radial correction is \(O(n^{-1})\). The source reports
that analogous corrections disappear at every separately fixed derivative
order under the same large-fan-in convention.  That all-order transfer is an
additional fixed-order reduction claim; it does not follow from the displayed
first-order estimate alone.  The global readout projection is the surviving
\(O(1)\) modification in the orders computed here.

If the first-layer input dimension \(d\) is fixed, its projector does survive. For a row \(v_i\), fixed input \(x\), and \(z_i^{(1)}=v_i\cdot x\),

\[
D_+z_i^{(1)}
=\beta_i
\left(
\|x\|^2-\frac{(z_i^{(1)})^2}{\|v_i\|^2}
\right),
\]

where \(\beta_i\) is the unprojected scalar backpropagation signal. The Taylor coefficients then contain joint spherical/gain integrals, not only Gaussian activation moments. If a scalar collapsed \(z_i^{(1)}\) is itself "weight-normalized," its direction is only a sign and direction-only training freezes it; that is a different, degenerate model.

### 4.2 General-activation value of \(A\)

Under the primary large-fan-in convention, let

\[
G_1\sim N(0,1),
\]

\[
Q_1=\mathbb E\phi(G_1)^2,
\qquad
P_1=\mathbb E\phi'(G_1)^2,
\]

and

\[
G_2\sim N(0,\gamma Q_1),
\]

\[
R=\mathbb E\phi(G_2)^2,
\qquad
P_2=\mathbb E\phi'(G_2)^2.
\]

Because \(f(0)=0\), the readout projector has no effect on the initial tangent kernel. Hence

\[
\boxed{
A_{\rm WN}
=R+Q_1P_2+\gamma P_1P_2.
}
\]

For fixed input dimension, replace \(P_1\) in the last term by the corresponding joint integral

\[
\mathbb E\left[
\left(
\|x\|^2-\frac{G_1^2}{g^2}
\right)\phi'(G_1)^2
\right].
\]

### 4.3 Explicit unnormalized Gaussian jet for \(B\)

The readout-WN result is simplest when expressed as an exact correction to the raw hidden-network jet.

At initialization set

\[
h=\phi(x),
\qquad
z=Wh,
\qquad
u=\phi(z),
\]

\[
\delta=a\phi'(z),
\qquad
b=W^\top\delta.
\]

The unnormalized feature-gradient direction is

\[
g_a=u,
\qquad
g_W=\frac1n\delta h^\top,
\qquad
g_x=\phi'(x)b.
\]

Define the straight-direction jets

\[
h_1=\phi'(x)g_x,
\qquad
h_2=\phi''(x)g_x^2,
\qquad
h_3=\phi'''(x)g_x^3,
\]

\[
z_1=g_Wh+Wh_1,
\]

\[
z_2=2g_Wh_1+Wh_2,
\]

\[
z_3=3g_Wh_2+Wh_3,
\]

\[
u_1=\phi'(z)z_1,
\]

\[
u_2=\phi''(z)z_1^2+\phi'(z)z_2,
\]

\[
u_3=\phi'''(z)z_1^3+3\phi''(z)z_1z_2+\phi'(z)z_3.
\]

Also set

\[
\delta_1=u\phi'(z)+a\phi''(z)z_1,
\]

\[
b_1=g_W^\top\delta+W^\top\delta_1,
\]

and

\[
r_a=u_1,
\]

\[
r_W=\frac1n(\delta_1h^\top+\delta h_1^\top),
\]

\[
r_x=\phi''(x)g_xb+\phi'(x)b_1.
\]

Then

\[
T_0
=\lim_{n\to\infty}
\mathbb E\left[\langle a,u_3\rangle+3\langle u,u_2\rangle\right],
\]

\[
Q_0
=\lim_{n\to\infty}
\mathbb E\left[
\langle r_a^2\rangle+\|r_W\|_F^2+\langle r_x^2\rangle
\right],
\]

and the raw full-network coefficient is

\[
\boxed{
B_0=2T_0+4Q_0.
}
\]

This is the explicit finite Gaussian integral whose Wick expansion was evaluated below.

### 4.4 Exact readout-sphere correction

Split the initial kernel into its readout and hidden parts:

\[
A=R+S,
\qquad
R=\mathbb E\phi(G_2)^2.
\]

At \(f=0\), the WN and raw vector fields have the same first velocity, so \(A\) is unchanged. At the next nonzero odd order, the projected readout equation contributes two effects:

1. differentiating the kernel subtraction \(-f^2/C\) gives \(-2A^2/C\);
2. the changed readout acceleration differentiates the hidden kernel, which is quadratic in \(a\), giving \(-2A(A-R)/C\).

Therefore

\[
\boxed{
B_{\rm WN}
=B_0-\frac{2A(2A-R)}{C}.
}
\]

This correction was obtained independently from the projected vector field and from the kernel decomposition.

### 4.5 Fully evaluated quadratic result

For \(\phi(u)=u^2/2\),

\[
Q_1=\frac34,
\qquad
G_2\sim N\!\left(0,\frac{3\gamma}{4}\right),
\]

and

\[
\boxed{
A(\gamma)
=\frac{75}{64}\gamma^2+\frac{9}{16}\gamma.
}
\]

The full Wick evaluation of the raw jet gives

\[
\boxed{
B_0(\gamma)
=\frac{5205}{32}\gamma^4
+\frac{47511}{256}\gamma^3
+\frac{15201}{256}\gamma^2
+\frac{243}{64}\gamma.
}
\]

With \(C=1\), the projected readout result is

\[
\boxed{
B_{\rm WN}(\gamma)
=\frac{323895}{2048}\gamma^4
+\frac{92565}{512}\gamma^3
+\frac{14877}{256}\gamma^2
+\frac{243}{64}\gamma.
}
\]

At \(\gamma=4/3\),

\[
A=\frac{17}{6},
\qquad
B_0=\frac{229957}{216},
\qquad
B_{\rm WN}=\frac{223939}{216}.
\]

For a coefficient-by-coefficient audit, the raw Wick groups at this value are

\[
T_0=\frac{5971}{96},
\qquad
Q_x=\frac{20675}{108},
\qquad
Q_W=\frac{1617}{64},
\qquad
Q_a=\frac{881}{48},
\]

and hence

\[
2T_0+4(Q_x+Q_W+Q_a)=\frac{229957}{216}.
\]

The independent readout/hidden split is

\[
R=\frac34,
\qquad
S=A-R=\frac{25}{12},
\]

which gives

\[
\frac{2A(R+2S)}C=\frac{1003}{36}
\]

for the sphere correction.

If the readout is excluded from WN, then the computed coefficient satisfies
\(B=B_0\). The extension saying that every separately fixed-order coefficient
equals the raw one is the additional large-fan-in reduction claim just
described.

---

## 5. Independent reduction checks

### 5.1 RMS top-block check

Freeze the first hidden block, use quadratic activation and \(z(0)\sim N(0,1)\), and train the middle feature plus readout under final RMSNorm. Define

\[
M_{p,r}=\mathbb E[a^p z^r],
\qquad
R^2=M_{0,4},
\qquad
f=\frac{M_{1,2}}R.
\]

The exact moment equations are

\[
a'=\frac{z^2}{R},
\qquad
z'=\frac{2z}{R}\left(a-\frac{fz^2}{R}\right),
\]

\[
M_{p,r}'
=\frac pR M_{p-1,r+2}
+\frac{2r}{R}M_{p+1,r}
-\frac{2rf}{R^2}M_{p,r+2}.
\]

For independent standard Gaussian \(a,z\),

\[
\boxed{
F(\tau)
=\frac73\tau
-\frac{464}{81}\tau^3
+\frac{174368}{3645}\tau^5
+O(\tau^7).
}
\]

This catches omitted denominator derivatives and projection terms.

### 5.2 Readout-WN top-block check

Freeze the first hidden block and use

\[
q=\mathbb E[(h^{(1)})^2]=\frac34,
\qquad
z(0)\sim N(0,1),
\qquad
C=1.
\]

Then

\[
a'=\frac12z^2-fa,
\qquad
z'=qaz,
\qquad
f=\frac12\mathbb E[az^2],
\]

and

\[
M_{p,r}'
=\frac p2M_{p-1,r+2}-pfM_{p,r}+rqM_{p+1,r}.
\]

The exact feature-time series is

\[
\boxed{
F(\tau)
=\frac32\tau
+\frac{75}{16}\tau^3
+\frac{8181}{640}\tau^5
+O(\tau^7).
}
\]

If hidden features are also frozen, direct readout-sphere ascent reduces further to

\[
F(\tau)
=\sqrt{CQ}\,
\tanh\!\left(\sqrt{\frac QC}\,\tau\right),
\qquad
Q=\mathbb E[(h^{(2)})^2].
\]

---

## 6. What the Taylor graphs say about closure

### 6.1 RMSNorm

The first differentiated second-layer message is already

\[
D_+z^{(2)}
=\left(I+WJ_1J_1^*W^\top\right)\delta_2.
\]

At higher order, differentiating

\[
J_\ell=s_\ell^{-1}P_\ell\operatorname{diag}\phi'
\]

creates three new families in addition to the raw matrix-reuse words:

1. derivatives of \(s_\ell^{-1}\), indexed by set/Bell partitions of the derivative hits;
2. derivatives of \(P_\ell=I-u^{(\ell)}\otimes u^{(\ell)}\), producing new outer-product attachments;
3. disconnected products of population contractions such as \(\langle h^{(p)},h^{(q)}\rangle\).

The number and grade of these decorated words grows with every derivative
order. RMSNorm fixes one second moment per layer; it does not determine the
higher mixed moments or the noncommutative messages.  This is a grammar-growth
statement, not proof that those words are all independent, reachable, or
immune to operator-valued compression.

The frozen-block recurrence above makes this nonclosure explicit. The derivative of \(M_{p,r}\) contains \(M_{p-1,r+2}\), \(M_{p+1,r}\), and \(M_{p,r+2}\). No finite degree cutoff is invariant.

### 6.2 Direction-only WN

For a fixed-radius row,

\[
P_w^{(m)}
=-\frac1{\|w\|^2}
\sum_{p=0}^m{m\choose p}
w^{(p)}(w^{(m-p)})^\top.
\]

Thus projector words also proliferate at every order. Under the report's
additional all-fixed-order large-fan-in reduction, their radial contributions
vanish at each separately fixed formal order, leaving the raw noncommutative
grammar. The displayed first-order estimate does not prove that reduction.
The global readout projector adds the scalar attachment \(-fa/C\), but does not identify
or eliminate the hidden message words.  Proliferation is not by itself a
full-system no-compression theorem.

Again, the exact frozen-block recurrence raises \(p\) or \(r\), proving that
no finite degree or rectangular cutoff in this ordinary monomial hierarchy is
invariant.

### 6.3 Why the old positivity proof no longer applies

The raw quadratic network was polynomial with nonnegative primitive coefficients. A selected positive scalar derivative history therefore survived Gaussian averaging as a lower bound, yielding factorial coefficient growth and zero Taylor radius.

RMSNorm contains

\[
a-fu,
\]

as well as alternating derivatives of \(s^{-1}\). Readout WN contains

\[
-\frac fC a.
\]

These terms have negative primitive coefficients. Wick-surviving graphs can now cancel. The embedded positive raw branch is no longer automatically a lower bound on the full normalized coefficient.

The tails themselves have not disappeared. For quadratic RMSNorm,

\[
u=\frac{G^2}{\sqrt3},
\qquad
\mathbb E[u^p]
=\frac{(2p-1)!!}{3^{p/2}}.
\]

Likewise, at initialization a coordinate of a radius-\(\sqrt n\) sphere
converges to a standard Gaussian. Therefore factorial raw moments remain
available, but a new signed asymptotic argument would be needed to prove zero
radius after normalization.

---

## 7. Precise PDE classification

The results support the following classification.

| Claim | RMSNorm | Direction-only WN |
|---|---:|---:|
| Low-order Taylor pattern changes substantially | Yes | Only mildly if readout is included |
| Invariant finite ordinary monomial cutoff in the displayed frozen top block | No | No |
| Full trained-system finite nonlinear/operator compression ruled out | No | No |
| Full message/graph independence and no-compression theorem | Not proved | Not proved |
| Raw positive-Wick lower bound transfers verbatim | No | No if readout projected; conditional for hidden-only WN on the reported all-fixed-order large-fan-in reduction |
| Zero radius of the normalized Taylor series proved here | No | No for global readout WN |
| Ordinary Taylor-jet PDE proved convergent | No | No |
| Every possible non-Taylor finite PDE ruled out | No | No |
| Certified real-axis approximation potentially more regular | Plausible, unproved | Plausible with controlled gains, unproved |

The strongest defensible conclusion is therefore:

\[
\boxed{
\text{Normalization changes the coefficients, while the displayed frozen monomial cutoffs remain non-invariant.}
}
\]

RMSNorm does change the cancellation pattern dramatically enough that the previous no-go theorem must be reproved from scratch if one wants a normalized zero-radius result. Conditional on the reported all-fixed-order large-fan-in reduction, direction-only hidden-row WN is almost invisible to the leading hidden mean-field Taylor hierarchy; its main \(O(1)\) effect in the computed orders is the global readout-sphere correction.

The broad non-Taylor approximation question remains logically separate. A finite ODE can always be packed syntactically into one source, and an exact curve can be encoded oracularly. A substantive positive theorem still needs a non-oracular compiler, a real-axis state space, a residual estimate, and a structure-preserving nonnegative kernel reconstruction. These low-order Taylor computations neither provide that theorem nor rule it out.

---

## 8. Audit trail and checks

The calculation was checked in four independent ways.

1. The physical-time coefficients were derived both by direct formal series substitution and by differentiating \(\dot{\mathcal L}=-4\kappa\mathcal L\) together with the residual clock.
2. Antipodal readout symmetry independently forces \(F''(0)=F^{(4)}(0)=0\); any nonzero deterministic value at those orders signals a missing pairing or projection term.
3. The WN shift
   \[
   -\frac{2A(2A-R)}C
   \]
   was derived both from the projected readout vector field and from the readout/hidden kernel decomposition.
4. Direct finite-width truncated-power-series integration, used only as an audit, converged toward
   \[
   B_{\rm RMS}\approx-375.46,
   \qquad
   B_{\rm WN}\approx1036.75,
   \]
   and the two frozen-block reductions reproduce their exact order-five series.

The key convention checks are:

- true RMSNorm must differentiate its time-dependent denominator;
- derivatives and Taylor coefficients differ by factorials;
- the squared-loss clock contributes the factors of two in the physical series;
- WN must be defined in the ambient weight space, not on a collapsed scalar preactivation;
- positive semidefiniteness of a matrix message does not imply coordinatewise positivity;
- for a generic activation, order four invokes \(\phi'''\), and order five invokes still higher derivatives unless a justified Gaussian integration-by-parts reduction is supplied.
