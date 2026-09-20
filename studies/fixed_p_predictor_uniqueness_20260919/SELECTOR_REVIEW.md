# Informed internal cross-check of the noisy selector

2026-09-19. This is an informed internal cross-check, not an independent isolated promotion review. No candidate file was edited. The complete allowed inputs were read and their SHA-256 hashes verified:

- `MODEL_AND_GEOMETRY.md`: `d3ed7af3baadbb55e190e2423f0751b11da5ba24ef0c8fcc5c47f627ef57ff89`.
- `UNIQUE_NOISY_SELECTOR.md`: `0201209112bbe74e04f96ba35879673ac40c42629857ef6739bcd71212658c73`.
- `PASSIVE_LIMITS.md`: `957af4f8276a3a597c97d4fef63eaef749bb1cd55251490198e91a327b9619a9`.

Canonical bounded marks, the bound \(\|D\|_{\rm op}\leq2\), and \(K_{h_0}>0\) were explicit review inputs. This review does not verify the separate canonical-feature proof, inspect another route or review, or use another study.

## Verdict

The central analytic construction passes under the declared inputs. The local constants, Hilbert-space minimizer argument, full moving-feature transport, physical coercivity, domain invariance, all-time well-posedness, and deterministic common predictor limit are valid. The proof does not rely on compactness of Hilbert balls or on a supplied endpoint.

There is one scope-completeness item for the phrase “genuinely noisy” across every allowed dataset: residual tangent noise is identically zero when the merged data count is \(m=1\). The frozen candidate proves nondegeneracy explicitly only for \(m\geq2\). A simple additional positive hidden-noise choice closes this item in the supplied canonical architecture; the complete argument is given below. Without that choice, the convergence theorem still holds, but its permitted parameter range includes entirely deterministic processes.

No blocker was found in the endpoint or convergence proof. Canonical Gram positivity remains a separate prerequisite by assignment.

## 1. Regularity and local constants

The model uses the original Hilbert norms on \(w,c\) and Frobenius norm on \(M\). On the hidden ball of radius one, \(\|M\|_{\rm op}\leq3\). For normalized inputs, \(|v_w\cdot x/\sqrt2|\leq|v_w|\). Taylor's formula with \(\|\tanh''\|_\infty\leq2\) therefore bounds the remainder in the finite-dimensional map
\(a_w(x)=E[b_1\tanh(w\cdot x/\sqrt2)]\) by \(B_1\|v_w\|_2^2\). Cauchy--Schwarz bounds the difference of two derivative operators by \(2B_1\|w-\widetilde w\|_2\). This proves actual Fréchet \(C^{1,1}\) regularity of this averaged map; it does not require a twice Fréchet differentiable \(L^2\) Nemytskii map.

For \(z_h=b_2^TMa_w\), the derivative bound
\(B_1B_2(\|v_M\|+3\|v_w\|)\leq4B_1B_2\|v\|\) is valid. The stated derivative difference bound has coefficients \(1,1,6\), whose sum is eight, so \(a_2=8B_1B_2\) is a valid conservative constant. Composing with the smooth scalar activation into \(L^\infty\) gives

\[
\|DA_h\|\leq a_1,\qquad
\operatorname{Lip}(DA)\leq a_3=2a_1^2+a_2.
\]

The finite-data operator estimates use \(\sum_i\mu_i=1\), \(\|H_h(x_i)\|_2\leq1\), and Cauchy--Schwarz against the readout. In particular \(\|A_h\|\leq1\). Product differentiation of \(K=AA^*\) then gives exactly

\[
\|DK_h\|\leq2a_1,\qquad
\operatorname{Lip}(DK)\leq2a_3+2a_1^2.
\]

The radius \(r=\min\{1/2,\sigma/(8a_1)\}\) satisfies \(2r\leq1\) and
\(\|K_h-K_{h_0}\|\leq4a_1r\leq\sigma/2\) on the radius-\(2r\) ball. Thus the uniform inverse bound \(2/\sigma\) and inverse Lipschitz constant \(8a_1/\sigma^2\) are correct.

The derivative of \(J=Y^TK^{-1}Y/2\), using \(|Y|=1\), gives

\[
\|\nabla J\|\leq4a_1/\sigma^2,
\quad
\operatorname{Lip}(\nabla J)
\leq\frac{32a_1^2}{\sigma^3}
+\frac{4(a_3+a_1^2)}{\sigma^2}=C_J.
\]

