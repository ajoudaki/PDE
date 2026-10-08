# A finite initialization panel: source rank, inverse accuracy, and storage

2026-10-08. Scoped theoretical audit. This note gives a deterministic
finite-panel consequence of the analytic-source, coordinate-selection,
fitting, and source-to-runtime interfaces in the authorized sources. It
does not independently certify their probability proof. In particular it
does not certify the empirical approximate-source and randomized-selector
choices merely from agreement of the runtime equations.

The sufficient bound obtained here is

\[
O\!\left((L+1)(2m+d+1)^2+
 (L+1)(2m+p)^2\left[\frac{U_{\rm fin}(16Ym/\gamma)}a\right]^2
 Y^4\left(\frac m\gamma\right)^4[\log(en)]^5
 +(m+p)d+m+p\right).
\tag{1}
\]

Here **p is the number of additional passive inputs**, not the total
panel size; the panel has \(m+p\) inputs. The source recurrence
\(U_{\rm fin}\) is specified below. No spanning condition or inequality
\(d\le m\) is used. The error is measured on this declared panel, for all
physical times including the fitted endpoint. The fourth power of
\(Ym/\gamma\) has not been replaced by its label allowance. This is a
sufficient bound for the specified representation, not a sharp lower
bound or an optimality theorem.

## 1. Model, scope, and the source event

Fix normalized vectors \(v_i=x_i/\sqrt d\in S^{d-1}\),
\(1\le i\le m+p\), before initialization. Only \(i\le m\) have labels
\(y_i\). All hidden layers have width \(n\), with \(L\ge2\), and

\[
z^{(1)}(v)=Av,\qquad z^{(j)}(v)=W^{(j)}h^{(j-1)}(v),\qquad
h^{(j)}(v)=\phi_j(z^{(j)}(v)),\qquad f_n(v)=w^\top h^{(L)}(v)/n.
\]

The first entries are independent \(N(0,1)\), hidden entries independent
\(N(0,1/n)\), and \(w(0)=0\), independently across blocks. The residual
is \(r_a=f_n(v_a)-y_a\), the loss is \(m^{-1}\sum_{a\le m}r_a^2\), and
the block mobilities are \((n,1,\ldots,1,n)\). Thus

\[
\begin{aligned}
\dot A&=-\frac2m\sum_{a\le m}r_a\delta_a^{(1)}v_a^\top,\\
\dot W^{(j)}&=-\frac2{mn}\sum_{a\le m}r_a
 \delta_a^{(j)}h_a^{(j-1)\top},\qquad
\dot w=-\frac2m\sum_{a\le m}r_ah_a^{(L)},\\
\delta_a^{(L)}&=w\odot\phi_L'(z_a^{(L)}),\qquad
\delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot
 W^{(j+1)\top}\delta_a^{(j+1)}.
\end{aligned}
\tag{2}
\]

No passive input enters a sum or changes the denominator \(m\). Each
activation is real on the real axis, holomorphic on \(|\Im z|<a\), and
has bounded first derivative there. Unbounded activation values are
allowed. Let

\[
b=\max_j|\phi_j(0)|,\quad
s=\max\{1,\sup_{j,|\Im z|\le a/2}|\phi_j'(z)|\},\quad
t_2=\max\{1,\sup_{j,|\Im z|\le a/2}|\phi_j''(z)|\},\quad
\beta=\max(10,1+b,s,t_2,16/a).
\]

Define the uncentered initialized population Gram on **training** inputs:

\[
Q^{(0)}_{ab}=v_a^\top v_b,\qquad
Q^{(j)}_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)],\quad
Z\sim N(0,Q^{(j-1)}),\qquad \gamma=\lambda_{\min}(Q^{(L)})>0.
\]

Use \(Y=\|y\|_2/\sqrt m>0\), \(\lambda=\gamma/m\),
\(z=Y/\lambda\), \(S=16z\), and \(\ell=\log(en)\).
The paper's entire existing Harmonic label interval is retained:

\[
z\le\min\{(8H_d\sqrt{F_d})^{-1},
 (16H_c\sqrt{F_c})^{-1},S_*^{\rm src}/16\}.
\tag{3}
\]

The constants in (3) have exactly the current paper's definitions
(`paper/integrated_appendix.tex`, equations 0054--0056 and source S.10).
In particular the source condition implies \(S\le1\). An already
applicable additional Legendre allowance can be retained in a joint
theorem; no new cap is introduced here. For \(Y=0\), the zero predictor
is exact and all formulas dividing by \(Y\) are unnecessary.

For reference, the source coefficients needed to evaluate (1) are the
following finite recurrences. Every symbol in these displays is a fixed
scalar coefficient, not a runtime coordinate or a free approximation
order:

