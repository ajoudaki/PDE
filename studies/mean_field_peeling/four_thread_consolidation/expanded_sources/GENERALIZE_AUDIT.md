# Generalize non-local GF limit: recovered theorem and evidence audit

Evidence consolidation only, 8 September 2026. No new proof search or numerical experiment was performed. The main result below is an **accepted arbitrary-fixed-depth, arbitrary-fixed-finite-data joint width/vanishing-step theorem**. Treating this task as merely a proposed extension, or as a population-only formal construction, omits its completed result.

Task: `01a07193-3b8a-77a1-a00f-4ae928368b82`, “Generalize non-local GF limit”, on `remote-ssh-discovered:black-chatgpt`. Its predecessor was `01a07114-b2fd-78b0-bb18-fa4c15cff3d6`, “L=2 arctan, two inputs”, on the other host. The eight-turn complete export is [GENERALIZE_PAGE1.json](GENERALIZE_PAGE1.json); the end cursor is null and `hasMore=false`. No turn in this export is empty. All exported user/final messages were read; the first turn's artifact creation, review completion and final changes were inspected. Later turns were checked for new or superseding mathematical scope, rather than treated as replacement summaries of the first result.

## Accepted positive result G-P1: every fixed depth and fixed finite dataset

Primary authority: the complete 524-line [main proof](GENERALIZE_PRIMARY/GENERAL_POPULATION_GF_PROOF.md), the complete 540-line [depth response proof](GENERALIZE_PRIMARY/GENERAL_DEPTH_RESPONSE_PROOF.md), and the three complete independent reviews. This is a theorem on one absolute positive physical-time interval, often called “semi-global” in the conversation and local-in-time in standard terminology. It is not an all-finite-horizons theorem.

| Item | Exact admitted scope |
|---|---|
| Depth and width | Every separately fixed finite number of hidden layers `L>=2`; each hidden layer has width `n`. No depth growing with width and no depth-independent existence time. |
| Samples and input dimension | Any fixed finite `m,d`; `x_a∈R^d`, `||x_a||/sqrt(d)<=X`. Coincident, parallel, antiparallel and zero inputs are admitted for existence. `G_ab=x_aᵀx_b/d` may be singular. No smallest eigenvalue or angle assumption. |
| Labels | Arbitrary real labels with `|y_a|<=Y`, including zero. No binary-label restriction. |
| Loss | `L_n=Σ_a ω_a(f_n,a-y_a)^2`, with each `ω_a>0` and `Σ_aω_a=1`. This is a declared change from the older summed loss. |
| Activations | Different functions at different layers are allowed. Each is globally `C^1`, has bounded derivative, and that derivative is globally Lipschitz. Common bounds are `|φ^(ℓ)(0)|<=D0`, `||φ^(ℓ)'||∞<=D1`, `Lip(φ^(ℓ)')<=D2`. Values may grow linearly and need not be bounded. Constant and affine activations are admitted for existence. |
| Examples actually checked in the proof | Arctan, tanh, logistic sigmoid, softplus, exact GELU, SiLU and the piecewise quadratic smoothing `0` for `t<=0`, `t²/2` for `0<=t<=1`, `t−1/2` for `t>=1`. ReLU itself is excluded. No oddness, analyticity, monotonicity or derivative lower bound is required. |
| First weights | Principal version: iid `N(0,σ_1²)`, using `z_a^(1)=W^(1)x_a/sqrt(d)`. Extension: iid centered subGaussian scalar entries with fixed bound. This normalization puts the `1/sqrt(d)` in the forward map rather than in the stored weights. |
| Middle weights | Independent Gaussian matrices, entries `N(0,σ_ℓ²/n)`, `2<=ℓ<=L`. All initialization groups are independent. |
| Stored readout | Independent iid entries from **any fixed subGaussian scalar law**; it need not be centered or vanish. This includes zero, bounded, noncentered and order-one Gaussian readout. The moment bound is `sup_(p>=2)||W_0^(L+1)||_p/sqrt(p)<=B_out`. |
| Scale degeneracies | Zero Gaussian scales and nonnegative finite learning multipliers `κ_ℓ>=0`, including frozen blocks, are permitted for existence. The activity theorem has stronger conditions. |
| GD and clock | Full-batch GD with stored learning rates `η_n(nκ_1,κ_2,…,κ_L,nκ_(L+1))`; physical time `t=kη_n`; linearly interpolate the stored parameters and recompute features. **Every positive sequence `η_n→0` is covered**, without any further relation to width. |
| Existence interval | `T_*>0` depends only on depth and common input, label, activation, initialization and learning bounds. It is independent of `n,η_n,m,d` and of small Gram eigenvalues/angles under those bounds. Nevertheless `m,d` and the dataset stay fixed in the convergence assertion. |

