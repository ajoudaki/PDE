# Independent audit of the unclipped finite-history theorem

2026-10-07. Reviewer: the kinetic-route agent. Scientific scope: the complete `UNCLIPPED_FINITE_HISTORY.md`; the complete `FINITE_RESPONSE_MEMORY.md`, read to verify actual-Euler membership and its local posterior formula; and the previously audited rank-robust conditional-law proof and the reviewer's own notes. Required mathematical skills remain current. No literature, other study, additional author-route file, experiment, or Git material was consulted. No source file was edited.

Reviewed hashes:

- `UNCLIPPED_FINITE_HISTORY.md`: `814a72f722b26ab2a8d360b8c03bb9e4781fe4ba4733948c14a731605da86595`.
- `FINITE_RESPONSE_MEMORY.md`: initially `bc4037f3e95d5a0587b01ec5d8e4ccbcfe990d4391c820e318f1dec45789fc09`; then reread completely at `edf19fb88cc1d3b719b3668c575aa6a1316fa30b2c822d277fc84e7428b34c91` after a concurrent edit was detected.
- Previously audited posterior/simulator proof in `RANK_ROBUST_FINITE_PROGRAM.md`: `baf872d95919981848b0b0d7958b737426feffb6a29508d7ea1870365c815f62`.

Provenance note: the main theorem remained unchanged throughout the audit. The concurrent response-memory edit restricted residual notation to training indices, qualified the information-reduction claim when histories span the entire matrix, and appended a sentence mentioning another internal audit's verdict. My proof check and the PASS below had already been written before this reread. I did not read the other report or use its verdict; this accidental exposure is disclosed, and no blind-review claim is made for the revised response-memory file. The revised membership equations give the same conclusion.

## Verdict

**PASS for the stated qualitative fixed-program theorem, including actual fixed finite Euler computations with the specified activation bounds.** The one-sided gated-product estimate is correct and closes the original/simulator comparison using only the simulator's empirical square-tail control. No higher empirical moment of the original program, independence between a query and its matrix, positive history-rank gap, or extra label restriction is required.

The conclusion is convergence of bounded Lipschitz empirical tests, second/cross moments, and the prescribed continuous scalar outputs for each fixed finite program. It supplies no width rate, statement uniform in the number of instructions, continuous-time limit, or all-time closure. Those exclusions are necessary and correctly stated.

A minor well-definedness convention should be retained when stating the abstract program class: scalar coefficient operations must produce finite values at the finite-width inputs where the program is run. If a coefficient formula is defined only on a neighborhood of its limiting argument, give it any finite measurable extension outside that neighborhood; the proof then shows that the extension is used with probability tending to zero. The actual Euler coefficients are polynomial combinations of finite inner products, so this convention imposes no restriction on that application.

## 1. The scalar construction is causal rather than circular

At each instruction, its input fields and all earlier empirical-inner-product limits have already been constructed. Evaluating the specified continuous scalar coefficient functions at those earlier limits produces finite deterministic coefficients, under the stated neighborhood qualification. Their finiteness can be checked recursively at the instruction where they first appear; no future law is needed.

The new matrix-query innovation variance is then an expectation under a previously constructed population law. If it is zero, the query input equals the retained-history linear combination in \(L^2\); if positive, it supplies a new independent \(L^2\) direction. The same augmented-Gram calculation as in the rank-robust proof shows that each retained Gram is positive definite. The retain/omit schedule and all omission coefficients are thus deterministic functions of the fixed program and its already constructed laws.

Every limiting scalar field has all finite moments. Globally Lipschitz scalar functions have at most linear growth; a gated product obeys

\[
|u\,a(v)|\le\|a\|_\infty |u|;
\]

finite linear combinations use finite deterministic coefficients; and each retained query is a finite linear combination plus a Gaussian innovation. Inner-product expectations therefore exist at each step. There is no rank assumption hidden in this moment induction. Small positive innovation variances can produce large fixed regression coefficients, but only zero variances are omitted, and the theorem claims no uniform rate near such parameter values.

