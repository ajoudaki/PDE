# Isolated adversarial complete-proof audit

Verdict: **CLEAN** for the exact first-layer compact containment theorem in PROOF.md, lines 138–273, including its stated consequences and the explanatory conclusions through line 1597. No substantive correction, missing hypothesis, or counterexample was found. This verdict does not extend the theorem to an identified population evolution, a full-width limit, or any of the stronger assertions excluded in Section IV.12.

## Input identity and full read scope

Audit date: 2026-09-09.

The only substantive inputs read were:

| Input | Full scope read | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| `/tmp/pde-first-layer-round2.5KzDckqd/PROOF.md` | Lines 1–1597, fully through EOF | 66376 | `02500ea3eee80f9dadd36790a5ccaea6258c06d0c6901564b54417624452ef93` |
| `/tmp/pde-first-layer-round2.5KzDckqd/NOTATION.md` | Lines 1–98, fully through EOF | 5110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

Both hashes were computed directly from the input files before the audit and rechecked after writing this report; both were unchanged. A truncated portion of one batched display was reread in an overlapping, untruncated display; no substantive input portion was left unread. Line references below are to PROOF.md unless explicitly marked NOTATION.md.

No source repository, study, prior review, history, other agent, skill document, internet resource, or subagent was consulted. No experiments, generators, installations, builds, or Git operations were performed. Neither input was edited. The report directory was genuinely created by `mktemp -d /tmp/pde-first-layer-isolated-audit.XXXXXXXX`, which returned `/tmp/pde-first-layer-isolated-audit.G8FWmxjK`. This REPORT.md is the only audit artifact created, and it was created with apply_patch.

## Target and interpretation checked

The target fixes a finite physical horizon T, deterministic normalized inputs, and a fixed correlation −1 ≤ ρ < 1. For fixed α, β, b₄, it asserts one deterministic compact subset of P₂ of the strong joint position/velocity/activation/activation-velocity space, containing every admissible GF outcome at every width and every admissible raw-GD outcome above one deterministic width threshold. It then gives Gaussian compact containment in probability and structural, raw-row, kinetic, and residual-weighted kernel conclusions along any W₂-convergent subsequence.

The audit kept those quantifiers. In particular, it did not add a first-weight operator bound, a positive gate lower bound, a nonvanishing residual assumption, a zero finite readout, independence of trained forward and reverse fields, an identified population equation, or equality of GF and GD limits.

## 1. Normalization, actual dynamics, and global finite GF

Checked lines 3–9, 13–136, and 282–424 against NOTATION.md, lines 10–42 and 70–88.

- There are two samples, so the unhalved sum loss is twice the notation contract's mean loss. Halving the sum-loss velocity gives mean-loss flow; doubling the sum-loss GD step gives the identical mean-loss parameter update. The stated clock bookkeeping is consistent.
- The prediction has the stored readout divided by n; first preactivations use x/√d; the second hidden matrix has no additional forward normalization. The stated δ fields are n times the corresponding prediction derivatives. Differentiating all three parameter blocks gives exactly (IV.23).
- The raw metric has weights 1/n, 1, 1/n. Its negative gradient is exactly (IV.6), and its simultaneous Euler update is exactly (IV.7). All three GD right-hand sides are evaluated at the old node. No transformed-coordinate Euler scheme or sequential block update is substituted.
- The loss derivative is exactly minus the squared raw speed, including the 1/n factors on first weights and readout. At fixed finite n and d, this metric is positive definite. A finite terminal time would give a Cauchy parameter trajectory by (IV.25), hence a finite endpoint where the smooth vector field extends the solution. This proves global finite GF; no coercivity of the loss is needed.
- The arctan bounds used throughout are valid: |φ| ≤ B, 0 < φ′ ≤ 1, and |φ″| ≤ 1. None depends on the magnitude of the first weights.

The primal bounds in (IV.26)–(IV.28) have the displayed constants. In particular, readout coordinates satisfy β + BK_c t, and the middle-matrix operator increment is bounded by BK_c times that readout bound. Integrating gives A_F exactly as written. The first-node equation is v_a = Σ_b G_ab c_b δ_b; |G_ab| ≤ 1 gives its RMS bound. The initial two-coordinate fourth-moment assumption bounds each sample's initial RMS by b₄^(1/4).

