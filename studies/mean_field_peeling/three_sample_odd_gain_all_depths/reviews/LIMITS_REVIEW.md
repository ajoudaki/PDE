# LIMITS review of the frozen all-depth odd-gain candidate

Date: 2026-09-08. Verdict: **PASS** for the theorem actually stated in the frozen candidate, including all fixed-finite-depth population and finite-algorithm conclusions. No blocking proof gap or counterexample was found. This verdict does not establish the exact unit-sum convex-mixture theorem or an activation family allowing only a small additive offset.

The reviewed activation is exactly

\[
\phi_\delta(z)=a_\delta(z+\arctan z),\qquad
a_\delta=324\pi e\,10^{10}\delta^{-2}.
\]

The same gain works for every fixed finite hidden depth \(L\ge2\). The width limit fixes the dataset, depth, gain, and physical horizon first. Constants in the observation bridges are allowed to depend on those fixed quantities. No conclusion uniform in growing depth or interchangeable infinite-time/width limits is certified.

## Frozen identity and review coverage

All five files agree with `CANDIDATE_HASHES.json`. Their independently checked SHA-256 values are:

| File | SHA-256 |
|---|---|
| CONTRACT.md | `219ea670b8e19a8d350ca74003fc9dc46933ce64563d199bbb4bef55fe644d90` |
| PROOF.md | `e8088b9554332c2d45250dec5e1b0004badb0252e5cfe63cefde0f8896e59f66` |
| SOURCE_RESPONSE.md | `c4dd77974660a1c7f556042f748c348af1fd3c2953d2e7220d508ee0960286f9` |
| INITIAL_MOTION.md | `dc4260ff571a3182362af01606706d7e0077d34d7552f0192ab340333a5fb12d` |
| POPULATION_LIMITS.md | `e7982d74e4004973ac3cdaa20715c9ad70fb9fd4ba04ad5b36e78fa8a222713c` |

The manifest itself has SHA-256 `4072431af0dbd76655338f704f133a1dbd396b7e32b3ed49db16552bf19f969e`.

I read all five candidate documents, the substantive proofs in `three_sample_self_contained/foundations.md` and `velocity.md`, and the initialization-geometry antecedent, especially its Sections 4–6. The dependency snapshots checked here are:

| Dependency | SHA-256 |
|---|---|
| ../three_sample_self_contained/foundations.md | `d4ec349056af9a265cf583a5e6196a8d17d1ae4eed4e764a85a1e9b59345dc55` |
| ../three_sample_self_contained/velocity.md | `36c8f3e5b89d766cf1137ab6fd21346a978272e407400249194c1ed132d20184` |
| ../odd_mixture_separation_quantitative/THREE_INPUT_GEOMETRY.md | `5b5788fcf61ca350c31ca36868bbb0eed9d86f88dcafb36348632a443b8c45dc` |

The review uses mathematical derivations and source inspection. No experiment was run, and no candidate mathematics was modified. Prior review verdicts are not premises of this verdict.

## 1. Exact raw model, normalization, and initialization

The raw metric gives a first-weight gradient factor \(1/d\), a hidden matrix update \(b\,h^T/n\), and readout gradient \(h\). Consequently the first kernel block is \(\Gamma_{ij}\langle b_i^1,b_j^1\rangle\), each middle block is the product of the backward and previous-feature contractions, and the readout block is the top feature Gram. There is neither an omitted width factor nor an extra gain in those formulas.

Writing \(z^\ell=a^{\ell-1}Z^\ell\) and \(h^\ell=a^\ell H^\ell\) gives

\[
H^\ell=\psi_\ell(Z^\ell),\quad
\psi_\ell(z)=z+a^{1-\ell}\arctan(a^{\ell-1}z),\quad
f_i=a^L\langle C,H_i^L\rangle.
\]

All raw parameters, including \(C\), are retained. Every raw gradient of \(f_i\) is \(a^L\) times the corresponding gradient of the normalized scalar predictor. The time change \(s=a^Lt\) and accumulated clock \(v=a^L\int\|r\|_1dt\) therefore reproduce the original physical flow exactly. The normalized incoming field at layer \(\ell\) corresponds to the original one multiplied by \(a^{L-\ell}\), so the layer-dependent auxiliary clipping convention is also consistent.

