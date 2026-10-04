# Internal reconstruction of the quantitative Gaussian-program route

2026-10-01. Scoped internal mathematical check, not a promotion review. No experiments or other-study inputs were used. The assigned candidate files were read completely. The relevant setting, conditional Gaussian proof, population operator construction, uniform Euler carrier estimates, reference comparison, initialization event, and tracking damping calculations in the assigned paper were also read.

Initial frozen versions checked (final accepted hashes appear at the end):

| File | SHA-256 |
|---|---|
| `PROGRAM_RATE_ROUTE.md` | `953d40311d3edc0e4c9d5d978b207ae1d6a992d0301c55db134ff6491847558c` |
| `TRANSFER_DERIVATION.md` | `c76e5c0d00da6867f835c8d83135fa839b9926ee7c75a7f371f32c03e4b0672d` |

The supervisor subsequently proposed an activity-damped transfer in a message. That proposal was independently reconstructed below; it was not present in these two frozen versions.

## Verdict and exact scope

No substantive mathematical defect was found in the finite-program regularization, conditional coupling, exponential constant budget, or the stated slow all-time transfer. The difficult bridges are reconstructed below rather than accepted from the displayed candidate estimates. The activity-damped refinement also works and supports a negative power of `log n`, under the same program lemma and the paper's small-label population construction.

This conclusion is relative to the current paper's constructed common population operators, existence theorem, and uniform small-activity Euler carrier bounds. It is not a new independent review of every response-cap estimate in that foundational theorem. The quantitative use of those results, including regularization bias and the growing-program coupling, was checked here. No polynomial rate in width, sharp nonlinear rate, or unconditional initialization RMS rate is established.

During the review, the bounded-domain program-budget wording and the descriptions of recomputed backward-node errors required correction. A net with polynomially many points in `K` need not fit into one `N<=C K^3` program for arbitrary fixed input dimension; separate single-probe estimates and a union bound resolve that issue. Backward-node discrepancies also contain the comparison-cutoff tail `exp(-cR^2)`, which cannot be absorbed into a polynomially small width error. The final versions distinguish that term explicitly. The empirical-test wording was clarified so that a signed pairing retains its scalar error estimate, whereas a squared-tail test yields a norm error by taking a square root. All these corrections are closed in the final frozen versions listed below.

## 1. Adaptive conditioning and the coupling filtration

For one initialized matrix, after the previous calls its constraints are `WV=Y` and `W^T U=Q`. Conditional on the whole revealed transcript, the remaining matrix component is Gaussian on the homogeneous constraint space. The mean and residual are

\[
Y(V^TV)^{-1}V^T+
U(U^TU)^{-1}Q^TP_{V^\perp}
+P_{U^\perp}\widetilde W P_{V^\perp}.
\]

The two mean terms solve the constraints because `U^T Y=Q^T V`; their difference from any other solution lies in the orthogonal homogeneous space. At an adaptive call, the query is measurable after exposing its fresh independent root. That root reveals no information about any matrix. Conditional independence of the distinct residual matrix factors therefore persists after the new linear observation.

For `h_perp=h−V alpha_n`, the exact new answer is

\[
Y\alpha_n+U\beta_n+\sigma_nP_{U^\perp}g,
\quad
\alpha_n=(V^TV/n)^{-1}(V^Th/n),
\quad
\beta_n=(U^TU/n)^{-1}(Q^Th_\perp/n),
\quad
\sigma_n=\|h_\perp\|/\sqrt n.
\]

One may expose a full standard Gaussian `g` by supplementing its visible projected part with independent noise in the removed subspace. The supplement contains no additional information about an unobserved matrix component. Thus adding the full `g` to the coupling filtration does not invalidate subsequent conditional Gaussian formulas. If the variance vanishes, use a wholly independent `g`.

