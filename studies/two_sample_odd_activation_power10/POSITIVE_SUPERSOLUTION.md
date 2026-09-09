# Positive affine supersolutions for the power-10 threshold

2026-09-07. This note proves the deterministic coefficient-closure step. It does not modify the existing theorem files. The nonlinear defect estimate used in Section 6 is the separate response agent's interface; its proof must accompany this note before the complete theorem is asserted.

I read the rigorous-math skill, the quantitative PROOF.md, AFFINE_POLYNOMIAL_BOUNDS.md, and POLYNOMIAL_RESPONSE_LEMMA.md, and the original NONLINEAR_RESPONSE_PERTURBATION.md, TWO_SAMPLE_SOURCE_BASELINE.md, and SOURCE_AND_LIMIT_BRIDGE.md. The exact source equations and their current returns are retained.

## 1. Certificate and notation

Let lambda=a^3 sqrt(v) and M=(3/(sqrt(2)lambda))^(1/4)>1 be the actual dataset's affine endpoint envelope. Then sqrt(v)=3/(sqrt(2)a^3 M^4) and M<=24^(1/4) delta^(-1/8). Constants denoted C below are universal and may increase. In original feature time, the already established safe bounds are

    S <= C M^4,                 v^(-1) <= C M^8,
    |A2_beta|_d, |A3_beta|_d <= C M^7,
    |B2_beta|_r, |B3_beta|_r <= C M^11.

Use three initialization scales 1<beta_in<beta_out<beta_far with every adjacent gap comparable to M^(-2). The affine continuation argument supplies these scales on the same feature interval, with common constants in the displayed bounds. Bounds at sufficiently fine fixed Euler meshes suffice.

For the response proof's source-value estimates we additionally use the certified safe affine transfer bounds

    |F_beta|_d <= C M^5, |V_beta|_d <= C M^7,
    |R1_beta|_r, |R_beta|_r, |L_beta|_r,
       |R3_beta|_r, |L3_beta|_r <= C M^11,
    |B3_beta|_r <= C M^9, |U_beta|_d <= C M^9,

where U=R3 A3, L3=(I-K3 A3)^(-1). These are safe envelopes, not sharp exponents. The affine agent supplies their direct source-injection probe proof, including the enlarged scales. The supersolution algebra below only needs F,V density M^7, R,L rows M^11, and the stronger product estimates in Section 3.

For a strict temporal kernel U, |U|_d=max_{j<k}|U_kj|/h_j; for a causal kernel Q, |Q|_r=max_k sum_{j<=k}|Q_kj|. Every row bound includes current diagonals. All meshes have positive steps; no lower step bound is used. Besides ordinary row submultiplicativity, we use

    |U Q V|_d <= S |U|_d |Q|_r |V|_d.

The coefficient map at unit Gaussian initialization variance is

    T0(A2,A3,B3,B2) = (F,V,T,W),

    F=(I-K1 B2)^(-1)K1,
    R=(I-a^2 A2 B3)^(-1),
    L=(I-a^2 B3 A2)^(-1),
    V=a^2 R A2,
    T=K3(I-A3 K3)^(-1),
    W=a^2 B3 R.

All inverses are finite causal polynomials at a fixed mesh. On nonnegative scalar kernels this map is monotone in every argument. The actual affine coefficients at initialization scale beta obey

    C_beta = beta^2 T0(C_beta) + M_beta,

where M_beta denotes the learned-moment coefficients.

## 2. Why diagonal sample sectors suffice for the full theorem

Fold labels and use constant controls (1/2,1/2). Let P denote sample interchange. The initial sample covariance commutes with P, the scalar readout is unchanged by interchange, and the same activation and cap act in both sample slots.

Induct through the actual finite source program. If the previous deterministic coefficients and Gaussian covariances are invariant under simultaneous interchange, then interchanging every sample-indexed root and named source argument interchanges each newly constructed sample pair, while leaving C unchanged. Its law is invariant because the Gaussian covariances are invariant. A learned covariance block consequently satisfies P M P=M. A formal derivative block transforms as P J P by the ordinary chain rule, with the deterministic arrays and covariances frozen; taking expectation therefore gives P E[J] P=E[J]. This proves invariance of the new coefficient blocks and then of the new Gaussian covariances. The induction starts at the exchange-invariant initial Gaussian pair and zero population readout.

