# MFP: a constructive calculus for nonlinear neural response

Reassessment of 11 October 2026. This document supersedes the first synthesis, preserved as [literature_review_v1.md](literature_review_v1.md). The target remains the unchanged `paper_MFP/main.tex` and bundled compiler. The question is the scientific contribution of the master theorem and calculus, rather than priority for a proof technique. The manuscript has not been edited.

## The strongest defensible case

**MFP makes a declared class of nonlinear neural-response calculations into a uniform symbolic calculus.** The user specifies a finite neural program and an admitted observable, derivative, gradient contraction, update or initial flow-jet request. The calculus proves exact finite-width compilation, constructs the Gaussian expectation graph for its width limit, and implements that construction through the same general rules. The contribution includes a mathematical closure theorem and an output reduction, as well as executable software.

For the standard smooth Gaussian MLP with squared loss, the initialization result is particularly concrete: **every fixed-order initial moving-flow jet of admitted outputs, losses and feature kernels reduces to sums and products of activation-derivative moments under the original forward-pass covariances. Each such integral uses at most the number of sample inputs in the program, independently of derivative order and depth.** The number of terms, derivative orders, coefficient expressions and retained source records can grow. This is a statement about the final activation integrals, not an efficiency theorem.

That is the positive scientific point the previous framing did not develop. A reader can change an admitted observable or derivative order while using the same probabilistic and symbolic construction. Matrix reuse, the gradient metric, shared sample parameters and moving residuals remain part of the calculation. The output is determined from the supplied network/data/activation specification; it does not require an unknown trained neural distribution as an additional input.

There is also a precise boundary to the originality claim. Tensor Programs already supplies the constructive Gaussian source-response evaluator and a broad derivative/backpropagation framework. MFP does not discover a new limiting law for its compiled primitive programs. Its additional explicit statements concern the declared derivative-query language, exact closure and state semantics, the initialization moment reduction, and their executable realization. These results justify describing MFP as **a mathematical foundation for systematic symbolic neural-response calculations in its stated regime**. The evidence does not establish that it inaugurates a new probabilistic universality class or is the first general theory of wide-network learning.

## What changed in the reassessment

The first pass had real proof and source checks, but its synthesis was too dominated by rejecting broad priority claims. It did not sufficiently distinguish a constructive primitive limit theorem from a complete user-level derivative calculus; it treated the normal-form restriction mainly as a limitation without showing the important family it contains; and it omitted a close recent implementation.

The reassessment therefore made substantive changes:

1. A fresh comparison reconstructs the exact embedding into TP IVb and the finite algebra still required for an arbitrary MFP query. It distinguishes genuinely additional closure/reduction statements from already available constructive probability.
2. A fresh manuscript/code assessment verifies that arbitrary fixed-order moving jets belong to the general API. The kernel example is an application of that API, rather than a special order-two differentiation implementation.
3. The initialization specialization and its integration-dimension bound are derived explicitly and submitted to a separate isolated mathematical check. This strengthens the explanation of an existing result; it does not silently extend the manuscript's general trained-state normal form.
4. The shortlist now includes the complete ICML 2026 *Finite-Width Neural Tangent Kernels from Feynman Diagrams* and its NTK Unlimited software. It also includes the updated nonlinear DMFT treatment and the recent quantitative Tensor Programs follow-up. These were absent from the first synthesis.
5. The proposed introduction is rebuilt around the calculation problem, the required answer and the exact reduction. Prior work is compared by its actual input, guarantee and output, rather than by a binary “has derivatives / has Gaussian expectations” checklist.

The independent reassessments are [TP IVb](reassessment_tp4b.md), [MFP calculus and code](reassessment_calculus.md), [discovery and NTK Unlimited](reassessment_discovery.md), [DMFT](reassessment_dmft.md), [quantitative TP](reassessment_quantitative_tp.md), and [initial-jet normal form](reassessment_normal_form_check.md). Earlier complete-paper and independent proof reports remain evidence; they are not replaced by more favorable wording.

## The question motivated by the user's examples

