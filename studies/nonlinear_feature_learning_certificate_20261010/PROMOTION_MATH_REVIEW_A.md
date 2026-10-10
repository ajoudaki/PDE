# Independent complete scientific review A — frozen promotion packet v1

**Overall scientific verdict: PASS.** The entire proposed section is mathematically sound under its stated inherited assumptions. I found no required scientific correction and no unresolved scientific objection. The candidate faithfully translates the supplied final paper theorem and shortened proof into the maintained book's notation. Its prerequisite uses are supported by the complete frozen Chapter 9.

This is a verdict on the frozen v1 scientific text, not an assertion that a rendered v1 book is ready to publish. During review the supervisor supplied one operational notice: five proof anchors lack blank-line separation from their fenced proof divs, and a v2 rendering copy reportedly repairs only spacing. I have not read v2 or independently verified that report. The v1 source visibly has the indicated adjacent anchor/div lines. That formatting issue does not change the mathematics reviewed here.

## Isolation, inputs, and coverage

I acted as a fresh isolated reviewer. I read the neutral assignment, the complete frozen packet below, the rigorous-math skill, and the canonical-notation skill with its neural-network reference. I did not read study history, the study README, selector output, prior reviews, another reviewer's work, other studies, Git history, the live book, or scientific sources outside the packet. I did not call `list_agents`, contact peers, delegate review work, or modify the candidate, book, input packet, or Git. The only incoming substantive task update was the operational formatting notice identified above; it supplied no scientific finding.

Required instructions read completely:

- `studies/nonlinear_feature_learning_certificate_20261010/PROMOTION_REVIEW_ASSIGNMENT.md`.
- `/etc/codex/skills/solve-math-rigorously/SKILL.md`.
- `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`.
- `/home/amir/.codex/skills/explain-with-canonical-notation/references/neural-response-memory.md`.

All packet paths in this report are relative to `data/generated/nonlinear_feature_learning_certificate_20261010/promotion_v1/review_inputs/`. Every line of every listed file was read, including all existing Chapter 9 proofs. An initially truncated aggregate read was repaired with explicit subsequent reads. Chapter 9 was read in contiguous ranges 1–550, 551–1100, 1101–1650, 1651–2200, 2201–2750, 2751–3300, 3301–3850, 3851–4400, and 4401–4537. The candidate was subsequently reread completely as 1–279 and 280–511. The index was reread separately in full.

| Frozen input | Exact line coverage | SHA-256 |
|---|---:|---|
| `manifest.json` | 1–42 | `40e79ca02b8585f36084bae0598f20c730fce6156d6378d5339c391494ff1023` |
| `index.qmd` | 1–260 | `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68` |
| `notation.qmd` | 1–98 | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `08b-trajectory-compression.qmd` | 1–4537 | `4aeaa51c0da24b65acf8b26edb4c4437dbb5dee14a3f336034de7c787faa6571` |
| `compact.tex` | 1–298 | `5944806ea716f04baea2a8e56d79db913613c3a168dc2644cf5d81cd53daec21` |
| `compact_fitting.tex` | 1–241 | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `feature_learning_theorem.tex` | 1–62 | `f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f` |
| `compact_feature_learning.tex` | 1–335 | `71f50a55613a3df12398d6226b8fe2380805f2f32082e134e7ab45846bfa4bd1` |
| `PROMOTION_SECTION.qmd` | 1–511 | `c04cc608c43cc0c402db40b1f0d4241e71a65eb9cd70bed5dcc18aff82fc307f` |
| `assemble_promotion.py` | 1–57 | `0a8716e6e88678c1f8386f64ee50a54282a3b47892012fc86e2d45b4c43c28e4` |

Total packet coverage is 6,441 lines. All nine source-file hashes agree with the manifest. In-memory insertion of the candidate at the unique assembly heading yields the manifest's assembled-chapter hash `5ca14b38f84ecfc62644ee0bf9bcadb434f2ff79f1ef3fe422e25c1d92af89b2`. No assembly script was executed against the live checkout. All candidate mathematical cross-references resolve in this assembled text, and its explicit IDs are unique.

## Scientific setup and prerequisite audit

