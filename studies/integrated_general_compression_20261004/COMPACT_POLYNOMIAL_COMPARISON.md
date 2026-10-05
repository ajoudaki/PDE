# Polynomial compact-to-dense comparison on the simple label cap

This is the complete deterministic comparison for the existing corrected-readout
compact model under the displayed label cap. It is conditional on the source,
selection, and independent fitting event specified below. The mathematical checks
and their provenance are recorded in [COMPACT_POLYNOMIAL_CHECK.md](COMPACT_POLYNOMIAL_CHECK.md).
No optimizer, source tolerance, horizon, selected dimension, retained coordinate,
or construction gate is changed.

Write
\(\lambda=\gamma/m\), without capping it, and \(\ell_n=\log(en)\).
On the existing event and with its existing width qualifications, the same
compressed predictor satisfies
\[
\sup_{t\in[0,\infty],\ \|v\|=1}|f_C(t,v)-f_n(t,v)|
\le 10\beta^{40L}\frac{Y}{\lambda}
       (1+\lambda^{-1/2})\frac{e^{2\sqrt{\ell_n}}}{n}.
\tag{1}
\]
In particular, an entirely polynomial strict-root consequence is
\[
\sup_{t\in[0,\infty],\ \|v\|=1}|f_C-f_n|
\le 250\beta^{40L}Y(1+m/\gamma)^2 n^{-1/2}.
\tag{2}
\]
The constants 10 and 250 are numerical; none depends on depth, dimension,
sample count, gap, labels, confidence, selected masses, or width. The powers
are deliberately conservative. No comparison exponential is transferred
into a width threshold.

## 1. Contract, inputs, and the exact optimizer

Fix \(L\ge2\), \(d,m\ge1\), unit training inputs \(v_a=x_a/\sqrt d\),
and arbitrary fixed real labels. The dense initialization, block mobilities,
physical clock, and network are those of the current integrated compact
theorem: independent Gaussian first weights of variance one, hidden weights
of variance \(1/n\), zero readout, and mean-square loss with mobilities
\((n,1,\ldots,1,n)\). Define
\[
Q^{(0)}_{ab}=v_a^{\mathsf T}v_b,\qquad
Q^{(j)}_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)],
\quad Z\sim N(0,Q^{(j-1)}),
\]
\[
\gamma=\lambda_{\min}(Q^{(L)})>0,\quad
\lambda=\gamma/m,\quad Y=\|y\|_2/\sqrt m.
\]
Each activation is real on the real axis and holomorphic on
\(|\operatorname{Im}w|<a\), with bounded first derivative on that strip.
Use the existing envelope
\[
\beta=\max\{10,1+\max_j|\phi_j(0)|,16/a,
 \max_{1\le j\le L,\ k\in\{1,2\}}\sup_{|\operatorname{Im}w|\le a/2}
                         |\phi_j^{(k)}(w)|\}.
\]
Assume precisely the common label cap
\[
0<Y\le\lambda\beta^{-30L}.
\tag{3}
\]
The case \(Y=0\) gives the exact zero predictor and is separate.

The source preprocessing and selection are unchanged. Write \(M_j\) for
the fixed selected-neuron metric, and \(\mathsf D_j\) for its positive
diagonal comparison metric. They satisfy
\(\mathsf D_j/4\preceq M_j\preceq\mathsf D_j\),
\(\|1\|_{M_j}=1\), and \(\|1\|_{\mathsf D_j}\le2\).
Every selected source subspace is exactly isometric to its full-width
counterpart. Coordinate source error is
\(\epsilon=n^{-1}\), through the unchanged horizon
\[
T=32\lambda^{-1}\ell_n.
\tag{4}
\]
Keep all inherited source/construction gates, including the comparison's
admissibility \(\epsilon\le\min(1,Y,S)\), where \(S=16Y/\lambda\).
No gate is added by the present comparison. The existence of the source
event at each sufficiently large width and fixed confidence is inherited;
its entire width threshold is not claimed polynomial.

