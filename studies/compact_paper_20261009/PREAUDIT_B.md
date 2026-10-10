# Independent preaudit B

Date: 2026-10-09. Review type: isolated adversarial proof audit of the frozen compact manuscript. The assignment's single-report format takes precedence over the review skill's general multi-artifact template.

## Verdict

**PASS on the supplied proof, with the verification limits below.** I found no concrete fatal, major, or minor mathematical flaw after reading all five assigned files and reconstructing the critical probability, stability, endpoint, and storage arguments. The headline is supported as an eventual, fixed-problem, exact-real-coordinate existence theorem. This is an independent mathematical audit, not machine verification or verification of a numerical implementation.

In particular, I did not find an unstated dense-trajectory input to the initializer, an illicit complex-Gram positivity argument, a confidence-dependent label cap, or a missing fitted-endpoint step. The very large possible width threshold and preprocessing cost are expressly excluded from the theorem's efficiency claims.

No repair is required by this audit. No scientific finding from another study, prior manuscript, prior review, or another reviewer was accessed.

## Frozen inputs and complete reading coverage

The following SHA-256 hashes identify the reviewed inputs. I read every line, including all proofs, definitions, displayed constants, and theorem assembly. The source TeX was the proof input; I did not use the optional PDF.

| File | Lines read | SHA-256 |
| --- | ---: | --- |
| `paper/compact.tex` | 1–257 | `64327f17c0a47b08a349890d274960b9732c8d650b2730e02a4d44d3e88fa6f9` |
| `paper/compact_fitting.tex` | 1–213 | `4cb10d4534f95ca5dbc9a957aac536c55a7268e0dc7128c105102de5bd195235` |
| `paper/compact_foundations.tex` | 1–1377 | `8de151e32734ee2c9116a91a1cccb7c5ecee7ec1369ff4784e88fb4d79a6148a` |
| `paper/compact_legendre.tex` | 1–699 | `45c40b7e6c1c1b501d6f2643a226ac2ca4a00a91e3d9704502ed54fadf4fe238` |
| `paper/compact_selected.tex` | 1–1007 | `12b2d33bf7732172d454cf3a2d74a4b322f027a74474d8747f3da9ef85b96c11` |

Required process inputs read completely: `solve-math-rigorously/SKILL.md`; `explain-with-canonical-notation/SKILL.md` and `references/neural-response-memory.md`; `review-ai-paper/SKILL.md` and its severity rubric. The scientific input scope was precisely the five files above. I did not read study administration, the established book, other studies, manuscript history, author notes, or supplementary code. No literature or empirical experiments were added.

## Claim and dependency assessment

Here \(\lambda=\gamma/m\), \(Y=\|y\|_2/\sqrt m>0\), \(S=16Y/\lambda\), and \(\ell=\log(en)\), as in the manuscript. All problem parameters are fixed as \(n\) increases.

| Claim | Argument verdict | Plausibility | Controlling dependencies |
| --- | --- | --- | --- |
| Global dense fitting, finite residual activity, and uniform-query endpoint tails | Sound within checked scope | Highly plausible | Initial Gram gap; small labels; mobility-coordinate energy identity |
| Uniform analytic sources and all-time training carriers | Sound within checked scope; the most technically demanding component | Plausible | Independent cavity stops; adaptive-control nets; trace absorption; fixed-order moment removal; domain continuation |
| Legendre all-time approximation with the displayed moving-state count | Sound within checked scope | Highly plausible conditional on the common source event | Order-independent closure fitting; projection identities; signed parameter comparison; all-time dense carrier bound |
| Harmonic and Logarithmic error \(Y/n\), including the fitted endpoint | Sound within checked scope | Highly plausible conditional on the source events | Exact source metric; independently fitting selected dynamics; readout-feedback cancellation; finite initialized jets; source dimensions |
| Error negligible relative to actual independent dense variability | Sound within checked scope | Highly plausible conditional on the analytic source event | Final-layer innovation; conditional scalar limit; analytic derivative-to-trajectory estimate; union-bound assembly |

