# Global and semi-global nonlinear frontier — independent source-group audit

Audit date: 2026-09-08. Assigned scope: PDE Resume L3 research (2), (3), (4), Generalize non-local GF; PDE-2 four Find Resume thread tasks, the distinct Find Resume research task, L=2 arctan/two inputs, and Explain audited proof. This is a read-only mathematical audit, not resumed research. No experiments, agents, task messages, commits, branch changes, permission changes, or research-file edits were performed. Only this report was created.

I used solve-math-rigorously and investigate-conjectures, reading their complete instructions and the evidence-ledger, adversarial-audit, and research-contract references myself. Their main effect here is to separate proof obligations, source versions, and scientific claims. Existing reviews and consolidation documents were locators/provenance, not substitutes for proof. I did not read the other new source-group auditors' reports. The later clipping continuation assigned to the root auditor is excluded.

## 1. Findings suitable for consolidation

1. There are genuinely global, identified nonlinear population limits with exact finite GF/GD bridges. The strongest fully read, internally self-contained examples are the one-sample fixed shifted-arctangent theorem at every fixed hidden depth L≥3, and the three-sample bounded-shape/large-offset-gain theorem at every fixed L≥2. A fully read older L=2 one-sample pure-arctangent proof is also internally complete.
2. The newer three-sample odd-gain theorem uses one activation aδ(z+arctan z) at every fixed L≥2. I read its four principal files and the underlying complete Gaussian-program and velocity bridge chapters, checking their finite-depth specialization. Its gain is enormous; it is not the no-gain convex-mixture result. Its remaining external norm input is a classical sharp Gaussian-matrix bound, identified below.
3. SG, the general C1,1 theorem, is much broader in data, activation, and initialization, but only proves one fixed positive interval. Its every-deterministic-vanishing-step quantifier rigorously implies the omitted finite-width-GF corollary for squared loss, including the stated observable topologies. Section 3.1 proves this implication. Do not label finite GF “unproved” merely because it was not separately stated.
4. The all-depth two-sample odd-activation continuation supersedes historical “L≥5 open” statements. The L=3 δ² refinement supersedes earlier δ^800, δ^10, and δ^4 sufficient bounds at that depth. I checked the current extension arguments in full, but did not re-read their entire older affine/source/velocity dependency chain. These receive a scoped-extension grade, not a fresh end-to-end certification.
5. Three-sample exact no-gain odd mixtures remain at sharp initialization bounds plus explicitly conditional continuation. Literal convex-offset mixtures have a proved initialization-conditioning obstruction, not a proved failure of every fixed-depth global theorem. Moderate calibrated sine has a fixed positive-time result, not a global continuation.
6. None of these results establishes a general, moderately nonlinear, arbitrary-data global learning theory. Strict positive affine-fit error, initial feature motion, and training interpolation on one/two/three examples must not be ranked as solving that scientific target. No universal novelty or necessary-scaling claim is supported by this audit.

Audit grades used below:

- **I**: principal manuscript and its substantive internal proof read fully; no decisive gap found in those arguments.
- **C**: full current argument checked, but a stated nonclassic external proof dependency remains unaudited.
- **E**: principal extension and named current companions read fully; substantive older internal dependencies not all re-audited. The extension checks are fresh, the full-package endorsement remains qualified.
- **P**: fully read theorem is partial, initialization-only, or conditional; not a global identified trained limit.

These are mathematical audit judgments, not formal verification and not translations of historical PASS labels.

## 2. Clean theorem inventory and quantifiers

### Common conventions and observable distinctions

L always counts hidden layers; m counts samples. All depth assertions fix finite L before taking width n→∞. No result below proves L=L(n)→∞. Each dataset is fixed in the convergence statement, even where one activation or existence time works over a class of datasets.

The stored readout is C, with prediction f_i=n^(-1) Cᵀh_i^L. Thus C_j∼N(0,n^(-2)) means coordinate standard deviation n^(-1), not an order-one stored readout. A vanishing prediction is not the same assumption as a vanishing readout field.

For the recent two/three-sample packages, initialization and optimizer convention **R** means independent W¹_jk∼N(0,1/d), z¹=W¹x, middle W^ell_jk∼N(0,1/n), C_j∼N(0,n^(-2)); normalized inputs ||x_i||²=d; loss (1/2)Σ_i(f_i-y_i)²; raw metric

    (d/n)||ΔW¹||_F² + Σ_(ell=2)^L ||ΔW^ell||_F² + ||ΔC||²/n.

The Euclidean-gradient multipliers per physical step are therefore (n/d,1,…,1,n). If instead W¹ is stored with variance 1 and z¹=W¹x/√d, they become (n,1,…,1,n). These are equivalent first-layer storage conventions, not different width regimes. R uses simultaneous exact raw Euler with η_n=n^(-2), t=kη_n, linear raw-parameter interpolation and recomputed hidden fields; GF uses the same metric and actual initialization. The table conservatively records the stated algorithm, even when a bridge's estimates allow more vanishing-step sequences.

**O-full** denotes predictions, loss, every entry of all L+1 true raw kernel blocks; layerwise joint sample field/velocity laws in W2 uniformly in time and at finitely many joint times; hidden preactivation/activation path laws in W2 for the uniform path norm; second moments and integrated squared hidden speeds; and fixed finite correctly typed generated action/adjoint probes. “Layerwise” does not arbitrarily identify neuron indices in different populations. It does not mean cross-width operator-norm convergence, all unbounded products, a uniform class of growing probes, or a simultaneous infinite-time limit.

**O-SG** is the actual SG statement: uniform predictions/loss/all kernels, layerwise joint m-input preactivation/activation path W2, integrated squared hidden speeds, and fixed typed probes built from Lipschitz coordinate maps, linear combinations, and bounded-continuous-factor times L2 products, measured by continuous quadratic-growth functions. It does not separately state the entire uniform-time velocity-law package O-full. The diagonal GF corollary preserves O-SG, not an enlarged package.

For nonaffinity, A_phi(Z)=inf_(b,c) E[(phi(Z)-b-cZ)²] is an absolute regression error. Positive A_phi need not be a substantial fraction of Var(phi(Z)). “Initial motion” means nonzero right acceleration and O(t²) hidden displacement/O(t) speed from zero limiting readout, not positive initial speed or perpetual activity.

### Global and positive-time identified limits

