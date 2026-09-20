# Countable bad-equilibrium basins and legitimate random initialization laws

Frozen scoped report, 2026-09-18. Scientific input scope: the supervisor's prompt only. No repository scientific source, other study, candidate proof, or numerical evidence was read. The solve-math-rigorously skill was applied. All arguments below are supplied directly; the assumed local center-stable graphs are not proved here.

## 1. State space and exact scope of the conclusion

Let

\[
E=C(K_1,\mathbb R^3)\times C(K_2,\mathbb R)\times\mathbb R^{3\times6},
\]

with any fixed product of the supremum and Euclidean norms. The compact metric mark supports make this a separable real Banach space. Write \(\Phi_t\) for the local flow of the smooth closure vector field on an open state domain \(\Omega\subseteq E\). Its time-\(t\) existence domain \(D_t\subseteq\Omega\) is open. Assume each \(\Phi_t:D_t\to E\) is a local \(C^1\) diffeomorphism.

Let \(S\) be any set of bad equilibria. It need not be countable, compact, or measurably specified. The local trapping hypothesis used here is the following precise one:

For every \(p\in S\), there are an open neighborhood \(U_p\subseteq\Omega\) of \(p\) and a local graph \(G_p\) such that every initial state whose entire forward orbit remains in \(U_p\) belongs to \(G_p\). The graph is Lipschitz over a closed complemented subspace of positive codimension, or is \(C^1\) and therefore locally of this kind.

The graph must contain *all* orbits trapped in the neighborhood, including orbits converging to other equilibria in that neighborhood. A theorem only about orbits converging to the graph's named equilibrium would not justify the countable-cover step below.

Define the convergent bad basin

\[
B_S=\{x:\Phi_t(x)\text{ exists for all }t\geq0,
\quad\Phi_t(x)\longrightarrow p\text{ for some }p\in S\}.
\]

**Conclusion.** There is an \(F_\sigma\) set \(A\subseteq E\), a countable union of closed Lipschitz hypersurfaces, with \(B_S\subseteq A\). Consequently:

1. \(B_S\) is meagre in \(E\), and relatively meagre in \(\Omega\).
2. \(A\) is shy: a compactly supported Borel probability \(\mu\), explicitly constructed below, satisfies \(\mu(a+A)=0\) for every \(a\in E\).
3. An explicit centered Gaussian probability \(\gamma\) with full support in \(E\) satisfies \(\gamma(a+A)=0\) for every \(a\in E\).

The statements about \(B_S\) can always be read as outer-probability-zero statements, or in the completed probability space, because the measurable set \(A\) contains it. Thus no hidden measurability assumption about \(S\) is required.

The result concerns trajectories converging to an equilibrium in \(S\). It does not assert convergence, and does not cover nonconvergent trajectories whose limit set merely contains bad equilibria.

## 2. Countably many neighborhoods suffice, without counting equilibria

Choose an open neighborhood \(V_p\) of each \(p\in S\) whose closure lies in \(U_p\). Every subspace of a second-countable space is second countable and Lindelöf: from a countable basis, for each basis element contained in a member of an open cover select one such member. Those selected members cover the subspace.

Apply this to \(\{V_p\cap S:p\in S\}\). Obtain a sequence \(p_j\in S\) such that \(S\subseteq\bigcup_j V_{p_j}\).

If \(\Phi_t(x)\to p\in S\), select \(j\) with \(p\in V_{p_j}\). Since \(U_{p_j}\) is open and contains \(p\), convergence gives an integer \(n\geq0\) such that

\[
\Phi_{n+t}(x)\in U_{p_j}\qquad(t\geq0).
\]

The trapping hypothesis gives \(\Phi_n(x)\in G_{p_j}\). Therefore

\[
B_S\subseteq\bigcup_{j\geq1}\bigcup_{n\geq0}
\{x\in D_n:\Phi_n(x)\in G_{p_j}\}.                 \tag{1}
\]

The limiting equilibrium need not equal \(p_j\). This is why the trapping formulation matters. The use of integer times loses nothing, because the entire sufficiently late tail remains in the selected neighborhood.

## 3. Graph geometry and backward images

