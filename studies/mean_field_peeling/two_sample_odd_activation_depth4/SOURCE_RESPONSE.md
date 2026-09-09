# Four-hidden-layer source response and positive coefficient closure

This is an independent derivation. No pre-existing proof file is changed. The `solve-math-rigorously` skill was read. Sources checked: `two_sample_odd_activation_power10/{PROOF,REFINED_RESPONSE,POSITIVE_SUPERSOLUTION}.md`; `two_sample_odd_activation_theorem/SOURCE_AND_LIMIT_BRIDGE.md`; and its sources `THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md`, `TWO_SAMPLE_SOURCE_BASELINE.md`, `L3_LOCAL_COMPLETE_PROOF.md` (finite conditioning/common-action passages), and `FIXED_CAP_VELOCITY_BRIDGE.md` (source, derivatives and velocity-query passages).

The result below uses the explicitly stated four-layer affine interface. AFFINE_CERTIFICATE.md proves this interface, with its item-by-item verification in Section 10. The closure already works with the conservative propagator exponent 9; the stronger exponent 4 in that certificate is unnecessary for this closure.

## 1. Exact four-layer source system

Use two label-folded samples, controls c=(1/2,1/2), and a finite positive feature-time mesh (h_j), total length S. Write P=Gamma diag(c), H_P,kj=h_jP for j<k, H_c,kj=h_j c^T, and E=(1,1)^T. Four independent population spaces are used; there is no cross-layer coordinate pairing. At fixed cap define

    phi(z)=az+e atan(z), D(z,q)=aq+e g(z) tau_R(q), g(z)=(1+z²)^−1.

The source equations, with sample slots retained, are

    Z1_k=Z1_0+sum_{j<k}h_j P delta1_j,
    Z2_k=xi2_k+sum_{j<k}A2_kj delta2_j,
    Z3_k=xi3_k+sum_{j<k}A3_kj delta3_j,
    Z4_k=xi4_k+sum_{j<k}A4_kj delta4_j,
    Hℓ_k=phi(Zℓ_k),
    q1_k=zeta1_k+sum_{j≤k}B2_kj H1_j,
    q2_k=zeta2_k+sum_{j≤k}B3_kj H2_j,
    q3_k=zeta3_k+sum_{j≤k}B4_kj H3_j,
    C_k=sum_{j<k}h_j c^T H4_j,
    deltaℓ_k=D(Zℓ_k,qℓ_k) (ℓ=1,2,3),
    delta4_k=D(Z4_k,E C_k).

There are six mutually independent centered Gaussian source groups xi2,xi3,xi4,zeta1,zeta2,zeta3, also independent of the first root. Their full time/sample covariance rules are

    Cov(xiℓ_ki,xiℓ_vj)=E_{ℓ−1}[H^{ℓ−1}_ki H^{ℓ−1}_vj],
    Cov(zeta^{ℓ−1}_ki,zeta^{ℓ−1}_vj)=E_ℓ[deltaℓ_ki deltaℓ_vj], ℓ=2,3,4.

At Gaussian initialization scale beta, both displayed covariances and derivative-only response corrections receive the appropriate beta² initial-matrix factor. All learned moments retain their original raw h_j c_j normalization.

For ℓ=2,3,4 the six exact coefficients are

    Aℓ_ki,vj = beta² E_{ℓ−1}[∂_{zeta^{ℓ−1}_vj}H^{ℓ−1}_ki]
                 + h_v c_j E_{ℓ−1}[H^{ℓ−1}_ki H^{ℓ−1}_vj], v<k,
    Bℓ_ki,vj = beta² E_ℓ[∂_{xiℓ_vj}deltaℓ_ki]
                 + 1_{v<k} h_v c_j E_ℓ[deltaℓ_ki deltaℓ_vj], v≤k.

At actual initialization beta=1. In every formal derivative all arrays, Gaussian covariances, controls, and previous scalar contractions are frozen; named slots remain distinct even for singular source covariances. The original finite readout is unchanged and has zero population limit.

These equations follow by unrolling each of the three trained matrices into its independent initial matrix plus rank-one updates, and applying the finite conditioning rule to all three matrices in both orientations. The conditioning theorem in the cited L3 file is explicitly proved for finitely many independent Gaussian matrices; its conditional projection proof says that a query adds a linear constraint only to the matrix being queried. Thus the new third matrix is covered by that theorem's actual hypotheses, rather than an inference from the file's title.

