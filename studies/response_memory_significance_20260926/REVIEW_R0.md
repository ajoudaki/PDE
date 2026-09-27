# Round 0 isolated adversarial review of `CANDIDATE_V0`

## Recommendation

**Major revision.** I do not find a fatal mathematical error in either compact-horizon convergence theorem. The ordinary-clock proof is substantially complete, and the response-clock theorem is supported by a valid detailed argument in the frozen theorem evidence. The paper nevertheless is not ready in its present form. Its central Variant-B state count and resulting accuracy-versus-state scaling omit an evolving Gram matrix; its headline compression language is stronger than the theorem and resource evidence; the closest ingredient and dynamical precedents are mostly absent from the bibliography; the response-clock proof in the manuscript is only an architecture rather than a complete proof; and a substantial subset of the numerical claims has no corresponding frozen evidence in the review packet.

Within the supplied literature set, I found no earlier result that satisfies the complete claimed contract simultaneously: fixed finite width and data, deep nonlinear feature-learning gradient flow, a finite scalar autonomous state of size independent of elapsed time, reconstruction of the learned internal-matrix increments, and uniform approximation of the complete physical parameter trajectory on every prescribed finite interval as order tends to infinity. That is the defensible theoretical contribution. It is materially narrower than an unqualified claim of neural-training compression, a practical resource reduction, or a new use of online polynomial memory.

## Review scope and reading coverage

I worked under the isolated-review restriction and did not browse, inspect Git history, read another study, inspect a live manuscript, or read any advocate report. I verified the supplied hashes of `CANDIDATE_V0.tex`, `CANDIDATE_V0.pdf`, `REFERENCES_V0.bib`, and all enumerated local evidence files against `LITERATURE_PACKET.md`. The candidate TeX was read line by line and checked against the rendered PDF. The bibliography was read in full.

I read the complete theorem and experiment reports `DEEP_ACTIVATION_ERROR_THEOREM.md`, `RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md`, `ORACLE_FINITE_HORIZON_BOUND.md`, `CANONICAL_FLOW.md`, `DEEP_CIRCLE_RESULTS.md`, and `MNIST100_RESULTS.md`, and inspected all three enumerated CSVs. I statically inspected the dense, ordinary-clock, weighted-clock, state-accounting, runner, and deterministic-check portions of `compact_flow.py`; I did not audit every unrelated dictionary-construction helper line. I read the relevant complete closure section C.4.7.9 of `BOOK_OBSERVABLE_CLOSURE.qmd` and the compact-horizon/stability material needed from `BOOK_TRAINABILITY.qmd`, rather than every chapter line.

For each supplied primary-source PDF, I checked the abstract and the anchors named in the packet. I additionally inspected the equations and surrounding argument needed for the comparisons below, especially HiPPO Definition 1, Theorem 2, Propositions 3--6 and Appendix D.3; NTH Assumptions 2.1--2.2, equations (2.1), (2.2), (2.7), (2.11), and Theorem 2.6; Tensor Programs IV Theorems 3.6, 3.8, 5.6, 6.4, 7.4, Corollary 3.9 and Algorithm 1; the DMFT equations, algorithm and complexity table; the multilayer mean-field and Neural Feature Flow definitions and approximation theorems; and Mori--Zwanzig equations (2.7) and (3.1). I did not read every appendix of every literature PDF cover to cover.

An attempted execution of `compact_flow.py --check-clock` with the default environment failed before running because that Python environment has no `torch` module. I therefore rely on static code inspection and the frozen check records, not an independent rerun. No file other than this report was edited.

There are three material coverage limits. First, the packet is explicitly nonexhaustive, so it cannot support an unrestricted priority claim. Second, `wide_linear_dynamics_1902.06720.pdf` is actually Lee et al., *Wide Neural Networks of Any Depth Evolve as Linear Models Under Gradient Descent*, not the Arora et al. paper named in the packet. Third, `sirignano_spiliopoulos_1805.01053.pdf` is *Mean Field Analysis of Neural Networks: A Law of Large Numbers*, not the claimed central-limit-theorem paper. The Celentano et al. citation in the candidate bibliography was not supplied as a source. These missing sources are recorded rather than silently replaced.

## Contract verdict

