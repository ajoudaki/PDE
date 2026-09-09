# Independent isolated modular audit: local exact GD/GF and observables

## Verdict and boundary

**MODULAR PASS for the stated local exact raw GD/GF/observables bridge.**

No required mathematical correction was found in the candidate or in the dependency implications used to obtain this local result. In particular, the additional truncation before the reused third-layer matrix is sufficient. The subsequent mesh and uniform-integrability argument is compressed, but it can be completed directly from the bounded first-layer cut velocity and the stated comparison estimates; it does not require a new probabilistic theorem or a whole-space higher-moment matrix bound. That completion is given below rather than assumed.

This verdict concerns the interval `0 <= t <= T_* = S_*/4`, with `0 < S_* <= 1/196`, the prescribed initialization and step size, the stated admissible fixed probe programs, and the stated quadratic/Wasserstein-2 observations. It is **not** a final single-document global PASS. It establishes neither continuation beyond this interval nor an all-finite-time theorem, nontriviality/nonlazy learning, or higher-order moment convergence for the actual uncut dynamics.

Required fixes: **none**. Optional clarifications appear at the end.

## Inputs, hashes, and isolation

All five mathematical inputs were read completely, including the proofs in the four dependencies. The candidate hash matches the requested SHA-256. Its four dependency hashes match the actual files and its own manifest.

All paths below are relative to `/tmp/l3-two-sample-proof-DLuelg/`.

| Input | Lines read | SHA-256 |
| --- | ---: | --- |
| `SOFTPLUS_LOCAL_EXACT_GD_OBSERVABLES.md` | 1–382 | `a830c8bfc6d6a398c693fef8669303341a0dc40e12cd498e75e7995f752a8071` |
| `SOFTPLUS_LOCAL_POPULATION_ASSEMBLY.md` | 1–441 | `398d12f41a60276cbee91323293c2f64b97055eac935f45ee31b8cac6946c97d` |
| `SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md` | 1–862 | `875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603` |
| `SOFTPLUS_THREE_CUT_PRIMAL_COMPARISON.md` | 1–1050 | `51323710f5c02314f232b3fa8e42a7dc9c0c385530398c009fa28a595bf3f02f` |
| `SOFTPLUS_LOCAL_GAUSSIAN_RESPONSE.md` | 1–473 | `0cf9f84eb9ff99d1831355b56e24034660fe5c0c98722d78b3a8e33c586a5b6b` |

The only additional instruction file read was `/etc/codex/skills/solve-math-rigorously/SKILL.md`, used solely for procedural proof-audit guidance. No project history, other mathematical files, other reviews, external mathematical sources, or conversation-recovery tools were inspected. References to other documents or previous reviews inside the permitted inputs were not followed and supplied no evidence for this verdict. No experiments or subagents were used. The five inputs were not edited. This report was written with `apply_patch`.

For concise references below, **Candidate**, **Assembly**, **Identification**, **Comparison**, and **Response** designate the five files in table order. Line references refer to the hashed versions above.

## 1. Dependency audit and interface matching

### 1.1 Fixed finite programs

Identification proves a fixed-program result, not a theorem uniform in the number of training steps. Its use here respects that distinction.

The essential points checked were:

- The capped maps `(z,v) -> phi'(z) tau_R(v)` have bounded first derivatives at fixed cap, while `phi` has linear growth and is globally Lipschitz. The readout update remains uncut. See Identification 232–252.
- The finite-program moment proof applies to the actual empirical-feedback graph. The derivative bounds in (19) have the correct normalizations: differentiating an initial matrix contributes `n^(-1/2)`, and differentiating a normalized contraction contributes `n^(-1/2)` before multiplication by a vector of Euclidean size `O(sqrt(n))`. These factors cancel as required. The Gaussian rotation estimate and permutation invariance then provide all fixed coordinate moments. This is a program-specific estimate, not an arbitrary-query `L^p` operator estimate. See 254–386.
- The conditional Gaussian mean includes both earlier forward and transpose constraints. Its projected residual retains the original matrix reuse. The rank-bounded discarded projection has vanishing empirical moments by (23), without a coordinate leverage assumption. See 388–505.
- The source/response calculation retains the response to all available opposite-direction calls and uses uncentered input second moments. It does not replace a trained transpose with independent noise. See 507–576.
- Singular query Grams are treated by an actual positive-noise comparison and removal argument, supported by the finite-width moment bounds. The scalar recursion is passed through covariance square roots and continuous bounded formal first derivatives, not through inverse Gram continuity. Formal zero-variance slots are retained. See 578–702 and 776–850.
- The oracle-feedback comparison is causal and transfers back to the actual contractions using RMS stability and higher moments. See 704–774.

