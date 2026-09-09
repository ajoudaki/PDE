# Fresh complete proof audit: power-four closure and original theorem

Date: 2026-09-07. Verdict: **PASS for the complete original odd two-input theorem**, on the four candidate hashes and the 23 dependency hashes recorded below.

This is a fresh mathematical audit. I read all four candidate documents in full, verified both manifests against file bytes, and inspected the original mathematical arguments needed to verify the full chain. I did not read historical or sibling review reports, status files, evidence ledgers, or review certificates. I made no candidate/dependency edits, ran no experiments, and created no subagents or commits. Hash verification is an integrity check, not experimental evidence for a mathematical claim. The report uses the final candidate bytes, including the corrected affine numerical rounding and the explicit fixed-terminal-time expectation convention.

## 1. Precisely what passes

The conclusion audited is the theorem in `../PROOF.md`, with the full model and observable scope specified in `../../two_sample_odd_activation_theorem/PROOF.md` Sections 1–2. It is valid for every fixed dataset with two deterministic inputs of squared norm d, arbitrary binary labels, and |rho| <= 1-delta, where 0 < delta <= 1, for all a in [1/2,1] and

    0 < e <= c_poly delta^4,
    phi(z) = a z + e atan(z),
    c_poly = min{1/4, c_*, 10^-70 H^-400}.

Here H and c_* are exactly the previously specified numerical constants. The proof preserves the independent Gaussian initialization, finite random readout, raw metric, and simultaneous raw GD step n^-2. The conclusion includes the autonomous global strong population flow, uniqueness against nonsymmetric bounded-primal strong competitors on the same canonical spaces, reached-state restart, full-width-sequence joint GF/GD limits on each fixed finite physical interval, all stipulated action/adjoint and raw-kernel observables, same-layer path and velocity laws, second moments and integrated squared speeds, positive activation-regression error at every finite physical time, and the initial feature-motion certificates.

This conclusion does not extend to either excluded endpoint, to three inputs, to uniform convergence over all datasets or the entire physical half-line, to arbitrary-state existence on the full L2 state space, or to an optimal exponent/prefactor claim. The original normalized positive-weight activation family is also inherited: if 0 < r <= c_poly delta^4, division of z+r atan(z) by its Gaussian L2 norm produces a in [1/2,1] and e <= r. A literal nontrivial convex mixture has Gaussian energy below one, as the original theorem explains.

## 2. Integrity and mathematical sources

All four candidate hashes and all 23 dependency hashes matched in the final verification. Manifest SHA-256 values were:

    CANDIDATE_HASHES.json:
    8439be694a44c71ad06986cdee28e55e20907fe682ead692ff9fe6747567d62d
    DEPENDENCY_HASHES.json:
    1e6427032404b97eeff50bcdabf65350fa9d64680e92639e4c522d8c50464316

I directly checked the original odd theorem assembly and both its affine and initial-motion companions; the source/limit bridge; the quantitative theorem and affine comparison/nonaffinity derivation; the power-ten affine-source certificate, normalization and probe extensions; its positive supersolution and same-array response equations; original source-baseline equations (23)–(25) and their current-source recurrences; the generic two-matrix conditioning, singular-query and common-action construction in `L3_LOCAL_COMPLETE_PROOF.md`; the asymmetric primal/physical continuation bridge; the strong radial/trajectory-chain-rule portions of `SYMMETRY_RADIAL_CLOCK.md`; and the fixed-cap velocity bridge, including its product-query and limit-order arguments. Historical source headers are not premises. The older response smallness conclusions are replaced by the new proof, rather than imported as extra hypotheses.

## 3. Intrinsic scale, primal construction and nonaffinity

The exact scale is essential. With v=(1+y1 y2 rho)/2, r=sqrt(v), lambda=a^3 r, and M=(3/(sqrt(2) lambda))^(1/4), one has

    M > 1,
    r = 3 M^-4/(sqrt(2) a^3),
    S <= 2/lambda <= M^4,
    M <= 24^(1/4) delta^-1/8.

The identity for r uses the actual dataset endpoint scale, not the delta-only upper envelope. Since lambda >= sqrt(delta)/(8 sqrt(2)), the last bound has the stated constant 24.