Let Gℓ=∂_z phi(Zℓ), Vℓ=∂_qD(Zℓ,qℓ), and Nℓ=∂_zD(Zℓ,qℓ). For ℓ=4 use q4=EC. At beta=1 the exact current returns are

    (B4_kk)_ij=1_{i=j} E N4_ki,
    (B3_kk)_ij=1_{i=j} E N3_ki +(B4_kk)_ij E[V3_ki G3_kj],
    (B2_kk)_ij=1_{i=j} E N2_ki +(B3_kk)_ij E[V2_ki G2_kj].

There is no current C dependence on xi4_k, because C uses strictly earlier times. The other two identities include the current higher backward return. All past derivative paths and all learned moments remain present. The chronological construction order is A2_k,A3_k,A4_k,B4_k,B3_k,B2_k.

Exchange equivariance proves that every deterministic coefficient block is diagonal in mean/contrast sample coordinates: induct on this chronological order, interchange all sample-indexed Gaussian roots and named slots, and use invariance of Gaussian covariances, learned contractions, and expected formal derivatives. Individual random gates are full 2×2 matrices in this basis; the estimates below retain their full matrix norms. Physical competitors need not be symmetric.

## 2. Affine interface actually needed

Let v=(1+y1 y2 rho)/2, r=sqrt(v), lambda=a^4r, and

    M=(3sqrt(5)/(2lambda))^(1/5)>1.

The required affine certificate, uniform on common enlarged beta paths and sufficiently fine fixed meshes, is

    S≤H M5, M≤76^(1/5) delta^−1/10,
    beta_in−1, beta_out−beta_in, beta_far−beta_out ≥H^−1 M^−3,
    active primary sizes ≤H M,
    affine variational propagator, including the radius-one tube, ≤H M9.

Here H is exactly the old C_B, not a new free constant. Superscripts M5 etc. denote powers. The normalized homogeneous-degree-five affine proof must establish the H prefactors; the source proof does not infer them from unspecified constants.

For strict U write |U|d=max_{j<k}|U_kj|/h_j; for causal Q write |Q|r=max_k sum_{j≤k}|Q_kj|. The affine transfer certificate needed is

| Quantity | M power, prefactor H |
|---|---:|
| A2,V1 density, full sample norm | 0 |
| A3,V2 density | 1 |
| A4,V3 density | 3 |
| B2,W2 complete row | 18 |
| B3,W3 complete row | 16 |
| B4,W4 complete row | 14 |
| R_i,L_i complete rows, i=1,...,4 | 12 |
| U_i density, i=1,...,4 | 0,1,3,5 |

Definitions are K1=H_P, K_i=A_i for i≥2, local B_i^loc=B_{i+1} for i<4 and B4^loc=EH_c;

    R_i=(I−a²K_i B_i^loc)^−1,
    L_i=(I−a²B_i^loc K_i)^−1,
    U_i=R_i K_i, V_i=a²U_i,
    W_i=a²B_i^loc R_i (i=2,3,4).

The coefficient map is

    (A2,A3,A4,B4,B3,B2)
       =beta²(V1,V2,V3,W4,W3,W2)+learned_moments.

The active sharper forward density powers are −1,1,3, but the full sample bottom bound 0 is used everywhere below. The inactive affine backward coefficients vanish; inactive forward densities are bounded by H. Every active V_i entry is at least H^−2 M^−10 h_j, i=1,2,3.

The source standard deviations in the full sample norm are O(1) for Z1_0,xi2,xi3,xi4 and O(M3,M2,M1) for zeta1,zeta2,zeta3. This uses the special original-variable scaling: active affine forward fields are r times polynomials of degree at most four in primary variables, while r is proportional to M^−5; inactive fields remain fixed. It cannot be replaced by the generic bound H M^ℓ without losing the target ledger.

The independently supplied primal comparison is raw discrepancy ≤H eM15, forward discrepancy at layer ℓ ≤H eM^(ℓ+14), and learned backward density discrepancy ≤H² eM^(24−2ℓ), ℓ=2,3,4. Hence the largest learned backward row defect is H³ eM25. Learned forward defects are smaller. Under eM100 sufficiently small, actual forward-source standard deviations remain O(1).

## 3. The precise coefficient box and local transfer persistence

Take active |A_i|≤A_i,beta_out entrywise, and |B_i|≤B_i,beta_out+J_i with nonnegative causal J_i and |J_i|r≤r0, where

    r0=H^−20 M^−9.

