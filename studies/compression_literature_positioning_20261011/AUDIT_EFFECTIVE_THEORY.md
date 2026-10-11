# Independent full-source audit: The Principles of Deep Learning Theory

Completed 11 October 2026. Scope: finite autonomous descriptions of nonlinear feature-learning trajectories, initialization dependence, approximation order, training horizon, and retained information. This is an unscored public-source mathematical audit, not an evaluation of every claim in the book.

## Outcome

The book supplies a substantive **finite, autonomous, fixed-data, finite-order training description**: outputs, the neural tangent kernel (NTK), and its first differential evolve together, with two second-differential tensors frozen at the retained order. It also solves time-dependent perturbation equations, not just the fitted endpoint. These contributions survive this audit.

It does **not** establish an exact compressed representation of an arbitrary finite-width network's complete trajectory, a uniform-in-training-time pathwise remainder, or a fixed-size representation of the learned function on unrestricted new inputs. Its ensemble description and its description of one initialization must not be conflated.

| ID | Finding | Classification and reach |
|---|---|---|
| L1 | Both NTK-fluctuation signs in (∞.79)/(∞.154) are reversed relative to expansion of the correct free solution (∞.93). The quadratic mean contribution in (∞.162) inherits the error. | **Minor Flaw**: a local sign repair preserves the main argument and qualitative result. It nevertheless changes the stated finite-width prediction. |
| M1 | Individual-realization orders are mixed with weak ensemble orders. The displayed \(O(n^{-2})\) endpoint remainder and the particular-network 1% estimate on p.374 lack pathwise justification. An exactly solvable allowed subcase has a nondegenerate \(n^{-3/2}\) omitted term. | **Major Flaw for the strong pathwise/uniform-error interpretation**: repair materially weakens the claim to a formal or suitably specified weak expansion. Not a refutation of that weaker expansion. |
| M2 | The earlier-layer covariance asserted to be \(O(n^{-2})\) in p.189 footnote35, (6.108), can be exactly \(2g^2/n\), including for a single fixed-neuron observable. | **Major Flaw within the claimed extra layer-by-layer suppression**: that qualitative suppression must be abandoned. Ancillary to the book-wide program. |
| L2 | The all-orders raw-moment scaling in p.87 footnote8 confuses moments with cumulants. | **Minor Flaw**: the weaker estimate actually needed at that step survives. |
| L3 | General sample-cost formula (ε.25) is off by two powers relative to its own expansion index and preceding examples. | **Minor Flaw**: that sequence requires \(O(N_D^{2k+2})\), not \(O(N_D^{2k})\). Neither is a proved minimum encoding cost. |

No fatal book-wide flaw is established. Formal probability-density truncation, nonsmooth activations, other parameter scalings, and arbitrary optimizers require the qualifications below; they are not silently treated as errors in results that exclude them.

## 1. Source identity, independence, and coverage

The frozen source is arXiv:2106.10165v2 [cs.LG], dated 24 August 2021, **471 PDF pages**. Its title-page authors are Daniel A. Roberts and Sho Yaida, based on research in collaboration with Boris Hanin.

- PDF: data/generated/compression_literature_positioning_20261011/hierarchies/roberts_yaida_hanin_v2.pdf; 4,786,010 bytes; SHA-256: 39431828579ea31513eb6de8d6a4bee3d524d8a4f398537d5a0b3900dba92361.
- Text: same stem with .txt extension; 29,690 lines, 212,148 words, 2,053,241 bytes; SHA-256: a86473222f83b6a31070e163721436cd29f6d849170bb0a10af18f2f699a2435.
- Page citations are **printed pages**. Printed page \(p\) is 1-based PDF page \(p+8\).
- Full sequential reading reached text EOF: front matter, Chapters0–11, Chapter∞, Epilogueε, both appendices, bibliography, and index. Truncated tool outputs were reread before counting coverage.
- Visual PDF checks confirmed pp.87, 189, 357, 361, 374, 375, 377, and 398, including the decisive signs/order/counting passages. Full-source reading means complete extracted-text reading plus targeted visual checks, **not** visual inspection of every PDF page or reconstruction of every proof.