The natural scientific objects are the finite MLP's predictions, loss and learned feature kernels. Write $L$ for hidden depth, $m$ for sample count, $d$ for input dimension and $n$ for width. For the manuscript's zero-bias neural specialization,

$$
z_a^{(1)}=W^{(1)}x_a/\sqrt d,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi(z_a^{(\ell)}),\qquad
f_{n,a}=W^{(L+1)\top}h_a^{(L)}/n.
$$

The hidden recursion is for $2\le\ell\le L$. First-layer entries are independent $N(0,1)$, hidden entries $N(0,1/n)$, and stored-readout entries $N(0,\tau^2)$ for fixed $\tau$. All blocks are independent. For loss $\mathcal L_n=m^{-1}\sum_a(f_{n,a}-y_a)^2$, use block mobilities $n\kappa_1,\kappa_2,\ldots,\kappa_L,n\kappa_{L+1}$ with fixed positive factors. The supplied kernel example uses half this loss; its physical clock is correspondingly different.

A representative request is

$$
K_{n,ab}^{(\ell)}(t)=\frac{h_a^{(\ell)}(t)^\top h_b^{(\ell)}(t)}n,
\qquad
J_{r,ab}^{(\ell)}=
\lim_{n\to\infty}\mathbb E\left[
\frac1{r!}\frac{d^r}{dt^r}K_{n,ab}^{(\ell)}(0)\right].
$$

The same question applies to $f_{n,a}$, $\mathcal L_n$, and admitted gradient contractions. The direction of differentiation is the gradient field of the entire batch. Its dependence on predictions, residuals and parameters must be differentiated. Arbitrary fixed correlated or repeated inputs are allowed. Symbolic geometry is encoded by coefficients on shared trainable first-layer columns, and labels by scalar symbols. Merely assigning a desired covariance to separately trainable sample preactivations would change the gradient metric and therefore the requested object.

A satisfactory calculus needs all of the following: a noncircular accepted language; exact expansion of the actual finite derivative; termination within a probabilistically controlled class; explicit covariances and matrix-reuse response terms; expectation convergence; and an implementation whose operations match these definitions. No single checkbox proves the whole result. Conversely, a prior work that supplies several of these components deserves full credit for those components.

The user's philosophy is strongest when stated this concretely. “Make mean-field neural response calculable by a uniform symbolic procedure” identifies the problem and the advance. “No previous theory can describe nonlinear feature learning” is false. “Any neural expression whatsoever” exceeds the declared grammar. The introduction should keep the former motivation and replace the latter possible interpretations with the actual theorem.

## What the master theorem and reduction accomplish

The primitive language has typed vector populations, iid Gaussian neuronwise root tuples, independent named Gaussian matrices, coordinate expressions in activation derivatives, polynomial arithmetic and normalized averages. A transpose uses the original matrix. The activation is $C^\infty$ and every derivative has polynomial growth. Program length, depth, data dimensions, derivative order and update count are fixed before $n\to\infty$. These assumptions give a substantial family while excluding arbitrary tensor contractions, dense arbitrary matrix directions, width-dependent coefficients and global shared random scalar roots.

For every admitted derivative query, exact finite rules first produce a primitive program. The Gaussian evaluator then returns

$$
I_j=\int F_j(g;I_1,\ldots,I_{j-1})\,
       N(0,K_j(I_1,\ldots,I_{j-1}))(dg),
\qquad O_*=P(I_1,\ldots,I_N),
$$

and proves $\mathbb E|O_n-O_*|^p\to0$ for every finite $p\ge1$, together with uniform moments and joint empirical laws. The integrands, covariance entries and coefficients are produced by the rules. A general integrand can contain nested nonlinearities; the statement that $P$ is polynomial does not eliminate that complexity.

For standard initial neural jets with polynomial loss, the stronger reduction does constrain the integrands. The detailed argument is in the [calculus reassessment](reassessment_calculus.md) and [independent specialization check](reassessment_normal_form_check.md). Its essential steps are:

1. Every activation node starts at an original preactivation. Differentiating $\phi^{(q)}(z_a^{(\ell)})$ produces $\phi^{(q+1)}(z_a^{(\ell)})Dz_a^{(\ell)}$. Products, averages, reverse adjoints and represented matrix actions preserve this form.
2. The polynomial-loss gradient field belongs to this class. Repeated moving Lie differentiation $O_{r+1}=DO_r[V]$ therefore stays in it, including all derivatives of $V$ and residuals.
3. Gaussian compilation gives polynomials in finitely many Gaussian sources multiplied by activation derivatives only at the original preactivations. Stein reduction removes the explicit Gaussian polynomial factors and terminates by degree.
4. The remaining nonlinear arguments on layer $\ell$ are the original $m$ Gaussian preactivations, whose covariance is

$$
\Sigma^{(1)}_{ab}=x_a^\top x_b/d,\qquad
\Sigma^{(\ell+1)}_{ab}
=\mathbb E_{Z\sim N(0,\Sigma^{(\ell)})}\phi(Z_a)\phi(Z_b).
$$

Thus the final atoms have the form

$$
\mathbb E_{Z\sim N(0,\Sigma^{(\ell)})}
  \prod_{j=1}^{k}\phi^{(r_j)}(Z_{a_j}).
$$

Repeated factors at a sample do not add coordinates. Auxiliary-source covariances become recursively determined coefficients, themselves reduced by the same earlier-node induction. Cross-layer contributions combine through scalar sums and products. The result is a finite expression over this layerwise activation-moment algebra.

This is the concrete structural simplification worth highlighting. High-order derivative fields need not be Gaussian; they are eliminated from the final integration variables in this subclass. The conclusion does not require generic covariance inverses, orthogonal inputs, a frozen tangent kernel or a frozen gradient direction. These properties are capabilities shared in part with TP, not automatically new priority claims.

The bound of $m$ applies to final activation integrals for the stated standard MLP provenance. General updated-state nonlinearities, nonlinear functions of derivative fields, additional populations or arbitrary nonpolynomial losses need their own check and generally remain in the broader graph. It is not a bound on source storage, graph size, polynomial degree, running time or total number of Gaussian moments. The compiler's declared-preactivation mode performs rebasing and coordinate pruning; the caller must identify genuine original preactivations. A successful type check cannot prove an arbitrary user's analytic activation assumptions or architecture interpretation.

## Complete shortlist and realistic comparison

The shortlist is selected by substantive overlap. “Read completely” means the specified primary version and its appendices were read by the assigned reviewer; it does not mean every external dependency was verified or every experiment reproduced. Exact locations and qualifications are in the linked reports.