Hence every actual deterministic coefficient block, at every amplitude, cap and fixed mesh, is diagonal in the orthonormal (+,-) basis. This assertion does not say that individual random gates are diagonal in that basis. Those gates can mix the two sectors and must be retained in the nonlinear defect estimate.

The two scalar coefficient sectors may therefore be treated separately. All arbitrary temporal backward forcing in each sector, including current diagonals, remains admissible below. No lemma for externally prescribed off-diagonal sample forcing is claimed or needed. The nonsymmetric physical uniqueness assertion is unchanged: it is proved by the original asymmetric raw-state comparison, not by this source-sector reduction.

## 3. Two products controlled by the positive scaling derivative

All active affine coefficients and learned moments are nonnegative polynomials in beta at a fixed Euler mesh. This is the same Wick-positivity statement proved in POLYNOMIAL_RESPONSE_LEMMA.md. Their beta derivatives are nonnegative.

Write primes for beta derivatives at a scale beta<=beta_out. Differentiating the scaled coefficient equations and retaining only positive terms yields

    A2_beta' >= 2 beta F_beta,
    A3_beta' >= beta^2 a^2 R_beta A2_beta' L_beta
              >= 2 beta^3 a^2 R_beta F_beta L_beta.

Since R_beta,L_beta>=I entrywise,

    F_beta L_beta <= R_beta F_beta L_beta,
    R_beta F_beta <= R_beta F_beta L_beta.

For every polynomial f with nonnegative coefficients and b>beta>=1,

    f'(beta) <= f(b)/(b-beta).

Indeed f is convex and increasing on [1,infinity), so (b-beta) f'(beta)<=f(b)-f(beta)<=f(b). With b=beta_far, the enlarged coefficient certificate and the M^(-2) scale gap give |A3_beta'|_d<=C M^9. Since a>=1/2, we obtain

    |F_beta L_beta|_d + |R_beta F_beta|_d <= C M^9.       (A)

The estimate is much smaller than multiplying the individual density and row envelopes. It is the positive weight which the direct supersolution uses.

In the active sector K1_kj=a^2 v h_j and K3_kj=a^2 h_j. Positivity also gives

    F_beta,kj >= a^2 v h_j >= c M^(-8) h_j,
    V_beta,kj >= a^4 v h_j >= c M^(-8) h_j.             (B)

## 4. Exact supersolution for arbitrary active backward row forcing

Fix beta=beta_in. Suppress beta subscripts temporarily. Let E2,E3 be nonnegative strict kernels of density at most q; let J3,J2 be arbitrary nonnegative causal kernels of row norm at most q. In particular J3,J2 may have nonzero current diagonals.

We prove that the forced unit-variance coefficient system

    C <= T0(C)+M_1+(E2,E3,J3,J2)

in the causal comparison sense is dominated by a concrete supersolution whenever q<=c M^(-32). The same conclusion applies to absolute values of a signed solution: the finite polynomial expansions imply |T0(C)|<=T0(|C|).

Set

    A2*=A2_beta, A3*=A3_beta,
    B3*=B3_beta+J3,
    R*=(I-a^2 A2_beta B3*)^(-1),
    W*=a^2 B3* R*,
    B2*=B2_beta+(W*-W_beta)+J2.                       (C)

Every added kernel is nonnegative. The B3 equation is automatically dominated because T depends only on A3, and

    T_beta+M_1,B3+J3 <= B3_beta+J3.

The B2 equation is dominated exactly because

    W*+M_1,B2+J2
      <= B2_beta+(W*-W_beta)+J2=B2*.

Here we used M_beta>=M_1 and beta^2>=1. There is no approximation of the backward forcing and no replacement by strict densities.

The resolvent identities are

    R*=(I-V_beta J3)^(-1) R_beta,
    W*-W_beta=a^2 L_beta J3 R*.

As |V_beta|_r<=C M^11, the first inverse has row norm at most two whenever C M^11 q<=1/2. Thus (A) gives

    |R* F_beta|_d <= C M^9,
    |R*|_r <= C M^11,
    |W*-W_beta|_r <= C M^22 q.                      (D)

Put D_B=B2*-B2_beta. Then

    F_beta D_B F_beta
      = F_beta J2 F_beta
        +a^2(F_beta L_beta) J3 (R* F_beta).

The first sandwich has density at most C M^18 q, while the second has density at most C M^22 q. Dividing entrywise by the lower bound (B) proves

    F_beta D_B F_beta <= eta F_beta,
    eta=C M^30 q.                                  (E)

