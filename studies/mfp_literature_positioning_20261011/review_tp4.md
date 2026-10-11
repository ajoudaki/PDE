# Scoped audit: Tensor Programs IV and the MFP finite calculus

Audit date: 2026-10-11. Reviewer scope: Greg Yang and Edward J. Hu, *Tensor Programs IV: Feature Learning in Infinite-Width Neural Networks*, its complete proceedings paper and supplement, latest arXiv text and version history, the directly load-bearing TP III master theorem, and narrowly relevant primary software. Repository comparison inputs are `docs/02-gaussian-reuse.qmd:252–1293`, `docs/12-three-sample-learning.qmd:316–684`, `paper_MFP/main.tex`, and `paper_MFP/code/MFP_CALCULUS.md`. This audit does not incorporate another reviewer's findings or other studies.

**Assessment.** TP IV is direct prior work for the MFP neural scaling, finite training-history lowering, Gaussian source-response evaluator, and the idea of mechanically compiling a neural computation to its infinite-width limit. In particular, its maximal-update parameterization is the same finite-width neural model as MFP's order-one stored input/readout parameters with mobilities `(n,1,…,1,n)`, after an explicit change of variables below. It already computes initial second derivatives of feature moments and third derivatives of an output with respect to a single SGD step's learning rate. MFP's defensible emphasis relative to this source is the specified finite physical differentiation interface, moving-flow and path jets, typed represented directions and updates, exact symbolic implementation and examples, and its separately proved uniform moments and all-finite-`L^p` conclusions. This is not a finding that MFP introduces a new general Gaussian program theorem; the current MFP introduction expressly makes no such claim.

The distinction between results and proof verification matters here. The exact finite-step lowering and its hypotheses can be checked directly. Its probabilistic foundation is TP III, Theorem E.15, explicitly invoked by TP IV. This audit does not certify every step of that theorem's compressed rank-removal proof. Separately, TP IV's classification proof contains demonstrably incorrect printed derivative coefficients and small-smoothing asymptotics, including in the latest arXiv version. Those errors do not establish that its main classification conclusions are false, and they do not remove the earlier fixed-step evaluator or parameterization correspondence.

## Sources, versions, and reading coverage

Primary links:

- [ICML/PMLR record](https://proceedings.mlr.press/v139/yang21c.html), PMLR 139, 11727–11737, 2021.
- [Proceedings main PDF](https://proceedings.mlr.press/v139/yang21c/yang21c.pdf), 11 PDF pages.
- [Proceedings supplement](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf), 38 PDF pages.
- [arXiv record and version history](https://arxiv.org/abs/2011.14522); title there is *Feature Learning in Infinite-Width Neural Networks*.
- [arXiv v3](https://arxiv.org/pdf/2011.14522v3), 65 pages, 2022-07-15; [v2](https://arxiv.org/pdf/2011.14522v2), 65 pages, 2021-05-11; [v1](https://arxiv.org/pdf/2011.14522v1), 63 pages, 2020-11-30.
- [Primary experimental software](https://github.com/edwardjhu/TP4), inspected revision `b640ba72aee46c641a18ac9b29f09c31ff967597`, commit dated 2021-05-11.

Downloaded artifacts and extracted pages are in `data/generated/mfp_literature_positioning_20261011/tp4/`. SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `main.pdf` | `d93eaf9ca5263627e96eb9c56dd60605aee3ed9f86bef4da3fed1d41dd2198c3` |
| `supp.pdf` | `c397e68fd2bc9a3333c49c5b1a07e064c9e8ba0d1868628fc6d19a7104d3c12a` |
| `arxiv-v1.pdf` | `423d40a55229b05354a93747bfbaef8d9cec35ab59bc104a5e1cdb5a66c02bcd` |
| `arxiv-v2.pdf` | `005045036221ac17f413c65d880ac339ac2d3e04acf270c678918899cdaf330d` |
| `arxiv-v3.pdf` | `60d2df4b6b8797cd92d6384ad41181436584012988695ff750b9f30c54e777d2` |

Reading coverage is complete for proceedings main pp. 1–11, supplement pp. 1–38, and arXiv v3 pp. 1–65, including references, experiments, every appendix, and all proof sections. The latest PDF's p. 60 was also visually inspected to verify that the derivative/asymptotic problems below are not extraction artifacts. Earlier versions were inspected by textual differences and selected original pages; this is not a claim to have independently reread all 63 pages of v1 or all 65 pages of v2. The complete v2–v3 textual diff was read. The larger v1–v2 diff was examined for changes affecting hypotheses and conclusions, with the original master-theorem and regularity passages checked directly.

Consequential version observations:

1. The rank-free, scalar-feedback master theorem is present already in v1, Theorem 7.4, pp. 24–25, citing TP III E.15; its assumptions are v1 E.4, p. 40. It is not a late repair that first introduced scalar feedback or removed a rank assumption in 2022.
2. V2 adds discussion and reorganizes appendices, including the detailed deep-mean-field comparison, and clarifies the weak existential definition of feature learning (v3 Remark H.10, p. 45). The central evaluator is substantively retained.
3. Compared with the proceedings supplement, arXiv v2/v3 correct the one-step derivative discussion to evaluate vanishing first derivatives at `η=0`, and use the Gaussian activation adjoint `Z^{dx_0^l}`, rather than the generally non-Gaussian preactivation adjoint `Z^{dh_0^l}`. Compare supplement N.7 pp. 33–35 with arXiv H.7 pp. 58–60.
4. V2→v3 corrects the covariance of the decoupled backward signal in footnote 31, p. 17, to use the upper-layer preactivation adjoints. It also renames the initial Gaussian backward variable from a dotted symbol to `\widetilde Z_0^l`, avoiding confusion with the source-response correction, throughout H.7. High-level theorem statements are unchanged. The derivative and smoothing issues documented below remain in v3.
5. A bounded search for the exact title together with “erratum” or “correction” did not locate an authoritative separate erratum. This does not prove none exists.

Software inspection covered the repository README, both experiment READMEs, and the complete `TP4MAML/meta/maml/model.py`. These exact files are preserved at the pinned revision in the generated directory. No experiments, software tests, or benchmarks were run. No other software repository was audited. One overly broad filename-scoped search of the permitted Quarto chapter inadvertently displayed isolated matches outside lines 252–1293; those matches were discarded and are not used for any conclusion here.

Unless marked otherwise, page numbers below refer to **arXiv v3**; proceedings/supplement correspondences are supplied for the central results.

## Exact parameter correspondence

Use the MFP convention: `z^l` denotes a preactivation and `h^l=φ(z^l)` an activation. For fixed input dimension `d`, MFP's neural example uses

\[
z^1(x)=B x/\sqrt d,\qquad
z^l(x)=W^l h^{l-1}(x)\ (2\le l\le L),\qquad
f_n(x)=a^T h^L(x)/n.
\]

The stored input matrix `B` and stored readout `a` have order-one Gaussian entries; the hidden matrices have independent `N(0,1/n)` entries. Each column of `B` and the vector `a` are vector-root parameters. Their physical mobilities are `n`, while the hidden matrices' mobility is one; fixed block multipliers can be included. These are the models and rules in `docs/02-gaussian-reuse.qmd:910–941`, the guide's gradient section at lines 200–215, and its two-hidden-layer examples at lines 247–355. The statement applies to this expressly declared order-one readout model, not to every other initialization in the book.

TP IV uses `h^l` for preactivation and `x^l` for activation. Its actual forward matrices are `W^l_TP=n^{-a_l}w^l`, while `w^l` are the trainable variables, initialized with entry variance `n^{-2b_l}`. The global learning rate is `ηn^{-c}` (Eq. (1), p. 2). Its μP choice is

\[
a_1=-\tfrac12,\quad a_l=0\ (2\le l\le L),\quad
 a_{L+1}=\tfrac12,\quad b_l=\tfrac12,\quad c=0.
\]

See Definition 5.1, p. 14; proceedings Definition 4.1, p. 5. Define trainable TP variables

\[
u=B/\sqrt n,\qquad v=a/\sqrt n,
\]

and feed TP the fixed rescaled input `ξ=x/√d`. Its actual first and last matrices are then `√n u=B` and `v^T/√n=a^T/n`, respectively, while the hidden trainable matrices are exactly `W^l`. Thus the finite-width forward maps agree, not merely their limiting exponents. The input factor and fixed initialization constants are explicitly allowed in TP IV's footnotes 4 (p. 2) and 24 (p. 15).

For any scalar loss `\mathcal L`, chain rule gives `∇_u\mathcal L=√n∇_B\mathcal L`. A Euclidean step `u^+=u−η∇_u\mathcal L` therefore becomes

\[
B^+=B-\eta n\nabla_B\mathcal L,\qquad
 a^+=a-\eta n\nabla_a\mathcal L,\qquad
 (W^l)^+=W^l-\eta\nabla_{W^l}\mathcal L.
\]

The same change of variables gives these mobilities for a gradient vector field. Dataset averaging and a factor `1/2` in the loss are fixed constants, to be matched when comparing numerical coefficients. They are not different width regimes. TP IV's “MFP” abbreviation elsewhere means shallow **mean-field parameterization**, not the present repository's mean-field peeling.

Consequently, a novelty statement that MFP first admits feature learning under this Gaussian initialization and these block mobilities would be incompatible with TP IV. A claim about an explicitly computed new observable, compiler interface, or proof strength must instead be judged at that narrower level.

## What the fixed-step evaluator already supplies

Definition 7.1, p. 23 (supplement G.1, p. 12), is the scalar-feedback language `NETSOR^{\top+}`: matrix/transpose multiplication, coordinate maps depending on earlier scalars, and normalized empirical moments. It retains one named Gaussian initialization for every matrix, reused at all later training times. Setup 7.2 uses independent Gaussian matrix entries, a fixed jointly Gaussian root tuple, and initial scalars converging almost surely to deterministic limits. Singular root covariance is not excluded.

For a matrix with entry variance `σ_W²/n`, Definition 7.3, p. 24, Eq. (31), defines

\[
Z^{Wx}=\widehat Z^{Wx}
 +\sigma_W^2\sum_{i} Z^{y_i}
     \mathbb E\left[\frac{\partial Z^x}
      {\partial\widehat Z^{W^Ty_i}}\right],
\qquad
\operatorname{Cov}(\widehat Z^{Wx},\widehat Z^{Wu})
 =\sigma_W^2\mathbb E[Z^x Z^u].
\]

The sum uses prior opposite-orientation calls. Gaussian source groups for different oriented matrices are independent, but the resulting vectors can depend on many such groups. Earlier deterministic scalar limits and covariance/expectation coefficients are fixed when taking the displayed formal partial. This is the MFP source-response rule after setting `σ_W=1`, assigning vector types, and translating notation. It is not the physical parameter derivative used to produce the input program.

Remark F.1, p. 41 (supplement L.1, p. 21), explicitly says that the derivative is a derivative of the expression obtained from the actual program, not merely of the resulting random variable; alternative expressions can have different individual partials. Remark F.2 uses a pseudoinverse to interpret response expectations for nonsmooth expressions. At singular covariance, its statement that the pseudoinverse “agrees” with derivative coefficients must be understood at the level of the **total response**, not necessarily each coefficient: if `C=E[YY^T]` and `b=C a`, then `Y^TC^+b=Y^Ta` almost surely since `Y` annihilates `ker C`. Duplicate opposite-orientation queries are therefore compatible with the law. MFP's explicit preservation of all formal source slots is a useful interface and explanation of the same invariant response.

Theorem 7.4, p. 25 (supplement G.4, p. 14), explicitly cites **TP III Theorem E.15** and states almost-sure convergence of every scalar and of

\[
\frac1n\sum_{\alpha=1}^n
 \psi(v^1_\alpha,\ldots,v^k_\alpha)
 \longrightarrow
 \mathbb E\psi(Z^{v^1},\ldots,Z^{v^k})
\]

for fixed finite node tuples and every pseudo-Lipschitz test `ψ`. Assumption F.4, p. 41 (supplement L.4, p. 21), requires coordinate maps and moment maps with at least one vector input to be jointly pseudo-Lipschitz in vector and scalar arguments. Pure scalar maps need only be continuous. There is **no rank-stability assumption in this theorem**. The lingering phrase “and rank stability” in the narrative program setup (p. 49; supplement p. 27) does not override its stated hypotheses. Arbitrary repeated use of both orientations, scalar averages used in later instructions, polynomial observables, singular Grams, and duplicate queries are within the stated theorem. Smooth functions with polynomially bounded derivatives, as in MFP, satisfy its regularity conditions by the mean-value theorem.

The source does not claim finite-width coordinates are actually independent. Its “roughly iid” description is shorthand for this empirical law theorem. Almost-sure empirical convergence plus second-moment convergence implies almost-sure `\mathcal W_2` convergence of the joint empirical laws. By contrast, almost-sure convergence of scalar outputs alone does not establish convergence of their expectations or uniform initialization moments. TP IV does not prove the general all-finite-`L^p`/uniform-moment conclusion asserted by the MFP theorem. That part must be supplied by MFP's separate estimates (and its attributed dependencies), not silently inferred from Theorem 7.4.

For training, Assumption H.22, p. 48 (supplement N.21, p. 27), is that `φ'` is pseudo-Lipschitz and not almost everywhere zero; the loss derivative in the output is continuous. The text also describes this as a polynomially bounded weak second derivative of the activation (p. 5). This is substantially weaker than requiring all orders of classical derivatives, but does **not** automatically give the paper's backpropagation theorem for ordinary ReLU: its discontinuous derivative fails the stated pseudo-Lipschitz requirement. The piecewise/singular initialization discussion concerns images of Gaussian roots under admissible maps; it is not permission for arbitrary heavy tails or arbitrary discontinuous training maps.

## Reconstructed finite-step proof and its limits

The load-bearing mechanism is an exact algebraic lowering followed by the master theorem. It does not need the later dynamical-dichotomy theorem.

Write `b^l_{t,s}=n∇_{z^l_t(x_s)}f_t(x_s)` for normalized preactivation adjoints and `χ_{t,s}=∂_f\ell(f_t(x_s),y_s)` for loss derivatives. For a fixed minibatch, averaging constants can be absorbed in `χ`. A hidden matrix step has the exact form

\[
W^l_{t+1}=W^l_t-\frac\eta n
 \sum_s\chi_{t,s}\,b^l_{t,s}(h^{l-1}_{t,s})^T.
\]

After fixed `T` steps, `W^l_T` is its initialized Gaussian matrix plus finitely many represented normalized outer products. Acting on a new vector `q` gives

\[
W^l_Tq=W^l_0q-\eta\sum_{t<T,s}\chi_{t,s}b^l_{t,s}
 \left\langle h^{l-1}_{t,s},q\right\rangle_n,
\quad \langle u,v\rangle_n=n^{-1}u^Tv.
\]

Its transpose acts by the corresponding reversed outer products. Hence all changing-matrix calls become calls to the same initialized Gaussian matrix plus coordinate maps and empirical scalar contractions. This is the same represented-update lowering used by MFP. Exact source locations are Eqs. (21)–(24), pp. 17–18, and H.3–H.4, pp. 49–52; proceedings supplement Eqs. (48)–(52), pp. 28–29. Printed occurrences of `h` where a preactivation adjoint `dh` is required in the final terms of Eq. (47)/(48) are transcription errors: the left-hand gradient formula and the subsequent program determine the adjoint unambiguously.

Forward activations use `φ`; backward activations use `φ'` and multiplication; empirical inner products use polynomial moment maps; `χ` uses the allowed continuous scalar map. Thus a fixed finite history satisfies F.4 when H.22 holds. In μP all required normalization powers are constant or vanish, as seen directly from its exponents. Applying Theorem 7.4 to the entire finite union of training and testing computations gives the joint almost-sure limits. This verifies the reduction and hypothesis matching conditional on the cited master theorem.

The first two training passes also expose the genuine transpose response. In the two-hidden-layer example, with TP notation and one datum,

\[
Z^{x_1(\xi)}
 =\phi\bigl(\xi Z^{U_0}
       -\chi_0\xi_0\xi\,\phi'(\xi_0Z^{U_0})
          \widehat Z^{W^T\bar d h_0}\bigr).
\]

Its response to the next forward `W` call is

\[
-\chi_0\xi_0\xi\,
 Z^{\bar d h_0}\,
 \mathbb E[\phi'(Z^{h_1(\xi)})\phi'(Z^{h_0})].
\]

Here `\bar d h_0` denotes TP's upper-layer preactivation adjoint `d\bar h_0`, not a new independent copy. This is derived explicitly on pp. 20–21, Theorem 6.4 and its example (supplement F.2, pp. 9–10). Its earlier decoupled model, Theorem 6.3, uses an independent copy of the backward matrix deliberately; the paper then corrects it to ordinary backpropagation. Treating the decoupled model as the paper's final result would miss the central comparison.

The finite-step statements hold for each fixed training horizon, fixed depth, and fixed finite collection of inputs; no rate in width, horizon growing with width, continuous-time trajectory theorem, or global training stability estimate is established by this argument. “Stable” in Definition H.4 permits bounds depending on time and learning rate, and does not mean loss decrease or boundedness as time tends to infinity. The last proof on p. 64 attempts to extend pointwise convergence from a dense input set by local Lipschitz continuity. A full uniform equicontinuity estimate would be needed to use that argument as a stronger function-space convergence theorem; I have not supplied it. The fixed finite-input conclusions used here avoid this additional step entirely.

The inherited dependency is specifically TP III E.15, not an unspecified assertion that all tensor programs work. I read the complete TP III v3 separately in this assignment and reconstructed its base transpose theorem and conditioning argument. Its E.15 proof in Appendix N, pp. 85–87, contains a malformed normalization and a compressed vanishing-direction coefficient claim in Lemma N.2 whose full quantitative justification I did not independently verify. That is a proof-check limitation, not a counterexample to E.15. TP IV supplies an application of this theorem, not an independent proof of its rank-free scalar-feedback case. The smooth polynomial MFP specialization can instead be supported by its own perturbation, truncation, and moment argument.

## Higher derivatives, physical differentiation, and compilation

TP IV already has two kinds of derivatives relevant to the comparison:

1. Physical backpropagation at each finite training state, including the normalized adjoints `n∇_z f` (p. 15; H.4 pp. 51–52).
2. Formal source partials in the Gaussian response law, holding earlier scalar limits fixed (Eq. (31), p. 24; Remark F.1, p. 41).

It also explicitly analyzes learning-rate derivatives of the infinite-width **one-step** feature statistics. In H.7, pp. 57–62 (supplement N.7 pp. 33–37), it defines

\[
\gamma^l(\eta)=\mathbb E[\phi(Z^l_0)\phi(Z^l_1(\eta))],\qquad
\lambda^l(\eta)=\mathbb E[\phi(Z^l_1(\eta))^2].
\]

It proves vanishing first derivatives, derives second-derivative recurrences, and uses a third derivative of the first-step output to argue that its dependence on the learning rate is not linear. These are genuine higher-derivative calculations, despite the errors in some printed coefficients below. Therefore “TP IV has no higher derivatives” or “only forward/backward initialization laws” is inaccurate.

The physical quantity is different from a moving-flow jet. For a state `θ`, smooth observable `O`, and vector field `V`, a single explicit step gives `O(θ+ηV(θ))`; its second derivative at zero is `D²O(θ)[V,V]`. The flow `\dot θ=V(θ)` gives instead

\[
\left.\frac{d^2}{dt^2}O(\theta(t))\right|_{t=0}
 =D^2O(\theta)[V,V]+DO(\theta)[DV(\theta)[V]].
\]

MFP's guide lines 128–198 explicitly distinguishes these operations, frozen seed data, and factorial-normalized path coefficients. Its feature-kernel example lines 277–355 takes finite-width moving derivatives before the width limit; all residuals, parameters, and reused transposes move. TP IV's `λ''(0)` for a single update cannot simply be substituted for this quantity. Conversely, the TP language is already broad enough to encode any such **fixed finite differentiated program**, provided that its derivative maps satisfy the master theorem. MFP's finite algebraic closure establishes this admissibility concretely; it does not reveal a new class of primitive probabilistic operations absent from TP IV.

This order of operations is useful mathematically. Pointwise convergence of `O_n(η)` to `O_∞(η)` does not by itself justify exchanging a derivative and a width limit. Compiling `∂_η^r O_n` exactly at finite width and then applying the master theorem directly proves the limit of the requested derivative observable. It need not assert that this equals the derivative of a positive-time limiting trajectory. The current MFP introduction and guide maintain this boundary.

Algorithm 1, p. 25 (supplement p. 15), already instructs the reader to express the complete training/inference computation as a tensor program, recursively calculate all source representatives and scalar expectations, and read off the output. A general claim that MFP originates the idea of a compiler from finite neural computation to Gaussian expectations would therefore be overstated. A narrower claim about a concrete typed frontend, two derivative engines, exact rational polynomial reduction, provenance-preserving source slots, and exposed Gaussian expectation DAGs is an implementation claim requiring direct comparison of implementations.

The inspected TP4 software supports the concrete experimental reduction rather than demonstrating a universal symbolic frontend: `MetaInfLin1LP` in [`model.py`](https://github.com/edwardjhu/TP4/blob/b640ba72aee46c641a18ac9b29f09c31ff967597/TP4MAML/meta/maml/model.py#L139) explicitly creates hidden size `d+d_out` with diagonal block initialization. This matches Corollary 6.2, p. 16, Theorem D.1, p. 36, and Algorithm 3, p. 37. I did not inspect every file and do not infer the absence of other capabilities from these selected files. The complete paper describes the general symbolic recipe and these special numerical realizations; it does not specify the full MFP physical-derivative API or a general executable symbolic compiler of that interface.

## Independently checked proof defects and bounded implications

These checks concern the classification proof, not the basic representation of finite SGD or the stated TP master theorem.

**First derivative repair across versions.** In the proceedings supplement N.37, p. 34, the displayed recurrence omits evaluation at zero and its proof treats a Gaussian backward variable as independent from the updated feature. That independence is valid at initialization, not for general nonzero learning rate. ArXiv Lemma H.38, p. 59, correctly states the recurrence at zero and says so in the proof. This repair must be recognized before criticizing the current paper.

**Factor error in second derivatives.** In the one-hidden-layer μP case with input `ξ_0=1` and `χ_0=1`, let `Z,A` be independent standard Gaussians. The exact one-step preactivation is

\[
Z_1(\eta)=Z-\eta A\phi'(Z).
\]

For the smooth activations used in H.7, differentiation under expectation is justified by polynomial domination on a compact interval of `η`; Gaussian moments are finite. Direct chain rule gives

\[
\begin{aligned}
\lambda''(0)&=\mathbb E[(\phi^2)''(Z)\phi'(Z)^2],\\
\gamma''(0)&=\mathbb E[\phi(Z)\phi''(Z)\phi'(Z)^2],\\
\left.\frac{d^2}{d\eta^2}\mathbb E Z_1(\eta)^2\right|_0
 &=2\mathbb E[\phi'(Z)^2].
\end{aligned}
\]

Theorem H.41, p. 60 (supplement N.40, p. 35), instead sets `C=2(β^l(0))²E(\widetilde Z_0^l)²`; in this example `β^1(0)=−1` and `C=2`, doubling the first two values. Theorem H.43 on the same page predicts `2C=4` for the third value, omitting its activation factor. The proof differentiates `φ²` and introduces an extra factor two. For any fixed σ-gelu, the first integrand is strictly positive, so this is an actual numerical disagreement within the stated smooth nonlinear setting, not merely an issue with a zero expression. The displayed formulas were visually confirmed in the PDF. The cubic-output display in H.46/H.49 also omits the factor three from `d³[-ηq(η)]/dη³|_0=−3q''(0)`. A common nonzero factor may leave a sign/nonvanishing argument intact, but these displayed coefficients are not reliable formulas to reuse in MFP.

**Incorrect smoothing asymptotics.** Definition H.1, p. 43, specifies

\[
\phi_\sigma(x)=\tfrac12x\operatorname{erf}(x/\sigma)
 +\frac{\sigma}{2\sqrt\pi}e^{-x^2/\sigma^2}+\tfrac12x.
\]

Thus `φ_σ'(x)=(1+erf(x/σ))/2` and `φ_σ''(x)=e^{-x²/σ²}/(σ√π)`. For `Z∼N(0,q)`, `q>0`, with density `ρ_q`,

\[
\mathbb E\phi_\sigma''(Z)^2
 =\frac1{\pi\sigma}\int_{\mathbb R}e^{-2u^2}\rho_q(\sigma u)\,du
 \sim\frac{\rho_q(0)}{\sigma\sqrt{2\pi}}\longrightarrow\infty.
\]

Also `2Eφ_σ'(Z)²→1` by dominated convergence, while `2Eφ_σ(Z)φ_σ''(Z)→0` by the substitution `z=σu` and `φ_σ(σu)=σφ_1(u)`. Therefore

\[
\mathbb E(\phi_\sigma^2)''(Z)\longrightarrow1.
\]

Proposition H.44, p. 60 (supplement N.43, p. 35), states that both quantities tend to zero. That statement is false as printed. In fact the same one-hidden-layer calculation gives `λ''(0)→1`, whereas H.45, p. 61, says it tends to zero. The proof of H.46 explicitly uses the wrong behavior of `γ_{22}=Eφ''²`, so repairing the complete small-σ argument requires more than changing an irrelevant sentence. I have not supplied a full corrected classification proof. None of these examples refutes the existence of the μP feature-learning limit, the fixed-step source recursion, or even the final classification result; they refute specific printed intermediates and prevent certification of that proof as written.

**Gaussian expectation differentiation.** Lemma H.39, p. 59 (supplement N.38, p. 34), is the covariance differentiation identity

\[
\partial_\eta\mathbb E F_\eta(G_\eta)
 =\mathbb E\partial_\eta F_\eta(G_\eta)
 +\tfrac12\langle\mathbb E\nabla^2F_\eta(G_\eta),\partial_\eta\Sigma_\eta\rangle,
\quad G_\eta\sim N(0,\Sigma_\eta).
\]

Mere `C²` regularity, as written in the lemma, is not an integrability hypothesis. The actual fixed-σ tanh/σ-gelu applications have sufficient polynomial bounds to justify Gaussian integration by parts and differentiation on bounded parameter intervals. At the singular covariance at `η=0`, the density proof needs regularization, e.g. `Σ_η+εI`, followed by domination as `ε↓0`. This standard repair verifies the identity needed here; it does not fix the incorrect subsequent coefficients. I did not separately audit the cited batch-normalization paper's Lemma F.18, since this identity was checked directly under the hypotheses actually used.

Other parts of the classification proof, including all “straightforward calculations” for transfer-learning claims and all sign assertions for tanh, were read but not independently re-proved in full. The classification scope is tanh or sufficiently small σ-gelu (Assumption 3.1 p. 8; H.13 p. 46). The paper itself explains that linear activations can admit both changing features and kernel dynamics, so its dichotomy cannot be exported to every activation in MFP's language. Feature learning is an existential change in an embedding or its kernel for some training routine, rather than a universal downstream-performance theorem (H.9–H.11 pp. 44–45).

## Computation and empirical evidence

Section 8, pp. 25–26 (supplement H, p. 15), explicitly warns that generic exact evaluation is difficult. Nested activation expressions lack general closed forms; Monte Carlo errors may accumulate; nonlinear polynomial activations can produce rapidly growing polynomial degree; additional training steps introduce Gaussian sources and their cross-covariances; opposite-orientation response sums grow with history. The source describes an `Ω(t²)` covariance-storage burden in generic deep trajectories and potentially exponential or worse symbolic expansion. Its particular count does not constitute an unconditional lower bound on every possible algorithm. The relevant conclusion is that the source itself distinguishes a formal finite Gaussian representation from a generally efficient solver.

The same boundary appears in MFP's guide lines 114–126 and 366–416: fixed program sizes and derivative orders, potentially large symbolic graphs, no automatic numerical integration, and no positive-time population solver. An efficiency claim for MFP would need measured tasks and complexity analysis beyond the existence of its compiler. TP IV's shallow linear reduction is an explicit efficient special case and should not be overlooked.

Reported, not reproduced, experiments:

- Figure 4, p. 27 (supplement Figure 6, p. 16), compares exact limits for linear/quadratic shallow and two-hidden-layer networks, including ordinary and deliberately decoupled backpropagation, with widths 1024/4096 and 100 initializations. These are short-horizon theory checks, not general long-horizon nonlinear population computation.
- Table 2, p. 28, reports 1-shot 5-way Omniglot with first-order MAML: the shallow linear μP limit reaches `66.42±0.19%`, compared with `47.82±0.04%` for its ReLU NTK baseline. Finite large-width linear results are close; the table does not support a strict ordering over every finite width. The displayed error bars are subject to the experimental procedure: Appendix D.1, p. 38, footnote 47 (supplement p. 18, footnote 42), says the 15-seed rerun excludes outliers at least one standard deviation from the mean. These are reported statistics, not independent certification or universal superiority claims.
- Table 3, p. 30, reports Word2Vec analogy accuracy `43.31%` on text8 and `56.45%` on fil9 for the linear μP limit, with finite-width comparisons. The primary [Word2Vec README](https://github.com/edwardjhu/TP4/blob/b640ba72aee46c641a18ac9b29f09c31ff967597/Word2Vec/README.md) discloses race conditions in its CPU implementation and machine-dependent numerical results. No reproduction is claimed here.

## Positioning conclusions supported by this inspection

| Proposed scope of contribution | Comparison supported by TP IV |
|---|---|
| Feature learning for Gaussian hidden weights and MFP's mobilities | Already directly present as μP; finite-width correspondence shown above |
| Fixed finite training histories with changing matrices | Already represented by initialized matrices plus normalized outer-product histories |
| Causal scalar feedback, arbitrary transpose reuse, singular/duplicate query laws | Already in the explicitly cited TP III E.15 / TP IV 7.4 theorem and source rule |
| General mechanical route from a neural computation to Gaussian expectations | Explicit Algorithm 1, p. 25 |
| Any use of higher derivatives of feature statistics | Already present in H.7; published coefficient errors should be acknowledged if formulas are reused |
| Exact finite physical differentiation, moving-flow/path jets, frozen seed semantics, typed API | A concrete MFP package and exposition to assess on its specified interface; compiled primitives remain within TP's existing probabilistic scope |
| Uniform initialization moments and every finite `L^p` convergence | Not supplied by TP IV's almost-sure empirical master theorem; requires the separate MFP moment argument |
| General efficient numerical or symbolic population solver | Neither source establishes this; TP IV gives a useful special shallow-linear reduction |
| Positive-time flow reconstruction from finitely many jets | Not established by either the fixed-step TP result or MFP's finite-jet theorem |

The current MFP introduction (`paper_MFP/main.tex:299–306`) is compatible with this comparison because it attributes its moment mechanism and disclaims a new general probabilistic program theorem. Strong positioning should nevertheless cite TP IV alongside TP III when discussing finite training, μP scaling, compilation, and higher derivatives of feature moments. The paper-specific analytic errors and proof-check limitations above should be kept separate from these substantial and explicit prior-art overlaps.
