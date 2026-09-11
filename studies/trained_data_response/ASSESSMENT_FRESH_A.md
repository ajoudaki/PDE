# Fresh isolated scientific assessment of P1

**Overall verdict: ACCEPT for the exact proposed scope.**

The supplied proof establishes a bounded data-to-forcing operator and its strong linear evolution, identification of actual finite-GF right derivatives on every separately fixed physical horizon with uniform whole-circle prediction observations, and a separate population homogeneous-propagator bound uniform in time. I found no surviving mathematical gap in those conclusions after reconstructing the dependencies and the finite cavity and tangent comparisons. This verdict does not extend to finite contamination, nonlinear perturbed-law population flows, law-dependent fitted endpoints, raw-GD derivatives, useful numerical response constants, or growing-horizon width limits.

The decisive point is that the packet supplies two bridges which a formal linearization would lack: an actual finite-GF column-deletion estimate yielding weighted source uniform integrability, and a same-width integrated tangent-defect estimate with width taken before mesh removal. Neither bridge is replaced by a population source formula or by bounded RMS norms alone.

## 1. Reviewer identity, isolation, and frozen-input coverage

Reviewer process: `/root/milestone1_fresh_audit`, launched as a fresh isolated independent scientific assessor on 2026-09-11. This process is distinct from the author/assembler and selector identities recorded in the manifest. No author discussion, live author drafts, study README, prior report, prior verdict, history, other study, or other agent's findings were consulted. No delegation, Git command, Git write, external lookup, training run, or parameter sweep was performed. The scientific reading was confined to the seven authorized P1 files below. Links to contextual literature and other repository chapters were not followed.

The complete required `solve-math-rigorously` and `investigate-conjectures` skills were read, together with `research-contract.md`, `adversarial-audit.md`, and, for the expressly authorized deterministic computation, `decisive-experiments.md`. The latter was applied proportionately as a precommitted algebra-check contract; the checks do not constitute training experiments.

Every line of the proposed section, dependency packet, ancillary packet, assignment, manifest, and both programs was read. Both complete reading guides were read: the old guide in the dependency packet and the revised guide in the ancillary packet. The dependency packet contains complete proof units for all mathematical inputs invoked here, including finite energy/existence, III.F, A.1–A.4, B.1, the full-row transport comparison and canonical action construction, and C.4.5.1–2. Reading those units also covered their ancillary GD, activity, and certificate arguments; these were not silently imported as a GF derivative theorem.

| Frozen input | Complete line coverage | SHA-256, before and after |
|---|---:|---|
| `P1_SECTION.md` | 1–2062 | `33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38` |
| `P1_DEPENDENCIES.md` | 1–3238 | `ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79` |
| `P1_ANCILLARY.md` | 1–300 | `649f0ee17af3c0a2f4b995e971929f8e7a62d9d420614baee418af62d6cdd420` |
| `P1_CHECK_IDENTITIES.py` | 1–197 | `b0bbbde5f1f024dbb46975b2092d3aa2a79cabd0375f4520c05489f934d3902f` |
| `P1_REFERENCE_CERTIFICATE.py` | 1–56 | `112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e` |
| `P1_ASSIGNMENT.md` | 1–47 | `a9f61d5f27d84e8a9de85d7ba5faaf39c4adb19e7829c27c285a455916488199` |
| `P1_MANIFEST.json` | 1–83 | `f9f3ac7dd834429f2afd1b2d819e20cf04da37446311405943332300ca4fa53d` |

The first six entries match the manifest exactly, including line counts. The manifest's own hash is independently recorded; it is not self-certified. Other build/integration entries in the manifest were treated solely as provenance and were not opened. A tool output truncation inside dependency lines 757–779 was repaired by rereading 750–783. A later combined output elided part of ancillary lines 172–173; rereading 165–177 repaired it. No truncated scientific passage was left unread.

All new scratch is in `data/generated/trained_data_response/assessment_fresh_a_20260911/`. It contains before/after hash records, the precommitted check contract, both prescribed command/output records, the prescribed identity result, and the independent check source/results. This report is the only write outside that assigned scratch directory. No frozen input was edited.

## 2. Research contract and component decisions

The target is two equal-width tanh hidden layers, no biases, first-row input normalization `u=x/sqrt(2)`, output `c^T h2/n`, stored Gaussian variances `(1,1/n,1/n²)`, and stored mobilities `(n,1,n)` for the unhalved mean-square loss. Both directions of the same initialized matrix remain. The reference law has exactly the two orthogonal opposite-label atoms; only the perturbing law is arbitrary on the compact circle/label space. The law is deterministic and fixed independently of initialization. Nonatomic finite loss integrals are exact integrals.