The reverse-query calculation in lines 373–405 differentiates the actual transpose of the actual middle matrix. Its bounds are

    RMS(dot z²_a) ≤ D_A B + A K_c Q,
    RMS(dot δ²_a) ≤ D_w + M D_Z,
    RMS(dot q¹_a) ≤ D_A M + A D_δ.

The middle line uses the coordinatewise readout bound, so an uncontrolled product of two merely RMS-bounded hidden fields does not enter. This is a valid dimension-independent query regularity estimate.

The three kernel terms in (IV.32) are the three raw-gradient pairings. Their normalizations are correct. Each entry is at most K_* in absolute value, so its 2-by-2 operator norm is at most 2K_*. From dot r = −2kr and c = −2r, the stated bound Σ_a |dot c_a| ≤ 8√2 K_* R₀ follows.

## 2. GF row work and moment gain

Checked lines 426–521.

The controlled query u = cq has an empirical RMS bound on the sum of the absolute sample derivatives. Minkowski gives the envelope bound (IV.38) with V_F = K_c Q + T K_u. This uses a second moment of the envelope, without assuming a coordinatewise width-independent query bound.

For an actual first row w_i, the exact identities are

    dot w_i = X e_i / √d,
    v_i = G e_i,
    |dot w_i|² = e_iᵀ G e_i = Σ_a u_{a,i} s_{a,i}.

Thus integrating by parts against bounded h controls the nonnegative row action by 2B υ_i. Both endpoint terms and the total variation of u are included. The bound is linear in υ_i; it is not an estimate obtained by squaring its supremum.

Since G is positive semidefinite with eigenvalues in [0,2], |Ge|² ≤ 2 eᵀGe. Consequently

    ∫ |v_i|² ≤ 4B υ_i,
    sup |v_i| ≤ 2υ_i,
    ∫ |v_i|³ ≤ 8B υ_i².

Together with the envelope second moment these give the space-time cubic bound and the fourth moment of the path's L² velocity norm. The path displacement bound gives

    average sup |z_i|⁴ ≤ 8b₄ + 128B²T² V_F².

The constants in (IV.42) follow. Since s = φ′(z) ⊙ v, all the asserted activation-velocity bounds follow as well. This argument remains valid for singular G and does not yet invert it.

## 3. Exact raw-GD descent: no circular stability assumption

Checked lines 523–641, especially 544–628.

The stopped argument is correctly ordered. Prior residual bounds control each update generating a candidate exit endpoint. Summing the readout increments first, and then the middle-matrix increments, bounds both endpoint norms by M_G and A_G. Convexity bounds the entire raw affine segment, including a candidate exit segment. This part does not use loss descent.

The raw Hessian estimate was independently checked, including its dependence on width. For a unit raw tangent ξ,

    ||ξ¹||_F ≤ √n,  ||ξ²||_F ≤ 1,  ||ξ³|| ≤ √n.

Input normalization gives the first-variation estimates in (IV.44). Writing J₀ = B + A, the first prediction variation is bounded by F_* = B + MJ₀.

The mixed second hidden variation has two matrix/first-weight cross terms and one W²-weighted gate-curvature term, exactly as in (IV.45). The two cross terms each have RMS at most one. For the last term,

    ||u ⊙ v|| / √n ≤ √n (||u|| / √n)(||v|| / √n),

so its RMS bound is A√n. No dimension-free bound is incorrectly asserted for this product.

The second prediction derivative has all four terms displayed in lines 585–592. In the gate-curvature term at the second layer, the coordinatewise readout bound permits

    (M/n) Σ_i |(D_ζ z²)_i (D_ξ z²)_i| ≤ M J₀².

The term containing the mixed hidden variation contributes at most M(2 + A√n). Thus

    F_**(n) = 2J₀ + MJ₀² + M(2 + A√n)

is valid; the √n growth is retained. This yields the raw Hessian bound H_*(n) in (IV.47).

At an admissible old node, the actual raw update direction has norm at most K_c F_*. The first variation controls each prediction change along the entire segment by ηK_c F_*², giving the segment residual bound R + 1 under the first small-step condition. Taylor's integral formula then gives loss decrease by at least (η/2)||g_k||² under ηH_*(n) ≤ 1. This bounds the candidate endpoint residual by R₀ < R, excluding exit.

