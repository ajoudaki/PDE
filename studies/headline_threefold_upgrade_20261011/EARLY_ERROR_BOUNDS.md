# Compression errors retain their initial-time factor

Research proof, 2026-10-11. This note strengthens the deterministic comparison
on the existing source/fitting event. It does not establish that event with a
new quantitative probability or prove a dense same-time lower bound.

## Statement and dependencies

Use exactly the canonical network, data, mobilities, activation class and label
cap of `paper/compact.tex`. In particular, \(Y=\|y\|_2/\sqrt m>0\),
\(\gamma=\lambda_{\min}(Q^{(L)})>0\),
\(\gamma/m\le1\), and \(Y\le(\gamma/m)\beta^{-30L}\).
For a compressed predictor define the error at one time, not a trajectory norm,

\[
E_n(t)=\sup_{x\in\mathcal X}|f_{\mathrm{model}}(t,x)-f_n(t,x)|.
\]

The domain is the sphere for Legendre and Harmonic, and the declared training
plus passive panel for Taylor. On the same events and at the same eventual
orders used by the paper,

\[
\begin{aligned}
E_n(t)&\le
\frac{C Y}{\sqrt n[\log(en)]^3}\min\{t,1\}
&&\text{(Legendre)},\\
E_n(t)&\le\frac{C Y}{n}\min\{t,1\}
&&\text{(Harmonic and Taylor)}.
\end{aligned}                                                    \tag{1}
\]

Here \(C\) depends only on activations and depth. The inequalities hold
simultaneously for every \(t\in[0,\infty]\), with the factor at infinity
defined to be one. No nonaffinity assumption is needed. The orders and retained
state bounds do not change; increasing the activation/depth constant in the
existing source tolerance can make the second constant one if desired.

The proof inputs are the projection identities, fitting proof, signed
comparison and absorption estimate of `paper/compact_legendre.tex`, and the
pair-defect, cancelled-energy and scalar integral comparison in
`paper/compact_selected.tex`. The modifications below are proved explicitly.
This is an extension of those proofs, not a replacement of their source-event
construction.

## 1. Legendre: keep the actual clock activity

All symbols in this section are local. Put \(\lambda=\gamma/m\),
\(z=Y/\lambda\). Use the original, unchanged residual clock

\[
A(t)=1+\int_0^t\widehat\rho(s)\,ds,
\qquad a_0=4z,
\]

where \(\widehat\rho\) is the compressed training residual RMS. Its fitting
proof gives \(\widehat\rho(t)\le Y\) and
\(0\le A(t)-1\le a_0\). Thus

\[
\frac{A(t)-1}{a_0}\le\min\{\lambda t/4,1\}
\le\min\{t,1\}.                                                \tag{2}
\]

In the existing comparison proof \(V_h\widehat\rho\) bounds the forward
feature speed in neuron RMS, so its clock derivative is bounded by \(V_h\).
The history is constant on its artificial prefix \([0,1]\). The weighted
Legendre tail estimate at a terminal clock value \(A\) therefore gives

\[
\|(I-P_q)h\|_{L^2([0,A])}
\le \frac{V_h}{q}
 \left(\int_1^A\xi(A-\xi)\,d\xi\right)^{1/2}
\le\frac{V_h(A-1)}q\sqrt{\frac{1+a_0}{2}}.                       \tag{3}
\]

The norms here have the same aggregate sample/neuron normalization as the
paper. The last inequality follows from
\(\xi\le A\le1+a_0\) and
\(\int_1^A(A-\xi)d\xi=(A-1)^2/2\). At an arbitrary finite physical
horizon \(T\), (3) improves the paper's forward-tail coefficient
\(F_h=V_ha_0\sqrt{(1+a_0)/2}\) to

\[
F_h(T)=F_h\frac{A(T)-1}{a_0}\le F_h\min\{T,1\}.                \tag{4}
\]

Nothing in the backward-tail proof needs changing. In particular its
freezing time is truncated at the current horizon if necessary, and all its
coefficients are upper bounds independent of that horizon. Write \(D(T)\)
for the supremum up to \(T\) of the sum of mobility-coordinate block errors.
Write \(\mathcal D_T\) for the integrated hidden vector-field defect and
\(\mathcal A_n\) for the existing signed comparison coefficient. Its two
inequalities, now using (3), are

