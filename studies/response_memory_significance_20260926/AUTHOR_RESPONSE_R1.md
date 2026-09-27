# Author response to Round 1

We thank the reviewer for rechecking both proofs and for separating the central mathematical result from the remaining localized issues. Round 1 reaches an important common ground: for positive initial residual, both compact-horizon trajectory theorems are sound at fixed finite width, depth, data and initialization; the response-clock argument is self-contained and noncircular; the Variant-B state count and resource statements are correct; and no fatal or major theorem defect remains.

We have applied all five requested V2 repairs in the manuscript itself. We also preserve every substantive correction made in V1. The resulting claim is deliberately precise and strong: coupled forward/backward response histories admit a finite-scalar autonomous moment closure at each fixed network and order; exact bilinear cancellation turns the physical matrix-update defect into a product of two projection errors; and the resulting nonlinear self-consistent closure tracks the complete fixed-width parameter path on every prescribed compact horizon, at order $O(P^{-1})$ for the activity clock and $O(P^{-2})$ for the response-speed clock.

## What the remaining limitations mean for the breakthrough claim

The remaining limitations do not diminish the central mathematical breakthrough in representation and trajectory closure. They delimit it.

The hard problem solved here is not ordinary compression of an array. The histories are endogenous: approximating them changes the reconstructed weights, which changes future forward activations and backward responses, which changes the histories being approximated. The closure nonetheless remains autonomous and restartable from a state whose size is independent of elapsed training time. The exact differentiation of the projected bilinear reconstruction cancels both mixed terms, leaving a product of the forward and backward projection errors. That cancellation is then propagated through the full nonlinear network rather than only through outputs or kernels. Variant B adds a second substantive construction: it chooses a coordinate in which the entire concatenated response path has unit speed, proves a clock bound before invoking sharp approximation, and closes the residual, physical, Gram and continuation stops to obtain $O(P^{-2})$ full-trajectory control.

We therefore defend “breakthrough” in this bounded technical sense: the work resolves a self-consistent mathematical representation and trajectory-closure obstruction that the reviewed exogenous-memory, hierarchy and population precedents do not resolve for one fixed finite deep network. We do not use the word to claim an efficient-training system, empirical confirmation of the asymptotic rate, or unrestricted historical priority. The absence of net storage reduction and runtime acceleration limits a systems-breakthrough interpretation. The lack of same-time rate experiments limits an empirical-breakthrough interpretation. The nonexhaustive literature packet limits a field-wide priority interpretation. None changes the proved mechanism or the complete physical-trajectory theorem.

The revised conclusion now makes this separation explicit in the manuscript at lines 1215–1224. It identifies the mathematical advance as representation and trajectory closure, and states that total storage, speed, empirical rate verification and unrestricted priority are separate questions whose current limitations bound scope without weakening the theorem.

## O1 — Variant-B state count

**Disposition: resolved in V1 and preserved without retreat.**

V2 continues to count the complete Variant-B moving state as

\[
nd+n+2(H-1)mnP+\frac{P(P+1)}2+1
\]

with a symmetry-packed Gram, while noting that the implementation stores $P^2$ Gram entries. It separately lists fixed $W_0$ and matching-prefix factors in the exact state table at lines 888–914. The complete sufficient accuracy scaling remains

\[
O\!\left(Hmn\varepsilon^{-1/2}+\varepsilon^{-1}\right)
\]

at lines 959–975. We agree that $O(Hmn\varepsilon^{-1/2})$ applies only to the history factors.

This correction is important for resource interpretation, but it does not weaken the response-clock theorem. The Gram is precisely what implements weighted projection in the evolving measure; counting it correctly changes the state claim, not the $O(P^{-2})$ trajectory estimate.

## O2 — Storage, runtime and crossover interpretation

**Disposition: resolved in V1 and preserved.**

V2 retains the exact learned-correction and total-action distinction, including the direct $W_0$ and transpose actions and the Variant-B factorization, solves and directional passes (lines 916–929). It retains the exact history crossover

\[
2mP<n,
\]

the complete Variant-A inequality, and the symmetry-packed Variant-B inequality

\[
2(H-1)mnP+\frac{P(P+1)}2+1<(H-1)n^2
\]

at lines 931–947. It continues to say that the theorem does not place an accuracy-sufficient order below these crossovers and that restartable total storage exceeds a minimal dense current-weight implementation (lines 946–958). The unfavorable measured MNIST totals and runtimes remain explicit at lines 1151–1160.

