# Isolated modular audit: local shifted-softplus nontriviality

Date: 2026-09-06.

Verdict: **PASS, conditional on the expressly imported local assembly and its specified common initial operators. No required correction to the candidate was found.** The argument establishes the stated one-sided local movement, raw readout-kernel change, and persistence of nonaffinity. It does not establish a global theorem or independent validity of the assembly's unprovided dependencies.

## 1. Files, exact hashes, and audit boundary

The following three mathematical files were read in full, including their internal qualifications. All paths below are relative to `/tmp/l3-two-sample-proof-DLuelg/`.

| Designation | File | Lines | SHA-256 of reviewed bytes |
| --- | --- | ---: | --- |
| N: candidate | `SOFTPLUS_LOCAL_NONTRIVIALITY.md` | 766 | `004e20c23963e2b628c84ece79e97226acc91ef70e3d0f61c554859647fe4258` |
| A: explicit dependency | `SOFTPLUS_LOCAL_POPULATION_ASSEMBLY.md` | 441 | `398d12f41a60276cbee91323293c2f64b97055eac935f45ee31b8cac6946c97d` |
| F: explicit dependency | `SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md` | 862 | `875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603` |

The actual A and F hashes agree with N's dependency table. No other mathematical source, source history, or review was opened. In particular, the primal/comparison, Gaussian-response, curvature-action, bootstrap, and standalone-proof files mentioned inside the permitted documents were not inspected. Their quoted hashes and review-status assertions were not independently verified. The rigorous-math skill was read only as procedural guidance. No experiments, numerical tests, agents, or external research were used. The three input files were not edited.

This is an audit of the implications newly asserted in N, using the following modular boundary:

* Accept A's expressly stated local construction, conditional on its unprovided dependencies: its positive local interval, prescribed common probability spaces, bounded initial operators and genuine adjoints, regular state path, raw metric, equations, and reference approximation properties.
* Use F only at a fixed finite program with its admissible instructions, polynomial-growth empirical tests, and Gaussian matrix norm control. Its stated extension to appended instructions is at F lines 128–134. Nothing here requires a width limit uniform in mesh size, number of instructions, or cap radius.
* Check that N actually connects its additional uncut products and transpose queries to those common operators; this connection is not included for free merely by accepting an abstract local path.
* Check N's stronger joint-time symmetry from the reference construction. Equality of one-time feature second moments alone would not suffice.

References of the form “N 173–205” mean line numbers in the exact candidate above. F and A are dependencies, not additional candidates whose entire historical proof chain is being certified by this report.

## 2. Required, optional, and scope findings

### Required

None. All of N's stated new conclusions follow within the specified modular boundary. In particular, no missing inverse-Gram moment assumption, arbitrary Lp bound for a population operator, L2 Fréchet differentiability claim, or unproved cancellation argument is needed.

### Optional O1: make the uniform-cap tightness quantifier explicit

At N 419–445, “tightness … uniformly in R” is valid in the sense needed for the iterated truncation limit. For each finite p and capped static tuple it can be written as

\[
 \lim_{M\to\infty}\limsup_{n\to\infty}\sup_{R\geq1}
 \mathbb P\!\left\{\|\mathcal X_n^R\|_{n,p}^p>M\right\}=0.
\]

It is also sufficient to take integer R, as in the countable reference construction. This statement bounds probabilities uniformly over fixed deterministic cap values; it does not assert tightness of the random supremum over all caps in a simultaneous coupling. N's proof supplies the former, and only the former is used. Adding this quantifier would prevent an unnecessarily stronger reading. This is a clarification, not a missing estimate or a required repair.

### Scope

The verdict applies for each fixed \(\rho\in[-1,1)\), all four sign-label vectors, and zero initial readout, on a configuration-dependent interval \([0,\varepsilon]\) contained in A's local interval. It certifies paired L2 displacement on the specified common spaces, positive motion in every hidden raw parameter block, the stated raw readout-Gram scalar expansion, and positive affine-fit error for all six scalar laws.

It does not certify positive-time Gaussianity, motion of every individual neuron, a changed marginal law for every single field merely from its paired L2 displacement, a full tangent-kernel statement, a uniform lower bound as the configuration varies, finite-width dynamical convergence, comparison with a small nonzero canonical readout, global continuation, or nonlazy behavior at every later time. None of those claims is needed or made in N's theorem.

## 3. Initial forward laws and the antiparallel geometry

