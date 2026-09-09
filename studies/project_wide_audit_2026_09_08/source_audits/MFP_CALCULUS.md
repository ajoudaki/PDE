# MFP calculus: isolated source audit

Audit date: 2026-09-08. Scope: exact Mean Field Peeling (MFP/OMFP), finite-order and finite-step Gaussian compilation, width-first identification, and the logical bridge to mesh refinement.

## 1. Consolidation verdict

The strongest locally self-contained result I recommend is the **single-sample, arbitrary separately fixed hidden-depth and step-count theorem** in the depth–time package: an identified width-first finite-step Gaussian program, a singular-covariance Price compiler, and a fifth-order remainder with a finite, explicitly depth/horizon-dependent bound. It is not a horizon-uniform continuous-time theorem.

The broadest genuinely joint depth/batch contracted result I checked is the **initialization cubic feature-flow observable** at arbitrary separately fixed \(H,B\), including singular input Gram matrices. Its probability identification depends on an external tensor-program master theorem. I checked the relevant external theorem statements and hypotheses, but not their complete proof dependencies; that dependency remains **unaudited here**, not disproved.

There is no audited unrestricted, depth-independent, finite-state compiler/completion theorem covering arbitrary observable heads, arbitrary orders, arbitrary batch growth, and full training trajectories. The canonical description itself labels that strengthening a target. The later CFPC/RCGC languages contain useful exact identities and conditional completion lemmas, not a general nonlinear mesh-removal theorem.

A substantive additional issue found in this audit: the bounded-slope “full-network ladder” and “super-\(t^5\)” counterexamples use an unproved uniform-in-width activation-stability step. Their asserted deterministic normalized-energy difference estimate is false; an explicit analytic witness appears in §7. Do not promote those full-network counterexamples solely from their historical audit labels.

| Claim | This audit's disposition |
|---|---|
| Three-hidden-layer backward kernel, leading annealed value | Correct conditional calculation; weighted covariance replacement is an assumption; concentration is not executed in the recovered task. |
| Joint fixed \(H,B\) cubic recursion | Algebra and response structure checked; probability theorem has the external dependency reservation above. |
| One-sample order-five DAG / 29-scalar flattening | Finite-order, model-specific closure; six sweeps, unit forward Grams for the scalar version. No exhaustive independent rederivation of every scalar transition coefficient here. |
| Arbitrary fixed \(L,N\), one sample, finite nonzero step | Recommend at the stated bounded-derivative/linear-growth scope; full local probability, compiler, and cubic manuscripts read. |
| Uniform \(t^4h^5\) remainder at \(L=1\) | Recommend: full elementary proof read, including Gaussian-envelope integration. |
| Same bound for generic \(L\ge2\), bounded derivatives through order 12 | Not established by the fixed-horizon package or the general completion proposals. |
| Quadratic activation, full expected-output step-doubling divergence | Positive-polynomial proof checked; fixed-program probability identification depends on the external master theorem. |
| A single smooth bounded-slope activation with infinite/super-polynomial effective fifth remainder | Withhold certification: stability bridge gap; later algebraic amendments do not repair that bridge. |
| One Banach algebra containing Gaussian atoms with the stipulated quantitative product bound | Impossible, by the source's elementary Gaussian-power contradiction. This does not disprove the scalar near-identity remainder. |
| General nonlinear, restartable, width/mesh-uniform calculus | Open in the inspected general-calculus sources. Specialized positive limits are outside this assignment. |

“Checked” below means inspection and mathematical audit of the stated source, not acceptance of an earlier PASS. No numerical or symbolic experiments were run.

## 2. Task provenance and coverage gaps

All repository findings refer to the **local bytes hashed in §10**. Matching apparent paths on another host would not establish matching contents. I did not obtain remote file hashes or remote task pages.

The available tool catalogue contains no callable app read_thread/list_threads tool. I searched the available tool metadata; I did not contact, resume, message, or create tasks. The user's supplied remote metadata is retained as metadata, not as evidence of the mathematics. I did not access alternate credentials, alter permissions, or attempt to read protected remote rollout directories.

| Requested task | Recovery and contribution / explicit gap |
|---|---|
| PDE #17, “MFP Audit — Backward-Kernel Proof”, 019fcc94-551d-7660-84a7-f240d3564575 | Located the local migrated rollout. Read the complete corrected standalone execution at JSONL line 1673 and the complete later variance discussion at line 1719, plus substantive earlier user amendments at lines 694, 1040, 1074, 1088, 1140, 1198, 1407, 1630, 1679. Contribution: top-down elimination, lower-group boundary factors, equality partitions, weighted covariance replacement, and separation of expectation from concentration. The full 1722-line rollout was not read; locator scans are not counted as full reads. |
| PDE-2 #10, “Test nonlinear mean-field scaling”, 01a03e53-2e5f-75e2-8dcf-a02ee6f8d10c | Remote page unavailable. Local nonlinear/mesh and scaling-comparison manuscripts were read, but their exact attribution to this task and amendment chronology are unverified. Coverage gap: the task's original experimental requests/results and complete conclusions were not recovered. No experiments were repeated. |
| PDE-2 #11, “Derive joint mean-field scaling”, 01a03d8a-3d77-7441-a157-7bc33559ecd2 | Remote page unavailable. Local joint-scaling synthesis distinguishes ODE-consistent diagonals, unresolved under-resolved diagonals, changed clocks, and coherent \(1/n\)-kernel initialization. The original positive nested finite-type manuscript was not located; the local comparison is secondary provenance, not its proof certificate. |
| PDE-2 #12, “Operator MFP t=2, general L”, 01a033d2-7d4d-7ce2-b123-20aa9e88fa58 | Remote page unavailable. The full local four-fine-versus-two-coarse theorem was read, as was the broader depth–time package that proves the corresponding \(t=2\) specialization. Exact task authorship/version linkage remains a coverage gap. |
| PDE-2 #18, “MFP Mirror — Order-5 DAG and Finite-Step Extension”, 01a01554-1f64-7c30-8412-032bfebc02ec | Remote page unavailable. Full local order-five DAG and scalar-recursion manuscripts, and the finite-step depth–time package, were read. No claim that these copies exhaust that task's older turns or latest amendments. |

The four PDE-2 IDs and hostId remote-ssh-discovered:black-chatgpt-2 are user-supplied metadata recovered by the user from read-only SQLite; I did not independently reopen that database.

The backward task's most important chronology is substantive, not a final-label inference: the user first corrected bottom-up extraction, then prohibited summing indices still present below, identified the layer ownership of Stein-created factors, chose deterministic replacement for the leading theorem, and finally asked how to establish determinism. The last response proposes a second-moment calculation; it does not perform it. [Corrected execution](/home/amir/.codex/sessions/2026/08/04/rollout-2026-08-04T13-41-41-019fcc94-551d-7660-84a7-f240d3564575.jsonl:1673), [variance discussion](/home/amir/.codex/sessions/2026/08/04/rollout-2026-08-04T13-41-41-019fcc94-551d-7660-84a7-f240d3564575.jsonl:1719).

## 3. Model and clock ledger

The principal MFP model has no biases, equal hidden width \(n\), separately fixed hidden depth \(H\) or \(L\), and separately fixed sample count \(B\). These are different parameters; \(N\) denotes update count and \(t\) the number of coarse steps in a paired comparison.

For the batch model,
\[
z^1=Ux/\sqrt{d_0},\qquad z^\ell=W_\ell h^{\ell-1}/\sqrt n,\qquad
f(x)=n^{-1}a^\top h^H(x).
\]
All raw Gaussian blocks are independent, centered, variance one; \(d_0,B,H\) are fixed. The single-sample depth–time package further fixes scalar input \(1\), so \(z^1=u\).

