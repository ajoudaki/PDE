# Isolated modular review of the local softplus population assembly

Review date: 2026-09-06.

**Verdict: PASS for the stated local, zero-initial-readout modular theorem. No required mathematical correction found in the four supplied versions.** The common-space construction, discharge of the response premises, fixed-cap evolution, removal of cuts, uncut identification, unrestricted same-space local uniqueness, restricted restart, energy identity, symmetry, and local physical clock are supported by these inputs. This verdict is not a final-goal review, a global theorem, or a certification of any unprovided curvature-action result.

The review read all four mathematical inputs in full: 2,826 lines total. No other project file, history, prior review, experiment, or agent material was used. References in the inputs to earlier reviews and other documents were not followed and are not evidence for this verdict. The rigorous-math skill supplied review procedure, not an additional mathematical premise. No experiments were performed. The inputs were not edited.

## 1. Exact versions and scope

All paths in this report are relative to `/tmp/l3-two-sample-proof-DLuelg/`. Line references identify the following exact versions.

| ID | Input | Lines | SHA-256 |
|---|---|---:|---|
| A | `SOFTPLUS_LOCAL_POPULATION_ASSEMBLY.md` | 441 | `398d12f41a60276cbee91323293c2f64b97055eac935f45ee31b8cac6946c97d` |
| I | `SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md` | 862 | `875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603` |
| P | `SOFTPLUS_THREE_CUT_PRIMAL_COMPARISON.md` | 1050 | `51323710f5c02314f232b3fa8e42a7dc9c0c385530398c009fa28a595bf3f02f` |
| G | `SOFTPLUS_LOCAL_GAUSSIAN_RESPONSE.md` | 473 | `0cf9f84eb9ff99d1831355b56e24034660fe5c0c98722d78b3a8e33c586a5b6b` |

All three dependency hashes recorded at A:12–23 agree with the actual supplied files. A second hash check after reading also agreed.

The audited conclusion fixes rho in [-1,1), fixes either choice of each label, constructs three generated probability spaces and two bounded initial operators, and obtains a local uncut path with W4(0)=0. Uniqueness refers to these same spaces and initial operators, in the stated L2/HS state class. The horizon is a strictly positive deterministic constant uniform in rho and labels; the spaces and operators themselves can depend on rho. The proof does not construct an evolution for arbitrary initial population data.

| Requested check | Assessment |
|---|---|
| Common initial actions and genuine adjoints | Established by finite-joint laws, density, operator bounds, and transpose pairings |
| Actual discharge of primal response hypotheses | Established, including both time-increment hypotheses |
| Fixed-cap ODE and fixed-cap mesh limit | Established on the stated complete affine space |
| Same-space Cauchy estimate and cut removal | Established with a coefficient linear in the old output ceiling |
| Identification of the uncut vector field | Established by uniform L2 convergence and bounded-gate product continuity |
| Uniqueness against arbitrary bounded-primal competitors | Established; no Gaussian-tail assumption on competitors |
| Restart | Established only for the remaining portion of the constructed interval |
| Raw-metric chain rule and energy | Established, with the rank-one input endpoint treated correctly |
| Exchange and label symmetry | Established through deterministic finite-program limits, including rho=-1 |
| Physical clock | Correct for the explicitly claimed per-sample factor -2r_a |
| Missing heavy local result | None identified within this four-file dependency chain |

## 2. Common initial operators: the construction is adequate

### 2.1 The finite-program lemma covers the needed enlarged query class

A:116–137 needs more than convergence of a single trajectory or its current two-sample Gram. I:128–134 expressly permits adjoining finitely many deterministic linear combinations, smooth globally Lipschitz coordinate instructions with bounded first derivatives, both orientations of both initial matrices, and the quadratic contraction feedback of the rank expansions. This covers finite unions of reference programs and the additional bounded smooth cylinder functions used to generate the probability spaces. The capped maps `(z,v) -> phi'(z) tau_R(v)` are within this class; uncapped multiplication of arbitrary L2 fields is not being inserted as a query instruction.

