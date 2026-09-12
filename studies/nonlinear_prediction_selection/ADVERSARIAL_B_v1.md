# Independent complete adversarial review B — candidate v1

**Verdict: REVISE for one minor but required mathematical statement correction.**

I found no failed implication in the main theorem for the actual parameter rectangle (NS1), after checking the full supplied dependency proofs and independently executing the exact rational certificate. However, the auxiliary linear-independence assertion in B.2 is false for a list with repeated inputs under its stated “nonantipodal” hypothesis. The missing pairwise-distinct hypothesis is used in its proof. The actual triple `(e1,e2,u_alpha)` satisfies the stronger condition, so this objection does not furnish a counterexample to the main selection theorem. It does prevent an unconditional PASS on the present frozen text, whose assignment requires correctness of every proposed mathematical assertion under its stated quantifiers.

The complete objection, positive component findings, evidence and completion record follow. This is my original report, not a consolidation of another review.

## 1. Assignment, identity and isolation

Reviewer identity: `/root/adversarial_b_v1`. This is a fresh isolated reviewer, distinct from `/root`, `/root/conditioning_route`, `/root/continuation_route`, `/root/geometric_route`, and `/root/relevance_selector`. I received the neutral assignment and its expected candidate hash, with no inherited author discussion. I did not communicate with reviewer A or read another review.

I read the complete `REVIEW_ASSIGNMENT_v1.md`, `AGENTS.md`, and `RESEARCH_WORKFLOW.md`, including the independent isolated review scope. I applied `solve-math-rigorously` and `investigate-conjectures`, reading their complete skill instructions and the latter's applicable `research-contract.md`, `adversarial-audit.md`, and `decisive-experiments.md` references. The isolated assignment replaced ordinary author startup: I did not read the study README, routes, author drafts/checks, source-coverage record, selector verdict, other tasks, other studies, or Git history. Links in the frozen guides were not followed. No external scientific source was fetched or assumed to fill a gap.

The only repository scientific inputs were the complete frozen files listed in section 2. A metadata-only Git status and current-HEAD query were made; no contents of other studies or Git history were inspected. No Git mutation was made. I wrote only this report and files in `data/generated/nonlinear_prediction_selection/adversarial_b_v1/`. No training experiment or established-file edit was performed.

## 2. Actual source coverage and fingerprints

All paths in this table are relative to `studies/nonlinear_prediction_selection/`. “Complete” means every line was read, including all scientific proof lines, rather than merely searching for selected statements. The start and end fingerprint records agree for all files, and the hashes agree with the supplied manifest entries wherever the manifests specify them.

| Frozen input | Lines read | SHA-256 |
|---|---:|---|
| `REVIEW_ASSIGNMENT_v1.md` | 1–96, complete | `57b550e6f4abf2a8d327e1f84e34a67ed5bdd49316f4fda34820c93f27af05c4` |
| `CANONICAL_ADDITION_v1.md` | 1–2300, complete | `e53cefcd3aa58c456d8cee49bc7bff8c6330bffb1f05b9d8baa3646074189404` |
| `PROPOSED_EDITS_v1.json` | 1–16, complete | `0493be3c29d2499826320e3324dea54a77ec865b494e0db0e169a438d3c9c006` |
| `PROPOSED_GUIDE_v1.md` | 1–285, complete | `d5ecdfd35fbddd511d98dccd148a9a9e840f5a4c814658f930c5732bab218bc5` |
| `DEPENDENCIES_GLOBAL_v1.md` | 1–8901, complete | `6ebdaf1a3b28bdd07244a7b8c1bb882a36c7c525c4170cd25af4d7661ab7d942` |
| `DEPENDENCIES_GAUSSIAN_v1.md` | 1–550, complete | `c95e358f6bb9741858e6293dabacf4fee01927a23cda1289cd3cd17e85a1ee77` |
| `DEPENDENCY_GUIDE_v1.md` | 1–284, complete | `5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f` |
| `DEPENDENCY_NOTATION_v1.md` | 1–98, complete | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `DEPENDENCY_MANIFEST_v1.json` | 1–44, complete | `75f8b2ae6716fb88d8f89306b78a104a2bffc62e1bf67bb64474b8298d5b415a` |
| `verify_reference_certificate.py` | 1–58, complete | `07c51c139ebf66912ef7b730201dcc71581b11355dd29dbee6140bf2bba63118` |
| `REVIEW_MANIFEST_v1.json` | 1–42, complete | `357a7b3bc9e805749fb8c5f3383400edfce0bdc56277861ce74987b0d65d67e7` |

