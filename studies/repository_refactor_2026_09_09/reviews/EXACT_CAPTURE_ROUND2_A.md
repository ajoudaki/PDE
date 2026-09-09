# Isolated adversarial complete proof review

## Verdict

**CLEAN. No required mathematical corrections found.**

The statements in Sections 8–12 are supported by their supplied proofs and the internal material in Sections 1–7, including Lemma 2.A. The audit found no missing specialized external theorem, circular source identification, unsupported transfer from fixed words to continuous flow, failure at singular Gram matrices, missing trace-norm tail control, or unsupported finite-time continuation step.

This verdict applies to the precise hypotheses, initializations, restart domains, limits, and observables stated in the files. In particular, it does not promote the additions to an arbitrary-data theorem, a GD theorem, a depth-uniform theorem, a global spectral theorem for arbitrary initial fields, or an all-depth fitting theorem.

## Isolation, input identity, and complete read coverage

Only these two source files were read:

| Input | Bytes | Lines | SHA-256 |
| --- | ---: | ---: | --- |
| `/tmp/pde-exact-capture-round2.ZYka2DDA/PROOF.md` | 104459 | 2634 | `c17c6adeb1c728e614b0b1e5d67706d9462223559182057134d56462e707d6ae` |
| `/tmp/pde-exact-capture-round2.ZYka2DDA/NOTATION.md` | 5110 | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

The main reviewer read NOTATION.md lines 1–98, fully to EOF, and PROOF.md in consecutive, nontruncated ranges 1–420, 421–840, 841–1260, 1261–1680, 1681–2100, 2101–2520, and 2521–2634, fully to EOF. The last proof line is the sentence ending “is not used as a continuous-time theorem.” The last notation line ends “finite-dimensional scalar state.” Every displayed equation, theorem, proof paragraph, scope qualification, and intervening passage was included.

No project files, history, study notes, previous reviews, skills, internet sources, other agents, or research computations were used. The references to `gaussian_calculus.md` at proof lines 1651 and 2633 were not followed. The relevant Wick argument is already contained in the input; the final reference expressly disclaims a continuous-time application of that other file.

Administrative operations were limited to reading/counting/hashing these inputs, creating a fresh directory with `mktemp -d`, writing this report with `apply_patch`, and checking output existence and permissions. The inputs were not edited. This report resides in the newly created private directory `/tmp/pde-proof-review.EfY4RBpX`; its directory permissions were verified as 0700. Both input SHA-256 hashes were recomputed after the report was written and exactly matched the values above.

All line references below refer to the supplied PROOF.md unless explicitly labeled NOTATION.md. Checks and explanatory derivations below are the reviewer's mathematical reasoning from the two inputs, not numerical experiments.

## Claim boundaries that were actually audited

| Result | Model and initialization | Positive conclusion | Boundary |
| --- | --- | --- | --- |
| Theorem 1, Sections 1–4 | One scalar datum, three hidden linear layers, order-one stored endpoint/readout coordinates | Global cyclic population; compact-time GF and exact-GD limits; named rooted observables; population fitting | GD requires a deterministic step tending to zero; no growing-horizon width limit or neuron-coordinate law |
| Theorem 4, Sections 5–6 | All current states in the stated open-state or zero-neighborhood classes | No uniform bounded-contraction polynomial/analytic scalar or local finite-order PDE closure | Does not prohibit arbitrary field encoders or a realization of just one initialized trajectory |
| Section 7 | The same finite linear dynamics | Local feature-flow profile and global physical-flow transport realization | The encoder can store the entire output trajectory and is outside the bounded-contraction class |
| Theorem EC8 | One scalar datum, one hidden nonlinear layer, stated C² activation bounds, order-one stored readout | Global marked characteristic population; compact-time GF scalar and block-energy limits; almost-sure versions under the specified nested coupling | No general fitting claim or empirical path-law claim; restart uses the full consistent marked state |
| Lemma EC9 | A separately fixed finite number of independent Gaussian matrix labels and two Gaussian roots | Fixed rooted Gram convergence and a high-probability operator-norm bound | No growing/adaptive word theorem or sharp spectral-edge result |
| Theorem EC10 | One scalar datum, every separately fixed linear hidden depth, order-one stored readout | Global GF population; named fixed programs, finite-rank signatures, increment trace norms, fixed singular values, and uniform trace-tail tightness | No depth-uniform estimates, GD extension, coordinate laws, or all-depth fitting conclusion |
| Theorem EC11 | Two hidden linear layers and one exactly unit-normalized datum | Canonical global physical spectral solution, scalar/block-energy limits, and exponential population residual decay | Restart is along the initialized spectral solution; this is not a claim for every spectral triple or for all rooted operator observables |
| Section 12 | Common cases of the preceding models | Agreement of the overlapping deterministic readouts | Does not identify different readout initializations or enlarge any observable or time-horizon scope |

The restrictions are mathematically substantive. In particular, the kernel of the spectral system need not be nonnegative at an arbitrary L² field pair, so the canonical initialization and its invariant estimates cannot be discarded.

## 1. Notation and normalization audit

NOTATION.md was checked against every model change. Its finite normalization is prediction `readoutᵀ hidden / n`, first-layer input normalization `x / sqrt(d)`, ordinary Euclidean/operator norms, and a residual `f-y` that is separate from backpropagation. A rank-one Hilbert operator is `v ⊗ w: z ↦ v⟨w,z⟩`; in normalized neuron coordinates its representative is an outer product divided by n.

The chapter explicitly overrides the small-readout convention with stored readout variance one in Sections 1, 8, 10, and 11. Normalizing the endpoint representatives by sqrt(n) changes their entry variance to 1/n without changing the stored-weight initialization. Equal limiting initial predictions do not identify those two initialization regimes.