We concede no additional point here because the paper now makes exactly the distinction the evidence requires. The result is learned-increment model reduction and elapsed-time-independent response-history closure. It is not a claim that standard dense gradient flow otherwise stores its full literal history, and it is not a net memory or runtime theorem.

## O3 — HiPPO and NTH

**Disposition: resolved in V1 and preserved.**

The manuscript continues to credit HiPPO for time-dependent polynomial projection, scaled Legendre memory and triangular dilation dynamics, while distinguishing an exogenous signal from the present pair of endogenous neural histories (lines 125–138). The NTH comparison retains the direct $O(m^p)$ training-tensor count, the translated horizon and output bound, the $O(m^{p-1})$ test-point count, the absence of a demonstrated truncated solver in the supplied source, and the different wide output/kernel target (lines 140–168).

Those credits narrow ingredient novelty but leave the central result intact. Neither precedent supplies the coupled learned-matrix reconstruction, the exact product-error identity under neural feedback, or a full fixed-network parameter-path theorem.

## O4 — Companion finite-type population closure

**Disposition: accepted and repaired in full.**

We agree that removing the earlier companion discussion did not answer this positive precedent. V2 now gives it a dedicated paragraph at lines 201–210 and a separate row in the contract table at line 241. The bibliography cites the maintained book and exact Section C.4.7.9 theorem anchor in references.bib lines 164–170.

The paragraph records every relevant positive fact identified by the reviewer: the systems are increasing and finite-type, autonomous, restartable from saved current state, and give uniform compact-time convergence of whole-circle predictions and declared joint observations for a specific nonlinear two-hidden-layer population flow. It also states the exact mismatch: their state contains two probability laws and a finite matrix of action contractions and therefore has infinitely many scalar degrees of freedom; they give no quantitative state/error rate and do not approximate the complete parameter path of one fixed finite network.

This precedent strengthens rather than undermines the paper's framing. It shows that autonomous restartable nonlinear closure is possible at the population-law level. The present theorem crosses a different boundary: a finite-scalar state at fixed $n,m,H,P$, one actual finite realization, learned internal-matrix reconstruction, the complete physical parameter trajectory, and explicit $P^{-1}$ and $P^{-2}$ compact-horizon rates. V2 retains the explicit “reviewed, nonexhaustive source set” limitation and makes no unrestricted priority claim (lines 246–252).

**Concession.** The companion theorem is a close positive autonomous-closure precedent and should have appeared in V1. It does not displace the fixed-finite-network theorem or its bilinear response mechanism.

## O5 — The zero-residual Variant-B branch

**Disposition: accepted as a formal definition defect and repaired without changing the positive-residual theorem.**

V2 no longer asserts that the displayed normalized-response ODE is defined at $0/0$. Before defining $\Psi$, it states that Variant B is defined for $\rho(0)>0$ and treats $\rho(0)=0$ as a separate trivial physical branch: dense gradient flow is constant and requires no normalized response or response-clock state (lines 628–633). The theorem continues to assume $\rho(0)>0$ and now explicitly says that the zero-loss physical branch is separate from the normalized-response ODE (lines 683–700). The proof begins with the stated positive-residual assumption (line 703).

This is the cleanest repair because it does not manufacture a locally unique extension of $r/\rho$ through the origin. The physical zero-loss statement remains true, while uniqueness is claimed only on the regular positive-residual branch actually analyzed.

The substantive proof remains unchanged. It still derives the dense residual lower bound and stopped tube, the raw coarse defect before the clock bound, the normalized-residual derivative formula, the unconditional clock bound, the joint Legendre tail, the sharp $1/[P(P+1)]$ defect, the explicit order conditions, and fixed-$P$ Gram continuation (lines 703–845).

**Concession.** V1's one-sentence zero-residual assertion did not define the displayed autonomous state. This was a branch-definition problem, not a defect in the positive-residual theorem.

## O6 — Factor-control initialization asymmetry

**Disposition: accepted and repaired.**

V2 now states the exact initialization at lines 1018–1024:

\[
A(0)=0,\qquad B_{ij}(0)\sim N(0,1/r).
\]

It explains that the factor control matches the initialized physical network exactly but matches the dense initial middle-matrix velocity only in expectation over $B$, not for either realized seed. The existing limitations remain: the comparison concerns two prescribed seeds, Euclidean factor flow, the specified matched-rank endpoint metric, and neither matched total compute/state nor all trainable low-rank methods (lines 1024–1033).

**Concession.** The realized initial-velocity asymmetry weakens a causal reading of the factor result as a pure representation comparison. It does not invalidate the numerical statement that response moments had lower error on the frozen metric in the 29 valid comparisons. We now present it only with the qualification needed to interpret that result.

