# Independent adversarial audit

**Verdict: CLEAN.** I found no substantive error, missing model-specific proof lemma, unjustified asymptotic count, or unresolved hypothesis in the claims as written. The positive theorem and the restricted negative theorem concern different state spaces and are compatible. This verdict applies only to the exact inputs identified below.

## Isolation, hashes, and complete read coverage

This was a fresh audit. I read only the following two input files, in full. I did not consult the rest of the project, source history, previous reviews, skills, external references, or the web. I used no agents, Git operations, or numerical experiments. The only file written was this `REVIEW.md`; neither input was edited.

| Input | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `NOTATION.md` | 98 | 5,110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `linear_dynamics.md` | 1,166 | 45,268 | `b43a1ec2a301a5b6dbc5bde1b299afa87b4257be32a93ae86f926c8685c6ee71` |

Both files are in `/tmp/pde-established-linear-review.FhGoMM/`. Hashes were checked before reading and again after the mathematical audit; they agreed exactly.

Read coverage is `NOTATION.md:1–98` and `linear_dynamics.md:1–1166`, including all prose, definitions, displayed equations, and proofs. An output truncation in the initial combined read was repaired by a separate complete read of lines 665–830. No unread interval remains.

| Portion of `linear_dynamics.md` | Coverage | Obligations checked |
| --- | --- | --- |
| Introduction and Section 1 | 1–143 | Model, normalizations, Theorem 1, scope of every limit and fitting claim |
| Section 2 | 144–368 | Cyclic algebra, explicit Fock source, Lemma 2, all moment and norm estimates |
| Section 3 | 369–545 | Trace ideals, local construction, global continuation, restart, Corollary 3 |
| Section 4 | 546–718 | Cutoff, finite-word Picard construction, Gram continuity, exact GD and interpolation |
| Section 5 | 719–828 | Exact encoder/closure hypotheses and Theorem 4's quantifiers |
| Section 6 | 829–1058 | Lemma 5, graph growth, PDE prolongation, polynomial and analytic contradictions, both physical-label cases |
| Section 7 | 1059–1166 | Local feature profiles, global physical transport, width-one counterchecks |

## Required errors or corrections

**None found.** In particular, I do not find a basis for rejecting Theorem 1, Lemma 2, Corollary 3, Theorem 4, or Lemma 5 under their stated hypotheses. The remaining comments below are optional clarifications, not conditions needed to make the results true.

## Detailed verification

### 1. Normalization, cyclic algebra, and initial source

Equations (1.1)–(1.4) and (2.1)–(2.4) are consistent with the notation contract. The loss is the full square, so the factor 2 belongs in the gradient. Dividing each endpoint by `sqrt(n)` converts the four canonical mobilities `(nκ,κ,κ,nκ)` into the common multiplier `κ` on the four normalized factor gradients. For example,

`ΔB = -(2κηr/n)(R^T W^(4))(W^(1))^T = -2κηr(R^T v)u^T`.

The other three blocks give exactly (2.1) multiplied by `-2κr`. The stored readout remains variance one; its normalized proof embedding has entry variance `1/n`. There is no unnoticed switch to small readout.

The four cyclic block positions give `D C=(C^T)^3`. Each length-three block path passes through a rank-one endpoint map, so `rank(C^3)≤4`, including for the infinite Hilbert-space construction. Each diagonal block of `C^4` has trace `v^T RBu`; hence `f=Tr(C^4)/4`. Differentiating the four factors gives exactly the four nonnegative terms in (1.4). Consequently `K=||C^{*3}||_HS^2` and the residual/loss factors in (1.6) are correct.

The six-letter real Fock construction is explicit and bounded. Acting with the first four creation/annihilation letters cannot delete the terminal fifth or sixth letter. Thus each root reproduces the vacuum moments and the two root sectors are orthogonal, as in (2.7). Typed copies provide actual adjoints between the specified layer spaces. The norm bound `||C_0||≤2` follows from the orthogonal cyclic block structure. The four initial kernel vectors in (2.14) are individual unit words, giving `K(0)=4`; the cross-root prediction is zero.

### 2. Gaussian fixed words and rooted Gram variance

