# Power-four source response: use primal L2 in the defect estimate

2026-09-07. Independent derivation. This note changes no existing theorem file. It uses the rigorous-math skill and the four requested power-ten companions, together with the original polynomial primal/source bridge. No experiments, delegation, or commits were performed.

The response conclusion is conditional on the new affine propagator certificate `G <= H M^3` and its explicit coordinate-probe consequences, being proved separately. It does not require an exact Gaussian covariance comparison. Its decisive observation is that the relatively large subGaussian source bounds are needed only for moments of a perturbative exponential; the factors multiplying that exponential can be estimated by the much smaller **already established actual primal L2 bounds**.

## 1. Exact input interface

Throughout, M=(3/(sqrt(2) a^3 sqrt(v)))^(1/4)>1 is the actual dataset endpoint scale, and H=C_B is the numerical constant in the prior theorem. Duration S is at most H M^4. Keep every original sample slot, forward and transpose named source, current return, cap, and positive mesh step.

The following same-array transfer bounds are needed on the outer coefficient box:

| Quantity | Bound |
|---|---:|
| strict density F,A2,V,A3 | H^2 |
| strict density Utop=Rtop A3 | H^2 |
| row R1,R2,Rtop,L2,Ltop | H^2 M^5 |
| row B2 | H^2 M^9 |
| row B3 | H^2 M^7 |
| row E Hc | H M^4 |

Here R1=(I-a^2 H_P B2)^(-1), R2=(I-a^2 A2 B3)^(-1), Rtop=(I-A3 K3)^(-1), L2=(I-a^2 B3 A2)^(-1), Ltop=(I-K3 A3)^(-1), and K3=a^2 E Hc. The strict density bounds imply rows of F,V,Utop at most H^3 M^4. Factors a^(-j), j<=4, are numerical because a>=1/2.

These bounds are full sample-block bounds. For random gates use the full two-by-two sample matrices; no claim of sample-diagonal random gates is made. Deterministic exchange symmetry only supplies the scalar-sector coefficient box from which the displayed bounds are proved. In particular, the true improved affine active Utop density is O(M^-1), and its inactive density is O(1), so the full bound H^2 is valid. The corresponding active F,V densities are O(M^-5), O(M^-3). Persistence on the larger nonlinear outer box belongs to the separate positive-supersolution argument; the response proof needs only the displayed interface.

The independently proved primal tube gives the actual cap/mesh source output norms

    sup_k ||q1_k||_2 <= H M^3,
    sup_k ||q2_k||_2 <= H M^2,
    sup_k ||C_k||_2  <= H M.

These are bounds on the actual capped program, not on the formal same-array affine comparison. For example q1=A* delta2 and q2=B* delta3, with ||delta_l||_2<=(a+e)||q_l||_2 and ||delta3||_2<=(a+e)||C||_2; the operator/readout/feature bounds give the displayed powers. The bounds |tau_R(q)|<=|q| and e<=1 make these estimates cap uniform. Their identity with the named source output laws holds at each fixed source program, as in the original bridge. Thus they are available before cap removal and before the new coefficient bootstrap closes.

Primitive Gaussian sources have standard deviations bounded, in their usual order, by

    Z1_initial: H;  zeta1: H M^2;
    xi2: H M;      zeta2: H M;   xi3: H M^2.

No independence beyond the existing source construction is required for the estimates below. Their arbitrary temporal correlations and singular covariance matrices cause no problem. Finally, every strict learned-moment discrepancy is at most H e M^15 h_j, hence each backward learned-moment row discrepancy is at most H^2 e M^19.

## 2. Cap-uniform subGaussian source moments

Put h(Z)=arctan Z and d(Z,q)=g(Z) tau_R(q), so |h|<=pi/2 and |d|<=|q|. Exact same-array affine elimination in the nonlinear value equations gives

    Z1=R1 Z1_initial+(F/a) zeta1
       + e(F/a^2)[d1+a B2 h1],
    Z2=R2 xi2+(V/a) zeta2
       + e(V/a^2)[d2+a B3 h2],
    Z3=Rtop xi3+e Utop[d3+a E Hc h3].

The incoming fields satisfy exactly

    q1=zeta1+B2(a Z1+e h1),
    q2=zeta2+B3(a Z2+e h2),
    C=Hc(a Z3+e h3).

For p>=2 denote the supremum over k of the individual Lp norms of Zi_k by Zi,p. This is not an Lp norm of a random supremum over time. The input table yields

    Z1,p <= H^6 M^6 sqrt(p)+e H^6 M^13 Z1,p,
    Z2,p <= H^6 M^6 sqrt(p)+e H^6 M^11 Z2,p,
    Z3,p <= H^6 M^7 sqrt(p)+e H^6 M^8 Z3,p.