| Work | Complete source coverage | What it actually contributes and how it compares |
|---|---|---|
| Yang, **Tensor Programs III** | All 87 pages of arXiv v3, A–N; relevant version comparisons. [Audit](review_tp3.md). | Constructive source-response law, reuse, transposes, singularity and scalar feedback. These are direct foundations, not difficulties that MFP first resolves. The earlier audit did not independently complete every Appendix N estimate; the later TP IVb route covers the fixed-input comparison. |
| Golikov–Yang, **Non-Gaussian Tensor Programs** | Entire 13-page proceedings paper and 33-page supplement; corrections/version checks. [Audit](review_nongaus.md). | Raw-entry moment bounds and smooth-program all-$L^p$ background. The literal initial-scalar hypothesis needs uniform moments, and the printed scalar-chain backpropagation has an error. Fixed deterministic MFP scalars avoid the first problem; Gaussian convergence plus the checked moment appendix avoids the defective interpolation branch. |
| Yang–Hu, **Tensor Programs IV** | Main 11 pages, supplement 38 pages, latest arXiv v3 65 pages. [Audit](review_tp4.md). | Same feature-learning normalization after parameter rescaling; explicit training-program construction and selected response derivatives. Its fixed-step evaluator is a real predecessor. Errors in a separate classification calculation do not remove that construction. |
| Yang–Littwin, **Tensor Programs IVb** | All 87 pages of v2, complete v1/v2 comparison; fresh direct MFP mapping. [Reassessment](reassessment_tp4b.md). | A broader primitive language, constructive backpropagation and all-$L^p$ theorem. MFP's compiled queries are inside its smooth Gaussian scope. The complete moving-jet/rank-contraction/normal-form contract still requires the additional finite arguments specified below. |
| Huang–Yau, **Neural Tangent Hierarchy** | Conference main 10 pages and complete 39-page arXiv v1, A–C. [Audit](review_nth.md). | Exact derivative hierarchy and a stronger positive-time approximation objective under its NTK scaling and conditioning assumptions. Independent checks found gaps in printed time estimates and a false probability bound; exact hierarchy identities survive. MFP's finite jets do not establish that positive-time theorem. |
| Chen–He–Su, **Label-Aware NTK** | All 32 pages of camera-ready v2, A–D; proceedings/version comparison. [Audit](review_lantk.md). | Recursive symbolic NTH construction, shallow Gaussian expressions and label-dependent kernels. Strong prior evidence against firstness for derivative recursions or symbolic labels. Specific Gaussian coefficients and singular/ReLU manipulations need correction; the exact smooth recurrence remains useful. |
| Dyer–Gur-Ari, **Feynman diagrams** | Entire 37-page arXiv v1, A–E. Final ICLR comparison remains incomplete. [Audit](review_feynman.md). | General contraction organization, finite-width corrections and derivative hierarchies; nonlinear breadth varies by theorem. Its polynomial calculations give explicit coefficients. Smoothness without integrability is insufficient, and a discrete correction has an index error with a direct repair. |
| Aitken–Gur-Ari, **Polynomial activations** | Entire 20-page v1, A–D. [Audit](review_feynman.md). | A genuine polynomial correlation-scaling theorem and exact Wick coefficients. Can recover matched polynomial MFP cases and retain finite-width terms MFP discards. Verified local normalization/coefficient errors do not refute the corrected main counting mechanism. |
| Guillen–Misof–Gerken, **Finite-width NTKs / NTK Unlimited** | Entire 53-page ICML 2026 proceedings version, A–K; pinned source inspection. [Reassessment](reassessment_discovery.md). | Implemented symbolic Gaussian processing and numerical compilation for prescribed preactivation/NTK/dNTK/ddNTK recurrence tensors. Arbitrary width-expansion order differs from arbitrary physical derivative order. The shipped recurrence list and NTK normalization differ substantively from MFP's query input and feature-learning flow. |
| Bordelon–Pehlevan, **Self-consistent dynamical field theory** | Updated JSTAT 2023 article, all 70 pages plus cover, and conference comparison. [Reassessment](reassessment_dmft.md). | Nonlinear feature-learning sources, response kernels and a numerical self-consistency procedure. A major mathematical/computational antecedent; a history-dependent dynamical solver answers a different question from finite derivative compilation. Precise formal, discrete and continuous-time proof status is recorded in its audit. |
| Agazzi–Mosig García–Trevisan, **Quantitative Gaussian-Process Limits of Tensor Programs** | Complete 37-page arXiv v1. [Reassessment](reassessment_quantitative_tp.md). | Quantitative joint Wasserstein and kernel scalar-$L^p$ rates, including a kernel-feedback extension. Its Lipschitz and nondegeneracy assumptions and absence of transpose operations prevent direct substitution for MFP's derivative language. Stronger quantitative conclusions on overlap must be credited. |
| Novak et al., **Neural Tangents** | Entire 19-page paper, A–D; pinned software inspection. [Audit](review_software.md). | Automatic supported NNGP/NTK kernels, numerical tools and arbitrary-order finite Taylor expansions. A strong architecture/AD precedent with wider engineering capabilities; these APIs do not by themselves compose into the inspected MFP source-response derivative compiler. |