This construction includes zero queries, zero labels, repeated queries, singular root covariances, and empty forward or reverse histories. With zero innovation, the omitted cross-direction correction would also vanish because the residual input is zero almost surely and all pairing factors have finite second moments.

## 2. Unbounded query inputs do not invalidate the simulator law

The simulator reveals only its retained matrix actions. Its omitted outputs are functions of the old transcript and deterministic limiting coefficients. Although the original program is later coupled on the same matrices, its extra queries are not included in the simulator's conditioning sigma-field. This separation is legitimate and essential.

The exact two-sided Gaussian posterior requires that a new query be predictable from that transcript and have finite coordinates. It does not require coordinatewise boundedness. Conditional on the past, the query is a fixed vector, so its new action is a linear observation of the Gaussian remainder. Unbounded random query norms present no problem for this conditional identity.

For retained forward histories \(H_n,F_n\) and reverse histories \(D_n,B_n\), the exact forward conditional law is

\[
G u_n=F_n a_n+D_n b_n+sigma_n(I-P_{D_n})\xi,
\]

where \(a_n,b_n\) are empirical regression coefficients and
\(\sigma_n^2=\|u_n-H_na_n\|_{2,n}^2\). This follows from the previously audited posterior mean and covariance with entry variance \(1/n\). It retains the necessary forward/reverse correction. Reuse in either direction and multiple independent matrices are handled by the same predictable-query induction; no new matrix independence is asserted after an adapted action.

On the simulator's moment-induction hypothesis, every retained empirical Gram converges to its positive definite limiting Gram. Thus normalized inverses and regression coefficients converge in probability. An accidental finite-width rank loss has probability tending to zero. The exact posterior uses pseudoinverses on that event, so the simulator remains defined there; only the asymptotic inverse calculations omit it.

For the opposite-history noise projection,

\[
P_{D_n}\xi=D_n e_n,
\qquad
e_n=(D_n^\top D_n)^{-1}D_n^\top\xi,
\]

the conditional covariance is exactly

\[
\operatorname{Cov}(e_n\mid\text{past})
=(D_n^\top D_n)^{-1}
=\frac1n(D_n^\top D_n/n)^{-1}.
\]

Localizing the latter inverse to a fixed bounded neighborhood of its limit gives \(e_n=O_{\mathbb P}(n^{-1/2})\). For every fixed finite \(p\),

\[
\|D_ne_n\|_{p,n}
\le\sum_j|e_{n,j}|\|D_{n,j}\|_{p,n}=o_{\mathbb P}(1),
\]

because the history has fixed finite length and its empirical moments are bounded in probability. Coordinatewise query boundedness is not needed for this step. The factor \(\sigma_n\) is also bounded in probability because it converges, so multiplying the projection by the conditional noise scale preserves the conclusion.

## 3. Simulator convergence of all polynomial-growth tests

The nonmatrix simulator induction is valid. For a fixed coefficient, composing a continuous polynomial-growth test with any allowed coordinate operation gives another continuous polynomial-growth test. In particular, the bounded gate makes its product at most linear in the unbounded field. Inner products are degree-two tests.

A random acquired scalar coefficient converges by the already established empirical-moment limit and the specified continuity of its scalar formula. On a compact neighborhood of that limit it is bounded. Its replacement by the limiting coefficient can be handled either directly in empirical \(p\)-norms for a linear combination, or by uniform continuity on bounded row sets and a higher empirical moment for an arbitrary composed test. Rare events outside the coefficient neighborhood can be discarded for convergence in probability. No expectation bound on the random finite-width coefficient is required.

After removing the negligible projection and replacing convergent regression coefficients, the new query answer is a fixed linear combination of old row fields and an independent Gaussian coordinate. For a continuous polynomial-growth test \(\psi(v,Z)\), the conditional expectation

\[
\overline\psi(v)=\mathbb E_Z\psi(v,Z)
\]

is continuous and has polynomial growth: Gaussian moments supply the growth envelope, and on a bounded set of \(v\) they also supply an integrable dominating function for continuity. Its empirical average has the required limit by induction.