These facts support fixed-mesh joint laws and polynomial-growth tests for the capped training graph and smooth admissible additional queries. The Candidate needs only W2 for its final uncut observations. An additional globally Lipschitz coordinate instruction can also be treated by smooth approximation if its stated regularity is read more broadly than the smooth class in Identification: at a fixed finite graph, approximate on a compact input set, control the linear-growth tail in L2, and propagate through bounded matrix actions. No formal derivative observable for such an extra instruction is claimed.

**Dependency issue found:** none affecting this interface. In particular, a growing `n^2`-step program is not smuggled into Identification.

### 1.2 Primal bounds and asymmetric comparison

Comparison uses ordinary Frobenius norms for the two raw hidden matrices and normalized vector norms for neuron fields. Its identity

`||u v^T/n||_F = ||u||_n ||v||_n`

is exactly the normalization needed for the raw updates. The first-layer coordinates are the canonical input-span coordinates, including the singular endpoint. See Comparison 21–95.

The primal induction has a strict margin and uses the uncut readout update, contracting cuts, and exact Euler increments. In particular, the forward increment identity uses the next matrix and includes the matrix-feature cross term. The constants in the displayed short-time bounds and the two lower-layer time metrics are consistent. See 321–573.

The key comparison split is

`tau_new(v_new) gate_new - tau_old(v_old) gate_old`

`= [tau_new(v_new)-tau_old(v_old)] gate_new`

`  + tau_old(v_old) [gate_new-gate_old]`.

Only the second term needs an output ceiling, and it is the OLD ceiling. The previous-layer error is multiplied by a bounded gate/operator coefficient, not by another cap. Consequently the coefficient is `C_ball(1+R)`, not `C_ball R^2`, and the forcing defects concern the actual old readout and old queries. The new cuts may be identity maps. See 714–890.

The Assembly's cuts have identity radius `R` and output ceiling `2R`; the Candidate correctly absorbs this factor two into `C(1+R)`. The nested-family inequality is explicitly proved in Assembly 189–209, so replacing old/new cut mismatch by old truncation defects is justified.

The comparison proof also supplies the individual backward-query/delta inequalities required by the Candidate, not just the sum of raw velocity errors. The extension to a larger fixed primal ball is explicit. State-dependent physical coefficients are handled by the same samplewise split with a bounded coefficient magnitude; the numerical `|b| <= 1` convention of Comparison's final subsection does not restrict the Candidate to coefficients of magnitude one.

**Dependency issue found:** none affecting this interface.

### 1.3 Local response tails

Response is conditional on its stipulated finite scalar law and primal/time-metric hypotheses. Assembly 253–274 discharges those hypotheses from Identification and Comparison, at fixed mesh before the width limit. This is not a circular use of the eventual uncut path.

The Gaussian maximum argument uses the covariance increment metric and a dyadic union bound, without time independence. The averaged reverse-source estimate uses Jensen, not a reverse-query supremum estimate. The causal response bootstrap bounds current `A2`, then `A3`, then `B3`, then `B2`; it retains both terms in the derivative of the capped top delta, including the readout derivative. The constants defining `S_0` are selected from envelopes based on the prior bootstrap threshold, not from the current response bound being proved. See Response 127–431.

The resulting query/readout square-exponential moments imply the old L2 defects at rate `C exp(-cR^2)`. No supremum-in-time reverse-query random-variable bound is needed or claimed. Passing each time to the exact fixed-cap flow uses L2 convergence and Fatou, after which the deterministic defect norm is uniform in time. See Response 433–458 and Assembly 276–291.

**Dependency issue found:** none affecting this interface.

### 1.4 Common population spaces, cap removal, and clock

Assembly constructs the base actions on a countable generated collection and extends them by their inherited L2 operator bounds. Exact finite transpose pairings identify true adjoints on the dense collection and hence on its closure. This avoids an undefined Gaussian operator on an arbitrarily specified whole L2 space. Different neuron populations remain separate. See Assembly 114–185.

