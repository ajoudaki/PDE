# Sharper affine propagator and actual source certificate for the power-four route

This calculation uses the rigorous-math skill and the original independent-root source identity. It edits no theorem file and runs no experiment. Throughout, M=(3/(sqrt(2) lambda))^(1/4) is the actual dataset endpoint scale, lambda=a^3 r, 1/2<=a<=1, and r=sqrt((1+tau rho)/2). In particular r=3 M^(-4)/(sqrt(2)a^3), and M<=24^(1/4) delta^(-1/8). The numerical envelope is exactly the existing H=C_B=10^30(1+C0+Cz+Cg+exp(1410))^4. It satisfies H>=10^30 exp(5640).

The main new result is the affine raw propagator C M^3, replacing C M^5. More precisely its radius-one tube obeys a two-time weighted bound exp(2100) [w(t)/w(s)]^3, where w(t)=sqrt(beta^2+||D_beta(t)||^2). This retains both the full raw geometry and the actual source-probe identification.

## 1. All four gradient terms improve the radial lower bound

At beta=1 write z=||D||^2, F=<D,BAp>, K=A0* A0-p0 tensor p0, J=A0 A0*-B0*B0, and K_B=B0B0*. The active normalized system is exactly

    p'=A*B*D,  A'=B*D tensor p,  B'=D tensor Ap,  D'=BAp.

The existing balances give

    ||p||^2=1+z,  A*A=p tensor p+K,
    AA*=B*B+J,    BB*=D tensor D+K_B.

The initial hypotheses ||A0||,||B0||<=10 and ||p0||=1 imply

    -I<=K<=100 I,  -100 I<=J<=100 I,  0<=K_B<=100 I.

Let s_A=||Ap||^2 and s_B=||B*D||^2. Then

    z(1+z)<=s_A<=(z+101)(z+1),
    z^2<=s_B<=z^2+100z.

The upper bound on s_A follows from A*A<=p tensor p+100I, which also slightly improves the old operator bound for A. The two matrix-gradient terms obey

    ||A'||_HS^2=s_B(1+z)>=z^3+z^2,
    ||B'||_HS^2=z s_A>=z^3+z^2.

For the readout gradient, using B*B=AA*-J and Cauchy--Schwarz against p,

    ||D'||^2=||BAp||^2
      >=||A*Ap||^2-100s_A
      >=s_A^2/(1+z)-100s_A
      >=z^2(1+z)-100(z+101)(z+1)
       =z^3-99z^2-10200z-10100.

No monotonicity of the quadratic in s_A is assumed: its positive term is bounded below and its negative term separately bounded below by the upper bound on s_A. For the bottom gradient, BB*D=zD+K_BD and K_B>=0 give

    ||p'||^2=||A*B*D||^2
      >=||BB*D||^2-100s_B
      >=z^3-100z^2-10000z.

Since the system is gradient ascent for F,

    F'>=4z^3-197z^2-20200z-10100,              (1)
    z'=2F,  F>=0.

Integrating (1) without dividing by F or z gives

    F^2 >= P(z):=z^4-(197/3)z^3-10100z^2-10100z.   (2)

Indeed the derivative of F^2-P(z) equals 2F[F'-P'(z)]>=0 and its initial value is zero. The old middle-gradient estimate also gives F>=z^2/sqrt(2). These two bounds imply the convenient global inequality

    F>=z^2-100z.                                  (3)

For 0<=z<=200, z^2/sqrt(2)>=z^2-100z because 1-1/sqrt(2)<1/2. For z>=200,

    P(z)-(z^2-100z)^2
      =z^2[(403/3)z-20100-10100/z]>0;

the bracket is increasing and positive at 200, and z^2-100z>=0. Thus (2) gives (3) also in this range.

## 2. A two-time M^3 propagator with an explicit constant

At scale beta, homogeneity gives Theta_beta(t)=beta Theta_1(beta^2t), F_beta=beta^4 F_1(beta^2t), and c_beta=||D_beta||=beta c_1(beta^2t). Therefore (3) becomes

    F_beta>=c_beta^4-100 beta^2 c_beta^2.

For w_beta=sqrt(beta^2+c_beta^2),

    (log w_beta)'=F_beta/(beta^2+c_beta^2)
      >= c_beta^2-101 beta^2.                    (4)

The existing enlargement applies on the same normalized interval 0<=t<=T<2 for

    beta_j=1+j/[10^6(200+M^2)], j=1,2,3,
    beta_far=1+1/[10^5(200+M^2)].