| ID / grade | Hidden depth; data and labels | Activation and its quantifiers | Readout, optimizer, time scope |
|---|---|---|---|
| SG / C, with proved GF corollary | Any fixed L≥2, m,d; bounded normalized inputs, including coincidences and singular Gram; bounded real labels; positive weights summing to one | Layer-dependent C1 activations with bounded, globally Lipschitz derivative, common finite bounds; at most linear growth, not necessarily nonaffine | Gaussian middle matrices; centered subGaussian first entries allowed. Any fixed iid subGaussian stored readout, including O(1) Gaussian/noncentered, plus vanishing RMS perturbations. κ_ell≥0; rates η_n(nκ₁,κ₂,…,κ_L,nκ_(L+1)); **every deterministic η_n→0**. One T*>0. [Statement](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/GENERALIZE_PRIMARY/GENERAL_POPULATION_GF_PROOF.md:12) |
| L2-A / I | L=2; one input x=y=1 | Pure arctan in both layers | First variance 1, middle 1/n, C variance n^(-2); loss r²; rates η_n(n,1,n), η_n√n→0. Every fixed T<∞; finite GF and exact GD. [Complete baseline](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/inherited_baselines/L2_ONE_SAMPLE_ARCTAN_GLOBAL_PROOF.md:1) |
| L2-G / C | L=2; any fixed finite orthogonal normalized inputs, arbitrary fixed real labels | First activation C1,1 with bounded derivative, possibly unbounded/nonmonotone/flat; second bounded C1,1 with bounded derivative. Different activations allowed | Positive fixed κ and Gaussian scales; zero limiting C with coordinate-sup vanishing perturbation, including n^(-β) Gaussian for every β>0, or fixed bounded iid C plus such perturbation. **Not O(1) Gaussian C.** Summed square loss; η_n√n→0 sufficient. Every finite T, finite GF and exact GD. Affine first activation extends geometry to arbitrary fixed inputs and needs only η_n→0. [Statement](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/GLOBAL_ACTIVATION_TRANSFORM_EXTENSION.md:5) |
| SA / I | Every fixed L≥3; one input x=y=1 | The same bounded phi(z)=1+arctan(z)/10, independent of L,n,T | First variance 1, middle 1/n, C variance n^(-2); loss r²; raw η_n=n^(-2), rates η_n(n,1,…,1,n). Every finite T, finite GF and exact GD. [Theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/SHIFTED_ATAN_ALL_DEPTHS/GENERAL_DEPTH_SELF_CONTAINED_PROOF.md:16) |
| 2S-offset / E | L=3, m=2; ρ∈[-1,1-δ], 0<δ≤2; all binary labels, including antipodal data | 1+z+e arctan z; one constructive eδ>0 for the whole fixed separation class, every 0<e≤eδ. Independent of n,T and particular angle | R; global population and compact-time finite GF/GD. [Theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_separated_angle_theorem/PROOF.md:9) |
| 2S-odd / E | L=3, m=2; |ρ|≤1-δ, 0<δ≤1; all binary labels | az+e arctan z, a∈[1/2,1], 0<e≤c_poly δ². Includes the small literal convex mixture and separately the normalized odd family, with the source's parameter restrictions | R; global population and compact-time finite GF/GD. Same very small c_poly as preceding polynomial refinements. [δ² theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/odd_activation_lower_powers_three_inputs/TWO_INPUT_PROOF.md:6) |
| 2S-depth / E | Every fixed L≥3, m=2; same two-sided separation and labels | az+e arctan z; e≤c_L δ^(p_L), c_L explicitly depth-dependent. p₃=31/8, p₄=9/2, p₅=21/4, p_L=9−43/[2(L+1)] for L≥6. L=3 can instead use sharper 2S-odd | R; global population and compact-time finite GF/GD. **Not one positive coefficient working at all depths.** [Theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth56/PROOF.md:8) |
| 2S-shape / E | L=3, m=2; same two-sided separation and all binary labels | az+eψ(z), a∈[1/2,1]; ψ∈C², |ψ(0)|,sup|ψ′|,sup|ψ″|≤1; possibly nonodd, nonmonotone, or linearly growing. Dynamics for e≤c_dyn δ^(31/8); persistent nonaffinity has an additional shape-dependent cutoff | R; global population and compact-time finite GF/GD. The dynamics class itself includes affine ψ. [Theorems A/B](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_activation_design/PROOF.md:54) |
| 3S-shape-depth / I | Every fixed L≥2, m=3; Γ_ij≤1−δ, 0<δ<1; all binary labels, singular Γ allowed | a(1+z)+eψ(z), ψ nonconstant C² with sup norms of ψ,ψ′,ψ″≤1; **one a=a_(δ,ψ)** and **any one e∈(0,1]**, including 1, work at every fixed depth. No n,T,d,labels,or individual-data dependence | R; global strong population flow, exponential population fitting, full compact-time finite GF/GD. [Theorem M.1](/home/amir/Codes/PDE/studies/mean_field_peeling/activation_class_all_depths/MANUSCRIPT.md:203) |
| 3S-odd-gain / I with classical external norm input | Every fixed L≥2, m=3; |Γ_ij|≤1−δ, 0<δ≤1; all binary labels, singular Γ allowed | aδ(z+arctan z), aδ=324π exp(1)·10^10 δ^(-2), same at every depth. Nonlinear/linear coefficient ratio is **one**, but the overall gain is huge | R; global strong population flow, exponential population fitting, O-full finite GF/GD on every fixed horizon. [Theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_gain_all_depths/PROOF.md:7) |
| Moderate-sine / E for explicit source bound; SG supplies existence on some positive interval | L=3, m=2; two-sided separation; all binary labels | Calibrated αz+βsin(2z) with underlying sine coefficient 2/5 fixed independently of δ, n and T; exact definition below | R; positive-time only, explicit source T*=S₀/3. No global trained result. [Local source theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/moderate_sine_global/LOCAL_SOURCE.md:7) |

SG's existence time depends on fixed depth, activation/init/rate/data bounds, but not m,d or a smallest Gram eigenvalue when normalized-input bounds and averaged-loss derivative bounds remain fixed. Nevertheless its convergence is for fixed m,d, not growing samples/dimension. Summed loss on m samples changes physical time by m. Its separable C1 loss extension needs locally Lipschitz derivatives with common bounds on bounded prediction intervals; it does not assume nonnegativity or give global finite-GF existence for such arbitrary losses.

### What is learned, and what is fitted?

| ID | Observable scope | Nonaffinity / nonlazy conclusion | Fitting and endpoint quantifier |
|---|---|---|---|
| SG | O-SG for GD and, by §3.1, finite GF | No general nonlazy assertion. Separate L=2 corollary: Gaussian first weights, zero limiting C, positive σ/κ, pairwise nonparallel normalized inputs, all labels nonzero, both activations nonaffine. Then every input/layer has nonzero initial motion, all three kernel blocks become PD/nonconstant, and A_phi stays positive on a smaller interval | Local loss identity only; no global interpolation or endpoint theorem |
| L2-A | Uniform predictions/loss/all three kernels, fixed forward/adjoint action measurements, hidden path W2 and integrated speeds | Both layers initially move; kernel changes at order t²; nonaffinity positive on a fixed short interval | Source does not assert a general fitting/endpoint theorem |
| L2-G | The stated fixed typed observations, all kernels, path W2 and speed energies; direct same-width GF/GD comparison in proof coordinates | Short-time activity under its extra nontriviality assumptions; not forever | No universal fitting theorem: the allowed class includes constant zero second activation |
| SA | O-full and explicit transformed same-width GF/GD comparison | Every hidden preactivation and activation speed is positive at every finite t>0; zero at t=0. A_phi has a positive minimum on every compact physical horizon; all blocks initially change | Population loss ≤exp(−25t/9); a strong fitting endpoint follows from the bounded feature-clock path. Not uniform-in-time width convergence or convergence of finite endpoints |
| 2S-offset | O-full, subject to inherited bridge audit qualification | A_phi≥e²ηδ/4 throughout; nonzero initial motion in each hidden layer/sample | Scalar population output y_i g reaches fitting as t→∞; strong endpoint follows from the finite feature-clock interval and bounded directions. Not an endpoint width-limit theorem |
| 2S-odd / 2S-depth | O-full, same qualification | Positive absolute all-time regression margin; nonzero initial motion, not a theorem of positive speed at every later time | Population exponential fitting; for 2S-depth loss ≤exp(−2a^(2L)δt). Strong population endpoint follows from the controlled path; no interchange of n and t→∞ |
| 2S-shape | O-full, same qualification | Nonaffine ψ gives initial activity. A_phi≥e²ηψ/4 globally only under extra c_NL(ψ) cutoff; affine ψ gives no such claim | Population loss ≤exp(−δt/2048); no broad-data or finite-endpoint limit |
| 3S-shape-depth | O-full | Every block/sample/layer has nonzero initial right acceleration; pᵀK(t)p=pᵀK(0)p+18t²||V||²+o(t²), p=y/3. A_phi≥e²cψ/[16a^(L−1)] globally. Stronger restricted shape classes improve depth dependence of the absolute margin | Population loss ≤(3/2)exp(−λa^(2L)t), λ=δ²/16. Integrable residual and bounded raw directions imply a strong fitting endpoint. No all-time-uniform width or endpoint convergence |
| 3S-odd-gain | O-full | A_phi≥(a_δ)²η₀/4, η₀=1/[108π exp(1)], globally and for every layer. Initial acceleration/kernel variation as above; no depth-uniform relative fraction or perpetual-speed assertion | Population loss ≤(3/2)exp(−λa_δ^(2L)t), λ=η₀δ²/3. Strong population fitting endpoint is a direct consequence, not a finite-endpoint width limit |
| Moderate-sine | Local full bridge claimed via inherited machinery; O-SG independently follows on some fixed positive interval | Substantial nonaffinity at initialization; direct small-time source control. Do not promote initialization sine cancellation to trained-time cancellation | No global fitting theorem |

In the 3S-odd-gain formulas, a_δ denotes the entire separation-dependent gain.