Both conditions hold for η = n⁻² since H_*(n) is a constant plus a constant times √n. The constants depend on T, α, β, and the fixed activation, but not on b₄, d, or ρ. Summing this actual descent inequality gives (IV.49). The proof correctly avoids asserting exact loss dissipation inside a GD cell.

## 4. Raw-GD query increments, row work, and recomputed fields

Checked lines 643–788.

The affine raw interpolation gives held update velocities for W², W³, and z¹. The fields z², δ², q¹, and c are recomputed and continuous across nodes. Product differentiation along cells gives (IV.51), and integrating gives the node increments. The exact endpoint product expansions in (IV.52) include the cross effects of simultaneous updates through their use of the new endpoint in the second product term.

The bound Σ_a |dot c_a| ≤ 4K_c F_*² follows from two samples and c = −2r. For the controlled node query,

    Δ(c_a q_a) = (Δc_a) q_{k,a} + c_{k+1,a} Δq_a,

both endpoint controls are available after the descent proof. This gives (IV.54). The envelope in (IV.55) uses exactly nodes 0 through N−1, which generate the actual cell velocities; it need not include u_N. The estimates

    average υ_i² ≤ V_G²,   max_i υ_i ≤ √n V_G

are established before any row-work absorption.

The raw first-weight update gives Δz_i = ηGe_{k,i} and |Δz_i|² ≤ 2η²a_{k,i}. Taylor expansion of the activation at the old node has the signed work term and remainder

    Σ_a u_{k,a,i} Δh_{a,i} = ηa_{k,i} + r^Tay_{k,i},
    |r^Tay_{k,i}| ≤ η²υ_i a_{k,i}.

This is a bound relative to the actual row action, not an unverified transformed-Euler identity. The condition ηυ_i ≤ 1/2 follows uniformly from V_G n^(-3/2) ≤ 1/2. Summation by parts, including the final h_N term, bounds the total work in absolute value by 2Bυ_i. Therefore

    (1 − ηυ_i) Σ_k ηa_{k,i} ≤ 2Bυ_i,
    A_i^G ≤ 4Bυ_i.

This verifies (IV.59) and all three jointly sufficient threshold conditions in (IV.60), without circular use of the action bound.

On each cell the actual preactivation velocity is Ge_k. The activation derivative is instead φ′(z(t)) ⊙ Ge_k, with recomputed z(t). The proof retains this distinction. Integrating through the full N cells to establish a nonnegative action bound also bounds a partial terminal cell. The resulting constants in (IV.61)–(IV.62), including 512B²H²V_G² for the path fourth-moment contribution, are correct.

## 5. Antiparallel endpoint and recovery of the controlled field

Checked lines 790–850 and the endpoint uses in lines 1339–1369 and 1516–1519.

At ρ = −1, normalized inputs satisfy x₂ = −x₁. Odd activations and even activation derivatives give, for every raw parameter state,

    z₂ = −z₁, h₂ = −h₁, f₂ = −f₁,
    δ²₂ = δ²₁, q¹₂ = q¹₁, δ¹₂ = δ¹₁.

The actual opposite labels then give c₂ = −c₁. These statements allow an arbitrary, nonzero stored readout, so they apply to the stated finite Gaussian initialization and to every point inside raw GD cells.

The controlled e and u fields, as well as z, h, v, and s, lie in E_- = {(b,−b)}. On that subspace G acts as 2I. Hence e = Dv with D = G/4, and ||D|| = 1/2. In the interior, the corresponding identity uses D = G⁻¹ with norm (1−|ρ|)⁻¹.

This resolves the potential nullspace obstruction. A pseudoinverse alone would not recover individual controlled kernel entries for arbitrary e at a singular Gram matrix; the architecture and label identities establish the needed range constraint here. No limiting argument in ρ is substituted for it.

## 6. Strong translations uniform over every admissible GD width

Checked lines 852–1041.

The assembled estimates distinguish an instantaneous empirical RMS velocity bound, a space-time L³ bound, and a fourth moment of the path L² norm. Each has been separately proved. The derivative/increment bounds on u give the shifted L² estimates in (IV.72). For GD the node gate has a τ + η displacement bound; the recomputed continuous position has a τ displacement bound. The index count is valid also near the final partial cell.

