# Independent mathematical audit — basalt

**Verdict: PASS for the mathematical result.** I found no unresolved mathematical objection to Theorem M.1, including the actual raw GF/GD, observation, regression, and initial-motion claims. Several formula tokens are visibly corrupted in the supplied transcription; their exact replacements and independent derivations are recorded below. They do not require a new hypothesis or a change in the theorem's constants.

**Document audited:** `/tmp/hidden_depth_review_20260908/manuscript.md`.

**SHA256:** `e61789c67fc6ea5ee918c50b82c7d5a233c0991e7222d32a003ca722f837606a`.

**Reading scope:** All 2,864 lines, including Parts M, F, S, G, V, N, and A, were read in full. I then reconstructed the essential source, comparison, velocity, and initial-motion recurrences. No other project files, previous manuscripts, author notes, reviews, conversations, or skill files supplied mathematical context. I used no subagents and communicated with no other reviewer. The hash and line count were checked directly.

This verdict concerns the stated order of quantifiers: each dataset, function, finite depth, and finite physical observation horizon is fixed before width tends to infinity. It does not validate simultaneous width/depth limits or an interchange of width and infinite time.

## 1. Dependency and obligation ledger

| Obligation | Finding | Main dependencies checked |
|---|---|---|
| Original raw metric, finite initialization, and finite algorithms | Validated | M.6–M.10; exact differentiation and metric inversion |
| Hidden normalization with unchanged readout and metric | Validated | M.12–M.14, F.39–F.43, V.2, V.34 |
| Finite Gaussian programs with reused transposes and singular queries | Validated | F.5–F.14; adaptive conditioning, integration by parts, noise regularization |
| Canonical bounded initialized actions and actual adjoints | Validated | F.24–F.33; generated-space density and limiting adjunction |
| Scalar Fréchet derivatives without false ambient Nemytskii differentiability | Validated | F.34–F.43 |
| Cap-independent controlled moments at every fixed depth | Validated | S.2–S.6, with the corrected elementary constants below |
| Uniform gain arithmetic and all-time control-clock closure | Validated | G.1–G.19 and M.4 |
| Strong uncut population path, uniqueness, and restart | Validated | V.7–V.10; reference-only tails and one factor of the training cap |
| Actual finite raw GF and GD with step n^-2 | Validated | V.11–V.12, V.30, V.35–V.36; actual nonzero finite readout retained |
| True raw kernels | Validated | V.33–V.34 and true backward observation closure |
| Source-valid velocity queries and uniform-time velocity laws | Validated | V.13–V.29, V.31–V.32, V.37 |
| Joint-time laws, full path W2, second moments, and integrated speeds | Validated | V.32, V.38–V.40 and ordered tail removal |
| Persistent nonaffinity and one gain at all finite depths | Validated | G.21–G.25; A.1–A.20 |
| Every hidden block/sample acceleration and coefficient 18 | Validated | N.4–N.23; exact source and innovation recurrences |

No nonclassical external theorem is invoked as a premise. The specialized finite-program and source statements actually used are proved in Part F; the moment statement is proved in Part S. Consequently there was no external specialized source whose complete primary text or proof had to be fetched. Standard finite-dimensional Gaussian projection, integration by parts, Hilbert-space completion, and elementary measure/ODE arguments were checked in their supplied uses; the manuscript also supplies the relevant constructions.

## 2. Raw model and scaling audit

For the physical predictor `f_i = n^-1 C^T h_i^L`, its Euclidean bottom derivative is `n^-1 b_i^1 x_i^T`. Inverting the bottom metric `d/n` gives `d^-1 b_i^1 x_i^T`. The internal matrix metric is ordinary Frobenius, so those derivatives retain `n^-1`; the readout metric `n^-1 I` removes the readout derivative's `n^-1`. This reproduces M.10 exactly.

The change `w = sqrt(d) W^1` is an isometry: `(d/n)||Delta W^1||_F^2 = ||Delta w||_n^2`. The normalized activation is exactly

`chi_l(Y) = phi(a^(l-1)Y)/a^l`.