The independently established primal tube is available before source bootstrap closure. The quantitative affine proof compares the capped nonlinear field at the same state to the affine field, differentiating only the latter. It gives raw discrepancy C0 e lambda^-3, hence at most H e M^12, uniformly in cap. Current raw operator and readout bounds are O(M), so the actual incoming fields satisfy

    ||q1_k||2 <= H M^3,
    ||q2_k||2 <= H M^2,
    ||C_k||2 <= H M.

This follows from q2=B* delta3, q1=A* delta2, and |D_cap(z,q)| <= (a+e)|q|. It is a bound on the actual programs, passed to their fixed-program output laws; it is not an assertion that an arbitrary bounded L2 action preserves subGaussian tails.

The old learned-memory comparison uses raw error e M^12 and at most three primary factors O(M), giving density H e M^15 and row H^2 e M^19 after summing h_j over S. Both matrix orientations are included. The restriction e <= c_* delta^(7/4) supplies the strict primal tube, endpoint g_e(S) >= 5/4, and nonaffinity. It follows from e <= c_poly delta^4 because delta^4 <= delta^(7/4).

I checked the absolute regression margin rather than merely accepting a delta-dependent variance claim. The frozen inactive Gaussian components and affine balance/radial bounds give marginal variances at least 1, 1/404 and 1/16. The third Hermite coefficient of atan(sigma G) obeys

    h(sigma) = -2 sigma^3 E[G^2/(1+sigma^2 G^2)^2],
    h'(sigma) = -2 sigma^2 E[G^4/(1+sigma^2 G^2)^2] < 0.

Consequently its squared regression error has the absolute lower bound eta_* stated in the quantitative proof. Optimal atan-regression slopes lie in [0,1], making the square root of the residual 1-Lipschitz under L2 coupling. The existing c_* transfers at least eta_*/4 to the nonlinear preactivations. Multiplication by e^2 gives the strict activation-regression error. No old exponent-ten or exponent-800 restriction appears in this part.

## 4. Sharpened affine propagator and source identification

The four-gradient calculation is correct. Set z=||D||^2 and F=<D,BAp>. The balances imply

    ||p||^2=1+z,
    z(1+z) <= ||Ap||^2 <= (z+101)(z+1),
    z^2 <= ||B*D||^2 <= z^2+100z.

The A and B gradient squares each exceed z^3+z^2. The D gradient is bounded below by

    ||A*Ap||^2 - 100||Ap||^2
    >= z^3 - 99z^2 - 10200z - 10100.

The positive and negative terms are bounded separately; no invalid monotonicity in ||Ap||^2 is used. For the p gradient, BB*D=zD+K_B D with K_B positive gives the lower bound z^3-100z^2-10000z. Summation gives

    F' >= 4z^3 - 197z^2 - 20200z - 10100,
    z'=2F, F>=0.

Thus F^2 >= z^4-(197/3)z^3-10100z^2-10100z by differentiating the difference. There is no division at the zero initial state. For z<=200, the older F>=z^2/sqrt(2) gives F>=z^2-100z; for z>=200, subtracting (z^2-100z)^2 from the polynomial gives a positive quantity. These cases justify the claimed global lower bound.

At beta scale, w_beta=sqrt(beta^2+||D_beta||^2) therefore satisfies

    (log w_beta)' >= ||D_beta||^2 - 101 beta^2.

For R_beta^2=200 beta^2+||D_beta||^2, the coefficient of the logarithm in the radius-one Hessian integral is exactly three. The constant terms are bounded by 903 beta^2 T < 1810. The radial estimate bounds integral c_beta by 1+sqrt(2), giving integral R_beta <31. The additional integral of 6R_beta+3 is below 192, leaving ample room under 2100. Hence

    G_beta(t,s) <= exp(2100) [w_beta(t)/w_beta(s)]^3
                  <= 10^5 exp(2100) M^3.

The earlier local extension by 1/[1000(200+M^2)] covers the full proposed beta family, since beta_far^2 T-T <= 6(beta_far-1). Bounded-set Euler approximation gives the asserted fixed numerical slack on sufficiently fine meshes. This is a deterministic statement at fixed dataset, not a Gaussian theorem for a growing transcript.