A global Lipschitz hypersurface means a set

\[
\Gamma=\{w+h(w)e:w\in W\},                       \tag{2}
\]

where \(E=W\oplus\mathbb Re\), \(W\) is closed, \(e\neq0\), and \(h:W\to\mathbb R\) is Lipschitz. Let \(\ell\in E^*\) and \(P:E\to W\) be the corresponding bounded projections: \(\ell(e)=1\), \(P=I-e\ell\), \(\ker\ell=W\).

### Positive codimension graphs lie in hypersurfaces

Suppose a local graph is \(\{y+g(y):y\in D\}\), with \(E=Y\oplus U\), \(U\neq\{0\}\), and \(g:D\subseteq Y\to U\) Lipschitz. Choose \(e\in U\) and \(\lambda\in U^*\) with \(\lambda(e)=1\). Set \(W=Y\oplus\ker\lambda\). For a graph point define

\[
w=y+g(y)-\lambda(g(y))e,\qquad t=\lambda(g(y)).
\]

The original bounded projection onto \(Y\) recovers \(y\) from \(w\), so \(t\) is a well-defined Lipschitz function of \(w\) on the projected domain. If its Lipschitz constant is \(L\), its extension to all of \(W\) is

\[
\widetilde h(w)=\inf_{d\in D_W}\{h(d)+L\|w-d\|\}.
\]

For nonempty \(D_W\), the Lipschitz inequalities make this finite, show agreement on \(D_W\), and give the same Lipschitz bound. Thus the original graph is contained in a hypersurface of the form (2). This works also when \(U\) is infinite dimensional. A \(C^1\) graph is covered by countably many Lipschitz graph pieces: use bounded derivatives on sufficiently small convex balls and second countability.

### A local diffeomorphism preserves this property locally

Let \(F\) be a local \(C^1\) diffeomorphism and let \(\Gamma\) have the form (2), with Lipschitz constant \(L\). Near any point \(x_0\), put \(T=DF(x_0)\) and use coordinates \(x=x_0+T^{-1}\xi\). After translation in the range,

\[
F(x_0+T^{-1}\xi)-F(x_0)=\xi+R(\xi).
\]

On a sufficiently small convex ball, \(R\) is \(\varepsilon\)-Lipschitz, with \(\varepsilon\) as small as desired. For two points of \(F^{-1}(\Gamma)\) in this ball, write \(\xi_k=w_k+t_ke\). The defining graph equation implies

\[
|t_1-t_2|
\leq L\|w_1-w_2\|
 +(L\|P\|+\|\ell\|)\varepsilon\|\xi_1-\xi_2\|.
\]

Put \(c=(L\|P\|+\|\ell\|)\varepsilon\), choosing \(c\|e\|<1\). Since
\(\|\xi_1-\xi_2\|\leq\|w_1-w_2\|+\|e\||t_1-t_2|\),

\[
|t_1-t_2|
\leq\frac{L+c}{1-c\|e\|}\|w_1-w_2\|.            \tag{3}
\]

In particular, the local preimage is a scalar Lipschitz graph over a subset of \(W\). Extend the scalar function as above and apply the affine coordinate map \(x_0+T^{-1}\xi\). This produces a global Lipschitz hypersurface in \(E\) containing the local preimage piece.

Second countability selects countably many such local pieces. Hence the preimage under a local \(C^1\) diffeomorphism of a countable union of Lipschitz graph pieces is contained in a countable union of global Lipschitz hypersurfaces. Apply this to each pair \((j,n)\) in (1), obtaining the stated set \(A\).

Each hypersurface (2) is closed, because \(x\mapsto\ell(x)-h(Px)\) is continuous. It has empty interior: moving any graph point by a sufficiently small nonzero multiple of \(e\) leaves the graph. Thus it is nowhere dense. This proves the category conclusion.

## 4. A compactly supported witness and a full-support Gaussian law

Fix, once for the state space \(E\), a sequence \((e_k)_{k\geq1}\) dense in its unit sphere. Let \(a_k=2^{-k}\). These choices do not depend on the bad equilibria or their graphs.

### A transverse coordinate for every graph

For (2), the open cone

