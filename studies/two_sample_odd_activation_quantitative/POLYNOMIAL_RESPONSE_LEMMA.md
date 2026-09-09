# A polynomial source-response bridge by positive affine scaling

Status: **candidate proof; requires independent adversarial review before promotion into the theorem.** The earlier open route is preserved in /tmp/sharpen_response_initial_gap.md. The positive-scaling argument below resolves its specific coupled-response inverse gap. This note does not modify the current proof, run experiments, or commit changes.

The theorem proved here is an interface lemma: polynomial affine geometry, primal comparison, and affine Gaussian-probe bounds imply a polynomial nonlinear source threshold. The root supplies those affine estimates and the separate geometry/nonaffinity/initial-motion assertions. The complete population/GF/raw-GD conclusion follows using the already attached bridges once the interface and the root's estimates have been independently checked.

Sources read substantively: PROOF.md and SOURCE_AND_LIMIT_BRIDGE.md; THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md; NONLINEAR_RESPONSE_PERTURBATION.md, including its derivative and chronological equations; PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md; conditioning and canonical action portions of L3_LOCAL_COMPLETE_PROOF.md. The solve-math-rigorously skill was read.

## 1. Explicit polynomial input/output statement

Use the existing two-sample source programs with gain 1/2<=a<=1, constant folded controls c=(1/2,1/2), and a positive mesh of feature duration S. Work up to the prescribed bounded affine target interval, with sufficiently fine meshes. Let B>=2 dominate the following quantities, uniformly over these meshes and the admissible datasets:

1. S, the reciprocal active input variance v_u^(-1), and every scalar source Gaussian standard deviation provided by the primal bound.
2. Affine and stopped nonlinear primal/forward/backward L2 bounds, and the raw-comparison constants needed to bound the difference of every learned-moment coefficient by B e h_j (strict times). The nonlinear comparison must already be cap-uniform, as in the root's polynomial primal argument.
3. The actual affine response coefficients: forward strict densities max |Aell_kj|/h_j and backward row norms max_k sum_{j<=k}|Bell_kj|. Include the analogous learned-moment norms, hence also the derivative-only arrays F,V,T,W below.
4. The same affine coefficient bounds at a common enlarged initialization scale beta_*>1, and (beta_*-1)^(-1). The enlarged trajectory must exist on the same mesh/horizon and have the polynomial affine probe bounds.

The matrix norm inside these definitions is the maximum absolute sample row sum. Fixed changes to an orthonormal (+,-) sample basis cost a universal factor, absorbed into B.

Then the source conclusion holds at least for

    0<=e<=10^(-70) B^(-400).                        (1)

Specifically, the actual coefficient arrays have uniformly bounded forward strict densities and backward row norms; C,q2,q1 and all source fields have cap/mesh-uniform subGaussian norms; and the derivative bounds needed by the existing cap-removal bridge hold. The estimate is uniform in the gain after using a^(-1)<=2.

The dependence in (1) is a fixed polynomial of the listed inputs. It does not use the old unspecified response constant K or its exponential. The exact source threshold is 10^(-70) B_delta^(-400). If the independent affine input certificate gives B_delta<=C_B delta^(-m), this yields e<=c delta^(400m), with c=10^(-70) C_B^(-400). The input exponent and resulting final exponent belong to the assembled affine/source proof, rather than being assumed in this interface lemma.

## 2. Temporal kernel algebra and the exact affine equations

Write A2,A3,B3,B2 for the source coefficient arrays. Let H_P and H_c be the strictly causal integration operators

    (H_P v)_k=sum_{j<k}h_j P_j v_j,
    (H_c v)_k=sum_{j<k}h_j c_j^T v_j,

and let E broadcast a readout scalar into two sample slots. Put K1=a²H_P and K3=a²E H_c. The derivative-only affine arrays are exactly

    F=(I-K1 B2)^(-1)K1,
    R=(I-a² A2 B3)^(-1),
    L=(I-a² B3 A2)^(-1),
    V=R a² A2,
    T=K3(I-A3 K3)^(-1),
    W=a² B3 R.                                      (2)