\[
\begin{gathered}
H_1=b+20s,\quad H_j=b+10sH_{j-1},\quad
k_j=H_L(10s)^{L-j},\quad \tau_j=sk_j,\\
P_1=3,\quad P_j=H_{j-1}+10sP_{j-1}+1,\quad f_j=sP_j,\\
g=\tau_1+\sum_{j=2}^L\tau_jH_{j-1},\quad
r_j^{\rm src}=P_jg,\quad q_j^{\rm src}=f_jg,\\
A_*=2sP_L+2s^2\sum_{j=2}^Lk_jP_{j-1},\quad
H_*=A_*+t_2\sum_{j=1}^LP_j^2k_j,\quad
E_*=t_2\sum_{j=1}^L(10s)^{2(j-1)}k_j,\\
D_0=(1+b+s)\{1+2H_*^2+4A_*^2(e^2-1)+E_*+s^2\max_jk_j^2\},\\
K_{\rm src}=128(D_0+1)\{1+32\max(1,\max_jH_j,\max_j\tau_j)\},\\
e_1=t_2r_1^{\rm src}P_1,\quad
e_j=t_2r_j^{\rm src}P_j+
s(q_{j-1}^{\rm src}+\tau_jH_{j-1}f_{j-1}+10e_{j-1}),\\
T_Q=8\max_jf_j\max_j(f_jH_*+e_j),\\
U_{\rm fin}(S)=\max\left\{4sK_{\rm src},\
 \max_{j\ge2}2\left[sK_{\rm src}
 (H_{j-1}^2+f_{j-1}^2+ST_Q+S^2H_{j-1}q_{j-1}^{\rm src})
 +64q_{j-1}^{\rm src}+1\right]\right\}.
\end{gathered}
\tag{4}
\]

These agree with the finite-query recurrence in
`GENERAL_TRAJECTORY_LOWER_BRIDGE.md` (9), with source constants from
`UNBOUNDED_COMPRESSOR_BRIDGE.md` (5)--(8), (22), (24).
The factor 64 is a Gaussian query-union coefficient. It is unrelated to
the separate 64 in the current paper's comparison exponent.

The required finite-query source event supplies, up to
\(T_0=32\ell/\lambda\), holomorphy on a neighborhood of

\[
[-r_t,T_0+r_t]+i[-r_t,r_t],\qquad
r_t=\frac{c_t}{\sqrt\ell},\qquad
c_t=\frac{a}{64YSU_{\rm fin}(S)}
    =\frac{a}{1024\lambda z^2U_{\rm fin}(S)}.
\tag{5}
\]

This uses the **uncapped** admissible radius from that bridge (12), not
the smaller convenient radius \(\min(1,a/[4S^2U_{\rm fin}])/(\lambda\sqrt\ell)\).
The latter leads to a valid different envelope, but using its label-cap
simplification would erase the explicitly requested label/gap powers.

The vector curves needed at layer \(j\) are

\[
\begin{array}{ll}
h^{(j)}(t,v_i),\ W_0^{(j)}h^{(j-1)}(t,v_i),&i\le m+p,\\
\delta_a^{(j)}(t),\ W_0^{(j+1)\top}\delta_a^{(j+1)}(t),&a\le m,
\end{array}
\tag{6}
\]

with nonexistent boundary-layer images omitted. Thus at most
\(2(2m+p)\) curves occur per layer. Passive backward sources are
unnecessary. Operator caps ten, feature RMS bounds \(H_j\), and readout
RMS bound \(SH_L\) give response RMS bounds \(S\tau_j\). Initial mixer
norms are at most eight. Consequently every coordinate in (6) is bounded
on (5) by

\[
M_n=M_0\sqrt n,\qquad M_0=10\max_j(H_j,\tau_j).
\tag{7}
\]

This inference uses \(|\phi_j(z)|\le b+s|z|\), not a uniform bound on
activation values. The event additionally supplies the training carrier
maximum \(16K_{\rm src}z\sqrt\ell\), exact initial Gram margin, and the
paired initialized-action identities used by the runtime comparison.

## 2. A complete temporal approximation and inverse degree

Let \(u(t)\) be any curve in (6) and put

\[
g(\theta)=u(T_0(1+\cos\theta)/2),\qquad
\alpha_t=\frac{r_t}{4T_0}
 =\frac{a}{2^{17}U_{\rm fin}(S)z^2\ell^{3/2}}.
\tag{8}
\]

At widths with \(0<\alpha_t\le1\), the strip
\(|\Im\theta|\le\alpha_t\) maps into (5): its imaginary displacement is
at most \(T_0\alpha_t=r_t/4\), and its real overshoot is at most
\(T_0\alpha_t^2/2\le r_t/8\). The even periodic function \(g\) has
Fourier coefficients \(c_k\) satisfying
\(\|c_k\|_\infty\le M_ne^{-\alpha_t|k|}\). To prove this, shift the
coefficient integral down by \(i\alpha_t\) for \(k>0\), up for
\(k<0\); holomorphy and periodicity cancel the vertical sides. Since
\(1-e^{-\alpha_t}\ge\alpha_t/2\), the Chebyshev series has tail

