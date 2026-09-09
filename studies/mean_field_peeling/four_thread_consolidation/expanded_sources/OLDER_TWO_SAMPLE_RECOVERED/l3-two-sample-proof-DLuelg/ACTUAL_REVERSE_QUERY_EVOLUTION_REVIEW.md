# Isolated adversarial review: actual reverse-query evolution

## Verdict and provenance

**Verdict: passes within its stated, conditional scope. No required mathematical repair found.** Equations (2)--(9), the ordering of sample matrices, the signs and factors, and the cut- and width-independent finite-interval bounds are correct under the existing-trajectory premises. The Hilbert-space regularity needed for the reverse-query derivative follows from those premises and the zero-initialized readout. This review supplies the mixed-norm product argument explicitly below.

This is a verdict on an actual-trajectory identity, temporal regularity, and the propagator with its coefficient path prescribed. It is not a verdict on existence, continuation, coefficient comparison between trajectories, removal of cuts, tails, or a population limit. In particular, the separately investigated coefficient-comparison bridge is not counted as a missing part of this deliberately narrower claim.

Provenance:

- Sole mathematical source, read in full: `/tmp/l3-two-sample-proof-DLuelg/ACTUAL_REVERSE_QUERY_EVOLUTION.md`.
- Source size: 205 lines, 9,484 bytes.
- Source SHA-256: `fb9b8fb1e43f31bf16c7b08f2e079e6e5ff20fb39fd7d7a142712514df34677c`.
- The initial, pre-drafting, and post-write source hash checks agreed. The candidate was not edited.
- Procedural skill personally read in full: `/etc/codex/skills/solve-math-rigorously/SKILL.md`, 115 lines, 7,593 bytes; SHA-256 `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.
- Audit timestamp obtained before drafting: `2026-09-06T15:48:39Z`.
- No other project, history, review, or mathematical file was consulted as source material. The newly authored output was checked after writing. No agents, experiments, external mathematical sources, or searches were used. Calculations below are direct deductions from the specified source.
- Line references below refer to the source with the hash above. Hilbert spaces are understood to be real, as required by the scalar activation. In the finite-width sentence using a single `n`, all three hidden populations are understood to have the common width `n` and uniform empirical weights.

## 1. Setup, activation, cuts, and sample geometry

The activation bounds in lines 11--13 are valid:

\[
|\phi(z)|\le 1+\pi/20<7/6=a,\qquad
\phi'(z)=\frac{1}{10(1+z^2)},\qquad
\phi''(z)=-\frac{z}{5(1+z^2)^2}.
\]

Thus \(|\phi'|\le e=1/10\) and \(|\phi''|\le c=1/5\); the last bound is conservative. The functions used as gates are continuous. No derivative beyond those needed for these explicit smooth functions is being assumed about a general activation.

The eigenvalues of \(C\) are \(1+\rho\) and \(1-\rho\). Hence \(C\ge0\) and \(\|C\|=1+|\rho|\le2\) throughout the stated range, including \(\rho=-1\). No inverse of \(C\) is used in any bound. For each fixed label choice, \(Y^*=Y\) and \(\|Y\|=1\); independence of the labels is unnecessary for the conclusions.

For a smooth cut, define \(\lambda(v)=\tau(v)/v\) off zero and \(\lambda(0)=\tau'(0)\). Smoothness and \(\tau(0)=0\) make this extension continuous. The ratio assumptions give \(0\le\lambda\le1\), including at zero. Consequently \(\tau(q)=\lambda(q)q\) in \(L^2\), \(\|\tau(q)\|_2\le\|q\|_2\), and the associated multiplication operator has norm at most one. No bound on \(\tau'\), uniform or otherwise, is needed below.

The scalar Gram matrices satisfy

\[
u^T G_\ell u=\left\|u_1H^{(\ell)}_1+u_2H^{(\ell)}_2\right\|_2^2\ge0,
\qquad
\|G_\ell\|\le\operatorname{tr}G_\ell\le2a^2.
\]

They act in sample space at the next population, with an identity on that population. This typing is essential; it does not assert that sample matrices commute with sample-dependent gates.

At \(\rho=-1\), the two rows of \(C\) are negatives. Equation (1) therefore gives \((Z^{(1)}_2)'=-(Z^{(1)}_1)'\), with either choice of cuts. The stipulated relation \(Z^{(1)}_2=-Z^{(1)}_1\) is preserved. No additional symmetry of higher-layer features or queries is needed or follows from this relation.

## 2. Hilbert chain rules and the readout product

These are valid, including for bounded initial operators that are not Hilbert--Schmidt. A curve whose increments are \(C^1\) in Hilbert--Schmidt norm is \(C^1\) in operator norm because \(\|T\|_{\rm op}\le\|T\|_{\rm HS}\). Its adjoint has the corresponding operator-norm regularity. Thus bounded-operator evaluation on a \(C^1\) Hilbert curve admits the bounded-bilinear product rule.

Here is the multiplier continuity fact needed throughout. If \(z(t)\) is continuous in \(L^2\) and \(g\) is bounded and continuous, then multiplication by \(g(z(t))\) is strongly continuous on \(L^2\). Indeed, \(z(t)\to z(s)\) in probability implies convergence in probability of the gates. Their uniform bound then gives convergence in \(L^2\): for their difference \(h_t\), bounded by \(2B\),

\[
\|h_t\|_2^2\le\varepsilon^2+4B^2\mu(|h_t|>\varepsilon).
\]

For an arbitrary fixed \(f\in L^2\), split it into \(|f|\le R\) and its complement to obtain

\[
\|h_tf\|_2\le R\|h_t\|_2+2B\|f\mathbf1_{|f|>R}\|_2.
\]

First take \(t\to s\), then \(R\to\infty\). This proves the asserted strong continuity without asserting operator-norm continuity.

For a \(C^1\) curve \(z:[0,S]\to L^2\), its Bochner integral representation and Fubini give scalar absolutely continuous representatives for almost every population point. The scalar chain rule gives

\[
\phi(z(t))-\phi(z(s))
=\int_s^t\phi'(z(r))z'(r)\,dr
\quad\text{in }L^2.
\]

The integrand is continuous in \(L^2\) by the multiplier fact and \(z'\in C(L^2)\), and has norm at most \(e\|z'(r)\|_2\). Thus \(\phi(z)\) is \(C^1\), with the claimed derivative. Applying the same argument to \(\phi'\), whose derivative \(\phi''\) is bounded and continuous, gives the second chain rule used in the candidate. In particular, the forward construction successively gives \(H^{(1)},Z^{(2)},H^{(2)},Z^{(3)}\in C^1(L^2)\).

The readout equation and \(w(0)=0\) yield

\[
w(t)=\frac12\sum_b y_b\int_0^tH^{(3)}_b(r)\,dr,
\qquad
\|w(t)\|_\infty\le at,
\qquad
\|w(t)-w(s)\|_\infty\le a|t-s|.
\]

These statements follow using a common pointwise integral representative. They do not require that \(w'\) be continuous as an \(L^\infty\)-valued function. The readout bounds are available before differentiating \(\delta^{(3)}\), so there is no circular use of the reverse-query equation.

The one product differentiation worth spelling out is \(\delta^{(3)}_a=w p_a\), where \(p_a=\phi'(Z^{(3)}_a)\). It is not an application of a continuous multiplication map \(L^2\times L^2\to L^2\), since no such map exists. Instead, use

\[
\frac{w(t+h)p_a(t+h)-w(t)p_a(t)}h
=p_a(t+h)\frac{w(t+h)-w(t)}h
+w(t)\frac{p_a(t+h)-p_a(t)}h.
\]

The first term converges to \(p_a(t)w'(t)\) in \(L^2\), because the difference quotient of \(w\) converges in \(L^2\), the gates are uniformly bounded, and their multipliers are strongly continuous. The second converges because \(w(t)\in L^\infty\) and \(p_a\in C^1(L^2)\). Hence

\[
(\delta^{(3)}_a)'=\phi'(Z^{(3)}_a)w'
+w\phi''(Z^{(3)}_a)(Z^{(3)}_a)'.
\]

This derivative is continuous: use \(w\in C(L^\infty)\), the strong continuity of the \(\phi''\) multiplier, and \((Z^{(3)}_a)'\in C(L^2)\). Therefore \(\delta^{(3)}\), and then \(q^{(2)}=(\boldsymbol W^{(3)})^*\delta^{(3)}\), are \(C^1\) in their pair Hilbert spaces. This verifies the regularity needed in (4), rather than assuming it.

Continuity of the remaining cut objects does not require their differentiation. Since \(q^{(2)}\) is continuous, so are \(\Lambda_2q^{(2)}\), \(\delta^{(2)}\), and \(q^{(1)}=(\boldsymbol W^{(2)})^*\delta^{(2)}\). Both \(\Lambda_j\) are strongly continuous by the bounded continuous ratio function. This also avoids a hidden appeal to a uniformly Lipschitz cut map.

## 3. Forward derivative and ordering in A_2

With the candidate's pair notation, direct substitution gives

\[
(H^{(1)})'
=\tfrac12 P_1 C Y P_1\Lambda_1
(\boldsymbol W^{(2)})^*P_2\Lambda_2q^{(2)}.
\]

For the learned-matrix contribution,

\[
(W^{(2)})'H^{(1)}_a
=\tfrac12\sum_b y_b\delta^{(2)}_b
\langle H^{(1)}_b,H^{(1)}_a\rangle
=\tfrac12\sum_bG_{1,ab}y_b\delta^{(2)}_b.
\]

Consequently

\[
(Z^{(2)})'
=\tfrac12\big[G_1Y+\boldsymbol W^{(2)}P_1CY P_1\Lambda_1
(\boldsymbol W^{(2)})^*\big]P_2\Lambda_2q^{(2)}.
\]

The label matrix commutes with block-diagonal duplicated operators and with all the diagonal multipliers. It is moved only through those factors on its right; it is not moved through \(C\) or \(G_1\). Multiplying by \(P_2\) therefore gives precisely

\[
(H^{(2)})'=\tfrac12 A_2Yq^{(2)},\qquad
A_2=P_2\big[G_1+\boldsymbol W^{(2)}P_1CP_1\Lambda_1
(\boldsymbol W^{(2)})^*\big]P_2\Lambda_2.
\]

The placement of both cuts and the terminal \(Y\) is correct. There is no time derivative of \(P_2\): this calculation differentiates \(\phi(Z^{(2)})\) once, not its derivative.

When the cuts are identities, for every pair \(f\),

\[
\langle f,A_2f\rangle
=\langle P_2f,G_1P_2f\rangle
+\langle P_1(\boldsymbol W^{(2)})^*P_2f,
C P_1(\boldsymbol W^{(2)})^*P_2f\rangle\ge0.
\]

The two terms are self-adjoint congruences, proving the stated self-adjoint positivity. Separate sample gate values in the cuts can destroy self-adjointness; the proof appropriately does not use positivity in that case. For all cuts,

\[
\|A_2\|
\le e^2\big[2a^2+\|W^{(2)}\|_{\rm op}^2 e^2\|C\|\big]
\le2e^2\big[a^2+e^2\|W^{(2)}\|_{\rm op}^2\big].
\]

This verifies (2)--(3), including the factor two from two samples and the bound on \(C\).

## 4. Reverse-query equation: every differentiated term

The adjoint learned-matrix term in component \(a\) is

\[
((W^{(3)})')^*\delta^{(3)}_a
=\tfrac12\sum_b y_bH^{(2)}_b
\langle\delta^{(3)}_b,\delta^{(3)}_a\rangle
=\tfrac12(J_3YH^{(2)})_a.
\]

This is \(J_3Y\), not \(YJ_3\). Symmetry of \(J_3\) follows from the real inner product; it does not permit interchanging \(J_3\) with \(Y\).

Likewise,

\[
(Z^{(3)})'=\tfrac12G_2Y\delta^{(3)}
+\boldsymbol W^{(3)}(H^{(2)})',
\qquad
(\delta^{(3)})'=P_3\boldsymbol v+D_3(Z^{(3)})'.
\]

Here \(\boldsymbol v=(w',w')\); the sample sum defining \(w'\) is already included in this quantity. It must not receive another factor \(1/2\).

The product rule for \(q^{(2)}\), followed by these substitutions, gives

\[
\begin{aligned}
(q^{(2)})'={}&\tfrac12J_3YH^{(2)}
+(\boldsymbol W^{(3)})^*P_3\boldsymbol v\\
&+\tfrac12(\boldsymbol W^{(3)})^*D_3G_2Y\delta^{(3)}\\
&+\tfrac12(\boldsymbol W^{(3)})^*D_3\boldsymbol W^{(3)}A_2Yq^{(2)}.
\end{aligned}
\]

These are exactly (4)--(5). Every sign agrees with the stated ascent flow. Both learned-matrix terms and the lower forward-flow contribution carry one factor \(1/2\). There is no missing additional term from the middle cut or a middle \(\phi''\) gate, because neither \(\delta^{(2)}\) nor \(A_2\) was differentiated.

All compositions have the correct types. In particular, \(A_2,Y,K\) act on the pair at population 2, \(D_3,G_2,P_3\) act on the pair at population 3, and \(J_3\) acts in sample space on the population-2 pair \(H^{(2)}\). The adjoints map in the required reverse directions.

## 5. Finite normalized realization and the gradient wording

For common width \(n\), take \(H_\ell=\mathbb R^n\) with \(\langle u,v\rangle_n=n^{-1}u^Tv\). If a matrix represents the actual operator acting on feature vectors, its Hilbert adjoint between these equally normalized spaces is its ordinary transpose, and

\[
(v\otimes h)u=\frac1n vh^Tu,
\qquad
\|v\otimes h\|_{\rm HS}=\|v\|_n\|h\|_n.
\]

Thus the displayed hidden evolution is exactly

\[
(W^{(\ell)})'=\frac1{2n}\sum_b y_b\delta^{(\ell)}_b(H^{(\ell-1)}_b)^T,
\]

while the first-feature and readout equations retain their displayed \(1/2\) factors. There is no extra \(1/n\) in the reverse query once \(W^{(\ell)}\) denotes this operator matrix. Calling a differently scaled array the raw hidden weight would require distinguishing that array from this matrix; the source makes no raw-GD identification.

The gradient-ascent description also has a concrete normalized realization. Choose two unit input vectors

\[
x_1=(1,0),\qquad x_2=(\rho,\sqrt{1-\rho^2}),
\]

so \(x_a\cdot x_b=C_{ab}\), and let \(Z^{(1)}_a=Bx_a\). For \(-1<\rho<1\), any stipulated first-feature pair is realizable by taking the columns of \(B\) to be \(Z^{(1)}_1\) and \((Z^{(1)}_2-\rho Z^{(1)}_1)/\sqrt{1-\rho^2}\). At \(\rho=-1\), precisely the stated relation between the two features is needed; the first column \(Z^{(1)}_1\) and a zero second column give a realization.

For the uncut flow, use the objective

\[
F=\frac12\sum_a y_a\langle w,H^{(3)}_a\rangle_n,
\]

with the normalized Hilbert metric on \(w\) and the Hilbert--Schmidt metrics on the operators, including \(B:\mathbb R^2\to H_1\). Its first-operator gradient is

\[
B'=\tfrac12\sum_b y_b\delta^{(1)}_b\otimes x_b,
\qquad
\delta^{(1)}_b=\phi'(Z^{(1)}_b)q^{(1)}_b.
\]

Evaluating this equation on \(x_a\) gives exactly the first-feature equation with \(C_{ab}\). Differentiation of the same finite-dimensional objective gives the other uncut equations with the normalizations above. This also checks the ascent sign independently. In particular, the first-feature equation need not be the Euclidean gradient in an unconstrained pair of feature variables: it is the induced equation from the shared input operator.

If unequal layer widths are intended, the generic Hilbert-space formulas remain valid, but the bare-transpose convention must be changed: for an ordinary matrix \(A:\mathbb R^{n_{\rm in}}\to\mathbb R^{n_{\rm out}}\) between normalized empirical spaces,

\[
A^*=\frac{n_{\rm in}}{n_{\rm out}}A^T,
\qquad
v\otimes h=\frac1{n_{\rm in}}vh^T.
\]

The source's single-\(n\) sentence is correct under its natural common-width reading. It should not be read as asserting the same bare-transpose formula for arbitrary unequal widths or nonuniform weights.

## 6. Uniform constants and the derivative norm

The pointwise readout bound gives \(\|\delta^{(3)}_a(s)\|_2\le eas\). The rank-one norm estimate, retaining the sample factor, gives

\[
\|(W^{(3)})'(s)\|_{\rm op}
\le\|(W^{(3)})'(s)\|_{\rm HS}
\le\tfrac12\sum_b\|\delta^{(3)}_b(s)\|_2\|H^{(2)}_b(s)\|_2
\le ea^2s.
\]

Integration yields \(M_3(s)=M_{3,0}+ea^2s^2/2\). The adjoint bound and the middle-cut contraction give

\[
\|q^{(2)}_a(s)\|_2\le M_3(s)eas,
\qquad
\|\delta^{(2)}_a(s)\|_2\le M_3(s)e^2as.
\]

The identical rank-one argument at layer 2 yields

\[
\|(W^{(2)})'(s)\|_{\rm op}\le e^2a^2sM_3(s),
\]

and therefore

\[
\|W^{(2)}(s)\|_{\rm op}
\le M_{2,0}+e^2a^2\left[M_{3,0}\frac{s^2}{2}
+ea^2\frac{s^4}{8}\right]=M_2(s).
\]

This verifies the quadratic and quartic coefficients in (6). Positivity of an action, invertibility of \(C\), bounds on cut derivatives, and assumptions about independent neurons are absent from the calculation.

Put \(M_\ell=M_\ell(S)\). The reverse multiplier satisfies \(\|D_3\|\le caS\), so

\[
\|K\|\le\tfrac12M_3^2(caS)\,2e^2(a^2+e^2M_2^2)
=ce^2aS M_3^2(a^2+e^2M_2^2)=k_S.
\]

For the forcing, \(J_3\ge0\) and \(\|J_3\|\le\operatorname{tr}J_3\le2e^2a^2S^2\). The three terms in (5) are bounded, respectively, by

\[
\begin{aligned}
\tfrac12\|J_3\|\|H^{(2)}\|
&\le\sqrt2\,e^2a^3S^2,\\
M_3\|P_3\|\|\boldsymbol v\|
&\le\sqrt2\,eaM_3,\\
\tfrac12 M_3\|D_3\|\|G_2\|\|\delta^{(3)}\|
&\le\sqrt2\,ce a^4S^2M_3.
\end{aligned}
\]

Their sum is exactly \(b_S\) in (7). The factors \(\sqrt2\) arise from the ordinary product Hilbert norm, not a sample-averaged pair norm.

Finally, the direct query bound in this same pair norm is

\[
\|q^{(2)}(s)\|_2\le\sqrt2 M_3eaS.
\]

Equation (4) consequently gives

\[
\sup_{0\le s\le S}\|(q^{(2)})'(s)\|_2
\le b_S+k_S\sqrt2 M_3eaS.
\]

Thus, for any \(s,t\in[0,S]\),

\[
\|q^{(2)}(t)-q^{(2)}(s)\|_2
\le\big(b_S+k_S\sqrt2 M_3eaS\big)|t-s|.
\]

This is precisely the claimed temporal estimate. The constants depend on \(S,a,e,c\) and the initial operator-norm bounds, and are uniform over the stated labels, correlations, internal cuts, and widths. Uniformity over a family of initializations requires common bounds on their initial operator norms, as the source expressly says. No common Hilbert--Schmidt norm bound on the initial operators is needed. At \(S=0\), the displayed bounds are consistent with \(w=q^{(2)}=D_3=J_3=0\), with the potentially nonzero initial query derivative coming from the readout-forcing term.

## 7. Strong continuity, propagator, and scope

All gate multipliers are strongly continuous by the argument in section 2 of this review. For \(D_3\), combine that argument for \(\phi''\) with the established \(L^\infty\) continuity of \(w\). The operators \(W^{(\ell)}\) and their adjoints are norm continuous. The finite sample matrices \(G_\ell\) and \(J_3\) are norm continuous because their entries are inner products of continuous \(L^2\) curves. Finite products of strongly continuous operator families with uniform operator bounds are strongly continuous: split the product difference one factor at a time and apply strong continuity to each fixed limiting test vector. These facts establish strong continuity of \(A_2\) and \(K\), and continuity of \(b\) in the pair Hilbert space.

For completeness, for fixed \(r\) and a pair \(x\), set

\[
T_0(t,r)x=x,\qquad
T_{j+1}(t,r)x=\int_r^tK(s)T_j(s,r)x\,ds.
\]

The integrands are strongly continuous. Induction gives

\[
\|T_j(t,r)x\|\le\frac{[k_S(t-r)]^j}{j!}\|x\|.
\]

The sum \(U(t,r)x=\sum_{j\ge0}T_j(t,r)x\) converges uniformly, defines a bounded linear operator, and solves the integral equation. Its norm is at most \(e^{k_S(t-r)}\). A zero-initial-data difference \(d\) between two solutions satisfies, after \(j\) iterations,

\[
\|d(t)\|\le\sup_{r\le s\le t}\|d(s)\|
\frac{[k_S(t-r)]^j}{j!};
\]

taking \(j\to\infty\) proves uniqueness. Uniqueness also gives the propagator composition law. The iterated integrals and their uniform bounds give joint strong continuity in \((t,r)\), making the continuous-forcing integral well defined. Substitution in the integral equation, with the bounded integrands justifying interchange of the vector-valued time integrals, proves

\[
q^{(2)}(t)=U(t,0)q^{(2)}(0)+\int_0^tU(t,r)b(r)\,dr.
\]

Since \(w(0)=0\), \(\delta^{(3)}(0)=q^{(2)}(0)=0\). This verifies (8)--(9) using strong vector integrals, with no need for integration of \(K\) in the operator-norm Banach space.

For a fixed coefficient path, the usual forcing interpretation is consequently valid: if \(d'=Kd+f\), then

\[
\|d(t)\|\le e^{k_S(t-r)}\|d(r)\|
+\int_r^t e^{k_S(t-s)}\|f(s)\|\,ds.
\]

Both \(K\) and \(b\) are evaluated along the full actual trajectory. The displayed affine linear equation is therefore not a closed autonomous equation for the query alone; the source's fixed-trajectory qualification is essential and accurate.

Positivity of the uncut \(A_2\) does not turn this into a contraction estimate. In particular, \(\phi''(z)\) changes sign. Under the change of variables \(p=Yq^{(2)}\), the homogeneous coefficient becomes

\[
YKY=\tfrac12(\boldsymbol W^{(3)})^*(YD_3)
\boldsymbol W^{(3)}A_2,
\]

where \(YD_3\) has entries \(y_aw\phi''(Z^{(3)}_a)\), exactly as stated in lines 194--196. Their signs are not controlled by the premises.

For different trajectories, direct subtraction produces

\[
(q^{(2)}-\widetilde q^{(2)})'
=K(q^{(2)}-\widetilde q^{(2)})
+(b-\widetilde b)+(K-\widetilde K)\widetilde q^{(2)}.
\]

Uniform bounds on individual coefficients do not estimate these coefficient differences in terms of a trajectory distance. The candidate explicitly acknowledges this limitation. There is no claimed comparison bridge to repair in the present statement.

The warning about arbitrary bounded \(L^2\) operators and Gaussian tails is also correct. For example, on the probability space \((0,1)\), let \(g(x)=x^{-1/4}\) and \(Tf=\langle f,1\rangle g\). Then \(T\) is bounded on \(L^2\), while it maps the bounded input \(1\) to an output satisfying \(\int_0^1e^{\eta g(x)^2}\,dx=\infty\) for every \(\eta>0\). Thus an \(L^2\) propagator norm alone cannot supply the excluded tail statement. This is a check of the scope warning, not a counterexample to the candidate's theorem or a claim about its actual propagator.

All the estimates are conditional on an existing curve on the closed finite feature-time interval. Nothing in this review treats them as construction or continuation of that curve, identifies feature time with raw physical gradient descent, or supplies a limit theorem.

## Required repairs versus presentation suggestions

**Required mathematical repairs: none found within the stated scope.** No sign, ordering, cut-placement, normalization, constant, derivative-norm, or regularity counterexample survives the stated premises and the common-width interpretation of the finite realization.

The following are presentation suggestions, not extra hypotheses needed to make (2)--(9) true:

1. At lines 118--119, add the short mixed-norm difference-quotient argument for \((\delta^{(3)})'\), or point forward explicitly to the readout \(L^\infty\) bound. The final sentence of lines 93--102 about bounded \(C^1\) operator curves is not, by itself, the appropriate product theorem for \(w\phi'(Z^{(3)})\): the proof establishes \(w\in C^1(L^2)\cap C^{0,1}(L^\infty)\), not \(C^1(L^\infty)\). The necessary product formula nevertheless follows under exactly those established hypotheses, as proved above.
2. At lines 43--46, say explicitly “common hidden width \(n\), with operator matrices acting directly on the feature vectors.” This makes the valid transpose and \(1/(2n)\) conventions unambiguous. Unequal widths require the adjoint and tensor factors displayed in this review; that would be an extension of the finite-width sentence, not a defect in the Hilbert formulation.
3. If retaining the phrase “actual uncut gradient-ascent equations” in a standalone document, specify the normalized objective and shared first-input operator, or include the brief realization above. This explains why \(C\) appears and what metric fixes the displayed gradient normalizations.

The solve-math-rigorously procedure influenced this review by requiring explicit justification of the mixed-norm product, the strong-integral propagator construction, and the distinction between a verified conditional theorem and an unproved extension of its scope.
