# Final integration review V3

Verdict: **PASS for the assigned integration scope.** No required scientific or integration correction was identified. The paper puts a polynomial sufficient-width guarantee for Legendre and Taylor inside its main theorem and places the four-row efficient-initialization proposition immediately afterward. The complete new proofs support these interfaces without changing the original model, storage powers, query domains, optimizer, label condition, or comparison denominator. The frozen book differs from the approved scientific reference only in two clarifications of coefficient locality.

Reviewer: fresh isolated agent `/root/final_integration_v3`, 2026-10-11. This is a final integration audit, not either of the paired promotion reviews and not a whole-book or whole-paper proof reaudit. No prior review, author check, study history, other study, or evolving source was consulted. No subagent was used. The reviewer wrote only this report and `data/generated/headline_threefold_upgrade_20261011/final_review_v3/`.

## Assignment and evidence boundary

The neutral assignment was to audit the frozen `paper_integration_v3/{paper/,docs/,integration.diff,preservation.json}` against the approved reference `promotion_v6/docs/08b-trajectory-compression.qmd`: complete new width/setup statements and proofs; the main theorem, assembly, and interfaces in both formats; necessary older dependency bodies; constants, probability and cost scopes, provenance, the actual dense discrepancy, references, local notation, and preservation. Untouched NTH and separate feature-learning proof bodies were excluded as independent proof targets, while their inputs and claims had to remain preserved.

Required instructions read completely: `RESEARCH_WORKFLOW.md` Parts 1 and 2; `/etc/codex/skills/solve-math-rigorously/SKILL.md`; `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`; and its full `references/neural-response-memory.md`. The frozen notation contract and reading guide were used. No author startup or study README was read.

The supervisor subsequently authorized exactly these read-only baseline Git objects at `ef8362764b4eb8144d7af8d6f8db080fdaaf82ca`: `paper/compact.tex`, `compact_foundations.tex`, `compact_selected.tex`, `compact_fitting.tex`, `compact_legendre.tex`, `feature_learning_theorem.tex`, `compact_feature_learning.tex`, `compact_nth.tex`, and `references.bib`. Their bytes were used only for preservation/diff authentication. There was no history search. Rendered checks used the explicitly supplied paper PDF and final book PDF/chapter HTML; no other rendered chapter was read.

## Exact reading coverage

The following paper sources were read completely, including proof bodies and finite ledgers:

| Source | Lines | Purpose |
| --- | ---: | --- |
| `compact.tex` | 1–399 | Model, constants, probability, notation inventory, main theorem, setup proposition, assembly |
| `compact_width.tex` | 1–1430 | Complete finite source proof, actual dense lower bound, third-order Legendre estimate, Taylor and final polynomial gates |
| `compact_initialization.tex` | 1–1510 | Complete source routine, stability/restarts, activation backend, both source spaces, sampler/coupling, all cost and storage ledgers |
| `compact_fitting.tex` | 1–241 | Initialization, fitting, tails, signed comparison |
| `compact_foundations.tex` | 1–1530 | Complete source proof and the coefficient, cavity, Gaussian, and working-domain dependencies used by the additions |
| `compact_legendre.tex` | 1–750 | Projection, runtime, order-independent fitting, defect/stability ledgers, derivative-to-trajectory and innovation dependencies |
| `compact_selected.tex` | 1–1096 | Selector, exact metric, corrected dynamics, fitting/cancellation/tails, initialized jets, Harmonic and Taylor source/count dependencies |
| `feature_learning_theorem.tex` | 1–62 | Preserved separate theorem and its assumptions/scope |

Additionally read `compact_feature_learning.tex` lines 1–82 (proof interface and initial-velocity dependency, extending slightly beyond the required interface) and `compact_nth.tex` lines 1–205 (its separate model, clock, data, counts, theorem/corollary, and initial dependency passage). The remaining lines 83–335 and 206–592, respectively, were not independently read or reaudited; the whole files were authenticated as byte-identical to baseline. Bibliography bytes and citation-key inventory were checked mechanically; this was not a literature review.

Frozen book sources read directly: all 98 lines of `notation.qmd`, all 260 lines of `index.qmd`, and all 68 lines of `_quarto.yml`. In `08b-trajectory-compression.qmd`, direct readings covered lines 1–365, 3214–3320, 4701–4762, 5900–5970, 7392–7468, 7914–7961, and both locality-diff passages around lines 619 and 2242.

