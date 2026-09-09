# Weighted two-sector closure below the fourth-power theorem

2026-09-07. Independent derivation by the closure route. This note changes no old proof, uses no experiment, and makes no three-input claim. The rigorous-math skill, the power-four proof and companions, the power-ten exact affine source certificate and positive supersolution, and the quantitative affine comparison were read. The result is a deterministic source-closure interface. Its final section explains the full-theorem consequences conditional on the stated response and primal inputs.

Write H for the unchanged explicit numerical envelope in the power-four theorem. In particular H > 10^30 exp(5640). Put

    r=sqrt((1+y1 y2 rho)/2), lambda=a^3 r,
    M=(3/(sqrt(2) lambda))^(1/4), 1/2<=a<=1.

Thus r is between fixed numerical multiples of M^-4. Normalized time is t=lambda s, with steps dt_j=lambda h_j. The common normalized endpoint satisfies T<2 and M>1. All deterministic source coefficient blocks are diagonal in the mean/contrast sample basis by the existing exchange-equivariance proof. Individual random gates need not be diagonal.

## 1. Weighted affine certificate from the existing actual probes

Fix one of the same beta references as in the power-four theorem and write

    w(t)=sqrt(beta^2+||D_beta(t)||^2).

It is nondecreasing, at least one, and at most 30M on the common interval. The already proved two-time raw propagator is

    G_beta(t,s) <= exp(2100) [w(t)/w(s)]^3.

The exact independent-root source probes from the old source certificate are used here. An injected answer at time s costs its local raw norms at s; its output Lipschitz cost uses the raw norms at t. Every primary norm is at most 15w. Therefore, in the active normalized source algebra, the following strict-density bounds hold with one numerical coefficient K=H:

    F(t,s) <= K w(t)^3/w(s)^3;
    V(t,s), W(t,s) <= K w(t)^4/w(s)^2;
    T(t,s) <= K w(t)^3/w(s)^3;
    B3(t,s) <= K [w(t)^3/w(s)^3+w(t)w(s)];
    (R-I)(t,s), (L-I)(t,s) <= K w(t)^4/w(s)^2.       (1)

A notation such as F(t,s) denotes F_kj/dt_j for j<k. Each resolvent has its current identity. For example, the middle transpose probe has injection cost C w(s) and Ap output cost C w(t); the middle forward probe has the same costs with B*D as output. R and L use precisely these same probes with their alternative output, as in the existing certificate. T has unit injection/output costs. The B3 learned-moment density is E[D_t D_s], bounded by w(t)w(s). Hence (1) is about the actual frozen formal source derivatives, not a generic raw tangent substituted for them.

The constants are numerical: the old 4 exp(2100) Euler/probe factor, products of local bounds 15w, fixed two-sample changes of basis, gains in [1/2,1], and moment additions are below H. K=H also leaves room for all the elementary integrals below. No covariance derivative or covariance square root is differentiated.

The radial inequality c'>=c^3/sqrt(2) after c=1, homogeneity, and duration T<2 give

    integral_0^t w(u) du <= K,
    integral_0^t w(u)^2 du <= K log(e w(t)),
    integral_0^t w(u)^4 du <= K w(t)^2,
    integral_s^T w(u)^(-2) du <= K w(s)^(-4).        (2)

For the last estimate, if c(s)>=1, use w>=c and dt<=sqrt(2)c^-3 dc to integrate c^-5, then compare w(s) and c(s) by a factor at most two. If c(s)<1, the part up to c=1 has duration at most two, the remaining tail is bounded, and w(s)<=2. The other three statements split at c=1 and integrate c^-2, c^-1 and c respectively. All numerical constants are less than K.

The same inequalities, enlarged by a factor two absorbed in K, hold for sufficiently fine positive Euler meshes. For each fixed M the continuous weights are positive and continuous on a compact interval, so all tail Riemann sums in (2) converge uniformly in their lower endpoint. The mesh may depend on M and beta, but no lower bound on any positive step is used. The finite-program width limit is still taken at fixed mesh.

