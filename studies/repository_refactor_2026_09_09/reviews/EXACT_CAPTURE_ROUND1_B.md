# Independent adversarial complete-proof review

## Verdict

**Qualified PASS.** I found no counterexample, incorrect normalization, invalid source identification, or substantive gap in the dynamical and width-limit arguments for the statements actually made in Sections 8–12. The dependencies in Sections 1–7 also survive the checks below. The qualifications on depth, data, initialization, restart states, time horizons, and convergence topology are essential and are respected.

There is one qualification to a *literal, wholly contained proof*: the infinite-dimensional trace-class arguments use the compact-operator singular-value decomposition and completeness of the trace-class norm without proving them. These are standard functional-analysis foundations, but they are not finite-dimensional elementary linear algebra. I flag them rather than silently treating them as proved by these inputs. Under the requested strict self-containment standard, add the foundational lemma described in R1 below; if these standard foundations are explicitly admitted, no mathematical correction to the stated conclusions is required. This is a minor foundational completion, not a defect in the Gaussian-source or dynamical arguments.

This verdict does not certify extensions to raw GD in Sections 8–12, multiple samples, arbitrary input Gram matrices, a depth growing with width, uniform-in-time finite-width approximation, arbitrary spectral initial states, or neuron-coordinate laws. None follows from this review.

## Inputs, hashes, and isolation

Only the following two supplied input files were read:

| Input | Lines | Bytes | SHA256 |
| --- | ---: | ---: | --- |
| `/tmp/pde-exact-capture-isolated.eYCeHCYW/PROOF.md` | 2452 | 94998 | `03a6ce55bda3e7c2eb27b1d80f53a081729137c1a4fce26bf42158733affee32` |
| `/tmp/pde-exact-capture-isolated.eYCeHCYW/NOTATION.md` | 98 | 5110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

Full-read coverage of `PROOF.md`: lines 1–240, 241–600, 601–960, 961–1320, 1321–1680, 1681–2040, and 2041–2452, including EOF. `NOTATION.md` was read from line 1 through its EOF at line 98. No output in these reads was truncated. Selected passages of the same proof were subsequently reread with line numbers for reference accuracy.

No project, history, prior-review, skill, or other source files were read. No network access, agents, numerical research, experiments, or tests were used. In particular, neither occurrence of `gaussian_calculus.md` was followed. No input was edited. Both input SHA256 values were recomputed after writing the report and remained identical to the values above. This report was created with `apply_patch` in the newly created private directory `/tmp/pde-proof-adversarial-review.Aunt2sGQ`, whose permissions were verified as `0700`.

All proof line references below refer to the hashed `PROOF.md`. Conclusions are based on algebra, estimates, and logical dependency checks, not passing tests or agreement with a prior summary.

## Required correction versus optional edits

### R1 — Required only for the literal contained-proof claim: supply the operator-ideal foundations

**Locations:** lines 371–395 and 437–443; the Banach-space construction around (EC10.5), (EC10.8), and lines 1683–1687; the singular-value argument at lines 1807–1813 and 1852–1858.

The proof uses the following infinite-dimensional facts:

1. A compact operator between the indicated separable Hilbert spaces has a singular-value expansion, with the usual rank truncations.
2. Operators with summable singular values form a complete normed space under their trace norm; finite-rank truncations converge in that norm.
3. The trace, ideal operations, and finite-rank singular-value formulas extend to that space as used in the text.

The text proves the relevant estimates *using* singular-value expansions and gives a proof of the approximation-number characterization once those expansions are available. It does not prove the expansions or trace-norm completeness. In particular, saying that Picard iterates are Cauchy in trace norm is insufficient by itself to place their limit in the proposed state space unless completeness has been admitted. Finite-dimensional SVD compactness in (4.4)/(EC10.12) does not supply this missing infinite-dimensional premise.

**Correction:** add a short preliminary lemma establishing these facts, or explicitly state that standard compact-operator and trace-class theory is part of the assumed foundations. The latter makes the scope of self-containment accurate; a literally contained proof requires the former. No initial law, equation, bound, or convergence claim needs changing.

This is a limited issue. A direct repair is available: obtain compact singular vectors successively by maximizing the quadratic form of the positive compact operator `T* T` on orthogonal complements; compactness forces the remaining singular values to tend to zero. Finite-dimensional trace-norm inequalities then extend along the resulting rank truncations. For completeness, take a trace-norm Cauchy sequence and a subsequence whose successive differences have summable trace norms. It converges in operator norm to a compact operator. The bounds on every finite singular-value sum, obtained by operator-norm continuity of those singular values, show that this limit has finite trace norm. Apply the same argument to each tail of the telescoping subsequence to obtain trace-norm convergence, and then to the original Cauchy sequence. This supplies exactly the foundational fact needed by the contraction and continuation arguments.

