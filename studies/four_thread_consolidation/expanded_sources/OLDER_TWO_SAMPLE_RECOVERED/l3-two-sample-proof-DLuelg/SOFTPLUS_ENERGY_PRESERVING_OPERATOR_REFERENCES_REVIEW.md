# Isolated adversarial review: energy-preserving uncut operator references

Reviewed candidate: `SOFTPLUS_ENERGY_PRESERVING_OPERATOR_REFERENCES.md`, all 391 lines, in `/tmp/l3-two-sample-proof-DLuelg/`.

Exact candidate SHA256:

```text
464df3966e4d899f8615179968926edfe2b1e592fade50bbde08ba9fdcdd06f2
```

Review date: 2026-09-06. This is an independent mathematical audit of the supplied candidate. No experiments, agents, canonical source, or other project/context files were used. The candidate was not edited. Line references below refer to the candidate with the hash above.

## Verdict and scope

**Conditional pass as a global bounded-kernel reference lemma, with local consistency. No required mathematical correction was identified under the explicitly imported common-space/local-assembly premise.** The continuation, approximation, readout-convexity, action, curvature, and local-comparison arguments withstand the checks below. There are several optional precision improvements, listed separately at the end.

This verdict is **not a Gaussian-initialization global theorem**. It establishes global genuine uncut dynamics for the modified bounded-kernel initializations, uniform primal and stated integrated curvature bounds for sufficiently large reference indices, and consistency on the imported canonical local interval. It does not establish a global canonical limit, a global finite-width limit, uniform reference tail estimates, or control of curvature multiplied by arbitrary source sensitivities. The candidate correctly preserves these distinctions in lines 376–391.

The order and extent of the quantifiers are important:

| Statement | Scope actually supported |
| --- | --- |
| Global physical flow | Every fixed bounded first-field/bounded-kernel initialization with zero readout; no symmetry required for this assertion |
| Symmetric approximating references | The specific symmetry-preserving construction in Section 2 |
| Uniform bounds on a fixed physical horizon | All these references, from uniform initial first-field and operator bounds |
| Positive initial feature speed and finite fitting feature time | All sufficiently large N; the threshold and time bound can depend on fixed rho and labels |
| Uniform bounds for the entire physical life | Those sufficiently large N, by the finite before-fit feature budget and the divergent physical clock |
| Integrated curvature-action bounds | Opposite labels, with the particular weights in (16) and its top-layer counterpart |
| Consistency with the prescribed initialization | Only the imported canonical local interval |

## Accepted-premise scope

The candidate cites `SOFTPLUS_LOCAL_POPULATION_ASSEMBLY.md` with SHA256 `398d12f41a60276cbee91323293c2f64b97055eac935f45ee31b8cac6946c97d`. That source was **not opened or audited**. Its hash here is the candidate's identification of the imported source, not an independently verified hash.

Following the requested scope, I accept the common-space/local-assembly result as a premise, with the interface the candidate expressly uses:

1. Separate generated probability spaces with separable L2, dense bounded query families, compatible bounded initial operators and their Hilbert adjoints, and initial operator norms at most 10. The common-space realization preserves the canonical initialization/query laws, including the initial Gaussian forward covariance recursion.
2. The canonical local path and the old three-cut references exist on the stated common feature interval. Their relevant fields are continuous L2 curves, their local primal bounds are uniform in the old cut radius, and the cut references converge to the canonical local path.
3. The old cut-tail estimate used at lines 354–355 is available in precisely the old readout/backward queries appearing in the multiplication split: a uniform local bound of the form C exp(-c R^2). The given restriction S_* <= 1/196 is also part of the invoked local interface.

I do not independently certify that the cited source supplies this interface. Under the user's instruction it is accepted here. No global conclusion, reference continuation, reference symmetry projection, readout-convexity argument, or new curvature estimate is accepted merely because that source was cited: these are checked below.

## 1. Genuine uncut flow, energy, and L-infinity continuation

### Local construction and raw metric

The L-infinity construction in lines 30–50 is sound. On a probability space a bounded kernel acts boundedly on L-infinity in both orientations. Integration, kernel application, pointwise multiplication, and the stated smooth activation therefore form a locally Lipschitz vector field on bounded sets of the product L-infinity state space. The residual is also locally Lipschitz there. The ordinary contraction construction applies to the displayed uncut equations themselves.

