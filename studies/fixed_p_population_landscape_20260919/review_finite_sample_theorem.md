# Informed internal review of the finite-sample theorem

2026-09-19. **Verdict: PASS for the theorem and explicit canonical sample bound as stated. No mathematical correction is required.** The unrestricted fixed-order question, with arbitrary sample count at that same order, remains outside the proved conclusion.

## Provenance and exact inputs

This is an explicitly informed internal review, not an isolated review or a promotion review. I previously authored dictionary_route.md and dictionary_counts.md and discussed those findings with the lead. The candidate also discloses a post-freeze contribution of its equal-dimension case from another route author. I did not read abstract_route.md or obtain its proof. The present verification uses the displayed candidate argument, the stated count proof, and the assigned exact-model book sections; no external Lyapunov/vector-measure theorem is a premise.

The complete frozen candidate and count file were read:

| Input | SHA-256 |
|---|---|
| finite_sample_theorem.md | 5242bfda61ed94f2e5bda83b8843fe713d37dcbf4b7e2f204dc1ba8c23757c24 |
| dictionary_counts.md | 87ddaf612ff335f0829a9cc5103c74022786dfec04de4bc9749800319c1fa804 |

Established scientific inputs were the previously assigned complete sections C.4.7.9.2–4 and C.4.7.10.B, C.1, D.3 of docs/global_nonlinear.md, together with docs/NOTATION.md. Current full-file hashes are:

| Source file | SHA-256 |
|---|---|
| docs/global_nonlinear.md | 81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |

Prior reviewer-authored background, already known before this review: dictionary_route.md, SHA-256 a95512882aa16474e6f6bd9ad0d4a88e3d9499d2b6976191188e4fa752079c53. Its derivative-separation and parity obstructions are not premises of the candidate theorem.

Only this review report was written during the review; the candidate remained frozen.

## 1. Model, topology, and differential identities

The theorem uses the stated canonical contraction map with the full fixed mark columns, an unrestricted coefficient matrix, and its actual transpose. It uses the unhalved, positive probability-weighted square loss. The factors of two in the finite-moment, matrix, and readout derivatives are consistent.

The loss is finite at every admitted state: bounded lower marks and activation give finite \(a_i\); bounded upper marks give bounded \(z_i,H_i\); and \(c\in L^2\) on a probability space implies \(E|c|<\infty\). For fixed \(c,M\), differentiation twice in the finite array \((a_i)_i\) is justified by bounded upper marks and bounded activation derivatives. Thus the locally uniform quadratic remainder used in section 3 requires no extra moments of \(w\) or \(c\).

The theorem is about local minima on the full \(L^2/L^2/\)Frobenius product space. Every displayed change is admissible in precisely that space. It does not assume that a local minimum or a comparison state is reached by the prescribed initialization. This ambient-state distinction is explicit and matches the claimed landscape conclusion.

## 2. Input ridge independence

For distinct non-antipodal unit inputs, all vectors defining the excluded hyperplanes are nonzero. Their finite union cannot cover \(\mathbb R^d\), including the case \(d=1\), in which there is at most one unoriented input direction. The selected projections are nonzero with distinct squares.

The tanh coefficient recurrence is correct:

\[
 (2n+1)a_n=\sum_{j+k=n-1}a_ja_k>0,\qquad a_0=1.
\]

Dividing each odd-order derivative identity by its nonzero common coefficient gives the stated Vandermonde system. Thus no unasserted linear independence of the input vectors is used. Normalizing \(x_i\) by \(\sqrt d\) is consistent with the book's input convention.

## 3. The local population-subset argument

This is the key step and is valid. If \(w(\omega)\) fails to globally minimize \(F_\omega\) on a positive-measure set, continuity in the comparison vector, countably many rational comparison vectors/margins, and the sets \(\{|w|\le R\}\) yield a single comparison vector, a uniform strict loss margin, and a finite \(w\)-bound on a positive-measure subset.

Nonatomicity supplies arbitrarily small positive-measure subsets. Only the scalar nonatomic property is needed: repeatedly split a positive-measure set and retain the smaller positive piece to obtain measures tending to zero. No exact vector-moment splitting is used.

On a subset of measure \(\varepsilon\), the replacement has squared \(L^2\) displacement \(O(\varepsilon)\), while every moment change is \(O(\varepsilon)\) because the marks and activation are bounded. Therefore the strictly negative linear loss change is of order \(\varepsilon\), and the finite-moment Taylor error is \(O(\varepsilon^2)\). This proves the claimed almost-sure global minimization condition without a stronger topology.

The expectation identity using matrix stationarity has the correct factor \(1/2\). Since \(F_\omega(w)\le0\), its zero expectation gives \(F_\omega(w)=0\) almost surely. Global minimality then gives \(F_\omega(s)\ge0\) for every \(s\); oddness gives the reverse inequality. Ridge independence yields each coefficient in equation (6). Positive sample weights justify dropping their factors.

