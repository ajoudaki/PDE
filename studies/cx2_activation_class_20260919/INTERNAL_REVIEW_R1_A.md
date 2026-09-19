# Independent internal scientific review R1-A

Reviewer: `cx2_partial_review_a`. Date: 2026-09-19.

**Verdict: the stated local full-class result, bounded orthogonal fitted reference, and conditional closure/continuation/finite-network results are supported, subject to two minor corrections recorded below.** I found no major defect in those claims after reading the complete frozen package. This is not a finding that C-X2 is complete, nor a promotion or integration verdict. The supplied arguments do not establish the general unbounded-activation continuation or a correlated-input fitting neighborhood at the prescribed fitting horizon.

## Scope and independence

I followed `REVIEW_R1_ASSIGNMENT_A.txt`. I am not any of the listed authors (`root`, `cx2_reference`, `cx2_source`, `cx2_closure`). I started from the neutral assignment and the frozen inputs, without author discussion, another review, live book retrieval, study history, other studies, or Git history. I did not edit an input or perform any Git operation. My only writes are this report and the assigned `review_r1_a/` scratch files.

Required skills read completely: `solve-math-rigorously/SKILL.md`, `investigate-conjectures/SKILL.md`, and the latter's `research-contract.md` and `adversarial-audit.md`. No external theorem was accepted merely because the author called it established: I inspected the supplied complete dependency proofs. Provenance references to sections outside the frozen excerpts were not followed. The adapted closure proof is self-contained on the supplied A.1–A.4 and III.F ingredients; those provenance references do not create a missing necessary input for the claims assessed here.

The reviewed model uses two hidden layers, the same fixed nonaffine C1,1 activation with bounded derivative, actual Gaussian middle action and adjoint, full first rows, HS learned increments, stored variances `(1,1/n,1/n²)`, mobilities `(n,1,n)`, and unhalved mean loss. The main local datum is the fixed nonparallel unit pair with labels `(1,-1)` and equal weights. The fitted reference uses the orthogonal pair. In particular, fixed-order systems containing two current probability laws are finite-type population systems, not finite scalar systems before cubature.

## Component verdicts

| Component | Verdict and exact scope |
|---|---|
| Fixed-order closure equations and global existence | Supported for each fixed dictionary order, including unbounded target activation. Global existence here does not imply existence of the unfiltered population target. |
| Universal dictionary, density, action initialization | Supported. The dictionary retains joint laws and both orientations, is independent of activation/data values/future paths, and handles singular source covariances without a rank-stability assumption. |
| Conditional dense closure | Supported from S and E on the specified fixed interval, in full-row L2 + increment HS + readout L2, with the declared observations. |
| Numerical consistency | Supported as the displayed nested, exact-real limits. Literal finite-precision execution additionally needs the stated activation-evaluation interface. No solver implementation or useful cost bound is proved. |
| Local full-class population and actual finite limit | Supported by the supplied C.1/C.2 proofs and the explicit full-row/HS upgrade. The actual finite Gaussian readout is retained. The vanishing-step assertion concerns the prescribed simultaneous raw GD. |
| Nonodd opposite-label symmetry | Supported for the deterministic canonical limit, using initialization-law invariance and equivariance. It does not require finite realized predictions to be exactly opposite. |
| Radial fitting mechanism | Supported on a strong symmetric reference interval; the coefficient is the actual positive initialization quantity q0. |
| Bounded orthogonal fitted reference | Supported globally, using B.1. Mean-loss time normalization and first-input scaling are handled correctly. |
| Full-class fitting at T_phi | Conditional, not proved: the strong interval through T_phi is missing for the general unbounded activation. |
| Longer-horizon finite bridge | Supported conditional on S/E for the actual canonical action, with width first at fixed proof mesh/cutoff, then mesh removal and cutoff removal on short subintervals. |
| Local paired activity and visited-law nonaffinity | Supported. The weighted correction uses omega_a y_a. No assertion of activity specifically at a later fitting endpoint follows. |
| Conditional source-response cap | Supported with the interpretation of B specified in objection A1. It supplies a local criterion, not a global cap. |
| Rare-event Hessian obstruction | Supported at the actual first raw Euler state. Its force is failure of ambient local Lipschitzness, not failure of exact GF, independent-probe estimates, fitting, or closure. |
| Deleted-row Gaussian driver lemma | Supported for each fixed deleted row, conditionally on its independent trajectory and the stated initialization event. Reinsertion remains unbounded by this argument. |