| Contract item | Verdict | Basis and qualification |
|---|---|---|
| Deep fully connected network, fixed finite width/sample count, hidden depth at least two, nonlinear feature learning | **Met** | Candidate Section 2 and Theorems `thm:old` and `thm:new`; local smoothness hypotheses are essential. ReLU and standard SELU experiments lie outside those smooth ODE theorems. |
| Learned internal increments compressed while retaining initialized matrices and outer blocks | **Met algebraically; misstated quantitatively** | Equation `eq:exact-history` and reconstructions `eq:old-recon`/`eq:new-recon` are correct. The Variant-B evolving Gram and fixed prefix factors are omitted from the headline count. |
| Autonomous, restartable order-`P` state with history storage independent of elapsed time | **Met** | The saved moments, clock, physical outer blocks, fixed `W_0`, and, for Variant B, Gram and prefix data suffice. State grows with order but not elapsed time. |
| Uniform complete physical-parameter approximation on each fixed `[0,T]` as order tends to infinity | **Met** | Theorems `thm:old` and `thm:new`. Constants and admissible starting order may depend on fixed width, depth, data, initialization and horizon. |
| Ordinary-clock `O_T(P^{-1})` | **Met** | Equation `eq:old-rate` is `1/sqrt(P(P+1))`; the proof uses only forward-history `H^1` regularity and a coarse backward-history energy. |
| Response-clock `O_T(P^{-2})` | **Met mathematically, incompletely proved in the manuscript** | Equation `eq:new-rate` follows from the joint unit-speed history and the stopped residual/clock continuation argument. The full quantitative bootstrap is only in the frozen supporting theorem report. |
| Circle/MNIST predictor fidelity | **Partly met** | Deep-circle and MNIST claims are supported for the stated matched-loss, mostly single-initialization experiments. Shallow-circle and dictionary/factorization numbers lack enumerated frozen evidence. None of the experiments estimates the same-time trajectory rates. |

## Mathematical audit of the two clocks

### Ordinary activity clock

I find the reconstruction and convergence mechanism valid under the stated assumptions.

1. The shifted-Legendre identity `eq:triangular` gives the moment ODE `eq:old-ode` after differentiating the dilated basis. The initialization and the zero backward prefix give the correct exact initial matrix.
2. Orthogonality gives `eq:projection-form`; differentiating its raw and projected energies gives the exact endpoint identity `eq:projection-energy`. The backward-prefix jump does not enter the `H^1` tail estimate and is harmless for this energy identity.
3. The Legendre tail Lemma `lem:legendre` has the right normalization: the Sturm--Liouville energy of mode `k` is `k(k+1)/(2k+1)`, so modes `k >= P` give the factor `1/[P(P+1)]`.
4. Differentiating the reconstructed product cancels both mixed projection terms and yields the product-of-errors defect `eq:defect`; Cauchy--Schwarz gives `eq:defect-energy`.
5. Only the forward histories require an `H^1` bound. In the depth induction, endpoint evaluation costs order `P`, while the Legendre tail contributes order `P^{-1}` in norm; `eq:e-square` correctly prevents a further loss with depth.
6. Dense loss dissipation gives global finite-time existence and a common compact ball. The first-exit argument plus `eq:old-defect-bound` and Gronwall gives `eq:old-explicit`. The bounded-activation corollary supplies order-independent physical bounds for every `P >= 1` on each finite interval.

I found no circular assumption of closure accuracy in this proof. The result is fixed-width and compact-horizon; it does not give a useful order threshold or a width-uniform statement.

### Joint response-speed clock

The core argument also checks out, but the submitted proof is too compressed.

1. With `g = rho + ||dot(Psi)||`, the physical-history density is `rho/g <= 1`, so `d mu <= d xi`, and the concatenated response path is one-Lipschitz in the new coordinate.
2. Equations `eq:new-recon`--`eq:new-ode` yield the endpoint fits `H G^{-1}e` and `U G^{-1}e`. Product differentiation cancels the dilation terms and produces `eq:new-defect`, with no hidden derivative of `g`.
3. The weighted projection residual satisfies the same exact accumulated endpoint-error identity. Weighted best approximation is bounded by ordinary Legendre approximation because `d mu <= d xi`. Applying the scalar tail bound to the full concatenated path gives the `P^{-2}` squared-error bound, and arithmetic--geometric mean gives the integrated physical defect of order `1/[P(P+1)]`.
4. The apparently implicit clock is executable as written in `eq:internal-velocity`: first form the physical velocity, then apply directional forward and reverse passes to compute `dot(Psi)`, then update the moments and Gram. No nonlinear scalar clock solve is needed.
5. The difficult continuation step is valid in the detailed frozen proof: raw-history energy first gives an order- and clock-independent coarse integrated-defect bound; dense residual has a positive lower bound on a fixed finite interval when initially nonzero; `D Psi` is bounded on the residual tube; this bounds the clock before a possible residual exit; the sharp estimate then keeps the closure residual in the tube for `P >= P_0(T)`; the matching prefix gives a positive Gram eigenvalue for each fixed `P`; and compactness extends the ODE through `T`.