### Partial results that must remain outside the global-joint table

| Source / grade | Exact positive content | What it does not supply |
|---|---|---|
| [Exact odd mixture](/home/amir/Codes/PDE/studies/mean_field_peeling/odd_mixture_general_depth/REPORT.md:77), P | m=3, L≥1, d≥2, 0<δ≤1/4, 0<θ≤1; phiθ=(1−θ)z+θ arctan z. Sharp initialized inf λ_min(Q_L) ≍ δ²θ²L/(1+θL)² and q_L≍1/(1+θL); normalized inf λ_min(Q_L/q_L) ≍ δ²θ²L/(1+θL). Explicit universal constants and strict planar matching examples | No positive sufficient θ*(δ,L) for a global trained identified GF/GD theorem |
| Same report, [Part II](/home/amir/Codes/PDE/studies/mean_field_peeling/odd_mixture_general_depth/REPORT.md:445), P | Arbitrary fixed-depth population continuation under explicit cap-uniform bounded primals **and weighted exponential backward tails** | Tail hypothesis not proved for canonical training; no finite-width bridge supplied by this criterion |
| [Literal convex offset](/home/amir/Codes/PDE/studies/mean_field_peeling/convex_offset_all_depths/REPORT.md:22), P | phi=(1−ε)(1+z)+εψ, 0<ε<1/2, bounded normalized nonconstant C² ψ: initialized intersample distances contract geometrically; no depth-uniform absolute or normalized kernel lower bound | Not a counterexample to qualitative global existence for each fixed L and fixed ε |
| [Finite L=3 arctan GF coercivity](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/EXPLAIN_PRIMARY/l3-full-resolution-9nbD4z/READOUT_COERCIVITY.md:176), I for finite optimization | One sample, pure atan, small nonzero RMS readout and nondegenerate top feature; global finite GF, persistent readout kernel, exponential fitting and finite-parameter endpoint, with a high-probability canonical Gaussian specialization | Not identification of the infinite-width global state |
| [Exact finite GD coercivity](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/EXPLAIN_PRIMARY/l3-full-resolution-9nbD4z/EXACT_GD_COERCIVITY.md:73), I for finite optimization | Same one-sample L=3 model, η=n^(-2), sufficiently large n and explicit initialization conditions: all iterations undershoot monotonically toward 1, finite total feature clock, exponential fitting and parameter endpoint | Not a full global trained population law or same-width GF/GD path comparison |
| [Practical assessment](/home/amir/Codes/PDE/studies/mean_field_peeling/practical_global_limit_assessment/ASSESSMENT.md:40), P | Correct separation of finite energy control, canonical infinite-dimensional continuation, Gaussian initialization depth effects, and calibrated initialization candidates | Not a proof of the practical global target, a trained depth ODE, or a simultaneous depth/width theorem |

## 3. Fresh verification: decisive proof skeletons and adversarial checks

### 3.1 SG, including the omitted finite-width-GF corollary

I read all 524 lines of the main proof, all 540 of the general-depth response proof, and all 373 of the activity source.

The substantive response estimate is not obtained by pretending matrix reuse preserves independence. Named Gaussian sources remain distinct formal slots, with full covariance and opposite-orientation responses. A strictly past pulse carries Δω_b. The forward-up/backward-down chronological induction preserves that factor, and uses weighted time/sample sums and marginal subGaussian bounds rather than the maximum of a growing collection of Gaussians. Thus the averaged-loss constants need not acquire a factor m or the number of steps.

The main stability estimate has one cutoff factor:

    ||F(θ)−F(θ_ref)|| ≤ C(1+R)d(θ,θ_ref)+C exp(−cR²).

Successive backward substitution adds a new cutoff term multiplying an already controlled forward error; it does not multiply previous errors by R at every layer. Only the reference needs tails. Gronwall therefore gives exp(CRT−cR²), which vanishes. The fixed coarse oracle is identified before refining its mesh or removing R. Actual GD is compared directly against that oracle, so no Gaussian limit for a growing program is smuggled in. C1,1 mollification uses uniform function/derivative errors and uniform response constants. The final amendment explicitly restores **Gaussian first weights in the activity corollary**, not in the general existence theorem. [Stability](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/GENERALIZE_PRIMARY/GENERAL_POPULATION_GF_PROOF.md:267), [finite GD bridge](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/GENERALIZE_PRIMARY/GENERAL_POPULATION_GF_PROOF.md:338), [amendment](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/GENERALIZE_FINAL_VS_REVIEWED.diff:1).

**Finite-GF implication, assessed in response to the integration check.** For squared loss it is valid for every observable actually named by SG.

Fix n and one finite initial parameter realization. In Euclidean coordinates the continuous finite system is

    θ′=−D_n ∇E_n(θ),

where D_n is the fixed nonnegative diagonal preconditioner encoding nκ₁, κ₂,…,nκ_(L+1). C1,1 activations imply a locally Lipschitz finite vector field, even though a global Lipschitz constant is unavailable. Zero κ blocks are simply constant. Since E_n≥0,

    E_n′=−∇E_nᵀD_n∇E_n,
    ∫₀ᵀ ||θ′||² dt ≤ ||D_n|| E_n(0).

Consequently parameter length on any finite interval is at most √(T||D_n||E_n(0)); tails of that interval are Cauchy. The solution stays in a finite-dimensional bounded ball, has a finite endpoint, and local uniqueness continues it. This proves global finite GF for every finite initialization. The n-dependent constant is harmless here.

At this fixed n, exact Euler with step η and polygonal raw interpolation converges uniformly to GF on [0,T*] as η→0. To see this without assuming a global Lipschitz constant, take a compact tube around the GF trajectory, use the local bound/Lipschitz constant there, and apply the stopped Euler error recurrence; a sufficiently small η closes the tube condition. Its piecewise constant parameter directions converge in essential supremum to the continuous GF direction. At finite n the network maps are C1, hence their derivatives are continuous on this compact tube. The actual derivatives of the recomputed hidden paths therefore converge in essential supremum, and thus in L2 time. This yields convergence of the integrated squared preactivation/activation speeds, not just parameter paths.

Every finite kernel is a continuous function of these parameters; uniform kernel convergence follows. For hidden path laws, pairing equal neuron indices gives

    W2²(μ_n^GD, μ_n^GF)
      ≤ (1/n) Σ_j ||X_(n,j)^GD−X_(n,j)^GF||_∞² →0

at fixed n. Fixed typed forward/adjoint probes are continuous finite compositions. The allowed bounded continuous multiplier products also converge uniformly on the relevant finite-dimensional compact images. Continuous quadratic-growth measurements cause no difficulty at fixed n: there are finitely many neuron trajectories and their values lie in a common compact set as η→0. The argument applies to a fixed finite requested probe list, precisely SG's quantifier; no supremum over all possible probes is needed. Arbitrary unbounded products are not added.

Let d_n be the sum of the required bounded observable distances: uniform prediction/loss/kernel errors, hidden path-law W2 distances, speed-energy errors, and measurements of that finite probe list. With the *same* random initialization in the GF and GD at width n, the fixed-n convergence is almost sure as η→0 and hence in probability. Choose deterministically 0<η_n<1/n so small that

    Pr{d_n(GD_(n,η_n),GF_n)>1/n}<1/n.

Random initialization-dependent local constants do not force a random step: convergence in probability permits the deterministic choice. SG applies to this sequence because it applies to **every** deterministic η_n→0. Triangle inequalities transfer its convergence to GF_n in all O-SG topologies.

This establishes the missing finite-GF corollary conditional only on SG itself, with no width-uniform Euler rate and no modification of its activation, squared-loss, initialization, or κ assumptions. For any other admissible GD step sequence, both algorithms then have the same limiting observable laws. This last observation is not by itself convergence of same-index GF/GD hidden coordinates in a common coupling, nor a rate, nor a global-in-time population theorem.

For the general separable-loss extension, the nonnegative-energy argument is unavailable. However the source's preliminary ball applies to finite GF as well as Euler on the high-probability bounded-initialization event and T*≤T_ball. A stopped/cemetery extension off that event gives the analogous short-time convergence-in-probability statement. This does **not** assert that every finite realization has a global GF for an arbitrary loss unbounded below. [Preliminary ball](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/GENERALIZE_PRIMARY/GENERAL_POPULATION_GF_PROOF.md:226), [loss extension](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/GENERALIZE_PRIMARY/GENERAL_POPULATION_GF_PROOF.md:473).

