# Complete isolated scientific review A: frozen promotion v1

**Verdict: PASS.** I found no required scientific correction, missing mathematical dependency, or unresolved correctness objection in the frozen candidate. This verdict covers the stated local, deep-linear, literal-array result and its proofs. It is not an integration, placement, rendering, numerical-implementation, or whole-book review, and does not authorize promotion by itself.

## Identity, isolation, inputs, and complete coverage

Reviewer: `/root/nth_science_review_a`, distinct from the originating-study authors, `/root`, `/root/nth_compact_assembly`, and selector `/root/nth_selector_current`. I started from the neutral assignment without inherited research discussion. I did not read the study README, original research reports, selector report, earlier verdicts, another reviewer’s work, another study, or archived book material. I launched no subagent and retrieved no external scientific material.

I read the complete neutral assignment at `studies/nth_lower_bound_20261010/PROMOTION_REVIEW_ASSIGNMENT.md`. I read `AGENTS.md`, the complete `RESEARCH_WORKFLOW.md` including all of Part 2, `/etc/codex/skills/solve-math-rigorously/SKILL.md`, `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`, and its complete `references/neural-response-memory.md`. These were process/presentation inputs, not additional scientific sources.

Scientific inputs were exactly the following frozen files under `data/generated/nth_lower_bound_20261010/promotion_v1/`:

| File | Complete read coverage | SHA-256 |
|---|---:|---|
| `candidate.qmd` | Lines 1–566, read in ranges 1–190, 191–380, 381–566; no truncated range | `63b519b86f65e519b09d0f399ad7942ea81608b91968a87d6dee2c8a8997f5b2` |
| `notation.qmd` | All 98 lines | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `references.bib` | All 11 lines | `7b7a4a33db9309b9ecb91c3f058236af8c855e7b7470fbd107809140d19b35a9` |

The candidate hash matches the supplied assignment. The bibliography supplies attribution only; no conclusion below imports an approximation theorem from the cited paper. No scientific input was missing. Metadata-only Git checks recorded HEAD `c17cb8c2e8d486ccc1d2b80e8cd173ba551145ae` and confirmed that my assigned report and scratch paths were unused before writing. I neither staged nor committed anything and did not edit the frozen packet or maintained book.

## Component verdicts

| Component | Verdict | Reason |
|---|---|---|
| Model, normalization, loss, and physical clock | PASS | The change of variables makes the stated mobilities exactly Euclidean gradient flow; the factor-two time conversion is correct. |
| Ordered hierarchy, initialization, residual, and passive queries | PASS | The reconstruction has the required ordering and reproduces the specified autonomous finite closure with its own residual. |
| All-order derivative bounds and reflection parity | PASS | The leaf count is dimension-free and the odd-rank zero initialization follows from the stated reflection. |
| Common analytic disk and real-interval convergence | PASS | The Picard and fixed-point constants are below one, uniformly in order; the dense remainder tends to zero. |
| First omitted coefficient with feedback | PASS | Feedback gains an additional time integration and cannot change that coefficient. |
| Nonzero coefficients at every effective order | PASS | The source-ascent invariant and coefficientwise comparison give the claimed simultaneous lower bound. |
| Transfer from a derivative to real-interval error | PASS | The Chebyshev derivative estimate, Taylor tail, and all constants have the required direction. |
| Gaussian matrix event and entropy concentration derivation | PASS | The net, Gaussian integral, semigroup calculation, extension, and uniformization are sufficient. |
| Actual dense-pair upper and lower bounds | PASS | Both concern the specified independent dense copies; the small-ball event is not conditioned incorrectly. |
| Degenerate cases, quantifiers, and probabilities | PASS | Zero forcing, small dimensions, uniform sample ranges, deterministic data, and adaptive order budgets are handled. |
| Literal moving/frozen storage and minimum-order implication | PASS | Counts and asymptotic conversion follow from the representation actually defined. |
| Claim scope and dependencies | PASS | No compression theorem, alternative initialization, factored encoding, numerical evidence, or longer-time claim is used. |

