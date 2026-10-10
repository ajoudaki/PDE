# Independent internal audit of the frozen master proof

**Verdict: PASS for the stated finite program language.** I found no counterexample or substantive gap in the complete proof chain. This is an internal mathematical audit, not a promotion review or approval to change the maintained book.

## Frozen input and coverage

The sole scientific input was `master_proof.md`, SHA256
`c4abad79d33496a1d8259d88faa6a6747d58c0017a3d8401298629d506b1d823`.
It contains 467 lines. An initial combined display was truncated; I then read the complete file in four explicitly bounded, untruncated chunks covering lines 1–120, 121–240, 241–340, and 341–467. The SHA256 was checked again after reconstruction and was unchanged.

I also read the required `solve-math-rigorously` skill, the complete canonical-notation skill, and its linked neural-response-memory reference. I did not read the study README, history, other reports, other research, the maintained book, the linked paper, or its supplement. The provenance claims about those external sources were not used as premises. No numerical experiment or external theorem invocation is needed to replace a missing scientific step in this candidate.

The scope is important: the graph, derivative order, root laws, and all scalar coefficients are fixed as width grows. Constants and constant vectors have the fixed meanings stated in the language; arbitrary width-dependent deterministic input arrays are not an additional input class. The result concerns scalar observables and vector empirical laws, not convergence of a neuron to a deterministic value. It admits neither unrestricted parameter tensor contractions nor dense matrix directions.

## Reconstruction of the analytical argument

### Evaluator existence and formal derivatives

Lines 55–93 give a causal construction. At a matrix call, its input is already a function of a finite prefix of Gaussian roots and named sources, with earlier scalar expectations treated as deterministic coefficients. Its Gram extension is positive semidefinite. Its response coefficients are expectations of formal source derivatives of that already defined input. Thus neither computing the new source covariance nor computing the response requires the new source itself.

Keeping each named source as a separate formal argument is essential when a Gaussian covariance is singular. The proof does so. It does not differentiate a chosen square root of the covariance or redefine derivatives intrinsically on the Gaussian support. Finite compositions, sums, products, and derivatives preserve polynomial growth, so all these Gaussian expectations exist. Scalar nonlinear dependence can appear inside an expectation node; the final polynomial assembly in (7) only claims polynomial assembly from those nodes.

### Uniform moments, including every raw-entry derivative order

The strengthened moment induction in lines 99–179 is valid. It is an induction over the finite instruction list, simultaneously for all finite moment exponents and raw-entry derivative orders. Consequently the matrix step may use a higher derivative order of an earlier node without circular reasoning. At fixed graph depth the resulting dependency on earlier bounds is finite.

For a matrix call and a fixed raw-entry derivative list, the product rule leaves one matrix sum and at most as many isolated earlier-node derivatives as the length of that list. A transpose changes a row into a column but leaves the argument intact. For an even moment, fix a tuple of summation indices. Let (b) be the number of distinct indices and (s) the number occurring once. Inserting the (s) commuting finite differences is legitimate: every discarded term is independent of at least one centered singleton entry except for its single linear factor. The fundamental theorem of calculus then adds one factor of each singleton entry and differentiates only earlier-node products.

The weight factor has squared expectation bounded by (C n^{-(p+s)}). The differentiated earlier-node product has a uniformly bounded second moment even after the selected entries are multiplied by arbitrary (t_u\in[0,1]), because the strengthened induction allows independent entry variances anywhere in ([0,1/n]). Derivatives are evaluated at the modified array; they are not derivatives of the map that scales the array. This removes any concern about extra (t_u) factors or division at (t_u=0).

Cauchy–Schwarz gives (C n^{-(p+s)/2}\le C n^{-b}), since (p\ge 2b-s). There are (O(n^b)) tuples of each fixed equality pattern. Their total contribution is bounded, and the number of patterns is finite. The empty singleton set is correctly covered by the same argument. Entry repetition, repeated matrix use, transpose reuse, zero entry variances, and index choices depending on the derivative list do not invalidate the estimate.

Coordinate maps and scalar feedback use finite chain-rule sums and Hölder bounds; normalized averages use Jensen. These steps retain uniformity in the allowed variance arrays and in function families with common derivative profiles. Jensen then gives precisely the two-exponent averaged moment bound (3), including nonintegral finite (p,q\ge1).

The operator-norm bound (14) is also sufficient as stated. Two (1/4)-nets have at most (9^{2n}) pairs, each pairing has variance (1/n), and the factor-two approximation gives the displayed tail exponent. For (t\ge10), its second bound is valid uniformly in (n\ge1). Integrating the tail supplies every fixed operator-norm moment.

