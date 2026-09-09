# Independent complete-candidate review

Verdict: **PASS** for the theorem stated in `two_sample_odd_activation_depth56/PROOF.md`, with the exact file hashes below. I found no blocking mathematical obligation after checking the affine estimates, their numerical prefactors, the nonlinear source closure, and the retained population and finite-width conclusions. This verdict does not certify a depth-independent positive prefactor, optimality of the displayed powers, or a uniform-in-depth limit; none of those is claimed.

Reviewer: `/root/depth56_final_affine`. Date: 2026-09-07. This is an independent reading and derivation, not an adoption of another review verdict. No trajectory experiment was run and no canonical theorem file was edited.

## Exact candidate reviewed

Paths are relative to `/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth56/`.

| File | SHA-256 |
|---|---|
| PROOF.md | `366bf83ff0250a42da9f4f2fae7d51f0dd296cfb2ea3c462761423fec09e8d70` |
| AFFINE_CERTIFICATE.md | `50d09b24de8fe6aa8cbf0d068f71f71596bcefc227c5d745191c69fdcaab095a` |
| SOURCE_RESPONSE.md | `9a05a1b7d4e2075156cb1483c69ed80e7ab02f9fd84de2c6d8a704f2466049b1` |
| POPULATION_AND_MOMENTS.md | `dd49edf52076dce683934f90df58e0ff2362e14fa02c00edd0d2cabd49b43c8b` |
| CONTRACT.md | `e3555b8366f9bdba253f1b0c991f84c1d1bc0082f06131416548646d50ae9207` |

The final change from “2019 text” to “first-edition text” is bibliographic only. The Gaussian matrix norm inequality used in the proof is also accompanied by its Gaussian-comparison derivation; its numerical constant does not depend on a tail-exponent constant from the citation.

## Dependencies inspected as mathematics

I read the new five-file candidate, the older depth-four affine certificate and source-response argument, and its population/motion derivation. I also checked the actual generic finite-Gaussian conditioning and common-action construction in `two_sample_odd_activation_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md`, especially lines 297–449 and 456–547. Those passages explicitly allow finitely many independent matrices reused in both orientations, despite the historical section title mentioning two matrices. I read the actual `FIXED_CAP_VELOCITY_BRIDGE.md` product-query, ordered-truncation, deterministic velocity-comparison, and width/Euler arguments, and the original odd `INITIAL_MOTION_AND_NORMALIZATION.md` transpose-covariance and motion calculations. The numerical definitions of the old H and c_poly were checked in `two_sample_odd_activation_power10/PROOF.md` and the quantitative proof. Earlier PASS records were not used as premises.

## Affine dynamics and raw norm

1. The normalized objective is the degree-(L+1) multilinear form F = <D,A_L ... A_2 p>. With t = a^L r s, its displayed gradient equations use exactly the original raw metric. Normalizing the active first-root coordinate contributes the compensating metric factor. Inactive first-root directions contribute zero to the affine objective and Hessian, so the tube Hessian also covers nonsymmetric raw perturbations.

2. The adjacent operator balances give ||p||² = 1+c² and ||A_j||² ≤ c²+4(L-j+1) with initialized action norm two. The norm-two conclusion passes through finite generated probes and dense extension, not through a false operator-norm convergence between widths. The initialized forward norm is one by fresh-matrix conditioning.

3. Cauchy in every gradient block gives F' ≥ F²[c^(-2)+S_L(c)]. For w=c², d(F²)/dw = F'. The initial ratio F²/w tends to one, so integration produces exactly F² ≥ c²(1+c²) product_k(1+c²/(4k)). Thus c'≥Q_L/b_L and F≥c^(L+1)/b_L. The operator bound in the matrix Cauchy estimate is legitimate because each matrix gradient is rank one; no infinite initialized Hilbert–Schmidt norm is invoked.

