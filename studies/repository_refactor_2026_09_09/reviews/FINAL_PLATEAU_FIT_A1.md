I independently read every line and proof in the two frozen candidates and the notation dependency. I consulted no project history, source studies, audit records, or other reviews, and made no edits.

**Verdict:** The stated mathematical results are correct and self-contained under their explicit conditional hypotheses. I found no counterexample, incorrect constant, substantive proof gap, or required mathematical correction. In particular, the plateau packet does not establish population existence, identification, or finite-width convergence, and the fitting packet supplies necessary scales conditional on successful fitting.

Read coverage and hashes, checked again after the review:

| File | Complete read ranges | SHA256 |
|---|---|---|
| `FINAL_PLATEAU_ADDITION.md` | 1–250, 251–500, 501–750, 751–930 | `459a0b230266c2f1078ae26c015504f189098cca3d27c8e03bbcec834851d790` |
| `FINAL_FITTING_SCALE_ADDITION.md` | 1–151 | `089389fe7c7e0111ff62be4bd1f5846e6266a9ba168da60316ced8557eb8050d` |
| `docs/NOTATION.md` | 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

I also read and applied `/etc/codex/skills/solve-math-rigorously/SKILL.md`.

For the plateau candidate:

- **Setup and physical scaling, lines 3–67:** The half-sum loss, stored readout normalization, and mobilities \((n,1,n)\) give (P.1) correctly. Population operators, their actual adjoints, rank-one updates, and the common row cap are typed consistently. Strong equations and chain rules are explicit assumptions, rather than conclusions.
- **Activation and protected geometry, lines 71–239:** The smooth extension argument and all derivative bounds are valid. The six-ball construction works in both rank two and rank three. The Gaussian constants are correct: \(c_2=1/8\), \(c_3=1/(12\sqrt{2\pi})>1/40\), and \(169/8<22\). Using one disjoint pair at a time correctly yields \(\lambda_\delta=p_\delta/6=e^{-22/\delta}/240\), without overcounting.
- **Invariance and finite initial Gram, lines 243–323:** The realized-coefficient uniqueness argument works forward and backward under the stated \(L^1\) hypothesis. Fubini and the Bochner integral representation supply the required almost-everywhere row interpretation. Frozen rows remain frozen under simultaneous raw GD for arbitrary step sizes; the text correctly withholds a GD no-entry conclusion. The variance bound \(729/(16n)\) and probability bound \(729/(4n\lambda_\delta^2)\) are correct.
- **Nonaffinity and activity, lines 327–401:** Both tail minimizations are correct, including the elementary minimum \(1/112\) and lower bound \(\rho(2)/56\). The extension to affine functions of the full Gaussian row correctly separates the independent orthogonal component. Activity is correctly distinguished from positive velocity and from a prediction-kernel lower bound.
- **Confinement, lines 405–605:** The planar lemma handles constant trajectories, boundary contacts, and arbitrarily many switches. Its displacement bound follows because only one direction acts outside double-strip intersections. The rank-three suffix argument correctly uses the earliest last activation time, including ties and a one-point suffix. The transverse estimate and \(\operatorname{dist}(u_k,\operatorname{span}(u_i,u_j))\ge\sqrt{\lambda_{\min}(G)}\) are valid. No unstated bound on control magnitudes or accumulated control is used.
- **Selected path laws, lines 610–767:** Every constant in (P.14)–(P.16) follows from the stated energy estimate and exact equations. The pointwise readout bound is essential and is available. Confinement supplies the uniform integrability needed for the first-population tuple; the second tuple is deterministically bounded. The interpolation, projection, rounding, and finite-support coupling proof establishes the stated \(\mathcal W_2\) total boundedness. Products in (P.21) depend only on the indicated same-population laws. Raw second preactivations, incoming fields, and the first kernel are appropriately excluded.
- **Protected forces and learned returns, lines 771–859:** The Hilbert–Schmidt inequality, protected Gram contraction, primitive (P.23), and \(\lambda_\delta^{-1/2}\) norm factor are correct. The text correctly distinguishes an exact energy identity on subintervals from the weaker assumed dissipation estimate. The learned-kernel bounds and the finite representative \(nU_{ij}\) have the correct normalization. The Gaussian maximum estimate retains the actual finite random readout.
- **Obstructions, lines 863–930:** The positive-probability saturated-top event is valid at every fixed \(n\ge3\); it produces the stated rank-one dynamics and positive limiting mixed-label loss. The second construction gives identical initial feature states with different later feature paths: correlated input motion carries one hidden raw preactivation out of its plateau earlier. Its scope is correctly restricted to arbitrary finite restart states.

For the fitting-scale candidate:

- **(F.1)–(F.4), lines 3–63:** Input linearity gives the exact cancellation in the first layer. The recursion and bounded arctangent terms yield (F.2). The loss threshold implies \(\sum_a f_a\ge3/2\), giving exactly \(1/(\pi\theta)\) in (F.3). The raw-distance and operator estimates imply (F.4).
- **(F.5)–(F.6), lines 65–100:** The explicit \(M=2\) bound is valid. The leading homogeneous term contains exactly \(L\) factors—readout and \(L-1\) adjacent increments. Applying arithmetic–geometric mean to their squared norms gives the stated \(\sqrt L\,\pi^{-1/L}\) lower constant. The lower-degree remainder vanishes after multiplication by \(\theta\) along bounded rescaled subsequences.
- **(F.7)–(F.9), lines 102–151:** The chord estimate follows from the explicitly assumed raw-metric energy identity. The first-exit argument requires no monotonicity of \(R\): continuity and the exclusion of successful states in the unit ball suffice. Both \(2/(3\pi B_{L,M}\theta)\) and its \(M=2\) specialization are correct. The comparison between the \(L=2\) and \(L>2\) conclusions is also correct.

Three optional wording refinements would remove small opportunities for misreading; none changes a theorem or proof:

1. At plateau lines 107–110, explicitly call the deterministic lower fraction a **population fraction**. A finite empirical active fraction is random.
2. At plateau lines 762–764, label the displayed first kernel the **uncapped physical first kernel**. If describing the actual prediction dynamics of a capped path, that contribution instead contains \(\mathbb E_1[c\,\Delta_a^{(1)}\Delta_b^{(1)}]\).
3. If “compactness” in the opening is intended explicitly to promise convergent subsequences, add the customary sentence that \(\mathcal W_2\) over the complete separable uniform path space is complete, so total boundedness gives relative compactness. The body already proves total boundedness and phrases observable convergence conditionally on a convergent subsequence.

**Required mathematical fixes: none.**
