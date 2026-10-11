# Independent final integration audit: shortened paper, frozen v2

Verdict: **PASS for the assigned paper-only proof-shortening integration audit.** No required correction was found. The public claims and all seven theorem/proposition/lemma statements in the two revised modules are preserved. The shortened arguments retain their quantitative premises, and the shared cost sums expand to the original eight ledgers. This is an independent mathematical and integration judgment, not a build-result inference or approval to promote book material.

## Isolation and inputs

Reviewer: `/root/short_final_integration_v2`, distinct from the authors, factoring adviser, and paired reviewers identified in the neutral assignment. I read `SHORT_INTEGRATION_ASSIGNMENT.md` completely. I used only the frozen `short_paper_v2/{paper,baseline,docs,preservation.json,build/compact.pdf}`, its supplied page images, and the permitted v1 paper comparison for the two display repairs and historical comments. I did not read author notes, other reviews, study history, evolving manuscript sources, Git history, other studies, or external research. No source, Git, or book edits were made. Scratch consists of independently rendered pages 75–76 under `short_paper_v2/integration_scratch/`.

Required instructions read completely: `solve-math-rigorously/SKILL.md`, `explain-with-canonical-notation/SKILL.md`, and its `references/neural-response-memory.md`. The report preserves the paper's readout symbol (w), residual (r=f-y), physical-time convention, and explicit normalized finite pairings. The frozen book notation identifies the exact readout correspondence (w=W^{(L+1)}); the paper explicitly states its zero-readout initialization instead of silently adopting the book's small random readout.

## Direct coverage

All final manuscript files were read completely, with the following source-line coverage. The two unchanged final proof modules at the end were read for integration and preservation, not treated as new scientific claims requiring a fresh proof audit.

| Final file | Direct lines read | Audit role |
|---|---:|---|
| `compact.tex` | 1–399 | Setup, 30-entry inventory, headline theorem, initialization proposition, assembly |
| `feature_learning_theorem.tex` | 1–62 | Separate nonlinear-learning interface and qualifications |
| `compact_fitting.tex` | 1–241 | Complete fitting and signed-perturbation proofs |
| `compact_foundations.tex` | 1–1530 | Complete coefficient, insertion, Gaussian, trace, moment, domain, and continuation proofs |
| `compact_legendre.tex` | 1–750 | Complete construction, order-independent fitting, projection, stability, innovation, and derivative-transfer proofs |
| `compact_width.tex` | 1–1184 | Entire revised quantitative width module |
| `compact_selected.tex` | 1–1096 | Complete selection, corrected optimizer, fitting, comparison, compiler, Harmonic and Taylor proofs |
| `compact_initialization.tex` | 1–1216 | Entire revised numerical initialization, sampler, execution and cost module |
| `compact_feature_learning.tex` | 1–335 | Unchanged integration context; byte preservation verified |
| `compact_nth.tex` | 1–592 | Unchanged independent benchmark context; byte preservation verified |
| `references.bib` | 1–170 | Complete bibliography; no external retrieval |

Also read frozen `docs/index.qmd` 1–260, `docs/notation.qmd` 1–98, and `preservation.json` 1–38. No whole-book review was performed.

Baseline coverage: all 1,448 lines of the complete width unified diff and all 1,640 lines of the complete initialization unified diff were directly read. Every removed baseline passage was thus read, while unchanged baseline passages were covered by their directly read matching final text. This covers baseline width lines 1–1430 and initialization lines 1–1510 without a second separate end-to-end baseline read. All other baseline files were compared byte-for-byte with their final counterpart. The first combined output was truncated; I repaired that read by rereading `compact.tex` and the feature-learning interface in full and rereading both complete diffs in bounded consecutive chunks. No assigned scientific text remains unread.

The permitted v1 comparison contains exactly two inline-to-display conversions in width (the definitions of (Z_0) and (D_c)) and replacement of three historical initialization comments with one self-contained comment. The mathematical expressions are identical. No v1 report was consulted.

## Mathematical checks and deletion coverage

### Finite source probability and polynomial widths — PASS

The width proof recalls the exact foundations recurrences and retains 

\[
X=\beta^L,\quad \lambda=\gamma/m,\quad S=16Y/\lambda,
\quad N_{\rm src}=\left\lceil(A_{N,\rho}/\rho)^{40000}\right\rceil,
\quad A_{N,\rho}=X^{4000}(1+\lambda^{-1})^8(N+d+u_\rho+1)^8.
\]

No inverse-label factor enters this source gate. I checked the finite initialization propagation for singular Gaussian covariances, net and operator allowances, zero-embedding cavity comparison, and conditional testing before adaptive substitution. The shortened initialization paragraph retains the same covariance recurrence, margins, fresh-row projection, test count, and Chebyshev allowance.

