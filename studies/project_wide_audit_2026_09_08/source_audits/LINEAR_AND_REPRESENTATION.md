# Linear limits and representation boundaries: independent source audit

Audit date: 2026-09-08. Scope: PDE #8 `01a02592-e627-7672-a2f7-ed654280a6e0`, #11 `01a01fcf-c121-7a41-860b-9a28453d6847`, #12 `01a02047-c7b7-7270-abb1-401d9d16f697`, and the linear strands of PDE-2 Operator 1 `01a03544-ddce-77a1-b5af-44df07c54f4b` and Operator 2 `01a044b8-39b5-7240-8406-c08a614deaa8`.

This is an independent proof/source audit, not resumed research. No experiments, tests, agent spawning, task messages, commits, branch changes, permission changes, or research-file edits were performed. Only this report was written. No other new source auditor's report was consulted. I read the solve-math-rigorously and investigate-conjectures skills myself, including the latter's evidence-ledger, adversarial-audit, and research-contract references, from `/etc/codex/skills`. Their claim-ladder and source-provenance rules determine the distinctions below.

## 1. Consolidation decision

**The latest fully read joint proof establishes L3, one sample. It does not establish arbitrary hidden depth and arbitrary fixed data.** The older arbitrary-depth claim was explicitly retracted; its replacement proves an internal deterministic path equation and leaves the general width bridge conditional. A later L3 amendment repairs exactly that depth. None of the audited linear manuscripts supplies the missing arbitrary-data theorem.

The strongest defensible claims are:

| Claim | Independent audit verdict | Exact boundary |
|---|---|---|
| L2 scalar spectral IDE | Proved under the stated Gaussian, one-sample, full-training assumptions | Width-first gradient-flow output/loss convergence on every compact physical interval; global limiting loss decay. Not an arbitrary-data or explicit joint-mesh theorem in this manuscript. |
| L3 operator IDE and exact-GD joint limit | Proved in the stated scope, with the explicit Euler interpretation in §3 below | Three hidden layers, four trainable maps, one unit input, one scalar label; Gaussian initialization; normalized mesh tending to zero; fixed compact physical horizons. |
| Arbitrary-depth rooted-path equation | Proved internally | Exact finite-width gradient identities and a globally well-posed deterministic candidate for every fixed depth, with limiting-equation loss decay. Identification for general depths above three is not proved in these sources. |
| Finite current-contraction scalar ODE no-go | Proved | Width-uniform, state-universal, bounded-degree complete-contraction coordinates; polynomial dynamics, or analytic germs around the zero network. |
| Bounded-current-contraction local PDE no-go | Proved | The same finite graph alphabet must encode the entire spatial profile and all its derivatives; finite-order polynomial/appropriately based analytic PDE and finite-jet output readout. |
| Branchwise bounded-filtration jet-encoder no-go | Separate dialogue-only argument; retain its explicit encoder assumptions | Exponential tagged-word capacity versus subexponential commutative jet capacity. Not a theorem about an output-only Gaussian trajectory or unrestricted PDEs. Formalization cautions in §5. |
| Strict classical compression originally requested in #8/#11 | Not settled by the operator positive | Those prompts expressly forbade hidden path/operator states, even if renamed fields. The later positive is valid under an operator/kernel contract. |
| Quadratic one-source attempt in #12 | Exact finite-width reductions; no positive-time compressed limit proved there | One-square Lax identities and a spectral-insufficiency witness survive. The QQ operator lift is explicitly left without well-posedness/identification. Later nonlinear strands are outside this audit. |

The number **3 is hidden depth, not the number of inputs**. The L3 network in the joint theorem is `aᵀRBx`, with two vectors and two matrices. Its `x` is the projected first-layer state for one sample, not a list of three training examples. Both the [joint model statement](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md:10) and the [arbitrary-depth model statement](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/arbitrary_depth_autonomous_mse_closure/CANONICAL_NOTE.md:17) are explicit.

## 2. Exact model, clocks, and observable contract

For the general one-sample linear chain, hidden depth is L, with L+1 trainable maps and L−1 square middle matrices. The input has unit Euclidean norm, there are no biases, all hidden widths equal n, and all normalized initial entries are mutually independent N(0,1/n). With normalized parameters Θ,

\[
f_n=W_{L+1}\cdots W_1x_{\rm input},\qquad
\mathcal L_n=(y-f_n)^2,\qquad
\dot\Theta=2\eta(y-f_n)\nabla_\Theta f_n,
\quad\eta>0.
\]

Writing each raw map as \(\widetilde W=\sqrt n W\), the output has raw prefactor \(n^{-(L+1)/2}\), and raw Euclidean mobility is **nη**. Thus \(\dot{\widetilde\Theta}=-n\eta\nabla_{\widetilde\Theta}\mathcal L_n\). For half-squared loss the factor 2 disappears. These are concrete coordinate/clock conventions, not an invocation of every model called μP. See [normalization derivation](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/arbitrary_depth_autonomous_mse_closure/CANONICAL_NOTE.md:58).

Feature time s deletes the common multiplier: \(d\Theta/ds=\nabla f_n\), with \(ds/dt=2\eta(y-f_n)\). This geometric scalar-clock reduction depends on having one output-gradient direction. For an averaged multi-sample loss the actual vector field instead contains \((2\eta/m)\sum_i e_i\nabla f_i\); its kernel is a matrix. Merely replacing the label by a vector does not prove the same scalar-clock argument. The canonical note itself states this [one-sample restriction](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/arbitrary_depth_autonomous_mse_closure/CANONICAL_NOTE.md:149).