The source argument is indispensable for all three relative-error conclusions: it supplies the training-carrier bound used by Legendre, the analytic bases used by the selected models, and the complex neighborhood used to turn initial derivative variability into positive-time variability. Its failure could not be treated as an ancillary issue. I found no demonstrated failure there.

## Adversarial checks and results

### 1. Normalizations, real fitting, and singular intermediate covariances

I reconstructed the mobility-coordinate calculation rather than identifying the flow with an unscaled Euclidean gradient. With physical parameter coordinates

\[
 (W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n),
\]

the loss is \(\rho^2=\|r\|_2^2/m\), and its gradient flow satisfies
\(-\partial_t\rho^2=\|\dot\theta\|_{\mathrm{par}}^2\). The stopped top-feature Gram \(\mathsf H^\top\mathsf H/(mn)\succeq\lambda I/4\) gives the readout contribution \(\|\dot\theta\|_{\mathrm{par}}^2\ge\lambda\rho^2\). Cauchy–Schwarz with factors \(\|\dot\theta\|/\sqrt\rho\) and \(\sqrt\rho\) yields the asserted length \(2\rho(t)/\sqrt\lambda\). This proves parameter convergence as well as residual convergence; neither is inferred merely from decreasing loss.

The initialization induction permits a singular \(Q^{(j)}\): continuity of the positive-semidefinite square root and Gaussian polynomial domination suffice. No inversion of an intermediate covariance is used. Uniform sphere control follows from a finite net and the operator event. Uniform initial cavity control uses the small RMS deletion error instead of union-bounding weak Gram convergence over all deletion sets. The latter is a necessary distinction and is present.

Locations: `compact_fitting.tex:71–177`; `compact_foundations.tex:907–932`.

### 2. Adaptive Gaussian arguments and independent stopping

I tried the following attacks on the cavity argument: conditioning an omitted root on full-network survival; substituting adaptive controls before a Gaussian estimate; dropping nonzero same-root quadratic means; assuming independence of the sample processes; and using a moment order that covertly tightens the label condition.

The supplied construction addresses each one. The reference cavity and its stopped extensions depend only on retained initialization. Linear and quadratic Gaussian estimates are proved uniformly over deterministic control histories before the actual controls are substituted. The same-root traces are retained explicitly in the four-term display at `compact_foundations.tex:711–718`; they are not declared centered. Sample RMS estimates use Jensen or Hölder. The fixed moment order is chosen after the width limit, and \(S_*\) is fixed beforehand.

The quantitative exponent separation is sufficient. The control-net logarithm is eventually below \(n^{0.65}\), whereas the Gaussian tail exponent is \(n^{0.78}\). Its interpolation error is \(n^{-1/8+1/200}\operatorname{poly}(\ell)=o(n^{-1/10})\). In the nonlinear remainder closure, the largest stated forcing exponent is \(-0.08\); adding the propagator exponent \(1/4000\) gives \(-0.07975<-1/25\). Thus the comparison improves the stopped remainder \(n^{-1/25}\), and the resulting coordinate bound \(n^{-1/30}\) is compatible with the powers displayed.

I checked that first-layer incoming rows are treated separately: their covariance is \(I_d\), but they do not create a retained reverse port below the first layer. The argument therefore does not apply a false \(1/n\) variance normalization to that row. At the top, the omitted readout contributes its explicit residual offset.

Locations: `compact_foundations.tex:254–319`, `378–678`, `683–800`, `1024–1080`.

### 3. Trace absorption and complete-path moments

The trace calculation uses normalized Schatten norms with normalization \(n^{-1/p}\), not parameter-space dimension. With Hölder exponents summing to one, the resulting trace has normalization \(1/n\) even though the parameter space has order \(n^2\) coordinates. The endpoint maps factor through neuron space, so the rank normalization is applicable.

I reconstructed the carrier part of the insertion series:

