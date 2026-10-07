# Independent bounded check of the two small-memory routes

2026-10-06. Fresh isolated check of the two frozen candidates identified
below. This is not a promotion review, a check of the inherited stochastic
source/fitting theorems, or a proof of the efficient unseen-query decoder.

## Verdict and boundary

No blocking mathematical objection was found in the new scoped lemmas at
the frozen hashes. The conditional Gaussian mean and variance, cosine
initial-velocity bias, scalar convolution rule, signed selected-row lower
bound, causal positive-response realization, complement return identity
and estimate, compatibility identity, and actual tanh/identity example
are correct under their stated conditions and the ordinary regularity
conventions noted below.

The candidates do not establish the requested whole-sphere, all-time
decoder with exponent-five memory and efficient acquisition/evaluation.
Their closing qualifications are necessary and correctly distinguish that
open statement from the proved lemmas. In particular, neither example is
an impossibility theorem for every admissible decoder.

The inherited analytic/source/fitting interface is conditional in this
check. The full original label allowance was preserved as an interface;
the linked definitions outside the permitted inputs were not opened or
reproved. The examples can use a fixed positive label inside the explicit
sufficient subrange displayed in the permitted finite-panel result. No
strengthening of the target label restriction is needed for the elementary
lemmas.

## 1. Conditional Gaussian action

For deterministic orthogonal projections, the observed matrix in panel
equation (1) is exactly

\[
 M=W-(I-P_U)W(I-P_V).
\]

After deterministic orthogonal changes of row and column bases, the four
rectangular blocks have independent centered Gaussian entries. The
observations determine three blocks, so the fourth retains its original
law independently of the observation sigma field. For measurable finite
\(h,b\), conditioning fixes both vectors. The omitted action consequently
has covariance

\[
 \frac{\|(I-P_V)h\|_2^2}{n}(I-P_U)
       =\tau^2(I-P_U).
\]

Its coordinate variances are exactly
\(\tau^2[1-(P_U)_{ii}]\). This verifies panel (4), including the
absence of any requirement that different residual coordinates be
independent.

The rotation argument gives
\(\operatorname{Var}F(g)\le(\pi^2/8)\mathbb E\|\nabla F(g)\|_2^2\):
the difference of independent copies contributes the factor two, the
integration interval has length \(\pi/2\), and its tangent Gaussian is
independent of the point on the rotation. Here