The factor `-2κr` is correct for full squared loss. In Sections 1 and 10, endpoint mobilities nκ and middle-matrix mobility κ produce the same normalized factor equations because the endpoint gradients contain the prediction's 1/n normalization. There is no extra n in the normalized rank-one middle update. The kernels omit κ; physical residual decay is consequently `ṙ=-2κrK`, and squared-loss decay is `-4κr²K`.

Section 8 instead has two coordinate fields, both stored at order one and both trained with mobility nκ. Its kernel is the ordinary sample average of the two squared feature derivatives. That is consistent with its different, shallow representation.

For Section 11, the initial vector `W^(1)x/sqrt(dn)` has independent N(0,1/n) entries because `||x||²/d=1`. Projecting the first-layer update onto x introduces exactly `xᵀx/d=1`; components orthogonal to x are constant. The equivalent raw middle matrix `mathsf A=sqrt(n)B` has mobility nκ because changing variables multiplies its mobility by n. The expression with three raw factors and prefactor n^(-3/2) is correct. This is a one-input projection, not a multiple-sample whitening argument.

There is no incompatible use of feature time as physical time. Section 8 constructs characteristics for both signs of feature time and then solves a scalar physical clock. Sections 10 and 11 prove continuation directly in physical time. The separate exact-GD proof in Section 4 treats residuals as recomputed readouts, as required by NOTATION.md.

## 2. Sections 1–2: cyclic algebra and Gaussian source

### Cyclic equations and rank bounds: lines 13–194

The four normalized factor derivatives in (2.1) follow from (1.2). On the scalar-plus-three-layer direct sum, cubing the transpose cyclic operator has precisely the four original cyclic block positions and the four feature derivatives. A length-three cyclic path necessarily passes through one of the scalar endpoint blocks. Thus every such block has rank at most one, and the full cube has rank at most four. These facts hold for bounded Hilbert operators as well as finite matrices.

Each diagonal block of the fourth power has trace `vᵀRBu`; the rank-one trace formula therefore gives `Tr(C⁴)/4=f`. Differentiating f with respect to all four factors produces exactly the four nonnegative terms in (1.4). Consequently `K=||C*³||HS²=Tr(C³C*³)`. The normalizations in the examples following (1.4) agree with the unnormalized hidden vectors.

### Word-space realization and fixed Gaussian words: lines 196–367

The left creation maps have norm one and their specified deletion maps are their actual adjoints. Hence the middle sources have norm at most two. Matrix-letter words cannot remove or change the final root letter 5 or 6. Each rooted sector has the vacuum inner products, and all cross-sector rooted inner products vanish. This is enough to establish (2.7); orthogonality of only the initial root vectors would not have sufficed.

The Wick proof correctly treats real, nonsymmetric Gaussian matrices. A paired raw entry identifies both its row indices and its column indices, with transpose markers determining the walk orientation. For a normalized trace word of length 2q, the quotient graph is connected and the contribution is `n^(v-q-1)`. A connected graph with q edges has at most q+1 vertices. Equality forces a tree, and a closed tree walk using each edge twice crosses that edge once in each direction. This forces opposite transpose markers in each surviving pair. Leaf removal gives noncrossing pairings, and the reverse adjacent-pair insertion proves sufficiency, including the number of free indices.

Expanding the explicit creation/annihilation words gives exactly those pairings, each with coefficient one. Odd moments vanish. In the two-trace variance calculation, disconnected pairings cancel, while any joining pairing gives one connected quotient graph and contributes at most O(1/n) after the two normalizations. This proves the stated fixed-word L² limit without invoking a free-probability representation theorem.

The 1/4-net cardinality `9^n`, bilinear approximation factor 2, and Gaussian tail threshold 6 give `2·81^n exp(-18n)` for the norm threshold 12. Squared norms of the normalized Gaussian endpoints have mean one and variance 2/n. These imply the joint bounded-norm event.

For independent Gaussian roots, the conditional quadratic-form variance is at most `2||T||²/n`, and the mixed-root second moment is at most `||T||²/n`. Conditioning on a matrix-measurable norm event is legitimate; it avoids requiring a uniform bound on all source outcomes. Applying these facts to `T=P_iᵀP_j`, and then a finite union, proves the rooted Gram statement. No degree is allowed to grow with n.

Finally, each of the four initial fields entering K is a single norm-one word. The zero cross-root prediction and these four norms give `f(0)=0` and `K(0)=4`. The block source norm is at most two because different input summands map into different output summands.

## 3. Lemma 2.A: complete foundational operator audit

Lines 369–549 contain the compact-operator and trace-norm results required later. The following checks found no foundational gap.

1. **Weak subsequence construction.** A coordinatewise diagonal subsequence of a bounded sequence defines a Hilbert vector: every finite sum of limiting coordinate squares is bounded by the common squared norm. Approximation of a fixed test vector by finite-coordinate vectors upgrades coordinate convergence to weak convergence. This works in finite dimension and for complex coordinates as well.

2. **Attainment of the compact operator norm.** A maximizing unit sequence has a weakly convergent subsequence and, by compactness, a further subsequence whose images converge in norm. Testing with the adjoint identifies the image limit with Tv. The weak limit has norm at most one; if its norm were smaller than one, rescaling would contradict norm maximality. The maximizing vector is therefore a unit vector.

3. **Singular directions.** Differentiating the normalized Rayleigh quotient in directions perpendicular to v gives `T*Tv=||T||²v`; in the complex case imaginary variations supply the remaining components. The restriction to the input orthogonal complement maps into the corresponding output orthogonal complement. Recursive restriction therefore produces orthonormal singular lists in both spaces.

4. **Exhaustion and convergence.** If the successive nonzero singular values failed to tend to zero, the images of the orthonormal right singular vectors would have a uniformly positive pairwise separation, contradicting compactness. The remainder norm is precisely the next restriction norm. Thus the displayed singular expansion converges in operator norm and leaves no undisclosed residual action on a complementary subspace.

