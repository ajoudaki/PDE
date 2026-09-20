# Hilbert basin nullity from strongly continuous directional derivatives

Frozen scoped extension, 2026-09-18. Scientific inputs: the supervisor's prompt, this route's frozen `basin_probability_route.md`, and the complete allowed `basin_spectral_route.md`. No other scientific source or experiment was used. The solve-math-rigorously skill remains in force.

**Result.** Operator-norm continuity of the derivative is unnecessary for pulling back Lipschitz hypersurfaces. A locally Lipschitz map with a bounded linear Gâteaux derivative, continuous in each fixed direction, has the required local graph property whenever its derivative is invertible. The exact physical \((v,c,M)\) closure on the Hilbert space in `basin_spectral_route.md` satisfies these field and flow hypotheses. Combining this extension with that report's local Hilbert trapping graphs makes the point-convergent finite bad basin shy and null under an explicit full-support Gaussian law. This is a statement about randomized closure initial states, not the deterministic canonical state.

## 1. A directional pullback lemma

Let \(E\) be a real Banach space, \(U\subseteq E\) open, and \(\Psi:U\to E\) locally Lipschitz. Assume its norm Gâteaux derivative \(D\Psi(x)\in\mathcal L(E,E)\) exists at every \(x\in U\), and

\[
x\longmapsto D\Psi(x)v\quad\text{is norm continuous for each fixed }v\in E. \tag{1}
\]

Fix \(x_0\in U\) where \(D\Psi(x_0)\) is an isomorphism. Let

\[
\Gamma=\{w+h(w)e:w\in W\},\qquad E=W\oplus\mathbb Re,
\]

where \(h:W\to\mathbb R\) has Lipschitz constant \(L\). Write \(\ell(e)=1\), \(\ker\ell=W\), and \(P=I-e\ell\). Then a neighborhood of \(x_0\) intersects \(\Psi^{-1}(\Gamma)\) in a set contained in a Lipschitz hypersurface.

**Proof.** Set \(v=D\Psi(x_0)^{-1}e\neq0\). By (1), shrink a neighborhood of \(x_0\) so that

\[
\ell(D\Psi(x)v)\geq a>0,
\qquad\|PD\Psi(x)v\|\leq b,
\qquad m:=a-Lb>0.                                \tag{2}
\]

This is possible since the central values are respectively \(1\) and \(0\). For example take \(a=1/2\) and \(b<1/[2(L+1)]\). Shrink again so \(\Psi\) is \(K\)-Lipschitz on the neighborhood.

Choose a closed complement \(W_0\) to \(\mathbb Rv\); in a Hilbert space use \(v^\perp\). A sufficiently small product cylinder

\[
Q=\{x_0+w+tv:\|w\|<r,\ |t|<r,\ w\in W_0\}
\]

lies in this neighborhood. The product form ensures that replacing the \(w\)-coordinate or the \(t\)-coordinate of a point by that of another point in \(Q\) stays in \(Q\).

For fixed \(w\), the norm derivative of \(t\mapsto\Psi(x_0+w+tv)\) equals \(D\Psi(x_0+w+tv)v\) and is continuous by (1). The Banach-valued fundamental theorem of calculus therefore applies. For \(t>s\), (2) gives

\[
\ell\big(\Psi(x_0+w+tv)-\Psi(x_0+w+sv)\big)\geq a(t-s),
\]
\[
\|P\big(\Psi(x_0+w+tv)-\Psi(x_0+w+sv)\big)\|\leq b(t-s).
\]

Define the scalar continuous function

\[
q(w,t)=\ell(\Psi(x_0+w+tv))-h(P\Psi(x_0+w+tv)).
\]

The preceding inequalities imply strict monotonicity with a uniform lower slope:

\[
q(w,t)-q(w,s)\geq m(t-s)\quad(t>s).               \tag{3}
\]

At fixed \(t\), local Lipschitzness of \(\Psi\) gives

