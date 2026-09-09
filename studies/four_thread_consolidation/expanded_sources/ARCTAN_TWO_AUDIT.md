# Audit of “L=2 arctan, two inputs” and its inherited one-sample baseline

Read-only evidence consolidation, 2026-09-08. Task `01a07114-b2fd-78b0-bb18-fa4c15cff3d6`, host `remote-ssh-discovered:black-chatgpt-2`. No new proof search, experiment, or modification of original manuscripts was performed. Original `/tmp` artifacts were recovered and preserved as exact byte copies under [arctan_two_primary](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary), with [copy provenance and SHA-256 hashes](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/ARCTAN_TWO_COPY_PROVENANCE.json).

The old consolidation omitted complete **L=2, pure arctangent, two- and three-input semi-global joint theorems**, and a **global L=2 theorem for a broad activation class and any fixed number of orthogonal inputs**. The last theorem also permits arbitrary real labels and a bounded nonvanishing readout law. These are substantive extensions of the existing inventory, not just intermediate lemmas. Their historical checking levels differ and are stated below.

“Verified” here means a saved mathematical argument with the recovered checking described at the claim, not formal proof-assistant verification or a new independent re-proof. A recovered source without a matching complete review is explicitly distinguished from the complete three-PASS results.

## Exact common contract for this task

Here L is **two hidden layers**, even though the readout is called W^(3). For fixed m inputs x_a in R^d, set u_a=x_a/sqrt(d), ||u_a||=1, and G_ab=<u_a,u_b>. The finite network is

- z_a^(1)=W^(1)x_a/sqrt(d), h_a^(1)=phi_1(z_a^(1));
- z_a^(2)=W^(2)h_a^(1), h_a^(2)=phi_2(z_a^(2));
- f_a=(W^(3))^T h_a^(2)/n, r_a=f_a-y_a, loss=sum_a r_a^2.

W^(1) is n by d, W^(2) is n by n, and W^(3) is a length-n **stored rescaled readout**. Base initialization has independent entries W1~N(0,1), W2~N(0,1/n), W3~N(0,n^-2). Layer learning-rate multipliers are (n,1,n), relative to physical step eta_n. Thus

    z_a^1,+ = z_a^1 - 2 eta_n sum_b G_ab r_b delta_b^1,
    W2,+ = W2 - (2 eta_n/n) sum_b r_b delta_b^2 (h_b^1)^T,
    W3,+ = W3 - 2 eta_n sum_b r_b h_b^2,

where delta_a^2=W3 phi_2'(z_a^2) and delta_a^1=phi_1'(z_a^1)(W2)^T delta_a^2. Finite parameters interpolate linearly on t=k eta_n; the forward pass is recomputed between steps. The population initialization W3=0 is a limit of the actual finite Gaussian readout, not a change to the actual algorithm.

This loss has **no factor 1/2**. Its prediction and loss identities are dot r=-2Kr and dot loss=-4r^T Kr. The master report's modern half-squared-loss convention must not be substituted without rescaling time. Equivalently its first effective forward matrix W1/sqrt(d) has entry variance 1/d; the normalization difference is representational, while the factor two in the physical clock is substantive.

For all complete joint results below, convergence is full-sequence in probability for each fixed dataset. The state retains first-layer fields, one shared middle operator and its actual adjoint, and readout; it is autonomous in its joint action law. Uniqueness is on the source's bounded-operator and bounded-readout-supremum class, with field coordinates in mean square. This is not unrestricted uniqueness over arbitrary L2 states, nor a finite-dimensional ODE closure.

The joint conclusions include finite GF identification and actual raw-GD convergence, predictions/residuals/loss, all three true kernel blocks, fixed finite generated probes using both operator orientations, same-layer **joint m-input** hidden path laws in W2 for the uniform path norm, second moments and integrated squared hidden speeds. Both varying factors of an ordinary product probe must be bounded; the specifically needed unbounded backward fields and quadratic contractions are supplied by explicit tail arguments. No cross-width operator-norm convergence, arbitrary higher-growth probes, or natural pairing of neurons across different hidden layers is claimed.

## Accepted complete results omitted from the old master

### AT1 — Two nonparallel inputs, pure arctangent: semi-global joint theorem

