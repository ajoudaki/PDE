# Independent mathematical audit A

Date: 2026-10-09. Assignment: isolated audit of the five frozen compact-manuscript sources, with special attention to the shared-source probability and continuation argument. This report is the sole review artifact.

## Verdict and scope

**No confirmed fatal, major, or minor mathematical defect was found.** The headline argument is sound within the verification coverage below: the stated small-label, fixed-problem, eventual-width hypotheses support the three approximation constructions and their comparison with actual independent dense-run variability. No required mathematical repair was identified.

This is an independent source-level mathematical audit, not a formal verification certificate, an experimental reproduction, or approval to promote the results. I read every line and every proof in the assigned inputs and independently reconstructed the principal normalization, probability, continuation, stability, and storage arguments. The very long local coefficient and remainder estimates were checked against their defining recurrences and the uses that make them load-bearing; I did not mechanically certify every scalar arithmetic inequality in those estimates. Confidence is high in the explicitly reconstructed identities and scope checks, and moderate-to-high in the complete shared-source proof, whose many interacting estimates remain the main concentration of audit risk.

The input restriction was observed. I did not read the study README, inventories, history, other studies, the original main paper, prior reviews, other reviewers' findings, or Git history. No manuscript file was edited. No scientific input needed for this assigned proof audit was missing. No external research was used, and no novelty comparison or code/empirical assessment is asserted. The required rigorous-math, canonical-notation (including neural conventions), paper-review, and severity-rubric instructions were read and applied. The explicitly assigned single-report format controls this audit.

## Frozen inputs and complete reading coverage

The initial hashes were taken before manuscript ingestion. The final hashes were taken after complete reading and the substantive checks; they agree exactly. The “SHA256 before = after” column records both measurements, not merely a hash supplied by the author.

| Input | Complete lines read | SHA256 before = after |
|---|---:|---|
| `paper/compact.tex` | 1–290 | `a56acbdc765fa6e42f8aba186dec0b3ea3a59e9fa4c7d66ac1a7839bc0688445` |
| `paper/compact_fitting.tex` | 1–244 | `f35f1dfd9c47bd5abbf97c849b0176347e9e5da8adba5e7ab8b75c79868b2c51` |
| `paper/compact_foundations.tex` | 1–1554 | `4e7d25a8501e7928f60e538f1c80e7e73a3e2f04d34a1ae4d40407ffc1f545f9` |
| `paper/compact_legendre.tex` | 1–752 | `bca774baab3a5ba9879340fc61a92b9cbdff522600620d1972ab12b876f48239` |
| `paper/compact_selected.tex` | 1–1118 | `cd203e7de6f8e3d23331d58ac64366350dd076405d63e8fc238f8f9a794beeee` |

Total: **3,958 lines**. This includes the setup and final assembly; initialization, cavity fitting, and signed perturbation; every part of the source proof and its public-bound reduction; projection identities, the entire Legendre comparison, innovation and conditional fluctuation; sparse selection, selected fitting and cancellation, initialized-jet compilation, joint harmonic approximation, and finite-panel construction. An initially truncated display of the main file was completed by a separate read of lines 120–180; no coverage claim rests on omitted output.

## Independently reconstructed mathematical chain

For the calculations in this report only, write \(\lambda=\gamma/m\), \(\ell=\log(en)\), and, when discussing the source proof, \(S=16Y/\lambda\). These are exactly the local quantities used in the manuscript; the meanings of its network weights, features, residuals, and backward responses are unchanged.

### 1. Dense fitting and signed stability

References: `compact_fitting.tex:4` and `compact_fitting.tex:209`.

