# Independent audit of the fixed-history width rate

2026-10-07. Reviewer: the kinetic-route agent. Scope: the complete `FIXED_HISTORY_RATE.md`, read both before and after its announced notation-only correction, together with the previously read finite-history and exact Gaussian-posterior proofs allowed by the assignment. No author summary, new scientific source, literature, experiment, other study, or Git material was consulted. Required mathematical skills remain current. The author's file was not edited.

Reviewed final SHA256: `585e877e5a7d3853847bb0859f44b79a938da9232d6e63cf77660aa5044ca2e1`. The pre-correction frozen hash was `9dbafab203759e85a42f442802f3e9a650d6b57f5ea456e5d3f92d0fd41995e8`. I reread the final file completely and independently verified that removing its new notation-correction paragraph and reversing the history-gap symbol replacement reproduces the exact pre-correction hash. The edit changes no mathematical content. In this report, \(\lambda_{\rm hist}\) means the final source's retained-history gap.

## Verdict

**PASS for every fixed program satisfying the stated local Lipschitz qualification on scalar coefficient maps.** The proof establishes the high-probability bound

\[
C_r n^{-1/2}[\log(en)]^{2Q+2}
\]

for same-population pairings and the stated scalar outputs, as well as an RMS coupling to iid rows of the deterministic scalar law, with failure probability at most \(C_rn^{-r}\). The constants and the width threshold may depend on the fixed program, its retained limiting Gram gaps and positive innovation variances, and \(r\).

I found no missing independence assumption, square-root loss, original-field moment hypothesis, or circular localization argument. Zero limiting innovations are handled by exact identities in the coupled reference rows, rather than by taking a square root of an empirical variance error. The retained positive innovations are handled by local Lipschitz continuity of the square root at their fixed positive limiting values.

This PASS is not uniform over program length, labels, ranks, or retained gaps. It supplies no continuous-time or all-time limit, no finite autonomous memory bound, and no reconstruction below the realized \(n^{-1/2}\) fluctuation scale. The author states these limitations correctly.

## 1. Scope, scalar-map regularity, and limiting-law construction

The qualitative predecessor permits continuous scalar coefficient maps. The rate theorem explicitly strengthens this to maps locally Lipschitz on neighborhoods of their limiting arguments. That strengthening is necessary: continuity by itself can convert a root-width input error into a larger error, for example through a square-root map at zero. The stated theorem does not make that mistake.

The actual canonical finite Euler program has polynomial shared scalar operations, so it satisfies the local Lipschitz condition at every finite limiting argument. This is a regularity condition on the program operations, not an added label-smallness or fitting condition. The rate theorem also requires that the finite-width program be defined; this resolves the off-neighborhood domain convention raised in the earlier unclipped audit.

The deterministic scalar law and retention decisions are well defined in the same sequential order as the qualitative proof. Every retained query adds a positive \(L^2\) innovation, so each nonempty retained Gram is positive definite. For a fixed finite instruction list, the minimum \(\lambda_{\rm hist}\) over its finitely many such Grams and the minimum positive innovation variance \(\nu\) are positive. Taking constants that depend on them is legitimate for a pointwise fixed-program theorem. It would not establish a uniform result for a family approaching a rank change, and no such result is claimed.

Empty histories and a program with no retained queries can use the stated default minima equal to one. Singular seed covariance is represented by a fixed linear image of independent standard Gaussian roots and requires no inverse.

## 2. Linear Gaussian envelope and iid-pair concentration

Every limiting row field is a deterministic function of the finite vector of its population's Gaussian roots and retained-query innovations. Its scalar coefficients are deterministic. The envelope

\[
|V_j(\zeta)|\le A_j(1+\|\zeta\|_1)
\]

is valid by induction. Globally Lipschitz coordinate maps have linear growth in their arguments. A bounded gate multiplies its unbounded field by at most a fixed constant. A finite linear combination adds envelope constants. A retained query is a finite linear combination plus one scaled Gaussian coordinate. The derivative of a field with respect to \(\zeta\) need not be bounded; the proof uses a value envelope, which these operations do preserve.

