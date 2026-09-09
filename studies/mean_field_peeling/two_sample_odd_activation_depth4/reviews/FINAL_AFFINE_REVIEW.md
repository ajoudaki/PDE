# Independent complete-proof review

2026-09-07. Reviewer: `/root/depth4_final_affine`.

**Verdict: PASS for the complete four-hidden-layer theorem at the exact file identities below.** The argument establishes the same numerical pair `(c_poly,10)` as the L3 power-ten theorem. This is a complete-proof review, including the nonlinear source closure, population construction, physical and finite-width bridges, nonaffinity, initial motion, and the separate depth discussion. It is not merely acceptance of the affine component.

I read the rigorous-math skill and the six new files, including the completed and subsequently clarified population bridge. I did not use any previous review outcome, certificate, status file, or another reviewer's verdict as evidence. No experiment, proof-file edit, old-file edit, or commit was performed. This report is the only file written by this reviewer.

## Exact reviewed files

Paths in this first table are relative to `studies/mean_field_peeling/two_sample_odd_activation_depth4/`.

| File | SHA256 |
|---|---|
| PROOF.md | `f91ce73868922220fd7f6621e08b167472639ebe10f8775d6bb632c10e31c585` |
| AFFINE_CERTIFICATE.md | `541d18c292f63fbd1d408953af9ade9c3911cb623fd68baee3dede4c72d0eb82` |
| SOURCE_RESPONSE.md | `25b0c23ad475f1d0565e15441de01cf9df8336aeff101c1dbf6f83224ced2e79` |
| POPULATION_AND_MOTION.md | `fd1dc71289992880ad4560afa787ddb29bb234f4883addc16cc62e49d519c837` |
| DEPTH_UNIFORMITY.md | `5782203423cba6e5695d7aa36ce1d271f75a2984801b859d426f870d7d10e9fb` |
| CONTRACT.md | `d46ad315beb3f92cd96aa6c608ecc23068106cdc8399e30a9987f4605b909eed` |

## Mathematical dependencies actually inspected

Paths here are relative to `studies/mean_field_peeling/`. A whole-file hash identifies the dependency even where only the indicated mathematical passages were needed. This table does not claim to have read every historical dependency mentioned by its authors.

| Dependency and inspected scope | SHA256 |
|---|---|
| two_sample_odd_activation_power10/PROOF.md, Sections 1–2 and start of 3: exact old coefficient, model scope, normalization, affine/source interface | `37b9e8a27135b95b8dffe05fe2b734229fadedc98bc1609259e365dbb2aeba37` |
| two_sample_odd_activation_power10/AFFINE_SOURCE_CERTIFICATE.md, all sections: both-sector normalization, coordinate probes, current direct terms, beta scaling, numerical prefactors | `bc55c0f8e25de1f3a4316fe36e86afa25c9486e014192f2eb818358909b048eb` |
| two_sample_odd_activation_theorem/PROOF.md, Sections 1–2 and initial Section 3: raw state, metric, algorithm, observable scope and symmetry | `a4d6ed0ee99a1e111b5eba068f2219cf561a2281b1828b26227aca7a0a54a050` |
| two_sample_odd_activation_theorem/AFFINE_CORE.md, Sections 2–7: active/inactive geometry, exact freezing, Gaussianity, nonaffinity and clock | `634dd3bbc35436e9d1760bee5c11cbf2124b3c42e8920a1bf3a4fcbb15039711` |
| two_sample_odd_activation_theorem/SOURCE_AND_LIMIT_BRIDGE.md, all sections | `2a140f2a5a39f911b5c2ca51bc79102d20e9209f1450d38005360c88103f6e77` |
| two_sample_odd_activation_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md, finite conditioning/source derivative/singular-Gram passages and countable common-action/adjunction construction, lines 297–402 and 456–548 | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` |
| two_sample_odd_activation_theorem/sources/FIXED_CAP_VELOCITY_BRIDGE.md, nonlinear independent-root probes, all-index causal derivatives, appended velocity queries and product truncation, Sections 2–5 | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` |
| two_sample_odd_activation_quantitative/PROOF.md, old numerical definitions and Hermite/regression certificate, especially equations (9), (10), (15), (17) | `0a7dbd32cb9cc291e706813b59c0142394e6f9532244e52c21a5ab5d89ed4d02` |

