# Independent complete proof review B1

**Verdict: CLEAN. No required correction remains in the supplied candidate.**

This verdict concerns the exact fixed-finite-width, fixed-finite-depth identities, global physical gradient flow, and supplied-trajectory response estimates actually stated in `docs/dense_response.md`. It does not establish a population limit, continuous-depth limit, uniform-in-size response theorem, autonomous compressed dynamics, eventual fitting, or a nonlazy limit. The candidate expressly excludes these conclusions.

## 1. Isolation, complete-read ledger, and integrity

The review used only the two documents in `/tmp/pde_dense_review_1`, their `INPUTS.json` manifest, and the explicitly requested mathematical-review skills and their applicable references. No checkout, studies, history, other task, prior review, or external mathematical source was consulted. No delegation, training, optimization trajectory, or experiment was performed. A small deterministic algebraic/directional-derivative check at one parameter state is recorded below.

Both supplied documents were read completely, with numbered lines:

| Document | Lines read | Bytes | SHA-256 before review | SHA-256 after review |
|---|---:|---:|---|---|
| `/tmp/pde_dense_review_1/docs/dense_response.md` | 1–380, all 380 | 13876 | `446c817b40cb7b32cf83a0fd1bdc3dd54461dbc7bf7b688eacdd9f5dbe9e0286` | `446c817b40cb7b32cf83a0fd1bdc3dd54461dbc7bf7b688eacdd9f5dbe9e0286` |
| `/tmp/pde_dense_review_1/docs/NOTATION.md` | 1–98, all 98 | 5110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

The manifest itself has SHA-256 `be467baadd47b0641eed063e0fb5f76f38ea216e7d6945f3035e8f0bfc34bb7d` before and after review. The 478 document lines are the full mathematical input. A final integrity check verified both document hashes, byte counts, and line counts against the manifest, and the unchanged manifest hash.

Instruction sources read in full:

- `/etc/codex/skills/solve-math-rigorously/SKILL.md`;
- `/etc/codex/skills/investigate-conjectures/SKILL.md`;
- `/etc/codex/skills/investigate-conjectures/references/research-contract.md`;
- `/etc/codex/skills/investigate-conjectures/references/evidence-ledger.md`;
- `/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md`.

The experiment-design and parallel-proof-search references were inapplicable: this was an isolated proof audit, without experimental work or delegation.

## 2. Contract and notation audit

Candidate lines 3–59 specify a separate dense residual architecture with finite integers `n,L,d,m >= 1`, arbitrary real `gamma`, arbitrary finite data, trainable `B`, every `W_ell`, and stored readout `a`. The residual-block count and parameter shapes are explicit. No input independence, invertibility, orthogonality, distinctness, or whitening is assumed or used.

The input map is exactly `h_a^0 = B x_a`, without a `1/sqrt(d)` factor. Therefore its parameter-gradient pairing contains `x_a^T x_b = d G_ab`. The candidate states this at lines 27–30 and uses it correctly throughout. This explicit separate-architecture definition does not silently apply the feedforward first-weight convention in `NOTATION.md` lines 16–24.

The independent Gaussian entries have variances `sigma_w^2/n`, `1`, and `A^2` in the residual, input, and stored-readout blocks respectively. In particular the stored readout is order one, not a readout secretly multiplied by `n` and not the canonical small-readout initialization. The distinction is explicit at candidate lines 34–43, as required by `NOTATION.md` lines 72–76. All subsequent statements hold for every finite parameter state, so no unproved Gaussian concentration or limiting initialization statement is needed.

The residual is `r=f-y`; it is not included in the adjoints. The full mean loss is `mathcal L = (1/m) sum r_a^2`. The mobilities are exactly `L` for residual matrices and `n` for the input and readout. These conventions are explicit and internally consistent. For `E=(1/2) sum r_a^2`, one has `mathcal L=(2/m) E`, hence the physical vector field is `(2/m)` times the half-sum vector field and `theta(t)=theta_E(2t/m)`. The candidate's clock conversion has the correct direction and factor.

Euclidean, Frobenius, and operator norms, RMS factors `1/sqrt(n)`, normalized sample pairings `1/n`, and finite matrix transposes agree with the canonical notation. The vector Kronecker products used to prove kernel positivity are explicitly finite Euclidean vectors, not population rank-one operators.