The special relative gate estimate is correct. Since |(log φ′)′| ≤ 1,

    θ(x,y) = |φ′(x)−φ′(y)| / (φ′(x)+φ′(y))
           ≤ min(1, |x−y|/2).

For arbitrary real controls u,v, the algebra in (IV.74) bounds the gated difference by 2|u−v| + θ(|a|+|b|). It does not divide by u, v, a residual, or a lower bound for φ′. Taking the maximum of the two scalar θ values yields the stated two-vector estimate without an extra sample factor.

The identification e = Dv supplies the necessary L³ bound for e. With empirical space-time measure, θ ≤ 1 implies

    ||θ||₆⁶ ≤ ||θ||₂² ≤ (TK_z²/4)(τ+ε)².

Hölder with 1/2 = 1/6 + 1/3 therefore gives the (τ+ε)^(1/3) contribution to the L² norm of the gated difference. This verifies (IV.75) and the squared velocity-translation bound (IV.76). For the recomputed activation derivative, the ordinary gate-difference bound and the continuous-position shift bound give (IV.77).

The remaining η is genuinely removed uniformly. For 0 < τ ≤ η, the step velocity changes only when the shift crosses an internal node. There are at most T/η such nodes; each crossing set has length at most τ. The empirical squared difference at any starting time is at most 4K_z². Thus (IV.78) holds without extending trajectories outside [0,T]. Combining it with (IV.76) gives

    shift² ≤ min{ C₀(τ+η)^(2/3), 4TK_z² min(1,τ/η) }.

For 0 < τ < min(1,T), splitting at η = τ^(3/5) bounds both cases by a constant times τ^(2/5). Equation (IV.77) transfers this to s, and GF already has the stronger squared exponent 2/3. Consequently (IV.80) covers all outcomes at all admitted widths, including each fixed admitted GD width. It is not merely an estimate along a selected width sequence.

## 7. Functional analysis: compactness in strong W₂

Checked lines 1043–1196.

The ambient product C × L² × C × L², with the displayed product norm, is a separable Banach space. The two L² coordinates are strong norm coordinates. The proof does not replace either by a weak topology.

For the finite-rank map Q_h, polygonal interpolation contracts the continuous-path supremum norm and cell averaging contracts the L² norm. The within-cell double-integral identity for the averaging error is exact. Enlarging the ordered within-cell pairs to all available pairs at a fixed time separation yields

    average (||v−P_hv||₂² + ||s−P_hs||₂²)
        ≤ (C₁/h) ∫₀ʰ τ^(2/5) dτ = (5C₁/7)h^(2/5).

Absolute continuity gives the position interpolation error at most 4h||v||₂² per row; the same applies to h and s. Therefore the actual coupling that sends each complete neuron tuple to its own projection has expected squared cost bounded by ε(h) in (IV.84). The two samples and four coordinates remain coupled throughout.

The fourth moment M₄ in (IV.85) is valid: the two velocity terms each contribute at most A_kin², the activation supremum contributes at most 4B⁴, and the position term contributes B_path. Projected laws retain this bound. In particular, moving mass outside a radius-R ball to zero has squared transport cost at most M₄/R². This supplies the required quadratic-tail control; bounded second moments alone are not being used as a substitute.

At fixed mesh, the projected range is finite dimensional. After the tail truncation, a finite spatial cover and then a finite cover of the mass simplex give a W₂ finite net. Unmatched mass costs at most that mass times the squared diameter of the finite support. Letting the mesh shrink and the other cover errors shrink proves total boundedness of the entire family, with no discarded fixed-width outcomes.

The subsequential-limit construction is valid without invoking a probability-measure compactness theorem. A fast Cauchy subsequence of finite empirical laws has adjacent finite couplings with summable RMS distances. Normalizing the finite coupling tables and successively subdividing [0,1] constructs a common probability space carrying the required adjacent couplings. The expected sum of the distances is finite, so the random points are almost surely Cauchy in the complete ambient space. The L² tail bound makes the law of their limit a P₂ law and proves W₂ convergence.