## 1. Statement, raw metric, and exact coefficient

Differentiating the stated normalized predictions in the raw metric gives precisely the first-layer factor `1/d`, each square-matrix factor `1/n`, and the readout factor one in (5). The five displayed kernel contractions are the resulting metric inner products. The physical residuals and loss normalization yield `dot f=-K r`; after folding, the physical field is `2(1-g) grad g`. Thus no extra factor is hidden in the time conversion or the loss rate.

The finite initialized readout still has entry variance `n^-2`, and normalized RMS norm `O_P(n^-1)`. Its zero population limit is obtained by stability, without resetting the finite algorithm. Simultaneous raw GD, its step `n^-2`, and recomputation of the hidden fields on the raw interpolant are preserved.

All terms in the new definitions of `C_0,C_z,C_g,eta_*,c_*,H,c_poly` agree with the earlier numerical definitions inspected above. The activation amplitude depends on delta alone. The dataset-dependent endpoint scale and beta family are proof devices, not parameters of the activation.

## 2. Affine continuation, balances, and numerical bounds

The active first projection divided by `r` has exactly its L2 raw metric: the corresponding first-weight increment has squared raw norm `||dP||^2/v`. The affine prediction is `g=a^4 r F`, and the auxiliary time is `t=a^4 r s`. Consequently the five normalized equations really are the gradient of the degree-five multilinear objective in L2/HS/HS/HS/L2.

I differentiated all four operator balances, including both endpoints. Together with `||p||^2=1+c^2`, they give the successive squared action bounds `16+c^2,32+c^2,48+c^2`. The improved initialized norm bound four follows from the stated net and chi-square calculation, whose union-bound exponent is positive. It is inherited on the generated action spaces, so it adds no hypothesis.

The A3 gradient component gives `F'>=c^6(1+c^2)`. Differentiating `F^2-c^8/4-c^10/5` verifies the integrated coercivity without division at zero. The additional forward/backward ratio argument gives `F'>=5(c^2-32)_+^4` and `F>=(c^2-32)_+^(5/2)`. The signs required when integrating these inequalities hold because `F(0)=0` and `F'=||grad F||^2>=0`.

Convexity of `||D||` follows from `D''=JJ*D`; its initial right slope is one. Thus `c'>=1` and `c'>=c^4/sqrt(5)` for positive time. These prove the first target hit, strong continuation through that hit, `S<=2/lambda<M^5`, and `M^100<=76^20 delta^-10`. Bounded primary actions alone are not mistaken for bounded HS initial actions: only the learned increments are HS, and their integrated rank-one norms are controlled.

I checked the radius-one Hessian estimate and the small/large-c split. Each row has four off-diagonal blocks bounded by `b^3`; integrating the large-c estimate leaves `4 log M` plus the stated numerical constant 4000. The mean-value estimate in (17) is valid for `32/c^2<=1/8`. The resulting propagator is `exp(4000)M^4`, including the raw-time cancellation of lambda. Integrating the same-state forcing `500 e b^4` gives the claimed `H eM^10` discrepancy. Forward telescoping and the exact lambda in the prediction then give `H eM^13` and `H eM^9`. The displayed generous H exceeds the explicit prefactors.

The homogeneous beta family has scaling `beta Theta(beta^3 t)`. Its gap and common extension estimates are compatible; every enlarged reference stays on a bounded common interval. The finite-mesh statements follow at sufficiently fine fixed meshes, without an assertion about a growing random transcript.

## 3. Affine Gaussian fields, actual probes, and nonaffinity

The inactive first root is independent of the active root and all initial matrices. Conditional Gaussian second moments of a learned chain correction are its ordinary Frobenius square divided by n. Telescoping the three-factor chain therefore freezes the inactive fields and proves their orthogonality to active fields. Merely assuming a bounded HS increment would not have supplied this conclusion; the proof includes the necessary independence.

The positive-Wick argument is valid. At fixed positive Euler mesh every active forward coordinate contains its initial chain plus a polynomial with nonnegative coefficients in independent centered Gaussian entries. All expectations in the additional cross and square terms are nonnegative. Fixed-degree polynomial norm bounds and Gaussian operator/root moments provide uniform integrability before the fixed-mesh width limit. Strong affine Euler convergence then gives `||x_l||^2>=1`, rather than only an expectation bound at finite width. Affine source linearity separately gives centered Gaussian marginals. Hence the L4 variances are at least `a^(2(l-1))>=1/64`, preserving the old `1/404` threshold.

