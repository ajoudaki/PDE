# Isolated adversarial audit: fixed-program softplus identification

## Document identity and audit boundary

- Candidate: `/tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md`
- Exact candidate SHA-256: `875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603`
- Coverage: all 862 lines, including the scope statements, proof, and final qualifications.
- Audit date: 2026-09-06.

This candidate was the only mathematical and contextual input. No cited document, project file, other candidate, or earlier review was read. No external source was consulted, no experiment was run, and no agent was used. General review-procedure instructions supplied no mathematical evidence. Line references below refer exclusively to the candidate identified by the hash above.

## Verdict

**PASS for the stated fixed-program lemma: no required mathematical repair found.** The document supplies a coherent, self-contained argument for empirical convergence in probability, including every fixed continuous polynomial-growth test and every fixed finite Wasserstein order, within each specified neuron population. I found no demonstrated false claim or major proof gap in that mathematical result.

The important potentially difficult steps are actually addressed: adaptive conditioning retains two separately reused Gaussian matrices; both transpose responses are derived; uniform coordinate moments are obtained for the actual feedback program; singular queries are handled by a coupled perturbation of initial-matrix inputs; and empirical contraction feedback is restored by a causal comparison. These conclusions do not require silently importing a general tensor-program theorem, a localization-transfer theorem, or a flow result.

There are two optional exposition improvements below. Neither is a missing hypothesis or a prerequisite for accepting the proof as written. The asserted agreement with equations in other documents is outside this audit and is not certified.

## Precise scope of the pass

The result concerns the program (3)--(4), with fixed finite instruction count, fixed finite caps, fixed deterministic update weights, and fixed `rho` in `[-1,1]`. Its readout update and predictions are uncapped; the caps appear at the locations actually displayed in (3). The proof also covers the stated finite extensions by population-compatible, smooth globally Lipschitz coordinate instructions, deterministic linear combinations, initial-matrix actions, and the specified causal contraction feedback.

For each fixed finite tuple in a neuron population, each fixed continuous polynomial-growth test has its asserted empirical limit in probability. A finite collection of such assertions is joint by a union bound. For each fixed `1 <= p < infinity`, the corresponding empirical measure converges in `W_p` in probability. This does not assert an almost-sure event supporting every test, uniformity in test degree or Wasserstein order, or a pairing of identically numbered neurons in different populations.

No growing mesh, increasing instruction count, cap removal, mesh-uniform response estimate, local or global flow, or gradient-energy identity is needed or established. The omitted primal hypotheses and external-document identities mentioned at lines 852--862 are not conclusions of this audit.

## Claim ledger

| Claim | Candidate evidence | Audit finding |
| --- | --- | --- |
| Actual-program coordinate moments of every fixed order | (14)--(20), lines 232--386 | Sound; the dimension factors in parameter derivatives and scalar feedback cancel correctly. |
| Adaptive Gaussian conditioning for both matrices and both orientations | (21)--(22), lines 388--430 | Sound under the causal, full-transcript interpretation already used by the unrolled graph. |
| Polynomial-growth empirical induction | (23)--(26), lines 432--505 | Sound; projection errors and tails have sufficient control beyond RMS. |
| Independent source groups, uncentered covariances, and complete transpose responses | (27)--(29), lines 507--576; (36)--(41), lines 776--850 | Sound; innovation variance is correctly distinguished from full source variance. |
| Rank-drop removal with separate learned memories | (30)--(33), lines 578--702 | Sound; read the generic response rules with the actual perturbed query inputs. |
| Restoration of empirical contraction feedback | (34)--(35), lines 704--761 | Sound; the oracle is causal and the actual-program comparison uses independently established moments. |
| Continuous polynomial-growth and Wasserstein conclusions | lines 615--637, 685--691, 743--774 | Sound for each fixed test/order and each specified population tuple. |

## 1. Moment and gradient estimates: dimension audit

The available coordinate maps meet the hypotheses used in the proof. Softplus has linear growth and bounded positive-order derivatives. For each cap, the two partial derivatives of `phi'(z) tau_j(v)` are

\[
\phi''(z)\tau_j(v),\qquad \phi'(z)\tau'_j(v).
\]

