# Independent internal scientific audit B — complete frozen R2 package

**Verdict: PASS for the stated partial and conditional results. Full C-X2 remains open.**

I found no unresolved correctness objection that invalidates the local full-class theorem, the bounded orthogonal fitted reference, or the conditional closure and finite-network theorems as actually stated. This is an internal scientific verdict, not a promotion or integration recommendation. The deterministic checks are supportive identity checks only; they do not establish convergence, fitting, or useful numerical accuracy.

## Independence, scope, and read coverage

I began with `REVIEW_R2_ASSIGNMENT_B.txt` and reviewed the frozen inputs from scratch. I am `cx2_partial_review_r2_b`, not one of the four authors named in the manifest. I did not read the study README, live scientific files, study history, prior reviews, another reviewer's findings, other studies, or Git history. I did not consult another reviewer, modify an input, use Git, browse for scientific inputs, or run training experiments. I wrote only this report and files under the assigned `data/generated/cx2_activation_class_20260919/review_r2_b/` scratch directory.

I read the complete required `solve-math-rigorously` and `investigate-conjectures` skills and the latter's research-contract, adversarial-audit, and decisive-experiments references. The frozen mathematical arguments were assessed directly, not accepted because of their author status labels.

Every line of the following thirteen manifest files was read: **5,643 lines total**, including prose, assumptions, formulas, corrections, proof details, validation code, and all supplied local import dependencies. One combined output truncated part of `SOURCE_PROOF.md`; I repaired it by reading lines 1–330 separately. The following ranges describe complete read coverage, not sampled coverage:

| Frozen input | Complete coverage |
|---|---:|
| `PARTIAL_RESULT.md` | 1–230 |
| `REFERENCE_PROOF.md` | 1–430 |
| `CLOSURE_PROOF.md` | 1–741 |
| `SOURCE_PROOF.md` | 1–651 |
| `NOTATION.md` | 1–98 |
| `global_A_B_C.md` | 1–1996 |
| `gaussian_foundation.md` | 1–542 |
| `finite_energy.md` | 1–227 |
| `finite_code_guide.md` | 1–135 |
| `check_identities.py` | 1–90 |
| `code/pde/finite_network.py` | 1–363 |
| `code/pde/__init__.py` | 1–26 |
| `code/pde/gaussian_moments.py` | 1–114 |

I also read all 90 lines of the manifest and the complete neutral assignment. The frozen source records contain references to other book sections, notably C.4 and III.M/S/V. Those sections were not supplied and were not fetched. No central result certified here requires their omitted definitions: the adapted closure estimates are rederived in the candidate, and the Gaussian/action, local-response, bounded-reference, and activity results used here are supplied in full. Incidental statements about particular cap systems or rescalings defined only in those absent sections are not separate certifications of those systems.

## Hash verification

At the initial inventory I computed the SHA256 of every frozen file and compared every listed digest with the manifest. All thirteen matched. Immediately before execution, explicit assertions checked every digest and manifest line count. The final verification repeats those assertions and checks the manifest itself against its initial digest. The before/after records are `review_r2_b/hashes_before_checks.json` and `review_r2_b/hashes_after_review.json`.

