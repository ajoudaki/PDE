# Targeted primary-literature audit

Audit date: 2026-09-08. Scope: four categorical prior-art claims, not comprehensive novelty certification. One auditor; no delegated proof reads, experiments, external communications, or source changes. The only written artifact is this file.

The `solve-math-rigorously` and `investigate-conjectures` skills, including the latter's evidence/adversarial references, were read and used to separate quantifiers, models, theorem hypotheses, and proof status. Local project reports located references and specified the comparison model; they were not counted as independent proof. Page numbers below are the PDF/printed pages of the identified versions; TP IV supplement locations are PDF pages.

## 1. Bottom line

| Categorical claim | Targeted finding | Essential qualification |
|---|---|---|
| (i) All DMFT neural-training theories lack even pointwise convergence. | Not defensible. Celentano–Cheng–Montanari (CCM), Theorem 2, gives convergence of empirical **continuous-path laws**, hence finite-time marginals. | Its neural application has fixed hidden width and growing input/sample dimensions. It is not a deep hidden-width limit. |
| (ii) No deep nonlinear feature-learning compact-time width/gradient-flow theorem exists. | Too broad. Nguyen–Pham (NP), Theorems 15, 20–21 and Corollary 17, give nonlinear multilayer mean-field/particle-flow/SGD comparisons uniform on compact time intervals. | Mean-field averaging, neuronal embeddings, and regularity/moment hypotheses differ from iid Gaussian hidden matrices of variance $1/n$. “Trainable nonlinear features” is not a claim of nonzero feature motion in every instance. |
| (iii) Compact-time approximation plus loss convergence to prescribed accuracy is wholly unprecedented. | False as a claim about the proof pattern. It appears explicitly in Chizat–Bach (CB), Appendix C.4, NP Corollary 40, and Mei–Montanari–Nguyen (MMN), Theorem 5. | CB/NP global conclusions have substantial convergence/diversity assumptions; MMN's general prescribed-accuracy result uses noise and regularization. A printed CB limit-interchange lemma is too broad in isolation; the restricted accuracy argument is valid (Section 5 below). |
| (iv) Tensor Programs can never say anything about training-to-convergence. | “Never” is unjustified. A finite-step limit plus a separately established contracting limiting recursion yields iterated-limit and prescribed-accuracy conclusions. | A fixed-program master theorem alone supplies neither a growing-step/continuous-time limit nor uniform-in-time finite-width convergence. The TP III/IV proof qualifications below must not be suppressed. |

These findings do **not** establish that any selected paper proves the project's exact deep, noiseless, iid-(N(0,1/n)), tiny-readout result. Incompatibility is not evidence that a paper's mathematics is merely formal.

### Quantifiers that must remain distinct

For an error $E_n(t)$, the following are different assertions:

1. For each fixed (t), $E_n(t)\to0$.
2. For every fixed $T<\infty$, $\sup_{t\le T}E_n(t)\to0$.
3. Given accuracy $\varepsilon>0$, choose a finite $T_\varepsilon$, then a sufficiently large width, to achieve that accuracy at $T_\varepsilon$.
4. Convergence uniformly for all $t\ge0$, or approximation for specified horizons $T_n\to\infty$.

A finite-program result has another quantifier: the number of instructions/training steps is fixed **before** width tends to infinity. It is not assertion 2 for an underlying gradient flow. Even simultaneous validity at every integer step, obtained by countable intersection, does not yield control along a width-dependent step index.

## 2. Multilayer mean-field primary evidence

### 2.1 Araújo–Oliveira–Yukimura: rigorous, modified multilayer model

