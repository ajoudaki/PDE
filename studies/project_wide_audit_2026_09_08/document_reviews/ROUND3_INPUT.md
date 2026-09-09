# Deep nonlinear learning: a reconciled research map

8 September 2026. Working consolidation; final document review pending.

## 1. The question the project is really asking

Can the actual training of a deep, genuinely nonlinear, feature-learning network be understood as a discretization of a uniquely defined, restartable population evolution—and can that evolution explain both successful optimization and the representations selected by training?

For the principal dense model, the aim is not merely to replace a finite network by another formal equation. It is to prove that independent Gaussian initialized networks, with every parameter block trained at the specified feature-learning rates, converge jointly as hidden width tends to infinity and the gradient-descent step tends to zero. The comparison should hold uniformly on each prescribed finite physical-time interval. It should identify predictions, loss, hidden representations, their motion, both directions of reused matrices, and the genuine parameter-gradient kernel blocks. The activation must remain nonlinear on the distributions actually encountered, and hidden motion must survive the limit.

There are then three additional questions, none automatically answered by the first:

1. **Optimization:** does the identified population loss approach the appropriate minimum, without assuming the desired convergence of the weights? For realizable labels, does it approach zero?
2. **Further limits:** can fixed depth and a fixed dataset be replaced by a controlled continuous-depth architecture and an input-population theory?
3. **Generalization:** what properties of the learned input-to-feature map explain risk on unseen inputs? Uniqueness of a training trajectory is not itself such an explanation.

The scientific constraint is essential. Orthogonalizing or whitening the data, freezing hidden layers, imposing a coherent finite-type or low-rank initialization, dividing the optimizer by the kernel, or suppressing effective nonlinearity can make a different problem easier without answering this one. Such constructions can be informative benchmarks, but are not the main recommendation. Normalized correlated inputs, ordinary Gaussian initialization, the prescribed optimizer, and quantitatively meaningful nonlinear feature learning remain the intended setting.

**Main assessment.** The project is not a uniformly failed campaign. It has substantial exact calculus, identified local and special global limits, finite-network optimization, and precise representation obstructions. However, several previously accepted negative claims need qualification, and some positive statements have unclosed imported-proof audit dependencies. The central unresolved mathematical issue is control of the response created by repeated use of trained random matrices, sufficiently strong for global continuation and identification. The evidence does not establish that ordinary nonorthogonal data or opposite labels make the desired population limit impossible.

## 2. What this audit does—and does not certify

All 36 requested task identities have been resolved; the exact IDs, hosts and saved-project metadata are in [TASK_INDEX.md](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/TASK_INDEX.md). Six initial fresh isolated source auditors worked on disjoint mathematical groups. They read principal persisted proofs, checked important calculations, traced corrections and recorded their actual read coverage. The coordinator read their reports in full, independently checked the main local continuation and clipping arguments, and reconciled contradictions. Two focused follow-ups and two additional sole-source/special-variant audits address disputed estimates and coverage omissions. No new experiments, old-task resumptions, commits, branch changes or source migrations were performed.

This is a mathematical consolidation, not a machine-checked proof of every result in the repository. Three evidence levels must remain visible:

- **Checked argument:** the operative proof was inspected and its conclusion is supported at its stated scope; ordinary classical dependencies may remain stated explicitly.
- **Dependency-qualified result:** the source contains a proof of the stated result and its internal argument was inspected, but an imported theorem's complete proof or a coefficient-generation dependency has not been fully certified here. This is not the same as a mathematically conditional theorem, and it is not a counterexample to the result.
- **Unclosed/corrected claim:** a concrete proof obligation remains, a displayed estimate is false, or only a conditional/formal/computational statement has been established. Historical PASS labels do not erase these distinctions.

The six source reports provide proof skeletons, precise assumptions, original line links and hashes: [MFP calculus](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/MFP_CALCULUS.md), [Stieltjes/quadratic](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/STIELTJES_QUADRATIC.md), [linear/representation](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/LINEAR_AND_REPRESENTATION.md), [older nonlinear/ResNet/RMS](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/OLD_NONLINEAR_RESNET_RMS.md), [primary literature](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/PRIMARY_LITERATURE.md), and [recent global limits](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/GLOBAL_NONLINEAR_FRONTIER.md). The coordinator's [continuation audit](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/ROOT_CONTINUATION_AND_OPERATOR.md) and [elementary logical bridges](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/LOGICAL_BRIDGES_AND_SCIENTIFIC_SCOPE.md) are additional supporting records.

The earlier [four-task master](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/CONSOLIDATED_RESULTS.md) was read completely and is preserved unchanged as a historical consolidation. Its recovered source archive is valuable, but neither the archive nor its review counts prove chronological completeness. A further 127 historical Markdown files from the destination arctangent continuation have been preserved unchanged under [sources/arctan_destination](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/sources/README.md), with a [hash manifest](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/sources/ARCTAN_DESTINATION_SHA256.txt). Invalid drafts are preserved for provenance, not promoted.

**History-access qualification.** Local task histories were inspected for substantive older amendments, not every conversational/tool line. Several older PDE-2 histories are private to another Unix account; metadata and many earlier exports are available, but a new app request for an older remote history has not returned. Identical-looking paths across hosts are not evidence of identical versions. Thus “36 identities resolved” must not be read as “36 complete histories exhaustively audited.” The final task map below states where attribution or history remains incomplete.

## 3. Contracts that prevent false comparisons

Throughout this report, $L$ counts hidden layers, $m$ samples, $d$ input dimension and $n$ hidden width. Unless stated otherwise, $L,m,d$ are separately fixed before width tends to infinity. Define $G_{ab}=x_a^Tx_b/d$; normalized inputs have $G_{aa}=1$. A singular $G$ is allowed in several positive theorems. Pairwise separation does not imply that $G$ is invertible.

GF denotes gradient flow; GD denotes the actual discrete gradient descent specified by each source. A finite vector's RMS norm is $\|v\|_2/\sqrt n$. The notation $W_2$ for laws means quadratic Wasserstein distance, with the stated Euclidean or uniform-path metric; it is unrelated to the hidden matrix $W^{(2)}$. For a finite parameter block with mobility $D_\ell$, its raw learning-metric kernel is $K^{(\ell)}_{ab}=(\nabla_{\theta_\ell}f_a)^TD_\ell\nabla_{\theta_\ell}f_b$, and the total kernel is the sum over trained blocks. Loss normalization supplies the separate residual multiplier.

In the modern small-readout model, the first preactivations have order-one Gaussian variance, middle entries $W^{(\ell)}_{ij}$ have variance $1/n$, and

\[
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi^{(\ell)}(z_a^{(\ell)}),\qquad
f_a=\frac{(W^{(L+1)})^Th_a^{(L)}}n.
\]

The **stored** readout coordinates initially have variance $n^{-2}$, so the population readout is zero. This is different from an order-one Gaussian stored readout whose averaged prediction also tends to zero. Those two initial predictions can agree while backward fields and training differ.

For first raw weights with $z_a^{(1)}=W^{(1)}x_a/\sqrt d$, the usual normalized Euclidean mobilities are $n\kappa_1,\kappa_2,\ldots,\kappa_L,n\kappa_{L+1}$. In the alternative first-weight convention $z_a^{(1)}=V^{(1)}x_a$, the first mobility is $n\kappa_1/d$. The exact step and the loss normalization belong to each theorem: many special results use $\eta_n=n^{-2}$; the broad local result permits every deterministic $\eta_n\to0$. Sum, half-sum and mean squared losses differ by a physical-time factor.

Finite matrix transpose is $^{T}$; the population adjoint is $^{*}$. Different hidden layers have separate neuron populations. A fixed number of population fields/operators need not mean finitely many scalar coordinates. No statement here identifies neurons across layers or claims operator-norm convergence between spaces of different widths.

The essential hierarchy is:

| Level | What is established | What still does not follow |
|---|---|---|
| Formal initialization jets | Exact finite-order derivatives and their annealed limits | A positive-time trajectory or an exchange of differentiation and limits |
| Fixed-program width limit | Joint empirical averages for a fixed finite number of matrix calls/updates | A width-dependent number of updates or a GF limit |
| Local joint limit | A positive width-independent interval and an identified population flow | Restart beyond its controlled interval |
| Global compact-time joint limit | The conclusion on every fixed finite physical horizon | Uniform approximation on all time, or at a prescribed growing $T_n$ |
| Optimization | Loss tends to its specified target | Width convergence of parameter endpoints or generalization |
| Generalization | Risk/representation control for unseen data | Not supplied by training loss or an equation alone |

For nontriviality, distinguish nonzero initial hidden derivatives, actual finite-time hidden displacement, persistent activation nonaffinity, a changing kernel, and separation from a linear or fixed-kernel predictor. They are not interchangeable. A deep linear model can move its hidden Gram. An initial tangent approximation agrees with an initial derivative even in a nonlazy model.

## 4. MFP: a useful calculus, not yet a general continuous-time compiler

The durable contribution of Mean Field Peeling is a typed way to transform initialization derivatives and finite training programs into explicit Gaussian expectations while preserving reused-matrix dependence. Its correct primitive is not “every new matrix output is independent Gaussian.” A new output equals the response forced by earlier uses, plus unexplored Gaussian randomness. The empirical-average law must be established jointly after reuse.

For a concrete finite-width example, let $W_{ij}$ be independent $N(0,1/n)$ variables, put $y=W\mathbf1$, and apply a smooth $g$ whose value and derivative have polynomial growth. Set $P=I-\mathbf1\mathbf1^T/n$ and $a_n=n^{-1}\sum_i y_i g(y_i)$. Gaussian row conditioning gives
\[
\mathbb E[W^Tg(y)\mid y]=a_n\mathbf1,\qquad
\operatorname{Cov}(W^Tg(y)\mid y)=\frac{\|g(y)\|_2^2}{n}P.
\]
Indeed $W=y\mathbf1^T/n+\widetilde W P$, with $\widetilde W$ an independent matrix of the same Gaussian law. Here $a_n$ is random, not already an expectation. Since the $y_i$ are independent standard Gaussians, $a_n\to\mathbb E[Gg(G)]=\mathbb E g'(G)$ by the law of large numbers and Gaussian integration by parts. Only this limiting coefficient is deterministic. Applying $W$ again requires remembering the transpose call. Keeping only forward covariances loses the response forced by previous uses; the joint empirical-average limit after reuse is the substantive obligation.

### 4.1 Checked machinery and its quantifiers

