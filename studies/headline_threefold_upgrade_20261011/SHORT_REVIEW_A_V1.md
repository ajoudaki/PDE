# Independent mathematical audit A: shortened paper v1

Verdict: **PASS for the assigned paper-only proof refactoring.** No required mathematical correction was found. This verdict covers the two shortened modules and the earlier proof bodies they require; it is not a new book-promotion verdict or a re-review of the separate feature-learning and NTH proofs.

Reviewer identity: `/root/short_audit_a_v1`. Authors/assembler identified in the neutral assignment were `/root`, `/root/shorten_width_author`, and `/root/shorten_setup_author`; the author-side selector was `/root/shorten_shared_opportunities`. I am distinct from those agents. I did not read author notes, their discussions, other reviews, other studies, study history, Git history, or evolving paper sources. I used no external scientific sources and made no source or Git edits.

## Inputs, isolation, and exact coverage

The scientific packet was `data/generated/headline_threefold_upgrade_20261011/short_paper_v1/`, with the neutral assignment at `studies/headline_threefold_upgrade_20261011/SHORT_REVIEW_ASSIGNMENT.md`. I read the complete assignment and the required rigorous-math skill, canonical-notation skill, and its complete neural-response-memory reference.

Complete direct scientific reads were:

| Candidate input | Direct coverage |
|---|---:|
| `paper/compact.tex` | lines 1–399 |
| `paper/compact_width.tex` | lines 1–1180 |
| `paper/compact_initialization.tex` | lines 1–1218 |
| `paper/compact_fitting.tex` | lines 1–241 |
| `paper/compact_foundations.tex` | lines 1–1530 |
| `paper/compact_legendre.tex` | lines 1–750 |
| `paper/compact_selected.tex` | lines 1–1096 |
| `paper/feature_learning_theorem.tex` | lines 1–62 |
| `docs/index.qmd`, `docs/notation.qmd` | complete |

The guide and notation were read at their authorized repository paths; subsequent `cmp` checks verified exact identity with the packet copies. An initially truncated width read was repaired by a direct lines 340–700 read covering the omitted region. The two baseline modules were compared through their complete unified diffs, with all deletions read and truncated diff output repaired in bounded chunks. Unchanged portions were read in the byte-identical candidate passages. I did not perform a separate sequential read of every unchanged baseline line.

The deliberately unread scientific complement consists of `compact_feature_learning.tex` (335 lines), `compact_nth.tex` (592 lines), and bibliography prose/entries (170 lines). Those bodies are outside the new proof targets. I mechanically checked their preservation, and read the complete separate feature-learning theorem interface. No required dependency body remains unread.

The initial packet's preservation booleans alone could not establish historical byte preservation. I reported this input limitation. The supervisor then explicitly authorized the supplemental frozen directory `data/generated/headline_threefold_upgrade_20261011/short_preservation_evidence/baseline/` solely for mechanical comparisons. Its stated provenance is extraction of commit `aa28e4693eecb93e6770db404878e959f5161fdf` using the study's checker. I did not read the checker, Git, or supplemental scientific text. Independent `cmp` and SHA-256 checks against these supplied baseline bytes resolved the limitation. Verification of the claimed Git extraction itself is outside this isolated audit.

### Input hashes

The following SHA-256 values were computed directly. For the nine unchanged entries, the supplemental baseline hash is identical to the candidate hash.

| Candidate file | SHA-256 |
|---|---|
| `compact.tex` | `62cbca244c507a581f462e0cc8c6a023c21a5ba2d3efba76f5998ffa9ef8bae6` |
| `compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `compact_foundations.tex` | `44c201bda34d1eac488c9cc3347a4d2cf608128a3f774df65210584606feaf6a` |
| `compact_legendre.tex` | `862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9` |
| `compact_selected.tex` | `cce32506923384c8124e0a5f965591ad3ae67a51b62377098563eda9b4ff54fd` |
| `compact_width.tex` | `09ae31ecae93a8ba295e3baa8e21d66ed19f6caa7d6a25f71d559df099a0924e` |
| `compact_initialization.tex` | `eccbf4cad4e215fbcfc18263850165b0fd7dc6d8934de7c189a5e12ec89edd22` |
| `feature_learning_theorem.tex` | `f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f` |
| `compact_feature_learning.tex` | `71f50a55613a3df12398d6226b8fe2380805f2f32082e134e7ab45846bfa4bd1` |
| `compact_nth.tex` | `38e50dee3b89a755e4efb719a8cf3396cd70f78a1cf163dbf0ff91076505a616` |
| `references.bib` | `1a5611e65d89ce20de47c62488c1fa34eb6e80c1777ab310e29723a94a0457a9` |

Other frozen hashes:

| Input | SHA-256 |
|---|---|
| Baseline `compact_width.tex` | `07cdfeda14ee650ae4d8b804cc7317f6046cd470542ec5edfb380b9c5f363988` |
| Baseline `compact_initialization.tex` | `f2f801a714205d28930c9887ded1d4028350c5a11379ba6440f6f9747f8366c5` |
| `docs/index.qmd` | `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| Neutral assignment | `c30e87828fbe3ba0123005cf6e6fc0797d0fe0202e3ae542b1c575ce3a056bd1` |

