# Independent compact-paper preaudit C

Date: 2026-10-09. Review form: the assigned single-report mathematical audit; no venue score or publication recommendation. This review concerns the five frozen inputs below, not another manuscript version.

## Assessment

I found no demonstrated major or fatal mathematical flaw in the supplied argument. The headline conclusions follow from the displayed modular chain at the resolution of this audit. In particular, I found no use of positivity for a complex Gram matrix, no conditional Gaussian claim applied after substituting adaptive controls, no growing-deletion moment argument, and no uncharged dense coefficient table in the selected runtime.

There is one minor wording correction, L1: the activated last-layer feature vectors are generally not Gaussian. The proof immediately following that sentence treats their nonlinear row products correctly, so this does not invalidate the fluctuation lemma or the headline comparison.

Confidence is moderately high for the finite-dimensional algebra, fitting, approximation/counting, and fluctuation arguments, and moderate for the much longer shared cavity/source argument. I read and reconstructed the latter's logical chain and its critical normalization, stopping, entropy, and trace steps. I did not formally verify every generous constant such as the individual remainder envelope with exponent `240L`, or independently implement the entire cavity construction. Numerical checks below are diagnostics, not substitutes for those proofs. No claim here establishes novelty, practical preprocessing, finite-precision behavior, or a useful finite width threshold.

## Isolation, inputs, and complete reading coverage

I read only the assigned scientific inputs and required skill/rubric instructions. I did not read the original manuscript, study README/history, author notes, earlier reviews, other studies, Git history, or other reviewer findings. The task-specific assignment replaces the general review artifact template and author startup. I read the complete rigorous-mathematics skill, canonical-notation skill and neural-network reference, and AI-paper-review skill and severity rubric.

All 3,553 source lines were read, including every proof body. An initially truncated tool display was remedied by rereading the affected foundations range. The source ranges read to completion were:

| Input | Complete coverage | SHA-256 |
|---|---:|---|
| `paper/compact.tex` | 1–257 | `64327f17c0a47b08a349890d274960b9732c8d650b2730e02a4d44d3e88fa6f9` |
| `paper/compact_fitting.tex` | 1–213 | `4cb10d4534f95ca5dbc9a957aac536c55a7268e0dc7128c105102de5bd195235` |
| `paper/compact_foundations.tex` | 1–1377 | `8de151e32734ee2c9116a91a1cccb7c5ecee7ec1369ff4784e88fb4d79a6148a` |
| `paper/compact_legendre.tex` | 1–699 | `45c40b7e6c1c1b501d6f2643a226ac2ca4a00a91e3d9704502ed54fadf4fe238` |
| `paper/compact_selected.tex` | 1–1007 | `12b2d33bf7732172d454cf3a2d74a4b322f027a74474d8747f3da9ef85b96c11` |

Hashes were checked at both the start and end and agreed. The generated PDF was used only as a compilation artifact; scientific reading was of the full TeX sources. I made no paper edits.

## Claim-level reconstruction

### 1. Fitting and shared analytic sources

Plausibility: highly plausible. Argument verdict: no material gap found in the checked chain; confidence in the long local-remainder portion is qualified above.

The deterministic fitting proof in `compact_fitting.tex:119–177` has the correct mobility norm. In that norm, the loss derivative is the negative squared parameter speed, and the readout Gram gap alone supplies the lower speed bound. Its weighted Cauchy–Schwarz estimate yields finite parameter length rather than merely residual decay. The stronger quadratic hidden displacement, together with the small-label cap, preserves the feature and Gram margins. Uniform initial cavity fitting is transferred by zero extension and feature/operator comparison, rather than by an unjustified union over only qualitative concentration statements (`:100–117`). The signed comparison identity at `:201–212` preserves the negative prediction-error square; its coefficient is exactly bounded by `K(3 rho + rho')`.

The shared source proof distinguishes three different roles that must not be merged:

1. Independently stopped cavity coefficients depend only on retained initialization (`compact_foundations.tex:254–298`). Their separately clipped extensions retain that independence.
2. For each frozen deterministic scalar control history, insertion maps are linear Gaussian images and root re-pairings are quadratic Gaussian forms. The uniform event is constructed before actual adaptive controls are substituted (`:599–677`). The manuscript explicitly declines to infer Gaussianity or centering after substitution.
3. Nonzero same-root contractions are preserved as traces and absorbed using the residual activity and Schatten estimates (`:683–801`). The direct external trace retains the evaluated sample's amplitude; the integrated terms use driving-sample RMS. This avoids an extra sample factor or a false centering argument.