Lemma 2's Wick counting is sufficient as stated. A pairing of a trace word of length `2q` contributes `n^(v-q-1)`: `n^v` index assignments, `n^-q` from covariances, and `n^-1` from the normalized trace. Its quotient multigraph is connected with `q` paired edges, so `v≤q+1`. At equality it is a tree. The original closed walk uses each tree edge once in each direction, which forces opposite transpose markers for a paired matrix entry. Leaf removal gives noncrossing pairings. Conversely, removing adjacent equal-colored, oppositely oriented pairs gives one new free vertex per restored pair. This establishes the leading count without an imported freeness theorem.

The vacuum expansion has exactly those nested color/orientation matches, each with coefficient one. Odd words vanish on both sides. For a covariance of two normalized traces, the pairings confined to separate traces cancel. Every remaining pairing joins the two walks, giving a connected quotient and the bound `n^(v-q-2)≤n^-1`. This rate need not be optimal; it already proves the claimed fixed-word `L^2` convergence. The number of pairings is fixed before taking width to infinity.

The net estimate is numerically consistent: two nets cost `9^(2n)=81^n`; `||G||>12` implies some net bilinear form exceeds 6; its Gaussian tail costs `2 exp(-18n)`. Gaussian endpoint squared norms have variance `2/n`. These estimates give a deterministic high-probability source norm bound without requiring convergence of the matrix operator norms.

For the independent endpoint roots, conditioning on the matrices gives the exact formulas

`Var(g^T T g | T) = 2||sym(T)||_HS^2/n^2`,

`E[(g^T T h)^2 | T] = ||T||_HS^2/n^2` for independent `g,h`.

They imply (2.12). The good event bounding `T=P_i^T P_j` is matrix-measurable, so conditional Chebyshev is legitimate there. Its complement has vanishing probability. No unproved expectation bound on the exceptional event is needed. This closes both same-root and cross-root Gram convergence, including joint convergence for any fixed finite family.

### 3. Global trace-class construction and fitting

The affine state space is correctly chosen. The source itself need not be trace class or Hilbert–Schmidt, whereas the current cube and fourth power are finite rank by the cyclic geometry. The cubic adjoint has the same block support as the increment. Thus (3.2) maps the closed cyclic trace-class subspace into itself and all asserted traces are defined.

The telescoping estimates in (3.3) are valid without commutation. The constants are consistent: the cubic difference costs `3A^2`, the fourth-power trace difference costs `A^3`, and the kernel difference costs `12A^5` after using `||C^{*3}||_HS≤2A^3`. The vector field is locally bounded and Lipschitz in trace norm. The supplied integral contraction argument gives local existence and uniqueness.

Differentiating the trace is legitimate because every differentiated term contains the trace-class factor `dot Q`; trace cyclicity gives (3.4). The residual formula yields

`integral_0^T r^2 K ≤ r(0)^2/(4κ)`.

Rank at most four gives `||C^{*3}||_1≤2 sqrt(K)`. Therefore the path length is bounded by `4κ integral |r| sqrt(K)`, and time Cauchy–Schwarz gives exactly

`||Q(T)-Q(0)||_1 ≤ 2|r(0)| sqrt(κT)`.

This is a dimension-independent bound on every finite horizon. On the resulting ball the vector field is bounded, so a solution approaching a finite maximal time has a trace-norm limit and can be continued. The same proof works from arbitrary cyclic trace-class restart states, with their residual recomputed, and for arbitrary finite initial factors. It does not require feature-time completeness.

Corollary 3 also closes. With `z=Bu`, `p=R^*v`, the product rule gives `D z=Ap`, `D p=Mz` and (3.8). The two endpoint squared norms have identical derivative `-4κrf` and initial value one. Since `r=-y exp(-2κ integral K)`, their common value remains at least one. Thus `K≥2|f|`. When `y≠0`, `dot f(0)=8κy` supplies a nonzero output at a positive time; `|f|` is nondecreasing thereafter. The exponent in (3.10) follows. This works for either sign of `y`. When `y=0`, uniqueness makes the initialized population stationary. Fitting is asserted for this initialized population, not for every possible restart state.

### 4. Picard width limit and exact GD

The cutoff is applied to the increment `Q`, with a unit margin beyond the energy bound. Its boundedness and Lipschitz constants are uniform in width on the stated high-probability initialization event. The support-boundary argument gives a global Lipschitz field, while the exact trajectories stay in the region where the cutoff equals one.

The finite-word Picard argument has the needed closure property. The pure source adjoint cube is a sum of four rank-one blocks. Multiplying a rank-one block by a source map appends a typed source letter or makes an endpoint pairing; multiplying rank-one blocks produces Gram coefficients. The pure source fourth-power trace is itself a rooted pairing. Integration changes coefficients only. Consequently each fixed Picard iterate uses a finite source-word list independent of width and time.