The supplemental baseline hashes of the two changed modules also equal the original packet baseline hashes above.

## Contract preservation

`compact.tex` is byte-identical to the supplemental baseline, establishing preservation of the entire public compression theorem, efficient-initialization proposition, operation model, probability conventions, and assembly. The separate feature-learning interface and the feature-learning/NTH proof bodies are also byte-identical. The complete unchanged dependency modules and bibliography passed `cmp` independently. The polynomial-onset theorem environment in the changed width module was separately extracted and compared: it too is byte-identical.

The preserved contract uses the residual \(r_a=f_a-y_a\), loss \(m^{-1}\sum_a r_a^2\), physical gradient flow with mobilities \((n,1,\ldots,1,n)\), ordinary Gaussian first/hidden matrices, and exactly zero initialized readout. Its small-label assumption is \(0<Y\le(\gamma/m)\beta^{-30L}\). The trajectory norm takes both suprema over the entire physical trajectory, includes the fitted endpoint, and uses either the whole sphere or the predeclared Taylor panel. A missing limit or zero denominator remains failure. No pointwise-in-time or endpoint lower bound is introduced.

I independently scanned the candidate TeX labels and references, including hyperref targets: 287 labels and 176 distinct referenced labels, with no duplicate or missing target found. This mechanical check supplements, rather than replaces, the proof-body checks below.

## Width proof: mathematical attacks and outcomes

Here \(X=\beta^L\), \(\lambda=\gamma/m\in(0,1]\), \(\chi=1+\lambda^{-1}\), \(S=16Y/\lambda\), and \(\ell_n=\log(en)\), as in the candidate.

### Finite initialization and independently stopped sources

I checked the covariance argument against singular and unequal marginal covariances. The empirical RMS concentration is derived from a Gaussian Lipschitz estimate; polarization gives the claimed entry error. Shrinking two covariance pairs to common marginal standard deviations and then varying correlation avoids any reciprocal variance. The correlation derivative is multiplied by the product of the marginal standard deviations, so continuity handles zero variances and correlations \(\pm1\). The recurrences for the RMS error and Gram-entry error close with the stated \(e_0,T_1,T_2,C_0^{\rm cov}\). The sphere-net estimate pays for dimension \(d\) without assuming \(d\le m\).

The cavity initialization transfer retains normalization \(n\), transfers a strict singular-value margin by zero embedding, and conditions on a fresh current row only after projecting the lower difference onto a deterministic ball. These are actual finite checks under \(N_{\rm src}\), not an appeal to the older eventual fitting threshold. Zero readout makes \(\bar F_a=\bar u_w^\top h_a^{(L)}\); rescaling by \(S\) creates no inverse-label derivative. The first-layer incoming row is correctly confined to the deleted scalar controls and supplies no fictitious retained reverse port.

For the deleted explicit map recurrences, I checked the earlier bodies at `cp:src-local-lemma`, `cp:src-response-recursion`, and `cp:src-direct-reverse`. They supply the three differentiated port forces, additive carrier curvature term, exact forward/backward remainders, lower-adjoint probe, and response products actually used by the shortened coefficient ledger. The new text retains the numerical map/control/time powers, including the single raw-coordinate \(\sqrt n\) factor and the \(X^{1000}\chi^2\) common envelope. The direct reverse-observable subtraction retains \(d_0+n^{-1/2}\); it is not estimated merely by an operator norm that would lose localization.

I checked the finite gate \(A\ell_n^{16}\le n^{1/1000}\), the confidence-order bounds, and their use in entropy and remainder absorption. Frozen one-dimensional histories are netted before adaptive substitution. Endpoint tests are measurable with respect to each cavity's own retained initialization and stop. The product grid plus prefix-level mesh covers a full-network-dependent common prefix only after the uniform Gaussian event is proved. The centered quadratic-form trace is retained; the adaptive substituted variations are not declared centered Gaussian. The entropy exponent \(0.627\) and mesh/deletion union exponent \(0.65\) stay below the Gaussian tail exponent \(0.78\). The remainder exponent \(-0.07875\) strictly improves the \(-1/25\) stop.