The principal deleted block was a second listing of first-variation and time-modulus recurrences. Its replacement at width lines 288–412 explicitly supplies the parameter coefficient, forward/backward recurrence, control substitution, reference speed recursion, and differentiated product terms. The full exact products remain in foundations' `cp:src-local-lemma`. I checked the six map/time powers (80,85,125;125,140,190), the additive carrier dependence, one raw-coordinate (\sqrt n), and the common (X^{1000}\chi^2) envelope. The retained calculation does not appeal to the older qualitative threshold to justify a finite power.

The deleted repeated definitions of the flaring domain and retractions are precisely those in `cp:src-panel-working`. The width module supplies its different capped radius, finite propagator gate, finite endpoint mesh, and all confidence calculations itself. In particular, the original (n^{-1}\le Y) eventual gate is not imported. The uniform frozen-control event precedes the adaptive substitution; each cavity is clamped by its own retained-measurable stop. The surviving remainder estimate retains the first-layer exception: its incoming increment belongs to deleted scalar controls, with no fictitious reverse port.

I checked the moment argument against the complete Gaussian and trace proof: four nonzero traces are retained, distinct main root references are conditionally independent only after fixing their common cavity, corrections use Cauchy–Schwarz/Hölder, and indicators are discarded only after domination by complete references. The finite moment order (u_\rho), collision count, strict cavity margin, and simultaneous-domain budget remain. The nominal allowance is (\rho/4+2(\rho/16+\rho/16+\rho/4)=\rho); the component estimates are strict, giving the claimed strict total bound. No independence of training sample processes or full-network survival is assumed.

The all-time carrier/response extension uses the finite parameter tail, not another source-width limit. The radius reciprocal and disk count retain the ( (Y/\lambda)^2\sqrt{\log(en)} ) term before source-rank squaring.

### Dense separation, Legendre improvement, and Taylor assembly — PASS

The finite small-ball proof remains complete and shift-uniform. Conditioning on the first run through layer (L-1) and the complete independent second run leaves iid final rows. The measurable maximizing coordinate and bounded conditional third moment are retained. I checked the variance lower bound using the full `cp:innovation` proof: its squared-area and two spectral bounds precede the equal-diagonal specialization, so reuse for the conditional matrix with unequal diagonals is valid. The finite lower proof retains (\gamma^4Y^2/(256X^{16})), the (\gamma^{-12}) gate, and the positive-time trajectory rather than endpoint witness. The ellipse transfer uses the unchanged derivative lemma with the new smaller training radius.