The Gram lower bound need not be uniform in `P`, and the theorem does not claim numerical conditioning. That is logically sufficient for exact ODE existence, but it leaves finite-precision behavior uncontrolled.

## Numbered objections and required revisions

### O1. **Major -- incorrect Variant-B state count and accuracy-versus-state scaling**

The abstract, Table `tab:complexity`, and the paragraph following that table state that the moving internal state is `2(H-1)mnP` and infer a Variant-B moving-state scaling `O(Hmn epsilon^{-1/2})`. Yet `eq:new-ode` evolves a shared symmetric `P x P` Gram matrix. The frozen deep theorem report, Section 7, explicitly counts `P(P+1)/2` Gram entries, one clock, and fixed matching-prefix vectors; `WeightedFlow.state` in `compact_flow.py` in fact stores a full `P x P` Gram tensor and the clock.

With common outer blocks included, the minimum scalar counts are

\[
\begin{aligned}
S_{\rm dense} &= nd+n+(H-1)n^2,\\
S_A^{\rm moving} &= nd+n+2(H-1)mnP+1,\\
S_B^{\rm moving} &= nd+n+2(H-1)mnP+\frac{P(P+1)}2+1
\end{aligned}
\]

when the Gram is symmetry-packed; the supplied implementation stores `P^2`, not `P(P+1)/2`, Gram scalars. Both closures additionally retain `(H-1)n^2` fixed initialized-matrix entries. Variant B also needs fixed matching-prefix factors, minimally `2(H-1)mn` scalars if they are saved rather than recomputed. The prefix outer products `C_{ell a}` should remain factorized; materializing them would be much worse.

Consequently, using the theorem's sufficient `P = O(epsilon^{-1/2})`, the complete Variant-B moving internal state scales as

\[
O\!\left(Hmn\,\epsilon^{-1/2}+\epsilon^{-1}\right),
\]

not solely `O(Hmn epsilon^{-1/2})`. At fixed `n,m,H`, the Gram term eventually dominates as `epsilon -> 0`. Calling only the history factors “moving learned state” does not repair the autonomous-state accounting: the Gram is evolving state required to reconstruct and advance those factors.

**Required revision:** correct the abstract, Table `tab:complexity`, the epsilon-scaling paragraph, conclusion, and every state comparison. Report both a theory-minimum symmetry-packed count and the actual `P^2` implementation count. List outer blocks, clock, Gram, prefix factors and `W_0` separately. If the authors wish to quote `O(Hmn epsilon^{-1/2})`, label it explicitly as *history-factor storage only*, not the closure state.

### O2. **Major -- the manuscript does not establish net memory or runtime compression**

The exact inequality requested by the scientific contract is absent. The history factors alone are smaller than the dense internal matrices exactly when

\[
2(H-1)mnP < (H-1)n^2 \quad\Longleftrightarrow\quad 2mP<n.
\]

For the complete moving Variant-B internal state, even before fixed prefixes, the comparison is

\[
2(H-1)mnP+\frac{P(P+1)}2+1 < (H-1)n^2.
\]

The convergence theorem only asserts existence of a task-dependent `P_0(T)` and constants. It does not show that an order satisfying the error target and `P >= P_0(T)` also satisfies either compression inequality. Since the theorem takes `P -> infinity` at fixed `n`, its autonomous state eventually exceeds the dense moving state.

Total minimal storage is also not reduced: adding the retained `(H-1)n^2` entries of `W_0` makes either closure strictly larger than a dense implementation that stores only the current internal matrices. The candidate acknowledges this later for MNIST, but the abstract and final “smaller state” wording remain too broad.

Nor is a full action subquadratic in width under the stated implementation. Each forward and transpose action includes a direct `W_0` or `W_0^T` multiply costing `O(n^2)` per vector, plus a learned-correction action `O(nmP)`. A full batch therefore includes the initialized cost `O(mn^2)` as well as the factor cost `O(nm^2P)` per link and direction. Variant B further pays `O(P^3)` for a shared factorization, `O((H-1)mnP^2)` for solves, Gram dilation, and directional forward/reverse passes. The Table row called “One full-batch action” currently lists only the learned-correction term.