\[
 \frac{8e^2D_*^2S^2\mathcal B}{\eta_*^2}
 \sum_{h\ge1}(2eD_*S^2/\eta_*)^h(h+2)^2.
\]

The inequality \(\sum_{h\ge1}q^h(h+2)^2\le36q\) for \(0\le q\le1/2\) is correct, including equality at \(q=1/2\). It gives the displayed \(S^4\) bound. The scalar feedback inequalities have coupling product \(4D_0C_FS^2\le1/2\), so their absorption is valid.

For budget removal, the correction processes are defined on complete independently stopped paths. Projecting a singleton/common-cavity difference onto its deterministic ball preserves independence from the paired root. Its normalized Gaussian radius is \(4n^{-49/100}\), so polynomial Lipschitz moduli still give vanishing fixed-order moments. The distinct-root contribution factors conditionally on the common cavity; collision multiplicities \(O_u(n^{k-u})\) dominate their \(n^{o(1)}\) weight bounds. The conclusion

\[
 \limsup_n\Pr\{\text{budget hit}\}\le mL(16L/\mathcal B)^u
\]

can therefore be sent to zero by taking the infimum over fixed integers \(u\), without a growing-deletion-count theorem.

Locations: `compact_foundations.tex:725–858`, `1024–1080`.

### 4. Complex continuation and the flaring domain

I specifically checked whether the proof assumes that a complex matrix \(G^\top G\) is positive. It does not. The fixed rectangle uses a short-segment operator bound. The flaring domain freezes the generator at a real anchor, where \(-2iG(t)G(t)^\top\) is skew-Hermitian, and bounds the changing part by the integrated derivative of \(G\).

The essential double integral is controlled by

\[
 \int_0^{h(t)}(h(t)-v)Ye^{-\nu t}e^{2\mathcal Kv}\,dv
 \le \frac{Yr_n}{2\mathcal K}.
\]

This follows directly from \(e^{2\mathcal K h(t)}-1=2\mathcal K r_ne^{\nu t}\). Since \(B_nr_n\to0\), the product of the operator-norm bounds on disjoint contour pieces is eventually below two, as needed in the insertion expansion. Thus this premise is supplied before using it in the local probabilistic argument.

The retractions commute with the real-anchor map; their Lipschitz constants are bounded. The source estimates use provisional response bounds for the derivative lemma, and only afterward improve response and pole margins and remove budgets. I did not find a circular use of the final analytic source claim. The all-time carrier extension is separately real: a crude factor \(n\) in parameter-to-carrier comparison is dominated by the \(e^{-16\ell}\) fitting tail.

Locations: `compact_foundations.tex:1084–1142`, `1166–1204`, `1244–1376`.

### 5. Legendre closure stability and endpoints

I checked the growing-interval projection identity and the endpoint coefficient at the boundary order \(q=1\). The squared multiplier norm is then exactly \(A/3\), so the endpoint bound includes this case. Differentiating the bilinear projection pairing gives the stated defect \(2\widehat\rho\sum_a e_{b,a}e_{h,a}^\top/(mn)\), with the correct sign.

The closure first obtains fitting and convergent parameters for every fixed order, independently of a dense comparison. Its residual-zero state is an equilibrium of the whole stored-state ODE, and \(\tau\ge1\) prevents a clock singularity. No runtime update divides by a residual.

