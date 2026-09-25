# First-principles route: invariant observables, interaction matrices, and the closure obstruction

Status: theory-only scoped route; exact conditional identities and counterexamples, not an established closure for the Gaussian-initialized network. No experiments or external sources were used. The scientific input was the supervisor's canonical network and gradient-flow equations. This note does not use another study's findings.

The target is an autonomous, restartable description with finitely many current coordinates per neuron and principled current aggregate interactions. Its dimension may depend on accuracy and horizon; independence from training-sample count is an additional requirement, not a consequence of finite rank on a fixed dataset. No coefficient may be supplied by the future target trajectory.

The main conclusion is that current Gram matrices determine interaction coefficients only after a generator-closure identity has been established. A low-rank covariance does not establish that identity. A particularly transparent sufficient condition gives an exact aggregate matrix equation, but it preserves fixed neuron-label subspaces and is very restrictive for an actual Gaussian coupling operator.

## 1. Exact memory actions and the interaction quantities they require

Write the data expectation as \(\int\cdot\,d\nu(a,y)\), and \(r_t(a,y)=f_t(a)-y\). The neuron-label spaces are \(\mathcal H_\ell=L^2(\Omega_\ell,\mu_\ell)\), with the actual adjoint relative to these inner products. All calculations assume the displayed expectations are finite and differentiation under them is justified, for example by absolute continuity in the relevant \(L^2\) spaces and integrable bounds. No time analyticity is assumed.

The exact middle-layer update is
\[
 W_2(t)=W_{20}-2\int_0^t\int r_s(a,y)
       \Delta_2(s,a)\otimes H_1(s,a)\,d\nu\,ds.
\]
Consequently
\[
\begin{aligned}
 Z_2(t,x)&=W_{20}H_1(t,x)
 -2\int_0^t\int r_s(a,y)\Delta_2(s,a)C_1(s,a;t,x)\,d\nu\,ds,\\
 Q(t,x)&=W_{20}^{*}\Delta_2(t,x)
 -2\int_0^t\int r_s(a,y)H_1(s,a)C_2(s,a;t,x)\,d\nu\,ds,
\end{aligned}
\]
where
\[
C_1(s,a;t,x)=\langle H_1(s,a),H_1(t,x)\rangle_1,
\qquad
C_2(s,a;t,x)=\langle\Delta_2(s,a),\Delta_2(t,x)\rangle_2.
\]
These two formulas require both time-dependent correlations and both directions of the same initial operator. Replacing the backward action by an independently sampled operator changes the canonical system.

Current covariance equations already display the next interaction statistics. Put \(g_\ell=1-H_\ell^2\) and \(k(a,x)=a\cdot x/d\). Then
\[
\dot H_1(x)=-2g_1(x)\int r(a,y)g_1(a)Q(a)k(a,x)\,d\nu,
\]
and hence
\[
\mathbb E_1[\dot H_1(x)H_1(b)]
=-2\int r(a,y)k(a,x)
 \mathbb E_1[H_1(b)g_1(x)g_1(a)Q(a)]\,d\nu.
\]
The right side is a response-weighted higher interaction, not a function of the covariance of \(H_1\) without an additional identity. Likewise,
\[
\begin{aligned}
\dot Z_2(x)&=-2\int r(a,y)\Delta_2(a)C_1(t,a;t,x)\,d\nu
                  +W_2\dot H_1(x),\\
\dot\Delta_2(x)&=-2g_2(x)\int r(a,y)H_2(a)\,d\nu
                  -2cH_2(x)g_2(x)\dot Z_2(x).
\end{aligned}
\]
Thus differentiating \(C_2\) introduces mixed moments involving \(c,H_2,\Delta_2\) and the forward action on \(\dot H_1\). A proposed closure must retain these contractions or prove how they reduce to its chosen state.

## 2. A sufficient finite transport assumption and its exact coupling equation

Let \(\Phi_\ell(t,\omega_\ell)\in\mathbb R^{k_\ell}\) be finite observable vectors and define
\[
T_\ell(t)v=\Phi_\ell(t,\cdot)^Tv,
\qquad G_\ell(t)=T_\ell(t)^*T_\ell(t)
=\mathbb E_\ell[\Phi_\ell\Phi_\ell^T].
\]
Assume the following on a fixed horizon.