Only the assigned frozen source and mandatory review, severity, rigorous-mathematics, and canonical-neural-notation instructions were read as inputs to this audit. No author study narrative, previous review, manuscript comparison, other study, or another reviewer's findings supplied scientific evidence. No new external sources were introduced. No source-code execution or training occurred; PDF rendering was document processing. The preface describes numerical checks maintained in private notebooks; those checks were not supplied or independently verified.

### Read versus reconstruction coverage

| Complete portion read | Reconstruction/checking performed |
|---|---|
| Front matter and Chapters0–3 | Architecture and initialization; exact deep-linear moment recursion; fixed-depth versus depth/width limit; nonuniformity in moment degree. |
| Chapters4–5 | Conditional-Gaussian metric; leading connected four-point mechanism; raw-moment order; fixed observed-neuron restriction; quartic truncation; scope of critical depth scaling. Not every activation's asymptotic recursion was rederived. |
| Chapters6–10 | Earlier-layer Bayesian covariance; fixed-kernel/free training; inverse expansion; NTK variance versus typical fluctuation. Not the complete Bayesian posterior or every generalization expression. |
| Chapter11 and all Chapter∞ | Contracted derivative definitions and closure algebra; coefficient trajectory versus endpoint; stable free dynamics and first-order convolution; endpoint signs and mean cascade; initialization/activation restrictions; tensor counts. Every lengthy layer recursion for the eleven ensemble tensors was read, but not independently rederived term by term. |
| Epilogueε | Ensemble information count, growing test-set dependence, order/sample-cost sequence. |
| AppendixA | Meaning and limitations of entropy/information expansions and the cubic optimal-aspect-ratio proxy; not the complete entropy algebra. |
| AppendixB | Residual architecture, critical initialization, modified fluctuation coefficient, and reliance on AppendixA's proxy. It provides no general residual-network finite-width training theorem. |
| Bibliography and index | Complete reading for source coverage and dependency inventory; cited papers were not thereby audited. |

## 2. Common setup and notation

Preserve the book's convention: \(L\) counts affine layers including the output layer, hence there are \(L-1\) hidden layers. For \(x\in\mathbb R^{n_0}\),

\[
z^{(1)}(x)=b^{(1)}+W^{(1)}x,\qquad
z^{(\ell+1)}(x)=b^{(\ell+1)}+W^{(\ell+1)}\sigma(z^{(\ell)}(x)),\qquad
f(x;\theta)=z^{(L)}(x)\in\mathbb R^q,
\]

where \(q=n_L\), \(\sigma\) acts coordinatewise, and \(\theta\) contains

\[
P=\sum_{\ell=1}^{L}n_\ell(n_{\ell-1}+1)
\]

weights and biases. Initialization is independent centered Gaussian, with bias variance \(C_b^{(\ell)}\) and weight variance \(C_W^{(\ell)}/n_{\ell-1}\), (2.19)–(2.22). The constant positive-semidefinite learning-rate matrix \(\Lambda\) is layer/block diagonal, with weight entries \(\lambda_W^{(\ell)}/n_{\ell-1}\) and bias entries \(\lambda_b^{(\ell)}\). These scalings are hypotheses, not dispensable conventions.

Let \(\mathcal D=\mathcal A\cup\mathcal B\) be a fixed finite training/test set, \(N_D=|\mathcal D|\), \(N_A=|\mathcal A|\). A combined output/sample index \(a=(i,\delta)\) ranges over \(M=qN_D\) observations; \(A\) denotes its training subset. With residual \(r_a=f_a-y_a\), the summed MSE loss and update are

\[
\mathcal L(\theta)=\frac12\sum_{a\in A}r_a^2,\qquad
\theta_{t+1}=\theta_t-\eta\Lambda\sum_{a\in A}\nabla_\theta f_a(\theta_t)r_a(t).
\]

An averaged loss rescales \(\eta\). In the initial expansion hidden widths are comparable to \(n\to\infty\), with \(L,q,N_D\) and the selected observables fixed. Subsequent depth asymptotics identify \(L/n\) as an accumulating expansion parameter in specified critically initialized families. They are not uniform statements over all initialization, activations, sample sizes, or width-dependent learning rates.

## 3. Five claim-level audits

### C1. Initialization has a leading non-Gaussian hierarchy, not an exact finite closure