The earliest backward-kernel execution correctly peels from the top, retains lower-layer boundary factors and splits index-equality patterns before using row independence. For three hidden layers, its leading annealed first backward kernel is the product of the three derivative covariances. However, it assumes weighted covariance replacements and does not complete the variance estimate needed for concentration. Its frozen-covariance branch count is not an exact finite-width bias expansion. [Primary execution](/home/amir/Codes/PDE/studies/mean_field_peeling/MUP_TRAINING_CASE_STUDY.md:605).

The later fixed-depth/fixed-batch cubic recursion handles arbitrary positive-semidefinite input Grams and the complete forward/reverse response structure. Its compact state has $O(m^2)$ entries per layer at that particular order. The universal identity, for $D=\nabla f\cdot\nabla$ in the chosen metric, is

\[
D^3f=2\nabla^3f[\nabla f,\nabla f,\nabla f]
       +4\|\nabla^2f\,\nabla f\|^2.
\]

It is a named-observable compiler, not a depth/order-independent closure for every possible head. Its probability passage imports a tensor-program theorem; the shared external-proof qualification in §11 applies. [Full recurrence](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/depth/DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md).

The one-sample order-five specialization uses six sweeps with 29 coordinate types plus depth caches, under unit initialized forward Grams. Its finite-order recurrence architecture is supported; the audit did not independently rederive every coefficient in the large flattened transition tables. The first raw-square activation without normalization does not satisfy that unit-Gram hypothesis. [Order-five manuscript](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/depth_order5_scalar/ARBITRARY_DEPTH_B1_ORDER5_SCALAR_RECURRENCE.md).

The strongest locally self-contained finite-step package proves width identification for one sample, every separately fixed depth $L$ and update count $N$, with linear-growth activation, bounded first two derivatives, and the stated Gaussian initialization/normalization. A remainder theorem assumes bounded derivatives through order 12. Its proof uses globally interlaced two-sided Gaussian conditioning, a finite-history rank argument at fixed nonzero step, stopped high-moment coupling, and a polynomial initial-energy bound to remove stopping. It does not assume finite coordinates are iid after reuse. [Probability proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/WIDTH_DEPTH_TIME.md).

The singular-covariance compiler differentiates expectations through Price's identity after adding $\varepsilon I$, then removes that regularization under a Gaussian envelope. It does not differentiate a singular covariance square root. Here $F_{k,L}(h)$ denotes the width-limit expected output after the separately fixed integer $k$ feature-ascent Euler updates of step $h$, not physical square-loss GD. The activation is normalized by $\mathbb E\phi(G)^2=1$. In the fixed population learning metric, writing $F$ for the output functional and $g=\nabla F$ at initialization, define $J_{\phi,L}=\nabla^3F[g,g,g]+4\|\nabla^2F\,g\|^2$; this is not $D^3F$, whose cubic term has coefficient two. Under the order-12 derivative/remainder assumptions above, the fixed-operator repair establishes, for $|h|\le1/2$,

\[
F_{k,L}(2h)-F_{2k,L}(h)
=-\frac{k(2k-1)}2J_{\phi,L}h^3+R_{k,L}(h),\qquad
|R_{k,L}(h)|\le B_\phi^{E_{L,2k}}|h|^5.
\]

The exponent is explicitly finite but depends strongly on depth and step count. This repairs earlier finite-horizon factorization/identification gaps, not the uniform mesh-refinement problem. At one hidden layer a sharper $C_\phi k^4|h|^5$ bound is proved on $|h|\le c_\phi/k$, and the power four is sharp even for the identity activation. [Main package](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/PROOF.md), [one-layer uniform proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/UNIFORM_L1.md).

### 4.2 What the failed compiler routes actually exclude

A literal fifth Euler coefficient is polynomial of degree at most four in the paired step count after its leading cancellation. A super-polynomial **effective remainder on an interval** is a different claim, involving higher orders. Quadratic activations give a positive-coefficient Gaussian-moment obstruction to the proposed uniform remainder family; this does not apply to bounded-slope activations merely by analogy.

The later bounded-slope ladder and super-$k^5$ manuscripts use a false deterministic activation-stability estimate. Take $\psi(x)=x+\arctan x$, perturb it by $n^{-1/2}$, and choose

\[
z^{(1)}_0=0,\quad W^{(3)}_0=\sqrt n\,e_1,\quad
W^{(2)}_0=e_1\mathbf1^T/\sqrt n.
\]

All relevant RMS/operator norms are bounded. For a common feature-time Euler step of $\dot z^{(1)}=n\nabla_{z^{(1)}}f$, the reference update is $4h\mathbf1$ and the perturbed update is $3h\mathbf1$. Their RMS difference is $|h|$, not $O(n^{-1/2})$ at fixed $h$. For physical square-loss GD with a fixed nonzero target, the residual factors tend to the same nonzero constant, so the order-$h$ discrepancy persists. This physical-loss conclusion is not asserted for target zero. This disproves the deterministic energy-ball estimate used by those proofs, not their final annealed counterexample theorem or a Gaussian-typical statement. An additional probabilistic stability argument is needed before those counterexamples can be accepted. [Exact objection](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/MFP_CALCULUS.md:323).

The newer causal-flow and renormalized-causal Gaussian calculi retain exact increment identities and useful conditional sewing/Picard lemmas. Their general dynamic response-tail, low-influence, source-compression stability and restart premises remain open. A finite dictionary at fixed tolerance is not a tolerance-uniform autonomous approximation theorem. These languages are research machinery, not an already established general nonlinear GF compiler.

## 5. Stieltjes, Taylor divergence and the quadratic boundary

### 5.1 What was disproved, and what remains open

The canonical Stieltjes model has two hidden layers, one sample, raw-square activations, independent standard Gaussian raw weights/readout and the unit block metric. The physical-loss no-go specialization uses target $y=1$ and limiting initial output zero. Its initial output kernel is $111=27+36+48$. The formal feature series is defined by fixed-order annealed limits, not by an already identified positive-time flow. If $S=F^{-1}$ formally, the candidate moments are defined by

\[
K(y)=F'(S(y)),\qquad
\frac{K(\sqrt x)-111}{x}=\sum_{r\ge0}(-1)^r\mu_r x^r.
\]

For this **specific** model, retained exact output coefficients reach order 17, giving eight moments and strictly positive ordinary/shifted Hankel gates through size four. The first-hidden norm has a ninth moment because its exact Ward identity is $Q_1'=8F$; that does not provide output order 19. The source audit checked 322 retained rational minor entries, including repeated entries, against the moment tables. It did not regenerate the upstream coefficients. All-order positivity, determinacy and identification with actual neural dynamics remain open. [Canonical contract](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/PROOF_CONTRACT.md), [order-17 results](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/canonical_high_order/RESULTS.md).

There are scoped counterexamples and negative witnesses in other models, with differing verification levels:

| Variant | Result or evidence | Why it does not settle canonical unit-metric QQ |
|---|---|---|
| Block metric $D_a+\alpha D_u+D_W$ | A shifted $3\times3$ Hankel determinant is negative for $0<\alpha\le1/100$, with every block trained | The canonical metric has $\alpha=1$ |
| One hidden layer, raw square | Exact two-dimensional characteristic reduction transfers a negative Stieltjes witness | Different depth |
| Two hidden layers, raw cubic | Exact order-nine moments have a negative shifted $2\times2$ determinant | Different activation |
| Inner quadratic / outer identity | Retained order-17 table has a negative shifted $4\times4$ determinant | Different architecture; coefficient-generation qualification remains |
| Sine variants | Retained high-precision negative signs | No independent rigorous transcendental enclosure was audited here |

The block-metric proof is particularly informative: it first computes a frozen-bottom two-variable polynomial recursion, then derives the positive-$\alpha$ chronological Gaussian recurrence and an exact determinant polynomial whose sign persists on a nonzero interval. Thus the negative is not merely an artifact of freezing a layer. It disproves an activation/metric-universal Stieltjes law, not operator-valued population evolution. [Full metric proof](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/BLOCK_METRIC_RESOLUTION.md), [all-block extension](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/POSITIVE_ALPHA_JET_DERIVATION.md).

A further retained positive prefix concerns **three hidden layers with raw-square activations**: the initial output kernel is $14175$, and coefficients through output order 13 give six moments with positive ordinary and shifted $3\times3$ Hankel gates. This is neither the raw-cubic negative above nor an all-order result. The source audit checked the retained rational certificates, not a fresh generation of every coefficient.

The generic multi-input noncommutative Stieltjes proposal was not completed: the transform from raw source-word jets to the proposed signed moment sequence, mixed-word conventions and causal reconstruction were still undefined. Positive finite word matrices alone would not fill those omissions. This is not an established multi-input closure theorem.

### 5.2 Zero Taylor radius is a real but limited obstruction

The formal quadratic feature coefficients have a factorial lower bound, obtained by retaining a positive polynomial branch and taking Gaussian moments. Their Taylor radius is zero; for the nonzero target $y=1$ and $F(0)=0$, formal physical-loss coefficients inherit that divergence through the residual clock, whose initial derivative is nonzero. This deduction excludes a zero initial residual, for which the physical solution can instead be stationary. Positive Taylor truncations coupled to that clock form a non-Cauchy family of continuous loss curves: their subtarget hitting times tend to zero. This rigorously excludes the specified width-first positive-Taylor/positive-compiler approximation families. It does not identify the true network trace, rule out signed resummation, or rule out every smooth ODE/IDE.

Here is a complete reason the stronger ODE inference is false. For standard Gaussian $G$,

\[
g(t)=\mathbb E(1+t^2G^2)^{-1}
\]

is $C^\infty$: every derivative of $r(u)=(1+u^2)^{-1}$ is bounded on the real line, and Gaussian moments justify differentiation. Its even Taylor coefficients are $(-1)^k(2k-1)!!$, so the Taylor radius is zero. Yet

\[
\dot s=1,\qquad \dot q=g'(s),\qquad (s(0),q(0))=(0,1)
\]

is a smooth nonsingular autonomous two-dimensional ODE with unique solution $(t,g(t))$. This is not a proposed neural closure; it disproves the logical implication “zero radius means no smooth ODE.” Analytic vector fields with analytic readouts obey a different local theorem. Formal jets also need a trajectory-identification bridge before they establish actual trajectory regularity. [Formal no-go proof](/home/amir/Codes/PDE/studies/quadratic_nonclosure/approximate_single_source_conjecture_resolution.md), [positive-compiler boundaries](/home/amir/Codes/PDE/studies/quadratic_nonclosure/adversarial_audit_report.md).

The project also explored initialization-jet/Borel transforms and alternative-basis reconstruction. These routes remain conditional on transform, growth and trajectory-identification assumptions; they supply no new unconditional global theorem in the recovered record. Their full Borel dependencies were not re-audited here. This is the disposition of PDE task 2, not a claim that resummation is impossible.