Each member of a finite union can be run with its own evolving state while sharing the same initial arrays. Extra queries do not change previously defined finite-width quantities. Consequently, convergence of their finite joint empirical laws makes their limiting marginals consistent, independently of which larger finite union is used to obtain them. The conclusion needed here is deterministic convergence in probability of empirical laws and moments; neither almost-sure convergence of all finite-width arrays nor iid evolved neurons is needed.

For a countable index set of real coordinates, consistent Borel probability laws on every finite subset have a probability extension to the countable product with its coordinate sigma field. These are exactly the objects at A:129–137. Apply this separately to each population and complete each measure. There is no cross-population empirical pairing in this application. This is an ordinary countable probability-extension step, not an assumption of a time-continuum Gaussian process or a growing-query identification theorem.

### 2.2 Density and bounded extension

Conditional expectations onto the first finitely many generating coordinates approximate every L2 function. For each finite-dimensional marginal, bounded continuous functions approximate bounded Borel functions in L2, by regularity of a finite Borel measure on Euclidean space. The indicated countable smooth family can be chosen with controlled bounds and compact support, giving the cylinder-function density used at A:139–150. A small presentational improvement concerning these bounds is recorded below; a stronger probabilistic result is not needed.

For a rational linear combination U of generated inputs, its initial-matrix output is also included in the query collection. I supplies convergence of the two squared norms. On an event of probability tending to one, the corresponding finite matrix obeys

    ||W0 U_n||_n <= 10 ||U_n||_n.

If the limiting deterministic second moments violated the squared version of this inequality, convergence in probability would contradict that event. Thus

    ||W0 U||_2 <= 10 ||U||_2.

The same reasoning applied to finite linear identities establishes linearity in L2. In particular, an L2-zero input, including a difference between two descriptions of the same input, has L2-zero output. The action is therefore well defined on equivalence classes. It extends uniquely from the dense rational span to a bounded real-linear map on the whole source L2 space. Countably many generating identities can be enforced simultaneously; the final extension is an identity of Hilbert-space elements.

The reverse action is constructed from the same finite query system. The exact finite pairing

    <V_n,W0 U_n>_n = <W0^T V_n,U_n>_n

passes to the limit using joint mixed second moments in the two respective populations. It yields

    <V,W0 U> = <W0* V,U>.

Density and boundedness extend this identity to all arguments. Thus the reverse operator really is the adjoint, and is not an independently resampled Gaussian map. No initial HS norm is asserted. Only the trained increments need be HS.

This constructs a representation of all generated initial actions. It is not operator-norm convergence of finite matrices embedded in an unspecified ambient Hilbert space; the assembly does not use such a statement.

### 2.3 Real parameters and raw first-field geometry

Approximation of real scalar coefficients and fixed real step sizes by rationals is valid for each finite program: coordinate maps are Lipschitz, operators are bounded, and scalar contractions are continuous on bounded L2 sets. For the particular cap family, real radii also fit this closure through `tau_R(x)=R tau_1(x/R)`; alternatively, integer radii alone suffice for the cut-removal sequence. Thus the countable generating construction does not obstruct the subsequent continuum of times or cap limit.

For |rho|<1, let E have columns e_1,e_2, with E^T E=C. The minimum-norm input-span increment producing v is E C^(-1)v, whose squared norm is v^T C^(-1)v. Equivalently this is the raw first-coordinate norm in P:82–95. At rho=-1, e_2=-e_1, and realizable pairs are (v,-v); their minimum squared norm is v^2. This verifies A:38–60 and its compatibility with P's first-coordinate estimates.

In particular, if b_a=y_a d_a/2, then

    ||Cb||_first = ||sum_a b_a e_a||_L2
                  <= (||d_1||_2+||d_2||_2)/2.

The corresponding formula holds in the reduced rank-one representation. These estimates avoid constants diverging as rho approaches an endpoint. The initial first-field squared raw norm is 2 for |rho|<1 and 1 in the reduced rho=-1 representation, so initial raw norm control is also uniform.

