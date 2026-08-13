# Finite Causal PDE Closure of Dense $\mu$P Feature-Learning Dynamics

## Master research monograph

> **Dated baseline.** This monograph records the project state on 31 July
> 2026.  It predates the maintained mean-field-peeling and output-kernel
> Stieltjes studies.  For later results, use the scoped current reports in
> [`studies/mean_field_peeling/`](studies/mean_field_peeling/) and
> [`studies/stieltjes_conjecture/`](studies/stieltjes_conjecture/).  Those
> reports supersede this document within their respective scopes.

**Document version:** 2.2  
**Release date:** 31 July 2026  
**Original release:** Version 1.0, 27 July 2026  
**Supersedes:** `FINITE_CAUSAL_NEURAL_PDE_MASTER_MONOGRAPH_v2.1_2026-07-28.md`  
**Project state:** 31 July 2026  
**Audit state:** The Version 2.1 mathematical and empirical claim ledgers remain unchanged. Version 2.2 adds the active repository crosswalk and a bounded post-Version-2.1 execution audit. Executable code and configurations are now present for most numerical programs, the central \(P=5\) PDE and its autonomous plateau have been rerun, and the preserved archive and evidence seals verify. Some compact releases still omit their complete raw trajectory collections, one historical ad hoc runner was not preserved, and no post-Version-2.1 check upgrades an open or conditional theorem. The recovered quadratic forest result, the remaining bridge `(FW)`, and the external TP/DMFT audit retain exactly their Version 2.1 status; see Appendices C.4 and D.6–D.9.  
**Central model class:** fully dense, fully trained, genuinely nonlinear Euclidean-$\mu$P networks  
**Canonical positive laboratory:** residual network, width first and residual depth second  
**Canonical negative laboratory:** two-hidden-layer network with unbounded quadratic features and positive Wick algebra  
**Primary observables:** outputs, loss, and depth-indexed hidden Gram matrices

## Executive synopsis

The project asks whether the deterministic limits furnished by modern infinite-width theories can be compressed further into a finite causal macroscopic state.

The broad thesis is:

> In a standard deep, dense, fully trained, nonlinear $\mu$P feature-learning regime, the ordered wide/deep training dynamics of outputs and representations admit an architecture-derived, autonomous PDE description with finitely many field species over a fixed finite-dimensional source space, to arbitrary prescribed accuracy, without retaining microscopic matrices or a training-history object whose dimension grows with the time horizon. The compiled PDE is internally restartable from its declared state. The stronger restart-robust form also supplies a correspondence from physically consistent positive-time dense states to PDE states and controls the future continuation error.

This is stronger than the existence of deterministic trajectories. Tensor Programs already derive infinite-width feature-learning limits under $\mu$P, and dynamical mean-field theory represents feature learning through self-consistent stochastic processes, two-time correlation kernels, causal response kernels, and memory. The first additional theorem sought here is an architecture-compiled autonomous approximation from canonical compiled initial states, with complexity independent of width and original depth. A still stronger theorem would prove that its current macroscopic state is also a sufficient restart state for the dense limit. Under the strongest formulation, the state type and complexity are independent of the training horizon.

The project has not proved those theorems. It has, however, documented four substantive findings.

1.  **A literal finite-cutoff PDE system is specified.** For the canonical residual architecture, the operator–Hermite Liouville construction is autonomous, width-independent, and uses the same projected operator in the forward and transpose directions. At every finite cutoff, wherever the flow is well posed, its projected-gradient identity, positive-semidefinite tangent kernel, direct moment readouts, and loss dissipation are exact internal theorems. A general existence theorem for that coupled PDE is not supplied.
2.  **The smallest nonlinear PDE is an accurate nonlazy surrogate on the tested family.** In the canonical benchmark it reproduces $O(1)$ hidden-Gram motion with a normalized Gram-increment discrepancy of about $1.14\%$, although the remaining gap is statistically resolved. Across fourteen transfer configurations, the reported median/max normalized errors were $1.71\%/4.14\%$ for Gram increments, $1.46\%/1.83\%$ for outputs, and $0.63\%/1.97\%$ for loss.
3.  **Several mundane explanations are rejected by the tested controls.** The observed agreement is not frozen-feature behavior, exact identity/deep-linear dynamics, or a scalar reparametrization of training time on those controls. A nonlinear sine stress also rejects the tested fixed-gain linear explanation for Gram dynamics: paired dense linear and dense sine trajectories differ by $15.95\%$, while the nonlinear PDE differs from dense sine by about $2.50\%$ in Gram and $2.81\%$ in output. Adaptive or state-dependent linear surrogates remain outside that test, and the joint three-observable $5\%$ gate is not passed because the reported sine loss discrepancy is $5.54\%$.
4.  **The arbitrary-accuracy bridge remains open.** The parity-correct Hermite hierarchy has not shown replicated aggregate Cauchy contraction. Its infinite operator flow has not been identified with the ordered dense limit. Cutoff-uniform stability, trained-depth homogenization, the surviving conditional/Onsager mean, and the all-time tail are unproved.

The quadratic laboratory gives a complementary negative result conditional on the remaining fixed-order deterministic-limit bridge `(FW)`. The recovered primary file `finite_invariant_differential_algebra_resolution.md` genuinely proves that every raw derivative history is a normalized bipartite forest, derives the width exponent \(n^{c-\beta-r}\), classifies the leading component-preserving forest quotients, and includes readout-, middle-weight-, and first-layer-training hits. It then gives a compressed paragraph claiming an \(O(n^{-1})\) variance bound, but it does not complete the equality-partition proof of expectation convergence, the doubled covariance enumeration, or the resulting \(L^1\) limit. Conditional on that remaining bridge, the prescribed initial Wick–Taylor compiler has limiting coefficients with a factorial lower bound and zero radius of convergence; the associated physical-time predictions form an initial boundary layer and fail uniformly. The global residual-clock stability theorem survives, but its required approximation defect is not small for this compiler. A stronger claimed instantaneous-fitting theorem is valid only conditional on the stated tagged-site DMFT representation and its response-kernel hypotheses; those hypotheses are not derived in the supplied project proof and must not be reported as an unconditional theorem about the finite network.

The resulting project-level verdict is therefore:

> A small causal nonlinear PDE is a robust empirical surrogate with exact internal geometry. Pure source-Hermite truncation is a plausible but unproved arbitrary-accuracy witness. The central theorem—finite autonomous causal compression of standard dense feature learning beyond the native history-valued TP/DMFT descriptions—remains open. The most credible proof route combines source-weighted compactness with an explicit causal response/Onsager sector; if the static source law is insufficient, the missing response coordinates must be promoted rather than hidden.

## Status language used throughout

Every substantive claim is assigned one of the following statuses.

| Status                      | Meaning                                                                                                            |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------|
| **Proved**                  | A complete argument is present under the assumptions stated beside the claim.                                      |
| **Exact under assumptions** | The conclusion follows exactly once separately named hypotheses or a proposed limiting representation are granted. |
| **Empirically supported**   | The claim is supported on an explicitly identified tested family and no larger one.                                |
| **Disfavored**              | Contrary evidence exists, but the alternative remains logically possible.                                          |
| **Falsified in scope**      | The precise statement is contradicted on the stated model, topology, or compiler class.                            |
| **Open**                    | A necessary construction, identification, compactness, stability, or limit bridge is missing.                      |
| **Superseded**              | A later valid correction replaces the earlier formulation or interpretation.                                       |

“Exact” is never used to mean “numerically close.” “Finite-cutoff exactness” refers to identities internal to the PDE, not equality between that PDE and a dense network. Failure of one witness is never promoted into failure of the broad existence conjecture.

Words such as “established,” “rejected,” “impossible,” or “not found” that appear in local source summaries are descriptive prose, not additional authoritative status categories. The bold status in the Chapter 9 claim ledger, together with its scope column, controls whenever a local source uses different terminology.

## Document architecture

This monograph has a chapter-to-section hierarchy. There is no intermediate “Part” layer.

1.  The common thesis and the landmark gap beyond TP and DMFT.
2.  The standard-regime contract and the full conjecture lattice.
3.  The exact causal skeleton and common mathematical machinery.
4.  Boundary and non-standard regimes.
5.  The two-hidden-layer quadratic theorem laboratory.
6.  The canonical dense residual construction and its exact internal theory.
7.  Empirical evidence and adversarial tests.
8.  The convergence and identification frontier.
9.  The authoritative project-wide synthesis, supersession ledger, and theorem roadmap.

## Chapter 1 — The theorem being sought and the boundary beyond TP and DMFT

### 1.1 The common thesis

The project is not primarily a claim that wide neural networks have deterministic training limits. It is not primarily a claim that those limits can learn features. Tensor Programs (TP) and dynamical mean-field theory (DMFT) already provide such descriptions in important $\mu$P feature-learning regimes.

The common project thesis is a stronger **causal-compression** statement:

> **Central finite-causal-PDE conjecture \[open\].** In a standard deep, fully dense, fully trained, genuinely nonlinear Euclidean-$\mu$P feature-learning regime, the ordered wide/deep training limit admits an architecture-derived family of autonomous, restartable PDEs with finitely many field species over finite-dimensional source spaces, such that the relevant representation dynamics can be approximated to arbitrary accuracy without retaining microscopic matrices or a training-history state whose domain grows with the elapsed training horizon.

The strongest observable form asks that the closure order required for accuracy $\varepsilon$ be independent of width, original depth, and training horizon. As formalized below, this gives an autonomous, horizon-independent realization along architecture-compiled initial states. It becomes a theorem that the PDE state is a finite **causal sufficient state for dense-limit restarts** only when supplemented by a state correspondence and continuation estimate on a declared class of physically consistent positive-time states. Observable agreement from the canonical initialization alone does not prove that stronger statement.

To state this at observable level, let $\vartheta$ denote the data and static model parameters in a declared compact class $\mathcal U$. Assume, provisionally, that the ordered target

$$
\mathcal O_\vartheta(t)
=
\bigl(f_\vartheta(t),G_\vartheta^h(\cdot,t)\bigr)
$$

exists, where $f_\vartheta(t)\in\mathbb R^m$ is the training-output vector and

$$
G_{\vartheta,rq}^h(s,t)
=
\lim_{L\to\infty}\lim_{n\to\infty}
\frac1n
h_r^{\lfloor Ls\rfloor}(t)^\top
h_q^{\lfloor Ls\rfloor}(t)
$$

is the depth-indexed hidden Gram field. The order of limits is always

$$
\boxed{n\to\infty\ \text{at fixed }L,\qquad L\to\infty\ \text{second}.}
$$

The displayed pointwise formula is only notation for the candidate limit. The conjectured target requires convergence of an interpolated Gram field in the uniform depth/training-time topology declared in §2.2; pointwise convergence in $s$ would not by itself justify the supremum metric used below.

For an admissible finite-PDE family $\{\mathsf P_k\}_{k\ge1}$, define

$$
d_{\mathrm{obs}}
\bigl((f,G),(\widetilde f,\widetilde G)\bigr)
=
\|f-\widetilde f\|_2
+
\sup_{s\in[0,1]}
\|G(s)-\widetilde G(s)\|_F
$$

and

$$
E_k(T)
=
\sup_{\vartheta\in\mathcal U}
\sup_{0\le t\le T}
d_{\mathrm{obs}}
\left(
\mathcal O_\vartheta(t),
\mathcal O_{\mathsf P_k,\vartheta}(t)
\right).
$$

The central all-time claim is that **there exists one predeclared admissible family** $\{\mathsf P_k\}_{k\ge1}$ such that

$$
\boxed{\inf_{k\ge1}E_k(\infty)=0.}
\tag{1.1}
$$

Equivalently, for every $\varepsilon>0$, some finite architecture-compiled PDE has

$$
\sup_{\vartheta\in\mathcal U}
\sup_{t\ge0}
d_{\mathrm{obs}}
\left(
\mathcal O_\vartheta(t),
\mathcal O_{\mathsf P_k,\vartheta}(t)
\right)
<\varepsilon.
$$

The state type and its equations may depend on $\varepsilon$, the fixed sample count $m$, input dimension $d$, activation, and declared regularity bounds. They may not depend on $n$, the original layer count $L$, the realized future trajectory, or the requested physical training horizon.

This thesis must not be weakened by an ambiguity in the word “finite.” A law-valued PDE is still infinite-dimensional as a function space. “Finite PDE” means:

- finitely many field species;
- each field lives on a declared finite-dimensional source or phase space;
- the source dimension is independent of $n$, $L$, and elapsed training time;
- no source coordinate hides an arbitrary function, matrix, or infinite history;
- the PDE is autonomous and restartable from its own current state.

This last internal property rules out trajectory playback. It is distinct from the stronger assertion that every physically consistent dense-limit restart has a corresponding finite PDE state with uniformly accurate continuation.

For example, the current operator-Hermite candidate evolves a conditional probability law $\rho_{s,t}^{\theta}(dw)$. Even at finite Hermite cutoff it is not a finite scalar ODE. Its claim to compression is instead that $\theta$, $w$, and the field list are finite-dimensional at each cutoff and do not acquire a second training-time axis as $t$ grows.

**Status.** Equation (1.1) is open. What is established is the explicit construction and algebraic internal correctness of a particular finite-cutoff operator-Liouville PDE family wherever its displayed flow is well posed, together with strong low-order empirical accuracy in the tested residual-network regimes. General global well-posedness, convergence of that family, identification with the ordered dense limit, and the all-time upgrade are not proved.

**Project provenance.** `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, Executive conclusion and §§1, 3, 5; `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§2–5 and §11; `dense_euclidean_continuous_depth_npde_audit.md`, §§8–10.

### 1.2 What TP already provides

[Tensor Programs IV](https://arxiv.org/abs/2011.14522) studies an $L$-hidden-layer MLP through the $abc$ parametrization

$$
W^\ell=n^{-a_\ell}w^\ell,\qquad
w^\ell_{\alpha\beta}(0)\sim N(0,n^{-2b_\ell}),
\qquad
\eta_n=\eta n^{-c}.
$$

Depth, the data sequence, and the number of discrete training steps are fixed while $n\to\infty$. A complete forward/backward/training computation is compiled into a finite tensor program whose primitive operations are multiplication by an initialized Gaussian matrix or its transpose, coordinatewise nonlinear maps, and empirical coordinate averages.

The rigorous engine is TP IV, Theorem 7.4. For a fixed compiled program satisfying its pseudo-Lipschitz regularity assumptions, every empirical coordinate statistic

$$
\frac1n\sum_{\alpha=1}^n
\psi\!\left(h_\alpha^1,\ldots,h_\alpha^q\right)
$$

converges almost surely to the corresponding expectation of recursively defined limiting random variables, and every scalar in the program converges almost surely to its deterministic recursive value. Matrix/transpose reuse is not replaced by independence: the limiting variable for a multiplication by a reused matrix contains a fresh Gaussian part plus a regression or derivative correction generated by its dependence on earlier program variables. This is the TP counterpart of the response term emphasized in the present project.

Within the paper's stable, nontrivial $abc$ class, the main classification separates two regimes. In the full Appendix-H statement for $\tanh$ and sufficiently small-$\sigma$ GELU, $r=0$ is equivalent to feature and feature-kernel evolution, while $r>0$ is equivalent to kernel-regime dynamics with fixed features. The maximal-update parametrization $\mu$P is the stable parametrization that makes every layer update maximal in the paper's precise sense. Thus TP IV rigorously establishes that suitable infinite-width limits exhibit nonlazy feature learning and gives a mechanical procedure for computing their fixed-program laws.

For the displayed MLP convention, the maximal-update exponents are

$$
c=0,\qquad b_\ell=\frac12,\qquad
a_1=-\frac12,\quad
a_2=\cdots=a_L=0,\quad
a_{L+1}=\frac12.
$$

Under Theorem 6.1's local hypothesis that $\phi'$ is pseudo-Lipschitz, it also gives an exact deterministic law recursion for the one-hidden-layer $\mu$P network at every SGD step $t$ fixed independently of width. In the paper's notation its output has the form

$$
\bar f_t(\xi)
=
\mathbb E\!\left[Z_{nV_t}Z_{x_t(\xi)}\right],
$$

with a closed recursion for the joint scalar coordinate variables. This is already an exact shallow law-valued closure. It is not, by itself, the continuous-time Wasserstein transport derivation mentioned in §4.2, nor the explicit single-hidden-layer quadratic moment reduction that is absent from the project corpus.

The proof architecture is:

1. compile the entire finite training computation, including every $W/W^\top$ reuse, as one tensor program;
2. recursively assign each vector a limiting scalar random variable, covariance data, and the deterministic correction caused by correlated transpose reuse;
3. apply the master theorem to all empirical moments and scalar outputs of that fixed program.

Consequently, TP IV already addresses:

- nonlazy infinite-width feature learning;
- ordinary deep dense matrix reuse, including correlations between a matrix and its transpose;
- almost-sure deterministic limits of scalar outputs and empirical coordinate statistics at each fixed program length;
- architecture-level bookkeeping for broad classes of neural computations.

Thus the project cannot claim novelty from any of the following statements alone:

$$
\text{“the infinite-width trajectory is deterministic,”}
$$

$$
\text{“the limit learns features,”}
$$

or

$$
\text{“the limit can be generated recursively.”}
$$

TP IV is naturally a **computation-unrolling** description. Each additional gradient step appends program variables and covariance relations. Section 8 observes that, in a deep nonlinear MLP, a new Gaussian variable associated with $W^\ell(0)x^\ell_t$ is generally required at each step and its covariance with earlier variables must be retained, producing $\Omega(t^2)$ bookkeeping. For polynomial activations, nested nonlinearities can make the Gaussian polynomial degree grow as $\Omega(2^t)$, so direct Isserlis expansion can be super-exponential; for general nonlinearities, the required Gaussian expectations need not have closed form. These are complexity statements about the paper's displayed exact evaluator, not an impossibility theorem for every compression or implementation.

The time quantifier is equally important. TP IV explicitly treats training time independent of width. Its master theorem applies to each fixed finite compiled program; it does not supply a width-uniform, arbitrarily long training theorem or a horizon-independent finite Markov state.

[Tensor Programs VI](https://arxiv.org/abs/2310.02244) studies the ordered limit $n\to\infty$ and then $L\to\infty$ for residual networks, so that limit order by itself is not new. Its general one-layer-block model is

$$
x^\ell=x^{\ell-1}
+L^{-\alpha}\operatorname{MS}\!\left(\varphi(W^\ell x^{\ell-1})\right),
$$

with widthwise $\mu$P scaling and a depth-dependent hidden-weight update of effective size $n^{-1}L^{-\gamma}$. Mean subtraction is part of the stated nonlinear setup. The paper classifies stability, nontriviality, faithfulness, feature learning, and a feature-diversity exponent. Its central Depth-$\mu$P claim selects $\alpha=\gamma=1/2$ as the unique member of that family simultaneously having all of those properties with maximal diversity; $\alpha>1/2$ produces smoother, redundant depth features in the paper's sense.

Here $\gamma$ describes the normalized-gradient update convention, not an isolated raw SGD learning-rate exponent. At $\alpha=\gamma=1/2$, the branch derivative already contributes $L^{-1/2}$, so the paper's scalar SGD learning rate is $O(1)$; its Adam prescription scales as $L^{-1/2}$. This distinction prevents an erroneous comparison with the canonical Euclidean-gradient rates in Chapter 6.

The rigor level must be stated exactly. Section 7 deliberately labels the general nonlinear classification as **claims** and says its Appendix-F arguments are heuristic subject to nontrivial technical conditions. Appendix E's Claim E.1 likewise proposes the nonlinear Gaussian-process limit without a proof or a complete definition of the required smoothness. The paper's rigorous depth-limit work is concentrated in the linear residual setting: Section 4/Appendix C gives a recursive $\Gamma/C$ covariance-response system and a dyadic-depth Cauchy argument leading to a Gaussian continuous-depth process. Even there, the main text assumes a sufficiently well-behaved fixed-point solution where the complete existence argument is omitted. The nonlinear classification is therefore important primary evidence and proof architecture, but not a fully proved theorem that can be imported without qualification.

TP VI also studies a different architecture/scaling family from the canonical model below: its optimal branch is $L^{-1/2}$ with mean subtraction and its associated update scaling, whereas the project asks about a particular $L^{-1}$ Euclidean-gradient residual model with its own hidden learning-rate convention. TP VI does not establish a finite current-state PDE, compact-time Galerkin convergence, dense-restart sufficiency, or an all-time closure theorem for that model.

The additional theorem sought here is:

> The growing TP computation admits, on the declared standard model class, an architecture-derived finite current-state realization whose approximation error can be made arbitrarily small, with a state type independent of the elapsed training horizon.

That is a realization/compression theorem **about** the TP-described limit. It is not a competing derivation of the same fixed-horizon limit, and it is not an impossibility claim about the TP formalism.

**External-source basis.** Yang and Hu, *Feature Learning in Infinite-Width Neural Networks*, Theorem 6.1, Definition 7.1, Theorem 7.4, Theorems 3.3–3.8, Definition 5.1, Theorem 5.6, Theorem H.13, and §8. Yang, Yu, Zhu, and Hayou, *Tensor Programs VI: Feature Learning in Infinite-Depth Neural Networks*, §§4, 6–7, Table 1, and Appendices C–F, especially the rigor qualification preceding Definition 7.1 and Claim E.1.

**Project provenance.** `positioning_roadmap_dmft_tp.tex`, “Target II: low-order long-horizon closure” and “Position relative to TP/DMFT”; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§1, 13, and 16.

### 1.3 What DMFT already provides

[Bordelon and Pehlevan’s self-consistent DMFT](https://arxiv.org/abs/2205.09653) starts from a fixed-depth fully connected network

$$
h_{\mu}^{\ell+1}
=\frac1{\sqrt N}W^\ell\phi(h_\mu^\ell),
\qquad
f_\mu
=\frac1{\gamma\sqrt N}w^L\!\cdot\phi(h_\mu^L),
$$

with unit-variance Gaussian parameters and gradient flow $\dot\theta=-\gamma^2\nabla_\theta\mathcal L$. The rich-limit scaling holds $\gamma_0=\gamma/\sqrt N=O_N(1)$ as $N\to\infty$; the limit $\gamma_0\to0$ gives the lazy NTK regime, while the paper identifies its unit-strength dynamics $\gamma_0=1$ with the $\mu$P stochastic process.

For each hidden layer it tracks the deterministic two-training-time feature and gradient kernels

$$
\Phi^\ell_{\mu\nu}(t,\tau),
\qquad
G^\ell_{\mu\nu}(t,\tau),
$$

together with response objects $A^\ell_{\mu\nu}(t,\tau)$ and $B^\ell_{\mu\nu}(t,\tau)$. These determine Gaussian effective fields and causal Volterra equations whose time integrals run over the history $0\le \tau\le t$. At the corresponding feature-learning strength, their DMFT recovers the stochastic process obtained from TP.

More explicitly,

$$
\Phi^\ell_{\mu\nu}(t,\tau)
=
\lim_{N\to\infty}\frac1N
\phi(h_\mu^\ell(t))\!\cdot\phi(h_\nu^\ell(\tau)),
\qquad
G^\ell_{\mu\nu}(t,\tau)
=
\lim_{N\to\infty}\frac1N
g_\mu^\ell(t)\!\cdot g_\nu^\ell(\tau).
$$

They determine the evolving tangent kernel

$$
K_{\mu\nu}(t,\tau)
=
\sum_{\ell=0}^{L}
G^{\ell+1}_{\mu\nu}(t,\tau)
\,\Phi^\ell_{\mu\nu}(t,\tau)
$$

and therefore the output dynamics through the diagonal $K(t,t)$. Conditional on the kernels, the single-site fields are driven by centered Gaussian processes

$$
u^\ell\sim\operatorname{GP}(0,\Phi^{\ell-1}),
\qquad
r^\ell\sim\operatorname{GP}(0,G^{\ell+1}),
$$

but are not merely Gaussian: the actual preactivation and backward fields satisfy causal Volterra equations of the schematic form

$$
h^\ell(t)
=u^\ell(t)
+\gamma_0\int_0^t
\bigl[A^{\ell-1}(t,\tau)+\Delta(\tau)\Phi^{\ell-1}(t,\tau)\bigr]
\,z^{\ell-1}(\tau)\phi'(h^{\ell-1}(\tau))\,d\tau,
$$

$$
z^\ell(t)
=r^\ell(t)
+\gamma_0\int_0^t
\bigl[B^\ell(t,\tau)+\Delta(\tau)G^{\ell+1}(t,\tau)\bigr]
\,\phi(h^{\ell+1}(\tau))\,d\tau,
$$

with sample-index sums suppressed. The response kernels are functional derivatives of the forward and backward fields with respect to the reciprocal Gaussian drives. More precisely, in the paper's normalization,

$$
A^\ell_{\mu\nu}(t,\tau)
=
\gamma_0^{-1}
\mathbb E\!\left[
\frac{\delta\phi(h^\ell_\mu(t))}
     {\delta r^\ell_\nu(\tau)}
\right],
\qquad
B^\ell_{\mu\nu}(t,\tau)
=
\gamma_0^{-1}
\mathbb E\!\left[
\frac{\delta g^{\ell+1}_\mu(t)}
     {\delta u^{\ell+1}_\nu(\tau)}
\right].
$$

They are the explicit Onsager corrections created by coupling feedforward and feedback signals through the same initialized disorder.

The derivation proceeds by:

1. separating the initial matrices from their gradient updates and introducing forward/backward random fields;
2. writing a moment-generating path integral and enforcing those field definitions with delta-function representations;
3. integrating the Gaussian initialization and introducing the two-time order parameters and their conjugates;
4. taking a large-$N$ stationary-action saddle and imposing self-consistency between the effective stochastic processes, kernels, and responses.

DMFT therefore already supplies:

- a deterministic macroscopic description of rich feature learning;
- hidden-feature and gradient laws, not merely loss;
- two-time covariance kernels;
- reciprocal functional-response terms generated by reused disorder;
- a self-consistent account of forward/backward coupling and the evolving tangent kernel.

The project should not describe DMFT as “infinite” merely because it uses integrals while calling the candidate PDE “finite” despite its own integrals. Both are continuum field theories. DMFT has finitely many **kernel species**, but each species is a function on a two-time domain. On a grid of $T$ training times for $P$ samples, each kernel is a $PT\times PT$ object; Table 1 reports $O(P^2T^2)$ full-DMFT kernel memory and $O(P^3T^3)$ kernel time in that implementation.

The finite-PDE candidate also uses nontrivial integrals:

- integration over the immutable source law $\mu(d\theta)$;
- integration over a finite-dimensional row-coordinate law $\rho^\theta(dw)$;
- integration or evolution in the physical depth variable $s$.

The proposed advance is therefore not “integrals versus no integrals,” “finite species versus infinite species,” or even an unconditional claim of lower numerical cost. The distinction is the **training-time geometry of the state**:

| Property                               | Native TP IV/VI description                                                | Native DMFT description                                    | Sought PDE theorem                                |
|----------------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------|---------------------------------------------------|
| Feature learning                       | Yes                                                                        | Yes                                                        | Yes                                               |
| Deterministic macroscopic observables  | Yes                                                                        | Yes                                                        | Yes                                               |
| Reused $W/W^\top$ correlations         | Program corrections; covariance/response fields in the depth theory        | Response/Onsager kernels                                   | Reconstructed from current PDE state              |
| Training-time domain in the state      | TP IV program grows with steps; TP VI retains two-time response information | Two-time causal triangle grows with horizon                | One current-time slice on fixed source domains    |
| Restart at $t_*$                       | Native representation carries the relevant unrolled/response state          | Native representation carries accumulated kernels/history | Same current-state equations determine the future |
| Approximation order                    | Not a finite-realization theorem by itself                                 | Not a finite-realization theorem by itself                 | Explicit architecture-local hierarchy             |
| Horizon-independent arbitrary accuracy | Not implied                                                                | Not implied                                                | Required in the strongest conjecture              |

An exact DMFT may be the most natural starting point for proving the conjecture. One possible route is to prove that its causal kernels admit a stable finite realization—through finitely many response modes, rational memory approximants, or another architecture-derived state. If that route succeeds, the PDE theorem would be a compression theorem **derived from DMFT**, not a repudiation of it.

**Status.** The cited DMFT gives a self-consistent feature-learning field theory for its stated wide-network setting, with training horizon and sample count $t,P=O_N(1)$ as $N\to\infty$, and explicitly exhibits the two-time/response structure. The authors state that the method is not fully rigorous and relies on heuristic physics techniques. It is therefore a formal saddle-point identification supported by derivation and numerical agreement, not a mathematical convergence theorem. The exact fixed-$L$ causal width theorem and trained $L\to\infty$ homogenization for the project’s canonical $L^{-1}$ residual model remain open.

**External-source basis.** Bordelon and Pehlevan, *Self-Consistent Dynamical Field Theory of Kernel Evolution in Wide Neural Networks*, equations (1)–(3), §§3–4, Appendix N.6, and Table 1; especially equations (9)–(10), the response definitions following them, and the paper’s explicit rigor qualification in §7.

**Project provenance.** `dense_euclidean_continuous_depth_npde_audit.md`, §§3.2, 4.2–4.4; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§13–16; `positioning_roadmap_dmft_tp.tex`, “Target II.”

### 1.4 Why dense training naturally produces history

The obstruction is already visible before taking any limit. Here $h_q^\ell$ is the hidden feature of sample $q$ at layer $\ell$, $e_q=f_q-y_q$ is its residual, $p_q^{\ell+1}$ is the unit-output adjoint, $D_q^\ell=\operatorname{diag}\sigma'(W_\ell h_q^\ell)$, and $\beta_q^\ell=D_q^\ell p_q^{\ell+1}$. For each residual block,

$$
\dot W_\ell(t)
=
-\frac{\gamma}{n}
\sum_{q=1}^m
e_q(t)\,
\beta_q^\ell(t)
h_q^\ell(t)^\top.
$$

Therefore

$$
W_\ell(t)
=
W_\ell(0)
-\frac{\gamma}{n}
\sum_q
\int_0^t
e_q(\tau)\,
\beta_q^\ell(\tau)
h_q^\ell(\tau)^\top
d\tau.
\tag{1.2}
$$

Define the two-time correlations

$$
C^{h,\ell}_{qr}(\tau,t)
=
\frac1n
h_q^\ell(\tau)^\top h_r^\ell(t),
$$

$$
C^{\beta,\ell}_{qr}(\tau,t)
=
\frac1n
\beta_q^\ell(\tau)^\top\beta_r^\ell(t).
$$

Multiplying (1.2) in the two orientations gives the exact identities

$$
\begin{aligned}
W_\ell(t)h_r^\ell(t)
={}&
W_\ell(0)h_r^\ell(t)\\
&-\gamma\sum_q\int_0^t
e_q(\tau)
C^{h,\ell}_{qr}(\tau,t)
\beta_q^\ell(\tau)\,d\tau,
\end{aligned}
\tag{1.3}
$$

$$
\begin{aligned}
W_\ell(t)^\top\beta_r^\ell(t)
={}&
W_\ell(0)^\top\beta_r^\ell(t)\\
&-\gamma\sum_q\int_0^t
e_q(\tau)
C^{\beta,\ell}_{qr}(\tau,t)
h_q^\ell(\tau)\,d\tau.
\end{aligned}
\tag{1.4}
$$

Equations (1.3)–(1.4) show why “just evolve the current Gram matrices” is not an exact derivation. Eliminating the trained matrix creates two-time memory. The initial matrix is also reused in forward and transposed directions, so its conditional law given the generated features generally acquires a nonzero mean. In DMFT language, this is the reciprocal response or Onsager term. Replacing $W^\top$ by an independent Gaussian copy deletes that term and in general changes the dynamics.

The desired PDE theorem would show that the information in (1.3)–(1.4) that matters for $(f,G^h)$ can be reconstructed, exactly or approximately, from a finite current causal state. This is the substantive mathematical claim.

**Status \[proved at finite $n,L$\].** Equations (1.2)–(1.4) are exact.

**Status \[open\].** Finite causal sufficiency for the ordered dense limit is unproved.

**Project provenance.** `dense_euclidean_continuous_depth_npde_audit.md`, §4.2; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§13.1 and 14; `dense_euclidean_continuous_depth_pde_conjecture(1).md`, §§4–5.

### 1.5 What would make the result landmark

The phrase “landmark” is justified only for a theorem that crosses a boundary not already crossed by deterministic TP/DMFT limits. The relevant boundary is finite causal realization.

First, the restart-robust version would prove a **Markovian realization of non-Markovian mean-field dynamics**. The exact dense equations generate Volterra memory and reciprocal response. An autonomous surrogate accurate only from the canonical start is already a nontrivial compression theorem; identifying its state with a finite current sufficient statistic for dense-limit continuation is the stronger restart theorem.

Second, it would give an **architecture-compiled hierarchy with controlled error**. The closure would not be a fitted surrogate for one trajectory. Its basis, state variables, initialization, drift, and readouts would be generated from the architecture and initialization law before positive-time data are observed.

Third, it would cover **representation dynamics**. The target includes the depthwise hidden Gram field, not merely training loss or final outputs. This is essential: many different internal dynamics can produce similar scalar loss.

Fourth, the all-time version would turn fixed-horizon asymptotics into a **uniform dynamical theory**. It would prove that one state complexity works through the active transient, plateau, and arbitrarily late continuation, rather than allowing the state to grow with the history interval.

Fifth, it would create a new mathematical normal form for comparing architectures. Once the dense network is represented by an autonomous macroscopic flow, one can ask about invariant sets, coercivity, stability, bifurcations, and parameter transfer directly in the reduced state.

The significance depends on the rung actually proved:

- An **exact admissible observable closure** would reproduce the declared observables from compiled canonical starts. With a state correspondence and continuation theorem on physically consistent restarts, it would establish a finite causal sufficient state for the deep dense limit.
- An **arbitrary-accuracy compact-time closure** would still go beyond simply deriving TP/DMFT, because it would prove stable finite autonomous approximability from compiled initial states on every finite horizon. Its required order could, however, grow with the horizon.
- An **arbitrary-accuracy all-time closure** with horizon-independent state complexity is the central landmark claim.
- A **pure-Hermite convergence theorem** would provide one explicit witness to the broad claim.
- A **response-enriched convergence theorem** would be equally valid project-level success and could be more faithful to the causal structure.
- A **single accurate low-order PDE** is scientifically useful and empirically nontrivial, but by itself is not a landmark theorem of arbitrary-accuracy closure.

No version should be sold as proving that every PDE solver is computationally cheaper than DMFT. High-dimensional quadrature for a law-valued PDE can be expensive. The theorem-level gain is causal state compression, restartability, and controlled approximation—not an automatic wall-clock guarantee.

**Project provenance.** `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§1, 5, 16, 17, and 19; `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§3, 5, and 8–11.

## Chapter 2 — Research contract, admissibility, and the conjecture lattice

### 2.1 The interesting-regime contract

A positive result counts as a resolution of the central project only if it preserves the regime that creates the deep theoretical difficulty. The following are model requirements, not optional proof conveniences.

| Requirement                | Canonical meaning                                                                      | What it excludes                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| $\mu$P feature learning    | Hidden representations or Grams move by $O(1)$ on $O(1)$ training time                 | NTK, frozen-feature, or vanishing-backbone limits                                       |
| Genuine depth              | At least two hidden transformations; the central residual program takes $L\to\infty$   | The exceptional one-hidden-layer transport PDE                                          |
| Dense architecture         | Fully dense, untied hidden matrices                                                    | Diagonal, low-rank, convolution-only, or tied substitutes                               |
| Dense training             | Input map, readout, and every hidden matrix train                                      | Frozen blocks or random-feature reductions                                              |
| Genuine nonlinearity       | A real nonlinear activation is evaluated in full                                       | Identity/deep-linear substitution                                                       |
| Ordinary optimization      | Euclidean gradient flow with the declared $\mu$P block rates                           | Orthogonal projection, natural gradient, quotient flow, or specially engineered descent |
| Standard initialization    | Independent Gaussian dense matrices at the usual central-limit scale                   | Mean-field-style $n^{-2}$ middle-layer variance or depth-coherent substitution          |
| Correct deep limit         | Width first, depth second                                                              | Silent interchange of $n,L$, or interpolation of iid layers into a smooth $W(s)$        |
| Nontrivial data and loss   | A fixed finite, nondegenerate training set and a standard loss, initially squared loss | A scalar bias or degenerate target that fits alone                                      |
| Representation observables | Outputs and all-depth hidden Grams                                                     | Loss-only playback                                                                      |

For the canonical residual laboratory,

$$
h_r^0=Bx_r,\qquad
h_r^{\ell+1}
=
h_r^\ell+\frac{\gamma}{L}\sigma(W_\ell h_r^\ell),
\qquad
f_r=\frac1n a^\top h_r^L,
$$

with every parameter trained by

$$
\eta_B=n,\qquad
\eta_a=n,\qquad
\eta_{W_\ell}=L.
$$

The principal positive program uses bounded smooth nonlinearities such as $\tanh$. Boundedness is a restriction of the current construction and analytic program, not the philosophical content of “real nonlinearity.” The separate quadratic branch is retained because it is a sharp theorem laboratory, but its one-sample setting, unbounded polynomial features coupled to the Gaussian readout, positive coefficient algebra, and absence of the residual $L\to\infty$ limit make its conclusions model-specific. Gaussian readout initialization alone is not distinctive: the canonical residual model also uses it.

Nonlazy behavior must be checked through representation motion, for example by requiring on at least one nondegenerate target in $\mathcal U$ that

$$
\sup_{t\le T}\sup_{s\in[0,1]}
\|G^h(s,t)-G^h(s,0)\|_F
$$

remain bounded below by a positive constant in the ordered limit. Merely assigning $\mu$P learning-rate exponents does not prove that a chosen task actually exhibits feature motion.

The one-hidden-layer case is excluded from the central claim because its parameter distribution is already a natural current transport state. The project asks whether an analogous finite causal state survives the repeated dense $W/W^\top$ reuse of genuine depth.

**Project provenance.** `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§1–3; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§2–3 and §11.4; `dense_euclidean_continuous_depth_npde_audit.md`, §§2–3.

### 2.2 The canonical target and approximation topology

Fix $m,d$ and the activation $\sigma$. Type the static parameter as

$$
\vartheta=(X,y,\sigma_w,A,\gamma),
\qquad
X=[x_1\ \cdots\ x_m]\in\mathbb R^{d\times m}.
$$

Let $\mathcal U$ be an explicitly declared compact subset of this finite-dimensional parameter space. In particular, its definition must give finite bounds on $\|X\|_F$ and $\|y\|_2$, place the positive scalars $\sigma_w,A,\gamma$ in compact intervals bounded away from zero, and state any data nondegeneracy condition used by a theorem. The canonical $m=d=3$ project contract is the concrete set

$$
\boxed{
\mathcal U=
\left\{
(X,y,\sigma_w,A,\gamma):
\begin{array}{l}
\|X^\top X-I_3\|_{\mathrm{op}}\le0.05,\\
\|y-y_\ast\|_2\le0.05,\\
|\sigma_w-0.65|\le0.05,\\
|A-1|\le0.05,\\
|\gamma-1|\le0.05
\end{array}
\right\},
}
$$

where

$$
m=d=3,\qquad
X_\ast=I_3,\qquad
y_\ast=(0.8,-0.55,0.35),
\qquad
\sigma_w=0.65,\quad A=\gamma=1.
$$

This near-orthogonal compact class is not claimed to be maximally general. Its role is to prevent a closure from memorizing a single target trajectory and to make all constants and quantifiers explicit. A theorem for another class must declare that class rather than silently reusing the symbol $\mathcal U$.

At finite $L$, regard the layerwise Gram sequence as its piecewise-linear interpolation on $[0,1]$. For each $\vartheta\in\mathcal U$, the canonical target is the ordered limit

$$
\mathcal O_\vartheta
=
\lim_{L\to\infty}\lim_{n\to\infty}
\mathcal O_{n,L}^\vartheta
$$

in the topology

$$
C\!\left(
[0,T];
\mathbb R^m
\times
C([0,1];\mathbb S^m)
\right)
$$

for each $T<\infty$, with metric $d_{\mathrm{obs}}$ from §1.1. Existence and uniqueness of this ordered trained limit are part of the conjecture, not a theorem silently assumed in its statement.

The continuity in normalized depth $s$, and convergence uniformly in $s$ and $t$ on compact training intervals, are therefore substantive target hypotheses. If the trained depth limit exists only as a measurable Young measure, in a weak topology, or after subsequence extraction, then the target space and error metric must be changed explicitly; the pointwise notation in §1.1 cannot be used to assume this regularity for free.

The minimal observable set is $(f,G^h)$. Loss is a function of $f$. The tangent kernel $\Theta$, adjoint Grams, and response observables are valuable strengthening targets and may be indispensable proof variables, but failure to approximate them should not automatically refute a conjecture whose declared output is only $(f,G^h)$.

Observable convergence is weaker than full-state convergence. It does not imply restartability. A closure can match one output curve from $t=0$ while omitting state information needed after a perturbation or positive-time restart. Therefore the central claim combines:

1.  observable accuracy from canonical initial data; and
2.  autonomy of the surrogate’s own current state.

A stronger restart-robust theorem additionally compares the surrogate to a declared neighborhood of physically consistent dense-limit states.

**Project provenance.** `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§1.1, 2.2, 3, and 5; `dense_euclidean_continuous_depth_npde_audit.md`, §§8.1–8.2.

### 2.3 Admissible finite PDEs

Let $\mathfrak A$ denote a predeclared compiler class. An approximation family $\{\mathsf P_k\}$ is admissible relative to $\mathfrak A$ only if all of the following hold.

1.  **Finite source and field lists.** At each $k$, the compiler emits finitely many fields on declared finite-dimensional domains. A conditional probability law is allowed, but no field may carry an undeclared infinite coefficient sequence.
2.  **Architecture-local provenance.** Initialization, drift, boundary equations, and readouts are computed from the architecture, activation, Gaussian initialization law, current PDE moments, and static parameters.
3.  **No microscopic state.** There is no $n\times n$ matrix, width-indexed vector, finite-network checkpoint, or source dimension that grows with $n$.
4.  **No trajectory oracle.** Positive-time dense outputs, Grams, kernels, hitting times, fitted constants, and trajectory-trained bases are forbidden, as is any subroutine whose definition is mathematically equivalent to first solving for the future target trajectory and then encoding it.
5.  **Predeclared approximation order.** The basis and hierarchy schedule are fixed before positive-time target data are observed.
6.  **Autonomy.** The current state determines the future under the same equations.
7.  **Internal restartability.** Restarting from an admissible reached PDE state does not require the past trajectory, an absolute-time playback clock, or recomputed target data. This clause does not, by itself, provide a state map from arbitrary dense-limit restarts.
8.  **Direct readouts.** Outputs and hidden Grams are current moments or declared local functionals of the state, not separately fitted decoders.
9.  **Correct limit semantics.** Projection is applied to the limiting operator/law representation after the width limit; it is not a low-rank replacement of the finite dense matrix.
10. **Uniformity over $\mathcal U$.** One family works over the declared model class. Coefficients may depend on the current $\vartheta$, but the grammar and ordering do not change after observing its trajectory.
11. **Finite description and no unbounded encoding.** At each fixed $k$, every emitted coefficient, source law, and operation belongs to a predeclared computable regular class with a finite description. No real coordinate or coefficient may encode an unbounded bit string, target trajectory, or training history. This requirement does not demand a computable accuracy-to-cutoff map, which is the separate stronger “effective closure” rung.

These clauses are necessary semantic filters, not by themselves a complete formal programming-language grammar. A universal existence or no-go theorem must quantify over an explicitly formalized choice of $\mathfrak A$—for example, a stated algebra of local architecture-derived operations and regular coefficients. The operator–Hermite hierarchy in Chapter 6 is one explicit family. The broad conjecture remains relative to the declared admissible compiler class until such a universal grammar is fixed.

The clauses exclude several formally finite but scientifically vacuous constructions. For any continuous scalar curve, one can use a compactifying clock, approximate the curve by a Bernstein polynomial, and pack the result into a two-state ODE or one-source PDE. One can also encode an arbitrary finite ODE in the finite jet of a single scalar source field. Therefore:

$$
\text{“one source”}+\text{“finite state”}
$$

has no closure content without provenance, regularity, uniformity, and restart requirements.

An admissible “single source” means a finite-dimensional immutable random label generated by the initialization—possibly a vector such as

$$
\theta=(B_i(0),a_i(0)/A)\in\mathbb R^{d+1},
$$

not literally one scalar capable of arbitrary-precision encoding. Its current conditional law may be part of the state, but it cannot contain future samples or a hidden history function.

**Project provenance.** `adversarial_audit_report(1).md`, §§1–3; `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §3; `dense_euclidean_continuous_depth_npde_audit.md`, §§8.3–10.

### 2.4 Error notation and well-posedness convention

For every family and horizon $T\in(0,\infty]$, set

$$
E_k(T)
=
\sup_{\vartheta\in\mathcal U}
\sup_{0\le t\le T}
d_{\mathrm{obs}}
\left(
\mathcal O_\vartheta(t),
\mathcal O_{\mathsf P_k,\vartheta}(t)
\right).
\tag{2.1}
$$

Use the convention

$$
E_k(T)=\infty
$$

if the ordered target does not exist uniquely on $[0,T]$, the finite PDE lacks a unique solution on that interval from its compiled initialization, or the declared readouts are undefined. This prevents an approximation claim from hiding its well-posedness obligations.

For $T=\infty$, this convention requires one compatible unique target trajectory and one unique PDE trajectory on every finite interval, both extendible for all $t\ge0$; compact-time existence alone does not make $E_k(\infty)$ finite.

For a particular Hermite family, use $E_{r_{\mathrm H}}^{\mathrm H}(T)$, where $r_{\mathrm H}$ is maximum total source-Hermite degree. This avoids collision with the sample index $r$. For a response-enriched family, use

$$
E_{r_{\mathrm H},K,J,N}^{\mathrm{HR}}(T),
$$

where:

- $r_{\mathrm H}$ is source-Hermite degree;
- $K$ is chronological response grade;
- $J$ is nonlinear differentiation/tree grade;
- $N$ is depth or numerical approximation grade.

The family, not merely the selected index, must be predeclared.

### 2.5 The conjecture lattice

The phrase “the PDE conjecture” refers to several inequivalent statements. They should be separated as follows.

| Label                                             | Formal statement                                                                                                                                                                             | Present status                                                                    |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Ordered-target existence                          | For every $\vartheta\in\mathcal U$, the width-first, depth-second observable limit exists uniquely on compact training intervals                                                             | **Open**                                                                          |
| Finite-cutoff internal equations                  | The displayed operator-Hermite PDE and its forward/transpose pairing, projected-gradient identity, PSD kernel, and dissipation identity hold wherever a sufficiently regular solution exists | **Equations and algebraic identities proved; general global well-posedness open** |
| Practical low-order surrogate                     | A fixed small $k_0$ has low error on a declared finite test suite                                                                                                                            | **Empirically supported**, not an arbitrary-accuracy theorem                      |
| Exact admissible observable closure               | $\exists k<\infty$ such that $E_k(\infty)=0$ from the compiled canonical initializations                                                                                                     | **Open**; this alone is not dense-restart equivalence                             |
| Exact admissible single-source observable closure | Exact observable closure holds in an admissible state built from a finite immutable initialization label and its current law, without extra response/history coordinates                     | **Open**; naive one-time marginals are obstructed                                 |
| Compact-time approximate single-source closure    | For the predeclared admissible single-source family, $\forall T<\infty,\ \inf_k E_k(T)=0$                                                                                                    | **Open**                                                                          |
| All-time approximate single-source closure        | For that family, $\inf_kE_k(\infty)=0$                                                                                                                                                       | **Open**                                                                          |
| Compact-time approximate closure                  | $\forall T<\infty,\ \forall\varepsilon>0,\ \exists k(\varepsilon,T)<\infty:\ E_k(T)<\varepsilon$                                                                                             | **Open**; principal near-term target                                              |
| All-time approximate closure                      | $\forall\varepsilon>0,\ \exists k(\varepsilon)<\infty:\ E_k(\infty)<\varepsilon$                                                                                                             | **Open**; central broad conjecture                                                |
| Pure-Hermite witness                              | $\inf_{r_{\mathrm H}} E_{r_{\mathrm H}}^{\mathrm H}(\infty)=0$                                                                                                                               | **Open**                                                                          |
| Canonical Hermite convergence                     | $\lim_{r_{\mathrm H}\to\infty}E_{r_{\mathrm H}}^{\mathrm H}(\infty)=0$ along the complete parity-correct sequence                                                                            | **Open and stronger** than the witness statement                                  |
| Compact-time Hermite convergence                  | $\forall T<\infty,\ \lim_{r_{\mathrm H}\to\infty}E_{r_{\mathrm H}}^{\mathrm H}(T)=0$, first to an infinite operator flow and then to the dense target                                        | **Open**                                                                          |
| Ordered-limit identification                      | The infinite operator flow equals the ordered dense observable limit on compact intervals                                                                                                    | **Open**                                                                          |
| Compact-time response-enriched witness            | For every $T<\infty$, along a fixed diagonal $(r_{\mathrm H,\ell},K_\ell,J_\ell,N_\ell)$, $E^{\mathrm{HR}}_{r_{\mathrm H,\ell},K_\ell,J_\ell,N_\ell}(T)\to0$                                 | **Open**; leading near-term fallback                                              |
| All-time response-enriched witness                | Along one fixed diagonal, $E^{\mathrm{HR}}_{r_{\mathrm H,\ell},K_\ell,J_\ell,N_\ell}(\infty)\to0$                                                                                            | **Open**; would prove the broad all-time claim                                    |
| Effective closure                                 | A computable map $(\varepsilon,T)\mapsto k$, or $\varepsilon\mapsto k$ all-time, comes with a proved error bound                                                                             | **Open and stronger**                                                             |
| Certified restart-robust closure                  | The same finite template has a residual certificate and remains accurate from a declared compact neighborhood of physically consistent restart states                                        | **Open and stronger**                                                             |
| Direct finite-network consistency                 | The finite PDE is controlled against finite $n,L$ in the ordered limit, not only against an assumed target                                                                                   | **Open and stronger**                                                             |

The broad all-time conjecture is

$$
\boxed{\inf_k E_k(\infty)=0.}
\tag{2.2}
$$

The pure-Hermite witness is

$$
\boxed{\inf_{r_{\mathrm H}} E_{r_{\mathrm H}}^{\mathrm H}(\infty)=0,}
\tag{2.3}
$$

whereas the canonical Galerkin statement is

$$
\boxed{\lim_{r_{\mathrm H}\to\infty}E_{r_{\mathrm H}}^{\mathrm H}(\infty)=0.}
\tag{2.4}
$$

Equation (2.3) allows success at one exact cutoff or along a favorable subsequence. Equation (2.4) requires every sufficiently high complete cutoff to work. Neither follows from the observed accuracy of $r_{\mathrm H}=1$.

For compact-time analysis, it is useful to separate two bridges. Let $\mathcal O_\vartheta^{(\infty)}$ be the observable of a well-posed infinite operator flow. Then internal Galerkin convergence is

$$
\forall T<\infty,\qquad
\lim_{r_{\mathrm H}\to\infty}
\sup_{\vartheta\in\mathcal U}
\sup_{t\le T}
d_{\mathrm{obs}}
\left(
\mathcal O_\vartheta^{(r_{\mathrm H})}(t),
\mathcal O_\vartheta^{(\infty)}(t)
\right)=0,
\tag{2.5}
$$

while identification is

$$
\mathcal O_\vartheta^{(\infty)}(t)
=
\mathcal O_\vartheta(t).
\tag{2.6}
$$

Only (2.5) together with (2.6) yields compact-time Hermite convergence to the dense target.

A direct finite-network strengthening, for a fixed approximation schedule $k_\ell$, has the form

$$
\forall\varepsilon>0,\qquad
\lim_{\ell\to\infty}
\limsup_{L\to\infty}
\limsup_{n\to\infty}
\sup_{\vartheta\in\mathcal U}
\Pr\!\left[
\sup_{t\ge0}
d_{\mathrm{obs}}
\left(
\mathcal O_{n,L}^\vartheta(t),
\mathcal O_{\mathsf P_{k_\ell},\vartheta}(t)
\right)>\varepsilon
\right]=0.
\tag{2.7}
$$

Here the probability is over the declared finite-network initialization (and any declared sampling randomness), while $\vartheta$ contains only the static instance parameters over which uniformity is required. The nested limits retain the required order: $n\to\infty$ first, then $L\to\infty$, then approximation order $\ell\to\infty$. This is stronger than convergence to a separately postulated ordered target.

**Project provenance.** `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§1 and 5; `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§3 and 5; `dense_euclidean_continuous_depth_pde_conjecture(1).md`, §§8.2–8.4.

### 2.6 Logical implications and non-implications

The basic implications are

$$
\text{exact admissible observable closure}
\Longrightarrow
\text{all-time approximate closure}
\Longrightarrow
\text{compact-time approximate closure}.
\tag{2.8}
$$

Here “broad finite-PDE existence” means the corresponding compact-time or all-time observable-approximation statement for at least one predeclared admissible family, according to the horizon attached to the premise. For the explicit all-time witness,

$$
\text{canonical Hermite convergence}
\Longrightarrow
\text{pure-Hermite witness}
\Longrightarrow
\text{broad finite-PDE existence}.
\tag{2.9}
$$

Likewise,

$$
\text{response-enriched convergence}
\Longrightarrow
\text{broad finite-PDE existence}.
\tag{2.10}
$$

The converse implications do not hold. In particular:

- broad existence does not imply that pure Hermites work;
- compact-time convergence does not imply an all-time result;
- internal gradient structure does not imply dense-limit identification;
- empirical low-order accuracy does not imply hierarchy convergence;
- convergence of a hierarchy does not by itself provide a computable cutoff;
- observable agreement from the canonical start does not imply robust restart equivalence.

The key all-time proof pattern is

$$
\text{compact-time consistency and identification}
+
\text{uniform tail stability}
\Longrightarrow
\text{all-time closure}.
\tag{2.11}
$$

Loss dissipation may help with the second term, but does not supply it automatically.

### 2.7 Falsifiers and their logical force

Different negative results attack different rungs.

**Ordered-target falsifier.** If the width-first, depth-second observable limit fails to exist or is nonunique on the declared class, the current formulation of every conjecture using $\mathcal O_\vartheta$ fails. A different stochastic or subsequential target would be a changed research contract.

**Static single-source falsifier.** Suppose two physically consistent restart states have the same complete proposed static source-law state and direct readouts, yet their future $(f,G^h)$ trajectories differ by $O(1)$. This defeats an exact restart-robust static single-source closure. It defeats the canonical-start observable version only if both states are reached within the declared class and the architecture compiler assigns them the same complete PDE state. If the missing datum has a summable response representation, the witness supports response enrichment rather than refuting broad finite-PDE existence.

**Pure-Hermite witness falsifier.** A literal falsifier of (2.3) is a proved bound

$$
\inf_{r_{\mathrm H}} E_{r_{\mathrm H}}^{\mathrm H}(\infty)>0.
$$

A proved failure of the complete cutoff sequence to be Cauchy falsifies canonical convergence (2.4), but need not exclude a favorable subsequence and hence need not falsify (2.3). The following would be serious mechanisms or evidence to investigate, but become theorem-level falsifiers only after they are connected to a positive observable error against the declared target:

- a positive lower bound on observable Cauchy increments along a cofinal odd-degree sequence;
- dynamically reachable energy-bounded states whose mass escapes to arbitrarily high source degree;
- nonuniqueness or unbounded cutoff forced gain in every plausible source-weighted topology;
- a nonvanishing full outgoing residual after all solver and cubature axes are controlled.

Numerical resolution can motivate these statements but cannot prove the required lower bound. None of them, even if proved for the pure family, would by itself refute a response-enriched family.

**All-time uniformity falsifier.** A family may converge on every compact interval while requiring $k\to\infty$ with the horizon. For a specified family, a proved reachable slow tangent-kernel direction in which every finite cutoff incurs an arbitrarily small but cumulatively $O(1)$ late-time error would defeat that family’s horizon-independent claim unless the slow mode is preserved relatively or exactly. Failure of one stability estimate is not a falsifier of every admissible family.

**Broad-existence falsifier.** Relative to a fixed, formally specified compiler class $\mathfrak A$, the logical negation must quantify over the whole admissible class:

$$
\text{for every predeclared }\mathfrak A\text{-admissible family }\{\mathsf P_k\},
\qquad
\inf_kE_k(\infty)>0.
$$

A single positive constant valid uniformly over all admissible families would be a stronger sufficient lower bound. Noncompactness of an ambient memory operator or a nondecaying continuum is not enough by itself, because the physically reachable set or the declared observables may still be compressible. Such a mechanism refutes the broad thesis only if it yields the required observable lower bound—for example through an appropriate lower bound on the relevant reachable-state approximation widths.

**Proof-route falsifier.** Zero radius of a training-time Taylor series, failure of one moment hierarchy, lack of a plain $L^2$ Lipschitz estimate, or failure of one basis defeats only that route unless it establishes a lower bound over the whole admissible class.

The project already contains examples of the last distinction. Conditional on the remaining fixed-order limit bridge (FW), whose forest and width-counting core is now recovered, the raw quadratic Wick-Taylor compiler has been disproved, while the broader real-axis closure question was not settled by that result. Likewise, the earlier claim that the $K/J/N$ prose compiler was already executable is superseded; its exact chronological identities and factorial propagator bound survive.

**Project provenance.** `approximate_single_source_conjecture_resolution(1).md`, §§2, 8–9; `adversarial_audit_report(1).md`, §§1–4; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§11, 13.4, 17, and 20; `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`, §§2 and 4–5.

### 2.8 Current authoritative status

The claim ladder at the start of the project is:

| Claim                                                                            | Status                                                                           |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Exact finite-$(n,L)$ gradients, adjoints, tangent kernel, PSD, and dissipation   | **Proved**                                                                       |
| Explicit finite-cutoff operator-Liouville equations and shared-transpose pairing | **Equations and internal identities proved; general global well-posedness open** |
| Low-order PDE captures active nonlinear representation motion on tested cases    | **Empirically supported**                                                        |
| Pure-Hermite hierarchy converges                                                 | **Open**                                                                         |
| Pure-Hermite hierarchy diverges                                                  | **Not established**                                                              |
| Infinite operator flow equals ordered dense limit                                | **Open**                                                                         |
| Response-enriched finite PDE exists and converges                                | **Open**                                                                         |
| Compact-time arbitrary-accuracy closure                                          | **Open**                                                                         |
| All-time arbitrary-accuracy closure                                              | **Open**                                                                         |
| Fully emitted $K/J/N$ compiler in the earlier response report                    | **Superseded**                                                                   |
| Training-time Wick-Taylor truncation solves the quadratic closure problem        | **Falsified for that stated compiler and model, conditional on (FW)**            |

This ledger is the baseline against which every later chapter should be read.

## Chapter 3 — Exact causal skeleton and the distinct approximation axes

### 3.1 Canonical finite network and notation

Fix $m$ samples $x_1,\ldots,x_m\in\mathbb R^d$, labels $y_1,\ldots,y_m$, width $n$, residual depth $L$, and a smooth activation $\sigma$, acting componentwise on vectors. Let

$$
h_r^0=Bx_r,
\qquad
z_r^\ell=W_\ell h_r^\ell,
$$

$$
h_r^{\ell+1}
=
h_r^\ell+\frac{\gamma}{L}\sigma(z_r^\ell),
\qquad
0\le \ell<L,
\tag{3.1}
$$

$$
f_r=\frac1n a^\top h_r^L,
\qquad
e_r=f_r-y_r,
\qquad
\mathcal L=\frac12\sum_{r=1}^m e_r^2.
\tag{3.2}
$$

Every $W_\ell\in\mathbb R^{n\times n}$ is dense and untied. The input map $B$, readout $a$, and all hidden matrices train. The canonical initialization is independent:

$$
B_{ij}\sim N(0,1),\qquad
a_i\sim N(0,A^2),\qquad
(W_\ell)_{ij}\sim N\!\left(0,\frac{\sigma_w^2}{n}\right).
\tag{3.3}
$$

The Euclidean $\mu$P multipliers are

$$
\eta_B=n,\qquad
\eta_a=n,\qquad
\eta_{W_\ell}=L.
\tag{3.4}
$$

Training time is denoted $t$, while normalized residual depth is $s=\ell/L$. This distinction will be maintained throughout.

### 3.2 Exact adjoint and parameter flow

Define the unit-output adjoint

$$
p_r^L=a,
$$

$$
D_r^\ell
=
\operatorname{diag}\sigma'(z_r^\ell),
\qquad
\beta_r^\ell=D_r^\ell p_r^{\ell+1}.
\tag{3.5}
$$

Backpropagation gives

$$
\boxed{
p_r^\ell
=
\left(
I+\frac{\gamma}{L}W_\ell^\top D_r^\ell
\right)p_r^{\ell+1}.
}
\tag{3.6}
$$

The raw derivative is $\partial f_r/\partial h_r^\ell=p_r^\ell/n$. Confusing it with $p_r^\ell$ creates a spurious factor of $n$.

Direct differentiation of (3.1)–(3.2), followed by the multipliers (3.4), gives

$$
\boxed{
\dot W_\ell
=
-\frac{\gamma}{n}
\sum_{q=1}^m
e_q\,\beta_q^\ell(h_q^\ell)^\top,
}
\tag{3.7}
$$

$$
\boxed{
\dot a=-\sum_qe_qh_q^L,
\qquad
\dot B=-\sum_qe_qp_q^0x_q^\top.
}
\tag{3.8}
$$

These equations are exact for every finite $n,L$. The rank-one hidden update has entries of RMS order $n^{-1}$ but can act coherently with operator norm $O(1)$ on $\sqrt n$-norm feature directions. Entrywise smallness is therefore compatible with $O(1)$ feature learning.

**Status \[proved\].** Equations (3.6)–(3.8) are exact.

**Project provenance.** `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§1.3–1.4; `dense_euclidean_continuous_depth_npde_audit.md`, §§2.1–2.2.

### 3.3 Exact tangent kernel and loss dissipation

For any sample-indexed vector family $u_r^\ell$, define

$$
G_{rq}^{u,\ell}
=
\frac1n(u_r^\ell)^\top u_q^\ell,
\qquad
Q^x_{rq}=x_r^\top x_q.
\tag{3.9}
$$

Differentiating the outputs along (3.7)–(3.8) yields

$$
\boxed{\dot f=-\Theta^{n,L}e,}
\tag{3.10}
$$

with

$$
\boxed{
\Theta^{n,L}_{rq}
=
G^{h,L}_{rq}
+
Q^x_{rq}G^{p,0}_{rq}
+
\frac{\gamma^2}{L}
\sum_{\ell=0}^{L-1}
G^{h,\ell}_{rq}G^{\beta,\ell}_{rq}.
}
\tag{3.11}
$$

The first term is the readout contribution. The second is the input-map contribution and equals the Schur product $Q^x\circ G^{p,0}$. Each hidden term is $G^{h,\ell}\circ G^{\beta,\ell}$. Gram matrices are positive semidefinite, and the Schur product theorem therefore gives

$$
\boxed{\Theta^{n,L}\succeq0.}
\tag{3.12}
$$

Consequently,

$$
\boxed{
\dot{\mathcal L}
=
-e^\top\Theta^{n,L}e
\le0.
}
\tag{3.13}
$$

The same gradient flow gives the inverse-metric energy identity

$$
\boxed{
-\dot{\mathcal L}
=
\frac1n\|\dot a\|_2^2
+
\frac1n\|\dot B\|_F^2
+
\frac1L\sum_{\ell=0}^{L-1}
\|\dot W_\ell\|_F^2.
}
\tag{3.14}
$$

On every finite time interval, (3.14) provides an $L^2$-in-time velocity budget and hence finite parameter travel by Cauchy-Schwarz. It does not provide:

- finite total arclength on $[0,\infty)$;
- a uniform positive lower bound on $\Theta$;
- coercivity in every hidden direction;
- source-Hermite compactness;
- or stability of an approximate kernel near vanishing slow eigenvalues.

Positive semidefiniteness is descent, not all-time error control.

**Status \[proved\].** Equations (3.10)–(3.14) are exact at finite $n,L$.

**Status \[open\].** Any cutoff-uniform kernel gap or all-time stability conclusion.

**Project provenance.** `dense_euclidean_continuous_depth_npde_audit.md`, §§2.3, 5.4–5.5, and 6.5; `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§1.4 and 4.5.

### 3.4 Exact dense-matrix memory

Integrating (3.7) gives

$$
W_\ell(t)
=
W_\ell(0)
-\frac{\gamma}{n}
\sum_q
\int_0^t
e_q(\tau)
\beta_q^\ell(\tau)
h_q^\ell(\tau)^\top
d\tau.
\tag{3.15}
$$

With

$$
C^{h,\ell}_{qr}(\tau,t)
=
\frac1n
h_q^\ell(\tau)^\top h_r^\ell(t),
\qquad
C^{\beta,\ell}_{qr}(\tau,t)
=
\frac1n
\beta_q^\ell(\tau)^\top\beta_r^\ell(t),
\tag{3.16}
$$

one obtains

$$
\boxed{
\begin{aligned}
W_\ell(t)h_r^\ell(t)
={}&W_\ell(0)h_r^\ell(t)\\
&-\gamma\sum_q\int_0^t
e_q(\tau)
C^{h,\ell}_{qr}(\tau,t)
\beta_q^\ell(\tau)\,d\tau,
\end{aligned}
}
\tag{3.17}
$$

$$
\boxed{
\begin{aligned}
W_\ell(t)^\top\beta_r^\ell(t)
={}&W_\ell(0)^\top\beta_r^\ell(t)\\
&-\gamma\sum_q\int_0^t
e_q(\tau)
C^{\beta,\ell}_{qr}(\tau,t)
h_q^\ell(\tau)\,d\tau.
\end{aligned}
}
\tag{3.18}
$$

These are exact finite-network identities. They imply that eliminating $W_\ell$ introduces a two-training-time state. Current one-time Grams do not determine the integrals in (3.17)–(3.18).

A general continuation witness makes this nonclosure concrete. Choose $h,\beta\in\mathbb R^n$ with

$$
h^\top\beta=0,\qquad
\|h\|^2=c^2n,\qquad
\|\beta\|^2=n,
$$

and a matrix $K$ annihilating the currently queried directions. Set

$$
W_0=K,\qquad
W_1=K+\frac1n h\beta^\top.
$$

Then the two states can agree on the current features, adjoints, Grams, $Wh$, and $W^\top\beta$, while

$$
W_1\beta-W_0\beta=h.
$$

Indeed,

$$
(W_1-W_0)h
=
\frac1n h(\beta^\top h)=0,
\qquad
(W_1-W_0)^\top\beta
=
\frac1n\beta(h^\top\beta)=0,
$$

whereas

$$
(W_1-W_0)\beta
=
\frac{\|\beta\|^2}{n}h=h.
$$

With $K$ chosen to annihilate the finitely many currently queried directions, all listed current actions agree, but a future response direction can separate the states by $O(1)$.

This witness has a precise scope. It disproves exact closure by the listed one-time quantities on any restart class containing the witness. It does not prove that both states are reachable from the canonical Gaussian initialization, and it does not disprove response-aware approximation.

**Status \[proved with scope\].** Exact memory identities and the algebraic continuation witness.

**Status \[open\].** Whether the canonical reachable set admits a finite approximate sufficient state.

**Project provenance.** `dense_euclidean_continuous_depth_npde_audit.md`, §§4.2 and 6.1; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§13.1 and 11.1.

### 3.5 Response and Onsager structure

The terms $W_\ell(0)h(t)$ and $W_\ell(0)^\top\beta(t)$ in (3.17)–(3.18) are not fresh Gaussian fields. The current $h(t)$ and $\beta(t)$ were themselves generated using the same initial matrix. Conditioning therefore decomposes each reused action into

$$
\text{conditional mean}
+
\text{centered Gaussian innovation}.
$$

The conditional mean is the Onsager or self-response term. At initialization, a basic row-wise identity is the Gaussian Stein relation

$$
\mathbb E
\left[
W^\top\varphi(Wh)
\mid h
\right]
=
\sigma_w^2
\mathbb E[\varphi'(Z)]\,h
$$

when $W_{ij}\stackrel{\mathrm{iid}}{\sim}N(0,\sigma_w^2/n)$, $h$ is held fixed, $\varphi$ acts componentwise, and $\varphi$ has the integrability and weak differentiability needed for Gaussian integration by parts. The right-hand side is generally nonzero. An independent backward Gaussian copy would return zero conditional mean and is therefore algebraically wrong.

Here $Z\sim N(0,\sigma_w^2\|h\|_n^2)$ and $\|h\|_n^2=n^{-1}\|h\|_2^2$.

An exact fixed-depth DMFT naturally records:

- the tagged forward and backward path laws;
- two-time covariances $C^h,C^\beta$;
- reciprocal functional-response kernels;
- Gaussian cavity innovations;
- the learned memory terms from (3.17)–(3.18).

The central closure problem is to determine whether these objects admit a finite causal realization after the ordered depth limit. The static operator-Hermite proposal attempts to reconstruct the needed transpose response from a current row law. The response-enriched proposal instead promotes any surviving response/history contractions to explicit current coordinates.

These are two candidate realizations of the same causal skeleton, not two different target dynamics.

**Status \[proved for the displayed Gaussian step\].** The Stein conditional-mean identity is exact under its stated regularity and independence hypotheses and shows why an independent transpose copy is wrong in general.

**Status \[formal in the cited DMFT; open for the canonical target\].** The full reciprocal-response field theory is part of the cited formal DMFT. A rigorous fixed-depth derivation for the canonical residual model, its trained depth limit, and identification of the operator-PDE shared transpose with the resulting Onsager mean remain open.

**Project provenance.** `dense_euclidean_continuous_depth_npde_audit.md`, §§4.2–4.4; `dense_euclidean_continuous_depth_pde_conjecture(1).md`, §§5–6.1; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§13–14.

### 3.6 Exact chronological response hierarchy

Continuous residual depth supplies a genuine **chronological-grade decay mechanism**. At this stage the fields remain width-$n$ vectors and retain the dense matrices, so the result is not yet a width-independent finite-PDE compression theorem. Let

$$
v_r^\ell=\partial_t h_r^\ell,
\qquad
A_r^\ell=\gamma D_r^\ell W_\ell,
\qquad
\Delta=\frac1L.
$$

Differentiating (3.1) and substituting (3.7) gives

$$
\boxed{
v_r^{\ell+1}
=
(I+\Delta A_r^\ell)v_r^\ell
+
\Delta F_r^\ell,
}
\tag{3.19}
$$

where

$$
F_r^\ell
=
-\gamma^2
\sum_qe_q
D_r^\ell\beta_q^\ell
G_{qr}^{h,\ell},
\tag{3.20}
$$

and

$$
v_r^0
=
-\sum_qe_qQ^x_{qr}p_q^0.
\tag{3.21}
$$

Separate the residual channels. Define

$$
q_{r\leftarrow q}^{0,0}
=
-Q^x_{qr}p_q^0,
$$

$$
q_{r\leftarrow q}^{0,\ell+1}
=
q_{r\leftarrow q}^{0,\ell}
-\Delta\gamma^2
D_r^\ell\beta_q^\ell
G_{qr}^{h,\ell},
\tag{3.22}
$$

and for $k\ge1$,

$$
q_{r\leftarrow q}^{k,\ell+1}
=
q_{r\leftarrow q}^{k,\ell}
+
\Delta A_r^\ell
q_{r\leftarrow q}^{k-1,\ell},
\qquad
q_{r\leftarrow q}^{k,0}=0.
\tag{3.23}
$$

Then

$$
\boxed{
\partial_t h_r^\ell
=
\sum_qe_q
\sum_{k\ge0}
q_{r\leftarrow q}^{k,\ell}.
}
\tag{3.24}
$$

The index $k$ counts chronologically ordered dense-Jacobian continuations. It is not a training-time derivative order.

The backward velocity $w_r^\ell=\partial_t p_r^\ell$ obeys

$$
\boxed{
w_r^\ell
=
\left(I+\Delta(A_r^\ell)^\top\right)
w_r^{\ell+1}
+
\Delta(\dot A_r^\ell)^\top p_r^{\ell+1},
}
\tag{3.25}
$$

with

$$
w_r^L=\dot a=-\sum_qe_qh_q^L.
$$

Write the residual-linear decomposition

$$
\dot A_r^\ell
=
\sum_q e_q(\dot A_r^\ell)_{\leftarrow q}.
$$

The reversed-orientation response fields are defined by

$$
\boxed{
r_{r\leftarrow q}^{0,\ell}
=
r_{r\leftarrow q}^{0,\ell+1}
+
\Delta
\left((\dot A_r^\ell)_{\leftarrow q}\right)^\top
p_r^{\ell+1},
\qquad
r_{r\leftarrow q}^{0,L}=-h_q^L,
}
\tag{3.25a}
$$

$$
\boxed{
r_{r\leftarrow q}^{k,\ell}
=
r_{r\leftarrow q}^{k,\ell+1}
+
\Delta(A_r^\ell)^\top
r_{r\leftarrow q}^{k-1,\ell+1},
\qquad
r_{r\leftarrow q}^{k,L}=0,\quad k\ge1.
}
\tag{3.25b}
$$

Thus the exact backward expansion is

$$
\partial_t p_r^\ell
=
\sum_qe_q\sum_{k\ge0}
r_{r\leftarrow q}^{k,\ell}.
\tag{3.26}
$$

Fix a finite training horizon $T$, use $\|u\|_n=n^{-1/2}\|u\|_2$, and assume

$$
\Lambda_T
=
\sup_{r,t\le T}
\frac1L\sum_{\ell=0}^{L-1}
\|A_r^\ell(t)\|_{\mathrm{op}}
<\infty.
\tag{3.27}
$$

Define

$$
B_{v,T}
=
\sup_{r,t\le T}
\left(
\|v_r^0(t)\|_n
+
\frac1L\sum_{\ell=0}^{L-1}
\|F_r^\ell(t)\|_n
\right).
\tag{3.27a}
$$

Here is the discrete proof of the factorial estimate. Iterating (3.19) expresses every term of chronological grade $j$ as an ordered product

$$
\Delta^jA_r^{\ell_j}\cdots A_r^{\ell_1},
\qquad
0\le \ell_1<\cdots<\ell_j<\ell,
$$

applied either to the initial source or to one of the injected terms $\Delta F_r^u$. Put

$$
a_\ell=\Delta\|A_r^\ell\|_{\mathrm{op}}\ge0.
$$

The elementary-symmetric-polynomial bound

$$
\sum_{\ell_1<\cdots<\ell_j}
a_{\ell_1}\cdots a_{\ell_j}
\le
\frac1{j!}\left(\sum_\ell a_\ell\right)^j
\le\frac{\Lambda_T^j}{j!}
$$

follows by expanding $(\sum_\ell a_\ell)^j$: every product with distinct indices appears at least $j!$ times. Summing the norms of the initial and injected sources gives exactly the envelope $B_{v,T}$. Therefore

$$
\boxed{
\sup_{r,\ell,t\le T}
\left\|
v_r^\ell-
\sum_qe_q\sum_{k=0}^K
q_{r\leftarrow q}^{k,\ell}
\right\|_n
\le
B_{v,T}
\sum_{j>K}\frac{\Lambda_T^j}{j!}
\le
B_{v,T}e^{\Lambda_T}
\frac{\Lambda_T^{K+1}}{(K+1)!}.
}
\tag{3.28}
$$

For the backward hierarchy with exact differentiated source $\dot A$, define

$$
B_{w,T}
:=
\sup_{r,t\le T}
\left(
\|w_r^L(t)\|_n
+
\frac1L\sum_{\ell=0}^{L-1}
\|(\dot A_r^\ell(t))^\top p_r^{\ell+1}(t)\|_n
\right),
$$

$$
R_K(\Lambda):=\sum_{j>K}\frac{\Lambda^j}{j!}.
$$

$$
\sup_{r,\ell,t\le T}
\left\|
w_r^\ell-
\sum_qe_q\sum_{k=0}^K
r_{r\leftarrow q}^{k,\ell}
\right\|_n
\le
B_{w,T}R_K(\Lambda_T).
\tag{3.28a}
$$

The backward estimate is the same ordered-product argument with the layer order reversed. No commutativity is used.

If $\dot A$ is instead recomputed from a truncated forward velocity, define the additional source-substitution term

$$
E_{A,K,T}
=
\sup_{r,t\le T}
\frac1L\sum_{\ell=0}^{L-1}
\left\|
\left(\dot A_r^\ell-\dot A_{r,K}^\ell\right)^\top
p_r^{\ell+1}
\right\|_n.
\tag{3.28b}
$$

$$
\sup_{r,\ell,t\le T}
\|w_r^\ell-w_{r,K,\mathrm{coupled}}^\ell\|_n
\le
B_{w,T}R_K(\Lambda_T)
+
e^{\Lambda_T}E_{A,K,T}.
\tag{3.29}
$$

For (3.29), subtract the exact-source and coupled recursions. Variation of constants propagates the source mismatch through products bounded by

$$
\prod_{\ell}(1+a_\ell)
\le
\exp\!\left(\sum_\ell a_\ell\right)
\le e^{\Lambda_T},
$$

which yields the additive $e^{\Lambda_T}E_{A,K,T}$ term. The factorial in (3.28) is geometric: it is the discrete analogue of the volume of an ordered simplex in residual depth. It is valid for noncommuting and nonnormal matrices because the proof uses ordered products and operator norms, not eigenvalue diagonalization.

These estimates are pathwise at fixed finite $n,L$ whenever the displayed envelopes are finite. They are uniform in width and depth on $[0,T]$ only under the additional hypothesis

$$
\sup_{n,L}\max\{B_{v,T},B_{w,T},\Lambda_T\}<\infty.
$$

An all-time factorial estimate would require corresponding bounds uniform in $T$.

There is also an exact reason not to compress the full neuron-coordinate propagator by low rank. In continuum depth let

$$
\partial_sJ(s,u)=A(s)J(s,u),
\qquad
J(u,u)=I_n,
$$

and suppose $\|J(s,u)^{-1}\|_{\mathrm{op}}\le e^{C(s,u)}$. Then every singular value of $J(s,u)$ is at least $e^{-C(s,u)}$. By the Eckart--Young theorem, every rank-$R<n$ matrix $\widetilde J_R$ therefore satisfies

$$
\|J(s,u)-\widetilde J_R\|_{\mathrm{op}}
\ge \sigma_{R+1}(J(s,u))
\ge e^{-C(s,u)}.
$$

Thus a width-independent operator-norm low-rank approximation of the complete propagator is impossible under this invertibility bound. A successful closure must compress the finitely queried response contractions or their statistics, not the entire neuron-coordinate map $J$.

This theorem is substantial but limited. It controls the pure chronological propagator tail. It does not control:

- the source-substitution defect $E_{A,K,T}$;
- nonlinear chain-rule branching;
- Gaussian conditional high-to-low contractions;
- truncation of source-label dependence;
- or the existence of a width-independent finite response PDE.

The earlier report’s claim that a complete $K/J/N$ compiler had already been emitted is superseded. Equations (3.19)–(3.29) and their finite-network proof survive intact.

**Status \[proved with hypotheses\].** The prelimit chronological identities and exact-source factorial tail under the displayed finite operator/source envelopes; width/depth uniformity requires their uniform boundedness.

**Status \[open\].** A full response-enriched finite-PDE residual theorem.

**Project provenance.** `dense_euclidean_continuous_depth_pde_conjecture(1).md`, §§5–6 and §12; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§6.6, 13.2–13.4, and 20; `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§6.5 and 8.

### 3.7 The approximation axes are not interchangeable

The project uses several indices that answer different questions.

| Axis                         |                                          Symbol | What it resolves                                                       | What it does not imply                           |
|------------------------------|------------------------------------------------:|------------------------------------------------------------------------|--------------------------------------------------|
| Width                        |                                             $n$ | Law-of-large-numbers/central-limit passage to a macroscopic wide limit | Depth or long-time convergence                   |
| Original residual depth      |                                             $L$ | Homogenization of iid layer types after width                          | Smooth convergence of the raw matrices           |
| Training-time jet order      |                                             $j$ | Derivatives of the flow at one training time                           | Positive-time convergence or source regularity   |
| Source-Hermite degree        | $r_{\mathrm H}$, with $P_{r_{\mathrm H}}$ modes | Dependence on immutable Gaussian neuron labels                         | Chronological memory depth                       |
| Chronological response grade |                                             $K$ | Ordered reuse of dense Jacobians through depth                         | Nonlinear tree closure or Hermite tails          |
| Nonlinear tree grade         |                                             $J$ | Chain-rule and activation-derivative branching                         | Response propagation or numerical depth accuracy |
| PDE depth/numerical grade    |                                             $N$ | Approximation of physical depth fields or solver resolution            | Closure of omitted causal state                  |
| Explicit history grade       |                                 model-dependent | Retained memory or response coordinates used to Markovize the state    | Static-source convergence                        |

Two distinctions are especially important.

First,

$$
\text{source Hermite degree}
\neq
\text{training-time Taylor order}.
$$

Hermite coefficients differentiate with respect to immutable Gaussian source variables. Taylor jets differentiate along the training vector field. The quadratic zero-radius theorem, conditional on (FW), concerns a training-time Wick-Taylor series and does not imply divergence of a source-Hermite Galerkin family.

Second,

$$
\text{source Hermite degree}
\neq
\text{Onsager order}.
$$

An Onsager term is a conditional mean caused by reuse of the same disorder. It can occur at low source degree. A high source Hermite can encode nonlinear dependence on initialization without introducing any additional chronological memory.

The correct fallback is therefore multi-axis:

$$
(r_{\mathrm H},K,J,N),
$$

possibly with a finite explicit history sector. Convergence along one axis cannot be used as evidence for convergence along another without a bridge theorem.

**Project provenance.** `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§12–14; `approximate_single_source_conjecture_resolution(1).md`, §§2 and 9; `dense_euclidean_continuous_depth_pde_conjecture(1).md`, §§5–6.

### 3.8 Energy, compactness, and stability are separate obligations

Let $\mu_\eta$ be the Gaussian source-neuron law and set

$$
H=L^2(\mu_\eta).
$$

Let $\eta$ denote a source-column neuron label and $\xi$ an independent target-row label of the same immutable Gaussian type as in §2.3; let $\omega$ carry the frozen Gaussian row randomness. Set

$$
\mathcal R=L^2(\mu_\xi\otimes\mathbb P_\omega),
\qquad
\mathcal R(H)
=
L^2(\mu_\xi\otimes\mathbb P_\omega;H).
$$

For the operator-Hermite cutoffs, write the Lagrangian learned-row characteristic as

$$
w=\sigma_w\epsilon+c
$$

and denote the trainable input, readout, and learned-row coordinates by $(b_{r_{\mathrm H}},a_{r_{\mathrm H}},c_{r_{\mathrm H}})$ at source cutoff $r_{\mathrm H}$. Wherever a sufficiently regular finite-cutoff solution exists, its projected-gradient structure gives

$$
-\dot{\mathcal L}_{r_{\mathrm H}}
=
\|\dot b_{r_{\mathrm H}}\|_H^2
+
\|\dot a_{r_{\mathrm H}}\|_H^2
+
\int_0^1
\|\dot c_{r_{\mathrm H}}(s)\|_{\mathcal R(H)}^2\,ds.
$$

Thus uniformly bounded initial losses give cutoff-uniform $L^2$-in-time velocity bounds and $1/2$-Hölder time equicontinuity on compact intervals in the natural **trainable Lagrangian** state norm. Uniform state bounds additionally use uniformly bounded initial state norms. Derived forward and adjoint fields require separate depth boundary-value estimates. The energy identity does not prove that such solutions exist globally, nor does it give source-mode compactness.

For the frozen Gaussian row operator, let $W_\omega$ be a standard isonormal process over $H$, and define $I:H\to\mathcal R$ by

$$
(Iu)(\xi,\omega)=W_\omega(u).
$$

Its Hilbert adjoint $T_W=I^\ast:\mathcal R\to H$ is defined by

$$
\langle T_W\beta,u\rangle_H
=
\mathbb E_{\xi,\omega}[\beta W_\omega(u)],
$$

and is bounded:

$$
\|T_W\beta\|_H\le\|\beta\|_{\mathcal R}.
$$

In a Hermite basis $\{\psi_\nu\}$ of $H$, put

$$
\epsilon_\nu(\omega)=W_\omega(\psi_\nu).
$$

Then

$$
T_W\beta
=
\sum_\nu
\psi_\nu\,
\mathbb E_{\xi,\omega}[\epsilon_\nu\beta].
$$

However, $T_W$ is not compact. Taking $\beta_\nu=\epsilon_\nu$ gives

$$
T_W\beta_\nu=\psi_\nu,
$$

so for every finite projection $\Pi_{r_{\mathrm H}}$,

$$
\sup_{\|\beta\|_{\mathcal R}\le1}
\|(\mathrm{Id}_H-\Pi_{r_{\mathrm H}})T_W\beta\|_H=1.
\tag{3.30}
$$

Strong projection convergence is uniform on compact sets, not on the energy-bounded unit ball.

The learned-row adjoint $T_c\beta=\mathbb E_{\xi,\omega}[c\,\beta]$ is bounded when $c\in\mathcal R(H)$, but it must be controlled together with the frozen term. Boundedness of either component does not supply the collective source compactness needed for cutoff convergence.

Plain $L^2$ is also insufficient for the nonlinear adjoint map

$$
(z,p)\mapsto\sigma'(z)p.
$$

Indeed,

$$
\delta\beta
=
\sigma'(z)\delta p
+
\widetilde p\,
\bigl[\sigma'(z)-\sigma'(\widetilde z)\bigr],
$$

and the second term contains $\widetilde p\,\delta z$. Two $L^2$ factors need only have an $L^1$ product. The obstruction is present at initialization because the terminal adjoint $p(1,\theta)=a(\theta)$ is an unbounded Gaussian coordinate.

Therefore a compact-time convergence theorem needs a stronger bundle:

$$
\boxed{
\begin{array}{l}
\text{collective source-tail compactness or propagated weighted regularity,}\\
\text{uniqueness or weak--strong uniqueness,}\\
\text{cutoff-uniform forced stability in a stronger-to-weaker topology.}
\end{array}
}
\tag{3.31}
$$

A Gaussian Sobolev estimate, an $L^4$ product estimate, or a Gaussian-Orlicz bound is a possible route. None has yet been proved uniformly for the full reachable family.

**Status \[proved with stated scope\].** Boundedness and noncompactness of the frozen transpose; insufficiency of plain $L^2$ for the displayed nonlinear product estimate; finite-cutoff energy bounds for sufficiently regular solutions.

**Status \[open\].** Collective source compactness, uniqueness of the infinite operator flow, and cutoff-uniform forced stability.

**Project provenance.** `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`, §§1–2 and §4; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§10 and 15.

### 3.9 What the causal skeleton establishes

The first three chapters leave the project in a precise state.

**Established**

- The finite dense model has exact adjoint, gradient, tangent-kernel, PSD, dissipation, and energy identities.
- Dense training produces exact two-time memory identities.
- Reused $W/W^\top$ actions require conditional response; an independent backward Gaussian copy is incorrect.
- Current Grams and simple one-time marginals are not exact closure variables on unrestricted restart classes.
- The chronological depth-response hierarchy has an exact factorial pure-propagator tail under the displayed finite operator and source envelopes.
- Wherever a sufficiently regular finite-cutoff operator-Hermite solution exists, its equations have the exact internal shared-transpose and projected-gradient identities developed in the residual-model chapter.

**Open**

- Existence and uniqueness of the canonical ordered trained limit.
- Identification of its exact fixed-depth DMFT and trained depth-homogenized Onsager mean.
- Sufficiency of the static source-law state.
- Compact-time convergence of the pure-Hermite hierarchy.
- A fully emitted response-enriched finite PDE.
- The all-time stability upgrade.

**Superseded**

- The claim that deterministic trajectories alone go beyond TP/DMFT.
- The unrestricted “one-source” formulation.
- Smooth interpolation of iid depth matrices into a nondegenerate $W(s)$.
- The claim that the earlier $K/J/N$ response compiler was already executable.
- The inference that fixed-order Wick/Taylor computability implies positive-time convergence.

The remaining chapters can now treat the non-standard regimes, quadratic theorem laboratory, and canonical residual construction without changing the meaning of “closure,” “source,” “response,” “finite,” or “proved.”

## Chapter 4 — Boundary and non-standard regimes

### 4.1 The purpose of the boundary registry

The central conjecture concerns a deep, fully dense, untied, fully trained, genuinely nonlinear network in the Euclidean $\mu$P feature-learning regime. Its proposed closure must be autonomous, non-oracular, restartable, width- and depth-independent at fixed accuracy, and accurate for representation observables rather than loss alone. A result obtained after changing one of these conditions can be mathematically exact and useful without resolving that conjecture.

This chapter records such results by the assumption that they change. Every entry answers four questions:

| Field                 | Meaning                                                        |
|-----------------------|----------------------------------------------------------------|
| Exact result          | What is actually proved or exactly reduced                     |
| Modified qualifier    | Which condition of the central research contract is changed    |
| Why it is not central | Why the result does not resolve the dense deep closure problem |
| Transfer back         | Which identity, obstruction, or proof device remains useful    |

The distinction is substantive. For example, a finite-dimensional law created by imposing a low-rank parameterization is not evidence that an unconstrained dense matrix dynamically becomes low rank. Likewise, a trajectory-fitted reduced model may be predictive, but it does not establish an architecture-derived closure.

The latest project syntheses make the same separation between model assumptions and still-unproved proof hypotheses. They identify the principal model as a bounded-activation, fully dense, untied residual network with Euclidean $\mu$P learning rates and the ordered limit $n\to\infty$ first, $L\to\infty$ second. They also explicitly warn that the quadratic/Gaussian no-go results below are model-specific.

*Provenance:* `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §2.2 “Model assumptions versus proof assumptions,” §3 “What counts as a finite neural PDE,” and §11.4 “Model-specific negative results that must not be overgeneralized”; identical synthesis in `MASTER_NEURAL_PDE_REPORT_WITH_FIGURES.md`, the corresponding §§2.2, 3, and 11.4.

### 4.2 Shallow depth

#### 4.2.1 Boundary statement

A one-hidden-layer mean-field model can often use the empirical law of a single neuron parameter as its macroscopic state. Schematically, for

$$
f_\rho(x)=\int a\,\phi(w\!\cdot x)\,\rho(da,dw),
$$

Euclidean gradient flow leads, when the usual propagation-of-chaos and regularity hypotheses hold, to a transport equation

$$
\partial_t\rho_t+\nabla_{a,w}\!\cdot\bigl(\rho_t V[\rho_t]\bigr)=0.
$$

The state is already a probability law on a fixed finite-dimensional neuron space. There is no learned dense matrix sitting between two trained hidden populations, and therefore no repeated forward/backward use of the same $W$ and $W^\top$ that must be compressed.

This is why the central contract requires at least two hidden layers. Shallow transport structure is a conceptual precedent for a neural PDE, but it does not solve the deep causal-response problem.

| Field                                          | Classification                                                                                                         |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Exact result in the project corpus             | None: the supplied foundational reports do not contain a standalone proof of the generic shallow transport theorem    |
| External result checked for Version 2.1        | TP IV, Theorem 6.1 gives an exact deterministic coordinate-law recursion for a one-hidden-layer $\mu$P network at each fixed discrete SGD step |
| Modified qualifier                             | Genuine depth, specifically the presence of at least two trained hidden layers                                         |
| Why it is not central                          | The hidden-to-hidden dense transpose/reuse mechanism is absent                                                         |
| Transfer back                                  | Empirical-measure transport, direct moment readouts, and gradient-flow dissipation are the right structural precedents |

The schematic transport equation above is contextual mathematical background, not a new theorem claimed by the present project. TP IV supplies the distinct fixed-step law recursion summarized in §1.2. Neither item, as written here, is an explicit continuous-time single-hidden-layer **quadratic** $\mu$P transport derivation or a proof of a smaller finite moment closure; that model-specific result remains absent from the unified notes.

### 4.3 Smooth or depth-coherent matrix processes

#### 4.3.1 Smooth depth is a different model

One audited boundary model makes this assumption explicit. For each fixed width $n$, let $W_n^0(s)$ be a centered continuous Gaussian matrix process, independent of $B$ and $a$, with

$$
\mathbb E[W^0_{ij}(s)W^0_{kl}(u)]
=\frac1n\delta_{ik}\delta_{jl}K_W(s,u),
\qquad
K_W(s,s)=1,
$$

where $K_W$ is a declared continuous positive-semidefinite kernel, and couple the depth discretizations by $W_{\ell,L}^0=W_n^0(\ell/L)$. In the older local convention of that report,

$$
\chi=\sigma=\tanh,\qquad
B_{ij}(0)\sim N(0,d^{-1}),\qquad
a_i(0)\sim N(0,1),
$$

$$
h_q(0,t)=\chi(B(t)x_q),\qquad
f_q(t)=\frac1n a(t)^\top h_q(1,t),\qquad
e_q=f_q-y_q,
$$

and the residual scale is one. At fixed $n$, the $L\to\infty$ equations are

$$
\partial_sh_q(s,t)=\sigma(W(s,t)h_q(s,t)),
$$

$$
-\partial_sp_q(s,t)
=W(s,t)^\top
\operatorname{diag}\sigma'(W(s,t)h_q(s,t))p_q(s,t),
\qquad
p_q(1,t)=a(t),
$$

where

$$
\beta_q(s,t)
=
\operatorname{diag}\sigma'(W(s,t)h_q(s,t))p_q(s,t).
$$

$$
\partial_tW(s,t)
=-\frac1n\sum_qe_q(t)\,
\beta_q(s,t)h_q(s,t)^\top,
$$

with

$$
\dot B
=-\sum_qe_q\,
\operatorname{diag}\chi'(Bx_q)p_q(0)x_q^\top,
\qquad
\dot a=-\sum_qe_qh_q(1).
$$

With

$$
g_q^B=\operatorname{diag}\chi'(Bx_q)p_q(0),
\qquad
G_{qk}^{B}=\frac1n(g_q^B)^\top g_k^B,
$$

the exact continuum tangent kernel of this separate finite-$n$ model is

$$
\Theta_{qk}
=
G_{qk}^h(1)
+
(x_q^\top x_k)G_{qk}^{B}
+
\int_0^1G_{qk}^h(s)G_{qk}^{\beta}(s)\,ds.
$$

These equations use the limit order

$$
L\to\infty\text{ at fixed }n,
\qquad
n\to\infty\text{ second},
$$

which is the reverse of the canonical project target. They are therefore a different model, not a derivation of the iid-depth limit.

More generally, if a depth-indexed path $W(s)$ is postulated with enough regularity, a residual recursion is a consistent discretization of

$$
\partial_s h(s)=\mathcal F\bigl(h(s),W(s)\bigr).
$$

Then continuous-depth analysis may legitimately treat $W(s)$ as a coefficient field and derive a neural-ODE or PDE limit. This assumption is not satisfied merely because the number of iid layers tends to infinity. Raw iid matrices do not become a smooth nondegenerate path under interpolation: adjacent layers remain independent innovations rather than $O(L^{-1})$ increments of one matrix-valued curve.

The canonical dense project therefore takes width first and depth second and seeks homogenization of observables and conditional response laws. It does not interpolate the microscopic matrices themselves.

The corresponding one-seed diagnostic was consistent with convergence of this separate smooth-depth discretization: against an $L=96$ numerical reference, the reported output/Gram grid-maximum errors were respectively

| $L$ | output | Gram |
|---:|---:|---:|
| 12 | $4.87\times10^{-3}$ | $2.34\times10^{-2}$ |
| 24 | $2.08\times10^{-3}$ | $1.02\times10^{-2}$ |
| 48 | $7.01\times10^{-4}$ | $3.44\times10^{-3}$ |

This is one seed and three resolutions, with $L=96$ only a numerical reference. It is not an iid-depth homogenization test or a certified continuum theorem.

| Field                    | Classification                                                                                                                                                    |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exact project conclusion | A smooth interpolation of raw iid depth matrices is not the canonical ordered target                                                                              |
| Modified qualifier       | Iid, untied depth is replaced by a smooth, tied, or coherently correlated depth process                                                                           |
| Why it is not central    | The difficult trained-depth homogenization and surviving conditional/Onsager mean have been assumed away or changed                                               |
| Transfer back            | Continuous-depth adjoints, depth transport, and homogenization templates remain useful after the iid innovations and conditional mean have been derived correctly |

*Provenance:* `dense_euclidean_continuous_depth_npde_audit.md`, §§3.1–3.2 and §§7.3–7.4; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §2.1 “Ordered target,” §11.1 “Established,” and §16.2 “Prelimit-first causal Galerkin”; same sections in `MASTER_NEURAL_PDE_REPORT_WITH_FIGURES.md`.

### 4.4 Normalized and projected geometries

#### 4.4.1 Why normalization is a boundary regime

RMS normalization and direction-only weight normalization change either the architecture map, the parameter-space metric, or both. They are therefore not positive answers for the unnormalized Euclidean model. They are nevertheless important because they test whether the quadratic obstruction is merely radial and whether normalization creates an exact finite moment algebra.

For the two-hidden-layer, one-sample quadratic laboratory, the audited result is:

| Field                                          | RMS after both hidden activations                    | Direction-only weight normalization                                                                                       |
|------------------------------------------------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Exact low-order result                         | The feature-time cubic coefficient changes sign      | Global readout projection changes the cubic coefficient but not the initial kernel                                        |
| Exact natural moment closure                   | No for the displayed frozen RMS reduction            | No for the displayed frozen readout-WN reduction                                                                           |
| Transfer of the raw positive-Wick proof        | No: reciprocal norms and projectors add signed terms | No when the global readout is projected; yes for hidden-only row normalization in the large-fan-in fixed-order convention |
| Zero radius proved for the normalized model    | No                                                   | No for global readout projection                                                                                          |
| Every real-axis finite approximation ruled out | No                                                   | No                                                                                                                        |

The precise vector fields, coefficients, and nonclosure recurrences are given in §5.9. The central logical point is already visible from the new signed terms:

$$
\delta_2
=
\frac{\phi'(z^{(2)})}{s_2}
\odot\bigl(a-fu^{(2)}\bigr)
$$

for final-layer RMS normalization, and

$$
D_+a=h^{(2)}-\frac fC a
$$

for global readout-sphere training. These negative projections destroy the coefficientwise positivity used in the raw quadratic zero-radius proof. One must not transfer that proof by analogy.

| Field                 | Classification                                                                                                                                                  |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Modified qualifier    | Unnormalized architecture and ordinary Euclidean parameter geometry                                                                                             |
| Why it is not central | It answers a different optimization/architecture question                                                                                                       |
| Transfer back         | The fixed-order derivative/Wick compiler, projector calculus, Bell-partition bookkeeping, and the proved failure of the displayed frozen natural-moment cutoffs |

*Provenance:* `normalized_mean_field_taylor_closure_audit(1).md`, §§3–7, especially §6 “What the Taylor graphs say about closure” and §7 “Precise PDE classification”; synthesis cross-check in `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§11.4 and 12, and the corresponding sections of `MASTER_NEURAL_PDE_REPORT_WITH_FIGURES.md`.

### 4.5 Frozen, tied, low-rank, and symmetric reductions

#### 4.5.1 Frozen first hidden layer

Two different uses of “frozen first layer” must be separated.

First, freezing the first hidden variables does **not** by itself make the full finite-width upper-neuron dynamics equal to a scalar cooperative system. The full composite equation still contains

$$
z'=q(a\odot z)+2K(a\odot z).
$$

What is exact inside the conditional zero-radius argument is a selected derivative history: at every differentiation one keeps the $q(a\odot z)$ term and never differentiates $q$. For a tagged upper-neuron polynomial this selected word is generated by

$$
a'=\frac12z^2,
\qquad
z'=qaz,
\qquad
q>0.
\tag{4.1}
$$

It contains the invariant ray $z=\sqrt{2q}\,a$, on which

$$
a'=qa^2.
\tag{4.2}
$$

This is an exact algebraic subhistory of the full derivation, not an invariant copy of the full frozen finite network. Coefficientwise positivity makes it a lower bound for the derivatives of the *fully trained* raw network; thus freezing is a proof device rather than a replacement model in that argument.

Second, `adversarial_audit_report(1).md` studies a genuine frozen-first-layer mean-field reduction used to audit Gaussian cutoff arguments. Its rescaled particle coordinates $u,v$ obey

$$
u'=qv^2,\qquad v'=quv,
$$

where $q>0$ is the frozen first-layer second moment, and the particle contributes $quv^2$ to the readout. Let $\mu_R$ be the centered bivariate Gaussian law conditioned to $[-R,R]^2$ and renormalized to total mass one. That report asserts that positive-corner comparison with the invariant ray $u=v$ forces every fixed subtarget $y<1$ to be reached before feature time $1/(qR)$, giving the residual-clock bound

$$
t_R(y)\le \frac{1}{2qR(1-y)}\longrightarrow0.
$$

Thus the claimed cutoff losses equal one at the origin but tend to zero at every fixed positive time; they are not uniformly Cauchy on any interval containing zero.

The supplied source gives only this comparison sketch; it does not spell out the normalized measure-level flow, the positive-corner mass estimate, or the passage from particle blow-up to the mean readout hitting time. This monograph therefore records the cutoff conclusion as a source-reported frozen-reduction claim, not as a reproduced proof. Even if completed, it cannot be promoted to the full model because the additional matrix message $K(a\odot z)$ is not componentwise positive.

| Field                 | Classification                                                                                                                                                                           |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result status         | Selected cooperative derivative word (4.1)–(4.2) is exact; Gaussian-cutoff singularity is source-reported but its full measure-level comparison proof is not reproduced                   |
| Modified qualifier    | The cutoff theorem freezes the first hidden block; the selected word is instead a proof subhistory inside the fully trained algebra                                                      |
| Why it is not central | The frozen cutoff dynamics remove feedback through the first hidden layer and part of the dense message hierarchy                                                                        |
| Transfer back         | The scalar branch gives a rigorous no-cancellation lower bound in the raw fully trained derivative algebra; the cutoff theorem invalidates proofs based only on initial tail convergence |

*Provenance:* `approximate_single_source_conjecture_resolution(1).md`, §3 “A positive embedded scalar branch” and §9 “Exact scope of the negative result”; `adversarial_audit_report(1).md`, §4.4 “Gaussian tail truncation can be dynamically singular.”

#### 4.5.2 Exact symmetric invariant manifold

At finite width the assignments

$$
x_i=x,\qquad a_j=a,\qquad W_{ji}=\frac wn
$$

form an invariant manifold for quadratic readout ascent. The exact reduced equations are

$$
f=\frac18aw^2x^4,\qquad
a'=\frac18w^2x^4,\qquad
w'=\frac14awx^4,\qquad
x'=\frac12aw^2x^3.
\tag{4.3}
$$

For

$$
a(0)=-1,\qquad w(0)=2,\qquad x(0)=\sqrt8,
$$

the invariants

$$
w^2-2a^2=2,\qquad x^2-4a^2=4
$$

reduce (4.3) to

$$
a'=4(1+a^2)^3,\qquad f=4a(1+a^2)^3.
$$

The forward real orbit crosses $f=0$ and reaches the target. Its backward blow-up distance $B$ and forward target-reaching time $\tau_*$ obey

$$
B
=\int_1^\infty\frac{ds}{4(1+s^2)^3}
\le\frac1{64},
\qquad
\tau_*
>
\int_0^1\frac{ds}{4(1+s^2)^3}
\ge\frac1{32}.
$$

Thus $B<\tau_*$: the nearest backward real singularity already bounds the Taylor radius by less than the forward target-reaching feature time. This is an exact counterexample to the inference

$$
\text{stable target-reaching real flow}
\Longrightarrow
\text{Taylor disk reaches the target}.
$$

It is not a typical Gaussian mean-field trajectory and does not establish closure.

| Field                 | Classification                                                                                              |
|-----------------------|-------------------------------------------------------------------------------------------------------------|
| Modified qualifier    | Generic iid dense initialization is replaced by exact permutation symmetry                                  |
| Why it is not central | Width has been collapsed by an imposed invariant ansatz                                                     |
| Transfer back         | It separates real-axis stability from complex-time analyticity without any asymptotic or numerical argument |

*Provenance:* `approximate_single_source_conjecture_resolution(1).md`, §7 “A finite-width check: real stability does not imply a Taylor disk.”

#### 4.5.3 Tied and low-rank parameterizations

No supplied foundational report proves a standalone closure theorem for a tied or explicitly low-rank deep network. Such systems belong in the registry because their imposed parameterization can make the state finite or coherent by construction.

| Field                              | Classification                                                                                                                              |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Exact result in the audited corpus | None                                                                                                                                        |
| Modified qualifier                 | Fully dense, untied hidden matrices                                                                                                         |
| Why it is not central              | The desired compression is inserted into the architecture rather than derived from dense training                                           |
| Transfer back                      | They can serve as controlled laboratories for response orientation, but cannot establish spontaneous compression of the unconstrained model |

This provenance gap should remain explicit until a primary project note containing a tied/low-rank theorem is supplied.

### 4.6 Exploratory but inadmissible surrogates

#### 4.6.1 Exact-curve Bernstein encoding

Let $f:[0,\infty)\to[f_0,1]$ be any continuous fitting curve with $\lim_{t\to\infty}f(t)=1$. Set

$$
q(t)=\frac{t}{1+t},\qquad
g(q)=f\!\left(\frac q{1-q}\right),\qquad g(1)=1,
$$

and let $p_M$ be the Bernstein polynomial of $g$. Then

$$
\|p_M-g\|_{L^\infty[0,1]}\to0.
$$

This approximation can be embedded in the one-field, one-source PDE

$$
\partial_tU_M
=
\bigl(1-\partial_\zeta U_M(t,0)\bigr)^2
\left[
p_M'\!\bigl(\partial_\zeta U_M(t,0)\bigr)+\zeta
\right],
\qquad
U_M(0,\zeta)=f_0.
\tag{4.4}
$$

The affine ansatz $U_M=u_M+q_M\zeta$ is invariant and gives

$$
\dot q_M=(1-q_M)^2,\qquad
\dot u_M=(1-q_M)^2p_M'(q_M),
$$

hence $q_M=t/(1+t)$ and $u_M=p_M(q_M)$. Thus (4.4) approximates *every* continuous target curve.

The construction is exact, and that is precisely why it is inadmissible: the coefficients of $p_M$ are positive-time samples of the unknown target curve. “One field,” “one source,” and even “two invariant states” do not prevent oracle playback.

*Provenance:* `adversarial_audit_report(1).md`, §1 “Why unrestricted finite one-source existence is tautological.”

#### 4.6.2 Packing an arbitrary finite ODE into one source

For any finite ODE $x'=F(x)$, the polynomial encoding

$$
U(t,\zeta)=\sum_{j=0}^{d-1}x_j(t)\zeta^j
$$

or the exponential encoding

$$
U(t,\zeta)=\sum_{j=0}^{d-1}x_j(t)e^{j\zeta}
$$

turns it syntactically into one source field by using finite coefficient extractors at $\zeta=0$. Therefore “one source” has mathematical content only when the source grammar, coefficient provenance, local operations, and complexity are fixed in advance.

*Provenance:* `adversarial_audit_report(1).md`, §§1–3; `mean_field_single_source_conjecture_audited_resolution(2).md`, §10 “Why a one-source PDE does not evade the theorem.”

#### 4.6.3 Trajectory-fitted bases and dense-matrix response surrogates

A POD, EDMD, neural surrogate, or co-moving basis chosen from the target trajectory may be a useful diagnostic. It is not an admissible witness unless the basis is fixed by the architecture or updated autonomously from the current reduced state. Similarly, a response truncation that retains every dense microscopic matrix may diagnose rapid causal-grade decay but is not a width-independent PDE.

The raw Volterra integration operator itself has singular values

$$
\sigma_k=\frac{2}{(2k-1)\pi},
$$

so unstructured causal low rank decays only algebraically. In one inadmissible diagnostic using a predetermined $66$-term total-degree Legendre basis whose coefficients were projected/fitted from realized snapshots, the reported errors were $8.5\times10^{-2}$ for iid depth, $1.28\times10^{-2}$ for a smooth generic case, and $1.66\times10^{-2}$ for a smooth nonnormal case. These numbers motivate structured response coordinates; because the coefficients use realized trajectories and the state retains dense matrices, they are not evidence for an admissible closure theorem.

| Field                  | Classification                                                                                                       |
|------------------------|----------------------------------------------------------------------------------------------------------------------|
| Exact/empirical result | Such surrogates may fit held-out time segments or show response-grade contraction                                    |
| Modified qualifier     | Architecture-local, non-oracular compilation and width-independent state                                             |
| Why it is not central  | The missing trajectory or microscopic matrix is retained in the coefficients/state                                   |
| Transfer back          | They identify promising basis directions and response variables that a later admissible compiler may try to generate |

These statements are inherited from the latest synthesis; the underlying POD and response experiment reports were not among the five primary files audited for this chapter.

*Provenance:* `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§13.4, 16.6, and 16.7; same sections in `MASTER_NEURAL_PDE_REPORT_WITH_FIGURES.md`. The source map is §20 in both files.

### 4.7 Boundary-regime conclusion

The boundary studies yield three project-wide rules.

1.  **Do not count imposed simplicity as derived compression.** Shallow depth, smooth/tied depth, freezing, low rank, and exact symmetry remove part of the mechanism that the central theorem must explain.
2.  **Do not transfer a no-go theorem across a geometry change.** RMS and sphere projections introduce signed terms that invalidate the raw positive-Wick comparison.
3.  **Do not identify finite syntax with finite information.** One source can encode an arbitrary finite ODE or an already-known target curve.

At the same time, these regimes provide indispensable proof devices: shallow transport suggests the desired state form; frozen and symmetric reductions produce exact counterexamples; normalized variants test robustness of the obstruction; and exploratory surrogates suggest what a legitimate architecture-local compiler might retain.

## Chapter 5 — The two-hidden-layer quadratic theorem laboratory

### 5.1 Scope, source key, and claim levels

This chapter studies one input, two trainable hidden layers, quadratic activation, a scalar output, and label-one squared loss. It retains a fully trained dense middle matrix and the stated $\mu$P metric, but it is not the canonical residual architecture: it has only one sample, unbounded polynomial features coupled to a Gaussian readout, a coefficientwise-positive Wick sector, and no $L\to\infty$ residual-depth limit.

For one sample, the trainable variables $x_i$ below are the first-layer preactivations on that sample. This reduction is exact for the chosen observable, but it suppresses the cross-sample geometry of a trainable input matrix. Nothing in this chapter by itself proves the corresponding multi-sample statement.

Four mathematical objects must be distinguished:

1.  the exact finite-width polynomial ODE;
2.  the putative deterministic coefficient obtained by taking $n\to\infty$ at each *fixed* derivative order, whose existence in the required mode is assumed in `(FW)`;
3.  a classical positive-time infinite-width mean-field flow, whose construction is not supplied by the foundational reports;
4.  the natural relaxed loss selected from an asserted tagged-site DMFT.

Confusing (2), (3), and (4) caused several earlier overclaims. The zero-radius theorem, conditional on (FW), concerns (2). The residual-clock theorem is an exact stability implication for any regular profile of type (1) or (3). The step-loss theorem concerns (4) and is conditional on the asserted causal DMFT representation and selection.

The source abbreviations used below are:

| Key | Exact filename                                                 |
|-----|----------------------------------------------------------------|
| Q0  | `finite_invariant_differential_algebra_resolution.md`          |
| Q1  | `approximate_single_source_conjecture_resolution(1).md`        |
| Q2  | `approximate_single_source_stability(1).md`                    |
| Q3  | `adversarial_audit_report(1).md`                               |
| Q4  | `mean_field_single_source_conjecture_audited_resolution(2).md` |
| Q5  | `normalized_mean_field_taylor_closure_audit(1).md`             |
| M15 | `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`                    |
| M16 | `MASTER_NEURAL_PDE_REPORT_WITH_FIGURES.md`                     |

Q0 is the genuine 21 July predecessor to the later references to “forest power counting.” It is directly recoverable as Library ID `libfile_f2f2d671cff081919e8c9d0a9156dd14`, File ID `file_0000000044a0820c8fbe2e119bfec4cd`, created 21 July 2026 at 19:48:38 UTC. It proves the raw forest invariant and leading width-counting rule below and gives a compressed covariance sketch; it does not prove the complete expectation or $L^1$ limit later imported as `(FW)`. No originating chat title or message identifier is preserved. The later filename `FIXED_ORDER_WICK_CONCENTRATION_THEOREM.md` does not exist; it was a proposed recovery-artifact name, not a source.

The latest master reports identify Q1–Q5 as the “foundational negative and stability reports” and preserve their fixed-order calculus, residual-clock stability, anti-oracle discipline, and model-specific no-go results. Q0 supplies the previously omitted primary structural predecessor.  
*Provenance:* Q0, Part IV; M15 and M16, §20 “Supersession and source map,” subsection “Foundational negative and stability reports.”

### 5.2 Exact finite-width model and $\mu$P scaling

For the single input, write the first hidden preactivations as $x_i$, and set

$$
h_i=\phi(x_i)=\frac{x_i^2}{2},
\qquad
z_j=\sum_{i=1}^nW_{ji}h_i,
\qquad
f_n=\frac1{2n}\sum_{j=1}^na_jz_j^2.
\tag{5.1}
$$

The loss is

$$
\mathcal L_n=(1-f_n)^2.
\tag{5.2}
$$

Initialization is independent:

$$
x_i\sim N(0,1),\qquad
a_j\sim N(0,1),\qquad
W_{ji}\sim N\!\left(0,\frac\gamma n\right),
\qquad \gamma>0.
\tag{5.3}
$$

The rescaled readout $a_j$ corresponds to a raw output weight $a_j/n$. Define the readout-ascent derivation

$$
D_{+,n}x_i=n\frac{\partial f_n}{\partial x_i},
\qquad
D_{+,n}W_{ji}=\frac{\partial f_n}{\partial W_{ji}},
\qquad
D_{+,n}a_j=n\frac{\partial f_n}{\partial a_j}.
\tag{5.4}
$$

Direct differentiation of (5.1) gives

$$
D_{+,n}a_j=\frac12z_j^2,
\tag{5.5}
$$

$$
D_{+,n}W_{ji}=\frac1n a_jz_jh_i,
\tag{5.6}
$$

$$
D_{+,n}x_i=x_i\sum_jW_{ji}a_jz_j.
\tag{5.7}
$$

Put

$$
q_n=\frac1n\sum_ih_i^2,\qquad
u=a\odot z,\qquad
K_n=W\operatorname{diag}(h)W^\top.
\tag{5.8}
$$

Using $D_+h_i=x_iD_+x_i=2h_i\sum_jW_{ji}u_j$, one obtains the exact composite equation

$$
D_{+,n}z=q_nu+2K_nu.
\tag{5.9}
$$

Equation (5.9) is the smallest formula exhibiting both mechanisms of the laboratory:

- $q_nu$ contains a cooperative scalar Riccati branch;
- $K_nu$ contains dense matrix reuse and is not componentwise positive, although $K_n\succeq0$ when $h_i\ge0$.

The physical squared-loss gradient flow is

$$
\dot x=2(1-f_n)D_{+,n}x,\quad
\dot W=2(1-f_n)D_{+,n}W,\quad
\dot a=2(1-f_n)D_{+,n}a.
\tag{5.10}
$$

Thus the model is nonlazy in scaling: all three parameter groups have $O(1)$ composite feature-time velocities under the chosen metric. This statement is about scaling and the exact equations; it is not a theorem that a regular infinite-width trajectory exists for positive time.

*Provenance:* Q1, §1 “Exact model and feature-time derivation”; Q2, §1 “Network and exact squared-loss identities”; Q4, §1 “Network, scaling, and notation.”

### 5.3 Tangent kernel, feature time, and residual clock

Define the metric tangent kernel

$$
\kappa_n
=
n\|\nabla_xf_n\|^2
+\|\nabla_Wf_n\|_F^2
+n\|\nabla_af_n\|^2
\ge0.
\tag{5.11}
$$

Along readout ascent $\Theta_n'(\tau)=D_{+,n}\Theta_n(\tau)$, let

$$
H_n(\tau)=f_n(\Theta_n(\tau)).
$$

Then, exactly,

$$
H_n'(\tau)=\kappa_n(\Theta_n(\tau)).
\tag{5.12}
$$

The squared-loss trajectory runs along the same parameter-space orbit with the residual clock

$$
\dot\tau_n(t)=2\bigl(1-H_n(\tau_n(t))\bigr),
\qquad
f_n(t)=H_n(\tau_n(t)).
\tag{5.13}
$$

Consequently

$$
\dot f_n=2(1-f_n)\kappa_n,
\qquad
\dot{\mathcal L}_n=-4\kappa_n\mathcal L_n.
\tag{5.14}
$$

These identities are exact at finite width wherever the ODE exists.

#### 5.3.1 Coercivity after positive entry

Let

$$
C_n=\frac1n\|a\|^2.
$$

The readout part of (5.11) is $\frac1{4n}\sum_jz_j^4$. Cauchy–Schwarz gives

$$
f_n^2
\le
C_n\left(\frac1{4n}\sum_jz_j^4\right)
\le C_n\kappa_n.
\tag{5.15}
$$

From (5.10),

$$
\dot C_n=4f_n(1-f_n).
\tag{5.16}
$$

Suppose $f_n(t_*)=a_*\in(0,1)$ and the trajectory stays on the target-side branch $0<f_n<1$. Then

$$
\frac d{dt}\frac{C_n}{f_n^2}
=
\frac{4(1-f_n)}{f_n}
\left(1-\frac{C_n\kappa_n}{f_n^2}\right)
\le0.
$$

Hence, for $t\ge t_*$,

$$
\kappa_n(t)\ge\frac{f_n(t)^2}{C_n(t)}
\ge\lambda_n,
\qquad
\lambda_n:=\frac{a_*^2}{C_n(t_*)}>0.
\tag{5.17}
$$

Therefore

$$
1-f_n(t)\le(1-a_*)e^{-2\lambda_n(t-t_*)},
\qquad
\mathcal L_n(t)\le(1-a_*)^2e^{-4\lambda_n(t-t_*)}.
\tag{5.18}
$$

The exact balance laws

$$
\frac d{dt}\frac{\|x\|^2}{4n}
=
\frac d{dt}\frac{\|W\|_F^2}{2}
=
\dot C_n
\tag{5.19}
$$

then prevent post-entry parameter blow-up.

The qualification matters. Negative-output finite-width initial states can lie in a dead-feature basin. At the centered Gaussian initialization with $\gamma=4/3$, the fixed-order calculation gives

$$
f_n(0)\longrightarrow0,
\qquad
\kappa_n(0)\longrightarrow\frac{17}{6}.
$$

Turning this pointwise initial value into a width-uniform mean-field version of (5.17) still requires a short-time moment/uniform-integrability estimate, which is not supplied by Q2.

#### 5.3.2 Finite feature-time budget

If $H_n$ reaches $1$ at feature time $\tau_*$, then (5.17) implies $\tau_*<\infty$. On the bounded post-entry finite-dimensional orbit, $\kappa_n$ is bounded; hence the exact residual exponential in (5.14) reaches zero only as physical time tends to infinity. Moreover,

$$
\int_{t_*}^{\infty}2(1-f_n(t))\,dt
=\tau_*-\tau_n(t_*)
\le\frac{1-a_*}{\lambda_n}.
\tag{5.20}
$$

Thus a residual-compatible hidden-equation defect $R$ accumulates according to

$$
\int_{t_*}^{\infty}2(1-f_n(t))\|R(t)\|\,dt
=
\int_{\tau_n(t_*)}^{\tau_*}\|R(\tau)\|\,d\tau.
\tag{5.21}
$$

This is the exact reason an all-physical-time *stability* theorem can follow from a compact feature-time approximation.

*Provenance:* Q2, §§1, 3, and 4. Q1, §8 preserves the clock theorem after disproving the concrete Taylor approximation.

### 5.4 The conditional global clock-shadowing theorem

Let $H,\widetilde H$ be monotone feature-time profiles with the same $f_0<1$, both reaching $1$. Assume that their target-reaching intervals lie in a common interval on which

$$
0<\mu\le H'(\tau)\le K,
\qquad
\|H-\widetilde H\|_\infty\le\varepsilon.
\tag{5.22}
$$

Let

$$
\dot\tau=2(1-H(\tau)),
\qquad
\dot{\widetilde\tau}=2(1-\widetilde H(\widetilde\tau)).
\tag{5.23}
$$

Assume the clocks have the same initial value, normalized here as $\tau(0)=\widetilde\tau(0)=0$.

Then

$$
\sup_{t\ge0}|\widetilde\tau(t)-\tau(t)|
\le\frac{\varepsilon}{\mu},
\tag{5.24}
$$

$$
\sup_{t\ge0}
|\widetilde H(\widetilde\tau(t))-H(\tau(t))|
\le
\left(1+\frac K\mu\right)\varepsilon,
\tag{5.25}
$$

and

$$
\sup_{t\ge0}
|\widetilde{\mathcal L}(t)-\mathcal L(t)|
\le
2(1-f_0)
\left(1+\frac K\mu\right)\varepsilon.
\tag{5.26}
$$

**Proof.** Put $e=\widetilde\tau-\tau$. When $e>0$, monotonicity and (5.22) give

$$
\dot e
=2\bigl(H(\tau)-\widetilde H(\widetilde\tau)\bigr)
\le-2\mu e+2\varepsilon.
$$

When $e<0$, the same inequality holds for the upper Dini derivative of $|e|$. Scalar comparison proves (5.24). Equation (5.25) follows by adding the profile defect to $K|e|$. Finally, $x\mapsto(1-x)^2$ is $2(1-f_0)$-Lipschitz on $[f_0,1]$, proving (5.26). $\square$

This theorem is complete under its displayed hypotheses. It proves *propagation control*, not *production of a small defect*. In particular it cannot be applied to the Wick–Taylor profiles below with $\varepsilon\to0$, because, under (FW), those profiles diverge.

*Provenance:* Q2, §6 “Global clock-shadowing theorem”; corrected scope in Q1, §8 “What remains true: the observable stability theorem”; audit in Q3, §5 “Audit of the positive identities.”

#### 5.4.1 Direct input-to-state stability in the loss channel

There is a complementary formulation that does not assume a common feature profile. Suppose, after a positive-entry time,

$$
\dot{\mathcal L}=-4\kappa\mathcal L,
\qquad
\dot{\widehat{\mathcal L}}
=-4\widehat\kappa\widehat{\mathcal L}+\delta_{\mathcal L},
$$

and assume

$$
\kappa,\widehat\kappa\ge\lambda>0,\qquad
|\widehat\kappa-\kappa|\le\delta,\qquad
|\delta_{\mathcal L}|\le\rho.
$$

Let $E_0$ be the loss mismatch at that time and $L_0$ the true loss. Integrating factors give

$$
\sup_{t\ge0}
|\widehat{\mathcal L}(t)-\mathcal L(t)|
\le
E_0
+L_0\Psi\!\left(\frac\delta\lambda\right)
+\frac{\rho}{4\lambda},
$$

where

$$
\Psi(x)=x(1+x)^{-1-1/x}
\le\min\!\left\{1,\frac xe\right\}.
$$

For the rate term, the cumulative rate mismatch is at most $\delta t$, while both cumulative rates are at least $\lambda t$. Maximizing

$$
e^{-4\lambda t}\bigl(1-e^{-4\delta t}\bigr)
$$

over $t\ge0$ gives $\Psi(\delta/\lambda)$. Duhamel’s formula bounds the additive channel by $\rho/(4\lambda)$. If the approximation preserves

$$
\dot{\widehat f}=2(1-\widehat f)\widehat\kappa,
$$

then $\delta_{\mathcal L}=0$. A small local hidden-state residual is not enough unless it yields the displayed kernel or loss-channel bounds.

*Provenance:* Q2, §7 “Direct input-to-state stability for an arbitrary finite PDE.”

### 5.5 Fixed-order Wick calculus and the proposed one-source Taylor closure

For every fixed $k$, define the random finite-width coefficient

$$
C_{n,k}:=\frac{D_{+,n}^kf_n(0)}{k!}.
$$

Q0 uses **descent** on the linear objective, whereas this chapter uses readout ascent. Write its derivation as

$$
D_{\downarrow,n}:=-D_{+,n}.
$$

Then

$$
D_{\downarrow,n}^{\,k}f_n
=(-1)^kD_{+,n}^{\,k}f_n,
\qquad
C_{n,k}
=\frac{(-1)^k}{k!}D_{\downarrow,n}^{\,k}f_n(0).
$$

If Q0's unnormalized expected descent coefficient exists,

$$
c_k^\downarrow
:=
\lim_{n\to\infty}
\mathbb E[D_{\downarrow,n}^{\,k}f_n(0)],
$$

then the coefficient convention in this chapter is

$$
c_k=\frac{(-1)^k}{k!}c_k^\downarrow.
$$

This sign and factorial translation is algebraic; it does not establish either limit.

#### 5.5.1 Recovered raw derivative-history theorem

Q0 represents a raw monomial in $D_{\downarrow,n}^{\,k}f_n$ as

$$
n^{-r_{\mathrm F}}
\sum_{\mathrm{indices}}
\prod_{u\in V_{\rm up}}a_u^{p_u}
\prod_{v\in V_{\rm low}}h_v^{m_v}
\prod_{e\in E}W_{u(e)v(e)}.
$$

There is one upper or lower occurrence vertex for each formal index class and one bipartite edge for each $W$-factor. Newly introduced summation indices are distinct formal occurrence labels before numerical equality partitions are imposed. The output (5.1) starts as one connected two-edge star with $r_{\mathrm F}=1$.

The descent derivation has three exact graph rewrites.

1.  An $a$-hit uses
    $$
    D_{\downarrow,n}a_u
    =
    -\frac12\sum_{v,w}W_{uv}W_{uw}h_vh_w.
    $$
    Differentiating $a_u^p$ grafts a two-leaf cherry at the same upper vertex. This represents trained readout weights and preserves both $r_{\mathrm F}$ and component count.
2.  An $h$-hit uses
    $$
    D_{\downarrow,n}h_v
    =
    -2h_v\sum_{u,w}W_{uv}a_uW_{uw}h_w.
    $$
    Differentiating $h_v^m$ grafts a lower--upper--lower path. This represents first-layer training through $h=x^2/2$ and again preserves $r_{\mathrm F}$ and component count.
3.  A middle-weight hit uses
    $$
    D_{\downarrow,n}W_{uv}
    =
    -\frac1n a_uh_v\sum_wW_{uw}h_w.
    $$
    It removes the differentiated edge, adds its explicit $1/n$, and grafts a new lower leaf at $u$. In a forest the removed edge is a bridge, so the operation increases both $r_{\mathrm F}$ and the number of components by one.

Induction gives the recovered structural theorem:

> **Raw derivative-history forest invariant [proved in Q0].** Every raw monomial in $D_{\downarrow,n}^{\,k}f_n$ is a bipartite forest with exactly $r_{\mathrm F}$ connected components when its explicit normalization is $n^{-r_{\mathrm F}}$.

The theorem includes all three trained parameter groups. It is stronger than the generic statement that only finitely many histories exist at fixed order.

#### 5.5.2 Width power counting and leading contractions

Suppose a raw forest contains $2P$ occurrences of $W$. A Gaussian pairing contributes $(\gamma/n)^P$ and identifies the two upper endpoints and the two lower endpoints in each paired edge pair. Collapse every paired pair to one quotient bond. Let

- $V$ be the number of free upper and lower quotient index classes;
- $c_{\mathrm F}$ be the quotient component count; and
- $\beta=P-V+c_{\mathrm F}\ge0$ be its cycle rank.

On the injective equality stratum of that quotient, the width exponent is

$$
n^{V-P-r_{\mathrm F}}
=
n^{c_{\mathrm F}-\beta-r_{\mathrm F}}.
$$

Pairing and identification cannot increase component count, so $c_{\mathrm F}\le r_{\mathrm F}$. Hence no contraction has positive width exponent. The exponent is zero exactly when

$$
c_{\mathrm F}=r_{\mathrm F},
\qquad
\beta=0.
$$

Thus:

> **Leading double-forest rule [proved in Q0].** A pairing is eligible for leading $n^0$ order exactly when it preserves every raw component and has a forest quotient. Pairings that merge raw components or create a quotient cycle lose at least one power of $n$.

“Eligible for leading order” does not mean that the coefficient is nonzero. Odd total $a$-degree at an upper quotient vertex, a zero history coefficient, or cancellation between signed descent histories can still kill it. Extra accidental equality of otherwise free upper or lower indices lowers $V$ and is subleading. At surviving quotient vertices,

$$
\mathbb E[h^m]
=
\frac{(2m)!}{4^m m!},
$$

while odd local powers of the centered Gaussian $a$ vanish.

#### 5.5.3 What the recovered concentration paragraph proves—and does not prove

For fixed $k$ there are finitely many raw histories and pairings. Q0's entire covariance discussion is one paragraph: in two replicas, contractions internal to each replica cancel against the product of expectations; any genuine cross-replica $W$-pairing or shared primitive initialization index connects two raw components; the width rule then loses at least one power of $n$. It concludes

$$
\operatorname{Var}\!\left(
D_{\downarrow,n}^{\,k}f_n(0)
\right)=O(n^{-1}).
$$

This is a serious and structurally plausible proof sketch, but not a fully expanded theorem. The source does not:

- enumerate the finite equality partitions and falling-factorial index counts needed to prove convergence of the expectation;
- organize doubled forests with possibly different component counts $r_1,r_2$;
- enumerate every cross-replica $W$-pairing and every shared upper $a$ or lower primitive-$x$ index;
- treat explicitly the induced cross-moments of the noncentered, non-Gaussian variable $h=x^2/2$; or
- expose the fixed-$k$ aggregate constant in the covariance bound.

Later reports add an unsupported sentence invoking fixed-degree Gaussian hypercontractivity and uniform integrability. Those are not separate necessary obligations if the two combinatorial steps above are completed. Expectation convergence together with the claimed variance bound would give

$$
\mathbb E\left|
C_{n,k}-c_k
\right|^2\longrightarrow0,
$$

and therefore $L^1$ convergence directly.

The stronger hypothesis actually used by the downstream theorem is therefore retained explicitly:

> **(FW) Remaining fixed-order deterministic-limit bridge.** For every fixed $k$,
> $$
> C_{n,k}\xrightarrow[n\to\infty]{L^1}c_k,
> \tag{5.27}
> $$
> where $c_k$ is deterministic and equals the sum of the surviving leading fixed-order Wick contractions.

The raw forest invariant, width exponent, and leading double-forest rule are proved structural inputs to `(FW)`; the expectation/covariance/$L^1$ completion is not. At increasing fixed order, the histories also contain ordered $W/W^\top$ reuse words, product-rule trees, activation derivatives, learned rank-one insertions, population contractions, and Wick pairings. “Finite at every fixed order” does not mean that the union over all orders is a finite closed algebra.

The proposed feature profile was

$$
H_M(\tau)=\sum_{k=0}^Mc_k\tau^k.
\tag{5.28}
$$

It was inserted into

$$
\partial_tU_M(t,\tau)
=2\bigl(1-U_M(t,0)\bigr)\partial_\tau U_M(t,\tau),
\qquad
U_M(0,\tau)=H_M(\tau).
\tag{5.29}
$$

The degree-$M$ polynomial subspace is invariant. With

$$
u_k(t)=\partial_\tau^kU_M(t,0),
$$

(5.29) is equivalent to

$$
\dot u_k=2(1-u_0)u_{k+1},
\quad 0\le k<M,
\qquad
\dot u_M=0,
\tag{5.30}
$$

initialized by $u_k(0)=k!c_k$.

This is a genuine finite autonomous system at each $M$. What fails is its convergence to the quadratic mean-field dynamics.

At finite width, ordinary Taylor’s theorem would give, on $0\le\tau\le T$,

$$
\left\|
H_n-\sum_{k=0}^M\frac{H_n^{(k)}(0)}{k!}\tau^k
\right\|_\infty
\le
\frac{T^{M+1}}{(M+1)!}
\sup_{0\le\sigma\le T}|H_n^{(M+1)}(\sigma)|.
$$

This identity is not a tail estimate uniform in $n$ and $M$. The lower bound in the next section proves that the limiting initialization coefficients cannot satisfy the analytic estimate that Q2 originally proposed to use.

*Provenance:* Q0, Part IV supplies the raw forest invariant, width counting, leading-pairing rule, and compressed variance sketch. Q1, §2 gives the precise conjecture being resolved; Q2, §§5 and 8 gives the proposed Taylor hierarchy. The claim in Q2, §9 that a uniform Taylor-tail estimate was the only remaining lemma is superseded by Q1 and by the explicit (FW) audit above.

### 5.6 Zero-radius theorem

#### 5.6.1 Positive scalar branch

Freeze $x$ only for the purpose of selecting one derivative history, and retain

$$
a'=\frac12z^2,\qquad z'=qaz.
\tag{5.31}
$$

Define

$$
\mathscr D_0
=
\frac{z^2}{2}\partial_a+qaz\,\partial_z,
\qquad
g(a,z)=\frac12az^2,
$$

$$
P_k(a,z;q)=\frac1{k!}\mathscr D_0^kg(a,z).
\tag{5.32}
$$

Every coefficient of $P_k$ is nonnegative. Each application of $\mathscr D_0$ increases total degree by one and reverses the parity of the exponent of $a$. Hence for odd $k$, with $m=(k+3)/2$,

$$
P_k(a,z;q)
=
\sum_{u+v=m}p_{uv}(q)a^{2u}z^{2v},
\qquad p_{uv}(q)\ge0.
\tag{5.33}
$$

The ray $z=\sqrt{2q}\,a$ is invariant. Starting from $a(0)=1$,

$$
a(\tau)=\frac1{1-q\tau},
\qquad
g(\tau)=\frac{q}{(1-q\tau)^3}.
$$

Comparing Taylor coefficients yields

$$
P_k(1,\sqrt{2q};q)
=q^{k+1}\binom{k+2}{2}.
\tag{5.34}
$$

#### 5.6.2 No cancellation in the raw full network

In independent primitive coordinates,

$$
f_n
=
\frac1{8n}
\sum_{j,i,\ell}
a_jW_{ji}W_{j\ell}x_i^2x_\ell^2.
\tag{5.35}
$$

The coefficients of (5.35) are nonnegative. The readout-ascent vector field is obtained by differentiating this polynomial and multiplying by positive metric factors, so it also has nonnegative primitive coefficients. Therefore $D_{+,n}$ preserves the cone of coefficientwise nonnegative polynomials.

For independent centered Gaussians, a primitive monomial has zero expectation if an exponent is odd and positive expectation if all exponents are even. Thus every surviving Wick history is nonnegative. The history that repeatedly selects $q_n(a\odot z)$ in (5.9) and never differentiates $q_n$ cannot be cancelled by the omitted $K_n$-histories.

At initialization

$$
q_n\to q_0:=\mathbb E\!\left[\left(\frac{G^2}{2}\right)^2\right]
=\frac34.
\tag{5.36}
$$

This convergence holds almost surely and in every fixed moment. More precisely, conditional on the entire first-hidden-layer vector $h$, for every upper neuron $j$,

$$
a_j\sim N(0,1),\qquad
z_j\sim N(0,\gamma q_n),
\qquad a_j\perp z_j,
$$

and the pairs are conditionally independent across $j$. Thus, for every fixed selected scalar-branch polynomial, conditional Gaussian evaluation followed by fixed-moment convergence of $q_n$ gives

$$
\mathbb E\!\left[P_k(a_j,z_j;q_n)\right]
\longrightarrow
\mathbb E\!\left[P_k(A,Z;q_0)\right],
\qquad
A\sim N(0,1),\quad Z\sim N(0,\gamma q_0),\quad A\perp Z.
$$

This limit for the single selected history does not require (FW). What requires (FW) is identification of the complete aggregate coefficient $C_{n,k}$ with a deterministic limit $c_k$. Q0's forest theorem explains which aggregate histories can be leading, but its compressed covariance paragraph does not complete that identification. Although Q0 writes descent histories, the algebraic factor $D_{\downarrow,n}^k=(-1)^kD_{+,n}^k$ is common to every order-$k$ history; after the translation in §5.5, the ascent-side coefficientwise positivity applies exactly as stated above.

#### 5.6.3 Factorial lower bound

Let

$$
b_\gamma
=\frac12\min\!\left\{1,\frac\gamma2\right\}>0.
\tag{5.37}
$$

For $u+v=m$,

$$
\frac{\mathbb E[A^{2u}Z^{2v}]}{(2q_0)^v}
=(2u-1)!!(2v-1)!!
\left(\frac\gamma2\right)^v.
$$

Since

$$
(2u-1)!!\ge u!,\qquad
(2v-1)!!\ge v!,\qquad
u!v!\ge\frac{m!}{2^m},
$$

and

$$
\left(\frac\gamma2\right)^v
\ge\min\!\left\{1,\frac\gamma2\right\}^{m},
$$

we obtain

$$
\mathbb E[A^{2u}Z^{2v}]
\ge
m!b_\gamma^m(2q_0)^v.
\tag{5.38}
$$

Assume (FW). Its $L^1$ convergence lets expectations pass to the deterministic aggregate limit. The preceding conditional calculation identifies the selected history's own limit without using (FW), and coefficientwise positivity makes every omitted ascent-side Wick history nonnegative. Therefore

$$
c_k
=\lim_{n\to\infty}\mathbb E[C_{n,k}]
\ge
\mathbb E[P_k(A,Z;q_0)].
$$

Combining this inequality with (5.33), (5.34), and (5.38) proves:

> **Theorem 5.1 (zero radius conditional on (FW)).**  
> For every odd $k$, with $m=(k+3)/2$, $$
> c_k
> \ge
> m!b_\gamma^m q_0^{k+1}\binom{k+2}{2}.
> \tag{5.39}
> $$ Consequently $$
> \limsup_{k\to\infty}c_k^{1/k}=+\infty.
> \tag{5.40}
> $$

For the variance-normalized project value $\gamma=4/3$, $b_\gamma=1/3$, so the bound specializes to

$$
c_k
\ge
m!\,3^{-m}\left(\frac34\right)^{k+1}
\binom{k+2}{2}
\qquad(k\ \text{odd}).
$$

Indeed, $(m!)^{1/k}\asymp\sqrt{k}$. Thus the formal series $\sum c_k\tau^k$ has radius zero. The statement is about the iterated fixed-order mean-field coefficients. It is not a claim about the random finite-$n$ Taylor radius under a coupled choice $k=k(n)$.

*Provenance:* Q0 proves the derivative-history forest and width-counting core. Q1, §§3–5 proves the selected positive-history comparison and the downstream lower bound; Q3, “Established zero-radius input” and §4.2, independently audits its scope. None of Q0–Q3 completes the remaining expectation/covariance/$L^1$ bridge (FW).

### 5.7 Consequences and scoped no-go theorems

Unless stated otherwise, every conclusion in §§5.7.1–5.7.4 that uses the limiting coefficients $c_k$ is conditional on (FW). The branchwise continuation-algebra result in §5.7.5 is independent of (FW) but conditional on its own freeness and continuation-separation lemmas. The real-axis non-identification statement in §5.7.6 is independent of (FW).

#### 5.7.1 Failure of the one-source Wick–Taylor PDE

Assume (FW). The order here is prescribed and iterated: for each fixed coefficient order $k$, first take $n\to\infty$ to obtain $c_k$; form the resulting degree-$M$ profile; only then send $M\to\infty$. No conclusion is asserted for a coupled diagonal $M=M(n)$, or for a fixed-$n$ Taylor germ inside its own random radius.

The precise shadowing claim under test is

$$
\lim_{M\to\infty}
\limsup_{n\to\infty}
\sup_{t\ge0}
|\mathcal L_M(t)-\mathcal L_n(t)|
=0.
$$

If this held, the triangle inequality would force the deterministic closure sequence to be uniformly Cauchy:

$$
\|\mathcal L_M-\mathcal L_{M'}\|_\infty
\le
\limsup_{n\to\infty}
\left(
\|\mathcal L_M-\mathcal L_n\|_\infty
+
\|\mathcal L_n-\mathcal L_{M'}\|_\infty
\right).
$$

All $c_k\ge0$, $c_0=0$, and (5.40) implies that for every $\tau>0$,

$$
H_M(\tau)\to+\infty.
\tag{5.41}
$$

For $y\in(0,1)$, let $\tau_M^\star(y)$ be the first positive root of $H_M(\tau)=y$. For any fixed odd $k$ and every $M\ge k$,

$$
y=H_M(\tau_M^\star(y))\ge c_k\bigl(\tau_M^\star(y)\bigr)^k,
$$

so

$$
\tau_M^\star(y)\le\left(\frac y{c_k}\right)^{1/k}.
\tag{5.42}
$$

Given any $\eta>0$, choose an odd $k$ with $(y/c_k)^{1/k}<\eta$, and then take every $M\ge k$. This proves $\tau_M^\star(y)\to0$ without interchanging the fixed-order width limit with the truncation limit.

The characteristic of (5.29) satisfies

$$
\dot\tau_M=2(1-H_M(\tau_M)),\qquad \tau_M(0)=0.
$$

The physical time required to reach $y$ is

$$
t_M(y)
=
\int_0^{\tau_M^\star(y)}
\frac{d\tau}{2(1-H_M(\tau))}
\le
\frac{\tau_M^\star(y)}{2(1-y)}
\to0.
\tag{5.43}
$$

Because $H_M$ is increasing, its characteristic approaches the first root $H_M=1$ without overshoot. For any fixed $t>0$ and any $y<1$, (5.43) puts the output above $y$ for all sufficiently large $M$; then letting $y\uparrow1$ gives

$$
\mathcal L_M(0)=1,
\qquad
\mathcal L_M(t)\to0\quad\text{for every fixed }t>0.
\tag{5.44}
$$

The continuous functions $\mathcal L_M$ approach a discontinuous step pointwise and are not uniformly Cauchy on any interval containing $0$. The triangle argument therefore contradicts the prescribed iterated finite-width shadowing claim, independently of whether a regular positive-time full mean-field loss exists. It is more precise to state this conclusion than to say that the closures fail to converge to a mean-field trajectory that has not itself been constructed.

*Provenance:* Q1, §6 “Direct failure of the one-source PDE in physical time.”

#### 5.7.2 $L^2$ and one-space Banach obstructions

Ordinary $L^2$ does not control the polynomial observables. On a nonatomic probability space, choose $\Pr(A_R)=R^{-3}$ and set

$$
a_R=z_R=R\,\mathbf 1_{A_R}.
$$

Then

$$
\|a_R\|_2^2+\|z_R\|_2^2=\frac2R\to0,
\qquad
\mathbb E[a_Rz_R^2]=1.
\tag{5.45}
$$

Thus the cubic readout is discontinuous under vanishing $L^2$ perturbations. A compactness or minimizing-movement proof based only on the quadratic balance laws cannot control the loss.

There is also no ordinary Banach function algebra $X$ that both contains a nondegenerate Gaussian and embeds continuously in $L^1$. If

$$
\|xy\|_X\le C_2\|x\|_X\|y\|_X,
\qquad
\|x\|_1\le C_1\|x\|_X,
$$

then

$$
\|x^m\|_1
\le C_1C_2^{m-1}\|x\|_X^m.
$$

Taking $m$-th roots and $m\to\infty$ gives

$$
\|x\|_\infty\le C_2\|x\|_X.
$$

Hence $X\subset L^\infty$, excluding a Gaussian coordinate.

Finally, assume (FW). An exact realization $Y'=F(Y)$, $H'=K(Y)$ with $F,K$ analytic near the Gaussian initial state in one Banach space would give a positive Taylor radius by the analytic ODE theorem, contradicting (5.40). A viable theory must therefore use an unbounded generator, a scale of spaces with loss of regularity, a renormalized/signed construction, or a genuinely nonanalytic real-axis formulation. The preceding $L^2$ counterexample and Gaussian Banach-algebra obstruction do not depend on (FW); only this zero-radius contradiction does.

*Provenance:* Q3, §4.2 “Ordinary Gaussian L2 is not a valid closure topology.”

#### 5.7.3 Positive-semigroup obstruction

Assume (FW). Let $\mathcal A_+$ be the cone of primitive polynomials with nonnegative coefficients, $D$ the readout-ascent derivation, and $\Lambda$ Gaussian Wick expectation. Suppose a positive strongly continuous semigroup $S(\tau)$:

1.  extends $D$ on every $D^kf$;
2.  preserves $\mathcal A_+$;
3.  admits the semigroup Taylor formula on these vectors; and
4.  has a continuous positive extension of $\Lambda$.

Then the integral remainder is positive and

$$
\Lambda(S(\tau)f)
\ge
\sum_{k=0}^Mc_k\tau^k.
$$

The right side tends to $+\infty$ for every $\tau>0$. Hence no *finite-valued positive classical semigroup completion satisfying all four conditions* exists.

This no-go theorem does not exclude a mild state outside all generator domains, a discontinuous or renormalized readout, or a signed nonlocal cancellation. Such an alternative must still be identified with the actual network.

*Provenance:* Q3, §4.2, paragraphs beginning “Positivity gives a stronger result.”

#### 5.7.4 Positive polynomial compiler obstruction

Assume (FW). Let $E_h$ be pullback by one explicit Euler state update:

$$
E_hp=p\circ(I+hX),
$$

where $X$ is the polynomial ascent vector field. Positivity of the primitive coefficients yields

$$
E_h=I+hD+\sum_{\ell\ge2}h^\ell A_\ell,
$$

with every $A_\ell$ preserving the positive polynomial cone. In $E_h^Nf$, select $hD$ in exactly $k$ factors and the identity in the others. Every omitted term has nonnegative Wick expectation, so with $h=\tau/N$,

$$
\mathbb E[E_{\tau/N}^Nf]
\ge
\tau^k\frac{(N)_k}{N^k}c_k.
\tag{5.46}
$$

For any $\tau>0$ and $A>0$, first choose $k$ with $c_k\tau^k>2A$, then $N$ with $(N)_k/N^k>1/2$. Thus the width-first, mesh-second Euler/Wick profile diverges to $+\infty$.

The same argument covers a Wick-positive consistent polynomial one-step compiler

$$
E_h=I+hD+\sum_{\ell\ge2}h^\ell A_\ell
$$

whose remainder operators preserve the positive cone, including the stated positive-stage polynomial schemes. More abstractly, if positive polynomial profiles recover every fixed $c_k$ coefficientwise, they diverge at every positive source value.

It does **not** cover an implicit or tamed nonpolynomial rule, a signed resummation, or a scale-space Galerkin method with a separately proved residual estimate.

*Provenance:* Q3, §4.3 “Worst-case numerical stability is not width/tail uniform” and §6 “Audit outcomes for proposed constructions.”

#### 5.7.5 Conditional branchwise continuation-algebra no-go

Q0 contains a second, logically different obstruction that later summaries did not preserve. In descent feature time,

$$
D_{\downarrow,n}z=-(q_nI+2K_n)A_nz,
\qquad
A_n=\operatorname{diag}(a),
$$

so repeatedly differentiating only the terminal $z$ produces every ordered word of length $r$ in

$$
U=A_n,\qquad V=K_nA_n.
$$

All $2^r$ words occur with nonzero selected-branch coefficients. This is an ordered, noncommutative response family; it is not captured merely by counting scalar Taylor coefficients.

Indeed, at each hit one selects either $-q_nU$ or $-2V$ while leaving the prefactors undifferentiated. A word containing $p$ selections of $U$ and $r-p$ selections of $V$ therefore appears with coefficient $(-1)^rq_n^p2^{r-p}\ne0$ almost surely at initialization.

The recovered source proposes the following restricted compiler category. An encoder is exact, linear on the formal branch span, and continuation-faithful: its continuation grammar can tag individual Leibniz branches and leading Wick pairings. Its state consists of finitely many fields over finitely many **commuting** source variables; its local dynamics use finite-jet differential polynomials. Give a jet coordinate $U_{b,\alpha}$ the additive weight

$$
\operatorname{wt}(U_{b,\alpha})=1+|\alpha|,
$$

extend weight additively to monomials, and let $\mathcal F_{B,d}^{(\le N)}$ be the span of differential monomials of total weight at most $N$. The **bounded-filtration assumption** is the precise requirement that constants $C_0,C_1$, independent of $r$, exist such that the encoder image of every depth-$r$ branch lies in $\mathcal F_{B,d}^{(\le C_0+C_1r)}$. This is the content needed from the source's informal statement that each microscopic hit raises one-hole operator weight by only $O(1)$.

Two additional lemmas are required.

1.  **Fixed-degree freeness and faithfulness.** At initialization, $A_n$ is independent of the orthogonally invariant $K_n=W\operatorname{diag}(h)W^\top$; their fixed-degree normalized trace moments converge to a free pair $(a,k)$ whose free-product state is faithful. Under the substitution $U\mapsto a$, $V\mapsto ka$, the trace Gram matrix
    $$
    G_{v,w}=\tau(M_v^*M_w)
    $$
    is positive definite on distinct words.
2.  **Branch-separating continuation.** The allowed tagged continuations realize this Gram separation in the formal derivative/Wick hierarchy, so an exact continuation-faithful encoder must preserve the $2^r$ independent length-$r$ branch classes.

Granting those lemmas, the remaining dimension argument is complete. With $B<\infty$ fields over $1\le d<\infty$ commuting sources, there are only $O(k^{d-1})$ jet generators of exact weight $k$. The zero-source case is smaller. The Hilbert-series bound for the corresponding commutative differential-polynomial algebra gives

$$
\dim\mathcal F_{B,d}^{(\le N)}
\le
\exp\!\left(O\!\left(N^{d/(d+1)}\right)\right)
=\exp(o(N)).
$$

For completeness, if $a_k\le Ck^{d-1}$ is the number of generators of weight $k$, the Hilbert series is bounded coefficientwise by

$$
\mathcal H(z)
\le
\prod_{k\ge1}(1-z^k)^{-a_k}.
$$

With $z=e^{-s}$,

$$
\log\mathcal H(e^{-s})
\le
\sum_{m,k\ge1}\frac{a_k}{m}e^{-skm}
\le C_d s^{-d}.
$$

The sum of coefficients through weight $N$ is therefore at most
$\exp(sN+C_ds^{-d})$; optimizing at $s\asymp N^{-1/(d+1)}$ gives the displayed subexponential bound.

Bounded filtration growth puts every depth-$r$ encoding in weight $N=O(r)$, whose available dimension is subexponential in $r$, contradicting the $2^r$ independent branch responses.

> **Conditional branchwise no-go.** Subject to the two lemmas above and the stated bounded-filtration compiler grammar, no exact finite-commuting-source, finite-jet differential-polynomial encoder can be linear and continuation-faithful on the complete tagged branch hierarchy.

This result does not use (FW), coefficient positivity, or time analyticity. Its scope is nevertheless narrow. It does **not** rule out an accidental equation for the untagged aggregate loss; approximate $(\varepsilon,T)$-dependent closures; signed nonpolynomial, nonlocal, infinite-order, or scale-of-spaces constructions; noncommuting, path-, graph-, or response-valued sources; positive-time real-axis methods; or the bounded residual architecture. The bounded-filtration assumption is substantive: without it, an exponentially large jet index can encode a binary word. Q0 sketches rather than proves the freeness/faithfulness and branch-separation lemmas, so this is an exact conditional implication, not a self-contained unconditional theorem.

*Provenance:* Q0, the finite-invariant differential-algebra and continuation-capacity sections. The combinatorial word count and Hilbert-series comparison survive audit; the two named bridge lemmas remain explicit dependencies.

#### 5.7.6 Complete jets do not identify a real-axis trajectory

Once analyticity fails, even the infinite initialization jet does not determine a smooth positive-time function: adding a nonzero flat term such as $e^{-1/\tau^2}\mathbf 1_{\tau>0}$ changes the real-axis trajectory without changing any derivative at $0$. Padé or Borel resummation therefore selects a continuation unless a quasianalyticity, summability, or independent real-axis well-posedness theorem identifies it with the network.

This is a semantic non-identification theorem, not a proof that every resummation fails.

*Provenance:* Q3, end of §3 and §4.3.

#### 5.7.7 What remains open

The preceding results do not rule out every non-oracular, accuracy-dependent, signed, nonanalytic real-axis compiler. A substantive positive theorem would need:

- an explicit mean-field state space and target-reaching solution;
- continuity of readout and kernel in the forcing topology;
- a fixed architecture-local compiler;
- computable initial, outgoing-residual, and kernel-reconstruction bounds tending to zero;
- a nonnegative approximate kernel or another target-reaching certificate;
- the clock-shadowing theorem of §5.4.

No such full-model construction is proved in Q1–Q5. Conversely, no lower bound covers all admissible signed real-axis compilers.

*Provenance:* Q3, §3 “A nontrivial and determinate conjecture,” §6, and §7 “Exact final conclusion.”

### 5.8 Conditional tagged-site DMFT and instantaneous fitting

#### 5.8.1 The representation hypothesis

The following result is conditional. Assume that the fully trained infinite-width system is represented, on an initial time triangle, by the causal tagged-site equations

$$
z(t)
=
\zeta(t)
+\int_0^t r(s)M(t,s)a(s)z(s)\,ds,
\qquad
\dot a(t)=r(t)z(t)^2,
\tag{5.47}
$$

where:

1.  $r=1-f$;
2.  $\zeta$ is a centered Gaussian process with continuous sample paths and $\operatorname{Var}\zeta(0)>0$;
3.  $a(0)\sim N(0,1)$ is independent of the entire cavity process $\zeta$;
4.  $M$ is deterministic, causal, and continuous near $0$;
5.  $f(0)=0$, and the self-consistent output obeys $$
    \dot f=2r\kappa,\qquad
    \kappa\ge\frac14\mathbb E[z^4]
    \tag{5.48}
    $$ while the classical flow exists.

In the convention that factors $r(s)$ outside $M$, the exact instantaneous coefficient suggested by the finite equations is

$$
M(0,0)
=
2\mathbb E[h_0^2]+4\gamma\mathbb E[h_0]
=\frac32+2\gamma>0,
\qquad h_0=\frac12G^2.
\tag{5.49}
$$

Hence continuity gives $M(t,s)\ge m>0$ on a sufficiently short triangle.

Q4 treats (5.47) as the canonical DMFT. The audited status used here is more cautious: Q1–Q5 do not derive (5.47), prove its self-consistency from the finite network, or construct its classical positive-time solution. The comparison theorem below is exact **if** (5.47)–(5.49) hold.

#### 5.8.2 Extreme-readout comparison

Fix $y\in(0,1)$ and suppose $f(t)<y$ on a positive interval, so

$$
r(t)\ge c:=1-y.
$$

Choose $z_*>0$ so that $\Pr[\zeta(0)\ge2z_*]>0$. Sample-path continuity implies

$$
\sup_{t\le\delta}|\zeta(t)-\zeta(0)|\longrightarrow0
\quad\text{almost surely as }\delta\downarrow0.
$$

Therefore, for sufficiently small $\delta_0$, the intersection of
$\{\zeta(0)\ge2z_*\}$ with
$\{\sup_{t\le\delta_0}|\zeta(t)-\zeta(0)|\le z_*\}$ has positive probability, and hence

$$
p_\zeta
:=
\Pr\!\left[\inf_{0\le t\le\delta_0}\zeta(t)\ge z_*\right]>0.
$$

For every finite $A$, define

$$
p_A
:=
\Pr\!\left[
a(0)\ge A,\ 
\inf_{t\le\delta_0}\zeta(t)\ge z_*
\right]
=
p_\zeta\Pr[a(0)\ge A]
>0.
\tag{5.50}
$$

Choose from now on $A>z_*/\sqrt m$ and large enough that the comparison blow-up time $T_A$ in (5.52) is below $\delta_0$; this is possible because $T_A\to0$. On this event, cooperative comparison gives

$$
a(t)\ge b(t),\qquad z(t)\ge v(t),
$$

where

$$
\dot b=cv^2,\qquad
\dot v=cm\,bv,\qquad
b(0)=A,\quad v(0)=z_*.
\tag{5.51}
$$

The invariant

$$
v^2-z_*^2=m(b^2-A^2)
$$

implies, with $\lambda_A=\sqrt{A^2-z_*^2/m}$,

$$
\dot b=cm(b^2-\lambda_A^2).
$$

Its blow-up time is

$$
T_A
=
\frac1{2cm\lambda_A}
\log\!\left(\frac{A+\lambda_A}{A-\lambda_A}\right)
=O\!\left(\frac{\log A}{A}\right)
\to0.
\tag{5.52}
$$

Before the subtarget is reached, (5.48) and the positive event imply

$$
\dot f(t)
\ge
\frac{c\,p_A}{2}v(t)^4.
\tag{5.53}
$$

Since $\int_0^{T_A}v(t)^4dt=\infty$, the output must hit $y$ before $T_A$. Sending $A\to\infty$ proves

$$
T_y=0
\qquad\text{for every }y\in(0,1).
\tag{5.54}
$$

Thus no classical output continuous at $0$ can satisfy the assumed DMFT. In the additional monotone, no-overshoot relaxed class, the selected loss is

$$
\mathcal L_{\mathrm{rel}}(t)
=
\begin{cases}
1,&t=0,\\
0,&t>0.
\end{cases}
\tag{5.55}
$$

Every continuous surrogate $\widehat{\mathcal L}$ then obeys

$$
\sup_{t\ge0}
|\widehat{\mathcal L}(t)-\mathcal L_{\mathrm{rel}}(t)|
\ge\frac12,
\tag{5.56}
$$

and if $\widehat{\mathcal L}(0)=1$, the lower bound is $1$.

The theorem proves the implication

$$
\text{causal representation (5.47)–(5.49)}
\Longrightarrow
\text{no continuous all-time uniform closure of its relaxed step loss}.
$$

It does not prove that the finite networks converge to (5.55), that the asserted DMFT is the unique infinite-width limit, or that the relaxed selection is forced without the monotone/no-overshoot criterion.

*Provenance:* Q4, §§2–10. The conditional classification is required by the later project-level audit summarized in M15/M16, §11.4, and by the fact that Q3, §4.1, records that the target full Gaussian mean-field flow had not been constructed.

### 5.9 Normalized and projected quadratic variants

#### 5.9.1 Universal residual-clock conversion

In this section,

$$
\langle v,w\rangle:=\frac1n\sum_i v_iw_i,
\qquad
\langle v\rangle:=\frac1n\sum_i v_i.
$$

For a centered feature profile

$$
H(\tau)=A\tau+\frac B{3!}\tau^3+O(\tau^5),
$$

the exact label-one residual clock gives

$$
\mathcal L(t)
=
1-4At+8A^2t^2
-\frac{32A^3+8B}{3}t^3
+\frac{32A^4+44AB}{3}t^4
+O(t^5).
\tag{5.57}
$$

Antipodal readout symmetry forces $H$ to be odd at centered initialization for the raw, RMS-normalized, and global direction-WN conventions considered in Q5.

*Provenance:* Q5, §2 “Universal loss jet through order five.”

#### 5.9.2 RMS after both hidden activations

Define

$$
s_\ell^2=\langle(h^{(\ell)})^2\rangle,
\qquad
u^{(\ell)}=\frac{h^{(\ell)}}{s_\ell},
$$

with the full normalized forward architecture

$$
h^{(1)}=\phi(z^{(1)}),\qquad
u^{(1)}=\frac{h^{(1)}}{s_1},
\qquad
z^{(2)}=W^{(2)}u^{(1)},\qquad
h^{(2)}=\phi(z^{(2)}),\qquad
u^{(2)}=\frac{h^{(2)}}{s_2}.
$$

and use

$$
f=\langle a,u^{(2)}\rangle.
$$

The denominators are recomputed at every feature time, with no centering, no learned gain, and no stabilizing $\varepsilon_\ell$. Freezing $s_\ell$ at initialization would be a fixed rescaling and would give different higher-order coefficients.

For

$$
J_\ell
=
\frac1{s_\ell}
\bigl(I-u^{(\ell)}\otimes u^{(\ell)}\bigr)
\operatorname{diag}\phi'(z^{(\ell)}),
$$

where $(u\otimes u)v=u\langle u,v\rangle$ in the normalized population inner product.

put

$$
\delta_2=J_2^*a
=
\frac{\phi'(z^{(2)})}{s_2}
\odot(a-fu^{(2)}),
$$

$$
b=W^\top\delta_2,\qquad
\delta_1=J_1^*b.
$$

The exact feature-time vector field is

$$
D_+a=u^{(2)},\qquad
D_+W=\frac1n\delta_2(u^{(1)})^\top,\qquad
D_+z^{(1)}=\delta_1,
$$

$$
D_+z^{(2)}=\delta_2+WJ_1\delta_1,
$$

and the exact tangent kernel is

$$
\kappa_{\mathrm{RMS}}
=
1+\langle\delta_2^2\rangle+\langle\delta_1^2\rangle.
\tag{5.58}
$$

For $\phi(u)=u^2/2$ and exact RMSNorm, the audited Gaussian contractions give, for every $\gamma>0$,

$$
A_{\mathrm{RMS}}(\gamma)
=\frac{25}{9}+\frac{4}{3\gamma},
$$

$$
B_{\mathrm{RMS}}(\gamma)
=-\frac{117760}{729}
-\frac{15616}{81\gamma}
-\frac{2848}{27\gamma^2}
-\frac{640}{27\gamma^3}.
$$

At $\gamma=4/3$,

$$
A_{\mathrm{RMS}}=\frac{34}{9},
\qquad
B_{\mathrm{RMS}}=-\frac{273712}{729}.
\tag{5.59}
$$

The negative cubic coefficient is a genuine sign reversal relative to the raw network. The exact vector field above is derived in the monograph, but the large rational Wick contractions for $A_{\mathrm{RMS}}$ and $B_{\mathrm{RMS}}$ are source-reported audited calculations: the supplied corpus gives grouped contraction checks, not a complete term-by-term symbolic certificate. Substitution into (5.57) yields the physical-time Taylor coefficients

$$
\mathcal L_{\mathrm{RMS}}(t)
=1-\frac{136}{9}t
+\frac{9248}{81}t^2
+\frac{103552}{243}t^3
-\frac{40745600}{2187}t^4
+O(t^5).
$$

These displayed numbers are Taylor coefficients; the $m$-th derivative at zero is $m!$ times the coefficient of $t^m$.

*Provenance:* Q5, §§3.1–3.5.

#### 5.9.3 Direction-only weight normalization

The convention is part of the theorem. The formulas below use direct projected (Riemannian) gradient on each fixed-radius row, rather than Euclidean training of an auxiliary variable $v$ in $w=gv/\|v\|$; they include one global sphere for the rescaled readout; and every normalized hidden row has large incoming fan-in in the fixed-order mean-field limit.

Under direct projected gradient on the global rescaled readout sphere,

$$
C=\langle a^2\rangle,\qquad
D_+a=h^{(2)}-\frac fC a,
\tag{5.60}
$$

so $C$ is constant and the readout kernel is

$$
\langle(h^{(2)})^2\rangle-\frac{f^2}{C}.
$$

For a fixed-radius middle row, write

$$
g_j^2=\|W_j\|_2^2
$$

for its fixed squared radius. Then

$$
D_+W_j
=
\frac{a_j\phi'(z_j)}n
\left(h^{(1)}-\frac{z_j}{g_j^2}W_j\right).
\tag{5.61}
$$

Its radial correction to $D_+z_j$ is $O(n^{-1})$ at each fixed derivative order under the large-fan-in convention. Thus hidden-row WN is asymptotically invisible to the fixed-order hierarchy; the global readout projection is the surviving modification.

If the first hidden row instead has fixed input dimension, its projector survives and the coefficients involve joint spherical/gain integrals. Applying direction-only normalization directly to the already-collapsed scalar $x_i$ would leave only a sign and freeze that coordinate; that is a different degenerate model, not the convention used for (5.61)–(5.63).

For the raw quadratic model,

$$
A(\gamma)
=
\frac{75}{64}\gamma^2+\frac9{16}\gamma,
$$

$$
B_0(\gamma)
=
\frac{5205}{32}\gamma^4
+\frac{47511}{256}\gamma^3
+\frac{15201}{256}\gamma^2
+\frac{243}{64}\gamma.
$$

Global readout projection gives

$$
B_{\mathrm{WN}}
=
B_0-\frac{2A(2A-R)}C,
\tag{5.62}
$$

where $R=\mathbb E[\phi(G_2)^2]$ is the readout contribution to $A$. For the quadratic Gaussian initialization, $C=1$ and

$$
G_2\sim N\!\left(0,\frac{3\gamma}{4}\right),
\qquad
R=\frac{27}{64}\gamma^2,
$$

so (5.62) is equivalently

$$
B_{\mathrm{WN}}(\gamma)
=\frac{323895}{2048}\gamma^4
+\frac{92565}{512}\gamma^3
+\frac{14877}{256}\gamma^2
+\frac{243}{64}\gamma.
$$

In particular, at $\gamma=4/3$,

$$
A=\frac{17}{6},\qquad
B_0=\frac{229957}{216},\qquad
B_{\mathrm{WN}}=\frac{223939}{216}.
\tag{5.63}
$$

As in the RMS case, the vector-field and projector formulas are explicit here, while the displayed high-order rational Wick coefficients are inherited from the source calculation rather than accompanied by every contraction table.

Thus

$$
\mathcal L_{\mathrm{WN}}(t)
=1-\frac{34}{3}t
+\frac{578}{9}t^2
-\frac{81197}{27}t^3
+\frac{14181587}{324}t^4
+O(t^5).
$$

*Provenance:* Q5, §§4.1–4.5.

#### 5.9.4 Exact failure of finite natural moment cutoffs in frozen reductions

The following exact frozen top-block reductions do not make the displayed monomial hierarchy invariant at any finite rectangular degree cutoff. They are independent denominator/projector checks, not invariant subsystems proved to represent the complete fully trained normalized networks.

For a frozen top block with final RMS normalization, let

$$
M_{p,r}=\mathbb E[a^pz^r],\qquad
R^2=M_{0,4},\qquad
f=M_{1,2}/R.
$$

Its exact feature-time particle equations are

$$
a'=\frac{z^2}{R},
\qquad
z'=\frac{2z}{R}\left(a-\frac{fz^2}{R}\right).
$$

The exact recurrence is

$$
M_{p,r}'
=
\frac pR M_{p-1,r+2}
+\frac{2r}{R}M_{p+1,r}
-\frac{2rf}{R^2}M_{p,r+2}.
\tag{5.64}
$$

For the frozen readout-WN top block,

$$
a'=\frac12z^2-fa,
\qquad
z'=qaz,
\qquad
f=\frac12\mathbb E[az^2],
$$

where $q=\mathbb E[(h^{(1)})^2]$ (equal to $3/4$ in the stated quadratic Gaussian audit), and therefore

$$
M_{p,r}'
=
\frac p2M_{p-1,r+2}
-pfM_{p,r}
+rqM_{p+1,r}.
\tag{5.65}
$$

As independent denominator/projector checks, these recurrences give, for the initializations stated in Q5,

$$
H_{\mathrm{RMS,top}}(\tau)
=\frac73\tau-\frac{464}{81}\tau^3
+\frac{174368}{3645}\tau^5+O(\tau^7),
$$

$$
H_{\mathrm{WN,top}}(\tau)
=\frac32\tau+\frac{75}{16}\tau^3
+\frac{8181}{640}\tau^5+O(\tau^7).
$$

Both recurrences generate moments outside every finite rectangular degree cutoff. They prove failure of the *natural polynomial-moment cutoff closure for these frozen reductions*. The full trained normalized differentiation graphs exhibit the same outward proliferation, but the corpus does not supply the invariant-embedding, algebraic-independence, or noncancellation argument needed to promote that diagnostic to a theorem for the full normalized systems. Neither result proves that no nonlinear sufficient statistic, algebraic relation among reachable moments, or accuracy-dependent real-axis approximation exists.

*Provenance:* Q5, §5 “Independent reduction checks” and §6 “What the Taylor graphs say about closure.”

#### 5.9.5 What normalization does and does not resolve

RMS differentiation creates reciprocal-moment vertices, projector derivatives, Bell partitions, and disconnected contractions. Direction-WN creates projector words; the readout adds $-fa/C$. These signed terms invalidate the raw coefficientwise-positive lower bound.

Accordingly:

- zero radius is **not proved** for RMSNorm;
- zero radius is **not proved** for global readout direction-WN;
- if only large-fan-in hidden rows are normalized and the readout is not projected, every fixed-order limiting coefficient agrees with the raw hierarchy, so under (FW) the raw zero-radius result transfers under that convention;
- no finite rectangular truncation of the displayed frozen natural-moment hierarchies is invariant; analogous full-system nonclosure is strongly indicated but not proved here;
- every non-Taylor finite PDE remains unruled-out.

*Provenance:* Q5, §§6.3 and 7.

### 5.10 Authoritative theorem and non-theorem ledger

| Claim                                                                                   | Status                                                              | Exact scope                                                                               |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Finite-width gradients, composite equation (5.9), kernel positivity, and residual clock | Proved                                                              | Exact polynomial ODE, while it exists                                                     |
| Positive-entry coercivity and finite feature-time budget                                | Proved under displayed trajectory hypotheses                        | Target-side finite-width trajectory; a uniform mean-field burn-in is not supplied         |
| Clock-shadowing bounds (5.24)–(5.26)                                                    | Proved                                                              | Any two monotone target-reaching profiles satisfying (5.22)                               |
| Raw derivative-history forest invariant                                                 | Proved in Q0                                                        | Every fixed order; all three trained parameter groups                                      |
| Width exponent and leading $c_{\mathrm F}=r_{\mathrm F}$, $\beta=0$ rule                | Proved in Q0                                                        | Injective equality strata; leading eligibility does not guarantee a nonzero coefficient    |
| $\operatorname{Var}(D_{\downarrow,n}^kf_n)=O(n^{-1})$                                   | Compressed source sketch; full proof open                           | Missing complete doubled-forest/shared-index enumeration                                   |
| Deterministic fixed-order $L^1$ limit                                                    | Open; assumed as (FW)                                               | Each order fixed before $n\to\infty$                                                       |
| Factorial lower bound and zero radius                                                   | Exact under (FW)                                                     | Raw quadratic, Gaussian initialization, unbounded readout                                 |
| Uniform convergence of the Taylor one-source PDE                                        | Falsified conditional on (FW)                                       | Prescribed width-first, order-second Wick–Taylor family                                   |
| Coefficientwise-positive fixed-order-consistent polynomial compilers                    | Falsified conditional on (FW)                                      | Positive polynomial/Wick cone; excludes signed or nonpolynomial methods                   |
| One analytic Banach-space realization                                                   | Impossible conditional on (FW)                                     | Exact analytic $F,K$ near the Gaussian initial state                                      |
| Positive classical semigroup realization                                                | Impossible under (FW) and four explicit positivity/domain/readout hypotheses | Does not cover mild/signed/renormalized constructions                              |
| Branchwise finite-commuting-source continuation encoder                                  | Exact conditional implication under the §5.7.5 compiler grammar and two bridge lemmas | Does not address the untagged aggregate loss or noncommuting/response-valued states |
| Naive Gaussian cutoff convergence                                                       | Falsified only in a frozen subsystem                                | Does not transfer componentwise through the full $K_nu$ message                           |
| Any non-oracular signed real-axis finite compiler                                       | Open                                                                | Requires explicit state, residual norm, and stability theorem                             |
| Tagged-site instantaneous fitting                                                       | Exact implication under the asserted DMFT representation            | Representation, finite-network identification, and relaxed selection remain unproved here |
| Natural relaxed step loss                                                               | Conditional selection                                               | Requires monotone, no-overshoot relaxation                                                |
| Finite natural moment/message cutoff in the frozen RMS/global-WN reductions             | Falsified                                                           | The displayed frozen hierarchies; full-system nonclosure is diagnostic, not proved         |
| Zero radius after RMS/global readout WN                                                 | Open                                                                | Raw positivity proof no longer applies                                                    |

The strongest transferable lesson is not that finite neural PDEs are impossible. It is narrower and more useful:

> Conditional on completion of (FW), in an unbounded quadratic/Gaussian feature-learning model, fixed-order correctness, squared-loss stability, and exact finite syntax do not imply a convergent closure. Ordinary initialization Taylor/Wick summation and broad positive polynomial compilers fail because rare Gaussian amplitudes generate factorial responses. Independently, the recovered continuation-capacity argument conditionally obstructs a narrow class of exact branchwise finite-commuting-source encoders. Any positive theorem for the canonical bounded residual network must instead be real-axis, causal, and explicit about its state topology and response information.

Conversely, the strongest non-transfer statement is:

> None of the raw positivity, zero-radius, or conditional instantaneous-fitting arguments is a no-go theorem for bounded nonlinear residual networks. Normalization already demonstrates why: signed projectors can change the coefficient structure, and the central residual architecture changes the activation, depth limit, data regime, and causal state.

*Final provenance check:* Q1, §9 and “Final conclusion”; Q3, §§6–7; Q4, §12; Q5, §7; M15 and M16, §§11.4, 12.4–12.5, and 20.

## Chapter 6 — The canonical dense residual program: construction and exact internal theory

### 6.1 Scope, notation, and the claim boundary

This chapter fixes the standard model used by the project’s principal positive program and derives two objects that must not be conflated:

1.  the finite dense residual network, whose equations and Euclidean-gradient identities are exact at every finite width $n$ and residual depth $L$; and
2.  the finite-cutoff operator–Hermite Liouville PDE, whose internal forward/transpose pairing, projected-gradient identity, positive-semidefinite tangent kernel, and loss dissipation are exact wherever that PDE is well posed.

Neither set of exact identities proves that the finite PDE is the ordered dense limit. The missing identification statement has three distinct layers: first take $n\to\infty$ at each fixed $L$; next homogenize the trained iid residual layers as $L\to\infty$; finally show that increasing the operator cutoff converges to the resulting limit. Uniformity for all training time is a further step.

The following notation will be used consistently.

- $r,q,k\in\{1,\ldots,m\}$ index training samples.
- $\ell\in\{0,\ldots,L-1\}$ is discrete residual depth and $s\in[0,1]$ is its continuum coordinate.
- $t\ge0$ is training time.
- $n$ is network width, $L$ is original residual depth, and $r_{\mathrm H}$ is a maximum source-Hermite degree. To avoid confusing the activation with the Hermite basis, the activation is denoted by $\sigma$, while source Hermites are denoted by $\psi_\nu$.
- $P_{r_{\mathrm H}}$ is the number of retained source modes. Numerical depth and cubature resolutions are denoted by $N,M,R$; they approximate a fixed PDE and are not network width or physical depth.
- “Exact finite-cutoff theorem” always means a theorem about the displayed finite PDE itself. “Dense-limit identification” means equality between that PDE hierarchy and the ordered limit of the original trained dense networks.

The canonical positive case uses $\sigma=\tanh$. The later sine, normalized-erf, and normalized-arctangent cases are empirical stress or extension cases; they do not silently enlarge the theorem’s model class.

**Status.** The finite-network equations below are proved by direct differentiation. The finite-PDE geometric identities are exact conditional on sufficient regularity and well-posedness of the displayed forward/backward boundary problem and transport flow. Ordered-limit existence, finite-cutoff-to-infinite-cutoff convergence, and dense-limit identification remain open.

**Primary provenance.** `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§1–6 and §11; `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§1–6 and §11; `dense_euclidean_continuous_depth_npde_audit.md`, §§2–4 and §12. The later master report supersedes the earlier smooth-depth and executable-$K/J/N$-compiler interpretations.

### 6.2 The finite dense residual network and the Euclidean $\mu$P metric

Fix a finite dataset

$$
\{(x_r,y_r)\}_{r=1}^m,\qquad x_r\in\mathbb R^d,\quad y_r\in\mathbb R.
$$

For width $n$, residual depth $L$, and residual scale $\gamma>0$, define

$$
h_r^0=Bx_r,\qquad z_r^\ell=W_\ell h_r^\ell,
$$

$$
\boxed{
h_r^{\ell+1}
=h_r^\ell+\frac{\gamma}{L}\sigma(z_r^\ell),
\qquad 0\le\ell<L,
}
\tag{6.1}
$$

$$
\boxed{
f_r=\frac1n a^\top h_r^L,\qquad
e_r=f_r-y_r,\qquad
\mathcal L=\frac12\sum_{r=1}^m e_r^2.
}
\tag{6.2}
$$

Here

$$
B\in\mathbb R^{n\times d},\qquad
W_\ell\in\mathbb R^{n\times n},\qquad
a\in\mathbb R^n.
$$

Every hidden matrix is fully dense, untied, and unconstrained; $B$, $a$, and all $W_\ell$ train. Canonical initialization is independent:

$$
B_{ij}\sim N(0,1),\qquad
a_i\sim N(0,A^2),\qquad
(W_\ell)_{ij}\sim N\!\left(0,\frac{\sigma_w^2}{n}\right).
\tag{6.3}
$$

The standard Euclidean feature-learning multipliers are

$$
\boxed{
\eta_B=n,\qquad
\eta_a=n,\qquad
\eta_{W_\ell}=L.
}
\tag{6.4}
$$

Thus

$$
\dot B=-n\nabla_B\mathcal L,\qquad
\dot a=-n\nabla_a\mathcal L,\qquad
\dot W_\ell=-L\nabla_{W_\ell}\mathcal L.
$$

The factor $L$ in the hidden-block rate compensates for the $L^{-1}$ residual branch. Without it, the feature motion produced by training the $W_\ell$’s vanishes in the residual-depth limit, although a separately trained input block could still move features. If one instead parameterizes $W_\ell=\widehat W_\ell/\sqrt n$, the equivalent raw multiplier for $\widehat W_\ell$ is $nL$.

This convention is not an orthogonal, natural-gradient, projected, normalized, or low-rank optimizer. Fixed positive constants multiplying the three block rates change the relative Euclidean block metric; a common constant merely rescales training time.

**Primary provenance.** `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §2; `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§1.1–1.3; `dense_euclidean_continuous_depth_pde_conjecture(1).md`, §§1–2.

### 6.3 Exact adjoint, gradients, tangent kernel, and finite-network dissipation

Define the unit-output adjoint by

$$
p_r^L=a.
$$

Let

$$
D_r^\ell=\operatorname{diag}\sigma'(z_r^\ell),
\qquad
\beta_r^\ell=D_r^\ell p_r^{\ell+1}.
$$

Differentiating the residual block gives the exact backward recursion

$$
\boxed{
p_r^\ell
=
\left(
I+\frac{\gamma}{L}W_\ell^\top D_r^\ell
\right)p_r^{\ell+1}.
}
\tag{6.5}
$$

The resulting parameter flow is

$$
\boxed{
\dot W_\ell
=-\frac{\gamma}{n}
\sum_{q=1}^m e_q\,
\beta_q^\ell(h_q^\ell)^\top,
}
\tag{6.6}
$$

$$
\boxed{
\dot a=-\sum_qe_qh_q^L,\qquad
\dot B=-\sum_qe_qp_q^0x_q^\top.
}
\tag{6.7}
$$

To derive the output equation, write

$$
G_{rq}^{u,\ell}
=\frac1n(u_r^\ell)^\top u_q^\ell,
\qquad
Q^x_{rq}=x_r^\top x_q.
$$

The three parameter blocks contribute

$$
\boxed{
\dot f=-\Theta^{n,L}e,
}
\tag{6.8}
$$

with

$$
\boxed{
\Theta_{rq}^{n,L}
=
G_{rq}^{h,L}
+
Q^x_{rq}G_{rq}^{p,0}
+
\frac{\gamma^2}{L}
\sum_{\ell=0}^{L-1}
G_{rq}^{h,\ell}G_{rq}^{\beta,\ell}.
}
\tag{6.9}
$$

The first two terms are Gram matrices. The last is an average of Schur products of two Gram matrices and is therefore positive semidefinite. Hence

$$
\boxed{
\Theta^{n,L}\succeq0,\qquad
\dot{\mathcal L}
=-e^\top\Theta^{n,L}e\le0.
}
\tag{6.10}
$$

The inverse-metric identity is

$$
\boxed{
-\dot{\mathcal L}
=
\frac1n\|\dot a\|^2
+
\frac1n\|\dot B\|_F^2
+
\frac1L\sum_{\ell=0}^{L-1}\|\dot W_\ell\|_F^2.
}
\tag{6.11}
$$

For fixed $n,L$, (6.11) bounds parameter travel on every finite training interval. Combined with smoothness of the finite-dimensional vector field, it gives global finite-$(n,L)$ gradient flow. It does not give a width/depth-uniform $L^1$-in-time feature arclength, a tangent-kernel spectral gap, or convergence as $t\to\infty$.

The scale is genuinely feature learning. If $\|h\|,\|\beta\|=O(\sqrt n)$, the rank-one learned matrix component $n^{-1}\beta h^\top$ has $O(n^{-1})$ RMS entries but $O(1)$ coherent operator action:

$$
\left\|\frac1n\beta h^\top\right\|_{\mathrm{op}}
=\frac{\|\beta\|\,\|h\|}{n}
=O(1).
\tag{6.12}
$$

This is precisely why entrywise or normalized-Frobenius smallness does not imply causal irrelevance.

**Primary provenance.** `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §1.4; `dense_euclidean_continuous_depth_npde_audit.md`, §§2.1–2.3; `dense_euclidean_continuous_depth_pde_conjecture(1).md`, §2.

### 6.4 The ordered target and the iid-depth homogenization problem

The canonical target is

$$
\boxed{
n\to\infty\ \text{at each fixed }L,
\qquad
L\to\infty\ \text{second}.
}
\tag{6.13}
$$

For each finite network, interpolate the depth-indexed hidden Gram in $s=\ell/L$ and define

$$
\mathcal O_{n,L}(t)
=\bigl(f_{n,L}(t),G_{n,L}^h(\cdot,t)\bigr).
$$

The ordered target, if it exists, is a deterministic path

$$
\mathcal O(t)
=\bigl(f(t),G^h(\cdot,t)\bigr)
\in
\mathbb R^m\times C([0,1];\mathbb S_+^m)
\tag{6.14}
$$

such that, for every $T<\infty$ and $\delta>0$,

$$
\lim_{L\to\infty}\lim_{n\to\infty}
\Pr\!\left[
\sup_{0\le t\le T}
\left(
\|f_{n,L}(t)-f(t)\|_2
+
\sup_{s\in[0,1]}
\|G_{n,L}^h(s,t)-G^h(s,t)\|_F
\right)>\delta
\right]=0.
\tag{6.15}
$$

Existence and uniqueness of this target for the fully trained model are not established in the supplied project corpus.

The second limit is not obtained by linearly interpolating the raw iid matrices $W_\ell(0)$. Their step interpolants are not strongly translation-compact in depth. At initialization, oddness of $\tanh$ and independence of the current layer give

$$
\mathbb E\!\left[
\tanh(W_\ell h_r^\ell)
\mid W_0,\ldots,W_{\ell-1},B
\right]=0,
$$

and therefore

$$
\mathbb E\frac{\|h_r^L-h_r^0\|^2}{n}
=
\frac{\gamma^2}{L^2}\sum_{\ell=0}^{L-1}
\mathbb E\frac{\|\tanh(W_\ell h_r^\ell)\|^2}{n}
\le \frac{\gamma^2}{L}.
\tag{6.16}
$$

The centered initialization displacement has normalized RMS at most $\gamma L^{-1/2}$, even though nonlinear local quantities such as $\mathbb E[\tanh'(Wh)]$ remain $O(1)$. The appropriate depth object is therefore a homogenized layer-type or Gaussian Young/cavity law coupled to slow forward and backward fields—not a realized smooth matrix path $W(s)$.

A depth-coherent Gaussian matrix process produces a legitimate classical neural-ODE limit, but that is a different initialization law and a different order of limits. It cannot be substituted for the iid-depth target. The present program must prove that, after training, centered row/column innovations still cancel under the $1/L$ residual accumulation while their conditional shared-transpose/Onsager mean survives.

**Primary provenance.** `dense_euclidean_continuous_depth_npde_audit.md`, §3; `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §2; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§2.1–2.2.

### 6.5 Exact memory identities and why current Grams do not close

Integrating (6.6) gives, exactly at finite $n,L$,

$$
\boxed{
W_\ell(t)
=W_\ell^0
-\frac{\gamma}{n}\sum_q
\int_0^t
e_q(\tau)\,
\beta_q^\ell(\tau)
h_q^\ell(\tau)^\top
\,d\tau.
}
\tag{6.17}
$$

Define the two-training-time correlations

$$
C_{qr}^{h,\ell}(\tau,t)
=\frac1n h_q^\ell(\tau)^\top h_r^\ell(t),
\qquad
C_{qr}^{\beta,\ell}(\tau,t)
=\frac1n\beta_q^\ell(\tau)^\top\beta_r^\ell(t).
$$

Then

$$
\boxed{
\begin{aligned}
W_\ell(t)h_r^\ell(t)
={}&W_\ell^0h_r^\ell(t)\\
&-\gamma\sum_q
\int_0^t e_q(\tau)
C_{qr}^{h,\ell}(\tau,t)
\beta_q^\ell(\tau)\,d\tau ,
\end{aligned}}
\tag{6.18}
$$

$$
\boxed{
\begin{aligned}
W_\ell(t)^\top\beta_r^\ell(t)
={}&(W_\ell^0)^\top\beta_r^\ell(t)\\
&-\gamma\sum_q
\int_0^t e_q(\tau)
C_{qr}^{\beta,\ell}(\tau,t)
h_q^\ell(\tau)\,d\tau .
\end{aligned}}
\tag{6.19}
$$

Thus eliminating $W_\ell$ does not produce a one-time Gram system; it produces two-time memory. Moreover, the same $W_\ell^0$ appears in a forward row action and a backward column action. Their conditional Gaussian mean is an Onsager/response term. Replacing the backward action by an independent Gaussian copy changes the model.

An exact continuation witness shows the missing information concretely. Choose $h,\beta\in\mathbb R^n$ with

$$
h^\top\beta=0,\qquad
\|h\|^2=c^2n,\qquad
\|\beta\|^2=n,
$$

and let a base matrix $K$ annihilate the presently queried directions. Set

$$
W_0=K,\qquad
W_1=K+\frac1n h\beta^\top.
\tag{6.20}
$$

For the minimal displayed witness it is enough to impose

$$
Kh=0,\qquad K^\top\beta=0;
$$

in a multi-sample state, $K$ is chosen to match all other finitely many currently queried actions as well.

Because $\beta^\top h=h^\top\beta=0$, the perturbation does not change the present actions $Wh$ or $W^\top\beta$, and it is invisible to ordinary limiting entry laws and fixed present Grams. Yet

$$
(W_1-W_0)\beta=h,\qquad
(W_1-W_0)^\top h=c^2\beta.
\tag{6.21}
$$

A future response direction can therefore differ by $O(1)$. This refutes exact closure by a current list of row marginals and Grams on any restart class containing the witness. It does not prove that the witness is dynamically reachable from the canonical Gaussian initialization, nor does it refute a response-aware or approximately sufficient state.

**Primary provenance.** `dense_euclidean_continuous_depth_npde_audit.md`, §§4.2–4.4 and §6.1; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§13.1 and 11.1; `dense_euclidean_continuous_depth_pde_conjecture(1).md`, §4.

### 6.6 The immutable Gaussian source and the cylindrical operator projection

The concrete finite PDE starts from the immutable neuron label

$$
\boxed{
\eta=
\left(B_j(0),\frac{a_j(0)}A\right)
\sim\mu=N(0,I_{d+1}).
}
\tag{6.22}
$$

Let $\{\psi_\nu\}_{\nu\in\mathbb N^{d+1}}$ be the normalized multivariate Hermite basis of $L^2(\mu)$. At complete total degree $r_{\mathrm H}$, retain

$$
\Lambda_{r_{\mathrm H}}
=\{\nu:|\nu|\le r_{\mathrm H}\},
\qquad
\boxed{
P_{r_{\mathrm H}}
=|\Lambda_{r_{\mathrm H}}|
=\binom{d+1+r_{\mathrm H}}{r_{\mathrm H}}.
}
\tag{6.23}
$$

For a slow source field $v\in L^2(\mu)$, the truncated initial row action is

$$
(W_{r_{\mathrm H}}^0v)(\xi,\varepsilon)
=
\sigma_w\sum_{\nu\in\Lambda_{r_{\mathrm H}}}
\varepsilon_\nu
\langle\psi_\nu,v\rangle_\mu,
\qquad
\varepsilon\sim N(0,I_{P_{r_{\mathrm H}}}).
\tag{6.24}
$$

For any fixed pair of queries,

$$
\mathbb E_\varepsilon
\bigl[(W_{r_{\mathrm H}}^0v)(W_{r_{\mathrm H}}^0v')\bigr]
=
\sigma_w^2
\langle\Pi_{r_{\mathrm H}}v,
\Pi_{r_{\mathrm H}}v'\rangle_\mu.
\tag{6.25}
$$

This is a cylindrical projection after the width limit. It is not a rank-$P_{r_{\mathrm H}}$ finite network: the limiting state remains law-valued, the row label is a population variable, and no pairwise neuron matrix appears.

Hermite completeness yields

$$
\|(I-\Pi_{r_{\mathrm H}})v\|_{L^2(\mu)}\to0
\tag{6.26}
$$

for each fixed $v$. It does not give uniform convergence on the evolving trained query family. That distinction is the central analytic issue in Chapter 8.

**Primary provenance.** `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§4.1–4.2 and 6.2; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§4 and 6.2.

### 6.7 The explicit operator–Hermite conditional Liouville PDE

It is useful to distinguish the source type of a column query, denoted $\eta$, from the type of the target row, denoted $\xi$; both have law $\mu$. For each depth $s$, time $t$, and target-row type $\xi$, let

$$
\rho_{s,t}^{\xi}(dw)
$$

be the conditional law of the current row coefficients

$$
w=(w_\nu)_{\nu\in\Lambda_{r_{\mathrm H}}}
\in\mathbb R^{P_{r_{\mathrm H}}}.
$$

Let $b(\eta,t)\in\mathbb R^d$ be the trained input-row field, $a(\eta,t)\in\mathbb R$ the trained readout field, and $h_q(s,\eta,t)$, $p_q(s,\eta,t)$ the slow forward and adjoint fields. Define

$$
H_{\nu q}(s,t)
=
\int\psi_\nu(\eta)
h_q(s,\eta,t)\,\mu(d\eta),
\tag{6.27}
$$

$$
z_q(s,\xi,w,t)
=
\sum_{\nu\in\Lambda_{r_{\mathrm H}}}
w_\nu H_{\nu q}(s,t),
\tag{6.28}
$$

$$
\beta_q(s,\xi,w,t)
=
\sigma'(z_q(s,\xi,w,t))
p_q(s,\xi,t).
\tag{6.29}
$$

The row-law characteristic velocity is

$$
\boxed{
V_\nu(s,\xi,w,t)
=-\gamma\sum_{q=1}^m
e_q^{(r_{\mathrm H})}(t)\,
\beta_q(s,\xi,w,t)
H_{\nu q}(s,t).
}
\tag{6.30}
$$

The conditional Liouville equation is

$$
\boxed{
\partial_t\rho_{s,t}^{\xi}
+
\nabla_w\!\cdot
\bigl(\rho_{s,t}^{\xi}V\bigr)
=0.
}
\tag{6.31}
$$

The coefficient domain is all of $\mathbb R^{P_{r_{\mathrm H}}}$, so there is no finite-$w$ boundary condition. The weak transport formulation conserves mass; the integrations by parts used below require the stated solution class to have sufficient moments and vanishing flux at infinity. The physical-depth boundary data are instead supplied by (6.33) and (6.35).

It is coupled to the forward depth equation

$$
\boxed{
\partial_s h_q(s,\xi,t)
=
\gamma\int
\sigma(z_q(s,\xi,w,t))
\rho_{s,t}^{\xi}(dw),
}
\tag{6.32}
$$

$$
h_q(0,\xi,t)
=b(\xi,t)^\top x_q,
\tag{6.33}
$$

and the shared-transpose adjoint equation

$$
\boxed{
-\partial_s p_q(s,\eta,t)
=
\gamma
\sum_{\nu\in\Lambda_{r_{\mathrm H}}}
\psi_\nu(\eta)
\int\mu(d\xi)
\int
w_\nu\beta_q(s,\xi,w,t)
\rho_{s,t}^{\xi}(dw),
}
\tag{6.34}
$$

$$
p_q(1,\eta,t)=a(\eta,t).
\tag{6.35}
$$

The boundary fields train by

$$
\boxed{
\dot b(\eta,t)
=-\sum_qe_q^{(r_{\mathrm H})}(t)
p_q(0,\eta,t)x_q,
}
\tag{6.36}
$$

$$
\boxed{
\dot a(\eta,t)
=-\sum_qe_q^{(r_{\mathrm H})}(t)
h_q(1,\eta,t).
}
\tag{6.37}
$$

Initialization is explicit:

$$
b(\eta,0)=\eta_{1:d},
\qquad
a(\eta,0)=A\eta_{d+1},
\tag{6.38}
$$

$$
\boxed{
\rho_{s,0}^{\xi}
=N(0,\sigma_w^2I_{P_{r_{\mathrm H}}})
}
\tag{6.39}
$$

for every $s,\xi$. The output and hidden Gram are direct current moments:

At finite $L$, distinct residual matrices are independent across the discrete depth index. The depth-continuum law above records their common local conditional marginal; using one common auxiliary row-noise variable to realize Lagrangian characteristics is only a coupling for analysis or quadrature and does not assert physical correlation between different depth locations.

$$
\boxed{
f_q^{(r_{\mathrm H})}(t)
=
\int a(\eta,t)h_q(1,\eta,t)\,\mu(d\eta),
}
\tag{6.40}
$$

$$
\boxed{
G_{qk}^{h,(r_{\mathrm H})}(s,t)
=
\int h_q(s,\eta,t)h_k(s,\eta,t)\,\mu(d\eta).
}
\tag{6.41}
$$

The mathematical source coordinate $(s,\xi,w)$ has dimension

$$
1+(d+1)+P_{r_{\mathrm H}}
=d+2+P_{r_{\mathrm H}},
$$

and there are finitely many coupled field species for fixed $m,d,r_{\mathrm H}$. This dimension is independent of $n$, $L$, and the requested training horizon. Numerical quadrature characteristics approximate integrals over this fixed source space; a large cubature point count is not a hidden physical network width.

**Primary provenance.** `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§4.3–4.4; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §4; `PDE_GENERALIZATION_FINAL_REPORT(2).md`, §3. Versions `(2)` and `(3)` of the generalization report are byte-identical.

### 6.8 Shared transpose, projected gradient, PSD kernel, and dissipation

For a slow field $v(\eta)$, define the current projected row action

$$
(W_{r_{\mathrm H}}v)(\xi,w)
=
\sum_{\nu\in\Lambda_{r_{\mathrm H}}}
w_\nu\langle\psi_\nu,v\rangle_\mu.
\tag{6.42}
$$

For a fast test field $\varphi(\xi,w)$, define

$$
(W_{r_{\mathrm H}}^\ast\varphi)(\eta)
=
\sum_{\nu\in\Lambda_{r_{\mathrm H}}}
\psi_\nu(\eta)
\int\mu(d\xi)\int
w_\nu\varphi(\xi,w)
\rho_{s,t}^{\xi}(dw).
\tag{6.43}
$$

Then

$$
\boxed{
\langle W_{r_{\mathrm H}}v,\varphi\rangle_{\mu\otimes\rho}
=
\langle v,W_{r_{\mathrm H}}^\ast\varphi\rangle_\mu.
}
\tag{6.44}
$$

Equation (6.34) is exactly the Hilbert adjoint of (6.32) under this pairing. No independent backward Gaussian is introduced.

Define

$$
G_{qk}^{p}(0)
=
\int p_q(0,\eta)p_k(0,\eta)\,\mu(d\eta),
$$

$$
G_{qk}^{\beta}(s)
=
\int\mu(d\xi)\int
\beta_q(s,\xi,w)\beta_k(s,\xi,w)
\rho_s^\xi(dw),
$$

and the projected hidden Gram

$$
G_{qk}^{h,r_{\mathrm H}}(s)
=
\sum_{\nu\in\Lambda_{r_{\mathrm H}}}
H_{\nu q}(s)H_{\nu k}(s).
\tag{6.45}
$$

We now give the blockwise calculation. Work in a Lagrangian characteristic lift of (6.31), so that

$$
w=\sigma_w\varepsilon+c,
\qquad
\dot c_\nu=V_\nu.
$$

Assume the forward and adjoint fields are differentiable in $t$ and $s$, the displayed moments are finite, and the weak Liouville equation has vanishing flux at $|w|=\infty$. Along a characteristic,

$$
\dot z_q
=
W_{r_{\mathrm H}}\dot h_q
+
\sum_{\nu}V_\nu H_{\nu q}.
$$

Linearizing (6.32) and pairing with $p_q$ gives

$$
\partial_s\langle p_q,\dot h_q\rangle_\mu
=
\langle\partial_sp_q,\dot h_q\rangle_\mu
+
\gamma\left\langle
p_q,
\mathbb E_{\rho}\!\left[
\sigma'(z_q)
\left(
W_{r_{\mathrm H}}\dot h_q+\sum_\nu V_\nu H_{\nu q}
\right)
\right]
\right\rangle_\mu.
$$

By (6.34) and the adjoint relation (6.44), the two terms containing
$W_{r_{\mathrm H}}\dot h_q$ cancel. Hence

$$
\partial_s\langle p_q,\dot h_q\rangle_\mu
=
\gamma
\int\mu(d\xi)\int\rho_s^\xi(dw)\,
\beta_q
\sum_\nu V_\nu H_{\nu q}.
$$

Integrating in depth and using $p_q(1)=a$ and
$\dot h_q(0,\eta)=\dot b(\eta)^\top x_q$ yields

$$
\langle a,\dot h_q(1)\rangle_\mu
=
\langle p_q(0),\dot b^\top x_q\rangle_\mu
+
\gamma\int_0^1
\mathbb E_{\mu\otimes\rho_s}
\left[
\beta_q\sum_\nu V_\nu H_{\nu q}
\right]ds.
$$

Since

$$
\dot f_q
=
\langle\dot a,h_q(1)\rangle_\mu
+
\langle a,\dot h_q(1)\rangle_\mu,
$$

substitution of (6.30), (6.36), and (6.37) gives, term by term,

$$
\dot f_q
=-\sum_k e_k
\left[
\langle h_q(1),h_k(1)\rangle_\mu
+
(x_q^\top x_k)
\langle p_q(0),p_k(0)\rangle_\mu
+
\gamma^2\int_0^1
\mathbb E[\beta_q\beta_k]
\sum_\nu H_{\nu q}H_{\nu k}\,ds
\right].
$$

This proves the exact same-system identity

$$
\boxed{
\dot f^{(r_{\mathrm H})}
=-\Theta_{r_{\mathrm H}}
e^{(r_{\mathrm H})},
}
\tag{6.46}
$$

$$
\boxed{
(\Theta_{r_{\mathrm H}})_{qk}
=
G_{qk}^h(1)
+
(x_q^\top x_k)G_{qk}^{p}(0)
+
\gamma^2\int_0^1
G_{qk}^{h,r_{\mathrm H}}(s)
G_{qk}^{\beta}(s)\,ds.
}
\tag{6.47}
$$

Each term is positive semidefinite; the backbone term is an integral of Schur products. Therefore

$$
\boxed{
\Theta_{r_{\mathrm H}}\succeq0,\qquad
\dot{\mathcal L}_{r_{\mathrm H}}
=
-(e^{(r_{\mathrm H})})^\top
\Theta_{r_{\mathrm H}}
e^{(r_{\mathrm H})}
\le0.
}
\tag{6.48}
$$

The stronger projected-gradient statement follows from the same calculation rather than from PSD alone. In the Lagrangian Hilbert metric for the trainable state $(b,a,c)$,

$$
\nabla_a\mathcal L=\sum_qe_qh_q(1),
\qquad
\nabla_b\mathcal L=\sum_qe_qp_q(0)x_q,
\qquad
(\nabla_c\mathcal L)_\nu
=
\gamma\sum_qe_q\beta_qH_{\nu q}.
$$

Equations (6.30), (6.36), and (6.37) are therefore

$$
\dot a=-\nabla_a\mathcal L,
\qquad
\dot b=-\nabla_b\mathcal L,
\qquad
\dot c=-\nabla_c\mathcal L.
$$

Consequently, on every interval where the regularity and no-flux hypotheses above hold,

$$
\boxed{
-\dot{\mathcal L}_{r_{\mathrm H}}
=
\|\dot a\|_{L^2(\mu)}^2
+
\|\dot b\|_{L^2(\mu;\mathbb R^d)}^2
+
\int_0^1
\mathbb E_{\mu\otimes\rho_s}
\|V(s)\|_2^2\,ds
=
e^\top\Theta_{r_{\mathrm H}}e.
}
$$

The backbone block in (6.47) uses the projected Gram $G^{h,r_{\mathrm H}}$, not the full slow Gram $G^h$. Replacing it by the latter would no longer be the sensitivity Gram of the same finite PDE.

Equations (6.44)–(6.48) and the block gradients above prove that the finite PDE is an exact Euclidean gradient system in its projected row-coordinate state. The state is still law-valued; “projected” refers to the finite source/operator coordinate, not to a finite number of scalar degrees of freedom. These identities do not prove that its projected tangent kernel equals the dense-limit tangent kernel or that $r_{\mathrm H}\to\infty$ converges.

**Primary provenance.** `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§4.3 and 4.5; `final_adversarial_pde_audit(1).md`, “Why this is genuinely a PDE” and Gates 6–8; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§4 and 6.1–6.3.

### 6.9 Autonomy, restartability, and well-posedness qualifications

The displayed state is

$$
\mathsf Y_{r_{\mathrm H}}(t)
=
\left(
b(\cdot,t),a(\cdot,t),
\{\rho_{s,t}^{\xi}\}_{s,\xi}
\right).
\tag{6.49}
$$

Where the coupled forward/backward depth problem has a unique solution, this state and the static model parameters let equations (6.27)–(6.35) reconstruct the current forward and adjoint fields, after which equations (6.30)–(6.37) determine the training velocity. No past trajectory or positive-time dense curve is an input. Thus the formulation is structurally autonomous and restartable on its well-posed solution class.

There are, however, three different restart statements:

1.  **Algebraic autonomy:** the right-hand side uses only the current PDE state. This follows directly from the displayed equations.
2.  **Numerical semigroup behavior:** for the implemented finite-cubature system, split integration and serialization/restart agree to roundoff, wrong static quadrature identities are rejected, and changed labels affect a positive-time state only through the new residual. This is experimentally established for the audited implementation.
3.  **Uniform mathematical restart theorem:** the same finite PDE is uniquely well posed on a neighborhood of physically reachable dense-limit restart states and approximates all their continuations. This is open.

Likewise, the phrase “at every finite cutoff” must carry the qualifier “wherever the boundary-value problem and Liouville flow are well posed.” A general global existence and uniqueness theorem, uniform over all declared data and all cutoffs, is not supplied by the project corpus. Loss dissipation is helpful but does not itself control every hidden law coordinate.

**Primary provenance.** `REPORT.md`, §§3 and 5; `final_adversarial_pde_audit(1).md`, Gates 5 and 15; `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§4.4–5 and 9.4–9.5.

### 6.10 Exact parity and the correct Hermite hierarchy

Assume:

- the activation $\sigma$ is odd, so $\sigma'$ is even;
- the source law $\mu$ is centered Gaussian;
- initialization is the symmetric one in (6.38)–(6.39); and
- the finite PDE solution is unique in the relevant class.

Let

$$
J_{\nu\nu}=(-1)^{|\nu|}.
$$

The PDE is equivariant under

$$
\bigl(b(\eta),a(\eta),\rho^\xi\bigr)
\longmapsto
\bigl(-b(-\eta),-a(-\eta),J_\#\rho^{-\xi}\bigr).
\tag{6.50}
$$

Initialization is fixed by this transformation, while the output

$$
f=\int ah\,d\mu
$$

and residual $e=f-y$ are invariant. Uniqueness therefore implies

$$
b(-\eta)=-b(\eta),\qquad
a(-\eta)=-a(\eta),
$$

$$
h_q(-\eta)=-h_q(\eta),\qquad
p_q(-\eta)=-p_q(\eta).
\tag{6.51}
$$

Since

$$
\psi_\nu(-\eta)=(-1)^{|\nu|}\psi_\nu(\eta),
$$

$$
H_{\nu q}
=\langle\psi_\nu,h_q\rangle_\mu
=(-1)^{|\nu|+1}H_{\nu q}.
$$

Hence

$$
\boxed{
H_{\nu q}=0
\quad\text{for every even }|\nu|.
}
\tag{6.52}
$$

Equation (6.30) then gives $V_\nu=0$ on every even shell. Its centered Gaussian row coordinate remains inert. Because $z$ and $\beta$ are independent of that inert coordinate, its centered first moment against $\beta$ vanishes, so it contributes neither to the forward action nor to the transpose.

For the canonical $d=3$ problem, the source and target-row copies satisfy $\eta,\xi\in\mathbb R^4$:

| maximum degree | full mode count $P$ | active odd modes |
|---------------:|--------------------:|-----------------:|
|              1 |                   5 |                4 |
|              2 |                  15 |                4 |
|              3 |                  35 |               24 |
|              4 |                  70 |               24 |
|              5 |                 126 |               80 |
|              7 |                 330 |              200 |

Therefore the first nontrivial ladder is

$$
\boxed{
P=5\longrightarrow35\longrightarrow126\longrightarrow330\longrightarrow\cdots,
}
\tag{6.53}
$$

not $5\to15\to35$. The earlier interpretation of $P=5\to15$ as a physical refinement is superseded. In the audited parity-null run, parity-paired cubature made $P=5$ and $P=15$ agree at approximately $10^{-17}$.

**Primary provenance.** `PDE_BRIDGEABILITY_RESOLUTION_REPORT.md`, §§1–4; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §4.1 and §§9.1–9.2. The bridgeability report supersedes the adverse hierarchy interpretation in `REPORT.md`, §4 and the preliminary warning in `PDE_LEAN_SALVAGE_REPORT.md`, §4.

### 6.11 Exact chronological response and the surviving role of the $K/J/N$ program

The operator–Hermite PDE is the only fully explicit width-independent PDE construction in the supplied residual-program corpus. A separate causal response calculus remains important, but its status is different.

Let

$$
v_r^\ell=\partial_t h_r^\ell,\qquad
A_r^\ell=\gamma D_r^\ell W_\ell.
$$

Differentiating (6.1) yields

$$
\boxed{
v_r^{\ell+1}
=
\left(I+\frac1L A_r^\ell\right)v_r^\ell
+\frac1L F_r^\ell,
}
\tag{6.54}
$$

where

$$
F_r^\ell
=-\gamma^2\sum_qe_q
D_r^\ell\beta_q^\ell G_{qr}^{h,\ell}.
\tag{6.55}
$$

Use the normalized neuron norm

$$
\|u\|_n=n^{-1/2}\|u\|_2.
$$

Separating label channels, define the direct forcing by

$$
q_{r\leftarrow q}^{0,\ell+1}
=
q_{r\leftarrow q}^{0,\ell}
-\frac{\gamma^2}{L}
D_r^\ell\beta_q^\ell
G_{qr}^{h,\ell},
\qquad
q_{r\leftarrow q}^{0,0}
=-(x_q^\top x_r)p_q^0,
\tag{6.56}
$$

and, for $k\ge1$,

$$
q_{r\leftarrow q}^{k,\ell+1}
=
q_{r\leftarrow q}^{k,\ell}
+\frac1L A_r^\ell
q_{r\leftarrow q}^{k-1,\ell},
\qquad
q_{r\leftarrow q}^{k,0}=0.
\tag{6.57}
$$

Then

$$
\partial_t h_r^\ell
=
\sum_qe_q\sum_{k\ge0}
q_{r\leftarrow q}^{k,\ell}.
\tag{6.58}
$$

For $w_r^\ell=\partial_t p_r^\ell$, direct differentiation of (6.5) gives

$$
w_r^\ell
=
\left(I+\frac1L(A_r^\ell)^\top\right)w_r^{\ell+1}
+\frac1L(\dot A_r^\ell)^\top p_r^{\ell+1},
\qquad
w_r^L=-\sum_qe_qh_q^L.
\tag{6.59}
$$

Separating $\dot A_r^\ell=\sum_qe_q(\dot A_r^\ell)_{\leftarrow q}$, define

$$
r_{r\leftarrow q}^{0,\ell}
=
r_{r\leftarrow q}^{0,\ell+1}
+\frac1L
\bigl((\dot A_r^\ell)_{\leftarrow q}\bigr)^\top
p_r^{\ell+1},
\qquad
r_{r\leftarrow q}^{0,L}=-h_q^L,
\tag{6.60}
$$

$$
r_{r\leftarrow q}^{k,\ell}
=
r_{r\leftarrow q}^{k,\ell+1}
+\frac1L(A_r^\ell)^\top
r_{r\leftarrow q}^{k-1,\ell+1},
\qquad
r_{r\leftarrow q}^{k,L}=0,
\quad k\ge1.
\tag{6.61}
$$

Then

$$
\partial_t p_r^\ell
=
\sum_qe_q\sum_{k\ge0}
r_{r\leftarrow q}^{k,\ell}.
\tag{6.62}
$$

Under the finite-time operator envelope

$$
\Lambda_T
=
\sup_{r,t\le T}
\frac1L\sum_{\ell=0}^{L-1}
\|A_r^\ell(t)\|_{\mathrm{op}}
<\infty,
\tag{6.63}
$$

and the source bound

$$
B_T
=
\sup_{r,t\le T}
\left(
\|v_r^0(t)\|_n
+\frac1L\sum_{\ell=0}^{L-1}
\|F_r^\ell(t)\|_n
\right),
\tag{6.64}
$$

define the grade-$k$ aggregate

$$
v_r^{[k],\ell}(t)
=
\sum_q e_q(t)\,
q_{r\leftarrow q}^{k,\ell}(t).
\tag{6.64a}
$$

The exact ordered-simplex estimate gives

$$
\boxed{
\sup_{r,\ell,t\le T}
\left\|
v_r^\ell-\sum_{k=0}^{K}v_r^{[k],\ell}
\right\|_n
\le
B_T
\sum_{j>K}\frac{\Lambda_T^j}{j!}
\le
B_Te^{\Lambda_T}
\frac{\Lambda_T^{K+1}}{(K+1)!}.
}
\tag{6.65}
$$

No commutativity, normality, or training-time analyticity is used. The backward hierarchy has the same bound when its differentiated source is held exact. If that source is recomputed from a truncated forward velocity, an additional term

$$
e^{\Lambda_T}E_{A,K,T}
\tag{6.66}
$$

must be controlled, where one admissible source-defect norm is

$$
E_{A,K,T}
=
\sup_{r,t\le T}
\frac1L\sum_{\ell=0}^{L-1}
\left\|
\left(
\dot A_r^\ell(t)-\dot A_{r,K}^\ell(t)
\right)^\top
p_r^{\ell+1}(t)
\right\|_n.
\tag{6.66a}
$$

Here $\dot A_{r,K}$ is the differentiated source recomputed from the grade-$K$ forward approximation. The factorial tail therefore controls pure chronological propagation, not every nonlinear source substitution, cavity contraction, or high-to-low feedback term.

The proposed $K/J/N$ program separates:

- $K$: chronological response depth;
- $J$: nonlinear differentiation/tree complexity;
- $N$: depth or numerical resolution;
- optional historical coefficients that would Markovize the learned part of the reused matrices.

Its exact finite-network $q/r$ recurrences, orientation grammar, Gaussian row/column conditioning identities, and factorial pure-propagator tail survive audit. Its earlier claim to have emitted a complete finite compiler does not: the required tag tables, historical coordinates, conditional kernel, and finite drift DAGs were not actually produced. It is therefore a causal mechanism and a response-enrichment blueprint, not a second implemented PDE.

**Primary provenance.** `dense_euclidean_continuous_depth_pde_conjecture(1).md`, §§5–7 and 10–12; `dense_euclidean_continuous_depth_npde_audit.md`, §§5.1 and 7; `REPORT.md`, §1; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§13.2–13.4. The latest master and `REPORT.md` supersede the earlier claim that the prose compiler was executable.

### 6.12 Chapter-level claim ledger

| Claim                                                                  | Status                          | Exact scope                                                                                                    |
|------------------------------------------------------------------------|---------------------------------|----------------------------------------------------------------------------------------------------------------|
| Equations (6.5)–(6.11)                                                 | **Proved**                      | Every finite $n,L$ network under the stated parameterization                                                   |
| Finite-network PSD tangent kernel and loss dissipation                 | **Proved**                      | Same finite network and Euclidean block metric                                                                 |
| Raw iid layer matrices converge to a nondegenerate smooth $W(s)$       | **False as stated**             | Strong interpolation of iid step matrices; an emergent effective law is not excluded                           |
| One-time Grams or ordinary row marginals exactly close dense reuse     | **False in general**            | Restart classes containing the continuation witness                                                            |
| Equations (6.31)–(6.41) define an explicit finite-source PDE           | **Established construction**    | Fixed $m,d,r_{\mathrm H}$                                                                                      |
| Shared transpose, projected-gradient identity, PSD kernel, dissipation | **Exact internal PDE theorems** | Wherever the finite flow and boundary problem are sufficiently regular and well posed                          |
| Structural autonomy of the PDE                                         | **Exact from the equations**    | Current PDE state determines the displayed drift                                                               |
| Global well-posedness uniformly in cutoff and data                     | **Open**                        | Not supplied by the finite-PDE identities                                                                      |
| Odd-parity reduction                                                   | **Proved**                      | Odd activation, symmetric initialization, uniqueness                                                           |
| Pure chronological factorial tail                                      | **Proved**                      | Finite-time operator envelope; exact backward source                                                           |
| Full $K/J/N$ finite compiler                                           | **Superseded/unsupported**      | Exact response algebra survives; complete finite drift was not emitted                                         |
| Finite PDE equals the ordered dense limit                              | **Open**                        | Requires width limit, trained depth homogenization, conditional/Onsager identification, and cutoff convergence |

## Chapter 7 — Empirical evidence, mechanism tests, and the Hermite-hierarchy audit

### 7.1 What the experiments can and cannot establish

The empirical program tests five logically different questions:

1.  **Literalness:** was a width-independent PDE, rather than a finite matrix surrogate, actually integrated?
2.  **Internal correctness:** does the implemented finite PDE satisfy the equations and geometric identities derived in Chapter 6?
3.  **Descriptive accuracy:** does one fixed low-order PDE track finite dense-network outputs, loss, and hidden-Gram motion?
4.  **Mechanism:** can the agreement be explained by lazy features, identity activation, a scalar training clock, or a fixed linear gain?
5.  **Hierarchy and identification:** do higher source cutoffs converge, and does the PDE equal the ordered $n\to\infty$, then $L\to\infty$ dense target?

The first two questions have passed strong algebraic and implementation audits for the finite-cubature realization. The third and fourth have substantial positive evidence on the tested regimes. The fifth remains open.

Unless explicitly stated otherwise, a “gap” is a maximum over the saved training-time/depth grid, not a certified continuous supremum. Gram-increment comparisons subtract each system’s own initialization:

$$
\Delta G(s,t)=G(s,t)-G(s,0).
\tag{7.1}
$$

This removes static finite-width initialization offsets and isolates learned feature evolution. The mathematical conjecture, however, concerns absolute ordered-limit Grams, so an increment match is not itself the final theorem norm.

No new experiment is introduced in this chapter, and Version 2.2 does not replace any frozen numerical value. All values below remain inherited from the frozen reports and their source-level audits. The active repository now contains executable code, configurations, tests, and processed or sealed evidence for most numerical programs. A later macOS ARM64 run independently re-executed the central \(P=5\) PDE and its authenticated continuation from \(t=8\) to \(t=32\), reproducing the archived scalar plateau diagnostics to floating-point precision. It did not regenerate the full refinement grid or the 128-member canonical dense ensemble. Several compact releases also continue to omit their large raw trajectory collections. The empirical claims below therefore retain their original frozen evidentiary scope; Appendix C.4 maps them to the active repository, and Appendix D.9 records the later execution audit without treating it as new validation evidence.

**Primary provenance.** `REPORT.md`; `final_adversarial_pde_audit(1).md`; `PDE_GENERALIZATION_FINAL_REPORT(2).md`; `ACTIVATION_LINEARITY_SMOKING_GUN_REPORT.md`; `PDE_LEAN_SALVAGE_REPORT.md`; `PDE_BRIDGEABILITY_RESOLUTION_REPORT.md`; `PDE_HIGH_TO_LOW_TAIL_ROUND_REPORT.md`; `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`; `SCALAR_HERMITE_MINIMAL_EXPERIMENT_REPORT.md`.

### 7.2 Literal-PDE, algebra, autonomy, and anti-oracle gates

The primary finite PDE used complete source degree one in the four-dimensional immutable label:

$$
r_{\mathrm H}=1,\qquad P=5,
\qquad N=16,\qquad M=256,\qquad R=128.
\tag{7.2}
$$

Here $N$ is numerical depth resolution, $M$ is immutable-label cubature resolution, and $R$ is row-innovation cubature resolution. The mathematical PDE contains no network width $n$, original residual depth $L$, or $n\times n$ matrix.

The following gates passed.

| Gate                       | Audited result                                                                                                                          |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| No microscopic dense state | The PDE stores only source/depth characteristic fields and row coefficients; no two-neuron-index matrix is allocated                    |
| Explicit drift             | Liouville velocity, forward field, adjoint, $b$-flow, $a$-flow, initialization, and moment readouts are fully specified                 |
| Shared transpose           | Pairing defect was at roundoff; an intentionally independent-transpose mutation was detected                                            |
| Coordinate gradient        | Generic positive-time coordinate-gradient defect at most $1.41\times10^{-11}$                                                           |
| Energy identity            | Defect $7.62\times10^{-13}$                                                                                                             |
| Output identity            | Across 20 perturbed states, maximum $\dot f+\Theta e$ directional defect $1.70\times10^{-10}$                                           |
| PSD kernel                 | $\Theta_P\succeq0$ in every audited state                                                                                               |
| Restart                    | Direct and split/serialized continuations agreed to $4.44\times10^{-16}$                                                                |
| Changed target             | At a fixed positive-time state, the velocity change followed the new residual with maximum linearity defect $4.44\times10^{-16}$        |
| Static-state integrity     | A same-shape wrong quadrature seed was rejected by the compiler/quadrature hash                                                         |
| Independent implementation | Two characteristic solvers agreed to $2.78\times10^{-16}$ in outputs and $8.88\times10^{-16}$ in all Gram entries under common cubature |
| Anti-oracle separation     | PDE code did not import or read dense trajectories; dense references entered only in post hoc comparison                                |

Changing the target at one serialized state altered the $b,a,c$ velocity with norms $1.107,1.103,7.198$, respectively, where $c$ is the learned row-coordinate displacement in the characteristic implementation. The current forward and adjoint fields were unchanged at the instant of relabeling, as the equations require. Continuing for $0.2$ training-time units under the changed target reduced loss monotonically from $0.2950$ to $0.07587$. This is an internal autonomy test, not a dense/PDE transfer theorem for arbitrary labels.

**Conclusion.** A literal, autonomous, width-independent finite PDE was integrated correctly. This establishes the construction and its internal finite-cutoff structure, not its identification with the dense limit.

**Primary provenance.** `final_adversarial_pde_audit(1).md`, Hard Gates 1–10 and “Evidence that is strong”; `REPORT.md`, §§1 and 5.

### 7.3 Canonical dense/PDE benchmark

The primary comparison used the fixed $P=5$ PDE and a pooled dense reference with

$$
n=256,\qquad L=32,\qquad S=128\ \text{independent networks}.
$$

The central results are:

| Quantity                                |                 Value |
|-----------------------------------------|----------------------:|
| PDE feature motion                      |           $0.6338011$ |
| Dense feature motion                    |            $0.639909$ |
| Maximum output gap                      | $1.0753\times10^{-2}$ |
| Maximum loss-of-ensemble-mean gap       | $1.8457\times10^{-3}$ |
| Maximum absolute-Gram gap               | $1.9408\times10^{-2}$ |
| Maximum Gram-increment surface gap      | $7.2433\times10^{-3}$ |
| Gram-increment gap / PDE feature motion |            $1.1428\%$ |
| Maximum tangent-kernel gap              | $3.3404\times10^{-2}$ |

The primary Gram-increment discrepancy was statistically resolved relative to finite-reference sampling error. The pooled and block-stratified curvewise 95% thresholds were

$$
5.0620\times10^{-3},
\qquad
4.9812\times10^{-3},
$$

with centered-bootstrap tail probabilities

$$
\widehat p=0.00300,\qquad0.00350.
$$

Leave-one-block-out Gram gaps ranged from

$$
6.731\times10^{-3}
\quad\text{to}\quad
7.852\times10^{-3}.
$$

Thus “close but distinguishable at this finite $(n,L,P,N,M,R)$” is supported. “Exact,” “statistically indistinguishable,” and “below the noise floor” are not.

The discrepancy is small relative to the $O(1)$ representation motion. Consequently the agreement cannot be explained by both systems remaining nearly static.

**Primary provenance.** `REPORT.md`, §2 and §5; `final_adversarial_pde_audit(1).md`, Executive Verdict and “Enlarged $n=256,L=32$ reference”; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §7.1.

### 7.4 Through-plateau prediction and late-time evidence

The primary PDE was integrated through the active transient to $t=8$, serialized, restarted from its autonomous state, and continued without changing cutoff or coefficients to $t=32$. On $8\le t\le32$:

| Plateau quantity        |               Maximum |
|-------------------------|----------------------:|
| output drift from $t=8$ | $4.996\times10^{-13}$ |
| all-depth Gram drift    | $4.236\times10^{-13}$ |
| tangent-kernel drift    | $4.168\times10^{-13}$ |
| residual norm           | $4.996\times10^{-13}$ |
| $\lvert\dot{\mathcal L}\rvert$ | $8.253\times10^{-25}$ |

A later reanalysis compared earlier and later windows:

| System                           | observable drift on $[2,4]$ | observable drift on $[4,8]$ |               ratio |
|----------------------------------|----------------------------:|----------------------------:|--------------------:|
| dense $n=128,L=32$, 16-seed mean |        $5.413\times10^{-4}$ |        $6.920\times10^{-7}$ | $1.28\times10^{-3}$ |
| $P=5$ PDE                        |        $4.833\times10^{-4}$ |        $3.040\times10^{-7}$ | $6.29\times10^{-4}$ |

The endpoint residual norms at $t=8$ were $4.99\times10^{-12}$ for the dense mean and $5.40\times10^{-13}$ for the PDE.

These facts rule out the interpretation of the simulated PDE as a short local training-time Taylor fit. They do not prove

$$
\sup_{t\ge0}d_{\mathrm{obs}}<\varepsilon.
$$

Dense ensembles were directly compared principally through $t=8$, finite-time flatness is not a literal $t\to\infty$ bound, and no worst-direction restart-neighborhood stability theorem was tested.

**Primary provenance.** `REPORT.md`, §3; `final_adversarial_pde_audit(1).md`, Gate 15 and “Nonlocal-in-training-time behavior”; `PDE_LEAN_SALVAGE_REPORT.md`, §6.

### 7.5 Numerical-resolution and statistical validity gates

Time integration was negligible at the principal dense/PDE discrepancy scale:

| Comparison                |               Output |       all-depth Gram |       tangent kernel |
|---------------------------|---------------------:|---------------------:|---------------------:|
| RK4 $dt=.02$ vs. $.01$    | $6.826\times10^{-8}$ | $1.090\times10^{-7}$ | $3.559\times10^{-7}$ |
| RK4 $dt=.01$ vs. $.005$   | $4.179\times10^{-9}$ | $6.670\times10^{-9}$ | $2.177\times10^{-8}$ |
| Heun vs. RK4 at $dt=.005$ | $1.727\times10^{-5}$ | $1.555\times10^{-5}$ | $4.442\times10^{-5}$ |

Depth refinement against $N=32$ gave:

| $N$ |               Output |       all-depth Gram |       tangent kernel |
|----:|---------------------:|---------------------:|---------------------:|
|   8 | $6.108\times10^{-4}$ | $2.521\times10^{-3}$ | $1.970\times10^{-2}$ |
|  16 | $2.051\times10^{-4}$ | $8.449\times10^{-4}$ | $6.628\times10^{-3}$ |

Relative to the primary $M=256,R=128$ cubature:

| Cubature change |               Output |       all-depth Gram |       tangent kernel |
|-----------------|---------------------:|---------------------:|---------------------:|
| $M=64,R=32$     | $7.330\times10^{-3}$ | $1.274\times10^{-2}$ | $1.214\times10^{-1}$ |
| $M=128,R=64$    | $3.586\times10^{-3}$ | $6.382\times10^{-3}$ | $1.012\times10^{-1}$ |
| $M=512,R=128$   | $1.526\times10^{-4}$ | $7.832\times10^{-4}$ | $6.323\times10^{-3}$ |
| $M=256,R=256$   | $1.118\times10^{-4}$ | $1.160\times10^{-3}$ | $6.321\times10^{-3}$ |

Three independent primary-resolution QMC scrambles had pairwise radii

$$
1.32\times10^{-3}\ \text{in output},\qquad
2.13\times10^{-3}\ \text{in all-depth Grams}.
$$

The low-order tensor Gauss–Hermite rule agreed with the independent implementation under identical cubature but differed from refined QMC by $1.94\times10^{-2}$ in Grams. It is therefore an implementation cross-check, not the primary accuracy rule.

The later $P=5$, $M=625,N=16,R=256$ proof-obligation scrambles differed by only

$$
d_{\mathrm{obs}}=3.3542\times10^{-4}=0.0335\%.
$$

This is favorable low-order numerical consistency. It does not certify a cofinal high-$P$, high-$M,R,N$ sequence.

**Primary provenance.** `REPORT.md`, §4; `final_adversarial_pde_audit(1).md`, Gates 11–12; `PDE_PROOF_OBLIGATION_STUDY_FROZEN_REPORT.md`, “Evidence present at freeze”; `PDE_LEAN_SALVAGE_REPORT.md`, §7.

### 7.6 Finite-grid width/depth evidence and its limits

The surviving finite-reference ladder is:

| Dense reference    |           output gap |     loss-of-mean gap |    absolute-Gram gap |   Gram-increment gap | dense feature motion |
|--------------------|---------------------:|---------------------:|---------------------:|---------------------:|---------------------:|
| $n=64,L=32,S=64$   | $4.311\times10^{-2}$ | $2.066\times10^{-2}$ | $9.001\times10^{-2}$ | $2.464\times10^{-2}$ | $6.419\times10^{-1}$ |
| $n=96,L=32,S=48$   |                    — |                    — |                    — | $1.169\times10^{-2}$ |                    — |
| $n=128,L=32,S=96$  | $1.818\times10^{-2}$ | $3.778\times10^{-3}$ | $4.115\times10^{-2}$ | $9.255\times10^{-3}$ | $6.285\times10^{-1}$ |
| $n=256,L=32,S=64$  | $1.708\times10^{-2}$ | $1.498\times10^{-3}$ | $2.787\times10^{-2}$ | $6.731\times10^{-3}$ | $6.392\times10^{-1}$ |
| $n=256,L=32,S=128$ | $1.075\times10^{-2}$ | $1.846\times10^{-3}$ | $1.941\times10^{-2}$ | $7.243\times10^{-3}$ | $6.399\times10^{-1}$ |
| $n=256,L=64,S=64$  | $1.660\times10^{-2}$ | $3.318\times10^{-3}$ | $3.766\times10^{-2}$ | $6.564\times10^{-3}$ | $6.386\times10^{-1}$ |
| $n=512,L=32,S=16$  | $2.398\times10^{-2}$ | $1.987\times10^{-2}$ | $3.868\times10^{-2}$ | $9.897\times10^{-3}$ | $6.351\times10^{-1}$ |

The decrease through $n=256$ is favorable. The $n=512$ ensemble is much smaller and does not continue the monotone curvewise trend.

The preregistered L-shaped exact-network Cauchy audit gave:

| Finite step             | Gram-increment Cauchy gap |  pooled 95% threshold | stratified 95% threshold | Decision     |
|-------------------------|--------------------------:|----------------------:|-------------------------:|--------------|
| $n:256\to512$ at $L=32$ |     $9.3504\times10^{-3}$ | $9.9672\times10^{-3}$ |   $1.03062\times10^{-2}$ | not resolved |
| $L:32\to64$ at $n=256$  |     $4.2263\times10^{-3}$ | $8.5680\times10^{-3}$ |    $8.9785\times10^{-3}$ | not resolved |

Failure to resolve a finite difference is not proof that it vanishes. There is no $(512,64)$ point, second width step at fixed depth, second depth step, or rigorous extrapolation.

A separate reduced four-root diagnostic through $T=0.5$ found:

| Depth | $D_{64\to128}$ | $D_{128\to256}$ |   ratio |
|------:|---------------:|----------------:|--------:|
|     8 |      $0.10596$ |       $0.04891$ | $0.462$ |
|    16 |      $0.09609$ |       $0.04685$ | $0.488$ |
|    32 |      $0.09079$ |       $0.04707$ | $0.518$ |

At $n=256$,

$$
D_{8\to16}=0.02212,\qquad
D_{16\to32}=0.01278,\qquad
\frac{D_{16\to32}}{D_{8\to16}}=0.578.
$$

Every root contracted at those scales. Geometric continuation still suggested unresolved tails of approximately $4.2\%$–$5.1\%$ in width and $1.75\%$ in depth. These are directional finite-grid diagnostics, not identification of (6.15).

**Primary provenance.** `final_adversarial_pde_audit(1).md`, “Width trend,” “Preregistered L-shaped width/depth audit,” and Blocker 1; `PDE_LEAN_SALVAGE_REPORT.md`, §1.

### 7.7 Broad transfer without retuning

The same smallest useful degree-one PDE was tested on 14 preregistered configurations. In this study

$$
P=5,\quad N=16,\quad M=81
\ \text{(order-three tensor Gauss–Hermite)},\quad
R=128,\quad dt=0.02,\quad T=32.
\tag{7.3}
$$

No case-specific coefficient was fitted and $P$ did not grow with sample count $m$.

The normalized full-curve metrics were

$$
E_G
=
\frac{
\sup_{t,s}\|\Delta G_{\mathrm{PDE}}(s,t)-\Delta G_{\mathrm{dense}}(s,t)\|_F
}{
\max\{
\sup\|\Delta G_{\mathrm{PDE}}\|_F,
\sup\|\Delta G_{\mathrm{dense}}\|_F,
0.05
\}
},
\tag{7.3a}
$$

$$
E_f
=
\frac{
\sup_t\|\Delta f_{\mathrm{PDE}}(t)-\Delta f_{\mathrm{dense}}(t)\|_2
}{
\max\{
\|y\|_2,
\sup\|\Delta f_{\mathrm{PDE}}\|_2,
\sup\|\Delta f_{\mathrm{dense}}\|_2,
0.1
\}
},
\tag{7.3b}
$$

$$
E_{\mathcal L}
=
\frac{
\sup_t|\mathcal L_{\mathrm{PDE}}(t)
-\mathcal L_{\mathrm{dense\,mean}}(t)|
}{
\max\{
\mathcal L_{\mathrm{PDE}}(0),
\mathcal L_{\mathrm{dense\,mean}}(0),
0.1
\}
}.
\tag{7.3c}
$$

The B0 anchor below uses the generalization study’s $n=128,L=32,S=32$ reference and its own fixed cubature, so its $1.81\%$ normalized Gram error is not the same statistic as the $1.1428\%$ canonical $n=256,L=32,S=128$ effect-size ratio in §7.3.

| Case | Modification                            |     Gram |   Output |     Loss | PDE numerics | two-window plateau |
|------|-----------------------------------------|---------:|---------:|---------:|--------------|--------------------|
| B0   | canonical $\tanh$ anchor                | $1.81\%$ | $1.34\%$ | $0.39\%$ | pass         | pass               |
| Y1   | label perturbation of norm $0.05$       | $1.26\%$ | $1.47\%$ | $1.41\%$ | pass         | pass               |
| Y2   | equal positive labels at original norm  | $1.56\%$ | $1.33\%$ | $0.95\%$ | pass         | pass               |
| Y3   | one-coordinate label at original norm   | $1.24\%$ | $1.47\%$ | $0.95\%$ | pass         | pass               |
| Y4   | doubled original labels                 | $0.95\%$ | $0.74\%$ | $0.70\%$ | pass         | pass               |
| X1   | generic asymmetric unit-vector geometry | $2.46\%$ | $1.53\%$ | $0.56\%$ | unresolved   | pass               |
| X2   | pairwise input correlation $0.85$       | $2.55\%$ | $1.59\%$ | $0.46\%$ | unresolved   | final window only  |
| M2   | two orthogonal samples                  | $1.62\%$ | $1.18\%$ | $0.46\%$ | pass         | pass               |
| M4   | four samples                            | $4.14\%$ | $1.51\%$ | $0.55\%$ | unresolved   | not flat by $32$   |
| M5   | five samples                            | $3.11\%$ | $1.83\%$ | $1.97\%$ | unresolved   | not flat by $32$   |
| A1   | normalized erf                          | $1.34\%$ | $1.46\%$ | $1.38\%$ | pass         | pass               |
| A2   | normalized arctangent                   | $1.52\%$ | $1.31\%$ | $0.31\%$ | pass         | pass               |
| I1   | correlated inputs and doubled labels    | $2.10\%$ | $1.04\%$ | $0.44\%$ | unresolved   | pass               |
| I2   | $m=5$ with normalized erf               | $2.44\%$ | $1.68\%$ | $1.96\%$ | unresolved   | not flat by $32$   |

Across all cases:

| Full-curve normalized metric |   Median |  Maximum |
|------------------------------|---------:|---------:|
| all-depth Gram increment     | $1.71\%$ | $4.14\%$ |
| output increment             | $1.46\%$ | $1.83\%$ |
| loss                         | $0.63\%$ | $1.97\%$ |

Every dense reference exhibited active feature learning, and the PDE/dense feature-motion ratio stayed in

$$
[0.977,1.023].
$$

The label cases are the cleanest anti-tuning evidence: all passed numerical and plateau gates, with maximum Gram/output/loss errors $1.56\%/1.47\%/1.41\%$.

The formal decision was nevertheless “boundary or unresolved,” not “uniform pass.” The global simultaneous one-sided 95% upper critical value was $5.94006\%$, already larger than the $5\%$ equivalence margin. Six cases failed at least one PDE-resolution gate, and four did not pass both plateau windows. No material counterexample was found, but category-wide certification over an infinite data/activation class is not established.

**Primary provenance.** `PDE_GENERALIZATION_FINAL_REPORT(2).md`, §§2–10 and §12. `PDE_GENERALIZATION_FINAL_REPORT(3).md` is byte-identical. Summary reconciliation: `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §7.2.

### 7.8 Nonlazy and nonlinear mechanism controls

The empirical success could have been less interesting for several different reasons. The controls address them one by one.

**Lazy or frozen features.** The canonical PDE Gram moved by $0.6338$, and all 14 transfer cases had active feature motion. This explanation is rejected on the tested regimes.

**Identity/deep-linear activation.** For

$$
\sigma_c(z)=\frac{\tanh(cz)}c,\qquad \sigma_0(z)=z,
$$

the global Gram results were:

| nonlinear case | dense distance from identity | matched nonlinear PDE error | identity PDE used on nonlinear target |
|----------------|-----------------------------:|----------------------------:|--------------------------------------:|
| $c=1$          |                    $22.44\%$ |                    $1.20\%$ |                             $21.38\%$ |
| $c=2$          |                    $36.38\%$ |                    $1.09\%$ |                             $35.37\%$ |
| $c=4$          |                    $45.82\%$ |                    $1.18\%$ |                             $44.83\%$ |

For the preregistered $c=2$ confirmatory Gram test, the dense separation had one-sided 95% lower bound $35.27\%$, while the matched PDE error had upper bound $1.09\%$. Exact identity/deep-linear dynamics are decisively rejected for the learned Gram. The output test also passed; the deliberately stronger loss rule did not.

**Scalar training clock.** Reparameterizing the $c=0$ and $c=2$ Gram paths by fractional loss progress left a $27.14\%$ dense separation, with 95% lower bound $25.91\%$, while the PDE activation-contrast error was $1.34\%$. A scalar time-rescaling explanation is rejected.

**Fixed gain-matched linearity.** The first $c=2$ test left a real loophole. The non-oracular initialization-Gaussian gain

$$
\kappa_2
=\mathbb E[\operatorname{sech}^2(1.3Z)]
=0.5101185599716273
$$

produced a trained linear control only $3.46\%$ from the nonlinear dense Gram, with interval $3.25\%$–$3.67\%$. The nonlinear PDE remained more accurate by a factor $3.16$, but the linear control stayed inside the project’s $5\%$ tolerance.

The later scalar stress used the theory-selected smooth, odd, bounded, 1-Lipschitz activation

$$
\boxed{
\sigma(z)=\frac{\sin(2.5z)}{2.5}.
}
\tag{7.4}
$$

At initialization, $62.14\%$ of its Gaussian $L^2$ energy lies outside the best zero-intercept linear component. The results were:

| Comparison                                                |      Gram |   Output |     Loss |
|-----------------------------------------------------------|----------:|---------:|---------:|
| initialization-gain linear control vs. degree-11 sine PDE | $17.70\%$ | $7.12\%$ | $7.51\%$ |
| RMS-gain linear control vs. sine PDE                      |  $8.68\%$ | $3.95\%$ | $4.68\%$ |
| paired dense initialization-gain linear vs. dense sine    | $15.95\%$ | $6.55\%$ | $6.95\%$ |
| degree-11 sine PDE vs. dense sine                         |  $2.50\%$ | $2.81\%$ | $5.54\%$ |

All eight paired dense seeds had Gram separation between $14.40\%$ and $18.75\%$. Thus the tested fixed initialization-gain explanation is rejected directly in dense Gram dynamics. The RMS-gain control is rejected relative to the nonlinear PDE path but was not separately run as a paired dense control. Adaptive, time-dependent, or state-dependent linear surrogates remain outside the scope of the test. The PDE loss error $5.54\%$ also prevents a joint all-three-metrics $5\%$ claim.

The sine dense comparison is an eight-seed paired diagnostic, not a separately bootstrapped category-wide confidence statement. Its force comes from the large separation and the fact that every paired seed exceeded the $5\%$ Gram threshold.

Finally, a low source degree is not a linear activation approximation. Every cutoff evaluates the full $\sigma(z)$ and $\sigma'(z)$; the cutoff resolves dependence on the immutable Gaussian neuron label. The sine experiment demonstrates the separation:

$$
\text{linear-control Gram gap}=17.70\%,
\qquad
\text{degree-1 to degree-11 source gap}=0.339\%.
$$

**Primary provenance.** `ACTIVATION_LINEARITY_SMOKING_GUN_REPORT.md`, §§2–10; `SCALAR_HERMITE_MINIMAL_EXPERIMENT_REPORT.md`, §§2–6 and §8; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §8.

### 7.9 Trained-depth homogenization and state-sufficiency diagnostics

Two related paired-layer experiments support the expected $L^{-1}$ centered variance.

The original direct-PDE study paired dense runs with common $B(0),a(0)$ and independently redrawn $W_\ell$’s:

| Field         | initialization variance slope | slope after training to $t=0.5$ |
|---------------|------------------------------:|--------------------------------:|
| hidden field  |                     $-1.0193$ |                       $-1.0039$ |
| input adjoint |                     $-0.9993$ |                       $-0.9924$ |

A later reduced diagnostic obtained

$$
\mathfrak s_{\mathrm{forward}}=-1.00219,\qquad
\mathfrak s_{\mathrm{backward}}=-0.99982
\tag{7.5}
$$

at $t=0.5$, with RMS slopes $-0.50110$ and $-0.49991$. These results strongly support cancellation of centered fast-depth innovations.

They do not identify the conditional/shared-transpose mean. A common missing mean term can survive while centered variance decays exactly as $L^{-1}$.

The same-state attack altered all $16$ dense layers while preserving the retained $P=5,15,35$ row coordinates and current forward fields, adjoints, output, Grams, and tangent kernel to relative defect at most

$$
5.28\times10^{-16}.
$$

At the strongest coherent perturbation, the normalized future observable gap was

$$
0.00120\quad\text{after }0.1,\qquad
0.00332\quad\text{after }0.5.
\tag{7.6}
$$

No gross projectability counterexample was found. This is one reduced cell, root, and perturbation family. A null attack is one-sided evidence and does not prove that the static operator state is sufficient.

**Primary provenance.** `REPORT.md`, §6; `PDE_LEAN_SALVAGE_REPORT.md`, §§2–3; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§7.3–7.4.

### 7.10 Chronological-response evidence

The finite-matrix response experiments retain every dense $W_\ell$ and are therefore not admissible finite PDEs. They test whether the exact causal-response expansion and its coupled-source remainder from (6.54)–(6.66a) are numerically compressible.

Across 16 completed long-horizon runs:

| response grade $K$ |            output error, median / max |    all-depth Gram error, median / max |
|-------------------:|--------------------------------------:|--------------------------------------:|
|                  0 | $8.51\times10^{-3}/1.58\times10^{-2}$ | $2.50\times10^{-2}/5.19\times10^{-2}$ |
|                  1 | $2.38\times10^{-4}/1.40\times10^{-3}$ | $1.88\times10^{-3}/3.62\times10^{-3}$ |
|                  2 | $1.42\times10^{-5}/5.71\times10^{-5}$ | $1.18\times10^{-4}/5.52\times10^{-4}$ |
|                  3 | $9.77\times10^{-7}/6.25\times10^{-6}$ | $6.08\times10^{-6}/5.93\times10^{-5}$ |

Every exact and fixed-$K$ trajectory passed the operational plateau test through $t=32$, and no new prefix-error maximum appeared after $t=16$.

An earlier ten-state instantaneous test used P06's older nearby convention—$h(0)=\tanh(Bx)$, $B_{ij}\sim N(0,d^{-1})$, and residual scale one—not the canonical Chapter 6 initialization. It found median forward/backward relative errors decreasing from roughly $8\times10^{-2}$ at $K=0$, to $5\times10^{-3}$ at $K=1$, $3\times10^{-4}$ at $K=2$, and $1.6\times10^{-5}$ at $K=3$. Positive-time restarts showed the same hierarchy. These results agree with the exact factorial pure-propagator mechanism, while not measuring the full width-independent outgoing residual.

One qualification is essential. In the older truncated-response diagnostic, the plotted positive-semidefinite reconstruction was $S_MS_M^\top$, whereas the approximate-adjoint trajectory actually uses the cross-kernel $SS_M^\top$. The latter need not be symmetric or positive semidefinite. Those runs therefore cannot borrow the exact gradient-flow, PSD, or dissipation theorem of the operator–Liouville PDE; they are response-accuracy diagnostics only.

**Conclusion.** Low chronological response grade is a strong empirical causal-compression mechanism. The experiment does not show that the dense matrices can be removed, that the response history has a finite Markov realization, or that the response-enriched PDE converges.

**Primary provenance.** `dense_euclidean_continuous_depth_pde_conjecture(1).md`, §§11.2–11.6; `dense_euclidean_continuous_depth_npde_audit.md`, §§7.5–7.11; `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §7.7; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §13.4.

### 7.11 Parity correction and the first proper odd-shell test

The original operator-order interpretation compared $P=5$, $15$, and $35$ as three successive physical cutoffs. Chapter 6 proved that this is invalid for the odd/symmetric model: $P=5$ and $P=15$ are the same exact PDE. Unpaired numerical cubature created symmetry leakage, and the apparent $5\to15$ denominator was not a physical truncation error.

After exact parity pairing, the even-shell null was:

|   Time | $P=5$ vs. $P=15$ observable distance |    backward residual |    outgoing residual |
|-------:|-------------------------------------:|---------------------:|---------------------:|
| $0.25$ |                 $2.19\times10^{-17}$ | $3.51\times10^{-17}$ | $2.00\times10^{-17}$ |
| $0.50$ |                 $1.60\times10^{-17}$ | $2.22\times10^{-17}$ | $9.69\times10^{-18}$ |

The proper odd-shell run used $N=4$, $M=1296$, $R=256$, and $\Delta t=0.05$. One cubature seed reached $t=0.5$; the independent seed stopped at the predeclared $t=0.25$ checkpoint. It is therefore a targeted diagnostic, not a cofinal resolution study.

On the correct $P=5\to35\to126$ ladder:

| seed/time         | quantity                    |       $5\leftarrow35$ |     $35\leftarrow126$ |    ratio |
|-------------------|-----------------------------|----------------------:|----------------------:|---------:|
| 20260723, $t=.25$ | lifted newly opened source  | $1.9743\times10^{-4}$ | $5.7237\times10^{-6}$ | $0.0290$ |
| 20260724, $t=.25$ | lifted newly opened source  | $2.0991\times10^{-4}$ | $6.7174\times10^{-6}$ | $0.0320$ |
| 20260723, $t=.50$ | lifted newly opened source  | $3.1202\times10^{-4}$ | $1.8381\times10^{-5}$ | $0.0589$ |
| 20260723, $t=.25$ | actual high-to-low feedback | $6.5919\times10^{-3}$ | $9.1541\times10^{-3}$ |  $1.389$ |
| 20260724, $t=.25$ | actual high-to-low feedback | $7.0412\times10^{-3}$ | $1.0287\times10^{-2}$ |  $1.461$ |
| 20260723, $t=.50$ | actual high-to-low feedback | $4.3824\times10^{-3}$ | $6.2354\times10^{-3}$ |  $1.423$ |

The newly opened lifted source contracts by factors $17$–$34$. It is not the actual trained tail: trained high-shell velocity can be much larger after the shell has evolved. Actual aggregate feedback and observable-generator defects did not contract. Observable differences remained tiny—approximately $0.0021\%$–$0.0079\%$ of the fixed scale—but their adjacent ordering was noncontracting.

The cubic shell has $20$ active modes and the quintic shell $56$. RMS-per-mode shell ratios were below one in most channels, while the aggregate Hilbert norm was not. Per-mode contraction is a mechanism diagnostic, not a convergence theorem.

A same-dimensional basis diagnostic inside a resolved $P=35$ space compared the first five Hermite coordinates, eight random rank-five subspaces, and a trajectory-POD rank-five subspace fitted at $t=0,0.25,0.5$ and evaluated later:

| held-out time |       Hermite defect |           POD defect | POD/Hermite | random median |
|--------------:|---------------------:|---------------------:|------------:|--------------:|
|         $1.0$ | $3.729\times10^{-4}$ | $1.856\times10^{-4}$ |     $0.498$ |       $0.610$ |
|         $1.5$ | $4.376\times10^{-4}$ | $2.227\times10^{-4}$ |     $0.509$ |       $0.671$ |
|         $2.0$ | $4.464\times10^{-4}$ | $2.278\times10^{-4}$ |     $0.510$ |       $0.679$ |

This shows that the eight tested random five-dimensional subspaces do not work and that a trajectory-adapted basis can improve this particular held-out defect. It is not an admissible convergence witness: the POD basis is fitted to the target trajectory, its held-out interval misses the early maximum defect, and five active POD mixtures were compared with four active linear Hermites plus one inert constant.

**Primary provenance.** `PDE_BRIDGEABILITY_RESOLUTION_REPORT.md`, §§1–6; `PDE_LEAN_SALVAGE_REPORT.md`, §4.1. The parity report supersedes the $P=5\to15\to35$ interpretation in `REPORT.md`, §4 and the preliminary adverse ratios in `PDE_LEAN_SALVAGE_REPORT.md`, §4.

### 7.12 Common-reference degree-seven and coupled Cauchy audits

The next audit evolved only one parity-reduced degree-seven state and evaluated lower-prefix vector fields on that same state. This avoids comparing separately trained high and low systems. The run used one seed with $N=1$, $M=4096$, $R=512$, $\Delta t=0.025$, and checkpoint $t=0.25$. Degree-five calibrations at $N=1,2$ made a gross depth artifact less likely, but they did not certify degree-seven depth convergence; no independent-seed or bootstrap campaign was run.

At $t=0.25$:

| adjacent shell | total projection commutator | normalized observable-generator defect |
|----------------|----------------------------:|---------------------------------------:|
| degree $1\to3$ |      $3.25317\times10^{-3}$ |                 $6.02185\times10^{-6}$ |
| degree $3\to5$ |      $7.25826\times10^{-3}$ |                 $3.02836\times10^{-5}$ |
| degree $5\to7$ |      $9.62238\times10^{-3}$ |                 $4.89803\times10^{-5}$ |

Therefore

$$
\frac{C_7}{C_5}=1.3257147,\qquad
\frac{\text{observable defect}_7}
{\text{observable defect}_5}
=1.6173852.
\tag{7.7}
$$

The theorem-facing aggregate quantities had not turned over by degree seven. The mechanism was less adverse:

- shell-cardinality adjustment gave $0.90564$ for the total state ratio;
- RMS-per-mode ratios for $c,\dot c,h,p$ were $0.865,0.865,0.903,0.965$;
- effective mode participation increased sharply, while the largest-mode energy fraction fell;
- more than $99.998\%$ of each dominant adjacent $b$-commutator remained in the newly opened shell;
- the weighted cosine of adjacent dominant commutators was $4.62\times10^{-4}$.

Thus a small number of coherently aligned resonant modes is ruled out at that checkpoint. Aggregate summability and observable-tail orthogonality are not.

The final coupled run co-evolved degrees $3,5,7$ and measured actual state tails, low-state shadows, feedback, and observable gaps:

| metric at $t=.25$      |        degree $3\to5$ |        degree $5\to7$ |    ratio |
|------------------------|----------------------:|----------------------:|---------:|
| projective state error | $1.3116\times10^{-3}$ | $1.7338\times10^{-3}$ | $1.3219$ |
| observable gap         | $2.1913\times10^{-5}$ | $3.5846\times10^{-5}$ | $1.6358$ |
| feedback commutator    | $7.2584\times10^{-3}$ | $9.6224\times10^{-3}$ | $1.3257$ |

The realized final-time shadow quotients were

$$
1.08921,\qquad1.08771,
$$

whose ratio is

$$
0.99862.
\tag{7.8}
$$

This detected no large change in amplification for one realized forcing direction. It is a secant quotient based on two nonzero checkpoints, not a worst-case propagator norm or a cutoff-uniform stability certificate.

**Primary provenance.** `PDE_HIGH_TO_LOW_TAIL_ROUND_REPORT.md`, §§1–7; `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`, §§3–5. The latter supersedes the stronger earlier phrase that flow amplification had been eliminated.

### 7.13 Scalar high-degree ladder

The $m=d=1$ reduction makes high source degrees cheaper while retaining a nontrivial depth/time Gram

$$
G(s,t)=\mathbb E[h(s,\eta,t)^2].
$$

For the sine stress at $y=2$, using degree $11$ as internal reference:

| source degree | Gram distance to degree 11 |
|--------------:|---------------------------:|
|             1 |                  $0.339\%$ |
|             3 |                  $0.369\%$ |
|             5 |                  $0.297\%$ |
|             7 |                  $0.205\%$ |
|             9 |                  $0.194\%$ |

At the stronger $y=4$ escalation, using degree $13$ as reference:

| source degree | Gram distance to degree 13 |
|--------------:|---------------------------:|
|             1 |                  $0.247\%$ |
|             3 |                  $0.274\%$ |
|             5 |                  $0.233\%$ |
|             7 |                  $0.178\%$ |
|             9 |                  $0.174\%$ |
|            11 |                  $0.115\%$ |

The corrections broadly decrease after degree three but are not monotone. Against the finite dense sine mean, Gram errors were

$$
2.4235\%\ \text{at degree 1},\qquad
2.3671\%\ \text{at degree 3},\qquad
2.4972\%\ \text{at degree 11}.
\tag{7.9}
$$

Higher degree therefore did not systematically improve the finite-reference match.

For canonical $\tanh$, the underresolved $R=128$ degree-13 pilot had condition number $2897.99$ and is inadmissible for a tail conclusion. At $R=512$, two well-conditioned scrambles gave:

| Quantity                                |  Scramble 1 |  Scramble 2 |
|-----------------------------------------|------------:|------------:|
| $E_{11\to13}/E_{9\to11}$                |     $0.958$ |     $1.913$ |
| outgoing-tail ratio                     |     $0.894$ |     $1.893$ |
| Gram-increment ratio                    |     $1.138$ |     $3.989$ |
| absolute $E_{11\to13}$                  |  $0.008996$ |  $0.009350$ |
| normalized degree-$11\to13$ Gram effect | $0.00462\%$ | $0.00608\%$ |

The apparent turnover did not replicate. The absolute high-degree effect is tiny, but no resolved monotone Cauchy trend exists.

**Primary provenance.** `SCALAR_HERMITE_MINIMAL_EXPERIMENT_REPORT.md`, §§1, 5, 7–9; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §9.5 for the degree-specific finite-dense comparison in (7.9).

### 7.14 Empirical synthesis and supersession ledger

The evidence supports the following calibrated conclusions.

| Claim                                                                                | Current empirical status                                          |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| A genuine width-independent PDE was integrated                                       | **Established**                                                   |
| The implementation obeys the finite-PDE equations and internal identities            | **Established to audited numerical precision**                    |
| The $P=5$ PDE predicts $O(1)$ nonlazy canonical feature motion with low error        | **Strongly supported**                                            |
| The finite canonical PDE/dense curves are exactly equal                              | **Falsified at the audited finite reference**                     |
| The low-order success is tuned only to one label/data case                           | **Strongly disfavored**                                           |
| Identity/deep-linear or scalar-clock dynamics explain the result                     | **Rejected**                                                      |
| The tested fixed initialization-gain linear model explains the sine stress           | **Rejected for Gram dynamics**                                    |
| Every adaptive linear surrogate is excluded                                          | **Open**                                                          |
| Centered trained-depth innovations scale as $L^{-1}$ in variance                     | **Strongly supported in the tested diagnostics**                  |
| The retained shared-transpose/Onsager mean is correct                                | **Open**                                                          |
| A large static-state continuation counterexample exists                              | **Not found; absence is not proof**                               |
| Low chronological response grade captures the tested finite-matrix causal correction | **Strongly supported**                                            |
| Lifted newly opened odd-shell source terms weaken                                    | **Supported at the tested rungs; not the trained aggregate tail** |
| Aggregate Hermite state/observable Cauchy increments contract                        | **Not observed**                                                  |
| Aggregate Hermite divergence is established                                          | **No**                                                            |
| Pure-Hermite arbitrary-accuracy convergence                                          | **Open**                                                          |
| Ordered dense-limit identification                                                   | **Open**                                                          |
| Uniform all-time accuracy                                                            | **Open**                                                          |

The following historical interpretations are superseded:

- $P=5\to15\to35$ is not a valid physical hierarchy for the odd/symmetric problem.
- Ratios $0.0290,0.0320,0.0589$ measure a lifted newly opened source, not the full trained tail.
- One realized secant-gain ratio near one is not a stability theorem.
- Near-unit projected energy does not certify the outgoing Hermite or transpose residual.
- The finite-matrix $q/r$ hierarchy is not itself a width-independent PDE.
- “Close” must not be replaced by “indistinguishable” for the primary finite reference.

The most accurate empirical conclusion is:

> One very small, nonlinear, autonomous PDE is a robust and surprisingly portable surrogate for the tested dense feature-learning dynamics. The data neither establish nor refute convergence of the parity-correct pure-Hermite hierarchy, and they do not identify the PDE with the ordered dense limit.

## Chapter 8 — The convergence and identification frontier

### 8.1 The theorem ladder and the decisive separation of bridges

There is no single undifferentiated “PDE convergence problem.” The residual program contains at least five separate bridges:

| Level | Statement                                                                                               | Current status                                                |
|-------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| I     | Each finite-cutoff PDE is internally correct and well defined on its interval of existence              | Internal identities proved; broad uniform well-posedness open |
| II    | One low-order PDE accurately approximates tested finite dense networks                                  | Strong empirical support                                      |
| III   | The parity-reduced finite PDEs converge on every compact training interval to an infinite operator flow | Open                                                          |
| IV    | That infinite operator flow equals the ordered $n\to\infty$, then $L\to\infty$ dense limit              | Open                                                          |
| V     | Compact-time convergence upgrades to uniform $t\ge0$ approximation                                      | Open                                                          |
| VI    | Some admissible finite PDE family works even if pure Hermites fail                                      | Broad project conjecture; open                                |

The strategically correct first analytic target is Level III. Let $Y_{r_{\mathrm H}}$ be the parity-reduced degree-$r_{\mathrm H}$ operator flow and $Y_\infty$ a putative infinite operator flow. For each $T<\infty$, seek

$$
\boxed{
\sup_{\vartheta\in\mathcal U}
\sup_{0\le t\le T}
d_{\mathrm{obs}}
\left(
\mathcal O[Y_{r_{\mathrm H}}](t),
\mathcal O[Y_\infty](t)
\right)
\longrightarrow0.
}
\tag{8.1}
$$

Only after (8.1) should one identify $Y_\infty$ with the ordered dense target. Only after both should one address

$$
\sup_{t\ge0}d_{\mathrm{obs}}.
$$

This order prevents three invalid inferences:

- Hermite completeness for one fixed field does not imply convergence of the trained cutoff flows.
- Convergence of the operator hierarchy does not identify its limit with the dense model.
- Compact-time convergence does not imply all-time accuracy.

**Primary provenance.** `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§1, 5.3–5.5 and 15; `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`, §§2.3 and 4–5.

### 8.2 The infinite source-space operator and its bounded but noncompact transpose

The clean analytic formulation must distinguish two Gaussian roles:

- $\eta$ is the source-neuron label with Hilbert space $$
  H=L^2(\mu_\eta);
  $$
- $(\xi,\omega)$ labels a target row and a common isonormal row-noise realization, with $$
  \mathcal R
  =L^2(\mu_\xi\otimes\mathbb P_\omega).
  $$

Let $W_\omega:H\to L^2(\Omega)$ be a unit-covariance isonormal process:

$$
\mathbb E[W(u)W(v)]=\langle u,v\rangle_H.
\tag{8.2}
$$

Define the isometric embedding

$$
(Iu)(\xi,\omega)=W_\omega(u).
\tag{8.3}
$$

Its Hilbert adjoint $T_W=I^\ast:\mathcal R\to H$ is the Riesz representative

$$
\boxed{
\langle T_W\beta,u\rangle_H
=
\mathbb E_{\xi,\omega}
\bigl[\beta(\xi,\omega)W_\omega(u)\bigr],
\qquad
\|T_W\beta\|_H\le\|\beta\|_{\mathcal R}.
}
\tag{8.4}
$$

In source-Hermite coordinates,

$$
T_W\beta
=
\sum_\nu\psi_\nu
\mathbb E[\epsilon_\nu\beta].
\tag{8.5}
$$

For a learned row field

$$
c\in
L^2(\mu_\xi\otimes\mathbb P_\omega;H),
$$

define

$$
(R_cu)(\xi,\omega)=\langle c(\xi,\omega),u\rangle_H,
$$

$$
T_c\beta=R_c^\ast\beta
=\mathbb E_{\xi,\omega}[c\,\beta].
\tag{8.6}
$$

The full row and shared transpose are

$$
\boxed{
A_c=\sigma_w I+R_c,
\qquad
A_c^\ast=\sigma_wT_W+T_c.
}
\tag{8.7}
$$

At cutoff $r_{\mathrm H}$, with source projection $\Pi_{r_{\mathrm H}}$ and $c$ taking values in its range,

$$
A_{c,r_{\mathrm H}}
=A_c\Pi_{r_{\mathrm H}},
\qquad
A_{c,r_{\mathrm H}}^\ast
=
\Pi_{r_{\mathrm H}}\sigma_wT_W+T_c.
\tag{8.8}
$$

This is exactly the ideal algebra of the finite operator PDE. The slow fields $b,a,h,p$ are not themselves projected; the cutoff acts on the source index of the row/query operator.

The Riesz formulation corrects one earlier overstatement. Malliavin differentiability is not needed merely to define the frozen transpose or to prove convergence on one fixed compact family of queries. When differentiability is available, Stein’s identity

$$
\mathbb E[\epsilon_\nu\beta]
=\mathbb E[\partial_{\epsilon_\nu}\beta]
\tag{8.9}
$$

gives an informative response representation, but boundedness already follows from (8.4).

Boundedness is not compactness. Taking

$$
\beta_\nu(\xi,\omega)=\epsilon_\nu(\omega)
$$

gives an orthonormal family in $\mathcal R$ with

$$
T_W\beta_\nu=\psi_\nu.
$$

Therefore

$$
\boxed{
\sup_{\|\beta\|_{\mathcal R}\le1}
\|(I-\Pi_{r_{\mathrm H}})T_W\beta\|_H
=1
}
\tag{8.10}
$$

for every finite cutoff. Strong projection convergence is uniform on compact sets, not on the energy-bounded unit ball.

**Primary provenance.** `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`, §§1.1–2.1; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §10 and §14.2. These sources supersede the separate-Malliavin-boundedness claim in `PDE_HIGH_TO_LOW_TAIL_ROUND_REPORT.md`, §6.

### 8.3 What dissipation supplies—and what it does not

Along any sufficiently regular finite-cutoff solution, use a Lagrangian characteristic coupling and write the trainable row coordinate as

$$
w=\sigma_w\epsilon+c.
$$

The natural trainable-state space has the schematic form

$$
X
=
H^d
\times H
\times
L^2\!\left(
[0,1]\times\mu_\xi\times\mathbb P_\omega;H
\right),
\tag{8.11}
$$

for $(b,a,c)$. The finite-cutoff gradient identity has the form

$$
\boxed{
-\dot{\mathcal L}_{r_{\mathrm H}}
=
\|\dot b_{r_{\mathrm H}}\|_H^2
+
\|\dot a_{r_{\mathrm H}}\|_H^2
+
\int_0^1
\|\dot c_{r_{\mathrm H}}(s)\|_{\mathcal R(H)}^2\,ds.
}
\tag{8.12}
$$

For each fixed $T$, this yields cutoff-uniform bounds

$$
\|Y_{r_{\mathrm H}}(t)\|_X
\le
\|Y_{r_{\mathrm H}}(0)\|_X
+\sqrt{T\mathcal L(0)},
\tag{8.13}
$$

$$
\|Y_{r_{\mathrm H}}(t)-Y_{r_{\mathrm H}}(s)\|_X
\le
\sqrt{|t-s|\mathcal L(0)}.
\tag{8.14}
$$

These are finite-time boundedness and time equicontinuity for the trainable Lagrangian state. The derived depth fields $h,p,\beta$ additionally require cutoff-uniform estimates for their coupled forward/backward boundary-value problem.

Even after those estimates, (8.13) is only boundedness in an infinite-dimensional Hilbert space. It does not prevent source-mode mass from escaping to larger and larger Hermite degrees. Equation (8.10) shows exactly why the transpose can carry such an escaping sequence without violating the energy bound.

Similarly, (8.12) gives an $L^2$-in-time speed budget:

$$
\int_0^\infty\|\dot Y(t)\|^2\,dt
\le\mathcal L(0),
$$

but not automatically the finite arclength

$$
\int_0^\infty\|\dot Y(t)\|\,dt<\infty.
$$

The latter, or a substitute such as residual integrability, is needed by the leading all-time arguments.

**Primary provenance.** `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`, §§1.3 and 2.1; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§10.1 and 15.4.

### 8.4 Why plain $L^2$ stability fails

The difficult adjoint nonlinearity is

$$
(z,p)\longmapsto\sigma'(z)p.
$$

For two states,

$$
\delta\beta
=
\sigma'(z)\delta p
+
\widetilde p\,
\bigl[\sigma'(z)-\sigma'(\widetilde z)\bigr].
\tag{8.15}
$$

When $\sigma''$ is bounded, as for the smooth activations under consideration, $\sigma'$ is Lipschitz and

$$
|\delta\beta|
\lesssim
|\delta p|+|\widetilde p|\,|\delta z|.
\tag{8.16}
$$

On a plain $L^2$ ball, $\widetilde p$ and $\delta z$ may each be only $L^2$, so their product is generally only $L^1$. This loss is genuine, not merely a failed proof technique. Choose a constant $z_\ast$ with $\sigma''(z_\ast)\ne0$, let $p(\eta)=\eta_{d+1}$, and set

$$
A_N=\{N\le|\eta_{d+1}|\le N+1\},
\qquad
\delta z_N=\varepsilon\mathbf1_{A_N}
$$

for a fixed sufficiently small $\varepsilon>0$. A uniform mean-value lower bound on the interval between $z_\ast$ and $z_\ast+\varepsilon$ gives

$$
\frac{
\|[\sigma'(z_\ast+\delta z_N)-\sigma'(z_\ast)]p\|_2
}{
\|\delta z_N\|_2
}
\ge cN\longrightarrow\infty,
$$

whereas $\|\delta z_N\|_2=\varepsilon\mu(A_N)^{1/2}\to0$. Thus the multiplier map is not locally Lipschitz in the plain $L^2$ topology. The obstruction is present already at initialization:

$$
p(1,\eta)=a(\eta)=A\eta_{d+1},
\tag{8.17}
$$

an unbounded Gaussian coordinate. Perturbations concentrated in regions where $|a|$ is large make the multiplier norm arbitrarily large.

Thus the formerly convenient assertion of a cutoff-uniform locally Lipschitz vector field on an $L^2$ ball is false. A valid stability topology must control products, for example through

$$
\mathcal H_{\mathrm G}^{\alpha}\cap L^4
\longrightarrow L^2
\tag{8.18}
$$

or a Gaussian-Orlicz analogue. Indeed,

$$
\|\sigma'(z)p-\sigma'(\widetilde z)\widetilde p\|_2
\le
\|p-\widetilde p\|_2
+
C\|\widetilde p\|_4
\|z-\widetilde z\|_4.
\tag{8.19}
$$

This is why the compactness and stability obligations cannot be discharged by energy in the natural $L^2$ metric alone.

**Primary provenance.** `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`, §2.2; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§10.2 and 15.3.

### 8.5 Weighted Gaussian source regularity

Let the Gaussian number operator satisfy

$$
\mathsf N\psi_\nu=|\nu|\psi_\nu.
$$

For $\alpha>0$, define the source-weighted Sobolev space

$$
\mathcal H_{\mathrm G}^{\alpha}
=D((I+\mathsf N)^{\alpha/2}),
$$

$$
\|u\|_{\mathcal H_{\mathrm G}^{\alpha}}^2
=
\sum_\nu(1+|\nu|)^\alpha|u_\nu|^2.
\tag{8.20}
$$

Then

$$
\boxed{
\|(I-\Pi_{r_{\mathrm H}})u\|_{L^2(\mu)}
\le
(1+r_{\mathrm H})^{-\alpha/2}
\|u\|_{\mathcal H_{\mathrm G}^{\alpha}}.
}
\tag{8.21}
$$

Equation (8.21) converts a cutoff-uniform positive amount of source regularity into a vanishing aggregate Hermite tail. A targeted sufficient estimate on every compact interval is

$$
\boxed{
\sup_{r_{\mathrm H}}
\sup_{0\le t\le T}
\mathcal E_\alpha[Y_{r_{\mathrm H}}(t)]
<\infty
}
\tag{8.22}
$$

for some $\alpha>0$, where $\mathcal E_\alpha$ controls at least:

$$
\sum_q
\left(
\|h_q\|_{\mathcal H_{\mathrm G}^{\alpha}}^2
+
\|p_q\|_{\mathcal H_{\mathrm G}^{\alpha}}^2
\right),
\tag{8.23}
$$

$$
\int_0^1
\mathbb E
\left[
\|c\|_{\mathcal H_{\mathrm G}^{\alpha}}^2
+
\sum_q
\|c\|_{\mathcal H_{\mathrm G}^{\alpha}}^2|\beta_q|^2
+
\sum_q|p_q|^2
\left\|
(I+\mathsf N)^{\alpha/2}
(\sigma_wI+R)H_q
\right\|^2
\right]ds,
\tag{8.24}
$$

together with the $L^4$ or Gaussian-Orlicz moments needed for (8.19). The mixed $c$--$\beta$ term is included specifically for the learned-transpose estimate (8.26); separate second-moment bounds would not imply it.

This is a sufficient route, not a theorem already proved and not the only possible compactness formulation. Generic Gaussian Sobolev or Orlicz bounds without source-mode-coercive weights are insufficient: infinitely many orthogonal coordinate functions can share the same unweighted bounds.

For the frozen term, (8.22) yields the needed estimate only after choosing a Lagrangian row-noise lift for which $c$ is differentiable in the Gaussian row noise, the response $R=D_\varepsilon c$ exists, and the displayed differentiation and expectation interchange is justified. Stein's identity and (8.24) then give

$$
\|T_W\beta_q\|_{\mathcal H_{\mathrm G}^{\alpha}}^2
\lesssim
\|\sigma''\|_\infty^2
\mathbb E\!\left[
|p_q|^2
\left\|
(I+\mathsf N)^{\alpha/2}
(\sigma_wI+R)H_q
\right\|^2
\right],
$$

and therefore

$$
\left(
\int_0^1
\|(I-\Pi_{r_{\mathrm H}})T_W\beta_q(s)\|_{L^2}^2\,ds
\right)^{1/2}
\lesssim
(1+r_{\mathrm H})^{-\alpha/2}C_T.
\tag{8.25}
$$

For the learned term, Cauchy--Schwarz in the row variables gives

$$
\|T_c\beta_q\|_{\mathcal H_{\mathrm G}^{\alpha}}
\le
\left(
\mathbb E
\|c\|_{\mathcal H_{\mathrm G}^{\alpha}}^2
|\beta_q|^2
\right)^{1/2}.
$$

Applying (8.21) to $T_c\beta_q$ gives the missing decay factor:

$$
\boxed{
\left(
\int_0^1
\|(I-\Pi_{r_{\mathrm H}})T_c\beta_q(s)\|_{L^2}^2\,ds
\right)^{1/2}
\le
(1+r_{\mathrm H})^{-\alpha/2}
\left(
\int_0^1
\mathbb E
\|c\|_{\mathcal H_{\mathrm G}^{\alpha}}^2
|\beta_q|^2
\;ds
\right)^{1/2}.
}
\tag{8.26}
$$

Thus the combined shared-transpose tail is $O((1+r_{\mathrm H})^{-\alpha/2})$ in $L^2([0,1]_s;L^2(\mu))$ under the stated joint moments and row-response regularity. A uniform-in-depth estimate would require replacing the integrated control in (8.24) by a corresponding $\sup_s$ bound. Bare $L^2$ boundedness would not imply either tail estimate. The hard step is propagating (8.22) through the coupled learned row, nonlinear forward field, and unbounded-terminal-adjoint equations—not proving (8.21).

**Primary provenance.** `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§6.2 and 15.1–15.3; `SCALAR_HERMITE_MINIMAL_EXPERIMENT_REPORT.md`, §7; `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`, §2.3.

### 8.6 The response/Onsager bridge

Source Hermites, row-noise responses, chronological response, and training-time derivatives are distinct axes.

For a sufficiently regular function $F(\eta)$ of the immutable Gaussian source and normalized source Hermite $\psi_\nu$,

$$
\mathbb E[F(\eta)\psi_\nu(\eta)]
=
\frac1{\sqrt{\nu!}}
\mathbb E[\partial_\eta^\nu F(\eta)].
\tag{8.27}
$$

A high source-Hermite coefficient is therefore a high Gaussian source-response coefficient. It is not a high training-time derivative.

The frozen transpose coefficient has the row-noise Stein representation (8.9), which is first order in the coordinate $\epsilon_\nu$, even when the associated source mode $\psi_\nu$ has high degree. Source differentiation $\partial_\eta^\nu$ and row-noise differentiation $\partial_{\epsilon_\nu}$ must not be identified.

To expose the learned response, choose a common Lagrangian characteristic lift. The identity below is conditional on $c(s,\xi,\varepsilon,t)$ being differentiable in $\varepsilon$, on differentiation commuting with the characteristic equation and the relevant expectations, and on the displayed mode contractions being summable:

$$
w_\mu=\sigma_w\epsilon_\mu+c_\mu(\epsilon),
\qquad
z_q=\sum_\mu w_\mu H_{\mu q}.
\tag{8.28}
$$

Define the row-response matrix

$$
R_{\nu\mu}
=\partial_{\epsilon_\nu}c_\mu.
\tag{8.29}
$$

Because $c(\cdot,0)=0$ at the Gaussian initialization,

$$
R(s,\xi,\varepsilon,0)=0.
$$

Holding the slow macroscopic fields fixed in the local tagged response,

$$
\partial_{\epsilon_\nu}\beta_q
=
\sigma''(z_q)p_q
\left[
\sigma_wH_{\nu q}
+
\sum_\mu R_{\nu\mu}H_{\mu q}
\right].
\tag{8.30}
$$

Since

$$
\dot c_\mu
=-\gamma\sum_qe_q\beta_qH_{\mu q},
$$

the local learned row response obeys

$$
\boxed{
\dot R
=-\gamma\sum_qe_q
\sigma''(z_q)p_q
\bigl[(\sigma_wI+R)H_q\bigr]
\otimes H_q.
}
\tag{8.31}
$$

Global variations of $e,p,H$ belong to the larger chronological $q/r$ hierarchy and are not contained in this local identity.

Under the stated differentiability and integrability assumptions, (8.31) is an exact local tagged-response identity. It is not yet a well-posed autonomous response equation: its coefficients use the coupled forward/adjoint solution, and no closed operator domain or propagation theorem for $R$ is supplied. It identifies the dynamically generated family that a weighted estimate should control and also exposes a state question. The Eulerian conditional law $\rho$ does not automatically determine a particular Lagrangian coupling or $R$. One must prove either:

1.  the needed response contractions are coupling-invariant and functions of the Eulerian state; or
2.  $R$, or only the finitely many query contractions $(\sigma_wI+R)H_q$, must be promoted to explicit response state.

This is the branch point between a pure-Hermite theorem and a response-enriched theorem.

Higher source Hermites are not “higher Onsager orders.” An Onsager term is a conditional mean caused by operator reuse; source degree resolves its dependence on immutable labels; chronological grade counts ordered dense reuses. A low source degree can carry a nontrivial Onsager response, while a high source degree can encode label dependence without adding memory.

**Primary provenance.** `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§14.1–14.4 and 15.1–15.2.

### 8.7 Chronological response as a forced-stability mechanism

The exact factorial estimate (6.65) controls the depth propagator without assuming normality. In continuum notation, if

$$
\partial_sJ(s,u)=A(s)J(s,u),
\qquad
J(u,u)=I,
$$

then

$$
J(s,u)
=I+
\sum_{k\ge1}
\int_{u<s_1<\cdots<s_k<s}
A(s_k)\cdots A(s_1)
\,ds_1\cdots ds_k,
\tag{8.32}
$$

and

$$
\boxed{
\|J-J_{\le K}\|_{\mathrm{op}}
\le
\sum_{j>K}\frac{C_A^j}{j!}
\le
e^{C_A}\frac{C_A^{K+1}}{(K+1)!},
\qquad
C_A=\int_u^s\|A(v)\|_{\mathrm{op}}\,dv.
}
\tag{8.33}
$$

The estimate is valid for noncommuting and nonnormal $A$. It is consequently a plausible foundation for a cutoff-uniform forced gain, rather than a false spectral/eigenvalue argument.

It is not a complete consistency theorem. A coupled truncation changes the source $\dot A$, nonlinear derivative trees branch, and Gaussian conditioning can contract omitted high objects back into retained observables. These errors must enter a full outgoing residual. In abstract form, if

$$
\dot Y=F(Y),
\qquad
\dot Y_{r_{\mathrm H}}
=F_{r_{\mathrm H}}(Y_{r_{\mathrm H}}),
$$

the relevant consistency defect is

$$
\mathfrak r_{r_{\mathrm H}}(Y)
=
F_{r_{\mathrm H}}(\mathcal P_{r_{\mathrm H}}Y)
-\mathcal P_{r_{\mathrm H}}F(Y),
\tag{8.34}
$$

not only the pure propagator tail. A valid stability theorem must bound the response

$$
\sup_{t\le T}
\|Y_{r_{\mathrm H}}(t)-\mathcal P_{r_{\mathrm H}}Y(t)\|
$$

in terms of the compatible initial defect and an integral of $\|\mathfrak r_{r_{\mathrm H}}\|$ in a topology strong enough to see coherent transpose actions but weak enough for compactness.

**Primary provenance.** `dense_euclidean_continuous_depth_npde_audit.md`, §§5.1–5.5 and 6.2–6.5; `dense_euclidean_continuous_depth_pde_conjecture(1).md`, §5.1; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§6.6, 13.2 and 15.3.

### 8.8 Two conditional compact-time Galerkin routes

The strongest presently valid statement is a pair of conditional reductions, not a proved unconditional convergence theorem. The statements below are pointwise in the static parameter $\vartheta$. To obtain the uniform claim (8.1), every hypothesis and modulus must hold uniformly over $\vartheta\in\mathcal U$.

Let $\mathcal P_{r_{\mathrm H}}$ act as the identity on the slow fields and as $\Pi_{r_{\mathrm H}}$ on the source/operator coordinate. Two logically different routes are available.

#### 8.8.1 Qualitative compactness--uniqueness route

Fix $T<\infty$ and view every projected state in one ambient state space $X$ by the canonical zero extension. Assume:

1.  each projected solution $Y_{r_{\mathrm H}}$ exists on $[0,T]$;
2.  $\{Y_{r_{\mathrm H}}\}$ is relatively compact in $C([0,T];X)$;
3.  the initial states converge in $X$;
4.  compact-set drift consistency and continuity of the forward/adjoint reconstruction are strong enough that every convergent subsequence solves the same infinite equation $\dot Y=F(Y)$;
5.  that infinite Cauchy problem is unique on the reachable class; and
6.  the output and Gram readouts are continuous in the topology of $X$.

Then every subsequence has a further subsequence converging to the unique infinite solution, so the full sequence converges in $C([0,T];X)$ and its readouts converge. This route is qualitative. It supplies no rate unless a quantitative stability modulus is added.

#### 8.8.2 Quantitative forced-stability route

Let $X_{\mathrm{str}}\hookrightarrow X_{\mathrm{wk}}$ be a stronger-to-weaker pair in which the consistency defect is controlled and the readouts are locally continuous. A **cutoff-uniform forced gain** $G_T$ means the following input-to-state estimate: for every exact projected solution

$$
\dot Y_{r_{\mathrm H}}=F_{r_{\mathrm H}}(Y_{r_{\mathrm H}})
$$

and every absolutely continuous comparison path $Z_{r_{\mathrm H}}$ with

$$
d_{r_{\mathrm H}}
:=
\dot Z_{r_{\mathrm H}}
-F_{r_{\mathrm H}}(Z_{r_{\mathrm H}})
\in L^1(0,T;X_{\mathrm{str}}),
$$

one has

$$
\boxed{
\|Y_{r_{\mathrm H}}-Z_{r_{\mathrm H}}\|_{C([0,T];X_{\mathrm{wk}})}
\le
G_T
\left[
\|Y_{r_{\mathrm H}}(0)-Z_{r_{\mathrm H}}(0)\|_{X_{\mathrm{wk}}}
+
\|d_{r_{\mathrm H}}\|_{L^1(0,T;X_{\mathrm{str}})}
\right],
}
\tag{8.35}
$$

with $G_T$ independent of $r_{\mathrm H}$. This is the hard stability hypothesis; it is not proved by naming it.

Assume an infinite solution $Y$ exists, set

$$
Z_{r_{\mathrm H}}=\mathcal P_{r_{\mathrm H}}Y,
\qquad
\delta_{r_{\mathrm H}}
=
\|Y_{r_{\mathrm H}}(0)-\mathcal P_{r_{\mathrm H}}Y(0)\|_{X_{\mathrm{wk}}},
$$

and suppose $\delta_{r_{\mathrm H}}\to0$ and, uniformly for $0\le t\le T$,

$$
\left\|
F_{r_{\mathrm H}}(\mathcal P_{r_{\mathrm H}}Y(t))
-\mathcal P_{r_{\mathrm H}}F(Y(t))
\right\|_{X_{\mathrm{str}}}
\le
C_T(1+r_{\mathrm H})^{-\zeta}
\tag{8.36}
$$

for some $\zeta>0$. Since the left side of (8.36), with the opposite sign, is the forcing defect of $Z_{r_{\mathrm H}}$, (8.35) gives

$$
\boxed{
\sup_{0\le t\le T}
\|Y_{r_{\mathrm H}}(t)-\mathcal P_{r_{\mathrm H}}Y(t)\|_{X_{\mathrm{wk}}}
\le
G_T
\left[
\delta_{r_{\mathrm H}}
+
TC_T(1+r_{\mathrm H})^{-\zeta}
\right].
}
\tag{8.37}
$$

For observable convergence, assume in addition that the finite readout maps are locally equicontinuous in $X_{\mathrm{wk}}$ on the reachable neighborhood and that reconstruction is consistent along the projected infinite solution:

$$
\sup_{t\le T}
d_{\mathrm{obs}}
\left(
\mathcal O_{r_{\mathrm H}}[\mathcal P_{r_{\mathrm H}}Y(t)],
\mathcal O[Y(t)]
\right)
\longrightarrow0.
$$

The triangle inequality and (8.37) then give convergence of outputs and Grams. With all constants, existence intervals, initial defects, reconstruction errors, and continuity moduli uniform over $\mathcal U$, the estimate may be supremized over $\vartheta$ and yields the uniform compact-time conclusion in (8.1). Otherwise it is only instancewise.

Weighted regularity such as (8.22), compactness, and the chronological factorial bound are possible ways to prove the hypotheses of one of these routes; they are not additional assumptions logically needed once (8.35)–(8.36) have been granted. Either route proves internal convergence only to the infinite operator flow. Neither identifies that flow with the dense limit or yields all-time uniformity.

**Primary provenance.** `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`, §2.3; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§10.3 and 15.4–15.5.

### 8.9 Ordered dense-limit identification

Even a complete proof by either route in §8.8 leaves a separate identification theorem. The required order is:

$$
n\to\infty\ \text{at fixed }L,
\qquad
L\to\infty,
\qquad
r_{\mathrm H}\to\infty.
\tag{8.38}
$$

No commutation of these limits is assumed.

The identification program has four components.

**Fixed-$L$ causal width theorem.** Derive the infinite-width joint law of forward rows, adjoints, preactivations, and learned row histories for every finite set of row and column queries. Because $W_\ell$ and $W_\ell^\top$ are reused, the limit must retain both reciprocal response kernels or an equivalent conditional Gaussian representation. Ordinary marginal convergence is not enough.

**Exact projected coefficient identity.** At finite width, the projected row coefficient

$$
w_{\ell i,\nu}^n
=\sum_{j=1}^n
W_{\ell,ij}\psi_\nu(\eta_j)
$$

satisfies

$$
\dot w_{\ell i,\nu}^n
=-\gamma\sum_qe_q
\beta_{q,i}^\ell
H_{\nu q}^{n,\ell},
\qquad
H_{\nu q}^{n,\ell}
=\frac1n\sum_j
\psi_\nu(\eta_j)h_{q,j}^\ell.
\tag{8.39}
$$

This exactly matches the candidate Liouville velocity after convergence of the empirical quantities. It does not by itself prove their joint convergence or close the transpose.

**Trained iid-depth homogenization.** Decompose every reused row/column action into:

$$
\text{conditional/shared-transpose mean}
+
\text{centered innovation}.
\tag{8.40}
$$

Prove the centered residual-depth accumulation is $O(L^{-1/2})$, uniformly on compact training intervals, while identifying the limiting conditional mean. The observed $L^{-1}$ centered variance is evidence for only the second-moment cancellation part.

**Shared-transpose/Onsager identification.** Show that the surviving conditional mean in (8.40) is exactly the Riesz/shared-transpose term $A_c^\ast\beta$, or identify the missing response coordinate. The finite-PDE algebra proves only that its own forward and transpose actions are paired; it does not prove that the dense model’s trained cavity mean equals that pair.

The output of these steps must be a well-posed infinite operator flow with the same observables as the ordered dense limit. Only then can the internal convergence conclusion of §8.8 be interpreted as dense-network approximation.

**Primary provenance.** `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§6.1–6.4 and 9.1–9.3; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§6.1–6.4, 14 and 15.4; `dense_euclidean_continuous_depth_npde_audit.md`, §11, Tiers 1–2.

### 8.10 The all-time upgrade and the coercivity trap

Suppose compact-time convergence and dense-limit identification have been established. Uniform approximation for all $t\ge0$ still needs a tail mechanism.

Loss dissipation and positive semidefiniteness are not enough. Consider

$$
\Theta_\delta=\operatorname{diag}(1,\delta),
\qquad
\widehat\Theta_\delta=\operatorname{diag}(1,0).
\tag{8.41}
$$

Both are PSD and

$$
\|\Theta_\delta-\widehat\Theta_\delta\|_{\mathrm{op}}=\delta.
$$

For any fixed horizon, residual trajectories are close as $\delta\to0$. For an initial residual in the second direction,

$$
\widehat e_2(t)=1,\qquad
e_2(t)=e^{-\delta t},
$$

and hence

$$
\sup_{t\ge0}
\|\widehat e(t)-e(t)\|=1.
\tag{8.42}
$$

Thus small absolute kernel error plus PSD does not provide an all-time modulus near arbitrarily slow learnable directions. A uniform kernel floor would suffice but is not established and should not be built into the central conjecture as an assumption.

Viable all-time mechanisms include:

- residual integrability, $$
  \int_0^\infty\|e(t)\|\,dt<\infty;
  $$
- finite state or feature arclength;
- eventual coercivity on the residual subspace;
- relative spectral control that preserves slow/null modes;
- a modulated contraction around the trained plateau;
- a residual-gated outgoing defect, so approximation error production vanishes as the residual vanishes.

The observed plateaus make these routes plausible. They do not choose among them or prove a uniform restart tube. The all-time theorem should be attempted after, not before, compact-time convergence and identification.

**Primary provenance.** `dense_euclidean_continuous_depth_npde_audit.md`, §§5.5, 6.5 and 11 Tier 3; `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §9.4; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§15.4 and 18 Priority 5.

### 8.11 Pure Hermites, response enrichment, and alternative witnesses

The broad finite-PDE thesis must not be made logically equivalent to success of one witness.

**Pure-Hermite route.** Continue with the state

$$
(b,a,\rho)
$$

only if the weighted source estimate closes and all needed transpose/response contractions are functions of the Eulerian state.

**Minimal response enrichment.** If a specific response or history coefficient:

1.  survives the ordered limit at $O(1)$;
2.  is not determined by $(b,a,\rho)$; and
3.  has a summable chronological or kernel tail,

then promote only that coefficient—or the query-restricted family it generates—to explicit autonomous state. A natural finite hierarchy would carry:

- source degree $r_{\mathrm H}$ and mode count $P_{r_{\mathrm H}}$;
- chronological response grade $K$;
- nonlinear tree grade $J$;
- depth approximation $N$;
- only those historical $\kappa_{\mathfrak a}$ coordinates, indexed by finite history words $\mathfrak a$, required to Markovize cyclic learned-row dependencies.

Hermites compress immutable disorder; responses compress causal reuse; historical variables Markovize the surviving memory. The earlier finite-matrix $q/r$ results support rapid decay in $K$, but no complete width-independent response PDE or full residual theorem has been emitted.

**Prelimit-first causal Galerkin.** Work first at finite $n,L$: derive the pathwise response truncation, control its source-substitution error, take $n\to\infty$ at fixed grade by joint Gaussian conditioning, homogenize depth, and only then remove the response/source/depth cutoffs. This is technically heavy but preserves causality and the required limit order.

**DMFT/Volterra finite-memory realization.** Once an exact two-time covariance/response DMFT has been derived for the canonical model, approximate its memory kernels by an architecture-derived, non-oracular finite auxiliary-state realization. This requires regularity or decay of the kernels and stability of the rational approximation; fitting exponentials to one observed trajectory is not enough.

**Variational convergence.** Because every finite operator PDE is a projected gradient flow, one may seek Mosco/evolutionary-$\Gamma$ convergence of energies and metric slopes. This still requires equicoercivity or compactness in hidden directions; loss alone is noncoercive.

**Co-moving architecture-derived basis.** A trajectory-fitted POD basis reduced one held-out defect but is inadmissible as a universal witness and was not an equal-active-rank comparison. A legitimate moving basis would have to be fixed by architecture or updated autonomously from current moments, and its connection/commutator terms would need to be included.

Failure of pure Hermites would be witness-fatal, not project-fatal. Failure of every finite response/history truncation—or proof of an essential nondecaying continuum of memory—would threaten the broad conjecture.

**Primary provenance.** `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§5.5, 15.6 and 16; `PDE_LEAN_SALVAGE_REPORT.md`, §4.1; `dense_euclidean_continuous_depth_npde_audit.md`, §8.6.

### 8.12 Falsifiers, branch criteria, and the ordered proof program

Canonical complete-sequence Hermite convergence would be falsified by a proved target-controlling non-Cauchy lower bound on a parity-correct cofinal sequence. The broader pure-Hermite witness is falsified only by

$$
\inf_{r_{\mathrm H}}E_{r_{\mathrm H}}^{\mathrm H}(T)>0
$$

on some declared compact horizon and parameter class, or by the corresponding all-time bound. Tail escape, noncompactness, a nonvanishing consistency residual, failure of uniqueness, or growth of cutoff forced gain are adverse mechanisms until converted into that observable target-error floor. A two-state continuation witness addresses restart-robust pure-Hermite closure only when both states are physically reachable, agree on the complete declared PDE state, and have a controlled future observable separation. None of these theorem-level falsifiers is currently established.

The broad finite-PDE conjecture would be threatened by stronger outcomes:

- the ordered dense observable limit fails to exist;
- no finite response/history sector gives a vanishing residual;
- causal memory has an essential noncompact, nondecaying continuum that affects the named observables;
- every admissible finite system has a fixed positive observable error floor.

The proof obligations form two parallel compact-time branches rather than one strictly serial chain. The dense-limit branch is Steps 1–2; the operator/Galerkin branch is Steps 3–8. Step 9 is their join, and Step 10 is downstream of that join. The numbering below records logical assembly, not a requirement to postpone the currently highest-leverage operator compactness work until the dense branch is complete.

1.  **Fixed-depth causal width limit.** Derive joint row/column conditioning, learned history, and reciprocal Onsager responses.
2.  **Trained depth homogenization.** Prove centered $O(L^{-1/2})$ cancellation and identify the surviving conditional mean.
3.  **Infinite operator-flow well-posedness.** Establish the correct strong/weak phase space and forward/backward boundary estimates.
4.  **Reachable response equation.** Derive $R=D_\epsilon c$, or the smaller query-restricted response family, and determine whether it is Eulerian-state measurable.
5.  **Source-weighted compactness.** Propagate (8.22), or prove direct compactness of the dynamically generated query family.
6.  **Nonlinear consistency.** Bound frozen and learned transpose tails and high-to-low commutators in the full outgoing residual.
7.  **Uniqueness and cutoff-uniform forced stability.** Use strong-to-weak product estimates and the chronological propagator, not a false plain-$L^2$ Lipschitz constant.
8.  **Compact-time Galerkin convergence.** Complete either conditional route in §8.8.
9.  **Dense-limit identification and branch join.** Use Steps 1–2 and the response/shared-transpose analysis in Steps 3–6 to prove that the ordered dense target equals the infinite operator flow; combine that identification with Step 8 to obtain finite-PDE approximation of the dense target.
10. **All-time upgrade.** Establish residual integrability, finite arclength, eventual coercivity, or another valid plateau-tail mechanism.

The branch rule is causal:

- if Steps 4–6 close with $(b,a,\rho)$, continue with pure Hermites;
- if one $O(1)$ response variable is not state-determined but has a finite/summable tail, add it minimally;
- if the required response family has no summable approximation and remains essential to observables, downgrade the broad conjecture.

**Primary provenance.** `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§15.4–15.6, 17 and 18; `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`, §§2.3 and 5; `SCALAR_HERMITE_MINIMAL_EXPERIMENT_REPORT.md`, §7.

### 8.13 Final frontier ledger

| Statement                                         | Status                                                                                           | Missing bridge                                                                 |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Finite-network causal skeleton                    | **Proved**                                                                                       | None                                                                           |
| Finite-cutoff operator PDE internal geometry      | **Proved where well posed**                                                                      | General cutoff-uniform well-posedness                                          |
| Bounded Riesz shared transpose                    | **Proved**                                                                                       | Compactness is false on bounded balls                                          |
| Finite-time energy bounds and time equicontinuity | **Proved for the trainable Lagrangian state along sufficiently regular finite-cutoff solutions** | General well-posedness, derived forward/adjoint bounds, and source compactness |
| Plain $L^2$ local Lipschitzness                   | **False**                                                                                        | Must use stronger-to-weaker topology                                           |
| Fixed-query Hermite projection convergence        | **Proved**                                                                                       | Uniformity over trained reachable family                                       |
| Source-weighted compactness estimate              | **Open**                                                                                         | Propagation through learned row and unbounded adjoint                          |
| Cutoff-uniform forced stability                   | **Open**                                                                                         | Full response/source error control                                             |
| Compact-time pure-Hermite convergence             | **Open**                                                                                         | Compactness, uniqueness, consistency, stability                                |
| Fixed-$L$ trained causal width limit              | **Open for this exact model in the supplied corpus**                                             | Joint row/column DMFT with learned history                                     |
| Trained iid-depth homogenization                  | **Open**                                                                                         | Centered cancellation plus mean identification                                 |
| Shared-transpose/Onsager identification           | **Open**                                                                                         | Conditional mean theorem                                                       |
| Ordered dense-limit equality                      | **Open**                                                                                         | All preceding identification bridges                                           |
| All-time uniform approximation                    | **Open**                                                                                         | Residual/arclength/coercivity tail mechanism                                   |
| Response-enriched finite PDE                      | **Plausible, not emitted**                                                                       | Minimal state and full outgoing residual                                       |
| Broad admissible finite-PDE existence             | **Open**                                                                                         | Some witness must complete all bridges                                         |

The strongest defensible conclusion is:

> The explicit operator–Hermite PDE has exact finite-cutoff mathematical structure and compelling low-order empirical performance. Its arbitrary-accuracy theorem is blocked by a precise compactness-and-stability bundle, followed by a separate ordered dense-limit identification and an all-time tail argument. The causal response/Onsager calculus supplies a principled route either to close the pure state or to identify the minimal missing state; it is not yet a completed alternative PDE.

## Chapter 9 — Authoritative project-wide synthesis

### 9.1 One thesis, several logically different laboratories

The project is not a sequence in which one model gradually turns into another. It is a family of theorem laboratories organized around one compression question.

The canonical residual branch asks for a positive theorem in the standard regime. The quadratic branch attacks stronger closure mechanisms in a deliberately tractable but singular model. The non-standard branch records exact positive or negative results obtained after changing one of the central qualifiers. These branches interact by transferring methods and warnings, not by silently transferring conclusions.

| Branch                                               | What it legitimately tests                                                                                                                                                | What it does not establish                                                                              |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Standard residual $\tanh$/bounded-activation program | Whether a deep, fully dense, fully trained Euclidean-$\mu$P model admits a finite causal PDE; internal correctness and empirical adequacy of the operator–Hermite witness | Convergence of the Hermite hierarchy, the ordered dense limit, or all-time accuracy                     |
| Two-hidden-layer quadratic/Gaussian program          | Proved derivative-history forest and width-counting algebra; conditional-on-(FW) failure of the initial Taylor closure; conditional branchwise continuation-capacity obstruction; residual-clock stability | A no-go theorem for bounded activations, residual depth, the untagged aggregate loss, or every non-Taylor closure |
| Normalized/projected variants                        | Exact vector fields, source-reported jets, and frozen-reduction nonclosure diagnostics under the altered geometry                                                         | A full-system nonclosure theorem or transfer of the raw positive-coefficient lower bound, because projector terms introduce signs |
| Smooth-depth or tied/coherent models                 | Exact neural-ODE/Dyson descriptions when a genuine regular $W(s)$ exists                                                                                                  | The iid-across-depth dense model, whose raw matrices do not converge to a smooth field                  |
| Shallow mean-field models                            | Distributional transport PDEs when the neuron law itself is a sufficient state                                                                                            | Resolution of the deep $W/W^\top$ response problem                                                      |
| Finite-matrix response surrogates                    | Rapid decay of chronological response grade and correctness of oriented causal identities                                                                                 | A width-independent finite PDE, because the tested surrogates retain dense matrices                     |
| Trajectory-fitted POD/EDMD or oracle source profiles | Basis-efficiency diagnostics and upper bounds on empirical compressibility                                                                                                | An admissible architecture-derived closure                                                              |

The comparison reveals the common lesson. Determinism is not the bottleneck. The bottleneck is whether the causal information generated by repeated dense operator reuse has finite sufficient statistics compatible with nonlinear representation dynamics.

### 9.2 Authoritative claim ledger

Write $E_k(T)$ for the worst-case observable error, over the declared parameter class and $0\le t\le T$, of the $k$-th member of a predeclared admissible compiler family from its canonical compiled initialization. The observable metric is

$$
d_{\mathrm{obs}}\bigl((f,G),(\widetilde f,\widetilde G)\bigr)
=
\|f-\widetilde f\|_2
+
\sup_{s\in[0,1]}\|G(s)-\widetilde G(s)\|_F,
$$

using the uniformly interpolated depth-Gram target rather than merely pointwise-in-depth values. Write $E^{\mathrm H}_{r_{\mathrm H}}(T)$ for the corresponding pure-Hermite family. Internal restartability of such a PDE is distinct from dense-restart sufficiency, which additionally requires a state correspondence and a continuation estimate for physically consistent positive-time dense states.

#### 9.2.1 Exact finite-system and finite-PDE identities

| ID  | Claim                                                                                                                                                                                 | Status     | Scope                                                                                                                                                                                                                                                    |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C1  | The finite dense residual network has the stated forward recursion, adjoint recursion, Euclidean-$\mu$P parameter flow, sensitivity-Gram tangent kernel, and loss dissipation.        | **Proved** | Finite $n,L$, stated smooth activation and squared loss                                                                                                                                                                                                  |
| C2  | Eliminating a trained dense matrix exactly produces history integrals and two-time correlations in both $W h$ and $W^\top\beta$.                                                      | **Proved** | Finite $n,L$; algebraic identity                                                                                                                                                                                                                         |
| C3  | There are algebraic continuation witnesses that agree on the audited present-time summaries or retained actions but separate in a future dense response direction.                    | **Proved** | Unrestricted restart classes containing the displayed witnesses; no canonical reachability claim and no no-go theorem for an enriched state                                                                                                              |
| C4  | At each finite Hermite cutoff, the operator–Liouville system uses one shared forward/transpose operator and is the Euclidean gradient flow of its finite-dimensional row-coordinate projection coupled to a law-valued state. | **Proved** | Internal PDE theorem for sufficiently regular solutions with the stated moment/no-flux conditions on their interval of existence; a general global well-posedness theorem is not supplied                                                        |
| C5  | The induced finite-cutoff tangent kernel is positive semidefinite and the PDE loss is nonincreasing.                                                                                  | **Proved** | Internal PDE theorem for sufficiently regular, well-posed finite-cutoff flow; not dense-network equality                                                                                                                                                 |
| C6  | Odd activation plus symmetric initialization makes even source-Hermite shells inert.                                                                                                  | **Proved** | Odd activation, symmetric initialization, and uniqueness of the symmetry-preserving flow; numerical preservation additionally requires parity-compatible cubature                                                                                        |
| C7  | The pure chronological forward tail and exact-source backward tail have factorial Volterra bounds.                                                                                    | **Proved** | Pathwise at fixed $n,L$ under finite $B_{v,T},B_{w,T},\Lambda_T$ (Chapter 6 abbreviates the forward bound as $B_T$); width/depth uniformity requires uniform envelopes; the coupled $E_{A,K,T}$ source defect and nonlinear-tree defects remain separate |
| C8  | The frozen shared-transpose/Riesz operator is bounded on $L^2$ but not compact.                                                                                                       | **Proved** | Frozen isonormal operator; learned and nonlinear terms require separate control                                                                                                                                                                          |
| C9  | Finite-cutoff dissipation yields finite-time state bounds and time equicontinuity for the trainable Lagrangian variables.                                                             | **Proved** | Sufficiently regular finite-cutoff solutions; does not prove global well-posedness, derived $h,p$ bounds, source compactness, or finite all-time arclength                                                                                               |
| C10 | Hermite projection converges strongly on each fixed source query and uniformly on compact query sets.                                                                                 | **Proved** | Fixed $L^2$ queries/compact query families; not uniformly on the unit ball or automatically on the trained reachable family                                                                                                                              |

#### 9.2.2 Quadratic theorem-laboratory claims

The following proved structural lemma supports C12–C13 but is not assigned a new project claim ID: every raw order-$k$ descent derivative history has a bipartite-forest occurrence graph with component count equal to its explicit normalization exponent, its Wick quotient has width order $n^{c_{\mathrm F}-\beta-r_{\mathrm F}}$, and leading eligibility requires $c_{\mathrm F}=r_{\mathrm F}$ and $\beta=0$. The result includes all three trained parameter groups. The remaining expectation, doubled-covariance, and $L^1$ bridge is precisely (FW).

| ID  | Claim                                                                                                                                                                                  | Status                      | Scope                                                                                                                                                                                           |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C11 | Squared-loss flow is a residual-gated time change of readout ascent, and a known small feature-profile defect yields a uniform-in-physical-time loss defect.                           | **Proved**                  | Common initial output/clock, target-reaching monotone profiles, and the stated derivative lower/upper bounds                                                                                    |
| C12 | The prescribed initial Wick–Taylor coefficients have a factorial lower bound along an odd subsequence and hence zero radius.                                                           | **Exact under assumptions** | Conditional on the remaining (FW) expectation/covariance/$L^1$ bridge; its derivative-history forest and leading-width topology are proved in Q0; two-hidden-layer, one-input quadratic model with the stated Gaussian initialization and order of limits |
| C13 | Positive Wick–Taylor partial sums send every subtarget hitting time to zero, so the associated continuous finite closures do not converge uniformly on an interval containing $t=0$.   | **Exact under assumptions** | Conditional on the same remaining (FW) bridge; the specific Taylor compiler, iterated finite-width shadowing claim, and physical-time construction                                              |
| C14 | The zero-radius result rules out every finite-source or real-axis compiler.                                                                                                            | **Falsified in scope**      | Conditional on (FW), the surviving theorem rules out the specified positive Taylor/analytic compiler classes. The separate §5.7.5 result conditionally excludes a narrow exact branchwise finite-commuting-source grammar. Neither covers all signed, nonanalytic, aggregate, or response-enriched constructions |
| C15 | The displayed natural hierarchy fails to close at every finite rectangular cutoff in the two frozen normalized top-block reductions.                                                       | **Proved**                  | Follows from the exact recurrences (5.64)–(5.65); analogous full-system graph proliferation is diagnostic, not a proved nonclosure theorem, and no no-go applies to every nonlinear statistic     |
| C16 | Under the asserted tagged-site DMFT representation and selection hypotheses, the relaxed quadratic loss is step-like and has the stated uniform separation from continuous surrogates. | **Exact under assumptions** | Requires the stated Volterra law, independence, continuity, positive local response, and monotone/no-overshoot target selection; the network-to-DMFT identification is not proved in the corpus |

#### 9.2.3 Empirical residual-PDE claims

| ID  | Claim                                                                                                                                                                     | Status                    | Scope                                                                                                                                                                       |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C17 | The canonical $P=5$ PDE closely predicts dense output and hidden-Gram motion while both undergo $O(1)$ feature learning.                                                  | **Empirically supported** | Reported canonical finite $n,L$, seed ensemble, time window, and numerical resolution                                                                                       |
| C18 | The canonical PDE is exactly equal to or statistically indistinguishable from the dense reference.                                                                        | **Falsified in scope**    | The Gram discrepancy is small but statistically resolved                                                                                                                    |
| C19 | The same low-order compiler and construction, without case-specific trajectory fitting, transfers across the fourteen tested data/label/sample/activation configurations. | **Empirically supported** | Descriptive portability on a finite suite; not simultaneous category-wide certification                                                                                     |
| C20 | The agreement is explained by lazy features, identity dynamics, or a scalar loss clock.                                                                                   | **Falsified in scope**    | The matched observables and tested configurations; not a no-go for every reduced surrogate                                                                                  |
| C21 | A fixed gain-adjusted linear model explains the nonlinear Gram dynamics.                                                                                                  | **Falsified in scope**    | Designed paired initialization-gain sine comparison; adaptive/state-dependent linear surrogates remain untested, and the joint three-observable $5\%$ gate fails on loss    |
| C22 | Centered trained-depth fluctuations have variance of order $L^{-1}$.                                                                                                      | **Empirically supported** | The reported reduced diagnostic; does not identify the surviving conditional mean                                                                                           |
| C23 | Pure-Hermite adjacent approximations form a convergent empirical Cauchy sequence.                                                                                         | **Open**                  | No replicated aggregate contraction on the parity-correct cofinal ladder                                                                                                    |
| C24 | Pure Hermites empirically diverge.                                                                                                                                        | **Open**                  | The old $5\to15\to35$ argument is superseded; later aggregate increments are noncontracting but small and nondecisive, so neither convergence nor divergence is established |

#### 9.2.4 Central theorem claims

| ID  | Claim                                                                                                                         | Status   | Decisive missing bridge                                                                                                       |
|-----|-------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------|
| C25 | The ordered trained limit $n\to\infty$ at fixed $L$, then $L\to\infty$, exists uniquely for the canonical model.              | **Open** | Fixed-depth causal width theorem plus trained-depth homogenization                                                            |
| C26 | The infinite operator flow exists uniquely in a topology controlling nonlinear products and observables.                      | **Open** | Well-posedness beyond a plain $L^2$ ball                                                                                      |
| C27 | Finite Hermite PDEs converge on each compact training interval to the infinite operator flow.                                 | **Open** | Collective source compactness/weighted regularity, consistency, uniqueness, and cutoff-uniform forced stability               |
| C28 | The infinite operator flow is the ordered dense limit, including the correct shared-transpose/Onsager mean.                   | **Open** | Joint row/column conditioning and homogenized conditional-mean identification                                                 |
| C29 | Compact-time convergence upgrades to uniform all-time approximation.                                                          | **Open** | Residual integrability/finite arclength plus eventual coercivity, contraction, or another tail argument                       |
| C30 | For one predeclared admissible family, $\inf_k E_k(T)=0$ for every $T<\infty$.                                                | **Open** | Broad compact-time existence conjecture; the selected order may depend on $T$                                                 |
| C31 | For one predeclared admissible family, $\inf_k E_k(\infty)=0$.                                                                | **Open** | Central all-time existence conjecture with horizon-independent state complexity                                               |
| C32 | The pure-Hermite family satisfies $\inf_{r_{\mathrm H}}E^{\mathrm H}_{r_{\mathrm H}}(\infty)=0$.                              | **Open** | One witness only; neither canonical-sequence convergence nor a favorable subsequence is established                           |
| C33 | For every $T<\infty$, a response-enriched Hermite family converges on $[0,T]$ along one fixed, predeclared diagonal of finite $(r_{\mathrm H},K,J,N)$ cutoffs. | **Open** | Compact-time version only; the response state and finite drift compiler have not been fully emitted, and summable chronological tails alone are insufficient |
| C34 | The compiled PDE state is a restart state for the ordered dense dynamics at physically consistent positive times.             | **Open** | Dense-to-PDE state correspondence plus a uniform continuation estimate; internal PDE autonomy alone is insufficient           |
| C35 | The all-time direct finite-network consistency statement (2.7) holds, controlling a finite PDE family against finite $n,L$ without first postulating the ordered limit. | **Open** | Joint finite-network consistency and quantitative width/depth/cutoff error bounds, with the explicit all-time horizon and nested limit order in (2.7) |

### 9.3 Supersession ledger

The main text uses only the corrected formulation. This ledger preserves why earlier claims changed.

| Earlier formulation                                                                                 | Defect found                                                                                                                                                            | Authoritative replacement                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| “One source” by itself expresses nontrivial compression.                                            | One real/source coordinate can encode an arbitrary trajectory or any finite ODE.                                                                                        | Source dimension must be paired with coefficient provenance, fixed grammar, bounded description complexity, autonomy, and uniformity over a declared class. |
| A complete fixed-order Wick/concentration theorem had already been established.                     | Q0 proves the raw forest invariant and leading width topology but gives only a compressed variance sketch; the expectation, doubled-covariance, and $L^1$ bridge is absent. | Retain the structural theorem as proved and every deterministic-limit consequence as conditional on the remaining hypothesis (FW).                         |
| “Only a Taylor-tail lemma remains.”                                                                 | Under (FW), the concrete Wick–Taylor coefficients have zero radius.                                                                                                     | Global clock stability is proved, but error production for that compiler is large; any surviving construction must be nonperturbative and real-axis.        |
| The quadratic Wick divergence disproves the broad PDE thesis.                                       | The proof uses an unbounded polynomial activation/readout and a positive compiler.                                                                                      | It is a model- and compiler-specific no-go; bounded residual activations remain a separate program.                                                         |
| The tagged-site instantaneous-fitting claim is unconditional.                                       | The causal DMFT representation and response-kernel properties were asserted rather than derived in the project source.                                                  | The Volterra comparison is an exact conditional theorem; DMFT identification is an explicit assumption.                                                     |
| Raw iid depth matrices can be smoothly interpolated as $W(s)$.                                      | Their slice-to-slice fluctuations do not vanish in the required manner.                                                                                                 | Take width first, then homogenize residual depth at the level of conditional means and centered innovations.                                                |
| The $K/J/N$ compiler already emitted a finite PDE.                                                  | Field tables, drift graph, kernels, and cutoff schedule were not fully specified.                                                                                       | The oriented identities and factorial propagation bound survive; the response-enriched PDE is a leading open construction.                                  |
| The hierarchy $P=5\to15\to35$ measures increasing Hermite resolution.                               | The even shell is exactly inert under odd symmetry.                                                                                                                     | Use the parity-correct ladder $P=5\to35\to126\to\cdots$.                                                                                                    |
| Newly opened-mode ratios $0.029$–$0.0589$ are the trained truncation tail.                          | They measure a lifted outgoing source, not the full coupled Cauchy increment.                                                                                           | Aggregate state, observable, and feedback increments are the relevant tail diagnostics; these have not contracted on the available ladder.                  |
| The frozen transpose needs Malliavin differentiability merely to exist.                             | Riesz representation already gives a bounded Hilbert adjoint.                                                                                                           | Differentiability/response regularity is needed only for stronger weighted estimates and causal identification, not bare boundedness.                       |
| Plain $L^2$ gives cutoff-uniform local Lipschitz stability.                                         | Products such as $p\,\delta z$ need not lie in $L^2$; the Gaussian terminal adjoint is unbounded.                                                                       | Work in an $L^4$, Gaussian Sobolev/Orlicz, or strong-to-weak topology, or use a variational/weak–strong argument.                                           |
| A favorable realized secant ratio proves stability.                                                 | One forcing direction is not the worst-case propagator norm.                                                                                                            | Cutoff-uniform forced stability remains open.                                                                                                               |
| Low source degree means an effectively linear activation.                                           | Every cutoff evaluates the full nonlinear $\sigma$ and $\sigma'$; only label dependence is truncated.                                                                    | The sine stress confirms that low source degree can encode strongly nonlinear activation dynamics.                                                          |
| The $P=5$ PDE is exact or below the dense noise floor.                                              | The dense/PDE discrepancy is statistically resolved.                                                                                                                    | It is close but distinguishable.                                                                                                                            |
| The fourteen cases certify universal generalization.                                                | The family is finite, some numerical gates are unresolved, and simultaneous certification is underpowered.                                                              | They establish broad tested portability, not a uniform theorem.                                                                                             |
| Autonomy of the finite PDE proves that its state is a sufficient restart state for the dense limit. | Internal PDE continuation and dense-state sufficiency are different assertions.                                                                                         | Dense-restart sufficiency requires a state correspondence on physically consistent positive-time dense states and a continuation-error theorem.             |
| The available Hermite data establish convergence or divergence.                                     | The parity-invalid comparison was superseded, while the corrected aggregate increments have not shown replicated contraction and are not a lower bound on target error. | Both empirical convergence and empirical divergence remain open.                                                                                            |

### 9.4 The exact threshold for a result beyond TP and DMFT

A result does not go beyond TP or DMFT merely because it produces deterministic trajectories. TP IV rigorously proves fixed-depth width limits for every fixed finite compiled training computation and retains the Onsager corrections generated by shared $W/W^\top$ use. TP VI develops an ordered width-then-depth covariance/response continuum, with a rigorous dyadic Cauchy analysis and a qualified fixed-point step in its linear laboratory, and explicitly heuristic claims for the general nonlinear model. Bordelon–Pehlevan DMFT derives a formal self-consistent nonlinear feature-learning theory whose state contains two-time feature, gradient, and response kernels. These are causal descriptions; their native computation graph or two-time memory grows with the requested horizon. The additional result sought here is a controlled, architecture-compiled, horizon-independent autonomous realization of the canonical ordered target. Neither framework is claimed incapable of supplying ingredients for its proof or of admitting a future compression.

For a fixed compact horizon $T$, the first theorem of genuinely new type would have the following form. It presupposes that the ordered target observable law has been constructed and is unique on $[0,T]$.

> **Compact-time canonical-start finite-causal-realization theorem.** For every $\varepsilon>0$ and every regularity-bounded parameter class $\mathcal U_R$, an architecture-local compiler produces an autonomous finite-field PDE $\mathsf P_{\varepsilon,T,R}$. Its coefficients and canonical initialization use only permitted model data; its field count and source dimension may depend on $\varepsilon,T,R,m,d$ but not on $n$ or $L$; its declared state defines an internally restartable PDE semigroup; and $$
> \sup_{\vartheta\in\mathcal U_R}
> \sup_{0\le t\le T}
> d_{\mathrm{obs}}\!\left(
> \mathcal O_\vartheta(t),
> \mathcal O_{\mathsf P_{\varepsilon,T,R},\vartheta}(t)
> \right)\le\varepsilon .
> $$

This theorem would be strictly additional to a native TP/DMFT description because it would provide a predeclared, architecture-local, finite-field autonomous approximation hierarchy from canonical compiled starts. It would yield:

1.  an autonomous semigroup on macroscopic surrogate states;
2.  a controlled architecture-derived approximation hierarchy;
3.  direct access to representation observables;
4.  a state type whose definition does not grow with elapsed training time.

It would **not**, by itself, prove that an arbitrary physically consistent positive-time dense state can be compressed into the current PDE state. That stronger conclusion requires a restart map $\mathcal C_k$ and a continuation estimate. Schematically, for every admissible dense-limit state $X(t_*)$ reachable at time $t_*$,

$$
\sup_{0\le u\le T-t_*}
d_{\mathrm{obs}}\!\left(
\mathcal O_{X(t_*)}(u),
\mathcal O_{\mathsf P_k,\mathcal C_k(X(t_*))}(u)
\right)
\le \varepsilon,
$$

where $\mathcal C_k$ is determined from permitted present-state information and does not replay or encode the full past. This **restart-robust finite-sufficient-statistic theorem** is the form that would justify saying that the native history-valued state itself has been finitely Markovized.

For one predeclared admissible family, the strongest landmark theorem adds horizon independence:

$$
\forall\varepsilon>0\ \exists k(\varepsilon)<\infty:
\quad
\sup_{\vartheta\in\mathcal U}
\sup_{t\ge0}
d_{\mathrm{obs}}
\left(
\mathcal O_\vartheta(t),
\mathcal O_{\mathsf P_{k(\varepsilon)},\vartheta}(t)
\right)
<\varepsilon ,
$$

with state type and complexity independent of the requested training horizon. This would be a global finite normal form for deep feature-learning dynamics. It would not imply that every numerical solver is cheaper than every DMFT solver, nor that TP/DMFT could not be used in its proof.

### 9.5 Ranked theorem program

The compact-time work has two parallel branches. Neither must wait for the other until their identification join. The ranking below reflects proof dependency, not perceived ease.

#### 9.5.1 Dense-target branch

1.  At fixed residual depth $L$, prove the width-$\infty$ causal law jointly for forward actions, shared-transpose reuse, learned row history, and reciprocal response.
2.  Prove existence, uniqueness, and observable continuity of that fixed-$L$ target on compact training intervals.
3.  Homogenize trained iid residual depth by decomposing each reused action into conditional mean plus centered innovation. Control the accumulated innovation in the observable topology and derive, rather than assume, the surviving conditional/shared-transpose mean.

The observed $L^{-1}$ centered-variance scaling supports only an innovation-decay diagnostic; it does not identify the conditional mean or prove this branch.

#### 9.5.2 Operator/Galerkin branch

1.  Define an infinite operator-flow phase space in which the nonlinear drift, boundary data, observables, and frozen transpose are well posed.

2.  Decide whether the learned response $R=D_\epsilon c$ is measurable from the Eulerian row law. If not, promote a finite response/history sector explicitly.

3.  Establish reachable-state source compactness, for example through a Gaussian number-operator estimate

    $$
    \sup_{r_{\mathrm H}}\sup_{0\le t\le T}
    \mathcal E_\alpha[Y_{r_{\mathrm H}}(t)]<\infty
    $$

    for some regularity order $\alpha>0$, together with fourth-moment, Gaussian Sobolev, or Orlicz control adequate for nonlinear products. The energy must include the frozen and learned transpose sectors and, if used, the query-restricted learned response

    $$
    (\sigma_w I+R)H_q.
    $$

    The estimate must control collective tails, not merely individual coefficients.

4.  Prove strong-to-weak nonlinear consistency, uniqueness or weak–strong uniqueness, and cutoff-uniform forced stability. A representative target is

    $$
    \sup_{t\le T}
    \|Y_{r_{\mathrm H}}(t)-\mathcal P_{r_{\mathrm H}}Y(t)\|_{\mathrm{weak}}
    \le
    G_T
    \left[
    \delta_{r_{\mathrm H}}
    +
    \int_0^T
    \|F_{r_{\mathrm H}}(\mathcal P_{r_{\mathrm H}}Y)
    -\mathcal P_{r_{\mathrm H}}F(Y)\|_{\mathrm{strong}}
    \,dt
    \right],
    $$

    where $\delta_{r_{\mathrm H}}$ is the initial projection/state defect and $G_T$ is independent of $r_{\mathrm H}$. The chronological response hierarchy is a candidate propagator tool, subject to its operator-envelope hypotheses. A global plain-$L^2$ Lipschitz constant is not available.

5.  Conclude compact-time Galerkin convergence to the unique infinite operator flow.

#### 9.5.3 Identification join

Once both branches exist, prove that the operator flow’s conditional transpose term equals the homogenized dense shared-transpose/Onsager response and that their observable laws agree. Only this join upgrades internal Galerkin convergence into approximation of the intended network. Neither branch alone proves the central closure statement.

#### 9.5.4 Downstream all-time and restart-robust upgrades

After compact-time identification, seek one of:

- integrability of the residual;
- finite feature/residual arclength;
- eventual tangent-kernel coercivity;
- a modulated contraction near the terminal manifold;
- or an explicit plateau-to-tail restart theorem.

Loss dissipation alone is insufficient because it does not coerce all hidden directions. Separately, a dense-restart theorem needs the positive-time state correspondence and continuation bound of Section 9.4; it does not follow automatically from canonical-start all-time accuracy.

#### 9.5.5 Separate quadratic fixed-order completion track

This side track does not alter or precede the residual-network branches above. Q0 removes derivative grammar, bookkeeping for all three trained blocks, width power counting, and leading topological classification from the missing work. The remaining tasks are:

1.  enumerate the finite equality partitions and their falling-factorial index counts, and prove convergence of $\mathbb E[C_{n,k}]$ for every fixed $k$;
2.  complete the doubled-forest covariance enumeration, including different raw component counts, every cross-replica $W$-pairing, shared upper $a$ indices, shared lower primitive-$x$ indices, and the induced noncentered $h=x^2/2$ cross-moments;
3.  prove the aggregate $O(n^{-1})$ covariance estimate and deduce $L^2$, hence $L^1$, convergence to the leading-contraction sum.

A separate hypercontractivity/uniform-integrability theorem is unnecessary on this route: completed expectation convergence and variance decay already imply (FW). The asymptotic-freeness and branch-separation lemmas used by the distinct §5.7.5 continuation-capacity result remain another narrowly scoped proof obligation.

### 9.6 Branch-selection and falsification rules

#### Continue the pure-Hermite branch if

- a positive source-regularity estimate closes on the static Eulerian state;
- the shared transpose has a vanishing collective projection tail on reachable trajectories;
- and a cutoff-uniform forced gain is established.

#### Promote response coordinates if

- a specific causal response/history coefficient survives at order one;
- it is not a measurable function of the static row law and boundary fields;
- and its chronological or kernel tail is summable.

That result would disfavor, and with a quantitative target-error lower bound could falsify, the static pure-Hermite witness. It would remain favorable to the broad finite-PDE thesis if the promoted response sector has a summable finite hierarchy.

#### Treat canonical complete-sequence Hermite convergence as falsified if

a proved, parity-correct cofinal sequence has a nonvanishing lower bound on a target-controlling Cauchy increment. Numerical noncontraction is adverse evidence, not a theorem.

This rejects convergence of the prescribed complete sequence. It does not exclude a favorable subsequence and therefore does not by itself falsify the witness statement

$$
\inf_{r_{\mathrm H}}E^{\mathrm H}_{r_{\mathrm H}}(T)=0.
$$

#### Treat the pure-Hermite witness as falsified only if

$$
\inf_{r_{\mathrm H}}E^{\mathrm H}_{r_{\mathrm H}}(T)>0
$$

for some declared compact horizon and parameter class, or, for the all-time witness,

$$
\inf_{r_{\mathrm H}}E^{\mathrm H}_{r_{\mathrm H}}(\infty)>0.
$$

A reachable bounded-energy escape mechanism, noncompact static transpose, nonvanishing consistency residual, or unbounded forced gain becomes such a falsifier only after it is converted into this observable target-error floor. A two-state continuation witness is decisive for restart-robust pure-Hermite closure only when both states are physically reachable, agree on the entire declared PDE state, and have a controlled future observable separation.

#### Treat the broad all-time finite-closure thesis as falsified only if

$$
\forall\ \text{predeclared }\mathfrak A\text{-admissible families }\{\mathsf P_k\},
\qquad
\inf_k E_k(\infty)>0.
$$

An essential nondecaying causal continuum or a lower bound on every finite response/history sector would establish this only if it yields that universal observable-error bound. Until $\mathfrak A$ is given as a formal grammar rather than only the semantic filters of §2.3, this is a research contract, not a theorem with a machine-checkable quantifier domain. Failure of the ordered dense observable limit would invalidate the present target contract rather than, by itself, prove a no-go theorem for every differently formulated limit.

Failure of Taylor closure, natural moments, pure Hermites, or one fitted basis is not such a result.

No current result meets either theorem-level falsifier.

### 9.7 Final project assessment

The strongest defensible conclusion has two halves.

The constructive half is already substantive:

> An architecture-compiled, autonomous, width-independent nonlinear operator–Liouville candidate has been constructed from the finite-network algebra and Gaussian initialization of a standard dense Euclidean-$\mu$P residual architecture. Its finite-cutoff gradient, transpose, kernel, moment, and dissipation structure is exact for sufficiently regular solutions on their interval of existence. Its smallest parity-correct realization predicts active dense feature dynamics with low reported error across a finite tested family, subject to the stated numerical, statistical, and simultaneous-certification limitations. Identification with the ordered dense limit remains open.

The theorem-level half remains a research program:

> No source in the audited corpus proves that increasing the cutoff converges, that the infinite operator flow equals the ordered dense limit, or that any finite family is uniformly accurate for all training time. The decisive bridge is a causal compactness-and-identification theorem, probably combining weighted source regularity with an explicit response/Onsager state.

If that bridge is proved, the result would go beyond the native form of TP and DMFT by showing that a genuinely deep feature-learning theory with two-time causal structure has a finite autonomous macroscopic realization. If the pure-Hermite witness fails but a small response-enriched state succeeds, the central thesis still survives. Only a quantitative lower bound over every predeclared admissible family would isolate an irreducible-memory obstruction to the broad thesis.

That is the correct current scientific position: a nontrivial empirical and structural discovery, a sharply posed landmark conjecture, several rigorous scoped obstructions, and one identifiable theorem bottleneck—not a completed theory and not a failed idea.

## Appendix A — Unified notation and semantic conventions

### A.1 Independent coordinates

| Symbol                                                       | Meaning                                                                                                        |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| $t$                                                          | Physical training time                                                                                         |
| $s\in[0,1]$                                                  | Continuous residual-depth coordinate                                                                           |
| $\ell\in\{0,\ldots,L-1\}$                                    | Discrete residual-layer index                                                                                  |
| $n$                                                          | Hidden width                                                                                                   |
| $L$                                                          | Residual depth                                                                                                 |
| $m$                                                          | Number of training samples                                                                                     |
| $d$                                                          | Input dimension                                                                                                |
| $q,r\in\{1,\ldots,m\}$                                       | Training-sample indices                                                                                        |
| $r_{\mathrm H}$                                              | Maximum source-Hermite degree                                                                                  |
| $P_{r_{\mathrm H}}=\binom{d+1+r_{\mathrm H}}{r_{\mathrm H}}$ | Full number of source Hermite modes through degree $r_{\mathrm H}$ for the canonical $(d+1)$-dimensional label |
| $K$                                                          | Chronological response grade                                                                                   |
| $J$                                                          | Nonlinear differentiation/tree grade                                                                           |
| $N$                                                          | Depth or numerical-resolution grade                                                                            |
| $\tau$                                                       | Feature time/readout-ascent time in the quadratic laboratory                                                   |

Training-time Taylor order, source-Hermite degree $r_{\mathrm H}$, response grade $K$, tree grade $J$, and depth resolution $N$ are independent approximation axes. No convergence statement in one axis is evidence of convergence in another without an explicit bridge.

### A.2 Canonical residual-network variables

| Symbol                                              | Meaning                                                                                                                    |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| $x_q,y_q$                                           | Input and label of sample $q$                                                                                              |
| $B,a,W_\ell$                                        | Input matrix, readout vector, and dense residual matrices                                                                  |
| $h_q^\ell,z_q^\ell$                                 | Hidden state and preactivation                                                                                             |
| $f_q$                                               | Network output                                                                                                             |
| $e_q=f_q-y_q$                                       | Residual                                                                                                                   |
| $p_q^\ell$                                          | Unit-output adjoint                                                                                                        |
| $D_q^\ell=\operatorname{diag}\sigma'(z_q^\ell)$       | Activation Jacobian in the residual branch; $\phi$ is reserved for the quadratic/shallow branch                          |
| $\beta_q^\ell=D_q^\ell p_q^{\ell+1}$                | Backpropagated preactivation message                                                                                       |
| $G^h,G^p,G^\beta$                                   | Normalized Gram matrices of the corresponding fields                                                                       |
| $\Theta$                                            | Tangent kernel, always defined as a sensitivity Gram in the exact finite system                                            |
| $\theta$                                            | Generic immutable Gaussian label in Chapters 1–2                                                                  |
| $\eta=(B_j(0),a_j(0)/A)$                            | Source-column label in §3.8 and Chapters 6–8                                                                               |
| $\xi=(B_i(0),a_i(0)/A)$                             | Target-row label in Chapters 6–8                                                                                           |
| $\epsilon$ or $\omega$                              | Frozen target-row innovation/noise on a chosen coupling                                                                    |
| $\psi_\nu$                                           | Normalized multivariate source-Hermite function                                                                           |
| $H_{\nu q}=\int\psi_\nu(\eta)h_q(\eta)\,\mu(d\eta)$ | Source-column Hermite coefficient of the hidden query in Chapters 6–8                                                      |
| $w=(w_\nu)$                                         | Projected row/operator coefficients                                                                                        |
| $\rho_{s,t}^{\xi}$                                  | Conditional law of $w$ for target-row label $\xi$                                                                          |
| $R=D_\epsilon c$                                    | Lagrangian learned row-noise response on a chosen coupling; whether it is measurable from the Eulerian row law is open     |

Chapters 1–2 use $\theta$ generically because no row/column split is yet needed. Once shared-transpose conditioning is exposed, the roles must not be collapsed: §3.8 and Chapters 6–8 use $\eta$ for a source column and $\xi$ for a target row.

Several symbols are intentionally local and must be interpreted from their chapter:

| Symbol collision | Global or residual usage                                                                | Quadratic/local usage                                                       |
|------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| $K$              | Chronological response grade                                                            | $K_n=W\operatorname{diag}(h)W^\top$ in Chapter 5                            |
| $\gamma$         | Residual-block scale in Chapters 6–8                                                    | Variance parameter of $W$ in Chapter 5                                      |
| $m$              | Number of training samples                                                              | Local factorial index $m=(k+3)/2$ in the zero-radius proof                  |
| $R$              | Row-noise response, or numerical row-innovation cubature count when explicitly declared | A locally defined Gaussian contraction scalar in the normalized calculation |
| $r$              | Training-sample index                                                                   | Never the Hermite cutoff; that cutoff is $r_{\mathrm H}$                    |

In §3.6 the forward chronological source envelope is $B_{v,T}$; §6.11 abbreviates the same role as $B_T$. The backward exact-source envelope is $B_{w,T}$.

The source label $\eta$ is distinct from the subscripted learning-rate multipliers $\eta_B,\eta_a,\eta_{W_\ell}$. The source-weighted space is $\mathcal H_{\mathrm G}^{\alpha}$; $\alpha$ is its regularity order, while $s$ remains residual depth and $\gamma$ remains the residual-block scale throughout the residual branch.

### A.3 Closure semantics

- **Autonomous:** the drift at time $t$ is a function of the current declared state and static model data.
- **Internally restartable:** the same PDE equations can continue from an admissible declared PDE state without replaying the PDE trajectory from initialization.
- **Dense-restart sufficient:** a stronger property requiring a correspondence from physically consistent positive-time dense states to declared PDE states and a uniform future-continuation estimate. Internal PDE autonomy does not prove it.
- **Finite PDE:** finitely many field species over a fixed finite-dimensional source/phase space. It need not be a finite scalar ODE; a law-valued field remains infinite-dimensional as a function.
- **Architecture-local:** the basis, initialization, drift, and readout are generated from the architecture, activation, data class, initialization law, and fixed compiler rules, not from positive-time reference trajectories.
- **Ordered dense limit:** $n\to\infty$ at each fixed $L$, followed by $L\to\infty$.
- **Internal PDE exactness:** an identity that holds within a finite-cutoff PDE. It does not assert that the PDE equals the dense-network limit.
- **Observable convergence:** convergence of the declared outputs and hidden Grams from the specified initial states. It is weaker than equivalence of the full microscopic state and does not by itself imply dense-restart sufficiency.

## Appendix B — Model and assumption matrix

### B.1 Central standard-regime contract

| Requirement      | Canonical interpretation                                                                                                      |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Feature learning | $O(1)$ hidden-representation/Gram motion                                                                                      |
| Depth            | At least two hidden transformations; canonical residual-depth limit                                                           |
| Connectivity     | Fully dense, untied hidden matrices                                                                                           |
| Training         | Input, output, and every hidden matrix train                                                                                  |
| Activation       | Genuine smooth nonlinear activation; bounded smooth odd activations are the principal positive class                          |
| Optimization     | Ordinary Euclidean gradient flow with $\mu$P learning-rate scaling                                                            |
| Parameterization | No low-rank factorization, tying, orthogonal constraint, or frozen block                                                      |
| Limit            | Width first, residual depth second                                                                                            |
| Observables      | Outputs and depth-indexed hidden Grams; loss follows from output                                                              |
| Approximation    | Autonomous, internally restartable, architecture-derived, non-oracular; dense-restart sufficiency is a separate stronger rung |
| Uniformity       | One predeclared family over a stated parameter neighborhood                                                                   |

### B.2 Branch comparison

| Feature                | Quadratic laboratory                                                                  | Canonical residual program                                                               |
|------------------------|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Hidden depth           | Two hidden layers                                                                     | Residual depth $L\to\infty$ after width                                                  |
| Activation             | $\phi(u)=u^2/2$, unbounded                                                            | $\tanh$ principally; other bounded smooth activations tested                             |
| Readout/feature tails  | Gaussian readout coupled to unbounded quadratic features and a positive Wick sector    | Gaussian readout, but bounded hidden activation                                          |
| Data                   | One input/sample in the main proof laboratory                                         | Multiple samples; canonical $m=d=3$, with transfer cases                                 |
| Training               | All displayed blocks train under Euclidean-$\mu$P flow                                | All $B,a,W_\ell$ train                                                                   |
| Main positive theorem  | Residual-clock/global observable stability given a small profile defect               | Exact finite-cutoff projected-gradient, PSD, transpose, and dissipation structure        |
| Main negative theorem  | Zero radius and uniform failure of the prescribed Wick–Taylor compiler, conditional on (FW) | No convergence no-go; pure-Hermite convergence remains open                         |
| Main open bridge       | Nonperturbative real-axis mean-field construction, if this singular model is retained | Ordered dense limit, causal identification, compactness, forced stability, all-time tail |

### B.3 What may and may not be transferred

The following transfer rules are mandatory.

1.  Conditional on (FW), the quadratic factorial lower bound rejects the prescribed ordinary initial Taylor/Wick compiler, and the audited positive analytic compiler classes, in the stated unbounded model. It is a warning against treating time analyticity as automatic; it is not a no-go theorem for bounded residual activations or every real-axis closure.
2.  The residual-clock stability theorem may be reused whenever its monotonicity and small-defect hypotheses are verified. It does not produce the small defect.
3.  The normalized-model jet calculations may be reused as derivative and audit machinery. Their signed projector terms prevent direct reuse of the raw quadratic positivity proof.
4.  The chronological response bound is a depth-ordered real-axis result and survives the quadratic Taylor failure. Its source-substitution and nonlinear-tree residuals remain separate.
5.  Shallow distributional PDE results demonstrate that law-valued closure is possible in special architectures. They do not solve the deep shared-transpose problem.

## Appendix C — Project source and provenance index

### C.1 Supplied core corpus

| Code | File                                                           | Authoritative use in this monograph                                                                                                 |
|------|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| P01  | `approximate_single_source_conjecture_resolution(1).md`        | Zero-radius theorem and physical-time boundary layer conditional on (FW); surviving clock stability                                  |
| P02  | `approximate_single_source_stability(1).md`                    | Exact feature-time reduction and conditional global stability; refers backward to earlier forest power counting but does not reproduce it; its former “only missing tail” conclusion is superseded by P01 |
| P03  | `adversarial_audit_report(1).md`                               | Anti-oracle semantics, compiler classification, real-axis conjecture, topology warnings                                             |
| P04  | `mean_field_single_source_conjecture_audited_resolution(2).md` | Tagged-site Volterra comparison and step-loss conclusion, used only conditionally on its asserted DMFT representation               |
| P05  | `normalized_mean_field_taylor_closure_audit(1).md`             | Exact normalized jets, nonclosure of natural moment lists, signed-projector qualification                                           |
| P06  | `dense_euclidean_continuous_depth_npde_audit.md`               | Exact causal state, response hierarchy, continuation obstructions, original certified-conjecture semantics                          |
| P07  | `dense_euclidean_continuous_depth_pde_conjecture(1).md`        | Continuous-depth conjecture, oriented causal grammar, proof obligations                                                             |
| P08  | `REPORT.md`                                                    | Literal PDE implementation and canonical direct comparison                                                                          |
| P09  | `final_adversarial_pde_audit(1).md`                            | Held-out statistical wording, hard gates, unresolved ordered-limit and cofinal-resolution issues                                    |
| P10  | `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`                  | Canonical residual equations and explicit operator–Hermite Liouville family                                                         |
| P11  | `PDE_GENERALIZATION_FINAL_REPORT(2).md`                        | Fourteen-case transfer study                                                                                                        |
| P12  | `PDE_GENERALIZATION_FINAL_REPORT(3).md`                        | Byte-identical duplicate of P11; no independent evidentiary weight                                                                  |
| P13  | `ACTIVATION_LINEARITY_SMOKING_GUN_REPORT.md`                   | Identity, loss-clock, and initial gain-matched controls                                                                             |
| P14  | `MASTER_NEURAL_PDE_REPORT(2).md`                               | Earlier synthesis; used only where not superseded                                                                                   |
| P15  | `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`                    | Latest text-only synthesis and source map                                                                                           |
| P16  | `MASTER_NEURAL_PDE_REPORT_WITH_FIGURES.md`                     | Same theoretical synthesis as P15 plus figure notes/captions; not byte-identical, but no independent theoretical evidentiary weight |

P11 and P12 are byte-identical and are counted once. P15 and P16 are different files but do not count as two independent theoretical sources.

### C.2 Recovered late reports and positioning material

| Code | File                                          | Authoritative use                                                                                 |
|------|-----------------------------------------------|---------------------------------------------------------------------------------------------------|
| P17  | `SCALAR_HERMITE_MINIMAL_EXPERIMENT_REPORT.md` | Sine nonlinearity stress and scalar degree-$13$ hierarchy                                         |
| P18  | `PDE_PROOF_OBLIGATION_STUDY_FROZEN_REPORT.md` | Frozen gate ledger and statement of missing arbitrary-accuracy evidence                           |
| P19  | `Stabiltiy - Sol/PDE_LEAN_SALVAGE_REPORT.md`  | Ordered-limit, state-sufficiency, generator, and short-amplification diagnostics                  |
| P20  | `PDE_BRIDGEABILITY_RESOLUTION_REPORT.md`      | Exact parity lemma and correction of the $5\to15\to35$ comparison                                 |
| P21  | `PDE_HIGH_TO_LOW_TAIL_ROUND_REPORT.md`        | Degree-seven common-reference tail and orthogonality audit                                        |
| P22  | `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`       | Riesz-adjoint correction, noncompactness, plain-$L^2$ obstruction, and realized secant diagnostic |
| P23  | `positioning_roadmap_dmft_tp.tex`             | Earlier project-positioning memo; used as intent/context, not as authority on external literature |
| P24  | `finite_invariant_differential_algebra_resolution.md` | Original quadratic forest invariant, width exponent, leading double-forest rule, compressed variance sketch, and conditional continuation-capacity argument |

P24 is the exact recovered file associated with Library ID `libfile_f2f2d671cff081919e8c9d0a9156dd14` and File ID `file_0000000044a0820c8fbe2e119bfec4cd`, created 21 July 2026 at 19:48:38 UTC. No originating chat title or message identifier is preserved. `FIXED_ORDER_WICK_CONCENTRATION_THEOREM.md` is not an extant source; it was introduced later as a desired recovery-artifact name.

### C.3 Primary external framework references

1.  Greg Yang and Edward J. Hu, [*Feature Learning in Infinite-Width Neural Networks*](https://arxiv.org/abs/2011.14522) (Tensor Programs IV).
2.  Greg Yang, Dingli Yu, Chen Zhu, and Soufiane Hayou, [*Tensor Programs VI: Feature Learning in Infinite-Depth Neural Networks*](https://arxiv.org/abs/2310.02244).
3.  Blake Bordelon and Cengiz Pehlevan, [*Self-Consistent Dynamical Field Theory of Kernel Evolution in Wide Neural Networks*](https://arxiv.org/abs/2205.09653).
4.  Song Mei, Andrea Montanari, and Phan-Minh Nguyen, [*A Mean Field View of the Landscape of Two-Layer Neural Networks*](https://arxiv.org/abs/1804.06561).

The full arXiv texts of references 1–3 were checked for Version 2.1. Chapter 1 states their models, limit orders, retained state, proof architecture, rigor qualifications, and exact relation to this project. In particular, TP IV is a rigorous fixed-finite-program width theorem; TP VI contains a rigorous dyadic Cauchy analysis in its linear depth laboratory, with the complete fixed-point existence step qualified, and labels its general nonlinear classification as claims supported by heuristic arguments; the cited DMFT is a formal large-width saddle-point derivation whose authors explicitly describe it as not entirely rigorous. These references close the report-level external-comparison gap. This monograph does not claim that TP or DMFT is incapable of producing a finite realization; it claims that the sought horizon-independent restart compression requires an additional theorem.

### C.4 Active repository crosswalk and evidence state

Sections C.1–C.2 preserve the filenames under which the sources were audited. The cleaned repository is organized by scientific program, so those historical names should not be interpreted as current root-level paths. The active correspondence on 31 July 2026 is:

| Historical corpus | Active location | Current reproduction/evidence state |
|---|---|---|
| P01–P05 | [`studies/quadratic_nonclosure`](studies/quadratic_nonclosure/) | Analytical reports only; there is no numerical pipeline to reproduce. |
| P06–P07 | [`studies/dense_response/early_audit`](studies/dense_response/early_audit/) and [`studies/dense_response/long_horizon`](studies/dense_response/long_horizon/) | Both phases retain executable code and results. The long-horizon phase includes its full declared raw NPZ set, processed summaries, figures, tests, and protocol. These finite-matrix response runs are not compiled Liouville-PDE runs. |
| P08–P10 | [`studies/operator_pde/core`](studies/operator_pde/core/) | The direct report is `REPORT.md`, the synthesis is `CONJECTURE_REPORT.md`, and the hostile audit is under `audits/`. Source, tests, protocol, processed evidence, and central figures are active. The original compact release omits its large canonical raw arrays; later locally generated raw trajectories are under [`studies/operator_pde/rerun_2026-07-31`](studies/operator_pde/rerun_2026-07-31/). |
| P11–P12 | [`studies/operator_pde/generalization`](studies/operator_pde/generalization/) | The nonduplicated active report is `FINAL_REPORT.md`. Source, frozen protocols, stage seals, processed evidence, figures, and tests are present. The compact release omits the large full-run raw trajectory set, which the frozen orchestrator can regenerate. |
| P13 | [`studies/operator_pde/activation_controls`](studies/operator_pde/activation_controls/) | Source lineage, protocol, tests, parent release, completed processed evidence, and immutable seals are present. The clean active `results/` tree is intentionally omitted; the runner can regenerate it. |
| P14–P16 | [`archive/earlier_documents/master_syntheses`](archive/earlier_documents/master_syntheses/) | Superseded syntheses retained for research history; they carry no additional evidentiary weight. |
| P17–P22 | [`studies/pde_convergence`](studies/pde_convergence/) | Reports and retained numerical arrays are organized chronologically as phases 01–05. Runners survive for phases 01 and 03–05. The bounded phase-02 ad hoc runner was not preserved, although its report and raw arrays remain. |
| P23–P24 | Historical nonlocal sources described in C.2 | No standalone active copy is present in the current working tree. Their role is restricted to the source-status statements already incorporated and audited in Versions 2.0–2.1; Version 2.2 makes no new claim from them. |
| Original release packages | [`archive/bundles`](archive/bundles/) | Eleven immutable ZIP packages are retained and covered by the archive SHA-256 manifest. |

This crosswalk changes navigation and reproduction status only. Historical filenames remain in the primary-provenance paragraphs because they identify the exact documents against which the monograph was audited. The authoritative scientific status remains the Chapter 9 claim and supersession ledgers.

## Appendix D — Audit protocol and audit record

### D.1 Audit standard

Each drafted chapter fragment was subjected to a first hostile audit and then an independent cross-audit against the other repaired fragments and the available primary reports. The front matter, Chapter 9, and appendices received a separate synthesis-level cross-audit.

1.  **Self-containment:** Are every model, scaling, limit order, observable, topology, and source variable defined before use?
2.  **Claim typing:** Does each theorem, conditional implication, empirical result, open conjecture, and superseded statement carry the correct status?
3.  **Quantifiers:** Is dependence on $\varepsilon,T,m,d,\mathcal U$, regularity, width, and depth explicit?
4.  **Causal sufficiency:** Does any “finite” state hide a matrix, trajectory, history function, future sample, or unbounded-precision encoding?
5.  **Mathematical consistency:** Are dimensions, normalizations, signs, adjoints, boundary conditions, and limit orders compatible?
6.  **Approximation-axis separation:** Are time jets, source degree, response grade, tree grade, and numerical resolution kept distinct?
7.  **Witness/existence separation:** Is a failure of one compiler or basis prevented from becoming a no-go theorem for every closure?
8.  **Error production/propagation separation:** Is a stability theorem prevented from being described as a truncation theorem?
9.  **Empirical validity:** Are finite tests, uncertainty, numerical-resolution gates, and control limitations stated beside their conclusions?
10. **Supersession:** Are corrected conclusions used in the main narrative, with older claims retained only in the ledger?
11. **Cross-chapter notation:** Does every repeated symbol have one stable meaning or an explicit local redefinition?
12. **Provenance:** Can every nontrivial claim be traced to a primary project source or an identified external framework paper?

An audit “pass” means that no known fatal or major internal inconsistency remains under the available sources. It is not a certification of an open theorem. The original Version 2.1 document audits were source audits rather than experimental reruns; the later bounded execution and integrity checks are recorded separately in D.9 and do not convert an unavailable full raw campaign into a reproduced one.

### D.2 Principal repairs made during chapter audits

| Chapter | Principal adversarial issue                                                                                                                                                    | Repair incorporated                                                                                                                                                                                                                       |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1       | Novelty could be claimed merely from determinism; canonical-start approximation could be conflated with dense restart sufficiency                                              | Calibrated the TP IV/TP VI/DMFT baseline; stated non-impossibility; separated internal PDE autonomy from the stronger dense-state correspondence and continuation theorem; made the target topology explicit                              |
| 2       | “One source” and “finite state” can be vacuous; witness-falsifier quantifiers were too weak                                                                                    | Added compiler provenance, uniformity, description-complexity, and anti-oracle clauses; separated canonical-sequence failure from $\inf_kE_k>0$ witness failure and from the universal broad no-go quantifier                             |
| 3       | Row/column labels and response grades could be conflated; the factorial response bound lacked all hypotheses                                                                   | Separated source-column, target-row, row-noise, chronological, tree, and time-jet coordinates; recorded $B_{v,T},B_{w,T},\Lambda_T$, fixed-$n,L$ scope, and the exact-source versus coupled-source distinction                            |
| 4       | Non-standard positive results could be advertised as central-regime progress; a selected scalar derivative word could be mistaken for full frozen dynamics                     | Organized results by the qualifier changed, stated transfer boundaries, and restricted the frozen calculation to the exact subsystem/word actually proved                                                                                 |
| 5       | Stability could be mistaken for convergence; clock initial conditions, limit order, and normalization conventions could be lost; the tagged-site result could be unconditional | Separated propagation from defect production, supplied equal-clock/monotonicity hypotheses and limit order, repaired WN conventions, and made the step-loss conclusion conditional on the asserted tagged-site representation             |
| 6       | Internal PDE exactness could be confused with dense identification or global well-posedness; scaling and $w$-boundary terms were vulnerable to omission                        | Distinguished internal and external claims throughout, restored the $\gamma^2$ variance factor and the $w$-boundary/no-flux qualification, and limited restart statements to well-posed PDE states                                        |
| 7       | Small discrepancy could be called exact; fixed-gain controls and generalization could be overstated; individual modes could be called the aggregate tail                       | Used statistically resolved wording, retained the sine-loss and adaptive-linear caveats, distinguished finite-suite portability from certification, and replaced the invalid ladder with the parity-correct aggregate audit               |
| 8       | Energy boundedness could be mistaken for compactness or plain-$L^2$ stability; dense and operator proof programs were serialized incorrectly                                   | Added the noncompact Riesz example, product-topology obstruction, strong-to-weak alternatives, cutoff-uniform Galerkin requirements, and two parallel branches joined only at identification                                              |
| 9       | Ledger scopes, TP/DMFT threshold, restart semantics, theorem ordering, and falsifier logic did not yet match Chapters 1–8                                                      | Reconciled statuses and transfer boundaries, separated canonical-start from restart-robust realization, made the proof branches parallel, stated target-error falsifiers with correct quantifiers, and recorded duplicate-source handling |

### D.3 Completed fragment-level audit record

The completed fragment-level audit coverage, consolidated directly into this master, is:

| Drafted material                        | First audit emphasis                                      | Independent cross-audit emphasis                                  |
|-----------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------|
| Chapters 1–3                            | Definitions, quantifiers, causal identities, TP/DMFT scope | Cross-branch notation, novelty boundary, and restart semantics    |
| Chapters 4–5                            | Quadratic algebra, conditions, signs, and non-transfer     | Proof dependencies, no-go scope, and normalization qualifications |
| Chapters 6–8                            | Finite-PDE calculus, adjoints, compactness, and stability  | Dense identification, empirical status, and theorem ordering      |
| Front matter, Chapter 9, and appendices | —                                                         | Global claim ledger, supersession, provenance, and references     |

These Version 2.1 audits checked the written arguments and reported source claims. They did not rerun experiments, formally verify proofs, or certify the open limiting constructions. The post-Version-2.1 execution audit in D.9 is a distinct later record.

### D.4 Completed post-merge whole-document audit

The assembled file received a fresh adversarial audit after merge. The audit checked:

- the exact Chapter $1$ through Chapter $9$ hierarchy, with no intermediate Part layer and only Appendices A–D afterward;
- uniqueness and order of every numbered section, subsection, equation tag, claim ID, and detected local reference;
- balanced display and inline mathematics, table structure, full-file Markdown/Pandoc parsing, merge seams, and unresolved-marker hygiene;
- agreement of the canonical residual model, Euclidean-$\mu$P rates, adjoint orientation, tangent kernel, and energy factors across Chapters 3, 6, 8, and 9;
- agreement of physical training time, quadratic feature time, residual depth, source degree, response grade, and numerical-resolution conventions;
- the admissibility, anti-encoding, canonical-start, internal-restart, and dense-restart quantifiers;
- separation of finite-cutoff internal exactness from operator convergence, dense-limit identification, and all-time approximation;
- reconciliation of the Chapter 9 claim and supersession ledgers with Chapters 1–8;
- numerical summaries against the authoritative source tables and earlier source-level audit records;
- duplicate-source handling, including counting P11/P12 once and assigning P15/P16 no independent theoretical weight.

The first whole-file pass found and repaired: a missing additive sign in the Chapter 9 forced-stability template; an overbroad Chapter 8 pure-Hermite falsifier list; a missing explicit finite-description/no-unbounded-encoding admissibility clause; one nonzero-initial-defect qualification in the Chapter 8 stability display; local feature/source-coordinate notation collisions; one GFM table-cell delimiter; and several obsolete TeX `\rm` forms. A second complete mechanical and consistency pass found no remaining fatal or major internal inconsistency. The operative audit record is this appendix; no separate audit document is required to interpret the verdict.

### D.5 First-round audit outcome, superseded in scope

The first-round audit recorded a PASS for source-faithful assembly and internal consistency. Its stronger wording that the monograph was fully self-contained is superseded by the second-round source-level audit below. The first pass also failed to distinguish two facts that Version 2.1 now separates: later reports imported a full fixed-order deterministic-limit theorem, while an earlier primary source genuinely proved only its derivative-forest and width-counting core.

### D.6 Second-round adversarial audit — 28 July 2026

The second round used four deliberately different readings:

1.  a cold-reader self-containment audit, asking whether every declared proved claim could be checked without opening another project file;
2.  a hostile mathematical audit of theorem hypotheses, quantifiers, inequalities, adjoints, tail estimates, and proof-route logic;
3.  a claim-to-source audit comparing the master against the primary and recovered late reports, with duplicate reports given no extra weight; and
4.  a global notation/mechanical audit checking the chapter hierarchy, equation tags, source/row labels, cutoff indices, math delimiters, and full Markdown parsing.

The consolidated high-value findings and dispositions are:

In this table, past-tense dispositions such as “replaced,” “added,”
“corrected,” “split,” “standardized,” and “restricted” are repairs already
applied in Version 2.0 or Version 2.1. They are not recommendations for later
editing. The compiler-domain row is deliberately only a partial repair: the
universal claims are now relative to a declared class $\mathfrak A$, but the
final formal grammar and complexity model remain in the nonlocal-dependency
list below.

| Finding | Severity | Disposition |
|---|---|---|
| The central class $\mathcal U$ was only described as a neighborhood | Major formal gap | Replaced by the explicit five-bound compact class and a typed parameter tuple in §2.2 |
| The universal admissible-family quantifier lacked a formal compiler grammar | Major research-contract gap | Made every universal statement relative to a chosen class $\mathfrak A$; the absence of a final formal grammar remains explicit |
| Later reports promoted an earlier forest/power-counting argument into a full fixed-order $L^1$ theorem | Major self-containment/status flaw | Recovered Q0; proved and reproduced its forest invariant and width rule; isolated the still-missing expectation/doubled-covariance/$L^1$ bridge as (FW); kept every dependent no-go conclusion conditional |
| The projected-gradient, tangent-kernel, and dissipation theorem was asserted without its blockwise proof | Major proof omission | Added the Lagrangian linearization, depth-adjoint cancellation, boundary terms, block gradients, PSD kernel, and squared-gradient identity in §6.8 |
| The learned-transpose tail omitted the factor that makes the tail decay | Major mathematical error | Corrected (8.26) to include $(1+r_{\mathrm H})^{-\alpha/2}$ and stated the required joint moment and row-response hypotheses |
| The compactness and forced-stability routes were conflated | Major logical gap | Split §8.8 into a qualitative compactness--uniqueness proposition and a quantitative forced-gain proposition; defined the gain, topology, initial defect, and consistency residual |
| The claim that plain $L^2$ local Lipschitzness fails lacked a counterexample | Conditional proof gap | Added an explicit Gaussian-tail multiplier sequence in §8.4 |
| Source/row labels, Hermite cutoffs, activation names, depth, and Sobolev exponents collided | Major global-consistency defect | Standardized $\eta/\xi$, $r_{\mathrm H}$, $\sigma/\phi$, $s$, and $\alpha$ throughout and repaired the parity and projected-coefficient formulas |
| The tagged-site comparison omitted $f(0)=0$ and the exact positive-cavity-event hypotheses | Major conditional-theorem gap | Added them and supplied the short continuity argument for the positive path event |
| Full normalized-model nonclosure was inferred from frozen reductions | Major scope overstatement | Restricted the theorem to the displayed frozen reductions; full-system graph proliferation is now labeled diagnostic |
| Smooth-depth, no-low-rank-propagator, and response-kernel qualifications from P06 were missing | Medium completeness gaps | Added the separate smooth-depth equations and limit order, the exact low-rank lower bound, the Volterra diagnostic, and the $SS_M^\top$ PSD caveat |
| TP IV, TP VI, and DMFT were represented only by project summaries | Major external-positioning gap | Checked the full primary texts; added exact architectures, scalings, retained states, proof architectures, theorem-versus-claim distinctions, rigor qualifications, complexity, and the precise additional compression objective in Chapter 1 |
| Q0's signed branchwise continuation-capacity result was absent | Medium local-completeness gap | Added its exponential-versus-subexponential core as a separately scoped conditional implication; exposed the freeness/faithfulness and branch-separation lemmas that Q0 only sketches |

The following nonlocal dependencies remain and are not repaired by assertion:

1.  **Remaining (FW) bridge:** Q0 proves the derivative-history forest invariant, the width exponent, and the leading-contraction topology, but it only sketches variance decay and does not complete expectation convergence, the full doubled covariance enumeration, or the resulting $L^1$ limit. If expectation convergence and variance decay are completed, $L^2$ and then $L^1$ follow directly; a separate hypercontractivity/uniform-integrability route is not required.
2.  **Branchwise continuation lemmas:** Q0's exponential word count and the commutative-jet Hilbert-series bound are reproduced, but a fully checked fixed-degree asymptotic-freeness/faithfulness lemma and a formal branch-separating continuation lemma are still required before §5.7.5 becomes unconditional.
3.  **Frozen Gaussian cutoff:** the source gives only a sketch, not the complete normalized measure-flow and comparison proof.
4.  **Normalized high-order coefficients:** the RMS/WN vector fields are explicit, but the large rational Wick coefficients are source-reported without every contraction table or a verifiable symbolic certificate.
5.  **Empirical reproduction, partially repaired after Version 2.1:** at the 28 July audit, the reports supplied protocols and summaries but not the complete raw arrays and executable code available to the later repository audit. The active tree now supplies code and configurations for most numerical programs, sealed or processed evidence, and a fresh central-PDE rerun. Complete raw campaigns are still not retained for every compact release, the phase-02 ad hoc runner is absent, and the full canonical dense/refinement campaign has not been independently regenerated; see C.4 and D.9.
6.  **Universal compiler class:** the semantic admissibility clauses are explicit, but a final formal grammar and complexity model for $\mathfrak A$ remain to be chosen. Section 5.7.5 formalizes only one restricted branchwise finite-commuting-source category, not the universal class.

The former external-framework item is closed at the level relevant to this report: the full TP IV, TP VI, and Bordelon–Pehlevan DMFT texts have been read and their applicable statements, proof architecture, retained state, limitations, and rigor status are incorporated with primary links and locators. Reproducing their complete proofs would turn this project monograph into a duplicate of those papers and is not needed to make the comparison self-contained. Their results remain external cited theorems or formal derivations, not new proofs claimed by this document.

The genuinely open neural-PDE problems—ordered-target existence, finite-cutoff global well-posedness, source compactness, infinite-flow uniqueness, shared-transpose/Onsager identification, compact-time convergence, dense-limit identification, and the all-time upgrade—are correctly labeled open. They are research gaps, not hidden steps in a claimed completed theorem.

**Second-round verdict.**

- **PASS for internal mathematical/logical consistency and claim discipline after repair.**
- **FAIL for strict proof self-containment.**

No fatal contradiction to the central thesis and no witness-fatal algebraic flaw was found. The document is now an internally rigorous, source-traceable conditional synthesis with a primary-source-audited external baseline. It may be upgraded to a stricter proof-and-reproduction archive only by supplying or completing the six nonlocal project dependencies above. The central ordered-limit and convergence problems remain genuine open research problems, not editorial omissions. Any future result should update the authoritative claim and supersession ledgers rather than append a parallel “final” narrative.

### D.7 Version 2.1 recovery and external-source audit

Version 2.1 received three bounded independent checks after the edits above.

1.  **Recovered-source mathematics.** Q0 was read in full and checked against the displayed finite-width equations. The audit verified the descent/ascent sign translation, all three derivative rewrites, the forest induction, the exponent $n^{c_{\mathrm F}-\beta-r_{\mathrm F}}$, the selected-history conditional Gaussian limit, and the exact boundary between proved structure and the unproved (FW) bridge.
2.  **Continuation-capacity scope.** A separate hostile pass verified the $2^r$ word count and the commutative-jet Hilbert-series bound. It required the freeness/faithfulness and branch-separating continuation steps to remain named assumptions and verified that §5.7.5 makes no claim about the untagged aggregate loss or arbitrary finite PDEs.
3.  **External primary sources and integration.** The full TP IV, TP VI, and Bordelon–Pehlevan DMFT arXiv texts were checked against Chapter 1 and Chapter 9. The final pass found no fatal or major source-status error. It requested one minor local qualification—TP IV Theorem 6.1's pseudo-Lipschitz derivative hypothesis and fixed-step quantifier—which is now included in §1.2.

The final mechanical gate confirms nine ordered chapters, 242 unique equation tags, 35 unique claim identifiers C1–C35, balanced display-math delimiters, successful full-document Markdown/Pandoc parsing, and no unresolved drafting marker or reference to a separate recovery/audit deliverable. The Version 2.1 verdict is therefore:

- **PASS** for the newly integrated local mathematics, external-source fidelity, unified notation, conditional-claim discipline, and mechanical integrity.
- **FAIL** for strict proof/reproduction completeness for the six dependency categories in §D.6. Version 2.2 partially repairs the empirical-reproduction category but does not close it.

This verdict does not upgrade any open conjecture or conditional theorem.

### D.8 Version history and recovery status

| Version | Date | Status |
|---|---|---|
| 1.0 | 27 July 2026 | Initial nine-chapter master and first-round whole-document audit |
| 2.0 | 28 July 2026 | Incorporates the second-round mathematical, scope, source-status, and notation repairs; supersedes the claim of strict proof self-containment |
| 2.1 | 28 July 2026 | Recovers Q0's proved forest/width core and narrowly scoped continuation-capacity argument; narrows (FW) to its true missing bridge; directly audits and incorporates the TP IV, TP VI, and DMFT primary texts; does not upgrade the conditional quadratic no-go theorem |
| 2.2 | 31 July 2026 | Adds the active repository crosswalk and post-Version-2.1 execution audit; records partial repair of empirical reproducibility; leaves all mathematical and empirical claim statuses unchanged |

Version 2.2 is the final master for the 31 July 2026 baseline. Version 2.1 remains the immutable
28 July audit snapshot in `archive/earlier_documents/`. The exact status of
the six nonlocal dependency categories is stated in D.6. The later repository
and execution audit partially repairs the empirical-reproduction category,
but it does not supply every omitted full raw campaign or close any of the
five mathematical dependency categories.

### D.9 Post-Version-2.1 repository and execution audit — 31 July 2026

This bounded audit was performed after the source archives were decompressed and organized by scientific program. Its purpose was to determine what is now executable and retained, not to rerun every expensive frozen campaign. The common environment used Python 3.12.13, NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8 on macOS ARM64.

#### D.9.1 Integrity and source-level execution

| Program | Check performed | Result and scope |
|---|---|---|
| Immutable releases | Verified `archive/SHA256SUMS.txt` | All eleven ZIP bundles match their recorded SHA-256 values. This proves byte integrity of the retained packages, not correctness of their scientific conclusions. |
| Core operator PDE | Ran the active source tests in `studies/operator_pde/core/tests/` | 12/12 passed, covering the scaled dense gradient, tangent-kernel identity, absence of a dense weight state, shared transpose, cubature moments, restartable positive-time state, PSD/output identity, and zero-residual freeze. |
| Independent operator audit | Ran `studies/operator_pde/core/audits/numerics/test_operator_hermite_pde.py` | 4/4 passed: weighted parameter gradients, shared-operator adjoint identity, tangent-kernel/output identity, and numerical restart semigroup. |
| Dense response | Ran `studies/dense_response/long_horizon/tests/` | 8/8 passed. The retained long-horizon phase also includes its declared raw NPZ traces and processed summaries. These tests concern the finite-matrix response hierarchy, not the width-independent PDE. |
| Proof-obligation framework | Ran `studies/pde_convergence/01_proof_audit/tests/` | 128/128 passed. As its report emphasizes, these are implementation and protocol checks; only two frozen scientific trajectories exist for that phase. |
| Generalization | Verified the frozen source digest and ran its source suite | The aggregate source digest passes as `421ae71793d558822da3ff8b16a40c4189fb118d30025cc9f08ca7d666a0fcab`. Four `m=2,3,4,5` subcases of one strict determinism test differ in one array entry by at most \(2.22044605\times10^{-16}\) when bootstrap batches are regrouped. The assertion requires exact array equality, so the current platform run is recorded as four test failures rather than relabeled a pass. No scientific metric or frozen processed result changes. |
| Activation controls | Verified `SHA256SUMS.txt` and ran the source suite | Every retained report, source, protocol, seal, processed-evidence, figure, and parent-release hash passes. Fourteen of fifteen source tests pass; the remaining strict scalar equality computes \(0.510118559971626\) instead of the frozen \(0.5101185599716273\), a difference of about \(1.3\times10^{-15}\). The frozen source is not modified to hide this platform-level distinction. |

The two exact-equality outcomes above are reproducibility facts, not evidence against the reported dynamics. They are also not silently converted to tolerance-based passes because doing so would alter hash-bound frozen source. A future maintained, nonfrozen compatibility harness may test numerical agreement with an explicit tolerance while leaving the archived protocols untouched.

#### D.9.2 Fresh central-PDE execution

The frozen core runner was executed without changing its scientific source; only the output root was redirected to `studies/operator_pde/rerun_2026-07-31/`. The primary run used

$$
P=5,\qquad N=16,\qquad M=256,\qquad R=128,\qquad
\Delta t=0.02,qquad 0\le t\le8,
$$

followed by an authenticated autonomous continuation with step \(0.1\) from \(t=8\) to \(t=32\). The principal comparisons are:

| Diagnostic | Fresh macOS ARM64 run | Archived processed value |
|---|---:|---:|
| Minimum projected hidden energy on \([0,8]\) | \(0.9999680532937116\) | \(0.9999680532937119\) |
| Maximum output drift on \([8,32]\) | \(4.998598884877478\times10^{-13}\) | \(4.996256488546761\times10^{-13}\) |
| Maximum all-depth Gram drift on \([8,32]\) | \(4.236957410629663\times10^{-13}\) | \(4.236439840938928\times10^{-13}\) |
| Maximum residual on \([8,32]\) | \(4.998598884877478\times10^{-13}\) | \(4.996256488546761\times10^{-13}\) |
| Maximum \(|\dot{\mathcal L}|\) on \([8,32]\) | \(8.260989159352565\times10^{-25}\) | \(8.253299521758154\times10^{-25}\) |

The fresh loss at \(t=8\) was \(1.249299540594919\times10^{-25}\), and the minimum tangent-kernel eigenvalue on \([0,8]\) was \(2.620888958800208\). The active integration and continuation took 121.9 and 77.1 seconds respectively.

The archived snapshot was produced on Linux x86-64. Equal quadrature weights hash identically, but the empirically whitened Sobol arrays and hence the aggregate compiler hash differ bytewise across the two platforms. The agreement above is therefore a numerical reproduction to floating-point precision, not a byte-for-byte reconstruction of the original raw archive.

A separate cheap smoke run used \(P=5,N=8,M=64,R=32\) and a 16-member \(n=64,L=16\) dense block through \(t=2\). It obtained a normalized output-curve gap of \(1.0526\%\), a Gram-increment gap of \(3.3593\%\), monotone PDE loss, and a successful authenticated continuation to \(t=3\). Because the dense block and PDE resolution are small, these values are execution diagnostics only and are not added to the Chapter 7 evidence ledger.

#### D.9.3 Reproduction disposition

The post-Version-2.1 evidence supports four carefully separated statements.

1.  The immutable release packages and retained activation evidence are byte-verified.
2.  The central PDE, dense-response, and proof-obligation implementations execute in the current repository, subject to the exact platform-sensitive equality outcomes stated above.
3.  The central \(P=5\) PDE and its autonomous plateau have been numerically reproduced on a different hardware/software platform.
4.  The full canonical dense ensemble, all PDE refinements, the complete fourteen-case raw campaign, and the complete activation raw campaign have not been independently regenerated in this audit.

Accordingly, the former statement that code and configurations awaited later supply is closed for most numerical programs. The stronger statement that the complete empirical corpus has been independently regenerated remains false. This partial repair changes no Chapter 9 claim ID, no theorem status, no empirical percentage, and no supersession relation.
