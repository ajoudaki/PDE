# Finite Causal PDE Closure of Dense $\mu$P Feature-Learning Dynamics

## Master research monograph

**Project state:** 27 July 2026  
**Audit state:** Chapters 1–9, the front matter, and the appendices passed their fragment-level independent audits, and the assembled master passed the post-merge whole-document audit after repair; see Appendix D.  
**Central model class:** fully dense, fully trained, genuinely nonlinear Euclidean-$\mu$P networks  
**Canonical positive laboratory:** residual network, width first and residual depth second  
**Canonical negative laboratory:** two-hidden-layer quadratic network with an unbounded Gaussian readout  
**Primary observables:** outputs, loss, and depth-indexed hidden Gram matrices

## Executive synopsis

The project asks whether the deterministic limits furnished by modern infinite-width theories can be compressed further into a finite causal macroscopic state.

The broad thesis is:

> In a standard deep, dense, fully trained, nonlinear $\mu$P feature-learning regime, the ordered wide/deep training dynamics of outputs and representations admit an architecture-derived, autonomous PDE description with finitely many field species over a fixed finite-dimensional source space, to arbitrary prescribed accuracy, without retaining microscopic matrices or a training-history object whose dimension grows with the time horizon. The compiled PDE is internally restartable from its declared state. The stronger restart-robust form also supplies a correspondence from physically consistent positive-time dense states to PDE states and controls the future continuation error.

This is stronger than the existence of deterministic trajectories. Tensor Programs already derive infinite-width feature-learning limits under $\mu$P, and dynamical mean-field theory represents feature learning through self-consistent stochastic processes, two-time correlation kernels, causal response kernels, and memory. The first additional theorem sought here is an architecture-compiled autonomous approximation from canonical compiled initial states, with complexity independent of width and original depth. A still stronger theorem would prove that its current macroscopic state is also a sufficient restart state for the dense limit. Under the strongest formulation, the state type and complexity are independent of the training horizon.

The project has not proved those theorems. It has, however, documented four substantive findings.

1.  **A literal finite-cutoff PDE exists.** For the canonical residual architecture, the operator–Hermite Liouville construction is autonomous, width-independent, and uses the same projected operator in the forward and transpose directions. At every finite cutoff, wherever the flow is well posed, its projected-gradient identity, positive-semidefinite tangent kernel, direct moment readouts, and loss dissipation are exact internal theorems.
2.  **The smallest nonlinear PDE is an accurate nonlazy surrogate on the tested family.** In the canonical benchmark it reproduces $O(1)$ hidden-Gram motion with a normalized Gram-increment discrepancy of about $1.14\%$, although the remaining gap is statistically resolved. Across fourteen transfer configurations, the reported median/max normalized errors were $1.71\%/4.14\%$ for Gram increments, $1.46\%/1.83\%$ for outputs, and $0.63\%/1.97\%$ for loss.
3.  **Several mundane explanations have been defeated in the tested controls.** The observed agreement is not frozen-feature behavior, exact identity/deep-linear dynamics, or a scalar reparametrization of training time. A nonlinear sine stress also defeats the tested fixed-gain linear explanation for Gram dynamics: paired dense linear and dense sine trajectories differ by $15.95\%$, while the nonlinear PDE differs from dense sine by about $2.50\%$ in Gram and $2.81\%$ in output. Adaptive or state-dependent linear surrogates remain outside that test, and the joint three-observable $5\%$ gate is not passed because the reported sine loss discrepancy is $5.54\%$.
4.  **The arbitrary-accuracy bridge remains open.** The parity-correct Hermite hierarchy has not shown replicated aggregate Cauchy contraction. Its infinite operator flow has not been identified with the ordered dense limit. Cutoff-uniform stability, trained-depth homogenization, the surviving conditional/Onsager mean, and the all-time tail are unproved.

The quadratic laboratory gives a complementary negative result. For the prescribed initial Wick–Taylor compiler, the limiting coefficients have a factorial lower bound and zero radius of convergence; the associated physical-time predictions form an initial boundary layer and fail uniformly. The global residual-clock stability theorem survives, but its required approximation defect is not small for this compiler. A stronger claimed instantaneous-fitting theorem is valid only conditional on the stated tagged-site DMFT representation and its response-kernel hypotheses; those hypotheses are not derived in the supplied project proof and must not be reported as an unconditional theorem about the finite network.

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