**Status: complete proof; three isolated full-manuscript PASS reviews.**

- L=2; m=2; phi_1=phi_2=atan; any fixed rho in (-1,1); arbitrary y_1,y_2 in {-1,1}.
- Base independent Gaussian initialization and exact raw updates above.
- There is a fixed T0>0, independent of n and eta_n, and **every positive sequence eta_n→0** gives the complete joint result on [0,T0]. No eta_n sqrt(n) restriction is needed on this local interval.
- On a possibly shorter fixed interval (0,T*], each input moves in both hidden layers; all three 2 by 2 kernel blocks are positive definite; the total kernel changes; summed loss strictly decreases; both hidden marginals have positive variance and positive best-affine regression error for atan.
- Strict hidden RMS speed is proportional to t near zero, not bounded away from zero as t↓0. Squared hidden displacement has a positive t^4 coefficient; integrated squared speed has a positive t^3 coefficient. The kernel's label-direction expansion has positive coefficient 8(A1+A2)t^2.
- The full local result was not superseded by a failure. Global time for **nonorthogonal** pure-arctangent inputs remained open in this task. The orthogonal case additionally has AT3's global result under its stronger step condition.

Authority: [complete proof](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/TWO_INPUT_LOCAL_LIMIT_PROOF.md:3), [review record](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/TWO_INPUT_LOCAL_LIMIT_REVIEW.md:1), and exact reviewer messages at original-rollout ordinals 1514, 1525, 1531 in [review extracts](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/ARCTAN_TWO_REVIEW_EXTRACTS.md:197). The precursor tail lemma separately received two isolated PASS reviews; it is subsumed by the complete theorem.

### AT2 — Three pairwise nonparallel inputs, pure arctangent: uniform semi-global joint theorem

**Status: complete proof; three independent full-manuscript PASS reviews.** The named reviewers had also checked AT1; the record says they were not supplied the exploratory derivations or one another's conclusions, but this audit does not call their contexts freshly isolated.

- L=2; m=3; phi_1=phi_2=atan; normalized inputs with x_a≠±x_b for a≠b; **singular G is allowed**; all eight binary-label patterns.
- Same actual initialization and raw updates, with sums over three samples.
- A **single absolute T0>0 works for all these normalized triples and binary labels**, independently of input dimension, width, learning rate, auxiliary mesh, and any lower input-Gram eigenvalue. The source chooses constants from |G_ab|≤1 and m=3, then imposes its bootstrap inequality C1 T0^2(MC+C0)≤1/2. It does not give a numerical evaluated T0.
- Every positive eta_n→0 gives all joint observables above. This is not a convergence-rate assertion uniform over datasets changing with n.
- All six hidden preactivations move on some smaller (0,T*]; all three kernel blocks are positive definite there; the total kernel changes; loss has strictly negative initial slope; all six hidden variances and best-affine errors stay positive on a short interval. T* and the strict positive margins may depend on the fixed geometry and labels.
- The first-layer relation induced by null(G) remains exact, but the initialized **activation** Gram Q is positive definite. The proof checks this by a Vandermonde argument for arctangent ridge functions. A new Gaussian innovation in each reused forward call proves motion of each second-layer sample individually; aggregate positivity or two-input exchange symmetry is not used as a substitute.

Authority: [complete proof and exact scope](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/THREE_INPUT_LOCAL_LIMIT_PROOF.md:3), [review record](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/THREE_INPUT_LOCAL_LIMIT_REVIEW.md:1), exact PASS messages at ordinals 1740, 1755, 1763 in [review extracts](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/ARCTAN_TWO_REVIEW_EXTRACTS.md:268).

This result is stronger than the previously retained L2/m3 **population-only** theorem for small convex mixtures in time/limit scope, but uses pure atan. It does not prove the separate requested no-gain mixture theorem for 0<theta≤1/2, and must not be used to erase that open question.

### AT3 — General activations, any fixed finite orthogonal dataset: global joint theorem

**Status: complete recovered manuscript with separate independent existence/GD and strict-activity checks; not three fresh isolated whole-manuscript PASS reviews.**