## 3. Identification dependency: the substantial imported result is actually addressed

I is the main probabilistic input. Its relevant proof is not merely a citation to a tensor-program theorem, a claim about current Grams, or an appeal to a second-moment localization argument.

1. **Finite-width moments.** I:254–386 proves a dimension-independent Gaussian moment inequality by Gaussian rotation. It then bounds the RMS values and the Euclidean parameter-derivative operator norms of every fixed graph node by a polynomial in K_n. The normalized contraction derivative has the necessary n^(-1/2), which cancels the sqrt(n) from a scalar-times-vector node. Independent neuron-permutation equivariance controls the coordinate means. Together with the Gaussian matrix norm tail, this supplies all fixed coordinate moments, including for the actual empirical-feedback program and its query-noise perturbations. It does not assume a whole-space Lp bound for W0.

2. **Adaptive conditioning in both directions.** I:390–430 gives the conditional matrix mean and projected Gaussian residual under past forward and transpose observations. The mean satisfies both constraints by U^T Y=Q^T V. At each adaptive step the next input is measurable from the old transcript, so its answer adds a linear constraint to the queried matrix. This supports the conditioning induction and preserves independence of the conditional residuals for the two matrices.

3. **Higher-moment projection and empirical averaging.** I:432–505 bounds the discarded projection using its fixed rank and the identity `sum_i P_ii <= J`, giving expected normalized p-th error at most C_p/n for p>=2. Conditional variance controls empirical tests after introducing the fresh Gaussian vector; higher coordinate moments control tails of continuous polynomial-growth tests. These are the needed ingredients for mixed second moments and the larger finite query class used in A.

4. **Response coefficients and source covariance.** I:507–576 derives both orientation rules by least-squares conditioning and Gaussian integration by parts. Orthogonality removes the old forward-input part of a reverse answer, and the remaining correction is the expected formal derivative. The full source covariance is the uncentered input Gram, while only the stepwise innovation has residual variance. This distinction is preserved in G. The chain rule differentiates complete earlier coordinate expressions with deterministic feedback coefficients held fixed.

5. **Singular Grams.** I:578–702 perturbs the input of each initial-matrix query with fresh noise. Each successive query has a positive Schur complement at positive noise. It compares perturbed and unperturbed finite graphs in RMS with error epsilon P(K_n), then upgrades to every finite moment using interpolation and the already established moment bounds. The scalar response recursion has no inverse covariance; continuity of PSD square roots and dominated convergence of bounded first derivatives pass through rank drops. This supplies an actual singular-limit transfer. Formal zero-variance slots are retained. The proof therefore covers the zero initial reverse queries and rho=-1.

6. **Empirical feedback.** I:704–761 constructs the deterministic-coefficient oracle causally and compares it with the actual graph using normalized contraction differences. The all-order moments upgrade the RMS comparison to the asserted tests. The exact rank expansions supply both learned forward and learned transpose memories. There is no missing derivative of the operation selecting a deterministic limiting coefficient.

The maps used by A have the regularity required throughout this argument. In particular the caps make each product map have bounded first derivatives at any fixed cap. No cap-uniform bound from I is claimed or needed. Its scalar equations (6)–(13) match G's equations (2)–(3), including the sample factor Delta/2, the input Gram in the first update, both learned memories, and the current reverse return. Its conclusion supplies the well-defined finite law and finite formal-derivative expectations that G separately assumes.

No unresolved heavy identification result was found at this interface. The claim remains a fixed-program claim, as required for A's order of limits.

## 4. The primal response premises are discharged without circularity

P uses the same raw hidden matrices and the same rank-one normalization `u v^T/n` as I. Its HS norm is the ordinary Frobenius norm of these effective matrices, and its population tensor has HS norm `||u||_2 ||v||_2`. A uses these conventions correctly. P writes the opposite-label equations explicitly but states and proves the primal bounds for coefficients of absolute value at most one. Its comparison proof likewise uses absolute values of the common label coefficients. Thus A's four label choices are covered.