The first-field metric and constants are consistent. For -1 < rho < 1, writing delta_a for delta1_a, the first variation of loss is

    dL[v] = 2 sum_a r_a E[delta_a v_a].

The raw inner product E[v^T C^(-1) u] therefore gives first-field gradient 2 C (r_a delta_a)_a, and its negative is exactly (1). At rho = -1 write Z1=(z,-z). The raw metric is E[v^2], and the loss derivative is 2 E[(r_1 delta_1-r_2 delta_2)v], giving the same reduced equation. The two-row formula preserves the opposite-pair constraint. There is no missing factor of two in this degeneracy.

The kernel and readout gradients follow by Hilbert-Schmidt and L2 transpose pairing. The reference path is C1 in L-infinity and hence in the raw Hilbert metric, so differentiation of loss along it gives (2). In particular, for every time inside its local existence interval,

    integral_0^t ||theta_dot||_raw^2 du = L(0)-L(t) <= 2,
    ||theta(t)-theta(0)||_raw <= sqrt(2t).

These bounds concern kernel increments. They do not involve the possibly large initial Hilbert-Schmidt norm. The resulting operator estimate is

    ||W^ell(t)||_op <= ||W^ell_0||_op + sqrt(2t).

First-field and readout L2 bounds follow similarly. Linear activation growth bounds the forward fields recursively. Bounded gates then give, for example,

    ||delta3_a||_2 <= e ||W4||_2,
    ||delta2_a||_2 <= e ||W3||_op ||delta3_a||_2,
    ||delta1_a||_2 <= e ||W2||_op ||delta2_a||_2.

Thus the common M_T in lines 63–68 is available before any L-infinity continuation argument. No backward-field supremum or initial kernel supremum is hidden in it.

### Exact memory bounds

Integrating the actual rank-one kernel updates gives (3), including both adjoint memories. The scalar coefficients are bounded using L2 alone. For example,

    |E[delta3_b(u) delta3_a(t)]| <= M_T^2,
    ||(W3_0)^* delta3_a(t)||_infinity <= D M_T.

The remaining factor in the q2 memory is H2_b(u). Accordingly,

    q2(t) <= D M_T + C_T integral_0^t (2+e z2(u)) du.

The forward z2 memory leaves delta2_b(u), bounded by e q2(u), after its feature covariance is bounded in L2. This gives the companion inequality for z2. The q1/z1 and z3/readout pairs work exactly as claimed. No estimate replaces a current trained adjoint by its initial adjoint, and no independence of trained fields is used.

For each pair, the sum X satisfies

    X(t) <= A_T + B_T integral_0^t X(u) du,

after absorbing the integrated constant on the fixed horizon. Hence X(t) <= A_T exp(B_T t). The pointwise kernel update is then bounded by an integral of bounded delta and feature suprema. This controls every state component on a putative finite maximal interval.

The continuation is not circular. Fix a finite T, perform the estimates on the portion of the already existing local solution before T, and obtain a finite state bound there. The vector field has bounded velocity and a uniform local Lipschitz constant on a larger ball. A finite maximal endpoint therefore has an L-infinity limit and admits a fresh local extension. This proves global physical existence for each fixed bounded initialization.

The constants involving D and the initial first-field supremum may diverge with N. They are used only for fixed-reference existence, not for uniform comparison.

### Feature ascent before fit

With zero initial readout, g(0)=0. Along feature ascent, the same transpose calculation gives

    g' = ||theta'||_raw^2,
    ||theta(s)-theta(0)||_raw <= sqrt(s g(s)).

On g <= 1 this supplies the same kind of L2 bounds on every bounded feature interval. Replacing the physical coefficients by y_a/2 in the exact memories leaves the Volterra argument intact. In particular, a bounded feature-time endpoint at g=1 is reached by an actual L-infinity solution and can be locally continued. A mere strong endpoint is not being substituted for existence.

### L2 multiplication and differentiability

There is no illicit L2-times-L2-to-L2 estimate in the continuation proof. Backward pointwise products have bounded gates; rank-one updates use fields on separate populations, with

    ||u tensor v||_HS = ||u||_2 ||v||_2.

Forward/backward covariances and readout predictions are scalar L2 pairings.

The candidate also correctly avoids claiming that the activation Nemytskii map is Fréchet differentiable L2 -> L2. Its bounded first-variation formula and chain rule along the existing L-infinity path suffice.