At fixed cap, the raw Hilbert-space flow is locally Lipschitz and continues across the short interval using the primal margin. Cut removal combines the linear-in-old-cap comparison with Gaussian old defects. The same comparison makes the raw velocities uniformly Cauchy. The bounded-gate/L2 product argument identifies the limit with the uncut formulas and proves the needed curvewise chain rule. The uniqueness argument compares a competing bounded continuous state path to the old capped reference and does not impose new-path Gaussian tails. See 187–357 and 386–416.

Sample symmetry is established from the zero-readout finite reference law and deterministic limits, including label reversal and `rho=-1`. It is not imposed on an individual finite realization. The energy identity gives `g' >= 0`; the primal bound gives `|g(s)| <= 49s`, so `S_* <= 1/196` yields `0 <= g <= 1/4`. Thus `s'=4(1-g)` lies between 3 and 4 and is Lipschitz on the local interval. See Assembly 359–441.

The rates imported as Candidate (2)–(3) follow from Assembly's state comparison, the full vector-field comparison, and the backward-field inequalities; multiplying `exp(-cR^2)` by a fixed linear polynomial in `R` or by `exp(CR S_*)` preserves a Gaussian-decay bound after weakening its constants.

**Dependency issue found:** none affecting this interface. The Assembly's statements about other curvature/action documents are not needed for this local bridge and were not treated as imported results.

## 2. Fixed-cap finite-width convergence, uniform time, and velocity programs

### 2.1 States, queries, and defects

At fixed `R`, the capped raw vector field is Lipschitz in the stated norm on the common enlarged primal ball, uniformly in width. The forward and capped backward maps have the same type of bound. The raw velocity is bounded there. Therefore a fixed feature mesh has raw Euler error `O_R(h)`, uniformly in width on the high-probability initial primal event. The strict primal margin removes stopping for sufficiently small `h`.

At a fixed mesh, Identification applies to the finite graph, including joint observations at any fixed finite set of mesh/interpolation times. Matrix increments are finite rank sums, so a trained matrix query is its initial query plus normalized contraction terms. The population Euler graph is on the Assembly's common spaces. The uniform raw Euler comparison therefore lets the mesh go to zero after width, and identifies the finite-reference current field laws in W2.

The exact fixed-cap raw path, forward fields, and backward queries have width-uniform RMS time moduli. A finite time grid upgrades pointwise W2 convergence to uniform-time W2 convergence. This is a grid argument with a fixed number of points at each stage, not a uniform-in-program-length identification theorem.

For `D_R(u)=u-tau_R(u)`, the chosen cuts satisfy `0 <= D_R' <= 1`. Hence the L2 defect norm is Lipschitz in the query. Finite-grid convergence, the fixed-cap query modulus, and the population defect estimate give Candidate (5). Predictions are Lipschitz on a fixed primal ball; the same argument gives (6).

### 2.2 The additional product before matrix 3

Candidate 289–313 correctly identifies a genuine obstruction and resolves it. The map `(z,v) -> phi'(z)v` is not globally Lipschitz in both variables because its derivative in `z` contains `v`. It cannot simply be added as an admissible instruction before another matrix query.

For the fixed-cap reference, the first-layer velocity is a finite sum of capped deltas. After bounding its scalar coefficients using the primal bounds and the bounded clock, it has a coordinatewise bound `C_R`. Thus the first product `phi'(z1) dot z1` is representable by a bounded-derivative map using a smooth cap beyond that bound. The resulting second-layer velocity is an admissible finite-program output, with all fixed empirical moments at fixed mesh.

Before matrix 3, replace `dot z2` by a smooth contracting cap `chi_A(dot z2)` which is identity on `[-A,A]`. Then

`||W3[phi'(z2)(dot z2-chi_A(dot z2))]||_n`

`<= ||W3||_op / 10 * ||dot z2-chi_A(dot z2)||_n`.

The latter norm tends to zero by the squared-tail control of the already identified second-layer velocity. For fixed `A`, the entire new query is admissible, even though `W3` has been used previously in either orientation. Its conditional response is supplied by Identification. Sending width to infinity at fixed mesh/cap/truncation, then `A` to infinity, identifies the true third-layer velocity in W2.