In the comparison, subtracting each backward gate with the dense carrier as the reference gives a coefficient affine in the dense carrier maximum, rather than a new carrier factor at every depth. The signed perturbation estimate retains the negative term \(-2\|r-r'\|_m^2\); direct absolute-value Gronwall would not give the asserted dependence. The backward history comparison uses the closure residual direction, then freezes the dense response history at \(t_q=2\log q/\kappa\). Its weighted derivative estimate cancels the reciprocal clock speed. The resulting \(q^{-2}\) forcing bound and \(q^{-1}\) absorption term have the right powers.

Finally \(q_{\mathrm{abs}}=n^{o(1)}\) is exceeded by the proposed \(n^{1/4}\) order. Since all comparison constants are horizon-independent and physical limits were already proved, passage to all times and the fitted endpoint is justified.

Locations: `compact_legendre.tex:60–157`, `159–278`, `304–502`; `compact_fitting.tex:180–213`.

### 6. Selected dynamics: metric geometry and feedback cancellation

I independently checked the finite sparsification barrier calculation and the metric construction. With \(G=P^\top DP\), the formula for \(M\) gives \(P^\top MP=I\) and \(D/4\preceq M\preceq D\). Coordinate gates need not be self-adjoint in this metric; their operator bound follows from comparison with \(D\), and the proof does not claim otherwise.

Although the selected directions are not asserted to be gradients of the corrected predictor, their parameter-speed norm is exactly the Gram quadratic form used in the deficit equation. Hence
\(-\partial_t\rho_C^2=\|\dot\theta_C\|_{\mathrm{par}}^2\) is valid. The corrected readout is an orthogonal sum, which bounds its norm despite the inverse Gram. This independently preserves the feature gap, gives global existence, and gives parameter and prediction tails.

For the comparison, put \(e=(c_C-c_n)/\sqrt m\), \(T_C=V_CQ_C^{-1}\), \(p=T_Ce\), and \(\zeta=w_C-w_R+p\). Differentiation gives the cancellation

\[
 2V_Ce-2T_CQ_Ce=0.
\]

The remaining \(Q_C\) term in \(\tfrac12\partial_t\|p\|^2\) is \(-2\|e\|^2\). The hidden-Gram error can be absorbed using the label cap. In particular, \(\|p\|\le2\|e\|/\sqrt\lambda\) yields the stated integrated deficit bound, and \(p=0\) implies \(e=0\), validating the regularization at zeros. Combining the coefficient estimates gives the displayed scalar inequality for \(E=a_h+\|p\|+\|\zeta\|\). I found no missing factor of \(m\) in the source Gram defect: each matrix entry carries \(1/m\).

Locations: `compact_selected.tex:19–91`, `114–269`, `339–572`.

### 7. Dense variability is an actual lower bound

The innovation lemma does not assume centered activations, independent training coordinates, or invertible \(Q^{(L-1)}\). Its squared-area inequality, truncation at \(R_0^2=2M_4/D\), and two eigenvalue lower bounds yield a positive coordinate variance when \(m\ge2\), \(y\ne0\), and \(Q^{(L)}\succeq\gamma I\).

Conditional on both lower-layer initializations, the two final-layer row groups are independent. The centered scalar conditional law tends to a nondegenerate Gaussian. Any lower-layer contribution remains an arbitrary measurable shift; the Gaussian centered-interval maximality argument correctly handles that shift instead of requiring it to vanish. The characteristic-function remainder uses bounded conditional third moments, supplied by linear activation growth and Gaussian sixth moments.

The parameter-two ellipse estimate converts the derivative lower bound to a trajectory lower bound. I checked the endpoint polynomial derivative factor and the tail constant: the final error coefficient is \(4+8/N+12/N^2\le24\), including \(N=1\). With \(r=(\lambda\sqrt\ell)^{-1}\) and \(N\le4\ell\), the resulting scale is \(Y\sqrt\gamma/(\sqrt n\ell^{5/2})\). The witness must occur at positive time because both initial predictions vanish; the theorem correctly makes no fitted-training-endpoint lower-bound claim.

Locations: `compact_legendre.tex:508–699`.

### 8. Initialization-only provenance, coordinate counts, and quantifiers

The initialized-jet compiler is a mathematical existence construction, not a claim that a short Taylor polynomial at zero reaches the entire time interval. Its explicit disk-to-rectangle map satisfies \(\mathfrak t(0)=0\) and \(\mathfrak t(\xi_*)=T\), with \(\xi_*<1\), so a finite number of origin derivatives suffices for every fixed required accuracy. Derivatives at later panel anchors are reconstructed from that continued origin polynomial. Initialized matrix images can be paired exactly because the scalar coefficient operations commute with those fixed matrices. No later dense weight or trajectory sample is an input.

The distinction between preprocessing and retained state is explicit. The selected models discard dense arrays, source bases, jets, quadrature tables, and panel schedules after forming the selected arrays. Their inventory includes metrics, inverse caches, training buffers, initial copies, direction arrays, and query workspace. Legendre counts its dense initialized mixers separately from its moving state.

I checked the leading source-count powers. For Harmonic, \(\alpha_T^{-1}=131072(Y/\lambda)^2(U/a)\ell^{3/2}\); the time–sphere simplex count gives \(N=O(C^d(d+3)^{d/2}(Y/\lambda)^2\ell^{3d/2+1}/d!)\). Squaring produces the claimed \((Y/\lambda)^4\ell^{3d+2}\) term. For the finite panel, \(J=O((Y/\lambda)^2\sqrt\ell+\lambda^{-1}\log(e+\ell))\), and Taylor order \(O(\ell)\) gives exactly the two displayed squared-rank terms. The input-span reduction is exact because every first-layer update acts in the training-input span, which is contained in the declared-panel span.

The fixed-problem quantifier legitimately permits the width threshold to depend on \(Y>0\), the dimension, the panel size, and confidence. It is essential when absorbing additive logarithmic constants, the first-layer storage, and tails. The assembly compares the models with an actual independently initialized dense run on the same query domain; it only uses a union bound and does not require independence of approximation and variability events.

Locations: `compact.tex:139–146`, `182–202`, `223–254`; `compact_selected.tex:577–670`, `703–885`, `907–1006`.

## Boundary and arithmetic checks

The following attempted boundary cases did not falsify the argument: \(d=1\), handled by the two points of \(S^0\); \(m=2\), where the innovation lower bound still has a positive constant; singular intermediate feature covariances; uncentered or linearly growing activations; zero residuals in the signed comparison and selected comparison; \(q=1\) in projection and closure fitting; and arbitrarily small but fixed \(Y>0\). Zero labels are explicitly outside the ratio theorem and give a stationary zero predictor. Affine activations with a rank-deficient final Gram are excluded by \(\gamma>0\), rather than incorrectly claimed as covered.

As a supplemental arithmetic check, I evaluated the source recurrences for \(A_*\), \(D_*\), \(H_*\), and \(E_*\) at \(b=\beta-1\), \(s=t_2=\beta\), \(\beta\in\{10,16,32,100\}\), and \(L\in\{2,3,4,8\}\). Every checked ratio to its displayed power bound was below one; the largest was approximately 0.2112. This was a bounded inline Python calculation, exited successfully, and wrote no scientific or runtime files. It is only a sanity check; the verdict does not treat this finite grid as proof of universal coefficient inequalities. The geometric recurrences, scale powers, and key numerical margins above were also checked algebraically.

## Severity triage, unresolved issues, and limits

There are no supported F, M, or L findings. In particular, no claim was classified as false merely because its constants are large or because its preprocessing may be impractical.

The common source proof is the main residual verification risk because it combines lengthy differential recursions, localized nonlinear remainders, conditional Gaussian estimates, and continuation. I checked its central dependencies and exponent margins, but did not formalize every large coefficient envelope in a proof assistant. This is a limitation of audit coverage, not an identified mathematical gap or a request for new scientific assumptions.

This audit does not assess novelty, empirical performance, finite-precision stability, implementability of arbitrary analytic activation derivatives, practical initialization cost, or polynomial width thresholds. Those are not claims of this theorem-focused manuscript. No code was supplied within the assigned input set, so no implementation claim or code-execution claim is made. No independent critical external research result is invoked as a black box by the audited headline proof; the classical elementary analytic and approximation facts used in it were assessed in their stated specializations.

Necessary repairs: **none identified**. Any change to a reviewed input invalidates the hash-specific scope of this verdict and requires checking the changed proof and its downstream dependencies.