The scalar reference recursion uses the same fresh `g` coordinates but deterministic population regression coefficients. Every new scalar tuple at a layer is therefore a coordinatewise deterministic map of that layer's previous iid tuple and fresh iid Gaussian coordinates. It remains iid across coordinates within the layer. No independence of the actual trained coordinates is asserted or used. Correlations across layers are irrelevant to empirical concentration of same-layer pairings, and later reverse calls retain the previous responses through their regression means.

## 2. Regularization removes the singularity quantitatively

At each call write `h=h_0+epsilon chi`, where the new scalar root is independent of the entire earlier program and of `h_0`. Its component is orthogonal in `L^2` to every previous same-orientation query. Hence each successive query-Gram Schur pivot and each new population innovation variance is at least `epsilon^2`.

The common population operator norm and coordinate Lipschitz constants give the elementary RMS envelope

\[
B=(CN^2)^{N+1},\qquad \log B=O(N\log N).
\]

For a query list of length `p<=N`,

\[
\det G_p\ge\epsilon^{2p},\qquad
\operatorname{tr}G_p\le pB^2,
\qquad
\lambda_{\min}(G_p)\ge
\frac{\epsilon^{2p}}{(pB^2)^{p-1}}.
\]

With `epsilon=exp(−N^2)`, its logarithmic reciprocal is at most
`2N^3+O(N^2 log N)`. Thus `gamma=exp(−CN^3)` is a valid lower bound. This determinant estimate is essential: a pivot floor alone does not give an equal eigenvalue floor.

The original and modified population programs can be put on the common initialized operators by taking their finite union. At every corresponding original carrier product,

\[
\|g(Z)\operatorname{clip}_N(P)-g(\widetilde Z)
\operatorname{clip}_N(\widetilde P)\|_2
\le jN\|Z-\widetilde Z\|_2+s\|P-\widetilde P\|_2.
\]

Clipping the original carrier costs at most `C exp(−cN^2)` by the uniform Euler tail estimate. Adding a fresh matrix-input root costs at most `K_0 epsilon`. Consequently the full graph induction costs at most `(CN^2)^{N+1}` times those biases, still `C exp(−c'N^2)`. This argument uses bounded common operators, not inverse query Grams, so the bias does not inherit `gamma^{-1}` amplification.

For `C^{1,1}` activations, the uniform original Euler carrier bound is obtained by taking the fixed finite program limit of mollified canonical Euler programs, including the convergence of their deterministic coefficients. Coordinate products are continuous with a linear envelope, so their values pass in `L^2`; Fatou transfers the common exponential-moment bound. Freezing the original coefficients before invoking a smoothed *canonical* program would require an extra argument; using the converging canonical coefficients avoids that issue. No quantitative mollification schedule is needed after the direct clipped Lipschitz maps are introduced.

## 3. Exponential constants do not hide an exponential recursion

Population regression coefficient sums are bounded by a fixed power of `CNB/gamma`; thus they are at most `exp(CN^3)`. There are only `N` chronological recursions. Each matrix node has the form `Y alpha+U beta+sigma g`, with deterministic coefficients and `sigma<=B`. Minkowski and the coordinate Lipschitz bounds therefore give

\[
\max_v\|v\|_4\le e^{CN^4}.
\]

Each required same-layer iid pairing or squared-tail statistic then has variance at most `exp(CN^4)/n`. With threshold `t=n^{-1/4}` and `O(N^2)` tests, Chebyshev costs at most `exp(CN^4)n^{-1/2}`. Removed Gaussian projections have conditional expected normalized squared norm at most `N/n`; Markov and a union bound give the same polynomial-width scale. Operator and fresh-root norm failures add `CN exp(−cn)`.

While the coupling error is below the Gram stopping margin, each actual empirical pairing differs from its population counterpart by at most

\[
t+C(B+1)e+e^2.
\]