Approximation in L2 by the capped outputs also supplies squared-tail control of the final uncapped output. There is no claim that the last matrix output has all higher moments, and none is required for the final theorem. The final feature velocity is multiplication by a bounded gate and uses the same product-continuity argument.

### 2.3 Why mesh refinement does not require a missing uniform higher moment

The passage at Candidate 315–324 deserves explicit verification: fixed-mesh moments alone would not justify multiplying two varying families while sending the mesh to zero. Here the needed control follows from the first-layer bound and the raw fixed-cap estimates.

Write `U_n` for the exact fixed-cap reference, `V_n` for its raw velocity, and `u_{ell,n}` for its recomputed preactivation velocity. Work on the common primal event. At fixed cap,

`||u_{1,n}(t)||_infinity <= C_R`,

`||u_{1,n}(t)-u_{1,n}(v)||_n <= C_R |t-v|`.

The first statement uses capped deltas; the second uses raw velocity Lipschitz continuity. Therefore

`||phi'(z1(t))u1(t)-phi'(z1(v))u1(v)||_n`

`<= (1/10)||u1(t)-u1(v)||_n`

`   + (1/40)||u1(v)||_infinity ||z1(t)-z1(v)||_n`

`<= C_R |t-v|`.

Apply this estimate to

`u2 = V2 h1 + W2[phi'(z1)u1]`.

Both `W2` and `V2` have width-uniform operator/Frobenius bounds and time moduli at fixed cap, and `h1` has a width-uniform RMS modulus. Consequently

`||u2(t)-u2(v)||_n <= C_R |t-v|`.

The same calculation comparing the exact reference with its raw Euler approximation gives a uniform `O_R(h)` RMS error for `u2`, because the first-layer velocities of both paths are coordinatewise bounded. No tail estimate for `u2` has been assumed in obtaining this conclusion.

At each fixed time, `u2` therefore has W2 convergence to the exact population-reference velocity by the already valid fixed-mesh identification. Combining this convergence with its uniform time modulus gives uniform squared-tail control by a finite time grid. The coarse Euler `u2` fields inherit that control as `h` decreases, since their RMS distance from the exact reference is `O_R(h)`.

Only now is the product bridge applied to `phi'(z2)u2`. Its input tails are already controlled uniformly over the needed times and meshes. Bounded matrix 3, the Frobenius comparison of matrix 3, and the rank-term estimates then give the third-layer velocity comparison. The last feature velocity follows in the same way. This also yields the reference velocity time modulus, which need only tend to zero and need not be Lipschitz at layer 3.

Thus the Candidate's layer-by-layer argument can be executed without circularly presupposing uniform tails for the very velocity being identified. The derivation above spells out the crucial intermediate bound implicit in that paragraph.

## 3. Actual physical coefficients, Euler error, and stopping

### 3.1 No false finite-width label symmetry

For `B_(n,R)(t)=Theta_(n,R)(s(t))`, the reference coefficient in each raw sample contribution is

`beta_a(t)=s'(t)y_a/2=2y_a(1-g(s(t)))`.

For the actual physical dynamics it is `alpha_a=-2(f_(n,a)-y_a)`. Their exact difference is

`alpha_a-beta_a=-2(f_(n,a)-y_a g(s(t)))`.

Splitting `f_(n,a)-y_a g` into actual-minus-reference prediction and reference-minus-population prediction produces precisely Candidate (7). On a fixed primal ball, `alpha_a` is bounded, each prediction difference is Lipschitz in raw distance, and each reference sample update has bounded raw norm. The samplewise old-cut comparison therefore gives (7) with constants depending only on the ball and the linear old cap factor.

This controls the component along the label vector and its orthogonal component. Nothing requires the finite prediction vector to lie in the label direction. In particular, the finite off-label mode is not silently set to zero.

### 3.2 Nonzero readout initialization

The actual initial readout and the zero-readout reference are different. With the stipulated variance `n^(-2)`,

`E ||W4_0||_n^2 = n^(-2)`,

so the initial raw discrepancy is `O_P(n^(-1))`. The hidden initial parameters are coupled identically, including the frozen first-layer perpendicular block. Candidate (8) retains this discrepancy. It is not necessary to prove small pointwise initial readout values or to alter the canonical initialization.

### 3.3 Exact raw Euler and local defect