1. **Observable representation.** There are coefficient vectors \(h(t,x)\in\mathbb R^{k_1}\), \(d(t,x)\in\mathbb R^{k_2}\) such that \(H_1(t,x)=T_1(t)h(t,x)\) and \(\Delta_2(t,x)=T_2(t)d(t,x)\) for all required inputs. The Grams are positive definite.
2. **Actual generator invariance.** Along the actual population evolution,
   \[
   \dot\Phi_\ell=A_\ell(S_t)\Phi_\ell,
   \]
   where \(S_t\) is the specified current reduced state and the functions \(A_\ell\) have a source-computable formula. Their time dependence is locally integrable. This is an identity about the actual velocity, not a regression fit to a trajectory.
3. **Both initial-operator actions close.** Initially,
   \[
   W_{20}\operatorname{ran}T_1(0)\subseteq\operatorname{ran}T_2(0),
   \qquad
   W_{20}^*\operatorname{ran}T_2(0)\subseteq\operatorname{ran}T_1(0).
   \]
4. **For a full autonomous network closure, an additional condition is needed.** The local parameters, residual, coefficient decoders \(h,d\), and any other components of \(S_t\) must have closed current-state equations derived from the original gradient flow. Their representation must not hide an arbitrary input function, the dense trajectory, or the full uncompressed operator. Conditions 1–3 alone close the displayed operator actions, not the remaining population dynamics.

If \(R_\ell(t,s)\) solves \(\partial_tR_\ell=A_\ell(S_t)R_\ell\), \(R_\ell(s,s)=I\), then
\[
\Phi_\ell(t)=R_\ell(t,s)\Phi_\ell(s),
\qquad
T_\ell(t)=T_\ell(s)R_\ell(t,s)^T.
\]
The fundamental matrix is invertible: its inverse solves \(\partial_tR^{-1}=-R^{-1}A_\ell\). Therefore \(\operatorname{ran}T_\ell(t)\) is the same fixed label-space subspace at every time. In particular, assumption 3 persists. This is why finite linear transport is a fixed dictionary in changing coordinates; calling it a moving basis does not weaken that condition.

Define the current aggregate matrix \(K(t)\in\mathbb R^{k_2\times k_1}\) by
\[
W_2(t)T_1(t)=T_2(t)K(t).
\]
It exists because every learned rank-one increment maps the first active subspace into the second. Differentiating this equality, using \(\dot T_\ell=T_\ell A_\ell^T\), gives
\[
\boxed{
\dot K=-A_2^TK+KA_1^T
          -2\left(\int r(t,a,y)d(t,a)h(t,a)^T\,d\nu\right)G_1.
}
\]
Indeed, \(\dot W_2T_1=-2T_2\bigl(\int rdh^T\,d\nu\bigr)G_1\); comparing it with the derivative of \(T_2K\) proves the equation. The initial matrix is obtained from the actual source operator,
\[
K(0)=G_2(0)^{-1}T_2(0)^*W_{20}T_1(0).
\]
The adjoint formula is
\[
W_2(t)^*T_2(t)=T_1(t)G_1(t)^{-1}K(t)^TG_2(t).
\]
To verify it, pair either side with \(T_1v\) and use \(\langle T_2Kv,T_2w\rangle=v^TK^TG_2w\). Equality, rather than only equality of projections, uses the backward-invariance assumption.

The exact current actions are therefore
\[
Z_2(t,x)=T_2(t)K(t)h(t,x),\qquad
Q(t,x)=T_1(t)G_1(t)^{-1}K(t)^TG_2(t)d(t,x),
\]
and
\[
\dot G_\ell=A_\ell G_\ell+G_\ell A_\ell^T.
\]
The same \(K\), with the two Gram metrics, governs both directions. Its forcing is precisely the gradient-flow contraction \(\int rdh^T\,d\nu\). Thus the aggregate interaction is derived, not selected or learned independently.

For completeness, the two-time Gram is
\[
\mathbb E_\ell[\Phi_\ell(s)\Phi_\ell(t)^T]
=G_\ell(s)R_\ell(t,s)^T.
\]
This yields both memory covariances, but the \(K\)-equation eliminates the need to store them. The retained state uses \(k_\ell\) coordinates per neuron plus matrices of sizes \(k_\ell^2\) and \(k_1k_2\), in addition to the explicitly declared local and aggregate variables in condition 4.