\[
 \nabla F(g)=\frac{\tau}{n}(I-P_U)
   \{b\odot\phi'(z+\tau(I-P_U)g)\}.
\]

Projection contraction and the derivative bound give precisely panel
(5). Chebyshev then gives (6), with coefficient
\(\pi\tau B_1\|b\|_2/(\sqrt{8\delta}\,n)\). The centered
linear term in Taylor's formula vanishes, and the second derivative
remainder gives (7) with the stated factor \(1/2\).

The degenerate cases are consistent. If \(h\in V\), the entire
conditional error vanishes. If \(U=\mathbb R^n\), it also vanishes
even when \(\tau>0\). If the activation is affine and \(b\in U\),
the first, sharper variance bound is zero. Bounded derivatives allow
unbounded activation values by linear growth.

These statements do not justify conditioning on spaces selected using
the omitted entries of \(W\). Conditioning on independent randomness
that fixes the spaces is valid; an arbitrary adaptive training transcript
needs an additional argument. The candidate explicitly retains that gap.

There is one harmless measure-theoretic convention to make explicit when
reusing this lemma: finite measurable \(h,b\) need not give globally
integrable \(X\). The displayed conditional moments are finite Gaussian
kernel integrals for each realized \(h,b\), equivalently conditional
moments after localization to bounded \(h,b\). If ordinary integrable
random-variable conditional expectations are intended instead, impose
the corresponding unconditional moment assumption. No global moment
bound is used by the candidate's pointwise conclusion or its bounded
cosine example.

## 2. Actual cosine initial bias

With the stated independent standard-Gaussian first columns, the limiting
first-layer training Gram and query cross-moment vector are

\[
 \begin{pmatrix}q&c\\c&q\end{pmatrix},\qquad
 \begin{pmatrix}b_0\\b_0\end{pmatrix},
 \quad q=(1+e^{-2})/2,\quad c=e^{-1},\quad
 b_0=e^{-1}\cosh(1/\sqrt2).
\]

The squared projection norm is therefore
\(p=2b_0^2/(q+c)\). Since \(q-c=(1-e^{-1})^2/2>0\), inversion
is continuous near the limiting Gram. The residual \(\rho^2=q-p\)
is strictly positive: an exact two-cosine representation would, after
setting the second Gaussian coordinate to zero, force its first cosine
coefficient to be both \(1/2\) and \(1/4\) by the second and fourth
derivatives at zero.

Conditionally on \(A,BH\), the omitted action is a vector of independent
\(N(0,\rho_n^2)\) variables. The cosine mean identity gives the
exact damping factor in panel (10); each bounded summand has variance
at most one, giving the variance bound \(1/n\). Separately, conditioning
only on \(A\) gives the displayed mean of the projected cosine product
and another conditional variance bound \(1/n\). These facts and the
bounded first-layer laws of large numbers prove the positive probability
limit (12).

The MSE/readout-mobility factors are correct: at zero readout,
\(\dot w(0)=(2/m)\sum_a y_a h_a^{(2)}\), so for \(m=2\) and
\(y=(\varepsilon,0)\), the query velocity is exactly
\(\varepsilon K_n\). The top population training Gram has the stated
diagonal and off-diagonal entries and a positive gap. Cosine meets the
strip assumptions. Any bounded convention on the vanishing-probability
singular-Gram event leaves the probability limit unchanged.

The conclusion concerns omission of this conditional-mean correction at
initial velocity. Multiplication by \(e^{-\rho_n^2/2}\) removes the
conditional bias exactly. Neither an all-time output lower bound nor a
lower bound for all selected networks follows; the candidate says so.

## 3. Scalar convolution and numerical count

All explicit constants in panel (13) are sufficient. Write
\(A_0=|\phi(0)|+B|z|\), so \(C_0=1+A_0+B\sigma\).
For the shifted integration lines, \(s\le1\) and
\(\sigma s\le a/2\), and linear growth gives

\[
 \int_{\mathbb R}|F(u\pm is)|\,du
 \le e^{s^2/2}
   \left[A_0+B\sigma s+B\sigma\sqrt{2/\pi}\right]
 <4C_0.
\]

The shifts lie inside the holomorphy domain, including when
\(\sigma s=a/2\). Gaussian decay controls the vertical contour sides.
The Fourier bound and absolutely convergent periodization therefore give
the asserted infinite trapezoid identity and error bound. Since
\(D\ge\log128\),

\[
 16C_0e^{-2\pi D}<\epsilon/4,
 \qquad 4C_0e^{-8D}<\epsilon/4.
\]

For the second inequality, the two deleted lattice tails are bounded by
the tail integral starting at \(Jh\ge R\); the real envelope
\((1+u)e^{-u^2/2}\) is decreasing there. Thus the exact arithmetic
error is smaller than \(\epsilon/2\), leaving the claimed numerical
slack. The node count is
\(2J+1\le8D^{3/2}/s+3\). Sequential summation uses a constant number
of scalar registers beyond the activation evaluator and precision
storage. The total positive weight is at most
\(1+h/\sqrt{2\pi}<2\), so activation errors of \(\epsilon/8\)
produce at most \(\epsilon/4\) output error.

The stated logarithmic allowance for weight/summation precision is
consistent with bounding every summand by \(C_0(1+R)\) and allocating
absolute error to each operation. Argument formation separately needs
\(B\) times the argument error to fit the same budget, as the candidate
explicitly requires. Its cost must include the input representation and
actual evaluator at that accuracy. There is no uniform evaluator-time
claim for arbitrary analytic activations. The case \(\sigma=0\) is
handled separately and avoids division by zero; \(B=0\) also causes
no problem.

The \(O(\log^{3/2}n)\) scalar-call statement requires bounded
\(s^{-1}\), not just logarithmic \(D\). If the variance grows or
the strip narrows, \(s^{-1}\) remains an explicit additional factor.
The candidate preserves that condition. Multiplication by the proposed
selected-row count is conditional on a uniform weak quadrature which
has not been established.

## 4. Signed selected-row lower bound

The even products \(\prod_{k\in S}a_k\) form all \(N=2^{r-1}\)
characters on the antipodal quotient of the hypercube. For distinct even
sets their product is a nonempty even character, and its quotient sum is
zero. Their squared character matrix is consequently \(NI_N\).

Merging duplicate or antipodal selected rows gives signed weights \(p\)
with support size at most \(q\) and total mass one. Cauchy--Schwarz
uses no positivity and gives \(\sum_i p_i^2\ge1/q\). The constant
character equals one; every other character has true uniform mean zero
and selected mean at most \(e^{\sigma^2/2}\epsilon\) in absolute
value. Parseval therefore gives

\[
 \frac Nq\le N\sum_i p_i^2
 \le 1+(N-1)e^{\sigma^2}\epsilon^2,
\]

which is exactly (15). An empty selected rule is excluded by its required
unit mass. For zero error the inequality forces \(q\ge N\); for large
error it may give only a trivial bound. A symmetric non-diagonal metric
with exact constant isometry has effective weights \(M\mathbf1\)
and the required unit mass, so the stated application is valid.

For fixed \(\sigma\) and \(N\epsilon^2\) large, this *lower bound*
has order \(\epsilon^{-2}\). It is not an upper bound or a proof of
an optimal node complexity. The exponential fixed-\(r\), vanishing-error
limit is also a necessary bound for this representation. Neither
reachable neural signatures nor arbitrary neural decoders are covered.
The candidate's final scope statements correctly make both distinctions.

## 5. Causal positive response and complement memory

Substitution of the response ODE for \(Z\) into \(I+BZB^T\) gives
exactly the Gauss--Newton generator and initial identity. No inversion
or full column rank of \(B\) is needed. Appending columns and padding
\(Z\) with zero blocks leaves the represented current operator
unchanged; the next interval's ODE then evolves the full current
correction, including its action on appended directions. This verifies
the stated absence of replay for the supplied representation.

The arithmetic count follows from three matrix products of cost
\(O(mr^2)\); the retained arrays cost \(O(r^2+rm)\). These are
counts for supplied Gram/coefficient/boundary data, not for retaining a
dense parameter-by-\(r\) array or acquiring its neural contractions.
The candidate explicitly makes the acquisition conditional. A dependent
basis is allowed, but contractivity of the represented operator does not
give numerical conditioning of its coefficients.

For the supplied-matrix statements, the ordinary finite-dimensional ODE
regularity convention is needed: for example continuous coefficients,
or local integrability of the generators, suffices. Actual smooth neural
trajectories satisfy it on every interval of existence. Arbitrary
nonmeasurable coefficient functions would not be an admissible ODE
input. This is a regularity clarification, not a failed identity.

Projection of the full response equation gives the two coupled equations
in response Section 3. Solving the complement equation with zero initial
complement and substituting it back gives a positive factor four and
exactly the ordered kernel (8). No commutation of its time-dependent
factors has been used.

For the leakage bound, the off-diagonal insertion norm is
\(2\|Q\mathcal H P\|\) by self-adjointness. Every block-diagonal
propagator segment is bounded by its curvature exponential; the
nonpositive Gauss--Newton contribution can be discarded in the squared
norm derivative. The segments cover disjoint time intervals, so their
product has bound \(e^{M(t)}\). A term returning from \(P\) to \(P\)
has an even number of off-diagonal insertions. Their ordered integrals
are bounded by \(\Lambda(t)^k/k!\), proving (9) with its precise
\(\cosh\Lambda-1\) factor. The comparison is on the range of \(P\),
or equivalently after extending \(U_P\) by zero off that range.

The sufficient condition for error \(\varepsilon\) is correct because
\(\cosh\Lambda-1<\Lambda^2\) for \(0<\Lambda\le1\). With
\(M=O(\sqrt{\log n})\), it requires a sufficient scale
\(\Lambda\le n^{-1/4+o(1)}\) for a near-root response error. The
estimate \(\Lambda\le M\) supplies no such decay. This is a
sufficient certificate and cannot be inverted to prove a necessary
leakage threshold.

The two-dimensional constant-operator example has exact return kernel
\(4b^2P\) and second-order discrepancy \(2b^2t^2P\). The candidate
correctly excludes its use as an actual one-sample neural trajectory,
whose Jacobian must satisfy the additional compatibility equation.

## 6. Compatibility and the actual nonlinear example

Along \(\dot\theta=-2\sum_a e_a\mathcal J_a\), differentiation
gives \(\dot{\mathcal J}_b=-2\sum_a e_aD\mathcal J_b\mathcal J_a\).
Adding and subtracting the reversed derivative term proves response
(11) with the stated sign of \(C_*\). Next,

\[
 \partial_t(\mathcal J R)
 =-2(\mathcal J\mathcal J^T+\mathcal H)\mathcal J R
       +2C_*R.
\]

Variation of constants yields exactly (12), including the minus sign
on its correction. Contractivity of \(R\) and the curvature bound for
\(U\) give (13). For one sample the bracket vanishes identically.
This transports training-gradient directions only; it does not give
arbitrary query-boundary contractions.

At zero readout in the stated tanh/identity model, only the readout
block of \(\mathcal J_a\) is nonzero, and it is
\(h_a^{(2)}/\sqrt{mn}\). Applying this direction to
\(\nabla_W e_a=w h_a^{(1)T}/(n\sqrt m)\) gives precisely (14).
No derivative of a first-layer feature contributes to that block at
zero readout. Independence and oddness of tanh give the first-layer
Gram limit \(qI_2\). Conditional Gaussian second moments give the
same second-layer limit, with variance controlled uniformly by bounded
first-layer normalized norms. The Frobenius identity then proves the
limit \(2q^2/m^2\) in (15).

The norm of the \(W\) block of \(C_2\) tends to
\(\eta\sqrt2 q/(m\sqrt m)=\eta q/m\), where the last equality
uses the specified \(m=2\). Thus there is no missing normalization
factor. The population training-feature gap is \(q>0\), and the
inputs span the input space. A common strip strictly inside the tanh
poles gives the required derivative bounds; the identity activation is
allowed despite its unbounded values.

The physical equations independently give the two stated initial
derivatives of \(w\) and \(W\), and

\[
 \ddot A(0)v_1=\frac{4\eta^2}{m^2}
       \tanh'(Av_1)\odot W^Th_1^{(2)}.
\]

Since \(\dot A(0)=\dot W(0)=0\), differentiating the feature twice
gives the displayed strictly positive inner product in response
Section 6. Its first term is already positive almost surely. Therefore
the example has actual hidden feature motion and a nonvanishing initial
bracket source. It does not provide a positive lower bound for the
time integral on a width-independent interval or prevent compact
retention of the brackets. Those limits are stated correctly.

The word recurrence in Section 7 is a causal recurrence for scalar
ordered-integral weights, initialized at the lower endpoint of the
chosen interval. Factors \((-2)^k\) from the complement generator
must be included in the Dyson sum; they do not affect the count.
The displayed \(D,K\) bounds permit polynomially many words and do
not guarantee polylogarithmic enumeration. Upper \(O\)-bounds alone
are not a lower bound on the necessary word count. The candidate
explicitly does not assert such a lower bound or the needed operator
approximation theorem.

## 7. Complete read coverage and provenance

The neutral assignment, both complete frozen candidates, and all four
permitted scientific dependencies were read. No linked scientific inputs,
study README/history, independent review reports, other agents' findings,
archive, experiments, or Git state were accessed. Provenance paragraphs
inside permitted inputs were not treated as verification evidence.

| Complete input | Lines | SHA-256 |
|---|---:|---|
| `SANE_PANEL_EXTENSION.md` | 546 | `8d570909d6431a2cca7f3c8456eb03344de62c7d12e4eb6bc880300d43d317b6` |
| `SANE_RESPONSE_MEMORY.md` | 446 | `de3407f4b7dac4e594b58ff261a65fd84cafa9a4c78437ce2240a9e653df7322` |
| `docs/notation.qmd` | 98 | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `EFFICIENT_QUERY_DIRECT.md` | 528 | `8a027e2e2b92f538aecf2bde4fc305e9f064fd3f32cea0364b8e9b11331f840b` |
| `COST_CONTRACT.md` | 321 | `3e29f96ef535ec58dc6b70bcdbd304ea6e9074579ad7652c9f377f15c948d03c` |
| `studies/finite_panel_absolute_compression_20261005/RESULT.md` | 506 | `38ca06a2e812d8e2b45c6b7350c0437d710433b11a00b89aa66487a9229b028b` |

Unqualified filenames in this table are in the current study. The two
candidate hashes agree with the assignment's frozen hashes.

The complete `solve-math-rigorously` and `investigate-conjectures` skills
and the latter's complete `research-contract.md` and
`adversarial-audit.md` references were read and applied. The required
canonical-notation skill returned OS `Permission denied`; its linked
neural reference was therefore unavailable. The assignment's authorized
fallback used the explicit user/repository mathematical requirements and
the complete maintained notation contract. No external theorem retrieval
was needed: all new checks above are elementary derivations from the
permitted definitions.

Only this assigned report was written. The scope supports an internal
bounded check of the stated lemmas; it does not certify promotion or close
any of the remaining decoder acquisition, uniformity, precision, or
prediction-transfer obligations.