The inherited network has fixed $m\ge2$, $L\ge2$, input dimension $d$, unit normalized inputs $v_a=x_a/\sqrt d$, and width $n\to\infty$. Its loss is $m^{-1}\sum_a(f_{n,a}-y_a)^2$; the block mobilities are $(n,1,\ldots,1,n)$, and the stored readout is exactly zero initially. Hidden matrices have independent $N(0,1/n)$ entries, and the first-layer rows are independent standard Gaussian vectors. Each activation is real analytic, has bounded first and second derivatives on the real line, and grows at most linearly. The new theorem additionally assumes that each activation is nonaffine and $ |v_a^\top v_b|<1$ for distinct training samples. Labels are fixed, nonzero, and satisfy the inherited small-label condition.

The direct new dependencies are the real fitting lemma and the three absolute approximation propositions. I checked their hypotheses and the portions of their proofs used here, while reading the remaining Chapter 9 proofs completely:

- Chapter 9 lines 223–461 establish initial Gram convergence, a probability-tending-to-one event with deterministic all-time operator/feature/residual bounds, and actual dense GF existence. The finite-query argument at lines 350–361 explicitly allows singular covariances and applies to a fixed augmented witness list. The new proof never needs a width-independent complex-time radius.
- The real fitting proof uses the correct inverse-mobility norm and exact energy identity. Its stopped Gram bound, finite residual integral, hidden displacement estimates, and strict continuation margins support the uniform short-time bounds invoked in the addition.
- The Legendre proposition at lines 2401–2918 gives absolute error $CY/(\sqrt n[\log(en)]^3)\to0$, on the sphere at all times. The addition does not incorrectly replace this by $Y/n$.
- Harmonic and Taylor, at lines 4250–4491, provide absolute $Y/n\to0$ errors on their respective promised domains. Their proofs use the supplied source, selection, runtime comparison, and initialization-only compiler results. The candidate needs only these absolute errors and their eventual probability statements. It does not infer them from the relative variability ratio alone.
- Taylor allows arbitrary fixed passive inputs declared before initialization, includes only training samples in its deficit equation and Gram inverse, and retains the same source/runtime guarantees after input-span reduction. Thus the four additional witness inputs need neither passive labels nor extra optimization terms.

No prerequisite mismatch or new dependence on an unprovided paper section was found. The paper's other `\input` files are not imported to complete the proposed book proof: the needed compression results and proofs are present in the frozen book. This audit did not identify a pre-existing Chapter 9 issue affecting the addition. It does not claim a new theorem about optimal constants or numerical efficiency of the older constructions.

## Component verdicts and adversarial checks

### Initial geometry and nonlinear prediction velocity — PASS

Candidate lines 95–119 correctly use the Gaussian Hermite covariance expansion. For a positive marginal variance $q$, the function $u\mapsto\phi^{(\ell)}(\sqrt q\,u)$ is in Gaussian $L^2$. Finite Hermite support would make it a polynomial almost everywhere, then everywhere by continuity, and the bounded derivative would force that polynomial to be affine. Nonaffineness therefore gives unbounded positive support in the covariance series. The stated transform argument proves the required Hermite completeness, and the generating-function identity gives the covariance coefficients.

Composition preserves nonnegative coefficients and summability. It also preserves unbounded support: an inner coefficient of positive degree $j\ge1$, combined with an arbitrarily large positive outer degree $k$, contributes positively at degree $jk$. Positive marginal variance follows inductively from a nonconstant activation of a nondegenerate Gaussian. This works with nonzero activation means.

For every integer degree, the tensor Gram $[(v_a^\top v_b)^k]$ is positive semidefinite. Along the unbounded positive coefficient support it converges to $I_m$, since all off-diagonal correlations have absolute value strictly below one. Consequently every hidden feature Gram is strictly positive definite, even when the input Gram is singular.

I specifically checked the parity attack. An even activation may have only even Hermite degrees, and an odd activation may have only odd degrees. Neither defeats the convergence to $I_m$; no even/odd balance or positive coefficient at degree one is needed. For example, cosine has covariance $e^{-q}\cosh(c)$ at covariance $c$, so it supplies a concrete even-only, noncentered case. The exclusion of parallel and antiparallel sample pairs is doing real work here.

