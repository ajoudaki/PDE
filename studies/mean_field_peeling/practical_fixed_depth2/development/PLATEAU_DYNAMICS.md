# Exact plateaus: invariant columns and a causal dormant-row kernel mechanism

2026-09-08. This note concerns a **distinct fixed bounded smooth activation with exact plateaus**, not the principal affine-plus-tanh activation in CONTRACT.md. It gives an exact frozen/active split, additional physical energy estimates, and a compact-horizon readout-kernel floor for a physical or dissipative approximation path with the stated canonical causal source realization. It does **not** remove the lower incoming-field cap, construct the global uncapped population flow, or prove the actual uncapped finite-width bridge.

The useful mechanism is stronger than saying that a Gaussian summand survives. Some top neurons can be shown to remain on three prescribed plateaus throughout a compact time interval. On those neurons the readout still trains, but every backward gate is zero. Causal initialized returns and the learned operator row then vanish exactly. The remaining active primitive Gaussian path must be retained when selecting those neurons.

## 1. Setting and assertion levels

Let \(\phi\in C^\infty(\mathbb R)\) satisfy

\[
|\phi|\le B,\qquad |\phi'|\le D,\qquad |\phi''|\le D_2,
\qquad
\phi(z)=a_-\ (z\le-a),\quad
\phi(z)=a_+\ (z\ge a),
\tag{1}
\]

where \(a>0\) and \(a_+\ne a_-\) are fixed. All parameters are independent of width, data separation and the training horizon. The specific alternative being integrated with the parallel geometry analysis is

\[
\phi(z)=1+\frac1{2I}\int_0^z\rho(s)ds,
\quad \rho(s)=e^{-1/(1-s^2)}1_{|s|<1},
\quad I=\int_0^1\rho(s)ds.
\tag{1a}
\]

It has \(a=1\), \(a_-=1/2\), \(a_+=3/2\), and \(B=3/2\). Section 7.6 evaluates the clock certificate for exactly this activation. The 0-to-2 and centered plateau examples in Sections 7.3–7.4 are separately labeled comparisons. No parameter is taken to zero. The hypothesis on the frozen-feature Gram below is assumed in this dynamics note; its proof for every admissible input configuration is a separate geometric assertion.

Use the contract's raw equations, with \(c_i=y_i-f_i\):

\[
\dot w=\sum_i c_i\phi'(z_i)q_i u_i,
\qquad \dot U=\sum_i c_i b_i\otimes h_i,
\qquad \dot C=\sum_i c_i k_i,
\tag{2}
\]

\[
z_i=u_i^Tw,\quad h_i=\phi(z_i),\quad
v_i=(A_0+U)h_i,\quad k_i=\phi(v_i),\quad
b_i=C\phi'(v_i),\quad q_i=(A_0+U)^*b_i.
\]

There are three unit input vectors; their Gram may be singular. The initial first-layer root is standard Gaussian, \(U(0)=0\), and \(C(0)=0\). Thus \(E_0=3/2\) for labels in \(\{-1,1\}\).

