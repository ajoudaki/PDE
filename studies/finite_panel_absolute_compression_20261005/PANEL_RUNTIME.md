# Finite-panel corrected runtime and conditional all-time comparison

2026-10-05. Independent scoped runtime route, frozen before reading any
other route in this study. This is a deterministic reduction conditional
on the finite-panel source and selection event specified below. It does
not independently establish that stochastic event or its success width.

The corrected autonomous optimizer transfers without changing its training
equations. Passive points need forward sources, but no labels, residual
coordinates, backward sources, or positive Gram gap. Conditional on a
common complex-time source radius proportional to
`log(en)^(-1/2)`, time approximation gives an absolute all-retained
storage exponent five. Section 9 records the subsequent verification that
the authorized finite-query localization supplies this regularity, relative
to its inherited insertion theorem. The improved comparison then remains
`n^(-1) exp(O(sqrt(log(en))))` through all physical time and the endpoint.

## 1. Model and exact passive-input identity

Fix a panel of unit vectors \(v_i=x_i/\sqrt d\), \(1\le i\le p\),
before initialization. The first \(m\) vectors are training inputs, span
\(\mathbb R^d\), and have labels \(y\in\mathbb R^m\). Thus \(p\ge m\ge d\).
Only these labels exist in the model. All hidden layers have width \(n\),
and \(L\ge2\). The dense network is
\[
z_n^{(1)}(v)=A_nv,\qquad
z_n^{(j)}(v)=W_n^{(j)}h_n^{(j-1)}(v),\qquad
h_n^{(j)}=\phi_j(z_n^{(j)}),\qquad
f_n(v)=w_n^Th_n^{(L)}(v)/n.
\]
The entries of \(A_n(0)\) are independent \(N(0,1)\), those of each
\(W_n^{(j)}(0)\) are independent \(N(0,1/n)\), the blocks are independent,
and \(w_n(0)=0\). The loss and mobilities are
\[
\mathcal L_n=m^{-1}\sum_{a=1}^m(f_n(v_a)-y_a)^2,
\qquad (n,1,\ldots,1,n).
\]
Set \(r_{n,a}=f_n(v_a)-y_a\) and \(c_{n,a}=-r_{n,a}\); the latter
is the auxiliary sign convention of the imported runtime. For training
indices define
\[
k_{n,a}^{(L)}=w_n,\quad
\delta_{n,a}^{(j)}=\phi'_j(z_{n,a}^{(j)})\odot k_{n,a}^{(j)},\quad
k_{n,a}^{(j)}=W_n^{(j+1)T}\delta_{n,a}^{(j+1)}.
\]
The exact dense flow is
\[
\dot A_n=\frac2m\sum_{a\le m}c_{n,a}\delta_{n,a}^{(1)}v_a^T,
\quad
\dot W_n^{(j)}=\frac2{mn}\sum_{a\le m}
 c_{n,a}\delta_{n,a}^{(j)}h_{n,a}^{(j-1)T},
\quad
\dot w_n=\frac2m\sum_{a\le m}c_{n,a}h_{n,a}^{(L)}.
\tag{1}
\]
A passive point \(i>m\) evolves by recomputing its forward pass through
these weights. More explicitly,
\[
\dot z_{n,i}^{(1)}=\dot A_nv_i,\quad
\dot z_{n,i}^{(j)}=\dot W_n^{(j)}h_{n,i}^{(j-1)}
 +W_n^{(j)}\dot h_{n,i}^{(j-1)},\quad
\dot h_{n,i}^{(j)}=\phi'_j(z_{n,i}^{(j)})\odot\dot z_{n,i}^{(j)}.
\tag{2}
\]
Thus passive features usually move, although no term with \(i>m\)
occurs in (1). Appending zero loss weights leaves the same vector field,
the denominator \(m\), and physical time unchanged. Dividing by \(p\)
instead would change the problem.

The activations are real on the real line, holomorphic on
\(|\operatorname{Im}z|<a_{\rm strip}\), and have bounded first derivative
there. Their values can be unbounded. Define
\[
\beta=\max\left\{10,1+\max_j|\phi_j(0)|,16/a_{\rm strip},
 \max_{j,k=1,2}\sup_{|\operatorname{Im}z|\le a_{\rm strip}/2}
 |\phi_j^{(k)}(z)|\right\}.
\]
The covariance recursion \(Q^{(0)}_{ab}=v_a^Tv_b\) and
\(Q^{(j)}_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)]\),
\(Z\sim N(0,Q^{(j-1)})\), uses training indices only. Put
\[
\gamma=\lambda_{\min}(Q^{(L)})>0,\quad
\lambda=\gamma/m,\quad Y=\|y\|_2/\sqrt m,\quad
\ell_n=\log(en),\quad T_n=32\lambda^{-1}\ell_n.
\]
No gap for the full \(p\)-point covariance is assumed. It may be
singular, including through duplicate panel points. The case \(Y=0\)
has the exact stationary zero predictor and is treated separately.