5. **Best finite-rank approximation.** Truncation proves one inequality in (2.A.2). For rank below j, the kernel of the approximating map intersects the span of the first j right singular vectors; a unit vector there proves the reverse inequality. Zero-padded and terminating lists cause no exception. Applying the infimum formula in both directions gives operator-norm Lipschitz continuity of each ordered singular value.

6. **Partial-sum variational formula.** For orthonormal test lists of length m, the expansion coefficients satisfy `|c_j|≤1` and `sum_j |c_j|≤m`, by two applications of Cauchy–Schwarz/Bessel. Their absolute weighted sum is therefore bounded by the first m singular values. The series is absolutely convergent even if T is not trace class. Choosing singular vectors attains the bound; if the singular list terminates early, orthonormal completion contributes zero. This proves (2.A.4), including the finite-dimensional case.

7. **Trace-norm triangle inequality.** The variational partial sums obey the triangle inequality. Increasing m to the available dimension, or to infinity, proves the trace-norm triangle inequality. Homogeneity and definiteness follow directly from the singular expansion. Compactness is preserved under the sums used here: finite singular truncations approximate the sum in operator norm, and the stated finite-net argument proves operator-norm closure of compact operators without using trace-norm completeness.

8. **Trace-norm completeness.** A trace-norm Cauchy sequence is operator-norm Cauchy. Its limit is a bounded compact operator. For fixed m, convergence of the first m singular values of `T_k-T_n` gives the corresponding bound for `T-T_n`; increasing m proves `||T-T_n||1≤ε`. This establishes trace-class membership and convergence, rather than assuming them from operator-norm convergence. The argument is not circular.

9. **Finite-rank density and ideal operations.** The remainder of a singular expansion has exactly the remaining singular values, so its trace norm is the summable tail. Bounded left and right multiplication of each singular rank-one term yields a trace-norm summable series. Completeness supplies its limit, and operator-norm convergence identifies that limit with ATB. Thus (2.A.3) holds for rectangular compatible spaces as used in Section 10. Taking adjoints of the singular expansion also preserves singular values and trace norm.

10. **Trace and cyclicity.** The basis-diagonal series is absolutely summable by Cauchy–Schwarz and Parseval. Exchanging the basis and singular sums gives `sum_j s_j⟨v_j,u_j⟩`, proving basis independence. The basis definition gives linearity; the same bound gives trace-norm continuity. Termwise evaluation of rank-one traces then proves `Tr(AT)=Tr(TA)` for bounded A. No trace of an unrestricted non-trace-class source is used.

11. **Hilbert–Schmidt identities.** Parseval identifies the squared column norm with `sum_j s_j²`. Its triangle and Cauchy–Schwarz inequalities follow from the Hilbert norm of that column list. The bound by the trace norm follows from the scalar sequence inequality. For rank at most four, the reverse estimate `||T||1≤2||T||HS` is the finite four-term Cauchy–Schwarz inequality.

12. **Singular Gram matrices.** The map `(V*V)^(1/2)x ↦ Vx` is well-defined and isometric on its support, including when the Gram matrix has a kernel. The coefficient matrix in (2.A.5) vanishes on the input kernel and has output in the output support. Partial isometries therefore preserve exactly its nonzero singular values. Bounded positive square roots have convergent subsequences in finite dimension, and uniqueness of the positive square root identifies every subsequential limit. This proves continuity at rank loss without any inverse or pseudoinverse.

13. **Full trace tails.** If R has rank at most m, adjoining R to a rank-below-j approximation of `T-R` gives `s_(j+m)(T)≤s_j(T-R)`. Summing this inequality proves (2.A.6). This controls the entire nuclear tail, not just finitely many singular values or an operator-norm remainder.

Finite-dimensional diagonalization, elementary Hilbert-space facts, and continuous integration in a complete normed space are sufficient for the remaining uses. An infinite-dimensional spectral theorem, an external Schatten-ideal theorem, or an unproved Banach-space completion is not required.

## 4. Sections 3–4: global cyclic flow, fitting, width limit, and GD

### Local closure and physical continuation: lines 551–682

The cyclic support subspace is closed in trace norm: each block compression is continuous by the ideal inequality. Its affine source space retains the cyclic form. The adjoint cube has the correct support and rank bound, so the vector field takes values in that same Banach space.

The noncommuting telescoping identity is correct. It gives the cubic difference bound `3A²||Q-Qtilde||1`; the fourth-power trace gives `A³||Q-Qtilde||1`; and the two rank-four Hilbert–Schmidt bounds give the kernel constant `12A⁵`. The estimates `|f|≤A⁴`, `K≤4A⁶`, and `||C*³||1≤4A³` follow from the same finite-rank bounds. Thus the field is bounded and Lipschitz on each relevant ball with no dimension factor.

The path integral contraction is legitimate because Lemma 2.A supplies a complete trace-norm state space. All differentiated fourth-power terms contain the trace-class velocity; telescoping differentiability and cyclicity justify `ḟ=Tr(C³Q̇)`. This proves the residual and loss identities.

The energy inequality is correctly normalized:

`integral_0^T r²K ≤ r(0)²/(4κ)` and
`integral_0^T ||Q̇||1 ≤ 4κ sqrt(T) sqrt(integral_0^T r²K) ≤ 2|r(0)|sqrt(κT)`.

A finite maximal time therefore bounds the state in a trace-norm ball; bounded velocity gives a norm limit at that time, and local existence extends it. This argument uses completeness, not compactness of bounded infinite-dimensional balls. It proves global forward existence at every cyclic trace-class restart and every finite initial state.

### Fitting: lines 684–726

The product derivatives of `z=Bu` and `p=R*v` have the stated positive-operator form. Both endpoint squared norms have derivative `-4κrf` and start at one. The exact scalar residual formula makes `rf≤0` for either sign of y, so those equal norms remain at least one. Consequently `K≥||z||²+||p||²≥2|f|`.