If eta<=1/2, the finite geometric expansion yields

    F(B2*)-F_beta <= eta/(1-eta) F_beta <=2 eta F_beta.

For clarity, this follows term by term: (F_beta D_B)^n F_beta<=eta^n F_beta, beginning with (E). No operator inverse norm is paid.

Likewise

    V_beta J3 V_beta <= C M^26 q V_beta,

since its density is at most S(CM^7)^2q=CM^18q and (B) costs M^8. Hence

    V(A2*,B3*)-V_beta <= C M^26 q V_beta.

Finally E2<=C M^8 q F_beta and E3<=C M^8 q V_beta. The affine scaled equations leave forward slack

    A2_beta-(F_beta+M_1,A2) >= (beta^2-1)F_beta,
    A3_beta-(V_beta+M_1,A3) >= (beta^2-1)V_beta.

Since beta^2-1>=c M^(-2), the two forward inequalities hold for q<=c M^(-32), after decreasing the universal c. Thus (C) is a supersolution for all four coefficient equations.

A finite induction through the original order A2_k,A3_k,B3_k,B2_k compares any signed actual coefficient solution to this positive supersolution. Its output bounds are

    |A2_actual|<=A2_beta, |A3_actual|<=A3_beta,
    |B3_actual|<=B3_beta+J3,
    |B2_actual|<=B2_beta+(W*-W_beta)+J2,

and the positive backward excess has row norm at most C M^22 q. This comparison does not require entrywise density bounds for J2 or J3.

## 5. Inactive scalar sector

At the affine inactive reference K3=0, B3_0=B2_0=0, and |A2_0|_d+|A3_0|_d<=C. Both affine backward learned moments vanish. Also K1 has density at most one. The affine learned forward kernels are nonnegative and have bounded density.

For the same arbitrary forcing E2,E3,J3,J2 as above, take

    A2*=A2_0+u H, A3*=A3_0+w H,
    B3*=J3,
    R*=(I-a^2 A2* J3)^(-1),
    B2*=a^2 J3 R*+J2,

where H_kj=h_j for j<k, and u,w are sufficiently large universal multiples of (1+S)q, with the multiple for w larger than that for u.

If C(1+S)q<=1/2 then |R*|_r<=2, |B2*|_r<=3q, and the exact identities

    F*=K1+K1 B2* F*,
    V*=a^2 A2*+(a^2 A2*) J3 V*

give |F*-K1|_d<=C S q and |V*-a^2 A2*|_d<=C S q. The choices of u,w therefore dominate both forward equations. T=0 makes the B3 equation automatic, and B2 was defined to dominate its equation exactly. Consequently

    |B3_actual|_r+|B2_actual|_r <=Cq,
    |A2_actual-A2_0|_d, |A3_actual-A3_0|_d
      <=C(1+S)q <=C M^4 q

in the positive-majorant sense (equivalently, |A_actual| is at most A0 plus the displayed strict kernel). Current diagonals are included throughout.

## 6. Closing the nonlinear source program with q=CeM^43

Use the following explicit interface from the companion nonlinear-response derivation. On the outer coefficient box described below, and for e M^32 sufficiently small, the exact same-array nonlinear derivative defect plus the independently controlled learned-moment discrepancy has

    forward strict densities <=q,
    backward causal row norms <=q,
    q=C e M^43.                                      (F)

The backward norm in (F) contains the actual current returns. It is not restricted to strict past entries. The separate derivation retains both random sample sectors in the local gates, both source and terminal multipliers, and uses exact backward resolvents before taking output norms. Its largest stated term is e M^11 M^21 M^11=e M^43. The learned-moment density e M^15 and its row sum e M^19 are smaller than (F).

The outer box is: active |Aell|<=Aell,beta_out entrywise; active backward positive excess above Bell,beta_out has row norm <=r0=c0 M^(-12); inactive forward absolute kernels are bounded by their affine value plus a fixed strict-density margin; inactive backward row norms are <=r0. This is a box in the diagonal sample coefficient algebra, not a restriction on random gates.

The companion same-array estimates remain valid on this box. For example the active perturbations beyond the positive affine majorant obey

    F<=F_beta_out+F_beta_out J2 F,
    V<=V_beta_out+V_beta_out J3 V,