**Source/hypotheses.** Chapters3–5; (3.45)–(3.47), (3.56)–(3.57), (4.40), (4.44), and pp.95–100. Independent Gaussian initialization is essential. The source itself notes on p.48 that non-Gaussian weight effects can enter at the retained \(1/n\) order.

Conditional on one layer's activations, the next preactivations are exactly Gaussian with random covariance

\[
\widehat G^{(\ell+1)}_{\alpha\beta}
=C_b^{(\ell+1)}+
\frac{C_W^{(\ell+1)}}{n_\ell}
\sum_{j=1}^{n_\ell}\sigma(z^{(\ell)}_{j\alpha})\sigma(z^{(\ell)}_{j\beta}).
\]

Its mean \(G=\mathbb E\widehat G\) is the covariance, and fluctuations of \(\widehat G\) generate the connected four-point tensor. This conditioning mechanism is exact; the resulting finite moment truncation is not.

**Exact check.** For a bias-free critically initialized linear network with equal hidden width \(n\), let \(G_2^{(\ell)}=\mathbb E[(z_i^{(\ell)})^2]\) and \(G_4^{(\ell)}=\mathbb E[(z_i^{(\ell)})^4]/3\) at one fixed input. The normalized four-point coefficient is

\[
\frac{G_4^{(\ell)}}{(G_2^{(\ell)})^2}
=\left(1+\frac2n\right)^{\ell-1}.
\]

Conditioning successively proves this: the next empirical variance equals the current variance times an independent \(\chi_n^2/n\), whose second moment is \(1+2/n\). At fixed \(\ell\), the normalized connected correction is \(2(\ell-1)/n+O_\ell(n^{-2})\). If \((\ell-1)/n\to r\), its exact limit is \(e^{2r}-1=2r+O(r^2)\), not exactly \(2r\). The book's small-\(r\) reading is consistent. The corresponding fixed-\(m\) normalized \(2m\)-point factor tends to \(e^{m(m-1)r}\); p.69 footnote8 explicitly warns that the expansion is not uniform in \(m\).

Thus the source supports a finite-order expansion with depth accumulation, not exact truncation at unrestricted \(r>0\).

**L2: raw moments versus cumulants.** Printed p.87 footnote8 derives a centered third metric moment of order \(n^{-2}\), then asserts the general centered raw \(m\)-th moment is \(O(n^{-(m-1)})\). For iid centered \(X_j\), variance \(v\),

\[
\mathbb E\left(\frac1n\sum_jX_j\right)^4
=\frac{3v^2}{n^2}+\frac{\kappa_4(X_1)}{n^3}.
\]

The pairings produce the first term; only the fourth cumulant has the asserted \(n^{-3}\) scaling. Taking \(X_j=Z_j^2-g\), \(Z_j\sim N(0,g)\), gives \(12g^4/n^2+48g^4/n^3\). The weaker estimate needed to discard this term at first order survives. This is a minor correction, not a failure of the leading quartic calculation.

**Density and marginal qualifications.** For one observed neuron and input with positive metric fluctuation variance, the action has the form

\[
S(z)=\frac12g_2z^2-\frac18v_4z^4+\cdots,\qquad v_4>0.
\]

The quartic-only density proportional to \(e^{-S(z)}\) is not normalizable: its tails grow exponentially in \(z^4\). Gaussian perturbation coefficients and weak asymptotic moment expansions can nevertheless be valid. A literal global probability model requires a stabilizing completion, cutoff, or a specified asymptotic interpretation; omitted terms are not uniformly small in the tails. This is a qualification of formal truncation, not evidence that the calculated coefficients are wrong.

Likewise, the fixed number of observed neurons in pp.95–100 matters. A fixed-marginal expansion is not automatically a uniform approximation to an entire \(n\)-neuron hidden layer.

**Judgment/cascade.** The checked conditioning identity and linear recursion are sound and highly plausible. The general finite-width density remains a formal approximation without the strong uniform remainder needed for exact trajectory compression. L2 leaves the leading non-Gaussian contribution intact.

### C2. Feature learning is present, but the claimed extra backward-layer suppression is false