The joint theorem controls f, the tangent kernel K, and squared loss uniformly in probability on [0,T] for each fixed T, plus each fixed finite family of current rooted-word/finite-rank contractions. This is pointed/action-observable identification. It is not literal trace-norm convergence of the initialized n-dimensional bulk matrices to an infinite matrix, nor uniform control over all word degrees, arbitrary coordinatewise nonlinear probes, increasing depth, or T→∞ together with n.

All four L3 blocks train. At initialization each block's squared feature-gradient norm tends to one, so K(0)=4 and nonzero labels give nonvanishing normalized block velocities. The source has evolving operator corrections and an evolving kernel; it is not a frozen-readout construction. Nevertheless the input-output function remains linear in the input. The theorem cannot certify nonaffine activation effects. At y=0 the deterministic limit is stationary; nontrivial feature-learning claims must exclude that case.

## 3. L3 positive: the bridge is a proof, not just jet matching

Primary source: [JOINT_DEEP_LINEAR_THEOREM.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md:1), read in full, 1,065 lines, SHA-256 `ca3407d83f19faa857307c976d680b4c5b97f90901fd5faf48920d2f9e20d799`. This matches the hash preserved in Operator 1's [2026-08-28 final](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR1_FINALS.txt:15898), so that historical version association has evidence beyond a shared pathname.

The decisive steps check as follows.

1. **Exact cyclic gradient algebra.** On \(\mathbb R\oplus(\mathbb R^n)^3\), put the blocks x, B, R, aᵀ successively around a four-cycle C. Direct block multiplication gives \(C_s=(C^*)^3\), \(f=\operatorname{Tr}(C^4)/4\), and \(K=\|(C^*)^3\|_{\rm HS}^2=f_s\). Each length-three cyclic path includes an endpoint map of rank one, so rank(C³)≤4. The four contributions to K are exactly \(\|RBx\|^2+\|a\|^2\|Bx\|^2+\|R^*a\|^2\|x\|^2+\|B^*R^*a\|^2\). The balancedness/self-commutator identity also checks. [Finite-width proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md:124).

2. **Actual initialization source.** The fixed Fock construction uses \(b=\ell_1+\ell_2^*\), \(r=\ell_3+\ell_4^*\), and independent tail sectors \(\xi_x=\ell_5\Omega\), \(\xi_a=\ell_6\Omega\). Matrix words preserve the final tail letter, giving identical same-root moments and zero cross-root moments. The real form is explicit, so adjoints represent real transposes. All four annihilation choices, including those for adjoint letters, are present in the corrected text. [Lemma 3](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md:416).

3. **Fixed-word Gaussian convergence.** The manuscript supplies its own Wick proof. For a paired trace word with 2q entries and v free indices, the power is \(n^{v-q-1}\). The quotient graph is connected with q edges, hence v≤q+1. Equality is the tree case: the closed boundary traverses each tree edge in opposite directions, yielding nested/noncrossing compatible pairings. These are the Fock vacuum contractions. Joining two trace polygons loses at least one power after the two trace normalizations, sufficient for variance tending to zero. Independent normalized Gaussian roots then have conditional quadratic/bilinear variances bounded by \(2\|T\|^2/n\) and \(\|T\|^2/n\). The finite-net bound on each initialized Gaussian matrix supplies uniform high-probability norms. This only requires fixed words, not strong convergence for growing polynomials.

4. **Global internal flow and legitimate traces.** C=C₀+Q, with Q trace class. Since C₀³ is finite rank, every term of \((C_0^*+Q^*)^3\) is trace class. Telescoping and the trace-ideal inequality give local Lipschitz continuity of the coupled Q,e equation. The cyclic subspace remains invariant. All traces are ordinary Hilbert-space traces of trace-class operators, not normalized bulk traces or the vacuum trace. The exact energy law and finite-rank estimate give

   \[
   (e^2)_t=-4\eta e^2K,\qquad
   \|Q(t)\|_1\le 2|y|\sqrt{\eta t}.
   \]

   Thus there is no finite-time escape, and uniqueness supplies restartability. [Existence and energy proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md:564).

5. **Width identification.** After a cutoff outside the common energy ball, finite and limiting equations have dimension-independent bounds and Lipschitz constants. Every fixed Picard iterate is a finite sum of rooted rank-one word operators. Multiplication appends fixed source letters or contracts root pairs; it introduces no unaccounted direction at that fixed iteration depth. Its coefficients, traces, and trace norm depend continuously on a finite Gram matrix: for \(A=\sum c_{ij}|u_i\rangle\langle v_j|\), nonzero singular values come from \(G_u^{1/2}CG_v^{1/2}\). The common factorial Picard remainder then permits iteration depth first, width second, and finally removal of the Picard error. This is the positive-time bridge absent from the old arbitrary-depth sketch. [Full argument](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md:634).

6. **Joint exact-GD diagonal.** The simultaneous parameter step is exactly Euler for the **single Q equation** with \(e(Q)=y-\operatorname{Tr}(C_0+Q)^4/4\). This distinction matters: exact GD is not simultaneous Euler for the separately adjoined residual ODE. On the common ball, the manuscript's trace readout bound makes e(Q) Lipschitz, so the Q-only vector field has the dimension-independent local-error and stability bounds used in §7. With the cutoff equal to one on a ball strictly larger than the energy bound, the actual Euler path stays inside it for sufficiently small δ. Therefore its error is O_T(δ), uniformly in n. Combining with step 5 proves every deterministic diagonal δₙ→0. [Exact update and Euler estimate](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md:759).