Since `K(0)=4`, `ḟ(0)=8κy`, giving a nonzero prediction for a positive time when y is nonzero. The residual formula makes |f| nondecreasing thereafter, and the displayed exponential bound follows. For y=0, uniqueness gives the stationary initialized state. This fitting proof is specific to the stated depth-three construction and is not used as an all-depth estimate.

### Fixed-word-to-flow transfer: lines 728–845

The common high-probability initial norm/residual event and the physical energy bound give a deterministic trace-norm radius through T+1. The cutoff is evaluated on Q, the evolving increment, and leaves a unit margin beyond that radius. Inside its support the ball estimates apply; across the support boundary the Lipschitz vanishing cutoff controls the product. Hence there is one bounded, globally Lipschitz cutoff field in each dimension, with common constants.

At each fixed Picard order, the initial source cube is finite rank. Applying a source appends a letter, and multiplying two finite-rank factors contracts a pair of source words. Integration changes coefficients only. Thus every iterate has a finite word list independent of n and time. Its scalar coefficients, including the cutoff, depend continuously on finitely many initial Grams. The singular-Gram formula provides the needed trace-norm continuity even when limiting roots or words are linearly dependent.

Uniform-in-time continuity follows by induction on the coefficient paths and the bounded norm of integration in the supremum topology. The factorial error estimate (4.5) is the sum of the successive Picard increments `M H^(h-1)t^h/h!`. The error tends to zero uniformly in dimension. Choosing the iteration order before taking the width limit is therefore valid; no adaptive or growing-word result is being smuggled into the continuous-time claim.

Current fixed rooted words telescope on the common ball. Endpoint changes are controlled in Hilbert norm and matrix changes in operator norm by the trace-norm increment error. Pairings, finite-rank contractions, and the stated Schatten norms follow by the same argument and finite Gram continuity. This proves exactly the observables in Theorem 1 without comparing operators on different ambient spaces.

### Exact GD: lines 847–899

The simultaneous stored-weight update becomes Euler for Q under the linear normalization map. The residual in (4.6) is recomputed from the new state at each mesh point. It is not separately Euler-updated using a differential product-rule identity.

Integrating the Lipschitz velocity gives the one-step defect `HMh²/2`. The geometric error recurrence yields (4.8); the H=0 case is correctly separated. Linear interpolation adds an O(h) error with dimension-independent constant. For small enough h the cutoff nodes stay within the unit margin, so induction identifies cutoff Euler with the actual GD updates. The extra horizon covers the interval intersecting T. The probability of the excluded source event vanishes, and no width/step relation beyond `eta_n→0` is required.

This is a valid preexisting L=3 GD theorem. The new Sections 8–12 do not inherit a GD conclusion merely by analogy.

## 5. Sections 5–7: nonclosure and unrestricted realizations

### Encoder class and stable independence: lines 901–1052

The finite tensor alphabet, degree bound, and paired typed slots give a finite graph list at fixed degree. Products correspond to disjoint unions. Width-dependent encoder coefficients accommodate the endpoint normalization but do not enlarge the finite connected graph alphabet.

The stable-independence proof correctly enlarges the auxiliary class to incidence networks with higher-valence index vertices when taking quotients. An injectively labeled monomial records all tensor types and their typed incident indices; distinct auxiliary graph types have disjoint monomial supports. Commuting entries forget only the permutation of identical tensor copies, already part of the graph isomorphism. Excluding isolated index vertices removes otherwise invisible factors of n.

A graph with maximal index-vertex count in a purported finite linear relation contributes its own injective type through the discrete partition. A nontrivial quotient has fewer vertices, so that coefficient cannot cancel. This proves independence for sufficiently large width, with no claim at every fixed width.

### Derivative obstruction: lines 1054–1239

For the endpoint-only derivation, `D0 U_j=X_j+Y_j` and `D0 X_j=D0 Y_j=2U_(j+1)` follow from `A H^j A*=(AA*)^(j+1)`. Iteration gives the coefficient `4^(j-1)` in (6.5). All tensor replacements in the full feature field have nonnegative graph coefficients, so those histories survive with at least that coefficient in the full derivative. The path `u*(B*R*RB)^j u` is connected and has degree `4j+2`.

All spatial derivatives of the encoder retain the same graph alphabet. Finite prolongation of the PDE uses the correct total spatial derivative, commutes with the state derivation, and yields (6.10). The highest jet order is at most `rho+k sigma`. For each fixed derivative order only finitely many graph types occur, independently of width-dependent coefficient values.

Polynomial identities on an open state set extend to polynomial identities everywhere. In the analytic variant, recentering at the actual zero-state jet removes the empty-graph constant and gives positive order in the common scaling parameter. Every fixed Taylor coefficient then uses only finitely many products from the connected alphabet. The stipulated mixed smoothness supplies the derivatives needed for that finite coefficient comparison. No expansion at an incorrect zero jet, uniform analytic radius across widths, or infinite Taylor summation is needed.

The feature derivative raises tensor degree by two, yielding the forbidden connected coefficient in degree `4j+2`. For physical flow with nonzero y, the lowest-degree term in the k-th derivative is `(2κy)^k D^k f`, because the other summand raises degree by six. For y=0, the recurrence `P_(k+1)=f D P_k` preserves nonnegative coefficients and retains `f^k D^k f`; the resulting disconnected graph still contains the forbidden connected component. The degree `4+6k` is correct. Stable independence completes all three contradictions.

The stationary initialized population at y=0 is not a counterexample to this result: the theorem concerns an open set of current states.

### Transport profile and finite examples: lines 1241–1348

The local feature-flow integral contraction has field bound `8 epsilon³`, Lipschitz constant `12 epsilon²`, and time radius `1/(24 epsilon²)`, giving contraction constant at most 1/2 and image norm below `2 epsilon`. Its flow identity produces the transport equation and its jets are the iterated feature derivatives. The unbounded connected graph degrees show why that encoder cannot belong to the bounded-degree class.