The rectangle and flaring-domain reuse is valid after the explicitly stated radius replacement. Its earlier proof supplies commuting Lipschitz retractions, the canonical contours, disk containment and the integration estimate for panel count. In imaginary time the frozen real symmetric generator is unitary; the \(C_gB_nYr_n\) term pays for its variation. No positivity of a complex algebraic Gram is assumed. Strict preactivation strip margins precede derivative use and continuation.

For budget removal I checked the distinction between the fixed-exponent main references and the order-\(u_\rho\) singleton/common-cavity corrections. Conditional independence is used only for distinct root pairs of one common cavity. The correction paths need not be mutually independent; Cauchy–Schwarz/Hölder and the explicit \(u\mu_n+u^2v_n^2\) gate supply their estimate. Repeated-index contributions retain their multiplicity and \(W_n\) factor. Markov gives \(emL(64e^2)^{-u_\rho}\le\rho/4\). The simultaneous two-domain failure allocation is within \(\rho\), with initialization counted once. Thus the finite claim does not exchange growing confidence/deletion order with an eventual-width limit.

The source gate contains no \(Y^{-1}\). The source-panel coefficient is confidence-free and preserves \((Y/\lambda)^2\sqrt{\ell_n}\); the extra capped-radius term is absorbed using \(b_n^{3/2}\le4\sqrt{\ell_n}\). The real late-time extension uses fitting and parameter subtraction, including its RMS-to-coordinate factors, rather than a late-time complex-domain claim.

### Actual dense discrepancy

I reconstructed the small-ball proof from the characteristic function, its Gaussian majorant and the finite Fourier cutoff. With \(h=\tau\sigma_0/24\), the leading small-ball term is at most \(\tau/8\). The variance lower bound follows from the full squared-area and spectral calculation in `cp:innovation` before its equal-diagonal specialization; that earlier proof really does establish the reused general inequality.

Conditioning on the first run through layer \(L-1\) and the entire second run leaves conditionally iid final feature rows. Choosing a conditional variance-maximizing coordinate is measurable. The quantitative covariance event gives \(\bar Q\succeq\gamma I/2\); the fourth/sixth moment bounds give

\[
\sigma_0^2=\frac{Y^2\gamma^4}{256X^{16}},\qquad
\frac{M_3^2}{\sigma_0^6}\le2^{30}m^6X^{96}\gamma^{-12}.
\]

The exact initial velocity factor \(2/(mn)\) gives derivative separation \(\tau Y\gamma^2/(192mX^8\sqrt n)\). Previous layers and the independent run enter only as a shift, which the finite inequality permits. The parameter-two ellipse fits the smaller training rectangle. With polynomial degree at most \(4\ell_n\), derivative transfer gives the stated \(\ell_n^{-5/2}\) trajectory factor; the third lower-width gate absorbs the \(n^{-2}\) analytic tail. This is an actual two-run lower event. The sharper eventual lower coefficient from the older proposition is not silently assigned polynomial onset.

### Third-order Legendre defect and Taylor assembly

I checked the actual closure's physical defect, order-independent fitting, backward-history freezing, signed comparison and coefficient ledger in the complete earlier Legendre proof. Those dependencies use the same closure residual and dense response reference, so the shortened cross-references do not switch dynamics.

Subtracting the integrated feature defect defines \(g\) with \(\partial_\tau g=a\). Its first derivative vanishes at the constant-prefix join because the initialized readout is zero. The weighted second derivative is controlled because \((A-\tau(t))/\widehat\rho(t)\le4/\lambda\). Consequently the Legendre differential operator gives a \(q^{-2}\) forward tail without a jump term. Differentiation follows the actual closure trajectory, including its defect; gate products use coordinate carrier/response caps with RMS velocities, avoiding an extra \(\sqrt n\) loss.

Writing \(d\) for integrated matrix-defect norm and \(D\) for the maximum summed parameter discrepancy, the checked inequalities are

\[
H\le YP\ell_n/q^2+Pd,\quad B\le2YP\ell_n/q,\quad
d\le2(L-1)HB,\quad D\le Pn^{1/64}d.
\]

