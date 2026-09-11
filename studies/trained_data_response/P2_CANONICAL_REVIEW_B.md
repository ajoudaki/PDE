# Original complete isolated scientific review B: proposed C.4.7

Reviewer: `/root/p2_canonical_review_b`.

Verdict: **PASS for the exact frozen scientific candidate and its stated A–C scope.** I found no unresolved correctness objection and require no correction to this packet. This is a scientific review of the proposed addition, not approval to edit established material, and not a whole-book review. The separate integration and user-approval gates remain separate.

This report is the reviewer's original complete report, written before receiving another review, an author response, or any comparison of findings. The findings below were not communicated before this report was frozen. The final report hash is communicated separately so that the report does not contain a circular self-hash.

## 1. Assignment, isolation, and authorization

I personally read the complete neutral assignment `P2_CANONICAL_REVIEW_ASSIGNMENT.md`, the exact manifest, `AGENTS.md`, the complete `RESEARCH_WORKFLOW.md`, and the required skills. I followed the independent isolated-review scope rather than author startup. I did not read the study README, historical notes, prior verdicts, author discussion, task history, Git history, another reviewer's report, or scientific material from another study. No scientific findings were received from other agents. Outgoing progress to the supervisor was metadata only: hash verification, validation completion, reading coverage, and report progress.

My identity is distinct from all manifest authors/assemblers: `/root`, `/root/p2_continuation`, `/root/p2_variation`, `/root/p2_reached_tails`, `/root/p2_canonical_source`, `/root/p2_canonical_variation`, and `/root/p2_edition_builder`; it is also distinct from selector `/root/p2_relevance`. I performed this review personally and did not delegate any part of the required scientific reading.

Writes were confined to this report and
`data/generated/trained_data_response/p2_20260911_02/canonical_review_b/`.
The supplied recipe ran in its fresh child `standalone_run/`. I did not change a frozen input, an established document, maintained code, or the Git index. I did not run training, an optimization trajectory, or a parameter sweep. Initial metadata inspection found HEAD `3c9feacb0befd20fd57aa577494af36286af5758`, an empty staged list, and preexisting tracked modifications; their contents were not read or changed.

Required skills/process read completely:

| Input | SHA-256 |
|---|---|
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `investigate-conjectures/references/adversarial-audit.md` | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| `investigate-conjectures/references/research-contract.md` | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |

The authorized computation was deterministic validation and bounded supplied-state algebra, not a research experiment or a proof-search campaign. No external theorem was fetched to repair the packet. The guide's external literature links were read as contextual links; they are expressly not proof dependencies, and I did not retrieve or certify those papers.

## 2. Exact frozen inputs and full read coverage

Manifest SHA-256, checked against the launch assignment:
`7ad4d1a5479153bc568c67706c1497ed28d5c64acace30ac0f43ef5f8334a73e`.

Assignment SHA-256:
`d32e861a604721b7afc083b25494e6bd6ad8a9899c6c373078c61a94001f1386`.

Every complete input below was personally read, including its implementation or proof body. Line counts include blank lines. The unread complement within these ten files is empty.

| Complete file under `studies/trained_data_response/` | Lines read | SHA-256 |
|---|---:|---|
| `P2_SECTION.md` | 1–2461 | `707a7d42eb2e2e58ae92fa2ee8e25343977224fe1307675e7c0c82609b0571f0` |
| `P2_PROPOSED_GUIDE.md` | 1–284 | `5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a` |
| `P2_PROMOTION_DEPENDENCIES.md` | 1–7434 | `a68aaa0107f4f73cd0df22af8a8f3867b1c76b515c5d0a920ef387ff2d32acd3` |
| `P2_EDITION_ANCILLARY.json` | 1–111 | `7aae13594bc1e5139d8d67cb33c3cc2f1b2e7f5dd5cafaaaae5ebededcb1dedc` |
| `P2_EDITION_BUILD.py` | 1–372 | `fac14c4e375a4504c71c868a14cf9f1c6490cbc2c341731d1725f514411ab5ac` |
| `P2_PROMOTION_CHECK.py` | 1–102 | `9a1526c6a030ac379ec1e1ae6f041a094464ad56ef9d2112f98ca7f254150549` |
| `P2_PROMOTION_TANGENT_CHECK.py` | 1–197 | `b0bbbde5f1f024dbb46975b2092d3aa2a79cabd0375f4520c05489f934d3902f` |
| `P2_PROMOTION_REFERENCE_CHECK.py` | 1–56 | `112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e` |
| `P2_PROMOTION_RADIAL_CHECK.py` | 1–67 | `91ef15a16d42063dc210e82055da3a855c4d9e9e6694b90db8b0191f3390998a` |
| `P2_PROMOTION_RECIPE.md` | 1–66 | `1fc72c36d72a574b37a4e095eecf1b7e3506068497a1012f3348928c20a697eb` |

