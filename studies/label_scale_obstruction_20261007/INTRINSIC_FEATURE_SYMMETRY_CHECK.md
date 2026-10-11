# Internal check of the intrinsic feature and symmetry routes

Status: the small-label theorem and the stated conditional mathematical lemmas pass this scoped internal check. No unconditional arbitrary-amplitude Gaussian fitting theorem is established. One wording correction is noted below. This is not a promotion review.

## Scope and provenance

The checker was the fresh scoped agent `intrinsic_feature_symmetry_check`. The complete scientific inputs were:

- `INTRINSIC_FEATURE_ROUTE.md`, SHA-256 `c74dd9b2a1ff0b9f7edd9a76320750b7570393dea89c8c30db937dbcd022a166`.
- `INTRINSIC_SYMMETRY_ROUTE.md`, SHA-256 `3122be35520a97b3aa8602e68726cb6b618d43729796c5abdfe461a04e9fc641`.
- The expressly permitted dependency, complete Sections 6 and 13 of `GAUSSIAN_POSITIVE_GEOMETRY.md`. The whole-file SHA-256 at reading was `d220fba99906085e9770aceb33b939b5d0cfa2bb2bc005909f31fe2449afa574`; the rest of that file was not read.

Required process and canonical-notation instructions, including the neural-network reference, were read. No prior verdict, other research history, other study, archived book, experiment, or external scientific source was used. The maintained-book assertions cited in symmetry Section 7 were not independently verified because those book passages are outside this assignment. Dependency Section 13 was inspected for capture normalization and scope; its independent orthogonal-population construction is not certified by this report.

The method was direct proof reconstruction: differentiate the finite model, check every normalization and bootstrap constant, prove the support statement as a Volterra equation with signed-measure memory, and make the conditional finite-width capture quantifiers explicit. The Git HEAD at the pre-write metadata check was `ef8362764b4eb8144d7af8d6f8db080fdaaf82ca`. Only this assigned report was written; the source notes were not changed.

## 1. Exact model and initialization ranks

In both notes the columns of \(X\in\mathbb R^{d\times m}\) are fixed unit inputs, and

\[
U=\tanh(AX),\quad H=\tanh(WU),\quad
f=H^\top w/n,\quad r=f-y,\quad \mathcal L=\|r\|_2^2/m.
\]

The parameter metric is

\[
\|\Delta\theta\|_{\rm par}^2
=\|\Delta A\|_F^2/n+\|\Delta W\|_F^2+\|\Delta w\|_2^2/n.
\]

The feature-route equations and all three displayed kernel blocks follow from this metric. In particular, writing \(b_a=w\odot(1-h_a^2)\) and \(c_a=(1-u_a^2)\odot W^\top b_a\), the middle block is \((b_a^\top b_b)(u_a^\top u_b)/n^2\), and the first-layer block is \((x_a^\top x_b)c_a^\top c_b/n\). Thus

\[
\dot r=-\frac2mKr,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^\top Kr
\]

has the stated factors. Each block is a Gram matrix in its corresponding parameter metric.

Both ridge-independence proofs are valid. Distinct nonantipodal unit inputs ensure that every excluded hyperplane is proper. A vector outside their finite union produces nonzero, pairwise distinct absolute projections. The feature route's unique slowest exponential then eliminates any nonzero linear dependence. The symmetry route's Taylor recurrence gives nonzero odd coefficients, and the resulting Vandermonde system gives the same conclusion. Neither proof requires \(\operatorname{rank}X=m\). In \(d=1\), the stated input restrictions allow at most one sample, so there is no exceptional multi-sample low-dimensional case hidden in the argument.