At \(q\ge4P^3\ell_n\), the linear term absorbs and yields \(d\le4YP^3\ell_n^2/q^3\), \(D\le4YP^4\ell_n^2n^{1/64}/q^3\). The structural gate also ensures \(q\le\sqrt n\) and improves the bootstrap to \(Y/(2\sqrt n)\). Substituting the prescribed \(q\) yields the power \(n^{-47/64}\). The final ratio has power \(n^{-15/64}\), which becomes \(n^{-1/8}\) after the explicit logarithm absorption. Moving and fixed inventories remain exactly the displayed \(n(d+1)+1+2(L-1)mnq\) and \((L-1)n^2\).

For Taylor, the earlier selected proof supplies independent fitting, exact metric isometry, the corrected readout, and the cancellation of the \(2V_Ce\) feedback term. The finite source event supplies all of its actual hypotheses. The reused Taylor proof supplies the half-radius tail, Euclidean base-coefficient error, exact initialized images, and input-span reduction. Compactness supplies the small rectangle needed by the origin-jet compiler. The finite degree gate preserves \(K+1\le8\ell_n\), with \(Y^{-1}\) used only for this simplification. Squaring the panel rank retains

\[
(m+p)^2\big[(Y/\lambda)^4\ell_n^3+
\lambda^{-2}\ell_n^2\log^2(e+\ell_n)\big].
\]

The two final width maxima have only the stated polynomial factors. Their probability union needs no independence between source and lower-bound events. No Harmonic or feature-learning polynomial-onset assertion has been added.

## Numerical initializer and Gaussian execution

The signed approximate-path proof retains the negative prediction-error square before maximization. Its result is

\[
E'\le2J^{\rm r}\rho E+
\tfrac12(C^{\rm r}+J^{\rm r})^2E^3+\|d_u\|.
\]

The integrating factor uses finite residual activity, and the two explicit smallness conditions exclude the first transformed-error crossing. The earlier signed lemma supplies precisely the identity and zero-error regularization now cited; the candidate supplies the new cubic estimate and constants itself. Endpoint Taylor remainders retain their carrier, changed-mixer and changed-readout contributions. The passive source estimate pays both RMS-to-coordinate factors and the initialized image operator bound.

I checked the moving complex ball: its radius controls preactivation change by \(a/16\), carrier change by one, and hence keeps the half-strip margin and a proved pairwise Lipschitz constant. The two ellipses cover the required rectangle and Cauchy disks. Discrete activation coefficients include aliasing, allowed value-call errors, and derivative control through the second derivative. The backend uses original activation values, not an oracle for high derivatives.

The local error map has contraction factor at most \(1/4\); the local solution discrepancy and parameter/derivative Taylor tails fit the stated smaller ball. The degree prescription bounds integrated defect over all panels. Applying stability on each completed prefix closes restart induction from exact initialization. The four source-error terms each fit \(\varepsilon_v/64\), giving the claimed \(\varepsilon_v/16\). This verifies \(J,D=O(\ell^{3/2})\), \(K=O(\ell)\) at separately fixed parameters. It covers the entire \(T=32\ell/\lambda\), with the compressed model initialized at time zero.

For Taylor, the flaring-panel reuse exactly identifies \(r_n,r_{\rm cap}\), \(b_n,b_{\rm cap}\), and \(B_n,B_{\rm cap}\). Chebyshev-root interpolation has the stated norm bound, reproduces the retained polynomial, and commutes with each initialized matrix. Base Euclidean errors are converted to image errors using operator norm eight. The numerical degree \(K_s\), including its factor two, is separately checked against the existing polynomial count gate. It has not been silently identified with the origin-jet degree.

For Harmonic, I checked positivity and unit mass of the polar rule, exactness through degree \(N_\theta-1\), the trapezoid and Chebyshev tails, and telescoping across the time/angle factors. Successive complex rotations remain within the query tube; the harmonic and Jacobian envelopes are charged. Exact and numerical coefficient errors are allocated separately for both a base and its analytic image. Applying initialized matrices to accumulated base coefficients preserves exact pairing. The mode set, two-point \(d=1\) case, and the factor \(\alpha^{-1}=128\beta^{30L}(Y/\lambda)^2\sqrt{d+3}\ell^{3/2}\) survive unchanged.

For the Gaussian sampler I independently checked the mean

\[
A=YV^\top+UR^\top(I-VV^\top)
\]

and conditional unexplored block \((I-UU^\top)G(I-VV^\top)\). Compatibility gives both observed directions. A new forward direction splits the unexplored matrix into a Gaussian action and a cross-covariance-zero remainder; the transpose calculation is the transposed split. This works for singular covariances, dependent queries and full opposite rank. Adaptive direction/layer choices are transcript-measurable. Bounded stopping preserves the conditional product kernels. Completing each layer at the stop gives ordinary independent Gaussian matrices and agreement with every earlier reply on one probability space.