Thus limiting fields have all finite moments and pair products have a quadratic Gaussian envelope. This assertion concerns the deterministic scalar law and its iid reference samples. It is not an unjustified high-moment assertion about the original interacting network.

Set

\[
\lambda_n=\sqrt{\log(en)},\qquad
\varepsilon_n=n^{-1/2}\lambda_n^3.
\]

For each prescribed failure exponent, a Gaussian union bound over the fixed number of primitive columns and their \(n\) coordinates bounds their joint maximum by \(C_r\lambda_n\) except with probability \(C_rn^{-r}\). The linear envelope gives the same order for all reference fields.

Truncating a row product when any of that row's primitive Gaussian coordinates exceeds the threshold preserves independence across rows. The truncated product is bounded by \(C_r\lambda_n^2\). For a centered variable bounded by \(M\), the source's symmetrization bound is correct:

\[
\mathbb E e^{tX}
\le\mathbb E e^{t(X-X')}
=\mathbb E\cosh(t(X-X'))
\le e^{2t^2M^2}.
\]

The first inequality follows from Jensen applied to the independent centered copy \(X'\); the last follows from \(|X-X'|\le2M\). For independent rows, exponential Markov inequality then gives average error \(C_rM\sqrt{\log(en)/n}\) with the requested polynomial failure probability. With \(M=C_r\lambda_n^2\), this is exactly \(C_r\varepsilon_n\).

Centering the bounded truncated variable changes its bound by at most a factor of two. The population truncation bias is also controlled: Cauchy–Schwarz bounds it by the square root of a Gaussian-tail probability times the fixed second moment of the product, equivalently a fourth-order envelope moment of the fields. Increasing the Gaussian threshold makes this bias smaller than the required rate. This is a genuine population tail estimate; no inference from sample localization alone is made.

A finite union covers all same-population field pairs. Their empirical second moments are bounded by fixed constants on this event for sufficiently large widths, because they differ from fixed finite expectations by \(C_r\varepsilon_n\to0\). It is this sharper second-moment fact, not the coordinate maximum alone, that is used later for pairing comparisons.

## 3. Coupling iid reference rows to an exact finite-width simulator

The coupling construction is valid. Generate the simulator sequentially through its exact conditional Gaussian response kernels, using fresh independent standard-normal columns. Its retained constraints remain compatible by the exact projected-noise formula. Complete each initialized matrix from its Gaussian posterior after the last retained query. The resulting joint matrix/seed marginal equals the original independent Gaussian model, because the response kernels and final posterior are precisely its sequential disintegration.

Unused components of a sampled innovation column do not become extra matrix observations. The posterior completion is conditioned on the simulator transcript, not on an enlarged transcript containing arbitrary unobserved innovation components. This interpretation is consistent with the construction in the source and is sufficient for the claimed Gaussian marginal.

Use the same primitive columns as inputs to the deterministic scalar-law recipes. Reference coordinates within a population are then independent copies of the scalar row law: each depends only on its own Gaussian root/innovation row and fixed coefficients. Simulator coordinates are not independent, because their regression coefficients and projections are empirical. The proof distinguishes those objects correctly.

After completing the matrices, run the original program on the same matrices and roots. Its additional queries are not inserted into the simulator's conditioning history. Dependence between the matrix-completion event and the reference good event is harmless: all later probability bounds are intersected using union bounds, not unjustified independence.

## 4. Retained-query coefficients, innovation scales, and projection tails

All retained-query regression coefficients are locally Lipschitz functions of finitely many existing empirical pairings, on a neighborhood with retained Grams bounded below by \(\lambda_{\rm hist}/2\). The explicit inverse estimates are correct. In particular,

\[
\Gamma_n^{-1}-\Gamma^{-1}
=\Gamma_n^{-1}(\Gamma-\Gamma_n)\Gamma^{-1}
\]

gives the displayed bound \(2\lambda_{\rm hist}^{-2}\|\Gamma_n-\Gamma\|\). Splitting the difference in \(\Gamma_n^{-1}b_n\) then gives the stated right-hand-side-vector estimate. The more complicated reverse-response coefficient is a composition of such inverses and finitely many pairings, so it is locally Lipschitz as claimed.

At a retained query, the limiting innovation variance satisfies \(\sigma^2\ge\nu>0\). Therefore

\[
|\sigma_n-\sigma|
=\frac{|\sigma_n^2-\sigma^2|}{\sigma_n+\sigma}
\le\nu^{-1/2}|\sigma_n^2-\sigma^2|.
\]

No positive lower bound on the finite-width \(\sigma_n\) is needed for this inequality; its denominator is at least the fixed positive \(\sigma\). Zero limiting innovations are handled elsewhere by omission.

For the projection coefficient

\[
\beta_n=(D_n^\top D_n)^{-1}D_n^\top\xi,
\]

conditional covariance is exactly \((D_n^\top D_n)^{-1}\). When the normalized Gram is at least \(\lambda_{\rm hist}/2\), it is bounded by \(2I/(n\lambda_{\rm hist})\). Its fixed finite number of Gaussian coordinates therefore obeys

\[
\|\beta_n\|\le C_rn^{-1/2}\lambda_n
\]

with the requested conditional failure probability. The proof correctly applies this estimate only before the first required Gram-neighborhood failure, a stopping condition determined by the past. It does not first condition on the global reference good event, which could involve future innovations and destroy that conditional argument.

There are finitely many calls. A union bound controls all pre-failure projection events, and the deterministic error estimates then prevent the Gram failure on the intersection with the reference event for large enough widths. This is a valid bootstrap, not a circular probability assumption.

## 5. Entrywise simulator error and zero innovations

Let the previous maximum row/scalar error be \(E\le1\). For a simulator pairing, expansion against its reference factors gives

\[
\left|\langle\widehat v,\widehat w\rangle_n-\mathbb E[VW]\right|
\le C_r\lambda_n E+E^2+C_r\varepsilon_n
\le C_r\lambda_n E+C_r\varepsilon_n.
\]

The last step uses \(E\le1\) and \(\lambda_n\ge1\). This justifies the source's pairing estimate without invoking moments of original fields.

At a retained query, coefficient errors are \(O(\lambda_n E+\varepsilon_n)\). Multiplication by reference coordinates or the fresh innovation costs at most another factor \(\lambda_n\). Existing field errors are multiplied by bounded coefficients on the chosen neighborhoods. The projected-noise term costs at most

\[
C_r\max_i\|D_{n,i}\|\,\|\beta_n\|
\le C_rn^{-1/2}\lambda_n^2,
\]

including the bounded conditional noise scale. These terms fit the deliberately loose recurrence

\[
E_j\le K_j\lambda_n^2(E_{j-1}+\varepsilon_n).
\]

Gated products cost one reference-maximum factor \(\lambda_n\); scalar-weighted linear combinations cost at most that factor for a coefficient error; other operations satisfy smaller bounds. Thus a single factor \(\lambda_n^2\) per prescribed instruction is safe even though a query's regression computation contains several fixed scalar algebraic operations.

The recursive constants \(A_j=K_j(A_{j-1}+1)\) yield

\[
E_j\le A_j\varepsilon_n\lambda_n^{2j}.
\]

For each fixed program this tends to zero, so choosing a sufficiently large width threshold keeps all relevant field and coefficient arguments in the neighborhoods used to derive the recurrence.

For an omitted query, \(\mathbb E(u-H^\top a)^2=0\) means that \(u-H^\top a=0\) almost surely as a function of its scalar-law Gaussian row. Every coupled reference row satisfies that identity; a finite, or countable across widths, union of null events remains null. Therefore

\[
\|\widehat u_n-\widehat H_na\|_\infty
\le(1+\|a\|_1)E_{j-1}.
\]

This is stronger than a mere empirical-variance comparison and is exactly why the proof avoids a fourth-root-width error at a zero innovation. It works for repeated queries, initially zero backward fields, zero labels, and an empty history with an identically zero query.

The simulator maximum is \(O(\lambda_n)\). Its normalized Euclidean norms are bounded by fixed constants, using reference second moments and the vanishing entrywise error; those are distinct bounds and the proof uses each in the correct place.

## 6. Original/simulator comparison and accumulated exponent

The completed matrices have the original Gaussian marginal, so the fixed operator-norm event has exponentially small failure probability. This statement is unconditional; no independence from the other good events is needed.

On that event, the original/simulator gated-product error satisfies

\[
\|u_na(v_n)-\widehat u_na(\widehat v_n)\|_{2,n}
\le\|a\|_\infty\|u_n-\widehat u_n\|_{2,n}
+\operatorname{Lip}(a)\|\widehat u_n\|_\infty
\|v_n-\widehat v_n\|_{2,n}.
\]

It costs at most \(C_r\lambda_n\Delta_{j-1}\). Only the simulator maximum appears. Original higher moments or coordinate maxima are not assumed.

While \(\Delta_{j-1}\le1\), original RMS norms are bounded by the simulator's norms plus one. Pairing differences are therefore \(O(\Delta_{j-1})\) by Cauchy–Schwarz, and the locally Lipschitz scalar maps preserve this rate inside their neighborhoods. Finite scalar-weighted linear combinations also use these RMS bounds. Retained matrix calls cost only a fixed operator-norm factor.

At an omitted call, the exact retained identity \(G\widehat H_n=\widehat F_n\) gives the two error terms displayed in the source. Their RMS norms are bounded by \(R\Delta_{j-1}+C_rE_{j-1}\), using the reference-row zero-innovation identity. Thus

\[
\Delta_j\le K'_j\lambda_n(\Delta_{j-1}+E_Q)
\]

is safe. Its recursion yields \(\Delta_Q\le B_Q E_Q\lambda_n^Q\). Together with
\(E_Q\le A_Q n^{-1/2}\lambda_n^{2Q+3}\), this gives

\[
\Delta_Q+E_Q\le C_rn^{-1/2}\lambda_n^{3Q+3}.
\]

The source's log exponent is conservative:

\[
\lambda_n^{3Q+3}
=[\log(en)]^{(3Q+3)/2}
\le[\log(en)]^{2Q+2},\qquad Q\ge1.
\]

Choosing a sufficiently large \(n_r\) makes both recurrences and all induced pairing errors smaller than the specified local neighborhood radii. The same deterministic first-exit reasoning closes the original scalar-map bootstrap. Its constants can be large, but they are fixed with the program and do not conceal width dependence.

## 7. Pairings, output probability, and final scope

Each final pairing is split into original/simulator, simulator/reference, and iid-reference/population differences. The first two use the fixed RMS norm bounds and contribute \(C_r(\Delta_Q+E_Q)\); the last is \(C_r\varepsilon_n\). Shared scalar register differences have already been included in the recurrences. The same bounds give the advertised original/reference RMS coupling.

The Gaussian-maximum, truncated-iid-pair, and stopped conditional-projection failures can each be assigned the prescribed polynomial tail exponent with enlarged program constants. Their finite union has probability \(C_rn^{-r}\). The matrix operator-norm failure is exponentially smaller and can be absorbed for all sufficiently large widths. No union over a width-growing program or parameter family appears.

The proof therefore establishes the stated rate for actual fixed finite Euler outputs and sampled feature/backward pairings, since the Euler memory coefficients are polynomial scalar maps and its activation derivative gates are bounded and globally Lipschitz under the stated strip hypothesis. The exact trained-matrix history identities used for membership were checked in the prior unclipped audit.

The fixed-program coupling is an approximation at root-width scale up to logarithmic factors. It neither reproduces the realized leading fluctuation with error \(o_{\mathbb P}(n^{-1/2})\) nor proves a central limit theorem. If step count, depth, sample count, local scalar sensitivities, or retained gaps vary with width, the present constants and bootstrap thresholds supply no uniform conclusion. No additional source-label qualification is being asserted.

I recommend accepting this candidate as internally checked at its explicit fixed-program scope. The history-gap symbol rename is complete. I found no correction required for the mathematical rate argument.
