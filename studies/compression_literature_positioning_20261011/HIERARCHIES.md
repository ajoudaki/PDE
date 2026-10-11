# Finite-width closed expansions: bounded public-literature audit

Date: 2026-10-11. Scope: Huang–Yau, Dyer–Gur-Ari, and the explicitly identified training chapters of Roberts–Yaida–Hanin. This is a public-literature positioning audit, not an official, confidential, scored review or a certification of the manuscript. The review-ai-paper skill and its severity rubric guided separation of claim, evidence, proof concern, and scope mismatch; the canonical-notation skill and its neural-network reference guided the translations below. No experiments or manuscript/Git changes were made.

**Version/assessment update.** The access and book-coverage caveats below describe the initial pass, not the final evidence inventory. The user has supplied the final 35-page Dyer–Gur-Ari publication; use `AUDIT_DYER_FINAL.md` for that version. The complete 471-page book has now received a fresh source-only audit; use `AUDIT_EFFECTIVE_THEORY.md`. The Huang–Yau attachment duplicates the already read proof version, and the official proceedings page exposes no separate supplement. A separate missing final supplement is not presumed to exist. The coordinator's integral repair below supersedes the initial unresolved status of the differential-majorant concern.

## Bottom line

Three corrections are essential to a fair positioning statement.

1. Finite autonomous, initialization-dependent training closures predate the present manuscript. Huang–Yau is not the only candidate: Dyer–Gur-Ari Appendix E.4 and Roberts–Yaida–Hanin Chapter ∞ provide closely related finite-order closed dynamics. The book also explicitly derives the fully trained prediction of a particular initialized network, before taking ensemble averages.
2. The present manuscript's literal-array cost `n^{Theta(log m)}` is a result about its separately specified short-time, deep-linear, zero-readout feature-learning benchmark. It is not a storage lower bound for Huang–Yau's original Gaussian-readout NTK parameterization. In the latter's fixed-data, fixed-time setting, its stated error bound improves by inverse powers of width at each fixed truncation rank. Transferring the manuscript's required rank to that model would be invalid.
3. The defensible distinction is the conjunction of contracts: fixed depth with nonvanishing nonlinear feature learning; coupling to one ordinary finite dense initialization; small retained state with the claimed query domain; a certified complete-trajectory error, including the fitted limit; and comparison with actual independent dense-run variability. None of the audited sources establishes that conjunction. Their different scopes are not defects. In particular, “feature learning vanishes” must be restricted to the fixed-depth infinite-width limit in their scaling, not used to deny their finite-width representation-learning corrections.

## Sources, versions, and reading coverage

All downloads, extracted text, and rendered mathematical pages are under `data/generated/compression_literature_positioning_20261011/hierarchies/`. Text was read sequentially through the selected complete documents/chapters; truncated retrievals were reread in smaller chunks. Reading a proof in full does not mean every algebraic identity was independently rederived.