Equation (1) is the actual raw Euler step for the specified raw metric. There is no feature-coordinate discretization being substituted for it.

The comparison path has derivative `s' F_R(B)`. At fixed cap, `F_R` is Lipschitz on the enlarged ball, `B` has bounded velocity, and `s'` is Lipschitz because `g'` is continuous and bounded. Hence

`||B(t+eta)-B(t)-eta B'(t)||_raw <= C_R eta^2`.

Summing this local defect over the physical mesh gives `O(C_R eta)`. Applying the old-cut discrepancy bound at the actual left nodes gives the recursion underlying (8):

`D_(k+1) <= (1+C(1+R)eta)D_k`

`          + C eta [old defects + reference prediction error]`

`          + C_R eta^2`.

The resulting bound is valid with `eta_n=n^(-2)`. At fixed `R`, the width remainders and initialization/mesh terms vanish. Subsequently,

`(1+R)^j exp(C(1+R)T_* - cR^2) -> 0`

for each fixed `j`, including the additional linear factor used when passing from state errors back to velocity/backward-field errors. No comparison with an exponentially growing `R(n)` is needed.

### 3.4 Removing the stopping assumption

The proof does not assume that the actual uncut path already lies in the reference primal ball. Before first exit from a fixed larger ball, linear activation growth, bounded gates, bounded hidden operators, and bounded readout RMS control all forward/backward RMS fields, residuals, and raw velocities independently of width and cap.

A GD step then has raw length `O(eta_n)`. Forward field norms and operator norms are controlled by raw distance, so its first exit node lies in a slightly enlarged fixed ball. The recursion uses the preceding in-ball node and holds through that exit node. Fixing a sufficiently large `R` makes the surviving deterministic error smaller than the reference margin; then sufficiently large width makes the remaining error small with probability tending to one. This contradicts an exit. The continuous version gives the GF conclusion.

If `T_*` is not a mesh node, the final partial raw segment uses the bounded velocity at the last preceding node and has length at most `C eta_n`; the comparison does not require extending the population path past `T_*`.

The separate finite-dimensional GF existence argument also has the correct energy metric: `dL/dt=-||grad_raw L||_raw^2`. Its integrated path-length bound `sqrt(T L(0))` prevents finite-time escape in the finite-dimensional raw coordinates. This energy argument is not used for the cut references or for an unproved discrete-GD energy identity.

## 4. Recomputed interpolation and raw kernel factors

### 4.1 Hidden velocities between GD nodes

The formulas in Candidate (9) are the derivatives of the recomputed forward network along the interpolated raw parameters. They are not derivatives of a separately interpolated hidden-field array.

Within a raw GD step, all raw state changes are `O(eta_n)`, so all preactivation changes have RMS `O(eta_n)`. The deterministic finite-vector inequality

`||v||_infinity <= sqrt(n)||v||_n`

then bounds each gate change by `O(eta_n sqrt(n))`. The first-layer raw velocity is constant on the step. Applying the product formula successively at layers 2 and 3, with bounded operator norms and RMS fields, gives hidden velocity variation `O(eta_n sqrt(n))`. No coordinatewise bound on the uncut actual features is used.

For `eta_n=n^(-2)`, this is `O(n^(-3/2))`, as claimed. The limiting velocity is continuous in L2, so the terminal-left and interior-right conventions have the same limit. This verifies the interpolation claim for velocities as well as for states.

### 4.2 Gradient and kernel normalization

Let `J_a^(ell)` denote the ordinary Euclidean parameter derivative of `f_a`. Direct differentiation gives

| Raw block | Euclidean derivative of `f_a` | Raw metric weight |
| --- | --- | --- |
| `W1` | `delta1_a x_a^T/n` | `d/n` times Frobenius inner product on the input span |
| `W2` | `delta2_a h1_a^T/n` | ordinary Frobenius inner product |
| `W3` | `delta3_a h2_a^T/n` | ordinary Frobenius inner product |
| `W4` | `h3_a/n` | `1/n` times Euclidean inner product |

The inverse metric factors therefore produce exactly the four updates in Candidate (1). Pairing these prediction gradients in the inverse metric gives

`K1_ab = (x_a^T x_b/d) <delta1_a,delta1_b>_n`,

`K2_ab = <delta2_a,delta2_b>_n <h1_a,h1_b>_n`,