Consequently \(Q_U\succ0\). For finite \(n\ge m\), the first \(m\) sampled feature rows have a determinant that is a nonzero real-analytic function of their Gaussian roots. The given zero-set proof is sufficient: at each zero, choose a derivative of least positive order that does not vanish; a derivative of one lower order vanishes there and has nonzero gradient. Countably many derivative choices and coordinate charts cover the zero set by null hypersurfaces. Hence \(U(0)\) has column rank \(m\) almost surely. Conditional on \(U(0)\), the top Gaussian covariance is nonsingular, coordinatewise tanh gives a density on an open cube, and the same finite-rank conclusion holds for \(H(0)\).

The population limit for \(H(0)^\top H(0)/n\) correctly uses conditional concentration and covariance continuity. It does not incorrectly treat the unconditional top rows as independent. Positive density of \(N(0,Q_U)\) and the open range of coordinatewise tanh imply \(Q_H\succ0\). These are fixed-dataset statements; they assert no lower bound uniform over growing sample counts or nearly colliding inputs.

## 2. Small labels and finite stationary points

The explicit small-label theorem checks without changes. With

\[
s(t)=\frac2{\sqrt m}\int_0^t\|r(v)\|_2\,dv,
\]

the exact velocities give

\[
\|w\|_\infty\le s,\quad
\|W-W_0\|_F\le s^2/2,\quad
\frac{\|A-A_0\|_F}{\sqrt n}
\le Ms^2/2+s^4/8.
\]

For example, the final estimate integrates

\[
\frac{\|\dot A\|_F}{\sqrt n}
\le s'\|W\|_{\rm op}\frac{\|w\|_2}{\sqrt n}
\le s's(M+s^2/2).
\]

Decomposing \(WU-W_0U_0=(W-W_0)U+W_0(U-U_0)\) yields exactly the feature perturbation bound in feature equation (5). The net argument also has the correct exponent: the threshold \(\|W_0\|_{\rm op}>10\) forces a net bilinear form larger than \(5\), whose Gaussian tail is bounded by \(2e^{-25n/2}\), before the \(9^{2n}\) union bound.

The defined \(s_0\) ensures \(\|H-H_0\|_F/\sqrt n\le\sqrt\kappa/2\), hence the readout Gram is at least \(\kappa I/4\). Therefore the residual exponent is \(\kappa/(2m)\), and

\[
s(t)\le\frac{4\sqrt m\|y\|_2}{\kappa}\le s_0/2.
\]

This closes the first-exit argument with a strict margin even at the allowed nonzero label threshold. For \(y=0\), the initialized state is stationary and the assertion holds directly. Finite-time global existence follows from the same estimates and loss dissipation. The asserted all-time loss exponent \(\kappa/m\) and the high-probability event are correct. Width is taken large only for initialization; there is no interchange of width and time limits.

The stationary-point argument is also correct. When \(U\) has full column rank, a nonzero readout coordinate at a finite critical point makes \(U[r\odot(1-h_i^2)]=0\), forcing \(r=0\). Thus a nonfitting critical point has \(w=0\) and \(y\ne0\). The selected middle-row direction exists by surjectivity of \(U^\top\); its mixed second derivative with \(w_i\) is \(-2\|y\|_2^2/(mn)\). The pure middle-row second derivative is zero, so this two-dimensional Hessian restriction has negative determinant. The strict-saddle statement follows. It does not prove that the initialized flow remains in the full-rank region, converges to a finite state, or avoids a saddle from the special initialization slice.

The shrinking-Gaussian example in feature Section 5 correctly disproves uniform coercivity from finite-time full support, bounded moments, and finite transport length alone. It is explicitly not an actual training counterexample. Its use does not contradict the conditional finite-endpoint mechanism below.

## 3. Symmetry and scalar ascent

The transformation \(T_Q(A,W,w)=(AQ^{-1},W,\chi(Q)w)\) preserves the parameter metric, loss, scalar objective, and initialized law. Therefore it preserves the law of each finite prediction path. A deterministic population limit has fixed predictions under the induced action, and transitivity then gives \(f_a=\sigma_ag\). A finite Gaussian realization need not have this symmetry. A random subsequential limit need not lie on this ray pathwise.