The projection formula at lines 121–143 is correct. Applying the affine projection in both variables to the tensor-feature kernel leaves exactly

\[
R_k(v,u)=(v^\top u)^k-a_k-b_kv^\top u.
\]

It is positive semidefinite because it is the Gram kernel of the projected tensor features. Both removed coefficients tend to zero for $d\ge2$, so the sample Gram of $R_k$ tends to $I_m$. The assumption $m\ge2$ together with nonparallel inputs rules out $d=1$. Thus no nonzero label vector can cancel all nonlinear degrees: the label contraction is a sum of nonnegative terms and has at least one strictly positive term.

The great-circle argument is valid in every permitted dimension. If every restriction were affine, its even antipodal part would be constant: any two sphere points share a plane. The homogeneous extension of the remaining odd part would be linear on every plane, hence additive and homogeneous on the full space. This contradicts nonaffinity. Three distinct points on the witnessing circle determine its affine restriction, and a failing fourth point supplies an affine-annihilating linear combination. Normalizing the absolute coefficient sum to one gives the exact norm bound used later.

The witnesses may depend on the fixed training labels through the limiting velocity. That is permitted: they are deterministic before initialization, and no labels for these passive inputs are requested. There is no claim of a label-blind universal witness panel.

### Initial backward fields and positive hidden forces — PASS

At initialization, let $k=2/m$, and let $P_a^{(\ell)}$, $B_a^{(\ell)}$ be exactly the pre-gated and gated vectors defined at candidate lines 179–182. Differentiating the actual GF with zero initial hidden velocities gives

\[
\dot\delta_a^{(\ell)}(0)=kB_a^{(\ell)},\qquad
\ddot W^{(1)}(0)=k^2\sum_a y_aB_a^{(1)}v_a^\top,
\quad
\ddot W^{(\ell)}(0)=\frac{k^2}{n}\sum_a y_aB_a^{(\ell)}h_a^{(\ell-1)\top}.
\]

The signs and all factors of $n,m$ agree with the maintained flow.

I checked the potentially dangerous conditioning step rather than treating reverse queries as independent matrix products. Given $WH=Z$, the regression term is $Z(H^\top H)^{-1}H^\top$, and the residual is a fresh Gaussian matrix acting on $I-\Pi_H$. Hence the reverse answer has mean $H Q_n^{-1}C_n$ and residual $(I-\Pi_H)\Xi D_n^{1/2}$, with the exact definitions in the candidate. No regression/response term has been discarded.

The adaptive ordering is sufficient. In the forward pass each query depends on previous answers. In the reverse pass the query for a matrix uses the forward transcript and higher-matrix reverse answers; these reveal no further part of that matrix's residual. Thus the relevant residual is still fresh conditional on the information used to form the query. The assertion would be false for an arbitrary query depending on that unrevealed residual, but the computation here does not make such a query.

The removed projection has expected squared Frobenius norm divided by $n$ equal to $\operatorname{rank}(H)\operatorname{tr}(D_n)/n$. Since the number of training queries is fixed and $D_n$ is tight, it vanishes in probability. The text correctly invokes tightness before conditional Markov.

The empirical $\mathcal W_2$ induction is adequate. Appending independent Gaussian rows preserves empirical weak convergence by conditional variance bounds and preserves second moments by the law of large numbers. For a continuous map of at most linear growth, an $L^2$ coupling plus uniform integrability gives convergence of the transformed second moments as well as weak convergence. Bounded derivatives make $\phi'(z)u$ such a map; bounded activation values are unnecessary. Products such as $Z^\top U/n$ then converge because they have quadratic growth. Vanishing RMS perturbations preserve the limit. The argument starts from the full first-layer Gaussian rows, so it retains their joint law with the first-layer acceleration rather than just a preactivation marginal.

All inverted limiting Grams are $Q^{(\ell)}$ with $\ell\ge1$; $Q^{(0)}$ is never inverted. Top backward-Gram positivity uses full support from $L\ge2$ and $Q^{(L-1)}\succ0$. If the displayed product of two analytic functions vanishes everywhere and the label-feature factor is nonzero somewhere, the derivative factor vanishes on an open set and hence everywhere. Varying one coordinate and using nonconstant $\phi'$ forces each coefficient to be zero. At lower layers, the conditional variance of the independent reverse innovation gives exactly the stated positive lower bound. The mean term cannot cancel a conditional variance.