External qualification: SG uses the substantive fixed-program theorem in Tensor Programs III. I inspected the primary Setup 2.2, Theorem 2.10, Box 1 and relevant remarks, including polynomial growth, Gaussian roots/matrices and derivative conventions. I did **not** read its full proof in Appendix L. This nonclassic dependency remains unaudited, not inferred from an abstract. The source's subGaussian quantile encoding and fixed-program hypotheses were checked, but that does not independently prove the external theorem. [Tensor Programs III, primary manuscript](https://arxiv.org/pdf/2009.10685). Tensor Programs IVb is cited as consistency of operator semantics, not an additional necessary theorem in the displayed construction.

**Final integration update supplied by the root/user:** the separate primary-literature audit reports a full read of TP III Appendices K–N, a printed N.3 normalization repair, and an unclosed N.2 core-plus-vanishing-Gram-coefficient/all-moments argument. I did not read that auditor's report or independently repeat this external audit. This is a reported proof-dependency issue, not a counterexample to the theorem. It reinforces the qualification here: SG and L2-G are internally checked arguments **importing** the rank-free fixed-program result, not first-principles certifications of that result. The finite-GF diagonal implication remains valid conditional on SG; it neither repairs nor worsens the external dependency.

The distinction is substantive. L2-A, SA and 3S-shape-depth prove their own narrower fixed-program laws by independent query perturbation, bounded-operator stability and explicit Gaussian conditioning. The 3S-odd-gain package specializes the separately fully read internal foundations/velocity proofs, with a classical Gaussian norm input. Their internal laws concern fixed programs with controlled coordinate maps, and remove singularity through a stated regularization argument; this audit did not substitute TP III's general rank-free theorem for those arguments. The two-sample E rows remain qualified for their unread internal dependency chains; no external TP failure is imputed to them merely by association.

The activity proof is genuinely separate: ridge-function independence via finite differences/differentiation yields positive forward Gram even when the input Gram is singular; Gaussian backward conditional covariance and a nonzero forward innovation prevent samplewise cancellation. Nonzero labels and Gaussian first weights matter. General existence with arbitrary subGaussian roots, zero learning rates, or affine activations cannot inherit those strict conclusions.

### 3.2 One-sample global results: pure atan at L=2 and shifted atan at all fixed depths

The older L2-A proof is self-contained at its stated regularity. It proves finite adaptive Gaussian conditioning with independent-query regularization, constructs common L2 actions and their adjoints, and uses F(z)=z+z³/3 to cancel the first gate. The transformed state has a locally Lipschitz vector field on sets with bounded readout coordinates. Bounded top activation and decreasing square loss give those bounds on every finite horizon. Its exact cubic raw-GD defect accumulates as C_T(η+η√n+η²n), explaining its step condition. Final backward probes are recovered by second-moment tails, and grid reconstruction proves uniform-path W2; no evolving fourth-moment premise is silently needed. The strict activity calculation uses a positive independent backward Gaussian component and adjunction. I found no decisive gap in this 543-line proof. It states short-time strict activity, not all-time fitting or perpetual speed.

SA's 1,727-line proof is also internally self-contained. Its φ stays between 5/6 and 7/6, with derivative at most 1/10. On feature time s≤3/2, the explicit forward/transpose response bounds close uniformly over each fixed depth: forward density at most 1.5Δ; top row ≤3067/3200<1; lower rows below 0.9; backward RMS ≤7/40. A Gaussian part plus bounded shift supplies E exp(q²/16)≤2. The one-R comparison removes caps with an error dominated by exp(CR−R²/256). I checked that current returns are retained and singular Grams use noise regularization, not continuity of pseudoinverses. [Response section](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/SHIFTED_ATAN_ALL_DEPTHS/GENERAL_DEPTH_SELF_CONTAINED_PROOF.md:757).

The raw feature-gradient kernel is at least 25/36. Starting from f=0, the feature-time first hit f=1 occurs at s*≤36/25<3/2. The physical clock

    t(s)=∫₀ˢ [2(1−f(u))]^(-1) du

diverges at that first hit, yielding all finite physical times and the population loss rate exp(−25t/9). The feature trajectory exists beyond the hit with slack, so its endpoint also gives a strong limiting fitting state as physical time tends to infinity. This is an implication within the population construction, not a width/endpoint interchange. [Clock proof](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/SHIFTED_ATAN_ALL_DEPTHS/GENERAL_DEPTH_SELF_CONTAINED_PROOF.md:1077).

The transformed raw GD is not declared exact Euler: its transform F=10(z+z³/3) has an explicitly summed defect of order η√n+η²n, and stopping closes on a longer physical interval. The observational appendix handles actual recomputed velocities. The last section proves every hidden speed stays positive for finite t>0; the zero at initialization is retained. Its nonaffinity argument is positivity on Gaussian-plus-bounded-shift support and compact-time continuity, not a universal numerical relative lower bound.

### 3.3 All-depth three-sample bounded shape with large offset gain

I read all 2,864 lines, including Parts F, S, G, V, N and A; this is not a statement-only or inherited-PASS check.

The exact gain is

    λ=δ²/16, T₀=12/λ=192/δ²,
    a=max{10^12(1+T₀), [2^36 T₀²/√cψ]^(2/5)},

with cψ from a positive finite-interval best-affine regression integral. It is independent of depth, but strongly dependent on separation and shape. The normalizations h^ell/a^ell and z^ell/a^(ell−1) are proof coordinates only: **the readout and raw metric are not rescaled**.

The geometry uses the three-point augmented Gram Γ+11ᵀ≥δ²I/4; this is not an arbitrary-m theorem. Large initial variances make the derivative perturbation losses summable over layers, preserving a normalized initialized Gram ≥λ. The controlled fitting interval S=T₀a^(−L) is short; F=32^L bounds gradients, and the hidden displacement is bounded by 3√L F²s². This makes the small-total-update argument compatible with one fixed gain at all separately fixed depths.

The source bootstrap uses a same-array Gaussian comparator, not an assumption of independence of nonlinear trained inputs and matrices. It separates a Gaussian component from a small normalized nonlinear remainder, retains the offset, and closes explicitly selected forward and backward coefficient bounds in chronological order. The gain beats the depth-dependent curvature envelopes on the fitting interval. [Source proof](/home/amir/Codes/PDE/studies/mean_field_peeling/activation_class_all_depths/MANUSCRIPT.md:812).

A decisive adversarial check is the capped residual equation. The capped hidden update is generally **not** a gradient, so its hidden contribution cannot be called PSD. The proof instead uses

    r′=−a^(2L)(Q_L+J_h U_(h,R))r,
    Q_L≥(3λ/4)I,  ||J_h U_(h,R)||≤λ/4.

This nonsymmetric perturbation bound yields exponential residual decay and closes the total controlled-time budget with a factor-two slack. [Capped fitting argument](/home/amir/Codes/PDE/studies/mean_field_peeling/activation_class_all_depths/MANUSCRIPT.md:1301). Replacing this step by positivity of a “clipped NTK” would be an error; the current manuscript does not make it.

Parts F/V prove their own finite-program theorem, common bounded actions, scalar gradient/chain rules, cap removal, finite uncut GF and raw GD, nested velocity-query truncations, true rather than surrogate kernels, and path W2. The velocity-tail limit order removes the cap at a fixed velocity-tail level before letting that level diverge, so an uncontrolled cap-dependent velocity-moment constant is not multiplied by the cap error.

Parts N/A prove every initial hidden acceleration and kernel variation, and persistent absolute nonaffinity. Nonconstant bounded C² ψ need not be monotone or analytic. At the decisive Gram step its bounded nonaffine part and the large affine derivative prevent collapse; the proof does not substitute “ψ″ is never zero.” The broad shape class has a depth-dependent absolute regression margin; stronger restricted shape classes in Part A improve it. Neither is a statement of a depth-uniform relative fraction.

### 3.4 All-depth three-sample odd gain

