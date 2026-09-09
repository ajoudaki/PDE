# Covariant Schur bridge: focused independent recheck

Date: 2026-09-08. Scope: the sharp difference-score multiplier estimate (4.12w7g′) and derivative-closed finite-word synthesis, especially slot order r=2, in `CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md`. This is an adversarial source check of the supplied objection, not a new model-theorem proof search.

## Verdict

**A concrete proof gap remains; the objection is not fully addressed by the manuscript's special-direction discussion.** The arbitrary graph-norm matrix example does not, by itself, falsify the special score-difference lemma: that lemma asserts additional pointwise and row/column bounds specifically for a full-minus-cavity score difference. However:

1. The two inequalities at (4.12w7g′) are the necessary analytic input, not consequences of the displayed algebra alone. Their mixed-derivative norm and the dimension-uniform concentration/restoration estimate are not specified and proved sufficiently to verify them.
2. The later r=2 catalogue explicitly admits pairs from a broader class of responses. Its stated restrictions do not ensure that every unnormalized coordinatewise product has a sharp difference-score factor. The proof of (4.19a4) substitutes a first-order constant squared for precisely the bilinear estimate that needs justification.
3. There is an additional **literal failure in a displayed prerequisite**: the optional-row initial-data estimate (4.15g), on its printed domain, misses the induced initial Z datum. A unit Euclidean row perturbation can give initial local response of size √n/L. Restricting this datum to the regression-residual subspace would exclude the example below, but that restriction is not in the displayed domain, and would still need to be preserved through the catalogue.

Thus the broad printed response/synthesis package cannot be certified as stated. Even granting the natural residual-only interpretation of the optional datum, the intended restricted sharp/synthesis bridge remains **unproved in this source**, not independently established by its historical PASS label. This recheck does **not** disprove the canonical initial-layer theorem itself, or prove that the intended restricted estimates are false.

## 1. Source, coverage, and authority

Primary source: [canonical covariant-Schur manuscript](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:1).

I read **all 3,342 lines**, including all definitions, displayed estimates, their proofs, the reciprocal-clock section, first-exit closure, coarea/spacing argument, release argument, and concluding dependency discussion. Reading was in consecutive, non-truncated blocks: 1–350, 351–700, 701–1040, 1041–1380, 1381–1745, 1746–2115, 2116–2460, 2461–2805, 2806–3090, and 3091–3342. I additionally searched all occurrences of the special mixed-derivative constant, fresh initial data, sharp bounds, and Lipschitz assertions to check for a later definition or missing repair.

Independently computed SHA-256 of the complete local file:

`a1eb606ab73a34476ac5ab8f848c25db681c662d655ac6a90f8099eb5ef24c1c`

The manuscript's opening historical audit refers to a mathematical-body hash `be9d0d95d12bd20f55429c1d57bcf431b7cfcd27885a447ed361a6a4f1587f37`. I did not reconstruct that body snapshot or infer that it equals this complete file. The verdict attaches to the local bytes hashed above. Historical audit statements are not proof evidence.

Full reading is not an end-to-end certification. I checked the algebra, norms, domains, and dependencies bearing on the two assigned bottlenecks. I did not independently certify the integer-arithmetic pole program, the moderate-deviation/coarea estimates, every bath moment assertion, or the post-cap release argument. They are not used to establish the present negative audit finding. I read no other source auditor's report, did not inspect private task rollouts, and did not use the previous linear audit as evidence for this nonlinear bridge.

I reread solve-math-rigorously and investigate-conjectures in full, plus the latter's evidence-ledger and adversarial-audit references. Their distinction between a failed proof bridge and a false model theorem governs this verdict. No experiments, tests, agent actions, source edits, permission changes, or other research mutations were performed. Only this report was written, using apply_patch.

## 2. What is correctly addressed