There is a minor exposition ambiguity in “the same cutoff” in §7: §6 used the augmented (Q,e) system. The Q-only reading above is required and directly justified by the existing equations; it is also explicitly recorded in the preserved [earlier review](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR1_REVIEWS.txt:24744). I do not identify this as a missing theorem-level bridge. The raw-coordinate multiplier is nηδₙ; requiring that multiplier itself tend to zero imposes nδₙ→0, an additional convention, not a requirement of the normalized theorem.

The equivalent central representation uses two free MP(1) sources X,Y, two orthogonal root copies, two vectors z,p, and a self-adjoint trace-class correction S:

\[
z_s=(I+X+hI+S)p,\quad
p_s=(I+Y+hI+S)z,\quad
h_s=2\langle z,p\rangle,\quad
S_s=|z\rangle\langle p|+|p\rangle\langle z|.
\]

The positivity lift through actual factors verifies \(L,M\ge(1+h)I\). In physical time, e retains its sign, f=y−e moves toward y, h≥0, and K≥2|f|. Since \(\dot f(0)=8\eta y\), for y≠0 the kernel is bounded below after a positive transient and the limiting loss decays to zero. This is global fitting for one label in the limiting system, not a uniform width/time theorem. [Central reduction and fitting](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md:804).

**External dependency boundary.** I read the entire historical unfrozen-readout manuscript as well. It invokes Xiang–Zhang Theorem 3.3. I did **not** independently read that preprint's full theorem/proof chain or the cited Brailovskaya–van Handel/Anderson research proofs in this audit. Their historical CLEAN labels are provenance only. The positive verdict here rests on the replacement Gaussian proof above, not that unaudited invocation. The latest manuscript expressly removes it as a dependency [at lines 1041 onward](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md:1041).

## 4. What the scalar and PDE no-go theorems actually prove

For C=BᵀRᵀRB, let \(\Gamma_m=x^TC^mx\). Keeping just endpoint differentiation gives

\[
\mathscr D_0^{2m-1}f
=4^{m-1}\{x^TC^mx+a^T(RBB^TR^T)^ma\}.
\]

Every coefficient in the full feature derivation is nonnegative, so Γₘ survives with positive coefficient in \(\mathscr D^{2m-1}f\). It is a connected contraction graph of tensor degree 4m+2. A finite list of contraction coordinates contains only finitely many connected graph types. Multiplying those coordinates forms disjoint unions and cannot create a new connected Γₘ. Stable-width graph independence converts this into a contradiction. The proof of independence is valid when graphs are understood as typed incidence contractions, modulo the stated type-preserving isomorphisms; the later PDE manuscript explicitly supplies the quotient-closed auxiliary graph class needed for its injective-labeling proof. [Scalar ladder](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md:211), [corrected independence proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_pde_no_go/PDE_CLOSURE_BOUNDARY.md:167).

The PDE theorem retains this argument because its encoder is

\[
U_{\alpha,n}(\zeta;\theta)
=\sum_{G\in\mathcal G_D}c_{\alpha,G,n}(\zeta)P_G^{(n)}(\theta),
\]

with a **uniform finite tensor-degree bound D**. Spatial derivatives only differentiate c; they never enlarge the graph alphabet. Evolutionary prolongation expresses every successive time derivative of the finite-jet readout as a polynomial in spatial jets from that same alphabet. Arbitrarily increasing spatial differentiation order therefore does not evade the proof. Smooth state-independent coefficient functions may even depend on n. [Encoder and readout assumptions](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_pde_no_go/PDE_CLOSURE_BOUNDARY.md:57), [prolongation proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_pde_no_go/PDE_CLOSURE_BOUNDARY.md:281).

The polynomial identities may initially hold on any nonempty open network-state set, because polynomial continuation then makes them identities. For analytic PDE/readout germs the manuscript requires a full neighborhood of the **zero network**, with analytic domains containing the realized zero-network jet tuples. Recentring every tuple before tensor scaling ensures that only finitely many Taylor monomials contribute at a fixed tensor degree. An arbitrary analytic germ along the Gaussian orbit is not covered. [Analytic proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_pde_no_go/PDE_CLOSURE_BOUNDARY.md:370).

The extension to physical loss flow also checks, including y=0. For y≠0, the lowest-degree part of \(\mathscr X^k f\) is \((2\eta y)^k\mathscr D^k f\); the −f factor raises degree further. For y=0, \((f\mathscr D)^k f\) contains \(f^k\mathscr D^k f\) with positive coefficient, so a Γₘ connected component still survives. The y=0 Gaussian limit being stationary is irrelevant to this state-universal assertion. [Physical-flow argument](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_pde_no_go/PDE_CLOSURE_BOUNDARY.md:398).

The theorem does **not** exclude every finite scalar ODE, arbitrary nonlinear encoders, a specially fitted orbit equation, width-dependent state sizes, or a fixed number of infinite-dimensional fields. It also is not a no-approximation theorem. The phrase “bounded-degree polynomial PDE” is inadequate unless the bound on **encoded dependence on current tensors** is retained.

The transport counterexample is valid in its stated output-semiconjugacy sense. For physical finite-width flow Ψ, set \(E_n(\theta)(s)=f_n(\Psi_n^s\theta)\), s≥0. The same energy estimate proves global forward physical flow. Then U(t,s)=Eₙ(θ)(t+s) solves Uₜ=Uₛ and U(t,0) is the output. It is autonomous and restartable, but initializes from the whole future-output profile. Thus it refutes a no-PDE assertion with unrestricted encoders while **failing the original no-playback/source-provenance requirement**. Feature-time flow only gives a local germ; the manuscript correctly separates this from the global physical half-line construction. [Counterexample proof](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_pde_no_go/PDE_CLOSURE_BOUNDARY.md:435).