For the canonical lower carrier, the retained Gaussian coordinate \(g_1\) has no atoms. For any measurable set \(B\), the map \(t\mapsto P(B\cap\{g_1\le t\})\) is continuous, since its jumps are bounded by \(P(g_1=t)=0\). This verifies the needed nonatomic subdivision even when \(B\) depends on all other marks and on the current field.

## 4. Prediction-preserving matrix changes

The effective lower coefficient space \(B_1\) is the orthogonal complement of the mark Gram nullspace, has dimension \(q_1\), and contains every \(a_i\). A nonzero vector in \(B_1\) has strictly positive mark variance \(E(b_1^Tq)^2\), regardless of coordinate redundancies.

When \(\operatorname{rank}A<q_1\), the chosen null direction exists and the rank-one change leaves every \(Ma_i\) unchanged exactly. It therefore preserves all quantities claimed in section 4. For a local-minimum ball of radius \(\rho\), any equal-value state strictly inside that ball is itself a local minimum, using a smaller ball of radius less than its distance to the boundary. The Frobenius distance of the change is \(|t||z||q|\), which can be made arbitrarily small. Subtracting equation (6) and using positive mark variance proves \(r_id_i=0\).

If this rank-deficient case fails, then

\[
 q_1=\operatorname{rank}A\le m\le q_1,
\]

so all three numbers coincide. A right inverse of \(A^T\) exists; explicitly it is \(A(A^TA)^{-1}\). Multiplying matrix stationarity by that right inverse proves the same conclusion. This checks the edge case \(q_1=m\) and removes any need to assume a strict dimension surplus in the abstract theorem.

## 5. Readout-null changes and upper effective dimension

If the loss is positive, readout stationarity supplies a nontrivial relation among the \(m\) upper features, so their span \(H\) has dimension at most \(m-1\), including when some features are identically zero.

Every \(k\in H^\perp\subset L^2\) defines an admissible perturbation \(c+tk\). For sufficiently small nonzero \(t\), its predictions and loss are unchanged and the perturbed state is again a local minimum. The allowed size of \(t\) may depend on \(k\); the argument only needs each direction separately. Subtracting equation (8) for any fixed nonzero-residual sample gives equation (9) for every such \(k\).

Each coordinate of \(b_2\phi'(z_i)\) belongs to \(L^2\). Orthogonality to every vector in \(H^\perp\) places it in the closed finite-dimensional space \(H\). Multiplication by \(\phi'(z_i)=\operatorname{sech}^2(z_i)>0\) is injective on the effective upper mark span, so the resulting image has dimension exactly \(q_2\). This argument uses effective dimension, not raw column count, and survives every linear redundancy. In fact \(z_i\) is bounded at a fixed state, so its gate is bounded away from zero, although injectivity alone suffices. The contradiction \(q_2\le m-1<q_2\) is valid.

No upper nonatomicity, upper-support density, mark-parity assumption, positive readout Gram lower bound, or polynomial-only replacement is used.

## 6. Counts, attainment, and observation identities

The canonical count proof retains the full word tail. Polynomial-core independence gives \(q_1\ge\binom{p+4}{4}\) and \(q_2\ge\binom{p+2}{2}\), while the upper tail contains at most \(p+1\) appended code entries. For \(p\ge2\), the displayed subtraction

\[
 \binom{p+4}{4}-\binom{p+2}{2}-(p+1)
 =\frac{p+1}{24}[p(p+2)(p+7)-24]
\]

is correct and positive. At \(p=1\), both code-prefix constants are already present, and the exact dimensions are \(5,3\). Positive-ridge normalization preserves each span. Thus the full canonical hierarchy satisfies the dimension hypotheses whenever \(m\le\binom{p+2}{2}\).

The canonical attainment construction is valid even beyond this sample bound. The lower constant implies \(E b_1\ne0\); the upper core coordinate \(X=\tanh\xi_1\) has positive density on \((-1,1)\). Almost-sure relations among \(\tanh(t_iX)\) become identities on that interval by continuity, and the same Taylor/Vandermonde calculation makes the corresponding Gram positive definite. The finite linear combination used for \(c\) is bounded and fits every specified label. The entire fixed dictionary remains present.

The repeated/antipodal grouping identity is the weighted scalar variance decomposition applied to signed labels. Its constant \(C\) is nonnegative and is zero exactly for within-group sign compatibility. The grouped weights stay positive and sum to one; representatives satisfy the needed input separation. Applying the theorem to the grouped loss therefore gives global loss \(C\) under the grouped sample bound. No extra input identities arise from ordinary linear dependence among distinct non-antipodal directions.

## Scope of the verdict

PASS certifies this internally reviewed finite-sample proof and the accompanying full-dictionary count. It does not certify the stronger arbitrary-\(m\), fixed-\(p\) conjecture, convergence of training to a minimizer, a fitting rate, a finite-particle analogue, or promotion into established material. No required correction was found in the frozen candidate.