## Main proof audit

### 1. Fixed-order system and its energy

In `CLOSURE_PROOF.md:240–318`, the use of `(w-g,c,M)` in L-infinity + L-infinity + finite matrices is legitimate: g is fixed and integrable, the marks are bounded at each fixed order, and every upper preactivation is pointwise bounded on such a local ball. C1,1, rather than a classical second derivative, suffices for local Lipschitzness there.

The row and readout gradients and the matrix derivative `d_a a_a^T` are the gradients of the same unhalved weighted loss in the claimed metric. This yields (10). The contraction bounds for U1 and U2 imply the order-independent L2/HS/operator estimates (11). Pointwise bounds (12), allowed to depend on dictionary order, then bound `w-g` and c in the actual local-existence spaces and prevent finite-time breakdown. It would be incorrect to deduce this continuation only from an L2 ball; the proof does not do so.

The middle state must be distinguished carefully: M is a finite matrix carrying the computational state; K_N is its U2/U1 lift; the initialized B_N is only strongly approximating A0. The identity for K_N' includes Q2 and Q1, exactly as needed. There is no claim that A0 is HS or that B_N converges to A0 in operator norm. At finite width the normalized Hilbert–Schmidt norm equals ordinary Frobenius norm, consistent with the raw metric and with the `1/n` in a rank-one update.

### 2. Density, source laws, and initialization

I checked `CLOSURE_PROOF.md:82–186` against the complete III.F construction. Fourier tests of rational affine combinations of finite tuples are total: continuity extends the vanishing Fourier transform to real frequencies, and Gaussian convolution followed by an approximate identity annihilates the finite signed measure. Thus no moment-determinacy assumption is hidden in the density argument. Smooth bounded truncations recover the unbounded generated coordinates.

Actions on bounded words and their actual adjoints preserve the completed observable spaces. The two invariances make the pair reducing in any larger common carrier, which is enough for the later invariance argument. Positive ridge normalization remains defined for duplicate or dependent words. The explicit estimate (6), together with density and contraction, proves strong convergence of Q_l to identity; it does not require nested orthonormal bases or a smallest Gram eigenvalue.

Source covariances are uncentered operand Grams. The oriented Gaussian source groups may be independent while the action answers are dependent through their response terms. The frozen named-source convention in (4) matches III.F.9–10. Singular covariance is handled by PSD extension and square-root continuity, not by continuity of a pseudoinverse. The dictionary's smooth probe functions avoid demanding nonexistent higher derivatives of the target C1,1 activation.

The initializer computes the full joint mark laws and D jointly with all required actions. Replacing these by separate marginals, or replacing the reverse action by a fresh Gaussian map, would invalidate the proof; neither replacement appears in the construction.

### 3. Closure error production and propagation

S alone is not treated as dense-closure convergence. The proof first obtains observable-space invariance through Euler comparison using S as the reference. The raw field is bounded on the stopped ball, and the comparison never assumes that it is locally Lipschitz on an arbitrary ambient L2 ball.

The compact target sets in (13) supply the missing error-production estimate. Strong convergence of the two initialized action orientations is uniform on those compact L2 sets. For the learned derivative, finite-rank approximation of a fixed HS operator and a finite net of the compact velocity curve justify the HS filter limit. A uniform raw norm bound by itself would not suffice.

The localization estimates (15)–(18) are correct. At the upper gate only reference c is cut off; the resulting backward error is passed through the bounded adjoint and bounded lower gate. The separate lower-gate term cuts off reference q. These terms add, producing C(1+R), not a product of two cutoff factors. Exponential reference tails therefore give an Osgood modulus `s log(e/s)` and (19). No tail is needed for the closure states or a competing strong solution. The uniqueness and Euler-to-S consequences use the same one-reference argument without circularity.

### 4. Observations, whole-circle prediction, and limits

The strong-multiplier lemma handles continuous bounded gates multiplying an L2 field. Uniformity along a compact target path follows by truncating a compact family of reference fields, whose squared tails are uniformly small. Induction through each separately fixed typed graph then handles both action directions. Common-carrier coupling gives W2 convergence of same-population joint tuples and Cauchy–Schwarz gives their quadratic contractions. This includes initial/current pairs; independently coupling the two marginals would not prove paired displacement. No cross-population neuron pairing or growing observation graph is claimed.