I checked the sample/time conversion of both response orientations. Forward strict densities acquire the actual factor `lambda` from `Delta t_j/h_j`, while backward complete rows do not. Active original forward scales contain `r^2`, which is of order `M^-10`; no inactive variance inverse enters because the affine coefficient blocks are sample diagonal and the inactive blocks have explicit formulas.

The coordinate-answer probe table includes the first preactivation and top backward answer, with integrated states retained separately and current identity terms retained. The inspected independent-Gaussian probe proof takes width first at fixed probe amplitude, uses Gaussian integration by parts with the scalar coefficient list frozen, and only then removes that amplitude. It therefore controls the actual formal derivative coefficients, not an unidentified surrogate tangent. Its forcing and output degrees give the claimed normalized powers and all four local resolvents/transfers. Numerical costs fit below H. Section 10's active lower bound also follows directly from the positive strict integration kernel; it carries the individual source step `h_j`.

Finally, the Hermite identity and its monotonicity in Gaussian standard deviation verify the exact old `eta_*`. The optimal arctangent regression slope lies in `[0,1]`; the square-root regression residual is consequently 1-Lipschitz in L2 coupling. The uniform forward discrepancy preserves the required `e^2 eta_*/4` margin through the cap limit and every finite physical time.

## 4. Full source closure, including the extra middle population

The six coefficients arise from unrolling each of the three trained matrices and applying the actual finite-conditioning source rule. Their covariances are full input second moments. All three current backward returns follow by formal differentiation, including the middle terms through the higher current return. Named source coordinates remain distinct at singular covariance. Exchange symmetry diagonalizes deterministic sample blocks, but the random gate matrices remain full in the estimates.

The same-array cancellation is algebraically correct: with `U=(I-a^2KB)^-1 K` and `L=(I-a^2BK)^-1`, the forward difference is `U[DeltaV Izeta+P J]` and the backward difference is `L[DeltaV Izeta+P J]`. The latter includes the current `N_k J_k`. No unproved cancellation between populations is required.

I checked the conservative ledger independently. The local `(U-density,B-row,incoming-field)` powers are `(0,18,30),(1,16,28),(3,14,26),(5,5,17)`. Their largest exponential-envelope moment power is 35. The forward defect formula `2u+5+q` gives `35,35,37`; the backward formula `12+12+q` gives `52,50,41`. Learned moments have smaller bounds and are included. The envelope uses weighted sums of marginal subGaussian variables, so it does not require a random supremum over source times.

Both added middle resolvent pairs are retained. The exact downward supersolution expands the bottom error into the direct B2 error, one pair around the B3 error, and two pairs around the B4 error. Its largest power is

`max(52,24+50,48+41)=89`.

The strict-factor sandwich retains `h_j` around arbitrary causal row errors. Positive compression of the unstarred left chains gives forward density powers `57,68,73`; division by the active lower bound and the beta margin gives the strongest forward condition at power 86. The backward radius costs nine more powers, so the sufficient condition is `e H^72 M^98<=1`. The inactive sector has zero affine backward rows and a finite triangular enlargement, without active-variance division. The chronological first-exit argument and amplitude continuity provide strict containment, including current and concentrated backward errors.

Since `76^20<H`, the unchanged coefficient implies `eM^100<=10^-70 H^-399`. This enforces the power-98 source restriction and every earlier moment, tube, endpoint and nonaffinity restriction. I found no missing additional power of M or inverse minimum mesh step.

## 5. Population existence, trajectories, finite algorithms, and motion

The conditioning theorem actually states finitely many independent Gaussian matrices, each usable in both orientations. Its adaptive conditional-projection proof, full-moment Gaussian source identification, and finite singular-query regularization apply to three matrices. The countable generated-space construction extends all six orientations as bounded actions, with finite transpose identities giving genuine adjoints. At fixed cap the coordinate maps have bounded first derivatives and linear growth. The clarified population bridge derives local Hilbert-space existence and strong Euler convergence from this local Lipschitz field and the strict bounded Euler prefixes; it does not assume the desired uncut flow.