All inverses exist algebraically at a finite mesh because the product subtracted from the identity is strictly causal. The coefficient equations are

    A2=F+MA2, A3=V+MA3, B3=T+MB3, B2=W+MB2,          (3)

where M denotes the actual learned-moment contribution. These formulas follow directly by differentiating the affine source equations with the coefficient arrays and moments frozen. For example H2=a xi2+a²A2(zeta2+B3H2), so its reverse-source derivative is V and the forward-source derivative of delta2=a(zeta2+B3H2) is W. At the top H3=a xi3+a²A3 E C and C=H_cH3, which yields T.

For a strictly causal matrix U define its density |U|_d=max_{k,j<k}|U_kj|/h_j. For any causal matrix Q define |Q|_r=max_k sum_{j<=k}|Q_kj|. The coefficient norm is

    ||C||=max(|A2|_d,|A3|_d,|B3|_r,|B2|_r).         (4)

The basic estimates, valid for arbitrary positive meshes, are

    |U|_r<=S|U|_d,
    |Q1 Q2|_r<=|Q1|_r|Q2|_r,
    |U1 Q U2|_d<=S|U1|_d |Q|_r |U2|_d.             (5)

For the last bound, in (U1 Q U2)_kj bound |U2_vj| by |U2|_d h_j, sum |Q_rv| in v, bound |U1_kr| by |U1|_d h_r, and sum h_r<=S. This sandwich estimate is what permits backward-row forcing, including diagonal forcing, without a lower mesh-size restriction.

## 3. Exact coupled Jacobian

At the actual affine baseline let X2,X3,Y3,Y2 denote coefficient variations. Differentiating (2)-(3) gives the exact forced system

    X2=F Y2 F+E2,
    X3=a²R X2 L+V Y3 V+E3,
    Y3=T X3 T+J3,
    Y2=a²L Y3 R+W X2 W+J2.                         (6)

For example dV=a²R(dA2)L+V(dB3)V, using I+B3V=L. The forcing E2,E3 is measured in strict density and J3,J2 in row norm. Let J0 denote the homogeneous right-hand-side map in (6). Its inverse is a finite chronological ladder expansion at any finite mesh.

Arbitrary backward-row forcing reduces exactly to forward-density forcing. Set

    Ytilde3=Y3-J3,
    Ytilde2=Y2-a²L J3 R-J2.

Then the homogeneous equations are unchanged and the only new forcing is

    Etilde2=E2+F J2 F+a²F L J3 R F,
    Etilde3=E3+V J3 V.                              (7)

Because L=I+B3V and R=I+VB3, both FL and RF have strict densities bounded polynomially in B. Thus (5) proves that both expressions in (7) have strict density bounded polynomially by the original forcing norm. Reconstruction of Y3,Y2 has polynomial row cost. This argument retains every current backward diagonal and needs no per-entry h_j bound on nonlinear backward forcing.

## 4. Sample sectors: only the active sector has a ladder

After folding labels, exchange symmetry diagonalizes every affine A2,A3,F,V,R,L in the (+,-) sample basis. The affine backward fields are identical across the two sample slots and depend only on active forward sources. Consequently B2,B3,T,W have only a ++ sample block.

It follows that (6) decouples into its four sample sectors. In every sector other than ++, multiplication T X3 T and W X2 W vanishes. Thus Y3=J3 first, then Y2=a²L J3R+J2, then X2 and X3 are determined without feedback. These sectors have polynomial bounds from (5). The inactive variance cannot generate a hidden exponential ladder.

Only the scalar active sample sector needs a new inverse argument.

## 5. Positive scaling bounds the active inverse

Scale all initialized raw hidden parameters (including the projected first root) by beta, leaving the zero readout zero. The two initial Gaussian matrix variances become beta². The raw affine quartic-gradient equation is homogeneous, so on its common existence interval

    Theta_beta(s)=beta Theta_1(beta²s).              (8)