The prediction estimate in `PARTIAL_RESULT.md:110–120` is correct:

`|f(u)-f(v)| <= ||c||_2 D1² ||A||_op ||w||_2 |u-v|`.

The raw bounds make this common to finite networks and the target on high-probability bounded events. A finite circle net upgrades fixed-input prediction convergence. Full rows are essential for this assertion and are retained.

At fixed order, bounded mark envelopes, the positive feature ridge, and W2 coupling give the quadrature stability estimate (26), including when the first hidden feature is unbounded. The only affected contraction is treated by Cauchy–Schwarz in (25). For fixed source regularization the finite smooth initializer has consistent cubature; removing regularization is a finite covariance/response continuity argument. Explicit Euler or Heun consistency only requires local Lipschitzness on the finite atomic state, with a first-exit argument around its exact path.

The displayed order `N, epsilon, Q, P, h, p` with the rightmost limit first is justified. It is not an arbitrary diagonal or effective order-selection rule. The computability qualification is necessary and correctly stated: C1,1 alone does not make an arbitrary activation evaluable.

### 5. Local source theorem and finite-network bridge

I read C.1 and the complete C.2 cap construction, including its current-time ordering. The forward response pulse carries its time/sample weight. Moment estimates use Jensen on weighted time sums of marginal subGaussian fields, rather than a maximum of a Gaussian history. Forward response caps are selected bottom-up, backward caps top-down, and only then is a positive time selected. At each current step, the required fields and higher response rows have already been constructed. This closes the local tail proof without assuming future tails.

The C1,1 passage uses uniform bounds on the mollified first derivative and second derivative and the one-reference comparison. It does not pass classical second derivatives pointwise. Fatou transfers local tails to the constructed target. For two hidden layers these tails cover precisely c and q in E.

The upgrade in `PARTIAL_RESULT.md:87–103` is valid: the full-row integral has the specified initial Gaussian row and reproduces every training projection. Rank-one factor continuity supplies an HS integral agreeing with the already constructed operator-norm integral. The same comparison estimates apply with Frobenius/HS increment differences and the full-row velocity bound.

For the longer conditional bridge, population Euler converges to S using E. Its needed node and velocity errors then vanish uniformly by continuity on the compact target path. At fixed proof mesh A.1 applies to all value instructions, including `c phi'(z)`, which is continuous with at most linear growth in the finite input tuple. Fixed-program quadratic convergence and localization identify the finite proxy velocities. The tail-transfer inequality at lines 174–179 is valid. Actual raw GD is compared to that proxy on a stopped ball; no false discrete energy identity is used.

The short-subinterval cutoff argument at lines 185–196 is sound. When proceeding to the next interval, first use the previously proved zero limiting start error at each fixed new cutoff; earlier cutoff parameters can be removed independently. One should not instead use a single growing cutoff in a global factor `exp(CRT)`, which need not vanish against the assumed exponential tails. Actual finite initial readout is never reset: its normalized L2 norm tends to zero and contributes an initial comparison error.

### 6. Symmetry, radial fitting, and activity

The transformation `(W,A,c) -> (WR,A,-c)` exchanges inputs and negates predictions, while preserving loss, metric, and the complete initialization law. Equivariance and deterministic canonical limits therefore yield `f1=-f2=b` without requiring phi to be odd. This is a law-level symmetry; the proof correctly avoids claiming it for an individual finite initialization.

On the symmetric flow the full raw gradient is `2(1-b) grad b`. In feature time, `c_s=h` and the hidden derivative is `J* c`, so

`b_s = ||h||² + ||J* c||²`,

`N'' = (||h||² + ||J* c||²)/N - <c,h>²/N³ >= 0`, where `N=||c||`.

The initialization expansion and nonreturn of N to zero justify division by N for positive feature time. Consequently `N' >= sqrt(q0)` and `||h||² >= q0`. This proves the claimed fitting mechanism without assuming monotonicity of individual features or a trained-kernel lower bound.

The initialization Gram `vI+mu²11^T` is strictly positive definite because v>0 for a continuous nonconstant activation on a nondegenerate Gaussian. Thus the upper pair has full support and `q0=(1/4)E(phi(Y1)-phi(Y2))²>0`. On a compact strong interval the scalar equation gives `1-b=exp(-2 integral K)>0`; feature time is valid there, and the loss rate is exactly `exp(-4q0 t)` for the stated mean loss.