- L=2; any separately fixed m<∞; G=I_m, hence m≤d. This includes one input.
- phi_1 in C1(R), phi_1' bounded and globally Lipschitz; phi_1 itself may be unbounded, nonmonotone, have derivative zeros, or be affine/constant.
- phi_2 bounded and C1(R), with bounded globally Lipschitz derivative.
- Arbitrary fixed **real** labels y_a.
- Independent W1 Gaussian with fixed finite variance sigma1^2, W2 Gaussian with entry variance sigma2^2/n. Positive fixed learning constants kappa1,kappa2,kappa3 give multipliers (n kappa1,kappa2,n kappa3). Existence itself permits zero initialization variances; strict activity uses positive sigma1,sigma2.
- Readout alternatives: (i) Gaussian sigma3^2 n^(-2 beta), any beta>0; (ii) more generally an independent readout with coordinate supremum→0 in probability; (iii) fixed bounded iid initial readout law on [-B0,B0], optionally plus a perturbation with supremum→0. The population starts from the actual limiting law. **Order-one unbounded Gaussian readout is excluded from this particular proof.**
- One autonomous population flow exists on every fixed finite [0,T]; finite GF and raw GD converge jointly under **eta_n>0 and eta_n sqrt(n)→0**, including eta_n=n^-2. The activation and initialization choices are fixed before T; this is not uniform convergence on [0,∞).
- The core exact scalar flow J_s=phi_1'(J), J(0,z)=z, supplies a gate-removing displacement coordinate even if phi_1' vanishes or changes sign. The proof controls clocks and operator norms globally on each finite horizon. Finite GD is compared by an exact effective-clock increment with quadratic defect; the final manuscript includes both requested audit additions, clock control and the path-grid inequality.
- Examples permitted **as the whole activation in both layers** include atan, tanh, sigmoid, erf, softsign, rational saturation z/sqrt(1+z^2), sine and cosine. Softplus, GELU and SiLU are additional first-layer examples with a bounded qualifying second activation. ReLU/derivative jumps are not covered.

With additional sigma1,sigma2,kappa1,kappa2,kappa3>0, zero limiting readout, binary labels, nonaffine phi_1 and nonconstant phi_2, the manuscript proves all-input movement in both hidden preactivations, nonzero middle action change on each initial activation, nonconstant kernel with all three blocks positive definite for small positive time, strictly positive short-time loss-descent rate, and positive best-affine errors/variances. Those are **short-time**, geometry/activation-dependent statements along a globally existing flow; they are not permanent activity claims. The manuscript does not state this strict package for its bounded nonzero readout alternative or for every real-label choice.

Authority: [complete theorem and proof](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/GLOBAL_ACTIVATION_TRANSFORM_EXTENSION.md:5). On the continuation rollout, ordinal 2340 is an independent PASS for initialization/global existence/fixed-mesh identification/raw-GD, with two requested explanatory completions. Ordinal 2303 independently passes the strict-activity argument conditional on the established flow. Ordinal 2425 confirms the polished manuscript incorporates both additions; the additions occur explicitly in current equations (21) and (23). Exact evidence is at [review extracts](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/ARCTAN_TWO_REVIEW_EXTRACTS.md:433). No historical content hash was supplied; present copies are byte-matched and hashed, but not described as historical hash-certified.

This completed turn is **absent from the current active-branch Page1 export**: it survives in the exact-session continuation rollout ending at ordinal 2434, turn 01a0716a-55c2-7211-be65-c4a2f8ef2e22. The later user clarification branched from an earlier point and then paused work. That branch change is not a mathematical retraction of AT3.

### AT4 — Affine first activation: global joint theorem for arbitrary fixed input geometry

**Status: proved exception within AT3's recovered complete manuscript; shares its scoped checking, without a separate fresh full-review certificate.**

For L=2, any fixed finite normalized input collection (arbitrary PSD G, including coincident/antipodal inputs and singular G), arbitrary fixed real labels, affine phi_1(z)=cz+d0, and the same bounded C1 phi_2 class, initialization and readout alternatives as AT3, the global population/GF/raw-GD theorem holds. Since the first derivative is constant, raw GD is ordinary Euler for the controlled raw-state vector field and only **eta_n→0** is needed. No inverse G is assumed. This exception has exactly zero first-layer activation best-affine error, so it does not answer the user's demand for genuinely nonlinear activations at every layer.