[Tensor Programs IV](https://arxiv.org/abs/2011.14522) proves that suitable infinite-width limits can exhibit feature learning and gives a rigorous procedure for computing the discrete-time $\mu$P limit at fixed finite program/training length as width tends to infinity. Its central mechanism is to express the complete finite training computation as a tensor program and apply a master theorem to the coordinate distributions of every vector generated by that program. Consequently, TP already addresses:

- nonlazy infinite-width feature learning;
- ordinary deep dense matrix reuse, including correlations between a matrix and its transpose;
- deterministic limits of outputs and coordinate statistics at each fixed program length;
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

TP IV is naturally a **computation-unrolling** description. Each additional gradient step appends new program variables and new covariance relations. The paper itself notes that at $t$ steps, new Gaussian variables must be introduced and their covariances with previous variables stored, giving $\Omega(t^2)$ covariance bookkeeping; it further notes that exact evaluation of the resulting nonlinear Gaussian expectations can itself be exponential or super-exponential in $t$ for the classes discussed there. These are complexity statements about the displayed exact procedure, not a theorem that the TP limit can never be compressed or that every implementation has those costs. They identify the native exact representation that the present project seeks to reorganize.

[Tensor Programs VI](https://arxiv.org/abs/2310.02244) further shows that TP can analyze width-then-depth limits and classify depth scalings for residual networks. This makes the comparison sharper, not weaker: taking width first and depth second is not itself beyond TP. However, TP VI studies a related Depth-$\mu$P program, principally with $L^{-1/2}$ residual scaling and its associated depthwise parameterization. It does not establish the present $L^{-1}$-residual, hidden-rate-$L$, fully trained, all-time finite-Markovian PDE theorem.

The additional theorem sought here is:

> The growing TP computation admits, on the declared standard model class, an architecture-derived finite current-state realization whose approximation error can be made arbitrarily small, with a state type independent of the elapsed training horizon.

That is a realization/compression theorem **about** the TP-described limit. It is not a competing derivation of the same fixed-horizon limit, and it is not an impossibility claim about the TP formalism.

**External-source basis.** Yang and Hu, *Feature Learning in Infinite-Width Neural Networks*, especially the Introduction and §§7–8, including §8’s discussion of exact-training computational cost; Yang, Yu, Zhu, and Hayou, *Tensor Programs VI: Feature Learning in Infinite-Depth Neural Networks*, Abstract and §§1, 3.3.

**Project provenance.** `positioning_roadmap_dmft_tp.tex`, “Target II: low-order long-horizon closure” and “Position relative to TP/DMFT”; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§1, 13, and 16.

### 1.3 What DMFT already provides

[Bordelon and Pehlevan’s self-consistent DMFT](https://arxiv.org/abs/2205.09653) formally derives an infinite-width feature-learning description in terms of deterministic two-training-time kernels and self-consistent stochastic fields. For each hidden layer it tracks feature and gradient kernels such as

$$
\Phi^\ell_{\mu\nu}(t,\tau),
\qquad
G^\ell_{\mu\nu}(t,\tau),
$$

together with response objects $A^\ell_{\mu\nu}(t,\tau)$ and $B^\ell_{\mu\nu}(t,\tau)$. These determine Gaussian effective fields and causal Volterra equations whose time integrals run over the history $0\le \tau\le t$. At the corresponding feature-learning strength, their DMFT recovers the stochastic process obtained from TP.

DMFT therefore already supplies:

- a deterministic macroscopic description of rich feature learning;
- hidden-feature and gradient laws, not merely loss;
- two-time covariance kernels;
- reciprocal functional-response terms generated by reused disorder;
- a self-consistent account of forward/backward coupling and the evolving tangent kernel.

The project should not describe DMFT as “infinite” merely because it uses integrals while calling the candidate PDE “finite” despite its own integrals. Both are continuum field theories. DMFT has finitely many **kernel species**, but each species is a function on a two-time domain. On a grid of $N_t$ training times, a two-time kernel has $O(N_t^2)$ entries; the cited DMFT paper explicitly represents the kernels as $PT\times PT$ matrices on a time grid and reports $O(P^2T^2)$ kernel memory in its notation.

The finite-PDE candidate also uses nontrivial integrals:

- integration over the immutable source law $\mu(d\theta)$;
- integration over a finite-dimensional row-coordinate law $\rho^\theta(dw)$;
- integration or evolution in the physical depth variable $s$.

The proposed advance is therefore not “integrals versus no integrals,” “finite species versus infinite species,” or even an unconditional claim of lower numerical cost. The distinction is the **training-time geometry of the state**:

| Property                               | Native TP description                                     | Native DMFT description                                   | Sought PDE theorem                                |
|----------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|---------------------------------------------------|
| Feature learning                       | Yes                                                       | Yes                                                       | Yes                                               |
| Deterministic macroscopic observables  | Yes                                                       | Yes                                                       | Yes                                               |
| Reused $W/W^\top$ correlations         | Program dependencies                                      | Response/Onsager kernels                                  | Reconstructed from current PDE state              |
| Training-time domain in the state      | Program grows with steps                                  | Two-time causal triangle grows with horizon               | One current-time slice on fixed source domains    |
| Restart at $t_*$                       | Native representation carries the relevant unrolled state | Native representation carries accumulated kernels/history | Same current-state equations determine the future |
| Approximation order                    | Not a finite-realization theorem by itself                | Not a finite-realization theorem by itself                | Explicit architecture-local hierarchy             |
| Horizon-independent arbitrary accuracy | Not implied                                               | Not implied                                               | Required in the strongest conjecture              |

An exact DMFT may be the most natural starting point for proving the conjecture. One possible route is to prove that its causal kernels admit a stable finite realization—through finitely many response modes, rational memory approximants, or another architecture-derived state. If that route succeeds, the PDE theorem would be a compression theorem **derived from DMFT**, not a repudiation of it.

**Status.** The cited DMFT gives a self-consistent feature-learning field theory for its stated wide-network setting, with the numbers of training steps and samples held $O_N(1)$, meaning fixed in the width $N\to\infty$ limit, and explicitly exhibits the two-time/response structure. Its path-integral saddle calculation is presented as a formal physics derivation rather than a rigorous convergence theorem. The exact fixed-$L$ causal DMFT and trained $L\to\infty$ homogenization for the project’s canonical $L^{-1}$ residual model remain open.

**External-source basis.** Bordelon and Pehlevan, *Self-Consistent Dynamical Field Theory of Kernel Evolution in Wide Neural Networks*, Abstract and §§2–4, especially the two-time order parameters, stochastic Volterra equations, response functions, and computational table.

**Project provenance.** `dense_euclidean_continuous_depth_npde_audit.md`, §§3.2, 4.2–4.4; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§13–16; `positioning_roadmap_dmft_tp.tex`, “Target II.”

### 1.4 Why dense training naturally produces history

The obstruction is already visible before taking any limit. Here $h_q^\ell$ is the hidden feature of sample $q$ at layer $\ell$, $e_q=f_q-y_q$ is its residual, $p_q^{\ell+1}$ is the unit-output adjoint, $D_q^\ell=\operatorname{diag}\phi'(W_\ell h_q^\ell)$, and $\beta_q^\ell=D_q^\ell p_q^{\ell+1}$. For each residual block,

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
h_r^\ell+\frac{\gamma}{L}\phi(W_\ell h_r^\ell),
\qquad
f_r=\frac1n a^\top h_r^L,
$$

with every parameter trained by

$$
\eta_B=n,\qquad
\eta_a=n,\qquad
\eta_{W_\ell}=L.
$$

The principal positive program uses bounded smooth nonlinearities such as $\tanh$. Boundedness is a restriction of the current construction and analytic program, not the philosophical content of “real nonlinearity.” The separate quadratic branch is retained because it is a sharp theorem laboratory, but its one-sample setting, unbounded activation, unbounded Gaussian readout, and absence of the residual $L\to\infty$ limit make its conclusions model-specific.

Nonlazy behavior must be checked through representation motion, for example by requiring on at least one nondegenerate target in $\mathcal U$ that

$$
\sup_{t\le T}\sup_{s\in[0,1]}
\|G^h(s,t)-G^h(s,0)\|_F
$$

remain bounded below by a positive constant in the ordered limit. Merely assigning $\mu$P learning-rate exponents does not prove that a chosen task actually exhibits feature motion.

The one-hidden-layer case is excluded from the central claim because its parameter distribution is already a natural current transport state. The project asks whether an analogous finite causal state survives the repeated dense $W/W^\top$ reuse of genuine depth.

**Project provenance.** `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`, §§1–3; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§2–3 and §11.4; `dense_euclidean_continuous_depth_npde_audit.md`, §§2–3.

### 2.2 The canonical target and approximation topology

Fix a compact, computably represented parameter class $\mathcal U$. A concrete first laboratory is a neighborhood of

$$
m=d=3,\qquad
X=I_3,\qquad
y=(0.8,-0.55,0.35),
\qquad
\sigma_w=0.65,\quad A=\gamma=1.
$$

The compact class is not claimed to be maximally general. Its role is to prevent a closure from memorizing a single target trajectory and to make all constants and quantifiers explicit.

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

An approximation family $\{\mathsf P_k\}$ is admissible only if all of the following hold.

1.  **Finite source and field lists.** At each $k$, the compiler emits finitely many fields on declared finite-dimensional domains. A conditional probability law is allowed, but no field may carry an undeclared infinite coefficient sequence.
2.  **Architecture-local provenance.** Initialization, drift, boundary equations, and readouts are computed from the architecture, activation, Gaussian initialization law, current PDE moments, and static parameters.
3.  **No microscopic state.** There is no $n\times n$ matrix, width-indexed vector, finite-network checkpoint, or source dimension that grows with $n$.
4.  **No trajectory oracle.** Positive-time dense outputs, Grams, kernels, hitting times, fitted constants, and trajectory-trained bases are forbidden.
5.  **Predeclared approximation order.** The basis and hierarchy schedule are fixed before positive-time target data are observed.
6.  **Autonomy.** The current state determines the future under the same equations.
7.  **Internal restartability.** Restarting from an admissible reached PDE state does not require the past trajectory, an absolute-time playback clock, or recomputed target data. This clause does not, by itself, provide a state map from arbitrary dense-limit restarts.
8.  **Direct readouts.** Outputs and hidden Grams are current moments or declared local functionals of the state, not separately fitted decoders.
9.  **Correct limit semantics.** Projection is applied to the limiting operator/law representation after the width limit; it is not a low-rank replacement of the finite dense matrix.
10. **Uniformity over $\mathcal U$.** One family works over the declared model class. Coefficients may depend on the current $\vartheta$, but the grammar and ordering do not change after observing its trajectory.
11. **Finite description and no unbounded encoding.** At each fixed $k$, every emitted coefficient, source law, and operation belongs to a predeclared computable regular class with a finite description. No real coordinate or coefficient may encode an unbounded bit string, target trajectory, or training history. This requirement does not demand a computable accuracy-to-cutoff map, which is the separate stronger “effective closure” rung.

These clauses exclude several formally finite but scientifically vacuous constructions. For any continuous scalar curve, one can use a compactifying clock, approximate the curve by a Bernstein polynomial, and pack the result into a two-state ODE or one-source PDE. One can also encode an arbitrary finite ODE in the finite jet of a single scalar source field. Therefore:

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

Equation (2.3) allows success at one exact cutoff or along a favorable subsequence. Equation (2.4) requires every sufficiently high complete cutoff to work. Neither follows from the observed accuracy of $r=1$.

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

**Broad-existence falsifier.** The logical negation must quantify over the whole admissible class:

$$
\text{for every predeclared admissible family }\{\mathsf P_k\},
\qquad
\inf_kE_k(\infty)>0.
$$

A single positive constant valid uniformly over all admissible families would be a stronger sufficient lower bound. Noncompactness of an ambient memory operator or a nondecaying continuum is not enough by itself, because the physically reachable set or the declared observables may still be compressible. Such a mechanism refutes the broad thesis only if it yields the required observable lower bound—for example through an appropriate lower bound on the relevant reachable-state approximation widths.

**Proof-route falsifier.** Zero radius of a training-time Taylor series, failure of one moment hierarchy, lack of a plain $L^2$ Lipschitz estimate, or failure of one basis defeats only that route unless it establishes a lower bound over the whole admissible class.

The project already contains examples of the last distinction. The raw quadratic Wick-Taylor compiler has been disproved, while the broader real-axis closure question was not settled by that result. Likewise, the earlier claim that the $K/J/N$ prose compiler was already executable is superseded; its exact chronological identities and factorial propagator bound survive.

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
| Training-time Wick-Taylor truncation solves the quadratic closure problem        | **Falsified for that stated compiler and model**                                 |

This ledger is the baseline against which every later chapter should be read.

## Chapter 3 — Exact causal skeleton and the distinct approximation axes

### 3.1 Canonical finite network and notation

Fix $m$ samples $x_1,\ldots,x_m\in\mathbb R^d$, labels $y_1,\ldots,y_m$, width $n$, residual depth $L$, and a smooth activation $\phi$, acting componentwise on vectors. Let

$$
h_r^0=Bx_r,
\qquad
z_r^\ell=W_\ell h_r^\ell,
$$

$$
h_r^{\ell+1}
=
h_r^\ell+\frac{\gamma}{L}\phi(z_r^\ell),
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
\operatorname{diag}\phi'(z_r^\ell),
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

Ordered-product expansion and the volume of the depth simplex give

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

The factorial in (3.28) is geometric: it is the volume of an ordered simplex in residual depth. It is valid for noncommuting and nonnormal matrices because the proof uses ordered products and operator norms, not eigenvalue diagonalization.

These estimates are pathwise at fixed finite $n,L$ whenever the displayed envelopes are finite. They are uniform in width and depth on $[0,T]$ only under the additional hypothesis

$$
\sup_{n,L}\max\{B_{v,T},B_{w,T},\Lambda_T\}<\infty.
$$

An all-time factorial estimate would require corresponding bounds uniform in $T$.

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

Hermite coefficients differentiate with respect to immutable Gaussian source variables. Taylor jets differentiate along the training vector field. The quadratic zero-radius theorem for a training-time Wick-Taylor series does not imply divergence of a source-Hermite Galerkin family.

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

Let $\eta$ denote a source-column neuron label and $\theta$ an independent target-row label of the same immutable Gaussian type as in §2.3; let $\omega$ carry the frozen Gaussian row randomness. Set

$$
\mathcal R=L^2(\mu_\theta\otimes\mathbb P_\omega),
\qquad
\mathcal R(H)
=
L^2(\mu_\theta\otimes\mathbb P_\omega;H).
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
(Iu)(\theta,\omega)=W_\omega(u).
$$

Its Hilbert adjoint $T_W=I^\ast:\mathcal R\to H$ is defined by

$$
\langle T_W\beta,u\rangle_H
=
\mathbb E_{\theta,\omega}[\beta W_\omega(u)],
$$

and is bounded:

$$
\|T_W\beta\|_H\le\|\beta\|_{\mathcal R}.
$$

In a Hermite basis $\{\phi_\nu\}$ of $H$, put

$$
\epsilon_\nu(\omega)=W_\omega(\phi_\nu).
$$

Then

$$
T_W\beta
=
\sum_\nu
\phi_\nu\,
\mathbb E_{\theta,\omega}[\epsilon_\nu\beta].
$$

However, $T_W$ is not compact. Taking $\beta_\nu=\epsilon_\nu$ gives

$$
T_W\beta_\nu=\phi_\nu,
$$

so for every finite projection $\Pi_{r_{\mathrm H}}$,

$$
\sup_{\|\beta\|_{\mathcal R}\le1}
\|(\mathrm{Id}_H-\Pi_{r_{\mathrm H}})T_W\beta\|_H=1.
\tag{3.30}
$$

Strong projection convergence is uniform on compact sets, not on the energy-bounded unit ball.

The learned-row adjoint $T_c\beta=\mathbb E_{\theta,\omega}[c\,\beta]$ is bounded when $c\in\mathcal R(H)$, but it must be controlled together with the frozen term. Boundedness of either component does not supply the collective source compactness needed for cutoff convergence.

Plain $L^2$ is also insufficient for the nonlinear adjoint map

$$
(z,p)\mapsto\phi'(z)p.
$$

Indeed,

$$
\delta\beta
=
\phi'(z)\delta p
+
\widetilde p\,
\bigl[\phi'(z)-\phi'(\widetilde z)\bigr],
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
| Exact result in the audited five-report corpus | None: the supplied foundational reports do not contain a standalone proof of the generic shallow mean-field theorem    |
| Modified qualifier                             | Genuine depth, specifically the presence of at least two trained hidden layers                                         |
| Why it is not central                          | The hidden-to-hidden dense transpose/reuse mechanism is absent                                                         |
| Transfer back                                  | Empirical-measure transport, direct moment readouts, and gradient-flow dissipation are the right structural precedents |

The schematic equation above is contextual mathematical background, not a new theorem claimed by the present project. Its hypotheses must be supplied by whichever shallow mean-field theorem is cited in the final bibliography.

### 4.3 Smooth or depth-coherent matrix processes

#### 4.3.1 Smooth depth is a different model

Suppose a depth-indexed matrix path $W(s)$ is postulated with enough regularity that a residual recursion is a consistent discretization of

$$
\partial_s h(s)=\mathcal F\bigl(h(s),W(s)\bigr).
$$

Then continuous-depth analysis may legitimately treat $W(s)$ as a coefficient field and derive a neural-ODE or PDE limit. This assumption is not satisfied merely because the number of iid layers tends to infinity. Raw iid matrices do not become a smooth nondegenerate path under interpolation: adjacent layers remain independent innovations rather than $O(L^{-1})$ increments of one matrix-valued curve.

The canonical dense project therefore takes width first and depth second and seeks homogenization of observables and conditional response laws. It does not interpolate the microscopic matrices themselves.

| Field                    | Classification                                                                                                                                                    |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exact project conclusion | A smooth interpolation of raw iid depth matrices is not the canonical ordered target                                                                              |
| Modified qualifier       | Iid, untied depth is replaced by a smooth, tied, or coherently correlated depth process                                                                           |
| Why it is not central    | The difficult trained-depth homogenization and surviving conditional/Onsager mean have been assumed away or changed                                               |
| Transfer back            | Continuous-depth adjoints, depth transport, and homogenization templates remain useful after the iid innovations and conditional mean have been derived correctly |

*Provenance:* `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §2.1 “Ordered target,” §11.1 “Established,” and §16.2 “Prelimit-first causal Galerkin”; same sections in `MASTER_NEURAL_PDE_REPORT_WITH_FIGURES.md`. The detailed causal derivation belongs to the residual-network chapters; it is not reproved in the five quadratic reports.

### 4.4 Normalized and projected geometries

#### 4.4.1 Why normalization is a boundary regime

RMS normalization and direction-only weight normalization change either the architecture map, the parameter-space metric, or both. They are therefore not positive answers for the unnormalized Euclidean model. They are nevertheless important because they test whether the quadratic obstruction is merely radial and whether normalization creates an exact finite moment algebra.

For the two-hidden-layer, one-sample quadratic laboratory, the audited result is:

| Field                                          | RMS after both hidden activations                    | Direction-only weight normalization                                                                                       |
|------------------------------------------------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Exact low-order result                         | The feature-time cubic coefficient changes sign      | Global readout projection changes the cubic coefficient but not the initial kernel                                        |
| Exact natural moment closure                   | No                                                   | No                                                                                                                        |
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
| Transfer back         | The fixed-order derivative/Wick compiler, projector calculus, Bell-partition bookkeeping, and the warning that natural moment nonclosure survives normalization |

*Provenance:* `normalized_mean_field_taylor_closure_audit(1).md`, §§3–7, especially §6 “What the Taylor graphs say about closure” and §7 “Precise PDE classification”; synthesis cross-check in `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§11.4 and 12, and the corresponding sections of `MASTER_NEURAL_PDE_REPORT_WITH_FIGURES.md`.

### 4.5 Frozen, tied, low-rank, and symmetric reductions

#### 4.5.1 Frozen first hidden layer

Two different uses of “frozen first layer” must be separated.

First, freezing the first hidden variables does **not** by itself make the full finite-width upper-neuron dynamics equal to a scalar cooperative system. The full composite equation still contains

$$
z'=q(a\odot z)+2K(a\odot z).
$$

What is exact for the raw zero-radius proof is a selected derivative history: at every differentiation one keeps the $q(a\odot z)$ term and never differentiates $q$. For a tagged upper-neuron polynomial this selected word is generated by

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

Second, there is a genuine frozen-first-layer mean-field reduction used to audit Gaussian cutoff arguments. After the source rescaling in Q3, one particle obeys

$$
u'=qv^2,\qquad v'=quv,
$$

and contributes $quv^2$ to the readout. For the centered Gaussian law conditioned to $[-R,R]^2$, comparison from the positive corner with the invariant ray $u=v$ forces every fixed subtarget $y<1$ to be reached before feature time $1/(qR)$. The residual-clock physical hitting time satisfies

$$
t_R(y)\le \frac{1}{2qR(1-y)}\longrightarrow0.
$$

Thus the cutoff losses equal one at the origin but tend to zero at every fixed positive time; they are not uniformly Cauchy on any interval containing zero.

The latter is a theorem only for this frozen mean-field reduction. It cannot be promoted to the full model because the additional matrix message $K(a\odot z)$ is not componentwise positive.

| Field                 | Classification                                                                                                                                                                           |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exact result          | Selected cooperative derivative word (4.1)–(4.2); dynamic singularity of naive Gaussian cutoff in the stated frozen mean-field reduction                                                 |
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

This chapter studies one input, two trainable hidden layers, quadratic activation, a scalar output, and label-one squared loss. It retains a fully trained dense middle matrix and the stated $\mu$P metric, but it is not the canonical residual architecture: it has only one sample, an unbounded activation, an unbounded trainable Gaussian readout, and no $L\to\infty$ residual-depth limit.

For one sample, the trainable variables $x_i$ below are the first-layer preactivations on that sample. This reduction is exact for the chosen observable, but it suppresses the cross-sample geometry of a trainable input matrix. Nothing in this chapter by itself proves the corresponding multi-sample statement.

Four mathematical objects must be distinguished:

1.  the exact finite-width polynomial ODE;
2.  the deterministic coefficient obtained by taking $n\to\infty$ at each *fixed* derivative order;
3.  a classical positive-time infinite-width mean-field flow, whose construction is not supplied by the foundational reports;
4.  the natural relaxed loss selected from an asserted tagged-site DMFT.

Confusing (2), (3), and (4) caused several earlier overclaims. The zero-radius theorem concerns (2). The residual-clock theorem is an exact stability implication for any regular profile of type (1) or (3). The step-loss theorem concerns (4) and is conditional on the asserted causal DMFT representation and selection.

The source abbreviations used below are:

| Key | Exact filename                                                 |
|-----|----------------------------------------------------------------|
| Q1  | `approximate_single_source_conjecture_resolution(1).md`        |
| Q2  | `approximate_single_source_stability(1).md`                    |
| Q3  | `adversarial_audit_report(1).md`                               |
| Q4  | `mean_field_single_source_conjecture_audited_resolution(2).md` |
| Q5  | `normalized_mean_field_taylor_closure_audit(1).md`             |
| M15 | `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`                    |
| M16 | `MASTER_NEURAL_PDE_REPORT_WITH_FIGURES.md`                     |

The latest master reports identify Q1–Q5 as the “foundational negative and stability reports” and preserve only their fixed-order calculus, residual-clock stability, anti-oracle discipline, and model-specific no-go results.  
*Provenance:* M15 and M16, §20 “Supersession and source map,” subsection “Foundational negative and stability reports.”

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

This theorem is complete under its displayed hypotheses. It proves *propagation control*, not *production of a small defect*. In particular it cannot be applied to the Wick–Taylor profiles below with $\varepsilon\to0$, because those profiles diverge.

*Provenance:* Q2, §6 “Global clock-shadowing theorem”; corrected scope in Q1, §8 “What remains true: the observable stability theorem”; audit in Q3, §5 “Audit of the positive identities.”

#### 5.4.1 Direct input-to-state stability in the loss channel

There is a complementary formulation that does not assume a common feature profile. Suppose, after a positive-entry time,

$$
\dot{\mathcal L}=-4\kappa\mathcal L,
\qquad
\dot{\widehat{\mathcal L}}
=-4\widehat\kappa\widehat{\mathcal L}+\eta,
$$

and assume

$$
\kappa,\widehat\kappa\ge\lambda>0,\qquad
|\widehat\kappa-\kappa|\le\delta,\qquad
|\eta|\le\rho.
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

then $\eta=0$. A small local hidden-state residual is not enough unless it yields the displayed kernel or loss-channel bounds.

*Provenance:* Q2, §7 “Direct input-to-state stability for an arbitrary finite PDE.”

### 5.5 Fixed-order Wick calculus and the proposed one-source Taylor closure

For every fixed $k$, define the limiting coefficient

$$
c_k
:=
\lim_{n\to\infty}
\frac{D_{+,n}^kf_n(0)}{k!},
\tag{5.27}
$$

when the fixed-order mean-field limit is taken. The project’s derivative/Wick calculus expands $D_{+,n}^kf_n$ into finitely many polynomial histories, applies Gaussian contractions, and proves a deterministic leading value at each fixed order. At increasing fixed order, the emitted objects include ordered $W/W^\top$ reuse words, product-rule trees, activation derivatives, learned rank-one insertions, population contractions, and Wick pairings. “Finite at every fixed order” does not mean that the union over all orders is a finite closed algebra.

The five foundational reports do not reproduce the full concentration theorem. Accordingly, the theorem below has one explicit dependency: existence of the fixed-order limits (5.27), as supplied by the earlier Wick calculus. Its factorial lower bound is proved directly in Q1.

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

*Provenance:* Q1, §2 “The precise conjecture being resolved”; Q2, §§5 and 8. The claim in Q2, §9 that a uniform Taylor-tail estimate was the only remaining lemma is superseded by Q1.

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

Conditionally on the first hidden layer,

$$
A\sim N(0,1),\qquad
Z\sim N(0,\gamma q_0)
$$

are independent in the fixed-order limit.

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

Combining (5.33), (5.34), (5.38), and the no-cancellation comparison proves:

> **Theorem 5.1 (zero radius of the limiting Wick–Taylor series).**  
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

*Provenance:* Q1, §§3–5. Q3, “Established zero-radius input” and §4.2, independently audits the scope.

### 5.7 Consequences and scoped no-go theorems

#### 5.7.1 Failure of the one-source Wick–Taylor PDE

The order here is prescribed and iterated: for each fixed coefficient order $k$, first take $n\to\infty$ to obtain $c_k$; form the resulting degree-$M$ profile; only then send $M\to\infty$. No conclusion is asserted for a coupled diagonal $M=M(n)$, or for a fixed-$n$ Taylor germ inside its own random radius.

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

The continuous functions $\mathcal L_M$ approach a discontinuous step pointwise and are not uniformly Cauchy on any interval containing $0$. This disproves the prescribed Wick–Taylor closure independently of whether a regular positive-time full mean-field loss exists.

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

Finally, an exact realization $Y'=F(Y)$, $H'=K(Y)$ with $F,K$ analytic near the Gaussian initial state in one Banach space would give a positive Taylor radius by the analytic ODE theorem, contradicting (5.40). A viable theory must therefore use an unbounded generator, a scale of spaces with loss of regularity, a renormalized/signed construction, or a genuinely nonanalytic real-axis formulation.

*Provenance:* Q3, §4.2 “Ordinary Gaussian L2 is not a valid closure topology.”

#### 5.7.3 Positive-semigroup obstruction

Let $\mathcal A_+$ be the cone of primitive polynomials with nonnegative coefficients, $D$ the readout-ascent derivation, and $\Lambda$ Gaussian Wick expectation. Suppose a positive strongly continuous semigroup $S(\tau)$:

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

Let $E_h$ be pullback by one explicit Euler state update:

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

#### 5.7.5 Complete jets do not identify a real-axis trajectory

Once analyticity fails, even the infinite initialization jet does not determine a smooth positive-time function: adding a nonzero flat term such as $e^{-1/\tau^2}\mathbf 1_{\tau>0}$ changes the real-axis trajectory without changing any derivative at $0$. Padé or Borel resummation therefore selects a continuation unless a quasianalyticity, summability, or independent real-axis well-posedness theorem identifies it with the network.

This is a semantic non-identification theorem, not a proof that every resummation fails.

*Provenance:* Q3, end of §3 and §4.3.

#### 5.7.6 What remains open

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
\xi(t)
+\int_0^t r(s)M(t,s)a(s)z(s)\,ds,
\qquad
\dot a(t)=r(t)z(t)^2,
\tag{5.47}
$$

where:

1.  $r=1-f$;
2.  $\xi$ is a nondegenerate continuous Gaussian process;
3.  $a(0)\sim N(0,1)$ is independent of the entire cavity process $\xi$;
4.  $M$ is deterministic, causal, and continuous near $0$;
5.  the self-consistent output obeys $$
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

Continuity and nondegeneracy of $\xi$ give $z_*>0$, $\delta_0>0$, and

$$
p_\xi
:=
\Pr\!\left[\inf_{0\le t\le\delta_0}\xi(t)\ge z_*\right]>0.
$$

For every finite $A$, define

$$
p_A
:=
\Pr\!\left[
a(0)\ge A,\ 
\inf_{t\le\delta_0}\xi(t)\ge z_*
\right]
=
p_\xi\Pr[a(0)\ge A]
>0.
\tag{5.50}
$$

On this event, cooperative comparison gives

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

implies, with $\alpha=\sqrt{A^2-z_*^2/m}$,

$$
\dot b=cm(b^2-\alpha^2).
$$

Its blow-up time is

$$
T_A
=
\frac1{2cm\alpha}
\log\!\left(\frac{A+\alpha}{A-\alpha}\right)
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

The negative cubic coefficient is a genuine sign reversal relative to the raw network. Substitution into (5.57) yields the physical-time Taylor coefficients

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

For a fixed-radius middle row,

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

#### 5.9.4 Exact failure of finite natural moment cutoffs

The normalized models do not make the displayed monomial hierarchy invariant at any finite degree cutoff; this failure is visible already in exact frozen top-block reductions.

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

Both recurrences generate moments outside every finite rectangular degree cutoff. They prove failure of the *natural polynomial-moment cutoff closure*. They do not prove that no nonlinear sufficient statistic, algebraic relation among reachable moments, or accuracy-dependent real-axis approximation exists.

*Provenance:* Q5, §5 “Independent reduction checks” and §6 “What the Taylor graphs say about closure.”

#### 5.9.5 What normalization does and does not resolve

RMS differentiation creates reciprocal-moment vertices, projector derivatives, Bell partitions, and disconnected contractions. Direction-WN creates projector words; the readout adds $-fa/C$. These signed terms invalidate the raw coefficientwise-positive lower bound.

Accordingly:

- zero radius is **not proved** for RMSNorm;
- zero radius is **not proved** for global readout direction-WN;
- if only large-fan-in hidden rows are normalized and the readout is not projected, every fixed-order limiting coefficient agrees with the raw hierarchy, so the raw zero-radius result transfers under that convention;
- no finite truncation of the natural moment/message hierarchy is invariant;
- every non-Taylor finite PDE remains unruled-out.

*Provenance:* Q5, §§6.3 and 7.

### 5.10 Authoritative theorem and non-theorem ledger

| Claim                                                                                   | Status                                                              | Exact scope                                                                               |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Finite-width gradients, composite equation (5.9), kernel positivity, and residual clock | Proved                                                              | Exact polynomial ODE, while it exists                                                     |
| Positive-entry coercivity and finite feature-time budget                                | Proved under displayed trajectory hypotheses                        | Target-side finite-width trajectory; a uniform mean-field burn-in is not supplied         |
| Clock-shadowing bounds (5.24)–(5.26)                                                    | Proved                                                              | Any two monotone target-reaching profiles satisfying (5.22)                               |
| Fixed-order Wick coefficients                                                           | Established dependency from earlier calculus                        | Each order fixed before $n\to\infty$; full proof not reproduced in Q1–Q5                  |
| Factorial lower bound and zero radius                                                   | Proved relative to the fixed-order coefficient limits               | Raw quadratic, Gaussian initialization, unbounded readout                                 |
| Uniform convergence of the Taylor one-source PDE                                        | Falsified                                                           | Prescribed width-first, order-second Wick–Taylor family                                   |
| Coefficientwise-positive fixed-order-consistent polynomial compilers                    | Falsified                                                           | Positive polynomial/Wick cone; excludes signed or nonpolynomial methods                   |
| One analytic Banach-space realization                                                   | Impossible                                                          | Exact analytic $F,K$ near the Gaussian initial state                                      |
| Positive classical semigroup realization                                                | Impossible under four explicit positivity/domain/readout hypotheses | Does not cover mild/signed/renormalized constructions                                     |
| Naive Gaussian cutoff convergence                                                       | Falsified only in a frozen subsystem                                | Does not transfer componentwise through the full $K_nu$ message                           |
| Any non-oracular signed real-axis finite compiler                                       | Open                                                                | Requires explicit state, residual norm, and stability theorem                             |
| Tagged-site instantaneous fitting                                                       | Exact implication under the asserted DMFT representation            | Representation, finite-network identification, and relaxed selection remain unproved here |
| Natural relaxed step loss                                                               | Conditional selection                                               | Requires monotone, no-overshoot relaxation                                                |
| Finite natural moment/message cutoff after RMS/global WN                                | Falsified                                                           | The displayed natural hierarchy; no claim about every nonlinear sufficient statistic      |
| Zero radius after RMS/global readout WN                                                 | Open                                                                | Raw positivity proof no longer applies                                                    |

The strongest transferable lesson is not that finite neural PDEs are impossible. It is narrower and more useful:

> In an unbounded quadratic/Gaussian feature-learning model, fixed-order correctness, squared-loss stability, and exact finite syntax do not imply a convergent closure. Ordinary initialization Taylor/Wick summation and broad positive polynomial compilers fail because rare Gaussian amplitudes generate factorial responses. Any positive theorem for the canonical bounded residual network must instead be real-axis, causal, and explicit about its state topology and response information.

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
\theta=
\left(B_i(0),\frac{a_i(0)}A\right)
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
b(\theta,0)=\theta_{1:d},
\qquad
a(\theta,0)=A\theta_{d+1},
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

Differentiating (6.40), using (6.31)–(6.37), and integrating by parts in $s$ and $w$ gives the exact same-system identity

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

The backbone block in (6.47) uses the projected Gram $G^{h,r_{\mathrm H}}$, not the full slow Gram $G^h$. Replacing it by the latter would no longer be the sensitivity Gram of the same finite PDE.

Equations (6.44)–(6.48) prove that the finite PDE is an exact projected Euclidean-gradient system. They do not prove that its projected tangent kernel equals the dense-limit tangent kernel or that $r_{\mathrm H}\to\infty$ converges.

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
\bigl(b,a,\rho^\theta\bigr)
\longmapsto
\bigl(-b(-\theta),-a(-\theta),J_\#\rho^{-\theta}\bigr).
\tag{6.50}
$$

Initialization is fixed by this transformation, while the output

$$
f=\int ah\,d\mu
$$

and residual $e=f-y$ are invariant. Uniqueness therefore implies

$$
b(-\theta)=-b(\theta),\qquad
a(-\theta)=-a(\theta),
$$

$$
h_q(-\theta)=-h_q(\theta),\qquad
p_q(-\theta)=-p_q(\theta).
\tag{6.51}
$$

Since

$$
\psi_\nu(-\theta)=(-1)^{|\nu|}\psi_\nu(\theta),
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

For the canonical $d=3$ problem, $\theta\in\mathbb R^4$:

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

No new experiment is introduced in this chapter. All numerical values are inherited from the frozen reports and, where available, their later source-level audits.

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
\alpha_{\mathrm{forward}}=-1.00219,\qquad
\alpha_{\mathrm{backward}}=-0.99982
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

An earlier ten-state instantaneous test found median forward/backward relative errors decreasing from roughly $8\times10^{-2}$ at $K=0$, to $5\times10^{-3}$ at $K=1$, $3\times10^{-4}$ at $K=2$, and $1.6\times10^{-5}$ at $K=3$. Positive-time restarts showed the same hierarchy. These results agree with the exact factorial pure-propagator mechanism, while not measuring the full width-independent outgoing residual.

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
G(s,t)=\mathbb E[h(s,\theta,t)^2].
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

On a plain $L^2$ ball, $\widetilde p$ and $\delta z$ may each be only $L^2$, so their product is generally only $L^1$. The obstruction is present already at initialization:

$$
p(1,\eta)=a(\eta)=A\eta_{d+1},
\tag{8.17}
$$

an unbounded Gaussian coordinate. Perturbations concentrated in regions where $|a|$ is large make the multiplier norm arbitrarily large.

Thus the formerly convenient assertion of a cutoff-uniform locally Lipschitz vector field on an $L^2$ ball is false. A valid stability topology must control products, for example through

$$
H_\gamma^s\cap L^4
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

For $s>0$, define the source-weighted Sobolev space

$$
H_\gamma^s
=D((I+\mathsf N)^{s/2}),
$$

$$
\|u\|_{H_\gamma^s}^2
=
\sum_\nu(1+|\nu|)^s|u_\nu|^2.
\tag{8.20}
$$

Then

$$
\boxed{
\|(I-\Pi_{r_{\mathrm H}})u\|_{L^2(\mu)}
\le
(1+r_{\mathrm H})^{-s/2}
\|u\|_{H_\gamma^s}.
}
\tag{8.21}
$$

Equation (8.21) converts a cutoff-uniform positive amount of source regularity into a vanishing aggregate Hermite tail. A targeted sufficient estimate on every compact interval is

$$
\boxed{
\sup_{r_{\mathrm H}}
\sup_{0\le t\le T}
\mathcal E_s[Y_{r_{\mathrm H}}(t)]
<\infty
}
\tag{8.22}
$$

for some $s>0$, where $\mathcal E_s$ controls at least:

$$
\sum_q
\left(
\|h_q\|_{H_\gamma^s}^2
+
\|p_q\|_{H_\gamma^s}^2
\right),
\tag{8.23}
$$

$$
\int_0^1
\mathbb E
\left[
\|c\|_{H_\gamma^s}^2
+
\sum_q|p_q|^2
\left\|
(I+\mathsf N)^{s/2}
(\sigma_wI+R)H_q
\right\|^2
\right]ds,
\tag{8.24}
$$

together with the $L^4$ or Gaussian-Orlicz moments needed for (8.19).

This is a sufficient route, not a theorem already proved and not the only possible compactness formulation. Generic Gaussian Sobolev or Orlicz bounds without source-mode-coercive weights are insufficient: infinitely many orthogonal coordinate functions can share the same unweighted bounds.

If (8.22) is available, the frozen and learned transpose tails satisfy schematically

$$
\|(I-\Pi_{r_{\mathrm H}})T_W\beta_q\|_{L^2}
\lesssim
(1+r_{\mathrm H})^{-s/2}C_T,
\tag{8.25}
$$

$$
\|(I-\Pi_{r_{\mathrm H}})T_c\beta_q\|_{L^2}
\le
\left(
\mathbb E
\|(I-\Pi_{r_{\mathrm H}})c\|_{H_\gamma^s}^2
|\beta_q|^2
\right)^{1/2}.
\tag{8.26}
$$

The hard step is propagating (8.22) through the coupled learned row, nonlinear forward field, and unbounded-terminal-adjoint equations—not proving (8.21).

**Primary provenance.** `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§6.2 and 15.1–15.3; `SCALAR_HERMITE_MINIMAL_EXPERIMENT_REPORT.md`, §7; `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`, §2.3.

### 8.6 The response/Onsager bridge

Source Hermites, row-noise responses, chronological response, and training-time derivatives are distinct axes.

For a sufficiently regular function $F(\eta)$ of the immutable Gaussian source and normalized source Hermite $H_\alpha$,

$$
\mathbb E[F(\eta)H_\alpha(\eta)]
=
\frac1{\sqrt{\alpha!}}
\mathbb E[\partial_\eta^\alpha F(\eta)].
\tag{8.27}
$$

A high source-Hermite coefficient is therefore a high Gaussian source-response coefficient. It is not a high training-time derivative.

The frozen transpose coefficient has the row-noise Stein representation (8.9), which is first order in the coordinate $\epsilon_\nu$, even when the associated source mode $\psi_\nu$ has high degree. Source differentiation $\partial_\eta^\alpha$ and row-noise differentiation $\partial_{\epsilon_\nu}$ must not be identified.

To expose the learned response, choose a common Lagrangian characteristic lift:

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

Equation (8.31) identifies the dynamically generated family that a weighted estimate should control. It also exposes a state question. The Eulerian conditional law $\rho$ does not automatically determine a particular Lagrangian coupling or $R$. One must prove either:

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
\dot Y_r=F_r(Y_r),
$$

the relevant consistency defect is

$$
\mathfrak r_r(Y)
=
F_r(\mathcal P_rY)
-\mathcal P_rF(Y),
\tag{8.34}
$$

not only the pure propagator tail. A valid stability theorem must bound the response

$$
\sup_{t\le T}
\|Y_r(t)-\mathcal P_rY(t)\|
$$

in terms of the compatible initial defect and an integral of $\|\mathfrak r_r\|$ in a topology strong enough to see coherent transpose actions but weak enough for compactness.

**Primary provenance.** `dense_euclidean_continuous_depth_npde_audit.md`, §§5.1–5.5 and 6.2–6.5; `dense_euclidean_continuous_depth_pde_conjecture(1).md`, §5.1; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§6.6, 13.2 and 15.3.

### 8.8 Conditional compact-time Galerkin theorem

The strongest presently valid reduction can be stated as a conditional theorem.

The statement below is pointwise in the static model parameter $\vartheta$. To obtain the uniform claim (8.1), every existence interval, regularity bound, consistency constant, forced gain, and initial projection estimate in the hypotheses must hold uniformly over $\vartheta\in\mathcal U$.

Let $\mathcal P_r$ be the block projection that acts as the identity on the slow fields and as $\Pi_r$ on the source/operator coordinate. Fix $T<\infty$. Assume:

1.  an infinite operator flow $Y$ exists on $[0,T]$;
2.  each finite projected flow $Y_r$ exists uniquely with compatible initial data;
3.  the reachable family has a cutoff-uniform compactness or weighted-regularity bound of the type (8.22);
4.  the nonlinear products are controlled in a stronger-to-weaker topology, such as $H_\gamma^s\cap L^4\to L^2$;
5.  the limiting flow is unique, or a weak–strong uniqueness principle is available;
6.  the projected flows have a cutoff-uniform forced gain $G_T$; and
7.  the full consistency defect satisfies $$
    \|F_r(\mathcal P_rY)-\mathcal P_rF(Y)\|
    \le C_T(1+r)^{-\alpha}
    \tag{8.35}
    $$ for some $\alpha>0$.

Set

$$
\delta_r
=
\|Y_r(0)-\mathcal P_rY(0)\|.
$$

Then

$$
\boxed{
\sup_{0\le t\le T}
\|Y_r(t)-\mathcal P_rY(t)\|
\lesssim
G_T
\left[
\delta_r
+
TC_T(1+r)^{-\alpha}
\right].
}
\tag{8.36}
$$

Locally continuous output and Gram readouts then converge.

With constants uniform over $\mathcal U$, the same estimate may be supremized over $\vartheta$ and yields the uniform compact-time conclusion in (8.1). Without that uniformity it proves only instancewise Galerkin convergence.

There are two proof architectures for these assumptions.

**Compactness and uniqueness.** Use energy equicontinuity plus a compact embedding of the weighted reachable class, extract a subsequence in $C([0,T];X_{\mathrm weak/strong})$, pass to the limit in the drift, and invoke uniqueness to identify every subsequence.

**Forced stability.** Start from a known infinite solution. When the projected initialization is exact, $Y_r(0)=\mathcal P_rY(0)$, directly estimate

$$
\sup_{t\le T}
\|Y_r(t)-\mathcal P_rY(t)\|
\le
G_T
\int_0^T
\|F_r(\mathcal P_rY)-\mathcal P_rF(Y)\|\,dt.
\tag{8.37}
$$

For nonzero compatible initial defect, add the term $G_T\delta_r$, as in (8.36).

Compactness of the one fixed limiting trajectory makes projection consistency plausible; cutoff-uniform control of the forced gain remains essential.

Equation (8.36) proves internal convergence only to the infinite operator flow. It does not identify that flow with the dense limit and does not yield all-time uniformity.

**Primary provenance.** `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`, §2.3; `MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`, §§10.3 and 15.4–15.5.

### 8.9 Ordered dense-limit identification

Even a complete proof of (8.36) leaves a separate identification theorem. The required order is:

$$
n\to\infty\ \text{at fixed }L,
\qquad
L\to\infty,
\qquad
r\to\infty.
\tag{8.38}
$$

No commutation of these limits is assumed.

The identification program has four components.

**Fixed-$L$ causal width theorem.** Derive the infinite-width joint law of forward rows, adjoints, preactivations, and learned row histories for every finite set of row and column queries. Because $W_\ell$ and $W_\ell^\top$ are reused, the limit must retain both reciprocal response kernels or an equivalent conditional Gaussian representation. Ordinary marginal convergence is not enough.

**Exact projected coefficient identity.** At finite width, the projected row coefficient

$$
w_{\ell i,\nu}^n
=\sum_{j=1}^n
W_{\ell,ij}\psi_\nu(\theta_j)
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
\psi_\nu(\theta_j)h_{q,j}^\ell.
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

The output of these steps must be a well-posed infinite operator flow with the same observables as the ordered dense limit. Only then can (8.36) be interpreted as dense-network approximation.

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

- source degree $r$ and mode count $P_r$;
- chronological response grade $K$;
- nonlinear tree grade $J$;
- depth approximation $N$;
- only those historical $\kappa_\alpha$ coordinates required to Markovize cyclic learned-row dependencies.

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
8.  **Compact-time Galerkin convergence.** Prove (8.36).
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
| Two-hidden-layer quadratic/Gaussian program          | Exact derivative/Wick algebra; failure of initial Taylor closure; residual-clock stability; singular effects of an unbounded readout                                      | A no-go theorem for bounded activations, residual depth, or every non-Taylor closure                    |
| Normalized/projected variants                        | Exact jets and nonclosure of natural finite moment lists under the altered geometry                                                                                       | Transfer of the raw positive-coefficient quadratic lower bound, because projector terms introduce signs |
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
| C4  | At each finite Hermite cutoff, the operator–Liouville system uses one shared forward/transpose operator and is the projected Euclidean gradient flow of its finite coefficient state. | **Proved** | Internal PDE theorem for sufficiently regular solutions on their interval of existence; a general global well-posedness theorem is not supplied                                                                                                          |
| C5  | The induced finite-cutoff tangent kernel is positive semidefinite and the PDE loss is nonincreasing.                                                                                  | **Proved** | Internal PDE theorem for sufficiently regular, well-posed finite-cutoff flow; not dense-network equality                                                                                                                                                 |
| C6  | Odd activation plus symmetric initialization makes even source-Hermite shells inert.                                                                                                  | **Proved** | Odd activation, symmetric initialization, and uniqueness of the symmetry-preserving flow; numerical preservation additionally requires parity-compatible cubature                                                                                        |
| C7  | The pure chronological forward tail and exact-source backward tail have factorial Volterra bounds.                                                                                    | **Proved** | Pathwise at fixed $n,L$ under finite $B_{v,T},B_{w,T},\Lambda_T$ (Chapter 6 abbreviates the forward bound as $B_T$); width/depth uniformity requires uniform envelopes; the coupled $E_{A,K,T}$ source defect and nonlinear-tree defects remain separate |
| C8  | The frozen shared-transpose/Riesz operator is bounded on $L^2$ but not compact.                                                                                                       | **Proved** | Frozen isonormal operator; learned and nonlinear terms require separate control                                                                                                                                                                          |
| C9  | Finite-cutoff dissipation yields finite-time state bounds and time equicontinuity for the trainable Lagrangian variables.                                                             | **Proved** | Sufficiently regular finite-cutoff solutions; does not prove global well-posedness, derived $h,p$ bounds, source compactness, or finite all-time arclength                                                                                               |
| C10 | Hermite projection converges strongly on each fixed source query and uniformly on compact query sets.                                                                                 | **Proved** | Fixed $L^2$ queries/compact query families; not uniformly on the unit ball or automatically on the trained reachable family                                                                                                                              |

#### 9.2.2 Quadratic theorem-laboratory claims

| ID  | Claim                                                                                                                                                                                  | Status                      | Scope                                                                                                                                                                                           |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C11 | Squared-loss flow is a residual-gated time change of readout ascent, and a known small feature-profile defect yields a uniform-in-physical-time loss defect.                           | **Proved**                  | Common initial output/clock, target-reaching monotone profiles, and the stated derivative lower/upper bounds                                                                                    |
| C12 | The prescribed initial Wick–Taylor coefficients have a factorial lower bound along an odd subsequence and hence zero radius.                                                           | **Proved**                  | Two-hidden-layer, one-input quadratic model with the stated Gaussian initialization and order of limits                                                                                         |
| C13 | Positive Wick–Taylor partial sums send every subtarget hitting time to zero, so the associated continuous finite closures do not converge uniformly on an interval containing $t=0$.   | **Proved**                  | The specific Taylor compiler and physical-time construction                                                                                                                                     |
| C14 | The zero-radius result rules out every finite-source or real-axis compiler.                                                                                                            | **Falsified in scope**      | It rules out the specified positive Taylor/analytic compiler classes, not all signed, nonanalytic, or response-enriched constructions                                                           |
| C15 | The displayed natural rectangular hierarchy of finitely many polynomial moments/messages closes exactly in the normalized variants.                                                    | **Falsified in scope**      | RMS-normalized and direction-only weight-normalized models; not a no-go for every nonlinear sufficient statistic                                                                                |
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
| C33 | A response-enriched Hermite family converges along one fixed, predeclared diagonal of finite $(r_{\mathrm H},K,J,N)$ cutoffs. | **Open** | The response state and finite drift compiler have not been fully emitted; summable chronological tails alone are insufficient |
| C34 | The compiled PDE state is a restart state for the ordered dense dynamics at physically consistent positive times.             | **Open** | Dense-to-PDE state correspondence plus a uniform continuation estimate; internal PDE autonomy alone is insufficient           |
| C35 | A finite PDE family is controlled directly against finite $n,L$, not only against a separately constructed ordered limit.     | **Open** | Joint finite-network consistency and quantitative width/depth/cutoff error bounds                                             |

### 9.3 Supersession ledger

The main text uses only the corrected formulation. This ledger preserves why earlier claims changed.

| Earlier formulation                                                                                 | Defect found                                                                                                                                                            | Authoritative replacement                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| “One source” by itself expresses nontrivial compression.                                            | One real/source coordinate can encode an arbitrary trajectory or any finite ODE.                                                                                        | Source dimension must be paired with coefficient provenance, fixed grammar, bounded description complexity, autonomy, and uniformity over a declared class. |
| “Only a Taylor-tail lemma remains.”                                                                 | The concrete Wick–Taylor coefficients have zero radius.                                                                                                                 | Global clock stability is proved, but error production for that compiler is large; any surviving construction must be nonperturbative and real-axis.        |
| The quadratic Wick divergence disproves the broad PDE thesis.                                       | The proof uses an unbounded polynomial activation/readout and a positive compiler.                                                                                      | It is a model- and compiler-specific no-go; bounded residual activations remain a separate program.                                                         |
| The tagged-site instantaneous-fitting claim is unconditional.                                       | The causal DMFT representation and response-kernel properties were asserted rather than derived in the project source.                                                  | The Volterra comparison is an exact conditional theorem; DMFT identification is an explicit assumption.                                                     |
| Raw iid depth matrices can be smoothly interpolated as $W(s)$.                                      | Their slice-to-slice fluctuations do not vanish in the required manner.                                                                                                 | Take width first, then homogenize residual depth at the level of conditional means and centered innovations.                                                |
| The $K/J/N$ compiler already emitted a finite PDE.                                                  | Field tables, drift graph, kernels, and cutoff schedule were not fully specified.                                                                                       | The oriented identities and factorial propagation bound survive; the response-enriched PDE is a leading open construction.                                  |
| The hierarchy $P=5\to15\to35$ measures increasing Hermite resolution.                               | The even shell is exactly inert under odd symmetry.                                                                                                                     | Use the parity-correct ladder $P=5\to35\to126\to\cdots$.                                                                                                    |
| Newly opened-mode ratios $0.029$–$0.0589$ are the trained truncation tail.                          | They measure a lifted outgoing source, not the full coupled Cauchy increment.                                                                                           | Aggregate state, observable, and feedback increments are the relevant tail diagnostics; these have not contracted on the available ladder.                  |
| The frozen transpose needs Malliavin differentiability merely to exist.                             | Riesz representation already gives a bounded Hilbert adjoint.                                                                                                           | Differentiability/response regularity is needed only for stronger weighted estimates and causal identification, not bare boundedness.                       |
| Plain $L^2$ gives cutoff-uniform local Lipschitz stability.                                         | Products such as $p\,\delta z$ need not lie in $L^2$; the Gaussian terminal adjoint is unbounded.                                                                       | Work in an $L^4$, Gaussian Sobolev/Orlicz, or strong-to-weak topology, or use a variational/weak–strong argument.                                           |
| A favorable realized secant ratio proves stability.                                                 | One forcing direction is not the worst-case propagator norm.                                                                                                            | Cutoff-uniform forced stability remains open.                                                                                                               |
| Low source degree means an effectively linear activation.                                           | Every cutoff evaluates the full nonlinear $\phi$ and $\phi'$; only label dependence is truncated.                                                                       | The sine stress confirms that low source degree can encode strongly nonlinear activation dynamics.                                                          |
| The $P=5$ PDE is exact or below the dense noise floor.                                              | The dense/PDE discrepancy is statistically resolved.                                                                                                                    | It is close but distinguishable.                                                                                                                            |
| The fourteen cases certify universal generalization.                                                | The family is finite, some numerical gates are unresolved, and simultaneous certification is underpowered.                                                              | They establish broad tested portability, not a uniform theorem.                                                                                             |
| Autonomy of the finite PDE proves that its state is a sufficient restart state for the dense limit. | Internal PDE continuation and dense-state sufficiency are different assertions.                                                                                         | Dense-restart sufficiency requires a state correspondence on physically consistent positive-time dense states and a continuation-error theorem.             |
| The available Hermite data establish convergence or divergence.                                     | The parity-invalid comparison was superseded, while the corrected aggregate increments have not shown replicated contraction and are not a lower bound on target error. | Both empirical convergence and empirical divergence remain open.                                                                                            |

### 9.4 The exact threshold for a result beyond TP and DMFT

A result does not go beyond TP or DMFT merely because it produces deterministic trajectories. Tensor Programs already provides rigorous width-limit machinery for fixed finite programs/training length, and its later depth work already addresses width-then-depth feature learning in its stated scaling. The cited DMFT represents its formal limit through self-consistent stochastic processes and two-time response/correlation state. The additional result sought here is a controlled, architecture-compiled autonomous realization of the canonical ordered target; neither framework is claimed incapable of supplying ingredients for its proof.

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
\forall\ \text{predeclared admissible families }\{\mathsf P_k\},
\qquad
\inf_k E_k(\infty)>0.
$$

An essential nondecaying causal continuum or a lower bound on every finite response/history sector would establish this only if it yields that universal observable-error bound. Failure of the ordered dense observable limit would invalidate the present target contract rather than, by itself, prove a no-go theorem for every differently formulated limit.

Failure of Taylor closure, natural moments, pure Hermites, or one fitted basis is not such a result.

No current result meets either theorem-level falsifier.

### 9.7 Final project assessment

The strongest defensible conclusion has two halves.

The constructive half is already substantive:

> A literal, autonomous, width-independent, nonlinear operator–Liouville PDE has been derived from a standard dense Euclidean-$\mu$P residual architecture. Its finite-cutoff gradient, transpose, kernel, moment, and dissipation structure is exact for sufficiently regular solutions on their interval of existence. Its smallest parity-correct realization predicts active dense feature dynamics with low reported error across a finite tested family, subject to the stated numerical, statistical, and simultaneous-certification limitations.

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
| $D_q^\ell=\operatorname{diag}\phi'(z_q^\ell)$ in Chapter 3, equivalently $\operatorname{diag}\sigma'(z_q^\ell)$ in Chapters 6–8 | Activation Jacobian; $\phi$ and $\sigma$ denote the same activation role in the two local notational conventions |
| $\beta_q^\ell=D_q^\ell p_q^{\ell+1}$                | Backpropagated preactivation message                                                                                       |
| $G^h,G^p,G^\beta$                                   | Normalized Gram matrices of the corresponding fields                                                                       |
| $\Theta$                                            | Tangent kernel, always defined as a sensitivity Gram in the exact finite system                                            |
| $\theta$                                            | Generic immutable Gaussian label in Chapters 1–2; target-row label in the refined row/column conditioning notation of §3.8 |
| $\eta=(B_j(0),a_j(0)/A)$                            | Source-column label in §3.8 and Chapters 6–8                                                                               |
| $\xi=(B_i(0),a_i(0)/A)$                             | Target-row label in Chapters 6–8                                                                                           |
| $\epsilon$ or $\omega$                              | Frozen target-row innovation/noise on a chosen coupling                                                                    |
| $\varphi_\nu$ or $\psi_\nu$                         | Normalized multivariate source-Hermite function; Chapters 6–8 use $\psi_\nu$ to reserve $\sigma$ for the activation        |
| $H_{\nu q}=\int\psi_\nu(\eta)h_q(\eta)\,\mu(d\eta)$ | Source-column Hermite coefficient of the hidden query in Chapters 6–8                                                      |
| $w=(w_\nu)$                                         | Projected row/operator coefficients                                                                                        |
| $\rho_{s,t}^{\xi}$                                  | Conditional law of $w$ for target-row label $\xi$                                                                          |
| $R=D_\epsilon c$                                    | Lagrangian learned row-noise response on a chosen coupling; whether it is measurable from the Eulerian row law is open     |

Chapters 1–2 use $\theta$ generically because no row/column split is yet needed. Once shared-transpose conditioning is exposed, the roles must not be collapsed: §3.8 uses $\eta$ for a source column and $\theta$ for a target row, whereas Chapters 6–8 rename the target row to $\xi$ and retain $\eta$ for the source column.

Several symbols are intentionally local and must be interpreted from their chapter:

| Symbol collision | Global or residual usage                                                                | Quadratic/local usage                                                       |
|------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| $K$              | Chronological response grade                                                            | $K_n=W\operatorname{diag}(h)W^\top$ in Chapter 5                            |
| $\gamma$         | Residual-block scale in Chapters 6–8                                                    | Variance parameter of $W$ in Chapter 5                                      |
| $m$              | Number of training samples                                                              | Local factorial index $m=(k+3)/2$ in the zero-radius proof                  |
| $R$              | Row-noise response, or numerical row-innovation cubature count when explicitly declared | A locally defined Gaussian contraction scalar in the normalized calculation |
| $r$              | Training-sample index                                                                   | Never the Hermite cutoff; that cutoff is $r_{\mathrm H}$                    |

In §3.6 the forward chronological source envelope is $B_{v,T}$; §6.11 abbreviates the same role as $B_T$. The backward exact-source envelope is $B_{w,T}$.

The source label $\eta$ is distinct from the subscripted learning-rate multipliers $\eta_B,\eta_a,\eta_{W_\ell}$. In Chapter 8’s local $H_\gamma^s$ notation, $\gamma$ denotes the Gaussian reference measure and the superscript $s$ is a Sobolev order, not the physical-depth coordinate; Chapter 9 renames that regularity order $\alpha$. Elsewhere Chapters 6–8 use the un-subscripted scalar $\gamma$ for residual-block scale.

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
| Readout initialization | Unbounded Gaussian                                                                    | Gaussian readout; hidden activation is bounded                                           |
| Data                   | One input/sample in the main proof laboratory                                         | Multiple samples; canonical $m=d=3$, with transfer cases                                 |
| Training               | All displayed blocks train under Euclidean-$\mu$P flow                                | All $B,a,W_\ell$ train                                                                   |
| Main positive theorem  | Residual-clock/global observable stability given a small profile defect               | Exact finite-cutoff projected-gradient, PSD, transpose, and dissipation structure        |
| Main negative theorem  | Zero radius and uniform failure of the prescribed Wick–Taylor compiler                | No convergence no-go; pure-Hermite convergence remains open                              |
| Main open bridge       | Nonperturbative real-axis mean-field construction, if this singular model is retained | Ordered dense limit, causal identification, compactness, forced stability, all-time tail |

### B.3 What may and may not be transferred

The following transfer rules are mandatory.

1.  The quadratic factorial lower bound rejects the prescribed ordinary initial Taylor/Wick compiler, and the audited positive analytic compiler classes, in the stated unbounded model. It is a warning against treating time analyticity as automatic; it is not a no-go theorem for bounded residual activations or every real-axis closure.
2.  The residual-clock stability theorem may be reused whenever its monotonicity and small-defect hypotheses are verified. It does not produce the small defect.
3.  The normalized-model jet calculations may be reused as derivative and audit machinery. Their signed projector terms prevent direct reuse of the raw quadratic positivity proof.
4.  The chronological response bound is a depth-ordered real-axis result and survives the quadratic Taylor failure. Its source-substitution and nonlinear-tree residuals remain separate.
5.  Shallow distributional PDE results demonstrate that law-valued closure is possible in special architectures. They do not solve the deep shared-transpose problem.

## Appendix C — Project source and provenance index

### C.1 Supplied core corpus

| Code | File                                                           | Authoritative use in this monograph                                                                                                 |
|------|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| P01  | `approximate_single_source_conjecture_resolution(1).md`        | Zero-radius theorem, physical-time boundary layer, surviving clock stability                                                        |
| P02  | `approximate_single_source_stability(1).md`                    | Exact feature-time reduction and conditional global stability; its former “only missing tail” conclusion is superseded by P01       |
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

### C.3 Primary external framework references

1.  Greg Yang and Edward J. Hu, [*Feature Learning in Infinite-Width Neural Networks*](https://arxiv.org/abs/2011.14522) (Tensor Programs IV).
2.  Greg Yang, Dingli Yu, Chen Zhu, and Soufiane Hayou, [*Tensor Programs VI: Feature Learning in Infinite-Depth Neural Networks*](https://arxiv.org/abs/2310.02244).
3.  Blake Bordelon and Cengiz Pehlevan, [*Self-Consistent Dynamical Field Theory of Kernel Evolution in Wide Neural Networks*](https://arxiv.org/abs/2205.09653).
4.  Song Mei, Andrea Montanari, and Phan-Minh Nguyen, [*A Mean Field View of the Landscape of Two-Layer Neural Networks*](https://arxiv.org/abs/1804.06561).

These references establish the external comparison baseline. This monograph does not claim that TP or DMFT is incapable of producing a finite realization; it claims that such a realization requires an additional compression theorem.

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

An audit “pass” means that no known fatal or major internal inconsistency remains under the available sources. It is not a certification of an open theorem or a reproduction of experiments for which raw arrays/code were not part of the supplied artifact bundle.

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

The completed audit records are:

| Drafted material                        | First audit            | Independent cross-audit      |
|-----------------------------------------|------------------------|------------------------------|
| Chapters 1–3                            | `foundations_audit.md` | `foundations_cross_audit.md` |
| Chapters 4–5                            | `quadratic_audit.md`   | `quadratic_cross_audit.md`   |
| Chapters 6–8                            | `residual_audit.md`    | `residual_cross_audit.md`    |
| Front matter, Chapter 9, and appendices | —                      | `ch9_cross_audit.md`         |

These audits checked the written arguments and reported source claims. They did not rerun experiments, formally verify proofs, or certify the open limiting constructions.

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

The first whole-file pass found and repaired: a missing additive sign in the Chapter 9 forced-stability template; an overbroad Chapter 8 pure-Hermite falsifier list; a missing explicit finite-description/no-unbounded-encoding admissibility clause; one nonzero-initial-defect qualification in the Chapter 8 stability display; local feature/source-coordinate notation collisions; one GFM table-cell delimiter; and several obsolete TeX `\rm` forms. A second complete mechanical and consistency pass found no remaining fatal or major internal inconsistency. The detailed record is `final_whole_document_audit.md`.

### D.5 Final audit outcome

**PASS after repair for the assembled master document.** The nine-chapter monograph is self-contained and internally consistent under the available project corpus, with all known theorem scopes, conditional dependencies, empirical limitations, open bridges, and supersessions preserved. This pass certifies the document’s present logical and structural consistency; it does not prove any open convergence, identification, restart-robustness, or all-time theorem, and it does not reproduce experiments for which raw arrays or code were not supplied. Any future result should update the authoritative claim and supersession ledgers rather than append a parallel “final” narrative.