## Proof reconstruction and adversarial checks

### 1. Normalization and the exact finite closure

Under `B=W^(1)/sqrt(n)` and `c=W^(3)/sqrt(n)`, the prediction is exactly `cᵀWBv`. The first and last block changes divide the stored-weight velocities by `sqrt(n)` and divide the corresponding gradients by the same factor, so their mobility `n` cancels. The middle block already has unit mobility. For half-MSE the prediction coefficient is `w=BᵀWᵀc`, the negative residual source is `b-Qw`, and the three displayed dense equations follow directly. Full-MSE doubles every velocity, hence its time `t` equals half-MSE time `2t`.

The source `V(v)` is the Euclidean/Frobenius gradient with precisely these normalized variables. Its dependence on `v` is linear. Recursive differentiation therefore leaves each input slot separately linear. The definition need not, and does not, impose permutation symmetry.

For a prescribed coefficient path `z`, put `u_a=(y_a-v_aᵀz)/m`. Repeated integration of the rank equations places the first appended input at the outer, latest integration time. Differentiating the displayed reconstruction at that outer time gives

\[
\frac{d}{dt}K_r^{(q)}(\mathbf v;t)
=\sum_a u_a(t)K_{r+1}^{(q)}(\mathbf v,v_a;t).
\]

Its top rank has only the zero-length integral and is frozen. At rank one, summing each source slot replaces `sum_a u_a v_a` by `b-Qz`; consequently the rank-one equation is precisely the finite fixed-point map. A fixed point thus generates the full initialized arrays, rather than merely a proposed prediction formula. Polynomial ODE uniqueness identifies these arrays with the requested closure. In particular no dense residual has been substituted for the closure residual.

The coordinate query rows have no role in the training sum. Linearity of initialization and of each evolution equation preserves the decoder `vᵀw_q`. The sphere error is therefore the Euclidean norm of the coefficient difference, and later queries require no additional query-labelled dynamics.

### 2. Dimension-free derivatives, analytic existence, and remainder

A scalar network monomial begins with three parameter leaves. One source differentiation replaces exactly one leaf by the corresponding quadratic source block. After `k` differentiations there are at most `3·4·…·(k+2)=(k+2)!/2` terms and `k+3` leaves. These expressions are chains, outer products, and scalar contractions with explicit input vectors. Replacing a matrix leaf by a rank-one source does not introduce a free identity contraction or a trace proportional to dimension. Operator and vector norms consequently give the displayed bound on every term. Substitution of block radius four yields the stated factor `32·4^k(k+2)!`.

For readout reflection `J`, differentiation of `K_r∘J=(-1)^r K_r` and use of `V(Jθ)=-JV(θ)` give `K_(r+1)∘J=(-1)^(r+1)K_(r+1)`. Since the initial point is fixed by `J`, every odd initialized rank vanishes.

On the complex path ball of radius one about the initial point, all block norms are at most five. Ordinary transpose has the same operator norm over complex coordinates, and the polynomial formulas extend without conjugation. The velocity bound is `25·126=3150`; its derivative in the maximum block norm is at most `2·5·126+25·75=3135`. Multiplication by `R0=2^-12` makes both quantities less than one. Picard integration thus supplies the holomorphic dense solution. Differentiating `w` gives three terms, each bounded by `625(||b||+||w||)`, and radial Gronwall gives the stated `exp(1875|t|)-1` estimate.

The simplex-volume division by `k!` converts the tensor bound into the two series used for the finite and infinite maps. At `8R0=1/512`, the self-map bound is approximately `0.3764696261` and the Lipschitz bound approximately `0.1889720243`. At `8T=1/4096`, the real self-map factor is approximately `0.0468978975`, below `1/16`, and the Lipschitz constant is approximately `0.0234604022`, below `1/32`. These constants hold for all finite orders as well as the infinite map.

In the dense repeated-integration remainder, earlier source vectors are fixed arguments while the parameter state is differentiated. The last tensor is evaluated at the innermost time. With block radius five and source norm at most `2||b||`, the remainder is bounded by