For the original uniform summed loss, the summed-loss path at time `t` is the averaged-loss path at time `mt`, so the interval furnished by a common averaged-loss time `T_*` is `T_*/m` in summed-loss physical time at the same multipliers. A sample-count-independent time must not be attached to the unnormalized summed-loss dynamics.

The finite readout is always the **stored rescaled vector**, with

`f_n,a=(W^(L+1))ᵀh_a^(L)/n`.

The source's exact updates, including all factors, are at main-proof lines 79–93. Each middle update is a normalized rank-one sum `−(2η_nκ_ℓ/n)Σ_bω_b r_b δ_b^(ℓ)(h_b^(ℓ−1))ᵀ`. The backpropagation fields omit the loss derivative and retain the transpose of the very same trained matrix.

The theorem asserts jointly on `[0,T_*]`:

1. A unique strong autonomous population flow. Its first-layer fields and readout are continuous in `L²`; middle maps are continuous bounded operators in operator norm; their actual adjoints are retained. The integral equations hold in those norms.
2. Uniform-in-time convergence in probability of predictions, loss, and every entry of all layer kernel blocks and the physical kernel.
3. Separately in each neuron population, convergence of the joint `m`-input hidden preactivation and activation path laws in `W₂` for the uniform path norm, including second moments.
4. Convergence of integrated squared hidden speeds and of fixed finite, correctly typed forward/adjoint probes assembled from Lipschitz coordinate maps, linear combinations, and a bounded continuous factor times an `L²` field, with continuous quadratic-growth joint measurements.

This is explicitly the simultaneous `n→∞, η_n→0` **actual GD to population GF** theorem. The source's enumerated statement and its later exposition appendix do not separately formulate a finite-width-GF-to-population theorem, so this audit does not silently add that claim. Main-proof lines 231–238 and appendix lines 84–106 explicitly give the same first-exit bound for finite vectors/integral solutions. The general localization estimate (8) is also available, but the actual comparison (12), restated at appendix lines 680–704, is expressly for GD's assigned fine-grid velocities versus the coarse proxy. Using a finite integral solution in that comparison would remove the fine-grid error; that is a short further deduction, not a separately recorded, independently reviewed convergence assertion. It also does not assert an operator-norm distance from an `n×n` matrix to an infinite-population operator: finite/proxy comparisons occur at the same width, and population comparisons occur on common population spaces.

The state has finitely many field/operator types but infinitely many scalar degrees of freedom. Autonomy and restart use the current full state on the remaining constructed interval; neither finite scalar closure nor a new guaranteed interval of length `T_*` at each endpoint follows.

The kernel identity, main proof around lines 405–419, is

`K^(1)_ab=G_ab E[δ_a^(1)δ_b^(1)]`,

`K^(ℓ)_ab=E[H_a^(ℓ−1)H_b^(ℓ−1)] E[δ_a^(ℓ)δ_b^(ℓ)]` for `2<=ℓ<=L`,

`K^(L+1)_ab=E[H_a^(L)H_b^(L)]`, `K=Σ_ℓκ_ℓK^(ℓ)`.