**Pass: N 26–55 and 97–146.** The initial forward instructions are admissible under F: linear combinations, the globally Lipschitz activation, and independent initial matrix actions. Consequently the respective population laws are

\[
 Z_1\sim N(0,C),\qquad
 Z_2\sim N(0,\Gamma_1),\qquad
 Z_3\sim N(0,\Gamma_2),\qquad
 \Gamma_\ell=\mathbb E_\ell[H_\ell H_\ell^T].
\]

The use of uncentered feature second moments is essential and correct: those are the covariances of the next centered Gaussian forward answers. Linear growth of \(\phi\) gives all finite forward moments. Each scalar first field has variance one, even at the singular endpoint.

For \(|\rho|<1\), if \(u^T\Gamma_1u=0\), continuity and the positive two-dimensional Gaussian density imply
\(u_1\phi(z_1)+u_2\phi(z_2)=0\) everywhere. Varying each coordinate and using strict monotonicity forces \(u=0\).

For \(\rho=-1\), no density on \(\mathbb R^2\) is available for the first pair. N correctly treats this separately. With \(Z_1=(G,-G)\), the symmetric and antisymmetric eigenvalues of \(\Gamma_1\) are

\[
 \frac12\mathbb E[(\phi(G)+\phi(-G))^2]>0,
 \qquad
 \frac12\mathbb E[(\phi(G)-\phi(-G))^2]
 =\frac12\mathbb E[(G/10)^2]=\frac1{200}>0.
\]

Thus \(\Gamma_1\) is positive definite even though C is singular. The full-density argument then applies at layers two and three to give \(\Gamma_2,\Gamma_3>0\). All scalar fields used in the initial nonaffinity argument are nondegenerate Gaussians.

The squared first raw norm is \(\mathbb E[u^TC^{-1}u]\) when C is invertible; at the endpoint it is \(\mathbb E[u^2]\) for the realizable pair \((u,-u)\). N neither inverts singular C nor counts two independent first-field directions there. Frozen directions outside the input span are not mistakenly counted as moving blocks.

## 4. Exact static conditioning: both actual transposes

### 4.1 Top transpose

**Pass: N 148–205.** Let \(\mathcal F\) be the transcript consisting of the initial first fields and the complete two-column forward answers \(Z_2=W_2H_1\), \(Z_3=W_3H_2\). Conditional on this transcript, H2 and D3 are fixed. Before this static reverse query, W3 has been observed only through its forward action on H2.

For a Gaussian matrix W with entries of variance \(1/n\), conditional row projection yields

\[
 W=Z(H^TH)^{-1}H^T+\widetilde W P_{H^\perp}.
\]

Applying the transpose to D gives the mean
\(H(H^TH)^{-1}Z^TD\). With \(\Gamma_n=H^TH/n\), this is \(HB_n^T\), where \(B_n=(D^TZ/n)\Gamma_n^{-1}\). The fresh preprojection array \(\widetilde W^TD\) has independent rows of covariance \(D^TD/n\). Therefore N's exact conditional formula is

\[
 Q_{2,n}\overset d=
 H_{2,n}B_{3,n}^T+
 P_{H_{2,n}^\perp}\mathcal G_{2,n}S_{3,n}^{1/2}.
\]

Both the matrix orientation and every factor of n are correct. The covariance is the full uncentered second moment S3,n of D3, not a regression-residual covariance of D3 against Z3. The projection is in the lower neuron space. Replacing the transpose with an independent matrix, or subtracting the top response variance, would change this formula; N does neither.

The inverse is used only on the event that the empirical forward feature Gram is invertible. Its convergence to a strictly positive definite deterministic Gram makes this event have probability tending to one, with the inverse bounded in probability. No expectation of its inverse is required.

### 4.2 Lower transpose and the enlarged transcript

**Pass: N 273–313.** The second transpose is not justified merely by repeating the first formula without an independence check. N supplies the needed check.

Condition first on the initial first fields and Z2. The unobserved residual of W2 remains independent of W3, conditionally on those fields and Z2. The subsequently revealed tuple

\[
 H_2,\ Z_3,\ D_3,\ Q_2,\ D_2
\]

is a function of Z2 and W3. In particular the actual Q2 uses W3 in both orientations but does not query the remaining W2 residual. Enlarging the transcript by this tuple therefore leaves that residual unobserved, with D2 now measurable. It follows that

