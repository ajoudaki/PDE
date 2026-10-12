# Targeted reassessment: derivative-program compilation and adjacent software

Discovery date: 2026-10-11. Scoped subagent report. Scientific repository input: the complete `paper_MFP/main.tex` (2,967 lines). External evidence below is primary literature and authors' software. No existing positioning report, study history, other study, or manuscript implementation was used. The canonical-notation skill, its neural-network reference, and `solve-math-rigorously` were applied. This is a literature comparison, not a correctness review of the MFP implementation or a complete independent proof audit of every cited theorem.

The most consequential additional precedent found is **Guillen–Misof–Gerken, “Finite-Width Neural Tangent Kernels from Feynman Diagrams,” ICML 2026**, together with **NTK Unlimited**. It should be included in any revised positioning. It already combines derivative-kernel statistics, Gaussian expectations, symbolic simplification, dependency management, and numerical compilation. Its documented input is a collection of tensor recurrences for multilayer perceptrons; the inspected release does not supply the manuscript's transformation from a declared neural program and a requested physical derivative or update to the corresponding limiting graph. This is a substantive adjacent capability, not an interchangeable implementation.

## The comparison being made

In the manuscript, the derivative order is any **fixed** integer, chosen before the width tends to infinity. The input is a finite typed program using smooth coordinatewise functions, normalized averages, and named independent Gaussian matrices that may be reused in either orientation. The frontend expands physical parameter/data derivatives, represented gradient directions, finite updates, and moving gradient-flow jets at finite width. The backend assigns a finite Gaussian-source/response graph, with deterministic limits of scalar outputs in every finite \(L^p\). Singular Gaussian covariance is allowed. The output may retain symbolic Gaussian expectations; it need not evaluate an integral analytically or numerically. The manuscript does not claim to reconstruct a flow at positive time from an infinite Taylor series, to handle growing program length or derivative order, or to cover every architecture or arbitrary tensor contraction.

Consequently, the following are distinct comparison targets: finite-dimensional automatic differentiation; a program-limit theorem; derivation of a prescribed set of kernel recurrences; symbolic processing of supplied recurrences; numerical integration; and the combined neural-program-to-derivative-limit transformation. A system can be a strong precedent for several components without providing the combined transformation.

## The ICML 2026 paper and NTK Unlimited