## 3. Why the Gram formula does not by itself obtain a closed coefficient law

For any differentiable observable vector with invertible Gram, define
\[
\widehat A=\mathbb E[\dot\Phi\Phi^T]G^{-1},
\qquad
\eta=\dot\Phi-\widehat A\Phi.
\]
Then \(\mathbb E[\eta\Phi^T]=0\). This is an exact least-squares projection identity. It does not prove either of the two facts needed for closure:

- that \(\eta=0\), or a quantitatively small residual in a norm controlling subsequent interaction;
- that the numerator is computable from the retained current state without access to the unresolved velocity.

A two-dimensional label-space example exposes the first gap. Let \(e_1,e_2\) be orthonormal random variables and take the one-coordinate observable
\[
\Phi_t=\cos(t)e_1+\sin(t)e_2.
\]
Then \(G(t)=1\), \(\mathbb E[\dot\Phi_t\Phi_t]=0\), and \(\widehat A(t)=0\) at every time. Nevertheless \(\dot\Phi_t\ne0\), and the two-time covariance is \(\cos(t-s)\), not the constant predicted by \(\dot\Phi=0\). The absent orthogonal velocity is exactly the source of the error.

The second gap occurs even for a scalar population with \(\dot z=z^2\). For \(\Phi=z\), the Gram formula needs \(\mathbb E z^3\), whereas \(G=\mathbb E z^2\). The laws
\[
\tfrac12\delta_{-1}+\tfrac12\delta_1,
\qquad
\tfrac13\delta_{\sqrt2}+\tfrac23\delta_{-1/\sqrt2}
\]
both have mean zero and second moment one. Their third moments are respectively zero and \(1/\sqrt2\). Thus even the mean and Gram together do not determine \(\widehat A\) or \(\dot G\). The network formulas in section 1 identify the corresponding unresolved mixed moments for the canonical gradient flow.

The formula becomes constructive only when the original generator gives an identity such as
\[
(\nabla\Phi)v=A(M)\Phi
\]
with \(M\) itself governed by closed current moment equations, or when a controlled approximation to this identity is proved. It is then legitimate to use the Gram formula as a derivation or verification of the already closed coefficient expression. A lower bound on the Gram eigenvalues is needed for stable approximate use.

## 4. An exact general criterion: constancy of the projected velocity on fibers

Let \(X\) denote the full population state, \(\dot X=V(X)\), and let \(P(X)\) be a prescribed differentiable current-state summary. On a forward-invariant admissible set, an autonomous equation \(\dot s=F(s)\) represents \(s=P(X)\) for every allowed initial state if and only if
\[
DP(X)V(X)=F(P(X)).
\]
Equivalently, the projected velocity must agree for any two allowed full states having the same summary. Necessity is obtained by differentiating at the initial time. Sufficiency is the chain rule, together with uniqueness for the reduced equation. Target observables additionally need a decoder from \(P(X)\).

This is a criterion, not a claim that a useful \(P\) has been found. It exposes exactly what current moment equations must prove. If the state retains probability laws of finite local neuron coordinates, the same principle applies to their transport equations; a finite number of coordinates per neuron does not mean that the population law itself is a finite vector.

Linear invariant dictionaries are a strong sufficient way to satisfy this criterion. Nonlinear finite realizations may satisfy it without finite covariance rank. Failure of a linear dictionary is therefore not a no-go theorem for all small present-state descriptions.

## 5. Equal-time covariance rank does not control predictive response rank

A scalar retained variable can have arbitrarily high-dimensional hidden response. For example, eliminate \(N\) coordinates from
\[
\dot x=\sum_{j=1}^N b_jz_j+u,
\qquad
\dot z_j=c_jx-\lambda_jz_j.
\]
The resulting equation for \(x\) has memory kernel
\[
K(t,s)=\sum_{j=1}^N b_jc_j e^{-\lambda_j(t-s)},\qquad t\ge s.
\]
For distinct \(\lambda_j\) and nonzero \(b_jc_j\), these exponentials are linearly independent: differentiating a proposed linear dependence at one time yields a Vandermonde system with nonzero determinant. A fixed time cut gives a past-to-future map of rank \(N\). The equal-time covariance of \(x\) is still a scalar.