| File | Verified SHA256 |
|---|---|
| `PARTIAL_RESULT.md` | `a47d85ca451bfe1d70e44fad4cb695d5011445a19b0ab9f182e8b5bf4293cd1b` |
| `REFERENCE_PROOF.md` | `535d4576ac2de2711bcacbed64d5864d2207a54eb1b7bc84bc668e8402395be7` |
| `CLOSURE_PROOF.md` | `15270cb49004fe359c49722508ad0c96695d8ddb2f939a66b84939a3be0f0d6c` |
| `SOURCE_PROOF.md` | `4b944a9c4bfe290a4b294a3586d1c67607ac776926482beeb8fa832c2613ceff` |
| `check_identities.py` | `22e441ce52e0e3efab6aa91708c5ff5a0460fa876660c0e812c450eca0982f44` |
| `NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `global_A_B_C.md` | `58e7dc1d8cf7abd991fcba7e305d084bfb522795cc5b9aee443c183fe4fa1c03` |
| `gaussian_foundation.md` | `8a8dbe6a31a51d3f73c999b75c75dcade76b3d533c8901a062c66587776cdd0a` |
| `finite_energy.md` | `bd10bbff9d16f60c63d26b06e793510fa19958e1ec91dbdd85709caff7d96980` |
| `finite_code_guide.md` | `3737d8f30a80aa3b14cfcb67cdffed160c5a98507ee95a151adac385e33ed9d2` |
| `code/pde/finite_network.py` | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/__init__.py` | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/gaussian_moments.py` | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |

The manifest's initial and final SHA256 is `e157377112c43577948b3a90c8966ff929ebc5c8154d29fc98416898a5e7bf37`.

## Mathematical assessment by component

### Model, metric, regularity, and local identification — PASS

The frozen notation, finite dynamics, code, and candidate agree on physical inputs `sqrt(2) u_a`, stored variances `(1,1/n,1/n²)`, readout normalization `c^T h/n`, mobilities `(n,1,n)`, and unhalved weighted mean-square loss. A finite rank action is `uv^T/n`; its Hilbert–Schmidt norm in normalized population coordinates is the ordinary finite Frobenius norm. Only the learned middle increment is HS. No initialized HS bound or cross-width operator distance is used.

The finite flow has a locally Lipschitz vector field for C1,1 activations: finite products of locally Lipschitz functions suffice, without a classical second derivative. Differentiating the C1 loss gives the energy identity. Its finite-endpoint length estimate gives global finite GF, but cannot by itself give population existence. The package respects this distinction.

I inspected all of C.1 and C.2, including the chronology of the response caps. The forward-response caps are chosen bottom-up, backward caps top-down, and time only afterward. Their coefficients retain each source pulse's mesh/sample weight. Gaussian moment control uses weighted time sums and Jensen, not a maximum over time or samples. Current response rows use already constructed fields; the local argument is not a bootstrap on unknown future tails. The C1,1 smoothing passage uses only uniform first-derivative and derivative-Lipschitz bounds.

For the requested two-layer model, C.1 supplies the short-time flow and finite every-vanishing-step limit. `PARTIAL_RESULT.md` 87–109 legitimately upgrades the projected/operational construction: integrating the full row velocity recovers each projected equation, preserves untrained perpendicular components, and the rank-one inequality supplies an HS integral and the same HS comparison. This yields S in the specified stronger topology. C.2 and Fatou supply E for both c and the actual reverse field q on a common positive interval. No large-horizon restart is inferred.

The finite initialized readout is not silently set to zero. Its normalized L2 norm vanishes, and C.1's explicit perturbation result covers it. The proxy can have zero limiting readout while actual GF/GD retains the sampled one.

### Nonodd symmetry and fitted orthogonal reference — PASS

The transformation `(W,A,c) -> (WR,A,-c)` swaps the two hidden sample inputs and negates readout, giving `(f1,f2) -> (-f2,-f1)` for every activation. It preserves the loss, raw metric, and initialized law. Deterministic canonical limits consequently have `f1=-f2=b`; activation oddness is not required. The candidate correctly limits the corresponding unbounded statement to a canonical symmetric strong interval.

For `h=(H1-H2)/2`, the displayed strong derivative J and actual adjoint J* have the correct full-row and HS blocks. In feature time, `c_s=h` and hidden velocity is `J*c`, so

`b_s=||h||²+||J*c||²`, and `c_ss=JJ*c`.

With `N=||c||`, `N''=(||h||²+||J*c||²)/N-<c,h>²/N³ >= 0`. The small-time expansion gives `N'(0+)=sqrt(q0)`. The separate argument excluding a return to N=0 is valid. Hence `||h|| >= N' >= sqrt(q0)`. This establishes the trained lower bound rather than assuming kernel monotonicity.

Initial first-layer covariance is the uncentered Gram `v I + mu² 11^T`, with `v>0` by nonconstancy and Gaussian full support. The upper pair has a positive density, so `q0=(1/4) E(phi(Y1)-phi(Y2))²>0`; linear growth guarantees finiteness. Physical time gives `b_t=2(1-b)K`, with continuous finite K on a compact strong interval, and therefore `L(t)<=exp(-4 q0 t)`. The conversion `T_phi=log(8)/(4 q0)` is correct.

B.1's hypotheses are satisfied for the bounded subclass. Its summed-loss clock is correctly converted to the mean-loss clock. The general equal-length anchor parameter g is consistent: normalizing the raw anchor direction and replacing its first coordinate activation by `v -> phi(sqrt(g)v)` preserves the original row dynamics. B.1 supplies global canonical existence, finite GF capture, and the stated sufficient `eta_n sqrt(n)->0` raw-GD condition. It supplies neither E for closure through that horizon nor a nonorthogonal theorem. The equal-label and balanced-sign extensions retain the exact symmetry needed for the same radial argument.

### Continuation interface and row-removal partial — PASS AS CONDITIONAL/PARTIAL

`REFERENCE_PROOF.md` 196–278 states both necessary premises for its sufficient construction: uniform transformed-Euler norm bounds and uniform readout exponential moments. The scalar flow coordinate removes the lower gate without dividing by it. The clock comparison localizes only the reference c; exponential tails overcome the linear-in-cutoff stability exponent on sufficiently short subintervals. Sending meshes to zero first at a fixed cutoff and then removing the cutoff, successively over finitely many intervals, is valid. Fatou transfers tails; the same one-reference estimate gives uniqueness. The premises are not claimed from energy alone.

The raw energy identity and finite-endpoint Cauchy estimate in section 7 are correct, including their failure to imply fresh local existence at arbitrary reached L2 data. The row-deleted finite trajectory is independent of the deleted initialized middle row. Conditional Gaussianity, the path covariance-trace estimate, the Gaussian Hilbert-vector exponential bound, and the resulting entire-path driver envelope in section 11 follow as stated. The reinsertion term uses the actual coupled trajectory and is explicitly uncontrolled. No bound for it is hidden in the deletion argument.

### Gaussian initializer, density, and actual actions — PASS

I inspected the complete supplied Gaussian foundation, including adaptive conditioning, singular Gram regularization, named-source derivatives, actual adjunction, HS estimates, and multiplier/chain-rule statements. Adaptive queries are conditioned on the transcript; the response terms are essential and retained. The full uncentered operand Grams are used. Singular laws use either a fixed pseudoinverse construction or continuous positive square roots, without claiming pseudoinverse continuity.

The closure's dictionary uses smooth bounded probes and their correctly typed actions, independently of the target activation and trajectory. Known bounded parent ranges permit smooth Lipschitz extensions of product instructions. Its initializer consequently does not demand higher derivatives of phi. The Fourier totality argument applies to arbitrary finite-coordinate laws, so density does not presume moment determinacy. The completed pair is invariant under both A0 and A0*, hence reducing.

The positive feature ridge gives contractions U and Q. For a fixed earlier-span vector, the bound `||(I-Q)S v||² <= eta_N |v|²/4` proves strong convergence by density, including redundant or singular dictionaries. Both orientations of `B_N=Q2 A0 Q1` converge strongly with uniform operator bounds. The proof correctly avoids an operator-norm approximation to A0 on the whole Hilbert ball.

### Fixed-order dynamics, closure, and restart — PASS UNDER S/E

The finite-type state is exactly two joint population laws and M. Its transpose operation uses M^T, and the learned increment evolves by the displayed positive two-sided filtering. Current correlations and the frozen first row g are retained. These are still probability-law fields before cubature, not finitely many scalar coordinates.

At fixed N, bounded marks give local Lipschitzness in `(w-g,c)` with L-infinity norms and M in finite dimensions despite unbounded g. The energy identity uses the true M Frobenius gradient. It bounds the raw increments uniformly in N; fixed-order bounded marks then turn these into pointwise velocity bounds needed for global continuation. The operator bound used there is also justified by `||M||op <= ||D_N||op+||M-D_N||F`. Restart uses precisely the saved joint state.

Under S/E, Euler-to-target comparison proves observable-space invariance; it is not assumed through ambient Hilbert local Lipschitzness. The target's time/input images are compact in L2, and its middle velocity is compact in HS. Strong action convergence on these compact sets and finite-rank approximation of the HS velocity prove vanishing error production.

For propagation, the upper c cutoff and lower q cutoff enter additively. Subtracting the adjoint action before the lower gate does not multiply two cutoff factors. Thus the estimate is `e' <= C(1+R)(e+epsilon_N)+CM exp(-aR)`, not one with R². Choosing logarithmic R gives the displayed Osgood estimate and convergence on every fixed S/E interval. Only the reference needs tails. This also proves uniqueness against bounded strong competitors and justifies Euler invariance. The weaker Osgood interface has the correctly divergent reciprocal-modulus criterion.