The mobility coordinates are \((W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\). With the manuscript's loss \(\rho^2=m^{-1}\|r\|_2^2\), their velocity is its negative Euclidean gradient. Consequently

\[
-\partial_t\rho^2=\|\dot\theta\|_{\rm par}^2,
\qquad
\|\dot\theta\|_{\rm par}^2\ge\lambda\rho^2
\]

on the stopped readout-Gram tube. Weighted Cauchy–Schwarz then gives the length bound \(2\rho(t)/\sqrt\lambda\); the hidden displacement and singular-value margins close the stop. The factors of \(m\), \(n\), and two agree with the displayed network and loss. The initialization argument uses covariance continuity on the positive semidefinite cone and therefore does not silently require nonsingular intermediate Grams. The cavity comparison keeps the original denominator \(n\).

For the signed perturbation lemma, putting \(d=\theta-\theta'\) and \(R=r-r'-J'd\) gives the exact negative term \(-2\|r-r'\|_m^2\). The remaining two nonlinear terms are bounded by \(K(\rho'+3\rho)\|d\|^2\). This checks both the sign and the coefficient in the integrable-residual stability estimate; it is not an unsigned Lipschitz estimate over an infinite physical horizon.

### 2. Shared-source probability and continuation

References: `compact_foundations.tex:356`, `:704`, `:788`, `:1092`, `:1129`, `:1187`, `:1250`, `:1312`, and `:1484`.

This is the principal load-bearing dependency. I checked the following logical order and quantitative links.

1. **Independent reference construction.** Each cavity's initial test, stopping rule, and clipped coefficient extension use retained initialization. Omitted roots are integrated only afterward. Actual adaptive scalar controls are substituted after obtaining estimates uniform over deterministic control histories. The manuscript does not subsequently assert that those adaptive variations remain centered Gaussian. Same-root quadratic means are retained in the four trace terms; the reverse port does not incorrectly enter the forward residual.

2. **Mobility and port normalization.** With \(\Theta=(W^{(1)},\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\) and \(F_a=nf_n(x_a)\), the physical equation is \(\dot\Theta=-(2/m)\sum_a r_a\nabla_\Theta F_a\). Rescaling \(\bar u=(\Theta-\Theta_0)/S\) and \(\bar F=F/S\) gives the retained equation and its generator

   \[
   -\frac{2}{mn}\sum_a g_ag_a^\top
   -\frac2m\sum_a r_aD^2F_a.
   \]

   In particular, the residual scaling does not introduce an unaccounted inverse power of \(S\) into the nonlinear remainder. The first-layer omitted row has its own treatment: there is no retained reverse port below it, so the proof does not apply the \(N(0,I/n)\) concentration argument to its \(N(0,I_d)\) incoming row.

3. **Entropy and nonlinear closing exponents.** The scalar-control net has log-cardinality \(n^{5/8}\operatorname{poly}(\ell)\), eventually below \(n^{.65}\). A map norm bounded by \(n^{1/200}\), normalized Gaussian covariance, and threshold \(n^{-1/10}\) give a concentration exponent of order \(n^{.79}\), leaving the stated \(.78\) margin. This dominates control, coordinate, terminal, frame, and every fixed-deletion-count union. With \(N=n^{.01}\), \(d_0=n^{-.1}\), and \(u_0=n^{-.04}\), the leading remainder terms are \(n^{-.08}\); multiplication by \(n^{1/4000}\operatorname{poly}(\ell)\) is still \(o(u_0)\). These exponents genuinely close the proposed first-exit comparison.

4. **Trace absorption and complete-path moments.** The normalized Schatten products supply \(n^{-1}\) traces despite the larger parameter dimension. The small allowance is chosen before the moment/deletion order. In the scalar feedback inequalities, the forward coefficient \(D=C_FS^2\) satisfies \(4D_0D\le1/2\), which permits actual absorption rather than assuming independent responses. The real reference modulus is in normalized residual activity, whose interval is bounded independently of the physical horizon. Under provisional stops, \(B_n=O(\log\ell)\); the complex-minus-real Gaussian radius is \(O(B_n/\sqrt\ell)\), and its expected supremum is \(O((\log\ell)^{3/2}/\sqrt\ell)\), which tends to zero. The common-cavity correction has radius \(O(n^{-49/100})\) and likewise has every fixed required exponential moment tending to one.

   Conditional independence is used for distinct omitted roots only after passing to their common cavity. Corrections need not be independent and are handled by Hölder. Repeated-root contributions vanish because their multiplicity loses a power of \(n\), whereas the stopped weights cost only \(n^{o(1)}\). The order of limits is legitimate:

   \[
   \limsup_{n\to\infty}\Pr\{\text{budget hit}\}
   \le mL(16L/\mathcal B)^u
   \]

   for every fixed positive integer \(u\), followed by the infimum over \(u\). Here \(\mathcal B=1024e^2L\), so the base is strictly below one. No growing deletion order or confidence-dependent label shrinkage is inserted.

5. **Complex continuation is not based on positivity of a complex Gram.** On the fixed rectangle, short exceptional pieces are controlled by operator norms. On the expanding domain, the real-anchor matrix \(A_t=2G(t)G(t)^\top\) is real symmetric; \(-iA_t\) generates unitary vertical motion. With

   \[
   h(t)=\frac1{2\mathcal K}\log(1+2\mathcal K r_ne^{\nu t}),
   \qquad \nu=\lambda/4,
   \]

   the independently available real decay gives

   \[
   \int_0^{h(t)}\rho(t+iv)\,dv\le Yr_n,
   \quad
   \int_0^{h(t)}(h(t)-v)\rho(t+iv)\,dv
   \le\frac{Yr_n}{2\mathcal K}.
   \]

   These bounds reproduce the growth exponent
   \(4\mathcal Kr_n+(2C_g/\sqrt{\mathcal K})B_nYr_n=o(1)\).
   The same additive bounds apply to disjoint subpieces of a canonical contour, as needed by the insertion series. Provisional derivative bounds precede this check, so the premise does not rely on already-removed probabilistic stops. The pole improvements, independent cavity margins, and complete-path moment estimates then close the continuation argument.

6. **The public statement supplies its callers.** The final reduction explicitly proves the stated time and query radii, coordinate envelopes, real all-time RMS bounds, and the pre-gated training-carrier bound. The latter is extended after \(T=32\ell/\lambda\) using parameter length: the coarse extra factor \(n\) multiplies \(e^{-16\ell}\), which vanishes fast enough. The panel centers and radii depend only on declared problem parameters, and the public count retains \((Y/\lambda)^2\sqrt\ell\). Later constructions do not need inaccessible private source coefficients. Passive backward fields on the sphere are obtained by their actual finite recursion; they add no passive training labels.

The proof is lengthy and algebraically dense, but I found neither a demonstrated conditioning error nor a circular use of the final source event in these critical steps.

### 3. Legendre dynamics, fitting, and comparison

References: `compact_legendre.tex:4`, `:78`, `:197`, and `:498`.

The growing-interval projection identity follows because the derivative of the projected polynomial remains in the same degree space. Differentiating the bilinear projected-history pairing gives the full endpoint product minus the product of the two endpoint errors, hence the positive defect

\[
\mathcal E_\ell=\frac{2\widehat\rho}{mn}
\sum_a e_{b,a}^{(\ell)}e_{h,a}^{(\ell-1)\top}.
\]

The history starts at clock one with a constant forward prefix and zero backward prefix. Its stored equations neither divide by a residual nor leave a nonzero clock velocity at zero residual. The order-independent physical argument controls this defect sufficiently to retain fitting and parameter limits for every finite order. The signed comparison uses actual dense training carriers; its backward subtraction does not presume the same coordinate bound for closure or passive-query carriers.

The forcing estimate has a \(q^{-2}\) term and a \(q^{-1}\) discrepancy term that is absorbed once \(q\ge q_{\rm abs}=n^{o(1)}\). The displayed choice of \(q\) eventually satisfies this condition. Squaring its factor \(n^{1/4}\ell^2e^{\sqrt\ell/2}\) cancels the comparison factor \(e^{\sqrt\ell}\) and yields \(CY/(\sqrt n\ell^3)\). The inventory distinguishes the moving \(O(mnq)\) memories from the \((L-1)n^2\) fixed mixers; it does not claim polylogarithmic total storage for this construction.

### 4. Actual dense variability and its probability

References: `compact_legendre.tex:539`, `:572`, `:602`, and `:645`.

The innovation proof uses the squared-area inequality with \(c=Qy\), a split at \(\|U\|=R_0\), and the positive spectral gap. Its conclusion is a strictly positive scalar variance at some deterministic training index even when earlier-layer covariance is singular.

At zero readout the exact derivative is

\[
\dot f_n(0,x_a)=\frac{2}{mn}\sum_iU_{i,a}(U_i^\top y).
\]

Conditional on the two lower-layer initializations, the two groups of last-layer rows are independent. Their centered difference has asymptotic variance \(s_*^2=8v_*/m^2\). The conditional mean difference may be an arbitrary random shift; the proof retains it and uses the maximal interval mass of a centered Gaussian, rather than incorrectly claiming an unconditional centered CLT. Uniform conditional CDF convergence justifies that small-ball estimate for random shifts.

I also checked the Chebyshev derivative-transfer factor: the endpoint polynomial inequality contributes \(2N^2/r\), and the explicitly summed derivative tail gives the stated constant 24. With \(r=(\lambda\sqrt\ell)^{-1}\) and \(N=O(\ell)\), the resulting lower bound has precisely \(n^{-1/2}\ell^{-5/2}\) scale. It is a positive-time training-input witness, not an endpoint fluctuation claim. The constant's remaining moment ratio depends only on activations and depth because all input norms are equal.

### 5. Selected geometry, fitting, and corrected dynamics

References: `compact_selected.tex:11`, `:90`, `:238`, `:373`, and `:549`.

The sparsification barriers produce weights with spectrum in \([1,4]\). In the constructed metric, the middle operator has eigenvalues those of \(G^{-1}\) on \(\operatorname{ran}Z\), and eigenvalue one on its complement; direct multiplication gives \(P^\top MP=I\). Thus the exact normalized source pairing, metric equivalence, constant mass, and factor-two coordinate-gate bounds are compatible. The selected initialized mixer and its metric adjoint reproduce the required paired images; an ordinary transpose would not suffice, and the manuscript uses the correct adjoint.

The prescribed selected directions need not be gradients of the corrected predictor. Nevertheless, their squared parameter norm equals \(4c_C^\top K_Cc_C/m^2\), and the separately evolved deficit satisfies the matching dissipation identity. The correction enforces \(f_C(x_a)=y_a-c_{C,a}\). The proof does not silently assume coordinate gates are self-adjoint in the non-diagonal metric.

For the decisive cancellation, define \(T_C=V_CQ_C^{-1}\), \(e=(c_C-c_n)/\sqrt m\), \(p=T_Ce\), and \(\zeta=w_C-w_R+p\), as in the manuscript. The identity \(T_CQ_C=V_C\) cancels the otherwise problematic \(2V_Ce\) term. Moreover,

\[
\langle p,T_CQ_Ce\rangle=\|e\|_2^2,
\qquad \|p\|\le2\|e\|_2/\sqrt\lambda,
\]

so the dissipative estimate really controls the needed integral of \(\|e\|_2\). The hidden-Gram error is small under the stated label cap. The source-energy integral, inherited from the dense parameter length, avoids an additional reciprocal-gap loss. Recombining these estimates gives the manuscript's coefficient integral \(\mathcal B_n\), including its single additive \(\sqrt\ell\) carrier factor. The all-time extension uses independently proved selected and dense tails; it does not extrapolate a finite complex-domain bound without justification.

### 6. Initialization-only provenance and retained dimensions

References: `compact_selected.tex:640`, `:661`, `:769`, `:905`, and `:997`.

The conformal time map in the compiler satisfies \(\mathfrak t(0)=0\) and \(\mathfrak t(\xi_*)=T\), maps the unit disk into the supplied time rectangle, and has \(\xi_*<1\). Thus finitely many origin jets give arbitrarily accurate finite coefficient lists through an actual uniformly convergent Taylor series. Derivatives at later anchors are recovered from this series on a larger compact disk; they are not supplied as later trained data. Initialized images are imposed by applying the actual initialized matrix to each base coefficient. This is a finite-existence result with potentially enormous preprocessing, as explicitly disclosed.

The harmonic argument includes spatial holomorphy on the quadric, the Gegenbauer multiplier estimate, the time Fourier contour, and the weighted-simplex coefficient count. In particular,

\[
\alpha_T^{-1}=128\beta^{30L}(Y/\lambda)^2\sqrt{d+3}\,\ell^{3/2},
\qquad r_q^{-1}=\beta^{3L}\sqrt{(d+3)\ell}.
\]

With the cutoff of order \(\ell\), this gives coefficient count proportional to \((Y/\lambda)^2\ell^{3d/2+1}\); squaring for the retained mixer/metric inventory gives \((Y/\lambda)^4\ell^{3d+2}\). The separate \(d=1\) argument has exponent five, consistently with this formula.

For a fixed finite panel, the Taylor degree is \(O(\ell)\) and the supplied partition has

\[
J=O\big((Y/\lambda)^2\sqrt\ell+\lambda^{-1}\log(e+\ell)\big).
\]

Squaring the resulting source rank gives the two advertised storage terms. Reducing the first layer to the span of the declared inputs preserves their norms, sample inner products, Gaussian row law, and coupled predictions; it does not change the normalization. The retained input map and original/transformed data are charged. Both selected inventories include metrics, inverse caches, initial copies, training arrays, selected indices, directions, and query workspace. Dense source bases, jets, and schedules are preprocessing artifacts and are explicitly discarded. Activation evaluation and finite precision are separately qualified, not silently free computational conclusions.

## Severity, dependency, and headline assessment

| Category | Confirmed concern | Affected result | Required repair |
|---|---|---|---|
| Fatal flaw | None found | None identified | None identified |
| Major flaw | None found | None identified | None identified |
| Minor mathematical flaw | None found | None identified | None identified |

The source proposition is shared by all three comparisons, by the dense lower bound, and by the initialized coefficient constructions. A failure there would have broad consequences; the continuation, conditioning, moment-order, and public-interface checks above were therefore treated as substantive proof checks rather than plausibility checks. They did not produce a counterexample or a demonstrated gap.

The final assembly uses the same query domain and full physical-time norm in numerator and denominator. Its union bound requires no independence between approximation and lower-bound events. A bound \(CY/(\sqrt n\ell^3)\) divided by the dense lower scale tends to zero as \(\ell^{-1/2}\); the selected \(Y/n\) bound gives \(\ell^{5/2}/\sqrt n\). The fixed-confidence limsup bound can then be sent to zero. Fitted-limit existence and zero-denominator failures are explicitly included in the probability convention.

The qualifications are material and consistent: data and depth are fixed while width grows; panels are declared before initialization; thresholds may depend on every fixed problem parameter and need not be practical; there is no uniform small-label limit, efficient-preprocessing claim, or precision bound. These are not empty hypotheses. For example, two orthogonal normalized inputs with odd strip-analytic `tanh` activations give a positive diagonal population Gram at every fixed layer, and admit strictly positive labels satisfying the stated sufficiently small cap. No stronger growing-data, undeclared-query, endpoint-variability, or computational-efficiency conclusion is supported or inferred here.