4. The all-block ratio estimate loses at most four per adjacent step and yields the additional large-c bound with K_L=4(L−2). Radial convexity follows from D''=J_h J_h*D and gives c'≥1. These inequalities provide actual strong continuation to F=3/(2lambda), not merely a formal target estimate. They also give T≤1+b_L/(L−1), S≤2M^(L+1), and M^(L+1)≤D_L delta^(-1/2).

## Hessian and old numerical H

The readout-hidden Hessian star has norm at most Qtilde sqrt(Stilde). The hidden-hidden block is dominated by a positive rank-one scalar block matrix, with norm at most (c+rho)Qtilde Stilde. Their sum is a valid upper bound in the Hilbert direct-sum norm. Dividing by c'≥Q_L/b_L gives the early integral in (D).

I checked the numerical L6 bounds and the tail independently. For c≥8, the two factors are bounded by

    dt/dc ≤ c^(-L)(1+208/c²),
    ||Hess F|| ≤ L c^(L−1)(1+0.1/c+100/c²).

The integrable product beyond L/c has integral at most

    6[0.1/8 +154/64 +20.8/(3·512) +5200/4096] <23.

Together with the early bound below 5070 this proves the stated 5100+L log N bound, including terminal c<8. The lower-depth early integrands and bounds are no larger. The original-time Hessian acquires lambda while ds=dt/lambda, so the same integral controls the original raw comparison; no extra angle-dependent exponential is present.

The numerical margin 10^80 exp(5200)<10^30 exp(5640)≤H is valid. The six-layer primary, forcing, probe, sample-coordinate, beta-gap and norm-conversion factors fit that allowance. The old H is therefore sufficient at all L=3,4,5,6; it is not silently replaced by a new depth-six constant.

## Explicit general-depth primitive prefactor

The general cutoff B_L=4sqrt(L(L−1)) makes K_L/c²≤1/(4L). The derivative bound used for (1−u)^(-(L+1)/2) is ≤L on that interval. The logarithm of the enlarged-primary power is below 1/4, validating its exponential linearization. Integrating its products with the radial estimate costs less than the stated 2L. Hence the explicit C_L and exp(C_L)M^L propagator are justified.

The elementary bounds (I), beta continuation interval, and gap reciprocal (J) check out. In particular the beta time displacement is smaller than the continuation time before c reaches 2M. The forcing in (K) follows from forward and backward telescoping with bounded arctangent and |tau_R(q)|≤|q|. Its time integral is bounded by (L); multiplying by lambda^(-1), the single propagator and norm conversions gives (M).

The remaining field, learned-moment and answer-probe costs have the displayed degree in M. The normalization r=3b_L/(2a^L) M^(-(L+1)) and a∈[1/2,1] accounts explicitly for the actual gain dependence. The forward density obtains r² and a strict-time factor; backward rows obtain r^(-1). The inactive forward component freezes and its backward coefficient vanishes, so no inverse inactive variance is needed. All primitive numerical products fit exp(C_L)J^(100L), and therefore the stated exp(C_L+1000L² log J). Products of multiple independent primitive bounds are subsequently counted as powers of H_L in the response proof.

## Nonlinear source closure and exponent ledger

The source equations retain full second-moment covariances and the recursively current transpose returns. In the same-array cancellation, all four terms N, a DeltaV B, a B DeltaG and DeltaV B DeltaG remain. This is essential: the improved incoming-field moment exponent cannot replace the deterministic backward row exponent.

The raw comparison precedes the source bootstrap. At an actual homotopy coefficient list, the exact decompositions into Z_G,q_G and nonlinear remainders recover the smaller Gaussian scales from that already available L2 bound. Gaussian moment bounds then apply to those Gaussian combinations regardless of their mutual correlations; absorption in the exact q equation proves the claimed marginal subGaussian bounds. No pathwise time maximum or Gaussianity of the nonlinear fields is assumed.

Using w_i=max(m_i,b_i)=b_i in the strict derivative envelope gives the listed forward defects and Q_j=8L−3−2j below the top, Q_L=5L−1 at the top. The learned-moment powers are smaller, including at L3. Weighted marginal-moment estimates control the envelope under the stated smallness condition.

