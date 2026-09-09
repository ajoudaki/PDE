# Power-four closure from the sharpened affine certificate

2026-09-07. Independent bounded derivation. The rigorous-math skill and the assigned power-ten proof, affine-source certificate, positive supersolution, and refined response were read. No repository proof edit, experiment, delegation, or commit was performed. This note proves the deterministic closure and nonlinear response given the exact sharpened affine input in Section 1. The parent supplied its improved affine variational estimate G <= C M^3; this note does not independently prove that estimate.

Write H=C_B for the original explicit numerical constant. In particular H >= 10^30. M always means the intrinsic endpoint scale

    M=(3/(sqrt(2) a^3 r))^(1/4),  r=sqrt(v),  1/2<=a<=1.

Thus r=3/(sqrt(2)a^3) M^-4 exactly. The uniform delta envelope is used only in the final paragraph.

The decisive points are separate active/inactive outer radii, the improved affine strict densities in the active sector, and using the raw primal L2 bound in Holder AFTER bounding the derivative exponential's moments. The latter does not require an improved subGaussian estimate or a covariance perturbation estimate.

## 1. Exact input interface

Use original feature-time steps h_j, strict density |K|d=max_{j<k}|K_kj|/h_j, and complete causal row norm |Q|r=max_k sum_{j<=k}|Q_kj|. Current diagonals of all backward errors are admitted.

The required improved affine certificate, for beta=b1,b2,b3 and beta_far from AFFINE_SOURCE_CERTIFICATE.md Section 8, is the following. Every displayed coefficient is at most H:

    S <= H M^4;
    active |A2|d,|F|d <= H M^-5;
    active |A3|d,|V|d <= H M^-3;
    active |B3|r,|T|r <= H M^7;
    active |B2|r,|W|r <= H M^9;
    |R1|r,|R2|r,|L2|r,|Rtop|r,|Ltop|r <= H M^5;
    active |Utop|d <= H M^-1;
    active |F L2|d,|R2 F|d <= H M^-1.

The inactive forward densities, including Utop, are at most H, and its affine backward arrays vanish; its resolvents are identity. The same probe argument as the existing certificate produces these orders by replacing its G=M^5 by G=M^3. The product bound follows from beta positivity, A3 density M^-3, and beta gap M^-2. The exact top probe, including Ltop, is still required; no product-of-row-norm shortcut is substituted.

The intrinsic beta gaps obey b_(j+1)-b_j >= H^-1 M^-2. Active lower bounds, independent of the sharper upper bounds, are

    F_kj,V_kj >= H^-2 M^-8 h_j.                       (1)

Gaussian source standard deviations remain <=H times 1,M^2,M,M,M^2 for (Z1_initial,zeta1,xi2,zeta2,xi3). The established raw tube supplies

    ||q1_k||2 <= H M^3, ||q2_k||2 <= H M^2,
    ||C_k||2 <= H M.                                 (2)

These follow by applying the actual bounded raw actions: q2=B*delta3 and q1=A*delta2, with all gates bounded, |tau_R(q)|<=|q|, and raw A,B,C bounded by constant times M. They also hold in the fixed-cap, sufficiently fine fixed-mesh source laws, by their existing raw/source identification. Only second moments are used here. The old learned-memory discrepancy remains <= H e M^15 h_j at strict entries, and hence <= H^2 e M^19 in backward row norm.

## 2. The outer box and all source transfers on it

All actual deterministic source coefficient blocks are sample diagonal by the exchange-equivariance induction in POSITIVE_SUPERSOLUTION.md Section 2. Random gates can mix the two sectors; all value and derivative bounds below retain full two-by-two gate norms.

At beta=b2 define the outer box by:

* active |Aell| <= Aell,b2 entrywise;
* active |Bi| <= Bi,b2+Ji entrywise for nonnegative causal Ji with |Ji|r <= ra:=H^-10 M^-2, i=2,3;
* inactive |Aell| <= Aell,1+Htime entrywise, where Htime_kj=h_j for j<k;
* inactive |Bi|r <= ri:=H^-10 M^-5, i=2,3.

