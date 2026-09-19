# Independent internal review R1-B

Reviewer: `cx2_partial_review_b`. Date: 2026-09-19.

**Verdict: the principal local, bounded-reference, and conditional claims are supported, with two minor corrections/clarifications recorded below. The package does not complete C-X2.** I found no major gap in the stated conditional closure theorem or in the new conditional finite-network bridge. The unbounded long-horizon construction and correlated-input extension remain substantive open obligations, exactly where the candidate places them. This is an internal scientific audit, not a promotion, relevance, integration, or executable-solver approval.

## 1. Scope and independence

I started from `REVIEW_R1_ASSIGNMENT_B.txt`, with no inherited author discussion. I read only that assignment, every file listed in the frozen input manifest, and the required `solve-math-rigorously` and `investigate-conjectures` skills. For the latter I also read its research-contract, adversarial-audit, and decisive-experiments references. I did not read the study README, author working files, other studies, another review, project history, or live book material. I did not retrieve external scientific sources. The frozen excerpts contain the required arguments; references to additional original-book sections were not used as substitutes for supplied proofs.

I am not any of the listed authors/assemblers (`root`, `cx2_reference`, `cx2_source`, `cx2_closure`). I consulted no other reviewer and delegated no part of this audit. The only writes were this assigned report and the assigned generated scratch. No Git operation, training experiment, or input edit was performed.

All line references below refer to the files in `data/generated/cx2_activation_class_20260919/review_r1_inputs/`, not their live originals.

## 2. Exact claim audited

The primary model has two hidden layers with one fixed nonaffine activation `phi` in globally `C1,1`, bounded first derivative, Gaussian stored variances `(1,1/n,1/n^2)`, block mobilities `(n,1,n)`, physical time, and unhalved weighted mean-square loss. The main pair has normalized nonparallel unit inputs and labels `(+1,-1)` with weights `(1/2,1/2)`. Actual finite Gaussian readout is retained; only its population limit is zero.

The population raw space is full-row `L2`, learned-middle Hilbert–Schmidt increment, and readout `L2`, with a bounded initialized Gaussian action and its actual adjoint. The initialized action is not claimed Hilbert–Schmidt. The requested observations are whole-circle predictions and separately fixed, correctly typed same-population tuples, including initial/current activation pairs and second moments.

The closure uses two evolving probability laws and a finite matrix at each order. It is finite-type, not a finite scalar state before population cubature. Its dictionary and initialization do not use future target data. The scalar numerical state after cubature has no neural-width dependence or growing history. This distinction is explicit and essential.

The three central conclusions are distinct:

1. A local positive interval for every fixed activation and nonparallel pair, with actual finite GF/every-vanishing-step raw GD identification and dense closure convergence.
2. An orthogonal fitted reference for bounded activations, with loss at most `exp(-4 q0 t)` and `T_phi=log(8)/(4 q0)`.
3. The same fitting inequality on a strong symmetric interval in the unbounded class, and closure/finite-network conclusions on a supplied strong interval with specified tails. Neither the required global interval nor those tails are claimed established for the full class.

I audited these conclusions rather than a stronger, unstated arbitrary-horizon theorem.

## 3. Component verdicts

