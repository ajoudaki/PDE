# Independent complete-proof audit

## Verdict

**PASS at the stated fixed-program scope.** I found no counterexample, missing hypothesis, incorrect normalization, or proof-breaking dependency in Theorem 8.1. The supplied arguments establish the claimed fifth-derivative bound, the compiler-defined cubic coefficient, and the fifth-order step-doubling remainder for each fixed activation and each separately fixed finite pair `(L,N)`. Section 5 supplies the needed pointwise, fixed-nonzero-step convergence of expectations.

**Required mathematical corrections: none identified.** There is one optional clarification concerning the activation dependence of Section 5's conditioning constants, described below. This verdict does not certify a uniform activation-class conditioning estimate or any joint growing-`N` width limit.

This is a mathematical audit, not a conclusion drawn from tests, previous reviews, implementation output, or a summary. I checked the arguments in the two supplied files and independently reconstructed the main cancellation, regularity, and bounding steps.

## Inputs, isolation, and complete read coverage

The only input files read were:

| Input | Bytes | Lines | SHA256 |
|---|---:|---:|---|
| `/tmp/pde-quantitative-isolated.8JwnFK8g/PROOF.md` | 108754 | 2676 | `acfee00f63de4f35023521fe5c9baef00d018dae3fe79186ea3d6147ea1e77ce` |
| `/tmp/pde-quantitative-isolated.8JwnFK8g/NOTATION.md` | 5110 | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

I read both files in full, through EOF. The complete proof coverage can be partitioned into lines 1–420, 421–840, 841–1260, 1261–1599, 1600–1840, 1841–2100, 2101–2460, and 2461–2676. The notation coverage is lines 1–98. One combined tool display was truncated; an overlapping read of proof lines 1600–1840 recovered the affected passage, including the end of Section 5 and all of Section 6. No coverage claim relies on omitted display text.

I checked the input hashes before and after the substantive audit; they agree. I made no input edits. I used no network, agents, numerical experiments, project files, history, previous reviews, or skill files. The report directory was created afresh with `mktemp -d`, and this report was written with `apply_patch`.

Line references below refer to the supplied `PROOF.md` unless explicitly labeled `NOTATION.md`.

## Scope and dependency audit

The operative chain is:

1. The exact stored-parameter network and simultaneous feature-ascent updates in Section 5.2.
2. The predictable finite matrix-action chronology, conditional Gaussian laws, response cancellation, strict rank, joint coupling, and expectation control in Sections 5.3–5.10.
3. The equivalent chronological layerwise expectation calls in Section 8.2.
4. The singular-covariance differentiation lemma and finite derivative/envelope compilers in Sections 8.3–8.4.
5. The explicit one-call majorant and its finite iteration in Section 8.5.
6. The parity and first-order calculation in Section 8.6, followed by integral Taylor expansion in Section 8.7.

Sections 1–4 provide elementary Gaussian-conditioning, derivative, and moment identities consistent with this chain. Section 6 limits stronger interpretations; neither its obstruction results nor Section 3's finite directional derivatives are used to justify exchanging width limits with derivatives.

The mathematical imports are elementary finite-dimensional linear algebra, Gaussian integration, probability inequalities, finite-moment laws of large numbers, and elementary differentiation/integration. The nontrivial conditioning, singular differentiation, concentration, and operator-norm estimates needed here have arguments within the supplied text. I found no missing non-elementary imported theorem needed for Theorem 8.1.

The claim at lines 225–227 about what a software API implements is not verifiable from these two files. It is not used as a mathematical premise: Section 4 proves the recurrence itself, and Section 8 defines its compiler mathematically. Accordingly, that implementation claim is not certified by this review and is not a proof gap in the addition.

## Model, normalization, and scope

The model matches the notation contract. Hidden matrices have entries of variance `1/n`; the first weight and stored readout have order-one standard Gaussian coordinates. The latter is explicitly a different regime from the small-readout convention in `NOTATION.md` lines 72–76. The output remains `W_readout^T h_top/n`.

The cotangent convention is `delta = n partial f/partial z`. It gives the gradients and updates in (5.2.7)–(5.2.8): first-weight and readout increments are respectively `h delta` and `h h_top`, whereas a middle matrix receives `(h/n) delta h_previous^T`. There is no missing factor of `n`, sample average, residual, or squared-loss factor of two.

