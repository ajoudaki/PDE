# Sector-resolved source response for the square-power mixing bound

2026-09-07. Independent bounded derivation. No old proof is edited. No experiment, commit, or three-input claim is made. The power-four proof and all three mathematical companions, the quantitative affine comparison and polynomial source lemma, and the exact power-ten affine source normalization and response identities were read. The result below is an interface lemma conditional on the weighted affine/outer-box transfer certificate in `WEIGHTED_AFFINE_AND_CLOSURE.md`. It uses the same exact finite source programs and derivative identities as the prior theorem.

The new arguments are: retain the two-time affine propagator in the primal comparison; use the actual active/inactive Gaussian covariance scales in the value equations; and retain sample sectors in the derivative calculation. Random local gates are NOT assumed diagonal in sample sectors. No scalar gain domination of such gates is used.

## 1. Precise interface and conclusion

Write H for the unchanged explicit numerical constant in the power-four theorem, so H>10^30 exp(5640). Let

    r=sqrt((1+y1 y2 rho)/2), lambda=a^3 r,
    M=(3/(sqrt(2)lambda))^(1/4), 1/2<=a<=1.

Thus r is between fixed numerical multiples of M^-4 and the original feature duration S is at most M^4. Write w(t)=sqrt(1+||D_0(t)||^2) on normalized affine time t=lambda s. Its beta enlargements have the same estimates, w>=1 and w<=30M. Work at arbitrary cap and a sufficiently fine positive mesh, taking the existing fixed-program limits in their original order.

The independent weighted closure supplies a deterministic sector-diagonal outer box, with all the following transfer prefactors at most H^40:

| Transfer | Active bound | Inactive bound |
| --- | --- | --- |
| F/a^2=U1 strict density | M^-5 | 1 |
| V/a^2=U2 strict density | M^-3 | 1 |
| Utop strict density | M^-1 | 1 |
| F row | M^-1 | M^4 |
| V row | M | M^4 |
| Utop row | M^3 | M^4 |
| R1 row | M^3 | 1 |
| R2,L2 row | M^4 | 1 |
| Rtop row | M^5 | 1 |
| Ltop row | M^3 | 1 |
| B2 row | M^9 | H^-100 M^-4 |
| B3 row | M^7 | H^-100 M^-4 |

The table deliberately weakens several of the new weighted bounds: the sharper active V row is O(1), and B2 row is O(M^8), but neither improvement is needed here. The top local B is E H_c, with active row at most H^5 M^4 and inactive row zero. All backward rows include current diagonals. Inactive resolvents need only the bounded numerical prefactor H^40.

A sufficient condition for the estimates below is

    e H^200 M^16 <= 1.                                      (1)

Let E2+,E3+ denote active forward strict-density forcing, and J2+,J3+ active complete backward row forcing, after subtracting the exact affine formulas at the actual deterministic arrays. Use minus signs for the inactive forcing. Then the complete forcing, including learned moments, obeys

    E2+ <= H^200 e M^3,    E3+ <= H^200 e M^5,
    E2- <= H^200 e M^13,   E3- <= H^200 e M^11,
    J2+ <= H^200 e M^15,   J3+ <= H^200 e M^12,
    J2- <= H^200 e M^3,    J3- <= H^200 e M.                 (2)

The incoming source fields have cap/mesh-uniform subGaussian scales H^94 M^10, H^94 M^9, H^94 M^7 for q1,q2,C. The derivative exponential moments needed by the old cap-removal bridge are bounded uniformly through order eight. Every constant is numerical and independent of the data, cap, mesh, and width.

## 2. Weighted raw comparison and actual forward/backward norms

The old same-state capped field comparison is

    ||V_e(Theta)-V_0(Theta)||raw <=40 e (R(t)+1)^3,

and its radius-one affine propagator is

    G(t,u)<=exp(2100)[w(t)/w(u)]^3.