Resolvent subtraction bounds inverse-Gram differences by `2 gamma^{-2}` times the Gram error. Applying this to `alpha`, then `h_perp`, then `beta`, and to the residual variance uses a fixed number of products and inverses, not a number growing with `N`. Their errors are bounded by a fixed power of `CNB/gamma` times `e+t`. Passing from variance to standard deviation divides by at most `epsilon`, because the population standard deviation is at least `epsilon`.

Thus every instruction has error recurrence

\[
e_{j+1}\le A(e_j+t),\quad A\le e^{CN^3},\qquad
e_N\le e^{CN^4}n^{-1/4}.
\]

For `log n>=C N^5` this is smaller than `gamma/[4CN(B+1)]`, so the stop cannot occur. The candidate's `exp(CN^5)` bound safely absorbs all these factors. There is no double exponential in this induction. Square-root conversion of a squared-tail measurement loses one additional factor `n^{-1/8}` only at the final norm measurement, not at every matrix call.

## 4. From sampled oracle nodes to a real parameter proxy

This is the central transfer check. Let the original population Euler nodes have residuals `r_j`, norms `rho_j`, step `h`, and activity bound `sum_j h rho_j<=C`. Write `zeta` for the uniform oracle-node and empirical contraction error after coupling and regularization. With the stated budget it can be taken polynomially small in `n`, plus `exp(−cN^2)`, even after harmless fixed polynomial factors.

Reconstruct finite proxy parameters `theta_p(t_j)` by the original Euler rank-one update formulas, using the sampled modified oracle vectors and the original deterministic residuals. Interpolate the updates affinely. The proxy starts at exactly the original finite initialization. Uniform RMS bounds for the sampled physical oracle nodes follow from their small coupling/bias relative to the original bounded population nodes. Hence proxy increments and operators remain in the fixed enlarged tube.

When the proxy hidden matrix acts on an oracle vector, its discrepancy from the prescribed oracle action is a weighted sum of empirical contraction errors plus the fresh initialized-query noise. Every memory coefficient has the activity weight `h rho_j`; its sum is bounded independently of the number of nodes and the horizon. Fixed-depth forward recomputation therefore costs `C zeta`.

Reverse recomputation uses the same contraction estimates and the gate inequality with comparison cutoff `R`. The omitted clipping at the much larger cutoff `N` is controlled by the soft-tail tests, hence by `C exp(−cN^2)+C zeta`. Descending the fixed number of layers adds, rather than multiplies, the comparison-cutoff factors. At a mesh node the resulting carrier and response discrepancies are at most

\[
C\{(1+R)\zeta+e^{-cR^2}\}.
\]

On an interpolation segment, `||theta_p(t)−theta_p(t_j)||<=C h rho_j`, so the same argument gives

\[
\|r_p(t)-r_j\|_m\le C(\zeta+h\rho_j),
\tag{A}
\]

\[
\text{carrier/response discrepancy from the oracle node}
\le C\{(1+R)(\zeta+h\rho_j)+e^{-cR^2}\}.
\tag{B}
\]

Here and below carrier norms are normalized Euclidean RMS norms. Equations (A)--(B) use only the finite node tails. They do not presume a Gaussian supremum over time.

Set `E_p=dot theta_p−F(theta_p)`. Expanding the difference between the frozen-node update and the actual proxy vector field first in its residual and then in its fields gives

\[
\|E_p(t)\|
\le C\zeta+C(1+R)h\rho_j
+C\rho_j\{(1+R)\zeta+e^{-cR^2}\}.
\tag{C}
\]

Without using activity damping, the same comparisons yield the candidate's `T exp(C(1+R)T)` estimate. All constants entering the integrand come from the fixed tube and node tails; an unspecified extra `C_T` is not needed. This verifies the original slow transfer.

## 5. The stronger activity-damped transfer

The refinement proposed by the supervisor is valid. By (A),

\[
\int_0^T\rho_p(t)\,dt\le C+CT\zeta,
\qquad
\epsilon_p:=\int_0^T\|E_p(t)\|\,dt
\le C\{(1+R)h+e^{-cR^2}+T(1+R)\zeta\}.
\tag{D}
\]