Inactive forward densities have fixed positive slack beyond their affine values; inactive backward rows are ≤r0. On this box all table bounds in Section 2 hold with prefactor H². Indeed, for i=1,2,3,

    V_i*=V_i,b+V_i,b J_{i+1} V_i*,
    R_i*=R_i,b+V_i,b J_{i+1} R_i*,
    L_i*=L_i,b+L_i,b J_{i+1} V_i*.

The largest row norm of V_i,b is HM3 times S≤HM5, so every ratio is at most H^−18M^−1. The last identity, used after bounding V_i*, preserves the L_i power 12. Top transfers depend only on A4 and are dominated by positivity. Inactive ratios are O(Sr0). This proves persistence in the specified box, including arbitrary concentrated or current backward errors; it does not claim such errors have strict densities.

## 4. Same-array source values and exact backward cancellation

For a local population write Z=xi+K delta, q=zeta+B H, H=phi(Z), delta=D(Z,q). Top zeta is zero. Solving the affine part at the actual coefficient arrays gives exactly

    Z=R xi +a U zeta +e U[d+aB h],
    h=atan(Z), d=g(Z)tau_R(q).

Since |h|≤pi/2 and |d|≤|q|, the table gives four inequalities

    Z_i,p ≤H^8 M12 sqrt(p)+ eH^8 M23 Z_i,p.

The exponent 23 is the largest (density U0 +duration5 +backward row18); the other self exponents are 22,22,15. Absorption gives

    ||Z_i,k||p≤H^9 M12 sqrt(p), all four i,
    ||q1_k||p≤H^12 M30 sqrt(p),
    ||q2_k||p≤H^12 M28 sqrt(p),
    ||q3_k||p≤H^12 M26 sqrt(p),
    ||C_k||p ≤H^12 M17 sqrt(p).

These are suprema of deterministic Lp norms over time, never a random time supremum. Power-series expansion gives corresponding subGaussian bounds with prefactor H13.