| Component | Verdict | Reason and boundary |
|---|---|---|
| Local full-class canonical flow | Supported | Frozen C.1–C.2 provide the mesh-uniform local response estimates, one-reference comparison, construction and uniqueness. |
| Full-row and HS strengthening | Supported | The full row is reconstructed by its vector integral; rank-one HS estimates upgrade increment comparisons without changing the initialized-action topology. |
| Local finite GF and raw GD for every `eta_n -> 0` | Supported | Fixed coarse programs, target/reference localization, and the explicit limit order avoid a growing-transcript application of the Gaussian theorem. |
| Nonodd opposite-label symmetry | Supported | Orthogonal input exchange together with readout sign reversal preserves the loss and initialized law. No activation oddness is used. |
| Radial fitting lower bound | Supported | `c_ss=J J* c` makes the readout norm convex in feature time; it gives `||h||^2 >= q0`. |
| Strict positivity of `q0` | Supported | The uncentered first Gram is positive definite; full Gaussian support and nonconstancy exclude zero signed-feature variance. |
| Global bounded orthogonal reference | Supported | B.1 applies directly at `C1,1` with bounded upper activation; the mean-loss time normalization is correct. |
| Unbounded continuation interface | Supported as a sufficient condition | Uniform Euler clock/raw bounds and exponential readout tails imply Cauchy convergence and uniqueness. The assumptions are not proved at `T_phi`. |
| Activation-independent dictionary/density | Supported | Bounded Fourier probes are total on finite-coordinate laws; truncation and bounded actions yield reducing observable spaces. |
| Fixed-order global well-posedness | Supported | Local `L-infinity` characteristic theory, exact gradient energy, and order-dependent pointwise speed bounds close continuation. |
| Dense closure from S+E | Supported | Compact-target error production and an additive single-cutoff comparison give an Osgood modulus. Approximation tails are not assumed. |
| Cubature/time consistency | Supported, with the stated nested limits | The source initializer uses only smooth probes, a positive ridge, and ordered regularization/cubature limits. Literal computability requires the stated activation interface. |
| Longer-interval finite-network bridge under S+E | Supported | Strong-target approximation transfers tail bounds to fixed coarse proxies, which suffice for intervalwise comparison with actual finite algorithms. |
| Local paired activity and visited-law nonaffinity | Supported | The weighted C.3 correction uses `omega_a y_a`, retains fresh Gaussian variance in the upper acceleration, and covers flat gates. |
| Conditional source-row cap and scalar cap test | Supported with minor wording corrections | The induction is causal and closes for short time; it supplies no arbitrary-horizon cap. |
| First-Euler rare-event curvature obstruction | Supported in its stated scope | Unit HS directions give unbounded negative second loss variation; this defeats ambient local Lipschitzness there, not GF existence or all admissible closures. |
| Row-removal driver estimate | Supported as a partial lemma | Deleted-row independence and finite energy give a conditional Gaussian path envelope. Reinsertion remains uncontrolled. |
| Full C-X2 / a general executable solver | Not established and not claimed | Continuation, reached-source control, correlated-neighborhood transfer, and implementation remain open. |

## 4. Scientific audit

### 4.1 Local theorem, topology, and finite readout

`PARTIAL_RESULT.md:76–103` invokes the actual hypotheses of frozen C.1 and C.2. Here `d=m=L=2`, input and label bounds are one, all mobilities are positive, and the first-row and middle-array initialization match the frozen convention. C.1's final perturbation clause (`global_A_B_C.md:1076–1083`) permits the stored readout with normalized RMS tending to zero. It does not replace the finite algorithm's initialized readout by zero.

The local C.2 proof is not just a fixed-program moment assertion. Its response cap selection occurs before the time choice (`global_A_B_C.md:1483–1545`), and its causal construction checks the current fields in the appropriate forward/backward order. Its time sums keep the sample weights and avoid maxima over Gaussian histories. The smoothing passage uses only the uniformly controlled first two derivative bounds; it does not ask the nonsmooth second derivative of a `C1,1` activation to converge pointwise.

The full-row reconstruction uses the vector integral with the actual `u_a`. Projecting it gives the original Gram-coupled bottom equation. A continuous rank-one middle velocity has a strong HS integral, which equals its operator-norm integral under the continuous embedding. Replacing the rank-one operator difference bound by the HS bound also proves the claimed stronger within-width increment comparisons. No cross-width operator or HS distance is asserted.

The circle extension is valid. The displayed prediction Lipschitz constant is bounded on the common raw/action ball. A finite input net, the fixed-query convergence, and this equicontinuity give the circle supremum, uniformly in time. The constants need not yield a useful approximation rate.

### 4.2 Symmetry and radial fitting

