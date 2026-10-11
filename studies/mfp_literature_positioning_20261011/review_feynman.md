# Scoped audit: Feynman diagrams and polynomial wide networks

Frozen audit, 2026-10-11. Scientific inputs were the complete primary preprints below, their primary bibliographic/version records, and the assigned maintained material: `docs/02-gaussian-reuse.qmd` lines 252–1293, `paper_MFP/main.tex`, and `code/MFP_CALCULUS.md`. No other study or reviewer findings were read. Required canonical-notation and rigorous-mathematics skills were applied. Here **Dyer** means Dyer and Gur-Ari, arXiv:1909.11304v1; **Aitken** means Aitken and Gur-Ari, arXiv:2006.06687v1. Page numbers below are printed PDF pages, which coincide with PDF page indices plus one.

The complete 37-page Dyer arXiv version and complete 20-page Aitken version were read, including every appendix. The requested ICLR conference-version comparison remains incomplete: its primary OpenReview PDF endpoint returned HTTP 403/browser challenge. The parent independently confirmed the access problem and instructed this audit to stop attempts. Consequently, defects below are claims about the identified arXiv versions, **not verified claims about the final ICLR paper**.

## Finding relevant to MFP positioning

These papers already organize arbitrary fixed orders of fully contracted parameter derivatives, prove polynomial-network width bounds, and derive an exact hierarchy for successive physical derivatives of outputs and kernels. They also retain enough information in Wick expansions to compute explicit coefficients. An assertion that earlier diagram methods cannot compute constants, cannot handle higher derivatives, or offer no expectation/moment control would be incorrect. Aitken's theorem is essential prior art; treating all deep nonlinear diagram results as merely conjectural ignores the proved polynomial case.

They do **not** state the MFP master theorem for a finite program with smooth polynomial-growth coordinate functions, causal scalar averages and feedback, named matrix/transpose reuse, and represented updates. The best defensible distinction is MFP's constructive language and Gaussian source-response evaluation for those admitted programs, together with its exact finite-width derivative lowering. This is a distinction in coverage and computation, not a new general principle that Gaussian derivatives or moments can be expanded. Conversely, Dyer's arbitrary fully paired parameter-tensor contractions are not all admitted MFP operations. Neither framework contains the other by an immediate syntactic inclusion.

The full master theorem's empirical joint-law and uniform node-moment statements are not supplied by these two papers. For their own polynomial observables, however, uniform moments and convergence in every finite \(L^p\) already follow readily in the concentrating cases; see the explicit derivation below. MFP should not present the mere upgrade from probability convergence to all finite \(L^p\) in this polynomial setting as a new probabilistic mechanism.

## Sources, versions, and coverage

