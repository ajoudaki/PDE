# Independent audit: Tensor Programs IV

Date: 2026-10-11. Scope: supplied ICML 2021 main paper (11 pages, including the final references page) and complete supplied supplement (38 pages). Supplement page numbers below count from its own first page. This is a venue-neutral, unscored source audit in the supervisor's requested single-report format. The papers are public. No submitted code, training, or reproduction was executed.

## Independence, inputs, and coverage

Before this assignment I had read the separate π-limit paper. I had no prior findings on Tensor Programs IV or the other three papers in this assignment, and did not use that earlier reading as evidence here. I did not read study history, prior reports/verdicts, another reviewer's findings, or the manuscript being positioned.

Read completely: `data/generated/compression_literature_positioning_20261011/tp_dmft/tp4_main.pdf` and `tp4_supp.pdf`, through their full extracted text. Visually checked main p. 6 and supplement pp. 10 and 35, where the decisive formulas occur. Supplemental illustrations, experiment descriptions, and all of Appendix N were included in the reading.

A directly cited primary dependency was independently retrieved: [Tensor Programs III, arXiv:2009.10685v3](https://arxiv.org/pdf/2009.10685), dated 8 May 2021. Checked Setup E.2, Assumption E.6, and Theorem E.15 (PDF pp. 29–33). This was a targeted dependency check, not a complete audit of its 87-page proof. The fetched statement agrees with the invoked pseudo-Lipschitz Master Theorem, including that rank stability is not separately required in that version.

The review used review-ai-paper and its severity rubric, solve-math-rigorously, and the canonical-neural presentation instructions. Full reading is distinguished below from independent reconstruction: I reconstructed the shallow updates, linear invariant subspace, first nontrivial transpose response, and smoothing-limit countercalculation; I did not independently rebuild every general-depth classification lemma.

## Assumption ledger

The paper considers a fixed-depth, fully connected network with hidden width \(n\), fixed input dimension \(d\), and scalar output in its main theoretical presentation. In source notation, \(h^1=W^1\xi\), \(x^\ell=\phi(h^\ell)\), \(h^{\ell+1}=W^{\ell+1}x^\ell\), and \(f=W^{L+1}x^L\). The trainable parameter is \(w^\ell\), with \(W^\ell=n^{-a_\ell}w^\ell\), independent Gaussian entries \(w^\ell_{ij}\sim N(0,n^{-2b_\ell})\), and SGD step size \(\eta n^{-c}\). The data sequence and \(\eta\) are fixed independently of width. Singleton batches simplify the statements; finite batches are expressible in the same framework.

For maximal update parametrization, \(c=0\), \(b_\ell=1/2\), \(a_1=-1/2\), \(a_\ell=0\) for hidden matrix layers, and \(a_{L+1}=1/2\). Thus input preactivations and intermediate preactivations have order-one coordinates, intermediate weights have variance \(1/n\), and the readout has entries of order \(1/n\). The limit output at initialization is zero. These are central-limit-scaled intermediate matrices, not an integral-kernel mean-field initialization with variance \(1/n^2\).

Limit existence uses pseudo-Lipschitz \(\phi'\) and a loss derivative continuous in the prediction (Assumptions L.4/N.21). The full dichotomy is restricted further to tanh or the specified smooth ReLU approximation with sufficiently small smoothing parameter (Assumption I.1). Linear activation is explicitly excluded from that dichotomy, and the paper itself gives a linear exception. ReLU is not silently covered by the smooth-activation existence theorem. Every horizon is fixed independently of width. “Stable” bounds may depend on time, input, and training routine; it does not mean global training-time stability.

## Claim 1: rigorous fixed-horizon feature-learning limits

**Location and type.** Main Theorem 5.1, pp. 6–7; supplement Theorem G.4, p. 14; Appendices N.3–N.5, pp. 26–30. Rigorous qualitative width convergence through a cited Master Theorem.

**Claim and evidence.** At each fixed training time and fixed input, the neural output converges almost surely to an expectation of recursively constructed coordinate random variables. Empirical averages of a fixed finite collection of intermediate vectors converge against pseudo-Lipschitz test functions. This specifies more than a forward Gaussian approximation.

**Independent reconstruction.** For the shallow network, let \(U=\sqrt n\,u\), \(V=v/\sqrt n\), and \(f(\xi)=V\phi(U\xi)\). With loss derivative \(\chi_t\), the exact parameter updates are

\[
 nV_{t+1}=nV_t-\eta\chi_t\phi(U_t\xi_t)^\top,
 \qquad U_{t+1}=U_t-\eta\chi_t\xi_t(nV_t)^\top\odot\phi'(U_t\xi_t).
\]

Replacing finitely many empirical averages by the Master Theorem gives Theorem 5.1's coordinate recursion and \(\mathring f_t(\xi)=\mathbb E[Z^{nV_t}\phi(\xi Z^{U_t})]\). Products and compositions remain pseudo-Lipschitz of some finite degree; a continuous scalar loss derivative is permitted by the special scalar-only clause. Fixed Gaussian initialization and a finite unrolled training graph meet the checked dependency hypotheses.

**Dependency verdict.** Valid invocation for this fixed-program conclusion: TP III Setup E.2 matches independent Gaussian matrices/vectors and convergent scalar arguments; Assumption E.6 matches L.4; E.15 supplies the stated almost-sure empirical-moment and scalar convergence. Its proof was not independently re-proved here. The exact degree-addition claim about compositions in supplement p. 21 is inaccurate, but closure at some finite degree, which is what this invocation needs, survives.

**Plausibility / soundness.** Highly plausible; checked shallow derivation and general finite-program invocation are sound. Some displayed specialized recursions need the corrections in Claim 2. No finite-width quantitative remainder, approximation relative to a realized initialization discrepancy, uniform-in-time estimate, or interchange with a fitted endpoint follows from E.15. The paper explicitly acknowledges fixed width-independent training time in Appendix A, pp. 1–2, so that limitation is not an author error.

## Claim 2: the Gaussian-plus-response mechanism is necessary, but the displayed backward sum is incomplete

**Location and type.** Supplement F.2, Eqs. (28)–(33), pp. 10–14; especially Theorem F.2, p. 10. Claimed exact limiting recursion.

**Surviving mechanism.** For an iid Gaussian matrix \(W\), reusing \(W^\top\) in backpropagation produces a response term. The elementary test \(WW^\top z\) contains the diagonal contribution \(z_i\sum_jW_{ij}^2\to z_i\), which would disappear if the backward matrix were independently resampled. The source's distinction between its deliberately decoupled model in F.1 and normal SGD in F.2 is valid and explicitly stated. The Gaussian component alone is not the trained preactivation law.

**Countercalculation to the printed F.2 recursion.** The backward response in F.2 is written as a sum over \(r=0,\ldots,t-1\), and \(Z^{d\bar h_t}\) is described as a function only of \(\widehat Z^{Wx_0},\ldots,\widehat Z^{Wx_{t-1}}\) and the initial readout. But

\[
 Z^{d\bar h_t}=Z^{nV_t}\,\phi'(Z^{\bar h_t})
\]

depends on the current forward Gaussian \(\widehat Z^{Wx_t}\) through \(Z^{\bar h_t}\). In the allowed example \(\phi(z)=z^2\), at \(t=1\),

\[
 Z^{nV_1}=Z^{nV_0}-\mathring\chi_0(Z^{\bar h_0})^2,
 \qquad
 \mathbb E\frac{\partial Z^{d\bar h_1}}
 {\partial\widehat Z^{Wx_1}}
 =2\mathbb E Z^{nV_1}
 =-2\mathring\chi_0\,\mathbb E(Z^{\bar h_0})^2.
\]

Choose a nonzero input and squared loss with a nonzero target, so that \(\mathring\chi_0\ne0\). This coefficient is nonzero. The source's own general ZDot rule therefore contributes this coefficient times \(Z^{x_1}\) to \(Z^{W^\top d\bar h_1}\), while the printed F.2 sum omits it. The current \(x_1\) generally has a new random component and cannot be absorbed into its older \(x_0\) term.

**Verdict L1.** The F.2 formula as printed is clearly false. This is a localized **Minor Flaw** under the rubric: include the current-time forward Gaussian and extend that backward-response index through \(t\); the correct general ZDot construction already supplies the repair, and the qualitative theorem remains unchanged. It would materially alter an implementation copied literally from F.2. The independent forward/backward Gaussian innovations and the general Tensor Program result are not disproved by this indexing defect.

## Claim 3: the supplied smooth-ReLU classification proof uses false auxiliary limits

**Location and type.** Supplement N.7.1–N.7.2, pp. 34–36, especially Proposition N.43 and Theorems N.40/N.44/N.45. Auxiliary derivative estimates support the non-kernel half of the classification theorem.

**Exact check.** The source defines

\[
 \phi_\sigma(z)=\tfrac12z\operatorname{erf}(z/\sigma)
 +\frac{\sigma}{2\sqrt\pi}e^{-z^2/\sigma^2}+\tfrac12z,
 \quad
 \phi_\sigma''(z)=\frac{1}{\sqrt\pi\sigma}e^{-z^2/\sigma^2}.
\]

For \(Z\sim N(0,q)\), \(q>0\), direct Gaussian integration gives

\[
 \mathbb E\phi_\sigma''(Z)^2
 =\frac{1}{\pi\sigma^2}\left(1+\frac{4q}{\sigma^2}\right)^{-1/2}
 =\frac{1}{\pi\sigma\sqrt{\sigma^2+4q}}
 \longrightarrow+\infty.
\]

Proposition N.43 instead says this quantity tends to zero. Moreover,

\[
 (\phi_\sigma^2)''=2(\phi_\sigma')^2+2\phi_\sigma\phi_\sigma'',
 \qquad \mathbb E(\phi_\sigma^2)''(Z)\longrightarrow1,
\]

because \(\phi_\sigma'\to\mathbf1_{z>0}\), while the second term is confined to a boundary layer of width \(O(\sigma)\) and has vanishing expectation. The same boundary-layer calculation gives \(\mathbb E[(\phi_\sigma^2)''(Z)(\phi_\sigma'(Z))^2]\to1\), not zero. These contradict three of the proposition's claimed limits.

The issue is used downstream, not merely stated in passing: Theorem N.45 treats \(\gamma_{22}=\mathbb E\phi''(Z)^2\) as tending to zero to discard its product with a preceding-layer derivative. Once its true divergence is restored, the vanishing of the other factor alone does not determine the product. A quantitative rate is necessary. The basic boundary-layer estimates suggest a repair: \(\gamma_{22}=O(\sigma^{-1})\), \(\gamma_{02},\kappa_3=O(\sigma)\), \(\kappa_1,\kappa_2=O(1)\), and the negative third-derivative terms have order \(-\sigma^{-1}\). But a complete general-depth repaired induction is not supplied by the printed proof and was not completed in this audit.

There are additional local derivative problems: Lemma N.37 uses independence from a backward Gaussian although \(Z_1^\ell\) contains that Gaussian at nonzero \(\eta\); that independence argument works at \(\eta=0\), not at every \(\eta\) as printed. In the simplest one-layer case \(Z_1=Z_0-\eta V\phi'(Z_0)\), with independent unit-variance \(V\), direct differentiation gives

\[
 \left.\partial_\eta^2\mathbb E\phi(Z_1)^2\right|_0
 =\mathbb E[(\phi^2)''(Z_0)\phi'(Z_0)^2],
\]

whereas Theorem N.40's stated \(C=2(\beta^\ell(0))^2\mathbb E(\dot Z_0^\ell)^2\) yields an extra factor of two for this specialization. Its sign conclusion may survive that factor correction.

**Verdict M1.** Auxiliary statements are clearly false; the full dichotomy conclusion remains plausible. The supplied smooth-ReLU argument has a **Major Flaw** at claim level: repairing the cancellation/dominance proof requires quantitatively rebuilding its derivative induction, while much of the nontrivial TP setup remains reusable. This is not a counterexample to the dichotomy itself, nor a reason to discard the independently supported finite-horizon µP construction. The tanh branch does not use the false \(\sigma\to0\) limits, although the shared derivative identities still require care. I do not certify the complete classification proof as sound from this supplement.

## Claim 4: exact bounded-state reduction survives in the shallow linear special case

**Location and type.** Main Corollary 5.2, pp. 6–7; supplement J.2.2 and Algorithms 2–3, pp. 17–18. Exact algebraic reduction of a special limiting model.

**Independent reconstruction.** Set \(\phi(z)=z\) in the checked shallow recursion. If \(P,Q\) are the independent standard Gaussian initial coordinate labels, write \(Z^{nV_t}=A_tP+B_tQ\), \(Z^{U_t}=C_tP+D_tQ\). The update closes exactly on the four coefficients, and the expectation equals \((A_tC_t+B_tD_t)\xi\). The source's coefficient updates follow directly because both parameter updates are linear combinations of those same initial labels. For input/output dimensions \(d,d_o\), the shared label dimension is \(d+d_o\), giving the deterministic-width \(d+d_o\) representation in Algorithm 3. Bias coefficients also lie in this span when initialized at zero. Gradient norms used for clipping are recovered by the orthonormal limiting label covariance.

**Cost.** Derived from the displayed arrays, this representation stores order \((d+d_o)^2\) coefficients, plus biases and workspace, independent of training history length. A dense batch forward/backward pass costs order \(B(d+d_o)^2\). This is a real fixed-state exact limit, but only for that linear architecture. For Word2Vec, \(d=d_o=|\mathcal V|\); the state is consequently quadratic in vocabulary size, not universally small.

For general deep nonlinear networks, Appendix H, supplement p. 15, explicitly identifies nested nonlinear Gaussian expectations, growing covariance matrices, and response coefficients. It reports at least quadratic-in-step covariance storage in the generic deep case and computationally expensive nested integration. Its exponential discussion concerns its explicit analytic expansion route; it is not a proved lower bound excluding every alternative approximation algorithm. No history compression, uniform-time numerical error control, or constant-dimensional general nonlinear closure is provided.

**Verdict.** Highly plausible; the linear invariant-space argument and coefficient cost are sound. Novelty is nontrivial within this source's formulation, but no exhaustive historical priority search was conducted. Extending this exact finite representation to a nonlinear deep network would change the claim and is unsupported here.

## Claim 5: the experiments support restricted feature-learning comparisons, not endpoint approximation guarantees

**Location and evidence.** Main Tables 2–3, p. 8, and supplement J, pp. 16–20. Omniglot uses one-hidden-layer linear µP networks and first-order MAML. Selected settings train for 100 epochs of 100 batches of 32 tasks; meta-test adaptation uses 20 steps. Reported µP accuracy is 66.42±0.19%, compared with ReLU NTK 47.82±0.04% and ReLU GP 47.60±0.02%. Finite linear width-512 accuracy is 66.43±0.23%, so the results do not establish strict infinite-width superiority over every finite width. Word2Vec reports 43.31%/56.45% for µP on text8/fil9 versus 42.56%/55.69% at width 1024. Its NTK baseline addresses the specified discarded-readout embedding analogy task, not every possible transfer protocol.

The controlled nonlinear validation in supplement Figure 6, p. 16, uses polynomial activations and only a few training steps because of the admitted cost. It compares loss curves at widths 1024/4096 over 100 seeds; it is useful fixed-horizon evidence, not a numerical proof of all-time convergence.

**Concern L2.** Supplement p. 18 footnote 42 says the final 15-seed Omniglot rerun excludes outliers at least one standard deviation from the mean. That selection changes both the reported mean and dispersion. A complete unfiltered rerun summary is needed to interpret the stated uncertainty. This is a **Minor Point** for the large kernel-versus-feature-learning separation but limits small finite-versus-limit comparisons; the latter already overlap numerically.

**Verdict.** The principal restricted empirical comparison is plausible. No code was inspected or executed, and accuracy was not independently reproduced. Training to a selected finite epoch is not an endpoint theorem. The source makes no verified exchange of \(n\to\infty\) with \(t\to\infty\), no norm bound relative to a coupled seed discrepancy, and no history-truncation guarantee.

## Severity triage and overall assessment

| ID | Affected claim | Severity | Dependency and surviving result |
|---|---|---|---|
| L1 | Printed Theorem F.2 backward-response recursion | Minor Flaw | Current-time response omitted; repaired locally by the general ZDot rule. Existence/mechanism survives. |
| M1 | N.43–N.45 smooth-ReLU classification argument | Major Flaw | False asymptotics enter the dominance proof; quantitative derivative induction needs repair. Fixed-program µP convergence and shallow linear reduction survive. |
| L2 | Selected Omniglot uncertainty summary | Minor Point | Outlier deletion limits uncertainty interpretation; large kernel gap survives as reported empirical evidence. |

The important surviving contribution is a rigorous fixed-horizon framework for central-limit-scaled feature-learning networks, including reuse-of-weights response effects and an exact finite coefficient model for shallow linear networks. The supplied supplement should not be cited as an error-free proof of every displayed recursion or classification lemma. Nor does its valid qualitative limit become a quantitative all-time, seed-coupled compressed surrogate. Confidence is high in the explicit countercalculations and linear reconstruction, moderate in the general theorem application, and limited on a fully repaired general-depth dichotomy proof and unexecuted empirical results.