The observable is the right law derivative at each finite width, with common initialization for every contamination parameter. Its population identification uses clock-row L2, learned-middle HS, and readout L2 approximations, and scalar predictions uniform on `[0,T]` times the circle. There is no subtraction of states on different carriers. Complexity of a proof proxy may depend on the fixed horizon, desired accuracy, cutoff, and quadrature; every program is fixed before width tends to infinity.

| Component | Decision | Main grounds |
|---|---|---|
| Exact finite right differentiation and equation T6 | Accepted | Smooth finite integrated loss, energy continuation, finite parameter difference quotients, exact gate cancellation in active clock rows |
| Canonical reference and fitted endpoint | Accepted from the reconstructed supplied proofs | Common generated actions/actual adjoints, transformed existence and mesh estimates, symmetry, `b_s≥m≥1/10`, finite feature endpoint |
| Actual finite passive weighted source estimates | Accepted | Column deletion with conditional independence on `E_n^i`, full residual comparison, Gaussian query-value chaining, polynomial clock-weight envelope |
| Admissible forcing and strong evolution | Accepted | Weighted L2 integrability, compact-parameter continuity, Bochner integration, bounded strongly continuous coefficients |
| Actual finite-GF derivative capture | Accepted | Fixed programs with source clips and law quadrature; strong multiplier consistency; integrated same-width tangent defect and ordered limits |
| Uniform whole-circle output capture | Accepted | Reference weighted product control, observation-field H1 bound, time equicontinuity, finite nets |
| Uniform population homogeneous propagation | Accepted | `E=S*D`, injective metric/kernel compatibility, finite-dimensional pseudoinverse formula, integrable actual coefficient perturbation |
| Revised guide/navigation statements | Accepted | They preserve GF, fixed-horizon width, population propagation, and infinitesimal/nonlinear distinctions |

The acceptance is scientific, not an integration or promotion approval. The manifest itself reserves approval for established-file edits.

## 3. Finite model, metric, and derivative reconstruction

For a datum `(u,y)`, direct output differentiation gives the raw metric gradient blocks