The complete book width section, lines 3214–4595, and complete setup proof, lines 5965–7391, were mechanically compared with the fully read paper versions, then every remaining difference was inspected. This establishes shared proof coverage; it is not claimed that each unchanged book line was separately reread. The comparison preserves prose and mathematical tokens while normalizing structural TeX/Quarto syntax, references, the readout translation `W^{(L+1)} ↔ w`, and activation layer notation. All 74 width and 103 setup difference fragments were inspected. They consist of display/table/list markup, two display-line breaks, the local absolute width constant `C ↔ c_{wid}`, explicit local definitions and the feature-learning scope clarification added in the paper, `psi^{(j)} ↔ psi_j`, the local ellipse variable `w ↔ zeta`, explicit source-reference wording, and statement-type wording. No different mathematical assertion or proof step was found.

The approved chapter was compared bytewise in full but read scientifically only through those differences and the corresponding candidate coverage. Older book dependency bodies outside the stated direct coverage were not independently reread in book typography; the complete corresponding paper dependency bodies listed above were read. Book feature-learning proof bodies after line 7468 were outside the independent proof target. No other chapter, maintained code API, or archived `old_docs/` passage was read. There are no new empirical results or maintained code changes in this packet to reproduce.

## Scientific and interface findings

### Width refinement

The common setup remains full-MSE physical gradient flow with mobilities `(n,1,...,1,n)`, ordinary independent Gaussian first/hidden matrices, zero readout, separately fixed correlated normalized data, `m >= 2`, `L >= 2`, positive population gap `gamma`, `lambda=gamma/m <= 1`, and `0 < Y <= lambda beta^{-30L}`. The finite-width probability is for each fixed problem and individual width. Neither a simultaneous dataset event nor unrestricted growing-data limit is introduced.

The finite source threshold is explicitly defined. Its initialization and cavity arguments do not require nonsingular intermediate Gaussian covariances, input rank, orthogonality, or an inverse label factor. I checked the covariance propagation, retained-measurable endpoint grids, frozen-control conditioning, interpolation and entropy exponents, the growing confidence-order moment calculation, and its probability union. In particular the gate controls deletion order, logarithms, and the quantitative map coefficients before invoking the Gaussian union. The panel geometry uses its capped radius rather than waiting for the original qualitative radius gate to become inactive. The training and panel events together use a total allowance strictly below `rho`, as claimed.

The denominator is the actual pair of independent dense predictors, with the same training data and query domain. The finite lower proof conditions on the first run below its last layer and the second complete run, uses a shift-uniform scalar small-ball inequality, and transfers an initial derivative separation into the supremum over a positive training-time interval. The conditional variance and third-moment powers yield the displayed lower-width gate. The analytic transfer error is absorbed by the third gate. The witness training input lies in both promised domains. The proof does not claim separation at every time or at a fitted training endpoint, where both references equal the label.

For Legendre I checked the clock normalization, constant/zero prefixes, exact reconstructed physical defect, actual-trajectory differentiation including the defect, zero prefix derivative at the join, weighted second-derivative projection estimate, backward freezing estimate, and signed comparison. Their product yields a third-order history defect without new state. The gates close `q <= sqrt(n)`, absorption, and the `Y/sqrt(n)` bootstrap; the whole-sphere output bound and fitted endpoint then follow. Dividing the `n^{-47/64} log(en)^2` error by the dense lower event leaves `n^{-15/64} log(en)^{9/2}`; the supplied logarithm bound yields the claimed polynomial accuracy gate. No inverse-label width factor is required for Legendre.

For Taylor the capped source count retains its `(Y/lambda)^2` term before squaring. The exact rank/inventory, input-span reduction, passive-query contract, exact initialized-image pairing, and `Y/n` tail allocation agree with the selected-model proof. The inverse-label gate is used to obtain `K+1 <= 8 log(en)`, not to change the source-probability proof. The explicit final maxima are polynomial in the parameters stated in the headline theorem, with one absolute exponent and coefficient; their enormous size is not represented as practical. The storage coefficients remain functions only of activations and depth.

### Four initialization claims

The four headline work/memory rows agree with the full ledgers. Supplied matrices define the actual reference realization. The implicit alternative samples a fresh ordinary Gaussian reference through adaptive products in both directions. Its proof-only completion is not an algorithmic dense array and does not provide a conversion of supplied entries or a prescribed seed.

The source construction is an executed finite prescription from initialization: exact original initialized training features, a finite real-value activation polynomial backend, causal numerical jets and restarts through `T=32(m/gamma)log(en)`, and real interpolation or positive quadrature. It does not take trained-reference states or high activation derivatives as inputs. The signed real stability inequality, complex moving-ball bounds and activation approximation justify those numerical sources against the original dense flow. The compressed runtime starts at zero and uses the original activations and unchanged corrected optimizer.

