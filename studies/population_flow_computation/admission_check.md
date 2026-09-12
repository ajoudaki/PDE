# Independent bounded check of the admission certificate

**Verdict: PASS for computable admission, within the assigned established-source contract.** The simultaneous constant in (5) is large enough for N24 and N51. Equations (6)–(12) then give a terminating scalar construction of a positive mesh threshold and law radius, and (13) gives a fixed genuinely nonatomic family inside that radius. This is an internal scientific check, not a promotion review or a practical accuracy certificate.

The candidate's bookkeeping is compressed. The subsidiary estimates below make the size comparison checkable without an unnamed continuity modulus. No central correction to the candidate is required by this check.

## Scope and provenance

Reviewer: scoped agent `/root/admission_check`, 2026-09-12. Read completely:

- `studies/population_flow_computation/admission_route.md`;
- `docs/global_nonlinear.md`, C.4.7, lines 8978–11440;
- the same file, C.4.9 proof unit A and A-supplement.4, lines 13184–13955;
- `docs/NOTATION.md`;
- the required solve-math-rigorously and investigate-conjectures skills, the latter's research-contract and adversarial-audit references, and shared workflow Part 1.

No other study, route, report, history or reviewer verdict was read. Repository status was inspected only for write safety. No training, scientific simulation, numerical integration or certificate evaluation was run. This report is the only written output.

Source SHA-256 values:

| Source | SHA-256 |
|---|---|
| `admission_route.md` | `8d1aeb89e5e162fd6aa33ed72072c9a3958f12e94f5b214c5f1ea52ede3deaab` |
| `docs/global_nonlinear.md` | `7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

Observed HEAD was `b384475316cc0e18bab14438f0140f8f2ede6c9a`; there were concurrent unrelated working changes and no staged paths. None was modified.

The target remains physical GF on [0,40], two hidden tanh layers, unhalved squared loss, mobilities (n,1,n), Gaussian initialized variances (1,1/n,1/n²), and limiting readout zero. Only the learned increment is Hilbert–Schmidt. Both initialized action orientations and all named source history remain present. The sum norm used below controls the stated raw Hilbert norm. Fixed-program width limits precede mesh/comparison refinements as in the supplied established statements. The contained source construction and reference existence results are accepted in the exact forms restated by the assigned sections; their earlier III.F/C.4.5 dependencies were not independently re-reviewed.

## 1. Raw comparison and tail constants

Equation (1) accounts for all three gradient blocks. Write s=x+W_b e for the first-feature difference. Their total difference has coefficients

\[
 (2H_bA_b^2+2H_bA_b+C_b+A_b+2U)s,
 \quad (2H_bA_b+C_b+2H_b+1)k,
 \quad(A_b+1)z,
\]

plus the explicit final input-vector cost A_b C_b e and the lower-gate tail 2τ_U. The upper backward subtraction uses the bounded comparison readout; no L^p action estimate with p>2 enters. The residual difference is at most Pd+(A_bC_bW_b+1)e. Multiplying the gradient/residual subtraction by the physical loss factor two yields (2), including 4R_b times the comparison tail. No term is missing from that subtraction.

For (3), Hölder gives

\[
 \|Q1_{|Q|>U}\|_2
 \le[8(3\sigma^4+D^4)]^{1/4}
       [2e^{-(U-D)_+^2/(2\sigma^2)}]^{1/4}.
\]

The product of the two numerical fourth roots is 2, giving precisely (3). Dependence between the Gaussian and bounded parts is harmless. The separate trivial branch σ+D is valid. These are individual-query tails; the proof does not replace them by a Gaussian-history maximum.

## 2. An explicit intermediary for the bookkeeping

Use H and b_* from (5), and define for this check only

\[
 P=e^{H^8},\qquad X=e^{H^{10}},\qquad
 R=e^{e^{4H^8}},\qquad J=e^{e^{8H^8}}.
\]

H≥10⁶. In particular

\[
 J^{1000}<b_*,\qquad
 e^{b_*^{33}}<C_*.
 \tag{A1}
\]

For the first inequality take logarithms twice and use
8H⁸+log(1000)<H¹². For the second, take logarithms twice and use
log(33)+H¹²<H¹⁶. These comparisons leave more slack than any powers used below.

For every temporary cap B≤B_cl+2 the following explicit estimates follow from the assigned recursions.

| Quantity | Sufficient upper bound |
|---|---|
| D-row absolute sum D₀ | H⁴ |
| N13 normalized lower-pulse moments, orders 1 through 96 | P |
| L⁴ norm of the lower random amplification from N25 | P |
| f_B in N14 | exp(2H⁸) |
| d₀ in N15 | 4H² |
| Pointwise U,C,V derivative row sums and old β density | R |
| N18 named marginal moments through order 96 and the w time-maximum moments | X |
| Passive-input F and β Lipschitz constants needed for transport | J |
| N22 L² field/residual difference coefficient | H¹⁰ |
| L¹² field/gate difference coefficient, with exponent 1/16 | J |
| Normalized reference clock pulse and its deterministic amplification | J |
| Summed normalized L² clock defect divided by h_max | J |

Here is verification of the entries involving exponentials. Since R₀,C₀,T≤H and D₀≤H⁴, the exponent in N13 for p≤96 is at most

\[
 6H^6+768H^6=774H^6.
\]

Together with the prefactor 4H this is below P. N11 applied to the amplification in N25 gives the same bound at the required fourth moment. Then f_B≤exp(2H⁸), and
f_Bd₀T≤4H³exp(2H⁸)<exp(3H⁸). N15–N17, including their polynomial prefactors, are below R. For N18, Q is Gaussian plus a remainder bounded by H⁴, w is its mass-weighted accumulated update plus g, and Z² has a Gaussian part of variance at most one plus a remainder bounded by C₀Tf_B. Each stated moment is below X. A maximum of Q or Z² over source history is never needed.

For the passive-input constants, N7 gives the normalized α Lipschitz coefficient at most (1+2X)P. The F density Lipschitz coefficient is therefore at most

\[
 4XP+2HX.
\]

In N8 multiply the resulting F-row change by the old pointwise derivative-row bound R. The remaining passive gate differences have L² bound at most a fixed numerical multiple of M W|u-v| and multiply the same bounded derivative rows and readout. All resulting terms are bounded by R³exp(H¹²), which is below J. This supplies the coefficient for the active-output transport cost; it is not inferred from a bare β row bound.

Interpolation from L² to L¹² using the L²⁴ bounds has exponent 1/11. Since the data diameter and η≤1 give a distance range bounded by a power of H, weakening to 1/16 introduces only a further power of H. The coefficient remains below J. Bounded gates have the stronger interpolation exponent 1/6. The same-passive-input convention is preserved throughout.

For the clock defect the unspecified numerical C in N33–N34 can be replaced by 6: differentiate N32 and use its displayed hyperbolic bounds, |φ''|≤2φ', and the integrals of 1-s and s(1-s). In particular

\[
 |\partial_pR_h|
 \le6h^2e^{2h|b_0|}(1+h|b_0|)
       (b_0^2|\partial_pw|+|b_0||\partial_pb_0|).
\]

The Gaussian part of b₀ has standard deviation at most 2H² and its bounded part has size at most 2H⁵. Gaussian exponential moments, Hölder, and polynomial Gaussian moments therefore bound the required exponential-polynomial factor in L⁴ by exp(H²⁰). At a later step,
\(\|\partial_pb_0/m_p\|_4\le2R_0D_0P\), and
\(\|\partial_pw/m_p\|_4\le P\).
At the direct step, \(|\partial_pb_0|\le2R_0p_b\) and \(\partial_pw=0\); division by \(m_p=h_sp_b\) leaves h_s, never 1/p_b. Summing \(h_k^2\le T h_{\max}\) gives a total coefficient below exp(2H²⁰)<J. N49 likewise gives a clock-pulse bound below J. Thus the clock-defect entry has an explicit bound independent of slot count and minimum mass.

## 3. Lower forcing, upper rows, and the two constants

Every elementary coefficient or normalized unchanged field used in the lower subtraction is now bounded by J in its required norm. The L⁴ integrating factor is also below J. The forcing has exactly the six types listed in the candidate: direct injection, update coefficient, explicit input vectors, outside gates/Q, D-row discrepancy, and the inside past gate/input. The D-row discrepancy is bounded by E_j plus J times its ordinary state and transport costs. Every unchanged old D coefficient has density at most J h_s p_b.

Hölder uses at most three L¹² factors and the L⁴ amplification. Multiplication by an additional coefficient and each of the at most two time-mass sums costs at most another J. Consequently J⁸ bounds each propagated forcing type including these mass sums; summing the types and the direct contribution is safely covered by J¹². This proves the explicit version

\[
 \frac{\|\max_{j\le k}|v_{j;p}-\bar v_{j;p}|\|_2}{m_p}
 \le J^{12}\left((\eta+e_b)^{1/16}+q^{1/16}
                         +\sum_{j<k}h_jE_j\right).
 \tag{A2}
\]

The past-source transport sum is bounded using
\(\sum_{s,b}h_sp_b e_b^{1/16}\le Tq^{1/16}\).
A row bound without the density estimate would not establish (A2). The candidate explicitly retains that estimate. Summing α over m_p and adding the learned contraction gives, conservatively, J¹⁸G_k for the same-passive F-row difference and J¹⁸(G_k+e_a) at an active output, where

\[
 G_k=(\eta+q)^{1/16}+\sum_{j<k}h_jE_j.
\]

For completeness define N_k to be the active-output mass average of the L² norm of the summed absolute U-row difference, C_k^d the L² norm of the summed absolute C-row difference, and L_k the corresponding active-output V-row average from N29a. Summing N29 first over derivative indices and then averaging its output index yields the following conservative scalar bounds:

\[
 N_k\le J^{19}G_k+J\sum_{j<k}h_jL_j,
\]
\[
 C_k^d\le J^4G_k+J\sum_{j<k}h_jN_j
          \le J^{23}G_k+J^4\sum_{j<k}h_jL_j,
\]
\[
 L_k\le J^{30}G_k+J^{30}\sum_{j<k}h_jL_j.
 \tag{A3}
\]

The first bound uses the F forcing times the barred V row. The second uses coefficient variation, gate variation, and the preceding U row; exchanging its two finite time sums costs at most T. The third uses the C row, the U row times the bounded readout, and the remaining current gate/readout differences times the barred rows. For η+q≤1, the averaged cost η+q is bounded by (η+q)^(1/16). The same equations at a passive output have no e_a cost.

Since G_k is nondecreasing and T≤J, (A3) gives

\[
 L_k\le e^{J^{32}}G_k,\qquad
 E_k\le e^{J^{33}}G_k.
\]

By (A1) these bounds are smaller than the candidate's intermediate b_* powers and final C_*. If η+q≥1, the absolute current upper-row bound from N15–N16 is already below J and covers that case directly. This completes the quantitative N24 check.

For N51, N48 has a deterministic integrating factor below J and a normalized barred pulse below J. Its D-row, coefficient and gate differences cost E_j+Jη_h. The summed defect just checked costs Jh_max. The same counting gives J¹²(η_h+h_max+Σh_jE_j) for the normalized lower pulse difference. Summing source masses and applying (A3) gives N51 with the same C_*. Thus no undefined larger scalar majorant remains necessary.

There is no first-failure circularity in either calculation. At node k all lower updates and clock defects use old Q rows. They produce the current α and F rows. Current upper moments and derivative rows follow from those F rows and old V rows. Only then is the current β row bounded. Current passive slots are paired as distinguished slots; splitting an atom does not multiply the current diagonal.

## 4. Mesh and radius construction

For large U, a(U) is affine while log of the nontrivial branch of (3) has a negative quadratic term. Therefore the left sides of (7) and (10) tend to zero. Enumerating integer cutoffs while refining rigorous exponential intervals until the strict inequality is certified terminates. Equality at one enumerated cutoff does not matter: a later strict solution exists.

Set
\(D_h=Te^{a(U_{cl})T}a(U_{cl})V+TL_0VE_0\).
Equation (8) makes D_h h_max≤χ/4. Equation (7) supplies the other χ/4 from the reference tail, so η_h≤χ/2, and h_max≤χ/4 gives

\[
 \eta_h+h_{\max}\le3\chi/4<\chi.
\]

The clock flow inherits the Gaussian-plus-bounded decomposition through the stated source isometry; passage of the bounded remainder needs only L² convergence and an almost surely convergent subsequence. No rate for that passage is used in the mesh estimate. The N51 induction then has strict discrepancy margin below 1/2.

For q≤ρ, (10)–(11) give η<β/2 and q<β/4, hence η+q<3β/4<β. N24/N31 therefore give a discrepancy strictly below 1/2. The candidate's B_cl+2 temporary cap covers the nearby-law induction and B_cl+1 covers its raw reference anchor. The same-mesh comparison has no omitted mesh floor. The cutoff tails are always on the already bounded reference endpoint.

Positive rational h_*,ρ,d can be selected by enumerating dyadics and certifying the displayed strict upper inequalities. Thus “small enough” in (8), (11) and the choice of d refers to explicit positive scalar bounds, not to an unspecified continuity modulus. A canonical first successful dyadic is an available fully deterministic choice. This report does not claim those dyadics have been materialized.

The final δ_adm=ρ/8 obeys the completion requirement δ<ρ/4. The additional nested radii ρ/4 and ρ/2 satisfy the later C.4.7 hypotheses. No effective finite-width rate is produced or needed for this admission claim.

## 5. Fixed law family and remaining scope

Because d>0 is selected before solver accuracy, every a,b∈[d,2d] stays positive under refinement. The two arc maps are injective on [-1,1], have disjoint images for d<1/100, and transport a nonatomic uniform measure. Both the input marginal and joint law are therefore nonatomic. Labels remain in [-1,1] and vary with arc position.

The within-branch coupling costs a/2+b/2. Correcting the branch probabilities costs at most 4|p-1/2|, so (14) is valid. Midpoint transport on a cell of length 2/N has mean parameter error 1/(2N); multiplying by a+b/2 proves (15). No parameter of the target family shrinks with N or requested accuracy.

The control-total-variation warning is sound for the nonatomic law: its input measure gives zero mass to both axes, so narrowing the arcs does not make its signed control measure close to the atomic reference in total variation. For odd finite midpoint quadratures there are midpoint atoms on the axes; those discrete measures are not literally mutually singular. Their axis masses shrink like 1/N, so this does not supply a uniform refinement admission through CT4 or alter the Wasserstein construction.

The exact local residual recursion (18) is consistent with (2). Its use still requires actual certified curve, tail and residual bounds, including finite-graph integration and covariance/source errors. Nothing in this check certifies an implemented solver at error 0.02 or 0.1, economical Gaussian integration, source compression, or a finite-width rate. Those limitations are already distinguished in the candidate.

**Definite admissibility status:** the displayed construction admits a fixed computably specified nonatomic family in principle. Its quantitative certificate is astronomically conservative. The assigned new admission bridge has no unresolved correctness objection in this check; broader milestone completion and any promotion require their separate complete reviews.