## 3. Complete adjoint, gradient, kernel, and energy audit

Write `q=gamma/L` within this review. The differential of a block with respect to its input is

`d h_a^(ell+1) = (I + q D_a^ell W_ell) d h_a^ell`.

Its transpose acts on the output adjoint. Thus terminal value `p_a^L=a` and recursion

`p_a^ell = (I + q W_ell^T D_a^ell) p_a^(ell+1)`

give precisely `p_a^ell = n partial f_a / partial h_a^ell`. The gate `beta_a^ell = D_a^ell p_a^(ell+1)` has the correct layer index. There is neither a residual factor nor an extra `1/n` inside the adjoint.

For arbitrary parameter variations, the independent chain-rule calculation is

`d f_a = (h_a^L)^T d a / n + (p_a^0)^T d B x_a / n + gamma/(nL) sum_ell (beta_a^ell)^T d W_ell h_a^ell`.

This proves every output gradient in (14.5). Multiplication by `(2/m) r_b`, summation over the batch, and then the block mobilities proves every physical velocity in (14.6). In particular the residual-matrix velocity is

`dot W_ell = -2 gamma/(mn) sum_b r_b beta_b^ell (h_b^ell)^T`.

The mobility `L` has canceled exactly the architectural `1/L` in this parameter gradient; the architectural depth factor remains in subsequent hidden-state recurrences.

Let `J_a` denote the full output-gradient row and let `D_res` be the positive diagonal mobility matrix. Then the tangent kernel is `K_ab = J_a D_res J_b^T`. The three block contributions are independently:

- readout: `(h_a^L)^T h_b^L/n = G_ab^(h,L)`;
- input: `(x_a^T x_b) (p_a^0)^T p_b^0/n = (x_a^T x_b) G_ab^(p,0)`;
- residual block `ell`: `gamma^2/(n^2 L) [(h_a^ell)^T h_b^ell][(beta_a^ell)^T beta_b^ell] = gamma^2 G_ab^(h,ell) G_ab^(beta,ell)/L`.

Thus (14.7), including `dot f=-(2/m)Kr`, has every factor correct. This calculation also confirms the use of the unnormalized input pairing rather than `G_ab` alone.

The vectors at lines 111–113 have precisely these three Gram matrices: `h_a^L/sqrt(n)`, `x_a tensor p_a^0/sqrt(n)`, and `gamma h_a^ell tensor beta_a^ell/(n sqrt(L))`. The latter denominator is correct because both normalized hidden pairings contribute a factor `1/n`. Their direct sum gives `c^T K c >= 0` for every real batch vector `c`, even when the data or kernel are singular and even when `gamma` is negative.

Differentiating the full mean loss yields

`dot mathcal L = (2/m) r^T dot f = -4 r^T K r/m^2`.

The block flow also gives

`-dot mathcal L = grad(mathcal L)^T D_res grad(mathcal L) = dot theta^T D_res^(-1) dot theta`.

These are exactly the two sides of (14.8). In particular the squared velocity coefficients are `1/n`, `1/n`, and `1/L`, not the mobilities themselves.

**Result:** (14.4)–(14.8) and their accompanying derivations are correct.

## 4. Global flow and all finite-horizon bounds

At fixed finite dimensions, compositions and products of the smooth function `tanh` make the parameter vector field smooth. On a closed sufficiently small parameter ball it is bounded and Lipschitz. The candidate explicitly constructs the contraction of continuous paths for `tau M` within the radius and `tau C<1`; a uniform limit of the iterates solves the integral equation and uniqueness follows from the same local Lipschitz estimate. No unstated global Lipschitz property is needed.

For `s<t` within a solution's existence interval, integrating the weighted velocity and applying Cauchy–Schwarz gives

`||D_res^(-1/2)(theta(t)-theta(s))|| <= sqrt(t-s) [integral_s^t ||D_res^(-1/2) dot theta||^2 du]^(1/2)`

`= sqrt((t-s)(mathcal L(s)-mathcal L(t))) <= sqrt((t-s) E_0)`.