\[
\left\|u(t)-c_0-2\sum_{k=1}^Kc_k
 T_k(2t/T_0-1)\right\|_\infty
\le\frac{4M_n}{\alpha_t}e^{-\alpha_t(K+1)}.
\tag{9}
\]

For any prescribed source tolerance \(0<\eta\le\eta_0\), where
\(\eta_0=\min(1,Y,S)\), it is sufficient to choose

\[
K(\eta)=\left\lceil\frac1{\alpha_t}
 \log\frac{64M_0\sqrt n}{\alpha_t\eta}\right\rceil.
\tag{10}
\]

The analytic tail is below \(\eta/16\). Finite coefficient computation
must allocate the remaining tolerance while preserving each initialized
image exactly: compute a preimage coefficient \(b\), then its image as
\(W_0b\), using the same scalar operations. On operator norm eight,
coefficient accuracy \(\eta/[128\sqrt n(K+1)]\) makes the total image
coefficient error below \(\eta/8\). This is conditional on an admissible
finite initialization/jet evaluator; abstract analyticity alone does not
provide that evaluator. These vectors are discarded after selection.

Include the constant vector, all \(d\) first-weight columns, and exact
initial training features and forward images. Their dimension overhead
is at most \(B=2m+d+1\), so

\[
R(\eta)=B+2(2m+p)(K(\eta)+1)
\tag{11}
\]

is a valid integer dimension bound. It is harmless when \(R>n\), but
the exact dense branch is then cheaper. No inference \(d\le m\) is
needed. In particular, positive nonlinear feature Gram does not imply
that the input vectors span \(\mathbb R^d\).

The dimension-linear selection interface gives \(q_j\le9R\) and
positive metrics \(M_j\) with an auxiliary positive diagonal metric
\(D_j\), \(D_j/4\preceq M_j\preceq D_j\), and coordinate restrictions
\(R_j\) with exact source isometry
\((R_ju)^\top M_jR_jv=u^\top v/n\). A selected initialized mixer and its
metric adjoint reproduce both paired actions. This simultaneous
two-direction property, not just rank approximation of outputs, is the
input needed by the corrected optimizer.

## 3. The all-time error certificate and its inverse

For the theorem's corrected optimizer, the moving arrays are
\((A_C,B_C^{(2)},\ldots,B_C^{(L)},w_C,c_C)\), with \(c_C\in\mathbb R^m\).
Writing \(H_C\) for its current top training features, its effective
readout is

\[
\widehat w_C=w_C+H_C(H_C^\top M_LH_C)^{-1}
 (y-c_C-H_C^\top M_Lw_C).
\tag{12}
\]

The training prediction is exactly \(y-c_C\). Its backward directions
use metric adjoints and \(\widehat w_C\). Its residual update uses the
positive algebraic Gram specified in the current paper. Under (3), its
fitting theorem preserves normalized Gram gap at least \(\lambda/4\),
exponentially decaying residual, and convergent raw/effective parameters.

Here is the source-to-trajectory mechanism relevant to the panel count.
Coordinate source error \(\eta\) is dense RMS error at most \(\eta\)
and restricted metric error at most \(2\eta\). For source vectors of
dense RMS at most \(A_1,A_2\), insertion of source approximants gives

\[
|(R_ju)^\top M_jR_jv-u^\top v/n|
\le3\eta(A_1+A_2)+9\eta^2.
\tag{13}
\]

Paired initialized actions have defect at most \(18\eta\). Learned
actions are integrals of (13) against training residuals. The selected
dense readout is controlled by its residual-weighted source integral,
giving readout norm \(O(Y/\sqrt\lambda)\), rather than the coarser
\(O(Y/\lambda)\). No source error is differentiated.

Write \(c_n=y-f_n=-r_n\) on the training inputs. With normalized feature
maps \(V_C=H_C/\sqrt m\), let
\(T_C=V_C(V_C^*V_C)^{-1}\) and
\(e=(c_C-c_n)/\sqrt m\). In the error variable
\(w_C-R_Lw_n+T_Ce\), the leading terms
\(+2V_Ce\) and \(-2T_CV_C^*V_Ce=-2V_Ce\) cancel. The latter identity
means \(-2T_CQ_Ce\), with \(Q_C=V_C^*V_C\); it does not assert that
\(T_CV_C^*\) is the identity on all features. Remaining backward
subtractions and Gram inverses involve training indices only. At a
passive input, forward subtraction uses (6), and taking its maximum
introduces no factor \(p\).