B.1 applies to bounded phi directly at C1,1 and supplies global orthogonal continuation. For arbitrary perpendicular scale g, the first activation in standardized coordinates is `v -> phi(sqrt(g)v)`, whose derivative contributes the necessary sqrt(g) mobility factor. This does not change the raw dynamics. B.1's sum-to-mean time factor and its sufficient `eta_n sqrt(n)->0` bridge are stated accurately.

The weighted C.3 correction proves the local activity assertion. Replacing y by omega*y is necessary in both first nonzero readout and hidden terms. Lower-layer conditional covariance remains positive; the upper forward/reverse/forward calculation retains an independent positive-variance Gaussian component. Multiplying by the upper derivative preserves positive squared norm because that derivative is nonzero with positive initial Gaussian probability. This addresses flat gates as well as nonmonotone activations. Initial Gaussian support and continuity of the regression moments give the positive best-affine-fit error on a short interval. None of these facts gives that error specifically at T_phi.

### 7. Source-control partial and obstruction

The orthogonal clock transformation divides by no gate and remains valid when gates vanish. Under the specified RMS and response caps, the lower pulse estimate is deterministic; the upper response bound keeps the random factor c phi'' rather than replacing it by an RMS constant. Jensen gives the displayed exponential-integrating-factor estimate. The scalar test `Psi_T(B)<B` improves the cap chronologically and holds for some positive short time. Its large-T growth does not establish a finite global cap.

For the rare-event example, the first Euler state has unchanged hidden parameters and `c=h(phi(Z1)-phi(Z2))`. Oddness is used only for this chosen example. The two initial upper coordinates are independent. Events with Z1 near `2 pi N+3 pi/2` and bounded Z2 give positive c and positive phi'' of order hN and one, respectively. The proposed HS direction has norm one and annihilates the second input. Its first prediction derivative tends to zero, while its second prediction derivative diverges positively. Since r1<0, the loss second directional derivative tends to minus infinity. Each individual directional differentiation is justified; together they contradict any common local gradient Lipschitz constant. The same K-only perturbation works in clock coordinates.

The counterexample to extracting spatial exponential moments from Hilbert energy is also valid and explicitly not a neural trajectory. Bounded-activation truncations need reached value and weighted-gate tails, which initial Gaussian truncation error does not supply. The deleted-row calculation in `REFERENCE_PROOF.md:340–424` correctly supplies a Gaussian Hilbert driver, conditional trace bound, and full-path envelope. It leaves the row-reinsertion correction uncontrolled and does not claim otherwise.

## Surviving objections and limitations

**A1 — Minor: specify which row is capped.** `SOURCE_PROOF.md:188–203` says a “full backward row” is capped by B, while the cap test at lines 371–391 proves a bound for the source response row beta; D also includes the learned Gram term. The calculations are valid with `sum_q |beta_iq| <= B`, giving `sum_q |D_iq| <= B+VS²T`. State that meaning explicitly at the premise of Section 3. I do not silently treat the displayed beta cap as a proof that the complete D row is bounded by B itself. This is a notation/statement ambiguity, not a failure of the conditional source estimates after the specified correction.

**A2 — Minor: distinguish the passive projection derivative from its activation derivative.** `SOURCE_PROOF.md:235–244` displays z_k(u), then says “its” derivative is bounded by M² sqrt(m) times the clock pulse. For z_k(u) the bound is M sqrt(m); the extra M belongs to the activated feature phi(z_k(u)). Since M is defined as the derivative norm and is not required to be at least one, the written projection bound is not generally valid. The intended passive alpha/F estimate follows after explicitly applying phi and then using M². No main local, fitting, or closure conclusion relies on the inaccurate projection wording.

**Open major obligations for the larger target, already acknowledged by the candidate:**

1. Construct the canonical strong flow through T_phi for every admissible unbounded phi. Existing energy and endpoint completeness do not furnish local existence at an arbitrary reached L2 state.
2. Prove sufficient reached tails for the actual construction. The orthogonal readout-only Euler interface is a sufficient reduction, but its uniform readout exponential moment and Euler norm premise are not established globally. The closure uses the separate S/E interface with c and q tails.
3. Extend the necessary source/continuation control to an actual positive neighborhood of correlated input pairs through the fitting horizon. Closeness to one reference path does not prove changed-data Euler paths are Cauchy.
4. Deliver and validate a general-activation executable solver under a stated evaluation interface. The finite identity checks and exact-real consistency proof are not that implementation.