### 5.3 Actual quadratic dynamics: the strongest claim needs another check

The tagged-site DMFT comparison is a valid deduction from its assumed continuous Gaussian forcing, independence, positive memory and dissipation equations. A large positive initial readout event forces cooperative finite-time growth under those assumptions. But the tagged law was not derived for the canonical trained network, and selecting an instantaneous-fitting step needs an additional relaxed-selection rule. This is a conditional effective-model contradiction, not a proved canonical training limit.

The 3,342-line covariant-Schur manuscript claims that actual Gaussian finite networks acquire a fixed output increment by time $O(1/\sqrt{\log n})$. With a width-independent positive probability this would exclude compact-time uniform convergence from initialization to a continuous output, even with infinite-dimensional state. Two source auditors read the manuscript fully. Its exact column decomposition and final implication are supported, but the adaptive difference-score and differentiated finite-word bridge remains unproved in the supplied argument. The focused recheck also finds a literal uniform row bound false on its printed tangent domain: choosing a tangent row parallel to an initial Gaussian row gives bounded printed graph norm but an initial directional response of order $\sqrt n$; the claimed polylogarithmic row control cannot follow. Restricting to a special residual-generated subspace might exclude this witness, but that restriction and its preservation through the derivative catalogue must be proved. This is a proof gap, not a canonical-trajectory counterexample. **Do not use the claimed initial layer as a settled canonical impossibility theorem.** [Primary manuscript](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md), [completed focused recheck](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/COVARIANT_SCHUR_FOCUSED_RECHECK.md).

The extremely fine-mesh full-network GD initial-layer argument depends on that finite-GF theorem and inherits this qualification. Separately, the all-vanishing-mesh initial-layer proof for the **frozen-bottom auxiliary model** has a direct positive-tail-block/Riccati argument; it does not cover every diagonal in the fully trained model. The width-first fixed-step quadratic output obstruction also has a different, positive-polynomial proof. These three statements must not be merged.

Hard ReLU provides another distinction. A fixed-width positive-probability attracting-gate example defeats an ordinary GF with a prescribed pointwise derivative convention at zero. It does not prove a width-uniform macroscopic obstruction. Conversely, actual Euler predictor/loss paths are locally tight in $C([0,T_0])$ for **every** vanishing mesh, with $T_0=1/(384\cdot6^4)$, by deterministic RMS/operator growth and increment bounds. Uniqueness and a full generalized state limit are unproved. Binary gate occupation has second moment $\lambda$, not $\lambda^2$; averaged slopes can therefore lose kernel information. [ReLU and quadratic mesh proofs](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_loss_mesh_resolution/FINAL_X2_RELU_MESH_VERDICT.md).

## 6. Shallow and deep-linear benchmarks: what operators buy

For one hidden layer, a neuron can be represented by its first-layer weight and readout, and a law of these parameters evolves by a characteristic/transport equation coupled through finitely many residuals. No trainable inter-hidden-layer operator is required. The law itself is infinite-dimensional, and its parameter domain need not be one-dimensional. Unbounded polynomial activations can still create nonintegrable characteristic poles; “shallow” is not automatic global well-posedness for every activation/initialization.

For the project's two-hidden-layer **linear**, one-sample model, a conserved matrix combination yields a spectral integral differential equation. A rooted $2\times2$ spectral measure converges to an explicit measure with a continuous Marchenko–Pastur-derived part and an atom of mass $3/4$ at $-1/2$. This gives a global physical-GF prediction/loss description. The original manuscript does not separately state the later exact-GD bundle. The classical spectral inputs and their scope are recorded in the linear audit.

The strongest fully assembled deep-linear theorem recovered here is **three hidden layers, one sample**, not arbitrary depth and arbitrary data. In its own normalization,

\[
f_n=a^TRBx,
\]

with every entry of $a,x,B,R$ initially independent (N(0,1/n)). A block-cyclic operator $C=C_0+Q$ packages the network, and the limiting physical flow is

\[
\dot Q=2\eta\left(y-\frac14\operatorname{Tr}C^4\right)(C^*)^3,
\qquad f=\frac14\operatorname{Tr}C^4,
\qquad K=\|C^3\|_{\mathrm{HS}}^2.
\]

The initialized source $C_0$ has an explicit colored Fock-space realization; $Q$ is trace class. The rank structure gives a trace-norm action bound $\|Q(t)\|_1\le2|y|\sqrt{\eta t}$, global existence and uniqueness. Fixed-word Wick convergence, finite-rank Gram comparisons and factorial Picard tails identify the finite-width flow. Exact raw GD is Euler for **$Q$ with its residual recomputed from $Q$**, not Euler for an independently updated residual equation. Every normalized physical mesh tending to zero is permitted. Predictions, loss, total kernel and specified rooted-word observables converge on compact time intervals; the population fits the scalar label. This is not the entire nonlinear hidden-path measurement contract. [Complete theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md).

The arbitrary-depth rooted-path candidate has internally well-posed operator dynamics, but the actual width-identification bridge beyond the completed three-hidden-layer case is conditional in the recovered source. No arbitrary-dataset theorem is extracted from an aggregate multihead loss. The related external deep-linear paper's broader-depth section is explicitly formal; it does not fill that gap.

Two valid representation negatives coexist with this positive operator theorem:

- No state-universal finite scalar polynomial/appropriate analytic closure built from a width-independent finite family of bounded-degree current tensor contractions.
- No fixed finite-order local PDE with the corresponding bounded-contraction encoder and finite-jet readout on the stated full open state sets.

Repeated derivatives generate connected noncommutative contraction paths of unbounded degree. Products of a fixed alphabet produce disconnected unions, not all new connected types; spatial differentiation changes coefficient functions, not that alphabet. The analytic version requires a full neighborhood of the zero-state jets. The negatives do not exclude infinite-dimensional current operators, arbitrary encodings, approximations, or a curve fitted to one orbit. A translation PDE initialized with the entire future output profile is formally possible but preloads the answer. [PDE boundary proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_pde_no_go/PDE_CLOSURE_BOUNDARY.md).

The mathematical lesson is representational, not pessimistic: matrix reuse can require an infinite-dimensional current action even when a globally stable population evolution exists. Separate source spectra generally lose the mixed noncommutative words needed by training.

### 6.1 Useful partial-quadratic reductions

The inner-square/outer-identity and inner-identity/outer-square models retain exact finite algebra even though no canonical quadratic population theorem results. Use the stored readout $W^{(3)}$, hidden matrix $W^{(2)}$ with entries of order $n^{-1/2}$, and feature time, without a residual inside the displayed updates. For inner square/outer identity,
\[
(W^{(3)})'=z^{(2)},\qquad
(h^{(1)})'=4h^{(1)}\odot(W^{(2)})^TW^{(3)},\qquad
(W^{(2)})'=\frac{W^{(3)}(h^{(1)})^T}{n}.
\]
For inner identity/outer square,
\[
(W^{(3)})'=(z^{(2)})^2,\qquad
(h^{(1)})'=2(W^{(2)})^T(W^{(3)}\odot z^{(2)}),\qquad
(W^{(2)})'=\frac{2(W^{(3)}\odot z^{(2)})(h^{(1)})^T}{n}.
\]
The respective block-Gram constructions have commutator evolution and conserved spectral information. But an explicit same-spectrum/same-output example changes the weighted contraction from $1/3$ to $7/9$, changing the kernel. Thus spectral eigenvalues alone discard necessary coordinate orientation. For both-square activations, the exact row/column balance identities survive but that particular common-Gram commutator construction does not. Neither a formal operator representation nor the partial spectral invariant proves real-axis population existence. [Full finite-algebra audit](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/LINEAR_AND_REPRESENTATION.md:177).

## 7. Nonlinear population limits and finite optimization

### 7.1 Broad local theorem and the finite-GF corollary

For every fixed $L\ge2,m,d$, the general theorem permits layer-dependent $C^{1,1}$ activations with bounded derivative, including linearly growing activations; arbitrary fixed bounded data and real labels; Gaussian middle matrices; centered subGaussian first weights; and any fixed iid subGaussian stored readout, including noncentered or order-one Gaussian readout. It also permits initial perturbations vanishing in the stated RMS/operator distance, so every Gaussian stored-readout scale $n^{-\beta}$, $\beta>0$, is covered. The rates are those in §3, with nonnegative fixed $\kappa_\ell$.

For averaged square loss, there is $T_*>0$ depending on the fixed depth and activation, initialization, rate, input and label bounds, but not on the input Gram's minimum eigenvalue or on $m,d$ under those bounds. For **every deterministic** $\eta_n\to0$, exact GD converges jointly to a unique autonomous population flow on $[0,T_*]$. The conclusions are uniform predictions/loss/all kernel blocks, same-layer joint sample hidden-path laws in $W_2$ for the uniform path norm, integrated squared hidden speeds, and fixed typed action/adjoint probes with the specified bounded-product restrictions. This is not a blanket claim of every uniform-time velocity-law observable. The existence theorem allows duplicate samples, affine activations and zero rates, so it does not itself promise nonlazy behavior.

A separate $L=2$ activity corollary assumes Gaussian first weights, positive scales/rates, zero limiting readout, nonzero labels, pairwise nonparallel normalized inputs, and nonaffine activations. It proves positive leading hidden displacements of order $t^2$, speeds of order $t$, positive/changing kernel blocks and positive activation affine-fit error on a smaller interval. It does not supply all-depth persistent activity. The general separable-loss extension requires $C^1$ losses with locally Lipschitz derivatives and common bounds on bounded prediction intervals. [Main proof](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/GENERALIZE_PRIMARY/GENERAL_POPULATION_GF_PROOF.md), [complete response proof](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/GENERALIZE_PRIMARY/GENERAL_DEPTH_RESPONSE_PROOF.md).

The essential new estimate controls expected response coefficients and reference backward tails uniformly over the time mesh. Each new past response carries its step and sample weight. Weighted time sums, not maxima over growing Gaussian histories, control the exponential estimates. A one-sided comparison then has the form

\[
\|F(\theta)-F(\theta_{\rm ref})\|
\le C(1+R)d(\theta,\theta_{\rm ref})+Ce^{-cR^2}.
\]

Only the reference requires the tail bound. Compare actual GD to a fixed coarse oracle first, pass width at fixed oracle and cutoff, then refine the oracle and remove the cutoff. This proves a joint limit without applying a fixed-program theorem to a growing program. The main and response manuscripts were read completely by both the coordinator and source auditor. Their rank-free fixed-program import remains dependency-qualified as explained in §11; the argument is not thereby declared false.