Primary references: [conference record](https://proceedings.mlr.press/v306/guillen26a.html), [complete proceedings PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/guillen26a/guillen26a.pdf), [arXiv record](https://arxiv.org/abs/2508.11522), and [authors' software](https://github.com/PhilippMisofCH/ntk-unlimited). The complete 53-page proceedings paper, including Appendices A–K, was read. Diagram extraction was imperfect; associated algebraic formulas were read, and PDF page 31 was rendered to verify Eq. (101). This is not a graphical audit of every diagram.

The software was downloaded at commit `22f40289b1aa4fc36fe670abcf03c3c30a141651`. Its complete README, file tree, recurrence dispatcher, the complete representative `F_expressions.py`, Gaussian numerical-integration module, and relevant symbolic-to-numeric paths were inspected. No package installation, complete test suite, or empirical reproduction was run. Downloads and extracted code are in `data/generated/mfp_literature_positioning_20261011/reassessment_discovery/`.

| Question | Primary evidence | Consequence for positioning |
|---|---|---|
| Architecture and regime | Main §2 and Appendix B, Eq. (20), use initialized MLPs with independent Gaussian weights, \(1/\sqrt{n_{\ell-1}}\) forward scaling, and width-independent learning rate. | The analyzed model is not the manuscript's entire declared program grammar or its feature-learning flow normalization. |
| What derivative objects are included? | Appendix C, Eqs. (25)–(27), defines dNTK and two ddNTK contractions using second and third parameter derivatives. | Higher derivatives are a genuine part of this precedent. Describing it as only NNGP/ordinary NTK computation would be misleading. |
| What does “all orders” mean? | Theorem 4.3 and Appendix E.4 extend diagrammatic rules to higher-rank cumulants and higher powers of \(1/n\). | This quantifier concerns the width expansion. It is not a theorem that accepts an arbitrary fixed-order physical derivative query on an arbitrary neural program. |
| What is actually automated? | §6.1 and Appendix J.1 begin from symbolic recurrence expressions, simplify Gaussian expectations and contractions, and generate numerical routines. | Symbolic Gaussian-expectation compilation and simplification are prior capabilities. The distinguishing input layer matters. |
| How broad is published recurrence coverage? | Code has a fixed dependency table and dispatcher for `V4`, `G1`, `F`, `D`, `H1`, `A`, `B`; separate expression files supply their recurrences. The CLI restricts the target to this list. | The inspected release is a solver/compiler for supplied tensor recurrences. No general network-definition plus derivative-query frontend was found in these paths or the documented API. |
| Scope of the paper's extension | §7 discusses extending diagrammatic rules to other architectures and says a full analysis of higher-order tensors is beyond scope. | An extendible calculus should not be equated with an already implemented general compiler. This limitation also should not erase its all-order diagrammatic claim. |

Concrete code anchors, all fixed to the inspected commit:

- [Fixed recurrence dependencies, `recursions.py`, lines 60–68](https://github.com/PhilippMisofCH/ntk-unlimited/blob/22f40289b1aa4fc36fe670abcf03c3c30a141651/src/ntkunlimited/recursions/recursions.py#L60), [CLI target selection, lines 830–833](https://github.com/PhilippMisofCH/ntk-unlimited/blob/22f40289b1aa4fc36fe670abcf03c3c30a141651/src/ntkunlimited/recursions/recursions.py#L830), and [dispatcher, lines 954–1057](https://github.com/PhilippMisofCH/ntk-unlimited/blob/22f40289b1aa4fc36fe670abcf03c3c30a141651/src/ntkunlimited/recursions/recursions.py#L954).
- [`F_expressions.py`, lines 26–57](https://github.com/PhilippMisofCH/ntk-unlimited/blob/22f40289b1aa4fc36fe670abcf03c3c30a141651/src/ntkunlimited/recursions/F_expressions.py#L26) explicitly constructs the known recurrence using Gaussian-expectation objects, activation derivatives, prior tensors, and covariance inverses. [Lines 64–79](https://github.com/PhilippMisofCH/ntk-unlimited/blob/22f40289b1aa4fc36fe670abcf03c3c30a141651/src/ntkunlimited/recursions/F_expressions.py#L64) compile that supplied expression numerically.
- [`numerical_integration.py`, lines 21–36](https://github.com/PhilippMisofCH/ntk-unlimited/blob/22f40289b1aa4fc36fe670abcf03c3c30a141651/src/ntkunlimited/recursions/numerical_integration.py#L21) performs Gaussian-weighted cubature. Thus this package goes further than the manuscript in numerical evaluation of its supported integrals; it should not be dismissed as merely formal notation.

### Width expansions, exact expectations, and verification status

The leading recurrences are stated with \(O(n^{-2})\) remainders, e.g. Appendix C, Eqs. (21)–(22), and Theorems 4.1–4.2 specify leading tensor orders. Appendix E.4 argues that the diagrammatic rules extend to all orders by admitting additional cumulant tensors. This is substantial structural information. The paper does not state the manuscript's general \(L^p\)-convergence and uniform-moment theorem for arbitrary derivative programs. I did not locate a general analytic remainder theorem in the complete paper that would turn every formal all-order calculation into an exact finite-width identity.

**Dependency verification is incomplete.** The paper's leading-order proofs compare recurrences to Roberts–Yaida–Hanin, *The Principles of Deep Learning Theory* (2022), while its preactivation diagrammatic expansion depends on Banta–Cai–Craig–Zhang, [“Structures of Neural Network Effective Theories”](https://arxiv.org/abs/2305.02334). Only the latter's primary abstract was screened in this assignment; neither dependency was read completely here. Therefore this report does not independently certify completeness of the all-order expansion, the stated remainders, or all its activation hypotheses. The architecture, definitions, symbolic pipeline, and software-input distinction above are directly inspectable without assuming those unverified claims.

Theorem 5.2 deserves separate treatment. Its claim concerns the **mean of a diagonal NTK entry** for piecewise linear positively homogeneous activations; it does not say that the random finite-width NTK is deterministic. Appendix I cancels width-expansion coefficients. Vanishing coefficients alone do not exclude a remainder smaller than every power of \(1/n\). Nevertheless, the exact diagonal-mean conclusion has a direct finite-width symmetry justification for the actual bias-free architecture, so a criticism based solely on that formal-versus-exact distinction would be too strong.

Here is an independent check, with its assumptions exposed. Write the Appendix B network as

\[
z_i^{(\ell+1)}=\frac1{\sqrt{n_\ell}}\sum_j W_{ij}^{(\ell+1)}\phi(z_j^{(\ell)}),
\qquad W_{ij}^{(\ell+1)}\sim N(0,C_W^{(\ell+1)}),
\]

with independent layers and positive variances. Let \(\vartheta_{\leq\ell}\) denote all raw weights through layer \(\ell\), fix an input, and define

\[
Q_\ell=\mathbb E[(z_i^{(\ell)})^2],\qquad
T_\ell=\mathbb E\|\nabla_{\vartheta_{\leq\ell}}z_i^{(\ell)}\|^2.
\]

Exchangeability makes these independent of the neuron index. Suppose \(\phi(z)=a_+z\) for \(z>0\), \(\phi(z)=a_-z\) for \(z<0\), and \(\phi(0)=0\). Set \(A=(a_+^2+a_-^2)/2\). Averaging the independent next-layer row first kills all off-diagonal products of its weights and gives the exact identity

\[
T_{\ell+1}=\mathbb E\phi(z_i^{(\ell)})^2+
C_W^{(\ell+1)}\mathbb E\!\left[\phi'(z_i^{(\ell)})^2
\|\nabla_{\vartheta_{\leq\ell}}z_i^{(\ell)}\|^2\right].
\]

Changing the sign of the whole incoming row of neuron \(i\) changes \(z_i^{(\ell)}\) to its negative. It leaves its own-row gradient unchanged and reverses the gradient with respect to all earlier weights. Therefore the squared full gradient is unchanged. Pairing the two row signs gives \(\mathbb E\phi(z)^2=AQ_\ell\) and the second expectation equal to \(AT_\ell\). At zero preactivation, the sign pairing needs care: conditional on a nonzero preceding activation vector, positive Gaussian variance makes zero preactivation a null event; on an event where the preceding activation vector is zero, its parameter derivatives vanish almost surely, by induction through this bias-free homogeneous network. The gradient factor therefore vanishes there. This covers the usual finite derivative convention at the ReLU kink for this argument. Consequently,

\[
Q_{\ell+1}=C_W^{(\ell+1)}AQ_\ell,
\qquad T_{\ell+1}=AQ_\ell+C_W^{(\ell+1)}AT_\ell.
\]

These exact recursions are independent of hidden widths. Their first-layer values are deterministic functions of the fixed input. They establish the width-independent diagonal NTK mean in this setup without summing an asymptotic series. No claim is made here about zero-variance layers, arbitrary biases, other parameter metrics, off-diagonal input pairs, or arbitrary observables.

PDF inspection confirms a minor error in Appendix I, Eq. (101): the printed coefficient for \(\mathbb E\phi'(Z)^2\) is \((a_+^2-a_-^2)/2\); the correct coefficient for a nondegenerate centered Gaussian is \(A\), with a plus sign. It is not an extraction artifact. Replacing this constant does not undermine the covariance-derivative cancellation used there. This is not evidence against the entire method, and no objection is inferred merely from its use of ReLU.

### Singular input covariance

The paper's displayed formulas use covariance inverses (e.g. main Eq. (5)), and Appendix J describes symbolic integration by parts that can cancel inverses. Existence of a removable inverse in one representation does not by itself restrict the underlying mathematics. However, the inspected numerical implementation does not expose a general singular-covariance treatment:

- [`comp_next_G1`, line 178](https://github.com/PhilippMisofCH/ntk-unlimited/blob/22f40289b1aa4fc36fe670abcf03c3c30a141651/src/ntkunlimited/recursions/recursions.py#L178) and [`comp_next_F`, line 258](https://github.com/PhilippMisofCH/ntk-unlimited/blob/22f40289b1aa4fc36fe670abcf03c3c30a141651/src/ntkunlimited/recursions/recursions.py#L258) unconditionally compute `np.linalg.inv(G)`.
- [`numerical_integration.py`, lines 39–69](https://github.com/PhilippMisofCH/ntk-unlimited/blob/22f40289b1aa4fc36fe670abcf03c3c30a141651/src/ntkunlimited/recursions/numerical_integration.py#L39) reduces repeated sample indices but constructs Gaussian density objects on the remaining covariance submatrices, without `allow_singular` or a covariance-support factorization.
- [`regularize_cov`, lines 665–687](https://github.com/PhilippMisofCH/ntk-unlimited/blob/22f40289b1aa4fc36fe670abcf03c3c30a141651/src/ntkunlimited/recursions/recursions.py#L665) provides optional diagonal regularization in a kernel helper; the inspected fixed-width setup [passes `diag_reg=None`, lines 941–949](https://github.com/PhilippMisofCH/ntk-unlimited/blob/22f40289b1aa4fc36fe670abcf03c3c30a141651/src/ntkunlimited/recursions/recursions.py#L941).

For example, two distinct input indices with identical input vectors produce a singular two-input Gram matrix, even after the repeated-index simplification. The explicit inverse is undefined in that case. This is a source-level limitation of the cited paths, not a claim that a nonsingular numerical approximation cannot work or that no singular extension of the paper is possible. No package-level singular-input experiment was run.

## Additional candidates screened

The table records **reading level**, so an abstract/README exclusion is not silently presented as a complete theorem audit. Known families supplied in the assignment were used as search seeds, not re-audited in full.

| Candidate and primary source | Reading level in this assignment | Retention decision and reason |
|---|---|---|
| Agazzi–Mosig García–Trevisan, [*Quantitative Gaussian-Process Limits of Tensor Programs*, arXiv:2607.06290](https://arxiv.org/html/2607.06290v1) | §§1.1–1.2; statement and discussion of Theorem 2.4/Remark 2.5. Proofs not audited. | Retain as a newer theorem-level comparator, not a demonstrated compiler equivalent. Basic Netsor gives quantitative Wasserstein convergence with Lipschitz nonlinearities and same-matrix reuse. Its scalar-kernel extension explicitly assumes joint nondegeneracy. The inspected grammar has no transpose or derivative-query frontend. This does not establish absence elsewhere in the paper. |
| Sakai–Karakida–Imaizumi, [*Infinite-Width Limit of a Single Attention Layer: Analysis via Tensor Programs*, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/33201f38001dd381aba2c462051449ba-Abstract-Conference.html), [author software](https://github.com/manasakai/infinite-width-attention) | Primary abstract and software README. | Retain as a scope reminder: standard \(1/\sqrt n\) finite-head attention has a non-Gaussian hierarchical limit conditional on similarity scores. The documented code is numerical experiments, not a derivative compiler. No full theorem assessment made. |
| Yang–Yu–Zhu–Hayou, [*Tensor Programs VI: Feature Learning in Infinite-Depth Neural Networks*](https://arxiv.org/abs/2310.02244) | Abstract. | Depth parametrization, feature diversity and Depth-µP are adjacent questions. No compiler equivalence follows from the primary description. |
| [NTK4A](https://github.com/thegregyang/NTK4A) and [GP4A](https://github.com/thegregyang/GP4A) | Complete relevant READMEs and file listings. | Authors describe reference implementations for selected architectures. NTK4A explicitly limits the software to a few advanced examples despite the theorem's broad title. No generic derivative-query frontend is documented. |
| [Neural Tangents](https://github.com/google/neural-tangents) | Primary README/API descriptions; no renewed full code audit. | Important automatic architecture-to-NNGP/NTK precedent. Its empirical derivative/Taylor utilities do not alone supply a proof of width-limit compilation for arbitrary derivative programs. Existing family retained; broad absence inside the library is not proved here. |
| Bernstein et al., [*Differentiating a Tensor Language*](https://arxiv.org/abs/2008.11256) | Abstract. | Proved efficient tensor AD, including sparse operations, is a component precedent. It does not advertise Gaussian width-limit integration. |
| Sathia et al., [*Compiler Optimizations for Higher-Order Automatic Differentiation*](https://ece.is/assets/pdf/diffprog-ppopp25-paper90.pdf) | Abstract/first page. | Higher-order AD and compiler rewrites for finite tensor computations; no advertised probability-limit semantics. |
| [Tangent](https://github.com/google/tangent), [FreeTensor](https://github.com/roastduck/FreeTensor) | Primary READMEs/project descriptions. | Source-to-source AD / differentiable tensor compilation. Excluded as a whole-transformation match, while retained as evidence that high-order AD machinery is not itself novel. |
| [DYNAMITE](https://github.com/DMFT-evolution/DYNAMITE) | Primary README/docs description. | Numerical solution of supplied dynamical mean-field correlation/response equations. No documented neural-program derivative frontend. It should not be confused with a symbolic derivation system. |
| [NEUROSPF](https://arxiv.org/abs/2103.00124) | Abstract. | Symbolic analysis/testing of finite neural programs, not a Gaussian infinite-width compiler. Terminology-only near match. |
| Hardware “tensor program” compilers, e.g. [QiMeng-Xpiler](https://www.usenix.org/system/files/osdi25-dong.pdf) | Primary first-page descriptions/search screening. | Tensor scheduling/hardware compilation is a different meaning of “tensor program”; excluded. |

The known Tensor Programs III/IV/IVb/Non-Gaussian TP, NTH, Label-Aware NTK, Dyer/Aitken, and Tensorgrad families remain relevant seeds. This report adds no new complete audit of those sources and should not replace the parent task's direct comparisons. Bordelon–Pehlevan's dynamical mean-field treatment was assigned to the parent and was not duplicated here.

## Search coverage and bounded conclusions

Searches combined the literal language of the proposed contribution with alternative terminology: `tensor programs symbolic compiler infinite width derivatives`; `infinite width symbolic computation`; `neural tangent hierarchy automatic computation github`; `neural tensor diagrams finite width symbolic package Feynman`; `Gaussian expectation neural symbolic package`; `NETSOR github compiler`; `NEXORT software implementation`; `automatic mean field theory neural networks compiler`; `dynamical mean field neural network software`; `neural network diagrammatic automatic expectations`; `Tensor Programs automatic differentiation`; and newer-followup searches including 2025/2026, TP VI/VII, attention, and quantitative limits. Generic compiler hits were screened separately from probability-program hits. Secondary discovery pages were not used to substantiate scientific conclusions. This was a targeted web search, not an exhaustive citation-index or all-repository census.

The strongest defensible candidate positioning after this search is the **integration of a declared derivative/update language with a rigorous Gaussian source-response limit compiler**, within the manuscript's stated smooth, fixed-program grammar. It should be compared explicitly to NTK Unlimited's recurrence-to-symbolic/numeric pipeline as well as to Tensor Programs' mathematical semantics. Claims of being the first to automate Gaussian expectation calculations, the first symbolic neural derivative calculus, the first all-order diagrammatic framework, or the first general wide-network limit theorem would be much too broad.

The bounded absence statement supported by this work is: **among the documented interfaces and source paths inspected here, no prior package was found that accepts the manuscript's full declared-program plus physical-derivative/moving-jet/update query and automatically returns the corresponding Gaussian source-response graph with the manuscript's convergence contract.** This is not a proof that no such system exists. It is also not a verdict that combining known pieces constitutes sufficient novelty: that requires comparing the actual lowering rules, transpose-reuse semantics, singular-covariance handling, expectation guarantees, and nontrivial compiled examples against the strongest existing mathematical frameworks.

Unresolved verification is specific: the ICML 2026 paper was read completely, but its external proof dependencies and general analytic remainder claims were not independently audited; newer quantitative and attention results were screened only at the stated reading levels; and no whole-package runtime or exhaustive search of every public branch was performed. These limits prevent universal novelty or mathematical-equivalence claims while leaving the concrete software-interface comparison reviewable.