I do not classify elementary finite-dimensional spectral resolution, basic Gaussian integration, dominated convergence, or the elementary Hilbert-space inequalities as comparable unresolved research dependencies. The integral-contraction and Grönwall estimates used for the actual flows are explained in the document.

### No required corrections to the mathematical statements were found

Subject to the foundational qualification above, none of the audited theorems needs a changed factor of `n`, factor of two, source measure, initialization, parameter range, convergence mode, or restart domain. No claimed fitting result needs withdrawal. No additional relation between width and step size is needed for the already separate Section 4 GD theorem.

### Optional edits

- **Remove the incidental external pointer at line 1469.** The preceding moment-generating-function argument already proves Wick's identity. The pointer to `gaussian_calculus.md` is not a dependency, but deleting it would make an isolated reading easier to assess. The final reference at lines 2451–2452 expressly disclaims use of that other theorem and is harmless.
- **Clarify the meaning of “classical marked solution” in EC8.** State explicitly that the fields solve the characteristic equations almost everywhere in the mark, the scalar residual is continuously differentiable, and the stated moment bounds hold on compact time intervals. The existing characteristic representation provides precisely this solution and its uniqueness; this is a presentation improvement, not a missing estimate.
- **Make the spectral restart restriction prominent.** EC11 correctly promises restart along its initialized trajectory. Retaining that wording matters because positivity of its displayed `K` is not automatic on the entire ambient Hilbert space. A one-sentence reminder after the local-Lipschitz assertion would prevent an incorrect stronger reading.
- **Use finite Taylor expansions in the analytic nonclosure argument.** At each fixed tensor degree only a finite Taylor jet with remainder is needed. This avoids any suggestion that spatial differentiation requires a common radius of convergence for an infinite analytic series. The stipulated mixed smoothness already suffices for the finite-order argument.

## Coverage and dependency structure

| Part | Lines | Audit result |
| --- | --- | --- |
| Model and population statement, Section 1 | 13–143 | Stored-weight normalization, full loss, mobilities, and observables consistent |
| Cyclic algebra and Gaussian source, Section 2 | 144–368 | Block identities, rank bounds, Wick counting, norm bound, and root geometry checked |
| Global flow and fitting, Section 3 | 369–545 | Estimates and continuation valid, subject to R1 |
| Width limit and existing GD bridge, Section 4 | 546–718 | Cutoff, finite-word Picard transfer, and dimension-independent Euler argument valid |
| Closure class and obstruction, Sections 5–6 | 719–1058 | Graph independence, prolongation, and all label cases checked |
| Unrestricted encoders, Section 7 | 1059–1167 | Local feature transport and global physical transport have the stated scope |
| Shallow characteristics, Section 8 | 1168–1382 | Global physical marked solution and compact-time empirical readouts proved |
| Gaussian source, Section 9 | 1383–1543 | Contained random-matrix argument; fixed words and fixed label count only |
| Every separately fixed linear depth, Section 10 | 1544–1859 | Global operator state and scalar-observable transfer proved, subject to R1 |
| Two-layer spectral reduction, Section 11 | 1860–2412 | Exact finite reduction, explicit source, global canonical flow, and uniform identification checked |
| Agreements and limitations, Section 12 | 2413–2452 | Comparisons follow at their stated common observables and scope |

The principal dependencies are as follows. EC8 has its own characteristic and empirical-average proof. EC9 extends the contained Wick/net argument of Lemma 2. EC10 uses EC9 for initial rooted geometry and the trace-ideal framework for a Banach-space evolution; its passage from fixed words to continuous time is supplied by its own cutoff Picard argument. EC11 uses EC9 for source moments and concentration, EC10 for finite-network global existence, and its own direct Hilbert-space estimate for the global limiting spectral flow. Section 12 compares deterministic limits of the same finite observables. The graph nonclosure result and transport encoders are not used to infer any of the new width limits.

## Normalization and conventions audit

The stated models all use full squared loss for one sample. Writing a normalized endpoint as `u = W/sqrt(n)` does not change the stored initialization. For a normalized product prediction, full-loss gradient flow produces the common factor `-2 kappa r`; hence

`df/dt = -2 kappa r K`, and `d(r^2)/dt = -4 kappa r^2 K`.

The proofs keep `kappa` outside the unit-mobility kernel. They also keep physical time distinct from feature time. Only EC8 and the explicit shallow comparison need a characteristic clock; their clock is `ds/dt = -2 kappa r`, with no assumption that it is positive for every label.