Thus `ḟ=−2KΩ(f−y)` and `L̇=−4(Ω(f−y))ᵀKΩ(f−y)`. These identities do not make every individual prediction monotone.

## G-P2: admitted loss and initialization extensions

These are proved corollaries within the same accepted theorem, not unattached speculative proposals. See main proof lines 454–497.

For separable loss `Σ_aω_a ℓ_a(f_a)`, each `ℓ_a` is `C¹` with derivative locally Lipschitz, and the derivatives have common finite bounds and Lipschitz constants on bounded prediction intervals. Replace `2r_a` by `ℓ'_a(f_a)` everywhere. Convexity and a global growth restriction are not required on this short interval. The time constant now also depends on these local loss-derivative bounds. The separate strict-activity result is for squared loss, not every admitted separable loss.

The initialization can be perturbed by quantities going to zero in probability in

`max_a ||z_0,a^(1)−z_ref,0,a^(1)||₂/sqrt(n) + Σ_(ℓ=2)^L ||W_0^(ℓ)−W_ref,0^(ℓ)||op + ||W_0^(L+1)−W_ref,0^(L+1)||₂/sqrt(n)`.

Vanishing changes of the learning multipliers are also allowed. In particular, zero population readout permits `σ_out n^(−β)g` for **every `β>0`**, and in fact any readout perturbation whose empirical RMS tends to zero in probability, even if a coordinatewise maximum does not. The independent fixed subGaussian readout theorem is stronger in a different direction: it also allows a nonvanishing law. None of this is universality for an order-one replacement of the Gaussian middle matrices by a non-Gaussian ensemble.

## G-P3: strict activity for two hidden layers, every fixed finite sample count

Primary authority: main-proof lines 499–519; the full [weighted activity audit](GENERALIZE_PRIMARY/ACTIVITY_SOURCE_AUDIT.md); the exact preserved 373-line [source activity note](GENERALIZE_PRIMARY/sources/GENERAL_ACTIVATION_ACTIVITY.md). The source activity note alone is conditional on existence; the accepted main theorem supplies that existence in its `C¹,¹` class. The standalone conditional activity algebra actually needs only nonaffine `C¹` activations with bounded continuous derivatives. These two scopes must not be conflated.

For the assembled unconditional activity corollary require:

- **`L=2`**, weighted squared loss, both activations nonaffine within the accepted bounded-derivative `C¹,¹` class.
- Gaussian first weights, independent Gaussian middle weights, **zero limiting readout**, `σ_1,σ_2>0` and all three `κ` values positive.
- Arbitrary fixed finite `m,d`, normalized `||x_a||²=d`, and pairwise nonparallel inputs: `|G_ab|<1` for `a≠b`. A singular input Gram is still allowed. The single-input case is included directly.
- **Every individual label is nonzero**, with arbitrary real signs and magnitudes. Positive normalized weights remain in force.

For each input and each of the two layers, on a possibly smaller fixed positive interval, the RMS preactivation **and activation** displacement has a strictly positive leading `t²` coefficient, and its RMS speed has a strictly positive leading `t` coefficient. Consequently mean-square displacement is order `t⁴` and integrated squared speed is order `T³`. Hidden initial speeds vanish at `t=0`; they are positive for each sufficiently small fixed positive time.

The middle matrix changes when applied to **each** initial first-layer feature. All three kernel blocks are positive definite at sufficiently small positive time and each is nonconstant; the physical kernel is nonconstant. The first two blocks are zero at initialization, while the readout block is already positive definite. Loss has uniformly strictly negative slope on a small interval. Every hidden marginal retains positive variance and a positive best-affine-fit error for its activation. This does not assert that trained hidden laws remain Gaussian, every kernel entry increases, or every residual magnitude decreases.