The physical flow is globally forward complete by Section 3. Its future-output profile is therefore defined on the fixed half-line. Right translation is a continuous forward semigroup in the compact-open topology, and the characteristic `tau ↦ (t-tau,s+tau)` proves the unique classical transport formula. It reaches the initial line and needs no inflow datum at s=0. The semigroup interpretation for continuous profiles is consistent.

For the width-one examples, the characteristic polynomial depends on the product and is `lambda⁴-1` in both states. The kernel values are 4 and `1/4+1+1+4=25/4`, so the stated distinction of feature velocities, and physical velocities when y≠1, is correct. Differentiating the four squared scalar factors gives `D a=D b=D c=D d0=2f`; differentiating their product output gives the four triple products in (7.7). This is a legitimate fixed-width scalar closure and does not violate a theorem requiring all sufficiently large widths.

## 6. Section 8: shallow characteristic population

Lines 1350–1563 were checked in full, including the nonlinear regularity assumptions, moment estimates, uniqueness, restart, and empirical-to-physical-time transfer.

**Finite equations.** Differentiating the average `a_i phi(u_i)` with the two nκ mobilities gives (EC8.2). Its kernel is the sum of the two nonnegative block energies. No normalization of `E phi(G)²` is used.

**Characteristic existence for both signs.** The field `(phi(U), A phi'(U))` is locally Lipschitz under (EC8.1). Its magnitude is bounded by a constant times `1+|A|+|U|`, even though its Jacobian need not be globally bounded. Integral Grönwall gives (EC8.7). Applying the same argument to the reversed field proves negative-time existence too. The bound prevents escape in the finite-dimensional characteristic equation.

**Expectation and derivatives.** The prediction integrand and H have quadratic envelopes in `J=1+|a0|+|u0|`. Their derivatives are correctly computed:

`d_s(A phi(U)) = phi(U)²+A² phi'(U)²`,

`d_s H = 4A phi(U) phi'(U)² + 2A³ phi'(U)² phi''(U)`.

The latter is bounded on compact feature intervals by `C_S J³`. The separate block derivatives displayed at lines 1506–1508 have the same envelope. Gaussian moments justify differentiation under expectation and continuity of K, and give `F(0)=0` by independence and centering of a0. Bounded phi'' and C² regularity suffice; no third activation derivative is needed.

**Physical clock and consistency.** The scalar equation has locally Lipschitz right-hand side because F is C¹. Differentiating `F(s(t))-y` gives the residual equation and its exponential solution. Thus `|s(t)|≤2κ|y|t`, whether or not F ever takes the value y. This excludes finite-time escape of the clock. Composing characteristics with it yields all finite moments on compact physical intervals and `f=y+r`.

**Uniqueness and restart.** For a classical marked solution, the integrated scalar coefficient identifies each mark with its unique characteristic at the same clock, including a stationary or nonmonotone clock. Differentiation under expectation preserves consistency and forces the same scalar clock equation. The argument starts from an arbitrary consistent marked pair having every finite moment, with J replaced by `1+|A_*|+|U_*|` and the residual bound by |r_*|. It does not claim that `(f,K,r)` alone determines a restart.

**Almost-sure uniform empirical convergence.** The fourth-moment expansion (EC8.12) has the correct diagonal and paired terms. Its O(n^-2) tail is summable, giving almost-sure convergence of each average. The same argument applies to the random Lipschitz envelope because all its required Gaussian moments are finite. A countable collection of finite rational nets plus (EC8.13) proves uniform convergence on compact feature intervals of the prediction and both kernel summands. The two limits are taken in the valid order: width first at a fixed net, then net refinement.

**Finite physical clocks.** The finite flow uses its true initial residual `F_n(0)-y`. Since `F_n'=K_n≥0`, its clock has the bound in lines 1541–1545 and is global. Both clocks lie eventually in the same deterministic compact feature interval. Subtracting the scalar integral equations using the Lipschitz constant of the deterministic F gives (EC8.14). The uniform empirical limits and uniform continuity of the limiting readouts can then be evaluated at the converging clocks. This proves every term of (EC8.5) and both block-energy limits. The argument also covers κ=0, with clocks identically zero.

The almost-sure assertion is correctly attached to the nested iid coupling; the intrinsic result is convergence in probability. Degenerate activations are allowed and do not create a contradiction because the theorem does not assert fitting for all such activations.

## 7. Section 9: the general fixed-label Gaussian source

Lines 1565–1724 reproduce and extend the contained Gaussian argument without requiring another source.

The q=0 case gives `F_q=R Omega` and two orthogonal roots in `R²`; empty operator maxima and products have the stated conventions. For q>0, creation/deletion maps have the indicated norm and adjoint relation. Taking two full direct-sum copies ensures the entire generated root sectors are orthogonal, not merely their first vectors.

The Gaussian tail/net constants, vector norm estimate, Wick quotient count, tree characterization, annihilation matching, and connected two-trace variance argument are the same valid calculations checked in Section 2. The variance equality for a possibly nonsymmetric T uses its symmetric part and is correct. In the independent-root case the exact second moment is `||T||HS²/n²`. All conditioning events used with these formulas are measurable from the matrices alone.

Linearity gives fixed polynomial trace tests, and taking a finite union gives joint fixed rooted Gram convergence. Typed compatible words are a subset of the proved word identities. The use of a separately fixed q justifies all finite unions and constants. No norm convergence to the sharp edge two, adaptive program theorem, or convergence of operators themselves is asserted or needed.

## 8. Section 10: every separately fixed linear depth

### Equations, source, and global state: lines 1726–1910

The forward/backward indexing is consistent: `x_(ell+1)=B_ell x_ell`, `b_ell=B_ell* b_(ell+1)`, and a matrix update is `-2κr b_(ell+1)⊗x_ell`. The normalized vectors are exactly the original forward/backward vectors divided by sqrt(n). Empty products at L=1 give the two-endpoint system without introducing a nonexistent matrix block.