Finally, for $Q\succeq0$, $D\succ0$, the Schur-product bound

\[
Q\circ D\succeq\lambda_{\min}(D)\operatorname{diag}(Q)
\]

follows by decomposing $Q$ into rank-one terms and applying the lower bound on $D$ to each diagonal conjugation. Positive diagonals suffice, so this step also survives singular $Q^{(0)}$. Each hidden acceleration energy therefore has a positive deterministic limit.

### Actual trajectory remainders and hidden feature motion — PASS

The real bounds in candidate lines 299–319 follow from the fitting event without assuming a uniform bound on individual initialized neurons. The readout and backward RMS are $O(t)$; hidden parameter increments in the inverse-mobility norm and all forward RMS increments are $O(t^2)$, uniformly over the sphere. The predictor expansion has a deterministic, width-independent $O(t^2)$ remainder on that event.

The key multiplier estimate is correct and addresses the lack of coordinatewise uniform continuity at growing width. Split the initial field $u$ at a fixed cutoff $D$; its low part is bounded using the Lipschitz gate and the forward RMS increment, and its high part uses the bounded gate and the initial squared tail. Empirical second-moment convergence permits choosing $D$ with a strict tail margin before choosing a small deterministic time. This proves the stated $o_*$ estimate uniformly on the small interval, including along every activation integration segment. No unproved fourth-moment control of the evolving fields is being used.

Downward backward subtraction only involves bounded operators, their $O(t^2)$ increments, propagated error, and the controlled gate difference acting on the initial pre-gated field. Integration of the actual updates consequently proves the hidden parameter expansion in the stated norm. The normalized outer-product identities in lines 360–361 are exact.

The adjoint pairing avoids a stronger forward-vector Taylor expansion that the proof has not established. Define

\[
E_{1,n}=\frac{\|\ddot W^{(1)}(0)\|_F^2}{n},\qquad
E_{\ell,n}=\|\ddot W^{(\ell)}(0)\|_F^2\quad(\ell\ge2).
\]

Pairing the increment of layer $\ell$ with its initial $P_a^{(\ell)}$ transfers the propagated term to the layer below and yields

\[
\sum_a y_a\frac{P_a^{(\ell)\top}[h_a^{(\ell)}(t)-h_a^{(\ell)}(0)]}{n}
=\frac{t^2}{2k^2}\sum_{j\le\ell}E_{j,n}+o_*(t^2).
\]

The omitted matrix-times-feature cross increment is $O(t^4)$ in RMS. Positive limiting energies and the bounded initial adjoint second moments turn this pairing into the asserted $t^2$ lower bound by Cauchy–Schwarz, for every hidden layer. Contributions from different layers cannot cancel in this test.

The definition of $o_*$ is sufficiently strong for the proof's use: finite sums, multiplication by uniformly bounded quantities, and time integration preserve the needed estimates. For example, a bound by $\varepsilon s^2$ uniformly for $s\le T$ integrates to at most $\varepsilon t^3/3$. The selection of cutoff, time, and then width has the correct order.

### Cubic separation from the frozen kernel — PASS

The training tangent matrix in lines 406–416 is the one generated by the stated loss and mobilities. Its initial hidden terms vanish. The readout part contracted against $y$ contributes $t^2\sum_\ell E_{\ell,n}/k^2+o_*(t^2)$, by twice the top adjoint pairing. The hidden terms contribute the same amount, because the backward vectors are $ktB_a^{(\ell)}+o_*(t)$. Thus

\[
y^\top[K(t)-K(0)]y=\frac{2t^2}{k^2}\sum_\ell E_{\ell,n}+o_*(t^2).
\]

The variation-of-constants expression is exact. Replacing its exponential by the identity and its deficit by $y$ makes only an $O(t^4)$ error, since $K(t)-K(0)=O(t^2)$ and $f_n(t)=O(t)$. Integration gives $2/(3k)=m/3$, confirming the coefficient and positive sign in the candidate. Dividing the label contraction by $\|y\|_1>0$ gives a training-input prediction gap. The coefficient has the correct label scaling: hidden acceleration is quadratic in $y$, its energy is quartic, and the resulting prediction gap has cubic label scale.