Equivalently the active Ji can be the positive part of |Bi|-Bi,b2. No density estimate on Ji is assumed.

On the active majorant, with subscript b denoting beta=b2,

    F=Fb+Fb J2 F, V=Vb+Vb J3 V,
    R2=R2b+Vb J3 R2,
    L2=L2b+L2b J3 V,
    R1=R1b+Fb J2 R1.

The two Neumann row ratios are bounded by

    |Fb|r |J2|r <= H^-8 M^-3,
    |Vb|r |J3|r <= H^-8 M^-1,

because |Fb|r<=H^2 M^-1 and |Vb|r<=H^2 M. Hence active F,V retain strict densities at most 2H M^-5,2H M^-3. R1,R2 retain rows at most 2H M^5. For the reverse resolvent use its exact identity: |L2|r<=H M^5(1+ra |V|r)<=2H M^5. This avoids the invalid claim that a right row multiplier preserves strict density. Rtop,Ltop,Utop depend only on A3 and are bounded directly by monotonicity.

In the inactive sector, A densities are <=2H, while S ri<=H^-9 M^-1. Every relevant Neumann ratio is at most 2H^-8 M^-1; F,V,Utop have bounded strict densities, forward/reverse resolvents have bounded rows, and K3 vanishes. In particular no M^-2 inactive radius is being used.

After the fixed two-sample norm conversion, the following full-sector bounds all have prefactor H^2 (enlarging this to H^3 for gain factors is harmless):

    |F|d,|V|d,|Utop|d <= H^2,
    |R1|r,|R2|r,|L2|r,|Rtop|r,|Ltop|r <= H^2 M^5,
    |B2|r <= H^2 M^9, |B3|r <= H^2 M^7.

Thus the larger active outer radius does not enlarge the source moment or derivative exponents. The inactive radius is separate and remains small enough.

## 3. Positive supersolution with arbitrary backward row defects

For nonnegative forward strict defects E2,E3 of density <=q and arbitrary nonnegative causal backward defects J3,J2 of row <=q, fix beta=b1. Set exactly as in the power-ten proof

    A2*=A2b, A3*=A3b, B3*=B3b+J3,
    R*=(I-a^2 A2b B3*)^-1,
    W*=a^2 B3*R*, B2*=B2b+(W*-Wb)+J2.              (3)

The backward inequalities hold exactly, because the learned affine moments increase with beta and the affine variance multiplier beta^2 exceeds one. All added arrays are nonnegative.

The finite causal identities are

    R*=(I-Vb J3)^-1 R2b,
    W*-Wb=a^2 L2b J3 R*,
    Fb(B2*-B2b)Fb
       =Fb J2 Fb+a^2(Fb L2b)J3(R*Fb).              (4)

The single sandwich inequality used here is

    |U Q V|d <= S |U|d |Q|r |V|d.                  (5)

It follows by expanding the entries and using the strict right factor's h_j. It holds for every positive-step mesh, including arbitrary current diagonals in Q.

Under q<=H^-16 M^-12, |Vb|r q<=H^2 M q<1/2. The numerical ledger is:

| Quantity | Upper bound |
|---|---|
| R* row | H^2 M^5 |
| R*Fb density | H^2 M^-1 |
| Fb J2 Fb density | H^3 M^-6 q |
| (Fb L2b)J3(R*Fb) density | H^4 M^2 q |
| Fb(B2*-B2b)Fb density | H^5 M^2 q |
| eta defined by Fb(B2*-B2b)Fb<=eta Fb | H^7 M^10 q |
| Vb J3 Vb relative to Vb | H^5 M^6 q |
| E2/Fb, E3/Vb | H^2 M^8 q |
| W*-Wb row | H^3 M^10 q |
| either total backward excess in (3) | H^4 M^10 q |

The first five lines use only (4),(5) and the exact active bounds; the relative lines use (1). Since eta<1/2, termwise positivity gives

    F(B2*)-Fb <= [eta/(1-eta)] Fb <=2eta Fb.