## 2. The unchanged finite autonomous optimizer

At layer \(j\), let the selected width be \(q_j\), with fixed positive
metric \(M_j\) and positive diagonal metric \(\mathsf D_j\) satisfying
\[
\mathsf D_j/4\preceq M_j\preceq\mathsf D_j,
\qquad \mathbf1^TM_j\mathbf1=1,
\qquad \mathbf1^T\mathsf D_j\mathbf1\le4.
\tag{3}
\]
Write \(\langle u,v\rangle_{M_j}=u^TM_jv\). The moving variables are
\[
A_C\in\mathbb R^{q_1\times d},\quad
B_C^{(j)}\in\mathbb R^{q_j\times q_{j-1}},\quad
w_C\in\mathbb R^{q_L},\quad c_C\in\mathbb R^m.
\]
They start at the selected initial weights, zero raw readout, and
\(c_C(0)=y\). For every declared input, compute
\[
z_C^{(1)}(v)=A_Cv,\quad z_C^{(j)}(v)=B_C^{(j)}h_C^{(j-1)}(v),
\quad h_C^{(j)}=\phi_j(z_C^{(j)}).
\]
Let \(V_C\) have columns \(h_C^{(L)}(v_a)/\sqrt m\), \(a\le m\),
and put \(Q_C=V_C^*V_C\). Stars mean the appropriate metric Hilbert
adjoints; sample space is Euclidean. The effective readout is
\[
\widehat w_C=w_C+V_CQ_C^{-1}
 [(y-c_C)/\sqrt m-V_C^*w_C],\qquad
f_C(v_i)=\langle\widehat w_C,h_C^{(L)}(v_i)\rangle_{M_L}.
\tag{4}
\]
Therefore \(c_{C,a}=y_a-f_C(v_a)\) exactly. The inverse in (4) is
\(m\)-by-\(m\); no passive point is inserted into it.

For \(a\le m\) define the specified responses
\[
k_{C,a}^{(L)}=\widehat w_C,\quad
\delta_{C,a}^{(j)}=\phi'_j(z_{C,a}^{(j)})\odot k_{C,a}^{(j)},\quad
k_{C,a}^{(j)}=(B_C^{(j+1)})^*\delta_{C,a}^{(j+1)},
\]
where \((B_C^{(j+1)})^*=M_j^{-1}B_C^{(j+1)T}M_{j+1}\).
Let \(\mathcal J_C\) have sample columns, divided by \(\sqrt m\),
\[
\left(\delta_{C,a}^{(1)}v_a^T,
 (\delta_{C,a}^{(j)}h_{C,a}^{(j-1)T}M_{j-1})_{j=2}^L\right).
\]
Its target is the direct sum of the first-weight and hidden-matrix
Hilbert spaces. A hidden block has squared norm
\(\|M_j^{1/2}BM_{j-1}^{-1/2}\|_F^2\). The autonomous equations are
\[
\dot\theta_{h,C}=2\mathcal J_Cc_C/\sqrt m,\qquad
\dot w_C=2V_Cc_C/\sqrt m,\qquad
\dot c_C=-2(Q_C+\mathcal J_C^*\mathcal J_C)c_C.
\tag{5}
\]
Every hidden block trains. The metric gates need not be self-adjoint,
so (5) is the imported specified optimizer, not an assertion of ordinary
gradient flow for (4). It is finite and restartable wherever \(Q_C\)
remains positive: the current state, retained data, metrics and fixed
activation evaluators determine all future derivatives and outputs.

## 3. Required finite-panel source interface

The deterministic comparison needs the following event. Its probability
and construction complexity are separate obligations.

For each layer there is a fixed source space \(E_j\subset\mathbb R^n\)
and coordinate restriction \(R_j\) such that
\[
u^Tv/n=(R_ju)^TM_j(R_jv)\qquad(u,v\in E_j).
\tag{6}
\]
On \([0,T_n]\), coordinate error is at most
\(\epsilon=n^{-1}\le\min(1,Y,16Y/\lambda)\) for these families:

- \(h_n^{(j)}(t,v_i)\), for every panel point \(i\le p\);
- \(W_n^{(j)}(0)h_n^{(j-1)}(t,v_i)\), for every panel point
  and each relevant hidden mixer;