The weighted onset algebra uses `p_a=ω_a y_a`, and `S=Σ_a p_a φ^(2)(Y_a)`. In particular `−L̇(0)=4κ_3E[S²]>0`. For each fixed dataset, the positive coefficients and the activity interval may depend on its geometry and labels. They are not uniform as inputs approach parallelism or labels approach zero.

The audited positivity proof is substantive: finite-difference ridge independence gives a positive first feature Gram even when the input Gram is singular; nonaffinity and full Gaussian support give a positive Gram for `Sφ^(2)'(Y_a)` despite activation flat intervals. Reusing the transpose introduces its correct deterministic response **plus independent covariance `σ_2² V`**, without subtracting the finite-forward projection covariance. The next reused forward call has fresh nonzero Gaussian variance, preventing cancellation of each second-layer leading motion. This is not a shortcut that replaces the transpose by an independent matrix.

Strict activity at arbitrary depth or with nonzero limiting readout remains unproved by this task. The broad existence theorem does not transfer its full scope automatically to this corollary.

## Why the general theorem is more than the older draft

The [two-layer response audit](GENERALIZE_PRIMARY/TWO_LAYER_RESPONSE_AUDIT.md), read in full, proves a useful narrower `C²` response lemma. Its concluding exclusions of arbitrary depth and `C¹,¹` concern that lemma alone. They are superseded for existence by the full depth response proof and the mollification passage in the accepted main proof. Likewise the handoff's `GENERAL_DEPTH_LIMIT_CHECK.md` was a bounded-activation draft, explicitly unreviewed at handoff; the later completed result supersedes it.

The accepted proof preserves an individual backward-source perturbation's factor `Δω_b` through later response propagation. It bounds weighted time sums using marginal subGaussian estimates and Jensen, without taking a maximum over an increasingly fine Gaussian history or assuming independent times. Response caps are selected forward through depth and backward through depth at zero time, then a positive time is chosen last; the source checks the causal construction order explicitly.

Localization of the unbounded backward multipliers yields a comparison coefficient linear in the cutoff `R`, not `R^L`. The resulting bound has the structure

`C exp(C(1+R)T_*) [(1+R)(η_n+Δ) + exp(−cR²) + o_P(1)]`.

A finite-rank-memory proxy with deterministic population residuals/contractions is used only inside the proof. The actual network always trains with its actual predictions. Width tends to infinity at fixed `R,Δ`, then `Δ→0`, then `R→∞`; the mollification passage inserts `ε→0` before the cutoff is removed. Gaussian tails defeat the Gronwall amplification. This is how the theorem removes a width-dependent step restriction; a fixed-computation tensor-program limit alone would not establish it.

Relative to the older Explain task, this establishes a broader positive-time theorem at every fixed depth, all fixed finite sample counts, many unbounded activations, more general labels and initialization, and every vanishing step. It does **not** supersede the older one-sample L2 all-finite-horizon atan theorem's stronger time quantifier. Nor does it turn the earlier one-sample L3 global finite-GF/GD optimization theorem into a global population convergence theorem.

## Distinct boundaries and negative examples

The following are scoped obstructions or excluded cases, not refutations of the accepted theorem:

| Finding | Meaning |
|---|---|
| ReLU's derivative jumps | The proved uniform mollification passage in `φ` and `φ'` does not cover ReLU. This is an open extension, not a no-go theorem. |
| Non-Gaussian middle matrices | The proof uses the Gaussian matrix/reused-transpose law. Order-one middle-ensemble universality is not established. Small operator-norm perturbations are a different admitted claim. |
| Growing `m,d,L`, all time | No convergence rate or existence statement permitting these limits is established. Uniform time under common bounds for separately fixed data does not give a growing-data theorem. |
| Broad second-moment product algebra | Arbitrary products of two unbounded `L²` fields are outside the measurement assertion. The actual proved probe class uses bounded continuous multipliers. |
| Nonparallelity/label degeneracy in activity | Identical inputs with opposite labels can have `S=0` and a frozen zero-readout flow. Antiparallel inputs with odd activations and equal labels can do the same. Zero labels can invalidate per-input onset for an orthogonal decoupled input. These inputs are still allowed by the existence theorem. |
| Affine/constant activations in activity | Constant activations kill relevant derivatives; an affine first layer can give a singular feature Gram, and an affine second activation gives a rank-at-most-one derivative Gram for multiple inputs. Existence still applies; the complete activity bundle need not. |
| SubGaussian first roots in activity | A general discrete root law can miss a derivative's support. The broad first-weight existence extension alone does not prove the Gaussian full-support activity argument. |

No review in this package identifies a surviving blocking gap in G-P1–G-P3 under the final stated hypotheses. This is a report of completed mathematical reviews, not proof-assistant verification or a new independent proof certification by this audit.

## Later reconstruction discussion: conditional positive and logical obstruction

The second task turn adds a distinct **conditional finite-ODE approximation implication**, with complete source and independent audit read here: [Borel hypothesis and local implications](GENERALIZE_PRIMARY/BOREL_HYPOTHESIS_AND_LOCAL_IMPLICATIONS.md) and [identification audit](GENERALIZE_PRIMARY/BOREL_IDENTIFICATION_AUDIT.md).

For one sample, a nonzero initial residual and positive initial kernel supply a fixed interval where the initialized prediction is strictly monotone. Hence that single initialized trajectory admits an output-coordinate kernel `κ(f(t))=K(t)` and scalar equation `ḟ=2(y−f)κ(f)`. This is restriction to one orbit, not a universal assertion that arbitrary states having equal prediction have equal kernel.

**Conditional positive G-C1:** if a declared initialization-only finite-jet reconstruction uniformly approximates the **actual** orbit kernel on the needed output interval, then its finite scalar ODE uniformly approximates prediction and loss on a fixed time interval, with error proportional to kernel error and an explicit time margin. For a proposed fixed-multiple-input extension, if

`δ_N=sup_(t<=T)||Ω^(1/2)(K_N(t)−K(t))Ω^(1/2)||op→0`,

then its known-coefficient prediction equation gives weighted prediction error at most `(exp(2δ_NT)−1)sqrt(L(0))` and loss error at most `(exp(4δ_NT)−1)L(0)`, with no positive minimum kernel eigenvalue needed. A finite clock variable can make that time-dependent approximation autonomous. Composing with G-P1 gives `o_P(1)+ε` actual-GD prediction error after fixing an accuracy-dependent finite approximation. The matrix reconstruction premise is a proposed extension of the earlier one-sample conjecture, not an established neural reconstruction theorem.

**Logical obstruction G-N1:** existence/uniqueness, a convergent formal Borel transform, or matching all initialization derivatives does not identify a resummation with the actual trajectory. The source gives the smooth globally Lipschitz scalar ODE `x'=1+g(x)`, `x(0)=0`, where `g(x)=exp(−1/x²)` for `x>0` and zero otherwise. Its actual solution exceeds `t` for positive time while its entire Taylor series is `t`. This is an explicit ordinary-ODE example, **not a neural counterexample**. Full-state uniqueness is useful only after proving the reconstruction solves the same strong integral equations. The broad `C¹,¹` GF theorem does not even assume all-order jets, let alone Gevrey bounds, analytic continuation or Borel identification.

The third and fourth turns discuss standard sufficient Padé/Stieltjes/analytic-domain conditions for finite-jet approximation, not their verification for this neural GF. These notes were archived as contextual sources; their mathematical proof details were not independently re-audited here. The full later `BOREL_PDF_ACCURACY_REVIEW.md` was also read in this final scope check: it gives an independent final mathematical PASS after checking the source notes and written appendices, explicitly covering the scalar conditional error, matrix error without a positive minimum eigenvalue, and actual-network quantifier order (items 4–6). This is an accuracy review of the written conditional conclusions, not three fresh exact-hash proof certifications and not a proof of neural reconstructibility. It preserves the distinction between these conditional approximation results and the accepted GF theorem. No all-time neural reconstruction or exact finite scalar state theorem was established by those later turns.