The current-plus-strict resolvent row estimates following from (1),(2) are

    |R_t|row, |L_t|row <= K^2 w(t)^4.              (3)

The bottom resolvent has row <=K^2 w(t)^3 from its own old coordinate probe (injection w(s)^2, output one). No improvement to the top forward row is asserted: it can have order M^5. None is needed in this deterministic closure.

### Full weighted source-transfer interface

The additional old coordinate probes give the following normalized strict densities and complete row bounds, with fixed coefficients at most K^2:

| Transfer | Strict density | Complete row |
|---|---|---|
| R1-I | w(t)^3/w(s) | R1: w(t)^3 |
| R2-I, L2-I | w(t)^4/w(s)^2 | R2,L2: w(t)^4 |
| Rtop-I | w(t)^5/w(s)^3 | Rtop: w(t)^5 |
| Ltop-I | w(t)^3/w(s) | Ltop: w(t)^3 |
| Utop=Rtop A3 | w(t)^5/w(s) | Utop: w(t)^5 |

For R1, add an independent Gaussian field to the first preactivation before its forward calls: the raw update insertion cost is C w(s)^2 and the p output cost one. For Rtop, the xi3 answer injection costs one and the BAp output costs C w(t)^2. For Ltop, inject the top backward answer used in d3, with update cost C w(s)^2, and observe the integrated D state; the current source derivative is identity. The same top-backward probe with BAp output gives Utop and no current identity. These are exactly the old permitted independent-root probes, now with their time-dependent costs retained.

In original feature time, active forward-transfer rows consequently obey

    F row <=K^3 r w(t)^3,
    V row <=K^3 r w(t)^4,
    Utop row <=K^3 r w(t)^5.                       (3a)

The active backward coefficient rows obey

    B3 row <=K^3 r^-1 w(t)^3,
    B2 row <=K^3 r^-1 w(t)^4.                     (3b)

The B3 moment uses integral w<=K. The B2 moment is bounded by w(t)^2 integral w(s)^2 ds<=K w(t)^2 log(e w(t))<=C K w(t)^4. All current identities are retained separately in resolvents. Inactive baseline resolvents are identity, all inactive baseline backward coefficients vanish, and inactive F,V,Utop have bounded original strict density and row at most K M^4.

The coefficient arrays A2,A3 also have their learned moments, so their normalized strict densities are respectively bounded by

    K [w(t)^3/w(s)^3+w(t)w(s)],
    K [w(t)^4/w(s)^2+w(t)^2 w(s)^2].              (3c)

On the outer box of Section 3, R1,R2,L2 and F,V retain these weighted rows and the corresponding strict weights by the displayed exact resolvent identities. Top Rtop,Ltop,Utop only depend on the forward A3 bound and are bounded by the beta2 baseline. Backward coefficient excess R_a adds at most H^-100 M^3 to (3b). Since r^-1 is bounded below by a numerical multiple of M^4 and w(t)>=1, this excess is dominated even by the pointwise right sides of (3b). Thus the weighted incoming source-row bounds persist as well as their global M^7,M^8 consequences. Inactive perturbed forward/transpose transfer rows are O(M^4), and its forward/backward resolvent rows are O(1). A causal inactive backward excess can include current diagonals and need not have a strict density.

## 2. Two weighted products replace the beta-derivative bound

In the normalized active algebra all gain factors cancel. The exact identities are

    L=I+B3 V,  R=I+V B3,
    F L=F+F B3 V,  R F=F+V B3 F.                  (4)

They hold for the full causal arrays, including the identity returns. Every coefficient in the affine reference is nonnegative. Inserting (1) in the first triple product yields the two integrands

    K^3 [w(t)^3/w(s)^2] w(q),
    K^3 [w(t)^3/w(s)^2] w(u)^(-2) w(q)^5,