This is (14.9). If a maximal forward existence interval ended at a finite time, the estimate would make the parameter path Cauchy at that endpoint in a norm equivalent to the ordinary finite-dimensional norm. It therefore has a finite limit. Local existence at that limit extends the original solution, contradicting maximality. Uniqueness propagates by overlapping local intervals. This proves global existence and uniqueness for every finite initial state and every nonnegative physical time.

The use of energy is sufficient even though the vector field need not be globally Lipschitz. The conclusion does not assert that parameters are bounded uniformly for all time, converge, or fit the data.

The readout and input parts of (14.10) follow by taking their coordinate blocks in (14.9) with `s=0`. For the residual-matrix part, let `Delta W_ell = W_ell(t)-W_ell(0)`. Then

`(1/L) sum ||W_ell(t)||_op <= (1/L) sum ||W_ell(0)||_op + (1/L) sum ||Delta W_ell||_F`

`<= (1/L) sum ||W_ell(0)||_op + [(1/L) sum ||Delta W_ell||_F^2]^(1/2)`

`<= (1/L) sum ||W_ell(0)||_op + sqrt(T E_0)`.

Thus the layer-average bound has no missing depth factor.

Since every coordinate of `tanh` has magnitude at most one, each residual increment has Euclidean norm at most `|gamma| sqrt(n)/L`. Consequently

`||h_a^ell(t)||/sqrt(n) <= ||B(t)||_F ||x_a||/sqrt(n) + (ell/L)|gamma|`,

which proves (14.11), using `ell<=L` and the input bound in (14.10). This correctly retains `||x_a||`, with no imported input normalization.

Also `||D_a^ell||_op <= 1` implies the asserted bound on `Lambda_T`. Multiplying the adjoint factors gives

`||p_a^ell|| <= ||a|| product_(i=ell)^(L-1) (1+||A_a^i||_op/L) <= ||a|| exp(Lambda_T)`.

Combined with (14.10), this is exactly the normalized adjoint bound at lines 297–299.

At fixed `n,L,T`, the global trajectory has compact image, all response/source expressions are continuous functions of that image, and the sample and layer sets are finite. Therefore `Lambda_T`, `B_v,T`, `B_w,T`, and `C_T` are finite. This finiteness claim does not require width-independent estimates on coordinate maxima.

**Result:** the global-flow argument, (14.9)–(14.11), and the later finite-horizon bounds are correct.

## 5. Exact physical training-time responses

Differentiating the original input map gives `v_a^0=dot B x_a`. Substituting the verified input velocity yields the first line of (14.12), with the factor `x_b^T x_a` and no division by `d`.

Differentiating a forward block gives

`v_a^(ell+1) = v_a^ell + gamma/L D_a^ell (W_ell v_a^ell + dot W_ell h_a^ell)`.

Hence `A_a^ell=gamma D_a^ell W_ell` is the correct forward generator and `F_a^ell=gamma D_a^ell dot W_ell h_a^ell`. The already verified matrix velocity implies

`dot W_ell h_a^ell = -2 gamma/m sum_b r_b beta_b^ell G_ba^(h,ell)`.

Multiplication by `gamma D_a^ell` yields the stated `F_a^ell`, including its negative sign, factor `2/m`, and factor `gamma^2`. The factor `n` has canceled against the hidden pairing, exactly as in (14.12)–(14.13).

The adjoint equation is `p_a^ell=(I+(A_a^ell)^T/L)p_a^(ell+1)`. Its time derivative is

`w_a^ell=(I+(A_a^ell)^T/L) w_a^(ell+1) + (dot A_a^ell)^T p_a^(ell+1)/L`.

The terminal derivative is `w_a^L=dot a`. Thus both the backward generator and source in (14.12) have the correct transpose and index.

The remaining product and chain rules are

`dot z = W v + dot W h`,

`dot D = diag(phi''(z) odot dot z)`,

`dot A = gamma(dot D W + D dot W)`,

`dot beta = dot D p^(ell+1) + D w^(ell+1)`.

All match (14.13). In particular `dot A` and therefore `S` can be computed from the supplied exact trajectory and the already determined forward response; there is no unclosed dependence on `w` inside `S`. The subsequent `dot beta` does contain the correctly computed `w`. The normalized Gram derivative is exactly the two product-rule terms divided by `n`.

**Result:** all formulas in (14.12)–(14.13), the source explanation, and the hidden Gram derivative are exact in physical training time.