Both contributions to this last expression match direct subtraction: changes in the two inverse-weighted label vectors give \(32a_1^2/\sigma^3\), and the change in \(DK\) gives the remaining term. The displayed bound
\(C_B=2a_1/\sigma+8a_1/\sigma^2\) for \(B=A^*K^{-1}\) is also valid.

The claim that \(B,P\) have bounded locally Lipschitz derivatives on this region is justified by their product and inverse formulas. For an explicit completion of the constants used in the local ODE argument, one may take

\[
\begin{aligned}
\|DB\|&\leq C_B,\\
\operatorname{Lip}(DB)&\leq C_{DB}
:=\frac{2a_3}{\sigma}
+\frac{8a_3+24a_1^2}{\sigma^2}
+\frac{64a_1^2}{\sigma^3},\\
\|DP\|&\leq C_B+a_1\sqrt{2/\sigma},\\
\operatorname{Lip}(DP)&\leq C_{DB}+2a_1C_B+a_3\sqrt{2/\sigma}.
\end{aligned}
\]

For example, if \(Q=K^{-1}\), then \(DQ=-Q(DK)Q\); subtracting its three factors bounds its derivative Lipschitz constant by
\(64a_1^2/\sigma^3+8(a_3+a_1^2)/\sigma^2\). Applying the product rule to \(B=A^*Q\) and \(P=I-BA\) gives the displayed bounds. No additional regularity assumption is needed.

## 2. Unique minimizer in the Hilbert ball

The choice
\(\rho=C_J+1+4J(h_0)/r^2\) makes
\(\omega=\rho-C_J>0\). Integrating the Lipschitz-gradient remainder for \(J\) gives the claimed \(\omega\)-strong-convexity inequality for \(F\) on the convex certified ball.

The midpoint argument is complete. If \(a\) is the infimum and \(h_n\) is a minimizing sequence, then

\[
\frac\omega8\|h_n-h_k\|^2
\leq\frac{F(h_n)+F(h_k)}2-a\longrightarrow0.
\]

Hence the sequence is strongly Cauchy. Completeness of the closed Hilbert ball, followed by continuity of \(F\), proves attainment. The same inequality proves uniqueness. This avoids an invalid inference from boundedness to strong compactness.

At radius \(r\), \(F\geq\rho r^2/2>J(h_0)\), so the minimizer is interior and has zero Fréchet gradient. The sublevel estimate
\(\|h-h_0\|\leq\sqrt{2J(h_0)/\rho}<r/\sqrt2\) is correct. Strong convexity with the stationary minimizer gives both inequalities (4) of the candidate. The gradient-dominance inequality follows by completing the square in
\(\langle\nabla F(h),h_*-h\rangle+\omega\|h_*-h\|^2/2\); no unconstrained minimization outside the ball is used.

The associated fitted state is unique: every feasible readout has the orthogonal decomposition \(c=B_hY+q\), \(q\in\ker A_h\), and therefore
\(\rho\|h-h_0\|^2/2+\|c\|^2/2=F(h)+\|q\|^2/2\). Thus the selected pair uniquely minimizes this explicit fitted-state objective within the declared hidden ball.

## 3. Tangent noise and nondegeneracy

For every Hilbert vector \(v\), the operator
\(T(v)=(\|v\|^2I-v\otimes v)/(1+\|v\|^2)\) is locally Lipschitz in operator norm. Its action annihilates the component parallel to \(v\), and multiplies the orthogonal component by \(\|v\|^2/(1+\|v\|^2)\). The two stated bounds and \(\langle v,T(v)u\rangle=0\) are therefore correct, including at zero.

Piecewise constant bounded directions with a positive refresh interval give an absolutely continuous continuous-time trajectory, with derivative identities holding almost everywhere. There are finitely many refreshes on every finite interval. This is a random ODE; no quadratic-variation correction belongs in the energy identities. The proof is deterministic for each allowed direction sequence, so its endpoint claim really holds for every such sequence.

The frozen text permits \(\nu_h=\nu_e=0\), and for \(m=1\) one always has \(T(e)=0\). Accordingly a genuinely random trajectory requires a positive amplitude and a nondegenerate direction choice. For \(m\geq2\), the candidate's signed-coordinate construction with \(\nu_e>0\) works: \(e(0)=-Y\ne0\), and at least one coordinate vector is not parallel to \(e(0)\).