I read PROOF, SOURCE_RESPONSE, POPULATION_LIMITS and INITIAL_MOTION completely, plus the complete 624-line foundations and 638-line velocity chapters they specialize. The generic proofs extend by induction over finitely many matrix instructions/layers, not by silently changing the number of samples or exchanging limits.

The initialization argument uses

    Γ^(entrywise 3) ≥ [δ²(2−δ)²/3] I₃,

proved with unit tensor test vectors annihilating the other two directions. A uniform cubic-Hermite coefficient of atan at variances σ²≥1 gives an absolute nonlinear Gram contribution. The normalized layer map z+K^(-1)atan(Kz) has derivative between 1 and 2. Gain aδ=10^10/λ, λ=δ²/[324π exp(1)], makes the total controlled fitting path S=(12/λ)aδ^(−L) short while preserving an initial nonlinear Gram floor. Controlled derivative bounds use F=8^L and retain local current curvature and higher-layer returns. The capped fitting step again uses a small hidden operator perturbation, not positivity of a capped gradient kernel. [Main geometry/fitting](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_gain_all_depths/PROOF.md:134).

The initial-motion companion proves forward and backward Gram positivity and then a nonzero new innovation at every upper layer, with the full recursive return included. This supports every sample/layer acceleration and the coefficient 18 in the projected kernel expansion. The four-file package and fully read generic bridge supply the claimed finite-algorithm/path/velocity identification.

One external input remains explicitly identified: E||G_(n,n)||≤2√n and Gaussian concentration yield finite initialized operator norm ≤3 with probability tending to one, and canonical norm ≤2. The package identifies Vershynin Theorem 7.3.1/Corollary 7.3.3; the all-depth affine certificate also supplies the Gaussian-comparison reasoning. These are classical Gaussian norm facts with the correct independent centered variance-1 entries and fixed finite union over layers. I checked the use and supplied comparison outline, but did not read the primary book proof. Unlike SG's Tensor Programs dependency, the nonclassic fixed-program/transpose/velocity machinery here was read directly in full.

This is not a tiny coefficient ratio: atan and z have equal coefficients. Nevertheless the huge gain drives large deep preactivations, where a bounded atan component is relatively small compared with the linear part. The theorem honestly gives an absolute nonaffinity floor, not a depth-uniform relative guarantee. Scaling down the activation is not merely changing physical time.

### 3.5 Two-sample refinements: fresh extensions, qualified full packages

For 2S-offset I read the 527-line main proof. The uniformity argument is valid: compact separation controls the affine reference feature interval and its primal norms; a positive minimum of Gaussian atan regression error over a compact mean/variance rectangle permits one eδ. The proof accommodates ρ=−1 through the offset. Population label symmetry gives f_i=y_i g, but the finite comparison retains both residuals and does not assume exact finite-sample symmetry. The older supplied response/continuation and velocity lemmas were not all read anew.

For 2S-depth I read all four current files. The affine balanced-chain estimates give the radial lower bound F≥c^(L+1)/b_L, b_L=2^(L−1)√((L−1)!), and operator bounds from exact balance identities. The source derivative keeps

    P = N + a ΔV B + a B ΔG + ΔV B ΔG.

Dropping either current B term would invalidate the improvement. The response chain is compressed entrywise using the available lower bound on the next active response, not by multiplying every crude worst-case bound. The resulting powers E₃=31, E₄=45, E₅=63, E_L=18L−25 for L≥6 give the stated p_L after the intrinsic-scale substitution. The explicit choice c_L=H_L^(−100)D_L^(−2p_L), D_L=3·2^(2L−2)√(2(L−1)!), closes the extension. The same old c_poly δ^10 is sufficient through L=6; a fixed exponent 9 is sufficient at all L with a **depth-dependent prefactor**, not one activation coefficient across all depths.

For the sharper L=3 δ² result I read TWO_INPUT_PROOF, SECTOR_RESPONSE and WEIGHTED_AFFINE_AND_CLOSURE. The weighted affine propagator bound and M≤24^(1/4)δ^(−1/8) are used in a sector-specific norm. Random gates are not assumed diagonal; off-diagonal returns pay two nonlinear factors. The closure controls the corrected M³ charge, retaining the current VJ₃V contribution. The final smallness is 8H^200 e M^16≤H^(−200), which follows from the retained extremely conservative c_poly. This verifies a sufficient exponent reduction, not its optimality or practicality.

For 2S-shape I read all four current files. Input swap combined with readout sign τ=y₁y₂ preserves the Gaussian initialized objective even for nonodd ψ. Forward and backward source bases differ by the label sign; only the deterministic coefficient blocks diagonalize. This is sufficient for the source argument without making random gates diagonal. The linear-growth supplement repairs a potential false estimate tying raw e/√δ to an intrinsic active scale when inactive variance can vanish independently. It obtains direct raw moments instead. Persistent nonaffinity requires the additional shape-dependent margin ηψ=min_(σ∈[1/√404,260]) A_ψ(σG)>0 and cutoff c_NL; the common dynamics cutoff alone does not guarantee a uniform positive margin over all normalized nonaffine shapes.

I found no decisive algebraic error in these current extensions. Their legacy affine, polynomial source, original nonlinear-comparison, and full observational bridge dependencies span many older files. Hash consistency was checked, but those dependencies were not all read in full. Do not upgrade this section to an independent complete re-proof.

### 3.6 Partial/frontier proofs and failed promotions

**Moderate sine.** The exact activation is defined by

    v=(1−exp(−8))/2−4exp(−4), s₀=√(1+4v/25),
    α=[1−(4/5)exp(−2)]/s₀, β=(2/5)/s₀,
    Φ(z)=αz+β sin(2z).

The LOCAL_SOURCE proof, read in full, fixes B=20 and derivative bound 2, derives a cap-independent small primal interval, and closes the four-stage chronological source estimate with current multiplier terms retained. Its explicit T*=S₀/3 is positive but extremely conservative. The initialization regression fraction reported for the calibrated coefficient is about 6.389%; this is an analytic initialization calculation, not new numerical evidence, and I did not audit the separate initialization note in full. The global issue is not erased by this positive-time theorem. Conditional sine averaging has exp(−2σ_new²), while the new innovation variance over a small step can be O(h²); that factor approaches 1, not the initialization factor exp(−2). The manuscript correctly declines global closure. Generic local GF/GD existence also follows from SG and §3.1, subject to SG's external dependency.

**Exact odd mixture.** I read all 643 lines. The initialization proof controls scalar variance q_ell, retention of first-chaos covariance, and the cubic nonlinear injection at **every** layer. Summing the injections is necessary for the factor L in the lower bound. The matching upper example is a strictly admissible clustered planar triple with a Gram-null vector, not coincident or forbidden antipodal data. A composed-kernel curvature bound supplies the upper estimate. The proof includes its Gaussian/Hermite identities; no nonclassic external theorem is silently used.

For fixed θ>0 as L→∞,

    q_L ~ 1/(2θL),
    A_(phiθ)(Z^L) ~ 1/(12θL³),
    A_(phiθ)(Z^L)/Var(phiθ(Z^L)) ~ 1/(6L²).

This rules out depth-uniform positive **absolute** nonaffinity in this model, but not a qualitative all-fixed-depth theorem with constants depending on L. The normalized initialized Gram remains well-conditioned at fixed separation in the specific sense of its sharp bound.

Part II uses the normalized backward coordinate q/√(1+z²) and assumes a cap-uniform exponential weighted tail. A secant bound for g(z)=(1+z²)^(-1), then a single-threshold Osgood comparison, proves conditional cap convergence and uniqueness. Its counterexample to deriving those tails from L2 bounds is an ambient state, not a state proved reachable by canonical GF. The missing canonical tail hypothesis must remain visible.

**Literal convex offset.** I read all 291 lines. With 0<ε<1/2, initial Gaussian scales remain in a compact interval, and κ²=max E[phi′(σG)²]<1: equality would force ψ′≡1, impossible for bounded ψ. The covariance differentiation identity is proved including limiting degenerate correlations. It gives

    λ_min(Q_L) ≤ (1−Γ_ij)κ^(2L),
    λ_max(Q_L) ≥ 3(1−2ε)².