Even the terminology “raw gradient” can be justified in the scalar Fréchet sense at each bounded reference state. For an L2 preactivation perturbation h, the activation remainder obeys

    ||phi(z+h)-phi(z)-phi'(z)h||_1 <= (e/8)||h||_2^2.

Pairing this remainder with a bounded old backward multiplier gives a quadratic scalar error. Successive transpose pairings through the network use bounded old readout and backward queries; terms containing both a kernel perturbation and a feature perturbation are also quadratic by the Hilbert-Schmidt/operator estimate. This establishes the scalar prediction's raw first derivative at such a state, without asserting an L2 Fréchet derivative for the vector-valued activation map. None of these bounded-multiplier constants needs to be uniform in N.

## 2. Initial approximation and symmetry

### Bounded kernels and both strong limits

The construction (6) is valid. Each finite-dimensional range has a bounded orthonormal basis. In these bases, P_out W_0 P_in has the finite kernel

    sum_(i,j) <e_i, W_0 e_j> e_i(x) e_j(y),

which is bounded for fixed N. Orthogonal projections are contractions on L2, so the operator norm remains at most 10. Explicitly,

    ||P_out,N W_0 P_in,N u - W_0 u||_2
       <= 10 ||P_in,N u-u||_2 + ||(P_out,N-I)W_0 u||_2.

Both terms vanish for each fixed u. Applying the same argument to P_in,N W_0^* P_out,N proves the adjoint strong limit. The adjoint assertion is essential and is not inferred from strong convergence alone.

The first-field approximation works with the intended bounded odd truncations converging pointwise to the identity and dominated in absolute value by the identity. Coordinatewise L2 convergence then implies raw convergence for fixed -1 < rho < 1 because C^(-1) is a fixed matrix. At rho=-1 oddness preserves the constraint and the scalar raw norm applies. No uniformity as rho tends to 1 is claimed or needed.

### Construction and use of the symmetry

The generated-algebra argument in lines 168–183 is a legitimate way to obtain the symmetry from the canonical initialization laws. Here is the needed logical content. Adjoin each query's root-exchanged counterpart. On bounded cylinder functions define

    J F(X_1,...,X_m) = F(X_1^swap,...,X_m^swap).

Invariance of their joint finite laws makes this definition independent of the cylinder representation modulo null sets, preserves every Lp norm, and preserves multiplication. Applying the exchange twice gives the identity. Consequently J extends to a unitary involution on L2 and commutes with scalar functional calculus. Exchange of a generated operator query is the same initial matrix applied to the exchanged input query; passing that identity through the common-space construction and density gives (8), and taking adjoints gives the corresponding adjoint intertwining.

The relevant invariance is of the joint initialization/query laws. Exchangeability of only the two root marginal variables, with arbitrary root-dependent initial operators, would not suffice. The note invokes the former through the canonical generated construction; this audit does not silently replace it by the weaker assertion.

An invariant finite span has an invariant orthogonal complement because J is unitary. Its orthogonal projection therefore commutes with J, so (6) preserves the intertwining exactly. There is no conflict between bounded bases, dense increasing spans, and symmetry.

For complete precision, the state involution used in lines 193–205 is

    (T Z1)_a = J_1 Z1_(3-a),
    T W^ell = J_ell W^ell J_(ell-1),
    T W4 = sigma J_3 W4.

Thus the first-field transformation includes J_1 as well as sample exchange. This is the natural reading of the surrounding equations, although the prose at line 201 abbreviates it to “exchange.” The map is an isometry of the raw metric: C commutes with the sample swap, and the degenerate scalar metric is preserved as well.

Under this map f_a transforms to sigma f_(3-a), r_a to sigma r_(3-a), and delta_a to sigma J delta_(3-a). The two sigma factors cancel in a physical hidden update. The feature-ascent equations are equivariant too, since y_(3-a)=sigma y_a. Uniqueness on the bounded reference state space now proves (9). In particular, no symmetry of a trained law is being inferred from independence after training.

## 3. Readout convexity, finite feature budget, and physical clock

Let V(alpha)=(H3_1+sigma H3_2)/2. At a bounded state, the first-variation formula for V defines a bounded linear map from raw hidden tangents to L2. For example, its variations pass successively through

    dot H1 = phi'(Z1) dot Z1,
    dot Z2 = dot W2 H1 + W2 dot H1,
    dot H2 = phi'(Z2) dot Z2,
    dot Z3 = dot W3 H2 + W3 dot H2.