The section was read in consecutive spans 1–494, 495–961, 962–1447, 1448–1860, 1861–2291, and 2292–2461. The dependency packet was read in consecutive spans 1–393, 394–1007, 1008–1787, 1788–2308, 2309–2946, 2947–3736, 3737–4465, 4466–5370, 5371–6114, 6115–6889, and 6890–7434.

Two tool-output truncations were detected and repaired. The first combined guide/ancillary/recipe output omitted part of the guide: I reread the entire guide alone and additionally reread the entire ancillary JSON alone; the recipe was completely visible in its original output. The second omission was inside the dependency read 394–1007: I reread 723–848 completely, restoring the adaptive conditioning and exact source-rule proof. No other scientific read was truncated. The source-excerpt correspondence and repeated arithmetic program were not used to skip any proof reading; the complete dependency packet was read even where it repeated material already seen in a guide or supplied script.

The runner independently verified these seven byte-exact complete dependency spans against the declared live established files:

| Established source span | Full source SHA-256 | Exact excerpt SHA-256 |
|---|---|---|
| `docs/README.md:1–278` | `88757537ae600ebf79cf265288d6ca3034254caba236b4dcb055a21dd568c721` | same as full source |
| `docs/NOTATION.md:1–98` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` | same as full source |
| `docs/finite_dynamics.md:1–227` | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` | `bd10bbff9d16f60c63d26b06e793510fa19958e1ec91dbdd85709caff7d96980` |
| `docs/special_data_limits.md:3785–4326` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` | `8a8dbe6a31a51d3f73c999b75c75dcade76b3d533c8901a062c66587776cdd0a` |
| `docs/global_nonlinear.md:1840–2453` | `3f32122dea7915e25e4abc7abe9d74017d535badfa5abbe1939e84fe2b100bdf` | `bcfd408439134d630c4f6b5e907f9d4cf08a7bc3388b48c15fc0e603dc17e408` |
| `docs/global_nonlinear.md:2924–3440` | same full global source | `cf223a3eed88b3755d0379948316534fb44febc9fa1d6f0bb5d282ff8be4ac94` |
| `docs/global_nonlinear.md:3836–8959` | same full global source | `135e9a5f7e949ae93c3eb6191f34e98e8b7c766d11483fb493833154b1c59d19` |

These contain the entire base guide, notation, finite-dynamics §§1–4, special-data III.F.1–11, global A.1–A.4 and B.1, global C.2, and the complete C.4 introduction through C.4.6. I audited the complete bodies, including the reference endpoint, activity certificate, source proof, and finite derivative passage; they were not treated as previously accepted premises.

For clarity, the scientific unread complement is all established material outside those complete spans. The other copied chapters were used only for frozen hashes, document preservation, and link/heading metadata, as authorized. Their full hashes, also verified initially and finally, are:

| Metadata-only copied document | SHA-256 |
|---|---|
| `docs/arctan_limits.md` | `19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead` |
| `docs/continuous_depth.md` | `12be7aafbf37cb3651facdcac9c5333281b793c96b96a8a52a1232cd86ca006d` |
| `docs/finite_optimization_and_controls.md` | `80dcce91ed3cd8313654523725e28b312ab925376cd7a28d71323bed648a5628` |
| `docs/gaussian_calculus.md` | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` |
| `docs/linear_dynamics.md` | `8de3beaca0cd6f970c27a25eb8c2bc4a1fefa2e7840bd97e7bccfc4f41281c1d` |

Machine-readable evidence is in `initial_hashes.json`, `read_coverage.json`, and `final_input_hashes.json` in the assigned scratch. Those files supplement the personal-read declaration; a coverage assertion by itself would not certify reading or mathematical correctness.

## 3. Contract and component decisions

The object audited is the two-hidden-layer, equal-width, no-bias tanh network on the normalized circle, with independent stored Gaussian variances `(1,1/n,1/n²)`, actual small finite Gaussian readout, mobilities `(n,1,n)`, unhalved exactly integrated Borel-law loss, and physical time `[0,40]`. The neighborhood is positive, uniform in width/count, and relative to all laws with labels in `[-Y,Y]`, `Y≥1`. It is not an orthogonal-data restriction on the changed laws.