In Sections 1 and 10 the stored endpoint entries have variance one, whereas the normalized endpoint vectors have entry variance `1/n`. Their ordinary Hilbert norms therefore have nonzero limits. The stored middle entries have variance `1/n`, and their operator norms are bounded with high probability; their Frobenius norms need not remain bounded. Population sources are bounded operators and are not falsely assumed trace class or Hilbert–Schmidt. Only trained increments occupy the trace-class state coordinates.

For EC8, both stored coordinates are initially independent standard Gaussians. Direct differentiation of `n^{-1} sum a_i phi(u_i)` with mobilities `n kappa` in both blocks gives exactly (EC8.2). There is no hidden normalization of `E phi(G)^2`.

For EC10, differentiation of a middle factor yields the finite outer product `b_{ell+1} x_ell^T` of the *normalized* vectors. In stored coordinates this is exactly `delta^{(ell+1)} (z^{(ell)})^T/n`, as stated. The two endpoint gradients supply the other two kernel terms. Empty products at `L=1` give the identity and no middle-block term.

For EC11 with a fixed normalized input, differentiating `W^(1) x/sqrt(d n)` introduces precisely `x^T x/d = 1`. Each projected initial row has variance `1/n`, and distinct rows remain independent at initialization. Components of the first matrix orthogonal to `x` have zero velocity. The equivalent raw middle matrix `sqrt(n) B` indeed has mobility `n kappa`, since its change of variables introduces the additional factor `n` in the mobility. This verifies the one-datum projection; it does not justify whitening or changing a multiple-sample Gram matrix.

The notation contract's small-readout convention is explicitly overridden in each relevant model. Equal limiting initial predictions cannot be used to transfer results between those regimes, and the proof does not do so.

## Sections 1–7: audit of explicit dependencies

### Cyclic identities and initial geometry

Every length-three path in the four-block cycle crosses at least one endpoint map whose rank is at most one. Thus each of the four nonzero blocks of `C^3` has rank at most one, giving total rank at most four. Each diagonal block of `C^4` has the same scalar trace `v* R B u`. These observations justify (2.3), the ordinary trace readout, and the Hilbert–Schmidt kernel without taking a trace of an infinite-rank source alone.

The feature vector field `(C*)^3` has the same cyclic positions as `C`. Differentiating the scalar product gives the four nonnegative terms of (1.4), with no cross term missing. The physical sign and factor then give (2.4).

The final root colors in the Fock construction cannot be deleted by matrix-color operators or their adjoints. The entire subspaces generated from the two roots, rather than just the initial vectors, are orthogonal. Within either sector the vacuum matching law is unchanged. The four vectors used for `K(0)` are individual unit words, so `f(0)=0` and `K(0)=4` are correct.

The Wick proof in Lemma 2 counts a term of a normalized trace by `n^(v-q-1)`. A connected quotient with `q` paired edges has `v <= q+1`. Equality means a tree, which forces opposite traversal of each paired edge and admits repeated adjacent-pair removal. Conversely, a matching-label noncrossing pairing with opposite transpose markers restores one free index at each insertion. This handles real transposes correctly, including the suppression of same-orientation pairings. In the variance, a cross-walk pairing makes the combined quotient connected; the two trace normalizations then cost an extra power of `n`. The conditional Gaussian root estimate applies to source-only matrices, where the required independence is actually present.

### Trace estimates, existence, and fitting

The noncommutative telescoping identity used in (3.3) has the correct factor order. The bounds on `f`, `K`, and the cubic trace norm follow from rank at most four and operator-norm bounds. Local Lipschitz continuity holds in the trace-class affine state, subject to R1; it is not asserted in a norm that fails to control the vector field.

The residual equation implies

`integral_0^T r^2 K dt <= r(0)^2/(4 kappa)`.

Since `||C^{*3}||_1 <= 2 sqrt(K)`, integrating the velocity gives

`||Q(T)-Q(0)||_1 <= 2 |r(0)| sqrt(kappa T)`.

This controls the full trained increment on every finite time interval. Boundedness of the vector field on that ball makes a finite terminal-time trajectory Cauchy, so continuation is justified. Restart uses the recomputed residual at the new state. The same argument is valid for every finite initial state, not just Gaussian ones.

For fitting, both endpoint squared norms have derivative `-4 kappa r f` and start at one. The initialized residual formula gives `r f <= 0`, so their common squared norm stays at least one. Formula (3.8) consequently gives `K >= 2 |f|`. If `y != 0`, the initial derivative `8 kappa y` supplies a time at which `f != 0`, after which this yields the claimed exponential residual estimate. If `y=0`, the initialized population is stationary. No lower bound for an arbitrary restart state's endpoint norms is being used to claim fitting from every restart state.

### Fixed-width transfer and the existing GD theorem