The measured evidence is unfavorable to an end-to-end resource claim. On MNIST100 the minimum moving-plus-fixed totals are 158.78, 165.03 and 171.28 MiB for `P=1,2,3`, compared with 152.53 MiB dense, and integration times are 139.89, 149.92 and 152.27 seconds versus 102.98 seconds dense. In the deep-circle campaign every finest closure run is slower than dense. In the 21 matched response-clock rows in the supplied CSV, the new-clock runtime is about 1.79--3.99 times the corresponding old-clock runtime (median 2.16). Lower measured CUDA peaks reflect solver workspace behavior, not smaller minimal total state.

**Required revision:** narrow the title/abstract/conclusion to compression of the *learned increment representation*. Add the exact inequalities above and a full storage/runtime table. Do not call the result a memory or speed compression theorem without an additional result proving a nonempty accuracy/order range below the dense count and an implementation that addresses the retained operator.

### O3. **Major -- HiPPO and Neural Tangent Hierarchy, the closest ingredient and autonomous-truncation precedents, are omitted**

The bibliography has only four entries and omits both works.

HiPPO Definition 1 (main-text p.3) formalizes online optimal projection of a cumulative history onto a finite polynomial space. HiPPO-LegS Theorem 2 (p.5) gives a closed scaled-Legendre coefficient ODE over all past time, Propositions 3--6 (pp.5--6) give scaling, update, gradient and approximation properties, and Appendix D.3 equation (29) (PDF p.31) derives the triangular dilated Legendre dynamics. This is direct precedent for the paper's scaled-history coordinate, Legendre moments and autonomous state whose dimension does not grow with elapsed time. HiPPO does **not** supply the paper's feedback-coupled pair of neural forward/backward histories, product reconstruction of learned matrices, fixed-width physical-trajectory comparison, or continuation theorem. It therefore narrows the ingredient novelty but does not displace the full neural theorem.

Neural Tangent Hierarchy is an even closer dynamical comparison. In its notation `n` is sample count and `m` is width. Equations (2.1)--(2.2) (p.6) are an exact infinite output/kernel hierarchy; equation (2.7) (p.8) makes an autonomous order-`p` truncation by freezing the top kernel. Evaluated on the training set, the order-`r` tensor has up to `n^r` values, so the stored hierarchy and a full top contraction are dominated by `O(n^p)` before symmetry. In the candidate's notation that is `O(m^p)` sample-indexed state and work, in sharp contrast to `O(HmnP)` response factors.

Theorem 2.6 (pp.8--9) assumes even `p`, Assumptions 2.1--2.2, and a positive initial-kernel eigenvalue. Translating to candidate notation (width `n`, samples `m`), its horizon is