**Source/hypotheses.** Bayesian representation changes (6.99), (6.104), pp.187–189; Chapter11's dNTK and its preactivation correlations (11.45), (11.49), (11.52); §§11.3–11.4 and Chapter∞. These depend on the specified initialization and learning-rate scaling. The smooth finite-width training calculation expressly excludes ReLU and other nonsmooth cases on pp.335–346; squared second-derivative quantities do not become justified by substituting distributions.

If \(\mathcal H_{ab}=\nabla f_a^T\Lambda\nabla f_b\) and \(\mathcal T_{abc}\) is the Hessian contraction defined in C3, the exact gradient-flow identity is

\[
\dot{\mathcal H}_{ab}
=-\sum_{c\in A}(\mathcal T_{abc}+\mathcal T_{bac})r_c.
\]

The feature inner products therefore change. In the source's scaling the leading ensemble interactions are order \(1/n\), with depth amplification in the critically initialized families studied. This is a perturbative feature-learning mechanism, not an impossibility theorem for every other infinite-width parameterization.

**M2: exact counterexample to (6.108).** Page189 footnote35 asserts that an \((L-2)\)-layer observable's posterior update is \(O(n^{-2})\), reducing it to a claimed covariance order.

Take a three-affine-layer bias-free linear network, both hidden widths \(n\), scalar output, \(C_W^{(2)}=C_W^{(3)}=1\), and one input whose first-layer neurons \(Z_j=z_j^{(1)}\) are iid \(N(0,g)\), \(g>0\). Define

\[
q_1=\frac1n\sum_jZ_j^2,\qquad
q_2=\frac1n\sum_j(z_j^{(2)})^2.
\]

Conditional on layer1, the layer2 neurons are independent \(N(0,q_1)\), so \(\mathbb E[q_2\mid z^{(1)}]=q_1\). The output stochastic metric is \(\widehat G^{(3)}=q_2\). For the single fixed-neuron observable \(O=(z_1^{(1)})^2\),

\[
\begin{aligned}
\mathbb E[(\widehat G^{(3)}-g)O]
&=\operatorname{Cov}(q_2,Z_1^2)
=\operatorname{Cov}(q_1,Z_1^2)\\
&=\frac{\operatorname{Var}(Z_1^2)}n
=\frac{2g^2}{n}.
\end{aligned}
\]

This exact counterexample avoids any growing-observable loophole. The cited conditioning/Taylor identities (8.54), (8.70) do not create an additional inverse-width factor. At the level of the book's first-order Bayes formula, an observed output \(y\) gives coefficient \((y^2-g)/n\), generically nonzero, rather than the proposed order \(n^{-2}\).

**Cascade/survival.** The explanation that each earlier layer adds another \(1/n\) suppression fails and cannot justify layerwise locality or compression. The penultimate-layer update, the existence of Bayesian feature changes, and the independent gradient-based dNTK mechanism do not depend on this extra suppression. A linear counterexample suffices for a claimed general MLP statement; it is not evidence against nonlinear feature learning.

**Judgment.** The checked feature-learning identity is sound. The asserted earlier-layer order is clearly false. Correcting it changes the qualitative depth-suppression assertion, hence a major flaw within that assertion, but not a book-wide fatality.

### C3. The retained hierarchy is autonomous and finite-data, with substantial fixed information

**Source.** Definitions (∞.4)–(∞.9); difference equations (∞.81)–(∞.83), pp.358–359; coefficient trajectories (∞.101), (∞.117), (∞.121)/(∞.124); endpoint (∞.141); cubic feature model (11.151)–(11.152); ensemble description (ε.13)–(ε.25).

Use parameter coordinates \(F_a(w)=f_a(\theta_{\rm init}+\Lambda^{1/2}w)\), \(w\in\mathbb R^P\). With derivatives at the current state, define

\[
g_a=\nabla F_a,\quad B_a=\nabla^2F_a,\quad C_a=\nabla^3F_a,
\]
\[
\mathcal H_{ab}=g_a\cdot g_b,\quad
\mathcal T_{abc}=B_a[g_b,g_c],\quad
\mathcal U_{abcd}=C_a[g_b,g_c,g_d],\quad
\mathcal V_{abcd}=(B_ag_c)\cdot(B_bg_d).
\]