The cutoff norm does not introduce a missing operator-limit hypothesis. For a finite-rank expression `U c V^*`, its nonzero singular values are those of `G_u^(1/2) c G_v^(1/2)`. The partial-isometry argument remains valid for singular Gram matrices. The supplied finite-dimensional continuity arguments justify square roots, singular values, and Schatten norms without Gram inverses. Iterating continuous operations and integration therefore gives coefficient and readout convergence in the uniform path topology at each fixed Picard index.

The factorial estimate (4.5) follows by summing successive-increment bounds `M H^(h-1)t^h/h!`. Its constants do not depend on width. All Picard paths lie in a common larger trace-norm ball. Choosing the iteration index first and width second proves (1.7); it does not exchange a growing word degree with the width limit. A fixed current rooted word expands into finitely many such expressions at each iterate. Factor telescoping and the fixed rank bounds justify the additional pairings, contractions, and Schatten-norm observables.

Equation (4.6) is exactly simultaneous GD in the normalized variables. It evolves `Q` alone and recomputes the residual from the fourth-power trace. It does not incorrectly Euler-step the continuous residual identity. This matters because the simultaneous factor update has higher-order prediction cross terms.

The cutoff flow has one-step defect at most `H M h^2/2`, and the geometric error recurrence gives (4.8). Interpolation adds at most `2Mh`. For sufficiently small `h`, the cutoff Euler nodes remain inside the unit margin; the interpolants do also, by the same estimate or convexity. The extra horizon covers the last interval intersecting `[0,T]`. Induction then identifies the cutoff Euler scheme with actual GD on the required interval. All thresholds are independent of width on the good event. Therefore every deterministic positive `η_n→0` is admissible, and recomputation after linear weight interpolation is exactly the readout being compared. No hidden width/step relation is needed.

### 5. Graph independence and unbounded connected graphs

Lemma 5 handles the main counting issue correctly. Equality partitions of index assignments can merge more than two slots, so the auxiliary higher-valence incidence networks are necessary and are explicitly included. For injective assignments, a tensor-entry monomial records the tensor types and their typed incident indices. Distinct numerical indices within a layer identify distinct vertices. Commutativity forgets only the ordering of identical tensor copies, which graph isomorphism already ignores. The prohibition of isolated index vertices prevents invisible factors of `n`.

Thus distinct injective network types have disjoint monomial supports. In (6.1), the discrete partition contributes the original injective type, while every proper quotient has fewer index vertices. Choosing a maximal-vertex graph with nonzero coefficient proves the asserted independence. An adequate width threshold is the largest number of index vertices of any one type in the finite family and its quotient closure. There is no appeal to independence of an infinite family at one fixed width.

The endpoint-only identities (6.4) and (6.5) are correct. In particular, the coefficient of `u^T H^j u` in `D_0^(2j-1)f` is `4^(j-1)`. Every replacement in the full derivation is a positive graph replacement. Therefore these endpoint-only histories survive with a positive coefficient in the full derivative. The selected graph `Γ_j` is a connected path with tensor degree `4j+2`, exactly as claimed. Additional differentiation histories cannot cancel it.

### 6. Scalar/PDE nonclosure, analytic basepoints, and zero label

The encoder bound controls the entire spatial profile, not merely finitely many values. Every spatial derivative still uses the same finite graph alphabet because only the coefficient functions depend on the spatial variable. Products can make disjoint unions but cannot create a new connected graph type. Hence all field jets lie in the algebra (6.7).

Equations (6.8)–(6.10) supply the required prolongation argument. The state derivation commutes with spatial differentiation, and the chain rule gives the evolutionary derivative at each readout point. After `k` applications, at most jet order `ρ+kσ` is needed. In the polynomial case the expression remains a finite polynomial in these jets, with a graph family bounded independently of width for fixed `k`. Identities on an open state set extend as polynomial identities by the supplied elementary argument. Lemma 5 is therefore applicable at the chosen derivative order.

For the analytic case, centering at the actual zero-network jet tuple is essential and has been done correctly. Empty-graph coefficients may depend on width and need not vanish. After centering, all nonzero terms have positive scaling order under `θ→λθ`. At any fixed order in `λ`, only finitely many Taylor terms contribute, and every resulting graph still has components in the same finite set. The stipulated mixed differentiability suffices for the finite prolongations and coefficient extraction. No uniform-in-width Taylor radius, inverse encoder, or nonsingular zero-state Jacobian is required. Comparing degree `4j+2` with the positive `Γ_j` coefficient proves the feature-flow contradiction.