The canonical variables are A,u,G, with X=u², Z=GX, B=A⊙Z, and R=GᵀB. The feature vector field has component F_A=Z² and matrix component F_G=2BXᵀ/n. Vector norms are normalized by n, while the matrix primitive norm is unnormalized Frobenius. The relevant definitions are [the exact flow](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:27), [primitive metric and Hessian](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:428), and [seven-component tangent/source graph](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:1745).

For a matrix-only direction Y=(0,0,M),

\[
D_GF_A[M]=2Z\odot(MX),\qquad
D_G^2F_A[M,M]=2(MX)^{\odot2}.
\]

Choose a bounded-mark column layer J of positive limiting density and put

\[
M=e_i\frac{(P_JX)^T}{\|P_JX\|_2}.
\]

Then ∥M∥F=1 and MX=∥P_JX∥₂e_i. Consequently

\[
\|MX\|_{2,n}=\frac{\|P_JX\|_2}{\sqrt n}=O(1),\qquad
\|D_G^2F_A[M,M]\|_{2,n}
=\frac{2\|P_JX\|_2^2}{\sqrt n}\asymp\sqrt n.
\]

On ordinary bounded layers, the layer weights only change these statements by fixed or polylogarithmic factors. The seven first-order graph legs do not by themselves supply a pointwise bound on MX. This invalidates a dimension-free bilinear bound on an arbitrary first-order graph-norm ball. It does not contradict the core **first derivative** estimate (4.7f): D²f, used there, is not D²F.

The manuscript explicitly recognizes this distinction [at 1174 onward](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:1174). Its sharp norm (4.12w7a) includes pointwise control of the difference fields and √n-scaled individual matrix-row and matrix-column norms. The concentrated M has a sharp matrix-row contribution of order √n, so it is not a unit special sharp direction.

If (4.12w7b) holds, its intended use is valid. With ζ the full-minus-cavity bath preactivation difference and κ=n^(-1/2+o(1)),

\[
\|D_b^W\zeta\|_{\infty,\mathrm{weighted}}\lesssim\kappa
\quad\Longrightarrow\quad
\|2(D_b^W\zeta)\odot\widehat Z\|_{\mathrm r,D}
\lesssim n^{o(1)}\kappa\|\widehat Z\|_{\mathrm r,D}.
\]

This is a valid multiplier estimate, not an L²-algebra claim. The displayed polarization table [at (4.12w7i′)](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:1438) has that special score factor in its first product. The exact common-clock cancellation (4.12w7d) and the Jacobian-difference identity (4.12w7m) also correctly distinguish a score difference from the two full endpoint score jets. These are substantive repairs to the unrestricted argument.

Likewise, two-label bookkeeping in (4.13), the common-source identity (4.15), and the second-resolvent identity (4.18h) are useful exact algebra. They avoid summing dense response outputs as though they were orthogonal primitive fibers. They do not automatically bound a second derivative of a coordinatewise square.

## 3. First bottleneck: (4.12w7g′)

The [special lemma statement](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:1211) needs a sharp supremum-plus-BV bound for the difference and one fixed-W score derivative. The proof introduces E₂^sp only as “the stopped norm” of a mixed score/residual-fiber derivative [at 1299](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:1299). It then asserts

\[
\mathfrak P\le C\kappa(1+\mathfrak E_2^{\rm sp})
 +Cq^\sharp\mathfrak P,
\qquad
\mathfrak E_2^{\rm sp}\le C(1+\mathfrak E_1^2)
 +C(q^\sharp+\mathfrak P)\mathfrak E_2^{\rm sp}.
\]

The bootstrap algebra is not the problem. If these estimates hold with uniform constants, fixed loose stops can be chosen and improved since κ,q^sharp→0. A coupled first exit is not inherently circular.

The missing verification is upstream of that absorption:

- E₂^sp has no displayed operator-norm definition specifying its residual-fiber domain, covariance/Euclidean normalization, output norm, score parameter, and BV weights. In particular, the covariance projector after score conditioning is not an optional detail when interpreting “one residual-fiber direction.” The later graph-source definitions do not define this constant retroactively.
- The first inequality requires a **sharp coordinate and row/column** concentration estimate for a differentiated, restored local solution map. The elementary arc-length estimate (4.23a) is proved only for a Gaussian linear functional of a coefficient curve independent of the tested fiber. A restored nonlinear response or its score derivative requires a justified derivative bound and conditional-mean estimate; naming Gaussian log-Sobolev does not supply them.
- The normalization matters. A bound of E on a derivative with output in normalized L² permits a single output coordinate derivative of size √n E. Gaussian covariance n⁻¹I then gives a coordinate fluctuation scale E, not E/√n. Obtaining the asserted κ scale requires retaining the insertion exposure and the coordinate influence throughout the mixed derivative estimate. The source table shows the small response-free inputs, but the needed propagation estimate is not derived from the printed E₂^sp definition.
- The second inequality invokes a “polarization of the finite word list” and the sharp multiplier. This explains a possible route once a correctly normalized sharp stop is assumed, but does not present the mixed variational equation and estimates in the norm defining E₂^sp, including the coefficient/fiber restoration terms. The word table verifies what must be estimated, not the missing uniform estimate itself.

The later sharp recurrence (4.12w7j′) and arbitrary-source bound (4.15m) rely on this input. They cannot independently certify it. My verdict for the **special** estimate is unproved here, not falsified by the generic M example.

## 4. Second bottleneck: the actual r=2 catalogue is broader

The [catalogue statement at 2336–2374](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:2336) includes every ordered slot derivative with r∈{0,1,2}, score order k∈{0,1}, and r+k≤2, together with the graph lift and local pullbacks. Its allowed directions are common responses R₀T, differences Zα(T), optional initial-fiber responses Rα(ηα,0), and permitted score derivatives.

In particular, **r=2,k=0 does not require either direction to be a score difference**. Nor does it require one direction to have the sharp norm (4.12w7a). The degree reduction from six to four, or ten to eight after the graph lift, counts factors; it does not bound their multiplication in the stated graph norms.

For example the two matrix slots of Φ_A produce

\[
(M_1v_1)\odot(M_2v_2).
\]

Knowing the two factors in normalized L² does not justify the mapping estimate (4.18i), whose Hadamard bound requires an L∞ factor. Counting a surviving insertion label is also insufficient: multiplying both concentrated vectors in the calculation of §2 by small insertion amplitudes preserves the √n amplification relative to the product of those amplitudes. A quantitative label-dependent pointwise or mixed-multiplier estimate is needed, not just the presence of the label.

The detailed analysis of [the particular derivative (4.19a2′)](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:2469) is narrower: it treats D²M[D_j Q,V_T] and correctly identifies where the special score estimate would be used. It does not prove the full r=2,k=0 catalogue as stated. The final line that products of two first-order quantities use E₁² [at 2533–2547](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:2533) is precisely where an additional bilinear norm estimate is needed.

“Common response” alone is not a mathematical exclusion of concentrated tangents. For any smooth zero-initial tangent path Y about a given smooth core trajectory, the additive source T=Y′−DF(y₀)Y produces R₀T=Y. Thus a restriction must be a quantitative restriction on the permitted source domain/norm or on its provenance, not merely the fact that the tangent solves a forced linear equation. The manuscript's arbitrary-source statements and completion of reachable sources do not explicitly impose a sharp multiplier restriction on one member of every r=2 pair.

I am not claiming that the generic M has unit norm in **every** displayed max-local source norm, or that it is the actual homotopy source. Those are additional issues. The concrete gap is that the proof neither excludes such concentration through the stated catalogue domains nor proves the stronger source-to-multiplier estimate needed to replace the invalid graph-norm inference. If only the particular score/common-response pairs in (4.19a2′) are needed, the catalogue must be narrowed and its closure under fresh-fiber differentiation and endpoint pullback actually checked. The current broader assertion cannot serve as that check.

