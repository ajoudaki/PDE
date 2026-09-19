# Extension R1: independent complete review B

Date: 2026-09-19. Reviewer: isolated reviewer B.

**Verdict: ACCEPT the complete frozen result, with its stated hypotheses and exclusions. No required scientific or implementation correction was identified.** This is an internal review verdict, not promotion approval. It applies to the packet identified below, not subsequent changes or a stronger activation/input/limit scope.

## Scope, independence, and integrity

I followed `EXTENSION_R1_ASSIGNMENT.md`. I read all thirty manifest-listed files completely: 16,155 lines comprising the ten candidate mathematical/assembly/validation documents, two candidate Python files, seven complete mathematical dependency excerpts, the notation document, and ten maintained Python import-closure files. Truncated displays were reread in smaller pieces. I also read the required rigorous-math and conjecture-investigation skills and their applicable contract, evidence, adversarial-audit, and decisive-experiment references. I did not read author history, other studies, earlier verdicts, another reviewer's findings, or live implementations. No scientific source was fetched outside the assigned packet.

Frozen root:

`/home/amir/Codes/PDE/data/generated/cx2_activation_class_20260919/extension_r1_inputs`

Manifest SHA-256, checked before and after review:

`b7ea60fc3c0335530c4d06e39ea96cc7ff1e82f2fbb86f79a53b3344a6753990`

All thirty file hashes and line counts matched before and after the audit. The full verified inventory is at the end of this report. The complete checks are also retained in `hashes_before.json` and `hashes_after.json` in the assigned scratch directory. I changed no frozen input and performed no Git mutation.

## Accepted mathematical scope

The accepted scope is the assembly in `REVISED_RESULT.md`, including its endpoint addition and numerical composition:

1. Every separately fixed nonaffine C1,1 activation with bounded derivative, possibly unbounded activation values, has the stated positive onset interval uniform over Borel laws on the normalized circle with labels in [-1,1]. The state includes the full first row in L2, the learned middle increment in HS, and the readout in L2. Uniqueness is on the prescribed initialized-action carrier.
2. For bounded activations in that C1,1 class, sufficiently small perturbations of the orthogonal opposite-label, half-mass pair have the strong solution and source-tail control through each separately fixed finite horizon. This supplies the stated substantial fitting horizon, early paired activity, and finite-horizon comparison to the reference's whole-circle learned endpoint.
3. Under the additional C2 hypothesis, with bounded continuous second derivative, the supported half-mass binary Borel family is admitted, including its represented nonatomic arcs. A global modulus of the second derivative, a third derivative, monotonicity, oddness, and strictly positive gates are not hypotheses.
4. The dense autonomous hierarchy and its separately ordered numerical refinements converge to those targets. Finite GF and actual simultaneous raw GD, with every vanishing learning-rate sequence, have the stated prediction and fixed-observation limits; the data-law sequences may approach the fixed admitted target without a relative sample/width growth restriction.

This does not accept nonatomic fitting for arbitrary bounded C1,1 activations, substantial fitting for general unbounded activations, exact ReLU, a changed-law infinite-time theorem, arbitrary numerical diagonals, approximation-order rates, or a finite-run accuracy/cost-to-tolerance certificate. Those are explicitly excluded or open in the packet. The older partial documents remain conditional dependencies; the new construction supplies the target and tail premises before invoking them.

## Scientific audit

### Model, topology, and onset

I checked the normalization throughout: u=x/sqrt(2), the same activation in both layers, stored variances (1,1/n,1/n^2), mobilities (n,1,n), and unhalved probability-weighted squared loss. The factor -2 and the weighted rank updates agree with these conventions. The initialized action is bounded and has its actual adjoint; only the learned increment is HS. A normalized finite rank a b^T/n has precisely the population rank's Frobenius/HS contraction, so the full-state bridge does not substitute an operator-norm estimate for the middle metric.

`ONSET_EXTENSION.md` correctly applies the weighted response estimate of activation-foundation C.2 before the law completion. The time is selected from activation/raw-ball constants, independently of atom number, positive atom weights, covariance rank, law refinement, and time mesh. The proof uses weighted source sums and their Gaussian exponential moments, not the maximum of an ever-growing Gaussian transcript. For the unbounded activation case, the readout and backward tails used in the comparison are integrated tails; a uniform pointwise readout bound is not silently imported from the bounded-activation case.