## O7 — Empirical scope

**Disposition: resolved in V1 and preserved.**

V2 continues to state that the panels are separately stopped matched-loss endpoint comparisons, generally at one initialization, and do not estimate same-time physical-parameter error or an order-rate slope (lines 1035–1047). It preserves the adverse response-clock step sensitivity, high-order case, Gram conditioning, runtime ratios, strict-fit denominators, fitted-pair medians and maxima, and miss count (lines 1048–1070). It preserves nonmonotone deep-circle and MNIST order behavior and the unfavorable total resource numbers.

We agree with the reviewer that a new experiment is not required to sustain the theorem. The empirical evidence supports executability and selected low-order predictor fidelity. It does not validate either trajectory rate, robust behavior across initialization, or practical response-clock superiority.

This limitation does not weaken the theorem because the theorem is proved analytically and the manuscript no longer uses the experiments as rate evidence. It does prevent an empirical-breakthrough claim, which we do not make.

## O8 — Build-complete frozen V2 source

**Disposition: accepted and repaired.**

V2 now has a self-contained frozen build in this study:

- CANDIDATE_V2.tex;
- REFERENCES_V2.bib, named exactly as the TeX requests;
- V2_figures/circle_shallow.pdf;
- V2_figures/circle_deep.pdf;
- V2_figures/mnist_scatter.pdf;
- V2_figures/mnist_rms.pdf; and
- BUILD_V2.md with the exact build command and tool versions.

From the study directory,

    latexmk -pdf -interaction=nonstopmode -halt-on-error CANDIDATE_V2.tex

builds CANDIDATE_V2.pdf without consulting the live paper directory. The verified environment is latexmk 4.76, pdfTeX 3.141592653-2.6-1.40.22 from TeX Live 2022/dev/Debian, and BibTeX 0.99d. Citations and cross-references resolve cleanly.

The live paper/main.tex and paper/references.bib also build cleanly. Thus the reviewed object and the live manuscript now have separate reproducible builds.

**Concession.** V1's rendered PDF was valid, but its frozen TeX inputs were not independently complete. V2 repairs that reproducibility defect.

## O9 — Finite-scalar terminology

**Disposition: accepted and repaired.**

The state-class definition now says that a finite-scalar ODE has finitely many real coordinates for each fixed $n,m,H,P$; its dimension may depend on those parameters but not on elapsed training time or a population discretization (lines 107–113). This agrees with the $O(HmnP)$ response state, the contract-table caption, and the contrast with probability-law and operator states.

We do not introduce a width-independent aggregate class because no such closure is proved here. The limitations section continues to identify an economical width-uniform scalar closure as open.

**Concession.** V1's definition mistakenly built width independence into “scalar ODE” and contradicted its own table. V2 now uses one consistent definition.

## Final scientific position

Round 1 confirms the mathematical core after independent re-audit: no major or fatal proof flaw remains; the ordinary-clock depth induction does not lose an order; and the response-clock proof obtains its clock bound without circular use of the sharp tail. The five V2 edits improve positioning, branch definition, baseline interpretation, reproducibility and terminology. None changes either positive-residual trajectory theorem.

The most consequential result remains the coupled neural closure mechanism. A forward history alone cannot reconstruct the learned matrix update, and a backward history alone cannot either. Their projected product does. Orthogonality then removes both mixed errors exactly, so physical defect is second order in the two approximation errors. Variant A uses one controlled forward-history tail and coarse backward energy to obtain $O(P^{-1})$ uniformly along the complete path at each fixed depth. Variant B regularizes the entire concatenated path and converts the same cancellation into $O(P^{-2})$. The closures are autonomous even though their approximated histories are generated by the closures themselves.

That is why total-storage, runtime and empirical-rate limitations do not diminish the representation/trajectory-closure breakthrough. They answer different questions. They do prevent broader claims, and V2 states those boundaries directly. Likewise, crediting HiPPO, NTH, population dynamics, DMFT, Mori–Zwanzig and the companion finite-type population closure does not erase the fixed-width full-parameter theorem; it identifies precisely what had to be added to those precedents.

Within the reviewed nonexhaustive source set, the complete contract remains unmatched. We make no statement beyond that source-bounded comparison. The final manuscript therefore presents a forceful but delimited claim: a mathematically new response-history representation and compact-horizon trajectory-closure theorem for deep nonlinear fixed-width gradient flow, with no accompanying claim of net efficient training, empirical rate confirmation, or unrestricted priority.