\[
\begin{aligned}
D(T)&\le\mathcal A_n\mathcal D_T,\\
\mathcal D_T&\le 2(L-1)F_h(T)
 \left\{\frac{b_0+b_1\sqrt{\log q}}{q^2}
       +\frac{B_d\sqrt{a_0}}qD(T)\right\}.                     \tag{5}
\end{aligned}
\]

For clarity, the second inequality follows by Cauchy--Schwarz in the sample
index and in \(dA=\widehat\rho\,dt\), followed by the projection-growth
identity. The integrated squared endpoint projection errors are bounded by
the terminal history-tail squares; the artificial initial projection errors
are zero. Thus the terminal forward-tail improvement (3) applies to the
entire integrated defect, not merely to its endpoint.

The original admissibility condition
\(q\ge4(L-1)F_hB_d\sqrt{a_0}\mathcal A_n\) absorbs the last term
in (5) with coefficient at most one half, since \(F_h(T)\le F_h\).
The same whole-sphere output subtraction with coefficient \(C_f\) yields

\[
\sup_{t\le T}E_n(t)
\le\frac{4(L-1)C_f\mathcal A_nF_h}{q^2}
       (b_0+b_1\sqrt{\log q})\min\{T,1\}.                    \tag{6}
\]

Apply the original coefficient ledger and original prescribed \(q\).
The coefficient without the last factor is at most
\(CY/(\sqrt n[\log(en)]^3)\). Taking \(T=t\) proves the first
line of (1) at every finite time. Existing parameter convergence extends it
to the fitted limit. Neither the clock nor the optimizer has been changed.

## 2. Selected methods: retain the zero initial readout

The auxiliary notation below is local to this proof. Put
\(\lambda=\gamma/m\), \(z=Y/\lambda\), \(X=\beta^L\), and
\(u=\sqrt{\log(en)}\). The finite comparison horizon is
\(T=32\log(en)/\lambda\ge1\). All selected norms use the fixed metrics
of the paper; dense vector norms use neuron RMS.

We first retain the elapsed time in two source-only errors. Let \(w_R\)
and \(h_R\) be restrictions of the actual dense readout and features.
The feature norm bound is \(\|h_R\|\le H_r\), where
\(H_r=\beta^{3L}+3\). If \(\eta\le1\) is the coordinate source
tolerance, the paper's pair-defect identity, applied to features at any two
times in \([0,T]\), gives error at most \(P_h\eta\), where
\(P_h=6\beta^{3L}+9\). Since \(w_R(0)=0\), its exact integrated
equation and Cauchy--Schwarz in samples imply

\[
\|w_R(t)\|\le2H_rYt,\qquad
|\langle w_R(t),h_R(t,x)\rangle-f_n(t,x)|
\le2P_h\eta Yt.                                                \tag{7}
\]

Indeed insert
\(w_R(t)=(2/m)\sum_a\int_0^t c_{n,a}(s)h_{R,a}(s)ds\),
where \(c_{n,a}=y_a-f_n(x_a)\), and use
\(m^{-1}\sum_a|c_{n,a}|\le\rho_n\le Y\).
Equation (7) also bounds by \(2P_h\eta Yt\) the Euclidean norm of
the training observation-defect vector, divided by \(\sqrt m\).
This uses source values only, not derivatives of an approximation error.

Recall the paper's comparison variables: \(a_h\) is the hidden-parameter
error; \(e=(c_C-c_n)/\sqrt m\);
\(V_C,V_R\) have top-feature columns divided by \(\sqrt m\);
\(T_C=V_C(V_C^*V_C)^{-1}\), \(P_C=T_CV_C^*\);
\(p=T_Ce\), \(\zeta=w_C-w_R+p\), and
\(b_e=\|p\|+\|\zeta\|\). Put \(E=a_h+b_e\).
These errors vanish at zero. The selected fitting and forward-error estimates
are

\[
\|T_C\|\le2/\sqrt\lambda,\quad
\|h_C\|\le H_C,\quad
\|h_C-h_R\|,\ \|V_C-V_R\|\le F(a_h+\eta).                    \tag{8}
\]