**The previously omitted finite-width-GF clause follows in exactly these observable topologies.** Here is the complete diagonal argument for square loss. At fixed $n$, write the finite flow as $\dot\theta=-D_n\nabla\mathcal E_n$, with its fixed nonnegative diagonal mobility. Local Lipschitzness holds in finite dimensions and

\[
\int_0^T\|\dot\theta\|^2dt
\le\|D_n\|\mathcal E_n(0).
\]

Cauchy–Schwarz bounds the path length on finite intervals, giving a finite endpoint and global continuation at this fixed width. Euler converges uniformly to this flow as its step tends to zero: take a compact tube around the flow, use its finite local Lipschitz bound and the stopped Euler recurrence, and choose the step sufficiently small to stay in the tube. Piecewise parameter derivatives converge in essential supremum; the finite network is $C^1$, so recomputed hidden derivatives converge in $L^2$ time. Kernels and each finite probe list converge by continuity. Pairing the same neurons bounds the **square** of the hidden-path $W_2$ distance by their averaged squared uniform-path difference.

For a bounded sum $d_n$ of these observable distances, fixed-width convergence is almost sure in the initialization, hence in probability. Choose a **deterministic** $0<\widehat\eta_n<1/n$ such that

\[
\mathbb P\{d_n({\rm GD}_{n,\widehat\eta_n},{\rm GF}_n)>1/n\}<1/n.
\]

The theorem applies to this sequence because it applies to every deterministic vanishing sequence. The triangle inequality proves finite-GF convergence to the same population object. No width-uniform Euler rate is needed. This corollary inherits the population theorem's dependency qualification; it does not enlarge the observable class, prove global population continuation, or give same-neuron coupling of two arbitrary step sequences. For arbitrary separable losses the preliminary short-time ball gives an analogous high-probability stopped statement, not global finite GF for every realization.

### 7.2 Global theorems: exact scope and audit grade

“Full modern bundle” below means the source's predictions/loss, all raw kernel blocks, typed current actions and adjoints, same-layer sample path $W_2$, and stated velocity/energy measurements. It is stronger than predictions alone, but is not all unbounded products or cross-width operator-norm convergence. In each two-sample row $\rho=G_{12}$; three-sample separation conditions apply only to distinct pairs $a<b$, never to diagonal entries. “All binary labels” means every vector in $\{-1,+1\}^m$. In the modern two/three-sample rows, use small Gaussian stored readout, all layers trained, half-sum square loss and raw step $n^{-2}$; the one-sample rows use full square loss. “Internal” means the principal proof and its own nonclassic Gaussian/limit machinery were fully read without a decisive gap found. “Extension-qualified” means the new proof was fully read but its older multi-file dependency chain was not all re-audited.

| Family | Data, activation and step | Established source conclusion / current audit |
|---|---|---|
| L2 pure atan baseline | $L=2,m=1,x=y=1$; $\phi=\arctan$; $\eta_n\sqrt n\to0$ | Global population/finite-GF/exact-GD bundle; short-time strict activity. **Internal** narrower Gaussian proof; no general all-label fitting theorem extracted |
| Broad L2 class | $L=2$, one or finitely many orthogonal normalized samples, arbitrary real labels; first activation $C^{1,1}$ with bounded derivative, second additionally bounded; vanishing-sup or bounded iid stored readout plus vanishing-sup perturbation; $\eta_n\sqrt n\to0$ | Global full bundle. **Dependency-qualified** fixed-program import. Nonlinearity/activity needs extra assumptions; constant zero second activation prevents any universal fitting statement |
| Affine-first L2 extension | Same second activation/readout class, arbitrary fixed finite input configurations including singular Grams, arbitrary real labels; every $\eta_n\to0$ | Global full bundle. **Dependency-qualified** as in the broad L2 row; the first layer is affine and fails the project's all-hidden-nonlinearity requirement |
| Fixed bounded activation, all depths | Every fixed $L\ge3$, $m=1,x=y=1$; $1+\arctan(z)/10$, independent of $L,T,n$; step $n^{-2}$ | Global full bundle and fitting; every hidden preactivation/activation speed positive at each $t>0$, persistent nonaffinity on every compact horizon. **Internal** |
| Two-sample offset perturbation | $L=3,m=2$, $\rho\le1-\delta$, $0<\delta\le2$, including antipodes, all binary labels; $1+z+e\arctan z$, one sufficiently small $e_\delta>0$ for that separation class | Global full bundle, exponential fitting and persistent absolute nonaffinity. **Extension-qualified** |
| Two-sample odd perturbation | $L=3,m=2$, $\lvert\rho\rvert\le1-\delta$, $0<\delta\le1$, all binary labels; $az+e\arctan z$, $1/2\le a\le1$, $0<e\le c_{\rm poly}\delta^2$ | Global full bundle and fitting. Includes a small exact odd convex mixture and a separately Gaussian-normalized version. **Extension-qualified** |
| Two-sample all-depth extension | Every fixed $L\ge3$, $m=2$, $\lvert\rho\rvert\le1-\delta$, $0<\delta\le1$, all binary labels; $az+e\arctan z$, $1/2\le a\le1$, $0<e\le c_L\delta^{p_L}$ | Global full bundle, fitting, absolute nonaffinity. $p_3=31/8,p_4=9/2,p_5=21/4,p_L=9-43/[2(L+1)]$ for $L\ge6$; the previous row improves the $L=3$ exponent. **Extension-qualified**, coefficient depends on depth |
| Two-sample shape class | $L=3,m=2$, $\lvert\rho\rvert\le1-\delta$, $0<\delta\le1$, all binary labels; $az+e\psi(z)$, $1/2\le a\le1$, $\psi\in C^2$, $\lvert\psi(0)\rvert,\lVert\psi'\rVert_\infty,\lVert\psi''\rVert_\infty\le1$; $0<e\le c_{\rm dyn}\delta^{31/8}$ | Global full bundle and fitting; nonodd/nonmonotone/linear-growth shapes allowed. Persistent nonaffinity requires nonaffine shape and an additional shape-dependent cutoff. **Extension-qualified** |
| Three samples, bounded shape and offset gain | Every fixed $L\ge2$; $G_{ab}\le1-\delta$ for $a<b$, $0<\delta<1$, all binary labels; $a(1+z)+e\psi(z)$, nonconstant $C^2$ shape with $\lVert\psi\rVert_\infty,\lVert\psi'\rVert_\infty,\lVert\psi''\rVert_\infty\le1$ | One $a=a_{\delta,\psi}$ and any fixed $e\in(0,1]$ work at all fixed depths: global full bundle, exponential fitting and persistent absolute nonaffinity. **Internal** |
| Three samples, odd overall gain | Every fixed $L\ge2$; $\lvert G_{ab}\rvert\le1-\delta$ for $a<b$, $0<\delta\le1$, all binary labels; $a_\delta(z+\arctan z)$, $a_\delta=324\pi e\,10^{10}\delta^{-2}$, where $e$ here is Euler's number | Global full bundle, fitting and persistent absolute nonaffinity. **Internal**, with the stated classical Gaussian norm input; not a no-gain result |

Principal sources: [L2 baseline](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/inherited_baselines/L2_ONE_SAMPLE_ARCTAN_GLOBAL_PROOF.md), [broad L2 and affine exception](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/GLOBAL_ACTIVATION_TRANSFORM_EXTENSION.md), [all-depth one-sample proof](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/SHIFTED_ATAN_ALL_DEPTHS/GENERAL_DEPTH_SELF_CONTAINED_PROOF.md), [two-sample offset](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_separated_angle_theorem/PROOF.md), [exponent-two refinement](/home/amir/Codes/PDE/studies/mean_field_peeling/odd_activation_lower_powers_three_inputs/TWO_INPUT_PROOF.md), [two-sample all-depth proof](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth56/PROOF.md), [shape extension](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_activation_design/PROOF.md), [three-sample all-depth shape proof](/home/amir/Codes/PDE/studies/mean_field_peeling/activation_class_all_depths/MANUSCRIPT.md), [odd-gain proof](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_gain_all_depths/PROOF.md).

The one-sample bounded proof explains a real success mechanism. Since $5/6\le\phi\le7/6$, the feature-gradient kernel is at least $25/36$. Explicit response bounds close through feature time $3/2$; the first hit $f=1$ occurs by $36/25<3/2$. The physical clock $dt/ds=[2(1-f)]^{-1}$ diverges at the hit, so that finite controlled feature interval covers all physical time. Population loss is at most $e^{-25t/9}$. The raw-GD coordinate transform is handled with its accumulated defect, not declared exact Euler. Persistent activity uses surviving innovations and nonaffinity on the actual marginal support.

The three-sample gain proofs use a different mechanism. A positive initialized nonlinear/augmented feature Gram and a huge gain make the total controlled fitting path short. To define the shape constant, choose an integer $r_\psi\ge1$ with $J_\psi=\inf_{b,c}\int_{-r_\psi}^{r_\psi}(\psi(x)-b-cx)^2\,dx>0$, and set $c_\psi=e^{-r_\psi^2/2}J_\psi/\sqrt{2\pi}$. Such an interval exists because a bounded, nonconstant continuous function cannot be affine on every bounded interval. For bounded shapes, $\lambda=\delta^2/16$, $S_0=192/\delta^2$, and

\[
a=\max\{10^{12}(1+S_0),
[2^{36}S_0^2/\sqrt{c_\psi}]^{2/5}\}.
\]

The $3\times3$ augmented Gram estimate is specific to three samples, not arbitrary $m$. The capped hidden contribution is **not** called positive semidefinite: it is bounded as a small possibly nonsymmetric perturbation of the coercive readout block. This preserves residual decay while Gaussian response estimates and the limit bridges close. The raw metric/readout remain unchanged; proof-coordinate normalizations must not be mistaken for a different optimizer.

These gain theorems are mathematically real, but they do not satisfy the user's intended moderate-scale scientific target. If $\phi(z)=az+e\psi(z)$, $\psi$ is 1-Lipschitz and $a>e$, then for every nondegenerate finite-variance $Z$,

\[
\frac{\inf_{b,c}\mathbb E(\phi(Z)-b-cZ)^2}
{\operatorname{Var}(\phi(Z))}
\le\left(\frac e{a-e}\right)^2.
\]