Here is a complete way to cover \(m=1\) using only the allowed inputs. All merged mass is then one, so \(K_{h_0}=E_2[\tanh^2(z_0)]>0\), where \(z_0=b_2^TD a_g(x_1)\). Vary only the middle matrix in direction \(D\). Differentiation under the bounded integrand gives

\[
DK_{h_0}[(0,D)]
=2E_2[z_0\tanh(z_0)\operatorname{sech}^2(z_0)]>0.
\]

The integrand is positive whenever \(z_0\ne0\), and positive Gram implies that set has positive measure. Thus
\(DJ(h_0)[(0,D)]=-DK_{h_0}[(0,D)]/(2K_{h_0}^2)<0\), so \(G(h_0)=\nabla J(h_0)\ne0\).

Choose \(\nu_h>0\), fix two orthonormal middle-matrix directions, and draw \(U\) uniformly from their two signed pairs. Such directions exist in the declared \(3\)-by-\(5\) canonical middle matrix. For every nonzero \(G\), at least one of these directions is not parallel to \(G\), so \(T(G)U\ne0\) with positive probability. Opposite signs then give different initial velocities and different short-time paths. These are fixed matrix directions and introduce no neuron marks. Taking this hidden choice and \(\nu_e>0\) with signed readout coordinates gives a genuinely random construction for every allowed merged count \(m\geq1\).

This is a small completion of the nondegeneracy specification, not a repair to the convergence or invariance estimates. The endpoint proof remains valid for arbitrary finite nonnegative amplitudes, including the deterministic special cases.

## 4. Moving-kernel transport

The transport is correct, including its sign. Differentiating \(P^2=P\) gives \(P\dot P P=0\). For the auxiliary equation
\(\dot q=\dot Pq-\gamma q\), set \(u=(I-P)q\). Direct differentiation gives

\[
\dot u=-P\dot Pq-\gamma u=-P\dot P u-\gamma u.
\]

With initial \(u=0\), local uniqueness of this bounded linear equation gives \(u=0\). Hence \(q=Pq\), \(Aq=0\), and
\(\langle q,\dot Pq\rangle=0\). The null component therefore decays at rate \(\gamma\) while following the moving kernel.

For completeness, differentiating the physical residual in (7) yields

\[
\dot e=DA[V_h]c+A\dot c=V_e.
\]

Indeed \(DA[V_h]B+A\dot B=0\) follows from \(AB=I\), and
\(DA[V_h]q+A\dot Pq=0\) follows from \(AP=0\) and \(q=Pq\). Conversely differentiating \(Pc\) cancels \(\dot P B+P\dot B\), using \(PB=0\), and returns \(\dot q=\dot Pq-\gamma q\). Thus the physical and auxiliary systems are equivalent on their constraint manifold. At the prescribed initialization \(q=0\), uniqueness makes it identically zero.

The identities
\(\frac d{dt}|e|^2=-2\gamma|e|^2\),
\(\frac d{dt}\|q\|^2=-2\gamma\|q\|^2\), and
\(\frac d{dt}F=-\|\nabla F\|^2\)
then follow exactly. Both changing-feature transport terms are necessary to this cancellation.

## 5. Physical coercivity, continuation, and endpoint

The potential is nonnegative and has exactly the stated zero. The unknown value \(F(h_*)\) is an additive normalization used only in the proof; no algorithmic coefficient uses it.

The displayed coercivity estimate follows from
\(c-B_{h_*}Y=(B_h-B_{h_*})Y+B_he+q\). For example, in the physical product Hilbert norm an explicit admissible constant is

\[
C^2=\frac2\omega+
\left(C_B\sqrt{2/\omega}+\sqrt{2/\sigma}+1\right)^2,
\quad
\|S-S_*\|\leq C\sqrt\Phi.
\]

It is finite and fixed by the model/data/design parameters. Thus there is no collapsing metric hiding physical displacement. The potential estimate yields a noise-uniform exponential physical-state bound with exponent \(\min\{\omega,\gamma\}\).

The all-time continuation argument is sound. Before a possible domain exit, exact decrease of \(F\) traps the hidden state in the radius-\(r/\sqrt2\) ball; residual and null norms are bounded. The larger radius-\(2r\) region supplies a strict domain margin and a uniform inverse-Gram bound. The regularity constants above bound the vector field and its local Lipschitz constants on the reached sets. Bounded velocity makes a finite-time endpoint strongly Cauchy, and that endpoint remains in the open local existence domain. Local continuation therefore rules out finite maximal time. No compactness or inverse-Gram moment estimate is assumed.