The conversion to source arrays uses the actual independent-root identity in `TWO_SAMPLE_SOURCE_BASELINE.md` (23)–(25): take width at fixed nonzero probe amplitude, pair with the independent Gaussian root, and then send the amplitude to zero. The affine scalar program with its deterministic arrays frozen is affine in this root. Its deterministic derivative therefore equals the covariance measured by that probe. Reusing signed copies of one root bounds complete absolute rows, including direct identities. Off-support named slots at singular covariance remain distinct. This fills the essential gap that a raw tangent bound alone would leave.

I checked the extra R1, top U and reverse-top Ltop probes in the frozen affine-source dependency. Their injection/output products are respectively O(M^2), O(M^4), and O(M^2). Thus the normalized density/row powers in the candidate follow from G=O(M^3). The beta-positivity derivative bounds the products FL and RF without multiplying crude individual row norms. The scaling back to original time contributes both the appropriate field factor and lambda in strict densities. In particular:

| Object | Active power of M | Full-sample bound |
|---|---:|---:|
| F,A2 strict density | -5 | H |
| V,A3 strict density | -3 | H |
| T,B3 complete row | 7 | H M^7 |
| W,B2 complete row | 9 | H M^9 |
| all required resolvent rows | 5 | H M^5 |
| Utop,FL,RF strict density | -1 | H |

The inactive forward densities are O(1), its affine backwards vanish, and its resolvents are identities. The full-sample Utop density is therefore O(1), not O(M^-1).

The final numerical ledger is valid: 4*10^14 times 10^3 times 3*10^7 times 10^4 equals 1.2*10^29, bounded by the final rounded 10^30. Thus 10^30 exp(2100) is below 10^30 exp(5640) <= H. The original H is retained.

## 5. Separate outer boxes and preservation of source transfers

The deterministic coefficient blocks commute with sample exchange. This follows by finite-program induction on both Gaussian covariances and expectations of formal derivative blocks, with frozen arrays transforming equivariantly. Thus the mean/contrast basis diagonalizes every actual deterministic block at every amplitude. Individual random gate matrices need not be diagonal and are kept as full two-by-two matrices in the response proof. This sector reduction makes no symmetry assumption about competitors in the later physical uniqueness argument.

The active backward excess radius is r_a=H^-10 M^-2. Since |F_b|_r <= H^2 M^-1 and |V_b|_r <= H^2 M, the two absorption ratios are at most H^-8 M^-3 and H^-8 M^-1. The exact identities F=F_b+F_b J2 F and V=V_b+V_b J3 V preserve their strict densities. The forward resolvents are controlled by the same left-multiplier identities. The reverse resolvent uses

    L2=L2_b+L2_b J3 V,

after bounding V. This is valid in complete row norm and avoids an invalid assertion that right multiplication by a bounded-row array preserves strict density. The top transfers depend only on A3 and are dominated by their affine forward majorant.

The inactive radius must be separate: r_i=H^-10 M^-5 makes S r_i <= H^-9 M^-1. With inactive strict densities bounded by 2H, all relevant ratios are at most 2H^-8 M^-1. In particular there is no uncontrolled inactive integration row of order M^4 multiplied by the larger M^-2 radius. These estimates justify the response's full-sample H^2 transfer table throughout the closed outer box.

## 6. Arbitrary current rows, the positive supersolution, and strict margins

For strict U,V and a completely arbitrary causal Q, including Q_rr, expand

    |(U Q V)_kj|
      <= |U|d |V|d h_j sum_{r<k} h_r sum_{s<=r}|Q_rs|
      <= S |U|d |Q|r |V|d h_j.

No bound on Q_rs/h_s occurs. This proves the precise strict/row/strict sandwich used by the candidate and retains the original h_j even on a mesh with arbitrarily small positive steps.

At beta=b1, take A2*=A2_b, A3*=A3_b, B3*=B3_b+J3 and define R*,W*,B2* as in `SECTOR_SUPERSOLUTION.md` (3). Positivity of the beta-scaled learned moments and beta^2>=1 makes the two backward inequalities exact. The resolvent identities in (4) are correct, including the factor a^2. Since |V_b|_r q<1/2,

    |R*|r <= H^2 M^5,
    |R* F_b|d <= H^2 M^-1.