\[
\frac{125}{2}(N+1)(N+2)(10\|b\|T)^N,
\]

which converges to zero. Thus the infinite fixed point is the actual dense trajectory, not just a formal series.

Parity makes `j=2 floor(q/2)+1` the first potentially omitted power. The tail estimate follows from the displayed elementary inequality in `j` and the geometric series for `(ℓ+1)^2`. Its fixed-point amplification is less than two; numerically the bound used is about `1.0250245882`. Finally `(j+1)(j+2)≤4^j`, `||b||≤1`, and `j≥q` give the stated `64||b||1024^-q` error. The separate zero-forcing argument avoids division by `||b||`.

### 3. The omitted coefficient retains the model’s own feedback

The hard data have `G=(I+11ᵀ)/2`, `||bar v||²=1/8+1/(2m)`, label mean `Y/2`, label RMS `Y`, and variance `3Y²/4`. The feature-Gram observation is consistent with identity activations and the initialization covariance; no evolved-Gram preservation is required by the proof.

An odd top is zero, so orders `2k` and `2k+1` have the same prediction map. Write `h=2 floor(q/2)`, `j=h+1`, and `e=w-w_h`. The omitted source series evaluated on `w` begins with

\[
\frac{t^j}{j!}K_{j+1}(v,b,\ldots,b;0).
\]

If `e=O(t^ℓ)`, the difference of the two finite maps contains one factor `-Qe` and at least one integration, and hence is `O(t^(ℓ+1))`. Starting from `e(0)=0` and iterating proves `e=O(t^j)` and moves the feedback correction to order `j+1`. Contracting the first slot with `bar v` and using `b=Y bar v` proves the exact leading derivative formula. This establishes the all-order feedback assertion, rather than assuming it from a source-only Taylor expansion.

For the positivity argument, `ξ=Bv_*`, source time `τ=λs`, and `a=W0ξ0` give

\[
c''=(A_0I+W_0W_0^\top)c+2(c^\top c)c,
\qquad A_0=\|\xi_0\|^2,\quad c(0)=0,\quad c'(0)=a.
\]

I checked both invariants used to derive this equation by differentiation. Diagonalizing its positive semidefinite linear part and choosing the eigenvector signs makes `a` nonnegative. Successive Taylor coefficients are then nonnegative, and comparison with `a u`, where `u''=A0 u+2H u³` and `H=||a||²`, is valid coefficient by coefficient, including coordinates with `a_i=0`.

On `A0,H≥1/2`, the comparison with `2 tan(τ/2)` is valid because this latter function satisfies `u''=u/2+u³/8`. The tangent recurrence gives `t_k≥3^-k`: the inductive lower bound reduces to `3k≥2k+1` for `k≥1`. It follows that `u≥τ/(1-τ²/12)` coefficientwise. The degree `j=2k+1` coefficient of `cᵀc'` is therefore at least `H(k+1)²12^-k`, which exceeds `8^-j`. Returning to the original output and clock contributes `λ^(j+1)`. Since `λ≥2^-3/2`, this gives the claimed `j!64^-j` bound.

The Gaussian norm ratios for `ξ0` and `W0ξ0` have independent chi-square laws because the conditional law of the second ratio is independent of the conditioning vector. Requiring each ratio to exceed `3/4` makes both `A0` and `H` exceed `1/2`. Their exponential lower-tail bound and the matrix event are independent of closure order. Thus the coefficient conclusion genuinely holds for every order on one event; there is no hidden union over infinitely many orders.

### 4. Analytic transfer on the real interval

The Chebyshev endpoint formula has denominator `1·3·…·(2j-1)≥j!`, giving the stated polynomial derivative estimate after rescaling the interval by `8/R`. The degree-`N` Taylor tail on `[0,R/4]` is at most `(2/3)4^-N`. Combining the polynomial derivative lower bound and the tail gives exactly

\[
\|g\|_{[0,R/4]}
\ge \frac{\vartheta^j(j!)^2}{2N^{2j+1}}-\frac23 4^{-N}.
\]