The unscaled-coordinate statement is also correct. With `A_middle = sqrt(n) W_middle`, one has `partial_A f = partial_W f/sqrt(n)`. An `hn` mobility in the unscaled coordinates therefore gives `Delta W = h partial_W f`, as required for the stored middle matrices.

Summing the matrix increments produces exactly the learned forward and backward terms in (5.2.11)–(5.2.12), with normalized pairings `Q = h_j^T h_k/n` and `K = delta_j^T delta_k/n`. Only `j<k` contributes. All expectations in the population version contract fields on the same physical layer; the two directions of one matrix have not been replaced by independent matrices.

The comparison is `N` steps of size `2h` versus `2N` steps of size `h`. Its equal accumulated feature-step length is not a physical-time gradient-flow assertion. Section 8 applies Section 5 at each separately fixed nonzero step, and handles zero independently. No common positive conditioning gap near zero is used.

## Sections 1–4 and 6

### Gaussian reuse and exact conditioning

In Section 1, projecting each Gaussian row onto the constant vector gives the stated conditional mean `y 1^T/n` and residual right projection. The transpose action then has conditional mean `a_n 1` and covariance `sigma_n^2 P`. The third term in the RMS comparison (4) is exactly the RMS of the removed constant Gaussian component. The moment assumptions cover all the laws of large numbers and integration by parts, including the degenerate variance case. The short weak-plus-second-moment argument for quadratic Wasserstein convergence is elementary and sufficient here.

In Section 2, compatibility `U^T Y=R^T V` verifies both affine constraints on the proposed mean. Homogeneous perturbations have the form `(I-P_U) A (I-P_V)`; each summand of the mean is orthogonal to that subspace. Thus the residual covariance and its scale are correct. The adaptive extension conditions on roots and past answers before choosing the next query, which is essential and is stated. Discarding exact dependencies is distinguished from passing to limits of poorly conditioned inverses.

### Derivative and moment identities

The three directional derivatives in (8) are correct: differentiating `2<g,Hg>` contributes `2 T[g,g,g]` and two equal Hessian-square terms totaling `4||Hg||^2`. The metric change is correct for constant positive definite `D` and introduces no residual factor.

For (9), applying Gaussian integration by parts to `X^(alpha-e_i)` gives the coefficient `alpha_j-1_(j=i)` and reduces degree by two. The representation `X=AG` proves the identity at singular covariance. The rational positive-semidefinite validation by a zero-pivot test or Schur complement has the stated necessity and sufficiency. Neither result is an adaptive inverse-stability theorem, and the text does not use it as one.

### Obstructions and nonanalytic example

The product-norm obstruction follows because bounded `L^(kp)` norms would force essential boundedness. The ordinary-jet shift/product tests yield the incompatible bound `j <= C_P C_S w_1`; the factorial-normalized version moves the factor `j` to the shift and gives the same contradiction.

For `g(t)=E(1+t^2G^2)^(-1)`, the bounded rational derivatives supply an integrable dominating function at every fixed derivative order. The Gaussian even moments give zero Taylor radius, while the displayed two-variable smooth ODE has the claimed unique solution. The example is correctly kept separate from a network closure or analytic flow claim.

## Section 5: the width-limit dependency

### Predictability, multi-matrix conditioning, and scale

The action count `(2N+1)(L-1)` is correct: `N` complete forward/backward sweeps followed by one terminal forward sweep. The query for each action is available before that action. In particular, current forward features may contain earlier transpose answers of the same connector, and the conditioning theorem explicitly permits that dependence.

For Lemma 5.4.1, condition on the global past. The residuals of the independently initialized matrices are still conditionally independent. A predictable new query selects a fixed direction in the remaining Gaussian subspace. Splitting along that direction leaves a Gaussian residual independent of the observed component and of the other matrix residuals. The same reasoning applies to a transpose query. It also applies if the query has zero orthogonal component, in which case no new constraint is added.

I checked the factors of `n` in (5.4.4)–(5.4.7). With `Y=MV/sqrt(n)`, `D=M^T U/sqrt(n)`, `Q=V^T V/n`, and `K=U^T U/n`, the cross identity is `U^T Y/n=D^T V/n`. The residual variance is the normalized squared orthogonal-query norm, rather than that norm itself. The Moore–Penrose interpretation for finite singular query blocks is valid and is used only for the exact raw conditional law, not to assert continuity of inverse coefficients.

### Inverse-free program and response cancellation