The root's normalized affine continuation supplies beta_*>1 with beta_*-1 inverse-polynomial in its endpoint size. The integrated affine Hessian on that slightly longer interval remains logarithmic in that size, so the assumed affine Gaussian-probe coefficient bounds at beta_* are polynomial. At fixed meshes it is enough to take sufficiently fine Euler meshes for this scaled family; no identity between a fixed Euler mesh and its time dilation is needed.

For matrix variance beta², Gaussian conditioning multiplies every initialized-matrix return by beta². Thus (3) becomes exactly

    A2_beta=beta²F_beta+MA2_beta,
    A3_beta=beta²V_beta+MA3_beta,
    B3_beta=beta²T_beta+MB3_beta,
    B2_beta=beta²W_beta+MB2_beta.                    (9)

The functions F,V,T,W still have the same forms (2); K1,K3 are unchanged because the raw gradient metric and data are unchanged. Scaling the first root changes learned moments, not those integration operators. There is therefore no omitted beta derivative of the time mesh, control, covariance square root, or gain in differentiating (9).

All active-sector kernels in (9) are entrywise nonnegative polynomials in beta at every fixed affine Euler mesh. Here is the needed positivity argument. In normalized active coordinates, the affine ascent updates for p,A,B,D contain only additions, positive step sizes and products; D_0=0, and all remaining initialized variables are centered independent Gaussians multiplied by beta. The coefficients of every raw-coordinate polynomial are nonnegative. In a covariance contraction, each Wick pairing contributes a nonnegative product of variances. Therefore every active learned moment is a polynomial in beta with nonnegative coefficients. The affine source recursions are chronological sums/products with nonnegative active integration coefficients, so the expected-derivative/source coefficients have the same property. In particular every derivative M'_ell(1) is nonnegative. This argument can be applied to finite Gaussian arrays and passed to the fixed-program limits; it does not assume positivity of an individual realization of the Gaussian weights.

Differentiate (9) at beta=1. With C'=dC_beta/dbeta|_1,

    (I-J0) C'=(2F+MA2',2V+MA3',2T+MB3',2W+MB2').   (10)

In the active sector K1 has entries a²v_u h_j and K3 has entries a²h_j. Since the inverse expansions and moments are nonnegative,

    F_kj>=a²v_u h_j,
    V_kj>=a⁴v_u h_j,
    T_kj>=a²h_j,
    W_kj>=a⁴h_j,       j<k.                        (11)

As a>=1/2 and v_u^(-1)<=B, the forcing in each component of (10) is at least h_j/(8B).

For a polynomial f(beta)=sum_m c_m beta^m with c_m>=0 and beta_*>1,

    f'(1)<=f(beta_*)/(beta_*-1).                    (12)

Indeed beta_*^m-1>=m(beta_*-1); summing gives a slightly stronger inequality with f(beta_*)-f(1). The assumed coefficient bounds and (12) bound C' by B² in its forward-density/backward-row norm.

After (7), let the active forward forcing have density at most q. Its entrywise absolute value is at most q h_j and its backward forcing is zero. The inverse (I-J0)^(-1) is entrywise nonnegative: its finite chronological ladder contains only nonnegative products. Equations (10)-(11) consequently imply

    |(I-J0)^(-1)(Etilde2,Etilde3,0,0)| <= 8B q C'   (13)

entrywise. Hence its coefficient norm is at most 8B³q. This proves the missing inverse bound without a paired-probe realization of arbitrary covariance forcing.

Using (5), the shift (7), the inactive/mixed-sector formulas, and reconstruction gives the conservative full bound

    ||(I-J0)^(-1)|| <= 10^6 B^20.                  (14)

For scale: FL and RF have density at most a universal multiple of B^4; their sandwich with a row forcing costs at most a multiple of B^9. Equation (13) then costs B³. The inactive/mixed-sector substitutions cost at most B^15. The oversized bound in (14) includes sample-basis conversion.