I checked the exponent separation in the uniform control event: a control mesh of scale `n^(-1/8)` with speed `sqrt(n) poly(log n)` has logarithmic cardinality `n^(5/8) poly(log n)`, while a centered quadratic form at threshold `n^(-1/10)` with operator size `n^(1/200)` has a tail exponent eventually at least `n^.78`. The claimed `n^.65` entropy and `n^.7` failure envelope leave genuine asymptotic margins. The nonlinear closing exponents also separate: with `N=n^.01`, `d0=n^(-.1)`, and `u0=n^(-.04)`, the worst displayed term after multiplication by `n^(1/4000)` remains `o(u0)` (`:656–678`). These checks concern the stated envelopes; they do not replace all the intervening differentiated recurrence estimates.

The normalized Schatten trace arguments use neuron normalization `n`, not the much larger parameter-space dimension (`:725–760`). In the exponential-moment step the deletion count/moment order is fixed before the width limit. The final infimum over integer moment orders is taken afterward (`:1046–1079`), so no estimate uniform in a growing cavity size is claimed. Repeated-root tuples have vanishing normalized multiplicity even after their `n^{o(1)}` cost.

The complex-domain arguments do not use real positivity off the real axis. On the short rectangle they use operator-norm growth (`:1095–1104`). On a vertical part of the flaring domain they freeze the real symmetric generator; multiplication by `i` then gives a unitary base evolution. Its perturbation is bounded by a double residual integral (`:1287–1325`). The identity defining `h(t)` gives the displayed residual integral and makes the perturbation gate tend to zero. The clipped reference correction radii tend to zero even with `B_n=O(log log n)`, as required for the complete-path Gaussian moments.

The all-time carrier extension uses deterministic real tail length after the finite complex horizon (`:1182–1204`); it does not claim unproved late-time complex analyticity. This is enough for the Legendre comparison.

### 2. Legendre compression

Plausibility: highly plausible. Argument verdict: sound in the checked scope, conditional on the shared carrier/source result.

The model stores actual history moments, uses the activity clock starting at one, and reconstructs the learned hidden weights from their projected bilinear pairing (`compact_legendre.tex:10–58`). The zero backward prefix and initialized constant forward prefix match the moment initialization. The stored ODE itself never divides by a residual.

The decisive defect is a product of two projection endpoint errors, not an arbitrary first-order history error (`:133–157`). Differentiating a growing-interval least-squares projection gives the squared endpoint error because its interior derivative is still in the polynomial space. Both this identity and the bilinear version have the correct signs and normalization. The order-independent fitting argument uses the `sqrt(q)` endpoint operator estimate together with the `1/sqrt(q)` forward endpoint tail; this removes `q` from its pointwise forcing bound (`:200–277`).

The signed comparison uses the actual dense carrier bound only once, additively in the Jacobian coefficient (`:316–362`). Gate subtraction is anchored at the dense carrier; the proof does not assume coordinate bounds for the closure's own carriers. The backward history is compared at the closure clock while its normalized residual remains the closure residual. Freezing after `t_q` and using `A-tau(t) <= rho_hat(t)/kappa` cancels the apparent inverse-clock singularity (`:433–458`). The resulting forcing is quadratic in projection order after absorption (`:460–487`).

The prescribed order exceeds the `n^{o(1)}` absorption threshold and gives the stated `Y/(sqrt(n) log^3(en))` error (`:490–502`). The count explicitly retains the fixed dense mixers separately. The `nd` term is absorbed only eventually for fixed input dimension, consistently with the headline quantifiers.

### 3. Actual dense-run variability

Plausibility: highly plausible. Argument verdict: sound, with wording correction L1.

The innovation lemma does not need nonsingular previous-layer covariance. It uses the strictly positive *top feature* Gram and the area inequality for the random vector `U(U^T y)` (`compact_legendre.tex:520–552`). Its two spectral lower bounds multiply to produce the stated `gamma^3` scale; equal feature diagonal moments give the stated `mu_2/mu_4` factor. This remains meaningful for affine activations and singular intermediate covariances allowed by the setup.

