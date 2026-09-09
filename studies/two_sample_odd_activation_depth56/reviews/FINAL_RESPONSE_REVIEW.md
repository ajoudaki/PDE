# Independent complete-proof review: depth 5, depth 6, and fixed finite depth

Reviewer: `/root/depth56_final_response`, 2026-09-07.

**Verdict: PASS for the complete theorem stated in the frozen candidate below.**

This review checked the mathematical chain, including the actual older source/limit dependencies. Earlier author reports and earlier review verdicts were not used as premises. No trajectory experiment was run. The only computation was elementary arithmetic verification of the displayed exponent expressions and numerical affine bounds.

## Exact files reviewed

Directory: `/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth56/`.

| File | SHA256 |
|---|---|
| PROOF.md | `366bf83ff0250a42da9f4f2fae7d51f0dd296cfb2ea3c462761423fec09e8d70` |
| AFFINE_CERTIFICATE.md | `50d09b24de8fe6aa8cbf0d068f71f71596bcefc227c5d745191c69fdcaab095a` |
| SOURCE_RESPONSE.md | `9a05a1b7d4e2075156cb1483c69ed80e7ab02f9fd84de2c6d8a704f2466049b1` |
| POPULATION_AND_MOMENTS.md | `dd49edf52076dce683934f90df58e0ff2362e14fa02c00edd0d2cabd49b43c8b` |
| CONTRACT.md | `e3555b8366f9bdba253f1b0c991f84c1d1bc0082f06131416548646d50ae9207` |

The report applies to these hashes. The final presentation changes concerning the generic H, the delta conversion, the eta constant and the Gaussian textbook edition were inspected.

## Dependencies inspected

I inspected the actual equations and arguments in depth4/SOURCE_RESPONSE.md, depth4/AFFINE_CERTIFICATE.md (balances, normalization, answer probes and general-depth formulas), depth4/POPULATION_AND_MOTION.md, odd_activation_theorem/SOURCE_AND_LIMIT_BRIDGE.md, and the finite Gaussian-conditioning, singular-query and common-action passages of odd_activation_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md. The velocity induction and ordered clip removal were checked in the depth-four bridge and its source/limit bridge, rather than inferred from a historical review.