## 6. Polynomial neighborhoods of the affine source map

Let D=||C-C0|| in (4). On D sufficiently smaller than B^(-20), all same-array affine source resolvents and required strict transfers have polynomial bounds by Neumann expansion about the baseline.

The useful distinction is that a source resolvent need only have a bounded row norm. Every local derivative perturbation is integrated through a strict transfer. The identities

    R1=I+F B2,
    R=I+V B3,
    L=I+B3V,
    R3=I+A3 T                                      (15)

show the baseline row bounds directly. Perturbing the strictly causal operators inside the inverses changes their row norms by a polynomial times D, so Neumann expansion closes on a polynomial neighborhood. For strict transfers, use the corresponding resolvent identities and (5); for example

    F-F0=F0 (B2-B2_0) F.

The same identities for V and T place every backward-row variation between strict transfers, or adjacent to an identity plus such a product. Thus the density bounds are preserved without assuming that B2-B2_0 or B3-B3_0 has a strict density.

Here is quantitative algebra behind that assertion. Enlarge B to include the baseline derivative-only arrays in (2). Write D for (4), and assume D<=1/(100 B^6), which follows from the bootstrap below. The exact identity F=F0+F0 DeltaB2 F and (5) give |F|_d<=B+S B D |F|_d, hence |F|_d<=2B. For V the exact identity

    V=V0+a²R0 DeltaA2 L+V0 DeltaB3 V,
    R0=I+V0 B3_0,  L=I+B3 V

and expansion of the middle product give

    |V|_d<=B+(1+B³)D+(3B²+2B^5)D |V|_d.

Thus |V|_d<=4B. For T, T=T0+T0 DeltaA3 T gives |T|_r<=B+B S D |T|_r, hence |T|_r<=2B. Consequently

    |R1|_r<=5B³, |R|_r,|L|_r<=9B³, |R3|_r<=5B³.

The top strict transfer obeys

    R3 A3=A3+A3 T A3,
    |R3 A3|_d<=2B+8B^4<=10B^4.

The bottom and middle strict transfers used by the derivative equations are R1 H_P=F/a² and R A2=V/a², bounded by 8B and 16B respectively. These estimates justify the use of the exact inverses without an exponential. Current backward diagonals are included in |B2|_r,|B3|_r<=2B throughout.

A conservative common bound for all source value transfers, their row norms, and the strict transfer densities is

    Rstar=10^4 B^20.                               (16)

Only addition, multiplication, the sandwich inequality (5), and a Neumann series with ratio at most 1/2 are used here. No exp(B^m) bound is used.

The coefficient map T0(C)=(F,V,T,W) has a quadratic Taylor remainder on this neighborhood:

    ||T0(C0+Delta)-T0(C0)-J0 Delta||
       <=10^20 B^100 D².                          (17)

For a more explicit check, the first variations are dF=F(dB2)F, dV=a²R(dA2)L+V(dB3)V, dT=T(dA3)T, and dW=a²L(dB3)R+W(dA2)W. The bounds above give |dF|_d,|dT|_r<=4B³D, |dV|_d<=116B^6 D, |dR|_r,|dL|_r<=236B^8 D, and |dW|_r<=405B^9 D. To check the density bound for dV, expand R(dA2)L using R=I+VB3 and L=I+B3V and apply (5) to each of its four terms. Differentiating that expansion again gives |d²V|_d<=5000B^11 D²; the largest term is a sandwich with dV,B3,dA2,B3,V, bounded by S²(116B^6)(2B)(2B)(4B)D². The other second variations satisfy |d²F|_d,|d²T|_r<=16B^5D². Differentiating dW gives |d²W|_r<=20000B^14D²: the largest terms are dW(dA2)W and W(dA2)dW, each at most (405B^9)(B)(18B^4)D². Taylor's integral remainder on the segment between C0 and C0+Delta proves (17), with ample numerical and degree slack. These calculations are uniform in transcript length and cap and involve no Gronwall estimate.