I checked the logarithmic tail comparison with `N=ceil(κj)`: the displayed expression is bounded by `j[u+v+3log(2κ)+3]`, then by `15jD`, which is less than `κj log 4`. The final use of `N≤2κj`, `j!≥(j/e)^j`, and `j≤2^j` yields precisely the denominator `8e²κ²` and prefactor `1/(8κ)`. These estimates work also for `j=1` and arbitrarily small positive `ρ` satisfying the lemma’s condition.

The application takes `R=R0/2`, so the dense and finite coefficient paths are holomorphic on a neighborhood of the closed transfer disk. The bound two is valid for the signed difference because `||bar v||≤1`. Since `R/4=T`, the resulting real interval is the interval in the error definition. The claimed exponential lower error is therefore a trajectory statement, not an inference from a formal jet alone.

### 5. Gaussian concentration, including its supplied proof

The sphere packing gives a `1/4` net of size at most `9^d`; approximating the maximizing unit vector gives the factor `4/3`. At chi-square exponential parameter `4/9`, the threshold `9n` gives `e^-4n 9^(n/2)`. The union bound with `d≤n` yields `exp[-(4-(3/2)log 9)n]` per matrix, as stated.

The entropy derivation is complete in the specialization used. The Gaussian integration-by-parts identity for the Ornstein–Uhlenbeck generator and invariance of Gaussian measure give the negative entropy derivative. The gradient intertwining identity and weighted Cauchy–Schwarz give

\[
\frac{|\nabla P_s h|^2}{P_s h}
\le e^{-2s}P_s\left(\frac{|\nabla h|^2}{h}\right).
\]

For the bounded positive smooth class, dominated convergence makes the terminal entropy zero. Integrating in `s` gives the factor `1/2` in the entropy inequality. Substitution of `h=exp(λF)` then gives `λψ'-ψ≤λ²L²/2`. Integration from zero, whose endpoint is `E F`, gives the centered logarithmic moment bound. Optimizing Markov’s inequality and treating `-F` yields the two-sided tail. Value truncation and convolution preserve the Lipschitz constant, while `|F(x)|≤|F(0)|+L|x|` supplies Gaussian-integrable exponential domination. Thus the extension to the unbounded Lipschitz maps actually used is justified; `L=0` is separately constant.

For good initial conditions, expanding the three velocities gives coefficients `630` for each of the two direct factor changes and `625` for each residual-induced change. Each block difference is at most `1255` times the sum norm and their sum has factor `3765`. The initial sum of two Frobenius differences is at most `sqrt(2)` times the Euclidean entry norm, so `50 exp(4000T)` safely bounds every scalar-query Lipschitz constant. This compares two trajectories directly and does not require the good initial-condition set to be convex.

The infimum extension agrees with the original map on the good set and preserves its Lipschitz constant. Identically distributed independent copies of that extension have the same expectation; deviations from that common expectation give the stated pair estimate. Applying this separately at every fixed time/query in the finite grid and net is legitimate. The grid size and mesh, sphere-net factor two, and pair time-Lipschitz bound give `4s+500000/n`. Taking `δ=1/n` yields the displayed hard-family dense-pair upper bound. The probability loss for the four initial matrices is included.

### 6. Dense-pair anti-concentration and zero cases

At initialization `f'(0,v_*)=||b||H`, with `H=UV` for independent normalized chi-square variables. For `n≥4`, the density’s mode is at least `1/2`. Its logarithmic curvature is bounded below by `-2n` on the interval used, implying density at least `e^-1` times its maximum over an interval of length `n^-1/2`; normalization yields `||p||∞≤e sqrt(n)`. Direct integration of the gamma density gives `E[V^-1]=n/(n-2)≤2`. The product density is bounded by `2e sqrt(n)` and convolution with the reflected second-copy density preserves this bound. Consequently

\[
\Pr\{|H-\widetilde H|\le 1/n\}\le 4e/\sqrt n.
\]