The dihedral example is valid for odd \(k\ge3\) and \(\vartheta\notin\pi\mathbb Z/(2k)\). This excludes both cross-polygon coincidences and antipodes and implies a trivial stabilizer. The reflection character gives the specified mixed labels. The input rank is two for every such example.

There is one wording correction: symmetry Section 2 says the example lies outside “any operator-norm neighborhood” of the identity Gram. Literally this is false for a sufficiently large neighborhood. More precisely, if \(G_X=X^\top X\), the two regular polygons give \(XX^\top=kI_2\); hence the eigenvalues of \(G_X\) are \(k,k,0,\ldots,0\), and

\[
\|G_X-I_{2k}\|_{\rm op}=k-1.
\]

Thus the example is outside every identity-centered ball of radius less than \(k-1\), in particular every sufficiently small perturbative neighborhood. The precise proposed source correction is to replace “outside any operator-norm neighborhood of the \(m\times m\) identity Gram” by “outside every operator-norm ball of radius less than 1 about the \(m\times m\) identity Gram.” This wording issue does not affect the geometry or fitting implications.

The scalar-ascent equations have the correct \(1/m\) and \(1/n\) factors. Their finite-width continuation bounds are valid. The readout-linearity lemma can be checked directly without importing an unprovided proof: write \(\eta=(A,W)\), endowed with the lower-parameter metric, and \(g=\langle w,\bar h(\eta)\rangle\). Along a sufficiently regular strong ascent trajectory,

\[
w'=\bar h,\qquad
\eta'=D\bar h^*w,\qquad
\langle w,w''\rangle=\|\eta'\|_{\rm par}^2\ge0.
\]