| Component | Decision | Main reason |
|---|---|---|
| A: strong raw flow, actual Gaussian action and adjoint, learned HS increment, uniqueness and reached restart | PASS | The two separate causal source bootstraps produce uniform tails before completion; Osgood comparison completes the raw Hilbert paths and compares arbitrary competitors to the constructed tail-bearing path. |
| B: deterministic law modulus, whole-circle capture, separately fixed Borel laws, arbitrary empirical-law/width sequences, independent iid samples | PASS | The finite oracle is fixed before width; same-carrier raw comparison and a finite time partition remove its approximation. HS ranks, both orientations, joint second moments, and paired hidden observations are retained. |
| C: uniform population small-o remainder and the stated finite width-first nonlinear probability limit | PASS | Reached weighted moments justify the clock equation and forcing continuity. Compact response directions suffice for Taylor consistency. A comparison with one bounded readout endpoint yields the nonlinear remainder; the final triangle uses separately fixed positive epsilon and law. |
| Binary risk/activity inheritance | PASS in exactly the stated intersection and times | The C.4.5 strict finite margins transfer through actual GF capture and paired observations: risk at 40, paired squared hidden displacements at 1/200. |
| Proposed guide/navigation and standalone deterministic validation | PASS in their declared scope | Seven exact replacements, unchanged other documents, exact inverse preservation, matching proposed guide, valid affected fragments, and all supplied checks succeeded. |

## 4. Adversarial audit of A and the source production argument

### Exact source semantics and dependency foundations

I checked III.F's adaptive conditioning argument, not merely its statement. Conditioning is performed successively on a transcript-measurable input, so the residual factors of the initialized matrices remain independent under the accumulated linear observations. The minimum-Frobenius-norm conditional mean obeys both constraints. The finite-rank projection error costs rank/n, and fixed-program second moments are identified before passing to Wasserstein convergence. The Gaussian integration-by-parts cancellation produces the two oriented source formulas. The source groups are independent; actual answers in opposite orientations are not independent.

The singular-query proof adds a separate fresh input noise to each fixed call, takes width first, and then removes that noise through positive-semidefinite square-root coupling and derivative envelopes. It does not require convergent pseudoinverses at rank loss. The generated common spaces are completed only after finite norm and transpose identities pass to the dense generated span. Thus the action used in the new section is the actual initialized action and its actual adjoint, with only the learned increment HS.

In the new section N2–N8 have the correct mean-loss factor and finite rank normalization. A named derivative freezes residuals, contractions, response coefficients, and covariance parameters. It differentiates the coordinate expression, even when named coordinates are singular or duplicated. Current c and w contain only older steps; hence the current upper derivative is exactly the one distinguished coefficient `E[c_k phi''(Z_ku)]`. Appending unused passive queries does not create extra current coefficients. I specifically attacked the possibility of an unweighted current-input sum: N6 and the distinguished-slot definition prevent it.

### Temporary cap, moments, and weighted law transport

The cap argument does not infer Gaussian `L^p` action bounds on arbitrary fields. Under a temporary beta-row cap, N10 is an actual decomposition `Q=zeta+J`, with Gaussian variance bounded by `C0²` and bounded remainder `D0`. Jensen over time-step/atom masses yields N11 without an independent-time assumption or Gaussian-history maximum. The normalized lower pulse starts with `2R0 h_s p_b`; its random integrating factor has every fixed moment by N11. This gives N12–N14 with constants independent of the minimum atom mass.

The upper derivative row obeys a pointwise Volterra inequality. More importantly, the single-past-slot argument yields N17, `|beta_ku,sb|≤b_B h_s p_b`, alongside the distinct unscaled current coefficient. A row bound alone would not suffice for transport; the proof actually supplies the needed density. I checked that the two nested time sums in the single-pulse estimate cost total time T, not the number of steps.

For transport, splitting coupling atoms preserves proportional past source coefficients and their total row bound. The comparison pairs the same passive output u; it does not compare a distant contaminant's current query to a reference-axis current query. N21 couples source differences through cross-program covariance contractions, rather than a Lipschitz square-root or inverse-Gram claim. N22 uses bounded readout in the upper gate; Q itself has no lower first-gate product.