All these beta are at most 1.001. Put R_beta=sqrt(200 beta^2+c_beta^2). Every affine component has norm at most R_beta. In the sum of the four raw increment norms, the affine Hessian is bounded by 3R_beta^2: its six pairs of off-diagonal blocks are products of the remaining two factors, and every column has three such blocks. The affine objective annihilates inactive first-layer directions, so this is also the full raw metric bound.

On a raw radius-one tube, the Hessian is bounded by 3(R_beta+1)^2. From (4), for any s<=t<=T,

    integral_s^t 3 R_beta^2 du
       <=3 log[w_beta(t)/w_beta(s)]+903 beta^2(t-s)
       <3 log[w_beta(t)/w_beta(s)]+1810.          (5)

The old radial inequalities c_1(t)>=t and c_1'>=c_1^3/sqrt(2) imply on its entire existence interval

    integral c_1 dt <=1+sqrt(2).

Before c_1 first reaches one the duration is at most one and c_1<=1. Afterwards substitute dt<=sqrt(2)c_1^(-3) dc_1 and integrate to any terminal value. Homogeneity yields integral_0^T c_beta dt<=1+sqrt(2). Hence

    integral_0^T R_beta dt
      <=sqrt(200) beta T+1+sqrt(2)<31.

Combining this with (5),

    integral_s^t 3(R_beta+1)^2 du
      <=3 log[w_beta(t)/w_beta(s)]+2100.          (6)

Consequently the raw variational propagator, and the finite-difference tube comparison relevant to the probes, have the two-time bound

    G_beta(t,s)<=exp(2100)[w_beta(t)/w_beta(s)]^3. (7)

The already established enlargement keeps the continued beta-one primary components below 2sqrt(200+M^2); after the beta factor, w_beta(T)<=30M. Also w_beta(s)>=beta>=1. Thus a safe common global bound is

    G_beta(t,s)<=10^5 exp(2100) M^3.             (8)

The radius-one term in (6) is integrated as 6R_beta+3. Replacing (R_beta+1)^2 by a fixed multiple of R_beta^2 would unnecessarily increase the logarithmic coefficient and lose the exact exponent three.

The same estimate with an extra factor four holds on every sufficiently fine positive Euler mesh. One first applies uniform bounded-set Euler approximation over the compact beta interval and then approximates the deterministic integral in (6). The mesh may depend on the fixed dataset and bound M. This statement requires no uniform width probability estimate for a growing transcript. At each fixed mesh the original finite-program width limit and then the independent-root amplitude limit are taken in their prescribed order.

## 3. The actual affine source arrays

Use the exact normalization of AFFINE_SOURCE_CERTIFICATE.md. Densities in this paragraph use normalized steps Delta t_j=lambda h_j. Every source probe is an additive independent standard Gaussian root inserted at its named answer instruction. Perturbed programs recompute all subsequent calls and updates. The probe identity is the original TWO_SAMPLE_SOURCE_BASELINE.md, equations (23)--(25): at fixed nonzero amplitude epsilon, take the fixed-program width limit, pair the output with the root, and only afterwards let epsilon tend to zero. The identity measures the deterministic formal derivatives with coefficient/covariance arrays frozen. No identification of an arbitrary raw tangent with a source derivative is used.

The existing injection and output costs are unchanged. Bottom transpose -> p and top forward -> D have product cost 1. Middle transpose -> Ap and middle forward -> B*D have product cost C M^2. The six forward/backward resolvent probes have product cost C M^2, and the top backward -> BAp probe has product cost C M^4. Each strict pulse carries its original Delta t_j. Reusing the same independent root with signs at all source slots bounds full absolute rows, including their direct identity where present.

Substituting (8) gives the following normalized-time bounds. They are uniform on the three inner beta scales.

| Affine object | Strict density or full row bound |
|---|---:|
| F,T,A2,B3 density | H M^3 |
| V,W,A3,B2 density | H M^5 |
| B3,T complete rows | H M^3 |
| B2,W complete rows | H M^5 |
| R1,R,L,R3,L3 complete rows | H M^5 |
| U=R3 A3 density | H M^7 |

The coefficient bounds add the actual learned moments, with density exponents 2,4,2,4, respectively. Their powers are lower than the displayed response powers. The inactive sector remains explicit: F_-=H_time, A2_-=2beta^2 H_time, V_-=2beta^2 H_time, A3_-=3beta^4 H_time, and all inactive affine backward arrays vanish. Inactive resolvents are identity.

The beta-positivity proof is unchanged. At a fixed mesh all active entries and learned moments are nonnegative polynomials in beta, and

    A3_beta'>=2 beta^3 R_beta F_beta L_beta.

The available beta gap has inverse at most 3*10^7 M^2. Since normalized A3 has density H M^5 before beta differentiation, the same direct coefficient argument yields

    |FL|d, |RF|d, |RFL|d <= H M^7.               (9)