with |Ji|_r<=r0. The absorption ratios are bounded by S|F_beta_out|_d r0<=CM^(-3) and S|V_beta_out|_d r0<=CM^(-1). R,L and the other source resolvents obey their corresponding identities. The top source resolvents are monotone in A3 and have no backward-coefficient perturbation. Thus the certified M^11 row, M^5/M^7 strict-transfer and subGaussian envelopes persist. The inactive ratios are O(Sr0)=O(M^(-8)).

At fixed cap and mesh the actual source coefficients are continuous under amplitude homotopy te, 0<=t<=1. The affine t=0 program lies in the interior of the outer box. Suppose a first exit occurred. On the closed box, (F) applies. Apply Sections 4 and 5 at beta_in, with the absolute values of the actual defect kernels as the forcing. If

    e<=c M^(-80),

then q<=C c M^(-37). In particular q<=c1 M^(-32) and the active supersolution is valid. Moreover

    active backward excess <=C M^22 q <=C c M^(-15)<r0/2,
    inactive backward norm <=Cq<r0/2,
    inactive forward added density <=C M^4 q<=C c M^(-33),
    active forward coefficients <=A_beta_in<A_beta_out.

After choosing c universally small, every bound is strict relative to the outer box. This contradicts first exit. The argument is uniform in cap, sufficiently fine mesh, and transcript length. It does not use a growing-transcript probabilistic statement.

The exponent arithmetic is therefore

    q exponent:                    43,
    active scale-slack requirement: 32,
    backward outer-box requirement: 22+12=34,
    derivative-moment requirement:  32,
    chosen total exponent:         80 > 43+34=77.

The spare three powers cover the strict outer backward margin; the active supersolution has five spare powers. Since M<=24^(1/4)delta^(-1/8), the single dataset-uniform condition e<=c' delta^10 implies e<=c M^(-80) when c'<=c 24^(-20). This implication uses the correct direction of the endpoint bound; it does not identify sqrt(v) with a power of the dataset-uniform upper envelope. The old primal comparison/nonaffinity restriction e<=c delta^(7/4) is automatic after further decreasing c'.

## 7. Proof boundary

Sections 2-5 give a complete deterministic positive-supersolution argument. Section 6 gives the complete homotopy closure conditional on (F) and the certified affine transfer bounds listed in Section 1. It removes both the generic coupled-inverse cost and the quadratic Taylor remainder from the previous proof. There is no remaining weighted-coefficient inequality to prove once those two companion interfaces are verified.

To promote the complete power-10 theorem, attach the independent derivations of (i) the affine direct-source-injection bounds, including enlarged beta references, and (ii) q<=CeM^43 on the stated outer box. Then the already established cap-removal, physical-clock, nonsymmetric uniqueness/restart, GF/raw-GD, and velocity/path-law bridges apply without any new amplitude restriction. No claim of arbitrary off-diagonal externally forced sample blocks is made.

## 8. Numerical constant ledger preserving every M power

This section replaces the universal constants in the deterministic closure by powers of the old explicitly defined envelope

    H=C_B=10^30(1+C0+Cz+Cg+exp(1410))^4.

In particular H>=10^30, H>=2^20, and 24^20<=H. The affine companion's input certificate is to be read with each coefficient in Section 1 at most H. This is an input requirement, not an assertion that an unspecified constant is dominated by H. The direct source-injection proof must verify it; its elementary probe factors are far smaller than this envelope.

Choose explicitly

    R0^2=200+M^2,
    beta_in =1+1/(10^6 R0^2),
    beta_out=1+2/(10^6 R0^2),
    beta_far=1+3/(10^6 R0^2).

The old affine continuation allows beta-1<=1/(10^5 R0^2), so all three scales are admissible. Since M>1, every adjacent gap is at least (201*10^6)^(-1) M^(-2)>=H^(-1)M^(-2). The same lower bound applies to beta_far-beta_out.

Take the following fully numerical input inequalities:

    S<=H M^4, v^(-1)<=H M^8,
    |Aell_beta|_d<=H M^7,
    |F_beta|_d<=H M^5, |V_beta|_d<=H M^7,
    every displayed affine row bound <=H M^(its stated power),
    inactive affine forward densities <=H.

The active lower bounds (B) can then be weakened to F_kj,V_kj>=H^(-2)M^(-8)h_j, because a^4>=1/16 and H>=16. Convexity and the beta gap give |A3_beta'|_d<=H^2 M^9. The factor (2 beta^3 a^2)^(-1)<=2 is absorbed by one H, giving

    |F_beta L_beta|_d, |R_beta F_beta|_d <=H^3 M^9.