integrated over s<q<u<t. The first integral is bounded by T integral w <=2K. In the second, reverse the nonnegative sums/integrals and use

    integral_q^t w(u)^(-2) du <= K w(q)^(-4),

then integral w <=K. Thus

    (F L)(t,s) <= K^6 w(t)^3/w(s)^2.              (5)

For V B3 F the two integrands are

    K^3 [w(t)^4/w(s)^3] w(u),
    K^3 [w(t)^4/w(s)^3] w(u)^(-1) w(q)^4.

Integrate the first directly. In the second use integral_0^u w(q)^4 dq<=K w(u)^2, then integral w<=K. This proves

    (R F)(t,s) <= K^6 w(t)^4/w(s)^3.              (6)

Equations (5),(6) are much stronger than the old endpoint density M^7. The proof explicitly retains the learned-moment part of B3; dropping that part would give an unjustified estimate.

## 3. Weighted stability permits a larger active outer radius

Use the same inner/outer beta scales beta1,beta2 from the power-four proof. At beta2 impose the forward inequalities |Aell|<=Aell,beta2. For active backward kernels impose

    |Bell| <= Bell,beta2 + Jell,
    Jell>=0 causal, |Jell|row <= R_a:=H^-100 M^3.  (7)

For the inactive sector impose its affine forward baseline plus density one and backward row radius

    R_i:=H^-100 M^-4.                             (8)

The old source box had smaller radii. The point is to prove all transfer estimates directly on this larger box.

Normalized backward excess scales as

    J2_hat=(r/a) J2,  J3_hat=ar J3.

Thus every normalized excess row is at most 2r R_a. The positive reference resolvent identities imply

    F*=F_b+F_b J2_hat F*,
    V*=V_b+V_b J3_hat V*,
    R*=R_b+V_b J3_hat R*,
    R1*=R1_b+F_b J2_hat R1*.

For F* use the weight w(t)^3/w(s)^3. The new weighted Neumann ratio is bounded by C r R_a T: the factor w(v)^3/w(u)^3 is at most one when v<=u. For V*, use weight w(t)^4/w(s)^2. Its ratio is bounded by

    C r R_a integral_0^T w(u)^2 du
       <=H^40 r R_a log(e 30M).                  (9)

The same ratio controls R* with row weight w(t)^4. Since r<=C M^-4 and log(e 30M)<=C M, (7) makes both ratios smaller than H^-50. Hence the weighted F,V,R,R1 bounds remain at most twice their affine values.

The reverse resolvent is treated with its exact one-sided identity

    L*=L_b+L_b J3_hat V*.

Using the identity-plus-strict decomposition of L_b, the causal bound w(v)<=w(u), and (2) gives row <=2K^2 w(t)^4 after fixed powers of K are enlarged to H^40. The same computation gives its strict-density weight w(t)^4/w(s)^2; the arbitrary current diagonal of J3 is permitted because the right factor V* is strict. This does not assume that multiplication by an arbitrary right row kernel preserves density.

Top transfers depend only on A3 and remain bounded by monotonicity. The active original F and V densities remain respectively O(M^-5) and O(M^-4), hence bounded by the older power-four envelopes. Backward excess R_a=H^-100 M^3 is below their original active baseline envelopes M^9 and M^7. Therefore every full-sample source transfer bound used in the power-four response proof remains valid (indeed several improve).

For the inactive sector, its integration duration is O(M^4), its baseline forward densities are bounded, and (8) gives a Neumann ratio below H^-50. Its old bounded strict transfers and identity-scale resolvent rows therefore persist.

This proves that (7),(8) are legitimate outer boxes for the existing source moment/derivative proof. Every affine or outer-box transfer inequality in Section 1, including (3a),(3b), may be delivered to the response calculation with the single common numerical prefactor H^40; the underlying products above are strictly below that envelope. The final response lemma must count that prefactor explicitly. It does not assume that the random gates preserve either sector.

## 4. Exact supersolution with distinct forcing types