An actual closed differentiable state \(s\in\mathbb R^q\), by contrast, has linear response
\[
R(t,s)=C(t)U(t,s)B(s),\qquad \partial_tU=DF(s_t)U.
\]
Across any fixed cut, this factors through \(\mathbb R^q\). This is finite predictive or separation rank. It should not be confused with finite rank of the entire causal integral operator, whose triangular support can give infinite operator rank even for a one-dimensional state.

Low predictive rank of both correlation and response can therefore support a finite realization assumption. It does not supply its coefficient law, source initialization, innovations, or stability. Those are separate obligations.

## 6. Smooth finite Gaussian Markov states cannot create continuing innovations

Here is a precise obstruction to an exact finite *smooth Gaussian* Markov lift. Let \(Z_t\in\mathbb R^q\) be centered, Gaussian, mean-square differentiable, with nonsingular covariance \(G(t)\) throughout the interval. Assume the needed derivatives and inverse covariances are locally bounded or integrable. Its Markov covariance identity is
\[
C(t,s)=C(t,u)G(u)^{-1}C(u,s),\qquad t\ge u\ge s.
\]
Define
\[
A(t)=\mathbb E[\dot Z_tZ_t^T]G(t)^{-1},
\qquad T(t,s)=C(t,s)G(s)^{-1}.
\]
Mean-square differentiability gives
\[
\dot G=AG+GA^T.
\]
The Markov identity gives \(T(t+h,s)=T(t+h,t)T(t,s)\). Since
\(T(t+h,t)=I+hA(t)+o(h)\), it follows that \(\partial_tT=A(t)T\).

The Gaussian conditional covariance
\[
V(t\mid s)=G(t)-T(t,s)G(s)T(t,s)^T
\]
therefore obeys
\[
\partial_tV=AV+VA^T,\qquad V(s\mid s)=0.
\]
Multiplying by inverse fundamental matrices shows that the only solution is zero. Hence \(Z_t=T(t,s)Z_s\) in \(L^2\). All future randomness is a linear image of the \(q\) current Gaussian coordinates; the full covariance kernel on the interval has rank at most \(q\).

Equivalently, the innovation covariance rate \(\dot G-AG-GA^T\) is zero. Nonanalytic but integrable coefficient functions do not change this conclusion. A finite linear Gaussian realization with nonzero continuing innovations requires a state that is not mean-square differentiable, or a violation of another stated hypothesis.

The nonsingularity qualification matters. Independent Gaussian coefficients multiplying smooth bumps on disjoint intervals, with zero variance between intervals, give a scalar smooth Gaussian Markov process that can reset its randomness repeatedly. Such a process has singular covariance at the reset times and lies outside the theorem. The theorem also does not rule out nonlinear finite states with non-Gaussian laws, whose observed covariance can have infinite rank, or a rough latent state producing smoother observed coordinates.

## 7. Why exact fixed active subspaces are restrictive for the canonical operator

In a finite-width model, suppose \(W_{20}\) is an \(n_2\times n_1\) matrix, \(n_2\ge n_1\), and a pair of subspaces closes under both \(W_{20}\) and \(W_{20}^*\). Then the first subspace is invariant under \(W_{20}^*W_{20}\).

If this positive matrix has distinct eigenvalues and an active vector \(h_0\) has a nonzero component in every eigenvector, the vectors
\[
h_0,(W_{20}^*W_{20})h_0,\ldots,(W_{20}^*W_{20})^{n_1-1}h_0
\]
are linearly independent, again by the Vandermonde determinant in the eigenbasis. Every invariant first-layer subspace containing \(h_0\) is then the whole \(n_1\)-dimensional space. These nondegeneracy properties are generic for a Gaussian matrix and an independently generic active vector. Thus the exact two-sided invariant-subspace route can require width-sized state. This is a witness obstruction, not an impossibility result for approximate or nonlinear realizations.