Authority: [arbitrary-geometry exception, equations (24)–(25)](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/GLOBAL_ACTIVATION_TRANSFORM_EXTENSION.md:536).

## Distinct checked extensions, with their narrower review provenance

### AT5 — Hyperparameter family for AT2, including bounded nonzero readout

**Status: complete bridge-check derivation plus separate component checking; no recovered fresh whole-manuscript review of the entire extended family.**

[THREE_INPUT_SCALED_LIMIT_EXTENSION_CHECK.md](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/THREE_INPUT_SCALED_LIMIT_EXTENSION_CHECK.md:1) checks every modification to AT2 for fixed positive finite sigma1,sigma2, finite sigma3≥0, any beta>0 in W3,0~N(0,sigma3^2 n^(-2 beta)), and multipliers (n·κ_{1,n}, κ_{2,n}, n·κ_{3,n}) where κ_{l,n}→κ_l in (0,∞). All positive eta_n→0 remain allowed. Exact zero readout is included. A common T0 may be chosen over bounded parameter sets; no lower G eigenvalue enters. Population first-layer covariance becomes sigma1^2 G. The Gaussian covariance **and both response sums** acquire sigma2^2, but the learned memory acquires kappa2, not sigma2^2. The physical kernel is kappa1 K1+kappa2 K2+kappa3 K3.

The same note separately establishes local existence/convergence for bounded nonvanishing iid readout, with that sampled root used in the oracle. Its backward response cap is O(1+B0), rather than O(T), and its T0 depends on the bound B0. This is a distinct population initial state. It does not inherit the zero-readout t^2 hidden-displacement expansion or strict changing-kernel proof. Order-one unbounded Gaussian readout remains outside this proof.

The positive-scale strict-activity expansions are supplied in [three_input_activity_lemma.md](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/three_input_activity_lemma.md:1), including hidden **activation** speeds (not just preactivation speeds), middle-action movement on each old activation, weighted kernel and best-affine margins. Independent ordinal 1934 PASS checks these three feature statements. The existence/scaling author gives its final verified bridge report at ordinal 1892. See [review extracts](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/ARCTAN_TWO_REVIEW_EXTRACTS.md:359). These are stronger constant/readout quantifiers than the base three-PASS manuscript and should retain that provenance distinction.

### AT6 — AT2's existence/limit part does not require nonparallelity or binary labels

**Status: recovered convergence/existence extension check; the three full theorem reviews explicitly concern AT2's binary/nonparallel statement.**

[THREE_INPUT_LIMIT_EXTENSION_CHECK.md](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/THREE_INPUT_LIMIT_EXTENSION_CHECK.md:1) proves the same local autonomous joint limit for **any normalized triple** G≥0, G_aa=1, and any labels |y_a|≤1, including coincident/antipodal samples. The common time uses only m=3 and |G_ab|≤1. The check explicitly separates strict nondegeneracy, which fails in some such cases. Its equations show that null(G) relations are exactly preserved without preventing population existence or the joint finite limits. This is a substantive weaker-conclusion/wider-input result, not a fitting theorem.

## Inherited one-sample result retained once

### AT0 — L2, one sample, pure arctangent, small readout: global joint

The inherited complete one-input theorem (x=y=1, same base initialization and loss (f-1)^2) gives global autonomous population existence and joint finite GF/raw-GD on each fixed [0,T], with eta_n sqrt(n)→0; hidden paths in W2, integrated squared speeds, all three kernels and its corrected action-probe class. Strict nonlinearity/activity is asserted only initially. Its polished complete proof and accepted round-two proof were read/reconciled; the old broad product wording was corrected before three new complete isolated PASS reviews.

The source is already permanently archived in [the existing inherited proof](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/inherited_baselines/L2_ONE_SAMPLE_ARCTAN_GLOBAL_PROOF.md:1) and [review record](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/inherited_baselines/L2_ONE_SAMPLE_ARCTAN_GLOBAL_REVIEW.md:1). AT3 generalizes its activation/scaling/orthogonal-data scope. Keep AT0 as a baseline with its stronger three-isolated-review evidence; do not count successive notation rewrites or earlier repairs as additional theorems.

