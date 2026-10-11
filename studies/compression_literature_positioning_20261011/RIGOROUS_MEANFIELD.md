# Nguyen–Pham (2023): scoped literature assessment

**Superseded assessment.** Use [AUDIT_NGUYEN_PHAM.md](AUDIT_NGUYEN_PHAM.md) for the fresh source-only proof audit and its more precise coupling qualifications. This initial report is not the controlling verdict.

**Source and coverage.** Phan-Minh Nguyen and Huy Tuan Pham, *A rigorous framework for the mean field limit of multilayer neural networks*, Math. Stat. Learn. 6 (2023), 201–357, DOI 10.4171/MSL/42. [Publisher record](https://ems.press/journals/msl/articles/12725639), [published PDF](https://ems.press/content/serial-article-files/29198?nt=1). Access checked 2026-10-11. The complete published article was read: main text §§1–9, pp. 201–278; Appendices A–G, pp. 278–354; references and end matter, pp. 355–357. Rendered equation pages 224, 229, 257, 260, 268 and 269 were visually inspected. The cached PDF/text and inspection images are under `data/generated/compression_literature_positioning_20261011/meanfield/`. Comparison inputs were the complete `paper/main.tex` and `paper/feature_learning_theorem.tex`; their included proofs were outside this assignment. No other studies, code or experiments were consulted or executed.

This is a public-paper, venue-neutral assessment of the specified comparison. The review skill and severity rubric were applied within the assigned single-report format. Complete reading is not complete independent proof reconstruction. Exact locators below use printed journal pages; PDF page = printed page minus 200.

## Assessment

This is substantial rigorous prior work on nonlinear multilayer population dynamics. It provides an actual coupling to finite networks, quantitative finite-time width bounds, and conditional global optimization theorems. It should not be described as merely a formal limit, as lacking trajectory guarantees, or as proving only lazy/kernel learning. Its state, scaling, time quantifiers and optimization assumptions nevertheless differ from the manuscript's finite autonomous compression target. No result in the reviewed paper supplies the conjunction of a small finite retained state, coupling to the manuscript's ordinary Gaussian network, uniform prediction fidelity through its finite-network fitted endpoint, and error negligible relative to actual independent-seed discrepancy.

The last sentence describes a difference in objectives, not a defect in Nguyen–Pham's contribution. Nor does this single-paper comparison establish a literature-wide priority claim.

## State, model and initialization

Nguyen–Pham use $L$ for the number of weight layers, including the scalar output layer. The manuscript uses $L$ for hidden layers. Thus their depth for the manuscript's architecture would be $L+1$. To avoid conflating the conventions, write $D$ for Nguyen–Pham's depth in this report only.

For the bias-free scalar network in (7.1), p. 255, their forward recursion is

\[
H_1(x,j_1)=\langle w_1(j_1),x\rangle,
\qquad
H_i(x,j_i)=\frac1{n_{i-1}}\sum_{j_{i-1}=1}^{n_{i-1}}
w_i(j_{i-1},j_i)\varphi_{i-1}(H_{i-1}(x,j_{i-1})),
\]

for $i=2,\ldots,D$, with $n_D=1$ and output $\widehat y(x)=\varphi_D(H_D(x,1))$. Here $n_i$ is the width at layer $i$, $w_1(j_1)\in\mathbb R^d$, and the other weights are scalar. SGD uses compensating layer learning rates; the general framework also admits biases, Hilbert-space-valued weights, convolutional examples and learning schedules (§2.1, pp. 208–212).

The neuronal ensemble is a fixed product probability space $\prod_{i=1}^{D}(\Omega_i,P_i)$, with $\Omega_D=\{1\}$. Its moving state comprises functions

\[
w_1(t,\cdot):\Omega_1\to\mathbb R^d,
\qquad
w_i(t,\cdot,\cdot):\Omega_{i-1}\times\Omega_i\to\mathbb R,
\]

and, in the general model, bias functions. Forward and backward sums become expectations over independent labels $C_i\sim P_i$. Their ODEs evolve these functions using the current forward and backward quantities and an expectation over the data distribution (§2.2, pp. 212–214; §7.2, pp. 255–256). This is a closed function-valued evolution. Constant learning schedules make it autonomous; the full framework permits explicit time dependence. Width-independent notation does not make the moving state finite-dimensional, and there is no theorem counting its numerical representation, retained real coordinates or fixed coefficient storage.

The coupling is concrete: sample neuronal labels once, then initialize each finite-network weight by evaluating the corresponding initial weight function at its sampled endpoint labels (Definitions 4.1–4.3 and §4.1, pp. 221–223). The finite network is random, whereas the population trajectory for a fixed ensemble/embedding is deterministic. Remark 2.3, pp. 213–214, also embeds a finite network exactly by taking finite uniform label spaces; that retains the finite network's own weights and is not itself a compression result.

**Exact scaling comparison.** In the manuscript, a hidden matrix acts as $z^{(\ell)}=W^{(\ell)}h^{(\ell-1)}$, with entries of $W^{(\ell)}(0)\sim\mathcal N(0,1/n)$. To identify the same forward map with the displayed averaged recursion at equal widths, one must set $w_\ell(j,k)=nW^{(\ell)}_{kj}$. These source-coordinate weights then have variance $n$, not a width-uniform sub-Gaussian scale. Assumption 4.6, pp. 223–224, requires a fixed bound on the sub-Gaussian moments. Thus the published many-width bound cannot simply be applied to this rescaled initialization with a width-independent constant. The input rescaling $x\mapsto x/\sqrt d$ and identity output activation are harmless identifications; the hidden-weight scale is substantive. The manuscript also allows unbounded activation values and uses squared loss, while the directly stated feedforward mean-field assumptions impose bounded hidden activations and bounded loss derivative. Extending the mean-field result by localization would require an additional argument.

## Quantitative trajectory guarantees

Theorem 4.7, p. 224, assumes bounded Lipschitz schedules (2.4), specified forward/backward growth and perturbation bounds (2.5–2.6), weakly dependent embedding samples (4.4), and sub-Gaussian initialization (4.6). For every fixed finite terminal time $T$, sufficiently large minimum hidden width $n_{\min}$, and sufficiently small SGD step $\epsilon$, it gives

\[
\mathcal D_T(W,\mathbf W)
\lesssim
(n_{\min}^{-c_1}+\epsilon^{c_1})
\sqrt{\log(n_{\max}^{2}/\delta+e)}
\]

outside an event of probability at most $2\delta+KD n_{\max}\exp(-K n_{\min}^{c_2})$. Here $\mathbf W$ is the SGD network, $W$ the population state, $\delta>0$ the confidence parameter, and $0<c_1<1/2$, $0<c_2<1/52$. The paper does not give explicit numerical values of these exponents. They are independent of depth and $T$, but the sufficient-width and step-size thresholds depend on $T$ and depth. Equation (4.1), p. 223, defines $\mathcal D_T$ as the maximum over layers/weight or bias types of the square root of the neuron-averaged squared, time-supremum coupled parameter error.

Theorem 4.12, p. 228, gives the corresponding population-versus-continuous-time-particle bound without the SGD discretization term. Theorem 4.13 controls particle-versus-SGD error. Calling these only distributional or nonquantitative results would miss their explicit coupling and rates.

For bounded initial weights and biases outside the first layer, Proposition 4.14, p. 229, gives a square-root-width bound. Its time dependence includes

\[
\sqrt{\frac1{n_{\min}}\log\!\left(\frac{2TD}{\delta}n_{\max}^{2}+e\right)}
\exp\!\left(K^{\bar K}(1+T^{\bar K})(1+B)\right),
\qquad \bar K\le K^D,
\]

where $B$ bounds those initial weights and biases. Proposition 4.15 supplies the analogous square-root-step-size estimate. Remark 4.8 mentions a stronger earlier bounded-initialization result; that earlier version was not independently reviewed here. The published propositions themselves already establish quantitative square-root rates under their stronger initialization assumption.

Corollary 4.9, pp. 224–225, transfers the coupling to bounded Lipschitz tests of layer features averaged over neurons and data, and to data-averaged Lipschitz tests of predictions. The displayed conclusions are uniform over $t\le T$. They are not the manuscript's supremum over the complete sphere or a specified passive panel. The proof also controls stronger intermediate prediction differences; the relevant limitation is the actual stated observable and horizon, not an assertion that the paper has no prediction control.

The proof architecture was followed through Appendix C: moment and concentration estimates, population/particle comparison, a separate SGD martingale comparison, Gronwall estimates, and truncation of sub-Gaussian initialization. No all-time estimate is hidden in those appendices. The exponential-in-$T$ factor in the bounded case and $T$-dependent onset in the general case prevent replacing finite $T$ by infinity without new control.

## Optimization and the order of limits

Theorem 3.1, p. 218, gives global existence and uniqueness of the mean-field evolution. Existence for every finite time is distinct from an all-time finite-width approximation or convergence to a fitted endpoint.

| Result | Actual endpoint conclusion and qualifications |
|---|---|
| Theorem 6.2, p. 242; Assumption 6.1 | Two-weight-layer population network: global minimum risk for convex loss, or zero risk for deterministic labels and a nonnegative loss whose stationary predictions have zero loss. Requires initial diversity, universal approximation, regularity, weighted moment convergence and uniform vanishing of the second-layer velocity. |
| Theorem 6.6, pp. 246–247; Assumption 6.5 | Three-weight-layer, i.i.d.-initialized population dynamics: corresponding risk conclusions. Adds weighted moment convergence and uniform vanishing of the middle-layer velocity; the output layer is either fixed with nonzero mass or trained from risk strictly below the zero-output baseline. The latter alternative does not cover the manuscript's identically zero initial readout. |
| Theorem 7.2, p. 258; Assumption 7.1, p. 257 | Arbitrary depth: corresponding population-risk conclusions, with correlated initialization satisfying bidirectional diversity, weighted moment convergence and uniformly vanishing last-layer velocity. |
| Theorems 8.2 and 8.4, pp. 266 and 268 | Alternative global convergence statements replace the uniform-velocity assumption by detailed Morse–Sard-type conditions on the limiting potential. Moment convergence is still assumed, and the arbitrary-depth theorem still uses the correlated diversity conditions. |

Bidirectional diversity in Assumption 7.1 requires full support of the incoming/outgoing weight-function pair in products such as $L^2(P_{i-1})\times L^2(P_{i+1})$. It is not ordinary independent Gaussian initialization. The proof of Theorem 7.2 preserves that diversity for every finite time by reversible auxiliary flows, propagates universal approximation through the layers, then uses the assumed convergence to obtain an optimal limit (§7.5, pp. 260–265). Diversity at the limiting point is not assumed. This is a substantive strength.

Finite-network Corollaries 6.3, 6.7 and 7.4, pp. 243, 247 and 260, take the limits in the order

\[
\lim_{t\to\infty}\lim_{n_{\min}\to\infty}\lim_{\epsilon\to0}
\mathbb E_Z\,\mathcal L(Y,\widehat y_{n,\epsilon}(\lfloor t/\epsilon\rfloor,X)).
\]

Unequal widths must obey the stated mild relative-growth condition. These conclusions do not exchange the width and time limits, prove fitting of every sufficiently wide fixed network, or identify matched finite-network and reduced-model fitted predictors. Conditional population optimization remains valuable even though it does not supply those stronger conclusions.

## I.i.d. degeneracy and empirical evidence

Section 5 constructs canonical embeddings for i.i.d. weights. Theorem 5.3, p. 235, completed by Theorem D.1, pp. 334–335, compares those embeddings to a simplified dynamics with error $K_{T,D}M^{-0.499}$ for fixed $T$, where $M$ is an auxiliary embedding-size parameter. This is not a retained-coordinate complexity bound.

Corollary 5.5, p. 237, says that for source depth $D\ge4$ and constant initial biases, the intermediate preactivations at layers $2,\ldots,D-2$ collapse to a common neuron-independent input function in the limit. Corollary 5.6, p. 238, additionally gives one deterministic translation of all weights within each layer $3,\ldots,D-2$, for $D\ge5$ and update maps independent of the current weight argument, including the specified unregularized feedforward examples. The same deterministic translation need not occur across different layers. These are precise degeneracies of this averaged mean-field scaling, not a no-feature-learning theorem for every Gaussian parameterization. The correlated initialization in §7 is designed to avoid this bottleneck.

There is no original numerical experiment or code validation in this article. Section 9.5, pp. 277–278, discusses observations from other papers, including Nguyen (2019), reference [23], and Lu et al. (2020), reference [20]. Those citations are not reproduced empirical evidence of this article's finite-time bounds, endpoint assumptions or any below-seed comparison. This assessment did not retrieve their experiments and does not independently endorse their numbers.

## Claim ledger, verification limits and safe wording

| Claim assessed | Evidence and assessment |
|---|---|
| A rigorous nonlinear multilayer mean-field framework with finite-network coupling exists. | §§2–4 and Appendices A–C give detailed constructions and proofs. Highly plausible; model, coupling, quantifiers and truncation/Gronwall architecture checked. A full audit of every estimate and external concentration theorem was not performed. |
| I.i.d. initialization can produce strong degeneracy in the stated mean-field scaling. | §5 and all of Appendix D read; exact indices, bias assumptions and translation conditions checked. Highly plausible within this scaling. Transferring this claim to the manuscript's different initialization normalization would be an unjustified extrapolation. |
| The paper establishes global optimization. | Correct as a description of the conditional theorem statements above; it is not unconditional finite-width fitting. The diversity-preservation and universal-approximation mechanism was followed. Section 8 has unresolved proof-reading questions described below, so no blanket soundness certificate is assigned. |
| It already proves the manuscript's compression guarantee. | Unsupported by any result in this paper. The retained state, initialization scale, time quantifiers and actual-seed denominator do not match. This is a scope distinction, not an author flaw. |

Two proof-reading questions in the alternative arbitrary-depth Morse–Sard argument remain open in this assessment. At the top of p. 269, convergence of the functions $G_D(t,u)$ and $G_{D-1}(t,u)$ is asserted uniformly over the unbounded space $u\in L^2(P_{D-2})$; basic moment convergence alone does not supply such uniformity when $u$ acts on changing features. The following paragraph obtains a positive local maximizer either in that Hilbert space or on its unit sphere from boundedness and a radial limit; an infinite-dimensional sphere is not compact. Additional structure may resolve these steps, but it was not independently reconstructed here. These are unresolved checks of Theorem 8.4's proof, not a counterexample to its conclusion, and they are not needed for the positioning distinction. No fatal/major/minor classification is assigned to an unestablished flaw.

External dependencies not independently audited include Pinelis (1994), reference [30], invoked in Appendix A for Hilbert-space concentration, and the universal-approximation literature used for examples of admissible activations. This is a verification boundary, not evidence against those results. Confidence is high on what the published statements promise and their mismatch with the proposed compression target; lower on complete proof correctness, especially the alternative §8 argument. The manuscript's own compression and feature-learning proofs were not assessed.

There is no lower bound or anti-concentration theorem for the manuscript's realized independent-seed discrepancy here. Even a square-root-width *upper* error bound would not by itself prove a vanishing ratio to that random denominator. Likewise, a finite discretization of the population state would need its own approximation and storage theorem; its existence or size cannot be inferred from a function-valued ODE alone.

**Suggested related-work wording:** “Nguyen and Pham develop a rigorous neuronal-embedding framework for multilayer mean-field training, with quantitative couplings on fixed finite time intervals and conditional population-level global convergence results. Their evolving state consists of functions on a fixed neuronal probability space, under mean-field normalization and specified initialization assumptions. Our target is a finite retained-state model coupled to a Gaussian-initialized finite network, with uniform prediction control through its fitted limit and error negligible relative to actual independent-run variability.”

The present related-work paragraph in `paper/main.tex` already makes the central distinction fairly. A precise revision could add “on fixed finite time intervals” to the trajectory comparison and “conditional population-level” to optimization, while preserving credit for quantitative finite-network coupling.

Finally, §9.5, p. 278, explicitly points to a distinct follow-up: Pham and Nguyen, *Limiting fluctuation and trajectorial stability of multilayer neural networks with mean field training*, NeurIPS 2021, pp. 4843–4855, reference [29] on p. 356. Its complete main paper and supplement are separately assessed in [TRAJECTORIAL_FLUCTUATIONS.md](TRAJECTORIAL_FLUCTUATIONS.md). That work proves quantitative fluctuation-scale coupling, an output CLT and conditional decay of width-scaled variance. Those stronger fluctuation conclusions must be credited to the follow-up, not silently attributed to this 2023 article or omitted from an assessment of the research line.