Source: Dyego Araújo, Roberto I. Oliveira, Daniel Yukimura, *A Mean-Field Limit for Certain Deep Neural Networks*, [arXiv:1906.00193v1](https://arxiv.org/pdf/1906.00193v1). Model: §§3–4, pp. 9–19; Assumptions 5.1–5.2 and Theorems 5.3–5.5: [pp. 19–22](https://arxiv.org/pdf/1906.00193v1#page=19).

**Model/hypotheses.** Fixed $L\ge3$ hidden layers of common width $N$, fixed input/output and per-edge dimensions. Forward maps use $1/N$ averaging. The input and output edge layers, numbered 0 and $L$, are frozen random features; internal edge layers are trained. Initialization is independent across edges, identically distributed within each layer, independent of iid training samples, and has a width-independent law with finite **first** moment. Bounded initial weights are not assumed. The maps $\sigma^{(\ell)}$, their first derivatives, and the learning schedule/derivative are bounded; map derivatives are Lipschitz; labels are bounded. These are conditions on the entire parameterized maps, not merely boundedness of a usual scalar activation. ReLU does not satisfy them. Compact support of the input distribution is not itself the printed assumption.

The optimizer is fresh-sample SGD with time $k\epsilon$, schedule $\alpha(k\epsilon)$, and $N^2$-scaled internal gradients; population gradient flow is an explicit intermediate system. The limiting object is a McKean–Vlasov **path** law with special endpoint dependence, not independent edge particles everywhere.

**Statements/topology.** Theorem 5.3 proves existence/uniqueness of that path-law dynamics on every prescribed finite interval. Theorem 5.4, Eq. (5.1), bounds expected loss discrepancy at each $k\le\lceil T/\epsilon\rceil$ by

\[
C(T,L)\bigl(\sqrt{d/N}+\epsilon+\sqrt{\epsilon d}\bigr).
\]

Theorem 5.5 supplies a coupled ideal-particle comparison for each selected input-to-output path, with the same type of expected discrepancy bound at each such $k$. The laws concern entire trajectories, but the printed error estimate is **not** an expectation of a supremum over time. A bound uniform in the index on pointwise expectations must not be rewritten as that stronger statement.

**Proof read.** Complete direct §9 proof, pp. 38–42, and §§10–12, pp. 43–58, including SGD/flow martingale comparison, ideal-particle concentration, forward/backward comparisons, and final Gronwall argument. Earlier special-measure construction lemmas in §§7–8 were not all independently re-proved/read through their entire dependency chain. Some intermediate layer cases and the final microscopic extension are abbreviated in the source. The final expected-error argument can use time-integrated expectation/Fubini; it should not be advertised as a joint-in-time high-probability event without an additional argument.

**Use here.** Genuine rigorous nonlinear multilayer approximation with trained internal layers; not an all-layers-trained theorem for the project's central-limit scaling. Its finite-moment initialization assumption also corrects the overbroad statement that all such results require compactly supported initialization. No global optimization claim is extracted.

### 2.2 Nguyen–Pham: compact-time multilayer particle-flow theorem

Source: Phan-Minh Nguyen, Huy Tuan Pham, *A Rigorous Framework for the Mean Field Limit of Multilayer Neural Networks*, [arXiv:2001.11443v3](https://arxiv.org/pdf/2001.11443v3), the February 2023 revision. Definitions/examples/Assumptions 1–4: pp. 7–18; Assumption 5 and main comparison: [pp. 19–24](https://arxiv.org/pdf/2001.11443v3#page=19).

**Model/hypotheses.** Arbitrary fixed $L$ weighted layers, $L-1$ hidden layers, $n_L=1$, $1/n_{i-1}$ forward averaging. Weights and biases can all train. A neuronal embedding specifies functions $w_i(0,c_{i-1},c_i)$, with finite networks obtained by sampling neuronal labels. Independent sampled labels do **not** mean all adjacent edge weights are independent. The framework is Hilbert-space valued and includes the fully connected example; the fixed data distribution may be the uniform law on a finite dataset. Online samples are independent of initialization. Normalized gradients have the corresponding layer-size multipliers (internal weights: $n_{i-1}n_i$); this is not the project's raw matrix parameterization.

Load-bearing conditions are the bounded/Lipschitz schedules of Assumption 1; weighted growth/Lipschitz conditions on forward maps (Assumption 2); backward maps, including bounded terminal error (Assumption 3); the quantitative approximate-independence sampling requirement (Assumption 4, iid neuronal sampling is a sufficient case); and uniform sub-Gaussian moment bounds on embedded initial weights/biases (Assumption 5). The fully connected specialization requires its activation, input, and loss-derivative regularity. An arbitrary unbounded squared-loss derivative is **not automatically covered** by a theorem assuming bounded terminal error. Smooth bounded-derivative losses provide legitimate nonlinear examples. This is not a compact-initialization-only theorem.

**Statements/topology.** Theorem 7, p. 15, gives global-in-time existence/uniqueness of the mean-field ODE (bounds are on each finite interval). Theorem 15, p. 20, compares SGD at $\lfloor t/\epsilon\rfloor$ with the mean-field trajectory. Its $D_T$, Eq. (3), p. 19, is the maximum over layers of the empirical RMS of the **coordinatewise time supremum** of parameter differences. There exist positive $c_1<1/2,c_2<1/52$ such that the high-probability bound is of order

\[
(n_{\min}^{-c_1}+\epsilon^{c_1})
\sqrt{\log(\delta^{-1}n_{\max}^{2}+e)},
\]

with failure probability bounded by $2\delta+KL n_{\max}\exp(-K n_{\min}^{c_2})$, once the theorem's (T,L)-dependent width/step thresholds hold. Joint limits must make these quantities vanish; merely saying “all widths diverge” without controlling extremely unequal growth is insufficient. The theorem initially takes $T\in\epsilon\mathbb N$; this is harmless for covering a prescribed compact interval by a slightly larger mesh endpoint.

Crucially, Theorem 20, p. 23, separately compares the finite **continuous-time population particle ODE** with the mean-field ODE; Theorem 21, p. 24, compares SGD with that particle ODE. Thus this is not just a fixed-number-of-SGD-steps theorem. Corollary 17, pp. 20–21, transfers the estimate uniformly over compact time to bounded Lipschitz hidden-feature tests and Lipschitz output/loss observables. It is a nonlinear evolving-feature limit, not a frozen-NTK approximation, although the theorem does not assert nondegenerate motion for every initialization/data choice.


For a concrete compatible feature-motion check, take the fully connected specialization with several hidden layers, scalar input $x=1$, target $0$, tanh hidden activations, linear readout, positive constant learning schedules, first-layer embedded weights uniform on $[1,2]$, remaining embedded weights initially $1$, and zero biases. Use smooth pseudo-Huber loss $\sqrt{1+f^2}-1$. All initial weights are bounded, the data law is a point mass, and the loss derivative is bounded/Lipschitz. At initialization the output, backward factors, weights and tanh derivatives are positive. The displayed mean-field gradient equations therefore give strictly negative first-layer weight drift and nonzero hidden-feature drift, with no width factor suppressing it. This is an elementary specialization, not a claim about Gaussian matrix initialization or functional diversity for global optimization; it shows that “nonlinear features may train” need not be merely nominal in the compact-time theorem.

**Proof read.** Complete direct proofs of Theorems 15, 20, 21, pp. 22–26; complete proofs of their comparison Propositions 22–24 in Appendix C.1, pp. 78–98; complete Corollary 17 proof, pp. 99–100. The mechanism is conditional concentration across sampled labels, forward/backward stability, time discretization, a martingale bound for SGD, and truncation of sub-Gaussian initialization before Gronwall. The direct Theorem 7 proof, pp. 16–17, was read; not every earlier moment/tail lemma in its recursive dependency tree was audited through its full proof. This is substantial direct-proof evidence, not a claim that the entire 125-page paper has been independently certified.

**Global qualification.** [Assumption 8 and Theorem 38, pp. 45–46](https://arxiv.org/pdf/2001.11443v3#page=45), require functional bidirectional diversity, appropriate activation/loss/data regularity and density properties, **assumed convergence of weights in specified weighted norms**, and uniform asymptotic stationarity of the last layer. Theorem 38's convex-loss conclusion is global optimality; its zero-loss alternative additionally requires deterministic labels and the stated zero-gradient/zero-loss condition. The complete proof in §7.5, pp. 48–52, was read: finite-time flow reversal preserves functional support; density plus stationarity eliminates a nonoptimal residual. This does not prove the assumed weight convergence. The paper explicitly notes on p. 47 that iid initialization fails its functional diversity condition for $L\ge3$. Corollary 40, p. 48, combines finite-time approximation with this **conditional** global theorem in an iterated width/step-then-time limit. It is prior evidence for the accuracy-transfer pattern, not an unconditional iid deep optimization theorem.

### 2.3 Sirignano–Spiliopoulos: two-hidden-layer, iterated widths

Source: Justin Sirignano, Konstantinos Spiliopoulos, *Mean Field Analysis of Deep Neural Networks*, [arXiv:1903.04440v5](https://arxiv.org/pdf/1903.04440v5). Main model, Assumption 2.1, Lemma 2.2, Theorem 2.3: [pp. 3–6](https://arxiv.org/pdf/1903.04440v5#page=3).

The proved model is

\[
g^{N_1,N_2}(x)=\frac1{N_2}\sum_i C_i
\sigma\!\left(\frac1{N_1}\sum_j W^2_{ij}\sigma(W^1_j\cdot x)\right).
\]

Input dimension is fixed; both hidden layers and readout train. The activation is $C_b^2$; data and initial parameters have compact support; initial laws have the stated continuous densities and independence. SGD uses fresh iid data, clock $k=\lfloor N_1t\rfloor$, and multipliers $\alpha_C=N_2/N_1$, $\alpha_{W^1}=1$, $\alpha_{W^2}=N_2$.

The limit is **$N_1\to\infty$ first, then $N_2\to\infty$**. Lemma 2.2 uses a measure-valued Skorokhod-path limit with $N_2$ fixed. Theorem 2.3 gives the final output convergence in probability at fixed (t,x); its second-stage estimate is $\sup_x\mathbb E|g_t^{N_2}(x)-g_t(x)|\le C(T)/\sqrt{N_2}$ for $t\le T$. Do not replace this by simultaneous equal-width convergence or by $\mathbb E\sup_t$ convergence.

Complete Theorem 2.3 proof (§5, pp. 18–25), uniqueness proof (§6, pp. 25–27), and Appendix A, pp. 27–33, were read. Appendix A.2 explicitly outsources its martingale estimate to an earlier paper; A.3 also omits final fixed-point details by reference. Those external proofs were not recursively audited. The three-hidden-layer discussion in §4.2, p. 16, leaves rigorous proof for future work; it must not be promoted to the same proved all-depth theorem.

Theorem 3.4, p. 9, is also **conditional**: Assumptions 3.1/3.3 include analytic/strictly increasing activation, bias/data/support conditions, and the theorem assumes convergence to a suitably nondegenerate limiting density with finite moments. Its full direct proof, pp. 10–12, was read. Remark 3.6 expressly leaves the convergence assumption open. Neither that theorem nor the abstract licenses unconditional global optimization for arbitrary iid deep networks.

## 3. Rigorous DMFT: what dimension grows?

### 3.1 Celentano–Cheng–Montanari

Source: Michael Celentano, Chen Cheng, Andrea Montanari, *The high-dimensional asymptotics of first order methods with random data*, [author PDF, dated December 14, 2021](https://web.stanford.edu/~chen96/papers/fom_dynamics.pdf). This audit is of that 83-page text, not a later revised arXiv version. Assumption 1 and Theorems 1–2: [pp. 7–8](https://web.stanford.edu/~chen96/papers/fom_dynamics.pdf#page=7).

**Model.** $X\in\mathbb R^{n\times d}$ has iid centered sub-Gaussian entries of variance $1/d$; $n/d\to\delta\in(0,\infty)$. The state is $\Theta\in\mathbb R^{d\times k}$ with fixed $k$, and

\[
\dot\Theta_t=-\Theta_t\Lambda_t-\delta^{-1}X^\top\ell_t(X\Theta_t;z).
\]

The same random dataset is reused throughout continuous-time dynamics. Initial state and auxiliary (z) are independent of (X); their empirical laws converge weakly with convergent finite second moments. Gaussian initialization with the appropriate moments is a possible specialization, not a mandatory assumption. The nonlinearity and its Jacobian are globally Lipschitz in state/time, uniformly in (z); $\Lambda_t$ is bounded, symmetric and Lipschitz. Theorem 1 also requires the explicit second-moment bound (16), including $\ell_t(0;z)$.

For safety, the conclusion here uses bounded/constant (z) with smooth bounded dependence, rather than treating the printed lack of a regularity condition in (z) as permission for arbitrary discontinuous/uncontrolled label dependence. In §4.1 a fixed-dimensional planted signal can be appended as nonmoving columns, subject to Assumption 2; random labels depending on (X) are not simply declared independent.

**Theorems.** Theorem 1 constructs a unique DMFT solution on every finite interval. Theorem 2 gives convergence **in probability of empirical path measures**, in any metric metrizing weak convergence on $C([0,T],\mathbb R^k)$; there is also the joint (z)/projection-path law. Evaluation at fixed times is continuous, so pointwise-time empirical-law convergence follows. Remark 3.2, pp. 8–9, spells out bounded continuous tests, and the Gaussian-design strengthening permits continuous tests of at most quadratic growth. This is not a coupling showing every particle path converges to a deterministic coordinate path.

**Neural scope.** Eq. (24), p. 9, is a **one-hidden-layer network with fixed hidden width $k$**, fixed readout coefficients, and trained input weights. Smooth bounded activations/loss derivatives in the stated regularity class give nonlinear examples. Input dimension and sample size grow; hidden width does not. Thus this rigorously contradicts (i) as written, but does not settle a deep hidden-width DMFT theorem in the project's model.

**Proof read.** Complete direct Theorem 1 proof (§5, pp. 15–21) and Theorem 2 proof (§6, pp. 21–24), plus complete Appendix C, pp. 52–76. This includes the finite-step AMP representation/state-evolution reduction, dimension-uniform flow discretization, identification of discrete/continuous DMFT, and path tightness. Not all contraction lemmas of Appendix B were read through their proofs, and the externally invoked AMP universality/state-evolution theorems [CL21, Theorem 2.4] and [JM13, Theorem 1] were not recursively proof-audited. Consequently this is a full direct convergence-proof read with declared external dependencies, not an axiom-to-theorem certification. The stationary-point discussion is not used as an unconditional long-time theorem.

### 3.2 Nishiyama–Imaizumi: corroboration, with a printed-proof qualification

Source: *High-Dimensional Limit of Stochastic Gradient Flow via Dynamical Mean-Field Theory*, [arXiv:2602.06320v2](https://arxiv.org/pdf/2602.06320v2), February 2026. Model and assumptions: pp. 4–8; Theorems 3.1–3.2: [p. 7](https://arxiv.org/pdf/2602.06320v2#page=7).

Again, input/sample dimensions grow proportionally and the number of state columns is fixed. Design entries are independent centered sub-Gaussians of variance $1/d$; the initial state/auxiliary data are independent of the design and their empirical laws satisfy the stated all-(p) Wasserstein moment conditions. Drift maps and derivatives obey Lipschitz/polynomial-growth assumptions. This is a data-dependent-noise **SGF SDE**, not a proof that ordinary mini-batch SGD itself has exactly that limit; the paper cautions about this distinction on p. 5.

Theorem 3.1 gives well-posedness on a sufficiently small interval in general. It allows every prescribed finite interval when the noise parameter $\tau=0$, or under its alternative zero-Hessian condition. Theorem 3.2 gives $W_2$ convergence in probability of empirical **joint finite-time marginals**, not a stated $W_2$ theorem on path space. The noiseless specialization is continuous-time gradient dynamics, but still not a deep growing-hidden-width result.

The complete direct proofs, Appendix C, pp. 19–32, and Appendix D, pp. 33–44, were read, together with the rigorous DMFT formulation in Appendix B, pp. 15–19. They use contraction, dimension-uniform discretization, and an external finite-step AMP theorem (Wang 2024, Theorem 2.21), whose proof was not independently read. A literal inconsistency needs correction/reconciliation: Definition C.2, p. 20, assigns a generally nonzero initial value to the covariance $\Sigma_\ell(0,0)$, whereas Eq. (39), p. 16, defines it through the integrated process starting at zero. This affects the declared fixed-point space. The PDF/proofs are available; this is **not** a clean uncorrected-proof certification. CCM, not this supplementary check, carries the main conclusion about (i).

## 4. Tensor Programs: exact supported scope and proof dependency

### 4.1 TP IV G.4 is the moment-feedback, fixed-program theorem

Sources: Greg Yang, Edward J. Hu, *Feature Learning in Infinite-Width Neural Networks*, [ICML 2021 main paper](https://proceedings.mlr.press/v139/yang21c/yang21c.pdf) and [official supplement](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf). Complete relevant statements read: Definition G.1, Setup G.2, Definition G.3 and Theorem G.4, supplement pp. 11–14; Remarks L.1–L.2, Definition L.3 and Assumption L.4, pp. 21–22. Supplement p. 1 explicitly restricts its training-time results to time independent of width.

Under Setup G.2, different initial matrices have mutually independent iid $N(0,\sigma_W^2/n)$ entries; initial vector-coordinate tuples are iid copies of a fixed joint Gaussian vector. Initial vector/matrix sources must have the independence required by the Gaussian setup. Initial scalars converge almost surely to deterministic constants. Width-dependent vanishing scalars are permitted; the source explicitly mentions them.

A **fixed finite** program can use matrix multiplication and transposes, coordinatewise nonlinearities, empirical scalar moments, and feed those scalar moments back into subsequent operations. Assumption L.4 requires joint pseudo-Lipschitz regularity in vector and scalar arguments when vector arguments occur. Scalar-only Moment operations need only continuity. Thus a continuous loss derivative can be applied to a scalar prediction; multiplication of residual scalars by vector quantities must still satisfy the appropriate joint regularity condition.

Theorem G.4 asserts almost-sure convergence of every fixed pseudo-Lipschitz empirical test of finitely many program vectors and of program scalars to the recursively defined expectations. It does **not** require a positive-definite initial source covariance or separately assume rank stability in this version. The alternative less-regular master theorem does require rank stability; the two versions must not be conflated.

**Singular sources and response coefficients.** In Remark L.2 set

\[
C_{ij}=\mathbb E[Z^{y_i}Z^{y_j}],\qquad
b_i=\mathbb E[\widehat Z^{W^\top y_i}Z^x],\qquad a=C^+b.
\]

The normalization is $\sigma_W^2\mathbb E[\partial Z^x/\partial\widehat Z^{W^\top y_i}]=a_i$ in the pseudoinverse convention; the factor $\sigma_W^2$ must not be lost. For singular $C$, the invariant object is the contracted correction $\sum_i a_i Z^{y_i}$. One cannot identify every off-support formal derivative vector with the pseudoinverse vector: components in the nullspace are invisible after contraction. The Gaussian sources for $W$ and $W^\top$ are separated in Definition G.3, but full $Z$-variables acquire response correlations. This is not an independence assertion about the full forward/backward variables. Nor does use of $C^+$ prove continuity of that pseudoinverse across a change of rank.

Definition L.3's ancillary claim that composition adds pseudo-Lipschitz degrees is incorrect as printed. For example $x^3\circ x^3=x^9$; degrees 2 and 2 do not yield degree 4. Closure of the **class** is valid with a sufficiently large finite degree, e.g. $(d_1+1)(d_2+1)-1$. This repair suffices when only finite polynomial growth, rather than that numerical degree, is used.

### 4.2 Full relevant master-proof read; not blanket uncorrected applicability

G.4 does not contain a new self-contained proof in the TP IV supplement: it points to Theorem E.15 of Yang's *Tensor Programs III: Neural Matrix Laws*, [arXiv:2009.10685v3](https://arxiv.org/pdf/2009.10685v3). The primary TP III text was read, not just the project's correction notes: Setup 2.2/Box 1, the appendix theorem assumptions/statements (pp. 29–33), and complete Appendices K, L, M, N, pp. 45–87. This covers Gaussian conditioning, the core-set/rank argument, projected-Gaussian moment estimates, the parameter-controlled extension, and the no-rank-stability extension.

The six correction groups located by earlier local audits were checked against the primary printed proof. With the notation of the source, they include:

| Primary location | Correction needed in the proof |
|---|---|
| K.9, p. 48 | Conditional mean $ZQ^+ + P^{+\top}X^\top-P^{+\top}P^\top ZQ^+$; the printed undefined $Y$ and a $Q^\top$ where the pseudoinverse is needed must be repaired. |
| K.23, p. 59 | The single-collision exponent is $n^{2p-1-(p-1)/4}=n^{(7p-3)/4}$, not $n^{7(p-1)/4}$. After normalization it is $n^{-(p+3)/4}$, still summable for the selected $p\ge6$. |
| L.3, case 2, p. 64 | Gaussian conditioning is on the **hatted Gaussian sources**; the resulting correction columns are the full, unhatted $Z$-variables. The singular case must be read as a contracted regression identity. |
| L.6, p. 66 | Conditional variance is $\sigma_A^2[(h^\top h)/n-\gamma^\top\Upsilon^+\gamma]$, not a further $1/n$ applied to the already-normalized regression term. |
| L.19, p. 76 | The variance identity uses the input $Z^h$ and yields $\mathring\sigma^2$: $\sigma_A^2[\mathbb E(Z^h)^2-\mathring\gamma^\top\mathring\Upsilon^+\mathring\gamma]$. It is not the printed output-variable/standard-deviation expression. |
| L.23, p. 83 | The bound on $\max(\sigma^2d_\alpha,\mathring\sigma^2)^p$ uses $\max(\sigma^2,\mathring\sigma^2)^p$, not exponent $p/2$. |

These are mathematical repair notes, not a claim that all uses of every version of TP III have now been certified. In particular, G.4 uses the **additional Appendix N extension**. Two further issues matter there:

* In N.3, p. 86, write $\widehat h^0=h^0-\Pi h^0$ and $s_n=(\|\widehat h^0\|^2/n)^{1/2}$. The core vector must be $h^1=\widehat h^0/s_n$, with $h^0=s_nh^1+\Pi h^0$. The printed choice neither residualizes nor correctly normalizes and therefore does not establish the announced orthogonality invariant. This is a concrete algebraic repair.
* Lemma N.2, p. 87, asserts convergence/boundedness of conditional regression coefficients after conditioning on both core and vanishing-moment vectors. The proof gives no sufficient control of coefficients when the corresponding finite-width Gram matrices lose rank, beyond referring to the limiting hatted/dotted decomposition. That limiting decomposition is precisely what the extension must justify. Bounded operator norm establishes vanishing normalized second moment of $A\Delta h$, **not by itself all higher empirical moments**. I did not verify the stronger coefficient/all-moment step from the printed argument. Similarly, scalar feedback depending on vanishing vectors needs to be accounted for when the preceding paragraph proposes conditioning only on core vectors.

The last item is an **unclosed proof obligation in this audit**, not a counterexample to G.4. A proof repair or another applicable primary theorem may resolve it. Therefore the permitted handoff is: the theorem **states** that singular covariance and pseudo-Lipschitz moment feedback are allowed; the finite-program encoding is meaningful; but this audit does not certify uncorrected blanket applicability of the entire E.15/G.4 class.

### 4.3 Application boundary for the local three-hidden-layer report

The comparison model in `OPERATOR2_L3_AUDITED_REPORT.md` has fixed $p,d$, distinct norm-$\sqrt d$ inputs, labels $\pm1$, $\phi=\sin+\cos$, first weights $N(0,I_d/d)$, hidden matrices (N(0,1/n)), readout $c_i\sim N(0,n^{-4})$, and multipliers (n/d,1,1,1/n). This local description is context, not external proof.

For a **fixed** number of Euler steps, the proposed encoding has the right structural ingredients for G.4: first-layer preactivations are iid joint Gaussian coordinate tuples with possibly singular data Gram covariance; the two initial hidden matrices are independent Gaussian sources; $C=nc=n^{-1}g$ is expressible using an iid standard Gaussian vector $g$ and a vanishing initial scalar. Trigonometric maps, their derivatives, finite products, and empirical inner products are pseudo-Lipschitz of some finite degree. Expanding trained matrices as their initial matrices plus finitely many past rank-one updates uses moment feedback and transpose operations, not fresh independent matrices at each step. This is a **syntax/hypothesis check**, subject to the master-proof qualification above. The main paper's activation-specific parametrization classification must not independently be applied to $\sin+\cos$ without checking its narrower activation assumptions.

The requested mesh condition is $n\eta_n\to0$, hence the step count on a positive fixed physical interval satisfies

\[
K_n\asymp T/\eta_n,\qquad K_n/n\to\infty.
\]

No cited fixed-program theorem supplies that diagonal. Allowing a vanishing scalar $\eta_n$ in a fixed program only makes its fixed number of steps cover vanishing physical time. Needed separately are width-uniform Euler/flow stability and moment bounds, tightness/equicontinuity in a specified path topology, and identification/uniqueness of the continuous limiting evolution. Uniformity as $T\to\infty$, autonomous current-state closure/restartability, and differentiation of limiting moments require still further arguments. This audit neither proves nor disproves those missing bridges.

### 4.4 TP training-to-convergence: a precise permissible inference

Source: Greg Yang, Etai Littwin, *Tensor Programs IIb: Architectural Universality of Neural Tangent Kernel Training Dynamics*, [arXiv:2105.03703v1](https://arxiv.org/pdf/2105.03703v1). Setup 5.2 and Theorem 5.3: p. 6; Master Theorem B.4 and Assumption B.8: pp. 16–17. Complete Appendix D training proof, pp. 18–28, was read; some final architecture/optimizer extensions are abbreviated by the authors. B.4 explicitly points to TP III E.15; there is no independent B.4 proof in IIb that bypasses Appendix N.

The theorem treats a fixed architecture/finite computation at NTK parameterization, with Gaussian initialized underlying parameters: hidden matrices $w/\sqrt n$, input matrices $u/\sqrt d$, readout $v/\sqrt n$. Training is discrete SGD (the displayed setup uses batch size one and normalized step size); the limiting recursion is a kernel recursion for each fixed iteration. Readout initialization produces a random GP output, so a deterministic zero initial predictor must not be silently substituted. Use the continuous **loss derivative** condition in the proof, not an insufficient assertion that loss continuity alone suffices. This is lazy/kernel training, not an evolving nonlinear feature-learning theorem. Its general proof imports a master theorem; Section 4.2 prevents treating all architectures as independently certified here.

Here is a conditional mathematical consequence, not an extra theorem claimed verbatim by the paper. Suppose an applicable finite-step specialization gives full-batch square-loss recursion on a finite dataset,

\[
e_{k+1}=(I-\eta K_\infty)e_k,
\quad K_\infty\succ0,
\quad 0<\eta<2/\lambda_{\max}(K_\infty).
\]

For loss $\frac12\|e\|^2$, $q=\max_j|1-\eta\lambda_j(K_\infty)|<1$, so $\|e_k\|\le q^k\|e_0\|$. This proves zero loss in the **width-first, iteration-second** limit. For high-probability prescribed accuracy, first bound the random initial GP norm at the desired confidence, choose a finite $k$, then take width large enough for the finite-step comparison. Kernel positivity and applicability to the chosen optimizer/data are separate hypotheses, not universal properties supplied by Tensor Programs. Rank-deficient kernels require the residual to lie in the learnable range. None of this proves convergence of every sufficiently wide finite network for all future iterations, or justifies interchanging the limits. It is nevertheless something mathematically meaningful about training-to-convergence, so “can never say anything” is the wrong boundary.

## 5. Shallow global optimization and prescribed accuracy

### 5.1 Chizat–Bach: the valid accuracy argument, and an overbroad lemma

Source: Lénaïc Chizat, Francis Bach, *On the Global Convergence of Gradient Descent for Over-parameterized Models using Optimal Transport*, [arXiv:1805.09545v2](https://arxiv.org/pdf/1805.09545v2). Assumption 2.1, particle-flow definition and Theorem 2.6: pp. 3–5; Assumptions 3.2/3.4, Theorems 3.3/3.5: pp. 6–7; [Lemma C.15 and proof: pp. 25–26](https://arxiv.org/pdf/1805.09545v2#page=25).

The model is a $1/m$-averaged collection of trainable particles with functional

\[
F(\mu)=R\!\left(\int\Phi(u)\,d\mu(u)\right)+\int V(u)\,d\mu(u).
\]

One-hidden-layer networks are a specialization, with (u) including feature and output-weight parameters. (R) is a smooth convex loss on a Hilbert prediction space, for example $L^2$ of a fixed data law. (V) is the allowed semiconvex regularizer. Particle dynamics is the **continuous-time** rescaled gradient/subgradient flow $-m\partial F_m$; despite the title, no discrete-SGD compact-limit theorem is inferred here. Initialization converges in $W_2$, with all supports in a common $Q_{r_0}$; iid sampling is sufficient, not necessary. Assumption 2.1's local regularity and sublinear derivative growth control trajectories on compact time intervals. Theorem 2.6 supplies the particle/measure-flow limit; its proof explicitly uses compact-time uniform weak-measure convergence and the requisite continuity/control of the functional.

Global Theorems 3.3/3.5 add 2-homogeneity or partial 1-homogeneity, support **separation**, Sard-type regularity, and, for the latter, boundary/asymptotic conditions. They **assume convergence** of the limiting measure in $W_2$; Appendix C weakens this to convergence of an appropriate projected measure but does not eliminate it. The initialization supports and topology are essential; arbitrary small finite particle supports do not themselves have the limiting separation property.

**Valid and sufficient prior proof pattern.** Once $F(\mu_t)\to F_{\min}:=\inf F$ is known, fix $\varepsilon>0$. Choose $T$ with $F(\mu_T)<F_{\min}+\varepsilon/2$, then $m_0$ so $F(\mu_{m,T})<F(\mu_T)+\varepsilon/2$ for all $m\ge m_0$. Monotonicity of each finite particle flow gives

\[
\forall m\ge m_0\ \forall t\ge T:\qquad
F_{\min}\le F(\mu_{m,t})<F_{\min}+\varepsilon.
\]

This argument, explicitly used in Appendix C.4, needs no all-time trajectory approximation. It is stronger than accuracy just at $T$, but it relies on a global lower bound matching the limiting loss.

**Do not rubber-stamp Lemma C.15 in isolation.** It prints equality of both iterated limits assuming only $F(\mu_t)\to F^*$. Its proof establishes the required upper bound, not the reverse bound when $F^*>\inf F$. A direct counterexample under Assumption 2.1 is $\Omega=\mathbb R$, $\Phi(u)=u^2$, $V=0$, $R(s)=(s-1)^2$, $Q_r=[-r,r]$. Start the limiting flow at $\mu_0=\delta_0$, so $F(\mu_t)=1$ forever. Start each (m)-particle flow with all particles $u_i(0)=1/m$, which converges to $\delta_0$ in $W_2$. Symmetry gives $\dot u=4u(1-u^2)$, hence $u(t)\to1$ and finite-particle loss tends to zero. The two iterated limits are 1 and 0. The restricted **global-optimality** application above is unaffected. This audit uses that restricted statement, not the false unrestricted interchange.

**Proof read/remaining qualifications.** Complete Appendices B and C, pp. 14–28, including existence/uniqueness, many-particle convergence, escape and support-separation arguments; the relevant neural specialization and Appendix D.3, p. 29, were also read. The latter requires moment/boundary qualifications; its displayed proof needs both the fourth and $2d-2$ data moments, so the printed minimum of these orders in Proposition 4.2 must not be used without reconciliation. There are also local cross-reference/sign/time-of-crossing slips in the partial-homogeneous proof. This audit does not certify every printed global specialization. The elementary, globally lower-bounded accuracy-transfer argument above is independently verified and already defeats the asserted novelty of the pattern.

### 5.2 Mei–Montanari–Nguyen: an explicit accuracy theorem with noise/regularization

Source: Song Mei, Andrea Montanari, Phan-Minh Nguyen, *A Mean Field View of the Landscape of Two-Layer Neural Networks*, [arXiv:1804.06561v2](https://arxiv.org/pdf/1804.06561v2). Model Eqs. (1), (3), (7), (11)–(12): pp. 3–6; Assumptions A1–A4, Theorems 3–5: [pp. 12–14](https://arxiv.org/pdf/1804.06561v2#page=12).

The network is $f_N(x)=N^{-1}\sum_i\sigma_*(x;\theta_i)$, with fixed parameter/input dimension and iid particle initialization. One-pass SGD means fresh iid training samples, with step $\epsilon\xi(k\epsilon)$, and all included particle coordinates train. A fixed empirical data law can be sampled with replacement, but an arbitrary deterministic sequence of reused examples is not the stated model. A1 requires a bounded Lipschitz schedule with infinite accumulated training time. A2 requires bounded $\sigma_*$ and labels and uniformly sub-Gaussian parameter gradients. A3 requires bounded Lipschitz interaction-potential gradients. Thus the unconstrained parameterization $a\sigma(w\cdot x)$ with arbitrarily large $a$ is not automatically an A2 example.

Theorem 3 gives compact-time, high-probability errors for empirical bounded Lipschitz tests and risk of size

\[
Ce^{CT}\sqrt{N^{-1}\vee\epsilon}
\bigl(\sqrt{D+\log(N/\epsilon)}+z\bigr).
\]

The joint-limit conditions include $N/\log(N/\epsilon)\to\infty$ and $\epsilon\log(N/\epsilon)\to0$. The proof couples finite trajectories with nonlinear processes; it is not just a theorem at a fixed number of SGD updates.

For Theorem 5, the optimizer is instead **regularized noisy SGD**, Eq. (11), with finite inverse temperature $\beta$ and positive weight decay $\lambda$ bounded above/below. A4 adds $C^4$ potential regularity; initialization must be absolutely continuous, sub-Gaussian, and have finite free energy. To directly combine the stated noisy Theorem 3 with the optimization theorem, stay in their common parameter range, in particular the former's $\lambda\le1$. Given accuracy (a>0), Theorem 5 chooses $\beta\ge K(a)D$, then a finite $T$, and requires $N,1/\epsilon\ge C_0e^{C_0T}D$, $\epsilon\ge N^{-10}$. For each indicated $k\in[T/\epsilon,10T/\epsilon]$, its risk guarantee is

\[
R_N(\theta^k)\le\inf_{\rho}R_\lambda(\rho)+a
\]

with the prescribed high probability. It is not a theorem of noiseless deep interpolation, and its target is a **regularized** benchmark. No useful general dimension/accuracy complexity bound for $T$ is extracted.

**Proof read and caveats.** Complete direct Theorem 3 proof (§7.1–7.2, pp. 24–32) and complete optimization proof development in §10, pp. 76–90, including Theorems 4–5, were read. The compact proof has a finite-particle independence assertion that needs the usual repair: evaluate the empirical fluctuation at the independent nonlinear-process particle and control the first-argument change by the coupling error. Theorem 4's printed Eq. (22) uses an unregularized benchmark, but Lemma 10.5, Eq. (10.16), p. 79, and the proof of Theorem 5 support the regularized benchmark above. Positive weight decay cannot simply be discarded by sending temperature to zero.

I do not mark the general global diffusion proof as independently closed: the passage in Lemma 10.12, p. 88, from integrability of dissipation to its full-time vanishing needs an additional continuity/time-shift argument; weak convergence of densities alone also does not justify the square-root weak-limit identification used on p. 89. Those may be repairable with further analytic estimates, but such repairs were not completed here. The source contains an explicit published prescribed-accuracy theorem and the relevant proof architecture; its whole generality is not silently certified. Claim (iii)'s proof-pattern correction already follows from the independently checked argument in Section 5.1.

## 6. Added linear-literature scope check

Source: Lénaïc Chizat, Maria Colombo, Xavier Fernández-Real, Alessio Figalli, *Infinite-width limit of deep linear neural networks*, [author PDF](https://people.math.ethz.ch/~afigalli/papers-pdf/Infinite-width-limit-of-deep-linear-neural-networks.pdf).

Following the user's added reference, I independently read the complete [§6, pp. 37–42](https://people.math.ethz.ch/~afigalli/papers-pdf/Infinite-width-limit-of-deep-linear-neural-networks.pdf#page=37), and introduction pp. 1–2. The core theorem and its complete proof were **not** audited here, so this entry is a scope check, not a substitute for that audit.

The paper's main treatment is the three-weight-layer/two-hidden-layer linear network. In §6, $L$ counts **middle square matrices**: $L+1$ hidden layers and $L+2$ weighted layers. Its $L=1$ is the project's two-hidden-layer case; its $L=2$ is the project's three-hidden-layer case. All activations are linear, though parameter dynamics are nonlinear. The formal construction has Gaussian initial endpoint vectors, fixed independent $Z^{(\ell)}$ matrices, zero initial update matrices $W^{(\ell)}$, actual middle operators $m^{-1/2}Z^{(\ell)}+m^{-1}W^{(\ell)}$, and the layer-scaled GD recursion (6.1). It assumes the requisite data moments.

Most importantly, §6 explicitly calls its arguments **formal**, assuming the Gaussian-basis/vanishing-error structure before deriving the broader-depth recursion. The introduction likewise distinguishes the core three-layer analysis from the final extension without technical details. Do not promote Eqs. (6.2)–(6.9), or the explicit $L=2$ indexing, into a fully proof-audited all-depth theorem. Conversely, the formality of §6 does not make the paper's separate core theorem formal. No claim about its complete core convergence/global-optimization proof is made in this audit.

## 7. Evidence completeness and defensible novelty wording

All named PDFs/proof sections above were available and personally read to the declared extent. “Full direct proof read” means the complete relevant printed proof, not every recursively cited external theorem. Explicit limits are: AOY's earlier special-measure construction and abbreviated cases; NP's earlier moment/tail dependency tree; SS's outsourced estimates; CCM's remaining contraction/AMP dependencies; NI's external AMP dependency and fixed-point inconsistency; TP III Appendix N's unclosed coefficient step; MMN's remaining analytic steps; and the unaudited CCFF core. This file distinguishes these from unavailable proofs—none of those primary PDFs was unavailable. The selected revisions are not asserted to be the final or strongest versions in the literature.

Corrections to project-wide assumptions that should survive consolidation:

* “Not our initialization/scaling” is not “nonrigorous.” Multilayer mean-field compact-time mathematics exists, including continuous particle-flow comparisons.
* “All prior initializations are bounded” is wrong for the selected AOY/NP versions. The actual obstruction is often scaling, embedding structure, or optimization diversity, not Gaussianity alone.
* Rigorous high-dimensional DMFT can have continuous-path convergence while failing to address growing hidden width.
* A theorem about trainable nonlinear features need not establish strict feature movement for every dataset; a zero-loss theorem needs more than finite-time approximation.
* Singular covariance is allowed in the stated TP IV theorem; it does not grant rank-uniform pseudoinverse estimates, and the printed master-proof corrections/dependencies remain relevant.
* Compact-time approximation plus an independently proved global limiting-loss theorem already gives prescribed accuracy by a finite-horizon argument. This is weaker than all-time trajectory approximation, but often sufficient for optimization.
* Conditional global theorems must retain their convergence/diversity assumptions. Noise and regularization must remain in both optimizer and benchmark. Formal broader-depth sections must stay marked formal.

A defensible, **unverified novelty candidate**, rather than a certified novelty claim, is the following particular package:

> A joint width/vanishing-step compact-time theorem for a specified all-layers-trained deep nonlinear network with iid hidden (N(0,1/n)) matrices, the project's tiny readout and balanced mobilities, fixed finite data including singular source covariance, and genuinely non-lazy feature evolution; together with a well-posed continuous limiting dynamics and a loss-to-prescribed-accuracy theorem that does not assume the desired weight convergence, impose incompatible functional-diversity initialization, add diffusion/regularization, or substitute a frozen-kernel regime.

The exact topology, simultaneous width/step quantifiers, arbitrary-depth versus fixed-depth scope, and whether an autonomous/restartable state representation is claimed must be specified. If the intended novelty additionally includes explicit growing-horizon rates or uniform-in-time finite-width control, those are separate stronger obligations. The targeted sources above do not establish that entire package for the comparison model. That observation is **not** evidence that no other primary paper does, nor does it close any mathematical gap in the project's own argument.