The cutoff is placed in increment norm, with a strict margin beyond the energy radius. Its field is bounded and Lipschitz uniformly in dimension on the stated source event. Each fixed Picard iterate expands into a finite list of initial rooted words and rank-one maps with time-dependent scalar coefficients. Time integration changes those coefficients, not the list of words.

The finite Gram formula `G_u^(1/2) c G_v^(1/2)` has the correct dimensions and nonzero singular values, even when either Gram matrix is singular. Consequently the cutoff norm is a continuous function of a finite list of source Grams. Uniformity in time follows from uniform continuity on compact coefficient/Gram sets and boundedness of the time-integration map. The factorial Picard-tail estimate lets the iteration index be chosen before width tends to infinity. This is the needed argument between fixed-word convergence and continuous-time convergence.

The Section 4 GD update is Euler for the weights, equivalently for `Q`. Its residual is recomputed rather than updated by an incorrect residual Euler equation. The one-step defect and geometric-series estimate have dimension-independent constants on the cutoff ball. The unit margin and extra unit of horizon handle the last interpolated interval. Thus the existing Section 4 claim for every deterministic `eta_n -> 0` is justified and does not impose an unstated width/step relation. This audit does not transfer that result to the new theorems.

### Nonclosure and unrestricted encoders

The injective-contraction proof of stable independence works because a tensor-entry monomial with injectively assigned typed indices records the incidence network up to its permitted isomorphisms. The temporary inclusion of higher-valence index vertices is necessary for quotient assignments and is made explicitly. Taking a maximal vertex count isolates a noncancellable injective type. The assertion remains a stable-width result; it is not a claim of independence at every fixed width.

For the endpoint-only derivation, differentiating `U_j` gives `X_j+Y_j`, while either quadratic endpoint contraction differentiates to `2 U_{j+1}`. Hence the coefficient `4^(j-1)` in (6.5) is correct. All full feature replacement histories have nonnegative graph coefficients, so the connected path `Gamma_j` cannot cancel. Its tensor degree is `4j+2`.

Spatial derivatives of the encoder do not enlarge its graph alphabet. Total spatial derivatives and the evolutionary chain rule place every finite output time derivative in the same component-generated algebra. At each fixed time-derivative order only finitely many graphs occur, uniformly in width, which is what makes stable coefficient comparison applicable despite width-dependent encoder coefficients.

For the analytic case, recentering at actual zero-state jets handles the empty-graph coefficients. At the required fixed tensor degree, a finite Taylor expansion uses products of the same graph alphabet. Mixed smoothness permits the finite prolongations. For physical flow with `y != 0`, the lowest-degree component is `(2 kappa y)^k D^k f`; the other term raises degree by six rather than two. For `y=0`, positivity in the recurrence `P_{k+1}=f D P_k` retains a component `f^k D^k f` and hence the forbidden connected graph. The zero-label proof does not mistakenly infer nonclosure from a moving canonical trajectory: its quantifier is an open set of current states.

The feature transport realization is local, with the advertised operator-norm contraction constants. The physical transport encoder uses an entire future output profile, and its global definition rests on the already proved finite physical flow. For `U_t=U_s` on `s>=0`, the characteristic from `(t,s)` reaches initial time at `s+t`, so no boundary datum at `s=0` is missing. The two width-one examples give kernels `4` and `25/4` at the same product and cyclic characteristic polynomial. The separate width-one polynomial closure is consistent with the stable-width obstruction. No unrestricted nonclosure claim is smuggled into the new sections.

## Section 8: shallow characteristic population

### Existence, moments, and clock

The characteristic vector field is locally Lipschitz because `phi` is `C^2`. Its magnitude has at most linear growth in `1+|A|+|U|`, even though its derivative need not be globally bounded in `(A,U)`. The term `A phi''(U)` in that derivative is therefore not a missing global-Lipschitz hypothesis: the proof uses local existence plus the growth estimate, which is sufficient. Applying the same bound to the reversed vector field handles negative feature time.

The bound (EC8.7) yields quadratic envelopes for `A phi(U)` and `H`, and a cubic envelope for their needed feature derivatives. Direct differentiation gives

`dH/ds = 4 A phi(U) phi'(U)^2 + 2 A^3 phi'(U)^2 phi''(U)`.

Thus all exchanges of derivative and expectation are supported by an integrable envelope on every compact feature interval. The two separate block-energy derivatives displayed after (EC8.11) sum to exactly this derivative. There is no missing third activation derivative.

Independence and centering of the initial readout give `F(0)=0`; the first population residual really is `-y`. Since `F'=K>=0`, the physical scalar clock is locally unique and its residual obeys the linear equation in (EC8.11). The resulting bound `|s(t)| <= 2 kappa |y| t` prevents finite physical escape, even if `F` never takes the value `y`. Existence of a fitting feature-time root is neither assumed nor needed.