\[
 Q_{1,n}\overset d=
 H_{1,n}B_{2,n}^T+
 P_{H_{1,n}^\perp}\mathcal G_{1,n}S_{2,n}^{1/2},
 \qquad
 B_{2,n}=(D_{2,n}^TZ_{2,n}/n)\Gamma_{1,n}^{-1}.
\]

This is conditioning for the actual W2 transpose. The Gram inverted here is \(\Gamma_{1,n}\), not C, so the argument remains valid at \(\rho=-1\).

The eventual statements \(Q_2=B_3H_2+\eta_2\) and \(Q_1=B_2H_1+\eta_1\) identify each query jointly with its own forward population. The claimed independence is \(\eta_2\perp Z_2\) and \(\eta_1\perp Z_1\). No independence from every other generated coordinate, or empirical pairing between different populations, is required or supplied.

### 4.3 Response coefficients

**Pass: N 315–341.** For the first coefficient, differentiate the actual static expression
\(d_{3a}(z)=\frac12\sum_b y_b\phi(z_b)p(z_a)\). This gives

\[
 \partial_b d_{3a}
 =\frac{y_b}{2}p(z_b)p(z_a)
   +\mathbf1_{a=b}V_0(z)r(z_a).
\]

Gaussian integration by parts with covariance \(\Gamma_2\) produces the first line of N (18), including the derivative of V0. That term is present even when \(a\ne b\).

For the second coefficient, use the already identified joint law and hold its deterministic B3 and independent \(\eta_2\) fixed:

\[
 \partial_b\{p(z_a)[(B_3\phi(z))_a+\eta_{2a}]\}
 =\mathbf1_{a=b}r(z_a)Q_{2a}
   +p(z_a)(B_3)_{ab}p(z_b).
\]

Integration by parts now uses covariance \(\Gamma_1\). This gives the second line of (18), retaining the return through the top matrix. The coefficients selecting the law are not differentiated. Both integrands and their first derivatives have at most linear growth in the finite Gaussian arguments, so the boundary terms and integrations are justified by Gaussian moments.

## 5. Empirical tests, moments, projections, and tightness

**Pass: N 157–171, 207–270, and 294–305.** N does not apply F's instruction theorem directly to the non-Lipschitz uncut map \(V_0p(z_a)\). It first uses a continuous polynomial-growth test of the already admissible forward tuple. Since that map is continuous with linear growth, every fixed polynomial-growth test of the augmented tuple is still a permitted forward test. This supplies S3,n convergence and all finite empirical moments before the first reverse query.

For a measurable projection P of rank at most two, each row of \(P\mathcal G S^{1/2}\) is centered Gaussian of covariance \(P_{ii}S\). Hence for \(p\geq2\),

\[
 \mathbb E[\|P\mathcal G S^{1/2}\|_{n,p}^p\mid P,S]
 \leq\frac{c_p\|S\|_{\rm op}^{p/2}}n
       \sum_iP_{ii}^{p/2}
 \leq\frac{2c_p\|S\|_{\rm op}^{p/2}}n.
\]

The last inequality uses \(0\leq P_{ii}\leq1\) and \(\sum_iP_{ii}\leq2\). For smaller orders the normalized RMS bound suffices. After localizing the tight covariance S, conditional Markov gives a negligible projection in every fixed empirical Lp norm. This does not presume small leverage at every coordinate or independence of the projected rows.

With the projection dropped, the added rows are conditionally independent Gaussians with means linear in the old features. Regression coefficients converge in probability because their numerators and positive definite Gram denominators do. For a test of growth degree d, bounded-coefficient localization gives

\[
 \operatorname{Var}\!\left(
 \frac1n\sum_i T(\text{old}_i,\text{new}_i)
 \,\middle|\,\mathcal F\right)
 \leq \frac{C}{n}
      \left(1+\frac1n\sum_i|\text{old}_i|^{2d}\right).
\]

The old empirical moment is tight. Localizing it too makes conditional Chebyshev valid without assuming unconditional integrability of inverse Grams. The conditional expectation is a Gaussian-integrated continuous test. Its dependence on converging coefficients and on the covariance square root is continuous, including at a singular innovation covariance. On bounded coefficient sets its growth is uniformly polynomial. Compact-set continuity and

\[
 \frac1n\sum_i|x_i|^d\mathbf1_{|x_i|>L}
 \leq L^{d-q}\|x\|_{n,q}^q,\qquad q>d,
\]

