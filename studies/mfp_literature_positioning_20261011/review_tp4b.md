# Scoped audit: Tensor Programs IVb and the MFP finite derivative evaluator

Date: 2026-10-11. Reviewer scope: the complete primary TP IVb paper and directly load-bearing primary dependencies; the specified established passages of `docs/02-gaussian-reuse.qmd` (lines 252–1293), `docs/12-three-sample-learning.qmd` (316–684), `paper_MFP/main.tex`, and `paper_MFP/code/MFP_CALCULUS.md`. No other study or reviewer report was used. Required canonical-notation and rigorous-mathematics skills were applied. This report is an independent comparison, not a promotion review of MFP's proof or implementation.

## Finding

TP IVb is direct, substantial prior art for the mathematical part of MFP. Its NEXORT language contains MFP's primitive language; its Gaussian source-response rule is the same rule; it explicitly constructs backpropagation programs; it states almost sure and every-finite-`L^p` scalar convergence under polynomial smoothness; and it treats fixed finite training with general input geometry and considerably more general adaptive updates than finite sums of rank-one SGD updates. Calling these ingredients absent from Tensor Programs would be incorrect.

MFP's documented contribution can still be described concretely: a typed executable interface that lowers specified physical derivatives and represented updates, preserves distinct formal sources at singular covariance, emits inspectable Gaussian expectation graphs, and reduces suitable initialization expressions to activation moments or exact polynomial moments. Full inspection of TP IVb did not reveal an implementation of that particular compiler interface, nor its particular frozen/moving/seed API or initialization normal-form theorem. This supports a limited comparison of the inspected artifacts, not a general priority claim about all software or literature. TP IVb already offers a symbolic mathematical evaluation procedure and explicit derivative-program constructions; executable packaging must not be described as the invention of those constructions.

There are proof limits worth retaining. The Gaussian argument for initial scalars with the stated subpolynomial `n^{-1/2}` rate is developed in detail. The extension to arbitrary slowly converging initial scalars explicitly defers its full proof. The non-Gaussian extension is presented by adaptation of Golikov–Yang (2022), whose central moment proof was checked below. For MFP's deterministic initial scalars, Gaussian matrices, and primitive coordinate/average language, the relevant overlap avoids both the deferred slow-scalar proof and the extra nonlinear-outer-product universality argument.

## Sources, versions, and complete-reading coverage