The Gaussian source covariances are deterministic second moments of previously constructed query fields. Blocks assigned to different sources are independent; chronological extension preserves their specified within-block correlations. On each physical layer, the random marks have exactly the placement listed in (5.9.2). Earlier response and covariance coefficients are held fixed under an ambient source derivative.

The construction is finite and has polynomial Gaussian envelopes under the `C^2` hypothesis: values use linear growth and bounded first derivatives, while a source derivative of a cotangent can use the bounded second derivative. No derivative of an earlier scalar coefficient with respect to a source is needed.

Here is an independent reconstruction of the cancellation. Write old population actions as `y=xi+P c` and `d=chi+S h`. Gaussian integration by parts gives

`R_cross = E[c y^T] = S Q + K P^T`.

For a new forward query with `q=E[h H_*]` and `rho=E[grad_chi H_*]`,

`v=E[d H_*]=K rho+S q`,

so

`K^(-1)(v-R_cross Q^(-1)q)=rho-P^T Q^(-1)q`.

The final term cancels the old response component inside `y^T Q^(-1)q`. What remains is the old Gaussian-source regression, its new innovation, and `c^T rho`. For a transpose query the identical calculation with the populations exchanged yields `Q^(-1)(omega-R_cross^T K^(-1)k)=sigma-S^T K^(-1)k`. This establishes both inverse-free responses with the stated signs and indices.

These algebraic calculations are used within the later coupling induction; their provisional population-limit notation is not an unsupported invocation of a separate state-evolution theorem. Rank can be proved directly for the already specified inverse-free construction before the coupling uses these inverses.

### Strict rank, including affine activations

The two rank facts in Section 5.7 are sufficient: a continuous nonconstant function has positive variance under every nondegenerate Gaussian translate, and a new field with positive expected conditional variance cannot be a deterministic linear combination of old fields measurable under that conditioning.

At initialization, normalization gives every forward second moment equal to one. Centered independent backward carriers make the time-zero responses vanish and yield `K_(ell,00)=mu^(L-ell+1)`, where `mu=E phi'(G)^2`. A nonconstant continuously differentiable activation has `mu>0`.

The induction uses genuinely fresh coordinates in the required order:

- A new forward-source innovation appears additively in the current preactivation, while its older features and learned response terms exclude that innovation. This extends the feature Gram and gives positive probability of a nonzero activation derivative.
- At the top, if `phi'` is nonconstant, the current forward innovation varies `phi'(Z_k)` with the readout held fixed. The readout is nonzero with positive probability: at `k=0` it is `A`; later its preceding update has positive conditional variance from the previous fresh top forward innovation and `h != 0`.
- If `phi(x)=p x+c` with `p != 0`, the current cotangent cannot be treated by nonconstancy of `phi'`. Instead it contains the previous top forward innovation with coefficient `h p^2 tau`. All older top cotangents exclude that innovation. Its variance is `h^2 p^4 tau^2>0`, exactly as needed.
- During descent, a fresh backward innovation multiplies the already constructed `phi'(Z_k)`, which is nonzero with positive probability. This extends each lower cotangent Gram.
- At the bottom, the current backward innovation enters the next state with coefficient `h upsilon phi'(Z_k)`. On the positive-probability nonzero-derivative event, it gives both a new independent feature direction and positive probability of a nonzero derivative at the next step.

This proves the terminal forward ranks as well as the nonterminal backward ranks. Negative nonzero `h` causes no failure: the relevant variances depend on squared coefficients and full support. Zero step is correctly excluded. For `L=1`, no conditioning history is used; the separate iid argument applies. Constant activations are handled without a cotangent inversion.

### Empirical ledger, moment tower, and stopping

The forward regression ledger contains the old Grams, the new feature's old-feature overlaps, its old-raw-transpose overlaps, and its squared norm. The backward ledger enlarges the forward block by precisely the missing current column before using the current cotangent. Thus the raw-response cross-moment needed after a forward action is retained, and no mixed-connector Gram needs inversion.

The even-moment estimate (5.9.4) is valid: centering removes every singleton index, so a surviving tuple uses at most `nu/2` distinct indices. The pair-moment estimate (5.9.5) follows by subtracting the coupled iid product average and applying Hölder twice. The sampled population products are iid within their physical population even though different fields at one coordinate are dependent.