## 7. Source moments by resolvent perturbation

On the same coefficient neighborhood, write the actual nonlinear source equations as their same-array affine equations plus nonlinear remainders. The only value estimates needed are

    |phi(z)-az|<=e pi/2,
    |D_cap(z,q)-aq|<=e|q|.                         (18)

For clarity, direct substitutions give explicit intermediate bounds before the oversized constant Rstar is used. Absorb the two sample slots into a factor two in the Gaussian Lp norms. At the bottom q1=zeta1+B2(aZ1+e arctan Z1), and the affine resolvent yields an inequality of the form

    ||Z1||_p<=100 B^5 sqrt(p)+20 B^5 e ||Z1||_p.

At the middle q2=zeta2+B3(aZ2+e arctan Z2); applying R with |A2|_r<=2B² gives

    ||Z2||_p<=400 B^6 sqrt(p)+72 B^6 e ||Z2||_p.

At the top C=H_c(aZ3+e arctan Z3); applying R3 with |A3|_r<=2B² gives

    ||Z3||_p<=100 B^6 sqrt(p)+20 B^6 e ||Z3||_p.

For example the middle nonlinear terms before applying R are a e A2 B3 arctan Z2 and e A2 g(Z2)tau_R(q2); their norms are at most 8B³e and 2B²e(B sqrt(p)+2B||Z2||_p+4Be), respectively. Multiplication by |R|_r<=9B³ gives the stated bounds after enlarging numerical constants. The bottom/top equations are the same two explicit substitutions with H_P or H_c. Under (1), absorb all three self terms. Then q1,q2,C, the features and deltas all have Lp norm at most 10^4 B^8 sqrt(p), which is below 2Rstar sqrt(p).

For each p>=2 let X_p be the maximum Lp norm of all source fields in the three populations. The bounded source Gaussian variances and the transfers in (16), followed by the finite-depth forward/backward substitutions, give

    X_p <= Rstar sqrt(p)+Rstar e X_p               (19)

with the displayed Rstar already larger than the direct substitution bounds above. Equivalently one can expand around the baseline inverse and obtain Rstar(e+D) in place of Rstar e. Both versions close under (1) and D<=d0, with d0 defined in Section 9. Thus X_p<=2Rstar sqrt(p), uniformly in p, cap and mesh. This provides Gaussian L2 tails of all incoming backward fields. The bound does not compare Gaussian covariance square roots; their variances came from the separate primal argument.

## 8. Nonlinear derivative defect, with no nonperturbative exponential