`K3_ab = <delta3_a,delta3_b>_n <h2_a,h2_b>_n`,

`K4_ab = <h3_a,h3_b>_n`.

There is no missing `n`, `d`, factor two, residual, or sample-average factor. The factor two belongs to differentiation of `L=r1^2+r2^2`, yielding

`dot f_a = -2 sum_b (K1_ab+K2_ab+K3_ab+K4_ab) r_b`.

At `rho=-1`, the first-field pair is realizable as `(v,-v)` and the reduced norm gives the same first-block expression. No inverse of a singular Gram matrix is needed. For `|rho|<1`, the identity with the `C^(-1)` metric is exactly the minimum input-span raw norm identity.

Every kernel pairing is within its own neuron population. Products of two such scalar pairings need no independence between populations. Convergence follows from the named field comparisons and their W2 laws. The population chain rule is the Assembly's curvewise L2 chain rule, not a claim of Frechet differentiability of the activation map on the entire L2 space.

For GD, the exact instantaneous kernel identity need not hold with the current residual inside a step because its raw velocity is frozen at the left node. The Candidate asserts the population chain rule; the proved interpolation and velocity convergence justify that limit without asserting an incorrect within-step finite-GD identity.

## 5. Observations, tails, limit order, and path laws

### 5.1 Products and admissible probes

The bounded-gate product lemma is valid in both empirical and population L2. One first splits

`B X-D Y = B(X-Y)+(B-D)Y`.

The first term is controlled by the bounded multiplier. For the second, restrict to `|Y| <= A`, where bounded convergence in empirical probability controls its L2 norm, then use the squared tail of `Y` on the complement. This proves the needed assertion without independence of coordinates or matrix inputs.

An ordinary probe matrix application transfers using

`||W_new p_new-W_old p_old||_2`

`<= ||W_new||_op ||p_new-p_old||_2`

`   + ||W_new-W_old||_HS ||p_old||_2`.

The transpose version is identical. Globally Lipschitz coordinate maps and normalized quadratic contractions then transfer by finite induction and Cauchy–Schwarz. The uncut backward instructions are handled separately by the asymmetric comparison; they are not reclassified as globally Lipschitz instructions.

### 5.2 Uniform integrability is used in the correct sense

For empirical fields the necessary tail statement is, at a fixed reference cap and for every `epsilon > 0`,

`lim_(A->infinity) limsup_(n->infinity)`

`P{sup_t <|Y_n(t)|^2 1_(|Y_n(t)|>A)>_n > epsilon} = 0`.

Fixed-grid W2 convergence and the RMS time modulus give this statement. A useful deterministic inequality, obtained by separating `|X| > A/2` from its complement, is

`<|Y|^2 1_(|Y|>A)>`

`<= 4||Y-X||_2^2 + 2<|X|^2 1_(|X|>A/2)>`.

It makes explicit why arbitrarily accurate L2 approximation by finitely many tail-controlled fields yields uniform tail control. A single approximation with fixed positive error would not suffice; the finite grids and mesh comparisons here allow that error to tend to zero.

Cap removal also needs attention: finiteness of a separate tail bound for each `R` alone would not control products against errors that only vanish as `R` increases. Here the population raw states and velocities converge uniformly by Candidate (2). Along the compact limiting L2 velocity curve, the bounded-gate product argument gives uniform convergence of the recomputed population hidden velocities as `R -> infinity`. Hence their squared tails are uniformly controlled for large `R`. The fixed-cap finite-width W2 convergence transfers that control in the iterated width/cap order. This supplies the tail input when transferring the actual-node hidden velocities from the references.

The Candidate does not need, and does not prove, all-order moment bounds uniform over a vanishing mesh, the actual uncut training graph, or the number of GD steps. W2 and the above squared-tail statements suffice.

### 5.3 Limit order

The valid order is:

1. Fix a reference cap, a finite coarse feature mesh, a finite observation/probe graph, and any additional product cutoff `A`.
2. Take width to infinity for that fixed graph.
3. Remove `A` at that fixed mesh using the second-layer velocity tails and bounded matrix action.
4. Remove the coarse feature mesh, using the width-uniform raw comparison and the layer-by-layer argument in Section 2.3 above.
5. Remove the reference cap using Gaussian old defects against the linear-in-cap Gronwall exponent, with the reference velocity tails as described above.