The latter uses a bounded left row multiplying the strict RF kernel. The two forward sandwiches have densities bounded by H^3 M^-6 q and H^4 M^2 q. Their sum is at most H^5 M^2 q. The active leading lower bounds F_kj,V_kj >= H^-2 M^-8 h_j then give

    F_b(B2*-B2_b)F_b <= eta F_b,
    eta <= H^7 M^10 q.

All quantities are nonnegative, so (F_b(B2*-B2_b))^n F_b <= eta^n F_b by induction. This justifies the relative increment eta/(1-eta), rather than introducing an unrelated coupled-inverse estimate. The V sandwich gives relative size H^5 M^6 q. Including the direct strict defects, the total relative errors are bounded by H^8 M^10 q and H^7 M^8 q.

Available beta variance slack is at least H^-1 M^-2 times the corresponding reference. Under q <= H^-16 M^-12, the first error is at most H^-8 M^-2 and the second at most H^-9 M^-4. Each is strictly below half that slack. Thus the supersolution really satisfies the two forward inequalities with margin.

The reconstructed backward excess is at most H^4 M^10 q <= H^-12 M^-2 < r_a/2. For the inactive construction, the inverse ratio is bounded by 2H^2 M^4 q, B2* has row at most 3q, and the forward additions

    u=H^3 M^4 q, w=H^5 M^4 q

dominate the F and V feedback plus E2,E3. They obey u,w<1/2, while 3q<r_i/2. The inner-to-outer active forward gap is at least H^-3 M^-10 h_j by integrating the positive beta derivatives. This is a strict margin for each entry at every fixed mesh.

Signed actual coefficients cause no difficulty: every causal inverse is a finite polynomial, giving |T0(C)|<=T0(|C|). The original chronological order A2_k,A3_k,B3_k,B2_k permits finite induction against the nonnegative supersolution. A2,A3 are strict in time, so the current B3 return precedes and may enter the current B2 return without an algebraic same-time cycle. This comparison applies to the absolute values of the actual defects and does not presuppose positivity of the nonlinear coefficients or a strict-density estimate for backward errors.

## 7. Nonlinear values, envelopes and all four coefficient defects

Exact affine elimination at the same deterministic arrays gives the three value equations in the response companion. The leading Z powers are (6,6,7), and the e-weighted self powers are (13,11,8). For example, bottom F has row O(M^4), its transpose Gaussian source has scale O(M^2), and B2 has row O(M^9), giving 6 and 13. The middle and top rows give the stated other powers. Under e H^22 M^19<=1, each self coefficient is below 1/2. The incoming subGaussian scales consequently have powers (15,13,11).

For the derivative, the exact same-array equations are

    J-J_aff=U[DeltaV I_zeta+P J],
    Ddelta-Ddelta_aff=L[DeltaV I_zeta+P J],
    P=L_gate+a DeltaV B+a B DeltaG+DeltaV B DeltaG.

The second identity follows from I+a^2 B U=L, in the displayed orientation. It includes its identity/current term. Gates have bounds DeltaV,DeltaG=O(e), L_gate=O(e Q). The strictness of U gives the causal product envelope with rate e H^6 sum h_r(Q_r+M^b), b=(9,7,4). A single transpose slot retains its h_j initial factor. A full forward-source row has direct norm H^3 M^5 and is padded by zeros at future slots.

The integrated stochastic powers are 4+(15,13,11)=(19,17,15); deterministic powers are (13,11,8). Weighted Jensen with weights h_r/S controls envelope moments from individual-time subGaussian estimates. It requires no temporal independence or random time maximum of Q. The explicit H^22 condition dominates the rate/duration/subGaussian coefficient product H^18, leaving ample room for the eighth moment and fixed numerical factors.

Only after controlling the envelope does the proof use the actual primal L2 bounds:

    E[Q_r E_k] <= ||Q_r||2 ||E_k||2 <= H^2 M^(3,2,1).

This estimate is uniform for every pair of times, so it covers current and source-time terms without independence. Each exact single-insertion defect contains just one explicit Q factor. No unproved small raw Lp norm for p>2 is required.