These are the source's NTK, dNTK, ddNTK-I and ddNTK-II. The calligraphic notation distinguishes the last object from its separately named ensemble four-point vertex \(V\). They are explicit contractions of the network derivatives, not arbitrary new learned parameters.

Summing repeated \(b,c,d\) over training observations, Taylor/product rules give the retained system

\[
\begin{aligned}
f_a^+&=f_a-\eta\mathcal H_{ab}r_b
 +\frac{\eta^2}{2}\mathcal T_{abc}r_br_c
 -\frac{\eta^3}{6}\mathcal U_{abcd}r_br_cr_d,\\
\mathcal H_{ab}^+&=\mathcal H_{ab}
 -\eta(\mathcal T_{abc}+\mathcal T_{bac})r_c
 +\frac{\eta^2}{2}(\mathcal U_{abcd}+\mathcal U_{bacd}+2\mathcal V_{abcd})r_cr_d,\\
\mathcal T_{abc}^+&=\mathcal T_{abc}
 -\eta(\mathcal U_{abcd}+\mathcal V_{abcd}+\mathcal V_{acbd})r_d.
\end{aligned}
\]

The first line is the directional Taylor expansion through order3. In the second, differentiating both gradients produces \(2\mathcal V\). In the third, differentiating the Hessian produces \(\mathcal U\), and the two gradient derivatives produce the two \(\mathcal V\) terms. This checks the central algebra and coefficients. The source freezes \(\mathcal U,\mathcal V\) at their initial retained-order values and discards higher-order terms, then solves with a consistent perturbative order projection. Solving the unprojected polynomial surrogate exactly may retain uncontrolled higher-order products.

For fixed labels, data and algorithm, this system is genuinely autonomous: it requires no externally supplied history. Its coefficient solutions cover time-dependent trajectories before the endpoint limit. Calling the work “endpoint only” would be incorrect.

What is not established is exact closure for the original network. Exact differentiation continues into higher derivatives/contractions; their neglect is an approximation obligation, not a consequence of autonomous notation.

#### Retained-coordinate ledger

Counts below are dense entries, not minimal independent dimension or memory lower bounds.

| Representation | Moving objects | Fixed information retained |
|---|---|---|
| Original network | \(P\) weights/biases | Architecture, activation, data, optimizer; the function is evaluated by the network. |
| Individual fixed-data hierarchy | \(f,\mathcal H,\mathcal T\): \(M+M^2+M^3\) dense entries | Initial \(\mathcal U,\mathcal V\): \(2M^4\) entries, plus labels/algorithm. Initial values of every moving object are also needed. |
| Infinite-width fitted ensemble, (ε.14) | Not a trajectory state for one realization | \(qN_A+N_D(N_D+1)\): labels and two symmetric sample kernels. |
| Leading finite-width fitted ensemble, (ε.13)/(ε.15) | Ensemble description | Two rank-two tensors \(G,H\), eleven rank-four tensors \(V,A,B,D,F,P,Q,R,S,T,U\): raw upper count \(qN_A+2N_D^2+11N_D^4\), before symmetries. Output dimension is fixed. |
| Endpoint algorithm projectors, (∞.142)–(∞.147) | None after data/algorithm are fixed | Two rank-four and four rank-six sample tensors: \(2N_A^4+4N_A^6\) if materialized. They are computed functions of lower-order kernels and \(\eta\), not independent information; factorization can avoid allocating all entries. |

The NTK is symmetric, \(\mathcal T\) is symmetric in its final two slots, and \(\mathcal U\) in its final three. Architecture-dependent relations can reduce these upper counts further; they do not make retained functions free.

For the quadratic model in §11.4, \(d=n_f+1\) feature coordinates require \(d+d(d+1)/2\) fixed ordinary/meta-feature functions per input, alongside \(qd\) trainable coefficients. The cubic parameter-space representation (11.151) retains, per scalar output and input, \(P+P(P+1)/2+P(P+1)(P+2)/6\) derivative coefficients, plus the base output in a Taylor expansion about initialization. These are constrained inherited functions, not independent trainable degrees of freedom, but their evaluation/storage cannot be omitted from a representation claim.