Both are bounded at fixed caps. Thus these delta maps are bounded and globally Lipschitz, while the feature and readout nodes can have linear growth. The argument does not incorrectly assume the readout or features are bounded. Higher cap derivatives are unnecessary: parameter differentiation and the later source-response argument use only first derivatives of the coordinate maps, and continuity of these derivatives suffices for the limit passage.

The Gaussian rotation proof of (16) is valid. At each rotation angle, the position and velocity are independent standard Gaussian vectors. Conditional on the position, the gradient-velocity inner product is a scalar Gaussian with variance equal to the squared gradient norm. Integral Hölder and conditional Jensen then give the stated dimension-independent bound. Integrability is checked for the finite graphs, rather than assumed uniformly over a growing parameter dimension.

The matrix tail estimate is also sufficient. Two `1/4` nets give at most `9^(2n)` bilinear forms, the approximation factor is two, and a fixed bilinear form has variance `1/n`. The resulting first bound in (18) implies its second bound for `t >= 10`. Integration gives uniform moments of the operator norms. Together with Gaussian root RMS moments, this proves the claimed uniform moments of `K_n`.

The crucial normalization checks in (19) are as follows. Write `a` for a direction in the vector of all standard Gaussian parameters. Since initial-matrix entries are scaled by `n^(-1/2)`,

\[
\|D W_0[a]\|_{\rm op}
\le \|D W_0[a]\|_F
\le n^{-1/2}\|a\|_2.
\]

Consequently,

\[
\|D(W_0x)[a]\|_2
\le \|W_0\|_{\rm op}\|Dx[a]\|_2
     +\|a\|_2\|x\|_{n,2}.
\]

The transpose has the identical bound. There is no factor of `sqrt(n)` left in this matrix-action differential.

For a normalized contraction,

\[
|D\langle x,y\rangle_n[a]|
\le n^{-1/2}
 \bigl(\|y\|_{n,2}\|Dx[a]\|_2
       +\|x\|_{n,2}\|Dy[a]\|_2\bigr).
\]

Polynomial scalar arithmetic preserves that `n^(-1/2)` factor. When the resulting scalar multiplies a vector, its differential is multiplied by `\|x\|_2 = sqrt(n)\|x\|_{n,2}`; these factors cancel. This proves the asserted finite-graph derivative induction without regression inverses and without an illicit Gaussian-matrix `L^p` operator estimate.

Finally, permutation equivariance within each population converts the RMS second-moment bound into a bound on each coordinate's second moment and mean. The coordinate gradient norm is bounded by the vector differential operator bound in (19). Applying (16) therefore yields (20) at every fixed order. The argument covers the actual empirical-feedback graph, fixed-coefficient oracles, and their input-noise versions uniformly in `epsilon` in `[0,1]`. This is an independent moment estimate, so its later use in feedback and perturbation transfer is not circular.

## 2. Adaptive conditioning with two reused matrices

For fixed old observations `WV=Y` and `W^T U=Q`, the mean in (21) lies in the sum of the two linear constraint spaces and satisfies both constraints. The compatibility relation `U^T Y=Q^T V` makes the second constraint hold. The map

\[
A\longmapsto P_{U^\perp} A P_{V^\perp}
\]

is the orthogonal projection, for the Frobenius inner product, onto the common homogeneous constraint space. Isotropic Gaussian conditioning therefore gives precisely (21). Separate full column rank of `U` and `V` suffices; independence of the two constraint families is not being assumed.

The adaptive justification at lines 409--414 is adequate when applied inductively. Conditional on the entire preceding transcript and the revealed roots, the next input is fixed. Its answer is a linear observation of one conditional residual matrix only. Starting from independent initial matrices, the two posterior residual laws thus remain conditionally independent: observing one of them does not further constrain the other after the previous transcript is fixed. This remains true when an input was computed using previous answers from both matrices.

This statement concerns conditional residual independence, not independence of the trained matrices or of all generated fields. The proof does not replace a reused transpose by a fresh independent matrix. The swapped version of (21)--(22) applies to each transpose with its own observation history.

The transcript must include the raw initial-matrix action nodes of the unrolled graph. Section 3 explicitly introduces this graph, so those nodes are available. A trained answer can equivalently be reduced to its raw action by subtracting its known learned rank terms. See optional clarification O2 below.

## 3. Conditional averaging and projection control