Conditioning on both lower-layer initializations leaves independent top-layer innovations. Conditional variances and third moments converge by continuity of Gaussian covariance square roots and linear activation growth. The conditional centered characteristic-function argument is scalar and gives uniform conditional CDF convergence in probability. An arbitrary random conditional-mean shift can only lower the maximal centered Gaussian small-ball probability (`:569–618`). Therefore earlier layers cannot cancel this source of independent-run fluctuation in the manner excluded by the proof.

The derivative-to-trajectory transfer uses a Chebyshev truncation and the endpoint polynomial derivative bound; it is valid for complex coefficients (`:633–650`). The explicit finite-query analytic radius and `N=O(log n)` produce the `log^(5/2)(en)` denominator. The confidence choice leaves a strict limiting margin before converting it to an eventual finite-width statement (`:671–698`). The witness is a positive time at a training input, and the argument does not falsely demand endpoint variability after both runs fit.

### 4. Selected nonlinear runtime and its correction

Plausibility: highly plausible. Argument verdict: sound in the checked scope, conditional on the source contract.

The sparsification proof preserves a real exact source metric, not just an approximate coordinate norm (`compact_selected.tex:35–92`). The formula for `M` gives `P^T M P=I`, `D/4 <= M <= D`, and the constant-source mass bound. Its use with different layer dimensions is valid. The gate operator need not be self-adjoint in `M`; the paper explicitly uses it as a prescribed multiplication operator and charges the factor two in its norm.

The corrected readout enforces the training deficit identity exactly. Expanding all cross-sample terms in the prescribed parameter velocities recovers the stated selected energy identity even when layer metrics are non-diagonal (`:194–232`). Consequently the fitting proof does not rely on a false gradient interpretation of that corrected predictor.

The runtime comparison constructs a restricted dense reference whose feature symbols are restricted dense values, not a recomputed forward pass (`:356–392`). The initialized forward/reverse source pairing and outer-product pair defects account for that discrepancy. Source approximation errors are used only as values, never differentiated.

For `p=T_C e` and `zeta=z_w+p`, the readout terms `2 V_C e` cancel exactly because `T_C Q_C=V_C` (`:427–470`). In the `p` energy, the `Q_C` contribution is `-2 ||e||^2`. The remaining hidden-Gram contribution is bounded using the small-label cap, leaving dissipation; it is not simply discarded as positive. The resulting integral bound controls the hidden discrepancy and avoids a sample/gap factor in the exponent (`:472–569`). The endpoint extension compares each real trajectory with its own value at the finite horizon and uses convergent readout/feature limits.

### 5. Initialization-only provenance and retained counts

Plausibility: highly plausible. Argument verdict: sound in the stated exact-arithmetic/existence setting.

The origin-jet compiler gives an explicit conformal time map, verifies its range, and obtains uniform truncation error from boundedness on a disk (`compact_selected.tex:588–647`). This supplies finite later-anchor derivatives or integral coefficient approximations from finitely many origin derivatives. It is an existence proof with potentially enormous work and precision, exactly as disclosed. Paired initialized images are formed with the actual initialized matrix, so finite coefficient errors do not silently destroy image pairing (`:660–670`).

The whole-sphere harmonic proof supplies the spatial exponential decay, including separate treatment of `d=1` and `d=2`, and then counts a weighted simplex of time/spatial indices (`:704–801`). The exact time-radius calculation retains the `z^2` factor before squaring for storage. The dimension-dependent factorial estimate then gives the displayed `(C/d)^(d+1)` factor, with fixed `d` absorbed only into the width threshold where expressly stated (`:835–885`).

The panel construction uses a *single fixed span* of all local Taylor coefficient vectors, rather than retaining a runtime forcing schedule. Boundary matching is unnecessary because the transfer estimate only uses approximation values. Input-span reduction is exact, respects the original Gaussian covariance and training normalization, and justifies its separate `(m+p)d` storage term (`:924–1005`). The runtime inventory includes metrics, inverse caches, selected mixers, initial copies, training arrays, data, and query workspace. The extra panel term `log^2(n) log^2 log(n)` is consistent with the fixed-problem `O(log^3 n)` statement in the abstract.