\[
\mathcal C_\Gamma
=\{v:|\ell(v)|>L\|Pv\|\}
\]

contains \(e\), and therefore contains some \(e_k\), after normalization. Every affine line parallel to such an \(e_k\) meets \(\Gamma\) in at most one point. Indeed, if its two parameters are \(s\neq t\), the graph's Lipschitz bound would give

\[
|s-t|\,|\ell(e_k)|\leq L|s-t|\,\|Pe_k\|,
\]

contradicting strict transversality. The same is true for every translate of \(\Gamma\).

### Compact witness for shyness

Let \(U_k\) be independent uniform variables on \([-1,1]\), and define

\[
X=\sum_{k\geq1}a_kU_ke_k,\qquad\mu=\operatorname{Law}(X).
\]

The series converges uniformly over the product \([-1,1]^{\mathbb N}\). Its sum is a continuous map from that compact product to \(E\); hence \(\mu\) has compact support.

For a fixed translated hypersurface, choose a transverse coordinate \(k\) and condition on all \(U_j\), \(j\neq k\). The remaining state varies on one affine line, which meets that hypersurface at most once. An atomless uniform variable hits the possible parameter with probability zero. Fubini's theorem gives

\[
\mu(a+\Gamma)=0\qquad(a\in E).
\]

Countable subadditivity now gives \(\mu(a+A)=0\) for every \(a\in E\). This is an explicit proof of shyness; no countable-union theorem for Haar-null sets or infinite-dimensional Lebesgue measure is being assumed. Multiplying every \(a_k\) by an arbitrary \(\delta>0\) makes the witness perturbation arbitrarily small without changing the proof.

### Concrete full-support Gaussian randomization

Let \(g_k\) be independent standard real normal variables, and define

\[
G=\sum_{k\geq1}a_kg_ke_k,\qquad\gamma=\operatorname{Law}(G).       \tag{4}
\]

Since \(\sum_k a_k\mathbb E|g_k|<\infty\), the series converges absolutely almost surely. For every \(\lambda\in E^*\),

\[
\lambda(G)\sim N\left(0,\sum_k a_k^2\lambda(e_k)^2\right),
\]

as follows by the characteristic functions of the finite sums and convergence of the displayed variance. Thus (4) defines a Banach-space Gaussian law. Its variance is positive for every nonzero \(\lambda\), because the \(e_k\) span a dense subspace.

It has full support. For any target \(x\in E\) and radius \(r>0\), first approximate \(x\) within \(r/3\) by a finite linear combination of the \(e_k\). Enlarge the truncation until the expected norm of the remaining tail is less than \(r/6\). The tail then has probability at least \(1/2\) of norm below \(r/3\), by Markov's inequality. Independently, the finitely many Gaussian coefficients have positive probability to approximate the chosen finite combination within \(r/3\). Their intersection has positive probability and puts \(G\) inside the radius-\(r\) ball about \(x\).

Conditioning on a transverse Gaussian coefficient, exactly as for the uniform witness, gives

\[
\gamma(a+A)=0\qquad(a\in E).                     \tag{5}
\]

Consequently every initialization law \(x_*+\delta G\), for deterministic \(x_*\in E\) and \(\delta>0\), avoids \(B_S\) almost surely. To retain an open admissible state region \(O\), condition this law on \(x_*+\delta G\in O\). Full support makes every nonempty open \(O\) have positive conditioning probability, and the zero-probability assertion survives conditioning. This permits, for example, strict constraints \(\|z\|_\infty<1\) whenever the intended admissible domain is open.

This assertion is explicitly nullity for the law (4), its translations, positive rescalings, and their positive-probability restrictions. It is not an assertion about every measure called Gaussian: a degenerate Gaussian supported on a hyperplane assigns that hyperplane probability one. There is no Lebesgue measure on \(E\) being used.

An optional stronger statement also has an elementary proof: every full-support Gaussian law on \(E\) that has finite second moment annihilates these hypersurfaces. For a centered such random variable \(Z\), define \(Q\lambda=\mathbb E[Z\lambda(Z)]\). The range of \(Q:E^*\to E\) is dense: an annihilating functional would have variance zero, contradicting full support. Choose \(Q\lambda\) in the open transverse cone. With \(\sigma^2=\mathbb E\lambda(Z)^2\), decompose