The explicit passive-input frozen flow in lines 10–16 is correctly normalized and is precisely the coupled dense initialization's readout-only flow. The theorem excludes this comparator, not every possible kernel model.

### Nonlinear part of the first-layer increment — PASS

The nonparallel-input assumption gives $\dim V\ge2$, where $V$ is the span of the training inputs. For nonzero $g,r\in V$, suppose $\phi'(g^\top v)(r^\top v)$ were affine on the unit sphere of $V$. Its values on the equator $r^\perp$ and their antipodes force the constant term to be zero and the linear coefficient to be parallel to $r$. Away from the equator, division then forces $\phi'(g^\top v)$ to be constant. Continuity covers the equator and the endpoints of the interval $[-\|g\|,\|g\|]$. Analyticity would then make the activation affine everywhere, a contradiction. This includes the potentially delicate two-dimensional and $g\parallel r$ cases.

The limiting projected first-layer Gaussian row is nonzero almost surely. Positive acceleration energy gives positive probability of nonzero $r$, without requiring independence between $g$ and $r$. The squared distance from affine functions is continuous in $(g,r)$, bounded by $\|\phi'\|_\infty^2\|r\|^2$, and strictly positive on their joint nonzero event. Empirical $\mathcal W_2$ convergence therefore gives a positive deterministic mean limit.

The actual increment is compared with the direction $t^2r_i/2$. The stated low-tail Taylor bound has the correct factor $1/8$; on the high tail bounded $\phi'$ gives the displayed linear bound in $\|r_i\|$. Choosing a cutoff first and time second gives the claimed $o_*(t^2)$ error in neuron-index-times-sphere $L^2$. Contractivity of the affine projection transfers positivity to the actual squared increment, of order $t^4$. The proof establishes this for the dense reference only, as the theorem states.

### Transfer, quantifiers, storage, and interpretation — PASS

The four-point combination annihilates every affine function $a^\top x+b$, including an affine function selected after seeing initialization or time. Its absolute coefficient sum is one, so the positive dense witness bounds the infimum over all such functions. Vanishing absolute compression error transfers both this lower bound and the frozen-kernel gap for each fixed positive time. The constants can be chosen jointly for the finitely many layers and constructions by taking smaller positive minima.

The candidate explicitly fixes time before the width limit. It does not infer a compressed lower bound along arbitrary $t_n\downarrow0$, for which absolute error alone would be insufficient. Nor does it assert a gap at a fitted endpoint. Eventual estimates at every fixed confidence do imply convergence in probability for these absolute errors.

For Taylor, adding at most four deterministic witnesses replaces $m+p$ by at most $m+p+4\le3(m+p)$. Its quadratic panel factor increases by at most nine and its linear data factor by at most three. No proof term silently changes the number of training samples, the loss normalization, or a Gram inverse. Legendre and Harmonic already cover the witnesses.

The conclusions distinguish three different facts correctly: the compressed predictors are nonaffine; they differ from the particular dense frozen-kernel comparator; and the dense hidden features, including a nonlinear first-layer component, move. Predictor closeness does not identify compressed state coordinates with dense neurons, and the text explicitly disclaims such an identification. There is no test-risk, endpoint, trained-population-limit, efficient-compilation, finite-precision, or raw-GD claim.

## Paper fidelity and canonical notation

The correspondence with the paper is exact: paper $w$ becomes $W^{(L+1)}$, paper $\phi_\ell$ becomes $\phi^{(\ell)}$, and paper normalized pairings $\langle u,v\rangle_n$ are displayed as $u^\top v/n$. The hidden inverse-mobility norm becomes the established parameter norm with zero readout component. The model's residual sign, mean-square loss, mobilities, initial zero readout, and physical time are preserved. All four paper supporting lemmas and the final transfer proof are present, with added clarifications of full-rank events, adaptive-query ordering, projection tightness, and fixed-time scope.

The candidate is self-contained relative to the frozen maintained chapter. It does not silently use a paper-private coefficient or proof. One optional editorial clarification would be to identify the Hermite paragraph's local variance explicitly as $q=F_{\ell-1}(1)>0$. Its intended value follows from the immediately preceding covariance recursion, so this is not a mathematical gap or a required scientific repair.