In N25–N29, subtraction retains every changed residual coefficient, input vector, gate, Q, response coefficient, and learned contraction. The source difference in D retains its old mass. The interpolation exponent for an `L²` difference with an `L²⁴` bound at `L¹²` is `1/11`, so weakening it to `1/16` is valid on a bounded distance range. Hölder controls the products, and N11 controls the random propagating factor. The past-source term N27a uses `h_s p_b`; Jensen gives `sum p_b e_b^(1/16)≤q^(1/16)`. I found no hidden replacement by `max_b e_b`.

The upper comparison N29a averages the active output index before estimating its transport error. Its passive-output counterpart has no active-output transport cost. Its right side uses only prior errors. This closes N24 without an unknown current beta on its right. These weighted causal details are sufficient for tail production; the proof does not merely establish propagation conditional on the desired tails.

### Clock anchor, raw defect, and the two independent bootstraps

I checked the complete-query forcing argument against physical residual feedback. In the clock scheme, forcing a reverse answer changes the clock update with factor `2R0 h_s p_b`. Forcing a forward answer changes H, delta, its residual, and its reverse answer. N43 includes the residual-variation contributions to all three state blocks. The pointwise c bound and HS/action bounds survive forced queries by bounded tanh values; no forced energy identity is assumed. The finite same-root Lipschitz constant is uniform in mesh and width.

For coefficient extraction, the finite forced and unforced graphs are compared first. At fixed graph and nonzero forcing, the width limit precedes Gaussian integration by parts and removal of forcing. The fresh root enters the specified source slot only; selected deterministic coefficients may depend on the forcing amplitude but are held fixed under the coordinate derivative. Root clipping, inactive readout clipping, and fixed-graph derivative bounds supply the zero-forcing continuity, including singular covariance. Thus N46–N47 bound named coefficients, not merely values on an unforced singular support.

For raw-to-clock transfer, the defect is `F(w+h b phi'(w))-F(w)-h b`. Expanding after cancellation gives N32. The factors `phi'(w)² F''(w+z)` and `phi'(w)² F'''(w+z)` are bounded by exponentials in `|z|`, with no uncontrolled exponential in the base w. N34 is the derivative of that cancelled expression. At the direct source injection, dividing by `h_s p_b` leaves `O(h_s)`, and later terms sum through `sum h_k²≤T h_max`. This establishes the differentiated consistency N36 with the same mass convention.

The raw/clock lower-pulse comparison uses the exact clock recursion plus these defects. Its propagation has bounded clock gates and deterministic capped D rows, and its comparison clock pulse has the pointwise bound N49. It consequently avoids multiplying a raw pulse discrepancy by an uncontrolled inverse gate. The upper rows then have identical recurrences and the stated prior-error estimate N51.

The first bootstrap fixes the independently proved clock cap, sets `B=B_cl+1`, and makes the raw/clock discrepancy less than 1/2 by choosing the mesh. The second fixes that raw reference cap, compares the two raw programs on the identical mesh with no mesh floor, and chooses a positive law radius for N31. Both start at zero readout and zero beta. At each prospective failure, lower derivatives use older Q fields, the current forward node is already available, and the current upper row uses strictly prior memories. Neither bootstrap assumes the uncontrolled current row. The constants can be extremely large, but the choices of positive mesh/radius are logically valid and independent of support count and smallest weight.

### Strong completion, uniqueness, restart, and energy

The HS upgrade is valid term by term: all action differences are bounded by HS differences, and a rank's HS norm is the product of its factor norms. The upper backward error passes only through bounded gates/actions before the new lower gate error is added, so NC has one cutoff factor, not its square.

Exponential tails suffice even when their exponent is small. Choosing the cutoff from the current discrepancy gives `s'≤L s log(e/s)`, with exponent `exp(-Lt)` after integration. The same argument at zero discrepancy gives uniqueness. It first establishes Cauchy convergence of finite-law Euler paths in the complete raw path space; the strong equation is then identified by joint state/law continuity. Compact data range and bounded multiplier continuity justify the Bochner integrals and uniform-in-time passage. The learned action is HS throughout the limit.

The energy identity is justified by the scalar weighted Taylor argument, rather than ambient `L²` Fréchet differentiability of the activation-valued map. Finite dynamics and the arbitrary-Borel finite smoothness argument match the unhalved metric exactly. At population level this yields initial loss at most `Y²` and the pointwise readout bound `2Yt`.