- \(\delta_{n,a}^{(j)}(t)\), only for training indices \(a\le m\);
- \(W_n^{(j+1)}(0)^T\delta_{n,a}^{(j+1)}(t)\), only for
  training indices and each relevant reverse mixer.

The approximation coefficients for a vector and its initialized image
are paired exactly. Include the constant vector, first-weight columns,
initialized training features and their forward images exactly, with
the existing conservative rank allowance \(2m+d+1\). The selected
initialized operators have norm at most eight, and the selected initial
normalized training-feature Gram equals the dense one. The dense
initialization event has gap at least \(\lambda/2\), operator bounds
eight and the initial real feature bounds needed in the fitting theorem.

Finally, retain the inherited source carrier estimate on training
points only:
\[
\max_{t\le T_n,\,a\le m,\,j,\,i}|k_{n,a,i}^{(j)}(t)|
 \le16K_{\rm src}(Y/\lambda)\sqrt{\ell_n}.
\tag{7}
\]
The source coefficient recurrences and the source small-label allowance
are exactly those in the imported bridge. The finite-panel event must
supply their same RMS and paired-action envelopes. Merely approximating
the panel's final outputs does not supply (6), the paired action, or (7).

No passive reverse source is necessary. The learned forward-action defect
at a passive point pairs a training feature with that passive feature;
both belong to the forward source family. All reverse-action defects in
the optimizer comparison are evaluated at training points. Likewise,
the only changed gate multiplied by an actual carrier belongs to a
training response, so (7) has no passive index.

## 4. Fitting and source energy survive without panel factors

Use the existing dense and compact fitting allowances and source
allowance. In their original recurrence notation the full condition is
\[
Y/\lambda\le\min\{(8H_d\sqrt{F_d})^{-1},
 (16H_c\sqrt{F_c})^{-1},S_*^{\rm src}/16\}.
\tag{8}
\]
These coefficients are defined in the imported complete fitting and
full-range proofs listed below. In particular, no bound in (8) changes
when a passive panel point is appended. A convenient smaller sufficient
condition is \(0<Y\le\lambda\beta^{-30L}\).