Primary source: Greg Yang and Etai Littwin, *Tensor Programs IVb: Adaptive Optimization in the Infinite-Width Limit*, [arXiv:2308.01814](https://arxiv.org/abs/2308.01814). The landing page identifies it as the complete version of the ICLR 2023 paper *Adaptive Optimization in the Infinite-Width Limit*.

| Artifact | Version/date | Pages | SHA-256 |
|---|---|---:|---|
| `tp4b-v1.pdf` | arXiv v1, 3 August 2023 | 87 | `9f67f1b574793b39eb0b48aa8b8d9bc74019147a56fb6968a6c6139b13611843` |
| `tp4b-v2.pdf` | arXiv v2, 7 August 2023; latest listed at audit | 87 | `fb5653c418d4b35dbd5133810cc9313a75a2167b820dada18d6428b3bb0538b1` |


PDF URLs are [v1](https://arxiv.org/pdf/2308.01814v1) and [v2](https://arxiv.org/pdf/2308.01814v2). Files are respectively 2,098,583 and 2,098,654 bytes. All generated material is in `data/generated/mfp_literature_positioning_20261011/tp4b/`.

I read every page of v2, including front matter, all of Chapters 1–5, all proof sections, experiments, acknowledgements, and bibliography. Specifically: pp.1–11 framing/notation; pp.12–41 all result statements and extensions; pp.42–53 classification and training proofs; pp.54–80 the entire master-theorem development; pp.81–87 experiments and references. There is no uninspected appendix in the latest 87-page text. I read the complete layout-text diff of v1 against v2: the only extracted changes are author affiliation/front-page formatting. Mathematical text is unchanged in that comparison. I did not perform a pixel-level comparison of the two PDFs.

The [ICLR conference PDF](https://openreview.net/pdf?id=zgVDqw9ZUES) could not be downloaded: direct retrieval returned HTTP 403 and the browser endpoint returned its verification challenge. Its search-index excerpt and the arXiv landing metadata were accessible, but I have not read that separate PDF or claimed a complete conference-to-arXiv change audit. The complete arXiv version itself was accessible and fully read. Bounded searches for the paper title with “erratum”, “correction”, and “code”, and the arXiv version history, found no separately identifiable primary erratum or paper-linked compiler repository. That is a search result, not evidence of their universal absence. Unrelated secondary search results were not used as scientific inputs.

The directly load-bearing dependency inspected is Eugene Golikov and Greg Yang, *Non-Gaussian Tensor Programs*, NeurIPS 2022: [primary proceedings page](https://proceedings.neurips.cc/paper_files/paper/2022/hash/8707924df5e207fa496f729f49069446-Abstract-Conference.html), [main PDF](https://proceedings.neurips.cc/paper_files/paper/2022/file/8707924df5e207fa496f729f49069446-Paper-Conference.pdf), and [supplement ZIP](https://proceedings.neurips.cc/paper_files/paper/2022/file/8707924df5e207fa496f729f49069446-Supplemental-Conference.zip). The main PDF is 13 pages, 366,499 bytes, hash `05569ae157ef8e5adb43cadcae39426949ba1f855112a227c7145ea9639d3dac`; the extracted appendix is 33 PDF pages (printed pp.14–46), 790,700 bytes, hash `d72e99b926952aa133d28f21216783f46ea652c5877a68bd5d765563a7f4adb8`. I read its relevant main definitions/theorems/proof architecture, and the load-bearing appendix moment argument, full expected-smoothness induction, backprogram construction, interpolation proof, and uniform-integrability argument (Appendices I–M, printed pp.29–43, with the immediately preceding chain/product estimates). I did not read the entire dependency or audit its unrelated applications/experiments. Its OpenReview endpoint was also challenged; the proceedings provided the substantive proof. TP IVb's citations to that dependency use older appendix numbering: its “I.3/J.6” correspond to the accessible proceedings' J.3/K.6 for the expected-smoothness bounds.

TP III's full latest paper, including its core-set and Gaussian-conditioning proof, was read directly earlier in this assigned audit. The relevant reused primary dependency is [TP III v3](https://arxiv.org/pdf/2009.10685v3), especially Appendix L.5 for rank stability and Appendix L for the Gaussian induction. No other review was consulted to recover it.

## Exact primitive-language and evaluator correspondence

TP IVb Definition 2.6.1, pp.19–20, has initial Gaussian vectors/matrices, transpose matrix multiplication, scalar averaging, and the instruction

\[
y_\alpha=\frac1{n^r}\sum_{\beta_1,\ldots,\beta_r}
 \psi(x_\alpha;x_{\beta_1};\ldots;x_{\beta_r};c).
\]

Here `x` is a finite tuple of existing vectors and `c` a finite tuple of existing scalars. With `r=0`, this is MFP's coordinate operation with scalar feedback. A scalar function of existing scalars can be broadcast as a constant vector and averaged (Lemma 2.6.2, p.20). Products and normalized contractions therefore lie in this language. MFP's vector types distinguish neuron populations but do not obstruct embedding the fixed, equal-width typed graph in a single NEXORT program. Its Gaussian roots with arbitrary fixed covariance, including singular covariance, are fixed linear images of independent standard roots, as already explained in TP IVb footnote 14, p.20. Separate rectangular width-ratio limits would require more bookkeeping; TP IVb's displayed master setup uses one common `n` (Remark 2.9.3, p.29).

For a matrix-call result `Wh`, write `Z_h` for the limiting scalar representative of its input and `ζ_{W,h}` for its centered Gaussian source. In MFP notation the rule is

\[
Z_{Wh}=\zeta_{W,h}
 +\sum_{v:\,W^\top v\text{ previously used}}
 Z_v\,\mathbb E[\partial_{\zeta_{W^\top,v}} Z_h],
\qquad
\operatorname{Cov}(\zeta_{W,h},\zeta_{W,k})=\mathbb E[Z_hZ_k].
\]

Definition 2.6.5, pp.21–22, equations (2.18)–(2.19), states exactly this, with `|h⟩=Z_h`, hat-kets for sources, and dot-kets for the response. Different oriented matrix names have independent Gaussian source groups. The displayed scalar expansion on p.21 explicitly identifies it with TP IV's earlier `Zdot` rule. The covariance is an uncentered input second moment; subtracting input means would change the theorem.

Repeated use of either orientation is allowed in the program definition and in uniformized equation (4.13), p.73. Neither the evaluator nor master statement assumes a single transpose call, a fresh matrix after a gradient step, or gradient independence. Remark 2.9.20, p.33, specifically warns that discarding the response term can be wrong in general architectures, even when the forward representation has no transpose.

The source partial is a partial derivative of the explicit expression in Gaussian source coordinates, with the earlier deterministic coefficients fixed. It is not physical differentiation of the network parameters or differentiation of the covariance construction. This is the same distinction maintained by MFP's separate physical-AD and source-AD engines. A finite physical derivative can change scalar feedback; the source evaluator treats already-computed scalar limits as coefficients.

For a singular Gaussian source vector `ζ` with covariance `C`, Stein's identity gives

\[
 b:=\mathbb E[\zeta F(\zeta)]=C a,
 \qquad a:=\mathbb E[\nabla F(\zeta)].
\]

If the corresponding prior input tuple is `Y`, then `C=E[YY^T]`; for every `u∈ker C`, `u^TY=0` almost surely. Hence

\[
Y^TC^+b=Y^TC^+Ca=Y^Ta.
\]

This is the pseudoinverse/source-derivative equivalence of Remark 2.6.6, p.22. It identifies the total response, not each coefficient: `C^+b` need not equal `a`. Duplicate queries are allowed; one must retain their separate formal expression slots when differentiating. The relation above explains why redundant directions do not change the answer and why quotienting the random variables before taking formal partials can be wrong. This singular-support issue is already inside the prior rule, although MFP exposes it more explicitly in an API example (`MFP_CALCULUS.md`, lines239–245).

## Hypotheses and convergence: the important overlap

Setup 2.6.3, p.20, assumes independent Gaussian matrices of entry variance `1/n`, independent standard Gaussian initial roots, initial scalars converging almost surely to zero, and pseudo-Lipschitz OuterNonlin maps. Nonzero deterministic initial scalar limits are absorbed into the maps. Pseudo-Lipschitz means a Lipschitz difference estimate multiplied by a polynomial in the input norms (footnote 7, p.15).

Setup 2.6.4, pp.20–21, permits independent centered non-Gaussian entries with variance `1/n` and uniformly bounded scaled moments of every order. It strengthens the maps to polynomially smooth: `C∞` with every partial derivative polynomially bounded. Initial scalar moments of all orders must be bounded uniformly in `n`. **Gaussian matrices satisfy this setup too.** It is not a theorem restricted to matrices that happen to be non-Gaussian.

Theorem 2.6.10, p.23, states:

- Every program scalar converges almost surely to the scalar computed by the ket evaluator, in either setup.
- In Setup 2.6.4 it also converges in every finite `L^p`.
- If initial scalar errors are `Õ(n^{-1/2})`, output scalar errors have that rate as well.

Here `Õ` is the paper's specific a.s. subpolynomial notion (Definition 1.2.5, p.11): every extra `n^{-ε}` factor drives the rescaled quantity to zero. It is not a stated finite-sample constant, a pure logarithmic correction, or an `L^p` error-rate bound. Remark 2.6.11 and §4.3.4, p.66, explicitly call the rate/Wasserstein interpretation informal because their vanishing definition is almost sure rather than based on expected transport cost. Do not quote that remark as a proved numerical Wasserstein bound.

An MFP empirical polynomial observable is another scalar instruction, so Theorem 2.6.10 applies after adjoining it. For a fixed tuple of same-type vectors, adjoining bounded smooth tests and the quadratic norm gives empirical weak convergence and convergence of second moments almost surely; a countable convergence-determining family suffices. The standard truncation argument then gives empirical `W_2` convergence. This is an immediate consequence of the scalar theorem, not an exact quotation of its vectorwise-dequivalence formulation. Thus MFP's empirical convergence in probability is not a stronger convergence mode.

For smooth MFP programs with deterministic initial scalars and fixed polynomial-growth maps, all these hypotheses are met after lowering. In fact the all-`L^p` chronology is earlier still: Golikov–Yang (2022), Theorem 3.7, p.6, already states a.s. and all-finite-`L^p` scalar convergence for the coordinate/average program language. Its Lemmas J.3/J.6 and Theorem M.3 explicitly supply uniform moments and the upgrade by uniform integrability. MFP itself attributes the raw-entry moment mechanism to this work (`main.tex`, lines304–307 and its uniform-moments section). The literature comparison should preserve that attribution.

Nonsmooth qualifications matter. Pseudo-Lipschitz primitive maps need not be everywhere differentiable; the pseudoinverse characterization in Remark 2.6.6 supplies the response without ordinary partials where required. But a neural training theorem also needs the differentiated network maps to satisfy its assumptions: Assumption 2.3.2, p.15, requires pseudo-Lipschitz `φ′`, and Assumption 2.9.17, p.32, requires pseudo-Lipschitz derivatives of the representing nonlinearities. Ordinary ReLU training is explicitly excluded by this hypothesis (p.15), even though the numerical experiments use ReLU. The all-`L^p` smooth branch does not prove an arbitrary discontinuous-derivative extension. MFP's stated smooth activation class lies safely inside the polynomially smooth branch.

## Derivative closure and update compilation

Definition 2.9.14, pp.31–32, explicitly constructs the backpropagation program of a NEXORT program. For a scalar observable `c=mean(x)`, its vector adjoints are normalized as `n∂c/∂y`; scalar adjoints are ordinary `∂c/∂a`. Matrix calls reverse orientation, averages broadcast scalar adjoints, and OuterNonlin backpropagates through every argument slot and averages over the other slots. Definition 2.9.16 combines these into a total program for all outputs and a finite list of inputs. Footnote 34, p.31, attributes the earlier NETSOR version to Golikov–Yang; its Appendix K, printed pp.38–40, gives that construction and its explicit finite program size bound.

For MFP's primitive sublanguage the exact closure can be checked without an appeal to a neural-network limiting heuristic. For a parameter-dependent finite graph:

\[
D\phi(v)[\dot v]=\sum_j(\partial_j\phi)(v)\dot v_j,
\quad D\operatorname{mean}(v)=\operatorname{mean}(Dv),
\quad D(Wv)=(DW)v+W(Dv).
\]

A represented matrix direction `DW=Σ_a u_a v_a^T/n` acts by `Σ_a u_a mean(v_a⊙h)`. Its transpose acts by `Σ_a v_a mean(u_a⊙h)`. These are primitive coordinate maps and averages followed by permitted original matrix calls. Differentiating such a represented direction again produces another finite sum of the same form. The chain/product rules therefore prove by induction closure at every fixed derivative order. Polynomial smoothness is preserved under taking derivatives, finite products, and composition. After finite differentiation, the enlarged program satisfies the same master theorem. This establishes the relevant finite-order convergence consequence without interchanging an `n→∞` limit and differentiation.

This last inference is stronger and more precise than saying TP IVb explicitly packages MFP's entire derivative API. It explicitly gives reverse programs and uses higher mixed matrix-entry derivatives in Lemmas 4.9.2–4.9.3, p.80; it does not state an API for arbitrary frozen versus moving directional jets. Nevertheless their existence and scalar convergence are consequences of the existing closure plus master theorem in the shared smooth finite-program class.

For a represented parameter vector field `V`, the exact moving second derivative is `D²O[V,V]+DO[DV[V]]`, whereas a frozen-direction second derivative is `D²O[V,V]`. Repeated application of the derivation `D_V` gives all fixed-order moving coefficients. Keeping independent seed coordinates fixed during physical differentiation is compatible with this argument: duplicate Gaussian values may be represented by distinct physical arguments sharing an initial root. No statistical independence follows from freezing a physical coordinate. These are useful MFP conventions, not new probabilistic obstructions outside Tensor Programs.

The parameterization also matches. TP IVb Definition 2.5.1, p.18, and Definition 2.9.12, p.31, give hidden matrices initialized at variance `1/n`, order-one first/readout stored vectors, output average `a^Th/n`, and SGD updates with matrix mobility one and vector mobility `n` in MFP's stored coordinates. Fixed input factors such as `x/√d` are constant coefficients. For SGD the hidden matrix update is exactly a finite sum of normalized outer products, so MFP's fixed update lowering is already representable in NETSOR⊤+.

NEXORT is strictly more expressive at the update level. For a general entrywise function `Q`, applying `Q` to a gradient outer product does not generally retain finite rank. Definition 2.6.1's nonlinear outer product handles its action; Theorems 2.7.1/2.7.3, pp.23–24, and 2.9.25/2.9.30, pp.35–36, cover memoryless or memoryful and stationary or nonstationary updates. MFP's documented normalized-rank-one update grammar should not be presented as covering every one of these adaptive matrix updates. Adam is represented with a positive stabilizer inside the square root (equation Adam and its smoothness discussion, p.12); variants with nonsmooth division require separate checking.

All these results concern each fixed finite number of steps. They do not establish uniformity for a width-dependent horizon, a continuous-time population solver from finitely many initial jets, or convergence of a Taylor series. TP IVb's broader optimizer coverage does not establish those different limits either.

## Input geometry and architecture

Setup 2.3.1, pp.14–15, takes an arbitrary fixed finite matrix of inputs, with an arbitrary prescribed output-error function. Its construction allows train/test masking and minibatch schedules. First-layer Gaussian covariance is the actual input Gram matrix; there is no orthogonality, equicorrelation, one-sample, or generic-full-rank hypothesis. Singular or repeated inputs are part of the master-program setup. Definitions 2.9.1 and 2.9.16, pp.29 and 32, extend this to representable architectures with fixed input/output dimensions and shared parameters over the input list. Thus “arbitrary fixed geometry” is prior mathematical scope. MFP's ability to retain symbolic real geometry coefficients and print the resulting formulas is a concrete implementation feature within that scope.

The general-architecture update results are stated with proofs omitted as adaptations of the MLP construction (§2.9, p.29). I have not certified every displayed general-architecture update formula as printed. In particular, a compiler must aggregate derivatives from both `W` and `W^T` occurrences with the appropriate orientation; the unambiguous formula for this is already in Golikov–Yang Proposition K.2, printed p.39. TP IVb's shorthand sums over `h=Wx` in (2.45) should not be copied without that orientation accounting for a representation containing transposes. Similarly, Remark 2.9.15's `r=0` vector-adjoint display appears to omit the `d_x` on the multiplying adjoint `y`; Definition 2.9.14 gives the intended chain rule. These are reasons to verify a compiler's exact finite rules, not evidence that transpose reuse lies outside the underlying master theorem.

## Load-bearing proof reconstruction and checks

The relevant Gaussian proof is not merely TP III Appendix N repeated. It has the following structure.

1. **Define a stable comparison notion.** A vanishing vector has normalized squared norm `Õ(n^{-1})` (Definition 4.3.5, p.61). Moment-bounded tensors have empirical moments of every order of subpolynomial size. Equivalence means their difference vanishes; dequivalence means this after a coupling up to distributional equality (Definitions 4.3.9, 4.3.15–17, pp.62,65–66). These are sequence-level statements.

2. **Prove closure of errors.** Proposition 4.3.11, pp.63–64, uses the pseudo-Lipschitz difference estimate and Hölder with exponent just above two. The dimension factor is `n^{s(1-2/q)}` for an order-`s` tensor, absorbed into an arbitrarily small extra power because `q` can approach two. Lemma 4.3.13 preserves the normalized squared error under averaging by Jensen. Proposition 4.3.14, p.65, preserves it under an arbitrarily correlated matrix call by `||W(x-y)||₂≤||W||op||x-y||₂`. No independence of query and matrix is assumed in this step.

3. **Strengthen the scalar-free Gaussian theorem.** Theorem 4.7.2, pp.74–77, revisits TP III's Gaussian induction. TP III's core-set rank-stability result is used to retain a basis of query directions; it is not assumed for the original scalar-feedback program. Conditional Gaussian regression gives

\[
Wh=\omega+\sigma P_{Y^\perp}g,
\quad
\omega=(GX^++Y^{+T}H^T-Y^{+T}H^TXX^+)h,
\quad \sigma^2=\|P_{X^\perp}h\|^2/n,
\]

where previous calls are `WX=G`, `W^TY=H`, and `g` is fresh standard Gaussian (equations 4.19–4.22, pp.75–76). On the retained basis, limiting Gram matrices are nonsingular. Lemmas 4.5.1–3, pp.72–73, control their inverses locally; the Schur complement has positive limit, so its square root is locally Lipschitz. The finite-rank projected part of `g` is vanishing (p.77). The limit mean/variance is the already-established hat/dot construction, preserving repeated and opposite-orientation queries.

4. **Compare to an integrated program.** Definition 4.8.1 and Lemma 4.8.2, pp.77–79, replace all scalar feedback by its deterministic limit and all nonlinear outer averages by independent-copy expectations. The resulting program is scalar-free NETSOR⊤ and has the same limiting kets. The original and integrated vectors are equivalent by induction. For `r=0`, the needed nonlinear comparison is just the pseudo-Lipschitz error estimate; there is no combinatorial outer-average issue. For `r>0`, Lemmas 4.4.5–6, pp.69–71, replace reused sample indices by independent copies. Repeated-index tuples number `O(n^{r-1})` and contribute `O(n^{-2p})` to normalized `2p` moments. Distinct tuples are partitioned into disjoint-index perfect matchings by ordered Baranyai; within each matching, conditional centering/independence yields `O(n^{-p})`. This reconstructs the rate bookkeeping in the proof.

5. **Average.** Lemma 4.4.2, pp.67–68, is the all-moment iid law of large numbers plus Borel–Cantelli, giving scalar convergence and the stated a.s. subpolynomial rate. Applying the comparison closure and averaging to the integrated program identifies the original scalar limit.

The Gaussian operator-norm hypothesis used in step 2 is satisfied for independent `N(0,1/n)` entries: a fixed `1/4`-net of the two unit spheres has at most `9^{2n}` pairs; each bilinear form has tail at most `2exp(-nt²/2)`. The usual net approximation converts this to a summable exponential tail for any sufficiently large fixed norm bound. This verifies the required almost-sure boundedness directly and does not need an unexamined optimal-edge theorem. The paper's finite-fourth-moment wording in Proposition 4.3.20, p.67, is broader than the caution in footnote 7, p.65, about dependence across widths. That issue is irrelevant to this Gaussian verification.

Baranyai's theorem itself (Theorems 4.1.5–6, p.56) was not independently proved or checked against its original source. Its stated hypotheses are met by taking the largest multiple of fixed `r` below `n` in the argument; ordered symmetrization preserves matchings. It is an external dependency of the full nonlinear-outer proof, but not of the `r=0` MFP comparison.

**The explicitly incomplete extension.** Section 4.9.1, p.79, asserts uniform local Lipschitzness in initial scalar data, says it follows from sub-Weibull tails and chaining, and states that full details will appear in a future paper. I have not independently supplied that general argument. This limitation does not affect programs with deterministic initial scalar data or `Õ(n^{-1/2})` initial scalar errors, where §§4.7–4.8 apply. Footnote 24, p.79, explicitly says the NT/µ limits use the latter regime.

**The moment proof behind all-`L^p`.** Golikov–Yang Lemma J.3 is an induction uniform over matrix-entry indices, fixed mixed derivative order, and matrices whose variances are shrunk below `1/n`. Coordinate maps use chain/product rules and Hölder; scalar averages use Jensen. For a matrix call, expand an even moment of `Σ_j w_j z_j`. If an index pattern has `b` distinct indices, `s` appearing singly, and total degree `p`, centering kills the Taylor terms that do not supply all singleton weights. The remainder supplies at least `s` extra weights; its moment scale is `n^{-(p+s)/2}≤n^{-b}` because `p+s≥2b`. The derivative factor is uniformly bounded by the earlier-node induction evaluated at shrunk entries. There are `O(n^b)` patterns of that type, so summing leaves a uniform bound. The case `s=0` is handled directly by Hölder without a negative-order Taylor expansion. This checks the central cancellation and its treatment of adaptive matrix dependence. MFP uses an iterated-singleton-difference formulation of this same mechanism.

Lemma J.6 then bounds every scalar moment. With `c_n→c` almost surely, choose `q>p`; bounded `q`th moments give uniform integrability of `|c_n-c|^p` and therefore `L^p` convergence (Theorem M.3, printed p.43). This suffices for the MFP overlap when combined with the Gaussian proof above. It does not need the non-Gaussian interpolation theorem.

For completeness, I also checked the dependency's interpolation architecture (main §5 and Appendix L): `A(t)=A_G cos(πt/2)+A_N sin(πt/2)` gives `E A′=E AA′=0`; scalar matrix derivatives have `O(n^{-1})` moments through the finite backprogram; a Taylor expansion kills the first two degrees for each singleton interpolation index; summing over `O(n²)` raw entries gives `E|c′(t)|^p=O(n^{-p/2})`. TP IVb Lemmas 4.9.2–3, p.80, extend the expected-smoothness/backprogram statements to OuterNonlin by a compressed argument. I checked their stated hypotheses and the normalized-average preservation, but did not independently formalize every multi-index step of that extension. The report therefore does not certify the entire non-Gaussian NEXORT theorem beyond the inspected proof route. Its prior-art statement and the directly verified MFP Gaussian consequence are distinct claims.

## Symbolic computation, efficiency, and reported experiments

Definition 2.6.5 is already an inductive symbolic evaluator; Definition 2.9.24, p.34, explicitly describes the symbolic procedure and its substitution of infinite-width kets/operators. Sections 3.1.1–3.1.3, pp.43–49, spell out the actual training-program construction, including scalar feedback, difference quotients, and repeated transposes. A comparison should not suggest that prior Tensor Programs supplied only existence without computable formulas.

No width enters the resulting fixed-program expectation graph, but graph size and numerical integration cost can increase with program length, derivative order, update count, and source count. TP IVb §5.1, p.81, says that general optimizer expectations lack analytic solutions and uses Monte Carlo. This does not establish a complexity lower bound or exclude special exact reductions. Conversely, merely returning a finite Gaussian expectation graph does not establish efficient numerical evaluation at large order. MFP's useful claims here are its concrete symbolic output, simplifications, source bookkeeping, and documented supported grammar; a general efficiency improvement would require a matched algorithmic comparison.

The complete IVb text contains no inspected standalone software compiler listing/link. A bounded primary search did not locate one; I did not audit any unlinked software. The numerical study is reported evidence only: §5.1, p.81, uses Adam, learning rate 0.2, epsilon10^-4, 100 Gaussian inputs in R^10, squared loss, ten trials, ReLU MLPs of depth 4 for NTP and depth 2 for µP, and widths 64,512,7000 (Figures 5.1–5.2, pp.82–83). Outputs are centered by subtracting each initialization's output. Monte Carlo limit curves are compared with finite-network trajectories. I have not reproduced these experiments. Their ReLU choice lies outside the differentiated-map smoothness hypotheses, so they empirically illustrate a proposed extension rather than independently verify those hypotheses.

## Positioning implications

The following would overstate the inspected distinction: MFP first supplies a finite Gaussian source-response calculus; Tensor Programs excludes scalar feedback or repeated transposes; singular inputs require an added rank-stability assumption; all-finite-`L^p` convergence is new; physical derivative programs are unavailable in the prior framework; arbitrary fixed data geometry or fixed-step µP training is new; or prior work has no symbolic evaluation algorithm.

A supportable narrower description is: MFP develops a particular typed implementation and self-contained specialization of the Tensor Programs finite-program calculus for fixed finite neural derivatives, with explicit frozen/moving/seed semantics, represented-update lowering, inspectable Gaussian expectation graphs, and specialized initialization-moment reduction. Any claimed new mathematical result beyond that should be isolated and compared separately with TP IVb's master theorem and derivative-program constructions and Golikov–Yang's moment/backprogram results. The documented finite-order moving-flow coefficient calculations can be new worked calculations while their general existence follows from this prior machinery.

The complete latest TP IVb source was read. Proof checking was deepest on the source rule, singular queries, Gaussian integrated-program argument, fixed derivative closure, and the all-moment upgrade, because those determine the MFP comparison. The distant parameterization-classification branch was read but not independently certified; its status does not control these conclusions.