Finally, the assembly at `compact.tex:223–254` uses a union bound, not independence between approximation and fluctuation events. For each fixed positive tolerance the limiting failure probability is bounded by an arbitrary confidence budget. Letting that budget decrease proves convergence in probability with the paper's failure convention.

## Concern and severity triage

### L1 — nonlinear feature rows called Gaussian

- Location: `paper/compact_legendre.tex:569–584`, specifically lines 572–573.
- Affected result: conditional scalar fluctuation lemma.
- Evidence: conditional on lower layers, the preactivation row is Gaussian; its componentwise image under a nonlinear activation generally is not. For example, `phi(z)=tanh(z)` gives bounded non-Gaussian coordinates. The manuscript's sentence calls the rows “independent Gaussian feature vectors.”
- Severity: minor point. This is localized wording; the rest of the proof explicitly works with nonlinear products `U_a(U^T y)`, uses Gaussian inputs only to establish their moments and continuity, and applies a scalar CLT to those products. No nontrivial proof restructuring is needed.
- Cascade: none after correction; the fluctuation lower bound and the three relative-error conclusions survive.
- Repair: replace the sentence by “Conditionally on the lower layers, the last-layer preactivation rows are independent Gaussian vectors; applying the activation gives independent feature vectors, and the two runs remain conditionally independent.”

No fatal or major concern is assigned. I found no substantive missing definition or broken cross-reference that prevents reconstructing a headline claim. External novelty and bibliographic completeness were outside this isolated frozen-input audit; no literature comparison is implied.

## Executed verification

Artifact-location note added by the lead after this audit: the diagnostic source
now lives at `studies/compact_paper_20261009/PREAUDIT_C_CHECKS.py`; the generated
build/scratch directory was moved intact to
`data/generated/compact_paper_20261009/preaudit_c_Mkp7sP/` to follow the repository
layout. The historical commands and original paths below are retained as run.
No audit conclusion or scientific input was changed by this relocation.

Scratch directory: `/home/amir/Codes/PDE/studies/compact_paper_20261009/audit_c.Mkp7sP`. The independent diagnostic script is `checks.py` there. It contains no manuscript code and writes no scientific outputs.

1. From `/home/amir/Codes/PDE/paper`, ran twice:

   `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/home/amir/Codes/PDE/studies/compact_paper_20261009/audit_c.Mkp7sP compact.tex`

   Both runs returned exit status zero. The second produced a 43-page PDF, 625,692 bytes, using pdfTeX 3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian. Searching its final log for `undefined|multiply defined|Overfull|Warning|Error` returned no matches. Initial first-pass undefined references disappeared on the second pass.

2. Ran `python /home/amir/Codes/PDE/studies/compact_paper_20261009/audit_c.Mkp7sP/checks.py`. The first attempt failed before testing because `mpmath` was unavailable. I replaced that optional dependency with Python's standard `decimal` module at 60-digit precision; no package was installed. The corrected script returned exit status zero, using NumPy 1.26.4.

   - Source coefficient/power and allowance checks: 5,244 inequalities, zero failures, over `beta=10,11,20,100`, depths 2–20, with the adverse scalar bound choices `b=beta-1`, `s=t2=beta`.
   - Exact source-metric formula for dimensions `(n,r)=(11,3),(30,5),(7,7)`: maximum `P^T M P-I` entry magnitude `7.77e-16`; both metric comparisons and constant mass assertions passed.
   - Corrected selected readout with non-diagonal metrics and unequal widths `(q1,q2)=(5,7)`: training identity absolute error `2.46e-11`; energy identity relative error `2.85e-16`. These are floating-point diagnostics, not certified interval errors.
   - Legendre bilinear projection-growth identity for orders 1–5 on independent random polynomial histories: maximum relative centered-difference error `9.93e-10`.
   - Innovation lower bound in the exactly computable Gaussian/linear-activation case: 220 random correlation-matrix cases with sample sizes 2–12; all passed, with smallest ratio of actual maximal row variance to claimed lower bound about 165.
   - Gaussian shifted-interval small-ball inequality: 804 deterministic grid checks passed.
   - Harmonic factorial counting inequality: all integer dimensions 2–100 passed.

These checks target constants and identities that could invalidate the modular assembly. I did not simulate full dense or compressed training, claim numerical reproduction of asymptotic rates, or test practical width/precision requirements.