The Legendre proof still differentiates the actual reconstructed path including its physical defect. Its amended response-product expression expands (W(\phi'R)) explicitly and loses no term. The (q^{-2}) forward history estimate uses the defect-subtracted history, zero derivative at the prefix join, terminal residual cancellation, two integrations by parts, and the Legendre eigenvalues. The reused backward-freezing argument has the same closure residual and dense response reference; its complete proof and explicit (b_0,b_1,B_d) bounds were checked. Thus the (q^{-3}) defect estimate is not an unsupported appeal to the older (q^{-2}) comparison.

Combining the forward and backward tails gives the retained absorption at (q\ge4P^3\ell_n). The signed comparison contributes at most (Pn^{1/64}). I checked the bootstrap improvement, (q\le\sqrt n), the (d^4) gate, and the whole-real-sphere output extension despite using only training inputs in the complex source argument. The resulting width error (4YP^5\ell_n^2n^{-47/64}) and ratio power (n^{-15/64}\ell_n^{9/2}) agree with the baseline.

Taylor reuses only the deterministic source construction of `cp:panel`, with the quantitative disk cover substituted explicitly. The origin-jet compiler requires a rectangle; compactness of the open disk union supplies it. Its exact base/image pairing, coefficient tolerances, input-span reduction, and no-passive-label contract remain. The source-degree gate and (K+1\le8\ell_n) remain quantitative. Rank squaring keeps ( (Y/\lambda)^4\ell_n^3 ) and the separate (\lambda^{-2}\ell_n^2\log^2(e+\ell_n)) term. Both final maximum gates, including the inverse-label count gate for Taylor only, are preserved.

### Numerical sources and exact implicit Gaussian execution — PASS

The shortened numerical stability proof reuses the exact signed identity, not merely a theorem name. It retains the three endpoint-remainder terms, training reference carrier, negative prediction square, cubic error term, integrating factor, first-crossing bound, and regularization at zero discrepancy. Thus it still proves the stated small-defect conditions and the (C_{\rm src}nE) real-query source error.

The complex restart section supplies its own balls, strip margins, pairwise Lipschitz coefficient, activation-polynomial error, and all finite orders. Reusing the earlier Fourier contour calculation does not remove the new inner-ellipse check, discrete alias estimate, derivative Cauchy bounds, or restart contraction. The numerical source error still has four separately controlled terms of size (\varepsilon_v/64). The algorithm differentiates finite polynomials and asks only for real activation values; high activation derivatives and later trained values are not input oracles.

The Taylor panel-count derivation deleted here is exactly the one retained in width; the correspondence (X=\beta^L), (\ell_n=\ell), (r_n=r_{\rm cap}), (b_n=b_{\rm cap}), (B_n=B_{\rm cap}) is explicit. Its count remains confidence-free and valid while the cap is active. Real interpolation nodes preserve exact image pairing. Harmonic keeps its joint time/quadric domain, positive quadrature, normalization and total weight bound, separate control of analytic image error, (d=1) case, and the exact mode set. Its label factor is preserved through (\alpha^{-1}=128\beta^{30L}(Y/\lambda)^2\sqrt{d+3}\ell^{3/2}).

I checked the sampler directly by expanding its conditional affine mean and orthogonal homogeneous space. The two directions are related by transposition with the correct stored-list swap. Zero/dependent queries, full opposite rank, singular Gaussians, adaptive layer choice, bounded stopping, and the product of conditional layer kernels remain covered. Completion is a proof object; the transcript has the exact dense law and all returned products agree with one completed matrix. The operation, Gaussian-draw and memory bounds are unchanged.

The finite numerical anchors still have exactly (bmK) accumulated columns, with causal coefficients and cached contractions. The four request classes include final source-basis images even when they are absent from the earlier query span. Substituting deterministic (\min(n,R)) for the query budget prevents conditioning a stopping bound on random final rank. Coupled explicit and implicit executions agree through source construction, selection, initial corrected-readout arrays, and autonomous future. No additional failure allowance or stronger matrix access has been introduced.

### Shared cost sums and public conclusions — PASS

I expanded each new shared expression at its stated substitutions and matched it term-by-term against its frozen baseline equation. All eight equations retain their labels and original sums (up to commutative order and (Ln^2N+Ln^2r=Ln^2(N+r))).

| Cost family | Shared substitution | Terms checked outside the shared part |
|---|---|---|
| Explicit Harmonic work/memory | (P=P_d, B=m+N_x) | Original matrices, geometry, time tables, projection, source and basis images, harmonic workspace |
| Explicit Taylor work/memory | (P=P_k, B=M+m) | Supplied (P_d), (dM^2+ndk), source-node evaluation/sorting, images, input map and transformed data |
| Implicit Harmonic work/memory | (e=d, F=N_x, Q=Q_{\rm H}) | Geometry, projection, time tables, harmonic workspace and data |
| Implicit Taylor work/memory | (e=k, F=M, Q=Q_{\rm T}) | Input reduction, source-node evaluation/sorting, input map and transformed data |

The shared formulas still charge sampler ( (L-1)nQ^2 ), accumulated trained-factor work ( (L-1)nm(m+F)J(J-1)K(K+1) ), factor memory ( (L-1)nJmK ), activation composition, (LnRr) orthogonalization, (Lnr^3) selection, metric solves, and initial Gram assembly. Numerical-only constants for finite sums are distinguished explicitly from fixed-problem constants in the headline cost table. The prose immediately before the eight displays states that the entire sum is inside (O(\cdot)).

The fixed-parameter orders give the original four work/memory pairs:

\[
\begin{array}{c|cc}
 &\text{work}&\text{peak memory}\\
\text{Harmonic supplied}&n^2\ell^{3d/2+1}&n^2\\
\text{Taylor supplied}&n^2\ell^{5/2}&n^2\\
\text{Harmonic implicit}&n\ell^{9d/2+3}&n\ell^{3d/2+1}\\
\text{Taylor implicit}&n\ell^5&n\ell^{5/2}
\end{array}
\]

Every entry denotes an (O\)-bound. I checked selector dominance for Harmonic, all three (n\ell^5) terms for implicit Taylor, and the supplied-matrix eventual dominance qualification. The full setup horizon, discarded working arrays, exact-real operation model, evaluator charges, supplied envelope/gap certificates, and restriction against subquadratic conversion of supplied matrices or a prescribed seed all survive.

## Integration, notation, and rendering

There is no proof cycle. Fitting and the deterministic source machinery precede the finite source event. The width assembly invokes the selected construction's deterministic transfer and Taylor source algebra, whose finite-panel use needs only that event, not the width theorem being proved. Initialization then uses the established quantitative source/count interfaces. The earlier initialization-jet compiler does not depend on the new efficient numerical compiler. Feature-learning and NTH do not become dependencies for the revised arguments.

All 30 persistent entries remain exactly as before. New/shared cost symbols are explicitly local, and source-rank bounds are distinguished from selected support sizes. The mathematical coefficient reuse identifies its defining recurrences. An independent scan of all final TeX found 287 labels, no duplicate labels, and no missing `ref`, `eqref`, `Cref`, `cref`, or `hyperref` targets. This is supporting integration evidence, not mathematical proof.

I directly inspected the supplied final page images 39, 40, 73, and 74. Pages 39 and 40 show the repaired (Z_0) and (D_c) expressions as intact displays with all factors visible. I independently rendered PDF pages 75 and 76 and inspected the images: page 75 contains the shared implicit memory continuation and all eight cost specializations, and page 76 contains the primitive counts and final asymptotic orders. The shared formulas, qualifications and displayed powers are readable without clipped terms or overlap. The PDF has 89 pages. I did not visually inspect every PDF page; the visual assignment was focused on repaired displays and shared costs.

The revised width and initialization modules total 2400 lines versus 2940 baseline lines, a reduction of 540 lines (about 18.4%). This is only a source-length measure. The substantive compression is repeated proof algebra replaced by checked internal references and four factored cost expressions; no claim depends on a study note.

## Frozen evidence

SHA-256 values were computed directly from the supplied files. The nine files marked `same` below were also compared byte-for-byte with `cmp`; the result does not rely on `preservation.json`.

| File | Final SHA-256 | Baseline |
|---|---|---|
| `compact.tex` | `62cbca244c507a581f462e0cc8c6a023c21a5ba2d3efba76f5998ffa9ef8bae6` | same |
| `feature_learning_theorem.tex` | `f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f` | same |
| `compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` | same |
| `compact_foundations.tex` | `44c201bda34d1eac488c9cc3347a4d2cf608128a3f774df65210584606feaf6a` | same |
| `compact_legendre.tex` | `862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9` | same |
| `compact_selected.tex` | `cce32506923384c8124e0a5f965591ad3ae67a51b62377098563eda9b4ff54fd` | same |
| `compact_feature_learning.tex` | `71f50a55613a3df12398d6226b8fe2380805f2f32082e134e7ab45846bfa4bd1` | same |
| `compact_nth.tex` | `38e50dee3b89a755e4efb719a8cf3396cd70f78a1cf163dbf0ff91076505a616` | same |
| `references.bib` | `1a5611e65d89ce20de47c62488c1fa34eb6e80c1777ab310e29723a94a0457a9` | same |
| `compact_width.tex` | `e28d2e777447c2f49ca5b97554ff5a3d2b50f8b867dd0284af96b51eaab49dfe` | `07cdfeda14ee650ae4d8b804cc7317f6046cd470542ec5edfb380b9c5f363988` |
| `compact_initialization.tex` | `f50b3d6f45d7aebdb37cfe6486b0f55637be5c7fc27386e52094112ca76f091a` | `f2f801a714205d28930c9887ded1d4028350c5a11379ba6440f6f9747f8366c5` |

Additional input hashes:

- Neutral assignment: `4135951f1d71acaaefddf7de87bf46381325a4545aa44ba21a3db15dd0bad30d`.
- Frozen `docs/index.qmd`: `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68`.
- Frozen `docs/notation.qmd`: `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023`.
- `preservation.json`: `2496749b6ba928a14efaf398c9991fd20b3ca8b04b175e6ec8d1fa99089af055`.
- Final `build/compact.pdf`: `e1befdf23ffb05b4165c17048082da945e54a02305bc1cdd1f6766d5775bc122`.
- Permitted v1 width: `09ae31ecae93a8ba295e3baa8e21d66ed19f6caa7d6a25f71d559df099a0924e`.
- Permitted v1 initialization: `eccbf4cad4e215fbcfc18263850165b0fd7dc6d8934de7c189a5e12ec89edd22`.
- Sorted final paper manifest: `25d4681e73548f54d2983132349392bb260f02c77cc28c28922f4d57af293f2d`.
- Sorted baseline manifest: `485a56c83acb0f0c186902e390beb79a3c40ee8fed1cf650070a483c7f911d56`.

Manifest convention: lexicographically sorted filenames, one line per file consisting of its lowercase SHA-256, two spaces, filename, and newline; SHA-256 of the resulting UTF-8 string. Each manifest contains all eleven paper files.

Independent whitespace-normalized extraction found all four theorem/proposition/lemma statement environments in width and all three in initialization identical to baseline. Public setup, theorem, proposition and assembly are byte-identical as part of `compact.tex`.

## Completion limitations and acceptance

All assigned shortening, quantitative-premise, dependency, access-contract, cost, notation, baseline-preservation and focused-rendering checks are complete. Required corrections: none. No numerical reproduction, finite-precision validation, external citation audit, whole-book audit, or renewed correctness certification of the unchanged feature-learning/NTH proof bodies is claimed. Those are outside this integration assignment. The preservation metadata mentions a book chapter not included in the frozen packet; I make no independent byte-preservation claim about that unsupplied chapter.

The final frozen paper passes this independent audit for proof shortening without loss of the assigned mathematical and computational content.