To bound a hard carrier tail of the proxy at cutoff `R`, dominate it by twice the positive-part tail at `R/2`, compare that 1-Lipschitz function against the neighboring oracle node, and use (B) with a constant multiple of `R`. Denoting the sum of proxy carrier tails by `H_p(R,t)`, this gives

\[
\int_0^T\rho_p(t)H_p(R,t)\,dt
\le C\{e^{-cR^2}+(1+R)(\zeta+h)\},
\tag{E}
\]

provided `T zeta<=1`, as holds for the schedules below. The factors `rho_j` are bounded and the total proxy activity is bounded; there is no factor `T` in the Gaussian-tail contribution.

Let `u=r_D−r_p` and `d(t)=d_n(theta_D(t),theta_p(t))`. The exact residual subtraction is

\[
\dot u=-2\Gamma_Du-2(\Gamma_D-\Gamma_p)r_p-J_pE_p.
\]

The actual dense Gram has its uniform positive gap. The proxy only needs bounded `J_p` and its physical tube; a proxy Gram gap is unnecessary. Gate subtraction against the proxy carriers gives

\[
\|\Gamma_D-\Gamma_p\|\le C\{(1+R)d+H_p\}.
\]

Integrating the damped norm inequality for `u` and then subtracting the parameter equations yields

\[
\int_0^t\|u\|_m\le C\left[(1+R)\int_0^t\rho_p d
+\int_0^t\rho_pH_p+\epsilon_p(t)\right],
\]

\[
d(t)\le C\epsilon_p(t)+C\int_0^t\|u\|_m
+C\int_0^t\rho_p\{(1+R)d+H_p\}.
\]

Gronwall with the finite measure `rho_p(t)dt` therefore gives

\[
\sup_{t\le T}d(t)
\le C e^{CR}\left[\epsilon_p+
\int_0^T\rho_pH_p\right]
\le C e^{CR}\{(1+R)h+e^{-cR^2}+T(1+R)\zeta\}.
\tag{F}
\]

For population Euler versus the exact population flow, repeat the same argument with `zeta=0`. The scalar prediction differential and rank-one parameter norms needed for this subtraction are exactly those constructed in the paper. Thus (F) controls both required reference comparisons.

Take

\[
K=\lfloor[\log(e^e+n)]^{1/128}\rfloor,\quad
N\asymp K^3,\quad
T=\frac2\kappa\log K,\quad h=T/K,\quad
R=B\sqrt{\log K},
\]

with `B` sufficiently large. The finite-program errors and their failure probability remain polynomially small in `n`, since `N^5=O((log n)^{15/128})=o(log n)`. Equation (F) is `K^{-1+o(1)}`. Late-time physical variation is at most `C K^{-2}`.

Comparing dense carriers to the oracle nodes adds at most another `1+R` factor, still `K^{-1+o(1)}`. Soft-tail tests at all integer cutoffs up to the program budget and monotonicity beyond it then give

\[
a_n\le K^{-1+o(1)}
\]

outside a polynomially small exceptional event. For any fixed beta in `(0,1)`, this implies `a_n<=C_beta K^{-beta}` eventually. The map `Phi` adds only `exp(O(sqrt(log K)))`, so `Phi(a_n)=K^{-1+o(1)}` as well. In particular the conservative shape `(log(e^e+n))^{-1/512}` is supported for both the tracking remainder and the population prediction error in probability. This exponent is a deliberately weak valid choice, not a sharp claim.

## 6. Whole-input norm and initialization probability

A normalized passive query uses `s_x=1+||x||/sqrt(d)`. Its first-layer root is a bounded-coefficient linear combination of the same `d` Gaussian roots. Its coordinate map `u -> phi(s_x u)/s_x` has a uniform Lipschitz constant and intercept. No derivative of that passive map enters backward training. Its deterministic memory coefficients are bounded by Cauchy--Schwarz against the training RMS bounds. The full single-probe estimate is therefore uniform in `x` after division by `s_x`.