Therefore `chi_l' = phi'/a`, `b_i^l = a^(L-l+1)d_i^l`, and `f_i = a^L F_i`, with **C unchanged**. Each hidden raw update and the readout update consequently has the same physical multiplier `a^L` in front of its normalized direction. There is no hidden readout scaling or change of learning rate.

The exact normalized kernel factors are

* bottom: `a^(2L) Gamma_ij <d_i^1,d_j^1>`;
* internal block l: `a^(2L) <d_i^l,d_j^l><X_i^(l-1),X_j^(l-1)>`;
* readout: `a^(2L)<X_i^L,X_j^L>`.

These agree both with direct metric differentiation and with the original backward/feature scalings. The finite rank-one action is `uv^T/n`, whose Hilbert–Schmidt norm in normalized vector spaces is its ordinary matrix Frobenius norm. Thus the action-space metric has the required finite counterpart.

The finite readout has `E||C_0,n||_n^2 = n^-2`, hence discrepancy `O_P(n^-1)` from zero. Its removal only in a fixed-cap comparison is legitimate. It is not reset in either actual algorithm. The physical GD interpolation has the preceding-node raw direction; recomputing the hidden fields requires the derivative at the interpolated state in this direction. V.8, V.10, and V.11 preserve that distinction.

## 3. Finite Gaussian foundation and differentiation

The adaptive conditioning proof does not incorrectly assume query/matrix independence. Conditional on the complete current transcript, the new query input is fixed, and the new observation conditions only the queried Gaussian residual factor. The minimum-Frobenius solution in F.6 satisfies both `WV=Y` and `W^T U=Q`; the compatibility relation supplies the otherwise potentially missing constraint. The free Gaussian part is precisely `P_(U-perp) Wtilde P_(V-perp)`.

The removed finite-dimensional projection of fresh noise has expected normalized squared norm `rank(U)/n`. The retained scalar source uses the full **uncentered input Gram** for its covariance. The opposite-orientation correction is obtained from `E[zeta h_perp] = G_U E[partial_zeta h_perp]`; substituting the old responses cancels the regression-input derivatives. This establishes F.9–F.10 with all named-source dependence retained.

For singular queries the added noise is a new independent input at each call. Its Schur complement contributes at least the square of its amplitude. The finite original/perturbed programs are compared with the same matrices using operator bounds, while limiting laws and expected source derivatives pass by finite covariance square roots and bounded derivatives. No pseudoinverse continuity at rank loss is needed. The singular-support contraction invariance in F.14 is also correct.

The common-space action construction is valid on the generated language: finite inequalities transfer to deterministic L2 inequalities, density extends the actions, and the finite adjunction identity extends by continuity. This is a construction of the initialized actions required by the theorem, not a substitution of arbitrary bounded operators.

F.41 is sufficient for the scalar Fréchet derivative: truncate the fixed incoming L2 weight, use the quadratic remainder on its bounded portion, and the linear remainder on its L2 tail. Forward increments are O(raw increment). The downward expansion then leaves only finitely many `o(raw increment)` scalar errors. Separately, bounded multiplier continuity proves the curve chain rules. No step needs the generally false assertion that a nonlinear activation is Fréchet differentiable as a map from all of L2 to L2.

## 4. Reconstructed controlled source recurrence

At a local layer, with deterministic coefficient arrays frozen, the equations are

`Y = xi + Acal d`, `q = zeta + Bcal X`, `X = chi(Y)`, `d = D(Y,q)`.

`Acal` is strictly past in time. `Bcal` includes the current transpose return. The learned forward contribution at `(k,j)` is `h_j c_j E[X_k X_j]`, and the learned reverse contribution is `1_(j<k) h_j c_j E[d_k d_j]`. The remaining coefficients are the exact expected named derivatives in S.1. The bottom and readout integrators have the stated strict-past structure.

Writing `X=Y+u`, `d=q+v`, with `|u|<=2/K` and `|v|<=|q|`, gives exactly

`Y-Y_G = U v + U Bcal u`,