The zero limiting readout makes the initial total kernel the readout block. Thus normalized conditioning also collapses. This is an initialization obstruction to a depth-uniform kernel bound, not a proof that every desired fixed-depth trained limit fails.

**Finite arctan fitting.** The fully read GF and GD coercivity notes settle a real finite optimization question. In feature time C″=D₃A₃D₃C with a PSD operator, giving convexity of the readout norm and a persistent top feature. Small RMS nonzero initialization is handled quantitatively; coordinate-sup smallness is not inserted. In GD the feature increment has an explicit O(√n α_k²) Taylor defect. A regularized readout norm is convex on interpolation segments; the accumulated negative knot jumps are bounded by Σα_k². Induction proves α_k=2η(1−f_k)>0 rather than presupposing it, closes the finite clock, and gives every finite parameter a fitting endpoint. None of this alone identifies a global population action law. The later Explain messages correctly retain that missing infinite-width continuation.

**Practical assessment.** Its 153 lines were read fully. Energy yields finite-dimensional path length and bounded raw population norms when a solution exists, not compactness in the required infinite-dimensional state or uniqueness from a generic L2 tail bound. Dense independent Gaussian near-identity layers do not behave like identity-residual blocks. A layer perturbation of size β/L gives vanishing accumulated nonlinear correlation correction under the stated bounded-variance expansion; variance-calibrated β/√L changes the initialization problem, not a trained result. The candidate is not evidence of a global joint limit.

## 4. Scientific scope and quantitative cautions

For phi(z)=az+eψ(z) with ψ Lipschitz constant ≤1 and a>e, independent-copy variance identities give

    Var(phi(Z)) ≥ (a−e)² Var(Z),
    A_phi(Z) ≤ e² Var(ψ(Z)) ≤ e² Var(Z),
    A_phi(Z)/Var(phi(Z)) ≤ [e/(a−e)]².

The same statement holds with any added constant. I read the complete relative-nonlinearity proof; this is valid for every nondegenerate finite-variance Z, not just Gaussian initialization. [Proof](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_activation_design/RELATIVE_NONLINEARITY.md:6).

Consequently the all-depth bounded-shape theorem's e=1 option is not a practical-amplitude conclusion: a≥10^12(1+192/δ²). For example the exact bound already gives e/a≤1/[10^12(1+192/δ²)]; no experiment is required to see the tiny relative fraction. The two-sample c_dyn and c_poly cutoffs are even more conservative. Historical logarithmic estimates of their astronomical smallness are provenance, not fresh numerical experiments; the exact symbolic constants in the manuscripts are the audited conditions.

This relative bound does not apply to the odd-gain theorem with e=a; its nonlinear-to-linear coefficient ratio is one. Its weakness for the user's no-gain/deep moderate-nonlinearity target is the large overall gain and absence of a depth-uniform relative margin, not a falsely claimed tiny coefficient ratio.

One-sample fitting, or interpolation of three distinct normalized samples when an offset supplies affine features, does not establish nonlinear function learning away from the training set. The theorem's nonaffinity observable concerns neuron activations under their own marginal laws; it is not an end-to-end input/output approximation lower bound, a generalization result, or proof that training relies essentially on nonlinear representational power. Initial nonzero hidden motion rules out an exactly frozen kernel locally, but not every quantitatively near-lazy description under other normalizations.

No manuscript here proves that these width powers are necessary, that GF forces a vanishing readout, or that the operator formulation/feature-learning phenomenon is novel to the literature. A common optimization step changes the clock as well as the displayed rates. The source group's Borel/Padé and initialization-jet continuations are formal/conditional reconstruction questions, not substitutes for the identified nonlinear global flow.

## 5. Task-history coverage, alternate continuations, and supersession

### Access limits and provenance

Local task IDs were resolved against [session_index.jsonl](/home/amir/.codex/session_index.jsonl:158), local metadata, accessible rollouts, and the read-only local history database. PDE-2 metadata was read from /home/codex-b/.codex/state_5.sqlite. Its display name field, not merely its initial-prompt title, distinguishes the Find tasks.

PDE-2 private session files remain unreadable as amir. No permission change was attempted. Its history database could be read only as an **immutable main-database snapshot** after ordinary read-only opening failed; that ignores any uncheckpointed WAL. It is supplementary older evidence, not proof of the newest complete transcript. SSH hostname resolution was unavailable. The preserved recovery files were therefore essential.

I read all 34 distinct final texts in [ORIGINAL_FOUR_ALL_BRANCH_FINALS.json](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/ORIGINAL_FOUR_ALL_BRANCH_FINALS.json:1), not just the latest visible task answers, and the complete associated [coverage inventory](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/ORIGINAL_FOUR_ALL_BRANCH_COVERAGE.json:1). The inventory reports 5/5/3/1 recovered rollout files and 18/9/5/2 distinct finals for Find root/(2)/(3)/(4). These are counts from prior recovery, not a claim that I newly accessed those private files.

### Assigned tasks actually covered

| Project/task ID | History read and exact result of reconciliation |
|---|---|
| PDE Resume research (4), 01a07740-6670-7863-bf1d-f588a0417d95 | Accessible local rollout and local checkpoint messages. Read its user requests, finals and research commentary, tracing the request at ordinal 6680 through the all-depth result at 7007. The principal SA proof was read fully. The direct local /tmp original and recovered archive have the same hash. |
| PDE Resume research (3), 01a07318-aba6-74d0-a4c0-2444beee801b | Both accessible base and alternate rollout (suffix 01a07346-6bc1-7243-8d72-67a1a7ba553d) checked; user/final/commentary evidence and the alternate final read. The extension is Borel reconstruction from initialization jets, conditional on transform/growth/identification assumptions. The alternate proposes fixed non-Taylor basis functions with a further coefficient-growth condition. Neither is a new unconditional global GF theorem. Full Borel manuscripts were not re-audited in this source group. |
| PDE Resume research (2), 01a072d1-4473-7c93-99bd-55554583c906 | Accessible rollout and checkpoint user/final sequence read, including the angle-specific authorization, later activation-uniform target, and stop. The final broad target remained unresolved, but that did **not** retract the earlier complete angle-specific theorem. The later separation-uniform source was read fully as an extension. Not every tool result in this long rollout was read. |
| PDE Generalize non-local GF, 01a07193-3b8a-77a1-a00f-4ae928368b82 | Accessible base and alternate suffix 01a072bc-1b1c-7560-8693-400cb513acce located. Main user handoff, accepted theorem final and local history read; alternate final headings/scopes inspected, including Borel/Padé and later exposition. Not all long alternate Borel/PDF answers read fully. The main GF proof, response lemma, activity proof and exact source amendment were read in full. User “non-local” explicitly meant fixed T*>0, not every finite T. |
| PDE-2 Find thread (4), 01a0804d-9bf4-71a2-8542-fc5b240235f9 | Recovered finals indices 32–33 fully read; immutable history adds checkpoint evidence. The broad shape theorem and fixed-amplitude sine local result are different claims. Latest metadata names the 2026-09-08T11-16-04 base rollout; recovered final entries come from that file. |
| PDE-2 Find thread (3), 01a07ce0-e69d-74d2-868d-c2edc3068c7d | Recovered finals 27–31 fully read across three branches. The depth-5/6/all-fixed-depth continuation at index 27 supersedes the older index-29 “L≥5 not proved.” The newer 01a07f8b branch is represented in recovered finals 30–31; it rejects gain as an answer to the no-gain target, without refuting the gain theorem. |
| PDE-2 Find thread (2), 01a07c68-9087-79b1-a4c1-536838241d32 | Recovered finals 18–26 fully read across the recovered branch collection; earlier odd-mixture existence, polynomial refinements, and three-sample failure to close are distinguished. Metadata points to newer suffix 01a07faf-c47a-7b83-a5eb-d7b852febe48, absent from the final-text file's listed provenance paths. I cannot certify unseen content in that latest private rollout; the prior inventory's count alone is not a substitute. |
| PDE-2 Find thread, user #4 “Work”, 01a07bd4-a15f-7d42-9559-f59d7a9e96ff | Recovered finals 0–17 fully read, including early mistaken scope, correction, separation-uniform theorem, three-sample gain and shape extensions, practical assessment, and alternate odd-mixture report. Metadata's latest suffix 01a080e9-5bd3-79d2-9efe-9bd67b615f3b, dated 2026-09-08T14-06-12, is not among final-text provenance paths; its unseen newest content remains unverified. Do not equate its path with a proved current version. |
| PDE-2 distinct Find research, 01a07b94-872c-7750-81c9-f3a5a2bea8a4 | Fresh metadata resolves this as a separate task, not the preceding “Work” task. Read all user/assistant messages present in its 93-item immutable checkpoint, including finals at ordinals 84 and 331 and the later unfinished question/commentary. It is retrieval/reconstruction discussion, not a new proved global theorem. Latest metadata suffix 01a07bcb-a226-7d30-bf68-e2765bdfc03e is private; checkpoint completeness/newest-branch content cannot be certified. |
| PDE-2 L=2 arctan/two inputs, 01a07114-b2fd-78b0-bb18-fa4c15cff3d6 | Read all seven completed-answer texts in recovered ARCTAN_TWO_CHRONOLOGY and the session coverage; inspected recovered user-message records and checkpoint finals. Three recovered files cover the base and alternates, including latest suffix 01a07186-5424-79c2-9f2c-1db3290497c5. Sequence: arbitrary-angle two/three-input local theorem, scaling/activity clarification, novelty corrections, global orthogonal-input activation extension, pause/handoff. The latest generalization request was handed to Generalize; it is not evidence that arbitrary-angle global time was solved here. |
| PDE-2 Explain audited proof, 01a04927-31c8-79d1-bd23-8196b13a1d9b | Inventoried all 40 recovered finals and read indices 23–39 fully, covering recent L=3 local/global distinction, completed finite GF/GD coercivity, unsuccessful population continuation refinements, stop/handoff and conjecture. Earlier 0–22 were scoped by chronology/headings, not all read in full; the long earlier teaching proof was not treated as a fresh certificate. Principal finite coercivity manuscripts and inherited L2 baseline were read fully. Latest metadata suffix 01a0707a-1fec-7762-875e-4e3ac36e4b39 is represented by the recovered recent chronology, but private raw contents were not newly accessible. |