The earlier order-one-Gaussian-readout arctangent operator theorem in the existing master is a different initialization/observable contract and is not replaced by AT0 or AT3. No extension to that initialization should be inferred from their bounded/vanishing-readout proofs.

## Substantive auxiliary outcomes and negative boundaries

The following are results about an implication or a proof obstruction. They must not be presented as unconditional failure of the population limit. Where their checking does not match AT1/AT2, that is explicit.

1. **Exact scalar-coordinate obstruction for correlated nonlinear inputs.** AT1/AT2 equation (M3) shows that the atan cubic coordinate produces off-diagonal factors (1+(Z_a^1)^2)/(1+(Z_b^1)^2). They are unbounded when G_ab≠0. This invalidates a direct transcription of the scalar/orthogonal global Lipschitz proof; it does not disprove global existence. The accepted local tail proof closes the short-time gap. AT3's scalar-flow transform and AT4's affine exception are the final positive statements for that method.

2. **A complete conditional global criterion remains useful.** [GLOBAL_MULTIINPUT_EXTENSION_ATTEMPT.md](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/GLOBAL_MULTIINPUT_EXTENSION_ATTEMPT.md:1) proves: for the same L2 bounded-activation/arctangent finite-mesh system, if for every fixed T there are c_T,C_T>0 such that sup_mesh,max_(a,k: k Delta≤T) E exp(c_T |P_a,k|)≤C_T, then the full global autonomous population/GF/raw-GD theorem follows for arbitrary fixed finite normalized datasets and eta_n→0. Partitioning [0,T] makes the exponential tail beat the localized Gronwall factor. Gaussian tails are more than needed. The premise is a property of already-defined population Euler calculations, not an assumed global flow. The note is a complete conditional derivation by its author, with no isolated full-review certificate recovered; its premise was **not established** globally.

3. **State norm bounds do not prove the missing adaptive tails.** The same primary note gives a bounded-query construction: an independent event E of probability epsilon, V=1_E, forward answer sqrt(epsilon)G0, and bounded transpose query U=atan(G0). Then (W0)^*U=Gamma+c epsilon^(-1/2)1_E, c=E[G0 atan(G0)]>0. Query amplitudes and initial L2 operator norm are bounded, while no common exponential-moment bound exists as epsilon→0. This is an explicit counterexample to deducing such moments from those bounds alone. It is not a path of the trained neural GF; the query derivative grows with epsilon^-1/2. The note also distinguishes endpoint L2 closeness from propagation of tails, so restarting the local independent-root lemma at a correlated endpoint is unjustified without a new response estimate. These are checked derivations in that note, without a separate complete isolated review.

4. **Hidden speed at initialization is zero for the vanishing-readout model.** The accepted expansions show hidden speed =Theta(t) for small positive t, while loss slope is already strictly negative at t=0. Thus a literal time-independent positive hidden speed on (0,T*] is false for this initialization. This does not undermine non-lazy feature learning at each fixed positive time.

5. **The positive scaling assumptions have real content.** The recovered arctan activity note proves that sigma1=0, sigma2=0 or kappa3=0 freezes the zero-readout population initialization; kappa1=0 freezes the first hidden layer; kappa2=0 freezes the middle matrix but need not freeze both preactivation layers; kappa1=kappa2=0 leaves readout-only training with constant kernel. These are exact boundary cases of the activity claims, not necessary-and-sufficient classification of all scalings.

6. **The inherited broad product-probe claim was false and was corrected.** The three initial one-sample reviews rejected “product with a clipped factor,” because one bounded varying factor multiplied by an unbounded varying factor need not obey the claimed Lipschitz state estimate. The accepted contract bounds both varying factors and separately handles named unbounded backward products through square-tail control. The old failed wording is not a surviving theorem.

7. **No new necessary scaling law was proved.** Both high-level comparison turns preserve the mathematical distinction between fixed-step width convergence and the joint eta_n→0 width limit with T/eta_n→∞, but they establish neither uniqueness of this scaling nor a contradiction of muP. This is a scope exclusion, not an additional research theorem; literature/novelty discussion is omitted from the accepted-result table.