The raw-coordinate gradient metric is \(nI\). Feature ascent is
\[
\theta^+=\theta+h\,n\nabla f.
\]
For \(g_c=c^\top f\), the initialization feature-flow operator is
\(D_c=n\nabla g_c\cdot\nabla\), with deterministic channel \(c\) held fixed.

| Convention | Consequence |
|---|---|
| Raw hidden connector \(W\), effective connector \(G=W/\sqrt n\) | Raw mobility \(n\) becomes effective mobility \(1\). |
| Raw readout \(a\), effective readout \(v=a/n\) | Raw mobility \(n\) becomes effective mobility \(1/n\). |
| First effective matrix \(U/\sqrt{d_0}\) | Mobility \(n/d_0\); \(d_0\) is fixed. |
| Normalized endpoint \(L^2\) metrics and effective connector Frobenius metric | Equivalent to the preceding raw metric; applying \(n\)-Euclidean mobility again to every effective block changes the model. |
| Full batch square loss \(B^{-1}\sum(f-y)^2\) | Descent velocity \(2nB^{-1}\sum(y-f)\nabla f\), with any learning-rate multiplier retained. |
| One-sample half-square loss \(\tfrac12(1-f)^2\) | Velocity \((1-f)n\nabla f\), physical time \(kh\). |
| Coarse-minus-fine \(D_t=F_t(2h)-F_{2t}(h)\) | Opposite sign to \(\Delta_t=F_{2t}(h)-F_t(2h)\) used in other directories. |

These scalings are explicit in the [case-study ledger](/home/amir/Codes/PDE/studies/mean_field_peeling/MUP_TRAINING_CASE_STUDY.md:211) and the [RCGC contract](/home/amir/Codes/PDE/studies/renormalized_causal_gaussian_calculus/RESEARCH_CONTRACT.md:1).

At initialization the centered \(1/n\) readout gives \(f_n\to0\); it is not a frozen readout or a lazy-training theorem. The case-study appendix also considers \(n^{-\alpha}\) readouts. Its normalized backward quantities cannot be mixed with unnormalized derivatives, and the \(\alpha=1/2\) random-output/loss-multiplier regime is different from the centered \(\alpha=1\) regime.

A one-sample continuous loss flow is a scalar time change of feature ascent while the clock is well defined. A discrete residual-dependent Euler schedule is not obtained by simply replacing \(h\) in a constant-feature-step formula. Neither finite jets nor finite-step limits prove global fitting, a positive-time nonlazy theorem, or convergence of the full parameter state.

## 4. What the exact peeling calculus actually proves

### 4.1 Backward-kernel laboratory