The candidate hash is exactly the hash named in the assignment. The global dependency file's declared original source ranges are 1840–2461, 2462–3440, 3836–4947, and 5269–11439; I read all of their frozen extracted bodies. Its declared upstream source hash is `bda93ec446425c05f8c06ac3a67fa1505906dff309b74e13bab4effc1527bf05`. The Gaussian dependency's declared upstream source hash is `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489`. These upstream identifiers are provenance from the frozen manifest, not a claim that I fetched or reread the current live originals.

Read coverage was checked explicitly after truncation. An initial batched output truncated part of the candidate/guides; I repaired it by standalone complete reads of candidate lines 1–500 and of the proposed and dependency guides/notation. Candidate lines 501–1100, 1101–1750, and 1751–2300 were then read in complete standalone outputs. The initial Gaussian-file output omitted a short passage in III.F.5; standalone reads of lines 245–265 and 265–290 restored the full covariance square-root passage and its surrounding argument. The 8901-line global dependency was read in the following contiguous, nontruncated outputs: 1–650, 651–1350, 1351–2050, 2051–2750, 2751–3500, 3501–4250, 4251–5000, 5001–5750, 5751–6500, 6501–7200, 7201–7900, 7901–8500, and 8501–8901. No known truncated scientific passage remains.

The shared instruction files had hashes `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` (`AGENTS.md`) and `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` (`RESEARCH_WORKFLOW.md`). The metadata-only HEAD query returned `f98be192b9b95002db4b3bef400c65bddc860e9f`. This does not replace the per-input content hashes.

### Dependency use, not merely dependency reading

I checked the included Gaussian III.F.1–III.F.11 proofs for finite joint program laws, separately named reused forward/transpose sources, true-adjoint contractions, singular covariance, common-carrier consistency, convergence of at-most-quadratic observations, and joint same-array programs. In the global excerpt I checked the actual action/operator construction and raw scalar chain rule; the local cutoff/Osgood/Euler arguments; C.4.1–C.4.3's normalization, generated carrier and finite-program approximation; all of the included C.4.5 clock and endpoint proof; and the C.4.6–C.4.7 source, Gaussian-envelope, tail, continuation and approximation arguments used by the addition.

The reference results actually used are its physical-clock identification, unique fitted endpoint with `s_dagger <= 10`, raw convergence rate, endpoint norm and prediction bounds, and the joint subGaussian envelope controlling the transformed first rows over the complete feature interval. The finite-source results actually used concern fixed finite graphs and their common carrier, plus Gaussian and bounded-response decompositions under explicitly controlled source rows. The addition separately proves its longer mixture continuation and finite-GF comparison. I did not infer these longer statements from an existing fixed-`T=40` law-response theorem.

Unchanged claims mentioned in guide context, including the C.4.8 sampling-limit statement, were not used as missing proof inputs for C.4.9. This is not an unrestricted independent audit of every chapter advertised by the unchanged guide.

## 3. Architecture, normalization and precise target

The finite model in the candidate matches its stated original network: independent full two-coordinate Gaussian first rows of variance 1, a reused Gaussian middle matrix with stored variance `1/n`, and an actual independent Gaussian stored readout with variance `1/n^2`; forward prediction is `c^T h2/n`. The first layer uses `u=x/sqrt(2)`, so the trained physical inputs are on `sqrt(2) S^1`. The raw finite metric is first-block Frobenius squared divided by `n`, middle-block Frobenius squared, and readout squared divided by `n`. Its gradient factors match mobilities `(n,1,n)` and the unhalved mean-square loss. In particular the two equally weighted reference atoms give the reference contribution `-G r`, while the added atom gives `-2 epsilon r_p g_p`.

The population initialized readout is zero because that is the limit of the stated finite array. The finite comparison does not replace the actual readout by zero: it starts both compared finite paths with that array. The initialized middle action is retained as `A0`; only `K=A-A0` is Hilbert–Schmidt. Both orientations of the same action, with its actual Hilbert adjoint, are used throughout. No independent transpose surrogate appears.