The conditional variance of the test average is bounded by

\[
\frac Cn\left(1+\frac1n\sum_i\|v_i\|^{2k}\right)
\]

for some finite fixed \(k\). The parenthesis is tight by the prior simulator moment convergence. Conditional Chebyshev, first on an event where that empirical moment is bounded, proves that the centered average vanishes in probability. Independence is needed only for the fresh Gaussian coordinates conditional on the existing simulator transcript, which the exact posterior supplies.

Vanishing projection and coefficient perturbations can then be passed through polynomial-growth tests by compact-row truncation and a strictly higher empirical moment. This is the same justified transfer step as in the prior rank-robust proof. It establishes joint convergence of all old and new row fields in the target population, not merely a marginal law for the newest field. Such joint convergence is what later history pairings require.

Consequently all simulator empirical moments converge in probability, although their unconditional expectations need not be uniformly bounded. The proof uses tight empirical moments, which is the appropriate and sufficient statement.

## 4. The one-sided RMS estimate is correct

Let \(a\) be bounded and globally Lipschitz. The exact comparison can be written

\[
u,a(v)-\widetilde u,a(\widetilde v)
=(u-\widetilde u)a(v)
+\widetilde u\,[a(v)-a(\widetilde v)].
\]

Splitting the second term according to \(|\widetilde u|\le R\) or \(|\widetilde u|>R\) gives

\[
\begin{aligned}
\|u,a(v)-\widetilde u,a(\widetilde v)\|_{2,n}
\le{}&\|a\|_\infty\|u-\widetilde u\|_{2,n}
+R\operatorname{Lip}(a)\|v-\widetilde v\|_{2,n}\\
&+2\|a\|_\infty
\|\widetilde u\,\mathbf1_{\{|\widetilde u|>R\}}\|_{2,n}.
\end{aligned}
\]

The unbounded multiplier in the sensitive term is exclusively the reference field \(\widetilde u\). At fixed \(R\), the first two terms vanish in probability under the assumed RMS comparisons. The last term vanishes in the iterated limit because

\[
\frac1n\sum_i |\widetilde u_i|^2\mathbf1_{\{|\widetilde u_i|>R\}}
\le\frac1{R^2}\frac1n\sum_i|\widetilde u_i|^4,
\]

and the simulator's empirical fourth moment converges to a finite deterministic value. This proves the precise uniform-integrability-in-probability condition used in the note. The inequality never invokes a higher moment of \(u\) or \(v\), and its use in the coupling is not circular.

The boundedness of \(a\) is decisive. With two unbounded factors, the near/tail decomposition displayed here would no longer control the first term by the original RMS error alone. The theorem has not silently admitted arbitrary coordinate products.

## 5. Coupling closes using only second moments of original fields

The fixed collection of initial Gaussian matrices has operator norms bounded in probability. The explicit net bound in the note is numerically correct: \(\|G\|_{\rm op}>8\) implies a net bilinear form exceeds 4, whose two-sided tail is \(2e^{-8n}\). The \(9^{2n}\) union factor leaves exponent \(2\log9-8<0\).

At each coupling step, the prior original registers are RMS-close to their simulator counterparts. Since the simulator RMS norms are bounded in probability, the original RMS norms are also bounded in probability by the triangle inequality. This supplies exactly what is needed for the two-factor estimate

\[
|\langle u,v\rangle_n-\langle\widetilde u,\widetilde v\rangle_n|
\le\|u-\widetilde u\|_{2,n}\|v\|_{2,n}
+\|\widetilde u\|_{2,n}\|v-\widetilde v\|_{2,n}.
\]

Thus acquired scalar arguments converge to the simulator's deterministic limits. Continuity and local finiteness of their prescribed coefficient functions then give convergence of the original and simulator coefficients to the same finite values. Finite scalar-weighted linear combinations preserve RMS comparison; Lipschitz coordinate operations do so directly; the gated products do so by Section 4 of this audit.