The nonlinear comparison has coefficient C(1+R), with additive readout and backward localization errors. It does not introduce an R^2 propagation coefficient. This matters: the Gaussian tail then dominates the cutoff amplification on the fixed onset interval. Finite-law Euler paths are Cauchy on a common carrier, and joint bounded-multiplier, action, and Bochner-integral continuity passes the full raw integral equation. The continuous velocity yields the claimed strong C1 solution. Positive-part/truncated-exponential passages transfer the required integrated tails without asserting continuity of a sharp tail event.

The smoothing order is valid. Source derivatives are used at fixed smooth finite programs; convergence to C1,1 values uses uniform convergence of phi and phi', the value theorem, and the tail estimates. Neither convergence of phi'' nor a response formula deduced from a singular covariance's value support is required. The final uniqueness argument localizes only the constructed reference, and therefore applies to any bounded strong competing path on the same carrier.

### Bounded C1,1 perturbed pair: the principal new source argument

I audited the preferred raw-Euler proof in `COMMUTATOR_RESPONSE.md` Section 9 together with all of Sections 1–8, especially the artificial module and its identification in Section 4, equations (13)–(22).

The artificial module is an actual finite linear program on the same base arrays. Its coefficients M and c phi''(Z) are bounded at each fixed mollification. Its updates include both terms in the differentiated rank and use A and its actual adjoint. The estimates (14)–(16) bound its propagation and injected response using only L2 operator and HS norms; they do not apply a Gaussian matrix to an Lp norm or impose a response cap to obtain the artificial anchor. The zero initial tangent, the direct injected-root response, and the current diagonal contribution CL have been accounted for.

The base/tangent parity step survives the most important objection. Conditional on the finite base arrays, every tangent field is linear in the independent centered root e, while base fields are independent of e. Hence all required limiting mixed contractions vanish. The supplied uniform linear-operator estimates also give the normalized finite-pairing variance O(1/n), so this conclusion is not obtained by assuming a vanishing mixed empirical contraction without justification. The resulting Gaussian source covariance is block diagonal between base and tangent sectors. In the scalar source program, differentiation in a base slot leaves a tangent expression odd; its expected derivative vanishes. Differentiation of a base expression in a tangent slot is zero. Thus the potentially missing mixed response terms vanish, while the within-tangent response terms remain.

Expanding the learned ranks then gives exactly (17)–(19). In particular K h_tan and K* d_tan vanish in the population odd sector for the stated reason; neither is discarded at finite width. The tangent derivative recursion depends on the base law and deterministic coefficients but not on the tangent covariance or the root-insertion location. Causal induction therefore defines common bar-alpha/bar-beta rows for all probe placements. Formal source names remain present at zero variance. The external root's coefficient solves the same upper pulse recursion, and its independence from the limiting source blocks gives E[e d_tan]=E[partial_e d_tan]=bar-beta. This establishes (21) and the artificial row bound (22), including at singular source covariances.

The true/artificial comparison uses identical base gates and identical c phi''(Z). It therefore contains no uncontrolled difference of second derivatives evaluated on different trajectories. The only lower discrepancy is the commutator plus, for raw Euler, its mesh defect. For the two active fields, the cross bracket is bounded by 2|u1 dot u2|LD and each self bracket vanishes. Section 9's transported-error identity (34) includes the endpoint term caused by insertion after J_j. Weighted moment sums in (36) and the single-node treatment of the direct pulse control this term without a maximum of Q over time. The resulting estimate (37) is C m_p[gamma+(1+S)h_max], where only S=||phi'''|| multiplies a vanishing mesh error.

The upper/lower response comparison is chronological: the new lower feature uses earlier beta rows, then determines F, and then the new upper beta row is computed. Equation (38) has no current unknown row on its right. Choosing B=B_cl+1 first, then a positive S-independent geometric radius, and finally an S-dependent mesh threshold gives a strict first-failure contradiction. Removing the mesh for each fixed mollification before removing smoothing is essential and is respected. The radius and tails, not the mesh threshold or the source coefficients, are uniform under smoothing.

Passive queries in Section 9.1 use the two active driving vector fields with a bounded passive outside factor. No extra commutator with the passive input is needed. This supplies the uniform marginal passive tails used for whole-circle observations and the later value comparison.