Denote by \(\mathcal A_n\) and \(\mathcal D\) the current paper's
explicit recurrence coefficients in equations 0068 and 0057. They depend
on \(Y,m/\gamma,L,\beta\), not on the passive panel. Use the coefficient
**64** in the carrier term of its comparison exponent (equation 0068),
which is conservative at \(T_0\). The resulting interface is

\[
\sup_{t\in[0,\infty]}\max_{i\le m+p}|f_C(t,v_i)-f_n(t,v_i)|
\le\mathcal A_n\eta+\mathcal D e^{-8\ell}.
\tag{14}
\]

After \(T_0\), compare each trajectory to its own value at \(T_0\)
and integrate its fitted tail. Both continue training; there is no
frozen output table. The same inequality passes to the endpoint. The
current paper supplies, throughout (3), a structural envelope of the
form

\[
\mathcal A_n\le C\beta^{42L}\frac Y\lambda
 \max(1,\lambda^{-1/2})(1+\sqrt\ell)e^{64\sqrt\ell},\qquad
\mathcal D\le C\beta^{9L}\frac Y\lambda\max(1,\lambda^{-1/2}),
\tag{15}
\]

with a universal numerical \(C\) covering the fixed exponential
constant. For a fully numerical substitute one may use the explicit
upper certificates proved in the current paper, equations 0264--0265:

\[
\begin{aligned}
\overline{\mathcal A}_n&=2000e^{44}\beta^{42L}\frac Y\lambda
 (1+\lambda^{-1/2})(1+\sqrt\ell)e^{64\sqrt\ell},\\
\overline{\mathcal D}&=236\beta^{9L}\frac Y\lambda
 (1+\lambda^{-1/2}).
\end{aligned}
\tag{15a}
\]

The exact recurrences give the sharper finite prescription below;
substituting (15a) everywhere for \(\mathcal A_n,\mathcal D\) gives a
fully specified conservative prescription without evaluating any
comparison recurrences.

For a target \(\varepsilon>0\) satisfying the explicit tail test
\(\mathcal D e^{-8\ell}\le\varepsilon/2\), set

\[
\eta_\varepsilon=\min\{\eta_0,\varepsilon/(2\mathcal A_n)\},\qquad
q_\varepsilon=\min\{n,9R(\eta_\varepsilon)\}.
\tag{16}
\]

If \(\mathcal A_n=0\), take \(\eta_\varepsilon=\eta_0\).
In the analytic branch (10)--(14) prove error at most \(\varepsilon\).
If the minimum chooses \(n\), retain every dense coordinate with metric
\(I/n\), giving exact agreement. Thus (16) is an inverse theorem for
this finite horizon and its tail. It does not claim arbitrary accuracy
below that fixed tail floor; one must then enlarge the horizon using the
paper's separate analytic-extension theorem or use exact retention.
No empirical law for \(q\) has been substituted into (16).

## 4. Calibration to actual dense variability

Let \(\|f-g\|_{\rm panel}=\sup_{t\in[0,\infty]}
\max_{i\le m+p}|f(t,v_i)-g(t,v_i)|\), and let \(b_{n,\rm panel}\)
be its \(99.99\%\) independent-dense-pair quantile. The paper's \(b_n\)
is the corresponding **whole-sphere** quantile. Norm domination gives
\(b_{n,\rm panel}\le b_n\), not equality.

For \(m\ge2\), the authorized variability lower proof selects a
deterministic **training index**. Hence its lower bound transfers to
this panel if that source/CLT theorem is valid. A useful coefficient at
failure probability \(0<\delta_0<1\) is

\[
c_{\delta_0}=\frac{\chi_{\rm act}}{128}
 \Phi^{-1}(1/2+\delta_0/4)\sqrt{v_L/\mu_4},\qquad
v_0=1,\quad v_j=\mathbb E\phi_j(\sqrt{v_{j-1}}Z)^2,\quad
\mu_4=\mathbb E\phi_L(\sqrt{v_{L-1}}Z)^4,
\tag{17}
\]

where \(Z\sim N(0,1)\) and

\[
\chi_{\rm act}=\min\{1,a/[4(S_*^{\rm src})^2
 U_{\rm fin}(S_*^{\rm src})]\}>0.
\]

At sufficiently large individual widths the pair discrepancy is at
least \(c_{\delta_0}Y\sqrt\gamma/(\sqrt n\ell^{5/2})\) with probability
at least \(1-\delta_0\). The proof uses an early positive time, never
the fitted training endpoint. For example, take \(\delta_0=1/2\).
Since \(1/2<0.9999\), this lower probability implies the deterministic
quantile inequalities

\[
P_n:=\frac{c_{1/2}Y\sqrt\gamma}{\sqrt n\ell^{5/2}}
\le b_{n,\rm panel}\le b_n.
\tag{18}
\]