The archived empty Find(4) duplicate 01a0804c-7657-7c73-92f8-4838a0837c4f is not the active assigned Find(4).

Local alternate rollout paths inspected:

- /home/amir/.codex/sessions/2026/09/06/rollout-2026-09-06T17-05-04-01a07740-6670-7863-bf1d-f588a0417d95.jsonl
- /home/amir/.codex/sessions/2026/09/05/rollout-2026-09-05T21-43-11-01a07318-aba6-74d0-a4c0-2444beee801b.jsonl
- /home/amir/.codex/sessions/2026/09/05/rollout-2026-09-05T22-33-10-01a07318-aba6-74d0-a4c0-2444beee801b_01a07346-6bc1-7243-8d72-67a1a7ba553d.jsonl
- /home/amir/.codex/sessions/2026/09/05/rollout-2026-09-05T20-25-12-01a072d1-4473-7c93-99bd-55554583c906.jsonl
- /home/amir/.codex/sessions/2026/09/05/rollout-2026-09-05T14-37-49-01a07193-3b8a-77a1-a00f-4ae928368b82.jsonl
- /home/amir/.codex/sessions/2026/09/05/rollout-2026-09-05T20-02-05-01a07193-3b8a-77a1-a00f-4ae928368b82_01a072bc-1b1c-7560-8693-400cb513acce.jsonl

### Supersession rules for the master

- Keep the accepted angle-specific result in Resume(2), then the later separation-uniform strengthening. Do not replace both with a terminal unresolved broader-target sentence.
- Keep the two-sample δ² refinement at L=3; the all-depth table's p₃=31/8 is not the best currently recorded L=3 exponent.
- Treat the all-depth two-sample extension, all-depth bounded-shape gain theorem, and all-depth odd-gain theorem as later results beyond the older L=3 master rows.
- Do not use all-depth offset/gain theorems to answer the literal convex/no-gain activation request. Those change the activation and deep variance recursion materially.
- Keep finite L=3 pure-arctan global optimization separate from its unresolved global population identification. A finite coercive kernel is not the missing canonical incoming-tail estimate.
- Keep Borel/formal/internal-oracle claims separate from actual trained-width limits.
- Newest private continuations not preserved in readable recovered content remain missing, even where a metadata title/path/date is known.

## 6. Read ledger, dependency limits and source integrity

### What was read in full

Every proof file in the hash ledger below with a line count was read completely by this auditor, including the current companion files, the inherited L2 baseline, and the two generic three-sample bridge chapters. Full reads sometimes required multiple chunks; they were not replaced by summaries, PASS labels, or code output. Principal theorem recommendations are graded according to these reads and their remaining dependencies.

Scoped rather than complete reads include: the old master and old audit appendices as locators; short RESULT files and dependency manifests; long task histories as specified above; selected primary external theorem statements; and the older Borel/Padé/exposition branches. Hashing a file is not reading its proof.

Not independently re-audited in full:

- The extensive older affine/reference, original nonlinear response/continuation, and fixed-cap observational dependencies behind the two-sample E rows. Their dependency lists contain 28–30 files. Current extension/source-algebra checks are not an end-to-end re-proof.
- The older L=3-only three-sample shape manuscript, whose current broad representative is the fully read independent all-depth manuscript. Its broader original separation range is not silently added to the all-depth theorem's stated δ<1.
- The older special-angle L=2 two-sample pure-atan package, bounded same-label L=3 two-sample variants, mixed plateau/near-identity variants, and older all-angle compactness-only sources. These remain historical variants, not newly certified principal claims here. L2-G subsumes orthogonal-input global regularity, but not automatically every stronger observable/activity assertion in each older special-angle package.
- The inherited 2,321-line L=3 pure-atan local manuscript. SG plus the diagonal corollary supplies the modern broad positive-time conclusion, subject to SG's external dependency, but I did not independently renew every old local claim.
- The old order-one-Gaussian-readout L=2 operator-IDE manuscript. Do not combine its initialization or observable scope with the small/bounded-readout L2-G theorem.
- Separate calibrated initialization notes and unfinished moderate-activation global continuation drafts. The fully read practical assessment/source note does not turn those into global theorems.
- Tensor Programs III's complete proof; other external literature mentioned in old discussion messages was not used as an audited premise or to assert novelty.

Read-only code/certificate work was limited to source discovery, parsing preserved histories/metadata, comparing files and dependency manifests, and SHA-256 computation. No numerical model, simulation, coefficient search, or experiment was run.

### Version comparisons actually performed

- All 26 entries in GENERALIZE_COPY_PROVENANCE, all 15 in ARCTAN_TWO_COPY_PROVENANCE, and all 82 in EXPLAIN_COPY_PROVENANCE matched their current archived file hashes. This checks archive integrity, not every proof in those collections.
- SG's final-vs-reviewed diff was read fully: the status paragraph changed, and “Gaussian first weights” was added explicitly to strict activity. The final main/response/activity hashes agree with the copy manifest and the applicable final checksum list.
- SA's recovered 1,727-line proof hash matches its recovery provenance, and the readable direct local /tmp/general-depth-proof-QpSvt6/GENERAL_DEPTH_SELF_CONTAINED_PROOF.md has exactly the same hash.
- The current all-depth bounded-shape manuscript matches its own final review manifest hash efa3…e4a; the current odd-mixture report matches its final manifest cd62…037. The latter manifest explicitly certifies only partial/conditional results. These are content-identity checks, not reliance on the verdict.
- All six odd-gain dependency hashes, all 28 all-depth two-sample dependency hashes, all 30 δ² dependency hashes, and all 28 broad-shape dependency hashes matched current repository bytes.
- The inherited L2 proof matches COPY_PROVENANCE's f066…17f.
- The recent repository manuscripts and their local manifests are consistent with the paths/scopes named in recovered finals. Private PDE-2 author rollout files could not be freshly hashed. Equal apparent /home/amir/Codes/PDE or /tmp paths on different hosts do not prove byte identity. The report therefore identifies **the local/recovered bytes actually audited**, and does not claim those are necessarily every newest private-host revision.

### SHA-256 ledger