Time grids used to establish uniform-time convergence and path interpolation are also fixed before their associated width limit, then refined after the corresponding estimates are established. These nested approximations give convergence along the full width sequence in probability. They do not select a favorable width subsequence or use Identification on a graph with `n`-dependent length.

### 5.4 Quadratic tests and integrated speeds

Joint finite-time W2 convergence follows by retaining all requested time slots in the fixed reference graph and using the same-neuron coupling for comparisons. It is stronger than independent one-time marginal identification.

Uniform RMS comparisons and reference squared-tail control transfer every fixed continuous test of at most quadratic growth by truncation and uniform continuity on compact sets. Norm squares transfer using

`| ||u||_2^2-||v||_2^2 | <= ||u-v||_2 (||u||_2+||v||_2)`.

The primal and velocity bounds are uniform over the local interval, so the same estimate integrated in time proves the stated squared-speed integral convergence. No limit exchange involving an uncontrolled fourth moment is required.

### 5.5 W2 path laws

For an absolutely continuous coordinate path and its nodal linear interpolant, Candidate 363–367 gives the valid bound

`||z-I_pi z||_sup^2 <= 4 |pi| integral_0^T |dot z(t)|^2 dt`.

Averaging over neurons bounds the squared W2 cost of coupling each path with its own interpolation. The population version is obtained by integration over the relevant neuron space. The raw velocity/primal bounds and (9) uniformly bound the resulting averaged energies.

On a fixed time mesh, the joint tuple law already converges in W2. Linear interpolation is Lipschitz from that finite-dimensional tuple space into the path supremum norm. Thus the triangle inequality gives the path-law convergence after the observation mesh tends to zero. The argument applies to the two samples together, and to features by their bounded gate or global Lipschitz activation.

The relevant pair-valued space is `C([0,T_*]; R^2)` for each neuron population, or a finite tuple of compatible same-population paths. No empirical pairing of neuron indices across distinct populations is implied. The proof does not establish path laws for the time derivatives or for reverse-query derivatives, which the Candidate expressly excludes.

## 6. Joint GD/GF limit and remaining scope

Both actual dynamics use the identical finite initialization and are compared to the same finite reference `B_(n,R)`. Their raw same-width distance is therefore at most the sum of the two comparison distances. The nested limits make that distance vanish uniformly in physical time in probability. Applying the observation comparisons on the same initialization event gives their joint deterministic population limit along the full width sequence.

The allowed restart statement is uniqueness on the remaining part of the already constructed local interval, on the same population spaces with the same initial operators. It supplies no existence past the local endpoint. The small physical interval is sufficient for this Candidate, so the absence of a global continuation estimate is not a defect of its stated theorem.

## 7. Required versus optional changes

### Required

None for the stated local modular result. No blocking dependency issue was identified in the permitted inputs.

### Optional clarifications

1. **Expand Candidate 315–324 with the intermediate second-layer velocity estimate.** State the fixed-cap coordinatewise bound on `dot z1`, derive the width-uniform RMS time modulus and `O_R(h)` mesh comparison for `dot z2`, and then invoke the product bridge at layer 3. This makes it immediately visible that mesh-dependent fixed-program moments are not being used as a uniform-mesh moment theorem. Section 2.3 of this report supplies the derivation.
2. **Write one empirical tail quantifier and the cap-removal tail transfer explicitly.** Candidate 257–269 and 315–324 are most naturally read in the high-probability, iterated-limit sense recorded in Section 5.2. Stating it would prevent an unintended interpretation as a uniform bound on expectations over all widths or as a bound on the coordinatewise time supremum of a reverse query.
3. **Specify the probe and path-law types in the theorem statement.** Clarify that fixed probe graphs start from the identified/generated fields on their appropriate neuron populations, and spell out the pair-valued path space. If nonsmooth globally Lipschitz extra maps are intended, mention the elementary smooth-approximation extension; no derivative observations of those maps should be inferred.

These are presentation improvements, not additional assumptions needed to close the audited local implication. The procedural rigorous-math guidance was used to check the normalizations, quantifiers, and product/limit steps explicitly; no conclusion was accepted because of a status label or a report mentioned inside an input.

**Final audit disposition:** local modular PASS, with no required fixes and the optional clarifications above. This report does not confer a single-document or global theorem PASS.