Indeed for every \(b<P_n\), the probability of discrepancy at most
\(b\) is at most \(1/2\), below the defining quantile level.
No independence between a compressed construction and a lower event is
required to draw this deterministic conclusion.

Choose \(\varepsilon=3P_n\) in (16). At the source event's prescribed
confidence \(1-\delta\), the panel error is at most
\(3b_{n,\rm panel}\), hence at most \(3b_n\). This is a panel error
bound calibrated to the whole-sphere benchmark; it is not a whole-sphere
error bound. With \(\delta=.01\), it has the paper's \(99\%\) comparison
confidence. The lower theorem's unquantified onset is an additional
width requirement. The tail test in (16) is eventually automatic.

A convenient stronger benchmark-free target is \(\varepsilon=Y/n\).
It eventually lies below \(3P_n\), gives a vanishing ratio to realized
panel discrepancy in probability, and has the same logarithmic storage
exponent. That stronger target costs more than required for a fixed
constant-factor certificate.

The direct target \(3P_n\) provides a precise constant-factor
improvement over source tolerance \(1/n\). For a fixed admissible
problem, (15) and its positive coefficient recurrences give
\(\log\mathcal A_n=o(\log n)\). Therefore

\[
\begin{array}{ll}
\eta=1/n:&
 \log[64M_0\sqrt n/(\alpha_t\eta)]
   =\tfrac32\log n+o(\log n),\\
\eta=\eta_{3P_n}:&
 \log[64M_0\sqrt n/(\alpha_t\eta)]
   =\log n+o(\log n).
\end{array}
\tag{19}
\]

Thus the certified temporal degree, and its leading rank, are reduced
by a factor tending to \(2/3\); the leading quadratic inventory is
reduced by \(4/9\). These are comparisons of the two explicit source
recipes, not of actual minimum selected ranks. They do not alter the
\(\log^5n\) power. At fixed confidence, the dependence of
\(c_{\delta_0}\), \(\gamma\), and the prefactors in (15) remains
inside the exact logarithm in (10).

For \(m=1\), positive uncentered gap alone does not guarantee positive
variability: a nonzero constant final activation gives a deterministic
training trajectory. Compression (14)--(16) still holds; a multiplicative
variability claim needs a separately established positive innovation or
an additive target. Zero labels have exact zero predictors.

## 5. Complete retained storage and explicit powers

The exact moving parameter-and-deficit dimension in the analytic branch
is

\[
dq_1+\sum_{j=2}^Lq_jq_{j-1}+q_L+m
\le(L-1)q_\varepsilon^2+(d+1)q_\varepsilon+m.
\tag{20}
\]

Current passive features can be recomputed sequentially from the state;
they do not require passive residual coordinates or a passive Gram
inverse. Retain all \(pd\) passive-input coordinates and all \(m+p\)
outputs; do not stream the panel from an uncounted external store.

The current paper's complete training inventory is at most
\(1020(L+1)R^2+10m(d+1)\). It includes fixed metrics and their inverse
caches, initialized copies, training feature/response arrays, Gram solves,
and current effective-readout workspace. Four additional neuron buffers
cost at most \(36R\). Consequently a sufficient retained count is

\[
1020(L+1)R^2+10m(d+1)+pd+(m+p)+36R+D_{\rm alg}.
\tag{21}
\]

The fixed activation evaluators, runtime description, and evaluator
workspace have counted size \(D_{\rm alg}\). Original-width vectors,
jets, quadratures, source bases, selected-index lists, and dense weights
are discarded. An evaluator may not hide width-dependent source data in
its program. This is a real-coordinate count, not a bit, conditioning,
preprocessing-time, or numerical-integration complexity theorem.

For either target above, impose the explicit eventual gate

\[
\log\frac{64M_0\sqrt n}{\alpha_t\eta_\varepsilon}\le4\ell,
\qquad \alpha_t\le1.
\tag{22}
\]

Then ceilings give \(K+1\le6\ell/\alpha_t\), so

\[
R\le B+A\ell^{5/2},\qquad
A=3\cdot2^{19}(2m+p)\frac{U_{\rm fin}(S)}a
 \left(\frac{Ym}\gamma\right)^2.
\tag{23}
\]

To state a fully numerical sufficient inventory without dropping cross
terms, combine (21), (23), and
\((B+A\ell^{5/2})^2\le2B^2+2A^2\ell^5\):

\[
\begin{aligned}
\operatorname{storage}\le{}&2040(L+1)(B^2+A^2\ell^5)
 +36B+36A\ell^{5/2}\\
&+10m(d+1)+pd+(m+p)+D_{\rm alg}.
\end{aligned}
\tag{24}
\]