Composing the global characteristics with this clock gives a marked physical solution with all finite moments on compact intervals. Conversely, a solution in the stated class defines its scalar clock by integrating `r`; markwise uniqueness then fixes its characteristics, and consistency forces the same scalar clock equation. For a restart pair, the same argument uses `1+|A_*|+|U_*|` and the true consistent residual `r_*`. No Gaussian independence is needed at restart.

### Uniform empirical limit

The fourth-moment identity (EC8.12) has the correct coefficient `3 n(n-1)` for the paired terms. Its summable bound proves almost-sure convergence at each fixed test, without importing a continuous-time law of large numbers. The Gaussian characteristic envelopes have the finite fourth moments needed both for the integrands and for the random Lipschitz constant.

Applying this argument to a countable set of finite nets and the envelope gives uniform convergence of the empirical characteristic readouts on compact feature intervals. The finite residual starts at `F_n(0)-y`, not `-y`. This gives the finite clock bound and its global existence. Eventually `|F_n(0)|<=1` under the nested coupling, so both clocks lie in the same deterministic feature interval.

Subtracting clock equations requires only the Lipschitz constant of deterministic `F` on that interval, plus the uniform error `F_n-F`. This proves (EC8.14). Evaluating the uniformly convergent readouts at convergent clocks establishes all stated physical-time observables, including both block energies and squared loss. Almost-sure convergence is claimed with the nested mark coupling; convergence in probability is intrinsic to the specified marginal models. These are correctly distinguished.

### Edge checks

- If `kappa=0`, both finite and population weights stay fixed and the empirical initial readout argument applies.
- If `y=0`, the population clock is zero; finite initial fluctuations need not be zero, and the proof accommodates them.
- If `phi` is identically zero, `K=0`, the residual need not decay, and the theorem remains true because it makes no shallow fitting claim.
- A constant nonzero activation, vanishing activation derivatives at some marks, or the absence of a root `F(s)=y` does not invalidate global existence or the compact-time limit.
- All signs of `y` are covered because characteristics exist for both signs of feature time.

## Section 9: contained Gaussian source

The operator construction is explicit on a fixed separable word Hilbert space. Creation has norm one and its stated deletion operator is its actual adjoint. Hence each source action has norm at most two. The direct sum produces two mutually orthogonal *root-generated sectors*. Merely choosing two orthogonal vectors in one sector would have been insufficient; that error is avoided here.

The `1/4`-net estimate is valid: approximating both unit vectors in a bilinear form loses at most half the operator norm, giving the factor two. There are at most `81^n` ordered pairs of net points; a matrix norm exceeding 12 forces a form exceeding 6, whose Gaussian two-sided tail is at most `2 exp(-18n)`. The exponent dominates `n log 81`. Gaussian vector squared norms have variance `2/n`. Only boundedness with probability tending to one is concluded, not a sharp spectral edge law.

The MGF differentiation contains Wick's identity, including singular covariance. The graph counting is the same valid tree/noncrossing argument as in Lemma 2, now for an arbitrary separately fixed number of labels. A real Gaussian entry is paired with its identical raw row and column, so transpose orientation must be accounted for at each side; the proof does this. Leading pairings match precisely the Fock creation/annihilation nesting. No independent-transpose assumption is made.

The connected two-walk count bounds the variance by `O(1/n)` at each fixed word length. Conditional on the source matrices, diagonal Gaussian quadratic forms concentrate about the normalized trace and cross-root forms have zero mean with the displayed variance bound. The norm event used for those conditional estimates is measurable from the matrices alone, preserving the necessary root independence. A finite union supplies joint rooted-Gram convergence.

For `q=0`, the word space is one-dimensional before the two-sector sum. The roots in `R^2` represent the limiting Gram matrix of two independent normalized Gaussian vectors. There are no source operators, and the empty-maximum convention is explicit. Typed words are a restriction of the valid word identities, not an additional independence assertion.

There is no uncontained free-probability theorem, growing-program theorem, sharp matrix-norm theorem, or spectral-law citation needed in this section.

## Section 10: every separately fixed hidden linear depth

### Autonomous state, identities, and global existence

The state norm controls endpoints in Hilbert norm, middle increments in trace norm, and the residual as a scalar. The source operators remain immutable. Telescoping products and the rank-one norm identity make the vector field locally Lipschitz, with constants that may depend on the fixed depth and source bound but not width. Subject to R1, the contraction argument therefore takes place in a complete state space.