### Adaptive Gaussian conditioning and the response formula

The conditioning argument in lines 193–264 handles adaptive inputs. Conditional on roots and the accumulated transcript, the next input is fixed. Independent conditional matrix factors are maintained when a linear observation is made of one matrix. The transcript records actual calls, including previous scalar feedback, so no additional independence between an input and its matrix is assumed.

The mean in (15) satisfies both (WV=Y) and (W^TU=Q): compatibility (U^TY=Q^TV) gives its reverse constraint, and the second term vanishes on (V). It is orthogonal to the homogeneous solution space (P_{U^\perp}KP_{V^\perp}), giving the projected isotropic Gaussian residual. Thus (16) and its transpose counterpart have the stated scaling.

When the limiting query Grams are positive definite, joint empirical (W_2) convergence supplies the normalized inner products needed for the projection coefficients and innovation variance. Inversion is then continuous. Removing the bounded-rank Gaussian projection costs vanishing normalized mean square. Conditional independence of the remaining Gaussian coordinates gives variance (O(1/n)) for bounded empirical tests; convergence of conditional means and the explicit second-moment calculation give the new joint (W_2) law. Lipschitz coordinate maps and normalized scalar averages preserve the induction. Replacing previous scalars by their deterministic limits is justified by the global Lipschitz bound, including in vector RMS.

I reconstructed the response cancellation explicitly. Let (H_\perp=H-\sum_r\alpha_rH_r) be orthogonal to every previous forward input. Every previous reverse answer is its reverse Gaussian source plus a deterministic linear combination of those forward inputs. Hence

\[
\mathbb E[V_sH_\perp]=\mathbb E[\zeta_sH_\perp].
\]

With (C_{st}=\mathbb E[U_sU_t]), Gaussian integration by parts gives the vector identity

\[
\mathbb E[\zeta H_\perp]
=C\,\mathbb E[\nabla_\zeta H_\perp].
\]

The resulting coefficient in (16) is

\[
\beta_s=\mathbb E[\partial_{\zeta_s}H]
-\sum_r\alpha_r\mathbb E[\partial_{\zeta_s}H_r].
\]

Substitution of the old forward answers cancels the second term, leaving (5). The new Gaussian source is the projection combination of the old forward sources plus an independent innovation. It has covariance (\mathbb E[HH_r]) with each old forward source and variance (\mathbb E[H^2]). The transposed argument yields (6). Its independence of other oriented source groups is inherited from the independent innovations and the induction; this does not assert independence of actual matrix outputs. Bounded first source derivatives and linear growth justify the integration by parts in this bounded-derivative stage.

### Singular Grams

The perturbation argument in lines 266–272 removes the need for rank stability. A fresh root is added only to the current call's input; it is independent of that input and of the earlier same-orientation query span. Its residual normalized squared norm tends to one because this span has bounded rank. The cross term tends to zero. Each newly enlarged limiting Gram therefore has a positive Schur complement of at least (\varepsilon^2).

For a fixed finite Lipschitz graph, a common-sample coupling propagates (O(\varepsilon)) vector RMS and scalar errors on the stated event of bounded matrix norms and fresh-root RMS. That event has probability tending to one. The constant need not be uniform over program lengths, and the theorem does not require it to be.

Continuity of the evaluator uses only positive semidefinite square roots and dominated convergence, not continuity of inverse query Grams. At each causal step the previously convergent coefficients are bounded, the expressions have common linear growth, and their first source derivatives are uniformly bounded. Coupling a finite source prefix through covariance square roots passes both covariance and response expectations to the limit, including rank loss. Taking (n\to\infty) before (\varepsilon\to0) proves the unperturbed law.

### Clipping, scalar feedback, and all-(L^p) convergence

The cutoff construction in lines 278–314 has uniform polynomial derivative profiles of every fixed order. It clips scalar arguments as well as vector arguments, and it also permits clipping scalar products. Thus each clipped graph satisfies the bounded-derivative law, while the moment lemma is uniform in both width and cutoff.

The proof correctly uses the probability space enlarged by a uniform neuron index. Uniform moments there upgrade an earlier (L^2) error to every fixed finite (L^p) error by interpolation. The polynomial mean-value bound and Hölder then control the propagated coordinate error. The cutoff error tends to zero by a uniform high-moment tail bound, even though the clipped input itself depends on the cutoff. Broadcasting a scalar into this argument is legitimate; Jensen handles averages.