Equation (24) is the explicit version of (1). In particular the
leading label/gap factor is \(Y^4(m/\gamma)^4\). The smaller cap
\(Y\le(\gamma/m)\beta^{-30L}\) has not been used to cancel that
factor. The dependence on \(d\) is in initialization/data overhead,
not in the exponent of \(\log n\).

For a coarse envelope using only \(\beta\), the recurrences (4),
\(S\le1\), \(L\ge2\), and \(\beta\ge10\) imply
\(U_{\rm fin}(S)/a\le\beta^{60L}\). One direct exponent ledger is

\[
\begin{gathered}
H_j,P_j\le\beta^{3j},\quad k_j\le\beta^{5L-2j},\quad
\tau_j\le\beta^{5L-2j+1},\quad g\le\beta^{7L},\\
\max_jr_j^{\rm src}\le\beta^{10L},\quad
\max_jq_j^{\rm src}\le\beta^{11L},\quad
A_*\le\beta^{8L},\quad H_*\le\beta^{11L},\quad E_*\le\beta^{8L},\\
D_0\le\beta^{24L},\quad K_{\rm src}\le\beta^{32L},\quad
\max_je_j\le\beta^{17L},\quad T_Q\le\beta^{22L},\quad
U_{\rm fin}\le\beta^{57L}.
\end{gathered}
\tag{25}
\]

These estimates use \(10s\le\beta^2\), geometric unrolling of each
recursion, and \(L\le\beta^L\). For example the bracket defining
\(U_j\) is at most \(4\beta^{22L}\), so its \(sK_{\rm src}\) term
is at most \(\beta^{56L}\), and the other terms are absorbed by
\(\beta^{57L}\). Since \(a^{-1}\le\beta/16\), the displayed
\(\beta^{60L}\) bound follows with slack. Substitution gives the
coarser sufficient leading storage envelope

\[
C(L+1)\beta^{120L}(2m+p)^2Y^4(m/\gamma)^4\ell^5,
\tag{26}
\]

plus the explicitly displayed initialization, data, and evaluator terms
in (24). This envelope is deliberately loose; (4), (10), (16), (21)
are the more informative finite recipe. Using \(S\le1\) to bound
the internal source coefficient does not replace the leading
\(Y^4(m/\gamma)^4\) by the label cap.

## 6. What remains conditional

The new derivations here are the temporal coefficient count, the exact
finite-panel inverse (16), its variability-target specialization, the
retained inventory, and the removal of the unnecessary input-span
assumption from these deterministic steps. They preserve the existing
source/fitting allowance and the original physical time.

The sufficient width must satisfy the inherited source probability
event, dense initialization, finite coefficient-construction conditions,
the radius gates

\[
n^{-1}\le\min(1,Y,S),\quad
\sqrt\ell\ge c_t\max\{8,\lambda,4\mathcal K/\log2,32YSD_W\},
\quad D_W=\max\{\tau_1,\max_{j\ge2}\tau_jH_{j-1}\},
\]

and (16), (22), together with the lower theorem's onset if (18) is used.
The event's stochastic threshold is qualitative and can depend on all
fixed task parameters and confidence. This note does not provide an
effective polynomial threshold, a uniform result for growing panels, or
one event covering infinitely many independently initialized widths.
For each fixed confidence the current source asserts eventual success;
its finite-query union must be rechecked if \(p=p(n)\).

The older finite-panel notes explicitly inherit their insertion,
selection, and finite-jet interfaces. The current paper includes later
arguments for these foundations. This scoped note has not independently
audited that entire source proof, so (1), (14), and (18) remain
conditional on their stated interfaces here. The source rank argument
cannot fill a missing Gaussian insertion estimate, nor can fitting
alone prove approximation accuracy.

The supervisor's direct inspection of `DeepHarmonic` confirms that the
empirical runtime does use the corrected readout and deficit Gram ODE,
matching (12). The remaining empirical/theorem distinction concerns
its full-rollout approximate source construction and its randomized
selector with metric condition cap 16, versus the certified source
tolerance and rigorous selection cap four used here. Agreement of the
runtime equations does not certify those initialization choices or a
particular empirical width.

## 7. Focused check of localization and the lower witness

The current paper's finite-query proof at lines 10003--10190 and the
complete authorized `GENERAL_TRAJECTORY_LOWER_BRIDGE.md` were checked
against this reduction. For fixed \(m,p,d,L,Y,\gamma\), a mesh of
spacing \(n^{-2}\) in (5) has \(O(n^4\sqrt\ell)\) points, hence at
most \(n^5\) eventually. Fixed input, training, layer and root indices
are absorbed into its stated \(n^{10}\) enclosing count. The Gaussian
tail union is \(4n^{10}e^{-1024\ell}\to0\); the off-grid bound is
\(n^{-2}\sqrt n\operatorname{polylog}n\to0\). Neither calculation
uses input span or a positive Gram on the passive panel. They do require
the independent-cavity Gaussian statement of the base insertion proof;
the finite-query union cannot establish it by itself. Its constants are
eventual fixed-panel constants, not an effective growing-panel theorem.