An arbitrary competing strong raw path is bounded on a compact interval. NC uses only the constructed path's tails, so uniqueness imposes no extra moment condition on that competitor. Restricting the already constructed strong path supplies existence at a reached restart; the same zero-discrepancy argument supplies uniqueness. This proves the stated reached continuation, not a new existence theorem from arbitrary ambient states.

## 5. Adversarial audit of B and all finite-limit passages

The relevant finite program is fixed by a finite comparison law, a finite raw mesh, and any finite observations before width tends to infinity. Expanding learned matrices as ranks converts every required action to the initialized action in the correct orientation plus finitely many contractions. The oracle uses causal deterministic population contractions; there is no future-trajectory oracle.

The actual finite initial Gaussian readout is included additively in proxy parameters. Its RMS and supremum vanish in probability, but actual GF is never reset to zero readout. Recomputed proxy backward products are recovered by clipping a fixed oracle factor, taking the fixed-program width limit, and removing that clip using its joint second moments. This is not an inferred uniform finite-width higher-moment theorem.

For `K=sum a_i tensor b_i`, the HS/Frobenius pairing is precisely the double sum of the two layer Gram contractions, as in NK. This checks the normalization `a_i b_i^T/n` and identifies both K and K-adjoint actions. Initial A0 is not asserted HS. No finite matrix is subtracted from an operator on another probability space.

NAP provides same-width actual-GF/proxy comparison with fixed-cutoff probability errors. When only exponential tails are retained, one cannot send one fixed whole-horizon cutoff to infinity unless its tail beats the amplification. The text handles this correctly with a finite time partition satisfying `C ell<a'/2`. Backwards choice of finitely many cutoffs and incoming tolerances, then choice of law and mesh, then width, gives the required forward error control. All choices remain finite; no growing transcript enters III.F.

The actual law can be a separately fixed nonatomic law because the comparison law alone must be finite. It can also be an arbitrary deterministic empirical-law sequence converging in Wasserstein distance. Compact Borel-cell sampling convergence, combined with fixed-reference initialization events, gives independent iid sampling with no relative rate. Neither argument uses total-variation convergence of empirical laws.

Whole-time/whole-circle predictions follow from full row input control, bounded raw velocity, fixed finite input/time nets, and fixed-program convergence. For the broader stated observation contract, bounded actions, globally Lipschitz coordinate instructions, and bounded continuous gates preserve the approximation after fixed factor truncation; the limiting compact families and joint second moments control their tails. Joint tuples retain initial/current hidden fields on the same population, so their displacements are actually paired observations. Marginal predictor convergence is not substituted for this identification.

## 6. Adversarial audit of C and response identification

The variation proof is stronger than an infinitesimal calculation. Its needed extra regularity is obtained on the actual constructed family.

The probe-atom proof is valid even though the preceding source theorem already supplies stronger passive Gaussian tails. On the identical Euler mesh, a probe of mass eta costs `C eta^alpha` in query norm, while its own active tail costs `eta^{-1} M exp(-aR/2)`. Choosing eta exponentially small in R balances the two terms and gives an individual passive exponential tail uniformly in law, mesh, time, and input. No preexisting atom mass is inverted, and there is no additive mesh floor as eta tends to zero. Fixed-time strong convergence and bounded truncated exponentials pass this estimate to every reached Borel-law path.

Radial saturation uses the exact identity for `d|w|²/dt`. The inequality `|z| sech²z≤1/2` gives the row-envelope bound with the correct factor 2. Jensen over normalized time and training law controls the integrated absolute query; Cauchy–Schwarz with the two-dimensional Gaussian root yields the stated positive Gaussian-square moment of the reached row supremum. This does not require independence between roots and queries. Hölder then gives all fixed moments of `cosh²(w_j) Q(u)` and in particular uniformly integrable squares of the exact inverse-gate forcing. No arbitrary `L^p` action bound is imported.

The scalar clock chain rule is applied to almost surely absolutely continuous reached rows. Its derivative is already integrable in `L²` by those forcing bounds, so the transformed curve is justified rather than postulated. The new absolute clock differs from C.4.6's displacement clock by the same fixed `F(g)` for every law; their tangent coordinates coincide.

The reference clock field has a Lipschitz comparison whenever one endpoint readout is bounded. The exact upper-factor subtraction uses that bounded endpoint, which is essential because the linear response readout need not belong to `L^infinity`. This comparison gives an actual `O(epsilon)` clock displacement. Together with reached uniform integrability, it gives forcing continuity uniformly over all contamination laws and passive inputs. It is not an assumption of smoothness of the contaminated field on an ambient Hilbert ball.