With q=L-1 in EC9, each initial forward or backward chain successively uses distinct labels. Its annihilation alternatives vanish at each step, leaving a single norm-one word. Cross-root sectors give f(0)=0. Thus the two endpoint kernel summands and the L-1 middle summands are all one, giving K(0)=L+1.

The product state is a Banach space by Hilbert completeness and Lemma 2.A for every rectangular trace-class component. On a state ball all current source-plus-increment operators are uniformly bounded. Telescoping products and the rank-one difference bound prove local Lipschitz continuity in exactly the stated state norm. The constants may depend on L; this is consistent with the theorem.

Inserting each block velocity into the prediction produces its corresponding square in K. Thus `ḟ=ṙ`, and the initialized consistency relation is preserved. The scalar equation makes `|r|` nonincreasing. For every block, its feature speed squared is a kernel summand. The middle feature velocity is rank one, so its Hilbert–Schmidt and trace norms agree. Cauchy–Schwarz yields the bound `integral ||theta_dot|| ≤ |r(0)|sqrt(κT)` for each of the L+1 blocks. Summing their lengths and adding the bounded residual controls the full state on every finite horizon.

Bounded velocity on the resulting ball supplies a norm limit at a hypothetical finite maximal time. The local contraction then extends the solution. This proves the stated global existence and consistent full-state restart with the same source. The finite system starts at `f_n(0)-y`, as the proof explicitly retains.

### Flow transfer and observable scope: lines 1912–2014

The deterministic radius (EC10.11) allows initial endpoint norms at most two each, L+1 block displacements, and residual at most |y|+1. Its cutoff has a uniform margin and is globally bounded and Lipschitz by the same inside/boundary argument as Section 4.

At fixed Picard order, endpoints are finite linear combinations of initial rooted words, increments are finite sums of rank-one maps between such words, and r is a scalar continuous function of finitely many initial Grams. The initial r itself is such a function. Source application, rank-one multiplication, kernel evaluation, and integration preserve this description. The state-norm cutoff introduces continuous finite-Gram operations, including square roots and trace norms, but no Gram inverses.

Continuity is uniform in time on a compact initial-Gram neighborhood. The factorial bound (EC10.13) is dimension independent on the source event. In the three-term inequality (EC10.14), each outer difference is estimated within its own state space, while the middle difference compares numerical descriptions from EC9. This is a valid fixed-word-to-flow transfer and does not subtract vectors or operators from different width spaces.

Every fixed rooted program specified in the theorem uses finitely many sums, scalar products, operator/adjoint applications, and pairings. These operations are polynomial and Lipschitz on the common bounded state set. Each finite-rank signature formed from a fixed list is controlled by its finite matrix representation. Increment trace norms are 1-Lipschitz in trace norm, and each singular value is 1-Lipschitz in operator norm. Consequently all the named uniform scalar, finite-rank, trace-norm, and fixed-singular-value conclusions follow from the same transfer. Fixed best-rank tails are also differences of those already controlled quantities.

### Uniform operator trace tails: lines 2016–2040

The state velocity is bounded on the actual trajectory ball, so the state is time-Lipschitz. Composing it with the locally Lipschitz block vector field makes `h_ell,n=P_dot_ell,n` uniformly Lipschitz in trace norm. Every h is rank at most one.

A left Riemann sum on N cells, with the last partial cell included, therefore has rank at most N+1 and uniform trace-norm error at most `C_T T²/(2N)`. The estimate follows by integrating `C_T(v-t_k)` on each full or partial cell. Summing the best-rank inequality from Lemma 2.A converts that trace-norm error to a bound on the full singular-value tail. The harmless N versus N+1 shift disappears in the tail limit.

The constants are deterministic on an event of probability tending to one. First selecting N and then removing the event gives precisely the order of limits in (EC10.7). The same construction works for the limiting increment. This establishes tail tightness rather than assuming it from convergence of individual singular values. For L=1 the empty maximum is zero, so there is no exceptional case.

There is no assertion here of all-depth fitting. Global existence and compact-time approximation do not themselves imply that assertion, and the theorem does not make it.

## 9. Section 11: two-layer spectral source and physical dynamics

### Exact finite reduction: lines 2042–2240

The one-datum projection and alternate raw normalization were checked above. The constants of motion are correct: the two product-rule terms in `(BB*)_dot` cancel those in `(aa*)_dot`, and the two endpoint squared norms have the same derivative. Thus `C=BB*-aa*` and `delta=||a||²-||u||²` are fixed even when the residual vanishes.

For `v=Bu` and `q=||a||²`, direct differentiation gives

`a_dot=g v`,
`v_dot=g[(BB*)a+||u||²a]=g[C+(2q-delta)I]a`.

Differentiating `a*v` gives the kernel in (EC11.10), including the term `q(q-delta)=||a||²||u||²`. This is a nonnegative finite-network kernel. The derivation does not divide by g or invert a clock.

The matrix-valued spectral measure is positive because each quadratic form in its two coefficients is a spectral mass of a real vector combination. Finite-dimensional diagonalization suffices for the mode representation. With coefficients q and g from the finite solution, each mode solves a linear equation; applying the finite functional calculus reproduces the reduced vectors. Conversely, the self-consistent mode equations reproduce the same locally unique reduced system. The finite network's global physical existence is supplied by the already proved block-energy estimate. Thus the reduction introduces no missing finite-width existence premise.

### Base density and transform: lines 2242–2333

For the alternating word `(BB*)^k`, every noncrossing pairing pairs opposite parity positions and hence opposite transpose markers. The first-pair decomposition gives the Catalan recursion. The moment integral of rho0, after lambda=4t, has the coefficient `4^(k+1)/(2pi)` and the beta-type integral shown in (EC11.16). The base value pi/2 and the integration-by-parts ratio `(k+1/2)/(k+2)` give `(2k)!/[k!(k+1)!]`. Solving the formal recursion yields the same coefficients.