Indeed [Fb(B2*-B2b)]^n Fb<=eta^n Fb by induction. No norm of a coupled inverse is inserted. The V expansion gives the corresponding relative increment <=2H^5 M^6q.

The total first-forward relative error is <=H^8 M^10 q, and the total second-forward error is <=H^7 M^8q. Available slack is

    A2b-(Fb+M_A2,1) >= (beta^2-1)Fb,
    A3b-(Vb+M_A3,1) >= (beta^2-1)Vb,
    beta^2-1 >= H^-1 M^-2.

Therefore

    q <= H^-16 M^-12                              (6)

puts both forward errors below half the available slack. This proves (3) is a supersolution. Finite chronological comparison also applies to signed coefficients because |T0(C)|<=T0(|C|).

The inactive proof is unchanged, with

    A2*=A2,1+u Htime, A3*=A3,1+w Htime,
    B3*=J3, R*=(I-a^2 A2*J3)^-1,
    B2*=a^2 J3R*+J2,
    u=H^3 M^4 q, w=H^5 M^4 q.

Under (6) the Neumann ratio is <1/2, backward rows are <=3q, and the forward increments have the stated densities. This construction includes all current backward diagonals.

The supersolution lies strictly inside the outer box. In the active sector its backward excess is <=H^4 M^10q<=H^-12 M^-2<ra/2. In the inactive sector 3q<ri/2 and u,w<1/2. Integrating the positive beta derivatives supplies the entrywise forward margin

    Aell,b2,kj-Aell,b1,kj >= H^-3 M^-10 h_j>0.

These margins hold at each fixed mesh without a lower bound on h_j.

## 4. Full nonlinear response and the raw-L2 improvement

On the outer box the exact value identities in REFINED_RESPONSE.md Section 3 apply. Using the full-sector bounds from Section 2, one obtains

    Z1,p <= H^6 M^6 sqrt(p)+e H^6 M^13 Z1,p,
    Z2,p <= H^6 M^6 sqrt(p)+e H^6 M^11 Z2,p,
    Z3,p <= H^6 M^7 sqrt(p)+e H^6 M^8 Z3,p.

For instance the bottom leading terms cost M^5 and M^4 M^2=M^6, and its self term costs M^4 M^9=M^13. The middle leading terms cost M^5 M=M^6 and M^4 M=M^5; its self term is M^4 M^7=M^11. The top has M^5 M^2=M^7 and self term M^4 M^4=M^8.

Under e H^22 M^19<=1 these self terms absorb. Consequently the incoming fields obey

    ||q1_k||p <= H^10 M^15 sqrt(p),
    ||q2_k||p <= H^10 M^13 sqrt(p),
    ||C_k||p  <= H^10 M^11 sqrt(p), p>=2.            (7)

The corresponding subGaussian scales have prefactor H^11. These are suprema of deterministic Lp norms, not random temporal suprema.

For each local population let R=(I-a^2KB)^-1, U=RK, L=(I-a^2BK)^-1. Here |U|d<=H^3 in all three populations; the full forward-source row and both middle/top backward resolvents have row bound H^3 M^5. The exact derivative identities, including terminal and source current factors, are

    J=Jaff+U[DeltaV Izeta+P J],
    delta_derivative-delta_aff_derivative
         =L[DeltaV Izeta+P J],
    Jaff=R Ixi+aU Izeta,
    P=Lgate+a DeltaV B+aB DeltaG+DeltaV B DeltaG.

Gates satisfy |DeltaG|,|DeltaV|<=Ce and |Lgate_k|<=Ce Q_k. They may mix sample sectors. Strictness of U and the causal product majorant give

    |J_kj| <= H^3 h_j E_k       (single transpose source),
    |J_k,bullet|r <= H^3 M^5 E_k (full forward-source row),
    E_k=exp{e H^6 sum_(r<k) h_r(Q_r+M^b)},