The identities R_{i+1}V_i≤(beta²a²)^(-1)V_{i+1} and V_iL_{i+1}≤(beta²a²)^(-1)V_{i+1} are valid without commutation of time matrices. Expanding a whole resolvent product yields the compressed chain bound. The uncompressed alternative is needed only for chains of length at most two in the maximization, so its numerical H-power remains fixed.

The wider active box explicitly includes the positive transfer constraint. This is sufficient to retain resolvent rows because max_{i<L}(u_i+d)+k≤2L−1. It avoids an invalid small-Neumann-ratio argument for the wider backward radius. In the auxiliary homotopy, strict factors on both sides of each arbitrary row defect compress; the active lower density and beta gap give the forward exponent 12L−5. The transfer improvement and backward-radius improvement close simultaneously. Chronological comparison with the inner supersolution keeps the actual coefficients and transfers strictly inside the outer box. The inactive sector is separately controlled by its small backward box and increasing strict forward margins, without dividing by inactive variance.

I independently checked the backward maxima 24,47,66,87 for L3,L4,L5,L6, with k=1,2,3,4. For L≥6 the j=5 term gives 18L−21; all later compressed terms and the top term are no larger. Thus the sufficient M powers are 31,45,63 and 18L−25, giving p_3=31/8, p_4=9/2, p_5=21/4 and p_L=9−43/[2(L+1)]. Every other displayed restriction is weaker than e H_L^100 M^E≤1.

## Conversion and full theorem

The explicit c_L=H_L^(-100)D_L^(-2p_L) gives the last smallness condition directly, since E=2(L+1)p_L. Remaining H powers supply strict tube, endpoint, source and nonaffinity slack even if that last inequality is an equality. For L≤6, D_L<48000 and E/(L+1)<12, with 48000^12<H, so the unchanged old c_poly≤10^(-70)H^(-400) suffices for each improved exponent and consequently for exponent ten.

The finite conditioning proof inspected above extends to any fixed finite L with genuine adjoints on separate generated L2 spaces. At fixed cap, bounded first gate derivatives make the raw vector field locally Lipschitz on a primal ball. The cap-uniform tube therefore gives capped strong solutions and deterministic Euler convergence. In the asymmetric backward comparison the cap R multiplies the already bounded forward-state error only once. The reference subGaussian tails defeat exp(C(1+eR)S), yielding strong cap removal, C1 direction convergence, uniqueness against nonsymmetric bounded-primal competitors, and reached-state restart.

Odd folding and deterministic exchange symmetry give the scalar constructed prediction before uniqueness is invoked. The first-hit inverse clock is global by bounded g', and the actual adjoint identity gives radial convexity and the rate exp(−2a^(2L)delta t). For convex a≥3/4 through L6 this implies the retained weaker exp(−delta t/32).

The ordered finite-program → deterministic mesh → cap argument retains the original finite random readout and actual two-residual raw GF/GD. The fixed-cap velocity proof handles each extra layer by a new clipped product query, removes inner clips with the outer clip fixed, and uses only bounded L2 actions. Its deterministic velocity estimate has a single reference truncation factor. Compactness of the uncut L2 time image permits removal of that factor, and the interpolation estimate upgrades fixed-grid joint laws to same-layer uniform-path W2 laws. Kernels, second moments and integrated speeds then follow from L2 products. There is no growing-transcript or cross-width operator-norm claim.

Finally, positive affine Euler Wick coefficients and uniform integrability give ||x_ell||²≥1; inactive freezing gives marginal variance ≥a^(2(ell−1)). The third-Hermite calculation and the L2-Lipschitz square-root regression residual give the claimed positive eta_L margin. For convex gains through six, the variance exceeds 1/404, retaining eta_*. Full backward second-moment covariance, rather than residual covariance, propagates positivity through every reused transpose and yields every hidden block and sample-layer initial acceleration. The total projected-kernel expansion follows with the stated physical-time factor eight.

No unresolved blocking obligation remains for these exact statements and hashes.