The metric triangle inequalities needed when passing from this family to its closure cause no disintegration obstruction. Whenever the intermediate measure is one of these finite empirical measures, each adjacent coupling can be restricted to a finite atom and divided by that atom's mass; the resulting conditional probabilities can be multiplied and summed. The ordinary L² triangle inequality then gives the required coupling cost bound. This is the finite-marginal gluing argument used in the proof.

A sequence in the closure is approximated by family members within 1/j and thus has a convergent subsequence. The open-cover argument at lines 1165–1172 correctly converts this into compactness. The resulting compact set contains the full deterministic family, not a single chosen outcome at each width.

The separately displayed tightness construction also checks out. Q_h is continuous, so its simultaneous approximation constraints define a closed set. A norm bound and approximation by bounded finite-dimensional images make that set totally bounded, hence compact. Markov's inequality uses the actual projection-cost bound established above; its error sum is at most a/2, alongside the norm-tail error a/2.

At T = 0, the L² spaces are zero spaces and the remaining coordinates are finite dimensional. The initial fourth moment gives the needed compact containment, and all integrated kinetic and kernel conclusions are zero-time identities. This case requires no positive-time mesh argument.

## 8. Gaussian events, measurability, and probability quantifiers

Checked lines 166–195 and 1198–1307.

The stated Gaussian initialization gives independent first-neuron pairs with covariance G. It keeps the finite stored readout variance n⁻²; the readout has not been replaced by its limiting value zero.

The Gaussian moments used for the first-layer event are correct:

    E|z_i(0)|⁴ = 8 + 4ρ² ≤ 12,
    E|z_i(0)|⁸ ≤ 8(E|z_{1,i}|⁸ + E|z_{2,i}|⁸) = 1680.

Independence across rows then gives the stated 1680/n Chebyshev bound for an empirical fourth moment exceeding 13, including at ρ = −1.

A maximal 1/4-separated unit-sphere set has at most 9ⁿ points by the radius-1/8 packing argument. Approximating both test vectors costs at most half the operator norm, so an operator norm exceeding 8 implies a net bilinear form exceeding 4. Each fixed form has Gaussian variance 1/n. The union bound is exactly 2exp(−(8−2log 9)n). The readout maximum bound is 2n exp(−n²/2). Adding the three event failures requires no independence between them.

Every outcome of E_n satisfies the deterministic hypotheses for both schemes. Thus a common initialization has joint failure probability at most b_n; separate initializations have joint failure probability at most 2b_n by a union bound. The GD threshold can vary with the fixed horizon, while the definition of E_n is unchanged.

The random empirical laws are measurable in the asserted W₂ topology. At fixed width, GD has finitely many smooth node maps and a fixed interpolation partition. GF depends continuously on its initial data on compact time intervals: the action bound puts solutions from a bounded initial neighborhood in a common finite-dimensional ball, where the smooth vector field has a finite Lipschitz constant. The velocity and activation-velocity coordinates then also vary continuously in their required norms. Pairing the same finite neuron indices proves continuity of the empirical law.

The two tail statements in (IV.91) correctly use, respectively, the tuple fourth moment and the space-time cubic velocity moment on E_n. They establish the displayed probability limits, without estimating tail expectations on E_n^c. The bound is for fixed deterministic inputs, uniformly in their numerical normalization parameters; it does not control every adaptively selected input pair in one realization. No unjustified eventual-almost-sure assertion is made from the nonsummable 1680/n bound.

## 9. Compatibility and actual first-row reconstruction

Checked lines 197–225 and 1309–1396.

All four relations in (IV.15) form a closed subset of the strong ambient space. The integral defect maps are continuous from C × L² into C. Composition by φ is continuous in the supremum norm. The bound in (IV.92) correctly proves continuity of (z,v) ↦ φ′(z) ⊙ v into L². A coupling whose expected distance tends to zero transfers support on this closed set to the limit, using the truncated distance function. The endpoint E_- constraints are closed as well.

For D as defined, D is symmetric positive semidefinite and DGD = D in both the interior and antiparallel cases. Hence

    A_rowᵀ A_row = D,
    dot W¹_i = A_row v_i,
    |dot W¹_i|² = v_iᵀ D v_i.