\[
Z=Y+vN,\quad N=\lambda(Z)/\sigma,\quad v=Q\lambda/\sigma.
\]

Every scalar linear functional of \(Y\) has zero covariance with \(N\); joint Gaussianity gives independence. Independence extends to the \(E\)-valued \(Y\), because in a separable Banach space its Borel sigma-field is generated by a countable norming family of continuous linear functionals. Conditioning on \(Y\) proves zero probability. This optional statement is not needed for (4)–(5), whose hypotheses were all checked directly.

## 5. Why the canonical initialization is not covered

The canonical infinite-width state is the fixed point

\[
x_{\mathrm{can}}=(z_0,0,D)\in E.
\]

Meagreness and shyness do not decide whether this particular point belongs to \(B_S\). In particular, the Dirac probability at that point may give \(B_S\) probability one. The construction (4) randomizes the closure functions and matrix themselves. It is an additional initialization experiment, not a reinterpretation of the deterministic canonical closure.

Randomness of particles before taking a limit is not automatically a nondegenerate random law for the limiting closure state. Likewise, randomizing only a matrix or restricting \(c=0\) is not covered merely because those random variables have densities: the entire chosen slice could lie in a graph. Such a law requires its own verified transversality or absolute-continuity argument.

Therefore the defensible inference is: **the convergent bad basin is contained in a meagre shy set and has probability zero under the explicitly stated randomization. No conclusion about the single canonical initialization follows.**

## 6. Conditional exact nonstationary trajectories approaching a collapsed saddle

This section gives an additional local construction for the supplied ODE. It does not identify the canonical state's basin.

Let \(p_*=(0,0,D)\), meaning all three \(z_i\) and \(c\) are zero and \(M=D\). Then \(a_i=v_i=H_i=d_i=0\), so \(p_*\) is an exact stationary state. Define

\[
C_1=\mathbb E_1[b_1b_1^\top],\qquad
C_2=\mathbb E_2[b_2b_2^\top],\qquad
Y=\sum_i p_i y_i u_i,\qquad
Q=\|Y\|^2DC_1D^\top.
\]

All are finite because the coordinates are bounded. Impose the explicit coupling condition

\[
C_2^{1/2}QC_2^{1/2}\text{ has a strictly positive eigenvalue }\lambda. \tag{6}
\]

Full support on the given compact supports alone does not imply (6): the coordinate spans and \(D\) can be degenerate. If \(u_i\) are linearly independent and some \(p_i y_i\neq0\), then \(Y\neq0\), but the covariance/matrix coupling still must be checked.

For a perturbation \((\zeta,h,N)\), put

\[
\eta=\mathbb E_2[b_2h],\qquad
\mathcal A\zeta=\sum_i p_i y_i D\mathbb E_1[b_1\zeta_i],\qquad
(\mathcal L\eta)_i=(u_i\cdot Y)(b_1^\top D^\top\eta).
\]

Direct differentiation of the supplied ODE at \(p_*\) gives

\[
\dot h=2b_2\cdot\mathcal A\zeta,\qquad
\dot\zeta=2\mathcal L\eta,\qquad
\dot N=0,\qquad
\mathcal A\mathcal L=Q.                          \tag{7}
\]

Choose an eigenvector \(v\) for the positive eigenvalue in (6), and set \(\eta=C_2^{1/2}v\neq0\). Then \(C_2Q\eta=\lambda\eta\). With \(\kappa=2\sqrt\lambda\), the functions

\[
h_\lambda(b_2)=\lambda^{-1}b_2\cdot Q\eta,\qquad
\zeta_\pm=\pm\lambda^{-1/2}\mathcal L\eta
\]

satisfy \(\mathbb E_2[b_2h_\lambda]=\eta\), and (7) maps
\((\zeta_\pm,h_\lambda,0)\) to \(\pm\kappa(\zeta_\pm,h_\lambda,0)\).
Thus there are explicit nonzero stable and unstable linear directions.