\[
|q(w,t)-q(\widetilde w,t)|
\leq K(\|\ell\|+L\|P\|)\|w-\widetilde w\|.       \tag{4}
\]

If \(q(w,t)=q(\widetilde w,\widetilde t)=0\), use the cross point \((w,\widetilde t)\), which remains in the cylinder, to combine (3) and (4):

\[
|t-\widetilde t|
\leq\frac{K(\|\ell\|+L\|P\|)}{m}\|w-\widetilde w\|. \tag{5}
\]

Thus there is at most one root over each \(w\), and the root coordinate is a Lipschitz function on its possibly proper domain in \(W_0\). If that domain is nonempty, extend it to all of \(W_0\) by
\(\widetilde h(w)=\inf_d[h_0(d)+C\|w-d\|]\), where \(C\) is the bound in (5). This gives the required global hypersurface containing the local preimage. If the domain is empty, there is nothing to cover. ∎

Only continuity in the single chosen direction \(v\) was used. No Fréchet derivative, operator-norm continuity, differentiability of the graph function, or differentiability of an inverse was assumed. In fact invertibility can be weakened to the existence of one direction whose image lies strictly inside a transverse cone.

## 2. Flow derivatives under strong Gâteaux regularity

Let \(F:E\to E\) be locally Lipschitz. Suppose \(DF(x)\) exists as a bounded linear norm Gâteaux derivative everywhere, \(x\mapsto DF(x)h\) is continuous for each fixed \(h\), and

\[
\sup_{\|x\|\leq R}\|DF(x)\|<\infty\qquad(R<\infty).              \tag{6}
\]

For every finite flow segment, its time map has a bounded linear Gâteaux derivative, this derivative is strongly continuous in the initial state, and the derivative is an isomorphism. The flow map is also a local bi-Lipschitz homeomorphism onto its open image.

Here is a proof that does not substitute operator-norm continuity for strong continuity.

First, (6) and strong continuity imply joint continuity of evaluation:

\[
(x,h)\longmapsto DF(x)h.                           \tag{7}
\]

Indeed, for \((x_n,h_n)\to(x,h)\), the difference is bounded by
\(K\|h_n-h\|+\|(DF(x_n)-DF(x))h\|\), which tends to zero. Integrating along a line segment gives

\[
F(y)-F(x)=\int_0^1 DF(x+s(y-x))(y-x)\,ds.          \tag{8}
\]

Consequently the field is Lipschitz on every bounded ball, with the derivative bound for that ball. For a finite reference trajectory \(u(t)=\Phi_t(x)\), nearby initial points have trajectories on the same finite interval and their trajectories converge uniformly to \(u\); the local Picard construction and its Gronwall bound give this, using finitely many existence intervals along the reference trajectory.

Put \(A(t)=DF(u(t))\). It is strongly continuous and uniformly bounded. For \(h\in E\), the equation

\[
V_h(t)=h+\int_0^t A(s)V_h(s)\,ds                 \tag{9}
\]

has a unique continuous solution. Successive integral iterates converge, because their operator bounds are dominated by \((Kt)^j/j!\); (7) gives continuity of each integrand. It is linear in \(h\), with \(\|V_h(t)\|\leq e^{Kt}\|h\|\).

For nonzero real \(\varepsilon\), let

\[
\Delta_\varepsilon(t)
=\frac{\Phi_t(x+\varepsilon h)-\Phi_t(x)}{\varepsilon}.
\]

Subtract the two nonlinear integral equations and apply (8). This yields

\[
\Delta_\varepsilon(t)=h+\int_0^t\int_0^1
A_\varepsilon(s,\tau)\Delta_\varepsilon(s)\,d\tau\,ds,
\]

where

\[
A_\varepsilon(s,\tau)
=DF\big(u(s)+\tau[\Phi_s(x+\varepsilon h)-u(s)]\big).
\]

All these operators are bounded by one \(K\). Moreover