The complete reached-hierarchy argument is valid within its stated domain: matching jointly retained typed probes identify the observable spaces and both actions, transported future HS increments remain supported there, and one-reference uniqueness identifies the continuation. It does not provide existence for arbitrary formal hierarchy sequences or after an unmatched data change.

### Observations, whole-circle convergence, and the longer finite bridge — PASS UNDER THEIR STATED PREMISES

The full-row formula retains off-training directions. Predictions have the stated input Lipschitz bound from two activation Lipschitz constants, the actual action bound, row L2 norm, and readout L2 norm. Fixed input convergence plus finite circle nets therefore gives whole-circle prediction convergence for the finite model. The closure's corresponding conclusion follows separately from compact target sets in its common carrier.

For any separately fixed declared observation graph, Lipschitz maps, bounded continuous multipliers, and both strongly convergent action orientations preserve L2 convergence. Compact target node curves make this uniform in time. Same-carrier coupling then gives W2 joint laws and quadratic moments. Initial upper features reconstructed with D_N converge to the actual initial action features. Initial/current pairs are genuinely paired; independent marginal coupling is not substituted. Products require a uniform declared bounded factor, not the order-dependent fact that a particular c_N is bounded.

The conditional finite bridge in `PARTIAL_RESULT.md` 131–209 is a valid additional argument beyond the closure theorem. Fixed-mesh oracle programs use continuous linear-envelope instructions, hence A.1. Recomputed rank actions differ by finitely many vanishing contractions, with backward products transferred by localization. Euler-to-target convergence gives uniform node error z_Delta; the elementary threshold inequality transfers target tails to proxy tails with this additive error. Width is taken first at fixed mesh/cutoff, mesh next, and cutoff last. Iterating short intervals is legitimate: each preceding initial discrepancy vanishes in that same iterated limit before the next interval's cutoff is removed. Raw GD first-exit bounds require only `eta_n -> 0`, not a maximum-neuron bound. GF uses its finite energy bounds. These arguments do not establish S/E at T_phi.

