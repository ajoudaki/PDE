# Independent complete scientific promotion review B — frozen v1

**Overall verdict: PASS.** I found no required scientific correction and no unresolved mathematical objection in the frozen candidate. This is a scientific verdict on the stated literal-array, short-time, deep-linear result, not approval to integrate or a whole-book integration review.

## Inputs, read coverage, and isolation

I read the neutral assignment `PROMOTION_REVIEW_ASSIGNMENT.md`, the current `AGENTS.md`, all of Part 2 of `RESEARCH_WORKFLOW.md`, the complete `solve-math-rigorously` and `explain-with-canonical-notation` skills, and the latter's complete neural-network reference. I applied these skills in the proof audit and this report.

The only scientific inputs were the three frozen files under `data/generated/nth_lower_bound_20261010/promotion_v1/`. I read every scientific line: candidate lines 1–190, 191–380, and 381–566 in separate untruncated reads, all 98 lines of the notation contract, and all 11 lines of the bibliography. Their SHA-256 hashes are:

| Input | SHA-256 |
| --- | --- |
| `candidate.qmd` | `63b519b86f65e519b09d0f399ad7942ea81608b91968a87d6dee2c8a8997f5b2` |
| `notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `references.bib` | `7b7a4a33db9309b9ecb91c3f058236af8c855e7b7470fbd107809140d19b35a9` |

The candidate hash matches the assigned hash. The bibliography supplies attribution only; no approximation theorem from that citation is needed or imported. I did not fetch it or any additional scientific source.

I am reviewer `/root/nth_science_review_b`, distinct from the supplied author/assembler and selector identities. I read no study README, history, original reports, selector report, prior verdicts, other reviewer findings, other studies, current book beyond the frozen notation input, or archived book. I did not launch subagents. I had no inherited author scientific discussion. All calculations were reconstructed from the frozen candidate. Writes were confined to this report and the assigned scratch directory `data/generated/nth_lower_bound_20261010/promotion_review_b_v1/`; no frozen input or established material was edited. No Git mutation was performed.

## Component verdicts

| Component | Verdict | Main adversarial check |
| --- | --- | --- |
| Model, mobilities, normalization, loss clock | PASS | The rescaled flow is exactly Euclidean gradient flow; the full-MSE clock doubles the speed. |
| Ordered hierarchy, passive queries, initialization, top freezing | PASS | Reconstructed the arrays and their own residual; exact noncommuting-source check confirms the slot order. |
| All-order leaf bound and parity | PASS | Directional differentiation introduces no dimension-dependent free trace; odd initialized ranks vanish. |
| Analytic existence, source remainder, geometric upper error | PASS | Verified disk, contraction, remainder, and tail constants, uniformly in finite order. |
| Nonzero omitted derivative | PASS | Reconstructed feedback cancellation and the positive-coefficient comparison for every effective order. |
| Analytic transfer to the real interval | PASS | Checked the endpoint polynomial derivative bound, Taylor tail, and all constants. |
| Gaussian norm and concentration estimates | PASS | Verified the net argument, scalar extension, dimension scaling, and time discretization. |
| Actual dense-pair anti-concentration | PASS | Verified the product density and the deterministic conversion from initial slope to path discrepancy. |
| Zero cases, probabilities, growing dimensions, uniformity | PASS | The zero-b case, small dimensions, parity, fixed success/accuracy parameters, and quantifiers are consistent. |
| Necessary/sufficient order and literal storage | PASS | The same-event lower bound excludes all affordable orders; moving and frozen counts have the claimed asymptotic order. |

## Proof reconstruction and attacks

### 1. Exact model and autonomous closure

The variables have the types stated in the candidate: \(B\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\), \(c\in\mathbb R^n\), and \(w=B^\top W^\top c\in\mathbb R^d\). The prediction is \(f_n(v)=v^\top w\), with residual \(f_n(v_a)-y_a\). From \(W^{(1)}=\sqrt n B\) and \(W^{(3)}=\sqrt n c\), the original block mobilities \(n,1,n\) become unit mobilities in these variables. Thus differentiating the half-MSE gives exactly the three displayed dense equations with driving vector \(b-Qw\). Replacing half-MSE by full-MSE multiplies every velocity by two, so the candidate's time statement is correct.

The data assumptions imply \(\|Q\|_{\rm op}\le1\) and \(\|b\|_2\le1\), with no invertibility assumption. Each tensor is linear in each input slot because both the prediction and source field are linear in the queried input, and the recursion differentiates only parameters. Along any fixed source path \(a(t)\), differentiation of a tensor appends \(a(t)\) in its last slot. Consequently, repeated integration puts the first appended slot at the latest time. For a fixed order, differentiating the reconstruction's outer limit produces

\[
\sum_a u_a(t)K_{r+1}^{(q)}(\mathbf v,v_a;t),
\qquad u_a(t)=\frac{y_a-v_a^\top z(t)}m.
\]

Setting \(z=\mathcal F_q[z]\) gives precisely the prescribed residual from that same closure. The term with zero integrations supplies exact initialization, and rank \(q\) has only that term and is frozen. Thus the reconstruction is a solution of the actual finite polynomial ODE. Local uniqueness identifies it with that ODE, rather than with a hierarchy driven by the dense residual.

The same first-slot linearity shows that the training predictions equal \(v_a^\top w_q\), while stored coordinate queries recover \(w_q\) and hence every later query. Passive queries supply no additional residual or labels. There is no need to retain dense matrices once the coefficient arrays have been initialized. The proof's \(Q,b\) are analysis summaries; the implemented literal hierarchy can use the stated retained dataset directly.

### 2. Dimension-free tensor control, parity, and existence

After \(k\) source derivatives, the scalar polynomial contains \(k+3\) parameter leaves. At the next derivative one of those leaves is replaced by a quadratic source expression. Starting with one term gives at most \(3\cdot4\cdots(k+2)=(k+2)!/2\) terms. Differentiating a matrix leaf inserts a rank-one outer product; differentiating a vector leaf inserts a matrix chain ending in an input vector. The resulting scalar products retain vector endpoints, so this process creates no unrestricted trace contraction. Operator/vector norm products therefore bound each term without a factor of \(n\) or \(d\). Substitution of block radius four gives the factor \(32\,4^k(k+2)!\).

For readout reflection \(J\), the source satisfies \(V(v;J\theta)=-JV(v;\theta)\). Applying the chain rule to the tensor recursion gives \(K_r(J\theta)=(-1)^rK_r(\theta)\). Since the initial readout is zero, all odd ranks vanish at initialization. In particular, order \(2h+1\) and order \(2h\) have identical prediction maps; no symmetry of input slots is used.

The complex extension uses ordinary transposes and is holomorphic. On the prescribed unit block-distance ball, the velocity and derivative bounds are 3150 and 3135. Their products with the disk radius are 0.769043 and 0.765381, so Picard preserves and contracts the ball. The dense coefficient bound has growth factor 0.580535 on the disk, safely below one.

The complex closure map and Lipschitz sums are 0.376470 and 0.188972; the corresponding real bounds are 0.046898 and 0.0234604. All claimed strict bounds hold uniformly in order. Reconstruction supplies every actual finite array, so analytic coefficient existence also gives existence of the prescribed closure ODE.

For the dense path, successive integrations hold the previously selected input vectors fixed while differentiating the next tensor. The remaining \(N\)-fold integral is bounded by

\[
\frac{125}{2}(N+1)(N+2)(10\|b\|T)^N.
\]

Since \(10\|b\|T<1\), this tends to zero. Thus the infinite fixed-point map is the actual dense trajectory. The argument does not assume that a formal tensor series already defines that trajectory.

Parity leaves \(j=2\lfloor q/2\rfloor+1\) as the first potentially nonzero omitted integration index. The stated tail sum and its polynomial prefactor follow by comparison with \(\sum_{\ell\ge0}(\ell+1)^2z^\ell\). The computed product of the tail factor and \(1/(1-L)\) is approximately 1.025025, safely below two. Finally, \((j+1)(j+2)\le4^j\), \(j\ge q\), and \(\|b\|^j\le\|b\|\) give the claimed \(64\|b\|1024^{-q}\) upper bound.

If \(b=0\), the dense initial point is stationary despite possibly nonzero individual labels. The zero coefficient path has zero contracted driving source, is a fixed point of every finite map, and reconstructs a global constant array solution. This includes arbitrary singular \(Q\), canceling labels, and zero input vectors. There is no division by a zero discrepancy in this case.

### 3. Omitted derivative and feedback

For the stated signed data, direct calculation gives

\[
G=\tfrac12(I+\mathbf1\mathbf1^\top),\quad
\bar v=\frac{e_0}{2\sqrt2}+\frac1{m\sqrt2}\sum_a s_ae_a,\quad
\|\bar v\|^2=\frac18+\frac1{2m},\quad b=Y\bar v.
\]

The label RMS and variance match the statement. The population-Gram remark is valid as an initialization second-moment assertion; the proof does not use trained-time Gram invariance.

Conditioning on the first Gaussian image verifies independence and the chi-square law of the second norm ratio. The stated exponential lower tail is valid. Two ratios at least three quarters give squared image norms at least three quarters and nine sixteenths, so the later lower bound of one half holds. This one event controls every order.

Let \(h=2\lfloor q/2\rfloor\) and \(j=h+1\). The finite map contains \(k\le h-1\), while the \(k=h\) initialized tensor is odd and zero. Therefore the infinite-minus-finite map first differs at \(t^j\), with coefficient \(K_{j+1}(v,b,\ldots,b;0)/j!\). If the prediction error is \(O(t^\ell)\), its insertion into any source slot contributes \(-Qe=O(t^\ell)\), and at least one time integration raises the order to \(O(t^{\ell+1})\). Starting from equal initial predictions and iterating this implication gives \(e=O(t^j)\); the own-feedback contribution then begins at order \(j+1\). This proves the claimed leading derivative without replacing either residual by the other.

For source ascent along \(\bar v\), rescaling source time by \(\lambda=\|\bar v\|\) gives the exact system for \(\xi=Bv_*\), \(W\), and \(c\). Differentiating the two asserted invariants verifies both. They yield

\[
c''=(A_0I+W_0W_0^\top)c+2\|c\|^2c,
\qquad A_0=\|\xi_0\|^2,\quad c'(0)=a=W_0\xi_0.
\]

After orthogonal diagonalization and sign choices, each coordinate has a nonnegative initial slope and nonnegative Taylor recursion. Induction therefore gives the coefficientwise comparison \(c_i\ge a_i u\), where \(u''=A_0u+2Hu^3\), \(H=\|a\|^2\), \(u'(0)=1\). The linear term dominates \(A_0a_i u\), and the cubic term dominates \(H a_i u^3\) before the factor two, as required.

Since \(A_0,H\ge1/2\), comparison with \(2\tan(\tau/2)\), whose equation is \(u''=u/2+u^3/8\), is valid. The tangent recurrence gives \(t_k\ge3^{-k}\) because \(3k\ge2k+1\) for \(k\ge1\). Thus the odd coefficients of \(u\) are at least \(12^{-k}\). For \(j=2k+1\), multiplication of \(c\) and \(c'\) gives coefficient at least

\[
H12^{-k}\sum_{r=0}^k(2r+1)
=H(k+1)^2 12^{-k}\ge8^{-j}.
\]

The source output and time rescaling contribute exactly \(\lambda^{j+1}\), not \(\lambda^j\). Since \(\lambda\ge2^{-3/2}\), \(\lambda^{j+1}8^{-j}\ge64^{-j}\) for \(j\ge1\). Contracting the first slot against \(\bar v\) and every source slot against \(Y\bar v\) gives the candidate's \(j!(Y/64)^j\) lower derivative, simultaneously for all finite orders.

### 4. Real-interval transfer

The transfer lemma uses the common complex bound to control the Taylor remainder, so it does not infer real-interval error from a derivative alone. I checked the interval scaling, the endpoint Chebyshev derivative product, and the factorial denominator; they give the displayed polynomial inequality.

\[
|P^{(j)}(0)|\le \frac{2N}{j!}(8N^2/R)^j\|P\|_{[0,R/4]}.
\]

For derivative order \(j\), Taylor degree \(N\), analytic radius \(R\), and derivative scale \(\rho\), put \(\vartheta=\rho R/8\). The Taylor remainder is exactly bounded by the stated geometric tail. Substituting the derivative bound gives the stated first term. Taking logarithms, I independently obtained the following expression for the tail comparison:

\[
j\log(1/\vartheta)+(2j+1)\log N-2\log(j!)+\log(8/3).
\]

Substituting the candidate’s integer degree and its chosen constant bounds this expression strictly below the degree times log four. The factorial lower bound and the elementary bound of an integer by two to that integer then give the exact displayed prefactor and exponential base.

For application to the closure error, \(R=2^{-13}\) is strictly inside the common disk \(R_0=2^{-12}\), so the required neighborhood of the closed radius-\(R\) disk exists. Both coefficients have norm at most one, and \(\lambda\le1\), giving the bound two for \(g_q\). Also \(R/4=T\) and \(\vartheta=Y/2^{22}\). The displayed \(a_Y,b_Y\) consequently agree with the transfer lemma.

### 5. Gaussian upper and lower bounds for the actual discrepancy

The sphere-net matrix estimate is correct: a \(1/4\)-net has at most \(9^d\) points, and a bound three on net images implies operator norm at most four. Exponential Markov with parameter \(4/9\) gives \(e^{-4n}9^{n/2}\); multiplying by \(9^d\) and using \(d\le n\) gives \(e^{-c_*n}\), with \(c_*=4-\tfrac32\log9\approx0.704163>0\). Both matrices, and later both dense copies, are counted in the stated failure probabilities.

The supplied Gaussian semigroup proof is complete: entropy differentiation, weighted Cauchy–Schwarz and integration give the one-half log-Sobolev constant; the exponential substitution gives the stated Gaussian tail. Bounded approximation is justified by Gaussian exponential integrability of functions growing at most linearly. No external concentration theorem is imported.

For two good dense trajectories, \(\|w-\widetilde w\|\le25\) times the sum of their three parameter differences. In each velocity the two direct product differences cost 630 on distinct blocks, while the residual difference costs 625 times the full sum, so 1255 times the sum is a valid per-block bound. Summing gives exponent 3765 in Gronwall. Initially only two blocks differ; their sum norm is at most \(\sqrt2\) times the Euclidean norm of the entries. Thus \(50e^{4000T}\) safely bounds the query Lipschitz constant. The extension agrees with the original function on the good set. Each independent initialization has the same extension mean, so the pair difference is controlled without needing to identify that mean.

The variance scaling, sphere net, and time grid produce exactly the stated dimension and logarithmic dependence. Each path has speed below 250000, so the pair’s grid error is at most 500000 divided by width. The result controls the actual dense paths, without requiring their mean to be identified.

For the lower discrepancy estimate, the initial derivative along \(v_*=b/\|b\|\) is exactly \(\|b\|H\), with \(H=UV\) and independent \(U,V\sim\chi_n^2/n\). The gamma density's mode is \(u_0=1-2/n\). For \(n\ge4\), its log second derivative on \([u_0,u_0+n^{-1/2}]\) is at least \(-2n\), so its supremum is at most \(e\sqrt n\). Also \(\mathbb E(V^{-1})=n/(n-2)\le2\). Product-density integration and then convolution give \(\|p_{H-\widetilde H}\|_\infty\le2e\sqrt n\), hence probability at most \(4e/\sqrt n\) for absolute difference at most \(1/n\).

The density argument is unconditional. Intersecting the resulting event with the matrix-norm event afterward avoids any invalid conditional anti-concentration inference. On the latter event, Cauchy's second-derivative bound is exactly \(2^{30}\|b\|\). At \(t_n=1/(2^{30}n)\), which lies in the physical interval for every \(n\ge4\), Taylor's integral remainder gives

\[
|g(t_n)|\ge \frac{\|b\|}{2^{30}n^2}
-\frac{\|b\|}{2^{31}n^2}
=\frac{\|b\|}{2^{31}n^2}.
\]

This supplies the actual path discrepancy and justifies the comparison with approximation error, even when \(\|b\|\) is arbitrarily small and nonzero.

### 6. Quantifiers, minimum sizes, and boundaries

Combining the geometric error with the dense-pair lower bound gives \(E_n(q)/D_n\le2^{37}n^2 1024^{-q}\) on the stated event. The chosen \(q_n\) therefore gives \(E_n(q_n)\le D_n/n\). For \(n\ge4\), this order is at least two. For any fixed \(A>0\) and \(p<1\), sufficiently large width makes \(1/n\le A\) and the event probability at least \(p\). Thus the minimum defining \(S_n(p,A)\) is over a nonempty set at those widths.

For the hard family, the same event gives \(E_n(q)\ge a_Ye^{-b_Yj}\) for every \(q\). The dense upper bound holds on a separate event whose intersection still has probability tending to one. Writing \(R_n=n/(m+\log(en))\), an order at most \(\log R_n/(4b_Y)\) has error at least \(a_Ye^{-b_Y}R_n^{-1/4}\), while the actual dense discrepancy is at most \(CR_n^{-1/2}\). The ratio diverges uniformly because \(m\le\sqrt n\). Consequently every such order fails the prescribed accuracy simultaneously on that event. This proves a necessary order of size \(\log n\), rather than merely failure of each fixed order separately.

The same uniform event handles any initialization-dependent order selector constrained by a deterministic budget: a budget small enough to allow only these orders cannot select a successful order on that event. This does not assert a lower bound for arbitrary data-dependent representations, random unbounded budgets, bit complexity, or coefficient-generation work.

For literal arrays, first-slot count is \(m+d\), later slots have \(m\) choices, and ranks range exactly as in the two formulas. For \(m\ge2\), geometric summation gives the displayed upper counts. With \(d=m+1\), \(2(m+d)m^{q-1}\le5m^q\). An odd zero top can be dropped, but its preceding rank still supplies \(m^{q-1}\) training entries; even after recognizing that preceding rank as frozen, lower moving ranks supply at least \(m^{q-2}\) entries. The coarser lower estimates used in the proof are valid for both parity conventions. Subtracting one or two from an order growing proportionally to \(\log n\) does not affect the exponential order. The retained dataset cost does not change either inequality.

Uniformly for \(4\le m\le\sqrt n\), \(\log R_n\) lies between fixed positive multiples of \(\log n\) for sufficiently large \(n\). Thus the constants in the exponent can depend only on fixed \(Y\); fixed \(p,A\) change the width threshold. The special growing sequence \(m=4\lfloor n^a/4\rfloor\) obeys the range eventually and has \(\log m\sim a\log n\), proving the displayed squared-log exponent. For fixed \(m,d\), the upper bound is polynomial in width, as stated.

I also checked the boundaries \(m=1\), \(q=2\), odd \(q\), zero inputs, canceling labels \(b=0\), singular \(Q\), and \(n=4\). For \(m=1\), the separate array formulas replace the geometric bounds correctly. The probability lower bound can be negative at small width and then is merely vacuous, not false. The hard family begins at \(m=4\), which implies \(n\ge16\), so \(d=m+1\le n\) automatically. No step needs a Gram gap, positive label mean in the general upper bound, or a uniform event over every possible deterministic dataset. The prohibition on such a simultaneous dataset interpretation is correctly explicit.

## Deterministic calculations and their outcomes

The standard-library exact-arithmetic script is `data/generated/nth_lower_bound_20261010/promotion_review_b_v1/exact_checks.py`; its complete output is in `exact_checks.txt`. I ran it with `python .../exact_checks.py`. A preliminary attempt to use SymPy failed because that package is unavailable; I replaced it with explicit polynomial dictionaries and rational Taylor arithmetic, with no dependency installation.

1. **Scalar own-feedback attack.** With scalar initial \(B=W=1,c=0\), the computed initialized ranks 1 through 11 are \(0,1,0,8,0,136,0,3968,0,176896,0\). The full dense training ODE and the finite closure ODEs, each with its own residual \(1-f\), were expanded through degree nine. Orders 2 and 3 first differ from dense at degree three by \(4/3\); orders 4 and 5 at degree five by \(17/15\); orders 6 and 7 at degree seven by \(248/315\). These equal the respective \(K_{j+1}(0)/j!\). Neighboring even/odd closure predictions agree exactly through degree nine. All assertions passed. This is a deterministic check of the algebra, not an empirical substitute for the all-order argument.

2. **Chronological-order attack with noncommuting source slots.** I used one hidden coordinate, two input coordinates, initial \(B=(1,2),W=1,c=0\), and external source \(a(t)=e_1+t e_2\). Here \(K_4(e_1,e_1,e_1,e_2)=16\) while \(K_4(e_1,e_2,e_1,e_1)=10\), so symmetrizing or reversing slots is a real change. Exact simplex integration with the candidate's latest-time-first order agrees with the direct parameter ODE through degree seven. Reversing the order fails already at degree four: the actual coefficient is \(35/12\), whereas the reversed convention gives \(41/12\). This directly challenges and supports the candidate's most order-sensitive reconstruction step.

3. **Constant checks.** The script evaluates \(c_*\), both complex contraction sums, both real contraction bounds, the tail multiplier, both Picard constants, and the dense growth factor. Every claimed strict inequality holds; the numerical values are recorded above and in the output. Their use in this review supplements the analytic inequalities rather than replacing them.

## Scope and completion

The candidate proves matched necessary and sufficient retained size for a specified literal tensor representation, a deep-linear network with all three parameter blocks trainable, zero initial readout, fixed nonzero \(Y\), and a fixed very short physical interval. Its comparison scale is the random discrepancy of two actual dense initializations. It neither imports the compression chapter's fixed-data/small-label hypotheses nor establishes a same-family separation from a compressed representation. It also makes no arbitrary-encoding, nonlinear-activation, long-time, finite-precision, or coefficient-generation complexity claim.

All assigned scientific components and all supplied proof/dependency bodies have been reviewed. No scientific dependency was missing, no required correction remains, and no objection is reserved for a later round. The optional observation about making the initialization meaning of the population-Gram sentence explicit is editorial only and is not needed by any proof or conclusion. **Final scientific verdict: PASS on the exact frozen hashes above.**


## Authorized format-only v2 correspondence check

After the independent scientific audit, the coordinator supplied a technical build note identifying six Quarto proof wrappers and authorized inspection of the format-only v2 candidate and `PROMOTION_FORMAT_v1_v2.diff`. No scientific finding or other reviewer conclusion was shared. I read that diff and independently compared the full candidate bytes, without using the diff as a substitute for comparison.

The exact regular-expression transformation replaces each line of the form `::: {#proof-... .proof}` with the same identifier in `[]{#proof-...}`, a blank line, and `::: {.proof}`. There are exactly six replacements. Applying this transformation to frozen v1 gives byte-for-byte frozen v2; reversing the transformation gives byte-for-byte v1. Thus there is no mathematical or prose change in any scientific line. The v2 candidate SHA-256 is `e8c8cbd7474b9e0bbaded9100ce02474708339f9ac95cf606de7b93886616d23`. All three original v1 scientific-input hashes were also recomputed and remain unchanged.

The complete scientific audit remains a review of frozen v1 and its supplied dependencies. Its PASS applies to the scientifically identical v2 content by this exact correspondence check. I did not independently run the complete book build or certify integration; those remain separate gates.