The stationary point is a nonglobal saddle for the squared loss. Along the fixed-matrix path \((\varepsilon\zeta_+,\varepsilon h_\lambda,D)\), Taylor expansion of \(\tanh\) on bounded coordinates gives

\[
\mathscr L(\varepsilon)-\mathscr L(0)
=-2\varepsilon^2\eta^\top\mathcal A\zeta_++O(\varepsilon^4)
=-2\varepsilon^2\lambda^{-1/2}\eta^\top Q\eta+O(\varepsilon^4)<0
\]

for sufficiently small nonzero \(\varepsilon\). Here \(\eta^\top Q\eta>0\), since \(Q\succeq0\) and \(C_2Q\eta=\lambda\eta\neq0\).

For completeness, these stable directions produce *exact nonstationary convergent trajectories*, rather than only solutions of the linearization. A short contraction argument suffices.

Write the translated exact equation as \(\dot x=Ax+R(x)\), with \(R(0)=DR(0)=0\). The operator \(A\) in (7) is finite rank. Its nonzero eigenvalues are real pairs \(\pm2\sqrt\lambda\), with \(\lambda>0\) an eigenvalue of \(C_2Q\): for a nonzero eigenvalue \(r\), the eigen-equations imply \(r^2\eta=4C_2Q\eta\), and \(\eta\neq0\). The nonzero eigenvalues of \(C_2Q\) are those of the positive semidefinite matrix \(C_2^{1/2}QC_2^{1/2}\). The remaining spectrum is zero.

A bounded finite-rank operator reduces to a finite-dimensional invariant block and a zero block: choose a finite-dimensional complement of its kernel and adjoin its range, then complement the remaining kernel. Finite-dimensional generalized eigenspaces therefore yield bounded invariant projections \(P_s,P_{cu}\), with \(P_s\neq0\), and constants such that, for suitable \(\alpha>0\) and any \(\epsilon>0\),

\[
\|e^{tA_s}\|\leq C_s e^{-\alpha t},\qquad
\|e^{-tA_{cu}}\|\leq C_{cu}e^{\epsilon t}\quad(t\geq0).
\]

Polynomial factors from possible Jordan blocks are absorbed by slightly reducing \(\alpha\) and choosing \(\epsilon>0\). Incorporate projection norms into these constants. Fix \(0<\epsilon<\beta<\alpha\). On a sufficiently small ball, \(R\) is Lipschitz with a constant \(L\) as small as desired, by continuity of \(DR\) at zero. For small \(\xi\in E_s\), seek a fixed point of

\[
\begin{split}
(\mathcal Tx)(t)={}&e^{tA_s}\xi
+\int_0^t e^{(t-s)A_s}P_sR(x(s))\,ds\\
&-\int_t^\infty e^{(t-s)A_{cu}}P_{cu}R(x(s))\,ds.
\end{split}                                                        \tag{8}
\]

On the complete space of continuous functions with norm
\(\|x\|_\beta=\sup_{t\geq0}e^{\beta t}\|x(t)\|\), the two integral operators have combined Lipschitz bound

\[
L\left(\frac{C_s}{\alpha-\beta}
+\frac{C_{cu}}{\beta-\epsilon}\right).
\]

Choose the spatial ball so this is less than \(1/2\), then choose \(\xi\) so \(C_s\|\xi\|\) is at most half the ball radius. Formula (8) maps the corresponding closed trajectory ball to itself and is a contraction. Its fixed point is differentiable by the convergent integral formula, solves the exact ODE, and satisfies \(\|x(t)\|\leq Ce^{-\beta t}\). Moreover \(P_sx(0)=\xi\), so nonzero \(\xi\) gives a nonstationary orbit converging to \(p_*\).

The same bounds, with the Lipschitz constant tending to zero as the ball shrinks, show \(x(0)=\xi+o(\|\xi\|)\). Thus taking \(\xi\) along the displayed negative eigenvector gives exact stable initial states tangent to that explicit direction. The construction remains within \(\|z\|_\infty<1\) if the ball is sufficiently small.

This establishes, under (6), the existence of nonstationary bad-basin points arbitrarily near this saddle. It is fully compatible with the basin being meagre and shy. It gives no claim that the canonical point lies on one of these trajectories.