### Activity and visited-law nonaffinity — PASS LOCALLY

I checked the entire weighted C.3 correction, including the independent unused Gaussian contribution in the forward/reverse/forward calculation. Gaussian ridge independence gives positive definite first features; the response Gram stays positive with nonodd activations and flat gates. Multiplication by the corresponding activation derivative retains positive squared displacement coefficients. The weights must enter as `p_a=omega_a y_a`, and the candidate uses this convention.

Thus each layer's paired activation displacement has a nonzero order-t² L2 coefficient for every sample. Initial Gaussian full support and nonaffinity give a strictly positive best-affine-fit error; continuity of variance and covariance preserves it on a possibly shorter initial interval. This establishes early-time activity and visited-law nonaffinity. It does not establish either quantity at the later fitting endpoint.

### Source-response partial and rare-event obstruction — PASS WITH THE STATED SCOPE

The orthogonal clock program is correctly distinguished from exact raw Euler. Its source equations retain the complete current backward response row, learned Gram terms, controls, and sample masses. Under the explicit backward response cap, the lower clock pulse bound has no random Q multiplier. The resulting subGaussian estimates and upper response recurrence retain the weighted time integral of |c|. Jensen and the moment bound give the explicit scalar cap test. First-failure induction uses only prior response rows when constructing the current forward state; it is not circular. The test yields a positive local interval, but no global cap has been selected. The C1,1 passage is conditional on a mollification-independent cap, as required.

For `phi(z)=z+epsilon sin(z)`, the first raw Euler state indeed leaves both hidden blocks at initialization and sets `c=h(phi(Z1)-phi(Z2))`. Orthogonality and oddness in this particular counterexample give the displayed opposite residuals. On the selected Gaussian rare events, unit HS perturbations change only sample 1, the first directional prediction derivative tends to zero, and its second derivative grows positively without bound. Multiplication by the negative residual makes the loss second directional derivative tend to negative infinity. This contradicts local Lipschitzness of the raw gradient and of the clock field in K-only directions. It is a reached Euler state, not a proved positive-time GF state. The obstruction does not concern independent Gaussian probe directions or rule out GF, source tails, or another closure.

The feature-energy counterexample correctly attacks only the proposed implication from Hilbert speed control to uniform spatial exponential moments; it is explicitly not a neural trajectory. The bounded-activation truncation discussion correctly retains later activation-value and weighted-gate defects. Uniform energy or small initial clipping error does not remove them.