## 6. Ordered noncommutative grading and exact-source tails

The product `P(ell,b)` in (14.14) places later-depth matrices on the left. Repeated substitution gives the source insertion after block `b` as `P(ell,b+1)F^b/L`, which is exactly (14.15). The endpoints and empty-product convention are correct.

For clarity, the corresponding exact backward formula is

`w^ell = P(L,ell)^T w^L + (1/L) sum_(b=ell)^(L-1) P(b,ell)^T S^b`.

Thus the source at depth `b` is propagated only through blocks preceding `b` in the backward direction. This directly verifies the backward indexing used in (14.16) and the reverse-depth argument used for (14.18).

In degree `j`, one selects distinct increasing indices `i_1<...<i_j`; the matrix monomial retains the order `A^(i_j)...A^(i_1)/L^j`. Submultiplicativity and the triangle inequality bound its degree sum by the scalar elementary symmetric polynomial in `c_i=||A^i||_op/L`. The power `(sum c_i)^j` includes each product with distinct indices exactly `j!` times, plus nonnegative repeated-index contributions. Therefore its degree-`j` norm is at most `(sum c_i)^j/j!`. Nothing in this argument commutes the matrices, diagonalizes them, or controls them by their eigenvalues; nonnormal amplification is covered by operator norms.

The grade-zero recurrences in (14.16) retain the full boundary and forcing terms. A positive grade is obtained by one additional generator insertion at a new depth. This generates precisely the same ordered monomials. Summing grades yields the original inhomogeneous recurrence and boundary values. Because there are only `L` distinct depths, grades above `L` vanish. The backward recurrence uses the transposed generators in the correct reverse order.

It is essential that the source itself has grade zero even if its exact expression already contains dense matrices or the exact forward response. Lines 275–276 explicitly state this convention. The theorem is a grading of propagator factors with supplied exact sources, not a polynomial-degree expansion of all nonlinear dependencies and not a Taylor expansion in training time.

For any boundary or source insertion, the omitted degree sum is bounded by `R_K(Lambda_T)`. Summing the boundary norm and the `1/L`-weighted forcing norms gives `B_v,T R_K(Lambda_T)` or `B_w,T R_K(Lambda_T)` after the explicit RMS normalization. This proves both inequalities in (14.18), uniformly over the finite samples and depths and over `[0,T]`.

For nonnegative `Lambda`, writing `j=K+1+q` and using `(K+1+q)! >= (K+1)!q!` gives

`R_K(Lambda) <= Lambda^(K+1)/(K+1)! sum_(q>=0) Lambda^q/q! = exp(Lambda) Lambda^(K+1)/(K+1)!`.

The exact finite polynomial errors vanish when `K>=L`, although the exponential upper bound need not vanish then. This is not a contradiction and is stated correctly.

**Result:** (14.14)–(14.18), including chronology, grading, all normalizations, and factorial tails, are correct.

## 7. Separate recomputed-source error

Keep the supplied trajectory, all generators, and the terminal response fixed, as stipulated in lines 328–330. Let `w_K` be the truncated response with exact source `S`. Then

`w - tilde w_K = (w-w_K) + (w_K-tilde w_K)`.

The first term is the exact-source tail already proved. The second is linear in `S-tilde S` and has zero terminal value. Every insertion is propagated by a truncated ordered product whose norm is at most

`sum_(j=0)^K Lambda_T^j/j! <= exp(Lambda_T)`.

The `1/L`-weighted sum of insertion norms is exactly the defined `E_S,T`. This proves (14.19), without silently treating a changed source as exact or claiming a factorial bound on an arbitrary source perturbation.

For the particular substitution `v -> v_K` while `W,dot W,h,p,z,D,r` remain exact,

`dot z - dot z_tilde = W(v-v_K)`.

Therefore

`dot D - dot D_tilde = diag(phi''(z) odot W(v-v_K))`.

The `D dot W` part of `dot A` is unchanged, so

`S-tilde S = gamma W^T [phi''(z) odot p^(ell+1) odot W(v-v_K)]`.

This is precisely (14.20), with no omitted term under the explicitly frozen quantities. Bounding the diagonal multiplier by its coordinate infinity norm gives