**L3: sample-cost index shift.** Equations (ε.14), (ε.15), (ε.23) give \(N_D^2,N_D^4,N_D^6\) for retained orders \(k=0,1,2\). With \(k\) defined by retaining \(n^{-k}\) in (ε.24), the compatible pattern is \(N_D^{2k+2}\), not (ε.25)'s \(N_D^{2k}\). This is a local correction; the leading \(N_D^4\) count survives. No minimum encoding complexity is proved by either pattern.

**Scope.** Page398 footnote7 explicitly says new test samples increase \(N_D\), contrasting the sample-space description with a trained microscopic network. Thus no unrestricted-input fixed-size function compression follows. Ensemble means/cumulants do not identify one realization's trajectory: its realized initial tensors, or their joint random initialization law at a stated approximation order, are needed. The endpoint trained kernel (∞.155) is data/algorithm dependent and nonunique, not an independently specified initialization kernel that alone generates the trajectory.

**Judgment.** The checked contraction algebra is sound and the finite-order autonomous construction is nontrivial. It is approximate and fixed-data. Comparative novelty is not independently scored in this single-source audit.

### C4. The endpoint fluctuation expansion has a verified sign error

**Source.** Correct free solution (∞.93), p.361; inverse expansion (∞.71), p.354; two-update result (∞.79), p.357; general endpoint (∞.141), p.372; final prediction (∞.154), p.375; mean term (∞.162), p.377. Decisive printed signs were visually checked.

Let \(K=\mathbb E\widehat H_{AA}\) be the invertible mean training NTK, \(J=\mathbb E\widehat H_{BA}\) the mean test/train block, realized blocks \(K+\Delta K,J+\Delta J\), initial training error \(e=f_A(0)-y_A\), and \(C=\Delta J-JK^{-1}\Delta K\). Here the subscripts \(A,B\) select training and test observations. The exact constant-kernel endpoint is

\[
f_B(\infty)=f_B(0)-(J+\Delta J)(K+\Delta K)^{-1}e.
\]

For \(\|K^{-1}\Delta K\|<1\), the Neumann series yields

\[
\boxed{
f_B(\infty)=f_B(0)-JK^{-1}e
-CK^{-1}e
+CK^{-1}\Delta K K^{-1}e+R_3.
}
\]

For uniformly bounded \(K^{-1}\), \(R_3\) is cubic in fluctuations. Both displayed fluctuation signs are opposite to (∞.79)/(∞.154). The source's unexpanded (∞.93), free term of (∞.141), and inverse expansion (∞.71) have the correct signs. This is an internal inconsistency.

**Exactly solvable allowed subcase.** Freeze the first layer of a bias-free linear two-affine-layer network and train only a scalar linear readout with mobility \(1/n\), initialized with independent weights \(v_j\sim N(0,1/n)\). Two orthogonal suitably normalized inputs give iid independent standard Gaussian hidden coordinates \(X_j,Y_j\), independent of the readout weights. Then

\[
\widehat H_{AA}=\frac1n\sum_jX_j^2=1+E,\qquad
\widehat H_{BA}=\frac1n\sum_jX_jY_j=D,\qquad K=1,\ J=0.
\]

All second/higher derivatives in the active parameters vanish, so all dNTK/ddNTK terms are exactly zero. The exact endpoint is

\[
f_B(\infty)=f_B(0)-\frac{D}{1+E}e.
\]

The printed terms give \(f_B(0)+De-DEe\), versus the correct \(f_B(0)-De+DEe\). The leading difference is \(2De\), typically \(n^{-1/2}\). The training kernel is positive almost surely. Gradient flow converges; constant-step gradient descent converges if \(0<\eta<2/(1+E)\). No simulated experiment is needed.

**Mean cascade.** Under centered output-layer sign symmetry, NTK fluctuations are invariant while initial outputs reverse sign. Odd expectations involving one initial output vanish. Since the fluctuations are centered, the corrected pure-fluctuation contribution to the mean is

\[
-\mathbb E[CK^{-1}\Delta K]K^{-1}y_A,
\]

opposite to the printed contribution. Thus (∞.162)'s \(m^{\Delta\mathrm{NTK}}\), together with its training-set projection in (∞.160), needs its sign reversed. Statistics derived from the erroneous endpoint require their cancellations to be rechecked; this does not imply that every derived statistic is wrong.