The event `||B||≤12` bounds the spectrum of M in [0,144]. Bernstein polynomial approximation is justified by the binomial variance bound, with error equal to a modulus-of-continuity term plus `2||h||/(4N epsilon²)`. Thus moment convergence implies weak empirical convergence on this event; no sharp edge theorem is needed.

The transform is defined with the convention `(z-lambda)^(-1)`, so it is negative on the negative real axis. Its formula

`m(z)=(1-sqrt(1-4/z))/2`, with `z m(z)(1-m(z))=1`,

has the correct sign and large-|z| behavior. The explicit sine/tangent substitutions extend the formula to every negative real z. In particular m(-1/2)=-1. No analytic continuation or inversion theorem is needed for that step.

### Rank-one perturbation, including the negative atom: lines 2335–2391

Conditional quadratic-form concentration gives `h_n(z)=a*(z-M_n)^(-1)a → m(z)`. Since `z-C=z-M+aa*`, solving the rank-one linear system gives

`a*(z-C)^(-1)a = h_n(z)/(1+h_n(z))`.

On the norm event C≥-4I, so the formula is applied safely at z<-4, and the limiting denominator is nonzero there. This proves the correct perturbed rooted transform.

The proposed continuous part of rho_a is `lambda/(1+2lambda) rho0`. The value m(-1/2)=-1 gives `integral (1+2lambda)^(-1) rho0=1/2`, hence continuous mass 1/4. Adding the stated atom of mass 3/4 at -1/2 makes mass one.

The partial-fraction computation is correct:

`integral (z-lambda)^(-1) rho_a = 3/[4(z+1/2)] + [z m(z)-1/2]/(1+2z)`

`= [z m(z)+1]/(1+2z) = m(z)/(1+m(z))`.

The last equality follows algebraically from `z m(1-m)=1`. This checks both the atom and the continuous density without an unproved spectral inversion rule.

The transform-to-moment argument is also complete. All measures in question have bounded mass and support in J=[-4,144] on the norm event. After multiplying the expansion in (EC11.21) by z^(k+1), the k-th moment has coefficient one and the remainder is bounded by `mass·144^(k+1)/(|z|-144)`. For a given tolerance, first choose one sufficiently negative fixed z, then use transform convergence and already convergent lower moments. This proves convergence of the k-th moment by induction. Bernstein approximation then proves weak convergence. The argument does not interchange an uncontrolled limit in z with the width limit.

### Remaining matrix-measure entries and all source constants: lines 2393–2445

Conditioning on B and a leaves u independent Gaussian. The conditional quadratic form for `v* p(C)v` has the stated variance bound. Since `C-M=-aa*`, telescoping powers and the trace ideal bound give a trace-norm difference of order one for every fixed degree on the norm event. Multiplication by M and division by n therefore make its normalized trace contribution O(1/n). The limiting lower-right measure is `rho_v=lambda rho0`.

The cross term is conditionally centered in u and has variance O(1/n) with the exact norm factors in (EC11.24). Its total variation is at most `||a|| ||v||`, by spectral-partition Cauchy–Schwarz. The diagonal masses are also bounded. These total-variation bounds justify polynomial-to-continuous approximation for all four entries, including the signed cross entries. Thus the matrix measure really converges to the stated diagonal one.

The two endpoint norm laws give delta_n→0. Averaging the three independent Gaussian factors gives `E f_n(0)²=1/n`. The first moment of rho_a is zero: the continuous part contributes `1/2-1/4+1/8=3/8`, canceled by the atom's -3/8. Both diagonal measures have mass one. These facts give `q(0)=1`, `F(0)=0`, and `K(0)=1+0+2=3`.

The scalar source nu is the sum of the two measures and has mass two. Its density equals the sum of their displayed densities, and the listed alpha and beta satisfy `alpha² nu=rho_a`, `beta² nu=rho_v`, including at the atom. Their L² norms are each one. No probability-measure normalization is silently applied to nu.

### Global canonical spectral solution: lines 2447–2503

Multiplication by lambda is bounded on the explicit L² space, so all readouts and the vector field are locally Lipschitz real polynomial maps. The use of complex fields packages two real channels; all scalar readouts use the required real parts. Hilbert norm differentiation yields `F_dot=r_dot` and `q_dot=-4κrF` exactly.

The negative atom is explicitly accounted for by `K≥2q²-q/2`. Starting on the interval q>1/2 makes K positive. The residual equation gives `r=-y theta`, with `0<theta≤1`, and consistency gives `F=y(1-theta)`. Hence

`0≤q_dot=4κy² theta(1-theta)≤κy²`.

Starting at q=1, the solution cannot exit through q=1/2. On the entire maximal interval, q≥1, `q≤1+κy²t`, `|r|≤|y|`, and K≥3/2. This bootstrap avoids assuming nonnegative spectral energy on the whole ambient state space.

The bound on q controls psi. The displayed bound on pi_dot uses `||lambda||∞≤4`, the q bound, and the r bound. It bounds pi on every finite interval from its unit initial norm. The full state is therefore bounded, its velocity is bounded on that ball, and the norm-limit/local-extension argument proves global physical existence. The residual inequality integrates to `|r(t)|≤|y| exp(-3κt)`.

For r≠0, the residual velocity itself is nonzero because K≥3/2. For r=0 every velocity vanishes. At y=0 the initialized state is stationary. Restart of the current triple along this canonical solution follows from uniqueness. This proof does not need completeness of feature time and does not prove global existence or positivity from an arbitrary L² triple.

### Uniform finite-width identification and block energies: lines 2505–2593

The diagonal matrix source is encoded by

`psi=alpha c1+i beta c2`, `pi=alpha d1+i beta d2`.