Let `r_n` be any conservative rate justified above. For each fixed `x`, the all-time normalized error is at most `C r_n` outside a probability at most `C n^{-c}`, with constants independent of `x`. On the common physical good event it is bounded by a fixed constant even if that individual program estimate fails. Since `n^{-c}=o(r_n^2)`,

\[
\mathbb E\left[1_{\mathcal G_n}
\sup_{t\ge0}|f_{n,D}(t,x)-f_\infty(t,x)|^2\right]
\le C s_x^2r_n^2.
\]

The time supremum is measurable by continuity and a supremum over rational times. Tonelli followed by Markov gives `d_{n,mu}=O_P(r_n)` for every fixed law with finite second moment. This is a truncated mean-square estimate and a full in-probability conclusion; it does not control unconditional moments on `G_n^c`. Its confidence prefactor for the test integral depends on the requested confidence, as required for `O_P`.

For a bounded input domain, apply the single-query result at a deterministic `r_n` net and union-bound the failures. The predictors' common input Lipschitz bound extends the estimate off the net. In the improved logarithmic-power case the net has a fixed polynomial number of points in `K`, and this union factor is negligible against `n^{-c}`. Separate single-probe programs avoid exceeding the `N<=CK^3` instruction budget when the input dimension is large.

The common initial-good-event probability can also be made polynomially quantitative. Root/Frobenius bounds use Gaussian moments, and initialized operator norms have exponential tails. For the initial feature Gram, use the quantitative finite-program lemma at one sufficiently large *fixed* budget, choosing its proof-noise amplitude small enough that forward-only Lipschitz perturbation changes the original Gram by less than a fixed fraction of the limiting gap. The coupling and empirical pairing estimate then give the remaining gap event with probability at least `1−C n^{-c}`. This avoids assuming a quantitative modulus of continuity for an arbitrary singular initial covariance map.

## Final classification

- Adaptive reused-matrix coupling and growing regularization: checked, no substantive defect found.
- Claimed `exp(CN^5)` budget: checked; the actual displayed inductions fit within `exp(CN^4)` before margins and bookkeeping.
- Original-versus-clipped/noisy population bias: checked using the common operators and original uniform carrier tails.
- Finite oracle-to-real-proxy consistency: reconstructed above, including residual mismatch and interpolation terms.
- Original slow all-time transfer: checked.
- Activity-damped logarithmic-power upgrade: independently reconstructed in (A)--(F); supported.
- General finite-second-moment test law: checked in probability, with exceptional-event moments explicitly excluded.
- Sharp nonlinear `n^{-1/2}` upper bound, polynomial width rate, or efficient epsilon-width budget: not obtained by this argument.

## Final frozen-chain verification

After the corrections, the complete final `PROGRAM_RATE_ROUTE.md`, complete final `PROGRAM_RATE_ADDENDUM.md` including Section 9, and complete final `DAMPED_TRANSFER.md` were reread. The original `TRANSFER_DERIVATION.md` was already read completely and remains the superseded conservative transfer. The accepted hashes are:

| File | SHA-256 |
|---|---|
| `PROGRAM_RATE_ROUTE.md` | `d6c7683057b03f710f73be4922a4411ad514bb3e508d3f17678c411a58a0547a` |
| `PROGRAM_RATE_ADDENDUM.md` | `a11c6e70204a0202da18075afc6565f6e46205de08865cdbcc5c5c38fccd43b7` |
| `DAMPED_TRANSFER.md` | `27ee61e6aa1367329e0baf3e1ae41993ead53f323ba98af2942a1f034bd3a96c` |
| `TRANSFER_DERIVATION.md` | `c76e5c0d00da6867f835c8d83135fa839b9926ee7c75a7f371f32c03e4b0672d` |