For `Q(W,A,c)=(WR,A,-c)`, the exchanged sample outputs are `(-f2,-f1)`, so the two-point loss is invariant even when `phi` is nonodd. The initialized finite-array law is invariant too. Deterministic canonical predictions therefore satisfy `f1=-f2=b`; the argument does not assert finite realized predictions are exactly antisymmetric. The gradient identity `-grad L=2(1-b) grad b` follows in the full raw tangent space at such a state.

In feature time, `c_s=h` and the hidden velocity is `J* c`. The strong chain rule gives

`c_ss=J J* c`, and `b_s=||h||^2+||J* c||^2`.

For forward feature time and `N=||c||`, the displayed expression for `N''` is nonnegative by Cauchy–Schwarz. Since `c(0)=0` and `c_s(0)=h0 != 0`, the right derivative at zero is `sqrt(q0)`. Consequently `N' >= sqrt(q0)` and `||h|| >= N'`; this proves the needed kernel lower bound. This argument does not infer monotonicity of individual features, nor differentiate `phi'`.

The initial covariance is the full uncentered first-feature Gram `v I + mu^2 11^T`, not a centered substitute. `v>0` follows from continuity, Gaussian support, and nonconstancy. The upper Gaussian pair then has full support and gives `q0>0`. The physical scalar equation keeps `1-b` positive on every compact strong interval and yields the factor `4 q0` in the loss exponent. The horizon `log(8)/(4 q0)` is correctly normalized.

B.1 supplies the global bounded-activation reference and the stated sufficient raw-GD condition `eta_n sqrt(n)->0`. The proof correctly refrains from inferring the longer-horizon closure tails merely from bounded activation or B.1. Equal-label and balanced-sign orthogonal extensions use the same legitimate permutation symmetries and signed-mean construction; their stated scope excludes unequal mixed classes and nonorthogonal fitting.

### 4.3 Continuation interface and the source partial

The orthogonal scalar clock removes the lower gate without dividing by it. Bounded Lipschitz `phi'` gives a global scalar flow, including at flat gates. In clock coordinates, only `c phi'(z)` needs localization. Its difference estimate has one cutoff factor and a reference-readout tail. Uniform exponential readout tails thus give a short-interval Cauchy comparison; finitely many intervals cover any separately fixed supplied horizon. This proves the sufficient interface in `REFERENCE_PROOF.md:229–278`. The retained Euler norm premise avoids inferring an Euler bound from the energy identity of an unconstructed solution.

The source skeleton in `SOURCE_PROOF.md:131–184` retains the current reverse row and all earlier forward/reverse response terms. Named derivatives freeze controls and covariance coefficients. At fixed graph, bounded first/second derivatives and finitely many product factors give the stated polynomial derivative envelope; the clock derivative in its varying argument is bounded, while roots are held fixed. This supports the fixed-graph truncation passage.

The response cap test is genuinely conditional. Given the cap on the full source-response row `beta`, lower clock pulses carry `h_s p_b`; their deterministic Gronwall bound leads to the forward response estimate. The moment recursion under that cap is linear in the subGaussian norm. The upper derivative row is then controlled by an exponential of a weighted time sum of `|c_j|`; Jensen uses marginal subGaussian bounds without time independence. Cauchy–Schwarz is applied to `|c| R`, not to an unbounded multiplication operator. These steps yield the displayed `Psi_T(B)`. Its small-time closure is valid, and no large-time closure follows.

The deleted-row calculation also has the right scope. Conditional on the deleted trajectory, the omitted initialized middle row remains Gaussian and independent. The time-derivative energy bound controls the trace of the Gaussian Hilbert covariance, hence a Gaussian envelope for the whole independent-driver path. It does not estimate the reinsertion term. The report explicitly retains that term and the unbounded readout multiplier in its response.

### 4.4 Dictionary, density, and source initialization

The dictionary uses constants, full first roots, rational affine combinations, fixed smooth bounded probes, bounded products, and both initialized action orientations. Its finite words use no target activation derivatives or trained trajectory. Bounded Fourier tests of each finite tuple are total, including at singular laws, so the retained spans are dense in the generated `L2` spaces. An unbounded word is recovered by bounded `R tanh(V/R)` truncations. Bounded actions and actual adjunction then give a reducing pair inside any common enlarged carrier.