For example the bottom Gaussian term F zeta1 has power 4+2=6, and its nonlinear self term has power 4+9=13. The middle direct forward term has power 5+1=6, its self term power 4+7=11; the top has power 5+2=7 and self power 4+4=8. The e-weighted Gaussian and bounded-atan additive terms are covered by the displayed leading terms under e H^6 M^13<=1/2.

Absorbing all three self terms gives Zi,p <= H^7 M^{zi} sqrt(p), with z=(6,6,7). The incoming fields therefore satisfy

    ||q1_k||_p <= H^10 M^15 sqrt(p),
    ||q2_k||_p <= H^10 M^13 sqrt(p),
    ||C_k||_p  <= H^10 M^11 sqrt(p).                 (1)

Thus their subGaussian scales are at most H^11 times these powers. Indeed the usual power-series expansion of exp(Q^2/L^2), with the even-p versions of (1), converges uniformly when L is a sufficiently large fixed multiple of its displayed coefficient. This argument proves the subGaussian claim; it does not assume that an arbitrary L2 action preserves Gaussian tails.

## 3. Formal derivatives with both current and source-time factors

For one local population use

    Z=xi+K delta, q=zeta+B Hfeat,
    Hfeat=phi(Z), delta=Dcap(Z,q).

The pairs (K,B) are (H_P,B2), (A2,B3), (A3,E Hc). Define

    R=(I-a^2 K B)^(-1), U=R K,
    L=(I-a^2 B K)^(-1).

All three U strict densities are at most H^3. The relevant forward/backward R,L rows are at most H^2 M^5; at bottom only R is needed. Let b=(9,7,4) be the powers for B.