The quantitative jet-complexity conclusion also needs its own width-uniform local-finiteness assumption. At jet cutoff ρ+(2m−1)r, a graph Γₘ of degree 4m+2 must already occur in a participating jet. It is not an unrestricted lower bound for arbitrary real-valued field encodings. [Exact condition](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_pde_no_go/PDE_CLOSURE_BOUNDARY.md:604).

## 5. The branchwise argument is a different result

The complete argument occurs in #8's [final message, rollout line 7221](/home/amir/.codex/sessions/2026/08/21/rollout-2026-08-21T20-26-19-01a02592-e627-7672-a2f7-ed654280a6e0.jsonl:7221), which I read in full. Searches of the assigned linear source directories found no separate manuscript containing this bounded-filtration/Hilbert-series proof. It must not be cited as though it were Theorem 1 of the later joint file.

Its target is the **complete tagged derivative/continuation grammar**, with an encoder linear on tagged branches, faithful to later scalar Wick contractions, and sending derivative-depth r branches to differential-polynomial weight at most C₀+C₁r. Coefficients belong to a fixed finitely generated graded algebra; arbitrary source functions encoding the word tree are excluded.

The core algebra is persuasive under that contract:

- The endpoint-only contribution to \(z^{(2m)}(0)\) is \([(I+X)(I+Y)]^mz_0\). Selecting X or Y from each pair yields every binary word of length m, hence 2ᵐ tagged branches.
- If \(P(X,Y)z_0=0\), faithfulness and the full support projection of the MP(1) variable X imply P=0. The algebraic free-product reduced-word decomposition makes distinct noncommutative monomials independent. Thus their rooted Gram matrix is positive definite.
- The central Leibniz contribution to \((\|z\|^2)^{(4m)}\), with both sides tagged, contains all these Gram pairings. If the encoder must preserve these tagged contraction contexts, it cannot identify any nonzero combination of the 2ᵐ branches.
- With B fields in d commuting source coordinates and jet weight 1+|α|, the number of jet generators at weight k is O(k^{d−1}). The weighted commutative polynomial algebra has cumulative dimension at most \(\exp(O(N^{d/(d+1)}))\); finitely many positive-weight coefficient generators do not change subexponential growth. Weight N=O(m) cannot contain 2ᵐ independent elements.

Two formalization cautions prevent treating the message as a broader manuscript theorem. First, “finitely generated graded coefficient algebra” must have locally finite weight spaces (in particular no freely variable degree-zero coefficient generator whose uncharged powers have infinite dimension). Otherwise the displayed Hilbert-series capacity bound does not follow. Second, access to every **separately tagged** Gram context is an encoder requirement, not something forced by accurately evolving the single untagged loss curve. Those contexts and the admissible evaluation map should be defined before attaching an unconditional theorem label to an encoder class.

I retain this as an exact-under-the-stated-faithfulness-and-filtration argument, with the grading qualification made explicit. It does not establish an output-only, arbitrary analytic, nonlocal-integral, or operator-encoder impossibility. The L2 comparison has only the one-source powers 1,C,…,Cᵐ; the exponential argument does not exclude its spectral field. The later bounded-current-contraction PDE theorem neither proves nor contradicts this stronger but differently scoped tagged statement.

## 6. Arbitrary depth: actual proof and actual gap

I read both the 582-line archived [THEOREM_AND_PROOF.md](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/arbitrary_depth_autonomous_mse_closure/THEOREM_AND_PROOF.md:1) and the complete 1,043-line [CANONICAL_NOTE.md](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/arbitrary_depth_autonomous_mse_closure/CANONICAL_NOTE.md:1).

The internal proof is sound. The fixed path edge operators have norm at most two. At every fixed L, forward and backward features are finite products of bounded source operators plus Hilbert–Schmidt trained increments. The vector field is locally Lipschitz, and its squared gradient norm is exactly

\[
K=\|b_0\|^2+\|a_{L-1}\|^2+
\sum_{j=1}^{L-1}\|b_j\|^2\|a_{j-1}\|^2.
\]

Loss dissipation bounds every trained block's displacement by |e(0)|√(ηT), preventing finite-time escape. For y≠0, let g=sgn(y)f and let q be either common endpoint squared norm. Then K≥2g²/q, dq/dg=2g/K≤q/g. After any t₀>0, g(t₀)>0 and q/g is nonincreasing, so K has a positive lower bound and the residual decays exponentially. This proves the behavior of the deterministic equation, independently of a width interpretation. [Global proof](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/arbitrary_depth_autonomous_mse_closure/CANONICAL_NOTE.md:844).

The missing bridge is not hidden: [§6](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/arbitrary_depth_autonomous_mse_closure/CANONICAL_NOTE.md:446) requires quantitative multi-edge rooted-word Gram and forward/transpose action estimates, and a compatible trained-block lift. [§9](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/arbitrary_depth_autonomous_mse_closure/CANONICAL_NOTE.md:756) leaves the lift/leakage and varying-space Picard identification conditional. A common energy ball supplies stability; it does not by itself supply the missing source comparison.