## Independent review and exact accepted versions

All three fresh reviewers read the complete main/depth proofs without their derivation history or another reviewer's verdict. Each returned PASS, with no required mathematical repair. They checked the relevant primary Tensor Programs III and IVb sources; the full reviews were read here, including their hypothesis checks and scope limitations.

| Reviewer | Preserved report | What its PASS covers |
|---|---|---|
| A | [INDEPENDENT_REVIEW_A.md](GENERALIZE_PRIMARY/INDEPENDENT_REVIEW_A.md) | Fixed-depth joint vanishing-step theorem, response and Gaussian source hypotheses, local time, arbitrary vanishing step and stated measurements. |
| B | [INDEPENDENT_REVIEW_B.md](GENERALIZE_PRIMARY/INDEPENDENT_REVIEW_B.md) | Full theorem, response, proxy and interpolation bridge, mollification, hidden paths/speeds/probes, fixed-data versus uniform-time distinction. |
| C | [INDEPENDENT_REVIEW_C.md](GENERALIZE_PRIMARY/INDEPENDENT_REVIEW_C.md) | Full theorem plus separately scoped Gaussian-initialization, zero-readout L2 activity, with the activity source checked rather than trusting its verdict. |

The [final manifest](GENERALIZE_PRIMARY/FINAL_SHA256SUMS.txt) has **10 files; all 10 hashes match**. The main proof's final hash is `5406c9e3a812127be623d22e225ac545e83bc8ea1010b5046bd4bab6a295514d`. All reviewers recorded the earlier main hash `792dbd8eca426dc8fd5434d67b183826025a7a301f42fd579d6332fa458005e2`.

That discrepancy is fully resolved, not merely accepted from a summary. The exact final patch survives in the first exported turn, item `exec-4e92d2d8-667e-40b7-9ad6-92410a460cce`. Reversing its two changes reconstructs [the reviewed main manuscript](GENERALIZE_PRIMARY/GENERAL_POPULATION_GF_PROOF_REVIEWED.md), whose SHA-256 **exactly matches all three reviewers**. The [recorded diff](GENERALIZE_FINAL_VS_REVIEWED.diff) changes only the status paragraph and explicitly repeats “Gaussian first weights” in the activity corollary. There is no post-review broadening of the theorem. The final response and activity proof hashes are unchanged from review.

The activity source copy also matches reviewer C's hash `c6bfa76ac200ce59f91109b31a40d22d668ec678e2ea60386f93f7d7604b4e89`. See [hash checks](GENERALIZE_HASH_CHECK.json), [copy provenance](GENERALIZE_COPY_PROVENANCE.json), [review record](GENERALIZE_PRIMARY/REVIEW_RECORD.md), and [research state](GENERALIZE_PRIMARY/RESEARCH_STATE.md). The reconstructed reviewed file is labelled as recovered from the recorded patch; all other archived source copies are byte-for-byte copies of accessible source files.

## Chronology and complete-source coverage ledger