Taylor uses its polynomial source/tail/count gates; the doubled interpolation degree still satisfies the stated `8 log(en)` gate. Harmonic retains its eventual source and scalar gates, with separate two-point treatment at `d=1`. Both preserve initialized-image pairing exactly and charge approximate generators by their actual span; no accidental rank deficiency is assumed stable.

The two-direction sampler accounts for repeated/dependent queries, full-rank saturation, layer adaptation, bounded stopping, and conditioning on the entire transcript. Its shared completed matrix gives pathwise agreement of the finite numerical algorithm, selected arrays, and future runtime. The independent-completion argument preserves the ordinary Gaussian law jointly across layers and with the first matrix.

The ledgers include initial feature evaluation, input reduction, dense or factored anchors, cached high-order actions, accumulated factor histories, source images, final basis images, source orthogonalization, the `n r^3` selector, metric/Gram solves, scalar geometry, activation composition, and scratch. At fixed parameters, `J,D=O(log(en)^{3/2})` and `K=O(log(en))`. Harmonic has rank `O(log(en)^{3d/2+1})`, so selection gives the advertised implicit `O(n log(en)^{9d/2+3})` work. Taylor's query count `O(log(en)^{5/2})`, accumulated factors, and activation compositions each fit `O(n log(en)^5)`. Their simultaneous memory counts match the table. In the supplied variants the additional terms are eventually below the stated `n^2` leading work and memory bounds. Setup big-O constants may depend on the entire separately fixed problem and confidence, explicitly distinct from storage constant `C`.

The exact-real primitive model, supplied activation envelopes/population-gap certificate, and separately charged nonprimitive evaluators are visible at the public interface. Finite precision, bit complexity, empirical speedup, and a favorable comparison with every high-order dense integrator are not claimed.

### Preservation, locality, placement, and references

Authenticated baseline comparisons show the 11 original headline formula environments unchanged: network, backward responses, physical flow, population Gram/label scale, label condition, trajectory norm, relative-error assertion, all three storage counts, and absolute selected-model accuracy. The complete 30-item persistent notation inventory is unchanged. Fitting, Legendre, both separate feature-learning files, NTH, and bibliography are byte-identical to baseline. The three modified older files contain only the supplied integration changes; the authenticated and supplied diff have identical nonblank changed-line sequences. Their raw diff sequences differ only in which unchanged blank line the two diff algorithms align.

The NTH benchmark remains explicitly separate: two identity hidden activations, growing correlated data, half-MSE clock, and a fixed short horizon. It is not turned into a same-family storage separation. The nonaffine/nonparallel-input hypotheses and up-to-four predeclared Taylor witnesses remain confined to the separate feature-learning theorem. Polynomial onset is explicitly not asserted for those certificates.

New auxiliary symbols remain local. The width proof explicitly recalls its source coefficients, defines its scalar envelopes/carriers and normalized parameter coordinates, and distinguishes the failure allowance `rho` from residual RMS `rho(t)`. The paper's local absolute width constant avoids confusion with its persistent activation/depth storage constant. The setup recurrences define quantities before numerical use; the Taylor-specific radius is explicitly given by a later named formula. The two book prose clarifications describe these coefficient recalls without altering the coefficients.

The main theorem refers to a coupled ordinary dense reference under either initializer, with an independent second dense run. Assembly keeps the qualitative sharper lower coefficient separate from the new quantitative weaker lower event. Stale blanket statements denying polynomial widths or all efficient preprocessing have been replaced; the original initialized-jet compiler is accurately retained as an alternative without an efficient work claim.

All 287 paper labels are unique, and every parsed `ref`, `eqref`, `Cref/cref`, and `hyperref` target resolves. All citation keys resolve in the preserved bibliography. All 300 chapter identifiers are unique, and all internal Quarto `@` scientific references resolve. This is not a global audit of links in unprovided book chapters.

## Executed checks and rendered interfaces

The reproducible checker is `data/generated/headline_threefold_upgrade_20261011/final_review_v3/check.py`. It verifies the frozen manifest hashes, labels/references, authorized baseline bytes and original formula environments, and saves complete translation difference fragments. Its run completed successfully. `authenticated.diff`, `preserved_files.json`, `hashes.json`, `width_translation_differences.json`, and `setup_translation_differences.json` retain the mechanical evidence. Additional direct Python checks confirmed unchanged persistent notation, immediate theorem/proposition adjacency, citation-key resolution, and authenticated nonblank diff correspondence.

`diff -u promotion_v6/docs/08b-trajectory-compression.qmd paper_integration_v3/docs/08b-trajectory-compression.qmd` showed exactly two locality-prose changes, at approved-reference lines 619 and 2240. It showed no mathematical change or other prose change to the approved chapter.