The alternative controlled-step construction in Sections 1–8 also exposes its extra fixed-graph derivative-envelope requirement. Its commutator and raw-consistency estimates are consistent with the stated controlled flow. At fixed smooth activation, the polynomial-times-exponential Gaussian derivative envelopes are integrable and support the stated clipping passage. I found no separate defect there. The accepted primary proof uses Section 9 and consequently does not depend on a mesh threshold uniform in that extra construction or in phi'''.

### Bounded C2 supported-law extension

`BOUNDED_EXTENSION.md` supplies a distinct proof for many atoms and Borel supports. Its compact-region/tail split gives a modulus for phi'' evaluated at nearby L2 fields: first select the region and its finite local modulus, then control the exceptional set using moments. Global uniform continuity of phi'' is not inferred from boundedness and continuity. The pulse products are estimated using the indicated finite moments and Hölder exponents; no inverse gate is used.

The reference clock construction and its differentiated consistency defect supply the reference cap before a changed-law cap is assumed. The same-mesh, one-reference raw comparison subsequently makes the changed-law state error small without assuming its unknown source cap. The causal response comparison then closes that cap. Its constants do not depend on minimum atom mass, atom count, or nonsingular Gram matrices. Supported finite approximations retain the two label masses and support caps, allowing the stated Borel completion.

The explicit jumping-second-derivative example correctly explains why the small-bracket route does not automatically handle many nearly parallel directions for arbitrary C1,1 activations. It is used as a limitation of a proof route, not as a counterexample to the neural theorem. The assembly maintains this distinction.

### Fitting, activity, endpoint, and neural identification

The reference symmetry works for nonodd activations: exchange the two input coordinates and negate the readout. Nonaffinity implies v>0 and q0>0 for the stated nondegenerate Gaussian pair. In feature time, c_s=h and c_ss=J J* c imply convexity of ||c|| and ||h||^2>=q0. Transforming back to physical time gives loss <=exp(-4q0 t), with loss <=1/8 at T_phi. This leaves a strict margin for the perturbed loss <1/4.

The early-activity argument uses the weighted direction p_a=omega_a y_a and paired initial/current variables on the same rows. It gives positive order-t^2 activation displacement at the anchors, then transfers a fixed positive-time margin by the proved law/input continuity. Positive initial affine-fit error follows from nonaffinity under a nondegenerate Gaussian; its variance/covariance formula is continuous under the available L2 convergence. No activity at the later fitting endpoint is inferred.

I checked the additional reference-endpoint calculation in `REVISED_RESULT.md`. With lambda=2q0, the integrable residual bounds first c in Linfty, then K in HS, then w in L2. The raw speed is bounded by V exp(-lambda t), so an actual strong endpoint exists. The displayed prediction estimate is uniform in u. At the enlarged fixed horizon the reference endpoint error is <=1/8; the perturbed/reference error <=1/16 gives <=3/16<1/4. The separate fitting margin can be retained by shrinking the fixed neighborhood. This is a finite-horizon comparison to the reference endpoint, not an infinite-time endpoint theorem for the perturbed law.

The finite-program bridge first fixes the proof law, mesh, and cutoff. The fixed-program theorem is never applied to a transcript growing with width. The actual finite Gaussian readout remains in the neural algorithm; its normalized initial discrepancy tends to zero, or it is included additively in the proxy. Localized proxy feedback and the exact finite-rank contraction identity give the required finite comparison. Exponential-tail versions are iterated over a finite time partition, with cutoffs and tolerances selected as in the supplied completion proof. This avoids a false inference that one fixed cutoff over an arbitrarily long horizon suffices.

For simultaneous raw GD, the additional node/interpolant displacement is O(eta_n). Stopping one raw unit outside the bounded proxy path and applying the comparison precludes exit with probability tending to one. This does not assume monotone discrete loss or a maximum-neuron bound. Data transport contributes C(1+R)W1(lambda_n,mu), with all tail burdens on the fixed comparison proxy. Hence the actual data laws need only approach the fixed admitted target; they need not themselves be two-atomic or have a uniform population continuation theorem. Compact empirical-law convergence and a finite union bound give the stated unrestricted joint sample/width limit.

### Dense hierarchy and separate numerical limits

`CLOSURE_PROOF.md` proves density using the fixed smooth bounded-probe language, including both initialized action orientations, rather than the training activation's particular form. The generated spaces are a reducing pair. The ridge filters are positive contractions converging strongly; their action on compact target sets and finite-rank approximations yields the forward, reverse, and HS omitted-source errors. No operator-norm approximation of A0 is asserted.

The finite hierarchy uses unrestricted moving row/readout coordinates and a finite matrix, with the declared weighted row/readout metrics and ordinary coefficient Frobenius metric. The energy identity and fixed-order bounds give autonomous continuation and restart. Lifting its matrix equation gives Q2 F_K Q1 exactly. The one-reference comparison uses tails only from the exact target, so no unavailable uniform higher moments of projected trajectories are required. This remains valid with the onset theorem's law-integrated tails. Same-carrier L2 convergence gives the joint and initial/current W2 observations and quadratic contractions.

The finite numerical assertion has an explicit additional premise: pure, coordinatewise, locally uniformly consistent evaluators of phi and its actual derivative. Regularity is not equated with computability. At fixed order, source covariance regularization is removed only after the complete source-coefficient cubature limit; population replay does not refit those coefficients. Singular covariance passage uses a continuous positive-semidefinite square-root coupling and retained formal derivatives. Positive feature ridge remains fixed during these inner limits.

The accepted order is precisely lim_N lim_epsilon-down-to-0 lim_Q lim_P lim_input lim_h-down-to-0 lim_precision, omitting the input refinement for exact finite data. The rational arithmetic and positive-pivot arguments concern each fixed computation; resource allowances may increase to admit it. The code's Heun map needs only the stated first-order convergence under C1,1 regularity. No second-order or finite-step energy theorem is claimed.

## Implementation and reproduced evidence

I read the full import closure and traced the adapter against the equations. `build_dictionary` retains every bounded valid code through 16N, including literal duplicate outputs, and uses ridge 2^-N. Its initialization always invokes the complete generic compiler. The compiler retains the named source responses in both action directions, freezes earlier covariance/coefficient selections during differentiation, and replays P-node marks after the Q-node coefficients have been fixed. The inverse-Cholesky coordinates are an orthogonal change of the proof's symmetric coordinates and preserve the Frobenius middle metric.

The same supplied activation appears in both moving layers and both initial/current paired fields. Runtime reverse action is the actual transpose of the current finite feature-action matrix. Callback ownership, finiteness/shape checks, and descriptor binding match the stated interface; descriptor equality is expressly a declaration rather than a verification of arbitrary callback semantics. Checkpoints retain the current state, frozen marks/action, data and arithmetic metadata, and require the matching external activation. They do not rerun initialization or retain an evolving source history. The storage/RHS/initializer counts include the correct separate feature, population, and input dimensions; evaluator work and scalar bit size are explicitly extra costs.

I independently ran the single authorized deterministic suite from the frozen packet, after reading its plan. Exact invocation, working directory, environment overrides, return code, and elapsed wall time are in the assigned scratch `execution.json`:

```text
cwd: /home/amir/Codes/PDE/data/generated/cx2_activation_class_20260919/extension_r1_inputs
timeout 120s python -B studies/cx2_activation_class_20260919/test_activation_closure.py

PYTHONPATH=/home/amir/Codes/PDE/data/generated/cx2_activation_class_20260919/extension_r1_inputs/code:/home/amir/Codes/PDE/data/generated/cx2_activation_class_20260919/extension_r1_inputs/studies/cx2_activation_class_20260919
PYTHONDONTWRITEBYTECODE=1
OPENBLAS_NUM_THREADS=1
OMP_NUM_THREADS=1
MKL_NUM_THREADS=1
ACTIVATION_NUMERICS_SCRATCH=/home/amir/Codes/PDE/data/generated/cx2_activation_class_20260919/extension_review_r1_b
```

The entry point additionally imposed 120 CPU seconds and 1 GiB address space. Result: exit 0, **8 tests passed, 0 failures, 0 errors**. Reported test wall time was 1.0896124057471752 seconds; enclosing process wall time was 1.2391925975680351 seconds; reported CPU usage was 1.169756 seconds and peak RSS 39,052 KiB. Environment: Python 3.10.12, NumPy 1.26.4.

All eight checks passed:

- all gradients, energy identity, and actual adjunction;
- callback shape, finiteness, ownership, and activation binding;
- complete nested source responses and frozen named derivatives;
- dense-network normalization at a supplied state;
- cofinal dictionary prefix, duplicates, and resource rejection;
- generic initialization and independence from the training activation;
- paired observations, one Heun map, and exact restart;
- finite precision and law-scope metadata.

Full stdout/stderr is in `suite.log`; `validation_record.json` records the suite and source hashes. Exact restart fixtures are `restart_None.json` and `restart_24.json`. No training, sweep, discarded run, retry, or diagnostic campaign was performed. These tests substantiate finite algebra and execution, not the mathematical long-time existence or hierarchy convergence proofs.

## Corrections and decision

**Required corrections: none.** I found no missing scientific dependency needed for the assembled result, no surviving mixed source-response term in the artificial anchor, no circular cap selection, and no implementation discrepancy invalidating the stated numerical theorem.

The preferred proof, its C2 supported-law companion, the neural bridge, and the numerical composition cover the complete claimed scope, not merely a narrower onset or orthogonal-reference result. The open/excluded cases listed above remain outside this acceptance. Any changed packet requires the assignment's fresh complete review process; this verdict does not itself authorize promotion.

## Verified frozen input hashes

Each row below matched both before and after review. Paths are relative to the frozen root, not live repository paths.

| Frozen path | Lines | SHA-256 |
|---|---:|---|
| `code/pde/__init__.py` | 26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/finite_network.py` | 363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | 114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/observable_arithmetic.py` | 230 | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `code/pde/observable_compiler.py` | 528 | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| `code/pde/observable_fixed.py` | 223 | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `code/pde/observable_initialization.py` | 397 | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `code/pde/observable_laws.py` | 472 | `6fb38416ce02ca77aae0392201927eb9aeba5c672ebe774181822dfb805d0503` |
| `code/pde/observable_solver.py` | 350 | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `code/pde/observable_words.py` | 217 | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `dependencies/activation_foundation.md` | 1996 | `58e7dc1d8cf7abd991fcba7e305d084bfb522795cc5b9aee443c183fe4fa1c03` |
| `dependencies/gaussian_foundation.md` | 542 | `8a8dbe6a31a51d3f73c999b75c75dcade76b3d533c8901a062c66587776cdd0a` |
| `dependencies/law_construction.md` | 1288 | `87e17770daea404d80da2c8a3e45cb5925f8110527660f2d7e70b08d3a92e0a1` |
| `dependencies/numerical_proof.md` | 815 | `ac29b96116d1e6069b0eee190e07359b8fe156567e8fc21abbf7d2dfdc1d4e83` |
| `dependencies/onset_law_proof.md` | 567 | `d205fbd13d1fe8dd97876d0a7ffa4f502380216a15a29bd4e2d016a2622c90b1` |
| `dependencies/source_and_completion.md` | 1384 | `10851308aa9a132214f828df24a99225b15f5d1798e187fbddc207fae08ff411` |
| `dependencies/supported_law_proof.md` | 1283 | `1046d356e89e34c829354eb633e246594ed65910b03c9ec43f88a7dc1bdc2e8e` |
| `docs/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `studies/cx2_activation_class_20260919/BOUNDED_EXTENSION.md` | 690 | `4cf3bce600d5518defd67225329d0f52720babd15e3d86984aab47a5187e09a2` |
| `studies/cx2_activation_class_20260919/CLOSURE_PROOF.md` | 741 | `15270cb49004fe359c49722508ad0c96695d8ddb2f939a66b84939a3be0f0d6c` |
| `studies/cx2_activation_class_20260919/COMMUTATOR_RESPONSE.md` | 887 | `632a158323c53dfaa50034a08855c9b51cc19c29af889e3176d160a101005625` |
| `studies/cx2_activation_class_20260919/NUMERICAL_EXTENSION.md` | 276 | `dd3dfeeedbec2381d1d33a8fc80a8e5086e7d3cd08243b399754a64f03c23dd3` |
| `studies/cx2_activation_class_20260919/NUMERICAL_VALIDATION_PLAN.md` | 68 | `edb4e15ff0b079ac356556460cd44765a440fcacd7a24a9810c36ba4436954fb` |
| `studies/cx2_activation_class_20260919/ONSET_EXTENSION.md` | 394 | `d5853c29a24e3075053ce0629e5aed63ea7f259107118f36d97f5805684b4593` |
| `studies/cx2_activation_class_20260919/PARTIAL_RESULT.md` | 230 | `a47d85ca451bfe1d70e44fad4cb695d5011445a19b0ab9f182e8b5bf4293cd1b` |
| `studies/cx2_activation_class_20260919/REFERENCE_PROOF.md` | 430 | `535d4576ac2de2711bcacbed64d5864d2207a54eb1b7bc84bc668e8402395be7` |
| `studies/cx2_activation_class_20260919/REVISED_RESULT.md` | 252 | `c7fbacd698236a800e737d0732d6a183f8cd96314a510df72d4e9aa218c5128d` |
| `studies/cx2_activation_class_20260919/SOURCE_PROOF.md` | 651 | `4b944a9c4bfe290a4b294a3586d1c67607ac776926482beeb8fa832c2613ceff` |
| `studies/cx2_activation_class_20260919/activation_closure.py` | 395 | `49b385deb1d1d700a168f5d17025037bf647a9f6e03b0f6dd85ede10284ccec3` |
| `studies/cx2_activation_class_20260919/test_activation_closure.py` | 248 | `6cc53274173f8bd376a5da904070eb5066843980bb04a84de0bc131f2f16deb3` |