For the two forward defects, one time integration and the retained B-row perturbations give powers 4+max(3,9)=13 and 4+max(2,7)=11. For the backward defects, L and J each contribute M^5, giving powers 10+max(2,7)=17 and 10+max(1,4)=14. The deterministic gate perturbations involving B are essential; omitting them would incorrectly replace 17 by 12. Current L_gate,k J_kk and B_kk are covered.

The final documents correctly formulate the backward estimate as

    max_k E[sum_{j<=k}|(Ddelta-Ddelta_aff)_kj|],

with the terminal-time maximum outside expectation. At fixed k, expand the deterministic L row and use the uniform-pair-time bound above term by term. This bounds max_k sum_j |E[(Ddelta-Ddelta_aff)_kj]|, precisely the deterministic coefficient norm needed by closure. A stronger E[max_k sum_j |...|] is neither proved nor used.

The learned-memory row e M^19 dominates all these derivative powers. The H ledger gives the complete forcing q <= H^30 e M^19. Estimates compare to the affine formulas at the same coefficient arrays, while the independently bounded learned moments compare to the true affine reference; there is no omitted coefficient displacement or covariance domination hypothesis.

## 8. Final numerical selection and homotopy

The implication from a delta-only coefficient has the correct direction:

    M^32 <= 24^8 delta^-4,
    e M^32 <= 10^-70 H^-400 24^8 < 10^-70 H^-399.

Because M>1,

    e H^22 M^19 < 10^-70 H^-377 < 1,
    q M^12 <= H^30 e M^31 < 10^-70 H^-369 < H^-16.

Thus all response, forward-slack and backward-radius conditions hold with strict numerical room. The required power sum is 19+12=31, while delta^4 pays for M^32. No amplitude depending on the realized trajectory, cap, mesh, width or physical horizon is selected.

At each fixed cap and sufficiently fine mesh, the actual source recursion is a finite causal construction with continuous dependence on the amplitude. Gaussian covariance square-root continuity and the fixed named-source convention handle singular covariance. The homotopy begins inside the outer box at e=0. At a proposed first exit, the closed-box response estimate and the explicit supersolution place every constraint strictly inside, a contradiction. This closes the actual cap/mesh-uniform source construction. One need not prove a uniform positive lower mesh step or a probabilistic statement for growing transcripts.

## 9. Restoration of the complete population/GF/GD and observable theorem

I checked the following downstream premises directly in the original sources.

1. **Common actions and adjoints.** The generic finite-program proof accommodates both Gaussian matrices and both orientations, frozen feedback contractions, independent added roots, and singular query laws by regularization and finite-program continuity. The countable generated-space construction passes finite norm inequalities and transpose identities to bounded actions with actual adjoints. The odd activation and capped gate satisfy the required bounded-derivative coordinate conditions. The original finite readout is retained and tends to zero in normalized norm by fixed-program stability.

2. **Uncut strong feature flow.** The original asymmetric gate estimate has a bounded coefficient on incoming differences, only one O(eR) loss multiplying a forward-state difference, and Gaussian tails only from the cap reference. It gives C exp(C(1+eR)S-cR^2), which vanishes. Current state and raw direction convergence yield the autonomous uncut C1 strong flow through S. The new source proof and primal comparison supply all its assumptions.

3. **Global physical time.** Sample folding and finite-program exchange symmetry give f_i=y_i g for constructed references without assuming uncut uniqueness. Each g_R starts at zero and exceeds one by S. Before its first hit s_R of one, 1-g_R>0; bounded g_R' gives 1-g_R(s)<=M_R(s_R-s), so integral ds/[2(1-g_R)] diverges. This works for capped fields without monotonicity. For the uncut gradient path the strong trajectory chain rule gives C''=JJ*C and g'>=delta/128. Thus the same clock produces one global physical trajectory while remaining inside the compact constructed feature interval.

4. **Nonsymmetric uniqueness and restart.** The original physical comparison keeps both actual residuals. It applies to an arbitrary bounded-primal strong competitor on the same canonical spaces and requires no competitor tails or sample symmetry. Sending R to infinity proves uniqueness on each finite interval. Starting the comparison at a reached state proves restart; the initial cap approximation error is still killed by Gaussian decay after multiplying by the linear-in-R Gronwall factor. No arbitrary-state existence is asserted.