The compact atom-forcing curve image has compact closed convex hull in the complete curve space: finite nets reduce convex combinations to a finite-dimensional simplex at each required tolerance. The bounded linear response map therefore produces a compact response-direction family. Compact Taylor is applied to this family, with a fixed-direction cutoff before epsilon tends to zero. The upper backward cross term `d[phi'(Z_new)-phi'(Z_*)]` is treated by compact `L²` tails of d, not by multiplying arbitrary `L²` fields. The other products are bounded multipliers, scalar pairings, or HS ranks.

Subtracting the actual nonlinear equation from the reference-plus-response curve leaves the reference-field comparison, epsilon times the vanishing forcing defect, and an `o(epsilon)` Taylor defect. The one-bounded-readout comparison and Gronwall therefore give a uniform clock remainder, then a raw remainder through the Lipschitz inverse clock, and a whole-circle predictor remainder. The argument yields uniform small-o over all probability contaminations, not just separate directional differentiability.

I compared the displayed generator and forcing term by term to C.4.6.T5, T6, T14 and P8–P11. Signs, factor two, atom weights, full row, adjoint terms, gate cancellation, and initial zero tangent match. Uniqueness identifies the response exactly with the finite-first response proved there.

The complete C.4.6 dependency is adequate for that identification. Its compatible singular endpoint factorization uses injectivity of the positive gate metric to obtain `ker Gamma=ker S=ker E*`; the nilpotent counterexample explains why positivity alone would not suffice. Its actual finite weighted-query proof deletes one initialized column but retains the entire learned cavity flow and its residuals. Conditioning uses the column-independent cavity event; the full event is only used afterward by inclusion. The conditional Gaussian parameter process has deterministic RMS time/input modulus, allowing its elementary chaining estimate. This establishes actual finite weighted uniform integrability, not an inference from RMS convergence. The finite tangent passage then removes cutoffs, quadrature, and time mesh on the tested compact tangent directions using strong multiplier continuity, without operator-norm convergence of multipliers.

Finally, at each fixed positive epsilon and fixed nu, both nonlinear finite prediction errors vanish by B and the finite derivative error vanishes by C.4.6. Their errors may be dependent; the triangle and finite union bound do not need independence. Division by epsilon occurs only after fixing epsilon. Sending width first and then epsilon proves NB. This supplies the actual finite nonlinear assertion; it does not imply a width-uniform finite-n remainder, a simultaneous epsilon/width rate, or a supremum over laws of finite failure probabilities.

## 7. Reference constants, risk/activity, and navigation

I checked the reference feature equation, the physical clock `ds/dt=2(1-b)`, its positive residual, the first `b=1` endpoint, and the energy-length estimate. The convexity argument for the readout norm yields `b_s≥m`; the rational certificate gives `m≥1/10`, so the physical error and risk bounds at 40 have the stated strict slack. The actual reuse calculations for both hidden activation displacements retain the reverse response and the later forward response, including the positive conditional-variance contributions. Their small-feature-time remainder bounds and conversion to physical time 1/200 support the paired RMS margin.

The inherited changed-law conclusion is restricted to binary labels and the intersection with `W1(mu,nu*)<exp(-exp(3000))`. It asserts risk at most 1/4 at time 40 and both paired squared hidden displacements at least `10^-13` at time 1/200. It does not transfer activity to time 40 or claim useful risk for every bounded-label law. C.4.5.3 applies to actual GF with zero discretization defect; the new capture and paired-observation statements then pass its strict finite margins to the constructed population flow.

All seven exact navigation replacements were read. They distinguish C.4.6's finite-first derivative theorem on every fixed horizon from C.4.7's nonlinear continuation through 40. They preserve C.4.5's separate raw-GD scope. The complete proposed guide makes the same distinctions and does not claim all-time changed-law dynamics. No scientific discrepancy between the new theorem and these summaries was found.

## 8. Commands, actual outcomes, and retained execution evidence

All commands used working directory `/home/amir/Codes/PDE` unless another directory is explicitly stated. All read/metadata commands exited 0. They consisted of `cat` for the assignment, manifest, instructions, required skills/references, whole guide, JSON, scripts, and recipe; `wc -l` on all ten inputs; `wc -c` on the section and dependency packet; `rg -n '^#{1,6} '` on those two files to map section boundaries; and `sed -n 'FIRST,LASTp'` for precisely the scientific spans listed in §2, including the repaired 723–848 read. Their outputs were the frozen content personally read above, line counts 2461/7434 for the scientific files, and byte counts 106371/353965. The initial Git metadata commands were `git status --short --untracked-files=no`, `git rev-parse HEAD`, and `git diff --cached --name-status`; the staged output was empty. The hashing/coverage scripts used only the named manifest inputs and assigned scratch outputs and exited 0. The skill `sha256sum` command produced the four hashes in §1.