### Numerical consistency and validation implementation — PASS FOR THE QUALIFIED CLAIM

At fixed order, bounded mark envelopes and positive feature ridge control the law perturbations. The contraction involving unbounded first features is handled by Cauchy–Schwarz. The upper finite action and fixed-order c,q bounds supply the remaining stability constants. Gaussian quantization has vanishing Wp error and uniformly integrable polynomial moments; finite smooth source programs permit successive cubature and source-regularization removal. Replayed marks retain joint laws with frozen initializer coefficients. Atomic characteristic systems are finite locally Lipschitz ODEs, and the stopped Euler/Heun comparison establishes their time-refinement limit.

The nested order is arithmetic precision, time, replay cubature, initializer cubature, source regularization, then dictionary order. No arbitrary refinement diagonal, hierarchy rate, or computable accuracy-to-order choice is proved. Literal finite-precision execution additionally requires the stated phi/phi' evaluators and data representation; C1,1 regularity alone is insufficient. The checkpoint count correctly stores both joint populations, M and D, and weights. This is a mathematical consistency construction, not a delivered general-activation solver.

I inspected all functions in the frozen finite-network API and its imported Gaussian-moment module. The forward normalization, residual-free backward pass, raw contractions, endpoint mobility cancellation, simultaneous GD, and finite metric agree with the mathematical identities tested. The C1,1 example is legitimate for these supplied-state first-derivative checks even though the general code guide states C2 as a sufficient finite-flow contract. `gaussian_moments.py` is imported by the package initializer but not used by these tests; its exact PSD validation and Wick recurrence have no effect on the identity results. The script is NumPy/standard-library only and performs no trajectory training.

## Reproduced computation

The pre-execution decision rule was to run the frozen `check_identities.py` unchanged against only its frozen local code, and to treat any assertion failure as a failed identity check. No threshold was altered and no exploratory training or parameter search was run. The child process had a hard 120-second CPU limit and 120-second wall timeout; numerical libraries were limited to one thread and bytecode writing was disabled.

```text
PYTHONPATH=/home/amir/Codes/PDE/data/generated/cx2_activation_class_20260919/review_r2_inputs/code
PYTHONDONTWRITEBYTECODE=1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
/usr/bin/python -B /home/amir/Codes/PDE/data/generated/cx2_activation_class_20260919/review_r2_inputs/check_identities.py
```

Result: **2 tests passed**, each iterating over softplus, oscillating-linear, nonodd bounded, and quadratic-smoothed-ReLU activations. They check prediction/loss/GF/raw-step symmetry and the feature-ascent chain rule with the raw metric, using forward-only directional finite differences for the latter. The original tolerances were preserved. Exit code was 0. The unittest run reported 0.057 seconds; child CPU time was 0.144 seconds and subprocess wall time 0.163 seconds. Environment: Python 3.10.12, NumPy 1.26.4. Full output is in `review_r2_b/identity_checks.log`.

These checks neither prove the radial inequality for a trajectory nor test a Gaussian-program limit, hierarchy convergence, global fitting, tail cap, or practical solver. Those verdicts above rest on the inspected mathematics and its explicit conditional scope.

## Remaining obligations and completion

There is no unresolved objection to the exact partial/conditional assertions certified above. The following are unresolved mathematical or implementation obligations for the larger target, not assumptions verified by this audit:

1. Construct a unique canonical strong flow for every allowed unbounded activation through its fitting horizon T_phi.
2. Prove adequate reached tails for that flow and its construction, or a different sufficient stability/existence estimate. The reference's readout-only transformed-Euler interface is sufficient but unverified globally; closure S/E needs the stated actual c and q tails.
3. Establish continuation and source control through the fitting horizon in a positive correlated-input neighborhood. Neither an orthogonal flow nor fixed proximity to it supplies this changed-data construction.
4. Supply and validate an executable general-activation solver with its evaluation interface. Numerical implementation alone cannot close the preceding mathematical gaps.

An affirmative internal review of this package therefore supports local full-class learning and closure, the bounded orthogonal fitted reference, and the conditional extensions. It is not evidence that full C-X2 has been completed or that unbounded continuation has been proved.

**Completion:** all frozen components and their supplied dependencies have been inspected, truncation repaired, the authorized bounded checks reproduced, and final manifest/file hashes verified unchanged.