The proposed determining equation uses the current `G`, current invertible `M=G*G`, and current orthogonal projection `Pi=I-G M^-1 G*`. Its hidden features, middle increment and readout all evolve. It describes a finite positive slow-time episode, with a width-first limit at each fixed positive epsilon. The theorem excludes slow time zero from the original-initialization convergence, claims whole-circle predictions, and measures paired second-hidden activations on the same initialized carrier. I found no implicit simultaneous width/epsilon rate, raw-GD claim, or changed-law final-endpoint claim in the statement.

## 4. Uniform source-control audit

This is the main point at which a raw Hilbert norm estimate would be insufficient. I checked the source cap as a separate claim rather than treating bounded `w,K,c` as evidence for Gaussian query tails.

### Controls, zero slots and singular sources

The integrated Euler controls are the quantities compared. Using a dominating row mass `m=|gamma|+|bar gamma|` and setting the relative control error to zero when `m=0` yields the exact weighted identity `sum m e = sum |gamma-bar gamma|`. The controls being compared can have a zero coefficient on one side and a new coefficient on the other. A past zero-control source has no subsequent state injection. A distinguished current passive source can have a direct current-query response; that response is not incorrectly counted as an old injected state after a zero update.

The finite source recursion retains separately named calls even for coincident directions or singular source covariance. CT12–CT16 explicitly differentiate the named source slot while holding the deterministic controls, residual coefficients and source covariance fixed. Covariance differentiation or differentiation of feedback control coefficients is not silently included. The common-source comparison in CT17 uses the Gaussian isometry; it does not require a Lipschitz matrix square root at a rank-deficient covariance. This is consistent with the supplied III.F conventions.

### Reference anchor and raw-to-clock transfer

The elementary raw bounds `||c||_infty <= L`, `||K||_HS <= L^2/2` and `||A|| <= 2+L^2/2` are used only as raw bounds. A Gaussian-plus-bounded query decomposition first requires a temporary source-row cap. The proof then establishes the reference cap using the full bounded feature interval, not a physical-time bound growing like `1/epsilon`.

I checked the transverse fresh-Gaussian pulse extraction. At a fixed finite graph, take the width limit, then let the pulse amplitude tend to zero. Source derivatives at clipped roots admit a deterministic bound independent of the root clip; continuity of covariance square roots suffices, including singular covariance. Because the fresh root is independent of the unforced source groups, its correlation with the forced node extracts the named-source derivative coefficient. A value-only clock estimate would not establish this transverse coefficient bound, but the displayed pulse construction supplies it.

The raw Euler step is not asserted to be exact clock Euler. CT22–CT23 keep the hyperbolic transform's second-order defect and its differentiated defect, including the terms containing derivatives of both `w` and the step field. Dividing a pulse response by its own injection mass leaves an order-`h_s` error. Summation gives `sum h_s^2 <= h_max sum h_s`, and the temporary-cap exponential moments control the hyperbolic factors. The transformed pulse equation has bounded clock gates and does not retain an uncontrolled random `Q` multiplier. Its deterministic Gronwall estimate supplies the raw reference source cap after the mesh error is absorbed. I found no hidden passage from value convergence to source-derivative convergence.

### Perturbation cap closure

For a controlled history under the temporary cap, the lower pulse is bounded by its injection mass times an exponential of accumulated absolute query force. Jensen's inequality gives the required exponential-moment bound for `sum |gamma_s| |Q_s|` with total control mass fixed; no maximum over all time indices and no independence between query times is used. The upper row is bounded by a Volterra estimate.

The one-reference raw comparison propagates only the two reference directions and pays a new direction through the control discrepancy. It has a modulus tending to zero with that discrepancy at the same mesh, without a nonvanishing discretization floor. In the source-row comparison I checked the direct `D` coefficient difference, the lower differentiated pulse injection, and the upper differentiated gate terms. The upper formula retains the term with the readout difference multiplying the reference second derivative and the term with the changed second derivative multiplying the changed readout.