The same arguments apply to a dissipative first-row cap \(\dot w=\chi(P)\sum_i c_i\phi'(z_i)q_i u_i\), with \(0\le\chi\le1\), provided the learned-operator and readout updates stay exact. For bounded activation the readout velocity is already bounded by \(B\sqrt{6E_0}\), so the readout cap in CAPS_MANUSCRIPT.md is inactive once its radius exceeds that number. These approximations obey

\[
E(t)+\int_0^t\|\dot\Theta(s)\|_{\rm raw}^2ds\le E_0.
\tag{3}
\]

We use the canonical initialized action and genuine adjoint. Its forward source decomposition is

\[
A_0h=\mathcal Fh+\mathcal Rh,
\tag{4}
\]

where \(\mathcal F\) is the primitive forward Gaussian isometry and \(\mathcal R\) is the complete initialized return. In the common-operator notation of GAUSSIAN_OPERATOR_ROUTE.md, \(\mathcal F=F\) and \(\mathcal R=R^*\). The primitive covariance is \(E[(\mathcal Fh)(\mathcal Fg)]=\langle h,g\rangle\). The return in (4) is never suppressed as a generic rule.

For the kernel result we require the canonical **causal source realization** of the path: at each deterministic time \(t\),

\[
\mathcal Rh_i(t)\in
\overline{\operatorname{span}}\{b_j(s):1\le j\le3, 0\le s\le t\}
\quad\hbox{in }H_2.
\tag{5}
\]

This is the chronological return property of the actual finite Gaussian programs. In a finite program, a forward return is a linear combination of backward queries available before that forward call. A useful invariant formulation is: the bottom coordinate is measurable with respect to its independent initial roots and the reverse primitive sources queried up to time \(t\). If \(g\in H_2\) is orthogonal to every past backward query, the reverse Gaussian source \(Rg\) is independent of those roots and sources and has mean zero. Hence \(\langle h_i(t),Rg\rangle=0\), proving (5). This also handles singular source covariances. For continuous paths it is a property of the justified source-adapted construction, not a consequence of a bounded abstract operator alone.

Thus the statements below apply to a fixed-cap canonical construction retaining this source chronology, and to a true physical source path whenever that path has already been identified. They do not assert source identification for an unconstructed uncapped path.

## 2. First-layer invariant set and the exact column split

Define the bottom event and multiplication projections

\[
\mathsf F=\{\omega_1:|z_i(0,\omega_1)|\ge a\text{ for every }i\},
\qquad P_f=1_{\mathsf F},\quad P_a=1-P_f.
\]

Write \(h_i^f=P_fh_i(0)\), and assume

\[
H_f=(\langle h_i^f,h_j^f\rangle)_{i,j=1}^3\succeq\kappa I_3,
\qquad\kappa>0.
\tag{6}
\]

**Lemma 1 (invariance).** On \(\mathsf F\), \(w(t)=w(0)\) throughout any existing compact-time strong physical path or the dissipative capped path.

**Proof.** Fix the actual incoming paths \(c_i(t)q_i(t,\omega_1)\), including the common cap factor when present. They are time-integrable for almost every \(\omega_1\), by their compact-time \(L^2\) bounds and Fubini. The resulting finite-dimensional nonautonomous equation in \(w\) has a time-integrable Lipschitz coefficient at most \(D_2\sum_i|c_iq_i|\). On \(\mathsf F\), the constant path \(w(0)\) solves that same equation because every gate is zero there. If two solutions have difference magnitude \(e(t)\), then \(e(t)\le\int_0^t L(s)e(s)ds\); applying the integrating factor to the right side gives \(e=0\). This proves the assertion without assuming that an individual zero gate freezes its own preactivation outside \(\mathsf F\). ∎

Consequently

\[
h_i(t)=h_i^f+h_i^a(t),\qquad h_i^a(t)=P_ah_i(t).
\tag{7}
\]

All initialized and learned columns split exactly:

\[
A_0=A_0P_f+A_0P_a,\qquad U=U_f+U_a,
\quad U_f=UP_f,\quad U_a=UP_a,
\]

\[
\dot U_f=\sum_jc_jb_j\otimes h_j^f,
\qquad
\dot U_a=\sum_jc_jb_j\otimes h_j^a.
\tag{8}
\]

The phrase “frozen first-layer neurons” does **not** mean frozen columns of the learned matrix: \(U_f\) evolves by (8). If

\[
D_j(t)=\int_0^t c_j(s)b_j(s)ds,
\]

then

\[
U_f(t)=\sum_j D_j(t)\otimes h_j^f,
\qquad U_f(t)h_i^f=\sum_j(H_f)_{ji}D_j(t).
\tag{9}
\]

The full forward and reverse fields are

\[
v_i=A_0h_i^f+A_0h_i^a+U_fh_i^f+U_ah_i^a,
\tag{10}
\]

\[
P_aq_i=P_aA_0^*b_i+U_a^*b_i,
\qquad P_fq_i=P_fA_0^*b_i+U_f^*b_i.
\tag{11}
\]

Only (11)'s active part enters the first-layer velocity. Both parts of (10), and both learned blocks in (8), remain in the algorithm.

Since \(h_i^f\) depends only on the initial bottom root, its initialized forward return is zero. Put

\[
G_i=\mathcal Fh_i^f=A_0h_i^f,
\qquad \xi_i(t)=\mathcal Fh_i^a(t).
\]

Then \(G\sim N(0,H_f)\), and the exact source split is

\[
v_i(t)=G_i+\xi_i(t)+\mathcal Rh_i^a(t)
+\sum_j(H_f)_{ji}D_j(t)+U_a(t)h_i^a(t).
\tag{12}
\]

The vector \(G\) is independent of the **whole primitive path** \((\xi_i(t))_{i,t}\). Indeed these are jointly Gaussian and

\[
E[G_j\xi_i(t)]=\langle h_j^f,h_i^a(t)\rangle=0.
\tag{13}
\]

The trained \(h_i^a\) may depend on all preceding physical feedback. This changes the deterministic covariance of the primitive family but not the exact support orthogonality in (13). Independence is not asserted for \(G\) and the full active initialized contribution \(A_0h_i^a=\xi_i+\mathcal Rh_i^a\). The latter includes the adapted return.

## 3. Extra physical energy control from the invariant Gram

At every reached state, \(H(t)=H_f+H_a(t)\succeq\kappa I\). Since \(U_f\) and \(U_a\) have orthogonal domain supports,

\[
\|\dot U\|_{\rm HS}^2\ge\|\dot U_f\|_{\rm HS}^2
=\sum_{i,j}(H_f)_{ij}\langle c_ib_i,c_jb_j\rangle
\ge\kappa\sum_i\|c_ib_i\|_2^2.
\tag{14}
\]

To verify the last inequality, diagonalize the real symmetric matrix \(H_f-\kappa I\); its quadratic form on a triple of Hilbert vectors is a sum of nonnegative eigenvalues times squared Hilbert norms. Integration of (14) and (3) gives

\[
\int_0^T\sum_i\|c_ib_i\|_2^2dt\le E_0/\kappa,
\quad
\int_0^T\sum_i\|c_iq_i\|_2^2dt
\le(\|A_0\|+\sqrt{TE_0})^2E_0/\kappa.
\tag{15}
\]

The true matrix kernel obeys

\[
K_A=H\circ(\langle b_i,b_j\rangle)\succeq
\kappa\operatorname{diag}(\|b_1\|_2^2,\|b_2\|_2^2,\|b_3\|_2^2).
\tag{16}
\]

For a direct proof of (16), its quadratic form minus the claimed diagonal term is the squared-norm quadratic form of \(H-\kappa I\) applied to \((x_ib_i)_i\), as in (14). In particular no inverse of the original input Gram occurs. The integral representation (9) also gives \(\sum_j\|D_j(t)\|_2^2\le TE_0/\kappa\).

These are individual residual-weighted incoming-field \(L^2\) controls. They do not by themselves give spatial exponential tails or a positive matrix-kernel floor when some \(b_i\) is zero.

## 4. A compact-time readout floor using permanently dormant top neurons

Put

\[
S=3B^2+3D^2E_0,\qquad
M_T=\sqrt{2(1+T)S},\qquad L_T=a+M_T+3,
\]

\[
p_T=\frac12(2\pi\,3B^2)^{-3/2}
\exp\left[-\frac{3L_T^2}{2\kappa}\right],
\qquad
\lambda_T=2(a_+-a_-)^2p_T.
\tag{17}
\]

**Theorem 2 (causal dormant-row floor).** Suppose a strong path on \([0,T]\) satisfies (1)–(6), the exact matrix update, and the energy inequality (3). Then its true readout Gram satisfies

\[
K_C(t)=(\langle k_i(t),k_j(t)\rangle)_{i,j=1}^3
\succeq\lambda_T I_3\qquad(0\le t\le T).
\tag{18}
\]

Thus (18) holds with the same positive constant across the canonical dissipative lower-cap paths for which the stated causal source construction is justified. It also holds for any already-existing source-identified true raw path from the initialization.

**Proof.** First, the primitive active source has an absolutely continuous version. The isometry \(\mathcal F\) maps the Bochner path derivative \(\dot h_i^a\) to its centered Gaussian derivative, and

\[
\sum_i\left(\|h_i^a(0)\|_2^2+
\int_0^T\|\dot h_i^a(t)\|_2^2dt\right)
\le3B^2+3D^2\int_0^T\|\dot w(t)\|_2^2dt\le S.
\]

Here \(\dot h_i=\phi'(z_i)u_i^T\dot w\), which is valid for capped and uncapped strong paths. The scalar path inequality

\[
\sup_{t\le T}|x(t)|^2
\le(1+T)\left(|x(0)|^2+\int_0^T|\dot x(t)|^2dt\right)
\]

follows from Cauchy–Schwarz applied to \(|x(0)|+\sqrt T\|\dot x\|_{L^2_t}\). It gives

\[
P\left(\max_i\sup_{t\le T}|\xi_i(t)|\le M_T\right)\ge\tfrac12.
\tag{19}
\]

For each \(\sigma\in\{-1,1\}^3\), let \(Q_\sigma\) be the unit box on which the \(i\)-th coordinate has sign \(\sigma_i\) and magnitude in \([a+M_T+2,a+M_T+3]\). By (6), \(H_f^{-1}\preceq\kappa^{-1}I\); also \(\lambda_{\max}(H_f)\le\operatorname{tr}H_f\le3B^2\). The Gaussian density on every such box is therefore at least

\[
(2\pi\,3B^2)^{-3/2}
\exp[-3L_T^2/(2\kappa)].
\]

Indeed the determinant is at most \((3B^2)^3\), and every box point has squared Euclidean norm at most \(3L_T^2\). Define

\[
\mathsf E_\sigma=
\{G\in Q_\sigma\}\cap
\{\max_i\sup_{t\le T}|\xi_i(t)|\le M_T\}.
\tag{20}
\]

Independence (13) and (19) imply \(P(\mathsf E_\sigma)\ge p_T\). These eight events are disjoint. On \(\mathsf E_\sigma\), each path \(G_i+\xi_i(t)\) stays at least distance 2 beyond its selected plateau boundary.

We next prove that the **actual** top preactivations stay on these plateaus. This is where causal returns are retained. Strong absolute continuity of \(h,U,C\) gives an almost surely continuous version of each \(v_i\), since

\[
\dot v_i=\dot U h_i+(A_0+U)\dot h_i
\]

is square-integrable on the compact interval. Thus \(b_i=C\phi'(v_i)\) has a pointwise continuous version. For a deterministic rational \(t\), let

\[
\mathsf D_t=\{b_j(s)=0\text{ for every }j\text{ and }s\le t\}.
\]

Every element of the closed span in (5) vanishes almost surely on \(\mathsf D_t\): multiplication by \(1_{\mathsf D_t}\) is a bounded \(L^2\) operator and annihilates every generator. Hence \(\mathcal Rh_i^a(t)=0\) on \(\mathsf D_t\). The learned integral

\[
(U(t)h_i(t))(\omega_2)
=\int_0^t\sum_jc_j(s)b_j(s,\omega_2)
\langle h_j(s),h_i(t)\rangle ds
\tag{21}
\]

also vanishes there. Take one full-probability set on which these facts hold at all rational times and all paths above are continuous.

For a point of \(\mathsf E_\sigma\) in that set, suppose the actual \(v\) first exits its three selected open plateaus at time \(\tau\le T\). At time zero the return and learned terms are zero, so the initial point has the stated strict margins. At every rational \(t<\tau\), all preceding \(b_j\) vanish, and (12), (21) and (5) give

\[
v_i(t)=G_i+\xi_i(t).
\]

Continuity extends this equality to \(\tau\), where its right side is still at least distance 2 inside the selected plateau. This contradicts the definition of the first exit. Consequently, on \(\mathsf E_\sigma\),

\[
b_i(t)=0,\qquad
k_i(t)=a_{\sigma_i}\qquad(0\le t\le T).
\tag{22}
\]

The readout need not be frozen: on this event its exact equation is \(\dot C=\sum_i c_i a_{\sigma_i}\). Equation (22) persists because every top derivative remains zero, regardless of this readout change. Also the initialized active row \(A_0P_a\) has not been removed: its complete changing contribution reduces to \(\xi_i(t)\) on this event after the vanishing of the causal return has been proved.

Let \(a_\sigma=(a_{\sigma_1},a_{\sigma_2},a_{\sigma_3})\). For every \(x\in\mathbb R^3\), disjointness and (22) give

\[
x^TK_C(t)x\ge p_T\sum_{\sigma\in\{-1,1\}^3}(x^Ta_\sigma)^2.
\]

Writing \(m=(a_++a_-)/2\) and \(d=(a_+-a_-)/2\), symmetry gives

\[
\sum_\sigma a_\sigma a_\sigma^T
=8m^2\mathbf1\mathbf1^T+8d^2I
\succeq2(a_+-a_-)^2I.
\]

This proves (18). ∎

For a physical flow, or a dissipative lower-cap flow with exact readout update, the loss derivative therefore obeys

\[
E'\le-\|\dot C\|_2^2=-c^TK_Cc\le-2\lambda_T E,
\qquad E(t)\le E_0e^{-2\lambda_Tt}\quad(0\le t\le T).
\tag{23}
\]

The rate depends on the chosen horizon. Equation (23) is not an all-time constant-rate assertion.

## 5. Why this still does not close continuation

Bounded activation already gives

\[
\|C(t)\|_\infty\le B\int_0^t\|c(s)\|_1ds
\le B\sqrt{6E_0}\,T.
\tag{24}
\]

Thus the full top gate \(C\phi'(v)\) is locally Lipschitz in \((C,v)\) along compact-time states satisfying this bound. The learned bottom return is also pointwise controlled. From (21)'s adjoint version,

\[
|(U^*b_i)(t,\omega_1)|
\le B\int_0^t\sum_j|c_j(s)|\|b_j(s)\|_2\|b_i(t)\|_2ds,
\tag{25}
\]

which is finite uniformly in \(\omega_1\) and across caps on each fixed horizon, using (3), (24) and bounded gates.

The remaining lower incoming field is the initialized reverse action

\[
P_aA_0^*b_i=P_a\bigl(Rb_i+F^*b_i\bigr).
\tag{26}
\]

The primitive part \(Rb_i\) is Gaussian. The complete repeated-matrix reverse return \(F^*b_i\) remains in (26). Neither the frozen-feature Gram bound (6), the energy estimates (15), nor the positive readout floor (18) gives a spatial tail estimate for that return. For example, (15) is an integrated \(L^2\) bound, while cap removal needs uniform integrability or a stronger comparison estimate for the lower incoming fields. The dormant top events control a part of the readout Gram; they do not control this reverse return on the complementary active top population.

The identity \(v=G+\text{remainder}\) alone is insufficient for a kernel argument, because its remainder is adapted to \(G\). The theorem avoids that error by using the independent *primitive* active path and then proving that every other term vanishes on a specific causal event. It does not extend this eventwise cancellation to the full population.

There is also no established all-time residual clock. The explicit \(\lambda_T\) in (17) can decay exponentially with \(T\), so integrating the finite-horizon estimate (23) gives no horizon-independent clock bound.

One can formulate a useful conditional clock test. Let \(\ell(t)=\int_0^t\|c(s)\|_1ds\), and suppose a new argument proves a kernel lower bound \(K_C(t)\succeq\lambda(\ell(t))I\). For \(R(t)=\|c(t)\|_2=\sqrt{2E(t)}\), the physical loss identity and \(\ell'\le\sqrt3R\) imply, wherever \(R>0\),

\[
\frac{dR}{d\ell}\le-\frac{\lambda(\ell)}{\sqrt3}.
\]

Thus \(\int_0^\infty\lambda(s)ds>\sqrt3R(0)\) would force a finite residual clock. The bounds proved here do not establish that integral condition. Even a finite clock would still require a quantitative response or continuation argument for (26); it is not silently substituted for such an argument.

For completeness, the same construction can be parameterized by a finite residual-clock horizon \(L\). The raw equations and bounded activation give

\[
\|C\|_2\le B\ell,\qquad
\|U\|_{\rm op}\le\tfrac12 DB^2\ell^2,
\qquad
\left\|\frac{dh_i}{d\ell}\right\|_2
\le D^3B\ell\left(\|A_0\|+\tfrac12DB^2\ell^2\right).
\tag{27}
\]

Indeed \(\|\dot U\|_{\rm op}\le DB\|C\|_2\|c\|_1\), while \(\|\dot h_i\|_2\le D^2\|c\|_1\max_j\|q_j\|_2\) and \(\|q_j\|_2\le D\|A\|\|C\|_2\). If the clock is momentarily constant then the state is constant too, so these inequalities define an absolutely continuous clock-parametrized path on its attained clock interval. Replacing \(T,S\) in (17) by

\[
L,\qquad
S_L=3B^2+3D^6B^2\int_0^L s^2
\left(\|A_0\|+\tfrac12DB^2s^2\right)^2ds
\]

proves a positive floor as a function of \(L\). Its displayed lower bound has exponent of order \(-L^8\); it therefore supplies no divergent-integral clock criterion. Section 7 proves a sharper polynomial floor by a direct Gaussian chaining argument and checks its constants against fixed moderate plateau examples.

Finally, no uncapped actual finite-width theorem follows by taking a cap depending on width. A fixed-cap source-program identification plus the uniform kernel floor above is useful positive evidence, but removing the cap uniformly in width is still a separate assertion. The finite small Gaussian readout in the contract has not been removed from any claimed finite-algorithm theorem, because no such theorem is asserted here.

## 6. Claim register

| Assertion | Status |
|---|---|
| Neurons whose three initial first-layer gates vanish remain fixed under the exact raw flow | Proved for every existing strong path; also for dissipative common first-row caps |
| Their learned matrix columns stay fixed | False in general; their exact update is (8) |
| The initial frozen Gaussian vector is independent of the active primitive source path | Proved by canonical joint Gaussianity and support orthogonality |
| It is independent of the entire trained active initialized contribution | Not asserted; initialized returns retain dependence |
| \(H_f\succeq\kappa I\) yields individual residual-weighted reverse-field energy bounds | Proved in (14)–(16), with singular original input Grams allowed |
| Top rows initially on plateaus automatically remain on them | Not asserted; the changing active primitive path must be included |
| A positive-probability top population remains on each prescribed plateau pattern throughout \([0,T]\) | Proved using the primitive-path event and causal first-exit argument |
| A compact-time positive true readout-kernel floor follows | Proved for source-identified physical and canonical dissipative-cap paths |
| The floor is positive uniformly for all training time | Not established |
| The floor supplies lower reverse-return tails or global cap removal | Not established |
| Full fixed-activation population and actual GF/GD contract | Still open; this note treats a distinct plateau activation and proves no uncapped width bridge |

## 7. Elementary entropy sharpening in the residual clock

This section improves the horizon dependence of the dormant-row certificate. It does not close the residual clock for a fixed moderate plateau activation: the resulting exponent can be large, and the explicit certificate has insufficient integral even on an orthogonal-input example.

Let \(p=P(\mathsf F^c)\), \(\sigma=B\sqrt p\). The uniform active-feature bound is

\[
\|h_i^a(\ell)\|_2\le\sigma.
\]

By (27), every active feature curve, on a clock interval \([0,L]\), admits a common deterministic arclength majorant

\[
V(L)=D^3B\left(\frac{\|A_0\|L^2}{2}
+\frac{DB^2L^4}{8}\right).
\tag{28}
\]

More precisely, using the increasing parameter obtained by integrating the right side of (27) makes each of the three Hilbert curves 1-Lipschitz on \([0,V(L)]\). A constant part can be filled in by its constant value. For a nonconstant activation, \(D>0\); hence \(V(L)\) has a positive quartic coefficient.

### 7.1 A complete finite-cover and increment bound

**Lemma 3 (three Gaussian curves).** Suppose \(g_i:[0,V]\to H\), \(1\le i\le3\), are 1-Lipschitz Hilbert curves with \(\sup_s\|g_i(s)\|\le\sigma\), and \(\mathcal G:H\to L^2\) is a Gaussian isometry. For every \(\varepsilon>0\) and \(0<\delta<1\), the processes \(X_i(s)=\mathcal Gg_i(s)\) have a continuous joint version satisfying

\[
P\left(\max_i\sup_{0\le s\le V}|X_i(s)|\le
M(V,\varepsilon,\delta)\right)\ge1-\delta,
\]

\[
M(V,\varepsilon,\delta)=
(\sigma+\varepsilon)
\sqrt{2\log\!\left(\frac{12(2+V/\varepsilon)}{\delta}\right)}
+2\varepsilon\sqrt{2\log2}.
\tag{29}
\]

No independence between process coordinates, mesh points or increments is assumed.

**Proof.** The case \(V=0\) is just the Gaussian union bound and is covered by (29). For \(V>0\), let \(n=\max(1,\lceil V/\varepsilon\rceil)\), \(\Delta=V/n\le\varepsilon\). Divide \([0,V]\) into \(n\) intervals and then repeatedly bisect them. Let \(X_i^{(k)}\) be the piecewise linear interpolation at the level-\(k\) grid.

A centered Gaussian of variance at most \(s^2\) satisfies \(P(|Z|>s\sqrt{2\log(2/\eta)})\le\eta\), from its exponential moment and the two one-sided Chernoff bounds. Applying that bound to the \(3(n+1)\) base-grid values shows, with failure probability at most \(\delta/2\),

\[
\max_i\|X_i^{(0)}\|_\infty
\le\sigma\sqrt{2\log(12(n+1)/\delta)}.
\tag{30}
\]

At level \(k\ge1\), the difference \(X_i^{(k)}-X_i^{(k-1)}\) is piecewise triangular. Its extrema are midpoint differences

\[
\mathcal G\left[g_i(s_{\rm mid})
-\tfrac12g_i(s_{\rm left})-\tfrac12g_i(s_{\rm right})\right],
\]

whose variances are at most \(\Delta^2 4^{-k}\), by the Lipschitz condition and the triangle inequality. There are \(3n2^{k-1}\) such differences. A union bound with failure budget \(\delta 2^{-k-1}\) therefore gives

\[
\max_i\|X_i^{(k)}-X_i^{(k-1)}\|_\infty
\le\Delta2^{-k}
\sqrt{2\log(6n/\delta)+4k\log2}.
\tag{31}
\]

The failure probabilities in (30)–(31) sum to \(\delta\). On their joint event, the interpolation sequence is uniformly Cauchy because the displayed increment bounds are summable. Its limit is continuous and agrees with the original process at every point of the dense union of grids. Gaussian \(L^2\) continuity then identifies this as a version of the process on the full interval.

Put \(A=\log(12(n+1)/\delta)\). Using \(\sqrt{x+y}\le\sqrt x+\sqrt y\), \(\sum_{k\ge1}2^{-k}=1\), and

\[
\sum_{k\ge1}2^{-k}\sqrt k
\le\sqrt{\sum_{k\ge1}2^{-k}k}=\sqrt2,
\]

the sum of (31) is at most \(\Delta[\sqrt{2A}+2\sqrt{2\log2}]\). Add (30), use \(\Delta\le\varepsilon\) and \(n+1\le2+V/\varepsilon\), and obtain (29). To obtain a continuous version without conditioning on a fixed high-probability event, perform this construction with failure probabilities tending to zero; the resulting continuous versions agree on the countable dense grid and hence everywhere on overlaps. The union of the events has probability one. ∎

Apply Lemma 3 with \(g_i=h_i^a\), the arclength parameter (28), and \(\mathcal G=\mathcal F\). The independent frozen Gaussian vector remains exactly the one in (13). Thus Theorem 2's causal first-exit proof applies with the bound (29) in place of \(M_T\).

### 7.2 Polynomial exponent and sign-pattern optimization

Fix \(0<\delta<1\) and choose

\[
\varepsilon_L=\frac{\sigma}{\log(e+V(L)/\sigma)}.
\tag{32}
\]

Here \(\sigma>0\), since \(p\ge P(|z_1(0)|<a)>0\). As \(L\to\infty\), (28)–(32) give

\[
M(V(L),\varepsilon_L,\delta)^2
=8\sigma^2\log L+o(\log L).
\tag{33}
\]

For verification, \(\log V(L)=4\log L+O(1)\), \(\varepsilon_L/\sigma=O(1/\log L)\), and
\(\log(V/\varepsilon_L)=\log V+O(\log\log V)\). Substituting these three facts into (29) proves (33).

For a sign vector \(s\in\{-1,1\}^3\), define

\[
q_s=s^TH_f^{-1}s,
\qquad a_s=(a_{s_1},a_{s_2},a_{s_3}).
\]

Among collections of sign patterns whose plateau vectors span \(\mathbb R^3\), set

\[
q_*=
\min_{\mathcal S:\operatorname{span}\{a_s:s\in\mathcal S\}=\mathbb R^3}
\max_{s\in\mathcal S}q_s.
\tag{34}
\]

There is at least one such collection: the eight plateau vectors span, since differences of two appropriate vectors equal \((a_+-a_-)e_i\). The minimum in (34) is over finitely many collections and is attained.

To make the probability estimate explicit, take fixed box width \(w>0\) and margin \(\eta>0\), and put \(M=M(V(L),\varepsilon_L,\delta)\). In pattern \(s\), require \(G_i\) to have sign \(s_i\) and magnitude in \([a+M+\eta,a+M+\eta+w]\). If

\[
Q=\frac{\sqrt3(a+\eta+w)}{\sqrt\kappa},
\]

then every box point satisfies \(\|G\|_{H_f^{-1}}\le M\sqrt{q_s}+Q\). This follows by writing \(G=Ms+r\), using the triangle inequality in the positive definite \(H_f^{-1}\) norm, and \(\|r\|_2\le\sqrt3(a+\eta+w)\). Consequently the dormant event has probability at least

\[
(1-\delta)w^3(2\pi)^{-3/2}(\det H_f)^{-1/2}
\exp\!\left[-\tfrac12(M\sqrt{q_s}+Q)^2\right].
\tag{35}
\]

Choose a minimizing collection \(\mathcal S\) in (34), and let \(\mu_{\mathcal S}>0\) be the smallest eigenvalue of \(\sum_{s\in\mathcal S}a_sa_s^T\). The product of \(\mu_{\mathcal S}\) and (35) with \(q_s\) replaced by \(q_*\) is a valid readout-kernel floor \(\lambda(L)\). Its exponent is

\[
\log\lambda(L)=-\alpha\log L+o(\log L),
\qquad \alpha=4B^2p\,q_*.
\tag{36}
\]

In particular \(\alpha<1\) is sufficient for \(\int_0^\infty\lambda(L)dL=\infty\): choose \(\alpha<\beta<1\), and (36) gives \(\lambda(L)\ge L^{-\beta}\) eventually. If \(\alpha>1\), (36) instead makes this particular floor integrable. At \(\alpha=1\), (36) alone decides neither outcome; the explicit positive margin term in (35) cannot be discarded at that boundary. No conclusion about the clock is claimed from \(\alpha\ge1\).

The weaker universal exponent obtained without sign optimization is \(12B^2p/\kappa\), because \(q_s\le3/\kappa\). This entire argument accommodates a singular original input Gram; only \(H_f\), already required in (6), is inverted.

### 7.3 Orthogonal inputs: the moderate plateau example is supercritical

Take three orthogonal inputs and any activation satisfying (1). Define

\[
f=P(|Z|\ge a)^3,\quad p=1-f,\quad
m=(a_++a_-)/2,\quad d=(a_+-a_-)/2\ne0,
\qquad Z\sim N(0,1).
\]

The initial signs are independent uniform signs even after conditioning on the three magnitudes exceeding \(a\). Therefore

\[
H_f=f(d^2I+m^2\mathbf1\mathbf1^T),
\]

\[
q_s=\frac1{fd^2}\left(3-
\frac{m^2(\sum_i s_i)^2}{d^2+3m^2}\right).
\tag{37}
\]

The two all-equal patterns have the smaller value; all six mixed patterns have the same larger value. Any spanning collection must include a mixed pattern, and the full set of mixed patterns together with any necessary all-equal pattern spans. Hence

\[
q_* =\frac1{fd^2}\left(3-\frac{m^2}{d^2+3m^2}\right).
\tag{38}
\]

Because \(B\ge|m|+|d|\), (36)–(38) imply

\[
\alpha\ge\frac{12(1-f)}{f}.
\tag{39}
\]

For the algebra, put \(r=|m/d|\). After dividing by \(4p/f\), the required inequality is
\((1+r)^2(3+8r^2)/(1+3r^2)\ge3\); subtracting the right numerator gives \(6r+2r^2+16r^3+8r^4\ge0\). Equality occurs for centered plateaus and \(B=|d|\).

Thus a subcritical exponent requires \(f>12/13\), an exceptionally large frozen fraction. More concretely, if \(a\ge1/25\), then

\[
P(|Z|<a)\ge\frac2{25}\,
\frac{e^{-1/1250}}{\sqrt{2\pi}}>\frac2{75}.
\]

The last inequality follows from \(\pi<4\), \(e^{-x}\ge1-x\), and \((1-1/1250)/\sqrt8>1/3\). Consequently

\[
f<(73/75)^3<12/13,
\]

where the final rational comparison is \(13\cdot73^3=5{,}057{,}221<5{,}062{,}500=12\cdot75^3\). Hence \(a\ge1/25\) forces \(\alpha>1\) for every choice of plateau offset. Since a transition from \(a_-\) to \(a_+\) over \([-a,a]\) requires \(D\ge|d|/a\), even satisfying this sufficient subcriticality condition requires derivative gain \(D>25|d|\). This is incompatible with using the criterion as a moderate-gain repair of the contract.

For the fixed smooth step with plateaus 0 and 2 outside \([-1,1]\), \(B=2\), \(m=d=1\), and (38) gives the more specific exponent

\[
\alpha=44(1-f)/f.
\tag{40}
\]

No numerical experiment is needed to see that it is large. Since
\(P(|Z|<1)\ge2e^{-1/2}/\sqrt{2\pi}>1/\sqrt6>1/3\), one has \(f<8/27\), so (40) gives \(\alpha>209/2\). For centered plateaus \(-1,1\), the corresponding exponent is \(12(1-f)/f>57/2\). These are conservative analytic bounds, sufficient to rule out the divergent-integral criterion for this certificate.

### 7.4 Even the integral threshold is not met by this certificate on the moderate example

An integrable lower bound could still have integral exceeding the initial residual requirement. For the fixed 0-to-2 step with \(a=1\), the bound here does not. This can be checked even if the Gaussian sign probabilities in the dormant events are evaluated exactly, instead of using the conservative density boxes (35).

Keep \(H_f=f(I+\mathbf1\mathbf1^T)\), \(f<8/27\), and use any fixed \(0<\delta<1\), \(0<\varepsilon_L\le\sigma\) in (29). Restricting \(\varepsilon\le\sigma\) loses no minimizer of that displayed threshold. Indeed, for \(A=\log(12(2+V/\varepsilon)/\delta)>1\) and \(\varepsilon\ge\sigma\), its derivative is at least \(\sqrt{2A}-2/\sqrt{2A}+2\sqrt{2\log2}>0\). Let \(M_L\) denote the threshold. For each sign pattern, use the full Gaussian orthant event \(s_iG_i>1+M_L\) and the common active-source event \(\sup|\xi|\le M_L\). Every point of this event has a strictly positive, possibly point-dependent plateau margin, so the same first-exit proof applies.

When testing the hypothesis of an unbounded residual clock, write \(K_{\rm dorm}(L)\) for the contribution of these eight events to the readout Gram at each attained clock horizon. For \(x=(1,-1,0)/\sqrt2\), only the four patterns with \(s_1\ne s_2\) contribute, each with \((x^Ta_s)^2=2\). On any one of these four orthants, one has either \(G_1-G_2>2(1+M_L)\) or its negative. The difference is Gaussian with variance \(2f\). The one-sided bound

\[
P(Z>t)\le\tfrac12e^{-t^2/2}\qquad(t\ge0)
\]

follows by writing its density integral as \(e^{-t^2/2}\int_0^\infty e^{-tu}\varphi(u)du\le e^{-t^2/2}/2\). Discarding the active-event factor, which is at most one, gives

\[
\lambda_{\min}(K_{\rm dorm}(L))
\le x^TK_{\rm dorm}(L)x
\le4\exp[-(1+M_L)^2/f].
\tag{41}
\]

For this example \(D\ge1\), so (28) gives \(V(L)\ge L^4\), while \(\sigma=2\sqrt{1-f}\le2\). Equation (29) therefore implies

\[
M_L^2\ge2\sigma^2\log[6(1+L^4)].
\]

Put \(\beta=2\sigma^2/f=8(1-f)/f>19\). Using \((1+M_L)^2\ge1+M_L^2\), integrating (41), and splitting the integral at 1 yields

\[
\int_0^\infty\lambda_{\min}(K_{\rm dorm}(L))dL
\le4e^{-1/f}6^{-\beta}
\left(1+\frac1{4\beta-1}\right)<1<3.
\tag{42}
\]

For the simple last bound, \(1/f>27/8>3\), \(e^3>8\), and the parenthesis is less than 2. Binary labels and the zero population readout give \(\sqrt3R(0)=3\), exactly the threshold from Section 5. Any scalar lower bound extracted from these same dormant events is at most their smallest eigenvalue, so its integral cannot pass the threshold either. This includes the boxes (35), which are subsets of the orthants used in (41).

Equation (42) concerns the event certificate with the explicit threshold (29) and arclength majorant (28). It is not an upper bound on the actual trained kernel, an assertion that the actual residual clock diverges, or a no-go result for a sharper use of the physical trajectory.

### 7.5 Separation deterioration and the remaining possibility

The subcritical exponent cannot hold uniformly over all separated three-input configurations for one fixed activation merely from these estimates. Consider a family with \(u_2\to u_1\), keeping \(u_3\) away from both collinear directions; this may be done in dimension two, so the original three-input Gram is singular throughout. Whenever (6) holds along the family, dominated convergence gives

\[
\|h_1^f-h_2^f\|_2^2\longrightarrow0.
\]

Gaussian boundary events \(z_i(0)=\pm a\) have probability zero, which justifies the indicator convergence in this statement. A collection of plateau vectors spanning \(\mathbb R^3\) must contain a pattern with \(s_1\ne s_2\). For \(e=(1,-1,0)\), Cauchy–Schwarz in the \(H_f\) metric gives

\[
s^TH_f^{-1}s\ge\frac{(s^Te)^2}{e^TH_fe}
=\frac4{\|h_1^f-h_2^f\|_2^2}.
\]

Meanwhile \(p\ge P(|Z|<a)>0\). Thus the sufficient exponent \(\alpha\) in (36) becomes arbitrarily large along this family, even though each nondegenerate member can satisfy a positive separation condition of its own.

The new positive result is the fully derived polynomial floor and its explicit conditional subcriticality test. For fixed moderate plateaus, the available quantitative bounds do not pass that test or the integral threshold. A stronger causal estimate might reduce the active-source path complexity or replace the worst-case active-feature variance. Such an estimate would be new physical information; it is not supplied by the invariant Gaussian component, bounded activation, or the raw energy inequality alone.

### 7.6 Evaluation for the actual fixed alternative (1a)

For (1a), \(a=1\), \(m=1\), \(d=1/2\), \(B=3/2\), and \(D\ge1/2\) by the mean value theorem. Its coefficients do give a moderate derivative bound: \(I\ge\tfrac12e^{-4/3}\), hence \(D=e^{-1}/(2I)\le e^{1/3}<3/2\). The precise value is not needed below.

On three orthogonal inputs, with the same \(f=P(|Z|\ge1)^3<8/27\),

\[
H_f=f\left(\tfrac14I+\mathbf1\mathbf1^T\right),
\qquad \sigma^2=\tfrac94(1-f),
\qquad q_* =\frac{140}{13f}.
\]

The optimized sign-pattern exponent from (36) is therefore

\[
\alpha=\frac{1260}{13}\frac{1-f}{f}
>\frac{5985}{26}>1.
\tag{43}
\]

Thus the polynomial lower bound is integrable, not subcritical, for this actual moderate activation even in the orthogonal example.

Its finite integral is also insufficient for the residual-clock test. This can again be verified using exact Gaussian orthants, so it does not depend on the density-box slack. For \(x=(1,-1,0)/\sqrt2\), the four patterns with \(s_1\ne s_2\) have \((x^Ta_s)^2=1/2\). The frozen Gaussian difference now has variance

\[
\operatorname{Var}(G_1-G_2)=f/2.
\]

On one of those orthants its magnitude is at least \(2(1+M_L)\), with a fixed specified sign. The one-sided Gaussian bound used in (41) gives

\[
\lambda_{\min}(K_{\rm dorm}(L))
\le\exp[-4(1+M_L)^2/f].
\tag{44}
\]

This already allows any active-event probability at most one. For (28), \(D\ge1/2\) and \(B=3/2\) imply

\[
V(L)\ge\frac{27}{1024}L^4,
\qquad
\frac{V(L)}{\varepsilon_L}\ge\frac9{512}L^4
\quad\text{when }\varepsilon_L\le\sigma\le3/2.
\]

For every \(0<\delta<1\), (29) therefore yields

\[
M_L^2\ge2\sigma^2
\log\!\left[24\left(1+\frac9{1024}L^4\right)\right].
\]

Set \(\beta=8\sigma^2/f=18(1-f)/f>171/4\). Combining this estimate with (44), changing variables by \((9/1024)^{1/4}L\), and splitting the resulting integral at 1 gives

\[
\int_0^\infty\lambda_{\min}(K_{\rm dorm}(L))dL
\le e^{-4/f}24^{-\beta}
\left(\frac{1024}{9}\right)^{1/4}
\left(1+\frac1{4\beta-1}\right)
<1<3.
\tag{45}
\]

For the last simple comparison, \((1024/9)^{1/4}<4\), the parenthesis is less than 2, and \(4/f>27/2>3\), so the expression is less than \(8e^{-3}<1\). The omitted factors make it smaller. The restriction \(\varepsilon_L\le\sigma\) still loses no minimizer of (29), by the derivative check in Section 7.4.

Equation (45) is the requested evaluation for (1a). The explicit entropy-and-dormant-event certificate neither has divergent integral nor exceeds the initial binary-label requirement 3. It does not show that the true kernel is this small or that the true clock is infinite. It identifies the quantitative failure of this particular attempt to turn the invariant frozen Gaussian component into a global residual-clock theorem.