## Latest paused work: preserve the boundary, not a nonexistent theorem

The final active branch asks for a broad absolute-positive-time extension, then explicitly requests a pause and supervisor handoff. The [handoff](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/PDE_GF_SUPERVISOR_HANDOFF.md:1) says no new broad theorem was delivered and identifies unfinished arguments.

- `/tmp/GENERAL_ACTIVATION_TWO_HIDDEN_LIMIT.md` **did not exist when the work was paused** and is absent now. This is a documented unfinished artifact, not an inaccessible completed proof to be inferred from conversation.
- [GENERAL_DEPTH_LIMIT_CHECK.md](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/GENERAL_DEPTH_LIMIT_CHECK.md:1) is a fixed-depth response-bootstrap draft for bounded C2 activations and derivatives. Although its text says its bootstrap closes, the final handoff explicitly calls it in-progress, possibly predating later reasoning, and not audited. Do not promote it to a completed arbitrary-depth arbitrary-geometry joint theorem or use it to fill the still-missing source.
- [GENERAL_ACTIVATION_ACTIVITY.md](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/arctan_two_primary/GENERAL_ACTIVATION_ACTIVITY.md:1) is a completed **conditional activity** note, assuming a strong mean-square population flow. It covers any fixed m pairwise nonparallel inputs, nonzero real labels, bounded nonconstant C1 activations with bounded derivatives; a broader conditional version permits nonaffine activations with bounded continuous derivatives. Its ridge-function independence, response-covariance and per-input innovation arguments are substantive conditional calculations, but no final isolated complete review was recovered and existence/width/GD for the whole class was unfinished. It is archived as conditional, not entered as a verified joint theorem.

These latest drafts do not retract AT1–AT6 or AT0. The fixed-depth draft is also not evidence that no such later theorem exists in a successor task; it only sets the boundary of this task's accepted state.

## Chronological coverage and supersession ledger

The current Page1 export alone is insufficient. Its active ancestry skips two mathematically relevant alternative turns. I located and read all **three exact-session** rollout files, extracted all completed turn finals and all relevant review messages, and reconciled the primary manuscripts. [Machine-readable coverage](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/ARCTAN_TWO_SESSION_COVERAGE.json) records file hashes, ordinals and completed turn IDs; [chronology](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/ARCTAN_TWO_CHRONOLOGY.txt) preserves all completed-turn text across the branches.

| Turn / source interval | Full relevant outcome | Disposition |
|---|---|---|
| Inherited 01a06e39, in Page1 | Polished one-sample global theorem; first-round product-probe rejection repaired; three new isolated PASS reviews | AT0 retained; older proof and notation repair files superseded |
| 01a07116; original rollout 1159–1561 | Two-input local proof, response lemma, complete final reviews | AT1; failed cavity route excluded except its valid generic tail obstruction already represented above |
| 01a0712b; original 1563–1780 | Three-input generalization, singular geometry, uniform time, complete final reviews | AT2, plus wider convergence-only check AT6 |
| 01a0713a; original 1782–1955 | Strict velocity/nonaffinity, hyperparameter and bounded-readout checks | AT5 and explicit activity/boundary statements |
| 01a0714a; original 1957–2048 | First muP/high-level interpretation answer | No new theorem; scaling/novelty overclaims excluded |
| 01a07152; continuation 1959–2092 | Revised longer muP/high-level comparison | Expository replacement; no new mathematical theorem |
| 01a0716a; continuation 2094–2434 | Completed broad global activation theorem; conditional arbitrary-angle criterion; independent scoped checks; final corrections | AT3/AT4 retained despite absence from current active-branch Page1 |
| 01a07186; last continuation 2096–2327 | Clarified fixed-positive-time broad-class attempt; interrupted for handoff | Incomplete depth/existence work excluded; conditional activity note preserved with limits |

The ordinal ranges overlap because the continuations branch; they must not be merged into one monotonically increasing file or deduplicated by ordinal alone. The completed broad-global turn preceded the final clarification in wall-clock time and its final primary artifact survives.