The exact readout-deficit identity is

\[
\widehat w_C-w_R
=(I-P_C)\zeta-p-T_C(V_C-V_R)^*w_R-T_Cd_R,                       \tag{9}
\]

where \(d_R=V_R^*w_R-(y-c_n)/\sqrt m\). Substituting (7)--(8)
into (9), then subtracting the query output, proves

\[
\begin{aligned}
E_n(t)\le{}&H_C b_e
 +(4H_CH_rFYt/\sqrt\lambda+2H_rFYt)(a_h+\eta)\\
 &+(4H_CP_hYt/\sqrt\lambda+2P_hYt)\eta.                       \tag{10}
\end{aligned}
\]

Unlike the global version, every source-only term in (10) vanishes linearly
at time zero.

The paper's cancelled-energy argument gives the scalar integral inequality

\[
E(t)\le\int_0^t g(s)\{E(s)+\eta(1+\lambda^{-1/2})\}\,ds,
\quad
g=200zF_c\rho_C+K_1M\rho_n+20F\nu/\sqrt\lambda,               \tag{11}
\]

where \(M=1+32zK_{\rm src}u\) and
\(\nu=\|V_Rc_n/\sqrt m\|\). Its established integral estimate is
\(\int_0^T g\le1+u\). Pointwise, \(\rho_C,\rho_n\le Y\)
and \(\nu\le H_rY\). The coefficient ledger gives

\[
H_r\le2X^3,\quad H_C\le2X^3,\quad P_h\le X^4,\quad
F\le X^6,\quad F_c\le X^{15},\quad K_1\le X^{18},\quad
K_{\rm src}\le X^{21}.
\]

For an explicit permissible constant set
\(A_X=200X^{15}+X^{18}+32X^{39}+40X^9\). Then

\[
g(t)\le YA_X(1+\lambda^{-1/2})(1+u).
\]

The integral comparison in (11) and \(e^v-1\le ve^v\) imply

\[
\begin{aligned}
E(t)&\le\eta(1+\lambda^{-1/2})
       e^{1+u}\int_0^t g(s)ds\\
&\le4eA_Xz\eta(1+u)e^u t.                                  \tag{12}
\end{aligned}
\]

Here \(Y(1+\lambda^{-1/2})^2\le4Y/\lambda=4z\) because
\(\lambda\le1\). For \(t\le1\), (10) now gives the desired output
bound with coefficients depending only on \(X\). Explicitly, let

\[
C_0=2X^3+16X^{12}+4X^9,\qquad
C_1=16X^{12}+4X^9+8X^7+2X^4.
\]

The coefficient of \(E\) in (10) is at most \(C_0\), using
\(Y/\sqrt\lambda\le z\le1\), and the source-only coefficient is at
most \(C_1z\eta t\). Thus, for \(0\le t\le1\),

\[
E_n(t)\le(4eA_XC_0+C_1)z\eta(1+u)e^u t.                     \tag{13}
\]

The paper chooses

\[
\eta=\min\left\{1,Y,16Y/\lambda,
\frac{\lambda}{2C n(1+\lambda^{-1/2})(1+u)e^u}\right\}.
\]

Insert this choice into (13), enlarging only the activation/depth constant
\(C\) if needed. This gives \(E_n(t)\le CYt/n\) on \([0,1]\).
For \(t\ge1\), use the already proved complete-trajectory estimate
\(E_n(t)\le Y/n\), including its tail and fitted-limit extension.
Together these prove the second line of (1). Changing the constant in
\(\eta\) only adds an activation/depth constant to logarithmic approximation
orders; it preserves all displayed powers in the retained-state bounds.

## What this establishes, and what it does not

Both comparison mechanisms have the correct initial-time zero at their
existing approximation orders. A sufficient missing dense statement would be
a simultaneous lower bound proportional to
\(\min\{t,1\}/\sqrt n\) on the same query domain, at fixed confidence.
Such a lower bound is not proved here, and it is impossible on the fitted
training-only panels described in `UNIFORM_TIME_SCOPE.md`.

An early positive-time witness for a trajectory supremum is not such a
simultaneous bound. An endpoint lower bound alone is not such a bound either.