The compressed forward pass is \(h_C^1(v)=\phi_1(Av)\) and
\(h_C^j(v)=\phi_j(B^jh_C^{j-1}(v))\). Let \(V_C\) have columns
\(h_C^L(v_a)/\sqrt m\), mapping Euclidean sample space into the top
selected Hilbert space, and let a star denote the appropriate Hilbert
adjoint. Set \(Q_C=V_C^*V_C\); the symbol \(q\) remains reserved for
the compact neuron budget. Its corrected readout is exactly
\[
\widehat w_C=w_C+V_CQ_C^{-1}
 \big[(y-c_C)/\sqrt m-V_C^*w_C\big],\qquad
f_C(v)=\langle\widehat w_C,h_C^L(v)\rangle_{M_L}.
\tag{5}
\]
Thus \(c_{C,a}=y_a-f_C(v_a)\). The specified backward signals are
\(k_{C,a}^L=\widehat w_C\),
\(\delta_{C,a}^j=\phi_j'(z_{C,a}^j)\odot k_{C,a}^j\), and
\(k_{C,a}^j=(B^{j+1})^*\delta_{C,a}^{j+1}\).

Define \(\mathcal J_C\) by its sample columns, each divided by
\(\sqrt m\), in the hidden-parameter Hilbert space:
\[
\big(\delta_{C,a}^1v_a^{\mathsf T},
 (\delta_{C,a}^j(h_{C,a}^{j-1})^{\mathsf T}M_{j-1})_{j=2}^L\big).
\tag{6}
\]
The first block has its metric Frobenius norm and each matrix block its
metric Hilbert--Schmidt norm. Consequently the runtime is exactly
\[
\dot\theta_{h,C}=2\mathcal J_C(c_C/\sqrt m),\quad
\dot w_C=2V_C(c_C/\sqrt m),\quad
\dot c_C=-2(V_C^*V_C+\mathcal J_C^*\mathcal J_C)c_C.
\tag{7}
\]
The last equation uses the normalized Gram; equivalently the unnormalized
runtime equation is \(\dot c_C=-2K_Cc_C/m\).
These are specified update directions; no gate is assumed self-adjoint
under a nondiagonal selected metric.

The proof-only reference arrays are the selected true first weights and
readout, and initialized selected mixers plus the rank-one integrals of
selected true features and responses driven by \(c_n=y-f_n\).
Write them as \(\theta_{h,R},w_R\). Define \(V_R,\mathcal J_R\) using
the actual selected dense features and responses in (6), not a forward
pass through those reference mixers. Then, exactly,
\[
\dot\theta_{h,R}=2\mathcal J_R(c_n/\sqrt m),\qquad
\dot w_R=2V_R(c_n/\sqrt m).
\tag{8}
\]
The reference arrays never enter the retained runtime.

The deterministic inputs are [GENERAL_EXPLICIT_FITTING.md](GENERAL_EXPLICIT_FITTING.md),
[EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md](EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md),
the source and action interfaces in [UNBOUNDED_COMPRESSOR_BRIDGE.md](UNBOUNDED_COMPRESSOR_BRIDGE.md),
and the recurrence envelopes in [SIMPLE_CONSTANTS_SOURCE_CHECK.md](SIMPLE_CONSTANTS_SOURCE_CHECK.md).
[COMPACT_SOURCE_ENERGY.md](COMPACT_SOURCE_ENERGY.md) records the selected-source
energy, pairing, velocity, and metric bounds. Source insertion, selection, and
probability are inherited interfaces; this theorem does not re-prove them.

## 2. Energy transfer and an explicit power ledger

For this proof only, set
\[
X=\beta^L\ge100,\qquad z=Y/\lambda\le X^{-30},\qquad
\alpha=Y/\sqrt\lambda=z\sqrt\lambda.
\tag{9}
\]
The checked current envelopes give
\[
\lambda\le X^4,\quad \alpha\le X^{-28},\quad
H_{\max},H_c,\max_jd_j^c\le X^3,\quad F_c\le X^{15},
\]
\[
P_h\le X^4,\quad P_\delta\le X^5,\quad
\tau\le X^4,\quad A_f,A_b\le X,\quad
F,\max_jF_j^z\le X^9,\quad K_{\rm src}\le X^{21}.
\tag{10}
\]
Here \(H_{\max},\tau,A_f,A_b,P_h,P_\delta,F,F_j^z\) are respectively
the source RMS, response, action, pairing, and forward subtraction
coefficients in the integrated bridge; \(H_c,d_j^c,F_c\) are the
compressed fitting coefficients. Their explicit recurrence audit is
the current `SIMPLE_CONSTANTS_SOURCE_CHECK.md`, especially (17)--(22).
In particular both selected true and compressed feature norms are at
most \(2X^3\). The independent fitting bounds give
\[
Q_C\succeq\lambda I/4,\quad
\|w_C\|\le2\alpha,\quad \|\widehat w_C\|\le5\alpha,\quad
\int_0^\infty\rho_C\le2z,\quad
\int_0^\infty\rho_n\le4z,
\tag{11}
\]
where \(\rho_C=\|c_C\|_2/\sqrt m\),
\(\rho_n=\|c_n\|_2/\sqrt m\). The last bound is deliberately
weaker than the available dense bound \(2z\).

The dense energy identity and Gram margin imply
\(\int_0^\infty\|\dot\theta_n\|_{\rm par}\le2\alpha\).
For completeness, their ingredients are
\(-d\rho_n^2/dt=\|\dot\theta_n\|_{\rm par}^2\) and
\(-\dot\rho_n\ge\lambda\rho_n/2\); hence the speed is at most
\(2(-\dot\rho_n)/\sqrt\lambda\). Integration gives the claim.

If \(V_n\) contains the full dense features divided by \(\sqrt m\),
exact isometry of the source approximants and the normalized column-error
Hilbert--Schmidt bound give, for every sample vector \(b\),
\[
\|V_Rb\|\le\|V_nb\|+3\epsilon\|b\|.
\tag{12}
\]
The full-width column errors have operator norm at most \(\epsilon\);
the selected errors have operator norm at most \(2\epsilon\). This
proves (12) without a sample-count factor.

Integrating source feature approximants against the actual residual gives
a source-space approximation to \(w_n\) with coordinate error at most
\(8z\epsilon\). One can take finite Riemann sums first and use
closedness of the finite-dimensional source space. Applying exact isometry
and the two coordinate-error bounds yields
\[
\|w_R\|\le2\alpha+24z\epsilon\le4\alpha.
\tag{13}
\]
The final inequality follows from
\(\epsilon/\sqrt\lambda\le Y/\sqrt\lambda=\alpha\le X^{-28}\).
The actual reference readout velocity has the more useful integral
\[
\nu(t)=\|V_R(t)c_n(t)/\sqrt m\|,\qquad
\int_0^T\nu\le\alpha+12z\epsilon\le2\alpha.
\tag{14}
\]
Here (12) was applied to \(c_n/\sqrt m\), and
\(2V_nc_n/\sqrt m=\dot w_n\). A generic bound by residual activity
would lose this energy scale.

Dense real backward propagation gives
\(\|\delta_{n,a}^j\|_n\le2X^2\alpha\): its coefficient is
\(s_1(9s_1)^{L-j}\le X^2\), where
\(s_1=\max(1,\sup|\phi_j'|)\le\beta\).
Selected source isometry adds at most \(3\epsilon\).
Since \(\epsilon\le Y\) and \(\sqrt\lambda\le X^2\),
\[
\|\delta_{R,a}^j\|\le6X^2\alpha\le X^3\alpha<1.
\tag{15}
\]
The compressed response bound is \(5X^3\alpha\).
Using \(L\le X\), the norm of a complete column direction in (6)
is at most its response norm times
\(\sqrt{1+(L-1)4X^6}\le3X^{7/2}\).
Normalized sample columns therefore give
\[
\|\mathcal J_C\|,\|\mathcal J_R\|\le X^8\alpha.
\tag{16}
\]
The operator bound follows from the Hilbert--Schmidt column bound, so
again no \(m\) appears. The actual differentiated compressed feature
recurrence gives
\[
\|\dot V_C\|\le2(5\alpha)F_c\rho_C
                         \le X^{16}\alpha\rho_C.
\tag{17}
\]
All these bounds hold without a bounded activation-value hypothesis.
Feature control is RMS control obtained from linear growth and bounded
operators. The inequalities explicitly use \(\lambda\le X^4\),
so they include \(\lambda>1\) without changing its value.

## 3. Readout geometry and the hidden-direction subtraction

Define the hidden error \(E_h=\|\theta_{h,C}-\theta_{h,R}\|\), the
normalized residual error \(e=(c_C-c_n)/\sqrt m\), and the raw readout
error \(w_C-w_R\). Define the right inverse and projector
\[
T_C=V_CQ_C^{-1},\qquad P_C=T_CV_C^*,\qquad
p=T_Ce,\qquad \zeta=w_C-w_R+p,
\]
\[
E_r=\|p\|+\|\zeta\|,\qquad E=E_h+E_r,\qquad u=\|e\|.
\tag{18}
\]
All errors start at zero. The fitting gap implies
\(\|T_C\|\le2/\sqrt\lambda\),
\(V_C^*p=e\), and \(\|p\|\le2u/\sqrt\lambda\).
The projector is orthogonal in the selected top metric.

The original forward subtraction recurrences apply with \(E_h\):
each hidden block discrepancy is bounded by \(E_h\), and the raw
readout does not enter a forward feature. Thus
\[
\|V_C-V_R\|\le X^9(E_h+\epsilon),\qquad
\sup_{j,v}\|h_C^j(v)-h_{n,I_j}^j(v)\|
                         \le X^9(E_h+\epsilon).
\tag{19}
\]
The same bound with \(F_j^z\) holds for preactivations. Write
\(\Delta V=V_C-V_R\). The selected readout pairing defect
\(d_R=V_R^*w_R-(y-c_n)/\sqrt m\) obeys
\(\|d_R\|\le16zP_h\epsilon\), including sphere queries.
Substitution in (5) gives exactly
\[
\eta:=\widehat w_C-w_R
=(I-P_C)(w_C-w_R)-p-T_C\Delta V^*w_R-T_Cd_R.
\tag{20}
\]
Since \((I-P_C)p=0\), (13), (19), and (20) imply
\[
\|\eta\|\le E_r+X^{10}z(E_h+\epsilon)
                         +X^5z\epsilon/\sqrt\lambda.
\tag{21}
\]
For example the two last coefficients before rounding are
\(8X^9z\) and \(32X^4z\), each bounded by the displayed power.

Let \(M\ge1\) bound all actual dense training carrier coordinates
through \(T\). The source event permits
\[
M=1+16X^{21}z\sqrt{\ell_n}.
\tag{22}
\]
No selected-compressed carrier maximum is required. In backward
subtraction, a changed gate acts on the true selected reference carrier.
Diagonal domination bounds its contribution by
\(2s_2M\|z_C^j-z_R^j\|\), where \(s_2\le\beta\) bounds
\(|\phi_j''|\). The remaining terms propagate with \(18s_1\),
and cost \(2s_1\) times a mixer error multiplying a response of norm
at most one, plus the reverse action defect \(A_b\epsilon\).
Consequently the maximum response difference is at most
\[
X^4\|\eta\|+X^{14}M(E_h+\epsilon).
\tag{23}
\]
To check the powers: \(18s_1\le\beta^3\), its finite propagation
sum is at most \(2X^3\), and the additive forcing is at most
\(4\beta X^9M(E_h+\epsilon)\). Their product is at most
\(8X^{25/2}M(E_h+\epsilon)\le X^{14}M(E_h+\epsilon)\).
The propagated terminal readout factor is at most \(X^4\).

Subtracting the rank-one directions gives
\[
\|\mathcal J_C-\mathcal J_R\|
\le \sqrt L\big[(1+2X^3)\max_j\|\delta_C^j-\delta_R^j\|
                              +X^9(E_h+\epsilon)\big].
\]
Using (23), this is at most
\(X^9\|\eta\|+X^{19}M(E_h+\epsilon)\).
Inserting (21) gives the useful separated bound
\[
\|\Delta\mathcal J\|
\le X^{10}E_r+X^{20}M(E_h+\epsilon)
                              +X^{15}z\epsilon/\sqrt\lambda.
\tag{24}
\]
The geometric argument only requires training backward differences;
whole-sphere output comparison uses (19) and (21).

## 4. Gram forcing with its two-factor structure retained

Let \(\mathcal K_n=K_n/m\) be the actual dense tangent Gram and set
\[
D=V_R^*V_R+\mathcal J_R^*\mathcal J_R-\mathcal K_n.
\]
The supplied coordinate-pairing estimate gives
\[
\|D\|\le X^5\epsilon.
\tag{25}
\]
Here is a termwise bound. Feature pairing defects are at most
\(P_h\epsilon\). Response pairing defects are at most
\(SP_\delta\epsilon\). The products in the hidden Gram therefore
give the total coefficient
\[
P_h+SP_\delta[1+(L-1)H_r^2]+(L-1)S^2\tau^2P_h
\le X^4+80zX^{12}+256z^2X^{13}\le X^5.
\]
The normalized sample operator norm is bounded by the largest unnormalized
entry defect, so no sample factor is lost. This also shows exactly where
the unchanged condition \(\epsilon\le S\) is used in the inherited
response-pairing estimate.

For \(\Delta\mathcal K=V_C^*V_C+\mathcal J_C^*\mathcal J_C-
\mathcal K_n\), the exact factorization is
\[
\Delta\mathcal K=V_C^*\Delta V+\Delta V^*V_R
 +\mathcal J_C^*\Delta\mathcal J
 +\Delta\mathcal J^*\mathcal J_R+D.
\tag{26}
\]
Put \(\mathcal F(t)=2\|T_C\Delta\mathcal K(c_n/\sqrt m)\|\).
Since \(T_CV_C^*=P_C\), (14), (16), (19), and (25) give
\[
\mathcal F\le
 2X^9\rho_n(E_h+\epsilon)
 +4X^9\frac\nu{\sqrt\lambda}(E_h+\epsilon)
 +8X^8z\rho_n\|\Delta\mathcal J\|
 +4X^5\epsilon\rho_n/\sqrt\lambda.
\tag{27}
\]
The second term contains the actual reference velocity \(\nu\), whose
integral has the improved scale (14). Insert (24) and use
\(8X^{28}z\le1\), \(8X^{23}z^2\le1\). This gives
\[
\mathcal F\le
X^{10}(M\rho_n+\nu/\sqrt\lambda)(E_h+\epsilon)
 +X^{19}z\rho_nE_r+X^6\epsilon\rho_n/\sqrt\lambda.
\tag{28}
\]
Every power used in these absorptions is strictly below the available
30 for one label factor or 60 for two label factors.

## 5. Cancellation and scalar closure

The exact residual and readout error equations are
\[
\dot e=-2(Q_C+\mathcal J_C^*\mathcal J_C)e
                      -2\Delta\mathcal K(c_n/\sqrt m),
\qquad
\frac d{dt}(w_C-w_R)=2V_Ce+2\Delta V(c_n/\sqrt m).
\tag{29}
\]
Differentiate the right inverse to obtain
\[
\dot T_C=(I-P_C)\dot V_CQ_C^{-1}-T_C\dot V_C^*T_C.
\tag{30}
\]
Because \(Q_C^{-1}e=T_C^*p\), (17) gives
\[
\|\dot T_Ce\|\le4\|\dot V_C\|\|p\|/\sqrt\lambda
                         \le X^{17}z\rho_C\|p\|.
\tag{31}
\]
Pairing the equation for \(p=T_Ce\) with \(p\) retains the negative
term \(-2\langle p,V_Ce\rangle=-2u^2\).
The hidden-Gram term need not have a sign in this metric, but its absolute
contribution is at most
\[
2\|p\|\|T_C\|\|\mathcal J_C\|^2u
                        \le8X^{16}z^2u^2\le u^2.
\]
Define
\[
I(t)=\int_0^t[X^{17}z\rho_C E_r+\mathcal F]\,dr.
\]
It follows that
\[
\|p(t)\|+\int_0^t\frac{u^2}{\|p\|}\,dr\le I(t),
\qquad
\int_0^tu\,dr\le\frac2{\sqrt\lambda}I(t).
\tag{32}
\]
At zero norm, regularize by \((\|p\|^2+\delta^2)^{1/2}\), integrate,
and let \(\delta\downarrow0\). The nonnegative damping integrands
increase to the displayed quotient; it is defined as zero where \(p=0\),
since then \(e=V_C^*p=0\). The second inequality uses
\(u\ge\sqrt\lambda\|p\|/2\).

In the equation for \(\zeta=w_C-w_R+p\), the terms \(2V_Ce\) and
\(-2T_CQ_Ce=-2V_Ce\) cancel exactly:
\[
\dot\zeta=2\Delta V(c_n/\sqrt m)+\dot T_Ce
 -2T_C\mathcal J_C^*\mathcal J_Ce
 -2T_C\Delta\mathcal K(c_n/\sqrt m).
\tag{33}
\]
The integrated hidden-Gram term is bounded by
\(8X^{16}z^2 I(t)\le I(t)\), by (32). Hence
\[
E_r(t)\le3I(t)+2X^9\int_0^t\rho_n(E_h+\epsilon)\,dr.
\tag{34}
\]
Subtracting the hidden velocities (7)--(8) and using (32) gives
\[
E_h(t)\le4X^8zI(t)+2\int_0^t\rho_n\|\Delta\mathcal J\|\,dr
          \le I(t)+2\int_0^t\rho_n\|\Delta\mathcal J\|\,dr.
\tag{35}
\]
The last step uses \(4X^8z\le1\).

Set \(G_\lambda=1+\lambda^{-1/2}\). Combining (24), (28),
(34), and (35), with \(4X^{17}z\le1\) and
\(4X^{19}z\le1\), yields
\[
E(t)\le X^{22}\int_0^t
 [M\rho_n+\rho_C+\nu/\sqrt\lambda]
                         [E+\epsilon G_\lambda]\,dr.
\tag{36}
\]
For an explicit last coefficient check, the coefficient on
\(M\rho_n(E_h+\epsilon)\) before rounding is
\(4X^{10}+2X^9+2X^{20}\le X^{21}\);
the \(\nu/\sqrt\lambda\) coefficient is \(4X^{10}\le X^{21}\).
The remaining \(E_r\) coefficients are at most one on \(\rho_C\)
and \(3X^{10}\) on \(\rho_n\); the direct
\(\epsilon/\sqrt\lambda\) coefficient is at most \(X^7\).
All are covered by (36). The factor \(G_\lambda\), instead of merely
\(\lambda^{-1/2}\), makes the forcing valid also when \(\lambda>1\).

Let \(B(t)\) be \(X^{22}\) times the integral of the first bracket
in (36). Equations (11) and (14) give
\[
B(t)\le4X^{22}z(M+1)\le X^{23}z(M+1)
       \le2X^{23}z+16X^{44}z^2\sqrt{\ell_n}.
\tag{37}
\]
Thus
\[
B(t)\le1+\sqrt{\ell_n},\qquad
B(t)\le X^{24}z(1+\sqrt{\ell_n}).
\tag{38}
\]
Both inequalities follow directly from \(z\le X^{-30}\): the two
coefficients in the first are at most \(2X^{-7}\) and \(16X^{-16}\);
for the second use \(X^{21}z\le1\).
Integral Gronwall with the zero initial error gives
\[
E(t)\le\epsilon G_\lambda(e^{B(t)}-1)
\le\epsilon G_\lambda X^{24}z(1+\sqrt{\ell_n})
                                   e^{1+\sqrt{\ell_n}}.
\tag{39}
\]
This is the point at which every depth and conditioning multiplier has
left the exponential. The label cap absorbs the depth powers explicitly;
the gap does not occur in (37) except through the allowed ratio \(z\).

## 6. Whole-sphere output, tail, and retained size

For every query, add and subtract the selected true pairing. Equations
(13), (19), (21), and the source observation defect give
\[
|f_C-f_n|\le H_C\|\eta\|+4\alpha X^9(E_h+\epsilon)
                                       +16zP_h\epsilon
              \le X^{15}(E+z\epsilon G_\lambda).
\tag{40}
\]
The displayed envelope uses only \(H_C\le X^4\),
\(\sqrt\lambda\le X^2\), and (3); in particular the coefficient
on \(E\) can already be bounded by \(X^5\).
Substitute (39), use \(1+r\le2e^r\) for \(r\ge0\), and absorb
the smaller additive term. This gives
\[
\sup_{t\le T,v}|f_C-f_n|
\le6X^{40}zG_\lambda\epsilon e^{2\sqrt{\ell_n}}.
\tag{41}
\]
No source-defect derivative has been taken.

For times beyond \(T\), use the already proved independent fitting
tails, including uniform convergence on the sphere. The current explicit
ledger gives \(\mathcal K\le X^7\) for the dense source Gram coefficient
and \(B_f\le X^{12}\sqrt{1+\lambda^{-1}}\) for the compact endpoint
coefficient. The same-time triangle comparison at \(T\) adds at most
\[
z(16\mathcal K+4B_f)e^{-8\ell_n}
 \le X^{13}z\sqrt{1+\lambda^{-1}}e^{-8\ell_n}
 \le X^{13}zG_\lambda e^{-8\ell_n}.
\tag{42}
\]
This bounds every later physical time and the endpoint, because each
trajectory's motion from its value at \(T\) is bounded by its integrated
speed tail. The runtime continues autonomously. Since
\(e^{-8\ell_n}\le n^{-1}\), (41)--(42) imply (1).

The strict-root conversion needs no width restriction: for
\(r=\sqrt{\ell_n}\), \(2r\le r^2/2+2\), and therefore
\[
n^{-1}e^{2\sqrt{\ell_n}}\le e^{5/2}n^{-1/2}.
\]
Also \(\lambda^{-1}(1+\lambda^{-1/2})\le
2(1+\lambda^{-1})^2\), and \(20e^{5/2}<250\). This proves (2)
with a universal numerical constant, not a parameter-dependent absorption.

The same source tolerance, source families, degree choices, horizon, exact
initialization additions, and selected dimensions are used. In particular
the all-retained count remains exactly the current envelope
\[
\operatorname{size}(C)\le
\beta^{(64+6d)L}\frac{(d+3)^d}{(d!)^2}
(Ym/\gamma)^4\ell_n^{3d+2}
+2040(L+1)(2m+d+1)^2+10m(d+1).
\tag{43}
\]
All new vectors and operators used for comparison are proof objects, not
stored state. The per-layer schedule is unchanged, as is the initialization-
only preprocessing and its exact-real computation/precision qualification.

## 7. Larger recurrence allowance and claim boundary

The current compact construction and fitting theorem also allow the larger
recurrence intersection
\[
Y/\lambda\le\min\{(8H_d\sqrt{F_d})^{-1},
 (16H_c\sqrt{F_c})^{-1},S_*^{\rm src}/16\}.
\tag{44}
\]
The dense and compact fitting recurrences define \(H_d,F_d,H_c,F_c\),
and the source bridge defines \(S_*^{\rm src}\). This allowance is not
replaced by (3) in the underlying construction. The present numerical
polynomial theorem is established on its displayed common subrange (3).
The larger range (44) is treated in
[COMPACT_FULL_LABEL_RANGE.md](COMPACT_FULL_LABEL_RANGE.md), with its own
universal numerical constants and exact source-storage coefficients.
The constants 10 and 250 and the simplified storage envelope (43) belong
to (3); estimate (38) is not asserted on the additional range. Actual
label factors in storage are retained.

The strongest surviving dependency is the inherited unbounded analytic
source event and its selection interface. This note proves only the new
deterministic transfer, relative to those inputs. It does not re-audit
their older unprovided insertion dependencies, make their construction
width polynomial, establish optimality, or justify promotion.

The required deterministic estimates are:
selected energy scales are (12)--(16); the noncommuting hidden Gram is
absorbed in (32), using the unchanged cap; fixed metrics require no
self-adjoint gates; source errors are never differentiated; \(\lambda>1\)
is handled by \(\lambda\le X^4\) and \(G_\lambda\); endpoint control is
(42); the remaining exponential has universal coefficients in (38).
The internal reconstructions in
[COMPACT_POLYNOMIAL_CHECK.md](COMPACT_POLYNOMIAL_CHECK.md) checked these
estimates and power roundings. This remains a conditional deterministic
theorem, not a promotion review of the inherited stochastic source chain.