All primary affine norms are at most 15w. Variation of constants in normalized time therefore gives

    E(t):=||Theta_e(t)-Theta_0(t)||raw
       <=40(e/lambda) exp(2100) w(t)^3
          integral_0^t [(R(u)+1)/w(u)]^3 du
       <=H^5 (e/lambda) w(t)^3.                            (3)

Here (R+1)/w is numerically bounded and T<2. Condition (1) closes the raw radius-one tube. This comparison is on arbitrary nearby raw states: it does not assume that nonlinear inactive fields freeze. The finite-mesh estimate follows by discrete variation of constants and uniform Riemann approximation on the fixed compact M-dependent interval; all constants remain cap uniform.

The affine inactive Gaussian fields have bounded norms, whereas the active forward fields have norms at most C r w, C r w^2, C r w^3 at the three layers. Hence each affine sample forward field has norm at most H. Direct propagation of (3) gives samplewise forward differences at most H^6(e/lambda)w^3, H^6(e/lambda)w^4, H^6(e/lambda)w^5. Under (1), actual H1,H2,H3 therefore have bounded L2 norms, say H^10.

There is a stronger active estimate. For odd 1-Lipschitz arctan, set

    Psi(P,Q)=[atan(P+Q)+atan(P-Q)]/2.

Then |Psi(P,Q)|<=|P| pointwise, since it is half the difference of atan(Q+P) and atan(Q-P). The first active preactivation is exactly r p_e even in the nearby nonlinear state: projection onto the normalized active input direction has norm at most its raw first-layer norm. Therefore

    ||H1,e,+-H1,0,+||2 <=C r(E+e w)<=H^10 e w^3,
    ||H2,e,+-H2,0,+||2 <=C r(w E+e w^2)<=H^10 e w^4.     (4)

For the second line propagate the first through A_e, compare the affine A_0 action, and again use |Psi|<=|P|. No product of arbitrary unbounded L2 functions is estimated in this step. In particular (1) gives

    ||H1,e,+||2 <=H^10 r w,
    ||H2,e,+||2 <=H^10 r w^2.                            (5)

Indeed the relative error in (4) is bounded by H^10 e M^6, which (1) makes small.

Raw operator bounds and bounded capped gates give

    ||q1||2<=H^10 w^3, ||q2||2<=H^10 w^2, ||C||2<=H^10 w. (6)

Backward contrast has an extra e without any source-tail assumption. The readout C is common to both samples, and

    delta3,- = (e/2) tau(C)[g(Z3,1)-g(Z3,2)],

where g(z)=(1+z^2)^-1 and |tau(q)|<=|q|. Thus ||delta3,-||2<=C e w. Applying B_e^* gives ||q2,-||2<=C e w^2. The exact formula delta2=a q2+e g(Z2)tau(q2) then gives

    ||delta2,-||2<=H^10 e w^2,
    ||delta3,-||2<=H^10 e w.                             (7)

These identities retain the cap and require no Gaussian covariance domination. At each fixed program the actual raw L2 norms are the norms of the corresponding named source output laws, by the original construction.

## 3. Learned-moment forcing

The four learned moments are exactly h_j times the two-time covariances of H1,H2,delta3,delta2, with fixed gain/sample factors already recorded in the prior source normalization. Those factors are bounded by H. For active forward moments, (4),(5) imply

    MA2,+ discrepancy density <=H^30 e r M^4 <=H^35 e,
    MA3,+ discrepancy density <=H^30 e r M^6 <=H^35 e M^2. (8)

For example the first covariance difference is bounded by
C e r[w(t)^3 w(s)+w(t)w(s)^3], using the actual and affine active norms. The second has the analogous powers four and two. The inactive (and full-sample) forward discrepancies satisfy the sufficient bounds H^35 e M^7 and H^35 e M^8, from (3) and the bounded actual forward norms.

Backward differences obey

    ||delta3,e-delta3,0||2 <=H^15(e/lambda)w^3,
    ||delta2,e-delta2,0||2 <=H^15(e/lambda)w^4.             (9)