The short-contour estimates check with the displayed radius: length at
most \(2r_t\), residual RMS at most \(2Y\), and source response maximum
\(SU_{\rm fin}\sqrt\ell\) give displacement at most
\(8c_tYSU_{\rm fin}=a/8\). The other gates respectively give
factor-two residual growth, extra activity at most \(S/2\), and parameter
increment at most \(1/4\). Hence (5) uses the full admissible radius
without a lost factor of \(m\), \(\lambda\), or \(S\).

The innovation calculation at current paper lines 9833--10002 uses only
\(Q=\mathbb EHH^\top\succeq\gamma I\) and equal fourth-moment bounds.
Putting \(c=Qy\), its squared-area inequality yields

\[
\operatorname{tr}\operatorname{Cov}(H(y^\top H))
 \ge\frac{\gamma^3v_L}{16\mu_4}\|y\|_2^2.
\]

At least one fixed training coordinate has variance at least the right
side divided by \(m\). The exact onset velocity is \(2K_ny/m\);
the initialized Gram CLT and independence of the second dense run then
give variance at least \(\gamma^3v_LY^2/(2m^2\mu_4)\). Chebyshev
approximation on the parameter-two ellipse, with degree at most
\(4\ell\), multiplies the derivative by \(c_t/(32\ell^{5/2})\)
and loses a negligible \(O(Y/(\lambda n^2))\) term. Using the bounded
training-timescale radius \(\chi_{\rm act}/(\lambda\sqrt\ell)\)
gives (17)--(18). This calculation confirms the training witness and the
unweighted \(Y\sqrt\gamma\) scale; it does not prove the initialized
CLT or insertion theorem anew.

Finally, the current variable-\(\eta\) source-energy proof at lines
11664--11797 uses only \(\eta\le\min(1,Y,S)\). For example
\(\|w_R\|\le2Y/\sqrt\lambda+12\eta Y/\lambda\le3Y/\sqrt\lambda\)
uses \(\eta/\sqrt\lambda\le Y/\sqrt\lambda\le1/16\), not
\(\eta\le1/n\). All source defects in its comparison remain linear
in \(\eta\). Thus (16) may legitimately choose a tolerance larger
than \(1/n\) when only a variability-scale error is required. Its safe
comparison exponent is 64 as in the current paper; the older finite-panel
coefficient 32 is not needed here. No additional localization error was
identified in this scoped check. The base source theorem, initialized
CLT, and selection theorem remain distinct proof dependencies.

## 8. Runtime work and live workspace at a supplied width

Let \(q=\max_jq_j\), and let \(A_\phi\) bound the arithmetic work of
one scalar activation value or first-derivative evaluation over all
layers. Let \(W_\phi\) bound its additional scalar working storage.
These are declared evaluator costs; analyticity by itself does not
make them bounded-cost primitives. If evaluation costs depend on the
requested numerical precision or argument, retain that dependence in
\(A_\phi,W_\phi\).

Once the current effective readout has been computed and cached, a
single query costs

\[
O(Lq^2+dq+LqA_\phi)
\tag{27}
\]

arithmetic operations, with additional live workspace
\(O(q+d)+W_\phi\). The first layer costs \(dq\), each hidden matrix
action at most \(q^2\), and the forward activation calls at most
\(LqA_\phi\). Two neuron buffers suffice for sequential layer
evaluation. The cache refresh after a parameter update is charged to
model preparation, not hidden in (27). Evaluating the entire retained
panel sequentially costs \(m+p\) times (27), with its already counted
input/output storage and the same reusable query workspace.

One vector-field evaluation, including the current corrected readout,
all training directions and the dense \(m\)-by-\(m\) training Gram
solve, has the sufficient cost

\[
O(Lmq^2+mdq+Lqm^2+m^3+LmqA_\phi).
\tag{28}
\]

Forward/backward matrix actions and rank-one parameter updates give
\(Lmq^2+mdq\); feature/response Gram assembly gives \(Lqm^2\); a
dense factorization/solve gives \(m^3\). Apply metric adjoints as
successive matrix-vector products using the retained metric inverse
caches, rather than explicitly multiplying three \(q\)-square
matrices at every evaluation. That implementation avoids an additional
\(Lq^3\) term. Value/derivative calls contribute the last term in (28).