### A literal prerequisite failure: optional row data

There is a sharper domain test that does not require constructing a positive-time homotopy response. The [optional datum definition](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:1771) permits M_i·(0)=η_i^r and charges only its weighted Euclidean row norm. The [row response norm and (4.15g)](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:1806) include

\[
\sup_\tau L^{-1}|(\mathcal T_yY)_{Z,i}|,
\qquad
\|\mathcal R_i(\eta_i^{\rm r},S)\|_{\mathrm{loc},i}
\le L^C\bigl(\|\eta_i^{\rm r}\|_{\mathrm{row}G,D}
 +\|S\|_{\mathrm{src},i}^{\rm r}\bigr).
\]

Take S=0, all other primitive initial variations zero, and a bounded-mark core layer J of positive density. Set

\[
\eta_i^{\rm r}=\frac{(P_JX(0))^T}{\|P_JX(0)\|_2}.
\]

Its norm in (4.15b′) is O(1): its support lies in a bounded-mark layer with density bounded below. But the exact tangent graph gives

\[
(\mathcal T_yY)_{Z,i}(0)=\eta_i^{\rm r}X(0)
=\|P_JX(0)\|_2\asymp\sqrt n.
\]

Therefore the left side of (4.15g) is at least c√n/L at time zero, while its right side is O(L^C). The estimate is false on the printed initial-data domain. A sufficiently small infinitesimal perturbation remains inside any open gate, so a loose finite-dimensional stopping rule does not remove this tangent.

Under the **intended regression-residual interpretation**, η_i^r must instead lie in X_P(0)^⊥. The example above then is inadmissible, and I do not count it as a counterexample to that narrower estimate. But the displayed definition and bound do not say this; nor do they charge an induced initial row-score datum for a general η. The synthesis proof subsequently calls for fresh-fiber derivatives using these optional-data resolvents. One must specify the projected domain and verify its derivatives, conditional mean directions, and moving-time uses, rather than cite (4.15g) in its present form.

The candidate-column definition does explicitly include induced initial P and Λ data in (4.15j_a)–(4.15j_b). That is an important distinction: the preceding row normalization failure should not be copied without checking into the column estimate.

## 5. Consequence and bounded stopping point

| Item | Focused verdict |
|---|---|
| Arbitrary graph-norm bilinear estimate for D²F_A | False; exact concentrated-matrix calculation above |
| Special sharp score-difference multiplier, assuming (4.12w7b) | Its use in a product with one arbitrary tangent is valid |
| Proof of (4.12w7b) through (4.12w7g′) | Necessary mixed-derivative/concentration estimate remains unverified and insufficiently specified |
| Optional-row bound (4.15g) on the printed datum domain | False at the initial endpoint; residual-domain qualification would remove this example |
| Broad derivative-closed synthesis r=2 | Not proved by the finite-word list, label count, or first-order estimates; sharper direction/norm closure is missing |
| Restricted score/common-response subcatalogue | Plausible intended target, but still depends on the unproved sharp bridge and a precise derivative-closure argument |
| Lemma 2 and downstream initial-layer no-go | Not certified by this manuscript through the audited bridge; the model theorem is not thereby disproved |

The dependency is decisive: (4.12w7g′) is used to obtain the sharp multiplier, then the candidate arbitrary-source resolvent; (4.19a4) supplies derivative-closed synthesis, then the source contraction (4.23), Lemma 2, and the clock comparison used downstream. Algebraic bootstrap absorption and downstream clock cancellation cannot replace the missing analytic input.

For consolidation, use: **“The covariant-Schur manuscript contains exact covariant identities and an explicit special-direction repair, but its sharp mixed-derivative estimate and full r=2 synthesis have not been independently certified. The printed optional-row datum bound also needs a domain/normalization correction. The claimed canonical no-go remains unsupported by this proof bridge in its current form.”**

This completes the requested bounded source check. No repair proof, experiment, or continuation of the nonlinear research program was attempted.