`||S_a^ell-tilde S_a^ell||/sqrt(n) <= |gamma| ||W_ell||_op^2 ||phi''(z_a^ell) odot p_a^(ell+1)||_infty ||v_a^ell-v_(K,a)^ell||/sqrt(n)`.

Taking the layer average and supremum proves `E_S,T <= C_T B_v,T R_K(Lambda_T)` with exactly the constant (14.21). In particular one may combine the two stated estimates to obtain

`sup ||w-tilde w_K||/sqrt(n) <= [B_w,T + exp(Lambda_T) C_T B_v,T] R_K(Lambda_T)`

for this specific replacement and fixed trajectory. The candidate does not need to display this immediate combined corollary for completeness.

The coordinate maximum in `C_T` is finite in this finite-state theorem. The normalized Euclidean adjoint bound alone does not make that coordinate maximum width independent, and the candidate expressly recognizes this. If the trajectory or `dot W` changes, additional terms appear; the final paragraph correctly excludes autonomous approximation and nonlinear feedback claims.

**Result:** (14.19)–(14.21) correctly separate propagation of source error from the source error created by truncating the forward response.

## 8. Deterministic single-state checks

These checks support the independent algebra above; they do not replace a proof or provide training or limiting evidence. There were no optimization steps and no trajectory simulation. One fixed state used `n=2`, `L=3`, `d=2`, `m=3`, `gamma=-0.7`, with

`X = [[1.2,-0.4],[0.3,0.9],[1.2,-0.4]]`,

`y = [0.2,-0.8,0.5]`, `a = [0.8,-0.6]`,

`B = [[0.4,-0.7],[0.9,0.2]]`,

`W_0 = [[0.2,0.8],[-0.5,0.1]]`,

`W_1 = [[-0.6,0.3],[0.7,0.4]]`,

`W_2 = [[0.1,-0.9],[0.6,-0.2]]`.

The repeated input makes the batch input Gram singular. The generators do not commute: the maximum over samples of `||A_a^0 A_a^1-A_a^1 A_a^0||_op` was approximately `0.4693442222`. These choices test the factors and ordering without relying on orthogonal data, positive residual strength, or scalar/commuting matrices.

The check independently assembled each output-gradient row, the diagonal mobility matrix, the explicit physical vector field, all response recurrences, and the grade recurrences. Central differences with step `1e-6` checked output derivatives and directional derivatives in the physical vector-field direction. Such parameter probes were derivative checks at this fixed state, not integration of the flow.

| Check | Maximum absolute discrepancy |
|---|---:|
| All output-gradient entries vs central differences | `4.63e-11` |
| Explicit physical vector field vs mobility-weighted loss gradient | `5.55e-17` |
| Kernel formula vs full gradient Gram | `4.44e-16` |
| Prediction velocity vs `-(2/m)Kr` | `6.92e-11` |
| Energy equality vs weighted squared parameter speed | `1.67e-16` |
| Forward response vs directional differences | `1.35e-10` |
| Backward response vs directional differences | `6.09e-11` |
| Gate response vs directional differences | `3.73e-11` |
| Gated-adjoint response vs directional differences | `5.94e-11` |
| All forward grades summed vs exact response | `2.22e-16` |
| All backward grades summed vs exact response | `5.56e-17` |
| Recomputed-source identity (14.20), over `K=0,1,2,3` | `3.62e-17` |

The kernel's smallest computed eigenvalue was `1.88e-16`, consistent with its exact singular positive-semidefinite Gram structure. The values for the same-state bounds were `Lambda=0.5589910729`, `B_v=0.6072156209`, `B_w=0.4429795736`, and `C=0.3191077739`.

| K | Forward error | Forward bound | Backward exact-source error | Backward bound | Recomputed backward error | Bound (14.19) |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | `0.1037443772` | `0.4547480837` | `0.06567992955` | `0.3317505434` | `0.06622764327` | `0.3391315415` |
| 1 | `0.01648687014` | `0.1153199723` | `0.01276761774` | `0.08412891632` | `0.01284302832` | `0.08491469488` |
| 2 | `0.0006689408435` | `0.02045133022` | `0.002202043302` | `0.01491977681` | `0.002202043302` | `0.01491977681` |
| 3 | `1.58e-16` | `0.002774422212` | `5.56e-17` | `0.002024013096` | `7.08e-17` | `0.002024013096` |