where b=(9,7,4) and the Q subGaussian powers are (15,13,11). Therefore the stochastic integrated exponents are (19,17,15), and the deterministic ones are (13,11,8). The weighted Jensen argument of the existing response proof, with rate H^6, duration H, and subGaussian scale H^11, shows that moments through order eight of E are <=2 whenever

    e H^22 M^19 <=1.                               (8)

At this point use (2), rather than the larger scales in (7):

    E[Q_r E_r] <= ||Q_r||2 ||E_r||2
                  <= H^2 M^qraw,
    qraw=(3,2,1).                                  (9)

If extra terminal or source-time multipliers are retained in a product, use the corresponding higher envelope moments and the available raw fixed moments only when established; they are not needed for the coefficient estimates below. The two exact derivative identities above reduce every coefficient error to a single P insertion and a single derivative envelope. Thus (9), with one Q, suffices. No raw Lp claim beyond L2 is made.

For a single bottom/middle transpose source, the expected defect has density

    e H^20 M^[4+max(qraw,b)],

because the two U density factors carry power zero and time integration costs M^4. Hence the two feature derivative defects have density <=H^21 e M^13 and H^21 e M^11, including the direct source and terminal feature gates.

For the middle/top backward coefficients use the exact L P J identity with Izeta=0 and the complete forward-source row, not a bound on its pieces before solving the backward resolvent. The two row factors cost M^5 each, yielding

    B2 derivative row defect <=H^21 e M^17,
    B3 derivative row defect <=H^21 e M^14.           (10)

The gate-curvature contributions alone are smaller: powers 12 and 11. The dominant terms in (10) are the bounded gate perturbations times the deterministic B row powers 7 and 4. The estimates include j=k. Precisely the estimate is max_k E[sum_{j<=k}|(delta_derivative-delta_aff_derivative)_{kj}|], with the terminal-time maximum outside expectation. It bounds the deterministic coefficient row norm max_k sum_{j<=k}|E[(delta_derivative-delta_aff_derivative)_{kj}]|. No random temporal maximum is taken inside expectation.

Finally add the independently proved learned-memory errors. Their strict densities are <=H e M^15, and complete backward rows <=H^2 e M^19. Thus all four coefficient forcing components satisfy

    q <= H^30 e M^19,                              (11)

under (8), uniformly in cap and sufficiently fine fixed mesh. The old H^30 budget is ample: value absorption uses H^6, derivative rate H^6, envelope base H^3, duration H, and raw-L2 expectation at most H^2; every displayed product and fixed sum fits below H^21 before the final H^30 rounding.

## 5. Homotopy and the delta-only amplitude

At each fixed cap and sufficiently fine mesh, continue the actual source program in amplitude te, 0<=t<=1. It begins strictly inside the outer box. At a proposed first exit, (8),(11) apply, and the exact positive supersolution of Section 3 puts every boundary inequality strictly inside, provided

    H^30 e M^19 <= H^-16 M^-12,
    equivalently e M^31 <= H^-46.                  (12)

This contradicts first exit. The proof retains deterministic sample exchange symmetry, random gate mixing, arbitrary causal backward forcing including current diagonals, and no smallest-step hypothesis.

The existing cap removal, scalar physical clock, nonsymmetric uniqueness/restart, full-width GF/raw-GD, action/kernel/path/velocity laws and initial-motion/nonaffinity bridges now apply once the parent's sharpened affine certificate in Section 1 is attached. The old primal restriction e<=c_* delta^(7/4) is automatic under the proposed delta^4 amplitude.

Indeed M<=24^(1/4)delta^-1/8 implies M^32<=24^8 delta^-4, and 24^8<H. With the unchanged old numerical constant

    c_poly=min(1/4,c_*,10^-70 H^-400),
    e<=c_poly delta^4,

one has e M^32<=10^-70 H^-399. Since M>1, this implies both (8) and (12), with very large strict margins. Thus this closure establishes the complete power-four amplitude once the improved affine input is verified; the deterministic box and nonlinear response have no remaining exponent gap.