For three hidden layers and two evaluated inputs, write
\(\delta^\ell_i=n\,\partial f/\partial z^\ell_i\) and
\(B_n^1=n^{-1}\sum_i\delta_i^1(x)\delta_i^1(x')\).
The full corrected computation gives
\[
\lim_n\mathbb E B_n^1=D_1D_2D_3,
\quad
D_\ell=\mathbb E[\phi'(Z_\ell(x))\phi'(Z_\ell(x'))],
\]
**provided the explicitly named weighted covariance replacements hold**.

The recovered execution assumes \(\phi,\phi',\phi'',\phi'''\) continuous with polynomial growth, and then separately assumes the weighted replacement estimates. Bare \(C^3\) regularity is not its probability hypothesis.

Decisive proof skeleton:

1. Scalarizing two backward paths gives a prefactor \(n^{-3}\).
2. Integrating the readout pairs the two top indices.
3. Conditional row-wise Gaussian integration of \(W_3\) gives a Wick delta and the complete two-weight Stein correction
\[
\mathbb E[w_pw_qG(Z)]
=\delta_{pq}\mathbb EG(Z)
+n^{-1}\sum_{\alpha,\beta}h_p^\alpha h_q^\beta
  \mathbb E[\partial_{\alpha\beta}G(Z)].
\]
The \(h_p^\alpha,h_q^\beta\) remain lower-layer boundary factors.
4. Before using row independence at layer two, split \(p=q\) and \(p\ne q\). The off-diagonal branch is generally nonzero: two one-weight Stein attachments contribute \(n^{-1}\), while the ordered row count is \(n(n-1)\).
5. The five completed branches have orders
\(1,n^{-1},n^{-1},n^{-2},(n-1)/n^2\).
Only the direct Wick ladder survives.
6. Random Gram replacement requires
\(\mathbb E[|\Gamma(Q_n)-\Gamma(Q)|\,|S_n|]\to0\);
unweighted convergence of \(Q_n\) is insufficient. Complementary \(L^p,L^q\) bounds suffice.

The surviving finite-width expressions after freezing covariance are **not an exact \(1/n\) bias expansion**, because the replacement error is only \(o(1)\). The final layer is direct Gaussian averaging; no CLT is required for this leading expectation.

The separate concentration obligation is \(\operatorname{Var}B_n^1\to0\). The last task response gives the correct martingale identity
\[
\operatorname{Var}B_n^1
=\sum_\ell\mathbb E\operatorname{Var}
  \bigl(\mathbb E[B_n^1\mid\mathcal F_\ell]\mid\mathcal F_{\ell-1}\bigr),
\]
but does not bound its summands. The manuscript likewise explicitly withholds concentration. [Case-study execution](/home/amir/Codes/PDE/studies/mean_field_peeling/MUP_TRAINING_CASE_STUDY.md:605), [concentration boundary](/home/amir/Codes/PDE/studies/mean_field_peeling/MUP_TRAINING_CASE_STUDY.md:906).

The same case study's generic nonlinear **two-step hidden-Gram section remains a formal coefficient calculation**, not a completed finite-step probability theorem. Its exact Taylor identity is
\[
G_2=G_0+2\eta L+\eta^2(4C+R)+O(\eta^3),
\qquad R=DG[DV[V]],
\]
where \(C=\tfrac12D^2G[V,V]\) is the one-step quadratic coefficient and \(V\) is the finite-width update vector field. The second increment therefore has coefficient \(3C+R\). One cannot differentiate the limiting statement \(L=0\) to discard \(R\). Its multichannel Stein formula is exact with frozen source vectors; applicability to adaptive vectors requires the complete response registry, and the general nonlinear execution still contains response-function placeholders. The later single-sample theorem in §5 resolves that subcase by a different complete finite-step DAG; it does not silently finish the case study's arbitrary-batch execution. [Exact two-step identity](/home/amir/Codes/PDE/studies/mean_field_peeling/MUP_TRAINING_CASE_STUDY.md:1924), [response schema and formal result](/home/amir/Codes/PDE/studies/mean_field_peeling/MUP_TRAINING_CASE_STUDY.md:2619).

### 4.2 Generic fixed depth and batch: the cubic observable

The full joint recursion concerns
\[
C_{n,c}=D_c^3g_c
=2n^3\nabla^3g_c[\nabla g_c,\nabla g_c,\nabla g_c]
 +4n^3\|\nabla^2g_c\,\nabla g_c\|^2.
\]
It allows any deterministic positive-semidefinite input Gram, including repeated/singular samples, at fixed \(H,B,c\).

I checked the universal derivative identity; orientation of batch contractions; the forward four-jet block; the differentiated reverse pass; the terminal parameter-block Hessian energies; and the parity eliminations. The decisive reused-source rule is “joint Gaussian innovation plus responses against every earlier opposite-orientation input,” with syntactic derivatives taken while previously computed scalar coefficients are fixed. Freshening \(W\) when \(W^\top\) is used is incorrect.

The recurrence retains all four potential forward-jet responses before eliminating three: two are absent by syntax, and the first-jet response vanishes by centered reverse-carrier parity. This is not a blanket rule that responses vanish. In particular the zeroth response contains the \(\phi'''\) term. The orientation \(G^{0,r-1}\), rather than its transpose, matters for \(B>1\).

The compact state uses \(O(B^2)\) scalar entries per layer at this named order. Auxiliary Gaussian variables are eliminated by Wick–Stein degree descent. The final activation atoms can be \(B\)-dimensional here; the unrestricted grammar may require several source/jet copies and hence dimensions \(qB\). Flat polynomial size is not bounded by the compact-state count. [Joint proof, model and identity](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/depth/DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md:17), [reverse responses](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/depth/DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md:381), [termination and probability boundary](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/depth/DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md:618).

For the full batch MSE, \(C_{n,c}\) alone is not the exact finite-width third loss derivative. The source retains additional Hessian contractions, then uses readout parity, deterministic limits, and Hölder with \(f_n(0)\to0\) to remove them. The claimed loss expansion is coefficientwise at zero, not a loss formula at positive time. [Exact loss mapping](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/depth/DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md:838).

The earlier EXACT_FIXED_DEPTH_PROGRAM is an exact finite-width order-three generator with ordinary Taylor coefficients, division by \(k+1\) in the ODE update, and factorial conversion at the terminal derivative. Its closing statement that genuinely joint \(H,B\) contraction remained open is superseded in scope by the full joint recursion above; it is not a reason to downgrade the later explicit joint proof.

This does not settle the canonical grammar-wide finite-state target: its closure and dimension claims are explicitly separated from named successful observable families. [Target and strengthenings](/home/amir/Codes/PDE/studies/mean_field_peeling/CURRENT_RESEARCH_STATE.md:1549), [remaining proof obligations](/home/amir/Codes/PDE/studies/mean_field_peeling/CURRENT_RESEARCH_STATE.md:1839).

### 4.3 Order five: precise strength and reservations

The order-five matrix-state manuscript uses ordinary Taylor coefficients through degree five, six forward and five reverse source levels, with covariance/response counts \(21+15+15+15=66\) per initialized connector in its one-sample formulation. Its chronological degree filtration and terminal Gaussian degree descent are finite. The count is not a generic arbitrary-order, arbitrary-head, arbitrary-batch state bound.

The scalar specialization assumes
\[
B=1,\qquad Q^0=\cdots=Q^H=1,
\]
with a shared activation; in particular \(\mathbb E\phi(G)^2=1\). It gives **six sweeps**, of dimensions \(7,8,4,4,3,3\), totaling 29 coordinate types, plus depth-indexed caches. It explicitly leaves a stronger single-forward/single-backward compression open. Unnormalized \(\phi(x)=x^2\) violates the unit-Gram hypothesis; its forward variance chain is not constant.

The universal fifth derivative backbone checks:
\[
D^5f=2V[p^5]+22U[Hp,p^3]+14\|T[p,p]\|^2
+30\langle T[p,p],H^2p\rangle
+36T[Hp,Hp,p]+16\|H^2p\|^2.
\]
The source regrouping using second and third moving-gradient jets gives its extra four sweeps. I checked this identity and regrouping, the pass dependencies, and the declared normalization. I read every displayed scalar transition, including Appendices A–C, but did **not** independently rederive every polynomial coefficient or rerun the large exact-map comparisons. The two terminal assemblers share local transition data; their agreement alone is not two independent local Wick derivations.

Thus consolidate the exact finite-order recurrence architecture and its scope; retain a separate coefficient-certificate qualification for the complete flattened tables. The general-depth interpolation suggested for an order-five deep-linear polynomial is explicitly conjectural in the matrix-state manuscript and is not its all-depth proof. [Matrix-state census](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/depth_order5/primary/ARBITRARY_DEPTH_RECURSION.md:213), [scalar theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/depth_order5_scalar/ARBITRARY_DEPTH_B1_ORDER5_SCALAR_RECURRENCE.md:3), [two-sweep boundary](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/depth_order5_scalar/ARBITRARY_DEPTH_B1_ORDER5_SCALAR_RECURRENCE.md:405).

Readout reflection kills suitable **annealed** even coefficients (and deterministic limiting values), not the same coefficient at every realized finite-width initialization. Likewise a squared hidden-activation RMS head is a particular observable head, not all nonlinear heads or the unsquared RMS.

## 5. Probability bridges and the broadest finite-step theorem

### 5.1 External dependency ledger

The primary Tensor Programs III text, Setup E.2 and Theorem E.15, permits fixed programs with Gaussian matrix/transpose reuse and pseudo-Lipschitz maps/tests, without a nonsingularity assumption. Its conclusion here is almost-sure scalar convergence, not automatically annealed convergence. I read those definitions/statements and Appendix N in full; Appendix N still invokes earlier conditioning proofs that I did not fully audit. [Local theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_self_contained/literature/yang_tensor_programs_iii.txt:2114).

A later amendment correctly invokes a different theorem: Golikov–Yang, Definition 3.1, Definition 3.5, Setup 3.6, Theorem 3.7. The primary statement allows tied transposes and scalar feedback and adds every-finite-\(L^p\) convergence under all-orders polynomial smoothness, Gaussian initial vectors, appropriate independent matrix moments, and initial scalar moment assumptions. Deterministic initial scalars and iid Gaussian matrices satisfy these requirements here. I read the primary definitions and theorem, not the complete proof/supplement. **External proof dependency unaudited.** [Primary theorem, pp. 4–6](https://proceedings.neurips.cc/paper_files/paper/2022/file/8707924df5e207fa496f729f49069446-Paper-Conference.pdf).

This amendment matters: it would be incorrect to report an unresolved UI gap merely because E.15 alone does not supply \(L^p\). Conversely, finite \(C^3\) or \(C^5\) regularity does not satisfy the all-orders theorem; polynomial growth of the highest available derivative does not imply that derivative is pseudo-Lipschitz. Smoothing requires a separate stability/removal argument. The historical [probability audit](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/PROBABILISTIC_BRIDGE_AUDIT.md:43) was used to locate this amendment, not as its proof.

### 5.2 Locally self-contained fixed \(L,N\), \(B=1\) identification

The WIDTH_DEPTH_TIME manuscript does not need the preceding external master theorem. Its identification assumptions are: fixed \(L,N\), scalar input \(1\), no biases, raw independent standard Gaussians, normalized \(1/n\) output, \(\mathbb E\phi(G)^2=1\), linear growth of \(\phi\), and bounded first and second derivatives. The nonconstant branch is handled at each fixed \(h\ne0\); constants are separate. The full remainder theorem strengthens this to bounded derivatives through order 12.

I read all 1321 lines and checked the following indispensable chain:

1. The exact trained-matrix split retains every historical rank-one update. There are \((2N+1)(L-1)\) globally interlaced, predictable initialized-matrix actions.
2. Adaptive two-sided Gaussian conditioning gives
\[
W=P_CW+WP_H-P_CWP_H+P_C^\perp\widetilde W P_H^\perp.
\]
The induction is over the global chronology, not independent per-matrix histories.
3. With \(Q,K\) the old input Grams, the cross-block identities
\(R=SQ+KP^\top\), \(v=K\rho+Sq\), \(r=Q\sigma+Pk\)
cancel the projection terms and produce the complete inverse-free forward/reverse response sums.
4. Fresh innovations give strict finite-history rank at fixed nonzero \(h\), by an upward feature/downward cotangent induction. Nonconstant \(\phi'\), nonzero affine slope, and constant activation are separate cases. No uniform spectral gap as \(h\to0\), \(N\to\infty\), or \(L\to\infty\) is asserted.
5. The stopped raw/extended/ideal coupling controls fields and empirical contractions at arbitrary prescribed finite moments using a finite backward moment tower. A chosen failure probability \(O(n^{-m})\) is obtained before removing the stop.
6. A raw normalized-energy polynomial majorant in initial endpoint norms and Gaussian connector operator norms removes stopping and proves terminal UI. Unlike the ladder argument in §7, the good-event estimate uses mixed higher moments and the adaptive Gaussian action kernel; it does not claim arbitrary energy-ball \(L^2\) product continuity.

This establishes actual finite-step width identification and expected-output convergence, not merely an internal Gaussian surrogate. The width limit is taken at fixed \(h,N,L\). [Conditioning proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/WIDTH_DEPTH_TIME.md:238), [rank proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/WIDTH_DEPTH_TIME.md:561), [coupling and UI](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/WIDTH_DEPTH_TIME.md:841).

### 5.3 Singular Price compiler and repaired cubic bridge

The compiler groups local Gaussian calls with dimension at most \(2N+2\). At \(h=0\), repeated-time covariances coalesce. Its proof differentiates Gaussian expectations by
\[
\mathcal P_C=\partial_h+\tfrac12 C'(h):D_Y^2,
\]
first at \(C+\varepsilon I\), then removes \(\varepsilon\) with a common polynomial Gaussian envelope. It does not differentiate a singular covariance square root. The reachable derivative budget is \(2r+j+q\le10\), plus the base response derivative; bounded activation derivatives through order 12 suffice.

The finite syntax-size recursion explicitly pays product-rule, covariance-pair, and derivative multiplicities. Solving the scalar majorant recursion produces \(B_\phi^{E_{L,N}}\), with \(B_\phi=\max(4,M_\phi)\) and \(E_{L,N}\) given by finite numerical recurrences. I checked the call count, derivative-budget mechanism, majorant recurrence, and Taylor factors; I did not recompute every very conservative integer syntax bound from an independent compiler.

The cubic bridge is importantly **not** the earlier finite-list oracle. It fixes Gaussian \(L^2\) spaces, disjoint first-chaos blocks, and onto isometries \(I_a,J_a\), then
\[
W_{a,0}=I_a+J_a^*,\qquad \|W_{a,0}\|\le2.
\]
For \(x=\Psi(J_ac_1,\ldots,J_ac_m,\zeta)\) with the required independent complementary block, Stein and Riesz give
\[
J_a^*x=\sum_r\mathbb E[\partial_r\Psi]c_r.
\]
This is compatible under history enlargement even for singular Grams. Adding finite-rank learned increments reproduces the chronological Gaussian DAG. Mixed derivatives are justified on finite generated smooth scalar slices, **not** by claiming global \(C^3\) Nemytskii regularity on an open \(L^2\) ball. I read the full 1700-line cubic proof and the separate fixed-operator check.

Let \(S=D^3\mathcal F[g,g,g]\), \(E=\|Dg[g]\|^2\), and \(J_{\phi,L}=S+4E\), where the source gives a terminating nine-Gaussian-moment, forward/reverse depth recursion. Euler differentiation yields
\[
F_{N,L}^{(3)}(0)
=\frac{N(4N^2-3N+1)}2 S+2N(N-1)(2N-1)E.
\]
Consequently
\[
D_{t,L}(h)=-\frac{t(2t-1)}2J_{\phi,L}h^3+R_{t,L}(h),
\qquad
|R_{t,L}(h)|\le B_\phi^{E_{L,2t}}|h|^5
\quad(|h|\le\tfrac12).
\]
Parity kills orders \(0,2,4\), and the linear clock cancels. The remainder factor is \((32+1)/120<1\). The continuous feature-flow cubic is instead \(2S+4E\); do not confuse it with the step-doubling invariant \(S+4E\).

For \(t=2\), the coarse-minus-fine coefficient is \(-3J_{\phi,L}\); fine-minus-coarse is \(+3J_{\phi,L}\). The older four-versus-two manuscript leaves the sixfold temporal factorization open because its marked response enlargement was incomplete. The fixed-operator proof supplies that missing bridge in the later local package. This is a mathematical supersession in scope, not verified remote version chronology.

Likewise, the earlier general-horizon algebra note's missing identification for arbitrary separately fixed step count is supplied by WIDTH_DEPTH_TIME. Its second missing ingredient—a bound uniform as the step count grows—is not.

[Full theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/PROOF.md:3), [singular Price proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/COMPILER_DEPTH_TIME.md:188), [fixed-operator repair](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/CUBIC_DEPTH_TIME.md:338), [nine-moment recursion and derivation](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/CUBIC_DEPTH_TIME.md:991), [older open factorization](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_general_depth_four_vs_two_bound/THEOREM.md:475).

## 6. Uniform refinement: positive result and exact negative scopes

### 6.1 One hidden layer

For \(L=1\), neurons remain iid under
\[
a^+=a+h\phi(u),\qquad u^+=u+ha\phi'(u).
\]
The expected width-\(n\) output equals the two-Gaussian population expectation for every \(n\). With the same normalized \(C^{12}\), linear-growth/bounded-derivative envelope, UNIFORM_L1 proves
\[
\left|D_{t,1}(h)+\frac{t(2t-1)}2J_{\phi,1}h^3\right|
\le B_{\phi,1}t^4|h|^5,\qquad |h|\le (16M_\phi t)^{-1}.
\]

The proof factors the exact coarse/fine defect as \(h^2\) times a sum of \(t\) transported local defects. Three \(h\)-derivatives cost \(t^3\). A pathwise envelope polynomial in \(r=1+|A|+|U|\) times \(e^{Cr}\) is Gaussian-integrable, justifying differentiation and yielding \(t^4\). No bounded-initial-coordinate assumption is hidden.

For \(\phi(x)=x\),
\[
F_{N,1}(h)=\tfrac12[(1+h)^{2N}-(1-h)^{2N}],
\]
and the paired fifth coefficient is
\(-\tfrac43t(t-1)(2t-1)(8t-9)\).
Thus a universal power below \(t^4\) is impossible even at one hidden layer. [Full proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/UNIFORM_L1.md:169), [sharpness](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/UNIFORM_L1.md:668).

### 6.2 A literal fifth coefficient cannot be super-quartic in horizon

For a fixed smooth Euler germ,
\([h^r]F_N=\sum_{m\le r}\binom Nm\Theta_{r,m}\).
The degree-five leading term cancels in
\([h^5](F_{2t}(h)-F_t(2h))\), so the result has degree at most four in \(t\).
This says nothing about the full remainder on \(0<h\le\rho/t\), when higher orders need not be uniformly controlled.

I read the complete rational weight-generator code and the all-six transition-census code without executing either. Their ascending-state chronology is implemented with descending coefficient updates so right sides remain at the old step. The census imports a separate transition compiler and does not independently prove that imported compiler complete. Its principal-weight check evaluates an identity background, whereas its subset count is a structural check; neither is by itself a complete arbitrary-background analytic stability proof. [Temporal algebra](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_quantitative_width_first_bound_general_t/ALGEBRA_AND_OBSTRUCTION.md:1).

### 6.3 Quadratic full-output obstruction

For \(B=1,L=2\), feature ascent, and
\(\phi(x)=px+qx^2\), \(p^2+3q^2=1\), \(q\ne0\), the primary no-go manuscript proves
\[
\Delta_t(\rho/t)\longrightarrow+\infty\qquad(\rho>0).
\]
Thus no cubic-subtracted fifth remainder bounded by any fixed polynomial in \(t\) holds on that interval.

The mechanism is all-order, not a bad fifth coefficient:

1. For nonnegative \(p,q\), the raw vector field and output have nonnegative formal polynomial coefficients.
2. Fine-minus-coarse composition preserves coefficientwise positivity. Deleting the bottom update gives a coefficientwise lower comparison **after Gaussian expectation**, not a pathwise comparison of signed Gaussian initializations.
3. The frozen-bottom block has an elementary two-dimensional polynomial recursion, with initialization \(A,Z\) independent standard Gaussians after the first-layer Gram tends to one.
4. At \(2t\) steps, a surviving highest-degree output term has \(h\)-degree \(3(4^t-1)\) and even Gaussian powers \(4^t,2\cdot4^t\).
5. Its logarithm at \(h=\rho/t\), divided by \(4^t\), is bounded below by
\(t\log4-3\log t+O_{q,\rho}(1)\), which diverges. The cubic subtraction is only \(O(1/t)\).
6. Orthogonal sign conjugacies handle all signs of \(p,q\).

I checked the composition/deletion argument, exponent and parity recursion, Gaussian-moment bound, and sign conjugacies. The full-network width passage uses the fixed-program lemma and therefore the external probability dependency of §5.1. The separate direct quadratic width bridge explicitly says its stopped-coupling sections are not the sole accepted proof; its polynomial bad-event removal does not alone supply the missing good-event coupling.

This no-go does not contradict §5: a quadratic activation lacks bounded first derivative and linear growth. Nor does it prove the same statement for every signed polynomial or every smooth bounded-slope activation. [No-go proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_quadratic_l2_order5/UNIFORM_NO_GO_THEOREM.md:82), [all-order term](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_quadratic_l2_order5/UNIFORM_NO_GO_THEOREM.md:179), [probability bridge](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_quadratic_l2_order5/FIXED_H_QUADRATIC_WIDTH_LEMMA.md:25).

### 6.4 A norm no-go is not a trajectory no-go

Suppose
\(\|V\|_{\mathfrak X}=\sum_m w_m\|\mathcal D^mV\|_{p_m}\)
is a norm containing constants and a Gaussian atom \(X\), with
\(\|UV\|_{\mathfrak X}\le C_\times\|U\|_{\mathfrak X}\|V\|_{\mathfrak X}\).
Then \(w_0>0\), \(p_0<\infty\), and
\[
w_0\|X\|_{np_0}^n
\le \|X^n\|_{\mathfrak X}
\le C_\times^{n-1}\|X\|_{\mathfrak X}^n.
\]
Taking roots contradicts Gaussian moment growth. The proof does not depend on positive-order weights. It invalidates the specified same-space product architecture, not all reachable grammars, radius-loss scales, or scalar remainders. The source's noncommutative hybrid telescope is correct, but its uniform transported-defect hypothesis remains a separate obligation. [Norm theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_uniform_near_identity_l2/FINAL_RESOLUTION.md:260).

## 7. New audit objection: bounded-slope ladder stability

The later SUPER_T5_EFFECTIVE_REMAINDER improves on the older FINAL_AUDITED_STATUS: it claims exact fixed-nonzero-step outputs for a single \(C^\infty\), positive bounded-slope activation and a two-rate minimax lower bound. Its principal symbol and two-rate algebra distinguish an effective interval remainder from a literal fifth jet. The older FULL_L2_LIPSCHITZ_LADDER has an additional obsolete flattened-excess argument: Stein differentiation can increase the total displayed excess across several atoms. The later source uses marked groups and a six-family census to address that issue.

But both full-network promotions still use the same unproved continuity bridge. FULL_L2_LIPSCHITZ_LADDER Lemma 2.1 asserts a dimension-free expected-output Lipschitz estimate in
\[
d_1(\psi,\widetilde\psi)
=\sup_x\frac{|\psi(x)-\widetilde\psi(x)|}{1+|x|}
 +\|\psi'-\widetilde\psi'\|_\infty.
\]
Its proof claims every coupled state difference is bounded by
\(d_1P(1+\|a^0\|_n+\|u^0\|_n+\|W^0/\sqrt n\|_{\rm op})\).
This deterministic claim is false.

Here is an analytic audit witness; no experiment is involved. Use the lemma's smooth reference
\(\psi(x)=x+\arctan x\), let
\(\widetilde\psi_n=\psi+n^{-1/2}\), and choose deterministic initial data
\[
u^0=0,\qquad a^0=\sqrt n\,e_1,\qquad
M^0=W^0/\sqrt n=e_1\mathbf1^\top/\sqrt n.
\]
The energy argument of \(P\) is exactly \(3\), and \(d_1=n^{-1/2}\).

For the reference network, \(H=0,z=0\), so
\(b=M^\top(a\psi'(z))=2\mathbf1\) and the first bottom update is
\(u^+=4h\mathbf1\).
For the perturbed activation,
\(\widetilde H=n^{-1/2}\mathbf1\), \(\widetilde z=e_1\),
\(\psi'(1)=3/2\), and
\(\widetilde b=(3/2)\mathbf1\), giving
\(\widetilde u^+=3h\mathbf1\).
Therefore
\[
\|\widetilde u^+-u^+\|_n=|h|,
\]
while the claimed bound is \(n^{-1/2}P(3)\to0\).

This locates the illegal step: normalized \(L^2\) control of a slope difference and an unbounded readout does not control their coordinatewise product in normalized \(L^2\). Rank-one matrix bounds do not repair that product. The witness lies in the energy balls used in the proof; Gaussian initialization makes such concentrated states atypical, which is precisely why an additional probabilistic/higher-moment argument is needed.

**Scope of objection:** this disproves the stated deterministic majorant, not the expected-output lemma itself or the final counterexample theorem. A valid annealed continuity modulus might still be proved. It has not been supplied by these arguments, so the diagonal transfer of finite-truncation jets to one final activation is not certified here.

The historical LIMIT_AUDIT calls Lemma 2.1 repairable and repeats an unspecified polynomial difference recursion; that does not answer this witness. SUPER_T5 §3 repeats the same normalized-energy argument. I do not inherit those endorsements. I also did not independently verify the imported complete 1045-term transition map, so its arbitrary-background marked insertion lemma is an additional coefficient/proof dependency reservation.

[False deterministic majorant](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/FULL_L2_LIPSCHITZ_LADDER.md:103), [later stability claim](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/SUPER_T5_EFFECTIVE_REMAINDER.md:276), [two-rate transfer](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/SUPER_T5_EFFECTIVE_REMAINDER.md:311).

## 8. Mesh removal and general calculus: what survives

The minimal-bridge manuscript proves useful **conditional** implications:

- A shared \(t^4h^5\) scalar remainder gives a summable \(O(h)\) coarse/fine discrepancy at fixed total time, hence a scalar dyadic terminal limit.
- Uniform convergence of interpolated scalar paths additionally needs uniform time-increment control.
- State-level sewing requires a common reachable set, width-independent stability, and a summable propagated local defect.
- Identification of an IDE needs generator consistency and continuity; uniqueness/restart need estimates for the correlated state at restart, retaining the same immutable source.
- Passing from width-first Euler to finite-width continuous flow needs a separate width-uniform exact-flow/Euler comparison and UI for unbounded observables.

I checked the geometric-series scalar argument and discrete-Gronwall state proof. In the state theorem, applying the generator to the limiting curve requires that the solution domain contain the closure of the reachable tube, or that the uniformly continuous generator be extended to that closure. The source leaves this natural domain qualification implicit. This is a conditional sewing lemma, not verification of its hypotheses for generic nonlinear MFP. [Minimal bridge](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/CONTINUOUS_TIME_MINIMAL_BRIDGE.md:26).

The CFPC uniform Picard lemma is similarly sound under its explicit common-ball, uniform Lipschitz/size, finite-program convergence, and observable-continuity assumptions. Its factorial tail and three-limit triangle are not a proof that a nonlinear reused-source flow satisfies those assumptions. A countable present-time character is restartable only if its topology and retained joint source actions determine the future; process/projective consistency alone is not a semigroup proof. [Picard lemma](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/UNIFORM_FINITE_PROGRAM_COMPLETION.md:7).

Three newer general-calculus manuscripts were read in full:

1. **Gate-resolved increments.** The identity
\[
\Delta W_-=q_-\bigl(G(0)^*a+\tfrac12x\|a\|_n^2\bigr)
\]
is exact for fixed right input \(x\) and integrated covector \(a\). The recursive frozen-input block is a surrogate, not the simultaneous full-network update. Its source explicitly falsifies normalized-energy backward/reconstraint stability and uniform local tangency via spikes. Size \(O(h)\) does not imply a difference estimate. [Identity and boundary](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/GATE_RESOLVED_INCREMENT_CALCULUS.md:42), [counterexample](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/GATE_RESOLVED_INCREMENT_CALCULUS.md:310).
2. **Causal source compression.** Exact sequential two-sided Gaussian innovation identities survive. A fixed dictionary tolerance gives finite constants, but their growth as tolerance vanishes can overwhelm the Osgood modulus. Pivot-threshold ties, coupled stability, and Markov sufficiency after discarding the dictionary are additional gaps. The manuscript's concluding correction supersedes its optimistic opening. It does not approximate the unseen Gaussian block in operator norm. [Correction](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/CAUSAL_SOURCE_COMPRESSION_CALCULUS.md:1), [quantitative and autonomy gaps](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/CAUSAL_SOURCE_COMPRESSION_CALCULUS.md:428).
3. **Controlled contextual traffic.** Its source-aware perturbation cone, tangent/Hessian identities, and formal fixed-port counting are different from a proven finite-width occupation estimate. The uniform-port proposal is withdrawn; the finite-width response-tail/restart gate remains open. I did not read/reprove the subsidiary forest census, so I do not independently certify its formal fixed-port estimate. [Current gates](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/CONTROLLED_CONTEXTUAL_TRAFFIC_CALCULUS.md:228).

RCGC distinguishes exact compilation from proposed dynamic Gaussian promotion. Its dynamic low-influence and Osgood-tail bounds are targets, not established hypotheses. A centered same-source word with order-one glued width degree cannot be dropped merely because its factors are centered; conversely, such a word does not prove that an infinite traffic hierarchy is necessary. The syntax compiler expressly says it does not decide convergence. [Semantic levels](/home/amir/Codes/PDE/studies/renormalized_causal_gaussian_calculus/CALCULUS_SPECIFICATION.md:7), [promotion requirements](/home/amir/Codes/PDE/studies/renormalized_causal_gaussian_calculus/CALCULUS_SPECIFICATION.md:176), [compiler scope](/home/amir/Codes/PDE/studies/renormalized_causal_gaussian_calculus/compiler/README.md:1).

The inspected general languages therefore do not supersede specialized positive arctangent or deep-linear proofs with a general theorem. Those positive proofs are assigned elsewhere and were not re-audited here.

## 9. Nonlinear and joint-scaling contributions: narrowly stated

The two local loss-mesh manuscripts were read fully. Their strongest conclusions require separation:

- For normalized \(x^2/\sqrt3\), the width-first predictor initial-layer argument follows from §6.3 and monotonicity in a deterministic nonnegative feature-step schedule. Before the loss output first reaches \(0<\delta<1\), every effective feature step is at least \((1-\delta)h\). The positive feature-output lower bound forces that hitting time to zero. This rules out a continuous initialized predictor limit. The corresponding loss statement follows for loss evaluated on a continuous predictor interpolation; if loss values themselves are interpolated independently through overshooting steps, that convention needs separate checking.
- The full joint-width/mesh no-go is asserted only for diagonals resolving the finite-width ODE through its initial layer, with a displayed very small sufficient mesh. Its covariant-Schur finite-width initial-layer theorem and detailed polynomial constants are dependencies **not independently audited here**. Do not export this as failure of every under-resolved diagonal.
- For normalized hard ReLU, the explicit width-two gate has one-sided normal velocities \(3/8\) and \(-21/8\). I checked the attracting-gate obstruction to an ordinary fixed-gate-derivative ODE. The positive-probability tube is a fixed-width claim, not a width-uniform population obstruction.
- Frozen hard-Euler gate occupation has binary second moment equal to its occupation fraction, not the square of that fraction. A scalar averaged gate is therefore insufficient for squared-cotangent observables. This is not a proof that a generalized width-first Euler limit fails.
- The later synthesis adds local scalar ReLU tightness using deterministic energy and predictor-increment bounds; it does not establish uniqueness, a restartable generalized state, or a sufficient rate based only on \(nh_n\). I checked this compactness mechanism, not an optimized value of its coarse numerical time constant.

[Width-first quadratic schedule proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_loss_mesh_resolution/FULL_RESOLUTION_AND_JOINT_SCALING.md:95), [joint conditional boundary](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_loss_mesh_resolution/FULL_RESOLUTION_AND_JOINT_SCALING.md:164), [ReLU proof and compactness](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_loss_mesh_resolution/FULL_RESOLUTION_AND_JOINT_SCALING.md:231).

The scaling-comparison source was used as provenance plus a checkable coordinate calculation. It correctly gives effective mobilities \(nh,h,h/n\). A coherent neuron-embedded \(1/n\) connector has entry variance \(O(n^{-2})\) and a law-of-large-numbers field, unlike the original iid \(1/\sqrt n\) connector and conditional Gaussian field. Centering one-coordinate marginals does not make that coherent model iid. Its cited finite-type witness also starts at output \(1/2\), unlike the original \(f_n(0)\to0\). No primary nested-model proof was recovered, so no new positive theorem is certified from this comparison. [Coordinate comparison](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_scaling_comparison/INDEPENDENT_COMPARISON.md:17).

Dividing the optimizer by the tangent kernel gives the exact scalar equation \(\dot f=1-f\) where that division is valid. That is a changed optimizer/clock, not a proof of original-clock state convergence or nonlazy fitting. Making a separate width-dependent multiplier vanish can produce a frozen limit; reducing an Euler mesh alone does not slow the physical vector field.

## 10. Reading record and SHA-256 manifest

I personally read the solve-math-rigorously and investigate-conjectures skills, and the latter's evidence-ledger, adversarial-audit, and research-contract references in full. Their effect on this report is the separate claim/dependency ledger, source-amendment recovery, and the adversarial product-stability check. No experiment, agent orchestration, or resumed research was performed.

Manifest status:

- **F**: entire listed file read, including appendices. This is not a claim of independently rederiving every coefficient or accepting every claim in that file.
- **S**: scoped read, specified below.
- **P**: complete historical/secondary provenance file read; its verdict was not substituted for a proof.

Scoped entries: S33, historical probability audit, lines 1–365, including the all-orders theorem amendment; S34, TP III local text, lines 1860–2155 and Appendix N, lines 6183–6338, plus proof locators; S40, machinery-frontier synthesis, lines 1–280 only; S45, transcript full messages and earlier amendments enumerated in §2, not the full rollout. The external Non-Gaussian Tensor Programs theorem was browser-read at its primary URL; no downloaded byte hash is claimed.

The full local manuscripts supporting the principal recommendations are F02–F06, F09–F15, F20–F22, F29, F36–F39, and F42, with the external, coefficient-certificate, and conditional-theorem reservations stated above. F16 and F18 were read fully as earlier theorem statements/proof syntheses; their separately linked proof modules were not all read and are not independent certifications here. P23, P26, P32, and S33/S40 are provenance, even when their internal algebra was inspected.

Missing or deliberately unaudited: the four remote task histories and remote versions/hashes; complete external master-theorem proof chains; every scalar transition/certificate producer and full imported large-map data; general signed-polynomial extensions; the finite-width quadratic covariant-Schur theorem; arbitrary joint-diagonal full-network refinements; the original nested finite-type manuscript; CCTC subsidiary forest proofs; specialized positive global limits, Stieltjes verdicts, old ResNet, and deep-linear closure proofs assigned to other auditors.

No other new source-auditor report was read. Only this assigned new report was written.


| ID / read | Local file (line 1) | Lines | SHA-256 |
|---|---|---:|---|
| F01 | [studies/mean_field_peeling/CURRENT_RESEARCH_STATE.md](/home/amir/Codes/PDE/studies/mean_field_peeling/CURRENT_RESEARCH_STATE.md:1) | 2096 | 6b3d993c085127a77212549da673a92ddb771e14cf711d865c4d61e7dda35465 |
| F02 | [studies/mean_field_peeling/MUP_TRAINING_CASE_STUDY.md](/home/amir/Codes/PDE/studies/mean_field_peeling/MUP_TRAINING_CASE_STUDY.md:1) | 3522 | 4b9ffa05622ba38dbc4c290614f6eca58250e72a8f0a7b88379682a60cbb7e21 |
| F03 | [studies/mean_field_peeling/generic_first_stieltjes/depth/EXACT_FIXED_DEPTH_PROGRAM.md](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/depth/EXACT_FIXED_DEPTH_PROGRAM.md:1) | 294 | bc906ed8356d64f7cd5a54bb6042b78899e640b0379bffa8bb433e70f580e1c7 |
| F04 | [studies/mean_field_peeling/generic_first_stieltjes/depth/DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/depth/DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md:1) | 936 | 073ca6b4ad786b50a4a31f292afbb019e2e2ec98b00fe7feb00b7a4e9c8c1fc2 |
| F05 | [studies/mean_field_peeling/generic_first_stieltjes/depth_order5/primary/ARBITRARY_DEPTH_RECURSION.md](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/depth_order5/primary/ARBITRARY_DEPTH_RECURSION.md:1) | 303 | 4ae39e965fdee328149a5e147e33cb1fc646c6ed976d5f9eaa6c6bfd0517eb1c |
| F06 | [studies/mean_field_peeling/generic_first_stieltjes/depth_order5_scalar/ARBITRARY_DEPTH_B1_ORDER5_SCALAR_RECURRENCE.md](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/depth_order5_scalar/ARBITRARY_DEPTH_B1_ORDER5_SCALAR_RECURRENCE.md:1) | 828 | 24d9f63d79319b514969c0e1fe85608721f4c4033615810c93157631c3a30f12 |
| F07 | [studies/mean_field_peeling/temporary_depth_time_doubling/RESEARCH_CONTRACT.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/RESEARCH_CONTRACT.md:1) | 104 | de6c8cdeecde7a047eb5321d779fcc18de43b95045d9eff56f5bf0380ae9ec08 |
| F08 | [studies/mean_field_peeling/temporary_depth_time_doubling/RESEARCH_STATE.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/RESEARCH_STATE.md:1) | 120 | c0cf73cc4152186de4a8880a332e1acd02abb7dab1e64f53e97a654304d5fda0 |
| F09 | [studies/mean_field_peeling/temporary_depth_time_doubling/PROOF.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/PROOF.md:1) | 1011 | 88e6ebfe3dd5b67b01421448d15e1bfd49944b814dd6519212b4849fb7b0d991 |
| F10 | [studies/mean_field_peeling/temporary_depth_time_doubling/WIDTH_DEPTH_TIME.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/WIDTH_DEPTH_TIME.md:1) | 1321 | 57e123a02c28f034f86222330882cf997176b5721679233953330b44bd9bd149 |
| F11 | [studies/mean_field_peeling/temporary_depth_time_doubling/COMPILER_DEPTH_TIME.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/COMPILER_DEPTH_TIME.md:1) | 862 | a7fde275877801a4185fdfe048c94a2a1baee81b45b5b5c75b7a0f88851d663f |
| F12 | [studies/mean_field_peeling/temporary_depth_time_doubling/CUBIC_DEPTH_TIME.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/CUBIC_DEPTH_TIME.md:1) | 1700 | e61b02a8c8a06db7baefbaa9e02ec7b9bb73f09f18cc21cc17a49e8862958edc |
| F13 | [studies/mean_field_peeling/temporary_depth_time_doubling/OPERATOR_BRIDGE_CHECK.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/OPERATOR_BRIDGE_CHECK.md:1) | 237 | a1c8becfe90845b1b3c54be4a82b8109f09cff8ca3ec3c6c9da51346a8d7b071 |
| F14 | [studies/mean_field_peeling/temporary_depth_time_doubling/UNIFORM_L1.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/UNIFORM_L1.md:1) | 687 | 0be27a8851562cfe063d919581dc57cbdcdc5d6ca3053010b4ed70af545964e1 |
| F15 | [studies/mean_field_peeling/temporary_depth_time_doubling/CONTINUOUS_TIME_MINIMAL_BRIDGE.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/CONTINUOUS_TIME_MINIMAL_BRIDGE.md:1) | 450 | 4e03628179864e8eacb9b495189c345757a4cc68c0eddcb7f85851a374dacce3 |
| F16 | [studies/mean_field_peeling/temporary_general_depth_four_vs_two_bound/THEOREM.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_general_depth_four_vs_two_bound/THEOREM.md:1) | 488 | e03ecfd09aa4b930280845fc16f2ca7b19137b3b2334420f8d07362a80f02e3c |
| F17 | [studies/mean_field_peeling/temporary_general_depth_general_time_stepdoubling_bound/RESEARCH_STATE.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_general_depth_general_time_stepdoubling_bound/RESEARCH_STATE.md:1) | 117 | 1c52477560f9949c88c141ec854b0f729166000e900987bcecad959783c8ef13 |
| F18 | [studies/mean_field_peeling/temporary_general_depth_general_time_stepdoubling_bound/FIXED_T_THEOREM.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_general_depth_general_time_stepdoubling_bound/FIXED_T_THEOREM.md:1) | 165 | 3429e681e7dba384eecfab11d27033facc6b8c43024bbc61370472c44828da8b |
| F19 | [studies/mean_field_peeling/temporary_quantitative_width_first_bound_general_t/ALGEBRA_AND_OBSTRUCTION.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_quantitative_width_first_bound_general_t/ALGEBRA_AND_OBSTRUCTION.md:1) | 399 | 06a0df5f830070a150d7d002026776f67d2fbbfb041530ca13c95100bdf2b748 |
| F20 | [studies/mean_field_peeling/temporary_quadratic_l2_order5/UNIFORM_NO_GO_THEOREM.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_quadratic_l2_order5/UNIFORM_NO_GO_THEOREM.md:1) | 361 | fc3fb2b01b9611fd7e712a12fe55de9c071a281fafeb097864cdc78d679ab344 |
| F21 | [studies/mean_field_peeling/temporary_quadratic_l2_order5/FIXED_H_QUADRATIC_WIDTH_LEMMA.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_quadratic_l2_order5/FIXED_H_QUADRATIC_WIDTH_LEMMA.md:1) | 113 | 9a4067a8108965983bc6a3794b366e1bff683e7918e5d800b4582513578a9fb0 |
| F22 | [studies/mean_field_peeling/temporary_quadratic_l2_order5/FIXED_H_QUADRATIC_BRIDGE.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_quadratic_l2_order5/FIXED_H_QUADRATIC_BRIDGE.md:1) | 432 | 48d65aef3a0aa3fbaf5bbedbeac2e3be0fe67adaf3058ba8dd030cb566cf1f11 |
| P23 | [studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/FINAL_AUDITED_STATUS.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/FINAL_AUDITED_STATUS.md:1) | 190 | 4933ff0cdb94589c8abe4bb9bb26cb070e1c7e853a5c2ec4dfa74c6d767a8b68 |
| F24 | [studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/FULL_L2_LIPSCHITZ_LADDER.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/FULL_L2_LIPSCHITZ_LADDER.md:1) | 588 | f18e02ef0c43b64a44238f567e2979e015bc8515e461628cc6121efbee263db0 |
| F25 | [studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/SUPER_T5_EFFECTIVE_REMAINDER.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/SUPER_T5_EFFECTIVE_REMAINDER.md:1) | 417 | 857f77cf067ac9b25f9ddd64dda57dce8fb9d1aeb72ed07c251dcbd236efdebe |
| P26 | [studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/FULL_L2_LIPSCHITZ_LADDER_LIMIT_AUDIT.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/FULL_L2_LIPSCHITZ_LADDER_LIMIT_AUDIT.md:1) | 277 | 1b047c2a55db81d1c2a306f34ac70efadc59c4a707ce0a0ee0eaed677a5701f0 |
| F27 | [studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/general_t_transition_weights.py](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/general_t_transition_weights.py:1) | 216 | 86770841c42a672bbdaccd4324abc3418f9d9c8c05c8ff7764dacfb3e39b979c |
| F28 | [studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/audit_general_t_transition_map.py](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/audit_general_t_transition_map.py:1) | 217 | a8d5d8d4f2466d2f2e325e9bf0ca70daacbbbde88478dc016990d3118fdf68b5 |
| F29 | [studies/mean_field_peeling/temporary_uniform_near_identity_l2/FINAL_RESOLUTION.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_uniform_near_identity_l2/FINAL_RESOLUTION.md:1) | 510 | b14075fe58a5353e4bf46c7afd1ac6ac122dd8ffbbebcfdf2464e94617606355 |
| F30 | [studies/mean_field_peeling/temporary_loss_mesh_resolution/FINAL_X2_RELU_MESH_VERDICT.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_loss_mesh_resolution/FINAL_X2_RELU_MESH_VERDICT.md:1) | 371 | a32d762ae6f80597f065a25547e73387bc13d201c9285e263068c5c86342022f |
| F31 | [studies/mean_field_peeling/temporary_loss_mesh_resolution/FULL_RESOLUTION_AND_JOINT_SCALING.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_loss_mesh_resolution/FULL_RESOLUTION_AND_JOINT_SCALING.md:1) | 408 | 4de44bde79bb339e794b99bad1ccf22f4cc8f8a8b87104605b631e874fb351e7 |
| P32 | [studies/mean_field_peeling/temporary_scaling_comparison/INDEPENDENT_COMPARISON.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_scaling_comparison/INDEPENDENT_COMPARISON.md:1) | 258 | f3bef75f98319881775ce85e1c8f43d9f9c2ace7d402dec012e9107a56fb888f |
| S33 | [studies/mean_field_peeling/generic_first_stieltjes/PROBABILISTIC_BRIDGE_AUDIT.md](/home/amir/Codes/PDE/studies/mean_field_peeling/generic_first_stieltjes/PROBABILISTIC_BRIDGE_AUDIT.md:1) | 674 | 0028683036ace5ed54196f7acead6f68c2f42cd1cf3c4ef7b262cbc748c2b734 |
| S34 | [studies/mean_field_peeling/three_sample_self_contained/literature/yang_tensor_programs_iii.txt](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_self_contained/literature/yang_tensor_programs_iii.txt:1) | 6338 | 7da471803779bc2f584cf34b262b47d353ec98181c4ffaa88f4d18b2571648d7 |
| F35 | [studies/causal_flow_peeling_calculus/PROGRAM_CONTRACT.md](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/PROGRAM_CONTRACT.md:1) | 260 | e44b7899536c65c1398bbeb7f4c09e219998a13dce1e337b43ee81edf59fe7b4 |
| F36 | [studies/causal_flow_peeling_calculus/UNIFORM_FINITE_PROGRAM_COMPLETION.md](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/UNIFORM_FINITE_PROGRAM_COMPLETION.md:1) | 267 | ca246377a7ed85b5f20aa4fd9e557d98aae75de837725550ab4069793a00fdb5 |
| F37 | [studies/causal_flow_peeling_calculus/CAUSAL_SOURCE_COMPRESSION_CALCULUS.md](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/CAUSAL_SOURCE_COMPRESSION_CALCULUS.md:1) | 522 | d9e562508229d83b9d2c17e049596c38502559d3eafd88d3ca44ec73ba10aa8c |
| F38 | [studies/causal_flow_peeling_calculus/GATE_RESOLVED_INCREMENT_CALCULUS.md](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/GATE_RESOLVED_INCREMENT_CALCULUS.md:1) | 403 | 186ed87e4ed48487801075f59876bb757723ad4ae412dc510738d3aff842f681 |
| F39 | [studies/causal_flow_peeling_calculus/CONTROLLED_CONTEXTUAL_TRAFFIC_CALCULUS.md](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/CONTROLLED_CONTEXTUAL_TRAFFIC_CALCULUS.md:1) | 487 | 7e8a430416ef8923836bc2eace9b1398157fdb069118f4453633d4c9c3eee71c |
| S40 | [studies/causal_flow_peeling_calculus/MACHINERY_VERDICT_AND_PROOF_FRONTIER.md](/home/amir/Codes/PDE/studies/causal_flow_peeling_calculus/MACHINERY_VERDICT_AND_PROOF_FRONTIER.md:1) | 482 | d9485dc1a0bebb358c36868f5d92cfe47655f78dfe03f95aba21f37f9dc1c20c |
| F41 | [studies/renormalized_causal_gaussian_calculus/RESEARCH_CONTRACT.md](/home/amir/Codes/PDE/studies/renormalized_causal_gaussian_calculus/RESEARCH_CONTRACT.md:1) | 172 | ecee4e7c21ac9d132400ac3d3cdc9e14de36f4850ddb62486681652f03c5d3d3 |
| F42 | [studies/renormalized_causal_gaussian_calculus/CALCULUS_SPECIFICATION.md](/home/amir/Codes/PDE/studies/renormalized_causal_gaussian_calculus/CALCULUS_SPECIFICATION.md:1) | 362 | 6a1489764720e53c7b756c52a2224be6d971c68d2d92836299c5357145034240 |
| F43 | [studies/renormalized_causal_gaussian_calculus/SOURCE_MAP.md](/home/amir/Codes/PDE/studies/renormalized_causal_gaussian_calculus/SOURCE_MAP.md:1) | 48 | 456af688fb8dd7e3e5c1e8cbddd75daea7256961af037608446a65194aa88f47 |
| F44 | [studies/renormalized_causal_gaussian_calculus/compiler/README.md](/home/amir/Codes/PDE/studies/renormalized_causal_gaussian_calculus/compiler/README.md:1) | 16 | 5cd40566e8ef21b9e0597e122e7684db448a05e6bddcd19cfdb1735586a05a50 |
| S45 | [/home/amir/.codex/sessions/2026/08/04/rollout-2026-08-04T13-41-41-019fcc94-551d-7660-84a7-f240d3564575.jsonl](/home/amir/.codex/sessions/2026/08/04/rollout-2026-08-04T13-41-41-019fcc94-551d-7660-84a7-f240d3564575.jsonl:1) | 1722 | 3bde84756fb7c5118b8265cd51d2f675da62b589bf5d687435bb81ee225504f4 |