Here is the complete ledger for Section 4. Each row follows by the indicated single product or addition; factors 2,3,6 and 16 are absorbed only where H>=2^20 is used.

| Quantity | Numerical upper bound | Product used |
|---|---:|---|
| V_beta temporal row | H^2 M^11 | S times density |
| (I-V_beta J3)^(-1) row | 2 | require H^2 M^11 q<=1/2 |
| R* F_beta density | H^4 M^9 | 2 times H^3 M^9 |
| R* row | H^2 M^11 | 2 times H M^11 |
| F_beta J2 F_beta density | H^3 M^18 q | H times H times H |
| (F_beta L_beta)J3(R*F_beta) density | H^8 M^22 q | H times H^3 times H^4 |
| F_beta D_B F_beta density | H^9 M^22 q | sum of preceding two terms |
| eta in (E) | H^11 M^30 q | divide by H^(-2)M^(-8)h_j |
| V_beta J3 V_beta relative to V_beta | H^5 M^26 q | H^3 M^18 q times H^2 M^8 |
| E2/F_beta or E3/V_beta | H^2 M^8 q | same lower bound |
| total first-forward relative defect | H^12 M^30 q | 2 eta plus forcing |
| total second-forward relative defect | H^6 M^26 q | twice previous V ratio plus forcing |
| W*-W_beta row | H^3 M^22 q | H M^11 times q times H^2 M^11 |
| either total backward excess row | H^4 M^22 q | preceding term plus J2 or J3 |

Thus the explicit condition

    q<=H^(-16) M^(-32)                               (G)

implies every Neumann ratio is below 1/2 and each forward defect is strictly less than half its available scale slack H^(-1)M^(-2). For example the first-forward relative defect is at most H^(-4)M^(-2), which is below H^(-1)M^(-2)/2.

Set the outer backward excess radius exactly to

    r0=H^(-10) M^(-12).

On this box the F and V absorption ratios are respectively at most H^(-8)M^(-3) and H^(-8)M^(-1). Each affine strict or row envelope in Section 1 therefore increases by at most a factor two, hence is bounded by H^2 times its displayed M power. For L, use L*=L_beta+L_beta J3 V* after bounding V*, rather than multiplying a crude inverse perturbation. R1 uses R1*=R1_beta+F_beta J2 R1*. R uses R*=R_beta+V_beta J3 R*. The top resolvents use monotonicity in A3. These identities justify the same H^2 convention for the outer source estimates without an uncounted product.

The strengthened numerical threshold

    q<=H^(-16) M^(-34)                               (H)

implies (G), and gives total active backward excess <=H^(-12)M^(-12)<=r0/2.

For the inactive supersolution one can take u=H^3 M^4 q and w=H^5 M^4 q. Indeed |A2*|_d<=2H, the R* Neumann ratio is at most 2H^2 M^4 q, |B2*|_r<=3q, |F*-K1|_d<=6H M^4q, and |V*-a^2 A2*|_d<=8H^3 M^4q. The selected u,w dominate these errors and the forcing. Under (H), both added forward densities are below 1/2, and the inactive backward rows are below r0/2. These are numerical inequalities because H>=2^20 and M>1.

The active gap between the inner and outer forward boundaries is also quantitative. Integrating A2_beta'>=2 beta F_beta and A3_beta'>=2 beta V_beta gives, for every strict entry,

    Aell,beta_out,kj-Aell,beta_in,kj
       >=H^(-3)M^(-10)h_j.

This is a strict entrywise margin at every fixed mesh, so the first-exit argument does not rely on an unspecified openness claim or a minimum mesh step.

The separate nonlinear-response ledger reports the following explicit interface on this H^2 outer envelope (its derivation must be attached):

    q<=H^30 e M^43,

with its source-moment/derivative conditions implied by e H^22 M^32<=1. Then the old numerical coefficient

    e<=10^(-70) H^(-400) delta^10

already suffices. In fact M^80<=24^20 delta^(-10) and 24^20<=H, so

    e M^80 <=10^(-70)H^(-399),
    q M^34 <=H^30 e M^77<=10^(-70)H^(-369)<=H^(-16),
    e H^22 M^32<=10^(-70)H^(-377)<=1.

Thus no enlargement of the old numerical coefficient is needed. Its use here is conditional only on the explicit H-prefactor certificates just stated for the affine and nonlinear companion estimates; the deterministic supersolution and first-exit calculation themselves have been fully counted above.