The standalone recipe command was:

```sh
python -B studies/trained_data_response/P2_PROMOTION_CHECK.py --output data/generated/trained_data_response/p2_20260911_02/canonical_review_b/standalone_run
```

It exited 0. It ran these four child commands, all exit 0:

1. `/usr/bin/python -B /home/amir/Codes/PDE/studies/trained_data_response/P2_EDITION_BUILD.py --output /home/amir/Codes/PDE/data/generated/trained_data_response/p2_20260911_02/canonical_review_b/standalone_run/edition --manifest /home/amir/Codes/PDE/studies/trained_data_response/P2_PROMOTION_MANIFEST.json`, from the repository root.
2. `/usr/bin/python -B P2_PROMOTION_TANGENT_CHECK.py --output /home/amir/Codes/PDE/data/generated/trained_data_response/p2_20260911_02/canonical_review_b/standalone_run/edition/standalone/data/generated/trained_data_response/checks/tangent`.
3. `/usr/bin/python -B P2_PROMOTION_REFERENCE_CHECK.py`.
4. `/usr/bin/python -B P2_PROMOTION_RADIAL_CHECK.py --output /home/amir/Codes/PDE/data/generated/trained_data_response/p2_20260911_02/canonical_review_b/standalone_run/edition/standalone/data/generated/trained_data_response/checks/radial`.

Commands 2–4 ran from `standalone_run/edition/standalone/validation/` under the assigned scratch. Their environment had empty `PYTHONPATH`, disabled bytecode, `OPENBLAS_NUM_THREADS=1`, and `OMP_NUM_THREADS=1`. I read the runner's complete returned record, all four complete logs, the complete edition validation report, and the scripts before interpreting their outputs. The standalone artifact contains neither `studies` nor `.git`.

| Retained log in `standalone_run/` | SHA-256 | Actual outcome |
|---|---|---|
| `edition.log` | `c48f4dc66a789329abc9e018b8312491a4e6f22351a1043dcd9cde48d7cbc387` | PASS; 10 documents, 7 replacements |
| `tangent.log` | `3e732b930cf23d9adfa4d21904e4f23e66ac89325fef724cec31b682bb38f42b` | PASS; central-difference errors decrease by about four per halving, last `1.608263607613758e-08`; loss-metric error `7.900680110140001e-12`; largest singular-semigroup error `1.5265444420160054e-14`; incompatible nilpotent negative control triggered as intended |
| `reference.log` | `ad40e8d8f73fed6d22cc9b68a19f7f9e6c3f2f59383d581e372ce0c976786900` | Exact rational assertions PASS; output `[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]` |
| `radial.log` | `15e0d9cc3b713eb024fd9e68bb33e1404bd5eb5e66f78e0c947485bb8c611664` | PASS; radial and energy errors both `5.551115123125783e-17`; all radial upper-bound slacks positive |

The complete commands, working directories, exits, excerpt hashes, and log hashes are retained in `standalone_run/validation.json`. The edition validation report SHA-256 is `100537f50687cc81e18aba0342f5eb1b05f01ee7c6a466fea48681cf692d0922`. Its exact assembled guide hash equals the frozen proposed guide hash. The assembled `docs/global_nonlinear.md` hash is `9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226`. Reversing the seven replacements and removing the exact appended suffix recovers all original bytes; the other eight documents are unchanged. It checked 154 balanced displays and the new equation namespace. The one preexisting `../code/README.md` guide link remains expressly outside this docs-only artifact; external URLs were preserved without retrieval. This is the declared link scope, not a proof or external-link certificate.

The deterministic runtime was Python 3.10.12, NumPy 1.26.4, and SciPy 1.13.0. The rational reference program uses only standard-library exact arithmetic. Its inequalities are checked before decimal summaries are printed. The tangent and radial checks concern supplied states; their PASS cannot certify the uniform tail or population proofs.

### Additional independent bounded checks

I wrote and ran `independent_algebra.py` only under my assigned scratch. It evaluates one fixed nonzero-readout finite state and three deliberately chosen scalar clock boundary cases. It does not integrate a training path.