The addendum's exact action differences (A11), (A13), gate decomposition (A15), current-state estimates (A19)--(A23), activity-weighted defect (A27)--(A29), weighted proxy tails (A31)--(A32), damped subtraction (A33)--(A35), and deterministic population counterpart (A36) agree with the independent reconstruction above. Its fixed-tolerance initialization argument in (A2) additionally proves the stronger elementary `P(G_n^c)<=C/n+Ce^{-cn}` bound: continuity is used only to select fixed tolerances, so it needs no quantitative covariance modulus.

The final `DAMPED_TRANSFER.md` now correctly separates forward/residual consistency `C eta` from backward consistency `C[(1+R)eta+exp(-cR^2)]`. Its defect bound is conservatively larger than the sharper addendum bound, and is valid. The proof consistently retains original population residuals in the source updates; proxy residuals enter only the true perturbed-flow identity. Thus no unproved fitting property of the proxy is assumed.

The schedule in the final damped transfer gives a per-query discrepancy `C K^{-3/4}`, carrier excess `C K^{-2/3}`, and tracking remainder `C K^{-1/2}`, for `K=floor(log(e^e+n)^{1/128})`. Tonelli and Markov applied to the truncated per-query mean square give both prediction-error threshold and exceptional probability of order `K^{-1/2}`. Therefore its `1/256` logarithmic exponent is supported; weakening to `1/512` is safe and is also supported directly by the addendum's more conservative exponent bookkeeping.

In particular, under the paper's unchanged hypotheses, write

\[
r_n=[\log(e^e+n)]^{-1/512}.
\]

For sufficiently large width there are common initialization events of probability at least `1-C_mu r_n` on which, simultaneously for every closure order `q>=1`,

\[
\sup_{t\ge0}d_n(\widehat\theta_{n,q}(t),\theta_n(t))
\le C\omega(q)+Cr_n,
\]

\[
\mathcal E_\mu(\widehat f_{n,q},f_\infty)
\le C_\mu\omega(q)+C_\mu r_n.
\]

The corresponding bounded-input-set supremum has the same rate after a finite-net union bound. Constants and the fixed width threshold may depend on the fixed problem and test law/domain, but not on `n,q,t`. These are high-probability statements; unconditional population-prediction RMS outside the original physical good event is not claimed.

Final internal verdict: the entire final quantitative proof chain listed above has been checked within this scoped audit, with no unresolved substantive defect found. The logarithmic width rate is internally supported. This verdict is not promotion approval or a substitute for the repository's fresh independent promotion reviews.

## Final result-statement consistency check

The complete `RESULT.md` was read against the accepted proof chain above. Its checked SHA-256 is `8050f8ff34f00e1263e422d8b8a51bba85be4ae216cec5bd66299b7b2454c267`.

No actual mismatch was found. In particular:

- The parameter estimate and all-order existence/fitting/convergence hold together outside a polynomially small exceptional event, because the quantitative event concerns the dense reference and the original common physical initialization event.
- The conservative width term `r_n=log(e^e+n)^{-1/512}` is weaker than the accepted carrier and parameter bounds. For the whole-input prediction statement, the truncated second moment of order `K_n^{-1}` and the threshold `K_n^{-1/4}` give exceptional probability of order `K_n^{-1/2}`, which is smaller than the stated `C_mu r_n`.
- The event is common to all closure orders; the prediction event may depend on the fixed test law, as stated. Constants and the fixed width threshold are independent of width, order, and physical time.
- Finite second moment is sufficient for the test law because the single-probe estimate is uniform after normalization by `1+||x||/sqrt(d)`. The time supremum is already inside that estimate before Tonelli and Markov are applied.
- The bounded-domain polynomial exceptional probability is supported by separate single-probe programs and a finite-net union bound.
- The statement retains the paper's hypotheses and explicitly excludes unconditional error-moment control on the exceptional initialization event, sharp polynomial-width claims, and promotion status.

The final result statement is consistent with the frozen internally checked proofs. No further correction was requested in this bounded check.