The ridge estimate in `CLOSURE_PROOF.md:164–186` proves strong convergence of the positive contractions `Q_l`, even with duplicate features and singular feature Gram matrices. It gives strong convergence of the compressed initialized action and its adjoint on the observable spaces. It does not give operator-norm approximation of `A0`.

The frozen Gaussian foundation provides the fixed-program theorem, adaptive same-array conditioning, singular-source construction, common carrier, adjunction, and HS facts needed here. Its source covariance is the uncentered operand Gram. Distinct orientation source groups can be independent while answer fields remain dependent through their response corrections. The closure initializer preserves this distinction.

At fixed dictionary order, all needed named-source derivatives of the smooth probe program have finite bounds. Source regularization followed by cubature convergence and then removal of regularization is legitimate by finite coefficient induction and continuity of positive-semidefinite covariance square roots. No continuity of empirical pseudoinverses or singular Cholesky factors is used. An approximate regularized initializer need not itself be an exact Gaussian action: it is an inner approximation whose laws and finite matrix converge before the outer theorem is applied.

### 4.5 Fixed-order dynamics, error production, and propagation

At fixed order, the marks `b_l` have deterministic finite envelopes. The dynamics are locally Lipschitz in `(w-g,c,M)` with the field coordinates in `L-infinity`; Gaussian `g` is fixed and integrable. Unbounded `phi` causes no failure here: its linear growth controls the finite contractions, while the upper preactivation is bounded on each such local ball.

The finite-order matrix variable is `M`, so its gradient norm in the energy identity is Frobenius. The learned operator is `U2(M-D)U1*`; its HS norm is at most the matrix Frobenius norm because the `U_l` are contractions. Exact loss dissipation yields the order-independent raw bounds. The separate order-dependent pointwise speed estimates prevent `L-infinity` escape and give global fixed-order existence. The current joint laws retain the static marks with their moving coordinates, so characteristic uniqueness proves restart from the saved state without hidden history.

The target-space invariance argument is not circular. First compare ordinary Euler on the full actual carrier to the supplied target using target tails and no dictionary approximation. That proves convergence and hence invariance in the closed observable block. Only then use compactness of target field images and the compact HS-velocity curve to show omitted-action/filter error tends to zero. Bounded norms alone would not suffice on an entire infinite-dimensional ball.

The gate comparison is additive: localize reference `c` in the upper gate, apply the bounded adjoint, then localize reference `q` in the lower gate. The first error is multiplied only by a bounded lower derivative. Therefore the stability coefficient is `C(1+R)`, not `C R^2`. With the exponentially decaying target tails, optimizing the cutoff gives a modulus proportional to `s log(e/s)`. Its reciprocal diverges at zero and proves convergence and strong uniqueness. Approximate closure and Euler paths need no exponential-tail premise. The weaker Osgood interface is correctly stated; mere finite moments or uniform integrability are not silently substituted for it.

### 4.6 Observation, numerical, and finite-network limits

Strong raw convergence plus bounded actions gives prediction convergence on compact input sets. For each fixed typed observation graph, action differences split into input error, HS increment error, and strong initialized-action error on the compact target node set. Bounded continuous gates use uniform integrability against that compact reference family. Induction preserves same-population joint laws. Common-carrier `L2` coupling proves `W2` convergence and convergence of quadratic contractions, including the actual initial/current pairing. It does not create a cross-layer neuron pairing or justify arbitrary products of two unbounded fields.

The reached-state hierarchy assertion retains both oriented answers jointly. Equality of all finite joint laws identifies bounded cylinder functions isometrically and extends to the observable `L2` spaces and action maps. Transporting the already supplied continuation and applying its one-reference uniqueness proves the stated reached continuation result. This is not existence from an arbitrary formal hierarchy or after a data-law change.