On the good event, the inverse identity bounds differences without differentiating an inverse at a singular matrix. The longest regression coefficient contains two unbounded moment factors, so its difference is bounded by `C Z_n^2 delta_n`. The innovation variances stay above a fixed threshold; the square-root Lipschitz factor in (5.9.7) is correct. Their upper moments follow from the normalized query norms, so an upper spectral stop is unnecessary.

For the removed Gaussian projection, conditional regression coefficients have covariance `(V^T V/n)^(-1)/n`. This proves the `n^(-1/2)` projection estimate in the explicitly normalized coordinate norm. The four error types in (5.9.8b) are exhaustive: old-field errors, coefficient errors, innovation-scale errors, and the removed projection. Moment order `8 nu` is sufficient for their Hölder products.

I also checked the bundled coordinate cost rather than treating it as a single Lipschitz operation. A learned scalar-times-field assignment can be followed by multiplication by a bounded activation derivative, or by the terminal readout-times-feature product. Two successive Hölder losses suffice; the bundle cost `4 nu` covers them. Pair moments cost `2 nu`. Thus the backwards tower `R_(j-1)=8 R_j` covers each of the at most `3(2N+1)(L-1)+1` ledger entries. The initial Gaussian marks have the resulting finite moments. Choosing a larger even common order controls arbitrary finite outer and coordinate orders on the two probability spaces.

The stop is predictable and cumulative. Before its first failure, raw and extended histories agree. After a failure, the extension uses deterministic population coefficients and the same fresh full Gaussian vector as the ideal array; its error still depends only on prior extended-field errors. The raw history continues from its exact conditional law, so it is never replaced by the extension.

The population spectral and Schur gap gives fixed positive failure thresholds. Entrywise concentration, inverse stability, and a finite union bound yield any prescribed polynomial failure probability. The positive gap belongs to this fixed program and activation; it is not asserted uniform near zero.

### Removal of stopping and convergence of expectations

The raw-network majorant uses ordinary operator norms and explicit RMS factors. Its rank-one estimate is `||(h/n)xy^T||_op <= |h| (||x||_2/sqrt(n))(||y||_2/sqrt(n))`. All its updates are polynomial with nonnegative coefficients, so fixed depth and step count give a finite polynomial in the initial norm majorant.

The supplied sphere-net proof gives a uniform Gaussian matrix operator-norm tail: the `9^n` net in each argument, the factor two in the norm approximation, and the exponent `n log 81 - n y^2/8` are consistent. For `y^2 >= 16 log 81`, the tail is at most `2 exp(-y^2/16)`. Thus every required moment of the initial majorant and its fixed polynomial is uniform in width.

For `p>=2`, the possible coordinate loss is only `n^(1/2-1/p)`. With the chosen failure exponent `b=2 nu` and `nu>=P`, Hölder gives the stopped-piece exponent `(1/2-1/p)_+ - nu/P <= -1/2`. For `p<=2`, there is no coordinate loss. This removes stopping from all the fields. Pairings are controlled by products of RMS norms, and the output is bounded by the square of the same polynomial majorant. The output is therefore uniformly integrable, and the coupling to the iid terminal product proves the claimed convergence of expectations.

This establishes precisely the dependency used by (8.1.6), without any claim about unextended inverse coefficients on rare singular finite-width events.

## Section 8: compiler, singular differentiation, and quantitative bounds

### Chronological Gaussian calls

The call schedule in Section 8.2 has no circular input. Interior forward calls receive the current lower feature covariance and the old upper cotangent covariance. They produce the next forward covariance and response. The top call then produces its current cotangent covariance and transpose responses. Descending calls propagate these to the bottom, whose update supplies the next-time bottom feature covariance and forward responses. Full coefficients formed from parallel expectation outputs are assembled after those integrals; they are not inputs to their own integrands.

Old fields reconstructed in a later call use only old source coordinates and old fixed scalar coefficients. The larger Gaussian law has the earlier law as its marginal. This verifies that saved old Gram entries and newly computed entries belong to one common second-moment matrix, which is positive semidefinite even at zero step.

The dimensions in (8.2.5) count the marks correctly and are at most `D_N=2N+2`. There are `2(L-1)` nonterminal calls per update and `L-1` terminal calls. The `L=1` case uses one two-dimensional Gaussian expectation with the exact simultaneous scalar recursion and requires no invented history block.

### Singular Price formula