The interpolation step uses actual higher moments provided under the temporary cap. Interpolation from `L2` to `L12` with an `L24` bound gives exponent `1/11`; the weakened exponent used in the final modulus is conservative. Hölder is applied to the displayed products before the deterministic source masses are summed. Rowwise Gronwall uses only preceding rows, so the first-failed-row bootstrap is causal. Choosing the cap as the reference cap plus one and making the integrated-control discrepancy small makes that first failure impossible. It then yields the Gaussian query tail by Gaussian-plus-bounded decomposition.

**Finding for unit A:** the proposed argument closes the claimed population named-source cap uniformly in the physical horizon, including zero/new controls, passive current slots, all retained old sources and singular covariance. It does not claim a probability bound uniform over all empirical feedback laws, and the later finite proof does not need such a claim.

## 5. Endpoint conditioning and the required correction

### Protected rows and dependence on the first roots

The supplied C.4.6 envelope gives a single joint random variable `N` with `||N||_p <= C sqrt(p)` controlling the transformed first-row displacement over the complete reference feature interval. The resulting bound `sup_s |X_a(s)| <= 5N` is on the same carrier as the first roots `g`; independence of `N` and `g` is not available or assumed.

For a direction `v` with nonzero coordinates, the candidate instead compares the Gaussian box probability around `r v`, bounded below by a constant times `exp(-O(r^2))`, against `Pr(N>r^2)`, bounded above by `exp(-c r^4)`. Thus their intersection has positive probability for large `r` even with arbitrary dependence. The inverse transformed-coordinate bound then gives `sup_s |w_a(s)-g_a| <= 20 e^2 r^2 exp(-2 rho r)`, tending to zero. This justifies the simultaneous limiting sign patterns used to test linear relations among endpoint tanh features.

### Objection B-1: repeated inputs invalidate the auxiliary assertion

**Location:** `CANONICAL_ADDITION_v1.md`, B.2, lines 1035–1048, particularly the assertion at lines 1045–1046 that the nonantipodal condition means no other sign changes at the selected perpendicular line.

**Exact failure:** a finite nonantipodal list need not be pairwise distinct. Set `m=2`, `u1=u2=e1`, and `(a1,a2)=(1,-1)`. No pair is antipodal, yet

\[
\tanh(w_\dagger\cdot u_1)-\tanh(w_\dagger\cdot u_2)=0
\]

identically, with nonzero coefficients. At the perpendicular line both signs change together, so the subtraction establishes a relation for the sum of the coefficients at that repeated direction, not `a_k=0` separately. No definition in the supplied candidate or notation contract strengthens “nonantipodal” to exclude repetitions.

**Required correction:** say “a finite pairwise distinct, nonantipodal list” or state `u_i != +/- u_j` for every `i != j`, and use that combined condition in the sign-crossing sentence. An alternative is to restrict this auxiliary argument directly to the actual triple `(e1,e2,u_alpha)`.

**Severity and downstream effect:** minor scope/statement defect, not a refutation of the main theorem on (NS1). Every actual triple in the compact rectangle has pairwise distinct, nonantipodal unit inputs. With the stated correction, the displayed proof proves exactly the needed independence without a new estimate or additional scientific input. Nevertheless the stronger assertion as written is false, and this review does not silently insert the missing hypothesis.

### Conditioning on the actual family

For the intended triples, crossing the perpendicular line isolates one sign, hence the first-hidden Gram is positive definite. The endpoint readout is nonzero because an anchor is fitted to 1. Since the second-layer gate is strictly positive at finite preactivation, each `delta(u)` is nonzero in `L2`.

For the middle-block gradients the tensor Gram estimate is

\[
\left\|\sum_i a_i\,\delta_i\otimes H_i^1\right\|_{HS}^2
\ge \lambda_H\sum_i a_i^2\|\delta_i\|_2^2.
\]

This does not assume injectivity of `A0` or `A_dagger`. Continuity over the compact angle interval gives a uniform positive lower bound. It controls both the full two-anchor Gram and the three-input middle Gram. The coefficients `t=(-beta,1)` of the projected added gradient have `|t|>=1`, so the projected gradient has a genuinely positive middle-block component. No numerical lower bound for this compactness constant is asserted.