The paper PDF has 94 pages. `pdftotext -layout` confirmed the main theorem/setup interface, assembly references, and absence of `??`/undefined markers in extracted text. The reviewer visually inspected rendered page 4: the polynomial statement is part of Theorem 1.1, Proposition 1.2 follows immediately, all four rows are legible, and the provenance/primitive/constant qualifications are present. No clipping, overlapping table content, or broken interface numbering was found there.

The final book PDF has 1810 pages. Only outline metadata was used to locate Chapter 9, followed by text extraction of pages 922–923 and 966–967 and visual inspection of pages 923 and 967. Theorem 33 and Proposition 15 display the intended widths, setup rows, and resolved references without clipping or overlap. The chapter HTML contains the quantitative theorem, setup proposition, and both final-width-gate anchors; no `quarto-unresolved-ref` marker was found. Rendered text, images, and comparison outputs remain in the assigned scratch directory. The reviewer did not build the book or inspect every rendered page. Initial attempts to use optional `fitz`/`pypdf` readers failed because those modules were absent; `qpdf` outline metadata and Poppler tools supplied the focused checks without installation.

## Exact hashes

All entries below are SHA-256. Paper and docs names are relative to `data/generated/headline_threefold_upgrade_20261011/paper_integration_v3/`.

| Frozen input | SHA-256 |
| --- | --- |
| `paper/compact.tex` | `62cbca244c507a581f462e0cc8c6a023c21a5ba2d3efba76f5998ffa9ef8bae6` |
| `paper/compact_width.tex` | `07cdfeda14ee650ae4d8b804cc7317f6046cd470542ec5edfb380b9c5f363988` |
| `paper/compact_initialization.tex` | `f2f801a714205d28930c9887ded1d4028350c5a11379ba6440f6f9747f8366c5` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `paper/compact_foundations.tex` | `44c201bda34d1eac488c9cc3347a4d2cf608128a3f774df65210584606feaf6a` |
| `paper/compact_legendre.tex` | `862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9` |
| `paper/compact_selected.tex` | `cce32506923384c8124e0a5f965591ad3ae67a51b62377098563eda9b4ff54fd` |
| `paper/feature_learning_theorem.tex` | `f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f` |
| `paper/compact_feature_learning.tex` | `71f50a55613a3df12398d6226b8fe2380805f2f32082e134e7ab45846bfa4bd1` |
| `paper/compact_nth.tex` | `38e50dee3b89a755e4efb719a8cf3396cd70f78a1cf163dbf0ff91076505a616` |
| `paper/references.bib` | `1a5611e65d89ce20de47c62488c1fa34eb6e80c1777ab310e29723a94a0457a9` |
| `docs/08b-trajectory-compression.qmd` | `4b18d60c47f760e91d0077182b56c97484697753937c814d64264d52df2d03aa` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `docs/index.qmd` | `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68` |
| `docs/_quarto.yml` | `3a64f59b5923060d7196ffaf7ad8494ec3a6f906c90d2801e86ecdb3027d5a2e` |
| `integration.diff` | `609d64cf57d18aadbce840ddb2748542eb96e8820b75657e2f6302b6e88ffad5` |
| `preservation.json` | `a980339984e62994f7b0e64e32cc0ab7bf0b853837941303e905a94b8bfaf0cf` |

Approved scientific reference `promotion_v6/docs/08b-trajectory-compression.qmd`: `3b6ca32de3f4feef6771c15c7826edc4c38d70836e7d261fa06468582f4646f1`.

Rendered paper `paper_integration_v3/build/compact.pdf`: `9c805f6cd89280b7ce92435e3c3a66ecda2e578c03b69c73b98ee60ac7ae13f9`.

Rendered book `book_live_integration_v2/live_source_snapshot/data/generated/DTDL/DTDL.pdf`: `df11c3753415976f85cbfba4a43e5d4bc4e1e38134bc952f88b32f9163288011`.

Rendered chapter HTML at that same output directory: `5eed3cd9f617ae2d2b5968021f98504263b579f5390ad7c61ba68f247afbe53e`.

Baseline hashes for every authorized object, including changed older sources, are recorded in `final_review_v3/preserved_files.json`. The frozen input hashes were rechecked after review.

## Completion and limits

All assigned new scientific text, its necessary dependency argument, the two-format interfaces, preservation checks, and focused rendered checks are complete. There are no unresolved blockers and no requested optional correction. This verdict does not assert practical sharpness of the very large polynomial thresholds, finite-precision executability, empirical reproduction, complete rendered-layout inspection, independent correctness of the unread separate NTH/feature-learning proof complements, or a new whole-book proof audit. It is valid for the exact frozen hashes above.