| Chronological turn | Turn id | Substance and disposition |
|---|---|---|
| 1 | `01a07193-3f18-7350-a8b4-ce5d609eeef0` | Supervisor handoff; older generalization draft explicitly pending; source identities verified; complete two-layer, depth and activity work written; main proof completed; three fresh reviews; final exact-hash acceptance and broad theorem delivered. Primary accepted mathematical result. |
| 2 | `01a072bc-1d4d-7442-82fa-f3a81eb9c580` | Recovered one-sample Borel conjecture, its local conditional finite-ODE implication, proposed matrix extension and surviving identification obstruction. Complete final and two main source/audit notes read. |
| 3 | `01a07723-7095-70d1-b1bd-06fe98f82e4d` | Padé/Stieltjes and Borel approximation sufficient conditions; actual-neural identification left open. Complete final read; contextual notes archived, not added as an unconditional neural theorem. |
| 4 | `01a0772e-7f31-7532-a4b5-551fcf347ed7` | Same Padé exposition reformatted for phone equation rendering; no new theorem scope. Complete final read. |
| 5 | `01a07735-4d9a-7833-8886-51d058326b26` | Ten-page GF exposition plus technical appendix, with accuracy/readability review and repairs. Complete final and both preserved review notes read; no broader GF assertion. |
| 6 | `01a0773f-2111-7eb3-ac58-167a40ceee7e` | Combined-PDF link only; no mathematical addition. |
| 7 | `01a07742-8a2c-7071-bc38-90aa9e51f182` | Borel/Padé/Stieltjes added as conditional appendices, producing 34 pages. Final read; appendix review records archived. No neural Borel reconstruction proved. |
| 8 | `01a07750-5879-79a0-9ef0-afcd043ea8db` | Private PDF download publication for phone/airplane access. Final and intervening user requests read; delivery logistics only. |

| Source family | Full-read coverage in this audit | Role |
|---|---|---|
| `GENERAL_POPULATION_GF_PROOF.md`, 524 lines | Entire final manuscript; reviewed version independently reconstructed and hash-checked | Theorem, actual-GD bridge, strong flow, observables, extensions. |
| `GENERAL_DEPTH_RESPONSE_PROOF.md`, 540 lines | Entire manuscript | Necessary mesh-uniform response/tail estimate at every fixed depth. |
| `TWO_LAYER_RESPONSE_AUDIT.md`, 300 lines | Entire manuscript | Narrower supporting proof; its depth exclusions are not current main-theorem exclusions. |
| `ACTIVITY_SOURCE_AUDIT.md`, 206 lines | Entire manuscript | Weighted strict-activity and matrix-reuse source audit. |
| `sources/GENERAL_ACTIVATION_ACTIVITY.md`, 373 lines | Entire manuscript and reviewer hash checked | Original conditional positivity proof; completed by main existence theorem under intersected assumptions. |
| `INDEPENDENT_REVIEW_A/B/C.md` | All three complete reports | Final mathematical acceptance and scoped hypotheses. |
| `GF_RESULT.md`, `REVIEW_RECORD.md`, `RESEARCH_STATE.md`, `FINAL_SHA256SUMS.txt` | Entire files; all manifest hashes checked | Index/status and exact provenance, subordinate to proofs. |
| `BOREL_HYPOTHESIS_AND_LOCAL_IMPLICATIONS.md`, `BOREL_IDENTIFICATION_AUDIT.md` | Entire two notes | Conditional reconstruction and distinct logical negative result. |
| `GF_EXPOSITION_MATH_REVIEW.md`, `GF_MAIN_READABILITY_REVIEW.md` | Entire reports | Later exposition preserves original scope; repaired overbroad matrix-convergence wording. |
| Three-input baseline proof/review in `sources/` | Archived byte-for-byte; used as inherited dependencies, not freshly read in full by this sub-audit | Dedicated predecessor audit covers the baseline; the completed general theorem was read directly. |
| `BOREL_PDF_ACCURACY_REVIEW.md` | Entire report read during final consolidation scope check | Independent final PASS explicitly includes scalar/matrix conditional error transfer and actual-network consequence; no neural reconstruction premise is certified. |
| Padé/Borel transfer, Stieltjes and analytic-guarantee notes; Borel-PDF readability review | Archived; final-turn claims assessed, detailed proofs outside this bounded GF evidence audit | Conditional generic approximation results, not additional established neural dynamics. |

All requested accepted Generalize proof/review artifacts were accessible and preserved. No missing primary source blocks G-P1–G-P3. No exact-id local rollout for this host's Generalize task was found under the local sessions directory, so chronology coverage is stated as the complete eight-turn app export, not an unsupported guarantee that no unexposed remote continuation exists.