Every insertion of a block velocity into the product prediction contributes the corresponding square in `K`. Thus `df/dt=dr/dt`, and initialization gives `f=y+r` on the true solution. Residual energy controls the integral of `r^2 K`. For each parameter block separately,

`integral_0^T ||dot theta|| dt <= 2 kappa sqrt(T) sqrt(integral_0^T r^2 K dt) <= |r(0)| sqrt(kappa T)`.

For a middle block the norm here is the trace norm because its instantaneous velocity has rank at most one. This controls all state coordinates, not just the prediction. Summing the finitely many block bounds and using `|r(t)|<=|r(0)|` gives the claimed compact-time ball and continuation. No coercivity of `K` in the parameters is needed. Restart on the consistency set is valid. The proof does not need to claim fitting at all depths.

At initialization, each forward product uses different source labels in order, and each backward product uses their adjoints in reverse order. Every annihilation term meets a different first letter or the vacuum and therefore vanishes. Each field in the initial kernel has norm one. Orthogonality of the two entire sectors gives `f(0)=0`, while the count of blocks gives `K(0)=L+1`. This also holds for `L=1`, where the kernel has just its two endpoint terms.

### Width transfer and claimed topology

The source event has probability tending to one by EC9 and includes the correct bound on the *finite* initial residual. The stated deterministic state radius is large enough for both endpoint initial norms, every block variation, and the residual. The cutoff is global in the full state norm and has a strict margin beyond the true trajectories.

For a fixed Picard index, endpoint fields use a finite list of initial rooted words and middle increments use finite sums of rank-one maps between those words. The residual coefficient is a scalar continuous function of their Grams; the Picard residual need not itself be consistent with the Picard endpoints for this numerical-description argument. The full augmented cutoff vector field, whose true solution is consistent, is being approximated.

The Gram-square-root formula includes null spaces through zero singular values. Its continuity does not require choosing continuous eigenvectors or inverting a nearly singular Gram matrix. Uniform convergence of coefficient paths follows by induction over finitely many operations and the time-integration map. This is sufficient to apply EC9 at each fixed Picard index.

The factorial tail in (EC10.13) is uniform in width. The three-term estimate in (EC10.14) subtracts only real readouts across different spaces; each state-space error is measured within its own space. Choosing the Picard index first and width second yields exactly compact-time convergence in probability for the finite families stated. Telescoping makes rooted polynomial readouts Lipschitz on the common ball. The trace norm of an increment is 1-Lipschitz in trace norm, and any fixed singular value is controlled by operator norm and hence trace norm. Finite-rank field readouts are covered by their bounded rank and the same Gram formula.

For tight trace tails, the actual velocity `dot P_ell` is trace-norm Lipschitz in time on the bounded state ball. A left Riemann approximation of its integral has error at most `C_T T^2/(2N)` uniformly in the upper time endpoint and rank at most `N+1` (a harmless loose bound). The approximation-number inequality `s_{j+N+1}(P) <= s_j(P-R)` follows by adding a rank-`<j` approximant of `P-R` to `R`. Summation gives the advertised nuclear-tail estimate. This is stronger than merely knowing each increment is pointwise trace class; it supplies the uniform tightness in (EC10.7). The source event may then be removed in probability.

The statement fixes depth before width and makes no assertion that these constants are uniform in depth. It does not assert operator-norm convergence between different ambient spaces, convergence of arbitrary adaptive or growing programs, or neuron-coordinate empirical laws. At `L=1` there are no increments; the empty maximum convention makes the tail statement vacuous and correct.

## Section 11: two-hidden-layer spectral flow

### Exact finite invariant and mode reduction

Differentiating `B B^T-a a^T` cancels its two rank-one terms exactly, with the common physical coefficient `g=-2 kappa r`. Both endpoint squared norms have derivative `2 g f`, so `delta=||a||^2-||u||^2` is constant. With `v=B u` and `q=||a||^2`,

`dot v = g [a ||u||^2 + B B^T a] = g [C + (2q-delta) I] a`.

This establishes (EC11.9) without division by `g`, `r`, or a clock. It remains valid at a stationary point. Differentiating `a^T v` gives (EC11.10), and substituting `B B^T=C+a a^T` recovers the three original nonnegative block energies.

Finite-dimensional spectral resolution of the fixed symmetric `C_n` is valid with repeated eigenvalues and singular matrices. The positive matrix-valued measure `Sigma_n` records both initial vectors and their cross spectral weights. Retaining this cross entry at finite width is necessary; the proof correctly discards it only after proving its weak limit is zero. Functional calculus with the real two-component mode coefficients reproduces the finite vectors and their readouts. There is no invertibility assumption on `B`, `C`, or the spectral Gram matrix.

### Derivation of the source, including its negative atom