**Judgment/cascade.** L1 is a verified error. Correcting two signs repairs the free fluctuation terms without discarding the free trajectory, inverse expansion, hierarchy, or the separate nonlinear projector terms. A local repair preserving the qualitative result is a **Minor Flaw** under the prescribed rubric, even in a prominent formula.

### C5. Coefficientwise infinite-time limits are available; uniform pathwise approximation is not

**Source.** Individual residual (∞.65), p.351; mean-for-realized-NTK substitution (∞.76)–(∞.78), pp.355–356; free evolution (∞.88)–(∞.93), pp.360–361; first-order convergence pp.368–369; error interpretation/percentage p.374; stability-boundary caveat p.381 footnote25.

Solving retained coefficient equations, taking their infinite-time limit, and proving the original network stays uniformly close are three different obligations. The source substantially addresses the first two; the third does not follow.

**Checked convergence mechanism.** For a fixed realized training kernel \(A_0\succ0\), put \(U=I-\eta A_0\). If

\[
0<\eta<2/\lambda_{\max}(A_0),\qquad \rho=\|U\|_2<1,
\]

the free residual is \(r^{(0)}(t)=U^tr(0)\). Leading dNTK/NTK coefficient corrections are bounded sums of decaying residual products. If the resulting first-order forcing obeys \(\|F(t)\|\le C\rho^t\), its zero-initial-data training solution satisfies

\[
\|r^{(1)}(t)\|
\le\eta\sum_{s=0}^{t-1}\rho^{t-1-s}\|F(s)\|
\le\eta Ct\rho^{t-1}\longrightarrow0.
\]

The test-output driving sums also converge. This validates the coefficientwise mechanism for a fixed stable kernel; constants depend on data, residual, kernel and step size. It is not a network-versus-surrogate bound. The source does warn that some algorithm-projector factors diverge at the stability boundary.

**M1: pathwise versus weak order.** NTK variance \(O(1/n)\) generically means fluctuations \(O_p(n^{-1/2})\), not \(O_p(n^{-1})\). In C4's random-feature example,

\[
\operatorname{Var}(E)=2/n,\qquad \operatorname{Var}(D)=1/n.
\]

A mean-kernel Newton step leaves exactly \(r(1)=-Er(0)\), contradicting (∞.65)'s \(O(1/n)\) individual-residual order under the ordinary typical/pathwise interpretation. A squared or suitable averaged error can have order \(1/n\), but is a different quantity.

Even after L1's sign correction, the quadratic endpoint expansion has exact remainder

\[
R_3=-\frac{DE^2}{1+E}e.
\]

The iid sample averages \(X_j^2-1\) and \(X_jY_j\), multiplied by \(\sqrt n\), converge jointly to independent \(Z_E\sim N(0,2)\), \(Z_D\sim N(0,1)\). Conditional on the hidden features, the initialized training output is \(N(0,1+E)\). Since \(E\to0\) in probability, its conditional characteristic function tends to that of \(Z_f\sim N(0,1)\), independently of the limiting metric fluctuations. Consequently, for any fixed scalar target \(y\),

\[
n^{3/2}R_3\ \Longrightarrow\ -Z_D Z_E^2(Z_f-y),
\]

with independent limiting variables and a nondegenerate product. This proves typical order \(n^{-3/2}\), not \(n^{-2}\), rather than merely estimating it dimensionally. Hence the displayed endpoint remainder has no conventional \(O_p(n^{-2})\) interpretation even in this smooth solvable subcase. Averaging may suppress odd fluctuations and yield an integer-order **weak** expansion, but that meaning needs a specified observable class and proof.

Similarly, multiplying a residual \(O_p(n^{-1})\) by a neglected NTK fluctuation \(O_p(n^{-1/2})\) in the pp.355–356 substitution naturally produces \(O_p(n^{-3/2})\), not automatically \(O_p(n^{-2})\). This is not an objection to systematic ensemble power counting; it is a warning against substituting it for a pathwise bound.