`q-q_G = Bcal U v + Lloc Bcal u`,

where `U=(I-Acal Bcal)^-1 Acal` and `Lloc=(I-Bcal Acal)^-1`. Thus, if `r=alpha S b<=1/8`,

`m_p(q-q_G) <= 2r m_p(q) + 4b/K`.

The Gaussian variance is bounded from the **actual** L2 field and this same-array identity, not from a comparison covariance. Absorbing `2r m_p(q)` yields the stated generous bound `20(Q+b/K)sqrt(p)`. The offset is harmless precisely because it is `O(1/K)`.

The source derivative recurrence is

`J = I_xi + Acal [N J + V(I_zeta + Bcal G J)]`.

In particular the `Bcal` diagonal is present. Its strict outer `Acal` makes this a past-time recurrence. Taking row norms gives

`J_k <= 1 + alpha sum_(j<k) h_j (N_j+4b) M_j`.

The product bound produces `E_k = exp(4 alpha b S + alpha sum_(j<k) h_j N_j)`. A single reverse slot has forcing at its own time followed by this same past-time propagation, yielding `|partial_(zeta_j)X_k| <= 4 alpha h_j E_k`. The response bounds are consequently

`alpha_next <= 3F^2 + 16 alpha`,

`b_previous <= 512(n_l+b) + 3S`.

The chronology closes without an unknown-current-row assumption: a current forward row only needs backward fields from completed earlier times; after all forward rows have been built, the top incoming readout row is already known; the reverse sweep then successively supplies the current incoming row needed at the next lower layer. This is the essential noncircularity check, and S.6 supplies it.

The independent primal bound is `D(s)<=3 sqrt(L) F^2 s^2`, with `F=32^L`. It precedes the source estimates and prevents an overshooting Euler node using only preceding states. The exact arithmetic for the box is

`alpha_l S b_l <= 24576 (67108864/a)^L 64^(-l) T^2/a`.

Also `n_l<=b_l/2048`, so `W_l=60(n_l+b_l)<=61b_l`. With `a>=10^12(1+T)`, the requirements for the exponential envelope are more than satisfied uniformly for finite `L>=2`. There is no depth-growing factor left outside the powers controlled by a.

## 5. Geometry, control clock, and regression arithmetic

The augmented Gram estimate is correct even for singular input Gram matrices. In the mixed-sign case its projected two-variable quadratic form has determinant `D^2`, trace at most 4, and `D>=delta`; also `(r_1+r_2)^2+b^2>=||v||^2`. Thus `Gamma+11^T >= delta^2 I/4`.

The Gaussian constant/linear projections preserve positive semidefinite order. The improvement `|E psi'(sigma G)|<=1/sigma`, together with `sigma_l >= (a/2)^(l-1)`, makes the normalized projection losses summable: `sum d_l=1/(a-2)`. This yields `Q_L(0)>=lambda I`, uniformly in finite depth.

The top Gram perturbation and possibly nonsymmetric capped hidden contribution are both bounded by `54*2^40*T0^2/a^4 < lambda/4`. It is correct to use an absolute operator bound for `J_h U_h,R`; symmetry is neither true nor required. Consequently the exact capped residual equation implies the claimed residual decay. Its total control time is at most `6/(lambda a^L)=S/2`, strictly inside the interval on which the independent controlled estimates were established. Fixed-cap continuation therefore closes globally before cap removal.

The optimal affine slope for a 1-Lipschitz target has magnitude at most 1, including the constant-variable case by direct choice. This proves the variance-free stability estimate for the square root of the regression residual. The finite-interval density lower bound gives `R_psi(sigma G)>=c_psi/sigma`. The ratio of the displacement to the required square-root margin is bounded by

`24 sqrt(L) T0^2 (32768/sqrt(a))^L /(sqrt(c_psi) a^(3/2))`

and hence by `3*2^34*T0^2/(sqrt(c_psi) a^(5/2)) <= 3/4`. Thus the exact second condition in M.4 suffices. The stronger layerwise bound in A.12 is consistent with M.17.