The imaginary unit is essential to the elementary calculation: the real readouts then contain the two diagonal channel contributions and no cross terms. With the already constructed bounded q and r on [0,T], the real mode coefficients solve linear equations continuously on the full compact interval J. Their integral equations give uniform bounds and continuity in lambda and time. Linear uniqueness identifies the resulting encoded fields with the canonical L² solution.

For finite width the mode coefficients extend to all of J using the globally defined finite network coefficients. On the source event the spectral support lies in J, and the diagonal masses are bounded by 4 and 576; the signed entries have the corresponding variation bounds. Each limiting test-function family in (EC11.29) is compact in C(J), by joint continuity on J×[0,T]. Finite uniform nets and the common variation bound therefore upgrade entrywise weak convergence to the uniform-in-time deterministic test errors epsilon_n(T).

Before the mode/residual discrepancy reaches one, every mode lies in a common bounded ball. Expanding one mode factor at a time in the measure integrals proves (EC11.30); the additional delta term and the nonlinear q factor are included. The initial residual discrepancy is f_n(0), while the mode initial data agree exactly. Subtracting the integral equations yields (EC11.31). Integral Grönwall bounds the stopped discrepancy by a constant times `|f_n(0)|+epsilon_n(T)+|delta_n|`, which tends to zero in probability. Continuity rules out the first stopping time on the resulting high-probability event.

This proves all four scalar readouts in (EC11.7), and q convergence. The three separate block-energy formulas are correct: the middle one uses `BB*=C+aa*`, and the last uses the invariant endpoint norm difference. Their limits are `||pi||²`, `integral lambda|psi|²+q²`, and q², which sum to the specified K. Positivity along the canonical dynamics is consistent with these finite nonnegative block energies.

The argument uses finite-dimensional spectral resolution, elementary polynomial approximation, explicit resolvent algebra, and ODE estimates. No specialized random-matrix perturbation theorem, infinite-dimensional spectral representation theorem, or unproved measure inversion is necessary.

## 10. Section 12: exact overlap and limits of identification

Lines 2595–2634 were checked through EOF.

For L=1 and identity activation, solving the two characteristic equations gives the displayed hyperbolic formulas. Independent standard Gaussian marks have the same two-root covariance as the orthonormal Hilbert roots. Thus `F(s)=sinh(2s)` and `K(s)=2cosh(2s)` in both representations, with physical clock `s_dot=-2κ(sinh(2s)-y)`. The models coincide in their common mobility range. Section 8's extra nonlinear activations do not extend Section 10 to nonlinear depth.

At L=2 with x=1, the finite initialization, mobilities, residual convention, and scalar/block-energy readouts are identical in EC10 and EC11. Two deterministic compact-time limits of the same finite random readout must agree: if their uniform difference were positive, the triangle inequality would force one of the two errors against that finite readout to stay positive, contradicting convergence in probability. This identifies the named readouts without claiming recovery of every rooted operator signature from the spectral fields.

At L=3, the same argument identifies the common readouts of EC10 and Theorem 1. In addition, the direct-sum root sectors and the final-root-letter sectors have identical source Grams, with actual adjoints in both representations. The asserted rooted identification is consequently supported; there is no extra independent transpose source.

The final paragraph accurately retains order-one readout initialization, one datum, fixed depth, fixed compact physical horizons, and GF-only scope for the additions. It explicitly keeps the existing L=3 GD theorem separate and makes no all-depth fitting assertion.

## Adversarial issue disposition

| Candidate failure | Disposition |
| --- | --- |
| Trace-class ODE invoked before proving its state space complete | Resolved by Lemma 2.A's explicit singular expansion and trace-Cauchy argument |
| Hidden use of a specialized compact spectral/Schatten theorem | Not needed; the required compact singular expansion, norms, trace, ideals, and tails are proved |
| Independent transpose action in the Gaussian source | Not present; deletion maps are actual adjoints, and Wick orientations match them |
| Orthogonal roots but correlated generated sectors | Avoided by final root letters in Section 2 and full direct sums in Section 9 |
| Fixed-word limit applied directly to an adaptive flow | Avoided by finite Picard descriptions and a dimension-independent factorial error bound |
| Rank-deficient Gram limits break coefficient or norm continuity | Avoided by support partial isometries and positive square roots, with no inverse Gram |
| Singular values converge but nuclear mass escapes into an uncontrolled tail | Excluded by trace-norm approximation of the rank-one velocity integral and the summed best-rank inequality |
| Moment law assumes a sharp Gaussian spectral edge | Not needed; the elementary norm threshold 12 yields compact support sufficient for approximation |
| Perturbed source loses a negative atom or has wrong mass | Explicit transform computation verifies atom -1/2 with mass 3/4, continuous mass 1/4, and total scalar-source mass two |
| Transform convergence is promoted to weak convergence without justification | Justified by bounded-support remainder estimates, moment induction, and Bernstein approximation |
| Signed cross spectral measures lack tight total variation | Controlled by the spectral-partition bound `||a|| ||v||` |
| Spectral continuation assumes K≥0 on all L² states | Avoided by the canonical q bootstrap; restart scope is restricted accordingly |
| Finite-time continuation uses compactness of an infinite-dimensional ball | Not used; bounded velocity gives a Cauchy limit in a complete state space |
| Residual normalization drops a factor of n, two, or κ | All endpoint/matrix updates, kernels, energy bounds, and residual decay constants check |
| The L=3 exact-GD argument updates r as an independent Euler variable | Not present; the update evolves Q and recomputes the prediction/residual |
| New GF results silently claim raw-GD, arbitrary data, depth-uniform control, or all-depth fitting | Explicitly excluded; the proofs do not need any such extension |
| Spectral readouts claimed to determine all rooted operator observables | Explicitly excluded in Section 12 |

## Required corrections

**None.** No mathematical statement within the declared scope required correction in this review. The examined foundational arguments and transfer estimates close the particular gaps targeted by the request. The input's restrictions on initialization, data, depth, time horizon, restart state, and observable family must remain part of the statements.