The second estimate expands B_e^*delta3,e-B_0^*delta3,0 and the bounded gate correction. In particular it uses only bounded operators on L2.

The radial estimates imply

    integral_0^t w <=H,
    integral_0^t w^2 <=H log(exp(1) w(t)),
    integral_0^t w^3 <=H w(t),
    integral_0^t w^4 <=H w(t)^2.                          (10)

They follow by splitting at ||D||=1 and using c'>=c^3/sqrt(2); all are uniform on the common enlarged interval and sufficiently fine meshes.

At fixed terminal t, (9) and the product difference inequality give for the top backward learned row

    H^30 e lambda^-2 [w(t)^3 integral w(s)ds
                     +w(t) integral w(s)^3 ds]
       <=H^35 e M^11.                                  (11)

The integrals here use normalized time. The two lambda^-1 factors come respectively from (9) and original feature-time integration. The middle backward learned row is at most

    H^30 e lambda^-2 [w(t)^4 integral w(s)^2ds
                     +w(t)^2 integral w(s)^4ds]
       <=H^35 e M^12 log(exp(1) 30M)<=H^40 e M^13.           (12)

These estimates hold for either sector and every terminal row. They are stronger than using a supremum density times the whole duration.

For the inactive backward moments use (7), since the affine counterpart vanishes identically. Their rows are at most H^35 e^2 M^6 log(exp(1) 30M)<=H^40 e^2 M^7 at middle, and H^35 e^2 M^5 at top. They are smaller than the inactive bounds claimed in (2) under (1).

## 4. Actual sector Gaussian scales and improved source tails

The primitive Gaussian source covariances are the actual feature/backward L2 covariance matrices. Combining (5),(7) with the initial root gives the following standard deviations, with prefactor at most H^10:

| Source | Active | Inactive |
| --- | --- | --- |
| Z1 initial | r | 1 |
| zeta1 | M^2 | e M^2 |
| xi2 | M^-3 | 1 |
| zeta2 | M | e M |
| xi3 | M^-2 | 1 |

These estimates preserve arbitrary time correlations and singular covariance matrices. They are direct bounds on each Gaussian variable; no covariance square-root derivative or independence between times is used.

The exact same-array source value identities are

    Z1=R1 Z1,initial+(F/a)zeta1
         +e(F/a^2)[d1+a B2 atan(Z1)],
    Z2=R2 xi2+(V/a)zeta2
         +e(V/a^2)[d2+a B3 atan(Z2)],
    Z3=Rtop xi3+e Utop[d3+a E H_c atan(Z3)].              (13)

Here |d_l|<=|q_l| (or |C| at top). Solve the linear Gaussian part separately in each deterministic sector. At bottom the active costs are M^3 r and M^-1 M^2, hence at most M; its inactive cost is 1+e M^6. At middle the active costs are M^4 M^-3 and M M, hence at most M^2; its inactive cost is 1+e M^5. At top the active cost is M^5 M^-2=M^3 and its inactive cost is bounded.

The nonlinear terms may be bounded in the full sample norm. With p>=2, writing Z_l,p for the supremum of the individual Lp norms rather than a random time supremum, the resulting inequalities are

    Z1,p <=H^51 M sqrt(p)+ e H^81 M^13 Z1,p,
    Z2,p <=H^51 M^2 sqrt(p)+e H^81 M^11 Z2,p,
    Z3,p <=H^51 M^3 sqrt(p)+e H^81 M^8 Z3,p.             (14)

The bounded-atan additive terms are covered under (1). For instance at bottom the largest nonlinear self product is the full F row M^4 times B2 row M^9. Each transfer has coefficient H^40, so H^81 covers the product and fixed gains. Gaussian prefactors H^10 and one transfer H^40 fit H^51 after the fixed gains and sums.

Absorption yields Z1,p,Z2,p,Z3,p bounded by H^52 times M,M^2,M^3 times sqrt(p). Substitution into

    q1=zeta1+B2(aZ1+e atan Z1),
    q2=zeta2+B3(aZ2+e atan Z2),
    C=H_c(aZ3+e atan Z3)