Paths in this ledger are relative to /home/amir/Codes/PDE/studies/mean_field_peeling. A line count marks a fully read proof/source file; uncounted entries are the history/provenance artifacts used for reconstruction. Links to decisive theorem/proof sections appear above.

    5406c9e3a812127be623d22e225ac545e83bc8ea1010b5046bd4bab6a295514d 524 four_thread_consolidation/expanded_sources/GENERALIZE_PRIMARY/GENERAL_POPULATION_GF_PROOF.md
    3dfb63e3cac21ee15573af7f4107287f58dc2013db7e4a11083c90472bf8995b 540 four_thread_consolidation/expanded_sources/GENERALIZE_PRIMARY/GENERAL_DEPTH_RESPONSE_PROOF.md
    c6bfa76ac200ce59f91109b31a40d22d668ec678e2ea60386f93f7d7604b4e89 373 four_thread_consolidation/expanded_sources/GENERALIZE_PRIMARY/sources/GENERAL_ACTIVATION_ACTIVITY.md
    741331782e571a38ed11896fc342f2ce6291d63b057d456419d799757fe4327f 1727 four_thread_consolidation/expanded_sources/SHIFTED_ATAN_ALL_DEPTHS/GENERAL_DEPTH_SELF_CONTAINED_PROOF.md
    efa3c2b1e592a469d8aa7900e95f0a8a43a4a1865b9c4c3f69f3bacfcb613e4a 2864 activation_class_all_depths/MANUSCRIPT.md
    e8088b9554332c2d45250dec5e1b0004badb0252e5cfe63cefde0f8896e59f66 414 three_sample_odd_gain_all_depths/PROOF.md
    c4dd77974660a1c7f556042f748c348af1fd3c2953d2e7220d508ee0960286f9 193 three_sample_odd_gain_all_depths/SOURCE_RESPONSE.md
    e7982d74e4004973ac3cdaa20715c9ad70fb9fd4ba04ad5b36e78fa8a222713c 332 three_sample_odd_gain_all_depths/POPULATION_LIMITS.md
    dc4260ff571a3182362af01606706d7e0077d34d7552f0192ab340333a5fb12d 251 three_sample_odd_gain_all_depths/INITIAL_MOTION.md
    356eddd6a5154d9099492cb0b676feebfc0bc16fd7c462144fe700da426b65b9 806 four_thread_consolidation/expanded_sources/arctan_two_primary/GLOBAL_ACTIVATION_TRANSFORM_EXTENSION.md
    366bf83ff0250a42da9f4f2fae7d51f0dd296cfb2ea3c462761423fec09e8d70 470 two_sample_odd_activation_depth56/PROOF.md
    50d09b24de8fe6aa8cbf0d068f71f71596bcefc227c5d745191c69fdcaab095a 261 two_sample_odd_activation_depth56/AFFINE_CERTIFICATE.md
    9a05a1b7d4e2075156cb1483c69ed80e7ab02f9fd84de2c6d8a704f2466049b1 234 two_sample_odd_activation_depth56/SOURCE_RESPONSE.md
    dd49edf52076dce683934f90df58e0ff2362e14fa02c00edd0d2cabd49b43c8b 126 two_sample_odd_activation_depth56/POPULATION_AND_MOMENTS.md
    1ec4886b450deafb255c60a3e053d5c7c32ef3c02ad9a2aa41e50f0db7f98e7a 317 odd_activation_lower_powers_three_inputs/TWO_INPUT_PROOF.md
    2f2e7e66f4d754fca842ebf9524e605ba846c5e2445fc9792e263c859f62d725 322 odd_activation_lower_powers_three_inputs/SECTOR_RESPONSE.md
    17d8bac86024c2dff6344f95d948c9783ad6f64b2fd12441ea5c953c08387076 279 odd_activation_lower_powers_three_inputs/WEIGHTED_AFFINE_AND_CLOSURE.md
    c36d92166c65affeb7974c5fe07ddfaa8697399b56d3c4322e89db51a02748ce 322 two_sample_activation_design/PROOF.md
    58432555e59bc191e98cb7fda7e1063d22410933c2cb5816003f6e5bbe061540 363 two_sample_activation_design/SHAPE_SYMMETRY.md
    5e06d3414959abef70cfbe569f1b393df689ad3826e31d391149d556ad861bd9 303 two_sample_activation_design/LINEAR_GROWTH.md
    bcaa95026a90736f32cd4e2cdd8f2a662439afa20051abb9522918becab2070f 111 two_sample_activation_design/RELATIVE_NONLINEARITY.md
    2891b892667396d64bd747689bcd59aa7ca3ffd224d3579fc3407bca0b623f9a 527 two_sample_separated_angle_theorem/PROOF.md
    4bfa60f57e8a226ed73ae85c225f28a17562f26b1aa498351e3617069c94be1e 309 moderate_sine_global/LOCAL_SOURCE.md
    cd62425a6d8ae0ca7351bb6e71b31cd0b4eb7266263e53e377f976bab261e037 643 odd_mixture_general_depth/REPORT.md
    a6dae64cd54b9ab34520d2b493b78cefbbd4c868b5c222552e169982aff9f668 291 convex_offset_all_depths/REPORT.md
    e105601d38f9df2dfbe58eab127f56ec842733214f811fc665453de52faeb9b6 153 practical_global_limit_assessment/ASSESSMENT.md
    0bd062da74fbde03d41a125561beee7345915ea6aa0578ed8e7b81d2c9f08c53 422 four_thread_consolidation/expanded_sources/EXPLAIN_PRIMARY/l3-full-resolution-9nbD4z/READOUT_COERCIVITY.md
    fcac71917f0a0c60c4368d7c86167aae0689ae87778622ab8745ac213fa9c35c 596 four_thread_consolidation/expanded_sources/EXPLAIN_PRIMARY/l3-full-resolution-9nbD4z/EXACT_GD_COERCIVITY.md
    f465df5d3ab7b56fcf4212d15eaf287a948e832cc453d1f1bbddcbbf35d4c59d four_thread_consolidation/expanded_sources/ORIGINAL_FOUR_ALL_BRANCH_COVERAGE.json
    8621eb30a81c87b2452ce01d44f20c465d84c329a0f8c60479fa5a6639d70f61 four_thread_consolidation/expanded_sources/ORIGINAL_FOUR_ALL_BRANCH_FINALS.json
    057953c6edb9d900adba633f2c93520d0dec005f0763de748909608aaae7d355 four_thread_consolidation/expanded_sources/EXPLAIN_ROLLOUT_FINALS.json
    0f5e67b9e0a3007aeadea6d4a273c7f6f55e99e23a789647fad1561ee7656caf four_thread_consolidation/expanded_sources/ARCTAN_TWO_CHRONOLOGY.txt
    c894fc98d24cc34d91e4b4989780ebaac27e9d4285914099d70a593db5b35710 four_thread_consolidation/expanded_sources/ARCTAN_TWO_SESSION_COVERAGE.json
    f0660112d066a5955d356909bc7f6d4b7086b571a7bf2f4b9675eb882a31017f 543 four_thread_consolidation/inherited_baselines/L2_ONE_SAMPLE_ARCTAN_GLOBAL_PROOF.md
    d4ec349056af9a265cf583a5e6196a8d17d1ae4eed4e764a85a1e9b59345dc55 624 three_sample_self_contained/foundations.md
    36c8f3e5b89d766cf1137ab6fd21346a978272e407400249194c1ed132d20184 638 three_sample_self_contained/velocity.md

## 7. Consolidation decision

Recommend retaining the global identified limit families with their exact data, depth, gain/readout, clock and observable qualifications; the SG finite-GF corollary should be added explicitly. Mark the two-sample refinements as current source-supported theorems with a fresh extension audit but an incompletely re-audited legacy chain. Mark SG/L2-G's nonclassic fixed-program dependency unaudited in this isolated report.

The scientific frontier remains the canonical trained global limit with meaningful nonlinear effects for substantially broader data/activation regimes, especially the exact no-gain three-sample family and moderate activations. Existing initialization bounds, conditional continuation, finite optimization, and tiny-near-affine or enormous-gain witnesses answer different questions. The absence of accessible newest private task content is a coverage limitation, not evidence for or against any mathematical theorem.