The directional chain rule suffices here. It follows from the strong equations, the bounded activation derivatives, bounded finite-horizon readout, and bounded action of \(W\). Also \(g'=\|w'\|_2^2+\|\eta'\|_{\rm par}^2\ge0\). If \(q_0=\|\bar h(0)\|_2^2>0\), then \(w(s)\ne0\) for \(s>0\): \(g\) is positive immediately and \(d\|w\|_2^2/ds=2g\). For \(R(s)=\|w(s)\|_2\),

\[
R''(s)=\frac{\|w'\|_2^2-(R')^2+\|\eta'\|_{\rm par}^2}{R}\ge0,
\qquad R'(0+)=\sqrt{q_0}.
\]

Thus \(\|w'\|_2^2\ge q_0\), and \(g'\ge q_0\). This proves the finite scalar target bound \(s_*\le\alpha/q_0\) conditional on the constructed strong trajectory. The initialized full-rank sample covariance proves \(q_0>0\) for any of the permitted character signs.

On an identified deterministic physical population path, \(\dot s=2(\alpha-g)\) and \(\mathcal L_\infty=(\alpha-g)^2\) give the stated rate \(4q_0\). The scalar time change still requires population existence and identification; symmetry alone supplies neither. Finite scalar ascent reaching its target does not imply that a finite physical realization follows scalar ascent.

## 4. Conditional support and endpoint gap

The characteristic theorem is correct with its stated independence, measurability, causality, and integrability hypotheses. Fix a source realization for which those integrals are finite. Its drift is bounded by the displayed integrable \(M(t)\), and its difference on two paths is bounded by the displayed \(L(t)\sup_{s\le t}|p(s)-\widetilde p(s)|\). The constants \(2\) and \(3\) are valid upper bounds from the gate and memory differences.

Finite signed measures and same-time atoms cause no difficulty: a term \(R_{ac}(t,\{t\})\tanh(p(t)\cdot x_c)\) is dependence on the current state, not an implicit derivative. On each short interval, the integral equation is a contraction when the integral of \(L\) is less than one, with the already constructed past held fixed. Since \(L\in L^1[0,T]\), a finite interval partition suffices. This produces a unique absolutely continuous solution for every root and continuous dependence on that root. The assumed measurable kernels make Picard iteration measurable as well.

The displacement bound \(D_T=\int_0^T M\) is uniform over roots after conditioning on the source. The continuous root map \(F_t\) is onto by the stated Brouwer argument: its auxiliary map takes a closed finite-dimensional ball into itself. Every nonempty open set therefore has a nonempty open preimage. Independence leaves the conditional root distribution equal to its full-support Gaussian law. Integration over sources proves full support at each time, including the fixed finite scalar endpoint. Backward uniqueness, absolute continuity of the transported law, and differentiability of the root map are not required.

The deterministic nature of the response measures and the independence of the entire source path from the initial root are material assumptions. The proof does not establish them for the trained network. A bound for every fixed Euler mesh, without an integrable limiting total-variation bound, does not satisfy these hypotheses.

Given full support, the ridge argument proves \(K_U\succ0\). The middle-block inequality

\[
K_U\odot K_b\succeq
\lambda_{\min}(K_U)\operatorname{diag}(\|b_a\|_2^2)
\]

is the Schur-product Gram argument written in the source. At a finite or strong \(L^2\) state, the preactivations are finite almost surely, so \(\operatorname{sech}^2z_a>0\) almost surely. Thus \(w\ne0\) implies every \(\|b_a\|_2>0\). At \(g=\alpha>0\), \(w\ne0\) is automatic. This proves a positive endpoint gap in all sample directions without a data-rank assumption.

## 5. Capture constants and order of limits

The local continuity estimate in symmetry Section 6 is valid even when a nearby readout has no useful supremum bound. Only the reference readout requires such a bound. For a reference state with \(\|w_*\|_\infty\le S\) and \(\|W_*\|_{\rm op}\le M\), set

\[
D=1+M,\qquad B=1+S+2SD,\qquad C=(D^2+B^2)^{1/2}.
\]

Using normalized neuron norms and the Frobenius norm for the middle block, a parameter displacement \(\rho\) gives

\[
\|\Delta h_a\|_{2,n}\le D\rho,\qquad
\|\Delta(b_a\otimes u_a)\|_F\le B\rho.
\]

For the second bound, use

\[
\Delta(b_a\otimes u_a)
=(b_a-b_{*,a})\otimes u_a
+b_{*,a}\otimes(u_a-u_{*,a}),
\]

with \(\|u_a\|_{2,n}\le1\) and \(\|b_{*,a}\|_{2,n}\le S\). Consequently the combined readout-plus-middle feature operator changes by at most \(\sqrt m C\rho\). These constants do not depend on width.

For explicit conditional quantifiers, let \(\lambda_*>0\) be the deterministic least eigenvalue of the endpoint readout-plus-middle Gram. Put \(S=s_*+1\), \(M=10+S^2/2\), and

\[
\rho=\frac{\sqrt{\lambda_*}}{4\sqrt m C},
\qquad \kappa=\lambda_*/16.
\]

If a finite reference Gram is at least \(\lambda_*I/2\), its Gram stays above \(\kappa I\) throughout this radius-\(\rho\) parameter ball. This follows by subtracting \(\sqrt m C\rho\) from its least feature singular value.

Strong endpoint continuity and the physical population rate allow one fixed time \(T\) at which the population Gram is at least \(3\lambda_*I/4\) and the population residual has norm less than \(\rho\sqrt\kappa/2\). Compact-time convergence of predictions and the indicated Gram observations transfers the strictly weaker finite inequalities with probability tending to one. The same prediction convergence controls

\[
s_n(T)=\frac2{\sqrt m}\int_0^T\|r_n(t)\|_2\,dt,
\]

whose population limit is at most \(s_*<S\). Thus the exact finite bounds give the needed reference \(S,M\), on the additional high-probability Gaussian event \(\|W_0\|_{\rm op}\le10\). Uniform convergence in probability on the fixed interval is sufficient; even pointwise convergence in probability suffices for this integral because loss dissipation bounds the integrand deterministically.

After entry, the full finite kernel is at least its readout-plus-middle block. Where \(r\ne0\),

\[
\|\dot\theta\|_{\rm par}
=\frac2m\sqrt{r^\top Kr}
\le-\frac1{\sqrt\kappa}\frac d{dt}\|r\|_2.
\]

At \(r=0\), the full gradient is zero and the trajectory remains there. Hence the remaining path length is less than \(\rho\), no first exit occurs, and the exact finite loss obeys the exponent \(4\kappa/m\). This proves the conditional statement

\[
\Pr\{\lim_{t\to\infty}\mathcal L_n(t)=0\}\longrightarrow1.
\]

The width limit is used at a single fixed horizon; the later infinite interval is controlled deterministically for each finite network. A prediction limit without Gram convergence or comparable state control would not justify this conclusion.

## 6. Claim boundary

The two notes maintain the necessary distinction:

- The rank-free initialized feature result and explicit fixed small-label theorem are complete mathematical claims within the checked packet.
- The symmetry, middle-layer endpoint inequality, and conditional signed-measure support theorem are valid in their stated scopes.
- Arbitrary-amplitude fitting for the dihedral character labels remains conditional on constructing and identifying the uncut population flows, proving the limiting response representation with its total-variation control, and proving the required compact-time Gram approximation.
- Arbitrary label ratios do not follow from the character-family symmetry. No positive-probability failure of the specified Gaussian initialization is proved either.

The learned-response identity in symmetry Section 7 follows directly by integrating the rank-one equation for \(W'\) and applying its adjoint. Its finite-horizon covariance bound is also valid when the hypothesized Gaussian source exists. The further claims that the maintained fixed-program theorem supplies the indicated discrete representation remain unverified source dependencies in this scoped check. They are not used here to replace the explicitly missing continuum construction or response estimate.

No substantive mathematical correction to the checked baseline theorem or conditional implications was found. The operator-norm wording above should be tightened before treating every sentence of the route note as literally precise.

## 7. Verification of the narrow source erratum

At the supervisor's follow-up request, the corrected symmetry source was checked at SHA-256 `95db9ed7d65408d7b229cbc86f35ec944dc7f5f8b214e1c359c02f28c4193c18`. Its sole change replaces “This family lies far outside any operator-norm neighborhood of the” with “This family lies outside every operator-norm ball of radius less than 1 about the” in the identity-Gram sentence in Section 2.

This correspondence was verified without changing the source: reversing that literal replacement in the current file's output and hashing the result reproduced the original SHA-256 `3122be35520a97b3aa8602e68726cb6b618d43729796c5abdfe461a04e9fc641`. Thus no other theorem text changed. The corrected sentence follows from the calculation in Section 3 of this report, and the original mathematical check remains valid for the corrected source. The wording objection is resolved. The original hashes and finding above are retained as the record of the frozen-source check.

## 8. Limited correspondence check of the synthesis

The supervisor separately authorized reading `INTRINSIC_DIMENSION_RESULT.md` to check only its summaries of the two routes reviewed here. The reviewed summary text is present in the version with whole-file SHA-256 `5e2742affac19419de482e2e7bb831d240c7b5aec7233c9fb040de5dc858fc64`. This follow-up input was not used in the original frozen-source proof check.

The summaries preserve the claim boundary: initialization rank and the fixed small-label theorem are positive results, whereas the arbitrary-amplitude character-family route still requires the uncut population construction, the adaptive-response bound, and the prediction/Gram approximation. The support summary now explicitly retains integrable source paths and deterministic measurable signed response measures. The capture summary now explicitly requires a positive readout-plus-middle endpoint Gram together with the requisite compact-time limits. These clarifications match the hypotheses checked above; no conditional conclusion is upgraded to an unconditional fitting theorem.

This correspondence check does not review the synthesis's separate finite-time analytic-rank proposition, the geometry route, prior fitting theorems, or any later endpoint addenda. No synthesis text was edited by this checker.