For `(B B^T)^k`, every noncrossing pairing of the alternating word has opposite parity endpoints, hence opposite transpose markers. The Catalan recursion therefore follows from EC9. The beta-integral calculation of the candidate density's moments has the correct normalization: the integral at `k=0` is `pi/2`, and successive beta integrals have ratio `(k+1/2)/(k+2)`. It gives `(2k)!/[k!(k+1)!]`, matching the recursion.

The operator-norm event bounds the eigenvalues of `M=B B^T` in `[0,144]`. Polynomial moment convergence and the explicitly justified Bernstein approximation therefore give weak empirical convergence in probability. No exact largest-eigenvalue limit or unproved moment-determinacy assertion is being used.

The scalar transform has convention `m(z)=integral (z-lambda)^{-1} d rho_0`, so it is negative on the negative real axis. The derived expression

`m(z) = (1-sqrt(1-4/z))/2`

has that sign. The elementary integral at `z=-b` confirms this formula throughout the negative axis, and specifically `m(-1/2)=-1`. This sign check is consequential for the negative atom.

For `C=M-aa^T`, rank-one resolvent algebra gives `a^T(z-C)^{-1}a = h_n(z)/(1+h_n(z))`, not a denominator `1-h_n`. On the source event `C>=-4 I`, so `z<-4` avoids all finite poles; the limiting denominator is also nonzero there. Independence of `a` from `M` supplies the conditional quadratic-form concentration.

The proposed continuous part of `rho_a` is `lambda/(1+2lambda) d rho_0`. From `m(-1/2)=-1`, its mass is `1/4`, so the atom of mass `3/4` gives a probability measure. Direct partial fractions give

`integral (z-lambda)^{-1} d rho_a = (z m(z)+1)/(1+2z) = m(z)/(1+m(z))`.

The last identity uses exactly `z m(1-m)=1`. Thus the displayed atom and density identify the *rooted spectral measure* of the rank-one-perturbed source; substituting the unperturbed empirical spectral law here would have been incorrect.

The passage from transforms to weak convergence is also supplied. For each fixed moment order, choose a sufficiently large negative `z` to bound the geometric-series remainders, then take `n` large with that `z` held fixed. Previously convergent lower moments remove the lower powers. This induction, followed by Bernstein approximation, works with the common compact support and bounded masses. It does not exchange an uncontrolled `z` limit with width.

For the second diagonal entry, condition on `(B,a)` so that `u` remains independent Gaussian. The finite-rank perturbation estimate makes the normalized trace of `M p(C)` differ from that of `M p(M)` by `O(1/n)` for each fixed polynomial. The limiting measure is therefore `rho_v=lambda rho_0`. Conditional centering proves cross-entry convergence for polynomials; its total variation is bounded by `||a|| ||v||` by spectral Cauchy–Schwarz. This is enough to extend convergence to continuous tests. The diagonal masses and supports are controlled on the same norm event.

The constants check independently as follows:

| Quantity | Value and reason |
| --- | --- |
| `rho_a(Lambda)` | `3/4+1/4=1` |
| `rho_v(Lambda)` | First moment of `rho_0`, equal to 1 |
| `nu(Lambda)` | 2, not 1 |
| `integral lambda d rho_a` | Continuous contribution `3/8` minus atomic contribution `3/8`, hence 0 |
| `alpha^2 nu`, `beta^2 nu` | Exactly `rho_a`, `rho_v`, including `beta=0` at the atom |
| `q(0)` | 1 |
| `F(0)` | 0, from the real/imaginary encoding |
| `K(0)` | `1+0+2=3` |
| `delta_n` | Tends to 0 by the two normalized Gaussian squared norms |
| `E f_n(0)^2` | `1/n` by successive conditioning |

In particular the negative atom, its sign, and the mass-two integration measure have not been lost in the scalar encoding.

### Global canonical flow in the stated L2 space

Multiplication by `lambda` is bounded on the specified measure space. The vector field is a polynomial on the underlying real Hilbert space of the two complex fields and the real residual, and is locally Lipschitz there. Complex notation combines two real channels; no complex analyticity is required.

Hilbert differentiation gives `dot F=dot r`, hence initialized consistency, and `dot q=-4 kappa r F`. Because the support is bounded below by `-1/2`,

`K >= 2 q^2 - q/2`.

This inequality alone is not nonnegative for all states. The proof correctly first works on `q>1/2`, which contains the initial value `q=1`. On that interval `K>0`, the residual multiplier lies in `(0,1]`, and

`dot q = 4 kappa y^2 theta(1-theta)` lies between 0 and `kappa y^2`.