The actual finite readout has \(E\|C_n(0)\|_n^2=n^{-2}\). Its zero population limit is justified by a same-width fixed-cap Lipschitz comparison with discrepancy \(O_{\Pr}(n^{-1})\); actual finite GF and GD retain the nonzero Gaussian initialization throughout subsequent comparisons. The bottom substitution \(w=\sqrt d\,W^1\), \(u_i=x_i/\sqrt d\) is an isometry for the first raw metric block.

## 2. Foundations and the extension from two to finitely many adjacent matrices

The load-bearing finite-program theorem is proved in foundations F.1–F.6 for fixed finite instructions with bounded continuous first coordinate derivatives, Gaussian roots, matrix calls in both orientations, and causal locally Lipschitz scalar feedback. The candidate satisfies these hypotheses at each fixed cap: \(\psi_\ell\) has bounded derivative, and \(D_{\ell,R}\) has bounded continuous first derivatives for fixed \(L,a,R\). Residuals are continuous inner products followed by locally Lipschitz scalar operations. Normalized residual controls are frozen only after their deterministic values are obtained; the actual finite feedback is not replaced in the algorithm.

The proof of the Gaussian-program theorem depends on the instruction count, not on having exactly two initialized matrices. Conditional on the full transcript, a call adds a linear constraint to the queried matrix; the other conditionally independent residual matrix factors remain untouched. The conditional unused block is the doubly projected Gaussian matrix. Finite-rank removal of fresh output noise costs rank divided by width. Adding finitely many independent matrices therefore preserves this induction.

Singular query Grams are handled by independent noise at every query input. At fixed noise each new Schur complement is positive; the finite-array perturbation error is controlled by operator norms without inverse Grams. The scalar recursion is continuous through covariance square roots and bounded formal derivatives. The argument consequently passes to singular covariance without assuming continuity of a pseudoinverse. Named opposite-orientation slots stay separate, and their contracted corrections remain invariant on a singular support.