Every term is bounded in L2 by the raw tangent norm using bounded gates, operator norms, and feature L2 norms. This proves the extension invoked at lines 213–219. Along the bounded curve the L-infinity chain rule identifies this extension with the actual curve derivative. Transpose pairing gives alpha'=D V^* W4, so

    W4'' = D V D V^* W4,
    <W4,W4''> = ||D V^*W4||_raw^2 >= 0.

No second derivative of V on all of raw Hilbert space is used.

If k_N=||V(alpha(0))||_2^2>0, then g'(0)=k_N, and monotonicity of g implies g(s)>0 for every positive feature time on its existence interval. Thus W4(s) cannot vanish there. For r=||W4||_2,

    r'' = (||W4'||_2^2-(r')^2+||D V^*W4||_raw^2)/r >= 0.

The expansion W4(s)=s V(alpha(0))+o(s), together with continuity of W4', yields r'(0+)=sqrt(k_N). Therefore r'>=sqrt(k_N), ||V||_2>=r', and g'>=k_N. This proves the claimed lower bound without a pointwise second-variation positivity assertion.

Before-fit continuation and g(s)>=k_N s imply that g reaches 1 by s_N<=1/k_N. If a purported finite maximal time occurred earlier, Section 1 would extend the solution; if there were no hit by 1/k_N, the lower bound would contradict g<1. This is a valid existence-and-hitting-time argument.

Strong initial operator convergence and activation Lipschitzness propagate initial field convergence through both hidden operators. The positive-definiteness argument for the canonical initial top Gram is also correct. For -1<rho<1, a Gaussian pair with full support cannot satisfy a nontrivial linear relation between the two strictly increasing coordinate features. For rho=-1, the sum of the two features is an everywhere positive even function, while their difference is eG, a nonzero odd function. These are orthogonal nonzero L2 functions, giving both positive Gram eigenvalues. The imported Gaussian covariance recursion propagates positive definiteness to the next two layers. Hence

    k_N -> k_0 = (1/4) y^T Q_top y > 0.

Only sufficiently large N are consequently guaranteed a finite s_N. For those N,

    s_N <= S_max = 2/k_0,
    integral_0^s_N ||theta'||_raw^2 ds = 1,
    ||theta(s)-theta(0)||_raw <= sqrt(S_max).

These are feature-time action and displacement statements. The corresponding total dissipated physical loss is 2, not 1; the candidate's use of “one” is correctly in feature time.

On the symmetric locus f_a=y_a g, the full raw gradients satisfy

    -grad L = 4(1-g) grad g.

Thus the physical clock in line 260 has the correct factor. The uniform primal bounds control all raw gradient blocks and hence g' from above by a finite constant. Since g(s_N)=1,

    1-g(s) = integral_s^s_N g'(u)du <= C(s_N-s).

It follows that integral ds/[4(1-g(s))] diverges at s_N. Every finite physical time is represented by the before-fit feature path, and uniqueness identifies this reparametrized path with the globally constructed physical reference. This yields uniform primal bounds throughout those references' physical lives, not a global convergence assertion about the original initialization.

## 4. Actual curvature-action estimates

For opposite labels the symmetry gives E[U^ell V^ell]=0. Expanding the exact feature gradient yields

    (W^ell)' = delta^ell_- tensor U^(ell-1)
                  + delta^ell_+ tensor V^(ell-1).

Its Hilbert-Schmidt cross term vanishes by this forward-field orthogonality, regardless of any correlation between the two backward fields. Since U>=1 on a probability space, the total raw action gives

    integral_0^s_N [ ||delta2_-||_2^2 + ||delta3_-||_2^2
        + kappa1 ||delta2_+||_2^2
        + kappa2 ||delta3_+||_2^2 ] ds <= 1.          (A)

There is no discarded multiplicative factor or sample normalization in (14).

Set p_a=phi'(Z_a). The scalar identity phi''=p-p^2/e implies, for each a separately,

    (p_a-p_a^2/e) q_a
       = [1-(p_1+p_2)/e] p_a q_a + (p_1 p_2/e) q_a.

The coefficients on the right are the same for both samples. Taking half-sums or half-differences therefore proves (15) without unwanted mixed plus/minus terms. The bounds |A|<=1 and 0<=B<=e are valid (the upper bound is a supremum).

Since the current adjoint is linear and shared by the samples,

    q2_+/- = (W3)^* delta3_+/-,
    ||M2_+/-||_2^2
       <= 2||delta2_+/-||_2^2 + 2e^2 M^2||delta3_+/-||_2^2.