Part A's compact-support obstruction is already present at initialization and correctly prevents a positive universal depth margin for the broad class. Its stronger open C_b^2 class is valid: the tail-limit computation for the arctangent center has positive residual, continuity gives a positive minimum over all scales at least one, and the uniform function perturbation estimate transfers that minimum to the entire ball. The displayed derivative maximum `3 sqrt(3)/32` is correct.

## 6. Cap removal and actual finite algorithms

The important gate comparison is V.7. After the forward discrepancy has been bounded by the raw state discrepancy, the downward recursion has the form

`E_l <= C E_(l+1) + C(1+R) alpha + C Tail_l`.

Solving it over fixed depth introduces **one** factor R, not R^L. All tails belong to the capped reference. Uniform subGaussian reference tails then dominate the Gronwall growth: `exp(C_T R-cR^2)` tends to zero. This gives uniform raw state and raw derivative convergence, the strong integral equation, uniqueness against a bounded-primal competitor without competitor tail assumptions, and restart from each reached state.

At fixed training cap the raw field is locally Lipschitz with width-independent constants on the chosen primal ball. The finite-program theorem is applied only to a fixed auxiliary transcript. Rank unrolling and convergence of its contractions give the finite primal event before probes or velocity estimates are used. Fixed-cap finite GF and the actual fine raw Euler algorithm are then compared to that same-width coarse reference. Initial readout stability is used only in this fixed-cap bridge.

For uncapped GD the comparison correctly applies the gate estimate at the preceding fine node and adds the capped reference's within-step variation. Thus the argument needs no width-uniform Lipschitz constant for the uncut field. With fixed cap, `eta_n=n^-2` tends to zero, and the comparison prevents a first exit. Width is taken before the training cap is removed. Finite GF global existence also follows independently from its exact raw energy identity.

## 7. Velocity queries, true kernels, and path laws

The instantaneous velocity recursion V.22 is the derivative of the recomputed hidden fields, including `A_l U_(l-1)`. Appending forward velocity queries in ascending layer order leaves only primary reverse inputs for the queried matrix. The new source formula therefore has the stated response row. Although the primary transcript has been completed through later times, a time-k input has zero derivative in future named source slots; correlated Gaussian slots do not change this formal derivative fact.

The bounded expected primary response rows from Gaussian forcing are sufficient for V.19. The subsequent pointwise derivative-row recurrence establishes the stronger bound actually needed for velocity queries. These two bounds are not conflated.

For each ascending velocity query the induction gives

`R_(zeta_m) P_m <= C`,

`R_(zeta_m) U_m <= C(1+|P_m|)`.

The latter follows from the exact product derivative `g_m' P_m partial Y_m + g_m partial P_m`. The new forward source has variance `||U_(m)||_2^2`; its deterministic response row and the primary subGaussian fields then give subGaussian velocity moments. Differentiation in the next layer's primary reverse sources annihilates the new primitive source and differentiates only the primary fields in its return term. This closes the induction at the required layer rather than presuming a future velocity estimate.

The products are legitimized with an outer cap while previous inner caps are removed. Their derivative envelopes are integrable independently of the outer cap, and the explicit source representations supply derivative convergence. W2 convergence alone is not being used to infer derivative convergence. Empirical cap removal uses the positive-part tail functional and bounded actions; it does not assume empirical fourth moments.

The deterministic state/direction velocity estimate V.29 also has one threshold factor. At fixed cap it bridges finite coarse node velocities to finite and population paths. For training-cap removal, the order is essential and correct: width at fixed R and M, then R to infinity at fixed M, then M to infinity. Compactness of the uncut population velocity image in L2 supplies the final uniformly vanishing tails. No uncontrolled growth of a cap-dependent fourth-moment constant is multiplied by the cap-removal error.

The descending true-backward observations have their own ordered clipping argument, so true kernels are not identified with the capped update kernel. Their uniform-time passage uses strong continuity and compact L2 tails. All sample off-diagonal pairings and all hidden blocks survive.

Finally, joint laws at a fixed observation grid plus

