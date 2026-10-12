# Fresh assessment: quantitative Gaussian-process limits of tensor programs

Assessment date: 2026-10-11. This is a scoped comparison with the supplied MFP manuscript, not a certification of that manuscript or a review of other studies.

The assigned primary source is Andrea Agazzi, Eloy Mosig García and Dario Trevisan, [*Quantitative Gaussian-Process Limits of Tensor Programs*, arXiv:2607.06290v1](https://arxiv.org/pdf/2607.06290v1), submitted 7 July 2026. I read the entire 37-page PDF, including all proofs, examples, numerical discussion and references. There are **no appendices in this version**. The local PDF has SHA-256 `f6c52d5420441da07916f3e2cf559c1cbc340068a7fdd5f5f7a4a5c6d4609aa9`.

I read the complete assigned MFP sections at `paper_MFP/main.tex:598–807` and `1148–1420`, and applied the canonical-notation skill, its neural-network reference, and `solve-math-rigorously`. For the relevant historical dependency I checked Yang's [*Tensor Programs I*, arXiv:1910.12478v3](https://arxiv.org/pdf/1910.12478v3), §5 and Appendix C.1, including Theorems 5.4, C.4 and C.11 and C.11's complete proof. I did not audit the entirety of Yang's 73-page paper. The new quantitative proof does not invoke its master theorem as a black box. No previous study assessment, verdict or history was read.

## Result of the comparison

The new paper is a substantial quantitative theorem for a restricted tensor-program language, including same-orientation matrix reuse and empirical-kernel scalar feedback. On the common domain, its inverse-square-root-width estimates are stronger than MFP's unquantified convergence. Its theorem is not a counterpart of MFP's full derivative-query-to-Gaussian-expectation calculus: its admissible operations and regularity assumptions are not closed under the ordinary derivatives, transpose calls and coordinate products required by that calculus. This conclusion follows from the actual mathematical restrictions, not simply from the absence of an automatic-differentiation frontend.

The strongest fair classification is therefore **quantitative background with meaningful overlap**, rather than a full calculus substitute. MFP should not claim that recursive Gaussian expectation evaluation, matrix reuse, or scalar feedback alone distinguishes it from this paper or earlier tensor programs. The comparison does not establish priority for MFP's source-response rule over the wider tensor-program literature.

The printed quantitative proof has errors in its coupling normalization and some examples. Below I exhibit them and give the corrected load-bearing coupling step. They do not supply a counterexample to the main rates. They do prevent treating the printed argument, without correction, as a fully verified proof.

## Exact theorem scope

Write \(W\in\mathbb R^{n\times m}\) for one named matrix, initialized with independent \(N(0,1/m)\) entries. Distinct named matrices are independent. The program is fixed and finite; deterministic input vectors have fixed dimensions. Its ordinary instructions are \(g=Wh\) and coordinatewise functions of previously constructed vectors. There is no instruction that creates \(W^\top\) from \(W\). The infinite-width representatives of the matrix outputs are jointly centered Gaussian, with coordinate covariance

\[
\operatorname{Cov}(\bar g_i,\bar g'_j)
=\mathbf 1_{i=j}\,\frac1m\mathbb E[\bar h^\top\bar h']
\]

when the calls use the same named matrix, and zero cross-covariance for different matrices. Other vector nodes are coordinatewise functions of those Gaussian variables. Thus the theorem does not say that all activated vectors are Gaussian. See §1.1, especially (1.3)–(1.4).

Let \(\mathcal N\) be the finite collection of hidden widths: dimensions produced by a matrix action and subsequently contracted by another matrix action. Define

\[
\delta=\sum_{m\in\mathcal N}m^{-1/2}.
\]

For a fixed program with vector nodes \(h^{(\ell)}\in\mathbb R^{n_\ell}\), **Theorem 1.2** assumes every coordinate nonlinearity is globally Lipschitz and states, for every finite \(p\ge1\),

\[
\mathcal W_p\!\left(
 (h^{(\ell)}/\sqrt{n_\ell})_\ell,
 (\bar h^{(\ell)}/\sqrt{n_\ell})_\ell
\right)\le C_p\delta.
\]

This uses the Euclidean norm on the concatenated vectors. It is a joint normalized-vector distributional estimate, not merely convergence of a selected final output. Constants depend on the fixed program, inputs and nonlinearities. The proof supplies no uniformity as the number of lines, conditioning of the limiting Gram matrices, or activation constants vary. Different hidden widths may diverge at different rates; no growing-program result is stated.

**Corollary 1.3** bounds the \(L^p\) error of \(n^{-1}h^\top h'\) from its deterministic Gaussian-execution expectation by the same order, with an additional \(n^{-1/2}\) sampling term when the kernel is taken over an output dimension. A fixed output dimension therefore does not automatically give a deterministic empirical-kernel limit. In the ordinary language there is no nondegeneracy hypothesis in Theorem 1.2: Lemma 3.9 first replaces redundant matrix calls by deterministic linear combinations. The proof of that reduction uses continuity and full Gaussian support after earlier redundancies have been removed.

**Theorem 2.4** adds the following operations:

\[
s=\frac1n h^\top h',\qquad
h_i=\varphi(h_{1,i},\ldots,h_{k,i};s),\qquad
s'=\psi(s).
\]

Input scalars are deterministic. Ordinary vector nonlinearities and scalar maps \(\psi\) must be globally Lipschitz. Scalar-parametric vector maps must satisfy the explicit bound (2.5):

\[
|\varphi(x;s)-\varphi(y;t)|
\le C(1+\|s\|+\|t\|)\|x-y\|
 +C(1+\|x\|+\|y\|)\|s-t\|.
\]

The concatenated vector/scalar execution has \(\mathcal W_p\) error at most \(C_p\delta\), where kernel contraction dimensions also count as hidden widths. Because the limiting scalars are deterministic, this includes their \(L^p\) error. It is a real scalar-feedback theorem: later vector and matrix inputs can depend on earlier empirical kernels.

Unlike Theorem 1.2, Theorem 2.4 explicitly assumes **joint nondegeneracy of the infinite-width Gaussian matrix-output variables**. Remark 2.5 explains why the basic reduction is insufficient: a relation involving deterministic limiting scalar values need not remain an exact finite-width relation when those scalars fluctuate. For example, start with an iid standard Gaussian vector \(g\), form \(s=n^{-1}\|g\|^2\), then \(u=(s-1)\mathbf1\), and apply a fresh Gaussian matrix to \(u\). All these operations meet the displayed regularity restrictions, but the last Gaussian limit vanishes, so Theorem 2.4's nondegeneracy hypothesis fails. MFP's stated theorem expressly allows this type of singularity.

The attention application uses \(n^{-1}q^\top k\) scores and deterministic scalar limits. It does not establish a quantitative limit for the usual centered fluctuation scaling \(n^{-1/2}q^\top k\); Remark 2.3 says this requires a different scalar CLT. With independent centered query and key projections in the displayed example, the limiting scores are zero. A claim about arbitrary transformer attention would therefore overstate the result.

## What does and does not match MFP

| Question | Quantitative tensor-program paper | Assigned MFP sections |
|---|---|---|
| Repeated use of a matrix | Admitted in the same orientation, including recurrent uses | Both orientations of the same named matrix |
| Scalar feedback | Kernel extraction, scalar maps, parameterized coordinate maps; quantitative under the stated regularity and nondegeneracy | General admitted coordinate-expression averages, sums/products and feedback |
| Gaussian expectation evaluation | Recursive covariance and expectation evaluation already present | Adds source-response fields for transpose reuse and an explicit derivative compilation/evaluation chain |
| Nonsmooth activations | Globally Lipschitz activations, including ReLU, are allowed | The stated full derivative theorem uses smooth activations with polynomially growing derivatives |
| Polynomial coordinate expressions | General coordinate multiplication is outside global Lipschitz assumptions | Explicitly admitted and derivative closed |
| Degenerate limiting queries | Removed exactly for ordinary programs; excluded by hypothesis for the scalar extension | Explicitly admitted, including scalar-feedback programs |
| Quantitative finite-width control | Joint normalized-vector \(\mathcal W_p\), kernel/scalar \(L^p\), order \(\delta\) | Stated \(L^p\) scalar convergence and uniform moments, without a rate |
| Training derivatives and finite jets | No theorem closing arbitrary admitted forward/reverse AD, fixed gradient updates or flow jets | Exact finite-width rules and finite compilation asserted before taking limits |

There are three substantive reasons the derivative theorem is not supplied by this quantitative result.

First, differentiating \(\phi(z)\) in a vector direction \(v\) creates \(\phi'(z)v\). Even for \(\phi=\tanh\), the map \((z,v)\mapsto\phi'(z)v\) is not globally Lipschitz: choose fixed \(z_1,z_2\) with different \(\phi'\) values and let \(|v|\to\infty\). The change in the output is proportional to \(|v|\), while the change in the input \((z,v)\) is fixed. Equation (2.5) does not rescue this, because \(v\) is a neuron-dependent vector coordinate, not one global scalar parameter. Higher derivatives also generate coordinate products. Thus regularity of the original forward network does not verify the theorem's hypotheses for its differentiated program.

Second, ordinary reverse AD creates \(W^\top b\). Treating this as multiplication by a new independent named matrix changes the law: for a deterministic vector \(x\), already \(\mathbb E[W^\top Wx]=x\) for a square matrix with variance \(1/n\), whereas replacing \(W^\top\) by an independent centered matrix gives mean zero. MFP's source-response terms address precisely such shared-matrix dependencies. The quantitative paper's matrix-output GP rule has no corresponding transpose correction.

Third, finite-gradient updates require the derivative factors just described. Nevertheless, it would be inaccurate to say the quantitative language cannot express any represented matrix update. Once suitable factors \(u,v\) are available, a forward action

\[
\left(W+cuv^\top/n\right)h=Wh+cu(v^\top h/n)
\]

uses a permitted kernel and scalar-vector multiplication. The obstruction to a general gradient-update theorem is generating all factors and maintaining the analytic hypotheses, not merely lacking an updated-matrix primitive. Likewise, scalar arithmetic can sometimes be re-expressed using broadcast vectors and kernels; the direct restriction on scalar maps alone is not a proof of algebraic inexpressibility.

Consequently, specialized derivative queries whose *compiled* programs satisfy all the quantitative hypotheses may inherit a rate. The paper does not prove that MFP's full class does. It also has features outside the assigned MFP theorem, including nonsmooth Lipschitz activations and unequal-width/fixed-output formulations, so describing it simply as a subset of MFP would be wrong.

The Gaussian-expectation computation itself is established background. In the checked primary dependency, Yang's Theorem 5.4 and Definition 5.2 already give recursive Gaussian expectations for ordinary programs, and Appendix C.1 defines explicit scalar moment variables and recursive limiting scalars. Theorem C.11 requires parameter-control and rank stability, and proves almost-sure empirical/scalar limits. I checked that theorem's statement and its simultaneous-induction proof, not all upstream proofs. This is sufficient to rule out novelty claims based only on having an expectation graph or scalar feedback; it is not a verification of all transpose-program results elsewhere in the literature.

## Load-bearing proof audit

The overall strategy is sound in its intended scope: reveal adaptive linear matrix observations, couple each conditional Gaussian innovation, obtain kernel fluctuations from the already coupled past, and transfer those fluctuations through regression maps smooth at the limiting Gram data. I checked the conditioning and projection formulas in §§3.2–3.3, the nondegeneracy reduction, and the quantitative induction in all of §4.

For one matrix \(W\), let the columns of \(H\) be its previous query vectors and let \(G=WH\). Given the previous program values, the residual covariance of \(W\) is the right projection

\[
R=I-HH^+,
\]

and the next call has conditional law

\[
Wh\mid\text{past}\sim
N\!\left(GH^+h,\frac{h^\top Rh}{m}I_n\right).
\]

These formulas follow by projecting each independent Gaussian row onto the observed query span. Adaptively chosen queries are already measurable when the corresponding observation is revealed, and coordinate/scalar instructions add no new matrix observation. This explains both reuse and why scalar feedback preserves the conditioning formula. It does not justify a transpose extension.

The kernel LLN is not circular. Given the coupling for all preceding nodes, the difference of finite and barred empirical kernels is controlled by Cauchy–Schwarz and higher coupling moments. The remaining barred empirical average is a sum of iid coordinate products. All moments exist. For example, an even \(2k\)-th moment expansion of its centered sum has only terms in which no index occurs once; there are at most \(k\) distinct indices, hence an \(O(n^k)\) numerator and an \(O(n^{-1/2})\) bound in \(L^{2k}\) after averaging. This verifies the scalar consequence of Rosenthal's inequality needed here without requiring any dimension-dependent vector estimate.

The nondegeneracy reduction also has a valid intended mechanism. If a new parent is a deterministic linear combination of preceding parents in the limiting \(L^2\) space, their difference is a continuous function of preceding Gaussian coordinates. Earlier **conditional** nondegeneracy gives a jointly full-support Gaussian tuple. Vanishing almost surely therefore implies an identically zero continuous function, which also vanishes on finite-width executions. Multiplication by the same matrix gives an exact finite-width replacement. Mere nondegeneracy of each marginal would not justify this full-support argument; the sequential induction in Lemma 3.9 supplies the needed stronger property. For scalar-feedback programs the extra scalar coordinates have deterministic limiting values, so this identity-lifting argument fails, as the authors explicitly acknowledge.

### Error in the printed residual step, and its repair

On p.30 the proof defines

\[
Z_s=(g'-\mu_{W\mid\mathcal F_{s-1}}h')
       \sqrt{(h'^\top Rh')^+}
\]

and asserts that it equals the corresponding barred standardized residual and has conditional law \(N(0,I_n/m)\). As printed, this is not valid on the event \(h'^\top Rh'=0\): its displayed definition gives \(Z_s=0\). This event can have positive probability even with a nondegenerate limiting Gram. Take \(h'=\operatorname{ReLU}(g)\) for an iid centered Gaussian vector \(g\). All coordinates are negative with probability \(2^{-m}\), so \(h'=0\), although \(m^{-1}\mathbb E\|h'\|^2>0\). A subsequent reuse of the matrix invokes exactly this update. The barred pairing is also normalized by \(1/m\), so using literally analogous barred definitions changes the residual scale by \(\sqrt m\).

Here is the corrected version of the step, derived directly from the paper's coupling (4.7). Retain its common innovation \(e_s\sim N(0,I_n)\), including when the finite conditional variance is zero. For the previous query \(h'\) and the current target \(h\), put

\[
q=h'^\top Rh',\qquad
b=\begin{cases}
\displaystyle\frac{h'^\top Rh}{\sqrt m\sqrt q},&q>0,\\[4pt]
0,&q=0.
\end{cases}
\]

For barred variables, with \(a^*b=m^{-1}\mathbb E[a^\top b]\) and \(\bar R\) the limiting \(L^2\) projection, put

\[
\bar b=\frac{\bar h'^*\bar R\bar h}
                 {\sqrt{\bar h'^*\bar R\bar h'}}.
\]

The limiting denominator is positive after the ordinary-program reduction or under Theorem 2.4's hypothesis. The two regression-mean increments are exactly \(e_sb\) and \(e_s\bar b\). This remains true when \(q=0\), since then \(Rh'=0\) and the finite regression increment is zero. It is unnecessary, and incorrect, to recover \(e_s\) by dividing a zero observed residual.

Both coefficients are evaluations of the same function of **normalized** Gram entries. That function is smooth near the limiting point and obeys

\[
|b|\le\frac{\|h\|}{\sqrt m},\qquad
|\bar b|\le\sqrt{\bar h^*\bar h}.
\]

The past coupling and barred moment bounds therefore give uniform coefficient moments. Lemma 3.1, applied to the augmented Gram matrix containing earlier parents, \(h'\), and \(h\), gives \(\|b-\bar b\|_{L^{2p}}\le C_p\delta\). Hölder then yields

\[
\left\|\frac{e_s(b-\bar b)}{\sqrt n}\right\|_{L^p}
\le
\left\|\frac{e_s}{\sqrt n}\right\|_{L^{2p}}
\|b-\bar b\|_{L^{2p}}
\le C_p\delta.
\]

No independence between \(b\) and \(e_s\) is required: the current query can depend on that earlier innovation. Summing over the fixed number of earlier calls proves the intended mean stability estimate. This corrects the zero-residual problem and normalization together.

The covariance step is similarly justified by the square root of the normalized Gram Schur complement. It is smooth near the strictly positive limiting residual variance and bounded by \(\|h\|/\sqrt m\) globally on the actual Gram data. Lemma 3.1 controls the exceptional region as well; no inverse-moment assumption is necessary. The Gram matrices displayed on pp.29–30 need to include the current query and the earlier update query, not just the previously stored parent list in the literal indices shown there. These are available past nodes, so the enlarged kernel estimate supplies them.

Thus the important gap has a direct repair within the stated assumptions. This assessment supports the theorem's mechanism, while recording that the printed derivation is not correct verbatim. It is not a claim of a fully formal line-by-line independent certification of every auxiliary statement.

### Additional corrections and limits of the examples

The summed NonLin+ bound on p.32 omits a \(\sqrt m\) multiplying the scalar-error constant term before division by \(\sqrt m\). Restoring it gives the announced rate and requires no extra hypothesis.

The claimed one-line LayerNorm map in Example 2.2,

\[
\varphi(x;\mu,\sigma)=(x-\mu)/\sqrt{\sigma^2+\varepsilon},
\]

does **not** satisfy (2.5) globally. Set \(x=y=0\), \((\mu,\sigma)=(M,1)\), and \((\mu',\sigma')=(M,2)\). The left side grows linearly with \(|M|\), while the right side of (2.5) is bounded by \(C\). Also, the displayed scalar instruction \(\sigma=\sqrt{\sigma^2}\) is not globally Lipschitz, even on nonnegative inputs near zero.

These are repairable encoding failures. First form the centered vector \(h_c=h-\mu\), then its empirical variance \(v=h_c^\star h_c\), then the scalar \(a=(\varepsilon+\max(v,0))^{-1/2}\), and finally \(ah_c\). The scalar map has a globally Lipschitz extension, the centering and multiplication satisfy (2.5), and \(v\ge0\) on actual executions. This reproduces the regularized normalization. It still leaves the separate joint Gaussian nondegeneracy hypothesis to be checked for the particular full architecture and input set.

The numerical section does not verify any derivative, transpose or scalar-feedback theorem. It measures selected output laws for MLPs, an RNN and a residual network. Equation (5.2) uses an expected empirical-measure error as though it were a deterministic bound, and the text predicts a slope of \(-1/2\) from a fixed sample-size noise floor. With fixed ensemble size, such a floor is width-independent and would ultimately flatten to slope zero. These problems limit the interpretation of the fitted slopes, not the conditional-Gaussian proof.

## Defensible positioning

A precise comparison would say that Agazzi–Mosig García–Trevisan provide inverse-square-root-width Wasserstein estimates for forward tensor programs with Lipschitz nonlinearities and for a nondegenerate kernel-feedback extension. MFP's claimed additional scope is closure of its specified smooth polynomial-growth derivative queries, transpose reuse, finite updates and finite jets into a singularity-tolerant Gaussian expectation computation, together with expectation convergence. Establishing the novelty and correctness of that additional scope still requires comparison with the broader transpose/scalar tensor-program results and verification of MFP's own proofs; this paper alone neither supplies nor refutes it.

The assigned question is therefore answered by an actual scope separation, with a quantitative advantage credited to the new paper and proof corrections recorded. Neither its title nor its use of a tensor-program language establishes a full derivative-calculus equivalence.