The local exact-session files begin at fork ordinal 1155. The coordinator subsequently supplied Page2 and Page3; Page3 hasMore=false exhausts the visible ancestry. Their eleven older turns (01a04927, 01a0492d, 01a0492f, 01a04933, 01a04938, 01a0493f, 01a04946, 01a04947, 01a0525e, 01a0526e, 01a0539e) concern AT0 teaching, notation, topology, limit order and a pedagogical one-population toy. They add no separate trained L2 theorem beyond the later polished AT0. The toy uses a fixed sign readout and one evolving scalar population and is excluded from the fully trained two-hidden-layer inventory. The older n^-2-only exposition is superseded by the accepted sufficient eta_n sqrt(n)→0 statement. [Inherited message extraction](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/ARCTAN_TWO_INHERITED_MESSAGES.txt) records these texts.

Page1 still contains two inherited turn records with zero items (01a05871 and 01a0584a). Their missing content is explicitly a visibility limit; no theorem is inferred from their existence. The separate explanation-task audit is the appropriate source for any parent-session recovery. This audit covers all post-fork work and both surviving alternative continuations, all visible ancestral turn outcomes, and the authoritative inherited complete proof/review, rather than treating a paginated first page as the entire task.

All 15 newly archived primary files match their readable original bytes. No completed primary result above is presently inaccessible. The only absent named latest manuscript is explicitly documented as never completed. No new empirical evidence is claimed.

## Required corrections to the master report

Add AT1/AT2 as pure-arctangent semi-global **joint** rows; retain AT3 as a broad-activation orthogonal-data global row and AT4 as its affine-first-layer arbitrary-geometry exception with its scoped review level. Preserve AT5/AT6 as wider checked variants with their exact checking provenance. Separate the inherited loss/clock and uniqueness/measurement contract from the modern half-loss contract. Qualify statements that no theorem treats arbitrary sample count, arbitrary real labels, or entire bounded activations: AT3 does, for fixed finite **orthogonal** datasets and its L2 architecture. Do not label all L2 two-sample arctangent results unrecovered; AT1 and the orthogonal AT3 are now primary-recovered. Antipodal-opposite-label global claims outside these manuscripts still require their own source recovery. Do not erase the open no-gain convex-mixture problem for three absolutely separated inputs merely because pure arctangent now has a verified local joint result.


## Cross-task supersession update from the coordinator

The coordinator recovered the later **Generalize non-local GF limit** successor package under `/tmp/pde-gf-supervisor-worktree` and is auditing its final accepted arbitrary-fixed-depth, arbitrary-finite-dataset C1,1 semi-global joint theorem separately. That successor, once its precise final assumptions are installed in the master, should absorb AT1/AT2/AT5/AT6 wherever it proves the same existence/limit conclusion under broader assumptions. Retain separately only non-superseded quantitative time, initialization, learning-step, topology or strict-activity refinements and historical review provenance. AT3/AT4 remain distinct **global** theorems. The paused-draft exclusions above describe the endpoint of this task, not the ultimate endpoint of its successor. This audit does not substitute the coordinator's brief report for reading that successor's accepted proof; its exact claim is supplied by the separate supervisor audit.


## Final bounded recovery supplements

Further read-only recovery requested during consolidation is recorded separately in `ODD_MIXTURE_DEPTH_ADDENDUM.md`, `L3_BOUNDED_SAME_LABEL_RECOVERY_AUDIT.md`, `L3_POSITIVE_TIME_CURVATURE_RECOVERY_AUDIT.md`, `L2_SPECIAL_ANGLES_RECOVERY_AUDIT.md`, and `L2_MIXED_FINITE_GF_RECOVERY_AUDIT.md`. The first is a later alternative branch of the current root task; the remaining recovered primary histories belong to a different original task, not the L=2 arctan, two inputs task. Do not reattribute them here. All 174 historical file-change chains in the two older two-sample directories were mechanically recovered; the manifest records exact changes and hashes. Original restricted directories were not opened or modified.

For AT3's finite-GF scope, the broad activation source explicitly proves the population limit of the **finite continuous flow** at the end of its population-identification section (line 373), then gives the same-width lifted-GD versus finite-flow bound (22). Thus its three-way population/finite-GF/raw-GD description is supported by an explicit proof passage, despite the opening theorem paragraph naming only GD convergence. The comparison is not an inferred extra theorem.