`||x-I_h x||_infinity^2 <= 4h integral |x'|^2`

give full path W2 convergence and the necessary supremum-norm second moments. Uniform-time velocity W2 gives convergence of the squared RMS speeds and therefore integrated squared speeds. This is an actual coordinate-path argument; fixed-time laws alone would not have sufficed. The finite-time concatenations and generated probes use finite unions and bounded-action error propagation, with no cross-width operator identification.

## 8. Initial motion and coefficient 18

The restriction `L>=2` matters in the proof of `S_L>0`: the top initialized three-sample Gaussian has full support because the first feature Gram is positive definite. If a linear combination of the top backward fields vanished, continuity and full support would force `sum v_i phi'(z_i)=0` everywhere. Differentiation and `phi''` not identically zero force every v_i to vanish. Bounded nonconstant psi guarantees that last nonvanishing condition.

The reverse representation is exactly `q_i^l=zeta_i^l+sum_k R_ik^l h_k^l`, with covariance `S_(l+1)`. Its response includes both the curvature term and the current higher-layer return. Conditional covariance then propagates strict positivity of every S_l. This proves every hidden block and every bottom sample direction is nonzero even when Gamma is singular.

For upper sample motion the exact ascending recurrence is

`U_j^l = xi_(T_j^(l-1)) + sum_i c_ji^l beta_i^l`,

`c_ji^l = p_i (Q_(l-1))_ij + c_ji^(l-1) E[D_j^(l-1)D_i^(l-1)]`.

Regressing the new centered source on the original forward tuple uses the **uncentered** input Gram, with no intercept in the input-space regression. Its positive innovation cannot be cancelled by the beta terms, which depend only on the original forward tuple and the independent reverse group. The innovation variance is positive at layer 2 by conditional reverse variance and remains positive upward after multiplication by the strictly positive derivative gate. The coherent clipping recurrences N.22–N.23 justify these source derivatives with C2 regularity; no third derivative is needed.

The physical expansions are `C(t)/t -> 3H`, `b_i^l(t)/t -> 3 beta_i^l`, and therefore `theta_h'(t)/t -> 9V`. The strong curve chain rule gives the corresponding `9U_j^l` and `9T_j^l` accelerations. The adjoint telescoping identity is `<H,T>=||V||_hidden^2`. Consequently the readout kernel part contributes `9t^2||V||^2` and the hidden gradient norm contributes another `9t^2||V||^2`. Their sum yields exactly 18, with every hidden block strictly positive.

## 9. Transcription repairs, independently resolved

These should be corrected in the document, but do not leave the mathematics undetermined:

1. At lines 977, 979, 989, and 999, `exp(S.1)` must be `exp(1)` (Euler's number, not the perturbation amplitude e).
2. At lines 945, 989, and 998, `sqrt(S.2)` must be `sqrt(2)`.
3. At line 2262, `o(N.1)` must be `o_P(1)` for the finite-width vector error (or an explicitly stated equivalent convergence-in-probability notation).

The first two repairs can be verified without guessing a result. From `||Z||_p<=M sqrt(p)`, expansion gives

`E exp(Z^2/(4 exp(1) M^2)) <= sum_(k>=0) 2^-k = 2`,

using `k! >= (k/exp(1))^k`. Young's inequality then gives the printed, deliberately loose bound `E exp(u|Z|) <= 2 exp(2 exp(1) M^2 u^2)`. Hence

`||E_k||_2 <= sqrt(2) exp(4 alpha b S + 4 exp(1) alpha^2 S^2 W_l^2)`.

The S.3 coefficients are `42` on `alpha S Q_l` and at most `44+4/sqrt(2)<50` on `alpha S b/K_l`. Thus these repairs preserve both production constants and every later gain inequality. The third repair follows directly from the finite number of convergent scalar coefficients and bounded-in-probability normalized vector norms.

No mathematical repair beyond these explicit transcription corrections was identified as necessary. In particular, the review does not rely on the manuscript's assertions of internal completeness: the decisive recurrences and the dependency order were checked above.