The finite-travel assertion also follows: the bound
\(\|V_h\|\leq(1+\nu_h/2)(\rho+C_J)\|h-h_*\|\) is integrable, as is
\(\|V_e\|\leq(\gamma+\nu_e/2)|e|\). The readout terms are bounded respectively by
\(C_B\|V_h\|(1+|e|)\), \(\sqrt{2/\sigma}\|V_e\|\),
\(\|DP\|\|V_h\|\|q\|\), and \(\gamma\|q\|\), all integrable. The fixed-mark law interpretation is compatible with this: strong field convergence induces convergence of the marked laws under their fixed-carrier coupling. No extra evolving mark is needed when the declared noise fields are functions of existing marks or fixed matrix directions.

## 6. Predictor conclusion and distinction from original flow

The state-to-predictor estimate in `PASSIVE_LIMITS.md` follows directly from Cauchy--Schwarz and the activation Lipschitz bound, with \(\beta_j=\|b_j\|_2\). All factors are bounded on the reached state region. It applies on every bounded query-input set and hence gives uniform exponential convergence on the normalized circle and locally uniform convergence on \(\mathbb R^2\). No query mesh is needed after strong convergence to the fixed state has been proved.

Formula (15) of the selector is exactly \(\langle B_{h_*}Y,H_{h_*}(x)\rangle\), so it is the predictor of that uniquely selected physical state and fits the training labels. Its determinism follows from the unique input-defined minimizer, not from loss convergence or per-realization finite travel alone.

The passive note correctly separates these claims. Its nullspace alternatives require the stated feature independence, and its noisy comparators use explicitly prescribed nullspace forcing with frozen hidden features. They do not establish noise dependence for a canonical evolving-feature optimizer. Its contrasting assertion for pure frozen-feature sampled-gradient increments is also valid: the orthogonal readout component is invariant, and two exact-fit limits must then coincide. Nothing in those comparator claims conflicts with the selector proof.

The candidate correctly identifies the new selection objective, strong anchor, and transported readout as a changed optimizer. The original loss gradient has zero hidden velocity at zero readout and has every interpolant as a stationary point; those properties need not hold for the selector. No original-GF implicit bias, uniqueness, or small-perturbation equivalence is proved. The selected endpoint can depend on the anchoring prescription, physical norms, initialization, and data, while being independent of every allowed noise realization for those fixed choices.

## Final disposition

- Analytic selector theorem under the declared canonical bounds and positive Gram: **passes this internal cross-check**.
- Full-state transport and original-norm convergence: **passes**.
- Unique common passive predictor: **passes**, using the supplied state-continuity estimate.
- Genuine noise for all allowed data counts: **make the positive hidden/readout amplitudes and two independent hidden directions explicit; the argument above closes the \(m=1\) case**.
- Canonical positive-Gram theorem, promotion, discretization, numerical cost, and original-gradient-flow uniqueness: **not assessed or not claimed**, as specified.

## Scoped closure after the noise-specification completion

2026-09-19. The revised `UNIQUE_NOISY_SELECTOR.md` was read completely and its SHA-256 verified as `d7a7b23f41688d652145d0eb19f407d4a8c974139b904291ffcede82c421eecf`. This closure checks the added final paragraph of §3 and the opening status change. The scientific scope and other accepted inputs of the review are unchanged; no new route or source was consulted.

The added paragraph specifies strictly positive hidden and readout noise amplitudes, signed coordinate readout directions, and signed pairs of two orthonormal middle-matrix directions. For \(m\geq2\), the previously checked residual argument applies. For \(m=1\), the paragraph correctly computes the strictly positive middle-matrix scaling derivative of the scalar Gram, deduces \(\nabla J(h_0)\ne0\), and uses the two independent directions to produce distinct initial hidden velocities with positive probability. Bounded initialized preactivation justifies the differentiation, and the stated canonical matrix dimension permits two orthonormal directions. Zero-amplitude cases are correctly retained only as deterministic special cases of the convergence theorem.

The sole scope-completeness item identified above is therefore **closed for this revised hash**. The revised selector has an explicit genuinely random continuous-time state process for every allowed merged data count \(m\geq1\), while retaining the previously verified convergence to one noise-independent fitted state and predictor. This is an internal-check conclusion under the declared inputs, not a promotion approval or a verification of the separately assigned canonical positive-Gram theorem.