In the asymmetric cap comparison, each extra gate contributes `eR` only on an already controlled forward state difference; backward differences propagate with a bounded gate and action. Thus the coefficient remains `C(1+eR)`. The source tails defeat its Gronwall factor. Both raw states and raw directions converge, yielding strong C1 solutions. The same estimate uses tails only from the constructed reference and therefore proves uniqueness against nonsymmetric bounded-primal competitors and restart at reached states.

Odd folding is an identity of the finite raw loss. Exchange equivariance and deterministic limiting contractions prove symmetry for the constructed flow before any uniqueness assertion is used. The compact feature interval reaches above one. Bounded `g'` makes the physical clock diverge at its first hit of one; this supplies all finite physical horizons with the same activation. Radial convexity gives `kappa>=kappa(0)>=a^8 delta/2`, and the loss identity gives `exp(-2a^8 delta t)`. The compact gain range has rate delta/128; the requested convex family has `a>=3/4` and retains `exp(-delta t/32)`. These distinct numerical claims are stated accurately.

Fixed finite transcripts, stopped deterministic Euler comparison, and then cap removal identify finite GF and raw GD along the full width sequence in probability. The additional raw-GD reference error is `C_{R,T}n^-2`; no conditioning theorem for growing transcripts is used. All five kernel contractions follow from L2 convergence.

The bridge supplies the third observational velocity query in the correct order. The nonlinear independent-root probe gives the primary complete derivative-row bounds; its causal reduction has no implicit same-time inverse. For each appended query, the new forward Gaussian argument has zero formal derivative with respect to the local primary reverse group. Expected response rows and Lp velocity moments therefore induct through all three queries. The products `phi'(Z)P` are first smoothly truncated, and their source derivatives and full covariance moments converge in the specified order. This avoids an unsupported Lp operator bound. The deterministic velocity comparison has a single truncation factor; compactness of the uncut reference's L2 time image supplies uniform tails. The stated uniform-time and fixed-multiple-time W2 laws, second moments, integrated speeds, and same-layer path laws follow. The path interpolation inequality has the required averaged integrated-speed bound.

At initialization, the forward Grams are positive definite. The top backward second-moment matrix is positive definite because a null relation would force a nontrivial relation between the nonconstant derivatives of the two independent Gaussian arguments. Each of the three actual transpose identities has a fresh reverse Gaussian covariance equal to the full preceding backward second moment. Conditional covariance and positive gates then propagate positivity down to layer one. Contracting these matrices with the preceding forward Grams proves every hidden raw block accelerates. The adjunction identity for the accumulated layer acceleration and exchange symmetry prove that both samples accelerate at every layer; positive gates give the corresponding feature statement. Strong small-time expansions justify trajectory derivatives and the projected kernel coefficient `8||V||^2` in physical time. These arguments do not claim perpetual nonzero velocity or movement of every scalar coordinate.

## 6. Arbitrary-depth claims and final scope

The separate initialization recursion for a fixed convex coefficient is correct. The small-variance expansion is `q_next=q-2 theta q^2+O_theta(q^3)`, yielding `L q_L ->1/(2 theta)`. The odd Hermite expansion preserves the correlation sign and decreases its magnitude, so `delta q_L/2<=kappa_L(0)<=q_L`. Differentiation at physical time zero excludes a positive exponential rate common to all depths. Removing the linear projection of the cubic term gives regression residual `(2/3)theta^2 q^3+O_theta(q^4)`, hence the stated `1/(12 theta L^3)` asymptotic.

These are valid obstructions to positive numerical bounds uniform in depth. They are not a counterexample to one common activation satisfying the qualitative theorem separately at every fixed finite depth. The general affine balance and source identities exhibit depth-dependent constants and powers; they do not prove a positive infimum of admissible amplitudes over all depths. The final theorem states that common-coefficient question as unresolved. That qualification is essential and is respected throughout the claim being accepted here.

No blocking mathematical gap was found in the exact five-file mathematical set identified above. The PASS covers L4 with the unchanged L3 coefficient and exponent, and the stated depth-uniform numerical obstruction; it does not certify a common-coefficient theorem at arbitrary finite depth.