| Source | Version and coverage | Local complete source | SHA-256 of PDF |
|---|---|---|---|
| [Dyer and Gur-Ari, *Asymptotics of Wide Networks from Feynman Diagrams*](https://arxiv.org/abs/1909.11304) | arXiv v1, submitted 25 September 2019, 37 pages. Main §§1–5 pp.1–10, A p.11, B pp.12–15, C pp.15–19, D pp.20–22, E pp.22–35, references pp.35–37: all read. | `data/generated/mfp_literature_positioning_20261011/root/feynman.pdf`, matching `feynman.txt` | `e27bb07affb17c56c2346e334854cb21aaee7912be26975cabee9606b0463e3a` |
| [Dyer ICLR 2020 record](https://openreview.net/forum?id=S1gFvANKDS) | Conference bibliographic metadata checked; complete conference PDF not obtained/read. | `feynman/dyer-refs.json` stores primary API bibliographic reference, not reviews. | Not available |
| [Aitken and Gur-Ari, *On the asymptotics of wide networks with polynomial activations*](https://arxiv.org/abs/2006.06687) | arXiv v1, submitted 11 June 2020, 20 pages. Main §§1–4 pp.1–8, references p.9, A pp.10–11, B pp.12–15, C pp.15–18, D pp.18–20: all read. | `data/generated/mfp_literature_positioning_20261011/feynman/aitken.pdf`, matching `aitken.txt` | `67896869501b2bdef9ce525f993de0d837bd1825a9f44bcd8bb4cbbab1f0aa3b` |

The full PDF URLs are [Dyer v1](https://arxiv.org/pdf/1909.11304v1) and [Aitken v1](https://arxiv.org/pdf/2006.06687v1). Primary arXiv histories list only v1 for each. Their downloaded metadata are `feynman/dyer-abs.html` and `feynman/aitken-abs.html`. Dyer's author publication page links arXiv; its archived HTML is `feynman/google-publication.html`. OpenReview bibliographic metadata names ICLR 2020 and an original attachment, but is insufficient to establish its equality with arXiv or identify corrections. No claim is made that no corrections exist. Dyer notes an earlier ICML 2019 workshop version on p.3; that workshop paper was not independently read because the complete later arXiv work was the scientific audit target.

Text hashes: Dyer `f6e10a42d00b369e4b663b0fedbaf0b15229003db99977fcad6a882e9cb88af5`; Aitken `6871490a5450f53248e8f176590e5ab6f32379d3ad8d1b924b187e8a7b4ff843`. Page-index files and visual checks of Aitken pp.5,17 and Dyer p.34 are stored in the owned `feynman/` generated directory. All cited pages were read in full, not inferred from abstracts or search snippets.

## Exact setup and theorem quantifiers

Both works fix architecture depth, input dimension, number of queried inputs, derivative orders, and contraction pattern before width \(n\to\infty\). Inputs \(x_1,\ldots,x_m\) are arbitrary fixed deterministic vectors. Hidden widths are equal in the displayed setup; proportional widths with fixed ratios are noted as an extension. Weights in distinct layers are independent, with independent standard Gaussian **raw** entries. Their scalar output uses the NTK normalization \(n^{-1/2}\), not an empirical mean readout.

For example, Dyer Eq.(2), pp.3–4, uses
\[
 f_\theta(x)=n^{-1/2}V^T\sigma\bigl(n^{-1/2}W^{d-1}\cdots
 \sigma(n^{-1/2}W^1\sigma(Ux))\bigr),
\]
with raw \(U,V,W^\ell\) standard Gaussian. Aitken Eqs.(4), p.3, additionally normalizes the fixed input layer by \(D_{\rm in}^{-1/2}\). Dyer's experiments use that input normalization too, Eq.(16), p.11. Biases, weight tying between layers, transpose reuse, and generic scalar-feedback programs are not part of these displayed theorem setups. Absence from this setup is not evidence that a diagram method cannot be extended to them.

Dyer Definition 1, Eq.(3), p.4, concerns
\[
 C_n=\mathbb E F_n,\qquad
 F_n=\sum_{\text{paired parameter indices}}
       \prod_{a=1}^m\partial_\theta^{k_a}f_\theta(x_a),
\]
where each derivative index is paired and summed over **all raw parameters**. The original definition takes \(m\) and the total number of derivative indices even. This is an arbitrary but fixed contraction, not a growing-order asymptotic. Define the cluster graph to have one vertex for each derivative tensor and an edge for each contracted pair connecting tensors. Let \(n_e\) and \(n_o\) count its components with even and odd numbers of vertices. Conjecture 1, Eq.(4), p.4, states
\[
 C_n=O(n^s),\qquad s=n_e+\frac{n_o-m}{2}.
\]
The constant may depend on architecture, activation, inputs, and the fixed contraction. The bound need not be sharp.

| Result | Exact scope and status |
|---|---|
| Dyer Theorem 1, p.4; B pp.12–15 | Proved for deep **linear** networks. |
| Dyer Theorem 2, p.5; C pp.15–19 | Proved claims for deep ReLU when **all queried inputs coincide**, and for one-hidden-layer networks with smooth activation. The smooth statement needs integrability, discussed below. ReLU derivatives are the almost-everywhere finite-network derivatives; this does not validate Taylor expansions across activation changes. |
| Dyer general deep smooth nonlinear case | Conjecture 1, supported by experiments; no general proof in this version. |
| Aitken Theorem 1, Eq.(3), p.2, proof pp.5–8 and B pp.12–15 | Proves the same bound for fixed-depth networks with fixed **polynomial** activations (potentially different polynomials at different layers). Coefficients and degrees do not grow with width. All queried inputs can differ. |
| Aitken Theorem 2, Eqs.(35)–(36), pp.15–17 | Covariance of two such contracted observables: exponent at most \(s_x+s_y-1\) if both graphs have no odd components, otherwise \(s_x+s_y\); odd total parity gives zero. This is a polynomial-network result in the paper's setup. |
| Aitken Corollary 1, Eq.(46), p.17 | \(\operatorname{Var}F_n=O(n^{2s-1})\) if \(n_o=0\), and \(O(n^{2s})\) otherwise. Its following worked example is mislabeled, but this corollary is consistent with the proof and table. |

Aitken's observation that a finite Taylor truncation is polynomial (pp.2–3,8) does not establish the theorem for tanh, sigmoid, all real-analytic activations, or all smooth activations. Degree-dependent constants and unbounded Gaussian inputs require quantitative approximation and limit-exchange control. Even tanh's Taylor series about zero has finite radius of convergence. The paper appropriately states its theorem for finite truncations and reports numerical evidence beyond them.

## Proof mechanics and what was independently checked

The crucial polynomial mechanism is exact Gaussian integration, not a formal large-width Gaussian approximation. Expand each finite polynomial network into weight monomials, apply Wick/Isserlis pairings independently within each weight block, and count neuron-index sums left free by the resulting Kronecker deltas. Every term has an explicit width power and a width-independent coefficient. Dyer B derives the linear-network diagram count; Aitken §2.2 and B allow multiple weight factors from polynomial activations.

A paired raw derivative removes two selected weight factors and replaces them by exactly their covariance delta. For matrices this is
\[
 \sum_{i,j}\frac{\partial W_{ab}}{\partial W_{ij}}
             \frac{\partial W_{cd}}{\partial W_{ij}}
   =\delta_{ac}\delta_{bd}=\mathbb E[W_{ab}W_{cd}].
\]
For first-layer projected inputs the corresponding contraction includes their fixed input inner product. Polynomial differentiation introduces multiplicities depending on fixed degree, not width. Aitken Lemma 2, Eqs.(29)–(33), pp.12–14, formalizes this: contractions with derivatives are a weighted subset of Wick contractions for the undifferentiated product. Repeated derivatives are included; they need not vanish as in a deep linear network.

Each network monomial has one output weight \(V\). Its Wick pairing forces every connected contraction component to contain an even number of function factors. Derivative pairings force the cluster graph to be a subgraph of the contraction graph. Consequently the latter has at most \(n_e+n_o/2\) components (Aitken Lemma 1 and B.2, pp.6,14–15). Adding a matrix-weight pair introduces at most one net free neuron sum with a compensating \(n^{-1}\); joining formerly distinct components removes an additional free sum. An input-weight pair has no width normalization and can remove a free sum when it joins components. This yields contribution \(O(n^{N-m/2})\) for \(N\) contraction components. There is a printed first-layer normalization error in Eqs.(11)–(14), documented below; the stated network and this index count give the standard corrected proof.

For covariances, subtracting the product of expectations cancels Wick pairings disconnected between the two observables (Aitken C, pp.15–17). At least one joining pairing remains. When both cluster graphs have only even components, joining loses a component and hence a power of \(n\). The argument is an upper bound term by term; claims that two differently weighted sums have exactly the same asymptotic order would additionally need to exclude coefficient cancellation. That stronger assertion is unnecessary for Theorem 2.

Verified dependencies are the finite Gaussian pairing identity, raw differentiation identity, parity/component counting, and elementary moment/probability arguments, all checked in the supplied papers or directly above. Dyer C.1's ReLU proof also invokes a gate/sign independence construction attributed to Hanin and Nica. That external paper and its complete proof were **not** independently read here, so the ReLU dependency is not fully certified. C.1 proves its displayed no-derivative comparison and does not explicitly return to its temporarily omitted contracted derivatives; a derivative-level gate argument is needed to make that presentation complete. This is an identified proof-presentation dependency, not a ReLU counterexample. No external physics argument is being used to establish a new MFP theorem.

### Moment and expectation consequences already available

For a polynomial observable \(F_n\) with cluster exponent \(s\), apply Aitken Theorem 1 to the product of \(2r\) copies of the same contracted observable. Its graph is the disjoint union of those copies, so
\[
 \mathbb E|F_n|^{2r}=\mathbb E F_n^{2r}=O(n^{2rs})
 \quad\text{for every fixed integer }r\ge1.
\]
Thus \(n^{-s}F_n\) has bounded moments of every fixed finite order. Products of finitely many such observables are covered by concatenating their tensors and contractions. This elementary corollary is stronger than merely reading Dyer D.1's variance estimate as an \(O_{\mathbb P}\) assertion.

If \(n_o=0\), Aitken's covariance improvement gives
\[
 \operatorname{Var}(n^{-s}F_n)=O(n^{-1}).
\]
The normalized mean is a finite sum of explicit powers of \(n\), by the Wick expansion, and the bound excludes surviving positive powers; it therefore has a finite limit \(c\). The variance gives convergence in probability to \(c\). The uniform \(2r\)-moment bounds give uniform integrability of \(|n^{-s}F_n-c|^p\) by choosing \(2r>p\). Hence
\[
 n^{-s}F_n\longrightarrow c\quad\text{in every finite }L^p.
\]
This is a deduction from the papers' results, not a theorem explicitly advertised in this form. It requires no Gaussian hypercontractivity citation. If odd components are present, the variance bound need not shrink after normalization; a random output such as \(f_\theta(x)\) or its square generally retains fluctuations. It would be wrong to convert all contracted correlation functions into deterministic scalar limits simply because their expectations obey a width bound.

Dyer Theorem 9, Eqs.(57)–(62), pp.22–23, already proves NTK convergence in probability in the deep linear case through connected-diagram variance decay and a finite power expansion of the mean. Aitken supplies its polynomial extension and the above all-moment corollary. These conclusions concern specified scalar contractions; neither paper proves the MFP assertion about joint empirical distributions of every intermediate vector node.

## Physical derivatives, training, and the finite-time boundary

Dyer Eq.(10), p.7, and Eqs.(78)–(79), pp.28–29, define an exact hierarchy
\[
 O_1(x)=f(x),\qquad
 O_s(x_1,\ldots,x_s)=
 \sum_\mu\partial_{\theta_\mu}O_{s-1}(x_1,\ldots,x_{s-1})
             \partial_{\theta_\mu}f(x_s).
\]
For squared loss \(L=\tfrac12\sum_a(f(x_a)-y_a)^2\), ordinary raw-parameter gradient flow gives exactly
\[
 \frac{d}{dt}O_s=-\sum_a O_{s+1}(x_1,\ldots,x_s,x_a)(f(x_a)-y_a).
\]
Repeated differentiation includes movement of all trainable parameters and residuals. The physical Lie-derivative idea and high-order kernel hierarchy therefore substantially predate MFP. Dyer Lemma 1, p.6, proved in D.2, Eq.(52), pp.20–21, controls each **fixed** initialization time derivative assuming the cluster conjecture and a polynomial loss. Its proof adds vertices and edges to graphs and checks that the exponent cannot increase. MFP's finite flow jets share this local scope, though MFP computes explicit Gaussian expectation limits through its admitted language.

The following claims need separation:

| Claim | What these sources establish |
|---|---|
| Fixed physical derivatives at initialization | Exact hierarchy; width exponents under the proved or conjectured network class. Polynomial loss is used in D.2. |
| Fixed number of discrete gradient steps | Dyer Theorem 8, pp.21–22, has an exact finite Taylor proof for deep linear networks. Theorem 10, pp.23–24, bounds NTK movement in mean and variance; Theorem 11, pp.24–25, controls the leading update. The proof extends to fixed polynomial activations using Aitken's theorem and termination at the fixed polynomial degree. This is a justified corollary, not an additional stated theorem in Aitken. Labels, data, steps, and learning rate are fixed. |
| General smooth network discrete steps | Dyer explicitly leaves control of the infinite Taylor sum open (D.3 p.22), and conditions related claims on interchanging its sum with the width limit (E.1 p.23; E.2 p.24). Smoothness itself does not give a Taylor representation. |
| Positive continuous time | Dyer §3 p.6 explicitly adds analyticity in time and a Taylor/width-exchange assumption. Fixed jets alone do not establish this. Aitken's proof of polynomial initialization bounds does not automatically prove this exchange or a common flow existence interval. |
| An infinite \(1/n\) expansion or arbitrary-order finite-time closure | E.4 pp.28–35 describes a formal construction and leading finite-width corrections. Uniform remainder control at every order and common-time convergence are not supplied by the initialization bound alone. |

For the logical distinction, the entire functions \(h_n(t)=t^n\) have every fixed derivative at zero eventually equal to zero, while \(h_n(1)=1\). This is a counterexample to deriving fixed-time control from bounds on each fixed initialization derivative, **not** a counterexample to a network theorem. Likewise, a smooth function need not equal its Taylor series: the standard function zero on \(t\le0\) and \(e^{-1/t^2}\) on \(t>0\) is smooth and nonanalytic. The parenthetical assertion on Dyer p.23 that smooth nonlinear networks are analytic in weights is too broad.

Dyer's leading finite-width formulas, Eqs.(12)–(13), p.7 and Eqs.(92)–(98), pp.30–31, require initial finite-network quantities such as \(f_0,\Theta_0,O_{3;0},O_{4;0}\). The exact hierarchy applies to an arbitrary fixed training set, not only equal inputs. The same-input restriction belongs specifically to the ReLU proof of Conjecture 1. Their correction formulas are not a general evaluated catalogue of these initial tensors in Gaussian activation moments. Conversely, the initial tensors can be computed by Wick expansions in the linear/polynomial cases, so this is not an intrinsic impossibility of their approach.

The formulas with \(\Theta_0^{-1}\) and inverse eigenvalues on pp.30–31 require a support/pseudoinverse or continuous-extension interpretation at singular kernels. For finite times the combinations \((1-e^{-t\lambda})/\lambda\) have removable singularities. Late-time inverses need stronger conditions on the relevant residual directions. The displayed inverse notation alone is not a theorem excluding singular problems; it is an omitted qualification. MFP treats singular Gaussian query Grams within its finite compiler, a different inverse issue.

Parameterization must be translated before comparing values: Dyer differentiates raw entries with explicit \(n^{-1/2}\) forward factors, uses an output of order one with random initialization fluctuations, and uses Euclidean raw-parameter updates. MFP stores matrices with variance \(1/n\), pairs vectors by \(1/n\), and uses prescribed vector mobility \(n\) and matrix mobility one for empirical-mean scalar losses. For a raw matrix \(\widetilde W=\sqrt n\,W\), \(\partial_{\widetilde W}=n^{-1/2}\partial_W\). Output, loss normalization, and block mobility add further factors. Theorems or coefficients cannot be compared by simply renaming \(W\).

## Exact checks of consequential-looking defects

These checks locate limits of the printed arguments and formulas. They are not presented as the source of MFP novelty. In particular, a repairable recurrence or normalization error does not disprove the polynomial cluster bound.

### 1. Smoothness alone does not ensure the one-layer theorem's expectations exist

Dyer Theorem 2, p.5, and Theorem 7/proof in C.2, pp.17–19, use finite activation/derivative moments when defining a finite maximum \(s_{\max}\) before Eq.(50). No growth or integrability condition accompanies the main smooth-activation claim. For the admitted one-hidden-layer expression with input \(x=1\), choose the smooth activation \(\sigma(z)=e^{z^2}\). Then
\[
 f=\frac1{\sqrt n}\sum_iV_i e^{U_i^2},\qquad
 \mathbb E f^2=\mathbb E e^{2G^2}=\infty,
 \quad G\sim N(0,1).
\]
The cluster graph of \(\mathbb E f^2\) predicts \(O(1)\), which is false as a literal assertion covering every smooth activation. This is a missing-assumption counterexample, not a counterexample under polynomial-growth assumptions. Requiring all relevant activation derivative products to be integrable repairs the one-layer argument; MFP's polynomial-growth assumptions satisfy that requirement. Aitken's polynomial theorem is unaffected.

### 2. Aitken's printed monomial normalization includes an extraneous first-layer width factor

In Aitken Eq.(11), p.5, the denominator is \(n^{(1+p_L+\cdots+p_1)/2}\), while \(p_1\) counts \(U\) factors and \(U_i(x)=D_{\rm in}^{-1/2}\sum_\alpha U_{i\alpha}x^\alpha\) has no \(n^{-1/2}\). For \(L=1\), \(D_{\rm in}=1\), and \(\phi(z)=z^2\), the actual network is \(n^{-1/2}\sum_iV_iU_i^2x^2\), whereas Eq.(11) gives \(n^{-3/2}\sum_iV_iU_i^2x^2\). Equation (10)'s width-independent coefficient cannot absorb the missing factor \(n\).

The normalization must exclude \(p_1\): \(n^{(1+p_L+\cdots+p_2)/2}\), with the same correction propagated to Eqs.(12),(14). The U-pair paragraph of the proof, p.7, otherwise counts the correct absence of new width normalization; its final parenthetical attribution of a gained \(n^{-1}\) to normalization should instead attribute it to merging free index sums. Visual inspection confirmed this is in the PDF. This correction restores consistency with the network, worked examples, and the index-count proof; it does not refute Theorem 1.

### 3. Aitken's \(C_{4,2}\) coefficient and variance case study

For \(\phi(z)=z^2\), one hidden layer, scalar input 1, define
\[
 f=\frac1{\sqrt n}\sum_iV_iU_i^2,\qquad
 F_{4,2}=f\,D^2f[\nabla f,\nabla f].
\]
This is exactly the contracted observable in Aitken Eq.(1c). Direct differentiation gives
\[
 F_{4,2}=\frac8{n^2}
       \left(\sum_iV_iU_i^2\right)
       \left(\sum_j(V_j^3U_j^2+V_jU_j^4)\right).
\]
Independence and Gaussian moments therefore give
\[
 \mathbb EF_{4,2}=\frac{192}{n},\qquad
 \operatorname{Var}F_{4,2}
   =\frac{82944}{n^2}+\frac{4396032}{n^3}.
\]
To check the variance transparently, set \(a=VU^2\), \(b=V^3U^2+VU^4\). Then
\(\mathbb Ea^2=3\), \(\mathbb Eb^2=240\), \(\mathbb Eab=24\), and \(\mathbb Ea^2b^2=70560\). Expanding independent sums gives the displayed formula.

Thus the coefficient 132 asserted just below Eq.(8), p.4, is incorrect for the stated example; the power \(n^{-1}\) is correct. More substantively, the case study after Corollary 1, p.17, assigns \((n_e,n_o)=(1,0)\) and variance \(O(n^{-3})\) to \(C_{4,2}\). Its actual graph has one size-three component and one isolated vertex, so \((n_e,n_o)=(0,2)\). The exact variance above contradicts that case-study assertion. Table 2, p.18, correctly lists \((0,2)\) and exponent \(-2\); the case-study graph and \(-3\) exponent belong instead to \(C_{4,3}\). Corollary 1 itself gives the correct \(-2\) bound for \(C_{4,2}\).

An independent exact rational polynomial script recomputed the derivatives and Gaussian moments for \(n=1,2,3\). The script and output are `feynman/algebra_checks.py` and `feynman/algebra_checks.json`. This is an actually reproduced finite algebra check, not a reproduction of the papers' numerical experiments.

### 4. Dyer's discrete correction has an off-by-one factor

Dyer Eq.(106), p.34, implies at the claimed leading order
\[
 O_{3;t+1}^{(1)}-O_{3;t}^{(1)}
   =-\eta O_{4;0}R^t r_0,
 \quad R=I-\eta\Theta_0,
 \quad r_0=f_0-y.
\]
Its solution is the finite sum
\[
 O_{3;t}^{(1)}=O_{3;0}-\eta O_{4;0}\sum_{k=0}^{t-1}R^k r_0.
\]
When \(\Theta_0\) is invertible, this equals
\(O_{3;0}-O_{4;0}\Theta_0^{-1}(I-R^t)r_0\).
Printed Eq.(109) inserts an extra factor \(R\). Eq.(108) also starts its sum at 1 and does not consistently use the summation index; Eq.(107) omits \(\eta\). Visual inspection confirmed these are printed errors.

A concrete network shows that the extra factor affects the retained order. For one hidden **linear** layer, one input 1, and \(f=n^{-1/2}\sum_iV_iU_i\),
\[
 \Theta=(\|U\|^2+\|V\|^2)/n,\qquad O_3=4f/n,\qquad O_4=4\Theta/n.
\]
One exact simultaneous gradient step on \(\tfrac12(f-y)^2\) gives
\[
 f_1=f-\eta\Theta r+\frac{\eta^2}{n}fr^2,
 \qquad
 O_{3;1}-O_{3;0}=-\frac{4\eta}{n}\Theta r
                              +\frac{4\eta^2}{n^2}fr^2,
 \quad r=f-y.
\]
Equation (109) instead includes an extra \(4\eta^2\Theta^2r/n\), generally of retained order \(1/n\) under Gaussian initialization. This is a counterexample to that printed correction formula, not to Theorems 8–11 or the cluster bound. A finite geometric sum repairs the formula without singular inverses. The analogous extra factor is present in Eq.(113), p.34. The ICLR version may differ; it was inaccessible.

### 5. Spectral claims need more than the displayed trace bounds

Dyer E.3, Eqs.(70)–(76), pp.25–26, decomposes the loss Hessian into its Gauss–Newton part \(A\) and residual part \(B\), relates trace moments of \(A\) to the NTK, and then infers eigenvalue scales for \(B\). A second-moment bound controls an RMS eigenvalue, not every eigenvalue or the exact top-eigenvalue difference. Even adding the displayed \(O(1/n)\) errors for all fixed higher moments does not force the stated scale for each eigenvalue: take a diagonal \(B_n\) of dimension \(d_n\ge n\) with spikes \(\pm n^{-1/4}\), and its remaining eigenvalues in balanced pairs \(\pm d_n^{-1/2}\). Odd trace moments vanish, \(\operatorname{Tr}B_n^2=O(1)\), and every fixed even moment at least four is \(O(1/n)\), but the spikes exceed \(d_n^{-1/2}\). This is an explicit counterexample to that inference from moments, not a constructed neural-network Hessian violating their prediction. Their eigenvalue comparisons are supported by reported numerical evidence; the displayed argument alone does not certify all those rates. Late-time claims also presume residual decay.

## Experiments and computational cost

All paper experiments are **reported evidence only**, not reproduced here. Dyer Table 1, p.5, tests six correlations in three-hidden-layer linear, ReLU, and tanh networks, widths \(2^7\) through \(2^{13}\), with 1000 initializations per width; Appendix A.1 repeats the comparison for Bernoulli weights, outside the stated Gaussian proofs. Dyer Table 3, p.20, checks variance exponents. A.2 p.11 specifies the MNIST subsets and training settings used for its finite-width dynamics plots. E.3 pp.27–28 compares Hessian/NTK spectra and moments. Aitken Table 1, p.7, uses the same width range and 1000 initializations for three-hidden-layer tanh, sigmoid, softplus, linear, ReLU, and hard-sigmoid networks; Table 2 p.18 reports variance exponents. Its Appendix D gives a polynomial example with an additional leading contribution absent in the linear case, explaining why an upper bound can be tight for nonlinear activations and loose for piecewise-linear ones. These tests do not prove a general smooth theorem or a universal tightness claim.

Wick expansion contains explicit coefficient information, as the simple examples in Dyer Eq.(6) and Aitken Eq.(8) demonstrate. In a fixed polynomial network it is in principle a finite exact calculation, including subleading powers. The number of monomials and Gaussian pairings can grow rapidly with degree, depth, and derivative order; these papers give no general efficient-compilation guarantee. MFP also explicitly disclaims such a guarantee and can suffer expression expansion. This audit contains no timing benchmark or complexity proof supporting an MFP speed advantage. The concrete software distinction is that the maintained MFP API performs typed finite-width AD and then builds a source-response expectation graph, retaining general activation integrals as explicit objects; it does not compute finite-width \(1/n\) corrections merely by taking its limiting output.

## Recommended positioning and residual uncertainty

Credit Dyer and Gur-Ari for the contracted-derivative framework, derivative hierarchy, diagrammatic finite-width analysis, and the linear/special nonlinear bounds. Credit Aitken and Gur-Ari for the fixed-polynomial proof and covariance improvement. Describe MFP as a constructive derivative-program calculus grounded in its cited Gaussian tensor-program foundation, with a specified reusable-matrix/scalar-feedback language and explicit limiting expectation graph. It is reasonable to distinguish the smooth polynomial-growth program theorem from the polynomial diagram theorem, and deterministic mean-field scalar outputs from generally fluctuating NTK-parameterized outputs. It is not reasonable to claim that diagram methods generally lack arbitrary derivatives, Gaussian expectation constants, or all-moment consequences.

The identified errors are precise local issues, several demonstrably repairable, and do not furnish a counterexample to the correctly normalized polynomial cluster theorem. The principal unresolved access issue is the complete ICLR version. The ReLU gate-independence dependency was not independently re-proved from its external primary source. No numerical training experiment, spectral experiment, or runtime comparison was reproduced. Those limits should accompany any downstream use of this report.