Freeze arrays/covariances and set J=∂Z, Ixi=∂xi, Izeta=∂zeta. Let

    G=aI+DeltaG, Vgate=aI+DeltaV,
    N=e diag(g'(Z)tau_R(q)),
    P=N+a DeltaV B+a B DeltaG+DeltaV B DeltaG.

Every random gate is kept as a full sample matrix. Exact subtraction of the same-array affine derivative yields

    J−Jaff=U[DeltaV Izeta+P J], Jaff=R Ixi+aU Izeta,
    ∂delta−∂delta_aff=L[DeltaV Izeta+P J].

The second identity follows from ∂delta−∂delta_aff=DeltaV Izeta+P J+a²B(J−Jaff) and L=I+a²BU. It uses no relation between different layers and therefore holds separately at both middle populations. It retains the current N_k J_k term.

Let (u,b,q) be the local powers of U density, B row, and incoming field. They are

    population 1: (0,18,30),
    population 2: (1,16,28),
    population 3: (3,14,26),
    population 4: (5,5,17).

Strict U gives the derivative envelope

    |single transpose J_kj|≤H³ M^u h_j E_k,
    |full forward derivative row J_k|r≤H³ M12 E_k,
    E_k=exp{eH^6 M^u sum_{r<k}h_r(Q_r+H²M^b)}.

The elementary product majorant proves this directly; all feedback through nonlocal B carries the preceding derivative. Weighted Jensen with weights h_r/S and the marginal subGaussian bound controls fixed moments through order eight under

    e H30 M35 ≤1.

The powers u+5+q are 35,34,34,27. In particular the bottom entry is 35, not 34. Deterministic powers u+5+b are 23,22,22,15. Holder gives E[Q_r E_r]≤H14 M^q, including any required source and terminal factors.

For a single transpose source, the expected feature derivative defect density has power 2u+5+q. For a complete forward-source backward output, the exact L identity has power 12+12+q. Thus, after also adding the independent learned moments, one may take

    forward A2 defect d2≤H40 eM35,
    forward A3 defect d3≤H40 eM35,
    forward A4 defect d4≤H40 eM37,
    backward B4 row defect q4≤H40 eM41,
    backward B3 row defect q3≤H40 eM50,
    backward B2 row defect q2≤H40 eM52.

All current diagonals are included. The numerical H40 is conservative: source value absorption costs H8, incoming moments H14, derivative base H3, transfer H2, duration H, and at most two finite sample/gain sums; their product is below H25. The remaining H15 covers learned moments, sums over four populations, and the fixed moment orders. There is no angle-dependent exponential in these prefactors.

## 5. Positive supersolution with individual backward errors

Active affine kernels and learned moments are nonnegative polynomials in beta at fixed mesh. This follows from the same positive Wick recursion as at three layers: every source instruction is linear at e=0; active covariances, constant controls, and chronological coefficients have nonnegative coefficients. The argument is an induction over six stages instead of four.

Fix beta=beta_in and suppress its subscripts. Let J4,J3,J2 be the absolute backward defects, with row bounds q4,q3,q2 above. Freeze the three forward coefficients at the enlarged reference and set

    A2*=A2, A3*=A3, A4*=A4,
    B4*=B4+J4,
    R3*=(I−a²A3 B4*)^−1,
    Delta3=W3(B4*)−W3(B4)+J3,
    B3*=B3+Delta3,
    R2*=(I−a²A2 B3*)^−1,
    Delta2=W2(B3*)−W2(B3)+J2,
    B2*=B2+Delta2.

The exact backward inequalities follow from beta²≥1 and learned_moments_beta≥learned_moments_1. The resolvent differences give

    Delta3=J3+a² L3 J4 R3*,
    Delta2=J2+a²L2 J3 R2*+a4 L2L3 J4 R3*R2*.

No current return has been discarded and no density is assigned to a J.

The ratios |V3|r q4 and |V2|r |Delta3|r are bounded respectively by H42 eM49 and H47 eM71. Under the final smallness condition below they are ≤1/2. Consequently |R3*|r,|R2*|r≤H²M12 and

    |Delta3|r≤H45 eM65,
    |Delta2|r≤H50 eM89.

The powers are 24+41=65 and max(52,24+50,48+41)=89. Retaining the separate top defect exponent 41 is essential for this simple proof. Replacing all q_i by eM52 would unnecessarily yield power 100 in Delta2 before the outer margin.

For the forward equations use A_{i+1}≥beta²V_i and the identities A_i L_i=R_i A_i. They imply entrywise

    V_i L_{i+1}≤V_{i+1}/(beta²a²),
    R_{i+1}V_i≤V_{i+1}/(beta²a²).

Iterating gives, for example, |V1L2|d≤H²M1 and |V1L2L3|d≤H²M3. This is valid because every relevant kernel is nonnegative. It compresses every unstarred strict chain without differentiation in beta.

For any strict U,V and causal J,

    |U J V|d≤ S |U|d |J|r |V|d.

Use the exact expansion for Delta2. The three terms in V1 Delta2 V1 have density powers

    J2: 5+0+52+0=57,
    J3: 5+1+50+12=68,
    J4: 5+3+41+24=73.

For the right factors only |R2*V1|d≤H³M12 and |R3*R2*V1|d≤H5M24 were used. Dividing by the active lower bound V1≥H^−2M^−10h_j proves

    V1 Delta2 V1 ≤eta1 V1, eta1≤H60 eM83.

Similarly V2 Delta3 V2 ≤eta2 V2 with eta2≤H60 eM72, and V3 J4 V3 ≤eta3 V3 with eta3≤H60 eM62. (The larger of the middle J3 and J4 contributions is 5+3+41+13+10=72.)

If eta_i≤1/2, geometric expansion gives V_i*−V_i≤2eta_i V_i term by term, preserving h_j. The forward learned/derivative defects satisfy d_i/V_i≤H42 eM47. Available beta slack is

    A_{i+1}−[V_i+learned_moment_1] ≥(beta²−1)V_i
                                                  ≥H^−1M^−3 V_i.

Hence all forward inequalities hold with strict slack whenever eH63M86≤1 after reserving one additional factor H for halves. Their strongest power is 83+3=86. All signed actual kernels compare to this positive supersolution because |T0(C)|≤T0(|C|), followed through the actual six-stage chronological order.

The outer backward radius r0=H^−20M^−9 is respected with strict slack if

    e H72 M98 ≤1.

Indeed |Delta2|r≤H50 eM89≤H^−22M^−9<r0/2; the other layers are smaller. This single condition also implies all preceding Neumann, moment and forward-slack conditions.

In the inactive sector B4,0=B3,0=B2,0=0 and forward densities are bounded. Choose B4*=J4, B3*=a²J4 R3*+J3, B2*=a²B3*R2*+J2, and successively enlarge A2,A3,A4 by fixed increasing multiples of S max_i q_i times the strict integration kernel. The local ratios are O(S max q_i), so all reverse rows are O(max q_i), and each forward added density is O(S max q_i). For explicit constants H5,H8,H11 on the three forward increments dominate the finite triangular equations. Under eH72M98≤1 these increments are strictly below the fixed forward margins and reverse rows strictly below r0/2.

At each fixed cap and mesh the amplitude homotopy starts at the affine coefficient list. Continuity follows by finite chronological induction and Gaussian square-root continuity, including rank drops. On the first possible exit from the outer box, Sections 3–4 produce the displayed defects, and the supersolution lies strictly inside every boundary. For active forward entries the inner/outer margin is at least H^−3M^−13 h_j, obtained by integrating A_{i+1,beta}'≥2beta V_i and using the beta gap. This avoids any smallest-step assumption. First exit is impossible.

## 6. Same old numerical coefficient and fixed-depth status

Because M100≤76^20 delta^−10 and 76^20<H, the OLD coefficient

    c_poly=min(1/4,c_*,10^−70 H^−400)

implies, for e≤c_poly delta10,

    eM100≤10^−70H^−399,
    eH72M98≤10^−70H^−327<1.

Thus the source/positive-comparison obligations for four hidden layers close with exactly the old coefficient, conditional on the explicit affine H-certificate. The exponent ledger is

    source moment restriction: 35,
    complete derivative defects B2,B3,B4: 52,50,41,
    maximum forward supersolution restriction: 86,
    bottom backward excess: 89,
    outer backward radius exponent: 9,
    total sufficient M exponent: 98<100.

These numerical claims concern L=4. They do not select one coefficient uniformly in arbitrary depth.

## 7. General finite chain and the transfer/limit checks

For arbitrary fixed L the same exact source rules hold for ℓ=2,...,L, with 2(L−1) coefficients, L−1 independent initial matrices, 2(L−1) oriented Gaussian groups, and a single shared C=H_c H^L. The chronological order is all A2,...,A_L then B_L,...,B2. Current returns satisfy

    B_L,kk=E diag(N_L,k),
    (B_i,kk)_ab=1_{a=b}E N_i,ka +(B_{i+1,kk})_ab E[V_i,ka G_i,kb].

The positive backward supersolution is exact for every finite chain:

    Delta_L=J_L,
    Delta_i=J_i+a²L_i Delta_{i+1} R_i*, i=L−1,...,2.

Thus Delta_i is the sum over t=i,...,L of

    a^{2(t−i)}(L_i...L_{t−1}) J_t (R_{t−1}*...R_i*).

Every forward error V_{i−1}Delta_i V_{i−1} retains strict factors on both sides of every arbitrary row error. The entrywise inequality V_jL_{j+1}≤V_{j+1}/(beta²a²) compresses the left strict product for any finite length; the corresponding R inequality compresses unstarred right products. The exact local cancellation in Section 4 also holds at every layer. This proves the algebraic mechanism at general fixed depth, not a depth-uniform numerical coefficient or exponent ledger. Such a ledger needs depth-dependent affine bounds and a fresh summation of the displayed products; the four-layer estimate alone does not establish it.

The required L4 limit bridge has the following checked changes.

1. Finite Gaussian conditioning: the actual theorem covers finitely many independent Gaussian matrices, so three matrices and six oriented groups meet its assumptions. Fixed cap maps have |phi'|≤2, |D_q|≤2, |D_z|≤2eR and linear growth. Singular-query regularization remains a finite-program argument. Common generated spaces use four L² spaces and three adjacent initial actions, with the finite transpose identities giving all three genuine adjoints.
2. Strong cap comparison: forward propagation through four bounded actions/gates is Lipschitz on the primal ball. At each backward gate the asymmetric difference is bounded by 2|Delta q|+2eR|Delta Z|+2e tail_R(q_reference). Induct backwards through four gates. Since Delta Z depends only on the forward state, while Delta q is multiplied by at most a bounded action times 2, the coefficient is C_{b,4}(1+eR), not R raised to the fourth power. The four reference incoming fields have the subGaussian bounds proved above. Hence the cap error is bounded by C exp(C(1+eR)S−cR²), and arbitrary bounded-primal uncut competitors need no tails of their own. This proves uniqueness and restart on the same action spaces once the affine/primal endpoint and symmetry inputs are supplied.
3. Physical clock: sample exchange symmetry and oddness give the same scalar folded prediction g. On an interval with g(0)=0 and g(S)>1, the first-hit argument and bounded g' imply divergence of the physical-time integral at the hit of 1. It depends on the scalar two-sample control, not the number of hidden layers.
4. Width/GF/GD: exact rank-one unrolling adds a third trained matrix increment, bounded by sums of delta^4 times H3 RMS products. On the fixed-cap primal ball, this is the same width-independent finite product estimate as for the other two matrices. Fixed finite meshes, stopped Euler comparison, and ordered width-then-cap limits apply with one extra finite component. Simultaneous raw GD remains Euler in five raw parameter blocks and step n^−2; the finite readout is retained. There is no growing-transcript conditioning invocation.
5. Velocities: append three, not two, queries W2 U1,W3 U2,W4 U3, where P1 is the true first preactivation velocity and

       Pℓ = dot(Wℓ) H^{ℓ−1}+Wℓ U^{ℓ−1},
       Uℓ=phi'(Zℓ)Pℓ, ℓ=2,3,4.

   The rank-one first term is a finite contraction. For the new query at each successive layer, freeze its contractions, truncate the product phi'(Z)P smoothly, apply the finite bounded-derivative source theorem, and remove this truncation using the preceding-layer reference moments. The number of steps is finite. The deterministic comparison inducts through these four chain-rule equations and has C_4[d1+(1+M_trunc)d0+sum_{ℓ,i}||(|P_ref^ℓ_i|−M_trunc)_+||2]. Each layer adds a single truncated reference factor; it does not multiply powers of M_trunc. Take population cap→uncut at fixed truncation then truncation→∞; for empirical laws take width first at fixed cap/truncation. Compact L² time images of uncut reference velocities give uniformly vanishing tails. The same-layer path upgrade follows from the existing deterministic interpolation inequality and integrated speed bounds.
6. Kernel count: there are now five raw kernel contributions (first layer, three hidden matrices, readout). Their contractions converge by the same bounded-action and L²-product identities. Any final L4 theorem must update the count, action list, and hidden-layer velocity/path tuples accordingly.

This source/limit derivation does not itself prove the L4 affine endpoint, activation regression nonaffinity lower margin, initial hidden motion certificates, or a depth-uniform coefficient. Those remain separate obligations; they must not be asserted merely by replacing L3 with L4 in an old theorem statement.

## 8. Optional sharper affine propagator interface

If the affine proof's subsequently obtained radius-one-tube propagator H M4 is independently accepted, the same argument can be shortened further. No change to the source equations or normalization occurs. The substitutions are

| Quantity | New M powers |
|---|---|
| Full forward coefficients and all four local U densities | 0,0,0,0 |
| All local R/L rows | 7 |
| Backward B2,B3,B4 rows | 13,11,9 |
| Z1,Z2,Z3,Z4 subGaussian scales | 8,7,7,7 |
| Incoming q1,q2,q3,C subGaussian scales | 21,18,16,12 |
| Forward coefficient defect densities A2,A3,A4 | eM26,eM23,eM21 |
| Backward complete defect rows B2,B3,B4 | eM32,eM30,eM26 |

The first Z bound is M8, not M7: U1 has full density O(1), so its row is O(M5), and the bottom reverse Gaussian source has scale M3. The value absorption condition has largest power 5+13=18. The derivative envelope moment condition has largest power 0+5+21=26.

Use outer radius r0=H^−20M^−6; every V row is O(M5). Each backward resolvent pair contributes M14. Thus Delta3 has power max(30,14+26)=40 and Delta2 has power max(32,14+30,28+26)=54. The backward interior requires eM60 small. The worst forward sandwich is the top J4 contribution to V1Delta2V1: duration5 +compressed left0 +q4power26 +two right resolvents14 +V1power0 gives density eM45, then the active lower bound costs M10 and beta slack M3, totaling eM58. Hence eH72M60≤1 is a sufficient conservative numerical condition with the same prefactor assignments, much weaker than eM100.

Alternatively, discarding the individual defect powers and using a common q=eM32 would still close by the elementary two-middle row loss M28 plus outer radius exponent6, giving total exponent66. This optional calculation is conditional on the new M4 affine/source-probe certificate; Section 1–7 need only M9 and already prove the required source closure at the old c_poly delta10 amplitude.