Let E2+,E3+ denote bounds on active forward strict-density defects in original feature time, and J2+,J3+ bounds on active complete causal row defects. The minus superscripts denote the analogous inactive defects. The defects may be signed; take their absolute values before the comparison. Backward current diagonals are included.

Use exactly the old positive supersolution at beta1:

    A2*=A2_b, A3*=A3_b, B3*=B3_b+J3,
    R*=(I-a^2 A2_b B3*)^-1,
    W*=a^2 B3* R*,
    B2*=B2_b+(W*-W_b)+J2.                         (10)

The backward inequalities hold exactly by affine beta positivity and beta^2>=1. The only forward increments to estimate are

    F_b J2 F_b,
    a^2(F_b L_b) J3 (R*F_b),
    V_b J3 V_b,

plus E2,E3.

We first bound R*F_b in normalized coordinates. From

    R*F_b=R_bF_b+V_b J3_hat(R*F_b),

and (6), its weight w(t)^4/w(s)^3 is stable when

    H^40 r J3+ log(e 30M) <=1/2.                 (11)

Indeed a causal J3_hat row is at most 2r J3+, and its right argument at v<=u has weight at most w(u)^4/w(s)^3. The remaining integral is integral w(u)^2 du. Thus (6), with twice its constant, applies also to R*F_b.

For the J2 sandwich, the same causal ordering gives in normalized density

    |F_hat J2_hat F_hat|(t,s)
      <=H^40 r J2+ w(t)^3/w(s)^3.                (12)

The integration over its first time variable costs only T<2, because w(v)^3/w(u)^3<=1. For the J3 sandwich, use (5),(6) to get

    |(F_hat L_hat) J3_hat(R*F_hat)|(t,s)
      <=H^40 r J3+ [w(t)^3/w(s)^3] log(e w(t)).   (13)

The remaining integral is integral w(u)^2 du. These estimates apply unchanged to an arbitrary current diagonal in J2 or J3.

Converting a normalized F-type strict density to original time multiplies by a numerical factor times r^2. As w(t)<=30M and w(s)>=1, (12),(13) therefore imply

    |F J2 F|density <=H^40 M^-9 J2+,
    |(FL) J3(R*F)|density
       <=H^40 M^-9 log(e 30M) J3+.               (14)

The old active lower bounds F_kj,V_kj>=H^-2 M^-8 h_j now give relative errors bounded by

    H^45 M^-1 [J2+ + log(e 30M) J3+].             (15)

For V J3 V, the same causal calculation gives normalized density

    <=H^40 r J3+ w(t)^4/w(s)^2 log(e w(t)).

Its original density is at most H^40 M^-8 log(e 30M) J3+, so its relative error is at most H^45 log(e 30M) J3+. This second-forward error needs M^2 log(M) J3+, one extra M power beyond (15). To retain a simple integer interface below, it is sufficient to charge J3+ M^3.

The direct forward forcing gives relative errors H^2 M^8 E2+ and H^2 M^8 E3+. Available beta slack is at least H^-1 M^-2. Hence all forward inequalities in (10) hold strictly provided

    H^100 [M^10(E2+ + E3+) + M J2+ + M^3 J3+] <=1. (16)

This corrects the preliminary M^2 J3 interface: the V J3 V second-forward term has the larger weighted endpoint w(t)^4. It must not be dropped.

The finite geometric expansion justifying the first-forward comparison is the same old entrywise argument: if F_b D_B F_b<=eta F_b, then (F_b D_B)^n F_b<=eta^n F_b. Condition (16) makes eta<1/2 and the summed increment below half the beta slack. The V expansion uses its own relative bound in the same way.

## 5. Backward reconstruction and the inactive sector

The exact backward reconstruction is

    W*-W_b=a^2 L_b J3 R*.

In normalized time R* has row <=H^40 w(v)^4. At a left time u, J3_hat R* thus has row <=H^45 r J3+ w(u)^4. The strict part of L_b has density <=K w(t)^4/w(u)^2, so (2) yields

    |L_b J3_hat R*|row(t)
      <=H^50 r J3+ w(t)^4 log(e w(t)).