For retained matrix calls, multiplication by the same matrix maps the RMS difference to another vanishing difference using its operator norm. For an omitted call, the simulator retains the exact identity \(G H_n=F_n\), and hence

\[
G u_n-F_na
=G(u_n-\widetilde u_n)+G(\widetilde u_n-H_na).
\]

The first input vanishes by prior comparison. The squared RMS norm of the second converges, by simulator joint second moments, to the zero innovation variance. Multiplication by an \(O_{\mathbb P}(1)\) operator norm preserves both limits without an independence assumption. The reverse direction is identical.

This finite induction establishes RMS comparison for every field. Bounded Lipschitz test averages transfer using their Lipschitz constant and normalized Cauchy–Schwarz. Second and cross moments transfer by the two-factor inequality. There is no invocation of convergence of a third or higher original empirical moment, and the source correctly does not claim it.

## 6. Membership of actual fixed finite Euler computations

The exact force-memory identities in `FINITE_RESPONSE_MEMORY.md`, equations (1)–(3), place a fixed finite Euler calculation in the new grammar without using the empirical Gram inverses of the response simulator as original-program operations.

The first-layer initial panel consists of iid Gaussian rows with the fixed input Gram as covariance, independently of the hidden initialized Gaussian matrices. The history identity for a later first-layer field is a finite scalar-weighted combination of these roots and stored backward fields.

For hidden layer \(\ell\ge2\), the current preactivation is the initialized matrix query \(G_\ell h_{\ell-1,a}^k\) plus a finite sum of stored backward fields. Its coefficients are products of a fixed step-size/loss factor, an earlier residual, and an empirical cross-time feature inner product. During a forward sweep the current lower-layer feature is already available, so all these inner products are causal.

During the backward sweep, \(\delta_{\ell,a}^k=\phi'_\ell(z_{\ell,a}^k)b_{\ell,a}^k\) is exactly an allowed gated product. The real strip derivative bound gives a bounded \(\phi'_\ell\), and the Cauchy estimate gives a bounded real \(\phi''_\ell\), so the gate is globally Lipschitz. The backward field one layer lower is the initialized transpose query plus a finite sum of stored features weighted by empirical cross-time backward inner products. Its current upper-layer backward field is already available at that point in the sweep.

Readout, predictions, and residuals are finite linear combinations and empirical inner products. Their history coefficients are polynomial, hence globally defined and continuous functions of earlier acquired scalar quantities. No additional label smallness, fitting condition, or step-size stability condition is needed merely to execute a fixed finite number of these Euler updates and take the width limit. All fixed finite values can be large; the theorem is qualitative and permits its constants to depend on the entire finite program.

Passive panel inputs are included among the evaluated fields, while only training indices enter the history-write sums. The exact identities preserve this distinction. The membership claim therefore includes their fixed-panel outputs and the named feature/backward pairings.

This audit does not validate the integrated-source numerical or compression claims discussed later in `FINITE_RESPONSE_MEMORY.md`. Those claims are unnecessary for the membership check and were not imported into the audited theorem.

## 7. Remaining limits and recommendation

The two separate inductions are logically ordered: first define the deterministic scalar laws and schedule; then prove the modified simulator's full polynomial-test convergence; finally compare the original program to that already controlled simulator in RMS norm. Neither the rank choice nor the reference tail bound depends on an unproved original-network limit.

The result identifies the actual finite-history aggregate law and its second-order observables for fixed depth, panel, step size, and number of Euler steps. It does not control an increasing program length, shrinking time step, or growing observable class. The tail argument takes limits in the order \(n\to\infty\) followed by the tail cutoff \(R\to\infty\); it supplies convergence but no \(n^{-1/2}\) rate. Population history gaps may shrink with program length, and the proof supplies no uniform bound on their inverses.

I recommend accepting the candidate as internally checked at this finite-history scope, with scalar coefficient operations understood to define a legitimate finite-width program. The extension beyond clipped globally Lipschitz query programs is substantive and the new one-sided comparison argument is sufficient for it. Continuous-time identification, quantitative weak stability, finite autonomous memory, and all-time accuracy remain open.