gives incoming Lp and subGaussian bounds with coefficient at most H^94 and powers

    q1: M^10, q2: M^9, C: M^7.                          (15)

The subGaussian assertion follows by expanding exp(Q^2/L^2) and using the even-p estimates. It does not assert that an arbitrary bounded L2 action preserves tails.

## 5. Exact derivative equations and a two-sector majorant

For any one local population use

    Z=xi+K delta, q=zeta+B Hfeat,
    Hfeat=phi(Z), delta=Dcap(Z,q),
    R=(I-a^2KB)^-1, U=RK, L=(I-a^2BK)^-1.

The pairs (K,B) are (H_P,B2),(A2,B3),(A3,E H_c). With deterministic arrays and covariances frozen, the exact identities from the old proof are

    J=Jaff+U[DeltaV I_zeta+P J],
    Ddelta-Ddelta_aff=L[DeltaV I_zeta+P J],
    Jaff=R I_xi+a U I_zeta,
    P=Lgate+a DeltaV B+a B DeltaG+DeltaV B DeltaG.         (16)

In original sample coordinates G=aI+DeltaG and V=aI+DeltaV are diagonal gates, and Lgate=e diag(g'(Z)tau(q)). In the mean/contrast basis they need not be diagonal. Every entry of DeltaG,DeltaV has modulus at most C e and every entry of Lgate at time k is at most C e Q_k. The deterministic B,U,R,L are sector diagonal. Thus, writing b=9,7,4 at the three populations, all blocks of P are bounded by the local curvature e Q and causal gate terms e H^40 M^b. Crucially the -- block has the sharper structure

    P-- = Lgate-- + a DeltaV-- B- + a B- DeltaG--
          + DeltaV-- B- DeltaG-- + DeltaV-+ B+ DeltaG+-. (17)

The large B+ enters (17) only with two e factors. This identity retains the full current B diagonal and is valid at every finite mesh.

Let q_sg=10,9,7 be the powers in (15), and put

    I_k=sum_{r<k} h_r[Q_r+H^40 M^b],
    E_k=exp(e H^81 I_k).                                (18)

The intentionally larger H^81 rate covers all full and sector majorants below. By weighted Jensen, the subGaussian scales (15), and S<=M^4, moments through order eight of E_k are at most two under (1). Indeed the largest coefficient before fixed-moment factors is e H^175 M^14: 81+94=175 and 4+10=14. The spare H^25 M^2 in (1) handles every fixed constant. No random supremum over source times is introduced. Also ||I_k||p<=H^96 M^(4+q_sg) sqrt(p), for each fixed p used below.

For completeness, a smaller rate H^45 is sufficient if the factor H^40 multiplying B is kept inside I as written; H^81 is convenient for the moment ledger but must not be charged twice in cross-generation constants. In subsequent cross estimates use this sharper H^45 rate. It comes from U's H^40 coefficient, fixed two-sample sums/gains, and the full causal row bound on B already included in I. The same E in (18) dominates this smaller-rate majorant.

Here is the precise sector estimate for a single transpose source in active sector at slot j. Let u=M^-5 at bottom and u=M^-3 at middle. After padding histories by zeros, the positive running-maximum inequality is bounded by the rank-one two-by-two matrix

    K_u = diag(u,1) [[1,1],[1,1]].

Its scalar increasing clock is e H^45 I_k. The direct source column is bounded by H^45 h_j (u+e u,e). A finite causal product is bounded entrywise by the corresponding matrix exponential; K_u^2=(1+u)K_u and 0<u<=1. Therefore

    |J++,kj| <=H^50 u h_j E_k,
    |J-+,kj| <=H^100 e h_j(1+u I_k) E_k.                (19)

One can verify (19) directly using exp(tK_u)=I+[(exp((1+u)t)-1)/(1+u)]K_u. This is an elementary matrix causal majorant, not a diagonal-gate assumption. Chronological B terms are bounded by their row norms times the past running maximum; strict U supplies h_r and the time ordering. Every single transpose-source term retains h_j and vanishes for k<=j.

At the fixed moments used below, (19) implies cross-derivative bounds H^200 e h_j M^9 at bottom and H^200 e h_j M^10 at middle, with its explicit envelope retained. The explicit coefficient H^196 follows from the displayed H^100 cross prefactor and H^96 clock moment. We use H^196 in the numerical products below; H^200 is only the final rounded interface.

For an inactive full forward-source column, the direct affine derivative has row in the inactive sector at most H^40 and its active part is zero. The same matrix formula, now with no DeltaV I_zeta term, gives

    |J--,k,row| <=H^50 E_k,
    |J+-,k,row| <=H^95 e u I_k E_k.                     (20)

At middle u=M^-3, q_sg=9; at top u=M^-1, q_sg=7. In both cases the cross derivative has fixed-moment size at most H^196 e M^10. Current forward-source identity terms remain in J--; (20) does not discard them.

Finally, for arbitrary full forward-source rows the old scalar majorant gives base H^50 M^4 at middle and H^50 M^5 at top, times E_k. For each pair of times the actual raw L2 bounds (6) and Holder give

    E[Q_r E_k]<=H^12 M^2 at middle,
    E[Q_r E_k]<=H^12 M at top,                         (21)

and H^12 M^3 at bottom. Independence is unnecessary. Products containing a cross derivative use its I_k factor and the fixed source moments (15), with Holder and the available eighth exponential moment.

## 6. Forward derivative forcing

Consider a single active transpose source. In the ++ part of (16), the direct bounded-gate source term is at most C e u h_j. For the diagonal return use (19), (21), and the B+ row. Its expected strict density is bounded by

    C e u^2 S [M^qraw+M^b],

where (u,qraw,b)=(M^-5,3,9) or (M^-3,2,7). These powers are e M^3 at bottom and e M^5 at middle.

For the cross return, use the second line of (19), the source moments (15), and Holder. Its bounds are

    H^350 e^2 M^18 at bottom,
    H^350 e^2 M^20 at middle.                          (22)

The powers are respectively -5+4+10+9 and -3+4+9+10: strict active U, time duration, incoming subGaussian Q (which dominates B), and the first cross generation. Direct offdiagonal source injection and terminal feature gate contributions are smaller. By (1), (22) is at most H^150 e M^2 and H^150 e M^4. Multiplication by the terminal feature gate G adds its diagonal O(e) difference and the offdiagonal e J-+ term; both are covered by the preceding bounds.

Thus active derivative forcing is at most H^180 e M^3 and H^180 e M^5. Adding (8) gives the active E bounds in (2).

For inactive forward forcing, the previous full-sample single-transpose proof is already sufficient. It uses U full density O(1), the raw L2 bound (21), and deterministic B rows, hence gives H^180 e M^13 and H^180 e M^11. The source-envelope premise is now (18), valid under (1). Adding inactive learned forward moments from Section 3 leaves these bounds unchanged. A sharper inactive argument is possible but unnecessary for the closure interface.

## 7. Backward derivative forcing, including current returns

For an active full forward-source row, apply the second identity in (16) before taking norms. At middle L+ has row M^4 and J has base M^4; at top they have powers M^3 and M^5. The bounded-gate terms retain the full B row, and (21) controls the single curvature factor. Consequently

    middle active defect <=H^180 e M^(4+4+7)=H^180 e M^15,
    top active defect <=H^180 e M^(3+5+4)=H^180 e M^12.   (23)

This controls the sum of absolute expected entries by the expected absolute row for each terminal time, then takes the terminal-time supremum outside expectation. No random time maximum is asserted. Learned rows (11),(12) are smaller than (23).

For an inactive forward-source row, L- has bounded row and use (17),(20). The curvature term in P-- J-- costs H^140 e M^2 at middle and H^140 e M at top, by (21). The B- terms cost at most H^140 e because its row is small. The two-offdiagonal diagonal gate term costs H^140 e^2 M^7 at middle and H^140 e^2 M^4 at top.

The remaining cross return P-+ J+- has, by (15),(20), bounds

    H^350 e^2 M^19 at middle,
    H^350 e^2 M^17 at top.                            (24)

Here the cross derivative has power ten, and the final incoming source powers are nine and seven. Under (1), (24) is bounded by H^150 e M^3 and H^150 e M. Thus the inactive backward defects are bounded by H^180 e M^3 and H^180 e M. The quadratic inactive learned rows from Section 3 are smaller.

Equations (17),(20) include j=k: the inactive direct forward-source identity is retained; L includes its identity; all B diagonal terms are included; and U alone is strict. Arbitrary causal row excess may concentrate on an arbitrarily short past step. No minimum step or backward strict-density assumption is used anywhere.

## 8. Numerical ledger and consequence

Here is one consistent rounded ledger accounting for the delivered H^40 transfer prefactors:

| Item | Prefactor sufficient |
| --- | --- |
| Weighted primal norms, actual Gaussian input scales | H^10 |
| Value leading terms; self products | H^51; H^81 |
| Absorbed Z1,Z2,Z3 | H^52 |
| Incoming Lp/subGaussian scales | H^94 |
| Clock fixed moments | H^96 |
| Global derivative exponential rate | H^81 |
| Sharper rate for cross-generation bookkeeping (B coefficient inside I) | H^45 |
| Direct derivative bases | H^50 |
| Single-insertion derivative defects | H^140 |
| One cross derivative, including its clock moment | H^196 |
| Two-insertion defects before amplitude reduction | H^350 |
| Two-insertion defects after e H^200 M^16<=1 | H^150 |
| Learned moments and all final forcing after fixed sums | H^200 |

Every entry comes from the displayed finite products. For example the incoming scale is H^52 times the B-row H^40 plus fixed sums, hence H^94. The global envelope coefficient is H^(81+94)=H^175 before fixed factors and duration, covered by H^200. A cross derivative uses the direct H^50, sharper rate H^45 and clock H^96, fitting H^196. Returning it through U or L (H^40), one incoming source (H^94), and fixed sums gives at most H^335, below H^350. Single-insertion products use at most two H^40 resolvents/transfers, one H^50 derivative base and fixed sums, fitting H^140. Multiplying a two-insertion term e^2 H^350 by (1) removes H^200 and sixteen M powers, leaving e H^150. These numerical margins avoid treating a saturated H^40 prefactor as if it were H.

The independent typed closure criterion is

    M^10(E2+ +E3+) + M J2+ + M^3 J3+
       +E2-+E3-+M^4(J2-+J3-) <=H^-200.                (25)

Inserting (2) gives a left side at most 8 H^200 e M^16. Thus a sufficient single selection is

    8 H^400 e M^16 <=1.                              (26)

It implies the moment/response condition (1) as well. Since M^16<=24^4 delta^-2, the unchanged prefactor

    c_poly=min{1/4,c_*,10^-70 H^-400}

and e<=c_poly delta^2 give 8 H^400 e M^16<=8*10^-70*24^4<1. The numerical factor 24^4 is retained explicitly; replacing it by H would needlessly exhaust the exact H budget.

Once the independent weighted closure proof is attached, (25) excludes every first exit along the cap/mesh amplitude homotopy. The old primal endpoint/nonaffinity hypothesis e<=c_*delta^(7/4) is implied by delta^2. The original cap removal, autonomous global physical flow, nonsymmetric uniqueness/restart, full-sequence GF/raw-GD population limits, kernels/actions/adjoints, same-layer path/velocity laws and moments, and original initial-motion certificates then use exactly their old bridges. No further smallness condition or change of model is introduced.

This interface therefore suffices for both delta^3 and delta^2. Its mathematical boundary is the independent weighted affine/outer-box/typed-closure certificate; no claim is made here about three inputs or exponents below two.