The original B2 conversion cancels r. Therefore

    |W*-W_b|row <=H^55 J3+ M^4 log(e 30M).        (17)

Under the stronger numerical form of (16) stated below, (17) and the direct J2+ addition are below R_a/2. Thus the forward beta1 reference and all reconstructed backward coefficients lie strictly inside the beta2 box (7). The old beta derivative lower bound supplies the same strict forward margin H^-3 M^-10 h_j at every positive mesh step.

In the inactive sector K3=0, both affine backward arrays vanish, and the old exact construction gives

    B3*=J3-, B2*=a^2 J3- R*+J2-,
    A2*=A2_0+u Htime, A3*=A3_0+w Htime,

with

    u<=H^20 [E2- + M^4(J2-+J3-)],
    w<=H^30 [E2-+E3-+M^4(J2-+J3-)].              (18)

To check this, first bound R* by two when its integration-row times J3- is small. Then B2* row is at most 3(J2-+J3-), F*-K1 density at most C S(J2-+J3-), and V*-a^2 A2* density at most C S(J2-+J3-); choose u then w larger than these terms and the direct E forcing. This is a triangular comparison, not a coupled inverse bound. It includes the current backward diagonals.

Consequently the following single typed criterion is sufficient for the complete deterministic supersolution and strict interiority:

    M^10(E2+ + E3+) + M J2+ + M^3 J3+
      + E2-+E3- + M^4(J2-+J3-) <= H^-200.        (19)

Every numerical product above is at most H^55; fixed sums, the beta margin, r-conversion factors, and log(e 30M)<=10M fit within H^100. The H^-200 criterion leaves at least H^-45 relative slack against the H^-100 outer radii. In particular J3+<=H^-200 M^-3 makes (17) at most H^-140 M^2, below R_a/2; J2+<=H^-200 M^-1 is smaller still. The inactive backward rows from (18) are below R_i/2 and its added forward densities below one half.

The finite chronological A2,A3,B3,B2 comparison applies to actual signed coefficient arrays because |T0(C)|<=T0(|C|). The amplitude-homotopy first-exit argument is therefore uniform in cap and sufficiently fine fixed mesh, exactly as in the existing theorem.

## 6. Consequences and remaining boundary

The power-four response proof, on the larger boxes justified in Section 3, already gives the derivative-only forcing bounds

    E2<=H^30 e M^13, E3<=H^30 e M^11,
    J2<=H^30 e M^17, J3<=H^30 e M^14,

under e H^22 M^19<=1. These are full-sector bounds, so they can be inserted into both signs in (19). The old learned-moment q=eM19 would spoil this improvement; it must be replaced by the independently derived weighted raw comparison

    ||Theta_e(t)-Theta_0(t)||raw <= C (e/lambda) w(t)^3.

Even a coarse use of this new comparison gives learned forward densities at most eM^7,eM^8 and backward rows at most eM^14,eM^12, respectively. Those powers are below the derivative bounds just displayed. Thus (19)'s largest exponent is

    max(13+10, 11+10, 17+1, 14+3, 17+4, 14+4)=23.

Together with the independent weighted raw comparison, this route is sufficient for the complete delta^3 theorem, since M^24<=24^6 delta^-3. The old explicit prefactor 10^-70 H^-400 covers the H^30 forcing, the H^-200 threshold, and the original moment condition by a large margin. The old primal/nonaffinity delta^(7/4) restriction is also implied by delta^3.

This note does not claim delta^2. For that target, the typed criterion identifies the obligations precisely: active forward forcing must cost at most eM^6 (or a better relative beta-slack comparison must replace the M^10 charge), inactive backward forcing at most eM^12, and the source exponential moment condition must fit eM^16. The active J2/J3 closure has ceased to be the principal loss. Additional sector-resolved response estimates are being developed separately; provisional scalar gain domination must not be used for random off-diagonal sample gates without a valid two-sector argument.