For physical flow with `y≠0`, the two summands in (6.12) raise homogeneous degree by two and six. Consequently the lowest-degree component of `X^k f` is precisely `(2κy)^k D^k f`; mixed differentiation cannot contribute at that degree. This proves the stated contradiction for either nonzero sign of the label.

The physical `y=0` argument is separately valid. Writing `X^k f=(-2κ)^k P_k` gives `P_(k+1)=f D P_k`. By induction, `P_k` contains `f^k D^k f` with nonnegative remainder in its graph expansion. At `k=2j-1`, the resulting disjoint union contains `k` output-path components and a `Γ_j` component with positive coefficient. Its degree is `4+6k`. No graph product from (6.7) can supply the forbidden component, so stable independence contradicts both a polynomial identity and the corresponding analytic Taylor coefficient. The vanishing vector field at the zero state does not defeat this higher-degree argument on a full state neighborhood.

The theorem's scope is appropriate: polynomial closures on open sets of all current states, or analytic closures near the zero network, with a width-uniform bounded-contraction encoder and local finite-order expressions/readouts. It does not establish nonclosure along the Gaussian-initialized orbit or rule out arbitrary encoders. The text explicitly preserves these limitations. The stationary initialized population at zero label is fully compatible with the open-state negative theorem.

### 7. Unrestricted transport and finite-width checks

The feature-profile construction is a valid local realization. On the `2ε` operator-norm ball, the cubic field bound is `8ε^3` and its Lipschitz bound is `12ε^2`. The stated interval gives contraction factor `1/2` and image norm at most `4ε/3`. The local flow identity gives the translation PDE and the jets in (7.3). Their unbounded graph degree excludes this encoder from (5.3).

For physical flow, global forward existence from arbitrary finite states was already proved. Thus (7.4) is defined on the fixed half-line for every current state. Translation is continuous in the compact-uniform topology and satisfies the restart identity. The characteristic `(t-τ,s+τ)` reaches the initial line without leaving the domain, proving the classical uniqueness formula for `C^1` profiles. The boundary at `s=0` is an outflow boundary; no additional inflow condition is missing. Continuous profiles have the stated translation semigroup evolution. This is an exact output realization with an unrestricted future-trajectory encoder, and the text appropriately refrains from identifying it with the constructive Gaussian population limit.

The width-one checks are correct: both displayed states have characteristic polynomial `λ^4-1`, while their kernels are `4` and `25/4`. Physical output derivatives consequently differ when `y≠1`. The squared-factor equations (7.7) follow directly from the product rule and give a valid width-one scalar closure. This does not contradict a theorem requiring the same bounded description for all sufficiently large widths.

## Self-containment and notation

The proof is self-contained for its substantive probabilistic, dynamical, approximation, and nonclosure claims. The specialized Gaussian/Fock limit, rooted variance reduction, global continuation, finite-word approximation, dimension-independent GD estimate, stable graph independence, and PDE prolongation arguments are all supplied. No external research theorem or unavailable project construction is needed.

In the literal foundational sense, the chapter assumes ordinary Hilbert-space and trace-class background: adjoints, singular-value decompositions, completeness of the trace-class norm, and elementary calculus/integration. It does not rederive all of that background. This is a prerequisite convention, not an open hypothesis in one of the stated results.

Notation is coherent in the substantive calculations. The finite/population norm distinction, canonical versus normalized endpoints, actual transpose/adjoint directions, residual convention, and mobility/time factors remain consistent. The auxiliary Hilbert vectors in Section 3 and the auxiliary contractions in Section 6 are identified separately from neuron coordinates and encoded fields. No implicit neuron-law or cross-space operator-norm convergence is asserted.

Optional clarifications only:

1. `NOTATION.md:78` reserves `t` for physical training time, whereas (7.2) uses `t` as the evolution parameter of the explicitly specified feature flow. The context and the subsequent separate physical construction make the meaning clear, so this does not invalidate a statement. Using `τ` in (7.2) would preserve the clock convention without a local reuse.
2. The self-containment declaration could explicitly name standard Hilbert/trace-class facts as background, particularly trace-class completeness used by the integral contraction argument. No additional model-specific lemma needs to be added.

Neither clarification changes the CLEAN verdict.