For the actual finite reference, the event

    max_a ||Z1_a(0)||_n <= 2,
    ||W2_0||op <= 10,  ||W3_0||op <= 10

has probability tending to one. The first assertion follows from the Gaussian marginal second moments, also at rho=-1; the matrix assertion is supplied by I's explicit Gaussian norm estimate. On this event P's deterministic proof applies to every node and cap choice on a fixed mesh.

The exact mapping to G's assumptions is as follows.

| Premise of G | Bound supplied by P | Verification |
|---|---|---|
| `||H1_ka||2 <= 2.3` | P:(20) | First primal box and softplus growth |
| `||H2_ka||2 <= 4.53` | P:(20) | `2+0.1*11*2.3=4.53` |
| `||H3_ka||2 <= 7` | P:(20) | `2+0.1*11*4.53=6.983<7` |
| `||delta3_ka||2 <= 0.7 s_k` | P:(24) | `0.1||w_k||2`, with `||w_k||2<=7s_k` |
| `||q2_ka||2 <= 7.7 s_k` | P:(24) | Operator norm at most 11 |
| `||delta2_ka||2 <= 0.77 s_k` | P:(24) | Gate at most 0.1 and contracting cut |
| First-feature increment bound | P:(27) | At most `0.0847 S |s_k-s_r|` |
| Second-feature increment bound | P:(27) | At most `0.5005 S |s_k-s_r|` |

Both increment constants are below one for S<=0.1. P obtains them from the exact product identity with the next-step operator, P:(14), so it has not discarded an Euler cross term. Its first and second feature slopes are respectively bounded by `0.0121||w_k||2` and `0.0715||w_k||2`.

I supplies convergence in probability of each empirical squared norm and each squared feature difference to its scalar-law expectation. A deterministic limit cannot violate a bound that holds with probability tending to one. This transfers every entry of the table to the law of G. There is no need to condition that law on the finite-width event, to average a bound over its complement, or to assert that auxiliary Gaussians in P are the actual network sources.

The logical order is therefore valid: actual finite primal inequalities; fixed-program moment identification; scalar primal hypotheses; response conclusion. The energy identity and uncut existence are not used to prove these premises. Width tends to infinity at a fixed finite mesh, and G supplies the separate uniformity in mesh size and caps.

## 5. Response dependency: its uniformity matches the assembly's use

The response proof was checked beyond its statement.

- G:127–225 obtains the forward-source maximum bound from the already supplied L2 time metric by a dyadic Gaussian-tail argument. Its reverse-source estimate is for a time average, obtained by convexity; it does not assert a mesh-uniform maximum for the reverse sources. Singular arrays cause no difficulty in either argument. Combining the envelopes uses convexity rather than independence of trained fields.
- G:227–304 derives path envelopes under past B-row bounds and the fixed A bounds 20 and 60. In particular, the exponential moments of L_1 and L_2 approach one as S decreases. This is sufficient to choose a positive S_a without using the current backward-row constants.
- G:306–365 bounds the two forward responses using only past rows. The direct source injection retains its Delta/2 factor, and the sample sum does not introduce a factor proportional to the number of slots. Zero initial reverse sources remain formal variables.
- G:367–431 includes both terms in the derivative of the top delta: the derivative through the readout, including the cap derivative, and the gate derivative multiplying the old readout. It bounds current B3 before current B2. The latter uses the full current B3 row and the separately supplied primal `||q2||2` estimate. Its constants are finite from the previously proved Gaussian envelope, so `S_0=min(S_a,1/10,1/(2C_B))` is strictly positive and uniform in rho, labels, mesh, and caps.
- G:433–458 gives Gaussian-square moments for each actual reverse query at each node, and the readout, followed by Gaussian truncation error. This is exactly the strength needed by A; a supremum inside the reverse-query exponential is not required.

The pointwise-in-time uniform bounds subsequently asserted in A:(10) respect this distinction. No missing whole-space Gaussian operator estimate or historical sensitivity bound is being substituted for G's conclusion.

## 6. Fixed-cap evolution and the mesh limit

