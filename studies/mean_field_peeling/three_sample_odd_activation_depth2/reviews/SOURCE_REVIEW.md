# Independent final source audit: three samples, two hidden layers

Date: 2026-09-08. Scope: the five mathematical files below, judged as partial results only. No experiments were run and no canonical file was edited by this reviewer. Earlier reviews were not used as premises. The exact Gaussian-conditioning and cap-comparison arguments in the older mathematical dependencies were inspected where needed.

## Frozen files and verdict

All paths in this table are relative to `/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/`.

| File | SHA256 |
|---|---|
| REPORT.md | `25cfd1e93b619b6c5aabc674cab7170199024ac7a3cb700365a23048e62d341f` |
| CONTRACT.md | `e4acafb4b6dee57ab867bd3947a92b6b25d994c51e62bbfaeaaccebede6c113d` |
| GEOMETRY_AND_NECESSARY_SCALES.md | `37a6c0bf1715ab5a182ecfd9a6a3213cddf9cb4a0ae95fd441a5a6a7d46f61e6` |
| SOURCE_AND_CONTINUATION.md | `4c3b8c54893a417ce210f73eaae2b8e71a71eac8f3205f5fdc32da9480c2a568` |
| NONLINEAR_REFERENCE.md | `778793eb7a832f16dadc5b5746e9b705c02ca08a74ab9e3f81748962a958a422` |

**PASS for the stated partial results and their stated scope. This is not a pass for the requested complete theorem.** I found no remaining mathematical defect in the frozen claims. The full polynomial-threshold/global population/GF/GD result remains open exactly where the report says it does. The source bounds can additionally close an initial, fixed short interval; an independently checked construction is given in the appendix. It supplies no arbitrary-horizon continuation result.

One wording defect was reported during the audit and repaired before the above freeze: a bounded L2 ball is uniformly integrable in L1, whereas its squared magnitudes need not be uniformly integrable. The current SOURCE §5 uses the correct squared-magnitude/L2-tail statement. This repair changes no estimate or conclusion.

## 1. Exact single-action source identities

The forward and reverse formulas have the correct orientations and time conventions. Unrolling the learned action gives

    A_k h_{k,i} = A_0 h_{k,i}
        + sum_{r<k,j} h_r c_{r,j} b_{r,j} E[h_{r,j}h_{k,i}],

    A_k^* b_{k,i} = A_0^* b_{k,i}
        + sum_{r<k,j} h_r c_{r,j} h_{r,j} E[b_{r,j}b_{k,i}].

Here `h_r` outside a sample index is the mesh step, as in the source note. Gaussian conditioning on both orientations of this same initialized matrix adds respectively

    sum_{r<k,j} b_{r,j} E[partial_{zeta_{r,j}} h_{k,i}],
    sum_{r<=k,j} h_{r,j} E[partial_{xi_{r,j}} b_{k,i}].

This verifies the displayed source A/B coefficients. There is no new independent matrix at a later time. Independence of the primitive xi and zeta groups does not assert independence of their corrected forward/reverse answers.

The underlying conditioning argument is applicable at fixed cap and fixed finite mesh: the coordinate maps phi and D_cap have bounded first derivatives, all contractions/controls can be frozen causally, and Gaussian roots have finite second moments. For singular covariance, the formal named-slot convention is necessary and is explicitly retained. Independent query regularization and finite-program continuity remove the rank assumption; the contracted correction, rather than an arbitrary off-support derivative representation, is the invariant object.