Tensorgrad is an additional software comparator: it already combines symbolic tensor AD and Gaussian mean/covariance algebra, and small moving-derivative calculations were executed. GP4A and NTK4A provide authors' architecture examples. The [discovery report](reassessment_discovery.md) records other screened sources and reading levels, including finite-head attention, infinite-depth parameterizations, general AD compilers and hardware tensor compilation. Those are screening/background entries, not fully audited additional shortlist papers or grounds for universal absence claims.

## The decisive comparison with Tensor Programs

A weak comparison would say that TP proves existence while MFP supplies calculation. That is incorrect: TP IVb Definition 2.6.5 already gives the Gaussian evaluator; Definition 2.9.14 explicitly gives backpropagation, including scalar averages; the update formulas already preserve named initialized matrices. Another weak comparison would say that applying TP leaves no mathematical content for MFP. That ignores the exact compilation and normal-form theorems and the complete software interface.

The [fresh mapping](reassessment_tp4b.md) identifies the remaining work for a user asking for the initial $R$th kernel jet:

- Encode the actual shared finite parameters, loss, initialization and gradient metric.
- Represent matrix gradients/directions as finite normalized rank sums, with all transpose occurrences counted; lower their actions and contractions exactly.
- Prove fixed-order closure while differentiating residuals, coefficients and the moving direction. Distinguish ambient updated-state gradients from differentiation through training history.
- Apply the prior Gaussian evaluator and verify smoothness and uniform-moment hypotheses for the expanded program.
- Prove and execute the restricted activation-moment reduction, with source naming, expression sharing, covariance dependencies and inspectable output.

MFP makes this into one specified construction. The closure proof is a finite induction using familiar calculus; the reduction is a terminating Stein induction. Their brevity does not make their semantic content disappear, but neither does stating them create a new probability principle. TP IVb's theorem covers the lowered primitive programs with the same Gaussian response rule and, with the checked moment bounds, the required expectation limits. No admitted MFP query was identified that needs a probabilistic mechanism beyond this prior machinery.

The [DMFT reassessment](reassessment_dmft.md) gives a useful exact bridge. For the finite-width training field $V_n$, take $q$ Euler updates with independent formal step sizes, $\theta_j=\theta_{j-1}+\varepsilon_jV_n(\theta_{j-1})$. The mixed derivative $\partial_{\varepsilon_1}\cdots\partial_{\varepsilon_q}O_n(\theta_q)$ at zero is exactly $(D[\,\cdot\,][V_n])^qO_n(\theta_0)$, the unnormalized moving-flow jet. Thus fixed initial jets do not require a new continuous-time stochastic theory: finite differentiation followed by a primitive program theorem already gives a route. MFP specifies its closure, moment control, symbolic reduction and implementation as one calculus. This bridge is a deduction in the review, rather than an all-order compiler theorem claimed in the DMFT article.

TP IVb's broader claims are not granted wholesale credit. Its slow-initial-scalar proof is explicitly deferred; its general non-Gaussian outer-product extension and general-architecture limits have compressed or omitted adaptation arguments. Those broader gaps are outside the route actually needed for MFP's fixed deterministic inputs and Gaussian coordinate/average sublanguage. The comparison uses that route, with assumptions verified, rather than the strongest words in its title.

The meaningful positive positioning is therefore **a constructive neural derivative calculus built on program-limit theory, with a proved activation-moment output algebra and an executable general query interface**. Calling this “only implementation” is inadequate. Calling it a first general Gaussian master theorem is also unsupported. The significance should come from the problem the complete calculus solves, not from either extreme label.

## Differences that really matter

**Input to the algorithm.** NTK Unlimited compiles supplied recurrence tensors. MFP takes the neural program and a derivative request, forms the finite derivative expression and derives its limit graph. Its general `jets(..., moving=True)` operation is used directly by the kernel producer. Increasing the requested order does not require adding a new differentiation rule to the engine. Building a different depth/batch still requires the corresponding typed network builder; a general architecture parser is not shipped.