For positive definite covariance, differentiating the density gives (8.3.3), including the factor `1/2`. Its contraction with the density Hessian gives the same expression. Both ordered off-diagonal terms are included in `C':D^2`. Two integrations by parts yield the stated differentiation operator.

For singular covariance, `C_epsilon=C+epsilon I` is positive definite, and all positive-order covariance derivatives remain unchanged. Thus the recursively obtained expressions `Psi_r` are exactly the same before taking the limit. At each fixed parameter, the two square roots commute and their eigenvalue differences are at most `sqrt(epsilon)`, giving the uniform operator bound (8.3.5).

The coupled Gaussian vectors are uniformly bounded by a fixed multiple of `||G_b||`. The polynomial envelopes therefore give uniform integrable tails. On bounded Gaussian balls, joint continuity of the finitely many integrands gives uniform convergence. Consequently every derivative expression through order five converges uniformly. Passing through the fundamental-theorem-of-calculus identities successively proves differentiability of the limiting expectation and continuity of its derivatives. This does not differentiate a singular square root and remains valid when the covariance rank changes.

The assumed mixed-derivative region is sufficient: after `r` applications, covariance derivatives of order at most `r` occur, and the integrand has only derivatives satisfying `j+ceil(|alpha|/2)<=r`. No positive lower bound on the original covariance is needed.

### Exact and envelope compilers; derivative budget

The envelope addition, multiplication, and activation rules preserve their stated polynomial bounds, including a degree-zero input. Earlier scalar nodes are tokens whose source derivatives vanish; only total parameter differentiation advances their derivative order.

The recursion (8.4.5) correctly differentiates a previously formed `Psi_r`: distributing `j` parameter derivatives over `C'` gives `binom(j,a) C^(a+1)`. Summing absolute envelopes over ordered spatial indices and then using an entrywise covariance bound is conservative, possibly overcounting but never omitting terms. The strict guard ensures all child entries and covariance derivatives are available.

An undifferentiated local state or product has activation atoms of order at most one. A response's preliminary ambient derivative raises this to at most two. Within a guarded entry, at most `2r+j+q<=10` additional ordinary derivatives can fall on the integrand. Hence the highest activation derivative is order twelve. Earlier scalar tokens and covariance entries need at most five parameter derivatives. Source differentiation never consumes extra derivatives of those tokens. This justifies `C^12` for arbitrary fixed program size without an activation-regularity requirement growing with the number of calls.

The Gaussian radial-moment formula in (8.4.6) is correct, including its zero-covariance interpretation. Coefficient assembly (8.4.7) uses `(hQ)^(j)=hQ^(j)+jQ^(j-1)` and treats the diagonal transpose response separately. At zero, the exact assembly correctly omits the `hQ^(j)` term.

Induction over the call schedule supplies continuous derivatives and polynomial bounds for each subsequent integrand and a `C^5` positive-semidefinite covariance. The singular Price lemma therefore proves both the bounds and the identification `J_r(T)=T^(r)(0)`. The compiler is defined before that identification and is not merely a name for an unknown derivative.

At zero, source copies coalesce only after ambient differentiation. The surviving activation arguments are individual standard Gaussians. Independent carrier moments eliminate odd carrier powers and turn even scale powers into integer powers of `mu`. Therefore the exact coefficient reduces to a finite expression in the integrals (8.4.12) and elementary Gaussian moments. It need not reduce to a short fixed list of activation moments for this claim to hold.

### Explicit constants and majorant accounting

I checked the obligations supporting Lemma 8.3 and the exponent, not just that the constants are large:

1. **Raw syntax.** With expression size at most `R`, a product of at most three expressions has size at most `3R+2`. Summing at most `2N+3` such products is bounded by `16(N+2)(R+1)`. Local histories require no more than the stated number of assignments, and `8(N+1)` iterations cover the separate single-layer unrolling as well. The factor in `c_(N,0)` covers the terminal/Gram product before differentiation.
2. **Differentiation.** For a product, the derivative tree contains two differentiated children and two unchanged children; for an activation it contains the unchanged argument and its derivative. Substituting the child bounds establishes `|partial e|<=2(|e|+1)^2`. Advancing a scalar token does not increase its tree size.
3. **Multiplicity.** Integer and binomial coefficients and all ordered index sums are expanded before counting. An initial spatial aggregation has at most `D^10` entries. A Price level has at most `1+32 D^2` summands. The map `64(D+1)^10(c+1)^2` dominates these additions, covariance multiplication, and a differentiation step. This is a count of operations on the guarded arrays, not an instruction to differentiate beyond their regularity budget.
4. **Number of size enlargements.** Ten base derivative levels, one preliminary response derivative, one spatial aggregation, five Price combination levels, and two assembly levels total nineteen. Twenty-four applications cover this count. Full coefficient assembly has at most seven unit summands at derivative order five; entrywise covariance assembly has at most `D^2` entries. Thus the count includes these post-integration operations.
5. **Envelope coefficient and degree.** A tree with at most `C_N` nodes has degree at most `C_N` and coefficient at most `(2 B_phi)^(C_N) S^(C_N)`. Bounded positive-order activation derivatives only reduce the degree. The factors of two cover additions and the linear-growth `1+A` term.
6. **One Gaussian cost.** Assembly is additive. Old scalar bounds can be regarded as constant integrands, so a sum of returned bounds is dominated by one common moment majorant of the largest degree. There is no hidden multiplication of two independently integrated new bounds in these assemblies.
7. **Moment scaling.** The covariance entrywise bound is at most `(D+1)^2 S`. Coupling standard Gaussians by their initial coordinates gives the factor `S^(C_N/2) nu_N`. Together with the envelope coefficient this costs `S^(3C_N/2)`, safely enlarged to `S^(2C_N)`. The definition of `alpha_N` supplies `2^(C_N) nu_N <= B_phi^(alpha_N)` because `B_phi>=4`.

These steps yield the stated one-call bound with `p_N=2C_N` and `r_N=C_N+alpha_N`, without an unspecified multiplicative constant.

Initialization uses constants bounded by `B_phi^(2L)`; a history node's value at zero is not incorrectly used as a bound on its derivatives. The recurrence `a_(j+1)=r_N+p_N a_j` therefore applies successively to all calls and gives exactly (8.5.13). The initial-coordinate coupling also proves monotonicity of the moment factor as `D_N` and `C_N` increase. The size recurrences, call count, and scalar recurrence then show `E_(L,N)` is nondecreasing in `N`, including the one-call case `L=1`.

## Parity, linear coefficient, and final remainder

### Symmetry without an activation-parity assumption

Under simultaneous sign reversal of the parameter `h`, the top mark `A`, and all backward Gaussian blocks, forward states and features are unchanged, while readouts and cotangents change sign. The source derivative defining a forward response contributes the sign from differentiating the reversed backward coordinate. A backward response inherits the cotangent sign with its forward coordinate unchanged. Thus both response families and the full coefficients are odd, while the two Gram families are even. Their covariance laws are preserved at the next chronological extension.

Consequently `F` is odd, all scalar responses vanish at zero, and every call has `C'(0)=0`. This assertion concerns scalar expectations and transformed fields; it does not incorrectly claim samplewise evenness while fixing the backward marks.

### Independent first-order reconstruction

At zero, the first Price derivative of an expectation is just the expectation of its explicit parameter derivative, because the covariance derivative vanishes. Ambient source coordinates must remain distinct during that differentiation.

For the bottom feature, differentiation of `Z_k=U+h sum_(j<k) Delta_j` gives

`partial_(chi_(2,j)) dot H_k = phi'(U)^2`,

so the first forward-response derivative is `b_(2,kj)=mu`. On an interior layer, the derivative of the learned full coefficient is `1+b_(ell,kj)`, while terms differentiating an old cotangent are multiplied by a zero coefficient and vanish. After taking the relevant ambient derivative and then coalescing the two forward sources, this gives

`b_(ell+1,kj)=mu(1+b_(ell,kj))`.

Therefore `b_(ell,kj)=sum_(a=1)^(ell-1) mu^a`. At the top,

`dot H_N = N (sum_(a=0)^(L-1) mu^a) A phi'(G_L)^2`,

and `dot W_N=N phi(G_L)`. Differentiating their product and taking expectation gives

`F'_(N,L)(0)=N sum_(a=0)^L mu^a`.

This includes the readout contribution `N` and all hidden-layer contributions with the correct mobility. It uses the population compiler directly, not differentiation of a width limit. The direct single-layer recursion gives the same result for `L=1`.

### Exact affine special case checked by hand

As an independent normalization and cubic-sign check, take `L=1` and `phi(x)=p x+c` with `p^2+c^2=1`. Set `H_0=pU+c` and `W_0=A`. The exact simultaneous updates become