I also verified the Gaussian norm result in the cited primary textbook: [Vershynin, High-Dimensional Probability, Theorem 7.3.1 and Corollary 7.3.3](https://anthonyhongxiao.github.io/pdfs/HDP-book.pdf), printed pages 167–169. They give the required sharp expectation bound and Gaussian upper tail after dividing the standard Gaussian matrix by sqrt(n). The hypotheses match the initialized square matrices. Passing the high-probability norm bound to countably many generated probes supplies bounded canonical actions, without claiming across-width operator-norm convergence.

## 1. Affine geometry and explicit constants

The normalized active first-root metric is the raw metric; the inactive first-root coordinate has no affine objective contribution. The adjacent operator balances give the displayed bounds with loss at most four at each neighboring Gram comparison. The use of the initialized operator norm in the Cauchy inequality for a matrix block is valid: its gradient is rank one, so its Hilbert–Schmidt norm is the product of its two vector norms.

With w=c^2, d(F^2)/dw=F' and F^2/w tends to one at zero. Integration therefore gives precisely

    F^2 >= c^2(1+c^2) product_{k=1}^{L-1}(1+c^2/(4k)).

There is no integration constant missing at the initially zero readout. Radial convexity supplies c'>=1. Together these estimates justify continuation to the affine endpoint and the intrinsic scale M, with M^(L+1)<=D_L delta^(-1/2).

The star-plus-hidden decomposition of the raw Hilbert Hessian controls the full nonsymmetric tube. The general large-c integrand is L/c plus integrable terms. The explicit numerical early-integral expressions evaluate to approximately 1015.774 at L5 and 5042.329 at L6, within the stated bounds 1100 and 5070; the displayed tail allowance is sufficient. Thus 5100+L log M and the unchanged old H apply through L6. The general beta extension, integrated forcing and probe accounting fit the explicit H_L in PROOF. No exponential in M has been hidden in H_L.

The prediction telescope correctly retains lambda in its affine term. The original forward variables have bounded affine norms because their active component contains r proportional to M^(-(L+1)); the inactive component is frozen. Consequently the improved learned-moment powers are consistent with the raw comparison, rather than obtained by assuming bounded formal response rows in advance.

## 2. Gaussian-part bootstrap and full derivative gates

At the same actual deterministic arrays, direct solution of the affine part gives the two exact Gaussian-part decompositions. The combinations Z_G and q_G are Gaussian because they are deterministic linear combinations of jointly Gaussian named source groups. They may be correlated with each other and with the nonlinear remainders; neither triangle inequalities nor the subsequent absorption uses independence of a remainder.

Write d=L+1, t=2L-1, m_i=L+1-i and u_i=(2i-L-4)_+. The relevant maximum powers are

    max(u_i+d+b_i)=5L-2,
    max(t+b_i-m_i)=5L-4,
    max(u_i+d+m_i)=2L+1.

The cap-uniform raw L2 comparison precedes this step. It first bounds the Gaussian variances using these exact identities. Gaussian moment estimates then apply in every finite Lp, and a^2 BU=L-I bounds the q feedback. The stated e H^20 M^(5L-2) restriction leaves enough numerical slack for absorption and the final H^12 sqrt(p) estimates. These are marginal norms; no random supremum in time is substituted.

Formal differentiation retains

    P=N+a DeltaV B+a B DeltaG+DeltaV B DeltaG.

The two resolvent subtraction identities are exact also for current B returns and the top readout integrator. Exchange diagonalizes the deterministic coefficient blocks only; it does not diagonalize individual random gates. The proof uses full sample-matrix norms for those gates.

For the strict-envelope estimate, a nonlocal B term can be bounded by its complete row times the preceding monotone derivative envelope. Strict U provides the outer h_r sum. Thus arbitrary current or concentrated B coefficients do not need a strict-density bound, and the random q_r factor remains inside a weighted time sum. Weighted Jensen and marginal Gaussian moment bounds control this envelope without a time maximum. The current terminal N factor is covered by the same finite-order Holder bounds.

In particular the deterministic B terms still cost b_i. This gives Q_j=2t+b_j=8L-3-2j below the top and Q_L=5L-1. The learned backward power 5L+4-2j is no larger for L>=3. Replacing b_i by m_i throughout would be invalid, but the frozen candidate does not do so.

## 3. Two-sided chain compression and both coefficient boxes

The forward-reference inequality A_(i+1)>=beta^2 V_i implies both compression orientations by multiplication with R_(i+1) or L_(i+1). The expansion of a resolvent product into an identity plus terms with one strict factor gives the stated minimum of the uncompressed and compressed row powers. The reverse-oriented product is covered by the same algebra.

For the starred system, keeping A fixed and recursively constructing B gives the exact identity Delta_i=J_i+a^2 L_i Delta_(i+1) R_i*. On the simultaneous homotopy constraints, A_(i+1)>=beta^2 V_i*/2; hence the starred right chain compresses as well as the unstarred left chain. The finite Volterra inverses are polynomials, so this argument is not concealing an inverse-radius assumption.

The enlarged row radius is compatible with local resolvent powers because

    max_{i<L}(u_i+d)+min(L-2,4)<=2L-1.

The extra local-transfer boundary in the *actual* active outer box is essential and is present. It makes the source estimates available at a first exit, before comparison with the inner supersolution. The latter gives transfer <=(4/3)V_inner and backward excess strictly below half the row radius, excluding a transfer-boundary exit as well as coefficient-boundary exits.

For each forward loop, the strict factors on both sides of J_j compress. The density bound is e H^50 M^(d+2u_(j-1)+Q_j). Division by the active lower density and reservation of the beta gap adds 2d+(L-1), yielding the maximum 12L-5. The geometric conclusion follows entrywise from V Delta V<=eta V by induction on the finite series; a small complete row of V Delta is unnecessary.

The inactive construction does not borrow that larger active radius. Its affine reverse coefficients vanish, its forward densities have fixed bounds, and its reverse recursion is bounded by B_i*<=2B_(i+1)*+eta, giving at most 2^L eta. The chosen increasing forward increments dominate the inherited increment, the direct defect and the O(S eta) reverse-loop contribution. Their size and the local inverse ratios are controlled by e H^52 M^(9L-6), which the final restriction makes strictly small. No inactive covariance or variance is divided by. Random off-diagonal gate effects have already entered the complete defects, so this scalar-sector comparison does not omit them.

## 4. Exponent and amplitude arithmetic

For L=3,4,5,6 respectively, the maximum backward-excess powers are 24,47,66,87 and the allowed radii have powers 1,2,3,4. Combining their differences with the forward requirement gives E=31,45,63,83. Direct substitution checks every displayed row in the tables.

For L>=6, j=5 attains D=18L-21. The j=2,3,4 expressions are smaller. For later non-top j the positive-part formula has its maximum at an endpoint of either linear branch and is at most 18L-21; the top is at most 17L-21. Hence E_L=18L-25. All source, primal, beta, direct-forward and inactive restrictions are below the final e H_L^100 M^E_L<=1 condition, with spare H powers supplying strict margins.

The conversion c_L=H_L^-100 D_L^(-E_L/(L+1)) is exactly H_L^-100 D_L^(-2p_L). For L3–L6, D_L<48000 and E_L/(L+1)<12, while 48000^12<H. Therefore the actual old c_poly upper bound 10^-70 H^-400 more than suffices at the new exponents. No numerical prefactor was silently replaced for those four depths.

## 5. Complete population/GF/raw-GD conclusions

The underlying conditioning proof actually allows finitely many independent matrices, each repeatedly queried in both orientations. Adaptive conditioning constrains only the queried matrix. Its finite-query perturbation argument handles singular limiting Grams without passing pseudoinverses through rank drops. Thus adding finitely many layers is covered by the proof's hypotheses, not by a theorem title. Countable generated probes and finite transpose identities provide the L separate canonical spaces and all genuine adjacent adjoints; learned increments are Hilbert–Schmidt.

At fixed cap the coordinate maps have bounded first derivatives and linear growth. Bounded actions and the raw ball give locally Lipschitz raw fields, capped strong solutions and deterministic Euler comparison. In the asymmetric backward comparison, only the already controlled forward-state difference is multiplied by R; reversing through further gates multiplies backward errors by bounded actions and bounded gates. This gives one factor 1+eR at every fixed depth. The reference Gaussian tails therefore defeat the comparison exponential, proving strong cap removal, C1 direction convergence, uniqueness against nonsymmetric bounded-primal strong competitors, and reached-state restart on the same action spaces.

Odd label folding and sample exchange give the constructed scalar physical clock. The endpoint is strictly above one; bounded g' makes the inverse clock diverge at its first hit of one. This produces the global physical path. Radial convexity yields g'>=kappa_0>=a^(2L)delta/2 and hence the stated loss rate. No cap-gradient assumption is used for the capped clock.

For width limits, the finite source law is applied only to fixed transcripts. Stopped Euler comparison removes the auxiliary mesh; same-width comparison to the cap reference then removes the cap. Raw GD uses the preceding-node uncut raw direction and a fixed-cap reference consistency error O(n^-2); it needs no width-uniform Lipschitz bound for the uncut field. The actual finite random readout is retained until its O_P(n^-1) RMS limit is taken. The arguments give full-sequence convergence in probability at fixed dataset, depth and finite physical horizon.

The velocity-query induction adds one adjacent initialized forward action at each layer. Each gate product is clipped first, with earlier inner clips removed while the later outer clip is fixed. Bounded initialized L2 actions, derivative-row domination and source-covariance continuity justify removal. The final deterministic comparison truncates only the reference velocity and contains a single truncation factor. Compactness of its L2 time image gives uniform tail removal. This supplies same-layer joint velocity W2 convergence, second moments and integrated speeds. Fixed-grid joint laws plus the stated interpolation inequality supply uniform-norm path W2 laws. L2 products give all L+1 kernels and their off-diagonal entries.

The affine positive-Wick argument has fixed-mesh uniform integrability, so its norm lower bound passes to the strong affine path. Inactive freezing and orthogonality then give variance >=a^(2(ell-1)). The Hermite integral is increasing in the Gaussian scale after the indicated substitution, and the regression square root is 1-Lipschitz by the regression-slope interval [0,1]. The raw preactivation discrepancy gives the claimed positive nonaffinity at every finite physical time.

Finally the top initialization backward Gram is positive definite since phi' is positive and nonconstant. The actual reused transpose conditioning formula, with the *full* upper backward second moment and all derivative responses, propagates conditional covariance positivity down the finite chain. Its positive contraction with the preceding forward Gram gives every hidden block's nonzero acceleration. Adjunction and exchange give both sample-layer accelerations, and the readout-plus-hidden kernel expansion has the stated coefficient 2 in feature time and 8 in physical time.

## Scope of the verdict

The complete theorem is justified at every fixed finite L with the displayed depth-dependent c_L, and with the unchanged old c_poly at L3–L6. The common exponent nine is sufficient with the depth-dependent prefactor. A common positive prefactor for all finite depths, depth-uniform numerical margins or rates, growing-depth width limits, and optimality of these exponents are not established and are not asserted. I found no unresolved mathematical gap in the frozen candidate within its stated scope.