There is a second possible obstruction if the first-layer initialization has a continuous nondegenerate weight component and inputs vary along an interval. Distinct positive scalings give linearly independent functions \(w\mapsto\tanh(x_jw)\): an identically zero finite combination first has coefficient sum zero by \(w\to+\infty\), then multiplication by the exponential corresponding to the smallest \(x_j\) forces its coefficient to vanish; induction completes the proof. Equality almost everywhere under a full-support continuous law extends to equality everywhere by continuity. Hence \(H_1(0,x)\) can already have infinite label-space span. This observation is conditional on that initialization and input class; those details were not supplied in the scoped prompt.

Even where exact nonlinear closure of a fixed function dictionary is sought, asking a finite-dimensional space to contain constants and remain closed under every pointwise product is restrictive: it is an algebra of functions on a finite measurable partition. To see this, powers of each member are linearly dependent, so that member takes finitely many values almost everywhere; a finite basis induces a common finite partition. This is a finite-neuron-type structure, not a generic continuous population law.

## 8. What a non-vacuous approximate hierarchy would need

An appropriate conditional hierarchy hypothesis is about the **actual projected velocity**, not arbitrary history filters. For each order \(n\), prescribe finite current coordinates and source-computable equations before seeing the future trajectory. Let the actual retained coordinates satisfy
\[
\dot s_n(t)=F_n(s_n(t))+e_n(t),\qquad
\|e_n(t)\|\le\varepsilon_n,
\]
and let the desired actual observable differ from its retained decoder \(D_n(s_n(t))\) by at most \(\delta_n\). Require these estimates uniformly over the specified problem class and horizon. In the present network, the defect must include omitted generator terms, both initial-operator action errors, and response-weighted mixed interactions from section 1.

If \(F_n\) is Lipschitz with constant \(L_n\) on the relevant tube, the reduced solution \(\dot{\hat s}_n=F_n(\hat s_n)\) has the same initial retained state, and \(D_n\) is Lipschitz with constant \(M_n\), then
\[
\sup_{t\le T}\|D_n(\hat s_n(t))-O(X_t)\|
\le \delta_n+M_n\varepsilon_nT e^{L_nT}.
\]
Indeed, the state difference is bounded by \(\int_0^t(L_n\|s_n-\hat s_n\|+\varepsilon_n)\,du\); multiplying the scalar differential bound by \(e^{-L_nt}\) yields the displayed estimate. Uniformly small raw covariance tails alone do not control \(\varepsilon_n\), and \(\varepsilon_n\to0\) alone is insufficient if the response amplification grows too quickly.

For a hierarchy independent of sample count \(m\), its coordinate dictionary and dimension bounds must be fixed on the allowed input domain independently of the chosen sample. Evaluating data expectations by an \(m\)-term sum is compatible with that requirement. Retaining an \(m\)-component activation vector per neuron is not. At a single time and on a fixed dataset, rank at most \(m\) is automatic and says nothing about sample-independent compression or the time-generated span.

## 9. Claim ledger and remaining bottleneck

| Claim | Status | Exact missing bridge |
|---|---|---|
| Learned middle-layer memory has the two correlation-weighted actions in section 1 | Exact under stated integrability | None |
| Finite invariant observable spaces with two-sided initial-operator closure yield the current \(K,G_1,G_2\) equations | Proved conditional identity | Actual satisfaction and remaining local closure |
| \(\mathbb E[\dot\Phi\Phi^T]G^{-1}\) supplies an autonomous coefficient law by itself | False | Orthogonal velocity and unresolved moments survive |
| Equal-time covariance rank bounds predictive-response rank | False | Hidden response can have arbitrary rank |
| A nonsingular, mean-square differentiable finite Gaussian Markov state can sustain new innovations | False | Innovation rate is identically zero |
| Exact fixed active subspaces remain small for generic Gaussian couplings | Disfavored by the explicit finite-width cyclic-subspace obstruction | Another realization or a controlled approximation is required |
| The canonical population admits a sample-independent approximate current-state hierarchy | Open | Source-computable projected-generator/response closure with a vanishing controlled defect |

The decisive next mathematical obligation is to exhibit a particular source-defined current observable dictionary for the actual global population evolution and bound its omitted generator and response terms. A small current Gram matrix, a fitted transition matrix, or finite rank established after observing the trajectory does not meet that obligation.