Here H in (9) is still one common numerical prefactor, as counted below, rather than multiplying a previously saturated bound H by another H and silently reducing it.

## 4. Original-time table and the useful active bounds

On the active sector, the exact factors are

    A2=(r/a) A2_hat,  A3=ar A3_hat,
    B3=(ar)^(-1) B3_hat,  B2=(a/r) B2_hat,

with the identical transformations for F,V,T,W. Strict densities have the additional factor lambda=a^3 r. Resolvents transform by diagonal similarity and their diagonal-sector rows do not change. U transforms like A3; FL,RF,RFL transform like F. Thus, with every common numerical constant at most the original H:

| Original-time object | Active sector | Full two-sample bound |
|---|---:|---:|
| F,A2 density | H M^-5 | H |
| V,A3 density | H M^-3 | H |
| T,B3 complete row | H M^7 | H M^7 |
| W,B2 complete row | H M^9 | H M^9 |
| R1,R,L,R3,L3 complete rows | H M^5 | H M^5 |
| U density | H M^-1 | H |
| FL,RF,RFL density | H M^-1 | H |

The inactive contribution to the final three strict transfers is O(1), not M^-1. The small active densities must be retained when making the active positive supersolution. Useful additional active row bounds are |F|r<=H M^-1 and |V|r<=H M; these follow directly from the normalized rows and the factor r. If obtained by multiplying the original-time density by the interval length, they give the same powers.

For the numerical check, on the enlarged reference take every primary bound as 100M. Formula (8), with a factor four for the Euler margin, costs at most 4*10^5 exp(2100) M^3. The largest product of injection/output costs is 9*(100M)^4, so 4*10^14 exp(2100) dominates every normalized probe prefactor. A factor 10^3 covers two-sample basis changes, duration <=2, current identities, beta<=1.001, gains, and moment additions. A further factor 3*10^7 handles beta differentiation. Conversion back to original time uses r^2<=288 M^-8 and r^-1<=M^4; another factor 10^4 is more than sufficient. Thus 10^30 exp(2100) dominates every displayed original-time coefficient, response, and beta-product prefactor. Since 10^30 exp(2100)<10^30 exp(5640)<=H, the table genuinely retains the existing explicit numerical envelope H.

## 5. Consequence for positive closure, and the remaining nonlinear obligation

The active supersolution algebra in POSITIVE_SUPERSOLUTION.md now has the following power count, using the same genuine strict/row/strict sandwich estimate and retaining arbitrary current diagonals:

    |F J2 F|d <= C M^(-6) q,
    |(FL) J3 (R*F)|d <= C M^2 q,
    |V J3 V|d <= C M^(-2) q.

Here the duration contributes M^4; the two active FL/RF densities each contribute M^-1. The relative active forcing divides by the unchanged lower bound F_kj,V_kj>=c M^-8 h_j. Thus the first-forward relative defect is C M^10 q, the second is at most C M^8 q, and the beta scale margin is c M^-2. Active forward closure needs q<=c M^-12.

Backward reconstruction has |L J3 R*|r<=C M^10 q. With active outer backward excess radius c0 M^-2, q<=c M^-12 also makes the backward supersolution interior. The active Neumann ratio uses |V|r<=C M, so that outer radius gives C c0 M^-1. Choose a separate inactive outer radius c0 M^-5, because its integration row is O(M^4); q<=c M^-12 is more than sufficient for its direct forced construction. The separate nonlinear source and positive-supersolution arguments use these distinct active/inactive outer radii.

A deliberately rounded numerical version can retain q<=H^-20 M^-12, active radius H^-10 M^-2, and inactive radius H^-10 M^-5. Exact H bookkeeping can follow the published closure ledger with the revised powers; there is ample spare prefactor in the ultimate c_poly= min(1/4,c_*,10^-70 H^-400).

This note proves the new affine input and its actual derivative identification, but does not by itself prove the full delta^4 theorem. The separate response lemma in PRIMAL_L2_RESPONSE.md supplies forcing q<=C e M^19 on this outer box. Its source-value triangle estimates retain incoming subGaussian exponents q1:M^15, q2:M^13, C:M^11, used to control derivative-envelope moments under e M^19 smallness. For the final product E[Q E], it uses the much smaller actual raw L2 incoming bounds M^3,M^2,M and Holder with the envelope's L2 bound. It retains the deterministic B-gate contributions as well. Thus the largest derivative defect is e M^17 and the learned-moment row defect e M^19 dominates. No additional covariance-domination lemma is necessary. Together with the independent positive closure at q<=c M^-12, that separate response result gives total cost e M^31, within the target budget e M^32.