\[
\sup_{s\in[0,T],\,\tau\in[0,1]}
\|(A_\varepsilon(s,\tau)-A(s))V_h(s)\|\longrightarrow0.          \tag{10}
\]

To verify the uniform statement, use joint continuity (7), uniform convergence of the perturbed trajectories, and compactness of
\(\{(u(s),V_h(s)):0\leq s\leq T\}\). Equivalently, a sequence contradicting (10) has a convergent subsequence of its time parameters, and (7) then forces the supposedly nonvanishing term to vanish.

Subtract (9), putting the unknown difference against the uniformly bounded \(A_\varepsilon\) and the remaining error against \(V_h\). Gronwall's inequality and (10) prove

\[
\sup_{0\leq t\leq T}\|\Delta_\varepsilon(t)-V_h(t)\|\to0.
\]

Hence \(D\Phi_t(x)h=V_h(t)\). If \(x_n\to x\), apply the same argument to the linear equations with coefficients \(DF(\Phi_s(x_n))\) and \(DF(\Phi_s(x))\). Their difference tested against the fixed reference solution \(V_h(s)\) tends uniformly to zero by (7) and the same compactness argument. Gronwall gives

\[
D\Phi_t(x_n)h\longrightarrow D\Phi_t(x)h,
\]

uniformly on the finite time interval.

The derivative is invertible. The bounded strongly continuous linear equation in (9) can also be solved backward from any terminal value. Its two-parameter evolution \(U(t,s)\) satisfies
\(U(t,s)U(s,r)=U(t,r)\) by uniqueness, and therefore
\(U(t,0)^{-1}=U(0,t)\). Both norms are at most \(e^{KT}\). This is a direct inverse construction for the derivative, requiring no inverse-function theorem.