This estimate is unconditional. Only afterward is it intersected with the matrix event, so there is no unjustified conditional density assertion.

On the common analytic disk, `|g|≤2||b||`. The specified circle of radius `R/2` centered at any `t∈[0,T]` is inside that disk, and Cauchy gives `|g''|≤2^30||b||`. At `t_n=1/(2^30n)`, the linear term has magnitude at least `||b||/(2^30n²)` and the second-order remainder costs at most half this amount. The lower bound is thus for the actual dense trajectory discrepancy `D_n`.

If `b=0`, the dense initialization is stationary even when individual labels are nonzero. For the finite closure, the zero prediction path gives `sum_a u_av_a=b=0`; multilinearity makes every contraction vanish. All arrays can therefore remain at initialization and all predictions are zero. The event `E≤AD` then means `0≤0` without any ratio. The cases `m=1`, zero input vectors, zero labels, and singular `Q` introduce no division by a Gram eigenvalue. The stated probability can be negative at small allowed `n`; as a lower probability bound this is vacuous but correct, and the asymptotic theorem uses sufficiently large width.

### 7. Minimum order, storage, and probability quantifiers

For the general upper bound, the ratio of the two proved bounds is at most `2^37 n² 1024^-q`. The stated `q_n` makes this at most `1/n`. The anti-concentration probability is for each fixed deterministic dataset, not for all deterministic datasets on one event, exactly as disclosed. No small-label or data-independence condition beyond those in the setup has been added.

For the hard family, write `R_n=n/(m+log(en))`. The error lower bound and discrepancy upper bound hold together with probability tending to one uniformly over `4≤m≤sqrt(n)`. If `q≤log(R_n)/(4b_Y)`, then the error is at least `a_Y exp(-b_Y) R_n^-1/4`, whereas `D_n≤C R_n^-1/2`. For every fixed `A`, their ratio diverges uniformly. Thus each such order has success probability tending to zero, eventually below the fixed target `p`. The width threshold may depend on `p,A`; the exponent constants need only depend on `Y`, as claimed.

The rank counts are literal arrays with `m+d` first-slot choices and `m` choices for every further slot. Summing the geometric series gives the general upper counts, with the separately stated arithmetic sum when `m=1`. Query rows and training rows are both charged by this representation even though a different encoding could share information. Data storage is charged separately; coefficient generation, peak initialization memory, bit precision, and integration costs are explicitly excluded.

An even top is retained. With an odd zero top omitted, the preceding even rank still has to be retained. The proof’s conservative lower bounds `m^(q-1)` for retained training arrays and `m^(q-2)` for moving arrays remain valid, including the possibility of treating a constant penultimate rank as frozen. The necessary order proportional to `log R_n` therefore gives a size exponential in `log m log R_n`. On the allowed sample range, `log R_n` and `log n` are uniformly comparable. For the upper bound, `d=m+1` and the geometric count give at most `5m^q_n+md+m`, and `q_n=O(log n)`. A sufficiently large width makes both `1/n≤A` and the upper success probability at least `p`, so the set over which the minimum is taken is nonempty.

The lower event excludes all low orders simultaneously. Consequently an initialization-dependent choice of order, even with access to the observed initialization, cannot evade it under a deterministic budget that only permits those orders. This is a stronger quantifier than separate bounds for each fixed order, and the proof actually supplies it. The conclusion does not concern arbitrary encodings, removal of all algebraically redundant entries, or computational time. For `m=4 floor(n^a/4)`, `log m=a log n+o(log n)` gives the stated quadratic logarithm exponent. Fixed `m,d` instead give polynomial size.

## Executed deterministic attacks and evidence

The supplementary script is `data/generated/nth_lower_bound_20261010/promotion_review_a_v1/checks.py`; its complete output is `checks.log` in the same directory. It uses only the Python standard library. I ran:

```text
python data/generated/nth_lower_bound_20261010/promotion_review_a_v1/checks.py > data/generated/nth_lower_bound_20261010/promotion_review_a_v1/checks.log
```

