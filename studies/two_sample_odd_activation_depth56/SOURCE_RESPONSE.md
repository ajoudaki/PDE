# Finite-depth source response, including a wider coefficient box

This note extends the exact chronological source system and derivative cancellation in `two_sample_odd_activation_depth4/SOURCE_RESPONSE.md`. Its affine inputs are explicitly listed below. All statements concern one fixed finite hidden depth L; no simultaneous width/depth limit is asserted.

## 1. Affine interface

Write d=L+1, t=2L-1, u_i=(2i-L-4)_+, and M>1. Let H≥10^100(8L)^L dominate every numerical affine constant, every elementary source coefficient constant, the common beta-gap reciprocal, and the original-forward and initial source norms. Assume on three nested initialization references beta_in<beta_out<beta_far:

* duration S≤H M^d;
* beta gaps ≥H^-1 M^-(L-1);
* local affine resolvent rows R_i,L_i≤H M^t;
* local strict transfer densities V_i=a²R_iK_i≤H M^u_i;
* active lower bound V_i,kj≥H^-2 M^-2d h_j for i<L;
* backward coefficient B_(i+1) rows≤H M^b_i, b_i=4L-1-2i for i<L, while the top readout integrator has row≤HM^d;
* original affine forward fields have bounded second moments H, original delta_i norms≤H M^(L+1-i), and primitive backward Gaussian source zeta_i standard deviations≤H M^(L-i);
* capped nonlinear raw comparison E≤H eM^(2L+2), forward differences≤H eM^(2L+i+1), backward differences≤H eM^(3L+2-i).

Strict density means sup |T_kj|/h_j, causal row means sup sum_j |T_kj|. All bounds include the full two-sample matrix norm. The expected deterministic coefficients diagonalize in mean/contrast sectors; individual random gates are kept as full matrices.

The affine probe identities originate in the L4 affine certificate, Section 9. AFFINE_CERTIFICATE.md here supplies their explicit prefactors and the full interface for all fixed finite depths. In the assembled theorem substitute H_L for this note's H.

## 2. Exact source system and defect powers

For i=2,...,L, introduce forward source xi_i and backward source zeta_(i-1). Exactly as at depth four:

    Z1=Z1_0+H_P delta1,
    Zi=xi_i+A_i delta_i,
    qi=zeta_i+B_(i+1) H_i  (i<L),
    qL=EC, C=H_c H_L,
    H_i=phi(Zi), delta_i=D(Zi,qi).

A_i is strict and B_i causal. Gaussian covariances are the full second moments of the corresponding lower H and upper delta fields. Coefficients are beta² times expected named-slot formal derivatives, plus their learned second moments with the original h_j c_j normalization. The current B_L return is E N_L, and recursively current B_i is E N_i plus B_(i+1),kk E[Vgate_i G_i]. The exact construction order is A2,...,AL,BL,...,B2.

The number of independent initialized matrices is finite. Each initial matrix is conditioned in both orientations; its new query constrains that matrix alone. Thus the existing finite-program conditional projection proof applies literally after changing this finite number, without adding independence between repeated queries.