I checked the per-request count and its sum \(4nQ^2+6nQ+2\), the maximum \(2n-1\) drawing increments, and storage of the four column lists without dense projectors. The client query list includes final basis images. Factored numerical anchors exactly reproduce explicit execution through coefficients and panels, including both directions; they do not assert finite rank for the true continuous dense trajectory. Deterministic tie-breaking then yields the same selected arrays and autonomous future pathwise. No additional source-event failure allowance is required, and the implicit method does not purport to convert supplied matrices or a prescribed seed.

## Four work and peak-memory bounds

I expanded the shared finite sums against the baseline ledgers. Terms for initialized images, final basis images, input reduction, geometry, node assignment, current-panel polynomial composition, accumulated trained factors, source orthogonalization, selection and metric/Gram assembly remain charged. The shared explicit memory sum still contains \(P_d\), even for reduced-input Taylor with supplied matrices. The implicit substitutions are \((e,F)=(d,N_x)\) and \((k,M)\); the extra \(m\) charges training backward queries in the latter.

The decisive fixed-parameter substitutions are:

| Quantity | Harmonic | Taylor |
|---|---|---|
| Numerical panels and activation degree | \(J,D=O(\ell^{3/2})\) | same |
| Time-series degree | \(K=O(\ell)\) | same |
| Source rank | \(R=O(\ell^{3d/2+1})\) | \(R=O(\ell^{3/2})\) |
| Initialized-matrix query count | \(Q=O(\ell^{3d/2+1})\) | \(Q=O(\ell^{5/2})\) |

For supplied Harmonic, constant-anchor products and initialized source/basis images cost \(O(n^2\ell^{3d/2+1})\); the selector costs \(O(n\ell^{9d/2+3})\) and is eventually smaller. Supplied Taylor has \(n^2JK=O(n^2\ell^{5/2})\); the remaining width-proportional terms fit \(O(n\ell^5)\). Both peak-memory sums are \(O(n^2)\).

For implicit Harmonic, the sampler exponent is \(3d+2\), trained-factor and activation exponent \(3d/2+7/2\), and projection exponents at most \(3d-1/2\) and \(3d/2+7/2\). All lie below the selector exponent \(9d/2+3\) for \(d\ge1\). Its memory is \(O(n\ell^{3d/2+1})\). For implicit Taylor, each of \(nQ^2\), \(nJ^2K^2\), and \(nJDK^2\) has exponent five; selection has exponent \(9/2\), and peak memory has exponent \(5/2\). These yield exactly all four public work/memory rows.

The finite ledgers use numerical constants; the public asymptotic table allows dependence on separately fixed problem parameters and confidence. Original activation calls, elementary operations, Gaussian samples, supplied envelopes/gap certificates, and nonprimitive evaluator work/description/scratch retain their stated treatment. Exact ranks and exact zero tests remain exact-real qualifications. None of these counts proves bit complexity or finite-precision stability.

## Compactness, component verdicts, and completion

The width module decreases from 1430 to 1180 lines; initialization decreases from 1510 to 1218, a combined reduction of 542 lines (about 18.4%). Essential new mathematics remains in the manuscript. The main reuse targets are valid earlier proof bodies: stopped local maps and responses, working domains, squared-area innovation, backward-history freezing, signed comparison, Taylor source compilation/input reduction, and scalar Fourier approximation. New finite probability, degree, restart, and cost powers remain explicit. The shared cost sums are defined before substitution and reduce genuine duplication without changing parameter conventions.

| Component | Verdict |
|---|---|
| Public theorem/proposition and separate theorem preservation | PASS, independent byte comparison |
| Finite source probability and source domains | PASS |
| Actual dense lower event | PASS |
| Third-order Legendre estimate and width gates | PASS |
| Taylor polynomial accuracy/count gates | PASS |
| Numerical source construction, stability and restart | PASS |
| Taylor/Harmonic spaces and exact initialized pairing | PASS |
| Adaptive two-direction Gaussian sampler and pathwise coupling | PASS |
| Four finite ledgers and asymptotic work/memory bounds | PASS |
| Self-containment, notation scope and cross-reference reuse | PASS |

Required corrections: **none**. Unresolved assigned proof obligations: **none**. I did not compile TeX or perform numerical experiments; this was a mathematical source audit with mechanical preservation/reference checks. The feature-learning and NTH bodies were intentionally not re-proved. No empirical, finite-precision, book-promotion, or historical-repository certification is implied by this report.