The process exited with status zero. The attacks and results were:

1. **Exact own-feedback boundary model.** For scalar `B0=W0=1`, `c0=0`, `Q=b=1`, source ascent gives `c=tan(s)` and source output `F(s)=c c'`. Each truncation uses its own physical clock `s'=1-F_q(s)`. Exact rational Taylor arithmetic, through degree 19, compared dense and truncated physical predictions at every order `q=2,…,12`. The first differences appeared at `j=2 floor(q/2)+1` and equalled the omitted source coefficient exactly. The consecutive coefficient values were `4/3`, `17/15`, `248/315`, `1382/2835`, `43688/155925`, and `929569/6081075`. Every comparison passed, including the even/odd order pairing. This is a deterministic algebra check, not a claim about a positive-probability scalar initialization.
2. **Contraction and tail constants.** Direct evaluation produced the four constants recorded above and tail amplification `1.0250245882389597`; all have the strict margins required by the proof.
3. **Coefficient inequalities.** Exact integer/rational comparisons checked `(j+1)(j+2)≤4^j` and the bound from the source-ascent coefficient to `8^-j` for every odd `j=3,…,999`. All passed. The report separately supplies the all-order justification; this finite sweep does not replace it.
4. **Analytic-transfer boundary range.** Eighteen log-domain checks covered `ρ∈{1/64,10^-8,10^-100}` and `j∈{1,2,3,10,100,1000}`. The Taylor tail was below half the polynomial lower term in every case. The symbolic argument above covers the lemma’s entire range.
5. **Zero and scope attacks.** I checked zero forcing with nonzero labels, singular input covariance, one-sample counts, an odd zero frozen top, large orders, small positive fixed `Y`, a deterministic adaptive-order budget, and the distinction between per-dataset probability and simultaneous probability over datasets. None contradicts the claims as scoped.

These calculations test possible cancellation, parity, constant, and boundary failures. No Monte Carlo result, training experiment, or numerical approximation is used to establish the theorem.

## Required corrections, unresolved objections, and completion

**Required corrections: none. Unresolved scientific objections: none.**

The review is complete for every scientific line and every dependency in the assigned frozen packet. The report’s conclusion is confined to this packet and to its explicit half-MSE interval, initialization, deep-linear model, deterministic bounded data, actual independent dense-pair comparator, and literal real-coordinate representation. I have not inferred a nonlinear-network theorem, a longer-time bound, a finite-precision result, a universal encoding lower bound, or a same-family comparison with the compression construction.

Only this assigned report and the assigned generated scratch files were written. Frozen input hashes were rechecked at completion and were unchanged.

## Additional mechanical v1-to-v2 correspondence check

After completing the scientific review, the coordinator supplied a technical formatting notice: Quarto rejects the six combined proof-ID/class wrappers in v1, and v2 separates each identifier into an anchor preceding the proof division. No scientific feedback or other reviewer finding was supplied. The coordinator explicitly extended my scope to verify this formatting-only correspondence.

I read the complete 68-line `studies/nth_lower_bound_20261010/PROMOTION_FORMAT_v1_v2.diff` and mechanically compared the complete bytes of `promotion_v1/candidate.qmd` and `promotion_v2/candidate.qmd`. The v2 candidate SHA-256 is:

```text
e8c8cbd7474b9e0bbaded9100ce02474708339f9ac95cf606de7b93886616d23
```

Using Python `re.subn` in multiline byte mode, I replaced exactly six occurrences of

```text
::: {#proof-IDENTIFIER .proof}
```

with

```text
[]{#proof-IDENTIFIER}

::: {.proof}
```

The transformed v1 bytes equal the complete v2 bytes. Reversing exactly those six substitutions recovers the complete v1 bytes. Both equality assertions passed, with exit status zero. Thus all scientific text, formulas, statements, proofs, ordering, and references are unchanged. The scientific PASS applies to that unchanged content in v2 as well. This mechanical result does not independently certify Quarto rendering or v2 dependency assembly; those remain integration checks. No second proof reading was necessary or claimed.