Freeze the actual coefficient arrays and covariance parameters. The local derivative matrices in the source equations are

    G=aI+e diag(g(Z)),
    Vgate=aI+e diag(g(Z) tau_R'(q)),
    Lgate=e diag(g'(Z) tau_R(q)).

Thus |G-aI|,|Vgate-aI|<=e and |Lgate|<=eQ, where Q is the appropriate incoming-field maximum. Compare to the affine derivative system at those SAME arrays.

For example the middle preactivation derivative is exactly

    J_k=I_k^xi+sum_{r<k} A2_kr [Lgate_r J_r
          +Vgate_r(I_r^zeta+sum_{v<=r}B3_rv G_v J_v)].

At the top,

    J_k=I_k^xi+sum_{r<k}A3_kr(Lgate_r J_r+Vgate_r E T_r),
    T_k=sum_{r<k}h_r c_r^T G_r J_r.

The bottom equation is the same substitution with H_P in place of A2. To make the middle comparison explicit, write G=aI+DeltaG and Vgate=aI+DeltaV. Applying the exact same-array inverse gives

    J=Jaff+R A2[Lgate J+DeltaV I^zeta
        +a DeltaV B3 J+a B3 DeltaG J+DeltaV B3 DeltaG J].

The formal affine source derivatives Jaff are deterministic once the arrays are frozen. This comparison differentiates no source covariance, covariance square root, or learned moment. Solve the affine part using the exact same-array resolvent. Every remaining unknown is multiplied by e or eQ and passes through a strict transfer before returning to a preactivation equation. One can see the polynomial rate without using a black-box derivative estimate. After applying the same-array inverse, bottom and middle local perturbations pass through F/a² or V/a². Their strict densities are at most 8B and 16B. Their remaining local factor is bounded by e(Q_r+6B) times the maximum prior derivative, because |B2|_r,|B3|_r<=2B and |G|,|Vgate|<=2. At the top the transfer R3A3 has density at most 10B^4; the additional readout sum has row norm at most B. Thus a bound 10^4 B^6 e(1+Q_r), multiplied by h_r, dominates every derivative feedback coefficient. Direct full forward-source rows have affine row norm at most 9B³; single transpose-source forcing is at most 32B h_j. The envelope constants below exceed all of these quantities.

Equations (5), (15)-(16) therefore give a deterministic majorant with rate

    Lstar=10^8 B^50

of the form

    |J_k| <= Lstar f
       exp(Lstar e s_k+Lstar e sum_{r<k}h_r Q_r).    (20)

Here f=h_j for a single transpose-source slot, and f=1 for the sum of block norms in a full forward-source derivative row. At a single transpose-source time the explicit injection carries h_j (or A_kj), the derivative vanishes before that time, and all later propagation preserves this factor. For full forward rows, the direct identity row has norm one. We do not need a per-entry h_j claim for every past forward source.

The backward-output derivative retains the required terminal factor

    Lstar(1+eQ_k)                                  (21)

multiplying the envelope. This includes current nonlinear returns, including Lgate_k J_k. A time-row estimate is sufficient because Section 3 handles arbitrary backward-row forcing.

By (19), Q_r has subGaussian norm at most a polynomial in B. Jensen in the weights h_r/S gives

    exp(u sum_r h_r Q_r)
       <=1-s_k/S+sum_r(h_r/S)exp(u S Q_r).

The scalar Gaussian moment estimate then bounds every needed fixed moment (for example orders up to eight) of (20)-(21) polynomially whenever e Lstar S Rstar is sufficiently small. Condition (1) is much stronger. No random supremum over source times is introduced. If source-time and terminal multipliers both occur, use Hölder to keep both Q_j and Q_k; their fixed moments are supplied by (19).

Subtracting the same-array affine derivative equations now leaves only the e/eQ forcing. Apply the same exact affine transfer, rather than a Gronwall estimate for its unperturbed coefficients. The resulting expected derivative defect satisfies

    forward strict density defect <=10^30 B^200 e,
    backward time-row defect <=10^30 B^200 e.        (22)

More explicitly, the difference of preactivation derivatives from their same-array affine values is bounded by an e multiple of the exact strict transfer applied to (1+Q_r) times the actual derivative. After inserting (20), its expected magnitude is at most a universal multiple of Lstar² e f S(1+Rstar), where f=h_j or f=1 as above. Backward outputs add the terms Lgate_k J_k, (Vgate_k-aI) B G J, a B(G-aI)J, and a² B(J-Jaff); their expected row norms are at most a universal multiple of e Lstar Rstar plus B times the preceding difference bound. Since Lstar=10^8 B^50, Rstar=10^4 B^20 and S<=B, these products have degree at most 123 and coefficient less than 10^30, well below (22). The source/terminal multipliers are handled by Hölder of fixed order, so no factor depending on the number of source slots occurs. In particular, (20) contributes at most two Lstar factors, the time sums contribute at most powers of S<=B, the terminal/source multipliers contribute fixed moments bounded by powers of Rstar, and the final backward substitution contributes a coefficient row norm. These fixed products have degree less than 200 and universal coefficient less than 10^30. The only exponential is (20), whose exponent is proportional to e and has uniformly bounded needed moments under (1). There is no exp(Lstar S) term.

The direct current returns remain exactly those of the original source proof:

    (B3_kk)_ij=1_{i=j} E Lgate3_k,i,
    (B2_kk)_ij=1_{i=j} E Lgate2_k,i
              +(B3_kk)_ij E[Vgate2_k,i G2_k,j].

They are part of the backward-row defect in (22), and are not dropped or inverted.

## 9. Closing the nonlinear coefficients

At any fixed mesh/cap use the amplitude homotopy lambda e, 0<=lambda<=1. Its source coefficients depend continuously on lambda by the finite causal source construction. The separate primal comparison bounds each learned-moment entry difference by B e h_j; the backward row sum therefore costs at most S B e<=B²e. Combining this with (17) and (22), write

    Delta=J0 Delta+forcing+quadratic remainder,
    ||forcing||<=2·10^30 B^200 e,
    ||quadratic remainder||<=10^20 B^100 D².

Equation (14) gives the explicit inequality

    D<=2·10^36 B^220 e+10^26 B^120 D².               (23)

Use the bootstrap radius

    d0=1/(4·10^26 B^120).

It lies inside D<=1/(100B^6) and every neighborhood used above. At D=d0 the quadratic term on the right of (23) equals d0/4. Under (1), the linear term is at most 2·10^(-34) B^(-180), which is smaller than d0/4: its ratio to d0/4 is 3.2·10^(-7) B^(-60). Thus the right side is at most d0/2, and there is no first exit as lambda increases. Moreover

    e Lstar S Rstar<=10^(-58) B^(-329),

so all required fixed moments of the derivative exponential remain bounded by universal constants on this bootstrap. The closed inequality implies

    D<=4·10^36 B^220 e.                             (24)

This proves the response coefficient bounds and validates all previous moment and derivative estimates on the complete source program. The proof uses a finite-amplitude homotopy at each fixed transcript; uniform estimates then pass to the source/Euler limits. It requires no uniform-in-width probability estimate for growing transcripts.

## 10. Consequences and review boundary

The uniformly subGaussian C,q2,q1 tails give the existing asymmetric cap estimate with error C exp(C(1+eR)S-cR²), which tends to zero for each fixed delta,e. The already supplied physical conversion, uniqueness against nonsymmetric bounded-primal competitors, fixed-width GF/raw-GD comparisons, velocity truncation order, and path-law upgrades then have no new amplitude restriction. All-time nonaffinity and initial feature learning must still be supplied by the root's separate geometric and initial-motion lemmas.

The genuinely new estimate is (14), followed by the polynomial resolvent-based moment/derivative closure. The active positive-scaling argument is not an assertion that arbitrary bounded operators preserve tails. The canonical warning in the appendix remains relevant.

This candidate should be independently audited at: (i) the active-sector positivity and beta² return factors; (ii) the backward-row forcing shift; (iii) same-array strict-transfer bounds in the mixed density/row norm; (iv) the e-weighted derivative envelope and current factors; and (v) the root's numerical polynomial bound for the input B. Do not claim an optimized power such as delta² from this conservative proof.

## Appendix: bounded canonical L2 actions do not preserve Lp tails

Let X be an initial standard Gaussian field and Z=A0X in the next layer. Fix p>2 and choose 1/(2p)<=c<1/4. Then V=exp(cZ²) is in L2 but not Lp. Use smooth bounded even truncations VM first, which are allowed fixed coordinate programs.

The actual transpose conditioning formula gives qM=A0*VM=zetaM+X E VM'(Z)=zetaM, since VM is even. This reverse Gaussian group is independent of the first root and forward sources. Set uM=tanh(qM), so |uM|<=1. The next forward query has the exact return

    A0uM=xiM+alphaM VM,  alphaM=E sech²(qM)>0.

Its forward Gaussian source has zero covariance with Z because E[uM X]=0. Passing to the L2 limit through the bounded action and Lipschitz tanh yields a bounded u with

    A0u=xi+alpha V,

where xi is Gaussian and alpha>0. Hence A0u is not in Lp. This is a canonical generated-space example, not a trained-trajectory counterexample; it establishes no necessity or sharpness claim for the mixing threshold.