give convergence of this conditional expectation and permit restoration of the projection. Consequently the result is convergence for all fixed continuous polynomial-growth tests, not only convergence for bounded tests or of second moments.

Applying the continuous bounded-gate map to the resulting population-two tuple gives all required D2 moments and its cross moment with Z2. The same proof then works for Q1 and D1. Reused neurons themselves are never asserted iid; independence is used only for the explicitly fresh preprojection rows. Every empirical contraction stays in the population that contains both operands.

## 6. Bridge from unbounded products to the actual common operators

**Pass: N 343–471.** This is a substantive additional step, and N proves it.

At fixed finite R, the appended capped queries are admissible instructions under F. For example,

\[
 \partial_z[p(z)\tau_R(q)]=r(z)\tau_R(q),\qquad
 \partial_q[p(z)\tau_R(q)]=p(z)\tau_R'(q)
\]

are bounded by \(2R/40\) and \(1/10\), respectively. V0 is a globally Lipschitz function of the top forward pair. Thus the static capped program uses smooth globally Lipschitz coordinate maps with bounded first derivatives, linear combinations, and the original transpose actions. It is among the programs represented by A's common operator construction (A 114–185). Integer R already suffices for the limiting argument; arbitrary fixed positive R can also be expressed using scaling of the radius-one cap.

The comparison in N (20) uses those same matrices at finite width and those same operators in population. Inserting \(\tau_R(Q_2)\) gives, for example,

\[
 \|p_2Q_2-p_2\tau_R(Q_2^R)\|_2
 \leq e\{\|Q_2-Q_2^R\|_2+T_R(Q_2)\}.
\]

The other lines follow from the cap contraction and bounded operator actions. In particular, all tail terms concern the actual uncut queries; N does not assume a tail estimate for an arbitrary vector acted on by an arbitrary L2-bounded operator.

At finite width, sign preservation, contraction, and the identity region of the cap give

\[
 T_R(X_n)^2
 \leq\frac1n\sum_i|X_{n,i}|^2\mathbf1_{|X_{n,i}|>R}
 \leq R^{2-p}\|X_n\|_{n,p}^p,\qquad p>2.
\]

Section 3 of N has already established the needed actual-query empirical moment tightness. The matrix norms are tight by F's Gaussian norm estimate (F 300–318). Localize those norms and moments first, then increase R. This gives precisely the iterated probability limit in N (22), with width sent to infinity before cap removal.

The extra claim of all-order capped moment tightness is also justified, independently of F's cap-dependent constants:

1. \(|D_{3a}^R|\leq e|V_0|\) bounds the top capped covariance and regression numerator using only forward empirical moments, uniformly in fixed R.
2. Localize the forward moments and \(\Gamma_{2,n}^{-1}\). The top conditional representation then bounds every fixed empirical moment of Q2,R, uniformly in R. The projection estimate is equally uniform under this localization.
3. \(|D_{2a}^R|\leq e|Q_{2a}^R|\) gives the middle second moment. Cauchy–Schwarz bounds the next regression numerator by the RMS norms of D2,R and Z2. Localizing these tight quantities and \(\Gamma_{1,n}^{-1}\), the lower conditional representation gives the same all-order bound for Q1,R and D1,R.

Only uniform bounds on probabilities for fixed cap choices are needed; see O1. There is no moment estimate for an inverse Gram hidden in this argument. There is also no use of a Gaussian matrix as a uniformly bounded Lp operator on arbitrary inputs.

Interpolation between empirical L2 closeness and a higher, uniformly tight empirical Lq norm proves N (23). Tail truncation and compact uniform continuity then transfer any fixed continuous polynomial-growth test. For joint second moments, N (24) is the direct Cauchy–Schwarz comparison and already suffices.

The population side is logically separate and noncircular. Define the uncut fields using A's bounded L2 operators; their L2 membership follows before their laws are known. Each fixed field has \(T_R(X)\to0\) by dominated convergence. The population version of (20) therefore gives \(\mathcal X^R\to\mathcal X\) in L2 on the actual common spaces. For any bounded Lipschitz test, use the triangle inequality between the finite uncut tuple, finite capped tuple, population capped tuple, and population uncut tuple. The finite uncut tuple's explicit law was already proved by direct static conditioning, and at fixed R the capped tuple has F's limit. Sending n to infinity and then R to infinity identifies the actual population tuple's law with the explicit static law.