The reference bounds give whole-circle endpoint Lipschitz constant less than 76 and zero prediction at the diagonal direction. The angle interval of radius `1/1216` therefore gives `|f_dagger(u_alpha)|<=1/16`; the declared labels imply `y-f_dagger(u_alpha)` lies in `[5/16,11/16]`. These estimates are uniform on the full compact rectangle, whose interior is nonempty and whose directions are nonorthogonal to both anchors.

## 6. Nonlinear episode and genuine hidden activity

The local raw-continuity estimates use the fixed endpoint's bounded readout and its `L4` queries. For example, bounded gates and an `L2` preactivation difference yield an `L4` gate difference with a square-root modulus. Multiplying it by a fixed `L4` query is legitimate in `L2`. This avoids assuming a uniform ambient `C2` bound in a space where an arbitrary product of two `L2` fields need not lie in `L2`. The finite-dimensional Gram inverse and projector inherit the needed continuity while the anchor Gram stays uniformly positive.

The hidden observable is a fixed-endpoint-readout contrast of the three evolving second-hidden features. Its endpoint gradient is the hidden part of the projected added gradient, with zero readout component. Consequently its directional derivative in the constrained field is

\[
O'(0)=-2r_p\,\|d_H\|^2\ge 5\kappa/8.
\]

This is not a readout displacement masquerading as hidden activity. The contrast's derivative has a uniform modulus along the actual moving field. The chosen raw radius retains `O' >= 5 kappa/16`, and the bounded-velocity first-exit argument provides a common positive time interval contained in that radius. Hence its finite change is at least `gamma_O tau`, with `gamma_O=5 kappa/16`.

Cauchy–Schwarz with the fixed readout and the three fixed coefficients gives `|Delta O|^2 <= 30 T0^2 J2`. Thus the stated hidden margin can be taken as `gamma_O^2 tau0^2/(30 T0^2)>0`. It compares the episode to the already fitted reference state on the same carrier and therefore excludes inherited reference activity and parameter-only displacement.

The exact added prediction derivative is `-2 r_p ||Pi g_p||^2`; the unhalved added-risk derivative is `-4 r_p^2 ||Pi g_p||^2`. The retained bounds `|r_p|>=5/32` and `||Pi g_p||^2>=kappa/4` yield risk gain at least `25 kappa tau0/1024`, independently of epsilon and width. The reference predictions are preserved by the exact identity `G*Pi=0`. These are finite-interval deductions for the constructed nonlinear solution, not extrapolations of its initial derivative.

**Finding for unit B:** the endpoint conditioning and both activity margins are proved for the actual family, subject to correcting the unnecessary broader assertion identified in B-1.

## 7. Construction, continuation and the slow limit

### Construction and uniqueness on the canonical carrier

The controlling modulus is Osgood: `omega(z)=z sqrt(log(e/z))` near zero and `integral dz/omega(z)=infinity`. The stated comparison envelope follows by substituting `sqrt(log(e/z))` in the scalar inequality. Its use is restricted to the small-distance region, with first exit excluding escape for sufficiently small initial error. The comparison only needs Gaussian tails on the constructed reference path; a competing strong solution is not silently assumed to have those tails.

The constrained path is built by finite reference prefixes followed by finite controlled Euler programs. Those programs exist before a limiting constrained path is invoked. Feedback coefficients are computed from the current finite-program state and bounded on the stopped invertible-Gram region. The omitted reference tail, finite-prefix approximation error and added control mass fit inside the source-control tube. Raw displacement bounds keep the stopped paths within the Gram region; then source control supplies the tails and Osgood comparison makes the meshes and reference prefixes Cauchy on the common carrier.

The countable program construction and joint source law are used for common parameter/mesh approximations, followed by continuity for the complete compact parameter family. Lipschitz soft cutoffs pass query tails to the limit, and higher uniform moments upgrade query `L2` convergence to the `L4` continuity used later. This supplies a strong constrained solution with its retained reference history. Uniqueness follows by the one-reference Osgood estimate. The equation's coefficients depend only on current state and initialized primitives, not on an unknown limiting mixture solution.

### Derivatives in the raw topology

I checked the derivatives needed for the residual product identity separately from scalar differentiability. Along reached controlled paths, the first-weight velocity has an `L4` bound proportional to accumulated control density; readout velocity is pointwise bounded; the middle increment velocity is Hilbert–Schmidt. These facts, the bounded gates/readout and the source query moments justify the successive `L2` derivatives of `H1`, `Z2`, `H2`, `delta`, and `Q`. In the differentiated first-gradient component the necessary product is `L4` times `L4`, hence lies in `L2`.

It follows that `G`, `M`, and `B=G M^-1` are absolutely continuous along these paths, with `||B'||` bounded by a constant times the control density. The inverse derivative is the ordinary derivative of a uniformly invertible two-by-two matrix. Thus the strong product rule for `B r` is available. No ambient bounded Hessian assumption is used to justify it.