## Reproducible diagnostic attacks

I created only study-owned scratch at `data/generated/nonlinear_feature_learning_certificate_20261010/review_a/audit_checks.py`. The script uses NumPy 1.26.4 and SciPy 1.13.0, takes no network inputs, and does not modify the packet. Commands run included:

```text
wc -l data/generated/nonlinear_feature_learning_certificate_20261010/promotion_v1/review_inputs/*
sha256sum data/generated/nonlinear_feature_learning_certificate_20261010/promotion_v1/review_inputs/*
python -c 'import numpy, scipy; print("numpy", numpy.__version__); print("scipy", scipy.__version__)'
python data/generated/nonlinear_feature_learning_certificate_20261010/review_a/audit_checks.py
```

The complete source reads used `cat` and the contiguous `nl -ba ... | sed -n ...` ranges recorded above. The diagnostic script additionally checks the nine manifest hashes, reconstructs the assembled chapter in memory and checks its hash, resolves all candidate theorem/lemma/proposition/equation references, and checks explicit-ID uniqueness. All those assertions passed.

For actual GF diagnostics, the script uses $n=24,m=3,d=2,L=3$, normalized input angles $0,0.7,1.8$, and a deterministic Gaussian seed. The input Gram eigenvalues are approximately $(-5.7\times10^{-17},1.1961023,1.8038977)$; its mathematical rank is two and all distinct-pair absolute correlations are below one. Thus it exercises correlated, rank-deficient input data. Activations are $\tanh z$, $\cos z$, $\sqrt{1+z^2}$, and $z+0.3\tanh z$, covering bounded/unbounded and even/odd cases. Each has the required strip regularity for some positive strip width.

The diagnostic uses moderate labels $(0.6,-0.3,0.4)$ to resolve the cubic difference numerically. These labels are deliberately outside the extremely small global fitting cap. Therefore the numerical checks test finite-width local algebra and actual short-time GF, not the theorem's asymptotic probability or global compression guarantee. The proof audit above is what establishes applicability under the stated cap.

The script independently propagates the exact feature accelerations and checks the telescoping adjoint coefficient, then integrates the actual weight ODE with DOP853. It compares the output with the matrix-exponential frozen flow and projects actual first-layer increments off constant/cosine/sine functions on a 1,024-point circle grid. At $t=0.002$:

| Activation | Cubic gap / predicted cubic term | Nonlinear squared increment / predicted leading term |
|---|---:|---:|
| $\tanh z$ | 0.999380 | 0.999433 |
| $\cos z$ | 0.996327 | 0.996904 |
| $\sqrt{1+z^2}$ | 0.972004 | 0.973840 |
| $z+0.3\tanh z$ | 0.987045 | 0.986303 |

The ratios move toward one as time decreases through $0.016,0.008,0.004,0.002$. The maximal normalized error in the independent exact adjoint-acceleration identity was below $6.8\times10^{-17}$. Every tested hidden acceleration energy and every projected first-layer acceleration mean-square was strictly positive. These checks found no sign, factor-of-two, mobility, or width-normalization error.

The conditioning diagnostic uses $n=64,m=3$ and the forward-answer-dependent reverse query $U=\cos Z+0.2Z$. It verifies the regression normalization and samples 4,000 Gaussian innovations. The removed projection's mean squared Frobenius norm divided by $n$ was 0.08770015, compared with the exact rank–trace prediction 0.08818092, a ratio of 0.994548. The conditional law and the vanishing projection argument were proved analytically in the audit; this numerical check merely tests their normalization.

The command exited with status zero and `ALL DIAGNOSTIC ASSERTIONS PASSED`.

## Required corrections and unresolved objections

There are no required scientific corrections and no unresolved scientific objections to the frozen candidate. The known Quarto anchor/div spacing defect is an operational formatting repair, and the optional local declaration of the Hermite variance is editorial. Neither changes the scientific verdict. No frozen scientific input was silently repaired.

**Final verdict: PASS for scientific promotion of this complete addition, subject to the repository's separate formatting, promotion, and user-approval process.**