A:189–209 constructs compatible smooth cuts. The denominator defining chi is positive; chi is one up to 1, zero from 2 onward, and nonincreasing in between. The flat endpoint derivatives give smooth joins. Thus its odd integral psi is smooth, `0<=psi'<=1`, and

    |tau_R(x)| <= min(|x|,2R),
    tau_R(x)=x for |x|<=R.

For x>=0, `psi(t)>=t chi(t)` gives

    partial_R [R psi(x/R)] = psi(x/R)-(x/R)chi(x/R) >= 0.

Together with oddness, this proves the precise old-defect nesting inequality used later. The radius R is not confused with the old output ceiling 2R.

The state space is the affine product of the first-field Hilbert space, two square-integrable kernels, and readout L2. It is complete in the sum of its four component norms. The fixed initial operators need only be bounded. P's population form and raw-coordinate comparison therefore apply.

With the same finite caps, all cut-mismatch defects vanish. P:(47c) gives a locally Lipschitz vector field on every fixed primal ball, and the primal estimates give a bounded velocity there. The contraction argument in A:216–225 consequently supplies a local C1 solution.

The continuation argument has actual quantitative control: P gives first displacement at most `0.4235 s^2`, K2 norm at most `0.8855 s^2`, K3 norm at most `1.5855 s^2`, and readout norm at most `7s`. At s<=0.1 the primal box is strictly improved. At fixed R, a slightly larger bounded ball has fixed finite Lipschitz and velocity constants, so successive extensions have a uniform positive available length. Bounded velocity also gives a state limit at any finite putative endpoint. This establishes continuation through 0.1 without assuming compactness of an infinite-dimensional ball or a clipped energy identity.

The one-step Euler defect on this ball is O_R(Delta^2), and the discrete inequality in A:241–246 yields O_R(Delta) uniform state error. Fixed-cap forward and backward field maps are locally Lipschitz by the same product estimates, so recomputed fields converge uniformly in L2. Nodal feature interpolation and raw-state recomputation are distinguished correctly.

For each fixed R and time s<=S_0, choose mesh nodes converging to s. Uniform L2 convergence permits an almost-surely convergent subsequence for each relevant field. Fatou transfers G's exponential moment bound to the fixed-cap ODE. The constants are uniform in R and s, even though the subsequence can depend on them. This proves a supremum of expectations, not an expectation of a time supremum. Taking square roots in G's squared tail estimate, with a possible change of constants and exponent, gives A:(11).

## 7. Same-space cut removal and uncut identification

### 7.1 Cauchy convergence of states and velocities