For a transcript-measurable rank-at-most-`J` projection, (23) gives

\[
\mathbb E[\|\sigma P g\|_{n,p}^p\mid\mathcal F]
 =\frac{m_p\sigma^p}{n}\sum_iP_{ii}^{p/2}
 \le\frac{m_pJ\sigma^p}{n},\qquad p\ge2.
\]

The inequality follows from `0 <= P_ii <= 1`; it does not require individual leverage scores to vanish. The residual input norm satisfies `sigma <= \|h\|_{n,2}`, whose moments are already controlled. For `p < 2`, the normalized `L^2` bound suffices. Thus dropping the projection is justified in every fixed empirical `L^p`, including for unusually concentrated projection subspaces.

After the projection is dropped, the fresh Gaussian coordinates are conditionally independent. On bounded-coefficient events the conditional variance bound (24) is correct. Positive definite limiting Grams imply convergence and tightness of the regression coefficients; their inverse moments are not needed. The conditional variance bound, combined with tightness of the old empirical moments, gives concentration in probability even though those coefficients can be large on exceptional events.

The Gaussian-integrated test is continuous and has polynomial growth uniformly on compact coefficient sets. Converging random coefficients can therefore be replaced by their deterministic limits using compact-set uniform continuity and (25). The original graph supplies moment bounds for the projected answer, while tight coefficients, old empirical moments, and fresh Gaussian moments supply bounds in probability for the answer with its projection dropped. This closes the induction for arbitrary continuous polynomial-growth tests, not just polynomials or differentiable tests.

## 4. Source law, uncentered covariances, and both responses

The cancellation in Section 5 is correct. If `alpha` is the least-squares coefficient of the new forward input on old forward inputs, then

\[
h_\perp=h-\sum_r\alpha_r v_r
\]

is orthogonal in the uncentered `L^2` inner product to every old forward input. Each old raw reverse answer is its reverse source plus a linear combination of such inputs. Hence

\[
\mathbb E[q_s h_\perp]=\mathbb E[\zeta_s h_\perp].
\]

Gaussian integration by parts yields

\[
\beta
=\mathbb E\nabla_\zeta h
 -\sum_r\alpha_r\mathbb E\nabla_\zeta v_r.
\]

Substitution into `Y alpha + U beta` cancels the old response contributions and gives (27). Interchanging the two populations proves (28), with a separate history for the matrix under consideration. The other matrix's earlier effects are present in the complete coordinate expression being differentiated.

If `Gamma_V = E[vv^T]`, the source constructed in this calculation is

\[
\xi_h=\sum_r\alpha_r\xi_r+\|h_\perp\|_{L^2}g_{\rm new}.
\]

Therefore

\[
\mathbb E[\xi_h\xi_r]=\mathbb E[h v_r],\qquad
\mathbb E\xi_h^2
=\alpha^T\Gamma_V\alpha+\mathbb E h_\perp^2
=\mathbb E h^2.
\]

These are uncentered input second moments, as required for a zero-mean Gaussian matrix acting on possibly nonzero-mean features. The innovation variance is the residual input second moment; the full source variance is the full input second moment. Subtracting a response variance from the latter would be incorrect, and the candidate does not do so.

Each newly constructed source is a deterministic linear combination of older sources in its own orientation group plus a fresh independent Gaussian. This preserves independence of the four Gaussian groups and independence from the root variables. It does not imply that a generated field is independent of its response factors. The independent population realization in lines 143--148 is consistent with the absence of cross-population empirical pairings.

The needed Gaussian integration-by-parts identity is proved in (29). With deterministic coefficients fixed, the scalar coordinate expressions have linear growth and bounded first derivatives. These properties justify the integrations and expected derivatives. No unstated nonclassical response theorem is required here.

## 5. Causal order and current-step derivatives

The order at lines 214--218 makes the displayed scalar recursion explicit. The first-layer update uses past bottom answers. A current layer-2 forward input uses past bottom information, and a current layer-3 forward input uses the current layer-2 forward answer. Current reverse layer-3 coefficients can then be selected before constructing the current layer-2 reverse answer; that answer is available before computing the reverse layer-2 coefficients. All expectation selections consequently use already available input expressions.

Equations (36)--(40) retain the relevant chain-rule terms. In particular:

- A derivative of the top delta through a past source includes the readout derivative and `tau'_w`.
- The current readout derivative is zero, while the current top preactivation derivative is the formal sample Kronecker delta. This gives (38).
- The current middle reverse answer depends on the current middle features through `B^(3)`. Differentiating this dependence produces the second term in (40), including `tau'_2`.
- The bottom update uses `C_ab` and the capped bottom delta, whose derivative is (41).

Thus the return through the top matrix is not omitted in the second transpose. Covariance between the two samples does not change a formal partial derivative into a covariance-weighted derivative. Holding selected contraction values and deterministic coefficients fixed is justified by the separate oracle comparison, audited below.

## 6. Rank drops and learned memories

The input-noise construction at lines 580--591 gives each new query positive `L^2` distance from the previous same-orientation span. Its fresh root is independent of both the query before adding that root and that span. The squared residual distance is therefore its previous value plus `epsilon^2`. This establishes positive limiting Schur complements for fixed positive noise. At sufficiently large finite width, the fresh Gaussian vector also prevents exact column dependence almost surely.

An essential distinction is that the histories in the conditioning and source rules contain the **perturbed matrix queries**, while learned factors remain the separately computed feature and delta nodes with no direct additive input noise. To make the audit explicit, suppress layer indices and write

\[
V_r^\epsilon=H_r^\epsilon+\epsilon a_r,
\qquad U_s^\epsilon=\Delta_s^\epsilon+\epsilon b_s.
\]

For a fixed-coefficient oracle, a forward total consisting of a raw queried action plus learned terms has the generic scalar representation

\[
\Xi_t^\epsilon
 +\sum_s U_s^\epsilon\,
       \mathbb E[\partial_{\mathcal Z_s}V_t^\epsilon]
 +\sum_r c_{tr}\Delta_r^\epsilon.
\]

Here `mathcal Z_s` denotes the reverse Gaussian source slot. The reverse representation analogously has Gaussian-response multipliers `V_r^epsilon` and learned multipliers `H_r^epsilon`. Source covariances are the Gram matrices of `V^epsilon` or `U^epsilon`, respectively. In particular, one must retain any auxiliary-root cross moments generated by earlier instructions; the covariance cannot in general be obtained by adding only a diagonal `epsilon^2` to the original law.

This is the interpretation of the generic rules (27)--(28) applied to the graph described in Section 6. The candidate does not claim that the positive-noise law is literally (6)--(13) with only changed variances. Nor does it substitute noisy query vectors into the learned rank factors. “No noise into learned factors” means no direct additive query-noise term there; those factors still change indirectly as the perturbed graph evolves. These distinctions make the construction consistent. Making them explicit would improve exposition, but no new estimate is required; see O1.

The finite-width comparison (30) follows by the same finite graph induction as (19): matrix actions use the original shared matrices, coordinate maps are globally Lipschitz, contraction differences satisfy (31), and scalar-times-vector differences are controlled by the RMS bounds. All additional roots are included in `K_n`. The resulting `epsilon P(K_n)` bound has uniform moments.

For every fixed `p > 2`, (32) combines this small RMS error with a uniformly tight higher empirical moment supplied by (20). For `p <= 2`, RMS suffices. This proves (33), including its uniformity over widths; it is not an inference of high-moment closeness from RMS alone.

The scalar rank-drop passage also avoids inverse covariance limits. Earlier coefficients converge inductively. On compact coefficient sets the relevant expressions have uniform linear growth and continuous bounded formal first derivatives. Continuity of positive semidefinite square roots, proved in lines 658--669, couples converging finite Gaussian source laws even at singular covariance matrices. Gaussian moment bounds give convergence of inputs in every finite `L^p`; dominated convergence gives convergence of the expected formal first derivatives. New covariances remain positive semidefinite because they are query-input Gram matrices.

Keeping formally distinct slots is necessary and valid. If a covariance is `Gamma = E[uu^T]` and `a` is in its kernel, then `u^T a=0` almost surely. The singular Gaussian integration-by-parts identity determines expected derivative coefficients modulo that kernel, and the contracted response is invariant under precisely this ambiguity. This supports zero initial reverse queries, redundant queries, and `rho=+/-1`. It does not require the individual formal derivative coefficients to be unique under arbitrary off-support redefinitions.