\[
t\le \min\!\left\{\frac{c\sqrt{\lambda n/m}}{(\log n)^C},
\frac{n^{p/[2(p+1)]}}{(\log n)^{C'}}\right\},
\]

and its output-error bound in equation (2.9) scales as

\[
\frac{(1+t)t^{p-1}\sqrt m}{n^{p/2}}
\min\{t,m/\lambda\},
\]

with the kernel error in equation (2.10). The test-point construction (2.11), p.9, adds one-test-point tensors through order `p`, up to `O(m^{p-1})` extra values per test point, in addition to the training hierarchy. The supplied paper gives equations, not a demonstrated executable NTH solver or NTH experiment. Its regime is wide/NTK-scaled: kernel motion is a finite-width correction of order `1/n`, rather than leading-order feature learning, and its represented objects are outputs and kernels rather than the complete finite-width parameter trajectory.

**Required revision:** add both sources and a contract table stating these exact overlaps and mismatches. The paper may claim that its *neural feedback/reconstruction and fixed-width trajectory theorem* go beyond HiPPO, and that it avoids NTH's exponential-in-order sample tensors while treating a different regime and object. It may not present online Legendre memory or autonomous hierarchy truncation as if no close precedent existed.

### O4. **Major -- the broader related-work positioning is too sparse to support the novelty language**

Several supplied works address leading-order feature learning or autonomous dynamical descriptions much more closely than the manuscript acknowledges:

| Prior source and exact anchor | Contract comparison |
|---|---|
| **Tensor Programs IV**, Theorems 3.6/3.8 and Corollary 3.9 (pp.9--10), Definition 5.1 and Theorem 5.6 (pp.13--14), Theorem 6.4 (pp.20--21), Algorithm 1 and Theorem 7.4 (pp.24--25) | `muP` has leading-order feature learning at infinite width. It represents coordinate distributions/random variables, not a fixed finite-width parameter trajectory. The limit is for each fixed discrete training time; Theorem 6.4's formulas contain sums over all prior steps and additional past-indexed Gaussian variables, so a direct representation grows with elapsed steps and can become computationally prohibitive. Algorithm 1 is executable in principle and the paper reports experiments. The candidate cites this work only for mobilities and never makes this comparison. |
| **Feature-learning DMFT**, equations (5)--(10), pp.3--5; Section 4; Section 7 and Table 1, p.10; Appendix B Algorithm 1, p.19 | Infinite-width rich feature learning is represented by self-consistent two-time activation, gradient and response kernels/fields. On a grid with `P` samples and `T` times in that paper's notation, Table 1 reports `O(P^2T^2)` kernel memory and `O(P^3T^3)` kernel time. The solution is an alternating Monte Carlo computation and the derivation is physics-level rather than a fixed-finite-width trajectory theorem. |
| **Finite-width DMFT**, Proposition 1 and covariance formulas; Section 7/conclusion | Gives perturbative `N^{-1/2}` fluctuations and `N^{-1}` mean corrections around DMFT order parameters, not an exact finite-width closure. The general deep Hessian has `O(T^4P^4)` entries to store/invert. |
| **Pham--Nguyen multilayer mean field**, Section 2.2 (pp.10--11), Theorem 7 (p.15), Definitions 11--12 (pp.17--18), Theorem 15 (pp.19--20) | A deep nonlinear autonomous mean-field ODE evolves functions on neuronal source spaces; finite networks couple to it on compact horizons as width and step size tend to their limits. It follows parameter-like fields but has infinitely many scalar degrees of freedom and is not a fixed-width matrix compression. The candidate cites it but does not explain this contract. |
| **Neural Feature Flow**, Section 3 (pp.7--8), Definition 1 (pp.10--11), Theorems 1--4 (pp.12--15) | Evolves probability measures over features and pair functions on their supports, has well-posed autonomous flow, and quantitatively approximates a wide finite network for width at least approximately `epsilon^{-2}` under its assumptions. It is a fixed-type but infinite-scalar state and a width-limit result, not the candidate's finite-width moment closure. It is uncited. |
| **`BOOK_OBSERVABLE_CLOSURE.qmd` C.4.7.9**, theorem in part 1 and saved-state equations in part 3 | Already gives increasing autonomous population systems, restartability from their saved state, and compact-time/whole-circle convergence of predictions and joint observations for a specific nonlinear population model. Its state is two probability laws plus a finite matrix, hence infinitely many scalar degrees and a different model. This sharply narrows “new lens” language and must be discussed. |
| **Mori--Zwanzig**, equation (2.7), PNAS p.2969, and equation (3.1), p.2970 | Exact projection produces a Markov term, memory integral and noise; dropping memory gives first-order optimal prediction. This is conceptual projection-memory precedent, although it has no neural fixed-width Legendre reconstruction theorem. |

The remaining supplied literature sets further boundaries. NNGP (abstract; Sections 1.2 and 2.3) is an untrained infinite-width function prior. NTK Theorems 1--2 and Section 5 give a constant limiting kernel and linear function-space flow. The actual supplied Lee et al. paper gives an all-time lazy-regime linearization in Theorem 2.1/equation (17), with parameter, output and kernel discrepancies of order width `^{-1/2}`, and includes implementation/experiments; hidden features move vanishingly in that regime. Schoenholz et al. Sections 2--4 and Pennington et al. equation (2), Sections 2--3 concern initialization signal propagation and input-output Jacobian spectra. Mei--Montanari--Nguyen Theorem 3, Chizat--Bach Definition 2.4/Theorem 2.6, and the actually supplied Sirignano--Spiliopoulos Theorems 1.2/1.6 give shallow distributional/particle limits, not deep fixed-width parameter compression.

None of these supplied results matches the entire candidate contract. That is the appropriate novelty statement. The packet does not justify “first” or unrestricted priority language, and different terminology cannot substitute for these comparisons.

**Required revision:** replace the current broad two-paragraph discussion with a contract-level related-work section covering regime, represented object, exactness, state scaling in all relevant variables, horizon/mode of convergence, retained operators/computation, and tested observable. Cite the local population theorem if it is being used as established companion work. State explicitly that priority is only assessed relative to the reviewed set unless a genuine systematic search is added.

### O5. **Major -- the response-clock theorem is not fully proved in the submitted manuscript**

The proof labeled “Proof architecture” after Theorem `thm:new` states, without enough derivation for independent verification, that raw histories give an order-independent coarse defect bound, that the dense residual has a finite-horizon positive lower bound, that `D Psi` is bounded on a residual tube, and that these facts close clock, residual, Gram and existence stops. Those are the nontrivial parts of the theorem; without them, the use of a bounded clock in the sharp approximation estimate would be circular.

The frozen `RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md` resolves this correctly in equations (11)--(27): it supplies physical bounds, coarse defect (14), path variation (15), the Lipschitz constant (16), residual lower bound (18), normalized-response derivative bound (19), clock bound (20), sharp defect (22), explicit order condition (25), residual separation (26), Gram lower bound (27), and the final first-exit/continuation argument. The deep theorem report extends the same structure to arbitrary fixed depth and the stated activation classes.

This is a **missing-proof-detail objection, not a mathematical invalidity finding**. The full evidence convinced me that the result is repairable without changing its statement.

**Required revision:** include the quantitative stopped argument in the paper or a submitted appendix, generalized at the stated depth. Define the stopped domain, derive the coarse estimate before assuming a clock bound, show the normalized residual derivative estimate, state a valid `P_0(T)` condition, and give the fixed-`P` prefix-Gram continuation argument. The proof must not rely on unpublished frozen study files.

### O6. **Major -- several prominent empirical and baseline claims have no enumerated frozen support**

The shallow-circle table and Figure `fig:circle-shallow` report exact `P=1,3,7` values, including 0.2363, 0.0730 and 0.00466. Section “Why this is not a frozen dictionary” reports dictionary discrepancies 1.100, 0.756 and 0.896, a `29`-cell win claim against trained factorization, and errors 0.004663 versus 0.516210 and 0.251026. None of these numbers appears in the enumerated `DEEP_CIRCLE_RESULTS.md`, `MNIST100_RESULTS.md`, the three CSVs, `CANONICAL_FLOW.md`, or the relevant implementation records. The PDF embeds plots, but the packet supplies no raw results, protocol, seeds, stopping details, numerical-refinement evidence, or machine-readable table for these claims.

By contrast, the depth-three circle and MNIST100 claims are traceable to the supplied reports and CSVs. The unsupported claims are especially consequential because the dictionary/factorization paragraph is used to argue a mechanism-specific advantage.

**Required revision:** add frozen raw predictions/metrics and a protocol report for the shallow-circle and all dictionary/factorization comparisons, including initializations, exact ranks/state budgets, stopping rule, solver resolution, all attempted cells and exclusions. Otherwise remove the exact numbers, the `29`-cell statement, the corresponding figure/table, and the mechanistic empirical conclusion.

### O7. **Moderate -- the experiments do not test the theorem's trajectory or rate claims, and the adverse response-clock results need fuller disclosure**

The deep-circle and MNIST comparisons stop each system at its own first training-MSE crossing. They test fitted-predictor agreement, not same-physical-time parameter trajectories, and usually use one initialization. This distinction is disclosed, but it means the empirical section cannot validate `eq:old-rate` or `eq:new-rate`, the complete physical state, or monotone convergence with order. The realized order trend is nonmonotone: in the deep-circle data, `P=3` is worse than `P=2` on both alternating tasks; on MNIST the held-out RMS is 0.00108443 for `P=2` and 0.00119922 for `P=3`.

The response-clock evidence is also less favorable than the selected sentence suggests. At maximum step `1/64`, the GELU depth-three alternating-quadrant discrepancy is 1.245 at `P=3`; at `1/128` it is 0.112. The shared-step experiment is therefore not a continuous-flow certificate. The `P=4,5` extension is worse for the new clock on that same task: new-clock `P=5` is 0.99568 at `1/64` and 0.10313 at `1/128`, while the old clock is 0.01279 and 0.02150. A larger order did not cure the finite-step result. The maximum recorded main-panel Gram condition is about 330.9.

In the 82-case sweep, dense, `P=1`, `P=2`, and `P=3` reach the strict training target in 79, 70, 67 and 66 cases. On fitted pairs, median discrepancies are 0.042725, 0.018895 and 0.006795, but maxima are 3.661275, 3.240721 and 1.362737; 17 cases contain at least one miss. Several activations in that sweep are outside the smooth theorem. These data support implementability and some useful low-order cases, not reliability, the asymptotic rate, or a practical advantage of the response clock.

**Required revision:** present fitted-pair denominators, worst cases, high-order extension, Gram conditioning and step sensitivity in the paper. Add same-time curves for parameter norm error, training predictions and passive predictions across enough orders to estimate a slope, with solver refinement demonstrably below closure error and multiple initializations. Until then, describe all numerical evidence strictly as endpoint predictor fidelity.

### O8. **Moderate -- source and reproducibility coverage is insufficient for some comparison claims**

The two mislabeled PDFs prevent the mandated exact comparison with Arora et al.'s equivalence theorem/algorithm and with the claimed Sirignano--Spiliopoulos CLT. The Celentano source is absent, so the candidate's phrase “rigorous ... high-dimensional DMFT results” cannot be checked from the frozen packet. The candidate bibliography also omits virtually every work needed for the contribution's positioning.

**Required revision:** supply the correct primary PDFs and bibliography entries, verify that each cited claim matches the actual theorem, and provide a build-complete versioned source bundle. The review should be repeated for the corrected related-work claims. No novelty conclusion should be inferred from the present packet's omissions.

### O9. **Minor -- notation and presentation defects obscure otherwise correct statements**

Equation `eq:new-clock` repeats `(a_{ell a},b_{ell a})` in the definition of `Psi`. The response-clock discussion should distinguish the mass `A`, coordinate length `L`, theoretical symmetry-packed Gram, and implementation's full Gram. “All hidden responses ... on passive inputs” in Theorem `thm:old` should say forward activations and predictions unless a labeled backward observable is defined for passive points. Table `tab:complexity` should rename “One full-batch action” to “one learned-correction full-batch action” if it continues to omit the retained `W_0` multiply. The manuscript should also consistently reserve “global on compact horizons” for the quantified finite-`T` statement; its current definition does this correctly and should be used everywhere.

**Required revision:** correct the duplicated formula and terminology, define every counted state class once, and align table row labels with the operations actually counted.

## Overall assessment of significance

The defensible contribution is a nontrivial fixed-width approximation theorem: the exact low-rank-in-time learned increment is represented through two coevolving response histories; polynomial moment truncation produces an autonomous finite ODE; and an exact product-of-projection-errors identity turns history approximation into complete physical-trajectory control despite nonlinear feedback. The response-speed clock improves the proven order by regularizing the joint path, and the continuation argument is substantive.

The result does not presently answer “how much” in a resource sense. It gives an approximation family as `P -> infinity`, without a bound ensuring that the required order lies below the dense-state crossover. It retains every initialized dense operator and both actions, has larger minimum total storage in the reported large experiments, and is slower there. Variant B's omitted Gram term further weakens its advertised state rate. The numerical evidence shows that small orders can reproduce selected fitted predictors, but it does not test the theorem's trajectory rates and includes sharp failures.

Relative to the frozen packet, the complete theorem contract appears distinct from prior work. Its ingredients and surrounding dynamical viewpoints have substantial precedent, especially HiPPO, NTH, feature-learning population flows, Tensor Programs and DMFT. The paper can become a strong specialized theory contribution after it corrects the state claim, supplies the full proof and evidence, and positions the theorem at this narrower level.

## Frozen factual claim ledger

1. **F1.** Candidate Theorem `thm:old` proves a `1/sqrt(P(P+1)) = O(P^{-1})` complete-trajectory bound at fixed finite dimensions on each prescribed finite interval under local `C^{1,1}` activations.
2. **F2.** The ordinary-clock reconstruction, projection tail, product-of-errors identity and feedback continuation are mathematically consistent; I found no fatal defect in them.
3. **F3.** Candidate Theorem `thm:new` has a valid `1/[P(P+1)] = O(P^{-2})` proof in the frozen supporting evidence for sufficiently large order on each fixed finite horizon.
4. **F4.** The response-clock manuscript proof omits the detailed coarse-bound, residual-tube, clock-bound, order-threshold and Gram-continuation derivations needed to make the theorem self-contained.
5. **F5.** Variant B evolves a shared Gram matrix through `eq:new-ode`; a symmetry-packed Gram has `P(P+1)/2` moving scalars, while the supplied implementation stores `P^2`.
6. **F6.** The correct complete Variant-B moving-state scaling implied by `P=O(epsilon^{-1/2})` is `O(Hmn epsilon^{-1/2}+epsilon^{-1})`, before common outer blocks.
7. **F7.** The history arrays alone are smaller than the dense internal moving matrices exactly when `2mP<n`.
8. **F8.** Both closures retain `(H-1)n^2` initialized internal entries and direct forward and transpose actions; a direct initialized-matrix action costs `O(n^2)` per vector.
9. **F9.** The candidate's Table `tab:complexity` “full-batch” closure count excludes the initialized dense action and its Variant-B moving-state row excludes the Gram.
10. **F10.** HiPPO Definition 1, Theorem 2, Propositions 3--6 and Appendix D.3 equation (29) precede the candidate's use of online scaled-Legendre projection and its closed moment ODE, but do not provide neural feedback-coupled matrix reconstruction or a fixed-width neural trajectory theorem.
11. **F11.** NTH equations (2.1)--(2.2) give an exact hierarchy and equation (2.7) an autonomous truncation; its order-`p` training state is dominated by `O(m^p)` sample tensors in candidate notation, and equation (2.11) adds up to `O(m^{p-1})` tensors per test point.
12. **F12.** NTH Theorem 2.6 is a wide/NTK-regime output/kernel approximation with explicit width-dependent horizon and error; it does not approximate the complete fixed-width parameter trajectory, and the supplied PDF demonstrates no executable NTH implementation.
13. **F13.** Tensor Programs IV, multilayer mean field, Neural Feature Flow and feature-learning DMFT all describe leading-order feature-learning dynamics, but their regimes, represented objects, state types and convergence modes differ from the candidate's full fixed-width contract.
14. **F14.** The local book's Section C.4.7.9 already proves restartable finite-type autonomous population systems with compact-time prediction/observation convergence for a specific nonlinear population model; its saved state contains two probability laws and a finite matrix rather than finitely many scalar coordinates for a fixed finite network.
15. **F15.** The deep-circle and MNIST evidence compares separately stopped matched-loss predictors, generally at one initialization, and does not measure same-time complete-trajectory error or an order-rate slope.
16. **F16.** In the supplied deep-circle data, `P=3` is worse than `P=2` on two alternating tasks; in MNIST100, `P=3` is slightly worse than `P=2` at the stated endpoint.
17. **F17.** The reported MNIST minimum moving-plus-fixed closure storage exceeds the dense minimum for every tested order, and every tested closure integration is slower than dense.
18. **F18.** The response-clock evidence includes a GELU alternating-quadrant case with large, step-sensitive errors through `P=5`, and the 82-case sweep has fewer strict fits for every closure order than for dense.
19. **F19.** The shallow-circle and dictionary/factorization numbers quoted in the candidate are not substantiated by any enumerated frozen result report or CSV.
20. **F20.** Two literature PDFs are mislabeled in the packet, the cited Celentano source is absent, and the supplied source set is explicitly nonexhaustive.

## Frozen evaluative claim ledger

1. **E1.** Neither convergence theorem is fatally invalid on the supplied evidence.
2. **E2.** The Variant-B state and epsilon-scaling claims are materially false as statements about the complete autonomous moving state.
3. **E3.** The current theorem establishes compression of the learned increment representation, not net model-memory reduction or runtime acceleration.
4. **E4.** The paper's novelty and significance positioning is not credible until HiPPO, NTH and the closest feature-learning population/field precedents are compared at the full contract level.
5. **E5.** The complete contract appears distinct within the supplied packet, but the packet cannot establish unrestricted priority.
6. **E6.** The response-clock theorem is repairable, but the manuscript must include the full quantitative continuation proof before the theorem is publication-ready.
7. **E7.** The supported experiments establish selected matched-loss predictor fidelity and implementation feasibility; they do not validate the trajectory rates, robust low-order accuracy, or a practical compression advantage.
8. **E8.** The unsupported baseline numbers and source mismatches require new frozen evidence or removal before the empirical and related-work conclusions can be accepted.
9. **E9.** After the state correction, proof completion, evidence repair and contract-level literature revision, the work could support a strong but specialized theoretical claim about finite-width response-history model reduction.