5. **Full-sequence GF and raw GD.** Width is first taken at fixed cap and auxiliary mesh. Finite rank-update sums supply operator bounds with slack, without cross-width trained operator-norm convergence. Deterministic Euler estimates remove the auxiliary mesh with constants independent of width. The same-width asymmetric comparison removes the cap. Simultaneous raw GD contributes only C_(R,T) n^-2 to its comparison with the cap reference; its actual raw interpolation and one-sided node derivatives are retained. These are full-sequence convergence-in-probability arguments and identify the joint GF/GD limit.

6. **Velocity, kernel and path laws.** `FIXED_CAP_VELOCITY_BRIDGE.md` explicitly applies to any fixed finite e under bounded primal/fixed-program premises; it has no old exponent-ten restriction. It first truncates d(Z)P product queries before applying bounded-derivative conditioning, then identifies their source derivatives and learned corrections by dominated convergence. Its deterministic velocity comparison has one reference-velocity truncation factor. The uncut velocity is a continuous L2 path by the strong trajectory chain rule and bounded continuous phi'. Its compact time image has uniformly vanishing L2 tails. The cap is removed at fixed velocity truncation, then the truncation is removed; finite width is taken first at fixed cap/truncation. No bound on the growth of cap-dependent fourth moments is needed. The path interpolation estimate with integrated squared speeds gives the stipulated W2(C([0,T])) laws. Products of convergent L2 fields give every raw kernel and second moment, including off-diagonal sample entries.

7. **Initial motion.** The odd-family proof uses full Gaussian support and phi'>=a to obtain positive initial feature Grams. Its reused-transpose innovations have their full second-moment covariance plus the actual response corrections. Conditional positivity propagates to all hidden acceleration blocks; adjunction and sample exchange make each sample/layer acceleration nonzero. Nonconstant phi'' for every e>0 supplies the required nondegeneracy. Physical-time factors s'(0)=2 and the projected-kernel quadratic coefficient agree. These arguments impose no additional smallness.

The older exponent-ten and exponent-800 thresholds belong to superseded source-closure routes. The original downstream bridge statements use bounded primal paths, cap/mesh-uniform incoming tails and g_R(S)>1, all newly proved here. They do not reintroduce those thresholds. The original superpolynomial E_* restriction is likewise a sufficient construction of the old response premise, not an independent requirement after that premise has been proved by the new argument.

## 10. Objections considered and disposition

| Potential objection | Disposition |
|---|---|
| A raw variational estimate does not identify formal source derivatives. | Resolved by the explicit independent-root finite-difference identity, with the required additional probes inspected. |
| A single M^-2 box could destabilize the inactive integration row. | Resolved by the separate M^-5 inactive radius. |
| Arbitrary backward current rows may destroy strict density. | Resolved by the strict/row/strict sandwich, correct resolvent orientation and finite chronological comparison. |
| Random gates need not be sample diagonal. | Retained as full sample matrices; only deterministic coefficient blocks are diagonalized. |
| L2 bounds alone cannot establish the exponential moments. | The proof first obtains the larger subGaussian scales, controls the exponential, and only then uses raw L2 in the single-Q insertion. |
| A random maximum over terminal times may have been moved through expectation. | Final wording explicitly places max_k outside expectation; the fixed-k expansion proves exactly the needed deterministic row bound. |
| The affine numerical product was rounded down. | Final common factor is 10^30 exp(2100), which exceeds the exact 1.2*10^29 exp(2100) product and remains below H. |
| A local coefficient result may silently replace the original global/full-population theorem. | All construction, clock, nonsymmetric uniqueness/restart, finite GF/GD, velocity/path and nonaffinity/motion bridges were checked with their actual premises. |

There is no remaining mathematical objection or open proof obligation for the claimed full theorem on the final hashes. Sharpness and improvement of the numerical prefactor remain separate unproved questions, as the candidate states.

## 11. Exact frozen file hashes

Candidate paths below are relative to `two_sample_odd_activation_power4/`; dependency paths are relative to `studies/mean_field_peeling/`. Every entry was checked against SHA-256 of its bytes.