For numerical population approximation, bounded marks and fixed-order bounded `c,q` give the drift stability estimate. The unbounded first feature in the perturbed mark contraction is handled correctly by Cauchy–Schwarz. Atomic replay yields a finite locally Lipschitz ODE. The stopped Euler/Heun comparison gives convergence on each fixed horizon without assuming discrete energy dissipation. The nested order puts arithmetic, time, replay, initialization cubature, source regularization, and finally dictionary refinement in the necessary sequence. There is no proved arbitrary diagonal or resolution selection rate. The computability qualification is necessary and correctly stated.

The additional finite bridge in `PARTIAL_RESULT.md:131–209` is logically stronger than the closure theorem alone and is proved separately. Target-reference comparison makes ordinary population Euler approach S; continuity of all required backward nodes makes its tail defect `z_Delta` vanish. At each fixed coarse mesh, A.1 applies to the entire deterministic-coefficient oracle, with continuous at-most-linear coordinate instructions. Fixed-program quadratic laws and localization then identify recomputed finite proxy velocities and tails. The actual finite path is compared to that proxy within a common raw ball.

The exponential-tail comparison must be used on short intervals with `C tau<a`, and the stated ordered limits are essential. The interval induction is valid: after the earlier interval discrepancy vanishes in the ordered limits, it supplies the next interval's initial error; proxy refinements themselves approach the same target. It does not require a single finite cutoff to erase accumulated errors on an arbitrary long interval. For GD, the first-exit argument uses bounded raw speed and `eta_n->0`; for finite GF, the finite-dimensional energy bound supplies global existence. Gaussian initial readout contributes only its vanishing initial normalized RMS discrepancy and is never overwritten by the physical algorithm.

### 4.7 Activity, nonaffinity, and the rare-event obstruction

The supplied weighted C.3 correction is applicable to nonparallel inputs, positive Gaussian variances and mobilities, nonzero labels, and zero population initial readout. The correct onset coefficients use `p_a=omega_a y_a`. The lower activation onset has a nonzero Gaussian conditional component. The upper onset retains an independent unused Gaussian component after the forward/reverse/forward calculation; multiplying by a gate nonzero on a set of positive Gaussian probability preserves positive squared norm. Thus flat gates do not invalidate the local paired-activation claim. Gaussian full support gives positive initial affine-fit errors; `L2` continuity preserves them initially. None of this asserts activity or nonaffinity at the later fitting endpoint.

For `phi(z)=z+epsilon sin(z)`, the first raw Euler state has unchanged hidden parameters and `c=h(phi(Z1)-phi(Z2))`. The selected rare events have positive measure, `c` of order `hN`, and positive `phi''(Z1)`. The unit HS direction changes only the first sample's upper preactivation. Its first prediction derivative tends to zero while its second prediction derivative tends to positive infinity. Since the first residual is negative, the second loss variation tends to negative infinity. This indeed contradicts any ambient local Lipschitz bound for the raw gradient, and the same matrix-only variation works in clock coordinates. The event probability normalization is accounted for correctly.

The obstruction concerns an actual reached Euler state and arbitrary concentrated unit directions. It does not concern an exact positive-time GF endpoint, does not refute independent-probe estimates, and does not imply failure of existence, tails, fitting, or the broader finite-closure class. The energy/spatial-tail and bounded-activation-truncation counterarguments likewise invalidate only the proposed inferences, not the target theorem.

## 5. Preserved objections and requested corrections

### B-1. Passive projection derivative has one power of the gate bound, not two

**Minor; `SOURCE_PROOF.md:235–244`.** The displayed object at line 238 is the passive preactivation

`z_k(u)=sum_a (u dot u_a) J(X_a,g_a)+w0_perp dot u`.

For a named reverse pulse, its derivative obeys

`|partial z_k(u)| <= M sqrt(m) max_a |partial X_a|`.

After applying the activation, the passive feature obeys

`|partial phi(z_k(u))| <= M^2 sqrt(m) max_a |partial X_a|`.