The note's opening amendment repairs L=3 using the separate cyclic/free-Wishart proof. Its older body still says “L≥3 conditional” in several places; that is stale for exactly L=3, not evidence against the later proof. For **L>3**, this source set still does not contain a written positive-time identification, let alone an arbitrary joint-mesh/arbitrary-data theorem. An apparent route for extending the later argument is not a completed proof, and no such extension was attempted in this audit.

I also checked the external primary source, [Chizat–Colombo–Fernández-Real–Figalli, author-hosted PDF, §6, pp. 37–42](https://people.math.ethz.ch/~afigalli/papers-pdf/Infinite-width-limit-of-deep-linear-neural-networks.pdf#page=37), at the scope statement and the displayed multi-layer construction. It explicitly calls those arguments formal and assumes the multi-edge bases/action relations. Its L counts middle matrices, so its L=1 is this project's two-hidden-layer case. I have not independently audited that paper's core general-data theorems and proof chain; they are not used here to promote a local arbitrary-data claim. This scoped primary-source check concerns the status of §6, not an endorsement of every result in the paper.

## 7. L2: a genuine spectral field closure, with a different source

The 570-line [L2 theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/depth2_autonomous_mse_closure/THEOREM_AND_PROOF.md:1) was read in full. For normalized f=xᵀBy, the conserved quantities are C=BBᵀ−xxᵀ and δ=∥x∥²−∥y∥². Therefore

\[
x_{ss}=(C+2r-\delta)x,\quad r=\|x\|^2,\quad f=r_s/2.
\]

Diagonalizing C gives an exact finite-width oscillator with a 2×2 rooted spectral measure. Conditional Gaussian concentration, the square MP limit, the Gaussian top-eigenvalue bound, and Sherman–Morrison identify its diagonal limiting measures ρₓ,ρᵥ and a vanishing cross measure. I checked the −1/2 pole and residue 3/4: with the convention m(z)=∫(z−λ)⁻¹dρ_MP, z=1/[m(1−m)], m(−1/2)=−1, and m/(1+m) has residue 3/4. The scalar source is

\[
d\nu=\tfrac34\delta_{-1/2}
+\frac{(1+\lambda)\sqrt{\lambda(4-\lambda)}}{\pi(1+2\lambda)}
\mathbf1_{(0,4)}d\lambda.
\]

It packages two real channels into ψ,π, with \(r=\int|\psi|^2d\nu\), \(K=\int(|\pi|^2+(\lambda+2r)|\psi|^2)d\nu\), and \(\dot\psi=2\eta e\pi\), \(\dot\pi=2\eta e(\lambda+2r)\psi\), \(\dot e=-2\eta eK\). The initialization is the explicit α,iβ in the source, not a curve-fitted measure.

Weak convergence of the rooted spectral measures on a common compact interval and a finite uniform net for the compact family of mode functions justify the uniform source error in [§5](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/depth2_autonomous_mse_closure/THEOREM_AND_PROOF.md:360). Grönwall then removes the stopping time. The feature solution satisfies r≥1 and rₛₛ≥3r² for s>0; bounded r would keep its linear mode equation bounded, so any finite maximal endpoint has r and then F diverging. This validates the range/clock argument and global physical-time fitting. Negative labels follow by the stated symmetry. No all-order Stieltjes positivity is used.

The classical random-matrix inputs are correctly specialized: square aspect ratio one, centered independent variance-1/n Gaussian entries, finite fourth moment, and independent Gaussian endpoint vectors. These classical MP/top-eigenvalue results were not re-proved or re-read from the original papers; their required hypotheses and use were checked. The negative support point of ν is not a negative mass and is unrelated to the proposed nonnegative Stieltjes representation of transformed output-kernel coefficients.

Two nearby sources do not enlarge this to arbitrary input data. The [multi-output aggregate note](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/depth2_multioutput_average_closure/RESULTS.md:119), read in full, trains the loss of a fixed aggregate of output heads. It explicitly excludes generic vector MSE [at its boundary](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/depth2_multioutput_average_closure/RESULTS.md:258). The [frozen-readout L3 statement](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/depth3_frozen_readout_closure/THEOREM_AND_PROOF.md:16), checked only through line 125, freezes A and reduces to L2. Its initial K is 3, whereas fully trained L3 has K=4. I do not present that scoped reading as an audit of the full frozen-readout proof.

## 8. Quadratic attempt: retain its reductions, not a limit theorem

I read the entire 325-line [THEOREM_AND_AUDIT.md](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/THEOREM_AND_AUDIT.md:1), its full protocol, the full order-17 results note, the 256-line recurrence code, and the partial-activation tests. No code was executed.

This model uses normalized inner product n⁻¹vᵀw, raw order-one Gaussian coordinate vectors, G=W/√n, and feature derivation n∇f·∇. Squares are raw coordinatewise squares, not normalized Hermites or z²/2. Its physical multiplier remains 2ηe. This distinction is necessary before transferring coefficients from other quadratic strands.

The finite-width algebra checks:

- Inner square/outer identity: X=u², Z=GX, R=G* A; Aₛ=Z, Xₛ=4X⊙R, Gₛ=A⊗X. For Q(c,v)=cA+Gv and its boost Sₓ, Qₛ=QSₓ and L=JQ*Q obeys Lₛ=[L,Sₓ].
- Inner identity/outer square: B=A⊙Z, R=G*B; Aₛ=Z², Xₛ=2R, Gₛ=2B⊗X. The other block Gram gives Lₛ=2[L,S_B].
- Both square: Xₛ=8X⊙R and Gₛ=2B⊗X, with the exact K containing the three terms shown in the source and physical equations [at line 221](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/THEOREM_AND_AUDIT.md:221). Direct differentiation gives both raw row/column balance laws. Coordinate-dependent boosts defeat that particular common-Gram Lax construction; they do not exclude all possible Lax forms.

The same-spectrum/same-output witness is valid with the normalized inner product: X=(1,2,3), r₁=(1,0,0), r₂=(1/3,−2/3,2/3), g=1/3. Both r's have squared normalized norm g and equal output 1/3, but \(\langle Xr_1^2,1\rangle_n=1/3\) and \(\langle Xr_2^2,1\rangle_n=7/9\). The Gram operators are orthogonally conjugate while the corresponding K differs. Thus eigenvalues plus the stated marginal/output do not determine the instantaneous vector field. [Witness](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/THEOREM_AND_AUDIT.md:95).

The [stored QI shifted 4×4 determinant](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/PARTIAL_ORDER17_RESULTS.md:51) is strictly negative as printed. Conditional on the listed μ₁,…,μ₇ being the actual coefficients, this excludes a nonnegative Stieltjes source: its shifted moment matrix would be ∫λv(λ)v(λ)ᵀdρ≥0. I inspected the exact-fraction recurrence and stored controls, but did not independently regenerate the order-17 coefficients, check that large determinant arithmetically, or prove the full Gaussian detransposition theorem behind the code. Accordingly this certificate remains a **reported fixed-order computational negative**, not a newly certified principal theorem of this audit. The current tests fix QI/IQ through order nine and QQ through thirteen; they do not themselves certify the QI order-seventeen gate. IQ's finite positive gates do not establish all-order positivity.

The source explicitly leaves two substantive obligations for QQ: an admissible classical source/field realization, and real positive-time well-posedness plus compact-time width identification. A formal traffic/Fock lift closes neither. [Unresolved bridge](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/THEOREM_AND_AUDIT.md:287). This describes #12's result, not a verdict on later nonlinear work assigned to the root reviewer.

There is also a historical statement requiring correction: #12's [user turn at line 6492](/home/amir/.codex/sessions/2026/08/20/rollout-2026-08-20T19-46-10-01a02047-c7b7-7270-abb1-401d9d16f697.jsonl:6492) says both linear and quadratic models have zero Taylor radius. That is not a theorem source. The identified L2/L3 linear equations have bounded fixed sources and polynomial Banach-space vector fields, hence positive local analytic radius by the local analytic-ODE/majorant argument. Feature-time finite blow-up does not mean zero local radius. Conversely a divergent formal quadratic jet does not exclude an unbounded-source IDE with a well-defined real-axis evolution, and alone does not identify an actual positive-time loss curve.

## 9. Supersession and provenance recovered from older turns

1. **#11 initially overclaimed arbitrary depth.** The [2026-08-20 response at rollout line 6724](/home/amir/.codex/sessions/2026/08/20/rollout-2026-08-20T17-35-04-01a01fcf-c121-7a41-860b-9a28453d6847.jsonl:6724) explicitly asserted compact-time convergence at every fixed depth and claimed its local proof supplied the missing published steps. The currently archived manuscript retracts that claim in its opening correction; the complete canonical replacement exposes the missing lemmas. I checked those passages and the [75-line supervisory provenance record](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/arbitrary_depth_autonomous_mse_closure/SUPERVISORY_AUDIT.md:10). The earlier response and test passes do not override the retraction.

2. **The strict compression contract was changed, not automatically solved.** #11's [line 7897 user prompt](/home/amir/.codex/sessions/2026/08/20/rollout-2026-08-20T17-35-04-01a01fcf-c121-7a41-860b-9a28453d6847.jsonl:7897) forbids path-space/hidden operator states even if called fields. The [final at 8369](/home/amir/.codex/sessions/2026/08/20/rollout-2026-08-20T17-35-04-01a01fcf-c121-7a41-860b-9a28453d6847.jsonl:8369), read in full, leaves that problem open while giving specific spectral/modal obstructions. #8 inherits a similarly explicit [contract at 6289](/home/amir/.codex/sessions/2026/08/21/rollout-2026-08-21T20-26-19-01a02592-e627-7672-a2f7-ed654280a6e0.jsonl:6289). The operator positive establishes a different admissible representation. Ordinary marginal spectra still fail: free moments τ(X²Y²)=4 and τ(XYXY)=3 disagree with commuting multiplication, and the joint manuscript's finite-state spectral examples give unequal K at equal spectral summaries. These are representation-specific failures, not a universal scalarization impossibility.

3. **#8's late branchwise theorem is separate.** Its complete final at 7221 adds the tagged capacity argument discussed in §5. It does not contain the later PDE-current-contraction proof, and neither should be described as merely the other theorem with different wording.

4. **Operator 1 strengthens the L3 operator result to a joint diagonal.** I read the complete relevant preserved chronology block, lines 22801–22916, including the Aug. 28 request, source recovery, Gaussian-source amendment, final hash, and subsequent PDE repairs. [Chronology start](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR1_CHRONOLOGY.txt:22801). The principal theorem is the fully read local hash-matching manuscript, not its historical audit labels.

5. **PDE closure boundary survives an interrupted task.** The preserved Operator 1 app page identifies the PDE follow-up turn `01a0497c-1770-78d0-b74b-84b633de4dcd` as interrupted, while its chronology records the corrected manuscript and clean intermediate audits. It has no later final in the exported finals file. That is a task-completion/provenance limit; the actual 654-line manuscript can still be independently checked, as it was here. The repairs—η>0, quotient-closed incidence graphs, analytic basepoints, local feature germs versus global physical flow—are actually present. No claim depends on assuming a missing final round completed.

6. **Operator 2 is not evidence of a broader linear theorem.** I searched its entire preserved chronology/finals for the linear, arbitrary-depth/data, joint-limit, and no-go strands, examined the app-page task/turn metadata, and read the relevant linear-reference context [at chronology line 18519](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR2_CHRONOLOGY.txt:18519). Its stronger general-data and L3 discussions concern nonlinear constructions; those are outside this source group's proof verdict. Shared inherited text in Operator 1/2 is not independent replication.

The local session index resolves #11 to **Deep Closure — Linear Depth L≥2 Program**; “Work” is not an additional mathematical source task. The preserved Operator app pages identify host `remote-ssh-discovered:black-chatgpt-2` and the exact Operator 1/2 titles. The metadata SQLite was queried only with `mode=ro`: it confirms both IDs and their private rollout paths under `/home/codex-b/.codex/sessions/`, but its `title` is the initial user prompt. UI title, initial-prompt metadata, and mathematical theorem scope are separate facts.

Private PDE-2 rollouts were not read or rehashed. Their hashes in the preservation manifest are **reported provenance**, not my independent verification. The apparent `/home/amir/Codes/PDE` path on both hosts is not a version identity proof. For the joint and PDE-boundary manuscripts, independently computed local hashes match the preservation manifest; for other local studies without that historical link, my mathematical verdict applies to the exact local bytes below. No live task-read tool was callable in this isolated tool set; preserved app pages and exports were used instead.

## 10. Reading and hash register

“Full” means I read the entire identified file, including its proof and final scope discussion. “Scoped” means only the stated portions/locators; no full-proof endorsement is inferred. All SHA-256 values below were computed in this audit, except the separately identified private-rollout hashes in the source manifest.

| Source | Reading scope | SHA-256 |
|---|---|---|
| [Joint L3 theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md:1) | Full, 1,065 lines | `ca3407d83f19faa857307c976d680b4c5b97f90901fd5faf48920d2f9e20d799` |
| [PDE boundary](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_pde_no_go/PDE_CLOSURE_BOUNDARY.md:1) | Full, 654 lines | `cc8b6fa5c8084ed69d56c794214edb5c14d8208801e47aab2fb4a5d5715bcd2e` |
| [L2 spectral theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/depth2_autonomous_mse_closure/THEOREM_AND_PROOF.md:1) | Full, 570 lines | `0a18f1badd4a9412886f08118e0d0ea8a6cfac06fda118edba848e2ca15c1430` |
| [L3 unfrozen theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/depth3_unfrozen_readout_closure/THEOREM_AND_PROOF.md:1) | Full, 985 lines; old external invocation unaudited | `21a1b3f2e3b7b12988b0bdc104fe7d2a2fb726a4ba79fb679d761ef13aa814e0` |
| [Arbitrary-depth archived attempt](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/arbitrary_depth_autonomous_mse_closure/THEOREM_AND_PROOF.md:1) | Full, 582 lines | `9964d9b3b8b8591d6f6b3c8b7b8917b533fa7f5587920dbdd4dd0b11108b3ae7` |
| [Arbitrary-depth canonical note](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/arbitrary_depth_autonomous_mse_closure/CANONICAL_NOTE.md:1) | Full, 1,043 lines | `735559345c27c30641cc4725936fb0af52935cdd663ef393bcd80f6b18e55904` |
| [Arbitrary-depth supervisory record](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/arbitrary_depth_autonomous_mse_closure/SUPERVISORY_AUDIT.md:1) | Full, provenance | `ec13a50aeb043ab3708b661cbf31ca957e2fcfbd87d1c27863bde5296cb2b1a5` |
| [Joint audit record](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/AUDIT_RECORD.md:1) | Full, provenance | `53bfd8e718a169671d80d584728d843dbd8bebbf8081050fef031e6d1f714a6b` |
| [Quadratic theorem/attempt](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/THEOREM_AND_AUDIT.md:1) | Full, 325 lines | `0a7c7313a447b3f7f5345b5901f189ff6133d22401a4bb6c3f7bad87242e42e0` |
| [Quadratic protocol](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/PROTOCOL.md:1) | Full | `28434136bdd2268ab31027446829031dc949c27792b564e1ea3b2bfea056d571` |
| [Order-17 results](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/PARTIAL_ORDER17_RESULTS.md:1) | Full; certificate not regenerated | `6c01d091fac00f679758d9ae34a857b7a4da3e83d9b6a5d11327a1a3765ee225` |
| [Partial activation recurrence](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/partial_activation_recurrence.py:1) | Full, 256 lines, read-only inspection | `920355141e32600e0e76b03900c8b38465c4c4e15682b539f340ddc8f9079f6f` |
| [Partial activation tests](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/test_partial_activation_recurrence.py:1) | Full; not run | `7b51445fb0266425e07187e4b540492ce1e294433a179ddf3acd46fa3e0e91b5` |
| [L3 regression code](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/depth3_unfrozen_readout_closure/test_unfrozen_readout_closure.py:1) | Full, 256 lines; floating-point tests, not proof certificates; not run | `3321280d240f65c35fa46eb50f1cb8786987bb8331b3215eda3b1e2759ad3e48` |
| [Multi-output aggregate](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/depth2_multioutput_average_closure/RESULTS.md:1) | Full, 279 lines | `bea08e349847a48c2c3d5350f86451090db7bbb0956b6605c69e37e48c50260f` |
| [Frozen-readout L3](/home/amir/Codes/PDE/studies/mean_field_peeling/identity_compiler/linear_gaussian_program/depth3_frozen_readout_closure/THEOREM_AND_PROOF.md:1) | Scoped, lines 1–125 | `f8f4578c008eafd587afdd28be2ef0173c75407cb09c0f5606a60dd5792de411` |

The three local rollouts were indexed for user/final turns; only the relevant mathematical messages and contract/amendment passages were read, not every inherited tool output. Relevant messages specifically read in full include #8 lines 6289 and 7221; #11 lines 6284, 6724, 7345, 7897 and 8369; #12 lines 6289, 6492 and 7200. Earlier common inherited work was used as a locator, not double-counted as independent proof.

| Historical source | Hash / scope |
|---|---|
| [#8 rollout](/home/amir/.codex/sessions/2026/08/21/rollout-2026-08-21T20-26-19-01a02592-e627-7672-a2f7-ed654280a6e0.jsonl:1) | `11afa7ce0f607d2eadb4e6388e265a67f53ec4d19ffec579e46ac0806bc10678`; scoped as above |
| [#11 rollout](/home/amir/.codex/sessions/2026/08/20/rollout-2026-08-20T17-35-04-01a01fcf-c121-7a41-860b-9a28453d6847.jsonl:1) | `a1e0e2742b42bf4354157c8bd6db14ce7f0e15df3ceb18ab603f1e5ab30076ae`; scoped as above |
| [#12 rollout](/home/amir/.codex/sessions/2026/08/20/rollout-2026-08-20T19-46-10-01a02047-c7b7-7270-abb1-401d9d16f697.jsonl:1) | `5c9d36312bc496323125566484bf41184302cb4a7fbf8a8526e5691f8bdfaad1`; scoped as above |
| [Operator 1 chronology](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR1_CHRONOLOGY.txt:22801) | `9a12f3f0b2ef85fc63deb1397dedb03c3981e0ad0cd5d1d6c24ebea483dc96a7`; whole-file locator search; full linear block 22801–22916 |
| [Operator 1 finals](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR1_FINALS.txt:15898) | `48ff0b33c75af97647b8e95c767ab51c5660baf7fbc0083ca9be19e8cd09c881`; whole-file search; relevant linear final fully read |
| [Operator 1 reviews](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR1_REVIEWS.txt:24670) | `392027f2936483642a67cdc08971a4f5b5eaf2839f704df037bb1eefe1bf38ad`; scoped late linear/source/Euler/PDE repairs; provenance only |
| [Operator 2 chronology](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR2_CHRONOLOGY.txt:18519) | `d767c6c931742d7b020363c3d904f9daa32b7b5a54aaee4609dfc4947b149088`; whole-file locator search, scoped relevant context |
| [Operator 2 finals](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR2_FINALS.txt:12308) | `3d79ff083516b2df8783041e251804769cbfc5432c4d534781980ad9398c71f2`; whole-file locator search, no nonlinear proof endorsement |
| [Operator 2 reviews](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR2_REVIEWS.txt:1) | `3d7ad724ba53d1066c8b86a5ad10c666907329c69773383225db55c27a65654c`; searched for assigned linear strand; not read in full |
| [Operator 1 preserved app page](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR1_PAGE1.json:1) | `334883f80d99b3b8e09a5d1e85d44ff77a122f434d918a416f73963340b3a859`; decoded task metadata and relevant turns |
| [Operator 2 preserved app page](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR2_PAGE1.json:1) | `5263a767c09bec0fe993617779308b1bd4d6ea98230c7765b1b7fc8193cb20be`; decoded task/turn metadata, not a full-history read |
| [Preservation manifest](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR_SOURCE_MANIFEST.json:1) | `40f9f0561af33a8ca74906d28f724d815789a2f0fca6b78f9cd0fc6fbf3f5ca7`; full |

These 100,000-plus lines of exported Operator history/reviews were available in full but were **not all read in full**. The complete primary proof readings above, targeted old turns, preservation hashes, and stated scoped history checks are the actual review coverage. No claim here rests on pretending a full-history audit occurred.

## 11. Remaining limitations and admissible consolidation wording

The main unresolved proof obligation in this source group is identification of the arbitrary-depth candidate beyond the specifically proved depths, and a separately formulated multi-sample linear limit if that is desired. A scalar one-label fitting theorem says nothing about arbitrary labels being linearly realizable. Loss convergence to zero, existence of a compact-time joint limit, and feature learning are distinct assertions.

The principal mathematical positives and bounded-contraction negatives survive this audit in their exact scopes. The material errors to prevent in consolidation are promoting the retracted arbitrary-depth bridge; reading L3 as three samples; counting the frozen-readout/aggregate reductions as full training on arbitrary data; calling the tagged encoder argument an output-only PDE theorem; treating the transport playback counterexample as an admissible predictive closure; or claiming that a word-space kernel meets the original prohibition on hidden operator states.

Recommended statement: **For one-sample deep linear Gaussian μP training, the project has a rigorous L2 commuting spectral field limit and a rigorous fully trained L3 noncommutative operator/kernel limit, the latter including arbitrary normalized vanishing-mesh exact-GD diagonals on fixed compact physical horizons. Exact state-universal bounded-current-contraction scalar and local-PDE encoders are obstructed. The separate tagged bounded-filtration argument has a stronger representation contract. The audited sources do not prove the advertised arbitrary-depth, arbitrary-fixed-data joint theorem.**