```text
PROOF.md
  7e33899649b547e7dcac8a465f2d118518d9db9ef001a3d04d2b9da615aa9485
AFFINE_PROPAGATOR.md
  88a1bfbaf6fd1fc6fcfea56b25a4490932663090eb01710e9d96ba04d26fe460
PRIMAL_L2_RESPONSE.md
  cf313286d301aa9fe5fb121d0c1fa5351213efbeaa4c087656d205c3156e417a
SECTOR_SUPERSOLUTION.md
  e1ce9401b58bcd20384e1b2932d725844fda6904e9c9d70ef4a4f1af0f9ab68d

two_sample_odd_activation_theorem/PROOF.md
  a4d6ed0ee99a1e111b5eba068f2219cf561a2281b1828b26227aca7a0a54a050
two_sample_odd_activation_theorem/AFFINE_CORE.md
  634dd3bbc35436e9d1760bee5c11cbf2124b3c42e8920a1bf3a4fcbb15039711
two_sample_odd_activation_theorem/SOURCE_AND_LIMIT_BRIDGE.md
  2a140f2a5a39f911b5c2ca51bc79102d20e9209f1450d38005360c88103f6e77
two_sample_odd_activation_theorem/INITIAL_MOTION_AND_NORMALIZATION.md
  c96316fdc481ef3f9e6fc402514ca9b45bcff12e199023505fbbb86d4e15bf24
two_sample_odd_activation_theorem/sources/ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md
  27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75
two_sample_odd_activation_theorem/sources/CONTRACT.md
  e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd
two_sample_odd_activation_theorem/sources/FIXED_CAP_VELOCITY_BRIDGE.md
  a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0
two_sample_odd_activation_theorem/sources/INITIAL_FEATURE_LEARNING.md
  bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351
two_sample_odd_activation_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md
  f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4
two_sample_odd_activation_theorem/sources/NONLINEAR_RESPONSE_PERTURBATION.md
  ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568
two_sample_odd_activation_theorem/sources/PREVIOUS_TWO_SAMPLE_PROOF.md
  2891b892667396d64bd747689bcd59aa7ca3ffd224d3579fc3407bca0b623f9a
two_sample_odd_activation_theorem/sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md
  99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066
two_sample_odd_activation_theorem/sources/SYMMETRY_RADIAL_CLOCK.md
  40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4
two_sample_odd_activation_theorem/sources/THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md
  49da0f68047b4f516d3ad3c94b7112259838bcebf68e2296a948364232842789
two_sample_odd_activation_theorem/sources/TWO_SAMPLE_SOURCE_BASELINE.md
  a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f
two_sample_odd_activation_quantitative/PROOF.md
  0a7dbd32cb9cc291e706813b59c0142394e6f9532244e52c21a5ab5d89ed4d02
two_sample_odd_activation_quantitative/AFFINE_POLYNOMIAL_BOUNDS.md
  8387e2f253063c139dacb282ca9f2372478521f54b33a9ef6c8dbd83f2b521ca
two_sample_odd_activation_quantitative/POLYNOMIAL_RESPONSE_LEMMA.md
  51b0f717b33ed618219e086d32b16a95ef4253892171597d1805dd9d37a64f7f
two_sample_odd_activation_quantitative/OLD_THRESHOLD_AND_NONAFFINITY.md
  c63753a83e832793c886b8ae8c122e30e0c01864b86a1a5dc9bee030852f9210
two_sample_odd_activation_power10/PROOF.md
  37b9e8a27135b95b8dffe05fe2b734229fadedc98bc1609259e365dbb2aeba37
two_sample_odd_activation_power10/AFFINE_SOURCE_CERTIFICATE.md
  bc55c0f8e25de1f3a4316fe36e86afa25c9486e014192f2eb818358909b048eb
two_sample_odd_activation_power10/REFINED_RESPONSE.md
  3622a0f903cd51b712d1d524a140d834471b5eb588611f059535c41f6efd2332
two_sample_odd_activation_power10/POSITIVE_SUPERSOLUTION.md
  e2be183521919ce69c7ae41b81f5cd78566c5430a78c2408687f52f1b6d86774
```