### Actual-mixture continuation precedes trajectory use

On any fixed initial interval `[0,b]`, the actual mixture Euler recursion exists outright. A crude deterministic bound controls these finite recursions. The one-reference raw comparison gives closeness to the reference when epsilon and the mesh tend to zero with `b` fixed. This in turn gives integrated-control closeness on that prefix before the source theorem is applied to the actual-mixture history.

After `b`, the proof works with stopped actual Euler programs and their affine partial steps. Under the stopping conditions they are legitimate controlled histories in the source tube. The established `L4` bounds justify the residual Taylor expansion with remainder `C h^2 (|r|+epsilon)^2`. The positive anchor Gram then gives the stable recursion

\[
|r_{k+1}|\le (1-\kappa h_k)|r_k|+C h_k\epsilon.
\]

The integrated residual force is therefore bounded by `C|r_b|+C epsilon(t-b)`, without a term that grows as `h t` independently of epsilon. The comparison budget includes the complete physical reference tail, not an abruptly stopped reference trajectory. Choose `b` large, then epsilon/mesh small, then a common small slow-time length. Both the raw-neighborhood and control-budget first exits are excluded through `b+tau0/epsilon`. Fixed-epsilon Osgood completion yields an actual population GF on the required finite horizon. This order does not presuppose the long mixture path whose existence is being proved.

### Exact residual identity and initial layer

With `v=r_p g_p` and the actual reference residual vector `r`, the physical equations are

\[
\theta'=-(1-\epsilon)Gr-2\epsilon v,
\qquad r'=-(1-\epsilon)Mr-2\epsilon G^*v.
\]

For `B=G M^-1` and `V=-2Pi v`, direct substitution gives the exact identity `theta'=epsilon V+B r'`. In particular no factor of two or factor `1-epsilon` is lost by the elimination. Product integration gives

\[
\theta(t)=\theta(b)+B(t)r(t)-B(b)r(b)
 +\epsilon\int_b^t V(\theta(s))\,ds-\int_b^t B'(s)r(s)\,ds.
\]

The residual decay bound is `|r(t)|<=exp(-2 kappa(t-b))|r(b)|+C epsilon`. Combining it with `||B'||<=C(|r|+epsilon)` bounds the last integral by `C(|r(b)|^2+epsilon |r(b)|+epsilon^2(t-b))`. On the slow interval this is small in the required sequential order. The endpoint/prefix boundary terms are bounded by the distance to the fitted endpoint and `|r(b)|`.

At fixed `b`, epsilon tends to zero and Osgood comparison identifies the constrained path up to an error controlled by the reference endpoint error. Then `b` tends to infinity using the established reference decay. The shift from `epsilon(t-b)` to `epsilon t` costs at most a constant times `epsilon b`; it is legitimate uniformly on `[tau_-,tau0]` for every `tau_->0`. It cannot give convergence at slow time zero, where the actual original state is still the Gaussian initial state. The theorem explicitly excludes that point. Thus there is no imposed pretraining/reset in the proof or statement.

Uniformity in `(alpha,y)` follows from common compact-family constants at each comparison step. Raw-state convergence gives whole-circle prediction convergence by the bounded forward operator/readout estimates, and gives the finite named hidden convergence through the same carrier. No source coefficient is obtained by differentiating a law response on the diverging `1/epsilon` horizon.

**Finding for unit C:** construction, strong uniqueness, actual-mixture continuation and the original-time slow selection are justified in the claimed order.

## 8. Actual finite GF and paired observations