Integrating the actual row equation gives the increment formula. The map taking a tuple to its raw increment and velocity is Lipschitz, with squared constant at most 4||A_row||². Pushing near-optimal couplings through it proves W₂ convergence, also jointly with the original tuple. No alignment of original neuron identities between different widths is required.

The orthogonal projection P = XDXᵀ/d is correct for both ranks of G. Its complement of the initial row remains constant because the actual row update is in the input span. Thus the two sample evaluations reconstruct increments and velocities, but do not assert full-row convergence without the missing initial orthogonal coordinates. At ρ = −1, e = (b,−b) gives row energy 4b² = |v|²/2, with no duplicated energy contribution.

## 10. Strong kinetic and full residual-weighted kernel conclusions

Checked lines 226–269 and 1398–1551.

The treatment of the L² coordinates as equivalence classes is sound. Cell averages are measurable functions of a path and time, converge to each L² path in L², and converge in L²(μ × dt) by the integrable majorant 4||V||₂². A subsequence with summable increments supplies a jointly measurable representative with the correct path sections almost surely. This makes the timewise expectations meaningful almost everywhere, without claiming continuous point evaluation on L². The same applies to S.

For couplings with squared tuple cost at most ε_n², let M_n² = E||v_n||₂² and M² = E||V||₂². Then |M_n−M| ≤ ε_n, and Cauchy–Schwarz yields

    ||E|v_n|² − E|V|²||_{L¹} ≤ ε_n(M_n+M).

The identical estimate handles the activation speed. The quadratic form vᵀDv adds the factor ||D|| and gives the raw first-row speed conclusion. These are genuine L¹ convergences of time densities, and therefore imply convergence of their integrals over every fixed measurable time subset. They do not merely compare total actions.

The node convention in GD is essential and is correctly maintained. Controls are common to all neurons for a sample, so the finite residual-weighted kernel is exactly

    j_{n,ab} = G_ab average_i (Dv_i)_a(Dv_i)_b.

This reconstructs the entire controlled matrix from the actual interpolated preactivation velocity. It never divides by a control or assumes convergence of the controls or unweighted reverse fields separately.

For H(v) = G ⊙ [(Dv)(Dv)ᵀ], entrywise multiplication by G contracts the Frobenius norm. The outer-product difference identity gives

    ||H(v)−H(w)||_{L¹(F)}
        ≤ ||D||² ||v−w||₂ (||v||₂+||w||₂).

Taking expectations in the coupling proves the displayed full-matrix L¹ convergence bound in (IV.105), including both off-diagonal entries. The population matrix is an integrable expectation, independent of choices of representatives as an L¹ class.

Summing all four entries gives

    Σ_ab H(v)_ab = (Dv)ᵀG(Dv) = vᵀDv,

which is the raw speed identity, not a trace identity. At the antiparallel endpoint the contribution is b² times the all-ones matrix, whose entry sum is exactly 4b². Positivity also follows from the displayed diagonal congruence with G.

The GD loss derivative in (IV.106) correctly pairs the recomputed gradient with the held update gradient and is not identified with minus the held raw speed squared. The claimed kernel convergence is for node fields; no unproved comparison to the recomputed interior-cell kernel is used.

Finally, the pushforward and expectation maps just checked are continuous on P₂ in W₂. Their joint image of the deterministic compact set is compact in the two measure spaces and four stated L¹ spaces. The same good event therefore gives compact containment of these joint observables with the same failure bound.

## Quantifier and scope conclusion

The proof supports one compact set for all admissible deterministic outcomes, every GF width, and every GD width above the specified threshold. Moment and stability estimates are independent of d, n, and ρ. Strong compactness and reconstruction may depend on the fixed correlation through D; the antiparallel endpoint is handled by exact identities. The dimension, inputs, and correlation are fixed when taking the asserted subsequences.

Either scheme, or an interleaving of schemes, admits convergent subsequences of good deterministic outcomes. Every such W₂-convergent subsequence has the stated structural, kinetic, and controlled-kernel conclusions for its own limit. The original random laws have compact containment in probability. No step promotes this to convergence in probability to an identified law, equality of scheme limits, a global population theorem, an almost-sure assertion over all widths, or an expectation estimate on bad events.

Required corrections: **none**.