Indeed use affine slope $a$ and intercept $e\mathbb E\psi(Z)$ (plus any fixed activation offset), then $\operatorname{Var}(\psi(Z))\le\operatorname{Var}(Z)$ by the independent-copy variance identity. The pointwise lower slope $a-e$ gives $\operatorname{Var}(\phi(Z))\ge(a-e)^2\operatorname{Var}(Z)$ by the same identity. Thus $e=1$ with enormous $a$ is not substantial relative nonlinearity. The odd-gain theorem instead has equal linear/nonlinear coefficients, so this particular bound does **not** apply to it; its problem is the overall gain and uncontrolled relative nonlinearity at large deep preactivations. Scaling the activation back down is not merely changing physical time. Very small $c_{\rm poly}$ and $c_{\rm dyn}$ are sufficient proof constants, not necessary thresholds.

### 7.3 Important variants and finite-only positives

The earlier order-one-Gaussian-readout $L=2$ arctangent theorem remains separate: it establishes global physical population/finite-GF prediction, total-kernel and loss convergence in its Gaussian-envelope class, not the newer entire raw-GD/path/velocity bundle. Its repaired internal proof uses an auxiliary fixed mesh to establish square-tail uniform integrability before removing readout clipping. The focused follow-up gives a narrower route around the disputed all-moment scalar-feedback import: compare the clipped finite program, on the same arrays, with a program using deterministic population expectations, then use finite $L^2$ stability and the parameter-free tensor-program specialization. A square-tail argument transfers from that companion program. This addresses the law/output/kernel specialization needed here, not the unrestricted scalar-feedback theorem, arbitrary higher-moment observables or $L=3$ continuation. The remaining external-proof scope is recorded in §11. [Original proof](/home/amir/Codes/PDE/studies/mean_field_peeling/nonlinear_activation_operator_ide/ARCTAN_THEOREM_AND_PROOF.md), [completed focused follow-up](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/OLD_NONLINEAR_RESNET_RMS.md:372).

Other recovered variants are retained, not silently swallowed by a more general but weaker row:

- $L=2$, ordinary atan, opposite-label **orthogonal or antipodal** pairs: global population/finite-GF/exact-GD theorem at step $n^{-2}$, unhalved sum loss, with every-positive-time hidden activity and same-population path laws of every fixed finite moment order. Its strict $0<f_1(t)<1$, $f_2(t)=-f_1(t)$ statement is **not** a proved asymptotic fitting assertion. The generic-angle continuation, for every $-1\le\rho<1$, gives global first-layer strong path/velocity compact containment and controlled node-level kinetic measurements along subsequences. It does not identify the second layer, unweighted full kernel, recomputed within-cell kernel, a unique full population flow or equality of the GF/GD limits.
- $L=3$, two **equal-label** samples, every fixed $-1\le\rho<1$: the bounded $1+\arctan z/10$ source and its five proof dependencies were freshly read in full, supporting global population/GF/GD, fitting and persistent activity/nonaffinity. With unhalved sum loss, the symmetric feature clock is $ds/dt=4(1-f_1)$, not the one-sample factor two. The separate $1+\arctan(\sinh z)/10$ transfer has retained historical proof/review evidence but was not fully re-audited in this special-variant check. Neither is generic opposite-label fitting.
- $L=2$, generic interior-angle opposite labels: a compactly supported first derivative and second activation $z+\epsilon\arctan z$ yield global **finite-GF** fitting, bounded accumulated residual, controlled parameters and endpoints on a high-probability Gaussian event. Finite GF exists globally for every finite initialization by its energy estimate, but the fitting claim is on the stated high-probability Gaussian event, not almost surely at each width. A separate strengthening preserves a positive mass of unsaturated first gates forever, on a further high-probability event. It does not prove nonzero velocity forever or a global population theorem. The exact-GD extension lacks recovered complete acceptance evidence and is not promoted here.

The principal retained sources and review versions are in the [special-angle recovery](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/L2_SPECIAL_ANGLES_RECOVERY_AUDIT.md), [same-label recovery](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/L3_BOUNDED_SAME_LABEL_RECOVERY_AUDIT.md), and [mixed finite-GF recovery](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/L2_MIXED_FINITE_GF_RECOVERY_AUDIT.md). The [fresh special-variant audit](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/SPECIAL_NONLINEAR_VARIANTS.md) read ten principal/dependency files completely (7,925 lines), found no substantive gap in the scopes just stated, and records a harmless misplaced-square typo in the same-label nonaffinity expression. This does not certify its separately listed unread transfer or GD extension.

Most importantly, canonical $L=3$, one-sample **pure atan** actual finite GF and exact raw GD with step $n^{-2}$ already fit globally with a width-uniform readout-kernel floor on a high-probability event. Their residuals decay exponentially, total feature time is bounded and finite parameters approach fitting endpoints. Both finite proofs were freshly read in full. Yet the global strong population limit is open. This cleanly demonstrates that successful finite optimization is not the same missing theorem as global population identification. [Finite-GF proof](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/EXPLAIN_PRIMARY/l3-full-resolution-9nbD4z/READOUT_COERCIVITY.md), [exact-GD proof](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/EXPLAIN_PRIMARY/l3-full-resolution-9nbD4z/EXACT_GD_COERCIVITY.md).

The original **$L=3$ arctangent program with order-one Gaussian stored readout** is a different open problem from the tiny-readout theorem below. Its exact autonomous operator algebra retains initial Gaussian actions, both adjoints and the trained rank memories. The persisted moment/cluster and ordered-limit arguments do not establish its global population limit for the nonzero-label feature-learning target. Dynamic cavity and Schur–Volterra formulations identify candidate response estimates, but do not discharge the uniform adaptive-tail and source-comparison bridges. The full source audit retains this algebra and these precise open obligations; it does not transfer either the newer shifted-activation global theorem or the tiny-readout local proof to this initialization. [Original-model correction and audit](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/OLD_NONLINEAR_RESNET_RMS.md:93).

The original **pure-arctangent $L=3$ local theorem** deserves a separate entry, not merely absorption into the broader local class. For one sample $x=y=1$, tiny Gaussian readout and exact raw step $n^{-2}$, its 2,321-line assembled proof internally derives fixed-program Gaussian reuse, singular-query removal, mesh-uniform local response tails, cutoff removal, raw-GD defects and physical-clock comparison. It constructs four autonomous fields/operators, uniquely restartable along the reached local trajectory, and proves the four raw kernel blocks, current actions/adjoints, same-population preactivation path laws in $W_2(C([0,T_0]))$, velocity measurements and same-width GF/GD agreement on an explicit positive $T_0$. Every hidden layer moves at order $t^2$, the total kernel changes at order $t^2$, and nonaffinity persists on an initial interval. These are local, not every-positive-time activity or global restart assertions. A fresh sole-source audit found no decisive gap or indispensable unproved nonclassic import. SHA256: `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4`. [Complete proof](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/EXPLAIN_PRIMARY/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md), [independent source audit](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/ORIGINAL_L3_LOCAL.md).

The corrected **$\sin z+\cos z$ operator reports** concern $L=3$, fixed finite distinct normalized inputs, binary labels and tiny readout. They retain exact finite equations/four kernels, fixed-program joint empirical convergence with feedback and transpose responses, positive initialized nonlinear Grams even for singular raw Grams, and initial hidden-activity jets. Their advertised all-source moment estimate fails already for a one-step Gaussian reverse query: its proposed small-step inequality would bound Gaussian $L^q$ norms uniformly in $q$. Thus the old global/GF claim is withdrawn; the newer broad local theorem applies only at its own local scope and dependency grade. [Corrected proof and objection](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/ROOT_CONTINUATION_AND_OPERATOR.md:113).

The older **$L=3$ tanh, order-one Gaussian readout** report supplies another genuine but limited positive. Its full 1,680-line corrective manuscript proves raw-kernel/query equicontinuity at initialization along every deterministic vanishing horizon. With target zero, the finite initial residual and feature clock on any fixed physical horizon are $O_{\mathbb P}(n^{-1/2})$; prediction/loss converge to zero and the kernel stays at its initialized value (reported as approximately $0.7357209343$). This is a stationary limit, not order-one feature learning. For nonzero labels, both adaptive tails and additional comparison/identification lemmas remain open. [Full corrective report](/home/amir/Codes/PDE/studies/mean_field_peeling/tanh_depth3_operator_ide/RESEARCH_REPORT_2026-08-22.md), [audit of the special results](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/OLD_NONLINEAR_RESNET_RMS.md:127).

### 7.4 Initialization results that change the strategy, not the time scope

For $\phi_\theta(z)=(1-\theta)z+\theta\arctan z$, define the admissible class $\mathcal A_{d,\delta}$ of normalized triples by $\|x_a\|_2^2/d=1$ and the **strict**, two-sided inequalities $-1+\delta<G_{ab}<1-\delta$ for $a<b$. Raw input Grams may be singular. Put $Q_0=G$ and, recursively, $Q_\ell=\mathbb E[\phi_\theta(Z^{(\ell)})\phi_\theta(Z^{(\ell)})^T]$ for the three-sample centered Gaussian tuple with covariance $Q_{\ell-1}$. Let $q_\ell$ be the common diagonal entry. The sharp initialization result is

\[
q_L\asymp(1+\theta L)^{-1},\qquad
\inf_{\mathcal A_{d,\delta}}\lambda_{\min}Q_L
\asymp\frac{\delta^2\theta^2L}{(1+\theta L)^2},\qquad
\inf_{\mathcal A_{d,\delta}}\lambda_{\min}(Q_L/q_L)
\asymp\frac{\delta^2\theta^2L}{1+\theta L}.
\]

The constants are universal over the stated $L\ge1,d\ge2,0<\theta\le1,0<\delta\le1/4$ class; strictly admissible planar triples match the order. The proof must sum the nonlinear Hermite injection over **all** layers to obtain the factor $L$. Its continuation part is conditional on weighted exponential backward tails, not a completed trained global theorem. [Complete sharp report](/home/amir/Codes/PDE/studies/mean_field_peeling/odd_mixture_general_depth/REPORT.md).

As $L\to\infty$ at fixed $\theta>0$, initialized variance behaves as $1/(2\theta L)$, absolute nonaffinity as $1/(12\theta L^3)$, and relative nonaffinity as $1/(6L^2)$. Hence normalized Gram conditioning can improve while feature scale and nonlinear strength shrink. A literal convex offset mixture has a different geometric contraction of initialized sample distances. Neither result disproves a fixed-depth global limit with depth-dependent constants.