| Source | Primary version and exact URL | Coverage and limits |
|---|---|---|
| Huang–Yau, *Dynamics of Deep Neural Networks and Neural Tangent Hierarchy* | [ICML 2020 proceedings PDF](https://proceedings.mlr.press/v119/huang20l/huang20l.pdf), 10 PDF pages; [arXiv:1909.08156v1](https://arxiv.org/pdf/1909.08156v1), 39 pages, submitted 2019-09-18 | Both PDFs read completely, including references and arXiv Appendices A–C. The proceedings main paper is authoritative for the displayed theorem statements; the complete proof audit uses the arXiv version. No later arXiv version is listed in the [version history](https://arxiv.org/abs/1909.08156). A guessed proceedings supplement URL returned 404, so identity with a separate final supplement was not verified. Visually inspected proceedings p. 5, and arXiv p. 31. |
| Dyer–Gur-Ari, *Asymptotics of Wide Networks from Feynman Diagrams* | [arXiv:1909.11304v1](https://arxiv.org/pdf/1909.11304v1), 37 pages, submitted 2019-09-25; ICLR 2020 [official PDF endpoint](https://openreview.net/pdf?id=S1gFvANKDS) | Latest/only arXiv version read completely, including Appendices A–E, figures, and references. The [version history](https://arxiv.org/abs/1909.11304) lists only v1, not an overlooked stronger v2. The official OpenReview PDF and API PDF endpoint returned access challenges/403; equivalence with the final ICLR version remains unverified. The [Google Research primary publication page](https://research.google/pubs/asymptotics-of-wide-networks-from-feynman-diagrams/) links its download to arXiv. Visually inspected arXiv p. 29, equations (80)–(85). Claims below are explicitly about the retrieved arXiv text. |
| Roberts–Yaida–Hanin, *The Principles of Deep Learning Theory* | [arXiv:2106.10165v2](https://arxiv.org/pdf/2106.10165v2), 471 PDF pages, revised 2021-08-24; Cambridge 2022 publication identified in the [version history](https://arxiv.org/abs/2106.10165) | Complete Chapter 7, printed pp. 191–198; complete Chapter ∞, printed pp. 335–390, including §∞.3's full ddNTK recursions; complete §11.1, pp. 293–296; §2.3 initialization/ensemble passage pp. 47–51; contents/preface orientation. Printed pagination is PDF pagination minus 8. Visually inspected printed p. 359/PDF p. 367. The rest of the book, including full Chapters 8–11, Appendix A/B, and the published Cambridge edition, was not audited. This is a complete-chapter audit of the relevant final training calculation, not a full-book proof review. |

Repository inputs: `paper/main.tex`, `paper/references.bib`, and `paper/feature_learning_theorem.tex` were read completely; `paper/compact_nth.tex` was read through its statements, setup, and the beginning of the proof, lines 1–310. Its remaining lower-bound proof was not audited. No other study, archived book, or other reader's report was read. Included manuscript proof files outside the assigned scope were not opened. Thus this report compares the manuscript's stated contract; it does not independently validate its headline compression theorem or its NTH lower bound.

## Common contract and notation

Here `n` denotes width, `m` the number of training inputs, `L` a fixed number of hidden layers, and `p` the number of predeclared passive inputs. Write `f_n(t,x)` for the dense prediction, `f_c(t,x)` for a compressed prediction initialized from that same dense realization, and `f_n'(t,x)` for an independently initialized dense prediction. The requested comparison is

\[
\frac{\sup_{t\in[0,\infty],\,x\in\mathcal X}|f_c(t,x)-f_n(t,x)|}
{\sup_{t\in[0,\infty],\,x\in\mathcal X}|f_n(t,x)-f_n'(t,x)|}
\longrightarrow 0\quad\text{in probability},
\]

with the fitted endpoint included and a failure convention when relevant limits or the denominator are missing. The manuscript uses a zero readout, Gaussian dense hidden matrices, readout normalization `1/n`, and layer mobilities `(n,1,...,1,n)` for averaged squared loss. Its analytic-activation, positive population-gap, and small-label assumptions are substantial. All problem parameters other than width are fixed in the headline limit. Harmonic promises the whole input sphere with polylogarithmic total retained state; Taylor promises only a predeclared finite panel, with `O(log^3 n)` total state for fixed problem parameters; Legendre reduces moving state to `n^{5/4+o(1)}` but retains quadratic fixed mixers. Setup work and peak memory have separate bounds; exact-real coordinate counts are not bit-complexity claims.

The feature-learning theorem adds hypotheses and certifies an early-time width-independent separation from every affine input predictor and from the reference's frozen initial kernel, together with movement in every hidden layer. It does not claim endpoint feature-learning separation or a test-risk advantage. These qualifications matter when comparing to prior perturbative results.

## 1. Huang–Yau: a genuine autonomous hierarchy, in another scaling

### Model, initialization, data, optimizer

The source uses `m` for width, `n` for training count, and `H` for hidden depth: these become our `n`, `m`, and `L`. Its layer features are normalized by `1/sqrt(width)` after activation, and the output is the inner product with a Gaussian readout. All weights and the readout are initialized as centered independent Gaussians with fixed order-one variances in that parameterization. In particular, the readout is random and nonzero and the initial scalar output is order one. Training is Euclidean gradient flow for averaged half squared loss. Neither initialization nor effective layer mobilities coincide with the manuscript's model.

Assumptions 2.1–2.2 require bounded activation derivatives through a specified finite order, bounded nonzero input norms, and quantitative linear independence of every small subset of inputs up to an order depending on the chosen hierarchy depth. The latter is stronger and different from merely requiring the manuscript's population feature Gram gap. Theorem 2.6 additionally assumes a positive smallest eigenvalue `lambda` of the initial empirical NTK. Depth, derivative bounds, and data nondegeneracy constants are held fixed; the proof does not provide uniform constants for arbitrary width-dependent truncation order.

### Retained state and exact autonomy

For scalar output and Euclidean parameters `theta`, define

\[
K_1(x;\theta)=f(x;\theta),\qquad
K_{r+1}(x_1,\ldots,x_{r+1};\theta)
=\nabla_\theta K_r(x_1,\ldots,x_r;\theta)
\cdot\nabla_\theta f(x_{r+1};\theta).
\]

With training residual `r_a(t)=f(t,x_a)-y_a`, chain rule gives

\[
\dot K_r(t)=-\frac1m\sum_{a=1}^m K_{r+1}(t;\cdot,x_a)r_a(t).
\]

Their equation (15), proceedings p. 5, freezes the top tensor at rank `q`, initializes all retained tensors from the actual dense realization, and uses the closure's own residuals thereafter. This is a finite autonomous nonlinear system, not an externally forced record of the dense trajectory. The paper's construction is directly relevant prior art.

Literal train-only storage is `m+sum_{r=2}^q m^r`, with the rank-`q` array fixed and lower arrays moving. This is our elementary array count, not a memory theorem claimed by Huang–Yau. For a fixed passive panel, one can append query-specific tensors and obtain analogous finite panel storage. Equation (22), proceedings p. 6, explains how a new query can be propagated once its initial query-dependent tensors have been supplied; it does not furnish a finite retained whole-sphere decoder that dispenses with the original network for arbitrary new queries. No cost bound for obtaining all derivative tensors comparable to the manuscript's numerical initializers is proved.

### What is proved and on what horizon

In manuscript notation, the stated Theorem 2.6, for even `q` up to a fixed regularity order `q_*`, gives

\[
\|f(t)-\widetilde f(t)\|_{\ell^2(\text{train})}
\lesssim \frac{(1+t)t^{q-1}\sqrt m}{n^{q/2}}
\min\{t,m/\lambda\},
\]

provided

\[
t\le \min\left\{
\frac{c\sqrt{\lambda n/m}}{(\log n)^C},
\frac{n^{q_*/[2(q_*+1)]}}{(\log n)^{C'}}\right\}.
\]

There is also a uniform entrywise kernel error bound, equation (19). The proof architecture is substantive: exact differentiation organizes the hierarchy; Gaussian conditioning/tensor-program-style projections control initialized tensors (Appendix A); a priori estimates control evolved higher derivatives (Appendix B); stability and residual decay compare the truncated and full systems (Appendix C). The kernel's finite-width movement is explicitly tracked rather than assumed zero.

For fixed data and fixed time, the displayed result is already `O(n^{-1})` at rank two and `O(n^{-2})` at rank four, up to the source's fixed constants. Thus one cannot attribute a necessary `q~log n` to this original model. With a width chosen for a target loss tolerance, Corollary 2.5 and the discussion after Theorem 2.6 reach that tolerance on a time proportional to `(m/lambda) log(m/epsilon)`. It would be unfair to describe the result simply as a short-time calculation. Nevertheless, its displayed truncation theorem has a finite, width-dependent horizon; it is not a single fixed-width uniform-in-physical-time bound through `t=infinity` with the manuscript's exact error norm and dense-pair normalization.

Corollary 2.4 bounds the NTK's time derivative by a polylogarithmic factor times `(1+t)/n`. This is finite-width feature learning that vanishes at fixed time in the fixed-depth infinite-width limit of this scaling. It is not the manuscript's width-independent departure from frozen-kernel evolution. A sufficiently accurate correction can still be below a stochastic fluctuation scale in this weaker regime; absence of the manuscript's explicit ratio theorem is not evidence that such a ratio is impossible there.

### Proof concerns, separated from contract mismatch

Two local issues were found in the complete arXiv proof. Neither is needed to establish the model/contract distinction, and neither justifies declaring the hierarchy theorem false.

- **Appendix B differential-majorant step, pp. 31–32, (B.27)–(B.34): proof-gap flag, not a counterexample.** The text differentiates a bound on a derivative norm to obtain higher derivatives of a norm maximum. Differentiating inequalities is not valid in general, and max norms need not be smooth. More concretely, the exact identity has the form `dot F=-n^{-1/2} m^{-1} sum_a F_a^(1) r_a`; differentiating again also produces `-n^{-1/2} m^{-1} sum_a F_a^(1) dot r_a`, not only the next directional tensor. Thus the displayed argument does not establish (B.29) as an ordinary-time-derivative inequality. Repeated integration of the directional hierarchy and a positive majorant may recover the intended bound without differentiating residuals or maxima; that repair was not proved in this audit. The affected claim is the displayed route to the long-time a priori estimate, not the chain-rule closure itself. Confidence is high in the literal issue, lower in any implication for the final theorem. The proceedings main text is not a substitute proof and the unavailable final supplement was not checked for a repair.
- **Probability convention versus Gaussian maxima: a genuine quantitative overstatement in the retrieved text.** Section 1.3 defines high probability as at least `1-exp(-n^c)` for some positive constant `c`, in our width notation. Corollary A.5, pp. 24–25, applies that language to `||v(0)||_infinity <= C(log n)^C` for expressions including Gaussian coordinates. Even one standard Gaussian exceeds that threshold with probability of order `exp[-O((log n)^{2C})]`, which is asymptotically larger than `exp(-n^c)` for every fixed positive `c`. A weaker overwhelmingly polynomial probability convention can retain useful concentration and the qualitative approximation claim; the stated stretched-exponential convention cannot simply be inherited by these events. This affects quantitative confidence, not the existence of finite-order closures.

There is also a minor statement-level mismatch: the theorem specifies even truncation order, while the following scaling illustration uses order three. That example is not covered verbatim by the stated theorem. It should not be used to erase the valid even-order claim.

### Coordinator check: the differential-majorant step has a local repair

An independent follow-up reader checked this repair against the source's generated-expression bounds, rather than accepting its classification: the initial logarithmic powers, the single remaining square-root-width factor, and the bootstrap exponent agree. The verdict below is conditional on those preceding source estimates, not a full independent audit of them.

This repairs the specific passage, conditional on the preceding bounds in the paper; it is not a new certification of its whole theorem. Preserve the source's notation in this paragraph: `m` is width and `p` is its fixed differentiation order. Let `G_r(t)` be the maximum infinity norm of the directional expressions `f_t^(r)` generated from the base family in (B.24), including all sample indices, and put `G_0(t)=xi(t)`. Equations (B.25)–(B.28), integrated before taking maxima, give for `0 <= r <= p`

\[
G_r(t)\le G_r(0)+\frac C{\sqrt m}\int_0^tG_{r+1}(s)\,ds.
\]

No derivative of a maximum or of an inequality is taken. Iterating this positive integral inequality gives

\[
\xi(t)\le
\sum_{r=0}^{p}\frac{(Ct/\sqrt m)^r}{r!}G_r(0)
+\frac{C^{p+1}}{p!m^{(p+1)/2}}
\int_0^t(t-s)^pG_{p+1}(s)\,ds.
\]

The source's initialized-expression bounds give `G_r(0) <= C(log m)^((2r+1)C)`, and (B.30)–(B.33) give
`G_(p+1)(s) <= C sqrt(m) max(1,xi(s))^(2p)` on the preceding a priori interval. For

\[
0\le t\le m^{p/[2(p+1)]}(\log m)^{-B},
\]

the initial polynomial is at most `C_0(log m)^A` for suitable fixed `A,C_0` and all sufficiently large `m`: every term with `r>0` contains the decaying factor `m^(-r/[2(p+1)])` times a fixed logarithmic power. Under the bootstrap `max(1,xi) <= 2C_0(log m)^A`, the integral term is bounded by

\[
C_1m^{-p/2}t^{p+1}(2C_0)^{2p}(\log m)^{2pA}
\le C_2(\log m)^{2pA-B(p+1)}.
\]

Choose `B` so that `B(p+1)>(2p-1)A`, and then enlarge the width threshold. The last term is less than one half of `C_0(log m)^A`. Continuity closes the bootstrap with a strict improvement; this interval is also within the earlier square-root-width a priori interval. This recovers the claimed width exponent in Proposition B.3 without the invalid differential manipulation, changing only unspecified logarithmic constants. Thus that passage is a **Minor Flaw with an explicit repair**, not evidence that the hierarchy theorem requires an essentially new argument. The separate stretched-exponential probability overstatement remains a quantitative issue; this repair does not fix it.

## 2. Dyer–Gur-Ari: finite same-instance corrections, with explicit conjectural boundaries

### Model and evidentiary layers

The paper uses the usual NTK normalization: internal matrix multiplications and the scalar readout carry inverse square-root width factors; the underlying parameter coordinates, including the readout, are independent centered unit Gaussians. The output is random of order one at initialization. Continuous training uses summed half squared loss and Euclidean gradient flow; the paper also analyzes discrete SGD and general losses. The missing factor `1/m` relative to averaged loss is a time rescaling, whereas the discrepancy with the manuscript's zero-readout feature-learning scaling is not merely a time rescaling.

The main large-width power-counting assertion is explicitly Conjecture 1 in the retrieved current arXiv version. Its proof status is differentiated, not concealed:

- arbitrary-depth linear networks: rigorous combinatorial result, Theorem 1 and Appendix B;
- deep ReLU with all correlation-function inputs equal: restricted proof, Theorem 2/Appendix C.1, not arbitrary multiple-input training;
- one-hidden-layer smooth nonlinear networks: Appendix C.2, Theorem 7;
- general deep nonlinear multiple-input networks: conjectural power counting, supported numerically, rather than a general rigorous theorem.

The diagram argument pairs Gaussian parameters, counts free index loops, and relates the resulting exponent to a graph of derivative contractions. Appendix D explains consequences for dynamics and variances. Lemma 5 controls variance at the same relevant order, so the theory is not exclusively a statement about ensemble means. For general nonlinear continuous dynamics, moving between the time-Taylor expansion and the width limit is assumed; the text flags this analytic issue. The exact finite Taylor expansion used in Appendix D.3 for discrete updates is justified for linear networks; the corresponding infinite nonlinear tail is not controlled there.

### The finite closed state is real, not an inference from the abstract

Appendix E.4, pp. 28–35, defines `O_1=f` and successive gradient contractions `O_s`, giving

\[
\dot O_s=-\sum_{a=1}^m O_{s+1}(\cdot,x_a)(f_a-y_a).
\]

For a selected order in inverse width, the hierarchy is cut off at a finite even rank; equations (80)–(85), p. 29, explicitly explain the truncation. At the first nontrivial inverse-width order, retain the output, NTK, rank-three tensor, and initialized rank-four tensor. Freezing the last and evolving the others with their own residuals is an autonomous finite nonlinear closure; expanding those equations order by order yields the paper's explicit corrections. The initialization uses the realized `f(0)`, empirical `Theta(0)`, and higher derivative contractions, rather than replacing them all by expectations.

Equations (91)–(97), pp. 30–31, express kernel and prediction corrections through initialized tensors and the kernel propagator. Equations (98)–(99) discuss late-time kernel and decay corrections. Figure 10, p. 32, compares individual network components with finite-width predictions for individual randomly initialized networks, on a small two-class MNIST problem, with widths 128 and 1024 and linear/tanh examples. This is genuine same-instance numerical evidence, albeit not a complete-trajectory/query-uniform error theorem.

A scalar train-only literal rank-four implementation has `O(m^3)` moving and `O(m^4)` fixed coordinates, independent of width at a fixed truncation order. These are inferred scalar-array counts. Finite panels add corresponding initial tensors; neither a whole-sphere decoder nor setup work/peak-memory/precision guarantees of the manuscript's kind are supplied. It is misleading to call this “not finite closed” merely because the accuracy justification is perturbative or partly conjectural. The correct distinction is between an explicit closed finite-order model and a rigorously controlled remainder for the desired regime.

### What it does not establish

The retrieved source supplies no high-probability, uniform-all-time remainder bound in the manuscript's fixed-depth nonvanishing-feature-learning scaling, no lower bound on the actual independent dense-run denominator, and no width-polylogarithmic whole-sphere retained decoder. Its order estimates must not be silently promoted from asymptotic correlator/perturbation statements into a pathwise error guarantee in that stronger setting. These are boundaries of its results, not flaws in a transparently conjectural/formal claim. No additional fatal error in its proved restricted cases was established by this audit; neither all diagram identities nor every tensor coefficient was independently rederived.

## 3. Roberts–Yaida–Hanin: nonlinear finite-state training and the trained endpoint

### Setup and state

Initialization equations (2.19)–(2.22), printed pp. 48–49, use independent Gaussian weights of variance `C_W/n_previous` and Gaussian biases of variance `C_b`. The last layer is also random. Chapter 7 introduces gradient-based updates with a layerwise learning-rate tensor, and the final training calculation treats summed squared loss. In the usual diagonal specialization, width factors in the learning-rate tensor balance the parameter normalization. One must not identify the manuscript's physical mobilities simply by noticing similar-looking Gaussian matrix variances.

Chapter ∞ develops the leading finite-width theory, with the depth-to-width ratio controlling the size of corrections under its critical scaling. Smoothness matters: the text explicitly discusses why naive activation Taylor expansions fail for nonsmooth ReLU. The strongest training formula is therefore not a general theorem for arbitrary nonsmooth activations.

The retained stochastic quantities are the output, the NTK, a rank-three differential NTK defined in (11.8), and two rank-four second differentials defined in (∞.5) and (∞.7). The rank-three object is a Hessian of one output contracted with gradients of two outputs; it is not literally the fully symmetrized next Huang–Yau kernel. The two rank-four tensors encode distinct third-derivative/Hessian contractions. Equations (∞.81)–(∞.83), printed pp. 358–359, give coupled nonlinear difference equations: output update is cubic in residuals at this order, NTK update quadratic, differential-NTK update linear, and the two second differentials are frozen at their initialized values to the retained order.

This is an explicit autonomous finite sample-space state at fixed order, including finite learning-rate effects. For scalar output on a panel of size `M=m+p`, literal full arrays use `O(M^3)` moving and `O(M^4)` fixed coordinates. These conservative counts are inferred from the displayed tensors, not optimized bounds proved in the book. They do not charge the derivative-tensor initialization work. An explicitly stored endpoint formula can additionally contain algorithm-projector arrays with six training indices, so one should distinguish endpoint formula storage from the cheaper autonomous rank-four evolution.

### Why the endpoint result cannot be ignored

Section ∞.2.2 treats many steps of gradient descent. It first solves the dynamics with the initial empirical NTK frozen, then treats the differential tensors as perturbative forcing. Under the stability condition that the eigenvalues of `I-eta H_initial` lie strictly within the unit circle, the free residuals decay; time sums of propagated residual products give corrections. The construction evolves the differential NTK, then the NTK, then the prediction, rather than only solving an initialization ensemble.

Equations (∞.141) and (∞.154), printed pp. 372 and 375, explicitly give the fully trained prediction. The discussion on p. 376 says that the quantities still refer to a particular realization; averaging and covariance calculations follow afterward. Section ∞.2 also treats two Newton-like updates and isolates algorithm dependence in projection tensors. Thus “only ensemble averages,” “no closed finite model,” and “no fitted-limit description” are all unfair descriptions of this source.

The essential limitation is the status and regime of the truncation error. The calculation is an effective-theory expansion through the leading inverse-width order, with higher-order terms omitted. Chapter ∞ does not prove a finite-width, high-probability bound for the supremum over all training steps and promised queries relative to actual independent dense variability. A formal remainder attached to a convergent finite-order solution is not by itself such a theorem. Statistical power counting and a single-realization error bound must also be distinguished: for example, fluctuations whose variance is order `1/n` have typical size `1/sqrt(n)`. I did not audit the full preceding ensemble chapters, so I do not assign a stronger pathwise interpretation to their remainder notation than this chapter establishes.

The theory deliberately studies nonzero representation-learning corrections. At fixed depth these shrink with width; allowing depth to grow can preserve an effective depth/width ratio, within the perturbative conditions. Neither statement matches the manuscript's fixed-depth, width-independent early-time feature-learning certificate. The book's explicit discussion of these effects is a strength and warrants a substantive citation. No counterexample to the book's stated effective expansion was established here. Its very long recursion identities were read, but not independently checked index by index.

## 4. What the manuscript's literal-array benchmark actually permits

`paper/compact_nth.tex` explicitly studies two identity hidden layers, zero readout, a particular family of training inputs, averaged half squared loss, and a short fixed interval. Its normalized coordinates have the same gradient-contraction hierarchy form as above, but its initialization and physical training regime differ from Huang–Yau. The tensor arrays are ordered, are retained literally, and include fixed top tensors; compressed/factorized/implicit encodings are outside the lower-bound class.

For the specified hard family, `4 <= m <= sqrt(n)`, the manuscript states a necessary-and-sufficient scalar count of `n^{Theta(log m)}` to meet its relative-accuracy benchmark. It also states an upper construction at rank proportional to `log n`. These are statements about that implementation class on that model. This report has not audited the complete lower-bound proof.

The following inferences would be invalid even if that proof is correct:

- that original Huang–Yau NTH requires this storage in its own NTK scaling;
- that every finite-order expansion, or every encoding of a hierarchy, needs this many retained coordinates;
- that the same storage separation has been proved on the manuscript's analytic nonlinear headline family;
- that the comparison proves computational speedups, bounded-precision savings, or optimality of Harmonic/Taylor;
- that the original NTH theorem's fixed-rank constants may be used uniformly at rank proportional to `log n` without a new argument.

Conversely, the original NTH's fixed-rank inverse-width error bound does not invalidate the manuscript's benchmark: the two models support different sizes of feature-learning effects. The existing caveats in `main.tex` and `compact_nth.tex` are scientifically necessary and should survive any more assertive narrative.

## Recommended positioning

A defensible formulation is:

> Prior finite-width theories already produce finite, initialization-dependent nonlinear closures and perturbative descriptions of the trained predictor. Huang–Yau supplies quantitative hierarchy truncation estimates in an NTK-scaled regime; Dyer–Gur-Ari develops diagrammatic finite-width corrections; Roberts–Yaida–Hanin derives finite-state training equations and trained predictions through leading inverse-width order. The present result addresses a different conjunction: fixed-depth nonlinear feature learning that persists with width, a small retained autonomous state coupled to a finite Gaussian dense realization, and certified complete-trajectory error below actual independent dense-run variability, on the stated whole-sphere or predeclared-panel domain. Its literal-array hierarchy benchmark is a separate, explicitly restricted comparison.

The current reference list contains Huang–Yau but not the other two audited sources. Adding both would materially improve attribution; no manuscript edits were authorized here. The proof concerns above should be retained as bounded technical notes, not used as a rhetorical reason to dismiss relevant prior art. Remaining version gap: Dyer–Gur-Ari's final ICLR PDF and any revised Huang–Yau final proof supplement were not accessible/verified. Remaining book gap: only the complete named chapters and explicit setup passages were read, not all 471 pages.