\[
 (u_a\phi'(w\cdot u)Q(u))_a,\qquad
 \delta(u)\otimes H^1(u),\qquad H^2(u).
\]

At finite width the middle block is `delta h^T/n`, while row and readout pairings divide by `n`. Thus the metric is precisely row Frobenius squared divided by `n`, ordinary middle Frobenius squared, and readout Euclidean squared divided by `n`. Multiplication by `-2r` and integration against the law give the stated mobilities and unhalved-loss factor. At the reference, `p_a=1/2` cancels this two; the clock row velocity is `X'_a=-r_a Q_a`.

The scalar primitive satisfies `F'=cosh²=1/phi'`, is strictly increasing onto the real line, and gives `w_a=j(X_a,g_a)`. Therefore `delta w_a=phi'(w_a) xi_a`. At an active input, `delta H_a^1=phi'(w_a)^2 xi_a`; the second gate is essential. Differentiating the transformed active velocity gives exactly

\[
 -2p_a\{\ell_a[v]Q_a+r_a(B^*\delta_a+A^*\dot\delta_a[v])\}.
\]

There is no extra own first-gate curvature in that row. Differentiating the raw equation and then differentiating the clock conversion in time cancels that term. The middle and readout product rules give P10. For direct law variation, cancellation is unavailable at a general `u`, and the source retains `u_a phi'(w·u)/phi'(w_a)`. This verifies the inverse gate, reference subtraction, sign, factor two, and both action orientations in T5–T6. The output variation T7 is obtained by the same chain rule and uses the normalized finite scalar pairings.

At fixed width and fixed initialized arrays, every derivative of the integrated finite loss is locally bounded uniformly over the compact data space. The loss is therefore smooth even for a nonatomic law. Energy bounds the displacement on each finite horizon, uniformly for the finite-dimensional family `epsilon∈[0,1]`; its metric is equivalent to Euclidean norm at this fixed width. Local ODE existence consequently continues across each finite proposed endpoint. Subtracting the finite integral equations first gives an `O_{n,T}(epsilon)` path difference. Dividing by epsilon and applying the mean-value formula gives coefficients tending uniformly to the reference Jacobian; the second difference inequality identifies the limiting linear equation uniformly in time. This proves the actual right derivative without any population differentiability assumption. Width dependence of those finite differentiability constants is harmless because they are not used to exchange limits.

The initial tangent is exactly zero, including the finite random readout tangent. A mass-zero signed direction need not be a two-sided tangent to probability measures. The later bounded linear extension through the displayed signed integral is mathematically distinct and legitimate.

## 4. Reconstructed reference and Gaussian-program dependencies

The supplied finite energy identity has the stated metric and no residual hidden inside `delta`. It gives `loss(t)≤loss(0)` and displacement at most `sqrt(T loss(0))`; finite-dimensional continuation does not require a bounded activation, although bounded tanh supplies the convenient uniform state bounds used here.

III.F establishes fixed-program convergence by successively conditioning the same Gaussian matrix on both forward and reverse constraints. The minimum-Frobenius conditional mean obeys both constraints; the residual has the projected independent Gaussian law. Adaptivity is handled by conditioning on the existing transcript before the next query, not by assuming query/matrix independence. The removed finite-rank Gaussian projection has normalized expected square `rank/n`, which vanishes for a fixed program. Conditional scalar tests and second-moment calculations identify joint empirical W2 laws.

For singular query Grams, adding a separate fresh input root at every call makes the fixed-noise limiting Grams positive definite. A same-array bound removes that noise after width; covariance square roots and bounded source derivatives identify the zero-noise scalar recursion. There is no claimed continuity of empirical pseudoinverses at rank loss. The forward and reverse Gaussian *source groups* can be independent because the answers include the response corrections. The finite transpose pairing identity then proves actual Hilbert adjunction on the generated dense span and its completion. The sharp action norm two follows from the contained Gaussian comparison/Poincare proof, not from changing finite initialization.

A.1 extends values to continuous maps of at most linear growth by fixed smooth approximations, W2 tails, and bounded action errors. Its approximation order is sufficient even without uniform cutoff Lipschitz constants. The tanh transform `j(X,g)` satisfies that growth condition but is not assigned a globally bounded root derivative. Same-root clock Lipschitz estimates supply the separate nonlinear Euler/flow comparison. Replacing middle operator distance by HS distance is valid because each rank-difference inequality holds in HS and HS bounds action norm; this gives the stronger increment topology used in C.4.6.

The C.4.5 reference feature flow is `c_s=h`, `(w,K)_s=J*c` with `h=(H_1²-H_2²)/2`. The strong curve chain rule gives

\[
 b_s=\|h\|_2^2+\|J^*c\|^2=\|\theta_s\|_{\rm raw}^2.
\]

For `g(s)=||c(s)||`, Cauchy–Schwarz in the displayed formula for `g_ss` makes `g` convex on its positive interval. Its initial right slope is `sqrt(m)>0`, so it never returns to zero, `g_s≥sqrt(m)`, and `b_s≥m`. The exact rational certificate establishes `m=v/2>1/10`. Hence the first `b=1` feature time is finite and at most ten. Bounded `b_s` near that endpoint makes the reciprocal physical-clock integral diverge. Thus `ds/dt=2(1-b)` covers every finite physical time and gives `e(t)≤exp(-t/5)`.

Integrating the raw speed and using Cauchy–Schwarz gives the endpoint bound `d_ref≤e/sqrt(m)≤sqrt(10)e`. The readout sup bound is independently supplied by its bounded feature velocity. These facts justify P2–P3 at the actual canonical endpoint.

The active endpoint fourth moment used in P5 is also supplied, rather than inferred from L2 convergence. I checked C.4.5.2's source-slot derivative convention, clipped-root justification, finite fresh-root pulses, response-coefficient bounds, and passage of the Gaussian-plus-bounded remainder to the common flow. In particular: fresh root injection is first analyzed at fixed mesh and fixed nonzero amplitude; its Gaussian integration-by-parts pairing is bounded using finite same-array sensitivity; only then is the amplitude removed. The response coefficients are held fixed for named-source differentiation. Their mesh sums yield `B_Q=225400 exp(2880)+180`. A canonical L2 limit of the bounded remainders remains bounded, and the limiting source variance is at most ten. Thus `||Q_{a,infty}||4≤3^(1/4)sqrt(10)+B_Q` is valid. This result alone would not establish weighted passive finite moments; the new cavity proof is separately necessary and present.

The dependency packet also supplies the quantitative hidden-activity calculation and its initial two-orientation reuse formulas. The exact rational program confirms the five Gaussian bounds used there. Those activity claims are not needed to infer a derivative limit or a benefit in risk, and neither inference is made in the proposal.

## 5. Actual finite-GF cavity and weighted source audit

This is the central finite probabilistic estimate (section lines 745–1518). On `E_n`, initial loss is at most four, so the full reference has the deterministic bounds `B=10+2sqrt(T)`, `C=1+2sqrt(T)`, `W=2+2sqrt(T)`, and readout supremum `H=1+4T`. The two residual magnitudes sum to at most four and each is less than three. Differentiating passive fields therefore gives the displayed normalized-L2 time and input Lipschitz constants using only the row RMS, matrix norm, and readout supremum. It does not require a pointwise input-derivative tail estimate.

Delete only initialized column `a_i=A0 e_i`. The comparison flow retains the whole first row, learned increment, readout, labels, and its own changing residuals. Its initialized matrix is the original matrix right-multiplied by an orthogonal projection, so `E_n⊂E_n^i`. The event `E_n^i` and the full cavity flow are measurable with respect to all initialized variables except `a_i`. Conditional on those variables, `a_i` still has independent `N(0,1/n)` entries. Conditioning on `E_n` directly instead would not permit this argument; the proof does not do so.

For the full-minus-cavity comparison, I reconstructed the two exact subtractions

\[
 \Delta Z^2=A\Delta H^1+\Delta K\,\widetilde H^1+a_i\widetilde H_i^1,
\]
\[
 \Delta Q=A^T\Delta\delta+\Delta K^T\widetilde\delta
                   +e_i a_i^T\widetilde\delta.
\]

The full matrix in the first reverse error is necessary: replacing it by the cavity matrix without accounting for the remaining term would leave an adapted-column error. These identities give S22. The residual comparison uses `Delta f=<Delta c,H2>+<c_tilde,Delta H2>`. Subtracting all three velocities gives S23, including those residual changes. With `D0=1+B+C+H+3`, the displayed intermediate coefficient bounds imply at most `81 D0^4` on the distance and `36 D0^3` on the forward column error, so `L=100 D0^4` is safe. The derivative inequality for the sum of component norms holds almost everywhere, including times at which a norm is zero. Integration yields S25.

No small initialized operator difference is asserted. The forward error instead has RMS `||a_i||/sqrt(n)`, and the reverse direct error has RMS `|a_i^T delta_tilde|/sqrt(n)`. The learned transpose contribution is bounded coordinatewise by its exact rank-integral formula, using bounded first features. Consequently the actual query envelope satisfies

\[
 N_{n,i}\le A_T Z_i^\#+B_T\quad\text{on }E_n.
\]

The comparison error converts correctly: `||a_i|| sqrt(n) ||delta-delta_tilde||RMS` is controlled by S25, and `||a_i||≤10` on `E_n`. This gives exactly the `80` and `400` coefficients in S28. It is an actual reached-flow bound, not an assertion for arbitrary adapted queries.

Conditional cavity probes form a continuous finite Gaussian process. Its conditional covariance is `delta_tilde(t,u)^T delta_tilde(s,v)/n`. S12, S15, S16 bound both variance and the canonical increment distance. The supplied dyadic-square chaining proof needs no independence between grid values: the scalar Gaussian tail plus a union bound controls each level, and the sum of `2^-k sqrt(k+2)` is finite. The constants `4C sqrt(p)` at the initial corners and `60L0 sqrt(p)` for increments are safe upper bounds. Therefore `||Z_i^#||p≤C_Z sqrt(p)` conditionally on the cavity-good event. Using the event inclusion after conditioning yields S34 for each coordinate; averaging then proves S4. No exchangeability-to-moments shortcut occurs.

The clock weight is controlled by an exact scalar identity:

\[
 \partial_X\cosh^2j(X,g)=2\tanh j(X,g),\qquad
 \cosh^2w_a\le\cosh^2g_a+2|X_a|.
\]

Integrating `X'_a=-r_a Q_a` gives `sup|X_a|≤3T N_i`. Thus products needed for inverse gates and the later observation derivative are polynomial in `N_i` and Gaussian-root polynomial/exponential factors. Every separately fixed moment is finite by Holder, with no independence between roots and reached queries needed. A moment order `p>2` gives empirical square-tail expectation bounded by a constant times `R^{-(p-2)}`. Markov and `P(E_n^c)→0` prove the ordered finite weighted uniform integrability statement. This supplies error production in the source approximation; linear stability alone would not have supplied it.

For the uniform population source, the auxiliary finite *feature* equation over `[0,10]` has zero readout only for that auxiliary construction. Its deterministic polynomial bounds give the same cavity estimate with fixed controls. This is not a replacement of actual physical finite GF. Fixed-mesh value identification, same-root uniform mesh comparison, and mesh removal identify that auxiliary law with the already constructed canonical feature flow. Finite bounded continuous tests of finitely many rational parameter values transfer the envelope moments in expectation; monotone convergence then gives the countable dense envelope `N#`. L2 continuity extends its bound to every deterministic parameter in the appropriate equivalence class. Fubini provides the required almost-everywhere bounds for each deterministic observation measure. A samplewise continuous Gaussian-query path is not assumed.

Integrating the active feature clocks gives `|X_a|≤5N#`, hence `|cosh²(w_a)Q(u)|≤(cosh²(g_a)+10N#)N#`. The stated Holder estimate with `||N#||4≤2C_*` yields S45. This verifies finiteness of `M_w` on the entire physical reference. The sharper forcing norm T9 correctly uses `sum_a u_a²=1` and the maximum individual weighted norm, rather than adding an unnecessary factor `sqrt(2)`.

Finally, normalized-L2 continuity of the query together with its higher moments and the `L2/L8→L4` interpolation inequality gives weighted source continuity. The weight's change is bounded by the clock change, and the gate's input change by `|g|+C N#`. Thus the integrand is genuinely continuous into the tangent Hilbert space, with a compact separable range. Its Bochner integral against every finite signed measure exists, is linear, and is bounded by its sup norm times total variation mass. The same finite envelopes give the tight random source modulus and permit exact-mass finite-cell quadrature for arbitrary Borel laws. No total-variation approximation of a nonatomic law by atomic laws is used.

## 6. Actual derivative identification and limit order

The critical distinction in section lines 1692–1917 is between fixed-program identification and the finite-flow comparison. Both are supplied.

First fix a source cutoff `R`, a finite-cell law approximation with its exact masses, and a time mesh. Clipping `cosh²(w_a)Q` by two bounded factors produces globally controlled data/state differences on the reference bounds. The removed source error is small in the correct finite clock norm by the actual weighted tails proved above; all other source blocks are bounded ranks or bounded readout features. Choose `R` before the data mesh when using the displayed Lipschitz quadrature estimate. The reference atoms can be retained exactly. The law's smallest positive atom weight and Gram rank never enter.

Expand each reference and tangent learned matrix at the fixed mesh into its finite sum of ranks. All remaining matrix calls use the initialized matrix or its actual transpose. Tangent coordinate instructions are continuous and at most linear in their full input tuple: the tangent is multiplied only by a bounded gate, or by a bounded readout times a bounded gate. Clipping readout outside an already proved bound leaves values unchanged. Causal scalar contractions are recovered one instruction at a time. A.1 therefore supplies joint same-layer W2 laws and all quadratic contractions, including the HS norms of the finite rank expansions.

The actual finite readout is retained. The zero limiting root in the deterministic oracle is compared to the actual finite root at a separately fixed program. Its RMS and supremum discrepancies tend to zero; finite induction propagates this difference. This is not resetting the actual finite flow or its derivative.

The multiplier estimate F16 is the correct topology-specific tool. A changing bounded gate cannot be assigned a small operator norm from an L2 preactivation difference. Instead, on a fixed testing vector `V`, its product error is bounded by a cutoff times the L2 preactivation error plus the L2 tail of `V`. A compact L2 family has uniformly vanishing such tails, by a finite-net approximation. This proves population strong consistency on the compact family traced by the limiting tangent solution. The common generator bound then gives population tangent-Euler convergence F19.

For the actual finite tangent, subtract the affine finite mesh equation from the actual finite linear equation. The exact defect F20 has three terms: generator change on a mesh tangent, motion within a time cell, and source change. Source Lipschitz bounds and reference Euler error control the last two. For the first, the listed training directional maps exhaust the products:

- `D_a² xi_a` requires a gate multiplier test on `xi_a`.
- `B H1+A dot h1` adds bounded action/HS differences.
- `d phi'(Z2)+c phi''(Z2) dot z2` requires tests on `d` and `dot z2`; the readout difference is itself a bounded multiplier difference and only needs L2 smallness.
- The reverse variation has both `A* dot delta2` and `B* delta2`.
- Rank and scalar blocks use HS subtraction and Cauchy–Schwarz. The representing row `D_a²Q_a` needs the same bounded-gate cutoff argument.

At each fixed mesh all testing-node second moments converge. The population testing nodes over a refining mesh sequence form a relatively compact L2 family because F19, reference convergence, bounded actions, and strong multiplier continuity identify their uniform limits. Thus their tails are uniform in the refining mesh. Multiplying each finite-node cutoff error by its time-cell length and summing permits width first, mesh removal at a fixed test cutoff next, and final cutoff removal. This proves F21; it does not apply a width theorem to a transcript growing with width. Gronwall for the actual bounded finite generator then bounds the uniform finite tangent error by its integrated defect. Source-cutoff and quadrature errors are propagated by the same inequality. These arguments produce exactly F22's same-width proxy topology.

Passing rank contractions and directional measurements through F22 is valid. The estimates compare objects on the same finite carrier, while fixed-program limits identify their canonical counterparts. For a changed gate multiplying a tangent, F22 plus compactness supplies the necessary tails. There is no hidden coordinate-supremum tangent path-law claim or finite-to-population operator-norm distance.

## 7. Whole-circle observations

The Riesz observation field F23 includes the row factor `u_a D_a phi'(w·u)Q(u)`. Its tangent-Hilbert norm is uniformly bounded by the raw-gradient norm composed with the bounded clock-to-raw map. In population this gives `L0=sqrt(1+10[1+(2+sqrt(10))²])<17`. The hidden response bounds `1` and `3+sqrt(10)` also follow directly by bounded gates, action norm, and `||B||op≤||B||HS`.

Input variation of the observation field has one extra unbounded product, `|w|Q(u)`. It is supplied by the finite source envelopes and their canonical counterpart; it is not inferred from a generic L2 multiplication principle. Strong differentiation of the passive preactivations and queries is valid by the supplied curve chain rule. Fubini gives coordinatewise absolutely continuous query representatives; the gate-difference quotient is dominated by the L2 envelope `2|w| sup|Q|`. This justifies the product derivative and the H1 estimate, rather than merely writing a formal derivative.

The resulting finite observation H1 norm, uniformly in time, is bounded in probability. The Hilbert-valued fundamental theorem and Cauchy–Schwarz give a `|alpha-beta|^(1/2)` modulus. The tangent sup norm is bounded in probability by its linear equation and source bound. The reference observation field also has time equicontinuity: query time differences are L2 Lipschitz, and the changing first gates use the reference-query tails. The finite tangent derivative is bounded in probability, so the scalar predictor derivatives inherit time equicontinuity. Finite product nets in time and angle, followed by refinement after width, prove T10. This is stronger than checking a finite passive input list, and it uses no Gaussian-tail assertion for input derivatives.

## 8. Uniform population propagation and endpoint compatibility

In the clock tangent space, `R v=(D_a xi_a,B,d)` has norm at most one and is injective, but its inverse need not be bounded. The metric operator called `D` in P14 is `R*R`, with row multipliers `phi'(w_a)^2`, and identities on the remaining blocks. Direct adjunction gives `E=S*D`. Each tanh gate is positive almost surely since `w_a` is a finite L2 random variable; hence `D` is injective despite having no uniform lower bound.

For `alpha∈R²`, `alpha^T Gamma alpha=||RS alpha||²`. Thus

\[
 \ker\Gamma=\ker S=\ker E^*,\qquad
 \operatorname{ran}E=\operatorname{ran}\Gamma.
\]

The last equality is on the finite training space; the displayed inclusion in the proposal is sufficient. This compatibility is what excludes a nonzero nilpotent `SE` on a zero Gram mode. Positivity of `ES` by itself would not suffice.

The power-series identity `(SE)^j=S Gamma^{j-1}E` and compatibility prove P16, including a zero Gram and a rank-one Gram. `Gamma+` is a fixed finite-dimensional pseudoinverse at the endpoint; no trajectory pseudoinverse limit or lower bound on its positive eigenvalues is needed. Since `||exp(-2tau Gamma)-I||≤1`, the bound `B_infty=1+||S||||Gamma+||||E||` is finite. The limiting projection has the stated range and kernel, and after applying `R` it becomes the raw orthogonal projection off the weighted gradient span. The raw interpretation is restricted to the image of the admissible clock domain; it does not require a bounded inverse of `R` on the raw Hilbert space.

An independent infinite-dimensional boundary check tests exactly the missing-coercivity issue. On `ell²(N)`, let `D e_j=4^{-j}e_j`, `g_j=2^{-j}`, and `S(a,b)=(a+2b)g`; set `E=S*D`. Then `D` is injective and has no positive lower bound, `gamma=<g,Dg>=1/15`, and `Gamma=gamma [[1,2],[2,4]]` has rank one. Here

\[
 SE=5g\otimes Dg,\quad
 e^{-2tSE}=I+(e^{-2t/3}-1)\,15g\otimes Dg.
\]

This is uniformly bounded because `||g||²=1/3` and `||Dg||²=1/63`. It confirms that the proof's finite-rank compatibility, rather than coercivity of the ambient metric, is the needed mechanism. Conversely `S=(1,0)^T`, `E=(0,1)` has `ES=0` and a nonzero nilpotent `SE`, so the unrestricted factorization argument would fail. The supplied check explicitly tests that counterexample.

For the actual time-dependent generator, the coefficients are strongly continuous, not generally norm-continuous. Fixed-vector multiplier truncation proves strong continuity of curvature. Only the finite-rank synthesis and evaluation fields need norm convergence at the endpoint. P18–P19 follow by factor subtraction with bounded endpoint readout. The extra evaluation multiplier difference satisfies

\[
 \|[\phi'(w_a)^2-\phi'(w_{a,\infty})^2]Q_{a,\infty}\|_2
 \le2\|Q_{a,\infty}\|_4\|w_a-w_{a,\infty}\|_2^{1/2}.
\]

This follows from `|gate²-gatebar²|≤min(1,4|w-wbar|)` and Holder; it requires the supplied endpoint L4 bound. It does not assert operator-norm convergence of a general multiplier. Subtracting `-2S_infty E_infty` from the full generator yields P21. Integrating `e≤exp(-t/5)` and its square root gives exactly

\[
 J_0=20L_0a_*\sqrt{10}+10a_*+40L_0M_4\,10^{1/4}.
\]

The residual-curvature contribution is included. Picard's absolutely summable integral series constructs the strong homogeneous evolution on every finite interval with the common operator bound. Variation of constants around the endpoint semigroup and scalar integral iteration then give `||U(t,s)||≤B_infty exp(B_infty J0)` uniformly for `s≤t`. For continuous data forcing the unique solution is strongly C1; for strongly measurable locally integrable forcing it is absolutely continuous and solves its equation almost everywhere. The distinction in the statement is correct.

## 9. Adversarial checks, commands, and outcomes

The check contract was written before new numerical checks. All runs were deterministic and all completed with exit zero; no failed run, excluded fixture, or parameter retuning occurred. Environment for the supplied identity run: Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0.

Exact commands, run from `/home/amir/Codes/PDE`:

```text
python studies/trained_data_response/P1_CHECK_IDENTITIES.py --output data/generated/trained_data_response/assessment_fresh_a_20260911/identities
python studies/trained_data_response/P1_REFERENCE_CERTIFICATE.py
python data/generated/trained_data_response/assessment_fresh_a_20260911/independent_checks.py
```

The two supplied programs were executed unchanged and in full. Their complete stdout/stderr/return codes are retained in `prescribed_check_1.json` and `prescribed_check_2.json`; the first also writes `identities/results.json`.

| Check | Result | Logical reach |
|---|---|---|
| Supplied transformed finite tangent central differences | Errors `1.0292819331e-6`, `2.5732050750e-7`, `6.4330121850e-8`, `1.6082636076e-8`; all required second-order ratios pass | Checks local algebra, not a flow or width theorem |
| Supplied raw loss/metric pairing | Absolute error `7.9006801101e-12` | Checks mobilities and normalization |
| Supplied singular semigroup identity | Maximum discrepancy `1.5265444420e-14` | Checks singular finite algebra; includes the incompatible nilpotent control |
| Exact rational Gaussian certificate | `[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`; all exact assertions pass | Certifies the reference lower/upper moment margins with outward rational rounding |
| Fresh complex-step derivative of the full transformed field | Maximum error `2.2204460493e-16` | Independent implementation at fixed asymmetric width two, nonzero stored readout, and off-axis signed forcing |
| Fresh full-minus-cavity forward/reverse identities | Maximum error `5.5511151231e-17` | Checks the exact subtraction and both orientations with unequal learned increments/readouts |
| Fresh clock boundary checks | Maximum primitive residual `1.4210854715e-14`; envelope holds including equality at `g=X=0` | Tests both signs and large clock changes across the origin |
| Fresh exact rational metric projection | Exact idempotence, evaluation-kernel identity, and metric symmetry | Tests a singular rank-one training Gram with very unequal positive metric weights |

The fresh script hash is `9b1b5695f68588bfe9cacfdb0ffaf4178af7fb3fad3a72953499428569037f8a`. Its source and full results are preserved in the assigned scratch. Its zero signed-source check also passed exactly.

The rational reference certificate is more than floating-point quadrature: its exponential remainders, alternating arctangent bounds for the density constant, monotone endpoint quadrature, Gaussian tail allowance, and per-term outward rounding all have the correct directions. The printed decimals only summarize exact rational comparisons. Conversely no numeric check evaluates the actual endpoint Gram or validates the enormous propagator constant numerically; the proposal expressly makes neither claim.

The principal attacks and dispositions were:

| Attack | Potential consequence | Disposition |
|---|---|---|
| Condition on the full good event and falsely keep a deleted column Gaussian | Would invalidate finite source moments | Avoided by `E_n^i` measurability and `E_n⊂E_n^i` |
| Delete training feedback or freeze cavity residuals | Would prove an easier model | Avoided; S22–S24 contain residual differences and learned increments |
| Infer weighted moments from RMS convergence | Would leave forcing and observation tails open | Avoided by finite conditional query moments and exact clock-weight envelope |
| Replace a reused transpose by an independent matrix | Would change both forcing and curvature | Avoided by actual conditioning, finite transpose identities, and rank expansion |
| Use only `Gamma≥0` at a singular endpoint | Could permit nilpotent growth | Closed by exact injective-metric kernel compatibility |
| Convert L2 gate convergence into multiplier norm convergence | Would invalidate tangent consistency | Avoided by fixed-vector cutoff tests and compact testing families |
| Apply fixed-program width convergence at a shrinking mesh directly | Would not establish actual finite derivatives | Avoided by F20–F22 and explicit width-first cutoff/mesh order |
| Upgrade finite input-list convergence to the whole circle without a modulus | Would leave T10 unsupported | Closed by the weighted observation H1 bound and time equicontinuity |
| Treat zero limiting readout as zero actual initialization | Would change the finite derivative | Avoided by a same-array fixed-program comparison retaining actual finite readout |
| Approximate nonatomic laws in total variation by finite laws | Would fail | Avoided by bounded/Hölder data integrands and exact cell-mass quadrature |

## 10. Surviving gaps, corrections, and interpretation

**No required mathematical correction was found for the exact proposed scope.** The source finiteness, uniform population propagation, fixed-horizon finite derivative identification, and whole-circle observation conclusions have complete bridges under the supplied hypotheses. The proof constants are extremely large but finite; lack of a useful numerical constant is not a gap in the stated finiteness theorem.

Optional presentation suggestions, not conditions of acceptance:

1. In the final exclusion list, “endpoint continuity” could be written “continuity of fitted endpoints as the training law changes.” The reference itself has a proved strong endpoint, so this wording would remove possible ambiguity.
2. A short sentence could state the noncommuting limits in application notation: finite `n` first gives the epsilon derivative; its width limit is then identified at fixed `T`. The existing sections already say this accurately.

For finite contamination versus infinitesimal response, the strongest justified application is precise. For every finite `n` and fixed `T`, smooth finite-dimensional dependence supplies an expansion

\[
 f_{n,\mu_\epsilon}(t,x)
 =f_{n,\nu_*}(t,x)+\epsilon D_\sigma f_n(t,x)
                  +o_{n,T}(\epsilon)
\]

uniformly on the compact time/circle domain. The new theorem identifies the coefficient `D_sigma f_n` as width grows. It supplies no width-uniform control of the remainder `o_{n,T}(epsilon)`, no nonzero contamination radius valid uniformly in width, and no limiting nonlinear changed-law flow on the full horizon. Consequently it cannot be used to approximate a fixed contaminated law by the linear response after sending width to infinity. The additional nonlinear products listed at the end of the candidate are actual missing obligations for that different theorem.

The homogeneous bound also does not imply a time-uniform forced response: bounded forcing gives the stated bound proportional to `T ||sigma||TV`, and persistent forcing may act in directions preserving fitted training predictions. The endpoint projection permits unseen first-order evaluations but proves neither that they are nonzero nor that they improve risk. Finite-width capture is for each fixed law and horizon, with no common law-uniform failure probability or width rate. There is no derivative theorem for raw GD, no sampling CLT, no expected-risk expansion, and no empirical-law total-variation approximation for a nonatomic distribution.

These limitations are already reflected accurately in the candidate section and its revised guide/navigation statements. They should remain attached to the accepted infinitesimal theorem.