The equilateral planar triple with all labels $+1$ supplies an affine-reference obstruction: its raw Gram is singular and the zero-readout purely linear population is stationary on the label direction. For $\phi_\theta(z)=(1-\theta)z+\theta\arctan z$, $0<\theta\le1/2$, any true strong population GF that reaches half-sum square loss at most $3/8$ must satisfy, for sufficiently small $\theta$ at each fixed $L\ge2$,
\[
T\ge\frac{4}{3\pi(3^L-1)\theta}.
\]
This follows from first exit from the unit raw-metric ball: the exact feature-sum recursion bounds the loss drop there by $(3\pi\theta/4)(3^L-1)$, while gradient dissipation and Cauchy–Schwarz bound that drop below by the reciprocal of exit time. Successful states must also leave every fixed raw-metric neighborhood as $\theta\downarrow0$. These are necessary bounds **if** a strong flow reaches that target, not proofs of existence, successful fitting or matching upper rates. They explain why shrinking nonlinearity is not uniformly cheap on data directions the affine model cannot learn. [Complete necessary-scale proof](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_near_identity_all_depths/NECESSARY_FITTING_SCALE.md).

A fixed calibrated sine has unit Gaussian initialized variance and approximately 6.389% best-affine residual fraction; it has a positive-time $L=3$, two-sample joint theorem with an extremely conservative explicit horizon, not a global theorem. A separate $L^{-1/2}$-strength calibrated layer family gives a nontrivial sequential width-first/depth-second **initialization** correlation limit. Neither supplies trained continuous-depth convergence. These are useful moderate-scale candidates/diagnostics, not completed answers. [Sine initialization](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_activation_design/SINE_INITIALIZATION.md), [local proof](/home/amir/Codes/PDE/studies/mean_field_peeling/moderate_sine_global/LOCAL_SOURCE.md), [calibrated-depth note](/home/amir/Codes/PDE/studies/mean_field_peeling/calibrated_near_identity_reviews/manuscript.md).

## 8. The clipped-backward results: important, but not three uncut limits

These results belong to the canonical one-sample $L=3$ pure-arctangent line with tiny Gaussian stored readout. They should be visible in the main research map. Their precise conclusions are different:

| Construction | Checked result | Missing bridge |
|---|---|---|
| Fixed coordinate-query cap $R$ | Unique global population evolution and finite-width identification on every fixed **feature-time** interval | This auxiliary dynamics is generally not the original gradient flow |
| Coordinate cap $R_n=o(\log n)$, including $\sqrt{\log n}$ | Actual causal filtered and unfiltered capped constructions are asymptotically close | No common population limit for the two varying constructions has been proved |
| Energy-compatible metric projection with $R\ge C\sqrt n$ | Projection is inactive; exact agreement with canonical finite GF, including all physical time on the fitting event | Different projection rule; no fixed-cap population theorem or raw-GD bridge for this rule |

The clipping convention is coordinatewise $\tau_R(u)=\max\{-R,\min\{u,R\}\}$. For the unit-rate, one-sample model, the finite reverse fields are
\[
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\qquad
\delta^{(2)}=\phi'(z^{(2)})\odot(W^{(3)})^T\delta^{(3)}.
\]
They contain **neither the residual nor the output factor $1/n$**: $\delta^{(\ell)}=n\nabla_{z^{(\ell)}}f$ in this finite convention. Population formulas replace $z$ by $Z$ and transpose by the actual adjoint. Feature time has $ds/dt=2(1-f)$ for the full square loss with target one. The projection matrix $M$ below uses exactly these unit lower-block rates; it is not a differently preconditioned optimizer.

For the first row, replace the middle reverse query by

\[
\delta_R^{(2)}=\phi'(Z^{(2)})\,
\tau_R\bigl((W^{(3)})^*\delta^{(3)}\bigr).
\]

The same generated spaces retain both trained memories and the true adjoints. On $[0,S]$, the vector field has Lipschitz constant $C_S(1+R)$. Picard/restart and fixed-program comparison give the auxiliary limit. A physical residual clock cannot silently restore the original gradient identity that clipping altered.

For the second row, the proof filters its **actual causal transcript**, not a frozen list of queries. With feature mesh $n^{-2}$, filter $n^{-1/8}$, and perturbation $n^{-1/4}$, its effective rank is at most $C_Sn^{11/12}\log(e+n)^{4/3}$. A two-stage adapted matrix martingale yields a raw-query perturbation $O(n^{-1/24}\log(e+n)^{8/3}+n^{-1/4})$, and nonlinear clipped stability gives

\[
E_n(S)\le C_S(1+R_n)e^{C_S(1+R_n)}
n^{-1/24}\log(e+n)^{8/3}\longrightarrow0.
\]

This is a genuine mesh-uniform quantitative comparison at the stated scales. Nevertheless, closeness of two $n$-dependent objects does not establish existence of a limit for either. The exact two-matrix adaptive Gaussian-law proof additionally identifies their coupled transcript law; the predictable prior-use response remains the uncontrolled part. [Preserved proof family and precise hashes](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/ROOT_CONTINUATION_AND_OPERATOR.md:32).

For the third row, define the current finite matrix