Thus `q` cannot exit through `1/2`. This closes the positivity argument without assuming its conclusion: on the full maximal trajectory `1<=q<=1+kappa y^2 t` and `K>=3/2`. The bound on `psi`, followed by direct integration of the bound on `dot pi`, controls the entire state on each finite interval. It establishes global continuation in physical time and avoids any assumption of complete feature-time dynamics.

The residual decay rate is consequently `2 kappa*(3/2)=3 kappa`, as claimed. Along this trajectory, `r!=0` makes `dot r!=0`; when `r=0` all velocities vanish. At `y=0` the initial residual is zero and uniqueness makes the initialized solution stationary. Restart along the canonical trajectory is valid. The theorem does not establish these bounds for every arbitrary point of the ambient spectral Hilbert space.

For an explicit scope stress test, choose `pi=0` and `psi` supported only at the negative atom with squared norm `q` in `(0,1/4)`. The same displayed kernel equals `2q^2-q/2<0`. This is a counterexample to *global positivity for arbitrary ambient states*, not to EC11, whose canonical trajectory has `q>=1`. It confirms why the restart qualification is necessary and cannot be broadened silently.

### Uniform finite-width identification and topology

The limiting coefficients `c,d` can be extended to the whole fixed interval `J=[-4,144]` by a linear equation with the already controlled scalar functions `q(t),r(t)`. Its solutions are jointly continuous in `lambda,t` and uniformly bounded on compact physical intervals. The scalar encoding then agrees with the already constructed Hilbert solution by uniqueness. This avoids constructing the limiting nonlinear solution by assuming a width limit.

The finite coefficients admit the same extension, using the globally existing finite network. On the norm event, the diagonal masses of `Sigma_n` are at most 4 and 576; the cross variation is bounded as well. The families in (EC11.29) are compact in `C(J)` as continuous images of the compact time interval. Finite uniform nets therefore turn weak measure convergence into uniform-in-time test convergence. Weak convergence is not applied directly to uncontrolled random test functions: the measure-error tests use the deterministic limiting coefficients, and deviations of finite coefficients are estimated separately.

Before the first mode-error stopping time, every factor in (EC11.13) is bounded. Subtracting one factor at a time gives the stated readout estimate, including both occurrences of `q` and the finite conserved offset `delta_n`. The initial residual error is exactly `f_n(0)`. The resulting integral inequality and Grönwall bound remove the stopping time with probability tending to one. All errors are scalar or mode functions on the common interval; no arbitrary alignment of finite spectral eigenvectors is required.

The three limiting block energies in (EC11.32) are correct. In particular the middle expression requires the additional `q^2`, since `B B^T=C+aa^T`. Their sum is precisely the spectral kernel in (EC11.4). The result proves compact-time convergence in probability of the stated readouts, and the proof also gives mode-coefficient comparison and convergence of `q_n`. It does not assert direct Hilbert-norm subtraction of random finite eigenvector fields against the limiting `L^2(nu)` fields.

## Section 12: exact agreements and limits

For the shallow linear model, the characteristic solution gives `F(s)=sinh(2s)` and `K(s)=2 cosh(2s)`. In EC10 at `L=1`, the initial two roots are orthonormal and their two-vector equations yield the same two quadratic readouts and the same physical clock. This comparison uses moments/inner products, not an assertion that the mark-coordinate fields and abstract vectors have identical coordinate laws.

At `L=2`, with the same normalized one datum, both the operator and spectral theorems approximate the same finite readouts in probability on a compact interval. Two different deterministic limits would contradict the triangle inequality against that common finite readout. This establishes agreement of the named observables and separate block energies, without needing to reconstruct all rooted signatures from spectral fields.

At `L=3`, the final-root-color source and the direct-sum source have the same rooted Grams. Both width-limit arguments also apply to the same finite model. Therefore the stated common rooted readouts agree. The unused parts of the source Hilbert spaces need not be identified, and no operator subtraction across them is claimed.

The limitations at the end of Section 12 are mathematically necessary and accurately describe the proved scope. In particular, neither equality of initial predictions with the small-readout regime nor the existing Section 4 GD result creates a new theorem for the additions.

## Final assessment

The additions supply the nontrivial arguments that would otherwise be missing: global two-sided shallow characteristics, a uniform empirical-to-clock transfer, an explicit fixed-word Gaussian source, a cutoff Picard passage from initial geometry to continuous physical time, uniform trace-tail control, the rooted spectral measure of the rank-one perturbation including its negative atom, and a stopped uniform mode comparison. Their constants and hypotheses are compatible with the notation contract.

The strongest verdict justified by the supplied pair alone is **qualified PASS, with R1 required for a literal all-foundations-contained proof**. With standard compact-operator and trace-class foundations admitted, the stated results pass this independent adversarial audit without a required change to their mathematical content.