For `K=0,1,2,3`, the source errors were respectively approximately `0.00422035`, `0.000449297`, `1.37e-17`, and `1.37e-17`; every value satisfied `E_S <= C B_v R_K(Lambda)`. The exact algebra explains why the two higher-order values are at roundoff: the source only uses forward responses through depth `L-1`.

Additional analytic edge checks were `gamma=0`, `E_0=0`, `L=1`, `K=0`, `K>=L`, and zero or repeated inputs. They introduce no exceptional denominators or missing terms. In particular `gamma=0` makes all propagator generators and residual sources zero, so grade zero is exact; `E_0=0` makes the physical vector field vanish; and zero/coincident data require no rank assumption.

## 9. Claim ledger and hostile audit

| Claim | Status | Scope and dependencies | Surviving required correction |
|---|---|---|---|
| Architecture, initialization, and physical-clock normalization | Exact under stated definitions | Finite dense residual architecture; explicitly distinct from the feedforward and small-readout conventions | None |
| Adjoint, output gradients, and physical block velocities | Proved algebraically | Smooth finite `tanh` network, all trainable blocks | None |
| Tangent kernel, positivity, prediction flow, and energy equality | Proved algebraically | Arbitrary finite batch, including singular/repeated inputs | None |
| Unique global physical gradient flow | Proved | Every finite initial state; nonnegative physical times; positive fixed mobilities | None |
| Finite-horizon parameter, hidden-state, and adjoint bounds | Proved | Each fixed `n,L,T`; actual initial norms and loss | None |
| Forward and backward physical responses and Gram derivatives | Proved algebraically | Along the exact finite flow | None |
| Ordered-product grading and exact-source factorial tails | Proved | Supplied exact trajectory, boundary values, sources, and generators | None |
| Arbitrary source-perturbation propagation bound | Proved | Same supplied trajectory, generators, and terminal response | None |
| Particular recomputation through `v_K` and constant `C_T` | Proved | Only forward response is substituted; all listed state/velocity quantities stay exact | None |
| Width/depth-uniform constants or a dense population limit | Not claimed | Would require new uniform estimates and limit arguments | Outside this theorem |
| Autonomous response dynamics, fitting, or a nonlazy limit | Not claimed | Would require trajectory/source feedback control and other new results | Outside this theorem |

The strongest apparent structural objections do not invalidate the stated result:

- **Hidden trajectory information:** the coefficient and source access is acknowledged at the outset. The result explicitly approximates derivatives along a supplied trajectory and retains ambient-sized matrices and vectors. It is not offered as an autonomous or compressed witness.
- **Matrix noncommutativity/nonnormality:** the exact chronological products and operator-norm bounds preserve these effects; neither eigenvalue control nor matrix commutation is assumed.
- **High-to-low/source feedback:** exact-source grading is distinguished from recomputation, and the latter receives the separate `E_S,T` term and a derived source estimate for one explicitly frozen-state substitution. Full dynamical feedback is excluded.
- **Width escape through coordinate maxima:** the finite `C_T` is not promoted to a width-independent constant. The candidate identifies this limitation expressly.
- **Finite/limiting claim confusion:** the finite global flow and compact-time response bound are not used to interchange width, depth, grade, or time limits. No all-time response-uniformity is asserted.
- **Degenerate input geometry:** the proofs use direct inner products and norm inequalities only; no inversion or whitening is hidden.
- **Self-containment:** every required identity, continuation argument, ordering count, scalar tail estimate, and source-perturbation estimate appears in the candidate. Its references to earlier sections merely distinguish scope and are not mathematical dependencies.

There is no supersession claim in this review: prior artifacts were neither read nor used. There is also no empirical claim-ladder promotion from the deterministic derivative checks.

## 10. Final assessment

All 21 numbered formulas and their proofs were checked against the complete canonical notation input. The finite dense architecture, original `Bx` input normalization, stored order-one Gaussian readout, full mean-loss factors, mobilities, adjoint transposes, exact gradient/kernel/energy relations, global continuation, compact-horizon estimates, bidirectional physical responses, chronological grading, exact-source tails, and separate recomputed-source estimate are consistent and justified. No required mathematical, normalization, scope, or self-containment correction was found.

**CLEAN for the supplied exact finite-scope theorem and estimates.**