For any fixed coefficient arrays, let R=(I-a²KB)^-1, L=(I-a²BK)^-1, U=RK, V=a²U. With gate perturbations DeltaG,DeltaV and N=e diag(g'(Z)tau_R(q)), set

    P=N+a DeltaV B+a B DeltaG+DeltaV B DeltaG.

The exact identities are

    J-Jaff=U[DeltaV I_zeta+P J],
    Ddelta-Ddelta_aff=L[DeltaV I_zeta+P J],
    Jaff=R I_xi+aU I_zeta.

No expected derivative is replaced by a derivative of an already expected scalar. Current gates and the full random sample matrices remain in P.

The naive separate-source row estimate is avoidable. The independently proved primal comparison gives the *actual* norms ||Z_i||2≤H and ||q_i||2≤H M^m_i, where m_i=L+1-i (including m_L=1). Freeze the deterministic coefficient arrays and put

    Z_G=R xi+aU zeta,
    q_G=L zeta+aBR xi.

These are centered Gaussian vectors even though the two displayed Gaussian combinations may be correlated. The exact identities are

    Z-Z_G=eU[d+aB h],
    q-q_G=e[aBU d+LB h],
    h=atan(Z), d=g(Z)tau_R(q).

Use |h|≤pi/2, |d|≤|q|, and a²BU=L-I. The first remainder is bounded in L2 by H^6 e[M^(u_i+d+m_i)+M^(u_i+d+b_i)]. The second is bounded by H^6 e[M^(t+m_i)+M^(t+b_i)]. Here b_L=d and otherwise b_i=4L-1-2i. Since

    max_i(u_i+d+b_i)≤5L-2,
    max_i(t+b_i-m_i)≤5L-4,
    max_i(u_i+d+m_i)≤2L+1,

smallness e H^20 M^(5L-2)≤1 implies ||Z_G||2≤H^8 and ||q_G||2≤H^8 M^m_i. A centered Gaussian's p norm is at most its L2 norm times a fixed multiple of sqrt(p). Apply the same two exact identities in Lp. First absorb the q feedback e aBU d using eH^4M^t≤1/2, then use the q bound in the Z identity. This proves

    ||Z_i||p≤H^12 sqrt(p),
    ||q_i||p≤H^12 M^m_i sqrt(p), p≥2.

This reasoning uses the already established raw L2 comparison and deterministic coefficient bounds. It does not assume Gaussianity of Z or q, or any independence between the Gaussian and nonlinear remainders. It is cap and mesh uniform, and gives subGaussian marginal tails by the Gaussian moment criterion.

The strict derivative envelope must still retain the deterministic B-gate terms in P. Thus put w_i=max(m_i,b_i), so w_i=b_i at all populations for L≥3. The exponent of the moment restriction is max_i(u_i+d+w_i)=5L-2. Weighted Jensen and the marginal subGaussian q bounds control the random factor; the deterministic B factors contribute this same polynomial restriction. This is not a pathwise Gaussian maximum.

Consequently every forward defect A_(i+1) has strict density at most H^40 eM^f_(i+1), with

    f_(i+1)=max(2u_i+d+w_i, 2L+i+1), i=1,...,L-1.

Every backward defect J_j has complete causal row at most H^40 eM^Q_j, with

    Q_j=8L-3-2j, 2≤j<L;
    Q_L=5L-1.

These are the powers 2t+w_j. The derivative estimate explicitly bounds all of N J, DeltaV B J, B DeltaG J, and DeltaV B DeltaG J; only the N term uses the sharper q exponent m_i. No unproved cancellation of the other gate terms is invoked.

The learned-moment errors are smaller: forward density eM^(2L+j), backward density eM^(4L+3-2j), hence backward row eM^(5L+4-2j). Their prefactors fit H^40 after enlarging H to absorb fixed-depth sums. The assumed e bound also keeps the nonlinear original forward norms bounded, validating the raw L2 source bounds used above.

## 3. The positive supersolution and elementary chain compression

Fix the beta_in affine coefficients A_i,B_i. Their active entries are nonnegative. Keep A_i*=A_i and recursively, from the top down, set

    B_L*=B_L+J_L,
    B_i*=B_i+[W_i(A_i,B_(i+1)*)-W_i(A_i,B_(i+1))]+J_i,
    W_i=a²B_(i+1)R_i.

All J_i are nonnegative absolute defect majorants. Put Delta_i=B_i*-B_i. At finite mesh all local inverses are finite Volterra polynomials; the construction exists continuously for every scaled defect alpha J, alpha∈[0,1]. There is no hidden denominator assumption.

The exact telescoping resolvent identity is

    Delta_i=J_i+a²L_i Delta_(i+1) R_i*.

Thus the contribution of J_j to Delta_i is a^(2(j-i)) L_i...L_(j-1) J_j R_(j-1)*...R_i*.

Affine positivity gives A_(i+1)≥beta² V_i. Therefore

    R_(i+1)V_i≤(beta²a²)^-1 V_(i+1),
    V_i L_(i+1)≤(beta²a²)^-1 V_(i+1).

If V_i*≤2V_i entrywise, the starred counterparts hold with factor2(beta²a²)^-1≤8. Consequently all strict chains compress, with an overall factor at most8^L.

A useful bound for a chain with no strict factor is obtained by expanding its rightmost resolvent. Since R_i=I+V_i B_(i+1),

    R_j...R_i = R_j...R_(i+1)
                 +R_j...R_(i+1)V_i B_(i+1).

Compress the strict product in the second term, and repeat. This yields

    R_j...R_i ≤ I+8^L sum_(k=i)^j V_j B_(k+1).

The analogous identity holds for L_i...L_j. For starred chains use V_j* and B_(k+1)*. If their local row/density powers are unchanged, this proves the row exponent

    r(i,j)=min((j-i+1)t, u_j+d+b_i).

The factors from sums and compression are bounded by H^4; when using the first, uncompressed alternative below it is needed only for chains of length at most two, costing at most H^4 as well.

## 4. Wider box and noncircular bootstrap

The small-radius box used at L4 was sufficient but is not necessary. Define

    k=min(L-2,4),  r0=H^-20 M^k.

For the auxiliary J-amplitude homotopy impose both

    |Delta_i|_r≤r0,
    V_i*≤2V_i entrywise,  i<L.

Inside this box the original affine resolvent powers persist without a Neumann assumption. Indeed,

    R_i*=I+V_i* (B_(i+1)+Delta_(i+1)),
    L_i*=I+(B_(i+1)+Delta_(i+1)) V_i*.

Their baseline terms are at most twice R_i,L_i. The added row has size at most2H M^(u_i+d) r0. Since

    max_(i<L)(u_i+d)+k≤2L-1=t,

both rows remain bounded by H²M^t. The B_i* row powers also persist because k≤4<b_i. This validates every chain estimate in Section3 on the bootstrap box.

For Delta2, the J_j term has row exponent

    D_j=Q_j+2 min((j-2)t,u_(j-1)+5L-4).

All other Delta_i are bounded by the same maximum D=max_jD_j. Hence |Delta_i|_r≤H^60 eM^D.

For a forward loop V_i Delta_(i+1) V_i, both strict sides compress. On the starred right, first use V_i≤V_i*, then the starred compression, then V_(j-1)*≤2V_(j-1). Thus the J_j contribution has density at most

    H^50 e M^(d+2u_(j-1)+Q_j).

After division by the lower bound on V_i and reserving the beta gap, all forward conditions are implied by

    e H^60 M^(12L-5)≤1.

The maximum follows from 4L+2+2u_(j-1)+Q_j≤12L-5. Direct forward defects need at most power8L-1. In particular V_i Delta_(i+1) V_i≤eta V_i with eta≤1/4, and the finite positive Volterra series implies

    V_i*≤(1-eta)^-1 V_i≤(4/3)V_i.

If e H^82 M^(D-k)≤1, the backward rows improve to |Delta_i|_r≤r0/2. These strict improvements exclude a first exit of the auxiliary homotopy, establishing the supersolution.

For the actual nonlinear coefficient homotopy, include an analogous local-transfer constraint in the outer box: the positive Volterra transfer formed from absolute active arrays must be at most2V_i,beta_out. Besides |A_i|≤A_i,beta_out, require |B_i|≤B_i,beta_out+J_i^out with J_i^out nonnegative of row at most r0. These transfer constraints are continuous at fixed mesh. They imply the same row/density bounds via R=I+VB and L=I+BV, so Section2 applies at a first exit. The supersolution constructed at beta_in then dominates all absolute actual coefficients by chronological induction. It also bounds their positive absolute transfer by at most(4/3)V_i,beta_in, strictly inside2V_i,beta_out. The beta gaps give strict forward entrywise margins proportional to h_j, with no smallest-step requirement. Thus first exit is impossible.

The inactive sector uses a separate *small* backward box. Put Qmax=8L-7 and eta=H^40 eM^Qmax. Give every inactive backward coefficient the row radius r_in=H^10 eta. Give each inactive forward coefficient a fixed increasing strict-density margin (for instance2^i at level i) beyond its reference, absorbed in H. Since

    S H r_in≤H^52 eM^(9L-6)≪1,

all inactive local resolvent rows are≤2, and strict transfer densities are bounded by twice their fixed forward bounds. No active-sector lower bound or wide-transfer condition is used here.

Choose the inactive strict forward coefficients in advance as A_i*=A_i,0+c_i(1+S)eta I, where I_kj=h_j for j<k and c_i=H²(8L)^i. Then construct the backward coefficients by backward finite recursion. The affine inactive backward coefficients vanish. Starting from J_L, the equation B_i*=a²B_(i+1)*R_i*+J_i increases backward row bounds by at most a factor2 at each stage, hence they are≤2^L eta≤H eta. Every forward change is the sum of its direct defect, an inherited preceding forward change, and a term bounded by C S eta from the small reverse coefficients. The chosen increasing c_i dominate these finite inequalities. Induction therefore bounds all forward density increments by (8L)^L H²(1+S)eta≤H^4(1+S)eta. These are strictly below every fixed forward margin, while the reverse rows are strictly below r_in/2. The same estimates also validate the assumed resolvent bound, by first exit or the finite positive Volterra series. Here eH^100M^E≤1 implies the displayed smallness since E≥9L-6 for every depth listed below. This explicit small inactive box closes independently of the larger active backward radius.

## 5. Exponent calculation

For L3:

    (Q2,Q3)=(17,14),
    chain powers=(0,5),
    (D2,D3)=(17,24),
    D=24, k=1, backward power23,
    forward power12L-5=31, hence E3=31.

For L4:

    (Q2,Q3,Q4)=(25,23,19),
    chain powers=(0,7,14),
    (D2,D3,D4)=(25,37,47),
    D=47, k=2, backward power45,
    forward power12L-5=43, hence E4=45.

For L5:

    (Q2,Q3,Q4,Q5)=(33,31,29,24),
    chain powers=(0,9,18,21),
    (D2,D3,D4,D5)=(33,49,65,66),
    D=66, k=3, E=63.

For L6:

    (Q2,Q3,Q4,Q5,Q6)=(41,39,37,35,29),
    chain powers=(0,11,22,26,26),
    (D2,D3,D4,D5,D6)=(41,61,81,87,81),
    D=87, k=4, E=83.

For every L≥6, D=18L-21. The j=5 term attains it. For j=2,3,4 the powers are8L-7,12L-11,16L-15. For j≥5 but j<L, compressed chains give

    D_j≤18L-11-2j+2(2j-L-6)_+≤18L-21.

At the top D_L≤17L-21≤18L-21. Hence

    E_L=18L-25, L≥6,
    E_3=31, E_4=45, E_5=63.

The forward supersolution power12L-5 is smaller at every L≥4; it determines E3. All source values, primal comparisons, gate moments including both B-gate terms, learned defects, forward beta slack and auxiliary homotopies are closed by the single convenient sufficient condition

    e H^100 M^E_L≤1.

If M≤A_L delta^(-1/[2(L+1)]), this becomes

    e≤H^-100 A_L^-E_L delta^p_L,
    p3=31/8, p4=9/2, p5=21/4,
    p_L=9-43/[2(L+1)] for L≥6.

In particular p6=83/14, and the common exponent9 works for every finite depth with this depth-dependent prefactor. This does not prove a depth-independent prefactor or a single fixed activation for all depths. The formula is the sharpest power justified by the displayed ledger, not an optimality claim.

PROOF.md, Section 6, verifies the numerical inequality c_poly H^100 A_L^E_L<1 at L3 through L6, where A_L=D_L^(1/(L+1)); it is a separate constant calculation.

## 6. Excluded sharper ledger

Replacing the old incoming-field exponent by m_i in every derivative term would incorrectly assign Q_i=2t+m_i. The terms L DeltaV B R and L B DeltaG R contain B and are not controlled by this smaller power without an additional argument. The proof above deliberately retains w_i=max(m_i,b_i). An alternative comparison at slope a+e may absorb positive bounded gate changes into a different affine reference, but it is not a premise of this certificate.