## 7. Actual empirical contraction feedback

The learned rank expansions (34)--(35) are exact, including their `1/n` contractions and strict past-step learned sums. They have the correct orientations: forward learned terms multiply past deltas by feature contractions, while reverse learned terms multiply past features by delta contractions.

The oracle construction in lines 721--727 is causal. A contraction can be selected after both of its inputs exist. Where a raw matrix answer is needed first, its law can be constructed first and the learned addition made afterwards. There is no fixed-point equation for a current feedback value. Sections 4--6 apply to every finite prefix with the previously selected coefficients held deterministic.

On `K_n <= L`, the actual and oracle graphs have bounded RMS norms and bounded scalar values. At a contraction node, decompose the discrepancy into the actual-versus-oracle empirical difference controlled by (31), and the oracle empirical-versus-limiting-expectation error. Every other instruction propagates these discrepancies with a bounded constant on this event. A finite causal induction bounds all RMS discrepancies by a constant depending on `L` times the sum of finitely many oracle contraction errors. Each error converges in probability to zero. Uniform moments of `K_n` then remove the localization event.

This argument needs no concentration estimate for inverse Grams, no small step size, and no derivative of the operation selecting an empirical contraction. The actual and oracle graphs independently satisfy (20), so interpolation and tail truncation upgrade their RMS comparison to all stated tests. The feedback conclusion is therefore about the actual finite-width program, not merely an oracle surrogate.

Combining the raw-action responses with the exact learned terms yields the two parts of (12)--(13): the expected formal derivative and the appropriate learned contraction. The current learned contribution is absent, while the current transpose response remains present. The prediction is a within-population normalized contraction and is covered as well.

## 8. All continuous polynomial-growth tests and Wasserstein orders

The test extension has the required two ingredients. For any fixed degree `d`, a higher empirical moment of order `q>d` controls the tails via (25). On a fixed ball, continuity gives a uniform modulus; a small empirical `L^p` discrepancy controls the fraction of coordinates separated by more than any fixed positive amount. Together these facts transfer a test between close tuples without requiring the test to be differentiable, globally Lipschitz, or a polynomial.

These ingredients are available at each comparison: restoring the Gaussian projection, removing input noise, and comparing actual feedback with the oracle. The scalar expectations also converge under noise removal, by the established finite-`L^p` convergence and higher-moment uniform integrability. Thus the empirical and scalar sides of the triangle inequality at lines 685--691 are both justified.

For `W_p`, use a higher moment `q>p` to control empirical `p`-tails in probability; the limiting law has the corresponding moments. On a fixed large ball, bounded continuous test convergence implies convergence of masses of a finite partition whose boundaries have zero limiting mass. Matching mass within small cells, then the vanishing unmatched bounded mass, controls the bounded part of the transport cost. Moving tails through the origin contributes at most a constant times their `p`-moments. This proves the claimed convergence in probability. The finite number of tests needed for any chosen partition avoids an uncountable-test quantifier issue.

## Required versus optional

**Required repairs: none found for the precise fixed-program result audited here.** No fatal or major flaw is assigned. In particular, none of the specifically audited issues needs an extra nonclassical theorem to close the proof.

**O1 — Optional: display the positive-noise law with separate names for queries and memories.** At lines 580--589 and 641--656, explicitly distinguish `V^epsilon,U^epsilon` from the feature/delta memory nodes. State that (27)--(28) use the former for source covariances and Gaussian-response multipliers, while learned rank terms use the latter. The generic argument already entails this distinction; a displayed formula would prevent an incorrect implementation or reading of the perturbation.

**O2 — Optional: specify raw-action transcript notation next to (21).** State that `Y,Q` are answers of the initial matrix before explicit learned sums are added, and that the transcript includes revealed roots and all previously computed nodes. The unrolled graph already supplies this information, so this is an exposition improvement rather than an additional probabilistic assumption.

## Verification limits

The pass is based on a full analytic inspection and re-derivation of the high-leverage steps above. It certifies neither correspondence with the external files named by the candidate nor any result outside the displayed finite-program scope. Those external assertions were deliberately left unchecked under the single-document restriction. Within the audited proof, I found no unproved heavy external reliance masked by those references.