This law identification also identifies all finite moments because the explicit laws have them. Joint second moments additionally pass directly through (24) and its population counterpart. Thus N's Gaussian innovations and response formulas apply to \(A_3^*D_3\) and \(A_2^*D_2\) themselves, rather than to a separately constructed scalar model.

## 7. Positivity and all hidden raw parameter blocks

**Pass: N 473–542.** The argument treats the two label modes and the singular first geometry correctly.

For any vector u,

\[
 u^TS_3u=\mathbb E[V_0^2(u_1p(Z_{31})+u_2p(Z_{32}))^2].
\]

For equal labels, \(|V_0|\geq1\). For opposite labels, strict monotonicity of \(\phi\) makes its zero set exactly the diagonal \(Z_{31}=Z_{32}\), a null set under the positive two-dimensional Gaussian density. Thus a zero quadratic form would force \(u_1p(z_1)+u_2p(z_2)=0\) everywhere, by continuity. Since p is strictly increasing, varying the coordinates separately forces \(u=0\). Hence S3 is positive definite.

Using the identified actual query law,

\[
 \operatorname{Cov}(D_2\mid Z_2)
 =\operatorname{diag}(p_2)S_3\operatorname{diag}(p_2)>0.
\]

The gates are strictly positive, although not uniformly bounded below. For each fixed nonzero direction its conditional variance is positive almost surely, and its expectation is positive and finite. This proves S2 positive definite. Repeating at the lower query gives

\[
 \operatorname{Cov}(D_1\mid Z_1)
 =\operatorname{diag}(p_1)S_2\operatorname{diag}(p_1)>0,
\]

including for the singular first pair \((G,-G)\).

The Hilbert–Schmidt tensor pairing is a product of within-population inner products. Consequently

\[
 \|v_3\|_{\rm HS}^2=\tfrac14\operatorname{tr}(\Gamma_2YS_3Y)>0,
 \qquad
 \|v_2\|_{\rm HS}^2=\tfrac14\operatorname{tr}(\Gamma_1YS_2Y)>0.
\]

Conjugation by the diagonal sign matrix Y preserves positive definiteness, and the trace of a product of two positive definite matrices is positive. No cross-population random-variable pairing is involved.

For the first sample b, row \(c_b\) of C is nonzero since its diagonal entry is one. Therefore

\[
 \operatorname{Var}((v_1)_b\mid Z_1)
 =\tfrac14 c_bY\operatorname{diag}(p_1)S_2
               \operatorname{diag}(p_1)Yc_b^T>0.
\]

This proves that both first-field components have positive L2 norm. At \(\rho=-1\) they are negatives of each other, with reduced scalar velocity
\((y_1D_{11}-y_2D_{12})/2\); its variance is still strictly positive. A's input-span estimate gives finiteness of the raw first norm and bounds each sample's L2 norm by it. Hence all three raw blocks have nonzero v, with the prescribed first metric.

## 8. C1 path to one-sided second-order jets

**Pass: N 544–615.** The regularity accepted from A is enough. N does not require a twice differentiable vector field or an L2 Fréchet derivative of the nonlinear feature map.

The multiplication fact used throughout is valid: if \(X_s\to X\) in L2, \(b_s\to b\) in probability, and all multipliers are uniformly bounded, then

\[
 b_sX_s-bX=b_s(X_s-X)+(b_s-b)X\longrightarrow0
 \quad\text{in L2}.
\]

The first term is bounded by the multiplier bound times \(\|X_s-X\|_2\). For the second, truncate the fixed L2 field X; on the bounded portion bounded convergence in probability gives L2 convergence, and the tail is uniformly small. A higher moment of X is unnecessary.

The readout equation and initial zero readout give

\[
 \frac{W^{(4)}(s)}s
 =\frac1s\int_0^s\frac12\sum_a y_aH^{(3)}_a(t)\,dt
 \longrightarrow V_0\quad\text{in L2}.
\]

Multiply by the bounded top gate, apply the actual trained adjoint, and repeat through the lower gates and adjoint. The trained operators converge in operator norm because their HS increments converge. This gives exactly N (31), \(\delta_\ell(s)/s\to D_\ell\) and \(q_j(s)/s\to Q_j\).