**Uniform-time remainder obligation.** A formal per-step error cannot simply be summed through infinitely many steps or justify exchanging width and training-time limits. Even a linear stable error recurrence with forcing at most \(\varepsilon_n\) accumulates a bound \(\varepsilon_n/(1-\rho)\). Shrinking spectral gap can worsen its order. Test accumulation and nonlinear feedback need further control.

A strong theorem requires a specified norm/probability statement, width-uniform conditioning and stability, derivatives/tensor bounds along the path, controlled labels/initial residual, and remainder estimates compatible with the time limit. These are not supplied for p.374's broad particular-network statement. Its \(L=10,n=100\) approximately-1% example simply substitutes into \((L/n)^2\); no error constant or relative-error denominator is given. It is not a certified quantitative guarantee.

**Algorithm/activation scope.** The all-algorithms endpoint form is expressly conjectural on p.374 footnote22 and qualified to MSE; a different cross-entropy form is anticipated. Actually developed cases include constant-rate full-batch MSE gradient descent, gradient flow, and specially chosen generalized second-order updates. These do not establish arbitrary adaptive optimization, stochastic gradients, weight decay, or arbitrary finite-horizon stopping. The smooth-activation restriction remains; smoothing ReLU introduces another approximation and potentially singular limit.

**Judgment/cascade.** The free solution and fixed-kernel convergence mechanism are sound. A weak/formal expansion remains plausible and supported by the construction. The individual-network \(O(n^{-2})\) interpretation fails in the explicit free subcase; uniform complete-trajectory accuracy and the quoted percentage are not established. Weakening these assertions materially changes their scope, making M1 major for that stronger claim, not fatal to the effective-theory program.

## 4. What the complete appendices add

AppendixA derives entropy/mutual-information expansions at initialization and an optimal aspect-ratio proxy from a cubic truncation, (A.72). For population sizes \(m_1,m_2\), its optimum is proportional to \(1/[(20+3m_1+3m_2)\nu]\), with activation-dependent fluctuation coefficient \(\nu\). This is an unsupervised information proxy, not a proof of test-risk optimality, a finite-time fitted endpoint, or uniform trajectory accuracy. At the stationary point of a quadratic-minus-cubic proxy, the cubic term is already \(2/3\) of the quadratic term; existence of the stationary point does not control omitted terms. Growing observed populations also require the marginal-uniformity checks in C1.

AppendixB studies fixed-width residual MLPs with skip factor \(\gamma\), adjusted critical initialization, and modified two-/four-point fluctuation scaling. Its optimal-depth discussion uses AppendixA's proxy. It does not supply a separate exact finite full-training reduction for arbitrary residual architectures.

Neither appendix repairs L1/M2 or supplies M1's missing estimates. Their initialization-side mechanisms remain meaningful in the stated approximation regimes. No broad falsity verdict is assigned to their unchecked coefficients.

## 5. Dependencies, remaining obligations, and conclusion

The decisive reconstructions use the frozen book plus explicit Gaussian conditioning/moments, Taylor/product rules, finite-dimensional matrix inversion, geometric-series estimates, and the standard iid multivariate central limit theorem. In the latter use, the summands are iid centered vectors \((X_j^2-1,X_jY_j)\) with finite covariance \(\operatorname{diag}(2,1)\); thus its hypotheses are satisfied. No specialized external result is invoked without checking its prerequisites.

The book's background references [57], [62], [66], [67], [70] and numerical claims were not independently audited. This is a coverage limitation, not “source unavailable”: retrieval was not attempted because those sources are unnecessary for the internal counterexamples. Their citations do not certify width/depth-uniform estimates here.

Remaining obligations include a weak-remainder theorem with specified observables; pathwise versus ensemble orders throughout Chapter∞; uniform control of the original trajectory; downstream statistics after L1; and extension beyond the smooth, perturbative regime. Every source section was read, but all eleven tensor recursions, all AppendixA entropy coefficients, and unrelated generalization claims were not reconstructed.

The defensible positioning is therefore precise: **the source already contains an autonomous finite-tensor model of perturbative nonlinear feature-learning trajectories on fixed finite data, with initialization-dependent state and quartic-or-higher retained data objects. It does not establish exact full-trajectory compression, a universal pathwise error guarantee, or cost-free retained kernels.** The verified errors narrow or repair particular claims; they do not erase that substantive construction.