\[
M=\frac{\|h^{(1)}\|_2^2}{n}I+
W^{(2)}\operatorname{diag}(\phi'(z^{(1)})^2)(W^{(2)})^T.
\]

Project the **complete** $\delta^{(2)}$ onto $|u_i|\le R$ in the $M$-metric and use that minimizer in both lower updates. For $e_R=M(\delta^{(2)}-u_R)$, the box optimality conditions give

\[
\frac{(\delta^{(2)}-u_R)^TMu_R}{n}
=\frac{R\|e_R\|_1}{n},\qquad
\int_0^S\frac{\|e_R\|_1}{n}\,ds\le\frac{C_S}{R}.
\]

The actual second-preactivation equation has defect $e_R$, so bounded adaptive tests also see a vanishing integrated defect. This does not imply a vanishing RMS defect or vanishing excess work. The bound $\|\delta^{(2)}\|_\infty\le C_S\sqrt n$ makes the projection exactly inactive above that scale. On the high-probability finite fitting event, total feature time is bounded by a width-independent $S_{\rm fit}$. Choosing the single cap $C_{S_{\rm fit}}\sqrt n$ therefore gives inactivity for **all** physical time. The constant is essential; a coefficient-one $\sqrt n$ claim is not proved. [Projection proof](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/sources/arctan_destination/l3-full-resolution-9nbD4z/ENERGY_COMPATIBLE_LOWER_PROJECTION.md).

These results cannot be concatenated into an uncut theorem: the clipping rules differ, the controlled scales differ, weak defects do not control squared observables, and no varying-cap population construction has been supplied. They are worth adding precisely because they isolate the remaining bridge and prevent further work from treating proved adaptation estimates as open suggestions.

## 9. What the accumulated obstructions have in common

The basic comparison term is

\[
\bigl[\phi'(Z^{(2)})-\phi'(\widetilde Z^{(2)})\bigr]
(\widetilde W^{(3)})^*\widetilde\delta^{(3)}.
\]

A small $L^2$ gate difference times an $L^2$-bounded reverse field need not be small in $L^2$. Rare coordinates can carry order-one squared energy. Energy dissipation, exchangeability, bounded activations and ordinary operator norms do not alone exclude this concentration.

The evidence has several strengths, which must not be conflated:

1. Arbitrary energy-ball examples disprove naive ambient product/Lipschitz bounds. They do not prove the Gaussian trajectory visits those states.
2. The audited generated-action obstruction uses three calls to a Gaussian matrix and its transpose. In the population generated-action space, for an even bump $e_\varepsilon=\psi(Y/\varepsilon)$, $Y=W_0^{(3)}\mathbf1$, and $v_\varepsilon=\mathbb E e_\varepsilon^2\asymp\varepsilon$, take $H_\varepsilon=\tanh((W_0^{(3)})^*e_\varepsilon/\sqrt{v_\varepsilon})$. Taking width to infinity separately at each fixed $\varepsilon>0$, the next forward coordinate law is
   \[
   W_0^{(3)}H_\varepsilon\ \stackrel d=
   \sigma G+c\,e_\varepsilon/\sqrt{v_\varepsilon},
   \]
   jointly with $Y$, where $G$ is standard normal independent of $Y$, $c=\mathbb E\operatorname{sech}^2G>0$, and $\sigma^2=\mathbb E\tanh^2G$. Thus bounded inputs can have output $L^p$ norm at least $c_p\varepsilon^{1/p-1/2}$ for $p>2$ on the same generated spaces. A countable sequence of bump scales belongs to the same generated spaces; the subsequent $\varepsilon\downarrow0$ argument does not assert a joint width-dependent bump scale. Whole-space higher-moment operator shortcuts are false. The coordinate sensitivities grow with $\varepsilon^{-1}$; these are not proved training queries. The formerly pending manuscript now has an exact-version isolated acceptance.
3. A deterministic zero-readout-reachable Hessian witness defeats a proposed primal-only signed material-Hessian estimate even along such reachable paths. Its initial hidden arrays are correlated deterministic arrays, not the canonical independent Gaussians.
4. A separate $1+\arctan(\sinh z)/10$ theorem proves failure of ordinary raw-Hilbert local Lipschitzness at actual small positive-time population states. It coexists with a constructed unique local flow. Ambient local Lipschitzness is therefore genuinely too strong a target, not a necessary condition for success.
5. Actual canonical Gaussian middle-curvature coefficients and squared-log response estimates provide narrower dynamic information. The latter still permits rare amplification as large as $e^{C\sqrt n}$, so it is not the needed square-tail bound.

The common issue is **response concentration on the reached set**, not simply an unfortunate initial matrix spectrum. A tail envelope as weak as $\exp[-cR/\log(e+R)]$, uniform over the appropriate actual comparison family, would suffice for the existing arctangent Osgood continuation argument. That is a precise sufficient criterion, not progress until its premise is proved for canonical trajectories.

The RMS-normalized quadratic program confirms the distinction. Differentiating the normalization gives correct finite GF/action identities and nondegenerate initial kernel $111/[27+\varepsilon(3+\varepsilon)^2]$, and **global finite GF for every finite initialization at fixed $\varepsilon>0$**. The normalization is differentiated exactly, so the finite vector field is smooth. Its nonnegative-loss energy identity bounds total squared metric speed on finite intervals; Cauchy–Schwarz supplies a finite parameter endpoint at any hypothetical finite escape time, and local existence extends through it. This is not a width-uniform response estimate: normalized RMS does not bound coordinate spikes. Its global population source, kinetic uniform integrability and uniqueness remain open. The source audit also corrects a false balancedness sentence: the row drift does not vanish merely by setting the normalization epsilon to zero. Positive initial feature speed is not a positive-time nonlazy theorem. [RMS audit](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/OLD_NONLINEAR_RESNET_RMS.md:145).

## 10. Continuous depth and generalization: one theorem, a different open program

A genuine **scalar-particle residual** result was missing from the narrow master. For fixed samples, its architecture is

\[
x_{a,\ell+1}=x_{a,\ell}
+\frac1{nL}\sum_i\Phi(\theta_{\ell i},x_{a,\ell}),
\qquad \dot\theta=-\eta nL\nabla_\theta\mathcal E.
\]

The hypotheses bound $\Phi(\theta,0)$, $\partial_x\Phi$, and the relevant parameter derivatives/Lipschitz constants on bounded state strips uniformly in raw parameters. A concrete example is

\[
\Phi(\alpha,\omega,\beta;x)
=\tanh\alpha\,\tanh(\tanh\omega\,x+\tanh\beta).
\]

The current state is a depth-indexed parameter law. Forward/backward depth equations determine a parameter transport velocity. Characteristic coupling gives width/depth-independent stability, and the depth discretization error is $O(L^{-1})$. The pathwise error is bounded by

\[
C_T\left[\frac1L\sum_\ell
W_1(\rho^n_{0,\ell},\rho_0)+L^{-1}\right].
\]

For iid depth-constant initialization with a finite first moment, the expected first term tends to zero independently of $L$. Hence every joint sequence $n,L\to\infty$ converges on compact training horizons in the stated depth-averaged law and forward/adjoint/output/kernel measurements. It does not require orthogonal samples. A concrete example has nonaffine initial residual field and nonzero limiting transport. It does not prove all-time fitting, a changing kernel for every instance, or a simultaneous GD-step limit. Its bounded effective amplitude/slope/bias and scalar residual architecture are materially different from the main dense model. [Complete general theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/residual_continuous_depth_gradient_flow/CONSTANT_SPECIES_GENERAL_ACTIVATION_IDE.md), [nontriviality witness](/home/amir/Codes/PDE/studies/mean_field_peeling/residual_continuous_depth_gradient_flow/RESNET_MEAN_FIELD_IDE_THEOREM.md:964).

The separate dense Gaussian-matrix ResNet campaign has an internally variational finite-source-Hermite PDE, but no proved dense width/depth identification or source-cutoff removal. Formal Hermite completeness does not supply reachable compactness. The Gaussian source action is bounded but noncompact, so unit energy can remain above every finite cutoff. A coarse solution's outgoing tail is not the tail of a trained finer solution.

Its numerical controls are useful historical evidence, not convergence theorems. Low source-Hermite degree does not linearize the activation. Several comparisons strongly separate the nonlinear prediction from the identity control, but not all tested gain-adjusted linear controls. The report named “generalization” is a finite synthetic transfer panel comparing PDE predictions with finite-network ensembles; its strongest simultaneous statistical acceptance criterion failed. It is not a theorem about risk on unseen draws. No experiments were rerun. [Detailed dense-ResNet evidence audit](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/OLD_NONLINEAR_RESNET_RMS.md:250).

## 11. Prior art: narrower novelty is stronger science

The exact Gaussian dense-network contract may distinguish this project, but the categorical statement that all related work is formal is incorrect. The audit read primary theorem statements and substantial complete proof sections, not abstracts alone. It also found printed-proof issues and records unaudited recursive dependencies. These sources are comparisons, not imported replacements for the project's missing theorem.

- Nguyen–Pham prove multilayer population existence and compact-time comparisons with finite continuous particle flow and SGD, in a neuronal-embedding, $1/n$-averaging regime. Their framework permits nonlinear evolving features and is not merely fixed-step TP. Its edge dependence/scaling differs from independent $1/\sqrt n$ Gaussian connectors. Their optimization results retain substantial diversity and convergence assumptions. [Primary paper](https://arxiv.org/pdf/2001.11443v3).
- Araújo–Oliveira–Yukimura give rigorous deep mean-field approximation with trained internal layers but frozen endpoint layers and a different scaling. Sirignano–Spiliopoulos prove a two-hidden-layer result with iterated widths, not an unrestricted simultaneous equal-width theorem. Neither can be dismissed as only equations; neither supplies the main contract. [AOY](https://arxiv.org/pdf/1906.00193v1), [SS](https://arxiv.org/pdf/1903.04440v5).
- Celentano–Cheng–Montanari prove empirical continuous-path convergence for a rigorous high-dimensional DMFT. In their neural application hidden width is fixed while input/sample dimensions grow. This refutes “DMFT has not even pointwise convergence,” without proving a deep hidden-width result. [Primary author manuscript](https://web.stanford.edu/~chen96/papers/fom_dynamics.pdf).
- Compact-time approximation plus limiting optimization already appears as a prescribed-accuracy proof pattern in shallow mean-field work. Chizat–Bach's globally optimal application uses precisely this finite-horizon logic; a more general printed interchange lemma is too broad, as the source audit's explicit counterexample shows. Mei–Montanari–Nguyen also state an accuracy theorem, but with noise, regularization and a regularized benchmark. These are not noiseless deep interpolation results. [CB](https://arxiv.org/pdf/1805.09545v2), [MMN](https://arxiv.org/pdf/1804.06561v2).
- Tensor Programs supplies fixed finite-program limits with feature learning in appropriate parameterizations. It alone does not give the growing number of steps needed for GF. But a fixed-step limit plus a separately proved contracting limiting recursion can yield training-to-prescribed-accuracy in an iterated limit; “TP can never address convergence” is too strong. [TP IV](https://proceedings.mlr.press/v139/yang21c/yang21c.pdf), [official supplement](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf).

**Important shared audit dependency.** TP III E.15 / TP IV G.4 state rank-free pseudo-Lipschitz fixed-program convergence, including transposes and scalar feedback. The literature auditor read TP III Appendices K–N completely and checked corrections to conditioning, normalization and moment exponents. Appendix N's stronger conditional-coefficient/all-moment argument for vanishing directions with changing Gram rank remains unclosed in this audit. A bounded matrix operator norm only proves the corresponding $L^2$ smallness, not all higher moments. This is not a counterexample to the master theorem. It means that a project proof importing that full extension is **dependency-qualified under the user's unusually strong proof-audit requirement** until the needed specialization is repaired or proved directly. The source-specific disposition is recorded rather than silently treating all published imports as flawless. [Exact proof locations and qualifications](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/PRIMARY_LITERATURE.md:147).

The plausible novelty target is the **particular combination** of independent Gaussian central-limit-scaled hidden matrices, all layers trained, substantive nonlinearity, joint width/step convergence with the specified strong observables, a constructive autonomous state and unconditional optimization. This targeted audit does not certify that no other paper establishes that package. Continuous depth, growing sample populations and generalization would be further claims requiring their own literature and mathematical checks.

## 12. Strategic conclusion and a scientifically meaningful next direction

The main recommendation is not to add a restrictive data hypothesis and declare the core difficulty removed. The most convincing obstructions concern the proof topology and adaptive response; some occur with **one sample**, and one actual-positive-time non-Lipschitz theorem coexists with a valid flow. Neither opposite labels nor generic correlations explain the entire barrier.

There are genuine broader fitting obstructions, but they must be interpreted correctly. Identical inputs with opposite labels have positive irreducible empirical risk. A bias-free all-odd network also obeys $f(-x)=-f(x)$, so antipodes with the same **nonzero** label cannot both fit. An even first activation instead imposes $f(-x)=f(x)$ and prevents fitting antipodes with unequal labels. These are model symmetries, not necessarily data mislabelling, and do not prevent a population evolution. An ordinary bias or nonodd activation can change that symmetry without whitening data, but this alone gives no global response estimate.

A positive offset helps the common residual mode but cancels from a sample contrast. If top features lie in $[c-a,c+a]$, fitting labels $+1,-1$, each within absolute prediction error $\varepsilon<1$, forces

\[
2(1-\varepsilon)
\le\|W^{(L+1)}\|_{L^2}\,
\|H_+^{(L)}-H_-^{(L)}\|_{L^2}
\le2a\|W^{(L+1)}\|_{L^2}.
\]

Thus a tiny bounded nonlinear variation requires a readout of size at least $(1-\varepsilon)/a$ for that contrast. This explains why a successful common-mode small-nonlinearity argument may fail to remain quantitatively useful for opposite labels. It is a necessary scale cost, not an impossibility theorem for any fixed $a>0$.

Accordingly, the highest-value next direction is **canonical reachable-response continuation for a fixed, moderately nonlinear smooth model on correlated data**, starting at $L=2$ if needed but retaining a path to $L\ge3$. The existing broad local theorem already handles the initial Gaussian singularities and joint mesh passage. The missing estimate should be proved on the actual reached/comparison class, using the exact innovation-plus-response decomposition and physical dissipation—not an ambient $L^2$-algebra assumption, a frozen-history isometry, or a presumed trained Gaussian law. The clipping and weak-defect results provide concrete intermediate tests of such an estimate; they are not themselves permission to change the final optimizer.

No presently justified, non-ad-hoc assumption on the setup is known to remove this response obstruction. A quantitative separation margin may control initial conditioning but has not been shown to control the trained response tails. Assuming the desired tail bound as a hypothesis is a conditional criterion, not a resolved setup recommendation. Where a route uses the broader fixed-program import, its required specialization must be justified; the self-contained original L3 local proof already avoids that dependency in its narrower model. The completed focused negative audits leave real gaps, so the project should not optimize activation design against those claims as if they were verified impossibility theorems.

For optimization, seek dissipation in the **actual residual direction**, which is weaker than a uniform spectral gap in every sample direction. With mean square loss, $r=f-y$, and the learning-metric kernel $K\succeq0$,

\[
\dot f=-\frac2mKr,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^TKr.
\]

A bound $r^TKr\ge\kappa\|r\|^2$ with a constant $\kappa>0$ uniform along training gives exponential loss decay. It must be proved along training; an initial positive Gram does not establish it. Requiring the raw input Gram to be uniformly positive definite would exclude ordinary $m>d$ data and is not justified by the present evidence. Nonlinear feature Grams can be positive definite even when the raw Gram is singular.

Once compact-time loss convergence and $\mathcal L(t)\to0$ are proved, the training-accuracy bridge is elementary. Choose finite $T_\varepsilon$ with $\mathcal L(T_\varepsilon)\le\varepsilon/2$. Then

\[
\mathbb P\{\mathcal L_n(T_\varepsilon)>\varepsilon\}
\le\mathbb P\left\{\sup_{t\le T_\varepsilon}
|\mathcal L_n(t)-\mathcal L(t)|>\varepsilon/2\right\}\longrightarrow0.
\]

This is approximation up to any prescribed accuracy, not a common finite time of exact zero loss, not a width bound for all accuracies simultaneously, and not all-time trajectory convergence. Monotone finite loss can preserve the achieved accuracy afterward without preserving closeness of parameter trajectories.

Finally, the first useful bridge toward generalization is to characterize the trained map on **passive test inputs**, then relate its selected representations to a specified data distribution. A finite training Gram, unique flow, or generic GF energy-dissipation identity does not by itself explain useful features. A minimal-action formulation is informative only if it yields a nontrivial selection property and a link to out-of-sample risk. That is an open research direction, not a consequence of the current master equations.

## 13. Task-by-task contribution and coverage map

Numbers match the user's list and [exact identity index](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/TASK_INDEX.md). A task can contribute a proof, a correction, a method, or recovery work; its title does not determine theorem scope. “Recovered” below refers to the identified local/exported bytes, not a claim of current remote filesystem identity.

### PDE on black-chatgpt

| No. / task | Consolidated contribution and current disposition |
|---|---|
| 1. Resume L3 proof research (4) | Same bounded shifted atan at every fixed $L\ge3$, one sample: full global theorem and persistent activity, §7.2. Complete 1,727-line proof freshly read; direct and recovered hashes agree |
| 2. Resume L3 proof research (3) | Initialization-jet/Borel and alternative basis reconstruction routes. Their transform/growth/identification assumptions remain conditional; no new unconditional global theorem inferred. Both local branch histories inspected; full Borel dependencies not re-audited, §5.2 |
| 3. Resume L3 proof research (2) | Angle-specific two-sample activation theorem, later separation-uniform extension. The broader final open target does not retract the narrower completed result; §7.2 extension qualification |
| 4. Resume L3 proof research | Destination arctangent continuation: integrated initial-query compression, adaptive rank/martingale and growing-cap comparison, exact two-matrix Gaussian law, metric projection, generated-action $L^p$ obstruction, actual-response/curvature estimates; §§8–9. This task now hosts the consolidation, not a resumed old campaign |
| 5. Generalize non-local GF limit | Broad fixed-positive-time $C^{1,1}$, arbitrary-data population/GD theorem and separate L2 activity result; §7.1 adds the finite-GF corollary. Here “non-local” meant a fixed positive interval, not every finite horizon |
| 6. Deep Closure — L3 Nonlinear Arctan Extension | Exact operator algebra plus failed/retracted moment/cluster arguments; the global original order-one-readout arctan/tanh nonzero-label feature-learning target remains open, §7.3; the stationary zero-label tanh exception is separate. Distinguish newer small-readout and changed-activation theorems |
| 7. Deep Closure — L2 Arctan IDE (Audited) | Repaired order-one-readout L2 global prediction/kernel/loss GF proof, with separate fixed-program import qualification; §7.3 |
| 8. Deep Closure — L3 Linear Nonclosure | Bounded-contraction scalar/PDE representation barriers; later operator positive is compatible, §6 |
| 9. Deep Closure — Quadratic Boundary-Layer No-Go | Canonical covariant-Schur initial-layer manuscript, detailed revisions and a newly unclosed adaptive derivative/probability audit; §5.3. Not currently accepted here as settled canonical nonexistence |
| 10. Deep Closure — RMS-Quadratic Program | Exact differentiated-normalization finite equations, global finite action and initial kernel/activity; kinetic/source/uniqueness gates open. Balancedness and initial-nonlazy overstatements corrected, §9 |
| 11. Deep Closure — Linear Depth L≥2 Program | L2 spectral IDE, general rooted-path proposal and retractable/conditional broader width bridge. Completed later L3 theorem does not prove every depth/data case, §6 |
| 12. Deep Closure — Quadratic Operator-IDE Attempt | QI/IQ exact reductions, invariants and spectra-only insufficiency; QI finite-order Stieltjes negative; no full canonical quadratic operator limit, §§5–6 |
| 13. Stieltjes Closure — Architecture Survey | Activation/depth-specific moment tests, exact cubic negative, QI negative and H3 finite positive prefix. No activation-universal Stieltjes law, §5.1 |
| 14. Quadratic μP Nonclosure — No-Go and DMFT Audit | Formal zero radius, positive-Taylor/compiler no-gos, and explicit correction that tagged DMFT was assumed rather than derived; §5 |
| 15. MFP 3 — Generalized Stieltjes and Experiments | Exact observable mobility identities, generalized noncommutative proposal and its missing transform/reconstruction amendment; qualified historical experiments, not global identification |
| 16. MFP 2 — Output-Kernel Stieltjes Program | Canonical output/hidden moment program, later order-17 extension and Ward-derived hidden order 18, retained rational certificates. All-order canonical positivity remains open |
| 17. MFP Audit — Backward-Kernel Proof | Top-down Gaussian peeling, boundary factors, equality partitions, weighted covariance replacement and the still-unexecuted variance/concentration step; §4.1 |

### PDE-2 on black-chatgpt-2

| No. / task | Consolidated contribution and current disposition |
|---|---|
| 1. Find Resume L3 proof thread (4) | Broad two-sample perturbation shape theorem, moderate sine local result and related limits; current proofs checked with inherited-dependency qualification. Recovered final texts read |
| 2. Find Resume L3 proof thread (3) | Two-sample depth-5/6/all-fixed-depth extension, three-sample odd-gain theorem, and explicit rejection of gain as answering no-gain target; §7.2. Alternative recovered finals supersede older “L≥5 open” wording |
| 3. Find Resume L3 proof thread (2) | Odd two-sample activation and improved separation powers, including exponent two; generic three-sample no-gain problem open. Current proofs and recovered branches checked; newest private branch not in preserved final-text provenance |
| 4. Find Resume L3 proof thread (“Work” in UI) | Separation-uniform two-sample theorem; three-sample offset/gain/shape and all-depth extension; sharp odd-mixture initialization and practical assessment. Many recovered alternatives read; newest private branch remains uninspected |
| 5. Find Resume L3 proof research | A distinct recovery/reconstruction task, not another new global theorem. Available checkpoint discussion inspected; latest private branch not certified |
| 6. L=2 arctan, two inputs | Arbitrary-angle local theorem, broad orthogonal-sample activation extension and affine-first general-data exception; special-angle/global compactness variants retained separately. Recovered chronology read, exact proof manifests checked |
| 7. Explain audited proof result | Original L2 baseline, complete L3 local result, global finite-GF/GD coercivity and failed uncut continuation routes; source handoff preserved. Recent recovered finals and principal finite proofs read; every earlier teaching turn not reread |
| 8. Operator MFP L=2, general t (2) | Corrected sin+cos fixed-program/kernel/initial-activity report; growing-mesh full proof withdrawn. Deep-linear global operator and final representation results consolidated in §6; complete corrected 885-line report read |
| 9. Operator MFP L=2, general t | Earlier related fixed-horizon/operator work, quadratic/ReLU loss-mesh analysis and scaling distinctions; complete corrected report and preserved reconciliation read. No inference from a terminal theorem claim alone |
| 10. Test nonlinear mean-field scaling | Local quadratic/ReLU mesh and scaling manuscripts located/read; exact attribution and complete private task experiment/history record unavailable. No new experiments or positive nested theorem inferred |
| 11. Derive joint mean-field scaling | Effective-coordinate mobility calculation and distinction from coherent $1/n$ connector model. Original nested finite-type primary theorem not recovered; secondary comparison is not certification of it |
| 12. Operator MFP t=2, general L | Four-fine versus two-coarse finite-depth theorem and later self-contained finite-step/Price/cubic package; §4. Exact private task/version linkage remains incomplete |
| 13. Depth 3 Arctan Closure Program — attempt 2 | Original order-one-readout arctan source continuation and dynamic cavity/Schur–Volterra route; current persisted frozen contract/open-state corrections read, §7.3. Private task history not newly recovered |
| 14. Depth 3 Arctan Closure Program | Same original model's exact autonomous algebra and failed ordered-limit/global bridges. Do not substitute shifted activation or tiny readout. Principal persisted sources read, private history incomplete, §7.3 |
| 15. Teach L=2 arctan theorem | Exposition of the original L2 theorem, not an independent theorem or independent review. Mathematical source read; private teaching chronology unavailable |
| 16. Deep-PDE Audit — L3 Tanh and ResNet Proofs | Corrective tanh report, zero-label stationary result, initialization equicontinuity, scalar-particle residual theorem versus dense ResNet gap. Full principal reports read; private history incomplete |
| 17. MFP Mirror — Continuous-Time Limits and L3/ResNet Audit | Continuous-time bridge analysis and residual/dense architecture distinction; genuine scalar-particle width/depth theorem retained, §10. Local primary proofs read; private history incomplete |
| 18. MFP Mirror — Order-5 DAG and Finite-Step Extension | Order-five DAG/scalar recurrence, fixed-depth/fixed-step Gaussian identification and mesh-refinement limitations; full principal local package read, private chronology/version linkage incomplete |
| 19. Stieltjes Program — High-Order Moments and Counterexamples | Identity confirmed in read-only metadata; local high-order/Stieltjes primary proofs audited. No fresh private history or version-matched task export recovered, so its additional amendments cannot be claimed exhausted |

The word “Work” is UI text, not an additional research task. Empty duplicate archived forks are not independent results or audits. The supersession map follows proof contents and explicit corrections, not which final message is newest.

## 14. Corrections and remaining audit obligations

The main corrections to the earlier consolidation/recollections are now explicit:

- Restore the clipping/adapted Gaussian/projection chain and the accepted generated-action obstruction; do not turn the three clipping scales into three uncut-limit theorems.
- Add exact finite-step MFP machinery and the scalar-particle continuous-depth theorem, retaining their distinct architectures/quantifiers.
- Correct output order 19 to retained order 17, and distinguish the disproved metric/activation-universal Stieltjes claim from the open canonical unit-metric case.
- Replace zero-radius “no smooth ODE” with the valid analytic/positive-compiler restrictions.
- Retain the completed L3 one-sample deep-linear theorem; do not claim arbitrary-depth/arbitrary-data identification from the older conditional proposal.
- Add the broad local theorem's finite-GF corollary, without broadening its time or observable scope or hiding its external proof dependency.
- Withhold blanket certification of the bounded-slope ladder negative and canonical covariant-Schur negative; the former uses a false deterministic estimate, while the latter has an unproved adaptive bridge and a false uniform row estimate on its printed domain, confirmed by focused recheck.
- Preserve the genuine global nonlinear examples while separating mathematical nonaffinity from scientifically meaningful nonlinear strength.
- Replace categorical dismissals of prior work and unsupported novelty claims with model-specific comparisons.

The focused covariant-Schur/import follow-ups and the special-variant/original-L3-local source audits are complete at their recorded scopes. Independent document-only review and correction are tracked in the review directory. Missing histories, unavailable primary artifacts, unrederived large coefficient tables and unclosed imported proof chains remain explicitly marked. A clean review of an accurately qualified consolidation does not make those mathematical premises proved or turn the main global/generalization objective into a completed result.