**Training regime.** The MFP examples retain the mean-field metric in which hidden features can move at leading order. A finite number of $1/n$ corrections around an NTK-scaled frozen leading kernel does not establish that different leading-order flow. This is a substantive model distinction against NTK perturbation approaches. It is not a distinction against TP IV/IVb or the feature-learning DMFT framework, which already treat the same kind of scaling.

**What is reduced.** Generic symbolic AD can differentiate a finite matrix expression, and generic Gaussian algebra can integrate many resulting tensors. MFP's source-response transformation also removes the growing-width matrix computation. In the initial-jet subclass its terminating reduction leaves only ordinary layerwise activation moments. The argument for significance is this full transformation and its scope, not the invention of AD or Gaussian integration.

**Singular inputs.** MFP's theorem and compiler retain singular Gaussian laws and separate formal slots. TP already has the corresponding mathematical coverage. NTK Unlimited's inspected `G1`/`F` paths explicitly invert the Gram matrix, and its density integration lacks a general singular-support treatment; optional regularization is not a theorem proving the singular limit. This is a concrete implementation difference, not proof that its formulas admit no singular extension.

**Guarantees versus useful evidence.** MFP proves all finite scalar $L^p$ limits in its declared class. A formal width expansion or a numerical self-consistency calculation is not the same guarantee. Conversely, MFP supplies neither finite-width error rates nor a numerical integrator or positive-time reconstruction. The quantitative TP result, diagram methods and DMFT supply different kinds of information that should not be made to look weaker by asking only MFP's question.

## Proof scrutiny: what the adverse evidence changes

The strongest criticisms have exact locations, reconstructions and independent checks in the original reports and [independent_proof_checks.md](independent_proof_checks.md), [independent_formula_checks.md](independent_formula_checks.md). They must affect only the claims they actually invalidate.

- NGTP's literal scalar-input moment assumption and printed scalar-chain reverse rule require repair. Later TP IVb explicitly supplies uniform initial moments and scalar adjoints; its Gaussian-plus-moments route remains a valid antecedent for MFP.
- NTH's printed long-time proof drops differentiated residual terms and includes an incompatible Gaussian-tail claim. This limits certification of that quantitative proof, not the exact hierarchy or the general usefulness of higher-order response calculations.
- TP IV's particular small-smoothing/classification calculation contains false derivative factors and asymptotics. An independently checked one-layer repair retains the intended nonzero cubic response. These faults do not invalidate the fixed-history Gaussian evaluator.
- LANTK's special shallow Gaussian/ReLU manipulations have concrete coefficient, rotation and repeated-input problems. The general smooth finite symbolic recursion remains a predecessor. A kernel proposal supported by experiments is not a proved general nonlinear flow compiler.
- Dyer/Aitken contain local normalization, summation and example-coefficient errors. In the quadratic example, the exact mean coefficient is 192 instead of 132, and the correctly applied variance corollary gives the correct order $n^{-2}$. Correcting these examples preserves the main polynomial contraction mechanism.
- The new ICML 2026 paper's all-order diagrammatic completeness and analytic remainder dependencies are not fully certified here. Its diagonal homogeneous-activation NTK-mean conclusion nevertheless has an independent exact row-sign-symmetry proof in the [new report](reassessment_discovery.md). A printed minus sign in its Gaussian derivative-square mean is repairable. A formal-series criticism alone would have unfairly dismissed a correct exact conclusion.
- The quantitative TP proof recovers a common Gaussian innovation by standardizing a residual that can vanish with positive finite-width probability; its printed equality then fails. Retaining the coupling's original innovation and consistently normalizing the Gram coefficients repairs the step under the stated hypotheses. Its LayerNorm examples also need a different permitted encoding. The [complete assessment](reassessment_quantitative_tp.md) gives these repairs and preserves credit for the quantitative rates; none is a counterexample to those rates.
- DMFT's explicit linear perturbation shortcut in journal (P.2)–(P.4) drops the layer dependence of the leading response operators. For two hidden linear layers and half-mean squared loss, it gives a last-hidden-kernel $t^2$ coefficient $4\lambda_a\lambda_b$, where $\lambda_a=m^{-1}\sum_bK^x_{ab}y_b$. The full response equations (F.2)–(F.4) instead give $9\lambda_a\lambda_b$, agreeing with direct finite-network differentiation and MFP. The [separate isolated check](reassessment_dmft_linear_check.md) reconstructs this discrepancy and the clock conversion. This invalidates the shortcut in that case, not the full DMFT law or every nonlinear perturbation construction. Separately, the continuous-time limit remains an acknowledged proof obligation; the discrete TP connection supplies genuine fixed-history rigor.