For a matrix call, (19) uses the operator-norm fourth moment and the fourth moment of the input error. It requires no independence of that error and the reused matrix. This closes uniform clipping removal for the complete graph, including causal scalar feedback.

The Gaussian evaluator has matching cutoff convergence by a causal induction on expectation nodes: convergent earlier coefficients and covariance square roots give a common polynomial envelope in fixed standard Gaussians, for values and the finitely many required formal derivatives. Dominated convergence is consequently applicable even at a singular limiting covariance.

The probability triangle argument and the uniform clipping bound yield (O_n\to O_*\) in probability. Choosing any higher finite moment exponent and splitting at a large threshold gives uniform integrability of (\lvert O_n-O_*\rvert^p), establishing (2) for every finite (p\ge1). A finite union of graphs remains a finite graph, so the joint assertion follows.

## Derivative compilation and normalization

Lines 343–417 preserve the finite-width object before applying an asymptotic law. Taylor coefficient extraction through a fixed order only needs smoothness; it does not assume analyticity. Matrix jets of positive order remain finite sums of normalized outer products, and multiplying a represented matrix by a vector expands exactly through (1). A frozen directional derivative and repeated differentiation along a state-dependent vector field are correctly distinguished.

The normalized reverse adjoint (b_u=n\,\partial O/\partial u) gives the factors in (22)–(24). In particular, the scalar adjoint from a coordinate map has an explicit normalized sum, the vector adjoint from an average has no extra (1/n), and a matrix gradient is a finite sum of (b_vu^T/n) or (ub_v^T/n). Contributions accumulate across repeated and transposed parameter uses. The vector mobility (n), matrix mobility one, and normalized contractions in (25) are consistent. They introduce no forbidden width-dependent primitive coefficient after compilation.

Computing the ambient gradient with respect to the current matrix before substituting its stored rank-one representation avoids differentiating the update factors as if they were independent coordinates of that current matrix. Subsequent represented updates and directional derivatives remain finite programs. The first-layer columns and readout in the specified MLP are Gaussian vector roots, while hidden matrices have the separate (1/n) entry variance. Their stated mobilities fit exactly these two cases.

At every finite width the smooth gradient field has a local solution. Formula (26) determines any fixed finite jet without a common positive existence horizon. Its inclusion of the derivative of the vector field is consistent with the displayed second observable derivative. The proof compiles these derivatives before taking width limits and does not exchange differentiation with a limiting expectation or limiting scalar output.

## Restricted activation-moment normal form

The syntactic restriction in lines 421–457 is strong enough for the claimed normal form. Original feedforward preactivations are constructed before reverse queries; their representatives are centered Gaussian sources or linear combinations of first-layer Gaussian roots. Their covariance recursion (27) has the correct first-layer and hidden-layer scaling.

Every later field in this subclass is a finite sum of a Gaussian polynomial times products of derivatives of the activation evaluated only at those designated original preactivations, with coefficients polynomial in previously computed scalar quantities. Formal source differentiation preserves that class, including when a preactivation is a linear combination of original coordinates. Introducing it as an additional integration coordinate does not change the original formal derivative convention.

For the Gaussian integration-by-parts reduction, remove one explicit Gaussian factor from a monomial and apply (29) to the rest. If the derivative hits the remaining polynomial, its degree drops further; if it hits an activation factor, the chosen Gaussian factor is still removed and only the activation derivative order increases. Thus the polynomial degree strictly decreases in every resulting term, proving finite termination. The representation (G=BZ) justifies the same identity for singular covariances without inversion. All functions actually used here have polynomially bounded derivatives, so the boundary and integrability conditions are satisfied.

The residual atoms contain only products of activation derivatives at original preactivations. Covariances used during reduction have already been computed at earlier causal evaluator steps. Substituting the earlier coefficient expressions therefore gives a finite polynomial in recursively computed atoms and fixed constants, with no circular definition or hidden covariance inverse. This conclusion would not cover an arbitrary nonlinear head or a nonlinearity applied to a derivative field, and the candidate explicitly excludes those cases.

## Audit outcome

The checks covered singleton-free moment patterns, repeated raw-entry derivatives, variance-zero entries, matrix and transpose reuse, causal scalar feedback, vanishing or redundant query inputs, singular root and source covariances, clipping after differentiation, the normalization of both parameter classes, fixed update and jet orders, and termination of the restricted Gaussian-moment reduction.

No mathematical correction is required for this frozen candidate. The proof establishes the claimed unconditional limits within its stated language and fixed-order scope. This verdict does not validate the external attribution that another paper independently covers the full language, establish a stronger contraction language, or supply the separate requirements for promotion.