With one full right-hand-side output buffer included in the resident
matrix inventory, a sufficient additional simultaneous training
workspace is \(O(Lmq+m^2)+W_\phi\); a simple implementation
stores current training features/responses and Gram/solve work arrays.
The certified selected construction has \(q\ge m\), since its exact
positive training Gram has rank \(m\). Thus these arrays are already
covered, together with that right-hand-side buffer, by (21)'s
conservative all-retained inventory, apart from the
explicit evaluator allowance in \(D_{\rm alg}\). Counting workspace
here explains that inventory and does not add it a second time.

These are sufficient implementation costs, not optimality claims. A
different regularized runtime at \(q<m\) may replace the dense training
Gram solve by a \(q\)-dimensional spectral calculation, but that is not
needed for the certified positive-Gram branch here. Counts of an
eigendecomposition or inverse in an exact-real arithmetic model are
separate from a finite-precision algorithm's accuracy, conditioning,
iteration count, and bit complexity. Equations (27)--(28) also do not
bound how many vector-field evaluations a numerical integration of the
all-time flow requires, nor the initialization work discarded before
runtime. No new experiment is used in these counts.

Allowed inputs read: the three assigned finite-panel notes completely;
the relevant current paper setting, statement, source, supplied-budget,
inverse, and inventory passages; the specified finite-query bridge and
general variability result; the directly cited unbounded-source and
full-range coefficient passages; maintained notation and required skills.
No other study or empirical output was used, no experiment was run, and
no Git mutation was made.

## 9. Exact panel-span reduction: ambient dimension need not be squared

This additional deterministic observation concerns only the declared-panel
guarantee, not whole-sphere approximation. It sharpens the dimension overhead
without another regularity assumption. Put \(N=m+p\), and let the columns
of \(U\in\mathbb R^{d\times k}\) form an orthonormal basis of the span
of all normalized panel inputs, where \(1\le k\le\min(d,N)\).
Replace each input by \(U^Tv_i\) and the dense first matrix by \(A_0U\).
The new inputs still have norm one. Gaussian rotational invariance follows
directly from their covariance: each row of \(A_0U\) is centered Gaussian
with covariance \(U^TU=I_k\), independently across rows and other layers.
All panel pairwise inner products and the population feature Grams are
unchanged, including \(\gamma\).

This is an exact dynamical reduction, not just matching initialization in law.
All first-layer updates are linear combinations of the rows \(v_a^T\),
so \(A(t)(I-UU^T)=A_0(I-UU^T)\). On the panel,
\(A(t)v_i=A(t)UU^Tv_i\), and
\(\partial_t(AU)=-(2/m)\sum_a r_a\delta_a^{(1)}(U^Tv_a)^T\).
Induction through the remaining layers gives the same predictions, residuals,
and hidden/readout updates. The Frobenius first-layer mobility is unchanged
because multiplication by \(U\) is an isometry on the moving subspace.
Thus the original dense trajectories and the reduced-input trajectories agree
on the entire panel for all times, for the actual coupled initialization.

Apply Sections 1–5 with \(k\) replacing \(d\), and retain \(U\) as a
fixed input map when queries are supplied in the original coordinates. The
source overhead becomes \(B=2m+k+1\le3N+1\); the coefficient \(A\)
in (23) is unchanged. The first compressed weights have shape \(q\)-by-\(k\)
and the fixed input map has \(dk\) entries. It is unnecessary to multiply
these into a \(q\)-by-\(d\) matrix. Store both original panel inputs and
their transformed inputs if desired: their combined size is at most \(2Nd\).
The fixed map costs at most \(Nd\). Consequently (24) implies the sharper
sufficient total retained bound

\[
C(L+1)(m+p)^2\left\{1+
 \left[\frac{U_{\rm fin}(16Ym/\gamma)}a\right]^2
 \left(\frac{Ym}{\gamma}\right)^4[\log(en)]^5\right\}
+C(m+p)d+D_{\rm alg}.
\tag{29}
\]

The universal numerical \(C\) absorbs only the previously explicit numerical
constants and the inequalities \(2m+p\le2N\), \(B\le4N\).
One may use \(U_{\rm fin}/a\le\beta^{60L}\) for the fully beta-only
envelope. This improves the additive \((m+d)^2\) term to \((m+p)^2\)
plus linear ambient-input storage. It does not change the label/gap power or
the absolute fifth logarithmic power. The precision and qualitative-width
qualifications are unchanged.

A concrete extra setup allowance is \(O(dN^2+N^3+ndk)\) arithmetic for
an orthonormal panel basis and the dense first projection, with workspace
\(O(dN+N^2+nk)\) in addition to the original dense arrays. A subsequent
query first computes \(U^Tv\), at cost \(O(dk)\) and \(O(k)\) extra
workspace; the remainder uses (27) with \(k\) replacing \(d\).
All these operations use inputs declared at initialization and no passive
labels. Predictions outside the panel remain evaluable, but their accuracy
is not covered by (29) or by this projection argument.