These obligations do not invalidate the claimed partial theorem because they are not asserted as conclusions. The review finds neither an impossibility theorem for C-X2 nor a proof of its missing requirements.

## Validation, full read coverage, and integrity

I inspected all validation source and all local imports: `check_identities.py`, `finite_network.py`, `pde/__init__.py`, and its imported `gaussian_moments.py`, plus the complete frozen API guide. External runtime dependencies are Python's standard library and NumPy. No dependency on the live checkout's `code/` was used in the run.

Reproduction command, run from the assigned scratch directory with one BLAS thread and bytecode disabled:

```text
PYTHONPATH=/home/amir/Codes/PDE/data/generated/cx2_activation_class_20260919/review_r1_inputs/code
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
/usr/bin/python -B /home/amir/Codes/PDE/data/generated/cx2_activation_class_20260919/review_r1_inputs/check_identities.py
```

Both tests passed: nonodd loss/flow/raw-step symmetry and feature-ascent chain rule/raw metric. They exercise four activations, including an unbounded oscillating example and a C1,1 activation with a flat region. Exit code 0; test-run CPU 0.147814 seconds; wall time 0.164965 seconds. A 120-second CPU hard limit and wall timeout were imposed. No training experiment was run. These finite supplied-state checks verify identities only; they supply no empirical evidence for width, order, or long-time convergence. Raw output and execution metadata are saved as `review_r1_a/check_identities.log` and `review_r1_a/check_result.json`.

I read every line of all 13 manifest inputs, totaling 5,636 lines. Reads were numbered and chunked. The initial combined display truncated part of `REFERENCE_PROOF.md`; I repaired it by reading lines 1–160 separately. No scientific section remains unread. Exact per-file coverage and integrity values follow below. Every manifest SHA256 and stated line count was checked before and after the audit, with identical results. The manifest itself remained unchanged, SHA256 `a2a240f25fcaf63faf7c25a90f4425399649bdc18f8006ce081a4c1ac4ae8f46`. Machine-readable records are `review_r1_a/hashes_before.json` and `review_r1_a/hashes_after.json`.

| Frozen file | Complete lines read | SHA256 verified before and after |
|---|---:|---|
| `PARTIAL_RESULT.md` | 1–230 | `a47d85ca451bfe1d70e44fad4cb695d5011445a19b0ab9f182e8b5bf4293cd1b` |
| `REFERENCE_PROOF.md` | 1–430 | `535d4576ac2de2711bcacbed64d5864d2207a54eb1b7bc84bc668e8402395be7` |
| `CLOSURE_PROOF.md` | 1–741 | `15270cb49004fe359c49722508ad0c96695d8ddb2f939a66b84939a3be0f0d6c` |
| `SOURCE_PROOF.md` | 1–644 | `1d057268b0910d9e2ddc9dbe0d2587c5829ef57d3b08d78127f4a504e18aa362` |
| `check_identities.py` | 1–90 | `22e441ce52e0e3efab6aa91708c5ff5a0460fa876660c0e812c450eca0982f44` |
| `NOTATION.md` | 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `global_A_B_C.md` | 1–1996 | `58e7dc1d8cf7abd991fcba7e305d084bfb522795cc5b9aee443c183fe4fa1c03` |
| `gaussian_foundation.md` | 1–542 | `8a8dbe6a31a51d3f73c999b75c75dcade76b3d533c8901a062c66587776cdd0a` |
| `finite_energy.md` | 1–227 | `bd10bbff9d16f60c63d26b06e793510fa19958e1ec91dbdd85709caff7d96980` |
| `finite_code_guide.md` | 1–135 | `3737d8f30a80aa3b14cfcb67cdffed160c5a98507ee95a151adac385e33ed9d2` |
| `code/pde/finite_network.py` | 1–363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/__init__.py` | 1–26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/gaussian_moments.py` | 1–114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |

**Completion:** independent scientific audit and assigned deterministic reproduction complete. All objections are preserved above; inputs were not repaired. This report supports only the exact partial and conditional claims identified here.