Freeze deterministic coefficients and source covariances. Write J for the formal derivative of Z in named source directions, with direct source matrices Ixi,Izeta. Set

    G=aI+DeltaG, Vgate=aI+DeltaV,
    Lgate=e diag(g'(Z) tau_R(q)),
    P=Lgate+a DeltaV B+a B DeltaG+DeltaV B DeltaG.

The gate bounds, including arbitrary caps, are

    |DeltaG_k|+|DeltaV_k| <= C e,
    |Lgate_k| <= C e Q_k,

where Q_k is the two-sample absolute incoming field norm (or |C_k| at top). No scalar-sector projection is applied to these random gates. Solving the affine part exactly gives

    J=Jaff+U[DeltaV Izeta+P J],
    Jaff=R Ixi+a U Izeta,                           (2)

    Ddelta-Ddelta_aff=L[DeltaV Izeta+P J].          (3)

To verify (3), before elimination its right-hand side is DeltaV Izeta+PJ+a^2 B(J-Jaff); substituting (2) yields (I+a^2 B U)[...]=L[...]. This uses the backward resolvent in its correct orientation and retains the current term in L.

For a single bottom/middle transpose slot j, J_k=0 for k<=j, and the direct forcing in (2) is bounded by H^3 h_j. For a full middle/top forward-source row, the direct forcing has row norm at most H^3 M^5; pad rows by zeros at future slots. The strictness of U and the full causal B-row bound yield

    |J_k| <= H^3 h_j E_k             (transpose slot),
    |J_{k,bullet}|_r <= H^3 M^5 E_k (full forward row),

    E_k=exp{H^6 e sum_{r<k} h_r(Q_r+M^b)}.          (4)

Here is the chronological bound explicitly. The Lgate part of UPJ costs at most C e sum_{r<k}h_r Q_r |J_r|. The other terms cost at most C e M^b sum_{r<k}h_r max_{s<=r}|J_s|. Replacing the derivative norm by its running maximum gives a scalar causal inequality whose majorant is the initial forcing times product_r(1+H^6 e h_r(Q_r+M^b)); the product is at most (4). The transpose initial factor h_j remains in every term. This reasoning includes any causal current B_rr, since r<k in U and the B history satisfies s<=r. It introduces no random time supremum of Q.

For the three source populations, the largest integrated stochastic powers in (4) are 4+(15,13,11)=(19,17,15); the deterministic powers are 4+b=(13,11,8). Consequently the explicit condition

    e H^22 M^19 <= 1                               (5)

ensures E E_k^8 <= 2, after the harmless numerical slack already built into H. One direct proof is weighted Jensen:

    exp(t sum_{r<k}h_r Q_r)
      <=1-s_k/S+sum_{r<k}(h_r/S) exp(t S Q_r).

Apply the subGaussian estimate (1) to each summand. The rate prefactor H^6, duration H, and subGaussian prefactor H^11 multiply to H^18; the spare H^4 in (5) controls factors 8, fixed two-sample conversions, and the scalar Gaussian exponential estimate. The same bound proves any lower fixed moment used below. It also implies value absorption in Section 2.

Now use the stronger, actual primal L2 bounds from Section 1. For every pair of times k,r, Cauchy-Schwarz gives

    E[Q_r E_k] <= ||Q_r||_2 ||E_k||_2
       <= H^2 M^{q_primal},
    q_primal=(3,2,1).                              (6)

This is the exponent improvement. It needs no independence between Q_r and E_k. In particular it applies with r=k and at the original source time, so terminal and source-time multipliers remain present. If an intermediate use of Hölder keeps two such explicit multipliers, the available eighth moments in (4) and the corresponding fixed Lp source bounds provide the original finite-moment truncation requirements; the single derivative defects (2)-(3) themselves contain only one explicit Q factor and use exactly (6).

## 4. All four derivative defects

For a single bottom/middle transpose source, subtract Jaff in (2). The term U DeltaV Izeta has density at most H^4 e. For UPJ insert the transpose bound in (4), apply (6) to Lgate, and apply the deterministic B-row bound to the other three terms. The sum of time weights is at most H M^4. Hence

    E|J_k-Jaff,k| <= H^20 e h_j M^4
                        (M^{q_primal}+M^b).

Since b=9 at bottom and b=7 at middle, this gives strict-density bounds H^20 e M^13 and H^20 e M^11. Multiplying the output by its feature gate G adds only H^4 e h_j; thus the two forward coefficient derivative defects satisfy

    A2 defect density <= H^21 e M^13,
    A3 defect density <= H^21 e M^11.               (7)

For middle/top backward coefficients the source is a complete forward-source row, so Izeta=0. Identity (3), the row bound for L, the forward derivative row bound in (4), and (6) give

    max_k E[sum_{j<=k}|(Ddelta-Ddelta_aff)_{kj}|]
       <= H^19 e M^5 M^5 (M^{q_primal}+M^b).

The resulting powers are

    B2 defect row <= H^19 e M^17,
    B3 defect row <= H^19 e M^14.                   (8)

The deterministic gate terms a DeltaV B and a B DeltaG are retained: they are why the middle exponent here is 17 rather than the tempting but incomplete 12. The maximum over terminal times is outside expectation: for each fixed k, expand the deterministic L row, sum the absolute j entries, and apply (6) uniformly to every pair of times appearing in PJ. This gives the displayed bound uniformly in k. Consequently it bounds max_k sum_{j<=k}|E[(Ddelta-Ddelta_aff)_{kj}]|, which is the deterministic coefficient row norm. No expectation of a random maximum over k is claimed. It includes j=k. In particular Lgate_k J_kk is explicitly controlled using Q_k in (6), and current B_kk factors occur in the retained causal B row. No strict-density estimate for arbitrary backward forcing, nor a minimum step, has been assumed.

Adding the learned-moment density H e M^15 and backward row H^2 e M^19 yields the complete actual coefficient forcing interface

    q <= H^30 e M^19,                              (9)

under (5). It applies to every amplitude along the fixed-cap, fixed-mesh homotopy as long as the source transfer table holds. The response estimates compare with the affine formulas at the exact same deterministic arrays, so there is no uncounted coefficient displacement term.

## 5. Numerical and theorem interface

The deliberately rounded H ledger is:

| Step | Prefactor |
|---|---:|
| outer transfer bounds | H^2 (rows of strict kernels H^3) |
| Gaussian Lp inputs | H^2 |
| value leading/self inequalities | H^6 |
| absorbed Zi | H^7 |
| incoming Q Lp | H^10 |
| incoming subGaussian scales | H^11 |
| derivative initial factor | H^3 |
| exponential rate before time integration | H^6 |
| E[Q_r E_k], using actual primal L2 | H^2 |
| transpose defect | H^20 |
| feature defect | H^21 |
| backward full row defect | H^19 |
| full forcing, including learned moments | H^30 |

Each entry follows from the displayed products and sums. The excess H powers cover a^(-j)<=16, two sample slots and basis changes, fixed Gaussian constants, and factors at most 10^6, using H>=10^30. There is no exponential depending on M except the e-weighted one in (4), already controlled by (5).

If the independent supersolution supplies the strict outer-box closure at

    q <= H^-C M^-12

for any fixed C comfortably below 350, then (9) is compatible with eM32 <=10^-70 H^-399: indeed q M12 <= H^30 eM31 <=10^-70 H^-369. Condition (5) also holds. Since M32 <=24^8 delta^-4 and 24^8<H, the unchanged prefactor e<=c_poly delta^4 implies that smallness.

This note supplies the new response part, not the new affine G3 proof or the coefficient supersolution. Once those interfaces are checked, all original cap removal, clocks, nonsymmetric uniqueness and restart, full-width GF/raw-GD limits, action/kernel/path/velocity laws, and nonaffinity/motion conclusions use exactly the old bridges. The only replacement is (9) and its verified smallness condition (5).