Also,

    kappa2 <= e^2 ||W2||_op^2 kappa1 <= e^2 M^2 kappa1.

Combining these inequalities with (A) verifies both estimates in (16). In fact (A) permits the stronger bounds

    integral ||M2_-||_2^2 ds <= 2 max(1,e^2 M^2),
    integral kappa2 ||M2_+||_2^2 ds <= 2e^2 M^2.

The stated constants 2(1+e^2 M^2) and 4e^2 M^2 are conservative, not erroneous.

At the top layer q3_a=W4 is the same field for both samples. As a function of p in [0,e], p-p^2/e has derivative in [-1,1], so

    |phi''(Z3_1)-phi''(Z3_2)| <= |p_1-p_2|.

Further, 0<=phi''<=phi'. Factoring the common W4 proves both pointwise inequalities |M3_-|<=|delta3_-| and |M3_+|<=|delta3_+|, even when W4 changes sign. Their jointly weighted integral is at most 1 by (A).

These are estimates for the actual globally existing uncut references. They are integrated L2 estimates with the indicated weights. They give neither a bound for multiplication by an arbitrary correlated L2 sensitivity nor a uniform pointwise curvature bound. No division by a possibly vanishing kappa is used.

## 5. Local consistency with strong, not operator-norm, approximation

### The operator error has the correct fixed inputs

The split (17) is exact. With Delta K=K_N-K_R and A_N=W_(0,N)-W_0,

    W_N H_N-W_R H_R
       = W_N(H_N-H_R) + Delta K H_R + A_N H_R.

For adjoints the identical expansion is

    W_N^* delta_N-W_R^* delta_R
       = W_N^*(delta_N-delta_R)
          + Delta K^* delta_R + A_N^* delta_R.

Thus strong convergence is applied only to the old reference's H1_R, H2_R, delta2_R, and delta3_R. At fixed R these inputs range over compact sets in L2, because they are continuous images of a compact time interval. Uniform operator bounds plus a finite epsilon-net prove uniform convergence on each such compact set. This establishes epsilon_(N,R)->0; it does not require compactness of the family of new reference fields.

### The cut-radius dependence stays linear

For one backward stage the displayed old-cut split gives explicitly

    ||phi'(z_N)v_N-phi'(z_R)tau_R(v_R)||_2
       <= e||v_N-v_R||_2 + e||v_R-tau_R(v_R)||_2
          + (e/4)||tau_R(v_R)||_infinity ||z_N-z_R||_2.

Up to a fixed cutoff convention, its last coefficient is O(R). Propagating a previously obtained backward-field difference through the next current adjoint costs a bounded operator norm; through the next gate it costs at most e. The next O(R) term is a new additive forward-field error. No stage multiplies the already accumulated O(R) error by another R.

Forward differences are bounded by C(d+epsilon_(N,R)) using (17), the activation Lipschitz bound, and uniform primal norms. The backward recursion consequently yields

    backward-field differences
       <= C(1+R)(d+epsilon_(N,R)) + C tails_R.

For a kernel velocity, use

    delta_N tensor H_N-delta_R tensor H_R
       = (delta_N-delta_R) tensor H_N
          + delta_R tensor (H_N-H_R).

The factors multiplying the field differences have uniformly bounded L2 norms. The first-field metric contributes only fixed constants. In physical time the residual difference is controlled by the same forward/readout bounds; in the local feature-time comparison the coefficients are simply y_a/2. This proves the form and the linear R dependence of (18). There is no need for an L-infinity bound uniform in N.

### Limits and velocities

Let eta_N denote the initial first-field raw distance. At fixed R, the integrated comparison gives a bound of the form

    sup_[0,S_*] d(theta_N,theta_R)
       <= exp(C(1+R)S_*) [ eta_N
             + C(1+R)S_* epsilon_(N,R)
             + C S_* exp(-cR^2) ].

First N tends to infinity with R fixed. Then R tends to infinity. This proves the claimed local state convergence after using the accepted old-cut convergence. Neither strong convergence uniformly over N-dependent inputs nor an exchange of these limits is used.

The velocity conclusion is supported as well. Substitution back into (18) bounds, after the N limit, the uniform velocity distance to the fixed old-cut velocity by a polynomial factor in R times exp(C(1+R)S_*-cR^2). This tends to zero. In particular the new-reference velocities form a uniformly Cauchy sequence in the raw Hilbert space. The integrated evolution identity and uniform state convergence identify its limit as the canonical path's derivative. This also justifies the velocity claim without assuming that unquantified state convergence alone can be multiplied by R.