For the compact fitting constants, set
\(s=\max(1,\max_j\|\phi'_j\|_\infty)\) and
\(b=\max_j|\phi_j(0)|\), and define
\[
H_1^c=\max(1,2b+16s),\quad
H_j^c=\max(1,2b+18sH_{j-1}^c),\quad H_c=H_L^c,
\]
\[
d_j^c=2s(18s)^{L-j},\qquad
F_c=(d_1^c)^2+4H_c^2\sum_{j=2}^L(d_j^c)^2.
\]
The dense fitting event can also be localized without any query net.
Define scalar moments \(q_0^{\rm mom}=1\),
\(q_j^{\rm mom}=\mathbb E\phi_j(\sqrt{q_{j-1}^{\rm mom}}Z)^2\),
\(Z\sim N(0,1)\), and
\(H_d=\max(1,\sqrt{q_1^{\rm mom}},\ldots,\sqrt{q_L^{\rm mom}})\).
Put \(s_2=\max_j\|\phi_j''\|_\infty\) and
\[
A_{\rm fit}=s^2+s_2(b+\sqrt2sH_d),\quad
T_{\rm fit}=\sum_{j=0}^{L-1}A_{\rm fit}^j,\quad
e_{\rm fit}=\min(1/4,\gamma/(2m)),\quad
M_{4,\rm fit}=8b^4+96s^4H_d^4.
\]
For failure probability \(\delta\), a sufficient width is
\[
N_{\rm fit}^{\rm panel}(\delta)=\left\lceil\max\left\{
1,\frac{\log(8L/\delta)}{8-2\log9},
\frac{d\log9+\log(8/\delta)}{8-\log9},
\frac{2L(m^2+p)M_{4,\rm fit}T_{\rm fit}^2}
 {\delta e_{\rm fit}^2}\right\}\right\rceil.
\tag{8a}
\]
Indeed the conditional covariance argument in the dense fitting proof
controls the \(m^2\) training Gram entries and the \(p\) individual
panel feature squared norms at every layer. The latter are at most
\(H_d^2+1/4\), so their RMS is below \(3H_d/2\).
No spatial interpolation is necessary. The same stopped subtraction
proof then gives panel-uniform features, fitting and output tails for
all time under the unchanged dense label cap. The Gaussian operator
bounds in (8a) concern the weight matrices, not a query representation.

The fitting proof gives, with \(\rho_C=\|c_C\|_2/\sqrt m\),
\[
Q_C\succeq\lambda I/4,\quad
\rho_C(t)\le Ye^{-\lambda t/2},\quad
\|w_C\|_{M_L}\le2Y/\sqrt\lambda,\quad
\|\widehat w_C\|_{M_L}\le5Y/\sqrt\lambda.
\tag{9}
\]
It uses the exact identity
\[
-\frac d{dt}\rho_C^2=\|\dot\theta_C\|_{\rm par}^2,
\qquad \int_0^\infty\|\dot\theta_C\|_{\rm par}
 \le2Y/\sqrt\lambda.
\]
The algebraic Gram in (5) proves this identity even though (5) is not
identified with the gradient of the corrected predictor. The raw
parameter norm excludes the independently stored residual.

For a dense vector \(u\) with coordinate-error \(e\) from \(E_j\),
(3) and (6) imply
\[
\|R_ju\|_{M_j}\le\|u\|_2/\sqrt n+3e.
\tag{10}
\]
Indeed the full-width approximation error has RMS at most \(e\), and
its restriction has \(M_j\)-norm at most \(2e\). Applying this column
by column to the training feature maps gives
\(\|V_R\xi\|\le\|V_n\xi\|+3\epsilon\|\xi\|_2\), where
\(V_R\) uses actual restricted dense features. The normalization of
each column by \(\sqrt m\) removes the sample factor.

Let \(w_R=R_Lw_n\), \(z=Y/\lambda\), and
\(\alpha=Y/\sqrt\lambda\). Integrating source approximants against
the actual training residual gives a source approximation to \(w_n\)
with coordinate error at most \(4z\epsilon\). Therefore
\[
\|w_R\|_{M_L}\le2\alpha+12z\epsilon\le3\alpha,
\qquad
\int_0^{T_n}\|V_Rc_n/\sqrt m\|_{M_L}\,dt\le2\alpha.
\tag{11}
\]
The last inequalities hold on (8), using
\(\epsilon/\sqrt\lambda\le\alpha\le1/16\). No source error is
differentiated. The same argument gives the source-energy bounds for
training responses. None of these estimates sums over passive points.

The effective runtime readout additionally satisfies
\[
\int_0^\infty\|\dot{\widehat w}_C\|_{M_L}\,dt
 \le\alpha(2+680F_cz^2)<5\alpha
\tag{12}
\]
on (8), by the exact projector-derivative identity in the source-energy
proof. This is a derived bound for the specified readout, not an assumed
norm bound on arbitrary decoders.

## 5. Deterministic comparison and the endpoint

The original polynomial comparisons apply to the finite-panel source
interface above. Here is the dependency check and exact cancellation
that makes this a reduction rather than a new stability assumption.

For proof only, take the selected dense first weights and readout, and
define each reference hidden mixer by its selected initialization plus
the integral of selected dense rank-one training updates. Denote the
hidden tuple by \(\theta_{h,R}\). Its actual dense restricted features
are not asserted to equal a forward pass through these reference mixers.
Their difference is precisely the paired-action defect in the source
interface. Reference objects never enter the runtime.

Set
\[
E_h=\|\theta_{h,C}-\theta_{h,R}\|,\quad
e=(c_C-c_n)/\sqrt m,\quad T_C=V_CQ_C^{-1},\quad P_C=T_CV_C^*,
\]
\[
\pi=T_Ce,\quad \zeta=w_C-w_R+\pi,\quad
E=E_h+\|\pi\|+\|\zeta\|.
\]
All these errors start at zero. The exact
residual and raw-readout differences satisfy
\[
\dot e=-2(Q_C+\mathcal J_C^*\mathcal J_C)e
 -2\Delta\mathcal Kc_n/\sqrt m,
\qquad
\frac d{dt}(w_C-w_R)=2V_Ce+2(V_C-V_R)c_n/\sqrt m,
\]
where \(\Delta\mathcal K\) is the difference of normalized training
tangent Grams. Since \(T_CQ_C=V_C\), the term \(-2V_Ce\) in
\(\dot\pi\) cancels \(+2V_Ce\) in the second equation. Also
\(V_C^*\pi=e\), so pairing with \(\pi\) yields damping
\(-2\|e\|_2^2\). The hidden Gram may have no sign in this pairing,
but (8) gives the sufficient absorption
\[
8\|\mathcal J_C\|^2/\lambda
 \le200z^2F_c\le25/(32H_c^2)<1.
\tag{13}
\]
The derivative of \(T_C\) uses the actual compact forward pass only:
\[
\dot T_C=(I-P_C)\dot V_CQ_C^{-1}-T_C\dot V_C^*T_C.
\]
All remaining Gram factors, training backward differences, and residual
activity integrals coincide with the imported comparison. The forward
subtraction is evaluated only at \(v_i\), \(i\le p\), and thus asks
exactly for the forward half of the panel event. Taking a maximum over
these points introduces no factor \(p\).

On the common cap \(Y\le\lambda\beta^{-30L}\), put \(X=\beta^L\).
The proved reduction is
\[
E(t)\le X^{22}\int_0^t
 [M\rho_n+\rho_C+\nu/\sqrt\lambda]
 [E+\epsilon(1+\lambda^{-1/2})]\,ds,
\]
where \(M=1+16X^{21}z\sqrt{\ell_n}\),
\(\nu=\|V_Rc_n/\sqrt m\|\), and
\(\rho_n=\|c_n\|_2/\sqrt m\). Equations (9)--(11) give an
integrated coefficient at most \(1+\sqrt{\ell_n}\). The same source
readout-pairing estimate at each panel point then yields
\[
\sup_{0\le t\le T_n}\max_{i\le p}|f_C(t,v_i)-f_n(t,v_i)|
 \le6\beta^{40L}z(1+\lambda^{-1/2})
       n^{-1}e^{2\sqrt{\ell_n}}.
\tag{14}
\]
Every coefficient and absorption is unchanged from the complete
polynomial comparison; (11) is its essential energy-scale input.

Both fitting proofs independently bound the output speed at every
declared input by an integrable residual multiple. The compact bound even
holds at every unit input, by its operator and feature recurrences alone.
In the imported notation,
the sum of dense and compact tails used after \(T_n\) is bounded by
\(z(16\mathcal K+4B_f)e^{-8\ell_n}\). The same-time triangle inequality
therefore proves
\[
\sup_{t\in[0,\infty]}\max_{i\le p}|f_C(t,v_i)-f_n(t,v_i)|
 \le10\beta^{40L}z(1+\lambda^{-1/2})
       n^{-1}e^{2\sqrt{\ell_n}}.
\tag{15}
\]
The endpoint is included because each parameter trajectory converges and
its output tail is bounded. Training continues by (5) after \(T_n\);
there is no frozen endpoint table.

On the full allowance (8), use the complete corrected forcing envelope
from the full-range proof. Its integrated coefficient is at most
\(44+32\sqrt{\ell_n}\), and its output bound is
\[
\sup_{t\in[0,\infty]}\max_{i\le p}|f_C-f_n|
 \le C\beta^{42L}\frac Y\lambda
 \max(1,\lambda^{-1/2})
 n^{-1}(1+\sqrt{\ell_n})e^{32\sqrt{\ell_n}},
\tag{16}
\]
where \(C\) is universal. In particular it is independent of
\(p,d,m,L,\gamma,Y,n\), apart from the displayed factors.
This uses the same source and fitting event, and retains the actual
label factor. The full-range source recurrences cannot be replaced by
the smaller-cap simplifications when counting their constants.

## 6. Conditional temporal rank and complete retained inventory

Here is a direct sufficient source-regularity condition that converts
this runtime reduction into an absolute logarithmic exponent. It is
stated conditionally to isolate the unresolved producer obligation.

Assume each required vector family in Section 3 has a holomorphic
extension to a neighborhood of
\[
[-r_n,T_n+r_n]+i[-r_n,r_n],\qquad
r_n=c_t/\sqrt{\ell_n},
\tag{17}
\]
and every coordinate there has modulus at most \(M_0\sqrt n\).
Here \(c_t,M_0>0\) are fixed before the width limit. Assume also that
finite operations on initial data and finite initial jets produce the
coefficients with prescribed finite error, preserving initialized-image
pairings. This is an initialization-only coefficient construction
condition, not permission to inspect a future training trajectory.

Put \(a_t=r_n/(4T_n)=c_t\lambda/(128\ell_n^{3/2})\), and assume
\(a_t\le1\) and \(r_n\le T_n\). The substitution
\(t=T_n(1+\cos u)/2\) maps \(|\operatorname{Im}u|\le a_t\)
inside (17): its imaginary displacement is at most
\(T_n\sinh(a_t)/2\le T_na_t\le r_n/4\), and its real overhang
is at most \(T_na_t^2/2\le r_n/32\). The cosine coefficients
therefore have modulus at most \(2M_0\sqrt n\,e^{-a_t k}\).
The tail after degree \(N\) is at most
\(4M_0\sqrt n\,a_t^{-1}e^{-a_t(N+1)}\). Consequently
\[
N=\left\lceil a_t^{-1}
 \log\frac{8M_0\sqrt n}{a_t\epsilon}\right\rceil
\tag{18}
\]
makes the truncation error at most \(\epsilon/2\); allocate the
other half to finite coefficient approximation.

At each layer at most \(2(p+m)\) vector source families are needed.
Hence the source rank, including exact initialization additions, obeys
\[
R\le2(p+m)(N+1)+2m+d+1.
\tag{19}
\]
This counts coefficient vectors spanning the proof source spaces.
Those full-width vectors are preprocessing objects and are discarded
after selection; no full-width vector is retained for runtime queries.

For an explicit eventual bound, require
\[
\log_+\frac{1024M_0}{c_t\lambda}\le\ell_n.
\tag{20}
\]
Since \((3/2)\log\ell_n\le\ell_n\) and \(\log n\le\ell_n\),
the logarithm in (18) is at most \(4\ell_n\). Thus define
\[
A_{\rm panel}=\frac{1024(p+m)}{c_t\lambda},\qquad
B_{\rm panel}=4(p+m)+2m+d+1;
\quad R\le A_{\rm panel}\ell_n^{5/2}+B_{\rm panel}.
\tag{21}
\]
The inherited selection has \(q_j\le9R\). Let \(q=\max_jq_j\).
The exact moving-state count is
\[
q_1d+\sum_{j=2}^Lq_jq_{j-1}+q_L+m
 \le(L-1)q^2+q(d+1)+m.
\tag{22}
\]
In particular there are only \(m\) residual coordinates, not \(p\).

The imported conservative all-retained training inventory, including
fixed metrics and copies, data, current training feature/response arrays,
and Gram/solve workspace, is
\(1020(L+1)R^2+10m(d+1)\). Retain the remaining inputs in
\((p-m)d\) coordinates, all \(p\) current outputs, and at most
\(4q\) extra scalar workspace for sequential passive forward evaluation.
Two neuron buffers suffice for one forward pass; the extra allowance
covers the final metric pairing and a temporary readout vector. Sequential
evaluation does not discard or externally stream the panel inputs.
The whole inventory is bounded by
\[
1020(L+1)R^2+10m(d+1)+(p-m)d+p+36R+D_{\rm alg}.
\tag{23}
\]
Here \(D_{\rm alg}\) counts the fixed finite activation descriptions,
evaluation workspace, and fixed runtime program in the inherited
exact-real computational convention. It is not a width-dependent
program containing the dense model. If an activation is supplied only
as an abstract function oracle with no counted evaluator, that is a
separate representation assumption and is not silently free in (23).

Combining (21)--(23) gives \(C_{\rm panel}\ell_n^5\) with the entire
displayed sufficient prefactor
\[
C_{\rm panel}=1020(L+1)(A_{\rm panel}+B_{\rm panel})^2
 +36(A_{\rm panel}+B_{\rm panel})+10m(d+1)
 +(p-m)d+p+D_{\rm alg}.
\tag{24}
\]
The exponent five is absolute. This does not make the prefactor
dimension independent or prove a bit-complexity bound. If the localized
source gives \(c_t=a_{\rm strip}\lambda/(1024Y^2U_{\rm fin})\),
then
\(A_{\rm panel}=2^{20}(p+m)(U_{\rm fin}/a_{\rm strip})(Y/\lambda)^2\),
which keeps the actual label dependence.

The sufficient width is the maximum of the source/selection success
threshold, dense initialization threshold, coefficient-construction
threshold, \(\epsilon\le\min(1,Y,16Y/\lambda)\), and the explicit
conditions (17)--(20) plus the localized source's own width gates.
The imported finite-query source proof has an unquantified stochastic
success width. No effective polynomial threshold is claimed here.
For \(p=p(n)\), (24) is not a fixed prefactor: the panel itself costs
\(pd\), the displayed construction costs quadratically in \(p+m\),
and the probability union must be rechecked. The exponent-five theorem
as stated has all task parameters, including \(p\), fixed.

## 7. Actual dense variability on this same panel

Define the panel norm
\[
\|f-g\|_{\rm panel}
 =\sup_{t\in[0,\infty]}\max_{i\le p}|f(t,v_i)-g(t,v_i)|.
\]
For \(m\ge2\), the imported general variability lower theorem is
witnessed at a deterministic training index, not at a query selected
outside the panel. It therefore implies, for every fixed confidence
\(1-\delta\) and sufficiently large individual width,
\[
\|f_n-\widetilde f_n\|_{\rm panel}
 \ge c_{\phi,L,\delta}
 \frac{Y\sqrt\gamma}{\sqrt n\,\ell_n^{5/2}}
\tag{25}
\]
with probability at least \(1-\delta\). Here the second dense run
has independent initialization and the same training data. On the
common cap one sufficient coefficient is
\[
c_{\phi,L,\delta}
 =\frac{\Phi^{-1}(1/2+\delta/4)}{128}
 \sqrt{q_L/\mu_4},
\]
where \(q_0=1\), \(q_j=\mathbb E\phi_j(\sqrt{q_{j-1}}Z)^2\),
\(\mu_4=\mathbb E\phi_L(\sqrt{q_{L-1}}Z)^4\), and \(Z\sim N(0,1)\).
On the full recurrence allowance multiply by the positive
activation/depth-only time factor \(\chi_{\rm act}\) of the imported
finite-query lower bridge. No panel gap enters.

This transfer uses the imported initialization CLT and finite-query
source theorem; it does not newly prove their stochastic dependencies.
Its scope is fixed \(d,m,L,y\), and its threshold is not effective.
The witnessing time is positive and at most
\(\chi(S)/(\lambda\sqrt{\ell_n})\). At training endpoints both dense
runs equal the labels, so (25) is not an endpoint separation statement.

When \(m=1\), use the separate scalar innovation condition
\(\eta=\operatorname{Var}(\phi_L(\sqrt{q_{L-1}}Z)^2)>0\).
If all activations are nonconstant analytic functions, their scalar
variances cannot collapse to zero: induction from \(q_0=1\) gives
\(q_{L-1}>0\), and a continuous nonconstant real function cannot have
a constant positive square on the full real line. Thus \(\eta>0\).
The imported scalar onset and trajectory bridge then supplies a
positive activation/depth-dependent lower coefficient of the same
\(n^{-1/2}\ell_n^{-5/2}\) order at the training point. If the activation
class instead permits effectively constant final features, positive
uncentered gap alone does not give this lower bound. Zero labels have
zero variability.

For every fixed nondegenerate task, (15) or (16), together with (25),
therefore implies
\[
\frac{\|f_C-f_n\|_{\rm panel}}
 {\|f_n-\widetilde f_n\|_{\rm panel}}
 \longrightarrow0\quad\hbox{in probability},
\tag{26}
\]
provided the finite-panel compression source event has success probability
tending to one. A union bound suffices; event independence is not needed.
For example the ratio of (15) to (25) is bounded by a fixed task
coefficient times
\(n^{-1/2}\ell_n^{5/2}e^{2\sqrt{\ell_n}}\), which tends to zero.
This is a comparison to actual dense discrepancy in the same panel norm,
and is logically stronger than comparison to an upper certificate.

## 8. Sources, checks, and remaining producer obligation

Allowed scientific inputs actually used were this study's README,
`docs/notation.qmd`, and the following authorized integrated files:

- `EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md` and its complete check;
- `GENERAL_EXPLICIT_FITTING.md`;
- `COMPACT_SOURCE_ENERGY.md`;
- `COMPACT_POLYNOMIAL_COMPARISON.md` and its complete check;
- `COMPACT_FULL_LABEL_RANGE.md` and its complete check;
- `UNBOUNDED_COMPRESSOR_BRIDGE.md`, initially its source inventory
  and rank/selection interface in Section 9; after freezing, also its
  Sections 1--2 and 6--8 for the coverage verification below;
- `GENERAL_VARIABILITY_LOWER_RESULT.md`,
  `GENERAL_TRAJECTORY_LOWER_BRIDGE.md`, and
  `GENERAL_ONSET_NONDEGENERACY.md`.

The canonical-notation skill remained permission-inaccessible. The
explicit user notation contract and maintained notation were followed;
the accessible rigorous-math and conjecture-investigation skills and
their relevant contract/audit references were read. No other study or
route was read, no experiment was run, and no Git index change was made.

The deterministic route has checked training-only normalization, exact
readout consistency, all-time fitting, the energy-scale cancellation,
the full label range, the temporal coefficient count, and the complete
additional panel inventory. This file has not received an independent
check and makes no promotion claim.

The remaining inherited obligation is the validity of the imported local
insertion theorem, selection and initialization-only coefficient
construction. Section 9 checks that the authorized finite-query
localization supplies all additional temporal source coverage needed
here relative to those interfaces. Neither deterministic fitting nor
the finite number of observations alone proves that producer theorem.

## 9. Post-freeze verification of the authorized localized source

After the first candidate was frozen, the supervisor directed verification
of the existing finite-query localization. This section uses the original
authorized integrated sources, not another current route's argument.

`GENERAL_TRAJECTORY_LOWER_BRIDGE.md`, Sections 2--3, takes any fixed
finite collection of real queries, preserves the training activity and
source allowance \(S=16Y/\lambda\le S_*^{\rm src}\), and replaces only
the spatial Gaussian union by a finite query union. Its conclusion is
holomorphy on (17), with
\[
c_t=\chi(S)/\lambda,\qquad
\chi(S)=\min\{1,a_{\rm strip}/(4S^2U_{\rm fin}(S))\}>0.
\tag{27}
\]
The recurrence \(U_{\rm fin}\) is that source's formula (9), with
the numerical Gaussian union coefficient 64. No spatial query net is
used. On the full source allowance, \(\chi(S)\ge\chi_{\rm act}>0\),
where \(\chi_{\rm act}\) depends only on activations and depth; on
the common cap \(Y\le\lambda\beta^{-30L}\), \(\chi(S)=1\).

The localized theorem explicitly retains the original complex-time
operator caps ten, contour activity at most \(S\), feature RMS bounds
\(H_j\), and readout RMS at most \(SH_L\). Here use the source's
half-strip derivative constant
\(s_{\rm src}=\max(1,\sup_{j,|\operatorname{Im}z|\le a_{\rm strip}/2}
|\phi'_j(z)|)\), and
\[
H_1=\max(1,b+20s_{\rm src}),\qquad
H_j=\max(1,b+10s_{\rm src}H_{j-1}).
\]
For completeness, these
properties supply more than its displayed prediction bound. The complex
backward recursion gives
\[
\|\delta_n^{(j)}(t,v_a)\|_2/\sqrt n\le S\tau_j,
\qquad \tau_j=s_{\rm src}H_L(10s_{\rm src})^{L-j}.
\]
The initialized hidden operators have norm at most eight, so their
forward images have RMS at most \(8H_{j-1}\) and their reverse images
have RMS at most \(8S\tau_{j+1}\). All four families are holomorphic:
the trained weights and features are holomorphic on the stated domain,
the backward equations use analytic gates and transpose, not conjugation,
and the initialized matrices are constant in time. Since \(S\le1\),
\[
M_0=10\max\{\max_jH_j,\max_j\tau_j\}
\tag{28}
\]
is a valid coefficient bound in (17) for all four families. The training
carrier maximum is the unchanged original source (23), exactly (7).
Thus no passive backward response estimate or source family must be
added to obtain the runtime comparison.

With (27), the scalar degree estimate (18) yields, for \(p\ge m\),
\[
R\le\frac{3072p}{\chi(S)}\ell_n^{5/2}+2m+d+1.
\tag{29}
\]
Indeed (21) gives \(2048p\chi(S)^{-1}\ell_n^{5/2}+8p+2m+d+1\),
and \(\chi(S)\le1\), \(\ell_n\ge1\) absorb \(8p\) into the
displayed coefficient. Substituting
\(A=3072p/\chi(S)\), \(B=2m+d+1\) for the corresponding two
rank coefficients in (23)--(24) gives a complete exponent-five retained
inventory. In particular the temporal leading coefficient has no
dimension dependence. One may use \(\chi_{\rm act}\) for a uniform
coefficient on the full recurrence label interval, and one on the
common cap.

A convenient rounded scalar inventory is obtained by setting
\[
R_n=\left\lceil3072p\chi(S)^{-1}\ell_n^{5/2}\right\rceil+2m+d+1.
\]
The additive padding and ceiling cost at most
\(2m+d+2\le3p+2\le5p\), so
\[
R_n\le3077p\chi(S)^{-1}\ell_n^{5/2},\qquad
q\le9R_n<30000p\chi(S)^{-1}\ell_n^{5/2}.
\]
The conservative retained count
\(2048(L+1)R_n^2+16p(d+1)+D_{\rm alg}\) dominates (23): its
quadratic allowance absorbs \(36R_n\), and the data/output allowance
exceeds \(10m(d+1)+(p-m)d+p\). Since
\(2048\cdot3077^2<2^{36}\), a sufficient final bound is
\[
\operatorname{storage}(C)
 \le2^{36}(L+1)p^2\chi(S)^{-2}\ell_n^5
       +16p(d+1)+D_{\rm alg}.
\tag{30}
\]

The localized stochastic event still inherits the original insertion
interface and has an unquantified success width. The conclusion here is
the transfer of that already-authorized interface, not a fresh proof of
its outside insertion dependencies. The initialization-only finite-jet
coefficient construction and exact selection are likewise retained from
the integrated bridge's Section 9. Removing angular approximation
requires fewer scalar coefficient operations and source families; it
does not supply or retain a target trajectory as a runtime oracle.