Finally, the nonlinear reversed equation \(u'=-F(u)\) is locally well posed and locally Lipschitz in its initial value. Following a finite reference segment backward, finitely many local existence neighborhoods yield a neighborhood of the terminal point on which the backward solution exists for the entire elapsed time. Uniqueness makes this map inverse to the forward map, and Gronwall makes both maps locally Lipschitz. Their domains are open. No global backward completeness is asserted.

## 3. The exact physical closure satisfies these hypotheses

This verification uses the physical Hilbert realization in the allowed spectral report:

\[
\mathcal H=L^2_{\rm odd}(\Omega_1;\mathbb R^3)
\oplus L^2_{\rm odd}(\Omega_2)
\oplus\mathbb R^{3\times6},\qquad \theta=(v,c,M),\qquad w=g+v.
\]

The fixed carriers are probability spaces, their marks \(b_1\in\mathbb R^6\), \(b_2\in\mathbb R^3\) are bounded, and \(g\) is fixed. Set \(\phi=\tanh\) and use the notation

\[
q_i=w\cdot u_i,\quad a_i=E_1[b_1\phi(q_i)],\quad z_i=Ma_i,
\quad s_i=b_2\cdot z_i,\quad h_i=\phi(s_i),
\]
\[
f_i=E_2[ch_i],\quad\rho_i=p_i(f_i-y_i),\quad
d_i=E_2[b_2c\phi'(s_i)],\quad T_i=\rho_iM^Td_i.
\]

Here \(z_i\) is a finite upper vector, following the spectral report's notation; it is not the function-valued tanh coordinate from the earlier prompt. The exact field is

\[
F_v=-2\sum_i\phi'(q_i)(b_1\cdot T_i)u_i,\quad
F_c=-2\sum_i\rho_i h_i,\quad
F_M=-2\sum_i\rho_i d_i a_i^T.                     \tag{11}
\]

All formulas make sense on all of \(\mathcal H\). All derivatives of \(\tanh\) needed below are bounded. Bounded gates, bounded marks, and Cauchy–Schwarz show the moment maps are locally Lipschitz; subtracting the two factors in \(F_v\) then gives local Lipschitzness of (11).

### Exact derivative formula

For a direction \(\delta\theta=(\zeta,\chi,N)\), successive differentiation gives

\[
\delta a_i=E_1[b_1\phi'(q_i)(\zeta\cdot u_i)],\qquad
\delta z_i=Na_i+M\delta a_i,
\]
\[
\delta h_i=\phi'(s_i)(b_2\cdot\delta z_i),\qquad
\delta f_i=E_2[\chi h_i+c\delta h_i],\qquad
\delta\rho_i=p_i\delta f_i,
\]
\[
\delta d_i=E_2[b_2\chi\phi'(s_i)
 +b_2c\phi''(s_i)(b_2\cdot\delta z_i)],
\]
\[
\delta T_i=(\delta\rho_i)M^Td_i+\rho_iN^Td_i+\rho_iM^T\delta d_i.
\]

The field derivative is

\[
\begin{split}
DF_v(\theta)\delta\theta=-2\sum_i\big[&
\phi''(q_i)(\zeta\cdot u_i)(b_1\cdot T_i)u_i\\
&+\phi'(q_i)(b_1\cdot\delta T_i)u_i\big],
\end{split}                                                       \tag{12}
\]
\[
DF_c(\theta)\delta\theta
=-2\sum_i[(\delta\rho_i)h_i+\rho_i\delta h_i],
\]
\[
DF_M(\theta)\delta\theta
=-2\sum_i[(\delta\rho_i)d_i a_i^T
 +\rho_i(\delta d_i)a_i^T+\rho_i d_i(\delta a_i)^T].              \tag{13}
\]

These are bounded linear maps of \(\delta\theta\). The first term of (12) is a bounded multiplication operator; all remaining derivative terms have finite-dimensional range at the fixed state.

### Norm Gâteaux differentiability

The only delicate operation is the lower gate as an \(L^2\)-valued map. For a fixed \(\zeta\in L^2\), pointwise differentiation gives

\[
\frac{\phi'(q_i+\varepsilon\zeta\cdot u_i)-\phi'(q_i)}{\varepsilon}
\longrightarrow\phi''(q_i)(\zeta\cdot u_i).
\]

Its absolute value is bounded by \(\|\phi''\|_\infty|\zeta\cdot u_i|\). Dominated convergence of its squared difference gives convergence in \(L^2\). Products with the bounded marks and the convergent finite coefficients preserve this convergence.

For clarity, the finite moment map \(a_i\) has more regularity:

\[
|a_i(v+\zeta)-a_i(v)-Da_i(v)\zeta|\leq C\|\zeta\|_2^2,
\quad\|Da_i(v)-Da_i(\widetilde v)\|_{L^2\to\mathbb R^6}
\leq C\|v-\widetilde v\|_2.
\]

The first inequality follows from the scalar Taylor bound with bounded \(\phi''\); the second from Cauchy–Schwarz and the Lipschitz lower derivative gate. The upper gates depend smoothly on finite vectors as maps into \(L^\infty\), because \(b_2\) is bounded. Their pairings with \(c\) are continuous bilinear operations. These facts justify every remaining differentiation above in norm. Thus (12)–(13) are the actual norm Gâteaux derivative everywhere.

### Bounds and strong continuity

On an \(\mathcal H\)-ball of radius \(R\), the quantities \(M,c,\rho_i,d_i,T_i\) are bounded by constants depending only on \(R\), the fixed marks, directions, labels and weights. The derivative moments above satisfy corresponding bounds proportional to \(\|\delta\theta\|_{\mathcal H}\). Bounded multiplier coefficients in (12) therefore give

\[
\sup_{\|\theta\|_{\mathcal H}\leq R}
\|DF(\theta)\|_{\mathcal H\to\mathcal H}\leq C_R<\infty.         \tag{14}
\]

Now fix \(\delta\theta\) and let \(\theta_n\to\theta\) in \(\mathcal H\). All finite moments and their directional derivatives converge, by the preceding continuity estimates and continuity of the upper finite-vector operations. Also \(\phi'(q_{i,n})\to\phi'(q_i)\) in \(L^2\), so the finite-rank part of (12) converges in \(L^2\).

For its multiplier part, the required assertion is

\[
\|[\phi''(q_{i,n})-\phi''(q_i)](\zeta\cdot u_i)\|_2\to0.       \tag{15}
\]

Here is a direct truncation proof. On the set \(\{|\zeta\cdot u_i|>A\}\), the squared integral is at most
\(4\|\phi''\|_\infty^2\int_{|\zeta\cdot u_i|>A}|\zeta\cdot u_i|^2\), uniformly in \(n\), and this tends to zero as \(A\to\infty\). On its complement, the squared integral is at most
\(A^2\|\phi''(q_{i,n})-\phi''(q_i)\|_2^2\), which tends to zero for fixed \(A\), since \(\phi'''\) is bounded and \(v_n\to v\) in \(L^2\). This proves (15). Continuity of \(T_i\), (12), and (13) now give

\[
DF(\theta_n)\delta\theta\to DF(\theta)\delta\theta
\quad\text{in }\mathcal H.                       \tag{16}
\]

The formulas hold first in the unrestricted product \(L^2\) space. The odd sector in the allowed source is a closed invariant linear subspace, and the formulas preserve it; hence the derivative assertions restrict to \(\mathcal H\).

Equations (14)–(16), local Lipschitzness, and Section 2 verify the required flow properties at every finite time where the flow exists. The exact field is not asserted to be Fréchet \(C^1\) on \(\mathcal H\). Nor is the polynomial function-valued tanh-coordinate equation being extended to unrestricted \(L^2\); its products would require separate integrability hypotheses. The physical coordinates (11) avoid that problem.

## 4. Globalization and explicit probability laws

Let \(S\) be the finite bad equilibria in the allowed spectral report. Use its already constructed closed local Hilbert trapping graphs of positive finite codimension. These graphs require that report's independent-input and strict-saddle hypotheses; the present extension does not reprove the earlier landscape result.

Select countably many smaller trapping neighborhoods covering \(S\), using second countability of \(\mathcal H\), with each closure inside the corresponding larger trapping neighborhood. If an orbit converges in \(\mathcal H\) to any \(s\in S\), then it eventually stays in one of the selected larger neighborhoods, even if that neighborhood was centered at another equilibrium. Some integer-time state therefore belongs to that neighborhood's graph. The point-convergent bad basin is contained in the countable union of those graph preimages under integer-time maps.

A positive-codimension Lipschitz graph is contained in a scalar Lipschitz hypersurface: select one nonzero vector in the complementary subspace, project onto the hyperplane obtained by deleting that vector, and recover the original base coordinate using its bounded projection. The scalar coordinate is Lipschitz on its projected domain and admits the scalar extension used in Section 1. This argument does not require finite codimension, although it is finite in the application.

Sections 1–3 show that each local time-map preimage lies locally in a Lipschitz hypersurface. Second countability selects countably many such pieces. Thus the complete point-convergent basin is contained in an \(F_\sigma\) set

\[
A=\bigcup_{j\geq1}\Gamma_j
\]

of closed Lipschitz hypersurfaces in \(\mathcal H\). In particular it is meagre. This supplies the geometric step not obtainable from mere bi-Lipschitzness of the time maps.

For a fully specified probability law, choose \((e_n)\) dense in the unit sphere of \(\mathcal H\), and positive coefficients \(a_n\) with \(\sum_n a_n<\infty\). Let

\[
G=\sum_{n\geq1}a_ng_ne_n,
\]

where \(g_n\) are independent standard real normal variables. The series converges absolutely almost surely because \(\sum a_nE|g_n|<\infty\). Every continuous linear functional is Gaussian with variance \(\sum a_n^2\lambda(e_n)^2\), so this is a Gaussian law. Its support is all of \(\mathcal H\): finite coefficient choices approximate every target by density of the span, have positive probability, and the remaining tail has arbitrarily small expected norm and an independently positive chance to be small.

For any hypersurface \(\Gamma=\{w+h(w)e\}\), let \(P,\ell,L\) denote its projections and Lipschitz constant. Its transverse cone

\[
\{d:|\ell(d)|>L\|Pd\|\}
\]

contains one of the dense directions \(e_n\). Every affine line in that direction meets any translate of \(\Gamma\) at most once: two intersections would contradict its Lipschitz inequality. Conditioning on all Gaussian coordinates except \(g_n\), then using atomlessness and Fubini, proves

\[
\mathbb P(G\in x+A)=0\qquad(x\in\mathcal H).      \tag{17}
\]

Replacing \(g_n\) by independent uniforms on \([-1,1]\) gives a compactly supported probability with exactly the same property. Compactness follows from uniform convergence of the series on the compact coefficient product. This proves that \(A\) is shy, directly from the defining translation-null compact probability witness. If the basin itself is not measurably specified, (17) gives outer probability zero through its Borel hull \(A\).

### Randomization can preserve bounded fields

Let

\[
X=L^\infty_{\rm odd}(\Omega_1;\mathbb R^3)
\oplus L^\infty_{\rm odd}(\Omega_2)
\oplus\mathbb R^{3\times6}
\]

with the norm in the allowed source. It is dense in \(\mathcal H\), by truncation of square-integrable odd fields. Choose the dense Hilbert unit directions \(e_n\) from \(X\), and set the concrete positive coefficients

\[
a_n=\frac{2^{-n}}{1+\|e_n\|_X}.                  \tag{18}
\]

Then
\(\sum_n E\|a_ng_ne_n\|_X\leq E|g_1|\sum_n2^{-n}<\infty\).
Consequently the Gaussian series converges absolutely in \(X\) almost surely, while its law still has full support in \(\mathcal H\) and satisfies (17). Measurability causes no difficulty despite possible nonseparability of \(X\): the series takes values in the separable closed \(X\)-span of the countable directions, and it is also a limit of \(\mathcal H\)-valued measurable finite sums.

Thus for any prescribed bounded-field state \(\theta_*\in X\) and any \(\delta>0\), the explicit initialization \(\theta_*+\delta G\) consists of bounded fields almost surely and avoids the point-convergent finite bad basin almost surely. Positive-probability conditioning on a nonempty open Hilbert constraint preserves this nullity. A compact uniform-series witness using (18) even has bounded \(X\)-norm and can be scaled to an arbitrarily small \(X\)-norm perturbation.

No claim of full support in the nonseparable \(X\) topology is made. Nor does the construction assign new randomness to the canonical exact initialization \((v,c,M)=(0,0,D)\); it defines a different, explicitly randomized experiment around it.

## 5. Exact status and remaining limits

The directional pullback lemma and the field/flow regularity verification are proved in this report. They remove the need for Hilbert Fréchet \(C^1\) time maps when transporting the supplied local trapping graphs. The resulting global nullity uses the local Hilbert graph theorem from the allowed spectral report, including that theorem's independent-input and prior strict-saddle dependencies.

The probability conclusion is for the explicit law above and its translated/scaled versions; it is not asserted for an arbitrary possibly degenerate Gaussian or for a randomization confined to an unverified finite-dimensional slice. The fixed canonical state can still belong to a shy meagre basin. No claim is made about arbitrary nonconvergent trajectories merely approaching a continuum of equilibria, all-time compactness, or positive-loss escape without a finite equilibrium limit.

## Display-only repair record

After complete review, the lead restored the backslash in the single
convergence arrow in Section 2 (a literal tab followed by o0 had replaced
the intended LaTeX command). No mathematical statement or proof changed.
Original reviewed SHA256: `acb04b58dba1c16859cbcd6587168ae8f29a66474227b8327807252d2b7a1ca8`.