The tensor map from L2 times L2 to HS is continuous. Substitution into the parameter equations therefore gives \(\theta'_{\rm hidden}(s)/s\to v\) in the raw norm. Integrating a remainder \(t\,o(1)\) gives

\[
 \theta_{\rm hidden}(s)-\theta_{\rm hidden}(0)
 =\tfrac12s^2v+o_{\rm raw}(s^2).
\]

The curvewise chain rule is also justified. For a C1 L2 curve Z, the feature difference quotient equals

\[
 \left(\int_0^1p(Z(t)+u[Z(t+h)-Z(t)])\,du\right)
 \frac{Z(t+h)-Z(t)}h.
\]

Its multiplier is bounded and converges in probability to \(p(Z(t))\). The multiplication fact proves derivative \(p(Z(t))Z'(t)\) in L2, and the same fact proves continuity of that derivative. Starting with the first field, the ordinary bounded bilinear operator-field product rule then makes the next preactivation C1, allowing this argument to be repeated. There is no circular assertion that every forward field is already differentiable.

Dividing these product rules by s gives the full recursion

\[
 \begin{aligned}
 J_{1a}&=(v_1)_a, &F_{1a}&=p_{1a}J_{1a},\\
 J_{2a}&=v_2H_{1a}+A_2F_{1a}, &F_{2a}&=p_{2a}J_{2a},\\
 J_{3a}&=v_3H_{2a}+A_3F_{2a}, &F_{3a}&=p_{3a}J_{3a}.
 \end{aligned}
\]

Both the changing parameter and changing input feature contribute at each hidden matrix. Integrating proves all preactivation and feature expansions with coefficient \(s^2/2\). The second derivative notation denotes the one-sided strong derivative of the first derivative at zero; it does not assert C2 regularity at positive times.

## 9. Every layer and sample moves: cancellation and joint-time symmetry

**Pass: N 617–693.** Nonzero v2 or v3 alone would not exclude cancellation between the two terms defining J2 or J3. N supplies the missing type of argument through exact pairings and symmetry.

For the first layer, with \(b=YD_1/2\),

\[
 \tfrac12\sum_a y_a\mathbb E[D_{1a}J_{1a}]
 =\mathbb E[b^TCb]=\|v_1\|_{\rm first}^2.
\]

At \(\rho=-1\), writing \(j=(y_1D_{11}-y_2D_{12})/2\) makes the same left side \(\mathbb E[j^2]\), with no factor of two from the redundant pair.

In the middle-layer pairing, the direct v2 term is \(\|v_2\|_{\rm HS}^2\). Moving A2 to its genuine adjoint turns the other term into the first-layer pairing because \(A_2^*D_{2a}=Q_{1a}\) and \(p_{1a}Q_{1a}=D_{1a}\). Repeating at the top yields

\[
 \tfrac12\sum_a y_a\mathbb E_\ell[D_{\ell a}J_{\ell a}]
 =\sum_{j\leq\ell}\|v_j\|_{\rm raw,j}^2>0,
 \qquad\ell=1,2,3.
\]

All products appear in finite inner products; N does not declare a product of two arbitrary L2 fields to lie in L2. Each positive sum rules out simultaneous vanishing of the two J fields in that layer.

For individual samples, let \(\sigma=y_1y_2\). At finite width, exchange the initial first fields while keeping the initial matrices fixed. The input law is invariant, even for \(\rho=-1\). The reference equations transform forward fields by sample exchange, readout by multiplication by \(\sigma\), and reverse fields by both operations. The identities \(y_{3-a}=\sigma y_a\) and simultaneous-exchange invariance of C preserve the hidden updates. Oddness of the three caps preserves the reverse transformation. This induction holds for time zero and any finite list of reference times together.

F provides the joint finite-program law, not just separate one-time laws. At fixed cap, A's mesh convergence is in the common state spaces and gives the corresponding L2 convergence for recomputed fields (A 241–251). A's cap removal and forward convergence are on these same spaces (A 293–336). Consequently the reference symmetry passes to the pair of fields at zero and any fixed local time s:

\[
 (Z^{(\ell)}_1(0),Z^{(\ell)}_1(s))
 \overset d=(Z^{(\ell)}_2(0),Z^{(\ell)}_2(s)).
\]

This extension uses stated approximation properties of the accepted assembly, without an additional global or uniqueness argument. It is stronger than equality of \(\mathbb E[H_a(s)^2]\). In particular it gives equality of displacement norms on the fixed coupling. Dividing by \(s^2/2\) and using the strong jet limits gives \(\|J_{\ell1}\|_2=\|J_{\ell2}\|_2\). Combining with the positive pairing makes each norm strictly positive. The first-layer conclusion also follows directly from its conditional variance.

Finally, \(p_{\ell a}>0\) almost surely implies \(F_{\ell a}=p_{\ell a}J_{\ell a}\ne0\) whenever \(J_{\ell a}\ne0\); a uniform positive lower gate bound is not necessary. This establishes the two strictly positive displacement limits for every one of the six preactivations and six corresponding features. Their finite number allows a common positive local interval for nonzero displacement.

## 10. Raw readout kernel and sample factors

**Pass: N 695–725.** Define \(V_3(s)=\frac12\sum_a y_aH^{(3)}_a(s)\). Then

\[
 \kappa_y(s)=\tfrac14y^TK^{\rm ro}(s)y=\|V_3(s)\|_2^2,
 \qquad
 V_3(s)=V_0+\tfrac12s^2L+o_{L^2}(s^2),
 \quad L=\tfrac12\sum_a y_aF_{3a}.
\]

The last positive pairing gives

\[
 \langle V_0,L\rangle
 =\tfrac12\sum_a y_a\mathbb E[D_{3a}J_{3a}]
 =\|v\|_{\rm hiddenraw}^2.
\]

Expanding the squared norm produces a cross term
\(2(s^2/2)\langle V_0,L\rangle\). The squared increment is of order \(s^4\), and the remaining cross term is \(o(s^2)\). Thus

\[
 \kappa_y(s)-\kappa_y(0)
 =s^2\|v\|_{\rm hiddenraw}^2+o(s^2).
\]

The coefficient in N (3) is correct. Initial positivity is \(y^T\Gamma_3y/4>0\). With equal diagonal entries under sample symmetry, y is an eigenvector of the raw readout Gram, and its eigenvalue is

\[
 \lambda_y=K^{\rm ro}_{11}+\sigma K^{\rm ro}_{12}
 =2\kappa_y.
\]

Its leading change is consequently \(2s^2\|v\|_{\rm hiddenraw}^2\), as stated. This calculation concerns the defined readout Gram, not a claim about the full network tangent kernel.

The notation \(DV_3v\) is legitimate for the bounded linear first-variation recursion used here. An arbitrary raw tangent passes through bounded gates, bounded initial operators, and HS actions on fixed L2 features. The needed path expansion has already been established by the curvewise argument. No neighborhood-wide Fréchet differentiability follows or is used.

## 11. Affine-fit error and the final local interval

**Pass: N 727–766.** For a real L2 field Z of positive variance, both Z and \(\phi(Z)\) are in L2. Minimizing over the intercept first and then the slope gives an attained minimum

\[
 \mathcal A(Z)=\operatorname{Var}(\phi(Z))
 -\frac{\operatorname{Cov}(Z,\phi(Z))^2}
        {\operatorname{Var}(Z)}.
\]

At every initial scalar Gaussian field, a zero minimum would mean \(\phi(Z)=\alpha+\beta Z\) almost surely. Positive scalar Gaussian density and continuity would make this identity hold on all of \(\mathbb R\), contradicting \(\phi''>0\). Thus each of the six initial errors is strictly positive; the joint singularity at the first antiparallel pair is irrelevant to this scalar argument.

If \(Z_m\to Z\) in L2, Lipschitzness gives \(\phi(Z_m)\to\phi(Z)\) in L2. Means and second moments converge. For the cross moment, for example,

\[
 |\mathbb E[Z_m\phi(Z_m)]-\mathbb E[Z\phi(Z)]|
 \leq\|Z_m-Z\|_2\|\phi(Z_m)\|_2
    +\|Z\|_2\|\phi(Z_m)-\phi(Z)\|_2\to0.
\]

The denominator stays bounded away from zero near each initial field. Therefore the displayed affine-fit formula is continuous there. Along each local curve, both its variance and its error stay at least half their initial positive values after shrinking the interval. This requires neither a positive-time support theorem nor positive-time Gaussianity.

The movement limits, kernel expansion, and the six variance/error continuities each hold in a neighborhood of zero. Their finite intersection, with the endpoint decreased if necessary and bounded by S*, supplies the single \(\varepsilon(\rho,y)>0\) asserted by N. There is no inference beyond that interval.

## 12. Disposition

Required changes: none. Optional clarification: O1 only. The candidate's newly added argument is valid as a conditional local theorem with the hashes and scope stated above. This review does not promote any unprovided dependency, earlier review assertion, or global continuation claim to an independently established result.