The current term is exactly diagonal. Since C_k and all b_r for r<k use only past xi slots, partial_{xi_k} Z_k=I and partial_{xi_k} C_k=0. Hence

    B_kk = diag E[e g'(Z_{k,i}) tau_cap(C_k)].

The bound `||B_kk||_infty <= e ||C_k||_2` follows from `|g'|<=1` and `|tau_cap(C)|<=|C|`. It does not control the past rows.

## 2. Exact derivatives and produced constants

With deterministic arrays and covariances frozen, direct differentiation gives all three displayed J/U/T recursions. Both N1 and N2 occur. The top readout integral does not cancel N2, and the bottom recurrence retains the current B_rr term multiplying J_rj. That term is causal because J_rr=0. No omitted middle-layer equation is needed at depth two.

For the norms stated in the note, the estimates are consistent:

* `||Gamma diag(c_r)||_infty <= ||c_r||_1 <= 3` supplies the bottom factor 3.
* The primitive Gaussian standard deviations are at most 1, B1, and R for z0, xi, and zeta. The constants 6 are conservative.
* Bottom discrete Gronwall gives U1. At the top, bounding the nested time sum by T times one Volterra sum gives U2; C then has constant MC=3TU2. These concern maxima of marginal norms, not a random supremum over mesh times.
* The random component maximum of q has Lp constant at most Lq=3Mq by Minkowski. This accounts for the factor needed in the bottom derivative exponent.
* Summing the top U source blocks gives the scalar majorant `exp(3 alpha T^2 + alpha e sum h_r |C_r|)`. Summing the T blocks adds at most 3T. The current multiplier therefore gives the full factor `e|C_k|+3T` in the B-row estimate.

The claimed exponential-moment implication is valid: for `||X||_p<=M sqrt(p)`, the m-th nonconstant term in the series for `E exp(X^2/(8 exp(1)M^2))` is at most `4^-m`, so the expectation is at most 4/3 and therefore at most 2. Completing the square yields the stated bound for `E exp(u|X|)`. Weighted Jensen applies to the time integral without any temporal independence.

In particular, the coefficient-production constants check exactly under the chosen norms:

    alpha_new <= 3 B1^2
        + 6 exp(3 beta T + 18 exp(1)e^2 T^2 Lq^2),

    beta_new <= 3 T R^2
        + sqrt(2)(sqrt(2)e MC+3T)
          exp(3 alpha T^2+4 exp(1)alpha^2 e^2 T^2 MC^2).

The A response uses `E||J|| <= 3h_j E exp(...)`. The B response uses Cauchy--Schwarz with the current factor `e|C_k|+3T`; the square-root exponential moment accounts for the coefficient 4 in its exponent. Learned contractions contribute exactly the safe bounds 3B1^2 and 3TR^2. Thus no missing sample or row-sum factor invalidates the conditional lemma.

## 3. Energy, continuation, and scope

The raw equations follow from the stated metric and genuine adjunction. For an already existing true strong trajectory, the chain rule gives `Ldot=-||Thetadot||_raw^2`. Path-length Cauchy--Schwarz gives the stated radius sqrt(3T/2), and the same estimate on shrinking intervals gives a strong raw endpoint at finite terminal time. At finite width, the positive definite fixed-width raw metric converts this bound into the usual finite-dimensional continuation bound; the finite random readout and initial loss are correctly retained.

These facts do not produce a local existence theorem at every endpoint in the infinite-dimensional space. The source-coefficient inequalities are coupled nonlinear radius estimates, not a linear Gronwall inequality. Nor does failure of their crude algebraic closure imply actual response explosion.

The stated ambient-space obstruction is real. A readout can be an unbounded L2 function on a set where `|phi''(Z_i)|` has a positive lower bound. Multiplication by `C phi''(Z_i)` is then unbounded on L2. The rank-one Hilbert--Schmidt variation `delta A=v tensor h_i/||h_i||_2^2` realizes every L2 variation v of that sample's top preactivation. Thus initialized operator boundedness does not give a uniform local Lipschitz constant on raw balls. This example concerns ambient states, not a reached-state counterexample.

Ordinary incoming-field clipping is not the original loss gradient, so assigning it the exact true energy identity would be invalid. The report avoids doing so. A bounded Galerkin family likewise has no automatic strong compactness sufficient for nonlinear gates or action products.

The bridge in SOURCE §6 is correctly conditional. With a uniform raw bound/slack and uniform response coefficients, the proved marginal subGaussian estimates give cap tails. The asymmetric gate identity puts one cap factor on forward-state discrepancies; incoming backward discrepancies only receive bounded factors. Gaussian tails dominate the resulting exponential propagation in the cap. The same comparison supports uniqueness against bounded-primal competitors without requiring their tails. Full-width and velocity/path claims still require the fixed-program, Euler, and ordered observational truncation arguments named in the source; energy alone supplies none of them.

## 4. Geometry and reference cross-check

I also independently checked the companion conclusions relevant to overall accuracy:

* The dual tensors have unit norm, annihilate the other two cubic tensors, and pair with their own by at least delta(2-delta). Summing the three coordinate inequalities gives the factor 1/3 in the lower bound for the cubic Hadamard Gram.
* Gaussian integration by parts gives `E[atan(G)(G^3-3G)]=1-2m`. The cubic-chaos projection gives the stated first Gram bound; Gaussian first-chaos regression preserves at least a^2 through layer two. The explicit numeric lower constant follows from the stated interval estimate and is correct.
* The nearly collinear second-difference family gives the upper scale theta^2 delta^2 through layer two. It satisfies the closed pairwise condition for the stated delta range. No independence of M,D,B0 is required.
* Equilateral cancellation gives the state bound `3R+R^2/2 >= 1/(pi theta)` and hence the stated excursion and fitting-time lower bounds. The initial derivative and the leading coefficient `y^T Q2 y=6 eta theta^2+o(theta^2)` are consistent. These refute a theta-independent rate without refuting positive-theta fitting.
* The scalar-clock lemma is conditional on strong continuation and justified symmetry. Its radial monotonicity calculation, path-length estimate, and divergent physical clock at a first hit are valid under those premises.
* For the frozen nonlinear-feature reference, the finite-dimensional invariant is exactly `BB^*-C tensor C=P_E`. It yields `B^*B>=I`, the output-Gram floor, exponential fitting, and the quartic readout bound. Bounded factors then give global continuation of this different reference model.
* In the equilateral reference states, `A^*C/c^2 -> e0`, and multiplication by the bounded vector U gives the nonzero bottom-gradient limit. Restoring the upper nonlinearity contributes errors of orders sqrt(theta) and theta. The common alpha term uses equal Gaussian marginal laws under sample permutation, and the constant part of the bottom gate cancels by sum u_i=0. The final physical force is therefore the displayed nonzero `3j(1-j)TU/tau^2`.

The reference argument compares vector fields at constructed reference states. It neither proves that the actual trajectory passes through those states nor rules out a more sophisticated stable comparison. The frozen files respect this distinction.

## Appendix: an initial local interval can actually be closed

This is an extra bounded-time result of the present audit, not a change to the canonical five-file statement. It uses the same fixed-cap/common-action construction and smooth clips as the cited source machinery. It does not claim existence or restart at an arbitrary later endpoint, generic fitting, or the complete target theorem.

### A. Cap-independent primal slack without using capped energy

Stop a capped physical path or Euler program at raw distance one from the canonical initialization. Within this ball, `||A0||<=2`, C0=0, and the forward/backward norm bounds give

    ||h_i||_2<=2,  ||A||<=3,  ||Z_i||_2,||H_i||_2<=6,
    ||C||_2<=1,  ||b_i||_2<=1,  ||q_i||_2,||d_i||_2<=3.

Consequently `||c||_1<=3(1+6)=21`. The three raw update-block norms are at most 63, 42, and 126. Their joint Hilbert norm is at most

    sqrt(63^2+42^2+126^2)=147.

This uses only `|D_cap(z,q)|<=|q|`, not an energy identity. On any interval of length at most 1/294, a first exit of the radius-one ball is impossible: total raw displacement before that exit would be at most 1/2. The same argument works for explicit Euler nodes and their segment interpolation by summing update norms.

### B. A concrete response supersolution on T0=10^-6

Replace the control constant 3 in the source proof by m=21. With B1=2, R=1, take

    T0=10^-6,  alpha=200,  beta=1.

The identical derivation gives

    U1=(6+6mRT)exp(m beta T),
    U2=6B1 exp(m alpha T^2),
    Mq=6R+beta U1,  Lq=3Mq,  MC=m T U2,

    alpha_new <= m B1^2
        +2m exp(m beta T+2 exp(1)m^2 e^2 T^2 Lq^2),

    beta_new <= m T R^2
        +sqrt(2)(sqrt(2)e MC+mT)
          exp(m alpha T^2+4 exp(1)alpha^2 e^2 T^2 MC^2).

For every T<=T0 and 0<e<=1/2, elementary bounds give

    U1<6.001,  U2<12.001,  Mq<12.001,
    Lq<36.003,  MC<0.000253.

The exponent in alpha_new is below 0.000022, hence

    alpha_new < 84+42 exp(0.000022) <127<200.

The exponent in beta_new is below 0.000001, hence

    beta_new <0.000021
        +(0.000253+0.000030)exp(0.000001)
        <0.001<1.

These are strict improvements with constants independent of cap and mesh. The chronological construction makes the bootstrap noncircular: A_k depends only on previous B rows; after A_k is bounded, the top forward row and B_k are constructed. Initialization has C0=0 and B00=0. Induction gives the alpha-density and beta-row bounds for every finite mesh in this interval, while part A supplies B1, R, and m independently.

### C. What this establishes, and where it stops

Parts A and B verify the source lemma's premises uniformly on this initial interval. The fixed-cap Euler/common-action construction therefore has uniform marginal subGaussian incoming-field tails. The asymmetric cap comparison then gives strong cap removal and a canonical strong uncut population solution on [0,T0], with uniqueness there against bounded-primal strong competitors. This is a local use of the same bridge already described in the source note; it does not assign energy to the capped flow.

Nothing here makes the reached state a fresh Gaussian initialization. Applying the same numerical box again from a later time would require new control of its inherited source history and response radii. Thus this explicit local closure leaves the report's arbitrary-horizon continuation gap intact.