At a fixed width the actual finite GF is smooth and global on finite time intervals: loss dissipation bounds the integrated squared raw velocity, and Cauchy–Schwarz bounds finite-time displacement, preventing finite-time escape in the finite-dimensional parameter space. Its constants may depend on the separately fixed horizon. The finite readout supremum is bounded by its actual initial supremum plus `2T sqrt(L(0))`; it is not assumed initially zero.

For the stored readout law, the union bound gives `Pr(max_i |c_i(0)|>eta) <= 2n exp(-n^2 eta^2/2)`, which tends to zero. Its normalized square norm also vanishes. First-row root moments and the initialized middle operator bound have the required high-probability controls. These are consistent with independent full first rows and the stated stored variances.

The proof first uses a fixed finite population Euler program. Its deterministic coefficients are computed causally and then frozen for the matching finite-array program; both orientations of the original middle array are retained. The supplied joint finite-program theorem and at-most-quadratic observation extension give the needed convergence, including empirical contractions. Comparing the small actual readout to the zero population root at this fixed graph is handled by cutoff induction, not by a dimension-dependent uniform Lipschitz bound on an entire parameter ball.

Actual finite GF is next compared to a finite affine proxy initialized with the same actual readout, making their initial distance zero. The one-reference cutoff estimate uses Gaussian tails of the proxy and bounded actual readout/action. It does not require a fresh independent query representation for the feedback-trained finite GF. Additional finite time grids control proxy tails between observation times; the affine interpolation's query continuity and soft cutoffs justify that passage. The error has the structure of an exponential in the cutoff times discretization/finite-program error plus Gaussian cutoff tails. At fixed epsilon and finite `T_epsilon`, take width first with the finite graph and cutoff fixed, then a sufficiently large cutoff, then a sufficiently small proof mesh. The Gaussian quadratic decay dominates the linear-exponential cutoff cost. No uniform-in-epsilon finite-width rate is needed or claimed.

The whole-circle statement uses bounded input Lipschitz constants and finite input nets, together with time control. Finite internal observations from the two trained laws are included in one joint same-array program. This is essential: two separate marginal width limits would not identify their cross term. Here the bounded tanh observations and the joint law give the normalized squared difference directly. The factor `1/(3n)` in (NS9) corresponds exactly to `1/3` times the sum of the three population `L2` squares, with no cross-layer neuron pairing.

For each fixed epsilon, both finite networks are observed at the same finite time `T_epsilon`. Only after the width limit is taken does epsilon tend to zero; the population reference at that time approaches its fitted endpoint. A finite-width reference endpoint is never assumed. Continuity of the added loss on the relevant bounded range and the positive margins established earlier then imply the stated `a/2` and `j/2` event with probability tending to one in the iterated order. The population uniformity over the parameter rectangle is not converted into a stronger uniform probability statement over all finite trained laws.

**Finding for unit D:** the original finite GF, actual readout, whole-circle prediction and genuinely paired hidden observable are captured for every separately fixed law and epsilon, in the stated width-first order.

## 9. Independent exact rational certificate

I read all 58 lines of the certificate, checked its mathematical bounds, and independently executed it in the assigned checkout while saving the output in my own scratch directory. Its executable abstract syntax tree agrees with the complete embedded program in the frozen dependency; only comments differ.

Command:

```text
/usr/bin/python studies/nonlinear_prediction_selection/verify_reference_certificate.py
```

Working directory: `/home/amir/Codes/PDE`.