All capped ODEs use the same initial operators, first fields, and zero readout. For R'>=R, take theta_R as the old state and theta_R' as the new state. P:(35), with old output ceiling 2R, yields

    ||F_R'(theta_R')-F_R(theta_R)||state
        <= L_R d(theta_R',theta_R) + E_R,
    L_R <= C(1+R),
    sup_s E_R(s) <= C exp(-c R^2).

The old-defect estimate is applicable to the actual old readout and both actual old reverse queries, by the verified nesting of the cuts. No estimate of a new query tail appears here. Integration with zero initial discrepancy gives

    sup_[0,S_0] d(theta_R',theta_R)
        <= C S_0 exp(C(1+R)S_0-c R^2)
        <= C_5 exp(-c_5 R^2).

The last step follows, for example, by absorbing the linear term in R into half the negative quadratic term plus a constant. It is uniform over every R'>=R. Completeness gives uniform state convergence on the same spaces. Applying the vector-field inequality once more gives a velocity error bounded by a constant times

    (1+R) exp(-c_5 R^2) + exp(-c R^2),

which tends to zero. Thus velocities converge uniformly to a continuous curve and the limiting state is its integral. This establishes C1 regularity without postulating an uncut locally Lipschitz vector field.

### 7.2 The limiting velocity is the claimed uncut one

The compact-L2-curve product fact at A:(13) is valid. A compact subset K of L2 has uniformly vanishing square tails. One way to obtain the required indicator tails from the positive-part truncations in A's proof is

    |x| 1_{|x|>2M} <= 2(|x|-M)_+.

A finite L2 net and the Lipschitz property of positive-part truncation therefore prove uniform tails. For a bounded Lipschitz h, truncate the multiplier A(t) at M; the bounded part contributes at most `M Lip(h)||B_m-B||2` and the complement is controlled by those uniform tails. This proves (13) uniformly in time.

First the forward fields converge uniformly in L2, by bounded operator norms, HS-to-operator control, and Lipschitzness of phi. Also

    ||tau_R(W4_R)-W4||2
        <= ||tau_R(W4_R)-W4_R||2 + ||W4_R-W4||2 -> 0

uniformly. Product continuity with multiplier W4 identifies delta3 as `W4 phi'(Z3)`. Operator convergence of the trained adjoints then identifies q2 and makes it a continuous L2 curve. The old q2 truncation error and the same product fact identify delta2. Repeating the argument identifies q1 and delta1. HS continuity of rank-one tensors identifies both hidden velocities; the first and readout velocities follow directly.

Thus the limit satisfies precisely A:(3), with no residual cap or memory approximation. Fatou transfers the exponential bounds to the resulting actual uncut reverse queries and readout. All products used here are either a bounded scalar gate times an L2 field, a bounded operator acting on L2, or a tensor between separate populations. The proof never needs the product of two arbitrary same-population L2 fields to belong to L2.

## 8. Uniqueness and restart: the asserted competitor class is covered

Let a competitor be a continuous, absolutely continuous integral solution in the same affine state space, with the same initial state. On any closed common time interval its continuous state image is bounded. Its first marginal norms, trained operator norms, and readout norm are therefore bounded by a finite primal ball. The references have a cap-independent primal bound, so one ball contains both.

Take the competitor as the new state with identity cuts, and theta_R as the old state. P:(47c) explicitly allows identity new cuts and yields

    d(t) <= d(u) + C_ball integral_u^t [(1+R)d(v)+E_R(v)] dv.

C_ball may depend on the competitor's bounded primal norms, but it does not depend on R. The defects still involve only theta_R and obey the Gaussian estimate. Starting at time zero, d(0)=0, so

    sup_t d(theta_comp(t),theta_R(t))
        <= C exp(C_ball(1+R)S_0-c R^2) -> 0.

This identifies the competitor with theta. The use of an integral inequality covers absolutely continuous competitors as well as classical solutions. No Gaussian moments, pointwise query bounds, L-infinity multipliers, or source representation are required for the competitor.

If the competitor starts at u with theta_comp(u)=theta(u), the initial discrepancy from theta_R(u) is at most `C_5 exp(-c_5 R^2)`. Gronwall multiplies it by only `exp(C_ball(1+R)(v-u))`, which still vanishes as R increases. This proves uniqueness of the restarted portion. Existence of that portion is the restriction of the already constructed theta. There is no existence argument beyond S_0, or beyond the smaller advertised S_*, and no general restart theorem for arbitrary bounded-primal initial states. A:95–100 and 351–357 state this restriction correctly.

## 9. Raw-metric chain rule and energy

The Nemytskii chain rule used at A:386–400 is valid along a C1 L2 curve. In its integral difference quotient, the averaged gate is bounded by e and converges in probability to phi'(Z(t)). Its product with the difference between the state difference quotient and Z'(t) tends to zero in L2 by the uniform gate bound. Its remaining product with the fixed L2 vector Z'(t) converges by truncation. Hence

    d phi(Z(t))/dt = phi'(Z(t)) Z'(t)  in L2.

Continuity of this derivative follows from the same bounded-gate product argument and continuity of Z'. Bilinear operator-vector and L2-pairing differentiation is valid because the trained operators are C1 in operator norm, their increments being C1 in HS norm. This argument does not assert Frechet differentiability or a locally Lipschitz gradient on the entire L2 state space.

Write `b_a=y_a delta1_a/2` and denote each component of the feature vector field by F. Differentiating `g=(1/2)sum_a y_a <W4,H3_a>` through the three forward layers gives

    g' = E_1 sum_a b_a (Z1_a)'
         + <F_2,W2'>HS + <F_3,W3'>HS + <F_4,W4'>2.

The genuine adjoints constructed in Section 2 justify each reverse step. The coefficient of each hidden variation is exactly the tensor sum in A:(3), using the same half-sample weights. Substituting the evolution gives the three upper-layer squared velocity norms. The first contribution is

    E_1 b^T Cb = E_1 (Cb)^T C^(-1)(Cb)

for |rho|<1. At rho=-1, write `(Z1_1)',(Z1_2)'=(v,-v)`, with `v=b_1-b_2`. Then the contribution is `(b_1-b_2)v=v^2`, exactly the reduced raw norm. There is no missing factor of two from representing a one-dimensional direction twice.

Consequently

    g' = ||theta'||raw^2 >= 0,
    g(0)=0.

The primal bounds give `|f_a(s)|<=||W4||2 ||H3_a||2<=49s`, hence `|g(s)|<=49s`. With `S_*=min(S_0,1/196)`, this proves

    0<=g(s)<=1/4,
    integral_0^s ||theta'(v)||raw^2 dv = g(s).

This is the raw Hilbert norm, not the sum norm used for comparison. Their distinction and equivalence are appropriate; the comparison norm is not squared in the energy identity.

## 10. Exchange symmetry, label reversal, and rho=-1

For labels `(1,sigma)`, sigma in {-1,1}, swap the two initial first-layer fields while keeping both initial matrices fixed. Their joint initialization has the same law. Under the transformation in A:(14), the hidden sample fields exchange, the hidden matrices are unchanged, W4 gains the factor sigma, and every reverse field both exchanges samples and gains sigma.

This transformation respects each step because:

- `C_ba=C_(3-b),(3-a)` and `y_(3-a)=sigma y_a` give the first-field update;
- the reverse factor sigma cancels the exchanged label factor in each hidden update;
- the readout update gains sigma;
- oddness of each cut gives the stated transformation of the reverse fields.

No parity of softplus is required. In particular, at rho=-1 the initial pair is `(G,-G)` and its exchange is `(-G,G)`, which has the same law. The first-field dynamics stay in this realizable pair subspace. The proof does not incorrectly make the positive softplus features antisymmetric.

Finite-width exchange is equality in distribution, not a pointwise identity between the two predictions in one sample. I makes each fixed-program limiting prediction and feature second moment deterministic. Equality in distribution of the transformed finite quantities therefore yields equality of those deterministic limits:

    f_a = sigma f_(3-a),
    E[(H^ell_1)^2] = E[(H^ell_2)^2].

Fixed-cap mesh convergence and uniform cut removal preserve these pairings by L2 convergence and bounded L2 norms. Thus for `(1,sigma)`, `f_a=y_a g`. Reversing both labels reverses W4 and all backward fields, while preserving hidden states, so the same conclusion holds for the other two label vectors with `g=(1/2)sum_a y_a f_a`. The reasoning does not invoke uncut uniqueness to obtain its own symmetry premise.

The existing-path, energy, and stated feature-second-moment symmetry outputs advertised by A are therefore established locally. Exact applicability of any other curvature-action lemma cannot be audited from these four inputs alone; that distinction is retained in Section 12.

## 11. Physical clock and its precise normalization

With `r_a=f_a-y_a`, the symmetry gives `r_a=-y_a(1-g)`. Let `grad_raw f_a` denote the derivative represented in the raw Hilbert metric verified above. The feature evolution is

    dtheta/ds = (1/2) sum_a y_a grad_raw f_a.

Define

    t(s)=integral_0^s [4(1-g(v))]^(-1) dv.

Since `0<=g<=1/4`, it is C1 and strictly increasing, with

    1/4 <= dt/ds <= 1/3,
    S_*/4 <= t(S_*) <= S_*/3.

Its inverse satisfies `ds/dt=4(1-g)`. Therefore

    dtheta/dt = 2(1-g) sum_a y_a grad_raw f_a
              = -2 sum_a r_a grad_raw f_a.

This is exactly the per-sample coefficient -2r_a claimed in A:435–439. Equivalently it is raw gradient descent for the squared loss `sum_a (f_a-y_a)^2`. If a half-sum or sample-average loss were used instead, its clock factor would change; the explicit factor claimed in A fixes the normalization here. The constructed physical path exists at least on `[0,S_*/4]`. Neither the change of clock nor the local energy bound gives a later feature-time path or a global physical-time construction.

## 12. Required corrections, optional improvements, and out-of-scope obligations

### Required for this local modular theorem

**None found.** In particular, the review does not leave the response primal bounds, singular-Gram identification, common adjoints, or uniqueness against non-Gaussian competitors as unproved assumptions. They are accounted for above. The standard countable probability-extension, finite-measure approximation, Hilbert completeness, contraction, and integration arguments are applicable to the stated objects. No extra heavy research theorem is needed to bridge this four-file local construction.

This conclusion judges the supplied proofs on their contents. A's statements about the status of other reviews were not verified and should not be treated as mathematical evidence.

### Optional improvements

1. **Make the density family visibly bounded during approximation (A:121–150).** Say that the rational-grid approximations have compact support and a common bound when approximating a fixed bounded target, and that smoothing preserves that bound. Compact-uniform approximation alone does not by itself justify discarding a small-measure complement with uncontrolled approximant size. The proposed construction permits this elementary choice, so this is a clarification of the density argument, not a missing operator-construction theorem.

2. **Name the norm rather than its squared-norm equation (A:64).** Replace “SUM of (1)” by “sum of the first-field norm, the two HS norms, and the readout L2 norm.” Equation (1) defines the square; the rest of the text, its norm-equivalence assertion, and all comparisons identify the intended meaning unambiguously.

3. **Spell out real-radius inclusion (A:180–185, 280).** Mention `tau_R(x)=R tau_1(x/R)`, or state that integer radii suffice for the construction and cut removal. This makes the relation between the countable generating programs and the displayed supremum over real R immediate.

4. **Write the short quantitative velocity estimate (A:309–312).** The state Cauchy bound and comparison give an error of order `(1+R)exp(-c_5 R^2)+exp(-c R^2)`. Displaying it would make the C1 passage especially easy to verify.

5. **Define the physical residual and loss normalization at the clock (A:435–439).** Add `r_a=f_a-y_a` and, if naming a loss, `L=sum_a r_a^2`. The existing -2r_a claim and clock agree, but the unqualified phrase “squared-loss” admits other common normalizations.

6. **Keep external action-lemma applicability conditional (A:427–433).** The report verifies the explicitly stated local outputs. A future combined document should identify the exact action-lemma versions and match any additional hypotheses there. Those unprovided statements are not part of this audit.

### Outside this audit and not supplied by this local assembly

- Comparison of zero readout initialization with the small canonical finite-width random readout.
- Raw GD, joint width/step/cap limits for training, or convergence of an actual finite-width physical-time trajectory on a continuum of times.
- A full observable-convergence theorem beyond the finite-program and constructed-path statements used here.
- Strictly positive learning, curvature-action nontriviality, or every-time nonlazy behavior. A nonnegative energy derivative alone does not prove these claims.
- Independent validation of unprovided top/middle curvature-action lemmas, historical sensitivity bounds, or prior review conclusions.
- Existence beyond the local constructed interval, arbitrary-initial-state local well-posedness, or a uniform continuation theorem obtained by repeated restart.
- Global opposite-label continuation or all-finite-physical-time convergence. A local change of clock supplies none of these missing long-time results.
- Uniqueness across arbitrary population-space realizations, or a common ambient operator-norm limit of the finite Gaussian matrices.
- A final self-contained theorem incorporating the other obligations just listed.

These are substantive possible requirements of a larger program, but their absence is not a defect in the explicitly delimited local modular theorem reviewed here.