The sharper spectral-norm input in POPULATION_LIMITS Section 1 was checked against the cited [Vershynin book, Theorem 7.3.1 and Corollary 7.3.3](https://anthonyhongxiao.github.io/pdfs/HDP-book.pdf). Their hypotheses are precisely independent standard Gaussian entries; scaling the square matrix by \(n^{-1/2}\) gives the high-probability norm-three event and the limiting norm-two bound used here. A finite union handles every fixed depth.

The common generated probability spaces and genuine adjoints follow from finite-program consistency, density of bounded smooth cylinder functions, the transferred norm inequality on the generated span, and the finite transpose pairing identity. No arbitrary bounded operator is substituted for Gaussian initialization. Only learned increments are Hilbert–Schmidt; their rank-one normalization agrees with the finite Frobenius metric. These constructions supply the common Hilbert space needed for strong cap comparisons and restart.

## 3. Global clipped construction and source estimate

The stopped primal estimates use only bounded actions, \(|\psi_\ell(z)|\le2|z|\), \(|D_{\ell,R}(z,q)|\le2|q|\), and readout integration. They do not borrow a gradient energy identity for the clipped field. The first-exit displacement estimate and the discrete identity bounding \(\sum_jh_jv_j\) supply strict continuous and Euler slack independently of the source estimates.

The cubic tensor separation gives \(\Gamma^{\circ3}\succeq\delta^2I/3\), including singular input Grams. The cubic arctangent coefficient has squared magnitude at least \(\eta_0=1/(108\pi e)\) for every Gaussian standard deviation at least one. The normalized first feature Gram is therefore at least \(\lambda I\). Equal marginal variances and the first-chaos regression coefficient at least one propagate that same floor through every initialized depth.

The pathwise forward displacement and hidden Jacobian bounds give

\[
Q_L\succeq\tfrac34\lambda I,
\qquad\|J_hU_{h,R}\|_{\mathrm{op}}\le\tfrac14\lambda.
\]

The hidden contribution need not be symmetric or positive; the norm bound is sufficient in the exact clipped residual equation. It produces the stated physical loss rate and total residual clock at most \(S/2\), excluding the controlled-clock stop. Uniform primal and speed bounds then give strong finite-time endpoints and continuation of each locally Lipschitz clipped flow.

SOURCE_RESPONSE's same-array Gaussian decomposition is essential and valid: it compares the actual nonlinear fields with Gaussian combinations at the same actual coefficient arrays. The bounded forward remainder contributes \(b/K_\ell\), which compensates the derivative factor \(K_\ell\). Actual raw \(L^2\) bounds control the Gaussian part before a higher-moment conclusion is drawn. Absorption uses \(\alpha S b\le1/8\), and Minkowski controls marginal norms without time independence.

The source Jacobian equation retains current reverse returns. Strict forward response order prevents a same-time inversion. Its Volterra envelope controls both forward production and the terminal incoming-field factor in reverse production. Weighted Jensen and the marginal subGaussian bound justify the exponential envelope; no random time-maximum estimate is used. The explicit box has

\[
\alpha_\ell S b_\ell
\le24576(1048576/a)^L64^{-\ell}T^2/a,
\]

and the gain hypothesis makes both this quantity and the random-derivative exponential parameter small uniformly over finite \(L\ge2\). Forward rows use earlier reverse history; reverse rows are generated downward after their current higher reverse row. The strict box improvements thus close by chronological induction, without a circular bootstrap or a smallest-mesh-step denominator. Applying this construction to fine clipped physical Euler meshes is legitimate after the strict residual-clock bound has been obtained.

## 4. Strong cap removal, asymmetric uniqueness, and restart

Equation (25) is a correct asymmetric gate comparison. Changing the first incoming field uses the uniform derivative bound in that variable. The preactivation difference is multiplied by the reference clip, and the remaining error is a tail of the reference incoming field only.

At arbitrary fixed depth, downward backward substitution multiplies an existing backward discrepancy by a bounded action and a bounded incoming derivative. A newly introduced factor \(R\) always multiplies an independently controlled forward discrepancy. Thus the constant grows linearly in \(R\), not as \(R^L\). The resulting \(e^{C_TR}\) stability loss is defeated by the proved \(e^{-cR^2}\) reference tails.

Uniform Cauchy convergence of both raw states and raw directions on compact intervals gives a strong \(C^1\) limit. The same asymmetric inequality identifies its direction with the uncut field. Bounded multiplier continuity and the bilinear action chain rule justify all forward derivatives. Repeated genuine adjunction identifies the raw scalar gradient, and the energy identity belongs to the resulting true flow.

The comparison against another strong solution uses only that competitor's compact-interval primal bound. It does not require sample symmetry or its own subGaussian tails. At a reached state the initial discrepancy from a clipped reference already has Gaussian-small size; multiplication by another linear-cap Gronwall exponential still tends to zero. This proves the declared nonsymmetric uniqueness and reached-state restart class, without asserting local uncut well-posedness at every arbitrary ambient \(L^2\) state.

## 5. Finite GF and simultaneous raw GD

At fixed cap, a fixed coarse Euler transcript has the required full-sequence empirical laws. Exact sums of rank-one update lengths bound its finite matrix norms and place it in a deterministic enlarged primal ball with high probability. This uses primary fixed-program laws, not an assumption about growing transcripts.

On that ball, the raw capped field has width-independent Lipschitz and norm bounds. The local Euler error is \(L_0M_0h^2/2\); a stopped comparison with the coarse interpolant closes the finite first-exit argument. Width is taken first at a fixed coarse mesh, then that mesh is refined. The actual raw GD step \(n^{-2}\) contributes only a vanishing deterministic consistency error. Hidden quantities and velocities are recomputed from the raw interpolation, with its actual preceding-node raw direction.

For the uncut finite algorithms, the reference-only cap comparison uses finite clipped incoming tails. Their uniform-time convergence is supplied by the fixed-cap observation bridge and continuous tail truncations. Large fixed cap precedes the width limit; then the cap is removed. The discrete comparison has the same single cap factor. Full-sequence convergence in probability follows from the fixed-program full-sequence law and these deterministic comparisons, rather than from an unidentified subsequential population solution.

## 6. True kernels, appended velocities, and path topology

The existing velocity proof V.3–V.11 has been checked at the points requiring more than raw state convergence. Its fixed-cap source-response bounds come from Gaussian answer probes, with all residual feedback recomputed at finite width. The limit derivative freezes deterministic coefficients exactly as foundations requires. Continuity of expected derivatives at a fixed perturbed transcript uses bounded coordinate derivatives and covariance-square-root coupling.

Expected signed derivative rows are first bounded by probes; pointwise absolute derivative rows are bounded separately by a Volterra inequality. The extension through finitely many layers is valid because current reverse responses are a finite downward substitution, while every forward response is strictly past in time. This yields the fixed-cap primary moments needed for the first appended velocity query.

Each higher velocity query uses the previous layer's already proved \(L^2\) velocity norm as its Gaussian source variance. Its return coefficient differentiates only in the appropriate reverse source group; a new forward source is a separate formal argument. Bounded primary derivative rows and the incoming velocity yield an integrable envelope. This induction establishes the next moments before using them above. It assumes no \(L^p\)-operator bound for an initialized matrix.

The product \(\phi'(Z)P\) is not treated as a bounded-derivative instruction. Ordered nested clips make each finite transcript legal; inner clips are removed while the current outer clip remains fixed, then the outer clip is removed using the previous step's established moments. This remains a finite induction for each fixed \(L\).

True backward fields observed at clipped states receive their own descending truncation and bounded-action closure. The resulting kernel limits concern all \(L+1\) true raw gradient blocks, including off-diagonal contractions, rather than clipped-update Grams.

The deterministic velocity comparison has one observation-cap factor multiplying the forward state error. At fixed training cap, moment bounds supply a uniform time modulus and convergence from finite time nets. During training-cap removal, compactness of the uncut continuous \(L^2\) velocity image supplies uniform tail removal. This avoids multiplying a possibly uncontrolled cap-dependent moment constant by the cap-removal error.

Finally, joint finite-time laws are strengthened to path-space laws using the coordinate interpolation estimate

\[
\|X-I_hX\|_\infty^2\le4h\int_0^T|X'(t)|^2dt.
\]

Averaging under same-neuron coupling and using bounded integrated RMS speeds controls both finite and population path interpolation errors. This proves \(W_2\) convergence in the uniform path norm and finite path second moments. Uniform-time state/velocity \(W_2\) convergence also gives the specified second moments and integrated squared speeds. The argument does not confuse a supremum of marginal moments with the moment of a random time supremum.

## 7. Nonaffinity, every individual acceleration, and the changing kernel

The square root of the optimal affine-regression error for \(\arctan X\) is one-Lipschitz under \(L^2\) coupling: every optimal slope lies in \([0,1]\), so the corresponding residual function has Lipschitz constant at most one. The initialization cubic bound and original-coordinate displacement estimate therefore give the uniform absolute nonaffinity claim after multiplication by \(a^2\).

INITIAL_MOTION retains the actual transpose returns and proves a positive definite top backward Gram from full Gaussian support and the nonconstant positive derivative. Each lower reverse innovation has the full positive covariance of the already established upper backward Gram, conditionally on its forward tuple. This proves all hidden block directions and every bottom sample direction nonzero even when the input Gram is singular.

For each upper sample, the added forward query has a Gaussian residual after regression on the three original forward sources. Its variance is the squared distance of the incoming feature direction from the original feature span. Conditional variance provides a strictly positive bottom seed, and the positive derivative propagates it through every layer. The exact return formula leaves all other terms measurable in the original forward and separate reverse variables, so this residual cannot cancel. Finite-transcript truncations and the explicit bounded derivative coefficients justify the source identities used here.

The trajectory bridge then gives \(C'(0)=3H\), \(b_i^\ell(t)/t\to3\beta_i^\ell\), and each hidden raw direction divided by \(t\) converges to \(9V^\ell\). Strong forward chain rules establish actual right second derivatives for each sample's preactivation and feature fields. The readout-kernel and hidden-kernel contributions each supply \(9t^2\|V\|^2\), yielding the exact coefficient \(18\|V\|^2>0\). No symmetry or scalar-residual reduction is needed.

## Disposition

No repair to the frozen mathematics is required by this review. Freezing dependency hashes alongside the candidate hashes would improve reproducibility; this report records them without changing the candidate. The theorem's large overall gain, absolute rather than relative nonaffinity, fixed finite depth, and compact-time width limits are substantive scope restrictions already stated correctly in the contract and proof.

**Final verdict: PASS for the complete stated odd-gain theorem. The exact unit-sum convex-mixture problem remains outside this verdict.**