Environment: Python `3.10.12 (main, Aug 31 2026, 10:18:17) [GCC 11.4.0]`; executable `/usr/bin/python`; platform `Linux-5.15.0-151-generic-x86_64-with-glibc2.35`. `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, and `MKL_NUM_THREADS` were unset. Only the standard library and exact rational/integer comparisons are used for the assertions.

Exit status: **0**. Recorded elapsed time: `3.276370070874691` seconds. Standard error was empty. Complete standard output:

```text
[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]
```

The output-file SHA-256 is `ad40e8d8f73fed6d22cc9b68a19f7f9e6c3f2f59383d581e372ce0c976786900`.

I checked why the exact assertions certify the needed estimates. The positive Taylor polynomial through degree 80 bounds the exponential from below, and its omitted-term geometric majorant bounds it from above on the stated range up to 18. The alternating arctangent bounds give rigorous bounds for pi through the displayed Machin identity. The rational normal-density constants are verified by squared comparisons, and the endpoint products use the correct monotonic directions of tanh, squared sech and the Gaussian density. Outward rounding at denominator `10^12` is conservative. The omitted Gaussian tail beyond 4 is bounded by `10^-4` as required. The square-root bracket follows from exact squaring.

The printed decimal values are diagnostics, not the proof of a threshold. The exact comparisons certify `0.39<q<0.4`, `v>0.2`, `a0>0.3`, `r0>0.6`, and consequently the weaker reference coercivity `m>=0.1` used in the endpoint argument. No numerical training or floating-point convergence experiment was substituted for these inequalities.

Scratch evidence consists of `input_hashes_start.json`, `input_hashes_end.json`, `environment.json`, `certificate_run.json`, `certificate.stdout.txt`, and `certificate.stderr.txt` under `data/generated/nonlinear_prediction_selection/adversarial_b_v1/`.

## 10. Assembly and exact scope edits

I compared the full proposed guide against the frozen existing guide. The only changes are the two C.4.9 additions in the chapter navigation/scope descriptions; the remaining guide is unchanged context. The `replace_once` old sentence in `PROPOSED_EDITS_v1.json` occurs exactly once in the frozen global dependency. The proposed C.4.9 anchor matches the candidate heading, and the append target names this exact candidate. The edits do not modify the notation contract or maintained code.

The added navigation text describes the original fixed-mixture training, finite nonlinear episode, whole-circle prediction, added-atom improvement, paired second-hidden adaptation and width-first finite GF. These match the main theorem's scope. Local equation labels are declared local to the proof units; the scalar-gradient reference to A.4 is supplied by the included established argument. I found no broken scientific dependency on an author route, history artifact, missing external source or unseen selector/reviewer result. I found no normalization change introduced by assembly. The overly broad sentence in B.2 is the one identified exception to correctness of the complete proposed text.

## 11. Component verdicts and completion

| Component | Verdict | Reason |
|---|---|---|
| Original architecture, stored readout, adjoint and physical normalization | PASS | Equations and finite metric match the stated arrays, mobilities and unhalved loss. |
| Complete supplied dependency use | PASS | Required proof bodies were supplied, fully read, and their used hypotheses checked; no missing input remains. |
| Uniform integrated-control named-source cap | PASS | Reference transverse cap, raw-to-clock defects and causal first-failure closure supply horizon-independent query tails. |
| General nonantipodal-list linear-independence assertion in B.2 | REVISE | Repeated inputs are an explicit counterexample; add pairwise distinctness. |
| Endpoint conditioning on the actual family (NS1) | PASS | Actual triples satisfy the stronger separation condition, and protected-row/tensor-Gram arguments apply uniformly. |
| Constrained strong construction, uniqueness and nonlinear feedback | PASS | Controlled-program construction, source tails and one-reference Osgood comparison close on the canonical carrier. |
| Actual-mixture continuation and initial-layer slow limit | PASS | Euler continuation precedes trajectory use; full reference tail and exact residual product identity control the `1/epsilon` horizon. |
| Positive added-risk and paired upper-hidden margins | PASS | Exact risk derivative and fixed-readout hidden contrast give finite positive uniform margins. |
| Actual finite GF and joint same-array limit | PASS | Fixed-epsilon finite horizon, actual readout, cutoff comparison and joint programs give the claimed iterated order. |
| Exact rational certificate | PASS | Independently executed with exit 0; rational inequalities and program correspondence checked. |
| Scope/navigation assembly | PASS apart from B-1 in appended text | Exact proposed scope matches the main theorem and introduces no missing dependency. |

**Final verdict: REVISE.** The sole unresolved required correction is B-1. It is a minor false overgeneralization of an auxiliary claim; the actual theorem family avoids the counterexample. I found no additional unresolved mathematical, computational, dependency or isolation objection. This report does not approve promotion of the current frozen text, silently amend it, or substitute a weaker theorem for the assigned one.

The review is complete: all assigned frozen scientific lines and complete dependency proofs were read, every known truncation was repaired, all nine requested attack categories were examined, the exact certificate was independently run, and every frozen input hash was rechecked unchanged at the end. No author/history/other-review material entered the audit. The report and study-owned scratch preserve the original reasoning and execution evidence for the coordinator to inspect.