These findings support a level comparison. They do not justify treating every earlier theorem as proved exactly as advertised; they also do not transfer novelty to MFP when the valid or explicitly repaired antecedent already supplies the relevant mechanism. The new DMFT and quantitative-paper reports apply the same distinction between source claims, complete reading and independently checked arguments.

## Recommended introduction and related-work framing

The opening should ask how to calculate nonlinear neural response systematically. It should then state what counts as an answer: a declared query language, exact derivative semantics, a finite explicit Gaussian graph, and expectation correctness. The master theorem and the initial-jet moment algebra should come before a long list of qualifications or a priority discussion.

A forceful, defensible central sentence is:

> MFP turns finite-order nonlinear neural response into a constructive symbolic calculus: every admitted derivative query is reduced, with a proved width-limit interpretation, to a finite Gaussian calculation; for initial polynomial-loss MLP jets, the calculation closes in activation-derivative moments at the original forward covariances.

The conceptual significance follows from the next sentence:

> This allows the observable and derivative order to vary while the mathematical rules and compiler remain fixed, preserving shared parameters, changing gradient directions and the dependence created by matrix reuse.

Use “foundation” for this precisely identified calculus if desired. Avoid an unsupported claim that the whole field previously lacked a Gaussian-response theory. Credit TP as a constructive predecessor at the point its semantics enter. Compare NTK Unlimited at the level of supplied recurrences versus derived derivative queries, and distinguish DMFT's dynamical solution target from initial response coefficients. Describe the polynomial diagram subclass as an actual overlapping capability, not merely an exponent bound. These choices make the strongest case without relying on omissions or inflated contrasts.

The proposed text is separate: [introduction](proposed_introduction.tex), [related work](proposed_related_work.tex), [bibliography](references.bib), and [LaTeX wrapper](proposed_framing.tex). The manuscript remains unchanged. Detailed disputed proof findings belong in the audit record rather than dominating the opening argument.

## Validation, cost and remaining limits

The first review reran all 72 bundled MFP tests and the worked example producers. The fresh calculus assessment again passed the 72 tests and added two targeted independent checks: an exact moving flow with scalar feedback through order six, and reduction of five shared Gaussian root columns to one preactivation integration coordinate. Source, commands, outcomes and hashes are linked from [reassessment_calculus.md](reassessment_calculus.md). These checks support the general API and the reduction mechanism; they are not a formal proof of every Python execution or a fresh independent reconstruction of every long kernel coefficient.

No comparative performance benchmark, new training campaign, or formal Lean proof was performed. The number of graph nodes, moment atoms and algebraic terms can grow rapidly. The normal-form dimension bound is useful mathematical structure, not a total-cost guarantee. Neither arbitrary symbolic PSD factorization nor natural-language/LaTeX query parsing is provided. Symbolic geometry factors and labels are supported; direct root covariance declarations require concrete PSD data.

Complete accessible versions of the retained shortlist were read. The earlier inaccessible final ICLR copies for Dyer and TP IVb, and the unavailable separate final NTH conference appendix, remain version-comparison limits; the full specified arXiv versions were used. Some external all-order, ReLU and spectral dependencies remain explicitly unverified. Newer screening entries are not silently treated as audited theorem exclusions. The absence of an equivalent package is bounded by inspected documented interfaces and pinned source paths.

This reassessment changes the scientific explanation of MFP's contribution while preserving the evidence-based boundary: a substantive exact-compilation and symbolic normal-form calculus, with an implementation, whose probabilistic foundation is already present in constructive Gaussian program theory.