### Common feature interval and the numerical bound

The small-time argument in lines 369–373 can be checked directly. On a before-fit interval with s<=1/10, (5) gives raw displacement at most sqrt(s)<=1. Each first-field coordinate displacement is bounded by this raw norm: for -1<rho<1 the coordinate functional has squared dual norm C_aa=1; the scalar case is the same. With the intended dominated truncation, each initial coordinate has L2 norm at most 1. Consequently one may use the deliberately loose bounds

    ||Z1_a||_2 <= 2,  ||W2||_op,||W3||_op <= 11,
    ||W4||_2 <= 1,
    ||H1_a||_2 <= 2.2,
    ||H2_a||_2 <= 4.42,
    ||H3_a||_2 <= 6.862.

The norms of the readout, third-layer, second-layer, and first-field feature-gradient blocks are respectively bounded by

    6.862,  0.442,  0.242,  0.121.

For the first-field block use the triangle inequality for the two sample covectors, each having unit input-metric norm. Squaring and adding gives

    g' <= 6.862^2 + 0.442^2 + 0.242^2 + 0.121^2
       = 47.355613 < 49.

Thus g(s)<=49s before fit. A fitting time no later than S_*<=1/196 would contradict g=1 there, since this estimate gives at most 1/4. If an existence endpoint occurred earlier, before-fit continuation would extend it. The entire common local interval is therefore available to the comparison. The argument also covers any early reference with k_N=0: it does not need the finite-fit conclusion for every N.

## Required fixes, optional improvements, and boundaries

### Required mathematical fixes

None identified under the accepted premise and the intended ordinary truncation convention. The numerical factors, metric, adjoint orientation, curvature algebra, and sequential limits are consistent. This is an adversarial mathematical review, not a machine-checked proof certificate.

The accepted-premise interface above remains a dependency, rather than a new result certified by this report. Likewise, removing the fixed-initialization, sufficiently-large-N, opposite-label, weighted-integral, or local-interval qualifications would change the theorem and would not be justified by this proof.

### Optional precision improvements

1. **Specify the scalar truncations** (lines 158–165, 370). State explicitly that tau_N is bounded, smooth and odd, tends pointwise to the identity, and satisfies |tau_N(x)|<=|x|. These are the properties already used by “domination” and by the initial marginal bound. A uniform cap convention for tau_R in the old-cut comparison would similarly make its O(R) factor explicit.
2. **Write the full first-field symmetry map** (lines 201–203): `(T Z1)_a=J_1 Z1_(3-a)`. Sample exchange alone does not fix the realized initial pair; the displayed J relation makes the intended combined transformation unambiguous. Also specify that joint initialization/query-law invariance, not just root-marginal exchangeability, supplies J.
3. **Expand the local backward recursion by one inequality** (lines 335–354). The estimate above makes transparent why the coefficient is linear in R and why the old tail terms are not multiplied by an accumulating sequence of cut radii. This is an exposition improvement; the displayed split already has the needed structure.
4. **Include a short verification of the 49 bound and distinguish time variables** (lines 369–373 and the introduction to Section 4). The calculation above confirms the constant. Stating explicitly that theta_N and theta_R in the local comparison are parameterized by feature time avoids a possible reading in physical time.
5. **Optionally tighten (16).** The stronger constants derived above follow from the joint action budget, but do not improve the theorem's scope or resolve the global-limit gap.

### Conclusions that remain outside this audit's positive verdict

- The existence or global continuation of the canonical Gaussian-initialization flow beyond the imported local interval.
- Uniform control of D_N, reference L-infinity norms, Gaussian tails of reference fields, or initial Hilbert-Schmidt norms.
- Operator-norm convergence of the initial operators or uniform strong convergence over arbitrary bounded families of evolving inputs.
- Bounds on products of curvature fields with arbitrary correlated source sensitivities, or the missing nonlinear comparison on later intervals.
- A global population/finite-width interchange or the canonical global theorem.

The candidate's new contribution survives within its stated scope: global exact uncut reference flows, preserved energy and readout-convexity structure, a uniform finite before-fit feature budget for sufficiently large references, the stated actual curvature-action estimates, and local consistency with the accepted canonical path.