The text assigns the second bound to “its named clock derivative” immediately after displaying the projection. If this means the displayed preactivation, that is false when `M<1`; this section does not assume `M>=1`. If it means the activation feature needed for `alpha`, it is correct but the referent should be stated. Replace the sentence by both bounds, or explicitly identify the feature derivative. The intended passive `alpha,F` estimate and the primary local theorem survive this correction. I preserve the objection despite the immediate repair.

### B-2. Name the response quantity capped by B explicitly

**Minor; `SOURCE_PROOF.md:188–202, 375–392`.** The first premise says “full backward row” has absolute sum at most `B`, while the scalar test closes `sum_p |beta_i,p|<B`. The actual backward coefficients are `D=beta+learned-memory`, whose bound is `D_*=B+VS^2 T`. The proof works when `B` caps the complete source-response row `beta`, including its current terms. It does not show `sum|D|<B`. State this premise explicitly and retain `D_*` for the actual backward row. The displayed definitions make the intended interpretation recoverable, so this is a clarification rather than a failed estimate.

No other unresolved objection to the principal stated partial/conditional conclusions was found. In particular, I do not classify the openly retained long-horizon assumptions as a hidden gap in a theorem that does not claim to prove them.

## 6. What still blocks C-X2

The missing bridge is a strong canonical construction for every allowed unbounded activation through the activation-dependent fitting horizon, together with sufficient reached-source/tail control. Raw energy gives bounded and Cauchy raw paths on existing intervals, but does not provide local existence or a uniqueness modulus at an arbitrary reached `L2` state. The scalar clock reduces the needed tail premise at the orthogonal reference; it does not prove it.

A positive correlated-input neighborhood through that longer horizon also requires a construction and tail estimate for the actual perturbed programs. Proximity to one reference path does not make those changed-data Euler programs Cauchy. The rare-event result rules out one ambient Lipschitz route, while leaving other response estimates possible. Finally, mathematical consistency and an activation-evaluation interface do not constitute the missing general executable solver. These are substantive remaining tasks; the package appropriately makes no full-completion or practical-complexity claim.

## 7. Validation and exact read coverage

All 13 manifest-listed files were read completely: **5,636 lines**, in addition to the 90-line manifest and the complete neutral assignment. The initial combined read of `CLOSURE_PROOF.md` was output-truncated; I repaired it by rereading lines 335–475. No scientific segment remained unread.

| Frozen file | Complete coverage | SHA256, verified before and after |
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

The validation script and all supplied repository import dependencies were inspected before execution. `finite_network.py` has the advertised input/readout normalization, residual-free backpropagation, physical block scaling, and simultaneous raw update. Importing `pde` also imports `gaussian_moments.py`; that dependency was read in full although these tests do not call it. The runtime dependencies are Python's standard library and NumPy; no live repository module outside the frozen package was imported.

The required check was run with this effective command from the assigned scratch directory:

```text
PYTHONPATH=/home/amir/Codes/PDE/data/generated/cx2_activation_class_20260919/review_r1_inputs/code
PYTHONDONTWRITEBYTECODE=1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
/usr/bin/python -B /home/amir/Codes/PDE/data/generated/cx2_activation_class_20260919/review_r1_inputs/check_identities.py
```

The wrapper also set `TMPDIR` to the assigned scratch, a 120-second CPU limit, and a 120-second wall timeout. Both tests passed, including the four activation subcases in each: nonodd loss/flow/raw-step equivariance and the feature-ascent chain rule with the raw metric. Unittest reported 0.061 seconds; measured child CPU time was 0.163403 seconds and wall time 0.183559 seconds. No training run or further numerical search was performed. The checks corroborate finite identities only; the proof audit supplies the mathematical verdict.

Scratch records: `hashes_before.json`, `hashes_after.json`, `validation_run.json`, and `identity_checks.log` in `data/generated/cx2_activation_class_20260919/review_r1_b/`. Hash checks recomputed SHA256 and line counts directly from every manifest-listed file. All before/after values matched the manifest.

**Completion:** full assigned scientific audit, complete frozen-input read coverage, required deterministic reproduction, and before/after integrity verification are complete. The only requested corrections are B-1 and B-2 above; the larger mathematical obligations remain open.