`W_(k+1)=W_k+hH_k`,  `H_(k+1)=H_k+h p^2 W_k`.

Since `E A H_0=0`, `E A^2=1`, and `E H_0^2=1`, direct multiplication gives

`F_(1,1)(h)=(1+p^2)h`,

`F_(2,1)(h)=2(1+p^2)h+2p^2(1+p^2)h^3`.

Thus `F_(1,1)(2h)-F_(2,1)(h)=-2p^2(1+p^2)h^3`. This agrees with `(8 J_(3,1,1)-J_(3,2,1))/6`. In particular, for `phi(x)=x` the coefficient is `-4`, not `+4` or a coefficient with an extra loss-normalization factor. This is an exact symbolic special case, not a numerical test used in place of the general proof.

### Taylor coefficient and constants

Oddness and `C^5` regularity eliminate the zeroth, second, and fourth derivatives at zero. Repeated integration of the fifth derivative gives the displayed Taylor formula, with remainder at most `sup|F^(5)| |u|^5/120`, also for negative `u`.

For the two programs, the linear terms cancel because `2 F'_(N,L)(0)=F'_(2N,L)(0)`. The remaining cubic coefficient is exactly `(8 J_(3,N,L)-J_(3,2N,L))/6`. The two remainder magnitudes contribute `(32 B_phi^(E_(L,N))+B_phi^(E_(L,2N)))/120`. Monotonicity of the exponent and `33/120<1` prove (8.1.5) with its stated constant and domain.

At zero, every raw update is the identity and the initialized centered readout is independent of the features, so the finite-width expectation is zero. The coalesced population terminal product has the same zero expectation. No rank assertion at zero is needed. If `mu=0`, continuity and full Gaussian support imply `phi'` vanishes everywhere; normalization gives `phi=+1` or `-1`, and the exact answer is `Nh`. This verifies the degenerate branch.

The optional smaller radius, the substitution `M_(3,2N)=8N+2`, and the epsilon-dependent cubic comparison follow from the displayed inequalities. The added `1` in the latter denominator is conservative. None of them supplies an estimate of order `N^4 |h|^5` or a uniform `1/N` domain.

## Corrections versus optional edits

### Required corrections

None identified for the theorem read at its stated fixed-activation, fixed-depth, fixed-step-count scope. In particular, I do not find a need to increase the activation regularity beyond `C^12`, repair the factor `1/2` in Price differentiation, change the cubic coefficient, increase the displayed numerical exponent, add an affine exclusion, or assume nonsingular covariance at zero.

### Optional clarification: conditioning constants depend on the chosen activation

Section 5's notation for constants sometimes lists only `(L,N,h,M)`, and writes the spectral gap as `gamma_(L,N,h)`; see lines 315–318, 1277–1283, and 1537–1540. The gap is defined from the population Grams of the particular activation, so that dependence is implicit in the proof.

It would be clearer to say explicitly that the constants may depend on the fixed activation through its population Grams, or to include `phi`/the chosen gap in their subscripts. A positive gap cannot be inferred uniformly merely from an upper activation bound and nonconstancy: for `phi_epsilon(x)=(1+epsilon x)/sqrt(1+epsilon^2)`, the hypotheses have a common finite upper bound as `epsilon` tends to zero, whereas `K_(L,00)=epsilon^2/(1+epsilon^2)` tends to zero. Thus the stated spectral gap tends to zero too.

This is a clarification of the fixed-activation interpretation, not a counterexample to Theorem 8.1 or a demonstrated failure of its quantitative bound. Section 8's explicit exponent does not use that gap; it uses the inverse-free Gaussian compiler. If Section 5 were intended to assert activation-uniform positive conditioning gaps under only its displayed upper bound, that stronger assertion would require correction.

## Calibrated conclusion

The supplied proof supports the quantitative doubling result as a fixed-program theorem, with the exact finite compiler as its cubic-coefficient formula. The singular covariance issue is resolved by uniform regularization, the width-expectation dependency includes rank and uniform integrability, and the derivative and numerical budgets have finite explicit majorants. No proof-breaking issue was found under the stated interpretation.

The verdict does not extend to growing depth or step count in a width limit, a joint small-step/width limit, an infinite Taylor expansion, physical-time loss-gradient flow, a compact alternative moment formula, or the correctness of any software implementation.