The first attempted command, `python -B data/generated/trained_data_response/p2_20260911_02/canonical_review_b/independent_algebra.py`, exited 1 before calculations because `mpmath` was not installed. The original source is preserved as `independent_algebra_unavailable_mpmath.py`; `independent_attempt_1.json` and `independent_attempt_1.log` record the command, original source hash, exit, and complete traceback. No package was installed. I rewrote the arithmetic using standard-library Decimal at precision 70 and reran the same command; it exited 0. This failed optional attempt is not omitted or counted as a successful test.

The successful source SHA-256 is `ffc9424ab55ceeb933f12eda0b0be33e2430cbdc09f3d6ab60e16d093d4ba3fc`. Full output is retained in `independent_algebra.json` and `independent_algebra.log`. The independent checks gave:

| Attack/check | Result |
|---|---|
| Complete forward-query forcing, including changed residual in clock, middle rank, and readout update, checked by complex-step differentiation | Maximum error `1.734723475976807e-18` |
| Split reference atom with weights 0.2 and 0.3 versus weight 0.5, retaining duplicate source-slot bookkeeping | Maximum additive discrepancy `5.421010862427522e-20` |
| Negative control suppressing residual feedback in that supplied state | Difference `0.0010650008147578167`, above the declared `1e-6` detection threshold |
| Cancelled raw-clock defect and its w/b derivatives at `(w,b,h)=(0,1.7,.03)` | Error `3.47552103374558122351106067e-43` |
| Same check at `(1.5,-.9,.04)` | Error `3.874451057234764673373896e-45` |
| Same check at saturated row `(6,-1.3,.03)` | Error `8.2659803174008575722e-46` |

For the clock calculation, the independent algebra used the hyperbolic addition expression
`[sinh(2w)(cosh(2theta)-1)+cosh(2w)(sinh(2theta)-2theta)]/4`
for the cancelled defect, and centered Decimal differences with step `1e-20` for its derivatives. These checks support the cancellation and source-normalization audit. They do not replace its uniform analytic estimates.

## 9. Objections, limitations, and completion declaration

I actively tested the following possible blockers and found them resolved in the exact packet: assuming Gaussian action bounds on arbitrary `L^p`; discarding the full first row or finite readout; treating transpose as independent; instability at singular or duplicate queries; losing a past source's step/atom mass; using a maximum atom transport cost; comparing different current passive queries; omitting residual feedback under forward forcing; extracting a singular transverse derivative from an unforced value law; ignoring differentiated raw-clock error; closing a cap with its own current unknown; assuming tail production from propagation; completing predictions without a strong raw/HS equation; imposing constructed-tail hypotheses on competitors; using a growing transcript in a fixed-program theorem; inferring finite weighted moments from RMS convergence; approximating nonatomic laws in total variation; expanding an ambient `L²` direction ball; requiring bounded response readout; and reversing the finite epsilon/width order.

There are **no unresolved scientific objections and no required corrections** in this original report. The optional missing `mpmath` dependency was local to my extra check, and the completed standard-library check removed that execution limitation. It is not a defect in the supplied recipe or candidate.

Acceptance here has the exact stated limits: physical GF only through 40 for changed laws; an existential positive neighborhood with no useful numerical radius claimed; all probability contamination directions for the population small-o, but each law and positive epsilon separately fixed before the finite width limit; no arbitrary simultaneous epsilon/width rate; no finite failure-probability supremum over laws; no new raw-GD derivative or nonlinear raw-GD capture theorem; no all-time changed-law dynamics, endpoint selection/continuity, universal fitting, or feature-learning superiority. Risk and activity have the stated binary subclass and different observation times. No empirical training claim is being certified.

The exact named scientific inputs, established correspondence sources, instructions, assignment, and manifest were rehashed after the audit and checks. All matched the frozen values. The recorded final pre-report check at `2026-09-11T16:25:03.214208+00:00` is in `final_input_hashes.json`; a sealing recheck is performed immediately before communicating this report's hash. No changed input or missing scientific dependency was found.

**Review completion:** every new scientific line, every full frozen dependency proof, the full notation and both guides, all proposed navigation replacements, all applicable implementation/check scripts, the exact recipe, all executed commands and outcomes, and the requested A–C bridges have been reviewed. This completes the original isolated scientific review B. The report is frozen before comparison and must not be edited in response to another review; any later correction requires a new packet and fresh complete reviews as specified by the workflow.
